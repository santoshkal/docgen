# Aider Repo Map — Insights for Enhancing Our Program Map

Reference: https://aider.chat/2023/10/22/repomap.html

## Key Insights from Aider's Approach

### 1. Graph-Based Ranking with PageRank

Aider builds a **cross-file reference graph** (NetworkX `MultiDiGraph`):
- **Nodes** = files
- **Edges** = identifier references between files, weighted by frequency
- Runs **PageRank** to find the most "important" symbols — those referenced most by other code

Our program map lists symbols in order of appearance. For multi-file projects, PageRank could help prioritize what context to include.

### 2. Definitions vs References Distinction

Aider uses tree-sitter `.scm` query files to classify every symbol as:
- **Definition** (`name.definition.*`) — where a function/class is declared
- **Reference** (`name.reference.*`) — where it's used

This enables the reference graph: "function X is *defined* in file A but *used* in files B, C, D."

Our current AST filter doesn't distinguish definitions from references — we just filter by line range.

### 3. Weighted Importance Scoring

Aider applies multipliers:
- **50x** boost for symbols in files the user is actively editing
- **10x** for `snake_case`/`camelCase` names (likely user-defined, not library)
- **0.1x** penalty for `_private` identifiers
- PageRank score from the reference graph

### 4. Token Budget via Binary Search

Instead of a fixed heuristic, Aider uses **binary search** to find the maximum number of ranked symbols that fit within `--map-tokens` (default 1K). Tests mid-point, counts tokens, adjusts — converges within 15% of target.

Our program map uses `token_budget // 50` for methods. Binary search would be more precise.

### 5. Tree-Sitter `.scm` Tag Queries

Aider doesn't walk raw ASTs. It uses **tag query files** (`.scm`) — language-specific grammars for extracting only meaningful symbols. Far more precise than walking generic AST JSON.

### 6. Output Format: Code Signatures, Not Just Names

Aider's map shows actual **code signatures with parameters** using `TreeContext` (surrounding source lines), not just `- MethodName() (line 42)`. Gives the LLM much richer structural context.

Example output:
```
aider/coders/base_coder.py:
⋮...
│class Coder:
│    abs_fnames = None
⋮...
│    @classmethod
│    def create(
│        self,
│        main_model,
│        edit_format,
│        io,
│        skip_model_availabily_check=False,
│        **kwargs,
⋮...
```

### 7. Libraries Used

- **networkx** — Graph algorithms (PageRank, MultiDiGraph)
- **grep_ast** — Tree-sitter wrapper, TreeContext rendering
- **tree-sitter** — AST parsing
- **diskcache** — SQLite-backed tag caching
- **pygments** — Fallback token/reference extraction

---

## What We Already Do Well

- Program map is per-file (appropriate for Phase 1 chunk processing)
- Language adapter abstraction makes it extensible
- AST filtering per chunk (Aider doesn't do this — it works at repo level)
- Token budget control exists (simpler but functional)

---

## Actionable Enhancements (Priority Order)

| # | Enhancement | Effort | Impact | Notes |
|---|------------|--------|--------|-------|
| 1 | Add method signatures (params, return types) to program map | Medium | High | LLM gets richer structural context |
| 2 | Use tree-sitter `.scm` queries for precise symbol extraction | High | High | Language-specific, replaces generic AST walk |
| 3 | Add reference counting (call frequency per symbol) | Medium | Medium | Helps prioritize what to show in budget |
| 4 | Binary search for token budget fitting | Low | Low | Current heuristic works but less precise |
| 5 | PageRank across files for multi-file projects | High | Medium | Most useful when we support cross-file docs |
| 6 | Show code signatures in `TreeContext` style (source lines) | Medium | High | Like Aider's `⋮...│` format |
