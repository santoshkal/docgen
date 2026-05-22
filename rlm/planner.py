"""λ-RLM-style planner: a single combinator chain runs every section.

The chain is fixed:

    Φ = M_synth ∘ REDUCE_CONCAT ∘ MAP(M, leaf_prompt) ∘ FILTER(p, items)

`items` are PageIndex blocks by default. For sections registered in
`pairwise_sections` (config), `items` becomes the CROSS product of two
metadata-derived lists. Otherwise `CROSS` is skipped — no overkill.

Section-specific knowledge lives entirely in YAML config and the existing
template.yaml (instruction + template per section). The planner module
contains zero hardcoded section IDs.

The LLM is invoked only at MAP leaves and at the synthesis step. It never
authors control-flow code, never sees a multi-page system prompt, and never
runs in a REPL loop.

Coverage logging:
    When `coverage_log_path` is provided, the planner appends one JSONL record
    per leaf and synth call to that file. The record format matches the
    legacy REPL-engine coverage log so downstream tools see the same shape:

        {timestamp, section_id, node_id, call_type, prompt_length,
         response_length, is_error, model}

    Leaf records carry the originating block's `node_id`; synth records have
    `node_id: null` because synthesis spans the whole filtered set.
"""

from __future__ import annotations

import asyncio
import json
import re
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Awaitable, Callable, Optional

from rlm.combinators import CROSS, FILTER, MAP, REDUCE_CONCAT

LLMFn = Callable[[str], Awaitable[str]]


# =============================================================================
# Stats
# =============================================================================


@dataclass
class PlannerStats:
    section_id: str = ""
    leaf_calls: int = 0
    synthesis_calls: int = 0
    elapsed_s: float = 0.0
    items_total: int = 0
    items_after_filter: int = 0
    used_cross: bool = False


# =============================================================================
# Helpers — pure, deterministic, no per-section knowledge
# =============================================================================


def _flatten_blocks(page_index: dict) -> list[dict]:
    """Flatten a PageIndex tree (chunk → block hierarchy) to a flat block list.

    Block `node_id` values are preserved on each item so leaf calls can be
    keyed back to the original PageIndex node in coverage logs.
    """
    out: list[dict] = []
    for chunk in (page_index or {}).get("structure", []) or []:
        for b in chunk.get("nodes", []) or []:
            out.append(b)
    return out


def _resolve_path(metadata: dict, path: str) -> Any:
    """Walk a dotted path through nested dicts. e.g.
    `_resolve_path(md, 'cross_references.cross_file_outgoing')`."""
    cur: Any = metadata
    for part in path.split("."):
        if not isinstance(cur, dict):
            return []
        cur = cur.get(part)
        if cur is None:
            return []
    return cur


# Cheap stopword list for keyword extraction. Generic, not section-specific.
_STOPWORDS = {
    "document", "documents", "documenting", "include", "describe", "details",
    "section", "sections", "the", "a", "an", "and", "or", "of", "for",
    "with", "to", "in", "on", "at", "this", "that", "these", "those",
    "any", "all", "from", "into", "is", "are", "be", "been", "have", "has",
    "by", "as", "such",
}


def _keywords_from_instruction(instruction: str) -> list[str]:
    """Extract relevance keywords from a section instruction.

    Splits on punctuation and whitespace, lowercases, removes stopwords and
    short tokens. Returns a small list. If the instruction is too generic
    (no usable keywords), returns []. The planner treats [] as 'pass all
    items through' — FILTER becomes identity for those sections.
    """
    tokens = re.findall(r"[A-Za-z][A-Za-z\-]{3,}", instruction.lower())
    seen: set[str] = set()
    out: list[str] = []
    for t in tokens:
        if t in _STOPWORDS or len(t) < 4 or t in seen:
            continue
        seen.add(t)
        out.append(t)
    return out


def _relevance_predicate(item: Any, keywords: list[str]) -> bool:
    """Generic predicate: item is relevant if any keyword appears in its text.
    Empty keyword list = always True (FILTER becomes identity).
    """
    if not keywords:
        return True
    haystack = json.dumps(item, default=str).lower()
    return any(kw in haystack for kw in keywords)


