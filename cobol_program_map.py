"""
COBOL Program Map Generator

Inspired by aider's repository map approach, this module generates a lightweight,
hierarchical view of a COBOL program showing key structures, signatures, and
relationships without the full implementation.

This provides efficient code context for LLM processing of large COBOL programs.

Key Features:
- Token-efficient (2-5K tokens vs 100K+ for full source)
- Importance ranking (shows most-referenced elements first)
- Hierarchical structure (divisions -> sections -> paragraphs)
- Call graph visualization (PERFORM and CALL relationships)
- Data item ranking (by reference count)

Based on existing metadata:
- CTags: Structure and symbols
- SuperBol CFG: Control flow, calls, performs
- GnuCOBOL: Variable usage statistics
"""

from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict, Counter


def estimate_token_count(text: str) -> int:
    """Estimate token count (conservative: 1 token ≈ 4 chars)"""
    return len(text) // 4


def rank_paragraphs_by_importance(
    superbol_cfg: Dict[str, Any],
    ctags_outline: Dict[str, Any]
) -> List[Tuple[str, int]]:
    """
    Rank paragraphs by importance using graph analysis.

    Scoring factors:
    1. How many times the paragraph is PERFORMED (in-degree)
    2. How many other paragraphs it PERFORMS (out-degree)
    3. Entry point bonus (main paragraphs)
    4. External call bonus (paragraphs that CALL external programs)

    Args:
        superbol_cfg: SuperBol control flow graph
        ctags_outline: CTags outline with paragraph definitions

    Returns:
        List of (paragraph_name, score) tuples, sorted by score descending
    """
    paragraph_scores = Counter()

    # Extract all paragraph names from CTags and initialize with score 0
    # Handle both old format (symbols) and new format (outline.other)
    all_paragraphs = set()
    symbols = ctags_outline.get('symbols', [])
    if not symbols:
        # Try new CTags format: outline.other
        outline = ctags_outline.get('outline', {})
        symbols = outline.get('other', [])

    for symbol in symbols:
        if symbol.get('kind') in ['paragraph', 'section']:
            para_name = symbol.get('name', '')
            all_paragraphs.add(para_name)
            # Initialize all paragraphs with score 0 so they're included even if not referenced
            paragraph_scores[para_name] = 0

    # Score based on PERFORM relationships (in-degree)
    if 'performs' in superbol_cfg:
        for perform in superbol_cfg['performs']:
            target = perform.get('to', '')
            if target:
                paragraph_scores[target] += 5  # Being performed = important

    # Score based on edges (general control flow)
    if 'edges' in superbol_cfg:
        for edge in superbol_cfg['edges']:
            target = edge.get('to', '')
            if target:
                paragraph_scores[target] += 2

    # Score based on external calls (paragraphs that call external programs)
    if 'calls' in superbol_cfg:
        for call in superbol_cfg['calls']:
            caller = call.get('from', '')
            if caller:
                paragraph_scores[caller] += 10  # Makes external calls = very important

    # Entry point detection (common patterns)
    entry_patterns = [
        'MAIN', 'START', 'BEGIN', 'INIT', 'ENTRY',
        'Z-INITIALIZATION', 'Z-MAIN', 'A-MAIN', '000-MAIN'
    ]

    for para in all_paragraphs:
        for pattern in entry_patterns:
            if pattern in para.upper():
                paragraph_scores[para] += 50  # Entry points are critical

    # Return sorted by score
    return sorted(paragraph_scores.items(), key=lambda x: x[1], reverse=True)


def rank_data_items_by_importance(
    gnucobol_analysis: Dict[str, Any],
    ctags_outline: Dict[str, Any]
) -> List[Tuple[str, int]]:
    """
    Rank data items by usage frequency.

    Scoring factors:
    1. Reference count from GnuCOBOL analysis
    2. Level-01 items (record structures) get bonus
    3. Group items get bonus

    Args:
        gnucobol_analysis: GnuCOBOL variable analysis
        ctags_outline: CTags outline with data definitions

    Returns:
        List of (data_item_name, score) tuples, sorted by score
    """
    data_scores = Counter()

    # Get variable usage from GnuCOBOL
    if 'variables' in gnucobol_analysis:
        for var_name, var_info in gnucobol_analysis['variables'].items():
            # Reference count is the score
            ref_count = var_info.get('references', 0)
            data_scores[var_name] = ref_count

    # Bonus for level-01 and group items from CTags
    # Handle both old format (symbols) and new format (outline.other)
    symbols = ctags_outline.get('symbols', [])
    if not symbols:
        outline = ctags_outline.get('outline', {})
        symbols = outline.get('other', [])

    for symbol in symbols:
        if symbol.get('kind') == 'data':
            name = symbol.get('name', '')
            # Level-01 items are important structure definitions
            if symbol.get('level') == '01':
                data_scores[name] += 20
            # Group items (no PICTURE clause) are structural
            if not symbol.get('picture'):
                data_scores[name] += 10

    return sorted(data_scores.items(), key=lambda x: x[1], reverse=True)


