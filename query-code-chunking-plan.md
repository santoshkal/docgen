# Enhancement Plan: Tree-Sitter `query_code` Based Semantic Chunking

## Goal

Replace the current regex/ctags-based boundary detection in Phase 1 chunking with tree-sitter `query_code` MCP tool results. This provides **precise start/end lines for every declaration** (class, method, property, constructor, etc.) and enables **structural context headers** that tell the LLM exactly where each chunk sits within the file's class hierarchy.

This implementation must be **language-agnostic** and **config-driven**.

---

## Current State (What We Have)

### Chunking Pipeline (Phase 1)
```
run_phase1_code_explanation()
  → build_section_context()
  → process_large_file_in_chunks()
      → adapter.chunk_source_file(file_path, max_tokens, metadata, program_map)
          → adapter.find_structural_boundaries(lines, metadata)  ← REGEX/CTAGS
          → create_chunks_at_boundaries(lines, boundaries, max_tokens, overhead)
      → FOR EACH CHUNK:
          → adapter.format_chunk_for_llm(chunk, ...)
          → format_context_as_plaintext(chunk_context)
          → generate_section_content(...)  → LLM call
```

### Current Boundary Detection
- **COBOL** (`languages/cobol/adapter.py:142-172`): CTags `paragraph` symbols → line numbers. Fallback: regex for DIVISION/SECTION/paragraph names.
- **C#** (`languages/dotnet/adapter.py:150-229`): CTags `class`/`method`/`property` symbols → line numbers. Fallback: regex patterns `_RE_TYPE_DECL`, `_RE_METHOD`.

### Limitations
1. **CTags gives start lines only** — no end lines. We don't know where a method/class ends.
2. **Regex fallback** is fragile — can't handle nested classes, complex generics, or multi-line signatures.
3. **No structural context** — the LLM doesn't know if a chunk is in the middle of a 2000-line class or contains three small classes.
4. **Language-specific regex** — each adapter hardcodes its own patterns.

### What `query_code` Provides
- **Precise `start_point.row` / `end_point.row`** for every matched node (0-indexed)
- **Hierarchical captures** — `@class.def`, `@method.def`, `@prop.def` etc.
- **Language-agnostic** — same tool, different `.scm` query patterns per language
- **No depth truncation** — unlike `generate_ast` with `max_depth`, `query_code` returns full ranges

---

## Design

### Architecture Overview (Post-Enhancement)

```
metadata generation (one-time per file):
  → MCP call: query_code(source_code, language, query_pattern)
  → Save result as query-code-{program}-boundaries.json

Phase 1 chunking:
  → load query_code boundaries from metadata dir
  → build_declaration_map(query_results)          ← NEW
      → containers: [{name, kind, start, end, members: [...]}]
      → standalone: [{name, kind, start, end}]
  → chunk_at_declaration_boundaries(lines, declaration_map, max_tokens)  ← NEW
      → splits at method/property boundaries
      → never splits a single declaration across chunks
  → FOR EACH CHUNK:
      → get_structural_context(chunk, declaration_map, seen_members)  ← NEW
      → inject structural context header into chunk
      → format_context_as_plaintext(chunk_context)  ← UPDATED
      → generate_section_content(...)  → LLM call
```

---

## Implementation Steps

### Step 1: Config Schema — Add `query_code` Tool + Chunking Config

**File: `config-dotnet-imes.yaml` (and all config files)**

Add `query_code` as a new MCP tool under `metadata.servers.tree-sitter`:

```yaml
metadata:
  servers:
    tree-sitter:
      docker_image: treesitter-mcp:test
      tools:
        - name: get_symbols
          args:
            source_code: "{{source_content}}"
            language: "c_sharp"
        - name: generate_ast
          args:
            source_code: "{{source_content}}"
            language: "c_sharp"
            max_depth: 6
        - name: query_code              # NEW
          args:
            source_code: "{{source_content}}"
            language: "c_sharp"
            query_pattern: "{{chunking_query}}"  # Resolved from chunking config
```

Add chunking configuration section:

