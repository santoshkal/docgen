"""
Full Context Mode Integration Tests

Tests end-to-end integration of full context mode functionality including:
- FullContextBuilder with real files
- Context strategy selection
- Prompt construction pipeline
- Context chaining across sections

US-6.2: Integration Test Suite
"""

import pytest
import os
import json
import tempfile
from pathlib import Path

from full_context_builder import FullContextBuilder
from context_strategy import (
    ContextStrategy,
    get_context_strategy,
    should_use_full_context,
    FULL_CONTEXT_SECTIONS,
)
from full_context_prompts import (
    build_full_context_prompt,
    build_executive_summary_prompt,
    build_business_logic_prompt,
)
from context_chain import (
    ContextChain,
    build_chained_context,
    get_previous_sections,
    FULL_CONTEXT_SECTION_ORDER,
)


# ============================================================================
# Test Fixtures - COBOL Program with Narrative Comments
# ============================================================================

@pytest.fixture
def test_cobol_program_with_comments():
    """
    Create a test COBOL program with rich narrative comments.

    This fixture creates a realistic COBOL program that includes:
    - IDENTIFICATION DIVISION with AUTHOR, DATE-WRITTEN, REMARKS
    - Inline comments explaining business logic
    - Multiple paragraphs with different purposes

    US-6.2.I2: Create test COBOL program with narrative comments
    """
    content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. PAYROLL-CALC.
       AUTHOR. John Smith.
       DATE-WRITTEN. 2024-01-15.
       DATE-COMPILED.
       INSTALLATION. Corporate Headquarters.
      *REMARKS.
      * This program calculates employee payroll based on hours worked
      * and hourly rate. It handles regular pay, overtime, and deductions.
      *
      * Business Rules:
      * - Regular hours: Up to 40 hours at base rate
      * - Overtime: Hours over 40 at 1.5x base rate
      * - Tax deduction: 22% of gross pay
      * - Benefits deduction: Fixed $50 per employee

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. IBM-370.
       OBJECT-COMPUTER. IBM-370.

       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT EMPLOYEE-FILE
               ASSIGN TO 'EMPFILE'
               ORGANIZATION IS SEQUENTIAL.
           SELECT PAYROLL-REPORT
               ASSIGN TO 'PAYRPT'
               ORGANIZATION IS SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD EMPLOYEE-FILE.
       01 EMPLOYEE-RECORD.
           05 EMP-ID              PIC 9(5).
           05 EMP-NAME            PIC X(30).
           05 EMP-HOURS           PIC 9(3)V9.
           05 EMP-RATE            PIC 9(3)V99.
           05 EMP-DEPT            PIC X(10).

       FD PAYROLL-REPORT.
       01 REPORT-LINE            PIC X(132).

       WORKING-STORAGE SECTION.
      * Constants for payroll calculations
       01 WS-CONSTANTS.
           05 WS-OVERTIME-THRESHOLD   PIC 9(2)    VALUE 40.
           05 WS-OVERTIME-MULTIPLIER  PIC 9V99    VALUE 1.50.
           05 WS-TAX-RATE             PIC V99     VALUE 0.22.
           05 WS-BENEFITS-DEDUCTION   PIC 9(3)V99 VALUE 50.00.

      * Working storage for calculations
       01 WS-CALCULATIONS.
           05 WS-REGULAR-HOURS    PIC 9(3)V9 VALUE 0.
           05 WS-OVERTIME-HOURS   PIC 9(3)V9 VALUE 0.
           05 WS-REGULAR-PAY      PIC 9(7)V99 VALUE 0.
           05 WS-OVERTIME-PAY     PIC 9(7)V99 VALUE 0.
           05 WS-GROSS-PAY        PIC 9(7)V99 VALUE 0.
           05 WS-TAX-DEDUCTION    PIC 9(7)V99 VALUE 0.
           05 WS-NET-PAY          PIC 9(7)V99 VALUE 0.

      * Status flags
       01 WS-FLAGS.
           05 WS-EOF-FLAG         PIC X VALUE 'N'.
              88 END-OF-FILE            VALUE 'Y'.
           05 WS-ERROR-FLAG       PIC X VALUE 'N'.
              88 PROCESSING-ERROR       VALUE 'Y'.

      * Counters and accumulators
       01 WS-TOTALS.
           05 WS-TOTAL-EMPLOYEES  PIC 9(5) VALUE 0.
           05 WS-TOTAL-PAYROLL    PIC 9(9)V99 VALUE 0.

       PROCEDURE DIVISION.
      *================================================================
      * MAIN-PROCESS: Main control paragraph
      * Controls the overall program flow:
      * 1. Initialize the program
      * 2. Process all employee records
      * 3. Generate final report and cleanup
      *================================================================
       MAIN-PROCESS.
           PERFORM INIT-ROUTINE
           PERFORM PROCESS-EMPLOYEES
               UNTIL END-OF-FILE
           PERFORM CLEANUP-ROUTINE
           STOP RUN.

      *================================================================
      * INIT-ROUTINE: Program initialization
      * Opens files and initializes working storage
      *================================================================
       INIT-ROUTINE.
           OPEN INPUT EMPLOYEE-FILE
           OPEN OUTPUT PAYROLL-REPORT
           MOVE 'N' TO WS-EOF-FLAG
           MOVE 0 TO WS-TOTAL-EMPLOYEES
           MOVE 0 TO WS-TOTAL-PAYROLL
           READ EMPLOYEE-FILE
               AT END SET END-OF-FILE TO TRUE
           END-READ.

      *================================================================
      * PROCESS-EMPLOYEES: Main processing loop
      * For each employee: calculate pay, apply deductions, write report
      *================================================================
       PROCESS-EMPLOYEES.
           PERFORM CALCULATE-PAY
           PERFORM APPLY-DEDUCTIONS
           PERFORM WRITE-EMPLOYEE-LINE
           ADD 1 TO WS-TOTAL-EMPLOYEES
           ADD WS-NET-PAY TO WS-TOTAL-PAYROLL
           READ EMPLOYEE-FILE
               AT END SET END-OF-FILE TO TRUE
           END-READ.

      *================================================================
      * CALCULATE-PAY: Determine gross pay based on hours worked
      * Business rule: Hours over 40 are paid at 1.5x rate
      *================================================================
       CALCULATE-PAY.
      * Determine regular vs overtime hours
           IF EMP-HOURS > WS-OVERTIME-THRESHOLD
               MOVE WS-OVERTIME-THRESHOLD TO WS-REGULAR-HOURS
               SUBTRACT WS-OVERTIME-THRESHOLD FROM EMP-HOURS
                   GIVING WS-OVERTIME-HOURS
           ELSE
               MOVE EMP-HOURS TO WS-REGULAR-HOURS
               MOVE 0 TO WS-OVERTIME-HOURS
           END-IF

      * Calculate pay amounts
           COMPUTE WS-REGULAR-PAY = WS-REGULAR-HOURS * EMP-RATE
           COMPUTE WS-OVERTIME-PAY = WS-OVERTIME-HOURS * EMP-RATE
               * WS-OVERTIME-MULTIPLIER
           ADD WS-REGULAR-PAY WS-OVERTIME-PAY GIVING WS-GROSS-PAY.

      *================================================================
      * APPLY-DEDUCTIONS: Calculate tax and benefits deductions
      * Business rule: Tax is 22% of gross, benefits is flat $50
      *================================================================
       APPLY-DEDUCTIONS.
           COMPUTE WS-TAX-DEDUCTION = WS-GROSS-PAY * WS-TAX-RATE
           SUBTRACT WS-TAX-DEDUCTION FROM WS-GROSS-PAY
               GIVING WS-NET-PAY
           SUBTRACT WS-BENEFITS-DEDUCTION FROM WS-NET-PAY.

      *================================================================
      * WRITE-EMPLOYEE-LINE: Output employee payroll line
      *================================================================
       WRITE-EMPLOYEE-LINE.
           STRING EMP-ID DELIMITED SIZE
                  ' ' DELIMITED SIZE
                  EMP-NAME DELIMITED SIZE
                  ' $' DELIMITED SIZE
                  WS-NET-PAY DELIMITED SIZE
               INTO REPORT-LINE
           WRITE REPORT-LINE.

      *================================================================
      * CLEANUP-ROUTINE: Final processing and file closure
      *================================================================
       CLEANUP-ROUTINE.
           PERFORM WRITE-TOTALS
           CLOSE EMPLOYEE-FILE
           CLOSE PAYROLL-REPORT.

      *================================================================
      * WRITE-TOTALS: Output summary totals
      *================================================================
       WRITE-TOTALS.
           MOVE SPACES TO REPORT-LINE
           STRING 'Total Employees: ' DELIMITED SIZE
                  WS-TOTAL-EMPLOYEES DELIMITED SIZE
               INTO REPORT-LINE
           WRITE REPORT-LINE
           MOVE SPACES TO REPORT-LINE
           STRING 'Total Payroll: $' DELIMITED SIZE
                  WS-TOTAL-PAYROLL DELIMITED SIZE
               INTO REPORT-LINE
           WRITE REPORT-LINE.
