"""
Language Adapter Interface

Defines the abstract base class for language-specific adapters and normalized
data types used across all languages. The orchestrator (cobol_doc_agent.py)
calls adapter methods instead of directly importing language-specific modules.

Each language (COBOL, .NET/C#, Java, etc.) provides a concrete adapter that
implements this interface.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# =============================================================================
# Normalized Data Types
# =============================================================================

@dataclass
class SourceChunk:
    """Language-agnostic source code chunk."""
    chunk_number: int
    start_line: int
    end_line: int
    line_count: int
    content: str
    estimated_tokens: int


@dataclass
class ChunkVerification:
    """Result of chunk coverage verification."""
    valid: bool
    total_lines: int = 0
    chunks: int = 0
    coverage: str = ""
    error: str = ""
    reconstruction: Optional[Dict[str, Any]] = None
    method: str = ""


@dataclass
class StructuralBoundary:
    """
    A logical boundary in source code.

    Replaces the COBOL-specific 'paragraph boundary' concept with a
    language-agnostic representation. For COBOL this maps to paragraphs
    and sections; for C# it maps to methods, classes, namespaces, etc.
    """
    line_number: int
    name: str
    kind: str  # e.g. 'paragraph', 'section', 'method', 'class', 'namespace'
    parent: Optional[str] = None


@dataclass
class DependencyReference:
    """
    An external file dependency.

    Replaces the COBOL-specific 'copybook' concept. For COBOL this is a
    COPY statement; for C# it's a using/import; for Java an import, etc.
    """
    name: str
    reference_type: str  # e.g. 'copybook', 'using', 'import', 'include'
    file_path: Optional[str] = None
    content: Optional[str] = None


@dataclass
class ExternalCallReference:
    """
    An external program/method call.

    Replaces the COBOL-specific 'CALL' concept. For COBOL this is a CALL
    statement; for C# it's a method invocation on another class/service, etc.
    """
    caller: str
    target: str
    call_type: str  # e.g. 'call', 'invoke', 'rpc'
    file_path: Optional[str] = None


@dataclass
class MandatoryElement:
    """
    A required documentation element.

    Replaces COBOL-specific naming pattern matching (MAIN, ERROR, etc.)
    with a language-agnostic representation.
    """
    name: str
    line: int
    category: str  # e.g. 'entry_point', 'call_site', 'error_handler'


@dataclass
class NormalizedMetadata:
    """
    Container for normalized metadata with standardized keys.

    Each language adapter maps its tool-specific metadata into these
    standardized buckets so the orchestrator can work uniformly.
    """
    symbol_table: Dict[str, Any] = field(default_factory=dict)
    control_flow_graph: Dict[str, Any] = field(default_factory=dict)
    static_analysis: Dict[str, Any] = field(default_factory=dict)
    structural_outline: Dict[str, Any] = field(default_factory=dict)
    syntax_tree: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary with normalized keys."""
        return {
            'symbol_table': self.symbol_table,
            'control_flow_graph': self.control_flow_graph,
            'static_analysis': self.static_analysis,
            'structural_outline': self.structural_outline,
            'syntax_tree': self.syntax_tree,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'NormalizedMetadata':
        """Create from dictionary."""
        return cls(
            symbol_table=data.get('symbol_table', {}),
            control_flow_graph=data.get('control_flow_graph', {}),
            static_analysis=data.get('static_analysis', {}),
            structural_outline=data.get('structural_outline', {}),
        )


@dataclass
class SectionSourceRequirement:
    """
    What source code a documentation section needs.

    Replaces COBOL-specific division-to-section mapping with a
    language-agnostic representation.
    """
    extract_source: bool
    structural_scopes: List[str] = field(default_factory=list)
    # For COBOL: structural_scopes = ['DATA DIVISION', 'PROCEDURE DIVISION']
    # For C#: structural_scopes = ['Properties', 'Methods']


# =============================================================================
# Abstract Base Class
# =============================================================================

class LanguageAdapter(ABC):
    """
    Abstract base class for language-specific adapters.

    Each language (COBOL, .NET/C#, Java, PL/SQL) implements this interface
    to provide language-specific behavior to the orchestrator. The orchestrator
    calls adapter methods instead of directly importing language-specific modules.

    Methods are grouped by responsibility:
    - Identity & Config
    - File Discovery
    - Source Chunking
    - Source Extraction
    - Multi-File Resolution
    - Metadata
    - Mandatory Elements
    - Program Map & Prompts
    """

    # =========================================================================
    # Identity & Config
    # =========================================================================

    @property
    @abstractmethod
    def language_id(self) -> str:
        """
        Unique identifier for this language.

        Returns:
            Language ID string, e.g. 'cobol', 'dotnet', 'java'
        """
        ...

    @property
    @abstractmethod
    def display_name(self) -> str:
        """
        Human-readable display name.

        Returns:
            Display name, e.g. 'COBOL', '.NET/C#', 'Java'
        """
        ...

    @property
    @abstractmethod
    def file_extensions(self) -> List[str]:
        """
        File extensions handled by this adapter.

        Returns:
            List of extensions including dot, e.g. ['.cbl', '.COB', '.c74']
        """
        ...

    @property
    @abstractmethod
    def template_path(self) -> Path:
        """
        Path to the language-specific documentation template YAML.

        Returns:
            Path to the template file
        """
        ...

    @property
    @abstractmethod
    def code_block_language(self) -> str:
        """
        Language identifier for markdown code fences.

        Returns:
            Language string for ```lang blocks, e.g. 'cobol', 'csharp'
        """
        ...

    # =========================================================================
    # File Discovery
    # =========================================================================

    @abstractmethod
    def discover_source_files(
        self,
        workspace_path: str,
        filter_config: Optional[Dict[str, Any]] = None
    ) -> List[Path]:
        """
        Discover source files in the workspace matching this language.

        Args:
            workspace_path: Root directory to search
            filter_config: Optional filter configuration with keys:
                - extensions_include: List of extensions to include
                - extensions_exclude: List of extensions to exclude
                - exclude_files: List of file patterns to exclude
                - include_files: List of file patterns to include (overrides all)

        Returns:
            List of discovered source file paths
        """
        ...

    @abstractmethod
    def get_program_name(self, file_path: str) -> str:
        """
        Derive a program name from a source file path.

        For COBOL: stem of filename (e.g., 'MAINPROG.cbl' -> 'MAINPROG')
        For C#: could be class name, namespace, etc.

        Args:
            file_path: Path to source file

        Returns:
            Program/module name string
        """
        ...

    # =========================================================================
    # Source Chunking
    # =========================================================================

    @abstractmethod
    def find_structural_boundaries(
        self,
        lines: List[str],
        metadata: Optional[Dict[str, Any]] = None
    ) -> List[StructuralBoundary]:
        """
        Find logical boundaries in source code for chunking.

        For COBOL: paragraph and section boundaries.
        For C#: class, method, property boundaries.

        Args:
            lines: Source code lines
            metadata: Optional metadata for more accurate boundary detection

        Returns:
            List of structural boundaries sorted by line number
        """
        ...

    def chunk_source_file(
        self,
        file_path: str,
        max_tokens_per_chunk: int = 100000,
        metadata: Optional[Dict[str, Any]] = None,
        program_map: Optional[str] = None,
        query_code_results: Optional[Dict[str, Any]] = None,
        chunking_config: Optional[Dict[str, Any]] = None,
    ) -> Tuple[List[SourceChunk], ChunkVerification]:
        """
        Split a source file into chunks for LLM processing.

        If query_code_results are provided and strategy is 'query_code',
        uses tree-sitter declaration boundaries for precise splitting.
        Otherwise falls back to the adapter-specific legacy implementation.

        Args:
            file_path: Path to source file
            max_tokens_per_chunk: Maximum tokens per chunk
            metadata: Optional metadata for boundary detection
            program_map: Optional program map (used to calculate overhead)
            query_code_results: Optional query_code MCP tool results
            chunking_config: Optional chunking configuration from YAML

        Returns:
            Tuple of (list of chunks, verification result)
        """
        chunking_config = chunking_config or {}
        strategy = chunking_config.get('strategy', 'ctags')

        # Try tree-sitter based strategies if configured and results available
        if strategy in ('query_code', 'tsg_graph') and query_code_results:
            from structural_chunker import (
                build_declaration_map, build_declaration_map_from_graph,
                chunk_at_declaration_boundaries,
            )
            from tokenizer import estimate_tokens

            # Auto-detect format: graph output is a list of nodes with "attrs"
            # or wrapped as {"success": true, "graph": [...]}
            is_graph = (
                (isinstance(query_code_results, list) and query_code_results
                 and 'attrs' in query_code_results[0])
                or (isinstance(query_code_results, dict)
                    and 'graph' in query_code_results)
            )

            if is_graph:
                decl_map = build_declaration_map_from_graph(query_code_results)
                strategy_label = 'tsg_graph'
            else:
                decl_map = build_declaration_map(query_code_results)
                strategy_label = 'query_code'

            if decl_map:
                content = Path(file_path).read_text(encoding='utf-8', errors='replace')
                lines = content.splitlines(keepends=True)

                overhead = 0
                if program_map:
                    overhead = estimate_tokens(program_map, model="gpt-4") + 200

                print(f"  → Using {strategy_label} strategy ({len(decl_map.containers)} containers, "
                      f"{sum(len(c.members) for c in decl_map.containers)} members)")

                chunks, verification = chunk_at_declaration_boundaries(
                    lines, decl_map, max_tokens_per_chunk, overhead
                )
                # Attach declaration_map for structural context generation later
                verification.declaration_map = decl_map
                return chunks, verification
            else:
                print(f"  ⚠ {strategy_label} results could not be parsed — falling back to {chunking_config.get('fallback_strategy', 'ctags')}")

        # Fallback to legacy adapter-specific implementation
        return self._chunk_source_file_legacy(
            file_path, max_tokens_per_chunk, metadata, program_map
        )

    @abstractmethod
    def _chunk_source_file_legacy(
        self,
        file_path: str,
        max_tokens_per_chunk: int = 100000,
        metadata: Optional[Dict[str, Any]] = None,
        program_map: Optional[str] = None
    ) -> Tuple[List[SourceChunk], ChunkVerification]:
        """
        Legacy chunking implementation (ctags/regex based).

        Each adapter implements this with its language-specific logic.
        Called as fallback when query_code results are unavailable.
        """
        ...

    @abstractmethod
    def format_chunk_for_llm(
        self,
        chunk: SourceChunk,
        total_chunks: int,
        file_name: str,
        program_map: Optional[str] = None,
        model: str = "gpt-4",
        structural_context: Optional[List[str]] = None,
    ) -> str:
        """
        Format a chunk with metadata headers for LLM processing.

        Args:
            chunk: Source chunk to format
            total_chunks: Total number of chunks in the file
            file_name: Name of the source file
            program_map: Optional program map for whole-file context
            model: Model name for token estimation
            structural_context: Optional list of structural context strings
                (e.g., "**Continues**: class LinePitch — 9 of 43 members")

        Returns:
            Formatted string with metadata + content ready for LLM
        """
        ...

    # =========================================================================
    # Source Extraction
    # =========================================================================

    @abstractmethod
    def extract_structural_scope(
        self,
        file_path: str,
        scope_name: str
    ) -> Optional[str]:
        """
        Extract source code for a named structural scope.

        For COBOL: extract a division (e.g., 'DATA DIVISION')
        For C#: extract a class, namespace, or method

        Args:
            file_path: Path to source file
            scope_name: Name of the scope to extract

        Returns:
            Extracted source code, or None if scope not found
        """
        ...

    @abstractmethod
    def compress_source(self, source: str) -> str:
        """
        Compress source code by removing comments and blank lines.

        Args:
            source: Source code string

        Returns:
            Compressed source code
        """
        ...

    @abstractmethod
    def get_section_source_requirements(self) -> Dict[str, SectionSourceRequirement]:
        """
        Get source extraction requirements for each documentation section.

        Returns:
            Dictionary mapping section IDs to their source requirements
        """
        ...

    # =========================================================================
    # Multi-File Resolution
    # =========================================================================

    @abstractmethod
    def parse_dependency_references(
        self,
        file_path: str
    ) -> List[DependencyReference]:
        """
        Parse external file dependencies from source code.

        For COBOL: COPY statements
        For C#: using directives
        For Java: import statements

        Args:
            file_path: Path to source file

        Returns:
            List of dependency references found
        """
        ...

    @abstractmethod
    def resolve_dependency(
        self,
        ref: DependencyReference,
        search_paths: List[str]
    ) -> DependencyReference:
        """
        Resolve a dependency reference to its actual file.

        Args:
            ref: Dependency reference to resolve
            search_paths: Directories to search in

        Returns:
            Updated DependencyReference with file_path and content populated
        """
        ...

    @abstractmethod
    def parse_external_calls(
        self,
        file_path: str
    ) -> List[ExternalCallReference]:
        """
        Parse external program/service calls from source code.

        For COBOL: CALL statements
        For C#: method invocations on external classes/services

        Args:
            file_path: Path to source file

        Returns:
            List of external call references found
        """
        ...

    @abstractmethod
    def resolve_external_call(
        self,
        call_ref: ExternalCallReference,
        search_paths: List[str]
    ) -> ExternalCallReference:
        """
        Resolve an external call to its target file.

        Args:
            call_ref: External call reference to resolve
            search_paths: Directories to search in

        Returns:
            Updated ExternalCallReference with file_path populated
        """
        ...

    @abstractmethod
    def build_call_hierarchy(
        self,
        file_path: str,
        search_paths: List[str],
        depth: int = 1
    ) -> Dict[str, Any]:
        """
        Build a call hierarchy tree for the given source file.

        Args:
            file_path: Path to source file
            search_paths: Directories to search for called programs
            depth: Maximum depth to traverse

        Returns:
            Hierarchical dictionary of call relationships
        """
        ...

    # =========================================================================
    # Metadata
    # =========================================================================

    @abstractmethod
    def get_metadata_file_patterns(
        self,
        program_name: str
    ) -> Dict[str, List[str]]:
        """
        Get file patterns for loading metadata files.

        Returns a dictionary mapping normalized metadata keys to lists of
        file path patterns to search for.

        For COBOL:
            {'structural_outline': ['ctags/{name}.json', 'ctags/{name}.*.json'],
             'control_flow_graph': ['superbol/{name}.json'],
             'symbol_table': ['superbol/{name}.json'],
             'static_analysis': ['gnucobol/{name}.json']}

        Args:
            program_name: Name of the program

        Returns:
            Dictionary mapping metadata keys to file patterns
        """
        ...

    @abstractmethod
    def normalize_metadata(
        self,
        raw_metadata: Dict[str, Any]
    ) -> NormalizedMetadata:
        """
        Normalize tool-specific metadata into the standard 4-key structure.

        For COBOL:
            ctags_outline    -> structural_outline
            superbol_cfg     -> control_flow_graph
            superbol_symbols -> symbol_table
            gnucobol_analysis -> static_analysis

        Args:
            raw_metadata: Raw metadata dictionary with tool-specific keys

        Returns:
            NormalizedMetadata with standardized keys
        """
        ...

    # =========================================================================
    # Mandatory Elements
    # =========================================================================

    @abstractmethod
    def get_entry_point_patterns(self) -> List[str]:
        """
        Get patterns identifying entry point symbols.

        For COBOL: ['MAIN', 'START', 'INIT', 'BEGIN', 'ENTRY', '0000-']
        For C#: ['Main', 'Startup', 'Configure']

        Returns:
            List of pattern strings
        """
        ...

    @abstractmethod
    def get_error_handler_patterns(self) -> List[str]:
        """
        Get patterns identifying error handling symbols.

        For COBOL: ['ERROR', 'ERR', 'EXCEPTION', 'ABEND']
        For C#: ['Catch', 'HandleError', 'OnException']

        Returns:
            List of pattern strings
        """
        ...

    @abstractmethod
    def identify_mandatory_elements(
        self,
        metadata: Dict[str, Any]
    ) -> Dict[str, List[MandatoryElement]]:
        """
        Identify mandatory documentation elements from metadata.

        Returns elements grouped by category (entry_points, call_sites,
        error_handlers).

        Args:
            metadata: Program metadata dictionary

        Returns:
            Dictionary mapping categories to lists of mandatory elements
        """
        ...

    # =========================================================================
    # AST Filtering
    # =========================================================================

    def filter_ast_for_chunk(
        self,
        syntax_tree: Dict[str, Any],
        start_line: int,
        end_line: int
    ) -> Dict[str, Any]:
        """
        Filter a syntax tree to only include nodes overlapping a line range.

        This provides chunk-level AST context so the LLM understands the
        structural role of the code in the current chunk. The default
        implementation walks the tree generically, looking for 'line',
        'startLine', 'start_line', 'end_line', or 'endLine' keys on nodes.

        Language adapters can override this for more precise filtering.

        Args:
            syntax_tree: Full program syntax tree (dict from JSON)
            start_line: First line of the chunk (1-based)
            end_line: Last line of the chunk (1-based)

        Returns:
            Filtered syntax tree containing only overlapping nodes
        """
        if not syntax_tree:
            return {}

        # Handle tree-sitter MCP wrapper: {"success": true, "ast": {...}, ...}
        # The actual tree is nested under "ast" key — unwrap before filtering
        tree_to_filter = syntax_tree
        is_wrapped = False
        if 'ast' in syntax_tree and isinstance(syntax_tree.get('ast'), dict):
            tree_to_filter = syntax_tree['ast']
            is_wrapped = True

        filtered = self._filter_ast_nodes(tree_to_filter, start_line, end_line)

        # Re-wrap if the input was wrapped
        if is_wrapped and filtered:
            result = {k: v for k, v in syntax_tree.items() if k != 'ast'}
            result['ast'] = filtered
            # Update node_count to reflect the filtered tree, not the full file
            if 'node_count' in result:
                result['node_count'] = self._count_ast_nodes(filtered)
            return result

        return filtered if filtered else {}

    @staticmethod
    def _count_ast_nodes(node: Any) -> int:
        """Count nodes in a filtered AST tree."""
        if isinstance(node, dict):
            count = 1
            for v in node.values():
                if isinstance(v, list):
                    count += sum(LanguageAdapter._count_ast_nodes(item) for item in v)
            return count
        return 0

    def _filter_ast_nodes(
        self,
        node: Any,
        start_line: int,
        end_line: int
    ) -> Any:
        """
        Recursively filter AST nodes by line range.

        Keeps a node if its line range overlaps [start_line, end_line].
        For container nodes (dicts with children), keeps the container
        if any child overlaps, pruning non-overlapping children.

        Works with common AST JSON conventions:
        - 'line' / 'startLine' / 'start_line' for node start
        - 'endLine' / 'end_line' for node end
        - 'start_point.row' / 'end_point.row' (tree-sitter format, 0-based)
        - 'children' / 'members' / 'body' / 'statements' for child arrays
        """
        if isinstance(node, dict):
            # Detect line range for this node
            node_start = (
                node.get('startLine')
                or node.get('start_line')
                or node.get('line')
            )
            node_end = (
                node.get('endLine')
                or node.get('end_line')
                or node_start  # single-line node
            )

            # Tree-sitter format: start_point.row / end_point.row (0-based)
            if node_start is None and 'start_point' in node:
                sp = node['start_point']
                ep = node.get('end_point', sp)
                if isinstance(sp, dict) and 'row' in sp:
                    node_start = sp['row'] + 1  # Convert 0-based to 1-based
                    node_end = (ep['row'] + 1) if isinstance(ep, dict) and 'row' in ep else node_start

            # If node has line info, check overlap
            if node_start is not None:
                node_start = int(node_start)
                node_end = int(node_end) if node_end is not None else node_start
                if node_end < start_line or node_start > end_line:
                    return None  # No overlap

            # Recurse into child collections
            child_keys = ['children', 'members', 'body', 'statements',
                          'methods', 'properties', 'fields', 'classes',
                          'namespaces', 'functions', 'parameters',
                          'paragraphs', 'sections', 'divisions']
            filtered = {}
            for key, value in node.items():
                if key in child_keys and isinstance(value, list):
                    filtered_children = [
                        c for c in (self._filter_ast_nodes(item, start_line, end_line)
                                    for item in value)
                        if c is not None
                    ]
                    if filtered_children:
                        filtered[key] = filtered_children
                else:
                    filtered[key] = value

            # If this node had line info and matched, keep it
            if node_start is not None:
                return filtered
            # If no line info (root/container), keep only if it has surviving children
            has_children = any(
                key in filtered and filtered[key]
                for key in child_keys
            )
            if has_children or node_start is not None:
                return filtered
            # Keep non-collection nodes (metadata, name, etc.) as-is
            return filtered if filtered else None

        elif isinstance(node, list):
            result = [
                c for c in (self._filter_ast_nodes(item, start_line, end_line)
                            for item in node)
                if c is not None
            ]
            return result if result else None

        # Scalars pass through
        return node

    # =========================================================================
    # Program Map & Prompts
    # =========================================================================

    @abstractmethod
    def generate_program_map(
        self,
        program_name: str,
        metadata: Dict[str, Any],
        token_budget: int = 5000
    ) -> str:
        """
        Generate a hierarchical program map for LLM context.

        The program map provides a compact overview of the program structure,
        ranked by importance, to give the LLM context without sending the
        full source code.

        Args:
            program_name: Name of the program
            metadata: Program metadata
            token_budget: Approximate token budget for the map

        Returns:
            Formatted program map string
        """
        ...

    @abstractmethod
    def get_language_context_for_prompt(self) -> str:
        """
        Get language-specific context to inject into LLM prompts.

        This provides the LLM with language-specific knowledge, terminology,
        and conventions to use when generating documentation.

        Returns:
            Context string to include in prompts
        """
        ...

    @abstractmethod
    def build_full_context_prompt(
        self,
        section_id: str,
        source_code: str,
        metadata: Dict[str, Any],
        program_map: str,
        instruction: str,
        program_name: str = ""
    ) -> str:
        """
        Build a full-context prompt for a documentation section.

        Args:
            section_id: Section identifier (e.g., 'executive-summary')
            source_code: Complete source code
            metadata: All metadata
            program_map: Formatted program map
            instruction: Section-specific instruction from template
            program_name: Name of the program

        Returns:
            Complete prompt string ready for LLM
        """
        ...

    @abstractmethod
    def build_full_context(
        self,
        program_name: str,
        source_file_path: str,
        metadata_dir: str,
        include_line_numbers: bool = False,
        include_program_map: bool = True
    ) -> Dict[str, Any]:
        """
        Build complete context dictionary for LLM calls.

        Assembles source code, metadata, and program map into a single
        context dictionary.

        Args:
            program_name: Name of the program
            source_file_path: Path to source file
            metadata_dir: Path to metadata directory
            include_line_numbers: Whether to add line numbers to source
            include_program_map: Whether to include program map

        Returns:
            Dictionary with keys: 'source_code', 'metadata', 'program_map'
        """
        ...
