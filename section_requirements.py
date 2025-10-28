"""
Section Requirements Configuration

Defines which sections require source code extraction and which divisions to extract.
"""

from typing import Dict, List, Optional, TypedDict


class SectionRequirement(TypedDict):
    """Configuration for a documentation section"""
    extract_source: bool
    divisions: List[str]


# Section requirements: defines which sections need source code extraction
SECTION_REQUIREMENTS: Dict[str, SectionRequirement] = {
    # Legacy section IDs (kept for backward compatibility)
    '1_program_overview': {
        'extract_source': False,
        'divisions': []
    },
    '2_data_structures': {
        'extract_source': True,
        'divisions': ['DATA DIVISION']
    },
    '3_business_logic': {
        'extract_source': True,
        'divisions': ['PROCEDURE DIVISION']
    },
    '4_file_operations': {
        'extract_source': True,
        'divisions': ['PROCEDURE DIVISION']
    },
    '5_database_operations': {
        'extract_source': True,
        'divisions': ['PROCEDURE DIVISION']
    },
    '6_technical_details': {
        'extract_source': True,
        'divisions': ['DATA DIVISION', 'PROCEDURE DIVISION']
    },
    '7_error_handling': {
        'extract_source': True,
        'divisions': ['PROCEDURE DIVISION']
    },
    '8_dependencies': {
        'extract_source': False,
        'divisions': []
    },
    '9_performance': {
        'extract_source': True,
        'divisions': ['PROCEDURE DIVISION']
    },
    '10_security': {
        'extract_source': True,
        'divisions': ['PROCEDURE DIVISION']
    },
    '11_maintenance': {
        'extract_source': False,
        'divisions': []
    },

    # New template section IDs (from cobol-doc-template.yaml)
    # Document Header sections
    'document-header': {
        'extract_source': False,
        'divisions': []
    },
    'metadata-info': {
        'extract_source': False,
        'divisions': []
    },

    # Executive Summary
    'executive-summary': {
        'extract_source': False,
        'divisions': []
    },

    # Program Structure sections
    'program-structure': {
        'extract_source': False,
        'divisions': []
    },
    'divisions-overview': {
        'extract_source': False,
        'divisions': []
    },
    'copybooks-referenced': {
        'extract_source': False,
        'divisions': []
    },
    'data-structures': {
        'extract_source': True,
        'divisions': ['DATA DIVISION']
    },

    # Control Flow Analysis sections
    'control-flow-analysis': {
        'extract_source': False,
        'divisions': []
    },
    'cfg-with-calls-diagram': {
        'extract_source': False,
        'divisions': []
    },
    'external-call-context': {
        'extract_source': True,
        'divisions': ['PROCEDURE DIVISION']
    },
    'paragraph-complexity': {
        'extract_source': False,
        'divisions': []
    },

    # Data Flow Analysis sections
    'data-flow-analysis': {
        'extract_source': False,
        'divisions': []
    },
    'dfa-diagram': {
        'extract_source': False,
        'divisions': []
    },
    'data-transformations': {
        'extract_source': True,  # NEEDS source to find MOVE/COMPUTE/STRING/UNSTRING
        'divisions': ['PROCEDURE DIVISION']
    },

    # Inter-Program Communication sections
    'inter-program-communication': {
        'extract_source': False,
        'divisions': []
    },
    'call-frequency-heatmap': {
        'extract_source': False,
        'divisions': []
    },
    'program-call-diagram': {
        'extract_source': False,
        'divisions': []
    },
    'system-wide-dependencies': {
        'extract_source': False,
        'divisions': []
    },
    'call-details-with-context': {
        'extract_source': True,
        'divisions': ['PROCEDURE DIVISION']
    },

    # Business Logic Explanation sections
    'business-logic': {
        'extract_source': False,
        'divisions': []
    },
    'execution-flow-sequence': {
        'extract_source': True,
        'divisions': ['PROCEDURE DIVISION']
    },
    'business-operations-catalog': {
        'extract_source': True,
        'divisions': ['PROCEDURE DIVISION']
    },

    # Error Handling Strategy
    'error-handling': {
        'extract_source': True,
        'divisions': ['PROCEDURE DIVISION']
    },

    # Technical Details sections
    'technical-details': {
        'extract_source': False,
        'divisions': []
    },
    'code-metrics': {
        'extract_source': False,
        'divisions': []
    },
    'dependencies-matrix': {
        'extract_source': False,
        'divisions': []
    },

    # Code References
    'code-references': {
        'extract_source': True,
        'divisions': ['IDENTIFICATION DIVISION', 'ENVIRONMENT DIVISION', 'DATA DIVISION', 'PROCEDURE DIVISION']
    },

    # Metadata Appendix sections
    'metadata-appendix': {
        'extract_source': False,
        'divisions': []
    },
    'superbol-summary': {
        'extract_source': False,
        'divisions': []
    },
    'gnucobol-summary': {
        'extract_source': False,
        'divisions': []
    },
    'ctags-summary': {
        'extract_source': False,
        'divisions': []
    }
}


def get_section_requirements(section_name: str) -> Optional[SectionRequirement]:
    """
    Get requirements for a specific section.

    Args:
        section_name: Name of the section (e.g., '2_data_structures')

    Returns:
        Section requirements dict or None if not found

    Examples:
        >>> req = get_section_requirements('2_data_structures')
        >>> req['extract_source']
        True
    """
    return SECTION_REQUIREMENTS.get(section_name)


def should_extract_source(section_name: str) -> bool:
    """
    Check if a section requires source code extraction.

    Args:
        section_name: Name of the section

    Returns:
        True if source extraction is required, False otherwise

    Examples:
        >>> should_extract_source('2_data_structures')
        True
        >>> should_extract_source('1_program_overview')
        False
    """
    req = get_section_requirements(section_name)
    if req is None:
        return False
    return req['extract_source']


def get_divisions_for_section(section_name: str) -> List[str]:
    """
    Get list of divisions to extract for a section.

    Args:
        section_name: Name of the section

    Returns:
        List of division names (e.g., ['DATA DIVISION', 'PROCEDURE DIVISION'])

    Examples:
        >>> get_divisions_for_section('2_data_structures')
        ['DATA DIVISION']
    """
    req = get_section_requirements(section_name)
    if req is None:
        return []
    return req['divisions']
