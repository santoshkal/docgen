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
    find_division_boundaries,
    extract_division,
    extract_paragraph,
    extract_paragraphs_by_names,
    compress_source_code,
    estimate_token_count,
    add_section_markers
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


@pytest.fixture
def test_paragraph_metadata():
    """Metadata for paragraphs in test COBOL file"""
    return {
        'MAIN-PARA': {'start': 15, 'end': 18},
        'SUB-PARA': {'start': 16, 'end': 17},  # Subset of MAIN-PARA for testing
        'ANOTHER-PARA': {'start': 18, 'end': 18}
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

    def test_extract_data_division(self, test_cobol_file):
        """Test extracting DATA DIVISION"""
        source = extract_division(test_cobol_file, 'DATA DIVISION')

        assert source is not None
        assert 'DATA DIVISION' in source
        assert 'WORKING-STORAGE SECTION' in source
        assert 'WS-COUNTER' in source

    def test_extract_procedure_division(self, test_cobol_file):
        """Test extracting PROCEDURE DIVISION"""
        source = extract_division(test_cobol_file, 'PROCEDURE DIVISION')

        assert source is not None
        assert 'PROCEDURE DIVISION' in source
        assert 'MAIN-PARA' in source
        assert 'STOP RUN' in source

    def test_extract_identification_division(self, test_cobol_file):
        """Test extracting IDENTIFICATION DIVISION"""
        source = extract_division(test_cobol_file, 'IDENTIFICATION DIVISION')

        assert source is not None
        assert 'IDENTIFICATION DIVISION' in source
        assert 'PROGRAM-ID' in source

    def test_extract_environment_division(self, test_cobol_file):
        """Test extracting ENVIRONMENT DIVISION"""
        source = extract_division(test_cobol_file, 'ENVIRONMENT DIVISION')

        assert source is not None
        assert 'ENVIRONMENT DIVISION' in source
        assert 'CONFIGURATION SECTION' in source

    def test_extract_division_not_found(self, test_cobol_file):
        """Test extracting a non-existent division"""
        source = extract_division(test_cobol_file, 'NONEXISTENT DIVISION')

        assert source is None


class TestParagraphExtraction:
    """Test COBOL paragraph extraction functionality"""

    def test_extract_paragraph_by_name(self, test_cobol_file, test_paragraph_metadata):
        """Test extracting a single paragraph by name"""
        source = extract_paragraph(
            test_cobol_file,
            'MAIN-PARA',
            test_paragraph_metadata
        )

        assert source is not None
        assert 'MAIN-PARA' in source
        assert 'MOVE 100' in source
        assert 'STOP RUN' in source

    def test_extract_paragraph_not_found(self, test_cobol_file, test_paragraph_metadata):
        """Test extracting a non-existent paragraph"""
        source = extract_paragraph(
            test_cobol_file,
            'NONEXISTENT-PARA',
            test_paragraph_metadata
        )

        assert source is None

    def test_extract_paragraphs_by_names(self, test_cobol_file, test_paragraph_metadata):
        """Test extracting multiple paragraphs by names"""
        extracts = extract_paragraphs_by_names(
            test_cobol_file,
            ['MAIN-PARA', 'SUB-PARA'],
            test_paragraph_metadata
        )

        assert len(extracts) == 2
        assert extracts[0]['name'] == 'MAIN-PARA'
        assert extracts[1]['name'] == 'SUB-PARA'
        assert 'MAIN-PARA' in extracts[0]['source']
        assert 'MOVE 100' in extracts[1]['source']

    def test_extract_paragraphs_with_missing(self, test_cobol_file, test_paragraph_metadata):
        """Test extracting paragraphs when some don't exist"""
        extracts = extract_paragraphs_by_names(
            test_cobol_file,
            ['MAIN-PARA', 'NONEXISTENT-PARA', 'SUB-PARA'],
            test_paragraph_metadata
        )

        # Should only return the found paragraphs
        assert len(extracts) == 2
        names = [e['name'] for e in extracts]
        assert 'MAIN-PARA' in names
        assert 'SUB-PARA' in names
        assert 'NONEXISTENT-PARA' not in names


class TestOptimizationFunctions:
    """Test source code optimization and helper functions"""

    def test_compress_source_code(self):
        """Test source code compression (remove comments and blank lines)"""
        source = """      * This is a comment
       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST.
      * Another comment

       DATA DIVISION.

       WORKING-STORAGE SECTION.
       01 WS-VAR PIC X(10).
"""
        compressed = compress_source_code(source)

        # Should remove comment lines and blank lines
        assert '* This is a comment' not in compressed
        assert '* Another comment' not in compressed
        # Should keep actual code
        assert 'IDENTIFICATION DIVISION' in compressed
        assert 'DATA DIVISION' in compressed
        assert 'WS-VAR' in compressed
        # Should have fewer lines
        assert compressed.count('\n') < source.count('\n')

    def test_compress_preserves_code(self):
        """Test that compression doesn't remove actual code"""
        source = """       MOVE A TO B.
       DISPLAY "Hello".
       STOP RUN."""
        compressed = compress_source_code(source)

        # All code should be preserved
        assert 'MOVE A TO B' in compressed
        assert 'DISPLAY "Hello"' in compressed
        assert 'STOP RUN' in compressed

    def test_estimate_token_count(self):
        """Test token count estimation"""
        source = "       MOVE A TO B.\n       DISPLAY 'Hello World'.\n"

        count = estimate_token_count(source)

        # Should return reasonable estimate (roughly 1 token per 4 chars)
        assert count > 0
        assert count < len(source)  # Should be less than character count
        assert isinstance(count, int)

    def test_add_section_markers(self):
        """Test adding markdown section markers"""
        sections = [
            {'name': 'DATA DIVISION', 'source': '01 WS-VAR PIC X.'},
            {'name': 'PROCEDURE DIVISION', 'source': 'MOVE A TO B.'}
        ]

        marked = add_section_markers(sections)

        # Should have markdown headers
        assert '### DATA DIVISION' in marked
        assert '### PROCEDURE DIVISION' in marked
        # Should have code blocks
        assert '```cobol' in marked
        assert '01 WS-VAR PIC X.' in marked
        assert 'MOVE A TO B.' in marked

    def test_add_section_markers_empty(self):
        """Test adding markers to empty list"""
        marked = add_section_markers([])
        assert marked == ""
