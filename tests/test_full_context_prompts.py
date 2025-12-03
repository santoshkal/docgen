"""
Test Suite for Full Context Prompts Module

Tests the prompt construction functions in full_context_prompts.py.
These prompts are used when full context mode is enabled for specific sections.

US-6.1.I4: Create test_full_context_prompts.py file
"""

import pytest
from full_context_prompts import (
    build_full_context_prompt,
    build_executive_summary_prompt,
    build_key_responsibilities_prompt,
    build_business_logic_prompt,
    build_overview_prompt,
    build_data_flow_prompt,
    _format_metadata_summary,
    _build_generic_full_context_prompt,
)


# Test fixtures
@pytest.fixture
def sample_source_code():
    """Sample COBOL source code for testing."""
    return """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST-PROGRAM.
       AUTHOR. Test Author.
      *REMARKS. This is a test program for documentation generation.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-COUNTER PIC 9(3) VALUE 0.
       01 WS-TOTAL PIC 9(5)V99 VALUE 0.

       PROCEDURE DIVISION.
       MAIN-PARAGRAPH.
      * Main processing paragraph
           PERFORM INIT-ROUTINE
           PERFORM PROCESS-DATA
           PERFORM CLEANUP-ROUTINE
           STOP RUN.

       INIT-ROUTINE.
      * Initialize working storage
           MOVE 0 TO WS-COUNTER
           MOVE 0 TO WS-TOTAL.

       PROCESS-DATA.
      * Process the input data
           ADD 1 TO WS-COUNTER
           ADD WS-COUNTER TO WS-TOTAL.

       CLEANUP-ROUTINE.
      * Cleanup and exit
           DISPLAY 'Total: ' WS-TOTAL."""


@pytest.fixture
def sample_metadata():
    """Sample metadata for testing."""
    return {
        'ctags_outline': {
            'symbols': [
                {'name': 'MAIN-PARAGRAPH', 'kind': 'paragraph', 'line': 12},
                {'name': 'INIT-ROUTINE', 'kind': 'paragraph', 'line': 18},
                {'name': 'PROCESS-DATA', 'kind': 'paragraph', 'line': 23},
                {'name': 'WS-COUNTER', 'kind': 'data', 'line': 8},
                {'name': 'WS-TOTAL', 'kind': 'data', 'line': 9},
            ]
        },
        'superbol_cfg': {
            'nodes': ['MAIN-PARAGRAPH', 'INIT-ROUTINE', 'PROCESS-DATA', 'CLEANUP-ROUTINE'],
            'edges': [
                {'from': 'MAIN-PARAGRAPH', 'to': 'INIT-ROUTINE'},
                {'from': 'MAIN-PARAGRAPH', 'to': 'PROCESS-DATA'},
                {'from': 'MAIN-PARAGRAPH', 'to': 'CLEANUP-ROUTINE'},
            ]
        },
        'gnucobol_analysis': {
            'lines_of_code': 30,
            'total_lines': 35,
        }
    }


@pytest.fixture
def sample_program_map():
    """Sample program map for testing."""
    return """## Program Map: TEST-PROGRAM

### Critical Elements
- MAIN-PARAGRAPH (Entry Point)
- PROCESS-DATA (Core Logic)

### Top Paragraphs
1. MAIN-PARAGRAPH (Score: 1.0) - Lines 12-17
2. INIT-ROUTINE (Score: 0.8) - Lines 18-21
3. PROCESS-DATA (Score: 0.7) - Lines 23-26

### Top Data Items
1. WS-COUNTER (Usage: 3)
2. WS-TOTAL (Usage: 2)"""


