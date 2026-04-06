#!/usr/bin/env python3
"""
Minimal test of multilspy-mcp-server with 4 interconnected C# files.

Tests:
  1. code_document_symbols — intra-file structure (verifies children fix)
  2. code_find_references — inter-file references
  3. code_navigate_definition — base class resolution across files
  4. code_get_hover — type signatures

Test files (inheritance chain):
  ScriptEngine/IScriptCommand.cs        → IScriptCommand interface
  ScriptEngine/DefaultScriptCommand.cs  → DefaultScriptCommand : IScriptCommand
  ScriptEngine/ItemLooper.cs            → ItemLooper : DefaultScriptCommand
  DataCommands/PickList.cs              → PickList : ItemLooper
                                          + 8 more classes : DefaultScriptCommand

Usage:
    python test_multilspy_minimal.py [--workspace ~/Downloads/iMES-master]
"""

import asyncio
import argparse
import json
import os
import sys
import time
from pathlib import Path
from datetime import datetime

from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
DOCKER_IMAGE = "multilspy-csharp:latest"

# 4 files with a clear inheritance chain across files
TEST_FILES = [
    "ScriptEngine/IScriptCommand.cs",
    "ScriptEngine/DefaultScriptCommand.cs",
    "ScriptEngine/ItemLooper.cs",
    "DataCommands/PickList.cs",
]

# Symbols to test find_references and navigate_definition on
# (name, file, line, column) — line/col are 0-indexed
# We'll discover these dynamically from document_symbols results

WORKSPACE_SEARCH_QUERIES = [
    "DefaultScriptCommand",
    "ItemLooper",
    "PickList",
    "IScriptCommand",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def serialize_result(result):
    if result is None:
        return None
    parts = []
    for block in result.content:
        if hasattr(block, "text"):
            try:
                parts.append(json.loads(block.text))
            except json.JSONDecodeError:
                parts.append(block.text)
        else:
            parts.append(str(block))
    return parts[0] if len(parts) == 1 else parts


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)


def print_symbol_tree(symbols, indent=0):
    """Pretty print symbol tree."""
    KIND_NAMES = {
        3: "NAMESPACE", 5: "CLASS", 6: "METHOD", 7: "PROPERTY",
        8: "FIELD", 9: "CONSTRUCTOR", 10: "ENUM", 11: "INTERFACE",
        12: "FUNCTION", 13: "VARIABLE",
    }
    for sym in symbols:
        kind = KIND_NAMES.get(sym.get("kind", 0), f"kind_{sym.get('kind', '?')}")
        name = sym.get("name", "?")
        r = sym.get("range") or sym.get("selection_range") or {}
        line = r.get("start", {}).get("line", "?")
        children = sym.get("children") or []
        marker = f"({len(children)} children)" if children else ""
        prefix = "  " * indent + "├─ "
        print(f"{prefix}L{line:<5} {kind:<12} {name} {marker}")
        if children:
            print_symbol_tree(children, indent + 1)


async def call_tool(session, name, arguments, label=""):
    tag = label or name
    try:
        result = await session.call_tool(name, arguments=arguments)
        data = serialize_result(result)
        if isinstance(data, dict) and not data.get("success", True):
            print(f"  [WARN] {tag}: {data.get('error', 'unknown')}")
        return data
    except Exception as e:
        print(f"  [ERROR] {tag}: {e}")
        return {"success": False, "error": str(e)}


# ---------------------------------------------------------------------------
# Test phases
# ---------------------------------------------------------------------------
async def test_document_symbols(session, output_dir):
    """Test 1: Document symbols with hierarchy (children fix verification)."""
    print(f"\n{'='*60}")
    print("TEST 1: Document Symbols (children fix verification)")
    print(f"{'='*60}")

    all_symbols = {}
    for fpath in TEST_FILES:
        print(f"\n  --- {fpath} ---")
        data = await call_tool(
            session, "code_document_symbols",
            {"file_path": fpath, "language": "csharp"},
            label=fpath,
        )
        if isinstance(data, dict) and data.get("success"):
            symbols = data.get("symbols", [])
            all_symbols[fpath] = symbols
            write_json(output_dir / f"symbols_{Path(fpath).stem}.json", data)

            # Check if children are populated
            has_children = any(
                bool(s.get("children"))
                for s in symbols
            )
            total = len(symbols)

            def count_all(syms):
                c = len(syms)
                for s in syms:
                    c += count_all(s.get("children") or [])
                return c

            deep_total = count_all(symbols)

            print(f"  Top-level symbols: {total}")
            print(f"  Total (with nested): {deep_total}")
            print(f"  Children populated: {'YES' if has_children else 'NO (still flat!)'}")
            print()
            print_symbol_tree(symbols)
        else:
            print(f"  FAILED")

    return all_symbols


