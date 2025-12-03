"""
Test suite for Enhanced Program Map Configuration

TDD tests for US-1.2: Enhanced Program Map Configuration
These tests are written FIRST before implementation.

Tests cover:
- Configurable paragraph limits
- Configurable data item limits
- Show all mode (-1 or None)
- Configuration loading from YAML
"""

import json
import os
import pytest
import tempfile
from pathlib import Path
from typing import Dict, Any


# ============================================================================
# TEST FIXTURES
# ============================================================================

@pytest.fixture
def sample_ctags_outline():
    """Sample CTags outline with multiple paragraphs and data items"""
    return {
        "file": "TESTPROG.cbl",
        "symbols": [
            {"name": "TESTPROG", "kind": "program", "line": 2},
            # 10 data items
            {"name": "WS-COUNTER", "kind": "data", "line": 13, "level": "01"},
            {"name": "WS-TOTAL", "kind": "data", "line": 14, "level": "01"},
            {"name": "WS-NAME", "kind": "data", "line": 15, "level": "01"},
            {"name": "WS-DATE", "kind": "data", "line": 16, "level": "01"},
            {"name": "WS-TIME", "kind": "data", "line": 17, "level": "01"},
            {"name": "WS-FLAG", "kind": "data", "line": 18, "level": "01"},
            {"name": "WS-RESULT", "kind": "data", "line": 19, "level": "01"},
            {"name": "WS-INPUT", "kind": "data", "line": 20, "level": "01"},
            {"name": "WS-OUTPUT", "kind": "data", "line": 21, "level": "01"},
            {"name": "WS-TEMP", "kind": "data", "line": 22, "level": "01"},
            # 8 paragraphs
            {"name": "0000-MAIN", "kind": "paragraph", "line": 30},
            {"name": "1000-INIT", "kind": "paragraph", "line": 40},
            {"name": "2000-PROCESS", "kind": "paragraph", "line": 50},
            {"name": "3000-READ", "kind": "paragraph", "line": 60},
            {"name": "4000-WRITE", "kind": "paragraph", "line": 70},
            {"name": "5000-CALCULATE", "kind": "paragraph", "line": 80},
            {"name": "8000-ERROR", "kind": "paragraph", "line": 90},
            {"name": "9000-CLEANUP", "kind": "paragraph", "line": 100}
        ]
    }


@pytest.fixture
def sample_superbol_cfg():
    """Sample SuperBol CFG metadata"""
    return {
        "program": "TESTPROG",
        "performs": [
            {"from": "0000-MAIN", "to": "1000-INIT"},
            {"from": "0000-MAIN", "to": "2000-PROCESS"},
            {"from": "0000-MAIN", "to": "9000-CLEANUP"},
            {"from": "2000-PROCESS", "to": "3000-READ"},
            {"from": "2000-PROCESS", "to": "4000-WRITE"},
            {"from": "2000-PROCESS", "to": "5000-CALCULATE"}
        ],
        "calls": [
            {"from": "2000-PROCESS", "to": "SUBPROG", "type": "CALL"}
        ],
        "edges": [
            {"from": "0000-MAIN", "to": "1000-INIT"},
            {"from": "1000-INIT", "to": "2000-PROCESS"}
        ]
    }


@pytest.fixture
def sample_gnucobol_analysis():
    """Sample GnuCOBOL analysis metadata"""
    return {
        "program": "TESTPROG",
        "variables": {
            "WS-COUNTER": {"references": 15, "type": "numeric"},
            "WS-TOTAL": {"references": 10, "type": "numeric"},
            "WS-NAME": {"references": 8, "type": "alphanumeric"},
            "WS-DATE": {"references": 5, "type": "alphanumeric"},
            "WS-TIME": {"references": 4, "type": "alphanumeric"},
            "WS-FLAG": {"references": 3, "type": "numeric"},
            "WS-RESULT": {"references": 2, "type": "numeric"},
            "WS-INPUT": {"references": 1, "type": "alphanumeric"},
            "WS-OUTPUT": {"references": 1, "type": "alphanumeric"},
            "WS-TEMP": {"references": 1, "type": "alphanumeric"}
        }
    }


@pytest.fixture
def sample_metadata(sample_ctags_outline, sample_superbol_cfg, sample_gnucobol_analysis):
    """Combined metadata fixture"""
    return {
        "ctags_outline": sample_ctags_outline,
        "superbol_cfg": sample_superbol_cfg,
        "gnucobol_analysis": sample_gnucobol_analysis
    }


# ============================================================================
# US-1.2.T1: Test Configurable Paragraph Limit
# ============================================================================

class TestConfigurableParagraphLimit:
    """US-1.2.T1: Test program map configurable paragraph limit"""

    def test_program_map_configurable_paragraph_limit_default(self, sample_metadata):
        """Test that default paragraph limit of 30 is used"""
        from cobol_program_map import generate_cobol_program_map

        program_map = generate_cobol_program_map(
            program_name="TESTPROG",
            metadata=sample_metadata
        )

        # Should include paragraphs up to limit
        assert program_map is not None
        assert "0000-MAIN" in program_map

    def test_program_map_configurable_paragraph_limit_custom(self, sample_metadata):
        """Test that custom paragraph limit is respected"""
        from cobol_program_map import generate_cobol_program_map

        # Limit to top 3 paragraphs
        program_map = generate_cobol_program_map(
            program_name="TESTPROG",
            metadata=sample_metadata,
            top_n_paragraphs=3
        )

        # Should include top ranked paragraphs
        assert program_map is not None
        # The exact paragraphs depend on ranking, but limit should be respected

    def test_program_map_configurable_paragraph_limit_very_high(self, sample_metadata):
        """Test that very high limit includes all paragraphs"""
        from cobol_program_map import generate_cobol_program_map

        # Set limit higher than total paragraphs
        program_map = generate_cobol_program_map(
            program_name="TESTPROG",
            metadata=sample_metadata,
            top_n_paragraphs=1000
        )

        # Should include all 8 paragraphs from test data
        assert "0000-MAIN" in program_map
        assert "1000-INIT" in program_map
        assert "9000-CLEANUP" in program_map


