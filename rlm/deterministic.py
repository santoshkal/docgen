"""
Deterministic section generators — pure-Python generators that emit Markdown
sections from `cross_references` + `page_index` metadata without any LLM call.

Each generator is a pure function:
    generate_*(cross_references, page_index, program_name, source_file, **kwargs) -> str | None

Returns None if required metadata is missing — the orchestrator falls back to
the RLM REPL flow for that section.

Ported from ~/rlm/demo/deterministic_sections.py.
"""

from __future__ import annotations

import traceback
from collections import Counter, defaultdict
from typing import Any, Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Dependency categorization (mirrors the template heuristics)
# ---------------------------------------------------------------------------

FRAMEWORK_PREFIXES = ("System", "Microsoft", "Windows", "Azure")
THIRD_PARTY_PREFIXES = (
    "Newtonsoft", "log4net", "NLog", "Serilog", "NUnit", "xUnit",
    "Moq", "AutoMapper", "Dapper", "MediatR", "FluentValidation",
)
INTERNAL_PREFIXES = ("ng.", "iMES.")


def categorize_dependency(name_or_path: str) -> str:
    s = name_or_path or ""
    if "/" in s:
        root = s.split("/")[0]
        if root.lower() in ("system",) or root.startswith(FRAMEWORK_PREFIXES):
            return "Framework"
        if root.startswith(THIRD_PARTY_PREFIXES):
            return "Third-party"
        return "Internal"
    for p in FRAMEWORK_PREFIXES:
        if s.startswith(p):
            return "Framework"
    for p in THIRD_PARTY_PREFIXES:
        if s.startswith(p):
            return "Third-party"
    for p in INTERNAL_PREFIXES:
        if s.startswith(p):
            return "Internal"
    return "Internal"


def sanitize_mermaid_id(name: str) -> str:
    if not name:
        return "UNKNOWN"
    out = []
    for ch in name:
        if ch.isalnum() or ch == "_":
            out.append(ch)
        else:
            out.append("_")
    result = "".join(out)
    if result and not result[0].isalpha():
        result = "N_" + result
    return result or "UNKNOWN"


def _get_required(cross_references: Optional[Dict], *keys: str) -> Optional[Tuple]:
    if not cross_references or not isinstance(cross_references, dict):
        return None
    result = []
    for k in keys:
        v = cross_references.get(k)
        if v is None:
            return None
        result.append(v)
    return tuple(result)


# ---------------------------------------------------------------------------
# Control Flow Analysis
# ---------------------------------------------------------------------------