```yaml
chunking:
  # Strategy: "query_code" (tree-sitter), "ctags" (legacy), "regex" (fallback)
  strategy: query_code

  # Tree-sitter .scm query for boundary detection.
  # This query must capture container declarations (@container.def, @container.name)
  # and member declarations (@member.def, @member.name).
  # The capture naming convention is: <role>.<part>
  #   role: "container" (class/struct/interface/namespace) or "member" (method/property/constructor/field)
  #   part: "def" (full node range) or "name" (identifier)
  #
  # Language-specific queries below. Add new languages by adding entries.
  queries:
    c_sharp: |
      (namespace_declaration name: (_) @container.name) @container.def
      (class_declaration name: (identifier) @container.name) @container.def
      (struct_declaration name: (identifier) @container.name) @container.def
      (interface_declaration name: (identifier) @container.name) @container.def
      (enum_declaration name: (identifier) @container.name) @container.def
      (record_declaration name: (identifier) @container.name) @container.def
      (constructor_declaration name: (identifier) @member.name) @member.def
      (method_declaration name: (identifier) @member.name) @member.def
      (property_declaration name: (identifier) @member.name) @member.def
      (field_declaration) @member.def
      (event_declaration) @member.def
      (operator_declaration) @member.def
      (destructor_declaration) @member.def

    java: |
      (package_declaration) @container.def
      (class_declaration name: (identifier) @container.name) @container.def
      (interface_declaration name: (identifier) @container.name) @container.def
      (enum_declaration name: (identifier) @container.name) @container.def
      (record_declaration name: (identifier) @container.name) @container.def
      (constructor_declaration name: (identifier) @member.name) @member.def
      (method_declaration name: (identifier) @member.name) @member.def
      (field_declaration) @member.def

    python: |
      (class_definition name: (identifier) @container.name) @container.def
      (function_definition name: (identifier) @member.name) @member.def

    # COBOL: paragraphs are the natural boundary; no nesting concept
    cobol: |
      (section_header (section_name) @container.name) @container.def
      (paragraph_header (paragraph_name) @member.name) @member.def

    typescript: |
      (class_declaration name: (type_identifier) @container.name) @container.def
      (interface_declaration name: (type_identifier) @container.name) @container.def
      (method_definition name: (property_identifier) @member.name) @member.def
      (public_field_definition name: (property_identifier) @member.name) @member.def
      (function_declaration name: (identifier) @member.name) @member.def

    go: |
      (type_declaration (type_spec name: (type_identifier) @container.name)) @container.def
      (function_declaration name: (identifier) @member.name) @member.def
      (method_declaration name: (field_identifier) @member.name) @member.def

  # Maximum tokens per chunk (can be overridden)
  max_tokens_per_chunk: 10000

  # Include structural context headers in chunks sent to LLM
  structural_context: true

  # Fallback strategy if query_code results unavailable
  fallback_strategy: ctags    # "ctags" or "regex"
```

**Key design decisions:**
- `.scm` queries live in config YAML, not in code — users can tune them per language
- Standardized capture names: `@container.def`/`@container.name` and `@member.def`/`@member.name`
- `strategy` field selects chunking backend; `fallback_strategy` used when primary fails
- Language key (e.g., `c_sharp`) matches tree-sitter language identifier

---

### Step 2: Metadata Generation — Call `query_code` During MCP Metadata Phase

**File: `mcp_metadata_generator.py`**

Add logic to invoke `query_code` tool when configured, using the query pattern from `chunking.queries.<language>`:

1. In `generate_tree_sitter_metadata()` (or equivalent), after calling `get_symbols` and `generate_ast`:
   - Read `chunking.queries.<language>` from config
   - Call `query_code` MCP tool with `source_code`, `language`, and the query pattern
   - Save result to `metadata/<program>/query-code-{program}-boundaries.json`

2. The query pattern placeholder `{{chunking_query}}` in the tool args should be resolved from `chunking.queries.<language>` at invocation time.

**Output file format** (same as MCP tool returns):
```json
{
  "success": true,
  "language": "c_sharp",
  "match_count": 248,
  "matches": [
    {
      "capture": "container.def",
      "type": "class_declaration",
      "text": "public class LinePitch { ... }",
      "start_point": {"row": 766, "column": 4},
      "end_point": {"row": 3355, "column": 5}
    },
    {
      "capture": "container.name",
      "type": "identifier",
      "text": "LinePitch",
      "start_point": {"row": 766, "column": 17},
      "end_point": {"row": 766, "column": 26}
    },
    {
      "capture": "member.def",
      "type": "method_declaration",
      "text": "public void CalculateOffset() { ... }",
      "start_point": {"row": 1400, "column": 8},
      "end_point": {"row": 1450, "column": 9}
    }
  ]
}
```

---

### Step 3: New Module — `structural_chunker.py`

Create a new module that is **language-agnostic** and works entirely from `query_code` results.

**File: `structural_chunker.py`**

#### 3A: Parse `query_code` Results → Declaration Map

