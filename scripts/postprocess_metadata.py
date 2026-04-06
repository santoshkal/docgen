#!/usr/bin/env python3
"""
Post-process multilspy document_symbols metadata to reconstruct:
  1. Hierarchical containment (class → methods/fields) from line ranges
  2. Enriched intra-file structure with parent-child relationships
  3. Aggregated project-wide symbol index

Reads:  ./metadata/document_symbols/*.json
Writes: ./metadata/enriched/
          ├── per-file/              — enriched per-file symbol trees
          ├── symbol_index.json      — flat index of all symbols with parents
          ├── class_index.json       — classes with their members
          ├── containment_stats.json — statistics
          └── intra_file_graph.json  — edges: parent → child (all files)

Usage:
    python postprocess_metadata.py [--input ./metadata] [--output ./metadata/enriched]
"""

import argparse
import json
import os
import sys
from pathlib import Path
from collections import defaultdict


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
KIND_NAMES = {
    1: "FILE", 2: "MODULE", 3: "NAMESPACE", 4: "PACKAGE",
    5: "CLASS", 6: "METHOD", 7: "PROPERTY", 8: "FIELD",
    9: "CONSTRUCTOR", 10: "ENUM", 11: "INTERFACE", 12: "FUNCTION",
    13: "VARIABLE", 14: "CONSTANT", 15: "STRING", 16: "NUMBER",
    17: "BOOLEAN", 18: "ARRAY", 19: "OBJECT", 20: "KEY",
    21: "NULL", 22: "ENUM_MEMBER", 23: "STRUCT", 24: "EVENT",
    25: "OPERATOR", 26: "TYPE_PARAMETER",
}

# Kinds that act as containers (can have children)
CONTAINER_KINDS = {3, 5, 10, 11, 23}  # NAMESPACE, CLASS, ENUM, INTERFACE, STRUCT


# ---------------------------------------------------------------------------
# Range helpers
# ---------------------------------------------------------------------------
def get_start_line(sym: dict) -> int:
    """Extract start line from a symbol's range."""
    r = sym.get("range") or sym.get("selection_range") or {}
    return r.get("start", {}).get("line", -1)


def get_end_line(sym: dict) -> int:
    """Extract end line from a symbol's range."""
    r = sym.get("range") or sym.get("selection_range") or {}
    return r.get("end", {}).get("line", -1)


def contains(parent: dict, child: dict) -> bool:
    """Check if parent's range fully contains child's range."""
    p_start = get_start_line(parent)
    p_end = get_end_line(parent)
    c_start = get_start_line(child)
    c_end = get_end_line(child)

    if any(v == -1 for v in [p_start, p_end, c_start, c_end]):
        return False

    return p_start <= c_start and p_end >= c_end


# ---------------------------------------------------------------------------
# Core: reconstruct hierarchy from flat symbols using range containment
# ---------------------------------------------------------------------------
def reconstruct_hierarchy(symbols: list[dict]) -> list[dict]:
    """
    Given a flat list of symbols with ranges, reconstruct the parent-child
    hierarchy by checking which symbols' ranges are contained within others.

    Algorithm:
      1. Sort symbols by start line, then by range size (largest first)
         so containers come before their children.
      2. For each symbol, find the smallest container that fully contains it.
      3. Attach it as a child of that container.
    """
    if not symbols:
        return []

    # Add computed fields to each symbol
    for sym in symbols:
        sym["_start"] = get_start_line(sym)
        sym["_end"] = get_end_line(sym)
        sym["_span"] = sym["_end"] - sym["_start"]
        sym["_children"] = []
        sym["_parent"] = None

    # Sort: by start line ascending, then by span descending (larger ranges first)
    sorted_syms = sorted(symbols, key=lambda s: (s["_start"], -s["_span"]))

    # For each symbol, find its tightest (smallest) enclosing container
    for i, child in enumerate(sorted_syms):
        best_parent = None
        best_span = float("inf")

        for j, candidate in enumerate(sorted_syms):
            if i == j:
                continue
            # candidate must fully contain child and be a different range
            if (candidate["_start"] <= child["_start"]
                    and candidate["_end"] >= child["_end"]
                    and candidate["_span"] > child["_span"]):
                # Pick the tightest fit (smallest span that still contains)
                if candidate["_span"] < best_span:
                    best_parent = candidate
                    best_span = candidate["_span"]

        if best_parent is not None:
            best_parent["_children"].append(child)
            child["_parent"] = best_parent["name"]

    # Collect top-level symbols (those with no parent)
    roots = [s for s in sorted_syms if s["_parent"] is None]
    return roots


