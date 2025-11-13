#!/usr/bin/env python3
"""
Test script to verify new chunk sizes with 10K token limit.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from source_chunker import chunk_large_cobol_file

COBOL_FILE = "/home/santosh/cobol-work/TDAS-MINDISTCALC.c74"
CTAGS_OUTLINE = "/home/santosh/cobol-work/metadata/ctags/ctags-TDAS-MINDISTCALC-outline.json"

print("="*80)
print("TESTING NEW CHUNK SIZES (10K tokens per chunk)")
print("="*80)

# Load CTags
with open(CTAGS_OUTLINE, 'r') as f:
    ctags_data = json.load(f)

# Test with 10K token limit (new setting)
print("\n[1] Creating chunks with 10K token limit...")
chunks, verification = chunk_large_cobol_file(
    COBOL_FILE,
    max_tokens_per_chunk=10000,  # New smaller limit
    ctags_metadata=ctags_data
)

print(f"\n{'='*80}")
print(f"RESULTS")
print(f"{'='*80}")
print(f"Total chunks created: {len(chunks)}")
print(f"Verification: {verification['coverage']}")

print(f"\n{'='*80}")
print(f"CHUNK DETAILS")
print(f"{'='*80}")

total_lines = 0
for chunk in chunks:
    total_lines += chunk['line_count']
    print(f"\nChunk {chunk['chunk_number']}:")
    print(f"  Lines: {chunk['start_line']:,} to {chunk['end_line']:,}")
    print(f"  Line count: {chunk['line_count']:,}")
    print(f"  Estimated tokens: ~{chunk['estimated_tokens']:,}")

print(f"\n{'='*80}")
print(f"SUMMARY")
print(f"{'='*80}")
print(f"Total chunks: {len(chunks)}")
print(f"Total lines covered: {total_lines:,}")
print(f"Average lines per chunk: {total_lines // len(chunks):,}")
print(f"\n✓ Expected: 10-20 chunks with ~2,000-3,000 lines each")
print(f"✓ Actual: {len(chunks)} chunks with ~{total_lines // len(chunks):,} lines per chunk")

if 10 <= len(chunks) <= 20 and 1500 <= (total_lines // len(chunks)) <= 3500:
    print(f"\n✓ SUCCESS: Chunk granularity is in target range!")
else:
    print(f"\n⚠ Note: Chunk sizes are outside target range but may still be effective")
