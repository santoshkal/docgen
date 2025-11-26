# Project-Level Documentation Orchestrator - Enhancement Proposal

**Date**: 2025-11-24
**Status**: 🔍 Requirements Clarification Phase
**Goal**: Transform single-file agent into project-level orchestrator with parallel processing

---

## 📝 Requirements

### Core Requirements
- **Project-Level Processing**: Ability to process entire COBOL project directories (multiple files) instead of single files
- **Tree MCP Integration**: Integrate existing Tree MCP server to scan and generate project directory structure
- **Project-Level Metadata**: Invoke additional MCP tools in SuperBOL LSP and GnuCOBOL servers to generate project-level metadata
- **Parallel Agent Execution**: Spin up multiple identical documentation agents in parallel (1 agent per source file)
  - Use Ray framework for distributed parallel execution
  - Example: 100 files → 100 agents running concurrently
- **Agent Identity & Tracking**: Each agent has unique ID mapped to specific source file for accurate tracking
- **Configurable Batching**: User-selectable batch sizes for resource management
  - Options: batch of 10, batch of 20, batch of 30, or all-at-once
  - Helps manage compute resources on smaller systems
- **Progress Tracking**: Real-time progress tracking file showing status of all agents and files
- **Inter-File Relationships**: Add new section to documentation showing how files relate to each other
  - Caller/Callee relationships
  - Shared copybooks
  - File I/O dependencies
  - Visualized with diagrams
- **TDD Architecture**: Build entire orchestrator using Test-Driven Development approach
  - Write tests first
  - Implement functionality to pass tests
  - Comprehensive test coverage

### Orchestrator Responsibilities
1. Read project directory using Tree MCP server
2. Generate project-level metadata using enhanced MCP tools
3. Create progress tracking file with all processing steps
4. Spawn N agents in parallel (where N = number of files to document)
5. Assign unique agent IDs and map to file IDs
6. Monitor agent progress and update tracking file
7. Handle agent failures and retries
8. Coordinate batch execution based on configuration
9. Ensure all agents complete successfully

### Agent Enhancement Requirements
- Each agent remains identical to current single-file documentation agent
- Add capability to document inter-file relationships from project-level metadata
- Add new "Inter-File Relationships" section to output document
- Maintain all existing functionality (three-pass generation, chunking, tracing, etc.)

### Configuration Requirements
- New orchestrator configuration section or file
- Specify batch mode (batch vs all-at-once)
- Specify batch size (10/20/30/custom)
- Specify parallel execution framework (Ray)
- Maintain backward compatibility with existing single-file mode

### Deliverables
- Orchestrator agent module (orchestrator.py or enhanced cobol_doc_agent.py)
- Ray integration for parallel execution
- Progress tracking implementation
- Inter-file relationships section in template
- Comprehensive test suite (unit, integration, end-to-end)
- Updated documentation and configuration examples

---

## 📋 Enhancement Overview

### Current State
- ✅ Single-file documentation agent (working)
- ✅ MCP servers: CTags, GnuCOBOL, SuperBOL LSP
- ✅ Three-pass generation with TOON integration
- ✅ Chunking, tracing, checksums
- ✅ Supports single program or batch processing (sequential)

### Proposed Enhancements
1. **New Component**: Orchestrator Agent (controls multiple doc agents)
2. **New MCP Integration**: Tree MCP server (project structure scanning)
3. **New Capability**: Project-level metadata extraction from SuperBOL/GnuCOBOL
4. **New Capability**: Parallel agent execution using Ray framework
5. **New Feature**: Inter-file relationship documentation in each document
6. **New Feature**: Configurable batch processing (10/20/30/all)
7. **New Requirement**: Progress tracking file with agent-to-file mapping
8. **Architecture**: Test-Driven Development (TDD) approach

### High-Level Workflow
```
1. Orchestrator reads config
2. Orchestrator calls Tree MCP → Gets project file list
3. Orchestrator calls SuperBOL/GnuCOBOL project-level tools → Gets inter-file relationships
4. Orchestrator creates progress tracking file
5. Orchestrator spawns N agents in parallel (via Ray) in batches
6. Each agent generates documentation for one file (existing workflow)
7. Each agent adds inter-file relationship section
8. Orchestrator updates progress tracking as agents complete
9. Orchestrator generates project-level summary (optional?)
10. Done!
```

---

## 🤔 Clarification Questions

### 1. Tree MCP Server Integration

**Questions:**
- What is the **exact tool name/method** exposed by your Tree MCP server?
  - Examples: `list_directory`, `get_file_tree`, `scan_workspace`, etc.
- What **format** does it return the tree structure in?
  - JSON with nested structure?
  - Flat list with paths?
  - YAML?
  - Example output structure?
- Should we **filter by file extensions**?
  - Only COBOL files (`.cob`, `.cbl`, `.c74`, `.CBL`, `.COB`, `.COBOL`)?
  - Or process ALL files in the directory?
  - Should copybooks (`.cpy`, `.CPY`) be included?
- Does the Tree MCP server run in **Docker** like the other MCP servers?
  - If yes, what's the Docker image name?
  - Does it need any special configuration?
- Does it handle **nested directories** recursively?
- Does it return **file metadata** (size, modification time, line count)?

