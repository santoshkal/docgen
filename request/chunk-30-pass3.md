# LLM Request Debug File
Generated: 2025-11-13T21:06:31.180042

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 30/55
- **Model**: gpt-4.1
- **Chunk Number**: 30
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~10,236 tokens
- **Total Input**: ~12,194 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 30/55" (ID: detailed-code-explanation)

CRITICAL REQUIREMENTS FOR CONSISTENCY:
1. Follow the template structure EXACTLY
2. Use ONLY information from the provided metadata - do not invent or assume
3. If metadata is missing, explicitly state "Information not available in metadata"
4. Use consistent formatting across all generated documents
5. Reference line numbers when available
6. For placeholders like {{program_name}}, replace with actual values
7. Generate valid Markdown syntax
8. For Mermaid diagrams, ensure valid syntax

TEMPLATE STRUCTURE TO FOLLOW:
The following analysis covers the entire source code sequentially, from the first line to the last.
Each numbered item represents a paragraph or logically grouped set of paragraphs that implement a single functionality.

{{comprehensive_code_explanations}}

---

## Chunk Completion Checklist

The following paragraphs were documented in this chunk:

{{paragraph_checklist}}


INSTRUCTION:
═══════════════════════════════════════════════════════════════════════════
⚠️  CRITICAL INSTRUCTIONS - READ CAREFULLY
═══════════════════════════════════════════════════════════════════════════

You will receive COBOL-74 source code from lines {{start_line}} to {{end_line}}.

🚨 YOUR MANDATORY TASK:
1. Return EVERY EXECUTABLE LINE in ```cobol code blocks with sequence numbers
2. Provide detailed explanations for each code section
3. Include self-assessment at the end

═══════════════════════════════════════════════════════════════════════════
📋 CODE INCLUSION RULES - ABSOLUTE REQUIREMENTS
═══════════════════════════════════════════════════════════════════════════

✅ ALWAYS INCLUDE (No Exceptions for Brevity or Repetition):
  • IDENTIFICATION DIVISION - ALL lines (PROGRAM-ID, AUTHOR, DATE-WRITTEN)
  • ENVIRONMENT DIVISION - ALL lines (FILE-CONTROL, SELECT statements)
  • DATA DIVISION - EVERY SINGLE LINE:
    → Every FD entry with complete record layouts
    → Every 01-level variable in WORKING-STORAGE
    → Every subordinate level (05, 10, 15, 77, 88)
    → Every FILLER definition (even if 1000+ repetitive ones)
    → Every PIC, VALUE, OCCURS, REDEFINES clause
    → Every data table entry (NO summarization allowed)
  • PROCEDURE DIVISION - EVERY SINGLE LINE:
    → Every paragraph/section definition
    → Every MOVE, PERFORM, IF, COMPUTE statement
    → Every period, condition, branch

═══════════════════════════════════════════════════════════════════════════
🚫 FORBIDDEN BEHAVIORS - WILL CAUSE VALIDATION FAILURE
═══════════════════════════════════════════════════════════════════════════

❌ NEVER use "Omitted for brevity"
   Bad:  "05 FILLER PIC X(10). ... (50 similar entries omitted)"
   Good: Show ALL 50 FILLER entries verbatim

❌ NEVER use "Similar pattern continues" or "Pattern repeats"
   Bad:  "05 FIELD-1 PIC 9(5). ... (pattern repeats 100 times)"
   Good: Show ALL 100 field definitions verbatim

❌ NEVER summarize repetitive code
   Bad:  "Multiple FILLER definitions follow..."
   Good: Include EVERY FILLER line with its sequence number

❌ NEVER skip sections you consider "boring" or "redundant"
   Bad:  Skipping 200 lines of data table entries
   Good: Include ALL 200 lines verbatim

❌ NEVER use ellipsis (...) to indicate omitted code
   Bad:  "05 FIELD-1 ... 05 FIELD-100"
   Good: Show FIELD-1, FIELD-2, ..., FIELD-100 (all 100 lines)

❌ NEVER skip lines because they look repetitive
   Bad:  "05 FILLER PIC X. (repeated 500 times)"
   Good: Show all 500 lines individually

═══════════════════════════════════════════════════════════════════════════
✅ VALIDATION CRITERIA - Your Output Will Be Automatically Checked
═══════════════════════════════════════════════════════════════════════════

Your code blocks will be validated against these requirements:

1. COMPLETE LINE COVERAGE:
   → Every executable line from {{start_line}} to {{end_line}} must appear in ```cobol blocks
   → Automated extraction of sequence numbers from your output
   → Missing even ONE executable line = VALIDATION FAILURE & RETRY

2. SEQUENCE NUMBER PRESERVATION:
   → Every line must include its 6-digit sequence number
   → Example: 003240 MOVE X TO Y.
   → This proves you didn't skip or summarize

3. NO SUMMARIZATION KEYWORDS:
   → Automated scan for: "omitted", "similar", "continues", "...", "repeats"
   → If found in code sections = VALIDATION FAILURE

4. COMPLETENESS VERIFICATION:
   → Expected executable lines: {{line_count}} minus comment lines
   → Your code blocks must contain this exact number
   → Coverage must be ≥95% of executable lines

═══════════════════════════════════════════════════════════════════════════
📝 REQUIRED OUTPUT FORMAT
═══════════════════════════════════════════════════════════════════════════

For each logical code block (paragraph, section, data group):

### Block N: [BLOCK-NAME] (Lines X-Y)

```cobol
[SEQUENCE#] [COMPLETE CODE LINE 1]
[SEQUENCE#] [COMPLETE CODE LINE 2]
... (show EVERY line - no skipping!)
[SEQUENCE#] [COMPLETE CODE LINE N]
```

**Purpose:**
[High-level summary of what this block does]

**Detailed Explanation:**
[Comprehensive explanation covering:]
- What the code does (functional purpose)
- Why it's structured this way (design rationale)
- How control flows through it (execution path)
- Important variables and their roles
- Conditional logic and branches
- Data transformations
- External interactions (CALL, PERFORM)
- Error handling (if any)

**Technical Details:**
- Variables used: [list]
- Called by: [caller info]
- Calls: [callee info]
- Side effects: [file I/O, state changes]

═══════════════════════════════════════════════════════════════════════════
📊 MANDATORY SELF-ASSESSMENT (Include at End of Response)
═══════════════════════════════════════════════════════════════════════════

After generating all code blocks, provide this self-assessment:

---

## Coverage Self-Assessment

**Code Blocks Generated:**
1. Block 1: [NAME] (Lines X-Y) - N lines
2. Block 2: [NAME] (Lines A-B) - M lines
... (list all blocks)

**Total Lines in My Code Blocks:** [NUMBER]

**Lines I Intentionally Excluded:**
- Comment lines (marked with * in column 7): [COUNT]
- Page breaks (marked with / in column 7): [COUNT]
- Total excluded: [NUMBER]

**My Calculation:**
- Source chunk contained: {{line_count}} total lines (lines {{start_line}}-{{end_line}})
- I included: [NUMBER] executable lines in my code blocks
- I excluded: [NUMBER] comment/page-break lines
- Expected executable: {{line_count}} - [excluded count]
- My self-assessed coverage: [NUMBER]%

⚠️ NOTE: This self-assessment will be verified programmatically.

---

═══════════════════════════════════════════════════════════════════════════
📌 CRITICAL REMINDERS
═══════════════════════════════════════════════════════════════════════════

1. ⚠️ NEVER abbreviate repetitive code for "readability"
2. ⚠️ NEVER assume pattern from first few lines
3. ⚠️ NEVER skip lines because they seem redundant
4. ⚠️ ALWAYS show complete data tables (even if 500+ lines)
5. ⚠️ ALWAYS include sequence numbers to prove coverage
6. ⚠️ VALIDATION WILL VERIFY: (Your lines / Expected lines) ≥ 95%

═══════════════════════════════════════════════════════════════════════════
🎯 Success Metric: Lines in your code blocks / Expected executable lines ≥ 95%
═══════════════════════════════════════════════════════════════════════════


**CHUNK 30 of 55**: Continue numbering from previous chunks.

