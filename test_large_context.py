#!/usr/bin/env python3
"""
Test script to simulate Phase 2 large context calls to Claude CLI.
This reproduces the actual error without running the full 3-hour Phase 1.
"""

import subprocess
import tempfile
import json
from pathlib import Path

def find_cli():
    import claude_agent_sdk
    return str(Path(claude_agent_sdk.__file__).parent / "_bundled" / "claude")

def test_phase2_simulation(context_size_kb=750):
    """
    Simulate a Phase 2 section generation with large context.
    
    Phase 2 receives:
    - prose: Extracted text from Phase 1 (can be 500KB-1MB)
    - metadata: Program structure info
    - template: Section template
    - system_prompt: Instructions
    """
    
    cli_path = find_cli()
    print(f"CLI: {cli_path}")
    
    # Simulate the prose content (this is what makes the context large)
    # In reality, this comes from Phase 1's detailed code explanation
    simulated_prose = """
## Code Explanation Summary

This COBOL program performs complex business calculations including:
- Minimum distance calculations between geographic points
- Data validation and error handling
- Database operations via embedded SQL
- Report generation

### Paragraph Analysis
""" + ("The paragraph processes data items and performs calculations. " * 5000)  # ~300KB of prose
    
    # Simulate metadata (typically 50-100KB)
    simulated_metadata = {
        "program_name": "TDAS-MINDISTCALC",
        "paragraphs": [{"name": f"PARA-{i:04d}", "line": i*10, "calls": ["SUB-ROUTINE"]} for i in range(500)],
        "data_items": [{"name": f"WS-VAR-{i:04d}", "type": "PIC X(100)", "level": "05"} for i in range(200)],
        "copy_statements": ["COPYBOOK1", "COPYBOOK2", "COPYBOOK3"],
    }
    
    # Build the full context like Phase 2 does
    context = {
        "prose": simulated_prose,
        "metadata": simulated_metadata,
        "section_id": "executive-summary",
        "program_name": "TDAS-MINDISTCALC",
    }
    
    # Build the prompt like generate_section_content() does
    system_prompt = """You are a technical documentation agent specializing in COBOL code analysis.
Your task is to generate documentation for the section: "Executive Summary"

Generate a 2-3 paragraph executive summary of this COBOL program based on the provided context."""

    user_prompt = f"""Based on the following context, generate an executive summary:

PROGRAM CONTEXT:
{json.dumps(context, indent=2)}

Generate only the executive summary section in Markdown format."""

    total_prompt = system_prompt + "\n\n" + user_prompt
    prompt_size = len(total_prompt.encode('utf-8'))
    
    print(f"\n{'='*60}")
    print(f"SIMULATING PHASE 2 SECTION GENERATION")
    print(f"{'='*60}")
    print(f"Prose size: {len(simulated_prose):,} bytes")
    print(f"Metadata size: {len(json.dumps(simulated_metadata)):,} bytes")
    print(f"Total prompt size: {prompt_size:,} bytes ({prompt_size/1024:.0f} KB)")
    print(f"{'='*60}\n")
    
    # Write to temp file (this is what the fix does)
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(total_prompt)
        temp_path = f.name
    
    cmd = [
        cli_path,
        "--print",
        "--model", "claude-sonnet-4-20250514",
        "--allowedTools", ""
    ]
    
    print(f"Running Claude CLI with prompt via stdin...")
    print(f"Command: {' '.join(cmd[:4])} ...")
    
    try:
        with open(temp_path, 'r') as f:
            result = subprocess.run(
                cmd,
                stdin=f,
                capture_output=True,
                text=True,
                timeout=300
            )
        
        print(f"\n{'='*60}")
        print(f"EXIT CODE: {result.returncode}")
        print(f"{'='*60}")
        
        print(f"\nSTDOUT ({len(result.stdout)} chars):")
        print("-" * 40)
        if result.stdout:
            print(result.stdout[:1000])
            if len(result.stdout) > 1000:
                print(f"... [{len(result.stdout) - 1000} more chars]")
        else:
            print("(empty)")
        
        print(f"\nSTDERR ({len(result.stderr)} chars):")
        print("-" * 40)
        if result.stderr:
            print(result.stderr[:1000])
        else:
            print("(empty)")
            
    finally:
        Path(temp_path).unlink(missing_ok=True)

if __name__ == "__main__":
    import sys
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 750
    test_phase2_simulation(size)
