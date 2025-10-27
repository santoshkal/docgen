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
