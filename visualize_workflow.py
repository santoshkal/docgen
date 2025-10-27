#!/usr/bin/env python3
"""
Visualize the COBOL Documentation Agent LangGraph Workflow

This script generates a visual representation of the agent's state graph,
showing all nodes and their connections/transitions.
"""

import sys
from pathlib import Path

# Import the agent
from cobol_doc_agent import create_documentation_agent

try:
    from IPython.display import Image, display
    IPYTHON_AVAILABLE = True
except ImportError:
    IPYTHON_AVAILABLE = False
    print("IPython not available. Will save image to file instead.")


def visualize_workflow(save_to_file: bool = True, display_inline: bool = True):
    """
    Visualize the LangGraph workflow

    Args:
        save_to_file: Save the PNG image to a file
        display_inline: Display the image inline (requires IPython/Jupyter)
    """
    print("Creating COBOL Documentation Agent workflow graph...")

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
  2. generate_metadata - Generate metadata via MCP servers (conditional)
  3. load_metadata - Load metadata from disk
  4. load_template - Load YAML documentation template
  5. extract_structure - Parse template structure
  6. process_section - Generate content for each section (loops)
  7. assemble_document - Combine all sections
  8. save_document - Write final markdown file
  9. END (exit point)

Edges:
  START → [checksum-based routing] → generate_metadata OR load_metadata
  generate_metadata → [saves checksums] → load_metadata
  load_metadata → load_template
  load_template → extract_structure
  extract_structure → process_section
  process_section → [conditional] → process_section OR assemble_document
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

  • check_completion(): Determines if more sections need processing

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

State Flow:
  All nodes receive and return AgentState (TypedDict) containing:
  - Input parameters (program_name, paths, flags, servers_config)
  - Checksum management (source/metadata checksum paths, generation reason)
  - Loaded metadata (superbol, gnucobol, ctags)
  - Processing state (current_section, section_ids, etc.)
  - Generated content and final document
  - Error tracking
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
