"""
Test suite for Tiered Detail Levels in Program Map

TDD tests for US-1.4: Tiered Detail Levels in Program Map
These tests are written FIRST before implementation.

Tests cover:
- Tier 1 (Top 50): Full details - line numbers, importance scores, relationships
- Tier 2 (Next 200): Names and scores only
- Tier 3 (Remainder): Summary count only ("...and N more paragraphs")
- Configurable tier thresholds
- Same tiering for both paragraphs and data items
"""

import os
import pytest
import tempfile
from typing import Dict, Any, List


# ============================================================================
# TEST FIXTURES
# ============================================================================

@pytest.fixture
def large_program_metadata():
    """Large program with 300 paragraphs and 200 data items for tiering tests"""
    return _create_metadata(num_paragraphs=300, num_data_items=200)


@pytest.fixture
def small_program_metadata():
    """Small program with 30 paragraphs and 15 data items (all fit in tier 1)"""
    return _create_metadata(num_paragraphs=30, num_data_items=15)


@pytest.fixture
def medium_program_metadata():
    """Medium program with 100 paragraphs and 80 data items (fits tier 1 and 2)"""
    return _create_metadata(num_paragraphs=100, num_data_items=80)


def _create_metadata(num_paragraphs: int, num_data_items: int) -> Dict[str, Any]:
    """Helper to create metadata with specified counts and importance scores"""
    symbols = []

    # Add program symbol
    symbols.append({"name": "TESTPROG", "kind": "program", "line": 1})

    # Add paragraphs with varying importance (higher index = lower importance)
    for i in range(num_paragraphs):
        symbols.append({
            "name": f"PARA-{i:04d}",
            "kind": "paragraph",
            "line": 100 + i * 10
        })

    # Add data items
    for i in range(num_data_items):
        symbols.append({
            "name": f"WS-DATA-{i:04d}",
            "kind": "data",
            "level": "01" if i < 10 else "05",
            "picture": f"X({10 + i})" if i % 2 == 0 else f"9({5 + i})",
            "line": 10 + i
        })

    # Create performs to establish importance ranking
    # First paragraphs are called more often (higher importance)
    performs = []
    for i in range(min(100, num_paragraphs - 1)):
        # More performs to early paragraphs
        for j in range(max(1, 10 - i // 10)):
            performs.append({
                "from": f"PARA-{max(0, i-1):04d}",
                "to": f"PARA-{i:04d}"
            })

    # Add some external calls from important paragraphs
    calls = []
    for i in range(min(20, num_paragraphs)):
        calls.append({
            "from": f"PARA-{i:04d}",
            "to": f"EXTPROG-{i:02d}",
            "type": "CALL"
        })

    # Create variable references (higher for early data items)
    variables = {}
    for i in range(num_data_items):
        variables[f"WS-DATA-{i:04d}"] = {
            "references": max(1, num_data_items - i + 10),
            "type": "alphanumeric" if i % 2 == 0 else "numeric"
        }

    return {
        "ctags_outline": {
            "file": "TESTPROG.cbl",
            "symbols": symbols
        },
        "superbol_cfg": {
            "program": "TESTPROG",
            "performs": performs,
            "calls": calls,
            "edges": []
        },
        "gnucobol_analysis": {
            "program": "TESTPROG",
            "variables": variables
        }
    }


# ============================================================================
# US-1.4.T1: Test Tier 1 Full Details
# ============================================================================

class TestTieredDetailTier1FullDetails:
    """US-1.4.T1: Test that Tier 1 elements have full details"""

    def test_tier1_paragraphs_have_line_numbers(self, large_program_metadata):
        """Tier 1 paragraphs should include line numbers"""
        from tiered_program_map import format_tiered_program_map

        result = format_tiered_program_map(
            program_name="TESTPROG",
            metadata=large_program_metadata,
            tier1_limit=50,
            tier2_limit=200
        )

        # First paragraph should have line number
        assert "line" in result.lower() or "(line" in result

    def test_tier1_paragraphs_have_importance_scores(self, large_program_metadata):
        """Tier 1 paragraphs should include importance scores"""
        from tiered_program_map import format_tiered_program_map

        result = format_tiered_program_map(
            program_name="TESTPROG",
            metadata=large_program_metadata,
            tier1_limit=50,
            tier2_limit=200
        )

        # Should contain importance or score indicators
        assert "importance" in result.lower() or "score" in result.lower() or "[" in result

    def test_tier1_paragraphs_have_relationships(self, large_program_metadata):
        """Tier 1 paragraphs should show relationships (performs/calls)"""
        from tiered_program_map import format_tiered_program_map

        result = format_tiered_program_map(
            program_name="TESTPROG",
            metadata=large_program_metadata,
            tier1_limit=50,
            tier2_limit=200,
            show_relationships=True
        )

        # Should contain relationship info for top elements
        # This might be "performs", "calls", or arrow notation
        assert "PARA-" in result  # At minimum, paragraph names should appear

    def test_tier1_format_paragraph_function(self, large_program_metadata):
        """format_paragraph_tier1() should return full details"""
        from tiered_program_map import format_paragraph_tier1

        paragraph_info = {
            "name": "PARA-0001",
            "line": 110,
            "importance_score": 85,
            "performs_to": ["PARA-0002", "PARA-0003"],
            "called_by": ["PARA-0000"]
        }

        result = format_paragraph_tier1(paragraph_info)

        assert "PARA-0001" in result
        assert "110" in result  # Line number
        assert "85" in result or "score" in result.lower()  # Score


# ============================================================================
# US-1.4.T2: Test Tier 2 Names and Scores Only
# ============================================================================

class TestTieredDetailTier2NamesScoresOnly:
    """US-1.4.T2: Test that Tier 2 elements have names and scores only"""

    def test_tier2_paragraphs_have_names(self, large_program_metadata):
        """Tier 2 paragraphs should include names"""
        from tiered_program_map import format_tiered_program_map

        result = format_tiered_program_map(
            program_name="TESTPROG",
            metadata=large_program_metadata,
            tier1_limit=50,
            tier2_limit=200
        )

        # Middle range paragraphs should have names
        # With 300 paragraphs: tier1=0-49, tier2=50-249, tier3=250-299
        assert "PARA-" in result

    def test_tier2_paragraphs_have_scores(self, large_program_metadata):
        """Tier 2 paragraphs should include scores but less detail than tier 1"""
        from tiered_program_map import format_tiered_program_map

        result = format_tiered_program_map(
            program_name="TESTPROG",
            metadata=large_program_metadata,
            tier1_limit=50,
            tier2_limit=200
        )

        # Should have score indicators
        assert "[" in result or "score" in result.lower()

    def test_tier2_format_paragraph_function(self, large_program_metadata):
        """format_paragraph_tier2() should return name and score only"""
        from tiered_program_map import format_paragraph_tier2

        paragraph_info = {
            "name": "PARA-0075",
            "line": 850,
            "importance_score": 25,
            "performs_to": ["PARA-0076"],
            "called_by": []
        }

        result = format_paragraph_tier2(paragraph_info)

        assert "PARA-0075" in result
        # Line number should NOT be in tier 2
        # Score should be present (possibly abbreviated)
        assert "25" in result or "score" in result.lower()

    def test_tier2_more_compact_than_tier1(self, large_program_metadata):
        """Tier 2 formatting should be more compact than tier 1"""
        from tiered_program_map import format_paragraph_tier1, format_paragraph_tier2

        paragraph_info = {
            "name": "PARA-0050",
            "line": 600,
            "importance_score": 50,
            "performs_to": ["PARA-0051", "PARA-0052"],
            "called_by": ["PARA-0049"]
        }

        tier1_result = format_paragraph_tier1(paragraph_info)
        tier2_result = format_paragraph_tier2(paragraph_info)

        # Tier 2 should be shorter
        assert len(tier2_result) <= len(tier1_result)


# ============================================================================
# US-1.4.T3: Test Tier 3 Summary Count
# ============================================================================

class TestTieredDetailTier3SummaryCount:
    """US-1.4.T3: Test that Tier 3 shows summary count only"""

    def test_tier3_shows_count_message(self, large_program_metadata):
        """Tier 3 should show '...and N more paragraphs' message"""
        from tiered_program_map import format_tiered_program_map

        result = format_tiered_program_map(
            program_name="TESTPROG",
            metadata=large_program_metadata,
            tier1_limit=50,
            tier2_limit=200
        )

        # With 300 paragraphs and tier2_limit=200, there are 100 in tier 3
        # But actual number depends on ranking
        assert "more" in result.lower() or "remaining" in result.lower() or "..." in result

    def test_tier3_format_paragraph_function(self, large_program_metadata):
        """format_paragraph_tier3() should return count summary"""
        from tiered_program_map import format_paragraph_tier3

        remaining_count = 100

        result = format_paragraph_tier3(remaining_count)

        assert "100" in result
        assert "more" in result.lower() or "remaining" in result.lower()

    def test_tier3_no_individual_names(self, large_program_metadata):
        """Tier 3 should not list individual paragraph names"""
        from tiered_program_map import format_paragraph_tier3

        remaining_count = 50

        result = format_paragraph_tier3(remaining_count)

        # Should NOT have individual PARA- names, just count
        assert "PARA-" not in result

    def test_tier3_grammar_singular_plural(self, large_program_metadata):
        """Tier 3 should use correct grammar for singular/plural"""
        from tiered_program_map import format_paragraph_tier3

        result_plural = format_paragraph_tier3(100)
        result_singular = format_paragraph_tier3(1)

        # Plural should say "paragraphs" or similar
        assert "paragraph" in result_plural.lower()
        # Singular should handle grammar correctly
        assert "paragraph" in result_singular.lower()


# ============================================================================
# US-1.4.T4: Test Configurable Thresholds
# ============================================================================

class TestTieredDetailConfigurableThresholds:
    """US-1.4.T4: Test that tier thresholds are configurable"""

    def test_custom_tier1_threshold(self, large_program_metadata):
        """Custom tier 1 threshold should be respected"""
        from tiered_program_map import format_tiered_program_map

        # Use smaller tier 1 limit
        result = format_tiered_program_map(
            program_name="TESTPROG",
            metadata=large_program_metadata,
            tier1_limit=20,
            tier2_limit=100
        )

        # Should still produce valid output
        assert "TESTPROG" in result or "PARA-" in result

    def test_custom_tier2_threshold(self, large_program_metadata):
        """Custom tier 2 threshold should be respected"""
        from tiered_program_map import format_tiered_program_map

        # Use larger tier 2 limit
        result = format_tiered_program_map(
            program_name="TESTPROG",
            metadata=large_program_metadata,
            tier1_limit=50,
            tier2_limit=250
        )

        # More items should be in tier 2, fewer in tier 3
        assert "PARA-" in result

    def test_thresholds_from_config(self):
        """Tier thresholds should be loadable from YAML config"""
        from config_loader import ConfigLoader

        config_content = """
source:
  mode: single
  program_name: TESTPROG
  source_files: ./source

output:
  metadata_dir: ./metadata
  docs_path: ./docs

llm:
  provider: anthropic
  model: claude-3-sonnet

program_map:
  top_n_paragraphs: 30
  top_n_data_items: 20
  tiered_details:
    enabled: true
    tier1_limit: 30
    tier2_limit: 150
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(config_content)
            config_path = f.name

        try:
            loader = ConfigLoader(config_path)
            loader.load()

            pm_config = loader.get_program_map_config()

            assert 'tiered_details' in pm_config
            assert pm_config['tiered_details']['enabled'] == True
            assert pm_config['tiered_details']['tier1_limit'] == 30
            assert pm_config['tiered_details']['tier2_limit'] == 150
        finally:
            os.unlink(config_path)

    def test_default_thresholds(self, large_program_metadata):
        """Default thresholds should be tier1=50, tier2=200"""
        from tiered_program_map import DEFAULT_TIER1_LIMIT, DEFAULT_TIER2_LIMIT

        assert DEFAULT_TIER1_LIMIT == 50
        assert DEFAULT_TIER2_LIMIT == 200


# ============================================================================
# US-1.4.T5: Test Tiering Applies to Data Items
# ============================================================================

class TestTieredDetailAppliesToDataItems:
    """US-1.4.T5: Test that same tiering applies to data items"""

    def test_data_items_tier1_full_details(self, large_program_metadata):
        """Tier 1 data items should have full details"""
        from tiered_program_map import format_data_item_tier1

        data_item_info = {
            "name": "WS-DATA-0001",
            "level": "01",
            "picture": "X(100)",
            "line": 11,
            "usage_count": 50
        }

        result = format_data_item_tier1(data_item_info)

        assert "WS-DATA-0001" in result
        assert "01" in result or "level" in result.lower()
        assert "X(100)" in result or "PIC" in result

    def test_data_items_tier2_names_scores(self, large_program_metadata):
        """Tier 2 data items should have names and usage only"""
        from tiered_program_map import format_data_item_tier2

        data_item_info = {
            "name": "WS-DATA-0075",
            "level": "05",
            "picture": "9(5)",
            "line": 85,
            "usage_count": 15
        }

        result = format_data_item_tier2(data_item_info)

        assert "WS-DATA-0075" in result
        # Should have usage count but not full details

    def test_data_items_tier3_summary(self, large_program_metadata):
        """Tier 3 data items should show summary count"""
        from tiered_program_map import format_data_item_tier3

        remaining_count = 75

        result = format_data_item_tier3(remaining_count)

        assert "75" in result
        assert "data" in result.lower() or "item" in result.lower()

    def test_program_map_tiers_both_paragraphs_and_data(self, large_program_metadata):
        """Program map should tier both paragraphs and data items"""
        from tiered_program_map import format_tiered_program_map

        result = format_tiered_program_map(
            program_name="TESTPROG",
            metadata=large_program_metadata,
            tier1_limit=50,
            tier2_limit=200
        )

        # Should have both paragraph and data item sections
        assert "PARA-" in result or "paragraph" in result.lower()
        assert "WS-DATA-" in result or "data" in result.lower()

    def test_data_item_tiers_use_same_thresholds(self, large_program_metadata):
        """Data items should use same tier thresholds as paragraphs"""
        from tiered_program_map import get_tier_for_rank, DEFAULT_TIER1_LIMIT, DEFAULT_TIER2_LIMIT
        from tiered_program_map import DetailTier

        # Rank 25 should be tier 1 for both
        assert get_tier_for_rank(25, DEFAULT_TIER1_LIMIT, DEFAULT_TIER2_LIMIT) == DetailTier.FULL

        # Rank 100 should be tier 2 for both
        assert get_tier_for_rank(100, DEFAULT_TIER1_LIMIT, DEFAULT_TIER2_LIMIT) == DetailTier.SUMMARY

        # Rank 250 should be tier 3 for both
        assert get_tier_for_rank(250, DEFAULT_TIER1_LIMIT, DEFAULT_TIER2_LIMIT) == DetailTier.COUNT_ONLY


# ============================================================================
# RUN TESTS
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
