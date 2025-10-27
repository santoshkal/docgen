"""
Source Code Integration Module

High-level functions to integrate source extraction with documentation generation.
This module ties together:
- source_extractor.py (extraction functions)
- section_requirements.py (configuration)
- multi_file_resolver.py (Phase 3 - copybooks and called programs)
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

# Phase 3: Multi-file support imports
try:
    from multi_file_resolver import CopybookResolver, CalledProgramResolver
    MULTI_FILE_AVAILABLE = True
except ImportError:
    MULTI_FILE_AVAILABLE = False


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


# ==================================================
# Phase 3: Multi-File Support Functions (Day 9)
# ==================================================

def extract_source_with_copybooks(
    section_id: str,
    cobol_file_path: str,
    copybook_resolver: Optional['CopybookResolver'] = None,
    compress: bool = True
) -> Optional[str]:
    """
    Extract source code including referenced copybooks.

    Args:
        section_id: Section identifier (e.g., '2_data_structures')
        cobol_file_path: Path to main COBOL file
        copybook_resolver: CopybookResolver instance
        compress: Whether to compress source

    Returns:
        Source code with copybook content included
    """
    if not MULTI_FILE_AVAILABLE or copybook_resolver is None:
        # Fallback to regular extraction
        return extract_source_for_section(section_id, cobol_file_path, compress=compress)

    # First, extract main file source
    main_source = extract_source_for_section(section_id, cobol_file_path, compress=compress)

    if main_source is None:
        return None

    # Resolve copybooks
    try:
        copybooks = copybook_resolver.resolve_all_copybooks(cobol_file_path)

        if not copybooks:
            return main_source

        # Build combined source with copybook content
        parts = [main_source]
        parts.append("\n\n### Referenced Copybooks:\n")

        for copybook_name, copybook_content in copybooks.items():
            parts.append(f"\n**{copybook_name}:**\n")
            parts.append("```cobol\n")
            if compress:
                copybook_content = compress_source_code(copybook_content)
            parts.append(copybook_content)
            parts.append("\n```\n")

        return ''.join(parts)

    except Exception as e:
        # Log error but return main source
        print(f"Warning: Failed to resolve copybooks: {e}")
        return main_source


def extract_source_with_called_programs(
    section_id: str,
    cobol_file_path: str,
    called_program_resolver: Optional['CalledProgramResolver'] = None,
    compress: bool = True
) -> Optional[str]:
    """
    Extract source code including information about called programs.

    Args:
        section_id: Section identifier (e.g., '3_business_logic')
        cobol_file_path: Path to main COBOL file
        called_program_resolver: CalledProgramResolver instance
        compress: Whether to compress source

    Returns:
        Source code with called program information
    """
    if not MULTI_FILE_AVAILABLE or called_program_resolver is None:
        # Fallback to regular extraction
        return extract_source_for_section(section_id, cobol_file_path, compress=compress)

    # First, extract main file source
    main_source = extract_source_for_section(section_id, cobol_file_path, compress=compress)

    if main_source is None:
        return None

    # Resolve called programs
    try:
        called_programs = called_program_resolver.resolve_all_calls(cobol_file_path)

        if not called_programs:
            return main_source

        # Add called program information
        parts = [main_source]
        parts.append("\n\n### Called Programs:\n")

        for prog_name, info in called_programs.items():
            parts.append(f"\n**{prog_name}:**\n")
            if info.get('path'):
                parts.append(f"- Location: `{info['path']}`\n")
                if info.get('purpose'):
                    parts.append(f"- Purpose: {info['purpose']}\n")
            else:
                parts.append(f"- Status: Not found in codebase\n")

        return ''.join(parts)

    except Exception as e:
        # Log error but return main source
        print(f"Warning: Failed to resolve called programs: {e}")
        return main_source


def extract_source_multi_file(
    section_id: str,
    cobol_file_path: str,
    copybook_resolver: Optional['CopybookResolver'] = None,
    called_program_resolver: Optional['CalledProgramResolver'] = None,
    compress: bool = True
) -> Optional[str]:
    """
    Extract source code with full multi-file support (copybooks + called programs).

    This is the complete Phase 3 integration combining copybooks and called programs.

    Args:
        section_id: Section identifier
        cobol_file_path: Path to main COBOL file
        copybook_resolver: CopybookResolver instance
        called_program_resolver: CalledProgramResolver instance
        compress: Whether to compress source

    Returns:
        Comprehensive source code with all multi-file context
    """
    if not MULTI_FILE_AVAILABLE:
        return extract_source_for_section(section_id, cobol_file_path, compress=compress)

    # Start with copybooks (for data sections)
    if section_id.startswith('2_') or 'data' in section_id.lower():
        source = extract_source_with_copybooks(
            section_id, cobol_file_path, copybook_resolver, compress
        )
    # For logic sections, include called programs
    elif section_id.startswith('3_') or 'logic' in section_id.lower():
        source = extract_source_with_called_programs(
            section_id, cobol_file_path, called_program_resolver, compress
        )
    else:
        # Default: regular extraction
        source = extract_source_for_section(section_id, cobol_file_path, compress=compress)

    return source
