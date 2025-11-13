#!/usr/bin/env python3
"""
Chunking Verification via Reconstruction & Diff

This is the SIMPLEST and MOST ACCURATE verification method:
1. Create chunks from source file
2. Concatenate all chunk contents in order to reconstruct the file
3. Compare reconstructed with original using diff
4. If identical → Perfect chunking
5. If different → Diff shows exact problems

Credit: Suggested by colleague for superior accuracy
"""

import json
import sys
import difflib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from source_chunker import chunk_large_cobol_file

# Configuration
COBOL_FILE = "/home/santosh/cobol-work/TDAS-MINDISTCALC.c74"
CTAGS_OUTLINE = "/home/santosh/cobol-work/metadata/ctags/ctags-TDAS-MINDISTCALC-outline.json"

print("="*80)
print("CHUNKING VERIFICATION VIA RECONSTRUCTION & DIFF")
print("="*80)
print("\nMethod: Reconstruct file from chunks, then compare with original")
print("Advantage: Simple, accurate, shows exact differences\n")

# Step 1: Load original source file
print("[1] Loading original source file...")
with open(COBOL_FILE, 'r') as f:
    original_content = f.read()

original_lines = original_content.splitlines(keepends=True)
original_line_count = len(original_lines)

print(f"  ✓ Original file: {original_line_count:,} lines")
print(f"  ✓ Original size: {len(original_content):,} characters")

# Step 2: Load CTags for chunking
print("\n[2] Loading CTags metadata...")
with open(CTAGS_OUTLINE, 'r') as f:
    ctags_data = json.load(f)

print(f"  ✓ CTags loaded")

# Step 3: Create chunks
print("\n[3] Creating chunks with 10K token limit...")
chunks, verification = chunk_large_cobol_file(
    COBOL_FILE,
    max_tokens_per_chunk=10000,
    ctags_metadata=ctags_data
)

print(f"  ✓ Created {len(chunks)} chunks")
print(f"  ✓ Built-in verification: {verification['coverage']}")

# Step 4: Reconstruct file from chunks
print("\n[4] Reconstructing file from chunks...")

reconstructed_content = ''.join(chunk['content'] for chunk in chunks)
reconstructed_lines = reconstructed_content.splitlines(keepends=True)
reconstructed_line_count = len(reconstructed_lines)

print(f"  ✓ Reconstructed: {reconstructed_line_count:,} lines")
print(f"  ✓ Reconstructed size: {len(reconstructed_content):,} characters")

# Step 5: Compare original vs reconstructed
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

# Step 6: Byte-for-byte comparison
print("\n" + "-"*80)
print("BYTE-FOR-BYTE COMPARISON")
print("-"*80)

if original_content == reconstructed_content:
    print("\n✅ PERFECT MATCH!")
    print("   Original and reconstructed are IDENTICAL")
    print("   Chunking is 100% accurate with:")
    print("   ✓ Complete coverage (no missing content)")
    print("   ✓ No overlaps (no duplicate content)")
    print("   ✓ Correct order (chunks in sequence)")
    print("   ✓ Content integrity (exact text preserved)")
    perfect_match = True
else:
    print("\n❌ MISMATCH DETECTED")
    print("   Original and reconstructed are DIFFERENT")
    perfect_match = False

# Step 7: If mismatch, show detailed diff
if not perfect_match:
    print("\n" + "-"*80)
    print("DETAILED DIFF ANALYSIS")
    print("-"*80)

    # Line-by-line comparison
    print("\nComparing line by line...")

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

    print(f"  Mismatched lines: {len(mismatches):,}")

    if mismatches:
        print(f"\n  First 10 mismatches:")
        for mismatch in mismatches[:10]:
            line_num = mismatch['line_num']
            orig = mismatch['original']
            recon = mismatch['reconstructed']

            print(f"\n  Line {line_num:,}:")

            if orig is None:
                print(f"    ORIGINAL: (missing)")
                print(f"    RECONSTRUCTED: {repr(recon[:60])}")
            elif recon is None:
                print(f"    ORIGINAL: {repr(orig[:60])}")
                print(f"    RECONSTRUCTED: (missing)")
            else:
                print(f"    ORIGINAL:      {repr(orig[:60])}")
                print(f"    RECONSTRUCTED: {repr(recon[:60])}")

        if len(mismatches) > 10:
            print(f"\n  ... and {len(mismatches) - 10:,} more mismatches")

    # Generate unified diff (like git diff)
    print("\n" + "-"*80)
    print("UNIFIED DIFF (first 50 lines)")
    print("-"*80)

    diff = difflib.unified_diff(
        original_lines,
        reconstructed_lines,
        fromfile='original.c74',
        tofile='reconstructed.c74',
        lineterm=''
    )

    diff_lines = list(diff)

    if diff_lines:
        print("\n" + '\n'.join(diff_lines[:50]))

        if len(diff_lines) > 50:
            print(f"\n... ({len(diff_lines) - 50} more diff lines)")
    else:
        print("\n(No differences)")

    # Analyze gaps by finding missing chunks of lines
    print("\n" + "-"*80)
    print("GAP ANALYSIS")
    print("-"*80)

    print("\nSearching for missing/extra sections...")

    # Find first and last mismatch
    if mismatches:
        first_mismatch = mismatches[0]['line_num']
        last_mismatch = mismatches[-1]['line_num']

        print(f"  First difference at line: {first_mismatch:,}")
        print(f"  Last difference at line: {last_mismatch:,}")
        print(f"  Affected range: {last_mismatch - first_mismatch + 1:,} lines")