**Impact**: Critical - This is the foundation for discovering what files to process.

---

### 2. Additional MCP Tools for Project-Level Metadata

**Context**: You mentioned invoking "additional MCP Tools for the existing MCP Servers (SuperBOL LSP Server MCP, and GnuCOBOL MCP) for generating project level metadata."

**Questions:**

#### SuperBOL LSP Server MCP
- What **additional tools/methods** are available for project-level analysis?
  - Workspace-wide symbol search?
  - Cross-file reference resolution?
  - Project-level control flow graph?
  - Program call graph across files?
  - Copybook dependency analysis?
- Are these **already implemented** in your SuperBOL MCP server?
  - If yes, what are the exact tool names?
  - If no, do they need to be added first?
- What **output format** do these tools produce?

#### GnuCOBOL MCP Server
- What **additional tools/methods** are available for project-level analysis?
  - Batch analysis across multiple files?
  - Inter-program dependency graph?
  - Project-wide call graph?
  - File I/O dependency analysis (which programs read/write which files)?
- Are these **already implemented** in your GnuCOBOL MCP server?
  - If yes, what are the exact tool names?
  - Current tool: `gnucobol_batch_analyze` - does this already do project-level analysis?
- What **output format** do these tools produce?

#### CTags
- Should CTags also be invoked at the project level?
  - Or is per-file CTags analysis sufficient?

**Impact**: High - Need to know what metadata is available before designing the inter-file relationships feature.

---

### 3. Progress Tracking File

**Questions:**
- What **format** should the tracking file use?
  - YAML (human-readable, easy to edit)
  - JSON (machine-readable, structured)
  - Markdown (human-readable, can be rendered)
  - SQLite database (queryable, concurrent-safe)
- What **location** should it be stored in?
  - Same as metadata directory?
  - Separate tracking directory (e.g., `./tracking/`)?
  - Alongside documentation output?
- What **information** should be tracked?
  ```yaml
  # Example format - please confirm
  project: my-cobol-project
  started: 2025-11-24T10:00:00Z
  status: in_progress
  total_files: 100
  completed: 45
  failed: 2
  pending: 53

  files:
    - file_id: 001
      file_path: src/MAINPROG.cbl
      agent_id: agent-001
      status: completed
      started: 2025-11-24T10:01:00Z
      completed: 2025-11-24T10:08:00Z
      duration_seconds: 420
      token_usage:
        input: 1200000
        output: 180000
        total: 1380000
      output_path: docs/MAINPROG-documentation.md

    - file_id: 002
      file_path: src/ACCTPROC.cbl
      agent_id: agent-002
      status: failed
      started: 2025-11-24T10:01:00Z
      failed: 2025-11-24T10:05:00Z
      error: "OpenAI API rate limit exceeded"
      retry_count: 0
  ```
- Should tracking be **real-time** (updated as agents complete) or **final** (written at end)?
- Should it include **error messages** and **stack traces** for failed agents?
- Should it track **token usage** per file for cost estimation?
- Should it track **batch information** (which batch each file belongs to)?

**Impact**: Medium - Affects observability and debugging capability.

---

### 4. Parallel Agent Execution with Ray

**Questions:**

#### Ray Setup
- Should we assume Ray is **already installed**, or add it to `requirements.txt`?
- What **Ray version** should we target? (Latest 2.x?)
- Should Ray be an **optional dependency**?
  - Fallback to sequential processing if Ray not available?
  - Or make it mandatory for orchestrator mode?

#### Ray Cluster Configuration
- **Local single-machine** Ray cluster only?
- Or support for **distributed clusters** (multiple machines)?
- Should users be able to specify Ray cluster address in config?

#### Resource Management
- Should we allow users to specify **resources per agent**?
  ```yaml
  orchestrator:
    ray:
      cpu_per_agent: 1
      memory_per_agent_gb: 2
      gpu_per_agent: 0  # For future LLM GPU support
  ```
- Should we implement **automatic resource detection**?
  - Detect available CPUs/memory
  - Calculate max concurrent agents based on resources
- Should we respect **LLM provider rate limits**?
  - OpenAI: 500 RPM, 90K TPM (tier 1)
  - Automatically throttle agent spawning to avoid rate limits?

#### Failure Handling
- If 1 agent out of 100 fails, should the orchestrator:
  - ✅ Continue with the other 99? (RECOMMENDED)
  - ⚠️ Stop everything immediately?
  - 🔄 Retry the failed agent automatically?
- **Retry strategy**:
  - Automatic retry with exponential backoff?
  - Max retry count (e.g., 3 attempts)?
  - Manual retry by user after reviewing errors?

#### Ray Task Structure
- Should each agent run as a **Ray task** (function) or **Ray actor** (stateful class)?
  - Ray task: Simpler, stateless
  - Ray actor: Can maintain state, more complex
- Should we use **Ray's progress tracking** APIs?
  - Ray provides built-in progress bars and status tracking

**Impact**: High - Ray is critical for parallel execution and needs careful design.

---

### 5. Batching Strategy

