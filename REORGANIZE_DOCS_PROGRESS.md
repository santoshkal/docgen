# Reorganize Documentation - Progress Tracker

## Overview

**Branch**: `reorganize-docs`
**Started**: 2025-12-12
**Status**: In Progress

### Objective

Refactor the documentation generation to use a two-phase approach:
1. **Phase 1**: Generate Detailed Code Explanation (chunked source) → Extract prose
2. **Phase 2**: Generate other sections using prose + metadata (no raw source code)
3. **Phase 3**: Assemble final document

### Key Decisions

| Decision | Choice |
|----------|--------|
| Config approach | Replace existing `full_context.enabled` behavior |
| Phase 2 execution | Sequential (parallel planned for future) |
| Tmp file location | Fixed: `./tmp/{program_name}/` |
| Cleanup | Remove tmp files after successful assembly |
| Error handling | Continue on section failure, mark in output |
| `full_context_prompts.py` | Skip entirely, use template YAML directly |

---

## Progress Summary

| Phase | Status | Progress |
|-------|--------|----------|
| Setup & Planning | Complete | 2/2 |
| Phase 1 Implementation | Complete | 4/4 |
| Phase 2 Implementation | Complete | 4/4 |
| Phase 3 Implementation | Complete | 2/2 |
| Integration & Testing | In Progress | 1/3 |

---

## Detailed Task List

### Setup & Planning

| Task ID | Description | Status | Notes |
|---------|-------------|--------|-------|
| S-1 | Create `reorganize-docs` branch | Done | |
| S-2 | Create progress tracker document | Done | This file |

### Phase 1: Code Explanation Generation

| Task ID | Description | Status | Notes |
|---------|-------------|--------|-------|
| P1-1 | Create `extract_prose_from_explanation()` function | Done | Lines 3074-3100 in cobol_doc_agent.py |
| P1-2 | Create tmp file helpers (`save_tmp`, `load_tmp`, `cleanup_tmp`) | Done | Lines 3013-3071 in cobol_doc_agent.py |
| P1-3 | Create `run_phase1_code_explanation()` function | Done | Lines 3103-3183 in cobol_doc_agent.py |
| P1-4 | Unit test Phase 1 functions | Done | 16/16 tests passed |

### Phase 2: Section Generation with Prose Context

| Task ID | Description | Status | Notes |
|---------|-------------|--------|-------|
| P2-1 | Create `build_prose_based_context()` function | Done | Lines 3288-3343 in cobol_doc_agent.py |
| P2-2 | Create `run_phase2_sections()` function | Done | Lines 3186-3285 in cobol_doc_agent.py |
| P2-3 | Modify `build_section_context()` for prose mode | Done | Using new build_prose_based_context() |
| P2-4 | Handle section failures gracefully | Done | Creates placeholder on failure |

### Phase 3: Document Assembly

| Task ID | Description | Status | Notes |
|---------|-------------|--------|-------|
| P3-1 | Create `assemble_final_document()` function | Done | Lines 3346-3405 in cobol_doc_agent.py |
| P3-2 | Add tmp file cleanup after assembly | Done | cleanup_tmp() called after save |

### Integration & Testing

| Task ID | Description | Status | Notes |
|---------|-------------|--------|-------|
| I-1 | Create `generate_documentation_reorganized()` entry point | Done | Lines 3408-3560 in cobol_doc_agent.py |
| I-2 | Update config handling (remove old full_context logic) | Deferred | Not needed for initial test |
| I-3 | End-to-end test with TDAS-MINDISTCALC | Ready | test_reorganize_e2e.py created |

---

## File Changes Tracker

| File | Change Type | Status | Lines Changed |
|------|-------------|--------|---------------|
| `cobol_doc_agent.py` | Add + Modify | Done | +545 lines (3005-3550) |
| `full_context_builder.py` | No change needed | - | - |
| `config_loader.py` | Pending | Not Started | ~15 est |
| `full_context_prompts.py` | Skip (not used) | - | - |
| `context_strategy.py` | Skip (not used) | - | - |

---

## New Functions Added to `cobol_doc_agent.py`

