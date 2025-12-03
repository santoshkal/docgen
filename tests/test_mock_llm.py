"""
Mock LLM Tests for Full Context Mode

Tests the full context mode pipeline with mock LLM responses.
This allows testing the entire documentation generation flow without
requiring actual LLM API calls.

US-6.3: Mock LLM Tests
"""

import pytest
from typing import Any, Dict, List, Optional


# ============================================================================
# Mock LLM Class
# ============================================================================

class MockLLM:
    """
    Mock LLM for testing full context mode without API calls.

    US-6.3.I1: Create MockLLM class

    This mock simulates LLM responses by:
    - Recording prompts sent to it
    - Returning predefined responses based on section type
    - Allowing custom response configuration
    """

    def __init__(
        self,
        default_response: str = "Mock LLM response",
        responses: Optional[Dict[str, str]] = None
    ):
        """
        Initialize MockLLM.

        Args:
            default_response: Default response when no specific response is configured
            responses: Dictionary mapping prompt keywords to specific responses
        """
        self.default_response = default_response
        self.responses = responses or {}
        self.call_history: List[Dict[str, Any]] = []
        self.call_count = 0

    def invoke(self, prompt: str, **kwargs) -> str:
        """
        Simulate an LLM API call.

        Args:
            prompt: The prompt to send to the LLM
            **kwargs: Additional arguments (ignored)

        Returns:
            Mock response string
        """
        self.call_count += 1
        self.call_history.append({
            'prompt': prompt,
            'kwargs': kwargs,
            'call_number': self.call_count
        })

        # Check for keyword-based responses
        for keyword, response in self.responses.items():
            if keyword.lower() in prompt.lower():
                return response

        return self.default_response

    def get_last_prompt(self) -> Optional[str]:
        """Get the last prompt sent to the LLM."""
        if self.call_history:
            return self.call_history[-1]['prompt']
        return None

    def get_all_prompts(self) -> List[str]:
        """Get all prompts sent to the LLM."""
        return [call['prompt'] for call in self.call_history]

    def reset(self) -> None:
        """Reset call history and count."""
        self.call_history = []
        self.call_count = 0


# ============================================================================
# Mock Response Fixtures
# ============================================================================

@pytest.fixture
def mock_executive_summary_response():
    """
    Mock response for executive summary section.

    US-6.3.I2: Create mock response fixtures
    """
    return """## Executive Summary

The PAYROLL-CALC program is a batch processing application that calculates
employee payroll based on hours worked and hourly rates. Originally authored
by John Smith on January 15, 2024, this program implements core payroll
business rules including:

- Regular hour calculations (up to 40 hours)
- Overtime calculations at 1.5x the base rate
- Tax deductions at 22% of gross pay
- Fixed benefits deduction of $50 per employee

The program reads employee records from EMPFILE, processes each employee's
pay calculations, and outputs a payroll report to PAYRPT."""


@pytest.fixture
def mock_key_responsibilities_response():
    """Mock response for key responsibilities section."""
    return """## Key Responsibilities

1. **Employee Record Processing** - Read and validate employee records from
   the EMPLOYEE-FILE, handling end-of-file conditions gracefully.

2. **Pay Calculation** - Calculate regular and overtime pay based on hours
   worked, applying the 1.5x overtime multiplier for hours over 40.

3. **Deduction Application** - Apply tax deductions (22% of gross) and
   benefits deductions ($50 flat rate) to calculate net pay.

4. **Report Generation** - Generate formatted payroll report lines and
   summary totals for management review.

5. **Resource Management** - Properly initialize and close file resources,
   maintaining data integrity throughout processing."""


@pytest.fixture
def mock_business_logic_response():
    """Mock response for business logic section."""
    return """## Business Logic

### Payroll Calculation Flow

The program follows a structured approach to payroll calculation:

1. **Initialization Phase**
   - Opens EMPLOYEE-FILE for input
   - Opens PAYROLL-REPORT for output
   - Initializes accumulators to zero

2. **Main Processing Loop**
   For each employee record:
   - Determine regular vs overtime hours (threshold: 40 hours)
   - Calculate regular pay: regular_hours × hourly_rate
   - Calculate overtime pay: overtime_hours × hourly_rate × 1.5
   - Apply tax deduction: gross_pay × 0.22
   - Subtract benefits deduction: $50.00
   - Accumulate totals

3. **Business Rules**
   - Overtime threshold: 40 hours
   - Overtime multiplier: 1.5x base rate
   - Tax rate: 22% of gross pay
   - Benefits: Fixed $50 per employee"""


@pytest.fixture
def mock_llm_with_section_responses(
    mock_executive_summary_response,
    mock_key_responsibilities_response,
    mock_business_logic_response
):
    """Create a MockLLM with all section responses configured."""
    return MockLLM(
        default_response="Default mock response for unrecognized sections.",
        responses={
            'Executive Summary': mock_executive_summary_response,
            'Key Responsibilities': mock_key_responsibilities_response,
            'Business Logic': mock_business_logic_response,
        }
    )


