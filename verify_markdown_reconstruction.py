#!/usr/bin/env python3
"""
Markdown Documentation Verification via Reconstruction

Uses the SAME METHOD as chunk verification:
1. Extract all COBOL code lines from markdown (by sequence number pattern)
2. Sort by sequence number to reconstruct original order
3. Concatenate to reconstruct source file
4. Byte-for-byte comparison with original
5. If identical → 100% coverage proven
6. If different → Diff shows exact missing/corrupted lines

This is SUPERIOR to pattern-based coverage checking because:
- Verifies actual content, not just mentions
- Catches corruption/truncation
- Simpler logic
- Definitive proof via byte comparison
"""

import re
import sys
import difflib
from pathlib import Path
from typing import Set, List, Tuple

# Configuration
MARKDOWN_FILE = "/home/santosh/cobol-work/docs/TDAS-MINDISTCALC-documentation.md"
SOURCE_FILE = "/home/santosh/cobol-work/TDAS-MINDISTCALC.c74"


def extract_cobol_lines_from_markdown(markdown_content: str) -> Set[int]:
    """
    Extract all COBOL sequence numbers from markdown content.

    Args:
        markdown_content: Markdown documentation string

    Returns:
        Set of sequence numbers found (e.g., {10, 12, 14, ...})
    """
    # Pattern: Lines starting with 6-digit sequence number
    # Example: "000010 IDENTIFICATION DIVISION."
    sequence_pattern = re.compile(r'^(\d{6})\s', re.MULTILINE)
    sequences_found = sequence_pattern.findall(markdown_content)

    return set(int(seq) for seq in sequences_found)


def find_missing_ranges(missing_lines: Set[int]) -> List[Tuple[int, int]]:
    """
    Convert set of missing lines into contiguous ranges.

    Args:
        missing_lines: Set of missing line numbers

    Returns:
        List of (start, end) tuples representing contiguous ranges
    """
    if not missing_lines:
        return []

    sorted_lines = sorted(missing_lines)
    ranges = []
    range_start = sorted_lines[0]
    range_end = range_start

    for line in sorted_lines[1:]:
        if line == range_end + 1:
            # Extend current range
            range_end = line
        else:
            # Save current range, start new one
            ranges.append((range_start, range_end))
            range_start = line
            range_end = line

    # Don't forget the last range
    ranges.append((range_start, range_end))

    return ranges

print("="*80)
print("MARKDOWN VERIFICATION VIA RECONSTRUCTION")
print("="*80)
print("\nMethod: Extract COBOL code from markdown → Reconstruct → Compare with original")
print("Advantage: Same proven approach as chunk verification\n")

# Step 1: Load original source file
print("[1] Loading original source file...")
try:
    with open(SOURCE_FILE, 'r') as f:
        original_content = f.read()

    original_lines = original_content.splitlines(keepends=True)
    original_line_count = len(original_lines)

    print(f"  ✓ Original file: {original_line_count:,} lines")
    print(f"  ✓ Original size: {len(original_content):,} characters")
except FileNotFoundError:
    print(f"  ✗ Error: Source file not found!")
    print(f"    Expected: {SOURCE_FILE}")
    sys.exit(1)

# Step 2: Load markdown documentation
print("\n[2] Loading markdown documentation...")
try:
    with open(MARKDOWN_FILE, 'r') as f:
        markdown_content = f.read()

    print(f"  ✓ Markdown file: {len(markdown_content):,} characters")
except FileNotFoundError:
    print(f"  ✗ Error: Markdown file not found!")
    print(f"    Expected: {MARKDOWN_FILE}")
    print(f"\n    Please generate documentation first using:")
    print(f"    python cobol_doc_agent.py")
    sys.exit(1)

# Step 3: Extract COBOL code lines from markdown
print("\n[3] Extracting COBOL code lines from markdown...")

# Pattern: Lines starting with 6-digit sequence number
# Example: "000010 IDENTIFICATION DIVISION."
# Example: "025680      MOVE WS-VARIABLE TO WS-OUTPUT"
sequence_pattern = re.compile(r'^(\d{6}\s.*)$', re.MULTILINE)
extracted_lines = sequence_pattern.findall(markdown_content)

print(f"  ✓ Extracted: {len(extracted_lines):,} COBOL code lines")

if len(extracted_lines) == 0:
    print(f"\n  ✗ ERROR: No COBOL code lines found in markdown!")
    print(f"    Pattern: Lines starting with 6-digit sequence number")
    print(f"    This suggests the markdown doesn't contain source code.")
    sys.exit(1)

# Step 4: Sort by sequence number (in case markdown presented out of order)
print("\n[4] Sorting lines by sequence number...")

# Convert to (sequence_number, line_text) tuples
line_tuples = []
for line in extracted_lines:
    seq_num = int(line[:6])
    line_tuples.append((seq_num, line))

