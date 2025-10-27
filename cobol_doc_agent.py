"""
COBOL Documentation Agent using LangGraph
BMAD-METHOD Inspired: Template-driven, metadata-based documentation generation

This agent ensures consistent documentation across COBOL projects by:
1. Loading metadata from SuperBol, GnuCOBOL, and ctags
2. Processing YAML template to understand structure
3. Using LLM to intelligently fill templates with metadata
4. Generating consistent Markdown documentation
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, TypedDict

import yaml
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph

# Import Anthropic support
try:
    from langchain_anthropic import ChatAnthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("⚠ Warning: langchain-anthropic not installed. Run: pip install langchain-anthropic")

# Import Source Extraction (Phase 1)
try:
    from source_integration import extract_source_for_section
    from section_requirements import should_extract_source
    SOURCE_EXTRACTION_AVAILABLE = True
except ImportError:
    SOURCE_EXTRACTION_AVAILABLE = False
    print("⚠ Warning: Source extraction modules not found. Run without source extraction.")

# ============================================================================
# STATE DEFINITION
# ============================================================================

class AgentState(TypedDict):
    """
    State maintained throughout the documentation generation process.
    This is the single source of truth passed between all nodes.
    """
    # Input
    program_name: str
    workspace_path: Path  # Path to COBOL source files
    metadata_dir: Path  # Path where the generated metadata will be stored
    template_path: Path  # Path to YAML template file
    output_dir: Path  # Path for writing final generated code-explanation docs using the
                      # generated metadata files

    # Checksum Management (for intelligent metadata regeneration)
    source_checksum_path: Path  # Path to source file checksums YAML
    metadata_checksum_path: Path  # Path to metadata file checksums YAML

    # Metadata Generation Control
    generate_metadata: bool  # Whether to generate metadata via MCP
    skip_existing_metadata: bool  # Skip metadata generation if files exist (deprecated - use checksums)
    cobol_files: List[str]  # List of COBOL files for batch metadata generation
    metadata_generation_reason: Optional[str]  # Reason for generating/skipping metadata
    servers_config: Dict[str, Any]  # MCP servers configuration from YAML config
    llm_config: Dict[str, Any]  # LLM configuration (provider, model, api_key, temperature)

    # Loaded Data
    template: Dict[str, Any]
    superbol_symbols: Dict[str, Any]
    superbol_cfg: Dict[str, Any]
    gnucobol_analysis: Dict[str, Any]
    ctags_outline: Dict[str, Any]

    # Two-Pass Generation Mode
    use_two_pass_mode: bool  # Whether to use two-pass generation (default: False)
    current_pass: Optional[int]  # Current pass number (1, 2, or 3) in two-pass mode
    passes: Optional[List[List[Dict[str, Any]]]]  # List of passes, each containing sections
    current_pass_index: int  # Current pass being processed in two-pass mode

    # Source Code Extraction (Phase 1 Integration)
    enable_source_extraction: bool  # Whether to extract source code for sections (default: False)
    compress_source: bool  # Whether to compress source (remove comments/blanks) (default: True)
    cobol_file_path: Optional[str]  # Path to COBOL source file for extraction

    # Processing State
    current_section: str
    section_ids: List[str]  # List of section IDs to process
    current_section_index: int  # Current section being processed
    generated_content: Dict[str, str]

    # Output
    final_document: str
    errors: List[str]


# ============================================================================
# LLM PROVIDER FACTORY
# ============================================================================

def create_llm(llm_config: Dict[str, Any]):
    """
    Create LLM instance based on configuration

    Args:
        llm_config: LLM configuration dict with keys:
            - provider: 'openai' or 'anthropic'
            - model: model name
            - api_key: API key (optional if set in env)
            - temperature: temperature value (optional, default 0.1)

    Returns:
        LLM instance (ChatOpenAI or ChatAnthropic)

    Raises:
        ValueError: If provider is not supported or required package not installed
    """
    provider = llm_config.get('provider', 'openai').lower()
    model = llm_config.get('model', 'gpt-4o')
    temperature = llm_config.get('temperature', 0.1)
    api_key = llm_config.get('api_key')

    if provider == 'openai':
        kwargs = {
            'model': model,
            'temperature': temperature
        }
        if api_key:
            kwargs['api_key'] = api_key

        return ChatOpenAI(**kwargs)

    elif provider == 'anthropic':
        if not ANTHROPIC_AVAILABLE:
            raise ValueError(
                "Anthropic provider requested but langchain-anthropic not installed. "
                "Run: pip install langchain-anthropic"
            )

        kwargs = {
            'model': model,
            'temperature': temperature
        }
        if api_key:
            kwargs['anthropic_api_key'] = api_key

        return ChatAnthropic(**kwargs)

    else:
        raise ValueError(
            f"Unsupported LLM provider: {provider}. "
            f"Supported providers: openai, anthropic"
        )


# ============================================================================
# METADATA GENERATION (MCP)
# ============================================================================

def generate_metadata_node(state: AgentState) -> AgentState:
    """
    Node 0: Generate metadata using MCP servers (optional, conditional)

    This node:
    1. Generates metadata via MCP servers
    2. Calculates and saves metadata checksums for future validation

    Checksums ensure metadata integrity and detect corruption/incompleteness.
    """
    from mcp_metadata_generator import generate_metadata_sync
    from checksum_manager import save_metadata_checksums

    print(f"\n{'='*70}")
    print("Metadata Generation via MCP Servers")
    print(f"{'='*70}")

    try:
        workspace_path = str(state["workspace_path"])
        metadata_dir = str(state["metadata_dir"])
        cobol_files = state.get("cobol_files", [])
        servers_config = state.get("servers_config", {})

        # If no cobol_files provided, auto-discover
        if not cobol_files:
            from checksum_manager import get_source_files
            workspace = Path(workspace_path)
            # Auto-discover all COBOL files (.COB, .cob, .cbl, .CBL, .COBOL, .cobol, .c74, .C74)
            discovered_files = get_source_files(workspace)
            cobol_files = sorted([f.name for f in discovered_files])
            print(f"Auto-discovered {len(cobol_files)} COBOL files")

        # Generate metadata for all COBOL files
        generate_metadata_sync(workspace_path, metadata_dir, cobol_files, servers_config)

        print(f"\n✓ Metadata generation complete")

        # Save metadata checksums for future validation
        metadata_checksum_path = state.get("metadata_checksum_path", Path("./metadata-checksum.yaml"))
        print(f"\n{'='*70}")
        print("Saving Metadata Checksums")
        print(f"{'='*70}")

        save_metadata_checksums(
            metadata_dir=Path(metadata_dir),
            metadata_checksum_path=metadata_checksum_path
        )

        print(f"✓ Metadata checksums saved for integrity verification")

    except Exception as e:
        error_msg = f"Error generating metadata: {str(e)}"
        print(f"✗ {error_msg}")
        state["errors"].append(error_msg)

    return state


def check_metadata_exists(state: AgentState) -> bool:
    """
    Check if metadata files already exist for the program

    Returns True if all required metadata files exist
    """
    program_name = state["program_name"]
    metadata_dir = Path(state["metadata_dir"])

    # TODO: Devise a mechanism to check the Names of the existing metadata files
    # TODO: cross-check if all the metadata is captured?

    # Core required files (always needed)
    required_files = [
        metadata_dir / "superbol" / f"superbol-{program_name}-doc-symbols.json",
        metadata_dir / "superbol" / "superbol-cfg" / f"{program_name}.json",
        metadata_dir / "ctags" / f"ctags-{program_name}-outline.json"
    ]

    # GnuCOBOL analysis: check for either batch file (multi-file) or single file
    gnucobol_batch = metadata_dir / "gnucobol" / "gnucobol-batch-analyze-all.json"
    gnucobol_single = metadata_dir / "gnucobol" / f"gnucobol-{program_name}-analysis.json"

    # At least one GnuCOBOL file must exist
    has_gnucobol = gnucobol_batch.exists() or gnucobol_single.exists()

    return all(f.exists() for f in required_files) and has_gnucobol


def should_generate_metadata(state: AgentState) -> str:
    """
    Routing function: Determine if metadata generation is needed

    Uses checksum-based validation to intelligently decide:
    - Compare source file checksums
    - Compare metadata file checksums
    - Detect corruption, changes, or missing files

    Returns:
        "generate_via_checksum" - Generate metadata via MCP (checksums indicate need)
        "skip_checksums_valid" - Skip generation, load existing metadata (checksums valid)
    """
    from checksum_manager import should_regenerate_metadata

    # Check if metadata generation is enabled in config
    if not state.get("generate_metadata", False):
        print("\nℹ Metadata generation disabled in config, loading existing metadata")
        return "skip_checksums_valid"

    # Get paths from state
    workspace_path = Path(state["workspace_path"])
    metadata_dir = Path(state["metadata_dir"])
    cobol_files = state.get("cobol_files", [])

    # Get checksum file paths from state (set by config loader)
    source_checksum_path = state.get("source_checksum_path", Path("./source-checksum.yaml"))
    metadata_checksum_path = state.get("metadata_checksum_path", Path("./metadata-checksum.yaml"))

    # Use checksum manager to determine if regeneration is needed
    # Pass specific files from config to avoid auto-discovery of all workspace files
    should_regenerate, reason = should_regenerate_metadata(
        workspace_path=workspace_path,
        source_checksum_path=source_checksum_path,
        metadata_dir=metadata_dir,
        metadata_checksum_path=metadata_checksum_path,
        cobol_files=cobol_files if cobol_files else None
    )

    if should_regenerate:
        print(f"\nℹ Metadata generation required: {reason}")
        # Store reason in state for logging
        state["metadata_generation_reason"] = reason
        return "generate_via_checksum"
    else:
        print(f"\nℹ Metadata generation skipped: {reason}")
        return "skip_checksums_valid"


# ============================================================================
# METADATA LOADERS
# ============================================================================

def load_metadata_node(state: AgentState) -> AgentState:
    """
    Node 1: Load all metadata files for the specified program.

    Loads:
    - SuperBol document symbols
    - SuperBol CFG (control flow graph)
    - GnuCOBOL batch analysis
    - Universal-ctags outline
    """
    program_name = state["program_name"]
    metadata_dir = Path(state["metadata_dir"])

    print(f"Loading metadata for program: {program_name}")

    try:
        # Load SuperBol Symbols
        superbol_symbols_path = metadata_dir / "superbol" / f"superbol-{program_name}-doc-symbols.json"
        with open(superbol_symbols_path, 'r') as f:
            state["superbol_symbols"] = json.load(f)

        # Load SuperBol CFG
        superbol_cfg_path = metadata_dir / "superbol" / "superbol-cfg" / f"{program_name}.json"
        with open(superbol_cfg_path, 'r') as f:
            state["superbol_cfg"] = json.load(f)

        # Load GnuCOBOL Analysis
        # In single-file mode, batch-analyze-all.json may not exist
        gnucobol_batch_path = metadata_dir / "gnucobol" / "gnucobol-batch-analyze-all.json"
        gnucobol_single_path = metadata_dir / "gnucobol" / f"gnucobol-{program_name}-analysis.json"

        if gnucobol_batch_path.exists():
            # Multi-file mode: load from batch analysis
            with open(gnucobol_batch_path, 'r') as f:
                gnucobol_data = json.load(f)
                # Extract this program's analysis
                state["gnucobol_analysis"] = {
                    "program_calls": gnucobol_data["result"]["program_calls"].get(program_name, []),
                    "per_file": gnucobol_data["result"]["per_file_analysis"],
                    "call_summary": gnucobol_data["result"]["call_summary"]
                }
        elif gnucobol_single_path.exists():
            # Single-file mode: load from individual file analysis
            with open(gnucobol_single_path, 'r') as f:
                state["gnucobol_analysis"] = json.load(f)
        else:
            print(f"⚠ Warning: No GnuCOBOL analysis found for {program_name}")
            state["gnucobol_analysis"] = {}

        # Load ctags Outline
        ctags_path = metadata_dir / "ctags" / f"ctags-{program_name}-outline.json"
        with open(ctags_path, 'r') as f:
            state["ctags_outline"] = json.load(f)

        print(f"✓ Successfully loaded all metadata for {program_name}")

    except Exception as e:
        error_msg = f"Error loading metadata: {str(e)}"
        print(f"✗ {error_msg}")
        state["errors"].append(error_msg)

    return state


def load_template_node(state: AgentState) -> AgentState:
    """
    Node 2: Load and parse the YAML documentation template.
    """
    template_path = Path(state["template_path"])

    print(f"Loading template from: {template_path}")

    try:
        with open(template_path, 'r') as f:
            state["template"] = yaml.safe_load(f)

        print(f"✓ Template loaded successfully")

    except Exception as e:
        error_msg = f"Error loading template: {str(e)}"
        print(f"✗ {error_msg}")
        state["errors"].append(error_msg)

    return state


# ============================================================================
# TEMPLATE PROCESSING NODES
# ============================================================================

def extract_template_structure_node(state: AgentState) -> AgentState:
    """
    Node 3: Analyze template structure and plan section generation.

    If two-pass mode is enabled, groups sections into passes.
    Otherwise, processes sections sequentially (single-pass mode).
    """
    template = state["template"]
    sections = template.get("sections", [])
    use_two_pass = state.get("use_two_pass_mode", False)

    print(f"Template has {len(sections)} main sections to process")

    # Initialize generated content dictionary
    state["generated_content"] = {}

    if use_two_pass:
        # Two-pass mode: Group sections into passes
        passes = group_sections_into_passes(sections)
        print(f"✓ Two-pass mode enabled: {len(passes)} passes created")
        for i, pass_sections in enumerate(passes, 1):
            section_titles = [s.get("title", s["id"]) for s in pass_sections]
            print(f"  Pass {i}: {len(pass_sections)} sections - {', '.join(section_titles)}")

        # Store passes and initialize pass tracking
        state["passes"] = passes
        state["current_pass_index"] = 0
        state["current_pass"] = 1
        state["section_ids"] = [s["id"] for s in sections]  # For tracking
        state["current_section_index"] = 0

    else:
        # Single-pass mode: Process sections sequentially
        print("Single-pass mode: Processing sections sequentially with aggressive filtering")
        state["section_ids"] = [s["id"] for s in sections]
        state["current_section_index"] = 0

    return state


def process_section_node(state: AgentState) -> AgentState:
    """
    Node 4: Process section(s).

    Two modes:
    - Two-pass mode: Process all sections in current pass together
    - Single-pass mode: Process one section at a time

    This is the core LLM-driven node that:
    1. Reads section instruction and template
    2. Extracts relevant metadata
    3. Uses LLM to generate content following template structure
    4. Validates output matches expected format
    5. Recursively processes nested subsections
    """
    use_two_pass = state.get("use_two_pass_mode", False)

    if use_two_pass:
        # Two-pass mode: Process all sections in current pass
        passes = state.get("passes", [])
        current_pass_index = state.get("current_pass_index", 0)

        if current_pass_index >= len(passes):
            return state

        pass_sections = passes[current_pass_index]
        current_pass_num = current_pass_index + 1

        print(f"\n{'='*60}")
        print(f"PASS {current_pass_num}: Processing {len(pass_sections)} sections")
        print(f"{'='*60}")

        # Set current pass number for filtering
        state["current_pass"] = current_pass_num

        # Process all sections in this pass
        for section in pass_sections:
            print(f"\n[Pass {current_pass_num}] Processing: {section.get('title', section['id'])}")
            content = process_section_recursive(state, section)
            state["generated_content"][section["id"]] = content

        # Move to next pass
        state["current_pass_index"] = current_pass_index + 1

    else:
        # Single-pass mode: Process one section at a time
        template = state["template"]
        sections = template.get("sections", [])
        current_index = state.get("current_section_index", 0)

        if current_index >= len(sections):
            return state

        section = sections[current_index]

        # Process this section (and its nested subsections recursively)
        content = process_section_recursive(state, section)

        # Store generated content
        state["generated_content"][section["id"]] = content
        state["current_section_index"] = current_index + 1

    return state


def process_section_recursive(state: AgentState, section: Dict[str, Any]) -> str:
    """
    Recursively process a section and all its nested subsections.

    Returns the complete content for this section including all subsections.
    """
    section_id = section["id"]
    section_title = section.get("title", "")
    instruction = section.get("instruction", "")
    section_template = section.get("template", "")
    subsections = section.get("sections", [])

    print(f"\nProcessing section: {section_id} - {section_title}")

    # Build context for LLM
    context = build_section_context(state, section)

    # If this section has nested subsections, process them
    if subsections:
        # Process parent section with instruction about subsections
        parent_content = generate_section_with_subsections(
            section_id=section_id,
            section_title=section_title,
            instruction=instruction,
            context=context,
            subsections=subsections,
            state=state
        )
        return parent_content
    else:
        # Leaf section - generate content directly
        content = generate_section_content(
            section_id=section_id,
            section_title=section_title,
            instruction=instruction,
            template=section_template,
            context=context,
            section_config=section,
            llm_config=state.get("llm_config")
        )
        return content


def generate_section_with_subsections(
    section_id: str,
    section_title: str,
    instruction: str,
    context: Dict[str, Any],
    subsections: List[Dict[str, Any]],
    state: AgentState
) -> str:
    """
    Generate a section that contains nested subsections.
    Processes each subsection recursively and combines them.
    """
    parts = []

    # Add main section header
    parts.append(f"## {section_title}")
    parts.append("")

    # Add instruction/context if provided
    if instruction:
        # Generate brief intro based on instruction
        intro = f"*{instruction.split('.')[0]}.*"
        parts.append(intro)
        parts.append("")

    # Process each subsection recursively
    for subsection in subsections:
        subsection_content = process_section_recursive(state, subsection)
        parts.append(subsection_content)
        parts.append("")  # Blank line between subsections

    return "\n".join(parts)


def group_sections_into_passes(sections: List[Dict[str, Any]]) -> List[List[Dict[str, Any]]]:
    """
    Group template sections into logical passes for two-pass generation.

    Pass 1 (Overview & Structure): Sections needing symbol structure, divisions, summary
    Pass 2 (Logic & Flow): Sections needing CFG, paragraphs, program calls
    Pass 3 (Technical Details): Sections needing metrics and dependencies

    Args:
        sections: List of section configurations from template

    Returns:
        List of passes, where each pass is a list of sections to generate together
    """
    pass1_keywords = ["metadata-info", "overview", "summary", "structure", "program-structure", "appendix"]
    pass2_keywords = ["control", "flow", "logic", "business", "data-flow", "communication", "inter-program", "execution"]
    pass3_keywords = ["error", "technical", "detail", "metric", "dependency"]

    pass1_sections = []
    pass2_sections = []
    pass3_sections = []

    def classify_section(section):
        section_id = section.get("id", "").lower()
        section_title = section.get("title", "").lower()

        # Check which pass this section belongs to
        for kw in pass1_keywords:
            if kw in section_id or kw in section_title:
                return 1
        for kw in pass2_keywords:
            if kw in section_id or kw in section_title:
                return 2
        for kw in pass3_keywords:
            if kw in section_id or kw in section_title:
                return 3
        # Default to pass 2 (most common)
        return 2

    for section in sections:
        pass_num = classify_section(section)
        if pass_num == 1:
            pass1_sections.append(section)
        elif pass_num == 2:
            pass2_sections.append(section)
        else:
            pass3_sections.append(section)

    # Return non-empty passes
    passes = []
    if pass1_sections:
        passes.append(pass1_sections)
    if pass2_sections:
        passes.append(pass2_sections)
    if pass3_sections:
        passes.append(pass3_sections)

    return passes


def filter_metadata_for_pass(pass_number: int, full_metadata: Dict[str, Any]) -> Dict[str, Any]:
    """
    Conservative pass-based filtering for two-pass generation.

    Pass 1: Full symbols + division structure + summary (for overview/structure sections)
    Pass 2: Full CFG + full paragraphs + program calls (for logic/flow sections)
    Pass 3: Targeted metrics + dependencies (for technical sections)

    Args:
        pass_number: Which pass (1, 2, or 3)
        full_metadata: Complete metadata from all sources

    Returns:
        Conservatively filtered metadata appropriate for this pass
    """
    superbol_symbols = full_metadata.get("superbol_symbols", {})
    superbol_cfg = full_metadata.get("superbol_cfg", {})
    gnucobol = full_metadata.get("gnucobol_analysis", {})
    ctags = full_metadata.get("ctags_outline", {})

    # Helper to limit arrays (conservative limits)
    def limit_array(arr, max_size):
        return arr[:max_size] if isinstance(arr, list) else arr

    filtered = {
        "program_name": full_metadata["program_name"],
        "timestamp": full_metadata["timestamp"]
    }

    if pass_number == 1:
        # Pass 1: Overview & Structure - Need full symbol tree, division structure
        filtered["superbol_symbols"] = superbol_symbols  # FULL symbols

        # CFG: Summary stats + CRITICAL external calls and copybooks for executive summary
        if isinstance(superbol_cfg, dict):
            filtered["superbol_cfg"] = {
                "summary": {
                    "total_nodes": len(superbol_cfg.get("nodes", [])),
                    "total_edges": len(superbol_cfg.get("edges", [])),
                    "entry_points": len([n for n in superbol_cfg.get("nodes", []) if n.get("type") == "entry"])
                },
                "calls": superbol_cfg.get("calls", []),  # MUST have for Executive Summary
                "copybooks": superbol_cfg.get("copybooks", [])  # MUST have for Program Structure
            }
        else:
            filtered["superbol_cfg"] = superbol_cfg

        # GnuCOBOL: Summary + program calls
        filtered["gnucobol_analysis"] = {
            "summary": gnucobol.get("summary", {}),
            "program_calls": gnucobol.get("program_calls", []),
            "call_summary": gnucobol.get("call_summary", {})
        }

        # Ctags: Full structure
        filtered["ctags_outline"] = ctags  # FULL outline

    elif pass_number == 2:
        # Pass 2: Logic & Flow - Need full CFG, paragraphs, program calls
        # SuperBOL: Full procedure division, limited data division
        filtered["superbol_symbols"] = {
            "program_id": superbol_symbols.get("program_id"),
            "children": limit_array(superbol_symbols.get("children", []), 100),  # First 100 children for context
            "procedure_division": superbol_symbols.get("procedure_division"),
            "paragraphs": superbol_symbols.get("paragraphs"),  # FULL paragraphs
            "sections": superbol_symbols.get("sections")  # FULL sections
        }

        # CFG: FULL but with conservative limits to stay under 1M
        if isinstance(superbol_cfg, dict):
            nodes = superbol_cfg.get("nodes", [])
            edges = superbol_cfg.get("edges", [])

            # Conservative limits: 500 nodes, 1000 edges (vs aggressive 100/200)
            # CRITICAL: Preserve calls[] and copybooks[] arrays for external dependencies
            filtered["superbol_cfg"] = {
                "nodes": limit_array(nodes, 500),
                "edges": limit_array(edges, 1000),
                "calls": superbol_cfg.get("calls", []),  # MUST preserve external calls
                "copybooks": superbol_cfg.get("copybooks", []),  # MUST preserve copybooks
                "performs": limit_array(superbol_cfg.get("performs", []), 1000),
                "total_nodes": len(nodes),
                "total_edges": len(edges)
            }
        else:
            filtered["superbol_cfg"] = superbol_cfg

        # GnuCOBOL: Full program calls + procedure structure
        paragraphs = gnucobol.get("paragraphs", [])
        filtered["gnucobol_analysis"] = {
            "summary": gnucobol.get("summary", {}),
            "program_calls": gnucobol.get("program_calls", []),  # FULL program calls
            "call_summary": gnucobol.get("call_summary", {}),
            "paragraphs": limit_array(paragraphs, 100),  # First 100 paragraphs
            "sections": limit_array(gnucobol.get("sections", []), 50),
            "performs": limit_array(gnucobol.get("performs", []), 200)
        }

        # Ctags: Full paragraph structure
        paragraphs = ctags.get("paragraphs", [])
        filtered["ctags_outline"] = {
            "program_name": ctags.get("program_name"),
            "divisions": ctags.get("divisions", []),
            "paragraphs": limit_array(paragraphs, 100),  # First 100 paragraphs
            "total_paragraphs": len(paragraphs),
            "sections": limit_array(ctags.get("sections", []), 50),
            "performs": limit_array(ctags.get("performs", []), 200),
            "data_items": limit_array(ctags.get("data_items", []), 50)  # Some data for reference
        }

    else:  # pass_number == 3
        # Pass 3: Technical Details - Need metrics, dependencies, error handling
        # SuperBOL: Limited symbols for metrics
        filtered["superbol_symbols"] = {
            "program_id": superbol_symbols.get("program_id"),
            "children": limit_array(superbol_symbols.get("children", []), 50),
            "paragraph_count": len(superbol_symbols.get("paragraphs", [])),
            "section_count": len(superbol_symbols.get("sections", [])),
            "data_item_count": len(superbol_symbols.get("children", []))
        }

        # CFG: Summary stats for metrics
        if isinstance(superbol_cfg, dict):
            filtered["superbol_cfg"] = {
                "node_count": len(superbol_cfg.get("nodes", [])),
                "edge_count": len(superbol_cfg.get("edges", [])),
                "entry_points": len([n for n in superbol_cfg.get("nodes", []) if n.get("type") == "entry"]),
                "complexity": len(superbol_cfg.get("edges", [])) - len(superbol_cfg.get("nodes", [])) + 2
            }
        else:
            filtered["superbol_cfg"] = {"note": "CFG data available"}

        # GnuCOBOL: Metrics + dependencies
        filtered["gnucobol_analysis"] = {
            "summary": gnucobol.get("summary", {}),
            "program_calls": gnucobol.get("program_calls", []),
            "copybooks": gnucobol.get("copybooks", []),
            "complexity_metrics": gnucobol.get("complexity_metrics", {})
        }

        # Ctags: Counts + samples
        filtered["ctags_outline"] = {
            "program_name": ctags.get("program_name"),
            "divisions": ctags.get("divisions", []),
            "total_paragraphs": len(ctags.get("paragraphs", [])),
            "total_sections": len(ctags.get("sections", [])),
            "total_data_items": len(ctags.get("data_items", [])),
            "total_performs": len(ctags.get("performs", [])),
            "sample_paragraphs": limit_array(ctags.get("paragraphs", []), 20),
            "sample_data_items": limit_array(ctags.get("data_items", []), 20)
        }

    return filtered


def filter_metadata_for_section_enhanced(section: Dict[str, Any], full_metadata: Dict[str, Any]) -> Dict[str, Any]:
    """
    Aggressive token-optimized filtering for very large COBOL files.

    For files generating 1.5M+ tokens, we need aggressive reduction while preserving quality.

    Key Strategy:
    1. Hard limits on ALL array sizes (nodes, edges, paragraphs, data items)
    2. Strict separation: Data sections get ONLY data, Logic sections get ONLY procedure
    3. Remove redundant metadata across sources
    4. Target: Reduce each section to <300k tokens

    Args:
        section: Section configuration from template
        full_metadata: Complete metadata from all sources

    Returns:
        Aggressively filtered but essential metadata for this section
    """
    section_id = section.get("id", "").lower()
    section_title = section.get("title", "").lower()

    # Detect section categories
    is_overview = any(kw in section_id or kw in section_title
                     for kw in ["overview", "summary", "introduction", "purpose", "metadata-info"])
    is_data = any(kw in section_id or kw in section_title
                 for kw in ["data", "structure", "variable", "copybook", "record", "transformation"])
    is_logic = any(kw in section_id or kw in section_title
                  for kw in ["logic", "procedure", "algorithm", "process", "flow", "operation", "business", "execution"])
    is_performance = any(kw in section_id or kw in section_title
                        for kw in ["performance", "optimization", "cfg", "control", "complexity"])
    is_error = any(kw in section_id or kw in section_title
                  for kw in ["error", "exception", "validation", "handling"])
    is_metrics = any(kw in section_id or kw in section_title
                    for kw in ["metric", "technical", "detail", "code", "dependency", "appendix"])
    is_communication = any(kw in section_id or kw in section_title
                          for kw in ["communication", "call", "program", "inter-program", "hierarchy"])

    # Start with base context (always included)
    filtered = {
        "program_name": full_metadata["program_name"],
        "timestamp": full_metadata["timestamp"]
    }

    # Get metadata sources
    superbol_symbols = full_metadata.get("superbol_symbols", {})
    superbol_cfg = full_metadata.get("superbol_cfg", {})
    gnucobol = full_metadata.get("gnucobol_analysis", {})
    ctags = full_metadata.get("ctags_outline", {})

    # Helper function to limit array size
    def limit_array(arr, max_size):
        return arr[:max_size] if isinstance(arr, list) else arr

    # === SuperBOL Symbols Filtering (AGGRESSIVE) ===
    if is_data:
        # Data sections: ONLY data division, NO procedure division
        filtered["superbol_symbols"] = {
            "program_id": superbol_symbols.get("program_id"),
            "data_division": superbol_symbols.get("data_division"),
            "working_storage": superbol_symbols.get("working_storage"),
            "file_section": superbol_symbols.get("file_section")
        }
    elif is_logic or is_communication or is_error:
        # Logic sections: ONLY procedure division, NO data division
        filtered["superbol_symbols"] = {
            "program_id": superbol_symbols.get("program_id"),
            "procedure_division": superbol_symbols.get("procedure_division"),
            "paragraphs": limit_array(superbol_symbols.get("paragraphs", []), 30),
            "sections": limit_array(superbol_symbols.get("sections", []), 20)
        }
    elif is_metrics:
        # Metrics: Limited data from both divisions
        filtered["superbol_symbols"] = {
            "program_id": superbol_symbols.get("program_id"),
            "children": limit_array(superbol_symbols.get("children", []), 30),
            "paragraph_count": len(superbol_symbols.get("paragraphs", [])),
            "data_item_count": len(superbol_symbols.get("children", []))
        }
    elif is_overview:
        # Overview: Bare minimum - program ID + division names only
        filtered["superbol_symbols"] = {
            "program_id": superbol_symbols.get("program_id"),
            "divisions": [d.get("name") for d in limit_array(superbol_symbols.get("children", []), 5)],
            "total_elements": len(superbol_symbols.get("children", []))
        }
    else:
        # Default: Minimal structure
        filtered["superbol_symbols"] = {
            "program_id": superbol_symbols.get("program_id")
        }

    # === SuperBOL CFG Filtering (HARD LIMITS) ===
    if is_performance or is_logic or is_communication:
        # Performance/Logic: Limited CFG (max 100 nodes, 200 edges)
        if isinstance(superbol_cfg, dict):
            # CRITICAL: Always preserve calls[] and copybooks[] for external dependencies
            filtered["superbol_cfg"] = {
                "nodes": limit_array(superbol_cfg.get("nodes", []), 100),
                "edges": limit_array(superbol_cfg.get("edges", []), 200),
                "calls": superbol_cfg.get("calls", []),  # MUST preserve external calls
                "copybooks": superbol_cfg.get("copybooks", []),  # MUST preserve copybooks
                "performs": limit_array(superbol_cfg.get("performs", []), 200),
                "total_nodes": len(superbol_cfg.get("nodes", [])),
                "total_edges": len(superbol_cfg.get("edges", []))
            }
        else:
            filtered["superbol_cfg"] = superbol_cfg
    elif is_metrics:
        # Metrics: CFG summary stats only
        if isinstance(superbol_cfg, dict):
            # CRITICAL: Preserve calls[] and copybooks[] for dependency metrics
            filtered["superbol_cfg"] = {
                "node_count": len(superbol_cfg.get("nodes", [])),
                "edge_count": len(superbol_cfg.get("edges", [])),
                "entry_points": len([n for n in superbol_cfg.get("nodes", []) if n.get("type") == "entry"]),
                "calls": superbol_cfg.get("calls", []),  # For external dependency metrics
                "copybooks": superbol_cfg.get("copybooks", [])  # For copybook metrics
            }
        else:
            filtered["superbol_cfg"] = {"note": "CFG data available"}
    else:
        # All other sections: Skip CFG entirely
        filtered["superbol_cfg"] = {
            "note": f"CFG omitted (use Control Flow section). {len(superbol_cfg.get('nodes', []))} nodes available."
            if isinstance(superbol_cfg, dict) else "CFG available in Control Flow section"
        }

    # === GnuCOBOL Analysis Filtering (TARGETED) ===
    if is_communication or is_metrics:
        # Communication/Metrics: Focus on program calls + summary
        filtered["gnucobol_analysis"] = {
            "summary": gnucobol.get("summary", {}),
            "program_calls": gnucobol.get("program_calls", []),
            "call_summary": gnucobol.get("call_summary", {})
        }
    elif is_data:
        # Data sections: Only data-related info, limit arrays
        data_items = gnucobol.get("data_items", [])
        filtered["gnucobol_analysis"] = {
            "data_items": limit_array(data_items, 50),
            "total_data_items": len(data_items),
            "copybooks": gnucobol.get("copybooks", []),
            "file_definitions": gnucobol.get("file_definitions", [])
        }
    elif is_logic or is_error:
        # Logic/Error: Only procedure-related info
        paragraphs = gnucobol.get("paragraphs", [])
        filtered["gnucobol_analysis"] = {
            "paragraphs": limit_array(paragraphs, 40),
            "total_paragraphs": len(paragraphs),
            "sections": limit_array(gnucobol.get("sections", []), 20),
            "performs": limit_array(gnucobol.get("performs", []), 100)
        }
    elif is_performance:
        # Performance: Summary + complexity metrics only
        filtered["gnucobol_analysis"] = {
            "summary": gnucobol.get("summary", {}),
            "complexity_metrics": gnucobol.get("complexity_metrics", {})
        }
    else:
        # Overview and others: Minimal summary
        filtered["gnucobol_analysis"] = {
            "summary": gnucobol.get("summary", {})
        }

    # === Ctags Outline Filtering (HARD LIMITS) ===
    if is_data:
        # Data sections: Only data items + divisions
        data_items = ctags.get("data_items", [])
        filtered["ctags_outline"] = {
            "program_name": ctags.get("program_name"),
            "divisions": ctags.get("divisions", []),
            "data_items": limit_array(data_items, 50),
            "total_data_items": len(data_items),
            "records": limit_array(ctags.get("records", []), 30)
        }
    elif is_logic or is_error or is_communication:
        # Logic/Error/Communication: Only paragraphs + sections
        paragraphs = ctags.get("paragraphs", [])
        filtered["ctags_outline"] = {
            "program_name": ctags.get("program_name"),
            "divisions": ctags.get("divisions", []),
            "paragraphs": limit_array(paragraphs, 40),
            "total_paragraphs": len(paragraphs),
            "sections": limit_array(ctags.get("sections", []), 25),
            "performs": limit_array(ctags.get("performs", []), 80)
        }
    elif is_metrics:
        # Metrics: Counts only, minimal examples
        filtered["ctags_outline"] = {
            "program_name": ctags.get("program_name"),
            "divisions": ctags.get("divisions", []),
            "total_paragraphs": len(ctags.get("paragraphs", [])),
            "total_sections": len(ctags.get("sections", [])),
            "total_data_items": len(ctags.get("data_items", [])),
            "total_performs": len(ctags.get("performs", [])),
            "sample_paragraphs": limit_array(ctags.get("paragraphs", []), 10)
        }
    elif is_overview:
        # Overview: Structure summary only
        filtered["ctags_outline"] = {
            "program_name": ctags.get("program_name"),
            "divisions": ctags.get("divisions", []),
            "paragraph_count": len(ctags.get("paragraphs", [])),
            "section_count": len(ctags.get("sections", [])),
            "data_item_count": len(ctags.get("data_items", []))
        }
    else:
        # Default: Minimal structure
        filtered["ctags_outline"] = {
            "program_name": ctags.get("program_name"),
            "divisions": ctags.get("divisions", [])
        }

    return filtered


def build_section_context(state: AgentState, section: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract relevant metadata for the current section.

    Two modes:
    - Two-pass mode: Uses pass-based conservative filtering (preserves quality)
    - Single-pass mode: Uses aggressive section-based filtering (saves tokens)

    Phase 1 Integration: Also extracts source code if enabled
    """
    # Build full metadata
    full_metadata = {
        "program_name": state["program_name"],
        "timestamp": datetime.now().isoformat(),
        "superbol_symbols": state["superbol_symbols"],
        "superbol_cfg": state["superbol_cfg"],
        "gnucobol_analysis": state["gnucobol_analysis"],
        "ctags_outline": state["ctags_outline"]
    }

    # Check which mode we're in
    if state.get("use_two_pass_mode", False):
        # Two-pass mode: Use pass-based filtering
        current_pass = state.get("current_pass", 1)
        filtered_context = filter_metadata_for_pass(current_pass, full_metadata)
        print(f"  → Using two-pass mode (Pass {current_pass})")
    else:
        # Single-pass mode: Use aggressive section-based filtering
        filtered_context = filter_metadata_for_section_enhanced(section, full_metadata)
        print(f"  → Using single-pass mode (aggressive filtering)")

    # Phase 1: Source Code Extraction Integration
    if state.get("enable_source_extraction", False) and SOURCE_EXTRACTION_AVAILABLE:
        section_id = section.get("id", "")
        cobol_file_path = state.get("cobol_file_path")

        if cobol_file_path and should_extract_source(section_id):
            compress = state.get("compress_source", True)
            print(f"  → Extracting source code (compress={compress})")

            try:
                source_code = extract_source_for_section(
                    section_id,
                    cobol_file_path,
                    paragraph_metadata=None,  # Could be enhanced to use ctags paragraphs
                    compress=compress
                )

                if source_code:
                    filtered_context["source_code"] = source_code
                    print(f"  → Source code extracted successfully")
                else:
                    print(f"  → No source code extracted for this section")
            except Exception as e:
                print(f"  ⚠ Warning: Source extraction failed: {e}")
                # Continue without source code - graceful degradation
    elif state.get("enable_source_extraction", False) and not SOURCE_EXTRACTION_AVAILABLE:
        print(f"  ⚠ Warning: Source extraction enabled but modules not available")

    return filtered_context