def generate_control_flow(
    cross_references: Optional[Dict] = None,
    page_index: Optional[Dict] = None,
    program_name: str = "",
    source_file: str = "",
    **kwargs: Any,
) -> Optional[str]:
    data = _get_required(cross_references, "intra_file_refs", "symbols")
    if data is None:
        return None
    intra_refs, symbols = data
    incoming = (cross_references or {}).get("cross_file_incoming", [])

    edges: set = set()
    for ref in intra_refs:
        src = ref.get("from_symbol", "")
        dst = ref.get("to_symbol", "")
        if src and dst and src != dst:
            edges.add((src, dst))

    mermaid_lines = ["```mermaid", "graph LR"]
    node_ids_seen: set = set()
    for src, dst in sorted(edges):
        src_id = sanitize_mermaid_id(src)
        dst_id = sanitize_mermaid_id(dst)
        if src_id not in node_ids_seen:
            mermaid_lines.append(f'  {src_id}["{src}"]')
            node_ids_seen.add(src_id)
        if dst_id not in node_ids_seen:
            mermaid_lines.append(f'  {dst_id}["{dst}"]')
            node_ids_seen.add(dst_id)
        mermaid_lines.append(f"  {src_id} --> {dst_id}")

    for ref in incoming:
        ext_sym = ref.get("symbol", "")
        if not ext_sym:
            continue
        ext_id = "EXT_" + sanitize_mermaid_id(ext_sym)
        src_file = ref.get("defined_in", "")
        if ext_id not in node_ids_seen:
            mermaid_lines.append(f'  {ext_id}[/"{ext_sym}<br/>({src_file})"/]')
            node_ids_seen.add(ext_id)
        prog_id = sanitize_mermaid_id(program_name or "CURRENT")
        if prog_id not in node_ids_seen:
            mermaid_lines.append(f'  {prog_id}(["{program_name or "CURRENT"}"])')
            node_ids_seen.add(prog_id)
        mermaid_lines.append(f"  {prog_id} -.-> {ext_id}")

    mermaid_lines.extend([
        "",
        "  classDef external fill:#aff,stroke:#06c,stroke-width:2px;",
        "  classDef method fill:#fff,stroke:#333,stroke-width:1px;",
        "```",
    ])
    mermaid = "\n".join(mermaid_lines)

    calls_by_caller: Dict[str, List[Dict]] = defaultdict(list)
    for ref in incoming:
        line = ref.get("referenced_at_line", 0)
        enclosing = _find_enclosing_symbol(line, symbols)
        caller_name = enclosing["name"] if enclosing else "(top-level)"
        calls_by_caller[caller_name].append(ref)

    ext_context_lines: List[str] = []
    for caller, refs in sorted(calls_by_caller.items()):
        ext_context_lines.append(f"### `{caller}`")
        ext_context_lines.append("")
        for ref in sorted(refs, key=lambda r: r.get("referenced_at_line", 0)):
            sym = ref.get("symbol", "?")
            src = ref.get("defined_in", "?")
            line = ref.get("referenced_at_line", "?")
            category = categorize_dependency(src)
            ext_context_lines.append(
                f"- `{sym}` ({category}) from `{src}` \u2014 referenced at line {line}"
            )
        ext_context_lines.append("")
    ext_context = "\n".join(ext_context_lines) if ext_context_lines else "No external calls detected."

    calls_out_per_method: Dict[str, int] = defaultdict(int)
    for ref in intra_refs:
        src = ref.get("from_symbol", "")
        if src:
            calls_out_per_method[src] += 1
    for ref in incoming:
        line = ref.get("referenced_at_line", 0)
        enclosing = _find_enclosing_symbol(line, symbols)
        if enclosing:
            calls_out_per_method[enclosing["name"]] += 1

    methods = [s for s in symbols if s.get("kind_name") in ("METHOD", "CONSTRUCTOR")]
    table_lines = [
        "| Method | Line | Calls Out | Kind | Complexity | Role |",
        "|---|---|---|---|---|---|",
    ]
    for m in sorted(methods, key=lambda x: x.get("line", 0)):
        name = m["name"]
        line = m.get("line", "-")
        calls_out = calls_out_per_method.get(name, 0)
        kind = m.get("kind_name", "METHOD")
        complexity = _complexity_bucket(calls_out)
        role = _infer_role(name, kind, calls_out)
        table_lines.append(
            f"| `{name}` | {line} | {calls_out} | {kind} | {complexity} | {role} |"
        )
    complexity_table = "\n".join(table_lines) if methods else "No methods found."

    return f"""## High-Level Control Flow with External Calls

{mermaid}

## External Call Context

{ext_context}

## Method Complexity & Business Role

{complexity_table}
"""


def _find_enclosing_symbol(line: int, symbols: List[Dict]) -> Optional[Dict]:
    best: Optional[Dict] = None
    best_range: Optional[int] = None
    for s in symbols:
        start = s.get("range_start")
        end = s.get("range_end")
        if start is None or end is None:
            continue
        if start <= line <= end:
            size = end - start
            if best is None or (best_range is not None and size < best_range):
                best = s
                best_range = size
    return best


def _complexity_bucket(calls_out: int) -> str:
    if calls_out == 0:
        return "Low"
    if calls_out <= 3:
        return "Low"
    if calls_out <= 8:
        return "Medium"
    return "High"


def _infer_role(name: str, kind: str, calls_out: int) -> str:
    n = name.lower()
    if kind == "CONSTRUCTOR":
        return "Entry point"
    if "init" in n:
        return "Initialization"
    if any(k in n for k in ("load", "get", "fetch", "read")):
        return "Data access"
    if any(k in n for k in ("validate", "check", "verify", "ensure")):
        return "Validation"
    if any(k in n for k in ("error", "exception", "fail", "handle")):
        return "Error handling"
    if calls_out > 5:
        return "Core business logic"
    if calls_out == 0:
        return "Helper/utility"
    return "Core business logic"


# ---------------------------------------------------------------------------
# Assembly References & Dependencies
# ---------------------------------------------------------------------------


