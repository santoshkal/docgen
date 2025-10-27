# MCP Integration Guide - COBOL Documentation Agent

## Overview

The COBOL Documentation Agent has been enhanced with **Model Context Protocol (MCP) integration**, allowing it to automatically generate metadata from COBOL source files before creating documentation.

This enhancement makes the agent **fully autonomous** - it can now:
1. Start Docker-based MCP servers
2. Extract metadata from COBOL source files concurrently
3. Generate comprehensive documentation using the extracted metadata

---

## Architecture

### Workflow

```
[Start]
   |
   v
[Should Generate Metadata?] ──No──> [Load Existing Metadata]
   |                                        |
   Yes                                     |
   |                                        |
   v                                        |
[Generate Metadata via MCP]                |
   |                                        |
   | - Start 3 Docker MCP Servers          |
   | - ctags-mcp-server                    |
   | - gnucobol-mcp-server                 |
   | - superbol-lsp-mcp-server             |
   |                                        |
   | - Generate metadata concurrently      |
   | - Write to output directory           |
   | - Cleanup Docker containers           |
   |                                        |
   v                                        |
[Load Metadata] <──────────────────────────┘
   |
   v
[Load Template]
   |
   v
[Generate Documentation Sections]
   |
   v
[Assemble & Save Document]
   |
   v
[End]
```

### Components

1. **`mcp_metadata_generator.py`** - MCP integration module
   - Docker container lifecycle management
   - MCP client configuration using `mcp-use` library
   - Concurrent metadata generation from 3 MCP servers
   - JSON output writing

2. **`cobol_doc_agent.py`** (Enhanced)
   - New `generate_metadata_node` for MCP metadata generation
   - Conditional routing via `should_generate_metadata`
   - Extended `AgentState` with metadata generation flags
   - Updated CLI with new parameters

3. **Docker-based MCP Servers**
   - **ctags-mcp-server**: Universal tags, symbols, outlines
   - **gnucobol-mcp-server**: COBOL analysis, call graphs
   - **superbol-lsp-mcp-server**: LSP symbols, CFG generation

---

## Installation

### 1. Install Dependencies

```bash
cd /home/santosh/cobol-work/agent
source .venv/bin/activate
pip install -r requirements.txt
```

**New dependency added**: `mcp-use>=0.1.0`

### 2. Verify Docker

Ensure Docker is installed and running:

```bash
docker --version
docker ps
```

### 3. Pull MCP Server Images (Optional)

Pre-pull images for faster startup:

```bash
docker pull ghcr.io/mcpservershub/mcp-servers/containers/ctags-mcp-server:sha-ab75899
docker pull ghcr.io/mcpservershub/mcp-servers/containers/gnucobol-mcp-server:sha-62a3014
docker pull ghcr.io/mcpservershub/mcp-servers/containers/custom-lsp-client-mcp-server:sha-ab75899
```

---

##Usage

### Mode 1: Documentation Only (Existing Behavior)

Generate documentation using **existing metadata**:

```bash
python cobol_doc_agent.py MAINPROG
```

This skips metadata generation and directly loads from `../output/`.

---

### Mode 2: Metadata + Documentation (New)

Generate metadata **and** documentation in one command:

```bash
python cobol_doc_agent.py MAINPROG --generate-metadata --workspace /path/to/cobol/source
```

**What happens:**
1. Starts 3 Docker MCP servers
2. Mounts `/path/to/cobol/source` as `/workspace` in containers
3. Generates metadata for all `*.COB` files concurrently
4. Writes metadata to `../output/{ctags,gnucobol,superbol}/`
5. Stops Docker containers (auto-cleanup via `--rm`)
6. Generates documentation using the fresh metadata

---

### Mode 3: Force Regenerate Metadata

Force metadata regeneration even if files exist:

```bash
python cobol_doc_agent.py MAINPROG --generate-metadata --no-skip-existing --workspace /path/to/cobol
```

---

### CLI Parameters

