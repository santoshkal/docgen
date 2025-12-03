"""
Mandatory Elements Module

Provides category-based mandatory inclusion in program maps.
Ensures critical elements like entry points, call sites, and error handlers
are always included regardless of their importance rank.

US-1.5: Category-Based Mandatory Inclusion in Program Map

Categories:
- Entry Points: MAIN, START, INIT, BEGIN, ENTRY patterns
- Call Sites: Paragraphs that make external CALL statements
- Error Handlers: ERROR, ERR, EXCEPTION, ABEND patterns
"""

from typing import Any, Dict, List, Optional, Set, Tuple
from collections import Counter


# ============================================================================
# DEFAULT PATTERN CONSTANTS
# ============================================================================

# US-1.5.I1: Define MANDATORY_CATEGORIES constant with default patterns

DEFAULT_ENTRY_POINT_PATTERNS: List[str] = [
    'MAIN',
    'START',
    'INIT',
    'BEGIN',
    'ENTRY',
    '0000-',     # Common prefix for main paragraphs (4 zeros)
    'A-MAIN',
    'Z-MAIN',
    'Z-INIT',
]

DEFAULT_ERROR_HANDLER_PATTERNS: List[str] = [
    'ERROR',
    'ERR',
    'EXCEPTION',
    'ABEND',
    'FAIL',
    'ABORT',
]

MANDATORY_CATEGORIES: Dict[str, Dict[str, Any]] = {
    'entry_points': {
        'description': 'Entry points and main drivers',
        'default_patterns': DEFAULT_ENTRY_POINT_PATTERNS,
    },
    'call_sites': {
        'description': 'Paragraphs making external CALL statements',
        'default_patterns': None,  # Detected from CFG, not patterns
    },
    'error_handlers': {
        'description': 'Error and exception handling routines',
        'default_patterns': DEFAULT_ERROR_HANDLER_PATTERNS,
    },
}


# ============================================================================
# US-1.5.I2: Identify Entry Points
# ============================================================================

def identify_entry_points(
    metadata: Dict[str, Any],
    patterns: Optional[List[str]] = None
) -> List[Dict[str, Any]]:
    """
    Identify entry point paragraphs in the program.

    Entry points are paragraphs whose names match patterns like MAIN, START, INIT.

    Args:
        metadata: Dictionary with ctags_outline, superbol_cfg, etc.
        patterns: Optional custom patterns. Uses DEFAULT_ENTRY_POINT_PATTERNS if None.

    Returns:
        List of entry point paragraph info dicts with 'name', 'line', 'category'
    """
    if patterns is None:
        patterns = DEFAULT_ENTRY_POINT_PATTERNS

    entry_points = []

    ctags_outline = metadata.get('ctags_outline', {})
    symbols = ctags_outline.get('symbols', [])

    for symbol in symbols:
        if symbol.get('kind') not in ('paragraph', 'section'):
            continue

        name = symbol.get('name', '')
        name_upper = name.upper()

        # Check if name matches any entry point pattern
        for pattern in patterns:
            if pattern.upper() in name_upper:
                entry_points.append({
                    'name': name,
                    'line': symbol.get('line', 0),
                    'category': 'entry_point',
                    'matched_pattern': pattern,
                })
                break  # Only add once per symbol

    return entry_points


# ============================================================================
# US-1.5.I3: Identify Call Sites
# ============================================================================

