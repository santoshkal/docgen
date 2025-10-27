"""
Tests for ripgrep_tool.py - Phase 2, Days 5-6

TDD Approach: Tests written FIRST before implementation
Following IMPLEMENTATION_PLAN.md Phase 2 structure
"""

import pytest
import tempfile
from pathlib import Path

# Import will fail initially - that's expected in TDD (RED phase)
try:
    from ripgrep_tool import RipgrepTool, check_ripgrep_installed
    IMPORT_SUCCESS = True
except ImportError:
    IMPORT_SUCCESS = False


# ==================================================
# DAY 5 MORNING: TDD Cycle 1 - Availability Check
# ==================================================

def test_ripgrep_module_exists():
    """RED: Test that ripgrep_tool module can be imported"""
    assert IMPORT_SUCCESS, "ripgrep_tool.py should exist and be importable"


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_check_ripgrep_installed():
    """RED: Test checking if ripgrep is installed"""
    installed = check_ripgrep_installed()
    assert isinstance(installed, bool)


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_ripgrep_tool_initialization():
    """RED: Test RipgrepTool initialization"""
    rg = RipgrepTool()
    assert rg is not None


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_ripgrep_tool_is_available():
    """RED: Test availability check"""
    rg = RipgrepTool()
    available = rg.is_available()
    assert isinstance(available, bool)


@pytest.mark.skipif(not IMPORT_SUCCESS or not check_ripgrep_installed(), reason="ripgrep not installed")
def test_ripgrep_get_version():
    """RED: Test getting ripgrep version"""
    rg = RipgrepTool()
    version = rg.get_version()
    assert version is not None
    assert len(version) > 0


# ==================================================
# DAY 5 AFTERNOON: TDD Cycle 2-4 - Basic Search
# ==================================================

@pytest.fixture
def test_cobol_file():
    """Create test COBOL file with patterns"""
    content = """    IDENTIFICATION DIVISION.
    PROGRAM-ID. TEST-PROG.

    PROCEDURE DIVISION.
        EXEC SQL
            SELECT * FROM CUSTOMERS
        END-EXEC.

        ON ERROR
            DISPLAY 'ERROR OCCURRED'.

        * This is a comment
        CALL 'SUBROUTINE-A' USING PARAM1.
"""
    test_file = Path(tempfile.gettempdir()) / "test_rg.cbl"
    test_file.write_text(content)
    return str(test_file)


@pytest.mark.skipif(not IMPORT_SUCCESS or not check_ripgrep_installed(), reason="ripgrep not installed")
def test_search_basic_pattern(test_cobol_file):
    """RED: Test basic pattern search"""
    rg = RipgrepTool()
    results = rg.search("EXEC SQL", test_cobol_file)

    assert len(results) > 0
    assert any("EXEC SQL" in r.match_text for r in results)


@pytest.mark.skipif(not IMPORT_SUCCESS or not check_ripgrep_installed(), reason="ripgrep not installed")
def test_search_with_context(test_cobol_file):
    """RED: Test search with before/after context"""
    rg = RipgrepTool()
    results = rg.search_with_context("ON ERROR", test_cobol_file, before=1, after=1)

    assert len(results) > 0
    result = results[0]
    assert result.context_before or result.context_after


@pytest.mark.skipif(not IMPORT_SUCCESS or not check_ripgrep_installed(), reason="ripgrep not installed")
def test_search_multiline(test_cobol_file):
    """RED: Test multiline pattern search"""
    rg = RipgrepTool()
    results = rg.search_multiline(r"EXEC SQL.*?END-EXEC", test_cobol_file)

    assert len(results) > 0


# ==================================================
# DAY 6 MORNING: TDD Cycle 5-8 - Pattern Extractors
# ==================================================

@pytest.mark.skipif(not IMPORT_SUCCESS or not check_ripgrep_installed(), reason="ripgrep not installed")
def test_extract_sql_statements(test_cobol_file):
    """RED: Test SQL statement extraction"""
    from ripgrep_tool import extract_sql_statements

    rg = RipgrepTool()
    sql_statements = extract_sql_statements(test_cobol_file, rg)

    assert len(sql_statements) > 0
    assert any("SELECT" in stmt for stmt in sql_statements)


@pytest.mark.skipif(not IMPORT_SUCCESS or not check_ripgrep_installed(), reason="ripgrep not installed")
def test_extract_comments(test_cobol_file):
    """RED: Test comment extraction"""
    from ripgrep_tool import extract_comments

    rg = RipgrepTool()
    comments = extract_comments(test_cobol_file, rg)

    assert len(comments) > 0
    assert any("This is a comment" in c for c in comments)


@pytest.mark.skipif(not IMPORT_SUCCESS or not check_ripgrep_installed(), reason="ripgrep not installed")
def test_extract_error_handling_blocks(test_cobol_file):
    """RED: Test error handling extraction"""
    from ripgrep_tool import extract_error_handling_blocks

    rg = RipgrepTool()
    errors = extract_error_handling_blocks(test_cobol_file, rg)

    assert len(errors) > 0
    assert any("ON ERROR" in e for e in errors)


@pytest.mark.skipif(not IMPORT_SUCCESS or not check_ripgrep_installed(), reason="ripgrep not installed")
def test_extract_call_statements(test_cobol_file):
    """RED: Test CALL statement extraction"""
    from ripgrep_tool import extract_call_statements

    rg = RipgrepTool()
    calls = extract_call_statements(test_cobol_file, rg)

    assert len(calls) > 0
    assert any("SUBROUTINE-A" in c["program"] for c in calls)


# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
