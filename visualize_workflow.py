#!/usr/bin/env python3
"""
Visualize the COBOL Documentation Agent LangGraph Workflow

This script generates a visual representation of the agent's state graph,
showing all nodes and their connections/transitions.
"""

import sys
from pathlib import Path

# Import the agent (will be done lazily in visualize_workflow if needed)
try:
    from IPython.display import Image, display
    IPYTHON_AVAILABLE = True
except ImportError:
    IPYTHON_AVAILABLE = False
    # Only print if we're actually trying to visualize
    # print("IPython not available. Will save image to file instead.")


def visualize_workflow(save_to_file: bool = True, display_inline: bool = True):
    """
    Visualize the LangGraph workflow

    Args:
        save_to_file: Save the PNG image to a file
        display_inline: Display the image inline (requires IPython/Jupyter)
    """
    print("Creating COBOL Documentation Agent workflow graph...")

    # Import the agent (lazy import to avoid dependency issues in summary-only mode)
    try:
        from cobol_doc_agent import create_documentation_agent
    except ImportError as e:
        print(f"✗ Error importing agent: {e}")
        print("Make sure langchain dependencies are installed: pip install langchain-core langgraph")
        raise

    # Create the agent (compiled graph)
    agent = create_documentation_agent()

    # Generate the graph visualization
    try:
        # Get the graph and draw it as PNG
        png_data = agent.get_graph().draw_mermaid_png()

        if save_to_file:
            output_file = Path(__file__).parent / "workflow_graph.png"
            with open(output_file, "wb") as f:
                f.write(png_data)
            print(f"✓ Workflow graph saved to: {output_file}")

        if display_inline and IPYTHON_AVAILABLE:
            print("\nDisplaying workflow graph...")
            display(Image(png_data))
        elif display_inline and not IPYTHON_AVAILABLE:
            print("\n⚠ IPython not available. Image saved to file but cannot display inline.")
            print("To view: open workflow_graph.png or install IPython with: pip install ipython")

        return png_data

    except Exception as e:
        print(f"✗ Error generating graph visualization: {e}")
        print("\nTrying alternative method (Mermaid format)...")

        try:
            # Alternative: Save as Mermaid diagram
            mermaid_code = agent.get_graph().draw_mermaid()
            mermaid_file = Path(__file__).parent / "workflow_graph.mmd"
            with open(mermaid_file, "w") as f:
                f.write(mermaid_code)
            print(f"✓ Workflow graph (Mermaid format) saved to: {mermaid_file}")
            print("\nYou can visualize this at: https://mermaid.live/")
            return mermaid_code
        except Exception as e2:
            print(f"✗ Error generating Mermaid diagram: {e2}")
            raise


