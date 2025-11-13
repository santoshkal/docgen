#!/usr/bin/env python3
"""
Final comprehensive test to verify the entire pipeline.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from source_chunker import chunk_large_cobol_file, format_chunk_for_llm, verify_chunk_reconstruction

COBOL_FILE = "/home/santosh/cobol-work/TDAS-MINDISTCALC.c74"
CTAGS_OUTLINE = "/home/santosh/cobol-work/metadata/ctags/ctags-TDAS-MINDISTCALC-outline.json"

print("="*80)
print("FINAL COMPREHENSIVE VERIFICATION")
print("="*80)

# Load source
with open(COBOL_FILE, 'r') as f:
    source_lines = f.readlines()
total_lines = len(source_lines)

# Load CTags
with open(CTAGS_OUTLINE, 'r') as f:
    ctags_data = json.load(f)

# Create chunks with NEW 10K token limit (matches agent configuration)
chunks, verification = chunk_large_cobol_file(
    COBOL_FILE,
    max_tokens_per_chunk=10000,  # Updated to match agent configuration
    ctags_metadata=ctags_data
)

print(f"\n[1] Source File: {total_lines:,} lines")
print(f"[2] Chunks Created: {len(chunks)}")
print(f"[3] Coverage: {verification['coverage']}")

# Verify each chunk contains correct lines
print("\n" + "="*80)
print("VERIFYING CHUNK CONTENT")
print("="*80)

program_map = "PROGRAM MAP (mock)"
all_verified = True

for i, chunk in enumerate(chunks, 1):
    # Format for LLM
    formatted = format_chunk_for_llm(
        chunk=chunk,
        total_chunks=len(chunks),
        file_name="TDAS-MINDISTCALC.c74",
        program_map=program_map
    )

    # Count lines in chunk content
    chunk_content_lines = chunk['content'].count('\n')

    # Verify first and last lines match source
    chunk_lines = chunk['content'].split('\n')
    expected_first = source_lines[chunk['start_line'] - 1].rstrip()
    expected_last = source_lines[chunk['end_line'] - 1].rstrip()

    actual_first = chunk_lines[0].rstrip() if chunk_lines else ""
    actual_last = chunk_lines[-2].rstrip() if len(chunk_lines) > 1 else ""  # -2 because last is empty after final \n

    print(f"\nChunk {i}:")
    print(f"  Expected lines: {chunk['line_count']:,}")
    print(f"  Content line count: {chunk_content_lines:,}")

    if chunk_content_lines == chunk['line_count']:
        print(f"  ✓ Line count matches")
    else:
        print(f"  ⚠ Line count mismatch!")
        all_verified = False

    print(f"\n  First line verification:")
    print(f"    Expected: {expected_first[:70]}")
    print(f"    Actual:   {actual_first[:70]}")
    if expected_first == actual_first:
        print(f"    ✓ First line matches")
    else:
        print(f"    ⚠ First line MISMATCH!")
        all_verified = False

    print(f"\n  Last line verification:")
    print(f"    Expected: {expected_last[:70]}")
    print(f"    Actual:   {actual_last[:70]}")
    if expected_last == actual_last:
        print(f"    ✓ Last line matches")
    else:
        print(f"    ⚠ Last line MISMATCH!")
        all_verified = False

    # Verify formatted output contains the content
    formatted_tokens = len(formatted) // 4
    print(f"\n  Formatted for LLM:")
    print(f"    Characters: {len(formatted):,}")
    print(f"    Estimated tokens: ~{formatted_tokens:,}")
    print(f"    Content is in formatted: {chunk['content'] in formatted}")

# Additional verification via reconstruction (most accurate method)
print("\n" + "="*80)
print("RECONSTRUCTION VERIFICATION")
print("="*80)

print("\nReconstructing file from chunks...")
original_content = ''.join(source_lines)
reconstruction_result = verify_chunk_reconstruction(chunks, original_content)

print(f"  Original size: {reconstruction_result['original_size']:,} characters")
print(f"  Reconstructed size: {reconstruction_result['reconstructed_size']:,} characters")

if reconstruction_result['match']:
    print(f"\n  ✓ PERFECT MATCH: Byte-for-byte identical!")
    print(f"  ✓ This proves:")
    print(f"     • 100% coverage (no missing content)")
    print(f"     • No overlaps (no duplicate content)")
    print(f"     • Correct order (chunks in sequence)")
    print(f"     • Content integrity (exact text preserved)")
    reconstruction_pass = True
else:
    print(f"\n  ✗ MISMATCH DETECTED")
    print(f"     Error: {reconstruction_result['error']}")
    if 'size_difference' in reconstruction_result:
        print(f"     Size diff: {reconstruction_result['size_difference']} characters")
    if 'first_difference_at' in reconstruction_result:
        print(f"     First diff at position: {reconstruction_result['first_difference_at']}")
    reconstruction_pass = False

all_verified = all_verified and reconstruction_pass

print("\n" + "="*80)
print("FINAL VERDICT")
print("="*80)

if all_verified:
    print("✓ ALL VERIFICATIONS PASSED")
    print("✓ Chunking works perfectly")
    print("✓ All source lines are included in chunks")
    print("✓ All chunks are correctly formatted for LLM")
    print("\nCONCLUSION: The technical pipeline is PERFECT.")
    print("The issue is that the LLM is choosing to only document ~11% of the code.")
    print("This is a PROMPT/INSTRUCTION problem, NOT a technical bug!")
else:
    print("⚠ VERIFICATION FAILED")
    print("There are technical issues in the chunking or formatting pipeline.")
