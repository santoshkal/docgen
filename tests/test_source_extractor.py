"""
Test suite for source_extractor.py

Following TDD approach: Tests written FIRST, then implementation.
"""

import pytest
import os
import tempfile
from source_extractor import extract_lines


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
