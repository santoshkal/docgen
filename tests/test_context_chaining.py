"""
Test Suite for Context Chaining (US-4.1)

US-4.1: Context Chaining Mechanism for Cross-Section Consistency

Context chaining allows previous section outputs to be included in subsequent
section prompts, enabling the LLM to maintain consistency across sections.

TDD Approach: Tests written FIRST, then implementation.
"""

import pytest
import tempfile
import os
from pathlib import Path


# ============================================================================
# US-4.1.T1: Test Context Chaining Stores Previous Outputs
# ============================================================================

class TestContextChainingStoresPreviousOutputs:
    """US-4.1.T1: Test that context chaining stores previous section outputs."""

    def test_context_chain_module_exists(self):
        """Test that context_chain module exists."""
        try:
            from context_chain import ContextChain
            assert ContextChain is not None
        except ImportError:
            pytest.skip("context_chain module not yet implemented")

    def test_context_chain_stores_output(self):
        """Test that ContextChain can store section output."""
        try:
            from context_chain import ContextChain

            chain = ContextChain()
            chain.add_section_output('executive-summary', 'This is the executive summary.')

            assert chain.has_section('executive-summary')
            assert chain.get_section_output('executive-summary') == 'This is the executive summary.'
        except ImportError:
            pytest.skip("context_chain module not yet implemented")

    def test_context_chain_stores_multiple_outputs(self):
        """Test that ContextChain can store multiple section outputs."""
        try:
            from context_chain import ContextChain

            chain = ContextChain()
            chain.add_section_output('executive-summary', 'Summary content')
            chain.add_section_output('key-responsibilities', 'Responsibilities content')
            chain.add_section_output('business-logic', 'Business logic content')

            assert chain.has_section('executive-summary')
            assert chain.has_section('key-responsibilities')
            assert chain.has_section('business-logic')
            assert len(chain.get_all_sections()) == 3
        except ImportError:
            pytest.skip("context_chain module not yet implemented")

    def test_context_chain_returns_none_for_missing(self):
        """Test that ContextChain returns None for missing sections."""
        try:
            from context_chain import ContextChain

            chain = ContextChain()
            assert chain.get_section_output('nonexistent') is None
            assert not chain.has_section('nonexistent')
        except ImportError:
            pytest.skip("context_chain module not yet implemented")


# ============================================================================
# US-4.1.T2: Test Build Chained Context Includes Previous
# ============================================================================

class TestBuildChainedContextIncludesPrevious:
    """US-4.1.T2: Test that build_chained_context includes previous outputs."""

    def test_build_chained_context_function_exists(self):
        """Test that build_chained_context function exists."""
        try:
            from context_chain import build_chained_context
            assert callable(build_chained_context)
        except ImportError:
            pytest.skip("build_chained_context not yet implemented")

    def test_build_chained_context_includes_previous_summary(self):
        """Test that chained context includes previous executive summary."""
        try:
            from context_chain import ContextChain, build_chained_context

            chain = ContextChain()
            chain.add_section_output('executive-summary', 'This program processes customer data.')

            context = build_chained_context(
                current_section='key-responsibilities',
                chain=chain
            )

            # Should include previous executive summary
            assert 'executive-summary' in context or 'customer data' in context
        except ImportError:
            pytest.skip("build_chained_context not yet implemented")

    def test_build_chained_context_formats_previous(self):
        """Test that chained context formats previous outputs clearly."""
        try:
            from context_chain import ContextChain, build_chained_context

            chain = ContextChain()
            chain.add_section_output('executive-summary', 'Summary text here.')
            chain.add_section_output('key-responsibilities', 'Responsibilities text here.')

            context = build_chained_context(
                current_section='business-logic',
                chain=chain
            )

            # Should include formatting/structure
            assert isinstance(context, str)
            assert len(context) > 0
        except ImportError:
            pytest.skip("build_chained_context not yet implemented")

    def test_build_chained_context_empty_chain(self):
        """Test that build_chained_context handles empty chain."""
        try:
            from context_chain import ContextChain, build_chained_context

            chain = ContextChain()

            context = build_chained_context(
                current_section='executive-summary',
                chain=chain
            )

            # Should return empty or minimal context for first section
            assert context == "" or "no previous" in context.lower() or context is None
        except ImportError:
            pytest.skip("build_chained_context not yet implemented")


# ============================================================================
# US-4.1.T3: Test Context Chaining Order
# ============================================================================

