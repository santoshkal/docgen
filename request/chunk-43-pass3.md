# LLM Request Debug File
Generated: 2025-11-13T21:37:54.902324

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 43/55
- **Model**: gpt-4.1
- **Chunk Number**: 43
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~9,466 tokens
- **Total Input**: ~11,424 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 43/55" (ID: detailed-code-explanation)

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


**CHUNK 43 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 43 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 20667 to 21245 (579 lines)\nChunk Tokens (estimated): ~7,725\nActual Input Tokens: 9,131 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 20667-21245 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 43 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 43 of 55.\n\n\n=============================================================================\nCHUNK 43 SOURCE CODE (Lines 20667-21245)\n=============================================================================\n\n```cobol\n041342 Z-5-254-1-ELSE.\n041344     IF WS-INHERIT-IRA-ON-TIN = 1\n041346         NEXT SENTENCE ELSE\n041348         GO TO Z-5-263-1-ELSE.\n041350     MOVE WS-PREV-TIN TO WS-RMDRPT2-TIN.\n041352     MOVE \"-\" TO WS-RMDRPT2-TIN-LDASH\n041354       , WS-RMDRPT2-TIN-RDASH.\n041356     MOVE WS-RMDRPT2-TIN TO RMDRPT-TOT-TIN-10.\n041358     IF NOT Z-SW3\n041360         NEXT SENTENCE ELSE\n041362         GO TO Z-5-267-1-ELSE.\n041364     COMPUTE Z-LINES-HOLD = 1.\n041366     COMPUTE Z-LINES = 1.\n041368     IF Z-RPT-2-TRAP > ZERO\n041370         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.\n041372     IF Z-LINES > Z-RPT-2-TRAP\n041374       IF Z-RPTINFO2-INBLOCK = ZERO\n041376         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1\n041378         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT\n041380         COMPUTE Z-LINES = 1.\n041382     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).\n041384     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).\n041386     MOVE RMDRPT-REC-10 TO Z-RPT-2-BUFFER.\n041388     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.\n041390     COMPUTE Z-LINES-HOLD = 1.\n041392     COMPUTE Z-LINES = 1.\n041394     IF Z-RPT-2-TRAP > ZERO\n041396         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.\n041398     IF Z-LINES > Z-RPT-2-TRAP\n041400       IF Z-RPTINFO2-INBLOCK = ZERO\n041402         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1\n041404         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT\n041406         COMPUTE Z-LINES = 1.\n041408     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).\n041410     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).\n041412     MOVE SPACES TO Z-RPT-2-BUFFER.\n041414     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.\n041416 Z-5-267-1-ELSE.\n041418 Z-5-263-1-ELSE.\n041420     MOVE ZEROS TO WS-TIN-TOTALS\n041422       , WS-INHERIT-IRA-ON-TIN\n041424       , WS-NON-INHERIT-IRA-ON-TIN.\n041426     MOVE RMD-COUNT TO RMDRPT-CNT-5.\n041428     COMPUTE Z-LINES-HOLD = 2.\n041430     COMPUTE Z-LINES = 2.\n041432     IF Z-RPT-1-TRAP > ZERO\n041434         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n041436     IF Z-LINES > Z-RPT-1-TRAP\n041438       IF Z-RPTINFO1-INBLOCK = ZERO\n041440         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n041442         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n041444         COMPUTE Z-LINES = 2.\n041446     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n041448     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n041450     MOVE RMDRPT-REC-5 TO Z-RPT-1-BUFFER.\n041452     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n041454     MOVE RMD-TOT-CHGD TO RMDRPT-TOT-FM-7.\n041456     IF SPECS-RMD-OVERRIDE = \"Y\"\n041458         NEXT SENTENCE ELSE\n041460         GO TO Z-5-274-1-ELSE.\n041462     COMPUTE Z-LINES-HOLD = 1.\n041464     COMPUTE Z-LINES = 1.\n041466     IF Z-RPT-1-TRAP > ZERO\n041468         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n041470     IF Z-LINES > Z-RPT-1-TRAP\n041472       IF Z-RPTINFO1-INBLOCK = ZERO\n041474         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n041476         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n041478         COMPUTE Z-LINES = 1.\n041480     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n041482     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n041484     MOVE RMDRPT-REC-7 TO Z-RPT-1-BUFFER.\n041486     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n041488 Z-5-274-1-ELSE.\n041490     IF WS-MDRPT2-OPEN = 1\n041492         NEXT SENTENCE ELSE\n041494         GO TO Z-5-276-1-ELSE.\n041496     MOVE RMD-COUNT-INHERIT TO RMDRPT-CNT-5.\n041498     COMPUTE Z-LINES-HOLD = 2.\n041500     COMPUTE Z-LINES = 2.\n041502     IF Z-RPT-2-TRAP > ZERO\n041504         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.\n041506     IF Z-LINES > Z-RPT-2-TRAP\n041508       IF Z-RPTINFO2-INBLOCK = ZERO\n041510         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1\n041512         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT\n041514         COMPUTE Z-LINES = 2.\n041516     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).\n041518     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).\n041520     MOVE RMDRPT-REC-5 TO Z-RPT-2-BUFFER.\n041522     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.\n041524     IF SPECS-RMD-OVERRIDE = \"Y\"\n041526         NEXT SENTENCE ELSE\n041528         GO TO Z-5-279-1-ELSE.\n041530     MOVE RMD-TOT-CHGD-INHERIT TO RMDRPT-TOT-FM-7.\n041532     COMPUTE Z-LINES-HOLD = 1.\n041534     COMPUTE Z-LINES = 1.\n041536     IF Z-RPT-2-TRAP > ZERO\n041538         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.\n041540     IF Z-LINES > Z-RPT-2-TRAP\n041542       IF Z-RPTINFO2-INBLOCK = ZERO\n041544         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1\n041546         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT\n041548         COMPUTE Z-LINES = 1.\n041550     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).\n041552     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).\n041554     MOVE RMDRPT-REC-7 TO Z-RPT-2-BUFFER.\n041556     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.\n041558 Z-5-279-1-ELSE.\n041560 Z-5-276-1-ELSE.\n041562 Z-5-229-1-ELSE.\n041564 Z-5-END.\n041566     IF Z-EDIT-ERROR\n041568         GO TO Z-5-XIT.\n041570 Z-5-SKIP.\n041572     IF Z-EXIT-LEVEL NOT < 0\n041574         MOVE 0 TO Z-EXIT-CODE\n041576         MOVE 9999 TO Z-EXIT-LEVEL.\n041578 Z-5-XIT.\n041580     EXIT.\n041582*\n041584*****************************************************************\n041586*    PROCEDURE TPR-TEAR-PAGES\n041588*****************************************************************\n041590 Z-21-PROCEDURE.\n041592*\n041594     MOVE 0 TO Z-EXIT-CODE.\n041596     MOVE 9999 TO Z-EXIT-LEVEL.\n041598     MOVE ZEROS TO PAGE-CTR.\n041600     MOVE SPACES TO PRINT-LINE.\n041602     IF GWS-TP-CTL = 1\n041604         NEXT SENTENCE ELSE\n041606         GO TO Z-21-3-1-ELSE.\n041608     MOVE HEADER-LINE1 TO PRINT-LINE.\n041610     GO TO Z-21-3-ENDIF.\n041612 Z-21-3-1-ELSE.\n041614     MOVE SPACES TO PRINT-LINE.\n041616 Z-21-3-ENDIF.\n041618     IF RPT601-BANNER-HEADER = 0\n041620         NEXT SENTENCE ELSE\n041622         GO TO Z-21-6-1-ELSE.\n041624     MOVE 1 TO PAGE-ADVANCE.\n041626************ PERFORM TPR-WRITE-TEAR\n041628     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.\n041630     IF  Z-EXIT-EDITEXIT\n041632         GO TO Z-21-XIT.\n041634     IF  Z-DMS2-ABORT-FLAG = 1\n041636         GO TO Z-21-XIT.\n041638     IF  Z-EXIT-LEVEL < 0\n041640         GO TO Z-21-END.\n041642*\n041644     GO TO Z-21-6-ENDIF.\n041646 Z-21-6-1-ELSE.\n041648     MOVE 0 TO RPT601-BANNER-HEADER.\n041650 Z-21-6-ENDIF.\n041652     MOVE 0 TO PAGE-ADVANCE.\n041654     MOVE ALL \"*\" TO PRINT-LINE.\n041656************ PERFORM TPR-WRITE-TEAR\n041658     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.\n041660     IF  Z-EXIT-EDITEXIT\n041662         GO TO Z-21-XIT.\n041664     IF  Z-DMS2-ABORT-FLAG = 1\n041666         GO TO Z-21-XIT.\n041668     IF  Z-EXIT-LEVEL < 0\n041670         GO TO Z-21-END.\n041672*\n041674************ PERFORM TPR-WRITE-TEAR\n041676     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.\n041678     IF  Z-EXIT-EDITEXIT\n041680         GO TO Z-21-XIT.\n041682     IF  Z-DMS2-ABORT-FLAG = 1\n041684         GO TO Z-21-XIT.\n041686     IF  Z-EXIT-LEVEL < 0\n041688         GO TO Z-21-END.\n041690*\n041692     MOVE SPACES TO PRINT-LINE.\n041694************ PERFORM TPR-WRITE-TEAR\n041696     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.\n041698     IF  Z-EXIT-EDITEXIT\n041700         GO TO Z-21-XIT.\n041702     IF  Z-DMS2-ABORT-FLAG = 1\n041704         GO TO Z-21-XIT.\n041706     IF  Z-EXIT-LEVEL < 0\n041708         GO TO Z-21-END.\n041710*\n041712     MOVE 0 TO TP-LN-POS.\n041714     MOVE 1 TO TP-LN-CT\n041716       , TP-LN-DPTH.\n041718 Z-21-18-LOOP.\n041720     IF TP-LN-CT = 4\n041722         GO TO Z-21-18-XIT.\n041724     MOVE 0 TO Z-EXIT-CODE.\n041726     MOVE 9999 TO Z-EXIT-LEVEL.\n041728     ADD 1 TO TP-LN-POS .\n041730     IF TP-LN-POS = 9\n041732         NEXT SENTENCE ELSE\n041734         GO TO Z-21-20-1-ELSE.\n041736     MOVE 1 TO TP-LN-POS.\n041738************ PERFORM TPR-PRINT-TEAR\n041740     PERFORM Z-30-PROCEDURE THRU Z-30-XIT.\n041742     IF  Z-EXIT-EDITEXIT\n041744         GO TO Z-21-XIT.\n041746     IF  Z-DMS2-ABORT-FLAG = 1\n041748         GO TO Z-21-XIT.\n041750     IF  Z-EXIT-LEVEL < 0\n041752         GO TO Z-21-18-END.\n041754*\n041756     GO TO Z-21-20-ENDIF.\n041758 Z-21-20-1-ELSE.\n041760     MOVE 1 TO TP-AR.\n041762     MOVE TP-DECODE (TP-AR) TO TP-DECODE-WKA (TP-LN-POS).\n041764 Z-21-25-LOOP.\n041766     IF ( TP-SUBSCRIPT (TP-LN-POS) = TP-IN-CHAR (TP-LN-POS) ) OR  \n041768         ( TP-SUBSCRIPT (TP-LN-POS) = SPACES )\n041770         GO TO Z-21-25-XIT.\n041772     ADD 1 TO TP-AR .\n041774     MOVE TP-DECODE (TP-AR) TO TP-DECODE-WKA (TP-LN-POS).\n041776     IF Z-EDIT-ERROR\n041778         GO TO Z-21-XIT.\n041780 Z-21-25-SKIP.\n041782     GO TO Z-21-25-LOOP.\n041784*\n041786 Z-21-25-XIT.\n041788 Z-21-20-ENDIF.\n041790 Z-21-18-END.\n041792     IF Z-EDIT-ERROR\n041794         GO TO Z-21-XIT.\n041796 Z-21-18-SKIP.\n041798     IF Z-EXIT-LEVEL < 1\n041800         GO TO Z-21-END.\n041802     IF Z-EXIT-CODE > 0\n041804         GO TO Z-21-18-XIT.\n041806     GO TO Z-21-18-LOOP.\n041808*\n041810 Z-21-18-XIT.\n041812     MOVE 0 TO Z-EXIT-CODE.\n041814     MOVE 9999 TO Z-EXIT-LEVEL.\n041816 Z-21-END.\n041818     IF Z-EDIT-ERROR\n041820         GO TO Z-21-XIT.\n041822 Z-21-SKIP.\n041824     IF Z-EXIT-LEVEL NOT < 0\n041826         MOVE 0 TO Z-EXIT-CODE\n041828         MOVE 9999 TO Z-EXIT-LEVEL.\n041830 Z-21-XIT.\n041832     EXIT.\n041834*\n041836*****************************************************************\n041838*    PROCEDURE TPR-PRINT-TEAR\n041840*****************************************************************\n041842 Z-30-PROCEDURE.\n041844*\n041846     MOVE 0 TO Z-EXIT-CODE.\n041848     MOVE 9999 TO Z-EXIT-LEVEL.\n041850 Z-30-1-LOOP.\n041852     IF TP-LN-DPTH = 6\n041854         GO TO Z-30-1-XIT.\n041856     MOVE 0 TO Z-EXIT-CODE.\n041858     MOVE 9999 TO Z-EXIT-LEVEL.\n041860 Z-30-2-LOOP.\n041862     IF TP-LN-POS = 9\n041864         GO TO Z-30-2-XIT.\n041866     MOVE TP-SUB (TP-LN-POS, TP-LN-DPTH) TO TP-SUB-CNT.\n041868     MOVE TPFORMCHAR (TP-SUB-CNT) TO PR-LN-LTR (TP-LN-POS).\n041870     ADD 1 TO TP-LN-POS .\n041872     IF Z-EDIT-ERROR\n041874         GO TO Z-30-XIT.\n041876 Z-30-2-SKIP.\n041878     GO TO Z-30-2-LOOP.\n041880*\n041882 Z-30-2-XIT.\n041884     MOVE PR-LINE-TP TO PRINT-LINE.\n041886************ PERFORM TPR-WRITE-TEAR\n041888     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.\n041890     IF  Z-EXIT-EDITEXIT\n041892         GO TO Z-30-XIT.\n041894     IF  Z-DMS2-ABORT-FLAG = 1\n041896         GO TO Z-30-XIT.\n041898     IF  Z-EXIT-LEVEL < 0\n041900         GO TO Z-30-1-END.\n041902*\n041904************ PERFORM TPR-WRITE-TEAR\n041906     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.\n041908     IF  Z-EXIT-EDITEXIT\n041910         GO TO Z-30-XIT.\n041912     IF  Z-DMS2-ABORT-FLAG = 1\n041914         GO TO Z-30-XIT.\n041916     IF  Z-EXIT-LEVEL < 0\n041918         GO TO Z-30-1-END.\n041920*\n041922     ADD 1 TO TP-LN-DPTH .\n041924     MOVE 1 TO TP-LN-POS.\n041926 Z-30-1-END.\n041928     IF Z-EDIT-ERROR\n041930         GO TO Z-30-XIT.\n041932 Z-30-1-SKIP.\n041934     IF Z-EXIT-LEVEL < 1\n041936         GO TO Z-30-END.\n041938     IF Z-EXIT-CODE > 0\n041940         GO TO Z-30-1-XIT.\n041942     GO TO Z-30-1-LOOP.\n041944*\n041946 Z-30-1-XIT.\n041948     MOVE 0 TO Z-EXIT-CODE.\n041950     MOVE 9999 TO Z-EXIT-LEVEL.\n041952     MOVE SPACES TO PRINT-LINE.\n041954************ PERFORM TPR-WRITE-TEAR\n041956     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.\n041958     IF  Z-EXIT-EDITEXIT\n041960         GO TO Z-30-XIT.\n041962     IF  Z-DMS2-ABORT-FLAG = 1\n041964         GO TO Z-30-XIT.\n041966     IF  Z-EXIT-LEVEL < 0\n041968         GO TO Z-30-END.\n041970*\n041972************ PERFORM TPR-WRITE-TEAR\n041974     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.\n041976     IF  Z-EXIT-EDITEXIT\n041978         GO TO Z-30-XIT.\n041980     IF  Z-DMS2-ABORT-FLAG = 1\n041982         GO TO Z-30-XIT.\n041984     IF  Z-EXIT-LEVEL < 0\n041986         GO TO Z-30-END.\n041988*\n041990     IF TP-LN-CT = 1 AND TP-LN2 = SPACES\n041992         NEXT SENTENCE ELSE\n041994         GO TO Z-30-14-1-ELSE.\n041996     ADD 1 TO TP-LN-CT .\n041998 Z-30-14-1-ELSE.\n042000     IF TP-LN-CT = 2 AND TP-LN3 = SPACES\n042002         NEXT SENTENCE ELSE\n042004         GO TO Z-30-16-1-ELSE.\n042006     ADD 1 TO TP-LN-CT .\n042008 Z-30-16-1-ELSE.\n042010     MOVE 1 TO TP-LN-DPTH.\n042012     ADD 1 TO TP-LN-CT .\n042014     IF TP-LN-CT = 2\n042016         NEXT SENTENCE ELSE\n042018         GO TO Z-30-20-1-ELSE.\n042020     MOVE TP-LN2 TO TP-LN1.\n042022 Z-30-20-1-ELSE.\n042024     IF TP-LN-CT = 3\n042026         NEXT SENTENCE ELSE\n042028         GO TO Z-30-22-1-ELSE.\n042030     MOVE TP-LN3 TO TP-LN1.\n042032 Z-30-22-1-ELSE.\n042034     MOVE 0 TO TP-LN-POS.\n042036 Z-30-END.\n042038     IF Z-EDIT-ERROR\n042040         GO TO Z-30-XIT.\n042042 Z-30-SKIP.\n042044     IF Z-EXIT-LEVEL NOT < 0\n042046         MOVE 0 TO Z-EXIT-CODE\n042048         MOVE 9999 TO Z-EXIT-LEVEL.\n042050 Z-30-XIT.\n042052     EXIT.\n042054*\n042056*****************************************************************\n042058*    PROCEDURE TPR-WRITE-TEAR\n042060*****************************************************************\n042062 Z-29-PROCEDURE.\n042064*\n042066     IF NOT Z-SW3\n042068         NEXT SENTENCE ELSE\n042070         GO TO Z-29-1-1-ELSE.\n042072     IF H-REPORT-NO = \"TDA-700\"\n042074         NEXT SENTENCE ELSE\n042076         GO TO Z-29-2-1-ELSE.\n042078     COMPUTE Z-LINES-HOLD = 1.\n042080     COMPUTE Z-LINES = 1.\n042082     IF Z-RPT-1-TRAP > ZERO\n042084         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n042086     IF Z-LINES > Z-RPT-1-TRAP\n042088       IF Z-RPTINFO1-INBLOCK = ZERO\n042090         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n042092         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n042094         COMPUTE Z-LINES = 1.\n042096     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n042098     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n042100     MOVE PRINT-LINE TO Z-RPT-1-BUFFER.\n042102     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n042104     GO TO Z-29-2-ENDIF.\n042106 Z-29-2-1-ELSE.\n042108     IF H-REPORT-NO = \"TDA-701\"\n042110         NEXT SENTENCE ELSE\n042112         GO TO Z-29-2-2-ELSE.\n042114     COMPUTE Z-LINES-HOLD = 1.\n042116     COMPUTE Z-LINES = 1.\n042118     IF Z-RPT-2-TRAP > ZERO\n042120         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.\n042122     IF Z-LINES > Z-RPT-2-TRAP\n042124       IF Z-RPTINFO2-INBLOCK = ZERO\n042126         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1\n042128         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT\n042130         COMPUTE Z-LINES = 1.\n042132     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).\n042134     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).\n042136     MOVE PRINT-LINE TO Z-RPT-2-BUFFER.\n042138     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.\n042140 Z-29-2-2-ELSE.\n042142 Z-29-2-ENDIF.\n042144 Z-29-1-1-ELSE.\n042146     IF Z-EDIT-ERROR\n042148         GO TO Z-29-XIT.\n042150 Z-29-SKIP.\n042152 Z-29-XIT.\n042154     EXIT.\n042156*\n042158*****************************************************************\n042160*    PROCEDURE RMDRPT-SETUP\n042162*****************************************************************\n042164 Z-24-PROCEDURE.\n042166*\n042168     MOVE 0 TO Z-EXIT-CODE.\n042170     MOVE 9999 TO Z-EXIT-LEVEL.\n042172     MOVE \"TDA-700\" TO H-REPORT-NO.\n042174     MOVE \"TDA/RMDRPT\" TO WS-TP-DLY-WKLY.\n042176     MOVE \"RMD CALCULATION REPORT\" TO H-RPT-TITLE.\n042178     MOVE RMD-BK TO GWS-CSI-BK\n042180       , BANK-NO.\n042182     IF WS-NEW-RPT = 1\n042184         NEXT SENTENCE ELSE\n042186         GO TO Z-24-5-1-ELSE.\n042188************ PERFORM CHECK-PRT-FILE\n042190     PERFORM Z-20-PROCEDURE THRU Z-20-XIT.\n042192     IF  Z-EXIT-EDITEXIT\n042194         GO TO Z-24-XIT.\n042196     IF  Z-DMS2-ABORT-FLAG = 1\n042198         GO TO Z-24-XIT.\n042200     IF  Z-EXIT-LEVEL < 0\n042202         GO TO Z-24-END.\n042204*\n042206     MOVE SPACES TO HEADER-LINE2-160\n042208       , HEADER-LINE3-160\n042210       , HEADER-LINE4-160\n042212       , HEADER-LINE5-160.\n042214 Z-24-5-1-ELSE.\n042216     MOVE RMDRPT-REC-2 TO HEADER-LINE2-160.\n042218     MOVE RMDRPT-REC-6 TO HEADER-LINE3-160.\n042220     MOVE 4 TO HDR-CTL.\n042222************ PERFORM SETUP-NEW-REPORT\n042224     IF WS-NEW-RPT = 1\n042226        NEXT SENTENCE ELSE\n042228        GO TO Z-24-11-SKIPPROC.\n042230************ PERFORM SETUP-NEW-REPORT\n042232     PERFORM Z-18-PROCEDURE THRU Z-18-XIT.\n042234     IF  Z-EXIT-EDITEXIT\n042236         GO TO Z-24-XIT.\n042238     IF  Z-DMS2-ABORT-FLAG = 1\n042240         GO TO Z-24-XIT.\n042242     IF  Z-EXIT-LEVEL < 0\n042244         GO TO Z-24-END.\n042246*\n042248 Z-24-11-SKIPPROC.\n042250 Z-24-END.\n042252     IF Z-EDIT-ERROR\n042254         GO TO Z-24-XIT.\n042256 Z-24-SKIP.\n042258     IF Z-EXIT-LEVEL NOT < 0\n042260         MOVE 0 TO Z-EXIT-CODE\n042262         MOVE 9999 TO Z-EXIT-LEVEL.\n042264 Z-24-XIT.\n042266     EXIT.\n042268*\n042270*****************************************************************\n042272*    PROCEDURE RMDRPT2-SETUP\n042274*****************************************************************\n042276 Z-25-PROCEDURE.\n042278*\n042280     MOVE 0 TO Z-EXIT-CODE.\n042282     MOVE 9999 TO Z-EXIT-LEVEL.\n042284     MOVE \"TDA-701\" TO H-REPORT-NO.\n042286     MOVE \"TDA/RMDRPT2\" TO WS-TP-DLY-WKLY.\n042288     MOVE \"RMD CALCULATION REPORT FOR INHERITED IRA'S\" TO         \n042290         H-RPT-TITLE.\n042292     MOVE RMD-BK TO GWS-CSI-BK\n042294       , BANK-NO.\n042296     IF WS-NEW-RPT = 1\n042298         NEXT SENTENCE ELSE\n042300         GO TO Z-25-5-1-ELSE.\n042302************ PERFORM CHECK-PRT-FILE\n042304     PERFORM Z-20-PROCEDURE THRU Z-20-XIT.\n042306     IF  Z-EXIT-EDITEXIT\n042308         GO TO Z-25-XIT.\n042310     IF  Z-DMS2-ABORT-FLAG = 1\n042312         GO TO Z-25-XIT.\n042314     IF  Z-EXIT-LEVEL < 0\n042316         GO TO Z-25-END.\n042318*\n042320     MOVE SPACES TO HEADER-LINE2-160\n042322       , HEADER-LINE3-160\n042324       , HEADER-LINE4-160\n042326       , HEADER-LINE5-160.\n042328 Z-25-5-1-ELSE.\n042330     MOVE RMDRPT2-REC-2 TO HEADER-LINE2-160.\n042332     MOVE RMDRPT2-REC-6 TO HEADER-LINE3-160.\n042334     MOVE 4 TO HDR-CTL.\n042336************ PERFORM SETUP-NEW-REPORT\n042338     IF WS-NEW-RPT = 1\n042340        NEXT SENTENCE ELSE\n042342        GO TO Z-25-11-SKIPPROC.\n042344************ PERFORM SETUP-NEW-REPORT\n042346     PERFORM Z-18-PROCEDURE THRU Z-18-XIT.\n042348     IF  Z-EXIT-EDITEXIT\n042350         GO TO Z-25-XIT.\n042352     IF  Z-DMS2-ABORT-FLAG = 1\n042354         GO TO Z-25-XIT.\n042356     IF  Z-EXIT-LEVEL < 0\n042358         GO TO Z-25-END.\n042360*\n042362 Z-25-11-SKIPPROC.\n042364 Z-25-END.\n042366     IF Z-EDIT-ERROR\n042368         GO TO Z-25-XIT.\n042370 Z-25-SKIP.\n042372     IF Z-EXIT-LEVEL NOT < 0\n042374         MOVE 0 TO Z-EXIT-CODE\n042376         MOVE 9999 TO Z-EXIT-LEVEL.\n042378 Z-25-XIT.\n042380     EXIT.\n042382*\n042384*****************************************************************\n042386*    PROCEDURE GENLCOPY-PROCEDURES\n042388*****************************************************************\n042390 Z-31-PROCEDURE.\n042392*\n042394 999999-CHANGE1.                                                  \n042396     CHANGE ATTRIBUTE FILENAME OF LISTING TO WS-LISTING-NAME.     \n042398 999999-CHANGE22.                                                 \n042400     CHANGE ATTRIBUTE FILENAME OF FICHE   TO WS-FICHE-NAME.       \n042402 999999-CHANGE24.                                                 \n042404     CHANGE ATTRIBUTE FAMILYNAME OF LISTING TO GWS-PACK.          \n042406 999999-CHANGE33.                                                 \n042408     CHANGE ATTRIBUTE FAMILYNAME OF FICHE   TO GWS-PACK.          \n042410 999999-CHANGE34.                                                 \n042412     CHANGE ATTRIBUTE DESTINATION OF LISTING TO \"DPRTR\".          \n042414 999999-CHANGE35.                                                 \n042416     CHANGE ATTRIBUTE DESTINATION OF LISTING TO \"DPRTR\".          \n042418 999999-CHANGE52.                                                 \n042420     CHANGE ATTRIBUTE DESTINATION OF FICHE TO \"DPRTR\".            \n042422 999999-CHANGE53.                                                 \n042424     CHANGE ATTRIBUTE DESTINATION OF FICHE TO \"DPRTR\".            \n042426 999999-CHANGE54.                                                 \n042428     CHANGE ATTRIBUTE PRINTDISPOSITION OF LISTING TO 2.           \n042430 999999-CHANGE55.                                                 \n042432     CHANGE ATTRIBUTE PRINTDISPOSITION OF LISTING TO 0.           \n042434 999999-CHANGE72.                                                 \n042436     CHANGE ATTRIBUTE PRINTDISPOSITION OF FICHE TO 2.             \n042438 999999-CHANGE73.                                                 \n042440     CHANGE ATTRIBUTE PRINTDISPOSITION OF FICHE TO 0.             \n042442     IF Z-EDIT-ERROR\n042444         GO TO Z-31-XIT.\n042446 Z-31-SKIP.\n042448 Z-31-XIT.\n042450     EXIT.\n042452*\n042454*****************************************************************\n042456*    PROCEDURE WRITE-CUST-FM-REC\n042458*****************************************************************\n042460 Z-26-PROCEDURE.\n042462*\n042464     IF ( WS-BANK-OPT = 3 ) AND ( WS-TIN-RMD-TOT > 0 )\n042466         NEXT SENTENCE ELSE\n042468         GO TO Z-26-1-1-ELSE.\n042470     MOVE 1 TO J.\n042472 Z-26-2-LOOP.\n042474     IF J > 50\n042476         GO TO Z-26-2-XIT.\n042478     MOVE 0 TO Z-EXIT-CODE.\n042480     MOVE 9999 TO Z-EXIT-LEVEL.\n042482********* EXIT WHEN\n042484     IF WS-TIN-CUST (J) = ZEROS\n042486        NEXT SENTENCE\n042488     ELSE\n042490        GO TO Z-26-3-EXIT-SKIP.\n042492     MOVE 1 TO Z-EXIT-LEVEL.\n042494     MOVE 1 TO Z-EXIT-CODE.\n042496     GO TO Z-26-2-END.\n042498 Z-26-3-EXIT-SKIP.\n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 579 lines from 20667 to 21245.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 43,
  "total_chunks": 55,
  "start_line": 20667,
  "end_line": 21245,
  "line_count": 579
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
- Source code length: 28322 characters

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
CHUNK 43 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 20667 to 21245 (579 lines)
Chunk Tokens (estimated): ~7,725
Actual Input Tokens: 9,131 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 20667-21245 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 43 of 55 chunks
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
      The source code below is only CHUNK 43 of 55.


=============================================================================
CHUNK 43 SOURCE CODE (Lines 20667-21245)
=============================================================================

```cobol
041342 Z-5-254-1-ELSE.
041344     IF WS-INHERIT-IRA-ON-TIN = 1
041346         NEXT SENTENCE ELSE
041348         GO TO Z-5-263-1-ELSE.
041350     MOVE WS-PREV-TIN TO WS-RMDRPT2-TIN.
041352     MOVE "-" TO WS-RMDRPT2-TIN-LDASH
041354       , WS-RMDRPT2-TIN-RDASH.
041356     MOVE WS-RMDRPT2-TIN TO RMDRPT-TOT-TIN-10.
041358     IF NOT Z-SW3
041360         NEXT SENTENCE ELSE
041362         GO TO Z-5-267-1-ELSE.
041364     COMPUTE Z-LINES-HOLD = 1.
041366     COMPUTE Z-LINES = 1.
041368     IF Z-RPT-2-TRAP > ZERO
041370         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.
041372     IF Z-LINES > Z-RPT-2-TRAP
041374       IF Z-RPTINFO2-INBLOCK = ZERO
041376         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1
041378         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT
041380         COMPUTE Z-LINES = 1.
041382     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).
041384     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).
041386     MOVE RMDRPT-REC-10 TO Z-RPT-2-BUFFER.
041388     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.
041390     COMPUTE Z-LINES-HOLD = 1.
041392     COMPUTE Z-LINES = 1.
041394     IF Z-RPT-2-TRAP > ZERO
041396         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.
041398     IF Z-LINES > Z-RPT-2-TRAP
041400       IF Z-RPTINFO2-INBLOCK = ZERO
041402         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1
041404         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT
041406         COMPUTE Z-LINES = 1.
041408     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).
041410     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).
041412     MOVE SPACES TO Z-RPT-2-BUFFER.
041414     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.
041416 Z-5-267-1-ELSE.
041418 Z-5-263-1-ELSE.
041420     MOVE ZEROS TO WS-TIN-TOTALS
041422       , WS-INHERIT-IRA-ON-TIN
041424       , WS-NON-INHERIT-IRA-ON-TIN.
041426     MOVE RMD-COUNT TO RMDRPT-CNT-5.
041428     COMPUTE Z-LINES-HOLD = 2.
041430     COMPUTE Z-LINES = 2.
041432     IF Z-RPT-1-TRAP > ZERO
041434         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
041436     IF Z-LINES > Z-RPT-1-TRAP
041438       IF Z-RPTINFO1-INBLOCK = ZERO
041440         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
041442         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
041444         COMPUTE Z-LINES = 2.
041446     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
041448     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
041450     MOVE RMDRPT-REC-5 TO Z-RPT-1-BUFFER.
041452     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
041454     MOVE RMD-TOT-CHGD TO RMDRPT-TOT-FM-7.
041456     IF SPECS-RMD-OVERRIDE = "Y"
041458         NEXT SENTENCE ELSE
041460         GO TO Z-5-274-1-ELSE.
041462     COMPUTE Z-LINES-HOLD = 1.
041464     COMPUTE Z-LINES = 1.
041466     IF Z-RPT-1-TRAP > ZERO
041468         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
041470     IF Z-LINES > Z-RPT-1-TRAP
041472       IF Z-RPTINFO1-INBLOCK = ZERO
041474         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
041476         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
041478         COMPUTE Z-LINES = 1.
041480     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
041482     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
041484     MOVE RMDRPT-REC-7 TO Z-RPT-1-BUFFER.
041486     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
041488 Z-5-274-1-ELSE.
041490     IF WS-MDRPT2-OPEN = 1
041492         NEXT SENTENCE ELSE
041494         GO TO Z-5-276-1-ELSE.
041496     MOVE RMD-COUNT-INHERIT TO RMDRPT-CNT-5.
041498     COMPUTE Z-LINES-HOLD = 2.
041500     COMPUTE Z-LINES = 2.
041502     IF Z-RPT-2-TRAP > ZERO
041504         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.
041506     IF Z-LINES > Z-RPT-2-TRAP
041508       IF Z-RPTINFO2-INBLOCK = ZERO
041510         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1
041512         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT
041514         COMPUTE Z-LINES = 2.
041516     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).
041518     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).
041520     MOVE RMDRPT-REC-5 TO Z-RPT-2-BUFFER.
041522     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.
041524     IF SPECS-RMD-OVERRIDE = "Y"
041526         NEXT SENTENCE ELSE
041528         GO TO Z-5-279-1-ELSE.
041530     MOVE RMD-TOT-CHGD-INHERIT TO RMDRPT-TOT-FM-7.
041532     COMPUTE Z-LINES-HOLD = 1.
041534     COMPUTE Z-LINES = 1.
041536     IF Z-RPT-2-TRAP > ZERO
041538         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.
041540     IF Z-LINES > Z-RPT-2-TRAP
041542       IF Z-RPTINFO2-INBLOCK = ZERO
041544         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1
041546         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT
041548         COMPUTE Z-LINES = 1.
041550     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).
041552     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).
041554     MOVE RMDRPT-REC-7 TO Z-RPT-2-BUFFER.
041556     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.
041558 Z-5-279-1-ELSE.
041560 Z-5-276-1-ELSE.
041562 Z-5-229-1-ELSE.
041564 Z-5-END.
041566     IF Z-EDIT-ERROR
041568         GO TO Z-5-XIT.
041570 Z-5-SKIP.
041572     IF Z-EXIT-LEVEL NOT < 0
041574         MOVE 0 TO Z-EXIT-CODE
041576         MOVE 9999 TO Z-EXIT-LEVEL.
041578 Z-5-XIT.
041580     EXIT.
041582*
041584*****************************************************************
041586*    PROCEDURE TPR-TEAR-PAGES
041588*****************************************************************
041590 Z-21-PROCEDURE.
041592*
041594     MOVE 0 TO Z-EXIT-CODE.
041596     MOVE 9999 TO Z-EXIT-LEVEL.
041598     MOVE ZEROS TO PAGE-CTR.
041600     MOVE SPACES TO PRINT-LINE.
041602     IF GWS-TP-CTL = 1
041604         NEXT SENTENCE ELSE
041606         GO TO Z-21-3-1-ELSE.
041608     MOVE HEADER-LINE1 TO PRINT-LINE.
041610     GO TO Z-21-3-ENDIF.
041612 Z-21-3-1-ELSE.
041614     MOVE SPACES TO PRINT-LINE.
041616 Z-21-3-ENDIF.
041618     IF RPT601-BANNER-HEADER = 0
041620         NEXT SENTENCE ELSE
041622         GO TO Z-21-6-1-ELSE.
041624     MOVE 1 TO PAGE-ADVANCE.
041626************ PERFORM TPR-WRITE-TEAR
041628     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.
041630     IF  Z-EXIT-EDITEXIT
041632         GO TO Z-21-XIT.
041634     IF  Z-DMS2-ABORT-FLAG = 1
041636         GO TO Z-21-XIT.
041638     IF  Z-EXIT-LEVEL < 0
041640         GO TO Z-21-END.
041642*
041644     GO TO Z-21-6-ENDIF.
041646 Z-21-6-1-ELSE.
041648     MOVE 0 TO RPT601-BANNER-HEADER.
041650 Z-21-6-ENDIF.
041652     MOVE 0 TO PAGE-ADVANCE.
041654     MOVE ALL "*" TO PRINT-LINE.
041656************ PERFORM TPR-WRITE-TEAR
041658     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.
041660     IF  Z-EXIT-EDITEXIT
041662         GO TO Z-21-XIT.
041664     IF  Z-DMS2-ABORT-FLAG = 1
041666         GO TO Z-21-XIT.
041668     IF  Z-EXIT-LEVEL < 0
041670         GO TO Z-21-END.
041672*
041674************ PERFORM TPR-WRITE-TEAR
041676     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.
041678     IF  Z-EXIT-EDITEXIT
041680         GO TO Z-21-XIT.
041682     IF  Z-DMS2-ABORT-FLAG = 1
041684         GO TO Z-21-XIT.
041686     IF  Z-EXIT-LEVEL < 0
041688         GO TO Z-21-END.
041690*
041692     MOVE SPACES TO PRINT-LINE.
041694************ PERFORM TPR-WRITE-TEAR
041696     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.
041698     IF  Z-EXIT-EDITEXIT
041700         GO TO Z-21-XIT.
041702     IF  Z-DMS2-ABORT-FLAG = 1
041704         GO TO Z-21-XIT.
041706     IF  Z-EXIT-LEVEL < 0
041708         GO TO Z-21-END.
041710*
041712     MOVE 0 TO TP-LN-POS.
041714     MOVE 1 TO TP-LN-CT
041716       , TP-LN-DPTH.
041718 Z-21-18-LOOP.
041720     IF TP-LN-CT = 4
041722         GO TO Z-21-18-XIT.
041724     MOVE 0 TO Z-EXIT-CODE.
041726     MOVE 9999 TO Z-EXIT-LEVEL.
041728     ADD 1 TO TP-LN-POS .
041730     IF TP-LN-POS = 9
041732         NEXT SENTENCE ELSE
041734         GO TO Z-21-20-1-ELSE.
041736     MOVE 1 TO TP-LN-POS.
041738************ PERFORM TPR-PRINT-TEAR
041740     PERFORM Z-30-PROCEDURE THRU Z-30-XIT.
041742     IF  Z-EXIT-EDITEXIT
041744         GO TO Z-21-XIT.
041746     IF  Z-DMS2-ABORT-FLAG = 1
041748         GO TO Z-21-XIT.
041750     IF  Z-EXIT-LEVEL < 0
041752         GO TO Z-21-18-END.
041754*
041756     GO TO Z-21-20-ENDIF.
041758 Z-21-20-1-ELSE.
041760     MOVE 1 TO TP-AR.
041762     MOVE TP-DECODE (TP-AR) TO TP-DECODE-WKA (TP-LN-POS).
041764 Z-21-25-LOOP.
041766     IF ( TP-SUBSCRIPT (TP-LN-POS) = TP-IN-CHAR (TP-LN-POS) ) OR  
041768         ( TP-SUBSCRIPT (TP-LN-POS) = SPACES )
041770         GO TO Z-21-25-XIT.
041772     ADD 1 TO TP-AR .
041774     MOVE TP-DECODE (TP-AR) TO TP-DECODE-WKA (TP-LN-POS).
041776     IF Z-EDIT-ERROR
041778         GO TO Z-21-XIT.
041780 Z-21-25-SKIP.
041782     GO TO Z-21-25-LOOP.
041784*
041786 Z-21-25-XIT.
041788 Z-21-20-ENDIF.
041790 Z-21-18-END.
041792     IF Z-EDIT-ERROR
041794         GO TO Z-21-XIT.
041796 Z-21-18-SKIP.
041798     IF Z-EXIT-LEVEL < 1
041800         GO TO Z-21-END.
041802     IF Z-EXIT-CODE > 0
041804         GO TO Z-21-18-XIT.
041806     GO TO Z-21-18-LOOP.
041808*
041810 Z-21-18-XIT.
041812     MOVE 0 TO Z-EXIT-CODE.
041814     MOVE 9999 TO Z-EXIT-LEVEL.
041816 Z-21-END.
041818     IF Z-EDIT-ERROR
041820         GO TO Z-21-XIT.
041822 Z-21-SKIP.
041824     IF Z-EXIT-LEVEL NOT < 0
041826         MOVE 0 TO Z-EXIT-CODE
041828         MOVE 9999 TO Z-EXIT-LEVEL.
041830 Z-21-XIT.
041832     EXIT.
041834*
041836*****************************************************************
041838*    PROCEDURE TPR-PRINT-TEAR
041840*****************************************************************
041842 Z-30-PROCEDURE.
041844*
041846     MOVE 0 TO Z-EXIT-CODE.
041848     MOVE 9999 TO Z-EXIT-LEVEL.
041850 Z-30-1-LOOP.
041852     IF TP-LN-DPTH = 6
041854         GO TO Z-30-1-XIT.
041856     MOVE 0 TO Z-EXIT-CODE.
041858     MOVE 9999 TO Z-EXIT-LEVEL.
041860 Z-30-2-LOOP.
041862     IF TP-LN-POS = 9
041864         GO TO Z-30-2-XIT.
041866     MOVE TP-SUB (TP-LN-POS, TP-LN-DPTH) TO TP-SUB-CNT.
041868     MOVE TPFORMCHAR (TP-SUB-CNT) TO PR-LN-LTR (TP-LN-POS).
041870     ADD 1 TO TP-LN-POS .
041872     IF Z-EDIT-ERROR
041874         GO TO Z-30-XIT.
041876 Z-30-2-SKIP.
041878     GO TO Z-30-2-LOOP.
041880*
041882 Z-30-2-XIT.
041884     MOVE PR-LINE-TP TO PRINT-LINE.
041886************ PERFORM TPR-WRITE-TEAR
041888     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.
041890     IF  Z-EXIT-EDITEXIT
041892         GO TO Z-30-XIT.
041894     IF  Z-DMS2-ABORT-FLAG = 1
041896         GO TO Z-30-XIT.
041898     IF  Z-EXIT-LEVEL < 0
041900         GO TO Z-30-1-END.
041902*
041904************ PERFORM TPR-WRITE-TEAR
041906     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.
041908     IF  Z-EXIT-EDITEXIT
041910         GO TO Z-30-XIT.
041912     IF  Z-DMS2-ABORT-FLAG = 1
041914         GO TO Z-30-XIT.
041916     IF  Z-EXIT-LEVEL < 0
041918         GO TO Z-30-1-END.
041920*
041922     ADD 1 TO TP-LN-DPTH .
041924     MOVE 1 TO TP-LN-POS.
041926 Z-30-1-END.
041928     IF Z-EDIT-ERROR
041930         GO TO Z-30-XIT.
041932 Z-30-1-SKIP.
041934     IF Z-EXIT-LEVEL < 1
041936         GO TO Z-30-END.
041938     IF Z-EXIT-CODE > 0
041940         GO TO Z-30-1-XIT.
041942     GO TO Z-30-1-LOOP.
041944*
041946 Z-30-1-XIT.
041948     MOVE 0 TO Z-EXIT-CODE.
041950     MOVE 9999 TO Z-EXIT-LEVEL.
041952     MOVE SPACES TO PRINT-LINE.
041954************ PERFORM TPR-WRITE-TEAR
041956     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.
041958     IF  Z-EXIT-EDITEXIT
041960         GO TO Z-30-XIT.
041962     IF  Z-DMS2-ABORT-FLAG = 1
041964         GO TO Z-30-XIT.
041966     IF  Z-EXIT-LEVEL < 0
041968         GO TO Z-30-END.
041970*
041972************ PERFORM TPR-WRITE-TEAR
041974     PERFORM Z-29-PROCEDURE THRU Z-29-XIT.
041976     IF  Z-EXIT-EDITEXIT
041978         GO TO Z-30-XIT.
041980     IF  Z-DMS2-ABORT-FLAG = 1
041982         GO TO Z-30-XIT.
041984     IF  Z-EXIT-LEVEL < 0
041986         GO TO Z-30-END.
041988*
041990     IF TP-LN-CT = 1 AND TP-LN2 = SPACES
041992         NEXT SENTENCE ELSE
041994         GO TO Z-30-14-1-ELSE.
041996     ADD 1 TO TP-LN-CT .
041998 Z-30-14-1-ELSE.
042000     IF TP-LN-CT = 2 AND TP-LN3 = SPACES
042002         NEXT SENTENCE ELSE
042004         GO TO Z-30-16-1-ELSE.
042006     ADD 1 TO TP-LN-CT .
042008 Z-30-16-1-ELSE.
042010     MOVE 1 TO TP-LN-DPTH.
042012     ADD 1 TO TP-LN-CT .
042014     IF TP-LN-CT = 2
042016         NEXT SENTENCE ELSE
042018         GO TO Z-30-20-1-ELSE.
042020     MOVE TP-LN2 TO TP-LN1.
042022 Z-30-20-1-ELSE.
042024     IF TP-LN-CT = 3
042026         NEXT SENTENCE ELSE
042028         GO TO Z-30-22-1-ELSE.
042030     MOVE TP-LN3 TO TP-LN1.
042032 Z-30-22-1-ELSE.
042034     MOVE 0 TO TP-LN-POS.
042036 Z-30-END.
042038     IF Z-EDIT-ERROR
042040         GO TO Z-30-XIT.
042042 Z-30-SKIP.
042044     IF Z-EXIT-LEVEL NOT < 0
042046         MOVE 0 TO Z-EXIT-CODE
042048         MOVE 9999 TO Z-EXIT-LEVEL.
042050 Z-30-XIT.
042052     EXIT.
042054*
042056*****************************************************************
042058*    PROCEDURE TPR-WRITE-TEAR
042060*****************************************************************
042062 Z-29-PROCEDURE.
042064*
042066     IF NOT Z-SW3
042068         NEXT SENTENCE ELSE
042070         GO TO Z-29-1-1-ELSE.
042072     IF H-REPORT-NO = "TDA-700"
042074         NEXT SENTENCE ELSE
042076         GO TO Z-29-2-1-ELSE.
042078     COMPUTE Z-LINES-HOLD = 1.
042080     COMPUTE Z-LINES = 1.
042082     IF Z-RPT-1-TRAP > ZERO
042084         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
042086     IF Z-LINES > Z-RPT-1-TRAP
042088       IF Z-RPTINFO1-INBLOCK = ZERO
042090         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
042092         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
042094         COMPUTE Z-LINES = 1.
042096     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
042098     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
042100     MOVE PRINT-LINE TO Z-RPT-1-BUFFER.
042102     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
042104     GO TO Z-29-2-ENDIF.
042106 Z-29-2-1-ELSE.
042108     IF H-REPORT-NO = "TDA-701"
042110         NEXT SENTENCE ELSE
042112         GO TO Z-29-2-2-ELSE.
042114     COMPUTE Z-LINES-HOLD = 1.
042116     COMPUTE Z-LINES = 1.
042118     IF Z-RPT-2-TRAP > ZERO
042120         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.
042122     IF Z-LINES > Z-RPT-2-TRAP
042124       IF Z-RPTINFO2-INBLOCK = ZERO
042126         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1
042128         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT
042130         COMPUTE Z-LINES = 1.
042132     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).
042134     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).
042136     MOVE PRINT-LINE TO Z-RPT-2-BUFFER.
042138     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.
042140 Z-29-2-2-ELSE.
042142 Z-29-2-ENDIF.
042144 Z-29-1-1-ELSE.
042146     IF Z-EDIT-ERROR
042148         GO TO Z-29-XIT.
042150 Z-29-SKIP.
042152 Z-29-XIT.
042154     EXIT.
042156*
042158*****************************************************************
042160*    PROCEDURE RMDRPT-SETUP
042162*****************************************************************
042164 Z-24-PROCEDURE.
042166*
042168     MOVE 0 TO Z-EXIT-CODE.
042170     MOVE 9999 TO Z-EXIT-LEVEL.
042172     MOVE "TDA-700" TO H-REPORT-NO.
042174     MOVE "TDA/RMDRPT" TO WS-TP-DLY-WKLY.
042176     MOVE "RMD CALCULATION REPORT" TO H-RPT-TITLE.
042178     MOVE RMD-BK TO GWS-CSI-BK
042180       , BANK-NO.
042182     IF WS-NEW-RPT = 1
042184         NEXT SENTENCE ELSE
042186         GO TO Z-24-5-1-ELSE.
042188************ PERFORM CHECK-PRT-FILE
042190     PERFORM Z-20-PROCEDURE THRU Z-20-XIT.
042192     IF  Z-EXIT-EDITEXIT
042194         GO TO Z-24-XIT.
042196     IF  Z-DMS2-ABORT-FLAG = 1
042198         GO TO Z-24-XIT.
042200     IF  Z-EXIT-LEVEL < 0
042202         GO TO Z-24-END.
042204*
042206     MOVE SPACES TO HEADER-LINE2-160
042208       , HEADER-LINE3-160
042210       , HEADER-LINE4-160
042212       , HEADER-LINE5-160.
042214 Z-24-5-1-ELSE.
042216     MOVE RMDRPT-REC-2 TO HEADER-LINE2-160.
042218     MOVE RMDRPT-REC-6 TO HEADER-LINE3-160.
042220     MOVE 4 TO HDR-CTL.
042222************ PERFORM SETUP-NEW-REPORT
042224     IF WS-NEW-RPT = 1
042226        NEXT SENTENCE ELSE
042228        GO TO Z-24-11-SKIPPROC.
042230************ PERFORM SETUP-NEW-REPORT
042232     PERFORM Z-18-PROCEDURE THRU Z-18-XIT.
042234     IF  Z-EXIT-EDITEXIT
042236         GO TO Z-24-XIT.
042238     IF  Z-DMS2-ABORT-FLAG = 1
042240         GO TO Z-24-XIT.
042242     IF  Z-EXIT-LEVEL < 0
042244         GO TO Z-24-END.
042246*
042248 Z-24-11-SKIPPROC.
042250 Z-24-END.
042252     IF Z-EDIT-ERROR
042254         GO TO Z-24-XIT.
042256 Z-24-SKIP.
042258     IF Z-EXIT-LEVEL NOT < 0
042260         MOVE 0 TO Z-EXIT-CODE
042262         MOVE 9999 TO Z-EXIT-LEVEL.
042264 Z-24-XIT.
042266     EXIT.
042268*
042270*****************************************************************
042272*    PROCEDURE RMDRPT2-SETUP
042274*****************************************************************
042276 Z-25-PROCEDURE.
042278*
042280     MOVE 0 TO Z-EXIT-CODE.
042282     MOVE 9999 TO Z-EXIT-LEVEL.
042284     MOVE "TDA-701" TO H-REPORT-NO.
042286     MOVE "TDA/RMDRPT2" TO WS-TP-DLY-WKLY.
042288     MOVE "RMD CALCULATION REPORT FOR INHERITED IRA'S" TO         
042290         H-RPT-TITLE.
042292     MOVE RMD-BK TO GWS-CSI-BK
042294       , BANK-NO.
042296     IF WS-NEW-RPT = 1
042298         NEXT SENTENCE ELSE
042300         GO TO Z-25-5-1-ELSE.
042302************ PERFORM CHECK-PRT-FILE
042304     PERFORM Z-20-PROCEDURE THRU Z-20-XIT.
042306     IF  Z-EXIT-EDITEXIT
042308         GO TO Z-25-XIT.
042310     IF  Z-DMS2-ABORT-FLAG = 1
042312         GO TO Z-25-XIT.
042314     IF  Z-EXIT-LEVEL < 0
042316         GO TO Z-25-END.
042318*
042320     MOVE SPACES TO HEADER-LINE2-160
042322       , HEADER-LINE3-160
042324       , HEADER-LINE4-160
042326       , HEADER-LINE5-160.
042328 Z-25-5-1-ELSE.
042330     MOVE RMDRPT2-REC-2 TO HEADER-LINE2-160.
042332     MOVE RMDRPT2-REC-6 TO HEADER-LINE3-160.
042334     MOVE 4 TO HDR-CTL.
042336************ PERFORM SETUP-NEW-REPORT
042338     IF WS-NEW-RPT = 1
042340        NEXT SENTENCE ELSE
042342        GO TO Z-25-11-SKIPPROC.
042344************ PERFORM SETUP-NEW-REPORT
042346     PERFORM Z-18-PROCEDURE THRU Z-18-XIT.
042348     IF  Z-EXIT-EDITEXIT
042350         GO TO Z-25-XIT.
042352     IF  Z-DMS2-ABORT-FLAG = 1
042354         GO TO Z-25-XIT.
042356     IF  Z-EXIT-LEVEL < 0
042358         GO TO Z-25-END.
042360*
042362 Z-25-11-SKIPPROC.
042364 Z-25-END.
042366     IF Z-EDIT-ERROR
042368         GO TO Z-25-XIT.
042370 Z-25-SKIP.
042372     IF Z-EXIT-LEVEL NOT < 0
042374         MOVE 0 TO Z-EXIT-CODE
042376         MOVE 9999 TO Z-EXIT-LEVEL.
042378 Z-25-XIT.
042380     EXIT.
042382*
042384*****************************************************************
042386*    PROCEDURE GENLCOPY-PROCEDURES
042388*****************************************************************
042390 Z-31-PROCEDURE.
042392*
042394 999999-CHANGE1.                                                  
042396     CHANGE ATTRIBUTE FILENAME OF LISTING TO WS-LISTING-NAME.     
042398 999999-CHANGE22.                                                 
042400     CHANGE ATTRIBUTE FILENAME OF FICHE   TO WS-FICHE-NAME.       
042402 999999-CHANGE24.                                                 
042404     CHANGE ATTRIBUTE FAMILYNAME OF LISTING TO GWS-PACK.          
042406 999999-CHANGE33.                                                 
042408     CHANGE ATTRIBUTE FAMILYNAME OF FICHE   TO GWS-PACK.          
042410 999999-CHANGE34.                                                 
042412     CHANGE ATTRIBUTE DESTINATION OF LISTING TO "DPRTR".          
042414 999999-CHANGE35.                                                 
042416     CHANGE ATTRIBUTE DESTINATION OF LISTING TO "DPRTR".          
042418 999999-CHANGE52.                                                 
042420     CHANGE ATTRIBUTE DESTINATION OF FICHE TO "DPRTR".            
042422 999999-CHANGE53.                                                 
042424     CHANGE ATTRIBUTE DESTINATION OF FICHE TO "DPRTR".            
042426 999999-CHANGE54.                                                 
042428     CHANGE ATTRIBUTE PRINTDISPOSITION OF LISTING TO 2.           
042430 999999-CHANGE55.                                                 
042432     CHANGE ATTRIBUTE PRINTDISPOSITION OF LISTING TO 0.           
042434 999999-CHANGE72.                                                 
042436     CHANGE ATTRIBUTE PRINTDISPOSITION OF FICHE TO 2.             
042438 999999-CHANGE73.                                                 
042440     CHANGE ATTRIBUTE PRINTDISPOSITION OF FICHE TO 0.             
042442     IF Z-EDIT-ERROR
042444         GO TO Z-31-XIT.
042446 Z-31-SKIP.
042448 Z-31-XIT.
042450     EXIT.
042452*
042454*****************************************************************
042456*    PROCEDURE WRITE-CUST-FM-REC
042458*****************************************************************
042460 Z-26-PROCEDURE.
042462*
042464     IF ( WS-BANK-OPT = 3 ) AND ( WS-TIN-RMD-TOT > 0 )
042466         NEXT SENTENCE ELSE
042468         GO TO Z-26-1-1-ELSE.
042470     MOVE 1 TO J.
042472 Z-26-2-LOOP.
042474     IF J > 50
042476         GO TO Z-26-2-XIT.
042478     MOVE 0 TO Z-EXIT-CODE.
042480     MOVE 9999 TO Z-EXIT-LEVEL.
042482********* EXIT WHEN
042484     IF WS-TIN-CUST (J) = ZEROS
042486        NEXT SENTENCE
042488     ELSE
042490        GO TO Z-26-3-EXIT-SKIP.
042492     MOVE 1 TO Z-EXIT-LEVEL.
042494     MOVE 1 TO Z-EXIT-CODE.
042496     GO TO Z-26-2-END.
042498 Z-26-3-EXIT-SKIP.
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 579 lines from 20667 to 21245.

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

