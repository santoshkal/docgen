"""
Test suite for Category-Based Mandatory Inclusion in Program Map

TDD tests for US-1.5: Category-Based Mandatory Inclusion in Program Map
These tests are written FIRST before implementation.

Tests cover:
- Entry points (MAIN, START, INIT patterns) always included
- External call sites (paragraphs with CALL statements) always included
- Error handlers (ERR, ERROR, EXCEPTION patterns) always included
- Configurable mandatory category patterns
- Separate "Critical Elements" section in program map
- No duplicates between mandatory and rank-based sections
"""

import os
import pytest
import tempfile
from typing import Dict, Any, List


# ============================================================================
# TEST FIXTURES
# ============================================================================

@pytest.fixture
def sample_metadata_with_entry_points():
    """Metadata with various entry point patterns"""
    return {
        "ctags_outline": {
            "file": "TESTPROG.cbl",
            "symbols": [
                {"name": "TESTPROG", "kind": "program", "line": 1},
                # Entry points (should be mandatory)
                {"name": "0000-MAIN-DRIVER", "kind": "paragraph", "line": 100},
                {"name": "A-MAIN-PROCESS", "kind": "paragraph", "line": 110},
                {"name": "START-PROCESSING", "kind": "paragraph", "line": 120},
                {"name": "INIT-PROGRAM", "kind": "paragraph", "line": 130},
                {"name": "Z-INITIALIZATION", "kind": "paragraph", "line": 140},
                # Regular paragraphs (not entry points)
                {"name": "1000-READ-FILE", "kind": "paragraph", "line": 200},
                {"name": "2000-WRITE-OUTPUT", "kind": "paragraph", "line": 300},
                {"name": "3000-CALCULATE", "kind": "paragraph", "line": 400},
                # Data items
                {"name": "WS-COUNTER", "kind": "data", "level": "01", "line": 10},
            ]
        },
        "superbol_cfg": {
            "program": "TESTPROG",
            "performs": [
                {"from": "0000-MAIN-DRIVER", "to": "1000-READ-FILE"},
                {"from": "0000-MAIN-DRIVER", "to": "2000-WRITE-OUTPUT"}
            ],
            "calls": [],
            "edges": []
        },
        "gnucobol_analysis": {
            "program": "TESTPROG",
            "variables": {}
        }
    }


@pytest.fixture
def sample_metadata_with_call_sites():
    """Metadata with paragraphs that make external calls"""
    return {
        "ctags_outline": {
            "file": "TESTPROG.cbl",
            "symbols": [
                {"name": "TESTPROG", "kind": "program", "line": 1},
                # Paragraphs that make calls (should be mandatory)
                {"name": "1000-CALL-SUBPROG", "kind": "paragraph", "line": 100},
                {"name": "2000-CALL-DATABASE", "kind": "paragraph", "line": 200},
                {"name": "3000-CALL-EXTERNAL", "kind": "paragraph", "line": 300},
                # Regular paragraphs (no calls)
                {"name": "4000-PROCESS-DATA", "kind": "paragraph", "line": 400},
                {"name": "5000-VALIDATE", "kind": "paragraph", "line": 500},
                # Data items
                {"name": "WS-DATA", "kind": "data", "level": "01", "line": 10},
            ]
        },
        "superbol_cfg": {
            "program": "TESTPROG",
            "performs": [],
            "calls": [
                {"from": "1000-CALL-SUBPROG", "to": "SUBPROG1", "type": "CALL"},
                {"from": "2000-CALL-DATABASE", "to": "DB2READ", "type": "CALL"},
                {"from": "2000-CALL-DATABASE", "to": "DB2WRITE", "type": "CALL"},
                {"from": "3000-CALL-EXTERNAL", "to": "EXTPROG", "type": "CALL"}
            ],
            "edges": []
        },
        "gnucobol_analysis": {
            "program": "TESTPROG",
            "variables": {}
        }
    }


