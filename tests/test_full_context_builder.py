"""
Test suite for Full Context Builder Module

TDD tests for US-1.1: Create Full Context Builder Class
These tests are written FIRST before implementation.

Tests cover:
- FullContextBuilder initialization
- Loading full source code with line numbers
- Loading full metadata without filtering
- Generating enhanced program map
- Building combined full context
"""

import json
import os
import pytest
import tempfile
from pathlib import Path
from typing import Dict, Any
from unittest.mock import MagicMock, patch


# Import will fail initially - that's expected in TDD
try:
    from full_context_builder import FullContextBuilder
    FULL_CONTEXT_BUILDER_AVAILABLE = True
except ImportError:
    FULL_CONTEXT_BUILDER_AVAILABLE = False
    FullContextBuilder = None


# ============================================================================
# TEST FIXTURES
# ============================================================================

@pytest.fixture
def sample_cobol_source():
    """Sample COBOL source code for testing"""
    return """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTPROG.
       AUTHOR. TEST AUTHOR.
      *****************************************************************
      * This is a test program for unit testing.
      *****************************************************************

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-COUNTER        PIC 9(4) VALUE 0.
       01 WS-TOTAL          PIC 9(8)V99 VALUE 0.
       01 WS-NAME           PIC X(50).

       PROCEDURE DIVISION.
       0000-MAIN.
           PERFORM 1000-INIT
           PERFORM 2000-PROCESS
           PERFORM 9000-CLEANUP
           STOP RUN.

       1000-INIT.
           MOVE 0 TO WS-COUNTER
           MOVE SPACES TO WS-NAME.

       2000-PROCESS.
           ADD 1 TO WS-COUNTER
           CALL 'SUBPROG' USING WS-NAME.

       9000-CLEANUP.
           DISPLAY "Done processing".
"""


@pytest.fixture
def sample_ctags_outline():
    """Sample CTags outline metadata"""
    return {
        "file": "TESTPROG.cbl",
        "symbols": [
            {"name": "TESTPROG", "kind": "program", "line": 2},
            {"name": "WS-COUNTER", "kind": "data", "line": 13, "level": "01"},
            {"name": "WS-TOTAL", "kind": "data", "line": 14, "level": "01"},
            {"name": "WS-NAME", "kind": "data", "line": 15, "level": "01"},
            {"name": "0000-MAIN", "kind": "paragraph", "line": 18},
            {"name": "1000-INIT", "kind": "paragraph", "line": 24},
            {"name": "2000-PROCESS", "kind": "paragraph", "line": 28},
            {"name": "9000-CLEANUP", "kind": "paragraph", "line": 32}
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
            {"from": "0000-MAIN", "to": "9000-CLEANUP"}
        ],
        "calls": [
            {"from": "2000-PROCESS", "to": "SUBPROG", "type": "CALL"}
        ],
        "edges": [
            {"from": "0000-MAIN", "to": "1000-INIT"},
            {"from": "1000-INIT", "to": "2000-PROCESS"},
            {"from": "2000-PROCESS", "to": "9000-CLEANUP"}
        ]
    }


@pytest.fixture
def sample_superbol_symbols():
    """Sample SuperBol document symbols"""
    return {
        "symbols": [
            {"name": "TESTPROG", "kind": 23, "range": {"start": {"line": 1}}},
            {"name": "WS-COUNTER", "kind": 13, "range": {"start": {"line": 12}}},
            {"name": "WS-TOTAL", "kind": 13, "range": {"start": {"line": 13}}},
            {"name": "WS-NAME", "kind": 13, "range": {"start": {"line": 14}}}
        ]
    }


@pytest.fixture
def sample_gnucobol_analysis():
    """Sample GnuCOBOL analysis metadata"""
    return {
        "program": "TESTPROG",
        "variables": {
            "WS-COUNTER": {"references": 3, "type": "numeric"},
            "WS-TOTAL": {"references": 1, "type": "numeric"},
            "WS-NAME": {"references": 2, "type": "alphanumeric"}
        },
        "paragraphs": {
            "0000-MAIN": {"performs": 3, "lines": 5},
            "1000-INIT": {"performs": 0, "lines": 3},
            "2000-PROCESS": {"performs": 0, "lines": 3},
            "9000-CLEANUP": {"performs": 0, "lines": 2}
        }
    }


