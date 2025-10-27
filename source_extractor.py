"""
Source Code Extractor for COBOL Documentation Agent

This module provides functions to extract specific lines and sections from COBOL source files
using metadata (line numbers from ctags, superbol, gnucobol).

Implements Tier 1 of the four-tier extraction strategy: Metadata-based structured extraction.
"""

from typing import Optional


def extract_lines(file_path: str, start: int, end: int) -> str:
    """
    Extract a range of lines from a file.

    Args:
        file_path: Path to the source file
        start: Starting line number (1-indexed)
        end: Ending line number (1-indexed, inclusive)

    Returns:
        Extracted lines as a string with newlines preserved

    Examples:
        >>> extract_lines("program.cbl", 1, 10)
        'Line 1\\nLine 2\\n...Line 10\\n'
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # Convert 1-indexed to 0-indexed
        return ''.join(lines[start-1:end])
