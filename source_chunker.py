"""
Smart Source Code Chunking for Large COBOL Files

This module handles intelligent chunking of large COBOL source files for
detailed code-block explanation, ensuring:
1. No code is missed (complete coverage)
2. No code is duplicated (no overlap in content)
3. Logical boundaries (split at paragraph/section boundaries)
4. Context preservation (metadata about chunk position)
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Try to import tiktoken for accurate token counting
try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False


def estimate_tokens(text: str, model: str = "gpt-4") -> int:
    """
    Calculate accurate token count for text using tiktoken.

    Falls back to conservative estimate (1 token ≈ 4 characters) if tiktoken unavailable.

    Args:
        text: Text to count tokens for
        model: Model name for tiktoken encoder (default: gpt-4)

    Returns:
        Token count
    """
    if TIKTOKEN_AVAILABLE:
        try:
            encoder = tiktoken.encoding_for_model(model)
            return len(encoder.encode(text))
        except Exception as e:
            # Fallback to estimation if tiktoken fails
            print(f"  ⚠ tiktoken failed ({e}), using estimation")
            return len(text) // 4
    else:
        # Fallback: Conservative estimate (1 token ≈ 4 characters)
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
    if ctags_metadata:
        # Debug: Show structure keys
        if isinstance(ctags_metadata, dict):
            print(f"  → CTags metadata keys: {list(ctags_metadata.keys())}")
        else:
            print(f"  → CTags metadata type: {type(ctags_metadata)}")

        # Handle different CTags metadata structures
        symbols = None

        # New format: {'outline': {'other': [...]}}
        if 'outline' in ctags_metadata and 'other' in ctags_metadata['outline']:
            symbols = ctags_metadata['outline']['other']
        # Legacy format: {'symbols': [...]}
        elif 'symbols' in ctags_metadata:
            symbols = ctags_metadata['symbols']

        # Extract paragraph boundaries from symbols
        if symbols:
            paragraph_count = 0
            for symbol in symbols:
                if symbol.get('kind') == 'paragraph' and 'line' in symbol:
                    line_num = symbol['line'] - 1  # Convert to 0-indexed
                    if line_num not in boundaries and 0 <= line_num < len(lines):
                        boundaries.append(line_num)
                        paragraph_count += 1

            if paragraph_count > 0:
                print(f"  → Using CTags: Found {paragraph_count:,} paragraphs from metadata")
            else:
                print(f"  ⚠ CTags metadata provided but no paragraphs found, falling back to pattern matching")
        else:
            print(f"  ⚠ CTags metadata structure not recognized, falling back to pattern matching")
    else:
        print(f"  ⚠ No CTags metadata provided, using pattern matching for boundaries")

    # Strategy 2: Pattern matching for COBOL paragraphs and divisions (fallback)
    initial_boundary_count = len(boundaries)

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

    # Report pattern matching additions
    pattern_additions = len(boundaries) - initial_boundary_count
    if pattern_additions > 0:
        print(f"  → Pattern matching: Added {pattern_additions:,} additional boundaries")

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
    max_tokens_per_chunk: int = 100000,
    overhead_tokens: int = 0
) -> List[Dict[str, Any]]:
    """
    Create chunks by grouping content between boundaries.

    **Semantic Chunking Strategy:**
    1. Respect paragraph/section boundaries (primary)
    2. If a single paragraph exceeds limit, split at statement boundaries (secondary)
    3. For huge data tables, split by line groups as last resort

    Ensures:
    - No missing lines (coverage verification)
    - No duplicate lines (exclusive ranges)
    - Respect token limits (including overhead like program maps)
    - Never split mid-statement

    Args:
        lines: Source code lines
        boundaries: Line numbers where natural breaks occur
        max_tokens_per_chunk: Maximum tokens per chunk
        overhead_tokens: Estimated overhead (headers, program map, etc.) to reserve

    Returns:
        List of chunk dictionaries with metadata
    """
    chunks = []
    current_chunk_start = 0

    # Reserve space for overhead (program map, headers, etc.)
    effective_max_tokens = max_tokens_per_chunk - overhead_tokens
    if effective_max_tokens < 1000:
        print(f"  ⚠ WARNING: Overhead ({overhead_tokens:,} tokens) leaves only {effective_max_tokens:,} tokens for content")
        effective_max_tokens = max_tokens_per_chunk // 2  # Use at least half

    if overhead_tokens > 0:
        print(f"  → Adjusted chunk limit: {max_tokens_per_chunk:,} - {overhead_tokens:,} (overhead) = {effective_max_tokens:,} tokens per chunk")
    current_chunk_lines = []
    current_tokens = 0

    for i in range(len(boundaries)):
        next_boundary = boundaries[i + 1] if i + 1 < len(boundaries) else len(lines)

        # Get lines from current boundary to next
        section_lines = lines[boundaries[i]:next_boundary]
        section_text = ''.join(section_lines)
        section_tokens = estimate_tokens(section_text, model="gpt-4")  # Use tiktoken

        # Case 1: Adding this section keeps us under limit
        if current_tokens + section_tokens <= effective_max_tokens:
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
                lines, statement_boundaries, effective_max_tokens
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
        # extract common elements fromthe covered_lines set
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


def verify_chunk_reconstruction(chunks: List[Dict[str, Any]], original_content: str) -> Dict[str, Any]:
    """
    Verify chunks by reconstructing original content and comparing.

    This is the MOST ACCURATE verification method:
    - Reconstructs the file by concatenating all chunk contents in order
    - Compares byte-for-byte with original
    - If identical, proves 100% coverage, no overlaps, correct order, content integrity

    Args:
        chunks: List of chunk dictionaries (must be in order)
        original_content: Original file content as string

    Returns:
        Verification result dictionary with:
        - valid: True if perfect match, False otherwise
        - method: 'reconstruction'
        - reconstructed_size: Size of reconstructed content
        - original_size: Size of original content
        - match: True if byte-for-byte identical
        - error: Error message if mismatch (with diff preview)
    """
    # Reconstruct file from chunks
    reconstructed_content = ''.join(chunk['content'] for chunk in chunks)

    # Byte-for-byte comparison
    perfect_match = (reconstructed_content == original_content)

    result = {
        'valid': perfect_match,
        'method': 'reconstruction',
        'reconstructed_size': len(reconstructed_content),
        'original_size': len(original_content),
        'match': perfect_match,
        'chunks': len(chunks)
    }

    if perfect_match:
        result['coverage'] = '100%'
        result['message'] = 'Perfect reconstruction - chunks are identical to original'
    else:
        # Provide diagnostic information
        size_diff = len(reconstructed_content) - len(original_content)
        result['size_difference'] = size_diff

        # Find first difference
        min_len = min(len(original_content), len(reconstructed_content))
        first_diff_pos = None

        for i in range(min_len):
            if original_content[i] != reconstructed_content[i]:
                first_diff_pos = i
                break

        if first_diff_pos is not None:
            result['first_difference_at'] = first_diff_pos
            # Show context around first difference
            context_start = max(0, first_diff_pos - 50)
            context_end = min(len(original_content), first_diff_pos + 50)
            result['diff_context'] = {
                'position': first_diff_pos,
                'original': original_content[context_start:context_end],
                'reconstructed': reconstructed_content[context_start:context_end] if first_diff_pos < len(reconstructed_content) else '(end of file)'
            }

        # Construct error message
        if size_diff > 0:
            error_msg = f"Reconstructed is {size_diff} chars larger (possible overlap/duplication)"
        elif size_diff < 0:
            error_msg = f"Reconstructed is {abs(size_diff)} chars smaller (missing content)"
        else:
            error_msg = "Same size but content differs"

        if first_diff_pos is not None:
            error_msg += f" - first difference at position {first_diff_pos}"

        result['error'] = error_msg

    return result


def chunk_large_cobol_file(
    file_path: str,
    max_tokens_per_chunk: int = 100000,
    ctags_metadata: Optional[Dict] = None,
    program_map: Optional[str] = None
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """
    Intelligently chunk a large COBOL file for processing.

    Main entry point that:
    1. Reads the file
    2. Finds logical boundaries
    3. Creates chunks accounting for overhead (headers, program map)
    4. Verifies coverage

    Args:
        file_path: Path to COBOL source file
        max_tokens_per_chunk: Maximum tokens per chunk (default 100K)
        ctags_metadata: Optional CTags metadata for better boundary detection
        program_map: Optional program map that will be added to each chunk (used to calculate overhead)

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

    # Calculate overhead tokens (program map + headers)
    overhead_tokens = 0
    if program_map:
        program_map_tokens = estimate_tokens(program_map, model="gpt-4")
        header_tokens = 500  # Approximate header size
        total_overhead = program_map_tokens + header_tokens

        # Safety check: if overhead is too large relative to max_tokens, warn user
        if total_overhead > max_tokens_per_chunk * 0.7:  # More than 70% overhead!
            print(f"  ⚠ WARNING: Program map is VERY large ({program_map_tokens:,} tokens)")
            print(f"     This leaves only {max_tokens_per_chunk - total_overhead:,} tokens for source code per chunk")
            print(f"     Consider: 1) Increasing max_tokens_per_chunk, or 2) Removing program_map from chunks")
            # Still use it, but warn

        overhead_tokens = total_overhead
        print(f"  → Program map overhead: {program_map_tokens:,} tokens + {header_tokens} (headers) = {overhead_tokens:,} tokens")
    else:
        # Even without program_map, reserve space for headers and safety margin
        overhead_tokens = 1000  # Safety margin
        print(f"  → Reserving {overhead_tokens:,} tokens for headers and safety margin")

    # Create chunks with overhead consideration
    chunks = create_chunks_at_boundaries(lines, boundaries, max_tokens_per_chunk, overhead_tokens)

    print(f"  → Created {len(chunks)} chunks")
    for chunk in chunks:
        print(f"     Chunk {chunk['chunk_number']}: Lines {chunk['start_line']}-{chunk['end_line']} "
              f"({chunk['line_count']:,} lines, ~{chunk['estimated_tokens']:,} tokens)")

    # Verify coverage using set-based method (fast check for gaps/overlaps)
    verification = verify_chunk_coverage(chunks, total_lines)

    if not verification['valid']:
        raise ValueError(f"Chunking verification failed: {verification['error']}")

    print(f"  ✓ Set-based verification passed: {verification['coverage']} coverage")

    # Additional verification via reconstruction (most accurate)
    original_content = ''.join(lines)
    reconstruction_result = verify_chunk_reconstruction(chunks, original_content)

    if not reconstruction_result['valid']:
        raise ValueError(f"Reconstruction verification failed: {reconstruction_result['error']}")

    print(f"  ✓ Reconstruction verification passed: byte-for-byte match")

    # Combine verification results
    verification['reconstruction'] = reconstruction_result
    verification['method'] = 'set-based + reconstruction'

    return chunks, verification


