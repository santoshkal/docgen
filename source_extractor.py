"""
Source Code Extractor for COBOL Documentation Agent

This module provides functions to extract specific lines and sections from COBOL source files
using metadata (line numbers from ctags, superbol, gnucobol).

Implements Tier 1 of the four-tier extraction strategy: Metadata-based structured extraction.
"""

import hashlib
from typing import Optional, List, Tuple, Dict, Any


def extract_lines(file_path: str, start: int, end: int) -> str:
    """
    Extract a range of lines from a file.

    Args:
        file_path: Path to the source file
        start: Starting line number (1-indexed)
        end: Ending line number (1-indexed, inclusive)

    Returns:
        Extracted lines as a string with newlines preserved

    Raises:
        ValueError: If line numbers are invalid (negative, zero, or end < start)
        FileNotFoundError: If the file doesn't exist

    Examples:
        >>> extract_lines("program.cbl", 1, 10)
        'Line 1\\nLine 2\\n...Line 10\\n'
    """
    # Validate line numbers
    if start <= 0 or end <= 0:
        raise ValueError("Line numbers must be positive (1-indexed)")

    if end < start:
        raise ValueError("End line must be >= start line")

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # Convert 1-indexed to 0-indexed
        return ''.join(lines[start-1:end])


def extract_lines_by_ranges(file_path: str, ranges: List[Tuple[int, int]]) -> str:
    """
    Extract multiple line ranges from a file.

    Args:
        file_path: Path to the source file
        ranges: List of (start, end) tuples, each with 1-indexed line numbers (inclusive)

    Returns:
        Concatenated extracted lines as a string with newlines preserved

    Raises:
        ValueError: If any range has invalid line numbers
        FileNotFoundError: If the file doesn't exist

    Examples:
        >>> extract_lines_by_ranges("program.cbl", [(1, 5), (10, 15)])
        'Lines 1-5 concatenated with lines 10-15'
    """
    result = []
    for start, end in ranges:
        result.append(extract_lines(file_path, start, end))
    return ''.join(result)


def extract_lines_with_context(
    file_path: str,
    start: int,
    end: int,
    context_before: int = 0,
    context_after: int = 0
) -> str:
    """
    Extract lines from a file with surrounding context.

    Args:
        file_path: Path to the source file
        start: Starting line number (1-indexed)
        end: Ending line number (1-indexed, inclusive)
        context_before: Number of lines to include before start (default: 0)
        context_after: Number of lines to include after end (default: 0)

    Returns:
        Extracted lines with context as a string with newlines preserved

    Raises:
        ValueError: If line numbers are invalid
        FileNotFoundError: If the file doesn't exist

    Examples:
        >>> extract_lines_with_context("program.cbl", 10, 15, context_before=2, context_after=2)
        'Lines 8-17 (lines 10-15 with 2 lines of context before and after)'
    """
    # Calculate actual range with context
    actual_start = max(1, start - context_before)

    # For end calculation, we need to read the file to know total line count
    with open(file_path, 'r', encoding='utf-8') as f:
        total_lines = sum(1 for _ in f)

    actual_end = min(total_lines, end + context_after)

    return extract_lines(file_path, actual_start, actual_end)


def compute_source_hash(source_code: str) -> str:
    """
    Compute SHA256 hash of source code for deduplication.

    Args:
        source_code: Source code string to hash

    Returns:
        Lowercase hexadecimal SHA256 hash (64 characters)

    Examples:
        >>> compute_source_hash("MOVE A TO B.")
        'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    """
    return hashlib.sha256(source_code.encode('utf-8')).hexdigest()