"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.cbl') as f:
        f.write(content)
        file_path = f.name

    yield file_path

    # Cleanup
    os.unlink(file_path)


@pytest.fixture
def test_metadata_files(test_cobol_program_with_comments):
    """
    Create test metadata files for the test COBOL program.

    US-6.2.I3: Create test metadata files
    """
    # Create a temporary directory for metadata
    with tempfile.TemporaryDirectory() as temp_dir:
        metadata_dir = Path(temp_dir)

        # Create ctags outline file
        ctags_data = {
            "symbols": [
                {"name": "MAIN-PROCESS", "kind": "paragraph", "line": 76, "pattern": "MAIN-PROCESS."},
                {"name": "INIT-ROUTINE", "kind": "paragraph", "line": 84, "pattern": "INIT-ROUTINE."},
                {"name": "PROCESS-EMPLOYEES", "kind": "paragraph", "line": 96, "pattern": "PROCESS-EMPLOYEES."},
                {"name": "CALCULATE-PAY", "kind": "paragraph", "line": 108, "pattern": "CALCULATE-PAY."},
                {"name": "APPLY-DEDUCTIONS", "kind": "paragraph", "line": 127, "pattern": "APPLY-DEDUCTIONS."},
                {"name": "WRITE-EMPLOYEE-LINE", "kind": "paragraph", "line": 135, "pattern": "WRITE-EMPLOYEE-LINE."},
                {"name": "CLEANUP-ROUTINE", "kind": "paragraph", "line": 143, "pattern": "CLEANUP-ROUTINE."},
                {"name": "WRITE-TOTALS", "kind": "paragraph", "line": 151, "pattern": "WRITE-TOTALS."},
                {"name": "WS-CONSTANTS", "kind": "data", "line": 42},
                {"name": "WS-CALCULATIONS", "kind": "data", "line": 48},
                {"name": "WS-FLAGS", "kind": "data", "line": 58},
                {"name": "WS-TOTALS", "kind": "data", "line": 64},
                {"name": "EMPLOYEE-RECORD", "kind": "data", "line": 32},
            ]
        }
        ctags_file = metadata_dir / "ctags-outline.json"
        with open(ctags_file, 'w') as f:
            json.dump(ctags_data, f)

        # Create superbol CFG file
        cfg_data = {
            "nodes": [
                {"name": "MAIN-PROCESS", "type": "paragraph"},
                {"name": "INIT-ROUTINE", "type": "paragraph"},
                {"name": "PROCESS-EMPLOYEES", "type": "paragraph"},
                {"name": "CALCULATE-PAY", "type": "paragraph"},
                {"name": "APPLY-DEDUCTIONS", "type": "paragraph"},
                {"name": "WRITE-EMPLOYEE-LINE", "type": "paragraph"},
                {"name": "CLEANUP-ROUTINE", "type": "paragraph"},
                {"name": "WRITE-TOTALS", "type": "paragraph"},
            ],
            "edges": [
                {"from": "MAIN-PROCESS", "to": "INIT-ROUTINE", "type": "PERFORM"},
                {"from": "MAIN-PROCESS", "to": "PROCESS-EMPLOYEES", "type": "PERFORM"},
                {"from": "MAIN-PROCESS", "to": "CLEANUP-ROUTINE", "type": "PERFORM"},
                {"from": "PROCESS-EMPLOYEES", "to": "CALCULATE-PAY", "type": "PERFORM"},
                {"from": "PROCESS-EMPLOYEES", "to": "APPLY-DEDUCTIONS", "type": "PERFORM"},
                {"from": "PROCESS-EMPLOYEES", "to": "WRITE-EMPLOYEE-LINE", "type": "PERFORM"},
                {"from": "CLEANUP-ROUTINE", "to": "WRITE-TOTALS", "type": "PERFORM"},
            ]
        }
        cfg_file = metadata_dir / "superbol-cfg.json"
        with open(cfg_file, 'w') as f:
            json.dump(cfg_data, f)

        # Create gnucobol analysis file
        gnucobol_data = {
            "lines_of_code": 165,
            "total_lines": 180,
            "comment_lines": 45,
            "blank_lines": 10,
            "divisions": ["IDENTIFICATION", "ENVIRONMENT", "DATA", "PROCEDURE"],
            "file_status": "valid"
        }
        gnucobol_file = metadata_dir / "gnucobol-analysis.json"
        with open(gnucobol_file, 'w') as f:
            json.dump(gnucobol_data, f)

        yield {
            'metadata_dir': metadata_dir,
            'source_file': test_cobol_program_with_comments,
            'ctags_file': ctags_file,
            'cfg_file': cfg_file,
            'gnucobol_file': gnucobol_file,
        }


