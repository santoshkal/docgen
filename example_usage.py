"""
Example usage of COBOL Documentation Agent

This script demonstrates different ways to use the agent:
1. Single program documentation
2. Batch processing
3. Custom configuration
4. Error handling
"""

import os
from pathlib import Path
from cobol_doc_agent import generate_documentation


def example_1_basic_usage():
    """
    Example 1: Generate documentation for a single program
    """
    print("\n" + "="*70)
    print("Example 1: Basic Usage")
    print("="*70)

    # Ensure API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠ Please set OPENAI_API_KEY environment variable")
        return

    # Generate documentation for MAINPROG
    output_path = generate_documentation("MAINPROG")

    print(f"\n✓ Documentation generated: {output_path}")


def example_2_batch_processing():
    """
    Example 2: Generate documentation for multiple programs
    """
    print("\n" + "="*70)
    print("Example 2: Batch Processing")
    print("="*70)

    programs = [
        "MAINPROG",
        "ACCTOPER",
        "CUSTMGMT",
        "TRANPROC"
    ]

    for program in programs:
        try:
            print(f"\nProcessing {program}...")
            output_path = generate_documentation(program)
            print(f"✓ {program}: {output_path}")
        except Exception as e:
            print(f"✗ {program}: {str(e)}")


def example_3_custom_configuration():
    """
    Example 3: Use custom paths and configuration
    """
    print("\n" + "="*70)
    print("Example 3: Custom Configuration")
    print("="*70)

    # Custom output directory for this project
    custom_output = "./docs/banking-system"

    output_path = generate_documentation(
        program_name="MAINPROG",
        metadata_dir="../output",
        template_path="./cobol-doc-template.yaml",
        output_dir=custom_output
    )

    print(f"\n✓ Documentation in custom location: {output_path}")


def example_4_error_handling():
    """
    Example 4: Robust error handling
    """
    print("\n" + "="*70)
    print("Example 4: Error Handling")
    print("="*70)

    programs = ["MAINPROG", "NONEXISTENT", "ACCTOPER"]

    results = {"success": [], "failed": []}

    for program in programs:
        try:
            # Check if metadata exists first
            metadata_dir = Path("../output")
            superbol_file = metadata_dir / "superbol" / f"superbol-{program}-doc-symbols.json"

            if not superbol_file.exists():
                print(f"⚠ Skipping {program}: metadata not found")
                results["failed"].append((program, "Metadata not found"))
                continue

            # Generate documentation
            output_path = generate_documentation(program)
            results["success"].append(program)
            print(f"✓ {program}: Success")

        except Exception as e:
            results["failed"].append((program, str(e)))
            print(f"✗ {program}: {str(e)}")

    # Summary
    print("\n" + "-"*70)
    print(f"Success: {len(results['success'])} programs")
    print(f"Failed: {len(results['failed'])} programs")

    if results["failed"]:
        print("\nFailed programs:")
        for prog, error in results["failed"]:
            print(f"  - {prog}: {error}")


def example_5_metadata_validation():
    """
    Example 5: Validate metadata before generation
    """
    print("\n" + "="*70)
    print("Example 5: Metadata Validation")
    print("="*70)

    program = "MAINPROG"
    metadata_dir = Path("../output")

    # Check required metadata files
    required_files = [
        metadata_dir / "superbol" / f"superbol-{program}-doc-symbols.json",
        metadata_dir / "superbol" / "superbol-cfg" / f"{program}.json",
        metadata_dir / "gnucobol" / "gnucobol-batch-analyze-all.json",
        metadata_dir / "ctags" / f"ctags-{program}-outline.json"
    ]

    all_exist = True
    for file_path in required_files:
        if file_path.exists():
            print(f"✓ Found: {file_path.name}")
        else:
            print(f"✗ Missing: {file_path.name}")
            all_exist = False

    if all_exist:
        print(f"\n✓ All metadata present for {program}")
        print("Proceeding with documentation generation...")
        output_path = generate_documentation(program)
        print(f"✓ Generated: {output_path}")
    else:
        print(f"\n✗ Cannot generate documentation: missing metadata")


def example_6_parallel_processing():
    """
    Example 6: Parallel processing (commented out - requires setup)
    """
    print("\n" + "="*70)
    print("Example 6: Parallel Processing (Demo)")
    print("="*70)

    print("""
    For parallel processing, uncomment this code:

    from concurrent.futures import ProcessPoolExecutor

    programs = ["MAINPROG", "ACCTOPER", "CUSTMGMT", "TRANPROC"]

    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(generate_documentation, prog)
            for prog in programs
        ]

        results = [f.result() for f in futures]

    print(f"Generated {len(results)} documents in parallel")
    """)


if __name__ == "__main__":
    print("\n" + "#"*70)
    print("COBOL Documentation Agent - Example Usage")
    print("#"*70)

    # Run examples
    # Uncomment the examples you want to try:

    example_1_basic_usage()

    # example_2_batch_processing()

    # example_3_custom_configuration()

    # example_4_error_handling()

    # example_5_metadata_validation()

    # example_6_parallel_processing()

    print("\n" + "#"*70)
    print("Examples complete!")
    print("#"*70 + "\n")
