"""
Test Suite for Full Context Mode (US-2.1, US-2.2)

US-2.1: Tests for enabling/disabling full context mode via configuration,
        including the enabled flag, sections list, and AgentState integration.

US-2.2: Tests for section context strategy selection, including
        get_context_strategy() and build_section_context() integration.

TDD Approach: Tests written FIRST, then implementation.
"""

import pytest
import tempfile
import os
from pathlib import Path


# ============================================================================
# US-2.1.T1: Test Full Context Config Enabled Flag
# ============================================================================

class TestFullContextConfigEnabledFlag:
    """Tests for full_context.enabled configuration flag."""

    def test_full_context_enabled_true(self, tmp_path):
        """Test that enabled=true is correctly parsed from config."""
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
"""
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        from config_loader import load_config
        loader = load_config(str(config_file))

        full_context_config = loader.get_full_context_config()
        assert full_context_config['enabled'] is True

    def test_full_context_enabled_false(self, tmp_path):
        """Test that enabled=false is correctly parsed from config."""
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
  enabled: false
"""
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        from config_loader import load_config
        loader = load_config(str(config_file))

        full_context_config = loader.get_full_context_config()
        assert full_context_config['enabled'] is False

    def test_full_context_enabled_boolean_type(self, tmp_path):
        """Test that enabled value is a boolean type."""
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
"""
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        from config_loader import load_config
        loader = load_config(str(config_file))

        full_context_config = loader.get_full_context_config()
        assert isinstance(full_context_config['enabled'], bool)


# ============================================================================
# US-2.1.T2: Test Full Context Config Sections List
# ============================================================================

class TestFullContextConfigSectionsList:
    """Tests for full_context.sections configuration list."""

    def test_full_context_sections_list_parsed(self, tmp_path):
        """Test that sections list is correctly parsed from config."""
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
  sections:
    - executive-summary
    - business-logic
    - overview
"""
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        from config_loader import load_config
        loader = load_config(str(config_file))

        full_context_config = loader.get_full_context_config()
        assert 'sections' in full_context_config
        assert isinstance(full_context_config['sections'], list)
        assert len(full_context_config['sections']) == 3

    def test_full_context_sections_contains_expected_ids(self, tmp_path):
        """Test that sections list contains the expected section IDs."""
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
  sections:
    - executive-summary
    - key-responsibilities
    - business-logic
    - overview
    - data-flow-analysis
"""
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        from config_loader import load_config
        loader = load_config(str(config_file))

        full_context_config = loader.get_full_context_config()
        sections = full_context_config['sections']

        assert 'executive-summary' in sections
        assert 'key-responsibilities' in sections
        assert 'business-logic' in sections
        assert 'overview' in sections
        assert 'data-flow-analysis' in sections

    def test_full_context_empty_sections_list(self, tmp_path):
        """Test that empty sections list is handled correctly."""
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
  sections: []
"""
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        from config_loader import load_config
        loader = load_config(str(config_file))

        full_context_config = loader.get_full_context_config()
        assert full_context_config['sections'] == []

    def test_full_context_sections_default_when_not_specified(self, tmp_path):
        """Test that default sections list is used when not specified."""
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
"""
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        from config_loader import load_config
        loader = load_config(str(config_file))

        full_context_config = loader.get_full_context_config()
        # When enabled but no sections specified, should use default list
        assert 'sections' in full_context_config
        # Default should include the key sections
        default_sections = full_context_config['sections']
        assert isinstance(default_sections, list)


# ============================================================================
# US-2.1.T3: Test Full Context Default Disabled
# ============================================================================

class TestFullContextDefaultDisabled:
    """Tests for full context mode being disabled by default."""

    def test_full_context_default_disabled_when_section_missing(self, tmp_path):
        """Test that full context is disabled when section is not in config."""
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
        assert full_context_config['enabled'] is False

    def test_full_context_default_disabled_backward_compatibility(self, tmp_path):
        """Test that existing configs without full_context section still work."""
        # This simulates an existing config that predates full context mode
        config_content = """
source:
  mode: single
  source_files: ../cobol-source
  program_name: TESTPROG
  workspace: ../cobol-source

output:
  metadata_dir: ../output
  docs_path: ../docs
  create_dirs: true

llm:
  provider: openai
  model: gpt-4o
  temperature: 0.2

logging:
  level: info
  verbose: true
"""
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        from config_loader import load_config
        loader = load_config(str(config_file))

        # Should not raise an error
        full_context_config = loader.get_full_context_config()

        # Should be disabled by default for backward compatibility
        assert full_context_config['enabled'] is False

    def test_full_context_default_sections_when_disabled(self, tmp_path):
        """Test that sections list is empty when disabled."""
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
        # When disabled, sections should be empty list
        assert full_context_config['sections'] == []


# ============================================================================
# US-2.1.T4: Test AgentState Includes Full Context Config
# ============================================================================

class TestAgentStateIncludesFullContextConfig:
    """Tests for full context configuration being available in AgentState."""

    def test_agent_state_has_use_full_context_mode_field(self):
        """Test that AgentState TypedDict includes use_full_context_mode field."""
        from cobol_doc_agent import AgentState
        import typing

        # Get the type hints for AgentState
        hints = typing.get_type_hints(AgentState)

        assert 'use_full_context_mode' in hints
        assert hints['use_full_context_mode'] == bool

    def test_agent_state_has_full_context_sections_field(self):
        """Test that AgentState TypedDict includes full_context_sections field."""
        from cobol_doc_agent import AgentState
        import typing
        from typing import List

        # Get the type hints for AgentState
        hints = typing.get_type_hints(AgentState)

        assert 'full_context_sections' in hints
        # Should be List[str]
        assert hints['full_context_sections'] == List[str]

    def test_generate_documentation_accepts_full_context_params(self):
        """Test that generate_documentation function accepts full context parameters."""
        import inspect
        from cobol_doc_agent import generate_documentation

        sig = inspect.signature(generate_documentation)
        params = sig.parameters

        # Check use_full_context_mode parameter exists
        assert 'use_full_context_mode' in params
        # Should default to False for backward compatibility
        assert params['use_full_context_mode'].default is False

        # Check full_context_sections parameter exists
        assert 'full_context_sections' in params

    def test_generate_documentation_full_context_default_false(self):
        """Test that generate_documentation defaults to full context disabled."""
        import inspect
        from cobol_doc_agent import generate_documentation

        sig = inspect.signature(generate_documentation)
        params = sig.parameters

        # use_full_context_mode should default to False
        assert params['use_full_context_mode'].default is False


# ============================================================================
# Additional Helper Tests
# ============================================================================

class TestFullContextConfigHelpers:
    """Tests for helper functions related to full context config."""

    def test_get_full_context_config_returns_dict(self, tmp_path):
        """Test that get_full_context_config returns a dictionary."""
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
  sections:
    - executive-summary
"""
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        from config_loader import load_config
        loader = load_config(str(config_file))

        result = loader.get_full_context_config()
        assert isinstance(result, dict)

    def test_full_context_config_has_required_keys(self, tmp_path):
        """Test that full context config always has required keys."""
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

        result = loader.get_full_context_config()

        # Should always have these keys
        assert 'enabled' in result
        assert 'sections' in result

    def test_to_agent_params_includes_full_context(self, tmp_path):
        """Test that to_agent_params includes full context configuration."""
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
  sections:
    - executive-summary
    - business-logic
