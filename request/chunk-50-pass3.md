# LLM Request Debug File
Generated: 2025-11-13T21:56:27.959519

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 50/55
- **Model**: gpt-4.1
- **Chunk Number**: 50
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~9,803 tokens
- **Total Input**: ~11,761 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 50/55" (ID: detailed-code-explanation)

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


**CHUNK 50 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 50 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 23894 to 24375 (482 lines)\nChunk Tokens (estimated): ~8,065\nActual Input Tokens: 9,471 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 23894-24375 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 50 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 50 of 55.\n\n\n=============================================================================\nCHUNK 50 SOURCE CODE (Lines 23894-24375)\n=============================================================================\n\n```cobol\n047796         HOLD-TDACUST.\n047798     MOVE TDAC-N1-MID OF TDACUST TO HOLD-TDAC-N1-MID OF           \n047800         HOLD-TDACUST.\n047802     MOVE TDAC-N1-LAST OF TDACUST TO HOLD-TDAC-N1-LAST OF         \n047804         HOLD-TDACUST.\n047806     MOVE TDAC-N1-PREFIX OF TDACUST TO HOLD-TDAC-N1-PREFIX OF     \n047808         HOLD-TDACUST.\n047810     MOVE TDAC-N1-SUFFIX OF TDACUST TO HOLD-TDAC-N1-SUFFIX OF     \n047812         HOLD-TDACUST.\n047814     MOVE TDAC-N1-FAMILIAR OF TDACUST TO HOLD-TDAC-N1-FAMILIAR OF \n047816         HOLD-TDACUST.\n047818     MOVE TDAC-N1-PRT-PFX OF TDACUST TO HOLD-TDAC-N1-PRT-PFX OF   \n047820         HOLD-TDACUST.\n047822     MOVE TDAC-N1-PRT-SFX OF TDACUST TO HOLD-TDAC-N1-PRT-SFX OF   \n047824         HOLD-TDACUST.\n047826     MOVE TDAC-N1-DESIGNAT OF TDACUST TO HOLD-TDAC-N1-DESIGNAT OF \n047828         HOLD-TDACUST.\n047830     MOVE TDAC-NAME-2 OF TDACUST TO HOLD-TDAC-NAME-2 OF           \n047832         HOLD-TDACUST.\n047834     MOVE TDAC-N2-MODIFIED OF TDACUST TO HOLD-TDAC-N2-MODIFIED OF \n047836         HOLD-TDACUST.\n047838     MOVE TDAC-N2-PRINT-CD OF TDACUST TO HOLD-TDAC-N2-PRINT-CD OF \n047840         HOLD-TDACUST.\n047842     MOVE TDAC-N2-KEY OF TDACUST TO HOLD-TDAC-N2-KEY OF           \n047844         HOLD-TDACUST.\n047846     MOVE TDAC-N2-FIRST OF TDACUST TO HOLD-TDAC-N2-FIRST OF       \n047848         HOLD-TDACUST.\n047850     MOVE TDAC-N2-MID OF TDACUST TO HOLD-TDAC-N2-MID OF           \n047852         HOLD-TDACUST.\n047854     MOVE TDAC-N2-LAST OF TDACUST TO HOLD-TDAC-N2-LAST OF         \n047856         HOLD-TDACUST.\n047858     MOVE TDAC-N2-PREFIX OF TDACUST TO HOLD-TDAC-N2-PREFIX OF     \n047860         HOLD-TDACUST.\n047862     MOVE TDAC-N2-SUFFIX OF TDACUST TO HOLD-TDAC-N2-SUFFIX OF     \n047864         HOLD-TDACUST.\n047866     MOVE TDAC-N2-FAMILIAR OF TDACUST TO HOLD-TDAC-N2-FAMILIAR OF \n047868         HOLD-TDACUST.\n047870     MOVE TDAC-N2-PRT-PFX OF TDACUST TO HOLD-TDAC-N2-PRT-PFX OF   \n047872         HOLD-TDACUST.\n047874     MOVE TDAC-N2-PRT-SFX OF TDACUST TO HOLD-TDAC-N2-PRT-SFX OF   \n047876         HOLD-TDACUST.\n047878     MOVE TDAC-N2-DESIGNAT OF TDACUST TO HOLD-TDAC-N2-DESIGNAT OF \n047880         HOLD-TDACUST.\n047882     MOVE TDAC-NAME-3 OF TDACUST TO HOLD-TDAC-NAME-3 OF           \n047884         HOLD-TDACUST.\n047886     MOVE TDAC-N3-MODIFIED OF TDACUST TO HOLD-TDAC-N3-MODIFIED OF \n047888         HOLD-TDACUST.\n047890     MOVE TDAC-N3-PRINT-CD OF TDACUST TO HOLD-TDAC-N3-PRINT-CD OF \n047892         HOLD-TDACUST.\n047894     MOVE TDAC-N3-KEY OF TDACUST TO HOLD-TDAC-N3-KEY OF           \n047896         HOLD-TDACUST.\n047898     MOVE TDAC-N3-FIRST OF TDACUST TO HOLD-TDAC-N3-FIRST OF       \n047900         HOLD-TDACUST.\n047902     MOVE TDAC-N3-MID OF TDACUST TO HOLD-TDAC-N3-MID OF           \n047904         HOLD-TDACUST.\n047906     MOVE TDAC-N3-LAST OF TDACUST TO HOLD-TDAC-N3-LAST OF         \n047908         HOLD-TDACUST.\n047910     MOVE TDAC-N3-PREFIX OF TDACUST TO HOLD-TDAC-N3-PREFIX OF     \n047912         HOLD-TDACUST.\n047914     MOVE TDAC-N3-SUFFIX OF TDACUST TO HOLD-TDAC-N3-SUFFIX OF     \n047916         HOLD-TDACUST.\n047918     MOVE TDAC-N3-FAMILIAR OF TDACUST TO HOLD-TDAC-N3-FAMILIAR OF \n047920         HOLD-TDACUST.\n047922     MOVE TDAC-N3-PRT-PFX OF TDACUST TO HOLD-TDAC-N3-PRT-PFX OF   \n047924         HOLD-TDACUST.\n047926     MOVE TDAC-N3-PRT-SFX OF TDACUST TO HOLD-TDAC-N3-PRT-SFX OF   \n047928         HOLD-TDACUST.\n047930     MOVE TDAC-N3-DESIGNAT OF TDACUST TO HOLD-TDAC-N3-DESIGNAT OF \n047932         HOLD-TDACUST.\n047934     MOVE TDAC-ADDR-KEY OF TDACUST TO HOLD-TDAC-ADDR-KEY OF       \n047936         HOLD-TDACUST.\n047938     MOVE TDAC-ADDR-1 OF TDACUST TO HOLD-TDAC-ADDR-1 OF           \n047940         HOLD-TDACUST.\n047942     MOVE TDAC-ADDR-2 OF TDACUST TO HOLD-TDAC-ADDR-2 OF           \n047944         HOLD-TDACUST.\n047946     MOVE TDAC-CITY OF TDACUST TO HOLD-TDAC-CITY OF HOLD-TDACUST.\n047948     MOVE TDAC-STATE OF TDACUST TO HOLD-TDAC-STATE OF             \n047950         HOLD-TDACUST.\n047952     MOVE TDAC-PROVINCE OF TDACUST TO HOLD-TDAC-PROVINCE OF       \n047954         HOLD-TDACUST.\n047956     MOVE TDAC-COUNTRY OF TDACUST TO HOLD-TDAC-COUNTRY OF         \n047958         HOLD-TDACUST.\n047960     MOVE TDAC-ZIP OF TDACUST TO HOLD-TDAC-ZIP OF HOLD-TDACUST.\n047962     MOVE TDAC-ZIP-4 OF TDACUST TO HOLD-TDAC-ZIP-4 OF             \n047964         HOLD-TDACUST.\n047966     MOVE TDAC-LONGITUDE OF TDACUST TO HOLD-TDAC-LONGITUDE OF     \n047968         HOLD-TDACUST.\n047970     MOVE TDAC-LATITUDE OF TDACUST TO HOLD-TDAC-LATITUDE OF       \n047972         HOLD-TDACUST.\n047974     MOVE TDAC-MAIL-CD OF TDACUST TO HOLD-TDAC-MAIL-CD OF         \n047976         HOLD-TDACUST.\n047978     MOVE TDAC-TICKLER-FLAG OF TDACUST TO HOLD-TDAC-TICKLER-FLAG  \n047980         OF HOLD-TDACUST.\n047982     MOVE TDAC-RESIDENT-CD OF TDACUST TO HOLD-TDAC-RESIDENT-CD OF \n047984         HOLD-TDACUST.\n047986     MOVE TDAC-ALIEN-CD OF TDACUST TO HOLD-TDAC-ALIEN-CD OF       \n047988         HOLD-TDACUST.\n047990     MOVE TDAC-SHT-NAME OF TDACUST TO HOLD-TDAC-SHT-NAME OF       \n047992         HOLD-TDACUST.\n047994     MOVE TDAC-BAR-CD OF TDACUST TO HOLD-TDAC-BAR-CD OF           \n047996         HOLD-TDACUST.\n047998     MOVE TDAC-PHONE-1 OF TDACUST TO HOLD-TDAC-PHONE-1 OF         \n048000         HOLD-TDACUST.\n048002     MOVE TDAC-PHONE-2 OF TDACUST TO HOLD-TDAC-PHONE-2 OF         \n048004         HOLD-TDACUST.\n048006     MOVE TDAC-TIN-CD OF TDACUST TO HOLD-TDAC-TIN-CD OF           \n048008         HOLD-TDACUST.\n048010     MOVE TDAC-TIN-CERT-CD OF TDACUST TO HOLD-TDAC-TIN-CERT-CD OF \n048012         HOLD-TDACUST.\n048014     MOVE TDAC-TIN-CERT-DT OF TDACUST TO HOLD-TDAC-TIN-CERT-DT OF \n048016         HOLD-TDACUST.\n048018     MOVE TDAC-TIN-NBR OF TDACUST TO HOLD-TDAC-TIN-NBR OF         \n048020         HOLD-TDACUST.\n048022     MOVE TDAC-OFFICER OF TDACUST TO HOLD-TDAC-OFFICER OF         \n048024         HOLD-TDACUST.\n048026     MOVE TDAC-EMP-CD OF TDACUST TO HOLD-TDAC-EMP-CD OF           \n048028         HOLD-TDACUST.\n048030     MOVE TDAC-FREE-MARK OF TDACUST TO HOLD-TDAC-FREE-MARK OF     \n048032         HOLD-TDACUST.\n048034     MOVE TDAC-INQ-SECR-CD OF TDACUST TO HOLD-TDAC-INQ-SECR-CD OF \n048036         HOLD-TDACUST.\n048038     MOVE TDAC-PRIVACY OF TDACUST TO HOLD-TDAC-PRIVACY OF         \n048040         HOLD-TDACUST.\n048042     MOVE TDAC-BK-DEF-CD1 OF TDACUST TO HOLD-TDAC-BK-DEF-CD1 OF   \n048044         HOLD-TDACUST.\n048046     MOVE TDAC-BK-DEF-CD2 OF TDACUST TO HOLD-TDAC-BK-DEF-CD2 OF   \n048048         HOLD-TDACUST.\n048050     MOVE TDAC-BK-DEF-CD3 OF TDACUST TO HOLD-TDAC-BK-DEF-CD3 OF   \n048052         HOLD-TDACUST.\n048054     MOVE TDAC-BK-DEF-CD4 OF TDACUST TO HOLD-TDAC-BK-DEF-CD4 OF   \n048056         HOLD-TDACUST.\n048058     MOVE TDAC-BK-DEF-CD5 OF TDACUST TO HOLD-TDAC-BK-DEF-CD5 OF   \n048060         HOLD-TDACUST.\n048062     MOVE TDAC-EMPLOYEE-ID OF TDACUST TO HOLD-TDAC-EMPLOYEE-ID OF \n048064         HOLD-TDACUST.\n048066     MOVE TDAC-EMAIL-ADDR OF TDACUST TO HOLD-TDAC-EMAIL-ADDR OF   \n048068         HOLD-TDACUST.\n048070     MOVE TDAC-EMAIL-PSSWRD OF TDACUST TO HOLD-TDAC-EMAIL-PSSWRD  \n048072         OF HOLD-TDACUST.\n048074     MOVE TDAC-GENDER OF TDACUST TO HOLD-TDAC-GENDER OF           \n048076         HOLD-TDACUST.\n048078     MOVE TDAC-NEW-CUST OF TDACUST TO HOLD-TDAC-NEW-CUST OF       \n048080         HOLD-TDACUST.\n048082     MOVE TDAC-OPEN-DT OF TDACUST TO HOLD-TDAC-OPEN-DT OF         \n048084         HOLD-TDACUST.\n048086     MOVE TDAC-LUPD-DATE OF TDACUST TO HOLD-TDAC-LUPD-DATE OF     \n048088         HOLD-TDACUST.\n048090     MOVE TDAC-LUPD-TIME OF TDACUST TO HOLD-TDAC-LUPD-TIME OF     \n048092         HOLD-TDACUST.\n048094     MOVE TDAC-LST-CONTACT OF TDACUST TO HOLD-TDAC-LST-CONTACT OF \n048096         HOLD-TDACUST.\n048098     MOVE TDAC-BIRTH-DT OF TDACUST TO HOLD-TDAC-BIRTH-DT OF       \n048100         HOLD-TDACUST.\n048102     MOVE TDAC-BIRTH-DT-2 OF TDACUST TO HOLD-TDAC-BIRTH-DT-2 OF   \n048104         HOLD-TDACUST.\n048106     MOVE TDAC-BIRTH-DT-3 OF TDACUST TO HOLD-TDAC-BIRTH-DT-3 OF   \n048108         HOLD-TDACUST.\n048110     MOVE TDAC-DEATH-DT OF TDACUST TO HOLD-TDAC-DEATH-DT OF       \n048112         HOLD-TDACUST.\n048114     MOVE TDAC-ADD-DT OF TDACUST TO HOLD-TDAC-ADD-DT OF           \n048116         HOLD-TDACUST.\n048118     MOVE TDAC-ADD-TM OF TDACUST TO HOLD-TDAC-ADD-TM OF           \n048120         HOLD-TDACUST.\n048122     MOVE TDAC-ROTH-DATE OF TDACUST TO HOLD-TDAC-ROTH-DATE OF     \n048124         HOLD-TDACUST.\n048126     MOVE TDAC-CD-BAL OF TDACUST TO HOLD-TDAC-CD-BAL OF           \n048128         HOLD-TDACUST.\n048130     MOVE TDAC-CD-BAL-BYR OF TDACUST TO HOLD-TDAC-CD-BAL-BYR OF   \n048132         HOLD-TDACUST.\n048134     MOVE TDAC-CD-PENLTY OF TDACUST TO HOLD-TDAC-CD-PENLTY OF     \n048136         HOLD-TDACUST.\n048138     MOVE TDAC-CD-WTHLD OF TDACUST TO HOLD-TDAC-CD-WTHLD OF       \n048140         HOLD-TDACUST.\n048142     MOVE TDAC-CD-INT OF TDACUST TO HOLD-TDAC-CD-INT OF           \n048144         HOLD-TDACUST.\n048146     MOVE TDAC-CD-OID-INT OF TDACUST TO HOLD-TDAC-CD-OID-INT OF   \n048148         HOLD-TDACUST.\n048150     MOVE TDAC-IRA-BAL OF TDACUST TO HOLD-TDAC-IRA-BAL OF         \n048152         HOLD-TDACUST.\n048154     MOVE TDAC-IRA-BAL-BYR OF TDACUST TO HOLD-TDAC-IRA-BAL-BYR OF \n048156         HOLD-TDACUST.\n048158     MOVE TDAC-IRA-PENLTY OF TDACUST TO HOLD-TDAC-IRA-PENLTY OF   \n048160         HOLD-TDACUST.\n048162     MOVE TDAC-IRA-WTHLD OF TDACUST TO HOLD-TDAC-IRA-WTHLD OF     \n048164         HOLD-TDACUST.\n048166     MOVE TDAC-IRA-INT OF TDACUST TO HOLD-TDAC-IRA-INT OF         \n048168         HOLD-TDACUST.\n048170     MOVE TDAC-IRA-CONTR OF TDACUST TO HOLD-TDAC-IRA-CONTR OF     \n048172         HOLD-TDACUST.\n048174     MOVE TDAC-IRA-CONTR-LY OF TDACUST TO HOLD-TDAC-IRA-CONTR-LY  \n048176         OF HOLD-TDACUST.\n048178     MOVE TDAC-IRA-DISTR OF TDACUST TO HOLD-TDAC-IRA-DISTR OF     \n048180         HOLD-TDACUST.\n048182     MOVE TDAC-IRA-DISTR-LY OF TDACUST TO HOLD-TDAC-IRA-DISTR-LY  \n048184         OF HOLD-TDACUST.\n048186     MOVE TDAC-IRA-ROLLOVER OF TDACUST TO HOLD-TDAC-IRA-ROLLOVER  \n048188         OF HOLD-TDACUST.\n048190     MOVE TDAC-IRA-TRF-IN OF TDACUST TO HOLD-TDAC-IRA-TRF-IN OF   \n048192         HOLD-TDACUST.\n048194     MOVE TDAC-IRA-TRF-OUT OF TDACUST TO HOLD-TDAC-IRA-TRF-OUT OF \n048196         HOLD-TDACUST.\n048198     MOVE TDAC-IRA-FAIR-MKT OF TDACUST TO HOLD-TDAC-IRA-FAIR-MKT  \n048200         OF HOLD-TDACUST.\n048202     MOVE TDAC-CIF-REMARK OF TDACUST TO HOLD-TDAC-CIF-REMARK OF   \n048204         HOLD-TDACUST.\n048206     MOVE TDAC-CD-ST-WHLD OF TDACUST TO HOLD-TDAC-CD-ST-WHLD OF   \n048208         HOLD-TDACUST.\n048210     MOVE TDAC-IRA-ST-WHLD OF TDACUST TO HOLD-TDAC-IRA-ST-WHLD OF \n048212         HOLD-TDACUST.\n048214     MOVE 1 TO Z-II.\n048216 Z-32-1-1-LOOP.\n048218     IF Z-II > 12\n048220         GO TO Z-32-1-1-LOOP-XIT.\n048222     MOVE TDAC-CURR-YR-AMT OF TDACUST (Z-II) TO                   \n048224         HOLD-TDAC-CURR-YR-AMT OF HOLD-TDACUST (Z-II).\n048226     MOVE TDAC-LAST-YR-AMT OF TDACUST (Z-II) TO                   \n048228         HOLD-TDAC-LAST-YR-AMT OF HOLD-TDACUST (Z-II).\n048230     ADD 1 TO Z-II.\n048232     GO TO Z-32-1-1-LOOP.\n048234 Z-32-1-1-LOOP-XIT.\n048236     MOVE TDAC-TIN-CD-2 OF TDACUST TO HOLD-TDAC-TIN-CD-2 OF       \n048238         HOLD-TDACUST.\n048240     MOVE TDAC-TIN-CRT-CD-2 OF TDACUST TO HOLD-TDAC-TIN-CRT-CD-2  \n048242         OF HOLD-TDACUST.\n048244     MOVE TDAC-TIN-CRT-DT-2 OF TDACUST TO HOLD-TDAC-TIN-CRT-DT-2  \n048246         OF HOLD-TDACUST.\n048248     MOVE TDAC-TIN-NBR-2 OF TDACUST TO HOLD-TDAC-TIN-NBR-2 OF     \n048250         HOLD-TDACUST.\n048252     MOVE TDAC-TIN-CD-3 OF TDACUST TO HOLD-TDAC-TIN-CD-3 OF       \n048254         HOLD-TDACUST.\n048256     MOVE TDAC-TIN-CRT-CD-3 OF TDACUST TO HOLD-TDAC-TIN-CRT-CD-3  \n048258         OF HOLD-TDACUST.\n048260     MOVE TDAC-TIN-CRT-DT-3 OF TDACUST TO HOLD-TDAC-TIN-CRT-DT-3  \n048262         OF HOLD-TDACUST.\n048264     MOVE TDAC-TIN-NBR-3 OF TDACUST TO HOLD-TDAC-TIN-NBR-3 OF     \n048266         HOLD-TDACUST.\n048268     MOVE TDAC-NAICS-CD OF TDACUST TO HOLD-TDAC-NAICS-CD OF       \n048270         HOLD-TDACUST.\n048272     MOVE TDAC-CIF-PASS-THR OF TDACUST TO HOLD-TDAC-CIF-PASS-THR  \n048274         OF HOLD-TDACUST.\n048276     MOVE TDAC-EMAIL-NTC OF TDACUST TO HOLD-TDAC-EMAIL-NTC OF     \n048278         HOLD-TDACUST.\n048280     MOVE TDAC-RMD-YR-AMT OF TDACUST TO HOLD-TDAC-RMD-YR-AMT OF   \n048282         HOLD-TDACUST.\n048284     MOVE TDAC-ADDR-CHG-DT OF TDACUST TO HOLD-TDAC-ADDR-CHG-DT OF \n048286         HOLD-TDACUST.\n048288     MOVE TDAC-WTHLD-CD OF TDACUST TO HOLD-TDAC-WTHLD-CD OF       \n048290         HOLD-TDACUST.\n048292     MOVE TDAC-ST-WHLD-CD OF TDACUST TO HOLD-TDAC-ST-WHLD-CD OF   \n048294         HOLD-TDACUST.\n048296     MOVE TDAC-WTHLD-AMT OF TDACUST TO HOLD-TDAC-WTHLD-AMT OF     \n048298         HOLD-TDACUST.\n048300     MOVE TDAC-ST-WHLD-AMT OF TDACUST TO HOLD-TDAC-ST-WHLD-AMT OF \n048302         HOLD-TDACUST.\n048304     MOVE TDAC-FOREIGN-LANG OF TDACUST TO HOLD-TDAC-FOREIGN-LANG  \n048306         OF HOLD-TDACUST.\n048308     MOVE TDAC-L-ROLLOVR-DT OF TDACUST TO HOLD-TDAC-L-ROLLOVR-DT  \n048310         OF HOLD-TDACUST.\n048312     MOVE TDAC-CUSTM-FIELDS OF TDACUST TO HOLD-TDAC-CUSTM-FIELDS  \n048314         OF HOLD-TDACUST.\n048316     MOVE TDAC-LLC-NAME OF TDACUST TO HOLD-TDAC-LLC-NAME OF       \n048318         HOLD-TDACUST.\n048320     MOVE TDAC-LLC-TIN-CD OF TDACUST TO HOLD-TDAC-LLC-TIN-CD OF   \n048322         HOLD-TDACUST.\n048324     MOVE TDAC-LLC-TIN OF TDACUST TO HOLD-TDAC-LLC-TIN OF         \n048326         HOLD-TDACUST.\n048328     MOVE TDAC-FOREIGN-PHN OF TDACUST TO HOLD-TDAC-FOREIGN-PHN OF \n048330         HOLD-TDACUST.\n048332     MOVE TDB-READ-DATE TO HOLD-READ-DATE.\n048334     MOVE 04 TO TDB-STRUCT-NBR.\n048336     MOVE SPACES TO TDB-DATA-AREA.\n048338     MOVE ZERO TO Z-FLINFO14-PRES.\n048340     MOVE 15 TO Z-FLINFO14-LAST-SEQ.\n048342     MOVE ZERO TO Z-FLINFO14-SOME.\n048344     SET TDAACTVBKSET OF TDAACTV OF LDBTDADB TO ENDING\n048346         ON EXCEPTION\n048348         MOVE \"TDAACTVBKSET OF TDAACTV OF LDBTDADB\" TO            \n048350             Z-DMS-EXCEPT-STR\n048352         MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n048354         MOVE 15 TO Z-DMS-EXCEPT-SEQ\n048356         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT\n048358         GO TO Z-32-5-XIT.\n048360 Z-32-5-READ.\n048362     FIND TDAACTV OF LDBTDADB VIA PRIOR TDAACTVBKSET OF TDAACTV   \n048364         OF LDBTDADB\n048366     AT TDA-ACTV-BANK = HOLD-TDAC-BANK AND\n048368        TDA-ACTV-CUST = HOLD-TDAC-CUST AND\n048370        TDA-ACTV-ACCT = 0\n048372         ON EXCEPTION\n048374         MOVE 15 TO Z-DMS-EXCEPT-SEQ\n048376         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n048378             GO TO Z-32-5-XIT\n048380         ELSE\n048382             MOVE \"TDAACTVBKSET OF TDAACTV OF LDBTDADB\" TO        \n048384                 Z-DMS-EXCEPT-STR\n048386             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n048388             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n048390\n048392 Z-32-5-PRESENT.\n048394*\n048396     MOVE 1 TO Z-FLINFO14-SOME.\n048398     MOVE 1 TO Z-FLINFO14-PRES.\n048400     GO TO Z-32-5-CONT.\n048402 Z-32-5-XIT.\n048404 Z-32-5-CONT.\n048406     IF TDA-ACTV-DATE < TDB-READ-DATE\n048408         NEXT SENTENCE ELSE\n048410         GO TO Z-32-6-1-ELSE.\n048412     MOVE \"C\" TO WS-ADJUSTED-IND.\n048414 Z-32-6-1-ELSE.\n048416 Z-32-8-LOOP.\n048418     IF Z-FLINFO14-ABSENT OR TDA-ACTV-DATE < TDB-READ-DATE OR     \n048420         TDAACTV (TDA-ACTV-TYPE ) = 6\n048422         GO TO Z-32-8-XIT.\n048424     MOVE 0 TO Z-EXIT-CODE.\n048426     MOVE 9999 TO Z-EXIT-LEVEL.\n048428     MOVE TDA-ACTV-BANK OF TDAACTV TO HOLD-TDA-ACTV-BANK OF       \n048430         HOLD-TDAACTV.\n048432     MOVE TDA-ACTV-BRCH OF TDAACTV TO HOLD-TDA-ACTV-BRCH OF       \n048434         HOLD-TDAACTV.\n048436     MOVE TDA-ACTV-APPL OF TDAACTV TO HOLD-TDA-ACTV-APPL OF       \n048438         HOLD-TDAACTV.\n048440     MOVE TDA-ACTV-CUST OF TDAACTV TO HOLD-TDA-ACTV-CUST OF       \n048442         HOLD-TDAACTV.\n048444     MOVE TDA-ACTV-ACCT OF TDAACTV TO HOLD-TDA-ACTV-ACCT OF       \n048446         HOLD-TDAACTV.\n048448     MOVE TDA-ACTV-TOT-CD OF TDAACTV TO HOLD-TDA-ACTV-TOT-CD OF   \n048450         HOLD-TDAACTV.\n048452     MOVE TDA-ACTV-IGL-GRP OF TDAACTV TO HOLD-TDA-ACTV-IGL-GRP OF \n048454         HOLD-TDAACTV.\n048456     MOVE TDA-ACTV-OFFICER OF TDAACTV TO HOLD-TDA-ACTV-OFFICER OF \n048458         HOLD-TDAACTV.\n048460     MOVE TDA-ACTV-NC-INDC OF TDAACTV TO HOLD-TDA-ACTV-NC-INDC OF \n048462         HOLD-TDAACTV.\n048464     MOVE TDA-ACTV-PROC-FG OF TDAACTV TO HOLD-TDA-ACTV-PROC-FG OF \n048466         HOLD-TDAACTV.\n048468     MOVE TDA-ACTV-EFF-DT OF TDAACTV TO HOLD-TDA-ACTV-EFF-DT OF   \n048470         HOLD-TDAACTV.\n048472     MOVE TDA-ACTV-DATE OF TDAACTV TO HOLD-TDA-ACTV-DATE OF       \n048474         HOLD-TDAACTV.\n048476     MOVE TDA-ACTV-MAINT OF TDAACTV TO HOLD-TDA-ACTV-MAINT OF     \n048478         HOLD-TDAACTV.\n048480     MOVE TDA-ACTV-TIME OF TDAACTV TO HOLD-TDA-ACTV-TIME OF       \n048482         HOLD-TDAACTV.\n048484     MOVE TDA-ACTV-SEQ-NBR OF TDAACTV TO HOLD-TDA-ACTV-SEQ-NBR OF \n048486         HOLD-TDAACTV.\n048488     MOVE TDA-ACTV-SERIAL OF TDAACTV TO HOLD-TDA-ACTV-SERIAL OF   \n048490         HOLD-TDAACTV.\n048492     MOVE TDA-ACTV-SOURCE OF TDAACTV TO HOLD-TDA-ACTV-SOURCE OF   \n048494         HOLD-TDAACTV.\n048496     MOVE TDA-ACTV-ERASED OF TDAACTV TO HOLD-TDA-ACTV-ERASED OF   \n048498         HOLD-TDAACTV.\n048500     MOVE TDA-ACTV-DR-CR OF TDAACTV TO HOLD-TDA-ACTV-DR-CR OF     \n048502         HOLD-TDAACTV.\n048504     MOVE TDA-ACTV-E-PUBID OF TDAACTV TO HOLD-TDA-ACTV-E-PUBID OF \n048506         HOLD-TDAACTV.\n048508     MOVE TDA-ACTV-PUB-ID OF TDAACTV TO HOLD-TDA-ACTV-PUB-ID OF   \n048510         HOLD-TDAACTV.\n048512     MOVE TDA-ACTV-SUB OF TDAACTV TO HOLD-TDA-ACTV-SUB OF         \n048514         HOLD-TDAACTV.\n048516     IF TDAACTV (TDA-ACTV-TYPE ) = 2\n048518         NEXT SENTENCE ELSE\n048520         GO TO Z-32-10-1-ELSE.\n048522     MOVE \"A\" TO WS-ADJUSTED-IND.\n048524     MOVE TDA-ACTVC-CODE TO HOLD-TDA-ACTVC-CODE.\n048526     MOVE TDA-ACTVC-EXCPT TO HOLD-TDA-ACTVC-EXCPT.\n048528     MOVE TDA-ACTVC-CHG-FRM TO HOLD-TDA-ACTVC-CHG-FRM.\n048530     MOVE TDA-ACTVC-CHG-TO TO HOLD-TDA-ACTVC-CHG-TO.\n048532     MOVE TDA-ACTVC-NCREOPN TO HOLD-TDA-ACTVC-NCREOPN.\n048534************ PERFORM TDB-ACTV-ADJUSTMENT\n048536     PERFORM Z-35-PROCEDURE THRU Z-35-XIT.\n048538     IF  Z-EXIT-EDITEXIT\n048540         GO TO Z-32-XIT.\n048542     IF  Z-DMS2-ABORT-FLAG = 1\n048544         GO TO Z-32-XIT.\n048546     IF  Z-EXIT-LEVEL < 0\n048548         GO TO Z-32-8-END.\n048550*\n048552 Z-32-10-1-ELSE.\n048554     MOVE ZERO TO Z-FLINFO14-PRES.\n048556     MOVE 16 TO Z-FLINFO14-LAST-SEQ.\n048558     MOVE ZERO TO Z-FLINFO14-SOME.\n048560 Z-32-18-READ.\n048562     FIND TDAACTV OF LDBTDADB VIA PRIOR TDAACTVBKSET OF TDAACTV   \n048564         OF LDBTDADB\n048566     AT TDA-ACTV-BANK = HOLD-TDAC-BANK AND\n048568        TDA-ACTV-CUST = HOLD-TDAC-CUST AND\n048570        TDA-ACTV-ACCT = 0\n048572         ON EXCEPTION\n048574         MOVE 16 TO Z-DMS-EXCEPT-SEQ\n048576         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n048578             GO TO Z-32-18-XIT\n048580         ELSE\n048582             MOVE \"TDAACTVBKSET OF TDAACTV OF LDBTDADB\" TO        \n048584                 Z-DMS-EXCEPT-STR\n048586             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n048588             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n048590\n048592 Z-32-18-PRESENT.\n048594*\n048596     MOVE 1 TO Z-FLINFO14-SOME.\n048598     MOVE 1 TO Z-FLINFO14-PRES.\n048600     GO TO Z-32-18-CONT.\n048602 Z-32-18-XIT.\n048604 Z-32-18-CONT.\n048606 Z-32-8-END.\n048608     IF Z-EDIT-ERROR\n048610         GO TO Z-32-XIT.\n048612 Z-32-8-SKIP.\n048614     IF Z-EXIT-LEVEL < 1\n048616         GO TO Z-32-END.\n048618     IF Z-EXIT-CODE > 0\n048620         GO TO Z-32-8-XIT.\n048622     GO TO Z-32-8-LOOP.\n048624*\n048626 Z-32-8-XIT.\n048628     MOVE 0 TO Z-EXIT-CODE.\n048630     MOVE 9999 TO Z-EXIT-LEVEL.\n048632     IF TDAACTV (TDA-ACTV-TYPE ) = 6\n048634         NEXT SENTENCE ELSE\n048636         GO TO Z-32-19-1-ELSE.\n048638     MOVE \"N\" TO WS-ADJUSTED-IND.\n048640 Z-32-19-1-ELSE.\n048642 Z-32-END.\n048644     IF Z-EDIT-ERROR\n048646         GO TO Z-32-XIT.\n048648 Z-32-SKIP.\n048650     IF Z-EXIT-LEVEL NOT < 0\n048652         MOVE 0 TO Z-EXIT-CODE\n048654         MOVE 9999 TO Z-EXIT-LEVEL.\n048656 Z-32-XIT.\n048658     EXIT.\n048660*\n048662*****************************************************************\n048664*    PROCEDURE TDB-IRA-01BAT4-ACTV-ADJ\n048666*****************************************************************\n048668 Z-33-PROCEDURE.\n048670*\n048672     MOVE TDAI-BANK OF TDAIRA TO HOLD-TDAI-BANK OF HOLD-TDAIRA.\n048674     MOVE TDAI-BRCH OF TDAIRA TO HOLD-TDAI-BRCH OF HOLD-TDAIRA.\n048676     MOVE TDAI-CUST OF TDAIRA TO HOLD-TDAI-CUST OF HOLD-TDAIRA.\n048678     MOVE TDAI-ACCT OF TDAIRA TO HOLD-TDAI-ACCT OF HOLD-TDAIRA.\n048680     MOVE TDAI-PUB-ID OF TDAIRA TO HOLD-TDAI-PUB-ID OF            \n048682         HOLD-TDAIRA.\n048684     MOVE TDAI-ADD-DT OF TDAIRA TO HOLD-TDAI-ADD-DT OF            \n048686         HOLD-TDAIRA.\n048688     MOVE TDAI-ADD-TM OF TDAIRA TO HOLD-TDAI-ADD-TM OF            \n048690         HOLD-TDAIRA.\n048692     MOVE 1 TO Z-II.\n048694 Z-33-1-1-LOOP.\n048696     IF Z-II > 20\n048698         GO TO Z-33-1-1-LOOP-XIT.\n048700     MOVE TDAI-DS-TYPE OF TDAIRA (Z-II) TO HOLD-TDAI-DS-TYPE OF   \n048702         HOLD-TDAIRA (Z-II).\n048704     MOVE TDAI-CN-TYPE OF TDAIRA (Z-II) TO HOLD-TDAI-CN-TYPE OF   \n048706         HOLD-TDAIRA (Z-II).\n048708     MOVE TDAI-DS-CN-AMT OF TDAIRA (Z-II) TO HOLD-TDAI-DS-CN-AMT  \n048710         OF HOLD-TDAIRA (Z-II).\n048712     MOVE TDAI-DS-PEN-AMT OF TDAIRA (Z-II) TO                     \n048714         HOLD-TDAI-DS-PEN-AMT OF HOLD-TDAIRA (Z-II).\n048716     MOVE TDAI-DS-WTHLD-AMT OF TDAIRA (Z-II) TO                   \n048718         HOLD-TDAI-DS-WTHLD-AMT OF HOLD-TDAIRA (Z-II).\n048720     MOVE TDAI-DS-ST-WH-AMT OF TDAIRA (Z-II) TO                   \n048722         HOLD-TDAI-DS-ST-WH-AMT OF HOLD-TDAIRA (Z-II).\n048724     MOVE TDAI-DS-EXC-EARN OF TDAIRA (Z-II) TO                    \n048726         HOLD-TDAI-DS-EXC-EARN OF HOLD-TDAIRA (Z-II).\n048728     ADD 1 TO Z-II.\n048730     GO TO Z-33-1-1-LOOP.\n048732 Z-33-1-1-LOOP-XIT.\n048734     MOVE TDAI-DS-C-YTD-CNT OF TDAIRA TO HOLD-TDAI-DS-C-YTD-CNT   \n048736         OF HOLD-TDAIRA.\n048738     MOVE TDAI-DS-P-YTD-CNT OF TDAIRA TO HOLD-TDAI-DS-P-YTD-CNT   \n048740         OF HOLD-TDAIRA.\n048742     MOVE TDAI-DS-AMT-C-YTD OF TDAIRA TO HOLD-TDAI-DS-AMT-C-YTD   \n048744         OF HOLD-TDAIRA.\n048746     MOVE TDAI-DS-AMT-P-YTD OF TDAIRA TO HOLD-TDAI-DS-AMT-P-YTD   \n048748         OF HOLD-TDAIRA.\n048750     MOVE TDAI-DS-INT-AMT OF TDAIRA TO HOLD-TDAI-DS-INT-AMT OF    \n048752         HOLD-TDAIRA.\n048754     MOVE TDAI-CN-YTD-CNT OF TDAIRA TO HOLD-TDAI-CN-YTD-CNT OF    \n048756         HOLD-TDAIRA.\n048758     MOVE TDAI-CN-YTD-AMT OF TDAIRA TO HOLD-TDAI-CN-YTD-AMT OF    \n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 482 lines from 23894 to 24375.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 50,
  "total_chunks": 55,
  "start_line": 23894,
  "end_line": 24375,
  "line_count": 482
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
- Source code length: 29780 characters

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
CHUNK 50 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 23894 to 24375 (482 lines)
Chunk Tokens (estimated): ~8,065
Actual Input Tokens: 9,471 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 23894-24375 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 50 of 55 chunks
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
      The source code below is only CHUNK 50 of 55.


=============================================================================
CHUNK 50 SOURCE CODE (Lines 23894-24375)
=============================================================================

```cobol
047796         HOLD-TDACUST.
047798     MOVE TDAC-N1-MID OF TDACUST TO HOLD-TDAC-N1-MID OF           
047800         HOLD-TDACUST.
047802     MOVE TDAC-N1-LAST OF TDACUST TO HOLD-TDAC-N1-LAST OF         
047804         HOLD-TDACUST.
047806     MOVE TDAC-N1-PREFIX OF TDACUST TO HOLD-TDAC-N1-PREFIX OF     
047808         HOLD-TDACUST.
047810     MOVE TDAC-N1-SUFFIX OF TDACUST TO HOLD-TDAC-N1-SUFFIX OF     
047812         HOLD-TDACUST.
047814     MOVE TDAC-N1-FAMILIAR OF TDACUST TO HOLD-TDAC-N1-FAMILIAR OF 
047816         HOLD-TDACUST.
047818     MOVE TDAC-N1-PRT-PFX OF TDACUST TO HOLD-TDAC-N1-PRT-PFX OF   
047820         HOLD-TDACUST.
047822     MOVE TDAC-N1-PRT-SFX OF TDACUST TO HOLD-TDAC-N1-PRT-SFX OF   
047824         HOLD-TDACUST.
047826     MOVE TDAC-N1-DESIGNAT OF TDACUST TO HOLD-TDAC-N1-DESIGNAT OF 
047828         HOLD-TDACUST.
047830     MOVE TDAC-NAME-2 OF TDACUST TO HOLD-TDAC-NAME-2 OF           
047832         HOLD-TDACUST.
047834     MOVE TDAC-N2-MODIFIED OF TDACUST TO HOLD-TDAC-N2-MODIFIED OF 
047836         HOLD-TDACUST.
047838     MOVE TDAC-N2-PRINT-CD OF TDACUST TO HOLD-TDAC-N2-PRINT-CD OF 
047840         HOLD-TDACUST.
047842     MOVE TDAC-N2-KEY OF TDACUST TO HOLD-TDAC-N2-KEY OF           
047844         HOLD-TDACUST.
047846     MOVE TDAC-N2-FIRST OF TDACUST TO HOLD-TDAC-N2-FIRST OF       
047848         HOLD-TDACUST.
047850     MOVE TDAC-N2-MID OF TDACUST TO HOLD-TDAC-N2-MID OF           
047852         HOLD-TDACUST.
047854     MOVE TDAC-N2-LAST OF TDACUST TO HOLD-TDAC-N2-LAST OF         
047856         HOLD-TDACUST.
047858     MOVE TDAC-N2-PREFIX OF TDACUST TO HOLD-TDAC-N2-PREFIX OF     
047860         HOLD-TDACUST.
047862     MOVE TDAC-N2-SUFFIX OF TDACUST TO HOLD-TDAC-N2-SUFFIX OF     
047864         HOLD-TDACUST.
047866     MOVE TDAC-N2-FAMILIAR OF TDACUST TO HOLD-TDAC-N2-FAMILIAR OF 
047868         HOLD-TDACUST.
047870     MOVE TDAC-N2-PRT-PFX OF TDACUST TO HOLD-TDAC-N2-PRT-PFX OF   
047872         HOLD-TDACUST.
047874     MOVE TDAC-N2-PRT-SFX OF TDACUST TO HOLD-TDAC-N2-PRT-SFX OF   
047876         HOLD-TDACUST.
047878     MOVE TDAC-N2-DESIGNAT OF TDACUST TO HOLD-TDAC-N2-DESIGNAT OF 
047880         HOLD-TDACUST.
047882     MOVE TDAC-NAME-3 OF TDACUST TO HOLD-TDAC-NAME-3 OF           
047884         HOLD-TDACUST.
047886     MOVE TDAC-N3-MODIFIED OF TDACUST TO HOLD-TDAC-N3-MODIFIED OF 
047888         HOLD-TDACUST.
047890     MOVE TDAC-N3-PRINT-CD OF TDACUST TO HOLD-TDAC-N3-PRINT-CD OF 
047892         HOLD-TDACUST.
047894     MOVE TDAC-N3-KEY OF TDACUST TO HOLD-TDAC-N3-KEY OF           
047896         HOLD-TDACUST.
047898     MOVE TDAC-N3-FIRST OF TDACUST TO HOLD-TDAC-N3-FIRST OF       
047900         HOLD-TDACUST.
047902     MOVE TDAC-N3-MID OF TDACUST TO HOLD-TDAC-N3-MID OF           
047904         HOLD-TDACUST.
047906     MOVE TDAC-N3-LAST OF TDACUST TO HOLD-TDAC-N3-LAST OF         
047908         HOLD-TDACUST.
047910     MOVE TDAC-N3-PREFIX OF TDACUST TO HOLD-TDAC-N3-PREFIX OF     
047912         HOLD-TDACUST.
047914     MOVE TDAC-N3-SUFFIX OF TDACUST TO HOLD-TDAC-N3-SUFFIX OF     
047916         HOLD-TDACUST.
047918     MOVE TDAC-N3-FAMILIAR OF TDACUST TO HOLD-TDAC-N3-FAMILIAR OF 
047920         HOLD-TDACUST.
047922     MOVE TDAC-N3-PRT-PFX OF TDACUST TO HOLD-TDAC-N3-PRT-PFX OF   
047924         HOLD-TDACUST.
047926     MOVE TDAC-N3-PRT-SFX OF TDACUST TO HOLD-TDAC-N3-PRT-SFX OF   
047928         HOLD-TDACUST.
047930     MOVE TDAC-N3-DESIGNAT OF TDACUST TO HOLD-TDAC-N3-DESIGNAT OF 
047932         HOLD-TDACUST.
047934     MOVE TDAC-ADDR-KEY OF TDACUST TO HOLD-TDAC-ADDR-KEY OF       
047936         HOLD-TDACUST.
047938     MOVE TDAC-ADDR-1 OF TDACUST TO HOLD-TDAC-ADDR-1 OF           
047940         HOLD-TDACUST.
047942     MOVE TDAC-ADDR-2 OF TDACUST TO HOLD-TDAC-ADDR-2 OF           
047944         HOLD-TDACUST.
047946     MOVE TDAC-CITY OF TDACUST TO HOLD-TDAC-CITY OF HOLD-TDACUST.
047948     MOVE TDAC-STATE OF TDACUST TO HOLD-TDAC-STATE OF             
047950         HOLD-TDACUST.
047952     MOVE TDAC-PROVINCE OF TDACUST TO HOLD-TDAC-PROVINCE OF       
047954         HOLD-TDACUST.
047956     MOVE TDAC-COUNTRY OF TDACUST TO HOLD-TDAC-COUNTRY OF         
047958         HOLD-TDACUST.
047960     MOVE TDAC-ZIP OF TDACUST TO HOLD-TDAC-ZIP OF HOLD-TDACUST.
047962     MOVE TDAC-ZIP-4 OF TDACUST TO HOLD-TDAC-ZIP-4 OF             
047964         HOLD-TDACUST.
047966     MOVE TDAC-LONGITUDE OF TDACUST TO HOLD-TDAC-LONGITUDE OF     
047968         HOLD-TDACUST.
047970     MOVE TDAC-LATITUDE OF TDACUST TO HOLD-TDAC-LATITUDE OF       
047972         HOLD-TDACUST.
047974     MOVE TDAC-MAIL-CD OF TDACUST TO HOLD-TDAC-MAIL-CD OF         
047976         HOLD-TDACUST.
047978     MOVE TDAC-TICKLER-FLAG OF TDACUST TO HOLD-TDAC-TICKLER-FLAG  
047980         OF HOLD-TDACUST.
047982     MOVE TDAC-RESIDENT-CD OF TDACUST TO HOLD-TDAC-RESIDENT-CD OF 
047984         HOLD-TDACUST.
047986     MOVE TDAC-ALIEN-CD OF TDACUST TO HOLD-TDAC-ALIEN-CD OF       
047988         HOLD-TDACUST.
047990     MOVE TDAC-SHT-NAME OF TDACUST TO HOLD-TDAC-SHT-NAME OF       
047992         HOLD-TDACUST.
047994     MOVE TDAC-BAR-CD OF TDACUST TO HOLD-TDAC-BAR-CD OF           
047996         HOLD-TDACUST.
047998     MOVE TDAC-PHONE-1 OF TDACUST TO HOLD-TDAC-PHONE-1 OF         
048000         HOLD-TDACUST.
048002     MOVE TDAC-PHONE-2 OF TDACUST TO HOLD-TDAC-PHONE-2 OF         
048004         HOLD-TDACUST.
048006     MOVE TDAC-TIN-CD OF TDACUST TO HOLD-TDAC-TIN-CD OF           
048008         HOLD-TDACUST.
048010     MOVE TDAC-TIN-CERT-CD OF TDACUST TO HOLD-TDAC-TIN-CERT-CD OF 
048012         HOLD-TDACUST.
048014     MOVE TDAC-TIN-CERT-DT OF TDACUST TO HOLD-TDAC-TIN-CERT-DT OF 
048016         HOLD-TDACUST.
048018     MOVE TDAC-TIN-NBR OF TDACUST TO HOLD-TDAC-TIN-NBR OF         
048020         HOLD-TDACUST.
048022     MOVE TDAC-OFFICER OF TDACUST TO HOLD-TDAC-OFFICER OF         
048024         HOLD-TDACUST.
048026     MOVE TDAC-EMP-CD OF TDACUST TO HOLD-TDAC-EMP-CD OF           
048028         HOLD-TDACUST.
048030     MOVE TDAC-FREE-MARK OF TDACUST TO HOLD-TDAC-FREE-MARK OF     
048032         HOLD-TDACUST.
048034     MOVE TDAC-INQ-SECR-CD OF TDACUST TO HOLD-TDAC-INQ-SECR-CD OF 
048036         HOLD-TDACUST.
048038     MOVE TDAC-PRIVACY OF TDACUST TO HOLD-TDAC-PRIVACY OF         
048040         HOLD-TDACUST.
048042     MOVE TDAC-BK-DEF-CD1 OF TDACUST TO HOLD-TDAC-BK-DEF-CD1 OF   
048044         HOLD-TDACUST.
048046     MOVE TDAC-BK-DEF-CD2 OF TDACUST TO HOLD-TDAC-BK-DEF-CD2 OF   
048048         HOLD-TDACUST.
048050     MOVE TDAC-BK-DEF-CD3 OF TDACUST TO HOLD-TDAC-BK-DEF-CD3 OF   
048052         HOLD-TDACUST.
048054     MOVE TDAC-BK-DEF-CD4 OF TDACUST TO HOLD-TDAC-BK-DEF-CD4 OF   
048056         HOLD-TDACUST.
048058     MOVE TDAC-BK-DEF-CD5 OF TDACUST TO HOLD-TDAC-BK-DEF-CD5 OF   
048060         HOLD-TDACUST.
048062     MOVE TDAC-EMPLOYEE-ID OF TDACUST TO HOLD-TDAC-EMPLOYEE-ID OF 
048064         HOLD-TDACUST.
048066     MOVE TDAC-EMAIL-ADDR OF TDACUST TO HOLD-TDAC-EMAIL-ADDR OF   
048068         HOLD-TDACUST.
048070     MOVE TDAC-EMAIL-PSSWRD OF TDACUST TO HOLD-TDAC-EMAIL-PSSWRD  
048072         OF HOLD-TDACUST.
048074     MOVE TDAC-GENDER OF TDACUST TO HOLD-TDAC-GENDER OF           
048076         HOLD-TDACUST.
048078     MOVE TDAC-NEW-CUST OF TDACUST TO HOLD-TDAC-NEW-CUST OF       
048080         HOLD-TDACUST.
048082     MOVE TDAC-OPEN-DT OF TDACUST TO HOLD-TDAC-OPEN-DT OF         
048084         HOLD-TDACUST.
048086     MOVE TDAC-LUPD-DATE OF TDACUST TO HOLD-TDAC-LUPD-DATE OF     
048088         HOLD-TDACUST.
048090     MOVE TDAC-LUPD-TIME OF TDACUST TO HOLD-TDAC-LUPD-TIME OF     
048092         HOLD-TDACUST.
048094     MOVE TDAC-LST-CONTACT OF TDACUST TO HOLD-TDAC-LST-CONTACT OF 
048096         HOLD-TDACUST.
048098     MOVE TDAC-BIRTH-DT OF TDACUST TO HOLD-TDAC-BIRTH-DT OF       
048100         HOLD-TDACUST.
048102     MOVE TDAC-BIRTH-DT-2 OF TDACUST TO HOLD-TDAC-BIRTH-DT-2 OF   
048104         HOLD-TDACUST.
048106     MOVE TDAC-BIRTH-DT-3 OF TDACUST TO HOLD-TDAC-BIRTH-DT-3 OF   
048108         HOLD-TDACUST.
048110     MOVE TDAC-DEATH-DT OF TDACUST TO HOLD-TDAC-DEATH-DT OF       
048112         HOLD-TDACUST.
048114     MOVE TDAC-ADD-DT OF TDACUST TO HOLD-TDAC-ADD-DT OF           
048116         HOLD-TDACUST.
048118     MOVE TDAC-ADD-TM OF TDACUST TO HOLD-TDAC-ADD-TM OF           
048120         HOLD-TDACUST.
048122     MOVE TDAC-ROTH-DATE OF TDACUST TO HOLD-TDAC-ROTH-DATE OF     
048124         HOLD-TDACUST.
048126     MOVE TDAC-CD-BAL OF TDACUST TO HOLD-TDAC-CD-BAL OF           
048128         HOLD-TDACUST.
048130     MOVE TDAC-CD-BAL-BYR OF TDACUST TO HOLD-TDAC-CD-BAL-BYR OF   
048132         HOLD-TDACUST.
048134     MOVE TDAC-CD-PENLTY OF TDACUST TO HOLD-TDAC-CD-PENLTY OF     
048136         HOLD-TDACUST.
048138     MOVE TDAC-CD-WTHLD OF TDACUST TO HOLD-TDAC-CD-WTHLD OF       
048140         HOLD-TDACUST.
048142     MOVE TDAC-CD-INT OF TDACUST TO HOLD-TDAC-CD-INT OF           
048144         HOLD-TDACUST.
048146     MOVE TDAC-CD-OID-INT OF TDACUST TO HOLD-TDAC-CD-OID-INT OF   
048148         HOLD-TDACUST.
048150     MOVE TDAC-IRA-BAL OF TDACUST TO HOLD-TDAC-IRA-BAL OF         
048152         HOLD-TDACUST.
048154     MOVE TDAC-IRA-BAL-BYR OF TDACUST TO HOLD-TDAC-IRA-BAL-BYR OF 
048156         HOLD-TDACUST.
048158     MOVE TDAC-IRA-PENLTY OF TDACUST TO HOLD-TDAC-IRA-PENLTY OF   
048160         HOLD-TDACUST.
048162     MOVE TDAC-IRA-WTHLD OF TDACUST TO HOLD-TDAC-IRA-WTHLD OF     
048164         HOLD-TDACUST.
048166     MOVE TDAC-IRA-INT OF TDACUST TO HOLD-TDAC-IRA-INT OF         
048168         HOLD-TDACUST.
048170     MOVE TDAC-IRA-CONTR OF TDACUST TO HOLD-TDAC-IRA-CONTR OF     
048172         HOLD-TDACUST.
048174     MOVE TDAC-IRA-CONTR-LY OF TDACUST TO HOLD-TDAC-IRA-CONTR-LY  
048176         OF HOLD-TDACUST.
048178     MOVE TDAC-IRA-DISTR OF TDACUST TO HOLD-TDAC-IRA-DISTR OF     
048180         HOLD-TDACUST.
048182     MOVE TDAC-IRA-DISTR-LY OF TDACUST TO HOLD-TDAC-IRA-DISTR-LY  
048184         OF HOLD-TDACUST.
048186     MOVE TDAC-IRA-ROLLOVER OF TDACUST TO HOLD-TDAC-IRA-ROLLOVER  
048188         OF HOLD-TDACUST.
048190     MOVE TDAC-IRA-TRF-IN OF TDACUST TO HOLD-TDAC-IRA-TRF-IN OF   
048192         HOLD-TDACUST.
048194     MOVE TDAC-IRA-TRF-OUT OF TDACUST TO HOLD-TDAC-IRA-TRF-OUT OF 
048196         HOLD-TDACUST.
048198     MOVE TDAC-IRA-FAIR-MKT OF TDACUST TO HOLD-TDAC-IRA-FAIR-MKT  
048200         OF HOLD-TDACUST.
048202     MOVE TDAC-CIF-REMARK OF TDACUST TO HOLD-TDAC-CIF-REMARK OF   
048204         HOLD-TDACUST.
048206     MOVE TDAC-CD-ST-WHLD OF TDACUST TO HOLD-TDAC-CD-ST-WHLD OF   
048208         HOLD-TDACUST.
048210     MOVE TDAC-IRA-ST-WHLD OF TDACUST TO HOLD-TDAC-IRA-ST-WHLD OF 
048212         HOLD-TDACUST.
048214     MOVE 1 TO Z-II.
048216 Z-32-1-1-LOOP.
048218     IF Z-II > 12
048220         GO TO Z-32-1-1-LOOP-XIT.
048222     MOVE TDAC-CURR-YR-AMT OF TDACUST (Z-II) TO                   
048224         HOLD-TDAC-CURR-YR-AMT OF HOLD-TDACUST (Z-II).
048226     MOVE TDAC-LAST-YR-AMT OF TDACUST (Z-II) TO                   
048228         HOLD-TDAC-LAST-YR-AMT OF HOLD-TDACUST (Z-II).
048230     ADD 1 TO Z-II.
048232     GO TO Z-32-1-1-LOOP.
048234 Z-32-1-1-LOOP-XIT.
048236     MOVE TDAC-TIN-CD-2 OF TDACUST TO HOLD-TDAC-TIN-CD-2 OF       
048238         HOLD-TDACUST.
048240     MOVE TDAC-TIN-CRT-CD-2 OF TDACUST TO HOLD-TDAC-TIN-CRT-CD-2  
048242         OF HOLD-TDACUST.
048244     MOVE TDAC-TIN-CRT-DT-2 OF TDACUST TO HOLD-TDAC-TIN-CRT-DT-2  
048246         OF HOLD-TDACUST.
048248     MOVE TDAC-TIN-NBR-2 OF TDACUST TO HOLD-TDAC-TIN-NBR-2 OF     
048250         HOLD-TDACUST.
048252     MOVE TDAC-TIN-CD-3 OF TDACUST TO HOLD-TDAC-TIN-CD-3 OF       
048254         HOLD-TDACUST.
048256     MOVE TDAC-TIN-CRT-CD-3 OF TDACUST TO HOLD-TDAC-TIN-CRT-CD-3  
048258         OF HOLD-TDACUST.
048260     MOVE TDAC-TIN-CRT-DT-3 OF TDACUST TO HOLD-TDAC-TIN-CRT-DT-3  
048262         OF HOLD-TDACUST.
048264     MOVE TDAC-TIN-NBR-3 OF TDACUST TO HOLD-TDAC-TIN-NBR-3 OF     
048266         HOLD-TDACUST.
048268     MOVE TDAC-NAICS-CD OF TDACUST TO HOLD-TDAC-NAICS-CD OF       
048270         HOLD-TDACUST.
048272     MOVE TDAC-CIF-PASS-THR OF TDACUST TO HOLD-TDAC-CIF-PASS-THR  
048274         OF HOLD-TDACUST.
048276     MOVE TDAC-EMAIL-NTC OF TDACUST TO HOLD-TDAC-EMAIL-NTC OF     
048278         HOLD-TDACUST.
048280     MOVE TDAC-RMD-YR-AMT OF TDACUST TO HOLD-TDAC-RMD-YR-AMT OF   
048282         HOLD-TDACUST.
048284     MOVE TDAC-ADDR-CHG-DT OF TDACUST TO HOLD-TDAC-ADDR-CHG-DT OF 
048286         HOLD-TDACUST.
048288     MOVE TDAC-WTHLD-CD OF TDACUST TO HOLD-TDAC-WTHLD-CD OF       
048290         HOLD-TDACUST.
048292     MOVE TDAC-ST-WHLD-CD OF TDACUST TO HOLD-TDAC-ST-WHLD-CD OF   
048294         HOLD-TDACUST.
048296     MOVE TDAC-WTHLD-AMT OF TDACUST TO HOLD-TDAC-WTHLD-AMT OF     
048298         HOLD-TDACUST.
048300     MOVE TDAC-ST-WHLD-AMT OF TDACUST TO HOLD-TDAC-ST-WHLD-AMT OF 
048302         HOLD-TDACUST.
048304     MOVE TDAC-FOREIGN-LANG OF TDACUST TO HOLD-TDAC-FOREIGN-LANG  
048306         OF HOLD-TDACUST.
048308     MOVE TDAC-L-ROLLOVR-DT OF TDACUST TO HOLD-TDAC-L-ROLLOVR-DT  
048310         OF HOLD-TDACUST.
048312     MOVE TDAC-CUSTM-FIELDS OF TDACUST TO HOLD-TDAC-CUSTM-FIELDS  
048314         OF HOLD-TDACUST.
048316     MOVE TDAC-LLC-NAME OF TDACUST TO HOLD-TDAC-LLC-NAME OF       
048318         HOLD-TDACUST.
048320     MOVE TDAC-LLC-TIN-CD OF TDACUST TO HOLD-TDAC-LLC-TIN-CD OF   
048322         HOLD-TDACUST.
048324     MOVE TDAC-LLC-TIN OF TDACUST TO HOLD-TDAC-LLC-TIN OF         
048326         HOLD-TDACUST.
048328     MOVE TDAC-FOREIGN-PHN OF TDACUST TO HOLD-TDAC-FOREIGN-PHN OF 
048330         HOLD-TDACUST.
048332     MOVE TDB-READ-DATE TO HOLD-READ-DATE.
048334     MOVE 04 TO TDB-STRUCT-NBR.
048336     MOVE SPACES TO TDB-DATA-AREA.
048338     MOVE ZERO TO Z-FLINFO14-PRES.
048340     MOVE 15 TO Z-FLINFO14-LAST-SEQ.
048342     MOVE ZERO TO Z-FLINFO14-SOME.
048344     SET TDAACTVBKSET OF TDAACTV OF LDBTDADB TO ENDING
048346         ON EXCEPTION
048348         MOVE "TDAACTVBKSET OF TDAACTV OF LDBTDADB" TO            
048350             Z-DMS-EXCEPT-STR
048352         MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
048354         MOVE 15 TO Z-DMS-EXCEPT-SEQ
048356         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT
048358         GO TO Z-32-5-XIT.
048360 Z-32-5-READ.
048362     FIND TDAACTV OF LDBTDADB VIA PRIOR TDAACTVBKSET OF TDAACTV   
048364         OF LDBTDADB
048366     AT TDA-ACTV-BANK = HOLD-TDAC-BANK AND
048368        TDA-ACTV-CUST = HOLD-TDAC-CUST AND
048370        TDA-ACTV-ACCT = 0
048372         ON EXCEPTION
048374         MOVE 15 TO Z-DMS-EXCEPT-SEQ
048376         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
048378             GO TO Z-32-5-XIT
048380         ELSE
048382             MOVE "TDAACTVBKSET OF TDAACTV OF LDBTDADB" TO        
048384                 Z-DMS-EXCEPT-STR
048386             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
048388             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
048390
048392 Z-32-5-PRESENT.
048394*
048396     MOVE 1 TO Z-FLINFO14-SOME.
048398     MOVE 1 TO Z-FLINFO14-PRES.
048400     GO TO Z-32-5-CONT.
048402 Z-32-5-XIT.
048404 Z-32-5-CONT.
048406     IF TDA-ACTV-DATE < TDB-READ-DATE
048408         NEXT SENTENCE ELSE
048410         GO TO Z-32-6-1-ELSE.
048412     MOVE "C" TO WS-ADJUSTED-IND.
048414 Z-32-6-1-ELSE.
048416 Z-32-8-LOOP.
048418     IF Z-FLINFO14-ABSENT OR TDA-ACTV-DATE < TDB-READ-DATE OR     
048420         TDAACTV (TDA-ACTV-TYPE ) = 6
048422         GO TO Z-32-8-XIT.
048424     MOVE 0 TO Z-EXIT-CODE.
048426     MOVE 9999 TO Z-EXIT-LEVEL.
048428     MOVE TDA-ACTV-BANK OF TDAACTV TO HOLD-TDA-ACTV-BANK OF       
048430         HOLD-TDAACTV.
048432     MOVE TDA-ACTV-BRCH OF TDAACTV TO HOLD-TDA-ACTV-BRCH OF       
048434         HOLD-TDAACTV.
048436     MOVE TDA-ACTV-APPL OF TDAACTV TO HOLD-TDA-ACTV-APPL OF       
048438         HOLD-TDAACTV.
048440     MOVE TDA-ACTV-CUST OF TDAACTV TO HOLD-TDA-ACTV-CUST OF       
048442         HOLD-TDAACTV.
048444     MOVE TDA-ACTV-ACCT OF TDAACTV TO HOLD-TDA-ACTV-ACCT OF       
048446         HOLD-TDAACTV.
048448     MOVE TDA-ACTV-TOT-CD OF TDAACTV TO HOLD-TDA-ACTV-TOT-CD OF   
048450         HOLD-TDAACTV.
048452     MOVE TDA-ACTV-IGL-GRP OF TDAACTV TO HOLD-TDA-ACTV-IGL-GRP OF 
048454         HOLD-TDAACTV.
048456     MOVE TDA-ACTV-OFFICER OF TDAACTV TO HOLD-TDA-ACTV-OFFICER OF 
048458         HOLD-TDAACTV.
048460     MOVE TDA-ACTV-NC-INDC OF TDAACTV TO HOLD-TDA-ACTV-NC-INDC OF 
048462         HOLD-TDAACTV.
048464     MOVE TDA-ACTV-PROC-FG OF TDAACTV TO HOLD-TDA-ACTV-PROC-FG OF 
048466         HOLD-TDAACTV.
048468     MOVE TDA-ACTV-EFF-DT OF TDAACTV TO HOLD-TDA-ACTV-EFF-DT OF   
048470         HOLD-TDAACTV.
048472     MOVE TDA-ACTV-DATE OF TDAACTV TO HOLD-TDA-ACTV-DATE OF       
048474         HOLD-TDAACTV.
048476     MOVE TDA-ACTV-MAINT OF TDAACTV TO HOLD-TDA-ACTV-MAINT OF     
048478         HOLD-TDAACTV.
048480     MOVE TDA-ACTV-TIME OF TDAACTV TO HOLD-TDA-ACTV-TIME OF       
048482         HOLD-TDAACTV.
048484     MOVE TDA-ACTV-SEQ-NBR OF TDAACTV TO HOLD-TDA-ACTV-SEQ-NBR OF 
048486         HOLD-TDAACTV.
048488     MOVE TDA-ACTV-SERIAL OF TDAACTV TO HOLD-TDA-ACTV-SERIAL OF   
048490         HOLD-TDAACTV.
048492     MOVE TDA-ACTV-SOURCE OF TDAACTV TO HOLD-TDA-ACTV-SOURCE OF   
048494         HOLD-TDAACTV.
048496     MOVE TDA-ACTV-ERASED OF TDAACTV TO HOLD-TDA-ACTV-ERASED OF   
048498         HOLD-TDAACTV.
048500     MOVE TDA-ACTV-DR-CR OF TDAACTV TO HOLD-TDA-ACTV-DR-CR OF     
048502         HOLD-TDAACTV.
048504     MOVE TDA-ACTV-E-PUBID OF TDAACTV TO HOLD-TDA-ACTV-E-PUBID OF 
048506         HOLD-TDAACTV.
048508     MOVE TDA-ACTV-PUB-ID OF TDAACTV TO HOLD-TDA-ACTV-PUB-ID OF   
048510         HOLD-TDAACTV.
048512     MOVE TDA-ACTV-SUB OF TDAACTV TO HOLD-TDA-ACTV-SUB OF         
048514         HOLD-TDAACTV.
048516     IF TDAACTV (TDA-ACTV-TYPE ) = 2
048518         NEXT SENTENCE ELSE
048520         GO TO Z-32-10-1-ELSE.
048522     MOVE "A" TO WS-ADJUSTED-IND.
048524     MOVE TDA-ACTVC-CODE TO HOLD-TDA-ACTVC-CODE.
048526     MOVE TDA-ACTVC-EXCPT TO HOLD-TDA-ACTVC-EXCPT.
048528     MOVE TDA-ACTVC-CHG-FRM TO HOLD-TDA-ACTVC-CHG-FRM.
048530     MOVE TDA-ACTVC-CHG-TO TO HOLD-TDA-ACTVC-CHG-TO.
048532     MOVE TDA-ACTVC-NCREOPN TO HOLD-TDA-ACTVC-NCREOPN.
048534************ PERFORM TDB-ACTV-ADJUSTMENT
048536     PERFORM Z-35-PROCEDURE THRU Z-35-XIT.
048538     IF  Z-EXIT-EDITEXIT
048540         GO TO Z-32-XIT.
048542     IF  Z-DMS2-ABORT-FLAG = 1
048544         GO TO Z-32-XIT.
048546     IF  Z-EXIT-LEVEL < 0
048548         GO TO Z-32-8-END.
048550*
048552 Z-32-10-1-ELSE.
048554     MOVE ZERO TO Z-FLINFO14-PRES.
048556     MOVE 16 TO Z-FLINFO14-LAST-SEQ.
048558     MOVE ZERO TO Z-FLINFO14-SOME.
048560 Z-32-18-READ.
048562     FIND TDAACTV OF LDBTDADB VIA PRIOR TDAACTVBKSET OF TDAACTV   
048564         OF LDBTDADB
048566     AT TDA-ACTV-BANK = HOLD-TDAC-BANK AND
048568        TDA-ACTV-CUST = HOLD-TDAC-CUST AND
048570        TDA-ACTV-ACCT = 0
048572         ON EXCEPTION
048574         MOVE 16 TO Z-DMS-EXCEPT-SEQ
048576         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
048578             GO TO Z-32-18-XIT
048580         ELSE
048582             MOVE "TDAACTVBKSET OF TDAACTV OF LDBTDADB" TO        
048584                 Z-DMS-EXCEPT-STR
048586             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
048588             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
048590
048592 Z-32-18-PRESENT.
048594*
048596     MOVE 1 TO Z-FLINFO14-SOME.
048598     MOVE 1 TO Z-FLINFO14-PRES.
048600     GO TO Z-32-18-CONT.
048602 Z-32-18-XIT.
048604 Z-32-18-CONT.
048606 Z-32-8-END.
048608     IF Z-EDIT-ERROR
048610         GO TO Z-32-XIT.
048612 Z-32-8-SKIP.
048614     IF Z-EXIT-LEVEL < 1
048616         GO TO Z-32-END.
048618     IF Z-EXIT-CODE > 0
048620         GO TO Z-32-8-XIT.
048622     GO TO Z-32-8-LOOP.
048624*
048626 Z-32-8-XIT.
048628     MOVE 0 TO Z-EXIT-CODE.
048630     MOVE 9999 TO Z-EXIT-LEVEL.
048632     IF TDAACTV (TDA-ACTV-TYPE ) = 6
048634         NEXT SENTENCE ELSE
048636         GO TO Z-32-19-1-ELSE.
048638     MOVE "N" TO WS-ADJUSTED-IND.
048640 Z-32-19-1-ELSE.
048642 Z-32-END.
048644     IF Z-EDIT-ERROR
048646         GO TO Z-32-XIT.
048648 Z-32-SKIP.
048650     IF Z-EXIT-LEVEL NOT < 0
048652         MOVE 0 TO Z-EXIT-CODE
048654         MOVE 9999 TO Z-EXIT-LEVEL.
048656 Z-32-XIT.
048658     EXIT.
048660*
048662*****************************************************************
048664*    PROCEDURE TDB-IRA-01BAT4-ACTV-ADJ
048666*****************************************************************
048668 Z-33-PROCEDURE.
048670*
048672     MOVE TDAI-BANK OF TDAIRA TO HOLD-TDAI-BANK OF HOLD-TDAIRA.
048674     MOVE TDAI-BRCH OF TDAIRA TO HOLD-TDAI-BRCH OF HOLD-TDAIRA.
048676     MOVE TDAI-CUST OF TDAIRA TO HOLD-TDAI-CUST OF HOLD-TDAIRA.
048678     MOVE TDAI-ACCT OF TDAIRA TO HOLD-TDAI-ACCT OF HOLD-TDAIRA.
048680     MOVE TDAI-PUB-ID OF TDAIRA TO HOLD-TDAI-PUB-ID OF            
048682         HOLD-TDAIRA.
048684     MOVE TDAI-ADD-DT OF TDAIRA TO HOLD-TDAI-ADD-DT OF            
048686         HOLD-TDAIRA.
048688     MOVE TDAI-ADD-TM OF TDAIRA TO HOLD-TDAI-ADD-TM OF            
048690         HOLD-TDAIRA.
048692     MOVE 1 TO Z-II.
048694 Z-33-1-1-LOOP.
048696     IF Z-II > 20
048698         GO TO Z-33-1-1-LOOP-XIT.
048700     MOVE TDAI-DS-TYPE OF TDAIRA (Z-II) TO HOLD-TDAI-DS-TYPE OF   
048702         HOLD-TDAIRA (Z-II).
048704     MOVE TDAI-CN-TYPE OF TDAIRA (Z-II) TO HOLD-TDAI-CN-TYPE OF   
048706         HOLD-TDAIRA (Z-II).
048708     MOVE TDAI-DS-CN-AMT OF TDAIRA (Z-II) TO HOLD-TDAI-DS-CN-AMT  
048710         OF HOLD-TDAIRA (Z-II).
048712     MOVE TDAI-DS-PEN-AMT OF TDAIRA (Z-II) TO                     
048714         HOLD-TDAI-DS-PEN-AMT OF HOLD-TDAIRA (Z-II).
048716     MOVE TDAI-DS-WTHLD-AMT OF TDAIRA (Z-II) TO                   
048718         HOLD-TDAI-DS-WTHLD-AMT OF HOLD-TDAIRA (Z-II).
048720     MOVE TDAI-DS-ST-WH-AMT OF TDAIRA (Z-II) TO                   
048722         HOLD-TDAI-DS-ST-WH-AMT OF HOLD-TDAIRA (Z-II).
048724     MOVE TDAI-DS-EXC-EARN OF TDAIRA (Z-II) TO                    
048726         HOLD-TDAI-DS-EXC-EARN OF HOLD-TDAIRA (Z-II).
048728     ADD 1 TO Z-II.
048730     GO TO Z-33-1-1-LOOP.
048732 Z-33-1-1-LOOP-XIT.
048734     MOVE TDAI-DS-C-YTD-CNT OF TDAIRA TO HOLD-TDAI-DS-C-YTD-CNT   
048736         OF HOLD-TDAIRA.
048738     MOVE TDAI-DS-P-YTD-CNT OF TDAIRA TO HOLD-TDAI-DS-P-YTD-CNT   
048740         OF HOLD-TDAIRA.
048742     MOVE TDAI-DS-AMT-C-YTD OF TDAIRA TO HOLD-TDAI-DS-AMT-C-YTD   
048744         OF HOLD-TDAIRA.
048746     MOVE TDAI-DS-AMT-P-YTD OF TDAIRA TO HOLD-TDAI-DS-AMT-P-YTD   
048748         OF HOLD-TDAIRA.
048750     MOVE TDAI-DS-INT-AMT OF TDAIRA TO HOLD-TDAI-DS-INT-AMT OF    
048752         HOLD-TDAIRA.
048754     MOVE TDAI-CN-YTD-CNT OF TDAIRA TO HOLD-TDAI-CN-YTD-CNT OF    
048756         HOLD-TDAIRA.
048758     MOVE TDAI-CN-YTD-AMT OF TDAIRA TO HOLD-TDAI-CN-YTD-AMT OF    
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 482 lines from 23894 to 24375.

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

