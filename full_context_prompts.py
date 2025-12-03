"""
Full Context Prompts Module

Provides specialized prompt construction for full context mode sections.
Each section has a dedicated prompt builder that formats the full context
(source code + metadata + program map) for optimal LLM understanding.

US-3.1: Executive Summary with Full Context
US-3.2: Key Responsibilities with Full Context
US-3.3: Business Logic with Full Context
US-3.4: Overview with Full Context
US-3.5: Data Flow with Full Context
"""

from typing import Any, Dict, Optional


def build_full_context_prompt(
    section_id: str,
    source_code: str,
    metadata: Dict[str, Any],
    program_map: str,
    instruction: str = "",
    program_name: str = ""
) -> str:
    """
    Build a full context prompt for any section.

    This is the main entry point that routes to section-specific prompt builders.

    Args:
        section_id: The section identifier (e.g., 'executive-summary')
        source_code: Complete COBOL source code
        metadata: Dictionary with all metadata sources
        program_map: Formatted program map string
        instruction: Section-specific instruction from template
        program_name: Name of the COBOL program

    Returns:
        Formatted prompt string ready for LLM
    """
    # Route to section-specific builders
    section_builders = {
        'executive-summary': build_executive_summary_prompt,
        'key-responsibilities': build_key_responsibilities_prompt,
        'business-logic': build_business_logic_prompt,
        'overview': build_overview_prompt,
        'data-flow-analysis': build_data_flow_prompt,
    }

    # Normalize section ID
    section_id_lower = section_id.lower()

    builder = section_builders.get(section_id_lower, _build_generic_full_context_prompt)

    return builder(
        source_code=source_code,
        metadata=metadata,
        program_map=program_map,
        instruction=instruction,
        program_name=program_name
    )


def build_executive_summary_prompt(
    source_code: str,
    metadata: Dict[str, Any],
    program_map: str,
    instruction: str = "",
    program_name: str = ""
) -> str:
    """
    Build a full context prompt for executive summary generation.

    The executive summary should:
    - Reference IDENTIFICATION DIVISION comments (AUTHOR, REMARKS, etc.)
    - Synthesize information from narrative comments in source
    - Correlate with program structure from metadata
    - Provide a comprehensive high-level overview

    Args:
        source_code: Complete COBOL source code with all comments
        metadata: Dictionary with ctags, superbol, gnucobol data
        program_map: Formatted program map showing structure
        instruction: Section-specific instruction from template
        program_name: Name of the COBOL program

    Returns:
        Formatted prompt for executive summary generation
    """
    prompt_parts = []

    # System context
    prompt_parts.append(f"""# Executive Summary Generation - Full Context Mode

You are generating an Executive Summary for the COBOL program: {program_name or 'UNKNOWN'}

## Instructions
{instruction or 'Generate a comprehensive executive summary for this COBOL program.'}

## Context Understanding Guidelines

You have access to COMPLETE source code and metadata. Use this to:
1. **Extract narrative comments** from IDENTIFICATION DIVISION (AUTHOR, REMARKS, INSTALLATION, DATE-WRITTEN)
2. **Identify program purpose** from inline comments (lines starting with *)
3. **Understand program structure** from the program map
4. **Correlate metadata** with actual source code for accuracy

## IMPORTANT: Comment Extraction

Pay special attention to:
- AUTHOR paragraph in IDENTIFICATION DIVISION
- REMARKS or *REMARKS sections
- DATE-WRITTEN and DATE-COMPILED entries
- Comment blocks at the start of major sections (*, /*)
- Inline comments describing business logic
""")

    # Program Map section
    if program_map:
        prompt_parts.append(f"""
---
## PROGRAM MAP (Structure Overview)

This shows the program's key paragraphs, data items, and control flow:

{program_map}
""")

    # Metadata summary
    metadata_summary = _format_metadata_summary(metadata)
    if metadata_summary:
        prompt_parts.append(f"""
---
## METADATA SUMMARY

{metadata_summary}
""")

    # Source code section
    if source_code:
        prompt_parts.append(f"""
---
## COMPLETE SOURCE CODE

Below is the complete COBOL source code. Focus on extracting:
- Program identification and author information
- Narrative comments explaining business purpose
- Key data structures and their purposes
- Main processing flow

```cobol
{source_code}
```
""")

    # Output instructions
    prompt_parts.append("""
---
## Output Requirements

Generate an executive summary that:
1. States the program's primary purpose and business function
2. References specific comments from the source (if available)
3. Highlights key responsibilities derived from the code structure
4. Notes any important dates, authors, or installation information
5. Is concise but comprehensive (2-4 paragraphs)

Begin your executive summary:
""")

    return '\n'.join(prompt_parts)


