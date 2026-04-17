#!/usr/bin/env python3
"""
Aggregate per-section "Questionnaire for ..." blocks into a single
"Questionnaires" section placed immediately AFTER the "Error Handling Strategy"
section in a generated documentation Markdown file.

Behavior: CUT and PASTE — the original per-section questionnaire blocks are
REMOVED from their original locations and moved into the aggregated section.

Usage:
    # In-place edit of a single file:
    python3 scripts/aggregate_questionnaires.py path/to/doc.md --in-place

    # Write to a new file:
    python3 scripts/aggregate_questionnaires.py path/to/doc.md -o path/to/out.md

    # Process every .md file under a directory (in place):
    python3 scripts/aggregate_questionnaires.py path/to/docs/ --in-place

A questionnaire block is any heading whose text starts with
"Questionnaire for" (case-insensitive) plus all lines up to the next heading
at the same or higher level.

If an aggregate "Questionnaires" section already exists, it is removed first so
the script is safe to re-run.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")


def parse_headings(lines: List[str]) -> List[Tuple[int, int, str]]:
    """Return [(line_index, level, text), ...] for every ATX heading."""
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
    """Return the line index where this section ends (first line of next
    same-or-higher-level heading, or EOF)."""
    level = headings[heading_idx][1]
    for j in range(heading_idx + 1, len(headings)):
        if headings[j][1] <= level:
            return headings[j][0]
    return total_lines


def _remove_ranges(lines: List[str], ranges: List[Tuple[int, int]]) -> List[str]:
    """Remove half-open [start, end) ranges from lines, collapsing runs of
    blank lines produced by the removal to at most one."""
    ranges = sorted(ranges, reverse=True)
    out = list(lines)
    for start, end in ranges:
        del out[start:end]
    # Collapse 3+ consecutive blank lines down to 1.
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


def remove_existing_aggregate(lines: List[str]) -> List[str]:
    """Remove any existing top-level 'Questionnaires' aggregate section."""
    headings = parse_headings(lines)
    to_remove: List[Tuple[int, int]] = []
    for idx, (line_idx, _level, text) in enumerate(headings):
        if text.strip().lower() == "questionnaires":
            end = _section_end(headings, idx, len(lines))
            to_remove.append((line_idx, end))
    if not to_remove:
        return lines
    return _remove_ranges(lines, to_remove)


def extract_questionnaire_blocks(
    lines: List[str],
) -> Tuple[List[str], List[Tuple[str, List[str]]]]:
    """Cut every 'Questionnaire for ...' block from lines.

    Returns (cleaned_lines, [(title, block_lines), ...]).
    """
    headings = parse_headings(lines)
    extracted: List[Tuple[str, List[str]]] = []
    to_remove: List[Tuple[int, int]] = []
    for idx, (line_idx, _level, text) in enumerate(headings):
        if not text.strip().lower().startswith("questionnaire for"):
            continue
        end = _section_end(headings, idx, len(lines))
        block = lines[line_idx:end]
        # Trim trailing blank lines from the block itself.
        while block and block[-1].strip() == "":
            block.pop()
        extracted.append((text.strip(), block))
        to_remove.append((line_idx, end))
    cleaned = _remove_ranges(lines, to_remove)
    return cleaned, extracted


def build_aggregate_section(
    extracted: List[Tuple[str, List[str]]], parent_level: int
) -> List[str]:
    """Build the aggregated 'Questionnaires' section.

    The aggregate heading is placed at `parent_level` (same as Error Handling
    Strategy). Each questionnaire sub-heading is normalized to `parent_level+1`.
    """
    child_prefix = "#" * (parent_level + 1)
    out: List[str] = []
    out.append("")
    out.append(f"{'#' * parent_level} Questionnaires")
    out.append("")
    out.append(
        "_Atomic, section-scoped questions aggregated from each section. "
        "Each question is answerable from the source section named in its heading._"
    )
    out.append("")
    for title, block in extracted:
        # Rewrite the first heading line to the normalized child level.
        first = block[0]
        m = HEADING_RE.match(first)
        if m:
            block = [f"{child_prefix} {m.group(2).strip()}"] + list(block[1:])
        out.extend(block)
        out.append("")
    return out


def insert_after_error_handling(
    lines: List[str], aggregate: List[str], parent_level: int
) -> List[str]:
    """Insert `aggregate` right after the Error Handling Strategy section.

    If no Error Handling Strategy heading is found, the aggregate is appended
    at end of file.
    """
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


def detect_error_handling_level(lines: List[str]) -> int:
    """Return the heading level of the Error Handling Strategy section.
    Defaults to 1 if not found."""
    for _line_idx, level, text in parse_headings(lines):
        if text.strip().lower() == "error handling strategy":
            return level
    return 1


def process_text(text: str) -> Tuple[str, int]:
    """Run the full pipeline on a single Markdown string.

    Returns (new_text, count_of_blocks_moved).
    """
    # Preserve trailing newline if present.
    had_trailing_newline = text.endswith("\n")
    lines = text.split("\n")
    if had_trailing_newline:
        lines = lines[:-1]

    parent_level = detect_error_handling_level(lines)
    # Extract first so children inside an existing aggregate are preserved;
    # then remove the now-empty aggregate container (if any).
    lines, extracted = extract_questionnaire_blocks(lines)
    lines = remove_existing_aggregate(lines)
    if not extracted:
        result = "\n".join(lines)
        return (result + "\n") if had_trailing_newline else result, 0

    aggregate = build_aggregate_section(extracted, parent_level)
    lines = insert_after_error_handling(lines, aggregate, parent_level)
    result = "\n".join(lines)
    return (result + "\n") if had_trailing_newline else result, len(extracted)


def process_file(path: Path, out_path: Path | None, in_place: bool) -> None:
    text = path.read_text()
    new_text, moved = process_text(text)
    if moved == 0:
        print(f"  {path}: no questionnaire blocks found — unchanged")
        return
    target = path if in_place else (out_path or path.with_suffix(".aggregated.md"))
    target.write_text(new_text)
    print(f"  {path} → {target}  ({moved} block(s) moved)")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Move all 'Questionnaire for ...' blocks into a single "
        "'Questionnaires' section placed after 'Error Handling Strategy'."
    )
    parser.add_argument(
        "input",
        help="Path to a Markdown file, or a directory containing .md files.",
    )
    parser.add_argument(
        "-o", "--output",
        help="Output path (only valid when input is a single file). "
             "Defaults to '<input>.aggregated.md' when --in-place is not set.",
    )
    parser.add_argument(
        "-i", "--in-place",
        action="store_true",
        help="Edit files in place.",
    )
    args = parser.parse_args()

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
            process_file(f, out_path=None, in_place=args.in_place)
    else:
        process_file(
            src,
            out_path=Path(args.output).resolve() if args.output else None,
            in_place=args.in_place,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
