#!/usr/bin/env python3
"""
End-to-End Integration Test for Source Extraction (Phase 1)

Tests the complete integration of source code extraction into the
COBOL Documentation Agent.

This test:
1. Runs the agent with source extraction enabled
2. Verifies source code is extracted for appropriate sections
3. Checks the generated documentation includes source code
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path


def create_test_cobol_file(directory: Path) -> Path:
    """Create a test COBOL program for integration testing"""
    cobol_content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST-E2E-PROG.
       AUTHOR. E2E-INTEGRATION-TEST.
      *
      * This is a test program for end-to-end integration testing
      * of source code extraction in the COBOL Documentation Agent
      *
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. IBM-PC.
       OBJECT-COMPUTER. IBM-PC.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-COUNTER PIC 9(3) VALUE 0.
       01 WS-NAME    PIC X(20) VALUE SPACES.
       01 WS-RESULT  PIC 9(5) VALUE 0.
       01 WS-STATUS  PIC X(10) VALUE "INIT".

       PROCEDURE DIVISION.
       MAIN-PARA.
           DISPLAY "Starting E2E test program".
           PERFORM INITIALIZE-VARS.
           PERFORM CALCULATE-RESULT.
           PERFORM DISPLAY-RESULTS.
           STOP RUN.

       INITIALIZE-VARS.
           MOVE "TEST" TO WS-NAME.
           MOVE "READY" TO WS-STATUS.
           EXIT.

       CALCULATE-RESULT.
           MOVE 100 TO WS-COUNTER.
           COMPUTE WS-RESULT = WS-COUNTER * 2.
           EXIT.

       DISPLAY-RESULTS.
           DISPLAY "Result: " WS-RESULT.
           DISPLAY "Status: " WS-STATUS.
           EXIT.
"""

    cobol_file = directory / "TEST-E2E-PROG.c74"
    cobol_file.write_text(cobol_content)
    return cobol_file


def create_test_config(test_dir: Path, cobol_file: Path, metadata_dir: Path, docs_dir: Path) -> Path:
    """Create a test configuration file"""
    config_content = f"""# E2E Integration Test Configuration
# Testing Phase 1: Source Code Extraction

# Source files
source:
  mode: single
  source_files: {cobol_file}
  program_name: TEST-E2E-PROG

# Output paths
output:
  create_dirs: true
  metadata_dir: {metadata_dir}
  docs_path: {docs_dir}

# Metadata generation
metadata:
  generate: false  # Use existing metadata or skip
  skip_existing: true

# Source Code Extraction (Phase 1) - ENABLED
source_extraction:
  enabled: true
  compress: true

# Template
template:
  path: ./cobol-doc-template.yaml

# LLM configuration
llm:
  provider: openai
  model: gpt-4o-mini  # Use faster model for testing
  api_key: ${{OPENAI_API_KEY}}
  temperature: 0.2

# Logging
logging:
  level: info
  format: detailed
"""

    config_file = test_dir / "config-e2e-test.yaml"
    config_file.write_text(config_content)
    return config_file


def verify_source_extraction(docs_dir: Path) -> tuple[bool, list[str]]:
    """
    Verify that source code was extracted and included in documentation

    Returns:
        Tuple of (success, list of findings)
    """
    findings = []

    # Find the generated documentation file
    doc_files = list(docs_dir.glob("TEST-E2E-PROG-documentation.md"))

    if not doc_files:
        findings.append("✗ Documentation file not found")
        return False, findings

    findings.append(f"✓ Documentation file found: {doc_files[0].name}")

    # Read the documentation
    doc_content = doc_files[0].read_text()

    # Check for source code sections
    checks = [
        ("Source Code header", "## Source Code"),
        ("COBOL code block", "```cobol"),
        ("DATA DIVISION", "DATA DIVISION"),
        ("PROCEDURE DIVISION", "PROCEDURE DIVISION"),
        ("WS-COUNTER variable", "WS-COUNTER"),
        ("MAIN-PARA paragraph", "MAIN-PARA"),
        ("CALCULATE-RESULT paragraph", "CALCULATE-RESULT"),
    ]

    all_passed = True
    for check_name, search_text in checks:
        if search_text in doc_content:
            findings.append(f"✓ Found {check_name}")
        else:
            findings.append(f"✗ Missing {check_name}")
            all_passed = False

    # Check that compression worked (comments should be removed)
    if "This is a test program for end-to-end" not in doc_content:
        findings.append("✓ Source compression working (comments removed)")
    else:
        findings.append("⚠ Source compression may not be working (comments present)")

    # Count occurrences of source code sections
    source_code_count = doc_content.count("## Source Code")
    findings.append(f"✓ Found {source_code_count} source code sections")

    return all_passed, findings


