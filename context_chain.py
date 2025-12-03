"""
Context Chain Module

Provides context chaining for cross-section consistency in full context mode.
Stores previous section outputs and makes them available to subsequent sections,
enabling the LLM to maintain consistency across the generated documentation.

US-4.1: Context Chaining Mechanism
"""

from typing import Any, Dict, List, Optional


# Section order for context chaining
# Earlier sections provide context for later sections
FULL_CONTEXT_SECTION_ORDER: List[str] = [
    'executive-summary',      # First - provides high-level context
    'key-responsibilities',   # Second - builds on summary
    'overview',               # Third - program structure
    'business-logic',         # Fourth - detailed logic
    'data-flow-analysis',     # Fifth - data movement
]


class ContextChain:
    """
    Stores and manages section outputs for context chaining.

    Context chaining allows previous section outputs to be included in
    subsequent section prompts, enabling cross-section consistency.

    Attributes:
        _sections: Dictionary mapping section IDs to their generated content
    """

    def __init__(self):
        """Initialize an empty context chain."""
        self._sections: Dict[str, str] = {}

    def add_section_output(self, section_id: str, content: str) -> None:
        """
        Add a section's generated output to the chain.

        Args:
            section_id: The section identifier (e.g., 'executive-summary')
            content: The generated content for this section
        """
        self._sections[section_id] = content

    def has_section(self, section_id: str) -> bool:
        """
        Check if a section output exists in the chain.

        Args:
            section_id: The section identifier to check

        Returns:
            True if the section exists in the chain
        """
        return section_id in self._sections

    def get_section_output(self, section_id: str) -> Optional[str]:
        """
        Get a section's output from the chain.

        Args:
            section_id: The section identifier

        Returns:
            The section's content, or None if not found
        """
        return self._sections.get(section_id)

    def get_all_sections(self) -> List[str]:
        """
        Get list of all section IDs in the chain.

        Returns:
            List of section identifiers
        """
        return list(self._sections.keys())

    def clear(self) -> None:
        """Clear all section outputs from the chain."""
        self._sections.clear()

    def to_dict(self) -> Dict[str, str]:
        """
        Convert the chain to a dictionary.

        Useful for serialization or storing in AgentState.

        Returns:
            Dictionary of section_id -> content
        """
        return dict(self._sections)

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> 'ContextChain':
        """
        Create a ContextChain from a dictionary.

        Args:
            data: Dictionary of section_id -> content

        Returns:
            New ContextChain instance with the data
        """
        chain = cls()
        chain._sections = dict(data)
        return chain


def get_previous_sections(current_section: str) -> List[str]:
    """
    Get the list of sections that come before the current section.

    Args:
        current_section: The current section being processed

    Returns:
        List of section IDs that should be included as previous context
    """
    current_lower = current_section.lower()

    # Find index of current section in the order
    try:
        current_idx = [s.lower() for s in FULL_CONTEXT_SECTION_ORDER].index(current_lower)
    except ValueError:
        # Section not in order list - no previous context
        return []

    # Return all sections before the current one
    return FULL_CONTEXT_SECTION_ORDER[:current_idx]


def should_use_chaining(
    use_full_context_mode: bool,
    chaining_enabled: bool
) -> bool:
    """
    Determine if context chaining should be used.

    Both full context mode and chaining must be enabled.

    Args:
        use_full_context_mode: Whether full context mode is enabled
        chaining_enabled: Whether context chaining is enabled

    Returns:
        True if chaining should be used
    """
    return use_full_context_mode and chaining_enabled


def build_chained_context(
    current_section: str,
    chain: ContextChain,
    enabled: bool = True,
    max_tokens: Optional[int] = None
) -> str:
    """
    Build context string from previous sections.

    Args:
        current_section: The section currently being processed
        chain: ContextChain containing previous outputs
        enabled: Whether chaining is enabled (False returns empty string)
        max_tokens: Optional maximum token limit (approximate)

    Returns:
        Formatted string containing previous section outputs
    """
    if not enabled:
        return ""

    previous_sections = get_previous_sections(current_section)

    if not previous_sections:
        return ""

    # Build context from previous sections
    context_parts = []
    total_chars = 0

    for section_id in previous_sections:
        if chain.has_section(section_id):
            content = chain.get_section_output(section_id)
            if content:
                # Check token limit (approximate: 1 token ≈ 4 chars)
                if max_tokens:
                    max_chars = max_tokens * 4
                    if total_chars + len(content) > max_chars:
                        # Truncate this section
                        remaining = max_chars - total_chars
                        if remaining > 100:  # Only include if enough space
                            content = content[:remaining] + "..."
                        else:
                            break

                section_header = section_id.replace('-', ' ').title()
                context_parts.append(f"## Previously Generated: {section_header}\n\n{content}")
                total_chars += len(content)

    if not context_parts:
        return ""

    header = "# Context from Previous Sections\n\nThe following sections have already been generated. Use them for consistency:\n\n"
    return header + "\n\n---\n\n".join(context_parts)


def get_chaining_config_from_state(state: dict) -> dict:
    """
    Extract context chaining configuration from agent state.

    Args:
        state: AgentState dictionary

    Returns:
        Dictionary with chaining configuration
    """
    return {
        'enabled': state.get('context_chaining_enabled', False),
        'max_tokens': state.get('context_chaining_max_tokens', None),
    }