def generate_assembly_references(
    cross_references: Optional[Dict] = None,
    page_index: Optional[Dict] = None,
    program_name: str = "",
    source_file: str = "",
    **kwargs: Any,
) -> Optional[str]:
    if not cross_references or not isinstance(cross_references, dict):
        return None
    incoming = cross_references.get("cross_file_incoming") or []
    if not incoming:
        return None

    by_file: Dict[str, List[Dict]] = defaultdict(list)
    for ref in incoming:
        src = ref.get("defined_in", "")
        if src:
            by_file[src].append(ref)

    table_lines = [
        "| Dependency | Category | Usage Count | Used At Lines | Importance |",
        "|---|---|---|---|---|",
    ]
    for src_file, refs in sorted(by_file.items(), key=lambda kv: -len(kv[1])):
        cat = categorize_dependency(src_file)
        count = len(refs)
        lines = sorted(set(r.get("referenced_at_line", 0) for r in refs))
        lines_str = ", ".join(str(x) for x in lines[:10]) + ("..." if len(lines) > 10 else "")
        importance = "High" if count >= 10 else "Medium" if count >= 3 else "Low"
        table_lines.append(
            f"| `{src_file}` | {cat} | {count} | {lines_str} | {importance} |"
        )
    dep_table = "\n".join(table_lines)

    prog_id = sanitize_mermaid_id(program_name or "CURRENT")
    mermaid_lines = [
        "```mermaid",
        "graph LR",
        f'  {prog_id}["{program_name or "CURRENT"}"]',
    ]
    node_ids = {prog_id}
    for src_file, refs in sorted(by_file.items()):
        dep_id = sanitize_mermaid_id(src_file)
        if dep_id in node_ids:
            dep_id = dep_id + "_dep"
        mermaid_lines.append(f'  {dep_id}["{src_file}"]')
        mermaid_lines.append(f"  {prog_id} -.-> {dep_id}")
        node_ids.add(dep_id)

    mermaid_lines.extend([
        "",
        "  classDef current fill:#f9f,stroke:#333,stroke-width:4px;",
        "  classDef framework fill:#ddd,stroke:#333,stroke-width:1px;",
        "  classDef thirdparty fill:#fc9,stroke:#333,stroke-width:1px;",
        "  classDef internal fill:#9cf,stroke:#333,stroke-width:2px;",
        f"  class {prog_id} current;",
        "```",
    ])
    mermaid = "\n".join(mermaid_lines)

    detail_lines: List[str] = []
    for src_file, refs in sorted(by_file.items(), key=lambda kv: -len(kv[1])):
        cat = categorize_dependency(src_file)
        symbols_used = Counter(r.get("symbol", "") for r in refs if r.get("symbol"))
        detail_lines.append(f"### `{src_file}` ({cat})")
        detail_lines.append("")
        detail_lines.append(f"**Reference Count**: {len(refs)}")
        detail_lines.append("")
        detail_lines.append("**Symbols Used**:")
        for sym, count in symbols_used.most_common():
            lines = sorted(set(
                r.get("referenced_at_line", 0) for r in refs if r.get("symbol") == sym
            ))
            lines_str = ", ".join(str(x) for x in lines[:15])
            if len(lines) > 15:
                lines_str += "..."
            detail_lines.append(f"- `{sym}` ({count}x) \u2014 lines {lines_str}")
        detail_lines.append("")
    detail = "\n".join(detail_lines)

    return f"""## Dependency Usage & Category

{dep_table}

## Dependency Hierarchy

{mermaid}

## Detailed Dependency Analysis

{detail}
"""


# ---------------------------------------------------------------------------
# Code References
# ---------------------------------------------------------------------------