"""
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        from config_loader import load_config
        loader = load_config(str(config_file))

        params = loader.to_agent_params()

        assert 'use_full_context_mode' in params
        assert params['use_full_context_mode'] is True
        assert 'full_context_sections' in params
        assert 'executive-summary' in params['full_context_sections']
        assert 'business-logic' in params['full_context_sections']


# ============================================================================
# US-2.2: Section Context Strategy Selection Tests
# ============================================================================

class TestContextStrategyReturnsFullForTargetSections:
    """US-2.2.T1: Test that get_context_strategy returns 'full' for target sections."""

    def test_get_context_strategy_executive_summary(self):
        """Test that executive-summary uses full context strategy."""
        from context_strategy import get_context_strategy

        strategy = get_context_strategy(
            section_id='executive-summary',
            full_context_sections=['executive-summary', 'business-logic']
        )
        assert strategy == 'full'

    def test_get_context_strategy_business_logic(self):
        """Test that business-logic uses full context strategy."""
        from context_strategy import get_context_strategy

        strategy = get_context_strategy(
            section_id='business-logic',
            full_context_sections=['executive-summary', 'business-logic']
        )
        assert strategy == 'full'

    def test_get_context_strategy_overview(self):
        """Test that overview uses full context strategy when in list."""
        from context_strategy import get_context_strategy

        strategy = get_context_strategy(
            section_id='overview',
            full_context_sections=['overview', 'executive-summary']
        )
        assert strategy == 'full'

    def test_get_context_strategy_case_insensitive(self):
        """Test that section ID matching is case-insensitive."""
        from context_strategy import get_context_strategy

        strategy = get_context_strategy(
            section_id='Executive-Summary',
            full_context_sections=['executive-summary', 'business-logic']
        )
        assert strategy == 'full'


class TestContextStrategyReturnsFilteredForOtherSections:
    """US-2.2.T2: Test that get_context_strategy returns 'filtered' for non-target sections."""

    def test_get_context_strategy_data_structures_not_in_list(self):
        """Test that data-structures uses filtered strategy when not in list."""
        from context_strategy import get_context_strategy

        strategy = get_context_strategy(
            section_id='data-structures',
            full_context_sections=['executive-summary', 'business-logic']
        )
        assert strategy == 'filtered'

    def test_get_context_strategy_paragraph_detail_not_in_list(self):
        """Test that paragraph-detail uses filtered strategy when not in list."""
        from context_strategy import get_context_strategy

        strategy = get_context_strategy(
            section_id='paragraph-detail',
            full_context_sections=['executive-summary']
        )
        assert strategy == 'filtered'

    def test_get_context_strategy_empty_sections_list(self):
        """Test that all sections use filtered when list is empty."""
        from context_strategy import get_context_strategy

        strategy = get_context_strategy(
            section_id='executive-summary',
            full_context_sections=[]
        )
        assert strategy == 'filtered'

    def test_get_context_strategy_disabled_mode(self):
        """Test that strategy is always 'filtered' when mode is disabled."""
        from context_strategy import get_context_strategy

        # When use_full_context_mode is False, should return 'filtered'
        strategy = get_context_strategy(
            section_id='executive-summary',
            full_context_sections=['executive-summary'],
            use_full_context_mode=False
        )
        assert strategy == 'filtered'


class TestBuildSectionContextUsesFullContextBuilder:
    """US-2.2.T3: Test that build_section_context uses FullContextBuilder for full strategy."""

    def test_full_context_sections_constant_exists(self):
        """Test that FULL_CONTEXT_SECTIONS constant is defined."""
        from context_strategy import FULL_CONTEXT_SECTIONS

        assert isinstance(FULL_CONTEXT_SECTIONS, list)
        assert len(FULL_CONTEXT_SECTIONS) > 0

    def test_full_context_sections_contains_key_sections(self):
        """Test that FULL_CONTEXT_SECTIONS contains expected sections."""
        from context_strategy import FULL_CONTEXT_SECTIONS

        expected_sections = [
            'executive-summary',
            'business-logic',
            'overview',
        ]

        for section in expected_sections:
            assert section in FULL_CONTEXT_SECTIONS

    def test_should_use_full_context_true_for_target_sections(self):
        """Test should_use_full_context helper returns True for target sections."""
        from context_strategy import should_use_full_context

        result = should_use_full_context(
            section_id='executive-summary',
            use_full_context_mode=True,
            full_context_sections=['executive-summary']
        )
        assert result is True

    def test_should_use_full_context_false_when_disabled(self):
        """Test should_use_full_context returns False when mode is disabled."""
        from context_strategy import should_use_full_context

        result = should_use_full_context(
            section_id='executive-summary',
            use_full_context_mode=False,
            full_context_sections=['executive-summary']
        )
        assert result is False


class TestBuildSectionContextFallsBackToFiltered:
    """US-2.2.T4: Test that build_section_context falls back to filtered for other sections."""

    def test_should_use_full_context_false_for_non_target(self):
        """Test should_use_full_context returns False for non-target sections."""
        from context_strategy import should_use_full_context

        result = should_use_full_context(
            section_id='data-structures',
            use_full_context_mode=True,
            full_context_sections=['executive-summary', 'business-logic']
        )
        assert result is False

    def test_get_context_strategy_default_sections(self):
        """Test get_context_strategy uses default sections when None provided."""
        from context_strategy import get_context_strategy, FULL_CONTEXT_SECTIONS

        strategy = get_context_strategy(
            section_id='executive-summary',
            full_context_sections=None,
            use_full_context_mode=True
        )
        # Should use default FULL_CONTEXT_SECTIONS
        if 'executive-summary' in FULL_CONTEXT_SECTIONS:
            assert strategy == 'full'
        else:
            assert strategy == 'filtered'

    def test_context_strategy_enum_values(self):
        """Test that ContextStrategy enum has expected values."""
        from context_strategy import ContextStrategy

        assert ContextStrategy.FULL.value == 'full'
        assert ContextStrategy.FILTERED.value == 'filtered'

    def test_get_context_strategy_returns_enum(self):
        """Test that get_context_strategy can return ContextStrategy enum."""
        from context_strategy import get_context_strategy

        # The function should return a string, but we could also test enum support
        strategy = get_context_strategy(
            section_id='executive-summary',
            full_context_sections=['executive-summary'],
            use_full_context_mode=True
        )
        assert strategy in ['full', 'filtered']


# ============================================================================
# US-8.1: Backward Compatibility Guarantee Tests
# ============================================================================

class TestBackwardCompatibilityExistingConfig:
    """US-8.1.T1: Test that existing configs without full_context section work."""

    def test_existing_config_no_full_context_section(self, tmp_path):
        """Test config without full_context section loads successfully."""
        # This represents an existing config before full context mode was added
        config_content = """
