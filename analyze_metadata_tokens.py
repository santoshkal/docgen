#!/usr/bin/env python3
"""
Analyze current metadata token usage to establish baseline before TOON integration.
Measures exact tokens using tiktoken for all metadata sources.
"""
import json
import tiktoken
from pathlib import Path

# Initialize tiktoken encoder (using GPT-4 encoding)
enc = tiktoken.encoding_for_model("gpt-4")

def count_tokens(text: str) -> int:
    """Count tokens using tiktoken"""
    return len(enc.encode(text))

def analyze_metadata_file(file_path: str, label: str):
    """Analyze a single metadata JSON file"""
    path = Path(file_path)
    if not path.exists():
        print(f"❌ {label}: File not found - {file_path}")
        return None

    with open(path) as f:
        data = json.load(f)

    # Convert to JSON string (pretty-printed, like what we send to LLM)
    json_str = json.dumps(data, indent=2)

    tokens = count_tokens(json_str)
    size_kb = len(json_str) / 1024

    print(f"\n{'='*70}")
    print(f"{label}")
    print(f"{'='*70}")
    print(f"  File: {path.name}")
    print(f"  Size: {size_kb:.1f} KB")
    print(f"  Tokens (JSON): {tokens:,}")

    return {
        'label': label,
        'file': str(path),
        'size_kb': size_kb,
        'tokens': tokens,
        'data': data
    }

def main():
    print("\n" + "="*70)
    print("METADATA TOKEN ANALYSIS - BASELINE (JSON FORMAT)")
    print("="*70)
    print("Using tiktoken with GPT-4 encoding (cl100k_base)")

    # Analyze all metadata files
    results = []

    # CTags
    result = analyze_metadata_file(
        '/home/santosh/cobol-work/metadata/ctags/ctags-TDAS-MINDISTCALC-outline.json',
        'CTags Outline'
    )
    if result:
        results.append(result)

    # SuperBOL Symbols
    result = analyze_metadata_file(
        '/home/santosh/cobol-work/metadata/superbol/superbol-TDAS-MINDISTCALC-doc-symbols.json',
        'SuperBOL Symbols'
    )
    if result:
        results.append(result)

    # SuperBOL CFG
    result = analyze_metadata_file(
        '/home/santosh/cobol-work/metadata/superbol/superbol-TDAS-MINDISTCALC-doc-cfg.json',
        'SuperBOL CFG'
    )
    if result:
        results.append(result)

    # GnuCOBOL Analysis
    result = analyze_metadata_file(
        '/home/santosh/cobol-work/metadata/gnucobol/gnucobol-TDAS-MINDISTCALC-analysis.json',
        'GnuCOBOL Analysis'
    )
    if result:
        results.append(result)

    # Summary
    if results:
        total_tokens = sum(r['tokens'] for r in results)
        total_size = sum(r['size_kb'] for r in results)

        print(f"\n{'='*70}")
        print("SUMMARY - BASELINE (JSON FORMAT)")
        print(f"{'='*70}")
        for r in results:
            print(f"  {r['label']:25s} {r['tokens']:>10,} tokens")
        print(f"  {'-'*35}")
        print(f"  {'TOTAL (UNFILTERED)':25s} {total_tokens:>10,} tokens")
        print(f"  {'Total Size':25s} {total_size:>10.1f} KB")
        print(f"\n  ⚠️  This exceeds 128K context window by {((total_tokens / 128000) * 100 - 100):.1f}%")
        print(f"  ⚠️  Current solution: Aggressive filtering (loses 70-90% of data)")

        return results

    return None

if __name__ == '__main__':
    main()