def generate_code_references(
    cross_references: Optional[Dict] = None,
    page_index: Optional[Dict] = None,
    program_name: str = "",
    source_file: str = "",
    **kwargs: Any,
) -> Optional[str]:
    if not cross_references or not isinstance(cross_references, dict):
        return None
    symbols = cross_references.get("symbols") or []
    if not symbols:
        return None

    by_kind: Dict[str, List[Dict]] = defaultdict(list)
    for s in symbols:
        by_kind[s.get("kind_name", "UNKNOWN")].append(s)

    order = ["NAMESPACE", "CLASS", "INTERFACE", "STRUCT", "ENUM",
             "CONSTRUCTOR", "METHOD", "PROPERTY", "FIELD"]
    plural = {
        "NAMESPACE": "Namespaces", "CLASS": "Classes", "INTERFACE": "Interfaces",
        "STRUCT": "Structs", "ENUM": "Enums", "CONSTRUCTOR": "Constructors",
        "METHOD": "Methods", "PROPERTY": "Properties", "FIELD": "Fields",
    }

    lines = ["### Quick Reference Links", ""]
    for kind in order:
        if kind not in by_kind:
            continue
        items = sorted(by_kind[kind], key=lambda x: x.get("line", 0))
        lines.append(f"#### {plural.get(kind, kind.title() + 's')}")
        lines.append("")
        for s in items:
            name = s.get("name", "?")
            line = s.get("line", "-")
            parent = s.get("parent")
            rng_start = s.get("range_start", "-")
            rng_end = s.get("range_end", "-")
            parent_str = f" (in `{parent}`)" if parent else ""
            lines.append(
                f"- `{name}`{parent_str} \u2014 line {line}, range {rng_start}-{rng_end}"
            )
        lines.append("")

    for kind, items in sorted(by_kind.items()):
        if kind in order:
            continue
        items = sorted(items, key=lambda x: x.get("line", 0))
        lines.append(f"#### {plural.get(kind, kind.title() + 's')}")
        lines.append("")
        for s in items:
            name = s.get("name", "?")
            line = s.get("line", "-")
            lines.append(f"- `{name}` \u2014 line {line}")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Technical Details
# ---------------------------------------------------------------------------


def generate_technical_details(
    cross_references: Optional[Dict] = None,
    page_index: Optional[Dict] = None,
    program_name: str = "",
    source_file: str = "",
    **kwargs: Any,
) -> Optional[str]:
    if not cross_references or not isinstance(cross_references, dict):
        return None

    symbols = cross_references.get("symbols") or []
    outgoing = cross_references.get("cross_file_outgoing") or []
    incoming = cross_references.get("cross_file_incoming") or []
    intra_refs = cross_references.get("intra_file_refs") or []

    kind_counts = Counter(s.get("kind_name", "UNKNOWN") for s in symbols)

    total_lines = 0
    if page_index and isinstance(page_index, dict):
        for chunk in page_index.get("structure", []):
            end = chunk.get("line_end", 0)
            if end > total_lines:
                total_lines = end
    if total_lines == 0 and symbols:
        total_lines = max((s.get("range_end", 0) for s in symbols), default=0)

    chunk_count = 0
    if page_index and isinstance(page_index, dict):
        chunk_count = len(page_index.get("structure", []))

    metrics_rows = [
        ("Total Lines", str(total_lines) if total_lines else "N/A"),
        ("Total Symbols", str(len(symbols))),
        ("Namespaces", str(kind_counts.get("NAMESPACE", 0))),
        ("Classes", str(kind_counts.get("CLASS", 0))),
        ("Interfaces", str(kind_counts.get("INTERFACE", 0))),
        ("Structs", str(kind_counts.get("STRUCT", 0))),
        ("Enums", str(kind_counts.get("ENUM", 0))),
        ("Methods", str(kind_counts.get("METHOD", 0))),
        ("Constructors", str(kind_counts.get("CONSTRUCTOR", 0))),
        ("Properties", str(kind_counts.get("PROPERTY", 0))),
        ("Fields", str(kind_counts.get("FIELD", 0))),
        ("Intra-file Edges", str(len(intra_refs))),
        ("Inbound Dependencies (symbols this file uses)", str(len(incoming))),
        ("Outbound References (this file's symbols used elsewhere)", str(len(outgoing))),
        ("Documentation Chunks", str(chunk_count) if chunk_count else "N/A"),
    ]
    metrics_table = "| Metric | Value |\n|---|---|\n" + "\n".join(
        f"| {k} | {v} |" for k, v in metrics_rows
    )

    deps_by_file: Dict[str, List[Dict]] = defaultdict(list)
    for ref in incoming:
        src = ref.get("defined_in", "")
        if src:
            deps_by_file[src].append(ref)

    dep_rows = [
        "| Dependency | Category | Reference Count | Line Count |",
        "|---|---|---|---|",
    ]
    for src_file, refs in sorted(deps_by_file.items(), key=lambda kv: -len(kv[1])):
        cat = categorize_dependency(src_file)
        line_count = len(set(r.get("referenced_at_line", 0) for r in refs))
        dep_rows.append(f"| `{src_file}` | {cat} | {len(refs)} | {line_count} |")
    deps_table = "\n".join(dep_rows)

    return f"""## Code Metrics

{metrics_table}

## Dependencies Matrix

{deps_table}
"""


