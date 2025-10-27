"""
Test suite for section_requirements.py

Tests section requirements configuration and helper functions.
"""

import pytest
from section_requirements import (
    SECTION_REQUIREMENTS,
    get_section_requirements,
    should_extract_source
)


class TestSectionRequirements:
    """Test section requirements configuration"""

    def test_all_sections_defined(self):
        """Test that all 11 sections have requirements"""
        expected_sections = [
            '1_program_overview',
            '2_data_structures',
            '3_business_logic',
            '4_file_operations',
            '5_database_operations',
            '6_technical_details',
            '7_error_handling',
            '8_dependencies',
            '9_performance',
            '10_security',
            '11_maintenance'
        ]

        for section in expected_sections:
            assert section in SECTION_REQUIREMENTS, f"Missing section: {section}"

    def test_section_structure(self):
        """Test that each section has required fields"""
        for section_name, config in SECTION_REQUIREMENTS.items():
            assert 'extract_source' in config
            assert 'divisions' in config
            assert isinstance(config['extract_source'], bool)
            assert isinstance(config['divisions'], list)

    def test_data_structures_section(self):
        """Test data structures section requires source extraction"""
        section = SECTION_REQUIREMENTS['2_data_structures']

        assert section['extract_source'] is True
        assert 'DATA DIVISION' in section['divisions']

    def test_business_logic_section(self):
        """Test business logic section requires source extraction"""
        section = SECTION_REQUIREMENTS['3_business_logic']

        assert section['extract_source'] is True
        assert 'PROCEDURE DIVISION' in section['divisions']


class TestHelperFunctions:
    """Test section requirements helper functions"""

    def test_get_section_requirements_valid(self):
        """Test getting requirements for valid section"""
        req = get_section_requirements('2_data_structures')

        assert req is not None
        assert req['extract_source'] is True
        assert 'DATA DIVISION' in req['divisions']

    def test_get_section_requirements_invalid(self):
        """Test getting requirements for invalid section"""
        req = get_section_requirements('nonexistent_section')

        assert req is None

    def test_should_extract_source_true(self):
        """Test should_extract_source returns True when needed"""
        assert should_extract_source('2_data_structures') is True
        assert should_extract_source('3_business_logic') is True

    def test_should_extract_source_false(self):
        """Test should_extract_source returns False when not needed"""
        # Program overview doesn't need source extraction
        assert should_extract_source('1_program_overview') is False

    def test_should_extract_source_invalid(self):
        """Test should_extract_source with invalid section"""
        assert should_extract_source('nonexistent_section') is False

    def test_get_divisions_for_section(self):
        """Test getting divisions for a section"""
        from section_requirements import get_divisions_for_section

        divisions = get_divisions_for_section('2_data_structures')
        assert divisions == ['DATA DIVISION']

        divisions = get_divisions_for_section('3_business_logic')
        assert divisions == ['PROCEDURE DIVISION']
