#!/usr/bin/env python3
"""
Markdown Documentation Coverage Verification

This script verifies that the generated markdown documentation captures
all code blocks from the source COBOL file by:
1. Extracting documented line ranges from markdown
2. Using set-based analysis to find gaps
3. Reporting coverage statistics
4. Identifying missing paragraphs
"""

import re
import json
import sys
from pathlib import Path

# Configuration
MARKDOWN_FILE = "/home/santosh/cobol-work/docs/TDAS-MINDISTCALC-documentation.md"
SOURCE_FILE = "/home/santosh/cobol-work/TDAS-MINDISTCALC.c74"
CTAGS_FILE = "/home/santosh/cobol-work/metadata/ctags/ctags-TDAS-MINDISTCALC-outline.json"

print("="*80)
print("MARKDOWN DOCUMENTATION COVERAGE VERIFICATION")
print("="*80)

# Step 1: Load source file
print(f"\n[1] Loading source file: {SOURCE_FILE}")
with open(SOURCE_FILE, 'r') as f:
    source_lines = f.readlines()

total_source_lines = len(source_lines)
print(f"  ✓ Total source lines: {total_source_lines:,}")

# Step 2: Load CTags for paragraph info
print(f"\n[2] Loading CTags metadata: {CTAGS_FILE}")
with open(CTAGS_FILE, 'r') as f:
    ctags_data = json.load(f)

all_paragraphs = [s for s in ctags_data['outline']['other'] if s['kind'] == 'paragraph']
print(f"  ✓ Total paragraphs in source: {len(all_paragraphs):,}")

# Create paragraph lookup by line
paragraph_by_line = {}
for para in all_paragraphs:
    paragraph_by_line[para['line']] = para['name']

# Step 3: Read markdown file
print(f"\n[3] Reading markdown file: {MARKDOWN_FILE}")
try:
    with open(MARKDOWN_FILE, 'r') as f:
        markdown_content = f.read()

    print(f"  ✓ Markdown file size: {len(markdown_content):,} characters")
except FileNotFoundError:
    print(f"  ✗ Error: Markdown file not found!")
    print(f"    Expected: {MARKDOWN_FILE}")
    sys.exit(1)

# Step 4: Extract documented line ranges from markdown
print(f"\n[4] Extracting documented line ranges from markdown...")

documented_lines = set()
documented_blocks = []

# Pattern 1: Look for COBOL sequence numbers (columns 1-6)
# Example: "000010$ RESET LIST" or "025680 Z-INITIALIZATION-PARAGRAPH"
sequence_pattern = re.compile(r'^(\d{6})\s', re.MULTILINE)
sequences_found = sequence_pattern.findall(markdown_content)

print(f"  → Found {len(sequences_found):,} COBOL sequence numbers in markdown")

# Convert sequence numbers to line numbers
# Sequence numbers start at 000010 and increment by 2
# Line 1 = 000010, Line 2 = 000012, etc.
for seq_str in sequences_found:
    seq_num = int(seq_str)
    # Calculate line number: (seq_num - 10) / 2 + 1
    if seq_num >= 10:
        line_num = (seq_num - 10) // 2 + 1
        if 1 <= line_num <= total_source_lines:
            documented_lines.add(line_num)

# Pattern 2: Look for explicit line number references
# Example: "Block 192: PARAGRAPH-NAME (Line 12836)"
# Example: "Lines 1-590"
# Example: "(Line 12836-12850)"
line_ref_patterns = [
    r'Line\s+(\d+)',
    r'Lines?\s+(\d+)\s*[-–]\s*(\d+)',
    r'\(Line\s+(\d+)\)',
    r'lines?\s+(\d+)\s*[-–]\s*(\d+)',
]

for pattern in line_ref_patterns:
    matches = re.finditer(pattern, markdown_content, re.IGNORECASE)
    for match in matches:
        if len(match.groups()) == 1:
            # Single line reference
            line_num = int(match.group(1))
            if 1 <= line_num <= total_source_lines:
                documented_lines.add(line_num)
        elif len(match.groups()) >= 2:
            # Line range
            start = int(match.group(1))
            end = int(match.group(2))
            if 1 <= start <= total_source_lines and 1 <= end <= total_source_lines:
                for line_num in range(start, end + 1):
                    documented_lines.add(line_num)

print(f"  → Extracted {len(documented_lines):,} unique documented lines")

# Pattern 3: Look for documented paragraph names and match with CTags
documented_paragraphs = set()
paragraph_pattern = re.compile(r'(?:^|\n)(?:###?\s+|Block\s+\d+:\s*)?([A-Z0-9][-A-Z0-9]*)\s*(?:\(Line\s+\d+\))?', re.MULTILINE)
paragraph_matches = paragraph_pattern.findall(markdown_content)

for para_name in paragraph_matches:
    # Check if this matches a real paragraph name from CTags
    for para in all_paragraphs:
        if para['name'] == para_name:
            documented_paragraphs.add(para_name)
            # Add all lines from this paragraph (estimate ~10 lines per paragraph)
            # We'll be conservative and just note it was mentioned
            break

print(f"  → Found {len(documented_paragraphs):,} documented paragraph names")

# Step 5: Analyze coverage using sets
print(f"\n{'='*80}")
print(f"COVERAGE ANALYSIS")
print(f"{'='*80}")

all_source_lines = set(range(1, total_source_lines + 1))
coverage_percentage = (len(documented_lines) / total_source_lines * 100) if documented_lines else 0

print(f"\nLine Coverage:")
print(f"  Total source lines: {total_source_lines:,}")
print(f"  Documented lines: {len(documented_lines):,}")
print(f"  Coverage: {coverage_percentage:.2f}%")

