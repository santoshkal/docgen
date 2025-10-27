"""
Source Code Extractor for COBOL Documentation Agent

This module provides functions to extract specific lines and sections from COBOL source files
using metadata (line numbers from ctags, superbol, gnucobol).

Implements Tier 1 of the four-tier extraction strategy: Metadata-based structured extraction.
"""

import hashlib
from typing import Optional, List, Tuple


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
