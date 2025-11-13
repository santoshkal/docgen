#!/usr/bin/env python3
"""
Test V2: Enhanced prompt for precise paragraph-level chunking metadata.

Improvements:
1. Focus ONLY on PROCEDURE DIVISION paragraphs
2. Explicit COBOL-74 format instructions
3. Examples of expected output
4. Structured JSON schema with mandatory line numbers
"""

import json
import os
import yaml
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Configuration
COBOL_FILE = "/home/santosh/cobol-work/TDAS-MINDISTCALC.c74"
OUTPUT_JSON = "/home/santosh/cobol-work/agent/llm_chunking_metadata_v2.json"
CONFIG_FILE = "/home/santosh/cobol-work/agent/config-test-detailed-code.yaml"

# Load config
print(f"Loading config: {CONFIG_FILE}")
with open(CONFIG_FILE, 'r') as f:
    config = yaml.safe_load(f)

llm_config = config.get('llm', {})
model = llm_config.get('model', 'gpt-4.1')
api_key_template = llm_config.get('api_key', '')

if api_key_template.startswith('${') and api_key_template.endswith('}'):
    env_var = api_key_template[2:-1]
    api_key = os.environ.get(env_var)
    if not api_key:
        print(f"✗ Error: {env_var} not set!")
        exit(1)
else:
    api_key = api_key_template

print(f"  Model: {model}")

# Initialize LLM
llm = ChatOpenAI(
    model=model,
    temperature=0.0,  # More deterministic
    api_key=api_key,
    model_kwargs={"response_format": {"type": "json_object"}}
)

# Read COBOL source
print(f"\nReading COBOL file: {COBOL_FILE}")
with open(COBOL_FILE, 'r') as f:
    source_lines = f.readlines()
    source_code = ''.join(source_lines)

total_lines = len(source_lines)
estimated_tokens = len(source_code) // 4

print(f"  Total lines: {total_lines:,}")
print(f"  Estimated tokens: ~{estimated_tokens:,}")

# Enhanced prompt - MUCH more specific
prompt = f"""You are a COBOL-74 code analyzer. Your task is to extract EVERY paragraph in the PROCEDURE DIVISION with EXACT line numbers.

## COBOL-74 Format Rules:
- Columns 1-6: Sequence numbers (e.g., "025680")
- Column 7: Indicator (* = comment, / = page break, space = code)
- Columns 8-72: COBOL code area
- Paragraph names start in columns 8-12 and END WITH A PERIOD
- Example: "025680 Z-INITIALIZATION-PARAGRAPH."

## Your Task:
1. Scan through the ENTIRE source file line by line
2. For EVERY line where column 7 is not '*' or '/' AND columns 8+ contain text ending with a period
3. Record that line as a paragraph definition with its EXACT line number
4. Track which paragraphs PERFORM other paragraphs (look for "PERFORM paragraph-name" statements)
5. Identify sections (lines ending with " SECTION.")

## Expected Output Format (JSON ONLY):
{{
  "analysis_method": "line-by-line scan of {total_lines} lines",
  "procedure_division_start": LINE_NUMBER,
  "procedure_division_end": LINE_NUMBER,
  "sections": [
    {{
      "name": "Z-INITIALIZATION",
      "line": EXACT_LINE_NUMBER,
      "paragraphs_in_section": ["PARA-1", "PARA-2"]
    }}
  ],
  "paragraphs": [
    {{
      "name": "Z-INITIALIZATION-PARAGRAPH",
      "line": EXACT_LINE_NUMBER,
      "section": "Z-INITIALIZATION or null",
      "performs": ["OTHER-PARA-1", "OTHER-PARA-2"],
      "performed_by": ["CALLING-PARA"],
      "estimated_lines": APPROX_NUMBER
    }}
  ],
  "perform_graph": [
    {{
      "from_line": LINE_NUMBER,
      "from_paragraph": "CALLER",
      "to_paragraph": "CALLEE",
      "statement": "PERFORM CALLEE"
    }}
  ],
  "suggested_semantic_chunks": [
    {{
      "chunk_id": 1,
      "description": "Initialization and setup",
      "paragraph_names": ["PARA-1", "PARA-2", "PARA-3"],
      "start_line": FIRST_PARA_LINE,
      "end_line": LAST_PARA_LINE,
      "rationale": "These paragraphs form initialization workflow"
    }}
  ]
}}

## Critical Rules:
1. MUST include exact line number for EVERY paragraph
2. MUST extract ALL paragraphs (expect ~2000-3000 in this file)
3. Line numbers are 1-indexed (first line = line 1)
4. Look at sequence numbers in columns 1-6 to help track position
5. ONLY output valid JSON, nothing else

## Example of what you're looking for:
```
025680 Z-INITIALIZATION-PARAGRAPH.       ← This is line 12836, paragraph name
025682     PERFORM Z-PROCESS-INIT.       ← PERFORM statement, track this
025684     MOVE SPACES TO WS-FLAG.
025686 Z-MAIN-CONTROL-PARAGRAPH.         ← This is a new paragraph at different line
```

Here is the complete COBOL-74 source code ({total_lines} lines):

{source_code}
"""