# ============================================================================
# Tests for MockLLM Class
# ============================================================================

class TestMockLLMClass:
    """Tests for the MockLLM class itself."""

    def test_mock_llm_returns_default_response(self):
        """Test that MockLLM returns default response."""
        mock = MockLLM(default_response="Test response")
        result = mock.invoke("Any prompt")
        assert result == "Test response"

    def test_mock_llm_records_call_history(self):
        """Test that MockLLM records call history."""
        mock = MockLLM()
        mock.invoke("First prompt")
        mock.invoke("Second prompt")

        assert mock.call_count == 2
        assert len(mock.call_history) == 2
        assert mock.call_history[0]['prompt'] == "First prompt"
        assert mock.call_history[1]['prompt'] == "Second prompt"

    def test_mock_llm_returns_keyword_based_response(self):
        """Test keyword-based response selection."""
        mock = MockLLM(
            default_response="Default",
            responses={
                'executive': "Executive response",
                'business': "Business response"
            }
        )

        assert mock.invoke("Generate executive summary") == "Executive response"
        assert mock.invoke("Explain business logic") == "Business response"
        assert mock.invoke("Something else") == "Default"

    def test_mock_llm_get_last_prompt(self):
        """Test getting the last prompt."""
        mock = MockLLM()
        mock.invoke("First")
        mock.invoke("Second")
        mock.invoke("Third")

        assert mock.get_last_prompt() == "Third"

    def test_mock_llm_get_all_prompts(self):
        """Test getting all prompts."""
        mock = MockLLM()
        mock.invoke("A")
        mock.invoke("B")
        mock.invoke("C")

        assert mock.get_all_prompts() == ["A", "B", "C"]

    def test_mock_llm_reset(self):
        """Test resetting the mock."""
        mock = MockLLM()
        mock.invoke("Test")
        mock.invoke("Test2")

        mock.reset()

        assert mock.call_count == 0
        assert len(mock.call_history) == 0


# ============================================================================
# Tests Using Mock LLM with Full Context
# ============================================================================

class TestFullContextWithMockLLM:
    """
    Tests for full context mode using mock LLM.

    US-6.3.I3: Write tests using mock LLM
    """

    def test_executive_summary_prompt_sent_to_llm(self, mock_llm_with_section_responses):
        """Test that executive summary prompt is correctly formed and sent."""
        from full_context_prompts import build_executive_summary_prompt

        prompt = build_executive_summary_prompt(
            source_code="IDENTIFICATION DIVISION.\nPROGRAM-ID. TEST.",
            metadata={'ctags_outline': {'symbols': []}},
            program_map="## Program Map",
            program_name="TEST"
        )

        # Invoke mock LLM
        result = mock_llm_with_section_responses.invoke(prompt)

        # Verify the prompt was sent
        assert mock_llm_with_section_responses.call_count == 1
        last_prompt = mock_llm_with_section_responses.get_last_prompt()
        assert 'Executive Summary' in last_prompt
        assert 'TEST' in last_prompt

    def test_business_logic_prompt_includes_source(self, mock_llm_with_section_responses):
        """Test that business logic prompt includes source code."""
        from full_context_prompts import build_business_logic_prompt

        source_code = """       PROCEDURE DIVISION.
       CALCULATE-PAY.
           COMPUTE WS-PAY = WS-HOURS * WS-RATE."""

        prompt = build_business_logic_prompt(
            source_code=source_code,
            metadata={},
            program_map="",
            program_name="PAYROLL"
        )

        mock_llm_with_section_responses.invoke(prompt)

        last_prompt = mock_llm_with_section_responses.get_last_prompt()
        assert 'CALCULATE-PAY' in last_prompt
        assert 'COMPUTE' in last_prompt

    def test_key_responsibilities_uses_cfg_data(self, mock_llm_with_section_responses):
        """Test that key responsibilities prompt references CFG."""
        from full_context_prompts import build_key_responsibilities_prompt

        prompt = build_key_responsibilities_prompt(
            source_code="PROCEDURE DIVISION.\n MAIN-PARA.\n PERFORM SUB-PARA.",
            metadata={
                'superbol_cfg': {
                    'nodes': ['MAIN-PARA', 'SUB-PARA'],
                    'edges': [{'from': 'MAIN-PARA', 'to': 'SUB-PARA'}]
                }
            },
            program_map="## Program Map\n- MAIN-PARA",
            program_name="TEST"
        )

        mock_llm_with_section_responses.invoke(prompt)

        last_prompt = mock_llm_with_section_responses.get_last_prompt()
        assert 'Key Responsibilities' in last_prompt
        assert 'MAIN-PARA' in last_prompt

    def test_mock_llm_response_matches_section(self, mock_llm_with_section_responses):
        """Test that mock returns appropriate response for each section."""
        from full_context_prompts import build_executive_summary_prompt

        prompt = build_executive_summary_prompt(
            source_code="",
            metadata={},
            program_map="",
            program_name="TEST"
        )

        result = mock_llm_with_section_responses.invoke(prompt)

        # Should match executive summary response
        assert 'PAYROLL-CALC' in result
        assert 'batch processing' in result

    def test_multiple_section_calls_recorded(self, mock_llm_with_section_responses):
        """Test that multiple section calls are recorded."""
        from full_context_prompts import (
            build_executive_summary_prompt,
            build_key_responsibilities_prompt,
            build_business_logic_prompt,
        )

        # Build and invoke prompts for multiple sections
        exec_prompt = build_executive_summary_prompt("", {}, "", "TEST")
        resp_prompt = build_key_responsibilities_prompt("", {}, "", "TEST")
        logic_prompt = build_business_logic_prompt("", {}, "", "TEST")

        mock_llm_with_section_responses.invoke(exec_prompt)
        mock_llm_with_section_responses.invoke(resp_prompt)
        mock_llm_with_section_responses.invoke(logic_prompt)

        assert mock_llm_with_section_responses.call_count == 3
        prompts = mock_llm_with_section_responses.get_all_prompts()
        assert len(prompts) == 3


