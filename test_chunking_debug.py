#!/usr/bin/env python3
"""
Debug script to investigate chunking behavior.

This will trace through the entire chunking process to identify
where code is being lost.
"""

import json
import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from source_chunker import (
    chunk_large_cobol_file,
    find_paragraph_boundaries,
    format_chunk_for_llm
)

# Configuration
COBOL_FILE = "/home/santosh/cobol-work/TDAS-MINDISTCALC.c74"
CTAGS_OUTLINE = "/home/santosh/cobol-work/metadata/ctags/ctags-TDAS-MINDISTCALC-outline.json"

print("="*80)
print("CHUNKING DEBUG INVESTIGATION")
print("="*80)

# Step 1: Load source file
print("\n[Step 1] Loading source file...")
with open(COBOL_FILE, 'r') as f:
    source_lines = f.readlines()

total_lines = len(source_lines)
print(f"✓ Source file: {total_lines:,} lines")

# Step 2: Load CTags metadata
print("\n[Step 2] Loading CTags metadata...")
with open(CTAGS_OUTLINE, 'r') as f:
    ctags_data = json.load(f)

# Extract paragraphs from CTags
paragraphs = [s for s in ctags_data['outline']['other'] if s['kind'] == 'paragraph']
print(f"✓ CTags paragraphs: {len(paragraphs):,}")
print(f"  First paragraph: {paragraphs[0]['name']} at line {paragraphs[0]['line']}")
print(f"  Last paragraph: {paragraphs[-1]['name']} at line {paragraphs[-1]['line']}")

# Step 3: Find boundaries using our function
print("\n[Step 3] Finding paragraph boundaries...")
boundaries = find_paragraph_boundaries(source_lines, ctags_data)
print(f"✓ Total boundaries found: {len(boundaries):,}")
print(f"  First boundary: line {boundaries[0]}")
print(f"  Last boundary: line {boundaries[-1]}")

# Check if boundaries cover full file
if boundaries[0] == 0 and boundaries[-1] < total_lines:
    print(f"✓ Boundaries span from line 0 to line {boundaries[-1]}")
else:
    print(f"⚠ Boundary coverage issue!")

# Step 4: Create chunks
print("\n[Step 4] Creating chunks with 10K token limit (NEW SETTING)...")
try:
    chunks, verification = chunk_large_cobol_file(
        COBOL_FILE,
        max_tokens_per_chunk=10000,  # Updated to match agent configuration
        ctags_metadata=ctags_data
    )

    print(f"✓ Chunks created: {len(chunks)}")
    print(f"✓ Verification: {verification}")

    # Analyze each chunk
    print("\n[Step 5] Analyzing chunk coverage...")
    print("-" * 80)

    total_chunk_lines = 0
    covered_lines = set()

    for i, chunk in enumerate(chunks, 1):
        start = chunk['start_line']
        end = chunk['end_line']
        lines = end - start + 1
        total_chunk_lines += lines

        # Track which lines are covered
        for line_num in range(start, end + 1):
            covered_lines.add(line_num)

        print(f"\nChunk {i}:")
        print(f"  Lines: {start:,} - {end:,} ({lines:,} lines)")
        print(f"  Tokens: ~{chunk['estimated_tokens']:,}")

        # Get first and last few lines of content to verify
        content_lines = chunk['content'].split('\n')
        first_line = content_lines[0][:60] if content_lines else "EMPTY"
        last_line = content_lines[-2][:60] if len(content_lines) > 1 else "EMPTY"

        print(f"  First: {first_line}...")
        print(f"  Last:  {last_line}...")

    print("\n" + "=" * 80)
    print("COVERAGE ANALYSIS")
    print("=" * 80)

    print(f"Total source lines: {total_lines:,}")
    print(f"Total chunk lines: {total_chunk_lines:,}")
    print(f"Unique lines covered: {len(covered_lines):,}")

    # Check for gaps
    all_lines = set(range(1, total_lines + 1))
    missing_lines = all_lines - covered_lines

    if missing_lines:
        missing_sorted = sorted(missing_lines)
        print(f"\n⚠ MISSING LINES: {len(missing_lines):,}")

        # Find gaps
        gaps = []
        gap_start = missing_sorted[0]
        gap_end = gap_start

        for line in missing_sorted[1:]:
            if line == gap_end + 1:
                gap_end = line
            else:
                gaps.append((gap_start, gap_end))
                gap_start = line
                gap_end = line
        gaps.append((gap_start, gap_end))

        print(f"  Gaps found: {len(gaps)}")
        for gap_start, gap_end in gaps[:10]:  # Show first 10
            gap_size = gap_end - gap_start + 1
            print(f"    Lines {gap_start:,} - {gap_end:,} ({gap_size:,} lines)")

        if len(gaps) > 10:
            print(f"    ... and {len(gaps) - 10} more gaps")
    else:
        print(f"\n✓ PERFECT COVERAGE! All {total_lines:,} lines are covered.")

    # Check for overlaps
    if total_chunk_lines > len(covered_lines):
        overlap = total_chunk_lines - len(covered_lines)
        print(f"\n⚠ OVERLAP DETECTED: {overlap:,} lines appear in multiple chunks")

except Exception as e:
    print(f"\n✗ ERROR during chunking: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 80)
print("INVESTIGATION COMPLETE")
print("=" * 80)
