"""
Test suite for Dynamic Program Map Limits Based on Program Size

TDD tests for US-1.3: Dynamic Program Map Limits Based on Program Size
These tests are written FIRST before implementation.

Tests cover:
- Small programs (< 100 paragraphs): Show all
- Medium programs (100-500 paragraphs): Top 200 paragraphs, top 100 data items
- Large programs (500+ paragraphs): Top 300 paragraphs, top 150 data items
- Configurable size thresholds
- Automatic size detection from metadata
"""

import os
import pytest
import tempfile
from typing import Dict, Any, List


# ============================================================================
# TEST FIXTURES
# ============================================================================

@pytest.fixture
def small_program_metadata():
    """Small program: 50 paragraphs, 30 data items"""
    return _create_metadata(num_paragraphs=50, num_data_items=30)


@pytest.fixture
def medium_program_metadata():
    """Medium program: 250 paragraphs, 150 data items"""
    return _create_metadata(num_paragraphs=250, num_data_items=150)


@pytest.fixture
def large_program_metadata():
    """Large program: 800 paragraphs, 500 data items"""
    return _create_metadata(num_paragraphs=800, num_data_items=500)


@pytest.fixture
def boundary_small_metadata():
    """Boundary case: 99 paragraphs (just under small threshold)"""
    return _create_metadata(num_paragraphs=99, num_data_items=60)


@pytest.fixture
def boundary_medium_metadata():
    """Boundary case: 100 paragraphs (exactly at medium threshold)"""
    return _create_metadata(num_paragraphs=100, num_data_items=70)


@pytest.fixture
def boundary_large_metadata():
    """Boundary case: 500 paragraphs (exactly at large threshold)"""
    return _create_metadata(num_paragraphs=500, num_data_items=300)


def _create_metadata(num_paragraphs: int, num_data_items: int) -> Dict[str, Any]:
    """Helper to create metadata with specified counts"""
    symbols = []

    # Add program symbol
    symbols.append({"name": "TESTPROG", "kind": "program", "line": 1})

    # Add paragraphs
    for i in range(num_paragraphs):
        symbols.append({
            "name": f"PARA-{i:04d}",
            "kind": "paragraph",
            "line": 100 + i * 10
        })

    # Add data items
    for i in range(num_data_items):
        symbols.append({
            "name": f"WS-DATA-{i:04d}",
            "kind": "data",
            "level": "01",
            "line": 10 + i
        })

    # Create performs for importance ranking
    performs = []
    for i in range(min(50, num_paragraphs - 1)):
        performs.append({
            "from": f"PARA-{i:04d}",
            "to": f"PARA-{i+1:04d}"
        })

    # Create variable references
    variables = {}
    for i in range(num_data_items):
        variables[f"WS-DATA-{i:04d}"] = {
            "references": max(1, num_data_items - i),
            "type": "alphanumeric"
        }

    return {
        "ctags_outline": {
            "file": "TESTPROG.cbl",
            "symbols": symbols
        },
        "superbol_cfg": {
            "program": "TESTPROG",
            "performs": performs,
            "calls": [],
            "edges": []
        },
        "gnucobol_analysis": {
            "program": "TESTPROG",
            "variables": variables
        }
    }


# ============================================================================
# US-1.3.T1: Test Small Program Shows All
# ============================================================================

class TestDynamicLimitsSmallProgram:
    """US-1.3.T1: Test that small programs show all elements"""

    def test_dynamic_limits_small_program_shows_all_paragraphs(self, small_program_metadata):
        """Small programs (< 100 paragraphs) should show all paragraphs"""
        from dynamic_program_limits import get_dynamic_limits, ProgramSizeCategory

        limits = get_dynamic_limits(small_program_metadata)

        # Small program should show all (-1)
        assert limits['top_n_paragraphs'] == -1, "Small program should show all paragraphs"

    def test_dynamic_limits_small_program_shows_all_data_items(self, small_program_metadata):
        """Small programs should show all data items"""
        from dynamic_program_limits import get_dynamic_limits

        limits = get_dynamic_limits(small_program_metadata)

        # Small program should show all (-1)
        assert limits['top_n_data_items'] == -1, "Small program should show all data items"

    def test_dynamic_limits_small_program_category(self, small_program_metadata):
        """Small programs should be categorized as SMALL"""
        from dynamic_program_limits import detect_program_size, ProgramSizeCategory

        category = detect_program_size(small_program_metadata)

        assert category == ProgramSizeCategory.SMALL

    def test_dynamic_limits_boundary_99_paragraphs_is_small(self, boundary_small_metadata):
        """99 paragraphs should be categorized as SMALL"""
        from dynamic_program_limits import detect_program_size, ProgramSizeCategory

        category = detect_program_size(boundary_small_metadata)

        assert category == ProgramSizeCategory.SMALL