@pytest.fixture
def sample_metadata_with_error_handlers():
    """Metadata with error handling paragraphs"""
    return {
        "ctags_outline": {
            "file": "TESTPROG.cbl",
            "symbols": [
                {"name": "TESTPROG", "kind": "program", "line": 1},
                # Error handlers (should be mandatory)
                {"name": "8000-ERROR-HANDLER", "kind": "paragraph", "line": 800},
                {"name": "8100-FILE-ERROR", "kind": "paragraph", "line": 810},
                {"name": "8200-DB-ERR-ROUTINE", "kind": "paragraph", "line": 820},
                {"name": "8300-EXCEPTION-PROC", "kind": "paragraph", "line": 830},
                {"name": "9000-ABEND-HANDLER", "kind": "paragraph", "line": 900},
                # Regular paragraphs
                {"name": "1000-PROCESS", "kind": "paragraph", "line": 100},
                {"name": "2000-VALIDATE", "kind": "paragraph", "line": 200},
                # Data items
                {"name": "WS-ERROR-CODE", "kind": "data", "level": "01", "line": 10},
            ]
        },
        "superbol_cfg": {
            "program": "TESTPROG",
            "performs": [],
            "calls": [],
            "edges": []
        },
        "gnucobol_analysis": {
            "program": "TESTPROG",
            "variables": {}
        }
    }


@pytest.fixture
def sample_metadata_comprehensive():
    """Comprehensive metadata with all mandatory categories"""
    return {
        "ctags_outline": {
            "file": "TESTPROG.cbl",
            "symbols": [
                {"name": "TESTPROG", "kind": "program", "line": 1},
                # Entry points
                {"name": "0000-MAIN", "kind": "paragraph", "line": 100},
                {"name": "0100-INIT", "kind": "paragraph", "line": 110},
                # Call sites (identified via superbol_cfg.calls)
                {"name": "1000-CALL-EXTERNAL", "kind": "paragraph", "line": 200},
                # Error handlers
                {"name": "8000-ERROR-HANDLER", "kind": "paragraph", "line": 800},
                {"name": "9000-ABEND", "kind": "paragraph", "line": 900},
                # Regular paragraphs (lower importance, might be filtered)
                {"name": "2000-READ", "kind": "paragraph", "line": 300},
                {"name": "3000-WRITE", "kind": "paragraph", "line": 400},
                {"name": "4000-CALC", "kind": "paragraph", "line": 500},
                {"name": "5000-VALIDATE", "kind": "paragraph", "line": 600},
                {"name": "6000-FORMAT", "kind": "paragraph", "line": 700},
                # Data items
                {"name": "WS-COUNTER", "kind": "data", "level": "01", "line": 10},
                {"name": "WS-TOTAL", "kind": "data", "level": "01", "line": 11},
            ]
        },
        "superbol_cfg": {
            "program": "TESTPROG",
            "performs": [
                {"from": "0000-MAIN", "to": "0100-INIT"},
                {"from": "0000-MAIN", "to": "2000-READ"},
                {"from": "2000-READ", "to": "3000-WRITE"}
            ],
            "calls": [
                {"from": "1000-CALL-EXTERNAL", "to": "EXTPROG", "type": "CALL"}
            ],
            "edges": []
        },
        "gnucobol_analysis": {
            "program": "TESTPROG",
            "variables": {
                "WS-COUNTER": {"references": 10},
                "WS-TOTAL": {"references": 5}
            }
        }
    }


@pytest.fixture
def sample_metadata_large_with_mandatory():
    """Large program with mandatory elements that might be ranked low"""
    symbols = [{"name": "TESTPROG", "kind": "program", "line": 1}]

    # Add 100 regular paragraphs first (will have higher importance due to performs)
    for i in range(100):
        symbols.append({
            "name": f"PARA-{i:04d}",
            "kind": "paragraph",
            "line": 100 + i * 10
        })

    # Add entry point (even though added later, should still be included)
    symbols.append({"name": "Z-MAIN-ENTRY", "kind": "paragraph", "line": 2000})

    # Add error handler (low in list, but should be included)
    symbols.append({"name": "9999-ERROR-EXIT", "kind": "paragraph", "line": 3000})

    # Add data items
    for i in range(50):
        symbols.append({
            "name": f"WS-DATA-{i:04d}",
            "kind": "data",
            "level": "01",
            "line": 10 + i
        })

    # Create performs to make first paragraphs more important
    performs = []
    for i in range(50):
        performs.append({"from": f"PARA-{i:04d}", "to": f"PARA-{i+1:04d}"})

    return {
        "ctags_outline": {
            "file": "TESTPROG.cbl",
            "symbols": symbols
        },
        "superbol_cfg": {
            "program": "TESTPROG",
            "performs": performs,
            "calls": [{"from": "PARA-0010", "to": "EXTPROG", "type": "CALL"}],
            "edges": []
        },
        "gnucobol_analysis": {
            "program": "TESTPROG",
            "variables": {}
        }
    }


