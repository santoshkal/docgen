"""
Questionnaire aggregator — cut every "Questionnaire for <X>" sub-section from
each generated Phase 2 section and consolidate them into a single
"Questionnaires for <ProgramName>" section placed after "Error Handling Strategy".

Two consumption modes:

1. In-pipeline (default) — called between Phase 2 and Phase 3 in
   cobol_doc_agent.generate_documentation():

       from questionnaire_aggregator import (
           aggregate_in_section_outputs,
           inject_section_after,
       )
       section_outputs, synthetic = aggregate_in_section_outputs(
           section_outputs, program_name
       )
       if synthetic:
           template = inject_section_after(
               template, synthetic, after_id="error-handling"
           )
       final_doc = assemble_final_document(
           program_name=program_name,
           code_explanation=code_explanation,
           section_outputs=section_outputs,
           template=template,
           ...
       )

2. Standalone file-based — `scripts/aggregate_questionnaires.py` is a thin CLI
   wrapper that calls `process_text()` / `process_file()` on an already-assembled
   markdown document.

Re-runs are idempotent: any pre-existing aggregate section (older "Questionnaires"
heading or newer "Questionnaires for ...") is removed before a fresh one is built.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
# Match aggregate headings only (plural): "Questionnaires" OR "Questionnaires for X".
# The singular form "Questionnaire for <SectionName>" is the per-section heading
# that we CUT from each section — it must NOT match this pattern.
AGGREGATE_TITLE_RE = re.compile(r"^\s*questionnaires(?:\s+for\s+.+)?\s*$", re.IGNORECASE)


# ---------------------------------------------------------------------------
# Heading parsing (fence-aware)
# ---------------------------------------------------------------------------


def parse_headings(lines: List[str]) -> List[Tuple[int, int, str]]:
    """Return [(line_index, level, text), ...] for every ATX heading that is
    not inside a fenced code block."""
    out: List[Tuple[int, int, str]] = []
    in_fence = False
    fence_marker = ""
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif stripped.startswith(fence_marker):
                in_fence = False
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if m:
            out.append((i, len(m.group(1)), m.group(2).strip()))
    return out


def _section_end(
    headings: List[Tuple[int, int, str]], heading_idx: int, total_lines: int
) -> int:
    """Return the first line index past this section (next same-or-higher-level
    heading, or EOF)."""
    level = headings[heading_idx][1]
    for j in range(heading_idx + 1, len(headings)):
        if headings[j][1] <= level:
            return headings[j][0]
    return total_lines


def _remove_ranges(lines: List[str], ranges: List[Tuple[int, int]]) -> List[str]:
    """Remove half-open [start, end) ranges from `lines`; collapse runs of
    3+ blank lines to 1."""
    ranges = sorted(ranges, reverse=True)
    out = list(lines)
    for start, end in ranges:
        del out[start:end]
    collapsed: List[str] = []
    blank_run = 0
    for ln in out:
        if ln.strip() == "":
            blank_run += 1
            if blank_run <= 1:
                collapsed.append(ln)
        else:
            blank_run = 0
            collapsed.append(ln)
    return collapsed


# ---------------------------------------------------------------------------
# Core extraction
# ---------------------------------------------------------------------------


def extract_questionnaire_blocks(
    lines: List[str],
) -> Tuple[List[str], List[Tuple[str, List[str]]]]:
    """Cut every 'Questionnaire for ...' block from `lines`.

    Returns (cleaned_lines, [(heading_text, block_lines), ...]).
    """
    headings = parse_headings(lines)
    extracted: List[Tuple[str, List[str]]] = []
    to_remove: List[Tuple[int, int]] = []
    for idx, (line_idx, _level, text) in enumerate(headings):
        if not text.strip().lower().startswith("questionnaire for"):
            continue
        end = _section_end(headings, idx, len(lines))
        block = lines[line_idx:end]
        while block and block[-1].strip() == "":
            block.pop()
        extracted.append((text.strip(), block))
        to_remove.append((line_idx, end))
    cleaned = _remove_ranges(lines, to_remove)
    return cleaned, extracted


def remove_existing_aggregate(lines: List[str]) -> List[str]:
    """Remove any pre-existing top-level 'Questionnaires' / 'Questionnaires for X'
    aggregate section."""
    headings = parse_headings(lines)
    to_remove: List[Tuple[int, int]] = []
    for idx, (line_idx, _level, text) in enumerate(headings):
        if AGGREGATE_TITLE_RE.match(text):
            end = _section_end(headings, idx, len(lines))
            to_remove.append((line_idx, end))
    if not to_remove:
        return lines
    return _remove_ranges(lines, to_remove)


def _aggregate_intro() -> str:
    return (
        "_Atomic, section-scoped questions aggregated from each section. "
        "Each question is answerable from the source section named in its heading._"
    )


def _format_aggregate_body(
    extracted: List[Tuple[str, List[str]]], child_heading_level: int = 2
) -> str:
    """Build the aggregate-section body (NO top-level heading — Phase 3 assembly
    emits that). Each collected Questionnaire-for-X block is re-emitted with
    its first heading normalized to `child_heading_level`.
    """
    prefix = "#" * child_heading_level
    parts: List[str] = [_aggregate_intro(), ""]
    for _title, block in extracted:
        if not block:
            continue
        first = block[0]
        m = HEADING_RE.match(first)
        if m:
            block = [f"{prefix} {m.group(2).strip()}"] + list(block[1:])
        parts.extend(block)
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Public API — dict / section-output mode (called between Phase 2 and Phase 3)
# ---------------------------------------------------------------------------

AGGREGATE_SECTION_ID = "questionnaires-for-program"


def aggregate_in_section_outputs(
    section_outputs: Dict[str, str],
    program_name: str,
    after_id: str = "error-handling",
) -> Tuple[Dict[str, str], Optional[Dict[str, Any]]]:
    """Strip 'Questionnaire for ...' blocks from each section's markdown and
    return a new dict plus a synthetic template-section descriptor.

    Args:
        section_outputs: Phase 2 output, `{section_id: markdown}`.
        program_name: used to build the aggregate title.
        after_id: diagnostic-only — the caller decides where to splice the
            synthetic section in the template via `inject_section_after`.

    Returns:
        (new_section_outputs, synthetic_or_None).
        - `new_section_outputs` is `section_outputs` with per-section
          questionnaires cut AND, if any were found, a new entry keyed by
          `AGGREGATE_SECTION_ID` containing the aggregate body.
        - `synthetic` is a dict `{"id": ..., "title": ...}` suitable to insert
          into the template's section list; `None` if no questionnaires existed.
    """
    extracted_all: List[Tuple[str, List[str]]] = []
    new_outputs: Dict[str, str] = {}

    for sec_id, md in section_outputs.items():
        # Also strip any stray aggregate the LLM may have emitted inline.
        lines = remove_existing_aggregate((md or "").split("\n"))
        cleaned, extracted = extract_questionnaire_blocks(lines)
        new_outputs[sec_id] = "\n".join(cleaned)
        extracted_all.extend(extracted)

    if not extracted_all:
        return new_outputs, None

    title = f"Questionnaires for {program_name}"
    aggregate_body = _format_aggregate_body(extracted_all, child_heading_level=2)
    new_outputs[AGGREGATE_SECTION_ID] = aggregate_body

    synthetic = {
        "id": AGGREGATE_SECTION_ID,
        "title": title,
    }
    return new_outputs, synthetic


def inject_section_after(
    template: Dict[str, Any],
    synthetic: Dict[str, Any],
    after_id: str,
) -> Dict[str, Any]:
    """Return a shallow copy of `template` with `synthetic` inserted directly
    after the first section whose `id == after_id`. If no such section is
    found, the synthetic is appended at the end of the sections list.
    """
    sections = list(template.get("sections", []) or [])

    # If the synthetic section is already present at the right spot, no-op.
    existing_ids = [s.get("id") for s in sections]
    if synthetic.get("id") in existing_ids:
        # Replace the existing entry in place to keep title fresh.
        new_sections: List[Dict[str, Any]] = []
        for sec in sections:
            if sec.get("id") == synthetic.get("id"):
                new_sections.append(synthetic)
            else:
                new_sections.append(sec)
        new_template = dict(template)
        new_template["sections"] = new_sections
        return new_template

    new_sections = []
    injected = False
    for sec in sections:
        new_sections.append(sec)
        if not injected and sec.get("id") == after_id:
            new_sections.append(synthetic)
            injected = True
    if not injected:
        new_sections.append(synthetic)

    new_template = dict(template)
    new_template["sections"] = new_sections
    return new_template


# ---------------------------------------------------------------------------
# File-based mode — used by the CLI wrapper on an already-assembled document
# ---------------------------------------------------------------------------


RE_DOC_HEADER = re.compile(r"^#\s+(.+?)\s*-\s*Code Documentation", re.MULTILINE)


def _detect_program_name(text: str) -> Optional[str]:
    m = RE_DOC_HEADER.search(text)
    return m.group(1).strip() if m else None


def _detect_error_handling_level(lines: List[str]) -> int:
    for _line_idx, level, text in parse_headings(lines):
        if text.strip().lower() == "error handling strategy":
            return level
    return 1


def _build_aggregate_section_text(
    extracted: List[Tuple[str, List[str]]],
    parent_level: int,
    title: str,
) -> List[str]:
    """Build the FULL aggregate section (heading + body) for file-based rewrites."""
    child_prefix = "#" * (parent_level + 1)
    out: List[str] = ["", f"{'#' * parent_level} {title}", "", _aggregate_intro(), ""]
    for _title, block in extracted:
        if not block:
            continue
        first = block[0]
        m = HEADING_RE.match(first)
        if m:
            block = [f"{child_prefix} {m.group(2).strip()}"] + list(block[1:])
        out.extend(block)
        out.append("")
    return out


def _insert_after_error_handling(
    lines: List[str], aggregate: List[str]
) -> List[str]:
    headings = parse_headings(lines)
    eh_idx = None
    for idx, (_line_idx, _level, text) in enumerate(headings):
        if text.strip().lower() == "error handling strategy":
            eh_idx = idx
            break
    if eh_idx is None:
        return lines + aggregate
    insert_at = _section_end(headings, eh_idx, len(lines))
    return lines[:insert_at] + aggregate + lines[insert_at:]


def process_text(text: str, program_name: Optional[str] = None) -> Tuple[str, int]:
    """File-based mode: CUT every 'Questionnaire for ...' block from the
    assembled markdown and re-PASTE them into a single 'Questionnaires for <name>'
    section inserted after 'Error Handling Strategy'.

    Args:
        text: Complete markdown document.
        program_name: Used in the aggregate heading. When omitted, it is
            auto-detected from the doc header; if that fails, "Program" is used.

    Returns:
        (new_text, count_of_blocks_moved).
    """
    had_trailing_newline = text.endswith("\n")
    lines = text.split("\n")
    if had_trailing_newline:
        lines = lines[:-1]

    detected = program_name or _detect_program_name(text) or "Program"
    title = f"Questionnaires for {detected}"

    parent_level = _detect_error_handling_level(lines)
    # Extract first (preserves children of any prior aggregate), then remove
    # the old aggregate container so re-runs don't double up.
    lines, extracted = extract_questionnaire_blocks(lines)
    lines = remove_existing_aggregate(lines)
    if not extracted:
        result = "\n".join(lines)
        return (result + "\n") if had_trailing_newline else result, 0

    aggregate = _build_aggregate_section_text(extracted, parent_level, title)
    lines = _insert_after_error_handling(lines, aggregate)
    result = "\n".join(lines)
    return (result + "\n") if had_trailing_newline else result, len(extracted)


def process_file(
    path: Path,
    out_path: Optional[Path] = None,
    in_place: bool = False,
    program_name: Optional[str] = None,
) -> None:
    text = path.read_text()
    new_text, moved = process_text(text, program_name=program_name)
    if moved == 0:
        print(f"  {path}: no questionnaire blocks found — unchanged")
        return
    target = path if in_place else (out_path or path.with_suffix(".aggregated.md"))
    target.write_text(new_text)
    print(f"  {path} → {target}  ({moved} block(s) moved)")


def cli(argv: Optional[List[str]] = None) -> int:
    """CLI entry point shared by scripts/aggregate_questionnaires.py."""
    import argparse

    parser = argparse.ArgumentParser(
        description=(
            "Move 'Questionnaire for ...' blocks into a single "
            "'Questionnaires for <ProgramName>' section placed after "
            "'Error Handling Strategy'."
        )
    )
    parser.add_argument("input", help="Path to a Markdown file or a directory of .md files.")
    parser.add_argument(
        "-o", "--output", help="Output path (single-file input only)."
    )
    parser.add_argument(
        "-i", "--in-place", action="store_true", help="Edit files in place."
    )
    parser.add_argument(
        "--program-name",
        default=None,
        help="Override program name used in the aggregate heading "
             "(default: auto-detect from '# <Name> - Code Documentation' header).",
    )
    args = parser.parse_args(argv)

    src = Path(args.input).resolve()
    if not src.exists():
        print(f"ERROR: Path not found: {src}", file=sys.stderr)
        return 1

    if src.is_dir():
        if args.output:
            print("ERROR: --output is only valid for a single-file input.", file=sys.stderr)
            return 2
        md_files = sorted(src.rglob("*.md"))
        if not md_files:
            print(f"No .md files found under {src}")
            return 0
        print(f"Processing {len(md_files)} file(s) under {src}")
        for f in md_files:
            process_file(f, in_place=args.in_place, program_name=args.program_name)
    else:
        process_file(
            src,
            out_path=Path(args.output).resolve() if args.output else None,
            in_place=args.in_place,
            program_name=args.program_name,
        )
    return 0


if __name__ == "__main__":
    sys.exit(cli())