# ============================================================================
# US-1.3.T2: Test Medium Program Top 200
# ============================================================================

class TestDynamicLimitsMediumProgram:
    """US-1.3.T2: Test that medium programs show top 200 paragraphs"""

    def test_dynamic_limits_medium_program_top_200_paragraphs(self, medium_program_metadata):
        """Medium programs (100-500 paragraphs) should show top 200 paragraphs"""
        from dynamic_program_limits import get_dynamic_limits

        limits = get_dynamic_limits(medium_program_metadata)

        assert limits['top_n_paragraphs'] == 200, "Medium program should show top 200 paragraphs"

    def test_dynamic_limits_medium_program_top_100_data_items(self, medium_program_metadata):
        """Medium programs should show top 100 data items"""
        from dynamic_program_limits import get_dynamic_limits

        limits = get_dynamic_limits(medium_program_metadata)

        assert limits['top_n_data_items'] == 100, "Medium program should show top 100 data items"

    def test_dynamic_limits_medium_program_category(self, medium_program_metadata):
        """Medium programs should be categorized as MEDIUM"""
        from dynamic_program_limits import detect_program_size, ProgramSizeCategory

        category = detect_program_size(medium_program_metadata)

        assert category == ProgramSizeCategory.MEDIUM

    def test_dynamic_limits_boundary_100_paragraphs_is_medium(self, boundary_medium_metadata):
        """100 paragraphs should be categorized as MEDIUM (boundary)"""
        from dynamic_program_limits import detect_program_size, ProgramSizeCategory

        category = detect_program_size(boundary_medium_metadata)

        assert category == ProgramSizeCategory.MEDIUM


# ============================================================================
# US-1.3.T3: Test Large Program Top 300
# ============================================================================

class TestDynamicLimitsLargeProgram:
    """US-1.3.T3: Test that large programs show top 300 paragraphs"""

    def test_dynamic_limits_large_program_top_300_paragraphs(self, large_program_metadata):
        """Large programs (500+ paragraphs) should show top 300 paragraphs"""
        from dynamic_program_limits import get_dynamic_limits

        limits = get_dynamic_limits(large_program_metadata)

        assert limits['top_n_paragraphs'] == 300, "Large program should show top 300 paragraphs"

    def test_dynamic_limits_large_program_top_150_data_items(self, large_program_metadata):
        """Large programs should show top 150 data items"""
        from dynamic_program_limits import get_dynamic_limits

        limits = get_dynamic_limits(large_program_metadata)

        assert limits['top_n_data_items'] == 150, "Large program should show top 150 data items"

    def test_dynamic_limits_large_program_category(self, large_program_metadata):
        """Large programs should be categorized as LARGE"""
        from dynamic_program_limits import detect_program_size, ProgramSizeCategory

        category = detect_program_size(large_program_metadata)

        assert category == ProgramSizeCategory.LARGE

    def test_dynamic_limits_boundary_500_paragraphs_is_large(self, boundary_large_metadata):
        """500 paragraphs should be categorized as LARGE (boundary)"""
        from dynamic_program_limits import detect_program_size, ProgramSizeCategory

        category = detect_program_size(boundary_large_metadata)

        assert category == ProgramSizeCategory.LARGE


# ============================================================================
# US-1.3.T4: Test Configurable Thresholds
# ============================================================================

