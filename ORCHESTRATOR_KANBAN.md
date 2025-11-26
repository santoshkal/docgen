# Orchestrator Enhancement - KanBan Task Board

> **Last Updated**: 2025-11-26
> **Status**: Planning Complete - Ready for Implementation

---

## 📋 BACKLOG

### Phase 0: Foundation & Setup
| ID | Task | Priority | Estimate | Dependencies |
|----|------|----------|----------|--------------|
| P0-1 | Add Ray to requirements.txt (latest 2025 version) | HIGH | Small | None |
| P0-2 | Create `./reports` directory structure | HIGH | Small | None |
| P0-3 | Create `./metadata` directory structure | HIGH | Small | None |
| P0-4 | Extend config schema for orchestrator settings | HIGH | Medium | None |
| P0-5 | Create orchestrator configuration validator | MEDIUM | Medium | P0-4 |

### Phase 1: Tree MCP Integration
| ID | Task | Priority | Estimate | Dependencies |
|----|------|----------|----------|--------------|
| P1-1 | Create TreeMCPClient class for Docker communication | HIGH | Medium | None |
| P1-2 | Implement `tree_json_output` tool invocation | HIGH | Medium | P1-1 |
| P1-3 | Add COBOL file extension filtering (.cbl, .cob, .cpy) | HIGH | Small | P1-2 |
| P1-4 | Parse JSON tree output to file list | HIGH | Medium | P1-2 |
| P1-5 | Write file list to centralized location | HIGH | Small | P1-4 |
| P1-6 | Unit tests for Tree MCP integration | HIGH | Medium | P1-1 to P1-5 |

### Phase 2: Metadata Generation Pipeline
| ID | Task | Priority | Estimate | Dependencies |
|----|------|----------|----------|--------------|
| P2-1 | Refactor MCP client to support batch file processing | HIGH | Large | P1-4 |
| P2-2 | Implement per-file metadata generation loop | HIGH | Large | P2-1 |
| P2-3 | Add `cobol_generate_cfg_project` (SuperBOL) invocation | HIGH | Medium | P2-2 |
| P2-4 | Add `extract_relationship` directory mode (GnuCOBOL) | HIGH | Medium | P2-2 |
| P2-5 | Add `extract_cross_references_tool` invocation | HIGH | Medium | P2-2 |
| P2-6 | Save metadata to `./metadata` with structured naming | HIGH | Medium | P2-2 to P2-5 |
| P2-7 | Implement metadata caching/reuse strategy | MEDIUM | Medium | P2-6 |
| P2-8 | Unit tests for metadata pipeline | HIGH | Large | P2-1 to P2-7 |

### Phase 3: Agent Enhancement
| ID | Task | Priority | Estimate | Dependencies |
|----|------|----------|----------|--------------|
| P3-1 | Create `AgentWorker` class (Ray-compatible) | HIGH | Large | P0-1 |
| P3-2 | Remove MCP invocation from agent flow | HIGH | Medium | P3-1 |
| P3-3 | Add metadata file reading capability | HIGH | Medium | P3-2, P2-6 |
| P3-4 | Implement "Inter-file relationships" section generator | HIGH | Large | P3-3 |
| P3-5 | Add agent ID assignment (file-name based) | HIGH | Small | P3-1 |
| P3-6 | Implement agent heartbeat mechanism | MEDIUM | Medium | P3-1 |
| P3-7 | Add per-agent logging to `./reports` | HIGH | Medium | P3-1 |
| P3-8 | Unit tests for enhanced agent | HIGH | Large | P3-1 to P3-7 |

