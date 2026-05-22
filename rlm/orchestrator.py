"""
Phase 2 orchestrator — PageIndex + deterministic generators + λ-RLM planner.

Entry point:
    run_phase2_rlm(state, code_explanation, llm_config, fallback_manager, full_config)
        → Dict[section_id, section_markdown]

Flow per source file:
    1. Build PageIndex tree from the Phase 1 code-explanation markdown
       (extract or llm mode, per config).
    2. Load any cross_references JSON for this source file, plus all other
       metadata already on `state`.
    3. Iterate template sections in order; for each:
         - skip if listed under `rlm.skip_sections`
         - skip if not listed under `rlm.sections` (outer allowlist)
         - deterministic generator if eligible (falls through to planner on None)
         - λ-RLM planner otherwise (universal catch-all)
       Mermaid validation runs on whatever content the chosen engine produced.
    4. Return the section_outputs dict consumed by the existing Phase 3
       assembly.

Fallback behavior (mirrors LLMFallbackManager):
    - Primary sub-LLM model comes from `llm_config.planner.sub_model`.
    - On any sub-LLM unrecoverable error, `fallback_manager.trigger_fallback()`
      flips session-wide state; subsequent calls resolve the model from
      `llm_config.fallback.planner.sub_model` instead.
"""

from __future__ import annotations

import asyncio
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from rlm import deterministic, pageindex
from rlm.planner import run_planner
from rlm.sub_llm import call_claude