class TestDynamicLimitsConfigurableThresholds:
    """US-1.3.T4: Test that size thresholds are configurable"""

    def test_dynamic_limits_custom_small_threshold(self, medium_program_metadata):
        """Custom small threshold should change categorization"""
        from dynamic_program_limits import get_dynamic_limits, detect_program_size, ProgramSizeCategory

        # With custom threshold of 300, a 250-paragraph program should be SMALL
        custom_thresholds = {
            'small_threshold': 300,
            'large_threshold': 600
        }

        category = detect_program_size(medium_program_metadata, thresholds=custom_thresholds)

        assert category == ProgramSizeCategory.SMALL

    def test_dynamic_limits_custom_large_threshold(self, medium_program_metadata):
        """Custom large threshold should change categorization"""
        from dynamic_program_limits import detect_program_size, ProgramSizeCategory

        # With custom threshold, 250 paragraphs could be LARGE if large_threshold is 200
        custom_thresholds = {
            'small_threshold': 50,
            'large_threshold': 200
        }

        category = detect_program_size(medium_program_metadata, thresholds=custom_thresholds)

        assert category == ProgramSizeCategory.LARGE

    def test_dynamic_limits_custom_limits_for_categories(self):
        """Custom limits per category should be respected"""
        from dynamic_program_limits import get_dynamic_limits, ProgramSizeCategory

        metadata = _create_metadata(num_paragraphs=250, num_data_items=150)

        custom_limits = {
            ProgramSizeCategory.SMALL: {'top_n_paragraphs': -1, 'top_n_data_items': -1},
            ProgramSizeCategory.MEDIUM: {'top_n_paragraphs': 150, 'top_n_data_items': 75},
            ProgramSizeCategory.LARGE: {'top_n_paragraphs': 250, 'top_n_data_items': 125}
        }

        limits = get_dynamic_limits(metadata, custom_limits=custom_limits)

        # 250 paragraphs = MEDIUM, should use custom MEDIUM limits
        assert limits['top_n_paragraphs'] == 150
        assert limits['top_n_data_items'] == 75

    def test_dynamic_limits_config_from_yaml(self):
        """Thresholds should be loadable from YAML config"""
        from config_loader import ConfigLoader

        config_content = """
source:
  mode: single
  program_name: TESTPROG
  source_files: ./source

output:
  metadata_dir: ./metadata
  docs_path: ./docs

llm:
  provider: anthropic
  model: claude-3-sonnet

program_map:
  top_n_paragraphs: 30
  top_n_data_items: 20
  dynamic_limits:
    enabled: true
    small_threshold: 100
    large_threshold: 500
    small:
      paragraphs: -1
      data_items: -1
    medium:
      paragraphs: 200
      data_items: 100
    large:
      paragraphs: 300
      data_items: 150
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(config_content)
            config_path = f.name

        try:
            loader = ConfigLoader(config_path)
            loader.load()

            pm_config = loader.get_program_map_config()

            assert 'dynamic_limits' in pm_config
            assert pm_config['dynamic_limits']['enabled'] == True
            assert pm_config['dynamic_limits']['small_threshold'] == 100
            assert pm_config['dynamic_limits']['large_threshold'] == 500
        finally:
            os.unlink(config_path)


# ============================================================================
# US-1.3.T5: Test Auto Size Detection
# ============================================================================

class TestDynamicLimitsAutoDetection:
    """US-1.3.T5: Test automatic size detection from metadata"""

    def test_dynamic_limits_auto_detects_from_ctags(self, medium_program_metadata):
        """Size should be automatically detected from CTags metadata"""
        from dynamic_program_limits import detect_program_size, ProgramSizeCategory

        # Should detect 250 paragraphs from CTags symbols
        category = detect_program_size(medium_program_metadata)

        assert category == ProgramSizeCategory.MEDIUM

    def test_dynamic_limits_counts_only_paragraphs_and_sections(self):
        """Size detection should only count paragraphs and sections, not data items"""
        from dynamic_program_limits import detect_program_size, ProgramSizeCategory

        # 50 paragraphs but 500 data items - should still be SMALL
        metadata = _create_metadata(num_paragraphs=50, num_data_items=500)

        category = detect_program_size(metadata)

        assert category == ProgramSizeCategory.SMALL

    def test_dynamic_limits_handles_missing_ctags(self):
        """Size detection should handle missing CTags gracefully"""
        from dynamic_program_limits import detect_program_size, ProgramSizeCategory

        # Empty metadata
        metadata = {}

        category = detect_program_size(metadata)

        # Should default to SMALL when no data available
        assert category == ProgramSizeCategory.SMALL

    def test_dynamic_limits_handles_empty_symbols(self):
        """Size detection should handle empty symbols list"""
        from dynamic_program_limits import detect_program_size, ProgramSizeCategory

        metadata = {
            "ctags_outline": {
                "file": "TESTPROG.cbl",
                "symbols": []
            }
        }

        category = detect_program_size(metadata)

        assert category == ProgramSizeCategory.SMALL

    def test_dynamic_limits_returns_correct_structure(self, medium_program_metadata):
        """get_dynamic_limits should return dict with expected keys"""
        from dynamic_program_limits import get_dynamic_limits

        limits = get_dynamic_limits(medium_program_metadata)

        assert isinstance(limits, dict)
        assert 'top_n_paragraphs' in limits
        assert 'top_n_data_items' in limits
        assert 'size_category' in limits


# ============================================================================
# RUN TESTS
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