# ============================================================================
# US-1.5.T1: Test Entry Points Always Included
# ============================================================================

class TestCategoryInclusionEntryPoints:
    """US-1.5.T1: Test that entry points are always included"""

    def test_identify_entry_points_main_pattern(self, sample_metadata_with_entry_points):
        """Entry points with MAIN in name should be identified"""
        from mandatory_elements import identify_entry_points

        entry_points = identify_entry_points(sample_metadata_with_entry_points)

        # Should find MAIN patterns
        entry_point_names = [ep['name'] for ep in entry_points]
        assert "0000-MAIN-DRIVER" in entry_point_names
        assert "A-MAIN-PROCESS" in entry_point_names

    def test_identify_entry_points_start_pattern(self, sample_metadata_with_entry_points):
        """Entry points with START in name should be identified"""
        from mandatory_elements import identify_entry_points

        entry_points = identify_entry_points(sample_metadata_with_entry_points)

        entry_point_names = [ep['name'] for ep in entry_points]
        assert "START-PROCESSING" in entry_point_names

    def test_identify_entry_points_init_pattern(self, sample_metadata_with_entry_points):
        """Entry points with INIT in name should be identified"""
        from mandatory_elements import identify_entry_points

        entry_points = identify_entry_points(sample_metadata_with_entry_points)

        entry_point_names = [ep['name'] for ep in entry_points]
        assert "INIT-PROGRAM" in entry_point_names
        assert "Z-INITIALIZATION" in entry_point_names

    def test_identify_entry_points_excludes_regular(self, sample_metadata_with_entry_points):
        """Regular paragraphs should not be identified as entry points"""
        from mandatory_elements import identify_entry_points

        entry_points = identify_entry_points(sample_metadata_with_entry_points)

        entry_point_names = [ep['name'] for ep in entry_points]
        assert "1000-READ-FILE" not in entry_point_names
        assert "2000-WRITE-OUTPUT" not in entry_point_names
        assert "3000-CALCULATE" not in entry_point_names


# ============================================================================
# US-1.5.T2: Test Call Sites Always Included
# ============================================================================

class TestCategoryInclusionCallSites:
    """US-1.5.T2: Test that call sites are always included"""

    def test_identify_call_sites_from_cfg(self, sample_metadata_with_call_sites):
        """Paragraphs with CALL statements should be identified from CFG"""
        from mandatory_elements import identify_call_sites

        call_sites = identify_call_sites(sample_metadata_with_call_sites)

        call_site_names = [cs['name'] for cs in call_sites]
        assert "1000-CALL-SUBPROG" in call_site_names
        assert "2000-CALL-DATABASE" in call_site_names
        assert "3000-CALL-EXTERNAL" in call_site_names

    def test_identify_call_sites_excludes_non_callers(self, sample_metadata_with_call_sites):
        """Paragraphs without CALL statements should not be call sites"""
        from mandatory_elements import identify_call_sites

        call_sites = identify_call_sites(sample_metadata_with_call_sites)

        call_site_names = [cs['name'] for cs in call_sites]
        assert "4000-PROCESS-DATA" not in call_site_names
        assert "5000-VALIDATE" not in call_site_names

    def test_identify_call_sites_includes_call_target_info(self, sample_metadata_with_call_sites):
        """Call sites should include information about what they call"""
        from mandatory_elements import identify_call_sites

        call_sites = identify_call_sites(sample_metadata_with_call_sites)

        # Find the 2000-CALL-DATABASE entry
        db_call = next((cs for cs in call_sites if cs['name'] == "2000-CALL-DATABASE"), None)
        assert db_call is not None
        assert 'calls_to' in db_call
        assert "DB2READ" in db_call['calls_to'] or len(db_call['calls_to']) >= 2

    def test_identify_call_sites_handles_empty_calls(self):
        """Should handle metadata with no calls gracefully"""
        from mandatory_elements import identify_call_sites

        metadata = {
            "ctags_outline": {"symbols": []},
            "superbol_cfg": {"calls": []},
            "gnucobol_analysis": {}
        }

        call_sites = identify_call_sites(metadata)

        assert call_sites == []


