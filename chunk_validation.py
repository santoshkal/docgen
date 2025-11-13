#!/usr/bin/env python3
"""
Chunk Documentation Validation using Pydantic

Validates that generated markdown documentation contains ALL source code lines
from the expected chunk range. Uses reconstruction method for accuracy.
"""

import re
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
    """Validates chunk documentation against expected source code"""

    def __init__(self, chunk: Dict[str, Any], markdown_output: str):
        """
        Initialize validator.

        Args:
            chunk: Chunk metadata with start_line, end_line, line_count
            markdown_output: Generated markdown documentation to validate
        """
        self.chunk = chunk
        self.markdown = markdown_output
        self.start_line = chunk['start_line']
        self.end_line = chunk['end_line']
        self.expected_line_count = chunk['line_count']

    def extract_sequence_numbers(self) -> Set[int]:
        """
        Extract all COBOL sequence numbers from markdown.

        Returns:
            Set of sequence numbers found in markdown
        """
        # Pattern: Lines starting with 6-digit sequence number
        # Example: "000010 IDENTIFICATION DIVISION."
        sequence_pattern = re.compile(r'^(\d{6})\s', re.MULTILINE)
        sequences_found = sequence_pattern.findall(self.markdown)

        return set(int(seq) for seq in sequences_found)

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

    def validate(self, min_coverage_percentage: float = 100.0) -> ChunkValidationResult:
        """
        Validate chunk documentation.

        Args:
            min_coverage_percentage: Minimum acceptable coverage (default 100%)

        Returns:
            ChunkValidationResult with validation details
        """
        # Expected lines for this chunk
        expected_lines = set(range(self.start_line, self.end_line + 1))

        # Documented lines found in markdown
        documented_lines = self.extract_documented_lines()

        # Find missing and extra lines
        missing_lines = expected_lines - documented_lines
        extra_lines = documented_lines - expected_lines

        # Calculate coverage
        found_count = len(documented_lines.intersection(expected_lines))
        coverage_percentage = (found_count / len(expected_lines) * 100) if expected_lines else 0.0

        # Find missing ranges
        missing_ranges = self.find_missing_ranges(missing_lines)

        # Determine if valid
        is_valid = (coverage_percentage >= min_coverage_percentage and len(missing_lines) == 0)

        # Create error message if invalid
        error_message = None
        if not is_valid:
            if missing_lines:
                error_message = (
                    f"INCOMPLETE DOCUMENTATION: Missing {len(missing_lines)} lines "
                    f"({100 - coverage_percentage:.2f}% of chunk). "
                    f"Expected lines {self.start_line}-{self.end_line}, "
                    f"but found only {found_count} lines. "
                )

                if missing_ranges:
                    # Show first 5 gap ranges
                    gap_examples = []
                    for start, end in missing_ranges[:5]:
                        gap_size = end - start + 1
                        seq_start = self.line_to_sequence(start)
                        seq_end = self.line_to_sequence(end)
                        gap_examples.append(
                            f"Lines {start}-{end} (Sequences {seq_start:06d}-{seq_end:06d}, {gap_size} lines)"
                        )

                    error_message += "\nLargest gaps:\n  - " + "\n  - ".join(gap_examples)

                    if len(missing_ranges) > 5:
                        error_message += f"\n  - ... and {len(missing_ranges) - 5} more gaps"

        # Build validation details
        validation_details = {
            'chunk_start': self.start_line,
            'chunk_end': self.end_line,
            'expected_sequences': f"{self.line_to_sequence(self.start_line):06d}-{self.line_to_sequence(self.end_line):06d}",
            'total_gaps': len(missing_ranges),
            'largest_gap_size': max((end - start + 1 for start, end in missing_ranges), default=0)
        }

        return ChunkValidationResult(
            is_valid=is_valid,
            expected_lines=len(expected_lines),
            found_lines=found_count,
            coverage_percentage=coverage_percentage,
            missing_line_ranges=missing_ranges,
            missing_line_count=len(missing_lines),
            extra_lines=sorted(extra_lines),
            error_message=error_message,
            validation_details=validation_details
        )

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
4. Ensure every line appears with its 6-digit sequence number

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
2. Include EVERY line in your markdown code blocks (```cobol ... ```)
3. Even boring/repetitive code MUST be included
4. Data Division tables with hundreds of FILLER entries MUST be shown completely
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
    print("\nUsage:")
    print("  from chunk_validation import validate_chunk_documentation")
    print("  result = validate_chunk_documentation(chunk, markdown_output)")
    print("  if not result.is_valid:")
    print("      print(result.error_message)")