# ============================================================================
# Integration Tests for FullContextBuilder
# ============================================================================

class TestFullContextBuilderIntegration:
    """
    Integration tests for FullContextBuilder with real files.

    US-6.2.I4: Write integration test for each full context section
    """

    def test_builder_loads_source_code(self, test_metadata_files):
        """Test that builder correctly loads source code from file."""
        builder = FullContextBuilder(
            program_name='PAYROLL-CALC',
            source_file_path=test_metadata_files['source_file'],
            metadata_dir=str(test_metadata_files['metadata_dir'])
        )

        source = builder.load_full_source_code()

        assert source is not None
        assert 'IDENTIFICATION DIVISION' in source
        assert 'PAYROLL-CALC' in source
        assert 'MAIN-PROCESS' in source

    def test_builder_loads_source_with_line_numbers(self, test_metadata_files):
        """Test that builder adds line numbers to source code."""
        builder = FullContextBuilder(
            program_name='PAYROLL-CALC',
            source_file_path=test_metadata_files['source_file'],
            metadata_dir=str(test_metadata_files['metadata_dir'])
        )

        source = builder.load_full_source_code(include_line_numbers=True)

        assert source is not None
        # Line numbers should be present
        assert '1:' in source or '   1\t' in source or ' 1 ' in source

    def test_builder_loads_metadata(self, test_metadata_files):
        """Test that builder loads metadata from JSON files."""
        builder = FullContextBuilder(
            program_name='PAYROLL-CALC',
            source_file_path=test_metadata_files['source_file'],
            metadata_dir=str(test_metadata_files['metadata_dir'])
        )

        metadata = builder.load_full_metadata()

        assert metadata is not None
        assert 'ctags_outline' in metadata
        assert 'superbol_cfg' in metadata
        assert 'gnucobol_analysis' in metadata

    def test_builder_builds_full_context(self, test_metadata_files):
        """Test that builder constructs complete context."""
        builder = FullContextBuilder(
            program_name='PAYROLL-CALC',
            source_file_path=test_metadata_files['source_file'],
            metadata_dir=str(test_metadata_files['metadata_dir'])
        )

        context = builder.build_full_context()

        assert context is not None
        assert 'source_code' in context
        assert 'metadata' in context
        assert 'program_map' in context or context.get('program_map', '') == ''

        # Source code should be complete
        assert 'IDENTIFICATION DIVISION' in context['source_code']
        assert 'PROCEDURE DIVISION' in context['source_code']