async def test_find_references(session, all_symbols, output_dir):
    """Test 2: Cross-file references for key classes/interfaces."""
    print(f"\n{'='*60}")
    print("TEST 2: Cross-File References")
    print(f"{'='*60}")

    # Collect class/interface symbols to test
    # Use selection_range (points at the name token) not range (points at declaration start)
    targets = []
    for fpath, symbols in all_symbols.items():
        def _collect(syms, file):
            for s in syms:
                kind = s.get("kind", 0)
                if kind in {5, 11}:  # CLASS, INTERFACE
                    sr = s.get("selection_range") or s.get("range") or {}
                    start = sr.get("start", {})
                    targets.append({
                        "name": s.get("name"),
                        "file": file,
                        "line": start.get("line", 0),
                        "column": start.get("character", 0),
                        "kind": kind,
                    })
                _collect(s.get("children") or [], file)
        _collect(symbols, fpath)

    print(f"\n  Found {len(targets)} classes/interfaces to check references for\n")

    all_refs = {}
    for t in targets:
        label = f"{t['name']} ({t['file']}:{t['line']})"
        print(f"  {label} ...", end=" ", flush=True)

        data = await call_tool(
            session, "code_find_references",
            {
                "file_path": t["file"],
                "line": t["line"],
                "column": t["column"],
                "language": "csharp",
            },
            label=label,
        )

        if isinstance(data, dict) and data.get("success"):
            locs = data.get("locations", [])
            same_file = sum(1 for l in locs
                           if (l.get("relative_path") or "") == t["file"])
            cross_file = len(locs) - same_file
            other_files = set(
                l.get("relative_path") or l.get("uri", "?")
                for l in locs
                if (l.get("relative_path") or "") != t["file"]
            )

            ref_key = f"{t['file']}::{t['name']}"
            all_refs[ref_key] = {
                "symbol": t["name"],
                "defined_in": t["file"],
                "line": t["line"],
                "total_refs": len(locs),
                "same_file": same_file,
                "cross_file": cross_file,
                "referenced_from_files": sorted(other_files),
                "locations": locs,
            }

            print(f"{len(locs)} refs ({cross_file} cross-file)")
            if other_files:
                for of in sorted(other_files):
                    print(f"    → {of}")
        else:
            print("FAILED")

    write_json(output_dir / "references.json", all_refs)

    # Summary
    print(f"\n  Cross-file reference summary:")
    for key, ref in all_refs.items():
        if ref["cross_file"] > 0:
            print(f"    {ref['symbol']}: referenced from "
                  f"{ref['cross_file']} locations in {len(ref['referenced_from_files'])} other files")

    return all_refs