# ---------------------------------------------------------------------------
# Data Flow Analysis (uses page_index block data_flow fields)
# ---------------------------------------------------------------------------


def generate_data_flow(
    cross_references: Optional[Dict] = None,
    page_index: Optional[Dict] = None,
    program_name: str = "",
    source_file: str = "",
    **kwargs: Any,
) -> Optional[str]:
    if not page_index or not isinstance(page_index, dict):
        return None

    data_flow_entries: List[Tuple[str, Any, List[str]]] = []
    for chunk in page_index.get("structure", []):
        for block in chunk.get("nodes", []):
            flow = block.get("data_flow")
            if flow:
                data_flow_entries.append((
                    block.get("title", "?"),
                    block.get("line_num", "-"),
                    flow if isinstance(flow, list) else [str(flow)],
                ))

    if not data_flow_entries:
        return None

    import re as _re
    mermaid_lines = ["```mermaid", "graph LR"]
    sources: set = set()
    sinks: set = set()
    processes: set = set()
    edges: List[Tuple[str, str]] = []

    for block_title, _line, flows in data_flow_entries:
        block_node = sanitize_mermaid_id(block_title)
        short_title = block_title.split("(")[0].strip()
        processes.add((block_node, short_title))
        for entry in flows:
            s = str(entry)
            reads = _re.findall(r"READS?\s+([^;:]+?)(?:[;:]|WRITES|TRANSFORMS|$)", s, _re.IGNORECASE)
            writes = _re.findall(r"WRITES?\s+([^;:]+?)(?:[;:]|TRANSFORMS|$)", s, _re.IGNORECASE)
            for group in reads:
                for item in [x.strip() for x in group.split(",") if x.strip()]:
                    item_clean = item.strip(" `.,")
                    if item_clean:
                        src_node = "SRC_" + sanitize_mermaid_id(item_clean)
                        sources.add((src_node, item_clean))
                        edges.append((src_node, block_node))
            for group in writes:
                for item in [x.strip() for x in group.split(",") if x.strip()]:
                    item_clean = item.strip(" `.,")
                    if item_clean:
                        sink_node = "SINK_" + sanitize_mermaid_id(item_clean)
                        sinks.add((sink_node, item_clean))
                        edges.append((block_node, sink_node))

    declared: set = set()
    for node_id, label in sources:
        if node_id not in declared:
            mermaid_lines.append(f'  {node_id}[/"{label}"/]')
            declared.add(node_id)
    for node_id, label in processes:
        if node_id not in declared:
            mermaid_lines.append(f'  {node_id}["{label}"]')
            declared.add(node_id)
    for node_id, label in sinks:
        if node_id not in declared:
            mermaid_lines.append(f'  {node_id}[\\"{label}"\\]')
            declared.add(node_id)
    for src, dst in sorted(set(edges)):
        mermaid_lines.append(f"  {src} --> {dst}")
    mermaid_lines.append("```")
    mermaid = "\n".join(mermaid_lines)

    transformation_lines: List[str] = []
    for block_title, line_num, flows in data_flow_entries:
        transformation_lines.append(f"**{block_title}** (line {line_num})")
        for entry in flows:
            transformation_lines.append(f"- {entry}")
        transformation_lines.append("")
    transformations = "\n".join(transformation_lines)

    return f"""## Data Flow Diagram (Key Items)

{mermaid}

## Data Transformations

{transformations}
"""


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

GENERATORS = {
    "control-flow-analysis": generate_control_flow,
    "assembly-references": generate_assembly_references,
    "code-references": generate_code_references,
    "technical-details": generate_technical_details,
    "data-flow-analysis": generate_data_flow,
}


def generate(section_id: str, **kwargs: Any) -> Optional[str]:
    gen = GENERATORS.get(section_id)
    if not gen:
        return None
    try:
        return gen(**kwargs)
    except Exception as e:
        print(f"  WARNING: Deterministic generator for {section_id!r} failed: {e}")
        traceback.print_exc()
        return None