# ============================================================================
# US-1.5.T3: Test Error Handlers Always Included
# ============================================================================

class TestCategoryInclusionErrorHandlers:
    """US-1.5.T3: Test that error handlers are always included"""

    def test_identify_error_handlers_error_pattern(self, sample_metadata_with_error_handlers):
        """Paragraphs with ERROR in name should be identified"""
        from mandatory_elements import identify_error_handlers

        error_handlers = identify_error_handlers(sample_metadata_with_error_handlers)

        handler_names = [eh['name'] for eh in error_handlers]
        assert "8000-ERROR-HANDLER" in handler_names
        assert "8100-FILE-ERROR" in handler_names

    def test_identify_error_handlers_err_pattern(self, sample_metadata_with_error_handlers):
        """Paragraphs with ERR in name should be identified"""
        from mandatory_elements import identify_error_handlers

        error_handlers = identify_error_handlers(sample_metadata_with_error_handlers)

        handler_names = [eh['name'] for eh in error_handlers]
        assert "8200-DB-ERR-ROUTINE" in handler_names

    def test_identify_error_handlers_exception_pattern(self, sample_metadata_with_error_handlers):
        """Paragraphs with EXCEPTION in name should be identified"""
        from mandatory_elements import identify_error_handlers

        error_handlers = identify_error_handlers(sample_metadata_with_error_handlers)

        handler_names = [eh['name'] for eh in error_handlers]
        assert "8300-EXCEPTION-PROC" in handler_names

    def test_identify_error_handlers_abend_pattern(self, sample_metadata_with_error_handlers):
        """Paragraphs with ABEND in name should be identified"""
        from mandatory_elements import identify_error_handlers

        error_handlers = identify_error_handlers(sample_metadata_with_error_handlers)

        handler_names = [eh['name'] for eh in error_handlers]
        assert "9000-ABEND-HANDLER" in handler_names

    def test_identify_error_handlers_excludes_regular(self, sample_metadata_with_error_handlers):
        """Regular paragraphs should not be identified as error handlers"""
        from mandatory_elements import identify_error_handlers

        error_handlers = identify_error_handlers(sample_metadata_with_error_handlers)

        handler_names = [eh['name'] for eh in error_handlers]
        assert "1000-PROCESS" not in handler_names
        assert "2000-VALIDATE" not in handler_names


# ============================================================================
# US-1.5.T4: Test Configurable Patterns
# ============================================================================

class TestCategoryInclusionConfigurablePatterns:
    """US-1.5.T4: Test that mandatory patterns are configurable"""

    def test_custom_entry_point_patterns(self, sample_metadata_with_entry_points):
        """Custom entry point patterns should be respected"""
        from mandatory_elements import identify_entry_points

        # Use custom patterns that only match specific entries
        custom_patterns = ["MAIN-DRIVER", "START-PROC"]

        entry_points = identify_entry_points(
            sample_metadata_with_entry_points,
            patterns=custom_patterns
        )

        entry_point_names = [ep['name'] for ep in entry_points]
        # Should find MAIN-DRIVER but not other MAIN patterns
        assert "0000-MAIN-DRIVER" in entry_point_names

    def test_custom_error_handler_patterns(self, sample_metadata_with_error_handlers):
        """Custom error handler patterns should be respected"""
        from mandatory_elements import identify_error_handlers

        # Use custom patterns
        custom_patterns = ["ABEND", "FILE-ERROR"]

        error_handlers = identify_error_handlers(
            sample_metadata_with_error_handlers,
            patterns=custom_patterns
        )

        handler_names = [eh['name'] for eh in error_handlers]
        assert "9000-ABEND-HANDLER" in handler_names
        assert "8100-FILE-ERROR" in handler_names

    def test_patterns_from_config(self):
        """Patterns should be loadable from YAML config"""
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
  mandatory_elements:
    enabled: true
    entry_point_patterns:
      - MAIN
      - START
      - INIT
      - BEGIN
    error_handler_patterns:
      - ERROR
      - ERR
      - EXCEPTION
      - ABEND
      - FAIL
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(config_content)
            config_path = f.name

        try:
            loader = ConfigLoader(config_path)
            loader.load()

            pm_config = loader.get_program_map_config()

            assert 'mandatory_elements' in pm_config
            assert pm_config['mandatory_elements']['enabled'] == True
            assert 'MAIN' in pm_config['mandatory_elements']['entry_point_patterns']
            assert 'ERROR' in pm_config['mandatory_elements']['error_handler_patterns']
        finally:
            os.unlink(config_path)

    def test_default_patterns_used_when_not_configured(self, sample_metadata_with_entry_points):
        """Default patterns should be used when no custom patterns provided"""
        from mandatory_elements import identify_entry_points, DEFAULT_ENTRY_POINT_PATTERNS

        entry_points = identify_entry_points(sample_metadata_with_entry_points)

        # Should use defaults and find common patterns
        entry_point_names = [ep['name'] for ep in entry_points]
        # At least MAIN patterns should be found with defaults
        assert any("MAIN" in name for name in entry_point_names)


