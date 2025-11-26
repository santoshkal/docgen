# Orchestrator Enhancement - Progress Tracker

> **Project Start Date**: 2025-11-26
> **Target Completion**: TBD
> **Current Phase**: Phase 3 - Agent Enhancement

---

## 🎯 Project Overview

Transform single-file COBOL documentation agent into a project-level orchestrator with:
- Parallel agent execution via Ray
- Project-wide metadata generation
- Inter-file relationship documentation
- Batch processing support
- Real-time progress tracking

---

## 📈 Overall Progress

```
Phase 0: Foundation      [██████████] 100% ✅
Phase 1: Tree MCP        [██████████] 100% ✅
Phase 2: Metadata        [██████████] 100% ✅
Phase 3: Agent           [░░░░░░░░░░] 0%   ← CURRENT
Phase 4: Orchestration   [░░░░░░░░░░] 0%
Phase 5: Progress        [░░░░░░░░░░] 0%
Phase 6: Error Handling  [░░░░░░░░░░] 0%
Phase 7: Output          [░░░░░░░░░░] 0%
Phase 8: Summary         [░░░░░░░░░░] 0%
Phase 9: Integration     [░░░░░░░░░░] 0%
Phase 10: Documentation  [░░░░░░░░░░] 0%
─────────────────────────────────────
TOTAL                    [███░░░░░░░] 26% (19/74 tasks)
```

---

## 📅 Implementation Log

### 2025-11-26
- ✅ Created KanBan task board (ORCHESTRATOR_KANBAN.md)
- ✅ Created Progress tracker (this file)
- ✅ **Phase 0 Complete**:
  - P0-1: Added Ray>=2.40.0 to requirements.txt
  - P0-2: Created `./reports` directory with .gitkeep
  - P0-3: Created `./metadata` directory with .gitkeep
  - P0-4: Extended config.example.yaml with orchestrator section (~150 lines)
  - P0-5: Created orchestrator_config.py (config validator, 370 lines)
  - P0-5: Created tests/test_orchestrator_config.py (33 tests, all passing)
- ✅ **Phase 1 Complete**:
  - P1-1: Created TreeMCPClient class (tree_mcp_client.py, ~400 lines)
  - P1-2: Implemented tree_json_output tool invocation via Docker
  - P1-3: Added file extension filtering (.cbl, .cob, .cpy, .c74)
  - P1-4: Implemented JSON tree parsing to extract files recursively
  - P1-5: Added write_file_list() to save results to ./metadata
  - P1-6: Created tests/test_tree_mcp_client.py (29 tests, all passing)
- ✅ **Phase 2 Complete**:
  - P2-1: Created ProjectMetadataGenerator class (project_metadata_generator.py, ~500 lines)
  - P2-2: Implemented per-file metadata generation loop with CTags, GnuCOBOL, SuperBOL
  - P2-3: Added cobol_generate_cfg_project (SuperBOL project-level CFG)
  - P2-4: Added extract_relationship directory mode (GnuCOBOL project relationships)
  - P2-5: Added extract_cross_references_tool per-file extraction
  - P2-6: Structured metadata storage in ./metadata/{ctags,gnucobol,superbol}
  - P2-7: Created MetadataCacheManager (metadata_cache.py, ~350 lines) with:
    - SHA256 checksums for change detection
    - Skip unchanged files
    - SharedMetadataReader for efficient parallel access
  - P2-8: Created tests/test_project_metadata.py (32 tests, all passing)
- ⏳ Starting Phase 3: Agent Enhancement

---

## 🏗️ Phase Details

### Phase 0: Foundation & Setup (5/5 tasks) ✅

| Task | Status | Notes |
|------|--------|-------|
| P0-1: Add Ray to requirements.txt | ✅ Done | ray>=2.40.0 |
| P0-2: Create `./reports` directory | ✅ Done | With .gitkeep |
| P0-3: Create `./metadata` directory | ✅ Done | With .gitkeep |
| P0-4: Extend config schema | ✅ Done | ~150 lines added to config.example.yaml |
| P0-5: Config validator | ✅ Done | orchestrator_config.py (370 lines, 33 tests) |

**Phase Notes**: Foundation complete. All tests passing.

---

### Phase 1: Tree MCP Integration (6/6 tasks) ✅

| Task | Status | Notes |
|------|--------|-------|
| P1-1: TreeMCPClient class | ✅ Done | tree_mcp_client.py (~400 lines) |
| P1-2: tree_json_output invocation | ✅ Done | Via mcp-use + Docker |
| P1-3: File extension filtering | ✅ Done | .cbl, .cob, .cpy, .c74 |
| P1-4: Parse JSON to file list | ✅ Done | Recursive directory traversal |
| P1-5: Write file list | ✅ Done | JSON output to ./metadata |
| P1-6: Unit tests | ✅ Done | 29 tests, all passing |

**Phase Notes**: Complete. TreeMCPClient ready for orchestrator integration.

