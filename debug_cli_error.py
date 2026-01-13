#!/usr/bin/env python3
"""Debug script to test Claude CLI with large prompts."""

import subprocess
import tempfile
from pathlib import Path

def find_cli():
    import claude_agent_sdk
    return str(Path(claude_agent_sdk.__file__).parent / "_bundled" / "claude")

def test_large_prompt(size_kb=750):
    cli_path = find_cli()
    
    # Create prompt similar to Phase 2 context
    large_content = "COBOL documentation context " * (size_kb * 50)
    prompt = f"""You are a technical documentation agent. 
    
Generate a brief summary (2-3 sentences) of this COBOL program context:

{large_content}

Respond with just the summary."""

    print(f"Prompt size: {len(prompt):,} bytes ({len(prompt)/1024:.0f} KB)")
    print(f"CLI: {cli_path}")
    
    # Write to temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(prompt)
        temp_path = f.name
    
    cmd = [
        cli_path,
        "--print",
        "--model", "claude-sonnet-4-20250514",
        "--allowedTools", ""
    ]
    
    print(f"\nRunning: {' '.join(cmd[:4])}...")
    print(f"(prompt via stdin from temp file)\n")
    
    try:
        with open(temp_path, 'r') as f:
            result = subprocess.run(
                cmd,
                stdin=f,
                capture_output=True,
                text=True,
                timeout=300
            )
        
        print(f"Exit code: {result.returncode}")
        print(f"\n{'='*50}")
        print("STDOUT:")
        print(f"{'='*50}")
        print(result.stdout[:1000] if result.stdout else "(empty)")
        
        print(f"\n{'='*50}")
        print("STDERR:")
        print(f"{'='*50}")
        print(result.stderr[:1000] if result.stderr else "(empty)")
        
    finally:
        Path(temp_path).unlink(missing_ok=True)

if __name__ == "__main__":
    import sys
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 750
    test_large_prompt(size)