def extract_division_structure(ctags_outline: Dict[str, Any]) -> Dict[str, List[Dict]]:
    """
    Extract hierarchical division structure from CTags.

    Returns:
        Dict mapping division names to lists of symbols within them
    """
    divisions = defaultdict(list)

    # Handle both old format (symbols) and new format (outline.other)
    symbols = ctags_outline.get('symbols', [])
    if not symbols:
        outline = ctags_outline.get('outline', {})
        symbols = outline.get('other', [])

    if not symbols:
        return divisions

    current_division = 'UNKNOWN'

    for symbol in symbols:
        kind = symbol.get('kind', '')
        name = symbol.get('name', '')

        # Track current division
        if kind == 'division':
            current_division = name

        # Add symbol to current division
        divisions[current_division].append(symbol)

    return divisions


def format_data_item(symbol: Dict, rank: Optional[int] = None) -> str:
    """
    Format a data item for the program map.

    Args:
        symbol: CTags symbol dict
        rank: Optional rank number (for top N items)

    Returns:
        Formatted string like: "WS-COUNTER PIC 9(05) [Rank: 3]"
    """
    name = symbol.get('name', 'UNKNOWN')
    level = symbol.get('level', '')
    picture = symbol.get('picture', '')

    parts = [f"{'│   ' if not rank else f'│   #{rank:2d}'}", name]

    if level:
        parts.append(f"(Level {level})")

    if picture:
        parts.append(f"PIC {picture}")
    elif level == '01':
        parts.append("(GROUP)")

    return "  ".join(parts)


def format_paragraph(name: str, rank: Optional[int] = None, line: Optional[int] = None) -> str:
    """
    Format a paragraph for the program map.

    Returns:
        Formatted string like: "#1  MAIN-PARAGRAPH (line 1234)"
    """
    parts = []

    if rank:
        parts.append(f"│   #{rank:2d}")
    else:
        parts.append("│    ")

    parts.append(name)

    if line:
        parts.append(f"(line {line})")

    return "  ".join(parts)


