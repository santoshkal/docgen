"""
Test suite for source_extractor.py

Following TDD approach: Tests written FIRST, then implementation.
"""

import pytest
import os
import tempfile
from source_extractor import (
    extract_lines,
    extract_lines_by_ranges,
    extract_lines_with_context,
    compute_source_hash,
    deduplicate_source_extracts,
    find_division_boundaries
)


# Test Fixtures for Division Extraction
@pytest.fixture
def test_cobol_file():
    """Create a test COBOL file with all divisions"""
    content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST-PROGRAM.
       AUTHOR. TEST.

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. IBM-PC.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-COUNTER PIC 9(3) VALUE 0.
       01 WS-NAME    PIC X(20).

       PROCEDURE DIVISION.
       MAIN-PARA.
           MOVE 100 TO WS-COUNTER.
           DISPLAY "Hello World".
           STOP RUN.
"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.cbl') as f:
        f.write(content)
        file_path = f.name

    yield file_path

    # Cleanup
    os.unlink(file_path)


@pytest.fixture
def test_division_metadata():
    """Metadata for test COBOL file divisions"""
    return {
        'IDENTIFICATION DIVISION': {'start': 1, 'end': 3},
        'ENVIRONMENT DIVISION': {'start': 5, 'end': 7},
        'DATA DIVISION': {'start': 9, 'end': 12},
        'PROCEDURE DIVISION': {'start': 14, 'end': 18}
    }


class TestBasicExtraction:
    """Test basic line extraction functionality"""

    def test_extract_lines_exists(self):
        """Test that extract_lines function exists"""
        assert callable(extract_lines)

    def test_extract_lines_basic(self):
        """Test basic line extraction"""
        # Create test file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.cbl') as f:
            test_file = f.name
            f.write("Line 1\n")
            f.write("Line 2\n")
            f.write("Line 3\n")

        try:
            # Test
            result = extract_lines(test_file, 1, 2)

            # Should extract lines 1-2
            assert result == "Line 1\nLine 2\n"
        finally:
            os.unlink(test_file)

    def test_extract_lines_by_ranges_single_range(self):
        """Test range extraction with single range"""
        # Create test file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.cbl') as f:
            test_file = f.name
            for i in range(1, 11):
                f.write(f"Line {i}\n")

        try:
            # Test single range
            result = extract_lines_by_ranges(test_file, [(3, 5)])

            # Should extract lines 3-5
            assert result == "Line 3\nLine 4\nLine 5\n"
        finally:
            os.unlink(test_file)

    def test_extract_lines_by_ranges_multiple_ranges(self):
        """Test range extraction with multiple ranges"""
        # Create test file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.cbl') as f:
            test_file = f.name
            for i in range(1, 11):
                f.write(f"Line {i}\n")

        try:
            # Test multiple ranges
            result = extract_lines_by_ranges(test_file, [(1, 2), (5, 6), (9, 10)])

            # Should extract lines 1-2, 5-6, 9-10
            expected = "Line 1\nLine 2\nLine 5\nLine 6\nLine 9\nLine 10\n"
            assert result == expected
        finally:
            os.unlink(test_file)

    def test_extract_lines_with_context(self):
        """Test line extraction with surrounding context"""
        # Create test file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.cbl') as f:
            test_file = f.name
            for i in range(1, 11):
                f.write(f"Line {i}\n")

        try:
            # Test extraction of line 5 with 2 lines of context before and after
            result = extract_lines_with_context(test_file, 5, 5, context_before=2, context_after=2)

            # Should extract lines 3-7 (line 5 with 2 lines before and after)
            expected = "Line 3\nLine 4\nLine 5\nLine 6\nLine 7\n"
            assert result == expected
        finally:
            os.unlink(test_file)


