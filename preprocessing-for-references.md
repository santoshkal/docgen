# Preprocessing for Rich Inter-File Relationships

## Analysis of Metadata Files in `metadata-5p`

### File-by-File Breakdown

| File | What it contains | Relationships? |
|------|-----------------|----------------|
| **treesitter-graph/graph.json** | 682 nodes with edges | **Intra-file only** — edges are `class→method`, `class→field`, `class→property`, `class→constructor`. All within `SequenceManager.cs`. No cross-file edges. |
| **structural_outline/SequenceManager.json** | Class list with inheritance patterns in `pattern` field | **Partial** — patterns show base classes (e.g., `TruckLoader : AbstractSequenceLoader`), but only for one file. |
| **ctags/csharp-project.tags** | 29,918 tags across **374 files** | **Best candidate for inter-file** — has every symbol across the entire project with file locations, kinds, namespaces, and inheritance patterns. |
| **syntax_tree/SequenceManager.json** | Full AST (39K lines) | Structural only, no relationship info. |
| **chunking_boundaries/SequenceManager.json** | Same as graph.json wrapped with metadata | Duplicate of treesitter-graph. |
| **symbol_table/SequenceManager.json** | Error — MCP tool failed | No data. |
| **project_tags.json** | Just ctags generation metadata | No relationship data. |

### Key Finding

**None of these files directly capture inter-file relationships.** Here's what's missing:

1. **treesitter-graph** only has containment edges (class owns method) within a single file. It doesn't track "method X calls method Y" or "class A in file1 uses type B from file2."

2. **ctags** has the raw material (all symbols + their files + inheritance in patterns) but it's a flat index — it records *definitions* only, not *references/usages*.

## What Preprocessing Would Produce a Rich Relationships Doc

A preprocessing step is needed. Here's what we suggest:

### 1. Inheritance/Interface Graph (extractable now from ctags)

Parse the `: BaseClass` patterns from ctags to build:
```
TruckLoader → AbstractSequenceLoader → ISequenceLoader
BatchContainerLoader → AbstractSequenceLoader
SequenceManager → MarshalByRefObject, IManageableService
```
This is **inter-file** — base classes often live in different files.

### 2. Cross-File Reference Index (requires new extraction)

