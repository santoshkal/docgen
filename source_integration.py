"""
Source Code Integration Module

High-level functions to integrate source extraction with documentation generation.
This module ties together:
- source_extractor.py (extraction functions)
- section_requirements.py (configuration)
"""

from typing import Dict, List, Any, Optional
from source_extractor import (
    extract_division,
    find_division_boundaries,
    extract_paragraph,
    extract_paragraphs_by_names,
    deduplicate_source_extracts,
    compress_source_code,
    add_section_markers,
    estimate_token_count
)
from section_requirements import (
    should_extract_source,
    get_divisions_for_section
)


def extract_source_for_section(
    section_name: str,
    cobol_file_path: str,
    paragraph_metadata: Optional[Dict[str, Dict[str, int]]] = None,
    compress: bool = True
) -> Optional[str]:
    """
    Extract source code for a documentation section.

    Args:
        section_name: Section name (e.g., '2_data_structures')
        cobol_file_path: Path to the COBOL source file
        paragraph_metadata: Optional paragraph metadata for targeted extraction
        compress: Whether to compress source (remove comments/blank lines)

    Returns:
        Extracted and formatted source code, or None if not needed

    Examples:
        >>> source = extract_source_for_section('2_data_structures', 'program.cbl')
        >>> 'DATA DIVISION' in source
        True
    """
    # Check if this section needs source extraction
    if not should_extract_source(section_name):
        return None

    # Get divisions to extract
    divisions = get_divisions_for_section(section_name)
    if not divisions:
        return None

    # Extract divisions
    sections = []
    try:
        for division_name in divisions:
            source = extract_division(cobol_file_path, division_name)
            if source:
                # Optionally compress
                if compress:
                    source = compress_source_code(source)

                sections.append({
                    'name': division_name,
                    'source': source
                })
    except FileNotFoundError:
        # File doesn't exist - return None
        return None
    except Exception:
        # Other errors - return None gracefully
        return None

    # If paragraphs provided and this is PROCEDURE DIVISION section, use those
    if paragraph_metadata and 'PROCEDURE DIVISION' in divisions:
        # This could be enhanced to extract specific paragraphs
        pass

    # Format with markdown markers
    if sections:
        return add_section_markers(sections)

    return None


def extract_source_for_all_sections(
    cobol_file_path: str,
    paragraph_metadata: Optional[Dict[str, Dict[str, int]]] = None,
    compress: bool = True
) -> Dict[str, Optional[str]]:
    """
    Extract source code for all documentation sections.

    Args:
        cobol_file_path: Path to the COBOL source file
        paragraph_metadata: Optional paragraph metadata
        compress: Whether to compress source

    Returns:
        Dictionary mapping section names to extracted source (None if not needed)

    Examples:
        >>> sources = extract_source_for_all_sections('program.cbl')
        >>> sources['2_data_structures'] is not None
        True
    """
    from section_requirements import SECTION_REQUIREMENTS

    results = {}
    for section_name in SECTION_REQUIREMENTS.keys():
        source = extract_source_for_section(
            section_name,
            cobol_file_path,
            paragraph_metadata,
            compress
        )
        results[section_name] = source

    return results


def get_extraction_stats(sources: Dict[str, Optional[str]]) -> Dict[str, Any]:
    """
    Get statistics about extracted source code.

    Args:
        sources: Dictionary of section_name -> source_code

    Returns:
        Statistics dictionary with counts and token estimates

    Examples:
        >>> sources = {'2_data_structures': 'DATA DIVISION...'}
        >>> stats = get_extraction_stats(sources)
        >>> stats['sections_with_source'] >= 0
        True
    """
    sections_with_source = sum(1 for s in sources.values() if s is not None)
    total_chars = sum(len(s) for s in sources.values() if s is not None)
    total_tokens = sum(estimate_token_count(s) for s in sources.values() if s is not None)

    return {
        'total_sections': len(sources),
        'sections_with_source': sections_with_source,
        'sections_without_source': len(sources) - sections_with_source,
        'total_characters': total_chars,
        'estimated_tokens': total_tokens
    }


def build_section_context_with_source(
    section_name: str,
    cobol_file_path: str,
    metadata: Dict[str, Any],
    compress: bool = True
) -> str:
    """
    Build section context including extracted source code.

    This function would integrate with the existing build_section_context()
    in cobol_doc_agent.py.

    Args:
        section_name: Section name
        cobol_file_path: Path to COBOL file
        metadata: Metadata dictionary (ctags, superbol, etc.)
        compress: Whether to compress source

    Returns:
        Context string with source code included

    Examples:
        >>> context = build_section_context_with_source('2_data_structures', 'prog.cbl', {})
        >>> len(context) > 0
        True
    """
    # Build base context (this would call existing function)
    context_parts = [
        f"# Section: {section_name}",
        ""
    ]

    # Add metadata summary
    if metadata:
        context_parts.append("## Metadata")
        context_parts.append(f"- File: {cobol_file_path}")
        context_parts.append("")

    # Extract and add source code if needed
    paragraph_metadata = metadata.get('paragraphs', {}) if metadata else None
    source = extract_source_for_section(
        section_name,
        cobol_file_path,
        paragraph_metadata,
        compress
    )

    if source:
        context_parts.append("## Source Code")
        context_parts.append("")
        context_parts.append(source)

    return '\n'.join(context_parts)
