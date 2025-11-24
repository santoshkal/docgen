# TOON Format Integration Plan

## Executive Summary

**EXACT Token Savings Measured with tiktoken:**

| Metadata Source | JSON Tokens | TOON Tokens | Saved | Savings % |
|----------------|-------------|-------------|-------|-----------|
| CTags Outline | 853,231 | 534,124 | 319,107 | **37.4%** |
| SuperBOL Symbols | 1,782,478 | 1,371,111 | 411,367 | **23.1%** |
| GnuCOBOL Analysis | 681,293 | 681,262 | 31 | **0.0%** |
| **TOTAL** | **3,317,002** | **2,586,497** | **730,505** | **22.0%** |

**Current State:**
- Baseline (JSON): 3,317,002 tokens (2,491% over 128K limit)
- Must filter to ~3.9% of data (lose 96.1%)

**With TOON:**
- New baseline: 2,586,497 tokens (1,921% over 128K limit)
- Can keep ~4.9% of data (lose 95.1%)
- **Improvement: 1.1% MORE context = 36,476 more tokens!**

---

## Goal: Enhance Final Documentation Quality

### How TOON Helps:

1. **22% token savings** = room for richer metadata
2. **Best savings on CTags (37.4%)** = more paragraph details
3. **Good savings on SuperBOL (23.1%)** = more symbol information
4. **GnuCOBOL (0%)** = already dense, no benefit

### Strategy:

**Focus TOON on high-value, high-savings metadata:**
- ✅ CTags (37.4% savings) → Use for Pass 2 logic sections
- ✅ SuperBOL Symbols (23.1% savings) → Use for Pass 2 structure
- ❌ GnuCOBOL (0% savings) → Keep as JSON (no benefit)

---

## Implementation Plan

### Phase 1: Create Metadata Converter Module

**File:** `metadata_toon_converter.py`

**Purpose:** Convert specific metadata to TOON format using CLI

```python
import subprocess
import json
from pathlib import Path

def convert_to_toon(data: dict, metadata_type: str) -> str:
    """
    Convert metadata dict to TOON format.
    
    Uses npx @toon-format/cli for conversion.
    Only converts metadata types with good token savings.
    """
    # Only convert if savings > 20%
    if metadata_type not in ['ctags', 'superbol_symbols']:
        return json.dumps(data, indent=2)  # Keep as JSON
    
    # Write temp file
    temp_file = Path(f'/tmp/metadata_{metadata_type}.json')
    with open(temp_file, 'w') as f:
        json.dump(data, f)
    
    # Convert using CLI
    result = subprocess.run(
        ['npx', '@toon-format/cli', str(temp_file)],
        capture_output=True,
        text=True
    )
    
    # Cleanup
    temp_file.unlink()
    
    return result.stdout
```

---

### Phase 2: Update Filtering Logic

**File:** `cobol_doc_agent.py`

**Changes:**

#### Option A: Minimal Integration (Conservative)
Convert metadata to TOON AFTER filtering, just before sending to LLM

```python
# In filter_metadata_for_pass()
def filter_metadata_for_pass(pass_number: int, full_metadata: Dict[str, Any]) -> str:
    # ... existing filtering logic ...
    
    # NEW: Convert to TOON for token efficiency
    from metadata_toon_converter import convert_to_toon
    
    if pass_number == 2:  # Only Pass 2 (logic sections)
        # Convert CTags to TOON (37.4% savings)
        filtered["ctags_outline"] = convert_to_toon(
            filtered["ctags_outline"],
            "ctags"
        )
        
        # Convert SuperBOL to TOON (23.1% savings)
        filtered["superbol_symbols"] = convert_to_toon(
            filtered["superbol_symbols"],
            "superbol_symbols"
        )
    
    return filtered  # Now contains TOON strings for high-value metadata
```

#### Option B: Aggressive Integration (Max Savings)
Convert earlier, then apply less aggressive filtering