def print_workflow_summary():
    """Print a text summary of the workflow"""
    print("\n" + "="*70)
    print("COBOL DOCUMENTATION AGENT - WORKFLOW SUMMARY")
    print("="*70)

    print("""
Nodes:
  1. START (entry point)
  2. should_generate_metadata - Checksum-based intelligent routing (conditional)
  3. generate_metadata - Generate metadata via MCP servers (if needed)
  4. load_metadata - Load metadata from disk
  5. load_template - Load YAML documentation template
  6. extract_structure - Parse template structure (creates passes for two-pass mode)
  7. process_section - Generate content for each section (loops with source extraction)
  8. check_completion - Determine if more sections/passes needed
  9. assemble_document - Combine all sections into final markdown
  10. save_document - Write final markdown file to disk
  11. END (exit point)

Edges:
  START → should_generate_metadata
  should_generate_metadata → [conditional]
    ├─ generate_via_checksum → generate_metadata (source changed or missing metadata)
    └─ skip_checksums_valid → load_metadata (all checksums valid)
  generate_metadata → load_metadata
  load_metadata → load_template
  load_template → extract_structure
  extract_structure → process_section
  process_section → check_completion
  check_completion → [conditional]
    ├─ continue → process_section (more sections/passes to process)
    └─ assemble → assemble_document (all sections complete)
  assemble_document → save_document
  save_document → END

Intelligent Checksum-Based Routing:
  • should_generate_metadata(): Uses SHA256 checksums to intelligently decide

    Decision Flow:
    ┌─────────────────────────────────────────────────────────────────┐
    │ 1. Calculate current source file checksums (SHA256)            │
    │ 2. Load previous source checksums (if exist)                   │
    │ 3. Compare:                                                     │
    │    ├─ CASE 1: No previous checksums → GENERATE (first run)     │
    │    ├─ CASE 2: Checksums differ → GENERATE (source changed)     │
    │    └─ CASE 3: Checksums match → Check metadata checksums       │
    │         ├─ No metadata checksums → GENERATE (missing)          │
    │         ├─ Metadata checksums differ → GENERATE (corrupted)    │
    │         └─ All checksums valid → SKIP (use existing metadata)  │
    └─────────────────────────────────────────────────────────────────┘

  • check_completion(): Determines if more sections/passes need processing
    - Two-pass mode: Processes sections in multiple passes with different filtering
    - Single-pass mode: Processes all sections once with aggressive filtering

Two-Pass Mode:
  Pass 1: Conservative filtering (Executive Summary, Program Structure, Appendix)
    - Keeps more metadata for high-level overview sections
    - Reduces risk of missing critical information

  Pass 2: Balanced filtering (Control Flow, Data Flow, Inter-Program Communication)
    - Optimized metadata filtering for detailed analysis
    - Includes source code extraction when enabled

  Pass 3: Aggressive filtering (Error Handling, Technical Details)
    - Maximum token reduction for final sections
    - Focuses on specific patterns and structures

Phase 1-3 Integration:

  Phase 1: Source Code Extraction (Option A)
    • extract_source_for_section(): Extracts COBOL source divisions
    • Configurable compression (removes comments/blank lines)
    • Section-specific extraction (DATA vs PROCEDURE DIVISION)
    • Integrated into build_section_context() node function

  Phase 2: RipGrep Pattern Extraction
    • extract_with_ripgrep(): Pattern-based extraction for specific constructs
    • Supports: SQL statements, EXEC blocks, error handlers, comments
    • Fallback to basic extraction when ripgrep unavailable
    • Reduces token usage by extracting only relevant code patterns

  Phase 3: Multi-File Support
    • CopybookResolver: Resolves COPY statements, includes copybook content
    • CalledProgramResolver: Identifies CALL statements, resolves programs
    • extract_source_multi_file(): Combines main program + dependencies
    • Initialized in generate_documentation() before workflow starts
    • Graceful degradation: Falls back to single-file when unavailable

build_section_context Node (Enhanced):
  1. Filters metadata based on pass mode (aggressive/conservative/balanced)
  2. Checks section_requirements.py for source extraction needs
  3. If Phase 3 enabled:
     - Routes to extract_source_multi_file() with resolvers
     - Includes copybook content for data sections
     - Includes called program info for logic sections
  4. If Phase 1 enabled (Phase 3 disabled):
     - Routes to extract_source_for_section() (basic extraction)
  5. Adds source code to section context for LLM
  6. Handles errors gracefully (continues without source if extraction fails)

Checksum Files:
  • source-checksum.yaml: SHA256 hashes of all COBOL source files
    - Tracks file size, modification time, relative paths
    - Supports nested directories and multiple file extensions
    - Auto-generated on first run, updated when sources change

  • metadata-checksum.yaml: SHA256 hashes of all generated metadata files
    - Validates CTags, GnuCOBOL, and SuperBOL outputs
    - Detects corruption, incompleteness, or manual edits
    - Auto-generated after metadata creation

Benefits:
  ⚡ 10x faster on unchanged files (skips expensive MCP processing)
  🔒 Automatic validation - detects corrupted or incomplete metadata
  📊 Audit trail - checksum files track all changes with timestamps
  🔄 Incremental updates - only regenerates what changed
  📝 Source-aware - includes actual COBOL code in documentation context
  🔗 Multi-file support - resolves copybooks and called programs
  🎯 Smart filtering - two-pass mode balances quality vs token usage

State Flow:
  All nodes receive and return AgentState (TypedDict) containing:

  Core Parameters:
    - program_name, workspace_path, metadata_dir, template_path, output_dir
    - servers_config, llm_config (provider, model, api_key, temperature)
    - generate_metadata, skip_existing_metadata, cobol_files

  Checksum Management:
    - source_checksum_path, metadata_checksum_path
    - metadata_generation_reason (why regeneration was needed)

  Loaded Metadata:
    - superbol_symbols, superbol_cfg (control flow graph with calls[] and copybooks[])
    - gnucobol_analysis (contains relationships and cross_references), ctags_outline

  Two-Pass Mode:
    - use_two_pass_mode (bool), current_pass (pass number)
    - passes (list of pass configurations), current_pass_index

  Phase 1-3: Source Code Extraction:
    - enable_source_extraction (bool), compress_source (bool)
    - cobol_file_path (path to main COBOL file)
    - resolve_copybooks (bool), resolve_called_programs (bool)
    - copybook_search_paths, program_search_paths
    - copybook_resolver (CopybookResolver instance)
    - called_program_resolver (CalledProgramResolver instance)

  Processing State:
    - template (parsed YAML), current_section, section_ids
    - current_section_index, generated_content

  Output:
    - final_document (assembled markdown), errors (list of error messages)

Recent Enhancements & Bug Fixes:

  ✓ Template Updates (cobol-doc-template.yaml):
    - Added emphatic CRITICAL instructions for extracting calls[] and copybooks[]
    - New "Referenced Copybooks" section for documenting COPY statements
    - Strengthened 10+ sections with explicit extraction guidance
    - Fixed: External calls and copybooks now properly documented

  ✓ Metadata Filtering Fix (cobol_doc_agent.py):
    - Preserved calls[] and copybooks[] arrays in all filtering functions
    - Pass 1 filtering: Lines 673-674 (Executive Summary)
    - Pass 2 filtering: Lines 708-710 (Control Flow Analysis)
    - Aggressive filtering: Lines 885-886, 901-902 (all passes)
    - Fixed: LLM now receives call/copybook data for documentation

  ✓ Section Requirements Update (section_requirements.py):
    - Added all new template section IDs (28 sections total)
    - Configured data-transformations section: extract_source=True
    - Fixed: MOVE/COMPUTE/STRING/UNSTRING operations now documented
    - Supports both legacy and new template section naming

  ✓ Batch Mode File Path Fix (cobol_doc_agent.py):
    - Line 1715: Changed from source_path.name to str(source_path)
    - Line 1723: Changed from f.name to str(f) for directory processing
    - Fixed: Source extraction now receives full paths, not just filenames
    - Impact: All sections requiring source code now work correctly

  ✓ Phase 3 Integration Complete:
    - Multi-file resolvers initialized before workflow starts
    - CopybookResolver: Searches 2+ paths, resolves all COPY statements
    - CalledProgramResolver: Searches 2+ paths, identifies CALL targets
    - build_section_context: Routes correctly based on section type
    - Graceful degradation: Falls back when resolvers unavailable

Known Issues & Limitations:
  • GnuCOBOL metadata may fail if copybooks not found (success=false)
  • SuperBol CFG is primary source for calls[] and copybooks[] arrays
  • RipGrep Phase 2 not yet fully integrated (prepared but not active)
  • Large programs (>100K lines) may exceed LLM token limits
    """)

    print("="*70 + "\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Visualize COBOL Documentation Agent LangGraph workflow"
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Don't save the graph to a file"
    )
    parser.add_argument(
        "--no-display",
        action="store_true",
        help="Don't try to display inline (useful in non-Jupyter environments)"
    )
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="Only print text summary, don't generate graph"
    )

    args = parser.parse_args()

    if args.summary_only:
        print_workflow_summary()
    else:
        try:
            visualize_workflow(
                save_to_file=not args.no_save,
                display_inline=not args.no_display
            )
            print_workflow_summary()
        except Exception as e:
            print(f"\n✗ Failed to generate visualization: {e}")
            print("\nFalling back to text summary:")
            print_workflow_summary()
            sys.exit(1)
