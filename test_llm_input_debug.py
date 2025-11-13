#!/usr/bin/env python3
"""
Debug script to examine what's actually sent to the LLM for each chunk.

This will help identify if chunks are being truncated or if the LLM
is choosing to only document small portions.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from source_chunker import (
    chunk_large_cobol_file,
    format_chunk_for_llm
)

# Configuration
COBOL_FILE = "/home/santosh/cobol-work/TDAS-MINDISTCALC.c74"
CTAGS_OUTLINE = "/home/santosh/cobol-work/metadata/ctags/ctags-TDAS-MINDISTCALC-outline.json"

print("="*80)
print("LLM INPUT DEBUG - What Gets Sent to the LLM?")
print("="*80)

# Load CTags
with open(CTAGS_OUTLINE, 'r') as f:
    ctags_data = json.load(f)

# Create chunks with NEW 10K token limit (matches agent configuration)
chunks, verification = chunk_large_cobol_file(
    COBOL_FILE,
    max_tokens_per_chunk=10000,  # Updated to match agent configuration
    ctags_metadata=ctags_data
)

print(f"\nCreated {len(chunks)} chunks")
print(f"Verification: {verification['coverage']}")

# Generate a simple program map (mock)
program_map = """
PROGRAM MAP (Summary):
- IDENTIFICATION DIVISION (lines 3-8)
- ENVIRONMENT DIVISION (lines 202-520)
- DATA DIVISION (lines 522-12834)
- PROCEDURE DIVISION (lines 12835-26755)
  - Z-INITIALIZATION SECTION (line 12835)
  - Z-MAIN-CONTROL SECTION (line 12876)
  - Z-WRAP-UP SECTION (line 12897)
  - Z-SUPPORT SECTION (line 12967)
  - Z-USERS-ROUTINES SECTION (line 14080)
"""

# Analyze what gets sent to LLM for each chunk
print("\n" + "="*80)
print("ANALYZING LLM INPUT FOR EACH CHUNK")
print("="*80)

for i, chunk in enumerate(chunks, 1):
    formatted = format_chunk_for_llm(
        chunk=chunk,
        total_chunks=len(chunks),
        file_name="TDAS-MINDISTCALC.c74",
        program_map=program_map
    )

    # Count lines in the formatted output
    formatted_lines = formatted.split('\n')
    total_formatted_lines = len(formatted_lines)

    # Count COBOL code lines (between ```cobol and ```)
    cobol_content_lines = 0
    in_cobol_block = False

    for line in formatted_lines:
        if line.strip() == '```cobol':
            in_cobol_block = True
        elif line.strip() == '```' and in_cobol_block:
            in_cobol_block = False
        elif in_cobol_block:
            cobol_content_lines += 1

    # Estimate tokens
    formatted_chars = len(formatted)
    formatted_tokens = formatted_chars // 4

    print(f"\n{'='*80}")
    print(f"CHUNK {i} - LLM INPUT ANALYSIS")
    print(f"{'='*80}")
    print(f"Source lines in chunk: {chunk['line_count']:,}")
    print(f"")
    print(f"Formatted for LLM:")
    print(f"  Total formatted lines: {total_formatted_lines:,}")
    print(f"  COBOL code lines in formatted: {cobol_content_lines:,}")
    print(f"  Header/instruction lines: {total_formatted_lines - cobol_content_lines:,}")
    print(f"  Total characters: {formatted_chars:,}")
    print(f"  Estimated tokens: ~{formatted_tokens:,}")
    print(f"")
    print(f"Coverage check:")
    if cobol_content_lines == chunk['line_count']:
        print(f"  ✓ PERFECT: All {chunk['line_count']:,} source lines included")
    else:
        diff = chunk['line_count'] - cobol_content_lines
        print(f"  ⚠ MISMATCH: Expected {chunk['line_count']:,}, got {cobol_content_lines:,}")
        print(f"  ⚠ Missing {diff:,} lines!")

    # Show first and last few lines of the COBOL content
    cobol_lines = [line for line in formatted_lines if line and not line.startswith('=') and not line.startswith('CHUNK') and not line.startswith('Lines:')]

    print(f"\nFirst 5 lines of formatted content:")
    for line in cobol_lines[:5]:
        print(f"  {line[:80]}")

    print(f"\nLast 5 lines of formatted content:")
    for line in cobol_lines[-5:]:
        print(f"  {line[:80]}")

# Summary
print("\n" + "="*80)
print("SUMMARY")
print("="*80)

total_source_lines = sum(c['line_count'] for c in chunks)
print(f"Total source lines across all chunks: {total_source_lines:,}")
print(f"Expected: 26,755 lines")

if total_source_lines == 26755:
    print("✓ All source lines are being formatted for LLM")
else:
    print(f"⚠ Mismatch: {26755 - total_source_lines:,} lines missing!")

print("\nNext step: The LLM receives complete code but may be choosing to")
print("only document portions. This is a PROMPT/INSTRUCTION issue, not chunking!")