def symbol_to_tree(sym: dict) -> dict:
    """Convert a symbol with _children into a clean nested dict."""
    kind_int = sym.get("kind", 0)
    node = {
        "name": sym["name"],
        "kind": kind_int,
        "kind_name": KIND_NAMES.get(kind_int, f"kind_{kind_int}"),
        "start_line": sym["_start"],
        "end_line": sym["_end"],
        "span": sym["_span"],
    }
    if sym["_parent"]:
        node["parent"] = sym["_parent"]
    if sym["_children"]:
        node["children"] = [symbol_to_tree(c) for c in
                            sorted(sym["_children"], key=lambda x: x["_start"])]
        node["child_count"] = len(sym["_children"])
    return node


def flatten_with_parents(sym: dict, file_path: str, parent_name: str = None) -> list[dict]:
    """Flatten a hierarchical symbol tree back into a list with parent info."""
    kind_int = sym.get("kind", 0)
    entry = {
        "name": sym["name"],
        "kind": kind_int,
        "kind_name": KIND_NAMES.get(kind_int, f"kind_{kind_int}"),
        "file": file_path,
        "start_line": sym["_start"],
        "end_line": sym["_end"],
        "parent": parent_name,
    }
    result = [entry]
    for child in sym.get("_children", []):
        result.extend(flatten_with_parents(child, file_path, sym["name"]))
    return result


