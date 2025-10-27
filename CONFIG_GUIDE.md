# Configuration Guide

This guide explains the YAML configuration system for the COBOL Documentation Agent.

## Configuration Files

Two example configuration files are provided:

1. **`config.example.yaml`** - Comprehensive configuration with all available options
2. **`config.minimal.yaml`** - Minimal configuration for quick start

## Quick Start

### 1. Copy a configuration template

```bash
# For minimal setup
cp config.minimal.yaml config.yaml

# For full configuration
cp config.example.yaml config.yaml
```

### 2. Edit your configuration

```bash
# Edit with your preferred editor
nano config.yaml
# or
vim config.yaml
```

### 3. Run the agent with configuration

```bash
python cobol_doc_agent.py --config config.yaml
```

## Configuration Sections

### 1. Source Files (`source`)

Controls what COBOL files to process:

```yaml
source:
  mode: batch  # or 'single'
  source_files: ../cobol-source
  program_name: MAINPROG  # Only for single mode
```

**Options:**
- `mode`: Processing mode
  - `single`: Process one program
  - `batch`: Process all files in directory
- `source_files`: Path to COBOL file or directory
- `program_name`: Program name (required for single mode)

### 2. Output Paths (`output`)

Where to store generated files:

```yaml
output:
  metadata_dir: ../output
  docs_path: ../docs
  create_dirs: true
```

**Options:**
- `metadata_dir`: Directory for metadata (ctags, gnucobol, superbol)
- `docs_path`: Directory for generated documentation
- `create_dirs`: Auto-create directories if they don't exist

### 3. Metadata Generation (`metadata`)

MCP server configuration:

```yaml
metadata:
  generate: true
  skip_existing: true
  force_regenerate: false
  servers:
    ctags:
      enabled: true
      docker_image: ctags-mcp-server:latest
```

**Options:**
- `generate`: Whether to generate metadata via MCP
- `skip_existing`: Skip if metadata files exist
- `force_regenerate`: Force regenerate even if exists
- `servers`: Per-server configuration

### 4. LLM Configuration (`llm`)

**Most Important Section** - Controls which AI model to use:

```yaml
llm:
  provider: openai
  model: gpt-4o
  api_key: ${OPENAI_API_KEY}
  temperature: 0.2
  max_tokens: 4096
```

#### Supported Providers

##### OpenAI

```yaml
llm:
  provider: openai
  model: gpt-4o  # or gpt-4-turbo, gpt-3.5-turbo
  api_key: ${OPENAI_API_KEY}
  temperature: 0.2
```

##### Anthropic (Claude)

```yaml
llm:
  provider: anthropic
  model: claude-3-5-sonnet-20241022
  api_key: ${ANTHROPIC_API_KEY}
  temperature: 0.2
  anthropic:
    max_tokens_to_sample: 4096
```

##### Azure OpenAI

```yaml
llm:
  provider: azure_openai
  model: gpt-4o
  api_key: ${AZURE_OPENAI_API_KEY}
  azure_openai:
    api_base: https://your-resource.openai.azure.com
    api_version: "2024-02-15-preview"
    deployment_name: your-gpt4-deployment
```

##### Google (Gemini)

```yaml
llm:
  provider: google
  model: gemini-1.5-pro
  api_key: ${GOOGLE_API_KEY}
  google:
    project_id: your-project-id
    location: us-central1
```

##### Ollama (Local)

```yaml
llm:
  provider: ollama
  model: llama2  # or mistral, codellama
  ollama:
    base_url: http://localhost:11434
```

##### AWS Bedrock

```yaml
llm:
  provider: bedrock
  model: anthropic.claude-3-sonnet-20240229-v1:0
  bedrock:
    region_name: us-east-1
```

### 5. Template (`template`)

Documentation template configuration:

```yaml
template:
  path: ./cobol-doc-template.yaml
  custom_vars:
    company_name: "Your Company"
    project_name: "COBOL Project"
```

### 6. Batch Processing (`batch`)

For processing multiple files:

```yaml
batch:
  parallel: false
  max_workers: 4
  continue_on_error: true
  generate_report: true
```

### 7. Logging (`logging`)

Control output verbosity:

