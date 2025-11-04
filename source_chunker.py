"""
Smart Source Code Chunking for Large COBOL Files

This module handles intelligent chunking of large COBOL source files for
detailed code-block explanation, ensuring:
1. No code is missed (complete coverage)
2. No code is duplicated (no overlap in content)
3. Logical boundaries (split at paragraph/section boundaries)
4. Context preservation (metadata about chunk position)
"""

from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path


def estimate_tokens(text: str) -> int:
    """
    Estimate token count for text.

    Conservative estimate: 1 token ≈ 4 characters
    """
    return len(text) // 4


def find_paragraph_boundaries(lines: List[str], ctags_metadata: Optional[Dict] = None) -> List[int]:
    """
    Find paragraph boundaries in COBOL source code.

    Uses multiple strategies:
    1. CTags metadata (if available) - most accurate
    2. Pattern matching for paragraph names (lines starting at column 8-12 with period)
    3. Section boundaries (DIVISION, SECTION keywords)

    Args:
        lines: List of source code lines
        ctags_metadata: Optional CTags metadata with paragraph information

    Returns:
        List of line numbers (0-indexed) where paragraphs start
    """
    boundaries = [0]  # Always start at line 0

    # Strategy 1: Use CTags metadata if available
    if ctags_metadata and 'symbols' in ctags_metadata:
        for symbol in ctags_metadata['symbols']:
            if symbol.get('kind') == 'paragraph' and 'line' in symbol:
                line_num = symbol['line'] - 1  # Convert to 0-indexed
                if line_num not in boundaries and 0 <= line_num < len(lines):
                    boundaries.append(line_num)

    # Strategy 2: Pattern matching for COBOL paragraphs and divisions
    for i, line in enumerate(lines):
        stripped = line.strip().upper()

        # Division boundaries
        if stripped.endswith(' DIVISION.'):
            if i not in boundaries:
                boundaries.append(i)

        # Section boundaries
        elif stripped.endswith(' SECTION.'):
            if i not in boundaries:
                boundaries.append(i)

        # Paragraph patterns (heuristic for COBOL-74/85)
        # Paragraphs typically start in column 8-12 and end with period
        elif len(line) >= 8 and line[7] != ' ' and stripped.endswith('.'):
            # Check if it's not a comment line
            if not (len(line) > 6 and line[6] in '*/-'):
                if i not in boundaries:
                    boundaries.append(i)

    # Sort boundaries
    boundaries = sorted(set(boundaries))

    return boundaries


def find_statement_boundaries_within_section(
    lines: List[str],
    start_line: int,
    end_line: int
) -> List[int]:
    """
    Find statement boundaries within a large paragraph/section.

    Used for secondary splitting when a single paragraph exceeds token limits.

    Looks for:
    1. COBOL statement endings (lines ending with period not in column 7)
    2. Control flow keywords (IF, PERFORM, EVALUATE, etc.)
    3. Blank lines
    4. Comment blocks

    Args:
        lines: All source lines
        start_line: Start of section (0-indexed)
        end_line: End of section (0-indexed)

    Returns:
        List of line numbers within section where safe splits can occur
    """
    sub_boundaries = [start_line]

    for i in range(start_line, end_line):
        if i >= len(lines):
            break

        line = lines[i]
        stripped = line.strip().upper()

        # Skip comment lines
        if len(line) > 6 and line[6] in '*/-':
            continue

        # Statement ending (period not in column 7)
        if stripped.endswith('.') and not (len(line) > 6 and line[6] == '.'):
            sub_boundaries.append(i + 1)  # Start next section on next line

        # Control flow keywords at start of statement
        elif any(stripped.startswith(kw) for kw in [
            'IF ', 'PERFORM ', 'EVALUATE ', 'WHEN ', 'ELSE',
            'READ ', 'WRITE ', 'OPEN ', 'CLOSE ', 'CALL ',
            'MOVE ', 'COMPUTE ', 'ADD ', 'SUBTRACT ', 'MULTIPLY ', 'DIVIDE '
        ]):
            if i not in sub_boundaries:
                sub_boundaries.append(i)

        # Blank line
        elif stripped == '':
            if i + 1 not in sub_boundaries and i + 1 < end_line:
                sub_boundaries.append(i + 1)

    return sorted(set(sub_boundaries))