# ---------------------------------------------------------------------------
# Process all files
# ---------------------------------------------------------------------------
def process_all_files(input_dir: Path, output_dir: Path):
    """Process all document_symbols JSON files."""

    symbols_dir = input_dir / "document_symbols"
    if not symbols_dir.exists():
        print(f"ERROR: {symbols_dir} not found")
        sys.exit(1)

    per_file_dir = output_dir / "per_file"
    per_file_dir.mkdir(parents=True, exist_ok=True)

    all_flat_symbols = []       # flat index across all files
    all_class_entries = {}      # class name → {file, members}
    all_edges = []              # parent → child edges
    stats = {
        "files_processed": 0,
        "files_skipped": 0,
        "total_symbols": 0,
        "total_containers": 0,
        "total_members": 0,
        "symbols_with_parent": 0,
        "orphan_symbols": 0,
        "max_nesting_depth": 0,
    }

    json_files = sorted(symbols_dir.glob("*.json"))
    print(f"Processing {len(json_files)} files from {symbols_dir}\n")

    for json_file in json_files:
        with open(json_file) as f:
            data = json.load(f)

        file_path = data.get("file", json_file.stem.replace("__", "/"))
        symbols = data.get("symbols", [])

        if not symbols:
            stats["files_skipped"] += 1
            continue

        stats["files_processed"] += 1
        stats["total_symbols"] += len(symbols)

        # Reconstruct hierarchy
        roots = reconstruct_hierarchy(symbols)

        # Build clean tree
        tree = [symbol_to_tree(r) for r in sorted(roots, key=lambda x: x["_start"])]

        # Write enriched per-file JSON
        safe_name = json_file.name
        enriched = {
            "file": file_path,
            "total_symbols": len(symbols),
            "root_symbols": len(roots),
            "tree": tree,
        }
        with open(per_file_dir / safe_name, "w") as f:
            json.dump(enriched, f, indent=2)

        # Flatten with parent info for global index
        for root in roots:
            flat = flatten_with_parents(root, file_path)
            all_flat_symbols.extend(flat)

        # Extract class → members for class index
        for sym in symbols:
            kind = sym.get("kind", 0)
            if kind in CONTAINER_KINDS and kind != 3:  # skip NAMESPACE
                class_key = f"{file_path}::{sym['name']}"
                members = []
                for child in sym.get("_children", []):
                    members.append({
                        "name": child["name"],
                        "kind": child.get("kind", 0),
                        "kind_name": KIND_NAMES.get(child.get("kind", 0), "?"),
                        "start_line": child["_start"],
                    })
                all_class_entries[class_key] = {
                    "name": sym["name"],
                    "kind": kind,
                    "kind_name": KIND_NAMES.get(kind, "?"),
                    "file": file_path,
                    "start_line": sym["_start"],
                    "end_line": sym["_end"],
                    "member_count": len(members),
                    "members": members,
                }
                stats["total_containers"] += 1
                stats["total_members"] += len(members)

        # Build containment edges
        for sym in symbols:
            if sym.get("_parent"):
                all_edges.append({
                    "file": file_path,
                    "parent": sym["_parent"],
                    "child": sym["name"],
                    "child_kind": KIND_NAMES.get(sym.get("kind", 0), "?"),
                    "child_line": sym["_start"],
                })

        # Compute max depth
        def _depth(s, d=0):
            if not s.get("_children"):
                return d
            return max(_depth(c, d + 1) for c in s["_children"])

        for root in roots:
            depth = _depth(root)
            stats["max_nesting_depth"] = max(stats["max_nesting_depth"], depth)

        # Print per-file summary
        containers = sum(1 for s in symbols if s.get("_children"))
        parented = sum(1 for s in symbols if s.get("_parent"))
        print(f"  {file_path:<55} {len(symbols):>3} symbols, "
              f"{containers:>2} containers, {parented:>3} nested")

    # Compute final stats
    stats["symbols_with_parent"] = sum(1 for s in all_flat_symbols if s.get("parent"))
    stats["orphan_symbols"] = sum(1 for s in all_flat_symbols if not s.get("parent"))

    # Write outputs
    print(f"\nWriting enriched metadata to {output_dir}/ ...")

    with open(output_dir / "symbol_index.json", "w") as f:
        json.dump(all_flat_symbols, f, indent=2)
    print(f"  symbol_index.json — {len(all_flat_symbols)} symbols")

    with open(output_dir / "class_index.json", "w") as f:
        json.dump(all_class_entries, f, indent=2)
    print(f"  class_index.json — {len(all_class_entries)} classes/structs/enums/interfaces")

    with open(output_dir / "intra_file_graph.json", "w") as f:
        json.dump(all_edges, f, indent=2)
    print(f"  intra_file_graph.json — {len(all_edges)} containment edges")

    with open(output_dir / "containment_stats.json", "w") as f:
        json.dump(stats, f, indent=2)
    print(f"  containment_stats.json")

    # Print summary
    print(f"\n{'='*60}")
    print(f"POST-PROCESSING COMPLETE")
    print(f"{'='*60}")
    print(f"  Files processed:    {stats['files_processed']}")
    print(f"  Files skipped:      {stats['files_skipped']}")
    print(f"  Total symbols:      {stats['total_symbols']}")
    print(f"  Containers found:   {stats['total_containers']}")
    print(f"  Members attached:   {stats['total_members']}")
    print(f"  Symbols with parent:{stats['symbols_with_parent']}")
    print(f"  Orphan (top-level): {stats['orphan_symbols']}")
    print(f"  Max nesting depth:  {stats['max_nesting_depth']}")

    # Print a sample enriched tree
    print(f"\n{'='*60}")
    print(f"SAMPLE: Enriched tree for a file with multiple classes")
    print(f"{'='*60}")
    # Find a file with several classes
    best_file = None
    best_classes = 0
    for jf in (per_file_dir).glob("*.json"):
        with open(jf) as f:
            d = json.load(f)
        class_count = sum(1 for t in d.get("tree", [])
                          if t.get("kind") == 5
                          or any(c.get("kind") == 5
                                 for c in t.get("children", [])))
        if class_count > best_classes:
            best_classes = class_count
            best_file = jf

    if best_file:
        with open(best_file) as f:
            sample = json.load(f)
        print(f"\nFile: {sample['file']}")
        print(f"Total symbols: {sample['total_symbols']}, Roots: {sample['root_symbols']}")
        _print_tree(sample["tree"])


def _print_tree(nodes: list, indent: int = 0):
    """Pretty-print a symbol tree."""
    for node in nodes:
        prefix = "  " * indent
        children = node.get("children", [])
        child_str = f" ({node.get('child_count', 0)} members)" if children else ""
        print(f"{prefix}├─ L{node['start_line']:<5} {node['kind_name']:<12} "
              f"{node['name']}{child_str}")
        if children:
            _print_tree(children, indent + 1)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Post-process multilspy metadata: reconstruct symbol hierarchy"
    )
    parser.add_argument(
        "--input", "-i",
        default=os.path.join(os.path.dirname(__file__), "metadata"),
        help="Input metadata directory (default: ./scripts/metadata)",
    )
    parser.add_argument(
        "--output", "-o",
        default=None,
        help="Output directory (default: <input>/enriched)",
    )
    args = parser.parse_args()

    input_dir = Path(args.input).resolve()
    output_dir = Path(args.output).resolve() if args.output else input_dir / "enriched"

    process_all_files(input_dir, output_dir)


if __name__ == "__main__":
    main()