# Step 8: Verify chunk boundaries
print("\n" + "-"*80)
print("CHUNK BOUNDARY VERIFICATION")
print("-"*80)

print("\nVerifying each chunk's boundaries match source...")

boundary_errors = []

for i, chunk in enumerate(chunks, 1):
    start_line = chunk['start_line']
    end_line = chunk['end_line']

    # Get expected lines from original
    expected_lines = original_lines[start_line - 1:end_line]
    expected_content = ''.join(expected_lines)

    # Get actual chunk content
    actual_content = chunk['content']

    if expected_content == actual_content:
        status = "✓"
    else:
        status = "✗"
        boundary_errors.append({
            'chunk': i,
            'start': start_line,
            'end': end_line,
            'expected_size': len(expected_content),
            'actual_size': len(actual_content)
        })

    if i <= 5 or status == "✗":  # Show first 5 or any errors
        print(f"  Chunk {i:2}: Lines {start_line:6,}-{end_line:6,} {status}")

if boundary_errors:
    print(f"\n  ⚠ Boundary errors in {len(boundary_errors)} chunks:")
    for err in boundary_errors[:5]:
        print(f"    Chunk {err['chunk']}: Expected {err['expected_size']} chars, got {err['actual_size']} chars")
else:
    print(f"\n  ✓ All {len(chunks)} chunks have correct boundaries")

# Final Summary
print("\n" + "="*80)
print("FINAL VERDICT")
print("="*80)

if perfect_match:
    print("\n🎉 ✅ CHUNKING IS PERFECT!")
    print("\n   The reconstructed file is IDENTICAL to the original.")
    print("   This proves:")
    print("   ✓ 100% coverage - no missing content")
    print("   ✓ No overlaps - no duplicate content")
    print("   ✓ Correct order - chunks properly sequenced")
    print("   ✓ Content integrity - exact text preserved")
    print(f"\n   All {len(chunks)} chunks verified!")
    print(f"   Total {original_line_count:,} lines perfectly captured.")

    print("\n   CONCLUSION: Chunking logic is production-ready! ✓")
    exit_code = 0
else:
    print("\n❌ CHUNKING HAS ISSUES")
    print("\n   The reconstructed file differs from the original.")
    print("   Problems detected:")

    if original_line_count != reconstructed_line_count:
        diff = reconstructed_line_count - original_line_count
        if diff > 0:
            print(f"   ⚠ {diff:,} extra lines (possible overlap)")
        else:
            print(f"   ⚠ {abs(diff):,} missing lines (incomplete coverage)")

    if len(mismatches) > 0:
        print(f"   ⚠ {len(mismatches):,} lines differ in content")

    if boundary_errors:
        print(f"   ⚠ {len(boundary_errors)} chunks have boundary issues")

    print("\n   CONCLUSION: Fix chunking logic before production use!")
    exit_code = 1

print("\n" + "="*80)
print("VERIFICATION COMPLETE")
print("="*80)

print("\nWhy this method is superior:")
print("  • Simple: Just concatenate and compare")
print("  • Accurate: Verifies actual content, not just line numbers")
print("  • Complete: One test validates everything")
print("  • Clear: Diff shows exactly what's wrong")
print("  • Standard: Uses familiar diff format")

sys.exit(exit_code)