def deduplicate_source_extracts(extracts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Remove duplicate source code extracts based on content hash.

    Keeps the first occurrence of each unique source code.

    Args:
        extracts: List of dictionaries with 'name' and 'source' keys

    Returns:
        Deduplicated list of extracts (first occurrence kept)

    Examples:
        >>> extracts = [
        ...     {'name': 'PARA-1', 'source': 'MOVE A TO B.'},
        ...     {'name': 'PARA-2', 'source': 'MOVE A TO B.'}  # Duplicate
        ... ]
        >>> result = deduplicate_source_extracts(extracts)
        >>> len(result)
        1
    """
    seen_hashes = set()
    deduplicated = []

    for extract in extracts:
        source_hash = compute_source_hash(extract['source'])
        if source_hash not in seen_hashes:
            seen_hashes.add(source_hash)
            deduplicated.append(extract)

    return deduplicated


def find_division_boundaries(file_path: str) -> Dict[str, Dict[str, int]]:
    """
    Find COBOL division boundaries by scanning file for DIVISION keywords.

    Args:
        file_path: Path to the COBOL source file

    Returns:
        Dictionary mapping division names to {'start': line_num, 'end': line_num}
        Line numbers are 1-indexed

    Examples:
        >>> boundaries = find_division_boundaries("program.cbl")
        >>> boundaries['DATA DIVISION']['start']
        42
    """
    divisions = {}
    division_names = []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find all division start lines
    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip().upper()
        if stripped.endswith(' DIVISION.'):
            # Extract division name (remove the trailing period)
            division_name = stripped.rstrip('.')
            divisions[division_name] = {'start': line_num}
            division_names.append(division_name)

    # Calculate end lines for each division
    for i, div_name in enumerate(division_names):
        if i < len(division_names) - 1:
            # End is the line before next division starts
            divisions[div_name]['end'] = divisions[division_names[i + 1]]['start'] - 1
        else:
            # Last division ends at EOF
            divisions[div_name]['end'] = len(lines)

    return divisions


def extract_division(file_path: str, division_name: str) -> Optional[str]:
    """
    Extract a specific COBOL division from a source file.

    Args:
        file_path: Path to the COBOL source file
        division_name: Name of the division (e.g., 'DATA DIVISION', 'PROCEDURE DIVISION')

    Returns:
        Source code of the division, or None if division not found

    Examples:
        >>> source = extract_division("program.cbl", "DATA DIVISION")
        >>> "WORKING-STORAGE SECTION" in source
        True
    """
    boundaries = find_division_boundaries(file_path)

    # Normalize division name to uppercase
    division_name = division_name.upper()

    if division_name not in boundaries:
        return None

    start = boundaries[division_name]['start']
    end = boundaries[division_name]['end']

    return extract_lines(file_path, start, end)


def extract_paragraph(
    file_path: str,
    paragraph_name: str,
    metadata: Dict[str, Dict[str, int]]
) -> Optional[str]:
    """
    Extract a specific COBOL paragraph using metadata.

    Args:
        file_path: Path to the COBOL source file
        paragraph_name: Name of the paragraph
        metadata: Dictionary mapping paragraph names to {'start': line, 'end': line}

    Returns:
        Source code of the paragraph, or None if not found

    Examples:
        >>> metadata = {'MAIN-PARA': {'start': 10, 'end': 15}}
        >>> source = extract_paragraph("program.cbl", "MAIN-PARA", metadata)
        >>> "MAIN-PARA" in source
        True
    """
    if paragraph_name not in metadata:
        return None

    start = metadata[paragraph_name]['start']
    end = metadata[paragraph_name]['end']

    return extract_lines(file_path, start, end)


def extract_paragraphs_by_names(
    file_path: str,
    paragraph_names: List[str],
    metadata: Dict[str, Dict[str, int]]
) -> List[Dict[str, Any]]:
    """
    Extract multiple COBOL paragraphs by names.

    Args:
        file_path: Path to the COBOL source file
        paragraph_names: List of paragraph names to extract
        metadata: Dictionary mapping paragraph names to {'start': line, 'end': line}

    Returns:
        List of dictionaries with 'name' and 'source' keys (skips missing paragraphs)

    Examples:
        >>> metadata = {'PARA-1': {'start': 10, 'end': 15}, 'PARA-2': {'start': 20, 'end': 25}}
        >>> extracts = extract_paragraphs_by_names("program.cbl", ['PARA-1', 'PARA-2'], metadata)
        >>> len(extracts)
        2
    """
    extracts = []
    for name in paragraph_names:
        source = extract_paragraph(file_path, name, metadata)
        if source is not None:
            extracts.append({
                'name': name,
                'source': source
            })
    return extracts


def compress_source_code(source: str) -> str:
    """
    Compress COBOL source code by removing comments and blank lines.

    COBOL comments start with '*' in column 7 (or after leading spaces).

    Args:
        source: COBOL source code

    Returns:
        Compressed source code without comments and blank lines

    Examples:
        >>> source = "      * Comment\\n       MOVE A TO B.\\n"
        >>> compressed = compress_source_code(source)
        >>> "* Comment" not in compressed
        True
    """
    lines = source.split('\n')
    compressed_lines = []

    for line in lines:
        stripped = line.strip()
        # Skip blank lines
        if not stripped:
            continue
        # Skip comment lines (COBOL comments start with * in column 7)
        if stripped.startswith('*'):
            continue
        compressed_lines.append(line)

    return '\n'.join(compressed_lines)


def estimate_token_count(source: str) -> int:
    """
    Estimate token count for source code.

    Uses a simple heuristic: approximately 1 token per 4 characters.
    This is a rough estimate for Claude's tokenizer.

    Args:
        source: Source code string

    Returns:
        Estimated token count

    Examples:
        >>> estimate_token_count("MOVE A TO B.")
        3
    """
    # Simple heuristic: ~1 token per 4 characters
    # This is approximate for Claude tokenizer
    return len(source) // 4


def add_section_markers(sections: List[Dict[str, Any]]) -> str:
    """
    Add markdown section markers to source code sections.

    Args:
        sections: List of dicts with 'name' and 'source' keys

    Returns:
        Markdown-formatted string with headers and code blocks

    Examples:
        >>> sections = [{'name': 'DATA DIVISION', 'source': '01 VAR PIC X.'}]
        >>> marked = add_section_markers(sections)
        >>> '### DATA DIVISION' in marked
        True
    """
    if not sections:
        return ""

    result = []
    for section in sections:
        # Add markdown header
        result.append(f"### {section['name']}")
        result.append("")
        # Add code block
        result.append("```cobol")
        result.append(section['source'].rstrip())
        result.append("```")
        result.append("")

    return '\n'.join(result)