OUTPUT FORMAT:
- Return ONLY the Markdown content for this section
- Include the section title as an H3 (###) for subsections
- Follow all formatting specified in the template
- Ensure Mermaid diagrams are wrapped in ```mermaid blocks
- For subsections, use H3 (###) headers

```

---

## User Prompt

```
Generate documentation for this section using the following metadata:

{
  "program_name": "TDAS-MINDISTCALC",
  "timestamp": "2025-11-13T19:58:35.744242",
  "superbol_symbols": {
    "program_id": null,
    "children": [],
    "paragraph_count": 0,
    "section_count": 0,
    "data_item_count": 0
  },
  "superbol_cfg": {
    "node_count": 25,
    "edge_count": 1890,
    "entry_points": 0,
    "complexity": 1867
  },
  "gnucobol_analysis": {
    "summary": {},
    "program_calls": [],
    "copybooks": [],
    "complexity_metrics": {}
  },
  "ctags_outline": {
    "program_name": null,
    "divisions": [],
    "total_paragraphs": 0,
    "total_sections": 0,
    "total_data_items": 0,
    "total_performs": 0,
    "sample_paragraphs": [],
    "sample_data_items": []
  },
  "chunked_file_info": {
    "type": "CHUNKED_FILE",
    "file_path": "../TDAS-MINDISTCALC.c74",
    "total_lines": 26755,
    "max_lines_per_chunk": 8000,
    "message": "File is too large (26,755 lines) for single-pass processing. Use chunked processing."
  },
  "program_map": "\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550",
  "source_code": "\n=============================================================================\nCHUNK 30 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 14253 to 14844 (592 lines)\nChunk Tokens (estimated): ~7,756\nActual Input Tokens: 9,162 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 14253-14844 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 30 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 30 of 55.\n\n\n=============================================================================\nCHUNK 30 SOURCE CODE (Lines 14253-14844)\n=============================================================================\n\n```cobol\n028514 Z-3-5-XIT.\n028516     MOVE 0 TO Z-EXIT-CODE.\n028518     MOVE 9999 TO Z-EXIT-LEVEL.\n028520     IF WS-BANK-OPT = 1\n028522         NEXT SENTENCE ELSE\n028524         GO TO Z-3-23-1-ELSE.\n028526     DISPLAY \"***PLEASE ENTER THE BANK NUMBER 9999 ***\".\n028528     ACCEPT WS-BANK-NO.\n028530     GO TO Z-3-23-ENDIF.\n028532 Z-3-23-1-ELSE.\n028534     IF WS-BANK-OPT = 2\n028536         NEXT SENTENCE ELSE\n028538         GO TO Z-3-23-2-ELSE.\n028540     MOVE SPACES TO WS-BANK-LIST.\n028542     DISPLAY \"***PLEASE ENTER UP TO 20 BANK NUMBERS***\".\n028544     DISPLAY \"***EXAMPLE - 0001000200030004...     ***\".\n028546     ACCEPT WS-BANK-LIST.\n028548 Z-3-23-2-ELSE.\n028550 Z-3-23-ENDIF.\n028552     MOVE ZEROS TO RMD-COUNT\n028554       , RMD-COUNT-INHERIT\n028556       , RMD-BK\n028558       , RMD-DC.\n028560     MOVE SPACES TO RMD-BK-NAME.\n028562     IF WS-BANK-OPT = 1\n028564         NEXT SENTENCE ELSE\n028566         GO TO Z-3-32-1-ELSE.\n028568     MOVE WS-BANK-NO TO PROC-BANK.\n028570************ PERFORM GET-BANK-INFO\n028572     PERFORM Z-4-PROCEDURE THRU Z-4-XIT.\n028574     IF Z-EXIT-PROCESS\n028576         MOVE 0 TO Z-EXIT-LEVEL\n028578         MOVE 2 TO Z-EXIT-CODE\n028580         GO TO Z-3-END.\n028582     IF  Z-EXIT-EDITEXIT\n028584         GO TO Z-3-XIT.\n028586     IF  Z-DMS2-ABORT-FLAG = 1\n028588         GO TO Z-3-XIT.\n028590     MOVE 0 TO Z-EXIT-CODE.\n028592     MOVE 9999 TO Z-EXIT-LEVEL.\n028594*\n028596************ PERFORM GET-ACCT-INFO\n028598     PERFORM Z-5-PROCEDURE THRU Z-5-XIT.\n028600     IF Z-EXIT-PROCESS\n028602         MOVE 0 TO Z-EXIT-LEVEL\n028604         MOVE 2 TO Z-EXIT-CODE\n028606         GO TO Z-3-END.\n028608     IF  Z-EXIT-EDITEXIT\n028610         GO TO Z-3-XIT.\n028612     IF  Z-DMS2-ABORT-FLAG = 1\n028614         GO TO Z-3-XIT.\n028616     MOVE 0 TO Z-EXIT-CODE.\n028618     MOVE 9999 TO Z-EXIT-LEVEL.\n028620*\n028622************ PERFORM CLOSE-FM-FILE-RPT\n028624     PERFORM Z-6-PROCEDURE THRU Z-6-XIT.\n028626     IF Z-EXIT-PROCESS\n028628         MOVE 0 TO Z-EXIT-LEVEL\n028630         MOVE 2 TO Z-EXIT-CODE\n028632         GO TO Z-3-END.\n028634     IF  Z-EXIT-EDITEXIT\n028636         GO TO Z-3-XIT.\n028638     IF  Z-DMS2-ABORT-FLAG = 1\n028640         GO TO Z-3-XIT.\n028642     MOVE 0 TO Z-EXIT-CODE.\n028644     MOVE 9999 TO Z-EXIT-LEVEL.\n028646*\n028648 Z-3-32-1-ELSE.\n028650     IF WS-BANK-OPT = 2\n028652         NEXT SENTENCE ELSE\n028654         GO TO Z-3-37-1-ELSE.\n028656     MOVE ZERO TO WS-BKSUB.\n028658     MOVE 1 TO Z-I-1.\n028660 Z-3-39-LOOP.\n028662     IF Z-I-1 > 20\n028664         GO TO Z-3-39-XIT.\n028666     MOVE 0 TO Z-EXIT-CODE.\n028668     MOVE 9999 TO Z-EXIT-LEVEL.\n028670     ADD 1 TO WS-BKSUB .\n028672********* EXIT WHEN\n028674     IF WS-BK-LNO (WS-BKSUB) = ZEROS\n028676        NEXT SENTENCE\n028678     ELSE\n028680        GO TO Z-3-41-EXIT-SKIP.\n028682     MOVE 1 TO Z-EXIT-LEVEL.\n028684     MOVE 1 TO Z-EXIT-CODE.\n028686     GO TO Z-3-39-END.\n028688 Z-3-41-EXIT-SKIP.\n028690     MOVE ZEROS TO RMD-COUNT\n028692       , RMD-COUNT-INHERIT\n028694       , RMD-BK\n028696       , RMD-DC\n028698       , WS-TIN-TOTALS.\n028700     MOVE ZEROS TO WS-1ST-TIME.\n028702     MOVE SPACES TO RMD-BK-NAME\n028704       , WS-FICHE-REQUEST.\n028706     MOVE SPACES TO WS-BK-RMD-ID (WS-BKSUB).\n028708     MOVE WS-BK-LNO (WS-BKSUB) TO WS-BANK-NO\n028710       , PROC-BANK.\n028712************ PERFORM GET-BANK-INFO\n028714     PERFORM Z-4-PROCEDURE THRU Z-4-XIT.\n028716     IF Z-EXIT-PROCESS\n028718         MOVE 0 TO Z-EXIT-LEVEL\n028720         MOVE 2 TO Z-EXIT-CODE\n028722         GO TO Z-3-39-END.\n028724     IF  Z-EXIT-EDITEXIT\n028726         GO TO Z-3-XIT.\n028728     IF  Z-DMS2-ABORT-FLAG = 1\n028730         GO TO Z-3-XIT.\n028732     IF  Z-EXIT-LEVEL < 0\n028734         GO TO Z-3-39-END.\n028736*\n028738************ PERFORM GET-ACCT-INFO\n028740     PERFORM Z-5-PROCEDURE THRU Z-5-XIT.\n028742     IF Z-EXIT-PROCESS\n028744         MOVE 0 TO Z-EXIT-LEVEL\n028746         MOVE 2 TO Z-EXIT-CODE\n028748         GO TO Z-3-39-END.\n028750     IF  Z-EXIT-EDITEXIT\n028752         GO TO Z-3-XIT.\n028754     IF  Z-DMS2-ABORT-FLAG = 1\n028756         GO TO Z-3-XIT.\n028758     IF  Z-EXIT-LEVEL < 0\n028760         GO TO Z-3-39-END.\n028762*\n028764     MOVE WS-DSTFM-ID TO WS-BK-RMD-ID (WS-BKSUB).\n028766************ PERFORM CLOSE-FM-FILE-RPT\n028768     PERFORM Z-6-PROCEDURE THRU Z-6-XIT.\n028770     IF Z-EXIT-PROCESS\n028772         MOVE 0 TO Z-EXIT-LEVEL\n028774         MOVE 2 TO Z-EXIT-CODE\n028776         GO TO Z-3-39-END.\n028778     IF  Z-EXIT-EDITEXIT\n028780         GO TO Z-3-XIT.\n028782     IF  Z-DMS2-ABORT-FLAG = 1\n028784         GO TO Z-3-XIT.\n028786     IF  Z-EXIT-LEVEL < 0\n028788         GO TO Z-3-39-END.\n028790*\n028792 Z-3-39-END.\n028794     IF Z-EDIT-ERROR\n028796         GO TO Z-3-XIT.\n028798 Z-3-39-SKIP.\n028800     IF Z-EXIT-LEVEL < 0\n028802         GO TO Z-3-39-XIT.\n028804     IF Z-EXIT-LEVEL < 1\n028806         GO TO Z-3-END.\n028808     IF Z-EXIT-CODE > 0\n028810         GO TO Z-3-39-XIT.\n028812     ADD 1 TO Z-I-1.\n028814     GO TO Z-3-39-LOOP.\n028816*\n028818 Z-3-39-XIT.\n028820     MOVE 0 TO Z-EXIT-CODE.\n028822     MOVE 9999 TO Z-EXIT-LEVEL.\n028824     IF WS-DSTFM-OPEN > 0\n028826         NEXT SENTENCE ELSE\n028828         GO TO Z-3-51-1-ELSE.\n028830     MOVE 0 TO WS-DSTFM-OPEN.\n028832*\n028834***********  CLOSE OF FILE DST-FILE-MAINT WITH CRUNCH\n028836*\n028838     IF Z-FLINFO5-OPEN NOT = 0\n028840         CLOSE DST-FILE-MAINT WITH CRUNCH\n028842         MOVE 0 TO Z-FLINFO5-OPEN\n028844         MOVE 0 TO Z-FLINFO5-RS-OPEN.\n028846     MOVE 1 TO WS-FM-OPS-DISP.\n028848 Z-3-51-1-ELSE.\n028850 Z-3-37-1-ELSE.\n028852     IF WS-BANK-OPT = 3\n028854         NEXT SENTENCE ELSE\n028856         GO TO Z-3-55-1-ELSE.\n028858*\n028860******* OPEN FILE PROC-FILE\n028862*\n028864     IF Z-FLINFO4-OPEN = 0\n028866         CHANGE ATTRIBUTE DEPENDENTSPECS OF PROC-FILE TO TRUE \n028868         OPEN INPUT PROC-FILE \n028870         IF ATTRIBUTE FILESTATE OF PROC-FILE = VALUE OPENED\n028872             MOVE ZEROS TO Z-FILE4-KEY\n028874             MOVE ZEROS TO Z-FLINFO4-RS-KEY\n028876             MOVE 1 TO Z-FLINFO4-OPEN\n028878             MOVE 1 TO Z-FLINFO4-RS-OPEN\n028880         ELSE\n028882             DISPLAY \">>> FILE PROC-FILE FAILED TO OPEN\"\n028884             MOVE ATTRIBUTE TITLE OF PROC-FILE TO                 \n028886                 Z-FL-EXCEPT-TITLE\n028888             DISPLAY \">>> OPEN FAIL, TITLE :\", Z-FL-EXCEPT-TITLE\n028890             DISPLAY \">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS\".\n028892*\n028894******* OPEN FILE PROC-FILE\n028896*\n028898     IF Z-FLINFO4-OPEN = 0\n028900         CHANGE ATTRIBUTE DEPENDENTSPECS OF PROC-FILE TO TRUE \n028902         OPEN INPUT PROC-FILE \n028904         IF ATTRIBUTE FILESTATE OF PROC-FILE = VALUE OPENED\n028906             MOVE ZEROS TO Z-FILE4-KEY\n028908             MOVE ZEROS TO Z-FLINFO4-RS-KEY\n028910             MOVE 1 TO Z-FLINFO4-OPEN\n028912             MOVE 1 TO Z-FLINFO4-RS-OPEN\n028914         ELSE\n028916             DISPLAY \">>> FILE PROC-FILE FAILED TO OPEN\"\n028918             MOVE ATTRIBUTE TITLE OF PROC-FILE TO                 \n028920                 Z-FL-EXCEPT-TITLE\n028922             DISPLAY \">>> OPEN FAIL, TITLE :\", Z-FL-EXCEPT-TITLE\n028924             DISPLAY \">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS\".\n028926     MOVE ZERO TO Z-FLINFO4-PRES.\n028928     MOVE ZERO TO Z-FLINFO4-SOME.\n028930     MOVE 3 TO Z-FLINFO4-LAST-SEQ.\n028932*\n028934 Z-3-57-LOOP.\n028936     MOVE ZERO TO Z-FLINFO4-PRES.\n028938*\n028940 Z-3-57-READ.\n028942     READ PROC-FILE RECORD \n028944         AT END\n028946         GO TO Z-3-57-XIT.\n028948     MOVE Z-FILE4-KEY TO Z-FLINFO4-RS-KEY.\n028950*\n028952     MOVE 1 TO Z-FLINFO4-PRES.\n028954     MOVE 1 TO Z-FLINFO4-SOME.\n028956     MOVE 1 TO Z-FLINFO4-MODIFY.\n028958     MOVE 0 TO Z-EXIT-CODE.\n028960     MOVE 9999 TO Z-EXIT-LEVEL.\n028962     MOVE ZEROS TO RMD-COUNT\n028964       , RMD-BK\n028966       , RMD-DC\n028968       , RMD-TOT-CHGD\n028970       , WS-TIN-TOTALS\n028972       , RMD-COUNT-INHERIT\n028974       , RMD-TOT-CHGD-INHERIT.\n028976     MOVE ZEROS TO WS-1ST-TIME.\n028978     MOVE SPACES TO RMD-BK-NAME\n028980       , WS-FICHE-REQUEST.\n028982     MOVE PROC-BANK TO WS-BANK-NO.\n028984     IF WS-CSTFM-OPEN = 0\n028986         NEXT SENTENCE ELSE\n028988         GO TO Z-3-62-1-ELSE.\n028990     MOVE PROCESS-DATE-MMDD TO WS-CSTFM-DT.\n028992     MOVE 000 TO WS-CSTFM-BK.\n028994     MOVE SPACES TO WS-CSTFM-SUFF-R.\n028996     MOVE WS-SUFFIX-IN TO WS-CSTFM-SUFF.\n028998*\n029000******* OPEN FILE CST-FILE-MAINT\n029002*\n029004     IF Z-FLINFO6-OPEN = 0\n029006         CHANGE ATTRIBUTE NEWFILE OF CST-FILE-MAINT TO VALUE TRUE\n029008         OPEN OUTPUT CST-FILE-MAINT \n029010         IF ATTRIBUTE FILESTATE OF CST-FILE-MAINT = VALUE OPENED\n029012             MOVE ZEROS TO Z-FILE6-KEY\n029014             MOVE ZEROS TO Z-FLINFO6-RS-KEY\n029016             MOVE 3 TO Z-FLINFO6-OPEN\n029018             MOVE 3 TO Z-FLINFO6-RS-OPEN\n029020         ELSE\n029022             DISPLAY \">>> FILE CST-FILE-MAINT FAILED TO OPEN\"\n029024             MOVE ATTRIBUTE TITLE OF CST-FILE-MAINT TO            \n029026                 Z-FL-EXCEPT-TITLE\n029028             DISPLAY \">>> OPEN FAIL, TITLE :\", Z-FL-EXCEPT-TITLE\n029030             DISPLAY \">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS\".\n029032     MOVE 1 TO WS-CSTFM-OPEN.\n029034 Z-3-62-1-ELSE.\n029036************ PERFORM GET-BANK-INFO\n029038     PERFORM Z-4-PROCEDURE THRU Z-4-XIT.\n029040     IF Z-EXIT-PROCESS\n029042         MOVE 0 TO Z-EXIT-LEVEL\n029044         MOVE 2 TO Z-EXIT-CODE\n029046         GO TO Z-3-57-END.\n029048     IF  Z-EXIT-EDITEXIT\n029050         GO TO Z-3-XIT.\n029052     IF  Z-DMS2-ABORT-FLAG = 1\n029054         GO TO Z-3-XIT.\n029056     IF  Z-EXIT-LEVEL < 0\n029058         GO TO Z-3-57-END.\n029060*\n029062************ PERFORM GET-ACCT-INFO\n029064     PERFORM Z-5-PROCEDURE THRU Z-5-XIT.\n029066     IF Z-EXIT-PROCESS\n029068         MOVE 0 TO Z-EXIT-LEVEL\n029070         MOVE 2 TO Z-EXIT-CODE\n029072         GO TO Z-3-57-END.\n029074     IF  Z-EXIT-EDITEXIT\n029076         GO TO Z-3-XIT.\n029078     IF  Z-DMS2-ABORT-FLAG = 1\n029080         GO TO Z-3-XIT.\n029082     IF  Z-EXIT-LEVEL < 0\n029084         GO TO Z-3-57-END.\n029086*\n029088************ PERFORM CLOSE-FM-FILE-RPT\n029090     PERFORM Z-6-PROCEDURE THRU Z-6-XIT.\n029092     IF Z-EXIT-PROCESS\n029094         MOVE 0 TO Z-EXIT-LEVEL\n029096         MOVE 2 TO Z-EXIT-CODE\n029098         GO TO Z-3-57-END.\n029100     IF  Z-EXIT-EDITEXIT\n029102         GO TO Z-3-XIT.\n029104     IF  Z-DMS2-ABORT-FLAG = 1\n029106         GO TO Z-3-XIT.\n029108     IF  Z-EXIT-LEVEL < 0\n029110         GO TO Z-3-57-END.\n029112*\n029114 Z-3-57-END.\n029116     IF Z-EDIT-ERROR\n029118         GO TO Z-3-XIT.\n029120 Z-3-57-SKIP.\n029122     IF Z-EXIT-LEVEL < 0\n029124         GO TO Z-3-57-XIT.\n029126     IF Z-EXIT-LEVEL < 1\n029128         GO TO Z-3-END.\n029130     IF Z-EXIT-CODE > 0\n029132         GO TO Z-3-57-XIT.\n029134 Z-3-RESTART-1.\n029136     MOVE 1 TO Z-RESTART-POINT.\n029138*\n029140     IF Z-DMS2-TRANS-STATE = 1\n029142         MOVE ZERO TO Z-RESTART-FOR-COUNT\n029144     ELSE\n029146         ADD 1 TO Z-RESTART-FOR-COUNT\n029148         IF  Z-RESTART-FOR-COUNT NOT < Z-RESTART-FOR-COUNT-LIMIT\n029150             MOVE ZERO TO Z-RESTART-FOR-COUNT\n029152             PERFORM Z-DMS2-BEGIN-TRANS\n029154                THRU Z-DMS2-BEGIN-TRANS-XIT\n029156             IF Z-DMS2-ABORT-FLAG = 1\n029158                 GO TO Z-3-XIT.\n029160     IF Z-DMS2-TRANS-STATE = 0\n029162         IF Z-DMS2-FOUND-LOCK = 1\n029164             PERFORM Z-DMS2-FREE\n029166                THRU Z-DMS2-FREE-XIT.\n029168     IF Z-DMS2-TRANS-STATE = 1\n029170         ADD 1 TO Z-RESTART-BY-COUNT\n029172         IF  Z-RESTART-BY-COUNT NOT < Z-RESTART-BY-COUNT-LIMIT\n029174             MOVE ZERO TO Z-RESTART-BY-COUNT\n029176             MOVE 2 TO Z-DMS2-ET-TYPE\n029178             PERFORM Z-DMS2-END-TRANS\n029180                THRU Z-DMS2-END-TRANS-XIT.\n029182     IF Z-DMS2-ABORT-FLAG = 1\n029184         GO TO Z-3-XIT.\n029186     GO TO Z-3-57-LOOP.\n029188*\n029190 Z-3-57-XIT.\n029192*\n029194     MOVE ZEROS TO Z-RESTART-BY-COUNT.\n029196     MOVE ZEROS TO Z-RESTART-FOR-COUNT.\n029198     IF Z-DMS2-TRANS-STATE = 0\n029200         IF Z-DMS2-FOUND-LOCK = 1\n029202             PERFORM Z-DMS2-FREE\n029204                THRU Z-DMS2-FREE-XIT.\n029206     IF Z-DMS2-TRANS-STATE = 1\n029208        MOVE 2 TO Z-DMS2-ET-TYPE\n029210        PERFORM Z-DMS2-END-TRANS\n029212           THRU Z-DMS2-END-TRANS-XIT\n029214        IF Z-DMS2-ABORT-FLAG = 1\n029216           GO TO Z-3-XIT.\n029218*\n029220*\n029222     MOVE 0 TO Z-EXIT-CODE.\n029224     MOVE 9999 TO Z-EXIT-LEVEL.\n029226     IF WS-DSTFM-OPEN > 0\n029228         NEXT SENTENCE ELSE\n029230         GO TO Z-3-72-1-ELSE.\n029232     MOVE 0 TO WS-DSTFM-OPEN.\n029234*\n029236***********  CLOSE OF FILE DST-FILE-MAINT WITH CRUNCH\n029238*\n029240     IF Z-FLINFO5-OPEN NOT = 0\n029242         CLOSE DST-FILE-MAINT WITH CRUNCH\n029244         MOVE 0 TO Z-FLINFO5-OPEN\n029246         MOVE 0 TO Z-FLINFO5-RS-OPEN.\n029248     MOVE 1 TO WS-FM-OPS-DISP.\n029250 Z-3-72-1-ELSE.\n029252     IF WS-CSTFM-OPEN > 0\n029254         NEXT SENTENCE ELSE\n029256         GO TO Z-3-76-1-ELSE.\n029258     MOVE 0 TO WS-CSTFM-OPEN.\n029260*\n029262***********  CLOSE OF FILE CST-FILE-MAINT WITH CRUNCH\n029264*\n029266     IF Z-FLINFO6-OPEN NOT = 0\n029268         CLOSE CST-FILE-MAINT WITH CRUNCH\n029270         MOVE 0 TO Z-FLINFO6-OPEN\n029272         MOVE 0 TO Z-FLINFO6-RS-OPEN.\n029274 Z-3-76-1-ELSE.\n029276     IF ( WS-FM-OPS-DISP = 1 ) OR ( WS-BANK-OPT = 3 )\n029278         NEXT SENTENCE ELSE\n029280         GO TO Z-3-79-1-ELSE.\n029282     DISPLAY \"**** CREATING BATCH FM RECORDS\".\n029284     DISPLAY \"WHEN MINDISTCALC PROGRAM IS COMPLETE\".\n029286     DISPLAY \"PLEASE RUN BR0080 PROGRAM \".\n029288     DISPLAY \"TO LOAD TDA FM FILE(S): \".\n029290     DISPLAY \"                        \".\n029292     IF ( WS-FM-OPS-DISP = 1 ) AND ( WS-BANK-OPT = 1 OR 3 )\n029294         NEXT SENTENCE\n029296     ELSE\n029298         GO TO Z-3-85-DISPLAY.\n029300     DISPLAY WS-DSTFM-ID.\n029302 Z-3-85-DISPLAY.\n029304     IF WS-BANK-OPT = 2\n029306         NEXT SENTENCE ELSE\n029308         GO TO Z-3-86-1-ELSE.\n029310     MOVE ZERO TO WS-BKSUB.\n029312     MOVE 1 TO Z-I-2.\n029314 Z-3-88-LOOP.\n029316     IF Z-I-2 > 20\n029318         GO TO Z-3-88-XIT.\n029320     MOVE 0 TO Z-EXIT-CODE.\n029322     MOVE 9999 TO Z-EXIT-LEVEL.\n029324     ADD 1 TO WS-BKSUB .\n029326********* EXIT WHEN\n029328     IF WS-BK-LNO (WS-BKSUB) = ZEROS\n029330        NEXT SENTENCE\n029332     ELSE\n029334        GO TO Z-3-90-EXIT-SKIP.\n029336     MOVE 1 TO Z-EXIT-LEVEL.\n029338     MOVE 1 TO Z-EXIT-CODE.\n029340     GO TO Z-3-88-END.\n029342 Z-3-90-EXIT-SKIP.\n029344     IF WS-BK-RMD-ID (WS-BKSUB) > SPACES\n029346         NEXT SENTENCE ELSE\n029348         GO TO Z-3-91-1-ELSE.\n029350     DISPLAY WS-DSTFM-ID.\n029352 Z-3-91-1-ELSE.\n029354 Z-3-88-END.\n029356     IF Z-EDIT-ERROR\n029358         GO TO Z-3-XIT.\n029360 Z-3-88-SKIP.\n029362     IF Z-EXIT-LEVEL < 0\n029364         GO TO Z-3-88-XIT.\n029366     IF Z-EXIT-LEVEL < 1\n029368         GO TO Z-3-END.\n029370     IF Z-EXIT-CODE > 0\n029372         GO TO Z-3-88-XIT.\n029374     ADD 1 TO Z-I-2.\n029376     GO TO Z-3-88-LOOP.\n029378*\n029380 Z-3-88-XIT.\n029382     MOVE 0 TO Z-EXIT-CODE.\n029384     MOVE 9999 TO Z-EXIT-LEVEL.\n029386 Z-3-86-1-ELSE.\n029388     IF WS-BANK-OPT = 3\n029390         NEXT SENTENCE\n029392     ELSE\n029394         GO TO Z-3-93-DISPLAY.\n029396     DISPLAY WS-CSTFM-ID.\n029398 Z-3-93-DISPLAY.\n029400     DISPLAY \"                        \".\n029402     DISPLAY \"AX BLANK TO CONTINUE.\".\n029404     ACCEPT WS-ACCEPT.\n029406 Z-3-79-1-ELSE.\n029408 Z-3-55-1-ELSE.\n029410 Z-3-END.\n029412     IF Z-EDIT-ERROR\n029414         GO TO Z-3-XIT.\n029416 Z-3-SKIP.\n029418     MOVE 0 TO Z-EXIT-CODE.\n029420     MOVE 9999 TO Z-EXIT-LEVEL.\n029422*\n029424*\n029426     MOVE ZEROS TO Z-RESTART-BY-COUNT.\n029428     MOVE ZEROS TO Z-RESTART-FOR-COUNT.\n029430     IF Z-DMS2-TRANS-STATE = 0\n029432         IF Z-DMS2-FOUND-LOCK = 1\n029434             PERFORM Z-DMS2-FREE\n029436                THRU Z-DMS2-FREE-XIT.\n029438     IF Z-DMS2-TRANS-STATE = 1\n029440        MOVE 2 TO Z-DMS2-ET-TYPE\n029442        PERFORM Z-DMS2-END-TRANS\n029444           THRU Z-DMS2-END-TRANS-XIT\n029446        IF Z-DMS2-ABORT-FLAG = 1\n029448           GO TO Z-3-XIT.\n029450*\n029452*\n029454     GO TO Z-3-XIT.\n029456*\n029458 Z-3-RESTART.\n029460     IF Z-RESTART-POINT = ZERO\n029462         GO TO Z-3-PROCESS.\n029464     IF Z-RESTART-POINT = 1\n029466         GO TO Z-3-RESTART-1.\n029468*\n029470 Z-3-XIT.\n029472     EXIT.\n029474*\n029476*****************************************************************\n029478*    PROCEDURE PRT-LABEL-CHECK\n029480*****************************************************************\n029482 Z-7-PROCEDURE.\n029484*\n029486*L\"S\"/\"GEN.L\"/\"PRINTER-PR\".                                       \n029488*=================================================================\n029490*                          PRINT ROUTINE                          \n029492*=================================================================\n029494*   FILENAME SETUP:                                               \n029496*     MOVE PACK-ID TO \"GWS-PACK\"                                  \n029498*     MOVE APPLICATION TO \"GWS-APPL\"                              \n029500*     MOVE NO OF PART PAPER TO \"GWS-NO-PARTS\"                     \n029502*     MOVE REPORT DESCRIPTOR TO \"GWS-PRT-DESCRIPTOR\"              \n029504*     MOVE CSI BRANCH CODE TO \"GWS-BRANCH-CODE\"                   \n029506*     MOVE NO OF MICROFICHE COPIES TO \"GWS-MICROFICHE-CODE\"       \n029508*     MOVE BANK NUMBER TO \"GWS-BANK-NUMBER\"                       \n029510*     MOVE SPACES TO \"GWS-TIME\" IF TIME NOT DESIRED ELSE MOVE ZERO\n029512*     MOVE 1 TO GWS-TIME-CTL IF GWS-TIME IS NOT TO USED FOR TIME  \n029514*     IF NONE OF THE ABOVE IS SET DEFAULTS WILL TAKE PLACE        \n029516*     PERFORM \"99-PRT-LABEL-CHECK\" - ROUTINE WILL EDIT            \n029518*        \"GWS-PRINT-LABEL\", AND IF DIFFERENT FROM CURRENT PRINT   \n029520*        FILE, CLOSE PRINT FILE, AND MOVE \"GWS-PRINT-LABEL\" TO    \n029522*        \"ID-PRT\" OR \"ID-PRT74\" IF \"COBOL74-CODE\" = 1; ALSO ALLOWS\n029524*        OPERATOR TO DESIGNATE PACK NAME IF SW3 = 1               \n029526*                                                                 \n029528*     TO USE LONG PRINTFILE NAMES:                                \n029530*        MOVE 1 TO \"GWS-LONG-PRTNAMES\" FOR PRT/ PREFIX LEVEL      \n029532*        MOVE 2 TO \"GWS-LONG-PRTNAMES\" FOR EOM/ PREFIX LEVEL      \n029534*        MOVE 3 TO \"GWS-LONG-PRTNAMES\" FOR EOY/ PREFIX LEVEL      \n029536*        MOVE 2-DIGIT NUMERIC CSI DATA CENTER TO \"GWS-CSI-DC\"     \n029538*        MOVE 3-DIGIT NUMERIC BANK NUMBER TO \"GWS-CSI-BK\"         \n029540*        EXAMPLE OF LONG FILENAME:                                \n029542*            PRT/00/101/DDA0P1SP00/0000123456                     \n029544*                                                                 \n029546*     REMOTE PRINT FILE NAME SETUP                                \n029548*        TO USE THE REMOTE PRINT NAME SETUP, COPY IN THE GENERAL  \n029550*        LIBRARY 'GEN.L/RMTPRTLBL'                                \n029552*        MOVE A '1' TO GWS-RMT-PRT-OPTION                         \n029554*        MOVE IN THE FILE NAME EXTENSION IF OTHER THAN 000        \n029556*          TO GWS-RMT-EXT                                         \n029558*        IN THE COPY STATEMENT USE THE COPY REPLACING             \n029560*          TO REPLACE 'PERFORM 99-PRT-REMOTE-LBL-CHK'             \n029562*          WITH 'PERFORM 99-PRT-RMT-LBL-CHK'.                     \n029564*        TO USE THE REMOTE FILE NAME SETUP, THE BANK FILE SPECS   \n029566*          MUST ALSO BE COPIED IN AS AN FD 'GEN.L/DC-FD.C'        \n029568*                                                                 \n029570*     TO USE NEW LONG PRINTFILE NAMES FOR EOM:                    \n029572*        MOVE 1 TO GWS-LONG-PRTNAMES-NEW                          \n029574*        MOVE CENTERVIEW CODE TO GWS-CNTR-VIEW (SPEC-CENTERVIEW)  \n029576*        MOVE NEW EOM PRINT TO GWS-PRT-NEW  (SPEC-PRT-NEW)        \n029578*        EXAMPLE OF NEW EOM LONG FILENAME:                        \n029580*            PRINT/00/DDA/01SP/0101/CR00/25DSP847                 \n029582*                                                                 \n029584*   SINGLE SPACE - PERFORM \"99-PRT1\"                              \n029586*   DOUBLE SPACE - PERFORM \"99-PRT2\"                              \n029588*   MULTI  SPACE - MOVE NUMBER TO \"NO-LINES\"; PERFORM \"99-PRT-MUL\"\n029590*                                                                 \n029592*   HEADER PRT: MOVE HEADING INFORMATION TO \"HEADER-LINE[1,2,3,4, \n029594*     OR 5] DEPENDING ON HOW MANY LINE(S) ARE NEEDED; MOVE NUMBER \n029596*     OF HEADING LINE(S) TO BE PRINTED TO \"HDR-CTL\"; ROUTINE WILL \n029598*     AUTOMATICALLY SKIP A LINE  AFTER LAST HEADER-LINE  PRINTED; \n029600*     MOVE NUMBER OF LINES/PAGE TO \"END-PAGE\"(DEFAULT IS 58 -LINE \n029602*     COUNT BEGINS WITH FIRST HEADER LINE); MOVE 0 TO \"PAGE-CTR\"; \n029604*     PERFORM \"99-HDR-PRT\" (NEED ONLY BE PERFORM ONCE BEFORE EACH \n029606*     NEW REPORT);  PRINT ROUTINE  DEFAULTS  TO BYPASSING HEADING \n029608*     PRINT ROUTINE IF VALUE IS NOT SET IN \"HDR-CTL\".             \n029610*     RECOMMENDED HEADER-LINE1 FORMAT:                            \n029612*       MOVE CSI BRANCH CODE TO \"H-CSI-BR-NO\"                     \n029614*       MOVE BANK NUMBER     TO \"H-BANK-NO\"                       \n029616*       MOVE BANK NAME       TO \"H-BANK-NAME\"                     \n029618*       MOVE NAME OF REPORT  TO \"H-REPORT-TITLE\"                  \n029620*       MOVE REPORT NUMBER   TO \"H-REPORT-NO\"                     \n029622*       MOVE DAY OF WEEK     TO \"H-DAY-WEEK\"                      \n029624*       MOVE DATE            TO \"H-DATE\"                          \n029626*       MOVE TIME            TO \"H-HHMM\"                          \n029628*                                                                 \n029630*   TEAR PAGES: MOVE \"DATA\" 8 BY 3 LINES TO \"TEAR-PAGE-IN\"        \n029632*     PERFORM \"99-TEAR-PAGES\".                                    \n029634*     MOVE ZERO TO \"TP-SKIP\" IF NO SKIP TO 1 BEFORE PRINT.        \n029636*     RECOMMENDED TEAR-PAGE FORMAT:                               \n029638*       MOVE BANK NUMBER TO \"TP-LN-BKNO\"                          \n029640*       MOVE DATE        TO \"TP-LN-DATE\"                          \n029642*       MOVE APPLICATION TO TP-LN3 (OPTIONAL).                    \n029644*                                                                 \n029646*   EXCEPTION PRINT RECORDS:                                      \n029648*    RECOMMENDED FORMAT:                                          \n029650*        BANK NO                                                  \n029652*        ACCOUNT NUMBER                                           \n029654*        GWS-PRT-EXCEPT-LINE - THIS DATA NAME IS A GROUP ITEM     \n029656*         (BLOCK NO /97/ HEADER LINE /98/ DETAIL LINE             \n029658*          PAGE CONTROL                                           \n029660*          NO OF LINES TO SPACES AFTER PRINTING                   \n029662*          PRINT DATA                                  )          \n029664*    CREATE: MOVE \"C\" TO GWS-PRT-EXC-FLAG.                        \n029666*    (PROGRAMMING NOTE: ADD THESE STATEMENTS IMMEDIATELY FOLLOWING\n029668*      THE COPY PRINTER PROCEDURE LIBRARY)                        \n029670*      MOVE GWS-PRT-EXCEPT-LINE TO (YOUR EXCEPT RECORD FOLLOWING  \n029672*                                   THE ACCOUNT NUMBER).          \n029674*      PERFORM (YOUR WRITE EXCEPTION ROUTINE).                    \n029676*    PRINT: MOVE \"P\" TO GWS-PRT-EXC-FLAG.                         \n029678*      MOVE (YOUR EXCEPTION REC FOLLOWING TO GWS-PRT-EXCEPT-LINE. \n029680*            THE ACCOUNT NUMBER)                                  \n029682*      PERFORM 99-PRT1.                                           \n029684*    CANCEL: MOVE SPACE TO GWS-PRT-EXC-FLAG.                      \n029686*=================================================================\n029688 PRT SECTION 00.                                                  \n029690*=================================================================\n029692*                 PRINTER FILENAME SETUP ROUTINE                  \n029694*=================================================================\n029696 99-PRT-LABEL-CHECK SECTION 51.                                   \n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 592 lines from 14253 to 14844.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 30,
  "total_chunks": 55,
  "start_line": 14253,
  "end_line": 14844,
  "line_count": 592
}

