"""
Source Code Extractor for COBOL Documentation Agent

This module provides functions to extract specific lines and sections from COBOL source files
using metadata (line numbers from ctags, superbol, gnucobol).

Implements Tier 1 of the four-tier extraction strategy: Metadata-based structured extraction.
"""

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
