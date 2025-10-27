# COBOL Documentation Agent - Architecture

This document explains how the COBOL Documentation Agent integrates MCP (Model Context Protocol) metadata generation with LangGraph-based documentation generation.

---

## System Overview

The agent consists of two primary modules working together:

1. **`mcp_metadata_generator.py`** - MCP integration for metadata extraction
2. **`cobol_doc_agent.py`** - LangGraph-based documentation orchestrator

These modules are **loosely coupled** through dynamic imports and state management, allowing the MCP integration to be completely optional.

---

## Module Architecture

### High-Level Component Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    cobol_doc_agent.py                       │
│  (Main orchestrator - LangGraph workflow)                   │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  START → should_generate_metadata()                │    │
│  │           ↓                        ↓                │    │
│  │      "generate"              "load"                 │    │
│  │           ↓                        ↓                │    │
│  │  generate_metadata_node()   load_metadata_node()   │    │
│  │           │                                         │    │
│  │           ├─ Dynamic import: mcp_metadata_generator│    │
│  │           │                                         │    │
│  │           └─ generate_metadata_sync(...)           │    │
│  │                                                     │    │
│  └────────────────────────────────────────────────────┘    │
└──────────────────────┬──────────────────────────────────────┘
                       │ imports when needed
                       ↓
┌─────────────────────────────────────────────────────────────┐
│             mcp_metadata_generator.py                       │
│  (Standalone MCP integration module)                        │
│                                                              │
│  • MCPMetadataGenerator class                               │
│  • Docker container management                              │
│  • MCP server communication (mcp-use library)               │
│  • Metadata file generation                                 │
│  • generate_metadata_sync() - sync wrapper                  │
└─────────────────────────────────────────────────────────────┘
                       │ uses
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                      mcp-use library                        │
│  (External dependency - manages MCP protocol)               │
└─────────────────────────────────────────────────────────────┘
```

---

## Integration Points

### 1. Entry Point: LangGraph Workflow

**File**: `cobol_doc_agent.py` (lines 466-523)

The LangGraph workflow defines the complete documentation generation pipeline with conditional routing:

```python
def create_documentation_agent() -> StateGraph:
    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("generate_metadata", generate_metadata_node)  # MCP node
    workflow.add_node("load_metadata", load_metadata_node)
    workflow.add_node("load_template", load_template_node)
    workflow.add_node("extract_structure", extract_template_structure_node)
    workflow.add_node("process_section", process_section_node)
    workflow.add_node("assemble_document", assemble_document_node)
    workflow.add_node("save_document", save_document_node)

    # Conditional routing from START
    workflow.add_conditional_edges(
        START,
        should_generate_metadata,  # Decision function
        {
            "generate": "generate_metadata",  # Route to MCP
            "load": "load_metadata"           # Skip MCP
        }
    )

    # Continue workflow after metadata generation
    workflow.add_edge("generate_metadata", "load_metadata")
    workflow.add_edge("load_metadata", "load_template")
    # ... rest of workflow
```

### 2. Conditional Router

**File**: `cobol_doc_agent.py` (lines 54-71)

Decides whether to generate metadata or use existing:

```python
def should_generate_metadata(state: AgentState) -> str:
    """
    Routing function: Determine if metadata generation is needed

    Returns:
        "generate" - Generate metadata via MCP
        "load" - Skip generation, load existing metadata
    """
    if not state.get("generate_metadata", False):
        return "load"  # Skip MCP, use existing metadata

    if state.get("skip_existing_metadata", True) and check_metadata_exists(state):
        return "load"  # Metadata exists, skip MCP

    return "generate"  # Need to generate via MCP