# Sort by sequence number
line_tuples.sort(key=lambda x: x[0])

# Check for duplicates
sequences = [seq for seq, _ in line_tuples]
unique_sequences = set(sequences)

if len(sequences) != len(unique_sequences):
    duplicates = len(sequences) - len(unique_sequences)
    print(f"  ⚠ Warning: Found {duplicates} duplicate sequence numbers")
    print(f"    (LLM may have included same lines multiple times)")
else:
    print(f"  ✓ No duplicates: All {len(sequences):,} lines unique")

# Get sequence range
min_seq = line_tuples[0][0] if line_tuples else 0
max_seq = line_tuples[-1][0] if line_tuples else 0

print(f"  ✓ Sequence range: {min_seq:06d} - {max_seq:06d}")

# Step 5: Reconstruct source file from extracted lines
print("\n[5] Reconstructing source file from markdown...")

# Remove duplicates while preserving order
seen_sequences = set()
unique_lines = []
for seq, line in line_tuples:
    if seq not in seen_sequences:
        seen_sequences.add(seq)
        unique_lines.append(line)

# Join with newlines (add trailing newline to match original format)
reconstructed_content = '\n'.join(unique_lines)
if reconstructed_content and not reconstructed_content.endswith('\n'):
    reconstructed_content += '\n'

reconstructed_lines = reconstructed_content.splitlines(keepends=True)
reconstructed_line_count = len(reconstructed_lines)

print(f"  ✓ Reconstructed: {reconstructed_line_count:,} lines")
print(f"  ✓ Reconstructed size: {len(reconstructed_content):,} characters")

# Step 6: Compare original vs reconstructed
print("\n" + "="*80)
print("COMPARISON: ORIGINAL vs RECONSTRUCTED")
print("="*80)

print("\nBasic Statistics:")
print(f"  Original lines:      {original_line_count:,}")
print(f"  Reconstructed lines: {reconstructed_line_count:,}")
print(f"  Difference:          {abs(original_line_count - reconstructed_line_count):,}")

print(f"\n  Original size:       {len(original_content):,} chars")
print(f"  Reconstructed size:  {len(reconstructed_content):,} chars")
print(f"  Difference:          {abs(len(original_content) - len(reconstructed_content)):,} chars")

# Coverage percentage
coverage_percentage = (reconstructed_line_count / original_line_count * 100) if original_line_count > 0 else 0
print(f"\n  Line coverage: {coverage_percentage:.2f}%")

# Step 7: Byte-for-byte comparison
print("\n" + "-"*80)
print("BYTE-FOR-BYTE COMPARISON")
print("-"*80)

if original_content == reconstructed_content:
    print("\n✅ PERFECT MATCH!")
    print("   Original and reconstructed are IDENTICAL")
    print("   This proves:")
    print("   ✓ 100% coverage - all code documented")
    print("   ✓ No corruption - exact text preserved")
    print("   ✓ Complete accuracy - byte-for-byte identical")
    perfect_match = True
else:
    print("\n❌ MISMATCH DETECTED")
    print("   Original and reconstructed are DIFFERENT")
    print("   Coverage is incomplete or content was modified")
    perfect_match = False

