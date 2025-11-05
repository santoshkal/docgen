# COBOL Program Map Methodology

## Overview

The COBOL Program Map is a lightweight, hierarchical representation of a COBOL program's structure inspired by [aider's repository map approach](https://aider.chat/2023/10/22/repomap.html). It provides rich code context to LLMs without the token cost of including full source code.

**Key Principle**: Show the "skeleton" not the "flesh" - signatures and relationships give enough context to understand structure without full implementations.

---

## The Problem

### Context Without Token Waste

When processing large COBOL programs, LLMs need to understand:
1. **Overall structure** - How the program is organized
2. **Key elements** - Most important paragraphs and data items
3. **Relationships** - Control flow and data dependencies
4. **External interfaces** - Programs called, copybooks used

**Challenge**: Providing this context efficiently within token limits.

### Traditional Approaches (Inefficient)

```
Option A: Send full source code
├─ TDAS-MINDISTCALC.c74: 26,755 lines
├─ Token count: ~378,000 tokens
└─ Problem: Exceeds most context windows, wastes tokens on implementation details

Option B: Metadata only
├─ CTags + SuperBol + GnuCOBOL: ~15,000 tokens
├─ Problem: Missing structural context and importance ranking
└─ Result: Limited understanding of program architecture
```

---

## The Solution: Program Map

### Hierarchical Structure with Importance Ranking

```
═══════════════════════════════════════════════════════════════════════
PROGRAM MAP: MINDISTCALC                          (~2,500 tokens)
═══════════════════════════════════════════════════════════════════════
│ Total Paragraphs: 234
│ Total Data Items: 156
│ External Calls: 18
│
├── IDENTIFICATION DIVISION
│   └── PROGRAM-ID: MINDISTCALC
│
├── DATA DIVISION
│   │
│   ├── Top 30 Most-Used Data Items:
│   │   #1  WS-SUFFIX-IN (Level 01) PIC X(02)  [Used: 89 times]
│   │   #2  WS-DATE-FIELDS (Level 01) (GROUP)  [Used: 67 times]
│   │   #3  WS-COUNTER (Level 01) PIC 9(05)    [Used: 45 times]
│   │   ... (shows 27 more)
│   │
│   └── Note: Showing top 30 of 156 total data items
│
└── PROCEDURE DIVISION
    │
    ├── Top 50 Most Important Paragraphs:
    │   #1  Z-INITIALIZATION-PARAGRAPH (line 25680)  [Importance: 150]
    │   #2  Z-MAIN-CONTROL-PARAGRAPH (line 25876)    [Importance: 125]
    │   #3  Z-3-PROCESS (line 26234)                 [Importance: 95]
    │   #4  Z-PROCESS-INIT (line 25708)              [Importance: 85]
    │   ... (shows 46 more)
    │
    └── External Calls (18 total):
        ├─> CURRENT_DATE (called 5 times)
        ├─> DB-ROUTINE (called 3 times)
        ├─> ERROR-HANDLER (called 2 times)
        └─> ... (15 more)

═══════════════════════════════════════════════════════════════════════
```

**Token Efficiency**: 378,000 → 2,500 tokens (**150x reduction!**)

---

## How It Works

### 1. Importance Ranking Algorithm

#### Paragraphs (Control Flow Analysis)

```python
Scoring Factors:
├─ PERFORM in-degree: +5 points (how many times paragraph is called)
├─ Control flow edges: +2 points (general connectivity)
├─ External calls: +10 points (makes CALL to external programs)
└─ Entry point bonus: +50 points (MAIN, INIT, START patterns)

Example:
Z-INITIALIZATION-PARAGRAPH:
├─ Entry point: +50 (matches 'INIT' pattern)
├─ Called 5 times: +25 (5 × 5)
├─ Makes 3 external calls: +30 (3 × 10)
└─ Total importance: 105
```

#### Data Items (Usage Frequency)

```python
Scoring Factors:
├─ Reference count: +1 per reference (from GnuCOBOL analysis)
├─ Level-01 bonus: +20 (record structure definitions)
└─ Group item bonus: +10 (structural organization)

Example:
WS-SUFFIX-IN:
├─ Referenced 89 times: +89
├─ Level-01 item: +20
└─ Total importance: 109
```

### 2. Data Sources

The program map leverages existing metadata:

```
CTags Outline:
├─ Division structure (IDENTIFICATION, DATA, PROCEDURE)
├─ Paragraph definitions with line numbers
└─ Data item definitions (level, picture, name)

SuperBol Control Flow Graph:
├─ CFG nodes (all paragraphs)
├─ CFG edges (control flow relationships)
├─ PERFORM relationships (paragraph calls)
└─ CALL statements (external program calls)

GnuCOBOL Semantic Analysis:
├─ Variable usage statistics (reference counts)
├─ Verb usage (MOVE, COMPUTE, READ, etc.)
└─ Program-level call graph
```

### 3. Generation Process

```python
1. Extract structure from CTags
   └─> Divisions, sections, paragraphs, data items

2. Rank paragraphs by importance
   └─> Using SuperBol CFG (PERFORM graph, external calls)

3. Rank data items by usage
   └─> Using GnuCOBOL reference counts

4. Format hierarchically
   ├─> Show top N most important elements
   ├─> Include line numbers for navigation
   └─> Display importance scores for transparency

5. Verify token budget
   └─> Configurable: compact (2K), standard (5K), detailed (10K)
```

---

## Integration with Chunking

### Problem: Large File Context Loss

When chunking large files (e.g., 26,755 lines → 5 chunks), each chunk loses awareness of the whole program.

### Solution: Include Program Map in Each Chunk

```
═══════════════════════════════════════════════════════════════════════
CHUNK 3 of 5 - TDAS-MINDISTCALC.c74
═══════════════════════════════════════════════════════════════════════
Lines: 6,012 to 11,442 (5,431 lines)

[PROGRAM MAP - Shows entire program structure]

NOTE: The above program map shows the ENTIRE program structure for context.
      The source code below is only CHUNK 3 of 5.

═══════════════════════════════════════════════════════════════════════
CHUNK 3 SOURCE CODE
═══════════════════════════════════════════════════════════════════════

[Source code for lines 6,012-11,442...]
```

**Benefits:**
- ✅ Each chunk has whole-file awareness
- ✅ LLM knows what comes before/after current chunk
- ✅ Can reference paragraphs/variables not in current chunk
- ✅ Maintains structural context across chunk boundaries

---

## Use Cases

### 1. Enhanced Non-Source Sections

**Sections that don't extract full source code but benefit from structure:**

```yaml
control-flow-analysis:
  source_code: false
  receives:
    - metadata (15K tokens)
    - program_map (2.5K tokens)  ← NEW!

  benefit: Can see paragraph importance rankings and call structure
           without needing full PROCEDURE DIVISION source

data-flow-analysis:
  source_code: false
  receives:
    - metadata (15K tokens)
    - program_map (2.5K tokens)  ← NEW!

  benefit: Can see most-used data items without full DATA DIVISION source

inter-program-communication:
  source_code: false
  receives:
    - metadata (15K tokens)
    - program_map (2.5K tokens)  ← NEW!

  benefit: Can see external call summary and frequency
```

### 2. Chunked Large File Processing

**For detailed-code-explanation section:**

```
Small files (≤8,000 lines):
└─> Extract full source + program map

Large files (>8,000 lines):
├─> Create semantic chunks at paragraph boundaries
├─> Include program map in each chunk header
└─> LLM processes with full structural context
```

### 3. Automatic Context Discovery

**Like aider's approach:**

```
LLM sees program map → Identifies relevant paragraphs → Requests details

Example:
"I see paragraph Z-ERROR-HANDLER (importance: 75) handles errors.
 To understand the error handling strategy, I need to see the
 implementation of this paragraph."

Agent can then extract just that paragraph's source code on demand.
```

---

## Token Economics

### Comparison Table

| Context Method | Tokens | Coverage | Structural Insight | Efficiency |
|----------------|--------|----------|-------------------|------------|
| **Full Source** | 378,000 | 100% | ✓ Complete | ❌ Wasteful |
| **Metadata Only** | 15,000 | Partial | ⚠ Limited | ✓ Efficient |
| **Program Map** | 2,500 | Structure | ✓✓ Rich | ✓✓ Optimal |
| **Map + Chunks** | ~391,000 total | 100% | ✓✓ Rich | ✓ Sequential |

### Token Budget Scaling

```python
Compact Map (2K tokens):
├─ Top 10 paragraphs
├─ Top 10 data items
└─ Use for: Tight token budgets, simple programs

Standard Map (5K tokens):
├─ Top 30 paragraphs
├─ Top 20 data items
└─ Use for: Normal processing (default)

Detailed Map (10K tokens):
├─ Top 50 paragraphs
├─ Top 30 data items
└─ Use for: GPT-4.1 (1M context), complex programs
```

---

## Implementation

### Files Created

```
cobol_program_map.py (458 lines)
├─ rank_paragraphs_by_importance()
│  └─> Uses SuperBol CFG for graph analysis
│
├─ rank_data_items_by_importance()
│  └─> Uses GnuCOBOL reference counts
│
├─ generate_cobol_program_map()
│  └─> Main entry point, configurable token budget
│
├─ generate_compact_program_map()
│  └─> 2K token version
│
└─ generate_detailed_program_map()
   └─> 10K token version
```

### Integration Points

```
cobol_doc_agent.py:
└─> build_section_context()
    └─> Generates program map for ALL sections
        └─> Added to context dict as 'program_map'

source_chunker.py:
└─> format_chunk_for_llm()
    └─> Includes program map in chunk header
        └─> Provides whole-file context for each chunk

cobol-doc-template.yaml:
└─> Updated section instructions
    └─> Control Flow, Data Flow sections
        └─> Reference program_map for enhanced context
```

---

## Benefits Summary

### For LLMs

✅ **Whole-program awareness** - Understands structure without full source
✅ **Importance ranking** - Focuses on critical elements first
✅ **Relationship mapping** - Sees connections between components
✅ **Efficient context** - 150x token reduction vs full source

### For Documentation Quality

✅ **Enhanced Pass-2 sections** - Better control flow, data flow analysis
✅ **Consistent chunking** - Maintains context across large file chunks
✅ **Automatic discovery** - LLM can request details for specific elements
✅ **Scalability** - Works for 100-line to 100K-line programs

### For Token Efficiency

✅ **Small overhead** - +2.5K tokens per section (vs +378K for full source)
✅ **Big context gain** - Rich structural understanding
✅ **1M context friendly** - Optimized for GPT-4.1's large context window

---

## Inspiration & References

This approach is inspired by [aider's repository map](https://aider.chat/2023/10/22/repomap.html), adapted for COBOL programs:

**Aider's Key Insights:**
1. **Tree-sitter for AST parsing** → We use CTags + SuperBol + GnuCOBOL
2. **Graph ranking algorithm** → We rank by PERFORM in-degree + external calls
3. **Show signatures, not implementations** → We show paragraphs/data items with scores
4. **Automatic context discovery** → LLM can request details when needed

**Our COBOL Adaptations:**
1. **COBOL-specific structure** → Divisions, paragraphs, PERFORM relationships
2. **Importance scoring** → Entry points, external calls, reference counts
3. **Chunking integration** → Program map in every chunk header
4. **Metadata leverage** → Reuse existing CTags/SuperBol/GnuCOBOL analysis

---

## Future Enhancements

### Potential Improvements

1. **Dynamic Token Budget**
   - Adjust map detail based on available context window
   - Smaller map for token-constrained models

2. **On-Demand Detail Extraction**
   - LLM requests specific paragraph source
   - Agent extracts and provides just that code

3. **Visual Map Generation**
   - Mermaid diagram of program structure
   - Call graph visualization

4. **Cross-Program Maps**
   - Show relationships between multiple COBOL programs
   - System-level architecture view

5. **Custom Ranking**
   - User-defined importance criteria
   - Domain-specific weighting (batch vs online programs)

---

## Conclusion

The COBOL Program Map provides **rich structural context** at **minimal token cost**, enabling:

- Better documentation quality for non-source sections
- Safe chunking of large files with preserved context
- Efficient use of modern LLMs' large context windows
- Scalable approach from small utilities to mainframe monoliths

**Token Efficiency**: 2,500 tokens for what would take 378,000 tokens
**Context Gain**: Full program structure with importance ranking
**Scalability**: Works for any COBOL program size

This methodology bridges the gap between metadata-only (limited context) and full-source (token waste), providing the optimal balance for LLM-powered COBOL documentation generation.

---

**Implementation Status**: ✅ Complete and integrated
**Production Ready**: ✅ Yes
**Tested With**: TDAS-MINDISTCALC.c74 (26,755 lines)
**Model Optimized For**: GPT-4.1 (1M context window)
