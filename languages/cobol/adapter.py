"""
COBOL Language Adapter

Concrete implementation of LanguageAdapter for COBOL programs.
Delegates to existing modules (source_chunker, source_extractor,
source_integration, section_requirements, multi_file_resolver,
mandatory_elements, cobol_program_map, full_context_builder,
full_context_prompts) without changing their behavior.
"""

import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from language_adapter import (
    ChunkVerification,
    DependencyReference,
    ExternalCallReference,
    LanguageAdapter,
    MandatoryElement,
    NormalizedMetadata,
    SectionSourceRequirement,
    SourceChunk,
    StructuralBoundary,
)


class CobolAdapter(LanguageAdapter):
    """
    COBOL language adapter.

    Delegates to existing COBOL-specific modules. This is a thin wrapper
    that translates between the normalized adapter interface and the
    existing module APIs.
    """

    # All supported COBOL file extensions
    _EXTENSIONS = [
        '.cbl', '.cob', '.CBL', '.COB',
        '.c74', '.C74',
        '.XMOD', '.xmod', '.XLIB', '.xlib',
        '.xgn', '.XGN',
    ]

    # =========================================================================
    # Identity & Config
    # =========================================================================

    @property
    def language_id(self) -> str:
        return 'cobol'

    @property
    def display_name(self) -> str:
        return 'COBOL'

    @property
    def file_extensions(self) -> List[str]:
        return list(self._EXTENSIONS)

    @property
    def template_path(self) -> Path:
        # Currently at the repo root; will move to languages/cobol/ in Phase D
        return Path(__file__).resolve().parent.parent.parent / 'cobol-doc-template.yaml'

    @property
    def code_block_language(self) -> str:
        return 'cobol'

    # =========================================================================
    # File Discovery
    # =========================================================================

    def discover_source_files(
        self,
        workspace_path: str,
        filter_config: Optional[Dict[str, Any]] = None
    ) -> List[Path]:
        """Discover COBOL source files in the workspace."""
        ws = Path(workspace_path)
        if not ws.exists():
            return []

        filter_config = filter_config or {}
        include_files = filter_config.get('include_files', [])
        exclude_files = filter_config.get('exclude_files', [])
        extensions_include = filter_config.get('extensions_include', [])
        extensions_exclude = filter_config.get('extensions_exclude', [])

        # Determine which extensions to use
        if extensions_include:
            # Normalize to include dot prefix
            exts = set()
            for e in extensions_include:
                exts.add(e if e.startswith('.') else f'.{e}')
        else:
            exts = set(self._EXTENSIONS)

        # Remove excluded extensions
        if extensions_exclude:
            for e in extensions_exclude:
                normalized = e if e.startswith('.') else f'.{e}'
                exts.discard(normalized)

        # Collect all matching files
        found: List[Path] = []
        for f in ws.iterdir():
            if not f.is_file():
                continue
            if f.suffix not in exts:
                continue

            # Apply include_files filter (if set, ONLY these)
            if include_files:
                if not any(self._matches_pattern(f.name, pat) for pat in include_files):
                    continue

            # Apply exclude_files filter
            if exclude_files:
                if any(self._matches_pattern(f.name, pat) for pat in exclude_files):
                    continue

            found.append(f)

        return sorted(found)

    def get_program_name(self, file_path: str) -> str:
        """Derive program name from COBOL source file path (stem of filename)."""
        return Path(file_path).stem

    @staticmethod
    def _matches_pattern(filename: str, pattern: str) -> bool:
        """Check if filename matches a glob-like pattern (*, ? wildcards)."""
        # Convert glob pattern to regex
        regex = pattern.replace('.', r'\.').replace('*', '.*').replace('?', '.')
        return bool(re.match(f'^{regex}$', filename, re.IGNORECASE))

    # =========================================================================
    # Source Chunking
    # =========================================================================

    def find_structural_boundaries(
        self,
        lines: List[str],
        metadata: Optional[Dict[str, Any]] = None
    ) -> List[StructuralBoundary]:
        """Find paragraph/section boundaries in COBOL source."""
        from source_chunker import find_paragraph_boundaries

        boundary_lines = find_paragraph_boundaries(lines, metadata)

        boundaries = []
        for line_num in boundary_lines:
            if 0 <= line_num < len(lines):
                line_text = lines[line_num].strip().upper()
                # Determine kind based on content
                if line_text.endswith(' DIVISION.'):
                    kind = 'division'
                    name = line_text.rstrip('.')
                elif line_text.endswith(' SECTION.'):
                    kind = 'section'
                    name = line_text.rstrip('.')
                else:
                    kind = 'paragraph'
                    name = line_text.rstrip('.')
                boundaries.append(StructuralBoundary(
                    line_number=line_num,
                    name=name,
                    kind=kind,
                ))

        return boundaries

    def _chunk_source_file_legacy(
        self,
        file_path: str,
        max_tokens_per_chunk: int = 100000,
        metadata: Optional[Dict[str, Any]] = None,
        program_map: Optional[str] = None
    ) -> Tuple[List[SourceChunk], ChunkVerification]:
        """Chunk a COBOL source file at paragraph/section boundaries (legacy)."""
        from source_chunker import chunk_large_cobol_file

        raw_chunks, raw_verification = chunk_large_cobol_file(
            file_path=file_path,
            max_tokens_per_chunk=max_tokens_per_chunk,
            ctags_metadata=metadata,
            program_map=program_map,
        )

        # Convert raw dicts to normalized types
        chunks = [
            SourceChunk(
                chunk_number=c['chunk_number'],
                start_line=c['start_line'],
                end_line=c['end_line'],
                line_count=c['line_count'],
                content=c['content'],
                estimated_tokens=c['estimated_tokens'],
            )
            for c in raw_chunks
        ]

        verification = ChunkVerification(
            valid=raw_verification.get('valid', False),
            total_lines=raw_verification.get('total_lines', 0),
            chunks=raw_verification.get('chunks', 0),
            coverage=raw_verification.get('coverage', ''),
            error=raw_verification.get('error', ''),
            reconstruction=raw_verification.get('reconstruction'),
            method=raw_verification.get('method', ''),
        )

        return chunks, verification

    def format_chunk_for_llm(
        self,
        chunk: SourceChunk,
        total_chunks: int,
        file_name: str,
        program_map: Optional[str] = None,
        model: str = "gpt-4",
        structural_context: Optional[List[str]] = None,
    ) -> str:
        """Format a COBOL chunk with metadata headers for LLM processing."""
        from source_chunker import format_chunk_for_llm as _format_chunk

        # Convert SourceChunk back to dict for the existing API
        chunk_dict = {
            'chunk_number': chunk.chunk_number,
            'start_line': chunk.start_line,
            'end_line': chunk.end_line,
            'line_count': chunk.line_count,
            'content': chunk.content,
            'estimated_tokens': chunk.estimated_tokens,
        }

        formatted = _format_chunk(
            chunk=chunk_dict,
            total_chunks=total_chunks,
            file_name=file_name,
            program_map=program_map,
            model=model,
        )

        # Inject structural context after the header if provided
        if structural_context:
            ctx_block = "\n### Structural Context\n"
            for ctx_line in structural_context:
                ctx_block += f"- {ctx_line}\n"
            ctx_block += "\n"
            # Insert after the header separator line
            separator = "=" * 77
            parts = formatted.split(separator, 2)
            if len(parts) >= 3:
                # Insert after the second separator (after "Lines: X to Y" header)
                formatted = separator.join(parts[:2]) + separator + ctx_block + parts[2]

        return formatted

    # =========================================================================
    # Source Extraction
    # =========================================================================

    def extract_structural_scope(
        self,
        file_path: str,
        scope_name: str
    ) -> Optional[str]:
        """Extract a COBOL division by name."""
        from source_extractor import extract_division
        return extract_division(file_path, scope_name)

    def compress_source(self, source: str) -> str:
        """Compress COBOL source by removing comments and blank lines."""
        from source_extractor import compress_source_code
        return compress_source_code(source)

    def get_section_source_requirements(self) -> Dict[str, SectionSourceRequirement]:
        """Get COBOL section-to-division mapping for source extraction."""
        from section_requirements import SECTION_REQUIREMENTS

        result = {}
        for section_id, req in SECTION_REQUIREMENTS.items():
            result[section_id] = SectionSourceRequirement(
                extract_source=req['extract_source'],
                structural_scopes=list(req['divisions']),
            )
        return result

    # =========================================================================
    # Multi-File Resolution
    # =========================================================================

    def parse_dependency_references(
        self,
        file_path: str
    ) -> List[DependencyReference]:
        """Parse COPY statements from a COBOL source file."""
        try:
            from multi_file_resolver import CopybookResolver
        except ImportError:
            return []

        resolver = CopybookResolver(str(Path(file_path).parent))
        copybook_names = resolver.parse_copy_statements(file_path)

        return [
            DependencyReference(
                name=name,
                reference_type='copybook',
            )
            for name in copybook_names
        ]

    def resolve_dependency(
        self,
        ref: DependencyReference,
        search_paths: List[str]
    ) -> DependencyReference:
        """Resolve a COBOL copybook reference to its file."""
        try:
            from multi_file_resolver import CopybookResolver
        except ImportError:
            return ref

        if not search_paths:
            return ref

        resolver = CopybookResolver(search_paths[0], search_paths[1:])
        found_path = resolver.find_copybook(ref.name)

        if found_path:
            content = resolver.extract_copybook_content(found_path)
            return DependencyReference(
                name=ref.name,
                reference_type=ref.reference_type,
                file_path=found_path,
                content=content,
            )

        return ref

    def parse_external_calls(
        self,
        file_path: str
    ) -> List[ExternalCallReference]:
        """Parse CALL statements from a COBOL source file."""
        try:
            from multi_file_resolver import CalledProgramResolver
        except ImportError:
            return []

        resolver = CalledProgramResolver(str(Path(file_path).parent))
        program_names = resolver.parse_call_statements(file_path)

        return [
            ExternalCallReference(
                caller=Path(file_path).stem,
                target=name,
                call_type='call',
            )
            for name in program_names
        ]

    def resolve_external_call(
        self,
        call_ref: ExternalCallReference,
        search_paths: List[str]
    ) -> ExternalCallReference:
        """Resolve a COBOL CALL reference to its target file."""
        try:
            from multi_file_resolver import CalledProgramResolver
        except ImportError:
            return call_ref

        if not search_paths:
            return call_ref

        resolver = CalledProgramResolver(search_paths[0], search_paths[1:])
        found_path = resolver.find_called_program(call_ref.target)

        if found_path:
            return ExternalCallReference(
                caller=call_ref.caller,
                target=call_ref.target,
                call_type=call_ref.call_type,
                file_path=found_path,
            )

        return call_ref

    def build_call_hierarchy(
        self,
        file_path: str,
        search_paths: List[str],
        depth: int = 1
    ) -> Dict[str, Any]:
        """Build a CALL hierarchy tree for the given COBOL source file."""
        try:
            from multi_file_resolver import CalledProgramResolver
        except ImportError:
            return {}

        if not search_paths:
            search_paths = [str(Path(file_path).parent)]

        resolver = CalledProgramResolver(search_paths[0], search_paths[1:])
        return resolver.build_call_hierarchy(file_path, depth=depth)

    # =========================================================================
    # Metadata
    # =========================================================================

    def get_metadata_file_patterns(
        self,
        program_name: str
    ) -> Dict[str, List[str]]:
        """Get COBOL metadata file patterns mapped to normalized keys."""
        return {
            'structural_outline': [
                f'ctags/ctags-{program_name}-outline.json',
            ],
            'control_flow_graph': [
                f'superbol/superbol-cfg/{program_name}.json',
            ],
            'symbol_table': [
                f'superbol/superbol-{program_name}-doc-symbols.json',
            ],
            'static_analysis': [
                f'gnucobol/gnucobol-{program_name}-analysis.json',
            ],
        }

    def normalize_metadata(
        self,
        raw_metadata: Dict[str, Any]
    ) -> NormalizedMetadata:
        """
        Normalize COBOL metadata keys to the standard 4-key structure.

        Maps:
            ctags_outline    -> structural_outline
            superbol_cfg     -> control_flow_graph
            superbol_symbols -> symbol_table
            gnucobol_analysis -> static_analysis
        """
        return NormalizedMetadata(
            structural_outline=raw_metadata.get('ctags_outline', {}),
            control_flow_graph=raw_metadata.get('superbol_cfg', {}),
            symbol_table=raw_metadata.get('superbol_symbols', {}),
            static_analysis=raw_metadata.get('gnucobol_analysis', {}),
        )

    # =========================================================================
    # Mandatory Elements
    # =========================================================================

    def get_entry_point_patterns(self) -> List[str]:
        """Get COBOL entry point patterns."""
        from mandatory_elements import DEFAULT_ENTRY_POINT_PATTERNS
        return list(DEFAULT_ENTRY_POINT_PATTERNS)

    def get_error_handler_patterns(self) -> List[str]:
        """Get COBOL error handler patterns."""
        from mandatory_elements import DEFAULT_ERROR_HANDLER_PATTERNS
        return list(DEFAULT_ERROR_HANDLER_PATTERNS)

    def identify_mandatory_elements(
        self,
        metadata: Dict[str, Any]
    ) -> Dict[str, List[MandatoryElement]]:
        """Identify COBOL mandatory elements from metadata."""
        from mandatory_elements import get_mandatory_elements

        raw = get_mandatory_elements(metadata)

        result: Dict[str, List[MandatoryElement]] = {}
        for category, elements in raw.items():
            result[category] = [
                MandatoryElement(
                    name=elem['name'],
                    line=elem.get('line', 0),
                    category=elem.get('category', category),
                )
                for elem in elements
            ]

        return result

    # =========================================================================
    # Program Map & Prompts
    # =========================================================================

    def generate_program_map(
        self,
        program_name: str,
        metadata: Dict[str, Any],
        token_budget: int = 5000
    ) -> str:
        """Generate a COBOL program map."""
        from cobol_program_map import generate_cobol_program_map

        return generate_cobol_program_map(
            program_name=program_name,
            metadata=metadata,
            token_budget=token_budget,
        )

    def get_language_context_for_prompt(self) -> str:
        """Get COBOL-specific context for LLM prompts."""
        return (
            "This is a COBOL program. COBOL is a procedural language with "
            "four divisions: IDENTIFICATION, ENVIRONMENT, DATA, and PROCEDURE. "
            "Programs are organized into sections and paragraphs. "
            "Data items are defined in the DATA DIVISION with level numbers "
            "(01-49, 66, 77, 88). The PROCEDURE DIVISION contains executable code "
            "using PERFORM for flow control and CALL for external program invocation. "
            "COPY statements include copybooks (shared data definitions). "
            "Use COBOL terminology: paragraph, section, division, copybook, "
            "level number, PIC clause, PERFORM, CALL, WORKING-STORAGE, etc."
        )

    def build_full_context_prompt(
        self,
        section_id: str,
        source_code: str,
        metadata: Dict[str, Any],
        program_map: str,
        instruction: str,
        program_name: str = ""
    ) -> str:
        """Build a full-context COBOL prompt for a documentation section."""
        from full_context_prompts import build_full_context_prompt as _build_prompt

        return _build_prompt(
            section_id=section_id,
            source_code=source_code,
            metadata=metadata,
            program_map=program_map,
            instruction=instruction,
            program_name=program_name,
        )

    def build_full_context(
        self,
        program_name: str,
        source_file_path: str,
        metadata_dir: str,
        include_line_numbers: bool = False,
        include_program_map: bool = True
    ) -> Dict[str, Any]:
        """Build complete COBOL context dictionary for LLM calls."""
        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name=program_name,
            source_file_path=source_file_path,
            metadata_dir=metadata_dir,
        )

        return builder.build_full_context(
            include_line_numbers=include_line_numbers,
        )