# Step 8: If mismatch, show detailed analysis
if not perfect_match:
    print("\n" + "-"*80)
    print("DETAILED GAP ANALYSIS")
    print("-"*80)

    # Create sets of sequence numbers
    original_sequences = set()
    for line in original_lines:
        if len(line) >= 6 and line[:6].isdigit():
            original_sequences.add(int(line[:6]))

    reconstructed_sequences = set(seq for seq, _ in line_tuples)

    # Find missing sequences
    missing_sequences = original_sequences - reconstructed_sequences
    extra_sequences = reconstructed_sequences - original_sequences

    print(f"\nSequence Number Analysis:")
    print(f"  Original sequences: {len(original_sequences):,}")
    print(f"  Reconstructed sequences: {len(reconstructed_sequences):,}")
    print(f"  Missing sequences: {len(missing_sequences):,}")
    print(f"  Extra sequences: {len(extra_sequences):,}")

    if missing_sequences:
        print(f"\n  Missing Lines (not in markdown):")

        # Convert to line numbers
        missing_line_nums = []
        for seq in sorted(missing_sequences):
            line_num = (seq - 10) // 2 + 1
            missing_line_nums.append(line_num)

        # Find contiguous ranges
        ranges = []
        if missing_line_nums:
            start = missing_line_nums[0]
            end = start

            for line_num in missing_line_nums[1:]:
                if line_num == end + 1:
                    end = line_num
                else:
                    ranges.append((start, end))
                    start = line_num
                    end = line_num
            ranges.append((start, end))

        print(f"\n  Gap Ranges: {len(ranges)}")
        print(f"\n  Top 10 largest gaps:")

        # Sort by size
        ranges_sorted = sorted(ranges, key=lambda x: x[1] - x[0] + 1, reverse=True)

        for i, (gap_start, gap_end) in enumerate(ranges_sorted[:10], 1):
            gap_size = gap_end - gap_start + 1
            seq_start = 10 + (gap_start - 1) * 2
            seq_end = 10 + (gap_end - 1) * 2

            print(f"\n  Gap {i}: Lines {gap_start:,}-{gap_end:,} ({gap_size:,} lines)")
            print(f"          Sequences {seq_start:06d}-{seq_end:06d}")

            # Show first line of gap
            if 0 <= gap_start - 1 < len(original_lines):
                first_line = original_lines[gap_start - 1][:70].rstrip()
                print(f"          Starts: {first_line}")

    if extra_sequences:
        print(f"\n  Extra Lines (in markdown but not in original):")
        print(f"    Count: {len(extra_sequences)}")
        print(f"    First 10: {sorted(extra_sequences)[:10]}")

    # Line-by-line diff (first 50 differences)
    print("\n" + "-"*80)
    print("LINE-BY-LINE DIFF (first 50 differences)")
    print("-"*80)

    mismatches = []
    max_lines = max(original_line_count, reconstructed_line_count)

    for i in range(max_lines):
        original_line = original_lines[i] if i < original_line_count else None
        reconstructed_line = reconstructed_lines[i] if i < reconstructed_line_count else None

        if original_line != reconstructed_line:
            mismatches.append({
                'line_num': i + 1,
                'original': original_line,
                'reconstructed': reconstructed_line
            })

    print(f"\nMismatched lines: {len(mismatches):,}")

    if mismatches:
        for j, mismatch in enumerate(mismatches[:50], 1):
            line_num = mismatch['line_num']
            orig = mismatch['original']
            recon = mismatch['reconstructed']

            print(f"\n  Difference {j} at line {line_num:,}:")

            if orig is None:
                print(f"    ORIGINAL: (missing)")
                print(f"    MARKDOWN: {repr(recon[:60])}")
            elif recon is None:
                print(f"    ORIGINAL: {repr(orig[:60])}")
                print(f"    MARKDOWN: (missing)")
            else:
                print(f"    ORIGINAL: {repr(orig[:60])}")
                print(f"    MARKDOWN: {repr(recon[:60])}")

        if len(mismatches) > 50:
            print(f"\n  ... and {len(mismatches) - 50:,} more differences")

# Final Summary
print("\n" + "="*80)
print("FINAL VERDICT")
print("="*80)

if perfect_match:
    print("\n🎉 ✅ 100% COVERAGE VERIFIED!")
    print("\n   The markdown contains ALL source code, byte-for-byte identical.")
    print("   This proves:")
    print("   ✓ Complete coverage - no missing lines")
    print("   ✓ Content integrity - exact text preserved")
    print("   ✓ No corruption - LLM didn't modify code")
    print(f"\n   All {original_line_count:,} lines perfectly captured!")
    print("\n   CONCLUSION: Documentation is COMPLETE! ✓")
    exit_code = 0
else:
    print("\n❌ INCOMPLETE COVERAGE")
    print("\n   The markdown does NOT contain all source code.")
    print(f"\n   Coverage: {coverage_percentage:.2f}%")
    print(f"   Missing: {original_line_count - reconstructed_line_count:,} lines")

    if coverage_percentage >= 95:
        print("\n   Status: EXCELLENT (≥95%) - minor gaps remain")
    elif coverage_percentage >= 90:
        print("\n   Status: VERY GOOD (≥90%) - some gaps exist")
    elif coverage_percentage >= 80:
        print("\n   Status: GOOD (≥80%) - significant gaps")
    elif coverage_percentage >= 50:
        print("\n   Status: MODERATE (≥50%) - major gaps")
    else:
        print("\n   Status: POOR (<50%) - most code missing")

    print("\n   Recommendation:")
    if coverage_percentage >= 90:
        print("   → Use two-pass approach to fill remaining gaps")
    elif coverage_percentage >= 70:
        print("   → Review missing sections, adjust chunking or prompts")
    else:
        print("   → Major issue - check agent configuration and LLM behavior")

    exit_code = 1

print("\n" + "="*80)
print("VERIFICATION COMPLETE")
print("="*80)

print("\nWhy this method is superior:")
print("  • Definitive: Byte-for-byte comparison proves completeness")
print("  • Accurate: Verifies actual content, not just mentions")
print("  • Simple: Same proven logic as chunk verification")
print("  • Complete: One test validates everything")
print("  • Clear: Shows exact gaps if incomplete")

sys.exit(exit_code)