class TestContextChainingWithMockLLM:
    """Test context chaining with mock LLM responses."""

    def test_chained_context_includes_previous_llm_output(self):
        """Test that chaining includes previous LLM outputs."""
        from context_chain import ContextChain, build_chained_context

        # Simulate LLM generating executive summary
        mock = MockLLM(default_response="Mock executive summary content")
        exec_summary_result = mock.invoke("Generate executive summary")

        # Store in chain
        chain = ContextChain()
        chain.add_section_output('executive-summary', exec_summary_result)

        # Build chained context for next section
        chained = build_chained_context(
            current_section='key-responsibilities',
            chain=chain,
            enabled=True
        )

        # Verify previous output is included
        assert 'Mock executive summary content' in chained
        assert 'Executive Summary' in chained

    def test_chain_accumulates_across_sections(self):
        """Test that chain accumulates outputs across multiple sections."""
        from context_chain import ContextChain, build_chained_context, FULL_CONTEXT_SECTION_ORDER

        mock = MockLLM()
        chain = ContextChain()

        # Simulate processing first three sections
        for i, section in enumerate(FULL_CONTEXT_SECTION_ORDER[:3]):
            response = mock.invoke(f"Generate {section}")
            chain.add_section_output(section, f"Content for {section}")

        # Check chaining for 4th section
        fourth_section = FULL_CONTEXT_SECTION_ORDER[3]
        chained = build_chained_context(
            current_section=fourth_section,
            chain=chain,
            enabled=True
        )

        # All three previous sections should be in chain
        for section in FULL_CONTEXT_SECTION_ORDER[:3]:
            assert f"Content for {section}" in chained


class TestPromptQualityWithMockLLM:
    """Test prompt quality using mock LLM."""

    def test_prompt_contains_all_required_context(self):
        """Test that prompt contains source, metadata, and program map."""
        from full_context_prompts import build_full_context_prompt

        mock = MockLLM()

        prompt = build_full_context_prompt(
            section_id='executive-summary',
            source_code="PROGRAM-ID. TEST.",
            metadata={'key': 'value'},
            program_map="## Map content",
            program_name="TEST"
        )

        mock.invoke(prompt)
        sent_prompt = mock.get_last_prompt()

        # All context components should be present
        assert 'PROGRAM-ID. TEST.' in sent_prompt
        assert 'Map content' in sent_prompt
        assert 'TEST' in sent_prompt

    def test_prompt_has_clear_section_markers(self):
        """Test that prompt has clear section markers."""
        from full_context_prompts import build_full_context_prompt

        mock = MockLLM()

        prompt = build_full_context_prompt(
            section_id='business-logic',
            source_code="SOURCE CODE",
            metadata={},
            program_map="PROGRAM MAP",
            program_name="TEST"
        )

        mock.invoke(prompt)
        sent_prompt = mock.get_last_prompt()

        # Should have clear markers
        assert 'Business Logic' in sent_prompt or 'BUSINESS LOGIC' in sent_prompt.upper()
        assert '---' in sent_prompt  # Section separators

    def test_prompt_includes_instructions(self):
        """Test that prompt includes instructions."""
        from full_context_prompts import build_full_context_prompt

        mock = MockLLM()

        custom_instruction = "Focus on data validation rules"
        prompt = build_full_context_prompt(
            section_id='business-logic',
            source_code="",
            metadata={},
            program_map="",
            instruction=custom_instruction,
            program_name="TEST"
        )

        mock.invoke(prompt)
        sent_prompt = mock.get_last_prompt()

        assert custom_instruction in sent_prompt