@pytest.fixture
def temp_workspace(sample_cobol_source, sample_ctags_outline, sample_superbol_cfg,
                   sample_superbol_symbols, sample_gnucobol_analysis):
    """Create a temporary workspace with test files"""
    with tempfile.TemporaryDirectory() as tmpdir:
        workspace = Path(tmpdir)

        # Create source file
        source_dir = workspace / "source"
        source_dir.mkdir()
        source_file = source_dir / "TESTPROG.cbl"
        source_file.write_text(sample_cobol_source)

        # Create metadata directory structure
        metadata_dir = workspace / "metadata"
        metadata_dir.mkdir()

        # CTags
        ctags_dir = metadata_dir / "ctags"
        ctags_dir.mkdir()
        (ctags_dir / "ctags-TESTPROG-outline.json").write_text(
            json.dumps(sample_ctags_outline)
        )

        # SuperBol
        superbol_dir = metadata_dir / "superbol"
        superbol_dir.mkdir()
        (superbol_dir / "superbol-TESTPROG-doc-symbols.json").write_text(
            json.dumps(sample_superbol_symbols)
        )

        superbol_cfg_dir = superbol_dir / "superbol-cfg"
        superbol_cfg_dir.mkdir()
        (superbol_cfg_dir / "TESTPROG.json").write_text(
            json.dumps(sample_superbol_cfg)
        )

        # GnuCOBOL
        gnucobol_dir = metadata_dir / "gnucobol"
        gnucobol_dir.mkdir()
        (gnucobol_dir / "gnucobol-TESTPROG-analysis.json").write_text(
            json.dumps(sample_gnucobol_analysis)
        )

        yield {
            "workspace": workspace,
            "source_file": source_file,
            "metadata_dir": metadata_dir,
            "program_name": "TESTPROG"
        }


# ============================================================================
# US-1.1.T1: Test FullContextBuilder Initialization
# ============================================================================

@pytest.mark.skipif(not FULL_CONTEXT_BUILDER_AVAILABLE,
                    reason="FullContextBuilder not yet implemented")
class TestFullContextBuilderInit:
    """US-1.1.T1: Test FullContextBuilder initialization"""

    def test_full_context_builder_init_with_valid_paths(self, temp_workspace):
        """Test that FullContextBuilder initializes with valid paths"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        assert builder is not None
        assert builder.program_name == "TESTPROG"
        assert builder.source_file_path == temp_workspace["source_file"]
        assert builder.metadata_dir == temp_workspace["metadata_dir"]

    def test_full_context_builder_init_stores_paths_as_path_objects(self, temp_workspace):
        """Test that paths are stored as Path objects"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=str(temp_workspace["source_file"]),  # Pass as string
            metadata_dir=str(temp_workspace["metadata_dir"])  # Pass as string
        )

        assert isinstance(builder.source_file_path, Path)
        assert isinstance(builder.metadata_dir, Path)

    def test_full_context_builder_init_with_missing_source_file(self, temp_workspace):
        """Test that initialization handles missing source file gracefully"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=Path("/nonexistent/path/file.cbl"),
            metadata_dir=temp_workspace["metadata_dir"]
        )

        # Should initialize but source_file_exists should be False
        assert builder is not None
        assert builder.source_file_exists is False

    def test_full_context_builder_init_with_missing_metadata_dir(self, temp_workspace):
        """Test that initialization handles missing metadata dir gracefully"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=Path("/nonexistent/metadata")
        )

        # Should initialize but metadata_dir_exists should be False
        assert builder is not None
        assert builder.metadata_dir_exists is False


# ============================================================================
# US-1.1.T2: Test load_full_source_code Returns Complete File
# ============================================================================

@pytest.mark.skipif(not FULL_CONTEXT_BUILDER_AVAILABLE,
                    reason="FullContextBuilder not yet implemented")