def _build_leaf_prompt(item: Any, section_title: str, instruction: str) -> str:
    """Generic leaf prompt — same shape for every section. The section's
    uniqueness flows in via `section_title` and `instruction`."""
    if isinstance(item, dict) and "title" in item and "text" in item:
        # PageIndex block
        return (
            f"You are extracting content for the '{section_title}' section.\n"
            f"Section instruction:\n{instruction}\n\n"
            f"Read THIS BLOCK and extract any content relevant to the section.\n"
            f"If the block contains nothing relevant, return exactly: {{}}\n\n"
            f"Block: {(item.get('title') or '')[:200]}\n"
            f"Summary: {(item.get('summary') or '')[:600]}\n"
            f"Text: {(item.get('text') or '')[:3000]}\n\n"
            f"Return a JSON object capturing the extracted content. "
            f"Use field names that match the section's needs. "
            f"Return ONLY the JSON object, no preamble or fences."
        )
    if isinstance(item, tuple) and len(item) == 2:
        # CROSS pair
        a, b = item
        return (
            f"You are extracting content for the '{section_title}' section.\n"
            f"Section instruction:\n{instruction}\n\n"
            f"Describe the relationship between these two items as it relates "
            f"to the section. If there is no meaningful relationship, return {{}}.\n\n"
            f"Item A: {json.dumps(a, default=str)[:1500]}\n"
            f"Item B: {json.dumps(b, default=str)[:1500]}\n\n"
            f"Return a JSON object. Return ONLY the JSON object."
        )
    return (
        f"You are extracting content for the '{section_title}' section.\n"
        f"Section instruction:\n{instruction}\n\n"
        f"Extract section-relevant content from this item:\n"
        f"{json.dumps(item, default=str)[:3000]}\n\n"
        f"Return a JSON object. Return ONLY the JSON object."
    )


def _build_synth_prompt(
    findings: str, section_title: str, instruction: str, template: str, program_name: str
) -> str:
    """Generic synthesis prompt — same shape for every section."""
    return (
        f"You are composing the '{section_title}' section of code documentation "
        f"for the program {program_name}.\n\n"
        f"Section instruction:\n{instruction}\n\n"
        f"Section output template (fill the placeholders, preserve markdown structure):\n"
        f"{template}\n\n"
        f"Findings extracted from individual blocks/items:\n"
        f"{findings}\n\n"
        f"Compose the section markdown. Use ONLY the findings — do not invent "
        f"content. If a placeholder has no supporting findings, write an explicit "
        f"statement like 'None present in this file' for that placeholder. "
        f"Return ONLY the markdown for the section, starting with the '#' heading. "
        f"No preamble, no fences."
    )


def _strip_code_fences(s: str) -> str:
    return re.sub(r"^```[a-zA-Z]*\s*\n?|\n?```\s*$", "", s.strip(), flags=re.MULTILINE)


def _safe_parse_json(s: str) -> Any:
    cleaned = _strip_code_fences(s)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {"raw": cleaned[:800]}


def _coverage_record(
    section_id: str,
    node_id: Optional[str],
    call_type: str,
    prompt_length: int,
    response_length: int,
    is_error: bool,
    model: Optional[str],
) -> dict:
    """Render a single coverage-log entry. Schema matches the legacy REPL
    coverage log so downstream tooling sees the same shape."""
    return {
        "timestamp": datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
        "section_id": section_id,
        "node_id": str(node_id) if node_id is not None else None,
        "call_type": call_type,
        "prompt_length": prompt_length,
        "response_length": response_length,
        "is_error": is_error,
        "model": model,
    }