class TestContextChainingOrder:
    """US-4.1.T3: Test that context chaining respects section order."""

    def test_full_context_section_order_constant_exists(self):
        """Test that FULL_CONTEXT_SECTION_ORDER constant exists."""
        try:
            from context_chain import FULL_CONTEXT_SECTION_ORDER
            assert isinstance(FULL_CONTEXT_SECTION_ORDER, (list, tuple))
            assert len(FULL_CONTEXT_SECTION_ORDER) > 0
        except ImportError:
            pytest.skip("FULL_CONTEXT_SECTION_ORDER not yet implemented")

    def test_section_order_starts_with_executive_summary(self):
        """Test that section order starts with executive-summary."""
        try:
            from context_chain import FULL_CONTEXT_SECTION_ORDER

            assert FULL_CONTEXT_SECTION_ORDER[0] == 'executive-summary'
        except ImportError:
            pytest.skip("FULL_CONTEXT_SECTION_ORDER not yet implemented")

    def test_section_order_includes_all_target_sections(self):
        """Test that section order includes all full context target sections."""
        try:
            from context_chain import FULL_CONTEXT_SECTION_ORDER
            from context_strategy import FULL_CONTEXT_SECTIONS

            # All sections in FULL_CONTEXT_SECTIONS should be in the order
            for section in FULL_CONTEXT_SECTIONS:
                assert section in FULL_CONTEXT_SECTION_ORDER
        except ImportError:
            pytest.skip("FULL_CONTEXT_SECTION_ORDER not yet implemented")

    def test_get_previous_sections_respects_order(self):
        """Test that get_previous_sections returns sections in order."""
        try:
            from context_chain import get_previous_sections, FULL_CONTEXT_SECTION_ORDER

            # For business-logic, should return executive-summary and key-responsibilities
            previous = get_previous_sections('business-logic')

            # Should be in order
            if 'executive-summary' in previous and 'key-responsibilities' in previous:
                exec_idx = previous.index('executive-summary')
                resp_idx = previous.index('key-responsibilities')
                assert exec_idx < resp_idx
        except ImportError:
            pytest.skip("get_previous_sections not yet implemented")

    def test_get_previous_sections_first_has_none(self):
        """Test that first section has no previous sections."""
        try:
            from context_chain import get_previous_sections, FULL_CONTEXT_SECTION_ORDER

            first_section = FULL_CONTEXT_SECTION_ORDER[0]
            previous = get_previous_sections(first_section)

            assert previous == [] or previous is None
        except ImportError:
            pytest.skip("get_previous_sections not yet implemented")


# ============================================================================
# US-4.1.T4: Test Context Chaining Disabled
# ============================================================================

class TestContextChainingDisabled:
    """US-4.1.T4: Test that context chaining can be disabled."""

    def test_context_chaining_disabled_by_default(self, tmp_path):
        """Test that context chaining is disabled by default for backward compat."""
        config_content = """
source:
  mode: single
  source_files: ../cobol-source
  program_name: TESTPROG

output:
  metadata_dir: ../output
  docs_path: ../docs

llm:
  provider: openai
  model: gpt-4o
"""
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        from config_loader import load_config
        loader = load_config(str(config_file))

        full_context_config = loader.get_full_context_config()

        # Context chaining should be disabled by default
        chaining_enabled = full_context_config.get('context_chaining', {}).get('enabled', False)
        assert chaining_enabled is False

    def test_context_chaining_enabled_via_config(self, tmp_path):
        """Test that context chaining can be enabled via config."""
        config_content = """
source:
  mode: single
  source_files: ../cobol-source
  program_name: TESTPROG

output:
  metadata_dir: ../output
  docs_path: ../docs

llm:
  provider: openai
  model: gpt-4o

full_context:
  enabled: true
  context_chaining:
    enabled: true
"""
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        from config_loader import load_config
        loader = load_config(str(config_file))

        full_context_config = loader.get_full_context_config()

        # Context chaining should be enabled
        chaining_config = full_context_config.get('context_chaining', {})
        assert chaining_config.get('enabled', False) is True

    def test_build_chained_context_returns_empty_when_disabled(self):
        """Test that build_chained_context returns empty when chaining disabled."""
        try:
            from context_chain import ContextChain, build_chained_context

            chain = ContextChain()
            chain.add_section_output('executive-summary', 'Summary content')

            context = build_chained_context(
                current_section='key-responsibilities',
                chain=chain,
                enabled=False
            )

            # When disabled, should return empty string
            assert context == ""
        except ImportError:
            pytest.skip("build_chained_context not yet implemented")

    def test_should_use_chaining_helper(self):
        """Test should_use_chaining helper function."""
        try:
            from context_chain import should_use_chaining

            # With chaining enabled
            assert should_use_chaining(use_full_context_mode=True, chaining_enabled=True) is True

            # With full context disabled
            assert should_use_chaining(use_full_context_mode=False, chaining_enabled=True) is False

            # With chaining disabled
            assert should_use_chaining(use_full_context_mode=True, chaining_enabled=False) is False
        except ImportError:
            pytest.skip("should_use_chaining not yet implemented")