**Questions:**
- Should the config format be:
  ```yaml
  orchestrator:
    batch_mode: batch  # Options: 'batch' or 'all'
    batch_size: 10     # Ignored if batch_mode = 'all'
  ```
  Or:
  ```yaml
  orchestrator:
    batch_size: 10     # Set to 0 or null for 'all at once'
  ```
- Should batches run **sequentially**?
  - Batch 1 completes → Start Batch 2 → Batch 2 completes → Start Batch 3
  - Advantage: Predictable resource usage
  - Disadvantage: Slower overall
- Or with **overlap/pipeline**?
  - Batch 1 at 50% → Start Batch 2
  - Advantage: Faster overall
  - Disadvantage: Peak resource usage higher
- Should batch size be **automatic** based on available resources?
  ```yaml
  orchestrator:
    batch_mode: auto   # Calculate optimal batch size
    max_memory_usage_percent: 80  # Don't exceed 80% of RAM
  ```
- Should users be able to **pause/resume** batch processing?
  - Save state after each batch
  - Allow resuming from interrupted run

**Impact**: Medium - Affects resource usage and user control.

---

### 6. Inter-File Relationships Section

**Questions:**

#### Section Metadata
- What should the **section be called**?
  - "Inter-File Relationships"
  - "Project Dependencies"
  - "Cross-Program References"
  - "Program Integration Points"
- Where should it appear in the document?
  - After "Inter-Program Communication" section?
  - As a new major section at the end?
  - As a subsection within "Inter-Program Communication"?

#### Content
What relationships should be documented?

**Option A: Caller/Callee Only**
```markdown
### Inter-File Relationships

#### Programs Called by This Program
- **ACCTPROC** (called 5 times)
  - Line 1234: CALL 'ACCTPROC' USING WS-ACCOUNT-ID
  - Line 2345: CALL 'ACCTPROC' USING WS-ACCOUNT-BALANCE

#### Programs That Call This Program
- **MAINPROG** (calls this program 3 times)
- **BATCHPROC** (calls this program 1 time)
```

**Option B: Caller/Callee + Copybooks**
```markdown
### Inter-File Relationships

#### Programs Called
- ACCTPROC (5 times)
- CUSTPROC (2 times)

#### Called By
- MAINPROG (3 times)
- BATCHPROC (1 time)

#### Shared Copybooks
- ACCOUNT-RECORD.cpy (used by 12 programs)
- ERROR-CODES.cpy (used by 45 programs)

#### Files Shared
- ACCOUNTS.dat (read by MAINPROG, written by ACCTPROC)
```

**Option C: Full Dependency Graph**
All of the above plus:
- Data flow between programs
- Control flow (which program runs first/next)
- Shared working storage patterns
- Common business logic

Which option do you prefer?

#### Visualization
- Should this include a **Mermaid diagram**?
  ```mermaid
  graph TD
      MAINPROG --> ACCTPROC
      MAINPROG --> CUSTPROC
      BATCHPROC --> ACCTPROC
      ACCTPROC --> DBQUERY
  ```
- Should the diagram show:
  - Just direct dependencies (1 level)?
  - Or full transitive dependencies (all levels)?
- Should we use **different colors/styles** for different relationship types?
  - Red for caller/callee
  - Blue for copybooks
  - Green for shared files

#### Data Source
- Where does this data come from?
  - SuperBOL CFG `calls` array?
  - GnuCOBOL `program_calls` array?
  - New project-level metadata from MCP tools?
- How do we handle **circular dependencies**?
  - PROG-A calls PROG-B, PROG-B calls PROG-A
  - Should we detect and flag these?

**Impact**: High - This is a key user-facing feature.

---

### 7. Agent Identity & File Mapping

**Questions:**
- What **Agent ID format** should we use?

  **Option A: Sequential**
  ```
  agent-001, agent-002, agent-003, ...
  ```
  - Pro: Simple, predictable
  - Con: Doesn't indicate which file

  **Option B: File-based**
  ```
  agent-MAINPROG, agent-ACCTPROC, ...
  ```
  - Pro: Clear mapping
  - Con: May have special characters in filenames

  **Option C: UUID**
  ```
  agent-abc123-def456, agent-789ghi-jkl012, ...
  ```
  - Pro: Guaranteed unique
  - Con: Hard to read/debug

  **Option D: Hybrid (Sequential + Program Name)**
  ```
  agent-001-MAINPROG, agent-002-ACCTPROC, ...
  ```
  - Pro: Best of both worlds
  - Con: Longer

- Where should the **Agent ID ↔ File mapping** be stored?
  - In the progress tracking file? (RECOMMENDED)
  - Separate mapping file (e.g., `agent-mapping.yaml`)?
  - In-memory only (logged to console)?

- Should Agent IDs be **persistent across runs**?
  - If orchestrator is restarted, should the same file get the same agent ID?
  - Or generate new IDs each run?

**Impact**: Low-Medium - Affects debugging and observability.

---

### 8. TDD Architecture Requirements

**Questions:**

#### Test Coverage
- What **test coverage target** should we aim for?
  - 80% (industry standard)
  - 90% (high confidence)
  - 100% (perfect, but may be overkill)
- Should we use **coverage tools**? (pytest-cov)

#### Test Types
Which test types are needed?

