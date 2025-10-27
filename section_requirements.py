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
