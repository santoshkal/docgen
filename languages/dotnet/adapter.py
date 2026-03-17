"""
.NET/C# Language Adapter

Concrete implementation of LanguageAdapter for .NET/C# programs.
Provides chunking via ctags metadata with regex-based fallback,
using directive parsing, and C#-appropriate program map generation.
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


# File patterns auto-excluded as generated/boilerplate
_AUTO_EXCLUDE_PATTERNS = [
    'AssemblyInfo.cs',
    '*.Designer.cs',
    '*.g.cs',
    '*.g.i.cs',
    'GlobalSuppressions.cs',
    'TemporaryGeneratedFile_*.cs',
]


class DotNetAdapter(LanguageAdapter):
    """
    .NET/C# language adapter.

    Provides C#-specific file discovery, structural boundary detection,
    chunking, using-directive parsing, and program map generation.
    """

    _EXTENSIONS = ['.cs']

    # =========================================================================
    # Identity & Config
    # =========================================================================

    @property
    def language_id(self) -> str:
        return 'dotnet'

    @property
    def display_name(self) -> str:
        return '.NET/C#'

    @property
    def file_extensions(self) -> List[str]:
        return list(self._EXTENSIONS)

    @property
    def template_path(self) -> Path:
        return Path(__file__).resolve().parent / 'template.yaml'

    @property
    def code_block_language(self) -> str:
        return 'csharp'

    # =========================================================================
    # File Discovery
    # =========================================================================

    def discover_source_files(
        self,
        workspace_path: str,
        filter_config: Optional[Dict[str, Any]] = None
    ) -> List[Path]:
        """Discover C# source files, recursively searching subdirectories."""
        ws = Path(workspace_path).expanduser()
        if not ws.exists():
            return []

        filter_config = filter_config or {}
        include_files = filter_config.get('include_files', [])
        exclude_files = filter_config.get('exclude_files', [])
        extensions_include = filter_config.get('extensions_include', [])

        # Determine extensions
        if extensions_include:
            exts = set()
            for e in extensions_include:
                exts.add(e if e.startswith('.') else f'.{e}')
        else:
            exts = set(self._EXTENSIONS)

        # Merge auto-exclude with user exclude
        all_exclude = list(_AUTO_EXCLUDE_PATTERNS) + list(exclude_files)

        found: List[Path] = []
        for f in ws.rglob('*'):
            if not f.is_file():
                continue
            if f.suffix not in exts:
                continue

            # include_files: if set, ONLY these
            if include_files:
                if not any(self._matches_pattern(f.name, pat) for pat in include_files):
                    continue

            # exclude patterns
            if any(self._matches_pattern(f.name, pat) for pat in all_exclude):
                continue

            found.append(f)

        return sorted(found)

    def get_program_name(self, file_path: str) -> str:
        """Derive program name from C# source file path (stem of filename)."""
        return Path(file_path).stem

    @staticmethod
    def _matches_pattern(filename: str, pattern: str) -> bool:
        """Check if filename matches a glob-like pattern (*, ? wildcards)."""
        regex = pattern.replace('.', r'\.').replace('*', '.*').replace('?', '.')
        return bool(re.match(f'^{regex}$', filename, re.IGNORECASE))

    # =========================================================================
    # Source Chunking
    # =========================================================================

    # Regex patterns for C# structural elements
    _RE_NAMESPACE = re.compile(
        r'^\s*(namespace)\s+[\w.]+', re.MULTILINE
    )
    _RE_TYPE_DECL = re.compile(
        r'^\s*(?:(?:public|private|protected|internal|static|abstract|sealed|partial)\s+)*'
        r'(class|struct|interface|enum|record)\s+\w+',
        re.MULTILINE,
    )
    _RE_METHOD = re.compile(
        r'^\s*(?:(?:public|private|protected|internal|static|virtual|override|abstract|async|new|sealed)\s+)*'
        r'(?:[\w<>\[\],\s]+?)\s+(\w+)\s*\(',
        re.MULTILINE,
    )

    def find_structural_boundaries(
        self,
        lines: List[str],
        metadata: Optional[Dict[str, Any]] = None
    ) -> List[StructuralBoundary]:
        """Find namespace/class/method boundaries in C# source."""
        boundaries: List[StructuralBoundary] = []

        # Strategy 1: Use ctags metadata if available
        if metadata:
            symbols = None
            if 'outline' in metadata and 'other' in metadata['outline']:
                symbols = metadata['outline']['other']
            elif 'symbols' in metadata:
                symbols = metadata['symbols']

            if symbols:
                kind_map = {
                    'namespace': 'namespace',
                    'class': 'class',
                    'struct': 'struct',
                    'interface': 'interface',
                    'enum': 'enum',
                    'method': 'method',
                    'property': 'property',
                    'function': 'method',
                    'member': 'method',
                }
                for symbol in symbols:
                    kind = symbol.get('kind', '')
                    mapped = kind_map.get(kind)
                    if mapped and 'line' in symbol:
                        line_num = symbol['line'] - 1  # 0-indexed
                        if 0 <= line_num < len(lines):
                            boundaries.append(StructuralBoundary(
                                line_number=line_num,
                                name=symbol.get('name', ''),
                                kind=mapped,
                                parent=symbol.get('scope', None),
                            ))
                if boundaries:
                    return sorted(boundaries, key=lambda b: b.line_number)

        # Strategy 2: Regex fallback
        full_text = ''.join(lines)
        # Track line offsets for character-to-line mapping
        line_offsets = []
        offset = 0
        for line in lines:
            line_offsets.append(offset)
            offset += len(line)

        def _char_to_line(pos: int) -> int:
            for i in range(len(line_offsets) - 1, -1, -1):
                if pos >= line_offsets[i]:
                    return i
            return 0

        seen_lines = set()

        for pattern, kind in [
            (self._RE_NAMESPACE, 'namespace'),
            (self._RE_TYPE_DECL, 'class'),
            (self._RE_METHOD, 'method'),
        ]:
            for m in pattern.finditer(full_text):
                ln = _char_to_line(m.start())
                if ln not in seen_lines:
                    seen_lines.add(ln)
                    name = lines[ln].strip().rstrip('{').strip()
                    # Truncate long names
                    if len(name) > 80:
                        name = name[:77] + '...'
                    boundaries.append(StructuralBoundary(
                        line_number=ln,
                        name=name,
                        kind=kind,
                    ))

        return sorted(boundaries, key=lambda b: b.line_number)

    def _chunk_source_file_legacy(
        self,
        file_path: str,
        max_tokens_per_chunk: int = 100000,
        metadata: Optional[Dict[str, Any]] = None,
        program_map: Optional[str] = None
    ) -> Tuple[List[SourceChunk], ChunkVerification]:
        """Split a C# source file into chunks at structural boundaries (ctags/regex fallback)."""
        from source_chunker import create_chunks_at_boundaries
        from tokenizer import estimate_tokens

        path = Path(file_path)
        if not path.exists():
            return [], ChunkVerification(valid=False, error=f"File not found: {file_path}")

        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        lines = content.splitlines(keepends=True)
        if not lines:
            return [], ChunkVerification(valid=False, error="Empty file")

        # Find boundaries
        struct_boundaries = self.find_structural_boundaries(lines, metadata)
        boundary_lines = sorted(set([0] + [b.line_number for b in struct_boundaries]))

        # Calculate overhead for program map
        overhead_tokens = 0
        if program_map:
            overhead_tokens = estimate_tokens(program_map, model="gpt-4") + 200

        # Use the shared chunker
        raw_chunks = create_chunks_at_boundaries(
            lines, boundary_lines, max_tokens_per_chunk, overhead_tokens
        )

        # Convert to SourceChunk
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

        # Build verification
        total_chunk_lines = sum(c.line_count for c in chunks)
        verification = ChunkVerification(
            valid=total_chunk_lines == len(lines),
            total_lines=len(lines),
            chunks=len(chunks),
            coverage=f"{total_chunk_lines}/{len(lines)}",
            method='structural_boundaries',
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
        """Format a C# chunk with metadata headers for LLM processing."""
        import hashlib
        from tokenizer import estimate_tokens

        chunk_hash = hashlib.sha256(chunk.content.encode('utf-8')).hexdigest()[:12]

        header = f"## Hash-ID: {chunk_hash} | Chunk {chunk.chunk_number}/{total_chunks}: {file_name}\n"
        header += f"Lines {chunk.start_line}\u2013{chunk.end_line} ({chunk.line_count} lines, ~{chunk.estimated_tokens} tokens)\n\n"

        if structural_context:
            header += "### Structural Context\n"
            for ctx_line in structural_context:
                header += f"- {ctx_line}\n"
            header += "\n"

        if program_map:
            header += "### Program Structure Map\n"
            header += program_map + "\n\n"

        header += f"### Source Code (lines {chunk.start_line}\u2013{chunk.end_line})\n\n"

        formatted = header + "```csharp\n" + chunk.content
        if not formatted.endswith('\n'):
            formatted += '\n'
        formatted += "```\n"

        return formatted

    # =========================================================================
    # Source Extraction
    # =========================================================================

    def extract_structural_scope(
        self,
        file_path: str,
        scope_name: str
    ) -> Optional[str]:
        """Extract a named scope (namespace, class, method) from C# source by brace matching."""
        path = Path(file_path)
        if not path.exists():
            return None

        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.readlines()

        scope_lower = scope_name.lower()
        # Find the line where the scope starts
        start_idx = None
        for i, line in enumerate(lines):
            if scope_lower in line.lower():
                start_idx = i
                break

        if start_idx is None:
            return None

        # Brace-match to find the end
        brace_depth = 0
        started = False
        result_lines = []
        for i in range(start_idx, len(lines)):
            result_lines.append(lines[i])
            for ch in lines[i]:
                if ch == '{':
                    brace_depth += 1
                    started = True
                elif ch == '}':
                    brace_depth -= 1
            if started and brace_depth <= 0:
                break

        return ''.join(result_lines) if result_lines else None

    def compress_source(self, source: str) -> str:
        """Compress C# source by removing comments and blank lines."""
        # Remove block comments
        result = re.sub(r'/\*.*?\*/', '', source, flags=re.DOTALL)
        # Remove line comments
        result = re.sub(r'//.*$', '', result, flags=re.MULTILINE)
        # Remove blank lines
        result = re.sub(r'\n\s*\n', '\n', result)
        return result.strip()

    def get_section_source_requirements(self) -> Dict[str, SectionSourceRequirement]:
        """Get C# section-to-scope mapping for source extraction."""
        return {
            'namespace-class-hierarchy': SectionSourceRequirement(
                extract_source=True,
                structural_scopes=['namespace'],
            ),
            'fields-properties': SectionSourceRequirement(
                extract_source=True,
                structural_scopes=['Properties', 'Fields'],
            ),
            'detailed-code-explanation': SectionSourceRequirement(
                extract_source=True,
                structural_scopes=['Methods', 'Classes'],
            ),
            'using-directives': SectionSourceRequirement(
                extract_source=False,
            ),
            'executive-summary': SectionSourceRequirement(
                extract_source=True,
                structural_scopes=['namespace', 'class'],
            ),
            'business-logic': SectionSourceRequirement(
                extract_source=True,
                structural_scopes=['Methods'],
            ),
        }

    # =========================================================================
    # Multi-File Resolution
    # =========================================================================

    def parse_dependency_references(
        self,
        file_path: str
    ) -> List[DependencyReference]:
        """Parse using directives from a C# source file."""
        path = Path(file_path)
        if not path.exists():
            return []

        refs: List[DependencyReference] = []
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                stripped = line.strip()
                # Stop at namespace/class declaration
                if re.match(r'^(namespace|class|public|internal|static)\s', stripped):
                    break
                m = re.match(r'^using\s+(static\s+)?([^;=]+);', stripped)
                if m:
                    ns = m.group(2).strip()
                    refs.append(DependencyReference(
                        name=ns,
                        reference_type='using',
                    ))
        return refs

    def resolve_dependency(
        self,
        ref: DependencyReference,
        search_paths: List[str]
    ) -> DependencyReference:
        """Resolve a using directive — for C# this is mostly a no-op (namespace-based)."""
        # Using directives reference namespaces, not files directly.
        # We could attempt to find matching .cs files but it's not 1:1.
        return ref

    def parse_external_calls(
        self,
        file_path: str
    ) -> List[ExternalCallReference]:
        """Parse new Xxx() and Xxx.Method() patterns from C# source."""
        path = Path(file_path)
        if not path.exists():
            return []

        caller = path.stem
        refs: List[ExternalCallReference] = []
        seen = set()

        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

        # Match `new ClassName(`
        for m in re.finditer(r'\bnew\s+([A-Z]\w+)\s*\(', content):
            target = m.group(1)
            if target not in seen:
                seen.add(target)
                refs.append(ExternalCallReference(
                    caller=caller,
                    target=target,
                    call_type='instantiation',
                ))

        # Match `ClassName.MethodName(` (static calls)
        for m in re.finditer(r'\b([A-Z]\w+)\.([A-Z]\w+)\s*\(', content):
            target = f"{m.group(1)}.{m.group(2)}"
            if target not in seen:
                seen.add(target)
                refs.append(ExternalCallReference(
                    caller=caller,
                    target=target,
                    call_type='invoke',
                ))

        return refs

    def resolve_external_call(
        self,
        call_ref: ExternalCallReference,
        search_paths: List[str]
    ) -> ExternalCallReference:
        """Resolve a C# external call — best-effort file lookup."""
        # Try to find a .cs file matching the class name
        class_name = call_ref.target.split('.')[0]
        for sp in search_paths:
            for f in Path(sp).rglob(f'{class_name}.cs'):
                return ExternalCallReference(
                    caller=call_ref.caller,
                    target=call_ref.target,
                    call_type=call_ref.call_type,
                    file_path=str(f),
                )
        return call_ref

    def build_call_hierarchy(
        self,
        file_path: str,
        search_paths: List[str],
        depth: int = 1
    ) -> Dict[str, Any]:
        """Build a call hierarchy tree for the given C# source file."""
        calls = self.parse_external_calls(file_path)
        hierarchy = {
            'file': Path(file_path).name,
            'calls': [
                {'target': c.target, 'type': c.call_type}
                for c in calls
            ]
        }
        return hierarchy

    # =========================================================================
    # Metadata
    # =========================================================================

    def get_metadata_file_patterns(
        self,
        program_name: str
    ) -> Dict[str, List[str]]:
        """Get C# metadata file patterns mapped to normalized keys."""
        return {
            'structural_outline': [
                f'structural_outline/{program_name}.json',
                f'ctags/ctags-{program_name}-outline.json',
            ],
            'symbol_table': [
                f'symbol_table/{program_name}.json',
            ],
            'syntax_tree': [
                f'syntax_tree/{program_name}.json',
            ],
            'control_flow_graph': [],  # Not typically generated for C#
        }

    def normalize_metadata(
        self,
        raw_metadata: Dict[str, Any]
    ) -> NormalizedMetadata:
        """Normalize C# metadata — pass-through since config-driven MCP uses normalized keys."""
        return NormalizedMetadata(
            structural_outline=raw_metadata.get('structural_outline', {}),
            control_flow_graph=raw_metadata.get('control_flow_graph', {}),
            symbol_table=raw_metadata.get('symbol_table', {}),
            syntax_tree=raw_metadata.get('syntax_tree', {}),
            static_analysis=raw_metadata.get('static_analysis', {}),
        )

    # =========================================================================
    # Mandatory Elements
    # =========================================================================

    def get_entry_point_patterns(self) -> List[str]:
        """Get C# entry point patterns."""
        return ['Main', 'Startup', 'Configure', 'ConfigureServices',
                'OnStart', 'Run', 'Execute', 'Program']

    def get_error_handler_patterns(self) -> List[str]:
        """Get C# error handler patterns."""
        return ['Catch', 'HandleError', 'OnException', 'HandleException',
                'ErrorHandler', 'ExceptionHandler', 'OnError']

    def identify_mandatory_elements(
        self,
        metadata: Dict[str, Any]
    ) -> Dict[str, List[MandatoryElement]]:
        """Identify C# mandatory elements from metadata."""
        entry_patterns = [p.lower() for p in self.get_entry_point_patterns()]
        error_patterns = [p.lower() for p in self.get_error_handler_patterns()]

        result: Dict[str, List[MandatoryElement]] = {
            'entry_points': [],
            'error_handlers': [],
            'call_sites': [],
        }

        # Extract symbols from metadata
        symbols = []
        outline = metadata.get('structural_outline', {})
        if isinstance(outline, dict):
            if 'outline' in outline and 'other' in outline['outline']:
                symbols = outline['outline']['other']
            elif 'symbols' in outline:
                symbols = outline['symbols']

        for sym in symbols:
            name = sym.get('name', '')
            line = sym.get('line', 0)
            name_lower = name.lower()

            if any(p in name_lower for p in entry_patterns):
                result['entry_points'].append(MandatoryElement(
                    name=name, line=line, category='entry_point'
                ))
            elif any(p in name_lower for p in error_patterns):
                result['error_handlers'].append(MandatoryElement(
                    name=name, line=line, category='error_handler'
                ))

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
        """Generate a C# program map showing namespace/class/method hierarchy."""
        lines = []
        lines.append(f"# Program Map: {program_name}")
        lines.append("")

        # Extract symbols
        symbols = []
        outline = metadata.get('structural_outline', metadata.get('ctags_outline', {}))
        if isinstance(outline, dict):
            if 'outline' in outline and 'other' in outline['outline']:
                symbols = outline['outline']['other']
            elif 'symbols' in outline:
                symbols = outline['symbols']

        if not symbols:
            lines.append("*(No structural metadata available)*")
            return '\n'.join(lines)

        # Group by kind
        namespaces = [s for s in symbols if s.get('kind') == 'namespace']
        classes = [s for s in symbols if s.get('kind') in ('class', 'struct', 'interface', 'enum')]
        methods = [s for s in symbols if s.get('kind') in ('method', 'function', 'member')]
        properties = [s for s in symbols if s.get('kind') == 'property']

        if namespaces:
            lines.append("## Namespaces")
            for ns in namespaces:
                lines.append(f"- {ns.get('name', '?')} (line {ns.get('line', '?')})")
            lines.append("")

        if classes:
            lines.append("## Types")
            for cls in classes:
                kind = cls.get('kind', 'class')
                scope = cls.get('scope', '')
                prefix = f"  [{scope}]" if scope else ""
                lines.append(f"- {kind} {cls.get('name', '?')}{prefix} (line {cls.get('line', '?')})")
            lines.append("")

        if methods:
            lines.append("## Methods")
            for meth in methods[:token_budget // 50]:  # Rough budget control
                scope = meth.get('scope', '')
                prefix = f"  [{scope}]" if scope else ""
                lines.append(f"- {meth.get('name', '?')}(){prefix} (line {meth.get('line', '?')})")
            if len(methods) > token_budget // 50:
                lines.append(f"  ... and {len(methods) - token_budget // 50} more methods")
            lines.append("")

        if properties:
            lines.append("## Properties")
            for prop in properties[:30]:
                lines.append(f"- {prop.get('name', '?')} (line {prop.get('line', '?')})")
            if len(properties) > 30:
                lines.append(f"  ... and {len(properties) - 30} more properties")
            lines.append("")

        # Summary
        lines.append("## Summary")
        lines.append(f"- Namespaces: {len(namespaces)}")
        lines.append(f"- Types: {len(classes)}")
        lines.append(f"- Methods: {len(methods)}")
        lines.append(f"- Properties: {len(properties)}")

        return '\n'.join(lines)

    def get_language_context_for_prompt(self) -> str:
        """Get C#-specific context for LLM prompts."""
        return (
            "This is a .NET/C# source file. C# is an object-oriented language "
            "organized into namespaces containing classes, interfaces, structs, "
            "and enums. Programs use method calls for flow control, try/catch for "
            "error handling, using directives for namespace imports, and properties "
            "for encapsulated field access. Key concepts include inheritance, "
            "interfaces, generics, async/await, LINQ, events, and delegates. "
            "Use C# terminology: namespace, class, method, property, field, "
            "interface, struct, enum, delegate, event, using, try/catch, async/await."
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
        """Build a full-context C# prompt for a documentation section."""
        context = self.get_language_context_for_prompt()

        prompt = f"""You are documenting the .NET/C# source file: {program_name}

{context}

## Program Structure Map
{program_map}

## Source Code
```csharp
{source_code}
```

## Documentation Section: {section_id}
{instruction}

Generate the documentation section based on the source code and metadata above.
Use C# terminology and conventions throughout.
"""
        return prompt

    def build_full_context(
        self,
        program_name: str,
        source_file_path: str,
        metadata_dir: str,
        include_line_numbers: bool = False,
        include_program_map: bool = True
    ) -> Dict[str, Any]:
        """Build complete C# context dictionary for LLM calls."""
        result: Dict[str, Any] = {}

        # Load source code
        path = Path(source_file_path)
        if path.exists():
            with open(path, 'r', encoding='utf-8', errors='replace') as f:
                source = f.read()
            if include_line_numbers:
                numbered_lines = []
                for i, line in enumerate(source.splitlines(), 1):
                    numbered_lines.append(f"{i:6d}\t{line}")
                source = '\n'.join(numbered_lines)
            result['source_code'] = source

        # Load metadata
        metadata = {}
        meta_dir = Path(metadata_dir)
        patterns = self.get_metadata_file_patterns(program_name)
        for key, file_patterns in patterns.items():
            for pat in file_patterns:
                fpath = meta_dir / pat
                if fpath.exists():
                    import json
                    with open(fpath, 'r') as f:
                        metadata[key] = json.load(f)
                    break
            if key not in metadata:
                metadata[key] = {}
        result['metadata'] = metadata

        # Generate program map
        if include_program_map:
            result['program_map'] = self.generate_program_map(program_name, metadata)

        return result
