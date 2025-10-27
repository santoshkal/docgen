"""
Tests for multi_file_resolver.py - Phase 3, Days 7-9

TDD Approach: Tests written FIRST before implementation
Following IMPLEMENTATION_PLAN.md Phase 3 structure
"""

import pytest
import tempfile
from pathlib import Path

# Import will fail initially - expected in TDD (RED phase)
try:
    from multi_file_resolver import (
        CopybookResolver,
        CalledProgramResolver
    )
    IMPORT_SUCCESS = True
except ImportError:
    IMPORT_SUCCESS = False


# ==================================================
# TEST FIXTURES - Create test codebase structure
# ==================================================

@pytest.fixture
def test_codebase():
    """
    Create test codebase structure:
    /tmp/test-codebase/
      programs/
        MAIN-PROG.cbl
        SUBROUTINE-A.cbl
      copybooks/
        CUSTOMER-REC.cpy
        ERROR-CODES.cpy
    """
    base_dir = Path(tempfile.mkdtemp(prefix="test-cobol-"))

    # Create directories
    programs_dir = base_dir / "programs"
    copybooks_dir = base_dir / "copybooks"
    programs_dir.mkdir(parents=True)
    copybooks_dir.mkdir(parents=True)

    # Create main program with COPY statements
    main_prog = programs_dir / "MAIN-PROG.cbl"
    main_prog.write_text("""       IDENTIFICATION DIVISION.
       PROGRAM-ID. MAIN-PROG.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
           COPY CUSTOMER-REC.
           COPY ERROR-CODES.
       01 WS-COUNTER PIC 9(3).

       PROCEDURE DIVISION.
           CALL 'SUBROUTINE-A'.
           STOP RUN.
""")

    # Create subroutine
    subroutine = programs_dir / "SUBROUTINE-A.cbl"
    subroutine.write_text("""       IDENTIFICATION DIVISION.
       PROGRAM-ID. SUBROUTINE-A.

       PROCEDURE DIVISION.
           DISPLAY 'SUBROUTINE A'.
           EXIT PROGRAM.
""")

    # Create copybooks
    customer_rec = copybooks_dir / "CUSTOMER-REC.cpy"
    customer_rec.write_text("""       01 CUSTOMER-REC.
          05 CUST-ID       PIC 9(5).
          05 CUST-NAME     PIC X(30).
          05 CUST-BALANCE  PIC 9(7)V99.
""")

    error_codes = copybooks_dir / "ERROR-CODES.cpy"
    error_codes.write_text("""       01 ERROR-CODES.
          05 ERR-FILE-NOT-FOUND    PIC XX VALUE '01'.
          05 ERR-INVALID-DATA      PIC XX VALUE '02'.
""")

    return {
        "base_dir": str(base_dir),
        "programs_dir": str(programs_dir),
        "copybooks_dir": str(copybooks_dir),
        "main_prog": str(main_prog),
        "subroutine": str(subroutine),
        "customer_rec": str(customer_rec),
        "error_codes": str(error_codes)
    }


# ==================================================
# DAY 7 MORNING: TDD Cycle 1 - Finding Copybooks
# ==================================================

def test_multi_file_resolver_module_exists():
    """RED: Test that multi_file_resolver module can be imported"""
    assert IMPORT_SUCCESS, "multi_file_resolver.py should exist and be importable"


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_copybook_resolver_initialization(test_codebase):
    """RED: Test CopybookResolver initialization"""
    resolver = CopybookResolver(
        codebase_root=test_codebase["base_dir"],
        search_paths=[test_codebase["copybooks_dir"]]
    )
    assert resolver is not None


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_find_copybook_in_same_directory(test_codebase):
    """RED: Test finding copybook in same directory"""
    resolver = CopybookResolver(
        codebase_root=test_codebase["base_dir"],
        search_paths=[test_codebase["copybooks_dir"]]
    )

    path = resolver.find_copybook("CUSTOMER-REC")

    assert path is not None
    assert "CUSTOMER-REC" in path


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_find_copybook_in_standard_location(test_codebase):
    """RED: Test finding copybook in standard location"""
    resolver = CopybookResolver(
        codebase_root=test_codebase["base_dir"],
        search_paths=[test_codebase["copybooks_dir"]]
    )

    path = resolver.find_copybook("ERROR-CODES")

    assert path is not None
    assert "ERROR-CODES" in path


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_find_copybook_not_found(test_codebase):
    """RED: Test handling of missing copybook"""
    resolver = CopybookResolver(
        codebase_root=test_codebase["base_dir"],
        search_paths=[test_codebase["copybooks_dir"]]
    )

    path = resolver.find_copybook("NONEXISTENT")

    assert path is None


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_extract_copybook_content(test_codebase):
    """RED: Test extracting copybook content"""
    resolver = CopybookResolver(
        codebase_root=test_codebase["base_dir"],
        search_paths=[test_codebase["copybooks_dir"]]
    )

    content = resolver.extract_copybook_content(test_codebase["customer_rec"])

    assert content is not None
    assert "CUSTOMER-REC" in content
    assert "CUST-ID" in content


