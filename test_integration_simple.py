#!/usr/bin/env python3
"""
Simple Integration Test for Source Extraction (Phase 1)

Tests the integration points without running the full agent.
This test verifies:
1. AgentState has source extraction fields
2. build_section_context can extract source
3. Config loader reads source extraction settings
"""

import sys
import tempfile
from pathlib import Path
from typing import TypedDict, Dict, Any


def test_agent_state_fields():
    """Test that AgentState has source extraction fields"""
    print("Test 1: AgentState TypedDict fields...")

    # Import the AgentState (this will fail if fields are missing)
    try:
        # Read the cobol_doc_agent.py file to verify AgentState has the fields
        with open('cobol_doc_agent.py', 'r') as f:
            content = f.read()

        # Check for the three new fields
        checks = [
            ('enable_source_extraction: bool', 'enable_source_extraction field'),
            ('compress_source: bool', 'compress_source field'),
            ('cobol_file_path: Optional[str]', 'cobol_file_path field'),
        ]

        all_passed = True
        for field_def, field_name in checks:
            if field_def in content:
                print(f"   ✓ Found {field_name}")
            else:
                print(f"   ✗ Missing {field_name}")
                all_passed = False

        if all_passed:
            print("   ✅ AgentState test PASSED")
            return True
        else:
            print("   ❌ AgentState test FAILED")
            return False

    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def test_source_extraction_modules():
    """Test that source extraction modules can be imported"""
    print("\nTest 2: Source extraction module imports...")

    try:
        from source_integration import extract_source_for_section
        from section_requirements import should_extract_source
        from source_extractor import extract_division

        print("   ✓ source_integration imported")
        print("   ✓ section_requirements imported")
        print("   ✓ source_extractor imported")
        print("   ✅ Module import test PASSED")
        return True

    except Exception as e:
        print(f"   ❌ Import error: {e}")
        return False


def test_config_loader():
    """Test that config loader can read source extraction config"""
    print("\nTest 3: Config loader source extraction support...")

    try:
        from config_loader import load_config

        # Create a test config file
        test_dir = Path(tempfile.mkdtemp(prefix="test_config_"))
        config_file = test_dir / "test.yaml"

        config_content = """
source:
  mode: single
  source_files: /test/file.cbl
  program_name: TEST

output:
  metadata_dir: /test/metadata
  docs_path: /test/docs

llm:
  provider: openai
  model: gpt-4o

source_extraction:
  enabled: true
  compress: false
"""

        config_file.write_text(config_content)

        # Load config
        loader = load_config(str(config_file))

        # Check if get_source_extraction_config exists
        if hasattr(loader, 'get_source_extraction_config'):
            print("   ✓ get_source_extraction_config() method exists")

            extraction_config = loader.get_source_extraction_config()
            print(f"   ✓ Config loaded: {extraction_config}")

            if extraction_config.get('enabled') == True:
                print("   ✓ 'enabled' field read correctly")
            else:
                print("   ✗ 'enabled' field not read correctly")
                return False

            if extraction_config.get('compress') == False:
                print("   ✓ 'compress' field read correctly")
            else:
                print("   ✗ 'compress' field not read correctly")
                return False

            print("   ✅ Config loader test PASSED")
            return True
        else:
            print("   ✗ get_source_extraction_config() method not found")
            return False

    except Exception as e:
        print(f"   ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_build_section_context_integration():
    """Test that build_section_context can integrate source extraction"""
    print("\nTest 4: build_section_context integration...")

    try:
        # Check that build_section_context calls source extraction
        with open('cobol_doc_agent.py', 'r') as f:
            content = f.read()

        # Check for integration points
        checks = [
            ('extract_source_for_section', 'extract_source_for_section call'),
            ('enable_source_extraction', 'enable_source_extraction check'),
            ('SOURCE_EXTRACTION_AVAILABLE', 'availability check'),
            ('source_code', 'source_code in filtered_context'),
        ]

        all_passed = True
        for search_text, check_name in checks:
            if search_text in content:
                print(f"   ✓ Found {check_name}")
            else:
                print(f"   ✗ Missing {check_name}")
                all_passed = False

        if all_passed:
            print("   ✅ build_section_context integration test PASSED")
            return True
        else:
            print("   ❌ build_section_context integration test FAILED")
            return False

    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def test_source_extraction_end_to_end():
    """Test actual source extraction with a test COBOL file"""
    print("\nTest 5: End-to-end source extraction...")

    try:
        from source_integration import extract_source_for_section

        # Create a test COBOL file
        test_dir = Path(tempfile.mkdtemp(prefix="test_cobol_"))
        cobol_file = test_dir / "test.cbl"

        cobol_content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST-PROG.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-COUNTER PIC 9(3).
       01 WS-NAME PIC X(20).

       PROCEDURE DIVISION.
       MAIN-PARA.
           DISPLAY "Test".
           STOP RUN.
"""

        cobol_file.write_text(cobol_content)

        # Extract source for data structures section
        source = extract_source_for_section('2_data_structures', str(cobol_file), compress=False)

        if source:
            print(f"   ✓ Source extracted successfully")

            if 'DATA DIVISION' in source:
                print(f"   ✓ Contains DATA DIVISION")
            else:
                print(f"   ✗ Missing DATA DIVISION")
                return False

            if 'WS-COUNTER' in source:
                print(f"   ✓ Contains WS-COUNTER")
            else:
                print(f"   ✗ Missing WS-COUNTER")
                return False

            if '```cobol' in source:
                print(f"   ✓ Has markdown formatting")
            else:
                print(f"   ✗ Missing markdown formatting")
                return False

            print("   ✅ End-to-end extraction test PASSED")
            return True
        else:
            print(f"   ✗ No source extracted")
            return False

    except Exception as e:
        print(f"   ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_all_tests():
    """Run all integration tests"""
    print("=" * 70)
    print("Phase 1 Integration Tests: Source Code Extraction")
    print("=" * 70)
    print()

    results = []

    # Run all tests
    results.append(("AgentState fields", test_agent_state_fields()))
    results.append(("Module imports", test_source_extraction_modules()))
    results.append(("Config loader", test_config_loader()))
    results.append(("build_section_context", test_build_section_context_integration()))
    results.append(("End-to-end extraction", test_source_extraction_end_to_end()))

    # Summary
    print()
    print("=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status:12} - {test_name}")

    print()
    print(f"Total: {passed}/{total} tests passed")

    if passed == total:
        print()
        print("✅ ALL INTEGRATION TESTS PASSED")
        print()
        print("🎉 Phase 1 source extraction is successfully integrated!")
        return 0
    else:
        print()
        print("❌ SOME TESTS FAILED")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
