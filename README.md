# COBOL Documentation Agent

**AI-powered documentation generator for COBOL codebases using LangGraph and OpenAI GPT-4o**

## Quick Start

### Using YAML Configuration (Recommended)

```bash
# 1. Navigate to agent directory
cd agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set API key
export OPENAI_API_KEY="your-openai-key"

# 4. Configure the agent (edit config.minimal.yaml)
# Update source files path, output paths, LLM settings, etc.

# 5. Run the agent with config file
python cobol_doc_agent.py --config config.minimal.yaml

# 6. View results
cat ../docs/MAINPROG-documentation.md
```

### Using CLI Arguments (Classic Mode)

```bash
# 1-3. Same as above

# 4. Generate documentation for single program
python cobol_doc_agent.py MAINPROG

# 5. View result
cat ../docs/MAINPROG-documentation.md
```

## What This Does

Generates **consistent, comprehensive documentation** for COBOL programs by:
1. Loading metadata from SuperBol LSP, GnuCOBOL Analyzer, and Universal-Ctags
2. Using a YAML template to define documentation structure
3. Using OpenAI GPT-4o to intelligently interpret metadata and generate content
4. Producing Markdown documentation with diagrams, explanations, and code references

## Directory Structure

```
cobol-work/
├── agent/                          ← Work from here
│   ├── cobol_doc_agent.py          # Main agent (LangGraph)
│   ├── cobol-doc-template.yaml     # Documentation template
│   ├── example_usage.py            # Usage examples
│   ├── requirements.txt            # Dependencies
│   ├── test_setup.sh              # Setup verification script
│   ├── QUICK-START.md             # Quick start guide
│   ├── README-COBOL-DOC-AGENT.md  # Comprehensive documentation
│   └── CHANGES.md                 # Recent changes
├── output/                         # Metadata (input)
│   ├── superbol/
│   │   ├── superbol-*-doc-symbols.json
│   │   └── superbol-cfg/*.json
│   ├── gnucobol/
│   │   └── gnucobol-batch-analyze-all.json
│   └── ctags/
│       └── ctags-*-outline.json
└── docs/                           # Generated documentation (output)
    └── *-documentation.md
```

## Key Features

✅ **YAML Configuration**: Configure once, run anywhere - all settings in a single config file
✅ **Intelligent Checksums**: SHA256-based change detection - only regenerates when needed
✅ **Template-Driven**: YAML template ensures consistent structure across all documents
✅ **Metadata-Based**: Uses structured metadata, not direct source parsing
✅ **LLM-Powered**: Supports multiple LLM providers (OpenAI, Anthropic, Google, Azure, Ollama)
✅ **Comprehensive**: Includes CFG, DFG, business logic, call hierarchies, and more
✅ **Mermaid Diagrams**: Automatic generation of flowcharts, sequence diagrams, etc.
✅ **Batch Processing**: Process entire directories with recursive file discovery
✅ **Consistent Output**: Low temperature + explicit constraints = reproducible results  

## Configuration

### YAML Configuration File (Recommended)

Edit `config.minimal.yaml` to configure all settings:

```yaml
# Source files configuration
source:
  mode: batch                     # or "single"
  source_files: ../cobol-source   # Directory or single file
  program_name: MAINPROG          # For single mode

# Checksum-based intelligent metadata generation
validate_checksums:
  source_checksum_file_path: ./source-checksum.yaml
  metadata_checksum_file_path: ./metadata_checksum.yaml

# Output paths
output:
  create_dirs: true
  metadata_dir: ../output
  docs_path: ../docs

# Metadata generation
metadata:
  generate: true                  # Enable intelligent checksum-based generation
  skip_existing: true

# LLM configuration
llm:
  provider: openai                # openai, anthropic, google, azure, ollama
  model: gpt-4o
  api_key: ${OPENAI_API_KEY}      # Use environment variable
  temperature: 0.2

# Documentation template
template:
  path: ./cobol-doc-template.yaml
```

See `CONFIG_GUIDE.md` for complete configuration documentation.

### Template Customization
Edit `cobol-doc-template.yaml` to customize:
- Section structure
- Diagram types
- Detail level
- Output format

## Usage Examples

### Using YAML Configuration (Recommended)

```bash
# 1. Edit config.minimal.yaml to set your preferences
# 2. Run with config file
python cobol_doc_agent.py --config config.minimal.yaml

# 3. Override specific settings via CLI
python cobol_doc_agent.py --config config.minimal.yaml --generate-metadata
```