def identify_call_sites(
    metadata: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """
    Identify paragraphs that make external CALL statements.

    Uses SuperBol CFG 'calls' section to find paragraphs that call external programs.

    Args:
        metadata: Dictionary with ctags_outline, superbol_cfg, etc.

    Returns:
        List of call site paragraph info dicts with 'name', 'line', 'calls_to', 'category'
    """
    call_sites = []
    call_sites_map: Dict[str, Dict[str, Any]] = {}

    superbol_cfg = metadata.get('superbol_cfg', {})
    calls = superbol_cfg.get('calls', [])

    # Build a map of paragraph -> list of programs it calls
    for call in calls:
        caller = call.get('from', '')
        target = call.get('to', '')

        if not caller or not target:
            continue

        if caller not in call_sites_map:
            call_sites_map[caller] = {
                'name': caller,
                'line': 0,  # Will be updated from CTags
                'category': 'call_site',
                'calls_to': [],
            }

        call_sites_map[caller]['calls_to'].append(target)

    # Enrich with line numbers from CTags
    ctags_outline = metadata.get('ctags_outline', {})
    symbols = ctags_outline.get('symbols', [])

    symbol_lines = {s.get('name', ''): s.get('line', 0) for s in symbols}

    for caller, info in call_sites_map.items():
        info['line'] = symbol_lines.get(caller, 0)
        call_sites.append(info)

    return call_sites


# ============================================================================
# US-1.5.I4: Identify Error Handlers
# ============================================================================

def identify_error_handlers(
    metadata: Dict[str, Any],
    patterns: Optional[List[str]] = None
) -> List[Dict[str, Any]]:
    """
    Identify error handling paragraphs in the program.

    Error handlers are paragraphs whose names match patterns like ERROR, ERR, EXCEPTION.

    Args:
        metadata: Dictionary with ctags_outline, superbol_cfg, etc.
        patterns: Optional custom patterns. Uses DEFAULT_ERROR_HANDLER_PATTERNS if None.

    Returns:
        List of error handler paragraph info dicts with 'name', 'line', 'category'
    """
    if patterns is None:
        patterns = DEFAULT_ERROR_HANDLER_PATTERNS

    error_handlers = []

    ctags_outline = metadata.get('ctags_outline', {})
    symbols = ctags_outline.get('symbols', [])

    for symbol in symbols:
        if symbol.get('kind') not in ('paragraph', 'section'):
            continue

        name = symbol.get('name', '')
        name_upper = name.upper()

        # Check if name matches any error handler pattern
        for pattern in patterns:
            if pattern.upper() in name_upper:
                error_handlers.append({
                    'name': name,
                    'line': symbol.get('line', 0),
                    'category': 'error_handler',
                    'matched_pattern': pattern,
                })
                break  # Only add once per symbol

    return error_handlers


# ============================================================================
# US-1.5.I5: Get All Mandatory Elements
# ============================================================================

def get_mandatory_elements(
    metadata: Dict[str, Any],
    entry_point_patterns: Optional[List[str]] = None,
    error_handler_patterns: Optional[List[str]] = None
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Get all mandatory elements from the program metadata.

    Combines entry points, call sites, and error handlers into a single
    dictionary, ensuring no duplicates across categories.

    Args:
        metadata: Dictionary with ctags_outline, superbol_cfg, etc.
        entry_point_patterns: Optional custom entry point patterns.
        error_handler_patterns: Optional custom error handler patterns.

    Returns:
        Dictionary with keys 'entry_points', 'call_sites', 'error_handlers',
        each containing a list of element info dicts.
    """
    # Identify each category
    entry_points = identify_entry_points(metadata, entry_point_patterns)
    call_sites = identify_call_sites(metadata)
    error_handlers = identify_error_handlers(metadata, error_handler_patterns)

    # Track seen names to avoid duplicates across categories
    seen_names: Set[str] = set()
    result: Dict[str, List[Dict[str, Any]]] = {
        'entry_points': [],
        'call_sites': [],
        'error_handlers': [],
    }

    # Add entry points first (highest priority)
    for ep in entry_points:
        name = ep['name']
        if name not in seen_names:
            seen_names.add(name)
            result['entry_points'].append(ep)

    # Add call sites (second priority)
    for cs in call_sites:
        name = cs['name']
        if name not in seen_names:
            seen_names.add(name)
            result['call_sites'].append(cs)

    # Add error handlers (third priority)
    for eh in error_handlers:
        name = eh['name']
        if name not in seen_names:
            seen_names.add(name)
            result['error_handlers'].append(eh)

    return result


# ============================================================================
# US-1.5.I6: Format Program Map with Mandatory Elements
# ============================================================================

def get_ranked_elements_excluding_mandatory(
    metadata: Dict[str, Any],
    mandatory: Dict[str, List[Dict[str, Any]]],
    top_n_paragraphs: int = 30
) -> List[Dict[str, Any]]:
    """
    Get ranked paragraphs excluding those already in mandatory elements.

    Args:
        metadata: Dictionary with ctags_outline, superbol_cfg, etc.
        mandatory: Dictionary of mandatory elements (from get_mandatory_elements)
        top_n_paragraphs: Number of top ranked paragraphs to include (-1 for all)

    Returns:
        List of ranked paragraph info dicts, excluding mandatory elements
    """
    # Get all mandatory names
    mandatory_names: Set[str] = set()
    for category in ['entry_points', 'call_sites', 'error_handlers']:
        for elem in mandatory.get(category, []):
            mandatory_names.add(elem['name'])

    # Get all paragraphs from CTags
    ctags_outline = metadata.get('ctags_outline', {})
    superbol_cfg = metadata.get('superbol_cfg', {})
    symbols = ctags_outline.get('symbols', [])

    # Build paragraph info with importance scores
    paragraphs: Dict[str, Dict[str, Any]] = {}
    for symbol in symbols:
        if symbol.get('kind') not in ('paragraph', 'section'):
            continue

        name = symbol.get('name', '')
        if name in mandatory_names:
            continue  # Skip mandatory elements

        paragraphs[name] = {
            'name': name,
            'line': symbol.get('line', 0),
            'importance_score': 0,
        }

    # Calculate importance from performs
    for perform in superbol_cfg.get('performs', []):
        target = perform.get('to', '')
        if target in paragraphs:
            paragraphs[target]['importance_score'] += 5

    # Bonus for external calls
    for call in superbol_cfg.get('calls', []):
        caller = call.get('from', '')
        if caller in paragraphs:
            paragraphs[caller]['importance_score'] += 10

    # Sort by importance (highest first)
    ranked = sorted(paragraphs.values(), key=lambda x: x['importance_score'], reverse=True)

    # Apply limit
    if top_n_paragraphs >= 0:
        ranked = ranked[:top_n_paragraphs]

    return ranked


def format_program_map_with_mandatory(
    program_name: str,
    metadata: Dict[str, Any],
    top_n_paragraphs: int = 30,
    top_n_data_items: int = 20,
    entry_point_patterns: Optional[List[str]] = None,
    error_handler_patterns: Optional[List[str]] = None,
    show_mandatory: bool = True
) -> str:
    """
    Generate a program map with mandatory elements in a separate section.

    The program map will have:
    1. Critical Elements section (mandatory elements)
    2. Ranked Elements section (remaining top elements by importance)

    Args:
        program_name: Name of the COBOL program
        metadata: Dictionary with ctags_outline, superbol_cfg, gnucobol_analysis
        top_n_paragraphs: Number of top ranked paragraphs to include
        top_n_data_items: Number of top data items to include
        entry_point_patterns: Optional custom entry point patterns
        error_handler_patterns: Optional custom error handler patterns
        show_mandatory: Whether to show mandatory elements section

    Returns:
        Formatted program map string with Critical Elements section
    """
    map_lines = []

    # Header
    map_lines.append("=" * 80)
    map_lines.append(f"PROGRAM MAP: {program_name}")
    map_lines.append("=" * 80)

    # Get mandatory elements
    mandatory = get_mandatory_elements(
        metadata,
        entry_point_patterns=entry_point_patterns,
        error_handler_patterns=error_handler_patterns
    )

    # Count totals
    ctags_outline = metadata.get('ctags_outline', {})
    symbols = ctags_outline.get('symbols', [])
    total_paragraphs = sum(1 for s in symbols if s.get('kind') in ('paragraph', 'section'))
    total_data_items = sum(1 for s in symbols if s.get('kind') == 'data')

    total_mandatory = (
        len(mandatory['entry_points']) +
        len(mandatory['call_sites']) +
        len(mandatory['error_handlers'])
    )

    map_lines.append("|")
    map_lines.append(f"| Total Paragraphs: {total_paragraphs}")
    map_lines.append(f"| Total Data Items: {total_data_items}")
    map_lines.append(f"| Critical Elements: {total_mandatory}")
    map_lines.append("|")

    # CRITICAL ELEMENTS SECTION
    if show_mandatory and total_mandatory > 0:
        map_lines.append("+-- CRITICAL ELEMENTS (Always Included)")
        map_lines.append("|   |")

        # Entry Points
        if mandatory['entry_points']:
            map_lines.append(f"|   +-- Entry Points ({len(mandatory['entry_points'])} found):")
            for ep in mandatory['entry_points']:
                map_lines.append(f"|   |   - {ep['name']}  (line {ep['line']})")

        # Call Sites
        if mandatory['call_sites']:
            map_lines.append(f"|   +-- Call Sites ({len(mandatory['call_sites'])} found):")
            for cs in mandatory['call_sites']:
                calls_str = ", ".join(cs.get('calls_to', [])[:3])
                if len(cs.get('calls_to', [])) > 3:
                    calls_str += f" +{len(cs['calls_to']) - 3} more"
                map_lines.append(f"|   |   - {cs['name']}  -> {calls_str}")

        # Error Handlers
        if mandatory['error_handlers']:
            map_lines.append(f"|   +-- Error Handlers ({len(mandatory['error_handlers'])} found):")
            for eh in mandatory['error_handlers']:
                map_lines.append(f"|   |   - {eh['name']}  (line {eh['line']})")

        map_lines.append("|   |")

    # RANKED ELEMENTS SECTION
    ranked_paragraphs = get_ranked_elements_excluding_mandatory(
        metadata, mandatory, top_n_paragraphs
    )

    if ranked_paragraphs:
        map_lines.append(f"+-- Top {len(ranked_paragraphs)} Ranked Paragraphs:")
        for para in ranked_paragraphs:
            score = para.get('importance_score', 0)
            map_lines.append(f"|   - {para['name']}  (line {para['line']})  [Score: {score}]")

    # DATA ITEMS SECTION
    gnucobol_analysis = metadata.get('gnucobol_analysis', {})
    variables = gnucobol_analysis.get('variables', {})

    # Get data items with usage counts
    data_items = []
    for symbol in symbols:
        if symbol.get('kind') != 'data':
            continue
        name = symbol.get('name', '')
        var_info = variables.get(name, {})
        data_items.append({
            'name': name,
            'line': symbol.get('line', 0),
            'level': symbol.get('level', '??'),
            'usage_count': var_info.get('references', 0),
        })

    # Sort by usage and apply limit
    data_items.sort(key=lambda x: x['usage_count'], reverse=True)
    if top_n_data_items >= 0:
        data_items = data_items[:top_n_data_items]

    if data_items:
        map_lines.append("|")
        map_lines.append(f"+-- Top {len(data_items)} Data Items:")
        for item in data_items:
            map_lines.append(f"|   - {item['name']}  (Level {item['level']})  [Used: {item['usage_count']}x]")

    map_lines.append("|")
    map_lines.append("=" * 80)

    return "\n".join(map_lines)


# ============================================================================
# CONFIGURATION HELPERS
# ============================================================================

def get_mandatory_config_from_dict(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract mandatory elements configuration from a config dictionary.

    Args:
        config: Configuration dictionary (from config_loader)

    Returns:
        Dictionary with mandatory elements configuration
    """
    pm_config = config.get('program_map', {})
    mandatory_config = pm_config.get('mandatory_elements', {})

    return {
        'enabled': mandatory_config.get('enabled', True),
        'entry_point_patterns': mandatory_config.get(
            'entry_point_patterns',
            DEFAULT_ENTRY_POINT_PATTERNS
        ),
        'error_handler_patterns': mandatory_config.get(
            'error_handler_patterns',
            DEFAULT_ERROR_HANDLER_PATTERNS
        ),
    }
