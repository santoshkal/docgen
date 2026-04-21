"""
PageIndex tree builder — parses a Phase 1 code-explanation Markdown into a
hierarchical chunk → block tree.

Two modes:
  - `extract` (zero-LLM, default): parses Purpose/Technical/CrossRef/CallFlow/
    DataFlow blocks from the structured Phase 1 document.
  - `llm`: delegates to preprocess_pageindex (PageIndex project + Claude
    summaries) — requires PAGEINDEX_PATH env var.

Ported from ~/rlm/demo/extract_pageindex.py with the CLI stripped out; only
the library functions are exposed.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

# ---------------------------------------------------------------------------
# Regex patterns for Phase 1 document structure
# ---------------------------------------------------------------------------

RE_CHUNK_HEADER = re.compile(
    r"^## Hash-ID:\s*(\S+)\s*\|\s*Chunk\s+(\d+)/(\d+)\s*\|\s*Lines:\s*(\d+)-(\d+)",
    re.MULTILINE,
)

RE_BLOCK_HEADER = re.compile(
    r"^#### Block\s+(\d+):\s*(.+?)\s*\(Lines\s+(\d+)[\u2013\-](\d+)\)",
    re.MULTILINE,
)

RE_PURPOSE_FUNCTIONAL = re.compile(
    r"\*\*Purpose:\*\*\s*\n-\s*\*\*Functional\*\*:\s*(.+?)(?:\n-\s*\*\*|\n\n|\n\*\*)",
    re.DOTALL,
)

RE_BOLD_SECTION = re.compile(
    r"^\*\*(.+?):\*\*\s*\n(.*?)(?=^\*\*[A-Z].+?:\*\*|\n---|\Z)",
    re.MULTILINE | re.DOTALL,
)

RE_CHUNK_SUMMARY = re.compile(
    r"### Chunk Summary for Chunk-ID:\s*\S+\s*\n+\*\*Summary:\*\*\s*(.+?)(?:\n---|\n\n###|\Z)",
    re.DOTALL,
)

RE_RETRIEVAL_TAGS = re.compile(
    r"### Retrieval Tags for Chunk-ID:\s*\S+\s*\n+\*\*Tags:\*\*\s*(.+?)(?:\n---|\n\n###|\Z)",
    re.DOTALL,
)

RE_RETRIEVAL_QUESTIONS = re.compile(
    r"### Retrieval Questions for Chunk-ID:\s*\S+\s*\n+((?:\d+\..+\n?)+)",
    re.MULTILINE,
)

RE_DOC_HEADER = re.compile(r"^# (.+?)\s*-\s*Code Documentation", re.MULTILINE)
RE_SOURCE_FILE = re.compile(r"\*\*Source\*\*:\s*`(.+?)`")


# ---------------------------------------------------------------------------
# Extraction helpers
# ---------------------------------------------------------------------------


def extract_doc_metadata(content: str) -> Dict[str, str]:
    result: Dict[str, str] = {}
    m = RE_DOC_HEADER.search(content)
    if m:
        result["program_name"] = m.group(1).strip()
    m = RE_SOURCE_FILE.search(content)
    if m:
        result["source_file"] = m.group(1).strip()
    return result


def extract_purpose_functional(text: str) -> str:
    m = RE_PURPOSE_FUNCTIONAL.search(text)
    return m.group(1).strip() if m else ""


def extract_block_sections(block_text: str) -> Dict[str, Any]:
    """Parse bold sub-sections (Purpose / Technical Details / Cross-References /
    Call Flow / Data Flow / ...) into structured fields."""
    sections: Dict[str, Any] = {}

    for m in RE_BOLD_SECTION.finditer(block_text):
        header = m.group(1).strip()
        body = m.group(2).strip()
        if not body:
            continue

        key = header.lower().replace("-", " ").replace(" ", "_")

        if header == "Purpose":
            purpose: Dict[str, str] = {}
            for line in body.split("\n"):
                line = line.strip()
                pm = re.match(r"-\s*\*\*(.+?)\*\*:\s*(.+)", line)
                if pm:
                    sub_key = pm.group(1).lower().replace(" ", "_")
                    purpose[sub_key] = pm.group(2).strip()
            sections["purpose"] = purpose

        elif header == "Technical Details":
            details: Dict[str, str] = {}
            for line in body.split("\n"):
                line = line.strip()
                dm = re.match(r"-\s*(.+?):\s*(.+)", line)
                if dm:
                    sub_key = dm.group(1).strip().lower().replace("/", "_").replace(" ", "_")
                    details[sub_key] = dm.group(2).strip()
            sections["technical_details"] = details

        elif header == "Cross-References":
            xrefs: Dict[str, str] = {}
            for line in body.split("\n"):
                line = line.strip()
                xm = re.match(r"-\s*(.+?):\s*(.+)", line)
                if xm:
                    sub_key = xm.group(1).strip().lower().replace(" ", "_")
                    xrefs[sub_key] = xm.group(2).strip()
            sections["cross_references"] = xrefs

        elif header in ("Call Flow", "Data Flow"):
            lines = [line.strip().lstrip("- ") for line in body.split("\n") if line.strip()]
            sections[key] = lines

        elif header == "Detailed Line-by-line Explanation":
            # Skip — too verbose; the full text is already kept on the node.
            continue

        else:
            sections[key] = body

    return sections


def extract_chunk_metadata(chunk_text: str) -> Dict[str, Any]:
    result: Dict[str, Any] = {}

    m = RE_CHUNK_SUMMARY.search(chunk_text)
    if m:
        result["summary"] = m.group(1).strip()

    m = RE_RETRIEVAL_TAGS.search(chunk_text)
    if m:
        tags_str = m.group(1).strip()
        result["tags"] = [t.strip() for t in tags_str.split(",") if t.strip()]

    m = RE_RETRIEVAL_QUESTIONS.search(chunk_text)
    if m:
        questions_text = m.group(1).strip()
        result["retrieval_questions"] = [
            re.sub(r"^\d+\.\s*", "", q.strip())
            for q in questions_text.split("\n")
            if q.strip()
        ]

    return result


def split_into_chunks(content: str) -> List[Tuple[str, str, int, int, int, int]]:
    matches = list(RE_CHUNK_HEADER.finditer(content))
    if not matches:
        return []

    chunks: List[Tuple[str, str, int, int, int, int]] = []
    for i, m in enumerate(matches):
        hash_id = m.group(1)
        chunk_num = int(m.group(2))
        total_chunks = int(m.group(3))
        start_line = int(m.group(4))
        end_line = int(m.group(5))

        chunk_start = m.start()
        chunk_end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        chunk_text = content[chunk_start:chunk_end]

        chunks.append((hash_id, chunk_text, chunk_num, total_chunks, start_line, end_line))

    return chunks


def extract_blocks_from_chunk(chunk_text: str) -> List[Dict[str, Any]]:
    matches = list(RE_BLOCK_HEADER.finditer(chunk_text))
    if not matches:
        return []

    blocks: List[Dict[str, Any]] = []
    for i, m in enumerate(matches):
        block_num = int(m.group(1))
        title = m.group(2).strip()
        start_line = int(m.group(3))
        end_line = int(m.group(4))

        block_start = m.start()
        block_end = matches[i + 1].start() if i + 1 < len(matches) else len(chunk_text)
        block_text = chunk_text[block_start:block_end].strip()

        sections = extract_block_sections(block_text)

        purpose = sections.get("purpose", {})
        summary = purpose.get("functional", extract_purpose_functional(block_text))

        block: Dict[str, Any] = {
            "title": f"Block {block_num}: {title} (Lines {start_line}-{end_line})",
            "node_id": None,
            "summary": summary,
            "text": block_text,
            "line_num": start_line,
        }

        if purpose:
            block["purpose"] = purpose
        for k in ("technical_details", "cross_references", "call_flow", "data_flow"):
            if sections.get(k):
                block[k] = sections[k]

        blocks.append(block)

    return blocks


def build_tree(content: str) -> Dict[str, Any]:
    """Build the full PageIndex tree from a code explanation document."""
    doc_meta = extract_doc_metadata(content)
    chunks = split_into_chunks(content)

    node_counter = 0
    tree_nodes: List[Dict[str, Any]] = []

    for hash_id, chunk_text, chunk_num, total_chunks, start_line, end_line in chunks:
        chunk_meta = extract_chunk_metadata(chunk_text)
        chunk_node: Dict[str, Any] = {
            "title": f"Chunk {chunk_num}/{total_chunks} | Lines: {start_line}-{end_line}",
            "node_id": str(node_counter).zfill(4),
            "hash_id": hash_id,
            "summary": chunk_meta.get("summary", ""),
            "tags": chunk_meta.get("tags", []),
            "retrieval_questions": chunk_meta.get("retrieval_questions", []),
            "line_start": start_line,
            "line_end": end_line,
        }
        node_counter += 1

        blocks = extract_blocks_from_chunk(chunk_text)
        child_nodes: List[Dict[str, Any]] = []
        for block in blocks:
            block["node_id"] = str(node_counter).zfill(4)
            child_nodes.append(block)
            node_counter += 1

        chunk_node["nodes"] = child_nodes
        tree_nodes.append(chunk_node)

    return {
        "doc_name": doc_meta.get("program_name", Path("unknown").stem),
        "source_file": doc_meta.get("source_file", ""),
        "extraction_mode": "zero-llm",
        "structure": tree_nodes,
    }


def count_nodes(nodes: List[Dict[str, Any]]) -> int:
    return sum(1 + count_nodes(n.get("nodes", [])) for n in nodes)


def build_pageindex(
    code_explanation: str,
    mode: str = "extract",
    include_text: bool = True,
    **llm_mode_kwargs: Any,
) -> Dict[str, Any]:
    """
    Build a PageIndex tree from the Phase 1 code-explanation markdown.

    Args:
        code_explanation: Phase 1 markdown content.
        mode: "extract" (zero-LLM, default) or "llm".
        include_text: If False, drop the `text` field from block nodes after build.
        **llm_mode_kwargs: Forwarded to preprocess_pageindex.build_pageindex_tree()
            when `mode == "llm"` (model, max_concurrent, thinning, min_token_threshold).

    Returns:
        Dict with keys: doc_name, source_file, structure, extraction_mode, ...
    """
    if mode == "extract":
        tree = build_tree(code_explanation)
        if not include_text:
            for chunk in tree.get("structure", []):
                for block in chunk.get("nodes", []):
                    block.pop("text", None)
        return tree

    if mode == "llm":
        # Delegates to the PageIndex-backed summary pipeline (requires the
        # PageIndex project on disk — see preprocess_pageindex.py for env vars).
        # We import lazily so the extract-mode default has zero extra deps.
        import tempfile
        import os
        import sys
        from pathlib import Path as _P

        # preprocess_pageindex reads from a file path, so tee to a temp file.
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False, encoding="utf-8"
        ) as tmp:
            tmp.write(code_explanation)
            tmp_path = tmp.name

        # Import from the sibling demo project (or user-configured path).
        demo_root = os.environ.get(
            "RLM_DEMO_PATH", os.path.expanduser("~/rlm/demo")
        )
        if not _P(demo_root).exists():
            raise FileNotFoundError(
                f"mode='llm' requires the RLM demo project at {demo_root}. "
                "Set RLM_DEMO_PATH or use mode='extract'."
            )
        sys.path.insert(0, demo_root)
        try:
            from preprocess_pageindex import build_pageindex_tree  # type: ignore
        finally:
            sys.path.pop(0)

        tree = build_pageindex_tree(
            md_path=tmp_path,
            if_text=include_text,
            **llm_mode_kwargs,
        )
        os.unlink(tmp_path)
        return tree

    raise ValueError(f"Unknown pageindex mode: {mode!r} (expected 'extract' or 'llm')")
