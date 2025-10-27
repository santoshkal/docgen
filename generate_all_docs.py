#!/usr/bin/env python3
"""
Batch Documentation Generator
Generates documentation for all COBOL programs in the project
"""

import os
import sys
from pathlib import Path
from cobol_doc_agent import generate_documentation


def get_available_programs(metadata_dir="../output"):
    """Get list of programs that have metadata available"""
    superbol_dir = Path(metadata_dir) / "superbol"
    programs = []

    if not superbol_dir.exists():
        print(f"❌ ERROR: Metadata directory not found: {superbol_dir}")
        return []

    for file in superbol_dir.glob("superbol-*-doc-symbols.json"):
        program_name = file.stem.replace("superbol-", "").replace("-doc-symbols", "")
        programs.append(program_name)

    return sorted(programs)


def main():
    print("=" * 70)
    print("COBOL Documentation Generator - Batch Mode")
    print("=" * 70)
    print()

    # Check API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ ERROR: OPENAI_API_KEY not set")
        print("   Run: export OPENAI_API_KEY='your-key'")
        sys.exit(1)

    # Get available programs
    programs = get_available_programs()

    if not programs:
        print("❌ No programs found in metadata directory")
        sys.exit(1)

    total = len(programs)
    print(f"Found {total} programs to document:")
    for prog in programs:
        print(f"  - {prog}")
    print()

    # Confirm
    response = input(f"Generate documentation for all {total} programs? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled.")
        sys.exit(0)

    print()
    print("=" * 70)
    print("Starting batch generation...")
    print("=" * 70)
    print()

    # Track results
    results = {
        "success": [],
        "failed": []
    }

    # Generate documentation for each program
    for i, program in enumerate(programs, 1):
        print(f"[{i}/{total}] Processing {program}...")

        try:
            output_path = generate_documentation(program)
            results["success"].append(program)
            print(f"  ✓ Success: {output_path}")
        except Exception as e:
            results["failed"].append((program, str(e)))
            print(f"  ✗ Failed: {e}")

        print()

    # Summary
    print("=" * 70)
    print("Batch Generation Complete!")
    print("=" * 70)
    print(f"Success: {len(results['success'])} programs")
    print(f"Failed:  {len(results['failed'])} programs")

    if results["failed"]:
        print()
        print("Failed programs:")
        for prog, error in results["failed"]:
            print(f"  - {prog}: {error}")
        print()
        print("Retry failed programs with:")
        for prog, _ in results["failed"]:
            print(f"  python cobol_doc_agent.py {prog}")

    print()
    print("Documentation saved to: ../docs/")

    docs_dir = Path("../docs")
    if docs_dir.exists():
        doc_files = list(docs_dir.glob("*.md"))
        print(f"Total files: {len(doc_files)}")
        print()
        print("Generated files:")
        for doc_file in sorted(doc_files):
            size = doc_file.stat().st_size
            print(f"  - {doc_file.name} ({size:,} bytes)")

    sys.exit(0 if not results["failed"] else 1)


if __name__ == "__main__":
    main()
