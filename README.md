# Code Documentation Agent

**AI-powered documentation generator for COBOL and C#/.NET codebases**

Generates comprehensive Markdown documentation by orchestrating LLM calls against metadata extracted from static analysis tools (Universal-Ctags, tree-sitter, tree-sitter-graph, multilspy/OmniSharp). Supports multiple LLM providers (OpenAI, Anthropic, Claude SDK) with automatic fallback.

## Quick Start

```bash
# Install dependencies (Python 3.10+)
pip install -r requirements.txt

# Set API key (choose your provider)
export OPENAI_API_KEY="..."       # for OpenAI
export ANTHROPIC_API_KEY="..."    # for Anthropic
# (claude_sdk provider uses Claude Code CLI auth — no API key needed)

# Run with YAML config (recommended)
python cobol_doc_agent.py --config config-dotnet-imes.yaml

# View results
cat ../output-imes/docs-questions/<PROGRAM>-documentation.md
```

## How It Works

### Three-Phase Documentation Pipeline

```
Source Code + Metadata (ctags / tree-sitter / multilspy)
  |
  v
Phase 1: Source chunking -> per-chunk LLM calls -> code explanation + prose
  |       (structural boundaries, cross-references injected per chunk)
  v
Phase 2: PageIndex + deterministic generators + lambda-RLM planner
  |       (per-section content; cost predictable from input shape)
  v
Phase 3: Assembly -> final Markdown document
  |       (ordered per template, mermaid-validated, questionnaires folded in)
  v
Output: docs/<PROGRAM>-documentation.md
```

