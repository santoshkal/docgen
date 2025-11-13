#!/usr/bin/env python3
"""
Test V3: Enhanced with Accountability Requirements (No Chunking)

This version:
1. Provides COMPLETE source code to LLM (like v2)
2. Adds strict accountability requirements (like our YAML template)
3. Requires completion checklist
4. Demands line-by-line processing
5. Makes skipped content obvious through missing line numbers
"""

import json
import os
import yaml
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Configuration
COBOL_FILE = "/home/santosh/cobol-work/TDAS-MINDISTCALC.c74"
OUTPUT_JSON = "/home/santosh/cobol-work/agent/llm_chunking_metadata_v3_accountability.json"
CONFIG_FILE = "/home/santosh/cobol-work/agent/config-test-detailed-code.yaml"

print("="*80)
print("TEST V3: ACCOUNTABILITY-ENHANCED PROMPT (NO CHUNKING)")
print("="*80)

# Load config
print(f"\n[1] Loading config: {CONFIG_FILE}")
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
    temperature=0.0,  # Deterministic
    api_key=api_key,
    model_kwargs={"response_format": {"type": "json_object"}}
)

# Read COBOL source
print(f"\n[2] Reading COBOL file: {COBOL_FILE}")
with open(COBOL_FILE, 'r') as f:
    source_lines = f.readlines()
    source_code = ''.join(source_lines)

total_lines = len(source_lines)
estimated_tokens = len(source_code) // 4

print(f"  Total lines: {total_lines:,}")
print(f"  Estimated tokens: ~{estimated_tokens:,}")