def generate_section_content(
    section_id: str,
    section_title: str,
    instruction: str,
    template: str,
    context: Dict[str, Any],
    section_config: Dict[str, Any],
    llm_config: Optional[Dict[str, Any]] = None
) -> str:
    """
    Use LLM to generate section content based on template and metadata.

    This is where the "magic" happens - the LLM interprets:
    1. The instruction (what to do)
    2. The template (how to format output)
    3. The metadata (source of information)

    And generates consistent, well-formatted documentation.

    Args:
        llm_config: LLM configuration dict (provider, model, api_key, temperature)
    """

    # Initialize LLM from configuration
    if llm_config:
        llm = create_llm(llm_config)
    else:
        # Fallback to OpenAI gpt-4o if no config
        llm = ChatOpenAI(model="gpt-4o", temperature=0.1)

    # Build system prompt
    system_prompt = f"""You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "{section_title}" (ID: {section_id})

CRITICAL REQUIREMENTS FOR CONSISTENCY:
1. Follow the template structure EXACTLY
2. Use ONLY information from the provided metadata - do not invent or assume
3. If metadata is missing, explicitly state "Information not available in metadata"
4. Use consistent formatting across all generated documents
5. Reference line numbers when available
6. For placeholders like {{{{program_name}}}}, replace with actual values
7. Generate valid Markdown syntax
8. For Mermaid diagrams, ensure valid syntax

TEMPLATE STRUCTURE TO FOLLOW:
{template if template else "Generate appropriate structure based on instruction"}

INSTRUCTION:
{instruction}

OUTPUT FORMAT:
- Return ONLY the Markdown content for this section
- Include the section title as an H3 (###) for subsections
- Follow all formatting specified in the template
- Ensure Mermaid diagrams are wrapped in ```mermaid blocks
- For subsections, use H3 (###) headers
"""

    # Build user prompt with metadata
    metadata_str = json.dumps(context, indent=2)
    user_prompt = f"""Generate documentation for this section using the following metadata:

{metadata_str}

Remember:
- Program name: {context.get('program_name', 'UNKNOWN')}
- Follow template structure exactly
- Be consistent in terminology and formatting
- Reference line numbers from metadata
- Generate valid Markdown and Mermaid syntax
"""

    # Call LLM
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]

    response = llm.invoke(messages)
    content = response.content

    print(f"  ✓ Generated {len(content)} characters for {section_id}")

    return content