async def test_navigate_definition(session, all_symbols, output_dir):
    """Test 3: Navigate to definition — resolve base classes across files."""
    print(f"\n{'='*60}")
    print("TEST 3: Navigate to Definition (base class resolution)")
    print(f"{'='*60}")

    # Known base class reference positions (from source inspection)
    # Line numbers are 0-indexed; columns point at the base class NAME token (after last dot)
    base_class_refs = [
        {
            "desc": "PickList → ItemLooper",
            "file": "DataCommands/PickList.cs",
            "line": 45,    # "public class PickList : ng.scripting.ItemLooper"
            "column": 38,  # position of "ItemLooper" (after "ng.scripting.")
        },
        {
            "desc": "AddPartToPickList → DefaultScriptCommand",
            "file": "DataCommands/PickList.cs",
            "line": 239,   # "public class AddPartToPickList : ng.scripting.DefaultScriptCommand"
            "column": 47,  # position of "DefaultScriptCommand"
        },
        {
            "desc": "DefaultScriptCommand → IScriptCommand",
            "file": "ScriptEngine/DefaultScriptCommand.cs",
            "line": 47,    # "public abstract class DefaultScriptCommand : ng.scripting.IScriptCommand, ..."
            "column": 59,  # position of "IScriptCommand"
        },
        {
            "desc": "ItemLooper → DefaultScriptCommand",
            "file": "ScriptEngine/ItemLooper.cs",
            "line": 24,    # "public abstract class ItemLooper : ng.scripting.DefaultScriptCommand, ..."
            "column": 49,  # position of "DefaultScriptCommand"
        },
    ]

    definitions = []
    for ref in base_class_refs:
        print(f"\n  {ref['desc']}")
        print(f"    Source: {ref['file']}:{ref['line']}:{ref['column']}")

        data = await call_tool(
            session, "code_navigate_definition",
            {
                "file_path": ref["file"],
                "line": ref["line"],
                "column": ref["column"],
                "language": "csharp",
            },
            label=ref["desc"],
        )

        if isinstance(data, dict) and data.get("success"):
            locs = data.get("locations", [])
            for loc in locs:
                target = loc.get("relative_path") or loc.get("uri", "?")
                target_line = loc.get("range", {}).get("start", {}).get("line", "?")
                print(f"    → Resolves to: {target}:{target_line}")

            definitions.append({
                "description": ref["desc"],
                "source_file": ref["file"],
                "source_line": ref["line"],
                "definitions": locs,
            })
        else:
            print(f"    → FAILED")
            definitions.append({
                "description": ref["desc"],
                "source_file": ref["file"],
                "source_line": ref["line"],
                "definitions": [],
                "error": data.get("error") if isinstance(data, dict) else str(data),
            })

    write_json(output_dir / "definitions.json", definitions)
    return definitions


async def test_hover(session, all_symbols, output_dir):
    """Test 4: Hover info — get type signatures for key symbols."""
    print(f"\n{'='*60}")
    print("TEST 4: Hover / Type Signatures")
    print(f"{'='*60}")

    # Test hover on class declarations and key methods
    hover_targets = [
        ("IScriptCommand", "ScriptEngine/IScriptCommand.cs"),
        ("DefaultScriptCommand", "ScriptEngine/DefaultScriptCommand.cs"),
        ("ItemLooper", "ScriptEngine/ItemLooper.cs"),
        ("PickList", "DataCommands/PickList.cs"),
    ]

    hover_results = {}
    for name, fpath in hover_targets:
        # Find the symbol's position from our collected data
        symbols = all_symbols.get(fpath, [])

        def _find(syms):
            for s in syms:
                if s.get("name") == name:
                    return s
                found = _find(s.get("children") or [])
                if found:
                    return found
            return None

        sym = _find(symbols)
        if not sym:
            print(f"\n  {name}: symbol not found in document_symbols, skipping")
            continue

        # Use selection_range (name token) not range (full declaration)
        sr = sym.get("selection_range") or sym.get("range") or {}
        line = sr.get("start", {}).get("line", 0)
        col = sr.get("start", {}).get("character", 0)

        print(f"\n  {name} ({fpath}:{line}:{col}) ...", end=" ", flush=True)

        data = await call_tool(
            session, "code_get_hover",
            {
                "file_path": fpath,
                "line": line,
                "column": col,
                "language": "csharp",
            },
            label=name,
        )

        if isinstance(data, dict) and data.get("success"):
            hover = data.get("hover")
            contents = hover.get("contents", "") if hover else ""
            hover_results[name] = {
                "symbol": name,
                "file": fpath,
                "line": line,
                "hover": hover,
            }
            # Print a truncated preview
            preview = str(contents)[:200]
            print(f"OK")
            print(f"    Type info: {preview}")
        else:
            print("FAILED")

    write_json(output_dir / "hover.json", hover_results)
    return hover_results