# Find gaps (missing lines)
missing_lines = all_source_lines - documented_lines

if missing_lines:
    print(f"\n  ⚠ Missing lines: {len(missing_lines):,} ({(len(missing_lines)/total_source_lines*100):.2f}%)")

    # Find contiguous gap ranges
    missing_sorted = sorted(missing_lines)
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

    print(f"\n  Gap ranges: {len(gaps)}")
    print(f"\n  Largest gaps (by size):")

    # Sort gaps by size
    gaps_sorted = sorted(gaps, key=lambda x: x[1] - x[0] + 1, reverse=True)

    for i, (gap_start, gap_end) in enumerate(gaps_sorted[:10], 1):
        gap_size = gap_end - gap_start + 1

        # Find which paragraphs are in this gap
        paragraphs_in_gap = []
        for para in all_paragraphs:
            if gap_start <= para['line'] <= gap_end:
                paragraphs_in_gap.append(para['name'])

        # Get sequence numbers for this range
        seq_start = 10 + (gap_start - 1) * 2
        seq_end = 10 + (gap_end - 1) * 2

        print(f"\n  Gap {i}: Lines {gap_start:,}-{gap_end:,} ({gap_size:,} lines)")
        print(f"          Sequences {seq_start:06d}-{seq_end:06d}")

        if paragraphs_in_gap:
            print(f"          Paragraphs: {', '.join(paragraphs_in_gap[:5])}")
            if len(paragraphs_in_gap) > 5:
                print(f"                      ... and {len(paragraphs_in_gap) - 5} more")
        else:
            print(f"          (No paragraph starts in this range)")

else:
    print(f"\n  ✓ NO GAPS: All source lines are documented!")

# Paragraph coverage
documented_para_count = len(documented_paragraphs)
para_coverage = (documented_para_count / len(all_paragraphs) * 100) if all_paragraphs else 0

print(f"\nParagraph Coverage:")
print(f"  Total paragraphs: {len(all_paragraphs):,}")
print(f"  Documented paragraphs: {documented_para_count:,}")
print(f"  Coverage: {para_coverage:.2f}%")

if documented_para_count < len(all_paragraphs):
    missing_paragraphs = []
    for para in all_paragraphs:
        if para['name'] not in documented_paragraphs:
            missing_paragraphs.append((para['name'], para['line']))

    print(f"\n  ⚠ Missing paragraphs: {len(missing_paragraphs):,}")
    print(f"\n  First 20 missing paragraphs:")
    for name, line in missing_paragraphs[:20]:
        seq = 10 + (line - 1) * 2
        print(f"    - {name:40} (Line {line:6,}, Seq {seq:06d})")

    if len(missing_paragraphs) > 20:
        print(f"    ... and {len(missing_paragraphs) - 20} more")

# Check for chunk completion checklists
print(f"\n{'='*80}")
print(f"ACCOUNTABILITY VERIFICATION")
print(f"{'='*80}")

checklist_pattern = re.compile(r'##\s+Chunk\s+Completion\s+Checklist', re.IGNORECASE)
checklists_found = checklist_pattern.findall(markdown_content)

print(f"\nCompletion Checklists Found: {len(checklists_found)}")

if len(checklists_found) > 0:
    print(f"  ✓ Accountability checklists are present")
else:
    print(f"  ⚠ No completion checklists found")
    print(f"    (Checklists help verify all content was processed)")

# Look for accountability markers
accountability_markers = [
    r'Block\s+\d+:',
    r'✓.*\(Line\s+\d+',
    r'Lines?\s+\d+\s*[-–]\s*\d+',
]

total_accountability_markers = 0
for pattern in accountability_markers:
    matches = re.findall(pattern, markdown_content, re.IGNORECASE)
    total_accountability_markers += len(matches)

print(f"\nAccountability Markers Found: {total_accountability_markers:,}")
if total_accountability_markers > 100:
    print(f"  ✓ Good use of line number references")
else:
    print(f"  ⚠ Few line number references found")

# Final verdict
print(f"\n{'='*80}")
print(f"FINAL VERDICT")
print(f"{'='*80}")

if coverage_percentage >= 95:
    print(f"\n✅ EXCELLENT COVERAGE ({coverage_percentage:.2f}%)")
    print(f"   The documentation captures nearly all source code!")
elif coverage_percentage >= 80:
    print(f"\n✓ GOOD COVERAGE ({coverage_percentage:.2f}%)")
    print(f"   Most source code is documented, some gaps remain")
elif coverage_percentage >= 50:
    print(f"\n⚠ MODERATE COVERAGE ({coverage_percentage:.2f}%)")
    print(f"   Significant portions of code are documented but many gaps exist")
else:
    print(f"\n❌ LOW COVERAGE ({coverage_percentage:.2f}%)")
    print(f"   Most source code is NOT documented")

print(f"\nSummary:")
print(f"  • Line coverage: {len(documented_lines):,}/{total_source_lines:,} ({coverage_percentage:.2f}%)")
print(f"  • Paragraph coverage: {documented_para_count:,}/{len(all_paragraphs):,} ({para_coverage:.2f}%)")
print(f"  • Missing lines: {len(missing_lines):,}")
print(f"  • Gap ranges: {len(gaps) if missing_lines else 0}")
print(f"  • Accountability checklists: {len(checklists_found)}")

print(f"\n{'='*80}")
print(f"VERIFICATION COMPLETE")
print(f"{'='*80}")

# Exit code based on coverage
if coverage_percentage >= 95:
    sys.exit(0)  # Success
else:
    sys.exit(1)  # Incomplete coverage