### Phase 4: Ray Orchestration
| ID | Task | Priority | Estimate | Dependencies |
|----|------|----------|----------|--------------|
| P4-1 | Create `Orchestrator` main class | HIGH | Large | P3-1 |
| P4-2 | Implement Ray initialization (local cluster) | HIGH | Medium | P4-1, P0-1 |
| P4-3 | Add distributed cluster configuration option | LOW | Medium | P4-2 |
| P4-4 | Implement batch creation logic | HIGH | Medium | P4-1, P1-4 |
| P4-5 | Implement sequential batch execution | HIGH | Large | P4-4 |
| P4-6 | Create agent spawning with Ray remote | HIGH | Large | P4-2, P3-1 |
| P4-7 | Implement resource allocation strategy | MEDIUM | Medium | P4-6 |
| P4-8 | Add circuit breaker for consecutive failures | HIGH | Medium | P4-6 |
| P4-9 | Unit tests for orchestration | HIGH | Large | P4-1 to P4-8 |

### Phase 5: Progress Tracking & Monitoring
| ID | Task | Priority | Estimate | Dependencies |
|----|------|----------|----------|--------------|
| P5-1 | Create `ProgressTracker` class with file locking | HIGH | Large | None |
| P5-2 | Implement markdown progress file format | HIGH | Medium | P5-1 |
| P5-3 | Add real-time progress updates | HIGH | Medium | P5-1 |
| P5-4 | Integrate tiktoken for token usage tracking | HIGH | Medium | P5-1 |
| P5-5 | Add batch progress tracking | HIGH | Small | P5-1, P4-4 |
| P5-6 | Add agent-file mapping persistence | HIGH | Small | P5-1, P3-5 |
| P5-7 | Implement zombie agent detection | MEDIUM | Medium | P5-1, P3-6 |
| P5-8 | Unit tests for progress tracking | HIGH | Medium | P5-1 to P5-7 |

### Phase 6: Error Handling & Resilience
| ID | Task | Priority | Estimate | Dependencies |
|----|------|----------|----------|--------------|
| P6-1 | Implement exponential backoff (starting at 3s) | HIGH | Small | None |
| P6-2 | Add 3-retry logic with backoff | HIGH | Medium | P6-1 |
| P6-3 | Implement corrective retry for LLM quality issues | HIGH | Medium | P6-2 |
| P6-4 | Add memory monitoring | MEDIUM | Medium | P4-6 |
| P6-5 | Implement graceful degradation on failures | HIGH | Medium | P6-2 |
| P6-6 | Create failure report generator | HIGH | Medium | P6-5 |
| P6-7 | Add race condition prevention for progress file | HIGH | Medium | P5-1 |
| P6-8 | Unit tests for error handling | HIGH | Large | P6-1 to P6-7 |

### Phase 7: Output Organization
| ID | Task | Priority | Estimate | Dependencies |
|----|------|----------|----------|--------------|
| P7-1 | Implement output directory mirroring logic | HIGH | Medium | P1-4 |
| P7-2 | Create directory structure before agent execution | HIGH | Small | P7-1 |
| P7-3 | Update agent to write to correct output path | HIGH | Small | P7-2, P3-1 |
| P7-4 | Unit tests for output organization | HIGH | Small | P7-1 to P7-3 |

### Phase 8: Project Summary Generation
| ID | Task | Priority | Estimate | Dependencies |
|----|------|----------|----------|--------------|
| P8-1 | Create `ProjectSummaryGenerator` class | HIGH | Large | P4-5 |
| P8-2 | Aggregate inter-file relationships from all docs | HIGH | Large | P8-1 |
| P8-3 | Generate core components summary | HIGH | Medium | P8-1 |
| P8-4 | Generate business logic overview | HIGH | Medium | P8-1 |
| P8-5 | Create dependency graph visualization | MEDIUM | Medium | P8-2 |
| P8-6 | Write project summary markdown | HIGH | Medium | P8-1 to P8-4 |
| P8-7 | Unit tests for summary generation | HIGH | Medium | P8-1 to P8-6 |

