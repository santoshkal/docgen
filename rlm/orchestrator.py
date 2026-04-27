"""
Phase 2 orchestrator — RLM REPL + PageIndex + deterministic generators.

Entry point:
    run_phase2_rlm(state, code_explanation, llm_config, fallback_manager, full_config)
        → Dict[section_id, section_markdown]

Flow per source file:
    1. Build PageIndex tree from the Phase 1 code-explanation markdown (extract
       or llm mode, per config).
    2. Load any cross_references JSON for this source file, plus all other
       metadata already on `state`.
    3. Iterate template sections in order; for each:
         - deterministic generator if eligible (falls through to RLM on failure)
         - RLM REPL iteration loop otherwise
         - skip if listed under `rlm.skip_sections`
    4. Return the section_outputs dict consumed by the existing Phase 3
       assembly.

Fallback behavior (mirrors LLMFallbackManager):
    - Primary models come from `llm_config.rlm.root_model` / `sub_model`.
    - On any sub-LLM / root-LLM unrecoverable error, `fallback_manager.trigger_fallback()`
      flips session-wide state; subsequent calls resolve models from
      `llm_config.fallback.rlm.root_model` / `sub_model` instead.
"""

from __future__ import annotations

import asyncio
import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

from rlm import deterministic, pageindex
from rlm.pipeline_repl import PipelineREPL, call_claude
from rlm.rlm_loop import calibrate_token_ratio, run_rlm_section


# Default section lists (match ~/rlm/demo/pipeline-config.yaml)
DEFAULT_RLM_SECTIONS = [
    "executive-summary",
    "program-structure",
    "control-flow-analysis",
    "data-flow-analysis",
    "inter-program-communication",
    "business-logic",
    "error-handling",
    "technical-details",
    "code-references",
]

DEFAULT_SKIP_SECTIONS = {
    "detailed-code-explanation",
}