class TestLoadFullSourceCodeComplete:
    """US-1.1.T2: Test load_full_source_code returns complete file"""

    def test_load_full_source_code_returns_complete_file(self, temp_workspace, sample_cobol_source):
        """Test that load_full_source_code returns the entire file content"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        source_code = builder.load_full_source_code()

        # Should contain all major sections
        assert "IDENTIFICATION DIVISION" in source_code
        assert "PROGRAM-ID. TESTPROG" in source_code
        assert "ENVIRONMENT DIVISION" in source_code
        assert "DATA DIVISION" in source_code
        assert "PROCEDURE DIVISION" in source_code
        assert "0000-MAIN" in source_code
        assert "9000-CLEANUP" in source_code

    def test_load_full_source_code_preserves_comments(self, temp_workspace):
        """Test that comments are preserved in source code"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        source_code = builder.load_full_source_code()

        # Comments should be preserved (asterisk comments)
        assert "This is a test program" in source_code

    def test_load_full_source_code_returns_none_for_missing_file(self, temp_workspace):
        """Test that load_full_source_code returns None for missing file"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=Path("/nonexistent/file.cbl"),
            metadata_dir=temp_workspace["metadata_dir"]
        )

        source_code = builder.load_full_source_code()

        assert source_code is None


# ============================================================================
# US-1.1.T3: Test load_full_source_code Includes Line Numbers
# ============================================================================

@pytest.mark.skipif(not FULL_CONTEXT_BUILDER_AVAILABLE,
                    reason="FullContextBuilder not yet implemented")
class TestLoadFullSourceCodeLineNumbers:
    """US-1.1.T3: Test load_full_source_code includes line numbers"""

    def test_load_full_source_code_includes_line_numbers(self, temp_workspace):
        """Test that source code includes line numbers when requested"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        source_code = builder.load_full_source_code(include_line_numbers=True)

        # Should have line numbers like "1:", "2:", etc.
        assert "1:" in source_code or "   1:" in source_code or "    1\t" in source_code

    def test_load_full_source_code_line_numbers_sequential(self, temp_workspace):
        """Test that line numbers are sequential"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        source_code = builder.load_full_source_code(include_line_numbers=True)
        lines = source_code.strip().split('\n')

        # Extract line numbers and verify they're sequential
        line_numbers = []
        for line in lines:
            # Handle format like "   1:\t..." or "1: ..." or "    1\t..."
            parts = line.split(':')[0].strip() if ':' in line else line.split('\t')[0].strip()
            if parts.isdigit():
                line_numbers.append(int(parts))

        # Should have sequential line numbers starting from 1
        assert len(line_numbers) > 0
        assert line_numbers[0] == 1
        for i in range(1, len(line_numbers)):
            assert line_numbers[i] == line_numbers[i-1] + 1

    def test_load_full_source_code_without_line_numbers(self, temp_workspace):
        """Test that source code can be loaded without line numbers"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        source_code = builder.load_full_source_code(include_line_numbers=False)

        # First line should not start with a number
        first_line = source_code.strip().split('\n')[0]
        assert not first_line.strip().split()[0].isdigit() if first_line.strip() else True


# ============================================================================
# US-1.1.T4: Test load_full_metadata No Filtering
# ============================================================================

@pytest.mark.skipif(not FULL_CONTEXT_BUILDER_AVAILABLE,
                    reason="FullContextBuilder not yet implemented")
class TestLoadFullMetadataNoFiltering:
    """US-1.1.T4: Test load_full_metadata loads without filtering"""

    def test_load_full_metadata_no_filtering(self, temp_workspace, sample_ctags_outline):
        """Test that metadata is loaded without any filtering"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        metadata = builder.load_full_metadata()

        # CTags should have all symbols
        assert "ctags_outline" in metadata
        assert len(metadata["ctags_outline"]["symbols"]) == len(sample_ctags_outline["symbols"])

    def test_load_full_metadata_includes_all_symbol_kinds(self, temp_workspace):
        """Test that all symbol kinds are included (no kind-based filtering)"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        metadata = builder.load_full_metadata()

        # Should have program, data, and paragraph symbols
        symbol_kinds = {s["kind"] for s in metadata["ctags_outline"]["symbols"]}
        assert "program" in symbol_kinds
        assert "data" in symbol_kinds
        assert "paragraph" in symbol_kinds

    def test_load_full_metadata_preserves_all_fields(self, temp_workspace):
        """Test that all metadata fields are preserved"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        metadata = builder.load_full_metadata()

        # SuperBol CFG should have all fields
        cfg = metadata["superbol_cfg"]
        assert "performs" in cfg
        assert "calls" in cfg
        assert "edges" in cfg

        # GnuCOBOL should have all fields
        gnucobol = metadata["gnucobol_analysis"]
        assert "variables" in gnucobol


# ============================================================================
# US-1.1.T5: Test load_full_metadata Loads All Sources
# ============================================================================

@pytest.mark.skipif(not FULL_CONTEXT_BUILDER_AVAILABLE,
                    reason="FullContextBuilder not yet implemented")
class TestLoadFullMetadataAllSources:
    """US-1.1.T5: Test load_full_metadata loads all metadata sources"""

    def test_load_full_metadata_loads_all_sources(self, temp_workspace):
        """Test that all metadata sources are loaded"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        metadata = builder.load_full_metadata()

        # All four metadata sources should be present
        assert "ctags_outline" in metadata
        assert "superbol_cfg" in metadata
        assert "superbol_symbols" in metadata
        assert "gnucobol_analysis" in metadata

    def test_load_full_metadata_handles_missing_sources_gracefully(self, temp_workspace):
        """Test that missing metadata sources are handled gracefully"""
        # Remove GnuCOBOL file to simulate missing source
        gnucobol_file = temp_workspace["metadata_dir"] / "gnucobol" / "gnucobol-TESTPROG-analysis.json"
        gnucobol_file.unlink()

        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        metadata = builder.load_full_metadata()

        # Should still load other sources
        assert "ctags_outline" in metadata
        assert "superbol_cfg" in metadata
        # Missing source should be empty dict or None
        assert metadata.get("gnucobol_analysis") in [None, {}]

    def test_load_full_metadata_returns_dict(self, temp_workspace):
        """Test that load_full_metadata returns a dictionary"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        metadata = builder.load_full_metadata()

        assert isinstance(metadata, dict)


# ============================================================================
# US-1.1.T6: Test generate_enhanced_program_map Higher Limits
# ============================================================================

@pytest.mark.skipif(not FULL_CONTEXT_BUILDER_AVAILABLE,
                    reason="FullContextBuilder not yet implemented")
class TestGenerateEnhancedProgramMap:
    """US-1.1.T6: Test generate_enhanced_program_map with higher limits"""

    def test_generate_enhanced_program_map_higher_limits(self, temp_workspace):
        """Test that program map can be generated with higher limits"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        # Load metadata first
        builder.load_full_metadata()

        # Generate with higher limits
        program_map = builder.generate_enhanced_program_map(
            top_n_paragraphs=100,
            top_n_data_items=50
        )

        assert program_map is not None
        assert isinstance(program_map, str)

    def test_generate_enhanced_program_map_includes_all_paragraphs_when_unlimited(self, temp_workspace):
        """Test that all paragraphs are included when limit is -1 (unlimited)"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        builder.load_full_metadata()

        # -1 means show all
        program_map = builder.generate_enhanced_program_map(
            top_n_paragraphs=-1,
            top_n_data_items=-1
        )

        # Should include all 4 paragraphs from our test data
        assert "0000-MAIN" in program_map
        assert "1000-INIT" in program_map
        assert "2000-PROCESS" in program_map
        assert "9000-CLEANUP" in program_map

    def test_generate_enhanced_program_map_respects_limits(self, temp_workspace):
        """Test that limits are respected"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        builder.load_full_metadata()

        # Limit to top 2
        program_map = builder.generate_enhanced_program_map(
            top_n_paragraphs=2,
            top_n_data_items=1
        )

        # Should be a valid program map
        assert program_map is not None
        assert len(program_map) > 0


