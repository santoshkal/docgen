"""
Tiered Program Map Module

Provides tiered detail levels for program map generation:
- Tier 1 (FULL): Full details - line numbers, importance scores, relationships
- Tier 2 (SUMMARY): Names and scores only
- Tier 3 (COUNT_ONLY): Summary count only ("...and N more paragraphs")

US-1.4: Tiered Detail Levels in Program Map

This allows balancing token usage with information richness by showing
full details for the most important elements while summarizing the rest.
"""

from enum import Enum
from typing import Any, Dict, List, Optional, Tuple
from collections import Counter


class DetailTier(Enum):
    """
    Detail level tiers for program map elements.

    Tiers:
        FULL: Complete details (line numbers, scores, relationships)
        SUMMARY: Names and scores only
        COUNT_ONLY: Just a count summary
    """
    FULL = "full"
    SUMMARY = "summary"
    COUNT_ONLY = "count_only"


# Default tier thresholds
DEFAULT_TIER1_LIMIT = 50   # Top 50 elements get full details
DEFAULT_TIER2_LIMIT = 200  # Next 150 (50-200) get summary


def get_tier_for_rank(
    rank: int,
    tier1_limit: int = DEFAULT_TIER1_LIMIT,
    tier2_limit: int = DEFAULT_TIER2_LIMIT
) -> DetailTier:
    """
    Determine which tier an element belongs to based on its rank.

    Args:
        rank: 0-based rank of the element (0 = most important)
        tier1_limit: Rank threshold for tier 1 (exclusive)
        tier2_limit: Rank threshold for tier 2 (exclusive)

    Returns:
        DetailTier enum value
    """
    if rank < tier1_limit:
        return DetailTier.FULL
    elif rank < tier2_limit:
        return DetailTier.SUMMARY
    else:
        return DetailTier.COUNT_ONLY


# ============================================================================
# PARAGRAPH FORMATTING FUNCTIONS
# ============================================================================

def format_paragraph_tier1(paragraph_info: Dict[str, Any]) -> str:
    """
    Format a paragraph with full details (Tier 1).

    Includes:
    - Name
    - Line number
    - Importance score
    - Relationships (performs_to, called_by)

    Args:
        paragraph_info: Dictionary with paragraph details:
            - name: Paragraph name
            - line: Source line number
            - importance_score: Calculated importance score
            - performs_to: List of paragraphs this one calls
            - called_by: List of paragraphs that call this one

    Returns:
        Formatted string with full details
    """
    name = paragraph_info.get('name', 'UNKNOWN')
    line = paragraph_info.get('line', '?')
    score = paragraph_info.get('importance_score', 0)
    performs_to = paragraph_info.get('performs_to', [])
    called_by = paragraph_info.get('called_by', [])

    parts = [f"    │   {name}"]
    parts.append(f"(line {line})")
    parts.append(f"[Score: {score}]")

    # Add relationship info if present
    if performs_to:
        performs_str = ", ".join(performs_to[:3])
        if len(performs_to) > 3:
            performs_str += f" +{len(performs_to) - 3} more"
        parts.append(f"→ {performs_str}")

    if called_by:
        callers_str = ", ".join(called_by[:2])
        if len(called_by) > 2:
            callers_str += f" +{len(called_by) - 2} more"
        parts.append(f"← {callers_str}")

    return "  ".join(parts)


def format_paragraph_tier2(paragraph_info: Dict[str, Any]) -> str:
    """
    Format a paragraph with names and scores only (Tier 2).

    Includes:
    - Name
    - Importance score (abbreviated)

    Args:
        paragraph_info: Dictionary with paragraph details

    Returns:
        Formatted string with name and score only
    """
    name = paragraph_info.get('name', 'UNKNOWN')
    score = paragraph_info.get('importance_score', 0)

    return f"    │   {name}  [{score}]"


def format_paragraph_tier3(remaining_count: int) -> str:
    """
    Format a summary count for remaining paragraphs (Tier 3).

    Args:
        remaining_count: Number of remaining paragraphs

    Returns:
        Formatted summary string
    """
    if remaining_count == 1:
        return f"    │   ...and 1 more paragraph"
    else:
        return f"    │   ...and {remaining_count} more paragraphs"


# ============================================================================
# DATA ITEM FORMATTING FUNCTIONS
# ============================================================================

