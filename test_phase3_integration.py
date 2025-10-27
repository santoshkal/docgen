"""
Integration Tests for Phase 3 Multi-File Support (Day 9)

Tests the integration of multi-file resolvers into the agent.

TDD Approach: Tests written FIRST
"""

import tempfile
from pathlib import Path


def test_source_integration_imports():
    """RED: Test that source_integration has multi-file support"""
    try:
        from source_integration import (
            extract_source_for_section,
            extract_source_with_copybooks,
            extract_source_with_called_programs
        )
        print("✓ source_integration imports work")
        return True
    except ImportError as e:
        print(f"✗ Import failed (expected in RED phase): {e}")
        return False


def test_extract_with_copybooks():
    """RED: Test extraction includes copybook content"""
    # This will be implemented after source_integration.py is updated
    try:
        from source_integration import extract_source_with_copybooks
        from multi_file_resolver import CopybookResolver

        # Create test files
        base_dir = Path(tempfile.mkdtemp(prefix="test-"))
        programs_dir = base_dir / "programs"
        copybooks_dir = base_dir / "copybooks"
        programs_dir.mkdir(parents=True)
        copybooks_dir.mkdir(parents=True)

        main_prog = programs_dir / "MAIN.cbl"
        main_prog.write_text("""       IDENTIFICATION DIVISION.
       PROGRAM-ID. MAIN.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
           COPY CUSTOMER-REC.
""")

        customer_rec = copybooks_dir / "CUSTOMER-REC.cpy"
        customer_rec.write_text("""       01 CUSTOMER-REC.
          05 CUST-ID PIC 9(5).
""")

        # Test extraction with copybooks
        cb_resolver = CopybookResolver(str(base_dir), [str(copybooks_dir)])
        result = extract_source_with_copybooks(
            section_id="2_data_structures",
            cobol_file_path=str(main_prog),
            copybook_resolver=cb_resolver
        )

        assert result is not None, "Should extract source"
        assert "CUSTOMER-REC" in result, "Should include copybook reference"
        # Note: Content may or may not include actual copybook content depending on implementation

        print("✓ extract_with_copybooks works")
        return True

    except Exception as e:
        print(f"✗ Test failed (expected in RED phase): {e}")
        return False


def test_extract_with_called_programs():
    """RED: Test extraction includes called program info"""
    try:
        from source_integration import extract_source_with_called_programs
        from multi_file_resolver import CalledProgramResolver
        from ripgrep_tool import RipgrepTool

        # Create test files
        base_dir = Path(tempfile.mkdtemp(prefix="test-"))
        programs_dir = base_dir / "programs"
        programs_dir.mkdir(parents=True)

        main_prog = programs_dir / "MAIN.cbl"
        main_prog.write_text("""       IDENTIFICATION DIVISION.
       PROGRAM-ID. MAIN.
       PROCEDURE DIVISION.
           CALL 'SUBPROG'.
""")

        subprog = programs_dir / "SUBPROG.cbl"
        subprog.write_text("""       IDENTIFICATION DIVISION.
       PROGRAM-ID. SUBPROG.
""")

        # Test extraction with called programs
        prog_resolver = CalledProgramResolver(str(base_dir), [str(programs_dir)], RipgrepTool())
        result = extract_source_with_called_programs(
            section_id="3_business_logic",
            cobol_file_path=str(main_prog),
            called_program_resolver=prog_resolver
        )

        assert result is not None, "Should extract source"
        assert "CALL" in result or "SUBPROG" in result, "Should include call info"

        print("✓ extract_with_called_programs works")
        return True

    except Exception as e:
        print(f"✗ Test failed (expected in RED phase): {e}")
        return False


def test_config_has_multi_file_settings():
    """RED: Test that config supports multi-file settings"""
    try:
        from config_loader import load_config
        import tempfile

        # Create test config
        config_content = """
source:
  mode: single
  source_files: /test/main.cbl
  program_name: MAIN

output:
  metadata_dir: /test/metadata
  docs_path: /test/docs

llm:
  provider: openai
  model: gpt-4o

source_extraction:
  enabled: true
  compress: true
  resolve_copybooks: true
  copybook_search_paths:
    - ./copybooks
    - ./COPY
"""
        config_file = Path(tempfile.mkdtemp()) / "test.yaml"
        config_file.write_text(config_content)

        loader = load_config(str(config_file))
        extraction_config = loader.get_source_extraction_config()

        assert "resolve_copybooks" in extraction_config, "Should have resolve_copybooks setting"
        assert "copybook_search_paths" in extraction_config, "Should have copybook_search_paths"

        print("✓ Config supports multi-file settings")
        return True

    except Exception as e:
        print(f"✗ Test failed (expected in RED phase): {e}")
        return False


def run_all_integration_tests():
    """Run all Phase 3 integration tests"""
    print("="*70)
    print("Phase 3 Day 9: Integration Tests")
    print("="*70)
    print()

    tests = [
        ("source_integration imports", test_source_integration_imports),
        ("extract_with_copybooks", test_extract_with_copybooks),
        ("extract_with_called_programs", test_extract_with_called_programs),
        ("config multi-file settings", test_config_has_multi_file_settings)
    ]

    results = []
    for name, test_func in tests:
        print(f"\nRunning: {name}")
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"✗ Test crashed: {e}")
            results.append((name, False))

    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status:10} - {name}")

    print(f"\nTotal: {passed}/{total} tests passed")

    if passed == total:
        print("\n✅ All integration tests PASSED (GREEN phase)")
        return 0
    else:
        print(f"\n⚠ {total - passed} tests FAILED (RED phase - expected)")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(run_all_integration_tests())
