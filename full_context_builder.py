"""
Full Context Builder Module

Provides a class to assemble complete context for LLM calls including:
- Full source code with optional line numbers
- All metadata without filtering (CTags, SuperBol, GnuCOBOL)
- Enhanced program map with configurable limits

This module is part of the Full Context Mode enhancement that enables
sending complete source + metadata + program map to each LLM call for
comprehensive documentation generation.

US-1.1: Create Full Context Builder Class
"""

import json
from pathlib import Path
from typing import Any, Dict, Optional, Union

# Import program map generator for enhanced program map
try:
    from cobol_program_map import generate_cobol_program_map
    PROGRAM_MAP_AVAILABLE = True
except ImportError:
    PROGRAM_MAP_AVAILABLE = False


class FullContextBuilder:
    """
    Assembles complete context (source + metadata + program map) for LLM calls.

    This class provides methods to:
    - Load complete source code with optional line numbers
    - Load all metadata without filtering
    - Generate enhanced program map with configurable limits
    - Build combined context dictionary

    Attributes:
        program_name: Name of the COBOL program
        source_file_path: Path to the COBOL source file
        metadata_dir: Path to the metadata directory
        source_file_exists: Whether the source file exists
        metadata_dir_exists: Whether the metadata directory exists
    """

    def __init__(
        self,
        program_name: str,
        source_file_path: Union[str, Path],
        metadata_dir: Union[str, Path]
    ):
        """
        Initialize the FullContextBuilder.

        Args:
            program_name: Name of the COBOL program (e.g., "TESTPROG")
            source_file_path: Path to the COBOL source file
            metadata_dir: Path to the metadata directory containing
                          ctags/, superbol/, gnucobol/ subdirectories
        """
        self.program_name = program_name
        self.source_file_path = Path(source_file_path)
        self.metadata_dir = Path(metadata_dir)

        # Check existence flags
        self.source_file_exists = self.source_file_path.exists()
        self.metadata_dir_exists = self.metadata_dir.exists()

        # Cached metadata
        self._metadata_cache: Optional[Dict[str, Any]] = None

    def load_full_source_code(
        self,
        include_line_numbers: bool = False
    ) -> Optional[str]:
        """
        Load the complete COBOL source file.

        Args:
            include_line_numbers: If True, prefix each line with its line number

        Returns:
            Complete source code as a string, or None if file doesn't exist
        """
        if not self.source_file_exists:
            return None

        try:
            with open(self.source_file_path, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()

            if include_line_numbers:
                # Format: right-aligned line number with colon, then tab, then content
                # Example: "   1:\t       IDENTIFICATION DIVISION."
                max_line_num = len(lines)
                width = len(str(max_line_num))
                numbered_lines = []
                for i, line in enumerate(lines, start=1):
                    # Remove trailing newline, add line number prefix
                    line_content = line.rstrip('\n\r')
                    numbered_lines.append(f"{i:>{width}}:\t{line_content}")
                return '\n'.join(numbered_lines)
            else:
                return ''.join(lines)

        except Exception as e:
            print(f"Error loading source code: {e}")
            return None

    def load_full_metadata(self) -> Dict[str, Any]:
        """
        Load all metadata without filtering.

        Loads from:
        - CTags outline: ctags/ctags-{program_name}-outline.json
        - SuperBol CFG: superbol/superbol-cfg/{program_name}.json
        - SuperBol Symbols: superbol/superbol-{program_name}-doc-symbols.json
        - GnuCOBOL Analysis: gnucobol/gnucobol-{program_name}-analysis.json

        Returns:
            Dictionary with all metadata sources, or empty dicts for missing sources
        """
        if self._metadata_cache is not None:
            return self._metadata_cache

        metadata = {
            "ctags_outline": {},
            "superbol_cfg": {},
            "superbol_symbols": {},
            "gnucobol_analysis": {}
        }

        if not self.metadata_dir_exists:
            return metadata

        # Load CTags outline
        ctags_path = self.metadata_dir / "ctags" / f"ctags-{self.program_name}-outline.json"
        metadata["ctags_outline"] = self._load_json_file(ctags_path)

        # Load SuperBol CFG
        cfg_path = self.metadata_dir / "superbol" / "superbol-cfg" / f"{self.program_name}.json"
        metadata["superbol_cfg"] = self._load_json_file(cfg_path)

        # Load SuperBol Document Symbols
        symbols_path = self.metadata_dir / "superbol" / f"superbol-{self.program_name}-doc-symbols.json"
        metadata["superbol_symbols"] = self._load_json_file(symbols_path)

        # Load GnuCOBOL Analysis
        gnucobol_path = self.metadata_dir / "gnucobol" / f"gnucobol-{self.program_name}-analysis.json"
        metadata["gnucobol_analysis"] = self._load_json_file(gnucobol_path)

        # Cache the metadata
        self._metadata_cache = metadata

        return metadata

    def _load_json_file(self, file_path: Path) -> Dict[str, Any]:
        """
        Load a JSON file safely.

        Args:
            file_path: Path to the JSON file

        Returns:
            Parsed JSON as dictionary, or empty dict if file doesn't exist or is invalid
        """
        try:
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except json.JSONDecodeError as e:
            print(f"JSON decode error for {file_path}: {e}")
        except Exception as e:
            print(f"Error loading {file_path}: {e}")

        return {}

    def generate_enhanced_program_map(
        self,
        top_n_paragraphs: int = 30,
        top_n_data_items: int = 20
    ) -> str:
        """
        Generate an enhanced program map with configurable limits.

        Args:
            top_n_paragraphs: Number of top paragraphs to include (-1 for all)
            top_n_data_items: Number of top data items to include (-1 for all)

        Returns:
            Program map as a formatted string
        """
        # Ensure metadata is loaded
        metadata = self.load_full_metadata()

        if not PROGRAM_MAP_AVAILABLE:
            return self._generate_basic_program_map(metadata, top_n_paragraphs, top_n_data_items)

        # Use the existing program map generator with custom limits
        try:
            program_map = generate_cobol_program_map(
                ctags_outline=metadata.get("ctags_outline", {}),
                superbol_cfg=metadata.get("superbol_cfg", {}),
                gnucobol_analysis=metadata.get("gnucobol_analysis", {}),
                top_n_paragraphs=top_n_paragraphs if top_n_paragraphs >= 0 else 10000,
                top_n_data_items=top_n_data_items if top_n_data_items >= 0 else 10000
            )
            return program_map
        except Exception as e:
            print(f"Error generating program map: {e}")
            return self._generate_basic_program_map(metadata, top_n_paragraphs, top_n_data_items)

    def _generate_basic_program_map(
        self,
        metadata: Dict[str, Any],
        top_n_paragraphs: int,
        top_n_data_items: int
    ) -> str:
        """
        Generate a basic program map when the full generator is not available.

        Args:
            metadata: Loaded metadata dictionary
            top_n_paragraphs: Number of paragraphs to include
            top_n_data_items: Number of data items to include

        Returns:
            Basic program map string
        """
        lines = [f"# Program Map: {self.program_name}", ""]

        # Extract paragraphs from CTags
        ctags = metadata.get("ctags_outline", {})
        symbols = ctags.get("symbols", [])

        paragraphs = [s for s in symbols if s.get("kind") in ["paragraph", "section"]]
        data_items = [s for s in symbols if s.get("kind") == "data"]

        # Apply limits
        if top_n_paragraphs >= 0:
            paragraphs = paragraphs[:top_n_paragraphs]
        if top_n_data_items >= 0:
            data_items = data_items[:top_n_data_items]

        # Format paragraphs
        if paragraphs:
            lines.append("## Paragraphs")
            for p in paragraphs:
                lines.append(f"- {p.get('name', 'UNKNOWN')} (line {p.get('line', '?')})")
            lines.append("")

        # Format data items
        if data_items:
            lines.append("## Data Items")
            for d in data_items:
                lines.append(f"- {d.get('name', 'UNKNOWN')} (line {d.get('line', '?')})")
            lines.append("")

        return '\n'.join(lines)

    def build_full_context(
        self,
        top_n_paragraphs: int = 30,
        top_n_data_items: int = 20,
        include_line_numbers: bool = False
    ) -> Dict[str, Any]:
        """
        Build complete context combining source, metadata, and program map.

        Args:
            top_n_paragraphs: Number of top paragraphs for program map
            top_n_data_items: Number of top data items for program map
            include_line_numbers: Whether to include line numbers in source code

        Returns:
            Dictionary with keys:
            - source_code: Complete source code string
            - metadata: Dictionary of all metadata sources
            - program_map: Formatted program map string
        """
        source_code = self.load_full_source_code(include_line_numbers=include_line_numbers)
        metadata = self.load_full_metadata()
        program_map = self.generate_enhanced_program_map(
            top_n_paragraphs=top_n_paragraphs,
            top_n_data_items=top_n_data_items
        )

        return {
            "source_code": source_code or "",
            "metadata": metadata,
            "program_map": program_map
        }