# ============================================================================
# US-1.5.T5: Test Separate Critical Elements Section
# ============================================================================

class TestCategoryInclusionSeparateSection:
    """US-1.5.T5: Test that mandatory elements appear in separate section"""

    def test_program_map_has_critical_elements_section(self, sample_metadata_comprehensive):
        """Program map should have a 'Critical Elements' section"""
        from mandatory_elements import format_program_map_with_mandatory

        result = format_program_map_with_mandatory(
            program_name="TESTPROG",
            metadata=sample_metadata_comprehensive
        )

        assert "Critical Elements" in result or "CRITICAL" in result.upper()

    def test_critical_elements_section_before_ranked(self, sample_metadata_comprehensive):
        """Critical Elements section should appear before ranked sections"""
        from mandatory_elements import format_program_map_with_mandatory

        result = format_program_map_with_mandatory(
            program_name="TESTPROG",
            metadata=sample_metadata_comprehensive
        )

        # Find positions
        critical_pos = result.upper().find("CRITICAL")
        # Regular ranked section might be labeled "Top" or "Most Important"
        ranked_pos = max(
            result.find("Top "),
            result.find("Most Important"),
            result.find("Ranked")
        )

        # Critical should come before ranked (if both exist)
        if critical_pos >= 0 and ranked_pos >= 0:
            assert critical_pos < ranked_pos

    def test_critical_elements_includes_all_mandatory_categories(self, sample_metadata_comprehensive):
        """Critical Elements section should include all mandatory categories"""
        from mandatory_elements import format_program_map_with_mandatory

        result = format_program_map_with_mandatory(
            program_name="TESTPROG",
            metadata=sample_metadata_comprehensive
        )

        # Should include entry point
        assert "0000-MAIN" in result or "MAIN" in result
        # Should include error handler
        assert "ERROR" in result or "ABEND" in result

    def test_get_mandatory_elements_combines_all_categories(self, sample_metadata_comprehensive):
        """get_mandatory_elements should return all mandatory elements combined"""
        from mandatory_elements import get_mandatory_elements

        mandatory = get_mandatory_elements(sample_metadata_comprehensive)

        assert isinstance(mandatory, dict)
        assert 'entry_points' in mandatory
        assert 'call_sites' in mandatory
        assert 'error_handlers' in mandatory

        # Should have some elements
        total = (len(mandatory['entry_points']) +
                len(mandatory['call_sites']) +
                len(mandatory['error_handlers']))
        assert total > 0


# ============================================================================
# US-1.5.T6: Test No Duplicates
# ============================================================================