def check_completion_node(state: AgentState) -> str:
    """
    Node 5: Check if all sections/passes are processed.
    Returns "continue" or "assemble" to route workflow.
    """
    use_two_pass = state.get("use_two_pass_mode", False)

    if use_two_pass:
        # Two-pass mode: Check if all passes are complete
        passes = state.get("passes", [])
        current_pass_index = state.get("current_pass_index", 0)

        print(f"Check completion: Pass {current_pass_index}/{len(passes)} completed")

        if current_pass_index < len(passes):
            return "continue"
        else:
            print(f"✓ All {len(passes)} passes completed!")
            return "assemble"
    else:
        # Single-pass mode: Check if all sections are processed
        total_sections = len(state.get("section_ids", []))
        current_index = state.get("current_section_index", 0)

        print(f"Check completion: {current_index}/{total_sections} sections processed")

        if current_index < total_sections:
            return "continue"
        else:
            return "assemble"


def assemble_document_node(state: AgentState) -> AgentState:
    """
    Node 6: Assemble all generated sections into final document.
    """
    print("\nAssembling final document...")

    template = state["template"]
    program_name = state["program_name"]
    generated_content = state["generated_content"]

    # Build document header
    template_info = template.get("template", {})
    output_info = template_info.get("output", {})
    doc_title = output_info.get("title", "{{program_name}} Documentation").replace("{{program_name}}", program_name)

    document_parts = [
        f"# {doc_title}",
        "",
        f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*",
        "",
        "---",
        ""
    ]

    # Add each section in order
    sections = template.get("sections", [])
    for section in sections:
        section_id = section["id"]
        if section_id in generated_content:
            document_parts.append(generated_content[section_id])
            document_parts.append("")  # Blank line between sections

    # Assemble
    state["final_document"] = "\n".join(document_parts)

    print(f"✓ Document assembled: {len(state['final_document'])} characters")

    return state