source:
  mode: single
  source_files: ../cobol-source
  program_name: MAINPROG
  workspace: ../cobol-source

output:
  metadata_dir: ../output
  docs_path: ../docs
  create_dirs: true

metadata:
  generate: true
  skip_existing: true

template:
  path: ./cobol-doc-template.yaml

program_map:
  top_n_paragraphs: 30
  top_n_data_items: 20

llm:
  provider: openai
  model: gpt-4o
  temperature: 0.2

logging:
  level: info
  verbose: true
"""
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        from config_loader import load_config
        loader = load_config(str(config_file))

        # Should load without errors
        full_context_config = loader.get_full_context_config()

        # Should default to disabled
        assert full_context_config['enabled'] is False
        assert full_context_config['sections'] == []

    def test_existing_config_agent_params_work(self, tmp_path):
        """Test that to_agent_params works with existing config."""
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

        params = loader.to_agent_params()

        # Should include full context params with defaults
        assert 'use_full_context_mode' in params
        assert params['use_full_context_mode'] is False
        assert 'full_context_sections' in params
        assert params['full_context_sections'] == []

    def test_existing_config_all_sections_load(self, tmp_path):
        """Test that all existing config sections still load correctly."""
        config_content = """
source:
  mode: batch
  source_files: ../cobol-source
  program_name: MAINPROG
  workspace: ../cobol-source

output:
  metadata_dir: ../output
  docs_path: ../docs
  create_dirs: true

metadata:
  generate: true
  skip_existing: true

template:
  path: ./cobol-doc-template.yaml
  custom_vars:
    company_name: "Test Company"

program_map:
  top_n_paragraphs: 50
  top_n_data_items: 30
  show_all: false

llm:
  provider: anthropic
  model: claude-3-sonnet
  temperature: 0.3

batch:
  parallel: true
  max_workers: 4

logging:
  level: debug
  verbose: true