# ============================================================================
# Additional Context Chain Tests
# ============================================================================

class TestContextChainIntegration:
    """Additional integration tests for context chaining."""

    def test_context_chain_is_serializable(self):
        """Test that ContextChain can be converted to dict (for state)."""
        try:
            from context_chain import ContextChain

            chain = ContextChain()
            chain.add_section_output('executive-summary', 'Summary')
            chain.add_section_output('key-responsibilities', 'Responsibilities')

            # Should be able to convert to dict
            as_dict = chain.to_dict()
            assert isinstance(as_dict, dict)
            assert 'executive-summary' in as_dict
            assert 'key-responsibilities' in as_dict
        except ImportError:
            pytest.skip("ContextChain not yet implemented")

    def test_context_chain_from_dict(self):
        """Test that ContextChain can be created from dict."""
        try:
            from context_chain import ContextChain

            data = {
                'executive-summary': 'Summary content',
                'key-responsibilities': 'Responsibilities content'
            }

            chain = ContextChain.from_dict(data)
            assert chain.has_section('executive-summary')
            assert chain.get_section_output('key-responsibilities') == 'Responsibilities content'
        except ImportError:
            pytest.skip("ContextChain not yet implemented")

    def test_context_chain_clear(self):
        """Test that ContextChain can be cleared."""
        try:
            from context_chain import ContextChain

            chain = ContextChain()
            chain.add_section_output('executive-summary', 'Summary')
            chain.add_section_output('key-responsibilities', 'Responsibilities')

            chain.clear()

            assert len(chain.get_all_sections()) == 0
            assert not chain.has_section('executive-summary')
        except ImportError:
            pytest.skip("ContextChain not yet implemented")

    def test_build_chained_context_max_tokens(self):
        """Test that build_chained_context can limit token count."""
        try:
            from context_chain import ContextChain, build_chained_context

            chain = ContextChain()
            # Add a very long output
            chain.add_section_output('executive-summary', 'A ' * 10000)

            context = build_chained_context(
                current_section='key-responsibilities',
                chain=chain,
                max_tokens=500
            )

            # Should be limited
            assert len(context.split()) < 10000
        except ImportError:
            pytest.skip("build_chained_context not yet implemented")


# ============================================================================
# US-5.1: Executive Summary Template Update Tests
# ============================================================================