# ENHANCED PROMPT with ACCOUNTABILITY (similar to YAML template)
prompt = f"""You are a COBOL-74 code analyzer. Your task is to extract EVERY paragraph and section in the PROCEDURE DIVISION with EXACT line numbers.

=============================================================================
MANDATORY ACCOUNTABILITY REQUIREMENTS
=============================================================================
⚠️  CRITICAL - YOU MUST:

1. **Process EVERY line from line 1 to line {total_lines} sequentially**
2. **Extract EVERY paragraph/section in the order it appears**
3. **Record exact line number for each paragraph/section**
4. **Process in strict sequential order** - no jumping around
5. **At the end, provide a completion checklist** with ALL paragraphs found
6. **Missing line numbers will make skipped content immediately obvious**
7. **NO SUMMARIZATION** - Extract every single paragraph, even if repetitive
8. **NEVER skip content** - If you skip paragraphs, it will be obvious from gaps in line numbers

**BLOCK-BY-BLOCK ACCOUNTABILITY:**
- Each paragraph must be listed with: Name, Line Number, Sequence Number
- If you extract 100 paragraphs, you MUST have 100 entries in the checklist
- Gaps in line numbers will expose incomplete extraction
- Expected: ~2,500-2,600 paragraphs (compare your count to this)

=============================================================================
COBOL-74 FORMAT RULES
=============================================================================
- **Columns 1-6**: Sequence numbers (e.g., "025680")
- **Column 7**: Indicator (* = comment, / = page break, space = code)
- **Columns 8-72**: COBOL code area
- **Paragraph names**: Start in columns 8-12 and END WITH A PERIOD
- **Section names**: End with " SECTION."
- **Example**: "025680 Z-INITIALIZATION-PARAGRAPH."

=============================================================================
YOUR TASK
=============================================================================
1. **Scan through the ENTIRE source file line by line** (all {total_lines} lines)
2. **For EVERY line** where:
   - Column 7 is not '*' or '/' (not a comment)
   - Columns 8+ contain text ending with a period
   - The text looks like a paragraph or section name
3. **Record it** with:
   - Exact line number (1-indexed)
   - Sequence number (from columns 1-6)
   - Paragraph/section name
   - Any PERFORM statements it contains
4. **Track PERFORM relationships**: Look for "PERFORM paragraph-name" statements
5. **Generate completion checklist**: List ALL paragraphs found with line numbers

=============================================================================
EXPECTED OUTPUT FORMAT (JSON ONLY)
=============================================================================
{{
  "analysis_method": "line-by-line scan of {total_lines} lines with accountability",
  "procedure_division_start_line": LINE_NUMBER,
  "procedure_division_end_line": LINE_NUMBER,
  "total_lines_processed": {total_lines},
  "sections": [
    {{
      "name": "Z-INITIALIZATION",
      "line": EXACT_LINE_NUMBER,
      "sequence_number": "025680",
      "paragraphs_in_section": ["PARA-1", "PARA-2"]
    }}
  ],
  "paragraphs": [
    {{
      "name": "Z-INITIALIZATION-PARAGRAPH",
      "line": EXACT_LINE_NUMBER,
      "sequence_number": "025680",
      "section": "Z-INITIALIZATION or null",
      "performs": ["OTHER-PARA-1", "OTHER-PARA-2"],
      "estimated_end_line": APPROX_LINE_NUMBER
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
  "statistics": {{
    "total_sections": COUNT,
    "total_paragraphs": COUNT,
    "total_performs": COUNT,
    "expected_paragraphs": 2598,
    "coverage_percentage": "(YOUR_COUNT / 2598) * 100"
  }},
  "completion_checklist": [
    "✓ PARAGRAPH-NAME (Line X, Seq NNNNNN) - Brief note",
    "✓ NEXT-PARAGRAPH (Line Y, Seq NNNNNN) - Brief note"
  ]
}}

=============================================================================
CRITICAL RULES (READ CAREFULLY)
=============================================================================
1. **MUST include exact line number for EVERY paragraph** (no exceptions)
2. **MUST extract ALL paragraphs** - expect ~2,500-2,600 total
3. **Line numbers are 1-indexed** (first line = line 1)
4. **Use sequence numbers** (columns 1-6) to help track position
5. **ONLY output valid JSON**, nothing else
6. **DO NOT SKIP CONTENT** even if paragraphs look similar
7. **Completion checklist is MANDATORY** - list every paragraph found
8. **Missing line numbers expose incomplete work** - gaps will be obvious

=============================================================================
EXAMPLES OF WHAT YOU'RE LOOKING FOR
=============================================================================
```
025680 Z-INITIALIZATION-PARAGRAPH.       ← Line 12836, paragraph name
025682     PERFORM Z-PROCESS-INIT.       ← PERFORM statement, track this
025684     MOVE SPACES TO WS-FLAG.       ← Regular statement, skip
025686 Z-MAIN-CONTROL-PARAGRAPH.         ← Line 12838, new paragraph
025688     PERFORM Z-VALIDATE.           ← Another PERFORM, track this
...
026754 Z-35-XIT.                         ← Line 26754, last paragraph
026756     EXIT.
```

You MUST extract ALL paragraphs from line 1 to line {total_lines}.

=============================================================================
COMPLETE COBOL-74 SOURCE CODE ({total_lines:,} lines)
=============================================================================

{source_code}

=============================================================================
NOW BEGIN EXTRACTION
=============================================================================
Extract ALL paragraphs with exact line numbers.
Provide completion checklist at the end.
Output ONLY valid JSON.
"""

print(f"\n[3] Sending accountability-enhanced prompt to LLM: {model}")
print(f"  Prompt tokens: ~{len(prompt)//4:,}")
print(f"  Waiting for response (this may take 60-90 seconds)...\n")