**Phase 1** chunks the source file at structural boundaries (class/method for C#, paragraph/section for COBOL) and processes each chunk through the LLM with minimal metadata. Each chunk receives cross-reference context (inter/intra-file relationships) when available. Output is a structured Markdown document with `## Hash-ID:` chunk headers and `#### Block N:` block headers.

**Phase 2** runs each template section through one of three engines, in priority order:

1. **PageIndex preprocess** (`rlm/pageindex.py`) parses the Phase 1 Markdown into a `chunk -> block` tree, persisted to `{docs_path}/page_index/{program}.pageindex.json`. The tree is the input shared by both downstream engines.
2. **Deterministic generators** (`rlm/deterministic.py`) emit Markdown directly from `cross_references` + `page_index` for sections like `control-flow-analysis`, `code-references`, `technical-details`, `metadata-appendix`, `assembly-references`, `document-header`. **Zero LLM calls.** Falls through to the planner on missing metadata.
3. **λ-RLM planner** (`rlm/planner.py`) is the universal catch-all. It runs a single fixed combinator chain per section:

   ```
   Phi = M_synth o REDUCE_CONCAT o MAP(M, leaf_prompt) o FILTER(p, items)
   ```

   `items` are PageIndex blocks by default; sections in `rlm.pairwise_sections` use `CROSS(a_list, b_list)`. The LLM is invoked only at MAP leaves (one call per filtered block) and one synthesis step — **no REPL, no `exec()`, no LLM-authored control flow.** Cost and iteration count are fully predictable from `items_total` / `items_after_filter` (printed in the per-section log).

Routing (Flavor B): `rlm.sections` is the outer allowlist; sections in `rlm.deterministic_sections` try Python first with planner fallback; sections in neither are skipped; `rlm.skip_sections` (e.g. `detailed-code-explanation`) are never re-generated in Phase 2.

After each section, `mermaid_validator.py` validates any ```` ```mermaid ```` blocks via a Docker-based MCP server and asks the LLM to repair invalid diagrams (with the section as context, up to `max_retries`). Post-Phase-2, `questionnaire_aggregator.py` folds every `## Questionnaire for ...` subsection into a synthetic `questionnaires-for-program` section and folds Phase 1 chunk-level retrieval questions into `questionnaires-from-source-code`.

**Phase 3** assembles Phase 1 + Phase 2 outputs in template order and writes `{docs_path}/<source-relative-dir>/<PROGRAM>-documentation-DD-MM-YYYY.md`.

## Supported Languages

| Language | Adapter | Metadata Tools | Extensions |
|----------|---------|----------------|------------|
| **COBOL** | `CobolAdapter` | SuperBol LSP, GnuCOBOL, Universal-Ctags | `.cbl`, `.cob`, `.CBL`, `.COB`, `.c74`, `.C74`, `.XMOD`, `.xmod`, `.XLIB`, `.xlib`, `.xgn`, `.XGN` |
| **C# / .NET** | `DotNetAdapter` | Universal-Ctags, tree-sitter, tree-sitter-graph, multilspy (OmniSharp) | `.cs` |

## Configuration

All settings live in a YAML config file. `config-dotnet-imes.yaml` is the live reference for .NET; `config-csi.yaml` for COBOL. The blocks below are the keys that matter most.

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
  cross_references_dir: ../output/metadata/cross_references/per_file  # multilspy output
  create_dirs: true

llm:
  provider: claude_sdk          # openai, anthropic, claude_sdk
  model: claude-opus-4-6
  temperature: 0.2
  phase1:
    model: claude-opus-4-6
    thinking: disabled
  planner:                      # Phase 2 sub-LLM config (used for MAP leaves + synthesis)
    sub_model: claude-opus-4-6
    max_output_tokens: 64000
    max_thinking_tokens: 0
    leaf_concurrency: 4         # Max concurrent leaf-LLM calls per section
  fallback:                     # Optional: switch provider session-wide on error
    provider: openai
    model: gpt-4o
    planner:
      sub_model: claude-sonnet-4-6
      max_output_tokens: 32000
      leaf_concurrency: 4

pageindex:
  enabled: true
  mode: extract                 # "extract" (zero-LLM, regex-parses Phase 1 md) or "llm"
  include_text: true
  regenerate: true

rlm:                            # Phase 2 routing (Flavor B)
  sections:                     # Outer allowlist
    - executive-summary
    - program-structure
    - control-flow-analysis
    - data-flow-analysis
    - business-logic
    - error-handling
    - technical-details
    - code-references
  skip_sections:                # Never generated in Phase 2 (handled by Phase 1 or assembly)
    - detailed-code-explanation
  deterministic_sections:       # Try Python generator first; fall back to planner
    - document-header
    - control-flow-analysis
    - assembly-references
    - code-references
    - technical-details
    - metadata-appendix
  pairwise_sections: {}         # Optional per-section CROSS items (see below)

mermaid_validator:              # Phase 2 post-processing
  enabled: true
  docker_image: ghcr.io/mcpservershub/mcp-servers/containers/mermaid-mcp-server:sha-c8989d9
  docker_args: [run, -i, --rm]
  tool_name: validate
  max_retries: 3

metadata:                       # Phase 1 metadata generation (MCP servers in Docker)
  generate: true
  skip_existing: true
  servers:
    ctags:
      enabled: true
      docker_image: ghcr.io/mcpservershub/mcp-servers/containers/ctags-mcp-server:sha-c8989d9
      tools: [...]
    tree-sitter:
      enabled: true
      docker_image: ghcr.io/mcpservershub/mcp-servers/containers/tree-sitter-mcp:sha-c8989d9
      tools: [...]
    treesitter-graph:
      enabled: true
      docker_image: ghcr.io/mcpservershub/mcp-servers/containers/tree-sitter-graph-mcp-server:sha-c8989d9
      tools: [...]

template:
  path: ./languages/dotnet/template.yaml

chunking:
  strategy: tsg_graph           # tsg_graph, query_code, ctags
  max_tokens_per_chunk: auto
```

### Pairwise sections

For sections where each fact is the *relationship between two metadata items* (e.g. `inter-program-communication`), set `rlm.pairwise_sections[<id>]` to two dotted paths into the metadata bundle. The planner then runs MAP over `CROSS(a_list, b_list)` instead of PageIndex blocks:

```yaml
rlm:
  pairwise_sections:
    inter-program-communication:
      a: cross_references.cross_file_outgoing
      b: cross_references.cross_file_incoming
```

### Available Config Files

| Config | Purpose |
|--------|---------|
| `config-dotnet-imes.yaml` | C# iMES project (batch) — **canonical reference for .NET + Phase 2** |
| `config-csi.yaml` | CSI COBOL codebase (batch) |
| `config.tdas-claude-sdk.yaml` | TDAS COBOL with Claude SDK (1M context) |
| `config.full-context.yaml` | Full context mode for large programs |
| `config.minimal.yaml` | Minimal COBOL quickstart (no Phase 2 customization) |
| `config.example.yaml` | All options documented |

## MCP Docker Images (auto-pull from registry)

Both `mcp_metadata_generator.py` (Phase 1 metadata) and `mermaid_validator.py` (Phase 2 post-processing) launch MCP servers as Docker containers. The image reference in your YAML can be any string `docker run` accepts — local (`ctags-mcp:test`) or fully-qualified (`ghcr.io/<org>/<image>:<tag>`).

`docker_image_helper.py:ensure_image(ref)` is invoked once per image per process before the container starts:

1. `docker image inspect <ref>` — if exit code 0, the image is present locally; the script continues.
2. Otherwise `docker pull <ref>` — pulls from whatever registry the reference points to (Docker Hub, ghcr.io, ECR, ...).
3. On pull failure (network, auth, missing tag), raises `RuntimeError` with the underlying docker stderr inlined. **Misconfiguration fails fast and loud.**

The per-process cache means batch runs over hundreds of files pull a given image at most once. The default `config-dotnet-imes.yaml` ships fully-qualified references to GitHub Container Registry:

```
ghcr.io/mcpservershub/mcp-servers/containers/ctags-mcp-server:sha-c8989d9
ghcr.io/mcpservershub/mcp-servers/containers/tree-sitter-mcp:sha-c8989d9
ghcr.io/mcpservershub/mcp-servers/containers/tree-sitter-graph-mcp-server:sha-c8989d9
ghcr.io/mcpservershub/mcp-servers/containers/mermaid-mcp-server:sha-c8989d9
```

Tags can be a specific git SHA (as above) or `latest` for floating refs.

## Batch Processing & Checkpoints

```bash
# Process all files matching config filters
python cobol_doc_agent.py --config config-csi.yaml

# Show progress
python cobol_doc_agent.py --config config-csi.yaml --status

# Resume after interruption (default behavior — re-running picks up the checkpoint)
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

# 4. Point the agent at the per-file JSON output via output.cross_references_dir
#    (one JSON per .cs file, named "Path__To__File.cs.json")
```

`output.cross_references_dir` in your YAML tells the agent where to find these files. Phase 2's `rlm/orchestrator.py:_load_cross_references` resolves the per-file JSON automatically by source path.

### Scripts

| Script | Purpose |
|--------|---------|
| `scripts/run_multilspy_metadata.sh` | Orchestrator: Docker build, verify, run metadata generation |
| `scripts/generate_multilspy_metadata.py` | Main generator: calls `code_document_symbols` + `code_find_references` via MCP for all `.cs` files. Supports checkpoint/resume and auto-restarts on OmniSharp failures. |
| `scripts/postprocess_metadata.py` | Reconstructs symbol hierarchy from flat metadata |
| `scripts/split_cross_references.py` | Splits a single project-wide JSON into per-file files matching the `Path__To__File.cs.json` convention |
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
| `claude_sdk` | `ClaudeSdkLLM` | 1M (beta) | Claude Agent SDK; no API key needed (uses Claude Code CLI auth); handles >50KB prompts via stdin |

`llm.fallback` configures session-wide fallback on unrecoverable LLM error. Once triggered, all subsequent calls in the session use the fallback model. Phase 2's planner observes the fallback flag before every leaf and synth call, so the model swap takes effect mid-flight.

The Phase 2 planner's sub-LLM calls go through `rlm/sub_llm.py:call_claude` — a one-shot `claude_agent_sdk.query()` wrapper with retry on transient (429/500/overloaded) errors and `LLMFallbackManager` integration. `ClaudeSDKClient` (the multi-turn class) is not used anywhere — Phase 2 has no multi-turn loops to maintain.

## Architecture

### Core Modules

| Module | Purpose |
|--------|---------|
| `cobol_doc_agent.py` | Main orchestrator: state, three-phase pipeline, CLI |
| `source_chunker.py` | Split source at structural boundaries (no overlap/gaps) |
| `structural_chunker.py` | Alternative chunking via tree-sitter query_code |
| `relationship_provider.py` | Load multilspy metadata, slice cross-references per chunk |
| `claude_sdk_client.py` | LangChain wrapper for Claude Agent SDK |
| `llm_fallback.py` | Provider fallback (primary -> backup on error, session-wide) |
| `llm_tracer.py` | Track LLM calls: timing, tokens, per-section stats |
| `config_loader.py` | YAML config with `${ENV_VAR}` substitution |
| `mcp_metadata_generator.py` | MCP integration for Docker-based metadata extraction (Phase 1) |
| `mermaid_validator.py` | Validate + repair Mermaid diagrams via MCP (Phase 2 post-processing) |
| `questionnaire_aggregator.py` | Fold per-section `Questionnaire for X` blocks into a synthetic section |
| `docker_image_helper.py` | `ensure_image(ref)` — local-check + auto-pull from any registry |
| `checkpoint_manager.py` | Batch checkpoint/resume with per-file status tracking |
| `checksum_manager.py` | SHA256 change detection for source and metadata files |
| `tokenizer.py` | Token estimation (tiktoken with character-based fallback) |

### `rlm/` package (Phase 2)

| Module | Purpose |
|--------|---------|
| `rlm/orchestrator.py` | `run_phase2_rlm()` — top-level dispatcher: PageIndex, routing (Flavor B), mermaid validation, planner-stats summary |
| `rlm/pageindex.py` | Parse Phase 1 Markdown into a `chunk -> block` tree (`extract` mode = zero-LLM regex; `llm` mode = Claude summaries) |
| `rlm/deterministic.py` | Pure-Python generators for `document-header`, `control-flow-analysis`, `assembly-references`, `code-references`, `technical-details`, `metadata-appendix`, `data-flow-analysis` |
| `rlm/planner.py` | λ-RLM combinator chain Φ. Generic leaf and synthesis prompts; no hardcoded section IDs. Coverage logging built in. |
| `rlm/combinators.py` | `MAP`, `FILTER`, `REDUCE_CONCAT`, `CROSS` — pre-verified, deterministic, total |
| `rlm/sub_llm.py` | `call_claude()` — one-shot Claude Agent SDK wrapper with retry + fallback-manager integration |

There is no REPL, no `exec()` of LLM-authored code, and no multi-turn root LLM. The planner's only neural primitive is `llm_fn(prompt) -> str` at MAP leaves and one synthesis step.

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
- `instruction` — LLM prompt guidance (stripped from final output)
- `template` — output format with `{{placeholders}}`

The C# template (`languages/dotnet/template.yaml`) includes per-chunk sections for:
- Technical Details (variables, calls, reads/writes, block type)
- Cross-References (dependencies, dependents, internal refs — from LSP data)
- Call Flow and Data Flow
- Retrieval Questions (10-15 natural language questions per chunk for search indexing)
- Retrieval Tags (keywords for hybrid search)
- Chunk Summary (one sentence for ranking)

## Outputs and Logs

Per run, the agent writes:

| Path | What |
|------|------|
| `{docs_path}/<rel>/<PROGRAM>-documentation-DD-MM-YYYY.md` | Final assembled document |
| `{docs_path}/page_index/<PROGRAM>.pageindex.json` | Phase 2 PageIndex tree |
| `{docs_path}/rlm_logs/coverage/<sec_id>_coverage_<ts>.jsonl` | One JSONL record per planner leaf + synth call (schema compatible with audit tooling) |
| `{metadata_dir}/...` | Per-tool MCP server outputs (ctags, tree-sitter, treesitter-graph, ...) |
| `.checkpoint.yaml` | Batch checkpoint state (per-file status + SHA256) |

## Running Tests

```bash
# All tests
python -m pytest tests/ -v

# Single test file
python -m pytest tests/test_mermaid_validator.py -v

# Integration tests (top-level, ad-hoc; require existing metadata)
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
  --continue-on-error       Continue processing if a file fails (default for batch)
  --max-retries N           Max retries for failed files (default: 3)
```

## Requirements

- Python 3.10+
- Docker (for MCP metadata generation, multilspy cross-references, and mermaid validation; the agent will auto-pull configured images from any registry — ghcr.io, Docker Hub, ECR, ...)
- API key for your chosen LLM provider (or Claude Code CLI for `claude_sdk` provider)
- Node.js (for the `claude_sdk` provider: `npm install -g @anthropic-ai/claude-code`)

## License

MIT License