class TestBuildFullContextPromptRouting:
    """Test the main routing function."""

    def test_routes_to_executive_summary(self, sample_source_code, sample_metadata, sample_program_map):
        """Test routing to executive summary builder."""
        prompt = build_full_context_prompt(
            section_id='executive-summary',
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map,
            program_name='TEST-PROGRAM'
        )
        assert 'Executive Summary Generation' in prompt

    def test_routes_to_key_responsibilities(self, sample_source_code, sample_metadata, sample_program_map):
        """Test routing to key responsibilities builder."""
        prompt = build_full_context_prompt(
            section_id='key-responsibilities',
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map,
            program_name='TEST-PROGRAM'
        )
        assert 'Key Responsibilities Generation' in prompt

    def test_routes_to_business_logic(self, sample_source_code, sample_metadata, sample_program_map):
        """Test routing to business logic builder."""
        prompt = build_full_context_prompt(
            section_id='business-logic',
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map,
            program_name='TEST-PROGRAM'
        )
        assert 'Business Logic Explanation' in prompt

    def test_routes_to_overview(self, sample_source_code, sample_metadata, sample_program_map):
        """Test routing to overview builder."""
        prompt = build_full_context_prompt(
            section_id='overview',
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map,
            program_name='TEST-PROGRAM'
        )
        assert 'Program Overview Generation' in prompt

    def test_routes_to_data_flow(self, sample_source_code, sample_metadata, sample_program_map):
        """Test routing to data flow builder."""
        prompt = build_full_context_prompt(
            section_id='data-flow-analysis',
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map,
            program_name='TEST-PROGRAM'
        )
        assert 'Data Flow Analysis' in prompt

    def test_routes_to_generic_for_unknown_section(self, sample_source_code, sample_metadata, sample_program_map):
        """Test routing to generic builder for unknown sections."""
        prompt = build_full_context_prompt(
            section_id='unknown-section',
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map,
            program_name='TEST-PROGRAM'
        )
        assert 'Full Context Documentation Generation' in prompt

    def test_case_insensitive_routing(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that routing is case-insensitive."""
        prompt = build_full_context_prompt(
            section_id='EXECUTIVE-SUMMARY',
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map,
            program_name='TEST-PROGRAM'
        )
        assert 'Executive Summary Generation' in prompt


class TestBuildExecutiveSummaryPrompt:
    """Test the executive summary prompt builder."""

    def test_includes_program_name(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes program name."""
        prompt = build_executive_summary_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map,
            program_name='MY-PROGRAM'
        )
        assert 'MY-PROGRAM' in prompt

    def test_includes_instruction(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes custom instruction."""
        instruction = "Focus on the business purpose of this program."
        prompt = build_executive_summary_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map,
            instruction=instruction
        )
        assert instruction in prompt

    def test_includes_source_code(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes source code."""
        prompt = build_executive_summary_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'IDENTIFICATION DIVISION' in prompt
        assert 'PROCEDURE DIVISION' in prompt

    def test_includes_program_map(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes program map."""
        prompt = build_executive_summary_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'PROGRAM MAP' in prompt
        assert 'Critical Elements' in prompt

    def test_includes_metadata_summary(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes metadata summary."""
        prompt = build_executive_summary_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'METADATA SUMMARY' in prompt

    def test_includes_comment_extraction_guidance(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes guidance for comment extraction."""
        prompt = build_executive_summary_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'AUTHOR' in prompt
        assert 'REMARKS' in prompt

    def test_handles_empty_source_code(self, sample_metadata, sample_program_map):
        """Test handling of empty source code."""
        prompt = build_executive_summary_prompt(
            source_code="",
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'Executive Summary Generation' in prompt
        assert '```cobol' not in prompt


class TestBuildKeyResponsibilitiesPrompt:
    """Test the key responsibilities prompt builder."""

    def test_includes_cfg_guidance(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes CFG guidance."""
        prompt = build_key_responsibilities_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'CFG' in prompt or 'driver paragraphs' in prompt

    def test_includes_perform_guidance(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes PERFORM guidance."""
        prompt = build_key_responsibilities_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'PERFORM' in prompt

    def test_output_format_requirement(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt specifies output format."""
        prompt = build_key_responsibilities_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert '4-8 key responsibilities' in prompt


class TestBuildBusinessLogicPrompt:
    """Test the business logic prompt builder."""

    def test_includes_control_flow_guidance(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes control flow guidance."""
        prompt = build_business_logic_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'Control flow' in prompt or 'CFG' in prompt

    def test_includes_data_flow_guidance(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes data flow guidance."""
        prompt = build_business_logic_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'Data flow' in prompt or 'data is transformed' in prompt

    def test_includes_business_rule_extraction_guidance(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes business rule guidance."""
        prompt = build_business_logic_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'business rules' in prompt.lower()


class TestBuildOverviewPrompt:
    """Test the overview prompt builder."""

    def test_includes_structure_guidance(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes structure guidance."""
        prompt = build_overview_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'structure' in prompt.lower()

    def test_includes_divisions_guidance(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes divisions guidance."""
        prompt = build_overview_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'Division' in prompt

    def test_includes_external_interfaces_guidance(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes external interfaces guidance."""
        prompt = build_overview_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'External' in prompt or 'external' in prompt


class TestBuildDataFlowPrompt:
    """Test the data flow prompt builder."""

    def test_includes_data_sources_guidance(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes data sources guidance."""
        prompt = build_data_flow_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'data sources' in prompt.lower()

    def test_includes_transformation_guidance(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes transformation guidance."""
        prompt = build_data_flow_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'MOVE' in prompt or 'COMPUTE' in prompt

    def test_includes_destination_guidance(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that prompt includes destination guidance."""
        prompt = build_data_flow_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'destination' in prompt.lower() or 'output' in prompt.lower()


class TestFormatMetadataSummary:
    """Test the metadata summary formatting function."""

    def test_formats_ctags_info(self, sample_metadata):
        """Test formatting of CTags information."""
        summary = _format_metadata_summary(sample_metadata)
        assert 'CTags' in summary
        assert 'paragraphs' in summary

    def test_formats_cfg_info(self, sample_metadata):
        """Test formatting of CFG information."""
        summary = _format_metadata_summary(sample_metadata)
        assert 'Control Flow' in summary
        assert 'nodes' in summary

    def test_formats_gnucobol_info(self, sample_metadata):
        """Test formatting of GnuCOBOL information."""
        summary = _format_metadata_summary(sample_metadata)
        assert 'GnuCOBOL' in summary
        assert 'lines' in summary.lower()

    def test_handles_empty_metadata(self):
        """Test handling of empty metadata."""
        summary = _format_metadata_summary({})
        assert summary == ""

    def test_handles_partial_metadata(self):
        """Test handling of partial metadata."""
        partial_metadata = {
            'ctags_outline': {
                'symbols': [
                    {'name': 'MAIN', 'kind': 'paragraph', 'line': 1}
                ]
            }
        }
        summary = _format_metadata_summary(partial_metadata)
        assert 'CTags' in summary
        assert 'Control Flow' not in summary


class TestGenericFullContextPrompt:
    """Test the generic fallback prompt builder."""

    def test_includes_program_name(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that generic prompt includes program name."""
        prompt = _build_generic_full_context_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map,
            program_name='GENERIC-TEST'
        )
        assert 'GENERIC-TEST' in prompt

    def test_includes_source_code(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that generic prompt includes source code."""
        prompt = _build_generic_full_context_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert '```cobol' in prompt
        assert 'PROCEDURE DIVISION' in prompt

    def test_includes_program_map(self, sample_source_code, sample_metadata, sample_program_map):
        """Test that generic prompt includes program map."""
        prompt = _build_generic_full_context_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map
        )
        assert 'PROGRAM MAP' in prompt

    def test_handles_missing_program_name(self, sample_source_code, sample_metadata, sample_program_map):
        """Test handling of missing program name."""
        prompt = _build_generic_full_context_prompt(
            source_code=sample_source_code,
            metadata=sample_metadata,
            program_map=sample_program_map,
            program_name=""
        )
        assert 'UNKNOWN' in prompt


class TestPromptStructureConsistency:
    """Test that all prompts have consistent structure."""

    @pytest.fixture
    def prompt_builders(self):
        """Return all prompt builder functions."""
        return [
            build_executive_summary_prompt,
            build_key_responsibilities_prompt,
            build_business_logic_prompt,
            build_overview_prompt,
            build_data_flow_prompt,
        ]

    def test_all_prompts_include_source_code_section(
        self, prompt_builders, sample_source_code, sample_metadata, sample_program_map
    ):
        """Test that all prompts include source code section."""
        for builder in prompt_builders:
            prompt = builder(
                source_code=sample_source_code,
                metadata=sample_metadata,
                program_map=sample_program_map
            )
            assert '```cobol' in prompt, f"{builder.__name__} missing source code section"

    def test_all_prompts_include_program_map_section(
        self, prompt_builders, sample_source_code, sample_metadata, sample_program_map
    ):
        """Test that all prompts include program map section."""
        for builder in prompt_builders:
            prompt = builder(
                source_code=sample_source_code,
                metadata=sample_metadata,
                program_map=sample_program_map
            )
            assert 'PROGRAM MAP' in prompt, f"{builder.__name__} missing program map section"

    def test_all_prompts_include_output_requirements(
        self, prompt_builders, sample_source_code, sample_metadata, sample_program_map
    ):
        """Test that all prompts include output requirements."""
        for builder in prompt_builders:
            prompt = builder(
                source_code=sample_source_code,
                metadata=sample_metadata,
                program_map=sample_program_map
            )
            assert 'Output Requirements' in prompt, f"{builder.__name__} missing output requirements"

    def test_all_prompts_have_instructions_placeholder(
        self, prompt_builders, sample_source_code, sample_metadata, sample_program_map
    ):
        """Test that all prompts include instructions section."""
        for builder in prompt_builders:
            prompt = builder(
                source_code=sample_source_code,
                metadata=sample_metadata,
                program_map=sample_program_map,
                instruction="CUSTOM INSTRUCTION TEST"
            )
            assert 'CUSTOM INSTRUCTION TEST' in prompt, f"{builder.__name__} not including instruction"
