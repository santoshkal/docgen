"""
Relationship Provider — loads pre-generated multilspy metadata and provides
chunk-scoped cross-reference context for the documentation pipeline.

Loads per-source-file JSONs from the directory configured via
output.cross_references_dir in the config YAML.

Usage:
    provider = RelationshipProvider("/path/to/cross_references/per_file")
    context = provider.get_context_for_chunk("DataCommands/PickList.cs", 43, 218)

The returned context is a plaintext string ready to inject into the LLM prompt.
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

# Symbol kinds to exclude from cross-reference output (too noisy)
NOISE_KINDS = {"NAMESPACE"}

# Symbol kinds that represent type-level definitions
TYPE_KINDS = {"CLASS", "INTERFACE", "ENUM", "STRUCT"}


def _safe_filename(file_path: str) -> str:
    """Convert a source file path to the safe filename used in per_file/ directory."""
    return file_path.replace("/", "__").replace("\\", "__")


class _FileData:
    """Cross-reference data for a single source file."""
    __slots__ = ("symbols", "cross_file_outgoing", "cross_file_incoming", "intra_file_refs")

    def __init__(
        self,
        symbols: List[dict],
        cross_file_outgoing: List[dict],
        cross_file_incoming: List[dict],
        intra_file_refs: List[dict],
    ):
        self.symbols = symbols
        self.cross_file_outgoing = cross_file_outgoing
        self.cross_file_incoming = cross_file_incoming
        self.intra_file_refs = intra_file_refs


class RelationshipProvider:
    """Loads per-file multilspy metadata and slices it per chunk."""

    def __init__(self, cross_references_dir: str):
        """
        Args:
            cross_references_dir: Path to directory containing per-source-file
                                  JSON files (e.g., DataCommands__PickList.cs.json)
        """
        self._cross_ref_dir = Path(cross_references_dir)
        # Cache for loaded per-file data (keyed by file_path)
        self._file_cache: Dict[str, Optional[_FileData]] = {}

        if not self._cross_ref_dir.is_dir():
            raise FileNotFoundError(
                f"Cross-references directory not found: {self._cross_ref_dir}"
            )

    def _load_file_data(self, file_path: str) -> Optional[_FileData]:
        """Load cross-reference data for a single source file from its per-file JSON."""
        if file_path in self._file_cache:
            return self._file_cache[file_path]

        json_path = self._cross_ref_dir / f"{_safe_filename(file_path)}.json"
        if not json_path.exists():
            self._file_cache[file_path] = None
            return None

        with open(json_path) as f:
            raw = json.load(f)

        data = _FileData(
            symbols=raw.get("symbols", []),
            cross_file_outgoing=raw.get("cross_file_outgoing", []),
            cross_file_incoming=raw.get("cross_file_incoming", []),
            intra_file_refs=raw.get("intra_file_refs", []),
        )
        self._file_cache[file_path] = data
        logger.info(f"Loaded cross-references for {file_path}: "
                     f"{len(data.symbols)} symbols, "
                     f"{len(data.cross_file_outgoing)} outgoing, "
                     f"{len(data.cross_file_incoming)} incoming, "
                     f"{len(data.intra_file_refs)} intra")
        return data

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def has_data_for_file(self, file_path: str) -> bool:
        """Check if we have metadata for this file."""
        return self._load_file_data(file_path) is not None

    def get_symbols_for_chunk(
        self, file_path: str, start_line: int, end_line: int
    ) -> List[dict]:
        """Get symbols whose range overlaps with the chunk."""
        data = self._load_file_data(file_path)
        if not data:
            return []
        return [
            s for s in data.symbols
            if s.get("range_start") is not None
            and s.get("range_end") is not None
            and s["range_start"] <= end_line
            and s["range_end"] >= start_line
        ]

    def get_cross_file_outgoing(
        self, file_path: str, start_line: int, end_line: int
    ) -> List[dict]:
        """Symbols defined in this chunk that are referenced from other files."""
        data = self._load_file_data(file_path)
        if not data:
            return []
        return [
            e for e in data.cross_file_outgoing
            if start_line <= e["defined_at_line"] <= end_line
        ]

    def get_cross_file_incoming(
        self, file_path: str, start_line: int, end_line: int
    ) -> List[dict]:
        """Symbols from other files that are referenced within this chunk's line range."""
        data = self._load_file_data(file_path)
        if not data:
            return []
        return [
            e for e in data.cross_file_incoming
            if start_line <= e["referenced_at_line"] <= end_line
        ]

    def get_intra_file_refs(
        self, file_path: str, start_line: int, end_line: int
    ) -> List[dict]:
        """Intra-file relationships where the reference occurs in this chunk."""
        data = self._load_file_data(file_path)
        if not data:
            return []
        return [
            e for e in data.intra_file_refs
            if start_line <= e["reference_at_line"] <= end_line
        ]

    def get_context_for_chunk(
        self, file_path: str, start_line: int, end_line: int
    ) -> Optional[str]:
        """
        Build a plaintext cross-reference context block for a source chunk.

        Returns None if no metadata is available for this file.
        Returns a formatted string ready to inject into the LLM prompt.
        """
        if not self.has_data_for_file(file_path):
            return None

        symbols = self.get_symbols_for_chunk(file_path, start_line, end_line)
        outgoing = self.get_cross_file_outgoing(file_path, start_line, end_line)
        incoming = self.get_cross_file_incoming(file_path, start_line, end_line)
        intra = self.get_intra_file_refs(file_path, start_line, end_line)

        if not symbols and not outgoing and not incoming and not intra:
            return None

        parts = []

        # Max items per section to keep prompt size manageable
        MAX_DEPS = 15
        MAX_DEPENDENTS = 10
        MAX_INTRA = 15

        # 1. Dependencies: what this chunk uses from other files
        if incoming:
            deps = _summarize_incoming(incoming)
            if deps:
                parts.append("**Dependencies (uses from other files):**")
                for dep in deps[:MAX_DEPS]:
                    parts.append(f"  - {dep}")
                if len(deps) > MAX_DEPS:
                    parts.append(f"  - ... and {len(deps) - MAX_DEPS} more")

        # 2. Dependents: who uses symbols defined in this chunk
        if outgoing:
            deps = _summarize_outgoing(outgoing)
            if deps:
                parts.append("**Dependents (used by other files):**")
                for dep in deps[:MAX_DEPENDENTS]:
                    parts.append(f"  - {dep}")
                if len(deps) > MAX_DEPENDENTS:
                    parts.append(f"  - ... and {len(deps) - MAX_DEPENDENTS} more")

        # 3. Intra-file references within this chunk
        if intra:
            refs = _summarize_intra(intra)
            if refs:
                parts.append("**Internal references (within this file):**")
                for ref in refs[:MAX_INTRA]:
                    parts.append(f"  - {ref}")
                if len(refs) > MAX_INTRA:
                    parts.append(f"  - ... and {len(refs) - MAX_INTRA} more")

        if not parts:
            return None

        return "\n".join(parts)

    def get_file_summary(self, file_path: str) -> Optional[str]:
        """
        Build a high-level cross-reference summary for the entire file.
        Useful for Phase 2 section generation (executive summary, dependencies).
        """
        data = self._load_file_data(file_path)
        if not data:
            return None

        outgoing = data.cross_file_outgoing
        incoming = data.cross_file_incoming

        if not outgoing and not incoming:
            return None

        parts = []

        # Type-level symbols defined in this file
        types = [s for s in data.symbols if s.get("kind_name") in TYPE_KINDS]
        if types:
            parts.append("**Types defined in this file:**")
            for t in types:
                type_refs = [
                    e for e in outgoing
                    if e["symbol"] == t["name"] and e["defined_at_line"] == t.get("line")
                ]
                ref_files = set(e["referenced_in"] for e in type_refs)
                if ref_files:
                    parts.append(f"  - {t['kind_name']} {t['name']}: referenced by {len(ref_files)} files")
                else:
                    parts.append(f"  - {t['kind_name']} {t['name']}")

        # Files this file depends on
        dep_files = set(e["defined_in"] for e in incoming)
        if dep_files:
            parts.append(f"**Depends on ({len(dep_files)} files):**")
            for f in sorted(dep_files)[:15]:
                count = sum(1 for e in incoming if e["defined_in"] == f)
                parts.append(f"  - {f} ({count} references)")
            if len(dep_files) > 15:
                parts.append(f"  - ... and {len(dep_files) - 15} more")

        # Files that depend on this file
        dependent_files = set(e["referenced_in"] for e in outgoing)
        if dependent_files:
            parts.append(f"**Depended on by ({len(dependent_files)} files):**")
            for f in sorted(dependent_files)[:15]:
                count = sum(1 for e in outgoing if e["referenced_in"] == f)
                parts.append(f"  - {f} ({count} references)")
            if len(dependent_files) > 15:
                parts.append(f"  - ... and {len(dependent_files) - 15} more")

        return "\n".join(parts) if parts else None


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