# ==================================================
# DAY 7 AFTERNOON: TDD Cycle 2 - Resolving All Copybooks
# ==================================================

@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_parse_copy_statements(test_codebase):
    """RED: Test parsing COPY statements from COBOL file"""
    resolver = CopybookResolver(
        codebase_root=test_codebase["base_dir"],
        search_paths=[test_codebase["copybooks_dir"]]
    )

    copy_statements = resolver.parse_copy_statements(test_codebase["main_prog"])

    assert len(copy_statements) >= 2
    assert any("CUSTOMER-REC" in stmt for stmt in copy_statements)
    assert any("ERROR-CODES" in stmt for stmt in copy_statements)


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_resolve_all_copybooks(test_codebase):
    """RED: Test resolving all copybooks in program"""
    resolver = CopybookResolver(
        codebase_root=test_codebase["base_dir"],
        search_paths=[test_codebase["copybooks_dir"]]
    )

    resolved = resolver.resolve_all_copybooks(test_codebase["main_prog"])

    assert "CUSTOMER-REC" in resolved
    assert "ERROR-CODES" in resolved
    assert len(resolved["CUSTOMER-REC"]) > 0
    assert "CUST-ID" in resolved["CUSTOMER-REC"]


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_copybook_dependency_graph(test_codebase):
    """RED: Test building copybook dependency graph"""
    resolver = CopybookResolver(
        codebase_root=test_codebase["base_dir"],
        search_paths=[test_codebase["copybooks_dir"]]
    )

    graph = resolver.build_copybook_dependency_graph(test_codebase["main_prog"])

    assert isinstance(graph, dict)
    assert test_codebase["main_prog"] in graph


# ==================================================
# DAY 8: TDD Cycle 3 - Called Program Resolver
# ==================================================

@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_called_program_resolver_initialization(test_codebase):
    """RED: Test CalledProgramResolver initialization"""
    from ripgrep_tool import RipgrepTool

    resolver = CalledProgramResolver(
        codebase_root=test_codebase["base_dir"],
        search_paths=[test_codebase["programs_dir"]],
        rg_tool=RipgrepTool()
    )
    assert resolver is not None


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_find_called_program(test_codebase):
    """RED: Test finding called program"""
    from ripgrep_tool import RipgrepTool

    resolver = CalledProgramResolver(
        codebase_root=test_codebase["base_dir"],
        search_paths=[test_codebase["programs_dir"]],
        rg_tool=RipgrepTool()
    )

    path = resolver.find_called_program("SUBROUTINE-A")

    assert path is not None
    assert "SUBROUTINE-A" in path


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_extract_program_header(test_codebase):
    """RED: Test extracting program header"""
    from ripgrep_tool import RipgrepTool

    resolver = CalledProgramResolver(
        codebase_root=test_codebase["base_dir"],
        search_paths=[test_codebase["programs_dir"]],
        rg_tool=RipgrepTool()
    )

    header = resolver.extract_program_header(test_codebase["subroutine"])

    assert "program_id" in header
    assert header["program_id"] == "SUBROUTINE-A"


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_parse_call_statements(test_codebase):
    """RED: Test parsing CALL statements from COBOL file"""
    from ripgrep_tool import RipgrepTool

    resolver = CalledProgramResolver(
        codebase_root=test_codebase["base_dir"],
        search_paths=[test_codebase["programs_dir"]],
        rg_tool=RipgrepTool()
    )

    calls = resolver.parse_call_statements(test_codebase["main_prog"])

    assert len(calls) >= 1
    assert any("SUBROUTINE-A" in call for call in calls)


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_resolve_all_calls(test_codebase):
    """RED: Test resolving all CALL statements"""
    from ripgrep_tool import RipgrepTool

    resolver = CalledProgramResolver(
        codebase_root=test_codebase["base_dir"],
        search_paths=[test_codebase["programs_dir"]],
        rg_tool=RipgrepTool()
    )

    resolved = resolver.resolve_all_calls(test_codebase["main_prog"])

    assert "SUBROUTINE-A" in resolved
    assert resolved["SUBROUTINE-A"]["path"] is not None


@pytest.mark.skipif(not IMPORT_SUCCESS, reason="Module not created yet")
def test_build_call_hierarchy(test_codebase):
    """RED: Test building call hierarchy"""
    from ripgrep_tool import RipgrepTool

    resolver = CalledProgramResolver(
        codebase_root=test_codebase["base_dir"],
        search_paths=[test_codebase["programs_dir"]],
        rg_tool=RipgrepTool()
    )

    hierarchy = resolver.build_call_hierarchy(test_codebase["main_prog"], depth=2)

    assert hierarchy["program"] == "MAIN-PROG"
    assert "calls" in hierarchy


# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