| Function | Lines | Purpose |
|----------|-------|---------|
| `get_tmp_dir()` | 3013-3015 | Get tmp directory path |
| `save_to_tmp()` | 3018-3038 | Save content to tmp |
| `load_from_tmp()` | 3041-3057 | Load content from tmp |
| `cleanup_tmp()` | 3060-3071 | Remove tmp directory |
| `extract_prose_from_explanation()` | 3074-3100 | Strip code blocks from explanation |
| `run_phase1_code_explanation()` | 3103-3183 | Phase 1: Generate code explanation |
| `run_phase2_sections()` | 3186-3285 | Phase 2: Generate other sections |
| `build_prose_based_context()` | 3288-3343 | Build context with prose + metadata |
| `assemble_final_document()` | 3346-3405 | Phase 3: Combine sections |
| `generate_documentation_reorganized()` | 3408-3548 | Main entry point |

---

## Changelog

| Date | Task ID | Description |
|------|---------|-------------|
| 2025-12-12 | S-1 | Created `reorganize-docs` branch |
| 2025-12-12 | S-2 | Created progress tracker document |
| 2025-12-12 | P1-1 | Implemented `extract_prose_from_explanation()` |
| 2025-12-12 | P1-2 | Implemented tmp file helpers |
| 2025-12-12 | P1-3 | Implemented `run_phase1_code_explanation()` |
| 2025-12-12 | P2-1 | Implemented `build_prose_based_context()` |
| 2025-12-12 | P2-2 | Implemented `run_phase2_sections()` |
| 2025-12-12 | P2-4 | Added failure handling in run_phase2_sections() |
| 2025-12-12 | P3-1 | Implemented `assemble_final_document()` |
| 2025-12-12 | P3-2 | Added cleanup_tmp() call after assembly |
| 2025-12-12 | I-1 | Implemented `generate_documentation_reorganized()` |
| 2025-12-12 | P1-4 | Unit tests passed (16/16) in tests/test_reorganize_docs.py |

---

## Bug Fixes (2025-12-12)

| Issue | Root Cause | Fix |
|-------|------------|-----|
| Phase 1 not chunking | `enable_source_extraction` not in state | Added parameter to `generate_documentation()` + passed from main |
| Phase 2 context 7.4MB | Raw metadata included in context | Removed raw metadata from `build_prose_based_context()` |
| Import error | Wrong function name | Changed `generate_program_map` → `generate_cobol_program_map` |
| LLM tracer not working | `init_tracer`/`finalize_tracer` never called | Added tracer init at start, finalize after doc saved |

---

## New Feature: Mermaid Validation (Per-Section in Phase 2)

**Added**: 2025-12-16
**Updated**: 2025-12-18 - Moved from Phase 2.5 to per-section validation in Phase 2

**Flow**:
```
Phase 1: Generate Code Explanation → Extract Prose
Phase 2: For each section:
         1. Generate section document
         2. If has mermaid → Validate via MCP
         3. If invalid → LLM fix with section context
         4. Write fixed mermaid back to section
Phase 3: Assemble Final Document
```

**Key Improvement (2025-12-18)**:
- Mermaid validation now happens INSIDE Phase 2 loop, not after
- Full section document passed as context to LLM for fixing
- This allows LLM to understand diagram's purpose from surrounding content

**New Files**:
- `mermaid_validator.py` - Mermaid validation using MCP server + LLM fix
- `tests/test_mermaid_validator.py` - 9 unit tests (all passing)

**Key Functions**:
- `validate_section_mermaid_sync()` - Called per-section in Phase 2
- `fix_mermaid_with_llm(code, error, section_content)` - Uses section context

**How it works**:
1. After generating each section, check for ```mermaid blocks
2. Validate each block via MCP server (Docker: `mermaid-mcp:test`)
3. If invalid: Pass (mermaid + error + FULL section doc) to LLM for fix
4. Write fixed mermaid back to section at exact position
5. Continue to next section
6. Summary printed at end of Phase 2

---

## Next Steps

1. ~~Implement core functions~~ Done
2. ~~Write unit test for `extract_prose_from_explanation()` (P1-4)~~ Done (16/16 passed)
3. ~~Bug fixes for chunking and context size~~ Done (16/16 tests pass)
4. ~~LLM tracer integration~~ Done (init at start, finalize after doc saved)
5. ~~Mermaid validation~~ Done (25/25 tests pass, moved to per-section in Phase 2)
6. End-to-end test with TDAS-MINDISTCALC (I-3) - Ready to test