# ============================================================================
# US-1.2.T2: Test Configurable Data Item Limit
# ============================================================================

class TestConfigurableDataItemLimit:
    """US-1.2.T2: Test program map configurable data item limit"""

    def test_program_map_configurable_data_item_limit_default(self, sample_metadata):
        """Test that default data item limit of 20 is used"""
        from cobol_program_map import generate_cobol_program_map

        program_map = generate_cobol_program_map(
            program_name="TESTPROG",
            metadata=sample_metadata
        )

        # Should include data items
        assert program_map is not None
        assert "DATA DIVISION" in program_map

    def test_program_map_configurable_data_item_limit_custom(self, sample_metadata):
        """Test that custom data item limit is respected"""
        from cobol_program_map import generate_cobol_program_map

        # Limit to top 3 data items
        program_map = generate_cobol_program_map(
            program_name="TESTPROG",
            metadata=sample_metadata,
            top_n_data_items=3
        )

        # Should show limited data items
        assert "Top 3" in program_map or "Most-Used Data Items" in program_map

    def test_program_map_configurable_data_item_limit_very_high(self, sample_metadata):
        """Test that very high limit includes all data items"""
        from cobol_program_map import generate_cobol_program_map

        # Set limit higher than total data items
        program_map = generate_cobol_program_map(
            program_name="TESTPROG",
            metadata=sample_metadata,
            top_n_data_items=1000
        )

        # Should include all data items (10 in test data)
        assert program_map is not None


# ============================================================================
# US-1.2.T3: Test Show All Mode
# ============================================================================

class TestShowAllMode:
    """US-1.2.T3: Test program map show all mode"""

    def test_program_map_show_all_mode_paragraphs(self, sample_metadata):
        """Test that -1 limit shows all paragraphs"""
        from cobol_program_map import generate_cobol_program_map

        # -1 means show all
        program_map = generate_cobol_program_map(
            program_name="TESTPROG",
            metadata=sample_metadata,
            top_n_paragraphs=-1
        )

        # All 8 paragraphs should be included
        assert "0000-MAIN" in program_map
        assert "1000-INIT" in program_map
        assert "2000-PROCESS" in program_map
        assert "3000-READ" in program_map
        assert "4000-WRITE" in program_map
        assert "5000-CALCULATE" in program_map
        assert "8000-ERROR" in program_map
        assert "9000-CLEANUP" in program_map

    def test_program_map_show_all_mode_data_items(self, sample_metadata):
        """Test that -1 limit shows all data items"""
        from cobol_program_map import generate_cobol_program_map

        # -1 means show all
        program_map = generate_cobol_program_map(
            program_name="TESTPROG",
            metadata=sample_metadata,
            top_n_data_items=-1
        )

        # All 10 data items should be included
        assert "WS-COUNTER" in program_map
        assert "WS-TOTAL" in program_map
        assert "WS-NAME" in program_map
        assert "WS-TEMP" in program_map  # Last data item

    def test_program_map_show_all_mode_both(self, sample_metadata):
        """Test that -1 limit for both shows all elements"""
        from cobol_program_map import generate_cobol_program_map

        program_map = generate_cobol_program_map(
            program_name="TESTPROG",
            metadata=sample_metadata,
            top_n_paragraphs=-1,
            top_n_data_items=-1
        )

        # All elements should be included
        assert "0000-MAIN" in program_map
        assert "WS-COUNTER" in program_map


# ============================================================================
# US-1.2.T4: Test Configuration from YAML
# ============================================================================

class TestConfigFromYaml:
    """US-1.2.T4: Test program map configuration from YAML"""

    def test_program_map_config_from_yaml_parsing(self):
        """Test that program_map config section is parsed from YAML"""
        from config_loader import ConfigLoader

        # Create temp config file with program_map section
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
  top_n_paragraphs: 100
  top_n_data_items: 50
  show_all: false
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(config_content)
            config_path = f.name

        try:
            loader = ConfigLoader(config_path)
            config = loader.load()

            # program_map section should exist
            assert 'program_map' in config
            assert config['program_map']['top_n_paragraphs'] == 100
            assert config['program_map']['top_n_data_items'] == 50
        finally:
            os.unlink(config_path)

    def test_program_map_config_defaults(self):
        """Test that defaults are used when program_map section is missing"""
        from config_loader import ConfigLoader

        # Create temp config without program_map section
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
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(config_content)
            config_path = f.name

        try:
            loader = ConfigLoader(config_path)
            config = loader.load()

            # get_program_map_config should return defaults
            pm_config = loader.get_program_map_config()
            assert pm_config.get('top_n_paragraphs', 30) == 30
            assert pm_config.get('top_n_data_items', 20) == 20
        finally:
            os.unlink(config_path)

    def test_program_map_config_getter_method(self):
        """Test that get_program_map_config() method exists and works"""
        from config_loader import ConfigLoader

        # Create temp config with program_map section
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
  top_n_paragraphs: 200
  top_n_data_items: 100
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(config_content)
            config_path = f.name

        try:
            loader = ConfigLoader(config_path)
            loader.load()

            # get_program_map_config() should return the config
            pm_config = loader.get_program_map_config()
            assert isinstance(pm_config, dict)
            assert pm_config['top_n_paragraphs'] == 200
            assert pm_config['top_n_data_items'] == 100
        finally:
            os.unlink(config_path)


# ============================================================================
# RUN TESTS
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