### CLI Mode - Single Program
```bash
# Using existing metadata
python cobol_doc_agent.py MAINPROG

# With metadata generation
python cobol_doc_agent.py MAINPROG --generate-metadata --workspace ../cobol-source
```

### CLI Mode - Batch Processing
```bash
# Process entire directory (recursive, multiple extensions)
python cobol_doc_agent.py --source-files ../cobol-source --generate-metadata

# Process specific files
for prog in MAINPROG ACCTOPER CUSTMGMT TRANPROC; do
    python cobol_doc_agent.py "$prog"
done
```

### Python API
```python
from cobol_doc_agent import generate_documentation

generate_documentation(
    program_name="MAINPROG",
    workspace_path="../cobol-source",
    metadata_dir="../output",
    template_path="./cobol-doc-template.yaml",
    output_dir="../docs",
    generate_metadata=True,
    source_checksum_path="./source-checksum.yaml",
    metadata_checksum_path="./metadata_checksum.yaml"
)
```

## Checksum-Based Intelligent Metadata Generation

The agent uses SHA256 checksums to intelligently decide when to regenerate metadata:

### How It Works
1. **First Run**: Calculates checksums of all COBOL source files → Generates metadata → Saves checksums
2. **Subsequent Runs**: Compares current checksums with saved checksums
   - ✅ **No changes detected** → Skips metadata generation (saves time!)
   - ⚠️ **Changes detected** → Regenerates metadata automatically
3. **Corruption Detection**: Also validates metadata file checksums to detect incomplete/corrupted metadata

### Benefits
- **⚡ 10x faster** on unchanged files (skips expensive MCP processing)
- **🔒 Automatic validation** - detects corrupted or incomplete metadata
- **📊 Audit trail** - checksum files track all changes with timestamps
- **🔄 Incremental updates** - only regenerates what changed
- **🌲 Nested directory support** - recursively finds all COBOL files
- **📝 Multiple extensions** - supports .COB, .cob, .cbl, .CBL, .COBOL, .cobol, .c74, .C74

### Checksum Files
- `source-checksum.yaml` - SHA256 hashes of all source files
- `metadata-checksum.yaml` - SHA256 hashes of all generated metadata

These files are automatically managed by the agent.

## Documentation Files

- **README.md** (this file) - Overview and quick start
- **config.minimal.yaml** - Minimal YAML configuration example
- **CONFIG_GUIDE.md** - Complete configuration documentation
- **checksum_manager.py** - Checksum system implementation
- **QUICK-START.md** - 5-minute setup guide
- **README-COBOL-DOC-AGENT.md** - Comprehensive documentation
- **WORKFLOW-GUIDE.md** - Detailed workflow explanation
- **CHANGES.md** - Recent updates and changes

## Requirements

- Python 3.10+
- OpenAI API key
- Existing metadata in `../output/` directory:
  - SuperBol LSP output
  - GnuCOBOL analyzer output
  - Universal-ctags output

## Cost Estimate

**OpenAI GPT-4o pricing** (approximate):
- ~$0.10-0.30 per program
- For 16 programs: ~$2-5 total

## Troubleshooting

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "AuthenticationError"
```bash
export OPENAI_API_KEY="sk-..."
echo $OPENAI_API_KEY  # Verify
```

### "FileNotFoundError"
```bash
# Verify metadata exists
./test_setup.sh
```

### "Output varies between runs"
Check temperature setting is low (0.1) in `cobol_doc_agent.py`

## Architecture

Based on **BMAD-METHOD** principles:
- Template defines structure + instructions
- `{{placeholders}}` guide LLM interpretation
- LLM fills templates with metadata-based content
- Consistent structure ensures uniform output

```
Metadata (JSON) → Template (YAML) → LangGraph Agent → LLM (GPT-4o) → Documentation (Markdown)
```

## Contributing

To modify the agent:
1. Edit `cobol-doc-template.yaml` for structure changes
2. Edit `cobol_doc_agent.py` for logic changes
3. Test with `./test_setup.sh`
4. Generate docs and verify consistency

## License

MIT License

## Support

- Read `QUICK-START.md` for setup help
- Read `README-COBOL-DOC-AGENT.md` for detailed documentation
- Check `CHANGES.md` for recent updates
- Run `./test_setup.sh` to diagnose issues
