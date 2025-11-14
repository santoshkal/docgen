# LLM Request Debug File
Generated: 2025-11-13T20:40:08.530483

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 19/55
- **Model**: gpt-4.1
- **Chunk Number**: 19
- **Pass Number**: 3
- **Attempt Number**: 2 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,147 tokens
- **User Prompt**: ~23,624 tokens
- **Total Input**: ~25,771 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 19/55" (ID: detailed-code-explanation)

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

**RETRY REQUIRED - Previous attempt had 24.8% coverage**
You missed 799 executable lines.

🚨 ANALYSIS: This chunk has 1061 executable lines (excluding 3 comments/page-breaks).
You returned 264 lines. You're missing 799 executable lines.

COMMON ISSUES:
- Skipping repetitive FILLER definitions (FORBIDDEN!)
- Summarizing data tables with "..." (FORBIDDEN!)
- Omitting "boring" sections for brevity (FORBIDDEN!)
- Using phrases like "similar pattern continues" (FORBIDDEN!)

YOU MUST:
- Include EVERY executable line with its sequence number
- Show ALL FILLERs even if there are 500+ repetitive ones
- Show ALL data table entries completely
- Never use abbreviation, summarization, or ellipsis
- Include complete WORKING-STORAGE and FILE SECTION layouts

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


