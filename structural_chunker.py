"""
Structural Chunker — Tree-Sitter query_code Based Semantic Chunking

Language-agnostic chunking module that uses tree-sitter query_code results
to split source files at precise declaration boundaries. Provides structural
context headers that tell the LLM exactly where each chunk sits within the
file's class/namespace hierarchy.

Capture naming convention (in .scm queries):
  @container.def / @container.name — classes, structs, interfaces, namespaces, enums
  @member.def    / @member.name    — methods, properties, constructors, fields

This module is config-driven: .scm query patterns live in YAML config,
not hardcoded here.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from language_adapter import ChunkVerification, SourceChunk


# =============================================================================
# Data Structures
# =============================================================================

@dataclass
class Declaration:
    """A single declaration (method, property, constructor, field, etc.)."""
    name: str
    kind: str          # node type from tree-sitter (e.g., "method_declaration")
    start_line: int    # 1-indexed
    end_line: int      # 1-indexed
    parent: Optional[str] = None  # container name if this is a member


@dataclass
class Container(Declaration):
    """A container declaration (class, struct, interface, namespace, enum)."""
    members: List[Declaration] = field(default_factory=list)


@dataclass
class DeclarationMap:
    """Parsed query_code results organized into containers and standalone members."""
    containers: List[Container]
    standalone: List[Declaration]

    @property
    def all_declarations(self) -> List[Declaration]:
        """Flat list of all declarations sorted by start_line."""
        all_decls: List[Declaration] = []
        all_decls.extend(self.containers)
        for c in self.containers:
            all_decls.extend(c.members)
        all_decls.extend(self.standalone)
        return sorted(all_decls, key=lambda d: d.start_line)


# =============================================================================
# Build Declaration Map from query_code Results
# =============================================================================

def build_declaration_map(query_results: Dict[str, Any]) -> Optional[DeclarationMap]:
    """
    Parse query_code MCP tool results into a DeclarationMap.

    Expects the standard query_code response format:
    {
        "success": true,
        "matches": [
            {"capture": "container.def", "type": "class_declaration",
             "text": "...", "start_point": {"row": N, "column": N},
             "end_point": {"row": N, "column": N}},
            {"capture": "container.name", "type": "identifier",
             "text": "ClassName", ...},
            ...
        ]
    }

    Capture naming convention:
      container.def / container.name — containers (class, struct, etc.)
      member.def    / member.name    — members (method, property, etc.)
    """
    if not query_results or not query_results.get('success'):
        return None

    matches = query_results.get('matches', [])
    if not matches:
        return None

    # Classify captures into container vs member roles.
    # Supports two conventions:
    #   Standardized: container.def/container.name, member.def/member.name
    #   Legacy:       class.def/class.name, ns.def/ns.name, method.def, etc.
    _CONTAINER_ROLES = {'container', 'class', 'struct', 'interface', 'enum',
                        'record', 'ns', 'namespace'}
    _MEMBER_ROLES = {'member', 'method', 'prop', 'property', 'ctor',
                     'constructor', 'field', 'event', 'operator', 'destructor'}

    container_defs = []
    container_names = []
    member_defs = []
    member_names = []

    for m in matches:
        capture = m.get('capture', '')
        start_pt = m.get('start_point', {})
        end_pt = m.get('end_point', {})
        start_line = start_pt.get('row', 0) + 1  # 0-indexed to 1-indexed
        end_line = end_pt.get('row', 0) + 1
        start_byte = m.get('start_byte', 0)
        end_byte = m.get('end_byte', 0)
        node_type = m.get('type', '')
        text = m.get('text', '')

        # Parse capture: "role.part" (e.g., "container.def", "class.name")
        parts = capture.split('.', 1)
        if len(parts) != 2:
            continue
        role, part = parts[0], parts[1]

        entry = {
            'start_line': start_line,
            'end_line': end_line,
            'type': node_type,
            'start_byte': start_byte,
            'end_byte': end_byte,
            'text': text,
        }

        if role in _CONTAINER_ROLES:
            if part == 'def':
                container_defs.append(entry)
            elif part == 'name':
                container_names.append(entry)
        elif role in _MEMBER_ROLES:
            if part == 'def':
                member_defs.append(entry)
            elif part == 'name':
                member_names.append(entry)

    # Pair container.def with container.name by byte containment
    containers: List[Container] = []
    for cdef in container_defs:
        name = _find_name_for_def(cdef, container_names)
        containers.append(Container(
            name=name,
            kind=cdef['type'],
            start_line=cdef['start_line'],
            end_line=cdef['end_line'],
        ))

    # Sort containers by start_line for consistent parent assignment
    containers.sort(key=lambda c: c.start_line)

    # Pair member.def with member.name by byte containment
    members: List[Declaration] = []
    for mdef in member_defs:
        name = _find_name_for_def(mdef, member_names)
        members.append(Declaration(
            name=name,
            kind=mdef['type'],
            start_line=mdef['start_line'],
            end_line=mdef['end_line'],
        ))

    # Assign members to containers via range containment
    # A member belongs to the smallest (most specific) container that fully contains it
    standalone: List[Declaration] = []
    for member in members:
        parent = _find_parent_container(member, containers)
        if parent:
            member.parent = parent.name
            parent.members.append(member)
        else:
            standalone.append(member)

    # Sort members within each container
    for c in containers:
        c.members.sort(key=lambda m: m.start_line)

    standalone.sort(key=lambda m: m.start_line)

    return DeclarationMap(containers=containers, standalone=standalone)


# =============================================================================
# Build Declaration Map from tree-sitter-graph Results
# =============================================================================

def build_declaration_map_from_graph(graph_data: Any) -> Optional[DeclarationMap]:
    """
    Parse tree-sitter-graph JSON output into a DeclarationMap.

    Expects the graph format: a list of nodes with attrs and edges.
    Each node has: {"id": N, "attrs": {"type": {"type":"string","string":"class"}, ...}, "edges": [...]}

    The graph may be wrapped: {"success": true, "graph": [...]} or bare [...].

    Nodes with edges are containers (class→method, class→property, etc.).
    Nodes without edges that are member types (method, property, etc.) are standalone.
    Rows are 0-indexed in graph output; converted to 1-indexed here.

    Container types: class, struct, interface, namespace, enum, record
    Member types: method, constructor, property, field, event, operator, destructor
    """
    # Unwrap if response envelope
    if isinstance(graph_data, dict):
        nodes = graph_data.get('graph', [])
        if not nodes:
            return None
    elif isinstance(graph_data, list):
        nodes = graph_data
    else:
        return None

    if not nodes:
        return None

    _CONTAINER_TYPES = {'class', 'struct', 'interface', 'namespace', 'enum', 'record'}
    _MEMBER_TYPES = {'method', 'constructor', 'property', 'field', 'event',
                     'operator', 'destructor'}

    def _attr_val(attrs: Dict, key: str) -> Any:
        """Extract value from TSG typed attrs: {"type":"string","string":"foo"} → "foo"."""
        v = attrs.get(key, {})
        if isinstance(v, dict):
            if 'string' in v:
                return v['string']
            if 'int' in v:
                return v['int']
        return v  # already plain value

    # Build id→node lookup
    by_id: Dict[int, Dict] = {n['id']: n for n in nodes}

    # Deduplicate containers: group by (name, start_row, end_row)
    # In TSG output, a class node is duplicated once per member edge
    container_key_map: Dict[tuple, Container] = {}
    member_ids_assigned: set = set()

    for node in nodes:
        attrs = node.get('attrs', {})
        ntype = _attr_val(attrs, 'type')
        edges = node.get('edges', [])

        if ntype in _CONTAINER_TYPES and edges:
            name = _attr_val(attrs, 'name') or f"anonymous_{node['id']}"
            start_row = _attr_val(attrs, 'start_row')
            end_row = _attr_val(attrs, 'end_row')
            # Convert 0-indexed rows to 1-indexed lines
            start_line = (start_row + 1) if isinstance(start_row, int) else 1
            end_line = (end_row + 1) if isinstance(end_row, int) else start_line

            key = (name, start_line, end_line)
            if key not in container_key_map:
                container_key_map[key] = Container(
                    name=name,
                    kind=f"{ntype}_declaration",
                    start_line=start_line,
                    end_line=end_line,
                )

            container = container_key_map[key]
            # Add child members from edges
            for edge in edges:
                child_id = edge.get('sink')
                if child_id is None:
                    continue
                child_node = by_id.get(child_id)
                if not child_node:
                    continue
                child_attrs = child_node.get('attrs', {})
                child_type = _attr_val(child_attrs, 'type')
                child_name = _attr_val(child_attrs, 'name') or f"anonymous_{child_id}"
                child_start = _attr_val(child_attrs, 'start_row')
                child_end = _attr_val(child_attrs, 'end_row')
                child_start_line = (child_start + 1) if isinstance(child_start, int) else 1
                child_end_line = (child_end + 1) if isinstance(child_end, int) else child_start_line

                # Deduplicate members by (name, start_line)
                member_key = (child_name, child_start_line)
                if member_key not in member_ids_assigned:
                    member_ids_assigned.add(member_key)
                    container.members.append(Declaration(
                        name=child_name,
                        kind=f"{child_type}_declaration" if child_type else "unknown",
                        start_line=child_start_line,
                        end_line=child_end_line,
                        parent=container.name,
                    ))

    # Collect standalone nodes (containers without edges, standalone members)
    containers = sorted(container_key_map.values(), key=lambda c: c.start_line)
    standalone: List[Declaration] = []

    for node in nodes:
        attrs = node.get('attrs', {})
        ntype = _attr_val(attrs, 'type')
        edges = node.get('edges', [])

        if not ntype:
            continue

        name = _attr_val(attrs, 'name') or f"anonymous_{node['id']}"
        start_row = _attr_val(attrs, 'start_row')
        end_row = _attr_val(attrs, 'end_row')
        start_line = (start_row + 1) if isinstance(start_row, int) else 1
        end_line = (end_row + 1) if isinstance(end_row, int) else start_line

        # Standalone containers (no edges — e.g., enums, empty classes)
        if ntype in _CONTAINER_TYPES and not edges:
            key = (name, start_line, end_line)
            if key not in container_key_map:
                containers.append(Container(
                    name=name,
                    kind=f"{ntype}_declaration",
                    start_line=start_line,
                    end_line=end_line,
                ))
                container_key_map[key] = containers[-1]

    # Sort members within each container
    for c in containers:
        c.members.sort(key=lambda m: m.start_line)

    containers.sort(key=lambda c: c.start_line)

    if not containers and not standalone:
        return None

    return DeclarationMap(containers=containers, standalone=standalone)


def _find_name_for_def(
    def_match: Dict[str, Any],
    name_matches: List[Dict[str, Any]]
) -> str:
    """Find the .name capture whose byte range falls inside the .def capture."""
    def_start = def_match['start_byte']
    def_end = def_match['end_byte']

    for nm in name_matches:
        if nm['start_byte'] >= def_start and nm['end_byte'] <= def_end:
            return nm['text']

    # Fallback: extract from the first line of the .def text
    text = def_match.get('text', '')
    if text:
        # Take first meaningful token from the text
        first_line = text.split('\n')[0].strip()
        # Truncate to something reasonable
        if len(first_line) > 60:
            first_line = first_line[:57] + '...'
        return first_line

    return f"anonymous_{def_match['start_line']}"


def _find_parent_container(
    member: Declaration,
    containers: List[Container]
) -> Optional[Container]:
    """
    Find the smallest container that fully contains the member.

    Uses range containment: member.start_line >= container.start_line
    and member.end_line <= container.end_line.
    """
    best: Optional[Container] = None
    best_size = float('inf')

    for c in containers:
        if member.start_line >= c.start_line and member.end_line <= c.end_line:
            size = c.end_line - c.start_line
            if size < best_size:
                best = c
                best_size = size

    return best


# =============================================================================
# Chunk at Declaration Boundaries
# =============================================================================

def chunk_at_declaration_boundaries(
    lines: List[str],
    declaration_map: DeclarationMap,
    max_tokens_per_chunk: int = 10000,
    overhead_tokens: int = 0,
) -> Tuple[List[SourceChunk], ChunkVerification]:
    """
    Split source lines into chunks at declaration boundaries.

    Never splits a single declaration across chunks. If a single
    declaration exceeds the token limit, it becomes its own chunk
    (the LLM handles it as best it can).

    Args:
        lines: Source code lines (with line endings)
        declaration_map: Parsed query_code results
        max_tokens_per_chunk: Maximum tokens per chunk
        overhead_tokens: Tokens to reserve for headers/program map

    Returns:
        Tuple of (list of SourceChunks, ChunkVerification)
    """
    from tokenizer import estimate_tokens

    total_lines = len(lines)
    if total_lines == 0:
        return [], ChunkVerification(valid=True, total_lines=0, chunks=0, coverage="0/0")

    effective_max = max_tokens_per_chunk - overhead_tokens
    if effective_max < 1000:
        print(f"  ⚠ Overhead ({overhead_tokens:,}) leaves only {effective_max:,} tokens — using half of max")
        effective_max = max_tokens_per_chunk // 2

    # Build sorted split candidates from all member start lines
    # These are the points where we can safely split
    split_points = set()
    split_points.add(0)  # Always include start of file

    # Add member boundaries (start of each member)
    for c in declaration_map.containers:
        split_points.add(c.start_line - 1)  # 0-indexed
        for m in c.members:
            split_points.add(m.start_line - 1)  # 0-indexed

    for m in declaration_map.standalone:
        split_points.add(m.start_line - 1)  # 0-indexed

    boundaries = sorted(split_points)

    # Use the existing chunking algorithm with these boundaries
    # This handles the accumulate-and-split logic correctly
    chunks: List[SourceChunk] = []
    current_start = 0  # 0-indexed
    current_lines: List[str] = []
    current_tokens = 0

    for i, boundary in enumerate(boundaries):
        next_boundary = boundaries[i + 1] if i + 1 < len(boundaries) else total_lines

        section_lines = lines[boundary:next_boundary]
        section_text = ''.join(section_lines)
        section_tokens = estimate_tokens(section_text, model="gpt-4")

        # Case 1: Fits in current chunk
        if current_tokens + section_tokens <= effective_max:
            current_lines.extend(section_lines)
            current_tokens += section_tokens

        # Case 2: Would overflow — save current chunk, start new one
        elif current_lines:
            chunk_text = ''.join(current_lines)
            chunks.append(SourceChunk(
                chunk_number=len(chunks) + 1,
                start_line=current_start + 1,  # 1-indexed
                end_line=current_start + len(current_lines),
                line_count=len(current_lines),
                content=chunk_text,
                estimated_tokens=current_tokens,
            ))
            current_start = boundary
            current_lines = list(section_lines)
            current_tokens = section_tokens

        # Case 3: Single section exceeds limit — it becomes its own chunk
        else:
            print(f"  ⚠ Large declaration at line {boundary + 1}: "
                  f"{len(section_lines):,} lines (~{section_tokens:,} tokens) exceeds limit")
            chunk_text = ''.join(section_lines)
            chunks.append(SourceChunk(
                chunk_number=len(chunks) + 1,
                start_line=boundary + 1,
                end_line=boundary + len(section_lines),
                line_count=len(section_lines),
                content=chunk_text,
                estimated_tokens=section_tokens,
            ))
            current_start = next_boundary
            current_lines = []
            current_tokens = 0

    # Final chunk
    if current_lines:
        chunk_text = ''.join(current_lines)
        chunks.append(SourceChunk(
            chunk_number=len(chunks) + 1,
            start_line=current_start + 1,
            end_line=current_start + len(current_lines),
            line_count=len(current_lines),
            content=chunk_text,
            estimated_tokens=current_tokens,
        ))

    # Verify coverage
    total_chunk_lines = sum(c.line_count for c in chunks)
    valid = total_chunk_lines == total_lines

    if not valid:
        # Run detailed verification
        chunk_dicts = [
            {'chunk_number': c.chunk_number, 'start_line': c.start_line,
             'end_line': c.end_line, 'line_count': c.line_count,
             'content': c.content, 'estimated_tokens': c.estimated_tokens}
            for c in chunks
        ]
        from source_chunker import verify_chunk_coverage
        detail = verify_chunk_coverage(chunk_dicts, total_lines)
        verification = ChunkVerification(
            valid=False,
            total_lines=total_lines,
            chunks=len(chunks),
            coverage=f"{total_chunk_lines}/{total_lines}",
            error=detail.get('error', f'Line count mismatch: {total_chunk_lines} vs {total_lines}'),
            method='query_code_boundaries',
        )
    else:
        verification = ChunkVerification(
            valid=True,
            total_lines=total_lines,
            chunks=len(chunks),
            coverage=f"{total_chunk_lines}/{total_lines} (100%)",
            method='query_code_boundaries',
        )

    return chunks, verification


# =============================================================================
# Structural Context Generation
# =============================================================================

def get_structural_context(
    chunk_start: int,
    chunk_end: int,
    declaration_map: DeclarationMap,
    seen_members: Dict[str, List[str]],
) -> List[str]:
    """
    Generate structural context lines for a chunk.

    Determines which container(s) a chunk overlaps and generates
    human-readable context like:
      **Continues**: class LinePitch (line 767–3356) — 9 of 43 members
      **Complete**: class SmallHelper (line 100–150) — 5 of 5 members

    Args:
        chunk_start: First line of chunk (1-indexed)
        chunk_end: Last line of chunk (1-indexed)
        declaration_map: Full declaration map for the file
        seen_members: Dict tracking {container_name: [member_names]} already processed

    Returns:
        List of structural context strings
    """
    context_lines: List[str] = []

    for container in declaration_map.containers:
        # Check overlap
        if chunk_end < container.start_line or chunk_start > container.end_line:
            continue  # No overlap

        # Count members in this chunk
        members_in_chunk = [
            m for m in container.members
            if m.start_line >= chunk_start and m.end_line <= chunk_end
        ]
        total_members = len(container.members)
        chunk_member_count = len(members_in_chunk)

        # Determine relationship tag
        contains_start = chunk_start <= container.start_line
        contains_end = chunk_end >= container.end_line

        if contains_start and contains_end:
            tag = "Complete"
        elif contains_start:
            tag = "Starts"
        elif contains_end:
            tag = "Ends"
        else:
            tag = "Continues"

        # Friendly kind name (strip _declaration suffix)
        kind = container.kind.replace('_declaration', '').replace('_definition', '')

        # Build context line
        line = f"**{tag}**: {kind} {container.name} "
        line += f"(line {container.start_line}\u2013{container.end_line})"
        if total_members > 0:
            line += f" \u2014 {chunk_member_count} of {total_members} members"

        # For Continues/Ends, note how many were previously documented
        if tag in ("Continues", "Ends"):
            prev = seen_members.get(container.name, [])
            if prev:
                line += f"\n  Previously documented: {len(prev)} members"

        context_lines.append(line)

    return context_lines


def update_seen_members(
    chunk_start: int,
    chunk_end: int,
    declaration_map: DeclarationMap,
    seen_members: Dict[str, List[str]],
) -> None:
    """
    Update seen_members with members that fall within this chunk's range.

    Call this after processing each chunk to track which members
    have been documented.

    Args:
        chunk_start: First line of chunk (1-indexed)
        chunk_end: Last line of chunk (1-indexed)
        declaration_map: Full declaration map
        seen_members: Dict to update in-place
    """
    for container in declaration_map.containers:
        for member in container.members:
            if member.start_line >= chunk_start and member.end_line <= chunk_end:
                seen_members.setdefault(container.name, []).append(member.name)
