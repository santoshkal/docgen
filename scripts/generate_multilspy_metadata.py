#!/usr/bin/env python3
"""
Generate project-wide inter/intra-file metadata for a C# codebase
using the multilspy-mcp-server via MCP protocol over stdio.

Uses only two MCP tools:
  1. code_document_symbols — intra-file structure (class → method/field hierarchy)
  2. code_find_references  — inter + intra-file references (all symbols)

Features:
  - Checkpoint/resume so the process can be stopped and restarted
  - Auto-restart Docker container after consecutive timeouts (OmniSharp recovery)
  - Failed files logged to failed_files.json

Usage:
    python generate_multilspy_metadata.py [--workspace /path/to/project] [--output ./metadata]
    python generate_multilspy_metadata.py --resume        # resume from checkpoint
    python generate_multilspy_metadata.py --status        # show checkpoint status
"""

import asyncio
import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
DOCKER_IMAGE = "multilspy-csharp:latest"
CONTAINER_WORKSPACE = "/workspace"
CONTAINER_CACHE = "/cache"

TOOL_TIMEOUT = 120          # seconds per tool call
MAX_CONSECUTIVE_TIMEOUTS = 3  # restart container after this many in a row

KIND_NAMES = {
    1: "FILE", 2: "MODULE", 3: "NAMESPACE", 4: "PACKAGE",
    5: "CLASS", 6: "METHOD", 7: "PROPERTY", 8: "FIELD",
    9: "CONSTRUCTOR", 10: "ENUM", 11: "INTERFACE", 12: "FUNCTION",
    13: "VARIABLE", 14: "CONSTANT", 22: "ENUM_MEMBER", 23: "STRUCT",
    24: "EVENT", 25: "OPERATOR", 26: "TYPE_PARAMETER",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def find_cs_files(workspace_path: str) -> list[str]:
    """Find all .cs files relative to workspace root."""
    root = Path(workspace_path)
    return sorted(
        str(p.relative_to(root))
        for p in root.rglob("*.cs")
        if "bin" not in p.parts
        and "obj" not in p.parts
        and ".git" not in p.parts
    )


def serialize_result(result) -> dict | list | str | None:
    """Extract JSON-serializable data from MCP CallToolResult."""
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
    """Write data to a JSON file with pretty-printing."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)


def safe_filename(key: str) -> str:
    """Convert a symbol key to a safe filename."""
    return key.replace("/", "__").replace("\\", "__").replace("::", "--")


def make_server_params(workspace_path: str) -> StdioServerParameters:
    """Build MCP server params for launching Docker container."""
    return StdioServerParameters(
        command="docker",
        args=[
            "run", "--rm", "-i",
            "-v", f"{workspace_path}:{CONTAINER_WORKSPACE}:ro",
            "-e", f"WORKSPACE_ROOT={CONTAINER_WORKSPACE}",
            "-e", f"MCP_LSP_CACHE_DIR={CONTAINER_CACHE}",
            "-e", "LOG_LEVEL=WARNING",
            DOCKER_IMAGE,
            "python", "-m", "multilspy_mcp",
        ],
    )


# ---------------------------------------------------------------------------
# Failure logger
# ---------------------------------------------------------------------------
class FailureLog:
    """Track failed files/symbols with reasons."""

    def __init__(self, output_dir: Path):
        self.path = output_dir / "failed_files.json"
        self.failures = []
        if self.path.exists():
            with open(self.path) as f:
                self.failures = json.load(f)

    def log(self, phase: str, item: str, reason: str):
        self.failures.append({
            "phase": phase,
            "item": item,
            "reason": reason,
            "timestamp": datetime.now().isoformat(),
        })
        self.save()

    def save(self):
        write_json(self.path, self.failures)

    def summary(self):
        from collections import Counter
        by_phase = Counter(f["phase"] for f in self.failures)
        by_reason = Counter(f["reason"].split(":")[0] for f in self.failures)
        print(f"  Total failures: {len(self.failures)}")
        for phase, count in sorted(by_phase.items()):
            print(f"    {phase}: {count}")
        for reason, count in sorted(by_reason.items(), key=lambda x: -x[1]):
            print(f"    {reason}: {count}")


# ---------------------------------------------------------------------------
# Checkpoint manager
# ---------------------------------------------------------------------------
class Checkpoint:
    """Track progress so the script can be stopped and resumed."""

    def __init__(self, output_dir: Path):
        self.path = output_dir / "checkpoint.json"
        self.state = {
            "phase1_completed_files": [],
            "phase1_failed_files": [],
            "phase2_completed_symbols": [],
            "phase2_failed_symbols": [],
            "phase1_done": False,
            "phase2_done": False,
            "started_at": None,
            "last_updated": None,
        }
        if self.path.exists():
            with open(self.path) as f:
                saved = json.load(f)
                self.state.update(saved)

    def save(self):
        self.state["last_updated"] = datetime.now().isoformat()
        write_json(self.path, self.state)

    def mark_phase1_file(self, fpath: str):
        if fpath not in self.state["phase1_completed_files"]:
            self.state["phase1_completed_files"].append(fpath)
        if len(self.state["phase1_completed_files"]) % 10 == 0:
            self.save()

    def mark_phase1_failed(self, fpath: str):
        if fpath not in self.state["phase1_failed_files"]:
            self.state["phase1_failed_files"].append(fpath)

    def mark_phase2_symbol(self, key: str):
        if key not in self.state["phase2_completed_symbols"]:
            self.state["phase2_completed_symbols"].append(key)
        if len(self.state["phase2_completed_symbols"]) % 20 == 0:
            self.save()

    def mark_phase2_failed(self, key: str):
        if key not in self.state["phase2_failed_symbols"]:
            self.state["phase2_failed_symbols"].append(key)

    def is_phase1_file_done(self, fpath: str) -> bool:
        return fpath in self.state["phase1_completed_files"]

    def is_phase1_file_failed(self, fpath: str) -> bool:
        return fpath in self.state.get("phase1_failed_files", [])

    def is_phase2_symbol_done(self, key: str) -> bool:
        return key in self.state["phase2_completed_symbols"]

    def is_phase2_symbol_failed(self, key: str) -> bool:
        return key in self.state.get("phase2_failed_symbols", [])

    @property
    def phase1_done(self) -> bool:
        return self.state.get("phase1_done", False)

    @phase1_done.setter
    def phase1_done(self, val: bool):
        self.state["phase1_done"] = val
        self.save()

    @property
    def phase2_done(self) -> bool:
        return self.state.get("phase2_done", False)

    @phase2_done.setter
    def phase2_done(self, val: bool):
        self.state["phase2_done"] = val
        self.save()

    def status(self):
        p1_done = len(self.state["phase1_completed_files"])
        p1_fail = len(self.state.get("phase1_failed_files", []))
        p2_done = len(self.state["phase2_completed_symbols"])
        p2_fail = len(self.state.get("phase2_failed_symbols", []))
        print(f"  Phase 1 (document_symbols): {p1_done} done, {p1_fail} failed, "
              f"{'COMPLETE' if self.phase1_done else 'in progress'}")
        print(f"  Phase 2 (find_references):  {p2_done} done, {p2_fail} failed, "
              f"{'COMPLETE' if self.phase2_done else 'in progress'}")
        print(f"  Started:      {self.state.get('started_at', 'N/A')}")
        print(f"  Last updated: {self.state.get('last_updated', 'N/A')}")


# ---------------------------------------------------------------------------
# Metrics collector
# ---------------------------------------------------------------------------
class MetricsCollector:
    """Collect MCP tool-call latency metrics, bucketed by C# source subdirectory.

    Output layout under metrics_dir:
        <subdir>.json          — every call record for that subdirectory
        <subdir>_summary.json  — p50/p90/p95/p99 + counts for that subdirectory
        project_summary.json   — aggregated stats across the whole project

    On resume the existing per-subdir files are read and new records are
    appended so latency history is cumulative across restarts.
    """

    def __init__(self, output_dir: Path, resume: bool = False):
        self.metrics_dir = output_dir / "metrics"
        self.metrics_dir.mkdir(parents=True, exist_ok=True)
        self.resume = resume
        # Unsaved records buffered in memory: subdir -> [record, ...]
        self._pending: dict[str, list] = defaultdict(list)

    def _get_subdir(self, file_path: str) -> str:
        parts = Path(file_path).parts
        return parts[0] if len(parts) > 1 else "root"

    def _detail_path(self, subdir: str) -> Path:
        safe = subdir.replace("/", "__").replace("\\", "__")
        return self.metrics_dir / f"{safe}.json"

    def record(
        self,
        tool: str,
        file_path: str,
        phase: int,
        latency_ms: float,
        status: str,
        symbol_name: str = None,
        symbol_kind: str = None,
        result_count: int = None,
    ):
        """Buffer one tool-call record. Call flush() to persist to disk."""
        subdir = self._get_subdir(file_path)
        entry = {
            "tool": tool,
            "file": file_path,
            "phase": phase,
            "timestamp": datetime.now().isoformat(),
            "latency_ms": round(latency_ms, 2),
            "status": status,
        }
        if symbol_name is not None:
            entry["symbol"] = symbol_name
        if symbol_kind is not None:
            entry["symbol_kind"] = symbol_kind
        if result_count is not None:
            entry["result_count"] = result_count
        self._pending[subdir].append(entry)

    def flush(self, subdir: str = None):
        """Persist buffered records to disk. Pass subdir=None to flush all."""
        targets = [subdir] if subdir else list(self._pending.keys())
        for sd in targets:
            records = self._pending.get(sd, [])
            if not records:
                continue
            path = self._detail_path(sd)
            existing = []
            if path.exists():
                with open(path) as f:
                    existing = json.load(f).get("calls", [])
            write_json(path, {"directory": sd, "calls": existing + records})
            self._pending[sd] = []

    def _compute_summary(self, label: str, calls: list) -> dict:
        if not calls:
            return {}
        latencies = [c["latency_ms"] for c in calls]
        ls = sorted(latencies)
        n = len(ls)

        def pct(p: float) -> float:
            return round(ls[min(int(n * p / 100), n - 1)], 2)

        return {
            "label": label,
            "total_calls": n,
            "by_tool": dict(Counter(c["tool"] for c in calls)),
            "by_phase": {str(k): v for k, v in Counter(c["phase"] for c in calls).items()},
            "by_status": dict(Counter(c["status"] for c in calls)),
            "latency_ms": {
                "min": round(min(latencies), 2),
                "max": round(max(latencies), 2),
                "mean": round(sum(latencies) / n, 2),
                "p50": pct(50),
                "p90": pct(90),
                "p95": pct(95),
                "p99": pct(99),
            },
        }

    def write_summaries(self):
        """Flush all pending records, then write per-subdir and project summaries."""
        self.flush()

        all_calls = []
        for detail_file in sorted(self.metrics_dir.glob("*.json")):
            if "_summary" in detail_file.stem or detail_file.stem == "project_summary":
                continue
            with open(detail_file) as f:
                data = json.load(f)
            calls = data.get("calls", [])
            if calls:
                subdir = data.get("directory", detail_file.stem)
                summary = self._compute_summary(subdir, calls)
                if summary:
                    write_json(self.metrics_dir / f"{detail_file.stem}_summary.json", summary)
                all_calls.extend(calls)

        if all_calls:
            project_summary = self._compute_summary("project", all_calls)
            project_summary["generated_at"] = datetime.now().isoformat()
            write_json(self.metrics_dir / "project_summary.json", project_summary)
            lat = project_summary["latency_ms"]
            print(f"\nMetrics written to {self.metrics_dir}")
            print(f"  Tool calls tracked: {len(all_calls)}")
            print(f"  Latency (ms): min={lat['min']}, mean={lat['mean']}, "
                  f"p95={lat['p95']}, max={lat['max']}")


# ---------------------------------------------------------------------------
# MCP tool callers
# ---------------------------------------------------------------------------
async def call_tool(
    session: ClientSession,
    name: str,
    arguments: dict,
    label: str = "",
    metrics: MetricsCollector | None = None,
    metrics_file: str = None,
    metrics_phase: int = None,
    metrics_symbol: str = None,
    metrics_kind: str = None,
):
    """Call an MCP tool with a timeout. Returns error dict if call hangs.

    When metrics is supplied the call's wall-clock latency and outcome are
    recorded via MetricsCollector.record().  Pass metrics_file so the record
    is bucketed into the right subdirectory.
    """
    tag = label or name
    t0 = time.time()
    try:
        result = await asyncio.wait_for(
            session.call_tool(name, arguments=arguments),
            timeout=TOOL_TIMEOUT,
        )
        latency_ms = (time.time() - t0) * 1000
        data = serialize_result(result)
        if isinstance(data, dict) and not data.get("success", True):
            status = "error"
            print(f"  [WARN] {tag}: {data.get('error', 'unknown error')}")
        else:
            status = "success"
        if metrics and metrics_file is not None:
            result_count = None
            if name == "code_document_symbols" and isinstance(data, dict):
                result_count = len(data.get("symbols", []))
            elif name == "code_find_references" and isinstance(data, dict):
                result_count = len(data.get("locations", []))
            metrics.record(name, metrics_file, metrics_phase or 0, latency_ms, status,
                           metrics_symbol, metrics_kind, result_count)
        return data
    except asyncio.TimeoutError:
        latency_ms = (time.time() - t0) * 1000
        print(f"  [TIMEOUT] {tag}: exceeded {TOOL_TIMEOUT}s, skipping")
        if metrics and metrics_file is not None:
            metrics.record(name, metrics_file, metrics_phase or 0, latency_ms, "timeout",
                           metrics_symbol, metrics_kind, None)
        return {"success": False, "error": f"timeout after {TOOL_TIMEOUT}s", "_timeout": True}
    except Exception as e:
        latency_ms = (time.time() - t0) * 1000
        print(f"  [ERROR] {tag}: {e}")
        if metrics and metrics_file is not None:
            metrics.record(name, metrics_file, metrics_phase or 0, latency_ms, "error",
                           metrics_symbol, metrics_kind, None)
        return {"success": False, "error": str(e)}


# ---------------------------------------------------------------------------
# Phase 1: Document Symbols
# ---------------------------------------------------------------------------
def _flatten_symbols(symbols: list, file_path: str, parent: str = None) -> list[dict]:
    """Flatten hierarchical symbols into a flat list with parent info and full range."""
    flat = []
    for sym in symbols:
        entry = {
            "name": sym.get("name", ""),
            "kind": sym.get("kind"),
            "kind_name": KIND_NAMES.get(sym.get("kind", 0), f"kind_{sym.get('kind', 0)}"),
            "parent": parent,
            "file": file_path,
        }
        sr = sym.get("selection_range") or sym.get("range")
        if sr and isinstance(sr, dict):
            start = sr.get("start", {})
            entry["line"] = start.get("line", 0)
            entry["column"] = start.get("character", 0)
        elif sym.get("location") and sym["location"].get("range"):
            start = sym["location"]["range"].get("start", {})
            entry["line"] = start.get("line", 0)
            entry["column"] = start.get("character", 0)

        r = sym.get("range")
        if r and isinstance(r, dict):
            entry["range_start"] = r.get("start", {}).get("line", 0)
            entry["range_end"] = r.get("end", {}).get("line", 0)

        flat.append(entry)

        children = sym.get("children") or []
        if children:
            flat.extend(_flatten_symbols(children, file_path, parent=sym.get("name")))

    return flat


async def collect_document_symbols(
    session: ClientSession,
    cs_files: list[str],
    output_dir: Path,
    checkpoint: Checkpoint,
    failure_log: FailureLog,
    metrics: MetricsCollector | None = None,
) -> tuple[dict, int]:
    """Phase 1: collect document symbols for every .cs file.
    Returns (symbol_index, consecutive_timeout_count)."""
    print(f"\n{'='*60}")
    print(f"Phase 1: Document Symbols ({len(cs_files)} files)")
    print(f"{'='*60}")

    symbols_dir = output_dir / "document_symbols"
    all_symbols = {}
    errors = []
    skipped = 0
    consecutive_timeouts = 0

    for i, fpath in enumerate(cs_files, 1):
        tag = f"[{i}/{len(cs_files)}] {fpath}"

        # Skip if already done or permanently failed
        if checkpoint.is_phase1_file_done(fpath):
            cached_file = symbols_dir / f"{safe_filename(fpath)}.json"
            if cached_file.exists():
                with open(cached_file) as f:
                    data = json.load(f)
                all_symbols[fpath] = data.get("symbols", [])
            skipped += 1
            continue

        if checkpoint.is_phase1_file_failed(fpath):
            skipped += 1
            continue

        print(f"  {tag} ...", end=" ", flush=True)

        data = await call_tool(
            session,
            "code_document_symbols",
            {"file_path": fpath, "language": "csharp"},
            label=tag,
            metrics=metrics,
            metrics_file=fpath,
            metrics_phase=1,
        )

        if isinstance(data, dict) and data.get("success"):
            consecutive_timeouts = 0  # reset on success
            symbols = data.get("symbols", [])
            all_symbols[fpath] = symbols
            write_json(symbols_dir / f"{safe_filename(fpath)}.json", {
                "file": fpath,
                "symbol_count": len(symbols),
                "symbols": symbols,
            })
            checkpoint.mark_phase1_file(fpath)

            def _count(syms):
                c = len(syms)
                for s in syms:
                    c += _count(s.get("children") or [])
                return c

            total = _count(symbols)
            print(f"{total} symbols ({len(symbols)} top-level)")
        else:
            is_timeout = isinstance(data, dict) and data.get("_timeout")
            reason = data.get("error", "unknown") if isinstance(data, dict) else str(data)
            errors.append(fpath)
            failure_log.log("phase1_document_symbols", fpath, reason)

            consecutive_timeouts += 1
            fail_type = "TIMEOUT" if is_timeout else "ERROR"
            print(f"{fail_type} ({consecutive_timeouts}/{MAX_CONSECUTIVE_TIMEOUTS})")

            if consecutive_timeouts >= MAX_CONSECUTIVE_TIMEOUTS:
                print(f"\n  *** {MAX_CONSECUTIVE_TIMEOUTS} consecutive failures — "
                      f"OmniSharp needs restart ***")
                if metrics:
                    metrics.flush()
                checkpoint.save()
                return all_symbols, consecutive_timeouts

        # Flush this file's metrics to disk now — mirrors the checkpoint cadence
        if metrics:
            metrics.flush(metrics._get_subdir(fpath))

    # Build flattened symbol index
    symbol_index = {}
    for fpath, symbols in all_symbols.items():
        symbol_index[fpath] = _flatten_symbols(symbols, fpath)

    write_json(output_dir / "symbol_index.json", symbol_index)
    checkpoint.phase1_done = True
    checkpoint.save()

    total_syms = sum(len(v) for v in symbol_index.values())
    print(f"\nPhase 1 complete: {len(all_symbols)} files ({skipped} from checkpoint), "
          f"{total_syms} symbols, {len(errors)} errors")
    return symbol_index, 0


# ---------------------------------------------------------------------------
# Phase 2: Find References (ALL symbols)
# ---------------------------------------------------------------------------
async def collect_references(
    session: ClientSession,
    symbol_index: dict,
    output_dir: Path,
    checkpoint: Checkpoint,
    failure_log: FailureLog,
    metrics: MetricsCollector | None = None,
) -> tuple[dict, int]:
    """Phase 2: find references for ALL symbols.
    Returns (all_refs, consecutive_timeout_count)."""
    print(f"\n{'='*60}")
    print(f"Phase 2: Find References (all symbols)")
    print(f"{'='*60}")

    all_syms = []
    for fpath, symbols in symbol_index.items():
        for sym in symbols:
            if sym.get("line") is not None:
                if KIND_NAMES.get(sym.get("kind",0)) not in NOISE_KINDS:
                    all_syms.append(sym)

    print(f"  Total symbols to check: {len(all_syms)}")

    refs_dir = output_dir / "references"
    all_refs = {}
    skipped = 0
    errors = 0
    consecutive_timeouts = 0
    prev_fpath = None  # tracks file changes so we flush metrics per-subdir boundary

    for i, sym in enumerate(all_syms, 1):
        fpath = sym["file"]

        # When the source file changes, flush buffered metrics for the previous
        # file's subdirectory — keeps memory footprint low on large projects.
        if metrics and prev_fpath and prev_fpath != fpath:
            metrics.flush(metrics._get_subdir(prev_fpath))
        prev_fpath = fpath
        name = sym["name"]
        kind = sym.get("kind", 0)
        line = sym["line"]
        col = sym.get("column", 0)
        ref_key = f"{fpath}::{name}::{line}"

        if checkpoint.is_phase2_symbol_done(ref_key):
            cached_file = refs_dir / f"{safe_filename(ref_key)}.json"
            if cached_file.exists():
                with open(cached_file) as f:
                    all_refs[ref_key] = json.load(f)
            skipped += 1
            continue

        if checkpoint.is_phase2_symbol_failed(ref_key):
            skipped += 1
            continue

        kind_name = KIND_NAMES.get(kind, f"kind_{kind}")
        tag = f"[{i}/{len(all_syms)}] {kind_name} {name} ({fpath}:{line})"
        print(f"  {tag} ...", end=" ", flush=True)

        data = await call_tool(
            session,
            "code_find_references",
            {
                "file_path": fpath,
                "line": line,
                "column": col,
                "language": "csharp",
            },
            label=tag,
            metrics=metrics,
            metrics_file=fpath,
            metrics_phase=2,
            metrics_symbol=name,
            metrics_kind=kind_name,
        )

        if isinstance(data, dict) and data.get("success"):
            consecutive_timeouts = 0
            locations = data.get("locations", [])

            same_file_locs = []
            cross_file_locs = []
            for loc in locations:
                ref_file = loc.get("relative_path") or loc.get("uri", "")
                if ref_file == fpath:
                    same_file_locs.append(loc)
                elif ref_file:
                    cross_file_locs.append(loc)

            ref_data = {
                "symbol": name,
                "kind": kind,
                "kind_name": kind_name,
                "defined_in": fpath,
                "defined_at_line": line,
                "parent": sym.get("parent"),
                "total_refs": len(locations),
                "same_file_refs": len(same_file_locs),
                "cross_file_refs": len(cross_file_locs),
                "same_file_locations": same_file_locs,
                "cross_file_locations": cross_file_locs,
            }
            all_refs[ref_key] = ref_data
            write_json(refs_dir / f"{safe_filename(ref_key)}.json", ref_data)
            checkpoint.mark_phase2_symbol(ref_key)

            print(f"{len(locations)} refs "
                  f"(same:{len(same_file_locs)}, cross:{len(cross_file_locs)})")
        else:
            is_timeout = isinstance(data, dict) and data.get("_timeout")
            reason = data.get("error", "unknown") if isinstance(data, dict) else str(data)
            errors += 1
            failure_log.log("phase2_find_references", ref_key, reason)

            # Count any failure (timeout or error) as consecutive —
            # OmniSharp returning empty errors means it's degraded
            consecutive_timeouts += 1
            fail_type = "TIMEOUT" if is_timeout else "ERROR"
            print(f"{fail_type} ({consecutive_timeouts}/{MAX_CONSECUTIVE_TIMEOUTS})")

            if consecutive_timeouts >= MAX_CONSECUTIVE_TIMEOUTS:
                print(f"\n  *** {MAX_CONSECUTIVE_TIMEOUTS} consecutive failures — "
                      f"OmniSharp needs restart ***")
                if metrics:
                    metrics.flush()
                checkpoint.save()
                return all_refs, consecutive_timeouts

    # Flush any remaining buffered metrics after the loop
    if metrics:
        metrics.flush()

    # Build aggregated edge lists
    cross_file_edges = []
    intra_file_edges = []

    for ref_key, ref_data in all_refs.items():
        fpath = ref_data["defined_in"]
        name = ref_data["symbol"]
        kind_name = ref_data.get("kind_name", "?")

        for loc in ref_data.get("cross_file_locations", []):
            ref_file = loc.get("relative_path") or loc.get("uri", "")
            ref_line = loc.get("range", {}).get("start", {}).get("line")
            cross_file_edges.append({
                "symbol": name,
                "kind": kind_name,
                "defined_in": fpath,
                "defined_at_line": ref_data["defined_at_line"],
                "referenced_in": ref_file,
                "referenced_at_line": ref_line,
            })

        for loc in ref_data.get("same_file_locations", []):
            ref_line = loc.get("range", {}).get("start", {}).get("line")
            if ref_line is not None and ref_line != ref_data["defined_at_line"]:
                intra_file_edges.append({
                    "symbol": name,
                    "kind": kind_name,
                    "file": fpath,
                    "defined_at_line": ref_data["defined_at_line"],
                    "referenced_at_line": ref_line,
                })

    write_json(output_dir / "cross_file_edges.json", cross_file_edges)
    write_json(output_dir / "intra_file_edges.json", intra_file_edges)

    symbols_with_cross = sum(1 for r in all_refs.values() if r["cross_file_refs"] > 0)
    symbols_with_intra = sum(1 for r in all_refs.values() if r["same_file_refs"] > 0)
    write_json(output_dir / "references_summary.json", {
        "total_symbols_checked": len(all_syms),
        "symbols_from_checkpoint": skipped,
        "symbols_with_cross_file_refs": symbols_with_cross,
        "symbols_with_intra_file_refs": symbols_with_intra,
        "total_cross_file_edges": len(cross_file_edges),
        "total_intra_file_edges": len(intra_file_edges),
        "errors": errors,
    })

    checkpoint.phase2_done = True
    checkpoint.save()

    print(f"\nPhase 2 complete:")
    print(f"  Symbols checked:       {len(all_syms)} ({skipped} from checkpoint)")
    print(f"  Cross-file edges:      {len(cross_file_edges)} ({symbols_with_cross} symbols)")
    print(f"  Intra-file edges:      {len(intra_file_edges)} ({symbols_with_intra} symbols)")
    print(f"  Errors:                {errors}")
    return all_refs, 0


# ---------------------------------------------------------------------------
# Post-processing: resolve intra-file "who references whom"
# ---------------------------------------------------------------------------
def resolve_intra_file_references(symbol_index: dict, output_dir: Path):
    """Resolve which method contains each intra-file reference line."""
    print(f"\n{'='*60}")
    print("Post-processing: Resolving intra-file containment")
    print(f"{'='*60}")

    intra_edges_file = output_dir / "intra_file_edges.json"
    if not intra_edges_file.exists():
        print("  No intra-file edges to process")
        return

    with open(intra_edges_file) as f:
        intra_edges = json.load(f)

    file_symbols = {}
    for fpath, syms in symbol_index.items():
        containers = [
            s for s in syms
            if s.get("range_start") is not None and s.get("range_end") is not None
        ]
        containers.sort(key=lambda s: s["range_end"] - s["range_start"])
        file_symbols[fpath] = containers

    resolved = []
    unresolved = 0

    for edge in intra_edges:
        fpath = edge["file"]
        ref_line = edge["referenced_at_line"]
        containers = file_symbols.get(fpath, [])

        containing_sym = None
        for sym in containers:
            if sym["range_start"] <= ref_line <= sym["range_end"]:
                if sym["name"] != edge["symbol"] or sym.get("line") != edge["defined_at_line"]:
                    containing_sym = sym
                    break

        if containing_sym:
            resolved.append({
                "file": fpath,
                "from_symbol": containing_sym["name"],
                "from_kind": containing_sym.get("kind_name", "?"),
                "from_line": containing_sym.get("line"),
                "to_symbol": edge["symbol"],
                "to_kind": edge["kind"],
                "to_line": edge["defined_at_line"],
                "reference_at_line": ref_line,
                "relationship": "references",
            })
        else:
            unresolved += 1

    write_json(output_dir / "intra_file_resolved.json", resolved)
    print(f"  Resolved: {len(resolved)} intra-file relationships")
    print(f"  Unresolved: {unresolved}")
    return resolved


# ---------------------------------------------------------------------------
# Post-processing: write per-source-file cross-reference JSONs
# ---------------------------------------------------------------------------
NOISE_KINDS = {"NAMESPACE"}


def write_per_file_cross_references(symbol_index: dict, output_dir: Path,
                                     cross_ref_output_dir: Path = None):
    """
    Split monolithic cross-reference data into per-source-file JSONs.

    Each file gets a single JSON containing only its own symbols, cross-file
    edges (both directions), and intra-file resolved relationships.
    This allows the doc agent to load only the data it needs per file.

    Reads:  symbol_index.json, cross_file_edges.json, intra_file_resolved.json
            from output_dir (where the monolithic files live)
    Writes: <target>/per_file/<safe_filename>.json

    Args:
        symbol_index: dict of file_path → symbol list
        output_dir: directory containing monolithic JSON files
        cross_ref_output_dir: target directory for per-file output (defaults to output_dir)
    """
    target_dir = cross_ref_output_dir or output_dir

    print(f"\n{'='*60}")
    print("Post-processing: Writing per-file cross-reference JSONs")
    print(f"{'='*60}")
    if cross_ref_output_dir:
        print(f"  Target: {cross_ref_output_dir}")

    # Load edge lists
    cross_path = output_dir / "cross_file_edges.json"
    intra_path = output_dir / "intra_file_resolved.json"

    cross_file_edges = []
    if cross_path.exists():
        with open(cross_path) as f:
            cross_file_edges = json.load(f)

    intra_file_resolved = []
    if intra_path.exists():
        with open(intra_path) as f:
            intra_file_resolved = json.load(f)

    # Collect all known files
    all_files = set(symbol_index.keys())

    # Index cross_file_edges by defined_in and referenced_in
    outgoing_by_file = defaultdict(list)
    incoming_by_file = defaultdict(list)
    for edge in cross_file_edges:
        if edge.get("kind", "") in NOISE_KINDS:
            continue
        outgoing_by_file[edge["defined_in"]].append(edge)
        incoming_by_file[edge["referenced_in"]].append(edge)
        all_files.add(edge["defined_in"])
        all_files.add(edge["referenced_in"])

    # Index intra_file_resolved by file
    intra_by_file = defaultdict(list)
    for ref in intra_file_resolved:
        if ref.get("to_kind", "") in NOISE_KINDS:
            continue
        intra_by_file[ref["file"]].append(ref)
        all_files.add(ref["file"])

    # Write per-file JSONs
    per_file_dir = target_dir / "per_file"
    per_file_dir.mkdir(parents=True, exist_ok=True)

    files_written = 0
    for file_path in sorted(all_files):
        symbols = symbol_index.get(file_path, [])
        outgoing = outgoing_by_file.get(file_path, [])
        incoming = incoming_by_file.get(file_path, [])
        intra = intra_by_file.get(file_path, [])

        if not symbols and not outgoing and not incoming and not intra:
            continue

        per_file_data = {
            "file": file_path,
            "symbols": symbols,
            "cross_file_outgoing": outgoing,
            "cross_file_incoming": incoming,
            "intra_file_refs": intra,
        }

        out_name = file_path.replace("/", "__").replace("\\", "__")
        write_json(per_file_dir / f"{out_name}.json", per_file_data)
        files_written += 1

    print(f"  Written {files_written} per-file JSONs to {per_file_dir}")
    return files_written


# ---------------------------------------------------------------------------
# Orchestrator with auto-restart
# ---------------------------------------------------------------------------
async def run_single_session(
    workspace_path: str,
    output_path: Path,
    cs_files: list[str],
    checkpoint: Checkpoint,
    failure_log: FailureLog,
    metrics: MetricsCollector | None = None,
) -> bool:
    """Run one MCP session. Returns True if fully complete, False if restart needed."""

    server_params = make_server_params(workspace_path)

    print(f"\nConnecting to multilspy-mcp-server (Docker: {DOCKER_IMAGE})...")

    try:
        async with stdio_client(server_params) as streams:
            async with ClientSession(*streams) as session:
                await session.initialize()
                print("MCP session initialized.\n")

                # Initialize workspace
                print("Initializing workspace via lsp_initialize...")
                init_result = await call_tool(
                    session,
                    "lsp_initialize",
                    {"workspace_root": CONTAINER_WORKSPACE},
                    label="lsp_initialize",
                )
                write_json(output_path / "init_result.json", init_result)
                print("Workspace initialized.\n")

                # Phase 1
                if not checkpoint.phase1_done:
                    result, timeouts = await collect_document_symbols(
                        session, cs_files, output_path, checkpoint, failure_log, metrics
                    )
                    if timeouts >= MAX_CONSECUTIVE_TIMEOUTS:
                        print("\n  Returning for container restart (Phase 1)...")
                        return False
                    symbol_index = result
                else:
                    print("Phase 1 already complete, loading from disk...")
                    with open(output_path / "symbol_index.json") as f:
                        symbol_index = json.load(f)
                    print(f"  Loaded {sum(len(v) for v in symbol_index.values())} symbols "
                          f"from {len(symbol_index)} files")

                # Phase 2
                if not checkpoint.phase2_done:
                    _, timeouts = await collect_references(
                        session, symbol_index, output_path, checkpoint, failure_log, metrics
                    )
                    if timeouts >= MAX_CONSECUTIVE_TIMEOUTS:
                        print("\n  Returning for container restart (Phase 2)...")
                        return False

    except Exception as e:
        print(f"\n  [SESSION ERROR] {e}")
        failure_log.log("session", "mcp_session", str(e))
        return False

    return True


async def run_metadata_generation(workspace: str, output_dir: str, resume: bool = False,
                                   cross_ref_output: Path = None):
    """Main orchestration with auto-restart on OmniSharp failures."""

    workspace_path = str(Path(workspace).resolve())
    output_path = Path(output_dir).resolve()
    output_path.mkdir(parents=True, exist_ok=True)

    checkpoint = Checkpoint(output_path)
    failure_log = FailureLog(output_path)
    metrics = MetricsCollector(output_path, resume=resume)

    if not resume:
        checkpoint.state["started_at"] = datetime.now().isoformat()
        checkpoint.save()

    cs_files = find_cs_files(workspace_path)
    if not cs_files:
        print(f"ERROR: No .cs files found in {workspace_path}")
        sys.exit(1)
    print(f"Found {len(cs_files)} C# files in {workspace_path}")

    if resume:
        print("\nResuming from checkpoint:")
        checkpoint.status()

        # Reset "done" flags if there are failed items to retry
        # This is the key: --resume means "keep what succeeded, retry everything else"
        p1_failed = checkpoint.state.get("phase1_failed_files", [])
        p2_failed = checkpoint.state.get("phase2_failed_symbols", [])

        if checkpoint.phase1_done and p1_failed:
            print(f"\n  Reopening Phase 1: {len(p1_failed)} failed files to retry")
            checkpoint.state["phase1_done"] = False
            checkpoint.state["phase1_failed_files"] = []  # clear so they get retried
            checkpoint.save()

        if checkpoint.phase2_done and p2_failed:
            print(f"  Reopening Phase 2: {len(p2_failed)} failed symbols to retry")
            checkpoint.state["phase2_done"] = False
            checkpoint.state["phase2_failed_symbols"] = []  # clear so they get retried
            checkpoint.save()

        # Also reopen Phase 2 if Phase 1 got new files on this resume
        # (Phase 2 needs to process symbols from newly-succeeded files)
        if not checkpoint.phase2_done or p1_failed:
            checkpoint.state["phase2_done"] = False
            checkpoint.save()

    start_time = time.time()
    max_restarts = 20  # safety limit
    restart_count = 0

    while restart_count < max_restarts:
        if checkpoint.phase1_done and checkpoint.phase2_done:
            break

        if restart_count > 0:
            print(f"\n{'='*60}")
            print(f"RESTARTING container (attempt {restart_count + 1}/{max_restarts})")
            print(f"{'='*60}")
            # Brief pause to let Docker clean up
            await asyncio.sleep(3)

        complete = await run_single_session(
            workspace_path, output_path, cs_files, checkpoint, failure_log, metrics
        )

        if complete:
            break

        restart_count += 1

    if restart_count >= max_restarts:
        print(f"\n  WARNING: Hit max restarts ({max_restarts}). Some files may be incomplete.")

    elapsed = time.time() - start_time

    # Load symbol index for post-processing
    si_path = output_path / "symbol_index.json"
    if si_path.exists():
        with open(si_path) as f:
            symbol_index = json.load(f)
        resolve_intra_file_references(symbol_index, output_path)
        write_per_file_cross_references(symbol_index, output_path, cross_ref_output)

    # Write final summary
    total_syms = sum(len(v) for v in symbol_index.values()) if si_path.exists() else 0
    cross_edges_file = output_path / "cross_file_edges.json"
    intra_edges_file = output_path / "intra_file_edges.json"
    cross_count = len(json.load(open(cross_edges_file))) if cross_edges_file.exists() else 0
    intra_count = len(json.load(open(intra_edges_file))) if intra_edges_file.exists() else 0

    summary = {
        "workspace": workspace_path,
        "generated_at": datetime.now().isoformat(),
        "elapsed_seconds": round(elapsed, 1),
        "total_cs_files": len(cs_files),
        "files_with_symbols": len(symbol_index) if si_path.exists() else 0,
        "total_symbols": total_syms,
        "cross_file_edges": cross_count,
        "intra_file_edges": intra_count,
        "container_restarts": restart_count,
        "total_failures": len(failure_log.failures),
        "output_dir": str(output_path),
        "tools_used": ["code_document_symbols", "code_find_references"],
    }
    write_json(output_path / "summary.json", summary)

    metrics.write_summaries()

    print(f"\n{'='*60}")
    print(f"METADATA GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"  Files processed:      {len(cs_files)}")
    print(f"  Symbols extracted:    {total_syms}")
    print(f"  Cross-file edges:     {cross_count}")
    print(f"  Intra-file edges:     {intra_count}")
    print(f"  Container restarts:   {restart_count}")
    print(f"  Failures:             {len(failure_log.failures)}")
    print(f"  Elapsed time:         {elapsed:.1f}s ({elapsed/3600:.1f} hrs)")
    print(f"  Output:               {output_path}")

    if failure_log.failures:
        print(f"\n  Failure breakdown:")
        failure_log.summary()
        print(f"\n  See {failure_log.path} for full details")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Generate project-wide metadata using multilspy-mcp-server"
    )
    parser.add_argument(
        "--workspace", "-w",
        default=os.path.expanduser("~/Downloads/iMES-master"),
    )
    parser.add_argument(
        "--output", "-o",
        default=os.path.join(os.path.dirname(__file__), "metadata"),
    )
    parser.add_argument("--resume", "-r", action="store_true")
    parser.add_argument("--status", "-s", action="store_true")
    parser.add_argument(
        "--cross-ref-output",
        default=None,
        help="Directory for per-file cross-reference JSONs "
             "(e.g., ../output-imes/metadata-5p/cross_references). "
             "If not set, writes to the --output directory.",
    )
    args = parser.parse_args()

    output_dir = Path(args.output).resolve()
    cross_ref_output = Path(args.cross_ref_output).resolve() if args.cross_ref_output else None

    if args.status:
        if not (output_dir / "checkpoint.json").exists():
            print("No checkpoint found.")
        else:
            checkpoint = Checkpoint(output_dir)
            print("Checkpoint status:")
            checkpoint.status()
            if (output_dir / "failed_files.json").exists():
                print("\nFailure log:")
                FailureLog(output_dir).summary()
        return

    asyncio.run(run_metadata_generation(args.workspace, args.output, args.resume,
                                         cross_ref_output))


if __name__ == "__main__":
    main()
