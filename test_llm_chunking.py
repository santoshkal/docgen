#!/usr/bin/env python3
"""
Test: Use LLM to analyze COBOL source and generate semantic chunking metadata.

Goal: Ask LLM to read complete source file and output JSON with:
- Code blocks (with line ranges)
- Symbol names for pattern matching
- Semantic relationships between blocks
"""

import json
import os
import yaml
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Configuration
COBOL_FILE = "/home/santosh/cobol-work/TDAS-MINDISTCALC.c74"
OUTPUT_JSON = "/home/santosh/cobol-work/agent/llm_chunking_metadata.json"
CONFIG_FILE = "/home/santosh/cobol-work/agent/config-test-detailed-code.yaml"

# Load config to get API key and model
print(f"Loading config: {CONFIG_FILE}")
with open(CONFIG_FILE, 'r') as f:
    config = yaml.safe_load(f)

llm_config = config.get('llm', {})
model = llm_config.get('model', 'gpt-4.1')
api_key_template = llm_config.get('api_key', '')

# Expand environment variables in API key
if api_key_template.startswith('${') and api_key_template.endswith('}'):
    env_var = api_key_template[2:-1]
    api_key = os.environ.get(env_var)
    if not api_key:
        print(f"✗ Error: Environment variable {env_var} not set!")
        print(f"   Run: export {env_var}='your-key'")
        exit(1)
else:
    api_key = api_key_template

print(f"  Model: {model}")
print(f"  API key: {api_key[:10]}..." if api_key else "  API key: NOT SET")

# Initialize LLM
llm = ChatOpenAI(
    model=model,
    temperature=0.1,
    api_key=api_key,
    model_kwargs={"response_format": {"type": "json_object"}}
)

# Read COBOL source
print(f"Reading COBOL file: {COBOL_FILE}")
with open(COBOL_FILE, 'r') as f:
    source_lines = f.readlines()
    source_code = ''.join(source_lines)

total_lines = len(source_lines)
estimated_tokens = len(source_code) // 4

print(f"  Total lines: {total_lines:,}")
print(f"  Total chars: {len(source_code):,}")
print(f"  Estimated tokens: ~{estimated_tokens:,}")

# Prepare prompt
prompt = f"""You are a COBOL code analyzer. Analyze this COBOL-74 source file and generate semantic chunking metadata.

TASK: Read the entire source code and output ONLY valid JSON (no markdown, no explanation) with this structure:

{{
  "file": "TDAS-MINDISTCALC.c74",
  "total_lines": {total_lines},
  "semantic_blocks": [
    {{
      "block_id": 1,
      "type": "section|paragraph|data-division|procedure-division",
      "name": "NAME-OF-PARAGRAPH",
      "start_line": 100,
      "end_line": 150,
      "symbols": ["SYMBOL1", "SYMBOL2"],
      "performs": ["PARA-CALLED-1", "PARA-CALLED-2"],
      "called_by": ["PARA-CALLER-1"],
      "semantic_group": "initialization|validation|processing|cleanup|etc",
      "description": "Brief purpose of this block"
    }}
  ],
  "semantic_relationships": [
    {{
      "from_block": 1,
      "to_block": 5,
      "relationship": "performs|calls|depends-on|data-flow",
      "description": "Why these blocks are related"
    }}
  ],
  "suggested_chunks": [
    {{
      "chunk_id": 1,
      "block_ids": [1, 2, 3],
      "start_line": 100,
      "end_line": 500,
      "purpose": "Why these blocks should stay together",
      "estimated_tokens": 25000
    }}
  ]
}}

IMPORTANT RULES:
1. Extract ALL paragraphs, sections, and divisions
2. Track PERFORM statements to identify paragraph relationships
3. Identify semantic groups (e.g., initialization, validation, business logic, cleanup)
4. Suggest chunks that preserve semantic relationships
5. Each chunk should be ~100K tokens max
6. Preserve COBOL-74 line numbering (columns 1-6)
7. Output ONLY JSON, nothing else

Here is the complete COBOL source code:

{source_code}
"""

print(f"\nSending to LLM: {model}")
print(f"  Prompt tokens: ~{len(prompt)//4:,}")
print(f"  Waiting for response...\n")

# Call LLM
try:
    messages = [
        SystemMessage(content="You are a COBOL code analysis expert. Output only valid JSON."),
        HumanMessage(content=prompt)
    ]

    response = llm.invoke(messages)

    # Extract response
    result = response.content

    # Try to get usage stats if available
    usage_metadata = getattr(response, 'response_metadata', {}).get('token_usage', {})
    prompt_tokens = usage_metadata.get('prompt_tokens', 'N/A')
    completion_tokens = usage_metadata.get('completion_tokens', 'N/A')
    total_tokens = usage_metadata.get('total_tokens', 'N/A')

    print(f"✓ LLM Response received!")
    if prompt_tokens != 'N/A':
        print(f"  Prompt tokens: {prompt_tokens:,}")
        print(f"  Completion tokens: {completion_tokens:,}")
        print(f"  Total tokens: {total_tokens:,}")
    print(f"  Model used: {model}")

    # Parse JSON
    metadata = json.loads(result)

    # Save to file
    with open(OUTPUT_JSON, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"\n✓ Saved to: {OUTPUT_JSON}")

    # Print summary
    print(f"\n=== Analysis Summary ===")
    print(f"Semantic blocks found: {len(metadata.get('semantic_blocks', []))}")
    print(f"Relationships found: {len(metadata.get('semantic_relationships', []))}")
    print(f"Suggested chunks: {len(metadata.get('suggested_chunks', []))}")

    if metadata.get('semantic_blocks'):
        print(f"\nFirst 5 semantic blocks:")
        for block in metadata['semantic_blocks'][:5]:
            print(f"  - {block.get('name', 'N/A')} (lines {block.get('start_line')}-{block.get('end_line')})")
            print(f"    Type: {block.get('type')}, Group: {block.get('semantic_group', 'N/A')}")

    if metadata.get('suggested_chunks'):
        print(f"\nSuggested chunks:")
        for chunk in metadata['suggested_chunks'][:3]:
            print(f"  Chunk {chunk.get('chunk_id')}: Lines {chunk.get('start_line')}-{chunk.get('end_line')}")
            print(f"    Purpose: {chunk.get('purpose', 'N/A')}")
            print(f"    Estimated tokens: ~{chunk.get('estimated_tokens', 0):,}")

    print(f"\n✓ Test complete! Review {OUTPUT_JSON} for full results.")

except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