### Phase 9: Integration & Testing
| ID | Task | Priority | Estimate | Dependencies |
|----|------|----------|----------|--------------|
| P9-1 | Create integration test suite | HIGH | Large | All phases |
| P9-2 | Test with small project (3-5 files) | HIGH | Medium | P9-1 |
| P9-3 | Test batch mode with 10+ files | HIGH | Medium | P9-2 |
| P9-4 | Test failure recovery scenarios | HIGH | Medium | P9-2 |
| P9-5 | Test backward compatibility (single-file mode) | HIGH | Medium | P9-1 |
| P9-6 | Performance profiling | MEDIUM | Medium | P9-2 |
| P9-7 | Memory usage analysis | MEDIUM | Medium | P9-2 |

### Phase 10: Documentation & Cleanup
| ID | Task | Priority | Estimate | Dependencies |
|----|------|----------|----------|--------------|
| P10-1 | Update README.md with orchestrator usage | HIGH | Medium | P9-5 |
| P10-2 | Update config.example.yaml with orchestrator options | HIGH | Small | P0-4 |
| P10-3 | Create orchestrator architecture diagram | MEDIUM | Small | P9-5 |
| P10-4 | Code cleanup and refactoring | MEDIUM | Medium | P9-5 |

---

## 🚧 IN PROGRESS

| ID | Task | Started | Assignee | Notes |
|----|------|---------|----------|-------|
| - | - | - | - | - |

---

## ✅ COMPLETED

| ID | Task | Completed | Notes |
|----|------|-----------|-------|
| - | - | - | - |

---

## ❌ BLOCKED

| ID | Task | Blocked By | Resolution Needed |
|----|------|------------|-------------------|
| - | - | - | - |

---

## 📊 Summary Statistics

| Phase | Total Tasks | Completed | In Progress | Blocked |
|-------|-------------|-----------|-------------|---------|
| Phase 0: Foundation | 5 | 0 | 0 | 0 |
| Phase 1: Tree MCP | 6 | 0 | 0 | 0 |
| Phase 2: Metadata | 8 | 0 | 0 | 0 |
| Phase 3: Agent | 8 | 0 | 0 | 0 |
| Phase 4: Orchestration | 9 | 0 | 0 | 0 |
| Phase 5: Progress | 8 | 0 | 0 | 0 |
| Phase 6: Error Handling | 8 | 0 | 0 | 0 |
| Phase 7: Output | 4 | 0 | 0 | 0 |
| Phase 8: Summary | 7 | 0 | 0 | 0 |
| Phase 9: Integration | 7 | 0 | 0 | 0 |
| Phase 10: Documentation | 4 | 0 | 0 | 0 |
| **TOTAL** | **74** | **0** | **0** | **0** |

---

## 🔗 Task Dependencies Graph

```
Phase 0 (Foundation)
    │
    ├──► Phase 1 (Tree MCP) ──► Phase 2 (Metadata) ──┐
    │                                                 │
    └──► Phase 3 (Agent) ◄────────────────────────────┘
              │
              ▼
         Phase 4 (Orchestration)
              │
              ├──► Phase 5 (Progress Tracking)
              │
              └──► Phase 6 (Error Handling)
                        │
                        ▼
                   Phase 7 (Output)
                        │
                        ▼
                   Phase 8 (Summary)
                        │
                        ▼
                   Phase 9 (Integration)
                        │
                        ▼
                   Phase 10 (Documentation)
```

---

## 📝 Notes

### Size Estimates
- **Small**: < 50 lines of code, straightforward implementation
- **Medium**: 50-200 lines, some complexity
- **Large**: 200+ lines, significant complexity or multiple components

### Priority Definitions
- **HIGH**: Critical path, blocks other tasks
- **MEDIUM**: Important but not blocking
- **LOW**: Nice to have, can defer

### TDD Approach
Each phase includes unit tests as the final task. Tests should be written:
1. Before implementation (test skeleton)
2. During implementation (test-first where practical)
3. After implementation (coverage completion)