def build_key_responsibilities_prompt(
    source_code: str,
    metadata: Dict[str, Any],
    program_map: str,
    instruction: str = "",
    program_name: str = ""
) -> str:
    """
    Build a full context prompt for key responsibilities generation.

    Args:
        source_code: Complete COBOL source code
        metadata: Dictionary with all metadata sources
        program_map: Formatted program map
        instruction: Section-specific instruction
        program_name: Name of the COBOL program

    Returns:
        Formatted prompt for key responsibilities generation
    """
    prompt_parts = []

    prompt_parts.append(f"""# Key Responsibilities Generation - Full Context Mode

You are generating Key Responsibilities for the COBOL program: {program_name or 'UNKNOWN'}

## Instructions
{instruction or 'Identify and describe the key responsibilities of this COBOL program.'}

## Context Understanding Guidelines

Use the complete source code and metadata to:
1. Identify main driver paragraphs (highest importance in CFG)
2. Extract responsibilities from paragraph comments
3. Correlate PERFORM statements with business functions
4. Note external program calls (CALL statements)
""")

    if program_map:
        prompt_parts.append(f"""
---
## PROGRAM MAP

{program_map}
""")

    if source_code:
        prompt_parts.append(f"""
---
## COMPLETE SOURCE CODE

```cobol
{source_code}
```
""")

    prompt_parts.append("""
---
## Output Requirements

List 4-8 key responsibilities. For each responsibility:
1. State the responsibility clearly
2. Reference the paragraph(s) that implement it
3. Note any dependencies or external calls

Begin your key responsibilities list:
""")

    return '\n'.join(prompt_parts)


def build_business_logic_prompt(
    source_code: str,
    metadata: Dict[str, Any],
    program_map: str,
    instruction: str = "",
    program_name: str = ""
) -> str:
    """
    Build a full context prompt for business logic explanation.

    Args:
        source_code: Complete COBOL source code
        metadata: Dictionary with all metadata sources
        program_map: Formatted program map
        instruction: Section-specific instruction
        program_name: Name of the COBOL program

    Returns:
        Formatted prompt for business logic explanation
    """
    prompt_parts = []

    prompt_parts.append(f"""# Business Logic Explanation - Full Context Mode

You are explaining the Business Logic for the COBOL program: {program_name or 'UNKNOWN'}

## Instructions
{instruction or 'Explain the business logic implemented in this COBOL program.'}

## Context Understanding Guidelines

Synthesize information from:
1. **Source code comments** - Extract business rules from inline comments
2. **Control flow (CFG)** - Understand execution paths
3. **Data flow** - Track how data is transformed
4. **Paragraph structure** - Identify logical groupings
""")

    if program_map:
        prompt_parts.append(f"""
---
## PROGRAM MAP

{program_map}
""")

    metadata_summary = _format_metadata_summary(metadata)
    if metadata_summary:
        prompt_parts.append(f"""
---
## METADATA

{metadata_summary}
""")

    if source_code:
        prompt_parts.append(f"""
---
## COMPLETE SOURCE CODE

```cobol
{source_code}
```
""")

    prompt_parts.append("""
---
## Output Requirements

Explain the business logic by:
1. Describing the main processing flow
2. Identifying key business rules and conditions
3. Explaining data transformations
4. Noting decision points and branching logic
5. Referencing specific code sections where helpful

Begin your business logic explanation:
""")

    return '\n'.join(prompt_parts)


def build_overview_prompt(
    source_code: str,
    metadata: Dict[str, Any],
    program_map: str,
    instruction: str = "",
    program_name: str = ""
) -> str:
    """
    Build a full context prompt for program overview generation.

    Args:
        source_code: Complete COBOL source code
        metadata: Dictionary with all metadata sources
        program_map: Formatted program map
        instruction: Section-specific instruction
        program_name: Name of the COBOL program

    Returns:
        Formatted prompt for overview generation
    """
    prompt_parts = []

    prompt_parts.append(f"""# Program Overview Generation - Full Context Mode

You are generating a Program Overview for: {program_name or 'UNKNOWN'}

## Instructions
{instruction or 'Generate a structural overview of this COBOL program.'}

## Context Understanding Guidelines

Use the complete context to describe:
1. **Program structure** - Divisions and their contents
2. **Data organization** - Key data structures and files
3. **Processing structure** - Main paragraphs and their relationships
4. **External interfaces** - Called programs, files, databases
""")

    if program_map:
        prompt_parts.append(f"""
---
## PROGRAM MAP

{program_map}
""")

    if source_code:
        prompt_parts.append(f"""
---
## COMPLETE SOURCE CODE

```cobol
{source_code}
```
""")

    prompt_parts.append("""
---
## Output Requirements

Provide a program overview covering:
1. Program identification and purpose
2. Division structure (what each contains)
3. Key data structures
4. Main processing sections
5. External dependencies

Begin your program overview:
""")

    return '\n'.join(prompt_parts)