```yaml
logging:
  level: info  # debug, info, warning, error
  verbose: true
  show_progress: true
```

## Environment Variables

You can use environment variables in the configuration:

```yaml
llm:
  api_key: ${OPENAI_API_KEY}  # References environment variable
```

Set environment variables:

```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
```

## Configuration Precedence

When both CLI arguments and config file are provided:

1. **CLI arguments** take precedence
2. **Config file** values are used as defaults
3. **Built-in defaults** are used if neither is specified

Example:

```bash
# Config file specifies gpt-4o, but CLI overrides to use Claude
python cobol_doc_agent.py --config config.yaml --llm-provider anthropic
```

## Common Configuration Scenarios

### Scenario 1: Generate Metadata + Documentation (OpenAI)

```yaml
source:
  mode: batch
  source_files: ../cobol-source

output:
  metadata_dir: ../output
  docs_path: ../docs

metadata:
  generate: true

llm:
  provider: openai
  model: gpt-4o
  api_key: ${OPENAI_API_KEY}
```

### Scenario 2: Use Existing Metadata with Claude

```yaml
source:
  mode: batch
  source_files: ../cobol-source

output:
  metadata_dir: ../output
  docs_path: ../docs

metadata:
  generate: false  # Use existing metadata

llm:
  provider: anthropic
  model: claude-3-5-sonnet-20241022
  api_key: ${ANTHROPIC_API_KEY}
```

### Scenario 3: Local LLM with Ollama

```yaml
source:
  mode: single
  program_name: MAINPROG

metadata:
  generate: false

llm:
  provider: ollama
  model: codellama
  ollama:
    base_url: http://localhost:11434
```

### Scenario 4: Azure OpenAI for Enterprise

```yaml
source:
  mode: batch
  source_files: ../cobol-source

llm:
  provider: azure_openai
  model: gpt-4o
  api_key: ${AZURE_OPENAI_API_KEY}
  azure_openai:
    api_base: https://your-company.openai.azure.com
    api_version: "2024-02-15-preview"
    deployment_name: gpt4-deployment
```

## Validation

The agent validates the configuration on startup:

- Checks for required fields
- Validates file paths exist
- Verifies provider-specific settings
- Tests API connectivity (optional)

## Tips and Best Practices

1. **Start with minimal config** - Use `config.minimal.yaml` as a starting point
2. **Use environment variables** - Don't commit API keys to version control
3. **Test with single mode** - Validate configuration on one file first
4. **Enable verbose logging** - Helps debug configuration issues
5. **Keep provider configs separate** - Create different config files for different LLMs

## Troubleshooting

### Issue: Configuration file not found

```bash
Error: Configuration file not found: config.yaml
```

**Solution**: Make sure the config file exists and path is correct

### Issue: Invalid YAML syntax

```bash
Error: Failed to parse configuration: ...
```

**Solution**: Validate YAML syntax at https://www.yamllint.com/

### Issue: Missing required field

```bash
Error: Missing required configuration: llm.provider
```

**Solution**: Add the required field to your config file

### Issue: API authentication failed

```bash
Error: OpenAI API authentication failed
```

**Solution**: Check your API key is correct and environment variable is set

## Example: Complete Working Configuration

```yaml
# config.yaml - Complete working example

source:
  mode: batch
  source_files: ../cobol-source

output:
  metadata_dir: ../output
  docs_path: ../docs
  create_dirs: true

metadata:
  generate: true
  skip_existing: true

template:
  path: ./cobol-doc-template.yaml

llm:
  provider: openai
  model: gpt-4o
  api_key: ${OPENAI_API_KEY}
  temperature: 0.2
  max_tokens: 4096

logging:
  level: info
  verbose: true
  show_progress: true

batch:
  continue_on_error: true
  generate_report: true
```

## Next Steps

1. Copy a template: `cp config.minimal.yaml config.yaml`
2. Edit your configuration
3. Set environment variables
4. Run: `python cobol_doc_agent.py --config config.yaml`
5. Review generated documentation in `docs_path`

For more information, see:
- `architecture.md` - System architecture
- `MCP_INTEGRATION_GUIDE.md` - MCP integration details
- `README.md` - General usage guide
