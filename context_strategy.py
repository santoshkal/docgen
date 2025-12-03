"""
Context Strategy Module

Provides strategy selection for section context generation.
Determines whether a section should use full context (complete source + metadata)
or filtered context (chunked/filtered for token efficiency).

US-2.2: Section Context Strategy Selection

Key Features:
- FULL_CONTEXT_SECTIONS constant defining target sections
- get_context_strategy() function for strategy selection
- should_use_full_context() helper for boolean check
- ContextStrategy enum for type-safe strategy values
"""

from enum import Enum
from typing import List, Optional


class ContextStrategy(Enum):
    """Enum representing context generation strategies."""
    FULL = 'full'         # Complete source + metadata + enhanced program map
    FILTERED = 'filtered'  # Chunked/filtered context for token efficiency


# Default sections that benefit from full context mode
# These sections require complete source code visibility for accurate generation
FULL_CONTEXT_SECTIONS: List[str] = [
    'executive-summary',      # Needs full program overview
    'key-responsibilities',   # Needs main driver analysis
    'business-logic',         # Needs complete code flow
    'overview',               # Needs full structure
    'data-flow-analysis',     # Needs complete data paths
]


def get_context_strategy(
    section_id: str,
    full_context_sections: Optional[List[str]] = None,
    use_full_context_mode: bool = True
) -> str:
    """
    Determine the context generation strategy for a section.

    Args:
        section_id: The ID of the section being processed
        full_context_sections: List of section IDs that should use full context.
                              If None, uses FULL_CONTEXT_SECTIONS default.
        use_full_context_mode: Whether full context mode is enabled globally.
                              If False, always returns 'filtered'.

    Returns:
        Strategy string: 'full' or 'filtered'
    """
    # If full context mode is disabled, always use filtered
    if not use_full_context_mode:
        return ContextStrategy.FILTERED.value

    # Use default sections if none provided
    if full_context_sections is None:
        full_context_sections = FULL_CONTEXT_SECTIONS

    # Empty list means no sections use full context
    if not full_context_sections:
        return ContextStrategy.FILTERED.value

    # Case-insensitive matching
    section_id_lower = section_id.lower()
    sections_lower = [s.lower() for s in full_context_sections]

    if section_id_lower in sections_lower:
        return ContextStrategy.FULL.value

    return ContextStrategy.FILTERED.value


def should_use_full_context(
    section_id: str,
    use_full_context_mode: bool,
    full_context_sections: Optional[List[str]] = None
) -> bool:
    """
    Check if a section should use full context mode.

    This is a convenience helper that returns a boolean instead of a strategy string.

    Args:
        section_id: The ID of the section being processed
        use_full_context_mode: Whether full context mode is enabled globally
        full_context_sections: List of section IDs that should use full context.
                              If None, uses FULL_CONTEXT_SECTIONS default.

    Returns:
        True if section should use full context, False otherwise
    """
    strategy = get_context_strategy(
        section_id=section_id,
        full_context_sections=full_context_sections,
        use_full_context_mode=use_full_context_mode
    )
    return strategy == ContextStrategy.FULL.value


def get_strategy_for_state(
    section_id: str,
    state: dict
) -> str:
    """
    Get context strategy using AgentState values.

    Convenience function that extracts full context settings from state dict.

    Args:
        section_id: The ID of the section being processed
        state: AgentState dict containing full context configuration

    Returns:
        Strategy string: 'full' or 'filtered'
    """
    use_full_context_mode = state.get('use_full_context_mode', False)
    full_context_sections = state.get('full_context_sections', [])

    return get_context_strategy(
        section_id=section_id,
        full_context_sections=full_context_sections,
        use_full_context_mode=use_full_context_mode
    )