Remember:
- Program name: TDAS-MINDISTCALC
- Follow template structure exactly
- Be consistent in terminology and formatting
- Reference line numbers from metadata
- Generate valid Markdown and Mermaid syntax

```

---

## Context (Metadata)

The following context was provided in the user prompt (embedded in JSON):

### Source Code Present
- Has source_code: Yes
- Source code length: 31287 characters

### Program Map Present
- Has program_map: Yes
- Program map length: 3219 characters

### Other Context Keys
- program_name: str
- timestamp: str
- superbol_symbols: dict
- superbol_cfg: dict
- gnucobol_analysis: dict
- ctags_outline: dict
- chunked_file_info: dict
- chunk_number: int
- total_chunks: int
- start_line: int
- end_line: int
- line_count: int

---

## Full Source Code (if present)


```cobol

=============================================================================
CHUNK 30 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 14253 to 14844 (592 lines)
Chunk Tokens (estimated): ~7,756
Actual Input Tokens: 9,162 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 14253-14844 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 30 of 55 chunks
- Continue numbering sequentially from previous chunks
- If this is chunk 1, start numbering from 1
- If this is chunk 2+, continue from where the previous chunk ended
- Parse EVERY line in this chunk - do not skip any content
- Group paragraphs ONLY when they implement a single functionality
- Provide completion checklist at end listing all documented paragraphs
=============================================================================