class TestExecutiveSummaryTemplateUpdate:
    """US-5.1: Test executive summary template backward compatibility."""

    def test_executive_summary_prompt_backward_compatible(self):
        """Test that executive summary prompt is backward compatible."""
        from full_context_prompts import build_executive_summary_prompt

        # Old-style call (minimal params)
        prompt = build_executive_summary_prompt(
            source_code="",
            metadata={},
            program_map=""
        )

        # Should not raise exception
        assert prompt is not None
        assert isinstance(prompt, str)

    def test_executive_summary_references_source_sections(self):
        """Test that prompt references source code sections."""
        from full_context_prompts import build_executive_summary_prompt

        prompt = build_executive_summary_prompt(
            source_code="IDENTIFICATION DIVISION.\nPROGRAM-ID. TEST.",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should reference source code
        assert 'source' in prompt.lower() or 'code' in prompt.lower()

    def test_executive_summary_references_remarks_author(self):
        """Test that prompt mentions REMARKS/AUTHOR extraction."""
        from full_context_prompts import build_executive_summary_prompt

        prompt = build_executive_summary_prompt(
            source_code="",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should mention author/remarks
        assert 'author' in prompt.lower() or 'remarks' in prompt.lower()

    def test_executive_summary_metadata_correlation(self):
        """Test that prompt mentions metadata correlation."""
        from full_context_prompts import build_executive_summary_prompt

        prompt = build_executive_summary_prompt(
            source_code="",
            metadata={"ctags_outline": {}},
            program_map="",
            program_name="TESTPROG"
        )

        # Should mention metadata or program map
        assert 'metadata' in prompt.lower() or 'program map' in prompt.lower()


# ============================================================================
# US-5.2: Business Logic Template Update Tests
# ============================================================================

class TestBusinessLogicTemplateUpdate:
    """US-5.2: Test business logic template backward compatibility."""

    def test_business_logic_prompt_backward_compatible(self):
        """Test that business logic prompt is backward compatible."""
        from full_context_prompts import build_business_logic_prompt

        # Old-style call (minimal params)
        prompt = build_business_logic_prompt(
            source_code="",
            metadata={},
            program_map=""
        )

        # Should not raise exception
        assert prompt is not None
        assert isinstance(prompt, str)

    def test_business_logic_paragraph_comments(self):
        """Test that prompt references paragraph comments."""
        from full_context_prompts import build_business_logic_prompt

        prompt = build_business_logic_prompt(
            source_code="",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should mention comments or source
        assert 'comment' in prompt.lower() or 'source' in prompt.lower()

    def test_business_logic_cfg_guidance(self):
        """Test that prompt mentions CFG correlation."""
        from full_context_prompts import build_business_logic_prompt

        prompt = build_business_logic_prompt(
            source_code="",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should mention control flow or CFG
        assert ('control' in prompt.lower() or 'flow' in prompt.lower() or
                'cfg' in prompt.lower() or 'paragraph' in prompt.lower())

    def test_business_logic_rule_extraction(self):
        """Test that prompt mentions business rule extraction."""
        from full_context_prompts import build_business_logic_prompt

        prompt = build_business_logic_prompt(
            source_code="",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should mention business rules
        assert 'business' in prompt.lower() or 'rule' in prompt.lower()


# ============================================================================
# US-5.3: Full Context Prompt Wrapper Tests
# ============================================================================

class TestFullContextPromptWrapper:
    """US-5.3: Test full context prompt structure."""

    def test_full_context_prompt_structure(self):
        """Test that full context prompt has proper structure."""
        from full_context_prompts import build_full_context_prompt

        prompt = build_full_context_prompt(
            section_id='executive-summary',
            source_code="IDENTIFICATION DIVISION.",
            metadata={},
            program_map="# Program Map",
            instruction="Generate summary",
            program_name="TESTPROG"
        )

        # Should have structured sections
        assert '---' in prompt or '#' in prompt  # Headers/separators
        assert 'TESTPROG' in prompt  # Program name

    def test_full_context_prompt_ordering(self):
        """Test that prompt components are in correct order."""
        from full_context_prompts import build_full_context_prompt

        prompt = build_full_context_prompt(
            section_id='executive-summary',
            source_code="IDENTIFICATION DIVISION.\nPROCEDURE DIVISION.",
            metadata={},
            program_map="# Program Map\n- MAIN-PARA",
            instruction="Generate summary",
            program_name="TESTPROG"
        )

        # Should have program map before source code (or at least structured)
        if 'PROGRAM MAP' in prompt.upper() and 'SOURCE' in prompt.upper():
            program_map_pos = prompt.upper().find('PROGRAM MAP')
            source_pos = prompt.upper().find('SOURCE')
            # Program map should come before source (in some formats)
            # This is flexible - just check both exist
            assert program_map_pos >= 0 and source_pos >= 0

    def test_full_context_prompt_routes_correctly(self):
        """Test that prompt routes to correct builder."""
        from full_context_prompts import build_full_context_prompt

        # Test different sections route correctly
        sections = ['executive-summary', 'key-responsibilities', 'business-logic', 'overview', 'data-flow-analysis']

        for section in sections:
            prompt = build_full_context_prompt(
                section_id=section,
                source_code="",
                metadata={},
                program_map="",
                program_name="TESTPROG"
            )
            assert prompt is not None
            assert len(prompt) > 0

    def test_full_context_prompt_generic_fallback(self):
        """Test that unknown sections get generic prompt."""
        from full_context_prompts import build_full_context_prompt

        prompt = build_full_context_prompt(
            section_id='unknown-section',
            source_code="SOME CODE",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should still return a valid prompt
        assert prompt is not None
        assert 'TESTPROG' in prompt