# Default section lists (kept loosely aligned with the previous defaults).
DEFAULT_SECTIONS = [
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


def _build_planner_llm_config(llm_config: Dict[str, Any]) -> Dict[str, Any]:
    """Extract the subset of llm_config the planner needs.

    Reads `llm_config.planner.*` first; falls back to top-level llm_config
    keys for backward compatibility with single-block configs.
    """
    planner_primary = llm_config.get("planner", {}) or {}
    return {
        "sub_model": (
            planner_primary.get("sub_model")
            or llm_config.get("sub_model")
            or llm_config.get("model", "claude-sonnet-4-5")
        ),
        "max_output_tokens": planner_primary.get(
            "max_output_tokens", llm_config.get("max_output_tokens", 16384)
        ),
        "max_thinking_tokens": planner_primary.get(
            "max_thinking_tokens", llm_config.get("max_thinking_tokens", 0)
        ),
        "leaf_concurrency": planner_primary.get("leaf_concurrency", 4),
    }


def _build_fallback_planner_config(
    llm_config: Dict[str, Any], primary: Dict[str, Any]
) -> Dict[str, Any]:
    """Extract the fallback planner config, inheriting from primary when unset."""
    fb = (llm_config.get("fallback") or {}).get("planner") or {}
    return {
        "sub_model": fb.get("sub_model", primary["sub_model"]),
        "max_output_tokens": fb.get("max_output_tokens", primary["max_output_tokens"]),
        "max_thinking_tokens": fb.get(
            "max_thinking_tokens", primary["max_thinking_tokens"]
        ),
        "leaf_concurrency": fb.get("leaf_concurrency", primary["leaf_concurrency"]),
    }


def _build_metadata_bundle(
    state: Dict[str, Any],
    page_index: Dict[str, Any],
    cross_references: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    """Assemble the metadata dict passed into the planner."""
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
# Fallback-aware model accessor
# ---------------------------------------------------------------------------


def _make_sub_model_getter(
    primary: Dict[str, Any],
    fallback: Dict[str, Any],
    fallback_manager: Optional[Any],
) -> Callable[[], str]:
    """Return a `get_sub_model()` callable that observes fallback state."""
    def _active() -> bool:
        return bool(
            fallback_manager
            and getattr(fallback_manager, "is_fallback_active", lambda: False)()
        )

    def get_sub_model() -> str:
        return fallback["sub_model"] if _active() else primary["sub_model"]

    return get_sub_model


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
# Planner driver per section
# ---------------------------------------------------------------------------


def _make_planner_llm(
    get_sub_model: Callable[[], str],
    primary: Dict[str, Any],
    fallback: Dict[str, Any],
    fallback_manager: Optional[Any],
):
    """Build the `llm_fn` closure the planner uses for leaf + synth calls.

    The closure consults `get_sub_model()` before every call so fallback
    state takes effect mid-flight.
    """
    async def _llm(prompt: str) -> str:
        active = (
            fallback
            if fallback_manager and fallback_manager.is_fallback_active()
            else primary
        )
        text, _info = await call_claude(
            prompt=prompt,
            model=get_sub_model(),
            max_thinking_tokens=active.get("max_thinking_tokens") or None,
            max_output_tokens=active.get("max_output_tokens"),
            fallback_manager=fallback_manager,
            get_model=get_sub_model,
        )
        return text

    return _llm


def _run_planner_for_section(
    section: Dict[str, Any],
    metadata: Dict[str, Any],
    program_name: str,
    primary: Dict[str, Any],
    fallback: Dict[str, Any],
    fallback_manager: Optional[Any],
    pairwise_sections: Dict[str, Dict[str, str]],
    coverage_log_path: Optional[Path],
) -> tuple[str, Any]:
    """Run the planner once for a section, with one automatic fallback retry."""
    sec_id = section.get("id", "")
    sec_title = section.get("title", sec_id)
    instruction = section.get("instruction", "")
    section_template = section.get("template", "")
    pairwise_cfg = pairwise_sections.get(sec_id)

    get_sub_model = _make_sub_model_getter(primary, fallback, fallback_manager)

    async def _run_once() -> tuple[str, Any]:
        active = (
            fallback
            if fallback_manager and fallback_manager.is_fallback_active()
            else primary
        )
        llm_fn = _make_planner_llm(get_sub_model, primary, fallback, fallback_manager)
        return await run_planner(
            section_id=sec_id,
            section_title=sec_title,
            instruction=instruction,
            template=section_template,
            metadata=metadata,
            llm_fn=llm_fn,
            program_name=program_name,
            pairwise_cfg=pairwise_cfg,
            leaf_concurrency=active.get("leaf_concurrency", 4),
            coverage_log_path=coverage_log_path,
            model_name=get_sub_model(),
        )

    try:
        return asyncio.run(_run_once())
    except Exception as e:
        if (
            fallback_manager
            and getattr(fallback_manager, "has_fallback", lambda: False)()
            and fallback_manager.is_fallback_active()
        ):
            print(f"  → Retrying section {sec_id!r} on fallback models after: {e}")
            try:
                return asyncio.run(_run_once())
            except Exception as e2:
                return (
                    f"## {sec_title}\n\n**Generation Failed (after fallback)**\n\n"
                    f"```\n{e2}\n```\n",
                    None,
                )
        return (
            f"## {sec_title}\n\n**Generation Failed**\n\n```\n{e}\n```\n",
            None,
        )


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
    Phase 2: PageIndex + deterministic generators + λ-RLM planner.

    Args:
        state: AgentState-shaped dict. Reads template, program_name, output_dir,
            cobol_file_path / source_file_path, and any metadata fields.
        code_explanation: Phase 1 markdown output.
        llm_config: Full LLM config (primary + optional fallback.planner sub-block).
        fallback_manager: Shared LLMFallbackManager; trigger state propagates
            across planner LLM calls and sections.
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
    coverage_log_dir = log_dir / "coverage"

    # --- Routing config (Flavor B: outer allowlist + deterministic-first + planner catch-all) ---
    rlm_cfg = full_config.get("rlm", {}) or {}
    pi_cfg = full_config.get("pageindex", {}) or {}
    pi_enabled = pi_cfg.get("enabled", True)

    sections_allowlist = set(rlm_cfg.get("sections") or DEFAULT_SECTIONS)
    skip_sections = set(rlm_cfg.get("skip_sections") or DEFAULT_SKIP_SECTIONS)
    deterministic_ids = set(
        rlm_cfg.get("deterministic_sections") or DEFAULT_DETERMINISTIC_SECTIONS
    )
    pairwise_sections = rlm_cfg.get("pairwise_sections") or {}

    primary = _build_planner_llm_config(llm_config)
    fallback = _build_fallback_planner_config(llm_config, primary)

    print(f"\n{'='*60}")
    print("PHASE 2: PageIndex + Deterministic + λ-RLM Planner")
    print(f"{'='*60}")
    print(f"  Primary sub_model : {primary['sub_model']}")
    if fallback_manager and fallback_manager.has_fallback():
        print(f"  Fallback sub_model: {fallback['sub_model']}")
    print(f"  Leaf concurrency  : {primary['leaf_concurrency']}")

    # --- Step 1: PageIndex ---
    page_index: Dict[str, Any] = {"structure": []}
    if pi_enabled:
        pi_path = _resolve_pageindex_path(output_dir, program_name, full_config)
        page_index = _generate_pageindex(code_explanation, pi_cfg, pi_path)
    else:
        print("  → PageIndex disabled; planner will see an empty tree")

    # --- Step 2: cross-references for this file ---
    source_file = (
        state.get("relative_source_path")
        or state.get("source_file_path")
        or state.get("cobol_file_path")
        or ""
    )
    relative_source = source_file  # best effort; preserved for downstream lookups
    cross_refs = _load_cross_references(full_config, relative_source, program_name)
    if cross_refs:
        print(f"  → cross_references loaded: {cross_refs.get('file', '(unknown)')}")

    # --- Step 3: metadata bundle ---
    metadata = _build_metadata_bundle(state, page_index, cross_refs)

    # --- Step 4: process sections ---
    section_outputs: Dict[str, str] = {}

    mermaid_cfg = full_config.get("mermaid_validator") or {}
    mermaid_enabled = mermaid_cfg.get("enabled", True)
    mermaid_stats: Dict[str, Any] = {
        "total": 0,
        "valid": 0,
        "fixed": 0,
        "failed": 0,
        "sections_with_mermaid": [],
    }

    planner_totals = {
        "sections_planned": 0,
        "leaf_calls": 0,
        "synthesis_calls": 0,
        "items_total": 0,
        "items_after_filter": 0,
        "elapsed_s": 0.0,
        "used_cross_sections": [],
    }

    print(f"\nTemplate has {len(sections)} sections:")
    for sec in sections:
        sec_id = sec.get("id", "")
        if sec_id in skip_sections:
            status = "SKIP"
        elif sec_id not in sections_allowlist and sec_id not in deterministic_ids:
            status = "SKIP (not in allowlist)"
        elif sec_id in deterministic_ids:
            status = "DETERMINISTIC→PLANNER"
        else:
            status = "PLANNER"
        print(f"  [{status}] {sec.get('title', sec_id)} ({sec_id})")

    total_start = time.time()
    for section in sections:
        sec_id = section.get("id", "")
        sec_title = section.get("title", sec_id)

        if sec_id in skip_sections:
            continue
        # Outer allowlist: must be in `sections` OR `deterministic_sections`.
        if sec_id not in sections_allowlist and sec_id not in deterministic_ids:
            continue

        content: Optional[str] = None

        # 4a. Try deterministic generator first
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
                    f"  [DETERMINISTIC→PLANNER] {sec_title} ({sec_id}) — "
                    "generator returned None, falling back to planner"
                )

        # 4b. Planner as universal catch-all
        if content is None:
            if sec_id not in sections_allowlist:
                # Section was deterministic-only and the generator failed.
                print(
                    f"  [SKIP] {sec_title} ({sec_id}) — "
                    "deterministic failed and section not in `sections` allowlist"
                )
                continue
            ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            section_coverage_log = coverage_log_dir / f"{sec_id}_coverage_{ts}.jsonl"
            content, stats = _run_planner_for_section(
                section=section,
                metadata=metadata,
                program_name=program_name,
                primary=primary,
                fallback=fallback,
                fallback_manager=fallback_manager,
                pairwise_sections=pairwise_sections,
                coverage_log_path=section_coverage_log,
            )
            if stats is not None:
                cross_marker = " [CROSS]" if stats.used_cross else ""
                print(
                    f"  [PLANNER]{cross_marker} {sec_title} ({sec_id}) — "
                    f"{stats.elapsed_s:.1f}s, {len(content):,} chars, "
                    f"{stats.leaf_calls} leaf + {stats.synthesis_calls} synth, "
                    f"{stats.items_after_filter}/{stats.items_total} items"
                )
                planner_totals["sections_planned"] += 1
                planner_totals["leaf_calls"] += stats.leaf_calls
                planner_totals["synthesis_calls"] += stats.synthesis_calls
                planner_totals["items_total"] += stats.items_total
                planner_totals["items_after_filter"] += stats.items_after_filter
                planner_totals["elapsed_s"] += stats.elapsed_s
                if stats.used_cross:
                    planner_totals["used_cross_sections"].append(sec_id)
            else:
                print(f"  [PLANNER-FAILED] {sec_title} ({sec_id})")

        # 4c. Mermaid validation (engine-agnostic)
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
    print(f"    Coverage logs    : {coverage_log_dir}")

    if planner_totals["sections_planned"] > 0:
        print(f"\n→ Planner Coverage:")
        print(f"    Sections via planner   : {planner_totals['sections_planned']}")
        print(f"    Leaf LLM calls         : {planner_totals['leaf_calls']}")
        print(f"    Synthesis LLM calls    : {planner_totals['synthesis_calls']}")
        print(
            f"    Items filtered/total   : "
            f"{planner_totals['items_after_filter']}/{planner_totals['items_total']}"
        )
        print(f"    Planner elapsed (sum)  : {planner_totals['elapsed_s']:.1f}s")
        if planner_totals["used_cross_sections"]:
            print(
                f"    CROSS sections         : "
                f"{', '.join(planner_totals['used_cross_sections'])}"
            )

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

    return section_outputs