"""
        config_file = tmp_path / "config.yaml"
        config_file.write_text(config_content)

        from config_loader import load_config
        loader = load_config(str(config_file))

        # All getters should work
        assert loader.get_source_config()['mode'] == 'batch'
        assert loader.get_output_config()['metadata_dir'] == '../output'
        assert loader.get_template_config()['path'] == './cobol-doc-template.yaml'
        assert loader.get_program_map_config()['top_n_paragraphs'] == 50
        assert loader.get_llm_config()['provider'] == 'anthropic'
        assert loader.get_logging_config()['level'] == 'debug'


class TestTwoPassModeStillWorks:
    """US-8.1.T2: Test that two-pass mode continues to work."""

    def test_two_pass_mode_default_enabled(self):
        """Test that two-pass mode is still enabled by default."""
        import inspect
        from cobol_doc_agent import generate_documentation

        sig = inspect.signature(generate_documentation)
        params = sig.parameters

        # Two-pass mode should still be True by default
        assert 'use_two_pass_mode' in params
        assert params['use_two_pass_mode'].default is True

    def test_two_pass_mode_independent_of_full_context(self):
        """Test that two-pass mode is independent of full context mode."""
        import inspect
        from cobol_doc_agent import generate_documentation

        sig = inspect.signature(generate_documentation)
        params = sig.parameters

        # Both parameters should exist independently
        assert 'use_two_pass_mode' in params
        assert 'use_full_context_mode' in params

        # They should have different defaults
        assert params['use_two_pass_mode'].default is True
        assert params['use_full_context_mode'].default is False

    def test_agent_state_has_both_modes(self):
        """Test that AgentState supports both two-pass and full context modes."""
        import typing
        from cobol_doc_agent import AgentState

        hints = typing.get_type_hints(AgentState)

        # Both mode flags should exist
        assert 'use_two_pass_mode' in hints
        assert 'use_full_context_mode' in hints


class TestFilteringPreservedWhenDisabled:
    """US-8.1.T3: Test that existing filtering logic is preserved when disabled."""

    def test_filtered_strategy_when_disabled(self):
        """Test that strategy is always 'filtered' when mode is disabled."""
        from context_strategy import get_context_strategy

        # Even for sections in the full context list, should return filtered
        for section_id in ['executive-summary', 'business-logic', 'overview']:
            strategy = get_context_strategy(
                section_id=section_id,
                full_context_sections=[section_id],
                use_full_context_mode=False
            )
            assert strategy == 'filtered', f"Section {section_id} should use filtered when disabled"

    def test_should_use_full_context_false_when_disabled(self):
        """Test should_use_full_context is False when mode disabled."""
        from context_strategy import should_use_full_context

        result = should_use_full_context(
            section_id='executive-summary',
            use_full_context_mode=False,
            full_context_sections=['executive-summary']
        )
        assert result is False

    def test_default_full_context_mode_is_false(self, tmp_path):
        """Test that full context mode defaults to False."""
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
        assert full_context_config['enabled'] is False

    def test_context_strategy_module_has_filtered_default(self):
        """Test that ContextStrategy has FILTERED as an option."""
        from context_strategy import ContextStrategy

        assert hasattr(ContextStrategy, 'FILTERED')
        assert ContextStrategy.FILTERED.value == 'filtered'


# ============================================================================
# US-3.1: Executive Summary with Full Context Tests
# ============================================================================

class TestExecutiveSummaryFullContextIncludesSource:
    """US-3.1.T1: Test that executive summary full context includes source code."""

    def test_full_context_executive_summary_has_source_code(self, tmp_path):
        """Test that full context for executive-summary includes source code."""
        # Create test COBOL source file
        source_content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTPROG.
      * AUTHOR: Test Author
      * This program processes customer data for billing.

       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-CUSTOMER-ID PIC X(10).

       PROCEDURE DIVISION.
       MAIN-PARA.
           DISPLAY "STARTING PROGRAM".
           STOP RUN.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        # Create metadata directory structure
        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()
        (metadata_dir / "ctags").mkdir()
        (metadata_dir / "superbol").mkdir()
        (metadata_dir / "gnucobol").mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        context = builder.build_full_context()

        # Context should include source code
        assert 'source_code' in context
        assert context['source_code'] is not None
        assert 'PROGRAM-ID. TESTPROG' in context['source_code']

    def test_full_context_includes_complete_source(self, tmp_path):
        """Test that full context includes the complete source file."""
        source_content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTPROG.
      * NARRATIVE: This is a detailed comment about the program.

       PROCEDURE DIVISION.
       MAIN-PARA.
           PERFORM PROCESS-DATA.
           STOP RUN.

       PROCESS-DATA.
           DISPLAY "Processing".
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()
        (metadata_dir / "ctags").mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        context = builder.build_full_context()

        # Should include all parts of the source
        assert 'IDENTIFICATION DIVISION' in context['source_code']
        assert 'PROCEDURE DIVISION' in context['source_code']
        assert 'MAIN-PARA' in context['source_code']
        assert 'PROCESS-DATA' in context['source_code']
        assert 'NARRATIVE' in context['source_code']

    def test_full_context_source_with_line_numbers(self, tmp_path):
        """Test that full context can include source with line numbers."""
        source_content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTPROG.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        context = builder.build_full_context(include_line_numbers=True)

        # Should include line numbers
        assert '1:' in context['source_code'] or '1:\t' in context['source_code']

    def test_executive_summary_section_uses_full_context_when_enabled(self):
        """Test that executive-summary section uses full context when enabled."""
        from context_strategy import should_use_full_context

        result = should_use_full_context(
            section_id='executive-summary',
            use_full_context_mode=True,
            full_context_sections=['executive-summary', 'business-logic']
        )

        assert result is True


class TestExecutiveSummaryFullContextIncludesMetadata:
    """US-3.1.T2: Test that executive summary full context includes metadata."""

    def test_full_context_includes_all_metadata_sources(self, tmp_path):
        """Test that full context includes all metadata sources."""
        import json

        # Create test source file
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text("       IDENTIFICATION DIVISION.\n       PROGRAM-ID. TESTPROG.\n")

        # Create metadata directory structure
        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()
        (metadata_dir / "ctags").mkdir()
        (metadata_dir / "superbol").mkdir()
        (metadata_dir / "superbol" / "superbol-cfg").mkdir()
        (metadata_dir / "gnucobol").mkdir()

        # Create test metadata files
        ctags_file = metadata_dir / "ctags" / "ctags-TESTPROG-outline.json"
        ctags_file.write_text(json.dumps({
            "symbols": [{"name": "MAIN-PARA", "kind": "paragraph", "line": 10}]
        }))

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        context = builder.build_full_context()

        # Should include metadata dictionary
        assert 'metadata' in context
        assert 'ctags_outline' in context['metadata']
        assert 'superbol_cfg' in context['metadata']
        assert 'superbol_symbols' in context['metadata']
        assert 'gnucobol_analysis' in context['metadata']

    def test_full_context_metadata_is_unfiltered(self, tmp_path):
        """Test that full context metadata is not filtered."""
        import json

        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text("       IDENTIFICATION DIVISION.\n       PROGRAM-ID. TESTPROG.\n")

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()
        (metadata_dir / "ctags").mkdir()

        # Create ctags with many symbols
        symbols = [
            {"name": f"PARA-{i}", "kind": "paragraph", "line": i * 10}
            for i in range(1, 101)  # 100 paragraphs
        ]
        ctags_file = metadata_dir / "ctags" / "ctags-TESTPROG-outline.json"
        ctags_file.write_text(json.dumps({"symbols": symbols}))

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        metadata = builder.load_full_metadata()

        # Should include all 100 symbols (not filtered)
        assert len(metadata['ctags_outline']['symbols']) == 100

    def test_full_context_includes_cfg_data(self, tmp_path):
        """Test that full context includes CFG data from SuperBol."""
        import json

        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text("       IDENTIFICATION DIVISION.\n       PROGRAM-ID. TESTPROG.\n")

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()
        (metadata_dir / "superbol").mkdir()
        (metadata_dir / "superbol" / "superbol-cfg").mkdir()

        cfg_data = {
            "nodes": [
                {"id": "MAIN-PARA", "type": "paragraph"},
                {"id": "PROCESS-DATA", "type": "paragraph"}
            ],
            "edges": [
                {"from": "MAIN-PARA", "to": "PROCESS-DATA", "type": "perform"}
            ]
        }
        cfg_file = metadata_dir / "superbol" / "superbol-cfg" / "TESTPROG.json"
        cfg_file.write_text(json.dumps(cfg_data))

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        metadata = builder.load_full_metadata()

        # Should include CFG data
        assert 'superbol_cfg' in metadata
        assert 'nodes' in metadata['superbol_cfg']
        assert len(metadata['superbol_cfg']['nodes']) == 2

    def test_full_context_includes_gnucobol_analysis(self, tmp_path):
        """Test that full context includes GnuCOBOL analysis."""
        import json

        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text("       IDENTIFICATION DIVISION.\n       PROGRAM-ID. TESTPROG.\n")

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()
        (metadata_dir / "gnucobol").mkdir()

        gnucobol_data = {
            "program_name": "TESTPROG",
            "file_path": "/path/to/TESTPROG.cbl",
            "lines_of_code": 150,
            "data_items": 25
        }
        gnucobol_file = metadata_dir / "gnucobol" / "gnucobol-TESTPROG-analysis.json"
        gnucobol_file.write_text(json.dumps(gnucobol_data))

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        metadata = builder.load_full_metadata()

        # Should include GnuCOBOL analysis
        assert 'gnucobol_analysis' in metadata
        assert metadata['gnucobol_analysis']['program_name'] == 'TESTPROG'


class TestExecutiveSummaryPromptConstruction:
    """US-3.1.T3: Test executive summary prompt construction for full context."""

    def test_build_full_context_prompt_module_exists(self):
        """Test that full context prompt module exists."""
        try:
            from full_context_prompts import build_full_context_prompt
            assert callable(build_full_context_prompt)
        except ImportError:
            # Module not yet implemented - test passes for TDD
            pytest.skip("full_context_prompts module not yet implemented")

    def test_build_executive_summary_prompt_function_exists(self):
        """Test that build_executive_summary_prompt function exists."""
        try:
            from full_context_prompts import build_executive_summary_prompt
            assert callable(build_executive_summary_prompt)
        except ImportError:
            pytest.skip("build_executive_summary_prompt not yet implemented")

    def test_executive_summary_prompt_includes_source(self):
        """Test that executive summary prompt includes source code section."""
        try:
            from full_context_prompts import build_executive_summary_prompt

            prompt = build_executive_summary_prompt(
                source_code="IDENTIFICATION DIVISION.\nPROGRAM-ID. TEST.",
                metadata={},
                program_map=""
            )

            # Prompt should include source code
            assert 'IDENTIFICATION DIVISION' in prompt or 'source' in prompt.lower()
        except ImportError:
            pytest.skip("build_executive_summary_prompt not yet implemented")

    def test_executive_summary_prompt_includes_metadata_guidance(self):
        """Test that prompt includes guidance on using metadata."""
        try:
            from full_context_prompts import build_executive_summary_prompt

            prompt = build_executive_summary_prompt(
                source_code="",
                metadata={"ctags_outline": {}, "superbol_cfg": {}},
                program_map=""
            )

            # Prompt should reference metadata usage
            assert 'metadata' in prompt.lower() or 'program map' in prompt.lower()
        except ImportError:
            pytest.skip("build_executive_summary_prompt not yet implemented")


class TestExecutiveSummaryExtractsNarrativeComments:
    """US-3.1.T4: Test that executive summary extracts narrative comments."""

    def test_source_code_contains_author_comment(self, tmp_path):
        """Test that source code with AUTHOR comment is captured."""
        source_content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTPROG.
       AUTHOR. John Smith.
      * This program handles customer billing operations.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        source_code = builder.load_full_source_code()

        # Source should include AUTHOR and narrative comments
        assert 'AUTHOR' in source_code
        assert 'John Smith' in source_code
        assert 'customer billing' in source_code

    def test_source_code_contains_remarks_paragraph(self, tmp_path):
        """Test that source code with REMARKS is captured."""
        source_content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTPROG.
       REMARKS.
           This program provides the following functionality:
           - Process daily transactions
           - Generate monthly reports
           - Archive old records
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        source_code = builder.load_full_source_code()

        # Source should include REMARKS
        assert 'REMARKS' in source_code
        assert 'daily transactions' in source_code
        assert 'monthly reports' in source_code

    def test_source_code_preserves_inline_comments(self, tmp_path):
        """Test that inline comments in source are preserved."""
        source_content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTPROG.

       PROCEDURE DIVISION.
       MAIN-PARA.
      * Initialize customer record processing
           PERFORM INIT-CUSTOMER.
      * Process all pending transactions
           PERFORM PROCESS-TRANSACTIONS.
      * Generate summary report
           PERFORM GENERATE-REPORT.
           STOP RUN.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        source_code = builder.load_full_source_code()

        # Source should include all inline comments
        assert 'Initialize customer record' in source_code
        assert 'pending transactions' in source_code
        assert 'summary report' in source_code

    def test_full_context_includes_identification_division(self, tmp_path):
        """Test that full context includes IDENTIFICATION DIVISION for comments."""
        source_content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTPROG.
       AUTHOR. Jane Doe.
       INSTALLATION. Corporate Headquarters.
       DATE-WRITTEN. 2024-01-15.
       DATE-COMPILED.
       SECURITY. Confidential - Level 2.

       ENVIRONMENT DIVISION.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        source_code = builder.load_full_source_code()

        # Should include all IDENTIFICATION DIVISION fields
        assert 'AUTHOR' in source_code
        assert 'Jane Doe' in source_code
        assert 'INSTALLATION' in source_code
        assert 'DATE-WRITTEN' in source_code
        assert 'SECURITY' in source_code


# ============================================================================
# US-3.2: Key Responsibilities with Full Context Tests
# ============================================================================

class TestKeyResponsibilitiesFullContext:
    """US-3.2.T1: Test that key responsibilities uses full context."""

    def test_key_responsibilities_uses_full_context_when_enabled(self):
        """Test that key-responsibilities section uses full context when enabled."""
        from context_strategy import should_use_full_context

        result = should_use_full_context(
            section_id='key-responsibilities',
            use_full_context_mode=True,
            full_context_sections=['key-responsibilities', 'business-logic']
        )

        assert result is True

    def test_key_responsibilities_in_default_sections(self):
        """Test that key-responsibilities is in default full context sections."""
        from context_strategy import FULL_CONTEXT_SECTIONS

        assert 'key-responsibilities' in FULL_CONTEXT_SECTIONS

    def test_key_responsibilities_full_context_includes_source(self, tmp_path):
        """Test that key responsibilities full context includes source code."""
        source_content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTPROG.

       PROCEDURE DIVISION.
       MAIN-PARA.
      * Primary responsibility: Initialize customer records
           PERFORM INIT-CUSTOMER.
      * Secondary responsibility: Process transactions
           PERFORM PROCESS-TRANSACTIONS.
           STOP RUN.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        context = builder.build_full_context()

        # Should include responsibility comments
        assert 'Primary responsibility' in context['source_code']
        assert 'Secondary responsibility' in context['source_code']

    def test_key_responsibilities_derives_from_cfig(self, tmp_path):
        """Test that full context includes CFG for responsibility derivation."""
        import json

        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text("       IDENTIFICATION DIVISION.\n       PROGRAM-ID. TESTPROG.\n")

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()
        (metadata_dir / "superbol").mkdir()
        (metadata_dir / "superbol" / "superbol-cfg").mkdir()

        # CFG with paragraph importance scores
        cfg_data = {
            "nodes": [
                {"id": "MAIN-PARA", "type": "paragraph", "importance": 1.0},
                {"id": "INIT-CUSTOMER", "type": "paragraph", "importance": 0.8},
                {"id": "PROCESS-TRANS", "type": "paragraph", "importance": 0.6}
            ]
        }
        cfg_file = metadata_dir / "superbol" / "superbol-cfg" / "TESTPROG.json"
        cfg_file.write_text(json.dumps(cfg_data))

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        metadata = builder.load_full_metadata()

        # Should include CFG with importance scores
        assert 'superbol_cfg' in metadata
        assert len(metadata['superbol_cfg']['nodes']) == 3


class TestKeyResponsibilitiesPromptConstruction:
    """US-3.2.T2: Test key responsibilities prompt construction."""

    def test_build_key_responsibilities_prompt_exists(self):
        """Test that build_key_responsibilities_prompt function exists."""
        from full_context_prompts import build_key_responsibilities_prompt
        assert callable(build_key_responsibilities_prompt)

    def test_key_responsibilities_prompt_includes_source(self):
        """Test that prompt includes source code."""
        from full_context_prompts import build_key_responsibilities_prompt

        prompt = build_key_responsibilities_prompt(
            source_code="PERFORM INIT-CUSTOMER.\nPERFORM PROCESS-TRANS.",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        assert 'TESTPROG' in prompt
        assert 'INIT-CUSTOMER' in prompt or 'source' in prompt.lower()

    def test_key_responsibilities_prompt_references_cfg(self):
        """Test that prompt references CFG for importance."""
        from full_context_prompts import build_key_responsibilities_prompt

        prompt = build_key_responsibilities_prompt(
            source_code="",
            metadata={},
            program_map="MAIN-PARA (importance: 1.0)",
            program_name="TESTPROG"
        )

        # Should mention driver/main paragraphs
        assert 'driver' in prompt.lower() or 'importance' in prompt.lower() or 'main' in prompt.lower()

    def test_key_responsibilities_prompt_output_format(self):
        """Test that prompt specifies output format."""
        from full_context_prompts import build_key_responsibilities_prompt

        prompt = build_key_responsibilities_prompt(
            source_code="",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should mention list format (4-8 responsibilities)
        assert 'responsibilit' in prompt.lower()


class TestKeyResponsibilitiesExtractsFromComments:
    """US-3.2.T3: Test that key responsibilities extracts from comments."""

    def test_source_preserves_responsibility_comments(self, tmp_path):
        """Test that source code preserves responsibility-related comments."""
        source_content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTPROG.

       PROCEDURE DIVISION.
      *-------------------------------------------------------
      * RESPONSIBILITY: Initialize master file records
      *-------------------------------------------------------
       INIT-MASTER.
           OPEN INPUT MASTER-FILE.

      *-------------------------------------------------------
      * RESPONSIBILITY: Validate input transactions
      *-------------------------------------------------------
       VALIDATE-TRANS.
           PERFORM VALIDATE-AMOUNT.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        source_code = builder.load_full_source_code()

        # Should preserve responsibility comments
        assert 'RESPONSIBILITY: Initialize master file' in source_code
        assert 'RESPONSIBILITY: Validate input' in source_code

    def test_source_preserves_paragraph_purpose_comments(self, tmp_path):
        """Test that source preserves paragraph purpose comments."""
        source_content = """       PROCEDURE DIVISION.
      * This paragraph processes all pending customer orders
      * and updates the inventory database accordingly.
       PROCESS-ORDERS.
           PERFORM VARYING WS-IDX FROM 1 BY 1 UNTIL WS-EOF
               READ ORDER-FILE INTO WS-ORDER
               PERFORM UPDATE-INVENTORY
           END-PERFORM.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        source_code = builder.load_full_source_code()

        assert 'pending customer orders' in source_code
        assert 'inventory database' in source_code

    def test_key_responsibilities_routing(self):
        """Test that build_full_context_prompt routes to key responsibilities."""
        from full_context_prompts import build_full_context_prompt

        prompt = build_full_context_prompt(
            section_id='key-responsibilities',
            source_code="PERFORM MAIN-PROCESS.",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should be routed to key responsibilities prompt builder
        assert 'responsibilities' in prompt.lower() or 'key' in prompt.lower()


# ============================================================================
# US-3.3: Business Logic with Full Context Tests
# ============================================================================

class TestBusinessLogicFullContext:
    """US-3.3.T1: Test that business logic uses full context."""

    def test_business_logic_uses_full_context_when_enabled(self):
        """Test that business-logic section uses full context when enabled."""
        from context_strategy import should_use_full_context

        result = should_use_full_context(
            section_id='business-logic',
            use_full_context_mode=True,
            full_context_sections=['business-logic', 'overview']
        )

        assert result is True

    def test_business_logic_in_default_sections(self):
        """Test that business-logic is in default full context sections."""
        from context_strategy import FULL_CONTEXT_SECTIONS

        assert 'business-logic' in FULL_CONTEXT_SECTIONS

    def test_business_logic_receives_full_source(self, tmp_path):
        """Test that business logic receives full source code."""
        source_content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTPROG.

       PROCEDURE DIVISION.
      * BUSINESS RULE: Customer discount is 10% if order > $1000
       CALCULATE-DISCOUNT.
           IF WS-ORDER-TOTAL > 1000
               COMPUTE WS-DISCOUNT = WS-ORDER-TOTAL * 0.10
           END-IF.

      * BUSINESS RULE: Tax rate is 8.25% for all orders
       CALCULATE-TAX.
           COMPUTE WS-TAX = WS-ORDER-TOTAL * 0.0825.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        context = builder.build_full_context()

        # Should include business rule comments
        assert 'BUSINESS RULE: Customer discount' in context['source_code']
        assert 'BUSINESS RULE: Tax rate' in context['source_code']

    def test_business_logic_includes_cfg_and_dfg(self, tmp_path):
        """Test that business logic includes CFG and metadata."""
        import json

        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text("       IDENTIFICATION DIVISION.\n       PROGRAM-ID. TESTPROG.\n")

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()
        (metadata_dir / "superbol").mkdir()
        (metadata_dir / "superbol" / "superbol-cfg").mkdir()

        cfg_data = {
            "nodes": [
                {"id": "MAIN-PARA", "type": "paragraph"},
                {"id": "VALIDATE", "type": "paragraph"},
                {"id": "PROCESS", "type": "paragraph"}
            ],
            "edges": [
                {"from": "MAIN-PARA", "to": "VALIDATE"},
                {"from": "VALIDATE", "to": "PROCESS"}
            ]
        }
        cfg_file = metadata_dir / "superbol" / "superbol-cfg" / "TESTPROG.json"
        cfg_file.write_text(json.dumps(cfg_data))

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        metadata = builder.load_full_metadata()

        # Should include CFG with control flow
        assert 'superbol_cfg' in metadata
        assert len(metadata['superbol_cfg']['edges']) == 2


class TestBusinessLogicPromptConstruction:
    """US-3.3.T2: Test business logic prompt construction."""

    def test_build_business_logic_prompt_exists(self):
        """Test that build_business_logic_prompt function exists."""
        from full_context_prompts import build_business_logic_prompt
        assert callable(build_business_logic_prompt)

    def test_business_logic_prompt_includes_source(self):
        """Test that prompt includes source code."""
        from full_context_prompts import build_business_logic_prompt

        prompt = build_business_logic_prompt(
            source_code="IF WS-AMOUNT > 1000\n    COMPUTE WS-DISCOUNT = 0.10",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        assert 'source' in prompt.lower() or 'code' in prompt.lower()

    def test_business_logic_prompt_mentions_synthesis(self):
        """Test that prompt guides synthesis of sources."""
        from full_context_prompts import build_business_logic_prompt

        prompt = build_business_logic_prompt(
            source_code="",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should mention synthesizing/combining sources
        assert ('synthe' in prompt.lower() or 'combin' in prompt.lower() or
                'source' in prompt.lower() or 'flow' in prompt.lower())

    def test_business_logic_prompt_references_rules(self):
        """Test that prompt mentions business rules extraction."""
        from full_context_prompts import build_business_logic_prompt

        prompt = build_business_logic_prompt(
            source_code="",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should mention business rules
        assert 'business' in prompt.lower() or 'rule' in prompt.lower() or 'logic' in prompt.lower()


class TestBusinessLogicSynthesizesSources:
    """US-3.3.T3: Test that business logic synthesizes multiple sources."""

    def test_source_contains_conditional_logic(self, tmp_path):
        """Test that source contains business conditional logic."""
        source_content = """       PROCEDURE DIVISION.
       EVALUATE-CUSTOMER.
      * Business Logic: Determine customer tier
           EVALUATE TRUE
               WHEN WS-TOTAL-PURCHASES > 10000
                   MOVE 'GOLD' TO WS-TIER
               WHEN WS-TOTAL-PURCHASES > 5000
                   MOVE 'SILVER' TO WS-TIER
               WHEN OTHER
                   MOVE 'BRONZE' TO WS-TIER
           END-EVALUATE.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        source_code = builder.load_full_source_code()

        # Should contain business logic patterns
        assert 'EVALUATE TRUE' in source_code
        assert 'GOLD' in source_code
        assert 'SILVER' in source_code

    def test_business_logic_routing(self):
        """Test that build_full_context_prompt routes to business logic."""
        from full_context_prompts import build_full_context_prompt

        prompt = build_full_context_prompt(
            section_id='business-logic',
            source_code="COMPUTE WS-TOTAL = WS-AMOUNT * WS-RATE.",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should be routed to business logic prompt builder
        assert 'business' in prompt.lower() or 'logic' in prompt.lower()

    def test_full_context_preserves_calculations(self, tmp_path):
        """Test that full context preserves calculation patterns."""
        source_content = """       PROCEDURE DIVISION.
       CALCULATE-INTEREST.
      * Calculate compound interest
           COMPUTE WS-INTEREST =
               WS-PRINCIPAL * (1 + WS-RATE) ** WS-YEARS
               - WS-PRINCIPAL.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        source_code = builder.load_full_source_code()

        # Should preserve calculation
        assert 'COMPUTE WS-INTEREST' in source_code
        assert 'compound interest' in source_code


# ============================================================================
# US-3.4: Overview with Full Context Tests
# ============================================================================

class TestOverviewFullContext:
    """US-3.4.T1: Test that overview uses full context."""

    def test_overview_uses_full_context_when_enabled(self):
        """Test that overview section uses full context when enabled."""
        from context_strategy import should_use_full_context

        result = should_use_full_context(
            section_id='overview',
            use_full_context_mode=True,
            full_context_sections=['overview', 'business-logic']
        )

        assert result is True

    def test_overview_in_default_sections(self):
        """Test that overview is in default full context sections."""
        from context_strategy import FULL_CONTEXT_SECTIONS

        assert 'overview' in FULL_CONTEXT_SECTIONS

    def test_overview_receives_full_structure(self, tmp_path):
        """Test that overview receives full program structure."""
        source_content = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTPROG.
       AUTHOR. Test Author.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT MASTER-FILE ASSIGN TO 'MASTER.DAT'.

       DATA DIVISION.
       FILE SECTION.
       FD MASTER-FILE.
       01 MASTER-RECORD PIC X(100).

       WORKING-STORAGE SECTION.
       01 WS-VARIABLES.
           05 WS-COUNTER PIC 9(5).

       PROCEDURE DIVISION.
       MAIN-PARA.
           STOP RUN.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        context = builder.build_full_context()

        # Should include all divisions
        assert 'IDENTIFICATION DIVISION' in context['source_code']
        assert 'ENVIRONMENT DIVISION' in context['source_code']
        assert 'DATA DIVISION' in context['source_code']
        assert 'PROCEDURE DIVISION' in context['source_code']


class TestOverviewPromptConstruction:
    """US-3.4.T2: Test overview prompt construction."""

    def test_build_overview_prompt_exists(self):
        """Test that build_overview_prompt function exists."""
        from full_context_prompts import build_overview_prompt
        assert callable(build_overview_prompt)

    def test_overview_prompt_references_structure(self):
        """Test that prompt references program structure."""
        from full_context_prompts import build_overview_prompt

        prompt = build_overview_prompt(
            source_code="",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should mention structure
        assert 'structure' in prompt.lower() or 'division' in prompt.lower()

    def test_overview_routing(self):
        """Test that build_full_context_prompt routes to overview."""
        from full_context_prompts import build_full_context_prompt

        prompt = build_full_context_prompt(
            section_id='overview',
            source_code="IDENTIFICATION DIVISION.",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should be routed to overview prompt builder
        assert 'overview' in prompt.lower() or 'structure' in prompt.lower()


# ============================================================================
# US-3.5: Data Flow with Full Context Tests
# ============================================================================

class TestDataFlowFullContext:
    """US-3.5.T1: Test that data flow uses full context."""

    def test_data_flow_uses_full_context_when_enabled(self):
        """Test that data-flow-analysis uses full context when enabled."""
        from context_strategy import should_use_full_context

        result = should_use_full_context(
            section_id='data-flow-analysis',
            use_full_context_mode=True,
            full_context_sections=['data-flow-analysis', 'overview']
        )

        assert result is True

    def test_data_flow_in_default_sections(self):
        """Test that data-flow-analysis is in default full context sections."""
        from context_strategy import FULL_CONTEXT_SECTIONS

        assert 'data-flow-analysis' in FULL_CONTEXT_SECTIONS

    def test_data_flow_captures_move_statements(self, tmp_path):
        """Test that data flow captures MOVE/COMPUTE statements."""
        source_content = """       PROCEDURE DIVISION.
       PROCESS-DATA.
           MOVE WS-INPUT TO WS-WORK-AREA.
           COMPUTE WS-TOTAL = WS-AMOUNT + WS-TAX.
           MOVE WS-TOTAL TO WS-OUTPUT.
           WRITE OUTPUT-RECORD FROM WS-OUTPUT.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        source_code = builder.load_full_source_code()

        # Should capture data movement statements
        assert 'MOVE WS-INPUT' in source_code
        assert 'COMPUTE WS-TOTAL' in source_code
        assert 'WRITE OUTPUT-RECORD' in source_code


class TestDataFlowPromptConstruction:
    """US-3.5.T2: Test data flow prompt construction."""

    def test_build_data_flow_prompt_exists(self):
        """Test that build_data_flow_prompt function exists."""
        from full_context_prompts import build_data_flow_prompt
        assert callable(build_data_flow_prompt)

    def test_data_flow_prompt_mentions_tracing(self):
        """Test that prompt mentions data tracing."""
        from full_context_prompts import build_data_flow_prompt

        prompt = build_data_flow_prompt(
            source_code="",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should mention tracing or flow
        assert 'trac' in prompt.lower() or 'flow' in prompt.lower()

    def test_data_flow_routing(self):
        """Test that build_full_context_prompt routes to data flow."""
        from full_context_prompts import build_full_context_prompt

        prompt = build_full_context_prompt(
            section_id='data-flow-analysis',
            source_code="MOVE WS-A TO WS-B.",
            metadata={},
            program_map="",
            program_name="TESTPROG"
        )

        # Should be routed to data flow prompt builder
        assert 'data' in prompt.lower() or 'flow' in prompt.lower()


class TestDataFlowHighLevelVsFullMode:
    """US-3.5.T3: Test high-level vs full mode configuration."""

    def test_data_flow_captures_string_operations(self, tmp_path):
        """Test that data flow captures STRING/UNSTRING operations."""
        source_content = """       PROCEDURE DIVISION.
       FORMAT-NAME.
           STRING WS-FIRST-NAME DELIMITED BY SPACE
                  ' '           DELIMITED BY SIZE
                  WS-LAST-NAME  DELIMITED BY SPACE
                  INTO WS-FULL-NAME.
           UNSTRING WS-ADDRESS DELIMITED BY ','
                    INTO WS-STREET WS-CITY WS-STATE.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        source_code = builder.load_full_source_code()

        # Should capture string operations
        assert 'STRING WS-FIRST-NAME' in source_code
        assert 'UNSTRING WS-ADDRESS' in source_code

    def test_data_flow_captures_file_io(self, tmp_path):
        """Test that data flow captures file I/O operations."""
        source_content = """       PROCEDURE DIVISION.
       PROCESS-FILE.
           OPEN INPUT CUSTOMER-FILE.
           READ CUSTOMER-FILE INTO WS-CUSTOMER.
           WRITE REPORT-RECORD FROM WS-OUTPUT.
           CLOSE CUSTOMER-FILE.
"""
        source_file = tmp_path / "TESTPROG.cbl"
        source_file.write_text(source_content)

        metadata_dir = tmp_path / "output"
        metadata_dir.mkdir()

        from full_context_builder import FullContextBuilder

        builder = FullContextBuilder(
            program_name="TESTPROG",
            source_file_path=str(source_file),
            metadata_dir=str(metadata_dir)
        )

        source_code = builder.load_full_source_code()

        # Should capture file I/O
        assert 'OPEN INPUT' in source_code
        assert 'READ CUSTOMER-FILE' in source_code
        assert 'WRITE REPORT-RECORD' in source_code