**Unit Tests**
- Test individual functions in isolation
- Mock all external dependencies (MCP, LLM, Ray)
- Fast execution (< 1 second per test)

**Integration Tests**
- Test orchestrator + real Ray cluster (local)
- Test MCP server communication
- Mock only LLM calls (expensive)
- Medium execution time (< 30 seconds per test)

**End-to-End Tests**
- Test full workflow with real/mock MCP servers
- Test with small test project (5-10 files)
- Mock LLM calls (too expensive)
- Slow execution (< 5 minutes per test)

Should we implement all three types?

#### Mocking Strategy
- **Ray**: Use Ray's testing utilities or mock completely?
- **MCP Servers**: Use real Docker containers or mock responses?
- **LLM Calls**: Always mock (too expensive to test) or allow optional real calls?
- **File System**: Use temporary directories or mock file I/O?

#### Test Data
Should I create **fixture COBOL projects** for testing?
- **Tiny project**: 3 files, simple call relationships
- **Small project**: 10 files, moderate complexity
- **Medium project**: 50 files, complex dependencies
- **Large project**: Mock 200 files (don't actually create, just simulate)

Where should test fixtures live?
- `tests/fixtures/tiny-project/`
- `tests/fixtures/small-project/`
- etc.

#### Test Framework
- Use **pytest** (current standard)?
- Use **unittest** (Python built-in)?
- Use **Ray's testing framework**?

**Impact**: High - TDD requires upfront test design before implementation.

---

### 9. Configuration File Structure

**Questions:**

Should the orchestrator config be a separate file or extend the existing config?

#### Option A: Separate Orchestrator Config
```yaml
# orchestrator.yaml
project:
  name: my-cobol-project
  source_dir: ../cobol-project
  file_extensions: [.cob, .cbl, .c74, .COB, .CBL, .COBOL]
  exclude_patterns:
    - "**/test/**"
    - "**/*.bak"

tree_mcp_server:
  enabled: true
  docker_image: tree-mcp:latest

orchestrator:
  # Parallel execution
  parallel_mode: ray           # Options: 'ray', 'sequential'
  batch_mode: batch            # Options: 'batch', 'all'
  batch_size: 10
  max_concurrent_agents: 100

  # Resource management
  ray:
    cpu_per_agent: 1
    memory_per_agent_gb: 2

  # Progress tracking
  tracking_file: ./tracking/project-progress.yaml
  update_interval_seconds: 10  # Update tracking file every 10 seconds

  # Error handling
  retry_failed: true
  max_retries: 3
  continue_on_failure: true

# Reference to existing agent config
agent_config: ./config-test-detailed-code.yaml

# Output settings
output:
  docs_dir: ../docs
  generate_project_summary: true
  organize_by_directory: true
```

**Pros:**
- Clear separation of concerns
- Orchestrator config separate from agent config
- Easy to have multiple orchestrator configs

**Cons:**
- Two config files to manage
- Potential duplication (output paths, etc.)

#### Option B: Extended Existing Config
```yaml
# config.yaml (extended)
source:
  mode: project               # NEW: 'project' mode added
  source_dir: ../cobol-project
  file_extensions: [.cob, .cbl, .c74]
  # For backward compatibility:
  # mode: single → single file
  # mode: batch → sequential batch (current behavior)
  # mode: project → parallel orchestrator

# NEW: Orchestrator section
orchestrator:
  enabled: true
  parallel_mode: ray
  batch_mode: batch
  batch_size: 10
  # ... rest of settings

# NEW: Tree MCP server
servers:
  tree:                       # NEW
    enabled: true
    docker_image: tree-mcp:latest
  ctags:                      # EXISTING
    enabled: true
    docker_image: ctags-mcp:latest
  gnuCobol:                   # EXISTING
    enabled: true
    docker_image: gnucobol-mcp:latest
  superbol-lsp:               # EXISTING
    enabled: true
    docker_image: superbol-lsp-mcp:latest

# Existing sections remain unchanged
output:
  metadata_dir: ../metadata
  docs_path: ../docs

llm:
  provider: openai
  model: gpt-4o
  api_key: ${OPENAI_API_KEY}
  temperature: 0.2
```

**Pros:**
- Single config file
- Unified configuration
- Easier for users (one file to edit)

**Cons:**
- Config file gets larger
- More complex validation logic

**Which option do you prefer?**

**Impact**: Medium - Affects user experience and code organization.

---

### 10. Error Handling & Retry Logic

**Questions:**

#### Partial Failures
If 3 out of 100 agents fail, should the orchestrator:

**Option A: Continue + Report**
- Continue processing remaining 97 files
- Generate documentation for successful files
- Create a failure report: `failed-files-report.yaml`
- User can review and retry failed files manually

**Option B: Stop Immediately**
- Stop all remaining agents
- Report which files succeeded before stopping
- User fixes issue and restarts entire run

**Option C: Retry Automatically**
- Retry failed agents up to N times (e.g., 3)
- If still failing, mark as failed and continue
- Generate failure report at the end

**Which approach do you prefer?**

#### Retry Strategy Details
If we implement automatic retry:
- **Exponential backoff**?
  - 1st retry: immediate
  - 2nd retry: wait 30 seconds
  - 3rd retry: wait 60 seconds
- **Different errors = different strategies**?
  - Rate limit error → wait longer
  - API key error → stop immediately (won't fix itself)
  - Transient network error → retry immediately
- **Max retry count**: Configurable or fixed at 3?

#### Manual Retry Command
Should we provide a command to retry only failed files?
```bash
# After initial run with failures
python orchestrator.py --retry-failed ./tracking/project-progress.yaml
```
This would:
- Read tracking file
- Identify failed files
- Retry only those files
- Update tracking file with results

**Impact**: High - Affects reliability and user experience for large projects.

---

### 11. Output Organization

**Questions:**

With 100 files generating 100 documents, how should they be organized?

#### Option A: Flat Structure
```
docs/
├── project-summary.md
├── PROGRAM-A-documentation.md
├── PROGRAM-B-documentation.md
├── PROGRAM-C-documentation.md
└── ... (97 more files)
```
**Pros:** Simple, easy to implement
**Cons:** Messy for large projects

#### Option B: Organized by Source Directory Structure
```
docs/
├── project-summary.md
├── module-A/
│   ├── PROG1-documentation.md
│   ├── PROG2-documentation.md
│   └── shared/
│       └── UTIL1-documentation.md
└── module-B/
    ├── PROG3-documentation.md
    └── PROG4-documentation.md
```
**Pros:** Mirrors source structure, easier to navigate
**Cons:** More complex to implement

#### Option C: Organized by Function/Category
```
docs/
├── project-summary.md
├── batch-processing/
│   ├── BATCHPROC-documentation.md
│   └── BATCHLOADER-documentation.md
├── online-transactions/
│   ├── MAINPROG-documentation.md
│   └── ACCTPROC-documentation.md
└── utilities/
    ├── UTIL1-documentation.md
    └── UTIL2-documentation.md
```
**Pros:** Organized by business function
**Cons:** Requires categorization logic or manual configuration

**Which option do you prefer?** Or combination?

Should this be **configurable**?
```yaml
output:
  organization: flat          # Options: 'flat', 'mirror', 'custom'
  preserve_directory_structure: true
```

**Impact**: Medium - Affects usability for large projects.

---

### 12. Project-Level Summary Document

**Questions:**

Should the orchestrator generate a **project-level overview document**?

If yes, what should it contain?

#### Proposed Structure
```markdown
# Project Documentation Summary

## Overview
- Project name
- Total programs: 100
- Total lines of code: 500,000
- Documentation generated: 2025-11-24

## Project Structure
\```
project/
├── module-A/ (25 programs)
├── module-B/ (40 programs)
└── utilities/ (35 programs)
\```

## Architecture Overview
[High-level description]

## Program Call Graph
\```mermaid
graph TD
    MAINPROG --> ACCTPROC
    MAINPROG --> CUSTPROC
    BATCHPROC --> ACCTPROC
    ACCTPROC --> DBQUERY
    ...
\```

## Shared Resources

### Copybooks
- ACCOUNT-RECORD.cpy (used by 12 programs)
- ERROR-CODES.cpy (used by 45 programs)
- ...

### Files
- ACCOUNTS.dat (read by 5 programs, written by 2 programs)
- TRANSACTIONS.dat (read by 8 programs, written by 3 programs)
- ...

## Program Index
- [MAINPROG](./MAINPROG-documentation.md) - Main entry point
- [ACCTPROC](./ACCTPROC-documentation.md) - Account processing
- ...

## Statistics
- Average program size: 5,000 lines
- Total complexity score: 12,500
- Programs with high complexity (>500): 8
- ...
```

Should we generate this? If yes:
- Should it be **mandatory** or **optional**?
- Should it include **all** of the above or a subset?
- Should it include **Mermaid diagrams**?
  - Full project call graph?
  - Module dependency graph?
- Should it include **metrics/statistics**?
  - Complexity metrics
  - Code coverage (if available)
  - Documentation coverage

**Impact**: Medium - Adds value but increases complexity.

---

## 🚧 Potential Challenges & Roadblocks

### 1. Ray Framework Learning Curve
**Challenge**: Ray is a complex distributed computing framework.

**Concerns:**
- Team may need time to learn Ray concepts (tasks, actors, object store)
- Ray debugging can be challenging (distributed state, async execution)
- Ray version compatibility issues
- Ray overhead for small projects (might be slower than sequential for < 10 files)

**Mitigation Strategies:**
- Start with simple Ray tasks (no actors)
- Implement fallback to sequential processing
- Comprehensive error handling and logging
- Create Ray debugging guide in docs
- Consider alternative: Python's `concurrent.futures` (simpler, but less powerful)

**Decision Needed:** Is Ray a hard requirement, or should we support alternatives?

---

### 2. LLM Rate Limits
**Challenge**: Spawning 100 parallel agents will hit LLM API rate limits.

**Concerns:**
- **OpenAI GPT-4o Limits** (Tier 1):
  - 500 requests per minute (RPM)
  - 90,000 tokens per minute (TPM)
  - With 100 agents running in parallel, we'd hit limits in < 30 seconds
- **Rate limit errors** will cause agent failures
- **Exponential backoff** adds unpredictable delays
- **Cost explosion** with parallel execution

**Example Scenario:**
- 100 agents spawn simultaneously
- Each agent makes 3 LLM calls (Pass 1, Pass 2, Pass 3)
- That's 300 requests in ~10 minutes
- Exceeds 500 RPM if agents complete passes at similar times

**Mitigation Strategies:**
1. **Throttling**: Implement request rate limiter
   ```python
   # Don't exceed N requests per minute
   rate_limiter = RateLimiter(max_rpm=400)  # Buffer below 500
   ```
2. **Staggered starts**: Don't spawn all agents at once
   ```python
   # Spawn 1 agent every 5 seconds
   for agent in agents:
       ray.remote(agent).remote()
       time.sleep(5)
   ```
3. **Batch size defaults based on tier**:
   ```yaml
   orchestrator:
     batch_size: auto  # Calculate based on LLM provider tier
   ```
4. **Monitor rate limit headers**: Track remaining quota
5. **Queue system**: Agents wait in queue for LLM access

**Decision Needed:** Which mitigation strategies should we implement?

---

### 3. Memory Consumption
**Challenge**: 100 parallel agents will consume significant memory.

**Concerns:**
- Each agent loads:
  - Metadata files (can be 10+ MB per program)
  - LangGraph state
  - LLM conversation history
  - Source code (for chunking)
- **Estimate per agent**: ~200-500 MB RAM
- **100 agents**: 20-50 GB RAM required
- Most development machines: 16-32 GB RAM
- **Risk**: System OOM (out of memory), thrashing, crashes

**Mitigation Strategies:**
1. **Dynamic batch sizing**:
   ```python
   # Calculate batch size based on available RAM
   available_ram = psutil.virtual_memory().available
   ram_per_agent = 300 * 1024 * 1024  # 300 MB
   max_batch = available_ram // ram_per_agent
   ```
2. **Lazy loading**: Don't load all metadata at once
3. **Streaming**: Process metadata in chunks, not all in memory
4. **Ray object store**: Use Ray's shared memory for metadata
5. **Garbage collection**: Aggressive cleanup after each agent

**Recommendation:** Default batch size should be conservative (10-20), not 100.

**Decision Needed:** Should we auto-calculate batch size or let users specify?

---

### 4. MCP Server Coordination
**Challenge**: Multiple agents calling MCP servers concurrently.

**Concerns:**
- **SuperBOL LSP**: Typically designed for single client (IDE)
  - May not handle 100 concurrent connections
  - May have internal state conflicts
- **GnuCOBOL MCP**: Spawns compiler processes
  - 100 agents → 100 compiler processes → resource exhaustion
- **Docker container limits**:
  - Each MCP server runs in Docker
  - Multiple concurrent requests may overwhelm container
- **File system contention**: Multiple writes to metadata directory

**Mitigation Strategies:**
1. **MCP connection pooling**:
   ```python
   # Shared pool of MCP connections
   mcp_pool = MCPConnectionPool(max_connections=5)
   # Agents request connection from pool, blocking if none available
   ```
2. **Pre-generate all metadata**:
   - Orchestrator calls MCP servers ONCE for entire project
   - Generates metadata for all files before spawning agents
   - Agents only read metadata, don't call MCP servers
   - **This is probably the best approach**
3. **Metadata caching**: Store metadata in shared Ray object store
4. **Serialize MCP calls**: Only 1 agent calls MCP at a time (defeats parallelism)

**Recommendation:** Pre-generate all metadata before spawning agents.

**Decision Needed:** Should agents call MCP servers, or should orchestrator pre-generate?

---

### 5. Progress Tracking File Concurrency
**Challenge**: 100 agents updating the same tracking file concurrently.

**Concerns:**
- **File corruption**: Simultaneous writes can corrupt YAML/JSON
- **Lost updates**: Agent A and Agent B both read, modify, write → one overwrites the other
- **File locking issues**: OS file locks may cause failures

**Mitigation Strategies:**
1. **Centralized tracker**:
   ```python
   # Ray actor with serial access
   @ray.remote
   class ProgressTracker:
       def update_status(self, agent_id, status):
           # Thread-safe update
           self.tracking_data[agent_id] = status
           self.write_to_file()
   ```
2. **Append-only log**:
   ```python
   # Each agent appends to JSONL file
   # Orchestrator reads and aggregates at end
   with open("progress.jsonl", "a") as f:
       f.write(json.dumps(status_update) + "\n")
   ```
3. **SQLite database**: Built-in concurrency support
4. **Redis/external store**: If running distributed cluster

**Recommendation:** Use Ray actor as centralized progress tracker.

**Decision Needed:** Which approach do you prefer?

---

### 6. Inter-File Relationships Data Source
**Challenge**: Determining inter-file relationships may require project-level analysis.

**Concerns:**
- **Current metadata is per-file**:
  - SuperBOL symbols: Only current file
  - GnuCOBOL analysis: Only current file
  - CTags: Only current file
- **CALL statements are unresolved**:
  - `CALL 'ACCTPROC'` → Which file is ACCTPROC?
  - Need to match program names to file names
  - Ambiguity: Multiple files with same PROGRAM-ID
- **Copybook locations are relative**:
  - `COPY ACCOUNT-RECORD` → Where is ACCOUNT-RECORD.cpy?
  - Need copybook search path resolution
- **File I/O dependencies unclear**:
  - `SELECT ACCOUNTS-FILE` → Which physical file?
  - Multiple programs may use different names for same file

**Mitigation Strategies:**
1. **Build program name → file path mapping**:
   ```python
   # Scan all files, extract PROGRAM-ID
   program_map = {
       "MAINPROG": "src/main/MAINPROG.cbl",
       "ACCTPROC": "src/accounting/ACCTPROC.cbl",
       ...
   }
   ```
2. **Resolve CALL statements**:
   ```python
   # CALL 'ACCTPROC' → Look up in program_map
   called_program = "ACCTPROC"
   called_file = program_map.get(called_program)
   ```
3. **Use project-level MCP tools** (if available):
   - SuperBOL workspace-level analysis
   - GnuCOBOL project-level call graph
4. **Post-processing step**:
   - Generate all docs first
   - Run post-processor to inject inter-file relationships
   - Requires re-writing markdown files

**Question:** Are project-level MCP tools available? If not, we'll need workarounds.

---

### 7. Backward Compatibility
**Challenge**: Don't break existing single-file and batch modes.

**Concerns:**
- Users rely on current agent behavior
- New orchestrator mode shouldn't affect existing modes
- Configuration changes shouldn't break old configs
- Need to maintain all three modes:
  1. **Single mode**: One file, synchronous
  2. **Batch mode**: Multiple files, sequential
  3. **Project mode**: Multiple files, parallel (NEW)

**Mitigation Strategies:**
1. **Separate entry points**:
   ```bash
   # Old (unchanged)
   python cobol_doc_agent.py MAINPROG

   # New
   python orchestrator.py --config orchestrator.yaml
   ```
2. **Mode detection in unified CLI**:
   ```bash
   python cobol_doc_agent.py --mode project --config config.yaml
   ```
3. **Comprehensive tests**: Test all three modes
4. **Deprecation path**: If we change existing modes, provide migration guide

**Recommendation:** Separate orchestrator.py entry point (cleaner separation).

**Decision Needed:** Separate entry point or unified CLI?

---

### 8. Token Budget Management
**Challenge**: Three-pass strategy with token budgets may not work for project mode.

**Concerns:**
- **Current approach**: Each agent independently decides what metadata to send based on token budget
- **Project mode issue**: Agents don't know about other files
  - Can't make informed decisions about relative importance
  - May send redundant information (same copybook details in 50 files)
- **TOON integration**: Currently optimizes single-file metadata
  - Project-level metadata may have different structure

**Mitigation Strategies:**
1. **Accept redundancy**: Each file's doc is self-contained
   - Pro: Simple, no coordination needed
   - Con: Repetitive information across docs
2. **Shared context store**:
   - Orchestrator pre-processes common elements (copybooks, shared utilities)
   - Agents reference shared context instead of repeating
3. **Post-processing consolidation**:
   - Generate all docs
   - Run post-processor to extract common sections
   - Create separate reference docs for shared elements
4. **Smarter filtering**:
   - Agents aware of project-level context
   - Can make better decisions about what to include

**Question:** Is redundancy acceptable, or should we optimize for project-level efficiency?

---

### 9. Testing Complexity
**Challenge**: TDD for distributed system is significantly more complex.

**Concerns:**
- **Ray testing**: Requires Ray cluster (local or real)
- **MCP testing**: Requires Docker containers or extensive mocking
- **LLM testing**: Expensive to test with real calls
- **Timing issues**: Async/parallel execution → non-deterministic test results
- **State management**: Tracking files, agents, progress → complex assertions
- **Fixture management**: Need realistic COBOL projects for testing

**Mitigation Strategies:**
1. **Layered testing approach**:
   - **Unit tests**: Pure functions, fully mocked, fast
   - **Integration tests**: Ray + mocked MCP/LLM, medium speed
   - **E2E tests**: Real Ray + mocked LLM, slow
2. **Test fixtures**:
   - Create 3-5 minimal COBOL programs for testing
   - Mock large-scale scenarios (simulate 100 files without creating them)
3. **Deterministic testing**:
   - Use fixed seeds for random operations
   - Mock time.time() for timestamp assertions
   - Use Ray's testing utilities for deterministic scheduling
4. **CI/CD considerations**:
   - May need Docker-in-CI for MCP server tests
   - May need Ray cluster in CI environment

**Impact:** Testing will take significant time to set up properly.

---

### 10. Cost Considerations
**Challenge**: Parallel execution amplifies costs.

**Concerns:**
- **Current single-file cost**: $5-8 per program (GPT-4o)
- **100-file project cost**: $500-800
- **Large project (500 files)**: $2,500-4,000
- **Development/testing costs**: Repeated runs during development
- **Failed agents**: Partial completion still incurs costs

**Mitigation Strategies:**
1. **Cost estimation upfront**:
   ```bash
   python orchestrator.py --estimate-cost
   # Output: Estimated cost: $650 for 100 files
   ```
2. **Cheaper model for testing**:
   ```yaml
   llm:
     provider: openai
     model: gpt-3.5-turbo  # $0.50-1 per program
   ```
3. **Dry-run mode**:
   ```bash
   python orchestrator.py --dry-run
   # Simulates entire workflow without LLM calls
   ```
4. **Incremental documentation**:
   - Only document changed files (use checksums)
   - Skip unchanged files
5. **Resume from checkpoint**:
   - If run fails at 50/100, resume from 51st file
   - Don't re-generate already completed files

**Recommendation:** Implement cost estimation and dry-run mode.

---

### 11. Documentation Quality Consistency
**Challenge**: 100 parallel agents may produce inconsistent documentation.

**Concerns:**
- **LLM non-determinism**: Even with temperature=0.2, slight variations occur
- **Section ordering**: May vary slightly between files
- **Terminology**: Same concept described differently in different files
- **Diagram styles**: Mermaid diagrams may look different
- **Level of detail**: Some files over-explained, others under-explained

**Mitigation Strategies:**
1. **Strict temperature**: Lower to 0.1 for more consistency
2. **Shared prompts**: All agents use identical prompts (already done)
3. **Post-processing validation**:
   - Check all docs have required sections
   - Validate Mermaid diagrams parse correctly
   - Check formatting consistency
4. **Style guide**: Generate style guide from first few files, enforce on rest
5. **Accept variation**: Embrace that each file is unique

**Question:** How important is consistency across 100 files? Strict or flexible?

---

### 12. Debugging & Troubleshooting
**Challenge**: Debugging 100 parallel agents is extremely difficult.

**Concerns:**
- **Which agent failed?** Ray logs may be scattered
- **Why did it fail?** Stack traces from 100 different processes
- **Reproducing issues**: Hard to reproduce race conditions
- **Log volume**: 100 agents × 3 passes × detailed logs = overwhelming
- **Ray dashboard**: Helps but has learning curve

**Mitigation Strategies:**
1. **Structured logging**:
   ```python
   logger.info("Agent 042 - MAINPROG.cbl - Pass 2 - Starting")
   # Include agent ID and file name in every log
   ```
2. **Centralized error collection**:
   ```python
   @ray.remote
   class ErrorCollector:
       def report_error(self, agent_id, error_info):
           # Aggregate all errors
   ```
3. **Debug mode**:
   ```yaml
   orchestrator:
     debug_mode: true  # Run sequentially with verbose logging
   ```
4. **Agent-specific logs**:
   ```
   logs/
   ├── agent-001-MAINPROG.log
   ├── agent-002-ACCTPROC.log
   └── ...
   ```
5. **Ray dashboard training**: Include guide in docs

**Recommendation:** Implement debug mode for troubleshooting.

---

## 📊 Complexity Assessment

### High Complexity Areas
1. ⚠️ **Ray integration** - Requires distributed systems expertise
2. ⚠️ **Inter-file relationships** - Depends on project-level MCP tools availability
3. ⚠️ **Rate limit handling** - Complex throttling and queuing logic
4. ⚠️ **TDD for distributed system** - Challenging test setup

### Medium Complexity Areas
1. 🟡 **Progress tracking** - Concurrency issues, but Ray actor solves it
2. 🟡 **Batch management** - Logic is straightforward, just needs careful design
3. 🟡 **Error handling & retry** - Standard patterns, well-documented
4. 🟡 **Memory management** - Requires monitoring and tuning

### Low Complexity Areas
1. ✅ **Tree MCP integration** - Similar to existing MCP servers
2. ✅ **Configuration** - Extend existing config system
3. ✅ **Output organization** - File system operations
4. ✅ **Agent ID management** - Straightforward mapping

---

## 🎯 Recommended Approach

Based on the challenges identified, I recommend:

### Phase 1: Foundation (MVP)
1. Tree MCP integration
2. Project-level metadata extraction
3. Sequential orchestrator (NO Ray initially)
4. Basic progress tracking (file-based, no concurrency)
5. Simple inter-file relationships (caller/callee only)

**Benefit:** Proves concept, simpler testing, no Ray complexity

### Phase 2: Parallelization
1. Ray integration
2. Parallel agent execution
3. Batch processing with configurable size
4. Rate limiting and throttling
5. Concurrent-safe progress tracking

**Benefit:** Performance improvements after validating approach

### Phase 3: Advanced Features
1. Enhanced inter-file relationships (copybooks, files)
2. Project-level summary document
3. Advanced error handling and retry
4. Cost estimation and dry-run mode
5. Memory optimization

**Benefit:** Polish and production-readiness

---

## ❓ Critical Questions Summary

**Before we proceed, please answer:**

1. **Tree MCP Server**: Tool names, format, Docker image?
2. **Project-level MCP tools**: What's available in SuperBOL/GnuCOBOL?
3. **Inter-file relationships**: What data is available? What should be documented?
4. **Ray requirement**: Mandatory or optional? Fallback to sequential?
5. **Rate limits**: How should we handle LLM rate limits?
6. **Configuration**: Separate file or extend existing config?
7. **Progress tracking**: Format and update strategy?
8. **Batch execution**: Sequential batches or overlapping?
9. **Phased approach**: Should we build MVP first without Ray?

---

**Next Step:** Once you answer these questions, I'll create a detailed KanBan board with actionable tasks! 🚀
