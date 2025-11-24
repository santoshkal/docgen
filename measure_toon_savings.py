#!/usr/bin/env python3
"""
Measure EXACT token savings when converting metadata to TOON format.
Compares JSON vs TOON using tiktoken.
"""
import json
import tiktoken
from pathlib import Path
from toon_format import encode

# Initialize tiktoken encoder
enc = tiktoken.encoding_for_model("gpt-4")

def count_tokens(text: str) -> int:
    """Count tokens using tiktoken"""
    return len(enc.encode(text))

def analyze_with_toon(file_path: str, label: str):
    """Analyze metadata file in both JSON and TOON formats"""
    path = Path(file_path)
    if not path.exists():
        print(f"❌ {label}: File not found")
        return None

    with open(path) as f:
        data = json.load(f)

    # JSON format (current)
    json_str = json.dumps(data, indent=2)
    json_tokens = count_tokens(json_str)

    # TOON format
    try:
        toon_str = encode(data)
        toon_tokens = count_tokens(toon_str)
    except Exception as e:
        print(f"❌ {label}: TOON encoding failed - {e}")
        return None

    # Calculate savings
    saved_tokens = json_tokens - toon_tokens
    saved_pct = (saved_tokens / json_tokens * 100) if json_tokens > 0 else 0

    print(f"\n{'='*70}")
    print(f"{label}")
    print(f"{'='*70}")
    print(f"  JSON tokens:   {json_tokens:>10,}")
    print(f"  TOON tokens:   {toon_tokens:>10,}")
    print(f"  Saved:         {saved_tokens:>10,} tokens ({saved_pct:.1f}%)")

    return {
        'label': label,
        'json_tokens': json_tokens,
        'toon_tokens': toon_tokens,
        'saved_tokens': saved_tokens,
        'saved_pct': saved_pct
    }

def main():
    print("\n" + "="*70)
    print("TOON FORMAT TOKEN SAVINGS ANALYSIS")
    print("="*70)
    print("Comparing JSON vs TOON using tiktoken (GPT-4 encoding)")

    results = []

    # CTags
    result = analyze_with_toon(
        '/home/santosh/cobol-work/metadata/ctags/ctags-TDAS-MINDISTCALC-outline.json',
        'CTags Outline'
    )
    if result:
        results.append(result)

    # SuperBOL Symbols
    result = analyze_with_toon(
        '/home/santosh/cobol-work/metadata/superbol/superbol-TDAS-MINDISTCALC-doc-symbols.json',
        'SuperBOL Symbols'
    )
    if result:
        results.append(result)

    # GnuCOBOL Analysis
    result = analyze_with_toon(
        '/home/santosh/cobol-work/metadata/gnucobol/gnucobol-TDAS-MINDISTCALC-analysis.json',
        'GnuCOBOL Analysis'
    )
    if result:
        results.append(result)

    # Summary
    if results:
        total_json = sum(r['json_tokens'] for r in results)
        total_toon = sum(r['toon_tokens'] for r in results)
        total_saved = total_json - total_toon
        total_saved_pct = (total_saved / total_json * 100) if total_json > 0 else 0

        print(f"\n{'='*70}")
        print("SUMMARY - TOKEN SAVINGS")
        print(f"{'='*70}")
        print(f"\n  {'Metadata Source':<25} {'JSON':>12} {'TOON':>12} {'Saved':>12}")
        print(f"  {'-'*65}")
        for r in results:
            print(f"  {r['label']:<25} {r['json_tokens']:>10,}  {r['toon_tokens']:>10,}  {r['saved_tokens']:>10,}  ({r['saved_pct']:>5.1f}%)")
        print(f"  {'-'*65}")
        print(f"  {'TOTAL':<25} {total_json:>10,}  {total_toon:>10,}  {total_saved:>10,}  ({total_saved_pct:>5.1f}%)")

        print(f"\n{'='*70}")
        print("IMPACT ANALYSIS")
        print(f"{'='*70}")
        print(f"  Current baseline (JSON):    {total_json:,} tokens")
        print(f"  With TOON format:           {total_toon:,} tokens")
        print(f"  Total savings:              {total_saved:,} tokens ({total_saved_pct:.1f}%)")
        print(f"\n  Context window limit:       128,000 tokens")
        print(f"  Baseline exceeds by:        {((total_json / 128000 - 1) * 100):,.1f}%")
        print(f"  TOON exceeds by:            {((total_toon / 128000 - 1) * 100):,.1f}%")
        
        # Calculate how much less filtering needed
        if total_json > 0:
            current_filtered_pct = (128000 / total_json) * 100
            toon_filtered_pct = (128000 / total_toon) * 100
            print(f"\n  Current: Must filter to ~{current_filtered_pct:.1f}% of data")
            print(f"  With TOON: Can keep ~{toon_filtered_pct:.1f}% of data")
            print(f"  → {toon_filtered_pct - current_filtered_pct:.1f}% MORE context available!")

if __name__ == '__main__':
    main()