# Call LLM
try:
    messages = [
        SystemMessage(content="You are a COBOL-74 parser with strict accountability requirements. Extract ALL paragraphs with exact line numbers. Provide completion checklist. Output ONLY valid JSON."),
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
    print(f"\n{'='*80}")
    print(f"ACCOUNTABILITY-ENHANCED RESULTS ANALYSIS")
    print(f"{'='*80}")

    sections = metadata.get('sections', [])
    paragraphs = metadata.get('paragraphs', [])
    performs = metadata.get('perform_graph', [])
    checklist = metadata.get('completion_checklist', [])
    stats = metadata.get('statistics', {})

    print(f"\nExtraction Results:")
    print(f"  Sections found: {len(sections)}")
    print(f"  Paragraphs found: {len(paragraphs)}")
    print(f"  PERFORM relationships: {len(performs)}")
    print(f"  Checklist items: {len(checklist)}")

    # Validate line numbers
    paragraphs_with_lines = [p for p in paragraphs if 'line' in p and p['line'] > 0]
    print(f"\nData Quality:")
    print(f"  Paragraphs with valid line numbers: {len(paragraphs_with_lines)}/{len(paragraphs)}")

    # Show sample paragraphs
    if paragraphs:
        print(f"\nFirst 15 paragraphs:")
        for p in sorted(paragraphs, key=lambda x: x.get('line', 0))[:15]:
            line = p.get('line', 'MISSING')
            name = p.get('name', 'N/A')
            seq = p.get('sequence_number', 'N/A')
            performs_count = len(p.get('performs', []))
            print(f"  Line {line:6} (seq {seq}): {name:45} performs: {performs_count}")

        print(f"\nLast 15 paragraphs:")
        for p in sorted(paragraphs, key=lambda x: x.get('line', 0))[-15:]:
            line = p.get('line', 'MISSING')
            name = p.get('name', 'N/A')
            seq = p.get('sequence_number', 'N/A')
            performs_count = len(p.get('performs', []))
            print(f"  Line {line:6} (seq {seq}): {name:45} performs: {performs_count}")

    # Show sample checklist
    if checklist:
        print(f"\nFirst 10 checklist items:")
        for item in checklist[:10]:
            print(f"  {item}")

        print(f"\nLast 10 checklist items:")
        for item in checklist[-10:]:
            print(f"  {item}")

    # Comparison with CTags
    print(f"\n{'='*80}")
    print(f"COMPARISON WITH CTAGS (GROUND TRUTH)")
    print(f"{'='*80}")
    print(f"Expected paragraphs (from CTags): 2,598")
    print(f"LLM extracted paragraphs: {len(paragraphs)}")
    coverage = (len(paragraphs) / 2598) * 100 if paragraphs else 0
    print(f"Coverage: {coverage:.1f}%")

    # Comparison with previous tests
    print(f"\n{'='*80}")
    print(f"IMPROVEMENT OVER PREVIOUS TESTS")
    print(f"{'='*80}")
    print(f"Test V1 (basic prompt): 4 elements (0.15% coverage)")
    print(f"Test V2 (enhanced prompt): 49 paragraphs (1.9% coverage)")
    print(f"Test V3 (accountability): {len(paragraphs)} paragraphs ({coverage:.1f}% coverage)")

    if coverage > 2:
        improvement = coverage / 1.9
        print(f"\n✓ Improvement: {improvement:.1f}x better than V2!")

    if coverage < 50:
        print(f"\n⚠ WARNING: Coverage still low ({coverage:.1f}%)")
        print(f"   Accountability approach helps but LLMs still struggle with exhaustive extraction.")
        print(f"   CTags remains the most reliable method for boundary detection.")
    elif coverage > 90:
        print(f"\n✓ EXCELLENT coverage ({coverage:.1f}%)!")
        print(f"   Accountability requirements worked!")
        print(f"   However, verify accuracy by comparing line numbers with CTags.")
    else:
        print(f"\n✓ MODERATE coverage ({coverage:.1f}%)")
        print(f"   Accountability improved results significantly.")
        print(f"   But still incomplete - chunking approach may be needed for 100% coverage.")

    print(f"\n{'='*80}")
    print(f"TEST COMPLETE")
    print(f"{'='*80}")
    print(f"\nOutput file: {OUTPUT_JSON}")
    print(f"\nKey Enhancements in V3:")
    print(f"  ✓ Added MANDATORY ACCOUNTABILITY REQUIREMENTS section")
    print(f"  ✓ Required completion checklist (like YAML template)")
    print(f"  ✓ Explicit line-by-line processing instructions")
    print(f"  ✓ Warning that skipped content will be obvious")
    print(f"  ✓ Block-by-block accountability tracking")
    print(f"  ✓ Expected count comparison (2,598 paragraphs)")
    print(f"\nThis mirrors the accountability approach in cobol-doc-template.yaml")

except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