```

### 3. MCP Integration Node

**File**: `cobol_doc_agent.py` (lines 66-101)

This is where the two modules connect:

```python
def generate_metadata_node(state: AgentState) -> AgentState:
    """
    Node 0: Generate metadata using MCP servers (optional, conditional)

    This node is only executed if:
    - generate_metadata flag is True
    - AND (skip_existing_metadata is False OR metadata doesn't exist)
    """
    from mcp_metadata_generator import generate_metadata_sync  # ← Dynamic import!

    workspace_path = str(state["workspace_path"])
    metadata_dir = str(state["metadata_dir"])
    cobol_files = state.get("cobol_files", [])

    # If no cobol_files provided, auto-discover
    if not cobol_files:
        workspace = Path(workspace_path)
        cobol_files = sorted([f.name for f in workspace.glob("*.COB")])

    # Call MCP module
    generate_metadata_sync(workspace_path, metadata_dir, cobol_files)

    return state
```

### 4. MCP Module

**File**: `mcp_metadata_generator.py`

Standalone module that:
- Manages Docker-based MCP servers (ctags, gnucobol, superbol)
- Handles concurrent metadata generation
- Writes metadata to output directories
- **Has zero dependency on cobol_doc_agent.py**

Key function:
```python
def generate_metadata_sync(workspace_path: str, output_dir: str, cobol_files: List[str]):
    """
    Synchronous wrapper for metadata generation
    Can be called from LangGraph nodes.
    """
    generator = MCPMetadataGenerator(workspace_path, output_dir)
    asyncio.run(generator.generate_all_metadata(cobol_files))
```

---

## State Management

All data flows through the **AgentState TypedDict**, which acts as the single source of truth:

```python
class AgentState(TypedDict):
    # Input
    program_name: str
    workspace_path: Path               # Where COBOL source files are
    metadata_dir: Path
    template_path: Path
    output_dir: Path

    # MCP Control Flags
    generate_metadata: bool            # Should we call MCP?
    skip_existing_metadata: bool       # Skip if metadata exists?
    cobol_files: List[str]             # Files to process

    # Loaded Metadata (output from MCP, input to doc generation)
    superbol_symbols: Dict[str, Any]
    superbol_cfg: Dict[str, Any]
    gnucobol_analysis: Dict[str, Any]
    ctags_outline: Dict[str, Any]

    # Processing State
    current_section: str
    section_ids: List[str]
    current_section_index: int
    generated_content: Dict[str, str]

    # Output
    final_document: str
    errors: List[str]
```

---

## Dependency Management

### Import Strategy: Lazy Loading

The MCP module is imported **inside the function** that needs it:

```python
# cobol_doc_agent.py line 74
def generate_metadata_node(state: AgentState) -> AgentState:
    from mcp_metadata_generator import generate_metadata_sync  # Import inside function!
    # ...
```

**Why lazy loading?**

1. **Optional dependency**: If user doesn't need metadata generation, MCP module never loads
2. **Faster startup**: No overhead when using existing metadata
3. **Better error handling**: Import errors only occur when the feature is actually used
4. **Cleaner separation**: No hard coupling between modules

### Package Dependencies

**File**: `requirements.txt`

```
# LangGraph and LangChain
langgraph>=0.0.40
langchain-core>=0.1.0
langchain-openai>=0.0.3

# LLM Provider
openai>=1.6.0

# Template Processing
pyyaml>=6.0