```python
@dataclass
class Declaration:
    name: str
    kind: str          # "class", "struct", "method", "property", etc.
    start_line: int    # 1-indexed
    end_line: int      # 1-indexed
    parent: Optional[str] = None  # container name if this is a member

@dataclass
class Container(Declaration):
    members: List[Declaration] = field(default_factory=list)

@dataclass
class DeclarationMap:
    containers: List[Container]    # classes, structs, interfaces, enums, namespaces
    standalone: List[Declaration]  # top-level functions/members not inside a container
    all_declarations: List[Declaration]  # flat list of all, sorted by start_line
```

**`build_declaration_map(query_results: Dict) -> DeclarationMap`**

Algorithm:
1. Separate matches into `container.def`/`container.name` pairs and `member.def`/`member.name` pairs
2. For each `container.def` match: create a `Container` with `start_line = row + 1`, `end_line = end_row + 1`
3. For each `container.name` match: associate the name with the container by matching byte position (the `.name` capture is always inside the `.def` capture)
4. For each `member.def` match: create a `Declaration`, determine parent container via **range containment** (member start/end falls within container start/end)
5. Members not inside any container → `standalone` list
6. Sort containers by start_line; sort members within each container by start_line

**Handling `.name` vs `.def` capture pairing:**
- `.def` captures provide the full range (start_line, end_line)
- `.name` captures provide the identifier text
- Match them: for each `.name`, find the `.def` whose byte range contains the `.name` capture
- For `field_declaration` and similar that may lack a `.name` capture: extract name from the `.def` text (first identifier), or use "anonymous_field_N"

#### 3B: Chunk at Declaration Boundaries

**`chunk_at_declaration_boundaries(lines, declaration_map, max_tokens, overhead_tokens) -> List[SourceChunk]`**

Algorithm:
1. Build a sorted list of **split candidates** — the start lines of all member declarations
2. Walk through split candidates, accumulating lines until `max_tokens - overhead_tokens` is reached
3. **Never split inside a declaration** — if adding a member would exceed the limit, the current chunk ends before that member
4. **Edge case: single member > max_tokens** — fall back to statement-level splitting within that member (reuse existing `create_chunks_at_statement_boundaries()`)
5. **Coverage guarantee** — all lines from line 1 to EOF are covered, no gaps, no overlaps
6. Run existing `verify_chunk_coverage()` and `verify_chunk_reconstruction()` for correctness proof

**Key difference from current approach:**
- Current: boundaries are **start lines only**, chunker doesn't know where boundaries end
- New: boundaries have **start AND end lines**, so we can guarantee no declaration is split

#### 3C: Structural Context Generation

**`get_structural_context(chunk_start, chunk_end, declaration_map, seen_members) -> List[str]`**

Algorithm (range-intersection):
```python
for container in declaration_map.containers:
    if chunk_end < container.start_line or chunk_start > container.end_line:
        continue  # no overlap

    # Count members of this container in this chunk
    members_in_chunk = [m for m in container.members
                        if m.start_line >= chunk_start and m.end_line <= chunk_end]
    total_members = len(container.members)
    chunk_member_count = len(members_in_chunk)

    # Determine relationship tag
    if chunk_start <= container.start_line and chunk_end >= container.end_line:
        tag = "Complete"
    elif chunk_start <= container.start_line:
        tag = "Starts"
    elif chunk_end >= container.end_line:
        tag = "Ends"
    else:
        tag = "Continues"

    # Build context line
    line = f"**{tag}**: {container.kind} {container.name} "
    line += f"(line {container.start_line}–{container.end_line}) — "
    line += f"{chunk_member_count} of {total_members} members"

    if tag in ("Continues", "Ends"):
        prev = seen_members.get(container.name, [])
        if prev:
            line += f"\n  Previously documented: {len(prev)} members"

    context_lines.append(line)
```

**`update_seen_members(chunk_start, chunk_end, declaration_map, seen_members)`**

After processing each chunk, record which members were in it:
```python
for container in declaration_map.containers:
    for member in container.members:
        if member.start_line >= chunk_start and member.end_line <= chunk_end:
            seen_members.setdefault(container.name, []).append(member.name)
```

---

### Step 4: Update Language Adapter Interface

**File: `language_adapter.py`**

Add new abstract method to `LanguageAdapter`:

```python
def get_chunking_query(self, config: Optional[Dict] = None) -> Optional[str]:
    """
    Return the tree-sitter .scm query for structural boundary detection.

    Checks config['chunking']['queries'][language_key] first.
    Returns None if no query available (triggers fallback).
    """
```

Update `chunk_source_file()` signature to accept optional `query_code_results`:

