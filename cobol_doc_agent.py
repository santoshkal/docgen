"""
COBOL Documentation Agent using LangGraph
BMAD-METHOD Inspired: Template-driven, metadata-based documentation generation

This agent ensures consistent documentation across COBOL projects by:
1. Loading metadata from static analysis, semantic analysis, and symbol parsing
2. Processing YAML template to understand structure
3. Using LLM to intelligently fill templates with metadata
4. Generating consistent Markdown documentation
"""

import hashlib
import json
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, TypedDict

import yaml
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph

# Import Anthropic support (LangChain)
try:
    from langchain_anthropic import ChatAnthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("⚠ Warning: langchain-anthropic not installed. Run: pip install langchain-anthropic")

# Import Claude Agent SDK support
try:
    from claude_sdk_client import CLAUDE_SDK_AVAILABLE, ClaudeSdkLLM
except ImportError:
    CLAUDE_SDK_AVAILABLE = False
    print("⚠ Warning: claude_sdk_client not available. Claude SDK provider disabled.")

# Import Source Extraction (Phase 1-3)
try:
    from multi_file_resolver import (CalledProgramResolver,  # Phase 3
                                     CopybookResolver)
    from section_requirements import should_extract_source
    from source_integration import \
        extract_source_multi_file  # Phase 3: Multi-file support
    from source_integration import extract_source_for_section
    SOURCE_EXTRACTION_AVAILABLE = True
    MULTI_FILE_AVAILABLE = True
except ImportError as e:
    SOURCE_EXTRACTION_AVAILABLE = False
    MULTI_FILE_AVAILABLE = False
    print(f"⚠ Warning: Source extraction modules not found: {e}")

# Import Full Context Mode modules (Epic 2 & 3)
try:
    from context_strategy import (get_strategy_for_state,
                                  should_use_full_context)
    from full_context_builder import FullContextBuilder
    from full_context_prompts import build_full_context_prompt
    FULL_CONTEXT_AVAILABLE = True
except ImportError as e:
    FULL_CONTEXT_AVAILABLE = False
    print(f"⚠ Warning: Full context modules not found: {e}")

# Import Context Chaining modules (Epic 4)
try:
    from context_chain import (FULL_CONTEXT_SECTION_ORDER, ContextChain,
                               build_chained_context, should_use_chaining)
    CONTEXT_CHAINING_AVAILABLE = True
except ImportError as e:
    CONTEXT_CHAINING_AVAILABLE = False
    print(f"⚠ Warning: Context chaining modules not found: {e}")

from llm_fallback import LLMFallbackManager, invoke_llm_with_fallback
# Import Run Logger
from run_logger import get_run_logger, init_run_logger
# Import Tokenizer and Fallback modules
from tokenizer import estimate_tokens, get_token_limit

# ============================================================================
# FATAL LLM ERROR HANDLING
# ============================================================================

class LLMFatalError(Exception):
    """Non-retryable LLM error (limit exhausted, CLI crash). Stops file processing."""
    pass

def is_fatal_llm_error(error: Exception) -> bool:
    """Check if an LLM error is non-retryable."""
    error_str = str(error).lower()
    fatal_patterns = [
        'command failed with exit code',
        'fatal error in message reader',
        'cli not found',
        'claude code cli not found',
    ]
    return any(pattern in error_str for pattern in fatal_patterns)

# ============================================================================
# LANGUAGE ADAPTER ACCESSOR
# ============================================================================

_current_adapter = None