**CHUNK 19 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 19 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 8840 to 9902 (1,063 lines)\nChunk Tokens (estimated): ~23,556\nActual Input Tokens: 24,962 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 8840-9902 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 19 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 19 of 55.\n\n\n=============================================================================\nCHUNK 19 SOURCE CODE (Lines 8840-9902)\n=============================================================================\n\n```cobol\n017688             OLD-TDAPC-BANK-SPECS.                                \n017690             15  OLD-TDAPC-CREATE-DT          PIC 9(07).          \n017692             15  OLD-TDAPC-CREATE-TM          PIC 9(12).          \n017694             15  OLD-TDAPC-DQVISTA            PIC X.              \n017696             15  OLD-TDAPC-MSI                PIC X.              \n017698             15  OLD-TDAPC-BK-TDA-STAT        PIC X.              \n017700             15  OLD-TDAPC-TDA-PILOT REDEFINES                    \n017702                 OLD-TDAPC-BK-TDA-STAT        PIC X.              \n017704             15  OLD-TDAPC-BK-STATUS          PIC X.              \n017706             15  OLD-TDAPC-BR-NO              PIC XX.             \n017708             15  OLD-TDAPC-CSI-BR-CODE REDEFINES                  \n017710                 OLD-TDAPC-BR-NO              PIC XX.             \n017712             15  OLD-TDAPC-BK-PHONE-NUM.                          \n017714                 20  OLD-TDAPC-AREA-CODE      PIC XXX.            \n017716                 20  OLD-TDAPC-PHONE.                             \n017718                     25  OLD-TDAPC-PHONE-1ST-3 PIC XXX.           \n017720                     25  OLD-TDAPC-PHONE-LST-4 PIC X(04).         \n017722             15  OLD-TDAPC-PHN-NUMBER REDEFINES                   \n017724                 OLD-TDAPC-BK-PHONE-NUM       PIC X(10).          \n017726             15  OLD-TDAPC-TDA-ADD-DAY        PIC XXX.            \n017728             15  OLD-TDAPC-HOLIDAYS           OCCURS 18 TIMES.    \n017730                 20  OLD-TDAPC-HOL-MM         PIC XX.             \n017732                 20  OLD-TDAPC-HOL-DD         PIC XX.             \n017734             15  OLD-TDAPC-FM-SUPPRESS        PIC X.              \n017736             15  OLD-TDAPC-RMT-BK-INDICATOR   PIC XX.             \n017738             15  OLD-TDAPC-RMT-IND REDEFINES                      \n017740                 OLD-TDAPC-RMT-BK-INDICATOR   PIC XX.             \n017742             15  OLD-TDAPC-BK-ADDR            PIC X(28).          \n017744             15  OLD-TDAPC-BK-ADDR-2          PIC X(27).          \n017746             15  OLD-TDAPC-FED-ID             PIC X(10).          \n017748             15  OLD-TDAPC-EOY-RPT-SEQ        PIC X.              \n017750             15  OLD-TDAPC-EOY-EARLY-RUN      PIC X.              \n017752             15  OLD-TDAPC-EOY-RETURN-TO-BK   PIC X.              \n017754             15  OLD-TDAPC-EOY-RETURN-TO-BANK REDEFINES           \n017756                 OLD-TDAPC-EOY-RETURN-TO-BK   PIC X.              \n017758             15  OLD-TDAPC-EOY-IRA-PHONE      PIC 9(10).          \n017760             15  OLD-TDAPC-EOY-DELETE-DATE    PIC 9(06).          \n017762             15  OLD-TDAPC-EOY-IRA-FICHE      PIC X.              \n017764             15  OLD-TDAPC-EOY-IRA-PAPER      PIC X.              \n017766             15  OLD-TDAPC-EOY-IRA-STMT-EARLY PIC X.              \n017768             15  OLD-TDAPC-NO-IRA-STMTS       PIC 9.              \n017770             15  OLD-TDAPC-EOY-IRA-STMT       PIC X.              \n017772             15  OLD-TDAPC-EOY-IRA-STMT-PRINT PIC X.              \n017774             15  OLD-TDAPC-EOY-EARLY-DATE     PIC 9(06).          \n017776             15  OLD-TDAPC-CK21-TDA           PIC X.              \n017778             15  OLD-TDAPC-MSI-OV-TDA         PIC X.              \n017780             15  OLD-TDAPC-BK-IMG-SERV        PIC X(01).          \n017782             15  OLD-TDAPC-EOY-APRIL-DATE     PIC 9(06).          \n017784             15  OLD-TDAPC-EOY-COD-CLOSED-RPT PIC X(01).          \n017786             15  OLD-TDAPC-PRT-NEW            PIC 9(01).          \n017788             15  OLD-TDAPC-IMONITOR           PIC X(01).          \n017790             15  OLD-TDAPC-ENTC-TDA           PIC X.              \n017792             15  OLD-TDAPC-EV-3RD-PARTY-1     PIC X.              \n017794             15  OLD-TDAPC-EV-3RD-PARTY-2     PIC X.              \n017796             15  OLD-TDAPC-HSA-LOCATION       PIC X.              \n017798             15  OLD-TDAPC-PROFITABILITY      PIC X.              \n017800             15  OLD-TDAPC-BANCVUE            PIC X.              \n017802             15  OLD-TDAPC-SPECIAL-DL-BILLING PIC X.              \n017804             15  OLD-TDAPC-CIF-NAME-ADDR      PIC 9.              \n017806             15  OLD-TDAPC-MAIL-ADDR-LINES    PIC X.              \n017808             15  OLD-TDAPC-WEB-ENABLED        PIC X(01).          \n017810             15  OLD-TDAPC-BRANCH-LENGTH      PIC 9.              \n017812             15  OLD-TDAPC-LOB                PIC 9.              \n017814             15  OLD-TDAPC-BILL-EDIT-TEMPLATES                    \n017816                                              PIC 9.              \n017818             15  OLD-TDAPC-MCIF-PRIVACY-OPT                       \n017820                                              PIC 9.              \n017822             15  OLD-TDAPC-TRAIN-BK-FLG       PIC X.              \n017824             15  OLD-TDAPC-EOY-CIB-F-MERD     PIC X(01).          \n017826             15  FILLER                       PIC X(39).          \n017828             15  OLD-TDAPC-LAST-EOM-PROC      PIC 9(08).          \n017830             15  OLD-TDAPC-BUS-DT-AFT-NX      PIC 9(08).          \n017832             15  OLD-TDAPC-NEXT-BUS-DATE      PIC 9(08).          \n017834                                                                  \n017836     05  OLD-TDABENEF.                                            \n017838         10  OLD-TDAB-BANK                    PIC 9(04).          \n017840         10  OLD-TDAB-CUST                    PIC 9(12).          \n017842         10  OLD-TDAB-ACCT                    PIC 9(10).          \n017844         10  OLD-TDAB-BENEF-NBR               PIC 9(02).          \n017846         10  OLD-TDAB-NAME                    PIC X(40).          \n017848         10  OLD-TDAB-NAME-2                  PIC X(40).          \n017850         10  OLD-TDAB-NAME-3                  PIC X(40).          \n017852         10  OLD-TDAB-ADDR-1                  PIC X(40).          \n017854         10  OLD-TDAB-ADDR-2                  PIC X(40).          \n017856         10  OLD-TDAB-CITY                    PIC X(40).          \n017858         10  OLD-TDAB-STATE                   PIC X(02).          \n017860         10  OLD-TDAB-PROVINCE                PIC X(02).          \n017862         10  OLD-TDAB-COUNTRY                 PIC X(02).          \n017864         10  OLD-TDAB-ZIP-CODE.                                   \n017866             15  OLD-TDAB-ZIP                 PIC 9(05).          \n017868             15  OLD-TDAB-ZIP-4               PIC 9(04).          \n017870         10  OLD-TDAB-PHONE                   PIC 9(10).          \n017872         10  OLD-TDAB-TIN                     PIC 9(09).          \n017874         10  OLD-TDAB-BIRTH-DT                PIC 9(08).          \n017876         10  OLD-TDAB-RELATION                PIC 9(01).          \n017878         10  OLD-TDAB-DESIGNATION             PIC 9(01).          \n017880         10  OLD-TDAB-PERCENT                 PIC 9(03).          \n017882         10  OLD-TDAB-FREE-REMARK             PIC X(24).          \n017884                                                                  \n017886     05  OLD-TDAADDR.                                             \n017888         10  OLD-TDADR-BANK                    PIC 9(04).         \n017890         10  OLD-TDADR-CUST                    PIC 9(12).         \n017892         10  OLD-TDADR-ACCT                    PIC 9(10).         \n017894         10  OLD-TDADR-ADDR-USAGE              PIC X(01).         \n017896         10  OLD-TDADR-TEMP-BEG-DT             PIC 9(04).         \n017898         10  OLD-TDADR-TEMP-END-DT             PIC 9(04).         \n017900         10  OLD-TDADR-TEMP-EFF-DT             PIC 9(08).         \n017902         10  OLD-TDADR-TEMP-EXP-DT             PIC 9(08).         \n017904         10  OLD-TDADR-ADDR-GROUP.                                \n017906             15  OLD-TDADR-T-ADDR.                                \n017908                 20  OLD-TDADR-T-ADDR-1        PIC X(40).         \n017910                 20  OLD-TDADR-T-ADDR-2        PIC X(40).         \n017912                 20  OLD-TDADR-T-CITY          PIC X(40).         \n017914                 20  OLD-TDADR-T-STATE         PIC X(02).         \n017916                 20  OLD-TDADR-T-PROVINCE      PIC X(02).         \n017918                 20  OLD-TDADR-T-COUNTRY       PIC X(02).         \n017920                 20  OLD-TDADR-T-ZIP-CODE.                        \n017922                     25  OLD-TDADR-T-ZIP       PIC 9(05).         \n017924                     25  OLD-TDADR-T-ZIP-4     PIC 9(04).         \n017926                 20  OLD-TDADR-T-ALIEN-CD      PIC 9(01).         \n017928                 20  OLD-TDADR-T-BAR-CODE      PIC 9(03).         \n017930                 20  OLD-TDADR-T-EMAIL-ADDR    PIC X(100).        \n017932                 20  OLD-TDADR-T-EMAIL-ADDR-R                     \n017934                                REDEFINES OLD-TDADR-T-EMAIL-ADDR. \n017936                     25  OLD-TDADR-T-EMAIL-ADDR-1-50   PIC X(50). \n017938                     25  OLD-TDADR-T-EMAIL-ADDR-51-100 PIC X(50). \n017940                 20  OLD-TDADR-T-MAIL-CD       PIC 9(01).         \n017942                 20  OLD-TDADR-T-ADDR-KEY      PIC X(28).         \n017944             15  OLD-TDADR-A-ADDR.                                \n017946                 20  OLD-TDADR-A-NAME-1          PIC X(40).       \n017948                 20  OLD-TDADR-A-NAME-AREA-1.                     \n017950                     25  OLD-TDADR-A-N1-KEY      PIC X(14).       \n017952                     25  OLD-TDADR-A-N1-FIRST    PIC X(40).       \n017954                     25  OLD-TDADR-A-N1-MID      PIC X(20).       \n017956                     25  OLD-TDADR-A-N1-LAST     PIC X(40).       \n017958                     25  OLD-TDADR-A-N1-PREFIX   PIC X(12).       \n017960                     25  OLD-TDADR-A-N1-SUFFIX   PIC X(12).       \n017962                     25  OLD-TDADR-A-N1-FAMILIAR PIC X(20).       \n017964                     25  OLD-TDADR-A-N1-PRT-PFX  PIC X(01).       \n017966                     25  OLD-TDADR-A-N1-PRT-SFX  PIC X(01).       \n017968                     25  OLD-TDADR-A-N1-DESIGNAT PIC X(20).       \n017970                 20  OLD-TDADR-A-NAME-2          PIC X(40).       \n017972                 20  OLD-TDADR-A-N2-MODIFIED     PIC X(01).       \n017974                 20  OLD-TDADR-A-N2-PRINT-CD     PIC X(01).       \n017976                 20  OLD-TDADR-A-NAME-AREA-2.                     \n017978                     25  OLD-TDADR-A-N2-KEY      PIC X(14).       \n017980                     25  OLD-TDADR-A-N2-FIRST    PIC X(40).       \n017982                     25  OLD-TDADR-A-N2-MID      PIC X(20).       \n017984                     25  OLD-TDADR-A-N2-LAST     PIC X(40).       \n017986                     25  OLD-TDADR-A-N2-PREFIX   PIC X(12).       \n017988                     25  OLD-TDADR-A-N2-SUFFIX   PIC X(12).       \n017990                     25  OLD-TDADR-A-N2-FAMILIAR PIC X(20).       \n017992                     25  OLD-TDADR-A-N2-PRT-PFX  PIC X(01).       \n017994                     25  OLD-TDADR-A-N2-PRT-SFX  PIC X(01).       \n017996                     25  OLD-TDADR-A-N2-DESIGNAT PIC X(20).       \n017998                 20  OLD-TDADR-A-NAME-3          PIC X(40).       \n018000                 20  OLD-TDADR-A-N3-MODIFIED     PIC X(01).       \n018002                 20  OLD-TDADR-A-N3-PRINT-CD     PIC X(01).       \n018004                 20  OLD-TDADR-A-NAME-AREA-3.                     \n018006                     25  OLD-TDADR-A-N3-KEY      PIC X(14).       \n018008                     25  OLD-TDADR-A-N3-FIRST    PIC X(40).       \n018010                     25  OLD-TDADR-A-N3-MID      PIC X(20).       \n018012                     25  OLD-TDADR-A-N3-LAST     PIC X(40).       \n018014                     25  OLD-TDADR-A-N3-PREFIX   PIC X(12).       \n018016                     25  OLD-TDADR-A-N3-SUFFIX   PIC X(12).       \n018018                     25  OLD-TDADR-A-N3-FAMILIAR PIC X(20).       \n018020                     25  OLD-TDADR-A-N3-PRT-PFX  PIC X(01).       \n018022                     25  OLD-TDADR-A-N3-PRT-SFX  PIC X(01).       \n018024                     25  OLD-TDADR-A-N3-DESIGNAT PIC X(20).       \n018026                 20  OLD-TDADR-A-ADDR-KEY        PIC X(28).       \n018028                 20  OLD-TDADR-A-ADDR-1        PIC X(40).         \n018030                 20  OLD-TDADR-A-ADDR-2        PIC X(40).         \n018032                 20  OLD-TDADR-A-CITY          PIC X(40).         \n018034                 20  OLD-TDADR-A-STATE         PIC X(02).         \n018036                 20  OLD-TDADR-A-PROVINCE      PIC X(02).         \n018038                 20  OLD-TDADR-A-COUNTRY       PIC X(02).         \n018040                 20  OLD-TDADR-A-ZIP-CODE.                        \n018042                     25  OLD-TDADR-A-ZIP       PIC 9(05).         \n018044                     25  OLD-TDADR-A-ZIP-4     PIC 9(04).         \n018046                 20  OLD-TDADR-A-ALIEN-CD      PIC 9(01).         \n018048                 20  OLD-TDADR-A-BAR-CODE      PIC 9(03).         \n018050                 20  OLD-TDADR-A-EMAIL-ADDR    PIC X(100).        \n018052                 20  OLD-TDADR-A-EMAIL-ADDR-R                     \n018054                                REDEFINES OLD-TDADR-A-EMAIL-ADDR. \n018056                     25  OLD-TDADR-A-EMAIL-ADDR-1-50   PIC X(50). \n018058                     25  OLD-TDADR-A-EMAIL-ADDR-51-100 PIC X(50). \n018060                 20  OLD-TDADR-A-MAIL-CD       PIC 9(01).         \n018062         10  OLD-TDADR-SHT-NAME                PIC X(20).         \n018064         10  OLD-TDADR-LUPD-DATE               PIC 9(08).         \n018066         10  OLD-TDADR-LUPD-TIME               PIC 9(08).         \n018068         10  OLD-TDADR-PUB-ID                  PIC X(08).         \n018070         10  OLD-TDADR-TIN-CD                  PIC X.             \n018072         10  OLD-TDADR-TIN-NBR                 PIC 9(9).          \n018074         10  OLD-TDADR-TIN-CERT-CD             PIC 9.             \n018076         10  OLD-TDADR-TIN-CD-2                PIC X(01).         \n018078         10  OLD-TDADR-TIN-NBR-2               PIC 9(09).         \n018080         10  OLD-TDADR-TIN-CT-CD-2             PIC 9(01).         \n018082         10  OLD-TDADR-TIN-CD-3                PIC X(01).         \n018084         10  OLD-TDADR-TIN-NBR-3               PIC 9(09).         \n018086         10  OLD-TDADR-TIN-CT-CD-3             PIC 9(01).         \n018088                                                                  \n018090     05  OLD-TDACHK.                                              \n018092         10  OLD-TDACK-BANK                    PIC 9(04).         \n018094         10  OLD-TDACK-BRCH                    PIC 9(04).         \n018096         10  OLD-TDACK-ADDR-CUST               PIC 9(12).         \n018098         10  OLD-TDACK-CUST                    PIC 9(12)          \n018100                                               OCCURS 10 TIMES.   \n018102         10  OLD-TDACK-ACCT                    PIC 9(10)          \n018104                                               OCCURS 10 TIMES.   \n018106         10  OLD-TDACK-LUPD-DATE               PIC 9(08).         \n018108         10  OLD-TDACK-LUPD-TIME               PIC 9(08).         \n018110         10  OLD-TDACK-PUB-ID                  PIC X(08).         \n018112                                                                  \n018114     05  OLD-TDAMESSAGE.                                          \n018116         10  OLD-TDAM-BANK                     PIC 9(04).         \n018118         10  OLD-TDAM-APPL                     PIC 9(01).         \n018120         10  OLD-TDAM-CODE-TYPE                PIC 9(01).         \n018122         10  OLD-TDAM-CODE                     PIC 9(04).         \n018124         10  OLD-TDAM-RPT-NBR                  PIC 9(04).         \n018126         10  OLD-TDAM-TEST-MSG                 PIC 9(01).         \n018128         10  OLD-TDAM-MESSAGE-NBR              PIC 9(03).         \n018130         10  OLD-TDAM-MESSAGE-GRP.                                \n018132             15  OLD-TDAM-MESSAGE              PIC X(60)          \n018134                                               OCCURS 6 TIMES.    \n018136         10  OLD-TDAM-STOP-DT                  PIC 9(08).         \n018138         10  OLD-TDAM-ADD-DT                   PIC 9(08).         \n018140         10  OLD-TDAM-ADD-TM                   PIC 9(08).         \n018142         10  OLD-TDAM-LUPD-DT                  PIC 9(08).         \n018144         10  OLD-TDAM-LUPD-TM                  PIC 9(08).         \n018146         10  OLD-TDAM-PUB-ID                   PIC X(08).         \n018148                                                                  \n018150*** PLEASE REMEMBER TO UPDATE THE OLD,AND HOLD FIELDS WHEN        \n018152*** UPDATING THE FOLLOWING TDB FIELDS.                            \n018154*************************************************************     \n018156                                                                  \n018158   03  TDB-RECORD.                                                \n018160     05  TDB-STANDARD-AREA.                                       \n018162         07  TDB-APPL-ID                        PIC X(3).         \n018164         07  TDB-FUNCTION-CD-X.                                   \n018166             10  TDB-FUNCTION-CD                PIC 9(2).         \n018168         07  TDB-ORIGINATE-CLIENT               PIC X(2).         \n018170         07  TDB-CLIENT-VER                     PIC 9(2).         \n018172         07  TDB-CLIENT-TRX-NBR                 PIC 9(4).         \n018174         07  TDB-REC-SEQ                        PIC 9(2).         \n018176         07  TDB-STRUCT-NBR                     PIC 9(2).         \n018178         07  TDB-ERROR-NBR-X.                                     \n018180             10  TDB-ERROR-NBR                  PIC 9(4).         \n018182         07  TDB-MESSAGE-NBR-X.                                   \n018184             10  TDB-MESSAGE-NBR                PIC 9(4).         \n018186         07  TDB-READ-INFO.                                       \n018188             10  TDB-READ-SET-NBR               PIC 9(02).        \n018190             10  TDB-READ-DIRECTION             PIC X(01).        \n018192             10  TDB-READ-AT                    PIC X(03).        \n018194         07  TDB-READ-DATE                      PIC 9(08).        \n018196         07  TDB-SPECIAL-ACTION-X.                                \n018198             10  TDB-SPECIAL-ACTION             PIC 9(02).        \n018200         07  TDB-EXPANSION                      PIC X(09).        \n018202     05  TDB-DATA-AREA                          PIC X(2800).      \n018204                                                                  \n018206     05  TDB-TDARESTART-R REDEFINES TDB-DATA-AREA.                \n018208         10  TDB-TDARESTART.                                      \n018210             15  TDB-TDARST-PROG-ID            PIC X(10).         \n018212             15  TDB-TDARST-USERAREA           PIC X(100).        \n018214             15  FILLER                        PIC X(2690).       \n018216                                                                  \n018218   03  TDB-RECORD-DATA-AREA.                                      \n018220                                                                  \n018222     05  TDB-TDACUST.                                             \n018224         10  TDB-TDAC-BANK-X.                                     \n018226             15  TDB-TDAC-BANK             PIC 9(4).              \n018228         10  TDB-TDAC-CUST-X.                                     \n018230             15  TDB-TDAC-CUST             PIC 9(12).             \n018232         10  TDB-TDAC-BRCH-X.                                     \n018234             15  TDB-TDAC-BRCH             PIC 9(4).              \n018236         10  TDB-TDAC-STATUS               PIC X(1).              \n018238         10  TDB-TDAC-NAME-1               PIC X(40).             \n018240         10  TDB-TDAC-NAME-AREA-1.                                \n018242             15  TDB-TDAC-N1-KEY           PIC X(14).             \n018244             15  TDB-TDAC-N1-FIRST         PIC X(40).             \n018246             15  TDB-TDAC-N1-MID           PIC X(20).             \n018248             15  TDB-TDAC-N1-LAST          PIC X(40).             \n018250             15  TDB-TDAC-N1-PREFIX        PIC X(12).             \n018252             15  TDB-TDAC-N1-SUFFIX        PIC X(12).             \n018254             15  TDB-TDAC-N1-FAMILIAR      PIC X(20).             \n018256             15  TDB-TDAC-N1-PRT-PFX       PIC X(01).             \n018258             15  TDB-TDAC-N1-PRT-SFX       PIC X(01).             \n018260             15  TDB-TDAC-N1-DESIGNAT      PIC X(20).             \n018262         10  TDB-TDAC-NAME-2               PIC X(40).             \n018264         10  TDB-TDAC-N2-MODIFIED          PIC X(01).             \n018266         10  TDB-TDAC-N2-PRINT-CD          PIC X(01).             \n018268         10  TDB-TDAC-NAME-AREA-2.                                \n018270             15  TDB-TDAC-N2-KEY           PIC X(14).             \n018272             15  TDB-TDAC-N2-FIRST         PIC X(40).             \n018274             15  TDB-TDAC-N2-MID           PIC X(20).             \n018276             15  TDB-TDAC-N2-LAST          PIC X(40).             \n018278             15  TDB-TDAC-N2-PREFIX        PIC X(12).             \n018280             15  TDB-TDAC-N2-SUFFIX        PIC X(12).             \n018282             15  TDB-TDAC-N2-FAMILIAR      PIC X(20).             \n018284             15  TDB-TDAC-N2-PRT-PFX       PIC X(01).             \n018286             15  TDB-TDAC-N2-PRT-SFX       PIC X(01).             \n018288             15  TDB-TDAC-N2-DESIGNAT      PIC X(20).             \n018290         10  TDB-TDAC-NAME-3               PIC X(40).             \n018292         10  TDB-TDAC-N3-MODIFIED          PIC X(01).             \n018294         10  TDB-TDAC-N3-PRINT-CD          PIC X(01).             \n018296         10  TDB-TDAC-NAME-AREA-3.                                \n018298             15  TDB-TDAC-N3-KEY           PIC X(14).             \n018300             15  TDB-TDAC-N3-FIRST         PIC X(40).             \n018302             15  TDB-TDAC-N3-MID           PIC X(20).             \n018304             15  TDB-TDAC-N3-LAST          PIC X(40).             \n018306             15  TDB-TDAC-N3-PREFIX        PIC X(12).             \n018308             15  TDB-TDAC-N3-SUFFIX        PIC X(12).             \n018310             15  TDB-TDAC-N3-FAMILIAR      PIC X(20).             \n018312             15  TDB-TDAC-N3-PRT-PFX       PIC X(01).             \n018314             15  TDB-TDAC-N3-PRT-SFX       PIC X(01).             \n018316             15  TDB-TDAC-N3-DESIGNAT      PIC X(20).             \n018318         10  TDB-TDAC-ADDR-KEY             PIC X(28).             \n018320         10  TDB-TDAC-ADDR-1               PIC X(40).             \n018322         10  TDB-TDAC-ADDR-2               PIC X(40).             \n018324         10  TDB-TDAC-CITY                 PIC X(40).             \n018326         10  TDB-TDAC-STATE                PIC X(2).              \n018328         10  TDB-TDAC-PROVINCE             PIC X(2).              \n018330         10  TDB-TDAC-COUNTRY              PIC X(2).              \n018332         10  TDB-TDAC-ZIP-CODE.                                   \n018334             15  TDB-TDAC-ZIP-X.                                  \n018336                 20  TDB-TDAC-ZIP          PIC 9(5).              \n018338             15  TDB-TDAC-ZIP-4-X.                                \n018340                 20  TDB-TDAC-ZIP-4        PIC 9(4).              \n018342         10  TDB-TDAC-LONGITUDE            PIC S9(3)V9(6).        \n018344         10  TDB-TDAC-LATITUDE             PIC S9(3)V9(6).        \n018346         10  TDB-TDAC-MAIL-CD              PIC 9(1).              \n018348         10  TDB-TDAC-TICKLER-FLAG-X.                             \n018350             15  TDB-TDAC-TICKLER-FLAG     PIC 9.                 \n018352         10  TDB-TDAC-RESIDENT-CD-X.                              \n018354             15  TDB-TDAC-RESIDENT-CD      PIC 9.                 \n018356         10  TDB-TDAC-ALIEN-CD             PIC 9(1).              \n018358         10  TDB-TDAC-SHT-NAME             PIC X(20).             \n018360         10  TDB-TDAC-BAR-CD-X.                                   \n018362             15  TDB-TDAC-BAR-CD           PIC 9(3).              \n018364         10  TDB-TDAC-PHONE-1-X.                                  \n018366             15  TDB-TDAC-PHONE-1          PIC 9(10).             \n018368         10  TDB-TDAC-PHONE-2-X.                                  \n018370             15  TDB-TDAC-PHONE-2          PIC 9(10).             \n018372         10  TDB-TDAC-TIN-CD               PIC X(1).              \n018374         10  TDB-TDAC-TIN-CERT-CD-X.                              \n018376             15  TDB-TDAC-TIN-CERT-CD      PIC 9(1).              \n018378         10  TDB-TDAC-TIN-CERT-DT-X.                              \n018380             15  TDB-TDAC-TIN-CERT-DT      PIC 9(8).              \n018382         10  TDB-TDAC-TIN-NBR-X.                                  \n018384             15  TDB-TDAC-TIN-NBR          PIC 9(9).              \n018386         10  TDB-TDAC-OFFICER              PIC X(3).              \n018388         10  TDB-TDAC-EMP-CD               PIC X(1).              \n018390         10  TDB-TDAC-FREE-MARK            PIC X(24).             \n018392         10  TDB-TDAC-INQ-SECR-CD-X.                              \n018394             15  TDB-TDAC-INQ-SECR-CD      PIC 9(1).              \n018396         10  TDB-TDAC-PRIVACY-X.                                  \n018398             15  TDB-TDAC-PRIVACY          PIC 9(1).              \n018400         10  TDB-TDAC-BK-DEF-CD1           PIC X(1).              \n018402         10  TDB-TDAC-BK-DEF-CD2           PIC X(1).              \n018404         10  TDB-TDAC-BK-DEF-CD3           PIC X(1).              \n018406         10  TDB-TDAC-BK-DEF-CD4           PIC X(1).              \n018408         10  TDB-TDAC-BK-DEF-CD5           PIC X(1).              \n018410         10  TDB-TDAC-EMPLOYEE-ID          PIC X(8).              \n018412         10  TDB-TDAC-EMAIL-ADDR           PIC X(100).            \n018414         10  TDB-TDAC-EMAIL-ADDR-R REDEFINES TDB-TDAC-EMAIL-ADDR. \n018416             15  TDB-TDAC-EMAIL-ADDR-1-30  PIC X(30).             \n018418             15  TDB-TDAC-EMAIL-ADDR-31-60 PIC X(30).             \n018420             15  TDB-TDAC-EMAIL-ADDR-61-90 PIC X(30).             \n018422             15  TDB-TDAC-EMAIL-ADDR-91-100                       \n018424                                           PIC X(10).             \n018426         10 TDB-TDAC-EMAIL-ADDR-RR                                \n018428                                   REDEFINES TDB-TDAC-EMAIL-ADDR. \n018430             15  TDB-TDAC-EMAIL-ADDR-1-50  PIC X(50).             \n018432             15  TDB-TDAC-EMAIL-ADDR-51-100 PIC X(50).            \n018434         10  TDB-TDAC-EMAIL-PSSWRD         PIC X(12).             \n018436         10  TDB-TDAC-GENDER               PIC X(1).              \n018438         10  TDB-TDAC-NEW-CUST-X.                                 \n018440             15  TDB-TDAC-NEW-CUST         PIC 9.                 \n018442         10  TDB-TDAC-OPEN-DT-X.                                  \n018444             15  TDB-TDAC-OPEN-DT          PIC 9(8).              \n018446         10  TDB-TDAC-LUPD-DATE-X.                                \n018448             15  TDB-TDAC-LUPD-DATE        PIC 9(8).              \n018450         10  TDB-TDAC-LUPD-TIME-X.                                \n018452             15  TDB-TDAC-LUPD-TIME        PIC 9(8).              \n018454         10  TDB-TDAC-LST-CONTACT-X.                              \n018456             15  TDB-TDAC-LST-CONTACT      PIC 9(8).              \n018458         10  TDB-TDAC-BIRTH-DT-X.                                 \n018460             15  TDB-TDAC-BIRTH-DT         PIC 9(8).              \n018462         10  TDB-TDAC-BIRTH-DT-2-X.                               \n018464             15  TDB-TDAC-BIRTH-DT-2       PIC 9(8).              \n018466         10  TDB-TDAC-BIRTH-DT-3           PIC 9(8).              \n018468         10  TDB-TDAC-DEATH-DT-X.                                 \n018470             15  TDB-TDAC-DEATH-DT         PIC 9(8).              \n018472         10  TDB-TDAC-ADD-DT-X.                                   \n018474             15  TDB-TDAC-ADD-DT           PIC 9(8).              \n018476         10  TDB-TDAC-ADD-TM-X.                                   \n018478             15  TDB-TDAC-ADD-TM           PIC 9(6).              \n018480         10  TDB-TDAC-ROTH-DATE-X.                                \n018482             15  TDB-TDAC-ROTH-DATE        PIC 9(8).              \n018484         10  TDB-TDAC-CD-BAL-X.                                   \n018486             15  TDB-TDAC-CD-BAL           PIC S9(15)V9(2).       \n018488         10  TDB-TDAC-CD-BAL-BYR-X.                               \n018490             15  TDB-TDAC-CD-BAL-BYR       PIC S9(15)V9(2).       \n018492         10  TDB-TDAC-CD-PENLTY-X.                                \n018494             15  TDB-TDAC-CD-PENLTY        PIC S9(15)V9(2).       \n018496         10  TDB-TDAC-CD-WTHLD-X.                                 \n018498             15  TDB-TDAC-CD-WTHLD         PIC S9(15)V9(2).       \n018500         10  TDB-TDAC-CD-INT-X.                                   \n018502             15  TDB-TDAC-CD-INT           PIC S9(15)V9(2).       \n018504         10  TDB-TDAC-CD-OID-INT-X.                               \n018506             15  TDB-TDAC-CD-OID-INT       PIC S9(15)V9(2).       \n018508         10  TDB-TDAC-IRA-BAL-X.                                  \n018510             15  TDB-TDAC-IRA-BAL          PIC S9(15)V9(2).       \n018512         10  TDB-TDAC-IRA-BAL-BYR-X.                              \n018514             15  TDB-TDAC-IRA-BAL-BYR      PIC S9(15)V9(2).       \n018516         10  TDB-TDAC-IRA-PENLTY-X.                               \n018518             15  TDB-TDAC-IRA-PENLTY       PIC S9(15)V9(2).       \n018520         10  TDB-TDAC-IRA-WTHLD-X.                                \n018522             15  TDB-TDAC-IRA-WTHLD        PIC S9(15)V9(2).       \n018524         10  TDB-TDAC-IRA-INT-X.                                  \n018526             15  TDB-TDAC-IRA-INT          PIC S9(15)V9(2).       \n018528         10  TDB-TDAC-IRA-CONTR-X.                                \n018530             15  TDB-TDAC-IRA-CONTR        PIC S9(15)V9(2).       \n018532         10  TDB-TDAC-IRA-CONTR-LY-X.                             \n018534             15  TDB-TDAC-IRA-CONTR-LY     PIC S9(15)V9(2).       \n018536         10  TDB-TDAC-IRA-DISTR-X.                                \n018538             15  TDB-TDAC-IRA-DISTR        PIC S9(15)V9(2).       \n018540         10  TDB-TDAC-IRA-DISTR-LY-X.                             \n018542             15  TDB-TDAC-IRA-DISTR-LY     PIC S9(15)V9(2).       \n018544         10  TDB-TDAC-IRA-ROLLOVER-X.                             \n018546             15  TDB-TDAC-IRA-ROLLOVER     PIC S9(15)V9(2).       \n018548         10  TDB-TDAC-IRA-TRF-IN-X.                               \n018550             15  TDB-TDAC-IRA-TRF-IN       PIC S9(15)V9(2).       \n018552         10  TDB-TDAC-IRA-TRF-OUT-X.                              \n018554             15  TDB-TDAC-IRA-TRF-OUT      PIC S9(15)V9(2).       \n018556         10  TDB-TDAC-IRA-FAIR-MKT-X.                             \n018558             15  TDB-TDAC-IRA-FAIR-MKT     PIC S9(15)V9(2).       \n018560         10  TDB-TDAC-CIF-REMARK           PIC X.                 \n018562         10  TDB-TDAC-CD-ST-WHLD-X.                               \n018564             15  TDB-TDAC-CD-ST-WHLD       PIC S9(15)V9(2).       \n018566         10  TDB-TDAC-IRA-ST-WHLD-X.                              \n018568             15  TDB-TDAC-IRA-ST-WHLD      PIC S9(15)V9(2).       \n018570         10  TDB-TDAC-CURR-YR-AMT-X.                              \n018572             15  TDB-TDAC-CURR-YR-AMT      PIC S9(15)V9(2)        \n018574                                               OCCURS 12 TIMES.   \n018576         10  TDB-TDAC-LAST-YR-AMT-X.                              \n018578             15  TDB-TDAC-LAST-YR-AMT      PIC S9(15)V9(2)        \n018580                                               OCCURS 12 TIMES.   \n018582         10  TDB-TDAC-TIN-CD-2-X.                                 \n018584             15  TDB-TDAC-TIN-CD-2         PIC X(01).             \n018586         10  TDB-TDAC-TIN-CRT-CD-2-X.                             \n018588             15  TDB-TDAC-TIN-CRT-CD-2     PIC 9(01).             \n018590         10  TDB-TDAC-TIN-CRT-DT-2-X.                             \n018592             15  TDB-TDAC-TIN-CRT-DT-2     PIC 9(08).             \n018594         10  TDB-TDAC-TIN-NBR-2-X.                                \n018596             15  TDB-TDAC-TIN-NBR-2        PIC 9(09).             \n018598         10  TDB-TDAC-TIN-CD-3             PIC X(01).             \n018600         10  TDB-TDAC-TIN-CRT-CD-3         PIC 9(01).             \n018602         10  TDB-TDAC-TIN-CRT-DT-3         PIC 9(08).             \n018604         10  TDB-TDAC-TIN-NBR-3            PIC 9(09).             \n018606         10  TDB-TDAC-NAICS-CD-X.                                 \n018608             15  TDB-TDAC-NAICS-CD         PIC 9(06).             \n018610         10  TDB-TDAC-CIF-PASS-THR-X.                             \n018612             15  TDB-TDAC-CIF-PASS-THR     PIC 9(01).             \n018614         10  TDB-TDAC-EMAIL-NTC-X.                                \n018616             15  TDB-TDAC-EMAIL-NTC        PIC 9(01).             \n018618         10  TDB-TDAC-RMD-YR-AMT           PIC S9(15)V9(2).       \n018620         10  TDB-TDAC-ADDR-CHG-DT-X.                              \n018622             15  TDB-TDAC-ADDR-CHG-DT      PIC 9(08).             \n018624         10  TDB-TDAC-WTHLD-CD             PIC 9(01).             \n018626         10  TDB-TDAC-ST-WHLD-CD           PIC 9(01).             \n018628         10  TDB-TDAC-WTHLD-AMT            PIC S9(12)V9(2).       \n018630         10  TDB-TDAC-ST-WHLD-AMT          PIC S9(12)V9(2).       \n018632         10  TDB-TDAC-FOREIGN-LANG         PIC X(01).             \n018634         10  TDB-TDAC-L-ROLLOVR-DT         PIC 9(08).             \n018636         10  TDB-TDAC-CUSTM-FIELDS         PIC 9(01).             \n018638         10  TDB-TDAC-LLC-NAME             PIC X(40).             \n018640         10  TDB-TDAC-LLC-TIN-CD           PIC X(01).             \n018642         10  TDB-TDAC-LLC-TIN              PIC 9(09).             \n018644         10  TDB-TDAC-FOREIGN-PHN          PIC X(20).             \n018646                                                                  \n018648     05  TDB-TDAACCT.                                             \n018650         10  TDB-TDAA-BANK-X.                                     \n018652             15  TDB-TDAA-BANK             PIC 9(4).              \n018654         10  TDB-TDAA-BRCH-X.                                     \n018656             15  TDB-TDAA-BRCH             PIC 9(4).              \n018658         10  TDB-TDAA-APPL-X.                                     \n018660             15  TDB-TDAA-APPL             PIC 9(1).              \n018662         10  TDB-TDAA-CUST-X.                                     \n018664             15  TDB-TDAA-CUST             PIC 9(12).             \n018666         10  TDB-TDAA-ACCT-X.                                     \n018668             15  TDB-TDAA-ACCT             PIC 9(10).             \n018670         10  TDB-TDAA-STATUS               PIC X(1).              \n018672         10  TDB-TDAA-IRA-TYPE-X.                                 \n018674             15  TDB-TDAA-IRA-TYPE         PIC 9(2).              \n018676         10  TDB-TDAA-ACCT-OPTION-X.                              \n018678             15  TDB-TDAA-ACCT-OPTION      PIC 9(2).              \n018680         10  TDB-TDAA-DT-CONDENSED-X.                             \n018682             15  TDB-TDAA-DT-CONDENSED     PIC 9(8).              \n018684         10  TDB-TDAA-CERT-X.                                     \n018686             15  TDB-TDAA-CERT             PIC 9(7).              \n018688         10  TDB-TDAA-SHT-NAME             PIC X(20).             \n018690         10  TDB-TDAA-TITLE                PIC X(40).             \n018692         10  TDB-TDAA-TITLE-PRINT          PIC X(1).              \n018694         10  TDB-TDAA-ADDR-USAGE           PIC X(01).             \n018696         10  TDB-TDAA-ADDR-ALT             PIC X(01).             \n018698         10  TDB-TDAA-ADDR-TEMP            PIC X(01).             \n018700         10  TDB-TDAA-TEMP-BEG-DT          PIC 9(04).             \n018702         10  TDB-TDAA-TEMP-END-DT          PIC 9(04).             \n018704         10  TDB-TDAA-TEMP-EFF-DT          PIC 9(08).             \n018706         10  TDB-TDAA-TEMP-EXP-DT          PIC 9(08).             \n018708         10  TDB-TDAA-END-OF-INT-X.                               \n018710             15  TDB-TDAA-END-OF-INT       PIC 9(1).              \n018712         10  TDB-TDAA-END-OF-MAT-X.                               \n018714             15  TDB-TDAA-END-OF-MAT       PIC 9(1).              \n018716         10  TDB-TDAA-END-OF-STMT-X.                              \n018718             15  TDB-TDAA-END-OF-STMT      PIC 9(1).              \n018720         10  TDB-TDAA-END-OF-CMPD-X.                              \n018722             15  TDB-TDAA-END-OF-CMPD      PIC 9(1).              \n018724         10  TDB-TDAA-END-OF-FEE-X.                               \n018726             15  TDB-TDAA-END-OF-FEE       PIC 9(1).              \n018728         10  TDB-TDAA-OFFICER              PIC X(3).              \n018730         10  TDB-TDAA-OFFICER-2            PIC X(3).              \n018732         10  TDB-TDAA-OFFICER-3            PIC X(3).              \n018734         10  TDB-TDAA-FREE-MARK            PIC X(24).             \n018736         10  TDB-TDAA-CLASS-CD             PIC X(1).              \n018738         10  TDB-TDAA-CORR-BK-CD           PIC X(1).              \n018740         10  TDB-TDAA-PUBLIC-FUND          PIC X(1).              \n018742         10  TDB-TDAA-TRUST-CD             PIC X(1).              \n018744         10  TDB-TDAA-RT-CHG-ALLOW-X.                             \n018746             15  TDB-TDAA-RT-CHG-ALLOW     PIC 9(1).              \n018748         10  TDB-TDAA-WTHDRW-ALLOW-X.                             \n018750             15  TDB-TDAA-WTHDRW-ALLOW     PIC 9(1).              \n018752         10  TDB-TDAA-DPOSIT-ALLOW-X.                             \n018754             15  TDB-TDAA-DPOSIT-ALLOW     PIC 9(1).              \n018756         10  TDB-TDAA-POST-MAT-X.                                 \n018758             15  TDB-TDAA-POST-MAT         PIC 9(1).              \n018760         10  TDB-TDAA-RT-FLOOR-X.                                 \n018762             15  TDB-TDAA-RT-FLOOR         PIC 9(1).              \n018764         10  TDB-TDAA-REPO-CD-X.                                  \n018766             15  TDB-TDAA-REPO-CD          PIC 9(1).              \n018768         10  TDB-TDAA-TOTAL-CD-X.                                 \n018770             15  TDB-TDAA-TOTAL-CD         PIC 9(3).              \n018772         10  TDB-TDAA-REN-TOTAL-CD-X.                             \n018774             15  TDB-TDAA-REN-TOTAL-CD     PIC 9(3).              \n018776         10  TDB-TDAA-ORG-TOTAL-CD         PIC 9(3).              \n018778         10  TDB-TDAA-INQ-SECR-CD-X.                              \n018780             15  TDB-TDAA-INQ-SECR-CD      PIC 9(1).              \n018782         10  TDB-TDAA-MAIL-CD-X.                                  \n018784             15  TDB-TDAA-MAIL-CD          PIC 9(1).              \n018786         10  TDB-TDAA-WTHD-REQD-CD-X.                             \n018788             15  TDB-TDAA-WTHD-REQD-CD     PIC 9(1).              \n018790         10  TDB-TDAA-TICKLER-FLAG-X.                             \n018792             15  TDB-TDAA-TICKLER-FLAG     PIC 9.                 \n018794         10  TDB-TDAA-DISP-CD-X.                                  \n018796             15  TDB-TDAA-DISP-CD          PIC 9(1).              \n018798         10  TDB-TDAA-CLS-DISP-CD          PIC 9(1).              \n018800         10  TDB-TDAA-DIST-STATUS-X.                              \n018802             15  TDB-TDAA-DIST-STATUS      PIC 9(1).              \n018804         10  TDB-TDAA-COMM-ACCT-X.                                \n018806             15  TDB-TDAA-COMM-ACCT        PIC 9(1).              \n018808         10  TDB-TDAA-RENEW-CD-X.                                 \n018810             15  TDB-TDAA-RENEW-CD         PIC 9(1).              \n018812         10  TDB-TDAA-PLEDGE-CD            PIC X(1).              \n018814         10  TDB-TDAA-NEGOT-CD             PIC X(1).              \n018816         10  TDB-TDAA-BENEF-CD-X.                                 \n018818             15  TDB-TDAA-BENEF-CD         PIC 9(1).              \n018820         10  TDB-TDAA-COMM-MAT-CD-X.                              \n018822             15  TDB-TDAA-COMM-MAT-CD      PIC 9(1).              \n018824         10  TDB-TDAA-NBR-BENEF-X.                                \n018826             15  TDB-TDAA-NBR-BENEF        PIC 9(1).              \n018828         10  TDB-TDAA-OVERRIDE-X.                                 \n018830             15  TDB-TDAA-OVERRIDE         PIC 9(1).              \n018832         10  TDB-TDAA-INT-CD-X.                                   \n018834             15  TDB-TDAA-INT-CD           PIC 9(1).              \n018836         10  TDB-TDAA-WTHLD-CD-X.                                 \n018838             15  TDB-TDAA-WTHLD-CD         PIC 9(1).              \n018840         10  TDB-TDAA-WTHLD-AMT-X.                                \n018842             15  TDB-TDAA-WTHLD-AMT        PIC S9(12)V9(2).       \n018844         10  TDB-TDAA-IGL-GRP-X.                                  \n018846             15  TDB-TDAA-IGL-GRP          PIC 9(2).              \n018848         10  TDB-TDAA-SUM-STMT-CD-X.                              \n018850             15  TDB-TDAA-SUM-STMT-CD      PIC 9(1).              \n018852         10  TDB-TDAA-REN-NTC-CD-X.                               \n018854             15  TDB-TDAA-REN-NTC-CD       PIC 9(1).              \n018856         10  TDB-TDAA-PMAT-NTC-CD-X.                              \n018858             15  TDB-TDAA-PMAT-NTC-CD      PIC 9(1).              \n018860         10  TDB-TDAA-RTCHG-NTC-CD-X.                             \n018862             15  TDB-TDAA-RTCHG-NTC-CD     PIC 9(1).              \n018864         10  TDB-TDAA-INT-NTC-CD-X.                               \n018866             15  TDB-TDAA-INT-NTC-CD       PIC 9(1).              \n018868         10  TDB-TDAA-CHG-NTC-X.                                  \n018870             15  TDB-TDAA-CHG-NTC          PIC 9(1).              \n018872         10  TDB-TDAA-YIELD-NUM-X.                                \n018874             15  TDB-TDAA-YIELD-NUM        PIC 9(3).              \n018876         10  TDB-TDAA-YIELD-DENOM-X.                              \n018878             15  TDB-TDAA-YIELD-DENOM      PIC 9(3).              \n018880         10  TDB-TDAA-CMPD-FREQ-X.                                \n018882             15  TDB-TDAA-CMPD-FREQ        PIC 9(1).              \n018884         10  TDB-TDAA-CMPD-NTRVL-X.                               \n018886             15  TDB-TDAA-CMPD-NTRVL       PIC 9(4).              \n018888         10  TDB-TDAA-RT-CHG-LIMIT-X.                             \n018890             15  TDB-TDAA-RT-CHG-LIMIT     PIC 9(1).              \n018892         10  TDB-TDAA-VAR-RT-IMMED-X.                             \n018894             15  TDB-TDAA-VAR-RT-IMMED     PIC 9(1).              \n018896         10  TDB-TDAA-VAR-RT-INT-X.                               \n018898             15  TDB-TDAA-VAR-RT-INT       PIC 9(1).              \n018900         10  TDB-TDAA-VAR-RT-SCHED-X.                             \n018902             15  TDB-TDAA-VAR-RT-SCHED     PIC 9(1).              \n018904         10  TDB-TDAA-VAR-RT-CUST-X.                              \n018906             15  TDB-TDAA-VAR-RT-CUST      PIC 9(1).              \n018908         10  TDB-TDAA-VAR-RT-BAL-X.                               \n018910             15  TDB-TDAA-VAR-RT-BAL       PIC 9(1).              \n018912         10  TDB-TDAA-RT-INDX-CD-X.                               \n018914             15  TDB-TDAA-RT-INDX-CD       PIC 9(2).              \n018916         10  TDB-TDAA-R-RT-INDX-CD         PIC XX.                \n018918         10  TDB-TDAA-RT-MARG-CD-X.                               \n018920             15  TDB-TDAA-RT-MARG-CD       PIC 9(2).              \n018922         10  TDB-TDAA-R-RT-MARG-CD         PIC XX.                \n018924         10  TDB-TDAA-RT-TIER-CD-X.                               \n018926             15  TDB-TDAA-RT-TIER-CD       PIC 9(2).              \n018928         10  TDB-TDAA-R-RT-TIER-CD         PIC XX.                \n018930         10  TDB-TDAA-RT-SR-CD-X.                                 \n018932             15  TDB-TDAA-RT-SR-CD         PIC 9(2).              \n018934         10  TDB-TDAA-R-RT-SR-CD           PIC XX.                \n018936         10  TDB-TDAA-RT-REGN-CD-X.                               \n018938             15  TDB-TDAA-RT-REGN-CD       PIC 9(2).              \n018940         10  TDB-TDAA-RT-CHG-NTRVL-X.                             \n018942             15  TDB-TDAA-RT-CHG-NTRVL     PIC 9(3).              \n018944         10  TDB-TDAA-CAP-RT-CHG           PIC X.                 \n018946         10  TDB-TDAA-R-TIER-RT-CH         PIC X.                 \n018948         10  TDB-TDAA-ALERT-CD-X.                                 \n018950             15  TDB-TDAA-ALERT-CD         PIC 9(2).              \n018952         10  TDB-TDAA-ALERT-CD-2           PIC 9(2).              \n018954         10  TDB-TDAA-ALERT-CD-3           PIC 9(2).              \n018956         10  TDB-TDAA-CENSUS-TRACT-X.                             \n018958             15  TDB-TDAA-CENSUS-TRACT     PIC 9(4)V9(2).         \n018960         10  TDB-TDAA-MK-SEGMENT           PIC X(2).              \n018962         10  TDB-TDAA-BK-DEF-TOT           PIC X(3).              \n018964         10  TDB-TDAA-BK-DEF-CD1           PIC X(1).              \n018966         10  TDB-TDAA-BK-DEF-CD2           PIC X(1).              \n018968         10  TDB-TDAA-BK-DEF-CD3           PIC X(1).              \n018970         10  TDB-TDAA-BK-DEF-CD4           PIC X(1).              \n018972         10  TDB-TDAA-BK-DEF-CD5           PIC X(1).              \n018974         10  TDB-TDAA-OID-METH-X.                                 \n018976             15  TDB-TDAA-OID-METH         PIC 9(1).              \n018978         10  TDB-TDAA-EOY-CD-X.                                   \n018980             15  TDB-TDAA-EOY-CD           PIC 9(1).              \n018982         10  TDB-TDAA-B-NOTC-YR1-X.                               \n018984             15  TDB-TDAA-B-NOTC-YR1       PIC 9(1).              \n018986         10  TDB-TDAA-B-NOTC-YR2-X.                               \n018988             15  TDB-TDAA-B-NOTC-YR2       PIC 9(1).              \n018990         10  TDB-TDAA-B-NOTC-YR3-X.                               \n018992             15  TDB-TDAA-B-NOTC-YR3       PIC 9(1).              \n018994         10  TDB-TDAA-NO-COMB-IRS-X.                              \n018996             15  TDB-TDAA-NO-COMB-IRS      PIC 9(1).              \n018998         10  TDB-TDAA-PENLTY-CD-X.                                \n019000             15  TDB-TDAA-PENLTY-CD        PIC 999.               \n019002         10  TDB-TDAA-MONEY-SRC-CD         PIC X(1).              \n019004         10  TDB-TDAA-INTERNET-CD.                                \n019006             15  TDB-TDAA-INTERNET-BPY-X.                         \n019008                 20  TDB-TDAA-INTERNET-BPY PIC 9(1).              \n019010             15  TDB-TDAA-INTERNET-TFR-X.                         \n019012                 20  TDB-TDAA-INTERNET-TFR PIC 9(1).              \n019014             15  TDB-TDAA-INTERNET-INQ-X.                         \n019016                 20  TDB-TDAA-INTERNET-INQ PIC 9(1).              \n019018         10  TDB-TDAA-IRA-BACKED-X.                               \n019020             15  TDB-TDAA-IRA-BACKED       PIC 9(1).              \n019022         10  TDB-TDAA-SAV-DEPOSIT          PIC 9(1).              \n019024         10  TDB-TDAA-MAT-TYPE-X.                                 \n019026             15  TDB-TDAA-MAT-TYPE         PIC 9(1).              \n019028         10  TDB-TDAA-MAT-TERM-X.                                 \n019030             15  TDB-TDAA-MAT-TERM         PIC 9(4).              \n019032         10  TDB-TDAA-ORG-MAT-TYPE-X.                             \n019034             15  TDB-TDAA-ORG-MAT-TYPE     PIC 9(1).              \n019036         10  TDB-TDAA-ORG-MAT-TERM-X.                             \n019038             15  TDB-TDAA-ORG-MAT-TERM     PIC 9(4).              \n019040         10  TDB-TDAA-ODD-PAYMENT-X.                              \n019042             15  TDB-TDAA-ODD-PAYMENT      PIC 9(1).              \n019044         10  TDB-TDAA-PAY-FREQ-X.                                 \n019046             15  TDB-TDAA-PAY-FREQ         PIC 9(1).              \n019048         10  TDB-TDAA-PAY-NTRVL-X.                                \n019050             15  TDB-TDAA-PAY-NTRVL        PIC 9(4).              \n019052         10  TDB-TDAA-FEE-FREQ-X.                                 \n019054             15  TDB-TDAA-FEE-FREQ         PIC 9(1).              \n019056         10  TDB-TDAA-FEE-NTRVL-X.                                \n019058             15  TDB-TDAA-FEE-NTRVL        PIC 9(4).              \n019060         10  TDB-TDAA-STMT-FREQ-X.                                \n019062             15  TDB-TDAA-STMT-FREQ        PIC 9(1).              \n019064         10  TDB-TDAA-STMT-NTRVL-X.                               \n019066             15  TDB-TDAA-STMT-NTRVL       PIC 9(4).              \n019068         10  TDB-TDAA-EMPLOYEE-ID          PIC X(8).              \n019070         10  TDB-TDAA-EFT-CARD             PIC X(1).              \n019072         10  TDB-TDAA-PEN-WAV-RESN         PIC X(1).              \n019074         10  TDB-TDAA-CLOSED-RESN          PIC X(1).              \n019076         10  TDB-TDAA-SPECIAL-STMT-X.                             \n019078             15  TDB-TDAA-SPECIAL-STMT     PIC 9(1).              \n019080         10  TDB-TDAA-CLS-THIS-MTH-X.                             \n019082             15  TDB-TDAA-CLS-THIS-MTH     PIC 9(1).              \n019084         10  TDB-TDAA-RC-MAT-ONLY          PIC 9(1).              \n019086         10  TDB-TDAA-GRACE-DAYS           PIC 9(2).              \n019088         10  TDB-TDAA-CLS-ON-MAT           PIC 9(1).              \n019090         10  TDB-TDAA-DDA-ACCT-1-X.                               \n019092             15  TDB-TDAA-DDA-ACCT-1       PIC 9(12).             \n019094         10  TDB-TDAA-DDA-ACCT-1-S-X.                             \n019096             15  TDB-TDAA-DDA-ACCT-1-S     PIC 9(10).             \n019098         10  TDB-TDAA-DDA-ACCT-2-X.                               \n019100             15  TDB-TDAA-DDA-ACCT-2       PIC 9(12).             \n019102         10  TDB-TDAA-DDA-ACCT-2-S-X.                             \n019104             15  TDB-TDAA-DDA-ACCT-2-S     PIC 9(10).             \n019106         10  TDB-TDAA-DDA-ACCT-3-X.                               \n019108             15  TDB-TDAA-DDA-ACCT-3       PIC 9(12).             \n019110         10  TDB-TDAA-DDA-ACCT-3-S-X.                             \n019112             15  TDB-TDAA-DDA-ACCT-3-S     PIC 9(10).             \n019114         10  TDB-TDAA-INT-ACCT-X.                                 \n019116             15  TDB-TDAA-INT-ACCT         PIC 9(12).             \n019118         10  TDB-TDAA-INT-ACCT-S-X.                               \n019120             15  TDB-TDAA-INT-ACCT-S       PIC 9(10).             \n019122         10  TDB-TDAA-CS-ACCT-X.                                  \n019124             15  TDB-TDAA-CS-ACCT          PIC 9(12).             \n019126         10  TDB-TDAA-CS-ACCT-S-X.                                \n019128             15  TDB-TDAA-CS-ACCT-S        PIC 9(10).             \n019130         10  TDB-TDAA-CC-ACCT-X.                                  \n019132             15  TDB-TDAA-CC-ACCT          PIC 9(12).             \n019134         10  TDB-TDAA-LNS-BORROWER-X.                             \n019136             15  TDB-TDAA-LNS-BORROWER     PIC 9(12).             \n019138         10  TDB-TDAA-LNS-NOTE-X.                                 \n019140             15  TDB-TDAA-LNS-NOTE         PIC 9(10).             \n019142         10  TDB-TDAA-CNV-OLD-ACCT         PIC X(15).             \n019144         10  TDB-TDAA-CLS-ACCT             PIC 9(12).             \n019146         10  TDB-TDAA-CLS-ACCT-S           PIC 9(10).             \n019148         10  TDB-TDAA-DAYS-IN-PER-X.                              \n019150             15  TDB-TDAA-DAYS-IN-PER      PIC 9(5).              \n019152         10  TDB-TDAA-RR-CYC-NBR-X.                               \n019154             15  TDB-TDAA-RR-CYC-NBR       PIC 9(2).              \n019156         10  TDB-TDAA-CR-CNT-STD-X.                               \n019158             15  TDB-TDAA-CR-CNT-STD       PIC 9(5).              \n019160         10  TDB-TDAA-CR-AMT-STD-X.                               \n019162             15  TDB-TDAA-CR-AMT-STD       PIC S9(12)V9(2).       \n019164         10  TDB-TDAA-DB-CNT-STD-X.                               \n019166             15  TDB-TDAA-DB-CNT-STD       PIC 9(5).              \n019168         10  TDB-TDAA-DB-AMT-STD-X.                               \n019170             15  TDB-TDAA-DB-AMT-STD       PIC S9(12)V9(2).       \n019172         10  TDB-TDAA-CR-CNT-YTD-X.                               \n019174             15  TDB-TDAA-CR-CNT-YTD       PIC 9(5).              \n019176         10  TDB-TDAA-CR-AMT-YTD-X.                               \n019178             15  TDB-TDAA-CR-AMT-YTD       PIC S9(12)V9(2).       \n019180         10  TDB-TDAA-DB-CNT-YTD-X.                               \n019182             15  TDB-TDAA-DB-CNT-YTD       PIC 9(5).              \n019184         10  TDB-TDAA-DB-AMT-YTD-X.                               \n019186             15  TDB-TDAA-DB-AMT-YTD       PIC S9(12)V9(2).       \n019188         10  TDB-TDAA-DAYS-IN-TERM-X.                             \n019190             15  TDB-TDAA-DAYS-IN-TERM     PIC 9(5).              \n019192         10  TDB-TDAA-BEG-INT-BAL-X.                              \n019194             15  TDB-TDAA-BEG-INT-BAL      PIC S9(12)V9(2).       \n019196         10  TDB-TDAA-PURCH-AMT-X.                                \n019198             15  TDB-TDAA-PURCH-AMT        PIC S9(12)V9(2).       \n019200         10  TDB-TDAA-CURR-BAL-X.                                 \n019202             15  TDB-TDAA-CURR-BAL         PIC S9(12)V9(2).       \n019204         10  TDB-TDAA-AVAIL-BAL-X.                                \n019206             15  TDB-TDAA-AVAIL-BAL        PIC S9(12)V9(2).       \n019208         10  TDB-TDAA-BAL-BEG-MAT-X.                              \n019210             15  TDB-TDAA-BAL-BEG-MAT      PIC S9(12)V9(2).       \n019212         10  TDB-TDAA-CLOSE-AMT-X.                                \n019214             15  TDB-TDAA-CLOSE-AMT        PIC S9(12)V9(2).       \n019216         10  TDB-TDAA-MONEY-AMT-X.                                \n019218             15  TDB-TDAA-MONEY-AMT        PIC S9(12)V9(2).       \n019220         10  TDB-TDAA-BAL-BEG-STMT-X.                             \n019222             15  TDB-TDAA-BAL-BEG-STMT     PIC S9(12)V9(2).       \n019224         10  TDB-TDAA-ACCR-INT-X.                                 \n019226             15  TDB-TDAA-ACCR-INT         PIC S9(12)V9(6).       \n019228         10  TDB-TDAA-ANTIC-INT-X.                                \n019230             15  TDB-TDAA-ANTIC-INT        PIC S9(12)V9(2).       \n019232         10  TDB-TDAA-INT-TO-POST-X.                              \n019234             15  TDB-TDAA-INT-TO-POST      PIC S9(12)V9(2).       \n019236         10  TDB-TDAA-1099-YTD-X.                                 \n019238             15  TDB-TDAA-1099-YTD         PIC S9(12)V9(2).       \n019240         10  TDB-TDAA-1099-LST-YR-X.                              \n019242             15  TDB-TDAA-1099-LST-YR      PIC S9(12)V9(2).       \n019244         10  TDB-TDAA-CURR-PENLTY-X.                              \n019246             15  TDB-TDAA-CURR-PENLTY      PIC S9(12)V9(2).       \n019248         10  TDB-TDAA-PENLTY-STD-X.                               \n019250             15  TDB-TDAA-PENLTY-STD       PIC S9(12)V9(2).       \n019252         10  TDB-TDAA-PENLTY-YTD-X.                               \n019254             15  TDB-TDAA-PENLTY-YTD       PIC S9(12)V9(2).       \n019256         10  TDB-TDAA-LST-PENLTY-X.                               \n019258             15  TDB-TDAA-LST-PENLTY       PIC S9(12)V9(2).       \n019260         10  TDB-TDAA-CURR-INT-ADJ-X.                             \n019262             15  TDB-TDAA-CURR-INT-ADJ     PIC S9(12)V9(2).       \n019264         10  TDB-TDAA-TOTAMT-HOLDS-X.                             \n019266             15  TDB-TDAA-TOTAMT-HOLDS     PIC S9(12)V9(2).       \n019268         10  TDB-TDAA-NXT-INT-ADJ-X.                              \n019270             15  TDB-TDAA-NXT-INT-ADJ      PIC S9(12)V9(2).       \n019272         10  TDB-TDAA-FEE-AMT-X.                                  \n019274             15  TDB-TDAA-FEE-AMT          PIC S9(12)V9(2).       \n019276         10  TDB-TDAA-OID-RPT-INT-X.                              \n019278             15  TDB-TDAA-OID-RPT-INT      PIC S9(12)V9(2).       \n019280         10  TDB-TDAA-FAIR-MRKT-X.                                \n019282             15  TDB-TDAA-FAIR-MRKT        PIC S9(12)V9(2).       \n019284         10  TDB-TDAA-CUR-WHLD-AMT-X.                             \n019286             15  TDB-TDAA-CUR-WHLD-AMT     PIC S9(12)V9(2).       \n019288         10  TDB-TDAA-LST-WHLD-AMT-X.                             \n019290             15  TDB-TDAA-LST-WHLD-AMT     PIC S9(12)V9(2).       \n019292         10  TDB-TDAA-WTHLD-STD-X.                                \n019294             15  TDB-TDAA-WTHLD-STD        PIC S9(12)V9(2).       \n019296         10  TDB-TDAA-WTHLD-YTD-X.                                \n019298             15  TDB-TDAA-WTHLD-YTD        PIC S9(12)V9(2).       \n019300         10  TDB-TDAA-LST-INT-PMT-X.                              \n019302             15  TDB-TDAA-LST-INT-PMT      PIC S9(12)V9(2).       \n019304         10  TDB-TDAA-BAL-BEG-YR-X.                               \n019306             15  TDB-TDAA-BAL-BEG-YR       PIC S9(12)V9(2).       \n019308         10  TDB-TDAA-BAL-AT-CONV-X.                              \n019310             15  TDB-TDAA-BAL-AT-CONV      PIC S9(12)V9(2).       \n019312         10  TDB-TDAA-BAL-BEG-LYR-X.                              \n019314             15  TDB-TDAA-BAL-BEG-LYR      PIC S9(12)V9(2).       \n019316         10  TDB-TDAA-MIN-BAL-STD-X.                              \n019318             15  TDB-TDAA-MIN-BAL-STD      PIC S9(12)V9(2).       \n019320         10  TDB-TDAA-MIN-BAL-YTD-X.                              \n019322             15  TDB-TDAA-MIN-BAL-YTD      PIC S9(12)V9(2).       \n019324         10  TDB-TDAA-MAX-BAL-YTD          PIC S9(12)V9(2).       \n019326         10  TDB-TDAA-LMINBAL-STD-X.                              \n019328             15  TDB-TDAA-LMINBAL-STD      PIC S9(12)V9(2).       \n019330         10  TDB-TDAA-CMPD-INT-X.                                 \n019332             15  TDB-TDAA-CMPD-INT         PIC S9(12)V9(2).       \n019334         10  TDB-TDAA-PER-DIEM-X.                                 \n019336             15  TDB-TDAA-PER-DIEM         PIC S9(12)V9(6).       \n019338         10  TDB-TDAA-AVG-PER-DIEM-X.                             \n019340             15  TDB-TDAA-AVG-PER-DIEM     PIC S9(12)V9(6).       \n019342         10  TDB-TDAA-EMAIL-MAXAMT-X.                             \n019344             15  TDB-TDAA-EMAIL-MAXAMT     PIC 9(10).             \n019346         10  TDB-TDAA-EMAIL-MINAMT-X.                             \n019348             15  TDB-TDAA-EMAIL-MINAMT     PIC 9(10).             \n019350         10  TDB-TDAA-DTH-FAIRMKT-X.                              \n019352             15  TDB-TDAA-DTH-FAIRMKT      PIC S9(12)V9(2).       \n019354         10  TDB-TDAA-PENLTY-WAIVE-X.                             \n019356             15  TDB-TDAA-PENLTY-WAIVE     PIC S9(12)V9(2).       \n019358         10  TDB-TDAA-BEG-INT-RT-X.                               \n019360             15  TDB-TDAA-BEG-INT-RT       PIC 9(2)V9(3).         \n019362         10  TDB-TDAA-CUR-INT-RT-X.                               \n019364             15  TDB-TDAA-CUR-INT-RT       PIC 9(2)V9(3).         \n019366         10  TDB-TDAA-FLOOR-RT-X.                                 \n019368             15  TDB-TDAA-FLOOR-RT         PIC 9(2)V9(3).         \n019370         10  TDB-TDAA-FLOOR-INCR-X.                               \n019372             15  TDB-TDAA-FLOOR-INCR       PIC 9(2)V9(3).         \n019374         10  TDB-TDAA-YIELD-RT-X.                                 \n019376             15  TDB-TDAA-YIELD-RT         PIC 9(2)V9(3).         \n019378         10  TDB-TDAA-RISE-RATE-X.                                \n019380             15  TDB-TDAA-RISE-RATE        PIC 9(2)V9(3)          \n019382                               OCCURS   10.                       \n019384         10  TDB-TDAA-LNS-INCRMNT-X.                              \n019386             15  TDB-TDAA-LNS-INCRMNT      PIC 9(2)V9(4).         \n019388         10  TDB-TDAA-RT-VARIANCE-X.                              \n019390             15  TDB-TDAA-RT-VARIANCE      PIC S9(1)V9(2).        \n019392         10  TDB-TDAA-CONST-RT-ADJ         PIC S9(2)V9(3).        \n019394         10  TDB-TDAA-RATE-AT-EOY-X.                              \n019396             15  TDB-TDAA-RATE-AT-EOY      PIC 9(2)V9(3).         \n019398         10  TDB-TDAA-RATE-LST-STM-X.                             \n019400             15  TDB-TDAA-RATE-LST-STM     PIC 9(2)V9(3).         \n019402         10  TDB-TDAA-ORG-YIELD-RT-X.                             \n019404             15  TDB-TDAA-ORG-YIELD-RT     PIC 9(2)V9(3).         \n019406         10  TDB-TDAA-REN-YIELD-RT-X.                             \n019408             15  TDB-TDAA-REN-YIELD-RT     PIC 9(2)V9(3).         \n019410         10  TDB-TDAA-SCHED-DT-X.                                 \n019412             15  TDB-TDAA-SCHED-DT         PIC 9(8).              \n019414         10  TDB-TDAA-ACCR-DT-X.                                  \n019416             15  TDB-TDAA-ACCR-DT          PIC 9(8).              \n019418         10  TDB-TDAA-OPEN-DT-X.                                  \n019420             15  TDB-TDAA-OPEN-DT          PIC 9(8).              \n019422         10  TDB-TDAA-CLSD-DT-X.                                  \n019424             15  TDB-TDAA-CLSD-DT          PIC 9(8).              \n019426         10  TDB-TDAA-LST-MAT-DT-X.                               \n019428             15  TDB-TDAA-LST-MAT-DT       PIC 9(8).              \n019430         10  TDB-TDAA-LST-POST-DT-X.                              \n019432             15  TDB-TDAA-LST-POST-DT      PIC 9(8).              \n019434         10  TDB-TDAA-LST-IN-PROC          PIC 9(8).              \n019436         10  TDB-TDAA-LST-CONTACT-X.                              \n019438             15  TDB-TDAA-LST-CONTACT      PIC 9(8).              \n019440         10  TDB-TDAA-LST-FEE-DT-X.                               \n019442             15  TDB-TDAA-LST-FEE-DT       PIC 9(8).              \n019444         10  TDB-TDAA-LST-RTCHG-DT-X.                             \n019446             15  TDB-TDAA-LST-RTCHG-DT     PIC 9(8).              \n019448         10  TDB-TDAA-LST-DIST-DT-X.                              \n019450             15  TDB-TDAA-LST-DIST-DT      PIC 9(8).              \n019452         10  TDB-TDAA-LST-STMT-DT-X.                              \n019454             15  TDB-TDAA-LST-STMT-DT      PIC 9(8).              \n019456         10  TDB-TDAA-LST-CMPD-DT-X.                              \n019458             15  TDB-TDAA-LST-CMPD-DT      PIC 9(8).              \n019460         10  TDB-TDAA-RR-CYC-DT-X.                                \n019462             15  TDB-TDAA-RR-CYC-DT        PIC 9(8)               \n019464                               OCCURS   10.                       \n019466         10  TDB-TDAA-BNF-BIRTH-DT-X.                             \n019468             15  TDB-TDAA-BNF-BIRTH-DT     PIC 9(8).              \n019470         10  TDB-TDAA-BNF-DEATH-DT-X.                             \n019472             15  TDB-TDAA-BNF-DEATH-DT     PIC 9(8).              \n019474         10  TDB-TDAA-LUPD-DATE-X.                                \n019476             15  TDB-TDAA-LUPD-DATE        PIC 9(8).              \n019478         10  TDB-TDAA-LUPD-TIME-X.                                \n019480             15  TDB-TDAA-LUPD-TIME        PIC 9(6).              \n019482         10  TDB-TDAA-ADD-DT-X.                                   \n019484             15  TDB-TDAA-ADD-DT           PIC 9(8).              \n019486         10  TDB-TDAA-ADD-TM-X.                                   \n019488             15  TDB-TDAA-ADD-TM           PIC 9(6).              \n019490         10  TDB-TDAA-CONV-DT-X.                                  \n019492             15  TDB-TDAA-CONV-DT          PIC 9(8).              \n019494         10  TDB-TDAA-ACT-CLOSE-DT-X.                             \n019496             15  TDB-TDAA-ACT-CLOSE-DT     PIC 9(8).              \n019498         10  TDB-TDAA-LST-TBACT-DT-X.                             \n019500             15  TDB-TDAA-LST-TBACT-DT     PIC 9(8).              \n019502         10  TDB-TDAA-ALERT-EXP-DT         PIC 9(8).              \n019504         10  TDB-TDAA-ALRT2-EXP-DT         PIC 9(8).              \n019506         10  TDB-TDAA-ALRT3-EXP-DT         PIC 9(8).              \n019508         10  TDB-TDAA-NXT-FEE-DT-X.                               \n019510             15  TDB-TDAA-NXT-FEE-DT       PIC 9(8).              \n019512         10  TDB-TDAA-NXT-POST-DT-X.                              \n019514             15  TDB-TDAA-NXT-POST-DT      PIC 9(8).              \n019516         10  TDB-TDAA-NXT-MAT-DT-X.                               \n019518             15  TDB-TDAA-NXT-MAT-DT       PIC 9(8).              \n019520         10  TDB-TDAA-NXT-DIST-DT-X.                              \n019522             15  TDB-TDAA-NXT-DIST-DT      PIC 9(8).              \n019524         10  TDB-TDAA-NXT-RT-CHG-X.                               \n019526             15  TDB-TDAA-NXT-RT-CHG       PIC 9(8).              \n019528         10  TDB-TDAA-NXT-IN-PROC-X.                              \n019530             15  TDB-TDAA-NXT-IN-PROC      PIC 9(8).              \n019532         10  TDB-TDAA-NXT-CMPD-DT-X.                              \n019534             15  TDB-TDAA-NXT-CMPD-DT      PIC 9(8).              \n019536         10  TDB-TDAA-NXT-STMT-DT-X.                              \n019538             15  TDB-TDAA-NXT-STMT-DT      PIC 9(8).              \n019540         10  TDB-TDAA-NXT-DS-PROC-X.                              \n019542             15  TDB-TDAA-NXT-DS-PROC      PIC 9(8).              \n019544         10  TDB-TDAA-ADV-NTC-DT-X.                               \n019546             15  TDB-TDAA-ADV-NTC-DT       PIC 9(8).              \n019548         10  TDB-TDAA-NXT-29YR-DT-X.                              \n019550             15  TDB-TDAA-NXT-29YR-DT      PIC 9(8).              \n019552         10  TDB-TDAA-FAIR-MRKT-DT-X.                             \n019554             15  TDB-TDAA-FAIR-MRKT-DT     PIC 9(8).              \n019556         10  TDB-TDAA-SORT-FIELD-1         PIC X(36).             \n019558         10  TDB-TDAA-SORT-FIELD-2         PIC X(36).             \n019560         10  TDB-TDAA-SORT-FIELD-3         PIC X(36).             \n019562         10  TDB-TDAA-SORT-FIELD-4         PIC X(36).             \n019564         10  TDB-TDAA-CMAT-PUB-ID          PIC X(8).              \n019566         10  TDB-TDAA-MSA-CONTR            PIC 9.                 \n019568         10  TDB-TDAA-MSA-CONTR-LY         PIC 9.                 \n019570         10  TDB-TDAA-AVG-ACCR-INT         PIC S9(12)V9(06).      \n019572         10  TDB-TDAA-LEVEL-PAY-X.                                \n019574             15  TDB-TDAA-LEVEL-PAY        PIC 9.                 \n019576         10  TDB-TDAA-ST-INT-CD-X.                                \n019578             15  TDB-TDAA-ST-INT-CD        PIC 9.                 \n019580         10  TDB-TDAA-ST-WHLD-CD-X.                               \n019582             15  TDB-TDAA-ST-WHLD-CD       PIC 9.                 \n019584         10  TDB-TDAA-ST-WHLD-AMT-X.                              \n019586             15  TDB-TDAA-ST-WHLD-AMT      PIC S9(12)V99.         \n019588         10  TDB-TDAA-ST-CUR-W-AMT-X.                             \n019590             15  TDB-TDAA-ST-CUR-W-AMT     PIC S9(12)V99.         \n019592         10  TDB-TDAA-ST-LST-W-AMT-X.                             \n019594             15  TDB-TDAA-ST-LST-W-AMT     PIC S9(12)V99.         \n019596         10  TDB-TDAA-ST-WHLD-STD-X.                              \n019598             15  TDB-TDAA-ST-WHLD-STD      PIC S9(12)V99.         \n019600         10  TDB-TDAA-ST-WHLD-YTD-X.                              \n019602             15  TDB-TDAA-ST-WHLD-YTD      PIC S9(12)V99.         \n019604         10  TDB-TDAA-CIF-REMARK           PIC X.                 \n019606         10  TDB-TDAA-CSR                  PIC X(03).             \n019608         10  TDB-TDAA-BSA-O-RSK-CD-X.                             \n019610             15  TDB-TDAA-BSA-O-RSK-CD     PIC 9(01).             \n019612         10  TDB-TDAA-BSA-C-RSK-CD-X.                             \n019614             15  TDB-TDAA-BSA-C-RSK-CD     PIC 9(01).             \n019616         10  TDB-TDAA-LRG-TRX-DT-X.                               \n019618             15  TDB-TDAA-LRG-TRX-DT       PIC 9(08).             \n019620         10  TDB-TDAA-HSA-FMLY-IND-X.                             \n019622             15  TDB-TDAA-HSA-FMLY-IND     PIC 9(01).             \n019624         10  TDB-TDAA-STOP-PAY-IND-X.                             \n019626             15  TDB-TDAA-STOP-PAY-IND     PIC 9(01).             \n019628         10  TDB-TDAA-IMG-PG-TYPE-X.                              \n019630             15  TDB-TDAA-IMG-PG-TYPE      PIC X(01).             \n019632         10  TDB-TDAA-CONT-LMT-CLC-X.                             \n019634             15  TDB-TDAA-CONT-LMT-CLC    PIC 9(5)V99.            \n019636         10  TDB-TDAA-CONT-LMT-ENT-X.                             \n019638             15  TDB-TDAA-CONT-LMT-ENT     PIC 9(5)V99.           \n019640         10  TDB-TDAA-MEMO-DB-X.                                  \n019642             15  TDB-TDAA-MEMO-DB          PIC S9(12)V99.         \n019644         10  TDB-TDAA-MEMO-CR-X.                                  \n019646             15  TDB-TDAA-MEMO-CR          PIC S9(12)V99.         \n019648         10  TDB-TDAA-MEMO-DB-2-X.                                \n019650             15  TDB-TDAA-MEMO-DB-2        PIC S9(12)V99.         \n019652         10  TDB-TDAA-MEMO-CR-2-X.                                \n019654             15  TDB-TDAA-MEMO-CR-2        PIC S9(12)V99.         \n019656         10  TDB-TDAA-RT-AT-CONV-X.                               \n019658             15  TDB-TDAA-RT-AT-CONV       PIC 9(2)V9(3).         \n019660         10  TDB-TDAA-ACCR-AT-CONV-X.                             \n019662             15  TDB-TDAA-ACCR-AT-CONV     PIC S9(12)V9(6).       \n019664         10  TDB-TDAA-RT-AT-ACRDT-X.                              \n019666             15  TDB-TDAA-RT-AT-ACRDT      PIC 9(2)V9(3).         \n019668         10  TDB-TDAA-BAL-AT-ACRDT-X.                             \n019670             15  TDB-TDAA-BAL-AT-ACRDT     PIC S9(12)V9(2).       \n019672         10  TDB-TDAA-ZERO-RT-ALLOW-X.                            \n019674             15  TDB-TDAA-ZERO-RT-ALLOW    PIC 9.                 \n019676         10  TDB-TDAA-EMAIL-NTC-X.                                \n019678             15  TDB-TDAA-EMAIL-NTC        PIC 9.                 \n019680         10  TDB-TDAA-EMAIL-STMT-X.                               \n019682             15  TDB-TDAA-EMAIL-STMT       PIC 9.                 \n019684         10  TDB-TDAA-FRAUD-CK-DT-X.                              \n019686             15  TDB-TDAA-FRAUD-CK-DT      PIC 9(8).              \n019688         10  TDB-TDAA-FRAUD-CK-CNT-X.                             \n019690             15  TDB-TDAA-FRAUD-CK-CNT     PIC 9(3).              \n019692         10  TDB-TDAA-FRAUD-CK-AMT-X.                             \n019694             15  TDB-TDAA-FRAUD-CK-AMT     PIC S9(12)V9(2).       \n019696         10  TDB-TDAA-MISC-ACCTNO-X.                              \n019698             15  TDB-TDAA-MISC-ACCTNO      PIC 9(8).              \n019700         10  TDB-TDAA-RMD-MAN-CALC         PIC 9(1).              \n019702         10  TDB-TDAA-RMD-AMOUNT           PIC S9(12)V9(2).       \n019704         10  TDB-TDAA-BROKERAGE-ID         PIC X(10).             \n019706         10  TDB-TDAA-EV-LARGE-TRX         PIC X(01).             \n019708         10  TDB-TDAA-EV-MAT-AMT           PIC S9(12)V9(2).       \n019710         10  TDB-TDAA-EV-DISP-ACCT         PIC 9(22).             \n019712         10  TDB-TDAA-EV-COMP-ACCT         PIC 9(22).             \n019714         10  TDB-TDAA-EV-PUBLIC-ID         PIC X(08).             \n019716         10  TDB-TDAA-EV-MAT-TYPE          PIC X(01).             \n019718         10  TDB-TDAA-EV-INT-TYPE          PIC X(01).             \n019720         10  TDB-TDAA-EV-ACCT-TYP          PIC X(01).             \n019722         10  TDB-TDAA-EV-WHLD-PCT          PIC 9(02).             \n019724         10  TDB-TDAA-EV-NON-ACCR          PIC X(01).             \n019726         10  TDB-TDAA-EV-CLOSED                 PIC X(01).        \n019728         10  TDB-TDAA-EV-CLOSE-MO          PIC X(01).             \n019730         10  TDB-TDAA-EV-OPEN-MO           PIC X(01).             \n019732         10  TDB-TDAA-EV-ANN-INT           PIC S9(12)V9(2).       \n019734         10  TDB-TDAA-EV-ORIG-RT           PIC 9(2)V9(3).         \n019736         10  TDB-TDAA-EV-DLY-INT           PIC S9(12)V9(6).       \n019738         10  TDB-TDAA-EV-INT-PAY           PIC S9(12)V9(6).       \n019740         10  TDB-TDAA-EV-AVAIL-BL          PIC S9(12)V9(2).       \n019742         10  TDB-TDAA-EV-RETAIN            PIC X(01).             \n019744         10  TDB-TDAA-EV-CL-RETAIN         PIC X(01).             \n019746         10  TDB-TDAA-EV-TIMES-REN         PIC 9(05).             \n019748         10  TDB-TDAA-EV-CURR-BAL          PIC S9(12)V9(02).      \n019750         10  TDB-TDAA-MONY-SRC-CD2         PIC X(03).             \n019752         10  TDB-TDAA-INHERIT-IRA          PIC 9(01).             \n019754         10  TDB-TDAA-LIFE-FACTOR          PIC 9(02)V9(1).        \n019756         10  TDB-TDAA-BRKR-DEP-CAT         PIC 9(01).             \n019758         10  TDB-TDAA-LINE-OF-BUS          PIC 9(4).              \n019760         10  TDB-TDAA-1ST-STMT             PIC 9(01).             \n019762         10  TDB-TDAA-POSTAL-CITY          PIC X(40).             \n019764         10  TDB-TDAA-POSTAL-CNTRY         PIC X(02).             \n019766         10  TDB-TDAA-CITIZN-CNTRY         PIC X(02).             \n019768         10  TDB-TDAA-CUSTM-FIELDS         PIC 9(01).             \n019770         10  TDB-TDAA-AVG-STEP-RT          PIC 9(2)V9(3).         \n019772         10  TDB-TDAA-MONITOR-INQ          PIC 9(01).             \n019774         10  TDB-TDAA-IGL-GRP-2            PIC 9(02).             \n019776         10  TDB-TDAA-AGG-DAYS-QTD         PIC 9(03).             \n019778         10  TDB-TDAA-AGG-BAL-QTD          PIC S9(15)V9(2).       \n019780         10  TDB-TDAA-IGL-GRP-3            PIC 9(02).             \n019782         10  TDB-TDAA-ALT-ADDR-EOY         PIC 9(01).             \n019784         10  TDB-TDAA-1042S-TAX-ID         PIC X(22).             \n019786         10  TDB-TDAA-LEC                  PIC X(01).             \n019788         10  TDB-TDAA-BAL-AT-CLOSE         PIC S9(12)V9(2).       \n019790         10  TDB-TDAA-AVL-CAP-INT          PIC S9(6)V9(2).        \n019792         10  TDB-TDAA-FIDM-TR-FUND-X.                             \n019794             15  TDB-TDAA-FIDM-TR-FUND     PIC 9(01).             \n019796         10  TDB-TDAA-IRS-FRM-DLVR-X.                             \n019798             15  TDB-TDAA-IRS-FRM-DLVR     PIC 9(01).             \n019800         10  TDB-TDAA-PROVINCE             PIC X(02).             \n019802         10  TDB-TDAA-PROMOTION            PIC X(25).             \n019804         10  TDB-TDAA-NONDB-FIELDS.                               \n019806             15  TDB-TDAA-DAYS-INTO-PER    PIC 9(5).              \n019808             15  TDB-TDAA-CURR-PAYOFF      PIC S9(9)V9(2).        \n019810             15  TDB-TDAA-MANUAL-RT-X      PIC X(5).              \n019812             15  TDB-TDAA-MANUAL-RT-RE   REDEFINES                \n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 1,063 lines from 8840 to 9902.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 19,
  "total_chunks": 55,
  "start_line": 8840,
  "end_line": 9902,
  "line_count": 1063
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
- Source code length: 84500 characters

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
CHUNK 19 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 8840 to 9902 (1,063 lines)
Chunk Tokens (estimated): ~23,556
Actual Input Tokens: 24,962 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 8840-9902 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 19 of 55 chunks
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
      The source code below is only CHUNK 19 of 55.


=============================================================================
CHUNK 19 SOURCE CODE (Lines 8840-9902)
=============================================================================

```cobol
017688             OLD-TDAPC-BANK-SPECS.                                
017690             15  OLD-TDAPC-CREATE-DT          PIC 9(07).          
017692             15  OLD-TDAPC-CREATE-TM          PIC 9(12).          
017694             15  OLD-TDAPC-DQVISTA            PIC X.              
017696             15  OLD-TDAPC-MSI                PIC X.              
017698             15  OLD-TDAPC-BK-TDA-STAT        PIC X.              
017700             15  OLD-TDAPC-TDA-PILOT REDEFINES                    
017702                 OLD-TDAPC-BK-TDA-STAT        PIC X.              
017704             15  OLD-TDAPC-BK-STATUS          PIC X.              
017706             15  OLD-TDAPC-BR-NO              PIC XX.             
017708             15  OLD-TDAPC-CSI-BR-CODE REDEFINES                  
017710                 OLD-TDAPC-BR-NO              PIC XX.             
017712             15  OLD-TDAPC-BK-PHONE-NUM.                          
017714                 20  OLD-TDAPC-AREA-CODE      PIC XXX.            
017716                 20  OLD-TDAPC-PHONE.                             
017718                     25  OLD-TDAPC-PHONE-1ST-3 PIC XXX.           
017720                     25  OLD-TDAPC-PHONE-LST-4 PIC X(04).         
017722             15  OLD-TDAPC-PHN-NUMBER REDEFINES                   
017724                 OLD-TDAPC-BK-PHONE-NUM       PIC X(10).          
017726             15  OLD-TDAPC-TDA-ADD-DAY        PIC XXX.            
017728             15  OLD-TDAPC-HOLIDAYS           OCCURS 18 TIMES.    
017730                 20  OLD-TDAPC-HOL-MM         PIC XX.             
017732                 20  OLD-TDAPC-HOL-DD         PIC XX.             
017734             15  OLD-TDAPC-FM-SUPPRESS        PIC X.              
017736             15  OLD-TDAPC-RMT-BK-INDICATOR   PIC XX.             
017738             15  OLD-TDAPC-RMT-IND REDEFINES                      
017740                 OLD-TDAPC-RMT-BK-INDICATOR   PIC XX.             
017742             15  OLD-TDAPC-BK-ADDR            PIC X(28).          
017744             15  OLD-TDAPC-BK-ADDR-2          PIC X(27).          
017746             15  OLD-TDAPC-FED-ID             PIC X(10).          
017748             15  OLD-TDAPC-EOY-RPT-SEQ        PIC X.              
017750             15  OLD-TDAPC-EOY-EARLY-RUN      PIC X.              
017752             15  OLD-TDAPC-EOY-RETURN-TO-BK   PIC X.              
017754             15  OLD-TDAPC-EOY-RETURN-TO-BANK REDEFINES           
017756                 OLD-TDAPC-EOY-RETURN-TO-BK   PIC X.              
017758             15  OLD-TDAPC-EOY-IRA-PHONE      PIC 9(10).          
017760             15  OLD-TDAPC-EOY-DELETE-DATE    PIC 9(06).          
017762             15  OLD-TDAPC-EOY-IRA-FICHE      PIC X.              
017764             15  OLD-TDAPC-EOY-IRA-PAPER      PIC X.              
017766             15  OLD-TDAPC-EOY-IRA-STMT-EARLY PIC X.              
017768             15  OLD-TDAPC-NO-IRA-STMTS       PIC 9.              
017770             15  OLD-TDAPC-EOY-IRA-STMT       PIC X.              
017772             15  OLD-TDAPC-EOY-IRA-STMT-PRINT PIC X.              
017774             15  OLD-TDAPC-EOY-EARLY-DATE     PIC 9(06).          
017776             15  OLD-TDAPC-CK21-TDA           PIC X.              
017778             15  OLD-TDAPC-MSI-OV-TDA         PIC X.              
017780             15  OLD-TDAPC-BK-IMG-SERV        PIC X(01).          
017782             15  OLD-TDAPC-EOY-APRIL-DATE     PIC 9(06).          
017784             15  OLD-TDAPC-EOY-COD-CLOSED-RPT PIC X(01).          
017786             15  OLD-TDAPC-PRT-NEW            PIC 9(01).          
017788             15  OLD-TDAPC-IMONITOR           PIC X(01).          
017790             15  OLD-TDAPC-ENTC-TDA           PIC X.              
017792             15  OLD-TDAPC-EV-3RD-PARTY-1     PIC X.              
017794             15  OLD-TDAPC-EV-3RD-PARTY-2     PIC X.              
017796             15  OLD-TDAPC-HSA-LOCATION       PIC X.              
017798             15  OLD-TDAPC-PROFITABILITY      PIC X.              
017800             15  OLD-TDAPC-BANCVUE            PIC X.              
017802             15  OLD-TDAPC-SPECIAL-DL-BILLING PIC X.              
017804             15  OLD-TDAPC-CIF-NAME-ADDR      PIC 9.              
017806             15  OLD-TDAPC-MAIL-ADDR-LINES    PIC X.              
017808             15  OLD-TDAPC-WEB-ENABLED        PIC X(01).          
017810             15  OLD-TDAPC-BRANCH-LENGTH      PIC 9.              
017812             15  OLD-TDAPC-LOB                PIC 9.              
017814             15  OLD-TDAPC-BILL-EDIT-TEMPLATES                    
017816                                              PIC 9.              
017818             15  OLD-TDAPC-MCIF-PRIVACY-OPT                       
017820                                              PIC 9.              
017822             15  OLD-TDAPC-TRAIN-BK-FLG       PIC X.              
017824             15  OLD-TDAPC-EOY-CIB-F-MERD     PIC X(01).          
017826             15  FILLER                       PIC X(39).          
017828             15  OLD-TDAPC-LAST-EOM-PROC      PIC 9(08).          
017830             15  OLD-TDAPC-BUS-DT-AFT-NX      PIC 9(08).          
017832             15  OLD-TDAPC-NEXT-BUS-DATE      PIC 9(08).          
017834                                                                  
017836     05  OLD-TDABENEF.                                            
017838         10  OLD-TDAB-BANK                    PIC 9(04).          
017840         10  OLD-TDAB-CUST                    PIC 9(12).          
017842         10  OLD-TDAB-ACCT                    PIC 9(10).          
017844         10  OLD-TDAB-BENEF-NBR               PIC 9(02).          
017846         10  OLD-TDAB-NAME                    PIC X(40).          
017848         10  OLD-TDAB-NAME-2                  PIC X(40).          
017850         10  OLD-TDAB-NAME-3                  PIC X(40).          
017852         10  OLD-TDAB-ADDR-1                  PIC X(40).          
017854         10  OLD-TDAB-ADDR-2                  PIC X(40).          
017856         10  OLD-TDAB-CITY                    PIC X(40).          
017858         10  OLD-TDAB-STATE                   PIC X(02).          
017860         10  OLD-TDAB-PROVINCE                PIC X(02).          
017862         10  OLD-TDAB-COUNTRY                 PIC X(02).          
017864         10  OLD-TDAB-ZIP-CODE.                                   
017866             15  OLD-TDAB-ZIP                 PIC 9(05).          
017868             15  OLD-TDAB-ZIP-4               PIC 9(04).          
017870         10  OLD-TDAB-PHONE                   PIC 9(10).          
017872         10  OLD-TDAB-TIN                     PIC 9(09).          
017874         10  OLD-TDAB-BIRTH-DT                PIC 9(08).          
017876         10  OLD-TDAB-RELATION                PIC 9(01).          
017878         10  OLD-TDAB-DESIGNATION             PIC 9(01).          
017880         10  OLD-TDAB-PERCENT                 PIC 9(03).          
017882         10  OLD-TDAB-FREE-REMARK             PIC X(24).          
017884                                                                  
017886     05  OLD-TDAADDR.                                             
017888         10  OLD-TDADR-BANK                    PIC 9(04).         
017890         10  OLD-TDADR-CUST                    PIC 9(12).         
017892         10  OLD-TDADR-ACCT                    PIC 9(10).         
017894         10  OLD-TDADR-ADDR-USAGE              PIC X(01).         
017896         10  OLD-TDADR-TEMP-BEG-DT             PIC 9(04).         
017898         10  OLD-TDADR-TEMP-END-DT             PIC 9(04).         
017900         10  OLD-TDADR-TEMP-EFF-DT             PIC 9(08).         
017902         10  OLD-TDADR-TEMP-EXP-DT             PIC 9(08).         
017904         10  OLD-TDADR-ADDR-GROUP.                                
017906             15  OLD-TDADR-T-ADDR.                                
017908                 20  OLD-TDADR-T-ADDR-1        PIC X(40).         
017910                 20  OLD-TDADR-T-ADDR-2        PIC X(40).         
017912                 20  OLD-TDADR-T-CITY          PIC X(40).         
017914                 20  OLD-TDADR-T-STATE         PIC X(02).         
017916                 20  OLD-TDADR-T-PROVINCE      PIC X(02).         
017918                 20  OLD-TDADR-T-COUNTRY       PIC X(02).         
017920                 20  OLD-TDADR-T-ZIP-CODE.                        
017922                     25  OLD-TDADR-T-ZIP       PIC 9(05).         
017924                     25  OLD-TDADR-T-ZIP-4     PIC 9(04).         
017926                 20  OLD-TDADR-T-ALIEN-CD      PIC 9(01).         
017928                 20  OLD-TDADR-T-BAR-CODE      PIC 9(03).         
017930                 20  OLD-TDADR-T-EMAIL-ADDR    PIC X(100).        
017932                 20  OLD-TDADR-T-EMAIL-ADDR-R                     
017934                                REDEFINES OLD-TDADR-T-EMAIL-ADDR. 
017936                     25  OLD-TDADR-T-EMAIL-ADDR-1-50   PIC X(50). 
017938                     25  OLD-TDADR-T-EMAIL-ADDR-51-100 PIC X(50). 
017940                 20  OLD-TDADR-T-MAIL-CD       PIC 9(01).         
017942                 20  OLD-TDADR-T-ADDR-KEY      PIC X(28).         
017944             15  OLD-TDADR-A-ADDR.                                
017946                 20  OLD-TDADR-A-NAME-1          PIC X(40).       
017948                 20  OLD-TDADR-A-NAME-AREA-1.                     
017950                     25  OLD-TDADR-A-N1-KEY      PIC X(14).       
017952                     25  OLD-TDADR-A-N1-FIRST    PIC X(40).       
017954                     25  OLD-TDADR-A-N1-MID      PIC X(20).       
017956                     25  OLD-TDADR-A-N1-LAST     PIC X(40).       
017958                     25  OLD-TDADR-A-N1-PREFIX   PIC X(12).       
017960                     25  OLD-TDADR-A-N1-SUFFIX   PIC X(12).       
017962                     25  OLD-TDADR-A-N1-FAMILIAR PIC X(20).       
017964                     25  OLD-TDADR-A-N1-PRT-PFX  PIC X(01).       
017966                     25  OLD-TDADR-A-N1-PRT-SFX  PIC X(01).       
017968                     25  OLD-TDADR-A-N1-DESIGNAT PIC X(20).       
017970                 20  OLD-TDADR-A-NAME-2          PIC X(40).       
017972                 20  OLD-TDADR-A-N2-MODIFIED     PIC X(01).       
017974                 20  OLD-TDADR-A-N2-PRINT-CD     PIC X(01).       
017976                 20  OLD-TDADR-A-NAME-AREA-2.                     
017978                     25  OLD-TDADR-A-N2-KEY      PIC X(14).       
017980                     25  OLD-TDADR-A-N2-FIRST    PIC X(40).       
017982                     25  OLD-TDADR-A-N2-MID      PIC X(20).       
017984                     25  OLD-TDADR-A-N2-LAST     PIC X(40).       
017986                     25  OLD-TDADR-A-N2-PREFIX   PIC X(12).       
017988                     25  OLD-TDADR-A-N2-SUFFIX   PIC X(12).       
017990                     25  OLD-TDADR-A-N2-FAMILIAR PIC X(20).       
017992                     25  OLD-TDADR-A-N2-PRT-PFX  PIC X(01).       
017994                     25  OLD-TDADR-A-N2-PRT-SFX  PIC X(01).       
017996                     25  OLD-TDADR-A-N2-DESIGNAT PIC X(20).       
017998                 20  OLD-TDADR-A-NAME-3          PIC X(40).       
018000                 20  OLD-TDADR-A-N3-MODIFIED     PIC X(01).       
018002                 20  OLD-TDADR-A-N3-PRINT-CD     PIC X(01).       
018004                 20  OLD-TDADR-A-NAME-AREA-3.                     
018006                     25  OLD-TDADR-A-N3-KEY      PIC X(14).       
018008                     25  OLD-TDADR-A-N3-FIRST    PIC X(40).       
018010                     25  OLD-TDADR-A-N3-MID      PIC X(20).       
018012                     25  OLD-TDADR-A-N3-LAST     PIC X(40).       
018014                     25  OLD-TDADR-A-N3-PREFIX   PIC X(12).       
018016                     25  OLD-TDADR-A-N3-SUFFIX   PIC X(12).       
018018                     25  OLD-TDADR-A-N3-FAMILIAR PIC X(20).       
018020                     25  OLD-TDADR-A-N3-PRT-PFX  PIC X(01).       
018022                     25  OLD-TDADR-A-N3-PRT-SFX  PIC X(01).       
018024                     25  OLD-TDADR-A-N3-DESIGNAT PIC X(20).       
018026                 20  OLD-TDADR-A-ADDR-KEY        PIC X(28).       
018028                 20  OLD-TDADR-A-ADDR-1        PIC X(40).         
018030                 20  OLD-TDADR-A-ADDR-2        PIC X(40).         
018032                 20  OLD-TDADR-A-CITY          PIC X(40).         
018034                 20  OLD-TDADR-A-STATE         PIC X(02).         
018036                 20  OLD-TDADR-A-PROVINCE      PIC X(02).         
018038                 20  OLD-TDADR-A-COUNTRY       PIC X(02).         
018040                 20  OLD-TDADR-A-ZIP-CODE.                        
018042                     25  OLD-TDADR-A-ZIP       PIC 9(05).         
018044                     25  OLD-TDADR-A-ZIP-4     PIC 9(04).         
018046                 20  OLD-TDADR-A-ALIEN-CD      PIC 9(01).         
018048                 20  OLD-TDADR-A-BAR-CODE      PIC 9(03).         
018050                 20  OLD-TDADR-A-EMAIL-ADDR    PIC X(100).        
018052                 20  OLD-TDADR-A-EMAIL-ADDR-R                     
018054                                REDEFINES OLD-TDADR-A-EMAIL-ADDR. 
018056                     25  OLD-TDADR-A-EMAIL-ADDR-1-50   PIC X(50). 
018058                     25  OLD-TDADR-A-EMAIL-ADDR-51-100 PIC X(50). 
018060                 20  OLD-TDADR-A-MAIL-CD       PIC 9(01).         
018062         10  OLD-TDADR-SHT-NAME                PIC X(20).         
018064         10  OLD-TDADR-LUPD-DATE               PIC 9(08).         
018066         10  OLD-TDADR-LUPD-TIME               PIC 9(08).         
018068         10  OLD-TDADR-PUB-ID                  PIC X(08).         
018070         10  OLD-TDADR-TIN-CD                  PIC X.             
018072         10  OLD-TDADR-TIN-NBR                 PIC 9(9).          
018074         10  OLD-TDADR-TIN-CERT-CD             PIC 9.             
018076         10  OLD-TDADR-TIN-CD-2                PIC X(01).         
018078         10  OLD-TDADR-TIN-NBR-2               PIC 9(09).         
018080         10  OLD-TDADR-TIN-CT-CD-2             PIC 9(01).         
018082         10  OLD-TDADR-TIN-CD-3                PIC X(01).         
018084         10  OLD-TDADR-TIN-NBR-3               PIC 9(09).         
018086         10  OLD-TDADR-TIN-CT-CD-3             PIC 9(01).         
018088                                                                  
018090     05  OLD-TDACHK.                                              
018092         10  OLD-TDACK-BANK                    PIC 9(04).         
018094         10  OLD-TDACK-BRCH                    PIC 9(04).         
018096         10  OLD-TDACK-ADDR-CUST               PIC 9(12).         
018098         10  OLD-TDACK-CUST                    PIC 9(12)          
018100                                               OCCURS 10 TIMES.   
018102         10  OLD-TDACK-ACCT                    PIC 9(10)          
018104                                               OCCURS 10 TIMES.   
018106         10  OLD-TDACK-LUPD-DATE               PIC 9(08).         
018108         10  OLD-TDACK-LUPD-TIME               PIC 9(08).         
018110         10  OLD-TDACK-PUB-ID                  PIC X(08).         
018112                                                                  
018114     05  OLD-TDAMESSAGE.                                          
018116         10  OLD-TDAM-BANK                     PIC 9(04).         
018118         10  OLD-TDAM-APPL                     PIC 9(01).         
018120         10  OLD-TDAM-CODE-TYPE                PIC 9(01).         
018122         10  OLD-TDAM-CODE                     PIC 9(04).         
018124         10  OLD-TDAM-RPT-NBR                  PIC 9(04).         
018126         10  OLD-TDAM-TEST-MSG                 PIC 9(01).         
018128         10  OLD-TDAM-MESSAGE-NBR              PIC 9(03).         
018130         10  OLD-TDAM-MESSAGE-GRP.                                
018132             15  OLD-TDAM-MESSAGE              PIC X(60)          
018134                                               OCCURS 6 TIMES.    
018136         10  OLD-TDAM-STOP-DT                  PIC 9(08).         
018138         10  OLD-TDAM-ADD-DT                   PIC 9(08).         
018140         10  OLD-TDAM-ADD-TM                   PIC 9(08).         
018142         10  OLD-TDAM-LUPD-DT                  PIC 9(08).         
018144         10  OLD-TDAM-LUPD-TM                  PIC 9(08).         
018146         10  OLD-TDAM-PUB-ID                   PIC X(08).         
018148                                                                  
018150*** PLEASE REMEMBER TO UPDATE THE OLD,AND HOLD FIELDS WHEN        
018152*** UPDATING THE FOLLOWING TDB FIELDS.                            
018154*************************************************************     
018156                                                                  
018158   03  TDB-RECORD.                                                
018160     05  TDB-STANDARD-AREA.                                       
018162         07  TDB-APPL-ID                        PIC X(3).         
018164         07  TDB-FUNCTION-CD-X.                                   
018166             10  TDB-FUNCTION-CD                PIC 9(2).         
018168         07  TDB-ORIGINATE-CLIENT               PIC X(2).         
018170         07  TDB-CLIENT-VER                     PIC 9(2).         
018172         07  TDB-CLIENT-TRX-NBR                 PIC 9(4).         
018174         07  TDB-REC-SEQ                        PIC 9(2).         
018176         07  TDB-STRUCT-NBR                     PIC 9(2).         
018178         07  TDB-ERROR-NBR-X.                                     
018180             10  TDB-ERROR-NBR                  PIC 9(4).         
018182         07  TDB-MESSAGE-NBR-X.                                   
018184             10  TDB-MESSAGE-NBR                PIC 9(4).         
018186         07  TDB-READ-INFO.                                       
018188             10  TDB-READ-SET-NBR               PIC 9(02).        
018190             10  TDB-READ-DIRECTION             PIC X(01).        
018192             10  TDB-READ-AT                    PIC X(03).        
018194         07  TDB-READ-DATE                      PIC 9(08).        
018196         07  TDB-SPECIAL-ACTION-X.                                
018198             10  TDB-SPECIAL-ACTION             PIC 9(02).        
018200         07  TDB-EXPANSION                      PIC X(09).        
018202     05  TDB-DATA-AREA                          PIC X(2800).      
018204                                                                  
018206     05  TDB-TDARESTART-R REDEFINES TDB-DATA-AREA.                
018208         10  TDB-TDARESTART.                                      
018210             15  TDB-TDARST-PROG-ID            PIC X(10).         
018212             15  TDB-TDARST-USERAREA           PIC X(100).        
018214             15  FILLER                        PIC X(2690).       
018216                                                                  
018218   03  TDB-RECORD-DATA-AREA.                                      
018220                                                                  
018222     05  TDB-TDACUST.                                             
018224         10  TDB-TDAC-BANK-X.                                     
018226             15  TDB-TDAC-BANK             PIC 9(4).              
018228         10  TDB-TDAC-CUST-X.                                     
018230             15  TDB-TDAC-CUST             PIC 9(12).             
018232         10  TDB-TDAC-BRCH-X.                                     
018234             15  TDB-TDAC-BRCH             PIC 9(4).              
018236         10  TDB-TDAC-STATUS               PIC X(1).              
018238         10  TDB-TDAC-NAME-1               PIC X(40).             
018240         10  TDB-TDAC-NAME-AREA-1.                                
018242             15  TDB-TDAC-N1-KEY           PIC X(14).             
018244             15  TDB-TDAC-N1-FIRST         PIC X(40).             
018246             15  TDB-TDAC-N1-MID           PIC X(20).             
018248             15  TDB-TDAC-N1-LAST          PIC X(40).             
018250             15  TDB-TDAC-N1-PREFIX        PIC X(12).             
018252             15  TDB-TDAC-N1-SUFFIX        PIC X(12).             
018254             15  TDB-TDAC-N1-FAMILIAR      PIC X(20).             
018256             15  TDB-TDAC-N1-PRT-PFX       PIC X(01).             
018258             15  TDB-TDAC-N1-PRT-SFX       PIC X(01).             
018260             15  TDB-TDAC-N1-DESIGNAT      PIC X(20).             
018262         10  TDB-TDAC-NAME-2               PIC X(40).             
018264         10  TDB-TDAC-N2-MODIFIED          PIC X(01).             
018266         10  TDB-TDAC-N2-PRINT-CD          PIC X(01).             
018268         10  TDB-TDAC-NAME-AREA-2.                                
018270             15  TDB-TDAC-N2-KEY           PIC X(14).             
018272             15  TDB-TDAC-N2-FIRST         PIC X(40).             
018274             15  TDB-TDAC-N2-MID           PIC X(20).             
018276             15  TDB-TDAC-N2-LAST          PIC X(40).             
018278             15  TDB-TDAC-N2-PREFIX        PIC X(12).             
018280             15  TDB-TDAC-N2-SUFFIX        PIC X(12).             
018282             15  TDB-TDAC-N2-FAMILIAR      PIC X(20).             
018284             15  TDB-TDAC-N2-PRT-PFX       PIC X(01).             
018286             15  TDB-TDAC-N2-PRT-SFX       PIC X(01).             
018288             15  TDB-TDAC-N2-DESIGNAT      PIC X(20).             
018290         10  TDB-TDAC-NAME-3               PIC X(40).             
018292         10  TDB-TDAC-N3-MODIFIED          PIC X(01).             
018294         10  TDB-TDAC-N3-PRINT-CD          PIC X(01).             
018296         10  TDB-TDAC-NAME-AREA-3.                                
018298             15  TDB-TDAC-N3-KEY           PIC X(14).             
018300             15  TDB-TDAC-N3-FIRST         PIC X(40).             
018302             15  TDB-TDAC-N3-MID           PIC X(20).             
018304             15  TDB-TDAC-N3-LAST          PIC X(40).             
018306             15  TDB-TDAC-N3-PREFIX        PIC X(12).             
018308             15  TDB-TDAC-N3-SUFFIX        PIC X(12).             
018310             15  TDB-TDAC-N3-FAMILIAR      PIC X(20).             
018312             15  TDB-TDAC-N3-PRT-PFX       PIC X(01).             
018314             15  TDB-TDAC-N3-PRT-SFX       PIC X(01).             
018316             15  TDB-TDAC-N3-DESIGNAT      PIC X(20).             
018318         10  TDB-TDAC-ADDR-KEY             PIC X(28).             
018320         10  TDB-TDAC-ADDR-1               PIC X(40).             
018322         10  TDB-TDAC-ADDR-2               PIC X(40).             
018324         10  TDB-TDAC-CITY                 PIC X(40).             
018326         10  TDB-TDAC-STATE                PIC X(2).              
018328         10  TDB-TDAC-PROVINCE             PIC X(2).              
018330         10  TDB-TDAC-COUNTRY              PIC X(2).              
018332         10  TDB-TDAC-ZIP-CODE.                                   
018334             15  TDB-TDAC-ZIP-X.                                  
018336                 20  TDB-TDAC-ZIP          PIC 9(5).              
018338             15  TDB-TDAC-ZIP-4-X.                                
018340                 20  TDB-TDAC-ZIP-4        PIC 9(4).              
018342         10  TDB-TDAC-LONGITUDE            PIC S9(3)V9(6).        
018344         10  TDB-TDAC-LATITUDE             PIC S9(3)V9(6).        
018346         10  TDB-TDAC-MAIL-CD              PIC 9(1).              
018348         10  TDB-TDAC-TICKLER-FLAG-X.                             
018350             15  TDB-TDAC-TICKLER-FLAG     PIC 9.                 
018352         10  TDB-TDAC-RESIDENT-CD-X.                              
018354             15  TDB-TDAC-RESIDENT-CD      PIC 9.                 
018356         10  TDB-TDAC-ALIEN-CD             PIC 9(1).              
018358         10  TDB-TDAC-SHT-NAME             PIC X(20).             
018360         10  TDB-TDAC-BAR-CD-X.                                   
018362             15  TDB-TDAC-BAR-CD           PIC 9(3).              
018364         10  TDB-TDAC-PHONE-1-X.                                  
018366             15  TDB-TDAC-PHONE-1          PIC 9(10).             
018368         10  TDB-TDAC-PHONE-2-X.                                  
018370             15  TDB-TDAC-PHONE-2          PIC 9(10).             
018372         10  TDB-TDAC-TIN-CD               PIC X(1).              
018374         10  TDB-TDAC-TIN-CERT-CD-X.                              
018376             15  TDB-TDAC-TIN-CERT-CD      PIC 9(1).              
018378         10  TDB-TDAC-TIN-CERT-DT-X.                              
018380             15  TDB-TDAC-TIN-CERT-DT      PIC 9(8).              
018382         10  TDB-TDAC-TIN-NBR-X.                                  
018384             15  TDB-TDAC-TIN-NBR          PIC 9(9).              
018386         10  TDB-TDAC-OFFICER              PIC X(3).              
018388         10  TDB-TDAC-EMP-CD               PIC X(1).              
018390         10  TDB-TDAC-FREE-MARK            PIC X(24).             
018392         10  TDB-TDAC-INQ-SECR-CD-X.                              
018394             15  TDB-TDAC-INQ-SECR-CD      PIC 9(1).              
018396         10  TDB-TDAC-PRIVACY-X.                                  
018398             15  TDB-TDAC-PRIVACY          PIC 9(1).              
018400         10  TDB-TDAC-BK-DEF-CD1           PIC X(1).              
018402         10  TDB-TDAC-BK-DEF-CD2           PIC X(1).              
018404         10  TDB-TDAC-BK-DEF-CD3           PIC X(1).              
018406         10  TDB-TDAC-BK-DEF-CD4           PIC X(1).              
018408         10  TDB-TDAC-BK-DEF-CD5           PIC X(1).              
018410         10  TDB-TDAC-EMPLOYEE-ID          PIC X(8).              
018412         10  TDB-TDAC-EMAIL-ADDR           PIC X(100).            
018414         10  TDB-TDAC-EMAIL-ADDR-R REDEFINES TDB-TDAC-EMAIL-ADDR. 
018416             15  TDB-TDAC-EMAIL-ADDR-1-30  PIC X(30).             
018418             15  TDB-TDAC-EMAIL-ADDR-31-60 PIC X(30).             
018420             15  TDB-TDAC-EMAIL-ADDR-61-90 PIC X(30).             
018422             15  TDB-TDAC-EMAIL-ADDR-91-100                       
018424                                           PIC X(10).             
018426         10 TDB-TDAC-EMAIL-ADDR-RR                                
018428                                   REDEFINES TDB-TDAC-EMAIL-ADDR. 
018430             15  TDB-TDAC-EMAIL-ADDR-1-50  PIC X(50).             
018432             15  TDB-TDAC-EMAIL-ADDR-51-100 PIC X(50).            
018434         10  TDB-TDAC-EMAIL-PSSWRD         PIC X(12).             
018436         10  TDB-TDAC-GENDER               PIC X(1).              
018438         10  TDB-TDAC-NEW-CUST-X.                                 
018440             15  TDB-TDAC-NEW-CUST         PIC 9.                 
018442         10  TDB-TDAC-OPEN-DT-X.                                  
018444             15  TDB-TDAC-OPEN-DT          PIC 9(8).              
018446         10  TDB-TDAC-LUPD-DATE-X.                                
018448             15  TDB-TDAC-LUPD-DATE        PIC 9(8).              
018450         10  TDB-TDAC-LUPD-TIME-X.                                
018452             15  TDB-TDAC-LUPD-TIME        PIC 9(8).              
018454         10  TDB-TDAC-LST-CONTACT-X.                              
018456             15  TDB-TDAC-LST-CONTACT      PIC 9(8).              
018458         10  TDB-TDAC-BIRTH-DT-X.                                 
018460             15  TDB-TDAC-BIRTH-DT         PIC 9(8).              
018462         10  TDB-TDAC-BIRTH-DT-2-X.                               
018464             15  TDB-TDAC-BIRTH-DT-2       PIC 9(8).              
018466         10  TDB-TDAC-BIRTH-DT-3           PIC 9(8).              
018468         10  TDB-TDAC-DEATH-DT-X.                                 
018470             15  TDB-TDAC-DEATH-DT         PIC 9(8).              
018472         10  TDB-TDAC-ADD-DT-X.                                   
018474             15  TDB-TDAC-ADD-DT           PIC 9(8).              
018476         10  TDB-TDAC-ADD-TM-X.                                   
018478             15  TDB-TDAC-ADD-TM           PIC 9(6).              
018480         10  TDB-TDAC-ROTH-DATE-X.                                
018482             15  TDB-TDAC-ROTH-DATE        PIC 9(8).              
018484         10  TDB-TDAC-CD-BAL-X.                                   
018486             15  TDB-TDAC-CD-BAL           PIC S9(15)V9(2).       
018488         10  TDB-TDAC-CD-BAL-BYR-X.                               
018490             15  TDB-TDAC-CD-BAL-BYR       PIC S9(15)V9(2).       
018492         10  TDB-TDAC-CD-PENLTY-X.                                
018494             15  TDB-TDAC-CD-PENLTY        PIC S9(15)V9(2).       
018496         10  TDB-TDAC-CD-WTHLD-X.                                 
018498             15  TDB-TDAC-CD-WTHLD         PIC S9(15)V9(2).       
018500         10  TDB-TDAC-CD-INT-X.                                   
018502             15  TDB-TDAC-CD-INT           PIC S9(15)V9(2).       
018504         10  TDB-TDAC-CD-OID-INT-X.                               
018506             15  TDB-TDAC-CD-OID-INT       PIC S9(15)V9(2).       
018508         10  TDB-TDAC-IRA-BAL-X.                                  
018510             15  TDB-TDAC-IRA-BAL          PIC S9(15)V9(2).       
018512         10  TDB-TDAC-IRA-BAL-BYR-X.                              
018514             15  TDB-TDAC-IRA-BAL-BYR      PIC S9(15)V9(2).       
018516         10  TDB-TDAC-IRA-PENLTY-X.                               
018518             15  TDB-TDAC-IRA-PENLTY       PIC S9(15)V9(2).       
018520         10  TDB-TDAC-IRA-WTHLD-X.                                
018522             15  TDB-TDAC-IRA-WTHLD        PIC S9(15)V9(2).       
018524         10  TDB-TDAC-IRA-INT-X.                                  
018526             15  TDB-TDAC-IRA-INT          PIC S9(15)V9(2).       
018528         10  TDB-TDAC-IRA-CONTR-X.                                
018530             15  TDB-TDAC-IRA-CONTR        PIC S9(15)V9(2).       
018532         10  TDB-TDAC-IRA-CONTR-LY-X.                             
018534             15  TDB-TDAC-IRA-CONTR-LY     PIC S9(15)V9(2).       
018536         10  TDB-TDAC-IRA-DISTR-X.                                
018538             15  TDB-TDAC-IRA-DISTR        PIC S9(15)V9(2).       
018540         10  TDB-TDAC-IRA-DISTR-LY-X.                             
018542             15  TDB-TDAC-IRA-DISTR-LY     PIC S9(15)V9(2).       
018544         10  TDB-TDAC-IRA-ROLLOVER-X.                             
018546             15  TDB-TDAC-IRA-ROLLOVER     PIC S9(15)V9(2).       
018548         10  TDB-TDAC-IRA-TRF-IN-X.                               
018550             15  TDB-TDAC-IRA-TRF-IN       PIC S9(15)V9(2).       
018552         10  TDB-TDAC-IRA-TRF-OUT-X.                              
018554             15  TDB-TDAC-IRA-TRF-OUT      PIC S9(15)V9(2).       
018556         10  TDB-TDAC-IRA-FAIR-MKT-X.                             
018558             15  TDB-TDAC-IRA-FAIR-MKT     PIC S9(15)V9(2).       
018560         10  TDB-TDAC-CIF-REMARK           PIC X.                 
018562         10  TDB-TDAC-CD-ST-WHLD-X.                               
018564             15  TDB-TDAC-CD-ST-WHLD       PIC S9(15)V9(2).       
018566         10  TDB-TDAC-IRA-ST-WHLD-X.                              
018568             15  TDB-TDAC-IRA-ST-WHLD      PIC S9(15)V9(2).       
018570         10  TDB-TDAC-CURR-YR-AMT-X.                              
018572             15  TDB-TDAC-CURR-YR-AMT      PIC S9(15)V9(2)        
018574                                               OCCURS 12 TIMES.   
018576         10  TDB-TDAC-LAST-YR-AMT-X.                              
018578             15  TDB-TDAC-LAST-YR-AMT      PIC S9(15)V9(2)        
018580                                               OCCURS 12 TIMES.   
018582         10  TDB-TDAC-TIN-CD-2-X.                                 
018584             15  TDB-TDAC-TIN-CD-2         PIC X(01).             
018586         10  TDB-TDAC-TIN-CRT-CD-2-X.                             
018588             15  TDB-TDAC-TIN-CRT-CD-2     PIC 9(01).             
018590         10  TDB-TDAC-TIN-CRT-DT-2-X.                             
018592             15  TDB-TDAC-TIN-CRT-DT-2     PIC 9(08).             
018594         10  TDB-TDAC-TIN-NBR-2-X.                                
018596             15  TDB-TDAC-TIN-NBR-2        PIC 9(09).             
018598         10  TDB-TDAC-TIN-CD-3             PIC X(01).             
018600         10  TDB-TDAC-TIN-CRT-CD-3         PIC 9(01).             
018602         10  TDB-TDAC-TIN-CRT-DT-3         PIC 9(08).             
018604         10  TDB-TDAC-TIN-NBR-3            PIC 9(09).             
018606         10  TDB-TDAC-NAICS-CD-X.                                 
018608             15  TDB-TDAC-NAICS-CD         PIC 9(06).             
018610         10  TDB-TDAC-CIF-PASS-THR-X.                             
018612             15  TDB-TDAC-CIF-PASS-THR     PIC 9(01).             
018614         10  TDB-TDAC-EMAIL-NTC-X.                                
018616             15  TDB-TDAC-EMAIL-NTC        PIC 9(01).             
018618         10  TDB-TDAC-RMD-YR-AMT           PIC S9(15)V9(2).       
018620         10  TDB-TDAC-ADDR-CHG-DT-X.                              
018622             15  TDB-TDAC-ADDR-CHG-DT      PIC 9(08).             
018624         10  TDB-TDAC-WTHLD-CD             PIC 9(01).             
018626         10  TDB-TDAC-ST-WHLD-CD           PIC 9(01).             
018628         10  TDB-TDAC-WTHLD-AMT            PIC S9(12)V9(2).       
018630         10  TDB-TDAC-ST-WHLD-AMT          PIC S9(12)V9(2).       
018632         10  TDB-TDAC-FOREIGN-LANG         PIC X(01).             
018634         10  TDB-TDAC-L-ROLLOVR-DT         PIC 9(08).             
018636         10  TDB-TDAC-CUSTM-FIELDS         PIC 9(01).             
018638         10  TDB-TDAC-LLC-NAME             PIC X(40).             
018640         10  TDB-TDAC-LLC-TIN-CD           PIC X(01).             
018642         10  TDB-TDAC-LLC-TIN              PIC 9(09).             
018644         10  TDB-TDAC-FOREIGN-PHN          PIC X(20).             
018646                                                                  
018648     05  TDB-TDAACCT.                                             
018650         10  TDB-TDAA-BANK-X.                                     
018652             15  TDB-TDAA-BANK             PIC 9(4).              
018654         10  TDB-TDAA-BRCH-X.                                     
018656             15  TDB-TDAA-BRCH             PIC 9(4).              
018658         10  TDB-TDAA-APPL-X.                                     
018660             15  TDB-TDAA-APPL             PIC 9(1).              
018662         10  TDB-TDAA-CUST-X.                                     
018664             15  TDB-TDAA-CUST             PIC 9(12).             
018666         10  TDB-TDAA-ACCT-X.                                     
018668             15  TDB-TDAA-ACCT             PIC 9(10).             
018670         10  TDB-TDAA-STATUS               PIC X(1).              
018672         10  TDB-TDAA-IRA-TYPE-X.                                 
018674             15  TDB-TDAA-IRA-TYPE         PIC 9(2).              
018676         10  TDB-TDAA-ACCT-OPTION-X.                              
018678             15  TDB-TDAA-ACCT-OPTION      PIC 9(2).              
018680         10  TDB-TDAA-DT-CONDENSED-X.                             
018682             15  TDB-TDAA-DT-CONDENSED     PIC 9(8).              
018684         10  TDB-TDAA-CERT-X.                                     
018686             15  TDB-TDAA-CERT             PIC 9(7).              
018688         10  TDB-TDAA-SHT-NAME             PIC X(20).             
018690         10  TDB-TDAA-TITLE                PIC X(40).             
018692         10  TDB-TDAA-TITLE-PRINT          PIC X(1).              
018694         10  TDB-TDAA-ADDR-USAGE           PIC X(01).             
018696         10  TDB-TDAA-ADDR-ALT             PIC X(01).             
018698         10  TDB-TDAA-ADDR-TEMP            PIC X(01).             
018700         10  TDB-TDAA-TEMP-BEG-DT          PIC 9(04).             
018702         10  TDB-TDAA-TEMP-END-DT          PIC 9(04).             
018704         10  TDB-TDAA-TEMP-EFF-DT          PIC 9(08).             
018706         10  TDB-TDAA-TEMP-EXP-DT          PIC 9(08).             
018708         10  TDB-TDAA-END-OF-INT-X.                               
018710             15  TDB-TDAA-END-OF-INT       PIC 9(1).              
018712         10  TDB-TDAA-END-OF-MAT-X.                               
018714             15  TDB-TDAA-END-OF-MAT       PIC 9(1).              
018716         10  TDB-TDAA-END-OF-STMT-X.                              
018718             15  TDB-TDAA-END-OF-STMT      PIC 9(1).              
018720         10  TDB-TDAA-END-OF-CMPD-X.                              
018722             15  TDB-TDAA-END-OF-CMPD      PIC 9(1).              
018724         10  TDB-TDAA-END-OF-FEE-X.                               
018726             15  TDB-TDAA-END-OF-FEE       PIC 9(1).              
018728         10  TDB-TDAA-OFFICER              PIC X(3).              
018730         10  TDB-TDAA-OFFICER-2            PIC X(3).              
018732         10  TDB-TDAA-OFFICER-3            PIC X(3).              
018734         10  TDB-TDAA-FREE-MARK            PIC X(24).             
018736         10  TDB-TDAA-CLASS-CD             PIC X(1).              
018738         10  TDB-TDAA-CORR-BK-CD           PIC X(1).              
018740         10  TDB-TDAA-PUBLIC-FUND          PIC X(1).              
018742         10  TDB-TDAA-TRUST-CD             PIC X(1).              
018744         10  TDB-TDAA-RT-CHG-ALLOW-X.                             
018746             15  TDB-TDAA-RT-CHG-ALLOW     PIC 9(1).              
018748         10  TDB-TDAA-WTHDRW-ALLOW-X.                             
018750             15  TDB-TDAA-WTHDRW-ALLOW     PIC 9(1).              
018752         10  TDB-TDAA-DPOSIT-ALLOW-X.                             
018754             15  TDB-TDAA-DPOSIT-ALLOW     PIC 9(1).              
018756         10  TDB-TDAA-POST-MAT-X.                                 
018758             15  TDB-TDAA-POST-MAT         PIC 9(1).              
018760         10  TDB-TDAA-RT-FLOOR-X.                                 
018762             15  TDB-TDAA-RT-FLOOR         PIC 9(1).              
018764         10  TDB-TDAA-REPO-CD-X.                                  
018766             15  TDB-TDAA-REPO-CD          PIC 9(1).              
018768         10  TDB-TDAA-TOTAL-CD-X.                                 
018770             15  TDB-TDAA-TOTAL-CD         PIC 9(3).              
018772         10  TDB-TDAA-REN-TOTAL-CD-X.                             
018774             15  TDB-TDAA-REN-TOTAL-CD     PIC 9(3).              
018776         10  TDB-TDAA-ORG-TOTAL-CD         PIC 9(3).              
018778         10  TDB-TDAA-INQ-SECR-CD-X.                              
018780             15  TDB-TDAA-INQ-SECR-CD      PIC 9(1).              
018782         10  TDB-TDAA-MAIL-CD-X.                                  
018784             15  TDB-TDAA-MAIL-CD          PIC 9(1).              
018786         10  TDB-TDAA-WTHD-REQD-CD-X.                             
018788             15  TDB-TDAA-WTHD-REQD-CD     PIC 9(1).              
018790         10  TDB-TDAA-TICKLER-FLAG-X.                             
018792             15  TDB-TDAA-TICKLER-FLAG     PIC 9.                 
018794         10  TDB-TDAA-DISP-CD-X.                                  
018796             15  TDB-TDAA-DISP-CD          PIC 9(1).              
018798         10  TDB-TDAA-CLS-DISP-CD          PIC 9(1).              
018800         10  TDB-TDAA-DIST-STATUS-X.                              
018802             15  TDB-TDAA-DIST-STATUS      PIC 9(1).              
018804         10  TDB-TDAA-COMM-ACCT-X.                                
018806             15  TDB-TDAA-COMM-ACCT        PIC 9(1).              
018808         10  TDB-TDAA-RENEW-CD-X.                                 
018810             15  TDB-TDAA-RENEW-CD         PIC 9(1).              
018812         10  TDB-TDAA-PLEDGE-CD            PIC X(1).              
018814         10  TDB-TDAA-NEGOT-CD             PIC X(1).              
018816         10  TDB-TDAA-BENEF-CD-X.                                 
018818             15  TDB-TDAA-BENEF-CD         PIC 9(1).              
018820         10  TDB-TDAA-COMM-MAT-CD-X.                              
018822             15  TDB-TDAA-COMM-MAT-CD      PIC 9(1).              
018824         10  TDB-TDAA-NBR-BENEF-X.                                
018826             15  TDB-TDAA-NBR-BENEF        PIC 9(1).              
018828         10  TDB-TDAA-OVERRIDE-X.                                 
018830             15  TDB-TDAA-OVERRIDE         PIC 9(1).              
018832         10  TDB-TDAA-INT-CD-X.                                   
018834             15  TDB-TDAA-INT-CD           PIC 9(1).              
018836         10  TDB-TDAA-WTHLD-CD-X.                                 
018838             15  TDB-TDAA-WTHLD-CD         PIC 9(1).              
018840         10  TDB-TDAA-WTHLD-AMT-X.                                
018842             15  TDB-TDAA-WTHLD-AMT        PIC S9(12)V9(2).       
018844         10  TDB-TDAA-IGL-GRP-X.                                  
018846             15  TDB-TDAA-IGL-GRP          PIC 9(2).              
018848         10  TDB-TDAA-SUM-STMT-CD-X.                              
018850             15  TDB-TDAA-SUM-STMT-CD      PIC 9(1).              
018852         10  TDB-TDAA-REN-NTC-CD-X.                               
018854             15  TDB-TDAA-REN-NTC-CD       PIC 9(1).              
018856         10  TDB-TDAA-PMAT-NTC-CD-X.                              
018858             15  TDB-TDAA-PMAT-NTC-CD      PIC 9(1).              
018860         10  TDB-TDAA-RTCHG-NTC-CD-X.                             
018862             15  TDB-TDAA-RTCHG-NTC-CD     PIC 9(1).              
018864         10  TDB-TDAA-INT-NTC-CD-X.                               
018866             15  TDB-TDAA-INT-NTC-CD       PIC 9(1).              
018868         10  TDB-TDAA-CHG-NTC-X.                                  
018870             15  TDB-TDAA-CHG-NTC          PIC 9(1).              
018872         10  TDB-TDAA-YIELD-NUM-X.                                
018874             15  TDB-TDAA-YIELD-NUM        PIC 9(3).              
018876         10  TDB-TDAA-YIELD-DENOM-X.                              
018878             15  TDB-TDAA-YIELD-DENOM      PIC 9(3).              
018880         10  TDB-TDAA-CMPD-FREQ-X.                                
018882             15  TDB-TDAA-CMPD-FREQ        PIC 9(1).              
018884         10  TDB-TDAA-CMPD-NTRVL-X.                               
018886             15  TDB-TDAA-CMPD-NTRVL       PIC 9(4).              
018888         10  TDB-TDAA-RT-CHG-LIMIT-X.                             
018890             15  TDB-TDAA-RT-CHG-LIMIT     PIC 9(1).              
018892         10  TDB-TDAA-VAR-RT-IMMED-X.                             
018894             15  TDB-TDAA-VAR-RT-IMMED     PIC 9(1).              
018896         10  TDB-TDAA-VAR-RT-INT-X.                               
018898             15  TDB-TDAA-VAR-RT-INT       PIC 9(1).              
018900         10  TDB-TDAA-VAR-RT-SCHED-X.                             
018902             15  TDB-TDAA-VAR-RT-SCHED     PIC 9(1).              
018904         10  TDB-TDAA-VAR-RT-CUST-X.                              
018906             15  TDB-TDAA-VAR-RT-CUST      PIC 9(1).              
018908         10  TDB-TDAA-VAR-RT-BAL-X.                               
018910             15  TDB-TDAA-VAR-RT-BAL       PIC 9(1).              
018912         10  TDB-TDAA-RT-INDX-CD-X.                               
018914             15  TDB-TDAA-RT-INDX-CD       PIC 9(2).              
018916         10  TDB-TDAA-R-RT-INDX-CD         PIC XX.                
018918         10  TDB-TDAA-RT-MARG-CD-X.                               
018920             15  TDB-TDAA-RT-MARG-CD       PIC 9(2).              
018922         10  TDB-TDAA-R-RT-MARG-CD         PIC XX.                
018924         10  TDB-TDAA-RT-TIER-CD-X.                               
018926             15  TDB-TDAA-RT-TIER-CD       PIC 9(2).              
018928         10  TDB-TDAA-R-RT-TIER-CD         PIC XX.                
018930         10  TDB-TDAA-RT-SR-CD-X.                                 
018932             15  TDB-TDAA-RT-SR-CD         PIC 9(2).              
018934         10  TDB-TDAA-R-RT-SR-CD           PIC XX.                
018936         10  TDB-TDAA-RT-REGN-CD-X.                               
018938             15  TDB-TDAA-RT-REGN-CD       PIC 9(2).              
018940         10  TDB-TDAA-RT-CHG-NTRVL-X.                             
018942             15  TDB-TDAA-RT-CHG-NTRVL     PIC 9(3).              
018944         10  TDB-TDAA-CAP-RT-CHG           PIC X.                 
018946         10  TDB-TDAA-R-TIER-RT-CH         PIC X.                 
018948         10  TDB-TDAA-ALERT-CD-X.                                 
018950             15  TDB-TDAA-ALERT-CD         PIC 9(2).              
018952         10  TDB-TDAA-ALERT-CD-2           PIC 9(2).              
018954         10  TDB-TDAA-ALERT-CD-3           PIC 9(2).              
018956         10  TDB-TDAA-CENSUS-TRACT-X.                             
018958             15  TDB-TDAA-CENSUS-TRACT     PIC 9(4)V9(2).         
018960         10  TDB-TDAA-MK-SEGMENT           PIC X(2).              
018962         10  TDB-TDAA-BK-DEF-TOT           PIC X(3).              
018964         10  TDB-TDAA-BK-DEF-CD1           PIC X(1).              
018966         10  TDB-TDAA-BK-DEF-CD2           PIC X(1).              
018968         10  TDB-TDAA-BK-DEF-CD3           PIC X(1).              
018970         10  TDB-TDAA-BK-DEF-CD4           PIC X(1).              
018972         10  TDB-TDAA-BK-DEF-CD5           PIC X(1).              
018974         10  TDB-TDAA-OID-METH-X.                                 
018976             15  TDB-TDAA-OID-METH         PIC 9(1).              
018978         10  TDB-TDAA-EOY-CD-X.                                   
018980             15  TDB-TDAA-EOY-CD           PIC 9(1).              
018982         10  TDB-TDAA-B-NOTC-YR1-X.                               
018984             15  TDB-TDAA-B-NOTC-YR1       PIC 9(1).              
018986         10  TDB-TDAA-B-NOTC-YR2-X.                               
018988             15  TDB-TDAA-B-NOTC-YR2       PIC 9(1).              
018990         10  TDB-TDAA-B-NOTC-YR3-X.                               
018992             15  TDB-TDAA-B-NOTC-YR3       PIC 9(1).              
018994         10  TDB-TDAA-NO-COMB-IRS-X.                              
018996             15  TDB-TDAA-NO-COMB-IRS      PIC 9(1).              
018998         10  TDB-TDAA-PENLTY-CD-X.                                
019000             15  TDB-TDAA-PENLTY-CD        PIC 999.               
019002         10  TDB-TDAA-MONEY-SRC-CD         PIC X(1).              
019004         10  TDB-TDAA-INTERNET-CD.                                
019006             15  TDB-TDAA-INTERNET-BPY-X.                         
019008                 20  TDB-TDAA-INTERNET-BPY PIC 9(1).              
019010             15  TDB-TDAA-INTERNET-TFR-X.                         
019012                 20  TDB-TDAA-INTERNET-TFR PIC 9(1).              
019014             15  TDB-TDAA-INTERNET-INQ-X.                         
019016                 20  TDB-TDAA-INTERNET-INQ PIC 9(1).              
019018         10  TDB-TDAA-IRA-BACKED-X.                               
019020             15  TDB-TDAA-IRA-BACKED       PIC 9(1).              
019022         10  TDB-TDAA-SAV-DEPOSIT          PIC 9(1).              
019024         10  TDB-TDAA-MAT-TYPE-X.                                 
019026             15  TDB-TDAA-MAT-TYPE         PIC 9(1).              
019028         10  TDB-TDAA-MAT-TERM-X.                                 
019030             15  TDB-TDAA-MAT-TERM         PIC 9(4).              
019032         10  TDB-TDAA-ORG-MAT-TYPE-X.                             
019034             15  TDB-TDAA-ORG-MAT-TYPE     PIC 9(1).              
019036         10  TDB-TDAA-ORG-MAT-TERM-X.                             
019038             15  TDB-TDAA-ORG-MAT-TERM     PIC 9(4).              
019040         10  TDB-TDAA-ODD-PAYMENT-X.                              
019042             15  TDB-TDAA-ODD-PAYMENT      PIC 9(1).              
019044         10  TDB-TDAA-PAY-FREQ-X.                                 
019046             15  TDB-TDAA-PAY-FREQ         PIC 9(1).              
019048         10  TDB-TDAA-PAY-NTRVL-X.                                
019050             15  TDB-TDAA-PAY-NTRVL        PIC 9(4).              
019052         10  TDB-TDAA-FEE-FREQ-X.                                 
019054             15  TDB-TDAA-FEE-FREQ         PIC 9(1).              
019056         10  TDB-TDAA-FEE-NTRVL-X.                                
019058             15  TDB-TDAA-FEE-NTRVL        PIC 9(4).              
019060         10  TDB-TDAA-STMT-FREQ-X.                                
019062             15  TDB-TDAA-STMT-FREQ        PIC 9(1).              
019064         10  TDB-TDAA-STMT-NTRVL-X.                               
019066             15  TDB-TDAA-STMT-NTRVL       PIC 9(4).              
019068         10  TDB-TDAA-EMPLOYEE-ID          PIC X(8).              
019070         10  TDB-TDAA-EFT-CARD             PIC X(1).              
019072         10  TDB-TDAA-PEN-WAV-RESN         PIC X(1).              
019074         10  TDB-TDAA-CLOSED-RESN          PIC X(1).              
019076         10  TDB-TDAA-SPECIAL-STMT-X.                             
019078             15  TDB-TDAA-SPECIAL-STMT     PIC 9(1).              
019080         10  TDB-TDAA-CLS-THIS-MTH-X.                             
019082             15  TDB-TDAA-CLS-THIS-MTH     PIC 9(1).              
019084         10  TDB-TDAA-RC-MAT-ONLY          PIC 9(1).              
019086         10  TDB-TDAA-GRACE-DAYS           PIC 9(2).              
019088         10  TDB-TDAA-CLS-ON-MAT           PIC 9(1).              
019090         10  TDB-TDAA-DDA-ACCT-1-X.                               
019092             15  TDB-TDAA-DDA-ACCT-1       PIC 9(12).             
019094         10  TDB-TDAA-DDA-ACCT-1-S-X.                             
019096             15  TDB-TDAA-DDA-ACCT-1-S     PIC 9(10).             
019098         10  TDB-TDAA-DDA-ACCT-2-X.                               
019100             15  TDB-TDAA-DDA-ACCT-2       PIC 9(12).             
019102         10  TDB-TDAA-DDA-ACCT-2-S-X.                             
019104             15  TDB-TDAA-DDA-ACCT-2-S     PIC 9(10).             
019106         10  TDB-TDAA-DDA-ACCT-3-X.                               
019108             15  TDB-TDAA-DDA-ACCT-3       PIC 9(12).             
019110         10  TDB-TDAA-DDA-ACCT-3-S-X.                             
019112             15  TDB-TDAA-DDA-ACCT-3-S     PIC 9(10).             
019114         10  TDB-TDAA-INT-ACCT-X.                                 
019116             15  TDB-TDAA-INT-ACCT         PIC 9(12).             
019118         10  TDB-TDAA-INT-ACCT-S-X.                               
019120             15  TDB-TDAA-INT-ACCT-S       PIC 9(10).             
019122         10  TDB-TDAA-CS-ACCT-X.                                  
019124             15  TDB-TDAA-CS-ACCT          PIC 9(12).             
019126         10  TDB-TDAA-CS-ACCT-S-X.                                
019128             15  TDB-TDAA-CS-ACCT-S        PIC 9(10).             
019130         10  TDB-TDAA-CC-ACCT-X.                                  
019132             15  TDB-TDAA-CC-ACCT          PIC 9(12).             
019134         10  TDB-TDAA-LNS-BORROWER-X.                             
019136             15  TDB-TDAA-LNS-BORROWER     PIC 9(12).             
019138         10  TDB-TDAA-LNS-NOTE-X.                                 
019140             15  TDB-TDAA-LNS-NOTE         PIC 9(10).             
019142         10  TDB-TDAA-CNV-OLD-ACCT         PIC X(15).             
019144         10  TDB-TDAA-CLS-ACCT             PIC 9(12).             
019146         10  TDB-TDAA-CLS-ACCT-S           PIC 9(10).             
019148         10  TDB-TDAA-DAYS-IN-PER-X.                              
019150             15  TDB-TDAA-DAYS-IN-PER      PIC 9(5).              
019152         10  TDB-TDAA-RR-CYC-NBR-X.                               
019154             15  TDB-TDAA-RR-CYC-NBR       PIC 9(2).              
019156         10  TDB-TDAA-CR-CNT-STD-X.                               
019158             15  TDB-TDAA-CR-CNT-STD       PIC 9(5).              
019160         10  TDB-TDAA-CR-AMT-STD-X.                               
019162             15  TDB-TDAA-CR-AMT-STD       PIC S9(12)V9(2).       
019164         10  TDB-TDAA-DB-CNT-STD-X.                               
019166             15  TDB-TDAA-DB-CNT-STD       PIC 9(5).              
019168         10  TDB-TDAA-DB-AMT-STD-X.                               
019170             15  TDB-TDAA-DB-AMT-STD       PIC S9(12)V9(2).       
019172         10  TDB-TDAA-CR-CNT-YTD-X.                               
019174             15  TDB-TDAA-CR-CNT-YTD       PIC 9(5).              
019176         10  TDB-TDAA-CR-AMT-YTD-X.                               
019178             15  TDB-TDAA-CR-AMT-YTD       PIC S9(12)V9(2).       
019180         10  TDB-TDAA-DB-CNT-YTD-X.                               
019182             15  TDB-TDAA-DB-CNT-YTD       PIC 9(5).              
019184         10  TDB-TDAA-DB-AMT-YTD-X.                               
019186             15  TDB-TDAA-DB-AMT-YTD       PIC S9(12)V9(2).       
019188         10  TDB-TDAA-DAYS-IN-TERM-X.                             
019190             15  TDB-TDAA-DAYS-IN-TERM     PIC 9(5).              
019192         10  TDB-TDAA-BEG-INT-BAL-X.                              
019194             15  TDB-TDAA-BEG-INT-BAL      PIC S9(12)V9(2).       
019196         10  TDB-TDAA-PURCH-AMT-X.                                
019198             15  TDB-TDAA-PURCH-AMT        PIC S9(12)V9(2).       
019200         10  TDB-TDAA-CURR-BAL-X.                                 
019202             15  TDB-TDAA-CURR-BAL         PIC S9(12)V9(2).       
019204         10  TDB-TDAA-AVAIL-BAL-X.                                
019206             15  TDB-TDAA-AVAIL-BAL        PIC S9(12)V9(2).       
019208         10  TDB-TDAA-BAL-BEG-MAT-X.                              
019210             15  TDB-TDAA-BAL-BEG-MAT      PIC S9(12)V9(2).       
019212         10  TDB-TDAA-CLOSE-AMT-X.                                
019214             15  TDB-TDAA-CLOSE-AMT        PIC S9(12)V9(2).       
019216         10  TDB-TDAA-MONEY-AMT-X.                                
019218             15  TDB-TDAA-MONEY-AMT        PIC S9(12)V9(2).       
019220         10  TDB-TDAA-BAL-BEG-STMT-X.                             
019222             15  TDB-TDAA-BAL-BEG-STMT     PIC S9(12)V9(2).       
019224         10  TDB-TDAA-ACCR-INT-X.                                 
019226             15  TDB-TDAA-ACCR-INT         PIC S9(12)V9(6).       
019228         10  TDB-TDAA-ANTIC-INT-X.                                
019230             15  TDB-TDAA-ANTIC-INT        PIC S9(12)V9(2).       
019232         10  TDB-TDAA-INT-TO-POST-X.                              
019234             15  TDB-TDAA-INT-TO-POST      PIC S9(12)V9(2).       
019236         10  TDB-TDAA-1099-YTD-X.                                 
019238             15  TDB-TDAA-1099-YTD         PIC S9(12)V9(2).       
019240         10  TDB-TDAA-1099-LST-YR-X.                              
019242             15  TDB-TDAA-1099-LST-YR      PIC S9(12)V9(2).       
019244         10  TDB-TDAA-CURR-PENLTY-X.                              
019246             15  TDB-TDAA-CURR-PENLTY      PIC S9(12)V9(2).       
019248         10  TDB-TDAA-PENLTY-STD-X.                               
019250             15  TDB-TDAA-PENLTY-STD       PIC S9(12)V9(2).       
019252         10  TDB-TDAA-PENLTY-YTD-X.                               
019254             15  TDB-TDAA-PENLTY-YTD       PIC S9(12)V9(2).       
019256         10  TDB-TDAA-LST-PENLTY-X.                               
019258             15  TDB-TDAA-LST-PENLTY       PIC S9(12)V9(2).       
019260         10  TDB-TDAA-CURR-INT-ADJ-X.                             
019262             15  TDB-TDAA-CURR-INT-ADJ     PIC S9(12)V9(2).       
019264         10  TDB-TDAA-TOTAMT-HOLDS-X.                             
019266             15  TDB-TDAA-TOTAMT-HOLDS     PIC S9(12)V9(2).       
019268         10  TDB-TDAA-NXT-INT-ADJ-X.                              
019270             15  TDB-TDAA-NXT-INT-ADJ      PIC S9(12)V9(2).       
019272         10  TDB-TDAA-FEE-AMT-X.                                  
019274             15  TDB-TDAA-FEE-AMT          PIC S9(12)V9(2).       
019276         10  TDB-TDAA-OID-RPT-INT-X.                              
019278             15  TDB-TDAA-OID-RPT-INT      PIC S9(12)V9(2).       
019280         10  TDB-TDAA-FAIR-MRKT-X.                                
019282             15  TDB-TDAA-FAIR-MRKT        PIC S9(12)V9(2).       
019284         10  TDB-TDAA-CUR-WHLD-AMT-X.                             
019286             15  TDB-TDAA-CUR-WHLD-AMT     PIC S9(12)V9(2).       
019288         10  TDB-TDAA-LST-WHLD-AMT-X.                             
019290             15  TDB-TDAA-LST-WHLD-AMT     PIC S9(12)V9(2).       
019292         10  TDB-TDAA-WTHLD-STD-X.                                
019294             15  TDB-TDAA-WTHLD-STD        PIC S9(12)V9(2).       
019296         10  TDB-TDAA-WTHLD-YTD-X.                                
019298             15  TDB-TDAA-WTHLD-YTD        PIC S9(12)V9(2).       
019300         10  TDB-TDAA-LST-INT-PMT-X.                              
019302             15  TDB-TDAA-LST-INT-PMT      PIC S9(12)V9(2).       
019304         10  TDB-TDAA-BAL-BEG-YR-X.                               
019306             15  TDB-TDAA-BAL-BEG-YR       PIC S9(12)V9(2).       
019308         10  TDB-TDAA-BAL-AT-CONV-X.                              
019310             15  TDB-TDAA-BAL-AT-CONV      PIC S9(12)V9(2).       
019312         10  TDB-TDAA-BAL-BEG-LYR-X.                              
019314             15  TDB-TDAA-BAL-BEG-LYR      PIC S9(12)V9(2).       
019316         10  TDB-TDAA-MIN-BAL-STD-X.                              
019318             15  TDB-TDAA-MIN-BAL-STD      PIC S9(12)V9(2).       
019320         10  TDB-TDAA-MIN-BAL-YTD-X.                              
019322             15  TDB-TDAA-MIN-BAL-YTD      PIC S9(12)V9(2).       
019324         10  TDB-TDAA-MAX-BAL-YTD          PIC S9(12)V9(2).       
019326         10  TDB-TDAA-LMINBAL-STD-X.                              
019328             15  TDB-TDAA-LMINBAL-STD      PIC S9(12)V9(2).       
019330         10  TDB-TDAA-CMPD-INT-X.                                 
019332             15  TDB-TDAA-CMPD-INT         PIC S9(12)V9(2).       
019334         10  TDB-TDAA-PER-DIEM-X.                                 
019336             15  TDB-TDAA-PER-DIEM         PIC S9(12)V9(6).       
019338         10  TDB-TDAA-AVG-PER-DIEM-X.                             
019340             15  TDB-TDAA-AVG-PER-DIEM     PIC S9(12)V9(6).       
019342         10  TDB-TDAA-EMAIL-MAXAMT-X.                             
019344             15  TDB-TDAA-EMAIL-MAXAMT     PIC 9(10).             
019346         10  TDB-TDAA-EMAIL-MINAMT-X.                             
019348             15  TDB-TDAA-EMAIL-MINAMT     PIC 9(10).             
019350         10  TDB-TDAA-DTH-FAIRMKT-X.                              
019352             15  TDB-TDAA-DTH-FAIRMKT      PIC S9(12)V9(2).       
019354         10  TDB-TDAA-PENLTY-WAIVE-X.                             
019356             15  TDB-TDAA-PENLTY-WAIVE     PIC S9(12)V9(2).       
019358         10  TDB-TDAA-BEG-INT-RT-X.                               
019360             15  TDB-TDAA-BEG-INT-RT       PIC 9(2)V9(3).         
019362         10  TDB-TDAA-CUR-INT-RT-X.                               
019364             15  TDB-TDAA-CUR-INT-RT       PIC 9(2)V9(3).         
019366         10  TDB-TDAA-FLOOR-RT-X.                                 
019368             15  TDB-TDAA-FLOOR-RT         PIC 9(2)V9(3).         
019370         10  TDB-TDAA-FLOOR-INCR-X.                               
019372             15  TDB-TDAA-FLOOR-INCR       PIC 9(2)V9(3).         
019374         10  TDB-TDAA-YIELD-RT-X.                                 
019376             15  TDB-TDAA-YIELD-RT         PIC 9(2)V9(3).         
019378         10  TDB-TDAA-RISE-RATE-X.                                
019380             15  TDB-TDAA-RISE-RATE        PIC 9(2)V9(3)          
019382                               OCCURS   10.                       
019384         10  TDB-TDAA-LNS-INCRMNT-X.                              
019386             15  TDB-TDAA-LNS-INCRMNT      PIC 9(2)V9(4).         
019388         10  TDB-TDAA-RT-VARIANCE-X.                              
019390             15  TDB-TDAA-RT-VARIANCE      PIC S9(1)V9(2).        
019392         10  TDB-TDAA-CONST-RT-ADJ         PIC S9(2)V9(3).        
019394         10  TDB-TDAA-RATE-AT-EOY-X.                              
019396             15  TDB-TDAA-RATE-AT-EOY      PIC 9(2)V9(3).         
019398         10  TDB-TDAA-RATE-LST-STM-X.                             
019400             15  TDB-TDAA-RATE-LST-STM     PIC 9(2)V9(3).         
019402         10  TDB-TDAA-ORG-YIELD-RT-X.                             
019404             15  TDB-TDAA-ORG-YIELD-RT     PIC 9(2)V9(3).         
019406         10  TDB-TDAA-REN-YIELD-RT-X.                             
019408             15  TDB-TDAA-REN-YIELD-RT     PIC 9(2)V9(3).         
019410         10  TDB-TDAA-SCHED-DT-X.                                 
019412             15  TDB-TDAA-SCHED-DT         PIC 9(8).              
019414         10  TDB-TDAA-ACCR-DT-X.                                  
019416             15  TDB-TDAA-ACCR-DT          PIC 9(8).              
019418         10  TDB-TDAA-OPEN-DT-X.                                  
019420             15  TDB-TDAA-OPEN-DT          PIC 9(8).              
019422         10  TDB-TDAA-CLSD-DT-X.                                  
019424             15  TDB-TDAA-CLSD-DT          PIC 9(8).              
019426         10  TDB-TDAA-LST-MAT-DT-X.                               
019428             15  TDB-TDAA-LST-MAT-DT       PIC 9(8).              
019430         10  TDB-TDAA-LST-POST-DT-X.                              
019432             15  TDB-TDAA-LST-POST-DT      PIC 9(8).              
019434         10  TDB-TDAA-LST-IN-PROC          PIC 9(8).              
019436         10  TDB-TDAA-LST-CONTACT-X.                              
019438             15  TDB-TDAA-LST-CONTACT      PIC 9(8).              
019440         10  TDB-TDAA-LST-FEE-DT-X.                               
019442             15  TDB-TDAA-LST-FEE-DT       PIC 9(8).              
019444         10  TDB-TDAA-LST-RTCHG-DT-X.                             
019446             15  TDB-TDAA-LST-RTCHG-DT     PIC 9(8).              
019448         10  TDB-TDAA-LST-DIST-DT-X.                              
019450             15  TDB-TDAA-LST-DIST-DT      PIC 9(8).              
019452         10  TDB-TDAA-LST-STMT-DT-X.                              
019454             15  TDB-TDAA-LST-STMT-DT      PIC 9(8).              
019456         10  TDB-TDAA-LST-CMPD-DT-X.                              
019458             15  TDB-TDAA-LST-CMPD-DT      PIC 9(8).              
019460         10  TDB-TDAA-RR-CYC-DT-X.                                
019462             15  TDB-TDAA-RR-CYC-DT        PIC 9(8)               
019464                               OCCURS   10.                       
019466         10  TDB-TDAA-BNF-BIRTH-DT-X.                             
019468             15  TDB-TDAA-BNF-BIRTH-DT     PIC 9(8).              
019470         10  TDB-TDAA-BNF-DEATH-DT-X.                             
019472             15  TDB-TDAA-BNF-DEATH-DT     PIC 9(8).              
019474         10  TDB-TDAA-LUPD-DATE-X.                                
019476             15  TDB-TDAA-LUPD-DATE        PIC 9(8).              
019478         10  TDB-TDAA-LUPD-TIME-X.                                
019480             15  TDB-TDAA-LUPD-TIME        PIC 9(6).              
019482         10  TDB-TDAA-ADD-DT-X.                                   
019484             15  TDB-TDAA-ADD-DT           PIC 9(8).              
019486         10  TDB-TDAA-ADD-TM-X.                                   
019488             15  TDB-TDAA-ADD-TM           PIC 9(6).              
019490         10  TDB-TDAA-CONV-DT-X.                                  
019492             15  TDB-TDAA-CONV-DT          PIC 9(8).              
019494         10  TDB-TDAA-ACT-CLOSE-DT-X.                             
019496             15  TDB-TDAA-ACT-CLOSE-DT     PIC 9(8).              
019498         10  TDB-TDAA-LST-TBACT-DT-X.                             
019500             15  TDB-TDAA-LST-TBACT-DT     PIC 9(8).              
019502         10  TDB-TDAA-ALERT-EXP-DT         PIC 9(8).              
019504         10  TDB-TDAA-ALRT2-EXP-DT         PIC 9(8).              
019506         10  TDB-TDAA-ALRT3-EXP-DT         PIC 9(8).              
019508         10  TDB-TDAA-NXT-FEE-DT-X.                               
019510             15  TDB-TDAA-NXT-FEE-DT       PIC 9(8).              
019512         10  TDB-TDAA-NXT-POST-DT-X.                              
019514             15  TDB-TDAA-NXT-POST-DT      PIC 9(8).              
019516         10  TDB-TDAA-NXT-MAT-DT-X.                               
019518             15  TDB-TDAA-NXT-MAT-DT       PIC 9(8).              
019520         10  TDB-TDAA-NXT-DIST-DT-X.                              
019522             15  TDB-TDAA-NXT-DIST-DT      PIC 9(8).              
019524         10  TDB-TDAA-NXT-RT-CHG-X.                               
019526             15  TDB-TDAA-NXT-RT-CHG       PIC 9(8).              
019528         10  TDB-TDAA-NXT-IN-PROC-X.                              
019530             15  TDB-TDAA-NXT-IN-PROC      PIC 9(8).              
019532         10  TDB-TDAA-NXT-CMPD-DT-X.                              
019534             15  TDB-TDAA-NXT-CMPD-DT      PIC 9(8).              
019536         10  TDB-TDAA-NXT-STMT-DT-X.                              
019538             15  TDB-TDAA-NXT-STMT-DT      PIC 9(8).              
019540         10  TDB-TDAA-NXT-DS-PROC-X.                              
019542             15  TDB-TDAA-NXT-DS-PROC      PIC 9(8).              
019544         10  TDB-TDAA-ADV-NTC-DT-X.                               
019546             15  TDB-TDAA-ADV-NTC-DT       PIC 9(8).              
019548         10  TDB-TDAA-NXT-29YR-DT-X.                              
019550             15  TDB-TDAA-NXT-29YR-DT      PIC 9(8).              
019552         10  TDB-TDAA-FAIR-MRKT-DT-X.                             
019554             15  TDB-TDAA-FAIR-MRKT-DT     PIC 9(8).              
019556         10  TDB-TDAA-SORT-FIELD-1         PIC X(36).             
019558         10  TDB-TDAA-SORT-FIELD-2         PIC X(36).             
019560         10  TDB-TDAA-SORT-FIELD-3         PIC X(36).             
019562         10  TDB-TDAA-SORT-FIELD-4         PIC X(36).             
019564         10  TDB-TDAA-CMAT-PUB-ID          PIC X(8).              
019566         10  TDB-TDAA-MSA-CONTR            PIC 9.                 
019568         10  TDB-TDAA-MSA-CONTR-LY         PIC 9.                 
019570         10  TDB-TDAA-AVG-ACCR-INT         PIC S9(12)V9(06).      
019572         10  TDB-TDAA-LEVEL-PAY-X.                                
019574             15  TDB-TDAA-LEVEL-PAY        PIC 9.                 
019576         10  TDB-TDAA-ST-INT-CD-X.                                
019578             15  TDB-TDAA-ST-INT-CD        PIC 9.                 
019580         10  TDB-TDAA-ST-WHLD-CD-X.                               
019582             15  TDB-TDAA-ST-WHLD-CD       PIC 9.                 
019584         10  TDB-TDAA-ST-WHLD-AMT-X.                              
019586             15  TDB-TDAA-ST-WHLD-AMT      PIC S9(12)V99.         
019588         10  TDB-TDAA-ST-CUR-W-AMT-X.                             
019590             15  TDB-TDAA-ST-CUR-W-AMT     PIC S9(12)V99.         
019592         10  TDB-TDAA-ST-LST-W-AMT-X.                             
019594             15  TDB-TDAA-ST-LST-W-AMT     PIC S9(12)V99.         
019596         10  TDB-TDAA-ST-WHLD-STD-X.                              
019598             15  TDB-TDAA-ST-WHLD-STD      PIC S9(12)V99.         
019600         10  TDB-TDAA-ST-WHLD-YTD-X.                              
019602             15  TDB-TDAA-ST-WHLD-YTD      PIC S9(12)V99.         
019604         10  TDB-TDAA-CIF-REMARK           PIC X.                 
019606         10  TDB-TDAA-CSR                  PIC X(03).             
019608         10  TDB-TDAA-BSA-O-RSK-CD-X.                             
019610             15  TDB-TDAA-BSA-O-RSK-CD     PIC 9(01).             
019612         10  TDB-TDAA-BSA-C-RSK-CD-X.                             
019614             15  TDB-TDAA-BSA-C-RSK-CD     PIC 9(01).             
019616         10  TDB-TDAA-LRG-TRX-DT-X.                               
019618             15  TDB-TDAA-LRG-TRX-DT       PIC 9(08).             
019620         10  TDB-TDAA-HSA-FMLY-IND-X.                             
019622             15  TDB-TDAA-HSA-FMLY-IND     PIC 9(01).             
019624         10  TDB-TDAA-STOP-PAY-IND-X.                             
019626             15  TDB-TDAA-STOP-PAY-IND     PIC 9(01).             
019628         10  TDB-TDAA-IMG-PG-TYPE-X.                              
019630             15  TDB-TDAA-IMG-PG-TYPE      PIC X(01).             
019632         10  TDB-TDAA-CONT-LMT-CLC-X.                             
019634             15  TDB-TDAA-CONT-LMT-CLC    PIC 9(5)V99.            
019636         10  TDB-TDAA-CONT-LMT-ENT-X.                             
019638             15  TDB-TDAA-CONT-LMT-ENT     PIC 9(5)V99.           
019640         10  TDB-TDAA-MEMO-DB-X.                                  
019642             15  TDB-TDAA-MEMO-DB          PIC S9(12)V99.         
019644         10  TDB-TDAA-MEMO-CR-X.                                  
019646             15  TDB-TDAA-MEMO-CR          PIC S9(12)V99.         
019648         10  TDB-TDAA-MEMO-DB-2-X.                                
019650             15  TDB-TDAA-MEMO-DB-2        PIC S9(12)V99.         
019652         10  TDB-TDAA-MEMO-CR-2-X.                                
019654             15  TDB-TDAA-MEMO-CR-2        PIC S9(12)V99.         
019656         10  TDB-TDAA-RT-AT-CONV-X.                               
019658             15  TDB-TDAA-RT-AT-CONV       PIC 9(2)V9(3).         
019660         10  TDB-TDAA-ACCR-AT-CONV-X.                             
019662             15  TDB-TDAA-ACCR-AT-CONV     PIC S9(12)V9(6).       
019664         10  TDB-TDAA-RT-AT-ACRDT-X.                              
019666             15  TDB-TDAA-RT-AT-ACRDT      PIC 9(2)V9(3).         
019668         10  TDB-TDAA-BAL-AT-ACRDT-X.                             
019670             15  TDB-TDAA-BAL-AT-ACRDT     PIC S9(12)V9(2).       
019672         10  TDB-TDAA-ZERO-RT-ALLOW-X.                            
019674             15  TDB-TDAA-ZERO-RT-ALLOW    PIC 9.                 
019676         10  TDB-TDAA-EMAIL-NTC-X.                                
019678             15  TDB-TDAA-EMAIL-NTC        PIC 9.                 
019680         10  TDB-TDAA-EMAIL-STMT-X.                               
019682             15  TDB-TDAA-EMAIL-STMT       PIC 9.                 
019684         10  TDB-TDAA-FRAUD-CK-DT-X.                              
019686             15  TDB-TDAA-FRAUD-CK-DT      PIC 9(8).              
019688         10  TDB-TDAA-FRAUD-CK-CNT-X.                             
019690             15  TDB-TDAA-FRAUD-CK-CNT     PIC 9(3).              
019692         10  TDB-TDAA-FRAUD-CK-AMT-X.                             
019694             15  TDB-TDAA-FRAUD-CK-AMT     PIC S9(12)V9(2).       
019696         10  TDB-TDAA-MISC-ACCTNO-X.                              
019698             15  TDB-TDAA-MISC-ACCTNO      PIC 9(8).              
019700         10  TDB-TDAA-RMD-MAN-CALC         PIC 9(1).              
019702         10  TDB-TDAA-RMD-AMOUNT           PIC S9(12)V9(2).       
019704         10  TDB-TDAA-BROKERAGE-ID         PIC X(10).             
019706         10  TDB-TDAA-EV-LARGE-TRX         PIC X(01).             
019708         10  TDB-TDAA-EV-MAT-AMT           PIC S9(12)V9(2).       
019710         10  TDB-TDAA-EV-DISP-ACCT         PIC 9(22).             
019712         10  TDB-TDAA-EV-COMP-ACCT         PIC 9(22).             
019714         10  TDB-TDAA-EV-PUBLIC-ID         PIC X(08).             
019716         10  TDB-TDAA-EV-MAT-TYPE          PIC X(01).             
019718         10  TDB-TDAA-EV-INT-TYPE          PIC X(01).             
019720         10  TDB-TDAA-EV-ACCT-TYP          PIC X(01).             
019722         10  TDB-TDAA-EV-WHLD-PCT          PIC 9(02).             
019724         10  TDB-TDAA-EV-NON-ACCR          PIC X(01).             
019726         10  TDB-TDAA-EV-CLOSED                 PIC X(01).        
019728         10  TDB-TDAA-EV-CLOSE-MO          PIC X(01).             
019730         10  TDB-TDAA-EV-OPEN-MO           PIC X(01).             
019732         10  TDB-TDAA-EV-ANN-INT           PIC S9(12)V9(2).       
019734         10  TDB-TDAA-EV-ORIG-RT           PIC 9(2)V9(3).         
019736         10  TDB-TDAA-EV-DLY-INT           PIC S9(12)V9(6).       
019738         10  TDB-TDAA-EV-INT-PAY           PIC S9(12)V9(6).       
019740         10  TDB-TDAA-EV-AVAIL-BL          PIC S9(12)V9(2).       
019742         10  TDB-TDAA-EV-RETAIN            PIC X(01).             
019744         10  TDB-TDAA-EV-CL-RETAIN         PIC X(01).             
019746         10  TDB-TDAA-EV-TIMES-REN         PIC 9(05).             
019748         10  TDB-TDAA-EV-CURR-BAL          PIC S9(12)V9(02).      
019750         10  TDB-TDAA-MONY-SRC-CD2         PIC X(03).             
019752         10  TDB-TDAA-INHERIT-IRA          PIC 9(01).             
019754         10  TDB-TDAA-LIFE-FACTOR          PIC 9(02)V9(1).        
019756         10  TDB-TDAA-BRKR-DEP-CAT         PIC 9(01).             
019758         10  TDB-TDAA-LINE-OF-BUS          PIC 9(4).              
019760         10  TDB-TDAA-1ST-STMT             PIC 9(01).             
019762         10  TDB-TDAA-POSTAL-CITY          PIC X(40).             
019764         10  TDB-TDAA-POSTAL-CNTRY         PIC X(02).             
019766         10  TDB-TDAA-CITIZN-CNTRY         PIC X(02).             
019768         10  TDB-TDAA-CUSTM-FIELDS         PIC 9(01).             
019770         10  TDB-TDAA-AVG-STEP-RT          PIC 9(2)V9(3).         
019772         10  TDB-TDAA-MONITOR-INQ          PIC 9(01).             
019774         10  TDB-TDAA-IGL-GRP-2            PIC 9(02).             
019776         10  TDB-TDAA-AGG-DAYS-QTD         PIC 9(03).             
019778         10  TDB-TDAA-AGG-BAL-QTD          PIC S9(15)V9(2).       
019780         10  TDB-TDAA-IGL-GRP-3            PIC 9(02).             
019782         10  TDB-TDAA-ALT-ADDR-EOY         PIC 9(01).             
019784         10  TDB-TDAA-1042S-TAX-ID         PIC X(22).             
019786         10  TDB-TDAA-LEC                  PIC X(01).             
019788         10  TDB-TDAA-BAL-AT-CLOSE         PIC S9(12)V9(2).       
019790         10  TDB-TDAA-AVL-CAP-INT          PIC S9(6)V9(2).        
019792         10  TDB-TDAA-FIDM-TR-FUND-X.                             
019794             15  TDB-TDAA-FIDM-TR-FUND     PIC 9(01).             
019796         10  TDB-TDAA-IRS-FRM-DLVR-X.                             
019798             15  TDB-TDAA-IRS-FRM-DLVR     PIC 9(01).             
019800         10  TDB-TDAA-PROVINCE             PIC X(02).             
019802         10  TDB-TDAA-PROMOTION            PIC X(25).             
019804         10  TDB-TDAA-NONDB-FIELDS.                               
019806             15  TDB-TDAA-DAYS-INTO-PER    PIC 9(5).              
019808             15  TDB-TDAA-CURR-PAYOFF      PIC S9(9)V9(2).        
019810             15  TDB-TDAA-MANUAL-RT-X      PIC X(5).              
019812             15  TDB-TDAA-MANUAL-RT-RE   REDEFINES                
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 1,063 lines from 8840 to 9902.

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

