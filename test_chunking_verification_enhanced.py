#!/usr/bin/env python3
"""
Enhanced Chunking Verification Test using Set-Based Analysis

This test uses a more precise approach:
1. Creates a set for each chunk containing its line numbers
2. Uses set.intersection() to detect overlaps between chunks
3. Uses set.union() to compute total coverage
4. Provides detailed diagnostics showing WHICH chunks have problems
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from source_chunker import chunk_large_cobol_file

# Configuration
COBOL_FILE = "/home/santosh/cobol-work/TDAS-MINDISTCALC.c74"
CTAGS_OUTLINE = "/home/santosh/cobol-work/metadata/ctags/ctags-TDAS-MINDISTCALC-outline.json"

print("="*80)
print("ENHANCED CHUNKING VERIFICATION - SET-BASED ANALYSIS")
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

paragraphs = [s for s in ctags_data['outline']['other'] if s['kind'] == 'paragraph']
print(f"✓ CTags paragraphs: {len(paragraphs):,}")

# Step 3: Create chunks
print("\n[Step 3] Creating chunks with 10K token limit...")
chunks, verification = chunk_large_cobol_file(
    COBOL_FILE,
    max_tokens_per_chunk=10000,
    ctags_metadata=ctags_data
)

print(f"✓ Chunks created: {len(chunks)}")
print(f"✓ Built-in verification: {verification}")

# Step 4: Enhanced set-based verification
print("\n" + "="*80)
print("[Step 4] SET-BASED VERIFICATION ANALYSIS")
print("="*80)

# Create a set for each chunk
chunk_sets = []
chunk_info = []

print("\nCreating sets for each chunk:")
for i, chunk in enumerate(chunks, 1):
    start = chunk['start_line']
    end = chunk['end_line']

    # Create set of line numbers for this chunk
    chunk_set = set(range(start, end + 1))
    chunk_sets.append(chunk_set)

    chunk_info.append({
        'chunk_number': i,
        'start': start,
        'end': end,
        'line_count': end - start + 1,
        'set_size': len(chunk_set),
        'set': chunk_set
    })

    print(f"  Chunk {i}: Lines {start:,}-{end:,} → Set size: {len(chunk_set):,}")

# Verify each chunk's set size matches its line count
print("\n" + "-"*80)
print("INTERNAL CONSISTENCY CHECK")
print("-"*80)

all_consistent = True
for info in chunk_info:
    if info['line_count'] != info['set_size']:
        print(f"⚠ Chunk {info['chunk_number']}: Line count mismatch!")
        print(f"    Expected: {info['line_count']:,}")
        print(f"    Set size: {info['set_size']:,}")
        all_consistent = False

if all_consistent:
    print("✓ All chunks internally consistent (line_count == set_size)")

# Check for overlaps using set.intersection()
print("\n" + "-"*80)
print("OVERLAP DETECTION (using set.intersection)")
print("-"*80)

overlaps_found = []

for i in range(len(chunk_info)):
    for j in range(i + 1, len(chunk_info)):
        chunk_i = chunk_info[i]
        chunk_j = chunk_info[j]

        # Find intersection between two chunks
        overlap = chunk_i['set'].intersection(chunk_j['set'])

        if overlap:
            overlaps_found.append({
                'chunk_a': chunk_i['chunk_number'],
                'chunk_b': chunk_j['chunk_number'],
                'overlapping_lines': sorted(overlap),
                'overlap_count': len(overlap)
            })

            print(f"\n⚠ OVERLAP DETECTED:")
            print(f"  Chunk {chunk_i['chunk_number']} (lines {chunk_i['start']:,}-{chunk_i['end']:,})")
            print(f"  Chunk {chunk_j['chunk_number']} (lines {chunk_j['start']:,}-{chunk_j['end']:,})")
            print(f"  Overlapping lines: {overlap}")
            print(f"  Overlap size: {len(overlap):,} lines")

if not overlaps_found:
    print("✓ NO OVERLAPS: All chunks are mutually exclusive")
else:
    print(f"\n⚠ Total overlaps found: {len(overlaps_found)}")

# Compute total coverage using set.union()
print("\n" + "-"*80)
print("COVERAGE ANALYSIS (using set.union)")
print("-"*80)

# Union of all chunk sets
if chunk_sets:
    covered_lines = set.union(*chunk_sets)
else:
    covered_lines = set()

print(f"Total unique lines covered: {len(covered_lines):,}")

# Expected lines
all_lines = set(range(1, total_lines + 1))
print(f"Expected lines: {len(all_lines):,}")

# Find gaps (missing lines)
missing_lines = all_lines - covered_lines

if missing_lines:
    missing_sorted = sorted(missing_lines)
    print(f"\n⚠ GAPS FOUND: {len(missing_lines):,} lines missing")

    # Find contiguous gap ranges
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

    print(f"  Gap ranges: {len(gaps)}")
    print(f"\n  First 10 gaps:")
    for gap_start, gap_end in gaps[:10]:
        gap_size = gap_end - gap_start + 1
        print(f"    Lines {gap_start:,}-{gap_end:,} ({gap_size:,} lines)")

    if len(gaps) > 10:
        print(f"    ... and {len(gaps) - 10} more gaps")
else:
    print(f"✓ NO GAPS: All {total_lines:,} lines are covered")

# Check for extra lines (beyond file end)
extra_lines = covered_lines - all_lines

if extra_lines:
    print(f"\n⚠ EXTRA LINES: {len(extra_lines):,} lines beyond file end")
    print(f"  Invalid line numbers: {sorted(extra_lines)[:20]}")
else:
    print("✓ NO EXTRA LINES: All covered lines are within file bounds")

# Compute statistics
print("\n" + "-"*80)
print("DETAILED STATISTICS")
print("-"*80)

total_declared_lines = sum(info['line_count'] for info in chunk_info)
unique_covered_lines = len(covered_lines)
duplicate_lines = total_declared_lines - unique_covered_lines

print(f"Total lines declared by chunks: {total_declared_lines:,}")
print(f"Unique lines covered: {unique_covered_lines:,}")
print(f"Duplicate lines (overlaps): {duplicate_lines:,}")
print(f"Coverage percentage: {(unique_covered_lines / total_lines * 100):.2f}%")

# Verify content integrity (sample first and last lines)
print("\n" + "-"*80)
print("CONTENT INTEGRITY VERIFICATION")
print("-"*80)

integrity_pass = True

for info in chunk_info[:5]:  # Check first 5 chunks
    chunk_num = info['chunk_number']
    chunk = chunks[chunk_num - 1]

    # Get content lines
    content_lines = chunk['content'].split('\n')

    # Remove empty trailing line if present
    if content_lines and content_lines[-1] == '':
        content_lines = content_lines[:-1]

    content_line_count = len(content_lines)
    expected_line_count = chunk['line_count']

    if content_line_count != expected_line_count:
        print(f"\n⚠ Chunk {chunk_num} content mismatch:")
        print(f"    Declared line count: {expected_line_count:,}")
        print(f"    Actual content lines: {content_line_count:,}")
        integrity_pass = False
    else:
        # Verify first and last lines match source
        expected_first = source_lines[chunk['start_line'] - 1].rstrip()
        actual_first = content_lines[0].rstrip()

        expected_last = source_lines[chunk['end_line'] - 1].rstrip()
        actual_last = content_lines[-1].rstrip()

        if expected_first == actual_first and expected_last == actual_last:
            print(f"✓ Chunk {chunk_num}: Content integrity verified")
        else:
            print(f"⚠ Chunk {chunk_num}: Content mismatch")
            print(f"    First line expected: {expected_first[:50]}")
            print(f"    First line actual:   {actual_first[:50]}")
            integrity_pass = False

if integrity_pass:
    print("\n✓ Content integrity verified for sampled chunks")

# Final verdict
print("\n" + "="*80)
print("FINAL VERDICT")
print("="*80)

all_tests_pass = (
    all_consistent and
    not overlaps_found and
    not missing_lines and
    not extra_lines and
    integrity_pass and
    unique_covered_lines == total_lines
)

if all_tests_pass:
    print("\n✅ ALL TESTS PASSED!")
    print("\n✓ Internal consistency: PASS")
    print("✓ No overlaps: PASS")
    print("✓ No gaps: PASS")
    print("✓ No extra lines: PASS")
    print("✓ Content integrity: PASS")
    print(f"✓ Perfect coverage: {total_lines:,}/{total_lines:,} lines (100%)")
    print("\n🎉 Chunking is PERFECT! Ready for production use.")
else:
    print("\n❌ TESTS FAILED!")
    if not all_consistent:
        print("✗ Internal consistency: FAIL")
    if overlaps_found:
        print(f"✗ Overlaps detected: {len(overlaps_found)} overlap(s)")
    if missing_lines:
        print(f"✗ Gaps found: {len(missing_lines):,} missing lines")
    if extra_lines:
        print(f"✗ Extra lines: {len(extra_lines):,} invalid lines")
    if not integrity_pass:
        print("✗ Content integrity: FAIL")

    print("\n⚠ Chunking has issues that need to be fixed!")

print("\n" + "="*80)
print("VERIFICATION COMPLETE")
print("="*80)