════════════════════════════════════════════════════════════════════════════════
PROGRAM MAP: TDAS-MINDISTCALC
════════════════════════════════════════════════════════════════════════════════
│
│ Total Paragraphs: 0
│ Total Data Items: 0
│ External Calls: 21
│
├── IDENTIFICATION DIVISION
│   └── PROGRAM-ID: TDAS-MINDISTCALC
│
└── PROCEDURE DIVISION
    │
    ├── Top 50 Most Important Paragraphs:
    │   # 1  Z-35-2-ENDIF  [Importance: 646]
    │   # 2  Z-DMS-EXCEPTION  [Importance: 210]
    │   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]
    │   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]
    │   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]
    │   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]
    │   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]
    │   # 8  030040*L"S"/"GENL"/"RMTPRTLBL"  [Importance: 80]
    │   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]
    │   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]
    │   #11  Z-5-XIT  [Importance: 58]
    │   #12  CALCULATIONS  [Importance: 56]
    │   #13  Z-DATE-CALC-Y  [Importance: 56]
    │   #14  Z-DATE-CALC-C  [Importance: 56]
    │   #15  Z-FL-EXCEPTION  [Importance: 56]
    │   #16  TPR-WRITE-TEAR  [Importance: 56]
    │   #17  Z-29-PROCEDURE  [Importance: 56]
    │   #18  Z-3-XIT  [Importance: 56]
    │   #19  032926********ENDIF  [Importance: 40]
    │   #20  033256********ENDIF  [Importance: 40]
    │   #21  Z-DMS2-END-TRANS  [Importance: 37]
    │   #22  Z-DMS2-FREE  [Importance: 35]
    │   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]
    │   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]
    │   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]
    │   #26  TPR-TEAR-PAGES  [Importance: 28]
    │   #27  Z-21-PROCEDURE  [Importance: 28]
    │   #28  Z-DATE-YY-DIFF  [Importance: 28]
    │   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]
    │   #30  SETUP-NEW-REPORT  [Importance: 28]
    │   #31  Z-21-XIT  [Importance: 26]
    │   #32  Z-5-14-END  [Importance: 24]
    │   #33  Z-30-XIT  [Importance: 22]
    │   #34  Z-OPEN-DB-2  [Importance: 21]
    │   #35  GET-BANK-INFO  [Importance: 21]
    │   #36  Z-4-PROCEDURE  [Importance: 21]
    │   #37  GET-ACCT-INFO  [Importance: 21]
    │   #38  Z-5-PROCEDURE  [Importance: 21]
    │   #39  CLOSE-FM-FILE-RPT  [Importance: 21]
    │   #40  Z-6-PROCEDURE  [Importance: 21]
    │   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]
    │   #42  HEADING-SETUP  [Importance: 21]
    │   #43  Z-16-PROCEDURE  [Importance: 21]
    │   #44  000026*REMARKS  [Importance: 20]
    │   #45  033774*****ENDIF  [Importance: 20]
    │   #46  Z-11-XIT  [Importance: 18]
    │   #47  Z-22-XIT  [Importance: 18]
    │   #48  99-NEW-END  [Importance: 16]
    │   #49  Z-PROCESS-INIT  [Importance: 14]
    │   #50  Z-OPEN-DB-1  [Importance: 14]
    │
    └── External Calls (21 total):
        ├─> CURRENT_DATE OF GENERALSUPPORT (called 16 times)
        ├─> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)
        ├─> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)
        ├─> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)