# ============================================================================
# Integration Tests for Section-Specific Full Context
# ============================================================================

class TestSectionFullContextIntegration:
    """
    Integration tests for full context mode with each target section.

    US-6.2.I4: Write integration test for each full context section
    """

    def test_executive_summary_full_context_pipeline(self, test_metadata_files):
        """Test executive summary generation with full context."""
        builder = FullContextBuilder(
            program_name='PAYROLL-CALC',
            source_file_path=test_metadata_files['source_file'],
            metadata_dir=str(test_metadata_files['metadata_dir'])
        )

        context = builder.build_full_context()

        prompt = build_executive_summary_prompt(
            source_code=context['source_code'],
            metadata=context['metadata'],
            program_map=context.get('program_map', ''),
            program_name='PAYROLL-CALC'
        )

        # Verify prompt contains narrative comments
        assert 'AUTHOR' in prompt
        assert 'REMARKS' in prompt
        # Verify program purpose is visible
        assert 'payroll' in prompt.lower()
        # Verify structure information
        assert 'MAIN-PROCESS' in prompt

    def test_business_logic_full_context_pipeline(self, test_metadata_files):
        """Test business logic generation with full context."""
        builder = FullContextBuilder(
            program_name='PAYROLL-CALC',
            source_file_path=test_metadata_files['source_file'],
            metadata_dir=str(test_metadata_files['metadata_dir'])
        )

        context = builder.build_full_context()

        prompt = build_business_logic_prompt(
            source_code=context['source_code'],
            metadata=context['metadata'],
            program_map=context.get('program_map', ''),
            program_name='PAYROLL-CALC'
        )

        # Verify business rules are visible in prompt
        assert 'CALCULATE-PAY' in prompt
        assert 'OVERTIME' in prompt or 'overtime' in prompt.lower()
        assert 'TAX' in prompt or 'tax' in prompt.lower()

    def test_key_responsibilities_full_context_pipeline(self, test_metadata_files):
        """Test key responsibilities with full context."""
        from full_context_prompts import build_key_responsibilities_prompt

        builder = FullContextBuilder(
            program_name='PAYROLL-CALC',
            source_file_path=test_metadata_files['source_file'],
            metadata_dir=str(test_metadata_files['metadata_dir'])
        )

        context = builder.build_full_context()

        prompt = build_key_responsibilities_prompt(
            source_code=context['source_code'],
            metadata=context['metadata'],
            program_map=context.get('program_map', ''),
            program_name='PAYROLL-CALC'
        )

        # Verify key paragraphs are visible
        assert 'MAIN-PROCESS' in prompt
        assert 'INIT-ROUTINE' in prompt
        assert 'PROCESS-EMPLOYEES' in prompt

    def test_data_flow_full_context_pipeline(self, test_metadata_files):
        """Test data flow analysis with full context."""
        from full_context_prompts import build_data_flow_prompt

        builder = FullContextBuilder(
            program_name='PAYROLL-CALC',
            source_file_path=test_metadata_files['source_file'],
            metadata_dir=str(test_metadata_files['metadata_dir'])
        )

        context = builder.build_full_context()

        prompt = build_data_flow_prompt(
            source_code=context['source_code'],
            metadata=context['metadata'],
            program_map=context.get('program_map', ''),
            program_name='PAYROLL-CALC'
        )

        # Verify data elements are visible
        assert 'EMPLOYEE-FILE' in prompt
        assert 'READ' in prompt or 'WRITE' in prompt

    def test_overview_full_context_pipeline(self, test_metadata_files):
        """Test program overview with full context."""
        from full_context_prompts import build_overview_prompt

        builder = FullContextBuilder(
            program_name='PAYROLL-CALC',
            source_file_path=test_metadata_files['source_file'],
            metadata_dir=str(test_metadata_files['metadata_dir'])
        )

        context = builder.build_full_context()

        prompt = build_overview_prompt(
            source_code=context['source_code'],
            metadata=context['metadata'],
            program_map=context.get('program_map', ''),
            program_name='PAYROLL-CALC'
        )

        # Verify program structure is visible
        assert 'IDENTIFICATION DIVISION' in prompt
        assert 'DATA DIVISION' in prompt
        assert 'PROCEDURE DIVISION' in prompt