print(f"\nSending enhanced prompt to LLM: {model}")
print(f"  Prompt tokens: ~{len(prompt)//4:,}")
print(f"  Waiting for response (this may take 60-90 seconds)...\n")

# Call LLM
try:
    messages = [
        SystemMessage(content="You are a COBOL-74 parser. Extract ALL paragraphs with exact line numbers. Output ONLY valid JSON."),
        HumanMessage(content=prompt)
    ]

    response = llm.invoke(messages)
    result = response.content

    # Get usage stats
    usage_metadata = getattr(response, 'response_metadata', {}).get('token_usage', {})
    prompt_tokens = usage_metadata.get('prompt_tokens', 'N/A')
    completion_tokens = usage_metadata.get('completion_tokens', 'N/A')
    total_tokens = usage_metadata.get('total_tokens', 'N/A')

    print(f"✓ LLM Response received!")
    if prompt_tokens != 'N/A':
        print(f"  Prompt tokens: {prompt_tokens:,}")
        print(f"  Completion tokens: {completion_tokens:,}")
        print(f"  Total tokens: {total_tokens:,}")

    # Parse JSON
    metadata = json.loads(result)

    # Save to file
    with open(OUTPUT_JSON, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"\n✓ Saved to: {OUTPUT_JSON}")

    # Detailed analysis
    print(f"\n=== Enhanced Analysis Results ===")

    sections = metadata.get('sections', [])
    paragraphs = metadata.get('paragraphs', [])
    performs = metadata.get('perform_graph', [])
    chunks = metadata.get('suggested_semantic_chunks', [])

    print(f"Sections found: {len(sections)}")
    print(f"Paragraphs found: {len(paragraphs)}")
    print(f"PERFORM relationships: {len(performs)}")
    print(f"Suggested semantic chunks: {len(chunks)}")

    # Validate we got line numbers
    paragraphs_with_lines = [p for p in paragraphs if 'line' in p and p['line'] > 0]
    print(f"\nParagraphs with line numbers: {len(paragraphs_with_lines)}/{len(paragraphs)}")

    if paragraphs:
        print(f"\nFirst 10 paragraphs:")
        for p in paragraphs[:10]:
            line = p.get('line', 'MISSING')
            name = p.get('name', 'N/A')
            section = p.get('section', None)
            performs_count = len(p.get('performs', []))
            print(f"  Line {line:6}: {name:40} (section: {section or 'none'}, performs: {performs_count})")

    if sections:
        print(f"\nSections found:")
        for s in sections:
            line = s.get('line', 'MISSING')
            name = s.get('name', 'N/A')
            para_count = len(s.get('paragraphs_in_section', []))
            print(f"  Line {line:6}: {name:40} ({para_count} paragraphs)")

    if chunks:
        print(f"\nSuggested semantic chunks:")
        for chunk in chunks[:5]:
            print(f"  Chunk {chunk.get('chunk_id')}: {chunk.get('description')}")
            print(f"    Lines {chunk.get('start_line')}-{chunk.get('end_line')}")
            print(f"    Paragraphs: {len(chunk.get('paragraph_names', []))}")
            print(f"    Rationale: {chunk.get('rationale', 'N/A')[:80]}...")

    # Comparison with CTags
    print(f"\n=== Comparison with CTags ===")
    print(f"Expected paragraphs (from CTags): 2,598")
    print(f"LLM extracted paragraphs: {len(paragraphs)}")
    coverage = (len(paragraphs) / 2598) * 100 if paragraphs else 0
    print(f"Coverage: {coverage:.1f}%")

    if coverage < 50:
        print(f"\n⚠ WARNING: Low coverage! LLM may have missed many paragraphs.")
        print(f"   This suggests CTags is more reliable for boundary detection.")
    elif coverage > 90:
        print(f"\n✓ Good coverage! LLM found most paragraphs.")
        print(f"   However, verify accuracy by comparing line numbers with CTags.")

    print(f"\n✓ Test complete! Review {OUTPUT_JSON} for detailed results.")

except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
