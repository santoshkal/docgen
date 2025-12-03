"""
Dynamic Program Limits Module

Provides automatic adjustment of program map limits based on program size.
This enables small programs to show all elements while large programs
show a meaningful, prioritized subset.

US-1.3: Dynamic Program Map Limits Based on Program Size

Size Categories:
- SMALL: < 100 paragraphs → Show all elements
- MEDIUM: 100-499 paragraphs → Top 200 paragraphs, top 100 data items
- LARGE: 500+ paragraphs → Top 300 paragraphs, top 150 data items
"""

from enum import Enum
from typing import Any, Dict, Optional


class ProgramSizeCategory(Enum):
    """
    Categorization of COBOL program size based on paragraph count.

    Categories:
        SMALL: Programs with fewer than 100 paragraphs
        MEDIUM: Programs with 100-499 paragraphs
        LARGE: Programs with 500 or more paragraphs
    """
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


# Default thresholds for size categorization
DEFAULT_THRESHOLDS = {
    'small_threshold': 100,   # < 100 paragraphs = SMALL
    'large_threshold': 500    # >= 500 paragraphs = LARGE, else MEDIUM
}

# Default limits for each size category
DEFAULT_LIMITS = {
    ProgramSizeCategory.SMALL: {
        'top_n_paragraphs': -1,   # Show all
        'top_n_data_items': -1    # Show all
    },
    ProgramSizeCategory.MEDIUM: {
        'top_n_paragraphs': 200,
        'top_n_data_items': 100
    },
    ProgramSizeCategory.LARGE: {
        'top_n_paragraphs': 300,
        'top_n_data_items': 150
    }
}


def count_paragraphs(metadata: Dict[str, Any]) -> int:
    """
    Count the number of paragraphs and sections in the program metadata.

    Args:
        metadata: Dictionary containing ctags_outline with symbols

    Returns:
        Count of paragraphs and sections
    """
    ctags = metadata.get('ctags_outline', {})
    symbols = ctags.get('symbols', [])

    paragraph_count = 0
    for symbol in symbols:
        kind = symbol.get('kind', '')
        if kind in ('paragraph', 'section'):
            paragraph_count += 1

    return paragraph_count


def detect_program_size(
    metadata: Dict[str, Any],
    thresholds: Optional[Dict[str, int]] = None
) -> ProgramSizeCategory:
    """
    Detect the program size category based on metadata.

    Categorization is based on paragraph/section count:
    - SMALL: < small_threshold paragraphs (default: 100)
    - MEDIUM: >= small_threshold and < large_threshold (default: 100-499)
    - LARGE: >= large_threshold paragraphs (default: 500+)

    Args:
        metadata: Dictionary containing ctags_outline, superbol_cfg, etc.
        thresholds: Optional custom thresholds dict with:
                   - 'small_threshold': int (default: 100)
                   - 'large_threshold': int (default: 500)

    Returns:
        ProgramSizeCategory enum value (SMALL, MEDIUM, or LARGE)
    """
    # Use custom or default thresholds
    if thresholds is None:
        thresholds = DEFAULT_THRESHOLDS

    small_threshold = thresholds.get('small_threshold', DEFAULT_THRESHOLDS['small_threshold'])
    large_threshold = thresholds.get('large_threshold', DEFAULT_THRESHOLDS['large_threshold'])

    # Count paragraphs from CTags
    paragraph_count = count_paragraphs(metadata)

    # Categorize based on count
    if paragraph_count < small_threshold:
        return ProgramSizeCategory.SMALL
    elif paragraph_count >= large_threshold:
        return ProgramSizeCategory.LARGE
    else:
        return ProgramSizeCategory.MEDIUM


def get_dynamic_limits(
    metadata: Dict[str, Any],
    thresholds: Optional[Dict[str, int]] = None,
    custom_limits: Optional[Dict[ProgramSizeCategory, Dict[str, int]]] = None
) -> Dict[str, Any]:
    """
    Get dynamic limits based on program size.

    Automatically detects program size and returns appropriate limits for
    the program map generation.

    Args:
        metadata: Dictionary containing ctags_outline, superbol_cfg, etc.
        thresholds: Optional custom thresholds for size categorization
        custom_limits: Optional custom limits per category, e.g.:
                      {
                          ProgramSizeCategory.SMALL: {'top_n_paragraphs': -1, 'top_n_data_items': -1},
                          ProgramSizeCategory.MEDIUM: {'top_n_paragraphs': 150, 'top_n_data_items': 75},
                          ProgramSizeCategory.LARGE: {'top_n_paragraphs': 250, 'top_n_data_items': 125}
                      }

    Returns:
        Dictionary with:
        - 'top_n_paragraphs': int (-1 for all, or positive limit)
        - 'top_n_data_items': int (-1 for all, or positive limit)
        - 'size_category': ProgramSizeCategory enum value
    """
    # Detect program size
    size_category = detect_program_size(metadata, thresholds)

    # Get limits for this category
    if custom_limits is not None and size_category in custom_limits:
        limits = custom_limits[size_category]
    else:
        limits = DEFAULT_LIMITS.get(size_category, DEFAULT_LIMITS[ProgramSizeCategory.SMALL])

    return {
        'top_n_paragraphs': limits['top_n_paragraphs'],
        'top_n_data_items': limits['top_n_data_items'],
        'size_category': size_category
    }


def get_limits_from_config(config: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Extract dynamic limits configuration from a loaded config dictionary.

    Args:
        config: Configuration dictionary (from config_loader)

    Returns:
        Dictionary with thresholds and limits if dynamic_limits is enabled,
        None if dynamic limits is disabled or not configured
    """
    pm_config = config.get('program_map', {})
    dynamic_config = pm_config.get('dynamic_limits', {})

    if not dynamic_config.get('enabled', False):
        return None

    # Extract thresholds
    thresholds = {
        'small_threshold': dynamic_config.get('small_threshold', DEFAULT_THRESHOLDS['small_threshold']),
        'large_threshold': dynamic_config.get('large_threshold', DEFAULT_THRESHOLDS['large_threshold'])
    }

    # Extract custom limits if provided
    custom_limits = {}

    if 'small' in dynamic_config:
        custom_limits[ProgramSizeCategory.SMALL] = {
            'top_n_paragraphs': dynamic_config['small'].get('paragraphs', -1),
            'top_n_data_items': dynamic_config['small'].get('data_items', -1)
        }

    if 'medium' in dynamic_config:
        custom_limits[ProgramSizeCategory.MEDIUM] = {
            'top_n_paragraphs': dynamic_config['medium'].get('paragraphs', 200),
            'top_n_data_items': dynamic_config['medium'].get('data_items', 100)
        }

    if 'large' in dynamic_config:
        custom_limits[ProgramSizeCategory.LARGE] = {
            'top_n_paragraphs': dynamic_config['large'].get('paragraphs', 300),
            'top_n_data_items': dynamic_config['large'].get('data_items', 150)
        }

    return {
        'thresholds': thresholds,
        'custom_limits': custom_limits if custom_limits else None
    }