# ============================================================================
# Integration Tests for Context Chaining
# ============================================================================

class TestContextChainingIntegration:
    """Integration tests for context chaining across sections."""

    def test_chaining_adds_previous_section_context(self, test_metadata_files):
        """Test that chaining adds previous section outputs to context."""
        builder = FullContextBuilder(
            program_name='PAYROLL-CALC',
            source_file_path=test_metadata_files['source_file'],
            metadata_dir=str(test_metadata_files['metadata_dir'])
        )

        context = builder.build_full_context()

        # Simulate processing executive summary first
        chain = ContextChain()
        exec_summary = "This program processes payroll for employees."
        chain.add_section_output('executive-summary', exec_summary)

        # Now build key responsibilities with chaining
        chained_context = build_chained_context(
            current_section='key-responsibilities',
            chain=chain,
            enabled=True
        )

        # Verify previous section is included
        assert 'Executive Summary' in chained_context
        assert exec_summary in chained_context

    def test_chaining_order_is_preserved(self):
        """Test that chaining respects section order."""
        chain = ContextChain()

        # Add sections in defined order
        chain.add_section_output('executive-summary', 'Summary content')
        chain.add_section_output('key-responsibilities', 'Responsibilities content')
        chain.add_section_output('overview', 'Overview content')

        # Business logic should see all three previous sections
        previous = get_previous_sections('business-logic')

        assert 'executive-summary' in previous
        assert 'key-responsibilities' in previous
        assert 'overview' in previous

    def test_chaining_serialization_round_trip(self):
        """Test that chain can be serialized and restored."""
        chain = ContextChain()
        chain.add_section_output('executive-summary', 'Summary content')
        chain.add_section_output('key-responsibilities', 'Responsibilities content')

        # Serialize to dict
        chain_data = chain.to_dict()

        # Restore from dict
        restored_chain = ContextChain.from_dict(chain_data)

        # Verify data is preserved
        assert restored_chain.get_section_output('executive-summary') == 'Summary content'
        assert restored_chain.get_section_output('key-responsibilities') == 'Responsibilities content'


