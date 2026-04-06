# Code Documentation Agent

**AI-powered documentation generator for COBOL and C#/.NET codebases**

Generates comprehensive Markdown documentation by orchestrating LLM calls against metadata extracted from static analysis tools (Universal-Ctags, tree-sitter, OmniSharp LSP). Supports multiple LLM providers (OpenAI, Anthropic, Claude SDK) with automatic fallback.

## Quick Start

```bash
# Install dependencies (Python 3.10+)
pip install -r requirements.txt

# Set API key (choose your provider)
export OPENAI_API_KEY="..."       # for OpenAI
export ANTHROPIC_API_KEY="..."    # for Anthropic

# Run with YAML config (recommended)
python cobol_doc_agent.py --config config.minimal.yaml

# View results
cat ../docs/MAINPROG-documentation.md
```

## How It Works

### Three-Phase Documentation Pipeline

```
Source Code + Metadata (ctags / tree-sitter / OmniSharp)
  |
  v
Phase 1: Source chunking --> per-chunk LLM calls --> code explanation + prose
  |       (structural boundaries, cross-references injected per chunk)
  v
Phase 2: Prose + metadata --> per-section LLM calls --> section content
  |       (executive summary, control flow, data flow, business logic, etc.)
  v
Phase 3: Assembly --> final Markdown document
  |       (ordered per template, validated, with Mermaid diagrams)
  v
Output: docs/<PROGRAM>-documentation.md
```