def _append_jsonl(path: Path, entry: dict) -> None:
    """Append one JSONL record. Best-effort — IO errors are swallowed so a
    full disk does not abort doc generation."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "a", encoding="utf-8") as f:
            json.dump(entry, f, default=str)
            f.write("\n")
    except OSError:
        pass


async def _gather_with_concurrency(coros, limit: int):
    sem = asyncio.Semaphore(limit)

    async def _run(c):
        async with sem:
            return await c

    return await asyncio.gather(*[_run(c) for c in coros])


# =============================================================================
# The single chain
# =============================================================================


async def run_planner(
    section_id: str,
    section_title: str,
    instruction: str,
    template: str,
    metadata: dict,
    llm_fn: LLMFn,
    program_name: str = "",
    pairwise_cfg: Optional[dict] = None,
    leaf_concurrency: int = 4,
    coverage_log_path: Optional[Path] = None,
    model_name: Optional[str] = None,
) -> tuple[str, PlannerStats]:
    """Run Φ for one section. Same chain shape regardless of section.

    Args:
        section_id, section_title, instruction, template: from template.yaml.
        metadata: the pipeline's metadata dict (page_index, cross_references, ...).
        llm_fn: async leaf-LLM call. Takes a prompt, returns text.
        program_name: program identifier, used in the synth prompt.
        pairwise_cfg: optional dict like {"a": "<dotted.path>", "b": "<dotted.path>"}.
            If present, items become the CROSS of the two referenced lists.
            If absent, items are page_index blocks.
        leaf_concurrency: max concurrent leaf-LLM calls.
        coverage_log_path: optional JSONL path. When provided, one record is
            appended per leaf + synth call. Schema matches the legacy
            REPL-engine coverage log.
        model_name: optional model name to stamp on coverage records. The
            planner does not select the model — that's `llm_fn`'s job — but
            the name is useful in the audit log.

    Returns:
        (section_markdown, PlannerStats).
    """
    stats = PlannerStats(section_id=section_id)
    t0 = time.time()
    try:
        # ---- items: blocks by default; CROSS-pairs if pairwise config given ----
        if pairwise_cfg:
            a_list = list(_resolve_path(metadata, pairwise_cfg["a"]) or [])
            b_list = list(_resolve_path(metadata, pairwise_cfg["b"]) or [])
            items: list[Any] = list(CROSS(a_list, b_list))
            stats.used_cross = True
        else:
            items = list(_flatten_blocks(metadata.get("page_index") or {}))

        stats.items_total = len(items)

        if not items:
            # Nothing to operate on — return a minimal stub the user can recognise.
            stats.elapsed_s = time.time() - t0
            return (
                f"# {section_title}\n\n"
                f"_No items available to populate this section "
                f"(items_total=0)._\n",
                stats,
            )

        # ---- FILTER: derive predicate from the section instruction itself ----
        keywords = _keywords_from_instruction(instruction)
        filtered = list(FILTER(lambda x: _relevance_predicate(x, keywords), items))
        if not filtered:
            # Predicate excluded everything; fall back to all items so we don't
            # produce an empty section.
            filtered = items
        stats.items_after_filter = len(filtered)

        # ---- MAP: per-item leaf prompts, parallel ----
        leaf_prompts = MAP(
            lambda x: _build_leaf_prompt(x, section_title, instruction),
            filtered,
        )

        # Pull a node_id off each filtered item when present (PageIndex blocks).
        # For CROSS pairs and other shapes there is no canonical node_id —
        # we record `None`. Used only for coverage logging.
        leaf_node_ids: list[Optional[str]] = []
        for it in filtered:
            if isinstance(it, dict) and it.get("node_id") is not None:
                leaf_node_ids.append(str(it["node_id"]))
            else:
                leaf_node_ids.append(None)

        async def _instrumented_leaf(prompt: str, node_id: Optional[str]) -> str:
            try:
                text = await llm_fn(prompt)
                is_error = False
            except Exception as e:
                text = f"Error: leaf-LLM call failed - {e}"
                is_error = True
            if coverage_log_path is not None:
                _append_jsonl(
                    coverage_log_path,
                    _coverage_record(
                        section_id=section_id,
                        node_id=node_id,
                        call_type="planner_leaf",
                        prompt_length=len(prompt),
                        response_length=len(text),
                        is_error=is_error,
                        model=model_name,
                    ),
                )
            return text

        findings_raw = await _gather_with_concurrency(
            [_instrumented_leaf(p, nid) for p, nid in zip(leaf_prompts, leaf_node_ids)],
            leaf_concurrency,
        )
        stats.leaf_calls += len(findings_raw)

        # Parse + drop empty findings
        parsed = []
        for f in findings_raw:
            obj = _safe_parse_json(f)
            if obj and obj != {} and obj != {"raw": ""}:
                parsed.append(obj)

        # ---- REDUCE_CONCAT: fold parsed findings into one text blob ----
        findings_text = REDUCE_CONCAT(
            [json.dumps(p, indent=2, default=str) for p in parsed],
            sep="\n---\n",
        ) or "(no findings extracted)"

        # ---- M_synth: single synthesis call ----
        synth_prompt = _build_synth_prompt(
            findings_text, section_title, instruction, template, program_name
        )
        try:
            final = await llm_fn(synth_prompt)
            synth_error = False
        except Exception as e:
            final = (
                f"## {section_title}\n\n"
                f"**Synthesis Failed**\n\n```\n{e}\n```\n"
            )
            synth_error = True
        stats.synthesis_calls += 1

        if coverage_log_path is not None:
            _append_jsonl(
                coverage_log_path,
                _coverage_record(
                    section_id=section_id,
                    node_id=None,
                    call_type="planner_synth",
                    prompt_length=len(synth_prompt),
                    response_length=len(final),
                    is_error=synth_error,
                    model=model_name,
                ),
            )

        return _strip_code_fences(final), stats
    finally:
        stats.elapsed_s = time.time() - t0