def run_integration_test():
    """Run the end-to-end integration test"""
    print("=" * 70)
    print("E2E Integration Test: Source Code Extraction (Phase 1)")
    print("=" * 70)
    print()

    # Create temporary test directory
    test_dir = Path(tempfile.mkdtemp(prefix="cobol_e2e_test_"))
    print(f"Test directory: {test_dir}")
    print()

    try:
        # Create subdirectories
        metadata_dir = test_dir / "metadata"
        docs_dir = test_dir / "docs"
        metadata_dir.mkdir(exist_ok=True)
        docs_dir.mkdir(exist_ok=True)

        # Create test COBOL file
        print("1. Creating test COBOL program...")
        cobol_file = create_test_cobol_file(test_dir)
        print(f"   ✓ Created: {cobol_file.name}")
        print()

        # Create test configuration
        print("2. Creating test configuration...")
        config_file = create_test_config(test_dir, cobol_file, metadata_dir, docs_dir)
        print(f"   ✓ Created: {config_file.name}")
        print()

        # Run the documentation agent
        print("3. Running COBOL Documentation Agent...")
        print("   (This may take a minute...)")
        print()

        # Import and run the agent
        from cobol_doc_agent import generate_documentation
        from config_loader import load_config

        # Load config
        config_loader = load_config(str(config_file))
        source_config = config_loader.get_source_config()
        output_config = config_loader.get_output_config()
        metadata_config = config_loader.get_metadata_config()
        template_config = config_loader.get_template_config()
        llm_config = config_loader.get_llm_config()
        source_extraction_config = config_loader.get_source_extraction_config()

        # Generate documentation
        output_path = generate_documentation(
            program_name=source_config['program_name'],
            workspace_path=str(test_dir),
            metadata_dir=str(metadata_dir),
            template_path=template_config.get('path', './cobol-doc-template.yaml'),
            output_dir=str(docs_dir),
            generate_metadata=False,  # Skip metadata generation for faster testing
            skip_existing_metadata=True,
            cobol_file_path=str(cobol_file),
            enable_source_extraction=source_extraction_config.get('enabled', False),
            compress_source=source_extraction_config.get('compress', True),
            llm_config=llm_config
        )

        print(f"   ✓ Documentation generated: {output_path}")
        print()

        # Verify source extraction
        print("4. Verifying source code extraction...")
        success, findings = verify_source_extraction(docs_dir)

        for finding in findings:
            print(f"   {finding}")

        print()
        print("=" * 70)

        if success:
            print("✅ E2E INTEGRATION TEST PASSED")
            print()
            print("Source code extraction is successfully integrated!")
            print(f"Documentation available at: {output_path}")
            return 0
        else:
            print("❌ E2E INTEGRATION TEST FAILED")
            print()
            print("Some checks failed. Review findings above.")
            return 1

    except Exception as e:
        print()
        print("=" * 70)
        print("❌ E2E INTEGRATION TEST ERROR")
        print("=" * 70)
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

    finally:
        # Cleanup (optional - comment out to keep test files)
        # print(f"\nCleaning up test directory: {test_dir}")
        # shutil.rmtree(test_dir)
        print(f"\nTest files kept at: {test_dir}")
        print("Delete manually when done reviewing.")


if __name__ == "__main__":
    sys.exit(run_integration_test())