```python
def chunk_source_file(
    self,
    file_path: str,
    max_tokens_per_chunk: int = 100000,
    metadata: Optional[Dict[str, Any]] = None,
    program_map: Optional[str] = None,
    query_code_results: Optional[Dict[str, Any]] = None,  # NEW
    chunking_config: Optional[Dict[str, Any]] = None,      # NEW
) -> Tuple[List[SourceChunk], ChunkVerification]:
```

Default implementation in base class:
```python
def chunk_source_file(self, file_path, max_tokens, metadata=None,
                      program_map=None, query_code_results=None,
                      chunking_config=None):
    strategy = (chunking_config or {}).get('strategy', 'ctags')
    structural_context_enabled = (chunking_config or {}).get('structural_context', True)

    if strategy == 'query_code' and query_code_results:
        from structural_chunker import (
            build_declaration_map, chunk_at_declaration_boundaries
        )
        decl_map = build_declaration_map(query_code_results)
        lines = Path(file_path).read_text().splitlines(keepaliines=True)
        overhead = estimate_tokens(program_map) if program_map else 1000
        chunks, verification = chunk_at_declaration_boundaries(
            lines, decl_map, max_tokens, overhead
        )
        # Attach declaration_map to verification for structural context later
        verification.declaration_map = decl_map
        return chunks, verification

    # Fallback to existing adapter-specific implementation
    return self._chunk_source_file_legacy(file_path, max_tokens, metadata, program_map)
```

Each concrete adapter moves its current `chunk_source_file()` body to `_chunk_source_file_legacy()`.

---

### Step 5: Update `format_chunk_for_llm()` — Inject Structural Context

**File: `language_adapter.py` (base class default)**

Update signature:

```python
def format_chunk_for_llm(
    self,
    chunk: SourceChunk,
    total_chunks: int,
    file_name: str,
    program_map: Optional[str] = None,
    model: str = "gpt-4",
    structural_context: Optional[List[str]] = None,  # NEW
) -> str:
```

Insert structural context between the chunk header and source code:

```
=============================================================================
CHUNK 3 of 6 - HeijunkaData.cs
=============================================================================
Lines: 1380 to 1980 (600 lines)

### Structural Context                          ← NEW SECTION
- **Continues**: class LinePitch (line 767–3356) — 9 of 43 members
  Previously documented: 25 members

=============================================================================
CHUNK 3 SOURCE CODE (Lines 1380-1980)
=============================================================================

```csharp
<actual source code>
```
```

---

### Step 6: Update `format_context_as_plaintext()` — Handle Structural Context

**File: `cobol_doc_agent.py` (~line 1970)**

Add `structural_context` to the known keys and render it in the plaintext format:

```python
# After chunk header, before source code:
structural_context = context.get('structural_context')
if structural_context:
    parts.append("### Structural Context")
    for line in structural_context:
        parts.append(f"- {line}")
    parts.append("")
```

Add `'structural_context'` to the `skip_keys` set so it's not duplicated in "Additional Context".

---

### Step 7: Update `process_large_file_in_chunks()` — Wire Everything Together

**File: `cobol_doc_agent.py` (~line 2306)**

Changes in the chunk processing loop:

```python
def process_large_file_in_chunks(context, chunked_file_info, state, ...):
    # ... existing setup ...

    # NEW: Load query_code results from metadata dir
    query_code_results = load_query_code_results(program_name, metadata_dir)
    chunking_config = config.get('chunking', {})

    # Updated call with new params
    chunks, verification = adapter.chunk_source_file(
        file_path=file_path,
        max_tokens_per_chunk=chunking_config.get('max_tokens_per_chunk', 10000),
        metadata=ctags_metadata,
        program_map=program_map,
        query_code_results=query_code_results,      # NEW
        chunking_config=chunking_config,              # NEW
    )

    # NEW: Get declaration_map for structural context
    declaration_map = getattr(verification, 'declaration_map', None)
    seen_members = {}  # tracks members processed across chunks

    for chunk_info in chunks:
        # ... existing context building ...

        # NEW: Generate structural context for this chunk
        if declaration_map and chunking_config.get('structural_context', True):
            from structural_chunker import get_structural_context, update_seen_members
            struct_ctx = get_structural_context(
                chunk_start=chunk_info['start_line'],
                chunk_end=chunk_info['end_line'],
                declaration_map=declaration_map,
                seen_members=seen_members,
            )
            chunk_context['structural_context'] = struct_ctx

        # ... existing LLM call ...

        # NEW: Update seen_members after processing
        if declaration_map:
            update_seen_members(
                chunk_info['start_line'], chunk_info['end_line'],
                declaration_map, seen_members,
            )
```

