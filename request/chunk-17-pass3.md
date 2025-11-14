# LLM Request Debug File
Generated: 2025-11-13T20:33:56.276495

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 17/55
- **Model**: gpt-4.1
- **Chunk Number**: 17
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~15,408 tokens
- **Total Input**: ~17,366 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 17/55" (ID: detailed-code-explanation)

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


**CHUNK 17 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 17 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 8033 to 8651 (619 lines)\nChunk Tokens (estimated): ~14,162\nActual Input Tokens: 15,568 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 8033-8651 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 17 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 17 of 55.\n\n\n=============================================================================\nCHUNK 17 SOURCE CODE (Lines 8033-8651)\n=============================================================================\n\n```cobol\n016074             HOLD-TDAPC-BANK-SPECS.                               \n016076             15  HOLD-TDAPC-CREATE-DT      PIC 9(07).             \n016078             15  HOLD-TDAPC-CREATE-TM      PIC 9(12).             \n016080             15  HOLD-TDAPC-DQVISTA        PIC X.                 \n016082             15  HOLD-TDAPC-MSI            PIC X.                 \n016084             15  HOLD-TDAPC-BK-TDA-STAT    PIC X.                 \n016086             15  HOLD-TDAPC-TDA-PILOT REDEFINES                   \n016088                 HOLD-TDAPC-BK-TDA-STAT    PIC X.                 \n016090             15  HOLD-TDAPC-BK-STATUS      PIC X.                 \n016092             15  HOLD-TDAPC-BR-NO          PIC XX.                \n016094             15  HOLD-TDAPC-CSI-BR-CODE REDEFINES                 \n016096                 HOLD-TDAPC-BR-NO          PIC XX.                \n016098             15  HOLD-TDAPC-BK-PHONE-NUM.                         \n016100                 20  HOLD-TDAPC-AREA-CODE  PIC XXX.               \n016102                 20  HOLD-TDAPC-PHONE.                            \n016104                     25  HOLD-TDAPC-PHONE-1ST-3 PIC XXX.          \n016106                     25  HOLD-TDAPC-PHONE-LST-4 PIC X(04).        \n016108             15  HOLD-TDAPC-PHN-NUMBER REDEFINES                  \n016110                 HOLD-TDAPC-BK-PHONE-NUM   PIC X(10).             \n016112             15  HOLD-TDAPC-TDA-ADD-DAY    PIC XXX.               \n016114             15  HOLD-TDAPC-HOLIDAYS       OCCURS 18 TIMES.       \n016116                 20  HOLD-TDAPC-HOL-MM     PIC XX.                \n016118                 20  HOLD-TDAPC-HOL-DD     PIC XX.                \n016120             15  HOLD-TDAPC-FM-SUPPRESS    PIC X.                 \n016122             15  HOLD-TDAPC-RMT-BK-INDICATOR PIC XX.              \n016124             15  HOLD-TDAPC-RMT-IND REDEFINES                     \n016126                 HOLD-TDAPC-RMT-BK-INDICATOR PIC XX.              \n016128             15  HOLD-TDAPC-BK-ADDR        PIC X(28).             \n016130             15  HOLD-TDAPC-BK-ADDR-2      PIC X(27).             \n016132             15  HOLD-TDAPC-FED-ID         PIC X(10).             \n016134             15  HOLD-TDAPC-EOY-RPT-SEQ    PIC X.                 \n016136             15  HOLD-TDAPC-EOY-EARLY-RUN  PIC X.                 \n016138             15  HOLD-TDAPC-EOY-RETURN-TO-BK PIC X.               \n016140             15  HOLD-TDAPC-EOY-RETURN-TO-BANK REDEFINES          \n016142                 HOLD-TDAPC-EOY-RETURN-TO-BK PIC X.               \n016144             15  HOLD-TDAPC-EOY-IRA-PHONE    PIC 9(10).           \n016146             15  HOLD-TDAPC-EOY-DELETE-DATE  PIC 9(06).           \n016148             15  HOLD-TDAPC-EOY-IRA-FICHE  PIC X.                 \n016150             15  HOLD-TDAPC-EOY-IRA-PAPER  PIC X.                 \n016152             15  HOLD-TDAPC-EOY-IRA-STMT-EARLY PIC X.             \n016154             15  HOLD-TDAPC-NO-IRA-STMTS   PIC 9.                 \n016156             15  HOLD-TDAPC-EOY-IRA-STMT   PIC X.                 \n016158             15  HOLD-TDAPC-EOY-IRA-STMT-PRINT PIC X.             \n016160             15  HOLD-TDAPC-EOY-EARLY-DATE PIC 9(06).             \n016162             15  HOLD-TDAPC-CK21-TDA       PIC X.                 \n016164             15  HOLD-TDAPC-MSI-OV-TDA     PIC X.                 \n016166             15  HOLD-TDAPC-BK-IMG-SERV    PIC X(01).             \n016168             15  HOLD-TDAPC-EOY-APRIL-DATE PIC 9(06).             \n016170             15  HOLD-TDAPC-EOY-COD-CLOSED-RPT  PIC X(01).        \n016172             15  HOLD-TDAPC-PRT-NEW        PIC 9(01).             \n016174             15  HOLD-TDAPC-IMONITOR       PIC X(01).             \n016176             15  HOLD-TDAPC-ENTC-TDA       PIC X.                 \n016178             15  HOLD-TDAPC-EV-3RD-PARTY-1 PIC X.                 \n016180             15  HOLD-TDAPC-EV-3RD-PARTY-2 PIC X.                 \n016182             15  HOLD-TDAPC-HSA-LOCATION   PIC X.                 \n016184             15  HOLD-TDAPC-PROFITABILITY  PIC X.                 \n016186             15  HOLD-TDAPC-BANCVUE        PIC X.                 \n016188             15  HOLD-TDAPC-SPECIAL-DL-BILLING PIC X.             \n016190             15  HOLD-TDAPC-CIF-NAME-ADDR  PIC 9.                 \n016192             15  HOLD-TDAPC-MAIL-ADDR-LINES PIC X.                \n016194             15  HOLD-TDAPC-WEB-ENABLED    PIC X(01).             \n016196             15  HOLD-TDAPC-BRANCH-LENGTH  PIC 9.                 \n016198             15  HOLD-TDAPC-LOB            PIC 9.                 \n016200             15  HOLD-TDAPC-BILL-EDIT-TEMPLATES                   \n016202                                           PIC 9.                 \n016204             15  HOLD-TDAPC-MCIF-PRIVACY-OPT                      \n016206                                           PIC 9.                 \n016208             15  HOLD-TDAPC-TRAIN-BK-FLG   PIC X.                 \n016210             15  HOLD-TDAPC-EOY-CIB-F-MERD PIC X(01).             \n016212             15  FILLER                    PIC X(39).             \n016214             15  HOLD-TDAPC-LAST-EOM-PROC  PIC 9(08).             \n016216             15  HOLD-TDAPC-BUS-DT-AFT-NX  PIC 9(08).             \n016218             15  HOLD-TDAPC-NEXT-BUS-DATE  PIC 9(08).             \n016220                                                                  \n016222     05  HOLD-TDAMESSAGE.                                         \n016224         10  HOLD-TDAM-BANK                PIC 9(04).             \n016226         10  HOLD-TDAM-APPL                PIC 9(01).             \n016228         10  HOLD-TDAM-CODE-TYPE           PIC 9(01).             \n016230         10  HOLD-TDAM-CODE                PIC 9(04).             \n016232         10  HOLD-TDAM-RPT-NBR             PIC 9(04).             \n016234         10  HOLD-TDAM-TEST-MSG            PIC 9(01).             \n016236         10  HOLD-TDAM-MESSAGE-NBR         PIC 9(03).             \n016238         10  HOLD-TDAM-MESSAGE-GRP.                               \n016240             15  HOLD-TDAM-MESSAGE         PIC X(60)              \n016242                                           OCCURS 6 TIMES.        \n016244         10  HOLD-TDAM-STOP-DT             PIC 9(08).             \n016246         10  HOLD-TDAM-ADD-DT              PIC 9(08).             \n016248         10  HOLD-TDAM-ADD-TM              PIC 9(08).             \n016250         10  HOLD-TDAM-LUPD-DT             PIC 9(08).             \n016252         10  HOLD-TDAM-LUPD-TM             PIC 9(08).             \n016254         10  HOLD-TDAM-PUB-ID              PIC X(08).             \n016256                                                                  \n016258*** PLEASE REMEMBER TO UPDATE THE TDB,AND HOLD FIELDS WHEN        \n016260*** UPDATING THE FOLLOWING OLD FIELDS.                            \n016262                                                                  \n016264**  The old dataset layouts are used to hold the before picture   \n016266**  of database records.  They will be used when posting activity \n016268**  by comparing the before and after pictures of the database.   \n016270**  This is neccessary because we alter the account record before \n016272**  posting the activity.                                         \n016274                                                                  \n016276     05  OLD-TDACUST-DATA              PIC X(1967).               \n016278     05  OLD-TDACUST.                                             \n016280         10  OLD-TDAC-BANK             PIC 9(4).                  \n016282         10  OLD-TDAC-CUST             PIC 9(12).                 \n016284         10  OLD-TDAC-BRCH             PIC 9(4).                  \n016286         10  OLD-TDAC-STATUS           PIC X(1).                  \n016288         10  OLD-TDAC-NAME-1           PIC X(40).                 \n016290         10  OLD-TDAC-NAME-AREA-1.                                \n016292             15  OLD-TDAC-N1-KEY       PIC X(14).                 \n016294             15  OLD-TDAC-N1-FIRST     PIC X(40).                 \n016296             15  OLD-TDAC-N1-MID       PIC X(20).                 \n016298             15  OLD-TDAC-N1-LAST      PIC X(40).                 \n016300             15  OLD-TDAC-N1-PREFIX    PIC X(12).                 \n016302             15  OLD-TDAC-N1-SUFFIX    PIC X(12).                 \n016304             15  OLD-TDAC-N1-FAMILIAR  PIC X(20).                 \n016306             15  OLD-TDAC-N1-PRT-PFX   PIC X(01).                 \n016308             15  OLD-TDAC-N1-PRT-SFX   PIC X(01).                 \n016310             15  OLD-TDAC-N1-DESIGNAT  PIC X(20).                 \n016312         10  OLD-TDAC-NAME-2           PIC X(40).                 \n016314         10  OLD-TDAC-N2-MODIFIED      PIC X(01).                 \n016316         10  OLD-TDAC-N2-PRINT-CD      PIC X(01).                 \n016318         10  OLD-TDAC-NAME-AREA-2.                                \n016320             15  OLD-TDAC-N2-KEY       PIC X(14).                 \n016322             15  OLD-TDAC-N2-FIRST     PIC X(40).                 \n016324             15  OLD-TDAC-N2-MID       PIC X(20).                 \n016326             15  OLD-TDAC-N2-LAST      PIC X(40).                 \n016328             15  OLD-TDAC-N2-PREFIX    PIC X(12).                 \n016330             15  OLD-TDAC-N2-SUFFIX    PIC X(12).                 \n016332             15  OLD-TDAC-N2-FAMILIAR  PIC X(20).                 \n016334             15  OLD-TDAC-N2-PRT-PFX   PIC X(01).                 \n016336             15  OLD-TDAC-N2-PRT-SFX   PIC X(01).                 \n016338             15  OLD-TDAC-N2-DESIGNAT  PIC X(20).                 \n016340         10  OLD-TDAC-NAME-3           PIC X(40).                 \n016342         10  OLD-TDAC-N3-MODIFIED      PIC X(01).                 \n016344         10  OLD-TDAC-N3-PRINT-CD      PIC X(01).                 \n016346         10  OLD-TDAC-NAME-AREA-3.                                \n016348             15  OLD-TDAC-N3-KEY       PIC X(14).                 \n016350             15  OLD-TDAC-N3-FIRST     PIC X(40).                 \n016352             15  OLD-TDAC-N3-MID       PIC X(20).                 \n016354             15  OLD-TDAC-N3-LAST      PIC X(40).                 \n016356             15  OLD-TDAC-N3-PREFIX    PIC X(12).                 \n016358             15  OLD-TDAC-N3-SUFFIX    PIC X(12).                 \n016360             15  OLD-TDAC-N3-FAMILIAR  PIC X(20).                 \n016362             15  OLD-TDAC-N3-PRT-PFX   PIC X(01).                 \n016364             15  OLD-TDAC-N3-PRT-SFX   PIC X(01).                 \n016366             15  OLD-TDAC-N3-DESIGNAT  PIC X(20).                 \n016368         10  OLD-TDAC-ADDR-KEY         PIC X(28).                 \n016370         10  OLD-TDAC-ADDR-1           PIC X(40).                 \n016372         10  OLD-TDAC-ADDR-2           PIC X(40).                 \n016374         10  OLD-TDAC-CITY             PIC X(40).                 \n016376         10  OLD-TDAC-STATE            PIC X(2).                  \n016378         10  OLD-TDAC-PROVINCE         PIC X(2).                  \n016380         10  OLD-TDAC-COUNTRY          PIC X(2).                  \n016382         10  OLD-TDAC-ZIP-CODE.                                   \n016384             15  OLD-TDAC-ZIP          PIC 9(5).                  \n016386             15  OLD-TDAC-ZIP-4        PIC 9(4).                  \n016388         10  OLD-TDAC-LONGITUDE        PIC S9(3)V9(6).            \n016390         10  OLD-TDAC-LATITUDE         PIC S9(3)V9(6).            \n016392         10  OLD-TDAC-MAIL-CD          PIC 9(1).                  \n016394         10  OLD-TDAC-TICKLER-FLAG     PIC 9.                     \n016396         10  OLD-TDAC-RESIDENT-CD      PIC 9.                     \n016398         10  OLD-TDAC-ALIEN-CD         PIC 9(1).                  \n016400         10  OLD-TDAC-SHT-NAME         PIC X(20).                 \n016402         10  OLD-TDAC-BAR-CD           PIC 9(3).                  \n016404         10  OLD-TDAC-PHONE-1          PIC 9(10).                 \n016406         10  OLD-TDAC-PHONE-2          PIC 9(10).                 \n016408         10  OLD-TDAC-TIN-CD           PIC X(1).                  \n016410         10  OLD-TDAC-TIN-CERT-CD      PIC 9(1).                  \n016412         10  OLD-TDAC-TIN-CERT-DT      PIC 9(8).                  \n016414         10  OLD-TDAC-TIN-NBR          PIC 9(9).                  \n016416         10  OLD-TDAC-OFFICER          PIC X(3).                  \n016418         10  OLD-TDAC-EMP-CD           PIC X(1).                  \n016420         10  OLD-TDAC-FREE-MARK        PIC X(24).                 \n016422         10  OLD-TDAC-INQ-SECR-CD      PIC 9(1).                  \n016424         10  OLD-TDAC-PRIVACY          PIC 9(1).                  \n016426         10  OLD-TDAC-BK-DEF-CD1       PIC X(1).                  \n016428         10  OLD-TDAC-BK-DEF-CD2       PIC X(1).                  \n016430         10  OLD-TDAC-BK-DEF-CD3       PIC X(1).                  \n016432         10  OLD-TDAC-BK-DEF-CD4       PIC X(1).                  \n016434         10  OLD-TDAC-BK-DEF-CD5       PIC X(1).                  \n016436         10  OLD-TDAC-EMPLOYEE-ID      PIC X(8).                  \n016438         10  OLD-TDAC-EMAIL-ADDR       PIC X(100).                \n016440         10  OLD-TDAC-EMAIL-ADDR-R REDEFINES OLD-TDAC-EMAIL-ADDR. \n016442             15  OLD-TDAC-EMAIL-ADDR-1-30  PIC X(30).             \n016444             15  OLD-TDAC-EMAIL-ADDR-31-60 PIC X(30).             \n016446             15  OLD-TDAC-EMAIL-ADDR-61-90 PIC X(30).             \n016448             15  OLD-TDAC-EMAIL-ADDR-91-100                       \n016450                                           PIC X(10).             \n016452         10 OLD-TDAC-EMAIL-ADDR-RR                                \n016454                                   REDEFINES OLD-TDAC-EMAIL-ADDR. \n016456             15  OLD-TDAC-EMAIL-ADDR-1-50  PIC X(50).             \n016458             15  OLD-TDAC-EMAIL-ADDR-51-100 PIC X(50).            \n016460         10  OLD-TDAC-EMAIL-PSSWRD     PIC X(12).                 \n016462         10  OLD-TDAC-GENDER           PIC X(1).                  \n016464         10  OLD-TDAC-NEW-CUST         PIC 9(1).                  \n016466         10  OLD-TDAC-OPEN-DT          PIC 9(8).                  \n016468         10  OLD-TDAC-LUPD-DATE        PIC 9(8).                  \n016470         10  OLD-TDAC-LUPD-TIME        PIC 9(8).                  \n016472         10  OLD-TDAC-LST-CONTACT      PIC 9(8).                  \n016474         10  OLD-TDAC-BIRTH-DT         PIC 9(8).                  \n016476         10  OLD-TDAC-BIRTH-DT-2       PIC 9(8).                  \n016478         10  OLD-TDAC-BIRTH-DT-3       PIC 9(8).                  \n016480         10  OLD-TDAC-DEATH-DT         PIC 9(8).                  \n016482         10  OLD-TDAC-ADD-DT           PIC 9(8).                  \n016484         10  OLD-TDAC-ADD-TM           PIC 9(6).                  \n016486         10  OLD-TDAC-ROTH-DATE        PIC 9(8).                  \n016488         10  OLD-TDAC-CD-BAL           PIC S9(15)V9(2).           \n016490         10  OLD-TDAC-CD-BAL-BYR       PIC S9(15)V9(2).           \n016492         10  OLD-TDAC-CD-PENLTY        PIC S9(15)V9(2).           \n016494         10  OLD-TDAC-CD-WTHLD         PIC S9(15)V9(2).           \n016496         10  OLD-TDAC-CD-INT           PIC S9(15)V9(2).           \n016498         10  OLD-TDAC-CD-OID-INT       PIC S9(15)V9(2).           \n016500         10  OLD-TDAC-IRA-BAL          PIC S9(15)V9(2).           \n016502         10  OLD-TDAC-IRA-BAL-BYR      PIC S9(15)V9(2).           \n016504         10  OLD-TDAC-IRA-PENLTY       PIC S9(15)V9(2).           \n016506         10  OLD-TDAC-IRA-WTHLD        PIC S9(15)V9(2).           \n016508         10  OLD-TDAC-IRA-INT          PIC S9(15)V9(2).           \n016510         10  OLD-TDAC-IRA-CONTR        PIC S9(15)V9(2).           \n016512         10  OLD-TDAC-IRA-CONTR-LY     PIC S9(15)V9(2).           \n016514         10  OLD-TDAC-IRA-DISTR        PIC S9(15)V9(2).           \n016516         10  OLD-TDAC-IRA-DISTR-LY     PIC S9(15)V9(2).           \n016518         10  OLD-TDAC-IRA-ROLLOVER     PIC S9(15)V9(2).           \n016520         10  OLD-TDAC-IRA-TRF-IN       PIC S9(15)V9(2).           \n016522         10  OLD-TDAC-IRA-TRF-OUT      PIC S9(15)V9(2).           \n016524         10  OLD-TDAC-IRA-FAIR-MKT     PIC S9(15)V9(2).           \n016526         10  OLD-TDAC-CIF-REMARK       PIC X.                     \n016528         10  OLD-TDAC-CD-ST-WHLD       PIC S9(15)V9(2).           \n016530         10  OLD-TDAC-IRA-ST-WHLD      PIC S9(15)V9(2).           \n016532         10  OLD-TDAC-CURR-YR-AMT      PIC S9(15)V9(2)            \n016534                                           OCCURS 12 TIMES.       \n016536         10  OLD-TDAC-LAST-YR-AMT      PIC S9(15)V9(2)            \n016538                                           OCCURS 12 TIMES.       \n016540         10  OLD-TDAC-TIN-CD-2         PIC X(01).                 \n016542         10  OLD-TDAC-TIN-CRT-CD-2     PIC 9(01).                 \n016544         10  OLD-TDAC-TIN-CRT-DT-2     PIC 9(08).                 \n016546         10  OLD-TDAC-TIN-NBR-2        PIC 9(09).                 \n016548         10  OLD-TDAC-TIN-CD-3         PIC X(01).                 \n016550         10  OLD-TDAC-TIN-CRT-CD-3     PIC 9(01).                 \n016552         10  OLD-TDAC-TIN-CRT-DT-3     PIC 9(08).                 \n016554         10  OLD-TDAC-TIN-NBR-3        PIC 9(09).                 \n016556         10  OLD-TDAC-NAICS-CD         PIC 9(06).                 \n016558         10  OLD-TDAC-CIF-PASS-THR     PIC 9(01).                 \n016560         10  OLD-TDAC-EMAIL-NTC        PIC 9(01).                 \n016562         10  OLD-TDAC-RMD-YR-AMT       PIC S9(15)V9(2).           \n016564         10  OLD-TDAC-ADDR-CHG-DT      PIC 9(08).                 \n016566         10  OLD-TDAC-WTHLD-CD         PIC 9(01).                 \n016568         10  OLD-TDAC-ST-WHLD-CD       PIC 9(01).                 \n016570         10  OLD-TDAC-WTHLD-AMT        PIC S9(12)V9(2).           \n016572         10  OLD-TDAC-ST-WHLD-AMT      PIC S9(12)V9(2).           \n016574         10  OLD-TDAC-FOREIGN-LANG     PIC X(01).                 \n016576         10  OLD-TDAC-L-ROLLOVR-DT     PIC 9(08).                 \n016578         10  OLD-TDAC-CUSTM-FIELDS     PIC 9(01).                 \n016580         10  OLD-TDAC-LLC-NAME         PIC X(40).                 \n016582         10  OLD-TDAC-LLC-TIN-CD       PIC X(01).                 \n016584         10  OLD-TDAC-LLC-TIN          PIC 9(09).                 \n016586         10  OLD-TDAC-FOREIGN-PHN      PIC X(20).                 \n016588                                                                  \n016590     05  OLD-TDAACCT-DATA              PIC X(2400).               \n016592     05  OLD-TDAACCT.                                             \n016594         10  OLD-TDAA-G-KEY.                                      \n016596             15  OLD-TDAA-BANK           PIC 9(4).                \n016598             15  OLD-TDAA-BRCH           PIC 9(4).                \n016600             15  OLD-TDAA-APPL           PIC 9(1).                \n016602             15  OLD-TDAA-CUST           PIC 9(12).               \n016604             15  OLD-TDAA-ACCT           PIC 9(10).               \n016606         10  OLD-TDAA-G-DATA-OPT.                                 \n016608             15  OLD-TDAA-STATUS         PIC X(1).                \n016610             15  OLD-TDAA-IRA-TYPE       PIC 9(2).                \n016612             15  OLD-TDAA-ACCT-OPTION    PIC 9(2).                \n016614             15  OLD-TDAA-DT-CONDENSED   PIC 9(8).                \n016616             15  OLD-TDAA-CERT           PIC 9(7).                \n016618             15  OLD-TDAA-SHT-NAME       PIC X(20).               \n016620             15  OLD-TDAA-TITLE          PIC X(40).               \n016622             15  OLD-TDAA-TITLE-PRINT    PIC X(1).                \n016624             15  OLD-TDAA-ADDR-USAGE     PIC X(01).               \n016626             15  OLD-TDAA-ADDR-ALT       PIC X(01).               \n016628             15  OLD-TDAA-ADDR-TEMP      PIC X(01).               \n016630             15  OLD-TDAA-TEMP-BEG-DT    PIC 9(04).               \n016632             15  OLD-TDAA-TEMP-END-DT    PIC 9(04).               \n016634             15  OLD-TDAA-TEMP-EFF-DT    PIC 9(08).               \n016636             15  OLD-TDAA-TEMP-EXP-DT    PIC 9(08).               \n016638             15  OLD-TDAA-END-OF-INT     PIC 9(1).                \n016640             15  OLD-TDAA-END-OF-MAT     PIC 9(1).                \n016642             15  OLD-TDAA-END-OF-STMT    PIC 9(1).                \n016644             15  OLD-TDAA-END-OF-CMPD    PIC 9(1).                \n016646             15  OLD-TDAA-END-OF-FEE     PIC 9(1).                \n016648             15  OLD-TDAA-OFFICER        PIC X(3).                \n016650             15  OLD-TDAA-OFFICER-2      PIC X(3).                \n016652             15  OLD-TDAA-OFFICER-3      PIC X(3).                \n016654             15  OLD-TDAA-FREE-MARK      PIC X(24).               \n016656             15  OLD-TDAA-CLASS-CD       PIC X(1).                \n016658             15  OLD-TDAA-CORR-BK-CD     PIC X(1).                \n016660             15  OLD-TDAA-PUBLIC-FUND    PIC X(1).                \n016662             15  OLD-TDAA-TRUST-CD       PIC X(1).                \n016664             15  OLD-TDAA-RT-CHG-ALLOW   PIC 9(1).                \n016666             15  OLD-TDAA-WTHDRW-ALLOW   PIC 9(1).                \n016668             15  OLD-TDAA-DPOSIT-ALLOW   PIC 9(1).                \n016670             15  OLD-TDAA-POST-MAT       PIC 9(1).                \n016672             15  OLD-TDAA-RT-FLOOR       PIC 9(1).                \n016674             15  OLD-TDAA-REPO-CD        PIC 9(1).                \n016676             15  OLD-TDAA-TOTAL-CD       PIC 9(3).                \n016678             15  OLD-TDAA-REN-TOTAL-CD   PIC 9(3).                \n016680             15  OLD-TDAA-ORG-TOTAL-CD   PIC 9(3).                \n016682             15  OLD-TDAA-INQ-SECR-CD    PIC 9(1).                \n016684             15  OLD-TDAA-MAIL-CD        PIC 9(1).                \n016686             15  OLD-TDAA-WTHD-REQD-CD   PIC 9(1).                \n016688             15  OLD-TDAA-TICKLER-FLAG   PIC 9.                   \n016690             15  OLD-TDAA-DISP-CD        PIC 9(1).                \n016692             15  OLD-TDAA-CLS-DISP-CD    PIC 9(1).                \n016694             15  OLD-TDAA-DIST-STATUS    PIC 9(1).                \n016696             15  OLD-TDAA-COMM-ACCT      PIC 9(1).                \n016698             15  OLD-TDAA-RENEW-CD       PIC 9(1).                \n016700             15  OLD-TDAA-PLEDGE-CD      PIC X(1).                \n016702             15  OLD-TDAA-NEGOT-CD       PIC X(1).                \n016704             15  OLD-TDAA-BENEF-CD       PIC 9(1).                \n016706             15  OLD-TDAA-COMM-MAT-CD    PIC 9(1).                \n016708             15  OLD-TDAA-NBR-BENEF      PIC 9(1).                \n016710             15  OLD-TDAA-OVERRIDE       PIC 9(1).                \n016712             15  OLD-TDAA-INT-CD         PIC 9(1).                \n016714             15  OLD-TDAA-WTHLD-CD       PIC 9(1).                \n016716             15  OLD-TDAA-WTHLD-AMT      PIC S9(12)V9(2).         \n016718             15  OLD-TDAA-IGL-GRP        PIC 9(2).                \n016720             15  OLD-TDAA-SUM-STMT-CD    PIC 9(1).                \n016722             15  OLD-TDAA-REN-NTC-CD     PIC 9(1).                \n016724             15  OLD-TDAA-PMAT-NTC-CD    PIC 9(1).                \n016726             15  OLD-TDAA-RTCHG-NTC-CD   PIC 9(1).                \n016728             15  OLD-TDAA-INT-NTC-CD     PIC 9(1).                \n016730             15  OLD-TDAA-CHG-NTC        PIC 9(1).                \n016732             15  OLD-TDAA-YIELD-NUM      PIC 9(3).                \n016734             15  OLD-TDAA-YIELD-DENOM    PIC 9(3).                \n016736             15  OLD-TDAA-CMPD-FREQ      PIC 9(1).                \n016738             15  OLD-TDAA-CMPD-NTRVL     PIC 9(4).                \n016740             15  OLD-TDAA-RT-CHG-LIMIT   PIC 9(1).                \n016742             15  OLD-TDAA-VAR-RT-IMMED   PIC 9(1).                \n016744             15  OLD-TDAA-VAR-RT-INT     PIC 9(1).                \n016746             15  OLD-TDAA-VAR-RT-SCHED   PIC 9(1).                \n016748             15  OLD-TDAA-VAR-RT-CUST    PIC 9(1).                \n016750             15  OLD-TDAA-VAR-RT-BAL     PIC 9(1).                \n016752             15  OLD-TDAA-RT-INDX-CD     PIC 9(2).                \n016754             15  OLD-TDAA-R-RT-INDX-CD   PIC XX.                  \n016756             15  OLD-TDAA-RT-MARG-CD     PIC 9(2).                \n016758             15  OLD-TDAA-R-RT-MARG-CD   PIC XX.                  \n016760             15  OLD-TDAA-RT-TIER-CD     PIC 9(2).                \n016762             15  OLD-TDAA-R-RT-TIER-CD   PIC XX.                  \n016764             15  OLD-TDAA-RT-SR-CD       PIC 9(2).                \n016766             15  OLD-TDAA-R-RT-SR-CD     PIC XX.                  \n016768             15  OLD-TDAA-RT-REGN-CD     PIC 9(2).                \n016770             15  OLD-TDAA-RT-CHG-NTRVL   PIC 9(3).                \n016772             15  OLD-TDAA-CAP-RT-CHG     PIC X.                   \n016774             15  OLD-TDAA-R-TIER-RT-CH   PIC X.                   \n016776             15  OLD-TDAA-ALERT-CD       PIC 9(2).                \n016778             15  OLD-TDAA-ALERT-CD-2     PIC 9(2).                \n016780             15  OLD-TDAA-ALERT-CD-3     PIC 9(2).                \n016782             15  OLD-TDAA-CENSUS-TRACT   PIC 9(4)V9(2).           \n016784             15  OLD-TDAA-MK-SEGMENT     PIC X(2).                \n016786             15  OLD-TDAA-BK-DEF-TOT     PIC X(3).                \n016788             15  OLD-TDAA-BK-DEF-CD1     PIC X(1).                \n016790             15  OLD-TDAA-BK-DEF-CD2     PIC X(1).                \n016792             15  OLD-TDAA-BK-DEF-CD3     PIC X(1).                \n016794             15  OLD-TDAA-BK-DEF-CD4     PIC X(1).                \n016796             15  OLD-TDAA-BK-DEF-CD5     PIC X(1).                \n016798             15  OLD-TDAA-OID-METH       PIC 9(1).                \n016800             15  OLD-TDAA-EOY-CD         PIC 9(1).                \n016802             15  OLD-TDAA-B-NOTC-YR1     PIC 9(1).                \n016804             15  OLD-TDAA-B-NOTC-YR2     PIC 9(1).                \n016806             15  OLD-TDAA-B-NOTC-YR3     PIC 9(1).                \n016808             15  OLD-TDAA-NO-COMB-IRS    PIC 9(1).                \n016810             15  OLD-TDAA-PENLTY-CD      PIC 999.                 \n016812             15  OLD-TDAA-MONEY-SRC-CD   PIC X(1).                \n016814             15  OLD-TDAA-INTERNET-CD.                            \n016816                 20  OLD-TDAA-INTERNET-BPY   PIC 9(1).            \n016818                 20  OLD-TDAA-INTERNET-TFR   PIC 9(1).            \n016820                 20  OLD-TDAA-INTERNET-INQ   PIC 9(1).            \n016822             15  OLD-TDAA-IRA-BACKED     PIC 9(1).                \n016824             15  OLD-TDAA-SAV-DEPOSIT    PIC 9(1).                \n016826             15  OLD-TDAA-MAT-TYPE       PIC 9(1).                \n016828             15  OLD-TDAA-MAT-TERM       PIC 9(4).                \n016830             15  OLD-TDAA-ORG-MAT-TYPE   PIC 9(1).                \n016832             15  OLD-TDAA-ORG-MAT-TERM   PIC 9(4).                \n016834             15  OLD-TDAA-ODD-PAYMENT    PIC 9(1).                \n016836             15  OLD-TDAA-PAY-FREQ       PIC 9(1).                \n016838             15  OLD-TDAA-PAY-NTRVL      PIC 9(4).                \n016840             15  OLD-TDAA-FEE-FREQ       PIC 9(1).                \n016842             15  OLD-TDAA-FEE-NTRVL      PIC 9(4).                \n016844             15  OLD-TDAA-STMT-FREQ      PIC 9(1).                \n016846             15  OLD-TDAA-STMT-NTRVL     PIC 9(4).                \n016848             15  OLD-TDAA-EMPLOYEE-ID    PIC X(8).                \n016850             15  OLD-TDAA-EFT-CARD       PIC X(1).                \n016852             15  OLD-TDAA-PEN-WAV-RESN   PIC X(1).                \n016854             15  OLD-TDAA-CLOSED-RESN    PIC X(1).                \n016856             15  OLD-TDAA-SPECIAL-STMT   PIC 9(1).                \n016858             15  OLD-TDAA-CLS-THIS-MTH   PIC 9(1).                \n016860             15  OLD-TDAA-RC-MAT-ONLY    PIC 9(1).                \n016862             15  OLD-TDAA-GRACE-DAYS     PIC 9(2).                \n016864             15  OLD-TDAA-CLS-ON-MAT     PIC 9(1).                \n016866         10  OLD-TDAA-G-ACCT-NBR.                                 \n016868             15  OLD-TDAA-DDA-ACCT-1     PIC 9(12).               \n016870             15  OLD-TDAA-DDA-ACCT-1-S   PIC 9(10).               \n016872             15  OLD-TDAA-DDA-ACCT-2     PIC 9(12).               \n016874             15  OLD-TDAA-DDA-ACCT-2-S   PIC 9(10).               \n016876             15  OLD-TDAA-DDA-ACCT-3     PIC 9(12).               \n016878             15  OLD-TDAA-DDA-ACCT-3-S   PIC 9(10).               \n016880             15  OLD-TDAA-INT-ACCT       PIC 9(12).               \n016882             15  OLD-TDAA-INT-ACCT-S     PIC 9(10).               \n016884             15  OLD-TDAA-CS-ACCT        PIC 9(12).               \n016886             15  OLD-TDAA-CS-ACCT-S      PIC 9(10).               \n016888             15  OLD-TDAA-CC-ACCT        PIC 9(12).               \n016890             15  OLD-TDAA-LNS-BORROWER   PIC 9(12).               \n016892             15  OLD-TDAA-LNS-NOTE       PIC 9(10).               \n016894             15  OLD-TDAA-CNV-OLD-ACCT   PIC X(15).               \n016896             15  OLD-TDAA-CLS-ACCT       PIC 9(12).               \n016898             15  OLD-TDAA-CLS-ACCT-S     PIC 9(10).               \n016900         10  OLD-TDAA-G-CNTR.                                     \n016902             15  OLD-TDAA-DAYS-IN-PER    PIC 9(5).                \n016904             15  OLD-TDAA-RR-CYC-NBR     PIC 9(2).                \n016906             15  OLD-TDAA-CR-CNT-STD     PIC 9(5).                \n016908             15  OLD-TDAA-CR-AMT-STD     PIC S9(12)V9(2).         \n016910             15  OLD-TDAA-DB-CNT-STD     PIC 9(5).                \n016912             15  OLD-TDAA-DB-AMT-STD     PIC S9(12)V9(2).         \n016914             15  OLD-TDAA-CR-CNT-YTD     PIC 9(5).                \n016916             15  OLD-TDAA-CR-AMT-YTD     PIC S9(12)V9(2).         \n016918             15  OLD-TDAA-DB-CNT-YTD     PIC 9(5).                \n016920             15  OLD-TDAA-DB-AMT-YTD     PIC S9(12)V9(2).         \n016922             15  OLD-TDAA-DAYS-IN-TERM   PIC 9(5).                \n016924         10  OLD-TDAA-G-AMT.                                      \n016926             15  OLD-TDAA-BEG-INT-BAL    PIC S9(12)V9(2).         \n016928             15  OLD-TDAA-PURCH-AMT      PIC S9(12)V9(2).         \n016930             15  OLD-TDAA-CURR-BAL       PIC S9(12)V9(2).         \n016932             15  OLD-TDAA-AVAIL-BAL      PIC S9(12)V9(2).         \n016934             15  OLD-TDAA-BAL-BEG-MAT    PIC S9(12)V9(2).         \n016936             15  OLD-TDAA-CLOSE-AMT      PIC S9(12)V9(2).         \n016938             15  OLD-TDAA-MONEY-AMT      PIC S9(12)V9(2).         \n016940             15  OLD-TDAA-BAL-BEG-STMT   PIC S9(12)V9(2).         \n016942             15  OLD-TDAA-ACCR-INT       PIC S9(12)V9(6).         \n016944             15  OLD-TDAA-ANTIC-INT      PIC S9(12)V9(2).         \n016946             15  OLD-TDAA-INT-TO-POST    PIC S9(12)V9(2).         \n016948             15  OLD-TDAA-1099-YTD       PIC S9(12)V9(2).         \n016950             15  OLD-TDAA-1099-LST-YR    PIC S9(12)V9(2).         \n016952             15  OLD-TDAA-CURR-PENLTY    PIC S9(12)V9(2).         \n016954             15  OLD-TDAA-PENLTY-STD     PIC S9(12)V9(2).         \n016956             15  OLD-TDAA-PENLTY-YTD     PIC S9(12)V9(2).         \n016958             15  OLD-TDAA-LST-PENLTY     PIC S9(12)V9(2).         \n016960             15  OLD-TDAA-CURR-INT-ADJ   PIC S9(12)V9(2).         \n016962             15  OLD-TDAA-TOTAMT-HOLDS   PIC S9(12)V9(2).         \n016964             15  OLD-TDAA-NXT-INT-ADJ    PIC S9(12)V9(2).         \n016966             15  OLD-TDAA-FEE-AMT        PIC S9(12)V9(2).         \n016968             15  OLD-TDAA-OID-RPT-INT    PIC S9(12)V9(2).         \n016970             15  OLD-TDAA-FAIR-MRKT      PIC S9(12)V9(2).         \n016972             15  OLD-TDAA-CUR-WHLD-AMT   PIC S9(12)V9(2).         \n016974             15  OLD-TDAA-LST-WHLD-AMT   PIC S9(12)V9(2).         \n016976             15  OLD-TDAA-WTHLD-STD      PIC S9(12)V9(2).         \n016978             15  OLD-TDAA-WTHLD-YTD      PIC S9(12)V9(2).         \n016980             15  OLD-TDAA-LST-INT-PMT    PIC S9(12)V9(2).         \n016982             15  OLD-TDAA-BAL-BEG-YR     PIC S9(12)V9(2).         \n016984             15  OLD-TDAA-BAL-AT-CONV    PIC S9(12)V9(2).         \n016986             15  OLD-TDAA-BAL-BEG-LYR    PIC S9(12)V9(2).         \n016988             15  OLD-TDAA-MIN-BAL-STD    PIC S9(12)V9(2).         \n016990             15  OLD-TDAA-MIN-BAL-YTD    PIC S9(12)V9(2).         \n016992             15  OLD-TDAA-MAX-BAL-YTD    PIC S9(12)V9(2).         \n016994             15  OLD-TDAA-LMINBAL-STD    PIC S9(12)V9(2).         \n016996             15  OLD-TDAA-CMPD-INT       PIC S9(12)V9(2).         \n016998             15  OLD-TDAA-PER-DIEM       PIC S9(12)V9(6).         \n017000             15  OLD-TDAA-AVG-PER-DIEM   PIC S9(12)V9(6).         \n017002             15  OLD-TDAA-EMAIL-MAXAMT   PIC 9(10).               \n017004             15  OLD-TDAA-EMAIL-MINAMT   PIC 9(10).               \n017006             15  OLD-TDAA-DTH-FAIRMKT    PIC S9(12)V9(2).         \n017008             15  OLD-TDAA-PENLTY-WAIVE   PIC S9(12)V9(2).         \n017010         10  OLD-TDAA-G-RATES.                                    \n017012             15  OLD-TDAA-BEG-INT-RT     PIC 9(2)V9(3).           \n017014             15  OLD-TDAA-CUR-INT-RT     PIC 9(2)V9(3).           \n017016             15  OLD-TDAA-FLOOR-RT       PIC 9(2)V9(3).           \n017018             15  OLD-TDAA-FLOOR-INCR     PIC 9(2)V9(3).           \n017020             15  OLD-TDAA-YIELD-RT       PIC 9(2)V9(3).           \n017022             15  OLD-TDAA-RISE-RATE      PIC 9(2)V9(3)            \n017024                               OCCURS 10.                         \n017026             15  OLD-TDAA-LNS-INCRMNT    PIC 9(2)V9(4).           \n017028             15  OLD-TDAA-RT-VARIANCE    PIC S9(1)V9(2).          \n017030             15  OLD-TDAA-CONST-RT-ADJ   PIC S9(2)V9(3).          \n017032             15  OLD-TDAA-RATE-AT-EOY    PIC 9(2)V9(3).           \n017034             15  OLD-TDAA-RATE-LST-STM   PIC 9(2)V9(3).           \n017036             15  OLD-TDAA-ORG-YIELD-RT   PIC 9(2)V9(3).           \n017038             15  OLD-TDAA-REN-YIELD-RT   PIC 9(2)V9(3).           \n017040         10  OLD-TDAA-G-DATES.                                    \n017042             15  OLD-TDAA-SCHED-DT       PIC 9(8).                \n017044             15  OLD-TDAA-ACCR-DT        PIC 9(8).                \n017046             15  OLD-TDAA-OPEN-DT        PIC 9(8).                \n017048             15  OLD-TDAA-CLSD-DT        PIC 9(8).                \n017050             15  OLD-TDAA-LST-MAT-DT     PIC 9(8).                \n017052             15  OLD-TDAA-LST-POST-DT    PIC 9(8).                \n017054             15  OLD-TDAA-LST-IN-PROC    PIC 9(8).                \n017056             15  OLD-TDAA-LST-CONTACT    PIC 9(8).                \n017058             15  OLD-TDAA-LST-FEE-DT     PIC 9(8).                \n017060             15  OLD-TDAA-LST-RTCHG-DT   PIC 9(8).                \n017062             15  OLD-TDAA-LST-DIST-DT    PIC 9(8).                \n017064             15  OLD-TDAA-LST-STMT-DT    PIC 9(8).                \n017066             15  OLD-TDAA-LST-CMPD-DT    PIC 9(8).                \n017068             15  OLD-TDAA-RR-CYC-DT      PIC 9(8)                 \n017070                               OCCURS 10.                         \n017072             15  OLD-TDAA-BNF-BIRTH-DT   PIC 9(8).                \n017074             15  OLD-TDAA-BNF-DEATH-DT   PIC 9(8).                \n017076             15  OLD-TDAA-LUPD-DATE      PIC 9(8).                \n017078             15  OLD-TDAA-LUPD-TIME      PIC 9(6).                \n017080             15  OLD-TDAA-ADD-DT         PIC 9(8).                \n017082             15  OLD-TDAA-ADD-TM         PIC 9(6).                \n017084             15  OLD-TDAA-CONV-DT        PIC 9(8).                \n017086             15  OLD-TDAA-ACT-CLOSE-DT   PIC 9(8).                \n017088             15  OLD-TDAA-LST-TBACT-DT   PIC 9(8).                \n017090             15  OLD-TDAA-ALERT-EXP-DT   PIC 9(8).                \n017092             15  OLD-TDAA-ALRT2-EXP-DT   PIC 9(8).                \n017094             15  OLD-TDAA-ALRT3-EXP-DT   PIC 9(8).                \n017096             15  OLD-TDAA-NXT-FEE-DT     PIC 9(8).                \n017098             15  OLD-TDAA-NXT-POST-DT    PIC 9(8).                \n017100             15  OLD-TDAA-NXT-MAT-DT     PIC 9(8).                \n017102             15  OLD-TDAA-NXT-DIST-DT    PIC 9(8).                \n017104             15  OLD-TDAA-NXT-RT-CHG     PIC 9(8).                \n017106             15  OLD-TDAA-NXT-IN-PROC    PIC 9(8).                \n017108             15  OLD-TDAA-NXT-CMPD-DT    PIC 9(8).                \n017110             15  OLD-TDAA-NXT-STMT-DT    PIC 9(8).                \n017112             15  OLD-TDAA-NXT-DS-PROC    PIC 9(8).                \n017114             15  OLD-TDAA-ADV-NTC-DT     PIC 9(8).                \n017116             15  OLD-TDAA-NXT-29YR-DT    PIC 9(8).                \n017118             15  OLD-TDAA-FAIR-MRKT-DT   PIC 9(8).                \n017120             15  OLD-TDAA-SORT-FIELD-1   PIC X(36).               \n017122             15  OLD-TDAA-SORT-FIELD-2   PIC X(36).               \n017124             15  OLD-TDAA-SORT-FIELD-3   PIC X(36).               \n017126             15  OLD-TDAA-SORT-FIELD-4   PIC X(36).               \n017128         10  OLD-TDAA-CMAT-PUB-ID        PIC X(8).                \n017130         10  OLD-TDAA-MSA-CONTR          PIC 9.                   \n017132         10  OLD-TDAA-MSA-CONTR-LY       PIC 9.                   \n017134         10  OLD-TDAA-AVG-ACCR-INT       PIC S9(12)V9(6).         \n017136         10  OLD-TDAA-LEVEL-PAY          PIC 9.                   \n017138         10  OLD-TDAA-ST-INT-CD          PIC 9.                   \n017140         10  OLD-TDAA-ST-WHLD-CD         PIC 9.                   \n017142         10  OLD-TDAA-ST-WHLD-AMT        PIC S9(12)V99.           \n017144         10  OLD-TDAA-ST-CUR-W-AMT       PIC S9(12)V99.           \n017146         10  OLD-TDAA-ST-LST-W-AMT       PIC S9(12)V99.           \n017148         10  OLD-TDAA-ST-WHLD-STD        PIC S9(12)V99.           \n017150         10  OLD-TDAA-ST-WHLD-YTD        PIC S9(12)V99.           \n017152         10  OLD-TDAA-CIF-REMARK         PIC X.                   \n017154         10  OLD-TDAA-CSR                PIC X(3).                \n017156         10  OLD-TDAA-BSA-O-RSK-CD       PIC 9(1).                \n017158         10  OLD-TDAA-BSA-C-RSK-CD       PIC 9(1).                \n017160         10  OLD-TDAA-LRG-TRX-DT         PIC 9(8).                \n017162         10  OLD-TDAA-HSA-FMLY-IND       PIC 9(01).               \n017164         10  OLD-TDAA-STOP-PAY-IND       PIC 9(01).               \n017166         10  OLD-TDAA-IMG-PG-TYPE        PIC X(01).               \n017168         10  OLD-TDAA-CONT-LMT-CLC       PIC 9(5)V99.             \n017170         10  OLD-TDAA-CONT-LMT-ENT       PIC 9(5)V99.             \n017172         10  OLD-TDAA-MEMO-DB            PIC S9(12)V99.           \n017174         10  OLD-TDAA-MEMO-CR            PIC S9(12)V99.           \n017176         10  OLD-TDAA-MEMO-DB-2          PIC S9(12)V99.           \n017178         10  OLD-TDAA-MEMO-CR-2          PIC S9(12)V99.           \n017180         10  OLD-TDAA-RT-AT-CONV         PIC 9(2)V9(3).           \n017182         10  OLD-TDAA-ACCR-AT-CONV       PIC S9(12)V9(6).         \n017184         10  OLD-TDAA-RT-AT-ACRDT        PIC 9(2)V9(3).           \n017186         10  OLD-TDAA-BAL-AT-ACRDT       PIC S9(12)V9(2).         \n017188         10  OLD-TDAA-ZERO-RT-ALLOW      PIC 9.                   \n017190         10  OLD-TDAA-EMAIL-NTC          PIC 9.                   \n017192         10  OLD-TDAA-EMAIL-STMT         PIC 9.                   \n017194         10  OLD-TDAA-FRAUD-CK-DT        PIC 9(8).                \n017196         10  OLD-TDAA-FRAUD-CK-CNT       PIC 9(3).                \n017198         10  OLD-TDAA-FRAUD-CK-AMT       PIC S9(12)V9(2).         \n017200         10  OLD-TDAA-MISC-ACCTNO        PIC 9(8).                \n017202         10  OLD-TDAA-RMD-MAN-CALC       PIC 9(1).                \n017204         10  OLD-TDAA-RMD-AMOUNT         PIC S9(12)V9(2).         \n017206         10  OLD-TDAA-BROKERAGE-ID       PIC X(10).               \n017208         10  OLD-TDAA-MONY-SRC-CD2       PIC X(03).               \n017210         10  OLD-TDAA-INHERIT-IRA        PIC 9(01).               \n017212         10  OLD-TDAA-LIFE-FACTOR        PIC 9(02)V9(1).          \n017214         10  OLD-TDAA-EV-LARGE-TRX       PIC X(01).               \n017216         10  OLD-TDAA-EV-MAT-AMT         PIC S9(12)V9(2).         \n017218         10  OLD-TDAA-EV-DISP-ACCT       PIC 9(22).               \n017220         10  OLD-TDAA-EV-COMP-ACCT       PIC 9(22).               \n017222         10  OLD-TDAA-EV-PUBLIC-ID       PIC X(08).               \n017224         10  OLD-TDAA-EV-MAT-TYPE        PIC X(01).               \n017226         10  OLD-TDAA-EV-INT-TYPE        PIC X(01).               \n017228         10  OLD-TDAA-EV-ACCT-TYP        PIC X(01).               \n017230         10  OLD-TDAA-EV-WHLD-PCT        PIC 9(02).               \n017232         10  OLD-TDAA-EV-NON-ACCR        PIC X(01).               \n017234         10  OLD-TDAA-EV-CLOSED          PIC X(01).               \n017236         10  OLD-TDAA-EV-CLOSE-MO        PIC X(01).               \n017238         10  OLD-TDAA-EV-OPEN-MO         PIC X(01).               \n017240         10  OLD-TDAA-EV-ANN-INT         PIC S9(12)V9(2).         \n017242         10  OLD-TDAA-EV-ORIG-RT         PIC 9(2)V9(3).           \n017244         10  OLD-TDAA-EV-DLY-INT         PIC S9(12)V9(6).         \n017246         10  OLD-TDAA-EV-INT-PAY         PIC S9(12)V9(6).         \n017248         10  OLD-TDAA-EV-AVAIL-BL        PIC S9(12)V9(2).         \n017250         10  OLD-TDAA-EV-RETAIN          PIC X(01).               \n017252         10  OLD-TDAA-EV-CL-RETAIN       PIC X(01).               \n017254         10  OLD-TDAA-EV-TIMES-REN       PIC 9(05).               \n017256         10  OLD-TDAA-EV-CURR-BAL        PIC S9(12)V9(2).         \n017258         10  OLD-TDAA-BRKR-DEP-CAT       PIC 9(01).               \n017260         10  OLD-TDAA-LINE-OF-BUS        PIC 9(4).                \n017262         10  OLD-TDAA-1ST-STMT           PIC 9(01).               \n017264         10  OLD-TDAA-POSTAL-CITY        PIC X(40).               \n017266         10  OLD-TDAA-POSTAL-CNTRY       PIC X(02).               \n017268         10  OLD-TDAA-CITIZN-CNTRY       PIC X(02).               \n017270         10  OLD-TDAA-CUSTM-FIELDS       PIC 9(01).               \n017272         10  OLD-TDAA-AVG-STEP-RT        PIC 9(2)V9(3).           \n017274         10  OLD-TDAA-MONITOR-INQ        PIC 9(01).               \n017276         10  OLD-TDAA-IGL-GRP-2          PIC 9(02).               \n017278         10  OLD-TDAA-AGG-DAYS-QTD       PIC 9(03).               \n017280         10  OLD-TDAA-AGG-BAL-QTD        PIC S9(15)V9(2).         \n017282         10  OLD-TDAA-IGL-GRP-3          PIC 9(02).               \n017284         10  OLD-TDAA-ALT-ADDR-EOY       PIC 9(01).               \n017286         10  OLD-TDAA-1042S-TAX-ID       PIC X(22).               \n017288         10  OLD-TDAA-LEC                PIC X(01).               \n017290         10  OLD-TDAA-BAL-AT-CLOSE       PIC S9(12)V9(2).         \n017292         10  OLD-TDAA-AVL-CAP-INT        PIC S9(6)V9(2).          \n017294         10  OLD-TDAA-FIDM-TR-FUND       PIC 9(01).               \n017296         10  OLD-TDAA-IRS-FRM-DLVR       PIC 9(01).               \n017298         10  OLD-TDAA-PROVINCE           PIC X(02).               \n017300         10  OLD-TDAA-PROMOTION          PIC X(25).               \n017302         10  OLD-EXTRA-FIELDS.                                    \n017304             15  OLD-TDAA-DAYS-INTO-PER  PIC 9(5).                \n017306             15  OLD-TDAA-CURR-PAYOFF    PIC S9(9)V9(2).          \n017308             15  OLD-TDAA-MANUAL-RT-X    PIC X(5).                \n017310             15  OLD-TDAA-MANUAL-RT-RE   REDEFINES                \n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 619 lines from 8033 to 8651.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 17,
  "total_chunks": 55,
  "start_line": 8033,
  "end_line": 8651,
  "line_count": 619
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
- Source code length: 52084 characters

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
CHUNK 17 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 8033 to 8651 (619 lines)
Chunk Tokens (estimated): ~14,162
Actual Input Tokens: 15,568 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 8033-8651 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 17 of 55 chunks
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
      The source code below is only CHUNK 17 of 55.


=============================================================================
CHUNK 17 SOURCE CODE (Lines 8033-8651)
=============================================================================

```cobol
016074             HOLD-TDAPC-BANK-SPECS.                               
016076             15  HOLD-TDAPC-CREATE-DT      PIC 9(07).             
016078             15  HOLD-TDAPC-CREATE-TM      PIC 9(12).             
016080             15  HOLD-TDAPC-DQVISTA        PIC X.                 
016082             15  HOLD-TDAPC-MSI            PIC X.                 
016084             15  HOLD-TDAPC-BK-TDA-STAT    PIC X.                 
016086             15  HOLD-TDAPC-TDA-PILOT REDEFINES                   
016088                 HOLD-TDAPC-BK-TDA-STAT    PIC X.                 
016090             15  HOLD-TDAPC-BK-STATUS      PIC X.                 
016092             15  HOLD-TDAPC-BR-NO          PIC XX.                
016094             15  HOLD-TDAPC-CSI-BR-CODE REDEFINES                 
016096                 HOLD-TDAPC-BR-NO          PIC XX.                
016098             15  HOLD-TDAPC-BK-PHONE-NUM.                         
016100                 20  HOLD-TDAPC-AREA-CODE  PIC XXX.               
016102                 20  HOLD-TDAPC-PHONE.                            
016104                     25  HOLD-TDAPC-PHONE-1ST-3 PIC XXX.          
016106                     25  HOLD-TDAPC-PHONE-LST-4 PIC X(04).        
016108             15  HOLD-TDAPC-PHN-NUMBER REDEFINES                  
016110                 HOLD-TDAPC-BK-PHONE-NUM   PIC X(10).             
016112             15  HOLD-TDAPC-TDA-ADD-DAY    PIC XXX.               
016114             15  HOLD-TDAPC-HOLIDAYS       OCCURS 18 TIMES.       
016116                 20  HOLD-TDAPC-HOL-MM     PIC XX.                
016118                 20  HOLD-TDAPC-HOL-DD     PIC XX.                
016120             15  HOLD-TDAPC-FM-SUPPRESS    PIC X.                 
016122             15  HOLD-TDAPC-RMT-BK-INDICATOR PIC XX.              
016124             15  HOLD-TDAPC-RMT-IND REDEFINES                     
016126                 HOLD-TDAPC-RMT-BK-INDICATOR PIC XX.              
016128             15  HOLD-TDAPC-BK-ADDR        PIC X(28).             
016130             15  HOLD-TDAPC-BK-ADDR-2      PIC X(27).             
016132             15  HOLD-TDAPC-FED-ID         PIC X(10).             
016134             15  HOLD-TDAPC-EOY-RPT-SEQ    PIC X.                 
016136             15  HOLD-TDAPC-EOY-EARLY-RUN  PIC X.                 
016138             15  HOLD-TDAPC-EOY-RETURN-TO-BK PIC X.               
016140             15  HOLD-TDAPC-EOY-RETURN-TO-BANK REDEFINES          
016142                 HOLD-TDAPC-EOY-RETURN-TO-BK PIC X.               
016144             15  HOLD-TDAPC-EOY-IRA-PHONE    PIC 9(10).           
016146             15  HOLD-TDAPC-EOY-DELETE-DATE  PIC 9(06).           
016148             15  HOLD-TDAPC-EOY-IRA-FICHE  PIC X.                 
016150             15  HOLD-TDAPC-EOY-IRA-PAPER  PIC X.                 
016152             15  HOLD-TDAPC-EOY-IRA-STMT-EARLY PIC X.             
016154             15  HOLD-TDAPC-NO-IRA-STMTS   PIC 9.                 
016156             15  HOLD-TDAPC-EOY-IRA-STMT   PIC X.                 
016158             15  HOLD-TDAPC-EOY-IRA-STMT-PRINT PIC X.             
016160             15  HOLD-TDAPC-EOY-EARLY-DATE PIC 9(06).             
016162             15  HOLD-TDAPC-CK21-TDA       PIC X.                 
016164             15  HOLD-TDAPC-MSI-OV-TDA     PIC X.                 
016166             15  HOLD-TDAPC-BK-IMG-SERV    PIC X(01).             
016168             15  HOLD-TDAPC-EOY-APRIL-DATE PIC 9(06).             
016170             15  HOLD-TDAPC-EOY-COD-CLOSED-RPT  PIC X(01).        
016172             15  HOLD-TDAPC-PRT-NEW        PIC 9(01).             
016174             15  HOLD-TDAPC-IMONITOR       PIC X(01).             
016176             15  HOLD-TDAPC-ENTC-TDA       PIC X.                 
016178             15  HOLD-TDAPC-EV-3RD-PARTY-1 PIC X.                 
016180             15  HOLD-TDAPC-EV-3RD-PARTY-2 PIC X.                 
016182             15  HOLD-TDAPC-HSA-LOCATION   PIC X.                 
016184             15  HOLD-TDAPC-PROFITABILITY  PIC X.                 
016186             15  HOLD-TDAPC-BANCVUE        PIC X.                 
016188             15  HOLD-TDAPC-SPECIAL-DL-BILLING PIC X.             
016190             15  HOLD-TDAPC-CIF-NAME-ADDR  PIC 9.                 
016192             15  HOLD-TDAPC-MAIL-ADDR-LINES PIC X.                
016194             15  HOLD-TDAPC-WEB-ENABLED    PIC X(01).             
016196             15  HOLD-TDAPC-BRANCH-LENGTH  PIC 9.                 
016198             15  HOLD-TDAPC-LOB            PIC 9.                 
016200             15  HOLD-TDAPC-BILL-EDIT-TEMPLATES                   
016202                                           PIC 9.                 
016204             15  HOLD-TDAPC-MCIF-PRIVACY-OPT                      
016206                                           PIC 9.                 
016208             15  HOLD-TDAPC-TRAIN-BK-FLG   PIC X.                 
016210             15  HOLD-TDAPC-EOY-CIB-F-MERD PIC X(01).             
016212             15  FILLER                    PIC X(39).             
016214             15  HOLD-TDAPC-LAST-EOM-PROC  PIC 9(08).             
016216             15  HOLD-TDAPC-BUS-DT-AFT-NX  PIC 9(08).             
016218             15  HOLD-TDAPC-NEXT-BUS-DATE  PIC 9(08).             
016220                                                                  
016222     05  HOLD-TDAMESSAGE.                                         
016224         10  HOLD-TDAM-BANK                PIC 9(04).             
016226         10  HOLD-TDAM-APPL                PIC 9(01).             
016228         10  HOLD-TDAM-CODE-TYPE           PIC 9(01).             
016230         10  HOLD-TDAM-CODE                PIC 9(04).             
016232         10  HOLD-TDAM-RPT-NBR             PIC 9(04).             
016234         10  HOLD-TDAM-TEST-MSG            PIC 9(01).             
016236         10  HOLD-TDAM-MESSAGE-NBR         PIC 9(03).             
016238         10  HOLD-TDAM-MESSAGE-GRP.                               
016240             15  HOLD-TDAM-MESSAGE         PIC X(60)              
016242                                           OCCURS 6 TIMES.        
016244         10  HOLD-TDAM-STOP-DT             PIC 9(08).             
016246         10  HOLD-TDAM-ADD-DT              PIC 9(08).             
016248         10  HOLD-TDAM-ADD-TM              PIC 9(08).             
016250         10  HOLD-TDAM-LUPD-DT             PIC 9(08).             
016252         10  HOLD-TDAM-LUPD-TM             PIC 9(08).             
016254         10  HOLD-TDAM-PUB-ID              PIC X(08).             
016256                                                                  
016258*** PLEASE REMEMBER TO UPDATE THE TDB,AND HOLD FIELDS WHEN        
016260*** UPDATING THE FOLLOWING OLD FIELDS.                            
016262                                                                  
016264**  The old dataset layouts are used to hold the before picture   
016266**  of database records.  They will be used when posting activity 
016268**  by comparing the before and after pictures of the database.   
016270**  This is neccessary because we alter the account record before 
016272**  posting the activity.                                         
016274                                                                  
016276     05  OLD-TDACUST-DATA              PIC X(1967).               
016278     05  OLD-TDACUST.                                             
016280         10  OLD-TDAC-BANK             PIC 9(4).                  
016282         10  OLD-TDAC-CUST             PIC 9(12).                 
016284         10  OLD-TDAC-BRCH             PIC 9(4).                  
016286         10  OLD-TDAC-STATUS           PIC X(1).                  
016288         10  OLD-TDAC-NAME-1           PIC X(40).                 
016290         10  OLD-TDAC-NAME-AREA-1.                                
016292             15  OLD-TDAC-N1-KEY       PIC X(14).                 
016294             15  OLD-TDAC-N1-FIRST     PIC X(40).                 
016296             15  OLD-TDAC-N1-MID       PIC X(20).                 
016298             15  OLD-TDAC-N1-LAST      PIC X(40).                 
016300             15  OLD-TDAC-N1-PREFIX    PIC X(12).                 
016302             15  OLD-TDAC-N1-SUFFIX    PIC X(12).                 
016304             15  OLD-TDAC-N1-FAMILIAR  PIC X(20).                 
016306             15  OLD-TDAC-N1-PRT-PFX   PIC X(01).                 
016308             15  OLD-TDAC-N1-PRT-SFX   PIC X(01).                 
016310             15  OLD-TDAC-N1-DESIGNAT  PIC X(20).                 
016312         10  OLD-TDAC-NAME-2           PIC X(40).                 
016314         10  OLD-TDAC-N2-MODIFIED      PIC X(01).                 
016316         10  OLD-TDAC-N2-PRINT-CD      PIC X(01).                 
016318         10  OLD-TDAC-NAME-AREA-2.                                
016320             15  OLD-TDAC-N2-KEY       PIC X(14).                 
016322             15  OLD-TDAC-N2-FIRST     PIC X(40).                 
016324             15  OLD-TDAC-N2-MID       PIC X(20).                 
016326             15  OLD-TDAC-N2-LAST      PIC X(40).                 
016328             15  OLD-TDAC-N2-PREFIX    PIC X(12).                 
016330             15  OLD-TDAC-N2-SUFFIX    PIC X(12).                 
016332             15  OLD-TDAC-N2-FAMILIAR  PIC X(20).                 
016334             15  OLD-TDAC-N2-PRT-PFX   PIC X(01).                 
016336             15  OLD-TDAC-N2-PRT-SFX   PIC X(01).                 
016338             15  OLD-TDAC-N2-DESIGNAT  PIC X(20).                 
016340         10  OLD-TDAC-NAME-3           PIC X(40).                 
016342         10  OLD-TDAC-N3-MODIFIED      PIC X(01).                 
016344         10  OLD-TDAC-N3-PRINT-CD      PIC X(01).                 
016346         10  OLD-TDAC-NAME-AREA-3.                                
016348             15  OLD-TDAC-N3-KEY       PIC X(14).                 
016350             15  OLD-TDAC-N3-FIRST     PIC X(40).                 
016352             15  OLD-TDAC-N3-MID       PIC X(20).                 
016354             15  OLD-TDAC-N3-LAST      PIC X(40).                 
016356             15  OLD-TDAC-N3-PREFIX    PIC X(12).                 
016358             15  OLD-TDAC-N3-SUFFIX    PIC X(12).                 
016360             15  OLD-TDAC-N3-FAMILIAR  PIC X(20).                 
016362             15  OLD-TDAC-N3-PRT-PFX   PIC X(01).                 
016364             15  OLD-TDAC-N3-PRT-SFX   PIC X(01).                 
016366             15  OLD-TDAC-N3-DESIGNAT  PIC X(20).                 
016368         10  OLD-TDAC-ADDR-KEY         PIC X(28).                 
016370         10  OLD-TDAC-ADDR-1           PIC X(40).                 
016372         10  OLD-TDAC-ADDR-2           PIC X(40).                 
016374         10  OLD-TDAC-CITY             PIC X(40).                 
016376         10  OLD-TDAC-STATE            PIC X(2).                  
016378         10  OLD-TDAC-PROVINCE         PIC X(2).                  
016380         10  OLD-TDAC-COUNTRY          PIC X(2).                  
016382         10  OLD-TDAC-ZIP-CODE.                                   
016384             15  OLD-TDAC-ZIP          PIC 9(5).                  
016386             15  OLD-TDAC-ZIP-4        PIC 9(4).                  
016388         10  OLD-TDAC-LONGITUDE        PIC S9(3)V9(6).            
016390         10  OLD-TDAC-LATITUDE         PIC S9(3)V9(6).            
016392         10  OLD-TDAC-MAIL-CD          PIC 9(1).                  
016394         10  OLD-TDAC-TICKLER-FLAG     PIC 9.                     
016396         10  OLD-TDAC-RESIDENT-CD      PIC 9.                     
016398         10  OLD-TDAC-ALIEN-CD         PIC 9(1).                  
016400         10  OLD-TDAC-SHT-NAME         PIC X(20).                 
016402         10  OLD-TDAC-BAR-CD           PIC 9(3).                  
016404         10  OLD-TDAC-PHONE-1          PIC 9(10).                 
016406         10  OLD-TDAC-PHONE-2          PIC 9(10).                 
016408         10  OLD-TDAC-TIN-CD           PIC X(1).                  
016410         10  OLD-TDAC-TIN-CERT-CD      PIC 9(1).                  
016412         10  OLD-TDAC-TIN-CERT-DT      PIC 9(8).                  
016414         10  OLD-TDAC-TIN-NBR          PIC 9(9).                  
016416         10  OLD-TDAC-OFFICER          PIC X(3).                  
016418         10  OLD-TDAC-EMP-CD           PIC X(1).                  
016420         10  OLD-TDAC-FREE-MARK        PIC X(24).                 
016422         10  OLD-TDAC-INQ-SECR-CD      PIC 9(1).                  
016424         10  OLD-TDAC-PRIVACY          PIC 9(1).                  
016426         10  OLD-TDAC-BK-DEF-CD1       PIC X(1).                  
016428         10  OLD-TDAC-BK-DEF-CD2       PIC X(1).                  
016430         10  OLD-TDAC-BK-DEF-CD3       PIC X(1).                  
016432         10  OLD-TDAC-BK-DEF-CD4       PIC X(1).                  
016434         10  OLD-TDAC-BK-DEF-CD5       PIC X(1).                  
016436         10  OLD-TDAC-EMPLOYEE-ID      PIC X(8).                  
016438         10  OLD-TDAC-EMAIL-ADDR       PIC X(100).                
016440         10  OLD-TDAC-EMAIL-ADDR-R REDEFINES OLD-TDAC-EMAIL-ADDR. 
016442             15  OLD-TDAC-EMAIL-ADDR-1-30  PIC X(30).             
016444             15  OLD-TDAC-EMAIL-ADDR-31-60 PIC X(30).             
016446             15  OLD-TDAC-EMAIL-ADDR-61-90 PIC X(30).             
016448             15  OLD-TDAC-EMAIL-ADDR-91-100                       
016450                                           PIC X(10).             
016452         10 OLD-TDAC-EMAIL-ADDR-RR                                
016454                                   REDEFINES OLD-TDAC-EMAIL-ADDR. 
016456             15  OLD-TDAC-EMAIL-ADDR-1-50  PIC X(50).             
016458             15  OLD-TDAC-EMAIL-ADDR-51-100 PIC X(50).            
016460         10  OLD-TDAC-EMAIL-PSSWRD     PIC X(12).                 
016462         10  OLD-TDAC-GENDER           PIC X(1).                  
016464         10  OLD-TDAC-NEW-CUST         PIC 9(1).                  
016466         10  OLD-TDAC-OPEN-DT          PIC 9(8).                  
016468         10  OLD-TDAC-LUPD-DATE        PIC 9(8).                  
016470         10  OLD-TDAC-LUPD-TIME        PIC 9(8).                  
016472         10  OLD-TDAC-LST-CONTACT      PIC 9(8).                  
016474         10  OLD-TDAC-BIRTH-DT         PIC 9(8).                  
016476         10  OLD-TDAC-BIRTH-DT-2       PIC 9(8).                  
016478         10  OLD-TDAC-BIRTH-DT-3       PIC 9(8).                  
016480         10  OLD-TDAC-DEATH-DT         PIC 9(8).                  
016482         10  OLD-TDAC-ADD-DT           PIC 9(8).                  
016484         10  OLD-TDAC-ADD-TM           PIC 9(6).                  
016486         10  OLD-TDAC-ROTH-DATE        PIC 9(8).                  
016488         10  OLD-TDAC-CD-BAL           PIC S9(15)V9(2).           
016490         10  OLD-TDAC-CD-BAL-BYR       PIC S9(15)V9(2).           
016492         10  OLD-TDAC-CD-PENLTY        PIC S9(15)V9(2).           
016494         10  OLD-TDAC-CD-WTHLD         PIC S9(15)V9(2).           
016496         10  OLD-TDAC-CD-INT           PIC S9(15)V9(2).           
016498         10  OLD-TDAC-CD-OID-INT       PIC S9(15)V9(2).           
016500         10  OLD-TDAC-IRA-BAL          PIC S9(15)V9(2).           
016502         10  OLD-TDAC-IRA-BAL-BYR      PIC S9(15)V9(2).           
016504         10  OLD-TDAC-IRA-PENLTY       PIC S9(15)V9(2).           
016506         10  OLD-TDAC-IRA-WTHLD        PIC S9(15)V9(2).           
016508         10  OLD-TDAC-IRA-INT          PIC S9(15)V9(2).           
016510         10  OLD-TDAC-IRA-CONTR        PIC S9(15)V9(2).           
016512         10  OLD-TDAC-IRA-CONTR-LY     PIC S9(15)V9(2).           
016514         10  OLD-TDAC-IRA-DISTR        PIC S9(15)V9(2).           
016516         10  OLD-TDAC-IRA-DISTR-LY     PIC S9(15)V9(2).           
016518         10  OLD-TDAC-IRA-ROLLOVER     PIC S9(15)V9(2).           
016520         10  OLD-TDAC-IRA-TRF-IN       PIC S9(15)V9(2).           
016522         10  OLD-TDAC-IRA-TRF-OUT      PIC S9(15)V9(2).           
016524         10  OLD-TDAC-IRA-FAIR-MKT     PIC S9(15)V9(2).           
016526         10  OLD-TDAC-CIF-REMARK       PIC X.                     
016528         10  OLD-TDAC-CD-ST-WHLD       PIC S9(15)V9(2).           
016530         10  OLD-TDAC-IRA-ST-WHLD      PIC S9(15)V9(2).           
016532         10  OLD-TDAC-CURR-YR-AMT      PIC S9(15)V9(2)            
016534                                           OCCURS 12 TIMES.       
016536         10  OLD-TDAC-LAST-YR-AMT      PIC S9(15)V9(2)            
016538                                           OCCURS 12 TIMES.       
016540         10  OLD-TDAC-TIN-CD-2         PIC X(01).                 
016542         10  OLD-TDAC-TIN-CRT-CD-2     PIC 9(01).                 
016544         10  OLD-TDAC-TIN-CRT-DT-2     PIC 9(08).                 
016546         10  OLD-TDAC-TIN-NBR-2        PIC 9(09).                 
016548         10  OLD-TDAC-TIN-CD-3         PIC X(01).                 
016550         10  OLD-TDAC-TIN-CRT-CD-3     PIC 9(01).                 
016552         10  OLD-TDAC-TIN-CRT-DT-3     PIC 9(08).                 
016554         10  OLD-TDAC-TIN-NBR-3        PIC 9(09).                 
016556         10  OLD-TDAC-NAICS-CD         PIC 9(06).                 
016558         10  OLD-TDAC-CIF-PASS-THR     PIC 9(01).                 
016560         10  OLD-TDAC-EMAIL-NTC        PIC 9(01).                 
016562         10  OLD-TDAC-RMD-YR-AMT       PIC S9(15)V9(2).           
016564         10  OLD-TDAC-ADDR-CHG-DT      PIC 9(08).                 
016566         10  OLD-TDAC-WTHLD-CD         PIC 9(01).                 
016568         10  OLD-TDAC-ST-WHLD-CD       PIC 9(01).                 
016570         10  OLD-TDAC-WTHLD-AMT        PIC S9(12)V9(2).           
016572         10  OLD-TDAC-ST-WHLD-AMT      PIC S9(12)V9(2).           
016574         10  OLD-TDAC-FOREIGN-LANG     PIC X(01).                 
016576         10  OLD-TDAC-L-ROLLOVR-DT     PIC 9(08).                 
016578         10  OLD-TDAC-CUSTM-FIELDS     PIC 9(01).                 
016580         10  OLD-TDAC-LLC-NAME         PIC X(40).                 
016582         10  OLD-TDAC-LLC-TIN-CD       PIC X(01).                 
016584         10  OLD-TDAC-LLC-TIN          PIC 9(09).                 
016586         10  OLD-TDAC-FOREIGN-PHN      PIC X(20).                 
016588                                                                  
016590     05  OLD-TDAACCT-DATA              PIC X(2400).               
016592     05  OLD-TDAACCT.                                             
016594         10  OLD-TDAA-G-KEY.                                      
016596             15  OLD-TDAA-BANK           PIC 9(4).                
016598             15  OLD-TDAA-BRCH           PIC 9(4).                
016600             15  OLD-TDAA-APPL           PIC 9(1).                
016602             15  OLD-TDAA-CUST           PIC 9(12).               
016604             15  OLD-TDAA-ACCT           PIC 9(10).               
016606         10  OLD-TDAA-G-DATA-OPT.                                 
016608             15  OLD-TDAA-STATUS         PIC X(1).                
016610             15  OLD-TDAA-IRA-TYPE       PIC 9(2).                
016612             15  OLD-TDAA-ACCT-OPTION    PIC 9(2).                
016614             15  OLD-TDAA-DT-CONDENSED   PIC 9(8).                
016616             15  OLD-TDAA-CERT           PIC 9(7).                
016618             15  OLD-TDAA-SHT-NAME       PIC X(20).               
016620             15  OLD-TDAA-TITLE          PIC X(40).               
016622             15  OLD-TDAA-TITLE-PRINT    PIC X(1).                
016624             15  OLD-TDAA-ADDR-USAGE     PIC X(01).               
016626             15  OLD-TDAA-ADDR-ALT       PIC X(01).               
016628             15  OLD-TDAA-ADDR-TEMP      PIC X(01).               
016630             15  OLD-TDAA-TEMP-BEG-DT    PIC 9(04).               
016632             15  OLD-TDAA-TEMP-END-DT    PIC 9(04).               
016634             15  OLD-TDAA-TEMP-EFF-DT    PIC 9(08).               
016636             15  OLD-TDAA-TEMP-EXP-DT    PIC 9(08).               
016638             15  OLD-TDAA-END-OF-INT     PIC 9(1).                
016640             15  OLD-TDAA-END-OF-MAT     PIC 9(1).                
016642             15  OLD-TDAA-END-OF-STMT    PIC 9(1).                
016644             15  OLD-TDAA-END-OF-CMPD    PIC 9(1).                
016646             15  OLD-TDAA-END-OF-FEE     PIC 9(1).                
016648             15  OLD-TDAA-OFFICER        PIC X(3).                
016650             15  OLD-TDAA-OFFICER-2      PIC X(3).                
016652             15  OLD-TDAA-OFFICER-3      PIC X(3).                
016654             15  OLD-TDAA-FREE-MARK      PIC X(24).               
016656             15  OLD-TDAA-CLASS-CD       PIC X(1).                
016658             15  OLD-TDAA-CORR-BK-CD     PIC X(1).                
016660             15  OLD-TDAA-PUBLIC-FUND    PIC X(1).                
016662             15  OLD-TDAA-TRUST-CD       PIC X(1).                
016664             15  OLD-TDAA-RT-CHG-ALLOW   PIC 9(1).                
016666             15  OLD-TDAA-WTHDRW-ALLOW   PIC 9(1).                
016668             15  OLD-TDAA-DPOSIT-ALLOW   PIC 9(1).                
016670             15  OLD-TDAA-POST-MAT       PIC 9(1).                
016672             15  OLD-TDAA-RT-FLOOR       PIC 9(1).                
016674             15  OLD-TDAA-REPO-CD        PIC 9(1).                
016676             15  OLD-TDAA-TOTAL-CD       PIC 9(3).                
016678             15  OLD-TDAA-REN-TOTAL-CD   PIC 9(3).                
016680             15  OLD-TDAA-ORG-TOTAL-CD   PIC 9(3).                
016682             15  OLD-TDAA-INQ-SECR-CD    PIC 9(1).                
016684             15  OLD-TDAA-MAIL-CD        PIC 9(1).                
016686             15  OLD-TDAA-WTHD-REQD-CD   PIC 9(1).                
016688             15  OLD-TDAA-TICKLER-FLAG   PIC 9.                   
016690             15  OLD-TDAA-DISP-CD        PIC 9(1).                
016692             15  OLD-TDAA-CLS-DISP-CD    PIC 9(1).                
016694             15  OLD-TDAA-DIST-STATUS    PIC 9(1).                
016696             15  OLD-TDAA-COMM-ACCT      PIC 9(1).                
016698             15  OLD-TDAA-RENEW-CD       PIC 9(1).                
016700             15  OLD-TDAA-PLEDGE-CD      PIC X(1).                
016702             15  OLD-TDAA-NEGOT-CD       PIC X(1).                
016704             15  OLD-TDAA-BENEF-CD       PIC 9(1).                
016706             15  OLD-TDAA-COMM-MAT-CD    PIC 9(1).                
016708             15  OLD-TDAA-NBR-BENEF      PIC 9(1).                
016710             15  OLD-TDAA-OVERRIDE       PIC 9(1).                
016712             15  OLD-TDAA-INT-CD         PIC 9(1).                
016714             15  OLD-TDAA-WTHLD-CD       PIC 9(1).                
016716             15  OLD-TDAA-WTHLD-AMT      PIC S9(12)V9(2).         
016718             15  OLD-TDAA-IGL-GRP        PIC 9(2).                
016720             15  OLD-TDAA-SUM-STMT-CD    PIC 9(1).                
016722             15  OLD-TDAA-REN-NTC-CD     PIC 9(1).                
016724             15  OLD-TDAA-PMAT-NTC-CD    PIC 9(1).                
016726             15  OLD-TDAA-RTCHG-NTC-CD   PIC 9(1).                
016728             15  OLD-TDAA-INT-NTC-CD     PIC 9(1).                
016730             15  OLD-TDAA-CHG-NTC        PIC 9(1).                
016732             15  OLD-TDAA-YIELD-NUM      PIC 9(3).                
016734             15  OLD-TDAA-YIELD-DENOM    PIC 9(3).                
016736             15  OLD-TDAA-CMPD-FREQ      PIC 9(1).                
016738             15  OLD-TDAA-CMPD-NTRVL     PIC 9(4).                
016740             15  OLD-TDAA-RT-CHG-LIMIT   PIC 9(1).                
016742             15  OLD-TDAA-VAR-RT-IMMED   PIC 9(1).                
016744             15  OLD-TDAA-VAR-RT-INT     PIC 9(1).                
016746             15  OLD-TDAA-VAR-RT-SCHED   PIC 9(1).                
016748             15  OLD-TDAA-VAR-RT-CUST    PIC 9(1).                
016750             15  OLD-TDAA-VAR-RT-BAL     PIC 9(1).                
016752             15  OLD-TDAA-RT-INDX-CD     PIC 9(2).                
016754             15  OLD-TDAA-R-RT-INDX-CD   PIC XX.                  
016756             15  OLD-TDAA-RT-MARG-CD     PIC 9(2).                
016758             15  OLD-TDAA-R-RT-MARG-CD   PIC XX.                  
016760             15  OLD-TDAA-RT-TIER-CD     PIC 9(2).                
016762             15  OLD-TDAA-R-RT-TIER-CD   PIC XX.                  
016764             15  OLD-TDAA-RT-SR-CD       PIC 9(2).                
016766             15  OLD-TDAA-R-RT-SR-CD     PIC XX.                  
016768             15  OLD-TDAA-RT-REGN-CD     PIC 9(2).                
016770             15  OLD-TDAA-RT-CHG-NTRVL   PIC 9(3).                
016772             15  OLD-TDAA-CAP-RT-CHG     PIC X.                   
016774             15  OLD-TDAA-R-TIER-RT-CH   PIC X.                   
016776             15  OLD-TDAA-ALERT-CD       PIC 9(2).                
016778             15  OLD-TDAA-ALERT-CD-2     PIC 9(2).                
016780             15  OLD-TDAA-ALERT-CD-3     PIC 9(2).                
016782             15  OLD-TDAA-CENSUS-TRACT   PIC 9(4)V9(2).           
016784             15  OLD-TDAA-MK-SEGMENT     PIC X(2).                
016786             15  OLD-TDAA-BK-DEF-TOT     PIC X(3).                
016788             15  OLD-TDAA-BK-DEF-CD1     PIC X(1).                
016790             15  OLD-TDAA-BK-DEF-CD2     PIC X(1).                
016792             15  OLD-TDAA-BK-DEF-CD3     PIC X(1).                
016794             15  OLD-TDAA-BK-DEF-CD4     PIC X(1).                
016796             15  OLD-TDAA-BK-DEF-CD5     PIC X(1).                
016798             15  OLD-TDAA-OID-METH       PIC 9(1).                
016800             15  OLD-TDAA-EOY-CD         PIC 9(1).                
016802             15  OLD-TDAA-B-NOTC-YR1     PIC 9(1).                
016804             15  OLD-TDAA-B-NOTC-YR2     PIC 9(1).                
016806             15  OLD-TDAA-B-NOTC-YR3     PIC 9(1).                
016808             15  OLD-TDAA-NO-COMB-IRS    PIC 9(1).                
016810             15  OLD-TDAA-PENLTY-CD      PIC 999.                 
016812             15  OLD-TDAA-MONEY-SRC-CD   PIC X(1).                
016814             15  OLD-TDAA-INTERNET-CD.                            
016816                 20  OLD-TDAA-INTERNET-BPY   PIC 9(1).            
016818                 20  OLD-TDAA-INTERNET-TFR   PIC 9(1).            
016820                 20  OLD-TDAA-INTERNET-INQ   PIC 9(1).            
016822             15  OLD-TDAA-IRA-BACKED     PIC 9(1).                
016824             15  OLD-TDAA-SAV-DEPOSIT    PIC 9(1).                
016826             15  OLD-TDAA-MAT-TYPE       PIC 9(1).                
016828             15  OLD-TDAA-MAT-TERM       PIC 9(4).                
016830             15  OLD-TDAA-ORG-MAT-TYPE   PIC 9(1).                
016832             15  OLD-TDAA-ORG-MAT-TERM   PIC 9(4).                
016834             15  OLD-TDAA-ODD-PAYMENT    PIC 9(1).                
016836             15  OLD-TDAA-PAY-FREQ       PIC 9(1).                
016838             15  OLD-TDAA-PAY-NTRVL      PIC 9(4).                
016840             15  OLD-TDAA-FEE-FREQ       PIC 9(1).                
016842             15  OLD-TDAA-FEE-NTRVL      PIC 9(4).                
016844             15  OLD-TDAA-STMT-FREQ      PIC 9(1).                
016846             15  OLD-TDAA-STMT-NTRVL     PIC 9(4).                
016848             15  OLD-TDAA-EMPLOYEE-ID    PIC X(8).                
016850             15  OLD-TDAA-EFT-CARD       PIC X(1).                
016852             15  OLD-TDAA-PEN-WAV-RESN   PIC X(1).                
016854             15  OLD-TDAA-CLOSED-RESN    PIC X(1).                
016856             15  OLD-TDAA-SPECIAL-STMT   PIC 9(1).                
016858             15  OLD-TDAA-CLS-THIS-MTH   PIC 9(1).                
016860             15  OLD-TDAA-RC-MAT-ONLY    PIC 9(1).                
016862             15  OLD-TDAA-GRACE-DAYS     PIC 9(2).                
016864             15  OLD-TDAA-CLS-ON-MAT     PIC 9(1).                
016866         10  OLD-TDAA-G-ACCT-NBR.                                 
016868             15  OLD-TDAA-DDA-ACCT-1     PIC 9(12).               
016870             15  OLD-TDAA-DDA-ACCT-1-S   PIC 9(10).               
016872             15  OLD-TDAA-DDA-ACCT-2     PIC 9(12).               
016874             15  OLD-TDAA-DDA-ACCT-2-S   PIC 9(10).               
016876             15  OLD-TDAA-DDA-ACCT-3     PIC 9(12).               
016878             15  OLD-TDAA-DDA-ACCT-3-S   PIC 9(10).               
016880             15  OLD-TDAA-INT-ACCT       PIC 9(12).               
016882             15  OLD-TDAA-INT-ACCT-S     PIC 9(10).               
016884             15  OLD-TDAA-CS-ACCT        PIC 9(12).               
016886             15  OLD-TDAA-CS-ACCT-S      PIC 9(10).               
016888             15  OLD-TDAA-CC-ACCT        PIC 9(12).               
016890             15  OLD-TDAA-LNS-BORROWER   PIC 9(12).               
016892             15  OLD-TDAA-LNS-NOTE       PIC 9(10).               
016894             15  OLD-TDAA-CNV-OLD-ACCT   PIC X(15).               
016896             15  OLD-TDAA-CLS-ACCT       PIC 9(12).               
016898             15  OLD-TDAA-CLS-ACCT-S     PIC 9(10).               
016900         10  OLD-TDAA-G-CNTR.                                     
016902             15  OLD-TDAA-DAYS-IN-PER    PIC 9(5).                
016904             15  OLD-TDAA-RR-CYC-NBR     PIC 9(2).                
016906             15  OLD-TDAA-CR-CNT-STD     PIC 9(5).                
016908             15  OLD-TDAA-CR-AMT-STD     PIC S9(12)V9(2).         
016910             15  OLD-TDAA-DB-CNT-STD     PIC 9(5).                
016912             15  OLD-TDAA-DB-AMT-STD     PIC S9(12)V9(2).         
016914             15  OLD-TDAA-CR-CNT-YTD     PIC 9(5).                
016916             15  OLD-TDAA-CR-AMT-YTD     PIC S9(12)V9(2).         
016918             15  OLD-TDAA-DB-CNT-YTD     PIC 9(5).                
016920             15  OLD-TDAA-DB-AMT-YTD     PIC S9(12)V9(2).         
016922             15  OLD-TDAA-DAYS-IN-TERM   PIC 9(5).                
016924         10  OLD-TDAA-G-AMT.                                      
016926             15  OLD-TDAA-BEG-INT-BAL    PIC S9(12)V9(2).         
016928             15  OLD-TDAA-PURCH-AMT      PIC S9(12)V9(2).         
016930             15  OLD-TDAA-CURR-BAL       PIC S9(12)V9(2).         
016932             15  OLD-TDAA-AVAIL-BAL      PIC S9(12)V9(2).         
016934             15  OLD-TDAA-BAL-BEG-MAT    PIC S9(12)V9(2).         
016936             15  OLD-TDAA-CLOSE-AMT      PIC S9(12)V9(2).         
016938             15  OLD-TDAA-MONEY-AMT      PIC S9(12)V9(2).         
016940             15  OLD-TDAA-BAL-BEG-STMT   PIC S9(12)V9(2).         
016942             15  OLD-TDAA-ACCR-INT       PIC S9(12)V9(6).         
016944             15  OLD-TDAA-ANTIC-INT      PIC S9(12)V9(2).         
016946             15  OLD-TDAA-INT-TO-POST    PIC S9(12)V9(2).         
016948             15  OLD-TDAA-1099-YTD       PIC S9(12)V9(2).         
016950             15  OLD-TDAA-1099-LST-YR    PIC S9(12)V9(2).         
016952             15  OLD-TDAA-CURR-PENLTY    PIC S9(12)V9(2).         
016954             15  OLD-TDAA-PENLTY-STD     PIC S9(12)V9(2).         
016956             15  OLD-TDAA-PENLTY-YTD     PIC S9(12)V9(2).         
016958             15  OLD-TDAA-LST-PENLTY     PIC S9(12)V9(2).         
016960             15  OLD-TDAA-CURR-INT-ADJ   PIC S9(12)V9(2).         
016962             15  OLD-TDAA-TOTAMT-HOLDS   PIC S9(12)V9(2).         
016964             15  OLD-TDAA-NXT-INT-ADJ    PIC S9(12)V9(2).         
016966             15  OLD-TDAA-FEE-AMT        PIC S9(12)V9(2).         
016968             15  OLD-TDAA-OID-RPT-INT    PIC S9(12)V9(2).         
016970             15  OLD-TDAA-FAIR-MRKT      PIC S9(12)V9(2).         
016972             15  OLD-TDAA-CUR-WHLD-AMT   PIC S9(12)V9(2).         
016974             15  OLD-TDAA-LST-WHLD-AMT   PIC S9(12)V9(2).         
016976             15  OLD-TDAA-WTHLD-STD      PIC S9(12)V9(2).         
016978             15  OLD-TDAA-WTHLD-YTD      PIC S9(12)V9(2).         
016980             15  OLD-TDAA-LST-INT-PMT    PIC S9(12)V9(2).         
016982             15  OLD-TDAA-BAL-BEG-YR     PIC S9(12)V9(2).         
016984             15  OLD-TDAA-BAL-AT-CONV    PIC S9(12)V9(2).         
016986             15  OLD-TDAA-BAL-BEG-LYR    PIC S9(12)V9(2).         
016988             15  OLD-TDAA-MIN-BAL-STD    PIC S9(12)V9(2).         
016990             15  OLD-TDAA-MIN-BAL-YTD    PIC S9(12)V9(2).         
016992             15  OLD-TDAA-MAX-BAL-YTD    PIC S9(12)V9(2).         
016994             15  OLD-TDAA-LMINBAL-STD    PIC S9(12)V9(2).         
016996             15  OLD-TDAA-CMPD-INT       PIC S9(12)V9(2).         
016998             15  OLD-TDAA-PER-DIEM       PIC S9(12)V9(6).         
017000             15  OLD-TDAA-AVG-PER-DIEM   PIC S9(12)V9(6).         
017002             15  OLD-TDAA-EMAIL-MAXAMT   PIC 9(10).               
017004             15  OLD-TDAA-EMAIL-MINAMT   PIC 9(10).               
017006             15  OLD-TDAA-DTH-FAIRMKT    PIC S9(12)V9(2).         
017008             15  OLD-TDAA-PENLTY-WAIVE   PIC S9(12)V9(2).         
017010         10  OLD-TDAA-G-RATES.                                    
017012             15  OLD-TDAA-BEG-INT-RT     PIC 9(2)V9(3).           
017014             15  OLD-TDAA-CUR-INT-RT     PIC 9(2)V9(3).           
017016             15  OLD-TDAA-FLOOR-RT       PIC 9(2)V9(3).           
017018             15  OLD-TDAA-FLOOR-INCR     PIC 9(2)V9(3).           
017020             15  OLD-TDAA-YIELD-RT       PIC 9(2)V9(3).           
017022             15  OLD-TDAA-RISE-RATE      PIC 9(2)V9(3)            
017024                               OCCURS 10.                         
017026             15  OLD-TDAA-LNS-INCRMNT    PIC 9(2)V9(4).           
017028             15  OLD-TDAA-RT-VARIANCE    PIC S9(1)V9(2).          
017030             15  OLD-TDAA-CONST-RT-ADJ   PIC S9(2)V9(3).          
017032             15  OLD-TDAA-RATE-AT-EOY    PIC 9(2)V9(3).           
017034             15  OLD-TDAA-RATE-LST-STM   PIC 9(2)V9(3).           
017036             15  OLD-TDAA-ORG-YIELD-RT   PIC 9(2)V9(3).           
017038             15  OLD-TDAA-REN-YIELD-RT   PIC 9(2)V9(3).           
017040         10  OLD-TDAA-G-DATES.                                    
017042             15  OLD-TDAA-SCHED-DT       PIC 9(8).                
017044             15  OLD-TDAA-ACCR-DT        PIC 9(8).                
017046             15  OLD-TDAA-OPEN-DT        PIC 9(8).                
017048             15  OLD-TDAA-CLSD-DT        PIC 9(8).                
017050             15  OLD-TDAA-LST-MAT-DT     PIC 9(8).                
017052             15  OLD-TDAA-LST-POST-DT    PIC 9(8).                
017054             15  OLD-TDAA-LST-IN-PROC    PIC 9(8).                
017056             15  OLD-TDAA-LST-CONTACT    PIC 9(8).                
017058             15  OLD-TDAA-LST-FEE-DT     PIC 9(8).                
017060             15  OLD-TDAA-LST-RTCHG-DT   PIC 9(8).                
017062             15  OLD-TDAA-LST-DIST-DT    PIC 9(8).                
017064             15  OLD-TDAA-LST-STMT-DT    PIC 9(8).                
017066             15  OLD-TDAA-LST-CMPD-DT    PIC 9(8).                
017068             15  OLD-TDAA-RR-CYC-DT      PIC 9(8)                 
017070                               OCCURS 10.                         
017072             15  OLD-TDAA-BNF-BIRTH-DT   PIC 9(8).                
017074             15  OLD-TDAA-BNF-DEATH-DT   PIC 9(8).                
017076             15  OLD-TDAA-LUPD-DATE      PIC 9(8).                
017078             15  OLD-TDAA-LUPD-TIME      PIC 9(6).                
017080             15  OLD-TDAA-ADD-DT         PIC 9(8).                
017082             15  OLD-TDAA-ADD-TM         PIC 9(6).                
017084             15  OLD-TDAA-CONV-DT        PIC 9(8).                
017086             15  OLD-TDAA-ACT-CLOSE-DT   PIC 9(8).                
017088             15  OLD-TDAA-LST-TBACT-DT   PIC 9(8).                
017090             15  OLD-TDAA-ALERT-EXP-DT   PIC 9(8).                
017092             15  OLD-TDAA-ALRT2-EXP-DT   PIC 9(8).                
017094             15  OLD-TDAA-ALRT3-EXP-DT   PIC 9(8).                
017096             15  OLD-TDAA-NXT-FEE-DT     PIC 9(8).                
017098             15  OLD-TDAA-NXT-POST-DT    PIC 9(8).                
017100             15  OLD-TDAA-NXT-MAT-DT     PIC 9(8).                
017102             15  OLD-TDAA-NXT-DIST-DT    PIC 9(8).                
017104             15  OLD-TDAA-NXT-RT-CHG     PIC 9(8).                
017106             15  OLD-TDAA-NXT-IN-PROC    PIC 9(8).                
017108             15  OLD-TDAA-NXT-CMPD-DT    PIC 9(8).                
017110             15  OLD-TDAA-NXT-STMT-DT    PIC 9(8).                
017112             15  OLD-TDAA-NXT-DS-PROC    PIC 9(8).                
017114             15  OLD-TDAA-ADV-NTC-DT     PIC 9(8).                
017116             15  OLD-TDAA-NXT-29YR-DT    PIC 9(8).                
017118             15  OLD-TDAA-FAIR-MRKT-DT   PIC 9(8).                
017120             15  OLD-TDAA-SORT-FIELD-1   PIC X(36).               
017122             15  OLD-TDAA-SORT-FIELD-2   PIC X(36).               
017124             15  OLD-TDAA-SORT-FIELD-3   PIC X(36).               
017126             15  OLD-TDAA-SORT-FIELD-4   PIC X(36).               
017128         10  OLD-TDAA-CMAT-PUB-ID        PIC X(8).                
017130         10  OLD-TDAA-MSA-CONTR          PIC 9.                   
017132         10  OLD-TDAA-MSA-CONTR-LY       PIC 9.                   
017134         10  OLD-TDAA-AVG-ACCR-INT       PIC S9(12)V9(6).         
017136         10  OLD-TDAA-LEVEL-PAY          PIC 9.                   
017138         10  OLD-TDAA-ST-INT-CD          PIC 9.                   
017140         10  OLD-TDAA-ST-WHLD-CD         PIC 9.                   
017142         10  OLD-TDAA-ST-WHLD-AMT        PIC S9(12)V99.           
017144         10  OLD-TDAA-ST-CUR-W-AMT       PIC S9(12)V99.           
017146         10  OLD-TDAA-ST-LST-W-AMT       PIC S9(12)V99.           
017148         10  OLD-TDAA-ST-WHLD-STD        PIC S9(12)V99.           
017150         10  OLD-TDAA-ST-WHLD-YTD        PIC S9(12)V99.           
017152         10  OLD-TDAA-CIF-REMARK         PIC X.                   
017154         10  OLD-TDAA-CSR                PIC X(3).                
017156         10  OLD-TDAA-BSA-O-RSK-CD       PIC 9(1).                
017158         10  OLD-TDAA-BSA-C-RSK-CD       PIC 9(1).                
017160         10  OLD-TDAA-LRG-TRX-DT         PIC 9(8).                
017162         10  OLD-TDAA-HSA-FMLY-IND       PIC 9(01).               
017164         10  OLD-TDAA-STOP-PAY-IND       PIC 9(01).               
017166         10  OLD-TDAA-IMG-PG-TYPE        PIC X(01).               
017168         10  OLD-TDAA-CONT-LMT-CLC       PIC 9(5)V99.             
017170         10  OLD-TDAA-CONT-LMT-ENT       PIC 9(5)V99.             
017172         10  OLD-TDAA-MEMO-DB            PIC S9(12)V99.           
017174         10  OLD-TDAA-MEMO-CR            PIC S9(12)V99.           
017176         10  OLD-TDAA-MEMO-DB-2          PIC S9(12)V99.           
017178         10  OLD-TDAA-MEMO-CR-2          PIC S9(12)V99.           
017180         10  OLD-TDAA-RT-AT-CONV         PIC 9(2)V9(3).           
017182         10  OLD-TDAA-ACCR-AT-CONV       PIC S9(12)V9(6).         
017184         10  OLD-TDAA-RT-AT-ACRDT        PIC 9(2)V9(3).           
017186         10  OLD-TDAA-BAL-AT-ACRDT       PIC S9(12)V9(2).         
017188         10  OLD-TDAA-ZERO-RT-ALLOW      PIC 9.                   
017190         10  OLD-TDAA-EMAIL-NTC          PIC 9.                   
017192         10  OLD-TDAA-EMAIL-STMT         PIC 9.                   
017194         10  OLD-TDAA-FRAUD-CK-DT        PIC 9(8).                
017196         10  OLD-TDAA-FRAUD-CK-CNT       PIC 9(3).                
017198         10  OLD-TDAA-FRAUD-CK-AMT       PIC S9(12)V9(2).         
017200         10  OLD-TDAA-MISC-ACCTNO        PIC 9(8).                
017202         10  OLD-TDAA-RMD-MAN-CALC       PIC 9(1).                
017204         10  OLD-TDAA-RMD-AMOUNT         PIC S9(12)V9(2).         
017206         10  OLD-TDAA-BROKERAGE-ID       PIC X(10).               
017208         10  OLD-TDAA-MONY-SRC-CD2       PIC X(03).               
017210         10  OLD-TDAA-INHERIT-IRA        PIC 9(01).               
017212         10  OLD-TDAA-LIFE-FACTOR        PIC 9(02)V9(1).          
017214         10  OLD-TDAA-EV-LARGE-TRX       PIC X(01).               
017216         10  OLD-TDAA-EV-MAT-AMT         PIC S9(12)V9(2).         
017218         10  OLD-TDAA-EV-DISP-ACCT       PIC 9(22).               
017220         10  OLD-TDAA-EV-COMP-ACCT       PIC 9(22).               
017222         10  OLD-TDAA-EV-PUBLIC-ID       PIC X(08).               
017224         10  OLD-TDAA-EV-MAT-TYPE        PIC X(01).               
017226         10  OLD-TDAA-EV-INT-TYPE        PIC X(01).               
017228         10  OLD-TDAA-EV-ACCT-TYP        PIC X(01).               
017230         10  OLD-TDAA-EV-WHLD-PCT        PIC 9(02).               
017232         10  OLD-TDAA-EV-NON-ACCR        PIC X(01).               
017234         10  OLD-TDAA-EV-CLOSED          PIC X(01).               
017236         10  OLD-TDAA-EV-CLOSE-MO        PIC X(01).               
017238         10  OLD-TDAA-EV-OPEN-MO         PIC X(01).               
017240         10  OLD-TDAA-EV-ANN-INT         PIC S9(12)V9(2).         
017242         10  OLD-TDAA-EV-ORIG-RT         PIC 9(2)V9(3).           
017244         10  OLD-TDAA-EV-DLY-INT         PIC S9(12)V9(6).         
017246         10  OLD-TDAA-EV-INT-PAY         PIC S9(12)V9(6).         
017248         10  OLD-TDAA-EV-AVAIL-BL        PIC S9(12)V9(2).         
017250         10  OLD-TDAA-EV-RETAIN          PIC X(01).               
017252         10  OLD-TDAA-EV-CL-RETAIN       PIC X(01).               
017254         10  OLD-TDAA-EV-TIMES-REN       PIC 9(05).               
017256         10  OLD-TDAA-EV-CURR-BAL        PIC S9(12)V9(2).         
017258         10  OLD-TDAA-BRKR-DEP-CAT       PIC 9(01).               
017260         10  OLD-TDAA-LINE-OF-BUS        PIC 9(4).                
017262         10  OLD-TDAA-1ST-STMT           PIC 9(01).               
017264         10  OLD-TDAA-POSTAL-CITY        PIC X(40).               
017266         10  OLD-TDAA-POSTAL-CNTRY       PIC X(02).               
017268         10  OLD-TDAA-CITIZN-CNTRY       PIC X(02).               
017270         10  OLD-TDAA-CUSTM-FIELDS       PIC 9(01).               
017272         10  OLD-TDAA-AVG-STEP-RT        PIC 9(2)V9(3).           
017274         10  OLD-TDAA-MONITOR-INQ        PIC 9(01).               
017276         10  OLD-TDAA-IGL-GRP-2          PIC 9(02).               
017278         10  OLD-TDAA-AGG-DAYS-QTD       PIC 9(03).               
017280         10  OLD-TDAA-AGG-BAL-QTD        PIC S9(15)V9(2).         
017282         10  OLD-TDAA-IGL-GRP-3          PIC 9(02).               
017284         10  OLD-TDAA-ALT-ADDR-EOY       PIC 9(01).               
017286         10  OLD-TDAA-1042S-TAX-ID       PIC X(22).               
017288         10  OLD-TDAA-LEC                PIC X(01).               
017290         10  OLD-TDAA-BAL-AT-CLOSE       PIC S9(12)V9(2).         
017292         10  OLD-TDAA-AVL-CAP-INT        PIC S9(6)V9(2).          
017294         10  OLD-TDAA-FIDM-TR-FUND       PIC 9(01).               
017296         10  OLD-TDAA-IRS-FRM-DLVR       PIC 9(01).               
017298         10  OLD-TDAA-PROVINCE           PIC X(02).               
017300         10  OLD-TDAA-PROMOTION          PIC X(25).               
017302         10  OLD-EXTRA-FIELDS.                                    
017304             15  OLD-TDAA-DAYS-INTO-PER  PIC 9(5).                
017306             15  OLD-TDAA-CURR-PAYOFF    PIC S9(9)V9(2).          
017308             15  OLD-TDAA-MANUAL-RT-X    PIC X(5).                
017310             15  OLD-TDAA-MANUAL-RT-RE   REDEFINES                
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 619 lines from 8033 to 8651.

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