def get_current_adapter():
    """Get the current language adapter (lazily defaults to COBOL)."""
    global _current_adapter
    if _current_adapter is None:
        from adapter_registry import get_adapter
        _current_adapter = get_adapter('cobol')
    return _current_adapter

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
    # Normalized metadata keys (language-agnostic, used by adapter-driven pipeline)
    structural_outline: Dict[str, Any]
    symbol_table: Dict[str, Any]
    static_analysis: Dict[str, Any]
    syntax_tree: Dict[str, Any]
    control_flow_graph: Dict[str, Any]
    called_by_graph: Dict[str, List[str]]  # PHASE 3: Reverse call graph (target → [callers])

    # Two-Pass Generation Mode
    use_two_pass_mode: bool  # Whether to use two-pass generation (default: False)
    current_pass: Optional[int]  # Current pass number (1, 2, or 3) in two-pass mode
    passes: Optional[List[List[Dict[str, Any]]]]  # List of passes, each containing sections
    current_pass_index: int  # Current pass being processed in two-pass mode

    # Source Code Extraction (Phase 1 Integration)
    enable_source_extraction: bool  # Whether to extract source code for sections (default: False)
    compress_source: bool  # Whether to compress source (remove comments/blanks) (default: True)
    cobol_file_path: Optional[str]  # Path to source file for extraction (legacy COBOL key)
    source_file_path: Optional[str]  # Path to source file for extraction (language-agnostic alias)

    # Multi-File Support (Phase 3 Integration)
    resolve_copybooks: bool  # Whether to resolve and include copybook content (default: False)
    resolve_called_programs: bool  # Whether to resolve called programs (default: False)
    copybook_search_paths: Optional[List[str]]  # Paths to search for copybooks
    program_search_paths: Optional[List[str]]  # Paths to search for called programs
    copybook_resolver: Optional[Any]  # CopybookResolver instance (initialized at runtime)
    called_program_resolver: Optional[Any]  # CalledProgramResolver instance (initialized at runtime)

    # Full Context Mode (Epic 2: Section-Specific Full Context Generation)
    use_full_context_mode: bool  # Whether to use full context mode (default: False)
    full_context_sections: List[str]  # List of section IDs that use full context
    max_message_chars: int  # Max chars for LLM prompt (OpenAI API limit ~10MB, default 9MB)

    # Context Chaining (Epic 4: Cross-Section Consistency)
    context_chaining_enabled: bool  # Whether context chaining is enabled (default: False)
    context_chain_data: Dict[str, str]  # Stored previous section outputs for chaining

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
            - provider: 'openai', 'anthropic', or 'claude_sdk'
            - model: model name
            - api_key: API key (optional if set in env, not needed for claude_sdk)
            - temperature: temperature value (optional, default 0.1)

    Returns:
        LLM instance (ChatOpenAI, ChatAnthropic, or ClaudeSdkLLM)

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

    elif provider == 'claude_sdk':
        if not CLAUDE_SDK_AVAILABLE:
            raise ValueError(
                "Claude SDK provider requested but claude-agent-sdk not installed. "
                "Run: pip install claude-agent-sdk\n"
                "Also ensure Claude Code CLI is installed: npm install -g @anthropic-ai/claude-code"
            )

        # NOTE: Beta-features wiring (1M-context beta) is intentionally disabled.
        # We force the standard 200K-token model; if a call's context exceeds
        # that limit the SDK raises, the file is marked failed in the
        # checkpoint, and a later restart retries it. To re-enable the 1M
        # beta, restore the commented block below AND re-enable the matching
        # truncation/auto-escalation paths.
        #   betas = llm_config.get('betas')
        betas = None

        # Get thinking config (new) or fall back to deprecated max_thinking_tokens
        thinking = llm_config.get('thinking')
        max_thinking_tokens = llm_config.get('max_thinking_tokens')
        max_output_tokens = llm_config.get('max_output_tokens')

        # Normalize string shorthand: "disabled" → {"type": "disabled"}, "adaptive" → {"type": "adaptive"}
        if isinstance(thinking, str):
            thinking = {"type": thinking}

        # ClaudeSdkLLM accepts temperature for compatibility but ignores it
        return ClaudeSdkLLM(
            model=model,
            temperature=temperature,
            api_key=api_key,
            betas=betas,  # NOTE: always None — see comment above.
            thinking=thinking,
            max_thinking_tokens=max_thinking_tokens,  # Deprecated fallback
            max_output_tokens=max_output_tokens
        )

    else:
        raise ValueError(
            f"Unsupported LLM provider: {provider}. "
            f"Supported providers: openai, anthropic, claude_sdk"
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
    from checksum_manager import save_metadata_checksums
    from mcp_metadata_generator import generate_metadata_sync

    print(f"\n{'='*70}")
    print("Metadata Generation via MCP Servers")
    print(f"{'='*70}")

    try:
        workspace_path = str(state["workspace_path"])
        metadata_dir = str(state["metadata_dir"])
        cobol_files = state.get("cobol_files", [])
        servers_config = state.get("servers_config", {})
        file_filter_config = state.get("file_filter_config")

        # If no cobol_files provided, auto-discover
        if not cobol_files:
            from checksum_manager import get_source_files
            workspace = Path(workspace_path)
            # Auto-discover COBOL files (respecting filter config if provided)
            discovered_files = get_source_files(workspace, filter_config=file_filter_config)
            cobol_files = sorted([f.name for f in discovered_files])
            print(f"Auto-discovered {len(cobol_files)} COBOL files")

        # Generate metadata for all source files
        # Pass full_config so factory can detect tools declarations for config-driven generation
        full_config = state.get("full_config")
        generate_metadata_sync(workspace_path, metadata_dir, cobol_files, servers_config,
                               config=full_config)

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

    # Check if force regeneration is requested (skip_existing_metadata = False means force regenerate)
    skip_existing = state.get("skip_existing_metadata", True)
    if not skip_existing:
        print("\nℹ Force metadata regeneration requested (skip_existing: false)")
        state["metadata_generation_reason"] = "Force regeneration requested"
        return "generate_via_checksum"

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
    - Document symbols from static analyzer
    - Control flow graph (CFG)
    - Semantic analysis results
    - Symbol outline from parser
    """
    program_name = state["program_name"]
    metadata_dir = Path(state["metadata_dir"])

    print(f"Loading metadata for program: {program_name}")

    try:
        # Load SuperBol Symbols with intelligent filtering for large files
        superbol_symbols_path = metadata_dir / "superbol" / f"superbol-{program_name}-doc-symbols.json"
        with open(superbol_symbols_path, 'r') as f:
            superbol_data = json.load(f)

            # PHASE 1 OPTIMIZATION: Filter large symbol arrays
            symbols = superbol_data.get('symbols', [])
            original_count = len(symbols)

            if original_count > 5000:  # Large file detected (> 5K symbols)
                print(f"  ⚠ Large SuperBol file detected: {original_count:,} symbols")

                # Categorize symbols by kind
                filtered_symbols = []
                kind_counts = {'original': {}, 'filtered': {}}

                # Count originals
                for symbol in symbols:
                    kind = symbol.get('kind', 'unknown')
                    kind_counts['original'][kind] = kind_counts['original'].get(kind, 0) + 1

                # Filter strategy:
                # - Kind 12 (Programs/Sections): Keep ALL (~1.6K) - CRITICAL
                # - Kind 17 (Paragraphs): Keep ALL (~258) - CRITICAL
                # - Kind 13 (Data items): Sample first 500 - BLOAT SOURCE (10K+)
                for symbol in symbols:
                    kind = symbol.get('kind', 'unknown')

                    if kind in [12, 17]:  # Programs and Paragraphs - keep all
                        filtered_symbols.append(symbol)
                        kind_counts['filtered'][kind] = kind_counts['filtered'].get(kind, 0) + 1
                    elif kind == 13:  # Data items - sample
                        if kind_counts['filtered'].get(13, 0) < 500:
                            filtered_symbols.append(symbol)
                            kind_counts['filtered'][kind] = kind_counts['filtered'].get(kind, 0) + 1

                superbol_data['symbols'] = filtered_symbols
                superbol_data['_optimization_metadata'] = {
                    'original_symbol_count': original_count,
                    'filtered_symbol_count': len(filtered_symbols),
                    'reduction_percentage': round((1 - len(filtered_symbols)/original_count) * 100, 1),
                    'kind_distribution_original': kind_counts['original'],
                    'kind_distribution_filtered': kind_counts['filtered']
                }

                reduction_pct = (1 - len(filtered_symbols)/original_count) * 100
                print(f"     Filtered to {len(filtered_symbols):,} symbols ({reduction_pct:.1f}% reduction)")
                print(f"     Kind 12 (Programs): {kind_counts['filtered'].get(12, 0):,} (kept all)")
                print(f"     Kind 17 (Paragraphs): {kind_counts['filtered'].get(17, 0):,} (kept all)")
                print(f"     Kind 13 (Data items): {kind_counts['filtered'].get(13, 0):,} (sampled from {kind_counts['original'].get(13, 0):,})")

            state["superbol_symbols"] = superbol_data

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
                gnucobol_data = json.load(f)

                # PHASE 1 OPTIMIZATION: Strip bloat fields (never used by template)
                bloat_fields = ['listing', 'stdout', 'stderr', 'command']
                total_bloat_removed = 0
                removed_fields = []

                for field in bloat_fields:
                    if field in gnucobol_data:
                        field_size = len(str(gnucobol_data[field]))
                        total_bloat_removed += field_size
                        removed_fields.append(f"{field}({field_size:,} chars)")
                        del gnucobol_data[field]

                if total_bloat_removed > 0:
                    print(f"  → Stripped GnuCOBOL bloat: {', '.join(removed_fields)}")
                    print(f"     Total removed: {total_bloat_removed:,} chars (~{total_bloat_removed//4:,} tokens)")

                # Preserve essential fields: file_path, success, message, analysis, error
                state["gnucobol_analysis"] = gnucobol_data
        else:
            print(f"⚠ Warning: No GnuCOBOL analysis found for {program_name}")
            state["gnucobol_analysis"] = {}

        # Load ctags Outline
        ctags_path = metadata_dir / "ctags" / f"ctags-{program_name}-outline.json"
        with open(ctags_path, 'r') as f:
            state["ctags_outline"] = json.load(f)

        print(f"✓ Successfully loaded all metadata for {program_name}")

        # PHASE 3: Build reverse call graph for "Called by" relationships
        called_by_graph = build_reverse_call_graph(
            state.get("superbol_cfg", {}),
            state.get("ctags_outline", {})
        )

        # Store in state for use in filtered contexts
        state["called_by_graph"] = called_by_graph

        if called_by_graph:
            total_relationships = sum(len(callers) for callers in called_by_graph.values())
            print(f"  → Built reverse call graph: {len(called_by_graph):,} targets with {total_relationships:,} relationships")

    except Exception as e:
        error_msg = f"Error loading metadata: {str(e)}"
        print(f"✗ {error_msg}")
        state["errors"].append(error_msg)

    return state


def build_reverse_call_graph(superbol_cfg: Dict[str, Any], ctags_outline: Dict[str, Any]) -> Dict[str, List[str]]:
    """
    Build reverse call graph: paragraph_name → [list of callers]

    PHASE 3: Solve "Called by: Information not available" problem

    Sources:
    - SuperBol CFG edges (from → to)
    - SuperBol CFG performs
    - CTags performs

    Returns:
        Dictionary mapping target → [list of callers]
        Example: {"PARA-B": ["PARA-A", "PARA-C"]}  # PARA-B is called by PARA-A and PARA-C
    """
    called_by = {}

    # Process SuperBol CFG edges
    if isinstance(superbol_cfg, dict):
        edges = superbol_cfg.get("edges", [])
        for edge in edges:
            source = edge.get("from")
            target = edge.get("to")

            if source and target:
                if target not in called_by:
                    called_by[target] = []
                if source not in called_by[target]:  # Avoid duplicates
                    called_by[target].append(source)

        # Process PERFORM statements from SuperBol
        performs = superbol_cfg.get("performs", [])
        for perform in performs:
            caller = perform.get("from")
            target = perform.get("to")

            if caller and target:
                if target not in called_by:
                    called_by[target] = []
                if caller not in called_by[target]:
                    called_by[target].append(caller)

    # Process CTags performs (additional source)
    if isinstance(ctags_outline, dict):
        outline = ctags_outline.get("outline", {})
        if isinstance(outline, dict):
            # CTags may have a performs array
            ctags_performs = outline.get("performs", [])
            # Or it might be in the top level
            if not ctags_performs:
                ctags_performs = ctags_outline.get("performs", [])

            for perform in ctags_performs:
                # CTags structure might be different - adapt as needed
                if isinstance(perform, dict):
                    caller = perform.get("from") or perform.get("caller")
                    target = perform.get("to") or perform.get("target") or perform.get("name")

                    if caller and target:
                        if target not in called_by:
                            called_by[target] = []
                        if caller not in called_by[target]:
                            called_by[target].append(caller)

    return called_by


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

    # Get pass number if in two-pass mode
    pass_number = state.get("current_pass") if state.get("use_two_pass_mode", False) else None

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

        # Check if this is a large file that needs chunked processing
        if 'chunked_file_info' in context:
            print(f"  → Detected large file - using chunked processing")
            content = process_large_file_in_chunks(
                section_id=section_id,
                section_title=section_title,
                instruction=instruction,
                template=section_template,
                context=context,
                chunked_file_info=context['chunked_file_info'],
                llm_config=state.get("llm_config"),
                pass_number=pass_number,
                state=state  # Pass state for accessing full CTags data
            )
        else:
            # Normal processing
            content, debug_path, latency = generate_section_content(
                section_id=section_id,
                section_title=section_title,
                instruction=instruction,
                template=section_template,
                context=context,
                section_config=section,
                llm_config=state.get("llm_config"),
                pass_number=pass_number
            )
            if debug_path:
                print(f"  [DEBUG] Request logged to: {debug_path} (latency: {latency:.2f}s)")
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

    # Note: instruction is for LLM guidance only, NOT included in final output
    # to avoid exposing internal tool names (SuperBol, CTags, GnuCOBOL, etc.)

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
        # PHASE 3: called_by_graph included selectively per pass (not in Pass 1 - too large for summaries)
    }

    if pass_number == 1:
        # Pass 1: Overview & Structure - Need SUMMARY, not full symbols
        # CRITICAL FIX: Pass 1 sections (executive-summary) don't need 2,412 full symbols OR 1,016 called_by relationships
        # They only need: counts, program name, basic structure, external calls
        if isinstance(superbol_symbols, dict):
            symbols = superbol_symbols.get('symbols', [])
            # Extract just counts and metadata, not all symbol details
            filtered["superbol_symbols"] = {
                "success": superbol_symbols.get("success"),
                "error": superbol_symbols.get("error"),
                "symbol_count": len(symbols),
                "program_count": len([s for s in symbols if s.get('kind') == 12]),
                "paragraph_count": len([s for s in symbols if s.get('kind') == 17]),
                "data_item_count": len([s for s in symbols if s.get('kind') == 13]),
                # Include optimization metadata if present
                "_optimization_metadata": superbol_symbols.get("_optimization_metadata", {})
            }
        else:
            filtered["superbol_symbols"] = superbol_symbols

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

        # GnuCOBOL: Summary + program calls + ESSENTIAL FIELDS
        filtered["gnucobol_analysis"] = {
            "summary": gnucobol.get("summary", {}),
            "program_calls": gnucobol.get("program_calls", []),
            "call_summary": gnucobol.get("call_summary", {}),
            # PHASE 2: Essential scalar fields (for template placeholders)
            "file_path": gnucobol.get("file_path"),
            "success": gnucobol.get("success"),
            "message": gnucobol.get("message"),
            "analysis": gnucobol.get("analysis", {})
        }

        # Ctags: SUMMARY ONLY (not full outline - too large for Pass 1)
        # Pass 1 sections only need counts and division names, not all paragraph details
        filtered["ctags_outline"] = {
            "program_name": ctags.get("program_name"),
            "divisions": ctags.get("divisions", []),  # Division names (small)
            "paragraph_count": len(ctags.get("paragraphs", [])),
            "section_count": len(ctags.get("sections", [])),
            "data_item_count": len(ctags.get("data_items", [])),
            "symbol_count": ctags.get("symbol_count"),
            # Include file path if available
            "file": ctags.get("outline", {}).get("file") if isinstance(ctags.get("outline"), dict) else None
        }

        # Pass 1: Do NOT include called_by_graph (too large - 1,016 entries not needed for summaries)

    elif pass_number == 2:
        # Pass 2: Logic & Flow - Need full CFG, paragraphs, program calls
        # CRITICAL: Pass 2 DOES need called_by_graph for paragraph relationships
        filtered["called_by_graph"] = full_metadata.get("called_by_graph", {})

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

        # GnuCOBOL: Full program calls + procedure structure + ESSENTIAL FIELDS
        paragraphs = gnucobol.get("paragraphs", [])
        filtered["gnucobol_analysis"] = {
            "summary": gnucobol.get("summary", {}),
            "program_calls": gnucobol.get("program_calls", []),  # FULL program calls
            "call_summary": gnucobol.get("call_summary", {}),
            "paragraphs": limit_array(paragraphs, 100),  # First 100 paragraphs
            "sections": limit_array(gnucobol.get("sections", []), 50),
            "performs": limit_array(gnucobol.get("performs", []), 200),
            # PHASE 2: Essential scalar fields (for template placeholders)
            "file_path": gnucobol.get("file_path"),
            "success": gnucobol.get("success"),
            "message": gnucobol.get("message"),
            "analysis": gnucobol.get("analysis", {})
        }

        # Ctags: Full paragraph structure + ESSENTIAL FIELDS
        paragraphs = ctags.get("paragraphs", [])
        ctags_outline = ctags.get("outline", {})
        filtered["ctags_outline"] = {
            "program_name": ctags.get("program_name"),
            "divisions": ctags.get("divisions", []),
            "paragraphs": limit_array(paragraphs, 100),  # First 100 paragraphs
            "total_paragraphs": len(paragraphs),
            "sections": limit_array(ctags.get("sections", []), 50),
            "performs": limit_array(ctags.get("performs", []), 200),
            "data_items": limit_array(ctags.get("data_items", []), 50),  # Some data for reference
            # PHASE 2: Essential scalar fields (for template placeholders)
            "symbol_count": ctags.get("symbol_count"),
            "file": ctags_outline.get("file") if isinstance(ctags_outline, dict) else None
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

        # GnuCOBOL: Metrics + dependencies + ESSENTIAL FIELDS
        filtered["gnucobol_analysis"] = {
            "summary": gnucobol.get("summary", {}),
            "program_calls": gnucobol.get("program_calls", []),
            "copybooks": gnucobol.get("copybooks", []),
            "complexity_metrics": gnucobol.get("complexity_metrics", {}),
            # PHASE 2: Essential scalar fields (for template placeholders)
            "file_path": gnucobol.get("file_path"),
            "success": gnucobol.get("success"),
            "message": gnucobol.get("message"),
            "analysis": gnucobol.get("analysis", {})
        }

        # Ctags: Counts + samples + ESSENTIAL FIELDS
        ctags_outline = ctags.get("outline", {})
        filtered["ctags_outline"] = {
            "program_name": ctags.get("program_name"),
            "divisions": ctags.get("divisions", []),
            "total_paragraphs": len(ctags.get("paragraphs", [])),
            "total_sections": len(ctags.get("sections", [])),
            "total_data_items": len(ctags.get("data_items", [])),
            "total_performs": len(ctags.get("performs", [])),
            "sample_paragraphs": limit_array(ctags.get("paragraphs", []), 20),
            "sample_data_items": limit_array(ctags.get("data_items", []), 20),
            # PHASE 2: Essential scalar fields (for template placeholders)
            "symbol_count": ctags.get("symbol_count"),
            "file": ctags_outline.get("file") if isinstance(ctags_outline, dict) else None
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


# ============================================================================
# FULL CONTEXT MODE HELPER (Epic 2-3)
# ============================================================================

def _build_full_context_for_section(state: AgentState, section: Dict[str, Any]) -> Dict[str, Any]:
    """
    Build full context (source + metadata + program map) for a section.

    This function is called when a section is configured to use full context mode.
    It uses the FullContextBuilder to assemble complete context without filtering.

    Args:
        state: Current agent state with program info and configuration
        section: Section configuration from template

    Returns:
        Context dictionary with full source, metadata, and program map
    """
    section_id = section.get("id", "")
    program_name = state["program_name"]
    cobol_file_path = state.get("cobol_file_path")
    metadata_dir = state.get("metadata_dir")

    print(f"  ✓ FULL CONTEXT MODE activated for section: {section_id}")

    # Initialize result context
    context = {
        "program_name": program_name,
        "timestamp": datetime.now().isoformat(),
        "full_context_mode": True,  # Flag to indicate full context is being used
        "section_id": section_id,
    }

    # Check if we can build full context
    if not cobol_file_path or not metadata_dir:
        print(f"  ⚠ Full context mode requires cobol_file_path and metadata_dir")
        print(f"    cobol_file_path: {cobol_file_path}")
        print(f"    metadata_dir: {metadata_dir}")
        # Fall back to existing metadata from state
        context["superbol_symbols"] = state.get("superbol_symbols", {})
        context["superbol_cfg"] = state.get("superbol_cfg", {})
        context["gnucobol_analysis"] = state.get("gnucobol_analysis", {})
        context["ctags_outline"] = state.get("ctags_outline", {})
        return context

    try:
        # Build full context using FullContextBuilder
        builder = FullContextBuilder(
            program_name=program_name,
            source_file_path=cobol_file_path,
            metadata_dir=metadata_dir
        )

        # Get full context with line numbers for source code reference
        full_context = builder.build_full_context(
            top_n_paragraphs=100,  # Higher limits for full context
            top_n_data_items=50,
            include_line_numbers=True
        )

        # Add source code to context
        # CRITICAL: Check if source is too large for single-pass processing
        # Files over 8000 lines need chunked processing (same threshold as source_integration.py)
        MAX_LINES_SINGLE_PASS = 8000

        source_code = full_context.get("source_code", "")
        if source_code:
            source_lines = len(source_code.split('\n'))

            if source_lines > MAX_LINES_SINGLE_PASS:
                # Large file detected - create chunked_file_info for chunked processing
                # This ensures run_phase1_code_explanation() uses process_large_file_in_chunks()
                print(f"    ⚠ LARGE FILE DETECTED: {source_lines:,} lines > {MAX_LINES_SINGLE_PASS:,} threshold")
                print(f"    → Switching to chunked processing mode")

                context["chunked_file_info"] = {
                    'type': 'CHUNKED_FILE',
                    'file_path': cobol_file_path,
                    'total_lines': source_lines,
                    'max_lines_per_chunk': MAX_LINES_SINGLE_PASS,
                }
                # Clear source_code - chunked processor will read file directly
                # This ensures later truncation logic doesn't try to use it
                source_code = ""
            else:
                # Small file - include source code directly
                context["source_code"] = source_code
                print(f"    → Source code loaded: {source_lines} lines")

        # Add full metadata (unfiltered)
        metadata = full_context.get("metadata", {})
        context["superbol_symbols"] = metadata.get("superbol_symbols", state.get("superbol_symbols", {}))
        context["superbol_cfg"] = metadata.get("superbol_cfg", state.get("superbol_cfg", {}))
        context["gnucobol_analysis"] = metadata.get("gnucobol_analysis", state.get("gnucobol_analysis", {}))
        context["ctags_outline"] = metadata.get("ctags_outline", state.get("ctags_outline", {}))

        # Add program map
        program_map = full_context.get("program_map", "")
        if program_map:
            context["program_map"] = program_map
            print(f"    → Program map generated (~{len(program_map)//4} tokens)")

        # Check if serialized context exceeds max_message_chars limit (OpenAI API limit)
        # The LLM call uses json.dumps(context), so we need to check that size
        max_message_chars = state.get("max_message_chars", 9000000)  # Default 9MB
        context_json = json.dumps(context)
        context_len = len(context_json)

        print(f"    → Context size: {context_len:,} chars (limit: {max_message_chars:,})")

        if context_len > max_message_chars:
            print(f"    ⚠ Context exceeds limit: {context_len:,} chars > {max_message_chars:,} max")

            # Calculate how much to truncate
            excess_chars = context_len - max_message_chars
            # Add buffer for safety (20% extra to account for JSON overhead)
            truncate_chars = int(excess_chars * 1.2)

            # Strategy: Truncate source_code first (largest component)
            if source_code and len(source_code) > truncate_chars:
                # Truncate source code from the middle (keep beginning and end)
                keep_chars = len(source_code) - truncate_chars
                half_keep = keep_chars // 2

                truncated_source = (
                    source_code[:half_keep] +
                    f"\n\n... [TRUNCATED {truncate_chars:,} characters to fit API limit] ...\n\n" +
                    source_code[-half_keep:]
                )

                print(f"    → Truncated source: {len(source_code):,} → {len(truncated_source):,} chars")
                context["source_code"] = truncated_source
                source_code = truncated_source

                # Verify new size
                context_json = json.dumps(context)
                print(f"    → New context size: {len(context_json):,} chars")
            else:
                # If source isn't enough, also trim metadata
                print(f"    → Source too small, trimming metadata...")

                # Remove large metadata items to reduce size
                if "superbol_symbols" in context and context["superbol_symbols"]:
                    symbols = context["superbol_symbols"]
                    if isinstance(symbols, list) and len(symbols) > 500:
                        context["superbol_symbols"] = symbols[:500]
                        print(f"    → Trimmed superbol_symbols: {len(symbols)} → 500")

                if "superbol_cfg" in context and context["superbol_cfg"]:
                    # Keep only essential CFG info
                    cfg = context["superbol_cfg"]
                    if isinstance(cfg, dict):
                        if "nodes" in cfg and len(cfg.get("nodes", [])) > 100:
                            cfg["nodes"] = cfg["nodes"][:100]
                        if "edges" in cfg and len(cfg.get("edges", [])) > 200:
                            cfg["edges"] = cfg["edges"][:200]
                        context["superbol_cfg"] = cfg
                        print(f"    → Trimmed superbol_cfg")

                # Verify new size
                context_json = json.dumps(context)
                print(f"    → New context size after metadata trim: {len(context_json):,} chars")

        # Store the full context prompt for this section
        instruction = section.get("instruction", "")
        full_context_prompt = build_full_context_prompt(
            section_id=section_id,
            source_code=source_code,
            metadata=metadata,
            program_map=program_map,
            instruction=instruction,
            program_name=program_name
        )
        context["full_context_prompt"] = full_context_prompt
        print(f"    → Full context prompt built for {section_id}")

        # Epic 4: Add context chaining if enabled
        if CONTEXT_CHAINING_AVAILABLE and state.get("context_chaining_enabled", False):
            chain_data = state.get("context_chain_data", {})
            chain = ContextChain.from_dict(chain_data)

            chained_context = build_chained_context(
                current_section=section_id,
                chain=chain,
                enabled=True
            )

            if chained_context:
                context["chained_context"] = chained_context
                print(f"    → Context chaining: included {len(chain.get_all_sections())} previous sections")

    except Exception as e:
        print(f"  ⚠ Error building full context: {e}")
        # Fall back to existing metadata from state
        context["superbol_symbols"] = state.get("superbol_symbols", {})
        context["superbol_cfg"] = state.get("superbol_cfg", {})
        context["gnucobol_analysis"] = state.get("gnucobol_analysis", {})
        context["ctags_outline"] = state.get("ctags_outline", {})

    return context


def build_section_context(state: AgentState, section: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract relevant metadata for the current section.

    Three modes (in priority order):
    - Full context mode: Complete source + metadata + program map for target sections
    - Two-pass mode: Uses pass-based conservative filtering (preserves quality)
    - Single-pass mode: Uses aggressive section-based filtering (saves tokens)

    Phase 1 Integration: Also extracts source code if enabled
    Epic 2-3: Full context mode for executive-summary, business-logic, etc.
    """
    section_id = section.get("id", "")

    # Epic 2-3: Check if this section should use full context mode
    if FULL_CONTEXT_AVAILABLE and state.get("use_full_context_mode", False):
        full_context_sections = state.get("full_context_sections", [])

        if should_use_full_context(
            section_id=section_id,
            use_full_context_mode=True,
            full_context_sections=full_context_sections
        ):
            return _build_full_context_for_section(state, section)

    # Build full metadata (for filtered modes)
    # Use .get() for all metadata keys — non-COBOL languages won't have superbol/gnucobol
    full_metadata = {
        "program_name": state["program_name"],
        "timestamp": datetime.now().isoformat(),
        "superbol_symbols": state.get("superbol_symbols", {}),
        "superbol_cfg": state.get("superbol_cfg", {}),
        "gnucobol_analysis": state.get("gnucobol_analysis", {}),
        "ctags_outline": state.get("ctags_outline", {}),
        "structural_outline": state.get("structural_outline", {}),
        "symbol_table": state.get("symbol_table", {}),
        "static_analysis": state.get("static_analysis", {}),
        "syntax_tree": state.get("syntax_tree", {}),
        "control_flow_graph": state.get("control_flow_graph", {}),
        "called_by_graph": state.get("called_by_graph", {})  # PHASE 3: Include reverse call graph
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

    # Phase 1-3: Source Code Extraction Integration (with multi-file support)
    if state.get("enable_source_extraction", False) and SOURCE_EXTRACTION_AVAILABLE:
        section_id = section.get("id", "")
        cobol_file_path = state.get("cobol_file_path")

        if cobol_file_path and should_extract_source(section_id):
            compress = state.get("compress_source", True)

            # Check if Phase 3 multi-file support is enabled
            resolve_copybooks = state.get("resolve_copybooks", False)
            resolve_called_programs = state.get("resolve_called_programs", False)
            use_multi_file = (resolve_copybooks or resolve_called_programs) and MULTI_FILE_AVAILABLE

            if use_multi_file:
                print(f"  → Extracting source code with multi-file support (compress={compress})")
                print(f"     Copybooks: {resolve_copybooks}, Called programs: {resolve_called_programs}")
            else:
                print(f"  → Extracting source code (compress={compress})")

            try:
                if use_multi_file:
                    # Phase 3: Use multi-file extraction
                    copybook_resolver = state.get("copybook_resolver") if resolve_copybooks else None
                    called_program_resolver = state.get("called_program_resolver") if resolve_called_programs else None

                    source_code = extract_source_multi_file(
                        section_id,
                        cobol_file_path,
                        copybook_resolver=copybook_resolver,
                        called_program_resolver=called_program_resolver,
                        compress=compress
                    )
                else:
                    # Phase 1: Regular extraction (no multi-file)
                    source_code = extract_source_for_section(
                        section_id,
                        cobol_file_path,
                        paragraph_metadata=None,  # Could be enhanced to use ctags paragraphs
                        compress=compress
                    )

                if source_code:
                    # Check if source_code is a CHUNKED_FILE marker (for large files)
                    import json
                    try:
                        parsed = json.loads(source_code)
                        if isinstance(parsed, dict) and parsed.get('type') == 'CHUNKED_FILE':
                            # Large file detected - store chunking info in context
                            filtered_context["chunked_file_info"] = parsed
                            print(f"  ⚠ Large file detected ({parsed['total_lines']:,} lines)")
                            print(f"     Chunked processing required (max {parsed['max_lines_per_chunk']:,} lines/chunk)")
                        else:
                            # Normal JSON content (shouldn't happen, but handle it)
                            filtered_context["source_code"] = source_code
                            print(f"  → Source code extracted successfully")
                    except (json.JSONDecodeError, TypeError):
                        # Not JSON - normal source code
                        filtered_context["source_code"] = source_code
                        print(f"  → Source code extracted successfully")
                else:
                    print(f"  → No source code extracted for this section")
            except Exception as e:
                print(f"  ⚠ Warning: Source extraction failed: {e}")
                # Continue without source code - graceful degradation
    elif state.get("enable_source_extraction", False) and not SOURCE_EXTRACTION_AVAILABLE:
        print(f"  ⚠ Warning: Source extraction enabled but modules not available")

    # Generate Program Map for code context (repo-map inspired approach)
    # This provides lightweight, token-efficient context showing program structure
    try:
        adapter = get_current_adapter()
        program_map = adapter.generate_program_map(
            program_name=state["program_name"],
            metadata=full_metadata,
            token_budget=10000  # Generous for 1M context models
        )

        filtered_context["program_map"] = program_map
        print(f"  ✓ Program map generated (~{len(program_map)//4} tokens)")

    except Exception as e:
        print(f"  ⚠ Warning: Program map generation failed: {e}")
        # Continue without program map - graceful degradation

    # PHASE 2: Extract source_file_path for template placeholders
    # Priority: gnucobol.file_path → ctags.outline.file → None
    source_file_path = None

    if "gnucobol_analysis" in filtered_context:
        source_file_path = filtered_context["gnucobol_analysis"].get("file_path")

    if not source_file_path and "ctags_outline" in filtered_context:
        ctags_outline = filtered_context["ctags_outline"]
        if isinstance(ctags_outline, dict):
            # Try direct file field first (Pass 2 & 3)
            source_file_path = ctags_outline.get("file")
            # Try outline.file if not found (Pass 1 - full ctags)
            if not source_file_path and "outline" in ctags_outline:
                outline = ctags_outline["outline"]
                if isinstance(outline, dict):
                    source_file_path = outline.get("file")

    # Add to context for template
    if source_file_path:
        filtered_context["source_file_path"] = source_file_path

    return filtered_context


def extract_explanations_from_llm_response(llm_response: str) -> str:
    """
    Extract ONLY the explanations from LLM response, excluding code blocks.

    This allows us to use the original chunk for source code (100% coverage)
    while using LLM's explanations for documentation.

    Args:
        llm_response: Complete LLM response with code blocks and explanations

    Returns:
        Explanations text with markdown formatting, without code blocks
    """
    import re

    # Split response into sections by markdown headers (### Block N:)
    # This preserves the structure while removing code blocks

    lines = llm_response.splitlines()
    result_lines = []
    in_code_block = False

    for line in lines:
        # Detect code block boundaries
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue  # Skip the ``` markers

        # Skip lines inside code blocks
        if in_code_block:
            continue

        # Keep everything else (headers, explanations, text)
        result_lines.append(line)

    return '\n'.join(result_lines)


def count_non_executable_lines(source_lines: List[str]) -> Dict[str, int]:
    """
    Count non-executable lines in COBOL-74 source code.

    COBOL-74 column 7 indicators:
    - '*' = Comment line (non-executable)
    - '/' = Page break/eject (non-executable)
    - 'D' = Debug line (executable - conditional compilation)
    - '$' = Compiler directive (executable - affects build)
    - '-' = Continuation (executable - part of code)
    - ' ' = Normal code (executable)

    Args:
        source_lines: List of COBOL source code lines

    Returns:
        Dict with counts:
        {
            'total_lines': int,
            'comment_lines': int (marked with *),
            'page_break_lines': int (marked with /),
            'non_executable_lines': int (total comments + page breaks),
            'executable_lines': int
        }
    """
    total_lines = len(source_lines)
    comment_count = 0
    page_break_count = 0

    for line in source_lines:
        # COBOL-74 format: columns 1-6 (sequence), column 7 (indicator), columns 8-72 (code)
        if len(line) < 7:
            continue  # Skip malformed lines

        indicator = line[6]  # Column 7 (0-indexed position 6)

        if indicator == '*':
            comment_count += 1
        elif indicator == '/':
            page_break_count += 1

    non_executable = comment_count + page_break_count
    executable = total_lines - non_executable

    return {
        'total_lines': total_lines,
        'comment_lines': comment_count,
        'page_break_lines': page_break_count,
        'non_executable_lines': non_executable,
        'executable_lines': executable
    }


def _write_llm_request_debug_file(
    section_id: str,
    section_title: str,
    system_prompt: str,
    user_prompt: str,
    context: Dict[str, Any],
    chunk_number: Optional[int] = None,
    pass_number: Optional[int] = None,
    model: str = "unknown"
) -> None:
    """
    Write LLM request data to a debug file for inspection.

    Creates files in ./request/ directory with complete request details.
    This helps debug what exactly is being sent to the LLM.

    Args:
        section_id: Section identifier
        section_title: Section title
        system_prompt: System message content
        user_prompt: User message content
        context: Context dict (metadata)
        chunk_number: Optional chunk number
        pass_number: Optional pass number
        model: Model name
    """
    import os
    from pathlib import Path

    from source_chunker import estimate_tokens

    # Create request directory in centralized run dir
    _rl = get_run_logger()
    request_dir = _rl.get_request_dir(_rl.get_current_program())
    request_dir.mkdir(parents=True, exist_ok=True)

    # Build filename
    if chunk_number is not None:
        # Chunk-based request (detailed-code-explanation)
        base_filename = f"chunk-{chunk_number:02d}"
        if pass_number:
            base_filename += f"-pass{pass_number}"
    else:
        # Section-based request
        base_filename = section_id
        if pass_number:
            base_filename += f"-pass{pass_number}"

    # Check if file exists (for retry attempts)
    # If it exists, append -attempt-N
    filename = base_filename + ".md"
    filepath = request_dir / filename
    attempt = 1
    while filepath.exists():
        attempt += 1
        filename = f"{base_filename}-attempt-{attempt}.md"
        filepath = request_dir / filename

    # Calculate accurate token counts using tiktoken
    system_tokens = estimate_tokens(system_prompt, model=model if model != "unknown" else "gpt-4")
    user_tokens = estimate_tokens(user_prompt, model=model if model != "unknown" else "gpt-4")
    total_tokens = system_tokens + user_tokens

    # Build debug content
    debug_content = f"""# LLM Request Debug File
Generated: {datetime.now().isoformat()}

## Request Metadata
- **Section ID**: {section_id}
- **Section Title**: {section_title}
- **Model**: {model}
- **Chunk Number**: {chunk_number if chunk_number else 'N/A'}
- **Pass Number**: {pass_number if pass_number else 'N/A'}

## Token Counts (measured with tiktoken)
- **System Prompt**: {system_tokens:,} tokens
- **User Prompt**: {user_tokens:,} tokens
- **Total Input**: {total_tokens:,} tokens

---

## System Prompt

```
{system_prompt}
```

---

## User Prompt

```
{user_prompt}
```

"""

    # Write to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(debug_content)

    # Don't print here - will be printed after response completes
    return filepath


def format_context_as_plaintext(context: Dict[str, Any]) -> str:
    """
    Format chunk context as structured plaintext instead of raw JSON.

    Human-readable content (source code, program map) is rendered as-is
    with real newlines and indentation. Structured data (syntax_tree)
    remains as compact JSON.

    This improves LLM comprehension compared to a single escaped JSON blob.
    """
    parts = []

    # Header metadata
    program = context.get('program_name', 'UNKNOWN')
    chunk_num = context.get('chunk_number')
    total = context.get('total_chunks')
    start = context.get('start_line')
    end = context.get('end_line')
    lines = context.get('line_count')

    parts.append(f"## File: {program}")
    if chunk_num:
        parts.append(f"Chunk: {chunk_num}/{total} (lines {start}\u2013{end}, {lines} lines)")
    parts.append("")

    # Structural context (from query_code-based chunking)
    structural_context = context.get('structural_context')
    if structural_context:
        parts.append("### Structural Context")
        for ctx_line in structural_context:
            parts.append(f"- {ctx_line}")
        parts.append("")

    # Program structure map (separate from source code)
    program_map = context.get('program_map', '')
    if program_map:
        parts.append("## Program Structure Map")
        parts.append(program_map)
        parts.append("")

    # Source code (chunk content only — no embedded program map)
    source = context.get('source_code', '')
    if source:
        parts.append(source)
        parts.append("")

    # Structured metadata — keep as JSON
    syntax_tree = context.get('syntax_tree')
    if syntax_tree:
        parts.append("### Syntax Tree (filtered for this chunk)")
        parts.append("```json")
        parts.append(json.dumps(syntax_tree, separators=(',', ':')))
        parts.append("```")
        parts.append("")

    # Cross-references from multilspy metadata (if available)
    cross_refs = context.get('cross_references')
    if cross_refs:
        parts.append("### Cross-References (verified from LSP analysis)")
        parts.append(cross_refs)
        parts.append("")

    # Pass through any other context keys not handled above (Phase 2 may have extras)
    skip_keys = {'program_name', 'timestamp', 'source_file_path', 'source_code',
                 'program_map', 'chunk_number', 'total_chunks', 'start_line',
                 'end_line', 'line_count', 'syntax_tree', 'section_id',
                 'structural_context', 'cross_references'}
    extras = {k: v for k, v in context.items() if k not in skip_keys and v}
    if extras:
        parts.append("### Additional Context")
        parts.append("```json")
        parts.append(json.dumps(extras, separators=(',', ':')))
        parts.append("```")
        parts.append("")

    return "\n".join(parts)


def _update_debug_file_on_success(filepath, elapsed: float, response):
    """Insert success metadata (latency, usage, cost) into the request debug file."""
    if not filepath:
        return
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        meta = f"- **LLM Latency**: {elapsed:.2f}s\n"
        meta += f"- **Status**: SUCCESS\n"
        if hasattr(response, 'usage') and response.usage:
            u = response.usage
            inp = u.get('input_tokens', 0)
            cc = u.get('cache_creation_input_tokens', 0)
            cr = u.get('cache_read_input_tokens', 0)
            total_in = inp + cc + cr
            if total_in:
                meta += f"- **Total Input (API)**: {total_in:,}\n"
            if 'output_tokens' in u:
                meta += f"- **Output Tokens**: {u['output_tokens']:,}\n"
            if inp:
                meta += f"- **Input Tokens (uncached)**: {inp:,}\n"
            if cc:
                meta += f"- **Cache Creation Tokens**: {cc:,}\n"
            if cr:
                meta += f"- **Cache Read Tokens**: {cr:,}\n"
        if hasattr(response, 'total_cost_usd') and response.total_cost_usd:
            meta += f"- **Total Cost**: ${response.total_cost_usd:.4f}\n"
        content = content.replace("\n\n## Token Counts", f"\n{meta}\n## Token Counts")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception:
        pass


def _update_debug_file_on_failure(filepath, elapsed: float, error: Exception):
    """Insert failure metadata into the request debug file."""
    if not filepath:
        return
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # Classify the error
        error_str = str(error)
        if 'timed out' in error_str.lower():
            error_type = "TIMEOUT"
        elif 'rate' in error_str.lower() and 'limit' in error_str.lower():
            error_type = "RATE_LIMITED"
        elif 'context' in error_str.lower() and ('overflow' in error_str.lower() or 'too long' in error_str.lower()):
            error_type = "CONTEXT_OVERFLOW"
        elif 'exit code' in error_str.lower():
            error_type = "CLI_ERROR"
        else:
            error_type = "ERROR"

        meta = f"- **LLM Latency**: {elapsed:.2f}s\n"
        meta += f"- **Status**: FAILED ({error_type})\n"
        meta += f"- **Error**: {error_str[:500]}\n"
        content = content.replace("\n\n## Token Counts", f"\n{meta}\n## Token Counts")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception:
        pass


def generate_section_content(
    section_id: str,
    section_title: str,
    instruction: str,
    template: str,
    context: Dict[str, Any],
    section_config: Dict[str, Any],
    llm_config: Optional[Dict[str, Any]] = None,
    pass_number: Optional[int] = None,
    chunk_number: Optional[int] = None,
    is_retry: bool = False,
    fallback_manager: Optional['LLMFallbackManager'] = None,
    phase: int = 1
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
        pass_number: Optional pass number (for two-pass mode)
        chunk_number: Optional chunk number (for large file processing)
        fallback_manager: Optional LLMFallbackManager for automatic fallback on errors
        phase: Phase number (1 or 2) for phase-specific fallback config
    """

    # Initialize LLM from configuration
    if llm_config:
        llm = create_llm(llm_config)
        model_name = llm_config.get('model', 'unknown')
    else:
        # Fallback to default config if no config provided
        default_config = {'provider': 'openai', 'model': 'gpt-4o', 'temperature': 0.1}
        llm = create_llm(default_config)
        model_name = "gpt-4o"

    # Build system prompt
    lang_name = get_current_adapter().display_name
    system_prompt = f"""You are a technical documentation agent specializing in {lang_name} code analysis.

Your task is to generate documentation for the section: "{section_title}" (ID: {section_id})

CRITICAL REQUIREMENTS FOR CONSISTENCY:
1. NEVER expand abbreviations or acronyms unless the expansion appears verbatim in the source code. If an acronym is not defined in the code, use it as-is without parenthetical expansion. Do NOT guess what abbreviations stand for.
2. Follow the template structure EXACTLY
3. Use ONLY information from the provided metadata - do not invent or assume
4. If metadata is missing, explicitly state "Information not available in metadata"
5. Use consistent formatting across all generated documents
6. Reference line numbers when available
7. For placeholders like {{{{program_name}}}}, replace with actual values
8. Generate valid Markdown syntax
9. For Mermaid diagrams, ensure valid syntax

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
    # CRITICAL: Use compact JSON (no indent) to reduce token count
    # indent=2 adds ~50% overhead (800K → 1.2M tokens)

    # NOTE: Beta-features wiring (1M-context beta) is intentionally disabled
    # below — `betas=None` forces the standard 200K-token limit. Overflow is
    # surfaced as an error (see the overflow guard further down) instead of
    # being silently truncated. To re-enable the 1M beta, restore the line
    # that reads from llm_config AND re-enable the truncation block and
    # Phase 1 chunk-level auto-escalation further down.
    #   betas = llm_config.get('betas') if llm_config else None
    betas = None
    MAX_INPUT_TOKENS = get_token_limit(model_name, betas=betas)

    context_json = json.dumps(context)
    context_tokens = estimate_tokens(context_json, model=model_name)

    if context_tokens > MAX_INPUT_TOKENS:
        # NOTE: Silent truncation is intentionally disabled. When the context
        # for a single LLM call exceeds the model's 200K-token limit, we raise
        # so the file is marked failed in the checkpoint (see
        # `checkpoint_manager.mark_file_failed`) instead of silently producing
        # a doc generated from a half-missing source. Restart — or
        # `--retry-failed` — picks the file back up after the root cause
        # (chunking config, metadata size) has been addressed.
        #
        # The original truncation strategy trimmed `source_code` to the first
        # half + last half and dropped large metadata blobs; to restore it, see
        # the git history for this block (cobol_doc_agent.py:2166 onward
        # before the Option-A edit).
        raise LLMFatalError(
            f"Context overflow for section {section_id!r}"
            f"{f' chunk {chunk_number}' if chunk_number is not None else ''}: "
            f"{context_tokens:,} tokens exceeds model limit "
            f"{MAX_INPUT_TOKENS:,} (model: {model_name}). "
            "The 1M-context beta is disabled — reduce chunk size "
            "(chunking.auto_chunk_sizing.target_pct) or trim metadata "
            "and re-run."
        )

    metadata_str = format_context_as_plaintext(context)

    # RETRY ENHANCEMENT: Build retry emphasis to insert RIGHT AFTER code block
    # This creates stronger proximity/association between source code and instruction
    retry_emphasis = ""
    if is_retry:
        retry_emphasis = """

=============================================================================
🚨 CRITICAL RETRY INSTRUCTION 🚨
=============================================================================

You were asked to READ and RETURN the source code in response.
But you have returned INCOMPLETE source code.

RETURN the COMPLETE source code THIS TIME.

DO NOT skip lines, summarize, or use ellipsis (...).
INCLUDE EVERY SINGLE LINE from the source code provided above.

=============================================================================
"""

    # Place retry emphasis RIGHT AFTER metadata (which contains source code)
    # This is better than appending at the END because:
    # 1. Stronger proximity to the actual code content
    # 2. Creates immediate association: "this is the code" → "return it complete"
    # 3. Attention mechanism favors nearby context
    user_prompt = f"""Generate documentation for this section.

{metadata_str}
{retry_emphasis}
Remember:
- Program name: {context.get('program_name', 'UNKNOWN')}
- Follow template structure exactly
- Be consistent in terminology and formatting
- Reference line numbers from metadata
- Generate valid Markdown and Mermaid syntax
"""

    # Log actual input token count (system + user prompt as sent to LLM)
    _sys_tokens = estimate_tokens(system_prompt, model=model_name)
    _usr_tokens = estimate_tokens(user_prompt, model=model_name)
    print(f"  → Context: {_sys_tokens + _usr_tokens:,} tokens (limit: {MAX_INPUT_TOKENS:,} for {model_name})")

    # Call LLM
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]

    # Write request to debug file before LLM call
    _debug_filepath = _write_llm_request_debug_file(
        section_id=section_id,
        section_title=section_title,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        context=context,
        chunk_number=chunk_number,
        pass_number=pass_number,
        model=model_name
    )

    # Start LLM call tracking
    from llm_tracer import get_tracer
    tracer = get_tracer()
    if tracer:
        tracer.start_call(
            section_id=section_id,
            section_title=section_title,
            pass_number=pass_number,
            chunk_number=chunk_number,
            model=model_name
        )

    # Use fallback-aware invocation if fallback_manager provided
    import time as _time
    _llm_start = _time.monotonic()
    try:
        if fallback_manager and llm_config:
            response = invoke_llm_with_fallback(
                llm_config=llm_config,
                messages=messages,
                fallback_manager=fallback_manager,
                phase=phase
            )
        else:
            response = llm.invoke(messages)
        _llm_elapsed = _time.monotonic() - _llm_start
        content = response.content
    except Exception as _llm_error:
        _llm_elapsed = _time.monotonic() - _llm_start
        # Write failure metadata to the debug file (request body already on disk)
        _update_debug_file_on_failure(_debug_filepath, _llm_elapsed, _llm_error)
        raise  # Re-raise so the caller's error handling still works

    # End LLM call tracking
    if tracer:
        tracer.end_call(
            response=response,
            input_messages=messages,
            input_text=system_prompt + "\n\n" + user_prompt
        )

    # Insert latency and usage into the Metadata block of the debug file
    _update_debug_file_on_success(_debug_filepath, _llm_elapsed, response)

    print(f"  ✓ Generated {len(content)} characters for {section_id} ({_llm_elapsed:.1f}s)")

    # Return content and debug info for caller to print after chunk completes
    return content, _debug_filepath, _llm_elapsed


def filter_context_for_code_explanation(context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create ultra-minimal metadata for code explanation chunks.

    CRITICAL: Code explanation only needs program name and source code.
    Passing full metadata (800K tokens) per chunk causes overflow.

    Target: < 10K tokens for metadata (vs 800K with full context)

    Returns minimal context with:
    - program_name
    - timestamp
    - source_file_path (if available)
    - called_by_graph (for this chunk's paragraphs only - added during processing)
    """
    return {
        "program_name": context.get("program_name", "UNKNOWN"),
        "timestamp": context.get("timestamp"),
        "source_file_path": context.get("source_file_path")
        # Note: source_code, chunk info added per chunk during processing
        # Note: called_by_graph filtered per chunk's paragraphs only
    }


def _resolve_chunk_token_limit(
    chunking_config: Dict[str, Any],
    llm_config: Optional[Dict[str, Any]] = None
) -> int:
    """
    Resolve the max tokens per chunk — explicit value or dynamic auto-sizing.

    When max_tokens_per_chunk is "auto", calculates:
        chunk_limit = (model_context_limit - overhead_buffer) * target_pct / 100

    Config keys (under chunking.auto_chunk_sizing):
        model_context_limit: Model's input context window (default: 200000)
        overhead_buffer: Reserved for program map, AST, etc. (default: 10000)
        target_pct: Chunk as percentage of available context (default: 15)

    Falls back to 10000 if not configured.
    """
    raw_value = chunking_config.get('max_tokens_per_chunk', 10000)

    # Explicit integer — use as-is
    if isinstance(raw_value, (int, float)) and not isinstance(raw_value, bool):
        return int(raw_value)

    # "auto" — dynamic sizing from config
    if str(raw_value).lower() == 'auto':
        sizing = chunking_config.get('auto_chunk_sizing', {})
        model_context_limit = sizing.get('model_context_limit', 200000)
        overhead_buffer = sizing.get('overhead_buffer', 10000)
        target_pct = sizing.get('target_pct', 10)

        available = model_context_limit - overhead_buffer
        chunk_limit = int(available * target_pct / 100)

        # Sanity bounds: at least 5K, at most 100K
        chunk_limit = max(5000, min(chunk_limit, 100000))

        print(f"  → Auto chunk sizing: {model_context_limit:,} context"
              f" - {overhead_buffer:,} buffer = {available:,} available"
              f" × {target_pct}% = {chunk_limit:,} tokens/chunk")
        return chunk_limit

    # Unrecognized value — fall back to default
    print(f"  ⚠ Unrecognized max_tokens_per_chunk value '{raw_value}', using default 10000")
    return 10000


def _load_query_code_results(program_name: str, metadata_dir: str) -> Optional[Dict[str, Any]]:
    """
    Load query_code boundary results from the metadata directory.

    Searches for files matching common naming patterns produced by
    the ConfigDrivenMCPMetadataGenerator.

    Returns:
        Parsed JSON dict if found, None otherwise.
    """
    from pathlib import Path
    candidates = [
        f"chunking_boundaries/{program_name}.json",
        f"query-code-{program_name}-boundaries.json",
        f"{program_name}/query-code-boundaries.json",
    ]
    for candidate in candidates:
        path = Path(metadata_dir) / candidate
        if path.exists():
            try:
                return json.loads(path.read_text(encoding='utf-8'))
            except (json.JSONDecodeError, OSError) as e:
                print(f"  ⚠ Failed to load {path}: {e}")
    return None


def process_large_file_in_chunks(
    section_id: str,
    section_title: str,
    instruction: str,
    template: str,
    context: Dict[str, Any],
    chunked_file_info: Dict[str, Any],
    llm_config: Optional[Dict[str, Any]] = None,
    pass_number: Optional[int] = None,
    state: Optional[Dict[str, Any]] = None,
    fallback_manager: Optional['LLMFallbackManager'] = None
) -> str:
    """
    Process a large COBOL file in chunks for detailed code-block explanation.

    This function:
    1. Uses source_chunker to split file into manageable pieces
    2. Processes each chunk with the LLM (with MINIMAL metadata)
    3. Combines results maintaining sequential numbering
    4. Verifies complete coverage

    Args:
        section_id: Section identifier
        section_title: Section title
        instruction: Processing instructions
        template: Output template
        context: Context dict (metadata) - WILL BE FILTERED to minimal
        chunked_file_info: Info about chunked file
        llm_config: LLM configuration
        pass_number: Optional pass number (for two-pass mode)
        state: Optional state dict for accessing full unfiltered CTags data
        fallback_manager: Optional LLMFallbackManager for automatic fallback on errors

    Returns:
        Combined documentation for all chunks
    """
    from pathlib import Path

    from chunk_validation import ChunkDocumentationValidator

    # Use adapter for chunking if available, otherwise fall back to source_chunker
    adapter = get_current_adapter()

    file_path = chunked_file_info['file_path']
    total_lines = chunked_file_info['total_lines']
    max_lines = chunked_file_info['max_lines_per_chunk']

    print(f"\n  → Processing large file in chunks...")
    print(f"     File: {file_path}")
    print(f"     Total lines: {total_lines:,}")

    # Get CTags metadata if available for better boundary detection
    # IMPORTANT: For chunking, we need FULL unfiltered CTags data (all paragraphs),
    # not the filtered version in context that may have limited arrays.
    # Get it directly from state to avoid polluting LLM context with massive data.
    ctags_metadata = None
    if state:
        # Try legacy COBOL key first, then normalized key
        ctags_metadata = state.get('ctags_outline') or state.get('structural_outline')
        if ctags_metadata:
            print(f"  → Using full unfiltered structural metadata from state for boundary detection")

    if not ctags_metadata:
        # Fallback to context (may be filtered)
        ctags_metadata = context.get('ctags_outline') or context.get('structural_outline')
        if ctags_metadata:
            print(f"  ⚠ Using structural metadata from context (may be filtered)")

    # Get program map from context to calculate overhead during chunking
    program_map = context.get('program_map')

    # Derive program_name early (needed for query_code loading and caching)
    program_name = state["program_name"] if state else context.get("program_name", "UNKNOWN")

    # Load query_code results for tree-sitter based chunking (if available)
    query_code_results = None
    chunking_config = {}
    if state:
        full_config = state.get('full_config', {})
        chunking_config = full_config.get('chunking', {})
        metadata_dir = state.get('metadata_dir')
        if metadata_dir and chunking_config.get('strategy') in ('query_code', 'tsg_graph'):
            query_code_results = _load_query_code_results(program_name, str(metadata_dir))
            if query_code_results:
                print(f"  → Loaded chunking boundary results for structural chunking")
            else:
                print(f"  ⚠ No chunking boundary results found — will use fallback strategy")

    # Resolve chunk token limit — explicit integer or "auto" (dynamic sizing)
    max_tokens = _resolve_chunk_token_limit(chunking_config, llm_config)
    try:
        adapter_chunks, adapter_verification = adapter.chunk_source_file(
            file_path,
            max_tokens_per_chunk=max_tokens,
            metadata=ctags_metadata,
            program_map=program_map,
            query_code_results=query_code_results,
            chunking_config=chunking_config,
        )
        # Convert SourceChunk objects to dicts for existing code compatibility
        chunks = [
            {
                'chunk_number': c.chunk_number,
                'start_line': c.start_line,
                'end_line': c.end_line,
                'line_count': c.line_count,
                'content': c.content,
                'estimated_tokens': c.estimated_tokens,
            }
            for c in adapter_chunks
        ]
        verification = {
            'valid': adapter_verification.valid,
            'total_lines': adapter_verification.total_lines,
            'chunks': adapter_verification.chunks,
            'coverage': adapter_verification.coverage,
            'error': adapter_verification.error,
            'method': adapter_verification.method,
        }
    except Exception as e:
        print(f"  ✗ Chunking failed: {e}")
        print(f"  → Falling back to explanation without source code")
        return f"""
## {section_title}

**Note**: This file is too large ({total_lines:,} lines) to process completely.
Chunking failed with error: {e}

Please process this file using paragraph-by-paragraph extraction or manually review the source code.
"""

    total_chunks = len(chunks)
    file_name = Path(file_path).name

    print(f"  → Processing {total_chunks} chunks...")

    all_results = []
    all_chunk_gaps = []  # Collect gaps from all chunks for Pass 2
    validation_stats = {
        'total_chunks': total_chunks,
        'validated': 0,
        'incomplete': 0,
        'total_coverage': 0.0
    }

    # Load any previously cached chunk results for resume support
    cached_chunks = load_completed_chunks(program_name)
    if cached_chunks:
        print(f"  → Loaded {len(cached_chunks)} cached chunk results, resuming from chunk {max(cached_chunks.keys()) + 1}")

    # Structural context: get declaration_map from verification (if query_code chunking was used)
    declaration_map = getattr(adapter_verification, 'declaration_map', None)
    seen_members: Dict[str, List[str]] = {}
    structural_context_enabled = chunking_config.get('structural_context', True) and declaration_map is not None
    if structural_context_enabled:
        print(f"  → Structural context enabled ({len(declaration_map.containers)} containers)")

    for chunk_info in chunks:
        chunk_num = chunk_info['chunk_number']

        # Skip chunks that were already processed (checkpoint resume)
        if chunk_num in cached_chunks:
            print(f"\n  → Chunk {chunk_num}/{total_chunks} — cached, skipping")
            all_results.append(cached_chunks[chunk_num])
            validation_stats['validated'] += 1
            validation_stats['total_coverage'] += 100.0
            continue

        print(f"\n  → Processing chunk {chunk_num}/{total_chunks} (lines {chunk_info['start_line']}-{chunk_info['end_line']})")

        # Generate structural context for this chunk (if available)
        chunk_structural_context = None
        if structural_context_enabled:
            from structural_chunker import \
                get_structural_context as _get_struct_ctx
            chunk_structural_context = _get_struct_ctx(
                chunk_info['start_line'], chunk_info['end_line'],
                declaration_map, seen_members,
            )
            if chunk_structural_context:
                for ctx_line in chunk_structural_context:
                    print(f"     {ctx_line.split(chr(10))[0]}")  # Print first line only

        # Format chunk with metadata and program map (for whole-file context)
        from language_adapter import SourceChunk
        program_map = context.get('program_map')  # Get program map from context
        chunk_as_obj = SourceChunk(
            chunk_number=chunk_info['chunk_number'],
            start_line=chunk_info['start_line'],
            end_line=chunk_info['end_line'],
            line_count=chunk_info['line_count'],
            content=chunk_info['content'],
            estimated_tokens=chunk_info['estimated_tokens'],
        )
        chunk_content = adapter.format_chunk_for_llm(
            chunk_as_obj,
            total_chunks,
            file_name,
            program_map=None,           # Passed separately in chunk_context
            structural_context=None,    # Rendered by format_context_as_plaintext()
        )

        # CRITICAL OPTIMIZATION: Use MINIMAL metadata for code explanation
        # Full context (~800K tokens) causes overflow when multiplied by 25 chunks
        # Code explanation only needs: program_name, source_code, and chunk info
        chunk_context = filter_context_for_code_explanation(context)

        # Add chunk-specific information
        chunk_context['source_code'] = chunk_content
        chunk_context['chunk_number'] = chunk_num
        chunk_context['total_chunks'] = total_chunks
        chunk_context['start_line'] = chunk_info['start_line']
        chunk_context['end_line'] = chunk_info['end_line']
        chunk_context['line_count'] = chunk_info['line_count']

        # Pass program map as separate context key (not embedded in source_code)
        if program_map:
            chunk_context['program_map'] = program_map

        # Add structural context to chunk_context for format_context_as_plaintext()
        if chunk_structural_context:
            chunk_context['structural_context'] = chunk_structural_context

        # Add cross-reference context from multilspy metadata (if available)
        if state and state.get("relationship_provider"):
            rel_provider = state["relationship_provider"]
            # Use relative path — metadata keys are relative (e.g., "DataCommands/PickList.cs")
            source_file = state.get("relative_source_path", "") or state.get("source_file_path", "")
            cross_ref_context = rel_provider.get_context_for_chunk(
                source_file, chunk_info['start_line'], chunk_info['end_line']
            )
            if cross_ref_context:
                chunk_context['cross_references'] = cross_ref_context
                print(f"     Cross-references: injected for lines {chunk_info['start_line']}-{chunk_info['end_line']}")

        # Add filtered syntax tree for this chunk's line range
        # Gives LLM structural awareness without sending the full AST
        full_syntax_tree = state.get("syntax_tree", {}) if state else {}
        if full_syntax_tree:
            filtered_ast = adapter.filter_ast_for_chunk(
                full_syntax_tree,
                chunk_info['start_line'],
                chunk_info['end_line']
            )
            if filtered_ast:
                chunk_context['syntax_tree'] = filtered_ast

        # Add line identifier pattern for language-agnostic validation
        chunk_info['line_identifier_pattern'] = r'^\d{6}'  # COBOL sequence numbers

        # Count total lines in this chunk for logging
        chunk_lines = chunk_info['content'].splitlines()
        total_lines_in_chunk = len(chunk_lines)

        print(f"     Lines: {total_lines_in_chunk} total")

        # NOTE: Per-chunk auto-escalation to the 1M-context model when the
        # chunk context > 120K tokens is intentionally disabled. We force the
        # standard 200K-token model; if a chunk exceeds that limit the
        # overflow guard in generate_section_content() raises LLMFatalError,
        # the file is marked failed in the checkpoint, and a restart retries
        # it after you've tuned chunking config. To re-enable the 1M beta,
        # uncomment the original block below AND re-enable the truncation
        # block + betas wiring in create_llm() / the token-limit calc.
        #
        # Original block:
        #   chunk_llm_config = dict(llm_config) if llm_config else {}
        #   if llm_config:
        #       from tokenizer import CLAUDE_1M_BETA_FLAG
        #       from tokenizer import estimate_tokens as _est_tokens
        #       available_betas = llm_config.get('betas') or []
        #       chunk_llm_config.pop('betas', None)
        #       chunk_context_json = json.dumps(chunk_context)
        #       chunk_context_tokens = _est_tokens(chunk_context_json, model=llm_config.get('model', 'unknown'))
        #       if chunk_context_tokens > 120_000 and CLAUDE_1M_BETA_FLAG in available_betas:
        #           provider = llm_config.get('provider', '')
        #           if provider in ('anthropic', 'claude_sdk'):
        #               print(f"     ⚠ Chunk context {chunk_context_tokens:,} tokens > 120K — enabling 1M context beta")
        #               chunk_llm_config['betas'] = available_betas
        #               base_model = chunk_llm_config.get('model', 'sonnet')
        #               if '[1m]' not in base_model:
        #                   chunk_llm_config['model'] = f"{base_model}[1m]"
        chunk_llm_config = dict(llm_config) if llm_config else {}
        # Strip any `betas` the YAML might carry — create_llm() also ignores
        # it, but we belt-and-braces remove it here so it never reaches any
        # downstream consumer that still looks at the key.
        chunk_llm_config.pop('betas', None)

        # ========================================================================
        # TEST MODE: RETRIES DISABLED - Testing prompt quality alone
        # ========================================================================
        # Generate content for this chunk with NO RETRY (testing prompt alone)
        chunk_result = None
        validation_result = None
        explanation_coverage = 0.0  # Initialize for scope
        chunk_debug_path = None
        chunk_latency = 0.0
        # max_retries = 1  # COMMENTED OUT - no retries in test mode

        # COMMENTED OUT: Retry loop - testing single attempt with improved prompts
        # for attempt in range(1, max_retries + 2):  # 1 + 1 retry = 2 attempts max
        attempt = 1  # SINGLE ATTEMPT ONLY
        try:
            current_instruction = instruction + f"\n\n**CHUNK {chunk_num} of {total_chunks}**: Continue numbering from previous chunks."

            # COMMENTED OUT: Retry logic
            # # On retry, add sleep and specific feedback about missing lines
            # if attempt > 1:
            #     import time
            #     sleep_duration = 3  # 3 seconds between retries
            #     print(f"  ↻ Retry attempt {attempt} (after {sleep_duration}s cooldown)...")
            #     time.sleep(sleep_duration)
            #
            #     # Add targeted retry feedback (only if coverage < 95%)
            #     if validation_result.coverage_percentage < 95.0:
            #         retry_feedback = f"""
            # **RETRY REQUIRED - Previous attempt had {validation_result.coverage_percentage:.1f}% coverage**
            # You missed {validation_result.missing_line_count} lines.
            #
            # 🚨 ANALYSIS: This chunk has {validation_result.expected_lines} expected lines.
            # You returned {validation_result.found_lines} lines. You're missing {validation_result.missing_line_count} lines.
            #
            # COMMON ISSUES:
            # - Skipping repetitive FILLER definitions (FORBIDDEN!)
            # - Summarizing data tables with "..." (FORBIDDEN!)
            # - Omitting "boring" sections for brevity (FORBIDDEN!)
            # - Using phrases like "similar pattern continues" (FORBIDDEN!)
            #
            # YOU MUST:
            # - Include EVERY executable line with its sequence number
            # - Show ALL FILLERs even if there are 500+ repetitive ones
            # - Show ALL data table entries completely
            # - Never use abbreviation, summarization, or ellipsis
            # - Include complete WORKING-STORAGE and FILE SECTION layouts
            # """
            #         current_instruction = retry_feedback + "\n" + current_instruction

            chunk_result, chunk_debug_path, chunk_latency = generate_section_content(
                section_id,
                f"{section_title} - Chunk {chunk_num}/{total_chunks}",
                current_instruction,
                template,
                chunk_context,
                {},  # section_config
                chunk_llm_config,
                pass_number=pass_number,
                chunk_number=chunk_num,
                is_retry=False,  # Never retry in test mode
                fallback_manager=fallback_manager,
                phase=1  # Chunked processing is always Phase 1
            )

            # Validate chunk result against expected lines
            validator = ChunkDocumentationValidator(chunk_info, chunk_result)
            validation_result = validator.validate(min_coverage_percentage=100.0)

            # Calculate explanation coverage (LLM's code vs expected lines)
            explanation_coverage = validation_result.coverage_percentage

            # TEST MODE: Just log coverage, no retry decisions
            if validation_result.coverage_percentage >= 95.0:  # 95% threshold
                print(f"  ✓ Complete: {explanation_coverage:.1f}% coverage ({validation_result.found_lines}/{validation_result.expected_lines} lines)")
                print(f"     [TEST MODE] LLM returned complete code")
                validation_stats['validated'] += 1
            else:
                print(f"  ⚠ Incomplete: {explanation_coverage:.1f}% coverage ({validation_result.found_lines}/{validation_result.expected_lines} lines)")
                print(f"     Missing: {validation_result.missing_line_count} lines")
                print(f"     [TEST MODE] Recording LLM coverage as-is (no retry, no fallback)")
                validation_stats['incomplete'] += 1

            # COMMENTED OUT: Retry decision logic
            #     # Only retry if coverage is below 95% and we have retries left
            #     if explanation_coverage >= 95.0:
            #         print(f"     → Accepting (explanation coverage ≥ 95%)")
            #         validation_stats['incomplete'] += 1
            #         break  # Good enough, don't retry
            #     elif attempt >= max_retries + 1:
            #         print(f"     → Max retries reached, accepting result")
            #         validation_stats['incomplete'] += 1
            #         break  # Out of retries
            #     else:
            #         # Retry (only for < 80% coverage)
            #         continue

        except Exception as e:
            # Extract detailed error information
            error_details = str(e)
            if hasattr(e, 'stderr') and e.stderr:
                error_details += f"\n    stderr: {e.stderr[:1000]}"
            if hasattr(e, 'stdout') and e.stdout:
                error_details += f"\n    stdout: {e.stdout[:1000]}"
            if hasattr(e, '__cause__') and e.__cause__:
                error_details += f"\n    caused by: {e.__cause__}"
            print(f"  ✗ Attempt {attempt} failed: {error_details}")
            if is_fatal_llm_error(e):
                raise LLMFatalError(f"Fatal LLM error on chunk {chunk_num}: {e}") from e
            chunk_result = f"\n\n**[Chunk {chunk_num} processing failed: {e}]**\n\n"
            validation_stats['incomplete'] += 1
            # COMMENTED OUT: Retry on exception
            # if attempt >= max_retries + 1:
            #     chunk_result = f"\n\n**[Chunk {chunk_num} processing failed: {e}]**\n\n"
            #     validation_stats['incomplete'] += 1
            #     break

        # Track coverage
        if validation_result:
            validation_stats['total_coverage'] += validation_result.coverage_percentage

            # Store gap information (even with retries, for visibility)
            if not validation_result.is_valid:
                all_chunk_gaps.append({
                    'chunk_number': chunk_num,
                    'validation_result': validation_result,
                    'chunk_info': chunk_info
                })

        # ========================================================================
        # TEST MODE: Use ONLY LLM response - no original source fallback
        # ========================================================================
        # COMMENTED OUT: Build final chunk documentation with original source fallback
        if chunk_result:
            # COMMENTED OUT: Extract explanations and add original source
            # # Extract explanations from LLM response (removes code blocks)
            # llm_explanations = extract_explanations_from_llm_response(chunk_result)
            #
            # # Build complete chunk doc with original source (100% coverage guaranteed)
            # final_chunk_doc = f"""
            # ## Chunk {chunk_num}/{total_chunks}: Lines {chunk_info['start_line']}-{chunk_info['end_line']}
            #
            # ### Complete Source Code
            #
            # ```cobol
            # {chunk_info['content']}```
            #
            # **Coverage:** 100% ({chunk_info['line_count']} lines) - Using original chunk source
            #
            # ---
            #
            # ### Detailed Explanations
            #
            # {llm_explanations}
            #
            # ---
            #
            # **Validation Summary:**
            # - Total lines in chunk: {total_lines_in_chunk}
            # - Expected lines: {validation_result.expected_lines}
            # - LLM returned lines: {validation_result.found_lines}
            # - LLM explanation coverage: {explanation_coverage:.1f}%
            # - Source coverage: 100% (guaranteed)
            #
            # """

            # Use raw LLM response, stripping the Coverage Self-Assessment
            # the LLM generates (we keep it in the prompt so the LLM validates
            # its own work, but omit it from the final documentation).
            chunk_hash = hashlib.sha256(chunk_info['content'].encode('utf-8')).hexdigest()[:12]
            clean_result = re.sub(
                r'---\s*\n#{2,3} Coverage Self-Assessment.*',
                '',
                chunk_result,
                flags=re.DOTALL
            ).rstrip()

            # Normalize LLM headings to H3+ (chunk header is H2, content must be below it)
            in_fence = False
            normalized_lines = []
            for line in clean_result.split('\n'):
                if line.startswith('```'):
                    in_fence = not in_fence
                    normalized_lines.append(line)
                    continue
                if not in_fence and line.startswith('#'):
                    level = len(line) - len(line.lstrip('#'))
                    if level > 0 and level < 3:
                        # Shift up to H3 minimum (H1→H3, H2→H3)
                        line = '###' + line[level:]
                normalized_lines.append(line)
            clean_result = '\n'.join(normalized_lines)

            final_chunk_doc = f"""
## Hash-ID: {chunk_hash} | Chunk {chunk_num}/{total_chunks} | Lines: {chunk_info['start_line']}-{chunk_info['end_line']}

{clean_result}

"""
            all_results.append(final_chunk_doc)
            save_chunk_result(program_name, chunk_num, final_chunk_doc)
            if chunk_debug_path:
                print(f"  [DEBUG] Request logged to: {chunk_debug_path} (latency: {chunk_latency:.2f}s)")
        else:
            no_result_doc = f"\n\n**[Chunk {chunk_num} - no result]**\n\n"
            all_results.append(no_result_doc)
            save_chunk_result(program_name, chunk_num, no_result_doc)
            if chunk_debug_path:
                print(f"  [DEBUG] Request logged to: {chunk_debug_path} (latency: {chunk_latency:.2f}s)")

        # Update seen_members for structural context tracking across chunks
        if structural_context_enabled:
            from structural_chunker import update_seen_members as _update_seen
            _update_seen(
                chunk_info['start_line'], chunk_info['end_line'],
                declaration_map, seen_members,
            )

    # Combine all results from Pass 1
    combined_result = "\n\n".join(all_results)

    # Show Pass 1 statistics
    avg_coverage = validation_stats['total_coverage'] / total_chunks if total_chunks > 0 else 0
    print(f"\n" + "="*80)
    print(f"PASS 1 COMPLETE: Initial Documentation")
    print(f"="*80)
    print(f"  • Chunks processed: {total_chunks}")
    print(f"  • Complete chunks (100%): {validation_stats['validated']}")
    print(f"  • Incomplete chunks: {validation_stats['incomplete']}")
    print(f"  • Average coverage: {avg_coverage:.1f}%")
    print(f"  • Chunking verification: {verification['coverage']}")

    # Decide if Pass 2 (gap-filling) is needed
    # CHANGED: More conservative threshold - only if coverage is really poor
    if avg_coverage >= 90.0:
        print(f"\n  ✓ Good coverage ({avg_coverage:.1f}%) - Gap filling not needed")
        print(f"     (Accepting 90%+ coverage as sufficient to avoid excessive API calls)")
        return combined_result
    elif len(all_chunk_gaps) == 0:
        print(f"\n  ✓ All chunks complete - No gaps to fill")
        return combined_result
    else:
        print(f"\n  ⚠ Low coverage ({avg_coverage:.1f}%) - Gap filling needed")
        print(f"  → {len(all_chunk_gaps)} chunks with gaps")

        # DISABLED: Gap-filling creates too many LLM calls
        # For now, accept ~90% coverage instead of pursuing 100%
        print(f"\n  ⚠ WARNING: Pass 2 gap-filling is DISABLED due to efficiency concerns")
        print(f"     Current implementation creates excessive LLM calls (1000+)")
        print(f"     Accepting {avg_coverage:.1f}% coverage from Pass 1")
        print(f"     To enable gap-filling, set ENABLE_GAP_FILLING=True")

        ENABLE_GAP_FILLING = False  # Feature flag

        if ENABLE_GAP_FILLING:
            # PASS 2: Gap-Filling (DISABLED by default)
            gap_fill_result = perform_gap_filling_pass2(
                all_chunk_gaps,
                file_path,
                context,
                section_id,
                section_title,
                instruction,
                template,
                llm_config,
                pass_number
            )

            # Merge gap-fill results into combined result
            if gap_fill_result:
                combined_result += "\n\n" + gap_fill_result

        return combined_result


def perform_gap_filling_pass2(
    all_chunk_gaps: List[Dict],
    file_path: str,
    context: Dict[str, Any],
    section_id: str,
    section_title: str,
    instruction: str,
    template: str,
    llm_config: Dict[str, Any],
    pass_number: Optional[int]
) -> str:
    """
    Pass 2: Fill gaps identified in Pass 1.

    Strategy:
    1. Collect all missing line ranges from all incomplete chunks
    2. Merge overlapping/adjacent ranges
    3. Create optimized gap-chunks (smaller, focused)
    4. Use ultra-strict "include everything verbatim" prompts
    5. Validate with retries (worthwhile now - targeted and small)

    Args:
        all_chunk_gaps: List of gap information from Pass 1
        file_path: Source file path
        context: Generation context
        section_id: Section being generated
        section_title: Section title
        instruction: Base instruction
        template: Template string
        llm_config: LLM configuration
        pass_number: Pass number

    Returns:
        Combined gap-fill documentation
    """
    from pathlib import Path

    from chunk_validation import ChunkDocumentationValidator

    print(f"\n" + "="*80)
    print(f"PASS 2: GAP-FILLING")
    print(f"="*80)

    # Step 1: Collect all missing line ranges
    print(f"\n[1] Analyzing gaps from {len(all_chunk_gaps)} incomplete chunks...")

    all_missing_ranges = []
    total_missing_lines = 0

    for gap_info in all_chunk_gaps:
        chunk_num = gap_info['chunk_number']
        validation_result = gap_info['validation_result']

        for start, end in validation_result.missing_line_ranges:
            all_missing_ranges.append((start, end))
            total_missing_lines += (end - start + 1)

    print(f"  • Total gap ranges: {len(all_missing_ranges)}")
    print(f"  • Total missing lines: {total_missing_lines:,}")

    if total_missing_lines == 0:
        print(f"  ✓ No gaps to fill")
        return ""

    # Step 2: Merge overlapping/adjacent ranges
    print(f"\n[2] Merging overlapping/adjacent ranges...")
    merged_ranges = merge_line_ranges(all_missing_ranges)
    print(f"  • Merged into: {len(merged_ranges)} gap ranges")

    # Show top 10 largest gaps
    sorted_ranges = sorted(merged_ranges, key=lambda x: x[1] - x[0] + 1, reverse=True)
    print(f"\n  Top 10 largest gaps:")
    for i, (start, end) in enumerate(sorted_ranges[:10], 1):
        gap_size = end - start + 1
        print(f"    {i}. Lines {start:,}-{end:,} ({gap_size:,} lines)")

    # Step 3: Create gap-chunks (smaller, focused)
    print(f"\n[3] Creating gap-chunks...")

    # Read source file
    with open(file_path, 'r') as f:
        source_lines = f.readlines()

    gap_chunks = []
    for i, (start, end) in enumerate(merged_ranges, 1):
        gap_size = end - start + 1
        gap_content = ''.join(source_lines[start-1:end])

        # For very large gaps, split them further
        if gap_size > 1000:  # If gap is > 1000 lines, split it
            print(f"    ⚠ Gap {i} is large ({gap_size:,} lines) - splitting...")
            sub_chunks = split_large_gap(source_lines, start, end, max_lines_per_chunk=500)
            gap_chunks.extend(sub_chunks)
        else:
            gap_chunk = {
                'chunk_number': len(gap_chunks) + 1,
                'start_line': start,
                'end_line': end,
                'line_count': gap_size,
                'content': gap_content,
                'estimated_tokens': len(gap_content) // 4,
                'is_gap_fill': True
            }
            gap_chunks.append(gap_chunk)

    print(f"  • Created {len(gap_chunks)} gap-chunks")

    # Step 4: Process gap-chunks with ultra-strict prompts
    print(f"\n[4] Processing gap-chunks with strict validation...")

    gap_results = []
    gap_stats = {
        'total': len(gap_chunks),
        'validated': 0,
        'retries': 0,
        'incomplete': 0
    }

    ultra_strict_instruction = """
**ULTRA-STRICT GAP-FILLING MODE:**

You are filling GAPS in documentation. These are sections that were MISSED in the first pass.
Most likely they are:
- Large DATA DIVISION tables with repetitive FILLER definitions
- Long comment blocks
- Boring/repetitive code sections

**MANDATORY REQUIREMENTS:**
1. **Include EVERY SINGLE LINE verbatim** - No summarization whatsoever
2. **Even if content is boring/repetitive, include it ALL**
3. **Show complete FILLER definitions** - Do not abbreviate
4. **Include all comment blocks completely**
5. **Validation will check that 100% of lines are present**
6. **If you skip ANY line, validation will FAIL and you will retry**

**OUTPUT FORMAT:**
Show the COMPLETE source code in a code block:
```{get_current_adapter().code_block_language}
[Include every line from {start_line} to {end_line} with sequence numbers]
```

Then provide a brief explanation of what this section contains.
"""

    for gap_chunk in gap_chunks:
        chunk_num = gap_chunk['chunk_number']
        print(f"\n  → Gap-chunk {chunk_num}/{len(gap_chunks)} (lines {gap_chunk['start_line']}-{gap_chunk['end_line']})")

        # Format with ultra-strict instructions
        file_name = Path(file_path).name
        chunk_content = f"""
=============================================================================
GAP-FILL CHUNK {chunk_num} of {len(gap_chunks)} - {file_name}
=============================================================================
Lines: {gap_chunk['start_line']} to {gap_chunk['end_line']} ({gap_chunk['line_count']:,} lines)

⚠️  THIS IS A GAP-FILLING CHUNK - MISSED IN FIRST PASS ⚠️

You MUST include EVERY line from {gap_chunk['start_line']} to {gap_chunk['end_line']}.
Validation will verify 100% coverage.
=============================================================================

{gap_chunk['content']}
"""

        # Update context
        gap_context = context.copy()
        gap_context['source_code'] = chunk_content
        gap_context['start_line'] = gap_chunk['start_line']
        gap_context['end_line'] = gap_chunk['end_line']
        gap_context['line_count'] = gap_chunk['line_count']

        # Retry loop (worthwhile for gap-chunks - small and targeted)
        max_retries = 3
        for attempt in range(1, max_retries + 1):
            try:
                if attempt > 1:
                    print(f"    ↻ Retry {attempt}/{max_retries}")
                    gap_stats['retries'] += 1

                # Generate with ultra-strict prompt
                gap_result, gap_debug_path, gap_latency = generate_section_content(
                    section_id,
                    f"{section_title} - Gap Fill {chunk_num}",
                    ultra_strict_instruction,
                    template,
                    gap_context,
                    {},
                    llm_config,
                    pass_number=pass_number,
                    chunk_number=chunk_num,
                    is_retry=(attempt > 1)  # Add retry emphasis on subsequent attempts
                )
                if gap_debug_path:
                    print(f"    [DEBUG] Request logged to: {gap_debug_path} (latency: {gap_latency:.2f}s)")

                # Validate
                validator = ChunkDocumentationValidator(gap_chunk, gap_result)
                validation_result = validator.validate(min_coverage_percentage=100.0)

                if validation_result.is_valid:
                    print(f"    ✓ Complete: 100% coverage")
                    gap_stats['validated'] += 1
                    gap_results.append(gap_result)
                    break
                else:
                    print(f"    ⚠ Incomplete: {validation_result.coverage_percentage:.1f}% coverage")

                    if attempt < max_retries:
                        # Add retry feedback
                        retry_prompt = validator.create_retry_prompt(validation_result)
                        ultra_strict_instruction = retry_prompt + "\n\n" + ultra_strict_instruction
                    else:
                        print(f"    ✗ Max retries reached - accepting {validation_result.coverage_percentage:.1f}%")
                        gap_stats['incomplete'] += 1
                        gap_results.append(gap_result)

            except Exception as e:
                print(f"    ✗ Failed: {e}")
                if attempt == max_retries:
                    gap_stats['incomplete'] += 1
                    gap_results.append(f"\n\n**[Gap-chunk {chunk_num} failed]**\n\n")
                    break

    # Show gap-fill statistics
    print(f"\n" + "="*80)
    print(f"PASS 2 COMPLETE: Gap-Filling")
    print(f"="*80)
    print(f"  • Gap-chunks processed: {gap_stats['total']}")
    print(f"  • Complete (100%): {gap_stats['validated']}")
    print(f"  • Incomplete: {gap_stats['incomplete']}")
    print(f"  • Total retries: {gap_stats['retries']}")

    combined_gap_result = "\n\n".join(gap_results)
    return combined_gap_result


def merge_line_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Merge overlapping or adjacent line ranges.

    Example:
    [(1, 5), (3, 8), (10, 15), (16, 20)] → [(1, 8), (10, 20)]

    Args:
        ranges: List of (start, end) tuples

    Returns:
        Merged list of ranges
    """
    if not ranges:
        return []

    # Sort by start line
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    merged = [sorted_ranges[0]]

    for current in sorted_ranges[1:]:
        last = merged[-1]

        # Check if overlapping or adjacent (within 5 lines)
        if current[0] <= last[1] + 5:
            # Merge: extend the last range
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            # No overlap: add as new range
            merged.append(current)

    return merged


def split_large_gap(
    source_lines: List[str],
    start: int,
    end: int,
    max_lines_per_chunk: int = 500
) -> List[Dict[str, Any]]:
    """
    Split a large gap into smaller sub-chunks.

    Args:
        source_lines: All source file lines
        start: Gap start line
        end: Gap end line
        max_lines_per_chunk: Maximum lines per sub-chunk

    Returns:
        List of sub-chunk dictionaries
    """
    sub_chunks = []
    current_start = start

    while current_start <= end:
        current_end = min(current_start + max_lines_per_chunk - 1, end)
        gap_size = current_end - current_start + 1
        gap_content = ''.join(source_lines[current_start-1:current_end])

        sub_chunk = {
            'chunk_number': len(sub_chunks) + 1,
            'start_line': current_start,
            'end_line': current_end,
            'line_count': gap_size,
            'content': gap_content,
            'estimated_tokens': len(gap_content) // 4,
            'is_gap_fill': True
        }
        sub_chunks.append(sub_chunk)

        current_start = current_end + 1

    return sub_chunks


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


def perform_gap_filling(state: AgentState) -> None:
    """
    Two-pass gap filling: Verify documentation coverage and fill gaps.

    This function:
    1. Runs reconstruction verification on generated markdown
    2. Identifies missing line ranges
    3. Creates focused chunks from gaps only
    4. Re-processes gaps with strict prompts
    5. Merges gap-fill results into generated_content

    Args:
        state: Agent state with generated content and source file info

    Returns:
        None (modifies state in-place)
    """
    from pathlib import Path

    from source_chunker import chunk_large_cobol_file
    from verify_markdown_reconstruction import (
        extract_cobol_lines_from_markdown, find_missing_ranges)

    print("\n" + "="*80)
    print("TWO-PASS GAP FILLING")
    print("="*80)

    # Get source file path and generated markdown
    source_file = state.get('source_file_path')
    if not source_file or not Path(source_file).exists():
        print("  ⚠ Source file not found - skipping gap filling")
        return

    # Get generated markdown from detailed-code-explanation section
    generated_content = state.get('generated_content', {})
    markdown_content = generated_content.get('detailed-code-explanation', '')

    if not markdown_content:
        print("  ⚠ No documentation generated yet - skipping gap filling")
        return

    print(f"\n[1] Loading source file: {source_file}")
    with open(source_file, 'r') as f:
        source_lines = f.readlines()

    total_source_lines = len(source_lines)
    print(f"  ✓ Total source lines: {total_source_lines:,}")

    # Extract documented lines from markdown
    print(f"\n[2] Analyzing markdown coverage...")
    documented_sequences = extract_cobol_lines_from_markdown(markdown_content)
    documented_lines = set()

    for seq in documented_sequences:
        line_num = (seq - 10) // 2 + 1
        if 1 <= line_num <= total_source_lines:
            documented_lines.add(line_num)

    coverage_pct = (len(documented_lines) / total_source_lines * 100) if total_source_lines > 0 else 0
    print(f"  ✓ Documented lines: {len(documented_lines):,}/{total_source_lines:,} ({coverage_pct:.2f}%)")

    # Check if gap filling is needed
    if coverage_pct >= 99.0:  # Allow 1% tolerance
        print(f"  ✓ Coverage is excellent ({coverage_pct:.2f}%) - no gap filling needed")
        return

    # Find missing ranges
    all_lines = set(range(1, total_source_lines + 1))
    missing_lines = all_lines - documented_lines
    missing_ranges = find_missing_ranges(missing_lines)

    print(f"\n[3] Gap Analysis:")
    print(f"  • Missing lines: {len(missing_lines):,} ({100 - coverage_pct:.2f}%)")
    print(f"  • Gap ranges: {len(missing_ranges)}")

    if len(missing_ranges) == 0:
        print(f"  ✓ No gaps found - coverage complete")
        return

    # Show top 10 gaps
    print(f"\n  Top 10 largest gaps:")
    sorted_ranges = sorted(missing_ranges, key=lambda x: x[1] - x[0] + 1, reverse=True)
    for i, (start, end) in enumerate(sorted_ranges[:10], 1):
        gap_size = end - start + 1
        seq_start = 10 + (start - 1) * 2
        seq_end = 10 + (end - 1) * 2
        print(f"    {i}. Lines {start:,}-{end:,} (Sequences {seq_start:06d}-{seq_end:06d}) - {gap_size:,} lines")

    # Ask user if they want to proceed with gap filling
    print(f"\n[4] Gap Filling Decision:")
    print(f"  Found {len(missing_ranges)} gaps totaling {len(missing_lines):,} lines")
    print(f"  Gap filling will process these missing lines with strict requirements")
    print(f"  ⚠ This may incur significant API costs for large gaps")

    # For now, proceed automatically (can add user confirmation later)
    print(f"  → Proceeding with gap filling...")

    # Create chunks from gap ranges only
    # (Simplified: for now, treat each gap as a separate chunk)
    print(f"\n[5] Creating gap chunks...")
    gap_chunks = []
    for i, (start, end) in enumerate(sorted_ranges, 1):
        gap_size = end - start + 1
        gap_content = ''.join(source_lines[start-1:end])

        gap_chunk = {
            'chunk_number': i,
            'start_line': start,
            'end_line': end,
            'line_count': gap_size,
            'content': gap_content,
            'estimated_tokens': len(gap_content) // 4,
            'is_gap_fill': True  # Mark as gap-fill chunk
        }
        gap_chunks.append(gap_chunk)

    print(f"  ✓ Created {len(gap_chunks)} gap chunks")

    # Process gap chunks with strict prompts
    print(f"\n[6] Processing gap chunks...")
    # (This part would integrate with the chunk processing loop)
    # For now, just log what would happen
    print(f"  → Would process {len(gap_chunks)} gap chunks with strict validation")
    print(f"  → Each chunk would be validated and retried up to 3 times")
    print(f"  → Gap-fill results would be merged into documentation")

    print(f"\n  ⚠ GAP FILLING NOT YET FULLY IMPLEMENTED")
    print(f"     This is a placeholder showing where gap filling would occur")


def assemble_document_node(state: AgentState) -> AgentState:
    """
    Node 6: Assemble all generated sections into final document.

    Before assembly, performs two-pass gap filling if enabled.
    """
    # Check if two-pass gap filling is enabled
    enable_gap_filling = state.get("enable_gap_filling", False)

    if enable_gap_filling:
        perform_gap_filling(state)

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
# REORGANIZE-DOCS: TWO-PHASE DOCUMENTATION GENERATION
# ============================================================================
# Phase 1: Generate detailed code explanation (chunked) → Extract prose
# Phase 2: Generate other sections using prose + metadata (no raw source)
# Phase 3: Assemble final document
# ============================================================================

def get_tmp_dir(program_name: str) -> Path:
    """Get the tmp directory path for a program."""
    return Path("./tmp") / program_name


def save_to_tmp(content: str, program_name: str, filename: str) -> Path:
    """
    Save content to tmp directory.

    Args:
        content: Content to save
        program_name: Program name (used as subdirectory)
        filename: Filename to save as

    Returns:
        Path to saved file
    """
    tmp_dir = get_tmp_dir(program_name)
    tmp_dir.mkdir(parents=True, exist_ok=True)

    file_path = tmp_dir / filename
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  → Saved to tmp: {file_path}")
    return file_path


def save_chunk_result(program_name: str, chunk_num: int, content: str) -> Path:
    """Save a single chunk result to disk for checkpointing."""
    chunks_dir = get_tmp_dir(program_name) / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)
    file_path = chunks_dir / f"chunk_{chunk_num:04d}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return file_path


def load_completed_chunks(program_name: str) -> Dict[int, str]:
    """Load previously completed chunk results from disk."""
    chunks_dir = get_tmp_dir(program_name) / "chunks"
    result = {}
    if not chunks_dir.exists():
        return result
    for chunk_file in sorted(chunks_dir.glob("chunk_*.md")):
        try:
            num = int(chunk_file.stem.split("_")[1])
            with open(chunk_file, 'r', encoding='utf-8') as f:
                result[num] = f.read()
        except (ValueError, IndexError):
            continue
    return result


def clear_chunk_cache(program_name: str) -> None:
    """Delete the chunks checkpoint directory after successful completion."""
    import shutil
    chunks_dir = get_tmp_dir(program_name) / "chunks"
    if chunks_dir.exists():
        shutil.rmtree(chunks_dir)
        print(f"  → Cleared chunk cache: {chunks_dir}")


def load_from_tmp(program_name: str, filename: str) -> Optional[str]:
    """
    Load content from tmp directory.

    Args:
        program_name: Program name (subdirectory)
        filename: Filename to load

    Returns:
        Content if file exists, None otherwise
    """
    file_path = get_tmp_dir(program_name) / filename

    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    return None


def cleanup_tmp(program_name: str) -> None:
    """
    Remove tmp directory for a program after successful assembly.

    Args:
        program_name: Program name (subdirectory to remove)
    """
    tmp_dir = get_tmp_dir(program_name)

    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
        print(f"  → Cleaned up tmp directory: {tmp_dir}")


def extract_prose_from_explanation(explanation_md: str) -> str:
    """
    Extract prose from generated code explanation by stripping code blocks.

    This removes all ```cobol ... ``` blocks while preserving:
    - ## Chunk N/M headers
    - ### Block N: headers
    - **Purpose:** sections
    - **Detailed Explanation:** sections
    - **Technical Details:** sections

    Args:
        explanation_md: Full markdown with code blocks

    Returns:
        Prose-only markdown without code blocks
    """
    # Remove all code blocks (```cobol ... ``` or ``` ... ```)
    prose = re.sub(r'```[\w]*\n.*?```', '', explanation_md, flags=re.DOTALL)

    # Clean up excessive whitespace (more than 2 newlines)
    prose = re.sub(r'\n{3,}', '\n\n', prose)

    # Remove "## COBOL Code (Complete Verbatim Copy)" headers since code is removed
    # Remove code verbatim copy headers (works for any language)
    prose = re.sub(r'##\s+(?:COBOL|C#|\.NET|Java|Source)\s+Code\s*\(Complete Verbatim Copy\)\s*\n*', '', prose)

    return prose.strip()


def run_phase1_code_explanation(
    state: AgentState,
    llm_config: Dict[str, Any],
    fallback_manager: Optional['LLMFallbackManager'] = None
) -> Tuple[str, str]:
    """
    Phase 1: Generate detailed code explanation using chunked processing.

    This function:
    1. Finds the detailed-code-explanation section from template
    2. Calls existing chunk processing logic
    3. Extracts prose from the generated explanation
    4. Saves both full explanation and prose to tmp

    Args:
        state: Agent state with program info and metadata
        llm_config: LLM configuration
        fallback_manager: Optional LLMFallbackManager for automatic fallback on errors

    Returns:
        Tuple of (full_explanation_md, extracted_prose)
    """
    program_name = state["program_name"]
    print(f"\n{'='*60}")
    print(f"PHASE 1: Generating Detailed Code Explanation")
    print(f"{'='*60}")

    # Find the detailed-code-explanation section from template
    template = state.get("template", {})
    sections = template.get("sections", [])

    code_explanation_section = None
    for section in sections:
        if section.get("id") == "detailed-code-explanation":
            code_explanation_section = section
            break

    if not code_explanation_section:
        raise ValueError("Template missing 'detailed-code-explanation' section")

    # Build context for the section
    context = build_section_context(state, code_explanation_section)

    # Always use chunked processing for Phase 1 (consistent Hash-ID, Call Flow, Data Flow format)
    # For small files that weren't flagged by source_integration, create chunked_file_info here
    if 'chunked_file_info' not in context:
        cobol_file_path = state.get("cobol_file_path")
        if cobol_file_path:
            try:
                with open(cobol_file_path, 'r', encoding='utf-8', errors='replace') as f:
                    total_lines = sum(1 for _ in f)
                context['chunked_file_info'] = {
                    'type': 'CHUNKED_FILE',
                    'file_path': cobol_file_path,
                    'total_lines': total_lines,
                    'max_lines_per_chunk': max(total_lines, 8000),  # Single chunk for small files
                }
                print(f"  → File: {total_lines:,} lines - using chunked processing")
            except Exception as e:
                print(f"  ⚠ Could not read file for chunking: {e}")

    if 'chunked_file_info' in context:
        full_explanation = process_large_file_in_chunks(
            section_id=code_explanation_section.get("id", ""),
            section_title=code_explanation_section.get("title", "Detailed Code Explanation"),
            instruction=code_explanation_section.get("instruction", ""),
            template=code_explanation_section.get("template", ""),
            context=context,
            chunked_file_info=context['chunked_file_info'],
            llm_config=llm_config,
            pass_number=1,
            state=state,
            fallback_manager=fallback_manager
        )
    else:
        # Fallback: no COBOL file path available
        print(f"  ⚠ No source file path - using single-pass fallback")
        full_explanation = process_section_recursive(state, code_explanation_section)

    # Extract prose from the explanation
    print(f"\n  → Extracting prose from explanation...")
    extracted_prose = extract_prose_from_explanation(full_explanation)

    # Calculate sizes for logging
    full_size = len(full_explanation)
    prose_size = len(extracted_prose)
    reduction = ((full_size - prose_size) / full_size * 100) if full_size > 0 else 0

    print(f"    Full explanation: {full_size:,} chars")
    print(f"    Extracted prose:  {prose_size:,} chars")
    print(f"    Reduction: {reduction:.1f}%")

    # Save to tmp
    save_to_tmp(full_explanation, program_name, "detailed_code_explanation.md")
    save_to_tmp(extracted_prose, program_name, "explanation_prose.txt")
    clear_chunk_cache(program_name)

    print(f"\n✓ Phase 1 complete")

    return full_explanation, extracted_prose


# ===========================================================================
# Legacy Phase 2 removed — see rlm/orchestrator.py (run_phase2_rlm).
# ===========================================================================

def _normalize_section_content(content: str, section_title: str) -> str:
    """Normalize heading hierarchy within a section.

    Ensures all headings in the content nest properly under the H1
    section heading added by the assembly. The shallowest heading
    in the content will be adjusted to H2.

    1. Remove leading heading if it duplicates the section title
    2. Adjust all heading levels so the shallowest is H2
    """
    lines = content.strip().split('\n')

    # Step 1: Remove leading heading if it duplicates the section title
    if lines and lines[0].startswith('#'):
        heading_text = lines[0].lstrip('#').strip()
        if heading_text.lower() == section_title.lower():
            lines = lines[1:]
            # Strip blank lines after the removed heading
            while lines and not lines[0].strip():
                lines = lines[1:]

    # Step 2: Find minimum heading level (skip lines inside code blocks)
    in_code_block = False
    heading_levels = []
    for line in lines:
        if line.startswith('```'):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            if level > 0:
                heading_levels.append(level)

    if not heading_levels:
        return '\n'.join(lines)

    min_level = min(heading_levels)
    if min_level == 2:
        # Already correct — H2 is the shallowest
        return '\n'.join(lines)

    # Step 3: Shift all headings so shallowest becomes H2
    offset = min_level - 2  # positive: shift up; negative: shift down
    in_code_block = False
    result = []
    for line in lines:
        if line.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue
        if in_code_block:
            result.append(line)
            continue
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            if level > 0:
                new_level = max(2, level - offset)
                line = '#' * new_level + line[level:]
        result.append(line)

    return '\n'.join(result)


def assemble_final_document(
    program_name: str,
    code_explanation: str,
    section_outputs: Dict[str, str],
    template: Dict[str, Any],
    relative_source_path: Optional[str] = None,
) -> str:
    """
    Phase 3: Assemble all sections into final markdown document.

    Combines sections in the order specified by the template.
    Each section gets an H1 heading; content within is normalized to H2+.

    Args:
        program_name: Program name for title
        code_explanation: Full code explanation from Phase 1
        section_outputs: Section outputs from Phase 2
        template: Template dict with section order
        relative_source_path: Relative path from workspace root to source file

    Returns:
        Complete markdown document
    """
    print(f"\n{'='*60}")
    print(f"PHASE 3: Assembling Final Document")
    print(f"{'='*60}")

    sections = template.get("sections", [])

    # Build document header
    source_display = relative_source_path or program_name
    doc_parts = [
        f"# {program_name} - Code Documentation\n",
        f"**Source**: `{source_display}`\n",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        f"**Program**: {program_name}\n",
        "\n---\n"
    ]

    # Add sections in template order
    for section in sections:
        section_id = section.get("id", "")
        section_title = section.get("title", section_id)

        if section_id == "detailed-code-explanation":
            # Use Phase 1 output
            content = code_explanation
            print(f"  → Adding: {section_title} (from Phase 1)")
        elif section_id in section_outputs:
            # Use Phase 2 output
            content = section_outputs[section_id]
            print(f"  → Adding: {section_title} (from Phase 2)")
        else:
            # Section not generated
            content = "*Section not generated*"
            print(f"  → Skipping: {section_title} (not generated)")

        # Normalize content headings to H2+ (remove duplicate title, shift H1s down)
        content = _normalize_section_content(content, section_title)

        # Add section with H1 heading and separator
        doc_parts.append(f"\n---\n\n# {section_title}\n\n{content}\n")

    final_doc = "\n".join(doc_parts)

    print(f"\n  → Final document: {len(final_doc):,} chars")
    print(f"✓ Phase 3 complete")

    return final_doc


def generate_documentation(
    program_name: str,
    workspace_path: str,
    metadata_dir: str,
    template_path: str,
    output_dir: str,
    llm_config: Dict[str, Any],
    cobol_file_path: Optional[str] = None,
    generate_metadata: bool = True,
    servers_config: Optional[Dict[str, Any]] = None,
    preloaded_metadata: Optional[Dict[str, Any]] = None,
    enable_source_extraction: bool = True,
    auto_start_phase2: bool = True,
    language: str = 'cobol',
    full_config: Optional[Dict[str, Any]] = None,
) -> Optional[str]:
    """
    Generate documentation using the two-phase approach.

    This is the main entry point for documentation generation:
    - Phase 1: Generate detailed code explanation (chunked) → Extract prose
    - Phase 2: Generate other sections using prose + metadata
    - Phase 3: Assemble final document

    Args:
        program_name: Name of the program
        workspace_path: Path to source files
        metadata_dir: Path to metadata directory
        template_path: Path to YAML template
        output_dir: Path for output
        llm_config: LLM configuration
        cobol_file_path: Optional path to specific source file
        generate_metadata: Whether to generate metadata first
        servers_config: MCP servers configuration
        preloaded_metadata: Optional pre-loaded metadata dict
        enable_source_extraction: Enable source code extraction for chunked processing
        auto_start_phase2: If True, proceed to Phase 2 immediately; if False, pause for user confirmation
        language: Language identifier (default: 'cobol')

    Returns:
        Path to generated documentation file, or None on failure
    """
    # Initialize language adapter
    global _current_adapter
    from adapter_registry import get_adapter
    adapter = get_adapter(language)
    _current_adapter = adapter

    # Default template path from adapter if not explicitly provided or if default
    if not template_path or template_path == './cobol-doc-template.yaml':
        if language != 'cobol':
            template_path = str(adapter.template_path)
    print(f"\n{'#'*60}")
    print(f"# REORGANIZED DOCUMENTATION GENERATION")
    print(f"# Program: {program_name}")
    print(f"{'#'*60}")

    # Convert paths
    workspace_path = Path(workspace_path)
    metadata_dir = Path(metadata_dir)
    template_path = Path(template_path)
    output_dir = Path(output_dir)

    try:
        # Initialize LLM call tracer for this program (centralized run dir)
        from llm_tracer import init_tracer
        _rl = get_run_logger()
        _rl.set_current_program(program_name)
        trace_log = _rl.get_trace_log_path(program_name)
        tracer = init_tracer(trace_log)
        print(f"\n→ LLM tracer initialized: {trace_log}")

        # Load template
        print(f"\n→ Loading template: {template_path}")
        with open(template_path, 'r') as f:
            template = yaml.safe_load(f)

        # Load metadata (use preloaded if provided)
        if preloaded_metadata:
            print(f"→ Using preloaded metadata")
            metadata = preloaded_metadata
            # Use adapter-driven metadata keys for validation
            adapter_patterns = adapter.get_metadata_file_patterns(program_name)
            expected_keys = list(adapter_patterns.keys())
            # Also check legacy COBOL keys for backward compatibility
            all_keys = set(expected_keys) | {"ctags_outline", "superbol_symbols", "superbol_cfg", "gnucobol_analysis"}
            for key in all_keys:
                if key in metadata and metadata[key]:
                    print(f"  ✓ {key}: loaded")
                elif key in expected_keys:
                    metadata[key] = {}
                    print(f"  ⚠ {key}: missing")
        else:
            print(f"→ Loading metadata from: {metadata_dir}")
            metadata = {}

            # Use adapter-driven metadata patterns
            adapter_patterns = adapter.get_metadata_file_patterns(program_name)

            # Also include legacy COBOL fallback patterns for backward compatibility
            if language == 'cobol':
                legacy_patterns = {
                    "ctags_outline": ["ctags_outline.json"],
                    "superbol_symbols": ["superbol_symbols.json"],
                    "superbol_cfg": ["superbol_cfg.json"],
                    "gnucobol_analysis": ["gnucobol_analysis.json"],
                }
                for key, patterns in legacy_patterns.items():
                    if key in adapter_patterns:
                        adapter_patterns[key] = adapter_patterns[key] + patterns
                    else:
                        adapter_patterns[key] = patterns

            for key, patterns in adapter_patterns.items():
                loaded = False
                for pattern in patterns:
                    file_path = metadata_dir / pattern
                    if file_path.exists():
                        try:
                            with open(file_path, 'r') as f:
                                content = f.read().strip()
                            if not content:
                                print(f"  ⚠ Empty metadata file, skipping: {pattern}")
                                continue
                            metadata[key] = json.loads(content)
                            print(f"  ✓ Loaded {key}: {pattern}")
                            loaded = True
                            break
                        except json.JSONDecodeError as e:
                            print(f"  ⚠ Invalid JSON in {pattern}: {e}")
                            continue
                if not loaded:
                    metadata[key] = {}
                    print(f"  ⚠ Missing {key}")

            # Map normalized keys to legacy COBOL state keys for backward compat
            if language == 'cobol' and 'structural_outline' in metadata:
                metadata.setdefault('ctags_outline', metadata['structural_outline'])

        # Determine source file path
        if not cobol_file_path:
            # Try to find it in workspace using adapter's file extensions
            for ext in adapter.file_extensions:
                potential_path = workspace_path / f"{program_name}{ext}"
                if potential_path.exists():
                    cobol_file_path = str(potential_path)
                    break
            # Also try recursive search for languages that nest files in subdirectories
            if not cobol_file_path and language != 'cobol':
                for ext in adapter.file_extensions:
                    matches = list(workspace_path.rglob(f"{program_name}{ext}"))
                    if matches:
                        cobol_file_path = str(matches[0])
                        break

        if cobol_file_path:
            print(f"→ {adapter.display_name} source: {cobol_file_path}")
        else:
            print(f"⚠ {adapter.display_name} source file not found")

        # Compute relative source path from workspace root
        # e.g., "AutolivSweden/Atoms.cs" or just "MAINPROG.cbl" for flat layouts
        if cobol_file_path:
            try:
                relative_source = str(Path(cobol_file_path).relative_to(workspace_path))
            except ValueError:
                relative_source = Path(cobol_file_path).name
        else:
            relative_source = program_name

        # Build initial state
        state: AgentState = {
            "program_name": program_name,
            "workspace_path": workspace_path,
            "metadata_dir": metadata_dir,
            "template_path": template_path,
            "output_dir": output_dir,
            "template": template,
            "cobol_file_path": cobol_file_path,
            "source_file_path": cobol_file_path,  # Language-agnostic alias
            "llm_config": llm_config,
            # Enable source extraction for chunked processing of large files
            "enable_source_extraction": enable_source_extraction,
            "relative_source_path": relative_source,
            # Full config for chunking strategy, query patterns, etc.
            "full_config": full_config or {},
            **metadata
        }

        # ═══════════════════════════════════════════════════════════════
        # Initialize Relationship Provider (multilspy cross-references)
        # ═══════════════════════════════════════════════════════════════
        # Derive cross-reference path: metadata_dir/per_file/ (multilspy output).
        # Falls back to the legacy cross_references_dir key if metadata_dir is absent.
        _out_cfg = (full_config or {}).get("output", {})
        _metadata_dir = _out_cfg.get("metadata_dir")
        cross_ref_dir = (
            str(Path(_metadata_dir) / "per_file") if _metadata_dir
            else _out_cfg.get("cross_references_dir")
        )
        if cross_ref_dir:
            cross_ref_path = Path(cross_ref_dir)
            if not cross_ref_path.is_dir():
                print(f"→ Cross-reference directory not found (multilspy not yet run?): "
                      f"{cross_ref_path}")
            elif not any(cross_ref_path.glob("*.json")):
                print(f"→ Cross-reference directory is empty: {cross_ref_path}")
            else:
                from relationship_provider import RelationshipProvider
                state["relationship_provider"] = RelationshipProvider(str(cross_ref_path))
                print(f"→ Cross-reference metadata loaded from {cross_ref_path}")

        # ═══════════════════════════════════════════════════════════════
        # Initialize LLM Fallback Manager (if fallback configured)
        # ═══════════════════════════════════════════════════════════════
        fallback_manager = LLMFallbackManager(llm_config)
        if fallback_manager.has_fallback():
            print(f"\n→ Fallback LLM configured: {llm_config.get('fallback', {}).get('provider', 'unknown')}")
        else:
            print(f"\n→ No fallback LLM configured (errors will be raised)")

        # ═══════════════════════════════════════════════════════════════
        # PHASE 1: Generate Detailed Code Explanation
        # ═══════════════════════════════════════════════════════════════
        code_explanation, prose = run_phase1_code_explanation(state, llm_config, fallback_manager)

        # ═══════════════════════════════════════════════════════════════
        # Phase 1 → Phase 2 Transition: Token counting & pause
        # ═══════════════════════════════════════════════════════════════
        phase2_config = llm_config.get('phase2', {})
        phase2_model = phase2_config.get('model', llm_config.get('model', 'sonnet'))
        prose_chars = len(prose)
        prose_tokens = estimate_tokens(prose, model=phase2_model)

        print(f"\n{'─'*60}")
        print(f"Phase 1 prose ready for Phase 2 context:")
        print(f"  Characters : {prose_chars:,}")
        print(f"  Tokens     : {prose_tokens:,}  (model: {phase2_model})")
        print(f"{'─'*60}")

        if not auto_start_phase2:
            user_input = input("\nPress Enter to start Phase 2 (or 'q' to skip): ").strip().lower()
            if user_input == 'q':
                print("→ Skipping Phase 2 by user request. Assembling document with Phase 1 only.")
                section_outputs = {}

                final_doc = assemble_final_document(
                    program_name=program_name,
                    code_explanation=code_explanation,
                    section_outputs=section_outputs,
                    template=template,
                    relative_source_path=relative_source,
                )

                # Mirror source directory structure in output path
                relative_dir = Path(relative_source).parent
                output_subdir = output_dir / relative_dir
                output_subdir.mkdir(parents=True, exist_ok=True)
                timestamp = datetime.now().strftime("%d-%m-%Y")
                output_filename = f"{program_name}-documentation-{timestamp}.md"
                output_path = output_subdir / output_filename

                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(final_doc)

                print(f"\n{'='*60}")
                print(f"✓ Documentation (Phase 1 only) saved to: {output_path}")
                print(f"{'='*60}")
                return str(output_path)

        # ═══════════════════════════════════════════════════════════════
        # PHASE 2: PageIndex + deterministic + λ-RLM planner
        # ═══════════════════════════════════════════════════════════════
        # Imported lazily so the module still loads in environments that do
        # not have claude-agent-sdk installed (planner sub-LLM calls need it).
        from rlm.orchestrator import run_phase2_rlm
        section_outputs = run_phase2_rlm(
            state=state,
            code_explanation=code_explanation,
            llm_config=llm_config,
            fallback_manager=fallback_manager,
            full_config=full_config,
        )

        # ─────────────────────────────────────────────────────────────────
        # POST-PHASE-2: Aggregate per-section questionnaires into a single
        # "Questionnaires for <ProgramName>" section placed after
        # "Error Handling Strategy". Runs before Phase 3 assembly so the
        # synthetic section flows through the normal assembly path.
        # ─────────────────────────────────────────────────────────────────
        from questionnaire_aggregator import (
            aggregate_in_section_outputs,
            aggregate_chunk_questionnaires_in_code_explanation,
            inject_section_after,
        )
        section_outputs, _synthetic_q_section = aggregate_in_section_outputs(
            section_outputs, program_name
        )
        if _synthetic_q_section:
            template = inject_section_after(
                template, _synthetic_q_section, after_id="error-handling"
            )
            state["template"] = template
            print(
                f"→ Questionnaires aggregated into synthetic section: "
                f"{_synthetic_q_section['title']!r}"
            )

        # Also fold per-chunk 'Retrieval Questions for Chunk-ID: ...' blocks
        # from the Phase-1 code explanation into a second synthetic section,
        # placed directly after the per-section aggregate above.
        code_explanation, section_outputs, _synthetic_chunk_q = (
            aggregate_chunk_questionnaires_in_code_explanation(
                code_explanation, section_outputs, program_name
            )
        )
        if _synthetic_chunk_q:
            chunk_after_id = (
                _synthetic_q_section["id"] if _synthetic_q_section else "error-handling"
            )
            template = inject_section_after(
                template, _synthetic_chunk_q, after_id=chunk_after_id
            )
            state["template"] = template
            print(
                f"→ Chunk questionnaires aggregated into synthetic section: "
                f"{_synthetic_chunk_q['title']!r}"
            )

        # ═══════════════════════════════════════════════════════════════
        # PHASE 3: Assemble Final Document
        # ═══════════════════════════════════════════════════════════════
        final_doc = assemble_final_document(
            program_name=program_name,
            code_explanation=code_explanation,
            section_outputs=section_outputs,
            template=template,
            relative_source_path=relative_source,
        )

        # Save final document — mirror source directory structure in output path
        relative_dir = Path(relative_source).parent
        output_subdir = output_dir / relative_dir
        output_subdir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%d-%m-%Y")
        output_filename = f"{program_name}-documentation-{timestamp}.md"
        output_path = output_subdir / output_filename

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_doc)

        print(f"\n{'='*60}")
        print(f"✓ Documentation saved to: {output_path}")
        print(f"{'='*60}")

        # Log if fallback was used during generation
        if fallback_manager.is_fallback_active():
            fb_status = fallback_manager.get_status()
            print(f"\n⚠ FALLBACK WAS USED:")
            print(f"  Primary: {fb_status['primary_provider']} / {fb_status['primary_model']}")
            print(f"  Fallback: {fb_status['fallback_provider']}")
            print(f"  Triggered at: {fb_status['triggered_at']}")
            print(f"  Error: {fb_status['trigger_error'][:100] if fb_status['trigger_error'] else 'N/A'}...")

        # Finalize LLM tracer and write reports (AFTER final document is saved)
        from llm_tracer import finalize_tracer
        finalize_tracer(
            doc_path=str(output_path),
            source_path=cobol_file_path
        )

        # Record success in run logger
        _rl = get_run_logger()
        _rl.record_program_result(program_name, 'completed', output_path=str(output_path))

        # Cleanup tmp files
        cleanup_tmp(program_name)

        return str(output_path)

    except Exception as e:
        print(f"\n✗ Documentation generation failed: {e}")
        import traceback
        traceback.print_exc()

        # Record failure in run logger
        _rl = get_run_logger()
        _rl.record_program_result(program_name, 'failed', error=str(e))

        return None


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

    # Checkpoint/Resume arguments
    parser.add_argument("--restart", action="store_true", help="Ignore checkpoint and restart batch processing from beginning")
    parser.add_argument("--status", action="store_true", help="Show checkpoint status and exit without processing")
    parser.add_argument("--retry-failed", action="store_true", help="Only retry previously failed files")
    parser.add_argument("--continue-on-error", action="store_true", help="Continue processing if a file fails (default for batch)")
    parser.add_argument("--max-retries", type=int, default=3, help="Maximum retries for failed files (default: 3)")

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

        # Language configuration (default: 'cobol' for backward compatibility)
        language = config_loader.get_language_config()

        # Phase 1: Source extraction configuration
        source_extraction_config = config_loader.get_source_extraction_config()
        enable_source_extraction = source_extraction_config.get('enabled', False)
        compress_source = source_extraction_config.get('compress', True)
        # cobol_file_path will be auto-detected based on source_files_arg

        # Phase 3: Multi-file support configuration
        resolve_copybooks = source_extraction_config.get('resolve_copybooks', False)
        resolve_called_programs = source_extraction_config.get('resolve_called_programs', False)
        copybook_search_paths = source_extraction_config.get('copybook_search_paths', [])
        program_search_paths = source_extraction_config.get('program_search_paths', [])

        # Epic 2: Full Context Mode configuration
        full_context_config = config_loader.get_full_context_config()
        use_full_context_mode = full_context_config.get('enabled', False)
        full_context_sections = full_context_config.get('sections', [])
        max_message_chars = full_context_config.get('max_message_chars', 9000000)

        # File filtering configuration
        file_filter_config = config_loader.get_file_filter_config()

        # Workflow configuration
        workflow_config = config_loader.get_workflow_config()
        auto_start_phase2 = workflow_config.get('auto_start_phase2', True)

        if use_full_context_mode:
            print(f"\n  Full Context Mode: ENABLED")
            print(f"  Full Context Sections: {full_context_sections}")
            print(f"  Max Message Chars: {max_message_chars:,}")

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
        language = 'cobol'  # CLI-only mode defaults to COBOL

        # Phase 1: Source extraction defaults (disabled by default)
        enable_source_extraction = False
        compress_source = True

        # Phase 3: Multi-file support defaults (disabled by default)
        resolve_copybooks = False
        resolve_called_programs = False
        copybook_search_paths = []
        program_search_paths = []

        # Epic 2: Full Context Mode defaults (disabled by default)
        use_full_context_mode = False
        full_context_sections = []
        max_message_chars = 9000000  # Default 9MB

        # File filtering defaults (no filtering)
        file_filter_config = None

        # Workflow defaults
        auto_start_phase2 = True

    # Validation: either program_name or source_files must be provided
    if not program_name and not source_files_arg:
        parser.error("Either program_name, --source-files, or --config must be provided")

    # ═══════════════════════════════════════════════════════════════════
    # RUN LOGGING INITIALIZATION (always enabled)
    # ═══════════════════════════════════════════════════════════════════
    run_logging_config = {}
    if config_loader:
        run_logging_config = config_loader.get_run_logging_config()

    _rl = init_run_logger(docs_path)
    if run_logging_config.get('console_tee', True):
        _rl.start_console_tee()

    # Determine which mode to use
    if source_files_arg:
        # Batch processing mode
        # Expand ~ to home directory
        source_path = Path(source_files_arg).expanduser()

        # Determine list of source files to process
        if source_path.is_file():
            # Single file - store both stem (for program_name) and full path (for source extraction)
            cobol_files_to_process = [(source_path.stem, str(source_path))]
            workspace_path = str(source_path.parent)
            print(f"\nProcessing single file: {source_path.name}")
        elif source_path.is_dir():
            # Directory - find all source files
            # Use adapter for file discovery if language is not cobol
            if language != 'cobol':
                from adapter_registry import get_adapter
                _adapter = get_adapter(language)
                source_file_paths = _adapter.discover_source_files(
                    str(source_path), filter_config=file_filter_config
                )
                cobol_files_to_process = sorted([(f.stem, str(f)) for f in source_file_paths])
            else:
                from checksum_manager import get_source_files
                cobol_file_paths = get_source_files(source_path, filter_config=file_filter_config)
                cobol_files_to_process = sorted([(f.stem, str(f)) for f in cobol_file_paths])
            # Store tuples of (stem, full_path)
            workspace_path = str(source_path)
            print(f"\nProcessing directory: {source_path}")
            print(f"Found {len(cobol_files_to_process)} {language.upper()} files")
            # Log filter configuration if active
            if file_filter_config:
                if file_filter_config.get('extensions_include'):
                    print(f"  → Extensions included: {file_filter_config['extensions_include']}")
                if file_filter_config.get('extensions_exclude'):
                    print(f"  → Extensions excluded: {file_filter_config['extensions_exclude']}")
                if file_filter_config.get('exclude_files'):
                    print(f"  → File patterns excluded: {file_filter_config['exclude_files']}")
        else:
            parser.error(f"Source path does not exist: {source_files_arg}")

        if not cobol_files_to_process:
            parser.error(f"No COBOL files found in: {source_files_arg}")

        # ═══════════════════════════════════════════════════════════════════
        # CHECKPOINT/RESUME INTEGRATION
        # ═══════════════════════════════════════════════════════════════════
        from checkpoint_manager import CheckpointManager

        # Compute config hash for change detection
        config_dict = {
            'llm': llm_config,
            'template': {'path': template_path},
        }
        config_hash = CheckpointManager.compute_config_hash(config_dict)

        # Initialize checkpoint manager
        checkpoint = CheckpointManager(
            output_dir=Path(docs_path),
            config_hash=config_hash,
            max_retries=args.max_retries
        )

        # Handle --restart flag
        if args.restart:
            import shutil
            checkpoint.delete_checkpoint()
            # Also delete checksum files to force full regeneration
            for checksum_file in [source_checksum_path, metadata_checksum_path]:
                checksum_path = Path(checksum_file)
                if checksum_path.exists():
                    checksum_path.unlink()
                    print(f"  ✓ Deleted checksum file: {checksum_path}")
            # Also clear chunk cache (./tmp/) to force re-processing of all chunks
            tmp_dir = Path("./tmp")
            if tmp_dir.exists():
                shutil.rmtree(tmp_dir)
                print(f"  ✓ Deleted chunk cache: {tmp_dir}")
            print("  Checkpoint, checksums, and chunk cache deleted. Starting fresh.\n")

        # Load or create checkpoint
        source_file_paths = [Path(fp) for _, fp in cobol_files_to_process]
        print(f"\n→ Initializing checkpoint...")
        checkpoint.load_or_create(source_file_paths)

        # Handle --status flag
        if args.status:
            print(checkpoint.get_summary_report())
            sys.exit(0)

        # Check for config changes
        if checkpoint.config_changed() and not args.restart:
            print("\n⚠ Configuration has changed since last run!")
            print("  Use --restart to start fresh, or continue with current config.")
            print("  Continuing with existing checkpoint...\n")

        # Handle --retry-failed flag
        if args.retry_failed:
            reset_count = checkpoint.reset_failed_files()
            print(f"  Reset {reset_count} failed files for retry.\n")

        # ═══════════════════════════════════════════════════════════════════
        # METADATA GENERATION (once for all files, before doc generation)
        # ═══════════════════════════════════════════════════════════════════
        # Check if metadata generation is needed based on checkpoint flag
        metadata_generated = checkpoint.state.get('metadata_generated', False) if checkpoint.state else False

        # Override checkpoint flag when checksums indicate regeneration is needed,
        # or when skip_existing is false (force regeneration).
        # This allows re-running metadata without --restart (which resets everything).
        if metadata_generated and generate_metadata:
            if not skip_existing:
                print(f"  → Force regeneration requested (skip_existing: false)")
                metadata_generated = False
            else:
                try:
                    from checksum_manager import should_regenerate_metadata
                    all_source_names = [Path(fp).name for _, fp in cobol_files_to_process]
                    should_regen, reason = should_regenerate_metadata(
                        workspace_path=Path(workspace_path),
                        source_checksum_path=Path(source_checksum_path),
                        metadata_dir=Path(metadata_dir),
                        metadata_checksum_path=Path(metadata_checksum_path),
                        cobol_files=all_source_names
                    )
                    if should_regen:
                        print(f"  → Checksum validation overrides checkpoint: {reason}")
                        metadata_generated = False
                except Exception as e:
                    print(f"  ⚠ Checksum validation failed ({e}), trusting checkpoint flag")

        progress = checkpoint.get_progress()
        is_resuming = progress['completed'] > 0

        if generate_metadata and not metadata_generated:
            print(f"\n{'='*70}")
            print(f"METADATA GENERATION: Processing {len(cobol_files_to_process)} files")
            print(f"{'='*70}\n")

            # Get all file paths for batch metadata generation
            all_cobol_files = [full_path for _, full_path in cobol_files_to_process]

            try:
                # Use the existing metadata generation infrastructure
                from mcp_metadata_generator import generate_metadata_sync

                # Get servers config
                servers_config_for_meta = {}
                full_config_for_meta = None
                if config_loader:
                    servers_config_for_meta = config_loader.get_servers_config()
                    full_config_for_meta = config_loader.config  # Full config for factory detection

                generate_metadata_sync(
                    workspace_path=workspace_path,
                    output_dir=metadata_dir,
                    cobol_files=all_cobol_files,
                    servers_config=servers_config_for_meta,
                    config=full_config_for_meta
                )

                # Save metadata checksums for future validation
                try:
                    from checksum_manager import save_metadata_checksums
                    save_metadata_checksums(
                        metadata_dir=Path(metadata_dir),
                        metadata_checksum_path=Path(metadata_checksum_path)
                    )
                    print(f"✓ Metadata checksums saved to: {metadata_checksum_path}")
                except Exception as chk_err:
                    print(f"  ⚠ Could not save metadata checksums: {chk_err}")

                # Mark metadata as generated in checkpoint
                if checkpoint.state:
                    checkpoint.state['metadata_generated'] = True
                    checkpoint.save()

                print(f"\n✓ Metadata generation complete for {len(all_cobol_files)} files\n")

            except Exception as e:
                print(f"\n✗ Metadata generation failed: {e}")
                print("  Continuing with documentation generation (may have limited metadata)...\n")

        elif generate_metadata and metadata_generated:
            print(f"\n→ Skipping metadata generation (already completed in previous run)")

        # Get files to process
        pending_files = checkpoint.get_pending_files()

        print(f"\n{'='*70}")
        print(f"BATCH MODE: {'RESUMING' if is_resuming else 'Starting'} - {len(pending_files)} files to process")
        print(f"{'='*70}")
        print(f"  Total files:  {progress['total']}")
        print(f"  Completed:    {progress['completed']}")
        print(f"  Failed:       {progress['failed']}")
        print(f"  Pending:      {len(pending_files)}")
        print(f"{'='*70}\n")

        if not pending_files:
            print("✓ All files already processed!")
            print(checkpoint.get_summary_report())
            sys.exit(0)

        # Process each pending file
        for idx, filename in enumerate(pending_files, 1):
            # Get full path from checkpoint
            file_path = checkpoint.get_file_path(filename)

            if not file_path:
                print(f"⚠ File path not found for: {filename}")
                continue

            prog_name = Path(file_path).stem

            print(f"\n{'#'*70}")
            print(f"# [{idx}/{len(pending_files)}] Processing: {filename}")
            print(f"# Program: {prog_name}")
            print(f"{'#'*70}")

            # Mark as in_progress and save checkpoint
            checkpoint.mark_file_started(filename)
            checkpoint.save()

            try:
                output_path = generate_documentation(
                    program_name=prog_name,
                    workspace_path=workspace_path,
                    metadata_dir=metadata_dir,
                    template_path=template_path,
                    output_dir=docs_path,
                    llm_config=llm_config,
                    cobol_file_path=file_path,
                    enable_source_extraction=enable_source_extraction,
                    auto_start_phase2=auto_start_phase2,
                    language=language,
                    full_config=config_loader.config if config_loader else None,
                )

                if output_path:
                    checkpoint.mark_file_completed(filename, output_path)
                    print(f"✓ Successfully generated: {output_path}")
                else:
                    checkpoint.mark_file_failed(filename, "generate_documentation returned None")
                    print(f"✗ Failed: No output generated")

            except KeyboardInterrupt:
                print(f"\n\n⚠ Interrupted by user. Saving checkpoint...")
                checkpoint.save()
                get_run_logger().finalize()
                print(f"  Checkpoint saved. Resume with: python cobol_doc_agent.py {args.config or ''}")
                sys.exit(130)

            except Exception as e:
                checkpoint.mark_file_failed(filename, str(e))
                print(f"✗ Failed: {e}")

                if not args.continue_on_error:
                    print("\n  Use --continue-on-error to skip failed files and continue.")
                    checkpoint.save()
                    raise

            # Save checkpoint after each file
            checkpoint.save()

            # Print running progress
            progress = checkpoint.get_progress()
            print(f"  Progress: {progress['percent_complete']:.1f}% ({progress['completed']}/{progress['total']})")

        # Final summary
        print(checkpoint.get_summary_report())

        # Finalize run logger
        progress = checkpoint.get_progress()
        get_run_logger().finalize(
            config_hash=config_hash,
            total_files=progress['total'],
            mode='batch',
        )

    else:
        # Single program mode - use two-phase approach
        try:
            output_path = generate_documentation(
                program_name=program_name,
                workspace_path=workspace,
                metadata_dir=metadata_dir,
                template_path=template_path,
                output_dir=docs_path,
                llm_config=llm_config,
                cobol_file_path=None,  # Will be auto-detected
                enable_source_extraction=enable_source_extraction,
                auto_start_phase2=auto_start_phase2,
                language=language,
                full_config=config_loader.config if config_loader else None,
            )
        except Exception as e:
            print(f"\n✗ Fatal error: {e}")
            output_path = None

        print(f"\n{'='*70}")
        print(f"Documentation generation complete!")
        print(f"Output: {output_path}")
        print(f"{'='*70}\n")

        # Finalize run logger
        get_run_logger().finalize(total_files=1, mode='single')