**`load_query_code_results(program_name, metadata_dir)`** — New helper:
```python
def load_query_code_results(program_name, metadata_dir):
    """Load query_code boundary results from metadata directory."""
    candidates = [
        f"query-code-{program_name}-boundaries.json",
        f"{program_name}/query-code-boundaries.json",
    ]
    for candidate in candidates:
        path = Path(metadata_dir) / candidate
        if path.exists():
            return json.loads(path.read_text())
    return None
```

---

### Step 8: Update `config.example.yaml` — Document New Config Section

Add the full `chunking` section with all options documented and commented.

---

## Fallback Chain

```
query_code results available?
  YES → build_declaration_map() → chunk_at_declaration_boundaries()
  NO  → fallback_strategy == "ctags"?
          YES → adapter.find_structural_boundaries(lines, ctags_metadata)
                → create_chunks_at_boundaries()  [current behavior]
          NO  → regex fallback [current behavior]
```

This ensures **zero regression** — existing COBOL/C# configs without `chunking.strategy` continue to work exactly as before.

---

## File Change Summary

| File | Change Type | Description |
|------|-------------|-------------|
| `structural_chunker.py` | **NEW** | Declaration map builder, semantic chunker, structural context generator |
| `language_adapter.py` | MODIFY | Add `query_code_results` + `chunking_config` params to `chunk_source_file()`, add `structural_context` param to `format_chunk_for_llm()`, add default `query_code` chunking in base class |
| `languages/dotnet/adapter.py` | MODIFY | Rename `chunk_source_file()` → `_chunk_source_file_legacy()` |
| `languages/cobol/adapter.py` | MODIFY | Rename `chunk_source_file()` → `_chunk_source_file_legacy()` |
| `cobol_doc_agent.py` | MODIFY | Update `process_large_file_in_chunks()` to load query_code results, pass chunking_config, generate structural context. Update `format_context_as_plaintext()` for structural_context key. |
| `mcp_metadata_generator.py` | MODIFY | Add `query_code` tool invocation during metadata generation, resolve `{{chunking_query}}` placeholder |
| `config-dotnet-imes.yaml` | MODIFY | Add `chunking` section, add `query_code` tool to tree-sitter server |
| `config.example.yaml` | MODIFY | Document new `chunking` config section |

---

## Config-Driven Elements (Brought Out of Code)

| Setting | Config Path | Default | Description |
|---------|-------------|---------|-------------|
| Chunking strategy | `chunking.strategy` | `ctags` | `query_code`, `ctags`, or `regex` |
| `.scm` query per language | `chunking.queries.<lang>` | — | Tree-sitter query for boundary detection |
| Max tokens per chunk | `chunking.max_tokens_per_chunk` | `10000` | Token budget per chunk |
| Structural context on/off | `chunking.structural_context` | `true` | Include structural context headers |
| Fallback strategy | `chunking.fallback_strategy` | `ctags` | Used when query_code results unavailable |
| `query_code` MCP tool args | `metadata.servers.tree-sitter.tools[].args` | — | Language, encoding passed to MCP tool |

---

## Testing Plan

1. **Unit tests** — `tests/test_structural_chunker.py`:
   - `test_build_declaration_map()` — parse mock query_code results
   - `test_chunk_at_declaration_boundaries()` — verify no declaration split, full coverage
   - `test_structural_context_complete()` — small class fully in one chunk
   - `test_structural_context_continues()` — large class spanning multiple chunks
   - `test_structural_context_starts_ends()` — class boundary at chunk edge
   - `test_empty_query_results()` — graceful fallback
   - `test_nested_classes()` — inner class inside outer class

2. **Integration test** — Run on HeijunkaData.cs (3675 lines, 17 classes):
   - Verify 6 chunks at ~600 lines each
   - Verify LinePitch class shows Starts/Continues/Ends across chunks
   - Verify small classes show Complete
   - Verify member counts are accurate

3. **Regression test** — Run on existing COBOL test files without `chunking` config:
   - Verify fallback to ctags/regex works
   - Verify no behavioral change

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| `query_code` MCP tool not available | Fallback chain to ctags → regex |
| `.scm` query syntax wrong for a language | Config-driven; user can fix without code change |
| Very large files (>10K lines) produce too many matches | `query_code` already handles this (tested at 3675 lines, 434 matches, 537KB result) |
| Member without `.name` capture (e.g., `field_declaration`) | Extract name from `.def` text or use positional fallback |
| Nested classes (class inside class) | Range-containment algorithm naturally handles nesting — inner class is a "member" of outer class |
| COBOL has no class/member concept | COBOL query uses section/paragraph captures mapped to container/member roles |
