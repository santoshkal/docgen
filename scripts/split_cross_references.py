#!/usr/bin/env python3
"""
Split monolithic cross-reference JSON files into per-source-file JSONs.

Reads:
  <input_dir>/symbol_index.json
  <input_dir>/cross_file_edges.json
  <input_dir>/intra_file_resolved.json

Writes:
  <input_dir>/per_file/<safe_filename>.json
    Each file contains: {
        "file": "DataCommands/PickList.cs",
        "symbols": [...],
        "cross_file_outgoing": [...],   # symbols defined here, used elsewhere
        "cross_file_incoming": [...],   # symbols from elsewhere, used here
        "intra_file_refs": [...]        # intra-file resolved relationships
    }

Usage:
    python split_cross_references.py <cross_references_dir>
    python split_cross_references.py ../output-imes/metadata-5p/cross_references
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path


# Symbol kinds to exclude (too noisy, filtered during earlier preprocessing)
NOISE_KINDS = {"NAMESPACE"}


def safe_filename(file_path: str) -> str:
    """Convert a source file path to a safe filename for JSON storage."""
    return file_path.replace("/", "__").replace("\\", "__")


def load_json(path: Path) -> list | dict:
    """Load a JSON file, return empty list/dict if missing."""
    if not path.exists():
        print(f"  WARNING: {path.name} not found, skipping")
        return []
    with open(path) as f:
        return json.load(f)


def split_cross_references(input_dir: Path):
    """Split monolithic cross-reference files into per-source-file JSONs."""
    print(f"Splitting cross-references in: {input_dir}\n")

    # Load monolithic files
    symbol_index = load_json(input_dir / "symbol_index.json")
    cross_file_edges = load_json(input_dir / "cross_file_edges.json")
    intra_file_resolved = load_json(input_dir / "intra_file_resolved.json")

    if not symbol_index:
        print("ERROR: No symbol_index.json found or empty. Nothing to split.")
        sys.exit(1)

    # symbol_index is a dict: {file_path: [symbols]}
    all_files = set(symbol_index.keys())

    # Index cross_file_edges by both defined_in and referenced_in
    outgoing_by_file = defaultdict(list)  # defined_in → edges
    incoming_by_file = defaultdict(list)  # referenced_in → edges
    for edge in cross_file_edges:
        kind = edge.get("kind", "")
        if kind in NOISE_KINDS:
            continue
        outgoing_by_file[edge["defined_in"]].append(edge)
        incoming_by_file[edge["referenced_in"]].append(edge)
        all_files.add(edge["defined_in"])
        all_files.add(edge["referenced_in"])

    # Index intra_file_resolved by file
    intra_by_file = defaultdict(list)
    for ref in intra_file_resolved:
        kind = ref.get("to_kind", "")
        if kind in NOISE_KINDS:
            continue
        intra_by_file[ref["file"]].append(ref)
        all_files.add(ref["file"])

    # Create output directory
    per_file_dir = input_dir / "per_file"
    per_file_dir.mkdir(parents=True, exist_ok=True)

    # Write per-file JSONs
    files_written = 0
    files_empty = 0

    for file_path in sorted(all_files):
        symbols = symbol_index.get(file_path, [])
        outgoing = outgoing_by_file.get(file_path, [])
        incoming = incoming_by_file.get(file_path, [])
        intra = intra_by_file.get(file_path, [])

        # Skip files with no useful data
        if not symbols and not outgoing and not incoming and not intra:
            files_empty += 1
            continue

        per_file_data = {
            "file": file_path,
            "symbols": symbols,
            "cross_file_outgoing": outgoing,
            "cross_file_incoming": incoming,
            "intra_file_refs": intra,
        }

        out_path = per_file_dir / f"{safe_filename(file_path)}.json"
        with open(out_path, "w") as f:
            json.dump(per_file_data, f, indent=2)

        files_written += 1

        # Progress every 50 files
        if files_written % 50 == 0:
            print(f"  Written {files_written} files...")

    # Summary
    print(f"\n{'='*60}")
    print(f"SPLIT COMPLETE")
    print(f"{'='*60}")
    print(f"  Input directory:    {input_dir}")
    print(f"  Output directory:   {per_file_dir}")
    print(f"  Files written:      {files_written}")
    print(f"  Files skipped:      {files_empty} (no data)")
    print(f"  Source files total:  {len(all_files)}")
    print(f"\n  Source data:")
    print(f"    symbol_index:        {len(symbol_index)} files")
    print(f"    cross_file_edges:    {len(cross_file_edges)} edges")
    print(f"    intra_file_resolved: {len(intra_file_resolved)} refs")


def main():
    parser = argparse.ArgumentParser(
        description="Split monolithic cross-reference JSONs into per-source-file JSONs"
    )
    parser.add_argument(
        "input_dir",
        help="Path to cross_references directory containing symbol_index.json, "
             "cross_file_edges.json, intra_file_resolved.json",
    )
    args = parser.parse_args()

    input_dir = Path(args.input_dir).resolve()
    if not input_dir.exists():
        print(f"ERROR: Directory not found: {input_dir}")
        sys.exit(1)

    split_cross_references(input_dir)


if __name__ == "__main__":
    main()