ctags only records definitions. To get *who calls/uses what*, you'd need one of:
- **tree-sitter `query_code`** with reference queries (`.scm` files with `name.reference.*` patterns) — this is what the Aider approach in our plan uses
- **Roslyn analyzer** (for C# specifically) — gives precise call graphs, type resolution
- **Simple grep/ripgrep scan** — search each symbol name across all 374 files to find usage sites (crude but effective)

### 3. Namespace Dependency Map (extractable now from ctags)

Group symbols by namespace + file, then trace which namespaces appear as base types in other namespaces. This gives a high-level module dependency view.

## Recommended Approach: Two-Pass Preprocessor

### Pass 1 — Static (from existing metadata)
- Parse ctags inheritance patterns → build class hierarchy graph
- Group by namespace/file → build namespace dependency map
- Merge with treesitter-graph → attach members to each class node

### Pass 2 — Dynamic (new extraction needed)
- Run tree-sitter reference queries (`.scm` with `name.reference.*`) across all 374 files
- OR use ripgrep to find where each defined symbol is referenced in other files
- Build a weighted cross-file reference graph (this is the Aider PageRank input)

## Output: `relationships.json`

The output would be a single `relationships.json` with:
- `inheritance_graph`: class → base classes/interfaces (with files)
- `namespace_dependencies`: namespace A depends on namespace B
- `cross_file_references`: symbol X defined in file A, used in files B, C, D (with line numbers)
- `call_graph`: method X calls method Y (if tree-sitter queries support it)

This is essentially the foundation for the PageRank-based repo map described in `Aider-implementation.md`.

---

## MCP Server Tool Inventory for Relationship Extraction

### Tree-sitter-MCP Server (`~/mcp-servers/tree-sitter-mcp-server`) — 12 Tools

| Tool | Purpose | Cross-file Potential |
|------|---------|---------------------|
| **`get_dependencies`** | Extracts import/using statements + module names from a source file | **High** — call on every file, aggregate to build import dependency graph |
| **`get_symbols`** | Extracts functions, classes, methods, interfaces with name/line/column | **High** — build project-wide symbol table (name → file:line) |
| **`query_code`** | Run custom tree-sitter S-expression queries on source code | **High** — write queries for call expressions, type references, base classes |
| **`find_pattern`** | Find matches for custom tree-sitter query patterns | **High** — flexible custom semantic extraction |
| **`get_query_template`** | Pre-built query templates (functions, classes, imports, interfaces, etc.) | Templates available for 8+ languages |
| **`build_query`** | Combine multiple query templates into a single query | Convenience for multi-pattern extraction |
| **`list_query_templates`** | List available templates per language | Discovery |
| `generate_ast` | Full AST of source code | Too noisy for relationships |
| `generate_graph` | JSON graph of syntax tree | Structural, not semantic |
| `get_node_at_position` | Find AST node at row/column | Point queries |
| `analyze_complexity` | Cyclomatic complexity, LOC, function/class counts | Metrics, not relationships |
| `list_languages` | List 100+ supported languages | Discovery |

### Tree-sitter-Graph-MCP Server (`~/mcp-servers/tree-sitter-graph-mcp-server`) — 1 Tool

| Tool | Purpose | Cross-file Potential |
|------|---------|---------------------|
| **`tree_sitter_graph`** | Run `.tsg` (Tree-sitter Graph) query files to produce node+edge JSON graphs | **Medium** — `.tsg` format can define rich edge relationships (class→method, function→call_target, class→base_class) but operates on single files only |

The `.tsg` format is more powerful than S-expressions for defining **edges** between AST nodes, but requires writing custom `.tsg` query files per language.

### Key Insight: Neither Server Does Cross-File Natively

Both servers are single-file tools. To get inter-file relationships, we need an **orchestration layer**.

---

## Revised Three-Pass Preprocessor (Using MCP Tools)

### Pass 1 — Collect (per-file, using existing MCP tools)

For each source file in the project:

1. **`get_dependencies(source_file)`** → extract `using`/`import` statements
   - Output: `{file: "SequenceManager.cs", imports: ["System", "ng.server", "ng.data"]}`

2. **`get_symbols(source_file)`** → extract all definitions
   - Output: `{file: "SequenceManager.cs", symbols: [{name: "TruckLoader", kind: "class", line: 5925}, ...]}`

3. **`query_code(source_code, language, pattern)`** with call-expression patterns → extract function/method calls
   - C# pattern: `(invocation_expression function: (member_access_expression name: (identifier) @call_target))`
   - Output: `{file: "SequenceManager.cs", calls: [{target: "getInstance", line: 200}, ...]}`

4. **`query_code`** with base-class patterns → extract inheritance
   - C# pattern: `(class_declaration bases: (base_list (identifier) @base_class))`
   - Output: `{file: "SequenceManager.cs", inherits: [{class: "TruckLoader", base: "AbstractSequenceLoader"}, ...]}`

### Pass 2 — Resolve (cross-file linking)

Using the aggregated outputs from Pass 1:

1. **Build symbol table**: `{symbol_name → [{file, line, kind}, ...]}` from all `get_symbols` results
2. **Resolve imports**: Match `using` namespaces to files containing that namespace
3. **Resolve call targets**: Match unresolved call names against symbol table → cross-file edges
4. **Resolve inheritance**: Match base class names to their definition files
5. **Supplement with ctags**: Use existing `csharp-project.tags` for symbols missed by tree-sitter (ctags has 29,918 entries across 374 files)

### Pass 3 — Output (`relationships.json`)

```json
{
  "inheritance_graph": {
    "TruckLoader": {
      "defined_in": "Sequencing/SequenceManager.cs:5925",
      "base_classes": ["AbstractSequenceLoader"],
      "base_defined_in": ["Sequencing/SequenceManager.cs:5065"]
    }
  },
  "namespace_dependencies": {
    "ng.data.requirements": ["ng.server", "ng.data", "ng.clients", "System"]
  },
  "cross_file_references": {
    "DefaultScriptCommand": {
      "defined_in": "ScriptEngine/DefaultScriptCommand.cs",
      "referenced_by": [
        "DataCommands/PickList.cs:AddBulkPartsToPickList",
        "ScriptCommands/standardCommands.cs:AddDataToAgentQualifiedList"
      ]
    }
  },
  "call_graph": {
    "SequenceManager.getInstance": {
      "defined_in": "Sequencing/SequenceManager.cs:200",
      "called_from": ["Sequencing/Commands.cs:45", "Heijunka/HeijunkaManager.cs:120"]
    }
  },
  "file_dependencies": {
    "Sequencing/SequenceManager.cs": {
      "depends_on": ["ScriptEngine/DatabaseObject.cs", "ScriptEngine/ServiceManager.cs"],
      "depended_on_by": ["Sequencing/Commands.cs", "SequencingJobs/JobLoaders.cs"]
    }
  },
  "statistics": {
    "total_files": 374,
    "total_symbols": 29918,
    "total_edges": 0,
    "pagerank_ready": true
  }
}
```

### Implementation Notes

- The `get_symbols` tool failed in initial metadata generation due to a parameter bug (`source_code` was passed instead of `source_file`). This needs fixing in the MCP tool invocation config.
- For C# specifically, writing custom tree-sitter S-expression queries for `invocation_expression` and `object_creation_expression` will capture most call-site references.
- The `.tsg` format in tree-sitter-graph could produce richer intra-file graphs (with edge labels like "calls", "inherits", "implements") but requires writing C#-specific `.tsg` files.
- PageRank can be run on the `cross_file_references` + `call_graph` data to rank symbols by importance — this is the Aider approach.

---

## MultilsPy MCP Server — LSP-Based Project-Wide Relationship Extraction

### Why MultilsPy Changes the Picture

The `multilspy-mcp-server` (`~/mcp-servers/multilspy-mcp-server`) wraps Microsoft Research's [MultilsPy](https://github.com/microsoft/multilspy) library to expose LSP (Language Server Protocol) operations as MCP tools. Unlike tree-sitter (which parses syntax) or ctags (which indexes definitions), **LSP provides semantic understanding** — it knows types, resolves symbols across files, and can trace references through the entire workspace.

This means we can get **cross-file relationships natively** without building a custom orchestrator.

### Supported Languages

11 languages via auto-downloaded language servers:

| Language | LSP Server | File Extensions |
|----------|-----------|-----------------|
| **C#** | OmniSharp (requires .NET) | `.cs` |
| Python | jedi-language-server / pylsp | `.py` |
| Java | jdtls | `.java` |
| TypeScript | tsserver | `.ts`, `.tsx` |
| JavaScript | tsserver | `.js`, `.jsx` |
| Go | gopls | `.go` |
| Rust | rust-analyzer | `.rs` |
| C/C++ | clangd | `.cpp`, `.cc`, `.h`, `.hpp` |
| Ruby | solargraph | `.rb` |
| Dart | dart analyze | `.dart` |
| Kotlin | kotlin-language-server | `.kt` |

**Note:** COBOL is not supported. For COBOL projects, continue using SuperBol LSP + ctags. For the C# IMES codebase, multilspy with OmniSharp is the ideal fit.

### Tools Relevant to Relationship Extraction

#### 1. `code_find_references(file_path, line, column)` — **The Key Tool**

Finds every location where a symbol is used across the **entire workspace**.

```
Input:  file_path="Sequencing/SequenceManager.cs", line=5065, column=20
        (pointing at AbstractSequenceLoader class definition)
Output: [
  {uri: "Sequencing/SequenceManager.cs", line: 5925},  // TruckLoader extends it
  {uri: "Sequencing/SequenceManager.cs", line: 6017},  // TruckSummaryLoader extends it
  {uri: "Sequencing/SequenceManager.cs", line: 6103},  // LoadingBatchContainers extends it
  {uri: "SequencingJobs/JobLoaders.cs", line: 42},      // cross-file usage
  ...
]
```

This directly gives us **inter-file reference edges** — no grep, no heuristic matching.

#### 2. `code_navigate_definition(file_path, line, column)` — Resolve Where Things Come From

Given a usage site, returns the **definition location** (possibly in another file).

```
Input:  file_path="DataCommands/PickList.cs", line=10, column=45
        (pointing at DefaultScriptCommand in "class AddBulkPartsToPickList : DefaultScriptCommand")
Output: {uri: "ScriptEngine/DefaultScriptCommand.cs", line: 15, column: 4}
```

This resolves inheritance and type references to their **actual definition files**.

#### 3. `code_document_symbols(file_path)` — Intra-File Structure

Returns all symbols in a file with hierarchical nesting (classes containing methods, etc.).

```
Output: {
  symbols: [
    {name: "SequenceManager", kind: CLASS, children: [
      {name: "getInstance", kind: METHOD},
      {name: "TriggerEvent", kind: METHOD},
      ...
    ]},
    {name: "TruckLoader", kind: CLASS, children: [...]},
  ]
}
```

This gives us the **intra-file containment graph** (same as treesitter-graph but semantically resolved).

#### 4. `code_search_workspace(query)` — Project-Wide Symbol Search

Searches all symbols across the workspace matching a query string.

```
Input:  query="Loader", limit=100
Output: [
  {name: "TruckLoader", kind: CLASS, file: "Sequencing/SequenceManager.cs"},
  {name: "TruckSummaryLoader", kind: CLASS, file: "Sequencing/SequenceManager.cs"},
  {name: "AbstractSequenceLoader", kind: CLASS, file: "Sequencing/SequenceManager.cs"},
  {name: "JobLoaders", kind: CLASS, file: "SequencingJobs/JobLoaders.cs"},
  ...
]
```

Useful for discovering all symbols of a certain type/pattern across the project.

#### 5. `code_get_hover(file_path, line, column)` — Type Info & Documentation

Returns type signatures, documentation, and resolved type info for a symbol.

```
Input:  file_path="Sequencing/SequenceManager.cs", line=200, column=10
Output: {contents: "public static SequenceManager getInstance()\nReturns the singleton instance..."}
```

Useful for enriching relationship data with type signatures.

### Workspace Initialization

```bash
# Option 1: Environment variable (auto-init on server start)
export WORKSPACE_ROOT=/path/to/csharp-project

# Option 2: Explicit tool call
lsp_initialize(workspace_root="/path/to/csharp-project")
```

- Language servers are **auto-downloaded** on first use (OmniSharp for C# requires .NET runtime)
- One LSP server instance per language, reused across requests
- Session can be saved/restored via `lsp_save_session` / `lsp_load_session`

### Leveraging MultilsPy for the Relationship Preprocessor

With multilspy, the three-pass preprocessor simplifies significantly:

#### Revised Pass 1 — Collect Symbols (per-file)

For each source file, call `code_document_symbols(file_path)`:
- Returns hierarchical symbol tree (classes → methods → fields)
- Builds the **intra-file containment graph** directly
- No need for treesitter-graph or ctags for this step

#### Revised Pass 2 — Collect Cross-File References (per-symbol)

For each "important" symbol (classes, interfaces, public methods), call `code_find_references(file_path, line, column)`:
- Returns all usage locations across the workspace
- Each reference in a **different file** = an inter-file edge
- Weighted by reference count = PageRank input

For inheritance resolution, call `code_navigate_definition` on base class references:
- Resolves `class TruckLoader : AbstractSequenceLoader` to the exact file/line of `AbstractSequenceLoader`

#### Pass 3 — Output (`relationships.json`)

Same output structure as before, but now with **semantically resolved** data:
- Inheritance edges are precise (not pattern-matched from ctags strings)
- Cross-file references are complete (not grep-approximated)
- Call targets are type-resolved (not just name-matched)

### Comparison: Tree-sitter vs MultilsPy for Relationships

| Capability | tree-sitter + ctags | multilspy (LSP) |
|-----------|-------------------|-----------------|
| Intra-file structure | Syntax-level (AST nodes) | Semantic-level (resolved types) |
| Cross-file references | Not available (need grep) | **Native via `find_references`** |
| Inheritance resolution | Pattern matching on `: BaseClass` | **Precise via `navigate_definition`** |
| Call graph | Unresolved name matching | **Type-resolved via LSP** |
| Overload resolution | Cannot distinguish | **Handles correctly** |
| Namespace resolution | Heuristic from ctags | **Full semantic resolution** |
| Setup complexity | Low (just parse files) | Medium (needs language server + .NET for C#) |
| Speed | Fast (no server startup) | Slower (LSP server init) |
| Language coverage | Any language with tree-sitter grammar | 11 languages with LSP servers |

### Recommended Hybrid Approach

Use **both** — multilspy for precision, tree-sitter/ctags for breadth:

1. **MultilsPy** for the target file being documented:
   - `code_find_references` on all public symbols → precise cross-file edges
   - `code_navigate_definition` on all base classes/interfaces → resolved inheritance
   - `code_get_hover` on key symbols → type signatures for documentation

2. **ctags** for project-wide context:
   - Already indexed 29,918 symbols across 374 files
   - Fast lookup for "where is this symbol defined?"
   - Fallback when LSP is slow or unavailable

3. **tree-sitter** for structural chunking:
   - Continue using for source code chunking in Phase 1
   - AST-level structure doesn't need semantic resolution

### Architecture

```
┌─────────────────────────────────────────────┐
│         Relationship Preprocessor           │
│                                             │
│  1. Walk source files in project            │
│  2. For each file:                          │
│     ├─ code_document_symbols() → symbols    │
│     └─ For each symbol:                     │
│        ├─ code_find_references() → refs     │
│        └─ code_navigate_definition() → def  │
│  3. Aggregate into relationships.json       │
│  4. Run PageRank on reference graph         │
└──────────────────┬──────────────────────────┘
                   │
    ┌──────────────▼──────────────┐
    │    multilspy-mcp-server     │
    │    (MCP over LSP)           │
    └──────────────┬──────────────┘
                   │ LSP Protocol
    ┌──────────────▼──────────────┐
    │    OmniSharp (C#)           │
    │    Workspace: /project      │
    │    374 files indexed        │
    └─────────────────────────────┘
```
