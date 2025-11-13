#!/usr/bin/env python3
"""
Test to verify the new accountability enhancements.
Shows how the new chunk headers and template instructions will appear to the LLM.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from source_chunker import chunk_large_cobol_file, format_chunk_for_llm

COBOL_FILE = "/home/santosh/cobol-work/TDAS-MINDISTCALC.c74"
CTAGS_OUTLINE = "/home/santosh/cobol-work/metadata/ctags/ctags-TDAS-MINDISTCALC-outline.json"

print("="*80)
print("ACCOUNTABILITY ENHANCEMENTS VERIFICATION")
print("="*80)

# Load CTags
with open(CTAGS_OUTLINE, 'r') as f:
    ctags_data = json.load(f)

# Create chunks with new smaller size
print("\n[1] Creating chunks with 10K token limit...")
chunks, verification = chunk_large_cobol_file(
    COBOL_FILE,
    max_tokens_per_chunk=10000,
    ctags_metadata=ctags_data
)

print(f"\nCreated {len(chunks)} chunks")
print(f"Verification: {verification['coverage']}")

# Show the enhanced header for first few chunks
print(f"\n{'='*80}")
print(f"SAMPLE CHUNK HEADERS (What LLM Will See)")
print(f"{'='*80}")

program_map = "MOCK PROGRAM MAP FOR TESTING"

for i in range(min(3, len(chunks))):
    chunk = chunks[i]
    formatted = format_chunk_for_llm(
        chunk=chunk,
        total_chunks=len(chunks),
        file_name="TDAS-MINDISTCALC.c74",
        program_map=program_map
    )

    # Show just the header (first 2000 characters)
    header_preview = formatted[:2000]

    print(f"\n{'='*80}")
    print(f"CHUNK {i+1} HEADER PREVIEW:")
    print(f"{'='*80}")
    print(header_preview)
    print("...")
    print(f"\n[Note: Full chunk continues with {chunk['line_count']:,} lines of COBOL code]")

print(f"\n{'='*80}")
print(f"SUMMARY OF ENHANCEMENTS")
print(f"{'='*80}")
print("""
✓ CHUNKING CHANGES:
  - Reduced from 4 large chunks to 38 smaller chunks
  - Average chunk size: ~704 lines (vs ~6,689 lines before)
  - More granular processing reduces LLM's ability to skip content

✓ TEMPLATE CHANGES (cobol-doc-template.yaml):
  - Added BLOCK-BY-BLOCK ACCOUNTABILITY section with 6 new requirements
  - Mandatory format: "Block N: PARAGRAPH-NAME (Line X)"
  - Required completion checklist at end of each chunk
  - Explicit warning that missing line numbers expose skipped content

✓ CHUNK HEADER CHANGES (source_chunker.py):
  - Added MANDATORY ACCOUNTABILITY REQUIREMENTS section
  - Clear instructions to document lines X-Y sequentially
  - Warning emoji (⚠️) to draw attention
  - Requirement to provide completion checklist

✓ EXPECTED RESULTS:
  - LLM cannot ignore accountability requirements in EVERY chunk header
  - Completion checklist makes skipped content immediately obvious
  - Smaller chunks reduce cognitive load and skipping behavior
  - Line number format enables easy verification of coverage
  - 38 separate LLM calls (vs 4) = 38 opportunities to enforce rules

✓ NEXT STEPS:
  - Run the documentation agent with these changes
  - Review the completion checklists in the generated output
  - Verify line number continuity across documented blocks
  - Check for gaps in line coverage
""")

print(f"\n{'='*80}")
print(f"READY FOR TESTING")
print(f"{'='*80}")
print("""
These changes are now ready to test with the full documentation agent.

To test:
1. Run: python cobol_doc_agent.py <config>
2. Check generated documentation for completion checklists
3. Verify each chunk documents its full line range
4. Look for gaps in line number sequences

If LLM still skips content, the completion checklists will make it obvious!
""")