def format_data_item_tier1(data_item_info: Dict[str, Any]) -> str:
    """
    Format a data item with full details (Tier 1).

    Includes:
    - Name
    - Level number
    - Picture clause
    - Line number
    - Usage count

    Args:
        data_item_info: Dictionary with data item details:
            - name: Data item name
            - level: COBOL level number (01, 05, etc.)
            - picture: PIC clause
            - line: Source line number
            - usage_count: Number of references

    Returns:
        Formatted string with full details
    """
    name = data_item_info.get('name', 'UNKNOWN')
    level = data_item_info.get('level', '??')
    picture = data_item_info.get('picture', '')
    line = data_item_info.get('line', '?')
    usage = data_item_info.get('usage_count', 0)

    parts = [f"│   {name}"]
    parts.append(f"(Level {level})")

    if picture:
        parts.append(f"PIC {picture}")
    else:
        parts.append("(GROUP)")

    parts.append(f"Line {line}")
    parts.append(f"[Used: {usage}x]")

    return "  ".join(parts)


def format_data_item_tier2(data_item_info: Dict[str, Any]) -> str:
    """
    Format a data item with names and usage only (Tier 2).

    Includes:
    - Name
    - Usage count

    Args:
        data_item_info: Dictionary with data item details

    Returns:
        Formatted string with name and usage only
    """
    name = data_item_info.get('name', 'UNKNOWN')
    usage = data_item_info.get('usage_count', 0)

    return f"│   {name}  [{usage}x]"


def format_data_item_tier3(remaining_count: int) -> str:
    """
    Format a summary count for remaining data items (Tier 3).

    Args:
        remaining_count: Number of remaining data items

    Returns:
        Formatted summary string
    """
    if remaining_count == 1:
        return f"│   ...and 1 more data item"
    else:
        return f"│   ...and {remaining_count} more data items"


# ============================================================================
# MAIN TIERED PROGRAM MAP FUNCTION
# ============================================================================