def generate_cobol_program_map(
    program_name: str,
    metadata: Dict[str, Any],
    token_budget: int = 5000,
    top_n_paragraphs: int = 30,
    top_n_data_items: int = 20,
    use_dynamic_limits: bool = False,
    dynamic_thresholds: Optional[Dict[str, int]] = None,
    dynamic_custom_limits: Optional[Dict] = None,
    use_tiered_details: bool = False,
    tier1_limit: int = 50,
    tier2_limit: int = 200,
    use_mandatory_elements: bool = False,
    entry_point_patterns: Optional[List[str]] = None,
    error_handler_patterns: Optional[List[str]] = None
) -> str:
    """
    Generate a COBOL program map from metadata.

    Args:
        program_name: Name of the COBOL program
        metadata: Dict with 'superbol_cfg', 'gnucobol_analysis', 'ctags_outline'
        token_budget: Maximum tokens for the map (will stay under this)
        top_n_paragraphs: Number of top paragraphs to show (ignored if use_dynamic_limits=True)
        top_n_data_items: Number of top data items to show (ignored if use_dynamic_limits=True)
        use_dynamic_limits: If True, automatically determine limits based on program size
        dynamic_thresholds: Custom thresholds for size detection (optional)
        dynamic_custom_limits: Custom limits per size category (optional)
        use_tiered_details: If True, use tiered detail levels (full/summary/count)
        tier1_limit: Number of elements to show with full details
        tier2_limit: Total elements to show with details (tier1 + tier2)
        use_mandatory_elements: If True, include Critical Elements section
        entry_point_patterns: Custom patterns for identifying entry points
        error_handler_patterns: Custom patterns for identifying error handlers

    Returns:
        Formatted program map string
    """
    # If mandatory elements is enabled, delegate to mandatory_elements module
    if use_mandatory_elements:
        try:
            from mandatory_elements import format_program_map_with_mandatory
            return format_program_map_with_mandatory(
                program_name=program_name,
                metadata=metadata,
                top_n_paragraphs=top_n_paragraphs,
                top_n_data_items=top_n_data_items,
                entry_point_patterns=entry_point_patterns,
                error_handler_patterns=error_handler_patterns
            )
        except ImportError:
            pass  # Fall back to standard formatting if module not available

    # If tiered details is enabled, delegate to tiered_program_map module
    if use_tiered_details:
        try:
            from tiered_program_map import format_tiered_program_map
            return format_tiered_program_map(
                program_name=program_name,
                metadata=metadata,
                tier1_limit=tier1_limit,
                tier2_limit=tier2_limit
            )
        except ImportError:
            pass  # Fall back to standard formatting if module not available

    # Apply dynamic limits if enabled
    if use_dynamic_limits:
        try:
            from dynamic_program_limits import get_dynamic_limits
            limits = get_dynamic_limits(
                metadata,
                thresholds=dynamic_thresholds,
                custom_limits=dynamic_custom_limits
            )
            top_n_paragraphs = limits['top_n_paragraphs']
            top_n_data_items = limits['top_n_data_items']
        except ImportError:
            pass  # Fall back to provided values if module not available
    map_lines = []

    # Header
    map_lines.append("═" * 80)
    map_lines.append(f"PROGRAM MAP: {program_name}")
    map_lines.append("═" * 80)

    # Get metadata components
    superbol_cfg = metadata.get('superbol_cfg', {})
    gnucobol_analysis = metadata.get('gnucobol_analysis', {})
    ctags_outline = metadata.get('ctags_outline', {})

    # Count total elements
    total_paragraphs = len([s for s in ctags_outline.get('symbols', [])
                           if s.get('kind') in ['paragraph', 'section']])
    total_data_items = len([s for s in ctags_outline.get('symbols', [])
                           if s.get('kind') == 'data'])
    total_calls = len(superbol_cfg.get('calls', []))

    map_lines.append(f"│")
    map_lines.append(f"│ Total Paragraphs: {total_paragraphs}")
    map_lines.append(f"│ Total Data Items: {total_data_items}")
    map_lines.append(f"│ External Calls: {total_calls}")
    map_lines.append(f"│")

    # Rank paragraphs and data items
    ranked_paragraphs = rank_paragraphs_by_importance(superbol_cfg, ctags_outline)
    ranked_data = rank_data_items_by_importance(gnucobol_analysis, ctags_outline)

    # Get division structure
    divisions = extract_division_structure(ctags_outline)

    # Build hierarchy
    map_lines.append("├── IDENTIFICATION DIVISION")
    map_lines.append(f"│   └── PROGRAM-ID: {program_name}")
    map_lines.append("│")

    # DATA DIVISION - Show top data items by importance
    if 'DATA DIVISION' in divisions or ranked_data:
        map_lines.append("├── DATA DIVISION")
        map_lines.append("│   │")

        # Handle -1 (show all) mode for data items
        if top_n_data_items < 0:
            effective_data_limit = len(ranked_data)
            data_header = f"│   ├── All {effective_data_limit} Data Items:"
        else:
            effective_data_limit = min(top_n_data_items, len(ranked_data))
            data_header = f"│   ├── Top {effective_data_limit} Most-Used Data Items:"
        map_lines.append(data_header)

        # Get full symbol info for top ranked items
        data_symbols = {s['name']: s for s in ctags_outline.get('symbols', [])
                       if s.get('kind') == 'data'}

        for rank, (data_name, score) in enumerate(ranked_data[:effective_data_limit], 1):
            if data_name in data_symbols:
                symbol = data_symbols[data_name]
                formatted = format_data_item(symbol, rank)
                map_lines.append(f"{formatted}  [Used: {score} times]")

        map_lines.append("│   │")

    # PROCEDURE DIVISION - Show top paragraphs by importance
    map_lines.append("└── PROCEDURE DIVISION")
    map_lines.append("    │")

    # Handle -1 (show all) mode for paragraphs
    if top_n_paragraphs < 0:
        effective_para_limit = len(ranked_paragraphs)
        para_header = f"    ├── All {effective_para_limit} Paragraphs:"
    else:
        effective_para_limit = min(top_n_paragraphs, len(ranked_paragraphs))
        para_header = f"    ├── Top {effective_para_limit} Most Important Paragraphs:"
    map_lines.append(para_header)

    # Get full symbol info for paragraphs
    para_symbols = {s['name']: s for s in ctags_outline.get('symbols', [])
                   if s.get('kind') in ['paragraph', 'section']}

    for rank, (para_name, score) in enumerate(ranked_paragraphs[:effective_para_limit], 1):
        line = None
        if para_name in para_symbols:
            line = para_symbols[para_name].get('line')

        formatted = format_paragraph(para_name, rank, line)
        map_lines.append(f"    {formatted}  [Importance: {score}]")

    # External Calls Summary
    if superbol_cfg.get('calls'):
        map_lines.append("    │")
        map_lines.append(f"    └── External Calls ({len(superbol_cfg['calls'])} total):")

        # Group calls by target program
        call_targets = Counter()
        for call in superbol_cfg['calls']:
            target = call.get('to', 'UNKNOWN')
            call_targets[target] += 1

        for target, count in call_targets.most_common(15):  # Top 15 external programs
            map_lines.append(f"        ├─> {target} (called {count} times)")

    map_lines.append("")
    map_lines.append("═" * 80)
    map_lines.append(f"Map Token Count: ~{estimate_token_count(chr(10).join(map_lines))}")
    map_lines.append("═" * 80)

    return "\n".join(map_lines)


def generate_compact_program_map(
    program_name: str,
    metadata: Dict[str, Any],
    token_budget: int = 2000
) -> str:
    """
    Generate a very compact program map for tight token budgets.

    Shows only the most critical elements.
    """
    return generate_cobol_program_map(
        program_name,
        metadata,
        token_budget=token_budget,
        top_n_paragraphs=10,
        top_n_data_items=10
    )


def generate_detailed_program_map(
    program_name: str,
    metadata: Dict[str, Any],
    token_budget: int = 10000
) -> str:
    """
    Generate a detailed program map for generous token budgets.

    Shows more elements for richer context.
    """
    return generate_cobol_program_map(
        program_name,
        metadata,
        token_budget=token_budget,
        top_n_paragraphs=50,
        top_n_data_items=30
    )