════════════════════════════════════════════════════════════════════════════════
Map Token Count: ~779
════════════════════════════════════════════════════════════════════════════════

NOTE: The above program map shows the ENTIRE program structure for context.
      The source code below is only CHUNK 30 of 55.


=============================================================================
CHUNK 30 SOURCE CODE (Lines 14253-14844)
=============================================================================

```cobol
028514 Z-3-5-XIT.
028516     MOVE 0 TO Z-EXIT-CODE.
028518     MOVE 9999 TO Z-EXIT-LEVEL.
028520     IF WS-BANK-OPT = 1
028522         NEXT SENTENCE ELSE
028524         GO TO Z-3-23-1-ELSE.
028526     DISPLAY "***PLEASE ENTER THE BANK NUMBER 9999 ***".
028528     ACCEPT WS-BANK-NO.
028530     GO TO Z-3-23-ENDIF.
028532 Z-3-23-1-ELSE.
028534     IF WS-BANK-OPT = 2
028536         NEXT SENTENCE ELSE
028538         GO TO Z-3-23-2-ELSE.
028540     MOVE SPACES TO WS-BANK-LIST.
028542     DISPLAY "***PLEASE ENTER UP TO 20 BANK NUMBERS***".
028544     DISPLAY "***EXAMPLE - 0001000200030004...     ***".
028546     ACCEPT WS-BANK-LIST.
028548 Z-3-23-2-ELSE.
028550 Z-3-23-ENDIF.
028552     MOVE ZEROS TO RMD-COUNT
028554       , RMD-COUNT-INHERIT
028556       , RMD-BK
028558       , RMD-DC.
028560     MOVE SPACES TO RMD-BK-NAME.
028562     IF WS-BANK-OPT = 1
028564         NEXT SENTENCE ELSE
028566         GO TO Z-3-32-1-ELSE.
028568     MOVE WS-BANK-NO TO PROC-BANK.
028570************ PERFORM GET-BANK-INFO
028572     PERFORM Z-4-PROCEDURE THRU Z-4-XIT.
028574     IF Z-EXIT-PROCESS
028576         MOVE 0 TO Z-EXIT-LEVEL
028578         MOVE 2 TO Z-EXIT-CODE
028580         GO TO Z-3-END.
028582     IF  Z-EXIT-EDITEXIT
028584         GO TO Z-3-XIT.
028586     IF  Z-DMS2-ABORT-FLAG = 1
028588         GO TO Z-3-XIT.
028590     MOVE 0 TO Z-EXIT-CODE.
028592     MOVE 9999 TO Z-EXIT-LEVEL.
028594*
028596************ PERFORM GET-ACCT-INFO
028598     PERFORM Z-5-PROCEDURE THRU Z-5-XIT.
028600     IF Z-EXIT-PROCESS
028602         MOVE 0 TO Z-EXIT-LEVEL
028604         MOVE 2 TO Z-EXIT-CODE
028606         GO TO Z-3-END.
028608     IF  Z-EXIT-EDITEXIT
028610         GO TO Z-3-XIT.
028612     IF  Z-DMS2-ABORT-FLAG = 1
028614         GO TO Z-3-XIT.
028616     MOVE 0 TO Z-EXIT-CODE.
028618     MOVE 9999 TO Z-EXIT-LEVEL.
028620*
028622************ PERFORM CLOSE-FM-FILE-RPT
028624     PERFORM Z-6-PROCEDURE THRU Z-6-XIT.
028626     IF Z-EXIT-PROCESS
028628         MOVE 0 TO Z-EXIT-LEVEL
028630         MOVE 2 TO Z-EXIT-CODE
028632         GO TO Z-3-END.
028634     IF  Z-EXIT-EDITEXIT
028636         GO TO Z-3-XIT.
028638     IF  Z-DMS2-ABORT-FLAG = 1
028640         GO TO Z-3-XIT.
028642     MOVE 0 TO Z-EXIT-CODE.
028644     MOVE 9999 TO Z-EXIT-LEVEL.
028646*
028648 Z-3-32-1-ELSE.
028650     IF WS-BANK-OPT = 2
028652         NEXT SENTENCE ELSE
028654         GO TO Z-3-37-1-ELSE.
028656     MOVE ZERO TO WS-BKSUB.
028658     MOVE 1 TO Z-I-1.
028660 Z-3-39-LOOP.
028662     IF Z-I-1 > 20
028664         GO TO Z-3-39-XIT.
028666     MOVE 0 TO Z-EXIT-CODE.
028668     MOVE 9999 TO Z-EXIT-LEVEL.
028670     ADD 1 TO WS-BKSUB .
028672********* EXIT WHEN
028674     IF WS-BK-LNO (WS-BKSUB) = ZEROS
028676        NEXT SENTENCE
028678     ELSE
028680        GO TO Z-3-41-EXIT-SKIP.
028682     MOVE 1 TO Z-EXIT-LEVEL.
028684     MOVE 1 TO Z-EXIT-CODE.
028686     GO TO Z-3-39-END.
028688 Z-3-41-EXIT-SKIP.
028690     MOVE ZEROS TO RMD-COUNT
028692       , RMD-COUNT-INHERIT
028694       , RMD-BK
028696       , RMD-DC
028698       , WS-TIN-TOTALS.
028700     MOVE ZEROS TO WS-1ST-TIME.
028702     MOVE SPACES TO RMD-BK-NAME
028704       , WS-FICHE-REQUEST.
028706     MOVE SPACES TO WS-BK-RMD-ID (WS-BKSUB).
028708     MOVE WS-BK-LNO (WS-BKSUB) TO WS-BANK-NO
028710       , PROC-BANK.
028712************ PERFORM GET-BANK-INFO
028714     PERFORM Z-4-PROCEDURE THRU Z-4-XIT.
028716     IF Z-EXIT-PROCESS
028718         MOVE 0 TO Z-EXIT-LEVEL
028720         MOVE 2 TO Z-EXIT-CODE
028722         GO TO Z-3-39-END.
028724     IF  Z-EXIT-EDITEXIT
028726         GO TO Z-3-XIT.
028728     IF  Z-DMS2-ABORT-FLAG = 1
028730         GO TO Z-3-XIT.
028732     IF  Z-EXIT-LEVEL < 0
028734         GO TO Z-3-39-END.
028736*
028738************ PERFORM GET-ACCT-INFO
028740     PERFORM Z-5-PROCEDURE THRU Z-5-XIT.
028742     IF Z-EXIT-PROCESS
028744         MOVE 0 TO Z-EXIT-LEVEL
028746         MOVE 2 TO Z-EXIT-CODE
028748         GO TO Z-3-39-END.
028750     IF  Z-EXIT-EDITEXIT
028752         GO TO Z-3-XIT.
028754     IF  Z-DMS2-ABORT-FLAG = 1
028756         GO TO Z-3-XIT.
028758     IF  Z-EXIT-LEVEL < 0
028760         GO TO Z-3-39-END.
028762*
028764     MOVE WS-DSTFM-ID TO WS-BK-RMD-ID (WS-BKSUB).
028766************ PERFORM CLOSE-FM-FILE-RPT
028768     PERFORM Z-6-PROCEDURE THRU Z-6-XIT.
028770     IF Z-EXIT-PROCESS
028772         MOVE 0 TO Z-EXIT-LEVEL
028774         MOVE 2 TO Z-EXIT-CODE
028776         GO TO Z-3-39-END.
028778     IF  Z-EXIT-EDITEXIT
028780         GO TO Z-3-XIT.
028782     IF  Z-DMS2-ABORT-FLAG = 1
028784         GO TO Z-3-XIT.
028786     IF  Z-EXIT-LEVEL < 0
028788         GO TO Z-3-39-END.
028790*
028792 Z-3-39-END.
028794     IF Z-EDIT-ERROR
028796         GO TO Z-3-XIT.
028798 Z-3-39-SKIP.
028800     IF Z-EXIT-LEVEL < 0
028802         GO TO Z-3-39-XIT.
028804     IF Z-EXIT-LEVEL < 1
028806         GO TO Z-3-END.
028808     IF Z-EXIT-CODE > 0
028810         GO TO Z-3-39-XIT.
028812     ADD 1 TO Z-I-1.
028814     GO TO Z-3-39-LOOP.
028816*
028818 Z-3-39-XIT.
028820     MOVE 0 TO Z-EXIT-CODE.
028822     MOVE 9999 TO Z-EXIT-LEVEL.
028824     IF WS-DSTFM-OPEN > 0
028826         NEXT SENTENCE ELSE
028828         GO TO Z-3-51-1-ELSE.
028830     MOVE 0 TO WS-DSTFM-OPEN.
028832*
028834***********  CLOSE OF FILE DST-FILE-MAINT WITH CRUNCH
028836*
028838     IF Z-FLINFO5-OPEN NOT = 0
028840         CLOSE DST-FILE-MAINT WITH CRUNCH
028842         MOVE 0 TO Z-FLINFO5-OPEN
028844         MOVE 0 TO Z-FLINFO5-RS-OPEN.
028846     MOVE 1 TO WS-FM-OPS-DISP.
028848 Z-3-51-1-ELSE.
028850 Z-3-37-1-ELSE.
028852     IF WS-BANK-OPT = 3
028854         NEXT SENTENCE ELSE
028856         GO TO Z-3-55-1-ELSE.
028858*
028860******* OPEN FILE PROC-FILE
028862*
028864     IF Z-FLINFO4-OPEN = 0
028866         CHANGE ATTRIBUTE DEPENDENTSPECS OF PROC-FILE TO TRUE 
028868         OPEN INPUT PROC-FILE 
028870         IF ATTRIBUTE FILESTATE OF PROC-FILE = VALUE OPENED
028872             MOVE ZEROS TO Z-FILE4-KEY
028874             MOVE ZEROS TO Z-FLINFO4-RS-KEY
028876             MOVE 1 TO Z-FLINFO4-OPEN
028878             MOVE 1 TO Z-FLINFO4-RS-OPEN
028880         ELSE
028882             DISPLAY ">>> FILE PROC-FILE FAILED TO OPEN"
028884             MOVE ATTRIBUTE TITLE OF PROC-FILE TO                 
028886                 Z-FL-EXCEPT-TITLE
028888             DISPLAY ">>> OPEN FAIL, TITLE :", Z-FL-EXCEPT-TITLE
028890             DISPLAY ">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS".
028892*
028894******* OPEN FILE PROC-FILE
028896*
028898     IF Z-FLINFO4-OPEN = 0
028900         CHANGE ATTRIBUTE DEPENDENTSPECS OF PROC-FILE TO TRUE 
028902         OPEN INPUT PROC-FILE 
028904         IF ATTRIBUTE FILESTATE OF PROC-FILE = VALUE OPENED
028906             MOVE ZEROS TO Z-FILE4-KEY
028908             MOVE ZEROS TO Z-FLINFO4-RS-KEY
028910             MOVE 1 TO Z-FLINFO4-OPEN
028912             MOVE 1 TO Z-FLINFO4-RS-OPEN
028914         ELSE
028916             DISPLAY ">>> FILE PROC-FILE FAILED TO OPEN"
028918             MOVE ATTRIBUTE TITLE OF PROC-FILE TO                 
028920                 Z-FL-EXCEPT-TITLE
028922             DISPLAY ">>> OPEN FAIL, TITLE :", Z-FL-EXCEPT-TITLE
028924             DISPLAY ">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS".
028926     MOVE ZERO TO Z-FLINFO4-PRES.
028928     MOVE ZERO TO Z-FLINFO4-SOME.
028930     MOVE 3 TO Z-FLINFO4-LAST-SEQ.
028932*
028934 Z-3-57-LOOP.
028936     MOVE ZERO TO Z-FLINFO4-PRES.
028938*
028940 Z-3-57-READ.
028942     READ PROC-FILE RECORD 
028944         AT END
028946         GO TO Z-3-57-XIT.
028948     MOVE Z-FILE4-KEY TO Z-FLINFO4-RS-KEY.
028950*
028952     MOVE 1 TO Z-FLINFO4-PRES.
028954     MOVE 1 TO Z-FLINFO4-SOME.
028956     MOVE 1 TO Z-FLINFO4-MODIFY.
028958     MOVE 0 TO Z-EXIT-CODE.
028960     MOVE 9999 TO Z-EXIT-LEVEL.
028962     MOVE ZEROS TO RMD-COUNT
028964       , RMD-BK
028966       , RMD-DC
028968       , RMD-TOT-CHGD
028970       , WS-TIN-TOTALS
028972       , RMD-COUNT-INHERIT
028974       , RMD-TOT-CHGD-INHERIT.
028976     MOVE ZEROS TO WS-1ST-TIME.
028978     MOVE SPACES TO RMD-BK-NAME
028980       , WS-FICHE-REQUEST.
028982     MOVE PROC-BANK TO WS-BANK-NO.
028984     IF WS-CSTFM-OPEN = 0
028986         NEXT SENTENCE ELSE
028988         GO TO Z-3-62-1-ELSE.
028990     MOVE PROCESS-DATE-MMDD TO WS-CSTFM-DT.
028992     MOVE 000 TO WS-CSTFM-BK.
028994     MOVE SPACES TO WS-CSTFM-SUFF-R.
028996     MOVE WS-SUFFIX-IN TO WS-CSTFM-SUFF.
028998*
029000******* OPEN FILE CST-FILE-MAINT
029002*
029004     IF Z-FLINFO6-OPEN = 0
029006         CHANGE ATTRIBUTE NEWFILE OF CST-FILE-MAINT TO VALUE TRUE
029008         OPEN OUTPUT CST-FILE-MAINT 
029010         IF ATTRIBUTE FILESTATE OF CST-FILE-MAINT = VALUE OPENED
029012             MOVE ZEROS TO Z-FILE6-KEY
029014             MOVE ZEROS TO Z-FLINFO6-RS-KEY
029016             MOVE 3 TO Z-FLINFO6-OPEN
029018             MOVE 3 TO Z-FLINFO6-RS-OPEN
029020         ELSE
029022             DISPLAY ">>> FILE CST-FILE-MAINT FAILED TO OPEN"
029024             MOVE ATTRIBUTE TITLE OF CST-FILE-MAINT TO            
029026                 Z-FL-EXCEPT-TITLE
029028             DISPLAY ">>> OPEN FAIL, TITLE :", Z-FL-EXCEPT-TITLE
029030             DISPLAY ">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS".
029032     MOVE 1 TO WS-CSTFM-OPEN.
029034 Z-3-62-1-ELSE.
029036************ PERFORM GET-BANK-INFO
029038     PERFORM Z-4-PROCEDURE THRU Z-4-XIT.
029040     IF Z-EXIT-PROCESS
029042         MOVE 0 TO Z-EXIT-LEVEL
029044         MOVE 2 TO Z-EXIT-CODE
029046         GO TO Z-3-57-END.
029048     IF  Z-EXIT-EDITEXIT
029050         GO TO Z-3-XIT.
029052     IF  Z-DMS2-ABORT-FLAG = 1
029054         GO TO Z-3-XIT.
029056     IF  Z-EXIT-LEVEL < 0
029058         GO TO Z-3-57-END.
029060*
029062************ PERFORM GET-ACCT-INFO
029064     PERFORM Z-5-PROCEDURE THRU Z-5-XIT.
029066     IF Z-EXIT-PROCESS
029068         MOVE 0 TO Z-EXIT-LEVEL
029070         MOVE 2 TO Z-EXIT-CODE
029072         GO TO Z-3-57-END.
029074     IF  Z-EXIT-EDITEXIT
029076         GO TO Z-3-XIT.
029078     IF  Z-DMS2-ABORT-FLAG = 1
029080         GO TO Z-3-XIT.
029082     IF  Z-EXIT-LEVEL < 0
029084         GO TO Z-3-57-END.
029086*
029088************ PERFORM CLOSE-FM-FILE-RPT
029090     PERFORM Z-6-PROCEDURE THRU Z-6-XIT.
029092     IF Z-EXIT-PROCESS
029094         MOVE 0 TO Z-EXIT-LEVEL
029096         MOVE 2 TO Z-EXIT-CODE
029098         GO TO Z-3-57-END.
029100     IF  Z-EXIT-EDITEXIT
029102         GO TO Z-3-XIT.
029104     IF  Z-DMS2-ABORT-FLAG = 1
029106         GO TO Z-3-XIT.
029108     IF  Z-EXIT-LEVEL < 0
029110         GO TO Z-3-57-END.
029112*
029114 Z-3-57-END.
029116     IF Z-EDIT-ERROR
029118         GO TO Z-3-XIT.
029120 Z-3-57-SKIP.
029122     IF Z-EXIT-LEVEL < 0
029124         GO TO Z-3-57-XIT.
029126     IF Z-EXIT-LEVEL < 1
029128         GO TO Z-3-END.
029130     IF Z-EXIT-CODE > 0
029132         GO TO Z-3-57-XIT.
029134 Z-3-RESTART-1.
029136     MOVE 1 TO Z-RESTART-POINT.
029138*
029140     IF Z-DMS2-TRANS-STATE = 1
029142         MOVE ZERO TO Z-RESTART-FOR-COUNT
029144     ELSE
029146         ADD 1 TO Z-RESTART-FOR-COUNT
029148         IF  Z-RESTART-FOR-COUNT NOT < Z-RESTART-FOR-COUNT-LIMIT
029150             MOVE ZERO TO Z-RESTART-FOR-COUNT
029152             PERFORM Z-DMS2-BEGIN-TRANS
029154                THRU Z-DMS2-BEGIN-TRANS-XIT
029156             IF Z-DMS2-ABORT-FLAG = 1
029158                 GO TO Z-3-XIT.
029160     IF Z-DMS2-TRANS-STATE = 0
029162         IF Z-DMS2-FOUND-LOCK = 1
029164             PERFORM Z-DMS2-FREE
029166                THRU Z-DMS2-FREE-XIT.
029168     IF Z-DMS2-TRANS-STATE = 1
029170         ADD 1 TO Z-RESTART-BY-COUNT
029172         IF  Z-RESTART-BY-COUNT NOT < Z-RESTART-BY-COUNT-LIMIT
029174             MOVE ZERO TO Z-RESTART-BY-COUNT
029176             MOVE 2 TO Z-DMS2-ET-TYPE
029178             PERFORM Z-DMS2-END-TRANS
029180                THRU Z-DMS2-END-TRANS-XIT.
029182     IF Z-DMS2-ABORT-FLAG = 1
029184         GO TO Z-3-XIT.
029186     GO TO Z-3-57-LOOP.
029188*
029190 Z-3-57-XIT.
029192*
029194     MOVE ZEROS TO Z-RESTART-BY-COUNT.
029196     MOVE ZEROS TO Z-RESTART-FOR-COUNT.
029198     IF Z-DMS2-TRANS-STATE = 0
029200         IF Z-DMS2-FOUND-LOCK = 1
029202             PERFORM Z-DMS2-FREE
029204                THRU Z-DMS2-FREE-XIT.
029206     IF Z-DMS2-TRANS-STATE = 1
029208        MOVE 2 TO Z-DMS2-ET-TYPE
029210        PERFORM Z-DMS2-END-TRANS
029212           THRU Z-DMS2-END-TRANS-XIT
029214        IF Z-DMS2-ABORT-FLAG = 1
029216           GO TO Z-3-XIT.
029218*
029220*
029222     MOVE 0 TO Z-EXIT-CODE.
029224     MOVE 9999 TO Z-EXIT-LEVEL.
029226     IF WS-DSTFM-OPEN > 0
029228         NEXT SENTENCE ELSE
029230         GO TO Z-3-72-1-ELSE.
029232     MOVE 0 TO WS-DSTFM-OPEN.
029234*
029236***********  CLOSE OF FILE DST-FILE-MAINT WITH CRUNCH
029238*
029240     IF Z-FLINFO5-OPEN NOT = 0
029242         CLOSE DST-FILE-MAINT WITH CRUNCH
029244         MOVE 0 TO Z-FLINFO5-OPEN
029246         MOVE 0 TO Z-FLINFO5-RS-OPEN.
029248     MOVE 1 TO WS-FM-OPS-DISP.
029250 Z-3-72-1-ELSE.
029252     IF WS-CSTFM-OPEN > 0
029254         NEXT SENTENCE ELSE
029256         GO TO Z-3-76-1-ELSE.
029258     MOVE 0 TO WS-CSTFM-OPEN.
029260*
029262***********  CLOSE OF FILE CST-FILE-MAINT WITH CRUNCH
029264*
029266     IF Z-FLINFO6-OPEN NOT = 0
029268         CLOSE CST-FILE-MAINT WITH CRUNCH
029270         MOVE 0 TO Z-FLINFO6-OPEN
029272         MOVE 0 TO Z-FLINFO6-RS-OPEN.
029274 Z-3-76-1-ELSE.
029276     IF ( WS-FM-OPS-DISP = 1 ) OR ( WS-BANK-OPT = 3 )
029278         NEXT SENTENCE ELSE
029280         GO TO Z-3-79-1-ELSE.
029282     DISPLAY "**** CREATING BATCH FM RECORDS".
029284     DISPLAY "WHEN MINDISTCALC PROGRAM IS COMPLETE".
029286     DISPLAY "PLEASE RUN BR0080 PROGRAM ".
029288     DISPLAY "TO LOAD TDA FM FILE(S): ".
029290     DISPLAY "                        ".
029292     IF ( WS-FM-OPS-DISP = 1 ) AND ( WS-BANK-OPT = 1 OR 3 )
029294         NEXT SENTENCE
029296     ELSE
029298         GO TO Z-3-85-DISPLAY.
029300     DISPLAY WS-DSTFM-ID.
029302 Z-3-85-DISPLAY.
029304     IF WS-BANK-OPT = 2
029306         NEXT SENTENCE ELSE
029308         GO TO Z-3-86-1-ELSE.
029310     MOVE ZERO TO WS-BKSUB.
029312     MOVE 1 TO Z-I-2.
029314 Z-3-88-LOOP.
029316     IF Z-I-2 > 20
029318         GO TO Z-3-88-XIT.
029320     MOVE 0 TO Z-EXIT-CODE.
029322     MOVE 9999 TO Z-EXIT-LEVEL.
029324     ADD 1 TO WS-BKSUB .
029326********* EXIT WHEN
029328     IF WS-BK-LNO (WS-BKSUB) = ZEROS
029330        NEXT SENTENCE
029332     ELSE
029334        GO TO Z-3-90-EXIT-SKIP.
029336     MOVE 1 TO Z-EXIT-LEVEL.
029338     MOVE 1 TO Z-EXIT-CODE.
029340     GO TO Z-3-88-END.
029342 Z-3-90-EXIT-SKIP.
029344     IF WS-BK-RMD-ID (WS-BKSUB) > SPACES
029346         NEXT SENTENCE ELSE
029348         GO TO Z-3-91-1-ELSE.
029350     DISPLAY WS-DSTFM-ID.
029352 Z-3-91-1-ELSE.
029354 Z-3-88-END.
029356     IF Z-EDIT-ERROR
029358         GO TO Z-3-XIT.
029360 Z-3-88-SKIP.
029362     IF Z-EXIT-LEVEL < 0
029364         GO TO Z-3-88-XIT.
029366     IF Z-EXIT-LEVEL < 1
029368         GO TO Z-3-END.
029370     IF Z-EXIT-CODE > 0
029372         GO TO Z-3-88-XIT.
029374     ADD 1 TO Z-I-2.
029376     GO TO Z-3-88-LOOP.
029378*
029380 Z-3-88-XIT.
029382     MOVE 0 TO Z-EXIT-CODE.
029384     MOVE 9999 TO Z-EXIT-LEVEL.
029386 Z-3-86-1-ELSE.
029388     IF WS-BANK-OPT = 3
029390         NEXT SENTENCE
029392     ELSE
029394         GO TO Z-3-93-DISPLAY.
029396     DISPLAY WS-CSTFM-ID.
029398 Z-3-93-DISPLAY.
029400     DISPLAY "                        ".
029402     DISPLAY "AX BLANK TO CONTINUE.".
029404     ACCEPT WS-ACCEPT.
029406 Z-3-79-1-ELSE.
029408 Z-3-55-1-ELSE.
029410 Z-3-END.
029412     IF Z-EDIT-ERROR
029414         GO TO Z-3-XIT.
029416 Z-3-SKIP.
029418     MOVE 0 TO Z-EXIT-CODE.
029420     MOVE 9999 TO Z-EXIT-LEVEL.
029422*
029424*
029426     MOVE ZEROS TO Z-RESTART-BY-COUNT.
029428     MOVE ZEROS TO Z-RESTART-FOR-COUNT.
029430     IF Z-DMS2-TRANS-STATE = 0
029432         IF Z-DMS2-FOUND-LOCK = 1
029434             PERFORM Z-DMS2-FREE
029436                THRU Z-DMS2-FREE-XIT.
029438     IF Z-DMS2-TRANS-STATE = 1
029440        MOVE 2 TO Z-DMS2-ET-TYPE
029442        PERFORM Z-DMS2-END-TRANS
029444           THRU Z-DMS2-END-TRANS-XIT
029446        IF Z-DMS2-ABORT-FLAG = 1
029448           GO TO Z-3-XIT.
029450*
029452*
029454     GO TO Z-3-XIT.
029456*
029458 Z-3-RESTART.
029460     IF Z-RESTART-POINT = ZERO
029462         GO TO Z-3-PROCESS.
029464     IF Z-RESTART-POINT = 1
029466         GO TO Z-3-RESTART-1.
029468*
029470 Z-3-XIT.
029472     EXIT.
029474*
029476*****************************************************************
029478*    PROCEDURE PRT-LABEL-CHECK
029480*****************************************************************
029482 Z-7-PROCEDURE.
029484*
029486*L"S"/"GEN.L"/"PRINTER-PR".                                       
029488*=================================================================
029490*                          PRINT ROUTINE                          
029492*=================================================================
029494*   FILENAME SETUP:                                               
029496*     MOVE PACK-ID TO "GWS-PACK"                                  
029498*     MOVE APPLICATION TO "GWS-APPL"                              
029500*     MOVE NO OF PART PAPER TO "GWS-NO-PARTS"                     
029502*     MOVE REPORT DESCRIPTOR TO "GWS-PRT-DESCRIPTOR"              
029504*     MOVE CSI BRANCH CODE TO "GWS-BRANCH-CODE"                   
029506*     MOVE NO OF MICROFICHE COPIES TO "GWS-MICROFICHE-CODE"       
029508*     MOVE BANK NUMBER TO "GWS-BANK-NUMBER"                       
029510*     MOVE SPACES TO "GWS-TIME" IF TIME NOT DESIRED ELSE MOVE ZERO
029512*     MOVE 1 TO GWS-TIME-CTL IF GWS-TIME IS NOT TO USED FOR TIME  
029514*     IF NONE OF THE ABOVE IS SET DEFAULTS WILL TAKE PLACE        
029516*     PERFORM "99-PRT-LABEL-CHECK" - ROUTINE WILL EDIT            
029518*        "GWS-PRINT-LABEL", AND IF DIFFERENT FROM CURRENT PRINT   
029520*        FILE, CLOSE PRINT FILE, AND MOVE "GWS-PRINT-LABEL" TO    
029522*        "ID-PRT" OR "ID-PRT74" IF "COBOL74-CODE" = 1; ALSO ALLOWS
029524*        OPERATOR TO DESIGNATE PACK NAME IF SW3 = 1               
029526*                                                                 
029528*     TO USE LONG PRINTFILE NAMES:                                
029530*        MOVE 1 TO "GWS-LONG-PRTNAMES" FOR PRT/ PREFIX LEVEL      
029532*        MOVE 2 TO "GWS-LONG-PRTNAMES" FOR EOM/ PREFIX LEVEL      
029534*        MOVE 3 TO "GWS-LONG-PRTNAMES" FOR EOY/ PREFIX LEVEL      
029536*        MOVE 2-DIGIT NUMERIC CSI DATA CENTER TO "GWS-CSI-DC"     
029538*        MOVE 3-DIGIT NUMERIC BANK NUMBER TO "GWS-CSI-BK"         
029540*        EXAMPLE OF LONG FILENAME:                                
029542*            PRT/00/101/DDA0P1SP00/0000123456                     
029544*                                                                 
029546*     REMOTE PRINT FILE NAME SETUP                                
029548*        TO USE THE REMOTE PRINT NAME SETUP, COPY IN THE GENERAL  
029550*        LIBRARY 'GEN.L/RMTPRTLBL'                                
029552*        MOVE A '1' TO GWS-RMT-PRT-OPTION                         
029554*        MOVE IN THE FILE NAME EXTENSION IF OTHER THAN 000        
029556*          TO GWS-RMT-EXT                                         
029558*        IN THE COPY STATEMENT USE THE COPY REPLACING             
029560*          TO REPLACE 'PERFORM 99-PRT-REMOTE-LBL-CHK'             
029562*          WITH 'PERFORM 99-PRT-RMT-LBL-CHK'.                     
029564*        TO USE THE REMOTE FILE NAME SETUP, THE BANK FILE SPECS   
029566*          MUST ALSO BE COPIED IN AS AN FD 'GEN.L/DC-FD.C'        
029568*                                                                 
029570*     TO USE NEW LONG PRINTFILE NAMES FOR EOM:                    
029572*        MOVE 1 TO GWS-LONG-PRTNAMES-NEW                          
029574*        MOVE CENTERVIEW CODE TO GWS-CNTR-VIEW (SPEC-CENTERVIEW)  
029576*        MOVE NEW EOM PRINT TO GWS-PRT-NEW  (SPEC-PRT-NEW)        
029578*        EXAMPLE OF NEW EOM LONG FILENAME:                        
029580*            PRINT/00/DDA/01SP/0101/CR00/25DSP847                 
029582*                                                                 
029584*   SINGLE SPACE - PERFORM "99-PRT1"                              
029586*   DOUBLE SPACE - PERFORM "99-PRT2"                              
029588*   MULTI  SPACE - MOVE NUMBER TO "NO-LINES"; PERFORM "99-PRT-MUL"
029590*                                                                 
029592*   HEADER PRT: MOVE HEADING INFORMATION TO "HEADER-LINE[1,2,3,4, 
029594*     OR 5] DEPENDING ON HOW MANY LINE(S) ARE NEEDED; MOVE NUMBER 
029596*     OF HEADING LINE(S) TO BE PRINTED TO "HDR-CTL"; ROUTINE WILL 
029598*     AUTOMATICALLY SKIP A LINE  AFTER LAST HEADER-LINE  PRINTED; 
029600*     MOVE NUMBER OF LINES/PAGE TO "END-PAGE"(DEFAULT IS 58 -LINE 
029602*     COUNT BEGINS WITH FIRST HEADER LINE); MOVE 0 TO "PAGE-CTR"; 
029604*     PERFORM "99-HDR-PRT" (NEED ONLY BE PERFORM ONCE BEFORE EACH 
029606*     NEW REPORT);  PRINT ROUTINE  DEFAULTS  TO BYPASSING HEADING 
029608*     PRINT ROUTINE IF VALUE IS NOT SET IN "HDR-CTL".             
029610*     RECOMMENDED HEADER-LINE1 FORMAT:                            
029612*       MOVE CSI BRANCH CODE TO "H-CSI-BR-NO"                     
029614*       MOVE BANK NUMBER     TO "H-BANK-NO"                       
029616*       MOVE BANK NAME       TO "H-BANK-NAME"                     
029618*       MOVE NAME OF REPORT  TO "H-REPORT-TITLE"                  
029620*       MOVE REPORT NUMBER   TO "H-REPORT-NO"                     
029622*       MOVE DAY OF WEEK     TO "H-DAY-WEEK"                      
029624*       MOVE DATE            TO "H-DATE"                          
029626*       MOVE TIME            TO "H-HHMM"                          
029628*                                                                 
029630*   TEAR PAGES: MOVE "DATA" 8 BY 3 LINES TO "TEAR-PAGE-IN"        
029632*     PERFORM "99-TEAR-PAGES".                                    
029634*     MOVE ZERO TO "TP-SKIP" IF NO SKIP TO 1 BEFORE PRINT.        
029636*     RECOMMENDED TEAR-PAGE FORMAT:                               
029638*       MOVE BANK NUMBER TO "TP-LN-BKNO"                          
029640*       MOVE DATE        TO "TP-LN-DATE"                          
029642*       MOVE APPLICATION TO TP-LN3 (OPTIONAL).                    
029644*                                                                 
029646*   EXCEPTION PRINT RECORDS:                                      
029648*    RECOMMENDED FORMAT:                                          
029650*        BANK NO                                                  
029652*        ACCOUNT NUMBER                                           
029654*        GWS-PRT-EXCEPT-LINE - THIS DATA NAME IS A GROUP ITEM     
029656*         (BLOCK NO /97/ HEADER LINE /98/ DETAIL LINE             
029658*          PAGE CONTROL                                           
029660*          NO OF LINES TO SPACES AFTER PRINTING                   
029662*          PRINT DATA                                  )          
029664*    CREATE: MOVE "C" TO GWS-PRT-EXC-FLAG.                        
029666*    (PROGRAMMING NOTE: ADD THESE STATEMENTS IMMEDIATELY FOLLOWING
029668*      THE COPY PRINTER PROCEDURE LIBRARY)                        
029670*      MOVE GWS-PRT-EXCEPT-LINE TO (YOUR EXCEPT RECORD FOLLOWING  
029672*                                   THE ACCOUNT NUMBER).          
029674*      PERFORM (YOUR WRITE EXCEPTION ROUTINE).                    
029676*    PRINT: MOVE "P" TO GWS-PRT-EXC-FLAG.                         
029678*      MOVE (YOUR EXCEPTION REC FOLLOWING TO GWS-PRT-EXCEPT-LINE. 
029680*            THE ACCOUNT NUMBER)                                  
029682*      PERFORM 99-PRT1.                                           
029684*    CANCEL: MOVE SPACE TO GWS-PRT-EXC-FLAG.                      
029686*=================================================================
029688 PRT SECTION 00.                                                  
029690*=================================================================
029692*                 PRINTER FILENAME SETUP ROUTINE                  
029694*=================================================================
029696 99-PRT-LABEL-CHECK SECTION 51.                                   
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 592 lines from 14253 to 14844.

    You MUST include EVERY line from this code block in your documentation output.

    🚨 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):
    ============================================================================
    COBOL-74 comments are marked with "*" in column 7 (after the 6-digit sequence number).

    Example comment lines:
      000020* This is a comment
      000026*REMARKS.
      000028*  SYSTEM    : TDAR

    ⚠️  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!

    Comments are NOT "already documented" - they are SOURCE CODE that must be preserved.
    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.

    DO NOT:
    - Skip comment lines thinking they don't need documentation
    - Omit comment blocks (even if they span 100+ lines)
    - Exclude REMARKS sections, copyright notices, or build information
    - Remove any line that starts with a * after the sequence number

    DO:
    - Include EVERY line starting with 000010* through 999999*
    - Preserve all comment formatting exactly as shown
    - Show complete comment blocks in their entirety
    - Treat comments as essential source code content
    ============================================================================

    **IMPORTANT - Document ALL COBOL Divisions:**
    - IDENTIFICATION DIVISION: Include program metadata verbatim
    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim
    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim
    - PROCEDURE DIVISION: Include all paragraphs with code and explanations

    Do NOT skip:
    - Data tables (even with thousands of FILLER definitions)
    - WORKING-STORAGE variables
    - FILE SECTION record layouts
    - ANY lines from the source code above

    Each line starts with a 6-digit sequence number (e.g., 003240).
    Include these sequence numbers in your code blocks to prove coverage.

```

