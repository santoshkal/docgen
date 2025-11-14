# LLM Request Debug File
Generated: 2025-11-13T20:23:10.357066

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 12/55
- **Model**: gpt-4.1
- **Chunk Number**: 12
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~10,326 tokens
- **Total Input**: ~12,284 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 12/55" (ID: detailed-code-explanation)

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


**CHUNK 12 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 12 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 5763 to 6105 (343 lines)\nChunk Tokens (estimated): ~6,259\nActual Input Tokens: 7,665 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 5763-6105 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 12 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 12 of 55.\n\n\n=============================================================================\nCHUNK 12 SOURCE CODE (Lines 5763-6105)\n=============================================================================\n\n```cobol\n011534 01  RMD-LEF-TABLE-3-2022-X.                                      \n011536   05  RMD-LEF-TABLE-3-2022.                                      \n011538     10 FILLER PIC X(54) VALUE                                    \n011540         \"274265255246237229220211202194185177168160152144137129\".\n011542     10 FILLER PIC X(54) VALUE                                    \n011544         \"122115108101095089084078073068064060056052049046043041\".\n011546     10 FILLER PIC X(39) VALUE                                    \n011548         \"039037035034033031030029028027025023020\".               \n011550                                                                  \n011552   05  WS-RMD-LEF-TABLE-3-2022 REDEFINES RMD-LEF-TABLE-3-2022.    \n011554       10  WS-RMD-TBL3-2022-LEF      PIC 999 OCCURS 49 TIMES.     \n011556                                                                  \n011558 01  TEMP-01.                                                     \n011560     02  GWS-PRINT-LABEL.                                         \n011562     05  GWS-FAMILY.                                              \n011564         10  GWS-APPL.                                            \n011566             15  GWS-APPL-1X         PIC X(01) VALUE \"C\".         \n011568             15  FILLER              PIC X(02) VALUE \"SI\".        \n011570         10  GWS-CST-PERIOD          PIC X(01) VALUE \"0\".         \n011572         10  GWS-FILE-TYPE           PIC X(01) VALUE \"P\".         \n011574         10  GWS-NO-PARTS.                                        \n011576             15  GWS-NO-PART-ZONE    PIC 9(01) COMP.              \n011578             15  GWS-NO-PART-NUMERIC PIC 9(01) VALUE @1@ COMP.    \n011580         10  GWS-PRT-DESCRIPTOR      PIC X(02) VALUE \"SP\".        \n011582         10  GWS-BRANCH-CODE         PIC X(02) VALUE \"00\".        \n011584     05  GWS-SLASH                   PIC X(01) VALUE \"/\".         \n011586     05  GWS-ELEM.                                                \n011588         10  GWS-MICRO-BANK.                                      \n011590             15  GWS-MICROFICHE-CODE PIC X(01) VALUE \"0\".         \n011592             15  GWS-BANK-NO-X.                                   \n011594                 20  GWS-BANK-NUMBER PIC 9(03) VALUE ZEROS.       \n011596         10  GWS-TIME.                                            \n011598             15  FILLER              PIC X(04) VALUE \"0000\".      \n011600             15  GWS-MISC            PIC X(02) VALUE \"00\".        \n011602     05  GWS-ON                      PIC X(04) VALUE \" ON \".      \n011604     05  GWS-PACK                    PIC X(10) VALUE SPACES.      \n011606     05  GWS-PERIOD                  PIC X(01) VALUE SPACE.       \n011608     05  FILLER                      PIC X(11) VALUE SPACES.      \n011610    02  GWS-PRT-LABEL   REDEFINES GWS-PRINT-LABEL.                \n011612         05  GWS-PRT-LABEL-1-15          PIC X(15).               \n011614         05  FILLER                      PIC X(32).               \n011616                                                                  \n011618 01 WS-FM-OPS-DISP               PIC 9(01) VALUE 0.               \n011620 01 RPT601-BANNER-HEADER         PIC 9(01) VALUE 0.               \n011622 01 RMD-DC                       PIC 9(02).                       \n011624 01 RMD-BK                       PIC 9(04).                       \n011626 01 RMD-BK-NAME                  PIC X(30).                       \n011628 01 RMD-COUNT                    PIC 9(08).                       \n011630 01 RMD-COUNT-INHERIT            PIC 9(08).                       \n011632 01 RMD-TOT-CHGD                 PIC 9(08).                       \n011634 01 RMD-TOT-CHGD-INHERIT         PIC 9(08).                       \n011636 01 WS-GRP-1.                                                     \n011638    05 FILLER                    PIC X(01) VALUE \"/\".             \n011640    05 WS-DATA-CENTER            PIC 9(02).                       \n011642    05 WS-BK-NO                  PIC 9(04).                       \n011644    05 FILLER                    PIC X(01) VALUE \"/\".             \n011646 01 WS-GRP-2.                                                     \n011648    05 FILLER                    PIC X(03) VALUE \"CSI\".           \n011650    05 WS-CSI-DAY                PIC 9(02).                       \n011652    05 WS-CSI-TIME               PIC 9(04).                       \n011654 01 WS-ACCEPT                    PIC X(01).                       \n011656 01 WS-BANK-OPT                  PIC 9(01).                       \n011658 01 WS-BANK-NO                   PIC 9(04).                       \n011660 01 WS-BANK-LIST.                                                 \n011662    05 WS-BK-LIST-TBL   OCCURS 20 TIMES.                          \n011664       10 WS-BK-LNO              PIC 9(04).                       \n011666    05 WS-BK-RMD-ID-TBL OCCURS 20 TIMES.                          \n011668       10 WS-BK-RMD-ID           PIC X(31).                       \n011670 01 WS-BKSUB                     PIC 9(02) VALUE ZEROS.           \n011672 01 WS-DC                        PIC 9(02).                       \n011674 01 WS-MDRPT-OPEN                PIC 9(01).                       \n011676 01 WS-MDRPT2-OPEN               PIC 9(01).                       \n011678 01 WS-DSTFM-OPEN                PIC 9(01) VALUE ZEROS.           \n011680 01 WS-CSTFM-OPEN                PIC 9(01) VALUE ZEROS.           \n011682 01 WS-RMDFM2-CUST-IND           PIC 9(01) VALUE ZEROS.           \n011684 01 WS-PROCFILE-TITLE.                                            \n011686    05 FILLER                    PIC X(10) VALUE \"TDA/DAILY/\".    \n011688    05 WS-PROCFILE-DAY           PIC X(03) VALUE \"TUE\".           \n011690    05 FILLER                    PIC X(11) VALUE \" ON GENERAL\".   \n011692    05 FILLER                    PIC X(01) VALUE \".\".             \n011694 01 WS-RMD-DATE.                                                  \n011696    05 WS-RMD-DATE-CCYY          PIC 9(04) VALUE ZEROS.           \n011698    05 WS-RMD-DATE-MMDD          PIC 9(04) VALUE ZEROS.           \n011700 01 WS-DATE-CCYYMMDD.                                             \n011702    05 WS-DATE-CCYY              PIC 9(04) VALUE ZEROS.           \n011704    05 WS-DATE-MMDD              PIC 9(04) VALUE ZEROS.           \n011706                                                                  \n011708 01  SPECS-BANK-TABLE.                                            \n011710     05  SPEC-BK-TBL OCCURS 1000 TIMES.                           \n011712         10 SPEC-BK-NO-TBL        PIC 9(04).                      \n011714         10 SPEC-BK-DC-TBL        PIC 9(02).                      \n011716         10 SPEC-BK-RMT-IND-TBL   PIC X(02).                      \n011718                                                                  \n011720 01  WS-DSREC-FLAG                PIC 9(01) VALUE 0.              \n011722 01  WS-NEW-DS-AMT                PIC 9(09)V99.                   \n011724 01  WS-FM-AMT-X.                                                 \n011726     05  FILLER                   PIC X(23).                      \n011728     05  WS-FM-AMT                PIC S9(15)V99.                  \n011730 01  WS-FM-LEF-X.                                                 \n011732     05  FILLER                   PIC X(37).                      \n011734     05  WS-FM-LEF                PIC 99V9.                       \n011736 01  WS-FM-AMT-CD-X.                                              \n011738     05  FILLER                   PIC X(39).                      \n011740     05  WS-FM-AMT-CD             PIC 9.                          \n011742                                                                  \n011744 01  WS-DSTFM-ID.                                                 \n011746     05  FILLER                   PIC X(06) VALUE \"RIN0D/\".       \n011748     05  FILLER                   PIC X(04) VALUE \"TDA/\".         \n011750     05  WS-DSTFM-DT              PIC 9(04).                      \n011752     05  FILLER                   PIC X(01) VALUE \"/\".            \n011754     05  WS-DSTFM-BK              PIC 9(03).                      \n011756     05  FILLER                   PIC X(07) VALUE \"/RMDDST\".      \n011758     05  WS-DSTFM-TIME            PIC X(04).                      \n011760     05  WS-DSTFM-SUFF-R REDEFINES WS-DSTFM-TIME.                 \n011762         10  WS-DSTFM-SUFF        PIC X(01).                      \n011764         10  FILLER               PIC X(03).                      \n011766     05  FILLER                   PIC X(01) VALUE \".\".            \n011768                                                                  \n011770 01  WS-CSTFM-ID.                                                 \n011772     05  FILLER                   PIC X(06) VALUE \"RIN0D/\".       \n011774     05  FILLER                   PIC X(04) VALUE \"TDA/\".         \n011776     05  WS-CSTFM-DT              PIC 9(04).                      \n011778     05  FILLER                   PIC X(01) VALUE \"/\".            \n011780     05  WS-CSTFM-BK              PIC 9(03).                      \n011782     05  FILLER                   PIC X(07) VALUE \"/RMDCST\".      \n011784     05  WS-CSTFM-TIME            PIC X(04).                      \n011786     05  WS-CSTFM-SUFF-R REDEFINES WS-CSTFM-TIME.                 \n011788         10  WS-CSTFM-SUFF        PIC X(01).                      \n011790         10  FILLER               PIC X(03).                      \n011792     05  FILLER                   PIC X(01) VALUE \".\".            \n011794                                                                  \n011796 01  WS-PREV-TIN                 PIC 9(09) VALUE ZEROS.           \n011798 01  WS-1ST-TIME                 PIC 9(01) VALUE 0.               \n011800 01  WS-INHERIT-IRA-ON-TIN       PIC 9(01) VALUE 0.               \n011802 01  WS-NON-INHERIT-IRA-ON-TIN   PIC 9(01) VALUE 0.               \n011804 01  WS-TIN-TOTALS.                                               \n011806     05  WS-TIN-BAL-TOT          PIC S9(11)V99.                   \n011808     05  WS-TIN-RMD-TOT          PIC S9(11)V99.                   \n011810 01  WS-MULTI-DISTR              PIC 9(01) VALUE 0.               \n011812 01  WS-IRA-DISTR-RECS           PIC 9(01) VALUE 0.               \n011814 01  WS-RMDRPT-FIELDS.                                            \n011816     05  WS-RMDRPT-DS-FREQ       PIC X(01).                       \n011818     05  WS-RMDRPT-DS-NTRVL      PIC X(04).                       \n011820     05  WS-RMDRPT-DS-METH       PIC X(04).                       \n011822     05  WS-RMDRPT-OLD-DS-AMT    PIC 9(09)V9(02).                 \n011824                                                                  \n011826 01  WS-RMDRPT-TIN-X.                                             \n011828     05  WS-RMDRPT-TIN           PIC 999B99B9999.                 \n011830     05  WS-RMDRPT-TIN-R REDEFINES WS-RMDRPT-TIN.                 \n011832         10  FILLER              PIC 9(03).                       \n011834         10  WS-RMDRPT-TIN-LDASH PIC X(01).                       \n011836         10  FILLER              PIC 9(02).                       \n011838         10  WS-RMDRPT-TIN-RDASH PIC X(01).                       \n011840         10  FILLER              PIC 9(04).                       \n011842                                                                  \n011844 01  WS-RMDRPT2-TIN-X.                                            \n011846     05  WS-RMDRPT2-TIN          PIC 999B99B9999.                 \n011848     05  WS-RMDRPT2-TIN-R REDEFINES WS-RMDRPT2-TIN.               \n011850         10  FILLER              PIC 9(03).                       \n011852         10  WS-RMDRPT2-TIN-LDASH PIC X(01).                      \n011854         10  FILLER              PIC 9(02).                       \n011856         10  WS-RMDRPT2-TIN-RDASH PIC X(01).                      \n011858         10  FILLER              PIC 9(04).                       \n011860                                                                  \n011862 01  WS-TIN-CUST-INDEX           PIC 9(03) VALUE 0.               \n011864 01  WS-TIN-CUST-TABLE.                                           \n011866     05  WS-TIN-CUST-TBL OCCURS 50 TIMES.                         \n011868         10  WS-TIN-CUST         PIC 9(12).                       \n011870                                                                  \n011872 01  WS-TIN-RMD-INDEX            PIC 9(03) VALUE 0.               \n011874 01  WS-TIN-RMD-MAX              PIC 9(03) VALUE 50.              \n011876 01  WS-TIN-RMD-TABLE.                                            \n011878     05  WS-TIN-RMD-TBL OCCURS 50 TIMES.                          \n011880         10  WS-TIN-RMD-CUST     PIC 9(12).                       \n011882         10  WS-TIN-RMD-ACCT     PIC 9(10).                       \n011884         10  WS-TIN-RMD-DS-NBR   PIC 9(02).                       \n011886         10  WS-TIN-RMD-DS-FREQ  PIC 9(01).                       \n011888         10  WS-TIN-RMD-DS-NTRVL PIC 9(04).                       \n011890         10  WS-TIN-RMD-AMT      PIC 9(9)V9(2).                   \n011892                                                                  \n011894 01  WS-TIN-DETAIL-INDEX         PIC 9(03) VALUE 0.               \n011896 01  WS-TIN-DETAIL-MAX           PIC 9(03) VALUE 100.             \n011898 01  WS-TIN-DETAIL-TABLE.                                         \n011900     05  WS-TIN-DETAIL-TBL OCCURS 100 TIMES.                      \n011902         10  WS-TIN-DET-LINE-3.                                   \n011904             15  FILLER                  PIC X(100).              \n011906             15  WS-TIN-DET-DIST-NTRVL.                           \n011908                 20  WS-TIN-DET-DS-NTRVL PIC 9(4).                \n011910             15  FILLER                  PIC X(1).                \n011912             15  WS-TIN-DET-DIST-FREQ    PIC X(1).                \n011914             15  FILLER                  PIC X(54).               \n011916         10  WS-TIN-DET-LINE-4       PIC X(160).                  \n011918         10  WS-TIN-DET-LINE-8       PIC X(160).                  \n011920                                                                  \n011922 01  WS-TIN-DISTR-RECS           PIC 9(2) VALUE 0.                \n011924 01  WS-PAGE-CNT-FICHE           PIC 9(4).                        \n011926                                                                  \n011928 01  RMDRPT-REC-2.                                                \n011930     02  Z-VA-RMDRPT-REC-2.                                       \n011932     05  FILLER                PIC  X(00050) VALUE                \n011934     \"   CUSTOMER/   ACCOUNT   BIRTHDATE   RMD AGE    RM\".        \n011936     05  FILLER                PIC  X(00050) VALUE                \n011938     \"D DATE    BAL AS OF      LE FACTR/ REQ ANNUAL   DI\".        \n011940     05  FILLER                PIC  X(00050) VALUE                \n011942     \"ST FREQ   OLD DIST   NEW DIST                     \".        \n011944     05  FILLER                PIC  X(00010) VALUE                \n011946     \"          \".                                                \n011948     02  Z-NX-RMDRPT-REC-2     REDEFINES Z-VA-RMDRPT-REC-2.       \n011950     05  FILLER                PIC X(0160).                       \n011952* 003 LINE RECORD FOLLOWS                                         \n011954 01  RMDRPT-REC-6.                                                \n011956     02  Z-VA-RMDRPT-REC-6.                                       \n011958     05  FILLER                PIC  X(00050) VALUE                \n011960     \"    NAME                              DATE        \".        \n011962     05  FILLER                PIC  X(00050) VALUE                \n011964     \"            12/31           TBL     MIN DIST     /\".        \n011966     05  FILLER                PIC  X(00050) VALUE                \n011968     \"METHOD       AMT        AMT                       \".        \n011970     05  FILLER                PIC  X(00010) VALUE                \n011972     \"          \".                                                \n011974     02  Z-NX-RMDRPT-REC-6     REDEFINES Z-VA-RMDRPT-REC-6.       \n011976     05  FILLER                PIC X(0160).                       \n011978* 007 LINE RECORD FOLLOWS                                         \n011980 01  RMDRPT2-REC-2.                                               \n011982     02  Z-VA-RMDRPT2-REC-2.                                      \n011984     05  FILLER                PIC  X(00050) VALUE                \n011986     \"   CUSTOMER/   ACCOUNT    BIRTHDATE    RMD AGE    \".        \n011988     05  FILLER                PIC  X(00050) VALUE                \n011990     \" RMD DATE    OWNER DTH  BAL AS OF      LE FACTR/ R\".        \n011992     05  FILLER                PIC  X(00050) VALUE                \n011994     \"EQ ANNUAL   DIST FREQ   OLD DIST   NEW DIST       \".        \n011996     05  FILLER                PIC  X(00010) VALUE                \n011998     \"          \".                                                \n012000     02  Z-NX-RMDRPT2-REC-2    REDEFINES Z-VA-RMDRPT2-REC-2.      \n012002     05  FILLER                PIC X(0160).                       \n012004* 003 LINE RECORD FOLLOWS                                         \n012006 01  RMDRPT2-REC-6.                                               \n012008     02  Z-VA-RMDRPT2-REC-6.                                      \n012010     05  FILLER                PIC  X(00050) VALUE                \n012012     \"    NAME                                DATE      \".        \n012014     05  FILLER                PIC  X(00050) VALUE                \n012016     \"               DATE       12/31           TBL     \".        \n012018     05  FILLER                PIC  X(00050) VALUE                \n012020     \"MIN DIST     /METHOD       AMT        AMT         \".        \n012022     05  FILLER                PIC  X(00010) VALUE                \n012024     \"          \".                                                \n012026     02  Z-NX-RMDRPT2-REC-6    REDEFINES Z-VA-RMDRPT2-REC-6.      \n012028     05  FILLER                PIC X(0160).                       \n012030* 007 LINE RECORD FOLLOWS                                         \n012032 01  WS-USER-AND-TDB-AREA.                                        \n012034   03  WS-USER-AREA.                                              \n012036**  The following data items can be used across multiple          \n012038**  processes.                                                    \n012040     05  WS-RPT465-AREA.                                          \n012042         10 WS-RPT465-AR-ACTV-TYPE                PIC 9(02).      \n012044         10 WS-RPT465-AR-ACTV-UNPOST              PIC 9(01).      \n012046         10 WS-RPT465-AR-DEP-CDE                  PIC X(03).      \n012048         10 WS-RPT465-AR-TRANS-AMT                PIC 9(09)V99.   \n012050         10 FILLER                                PIC X(09).      \n012052                                                                  \n012054     05  WS-CMAT-WITHHOLD         PIC S9(09)V99.                  \n012056                                                                  \n012058     05  WS-TISA-DT               PIC 9(08) VALUE 19930621.       \n012060     05  WS-WORK-AREA-HOST        PIC X(256) VALUE SPACES.        \n012062     05  WS-SYS-HOST              PIC X(17)  VALUE SPACES.        \n012064                                                                  \n012066     05  WS-SERIAL-NO             PIC 9(12).                      \n012068     05  WS-SERIAL-NO-RE  REDEFINES  WS-SERIAL-NO.                \n012070         10  WS-SERIAL-DT-X.                                      \n012072             15  WS-SERIAL-DT     PIC 9(7).                       \n012074         10  WS-SERIAL-TM-X.                                      \n012076             15  WS-SERIAL-TM     PIC 9(5).                       \n012078                                                                  \n012080     05  GWS-INITIALIZE-IND       PIC X(1)  VALUE \"N\".            \n012082         88 INITIALIZE-GWS                  VALUE \"Y\".            \n012084                                                                  \n012086     05  WS-SPEC-TDA-ADD-DAY.                                     \n012088         10 FILLER                PIC X(02).                      \n012090         10 WS-SPEC-TDA-SUFFIX    PIC X.                          \n012092                                                                  \n012094     05  WS-RUNNING-BAL           PIC S9(12)V99 VALUE 0.          \n012096     05  WS-HMS-LOW-HOLD-NBR      PIC 9999  VALUE 0.              \n012098     05  WS-ACCR-TO-POST          PIC S9(10)V9(4).                \n012100     05  WS-POST-AMT              PIC S9(10)V9(2).                \n012102     05  WS-SWITCH                PIC 9     VALUE 0.              \n012104                                                                  \n012106     05  SCREEN-SUB               PIC 999   VALUE ZEROS.          \n012108                                                                  \n012110     05  WS-CALC-ERROR-FLD        PIC X(12).                      \n012112     05  PREVIOUS-ERROR-NBR       PIC 9(04).                      \n012114                                                                  \n012116     05  WS-SPECS-GRACE-CLOSE     PIC 99.                         \n012118                                                                  \n012120     05  MAX-DISTR                PIC 99 VALUE 2.                 \n012122     05  WS-NEW-DS-NBR            PIC 99 VALUE 0.                 \n012124                                                                  \n012126                                                                  \n012128     05  WS-DIST-CLOSE            PIC 9(01) VALUE 0.              \n012130                                                                  \n012132     05  WS-TRGR-DEL-TABLE-X.                                     \n012134         10  WS-TRGR-DEL-TABLE OCCURS 20 TIMES.                   \n012136             15 TRGR-DEL-BANK    PIC 9(04).                       \n012138             15 TRGR-DEL-RPT-NBR PIC 999.                         \n012140             15 TRGR-DEL-APPL    PIC 9.                           \n012142             15 TRGR-DEL-CUST    PIC 9(12).                       \n012144             15 TRGR-DEL-ACCT    PIC 9(10).                       \n012146             15 TRGR-DEL-PRT-DT  PIC 9(08).                       \n012148             15 TRGR-DEL-SEQ-NBR PIC 9(04).                       \n012150     05  WS-ACTV-DEL-TABLE-X.                                     \n012152         10  WS-ACTV-DEL-TABLE OCCURS 20 TIMES.                   \n012154            15  ACTV-DEL-BANK    PIC 9(04).                       \n012156            15  ACTV-DEL-DATE    PIC 9(08).                       \n012158            15  ACTV-DEL-CUST    PIC 9(12).                       \n012160            15  ACTV-DEL-ACCT    PIC 9(10).                       \n012162            15  ACTV-DEL-TIME    PIC 9(08).                       \n012164            15  ACTV-DEL-SEQ-NBR PIC 9(02).                       \n012166                                                                  \n012168     05  ACTV-DEL-NDX            PIC 99.                          \n012170     05  TRGR-DEL-NDX            PIC 99.                          \n012172     05  HMS-ROLBAK-NDX          PIC 99.                          \n012174     05  DISTR-ROLBAK-NDX        PIC 99.                          \n012176                                                                  \n012178                                                                  \n012180     05 WS-ADDR-ALT-EMAIL        PIC X(100).                      \n012182     05 WS-ADDR-ALT-EMAIL-R REDEFINES                             \n012184        WS-ADDR-ALT-EMAIL.                                        \n012186        10 WS-ADDR-ALT-EMAIL-1   PIC X(40).                       \n012188        10 WS-ADDR-ALT-EMAIL-2   PIC X(40).                       \n012190        10 WS-ADDR-ALT-EMAIL-3   PIC X(20).                       \n012192     05 WS-OLD-ALT-EMAIL        PIC X(100).                       \n012194     05 WS-OLD-ALT-EMAIL-R REDEFINES                              \n012196        WS-OLD-ALT-EMAIL.                                         \n012198        10 WS-OLD-ALT-EMAIL-1   PIC X(40).                        \n012200        10 WS-OLD-ALT-EMAIL-2   PIC X(40).                        \n012202        10 WS-OLD-ALT-EMAIL-3   PIC X(20).                        \n012204     05 WS-ADDR-TEMP-EMAIL       PIC X(100).                      \n012206     05 WS-ADDR-TEMP-EMAIL-R REDEFINES                            \n012208        WS-ADDR-TEMP-EMAIL.                                       \n012210        10 WS-ADDR-TEMP-EMAIL-1  PIC X(40).                       \n012212        10 WS-ADDR-TEMP-EMAIL-2  PIC X(40).                       \n012214        10 WS-ADDR-TEMP-EMAIL-3  PIC X(20).                       \n012216     05 OLD-ADDR-TEMP-EMAIL      PIC X(100).                      \n012218     05 OLD-ADDR-TEMP-EMAIL-R REDEFINES                           \n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 343 lines from 5763 to 6105.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 12,
  "total_chunks": 55,
  "start_line": 5763,
  "end_line": 6105,
  "line_count": 343
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
- Source code length: 31934 characters

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
CHUNK 12 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 5763 to 6105 (343 lines)
Chunk Tokens (estimated): ~6,259
Actual Input Tokens: 7,665 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 5763-6105 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 12 of 55 chunks
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
      The source code below is only CHUNK 12 of 55.


=============================================================================
CHUNK 12 SOURCE CODE (Lines 5763-6105)
=============================================================================

```cobol
011534 01  RMD-LEF-TABLE-3-2022-X.                                      
011536   05  RMD-LEF-TABLE-3-2022.                                      
011538     10 FILLER PIC X(54) VALUE                                    
011540         "274265255246237229220211202194185177168160152144137129".
011542     10 FILLER PIC X(54) VALUE                                    
011544         "122115108101095089084078073068064060056052049046043041".
011546     10 FILLER PIC X(39) VALUE                                    
011548         "039037035034033031030029028027025023020".               
011550                                                                  
011552   05  WS-RMD-LEF-TABLE-3-2022 REDEFINES RMD-LEF-TABLE-3-2022.    
011554       10  WS-RMD-TBL3-2022-LEF      PIC 999 OCCURS 49 TIMES.     
011556                                                                  
011558 01  TEMP-01.                                                     
011560     02  GWS-PRINT-LABEL.                                         
011562     05  GWS-FAMILY.                                              
011564         10  GWS-APPL.                                            
011566             15  GWS-APPL-1X         PIC X(01) VALUE "C".         
011568             15  FILLER              PIC X(02) VALUE "SI".        
011570         10  GWS-CST-PERIOD          PIC X(01) VALUE "0".         
011572         10  GWS-FILE-TYPE           PIC X(01) VALUE "P".         
011574         10  GWS-NO-PARTS.                                        
011576             15  GWS-NO-PART-ZONE    PIC 9(01) COMP.              
011578             15  GWS-NO-PART-NUMERIC PIC 9(01) VALUE @1@ COMP.    
011580         10  GWS-PRT-DESCRIPTOR      PIC X(02) VALUE "SP".        
011582         10  GWS-BRANCH-CODE         PIC X(02) VALUE "00".        
011584     05  GWS-SLASH                   PIC X(01) VALUE "/".         
011586     05  GWS-ELEM.                                                
011588         10  GWS-MICRO-BANK.                                      
011590             15  GWS-MICROFICHE-CODE PIC X(01) VALUE "0".         
011592             15  GWS-BANK-NO-X.                                   
011594                 20  GWS-BANK-NUMBER PIC 9(03) VALUE ZEROS.       
011596         10  GWS-TIME.                                            
011598             15  FILLER              PIC X(04) VALUE "0000".      
011600             15  GWS-MISC            PIC X(02) VALUE "00".        
011602     05  GWS-ON                      PIC X(04) VALUE " ON ".      
011604     05  GWS-PACK                    PIC X(10) VALUE SPACES.      
011606     05  GWS-PERIOD                  PIC X(01) VALUE SPACE.       
011608     05  FILLER                      PIC X(11) VALUE SPACES.      
011610    02  GWS-PRT-LABEL   REDEFINES GWS-PRINT-LABEL.                
011612         05  GWS-PRT-LABEL-1-15          PIC X(15).               
011614         05  FILLER                      PIC X(32).               
011616                                                                  
011618 01 WS-FM-OPS-DISP               PIC 9(01) VALUE 0.               
011620 01 RPT601-BANNER-HEADER         PIC 9(01) VALUE 0.               
011622 01 RMD-DC                       PIC 9(02).                       
011624 01 RMD-BK                       PIC 9(04).                       
011626 01 RMD-BK-NAME                  PIC X(30).                       
011628 01 RMD-COUNT                    PIC 9(08).                       
011630 01 RMD-COUNT-INHERIT            PIC 9(08).                       
011632 01 RMD-TOT-CHGD                 PIC 9(08).                       
011634 01 RMD-TOT-CHGD-INHERIT         PIC 9(08).                       
011636 01 WS-GRP-1.                                                     
011638    05 FILLER                    PIC X(01) VALUE "/".             
011640    05 WS-DATA-CENTER            PIC 9(02).                       
011642    05 WS-BK-NO                  PIC 9(04).                       
011644    05 FILLER                    PIC X(01) VALUE "/".             
011646 01 WS-GRP-2.                                                     
011648    05 FILLER                    PIC X(03) VALUE "CSI".           
011650    05 WS-CSI-DAY                PIC 9(02).                       
011652    05 WS-CSI-TIME               PIC 9(04).                       
011654 01 WS-ACCEPT                    PIC X(01).                       
011656 01 WS-BANK-OPT                  PIC 9(01).                       
011658 01 WS-BANK-NO                   PIC 9(04).                       
011660 01 WS-BANK-LIST.                                                 
011662    05 WS-BK-LIST-TBL   OCCURS 20 TIMES.                          
011664       10 WS-BK-LNO              PIC 9(04).                       
011666    05 WS-BK-RMD-ID-TBL OCCURS 20 TIMES.                          
011668       10 WS-BK-RMD-ID           PIC X(31).                       
011670 01 WS-BKSUB                     PIC 9(02) VALUE ZEROS.           
011672 01 WS-DC                        PIC 9(02).                       
011674 01 WS-MDRPT-OPEN                PIC 9(01).                       
011676 01 WS-MDRPT2-OPEN               PIC 9(01).                       
011678 01 WS-DSTFM-OPEN                PIC 9(01) VALUE ZEROS.           
011680 01 WS-CSTFM-OPEN                PIC 9(01) VALUE ZEROS.           
011682 01 WS-RMDFM2-CUST-IND           PIC 9(01) VALUE ZEROS.           
011684 01 WS-PROCFILE-TITLE.                                            
011686    05 FILLER                    PIC X(10) VALUE "TDA/DAILY/".    
011688    05 WS-PROCFILE-DAY           PIC X(03) VALUE "TUE".           
011690    05 FILLER                    PIC X(11) VALUE " ON GENERAL".   
011692    05 FILLER                    PIC X(01) VALUE ".".             
011694 01 WS-RMD-DATE.                                                  
011696    05 WS-RMD-DATE-CCYY          PIC 9(04) VALUE ZEROS.           
011698    05 WS-RMD-DATE-MMDD          PIC 9(04) VALUE ZEROS.           
011700 01 WS-DATE-CCYYMMDD.                                             
011702    05 WS-DATE-CCYY              PIC 9(04) VALUE ZEROS.           
011704    05 WS-DATE-MMDD              PIC 9(04) VALUE ZEROS.           
011706                                                                  
011708 01  SPECS-BANK-TABLE.                                            
011710     05  SPEC-BK-TBL OCCURS 1000 TIMES.                           
011712         10 SPEC-BK-NO-TBL        PIC 9(04).                      
011714         10 SPEC-BK-DC-TBL        PIC 9(02).                      
011716         10 SPEC-BK-RMT-IND-TBL   PIC X(02).                      
011718                                                                  
011720 01  WS-DSREC-FLAG                PIC 9(01) VALUE 0.              
011722 01  WS-NEW-DS-AMT                PIC 9(09)V99.                   
011724 01  WS-FM-AMT-X.                                                 
011726     05  FILLER                   PIC X(23).                      
011728     05  WS-FM-AMT                PIC S9(15)V99.                  
011730 01  WS-FM-LEF-X.                                                 
011732     05  FILLER                   PIC X(37).                      
011734     05  WS-FM-LEF                PIC 99V9.                       
011736 01  WS-FM-AMT-CD-X.                                              
011738     05  FILLER                   PIC X(39).                      
011740     05  WS-FM-AMT-CD             PIC 9.                          
011742                                                                  
011744 01  WS-DSTFM-ID.                                                 
011746     05  FILLER                   PIC X(06) VALUE "RIN0D/".       
011748     05  FILLER                   PIC X(04) VALUE "TDA/".         
011750     05  WS-DSTFM-DT              PIC 9(04).                      
011752     05  FILLER                   PIC X(01) VALUE "/".            
011754     05  WS-DSTFM-BK              PIC 9(03).                      
011756     05  FILLER                   PIC X(07) VALUE "/RMDDST".      
011758     05  WS-DSTFM-TIME            PIC X(04).                      
011760     05  WS-DSTFM-SUFF-R REDEFINES WS-DSTFM-TIME.                 
011762         10  WS-DSTFM-SUFF        PIC X(01).                      
011764         10  FILLER               PIC X(03).                      
011766     05  FILLER                   PIC X(01) VALUE ".".            
011768                                                                  
011770 01  WS-CSTFM-ID.                                                 
011772     05  FILLER                   PIC X(06) VALUE "RIN0D/".       
011774     05  FILLER                   PIC X(04) VALUE "TDA/".         
011776     05  WS-CSTFM-DT              PIC 9(04).                      
011778     05  FILLER                   PIC X(01) VALUE "/".            
011780     05  WS-CSTFM-BK              PIC 9(03).                      
011782     05  FILLER                   PIC X(07) VALUE "/RMDCST".      
011784     05  WS-CSTFM-TIME            PIC X(04).                      
011786     05  WS-CSTFM-SUFF-R REDEFINES WS-CSTFM-TIME.                 
011788         10  WS-CSTFM-SUFF        PIC X(01).                      
011790         10  FILLER               PIC X(03).                      
011792     05  FILLER                   PIC X(01) VALUE ".".            
011794                                                                  
011796 01  WS-PREV-TIN                 PIC 9(09) VALUE ZEROS.           
011798 01  WS-1ST-TIME                 PIC 9(01) VALUE 0.               
011800 01  WS-INHERIT-IRA-ON-TIN       PIC 9(01) VALUE 0.               
011802 01  WS-NON-INHERIT-IRA-ON-TIN   PIC 9(01) VALUE 0.               
011804 01  WS-TIN-TOTALS.                                               
011806     05  WS-TIN-BAL-TOT          PIC S9(11)V99.                   
011808     05  WS-TIN-RMD-TOT          PIC S9(11)V99.                   
011810 01  WS-MULTI-DISTR              PIC 9(01) VALUE 0.               
011812 01  WS-IRA-DISTR-RECS           PIC 9(01) VALUE 0.               
011814 01  WS-RMDRPT-FIELDS.                                            
011816     05  WS-RMDRPT-DS-FREQ       PIC X(01).                       
011818     05  WS-RMDRPT-DS-NTRVL      PIC X(04).                       
011820     05  WS-RMDRPT-DS-METH       PIC X(04).                       
011822     05  WS-RMDRPT-OLD-DS-AMT    PIC 9(09)V9(02).                 
011824                                                                  
011826 01  WS-RMDRPT-TIN-X.                                             
011828     05  WS-RMDRPT-TIN           PIC 999B99B9999.                 
011830     05  WS-RMDRPT-TIN-R REDEFINES WS-RMDRPT-TIN.                 
011832         10  FILLER              PIC 9(03).                       
011834         10  WS-RMDRPT-TIN-LDASH PIC X(01).                       
011836         10  FILLER              PIC 9(02).                       
011838         10  WS-RMDRPT-TIN-RDASH PIC X(01).                       
011840         10  FILLER              PIC 9(04).                       
011842                                                                  
011844 01  WS-RMDRPT2-TIN-X.                                            
011846     05  WS-RMDRPT2-TIN          PIC 999B99B9999.                 
011848     05  WS-RMDRPT2-TIN-R REDEFINES WS-RMDRPT2-TIN.               
011850         10  FILLER              PIC 9(03).                       
011852         10  WS-RMDRPT2-TIN-LDASH PIC X(01).                      
011854         10  FILLER              PIC 9(02).                       
011856         10  WS-RMDRPT2-TIN-RDASH PIC X(01).                      
011858         10  FILLER              PIC 9(04).                       
011860                                                                  
011862 01  WS-TIN-CUST-INDEX           PIC 9(03) VALUE 0.               
011864 01  WS-TIN-CUST-TABLE.                                           
011866     05  WS-TIN-CUST-TBL OCCURS 50 TIMES.                         
011868         10  WS-TIN-CUST         PIC 9(12).                       
011870                                                                  
011872 01  WS-TIN-RMD-INDEX            PIC 9(03) VALUE 0.               
011874 01  WS-TIN-RMD-MAX              PIC 9(03) VALUE 50.              
011876 01  WS-TIN-RMD-TABLE.                                            
011878     05  WS-TIN-RMD-TBL OCCURS 50 TIMES.                          
011880         10  WS-TIN-RMD-CUST     PIC 9(12).                       
011882         10  WS-TIN-RMD-ACCT     PIC 9(10).                       
011884         10  WS-TIN-RMD-DS-NBR   PIC 9(02).                       
011886         10  WS-TIN-RMD-DS-FREQ  PIC 9(01).                       
011888         10  WS-TIN-RMD-DS-NTRVL PIC 9(04).                       
011890         10  WS-TIN-RMD-AMT      PIC 9(9)V9(2).                   
011892                                                                  
011894 01  WS-TIN-DETAIL-INDEX         PIC 9(03) VALUE 0.               
011896 01  WS-TIN-DETAIL-MAX           PIC 9(03) VALUE 100.             
011898 01  WS-TIN-DETAIL-TABLE.                                         
011900     05  WS-TIN-DETAIL-TBL OCCURS 100 TIMES.                      
011902         10  WS-TIN-DET-LINE-3.                                   
011904             15  FILLER                  PIC X(100).              
011906             15  WS-TIN-DET-DIST-NTRVL.                           
011908                 20  WS-TIN-DET-DS-NTRVL PIC 9(4).                
011910             15  FILLER                  PIC X(1).                
011912             15  WS-TIN-DET-DIST-FREQ    PIC X(1).                
011914             15  FILLER                  PIC X(54).               
011916         10  WS-TIN-DET-LINE-4       PIC X(160).                  
011918         10  WS-TIN-DET-LINE-8       PIC X(160).                  
011920                                                                  
011922 01  WS-TIN-DISTR-RECS           PIC 9(2) VALUE 0.                
011924 01  WS-PAGE-CNT-FICHE           PIC 9(4).                        
011926                                                                  
011928 01  RMDRPT-REC-2.                                                
011930     02  Z-VA-RMDRPT-REC-2.                                       
011932     05  FILLER                PIC  X(00050) VALUE                
011934     "   CUSTOMER/   ACCOUNT   BIRTHDATE   RMD AGE    RM".        
011936     05  FILLER                PIC  X(00050) VALUE                
011938     "D DATE    BAL AS OF      LE FACTR/ REQ ANNUAL   DI".        
011940     05  FILLER                PIC  X(00050) VALUE                
011942     "ST FREQ   OLD DIST   NEW DIST                     ".        
011944     05  FILLER                PIC  X(00010) VALUE                
011946     "          ".                                                
011948     02  Z-NX-RMDRPT-REC-2     REDEFINES Z-VA-RMDRPT-REC-2.       
011950     05  FILLER                PIC X(0160).                       
011952* 003 LINE RECORD FOLLOWS                                         
011954 01  RMDRPT-REC-6.                                                
011956     02  Z-VA-RMDRPT-REC-6.                                       
011958     05  FILLER                PIC  X(00050) VALUE                
011960     "    NAME                              DATE        ".        
011962     05  FILLER                PIC  X(00050) VALUE                
011964     "            12/31           TBL     MIN DIST     /".        
011966     05  FILLER                PIC  X(00050) VALUE                
011968     "METHOD       AMT        AMT                       ".        
011970     05  FILLER                PIC  X(00010) VALUE                
011972     "          ".                                                
011974     02  Z-NX-RMDRPT-REC-6     REDEFINES Z-VA-RMDRPT-REC-6.       
011976     05  FILLER                PIC X(0160).                       
011978* 007 LINE RECORD FOLLOWS                                         
011980 01  RMDRPT2-REC-2.                                               
011982     02  Z-VA-RMDRPT2-REC-2.                                      
011984     05  FILLER                PIC  X(00050) VALUE                
011986     "   CUSTOMER/   ACCOUNT    BIRTHDATE    RMD AGE    ".        
011988     05  FILLER                PIC  X(00050) VALUE                
011990     " RMD DATE    OWNER DTH  BAL AS OF      LE FACTR/ R".        
011992     05  FILLER                PIC  X(00050) VALUE                
011994     "EQ ANNUAL   DIST FREQ   OLD DIST   NEW DIST       ".        
011996     05  FILLER                PIC  X(00010) VALUE                
011998     "          ".                                                
012000     02  Z-NX-RMDRPT2-REC-2    REDEFINES Z-VA-RMDRPT2-REC-2.      
012002     05  FILLER                PIC X(0160).                       
012004* 003 LINE RECORD FOLLOWS                                         
012006 01  RMDRPT2-REC-6.                                               
012008     02  Z-VA-RMDRPT2-REC-6.                                      
012010     05  FILLER                PIC  X(00050) VALUE                
012012     "    NAME                                DATE      ".        
012014     05  FILLER                PIC  X(00050) VALUE                
012016     "               DATE       12/31           TBL     ".        
012018     05  FILLER                PIC  X(00050) VALUE                
012020     "MIN DIST     /METHOD       AMT        AMT         ".        
012022     05  FILLER                PIC  X(00010) VALUE                
012024     "          ".                                                
012026     02  Z-NX-RMDRPT2-REC-6    REDEFINES Z-VA-RMDRPT2-REC-6.      
012028     05  FILLER                PIC X(0160).                       
012030* 007 LINE RECORD FOLLOWS                                         
012032 01  WS-USER-AND-TDB-AREA.                                        
012034   03  WS-USER-AREA.                                              
012036**  The following data items can be used across multiple          
012038**  processes.                                                    
012040     05  WS-RPT465-AREA.                                          
012042         10 WS-RPT465-AR-ACTV-TYPE                PIC 9(02).      
012044         10 WS-RPT465-AR-ACTV-UNPOST              PIC 9(01).      
012046         10 WS-RPT465-AR-DEP-CDE                  PIC X(03).      
012048         10 WS-RPT465-AR-TRANS-AMT                PIC 9(09)V99.   
012050         10 FILLER                                PIC X(09).      
012052                                                                  
012054     05  WS-CMAT-WITHHOLD         PIC S9(09)V99.                  
012056                                                                  
012058     05  WS-TISA-DT               PIC 9(08) VALUE 19930621.       
012060     05  WS-WORK-AREA-HOST        PIC X(256) VALUE SPACES.        
012062     05  WS-SYS-HOST              PIC X(17)  VALUE SPACES.        
012064                                                                  
012066     05  WS-SERIAL-NO             PIC 9(12).                      
012068     05  WS-SERIAL-NO-RE  REDEFINES  WS-SERIAL-NO.                
012070         10  WS-SERIAL-DT-X.                                      
012072             15  WS-SERIAL-DT     PIC 9(7).                       
012074         10  WS-SERIAL-TM-X.                                      
012076             15  WS-SERIAL-TM     PIC 9(5).                       
012078                                                                  
012080     05  GWS-INITIALIZE-IND       PIC X(1)  VALUE "N".            
012082         88 INITIALIZE-GWS                  VALUE "Y".            
012084                                                                  
012086     05  WS-SPEC-TDA-ADD-DAY.                                     
012088         10 FILLER                PIC X(02).                      
012090         10 WS-SPEC-TDA-SUFFIX    PIC X.                          
012092                                                                  
012094     05  WS-RUNNING-BAL           PIC S9(12)V99 VALUE 0.          
012096     05  WS-HMS-LOW-HOLD-NBR      PIC 9999  VALUE 0.              
012098     05  WS-ACCR-TO-POST          PIC S9(10)V9(4).                
012100     05  WS-POST-AMT              PIC S9(10)V9(2).                
012102     05  WS-SWITCH                PIC 9     VALUE 0.              
012104                                                                  
012106     05  SCREEN-SUB               PIC 999   VALUE ZEROS.          
012108                                                                  
012110     05  WS-CALC-ERROR-FLD        PIC X(12).                      
012112     05  PREVIOUS-ERROR-NBR       PIC 9(04).                      
012114                                                                  
012116     05  WS-SPECS-GRACE-CLOSE     PIC 99.                         
012118                                                                  
012120     05  MAX-DISTR                PIC 99 VALUE 2.                 
012122     05  WS-NEW-DS-NBR            PIC 99 VALUE 0.                 
012124                                                                  
012126                                                                  
012128     05  WS-DIST-CLOSE            PIC 9(01) VALUE 0.              
012130                                                                  
012132     05  WS-TRGR-DEL-TABLE-X.                                     
012134         10  WS-TRGR-DEL-TABLE OCCURS 20 TIMES.                   
012136             15 TRGR-DEL-BANK    PIC 9(04).                       
012138             15 TRGR-DEL-RPT-NBR PIC 999.                         
012140             15 TRGR-DEL-APPL    PIC 9.                           
012142             15 TRGR-DEL-CUST    PIC 9(12).                       
012144             15 TRGR-DEL-ACCT    PIC 9(10).                       
012146             15 TRGR-DEL-PRT-DT  PIC 9(08).                       
012148             15 TRGR-DEL-SEQ-NBR PIC 9(04).                       
012150     05  WS-ACTV-DEL-TABLE-X.                                     
012152         10  WS-ACTV-DEL-TABLE OCCURS 20 TIMES.                   
012154            15  ACTV-DEL-BANK    PIC 9(04).                       
012156            15  ACTV-DEL-DATE    PIC 9(08).                       
012158            15  ACTV-DEL-CUST    PIC 9(12).                       
012160            15  ACTV-DEL-ACCT    PIC 9(10).                       
012162            15  ACTV-DEL-TIME    PIC 9(08).                       
012164            15  ACTV-DEL-SEQ-NBR PIC 9(02).                       
012166                                                                  
012168     05  ACTV-DEL-NDX            PIC 99.                          
012170     05  TRGR-DEL-NDX            PIC 99.                          
012172     05  HMS-ROLBAK-NDX          PIC 99.                          
012174     05  DISTR-ROLBAK-NDX        PIC 99.                          
012176                                                                  
012178                                                                  
012180     05 WS-ADDR-ALT-EMAIL        PIC X(100).                      
012182     05 WS-ADDR-ALT-EMAIL-R REDEFINES                             
012184        WS-ADDR-ALT-EMAIL.                                        
012186        10 WS-ADDR-ALT-EMAIL-1   PIC X(40).                       
012188        10 WS-ADDR-ALT-EMAIL-2   PIC X(40).                       
012190        10 WS-ADDR-ALT-EMAIL-3   PIC X(20).                       
012192     05 WS-OLD-ALT-EMAIL        PIC X(100).                       
012194     05 WS-OLD-ALT-EMAIL-R REDEFINES                              
012196        WS-OLD-ALT-EMAIL.                                         
012198        10 WS-OLD-ALT-EMAIL-1   PIC X(40).                        
012200        10 WS-OLD-ALT-EMAIL-2   PIC X(40).                        
012202        10 WS-OLD-ALT-EMAIL-3   PIC X(20).                        
012204     05 WS-ADDR-TEMP-EMAIL       PIC X(100).                      
012206     05 WS-ADDR-TEMP-EMAIL-R REDEFINES                            
012208        WS-ADDR-TEMP-EMAIL.                                       
012210        10 WS-ADDR-TEMP-EMAIL-1  PIC X(40).                       
012212        10 WS-ADDR-TEMP-EMAIL-2  PIC X(40).                       
012214        10 WS-ADDR-TEMP-EMAIL-3  PIC X(20).                       
012216     05 OLD-ADDR-TEMP-EMAIL      PIC X(100).                      
012218     05 OLD-ADDR-TEMP-EMAIL-R REDEFINES                           
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 343 lines from 5763 to 6105.

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