def rank_paragraphs_with_details(
    metadata: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """
    Rank paragraphs by importance and return with full details.

    Args:
        metadata: Dictionary with ctags_outline, superbol_cfg

    Returns:
        List of paragraph info dicts, sorted by importance (highest first)
    """
    ctags_outline = metadata.get('ctags_outline', {})
    superbol_cfg = metadata.get('superbol_cfg', {})

    # Build paragraph info from CTags
    paragraphs = {}
    for symbol in ctags_outline.get('symbols', []):
        if symbol.get('kind') in ('paragraph', 'section'):
            name = symbol.get('name', '')
            paragraphs[name] = {
                'name': name,
                'line': symbol.get('line', 0),
                'importance_score': 0,
                'performs_to': [],
                'called_by': []
            }

    # Calculate importance from performs
    for perform in superbol_cfg.get('performs', []):
        caller = perform.get('from', '')
        target = perform.get('to', '')

        if target in paragraphs:
            paragraphs[target]['importance_score'] += 5
            paragraphs[target]['called_by'].append(caller)

        if caller in paragraphs:
            paragraphs[caller]['performs_to'].append(target)

    # Bonus for external calls
    for call in superbol_cfg.get('calls', []):
        caller = call.get('from', '')
        if caller in paragraphs:
            paragraphs[caller]['importance_score'] += 10

    # Entry point bonus
    entry_patterns = ['MAIN', 'START', 'BEGIN', 'INIT', 'ENTRY', '000-', 'A-MAIN']
    for name, info in paragraphs.items():
        for pattern in entry_patterns:
            if pattern in name.upper():
                info['importance_score'] += 50
                break

    # Sort by importance (highest first)
    ranked = sorted(paragraphs.values(), key=lambda x: x['importance_score'], reverse=True)

    return ranked


def rank_data_items_with_details(
    metadata: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """
    Rank data items by usage and return with full details.

    Args:
        metadata: Dictionary with ctags_outline, gnucobol_analysis

    Returns:
        List of data item info dicts, sorted by usage (highest first)
    """
    ctags_outline = metadata.get('ctags_outline', {})
    gnucobol_analysis = metadata.get('gnucobol_analysis', {})

    # Get usage counts from GnuCOBOL
    variables = gnucobol_analysis.get('variables', {})

    # Build data item info from CTags
    data_items = {}
    for symbol in ctags_outline.get('symbols', []):
        if symbol.get('kind') == 'data':
            name = symbol.get('name', '')
            usage_info = variables.get(name, {})
            data_items[name] = {
                'name': name,
                'level': symbol.get('level', '??'),
                'picture': symbol.get('picture', ''),
                'line': symbol.get('line', 0),
                'usage_count': usage_info.get('references', 0)
            }

            # Bonus for level-01 items
            if symbol.get('level') == '01':
                data_items[name]['usage_count'] += 20

    # Sort by usage (highest first)
    ranked = sorted(data_items.values(), key=lambda x: x['usage_count'], reverse=True)

    return ranked


def format_tiered_program_map(
    program_name: str,
    metadata: Dict[str, Any],
    tier1_limit: int = DEFAULT_TIER1_LIMIT,
    tier2_limit: int = DEFAULT_TIER2_LIMIT,
    show_relationships: bool = True
) -> str:
    """
    Generate a program map with tiered detail levels.

    Tier 1 (ranks 0 to tier1_limit-1): Full details
    Tier 2 (ranks tier1_limit to tier2_limit-1): Names and scores
    Tier 3 (ranks tier2_limit+): Summary count only

    Args:
        program_name: Name of the COBOL program
        metadata: Dictionary with ctags_outline, superbol_cfg, gnucobol_analysis
        tier1_limit: Number of elements to show with full details
        tier2_limit: Number of elements to show with names/scores
        show_relationships: Whether to show relationships in tier 1

    Returns:
        Formatted program map string with tiered details
    """
    map_lines = []

    # Header
    map_lines.append("═" * 80)
    map_lines.append(f"PROGRAM MAP: {program_name}")
    map_lines.append("═" * 80)

    # Get ranked paragraphs and data items
    ranked_paragraphs = rank_paragraphs_with_details(metadata)
    ranked_data_items = rank_data_items_with_details(metadata)

    # Program statistics
    map_lines.append(f"│")
    map_lines.append(f"│ Total Paragraphs: {len(ranked_paragraphs)}")
    map_lines.append(f"│ Total Data Items: {len(ranked_data_items)}")
    map_lines.append(f"│")

    # DATA DIVISION
    map_lines.append("├── DATA DIVISION")
    map_lines.append("│   │")

    # Format data items by tier
    tier1_data = ranked_data_items[:tier1_limit]
    tier2_data = ranked_data_items[tier1_limit:tier2_limit]
    tier3_count_data = max(0, len(ranked_data_items) - tier2_limit)

    if tier1_data:
        map_lines.append(f"│   ├── Top {len(tier1_data)} Data Items (Full Details):")
        for item in tier1_data:
            map_lines.append(format_data_item_tier1(item))

    if tier2_data:
        map_lines.append(f"│   ├── Next {len(tier2_data)} Data Items:")
        for item in tier2_data:
            map_lines.append(format_data_item_tier2(item))

    if tier3_count_data > 0:
        map_lines.append(format_data_item_tier3(tier3_count_data))

    map_lines.append("│   │")

    # PROCEDURE DIVISION
    map_lines.append("└── PROCEDURE DIVISION")
    map_lines.append("    │")

    # Format paragraphs by tier
    tier1_paras = ranked_paragraphs[:tier1_limit]
    tier2_paras = ranked_paragraphs[tier1_limit:tier2_limit]
    tier3_count_paras = max(0, len(ranked_paragraphs) - tier2_limit)

    if tier1_paras:
        map_lines.append(f"    ├── Top {len(tier1_paras)} Paragraphs (Full Details):")
        for para in tier1_paras:
            map_lines.append(format_paragraph_tier1(para))

    if tier2_paras:
        map_lines.append(f"    ├── Next {len(tier2_paras)} Paragraphs:")
        for para in tier2_paras:
            map_lines.append(format_paragraph_tier2(para))

    if tier3_count_paras > 0:
        map_lines.append(format_paragraph_tier3(tier3_count_paras))

    map_lines.append("")
    map_lines.append("═" * 80)

    return "\n".join(map_lines)


def get_tiered_config_from_dict(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract tiered details configuration from a config dictionary.

    Args:
        config: Configuration dictionary (from config_loader)

    Returns:
        Dictionary with tier configuration or defaults
    """
    pm_config = config.get('program_map', {})
    tiered_config = pm_config.get('tiered_details', {})

    return {
        'enabled': tiered_config.get('enabled', False),
        'tier1_limit': tiered_config.get('tier1_limit', DEFAULT_TIER1_LIMIT),
        'tier2_limit': tiered_config.get('tier2_limit', DEFAULT_TIER2_LIMIT)
    }