DEFAULT_DETERMINISTIC_SECTIONS = [
    "document-header",
    "control-flow-analysis",
    "assembly-references",
    "code-references",
    "technical-details",
    "metadata-appendix",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _safe_filename(file_path: str) -> str:
    return file_path.replace("/", "__").replace("\\", "__")


def _resolve_pageindex_path(
    output_dir: Path, program_name: str, full_config: Dict[str, Any]
) -> Path:
    """Resolve where the PageIndex JSON lives for this program."""
    pi_cfg = (full_config or {}).get("pageindex", {}) or {}
    if pi_cfg.get("output_dir"):
        base = Path(pi_cfg["output_dir"]).expanduser()
    else:
        base = Path(output_dir) / "page_index"
    return base / f"{program_name}.pageindex.json"


def _build_rlm_llm_config(
    llm_config: Dict[str, Any],
) -> Dict[str, Any]:
    """Extract the subset of llm_config the RLM modules expect."""
    rlm_primary = llm_config.get("rlm", {}) or {}
    return {
        "root_model": rlm_primary.get("root_model") or llm_config.get("root_model")
            or llm_config.get("model", "claude-sonnet-4-5"),
        "sub_model": rlm_primary.get("sub_model") or llm_config.get("sub_model")
            or llm_config.get("model", "claude-sonnet-4-5"),
        "max_output_tokens": rlm_primary.get("max_output_tokens",
            llm_config.get("max_output_tokens", 16384)),
        "max_thinking_tokens": rlm_primary.get("max_thinking_tokens",
            llm_config.get("max_thinking_tokens", 0)),
        "max_iterations": rlm_primary.get("max_iterations",
            llm_config.get("max_iterations", 10)),
    }


def _build_fallback_rlm_config(
    llm_config: Dict[str, Any],
    primary_rlm: Dict[str, Any],
) -> Dict[str, Any]:
    """Extract the fallback RLM config, inheriting from primary when unset."""
    fb = (llm_config.get("fallback") or {}).get("rlm") or {}
    return {
        "root_model": fb.get("root_model", primary_rlm["root_model"]),
        "sub_model": fb.get("sub_model", primary_rlm["sub_model"]),
        "max_output_tokens": fb.get("max_output_tokens", primary_rlm["max_output_tokens"]),
        "max_thinking_tokens": fb.get("max_thinking_tokens", primary_rlm["max_thinking_tokens"]),
        "max_iterations": fb.get("max_iterations", primary_rlm["max_iterations"]),
    }


def _build_metadata_bundle(
    state: Dict[str, Any],
    page_index: Dict[str, Any],
    cross_references: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    """Assemble the metadata dict passed into the REPL as `metadata`."""
    keys = [
        "structural_outline", "symbol_table", "static_analysis",
        "syntax_tree", "control_flow_graph",
        "superbol_symbols", "superbol_cfg", "gnucobol_analysis", "ctags_outline",
        "chunking_boundaries", "treesitter_graph",
    ]
    bundle: Dict[str, Any] = {"page_index": page_index}
    if cross_references is not None:
        bundle["cross_references"] = cross_references
    for k in keys:
        v = state.get(k)
        if v:
            bundle[k] = v
    return bundle


def _load_cross_references(
    full_config: Dict[str, Any], relative_source: str, program_name: str
) -> Optional[Dict[str, Any]]:
    """Look up the per-source-file cross_references JSON.

    Uses `output.cross_references_dir`. If a direct file path happens to be
    provided (not a directory), that file is loaded instead.
    """
    xr_cfg_val = (full_config or {}).get("output", {}).get("cross_references_dir")
    if not xr_cfg_val:
        return None

    xr_path = Path(xr_cfg_val).expanduser()

    # Direct file path
    if xr_path.is_file():
        with open(xr_path, "r", encoding="utf-8") as f:
            return json.load(f)

    # Directory — resolve by source_file name
    if xr_path.is_dir():
        # First try the full relative path: "Dir/File.cs" -> "Dir__File.cs.json"
        if relative_source:
            candidate = xr_path / f"{_safe_filename(relative_source)}.json"
            if candidate.exists():
                with open(candidate, "r", encoding="utf-8") as f:
                    return json.load(f)
        # Fallback: glob for *__{program_name}.{ext}.json
        matches = (
            list(xr_path.glob(f"*__{program_name}.cs.json"))
            + list(xr_path.glob(f"*__{program_name}.cbl.json"))
            + list(xr_path.glob(f"*__{program_name}.json"))
        )
        if len(matches) == 1:
            with open(matches[0], "r", encoding="utf-8") as f:
                return json.load(f)
        if len(matches) > 1:
            print(
                f"  WARNING: multiple cross-reference files match {program_name}; "
                f"set source_file to disambiguate: {[m.name for m in matches]}"
            )

    return None


# ---------------------------------------------------------------------------
# Fallback-aware model accessors
# ---------------------------------------------------------------------------


def _make_model_getters(
    primary_rlm: Dict[str, Any],
    fallback_rlm: Dict[str, Any],
    fallback_manager: Optional[Any],
):
    """Return (get_root_model, get_sub_model) callables that observe fallback state."""
    def _active() -> bool:
        return bool(
            fallback_manager
            and getattr(fallback_manager, "is_fallback_active", lambda: False)()
        )

    def get_root_model() -> str:
        return fallback_rlm["root_model"] if _active() else primary_rlm["root_model"]

    def get_sub_model() -> str:
        return fallback_rlm["sub_model"] if _active() else primary_rlm["sub_model"]

    return get_root_model, get_sub_model


# ---------------------------------------------------------------------------
# PageIndex generation
# ---------------------------------------------------------------------------


def _generate_pageindex(
    code_explanation: str,
    pi_cfg: Dict[str, Any],
    pi_out_path: Path,
) -> Dict[str, Any]:
    """Build a PageIndex tree and persist it; reuse existing file unless asked
    to regenerate."""
    mode = pi_cfg.get("mode", "extract")
    include_text = pi_cfg.get("include_text", True)
    regenerate = pi_cfg.get("regenerate", True)

    if pi_out_path.exists() and not regenerate:
        print(f"  → PageIndex exists, reusing: {pi_out_path}")
        with open(pi_out_path, "r", encoding="utf-8") as f:
            return json.load(f)

    print(f"  → Building PageIndex (mode={mode})...")
    t0 = time.time()
    llm_mode_kwargs: Dict[str, Any] = {}
    if mode == "llm":
        llm_mode_kwargs["model"] = pi_cfg.get("model", "claude-sonnet-4-20250514")
        if pi_cfg.get("concurrency"):
            llm_mode_kwargs["max_concurrent"] = pi_cfg["concurrency"]
        if pi_cfg.get("thinning"):
            llm_mode_kwargs["if_thinning"] = True
            llm_mode_kwargs["min_token_threshold"] = pi_cfg.get("min_token_threshold", 500)

    pi = pageindex.build_pageindex(
        code_explanation,
        mode=mode,
        include_text=include_text,
        **llm_mode_kwargs,
    )
    elapsed = time.time() - t0

    pi_out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(pi_out_path, "w", encoding="utf-8") as f:
        json.dump(pi, f, indent=2)

    total_nodes = pageindex.count_nodes(pi.get("structure", []))
    print(
        f"    PageIndex: {total_nodes} nodes, "
        f"{pi_out_path.stat().st_size:,} bytes, {elapsed:.1f}s → {pi_out_path}"
    )
    return pi


# ---------------------------------------------------------------------------
# Section processing
# ---------------------------------------------------------------------------


def _format_section_instruction(section: Dict[str, Any], depth: int = 0) -> str:
    """Render the template's section (and its sub-sections) as one instruction blob."""
    parts: List[str] = []
    prefix = "#" * (depth + 2)
    title = section.get("title", section.get("id", ""))
    parts.append(f"{prefix} {title}")
    if (instruction := section.get("instruction")):
        parts.append(instruction.strip())
    if (template := section.get("template")):
        parts.append(f"Output template:\n{template.strip()}")
    for sub in section.get("sections", []) or []:
        parts.append(_format_section_instruction(sub, depth + 1))
    return "\n\n".join(parts)


async def _process_section_async(
    section_id: str,
    section_title: str,
    instruction: str,
    code_explanation: str,
    metadata: Dict[str, Any],
    program_name: str,
    log_dir: Path,
    primary_rlm: Dict[str, Any],
    fallback_rlm: Dict[str, Any],
    fallback_manager: Optional[Any],
    sub_llm_max_chars: int,
    chars_per_token: float,
    coverage_log_path: Optional[Path] = None,
) -> str:
    """Run the RLM loop once for a section, with one automatic fallback retry."""
    get_root_model, get_sub_model = _make_model_getters(
        primary_rlm, fallback_rlm, fallback_manager
    )

    print(f"\n{'='*70}")
    print(f"Processing (RLM): {section_title} ({section_id})")
    print(f"{'='*70}")
    print(f"  Max iterations: {primary_rlm['max_iterations']}")
    print(f"  Context size: {len(code_explanation):,} chars")

    async def _run_once() -> str:
        active_config = (
            fallback_rlm
            if fallback_manager and fallback_manager.is_fallback_active()
            else primary_rlm
        )
        repl = PipelineREPL(
            llm_config=active_config,
            fallback_manager=fallback_manager,
            get_sub_model=get_sub_model,
            coverage_log_path=coverage_log_path,
            section_id=section_id,
        )
        try:
            repl.add_context(code_explanation, "context")
            repl.add_context(metadata, "metadata")
            repl.add_context(instruction, "section_instruction")
            repl.add_context(section_title, "section_title")
            repl.add_context(program_name, "program_name")

            root_prompt = (
                f"Generate the '{section_title}' section of documentation for the program "
                f"{program_name}. Follow the section_instruction variable for the required format "
                f"and content. Use the context variable (detailed code explanation) and metadata "
                f"variable (structured analysis) as your information sources."
            )

            text, stats = await run_rlm_section(
                repl=repl,
                root_prompt=root_prompt,
                llm_config=active_config,
                max_iterations=active_config["max_iterations"],
                context_length=len(code_explanation),
                log_dir=log_dir,
                section_id=section_id,
                sub_llm_max_chars=sub_llm_max_chars,
                chars_per_token=chars_per_token,
                fallback_manager=fallback_manager,
                get_root_model=get_root_model,
            )
            print(f"  → Stats: {stats}")
            return text
        finally:
            repl.cleanup()

    try:
        return await _run_once()
    except Exception as e:
        # If fallback was just triggered by the RLM loop, retry once on the
        # fallback models.
        if (
            fallback_manager
            and getattr(fallback_manager, "has_fallback", lambda: False)()
            and fallback_manager.is_fallback_active()
        ):
            print(f"  → Retrying section {section_id!r} on fallback models after: {e}")
            try:
                return await _run_once()
            except Exception as e2:
                return (
                    f"## {section_title}\n\n"
                    f"**Generation Failed (after fallback)**\n\n"
                    f"```\n{e2}\n```\n"
                )
        return (
            f"## {section_title}\n\n"
            f"**Generation Failed**\n\n"
            f"```\n{e}\n```\n"
        )


# ---------------------------------------------------------------------------
# Node-coverage verification + deterministic gap-fill
# ---------------------------------------------------------------------------


def _read_processed_node_ids(path: Path) -> set:
    """Return the set of node IDs recorded in a coverage-log JSONL file.

    Only successful, node-scoped calls count: `node_id` non-null and
    `is_error == False`. The log is written by the Python plumbing in
    `PipelineREPL`, so the contents reflect what was *actually* called — not
    what the root LLM claimed.
    """
    processed: set = set()
    if not path.exists():
        return processed
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if entry.get("is_error"):
                continue
            nid = entry.get("node_id")
            if nid is not None:
                processed.add(str(nid))
    return processed


def _find_node_by_id(
    pi: Dict[str, Any], node_id: str
) -> Optional[Dict[str, Any]]:
    """Depth-first search for a node with the given `node_id` in the tree."""
    def _walk(nodes: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        for n in nodes or []:
            if str(n.get("node_id")) == str(node_id):
                return n
            found = _walk(n.get("nodes", []))
            if found is not None:
                return found
        return None

    return _walk(pi.get("structure", []) if isinstance(pi, dict) else [])


def _assemble_node_context(node: Dict[str, Any]) -> str:
    """Render a PageIndex node as an enriched prompt context string.

    Mirrors `assemble_block_context` from the root-LLM worked example so the
    gap-fill sub-LLM sees the same format the root LLM would have sent.
    """
    parts: List[str] = []
    title = node.get("title", f"Node {node.get('node_id', '?')}")
    parts.append(f"Node: {title}")
    if node.get("summary"):
        parts.append(f"\nSummary: {node['summary']}")
    if node.get("tags"):
        parts.append(f"\nTags: {', '.join(str(t) for t in node['tags'])}")
    if node.get("retrieval_questions"):
        parts.append("\nRetrieval Questions:")
        for q in node["retrieval_questions"]:
            parts.append(f"  - {q}")
    if node.get("purpose"):
        parts.append("\nPurpose:")
        for k, v in (node.get("purpose") or {}).items():
            parts.append(f"  {k.replace('_', ' ').title()}: {v}")
    if node.get("technical_details"):
        parts.append("\nTechnical Details:")
        for k, v in (node.get("technical_details") or {}).items():
            parts.append(f"  {k.replace('_', ' ').title()}: {v}")
    if node.get("cross_references"):
        parts.append("\nCross-References:")
        for k, v in (node.get("cross_references") or {}).items():
            parts.append(f"  {k.replace('_', ' ').title()}: {v}")
    if node.get("call_flow"):
        parts.append("\nCall Flow:")
        for entry in node["call_flow"]:
            parts.append(f"  {entry}")
    if node.get("data_flow"):
        parts.append("\nData Flow:")
        for entry in node["data_flow"]:
            parts.append(f"  {entry}")
    if node.get("text"):
        parts.append(f"\n--- Full Text ---\n{node['text']}")
    return "\n".join(parts)


async def _gap_fill_missing_nodes(
    missing_ids: List[str],
    page_index: Dict[str, Any],
    section_title: str,
    section_instruction: str,
    program_name: str,
    llm_config: Dict[str, Any],
    fallback_manager: Optional[Any],
    get_sub_model: Callable[[], str],
    coverage_log_path: Optional[Path],
    section_id: str,
) -> List[Tuple[str, str]]:
    """Run a deterministic sub-LLM pass over each missing node.

    Returns a list of `(node_id, finding_text)` pairs — one per missing node.
    Each call is recorded in the coverage log the same way a normal sub-LLM
    call would be, so a second coverage check after gap-fill will show 100%.
    """
    query_template = (
        f"Extract information relevant to the '{section_title}' documentation section "
        f"for program {program_name} from this PageIndex node. "
        f"Return ONLY facts explicitly stated — do NOT infer or invent names, values, "
        f"or line numbers. No preambles. If nothing in the node is relevant to this "
        f"section, respond with exactly: 'No content relevant to this section.'\n\n"
        f"Section instruction:\n{section_instruction}\n\n"
    )

    async def _run_one(node_id: str) -> Tuple[str, str]:
        node = _find_node_by_id(page_index, node_id)
        if node is None:
            return node_id, f"[gap-fill] node '{node_id}' not found in PageIndex"
        prompt = query_template + _assemble_node_context(node)
        try:
            text, result_info = await call_claude(
                prompt=prompt,
                model=get_sub_model(),
                max_thinking_tokens=llm_config.get("max_thinking_tokens"),
                max_output_tokens=llm_config.get("max_output_tokens"),
                fallback_manager=fallback_manager,
                get_model=get_sub_model,
            )
        except Exception as e:
            text = f"[gap-fill error] {type(e).__name__}: {e}"
            result_info = None

        # Append a coverage-log entry for the gap-fill call so a follow-up
        # diff would show the node as processed.
        if coverage_log_path is not None:
            entry = {
                "timestamp": datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
                "section_id": section_id,
                "node_id": str(node_id),
                "call_type": "gap_fill",
                "prompt_length": len(prompt),
                "response_length": len(text),
                "is_error": "[gap-fill error]" in text,
                "model": get_sub_model(),
            }
            try:
                coverage_log_path.parent.mkdir(parents=True, exist_ok=True)
                with open(coverage_log_path, "a", encoding="utf-8") as f:
                    json.dump(entry, f, default=str)
                    f.write("\n")
            except OSError:
                pass

        return node_id, text

    # Limit concurrency so we don't overrun rate limits; the semaphore default
    # matches PipelineREPL.
    sem = asyncio.Semaphore(os.cpu_count() or 4)

    async def _throttled(nid: str) -> Tuple[str, str]:
        async with sem:
            return await _run_one(nid)

    results = await asyncio.gather(*(_throttled(nid) for nid in missing_ids))
    return list(results)


def _format_gap_fill_annex(
    pairs: List[Tuple[str, str]],
    section_title: str,
) -> str:
    """Render gap-fill findings as a markdown annex appended to the section."""
    if not pairs:
        return ""
    lines = [
        "",
        "---",
        "",
        "### Coverage Annex — Gap-Fill Findings",
        "",
        "> The Phase 2 coverage verifier found PageIndex nodes that were not "
        "processed by the RLM loop. The sections below are deterministic "
        "per-node extracts (one sub-LLM call per missing node) generated to "
        "complete coverage for this section.",
        "",
    ]
    for node_id, text in pairs:
        clean = text.strip()
        if not clean or clean == "No content relevant to this section.":
            continue
        lines.append(f"#### Node `{node_id}`")
        lines.append("")
        lines.append(clean)
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Top-level entry point
# ---------------------------------------------------------------------------


def run_phase2_rlm(
    state: Dict[str, Any],
    code_explanation: str,
    llm_config: Dict[str, Any],
    fallback_manager: Optional[Any] = None,
    full_config: Optional[Dict[str, Any]] = None,
) -> Dict[str, str]:
    """
    Phase 2 (RLM + PageIndex). Replaces `run_phase2_sections`.

    Args:
        state: AgentState-shaped dict. Reads template, program_name, output_dir,
            cobol_file_path / source_file_path, and any metadata fields.
        code_explanation: Phase 1 markdown output.
        llm_config: Full LLM config (primary + optional fallback.rlm sub-block).
        fallback_manager: Shared LLMFallbackManager; trigger state propagates
            across RLM sub/root LLM calls and sections.
        full_config: Full YAML config dict; reads `pageindex.*`, `rlm.*`,
            `output.cross_references_dir`, and `output.docs_path`.

    Returns:
        Dict mapping section_id → generated markdown content. Compatible with
        the existing Phase 3 assembler.
    """
    full_config = full_config or {}
    program_name = state["program_name"]
    template = state.get("template", {}) or {}
    sections = template.get("sections", []) or []

    output_dir_cfg = (
        full_config.get("output", {}).get("docs_path")
        or full_config.get("output", {}).get("docs_dir")
        or str(state.get("output_dir", "./output"))
    )
    output_dir = Path(output_dir_cfg).expanduser()
    log_dir = Path(
        full_config.get("output", {}).get("rlm_log_dir")
        or (output_dir / "rlm_logs")
    )

    # --- RLM + PageIndex config ---
    rlm_cfg = full_config.get("rlm", {}) or {}
    pi_cfg = full_config.get("pageindex", {}) or {}
    pi_enabled = pi_cfg.get("enabled", True)

    rlm_sections_cfg = rlm_cfg.get("sections") or DEFAULT_RLM_SECTIONS
    skip_sections = set(rlm_cfg.get("skip_sections") or DEFAULT_SKIP_SECTIONS)
    deterministic_ids = set(
        rlm_cfg.get("deterministic_sections") or DEFAULT_DETERMINISTIC_SECTIONS
    )

    primary_rlm = _build_rlm_llm_config(llm_config)
    fallback_rlm = _build_fallback_rlm_config(llm_config, primary_rlm)

    print(f"\n{'='*60}")
    print("PHASE 2: RLM REPL + PageIndex")
    print(f"{'='*60}")
    print(f"  Primary root_model : {primary_rlm['root_model']}")
    print(f"  Primary sub_model  : {primary_rlm['sub_model']}")
    if fallback_manager and fallback_manager.has_fallback():
        print(f"  Fallback root_model: {fallback_rlm['root_model']}")
        print(f"  Fallback sub_model : {fallback_rlm['sub_model']}")
    print(f"  Max iterations     : {primary_rlm['max_iterations']}")

    # --- Step 1: PageIndex ---
    page_index: Dict[str, Any] = {"structure": []}
    if pi_enabled:
        pi_path = _resolve_pageindex_path(output_dir, program_name, full_config)
        page_index = _generate_pageindex(code_explanation, pi_cfg, pi_path)
    else:
        print("  → PageIndex disabled; RLM will fall back to Hash-ID splitting")

    # --- Step 2: cross-references for this file ---
    source_file = (
        state.get("relative_source_path")
        or state.get("source_file_path")
        or state.get("cobol_file_path")
        or ""
    )
    if source_file and "/" in source_file:
        relative_source = source_file
    else:
        relative_source = source_file  # best effort
    cross_refs = _load_cross_references(full_config, relative_source, program_name)
    if cross_refs:
        print(f"  → cross_references loaded: {cross_refs.get('file', '(unknown)')}")

    # --- Step 3: build metadata bundle for the REPL ---
    metadata = _build_metadata_bundle(state, page_index, cross_refs)

    # --- Step 4: token calibration ---
    print("  → Calibrating token ratio...")
    chars_per_token = calibrate_token_ratio(
        code_explanation[:10_000], primary_rlm["sub_model"]
    )
    sub_llm_max_chars = int(100_000 * chars_per_token)
    print(
        f"    chars/token ≈ {chars_per_token:.2f}, "
        f"sub-LLM capacity ≈ {sub_llm_max_chars:,} chars (~100K tokens)"
    )

    # --- Step 5: process sections ---
    section_outputs: Dict[str, str] = {}

    # Mermaid validation stats — ported from legacy run_phase2_sections
    # (commit 62694c3b). Each generated section is post-processed through the
    # mermaid MCP validator when it contains a ```mermaid block; invalid
    # diagrams are handed to an LLM to repair with the full section as context.
    mermaid_cfg = full_config.get("mermaid_validator") or {}
    mermaid_enabled = mermaid_cfg.get("enabled", True)
    mermaid_stats: Dict[str, Any] = {
        "total": 0,
        "valid": 0,
        "fixed": 0,
        "failed": 0,
        "sections_with_mermaid": [],
    }

    # Node-coverage verifier — for each RLM section, record every sub-LLM
    # call's `node_id` argument to a JSONL file. After the RLM loop returns,
    # diff the expected set (walked from the PageIndex tree) against the
    # actually-called set. Missing nodes trigger a deterministic gap-fill.
    coverage_cfg = rlm_cfg.get("coverage") or {}
    coverage_enabled = coverage_cfg.get("enabled", True)
    coverage_gap_fill = coverage_cfg.get("gap_fill_enabled", True)
    coverage_strict = coverage_cfg.get("strict", False)
    coverage_log_dir = Path(
        coverage_cfg.get("log_dir") or (log_dir / "coverage")
    )
    if coverage_enabled:
        coverage_log_dir.mkdir(parents=True, exist_ok=True)
    expected_node_ids: List[str] = (
        pageindex.walk_node_ids(page_index) if coverage_enabled else []
    )
    coverage_stats: Dict[str, Any] = {
        "expected": len(expected_node_ids),
        "sections_checked": 0,
        "sections_complete": 0,
        "sections_with_gaps": 0,
        "total_gaps_filled": 0,
    }

    print(f"\nTemplate has {len(sections)} sections:")
    for sec in sections:
        sec_id = sec.get("id", "")
        status = "SKIP" if sec_id in skip_sections else (
            "DETERMINISTIC" if sec_id in deterministic_ids else "RLM"
        )
        if sec_id not in rlm_sections_cfg and sec_id not in deterministic_ids and sec_id not in skip_sections:
            status = "SKIP (not listed)"
        print(f"  [{status}] {sec.get('title', sec_id)} ({sec_id})")

    total_start = time.time()
    for section in sections:
        sec_id = section.get("id", "")
        sec_title = section.get("title", sec_id)

        if sec_id in skip_sections:
            continue
        # Sections neither listed for RLM nor marked deterministic are skipped
        # (Phase 3 handles detailed-code-explanation and document-header).
        if sec_id not in rlm_sections_cfg and sec_id not in deterministic_ids:
            print(f"  [SKIP] {sec_title} ({sec_id}) — not in configured sections")
            continue

        content: Optional[str] = None

        # 5a. Try deterministic generator
        if sec_id in deterministic_ids:
            t0 = time.time()
            content = deterministic.generate(
                sec_id,
                cross_references=cross_refs,
                page_index=page_index,
                program_name=program_name,
                source_file=relative_source,
            )
            elapsed_ms = (time.time() - t0) * 1000
            if content:
                print(
                    f"  [DETERMINISTIC] {sec_title} ({sec_id}) — "
                    f"{elapsed_ms:.0f}ms, {len(content):,} chars, 0 LLM calls"
                )
            else:
                print(
                    f"  [DETERMINISTIC→RLM] {sec_title} ({sec_id}) — "
                    "generator returned None, falling back to RLM"
                )

        # 5b. RLM fallback
        section_coverage_log: Optional[Path] = None
        ran_rlm = False
        if content is None:
            if sec_id not in rlm_sections_cfg:
                # Deterministic-only section where generator failed; skip rather
                # than force RLM on something not intended for LLM synthesis.
                print(f"  [SKIP] {sec_title} ({sec_id}) — deterministic failed and not RLM-eligible")
                continue
            instruction = _format_section_instruction(section)
            if coverage_enabled and expected_node_ids:
                ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                section_coverage_log = coverage_log_dir / f"{sec_id}_coverage_{ts}.jsonl"
            content = asyncio.run(
                _process_section_async(
                    section_id=sec_id,
                    section_title=sec_title,
                    instruction=instruction,
                    code_explanation=code_explanation,
                    metadata=metadata,
                    program_name=program_name,
                    log_dir=log_dir,
                    primary_rlm=primary_rlm,
                    fallback_rlm=fallback_rlm,
                    fallback_manager=fallback_manager,
                    sub_llm_max_chars=sub_llm_max_chars,
                    chars_per_token=chars_per_token,
                    coverage_log_path=section_coverage_log,
                )
            )
            ran_rlm = True

        # ─────────────────────────────────────────────────────────────────
        # Node-coverage check (RLM sections only — deterministic generators
        # are already deterministic). The diff and gap-fill are pure Python —
        # the root LLM is never consulted about what it did or didn't process.
        # ─────────────────────────────────────────────────────────────────
        if (
            ran_rlm
            and coverage_enabled
            and expected_node_ids
            and section_coverage_log is not None
        ):
            expected_set = set(expected_node_ids)
            processed_set = _read_processed_node_ids(section_coverage_log)
            missing = sorted(expected_set - processed_set)
            coverage_stats["sections_checked"] += 1
            if not missing:
                coverage_stats["sections_complete"] += 1
                print(
                    f"  [COVERAGE] {sec_id}: {len(processed_set)}/{len(expected_set)} "
                    "nodes processed — OK"
                )
            else:
                coverage_stats["sections_with_gaps"] += 1
                print(
                    f"  [COVERAGE] {sec_id}: {len(processed_set)}/{len(expected_set)} "
                    f"nodes processed — MISSING {len(missing)} "
                    f"({', '.join(missing[:10])}{'…' if len(missing) > 10 else ''})"
                )
                if coverage_strict:
                    raise RuntimeError(
                        f"Coverage check failed for section {sec_id!r}: "
                        f"{len(missing)} PageIndex node(s) were not processed "
                        f"({', '.join(missing[:5])}"
                        f"{'…' if len(missing) > 5 else ''}). "
                        "Set rlm.coverage.strict=false or rlm.coverage.gap_fill_enabled=true to recover."
                    )
                if coverage_gap_fill:
                    print(
                        f"    → Running gap-fill on {len(missing)} missing "
                        "node(s)..."
                    )
                    _, get_sub_model = _make_model_getters(
                        primary_rlm, fallback_rlm, fallback_manager
                    )
                    active_config = (
                        fallback_rlm
                        if fallback_manager and fallback_manager.is_fallback_active()
                        else primary_rlm
                    )
                    pairs = asyncio.run(
                        _gap_fill_missing_nodes(
                            missing_ids=missing,
                            page_index=page_index,
                            section_title=sec_title,
                            section_instruction=instruction,
                            program_name=program_name,
                            llm_config=active_config,
                            fallback_manager=fallback_manager,
                            get_sub_model=get_sub_model,
                            coverage_log_path=section_coverage_log,
                            section_id=sec_id,
                        )
                    )
                    annex = _format_gap_fill_annex(pairs, sec_title)
                    if annex:
                        content = (content or "") + annex
                    coverage_stats["total_gaps_filled"] += len(pairs)
                    print(
                        f"    → Gap-fill complete: {len(pairs)} node(s) processed, "
                        f"annex appended ({len(annex):,} chars)"
                    )

        # ─────────────────────────────────────────────────────────────────
        # Mermaid validation — validate/fix diagrams produced by either the
        # deterministic generator or the RLM loop. Mirrors the legacy
        # per-section hook from run_phase2_sections (commit 62694c3b).
        # All knobs (docker image, docker args, MCP tool name, retry budget)
        # come from the top-level `mermaid_validator` config block.
        # ─────────────────────────────────────────────────────────────────
        if mermaid_enabled and content and "```mermaid" in content:
            try:
                from mermaid_validator import validate_section_mermaid_sync
                content, section_mermaid_stats = validate_section_mermaid_sync(
                    section_id=sec_id,
                    section_content=content,
                    llm_config=llm_config,
                    docker_image=mermaid_cfg.get(
                        "docker_image", "mermaid-mcp:test"
                    ),
                    docker_args=mermaid_cfg.get("docker_args"),
                    tool_name=mermaid_cfg.get("tool_name", "validate"),
                    max_retries=mermaid_cfg.get("max_retries", 3),
                    fallback_manager=fallback_manager,
                )
                mermaid_stats["total"] += section_mermaid_stats["total"]
                mermaid_stats["valid"] += section_mermaid_stats["valid"]
                mermaid_stats["fixed"] += section_mermaid_stats["fixed"]
                mermaid_stats["failed"] += section_mermaid_stats["failed"]
                if section_mermaid_stats["total"] > 0:
                    mermaid_stats["sections_with_mermaid"].append(sec_id)
            except Exception as e:
                # Validator failure (e.g. Docker image missing, MCP server
                # unreachable) must not abort doc generation — log and keep
                # the original content.
                print(
                    f"  ⚠ Mermaid validation skipped for {sec_id!r}: "
                    f"{type(e).__name__}: {e}"
                )

        section_outputs[sec_id] = content

    total_elapsed = time.time() - total_start
    print(f"\n→ Phase 2 Summary:")
    print(f"    Sections produced: {len(section_outputs)}")
    print(f"    Total elapsed    : {total_elapsed:.1f}s")
    print(f"    RLM logs         : {log_dir}")

    if mermaid_stats["total"] > 0:
        print(f"\n→ Mermaid Validation Summary:")
        print(f"    Total diagrams: {mermaid_stats['total']}")
        print(f"    Already valid:  {mermaid_stats['valid']}")
        print(f"    Fixed by LLM:   {mermaid_stats['fixed']}")
        print(f"    Failed:         {mermaid_stats['failed']}")
        if mermaid_stats["sections_with_mermaid"]:
            print(
                f"    Sections with mermaid: "
                f"{', '.join(mermaid_stats['sections_with_mermaid'])}"
            )

    if coverage_enabled and coverage_stats["sections_checked"] > 0:
        print(f"\n→ Node-Coverage Summary:")
        print(f"    Expected PageIndex nodes: {coverage_stats['expected']}")
        print(f"    Sections checked        : {coverage_stats['sections_checked']}")
        print(f"    Fully covered           : {coverage_stats['sections_complete']}")
        print(f"    Gaps detected           : {coverage_stats['sections_with_gaps']}")
        print(f"    Gap-filled (deterministic): {coverage_stats['total_gaps_filled']}")
        print(f"    Coverage logs           : {coverage_log_dir}")

    return section_outputs