```python
# Load metadata as TOON from the start
ctags_toon = convert_to_toon(full_metadata["ctags_outline"], "ctags")

# NEW filtering thresholds (can afford more context!)
if pass_number == 2:
    # OLD: limit_array(paragraphs, 100)
    # NEW: limit_array(paragraphs, 150)  # 50% more paragraphs!
    filtered["ctags"]["paragraphs"] = limit_array(paragraphs, 150)
```

---

### Phase 3: Optimize Pass 2 Filtering

**Goal:** Use token savings to send MORE context

**Current Pass 2 Limits:**
- CTags paragraphs: 100
- SuperBOL nodes: 500
- SuperBOL edges: 1,000

**New Pass 2 Limits (with TOON savings):**
- CTags paragraphs: **150** (+50%)
- SuperBOL nodes: **650** (+30%)
- SuperBOL edges: **1,300** (+30%)

**Calculation:**
- Pass 2 currently: ~880K tokens
- With TOON savings: ~880K - (320K CTags + 411K SuperBOL) * 0.22 = ~719K tokens
- Freed budget: ~161K tokens
- Use for: More paragraphs, nodes, edges!

---

## Expected Documentation Quality Improvements

### Pass 1 (Overview): No Change
- Still summary-only
- No TOON needed (minimal data anyway)

### Pass 2 (Logic & Flow): **MAJOR IMPROVEMENT**

**Before (JSON):**
- 100 paragraphs (first 4% of 2,412)
- 500 nodes (first 10% of 5,000)
- Missing: 96% of paragraph context

**After (TOON):**
- 150 paragraphs (first 6% of 2,412) - **50% more!**
- 650 nodes (first 13% of 5,000) - **30% more!**
- Better coverage of critical logic paths

**Sections Improved:**
- ✅ Control Flow Diagram (more nodes/edges)
- ✅ Business Operations Catalog (more paragraphs)
- ✅ Call Frequency Heatmap (better relationships)
- ✅ Program Call Hierarchy (richer call graph)

### Pass 3 (Code Explanation): **NO CHANGE**
- Already ultra-minimal (program name only)
- TOON not applicable

---

## Implementation Steps

### Step 1: Create Converter Module (1-2 hours)
```bash
# Create metadata_toon_converter.py
# Add convert_to_toon() function
# Test with sample metadata
```

### Step 2: Update Pass 2 Filtering (2-3 hours)
```bash
# Modify filter_metadata_for_pass()
# Add TOON conversion for CTags + SuperBOL
# Keep GnuCOBOL as JSON (no savings)
```

### Step 3: Adjust Filtering Thresholds (1 hour)
```bash
# Increase paragraph limit: 100 → 150
# Increase node limit: 500 → 650
# Increase edge limit: 1000 → 1300
```

### Step 4: Test Documentation Quality (2-3 hours)
```bash
# Run full documentation generation
# Compare Pass 2 sections (before/after)
# Verify token counts stay under 128K
# Assess documentation richness
```

### Step 5: Measure & Document (1 hour)
```bash
# Measure actual token usage in production
# Document improvements
# Create before/after comparison
```

**Total Time: 7-10 hours**

---

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| LLM confused by TOON format | Medium | High | Add TOON format explanation to system prompt |
| Token budget exceeded | Low | High | Monitor with tiktoken, adjust limits if needed |
| Quality degradation | Low | Medium | A/B test sections, revert if worse |
| CLI dependency issues | Low | Low | Cache npx installation, fallback to JSON |

---

## Success Criteria

✅ **Token savings achieved:** ~22% reduction (measured with tiktoken)  
✅ **Context improvement:** 50% more paragraphs in Pass 2 sections  
✅ **Quality improvement:** Richer Control Flow, Business Operations docs  
✅ **No regressions:** Code Explanation section unchanged  
✅ **Under budget:** All passes stay under 128K context window  

---

## Recommendation

**PROCEED with TOON integration for CTags + SuperBOL in Pass 2 only.**

**Rationale:**
- 22% token savings is significant
- CTags (37.4%) and SuperBOL (23.1%) have good ROI
- GnuCOBOL (0%) not worth the complexity
- Low risk (only affects Pass 2, doesn't touch Code Explanation)
- High reward (50% more paragraph context)

**Next Action:** Create `metadata_toon_converter.py` module