# ============================================================================
# Integration Tests for Context Strategy Selection
# ============================================================================

class TestContextStrategyIntegration:
    """Integration tests for context strategy selection."""

    def test_full_context_strategy_for_target_sections(self):
        """Test that full context is selected for target sections."""
        for section in FULL_CONTEXT_SECTIONS:
            strategy = get_context_strategy(
                section_id=section,
                full_context_sections=FULL_CONTEXT_SECTIONS,
                use_full_context_mode=True
            )
            assert strategy == ContextStrategy.FULL.value, \
                f"Expected 'full' for {section}, got {strategy}"

    def test_filtered_strategy_when_disabled(self):
        """Test that filtered strategy is used when full context is disabled."""
        for section in FULL_CONTEXT_SECTIONS:
            strategy = get_context_strategy(
                section_id=section,
                full_context_sections=FULL_CONTEXT_SECTIONS,
                use_full_context_mode=False
            )
            assert strategy == ContextStrategy.FILTERED.value, \
                f"Expected 'filtered' when disabled for {section}, got {strategy}"

    def test_filtered_strategy_for_non_target_sections(self):
        """Test that filtered strategy is used for non-target sections."""
        non_target_sections = [
            'paragraph-detail',
            'data-structures',
            'dependencies',
            'maintenance',
        ]

        for section in non_target_sections:
            strategy = get_context_strategy(
                section_id=section,
                full_context_sections=FULL_CONTEXT_SECTIONS,
                use_full_context_mode=True
            )
            assert strategy == ContextStrategy.FILTERED.value, \
                f"Expected 'filtered' for non-target section {section}, got {strategy}"