# MCP Integration (optional feature)
mcp-use>=0.1.0
```

---

## Complete Execution Flow

### Full Pipeline Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     User CLI Command                        │
│  python cobol_doc_agent.py --source-files ../cobol-source   │
│                      --generate-metadata                     │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│              cobol_doc_agent.py __main__                    │
│  • Parse CLI arguments                                      │
│  • Validate inputs                                          │
│  • Determine batch vs single mode                           │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│           generate_documentation() function                 │
│  • Create initial_state with all parameters                 │
│  • Set generate_metadata flag based on CLI args             │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│              agent.invoke(initial_state)                    │
│  LangGraph workflow execution begins                        │
└────────────────────────┬────────────────────────────────────┘
                         ↓
         ┌───────────────┴───────────────┐
         │    START (LangGraph)          │
         └───────────────┬───────────────┘
                         ↓
         ┌───────────────────────────────────┐
         │  should_generate_metadata()       │
         │  Decision point                   │
         └───────┬───────────────┬───────────┘
                 ↓               ↓
         generate_metadata=True?  No
                 ↓                ↓
              YES          ┌──────────────────┐
                 ↓         │ load_metadata    │
┌────────────────────────┐ │ (skip MCP)       │
│ generate_metadata_node │ └─────┬────────────┘
│                        │       │
│ 1. Dynamic import:     │       │
│    mcp_metadata_gen    │       │
│                        │       │
│ 2. generate_metadata_  │       │
│    sync(...)           │       │
│    ↓                   │       │
│ MCPMetadataGenerator   │       │
│    ↓                   │       │
│ Start Docker containers│       │
│ • ctags-mcp-server     │       │
│ • gnucobol-mcp-server  │       │
│ • superbol-mcp-server  │       │
│    ↓                   │       │
│ Concurrent metadata    │       │
│ generation via mcp-use │       │
│    ↓                   │       │
│ Write to output_dir/:  │       │
│ • ctags/*.json         │       │
│ • gnucobol/*.json      │       │
│ • superbol/*.json      │       │
│ • superbol-cfg/*.json  │       │
└────────┬───────────────┘       │
         └───────────┬────────────┘
                     ↓
         ┌───────────────────────┐
         │  load_metadata_node   │
         │  Read metadata from   │
         │  output_dir/          │
         └──────────┬────────────┘
                    ↓
         ┌───────────────────────┐
         │  load_template_node   │
         │  Read YAML template   │
         └──────────┬────────────┘
                    ↓
         ┌───────────────────────┐
         │  extract_structure    │
         │  Parse template       │
         └──────────┬────────────┘
                    ↓
         ┌───────────────────────┐
         │  process_section      │◄─────┐
         │  Use LLM + metadata   │      │
         │  to generate content  │      │
         └──────────┬────────────┘      │
                    ↓                    │
         ┌───────────────────────┐      │
         │  check_completion     │      │
         │  More sections?       │      │
         └──────┬────────┬───────┘      │
                │        │               │
               YES      NO               │
                │        ↓               │
                └────────────────────────┘
                         ↓
         ┌───────────────────────┐
         │  assemble_document    │
         │  Combine all sections │
         └──────────┬────────────┘
                    ↓
         ┌───────────────────────┐
         │  save_document_node   │
         │  Write to docs_path/  │
         └──────────┬────────────┘
                    ↓
         ┌───────────────────────┐
         │  END (LangGraph)      │
         └───────────────────────┘
                    ↓
         ┌───────────────────────┐
         │  Return output path   │
         │  Display summary      │
         └───────────────────────┘
```

---

## Key Design Benefits

### 1. Loose Coupling
- MCP module doesn't know about LangGraph
- Can be used independently
- Easy to test in isolation

### 2. Single Responsibility
- `mcp_metadata_generator.py`: Metadata extraction via MCP
- `cobol_doc_agent.py`: Documentation orchestration

### 3. Optional Feature
- MCP integration is completely opt-in
- Agent works with or without metadata generation
- No performance penalty when not used

### 4. Testability
- Each module can be tested independently
- Mock boundaries are clear
- State is explicit and traceable

### 5. Reusability
- MCP generator can be used by other tools
- LangGraph workflow can use other metadata sources
- Clean separation of concerns

---

## File Organization