def save_document_node(state: AgentState) -> AgentState:
    """
    Node 7: Save the final document to file.
    """
    output_dir = Path(state["output_dir"])
    program_name = state["program_name"]

    # Create output directory if needed
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate output filename
    output_filename = f"{program_name}-documentation.md"
    output_path = output_dir / output_filename

    # Save document
    with open(output_path, 'w') as f:
        f.write(state["final_document"])

    print(f"\n✓ Documentation saved to: {output_path}")

    return state


# ============================================================================
# GRAPH CONSTRUCTION
# ============================================================================

def create_documentation_agent() -> StateGraph:
    """
    Build the LangGraph workflow for documentation generation.

    Workflow:
    0. (Conditional) Generate metadata via MCP servers
    1. Load metadata
    2. Load template
    3. Extract template structure
    4. Process sections (loop)
    5. Assemble document
    6. Save document
    """

    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("generate_metadata", generate_metadata_node)
    workflow.add_node("load_metadata", load_metadata_node)
    workflow.add_node("load_template", load_template_node)
    workflow.add_node("extract_structure", extract_template_structure_node)
    workflow.add_node("process_section", process_section_node)
    workflow.add_node("assemble_document", assemble_document_node)
    workflow.add_node("save_document", save_document_node)

    # Define edges
    # Start with conditional: checksum-based routing to decide if metadata generation is needed
    workflow.add_conditional_edges(
        START,
        should_generate_metadata,  # Uses SHA256 checksums to intelligently decide
        {
            "generate_via_checksum": "generate_metadata",  # Checksums indicate generation needed
            "skip_checksums_valid": "load_metadata"  # Checksums valid: skip metadata generation
        }
    )

    # After metadata generation, load it
    workflow.add_edge("generate_metadata", "load_metadata")

    # Continue with normal workflow
    workflow.add_edge("load_metadata", "load_template")
    workflow.add_edge("load_template", "extract_structure")
    workflow.add_edge("extract_structure", "process_section")

    # Conditional edge: loop through sections or move to assembly
    workflow.add_conditional_edges(
        "process_section",
        check_completion_node,
        {
            "continue": "process_section",  # Loop back
            "assemble": "assemble_document"  # Move forward
        }
    )

    workflow.add_edge("assemble_document", "save_document")
    workflow.add_edge("save_document", END)

    return workflow.compile()


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def generate_documentation(
    program_name: str,
    workspace_path: str = "..",
    metadata_dir: str = "../output",
    template_path: str = "./cobol-doc-template.yaml",
    output_dir: str = "../docs",
    generate_metadata: bool = False,
    skip_existing_metadata: bool = True,
    cobol_files: Optional[List[str]] = None,
    source_checksum_path: str = "./source-checksum.yaml",
    metadata_checksum_path: str = "./metadata-checksum.yaml",
    servers_config: Optional[Dict[str, Any]] = None,
    llm_config: Optional[Dict[str, Any]] = None,
    use_two_pass_mode: bool = True,  # NEW: Enable two-pass generation by default
    enable_source_extraction: bool = False,  # Phase 1: Enable source code extraction
    compress_source: bool = True,  # Phase 1: Compress extracted source (remove comments/blanks)
    cobol_file_path: Optional[str] = None  # Phase 1: Path to COBOL source file
) -> str:
    """
    Main entry point for documentation generation.

    Args:
        program_name: Name of COBOL program (e.g., "MAINPROG")
        workspace_path: Path to directory containing COBOL source files
        metadata_dir: Directory containing/for metadata files
        template_path: Path to documentation template YAML
        output_dir: Directory to save generated documentation
        generate_metadata: Whether to generate metadata via MCP servers
        skip_existing_metadata: Skip metadata generation if files exist (deprecated)
        cobol_files: List of COBOL files for metadata generation (auto-discovered if None)
        source_checksum_path: Path to source file checksums YAML
        metadata_checksum_path: Path to metadata file checksums YAML
        servers_config: Optional MCP servers configuration from YAML config
        llm_config: Optional LLM configuration (provider, model, api_key, temperature)
        use_two_pass_mode: Enable two-pass generation (conservative filtering, better quality)
        enable_source_extraction: Enable Phase 1 source code extraction (default: False)
        compress_source: Compress extracted source by removing comments/blanks (default: True)
        cobol_file_path: Path to COBOL source file for extraction (auto-determined if None)

    Returns:
        Path to generated documentation file
    """

    print(f"\n{'='*70}")
    print(f"COBOL Documentation Generator")
    print(f"Program: {program_name}")
    if generate_metadata:
        print(f"Mode: Checksum-based intelligent metadata generation")
    else:
        print(f"Mode: Documentation only (using existing metadata)")
    if use_two_pass_mode:
        print(f"Strategy: Two-pass generation (conservative filtering)")
    else:
        print(f"Strategy: Single-pass generation (aggressive filtering)")
    if enable_source_extraction:
        print(f"Phase 1: Source extraction ENABLED (compress={compress_source})")
    print(f"{'='*70}\n")

    # Auto-determine COBOL file path if not provided
    if enable_source_extraction and not cobol_file_path:
        # Try to find the COBOL file in workspace
        from pathlib import Path as PathLib
        workspace = PathLib(workspace_path)
        # Look for .cbl, .cob, .c74 files with matching name
        for ext in ['.cbl', '.cob', '.c74', '.CBL', '.COB']:
            candidate = workspace / f"{program_name}{ext}"
            if candidate.exists():
                cobol_file_path = str(candidate)
                print(f"  → Auto-detected COBOL file: {cobol_file_path}")
                break

    # Initialize state
    initial_state = AgentState(
        program_name=program_name,
        workspace_path=Path(workspace_path),
        metadata_dir=Path(metadata_dir),
        template_path=Path(template_path),
        output_dir=Path(output_dir),
        source_checksum_path=Path(source_checksum_path),
        metadata_checksum_path=Path(metadata_checksum_path),
        generate_metadata=generate_metadata,
        skip_existing_metadata=skip_existing_metadata,
        cobol_files=cobol_files or [],
        metadata_generation_reason=None,
        servers_config=servers_config or {},
        llm_config=llm_config or {},
        template={},
        superbol_symbols={},
        superbol_cfg={},
        gnucobol_analysis={},
        ctags_outline={},
        use_two_pass_mode=use_two_pass_mode,  # NEW: Two-pass mode flag
        current_pass=None,  # NEW: Current pass number
        passes=None,  # NEW: Passes list (populated during template structure extraction)
        current_pass_index=0,  # NEW: Current pass index
        enable_source_extraction=enable_source_extraction,  # Phase 1: Source extraction flag
        compress_source=compress_source,  # Phase 1: Compression flag
        cobol_file_path=cobol_file_path,  # Phase 1: Path to COBOL source
        current_section="",
        section_ids=[],  # Initialize section IDs list
        current_section_index=0,  # Initialize index
        generated_content={},
        final_document="",
        errors=[]
    )

    # Create and run agent
    agent = create_documentation_agent()
    final_state = agent.invoke(initial_state)

    # Check for errors
    if final_state.get("errors"):
        print("\n⚠ Errors occurred during generation:")
        for error in final_state["errors"]:
            print(f"  - {error}")

    output_path = Path(output_dir) / f"{program_name}-documentation.md"
    return str(output_path)