# ============================================================================
# US-1.1.T7: Test build_full_context Combines All
# ============================================================================

@pytest.mark.skipif(not FULL_CONTEXT_BUILDER_AVAILABLE,
                    reason="FullContextBuilder not yet implemented")
class TestBuildFullContext:
    """US-1.1.T7: Test build_full_context combines all context"""

    def test_build_full_context_combines_all(self, temp_workspace):
        """Test that build_full_context combines source, metadata, and program map"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        context = builder.build_full_context()

        # Should have all three components
        assert "source_code" in context
        assert "metadata" in context
        assert "program_map" in context

    def test_build_full_context_source_is_complete(self, temp_workspace):
        """Test that source code in context is complete"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        context = builder.build_full_context()

        # Source should have all divisions
        assert "IDENTIFICATION DIVISION" in context["source_code"]
        assert "PROCEDURE DIVISION" in context["source_code"]

    def test_build_full_context_metadata_is_complete(self, temp_workspace):
        """Test that metadata in context is complete"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        context = builder.build_full_context()

        # Metadata should have all sources
        metadata = context["metadata"]
        assert "ctags_outline" in metadata
        assert "superbol_cfg" in metadata

    def test_build_full_context_program_map_included(self, temp_workspace):
        """Test that program map is included in context"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        context = builder.build_full_context()

        # Program map should be a non-empty string
        assert isinstance(context["program_map"], str)
        assert len(context["program_map"]) > 0

    def test_build_full_context_with_custom_limits(self, temp_workspace):
        """Test that build_full_context respects custom program map limits"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        context = builder.build_full_context(
            top_n_paragraphs=100,
            top_n_data_items=50,
            include_line_numbers=True
        )

        # Should have all components with custom settings
        assert "source_code" in context
        assert "1:" in context["source_code"] or "   1:" in context["source_code"]

    def test_build_full_context_returns_dict(self, temp_workspace):
        """Test that build_full_context returns a dictionary"""
        builder = FullContextBuilder(
            program_name=temp_workspace["program_name"],
            source_file_path=temp_workspace["source_file"],
            metadata_dir=temp_workspace["metadata_dir"]
        )

        context = builder.build_full_context()

        assert isinstance(context, dict)


# ============================================================================
# RUN TESTS
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
