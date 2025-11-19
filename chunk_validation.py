#!/usr/bin/env python3
"""
Chunk Documentation Validation using Pydantic

Validates that generated markdown documentation contains ALL source code lines
from the expected chunk range.

Supports two validation strategies:
1. Pattern-based: Fast validation using configurable line identifier patterns (e.g., COBOL sequence numbers)
2. Diff-based: Robust fallback using content comparison (language-agnostic)
"""

import re
import difflib
from typing import List, Set, Dict, Any, Optional
from pydantic import BaseModel, Field, field_validator, model_validator

class ChunkValidationResult(BaseModel):
    """Result of validating chunk documentation"""

    is_valid: bool = Field(..., description="Whether validation passed")
    expected_lines: int = Field(..., description="Number of lines expected in chunk")
    found_lines: int = Field(..., description="Number of lines found in documentation")
    coverage_percentage: float = Field(..., description="Percentage of lines found")
    missing_line_ranges: List[tuple[int, int]] = Field(default_factory=list, description="Ranges of missing lines")
    missing_line_count: int = Field(..., description="Total number of missing lines")
    extra_lines: List[int] = Field(default_factory=list, description="Lines found but not expected")
    error_message: Optional[str] = Field(None, description="Error message if validation failed")
    validation_details: Dict[str, Any] = Field(default_factory=dict, description="Additional validation details")
    validation_method: Optional[str] = Field(None, description="Method used for validation: 'pattern-based' or 'diff-based'")

    @field_validator('coverage_percentage')
    @classmethod
    def validate_coverage(cls, v: float) -> float:
        """Ensure coverage is between 0 and 100"""
        if not 0 <= v <= 100:
            raise ValueError(f"Coverage percentage must be between 0 and 100, got {v}")
        return round(v, 2)

    @model_validator(mode='after')
    def validate_consistency(self):
        """Ensure validation result is internally consistent"""
        # If 100% coverage, should be valid
        if self.coverage_percentage == 100.0 and self.missing_line_count == 0:
            if not self.is_valid:
                self.is_valid = True  # Auto-correct

        # If missing lines, should not be valid
        if self.missing_line_count > 0:
            if self.is_valid:
                self.is_valid = False  # Auto-correct
                if not self.error_message:
                    self.error_message = f"Missing {self.missing_line_count} lines from documentation"

        return self