if __name__ == "__main__":
    import argparse
    import sys

    # Command-line interface with argument parsing
    parser = argparse.ArgumentParser(
        description="COBOL Documentation Generator with checksum-based intelligent metadata generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Using YAML configuration (RECOMMENDED)
  python cobol_doc_agent.py --config config.minimal.yaml

  # Single program mode - using existing metadata
  python cobol_doc_agent.py MAINPROG

  # Single program mode - generate metadata AND documentation
  python cobol_doc_agent.py MAINPROG --generate-metadata --workspace ../cobol-source

  # Batch mode - process all COBOL files in a directory
  python cobol_doc_agent.py --source-files ../cobol-source --generate-metadata

  # Batch mode with custom output paths
  python cobol_doc_agent.py --source-files ../cobol-source --generate-metadata \\
      --output-dir ./metadata --docs-path ./documentation

  # Override config file settings with CLI arguments
  python cobol_doc_agent.py --config config.minimal.yaml --generate-metadata
        """
    )

    # Config file argument (highest priority)
    parser.add_argument("--config", help="Path to YAML configuration file (recommended)")

    # Traditional CLI arguments (backward compatibility)
    parser.add_argument("program_name", nargs='?', help="Name of COBOL program (e.g., MAINPROG) - optional if --config or --source-files is provided")
    parser.add_argument("--source-files", help="Path to COBOL source file or directory containing multiple files for batch processing")
    parser.add_argument("--workspace", help="Path to COBOL source files directory")
    parser.add_argument("--output-dir", help="Output directory for metadata storage")
    parser.add_argument("--docs-path", help="Output path for generated documentation markdown files")
    parser.add_argument("--template", help="Documentation template YAML file")
    parser.add_argument("--generate-metadata", action="store_true", help="Generate metadata via MCP servers before documentation")
    parser.add_argument("--no-skip-existing", action="store_true", help="Force regenerate metadata even if it exists")

    args = parser.parse_args()

    # Load configuration from YAML if --config is provided
    config_loader = None
    if args.config:
        from config_loader import load_config

        print(f"{'='*70}")
        print(f"Loading configuration from: {args.config}")
        print(f"{'='*70}\n")

        try:
            config_loader = load_config(args.config)

            # Display loaded configuration
            source_config = config_loader.get_source_config()
            output_config = config_loader.get_output_config()
            metadata_config = config_loader.get_metadata_config()
            checksum_config = config_loader.get_checksum_config()
            llm_config = config_loader.get_llm_config()

            print("✓ Configuration loaded successfully\n")
            print(f"  Source mode: {source_config.get('mode', 'single')}")
            print(f"  Source path: {source_config.get('source_files', 'N/A')}")
            print(f"  Program name: {source_config.get('program_name', 'N/A')}")
            print(f"  Metadata dir: {output_config.get('metadata_dir', 'N/A')}")
            print(f"  Docs path: {output_config.get('docs_path', 'N/A')}")
            print(f"  Generate metadata: {metadata_config.get('generate', False)}")
            print(f"  LLM: {llm_config.get('provider', 'N/A')} / {llm_config.get('model', 'N/A')}")

            # Display source extraction config
            source_extraction_config = config_loader.get_source_extraction_config()
            if source_extraction_config:
                print(f"  Source extraction: {source_extraction_config.get('enabled', False)}")
                print(f"  Compress source: {source_extraction_config.get('compress', True)}")

            print()

        except Exception as e:
            print(f"✗ Error loading configuration: {e}")
            sys.exit(1)

    # Determine configuration source (config file vs CLI args)
    if config_loader:
        # Use config file values, but CLI args can override
        source_config = config_loader.get_source_config()
        output_config = config_loader.get_output_config()
        checksum_config = config_loader.get_checksum_config()
        metadata_config = config_loader.get_metadata_config()
        template_config = config_loader.get_template_config()

        # Extract values from config
        mode = source_config.get('mode', 'single')
        config_program_name = source_config.get('program_name')
        config_source_files = source_config.get('source_files')

        # For both single and batch mode, use source_files to determine workspace
        # In single mode: source_files is a file path, workspace is parent dir
        # In batch mode: source_files is a directory path, workspace is that dir
        if config_source_files:
            source_path = Path(config_source_files)
            if mode == 'single' and source_path.is_file():
                config_workspace = str(source_path.parent)
            else:
                config_workspace = config_source_files
        else:
            config_workspace = '..'

        config_metadata_dir = output_config.get('metadata_dir', '../output')
        config_docs_path = output_config.get('docs_path', '../docs')
        config_template = template_config.get('path', './cobol-doc-template.yaml')
        config_generate_metadata = metadata_config.get('generate', True)
        config_skip_existing = metadata_config.get('skip_existing', True)

        # CLI arguments override config file
        program_name = args.program_name or config_program_name
        # Pass source_files for both single and batch modes (will be parsed later)
        source_files_arg = args.source_files or config_source_files
        workspace = args.workspace or config_workspace
        metadata_dir = args.output_dir or config_metadata_dir
        docs_path = args.docs_path or config_docs_path
        template_path = args.template or config_template
        generate_metadata = args.generate_metadata or config_generate_metadata
        skip_existing = (not args.no_skip_existing) and config_skip_existing
        source_checksum_path = checksum_config.get('source_checksum_file_path', './source-checksum.yaml')
        metadata_checksum_path = checksum_config.get('metadata_checksum_file_path', './metadata-checksum.yaml')
        servers_config = config_loader.get_servers_config()
        llm_config = config_loader.get_llm_config()

        # Phase 1: Source extraction configuration
        source_extraction_config = config_loader.get_source_extraction_config()
        enable_source_extraction = source_extraction_config.get('enabled', False)
        compress_source = source_extraction_config.get('compress', True)
        # cobol_file_path will be auto-detected based on source_files_arg

    else:
        # Use CLI arguments only (backward compatibility)
        program_name = args.program_name
        source_files_arg = args.source_files
        workspace = args.workspace or ".."
        metadata_dir = args.output_dir or "../output"
        docs_path = args.docs_path or "../docs"
        template_path = args.template or "./cobol-doc-template.yaml"
        generate_metadata = args.generate_metadata
        skip_existing = not args.no_skip_existing
        source_checksum_path = "./source-checksum.yaml"
        metadata_checksum_path = "./metadata-checksum.yaml"
        servers_config = {}
        llm_config = {}  # Default to OpenAI gpt-4o

        # Phase 1: Source extraction defaults (disabled by default)
        enable_source_extraction = False
        compress_source = True

    # Validation: either program_name or source_files must be provided
    if not program_name and not source_files_arg:
        parser.error("Either program_name, --source-files, or --config must be provided")

    # Determine which mode to use
    if source_files_arg:
        # Batch processing mode
        source_path = Path(source_files_arg)

        # Determine list of COBOL files to process
        if source_path.is_file():
            # Single file - store both stem (for program_name) and full name (for cobol_files)
            cobol_files_to_process = [(source_path.stem, source_path.name)]
            workspace_path = str(source_path.parent)
            print(f"\nProcessing single file: {source_path.name}")
        elif source_path.is_dir():
            # Directory - find all COBOL files recursively
            from checksum_manager import get_source_files
            cobol_file_paths = get_source_files(source_path)
            # Store tuples of (stem, full_name)
            cobol_files_to_process = sorted([(f.stem, f.name) for f in cobol_file_paths])
            workspace_path = str(source_path)
            print(f"\nProcessing directory: {source_path}")
            print(f"Found {len(cobol_files_to_process)} COBOL files")
        else:
            parser.error(f"Source path does not exist: {source_files_arg}")

        if not cobol_files_to_process:
            parser.error(f"No COBOL files found in: {source_files_arg}")

        # Batch process all files
        print(f"\n{'='*70}")
        print(f"BATCH MODE: Processing {len(cobol_files_to_process)} COBOL programs")
        print(f"{'='*70}\n")

        successful = []
        failed = []

        for idx, (prog_name, full_filename) in enumerate(cobol_files_to_process, 1):
            print(f"\n{'#'*70}")
            print(f"# Processing {idx}/{len(cobol_files_to_process)}: {prog_name}")
            print(f"{'#'*70}")

            try:
                # Build list of all filenames for metadata generation (only on first iteration)
                if idx == 1 and generate_metadata:
                    # Pass all files to metadata generation to process them together
                    all_cobol_files = [name for _, name in cobol_files_to_process]
                else:
                    # For documentation-only, pass just this file
                    all_cobol_files = [full_filename]

                output_path = generate_documentation(
                    program_name=prog_name,
                    workspace_path=workspace_path,
                    metadata_dir=metadata_dir,
                    template_path=template_path,
                    output_dir=docs_path,
                    generate_metadata=generate_metadata and idx == 1,  # Only generate metadata once (first file)
                    skip_existing_metadata=skip_existing,
                    cobol_files=all_cobol_files,  # Pass specific files to avoid auto-discovery
                    source_checksum_path=source_checksum_path,
                    metadata_checksum_path=metadata_checksum_path,
                    servers_config=servers_config,
                    llm_config=llm_config,
                    enable_source_extraction=enable_source_extraction,
                    compress_source=compress_source,
                    cobol_file_path=full_filename  # Use the actual file being processed
                )
                successful.append((prog_name, output_path))
                print(f"✓ Successfully generated documentation for {prog_name}")
            except Exception as e:
                failed.append((prog_name, str(e)))
                print(f"✗ Failed to generate documentation for {prog_name}: {e}")

        # Summary
        print(f"\n{'='*70}")
        print(f"BATCH PROCESSING COMPLETE")
        print(f"{'='*70}")
        print(f"Successful: {len(successful)}/{len(cobol_files_to_process)}")
        print(f"Failed: {len(failed)}/{len(cobol_files_to_process)}")

        if successful:
            print(f"\n✓ Successfully generated documentation for:")
            for prog_name, out_path in successful:
                print(f"  - {prog_name}: {out_path}")

        if failed:
            print(f"\n✗ Failed to generate documentation for:")
            for prog_name, error in failed:
                print(f"  - {prog_name}: {error}")

        print(f"\n{'='*70}\n")

    else:
        # Single program mode (original behavior)
        output_path = generate_documentation(
            program_name=program_name,
            workspace_path=workspace,
            metadata_dir=metadata_dir,
            template_path=template_path,
            output_dir=docs_path,
            generate_metadata=generate_metadata,
            skip_existing_metadata=skip_existing,
            source_checksum_path=source_checksum_path,
            metadata_checksum_path=metadata_checksum_path,
            servers_config=servers_config,
            llm_config=llm_config,
            enable_source_extraction=enable_source_extraction,
            compress_source=compress_source,
            cobol_file_path=None  # Will be auto-detected
        )

        print(f"\n{'='*70}")
        print(f"Documentation generation complete!")
        print(f"Output: {output_path}")
        print(f"{'='*70}\n")