class TestValidation:
    """Test validation of extraction parameters"""

    def test_extract_lines_invalid_range_negative_start(self):
        """Test extraction with negative start line"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.cbl') as f:
            test_file = f.name
            f.write("Line 1\n")

        try:
            with pytest.raises(ValueError, match="Line numbers must be positive"):
                extract_lines(test_file, -1, 10)
        finally:
            os.unlink(test_file)

    def test_extract_lines_invalid_range_zero_start(self):
        """Test extraction with zero start line"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.cbl') as f:
            test_file = f.name
            f.write("Line 1\n")

        try:
            with pytest.raises(ValueError, match="Line numbers must be positive"):
                extract_lines(test_file, 0, 10)
        finally:
            os.unlink(test_file)

    def test_extract_lines_file_not_found(self):
        """Test extraction with non-existent file"""
        with pytest.raises(FileNotFoundError):
            extract_lines("/nonexistent/path/to/file.cbl", 1, 10)

    def test_extract_lines_end_before_start(self):
        """Test extraction with end < start"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.cbl') as f:
            test_file = f.name
            f.write("Line 1\n")
            f.write("Line 2\n")

        try:
            with pytest.raises(ValueError, match="End line must be >= start line"):
                extract_lines(test_file, 10, 5)
        finally:
            os.unlink(test_file)


class TestDeduplication:
    """Test source code deduplication functionality"""

    def test_compute_source_hash(self):
        """Test that source code hashing is deterministic"""
        source1 = "Line 1\nLine 2\nLine 3\n"
        source2 = "Line 1\nLine 2\nLine 3\n"
        source3 = "Different content\n"

        # Same content should produce same hash
        hash1 = compute_source_hash(source1)
        hash2 = compute_source_hash(source2)
        assert hash1 == hash2

        # Different content should produce different hash
        hash3 = compute_source_hash(source3)
        assert hash1 != hash3

        # Hash should be SHA256 format (64 hex characters)
        assert len(hash1) == 64
        assert all(c in '0123456789abcdef' for c in hash1)

    def test_deduplicate_source_extracts(self):
        """Test deduplication of source code extracts"""
        extracts = [
            {'name': 'PARA-001', 'source': 'MOVE A TO B.\n'},
            {'name': 'PARA-002', 'source': 'DISPLAY "Hello".\n'},
            {'name': 'PARA-003', 'source': 'MOVE A TO B.\n'},  # Duplicate of PARA-001
            {'name': 'PARA-004', 'source': 'ADD 1 TO COUNTER.\n'},
            {'name': 'PARA-005', 'source': 'DISPLAY "Hello".\n'},  # Duplicate of PARA-002
        ]

        result = deduplicate_source_extracts(extracts)

        # Should have 3 unique extracts
        assert len(result) == 3

        # Check that we kept the first occurrence of each
        names = [e['name'] for e in result]
        assert 'PARA-001' in names
        assert 'PARA-002' in names
        assert 'PARA-004' in names
        assert 'PARA-003' not in names  # Duplicate removed
        assert 'PARA-005' not in names  # Duplicate removed

    def test_deduplicate_empty_list(self):
        """Test deduplication with empty list"""
        result = deduplicate_source_extracts([])
        assert result == []

    def test_deduplicate_empty_source(self):
        """Test deduplication with empty source strings"""
        extracts = [
            {'name': 'PARA-001', 'source': ''},
            {'name': 'PARA-002', 'source': ''},
            {'name': 'PARA-003', 'source': 'MOVE A TO B.\n'},
        ]

        result = deduplicate_source_extracts(extracts)

        # Empty sources have same hash, only first should be kept
        assert len(result) == 2
        names = [e['name'] for e in result]
        assert 'PARA-001' in names
        assert 'PARA-003' in names
        assert 'PARA-002' not in names

    def test_deduplicate_all_identical(self):
        """Test deduplication when all sources are identical"""
        extracts = [
            {'name': 'PARA-001', 'source': 'MOVE A TO B.\n'},
            {'name': 'PARA-002', 'source': 'MOVE A TO B.\n'},
            {'name': 'PARA-003', 'source': 'MOVE A TO B.\n'},
        ]

        result = deduplicate_source_extracts(extracts)

        # Should keep only the first one
        assert len(result) == 1
        assert result[0]['name'] == 'PARA-001'


class TestDivisionExtraction:
    """Test COBOL division extraction functionality"""

    def test_find_division_boundaries(self, test_cobol_file):
        """Test finding division boundaries in COBOL file"""
        boundaries = find_division_boundaries(test_cobol_file)

        # Should find all 4 divisions
        assert 'IDENTIFICATION DIVISION' in boundaries
        assert 'ENVIRONMENT DIVISION' in boundaries
        assert 'DATA DIVISION' in boundaries
        assert 'PROCEDURE DIVISION' in boundaries

        # Check line numbers are correct
        assert boundaries['IDENTIFICATION DIVISION']['start'] == 1
        assert boundaries['ENVIRONMENT DIVISION']['start'] == 5
        assert boundaries['DATA DIVISION']['start'] == 9
        assert boundaries['PROCEDURE DIVISION']['start'] == 14