---

### Phase 2: Metadata Generation (8/8 tasks) ✅

| Task | Status | Notes |
|------|--------|-------|
| P2-1: Refactor MCP client | ✅ Done | ProjectMetadataGenerator class |
| P2-2: Per-file metadata loop | ✅ Done | generate_per_file_metadata() |
| P2-3: cobol_generate_cfg_project | ✅ Done | SuperBOL project CFG |
| P2-4: extract_relationship (dir) | ✅ Done | GnuCOBOL directory mode |
| P2-5: extract_cross_references | ✅ Done | Per-file cross-refs |
| P2-6: Save to ./metadata | ✅ Done | Structured naming |
| P2-7: Metadata caching | ✅ Done | MetadataCacheManager, SharedMetadataReader |
| P2-8: Unit tests | ✅ Done | 32 tests, all passing |

**Phase Notes**: Complete. Project metadata pipeline ready.

---

### Phase 3: Agent Enhancement (0/8 tasks)

| Task | Status | Notes |
|------|--------|-------|
| P3-1: AgentWorker class | ⬜ Pending | Ray-compatible |
| P3-2: Remove MCP from agent | ⬜ Pending | One-time pre-step |
| P3-3: Metadata file reading | ⬜ Pending | |
| P3-4: Inter-file relationships | ⬜ Pending | New section |
| P3-5: Agent ID assignment | ⬜ Pending | File-name based |
| P3-6: Heartbeat mechanism | ⬜ Pending | |
| P3-7: Per-agent logging | ⬜ Pending | To ./reports |
| P3-8: Unit tests | ⬜ Pending | |

**Agent Changes**:
- MCP step removed (metadata pre-generated)
- New "Inter-file relationships" section added
- All existing functionality preserved (3-pass, chunking, tracing)

---

### Phase 4: Ray Orchestration (0/9 tasks)

| Task | Status | Notes |
|------|--------|-------|
| P4-1: Orchestrator class | ⬜ Pending | Main entry point |
| P4-2: Ray init (local) | ⬜ Pending | |
| P4-3: Distributed option | ⬜ Pending | Low priority |
| P4-4: Batch creation | ⬜ Pending | |
| P4-5: Sequential batch exec | ⬜ Pending | Batch 1 → 2 → ... |
| P4-6: Agent spawning | ⬜ Pending | Ray remote |
| P4-7: Resource allocation | ⬜ Pending | |
| P4-8: Circuit breaker | ⬜ Pending | 5 consecutive fails |
| P4-9: Unit tests | ⬜ Pending | |

**Batch Configuration**:
```yaml
orchestrator:
  batch_mode: batch  # 'batch' or 'all'
  batch_size: 10     # Ignored if batch_mode = 'all'
```

---

### Phase 5: Progress Tracking (0/8 tasks)

| Task | Status | Notes |
|------|--------|-------|
| P5-1: ProgressTracker class | ⬜ Pending | File locking |
| P5-2: Markdown format | ⬜ Pending | |
| P5-3: Real-time updates | ⬜ Pending | |
| P5-4: Tiktoken integration | ⬜ Pending | Token usage |
| P5-5: Batch tracking | ⬜ Pending | |
| P5-6: Agent-file mapping | ⬜ Pending | Persists across runs |
| P5-7: Zombie detection | ⬜ Pending | |
| P5-8: Unit tests | ⬜ Pending | |

**Progress File Location**: `./reports/project_progress.md`

---

### Phase 6: Error Handling (0/8 tasks)

| Task | Status | Notes |
|------|--------|-------|
| P6-1: Exponential backoff | ⬜ Pending | Start at 3s |
| P6-2: 3-retry logic | ⬜ Pending | |
| P6-3: Corrective retry (LLM) | ⬜ Pending | |
| P6-4: Memory monitoring | ⬜ Pending | |
| P6-5: Graceful degradation | ⬜ Pending | |
| P6-6: Failure report | ⬜ Pending | |
| P6-7: Race condition prevention | ⬜ Pending | |
| P6-8: Unit tests | ⬜ Pending | |

**Retry Strategy**:
1. First retry: 3 second delay
2. Subsequent: Exponential backoff (6s, 12s, ...)
3. Max retries: 3
4. On failure: Mark failed, continue, report at end

---

### Phase 7: Output Organization (0/4 tasks)

| Task | Status | Notes |
|------|--------|-------|
| P7-1: Directory mirroring | ⬜ Pending | Match source structure |
| P7-2: Create dirs before exec | ⬜ Pending | |
| P7-3: Agent output path | ⬜ Pending | |
| P7-4: Unit tests | ⬜ Pending | |

**Output Structure Example**:
```
source/                     docs/
├── main/                   ├── main/
│   ├── PROG1.cbl    →     │   ├── PROG1.md
│   └── PROG2.cbl    →     │   └── PROG2.md
└── copy/                   └── copy/
    └── COMMON.cpy   →         └── COMMON.md
```