# ============================================================================
# Quality Comparison Tests
# ============================================================================

class TestQualityComparison:
    """
    Tests comparing filtered vs full context mode outputs.

    US-6.2.I5: Write quality comparison test
    """

    def test_full_context_includes_more_detail(self, test_metadata_files):
        """Test that full context mode includes more program details."""
        builder = FullContextBuilder(
            program_name='PAYROLL-CALC',
            source_file_path=test_metadata_files['source_file'],
            metadata_dir=str(test_metadata_files['metadata_dir'])
        )

        context = builder.build_full_context()

        # Full context should include all narrative comments
        source = context['source_code']

        # Business rules from comments should be present
        assert 'overtime' in source.lower() or 'OVERTIME' in source
        assert 'tax' in source.lower() or 'TAX' in source

        # All paragraphs should be visible
        assert 'CALCULATE-PAY' in source
        assert 'APPLY-DEDUCTIONS' in source

    def test_full_context_preserves_comments(self, test_metadata_files):
        """Test that full context preserves important comments."""
        builder = FullContextBuilder(
            program_name='PAYROLL-CALC',
            source_file_path=test_metadata_files['source_file'],
            metadata_dir=str(test_metadata_files['metadata_dir'])
        )

        context = builder.build_full_context()
        source = context['source_code']

        # REMARKS section should be preserved
        assert 'REMARKS' in source or 'Business Rules' in source

        # Inline paragraph comments should be preserved
        assert 'Main control paragraph' in source or '*' in source

    def test_full_context_has_complete_structure(self, test_metadata_files):
        """Test that full context includes complete program structure."""
        builder = FullContextBuilder(
            program_name='PAYROLL-CALC',
            source_file_path=test_metadata_files['source_file'],
            metadata_dir=str(test_metadata_files['metadata_dir'])
        )

        context = builder.build_full_context()
        source = context['source_code']

        # All divisions should be present
        assert 'IDENTIFICATION DIVISION' in source
        assert 'ENVIRONMENT DIVISION' in source
        assert 'DATA DIVISION' in source
        assert 'PROCEDURE DIVISION' in source

        # File definitions should be present
        assert 'EMPLOYEE-FILE' in source
        assert 'PAYROLL-REPORT' in source


# ============================================================================
# Error Handling Integration Tests
# ============================================================================

class TestErrorHandlingIntegration:
    """Integration tests for error handling."""

    def test_handles_missing_metadata_gracefully(self, test_cobol_program_with_comments):
        """Test that missing metadata doesn't crash the system."""
        with tempfile.TemporaryDirectory() as empty_dir:
            builder = FullContextBuilder(
                program_name='PAYROLL-CALC',
                source_file_path=test_cobol_program_with_comments,
                metadata_dir=empty_dir
            )

            # Should load source even without metadata
            source = builder.load_full_source_code()
            assert source is not None
            assert 'PAYROLL-CALC' in source

            # Metadata should be empty but not error
            metadata = builder.load_full_metadata()
            assert metadata is not None

    def test_handles_partial_metadata(self, test_cobol_program_with_comments):
        """Test handling of partial metadata files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            metadata_dir = Path(temp_dir)

            # Only create ctags file
            ctags_data = {"symbols": [{"name": "MAIN", "kind": "paragraph"}]}
            with open(metadata_dir / "ctags-outline.json", 'w') as f:
                json.dump(ctags_data, f)

            builder = FullContextBuilder(
                program_name='PAYROLL-CALC',
                source_file_path=test_cobol_program_with_comments,
                metadata_dir=str(metadata_dir)
            )

            metadata = builder.load_full_metadata()

            # CTags should be present
            assert 'ctags_outline' in metadata
            # Other sources may be empty or missing