def format_chunk_for_llm(
    chunk: Dict[str, Any],
    total_chunks: int,
    file_name: str,
    program_map: Optional[str] = None,
    model: str = "gpt-4"
) -> str:
    """
    Format a chunk with metadata for LLM processing.

    Adds context about chunk position in file and optional program map.
    Calculates actual token count using tiktoken for accurate sizing.

    Args:
        chunk: Chunk dictionary
        total_chunks: Total number of chunks
        file_name: Name of source file
        program_map: Optional program map providing whole-file context
        model: Model name for tiktoken encoder (default: gpt-4)

    Returns:
        Formatted string with metadata + content
    """
    # Calculate actual token count for the full formatted content
    # This includes metadata, program map, and source code
    full_content = chunk['content']
    if program_map:
        full_content = program_map + "\n\n" + full_content

    actual_tokens = estimate_tokens(full_content, model=model)

    # Show both estimated (for chunk splitting) and actual (for LLM input)
    token_info = f"Chunk Tokens (estimated): ~{chunk['estimated_tokens']:,}"
    if TIKTOKEN_AVAILABLE:
        token_info += f"\nActual Input Tokens: {actual_tokens:,} (measured with tiktoken)"

    header = f"""
=============================================================================
CHUNK {chunk['chunk_number']} of {total_chunks} - {file_name}
=============================================================================
Lines: {chunk['start_line']} to {chunk['end_line']} ({chunk['line_count']:,} lines)
{token_info}

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines {chunk['start_line']}-{chunk['end_line']} sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk {chunk['chunk_number']} of {total_chunks} chunks
- Continue numbering sequentially from previous chunks
- If this is chunk 1, start numbering from 1
- If this is chunk 2+, continue from where the previous chunk ended
- Parse EVERY line in this chunk - do not skip any content
- Group paragraphs ONLY when they implement a single functionality
- Provide completion checklist at end listing all documented paragraphs
=============================================================================

"""

    # Add program map if provided (gives whole-file context for this chunk)
    if program_map:
        header += f"""
{program_map}

NOTE: The above program map shows the ENTIRE program structure for context.
      The source code below is only CHUNK {chunk['chunk_number']} of {total_chunks}.

"""

    # Wrap source code in markdown code block for clear visual separation
    # This helps LLM distinguish source code from metadata/instructions
    # and makes it obvious what content needs to be documented
    source_code_section = f"""
=============================================================================
CHUNK {chunk['chunk_number']} SOURCE CODE (Lines {chunk['start_line']}-{chunk['end_line']})
=============================================================================

```cobol
{chunk['content']}```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL {chunk['line_count']:,} lines from {chunk['start_line']} to {chunk['end_line']}.

    You MUST include EVERY line from this code block in your documentation output.

    🚨 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):
    ============================================================================
    COBOL-74 comments are marked with "*" in column 7 (after the 6-digit sequence number).

    Example comment lines:
      000020* This is a comment
      000026*REMARKS.
      000028*  SYSTEM    : TDAR

    ⚠️  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!

    Comments are NOT "already documented" - they are SOURCE CODE that must be preserved.
    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.

    DO NOT:
    - Skip comment lines thinking they don't need documentation
    - Omit comment blocks (even if they span 100+ lines)
    - Exclude REMARKS sections, copyright notices, or build information
    - Remove any line that starts with a * after the sequence number

    DO:
    - Include EVERY line starting with 000010* through 999999*
    - Preserve all comment formatting exactly as shown
    - Show complete comment blocks in their entirety
    - Treat comments as essential source code content
    ============================================================================

    **IMPORTANT - Document ALL COBOL Divisions:**
    - IDENTIFICATION DIVISION: Include program metadata verbatim
    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim
    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim
    - PROCEDURE DIVISION: Include all paragraphs with code and explanations

    Do NOT skip:
    - Data tables (even with thousands of FILLER definitions)
    - WORKING-STORAGE variables
    - FILE SECTION record layouts
    - ANY lines from the source code above

    Each line starts with a 6-digit sequence number (e.g., 003240).
    Include these sequence numbers in your code blocks to prove coverage.
"""

    return header + source_code_section