def build_data_flow_prompt(
    source_code: str,
    metadata: Dict[str, Any],
    program_map: str,
    instruction: str = "",
    program_name: str = ""
) -> str:
    """
    Build a full context prompt for data flow analysis.

    Args:
        source_code: Complete COBOL source code
        metadata: Dictionary with all metadata sources
        program_map: Formatted program map
        instruction: Section-specific instruction
        program_name: Name of the COBOL program

    Returns:
        Formatted prompt for data flow analysis
    """
    prompt_parts = []

    prompt_parts.append(f"""# Data Flow Analysis - Full Context Mode

You are analyzing Data Flow for the COBOL program: {program_name or 'UNKNOWN'}

## Instructions
{instruction or 'Analyze the data flow in this COBOL program.'}

## Context Understanding Guidelines

Trace data through the program by:
1. **Identifying data sources** - File reads, external inputs
2. **Tracking transformations** - MOVE, COMPUTE, STRING, UNSTRING
3. **Following data destinations** - File writes, outputs, external calls
4. **Noting intermediate storage** - Working storage variables
""")

    if program_map:
        prompt_parts.append(f"""
---
## PROGRAM MAP

{program_map}
""")

    if source_code:
        prompt_parts.append(f"""
---
## COMPLETE SOURCE CODE

Pay attention to:
- READ and WRITE statements
- MOVE and COMPUTE statements
- Data transformations (STRING, UNSTRING, INSPECT)
- CALL statement parameters

```cobol
{source_code}
```
""")

    prompt_parts.append("""
---
## Output Requirements

Describe the data flow:
1. Key data inputs (files, parameters)
2. Major data transformations
3. Data outputs (files, return values)
4. Critical data paths through the program

Begin your data flow analysis:
""")

    return '\n'.join(prompt_parts)


def _build_generic_full_context_prompt(
    source_code: str,
    metadata: Dict[str, Any],
    program_map: str,
    instruction: str = "",
    program_name: str = ""
) -> str:
    """
    Build a generic full context prompt for sections without specific builders.

    Args:
        source_code: Complete COBOL source code
        metadata: Dictionary with all metadata sources
        program_map: Formatted program map
        instruction: Section-specific instruction
        program_name: Name of the COBOL program

    Returns:
        Generic formatted prompt
    """
    prompt_parts = []

    prompt_parts.append(f"""# Full Context Documentation Generation

Program: {program_name or 'UNKNOWN'}

## Instructions
{instruction or 'Generate documentation for this COBOL program section.'}
""")

    if program_map:
        prompt_parts.append(f"""
---
## PROGRAM MAP

{program_map}
""")

    if source_code:
        prompt_parts.append(f"""
---
## SOURCE CODE

```cobol
{source_code}
```
""")

    return '\n'.join(prompt_parts)


def _format_metadata_summary(metadata: Dict[str, Any]) -> str:
    """
    Format metadata into a concise summary for prompts.

    Args:
        metadata: Dictionary with metadata sources

    Returns:
        Formatted metadata summary string
    """
    summary_parts = []

    # CTags summary
    ctags = metadata.get('ctags_outline', {})
    if ctags:
        symbols = ctags.get('symbols', [])
        paragraphs = [s for s in symbols if s.get('kind') in ['paragraph', 'section']]
        data_items = [s for s in symbols if s.get('kind') == 'data']
        summary_parts.append(f"- CTags: {len(paragraphs)} paragraphs, {len(data_items)} data items")

    # CFG summary
    cfg = metadata.get('superbol_cfg', {})
    if cfg:
        nodes = cfg.get('nodes', [])
        edges = cfg.get('edges', [])
        summary_parts.append(f"- Control Flow: {len(nodes)} nodes, {len(edges)} edges")

    # GnuCOBOL summary
    gnucobol = metadata.get('gnucobol_analysis', {})
    if gnucobol:
        loc = gnucobol.get('lines_of_code', gnucobol.get('total_lines', 'N/A'))
        summary_parts.append(f"- GnuCOBOL: {loc} lines of code")

    if summary_parts:
        return '\n'.join(summary_parts)

    return ""