class TestCategoryInclusionNoDuplicates:
    """US-1.5.T6: Test that no duplicates appear between sections"""

    def test_no_duplicates_in_mandatory_elements(self, sample_metadata_comprehensive):
        """Same element should not appear twice in mandatory elements"""
        from mandatory_elements import get_mandatory_elements

        mandatory = get_mandatory_elements(sample_metadata_comprehensive)

        all_names = []
        for category in ['entry_points', 'call_sites', 'error_handlers']:
            names = [elem['name'] for elem in mandatory.get(category, [])]
            all_names.extend(names)

        # Check no duplicates
        assert len(all_names) == len(set(all_names)), "Duplicate elements found in mandatory"

    def test_mandatory_elements_excluded_from_ranked(self, sample_metadata_comprehensive):
        """Elements in mandatory should not appear in ranked section"""
        from mandatory_elements import get_mandatory_elements, get_ranked_elements_excluding_mandatory

        mandatory = get_mandatory_elements(sample_metadata_comprehensive)
        ranked = get_ranked_elements_excluding_mandatory(sample_metadata_comprehensive, mandatory)

        # Get all mandatory names
        mandatory_names = set()
        for category in ['entry_points', 'call_sites', 'error_handlers']:
            for elem in mandatory.get(category, []):
                mandatory_names.add(elem['name'])

        # Check none of the ranked elements are in mandatory
        ranked_names = [elem['name'] for elem in ranked]
        for name in ranked_names:
            assert name not in mandatory_names, f"{name} appears in both mandatory and ranked"

    def test_program_map_no_duplicate_paragraphs(self, sample_metadata_comprehensive):
        """Same paragraph should not appear twice in program map output"""
        from mandatory_elements import format_program_map_with_mandatory

        result = format_program_map_with_mandatory(
            program_name="TESTPROG",
            metadata=sample_metadata_comprehensive
        )

        # Count occurrences of specific paragraph (0000-MAIN should appear once)
        main_count = result.count("0000-MAIN")
        assert main_count <= 1, f"0000-MAIN appears {main_count} times"

    def test_mandatory_low_ranked_still_included(self, sample_metadata_large_with_mandatory):
        """Mandatory elements should be included even if ranked low"""
        from mandatory_elements import get_mandatory_elements, format_program_map_with_mandatory

        mandatory = get_mandatory_elements(sample_metadata_large_with_mandatory)

        # The entry point and error handler should be found
        all_mandatory_names = []
        for category in ['entry_points', 'call_sites', 'error_handlers']:
            for elem in mandatory.get(category, []):
                all_mandatory_names.append(elem['name'])

        # Z-MAIN-ENTRY should be in entry points
        assert "Z-MAIN-ENTRY" in all_mandatory_names
        # 9999-ERROR-EXIT should be in error handlers
        assert "9999-ERROR-EXIT" in all_mandatory_names

        # And they should appear in the program map
        result = format_program_map_with_mandatory(
            program_name="TESTPROG",
            metadata=sample_metadata_large_with_mandatory,
            top_n_paragraphs=10  # Very limited, but mandatory should still appear
        )

        assert "Z-MAIN-ENTRY" in result
        assert "9999-ERROR-EXIT" in result


# ============================================================================
# ADDITIONAL HELPER TESTS
# ============================================================================

class TestMandatoryElementsHelpers:
    """Test helper functions and constants"""

    def test_default_patterns_exist(self):
        """Default pattern constants should be defined"""
        from mandatory_elements import (
            DEFAULT_ENTRY_POINT_PATTERNS,
            DEFAULT_ERROR_HANDLER_PATTERNS
        )

        assert isinstance(DEFAULT_ENTRY_POINT_PATTERNS, (list, tuple))
        assert isinstance(DEFAULT_ERROR_HANDLER_PATTERNS, (list, tuple))
        assert len(DEFAULT_ENTRY_POINT_PATTERNS) > 0
        assert len(DEFAULT_ERROR_HANDLER_PATTERNS) > 0

    def test_mandatory_categories_constant(self):
        """MANDATORY_CATEGORIES constant should be defined"""
        from mandatory_elements import MANDATORY_CATEGORIES

        assert isinstance(MANDATORY_CATEGORIES, dict)
        assert 'entry_points' in MANDATORY_CATEGORIES
        assert 'error_handlers' in MANDATORY_CATEGORIES

    def test_handles_empty_metadata(self):
        """Should handle empty metadata gracefully"""
        from mandatory_elements import get_mandatory_elements

        metadata = {}
        mandatory = get_mandatory_elements(metadata)

        assert isinstance(mandatory, dict)
        assert mandatory.get('entry_points', []) == []
        assert mandatory.get('call_sites', []) == []
        assert mandatory.get('error_handlers', []) == []


# ============================================================================
# RUN TESTS
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