def create_chunks_at_boundaries(
    lines: List[str],
    boundaries: List[int],
    max_tokens_per_chunk: int = 100000
) -> List[Dict[str, Any]]:
    """
    Create chunks by grouping content between boundaries.

    **Semantic Chunking Strategy:**
    1. Respect paragraph/section boundaries (primary)
    2. If a single paragraph exceeds limit, split at statement boundaries (secondary)
    3. Only as last resort, split at arbitrary line count

    Ensures:
    - No missing lines (coverage verification)
    - No duplicate lines (exclusive ranges)
    - Respect token limits
    - Never split mid-statement

    Args:
        lines: Source code lines
        boundaries: Line numbers where natural breaks occur
        max_tokens_per_chunk: Maximum tokens per chunk

    Returns:
        List of chunk dictionaries with metadata
    """
    chunks = []
    current_chunk_start = 0
    current_chunk_lines = []
    current_tokens = 0

    for i in range(len(boundaries)):
        next_boundary = boundaries[i + 1] if i + 1 < len(boundaries) else len(lines)

        # Get lines from current boundary to next
        section_lines = lines[boundaries[i]:next_boundary]
        section_text = ''.join(section_lines)
        section_tokens = estimate_tokens(section_text)

        # Case 1: Adding this section keeps us under limit
        if current_tokens + section_tokens <= max_tokens_per_chunk:
            current_chunk_lines.extend(section_lines)
            current_tokens += section_tokens

        # Case 2: Adding this section would exceed limit, and we have content in current chunk
        elif current_chunk_lines:
            # Save current chunk
            chunk_text = ''.join(current_chunk_lines)
            chunks.append({
                'chunk_number': len(chunks) + 1,
                'start_line': current_chunk_start + 1,
                'end_line': current_chunk_start + len(current_chunk_lines),
                'line_count': len(current_chunk_lines),
                'content': chunk_text,
                'estimated_tokens': current_tokens
            })

            # Start new chunk with this section
            current_chunk_start = boundaries[i]
            current_chunk_lines = section_lines
            current_tokens = section_tokens

        # Case 3: CRITICAL - This single section itself exceeds the limit!
        # Need secondary splitting at statement boundaries
        else:
            print(f"  ⚠ Large paragraph detected: {len(section_lines):,} lines (~{section_tokens:,} tokens)")
            print(f"     Applying semantic statement-level splitting...")

            # Find statement boundaries within this large section
            statement_boundaries = find_statement_boundaries_within_section(
                lines, boundaries[i], next_boundary
            )

            print(f"     Found {len(statement_boundaries)} statement boundaries")

            # Recursively chunk at statement level
            statement_chunks = create_chunks_at_statement_boundaries(
                lines, statement_boundaries, max_tokens_per_chunk
            )

            # Add all statement-level chunks
            for stmt_chunk in statement_chunks:
                chunks.append({
                    'chunk_number': len(chunks) + 1,
                    'start_line': stmt_chunk['start_line'],
                    'end_line': stmt_chunk['end_line'],
                    'line_count': stmt_chunk['line_count'],
                    'content': stmt_chunk['content'],
                    'estimated_tokens': stmt_chunk['estimated_tokens']
                })

            # Reset for next section
            current_chunk_start = next_boundary
            current_chunk_lines = []
            current_tokens = 0

    # Add final chunk
    if current_chunk_lines:
        chunk_text = ''.join(current_chunk_lines)
        chunks.append({
            'chunk_number': len(chunks) + 1,
            'start_line': current_chunk_start + 1,
            'end_line': current_chunk_start + len(current_chunk_lines),
            'line_count': len(current_chunk_lines),
            'content': chunk_text,
            'estimated_tokens': current_tokens
        })

    return chunks


def create_chunks_at_statement_boundaries(
    lines: List[str],
    statement_boundaries: List[int],
    max_tokens_per_chunk: int
) -> List[Dict[str, Any]]:
    """
    Create chunks at statement-level boundaries (secondary splitting).

    Used when a single paragraph is too large.

    Args:
        lines: All source lines
        statement_boundaries: Statement boundary positions
        max_tokens_per_chunk: Token limit

    Returns:
        List of chunks
    """
    chunks = []
    current_start = statement_boundaries[0]
    current_lines = []
    current_tokens = 0

    for i in range(len(statement_boundaries)):
        next_boundary = statement_boundaries[i + 1] if i + 1 < len(statement_boundaries) else len(lines)

        # Get lines from current statement to next
        stmt_lines = lines[statement_boundaries[i]:next_boundary]
        stmt_tokens = estimate_tokens(''.join(stmt_lines))

        if current_tokens + stmt_tokens <= max_tokens_per_chunk:
            current_lines.extend(stmt_lines)
            current_tokens += stmt_tokens
        elif current_lines:
            # Save chunk
            chunks.append({
                'start_line': current_start + 1,
                'end_line': current_start + len(current_lines),
                'line_count': len(current_lines),
                'content': ''.join(current_lines),
                'estimated_tokens': current_tokens
            })

            # Start new
            current_start = statement_boundaries[i]
            current_lines = stmt_lines
            current_tokens = stmt_tokens
        else:
            # Even a single statement exceeds limit - take it anyway (last resort)
            chunks.append({
                'start_line': statement_boundaries[i] + 1,
                'end_line': next_boundary,
                'line_count': len(stmt_lines),
                'content': ''.join(stmt_lines),
                'estimated_tokens': stmt_tokens
            })
            current_start = next_boundary
            current_lines = []
            current_tokens = 0

    # Add final
    if current_lines:
        chunks.append({
            'start_line': current_start + 1,
            'end_line': current_start + len(current_lines),
            'line_count': len(current_lines),
            'content': ''.join(current_lines),
            'estimated_tokens': current_tokens
        })

    return chunks