**Phase 1** chunks the source file at structural boundaries (class/method for C#, paragraph/section for COBOL) and processes each chunk through the LLM with minimal metadata. Each chunk receives cross-reference context (inter/intra-file relationships) when available.

**Phase 2** generates remaining documentation sections using the prose extracted from Phase 1 plus normalized metadata. Raw metadata JSON is excluded to stay within token limits.

**Phase 3** combines Phase 1 and Phase 2 outputs into the final Markdown document, ordered per the YAML template.

## Supported Languages

| Language | Adapter | Metadata Tools | Extensions |
|----------|---------|----------------|------------|
| **COBOL** | `CobolAdapter` | SuperBol LSP, GnuCOBOL, Universal-Ctags | `.cbl`, `.cob`, `.CBL`, `.COB`, `.c74`, `.C74`, `.XMOD`, `.xmod`, `.XLIB`, `.xlib`, `.xgn`, `.XGN` |
| **C# / .NET** | `DotNetAdapter` | Universal-Ctags, tree-sitter, tree-sitter-graph, multilspy (OmniSharp) | `.cs` |

## Configuration

All settings are defined in a YAML config file. Key sections:

```yaml
source:
  language: dotnet              # or "cobol"
  mode: batch                   # or "single"
  source_files: ~/project       # Directory or single file
  extensions:
    include: ['.cs']
  exclude_files: ['AssemblyInfo.cs', '*.Designer.cs']
  include_files: ['PickList.cs'] # Process only these files (optional)

output:
  metadata_dir: ../output/metadata
  docs_path: ../output/docs
  create_dirs: true

llm:
  provider: claude_sdk          # openai, anthropic, claude_sdk
  model: claude-opus-4-6
  temperature: 0.2
  phase1:
    model: claude-opus-4-6
  phase2:
    model: claude-opus-4-6
  fallback:                     # Optional: switch provider on error
    provider: openai
    model: gpt-4o

metadata:
  generate: true
  skip_existing: true
  servers:                      # MCP servers for metadata extraction
    ctags:
      enabled: true
      docker_image: ctags-mcp:test
      tools: [...]
    tree-sitter:
      enabled: true
      docker_image: treesitter-mcp:test
      tools: [...]

template:
  path: ./languages/dotnet/template.yaml

chunking:
  strategy: tsg_graph           # tsg_graph, query_code, ctags
  max_tokens_per_chunk: auto
```

### Available Config Files

| Config | Purpose |
|--------|---------|
| `config.minimal.yaml` | Quickstart with essential settings |
| `config.example.yaml` | All options documented |
| `config-dotnet-imes.yaml` | C# iMES project (batch) |
| `config-csi.yaml` | CSI COBOL codebase (batch) |
| `config.tdas-claude-sdk.yaml` | TDAS COBOL with Claude SDK (1M context) |
| `config.full-context.yaml` | Full context mode for large programs |

## Batch Processing & Checkpoints

```bash
# Process all files matching config filters
python cobol_doc_agent.py --config config-csi.yaml

# Show progress
python cobol_doc_agent.py --config config-csi.yaml --status

# Resume after interruption
python cobol_doc_agent.py --config config-csi.yaml

# Restart from scratch
python cobol_doc_agent.py --config config-csi.yaml --restart

# Retry only failed files
python cobol_doc_agent.py --config config-csi.yaml --retry-failed
```

The checkpoint system tracks per-file status (`PENDING` / `IN_PROGRESS` / `COMPLETED` / `FAILED`) with SHA256 change detection. Interrupted runs resume automatically. Checkpoint state is stored in `.checkpoint.yaml` in the output directory.

## Cross-Reference Metadata (C# / .NET)

For C# projects, the agent can inject verified cross-file and intra-file relationship data into each chunk's LLM prompt. This is powered by OmniSharp (C# language server) via the multilspy MCP server.

### What it provides per chunk

- **Dependencies**: types/methods this chunk uses from other files, with file paths
- **Dependents**: other files that reference symbols defined in this chunk
- **Internal references**: which methods read/write which fields within the file

### How to generate cross-reference metadata

The metadata is pre-generated using a script in `scripts/`:

```bash
# 1. Build the Docker image (first time only)
#    Includes .NET 8.0 SDK + OmniSharp for C# analysis
./scripts/run_multilspy_metadata.sh

# 2. Check progress (long-running: ~90 min for 400+ files)
./scripts/run_multilspy_metadata.sh --status

# 3. Resume if interrupted
./scripts/run_multilspy_metadata.sh --resume

# 4. Copy output to the metadata directory
cp scripts/metadata/{symbol_index,cross_file_edges,intra_file_edges,intra_file_resolved,references_summary}.json \
   ../output/metadata/cross_references/
```

The agent automatically loads cross-reference data from `{metadata_dir}/cross_references/` if present. No config changes needed.

### Scripts

| Script | Purpose |
|--------|---------|
| `scripts/run_multilspy_metadata.sh` | Orchestrator: Docker build, verify, run metadata generation |
| `scripts/generate_multilspy_metadata.py` | Main generator: calls `code_document_symbols` + `code_find_references` via MCP for all `.cs` files. Supports checkpoint/resume and auto-restarts on OmniSharp failures. |
| `scripts/postprocess_metadata.py` | Reconstructs symbol hierarchy from flat metadata (used when OmniSharp returns flat SymbolInformation) |
| `scripts/test_multilspy_minimal.py` | Minimal test with 4 interconnected C# files |
| `scripts/Dockerfile.multilspy-csharp` | Docker image with Python 3.12 + .NET 8.0 SDK |

### MCP Tools Used

| Tool | What it extracts |
|------|-----------------|
| `code_document_symbols` | Hierarchical symbol tree per file (namespace -> class -> method/field/property) |
| `code_find_references` | All locations where each symbol is referenced (cross-file + intra-file) |

## LLM Provider Support

Three provider backends configured via `llm.provider`:

| Provider | Class | Context | Notes |
|----------|-------|---------|-------|
| `openai` | `ChatOpenAI` (LangChain) | 128K | Standard OpenAI API |
| `anthropic` | `ChatAnthropic` (LangChain) | 200K | Standard Anthropic API |
| `claude_sdk` | `ClaudeSdkLLM` | 1M (beta) | Claude Agent SDK, no API key needed, handles >50KB prompts via stdin |

Fallback: configure `llm.fallback` to automatically switch providers on error.

## Architecture

### Core Modules

| Module | Purpose |
|--------|---------|
| `cobol_doc_agent.py` | Main orchestrator: AgentState, three-phase pipeline, CLI |
| `source_chunker.py` | Split source at structural boundaries (no overlap/gaps) |
| `structural_chunker.py` | Alternative chunking via tree-sitter query_code |
| `relationship_provider.py` | Load multilspy metadata, slice cross-references per chunk |
| `claude_sdk_client.py` | LangChain wrapper for Claude Agent SDK |
| `llm_fallback.py` | Provider fallback (primary -> backup on error) |
| `llm_tracer.py` | Track LLM calls: timing, tokens, per-section stats |
| `config_loader.py` | YAML config with `${ENV_VAR}` substitution |
| `mcp_metadata_generator.py` | MCP integration for Docker-based metadata extraction |
| `checkpoint_manager.py` | Batch checkpoint/resume with per-file status tracking |
| `checksum_manager.py` | SHA256 change detection for source and metadata files |
| `tokenizer.py` | Token estimation (tiktoken with character-based fallback) |

### Language Adapters

```
languages/
  cobol/
    adapter.py          # COBOL-specific chunking, boundaries, program map
  dotnet/
    adapter.py          # C#/.NET chunking, structural boundaries, AST filtering
    template.yaml       # C#-specific template with Technical Details, Cross-References
```

Adapters register via `adapter_registry.py`. Each adapter implements:
- `chunk_source_file()` — structural chunking strategy
- `find_structural_boundaries()` — detect class/method/paragraph boundaries
- `generate_program_map()` — hierarchical symbol map
- `filter_ast_for_chunk()` — filter syntax tree to chunk line range

### Template System

Templates are YAML files defining the documentation structure. Each section has:
- `id` — unique identifier
- `title` — section heading
- `instruction` — LLM prompt instructions
- `template` — output format with `{{placeholders}}`

The C# template (`languages/dotnet/template.yaml`) includes per-chunk sections for:
- Technical Details (variables, calls, reads/writes, block type)
- Cross-References (dependencies, dependents, internal refs — from LSP data)
- Call Flow and Data Flow
- Retrieval Questions (10-15 natural language questions for search indexing)
- Retrieval Tags (keywords for hybrid search)
- Chunk Summary (one sentence for ranking)

## Running Tests

```bash
# All tests
python -m pytest tests/ -v

# Single test file
python -m pytest tests/test_mermaid_validator.py -v

# Integration tests
python -m pytest test_chunking_reconstruction.py -v
```

## CLI Reference

```
python cobol_doc_agent.py [program_name] [options]

Positional:
  program_name              Program name (optional if --config or --source-files provided)

Options:
  --config PATH             YAML configuration file (recommended)
  --source-files PATH       Source file or directory for batch processing
  --workspace PATH          Source files directory
  --output-dir PATH         Metadata output directory
  --docs-path PATH          Documentation output path
  --template PATH           Template YAML file
  --generate-metadata       Generate metadata via MCP servers before documentation
  --no-skip-existing        Force regenerate metadata even if it exists
  --restart                 Ignore checkpoint, restart batch from beginning
  --status                  Show checkpoint status and exit
  --retry-failed            Retry only previously failed files
  --continue-on-error       Continue processing if a file fails
  --max-retries N           Max retries for failed files (default: 3)
```

## Requirements

- Python 3.10+
- API key for your chosen LLM provider
- Docker (for MCP metadata generation and multilspy cross-references)
- Node.js (for Claude SDK provider: `npm install -g @anthropic-ai/claude-code`)

## License

MIT License