def _summarize_incoming(edges: List[dict]) -> List[str]:
    """Summarize cross-file dependencies: what symbols this chunk uses from other files."""
    by_symbol: Dict[str, list] = {}
    for e in edges:
        by_symbol.setdefault(e["symbol"], []).append(e)

    lines = []
    for symbol, symbol_edges in sorted(by_symbol.items(), key=lambda x: min(e["referenced_at_line"] for e in x[1])):
        source_files = set(e["defined_in"] for e in symbol_edges)
        kind = symbol_edges[0]["kind"]

        if len(source_files) > 5:
            lines.append(
                f"{kind} `{symbol}`: defined in {len(source_files)} files (common override/interface method)"
            )
        else:
            for src_file in sorted(source_files):
                file_edges = [e for e in symbol_edges if e["defined_in"] == src_file]
                src_line = file_edges[0]["defined_at_line"]
                ref_count = len(file_edges)
                at = f"at L{file_edges[0]['referenced_at_line']}" if ref_count == 1 else f"at {ref_count} locations"
                lines.append(f"{kind} `{symbol}` from {src_file}:{src_line} ({at})")
    return lines


def _summarize_outgoing(edges: List[dict]) -> List[str]:
    """Summarize cross-file dependents: symbols defined here, used elsewhere."""
    grouped: Dict[str, Dict] = {}
    for e in edges:
        key = f"{e['symbol']}|{e['defined_at_line']}"
        if key not in grouped:
            grouped[key] = {
                "symbol": e["symbol"],
                "kind": e["kind"],
                "line": e["defined_at_line"],
                "ref_files": set(),
                "ref_count": 0,
            }
        grouped[key]["ref_files"].add(e["referenced_in"])
        grouped[key]["ref_count"] += 1

    lines = []
    for g in sorted(grouped.values(), key=lambda x: -x["ref_count"]):
        file_count = len(g["ref_files"])
        file_list = ", ".join(sorted(g["ref_files"])[:3])
        if file_count > 3:
            file_list += f", ... (+{file_count - 3} more)"
        lines.append(
            f"{g['kind']} `{g['symbol']}` (L{g['line']}): {g['ref_count']} refs from {file_count} files [{file_list}]"
        )
    return lines


def _summarize_intra(edges: List[dict]) -> List[str]:
    """Summarize intra-file relationships: who references whom within this chunk."""
    grouped: Dict[str, Dict] = {}
    for e in edges:
        key = f"{e['from_symbol']}→{e['to_symbol']}"
        if key not in grouped:
            grouped[key] = {
                "from": e["from_symbol"],
                "from_kind": e["from_kind"],
                "to": e["to_symbol"],
                "to_kind": e["to_kind"],
                "ref_lines": [],
            }
        grouped[key]["ref_lines"].append(e["reference_at_line"])

    lines = []
    for g in sorted(grouped.values(), key=lambda x: min(x["ref_lines"])):
        ref_count = len(g["ref_lines"])
        at = f"at L{g['ref_lines'][0]}" if ref_count == 1 else f"at {ref_count} locations"
        lines.append(f"`{g['from']}` ({g['from_kind']}) references `{g['to']}` ({g['to_kind']}) {at}")
    return lines
