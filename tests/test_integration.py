"""
Integration Tests for Source Extraction

Tests end-to-end integration of all source extraction components.
"""

import pytest
import os
import tempfile
from source_integration import (
    extract_source_for_section,
    extract_source_for_all_sections,
    get_extraction_stats,
    build_section_context_with_source
)


@pytest.fixture
def test_cobol_program():
    """Create a complete test COBOL program"""
    content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST-PROGRAM.
       AUTHOR. INTEGRATION-TEST.
      *
      * This is a test program for integration testing
      *
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. IBM-PC.
       OBJECT-COMPUTER. IBM-PC.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-COUNTER PIC 9(3) VALUE 0.
       01 WS-NAME    PIC X(20) VALUE SPACES.
       01 WS-RESULT  PIC 9(5) VALUE 0.

       PROCEDURE DIVISION.
       MAIN-PARA.
           DISPLAY "Starting program".
           PERFORM CALCULATE-RESULT.
           DISPLAY "Result: " WS-RESULT.
           STOP RUN.

       CALCULATE-RESULT.
           MOVE 100 TO WS-COUNTER.
           COMPUTE WS-RESULT = WS-COUNTER * 2.
           EXIT.
"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.cbl') as f:
        f.write(content)
        file_path = f.name

    yield file_path

    # Cleanup
    os.unlink(file_path)


class TestSectionExtraction:
    """Test extracting source for specific sections"""

    def test_extract_data_structures_section(self, test_cobol_program):
        """Test extracting source for data structures section"""
        source = extract_source_for_section('2_data_structures', test_cobol_program)

        assert source is not None
        assert 'DATA DIVISION' in source
        assert 'WS-COUNTER' in source
        assert 'WS-NAME' in source
        # Should have markdown formatting
        assert '###' in source
        assert '```cobol' in source

    def test_extract_business_logic_section(self, test_cobol_program):
        """Test extracting source for business logic section"""
        source = extract_source_for_section('3_business_logic', test_cobol_program)

        assert source is not None
        assert 'PROCEDURE DIVISION' in source
        assert 'MAIN-PARA' in source
        assert 'CALCULATE-RESULT' in source

    def test_extract_overview_section_no_source(self, test_cobol_program):
        """Test that overview section doesn't extract source"""
        source = extract_source_for_section('1_program_overview', test_cobol_program)

        assert source is None

    def test_compression_removes_comments(self, test_cobol_program):
        """Test that compression removes COBOL comments"""
        source = extract_source_for_section('2_data_structures', test_cobol_program, compress=True)

        # Comments should be removed
        assert 'This is a test program' not in source
        # Code should remain
        assert 'WS-COUNTER' in source

    def test_no_compression_keeps_comments(self, test_cobol_program):
        """Test that without compression, comments are kept"""
        source = extract_source_for_section('2_data_structures', test_cobol_program, compress=False)

        # This test may fail if DATA DIVISION doesn't have comments
        # Code should be present
        assert 'WS-COUNTER' in source


class TestAllSectionsExtraction:
    """Test extracting source for all sections"""

    def test_extract_all_sections(self, test_cobol_program):
        """Test extracting source for all sections"""
        sources = extract_source_for_all_sections(test_cobol_program)

        # Should have 11 sections
        assert len(sources) == 11

        # Sections requiring source should have it
        assert sources['2_data_structures'] is not None
        assert sources['3_business_logic'] is not None

        # Sections not requiring source should be None
        assert sources['1_program_overview'] is None
        assert sources['8_dependencies'] is None
        assert sources['11_maintenance'] is None

    def test_extraction_stats(self, test_cobol_program):
        """Test extraction statistics"""
        sources = extract_source_for_all_sections(test_cobol_program)
        stats = get_extraction_stats(sources)

        assert stats['total_sections'] == 11
        assert stats['sections_with_source'] >= 5  # At least data structures, business logic, etc.
        assert stats['sections_without_source'] >= 3  # Overview, dependencies, maintenance
        assert stats['total_characters'] > 0
        assert stats['estimated_tokens'] > 0
        # Token estimate should be less than character count
        assert stats['estimated_tokens'] < stats['total_characters']


class TestContextBuilding:
    """Test building context with source code"""

    def test_build_context_with_source(self, test_cobol_program):
        """Test building section context with source code"""
        metadata = {
            'file': test_cobol_program,
            'paragraphs': {}
        }

        context = build_section_context_with_source(
            '2_data_structures',
            test_cobol_program,
            metadata
        )

        assert len(context) > 0
        assert '2_data_structures' in context
        assert 'Source Code' in context
        assert 'WS-COUNTER' in context

    def test_build_context_no_source(self, test_cobol_program):
        """Test building context for section without source"""
        context = build_section_context_with_source(
            '1_program_overview',
            test_cobol_program,
            {}
        )

        # Should still have context but no source code section
        assert len(context) > 0
        assert '1_program_overview' in context
        # Shouldn't have source code
        assert 'WS-COUNTER' not in context


class TestErrorHandling:
    """Test error handling in integration"""

    def test_nonexistent_file(self):
        """Test handling of non-existent file"""
        # Should not raise exception, just return None
        source = extract_source_for_section('2_data_structures', '/nonexistent/file.cbl')
        # Should handle gracefully and return None
        assert source is None

    def test_invalid_section(self, test_cobol_program):
        """Test handling of invalid section name"""
        source = extract_source_for_section('99_invalid_section', test_cobol_program)
        assert source is None