```
python cobol_doc_agent.py <PROGRAM_NAME> [OPTIONS]

Positional Arguments:
  program_name              Name of COBOL program (e.g., MAINPROG)

Optional Arguments:
  --workspace PATH          Path to COBOL source files directory (default: ..)
  --metadata-dir PATH       Metadata directory (default: ../output)
  --template PATH           Documentation template (default: ./cobol-doc-template.yaml)
  --output-dir PATH         Output directory for documentation (default: ../docs)
  --generate-metadata       Generate metadata via MCP servers before documentation
  --no-skip-existing        Force regenerate metadata even if it exists

Examples:
  # Generate documentation using existing metadata
  python cobol_doc_agent.py MAINPROG

  # Generate metadata AND documentation
  python cobol_doc_agent.py MAINPROG --generate-metadata --workspace /path/to/cobol

  # Force regenerate metadata
  python cobol_doc_agent.py MAINPROG --generate-metadata --no-skip-existing
```

---

## MCP Metadata Generator Module

### Standalone Usage

The metadata generator can be used independently:

```bash
python mcp_metadata_generator.py /path/to/cobol/workspace /path/to/output
```

### Programmatic Usage

```python
from mcp_metadata_generator import generate_metadata_sync

# Generate metadata for specific COBOL files
generate_metadata_sync(
    workspace_path="/path/to/cobol",
    output_dir="./output",
    cobol_files=["MAINPROG.COB", "CUSTOMER.COB", "ACCTOPER.COB"]
)
```

### Async Usage

```python
from mcp_metadata_generator import MCPMetadataGenerator
import asyncio

async def main():
    generator = MCPMetadataGenerator(
        workspace_path="/path/to/cobol",
        output_base_dir="./output"
    )

    cobol_files = ["MAINPROG.COB", "CUSTOMER.COB"]
    await generator.generate_all_metadata(cobol_files)

asyncio.run(main())
```

---

## MCP Server Configuration

### How `mcp-use` Works

The `mcp-use` library handles:
- Starting Docker containers via `docker run` commands
- Establishing stdio communication
- Managing container lifecycle (cleanup via `--rm`)

### Configuration Structure

```python
{
    "mcpServers": {
        "ctags": {
            "command": "docker",
            "args": [
                "run", "-i", "--rm",
                "-v", "/workspace:/workspace:ro",
                "-v", "/output/ctags:/workspace/output",
                "ghcr.io/mcpservershub/mcp-servers/containers/ctags-mcp-server:sha-ab75899"
            ]
        },
        # ... gnucobol, superbol
    }
}
```

**Key flags:**
- `-i`: Interactive mode for stdio communication
- `--rm`: Auto-remove container when stopped
- `-v`: Volume mounts for source code and output

---

## Metadata Output Structure

```
output/
├── ctags/
│   ├── cobol-project.tags          # Universal ctags file
│   ├── project-symbols.json        # Project-wide symbols
│   ├── ctags-MAINPROG-outline.json # Per-program outline
│   ├── ctags-CUSTOMER-outline.json
│   └── ...
│
├── gnucobol/
│   └── gnucobol-batch-analyze-all.json  # Batch analysis of all programs
│
└── superbol/
    ├── superbol-MAINPROG-doc-symbols.json  # LSP document symbols
    ├── superbol-CUSTOMER-doc-symbols.json
    ├── ...
    └── superbol-cfg/                       # Control flow graphs
        ├── MAINPROG.json
        ├── CUSTOMER.json
        └── ...
```

---

## MCP Server Details

### 1. Ctags MCP Server

**Image**: `ghcr.io/mcpservershub/mcp-servers/containers/ctags-mcp-server:sha-ab75899`

**Tools Used:**
- `generate_tags` - Generate Universal Ctags file
- `generate_project_symbols` - Extract project symbols
- `generate_project_outline` - Generate per-file outlines

**Output:**
- Tags file with all COBOL symbols
- Project-level symbol index
- Per-program code structure outlines

### 2. GnuCOBOL MCP Server

**Image**: `ghcr.io/mcpservershub/mcp-servers/containers/gnucobol-mcp-server:sha-62a3014`

**Tools Used:**
- `batch_analyze` - Analyze multiple COBOL files at once

**Output:**
- Program call graphs
- Call frequency analysis
- Per-file analysis results
- System-wide call summary

### 3. SuperBol LSP MCP Server