---

### Phase 8: Project Summary (0/7 tasks)

| Task | Status | Notes |
|------|--------|-------|
| P8-1: SummaryGenerator class | ⬜ Pending | |
| P8-2: Aggregate relationships | ⬜ Pending | |
| P8-3: Core components | ⬜ Pending | |
| P8-4: Business logic | ⬜ Pending | |
| P8-5: Dependency graph | ⬜ Pending | Visualization |
| P8-6: Write summary MD | ⬜ Pending | |
| P8-7: Unit tests | ⬜ Pending | |

**Summary Contents**:
- Core components overview
- Business logic explanation
- Inter-file relationships
- Dependency graph
- Project statistics

---

### Phase 9: Integration Testing (0/7 tasks)

| Task | Status | Notes |
|------|--------|-------|
| P9-1: Integration test suite | ⬜ Pending | |
| P9-2: Small project test | ⬜ Pending | 3-5 files |
| P9-3: Batch mode test | ⬜ Pending | 10+ files |
| P9-4: Failure recovery test | ⬜ Pending | |
| P9-5: Backward compat test | ⬜ Pending | Single-file mode |
| P9-6: Performance profiling | ⬜ Pending | |
| P9-7: Memory analysis | ⬜ Pending | |

**Test Coverage Target**: 90%+ (aim for 100%)

---

### Phase 10: Documentation (0/4 tasks)

| Task | Status | Notes |
|------|--------|-------|
| P10-1: Update README.md | ⬜ Pending | Orchestrator usage |
| P10-2: Update config example | ⬜ Pending | |
| P10-3: Architecture diagram | ⬜ Pending | |
| P10-4: Code cleanup | ⬜ Pending | |

---

## 📊 Metrics

### Code Metrics
| Metric | Value |
|--------|-------|
| New files created | 9 |
| Files modified | 2 |
| Lines added | ~2100 |
| Lines removed | 0 |
| Test coverage | 94 tests passing |

### Token Usage (Will track during execution)
| Component | Tokens Used |
|-----------|-------------|
| Planning | TBD |
| Implementation | TBD |
| Testing | TBD |
| **Total** | **TBD** |

---

## 🗂️ File Inventory

### New Files to Create
| File | Purpose | Phase |
|------|---------|-------|
| `orchestrator.py` | Main orchestrator class | P4 |
| `tree_mcp_client.py` | Tree MCP Docker communication | P1 |
| `progress_tracker.py` | Progress tracking with locking | P5 |
| `project_summary_generator.py` | Project-level summary | P8 |
| `agent_worker.py` | Ray-compatible agent wrapper | P3 |
| `error_handlers.py` | Error handling utilities | P6 |
| `tests/test_orchestrator.py` | Orchestrator tests | P4 |
| `tests/test_tree_mcp.py` | Tree MCP tests | P1 |
| `tests/test_progress.py` | Progress tracker tests | P5 |
| `tests/test_integration.py` | Integration tests | P9 |

### Files to Modify
| File | Changes | Phase |
|------|---------|-------|
| `requirements.txt` | Add Ray | P0 |
| `config.example.yaml` | Add orchestrator config | P0, P10 |
| `cobol_doc_agent.py` | Remove MCP step, add inter-file section | P3 |
| `README.md` | Add orchestrator documentation | P10 |

### Directories to Create
| Directory | Purpose |
|-----------|---------|
| `./metadata` | Store generated metadata |
| `./reports` | Logs, metrics, progress tracker |
| `./docs` | Output documentation (mirrors source) |

---

## ⚠️ Known Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Race conditions on progress file | HIGH | File locking, atomic writes |
| Ray worker crashes | MEDIUM | Auto-retry, circuit breaker |
| Memory exhaustion | HIGH | Memory monitoring, adaptive batch |
| MCP server failures | MEDIUM | Per-tool retry, graceful skip |
| Token budget exceeded | MEDIUM | Efficient metadata strategy |

---

## 📞 Quick Reference

### Key Decisions
- **Batch execution**: Sequential (Batch 1 → Batch 2)
- **Agent ID**: File-name based, persists across runs
- **Output**: Mirrors source directory structure
- **Retries**: 3 max, exponential backoff from 3s
- **Ray**: Local cluster, distributed option available
- **Progress**: Markdown, real-time, in `./reports`

### Config Example
```yaml
orchestrator:
  enabled: true
  batch_mode: batch        # 'batch' or 'all'
  batch_size: 10
  ray:
    local: true
    num_cpus: null         # Auto-detect
  reports_dir: ./reports
  metadata_dir: ./metadata
```

---

## 📝 Session Notes

### Session 1 (2025-11-26)
- Reviewed clarifications.md - all questions answered
- Created KanBan board with 74 tasks across 10 phases
- Created this progress tracker
- Ready to begin implementation

---

*This document is updated in real-time during implementation.*