---

## Program Map (if present)


```
════════════════════════════════════════════════════════════════════════════════
PROGRAM MAP: TDAS-MINDISTCALC
════════════════════════════════════════════════════════════════════════════════
│
│ Total Paragraphs: 0
│ Total Data Items: 0
│ External Calls: 21
│
├── IDENTIFICATION DIVISION
│   └── PROGRAM-ID: TDAS-MINDISTCALC
│
└── PROCEDURE DIVISION
    │
    ├── Top 50 Most Important Paragraphs:
    │   # 1  Z-35-2-ENDIF  [Importance: 646]
    │   # 2  Z-DMS-EXCEPTION  [Importance: 210]
    │   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]
    │   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]
    │   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]
    │   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]
    │   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]
    │   # 8  030040*L"S"/"GENL"/"RMTPRTLBL"  [Importance: 80]
    │   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]
    │   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]
    │   #11  Z-5-XIT  [Importance: 58]
    │   #12  CALCULATIONS  [Importance: 56]
    │   #13  Z-DATE-CALC-Y  [Importance: 56]
    │   #14  Z-DATE-CALC-C  [Importance: 56]
    │   #15  Z-FL-EXCEPTION  [Importance: 56]
    │   #16  TPR-WRITE-TEAR  [Importance: 56]
    │   #17  Z-29-PROCEDURE  [Importance: 56]
    │   #18  Z-3-XIT  [Importance: 56]
    │   #19  032926********ENDIF  [Importance: 40]
    │   #20  033256********ENDIF  [Importance: 40]
    │   #21  Z-DMS2-END-TRANS  [Importance: 37]
    │   #22  Z-DMS2-FREE  [Importance: 35]
    │   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]
    │   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]
    │   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]
    │   #26  TPR-TEAR-PAGES  [Importance: 28]
    │   #27  Z-21-PROCEDURE  [Importance: 28]
    │   #28  Z-DATE-YY-DIFF  [Importance: 28]
    │   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]
    │   #30  SETUP-NEW-REPORT  [Importance: 28]
    │   #31  Z-21-XIT  [Importance: 26]
    │   #32  Z-5-14-END  [Importance: 24]
    │   #33  Z-30-XIT  [Importance: 22]
    │   #34  Z-OPEN-DB-2  [Importance: 21]
    │   #35  GET-BANK-INFO  [Importance: 21]
    │   #36  Z-4-PROCEDURE  [Importance: 21]
    │   #37  GET-ACCT-INFO  [Importance: 21]
    │   #38  Z-5-PROCEDURE  [Importance: 21]
    │   #39  CLOSE-FM-FILE-RPT  [Importance: 21]
    │   #40  Z-6-PROCEDURE  [Importance: 21]
    │   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]
    │   #42  HEADING-SETUP  [Importance: 21]
    │   #43  Z-16-PROCEDURE  [Importance: 21]
    │   #44  000026*REMARKS  [Importance: 20]
    │   #45  033774*****ENDIF  [Importance: 20]
    │   #46  Z-11-XIT  [Importance: 18]
    │   #47  Z-22-XIT  [Importance: 18]
    │   #48  99-NEW-END  [Importance: 16]
    │   #49  Z-PROCESS-INIT  [Importance: 14]
    │   #50  Z-OPEN-DB-1  [Importance: 14]
    │
    └── External Calls (21 total):
        ├─> CURRENT_DATE OF GENERALSUPPORT (called 16 times)
        ├─> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)
        ├─> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)
        ├─> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)

════════════════════════════════════════════════════════════════════════════════
Map Token Count: ~779
════════════════════════════════════════════════════════════════════════════════
```

