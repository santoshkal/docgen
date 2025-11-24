#!/bin/bash
# Compare JSON vs TOON token counts using tiktoken

cd /home/santosh/cobol-work/agent
source .venv/bin/activate

python3 << 'PYTHON'
import json
import subprocess
import tiktoken
from pathlib import Path

enc = tiktoken.encoding_for_model("gpt-4")

def count_tokens(text):
    return len(enc.encode(text))

def convert_to_toon(json_file):
    """Convert JSON to TOON using CLI"""
    result = subprocess.run(
        ['npx', '@toon-format/cli', json_file],
        capture_output=True,
        text=True,
        cwd='/home/santosh/cobol-work/metadata'
    )
    return result.stdout

print("\n" + "="*70)
print("JSON vs TOON TOKEN COMPARISON (EXACT MEASUREMENTS)")
print("="*70)
print("Using tiktoken (GPT-4 encoding: cl100k_base)\n")

files = [
    ('/home/santosh/cobol-work/metadata/ctags/ctags-TDAS-MINDISTCALC-outline.json', 'CTags Outline'),
    ('/home/santosh/cobol-work/metadata/superbol/superbol-TDAS-MINDISTCALC-doc-symbols.json', 'SuperBOL Symbols'),
    ('/home/santosh/cobol-work/metadata/gnucobol/gnucobol-TDAS-MINDISTCALC-analysis.json', 'GnuCOBOL Analysis'),
]

results = []

for file_path, label in files:
    path = Path(file_path)
    if not path.exists():
        continue
    
    # JSON tokens
    with open(path) as f:
        data = json.load(f)
    json_str = json.dumps(data, indent=2)
    json_tokens = count_tokens(json_str)
    
    # TOON tokens
    print(f"Converting {label} to TOON...", end=" ", flush=True)
    toon_str = convert_to_toon(str(path))
    toon_tokens = count_tokens(toon_str)
    print("✓")
    
    saved = json_tokens - toon_tokens
    saved_pct = (saved / json_tokens * 100) if json_tokens > 0 else 0
    
    results.append({
        'label': label,
        'json': json_tokens,
        'toon': toon_tokens,
        'saved': saved,
        'pct': saved_pct
    })

# Print results
print(f"\n{'Metadata Source':<25} {'JSON':>12} {'TOON':>12} {'Saved':>15}")
print("-" * 70)
for r in results:
    print(f"{r['label']:<25} {r['json']:>10,}  {r['toon']:>10,}  {r['saved']:>10,} ({r['pct']:>5.1f}%)")

total_json = sum(r['json'] for r in results)
total_toon = sum(r['toon'] for r in results)
total_saved = total_json - total_toon
total_pct = (total_saved / total_json * 100) if total_json > 0 else 0

print("-" * 70)
print(f"{'TOTAL':<25} {total_json:>10,}  {total_toon:>10,}  {total_saved:>10,} ({total_pct:>5.1f}%)")

print(f"\n{'='*70}")
print("IMPACT ON DOCUMENTATION GENERATION")
print(f"{'='*70}")
print(f"Current (JSON):           {total_json:,} tokens (exceeds 128K by {((total_json/128000-1)*100):.0f}%)")
print(f"With TOON:                {total_toon:,} tokens (exceeds 128K by {((total_toon/128000-1)*100):.0f}%)")
print(f"Total savings:            {total_saved:,} tokens ({total_pct:.1f}%)")

# Calculate filtering impact
current_keep = (128000 / total_json) * 100
toon_keep = (128000 / total_toon) * 100
print(f"\nCurrent filtering:        Keep ~{current_keep:.1f}% of data (lose {100-current_keep:.1f}%)")
print(f"With TOON:                Keep ~{toon_keep:.1f}% of data (lose {100-toon_keep:.1f}%)")
print(f"Improvement:              {toon_keep - current_keep:.1f}% MORE context available!")

PYTHON