class ChunkDocumentationValidator:
    """
    Validates chunk documentation against expected source code.

    Supports two validation strategies:
    1. Pattern-based: Uses configurable regex pattern to extract line identifiers
    2. Diff-based: Compares actual content using difflib (fallback)
    """

    def __init__(self, chunk: Dict[str, Any], markdown_output: str, line_pattern: Optional[str] = None):
        """
        Initialize validator.

        Args:
            chunk: Chunk metadata with start_line, end_line, line_count, content
            markdown_output: Generated markdown documentation to validate
            line_pattern: Optional regex pattern for line identifiers (e.g., r'^\d{6}' for COBOL)
                         If not provided, will check chunk metadata for 'line_identifier_pattern'
        """
        self.chunk = chunk
        self.markdown = markdown_output
        self.start_line = chunk['start_line']
        self.end_line = chunk['end_line']
        self.expected_line_count = chunk['line_count']

        # Get line pattern from: parameter > chunk metadata > default
        self.line_pattern = (
            line_pattern or
            chunk.get('line_identifier_pattern') or
            r'^\d{6}'  # Default: COBOL sequence numbers
        )

    def _has_line_pattern(self) -> bool:
        """Check if a line pattern is available for pattern-based validation"""
        return self.line_pattern is not None

    def _extract_code_blocks_from_markdown(self) -> str:
        """
        Extract all code blocks from markdown output.

        Returns:
            Concatenated code from all code blocks
        """
        # Match: ```language\nCODE\n```
        pattern = r'```\w*\n(.*?)\n```'
        blocks = re.findall(pattern, self.markdown, re.DOTALL)
        return '\n'.join(blocks)

    def extract_line_identifiers_from_text(self, text: str) -> Set[str]:
        """
        Extract line identifiers from text using the configured pattern.

        Args:
            text: Source text to extract from

        Returns:
            Set of line identifier strings (e.g., {'000010', '000012', ...})
        """
        pattern = re.compile(self.line_pattern, re.MULTILINE)
        matches = pattern.findall(text)
        return set(matches)

    def extract_sequence_numbers(self) -> Set[int]:
        """
        Extract all COBOL sequence numbers from markdown (backward compatibility).

        Returns:
            Set of sequence numbers found in markdown
        """
        identifiers = self.extract_line_identifiers_from_text(self.markdown)
        # Convert to integers if possible
        try:
            return set(int(seq) for seq in identifiers)
        except ValueError:
            # Not all integers - return as-is
            return set()

    def sequence_to_line(self, sequence: int) -> int:
        """
        Convert COBOL sequence number to line number.

        COBOL sequence numbers start at 000010 and increment by 2.
        Line 1 = 000010, Line 2 = 000012, etc.

        Args:
            sequence: Sequence number (e.g., 000010)

        Returns:
            Line number (e.g., 1)
        """
        if sequence < 10:
            return 0  # Invalid
        return (sequence - 10) // 2 + 1

    def line_to_sequence(self, line: int) -> int:
        """
        Convert line number to COBOL sequence number.

        Args:
            line: Line number (e.g., 1)

        Returns:
            Sequence number (e.g., 000010)
        """
        return 10 + (line - 1) * 2

    def extract_documented_lines(self) -> Set[int]:
        """
        Extract all line numbers documented in markdown.

        Returns:
            Set of line numbers found in markdown
        """
        sequences = self.extract_sequence_numbers()
        lines = set()

        for seq in sequences:
            line_num = self.sequence_to_line(seq)
            if line_num > 0:
                lines.add(line_num)

        return lines

    def find_missing_ranges(self, missing_lines: Set[int]) -> List[tuple[int, int]]:
        """
        Convert set of missing lines into contiguous ranges.

        Args:
            missing_lines: Set of missing line numbers

        Returns:
            List of (start, end) tuples representing contiguous ranges
        """
        if not missing_lines:
            return []

        sorted_lines = sorted(missing_lines)
        ranges = []
        range_start = sorted_lines[0]
        range_end = range_start

        for line in sorted_lines[1:]:
            if line == range_end + 1:
                # Extend current range
                range_end = line
            else:
                # Save current range, start new one
                ranges.append((range_start, range_end))
                range_start = line
                range_end = line

        # Don't forget the last range
        ranges.append((range_start, range_end))

        return ranges

    def _validate_by_pattern(self, min_coverage: float = 100.0) -> ChunkValidationResult:
        """
        Validate using pattern-based line identifier extraction.
        Fast but requires correct pattern configuration.

        Args:
            min_coverage: Minimum acceptable coverage percentage

        Returns:
            ChunkValidationResult with validation details
        """
        # Extract identifiers from source chunk
        source_code = self.chunk.get('content', '')
        expected_identifiers = self.extract_line_identifiers_from_text(source_code)

        # Extract identifiers from LLM output
        llm_code = self._extract_code_blocks_from_markdown()
        documented_identifiers = self.extract_line_identifiers_from_text(llm_code)

        # Calculate coverage
        if not expected_identifiers:
            # Pattern found nothing - this validation method failed
            return ChunkValidationResult(
                is_valid=False,
                expected_lines=0,
                found_lines=0,
                coverage_percentage=0.0,
                missing_line_count=0,
                validation_method='pattern-based',
                error_message="Pattern-based validation failed: no line identifiers found in source"
            )

        missing = expected_identifiers - documented_identifiers
        found = expected_identifiers & documented_identifiers
        extra = documented_identifiers - expected_identifiers

        coverage = (len(found) / len(expected_identifiers) * 100)
        is_valid = (coverage >= min_coverage and len(missing) == 0)

        # Build error message
        error_message = None
        if not is_valid:
            error_message = (
                f"INCOMPLETE DOCUMENTATION: Missing {len(missing)} line identifiers "
                f"({100 - coverage:.2f}% of chunk). "
                f"Expected {len(expected_identifiers)} identifiers, "
                f"found {len(found)}."
            )

        # Build validation details
        validation_details = {
            'validation_strategy': 'pattern-based',
            'pattern_used': self.line_pattern,
            'expected_identifier_count': len(expected_identifiers),
            'found_identifier_count': len(found),
            'missing_identifier_count': len(missing),
            'extra_identifier_count': len(extra)
        }

        return ChunkValidationResult(
            is_valid=is_valid,
            expected_lines=len(expected_identifiers),
            found_lines=len(found),
            coverage_percentage=coverage,
            missing_line_ranges=[],  # Not applicable for pattern-based
            missing_line_count=len(missing),
            extra_lines=[],  # Not applicable for pattern-based
            error_message=error_message,
            validation_details=validation_details,
            validation_method='pattern-based'
        )

    def _validate_by_diff(self, min_coverage: float = 100.0) -> ChunkValidationResult:
        """
        Validate by comparing actual source content vs LLM output using difflib.
        Language-agnostic fallback method.

        Args:
            min_coverage: Minimum acceptable coverage percentage

        Returns:
            ChunkValidationResult with validation details
        """
        # Get source code from chunk
        source_code = self.chunk.get('content', '').strip()
        source_lines = [line for line in source_code.split('\n') if line.strip()]  # Non-empty lines

        # Extract all code blocks from LLM markdown
        llm_code = self._extract_code_blocks_from_markdown().strip()
        llm_lines = [line for line in llm_code.split('\n') if line.strip()]  # Non-empty lines

        if not source_lines:
            return ChunkValidationResult(
                is_valid=False,
                expected_lines=0,
                found_lines=0,
                coverage_percentage=0.0,
                missing_line_count=0,
                validation_method='diff-based',
                error_message="Diff-based validation failed: no source lines found"
            )

        # Compare using difflib
        matcher = difflib.SequenceMatcher(
            isjunk=lambda x: x.strip() == '',
            a=source_lines,
            b=llm_lines
        )

        # Calculate similarity ratio
        similarity_ratio = matcher.ratio()  # 0.0 to 1.0
        coverage_percentage = similarity_ratio * 100

        # Find missing/changed lines
        missing_line_indices = []
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag in ('delete', 'replace'):
                # Lines in source but not in LLM output (or changed)
                missing_line_indices.extend(range(i1, i2))

        is_valid = (coverage_percentage >= min_coverage)

        # Build error message
        error_message = None
        if not is_valid:
            error_message = (
                f"INCOMPLETE DOCUMENTATION: {coverage_percentage:.1f}% content match. "
                f"Expected {len(source_lines)} lines, "
                f"found {len(llm_lines)} lines. "
                f"Approximately {len(missing_line_indices)} lines missing or changed."
            )

        # Build validation details
        validation_details = {
            'validation_strategy': 'diff-based',
            'source_line_count': len(source_lines),
            'llm_line_count': len(llm_lines),
            'similarity_ratio': similarity_ratio,
            'missing_or_changed_lines': len(missing_line_indices)
        }

        return ChunkValidationResult(
            is_valid=is_valid,
            expected_lines=len(source_lines),
            found_lines=len(llm_lines),
            coverage_percentage=coverage_percentage,
            missing_line_ranges=[],  # Not applicable for diff-based
            missing_line_count=len(missing_line_indices),
            extra_lines=[],
            error_message=error_message,
            validation_details=validation_details,
            validation_method='diff-based'
        )

    def validate(self, min_coverage_percentage: float = 100.0) -> ChunkValidationResult:
        """
        Validate chunk documentation using hybrid approach.

        Strategy:
        1. Try pattern-based validation (fast) if pattern is available
        2. If pattern-based finds 0 lines or fails, fall back to diff-based (robust)

        Args:
            min_coverage_percentage: Minimum acceptable coverage (default 100%)

        Returns:
            ChunkValidationResult with validation details
        """
        # Strategy 1: Pattern-based validation (if pattern available)
        if self._has_line_pattern():
            result = self._validate_by_pattern(min_coverage_percentage)

            # Check if pattern-based validation succeeded
            if result.found_lines > 0:
                # Pattern found something - use this result
                return result

            # Pattern failed to find anything - fall back to diff
            print(f"  ⚠ Pattern validation found 0 lines (pattern may be incorrect), falling back to diff-based validation")

        # Strategy 2: Diff-based validation (fallback or no pattern available)
        return self._validate_by_diff(min_coverage_percentage)

    def create_retry_prompt(self, validation_result: ChunkValidationResult) -> str:
        """
        Create a prompt for LLM to retry documentation with missing lines.

        Args:
            validation_result: Result from validation

        Returns:
            Prompt text for retry
        """
        if validation_result.is_valid:
            return ""  # No retry needed

        prompt = f"""
VALIDATION FAILED: Your previous documentation is INCOMPLETE.

REQUIRED: Lines {self.start_line}-{self.end_line} (Total: {self.expected_line_count} lines)
FOUND: Only {validation_result.found_lines} lines ({validation_result.coverage_percentage:.2f}% coverage)
MISSING: {validation_result.missing_line_count} lines

YOU MUST FIX THIS BY:
1. Including EVERY line from {self.start_line} to {self.end_line} in your code blocks
2. Do NOT skip data tables, FILLERs, comments, or any content
3. Show ALL repetitive code - no abbreviation or summarization
4. Ensure every line appears with its line identifier

MISSING LINE RANGES (you MUST add these):
"""

        for start, end in validation_result.missing_line_ranges[:10]:
            gap_size = end - start + 1
            seq_start = self.line_to_sequence(start)
            seq_end = self.line_to_sequence(end)
            prompt += f"\n  • Lines {start:,}-{end:,} (Sequences {seq_start:06d}-{seq_end:06d}) - {gap_size} lines missing"

        if len(validation_result.missing_line_ranges) > 10:
            prompt += f"\n  • ... and {len(validation_result.missing_line_ranges) - 10} more gaps"

        prompt += f"""

INSTRUCTIONS FOR RETRY:
1. Review the source code for lines {self.start_line}-{self.end_line}
2. Include EVERY line in your markdown code blocks
3. Even boring/repetitive code MUST be included
4. Data tables with hundreds of entries MUST be shown completely
5. Comments MUST be included
6. Validation will check that all {self.expected_line_count} lines are present

CRITICAL: If you skip any lines again, validation will fail again.
"""

        return prompt


def validate_chunk_documentation(
    chunk: Dict[str, Any],
    markdown_output: str,
    min_coverage: float = 100.0
) -> ChunkValidationResult:
    """
    Convenience function to validate chunk documentation.

    Args:
        chunk: Chunk metadata
        markdown_output: Generated markdown
        min_coverage: Minimum acceptable coverage percentage

    Returns:
        ChunkValidationResult
    """
    validator = ChunkDocumentationValidator(chunk, markdown_output)
    return validator.validate(min_coverage_percentage=min_coverage)


if __name__ == "__main__":
    # Example usage
    print("Chunk Documentation Validator")
    print("=" * 80)
    print("\nThis module validates that generated markdown contains all expected source lines.")
    print("\nSupports two validation strategies:")
    print("  1. Pattern-based: Fast validation using line identifier patterns")
    print("  2. Diff-based: Robust content comparison (language-agnostic fallback)")
    print("\nUsage:")
    print("  from chunk_validation import validate_chunk_documentation")
    print("  result = validate_chunk_documentation(chunk, markdown_output)")
    print("  if not result.is_valid:")
    print("      print(result.error_message)")
    print(f"  print(f'Validation method: {result.validation_method}')")