async def test_workspace_search(session, output_dir):
    """Test 5: Workspace symbol search — project-wide discovery."""
    print(f"\n{'='*60}")
    print("TEST 5: Workspace Symbol Search")
    print(f"{'='*60}")

    results = {}
    for query in WORKSPACE_SEARCH_QUERIES:
        print(f"\n  Searching '{query}' ...", end=" ", flush=True)
        data = await call_tool(
            session, "code_search_workspace",
            {"query": query, "language": "csharp", "limit": 50},
            label=f"search:{query}",
        )

        if isinstance(data, dict) and data.get("success"):
            symbols = data.get("symbols", [])
            results[query] = symbols
            print(f"{len(symbols)} matches")
            for s in symbols[:10]:
                loc = s.get("location", {})
                fpath = loc.get("relative_path") or loc.get("uri", "?")
                line = loc.get("range", {}).get("start", {}).get("line", "?")
                kind = s.get("kind", "?")
                print(f"    {s.get('name', '?')} (kind={kind}) → {fpath}:{line}")
            if len(symbols) > 10:
                print(f"    ... and {len(symbols) - 10} more")
        else:
            print("FAILED")

    write_json(output_dir / "workspace_search.json", results)
    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
async def run_tests(workspace: str, output_dir: str):
    workspace_path = str(Path(workspace).resolve())
    output_path = Path(output_dir).resolve()
    output_path.mkdir(parents=True, exist_ok=True)

    # Verify test files exist
    for f in TEST_FILES:
        full = Path(workspace_path) / f
        if not full.exists():
            print(f"ERROR: Test file not found: {full}")
            sys.exit(1)

    print(f"Workspace: {workspace_path}")
    print(f"Output:    {output_path}")
    print(f"Test files: {len(TEST_FILES)}")
    for f in TEST_FILES:
        print(f"  - {f}")

    server_params = StdioServerParameters(
        command="docker",
        args=[
            "run", "--rm", "-i",
            "-v", f"{workspace_path}:/workspace:ro",
            "-e", "WORKSPACE_ROOT=/workspace",
            "-e", "MCP_LSP_CACHE_DIR=/cache",
            "-e", "LOG_LEVEL=WARNING",
            DOCKER_IMAGE,
            "python", "-m", "multilspy_mcp",
        ],
    )

    print(f"\nStarting multilspy-mcp-server (Docker: {DOCKER_IMAGE})...")
    start = time.time()

    async with stdio_client(server_params) as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()
            print("MCP session initialized.")

            # Initialize workspace
            init = await call_tool(
                session, "lsp_initialize",
                {"workspace_root": "/workspace"},
            )
            write_json(output_path / "init.json", init)
            print(f"Workspace initialized: {init.get('success')}")

            # Run all tests
            all_symbols = await test_document_symbols(session, output_path)
            refs = await test_find_references(session, all_symbols, output_path)
            defs = await test_navigate_definition(session, all_symbols, output_path)
            hover = await test_hover(session, all_symbols, output_path)
            ws = await test_workspace_search(session, output_path)

    elapsed = time.time() - start

    # Write summary
    summary = {
        "workspace": workspace_path,
        "test_files": TEST_FILES,
        "elapsed_seconds": round(elapsed, 1),
        "timestamp": datetime.now().isoformat(),
        "results": {
            "document_symbols": {
                "files": len(all_symbols),
                "children_populated": any(
                    any(bool(s.get("children")) for s in syms)
                    for syms in all_symbols.values()
                ),
            },
            "references": {
                "symbols_checked": len(refs),
                "with_cross_file_refs": sum(1 for r in refs.values() if r["cross_file"] > 0),
            },
            "definitions": {
                "tested": len(defs),
                "resolved": sum(1 for d in defs if d.get("definitions")),
            },
            "hover": {
                "tested": len(hover),
                "with_content": sum(1 for h in hover.values() if h.get("hover")),
            },
            "workspace_search": {
                "queries": len(ws),
                "total_matches": sum(len(v) for v in ws.values()),
            },
        },
    }
    write_json(output_path / "summary.json", summary)

    print(f"\n{'='*60}")
    print(f"ALL TESTS COMPLETE — {elapsed:.1f}s")
    print(f"{'='*60}")
    print(f"  Output: {output_path}")
    print(json.dumps(summary["results"], indent=2))


def main():
    parser = argparse.ArgumentParser(description="Minimal multilspy test with 4 C# files")
    parser.add_argument(
        "--workspace", "-w",
        default=os.path.expanduser("~/Downloads/iMES-master"),
    )
    parser.add_argument(
        "--output", "-o",
        default=os.path.join(os.path.dirname(__file__), "metadata", "test_minimal"),
    )
    args = parser.parse_args()
    asyncio.run(run_tests(args.workspace, args.output))


if __name__ == "__main__":
    main()