def verify_chunk_coverage(chunks: List[Dict[str, Any]], total_lines: int) -> Dict[str, Any]:
    """
    Verify that chunks cover all lines with no gaps or overlaps.

    Args:
        chunks: List of chunk dictionaries
        total_lines: Total number of lines in source file

    Returns:
        Verification result dictionary
    """
    covered_lines = set()

    for chunk in chunks:
        start = chunk['start_line']
        end = chunk['end_line']

        # Check for overlaps
        chunk_range = set(range(start, end + 1))
        overlap = covered_lines.intersection(chunk_range)

        if overlap:
            return {
                'valid': False,
                'error': f"Chunk {chunk['chunk_number']} overlaps with previous chunks at lines {sorted(overlap)}"
            }

        covered_lines.update(chunk_range)

    # Check for gaps
    all_lines = set(range(1, total_lines + 1))
    missing_lines = all_lines - covered_lines

    if missing_lines:
        return {
            'valid': False,
            'error': f"Missing lines: {sorted(missing_lines)[:10]}..." if len(missing_lines) > 10 else f"Missing lines: {sorted(missing_lines)}"
        }

    # Check for extra lines
    extra_lines = covered_lines - all_lines

    if extra_lines:
        return {
            'valid': False,
            'error': f"Extra lines beyond file end: {sorted(extra_lines)}"
        }

    return {
        'valid': True,
        'total_lines': total_lines,
        'chunks': len(chunks),
        'coverage': '100%'
    }


def chunk_large_cobol_file(
    file_path: str,
    max_tokens_per_chunk: int = 100000,
    ctags_metadata: Optional[Dict] = None
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """
    Intelligently chunk a large COBOL file for processing.

    Main entry point that:
    1. Reads the file
    2. Finds logical boundaries
    3. Creates chunks
    4. Verifies coverage

    Args:
        file_path: Path to COBOL source file
        max_tokens_per_chunk: Maximum tokens per chunk (default 100K)
        ctags_metadata: Optional CTags metadata for better boundary detection

    Returns:
        Tuple of (chunks, verification_result)

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If chunking verification fails
    """
    # Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)

    # Find boundaries
    boundaries = find_paragraph_boundaries(lines, ctags_metadata)

    print(f"  → File: {total_lines:,} lines")
    print(f"  → Found {len(boundaries):,} paragraph/section boundaries")

    # Create chunks
    chunks = create_chunks_at_boundaries(lines, boundaries, max_tokens_per_chunk)

    print(f"  → Created {len(chunks)} chunks")
    for chunk in chunks:
        print(f"     Chunk {chunk['chunk_number']}: Lines {chunk['start_line']}-{chunk['end_line']} "
              f"({chunk['line_count']:,} lines, ~{chunk['estimated_tokens']:,} tokens)")

    # Verify coverage
    verification = verify_chunk_coverage(chunks, total_lines)

    if not verification['valid']:
        raise ValueError(f"Chunking verification failed: {verification['error']}")

    print(f"  ✓ Verification passed: {verification['coverage']} coverage")

    return chunks, verification


def format_chunk_for_llm(chunk: Dict[str, Any], total_chunks: int, file_name: str) -> str:
    """
    Format a chunk with metadata for LLM processing.

    Adds context about chunk position in file.

    Args:
        chunk: Chunk dictionary
        total_chunks: Total number of chunks
        file_name: Name of source file

    Returns:
        Formatted string with metadata + content
    """
    header = f"""
=============================================================================
CHUNK {chunk['chunk_number']} of {total_chunks} - {file_name}
=============================================================================
Lines: {chunk['start_line']} to {chunk['end_line']} ({chunk['line_count']:,} lines)
Estimated Tokens: ~{chunk['estimated_tokens']:,}

IMPORTANT INSTRUCTIONS:
- This is chunk {chunk['chunk_number']} of {total_chunks} chunks
- Continue numbering sequentially from previous chunks
- If this is chunk 1, start numbering from 1
- If this is chunk 2+, continue from where the previous chunk ended
- Parse EVERY line in this chunk - do not skip content
- Group paragraphs only when they implement a single functionality
=============================================================================

"""

    return header + chunk['content']