**Image**: `ghcr.io/mcpservershub/mcp-servers/containers/custom-lsp-client-mcp-server:sha-ab75899`

**Tools Used:**
- `code_document_symbol` - LSP document symbols per file
- `cobol-generate_cfg_project` - Control flow graphs for all files

**Output:**
- LSP-based document symbols
- Control flow graphs (CFG) in JSON format
- Per-program CFG files

---

## Concurrent Execution

The metadata generator runs all 3 MCP servers **concurrently** using `asyncio.gather()`:

```python
await asyncio.gather(
    self.generate_ctags_metadata(cobol_files),
    self.generate_gnucobol_metadata(cobol_files),
    self.generate_superbol_metadata(cobol_files),
    return_exceptions=True
)
```

**Benefits:**
- Faster execution (3 servers run in parallel)
- If one server fails, others continue
- Errors are collected and reported

---

## Error Handling

### Graceful Degradation

If metadata generation fails:
1. Error is logged to `state["errors"]`
2. Agent attempts to load existing metadata
3. Documentation generation continues if metadata exists

### Container Cleanup

Docker containers are automatically cleaned up via:
- `--rm` flag in `docker run`
- Exception handling ensures cleanup even on errors

### Debugging

Check Docker containers:
```bash
docker ps -a | grep mcp
```

View container logs:
```bash
docker logs <container_id>
```

---

## Performance

### Expected Times

**Single Program (with metadata generation):**
- Metadata generation: 30-60 seconds (concurrent)
- Documentation generation: 30-60 seconds (LLM calls)
- **Total**: ~1-2 minutes

**Batch (16 programs):**
- Metadata generation: ~1 minute (once for all files)
- Documentation generation: ~10-15 minutes (11 sections × 16 programs)
- **Total**: ~11-16 minutes

### Optimization

Metadata generation is done **once** for all programs:
- Ctags: Generates project-wide tags file
- GnuCOBOL: Batch analyzes all files together
- SuperBol: Processes all files in one CFG generation

Subsequent documentation runs skip metadata if `--skip-existing` (default).

---

## Troubleshooting

### Issue: "docker: command not found"
**Solution**: Install Docker and ensure it's in PATH

### Issue: "permission denied while trying to connect to Docker daemon"
**Solution**: Add user to docker group
```bash
sudo usermod -aG docker $USER
newgrp docker
```

### Issue: "No module named 'mcp_use'"
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: "No COBOL files (*.COB) found"
**Solution**: Ensure workspace path is correct and contains `*.COB` files

### Issue: MCP tool returns error
**Solution**: Check MCP server logs
```bash
docker logs $(docker ps -a | grep mcp-ctags | awk '{print $1}')
```

---

## Advanced Usage

### Custom MCP Configuration

Modify `mcp_metadata_generator.py` to customize MCP server configurations:

```python
def get_mcp_config(self) -> Dict[str, Any]:
    config = {
        "mcpServers": {
            "ctags": {
                "command": "docker",
                "args": [
                    "run", "-i", "--rm",
                    "-v", f"{self.workspace_path}:/workspace:ro",
                    "-v", f"{self.output_base_dir / 'ctags'}:/workspace/output",
                    # Add custom environment variables
                    "-e", "CTAGS_OPTIONS=--fields=+n",
                    "ghcr.io/mcpservershub/mcp-servers/containers/ctags-mcp-server:sha-ab75899"
                ]
            },
            # ... other servers
        }
    }
    return config
```

### Extending with Additional MCP Servers

To add more MCP servers:

1. Add server configuration to `get_mcp_config()`
2. Create new `generate_<server>_metadata()` method
3. Add to `asyncio.gather()` in `generate_all_metadata()`

---

## Future Enhancements

Potential improvements:
1. **Parallel documentation generation** for multiple programs
2. **Incremental metadata updates** (only regenerate for changed files)
3. **MCP server pooling** (reuse containers across runs)
4. **Progress bars** for long-running operations
5. **Web UI** for metadata and documentation management

---

## References

- [MCP-Use Python Library](https://github.com/mcp-use/mcp-use)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [MCP Servers Hub](https://github.com/mcpservershub)

---

*Last Updated: 2025-10-17*
*Version: 1.0*