```
cobol-work/
├── agent/
│   ├── cobol_doc_agent.py          # Main orchestrator (LangGraph)
│   ├── mcp_metadata_generator.py   # MCP integration module
│   ├── cobol-doc-template.yaml     # Documentation template
│   ├── requirements.txt            # Python dependencies
│   ├── architecture.md             # This file
│   ├── MCP_INTEGRATION_GUIDE.md    # MCP usage guide
│   └── .venv/                      # Virtual environment
├── cobol-source/                   # Input: COBOL source files
│   └── *.COB
├── output/                         # Generated metadata
│   ├── ctags/
│   ├── gnucobol/
│   └── superbol/
└── docs/                           # Generated documentation
    └── *-documentation.md
```

---

## Usage Patterns

### Pattern 1: Generate Metadata + Documentation (One-Shot)

```bash
python cobol_doc_agent.py --source-files ../cobol-source \
    --generate-metadata \
    --output-dir ../output \
    --docs-path ../docs
```

**Flow**: START → generate_metadata → load_metadata → ... → save_document

### Pattern 2: Use Existing Metadata

```bash
python cobol_doc_agent.py MAINPROG \
    --output-dir ../output \
    --docs-path ../docs
```

**Flow**: START → load_metadata → ... → save_document (skips MCP)

### Pattern 3: Force Regenerate Metadata

```bash
python cobol_doc_agent.py --source-files ../cobol-source \
    --generate-metadata \
    --no-skip-existing
```

**Flow**: START → generate_metadata (even if exists) → ... → save_document

---

## Error Handling

### Metadata Generation Failures

If MCP metadata generation fails:
1. Error is caught in `generate_metadata_node()`
2. Error message added to `state["errors"]`
3. Workflow continues to `load_metadata_node()`
4. Documentation may be generated with partial metadata

### Missing Metadata Files

If metadata files don't exist:
1. `load_metadata_node()` catches the error
2. Error added to `state["errors"]`
3. Documentation generation may fail or produce incomplete results
4. User is notified via error summary

---

## Extension Points

### Adding New MCP Servers

1. Add server configuration to `mcp_metadata_generator.py`:
   ```python
   config["mcpServers"]["new-server"] = {
       "command": "docker",
       "args": [...]
   }
   ```

2. Add generation method:
   ```python
   async def generate_newserver_metadata(self, cobol_files):
       # Implementation
   ```

3. Add to concurrent execution:
   ```python
   await asyncio.gather(
       self.generate_ctags_metadata(...),
       self.generate_newserver_metadata(...)
   )
   ```

### Adding New Documentation Sections

1. Update `cobol-doc-template.yaml` with new section
2. No code changes needed - LangGraph processes dynamically

### Customizing LLM Behavior

Modify `generate_section_content()` in `cobol_doc_agent.py`:
- Change model: `model="gpt-4-turbo"`
- Adjust temperature: `temperature=0.3`
- Modify system prompt for different output style

---

## Performance Considerations

### Concurrent Metadata Generation

MCP servers run concurrently via `asyncio.gather()`:
```python
await asyncio.gather(
    self.generate_ctags_metadata(cobol_files),
    self.generate_gnucobol_metadata(cobol_files),
    self.generate_superbol_metadata(cobol_files),
    return_exceptions=True
)
```

**Benefit**: 3x faster than sequential execution

### Batch Processing Optimization

In batch mode, metadata is generated **once** for all files:
```python
generate_metadata=args.generate_metadata and idx == 1
```

Only the first file triggers metadata generation; subsequent files reuse it.

### Docker Container Lifecycle

Containers use `--rm` flag for automatic cleanup:
```python
"args": ["run", "-i", "--rm", ...]
```

No manual cleanup needed - containers self-destruct on exit.

---

## Summary

The COBOL Documentation Agent achieves clean integration between MCP metadata generation and LangGraph-based documentation through:

1. **Conditional routing** - Metadata generation is optional
2. **Lazy imports** - MCP module loaded only when needed
3. **State management** - All data flows through AgentState
4. **Loose coupling** - Modules are independent
5. **Single responsibility** - Each module has one job

This architecture enables flexible, testable, and maintainable documentation generation for COBOL projects.
