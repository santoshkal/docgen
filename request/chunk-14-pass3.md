# LLM Request Debug File
Generated: 2025-11-13T20:27:09.524354

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 14/55
- **Model**: gpt-4.1
- **Chunk Number**: 14
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~14,918 tokens
- **Total Input**: ~16,876 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 14/55" (ID: detailed-code-explanation)

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


**CHUNK 14 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 14 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 6255 to 6846 (592 lines)\nChunk Tokens (estimated): ~12,161\nActual Input Tokens: 13,567 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 6255-6846 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 14 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 14 of 55.\n\n\n=============================================================================\nCHUNK 14 SOURCE CODE (Lines 6255-6846)\n=============================================================================\n\n```cobol\n012518                 RATE-TDARR-RATE-DATA.                            \n012520                 20 RATE-TDATR-TIER-BAL1    PIC 9(08)V99.         \n012522                 20 RATE-TDATR-TIER-INCR1   PIC S99V999.          \n012524                 20 RATE-TDATR-TIER-BAL2    PIC 9(08)V99.         \n012526                 20 RATE-TDATR-TIER-INCR2   PIC S99V999.          \n012528                 20 RATE-TDATR-TIER-BAL3    PIC 9(08)V99.         \n012530                 20 RATE-TDATR-TIER-INCR3   PIC S99V999.          \n012532                 20 RATE-TDATR-TIER-BAL4    PIC 9(08)V99.         \n012534                 20 RATE-TDATR-TIER-INCR4   PIC S99V999.          \n012536                 20 RATE-TDATR-TIER-BAL5    PIC 9(08)V99.         \n012538                 20 RATE-TDATR-TIER-INCR5   PIC S99V999.          \n012540                 20 RATE-TDATR-TIER-BAL6    PIC 9(08)V99.         \n012542                 20 RATE-TDATR-TIER-INCR6   PIC S99V999.          \n012544                 20 RATE-TDATR-TIER-BAL7    PIC 9(08)V99.         \n012546                 20 RATE-TDATR-TIER-INCR7   PIC S99V999.          \n012548                 20 RATE-TDATR-TIER-BAL8    PIC 9(08)V99.         \n012550                 20 RATE-TDATR-TIER-INCR8   PIC S99V999.          \n012552                 20 RATE-TDATR-TIER-BAL9    PIC 9(08)V99.         \n012554                 20 RATE-TDATR-TIER-INCR9   PIC S99V999.          \n012556                 20 RATE-TDATR-TIER-BAL10   PIC 9(08)V99.         \n012558                 20 RATE-TDATR-TIER-INCR10  PIC S99V999.          \n012560                 20 RATE-TDATR-TIER-BAL11   PIC 9(08)V99.         \n012562                 20 RATE-TDATR-TIER-INCR11  PIC S99V999.          \n012564                 20 RATE-TDATR-TIER-BAL12   PIC 9(08)V99.         \n012566                 20 RATE-TDATR-TIER-INCR12  PIC S99V999.          \n012568                 20 RATE-TDATR-TIER-BAL13   PIC 9(08)V99.         \n012570                 20 RATE-TDATR-TIER-INCR13  PIC S99V999.          \n012572                 20 RATE-TDATR-TIER-BAL14   PIC 9(08)V99.         \n012574                 20 RATE-TDATR-TIER-INCR14  PIC S99V999.          \n012576                 20 RATE-TDATR-TIER-BAL15   PIC 9(08)V99.         \n012578                 20 RATE-TDATR-TIER-INCR15  PIC S99V999.          \n012580                                                                  \n012582     05  TOTAL-SCREEN-DATA.                                       \n012584         10  TOTAL-SUB                     PIC 9(2)  VALUE 0.     \n012586         10  TOTAL-MAX                     PIC 9(2)  VALUE 13.    \n012588         10  TOTAL-ENTRIES                 PIC 9(2)  VALUE 0.     \n012590         10  TOTAL-TABLE    OCCURS 14 TIMES.                      \n012592             15  TOTAL-TOTAL-CD            PIC 9(03).             \n012594             15  TOTAL-APPL                PIC 9.                 \n012596             15  TOTAL-VOID-DATE           PIC 9(08).             \n012598             15  TOTAL-VOID-PUB-ID         PIC X(8).              \n012600             15  TOTAL-ADD-DATE            PIC 9(8).              \n012602             15  TOTAL-ADD-TIME            PIC 9(8).              \n012604             15  TOTAL-TOTAL-DATA.                                \n012606                 20  TOTAL-RENEW-CD        PIC 9(1).              \n012608                 20  TOTAL-OVERRIDE        PIC 9(1).              \n012610                 20  TOTAL-PENALTY-CD      PIC 9(3).              \n012612                 20  TOTAL-YIELD-NUM       PIC 9(3).              \n012614                 20  TOTAL-YIELD-DENOM     PIC 9(3).              \n012616                 20  TOTAL-WTHDRW-ALOW     PIC 9(1).              \n012618                 20  TOTAL-DPOSIT-ALOW     PIC 9(1).              \n012620                 20  TOTAL-RT-CHG-ALOW     PIC 9(1).              \n012622                 20  TOTAL-ODD-PAYMENT     PIC 9(1).              \n012624                 20  TOTAL-MAT-TYPE        PIC 9(1).              \n012626                 20  TOTAL-MAT-TERM        PIC 9(4).              \n012628                 20  TOTAL-CMPD-FREQ       PIC 9(1).              \n012630                 20  TOTAL-CMPD-NTRVL      PIC 9(4).              \n012632                 20  TOTAL-PAY-FREQ        PIC 9(1).              \n012634                 20  TOTAL-PAY-NTRVL       PIC 9(4).              \n012636                 20  TOTAL-STMT-FREQ       PIC 9(1).              \n012638                 20  TOTAL-STMT-NTRVL      PIC 9(4).              \n012640                 20  TOTAL-RTCHG-LIMIT     PIC 9(1).              \n012642                 20  TOTAL-CHG-NTRVL       PIC 9(3).              \n012644                 20  TOTAL-VAR-IMMED       PIC 9(1).              \n012646                 20  TOTAL-VAR-INT         PIC 9(1).              \n012648                 20  TOTAL-VAR-STEP        PIC 9(1).              \n012650                 20  TOTAL-VAR-SCHED       PIC 9(1).              \n012652                 20  TOTAL-VAR-BAL         PIC 9(1).              \n012654                 20  TOTAL-VAR-CUST        PIC 9(1).              \n012656                 20  TOTAL-POST-MAT        PIC 9(1).              \n012658                 20  TOTAL-END-OF-MAT      PIC 9(1).              \n012660                 20  TOTAL-END-OF-INT      PIC 9(1).              \n012662                 20  TOTAL-END-OF-CMPD     PIC 9(1).              \n012664                 20  TOTAL-END-OF-STMT     PIC 9(1).              \n012666                 20  TOTAL-REN-NTC         PIC 9(1).              \n012668                 20  TOTAL-PMAT-NTC        PIC 9(1).              \n012670                 20  TOTAL-INT-NTC         PIC 9(1).              \n012672                 20  TOTAL-RTCHG-NTC       PIC 9(1).              \n012674                 20  TOTAL-FLOOR-RT        PIC 9(2)V9(3).         \n012676                 20  TOTAL-FLOOR-INCR      PIC 9(2)V9(3).         \n012678                 20  TOTAL-CHG-NTC         PIC 9(1).              \n012680                 20  TOTAL-IRA-BACKED      PIC 9(1).              \n012682                 20  TOTAL-LEVEL-PAY       PIC 9(1).              \n012684                 20  TOTAL-CAP-RT-CHG      PIC X(1).              \n012686                 20  TOTAL-FEE-FREQ        PIC 9.                 \n012688                 20  TOTAL-FEE-NTRVL       PIC 9(4).              \n012690                 20  TOTAL-END-OF-FEE      PIC 9.                 \n012692                 20  TOTAL-ZERO-RT-ALLOW   PIC 9.                 \n012694                 20  TOTAL-FEE-AMT         PIC S9(9)V99.          \n012696                                                                  \n012698     05  HOLDS-TABLE-REC.                                         \n012700         10  HOLDS-SUB             PIC 9(02) VALUE 0.             \n012702         10  HOLDS-MAX             PIC 9(02) VALUE 12.            \n012704         10  HOLDS-ENTRIES         PIC 9(02) VALUE 0.             \n012706         10  HOLDS-TABLE   OCCURS 12 TIMES.                       \n012708             15  HOLDS-CUST        PIC 9(12).                     \n012710             15  HOLDS-ACCT        PIC 9(10).                     \n012712             15  HOLDS-HOLD-NBR    PIC 9(4).                      \n012714             15  HOLDS-TYPE        PIC X.                         \n012716             15  HOLDS-COMMENT     PIC X(40).                     \n012718             15  HOLDS-EXP-DATE    PIC 9(08).                     \n012720             15  HOLDS-ADD-DATE    PIC 9(08).                     \n012722             15  HOLDS-ADD-TIME    PIC 9(08).                     \n012724             15  HOLDS-VOID-DATE   PIC 9(08).                     \n012726             15  HOLDS-PLDG-ACCT   PIC 9(12).                     \n012728             15  HOLDS-PLDG-ACCT-S PIC 9(10).                     \n012730             15  HOLDS-VOID-PUB-ID PIC X(08).                     \n012732             15  HOLDS-SOURCE      PIC 99.                        \n012734             15  HOLDS-BK-TYPE     PIC X(01).                     \n012736             15  HOLDS-AMT         PIC S9(09)V99.                 \n012738                                                                  \n012740     05  ACT-TABLE-REC.                                           \n012742         10  ACT-SUB              PIC 9(02) VALUE 0.              \n012744         10  ACT-MAX              PIC 9(02) VALUE 17.             \n012746         10  ACT-ENTRIES          PIC 9(02) VALUE 0.              \n012748         10  ACT-HIST-IND         PIC 9(01).                      \n012750         10  ACT-TABLE OCCURS 17 TIMES.                           \n012752             15  ACT-EFF-DT       PIC 9(08).                      \n012754             15  ACT-DATE         PIC 9(08).                      \n012756             15  ACT-TIME         PIC 9(08).                      \n012758             15  ACT-SEQ-NBR      PIC 9(02).                      \n012760             15  ACT-SUB-ACCT     PIC 9(03).                      \n012762                                                                  \n012764     05  PCR-TABEL-REC.                                           \n012766         10  PCR-SUB              PIC 9(02) VALUE 0.              \n012768         10  PCR-MAX              PIC 9(02) VALUE 15.             \n012770         10  PCR-ENTRIES          PIC 9(02) VALUE 0.              \n012772         10  PCR-TABLE OCCURS 15 TIMES.                           \n012774             15  PCR-APPL-TYPE    PIC 9(01).                      \n012776             15  PCR-RPT-NBR      PIC 9(04).                      \n012778             15  PCR-SPECS        PIC X(65).                      \n012780             15  PCR-COPIES       PIC 9(02).                      \n012782             15  PCR-LASER-PRT    PIC 9(02).                      \n012784             15  PCR-FICHE-PRT    PIC 9(02).                      \n012786             15  PCR-PRT-DLY      PIC X(01).                      \n012788             15  PCR-DLY-IND      PIC X(07).                      \n012790             15  PCR-LST-PRT-D    PIC 9(08).                      \n012792             15  PCR-PRT-WK       PIC X(01).                      \n012794             15  PCR-WK-IND       PIC X(07).                      \n012796             15  PCR-LST-PRT-W    PIC 9(08).                      \n012798             15  PCR-PRT-MTH      PIC X(01).                      \n012800             15  PCR-LST-DAY-M    PIC X(01).                      \n012802             15  PCR-NXT-PRT-M    PIC 9(08).                      \n012804             15  PCR-LST-PRT-M    PIC 9(08).                      \n012806             15  PCR-PRT-QTR      PIC X(01).                      \n012808             15  PCR-LST-DAY-Q    PIC X(01).                      \n012810             15  PCR-NXT-PRT-Q    PIC 9(08).                      \n012812             15  PCR-LST-PRT-Q    PIC 9(08).                      \n012814             15  PCR-PRT-YR       PIC X(01).                      \n012816             15  PCR-NXT-PRT-Y    PIC 9(08).                      \n012818             15  PCR-LST-PRT-Y    PIC 9(08).                      \n012820             15  PCR-LUPD-DT      PIC 9(08).                      \n012822             15  PCR-LUPD-TM      PIC 9(06).                      \n012824             15  PCR-PUB-ID       PIC X(08).                      \n012826                                                                  \n012828     05  SCREEN-DATA-TABLE.                                       \n012830         10  SCREEN-TABLE OCCURS 17 TIMES.                        \n012832             15  SCREEN-TBL-SERIAL   PIC 9(12).                   \n012834                                                                  \n012836     05  KEY-VALUES.                                              \n012838         10  KEY-BANK             PIC 9(04).                      \n012840         10  KEY-APPL             PIC 9(01).                      \n012842         10  KEY-CUST             PIC 9(12).                      \n012844         10  KEY-ACCT             PIC 9(10).                      \n012846                                                                  \n012848                                                                  \n012850     05  HELP-SCREEN-AREA.                                        \n012852         10  HELP-INVOKE-IND      PIC X(1)   VALUE \"N\".           \n012854             88  HELP-IN-USE                 VALUE \"Y\".           \n012856                                                                  \n012858         10  HELP-RETURN-SCREEN   PIC X(2200).                    \n012860         10  HELP-POS-START       PIC 9(4).                       \n012862         10  HELP-POS-STOP        PIC 9(4).                       \n012864         10  HELP-FIELD-VALU      PIC X(80).                      \n012866         10  HELP-SCREEN-FORMAT   PIC X(12).                      \n012868                                                                  \n012870     05  SAVE-SCREEN-FORMAT       PIC X(12).                      \n012872     05  SAVE-SCREEN-DATA         PIC X(2200).                    \n012874                                                                  \n012876     05  RECALL-SCREEN-FORMAT     PIC X(12).                      \n012878                                                                  \n012880     05  WS-CHECK-WARNING         PIC X(01) VALUE \" \".            \n012882         88 WS-CHECK-FOR-WARNING            VALUE \"Y\".            \n012884                                                                  \n012886     05  WS-KEY-CHANGED-IND       PIC X(01) VALUE \"N\".            \n012888         88 WS-KEY-CHANGED                  VALUE \"Y\".            \n012890                                                                  \n012892     05  WS-BLANK-CDSUB-IND       PIC X(01) VALUE \"N\".            \n012894         88 WS-BLANK-CDSUB                  VALUE \"Y\".            \n012896                                                                  \n012898     05  WS-REDISPLAY-IND         PIC X(01) VALUE \"Y\".            \n012900         88 WS-REDISPLAY                    VALUE \"Y\".            \n012902                                                                  \n012904     05  WS-ACTION-LIST-IND       PIC X(01) VALUE \" \".            \n012906         88 WS-ADDITION-LIST                VALUE \"A\".            \n012908         88 WS-DELETION-LIST                VALUE \"D\".            \n012910         88 WS-CORRECTION-LIST              VALUE \"C\".            \n012912                                                                  \n012914     05  SCREEN-TOP-CODE          PIC 9(03) VALUE 0.              \n012916     05  SCREEN-BOT-CODE          PIC 9(03) VALUE 0.              \n012918                                                                  \n012920     05  SCREEN-TOP-RPT-NBR       PIC 9(04) VALUE 0.              \n012922     05  SCREEN-BOT-RPT-NBR       PIC 9(04) VALUE 0.              \n012924                                                                  \n012926     05  HOLD-SCREEN-KEY-X.                                       \n012928         10  HOLD-REGION-X           PIC X(01).                   \n012930         10  HOLD-START-RPT-NBR-X    PIC X(04).                   \n012932         10  HOLD-START-CODE-X       PIC X(03).                   \n012934         10  HOLD-START-EFF-DATE-X   PIC X(06).                   \n012936         10  HOLD-LIST-CURRENT-X     PIC X(01).                   \n012938         10  HOLD-CUST-X             PIC X(12).                   \n012940         10  HOLD-ACCT-X             PIC X(10).                   \n012942                                                                  \n012944     05  INPUT-TDAIR-DATA.                                        \n012946         10 INPUT-TDAIR-REGION        PIC 9(01) VALUE 0.          \n012948         10 INPUT-TDAIR-INDX-CD       PIC 9(02) VALUE 0.          \n012950         10 INPUT-TDAIR-EFF-DATE      PIC 9(06) VALUE 0.          \n012952         10 INPUT-TDAIR-LIST-CURRENT  PIC X(01) VALUE \"X\".        \n012954                                                                  \n012956     05  INPUT-TDAMR-DATA.                                        \n012958         10 INPUT-TDAMR-REGION        PIC 9(01) VALUE 0.          \n012960         10 INPUT-TDAMR-MARG-CD       PIC 9(02) VALUE 0.          \n012962         10 INPUT-TDAMR-EFF-DATE      PIC 9(06) VALUE 0.          \n012964         10 INPUT-TDAMR-LIST-CURRENT  PIC X(01) VALUE \"X\".        \n012966                                                                  \n012968     05  INPUT-TDARR-DATA.                                        \n012970         10 INPUT-TDARR-REGION        PIC 9(01) VALUE 0.          \n012972         10 INPUT-TDARR-RISE-CD       PIC 9(02) VALUE 0.          \n012974         10 INPUT-TDARR-EFF-DATE      PIC 9(06) VALUE 0.          \n012976         10 INPUT-TDARR-LIST-CURRENT  PIC X(01) VALUE \"X\".        \n012978                                                                  \n012980     05  INPUT-TDATR-DATA.                                        \n012982         10 INPUT-TDATR-REGION        PIC 9(01) VALUE 0.          \n012984         10 INPUT-TDATR-TIER-CD       PIC 9(02) VALUE 0.          \n012986         10 INPUT-TDATR-EFF-DATE      PIC 9(06) VALUE 0.          \n012988         10 INPUT-TDATR-LIST-CURRENT  PIC X(01) VALUE \"X\".        \n012990                                                                  \n012992     05  INPUT-TDATT-DATA.                                        \n012994         10  INPUT-TDATT-REGION       PIC 9(01) VALUE 0.          \n012996         10  INPUT-TDATT-TOTAL-CD     PIC 999   VALUE 0.          \n012998         10  INPUT-TDATT-LIST-CURRENT PIC X(01) VALUE \"Y\".        \n013000                                                                  \n013002     05  INPUT-TDAPC-DATA.                                        \n013004         10  INPUT-TDAPC-RPT-NBR      PIC 9(04) VALUE 0.          \n013006                                                                  \n013008     05  HOLD-INPUT-DATE              PIC 9(08).                  \n013010                                                                  \n013012     05  HOLD-TDB-STANDARD-AREA       PIC X(50).                  \n013014                                                                  \n013016     05  HOLD-READ-DATE               PIC 9(08).                  \n013018                                                                  \n013020     05  HOLD-NEW-FOR-ACTVC.                                      \n013022         10  HOLD-NEW-BANK              PIC 9(4).                 \n013024         10  HOLD-NEW-CUST              PIC 9(12).                \n013026         10  HOLD-NEW-ACCT              PIC 9(10).                \n013028         10  HOLD-NEW-APPL              PIC 9(1).                 \n013030         10  HOLD-NEW-BRCH              PIC 9(4).                 \n013032         10  HOLD-NEW-OFFICER           PIC X(3).                 \n013034         10  HOLD-NEW-PUB-ID            PIC X(8).                 \n013036                                                                  \n013038   05  OLD-TDAA-R-RT-INDX-CD-X        PIC XX.                     \n013040   05  OLD-TDAA-R-RT-INDX-CD-RE REDEFINES OLD-TDAA-R-RT-INDX-CD-X.\n013042       10  OLD-TDAA-R-RT-INDX-CD-9    PIC 99.                     \n013044   05  OLD-TDAA-R-RT-MARG-CD-X        PIC XX.                     \n013046   05  OLD-TDAA-R-RT-MARG-CD-RE REDEFINES OLD-TDAA-R-RT-MARG-CD-X.\n013048       10  OLD-TDAA-R-RT-MARG-CD-9    PIC 99.                     \n013050   05  OLD-TDAA-R-RT-TIER-CD-X        PIC XX.                     \n013052   05  OLD-TDAA-R-RT-TIER-CD-RE REDEFINES OLD-TDAA-R-RT-TIER-CD-X.\n013054       10  OLD-TDAA-R-RT-TIER-CD-9    PIC 99.                     \n013056   05  OLD-TDAA-R-RT-SR-CD-X          PIC XX.                     \n013058   05  OLD-TDAA-R-RT-SR-CD-RE REDEFINES OLD-TDAA-R-RT-SR-CD-X.    \n013060       10  OLD-TDAA-R-RT-SR-CD-9      PIC 99.                     \n013062   05  TDB-TDAA-R-RT-INDX-CD-X        PIC XX.                     \n013064   05  TDB-TDAA-R-RT-INDX-CD-RE REDEFINES TDB-TDAA-R-RT-INDX-CD-X.\n013066       10  TDB-TDAA-R-RT-INDX-CD-9    PIC 99.                     \n013068   05  TDB-TDAA-R-RT-MARG-CD-X        PIC XX.                     \n013070   05  TDB-TDAA-R-RT-MARG-CD-RE REDEFINES TDB-TDAA-R-RT-MARG-CD-X.\n013072       10  TDB-TDAA-R-RT-MARG-CD-9    PIC 99.                     \n013074   05  TDB-TDAA-R-RT-TIER-CD-X        PIC XX.                     \n013076   05  TDB-TDAA-R-RT-TIER-CD-RE REDEFINES TDB-TDAA-R-RT-TIER-CD-X.\n013078       10  TDB-TDAA-R-RT-TIER-CD-9    PIC 99.                     \n013080   05  TDB-TDAA-R-RT-SR-CD-X          PIC XX.                     \n013082   05  TDB-TDAA-R-RT-SR-CD-RE REDEFINES TDB-TDAA-R-RT-SR-CD-X.    \n013084       10  TDB-TDAA-R-RT-SR-CD-9      PIC 99.                     \n013086  05 HOLD-TDAA-R-RT-INDX-CD-X        PIC XX.                      \n013088  05 HOLD-TDAA-R-RT-INDX-CD-RE REDEFINES HOLD-TDAA-R-RT-INDX-CD-X.\n013090      10 HOLD-TDAA-R-RT-INDX-CD-9    PIC 99.                      \n013092  05 HOLD-TDAA-R-RT-MARG-CD-X        PIC XX.                      \n013094  05 HOLD-TDAA-R-RT-MARG-CD-RE REDEFINES HOLD-TDAA-R-RT-MARG-CD-X.\n013096      10 HOLD-TDAA-R-RT-MARG-CD-9    PIC 99.                      \n013098  05 HOLD-TDAA-R-RT-TIER-CD-X        PIC XX.                      \n013100  05 HOLD-TDAA-R-RT-TIER-CD-RE REDEFINES HOLD-TDAA-R-RT-TIER-CD-X.\n013102      10 HOLD-TDAA-R-RT-TIER-CD-9    PIC 99.                      \n013104  05 HOLD-TDAA-R-RT-SR-CD-X          PIC XX.                      \n013106  05 HOLD-TDAA-R-RT-SR-CD-RE REDEFINES HOLD-TDAA-R-RT-SR-CD-X.    \n013108      10 HOLD-TDAA-R-RT-SR-CD-9      PIC 99.                      \n013110                                                                  \n013112*** PLEASE REMEMBER TO UPDATE THE TDB,AND OLD FIELDS WHEN         \n013114*** UPDATING THE FOLLOWING HOLD FIELDS.                           \n013116*** IF DATABASE STRUCTURES ARE EXPANDED, PLEASE VERIFY THE        \n013118*** SORT-DATA FIELDS IN RPTWRK.XLIB ARE LARGE ENOUGH              \n013120*************************************************************     \n013122**  The hold areas for the database datsets are used in           \n013124**  capturing the changes to the record.  We can't use the        \n013126**  tdb record layouts because it has redefines for each          \n013128**  record type and we will be using that layout for reads of     \n013130**  multiple record types in a single process.                    \n013132                                                                  \n013134     05  HOLD-TDACUST.                                            \n013136         10  HOLD-TDAC-BANK             PIC 9(4).                 \n013138         10  HOLD-TDAC-CUST             PIC 9(12).                \n013140         10  HOLD-TDAC-BRCH             PIC 9(4).                 \n013142         10  HOLD-TDAC-STATUS           PIC X(1).                 \n013144         10  HOLD-TDAC-NAME-1           PIC X(40).                \n013146         10  HOLD-TDAC-NAME-AREA-1.                               \n013148             15  HOLD-TDAC-N1-KEY       PIC X(14).                \n013150             15  HOLD-TDAC-N1-FIRST     PIC X(40).                \n013152             15  HOLD-TDAC-N1-MID       PIC X(20).                \n013154             15  HOLD-TDAC-N1-LAST      PIC X(40).                \n013156             15  HOLD-TDAC-N1-PREFIX    PIC X(12).                \n013158             15  HOLD-TDAC-N1-SUFFIX    PIC X(12).                \n013160             15  HOLD-TDAC-N1-FAMILIAR  PIC X(20).                \n013162             15  HOLD-TDAC-N1-PRT-PFX   PIC X(01).                \n013164             15  HOLD-TDAC-N1-PRT-SFX   PIC X(01).                \n013166             15  HOLD-TDAC-N1-DESIGNAT  PIC X(20).                \n013168         10  HOLD-TDAC-NAME-2           PIC X(40).                \n013170         10  HOLD-TDAC-N2-MODIFIED      PIC X(01).                \n013172         10  HOLD-TDAC-N2-PRINT-CD      PIC X(01).                \n013174         10  HOLD-TDAC-NAME-AREA-2.                               \n013176             15  HOLD-TDAC-N2-KEY       PIC X(14).                \n013178             15  HOLD-TDAC-N2-FIRST     PIC X(40).                \n013180             15  HOLD-TDAC-N2-MID       PIC X(20).                \n013182             15  HOLD-TDAC-N2-LAST      PIC X(40).                \n013184             15  HOLD-TDAC-N2-PREFIX    PIC X(12).                \n013186             15  HOLD-TDAC-N2-SUFFIX    PIC X(12).                \n013188             15  HOLD-TDAC-N2-FAMILIAR  PIC X(20).                \n013190             15  HOLD-TDAC-N2-PRT-PFX   PIC X(01).                \n013192             15  HOLD-TDAC-N2-PRT-SFX   PIC X(01).                \n013194             15  HOLD-TDAC-N2-DESIGNAT  PIC X(20).                \n013196         10  HOLD-TDAC-NAME-3           PIC X(40).                \n013198         10  HOLD-TDAC-N3-MODIFIED      PIC X(01).                \n013200         10  HOLD-TDAC-N3-PRINT-CD      PIC X(01).                \n013202         10  HOLD-TDAC-NAME-AREA-3.                               \n013204             15  HOLD-TDAC-N3-KEY       PIC X(14).                \n013206             15  HOLD-TDAC-N3-FIRST     PIC X(40).                \n013208             15  HOLD-TDAC-N3-MID       PIC X(20).                \n013210             15  HOLD-TDAC-N3-LAST      PIC X(40).                \n013212             15  HOLD-TDAC-N3-PREFIX    PIC X(12).                \n013214             15  HOLD-TDAC-N3-SUFFIX    PIC X(12).                \n013216             15  HOLD-TDAC-N3-FAMILIAR  PIC X(20).                \n013218             15  HOLD-TDAC-N3-PRT-PFX   PIC X(01).                \n013220             15  HOLD-TDAC-N3-PRT-SFX   PIC X(01).                \n013222             15  HOLD-TDAC-N3-DESIGNAT  PIC X(20).                \n013224         10  HOLD-TDAC-ADDR-KEY         PIC X(28).                \n013226         10  HOLD-TDAC-ADDR-1           PIC X(40).                \n013228         10  HOLD-TDAC-ADDR-2           PIC X(40).                \n013230         10  HOLD-TDAC-CITY             PIC X(40).                \n013232         10  HOLD-TDAC-STATE            PIC X(2).                 \n013234         10  HOLD-TDAC-PROVINCE         PIC X(2).                 \n013236         10  HOLD-TDAC-COUNTRY          PIC X(2).                 \n013238         10  HOLD-TDAC-ZIP-CODE.                                  \n013240             15  HOLD-TDAC-ZIP          PIC 9(5).                 \n013242             15  HOLD-TDAC-ZIP-4        PIC 9(4).                 \n013244         10  HOLD-TDAC-LONGITUDE        PIC S9(3)V9(6).           \n013246         10  HOLD-TDAC-LATITUDE         PIC S9(3)V9(6).           \n013248         10  HOLD-TDAC-MAIL-CD          PIC 9(1).                 \n013250         10  HOLD-TDAC-TICKLER-FLAG     PIC 9(1).                 \n013252         10  HOLD-TDAC-RESIDENT-CD      PIC 9(1).                 \n013254         10  HOLD-TDAC-ALIEN-CD         PIC 9(1).                 \n013256         10  HOLD-TDAC-SHT-NAME         PIC X(20).                \n013258         10  HOLD-TDAC-BAR-CD           PIC 9(3).                 \n013260         10  HOLD-TDAC-PHONE-1          PIC 9(10).                \n013262         10  HOLD-TDAC-PHONE-2          PIC 9(10).                \n013264         10  HOLD-TDAC-TIN-CD           PIC X(1).                 \n013266         10  HOLD-TDAC-TIN-CERT-CD      PIC 9(1).                 \n013268         10  HOLD-TDAC-TIN-CERT-DT      PIC 9(8).                 \n013270         10  HOLD-TDAC-TIN-NBR          PIC 9(9).                 \n013272         10  HOLD-TDAC-OFFICER          PIC X(3).                 \n013274         10  HOLD-TDAC-EMP-CD           PIC X(1).                 \n013276         10  HOLD-TDAC-FREE-MARK        PIC X(24).                \n013278         10  HOLD-TDAC-INQ-SECR-CD      PIC 9(1).                 \n013280         10  HOLD-TDAC-PRIVACY          PIC 9(1).                 \n013282         10  HOLD-TDAC-BK-DEF-CD1       PIC X(1).                 \n013284         10  HOLD-TDAC-BK-DEF-CD2       PIC X(1).                 \n013286         10  HOLD-TDAC-BK-DEF-CD3       PIC X(1).                 \n013288         10  HOLD-TDAC-BK-DEF-CD4       PIC X(1).                 \n013290         10  HOLD-TDAC-BK-DEF-CD5       PIC X(1).                 \n013292         10  HOLD-TDAC-EMPLOYEE-ID      PIC X(8).                 \n013294         10  HOLD-TDAC-EMAIL-ADDR       PIC X(100).               \n013296         10 HOLD-TDAC-EMAIL-ADDR-R REDEFINES HOLD-TDAC-EMAIL-ADDR.\n013298             15  HOLD-TDAC-EMAIL-ADDR-1-30  PIC X(30).            \n013300             15  HOLD-TDAC-EMAIL-ADDR-31-60 PIC X(30).            \n013302             15  HOLD-TDAC-EMAIL-ADDR-61-90 PIC X(30).            \n013304             15  HOLD-TDAC-EMAIL-ADDR-91-100                      \n013306                                           PIC X(10).             \n013308         10 HOLD-TDAC-EMAIL-ADDR-RR                               \n013310                                   REDEFINES HOLD-TDAC-EMAIL-ADDR.\n013312             15  HOLD-TDAC-EMAIL-ADDR-1-50  PIC X(50).            \n013314             15  HOLD-TDAC-EMAIL-ADDR-51-100 PIC X(50).           \n013316         10  HOLD-TDAC-EMAIL-PSSWRD     PIC X(12).                \n013318         10  HOLD-TDAC-GENDER           PIC X(1).                 \n013320         10  HOLD-TDAC-NEW-CUST         PIC 9(1).                 \n013322         10  HOLD-TDAC-OPEN-DT          PIC 9(8).                 \n013324         10  HOLD-TDAC-LUPD-DATE        PIC 9(8).                 \n013326         10  HOLD-TDAC-LUPD-TIME        PIC 9(8).                 \n013328         10  HOLD-TDAC-LST-CONTACT      PIC 9(8).                 \n013330         10  HOLD-TDAC-BIRTH-DT         PIC 9(8).                 \n013332         10  HOLD-TDAC-BIRTH-DT-2       PIC 9(8).                 \n013334         10  HOLD-TDAC-BIRTH-DT-3       PIC 9(8).                 \n013336         10  HOLD-TDAC-DEATH-DT         PIC 9(8).                 \n013338         10  HOLD-TDAC-ADD-DT           PIC 9(8).                 \n013340         10  HOLD-TDAC-ADD-TM           PIC 9(6).                 \n013342         10  HOLD-TDAC-ROTH-DATE        PIC 9(8).                 \n013344         10  HOLD-TDAC-CD-BAL           PIC S9(15)V9(2).          \n013346         10  HOLD-TDAC-CD-BAL-BYR       PIC S9(15)V9(2).          \n013348         10  HOLD-TDAC-CD-PENLTY        PIC S9(15)V9(2).          \n013350         10  HOLD-TDAC-CD-WTHLD         PIC S9(15)V9(2).          \n013352         10  HOLD-TDAC-CD-INT           PIC S9(15)V9(2).          \n013354         10  HOLD-TDAC-CD-OID-INT       PIC S9(15)V9(2).          \n013356         10  HOLD-TDAC-IRA-BAL          PIC S9(15)V9(2).          \n013358         10  HOLD-TDAC-IRA-BAL-BYR      PIC S9(15)V9(2).          \n013360         10  HOLD-TDAC-IRA-PENLTY       PIC S9(15)V9(2).          \n013362         10  HOLD-TDAC-IRA-WTHLD        PIC S9(15)V9(2).          \n013364         10  HOLD-TDAC-IRA-INT          PIC S9(15)V9(2).          \n013366         10  HOLD-TDAC-IRA-CONTR        PIC S9(15)V9(2).          \n013368         10  HOLD-TDAC-IRA-CONTR-LY     PIC S9(15)V9(2).          \n013370         10  HOLD-TDAC-IRA-DISTR        PIC S9(15)V9(2).          \n013372         10  HOLD-TDAC-IRA-DISTR-LY     PIC S9(15)V9(2).          \n013374         10  HOLD-TDAC-IRA-ROLLOVER     PIC S9(15)V9(2).          \n013376         10  HOLD-TDAC-IRA-TRF-IN       PIC S9(15)V9(2).          \n013378         10  HOLD-TDAC-IRA-TRF-OUT      PIC S9(15)V9(2).          \n013380         10  HOLD-TDAC-IRA-FAIR-MKT     PIC S9(15)V9(2).          \n013382         10  HOLD-TDAC-CIF-REMARK       PIC X.                    \n013384         10  HOLD-TDAC-CD-ST-WHLD       PIC S9(15)V9(2).          \n013386         10  HOLD-TDAC-IRA-ST-WHLD      PIC S9(15)V9(2).          \n013388         10  HOLD-TDAC-CURR-YR-AMT      PIC S9(15)V9(2)           \n013390                                            OCCURS 12 TIMES.      \n013392         10  HOLD-TDAC-LAST-YR-AMT      PIC S9(15)V9(2)           \n013394                                            OCCURS 12 TIMES.      \n013396         10  HOLD-TDAC-TIN-CD-2         PIC X(01).                \n013398         10  HOLD-TDAC-TIN-CRT-CD-2     PIC 9(01).                \n013400         10  HOLD-TDAC-TIN-CRT-DT-2     PIC 9(08).                \n013402         10  HOLD-TDAC-TIN-NBR-2        PIC 9(09).                \n013404         10  HOLD-TDAC-TIN-CD-3         PIC X(01).                \n013406         10  HOLD-TDAC-TIN-CRT-CD-3     PIC 9(01).                \n013408         10  HOLD-TDAC-TIN-CRT-DT-3     PIC 9(08).                \n013410         10  HOLD-TDAC-TIN-NBR-3        PIC 9(09).                \n013412         10  HOLD-TDAC-NAICS-CD         PIC 9(06).                \n013414         10  HOLD-TDAC-CIF-PASS-THR     PIC 9(01).                \n013416         10  HOLD-TDAC-EMAIL-NTC        PIC 9(01).                \n013418         10  HOLD-TDAC-RMD-YR-AMT       PIC S9(15)V9(2).          \n013420         10  HOLD-TDAC-ADDR-CHG-DT      PIC 9(08).                \n013422         10  HOLD-TDAC-WTHLD-CD         PIC 9(01).                \n013424         10  HOLD-TDAC-ST-WHLD-CD       PIC 9(01).                \n013426         10  HOLD-TDAC-WTHLD-AMT        PIC S9(12)V9(2).          \n013428         10  HOLD-TDAC-ST-WHLD-AMT      PIC S9(12)V9(2).          \n013430         10  HOLD-TDAC-FOREIGN-LANG     PIC X(01).                \n013432         10  HOLD-TDAC-L-ROLLOVR-DT     PIC 9(08).                \n013434         10  HOLD-TDAC-CUSTM-FIELDS     PIC 9(01).                \n013436         10  HOLD-TDAC-LLC-NAME         PIC X(40).                \n013438         10  HOLD-TDAC-LLC-TIN-CD       PIC X(01).                \n013440         10  HOLD-TDAC-LLC-TIN          PIC 9(09).                \n013442         10  HOLD-TDAC-FOREIGN-PHN      PIC X(20).                \n013444                                                                  \n013446     05  HOLD-TDACHK.                                             \n013448         10  HOLD-TDACK-BANK            PIC 9(04).                \n013450         10  HOLD-TDACK-BRCH            PIC 9(04).                \n013452         10  HOLD-TDACK-ADDR-CUST       PIC 9(12).                \n013454         10  HOLD-TDACK-CUST            PIC 9(12)                 \n013456                                                  OCCURS 10 TIMES.\n013458         10  HOLD-TDACK-ACCT            PIC 9(10)                 \n013460                                                  OCCURS 10 TIMES.\n013462         10  HOLD-TDACK-LUPD-DATE       PIC 9(08).                \n013464         10  HOLD-TDACK-LUPD-TIME       PIC 9(08).                \n013466         10  HOLD-TDACK-PUB-ID          PIC X(08).                \n013468                                                                  \n013470     05  HOLD-TDAACCT.                                            \n013472         10  HOLD-TDAA-G-KEY.                                     \n013474             15  HOLD-TDAA-BANK           PIC 9(4).               \n013476             15  HOLD-TDAA-BRCH           PIC 9(4).               \n013478             15  HOLD-TDAA-APPL           PIC 9(1).               \n013480             15  HOLD-TDAA-CUST           PIC 9(12).              \n013482             15  HOLD-TDAA-ACCT           PIC 9(10).              \n013484         10  HOLD-TDAA-G-DATA-OPT.                                \n013486             15  HOLD-TDAA-STATUS         PIC X(1).               \n013488             15  HOLD-TDAA-IRA-TYPE       PIC 9(2).               \n013490             15  HOLD-TDAA-ACCT-OPTION    PIC 9(2).               \n013492             15  HOLD-TDAA-DT-CONDENSED   PIC 9(8).               \n013494             15  HOLD-TDAA-CERT           PIC 9(7).               \n013496             15  HOLD-TDAA-SHT-NAME       PIC X(20).              \n013498             15  HOLD-TDAA-TITLE          PIC X(40).              \n013500             15  HOLD-TDAA-TITLE-PRINT    PIC X(1).               \n013502             15  HOLD-TDAA-ADDR-USAGE     PIC X(01).              \n013504             15  HOLD-TDAA-ADDR-ALT       PIC X(01).              \n013506             15  HOLD-TDAA-ADDR-TEMP      PIC X(01).              \n013508             15  HOLD-TDAA-TEMP-BEG-DT    PIC 9(04).              \n013510             15  HOLD-TDAA-TEMP-END-DT    PIC 9(04).              \n013512             15  HOLD-TDAA-TEMP-EFF-DT    PIC 9(08).              \n013514             15  HOLD-TDAA-TEMP-EXP-DT    PIC 9(08).              \n013516             15  HOLD-TDAA-END-OF-INT     PIC 9(1).               \n013518             15  HOLD-TDAA-END-OF-MAT     PIC 9(1).               \n013520             15  HOLD-TDAA-END-OF-STMT    PIC 9(1).               \n013522             15  HOLD-TDAA-END-OF-CMPD    PIC 9(1).               \n013524             15  HOLD-TDAA-END-OF-FEE     PIC 9(1).               \n013526             15  HOLD-TDAA-OFFICER        PIC X(3).               \n013528             15  HOLD-TDAA-OFFICER-2      PIC X(3).               \n013530             15  HOLD-TDAA-OFFICER-3      PIC X(3).               \n013532             15  HOLD-TDAA-FREE-MARK      PIC X(24).              \n013534             15  HOLD-TDAA-CLASS-CD       PIC X(1).               \n013536             15  HOLD-TDAA-CORR-BK-CD     PIC X(1).               \n013538             15  HOLD-TDAA-PUBLIC-FUND    PIC X(1).               \n013540             15  HOLD-TDAA-TRUST-CD       PIC X(1).               \n013542             15  HOLD-TDAA-RT-CHG-ALLOW   PIC 9(1).               \n013544             15  HOLD-TDAA-WTHDRW-ALLOW   PIC 9(1).               \n013546             15  HOLD-TDAA-DPOSIT-ALLOW   PIC 9(1).               \n013548             15  HOLD-TDAA-POST-MAT       PIC 9(1).               \n013550             15  HOLD-TDAA-RT-FLOOR       PIC 9(1).               \n013552             15  HOLD-TDAA-REPO-CD        PIC 9(1).               \n013554             15  HOLD-TDAA-TOTAL-CD       PIC 999.                \n013556             15 HOLD-TDAA-TOTAL-CD-R REDEFINES HOLD-TDAA-TOTAL-CD.\n013558                 20  HOLD-TDAA-TOTAL-CD-9  PIC 9(1).              \n013560                 20  HOLD-TDAA-TOTAL-CD-99 PIC 9(2).              \n013562             15  HOLD-TDAA-REN-TOTAL-CD   PIC 9(3).               \n013564             15  HOLD-TDAA-ORG-TOTAL-CD   PIC 9(3).               \n013566             15  HOLD-TDAA-INQ-SECR-CD    PIC 9(1).               \n013568             15  HOLD-TDAA-MAIL-CD        PIC 9(1).               \n013570             15  HOLD-TDAA-WTHD-REQD-CD   PIC 9(1).               \n013572             15  HOLD-TDAA-TICKLER-FLAG   PIC 9(1).               \n013574             15  HOLD-TDAA-DISP-CD        PIC 9(1).               \n013576             15  HOLD-TDAA-CLS-DISP-CD    PIC 9(1).               \n013578             15  HOLD-TDAA-DIST-STATUS    PIC 9(1).               \n013580             15  HOLD-TDAA-COMM-ACCT      PIC 9(1).               \n013582             15  HOLD-TDAA-RENEW-CD       PIC 9(1).               \n013584             15  HOLD-TDAA-PLEDGE-CD      PIC X(1).               \n013586             15  HOLD-TDAA-NEGOT-CD       PIC X(1).               \n013588             15  HOLD-TDAA-BENEF-CD       PIC 9(1).               \n013590             15  HOLD-TDAA-COMM-MAT-CD    PIC 9(1).               \n013592             15  HOLD-TDAA-NBR-BENEF      PIC 9(1).               \n013594             15  HOLD-TDAA-OVERRIDE       PIC 9(1).               \n013596             15  HOLD-TDAA-INT-CD         PIC 9(1).               \n013598             15  HOLD-TDAA-WTHLD-CD       PIC 9(1).               \n013600             15  HOLD-TDAA-WTHLD-AMT      PIC S9(12)V9(2).        \n013602             15  HOLD-TDAA-IGL-GRP        PIC 9(2).               \n013604             15  HOLD-TDAA-SUM-STMT-CD    PIC 9(1).               \n013606             15  HOLD-TDAA-REN-NTC-CD     PIC 9(1).               \n013608             15  HOLD-TDAA-PMAT-NTC-CD    PIC 9(1).               \n013610             15  HOLD-TDAA-RTCHG-NTC-CD   PIC 9(1).               \n013612             15  HOLD-TDAA-INT-NTC-CD     PIC 9(1).               \n013614             15  HOLD-TDAA-CHG-NTC        PIC 9(1).               \n013616             15  HOLD-TDAA-YIELD-NUM      PIC 9(3).               \n013618             15  HOLD-TDAA-YIELD-DENOM    PIC 9(3).               \n013620             15  HOLD-TDAA-CMPD-FREQ      PIC 9(1).               \n013622             15  HOLD-TDAA-CMPD-NTRVL     PIC 9(4).               \n013624             15  HOLD-TDAA-RT-CHG-LIMIT   PIC 9(1).               \n013626             15  HOLD-TDAA-VAR-RT-IMMED   PIC 9(1).               \n013628             15  HOLD-TDAA-VAR-RT-INT     PIC 9(1).               \n013630             15  HOLD-TDAA-VAR-RT-SCHED   PIC 9(1).               \n013632             15  HOLD-TDAA-VAR-RT-CUST    PIC 9(1).               \n013634             15  HOLD-TDAA-VAR-RT-BAL     PIC 9(1).               \n013636             15  HOLD-TDAA-RT-INDX-CD     PIC 9(2).               \n013638             15  HOLD-TDAA-R-RT-INDX-CD   PIC XX.                 \n013640             15  HOLD-TDAA-RT-MARG-CD     PIC 9(2).               \n013642             15  HOLD-TDAA-R-RT-MARG-CD   PIC XX.                 \n013644             15  HOLD-TDAA-RT-TIER-CD     PIC 9(2).               \n013646             15  HOLD-TDAA-R-RT-TIER-CD   PIC XX.                 \n013648             15  HOLD-TDAA-RT-SR-CD       PIC 9(2).               \n013650             15  HOLD-TDAA-R-RT-SR-CD     PIC XX.                 \n013652             15  HOLD-TDAA-RT-REGN-CD     PIC 9(2).               \n013654             15  HOLD-TDAA-RT-CHG-NTRVL   PIC 9(3).               \n013656             15  HOLD-TDAA-CAP-RT-CHG     PIC X.                  \n013658             15  HOLD-TDAA-R-TIER-RT-CH   PIC X.                  \n013660             15  HOLD-TDAA-ALERT-CD       PIC 9(2).               \n013662             15  HOLD-TDAA-ALERT-CD-2     PIC 9(2).               \n013664             15  HOLD-TDAA-ALERT-CD-3     PIC 9(2).               \n013666             15  HOLD-TDAA-CENSUS-TRACT   PIC 9(4)V9(2).          \n013668             15  HOLD-TDAA-MK-SEGMENT     PIC X(2).               \n013670             15  HOLD-TDAA-BK-DEF-TOT     PIC X(3).               \n013672             15  HOLD-TDAA-BK-DEF-CD1     PIC X(1).               \n013674             15  HOLD-TDAA-BK-DEF-CD2     PIC X(1).               \n013676             15  HOLD-TDAA-BK-DEF-CD3     PIC X(1).               \n013678             15  HOLD-TDAA-BK-DEF-CD4     PIC X(1).               \n013680             15  HOLD-TDAA-BK-DEF-CD5     PIC X(1).               \n013682             15  HOLD-TDAA-OID-METH       PIC 9(1).               \n013684             15  HOLD-TDAA-EOY-CD         PIC 9(1).               \n013686             15  HOLD-TDAA-B-NOTC-YR1     PIC 9(1).               \n013688             15  HOLD-TDAA-B-NOTC-YR2     PIC 9(1).               \n013690             15  HOLD-TDAA-B-NOTC-YR3     PIC 9(1).               \n013692             15  HOLD-TDAA-NO-COMB-IRS    PIC 9(1).               \n013694             15  HOLD-TDAA-PENLTY-CD      PIC 999.                \n013696             15  HOLD-TDAA-MONEY-SRC-CD   PIC X(1).               \n013698             15  HOLD-TDAA-INTERNET-CD-R  PIC 999.                \n013700             15  HOLD-TDAA-INTERNET-CD REDEFINES                  \n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 592 lines from 6255 to 6846.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 14,
  "total_chunks": 55,
  "start_line": 6255,
  "end_line": 6846,
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
- Source code length: 50113 characters

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
CHUNK 14 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 6255 to 6846 (592 lines)
Chunk Tokens (estimated): ~12,161
Actual Input Tokens: 13,567 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 6255-6846 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 14 of 55 chunks
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
      The source code below is only CHUNK 14 of 55.


=============================================================================
CHUNK 14 SOURCE CODE (Lines 6255-6846)
=============================================================================

```cobol
012518                 RATE-TDARR-RATE-DATA.                            
012520                 20 RATE-TDATR-TIER-BAL1    PIC 9(08)V99.         
012522                 20 RATE-TDATR-TIER-INCR1   PIC S99V999.          
012524                 20 RATE-TDATR-TIER-BAL2    PIC 9(08)V99.         
012526                 20 RATE-TDATR-TIER-INCR2   PIC S99V999.          
012528                 20 RATE-TDATR-TIER-BAL3    PIC 9(08)V99.         
012530                 20 RATE-TDATR-TIER-INCR3   PIC S99V999.          
012532                 20 RATE-TDATR-TIER-BAL4    PIC 9(08)V99.         
012534                 20 RATE-TDATR-TIER-INCR4   PIC S99V999.          
012536                 20 RATE-TDATR-TIER-BAL5    PIC 9(08)V99.         
012538                 20 RATE-TDATR-TIER-INCR5   PIC S99V999.          
012540                 20 RATE-TDATR-TIER-BAL6    PIC 9(08)V99.         
012542                 20 RATE-TDATR-TIER-INCR6   PIC S99V999.          
012544                 20 RATE-TDATR-TIER-BAL7    PIC 9(08)V99.         
012546                 20 RATE-TDATR-TIER-INCR7   PIC S99V999.          
012548                 20 RATE-TDATR-TIER-BAL8    PIC 9(08)V99.         
012550                 20 RATE-TDATR-TIER-INCR8   PIC S99V999.          
012552                 20 RATE-TDATR-TIER-BAL9    PIC 9(08)V99.         
012554                 20 RATE-TDATR-TIER-INCR9   PIC S99V999.          
012556                 20 RATE-TDATR-TIER-BAL10   PIC 9(08)V99.         
012558                 20 RATE-TDATR-TIER-INCR10  PIC S99V999.          
012560                 20 RATE-TDATR-TIER-BAL11   PIC 9(08)V99.         
012562                 20 RATE-TDATR-TIER-INCR11  PIC S99V999.          
012564                 20 RATE-TDATR-TIER-BAL12   PIC 9(08)V99.         
012566                 20 RATE-TDATR-TIER-INCR12  PIC S99V999.          
012568                 20 RATE-TDATR-TIER-BAL13   PIC 9(08)V99.         
012570                 20 RATE-TDATR-TIER-INCR13  PIC S99V999.          
012572                 20 RATE-TDATR-TIER-BAL14   PIC 9(08)V99.         
012574                 20 RATE-TDATR-TIER-INCR14  PIC S99V999.          
012576                 20 RATE-TDATR-TIER-BAL15   PIC 9(08)V99.         
012578                 20 RATE-TDATR-TIER-INCR15  PIC S99V999.          
012580                                                                  
012582     05  TOTAL-SCREEN-DATA.                                       
012584         10  TOTAL-SUB                     PIC 9(2)  VALUE 0.     
012586         10  TOTAL-MAX                     PIC 9(2)  VALUE 13.    
012588         10  TOTAL-ENTRIES                 PIC 9(2)  VALUE 0.     
012590         10  TOTAL-TABLE    OCCURS 14 TIMES.                      
012592             15  TOTAL-TOTAL-CD            PIC 9(03).             
012594             15  TOTAL-APPL                PIC 9.                 
012596             15  TOTAL-VOID-DATE           PIC 9(08).             
012598             15  TOTAL-VOID-PUB-ID         PIC X(8).              
012600             15  TOTAL-ADD-DATE            PIC 9(8).              
012602             15  TOTAL-ADD-TIME            PIC 9(8).              
012604             15  TOTAL-TOTAL-DATA.                                
012606                 20  TOTAL-RENEW-CD        PIC 9(1).              
012608                 20  TOTAL-OVERRIDE        PIC 9(1).              
012610                 20  TOTAL-PENALTY-CD      PIC 9(3).              
012612                 20  TOTAL-YIELD-NUM       PIC 9(3).              
012614                 20  TOTAL-YIELD-DENOM     PIC 9(3).              
012616                 20  TOTAL-WTHDRW-ALOW     PIC 9(1).              
012618                 20  TOTAL-DPOSIT-ALOW     PIC 9(1).              
012620                 20  TOTAL-RT-CHG-ALOW     PIC 9(1).              
012622                 20  TOTAL-ODD-PAYMENT     PIC 9(1).              
012624                 20  TOTAL-MAT-TYPE        PIC 9(1).              
012626                 20  TOTAL-MAT-TERM        PIC 9(4).              
012628                 20  TOTAL-CMPD-FREQ       PIC 9(1).              
012630                 20  TOTAL-CMPD-NTRVL      PIC 9(4).              
012632                 20  TOTAL-PAY-FREQ        PIC 9(1).              
012634                 20  TOTAL-PAY-NTRVL       PIC 9(4).              
012636                 20  TOTAL-STMT-FREQ       PIC 9(1).              
012638                 20  TOTAL-STMT-NTRVL      PIC 9(4).              
012640                 20  TOTAL-RTCHG-LIMIT     PIC 9(1).              
012642                 20  TOTAL-CHG-NTRVL       PIC 9(3).              
012644                 20  TOTAL-VAR-IMMED       PIC 9(1).              
012646                 20  TOTAL-VAR-INT         PIC 9(1).              
012648                 20  TOTAL-VAR-STEP        PIC 9(1).              
012650                 20  TOTAL-VAR-SCHED       PIC 9(1).              
012652                 20  TOTAL-VAR-BAL         PIC 9(1).              
012654                 20  TOTAL-VAR-CUST        PIC 9(1).              
012656                 20  TOTAL-POST-MAT        PIC 9(1).              
012658                 20  TOTAL-END-OF-MAT      PIC 9(1).              
012660                 20  TOTAL-END-OF-INT      PIC 9(1).              
012662                 20  TOTAL-END-OF-CMPD     PIC 9(1).              
012664                 20  TOTAL-END-OF-STMT     PIC 9(1).              
012666                 20  TOTAL-REN-NTC         PIC 9(1).              
012668                 20  TOTAL-PMAT-NTC        PIC 9(1).              
012670                 20  TOTAL-INT-NTC         PIC 9(1).              
012672                 20  TOTAL-RTCHG-NTC       PIC 9(1).              
012674                 20  TOTAL-FLOOR-RT        PIC 9(2)V9(3).         
012676                 20  TOTAL-FLOOR-INCR      PIC 9(2)V9(3).         
012678                 20  TOTAL-CHG-NTC         PIC 9(1).              
012680                 20  TOTAL-IRA-BACKED      PIC 9(1).              
012682                 20  TOTAL-LEVEL-PAY       PIC 9(1).              
012684                 20  TOTAL-CAP-RT-CHG      PIC X(1).              
012686                 20  TOTAL-FEE-FREQ        PIC 9.                 
012688                 20  TOTAL-FEE-NTRVL       PIC 9(4).              
012690                 20  TOTAL-END-OF-FEE      PIC 9.                 
012692                 20  TOTAL-ZERO-RT-ALLOW   PIC 9.                 
012694                 20  TOTAL-FEE-AMT         PIC S9(9)V99.          
012696                                                                  
012698     05  HOLDS-TABLE-REC.                                         
012700         10  HOLDS-SUB             PIC 9(02) VALUE 0.             
012702         10  HOLDS-MAX             PIC 9(02) VALUE 12.            
012704         10  HOLDS-ENTRIES         PIC 9(02) VALUE 0.             
012706         10  HOLDS-TABLE   OCCURS 12 TIMES.                       
012708             15  HOLDS-CUST        PIC 9(12).                     
012710             15  HOLDS-ACCT        PIC 9(10).                     
012712             15  HOLDS-HOLD-NBR    PIC 9(4).                      
012714             15  HOLDS-TYPE        PIC X.                         
012716             15  HOLDS-COMMENT     PIC X(40).                     
012718             15  HOLDS-EXP-DATE    PIC 9(08).                     
012720             15  HOLDS-ADD-DATE    PIC 9(08).                     
012722             15  HOLDS-ADD-TIME    PIC 9(08).                     
012724             15  HOLDS-VOID-DATE   PIC 9(08).                     
012726             15  HOLDS-PLDG-ACCT   PIC 9(12).                     
012728             15  HOLDS-PLDG-ACCT-S PIC 9(10).                     
012730             15  HOLDS-VOID-PUB-ID PIC X(08).                     
012732             15  HOLDS-SOURCE      PIC 99.                        
012734             15  HOLDS-BK-TYPE     PIC X(01).                     
012736             15  HOLDS-AMT         PIC S9(09)V99.                 
012738                                                                  
012740     05  ACT-TABLE-REC.                                           
012742         10  ACT-SUB              PIC 9(02) VALUE 0.              
012744         10  ACT-MAX              PIC 9(02) VALUE 17.             
012746         10  ACT-ENTRIES          PIC 9(02) VALUE 0.              
012748         10  ACT-HIST-IND         PIC 9(01).                      
012750         10  ACT-TABLE OCCURS 17 TIMES.                           
012752             15  ACT-EFF-DT       PIC 9(08).                      
012754             15  ACT-DATE         PIC 9(08).                      
012756             15  ACT-TIME         PIC 9(08).                      
012758             15  ACT-SEQ-NBR      PIC 9(02).                      
012760             15  ACT-SUB-ACCT     PIC 9(03).                      
012762                                                                  
012764     05  PCR-TABEL-REC.                                           
012766         10  PCR-SUB              PIC 9(02) VALUE 0.              
012768         10  PCR-MAX              PIC 9(02) VALUE 15.             
012770         10  PCR-ENTRIES          PIC 9(02) VALUE 0.              
012772         10  PCR-TABLE OCCURS 15 TIMES.                           
012774             15  PCR-APPL-TYPE    PIC 9(01).                      
012776             15  PCR-RPT-NBR      PIC 9(04).                      
012778             15  PCR-SPECS        PIC X(65).                      
012780             15  PCR-COPIES       PIC 9(02).                      
012782             15  PCR-LASER-PRT    PIC 9(02).                      
012784             15  PCR-FICHE-PRT    PIC 9(02).                      
012786             15  PCR-PRT-DLY      PIC X(01).                      
012788             15  PCR-DLY-IND      PIC X(07).                      
012790             15  PCR-LST-PRT-D    PIC 9(08).                      
012792             15  PCR-PRT-WK       PIC X(01).                      
012794             15  PCR-WK-IND       PIC X(07).                      
012796             15  PCR-LST-PRT-W    PIC 9(08).                      
012798             15  PCR-PRT-MTH      PIC X(01).                      
012800             15  PCR-LST-DAY-M    PIC X(01).                      
012802             15  PCR-NXT-PRT-M    PIC 9(08).                      
012804             15  PCR-LST-PRT-M    PIC 9(08).                      
012806             15  PCR-PRT-QTR      PIC X(01).                      
012808             15  PCR-LST-DAY-Q    PIC X(01).                      
012810             15  PCR-NXT-PRT-Q    PIC 9(08).                      
012812             15  PCR-LST-PRT-Q    PIC 9(08).                      
012814             15  PCR-PRT-YR       PIC X(01).                      
012816             15  PCR-NXT-PRT-Y    PIC 9(08).                      
012818             15  PCR-LST-PRT-Y    PIC 9(08).                      
012820             15  PCR-LUPD-DT      PIC 9(08).                      
012822             15  PCR-LUPD-TM      PIC 9(06).                      
012824             15  PCR-PUB-ID       PIC X(08).                      
012826                                                                  
012828     05  SCREEN-DATA-TABLE.                                       
012830         10  SCREEN-TABLE OCCURS 17 TIMES.                        
012832             15  SCREEN-TBL-SERIAL   PIC 9(12).                   
012834                                                                  
012836     05  KEY-VALUES.                                              
012838         10  KEY-BANK             PIC 9(04).                      
012840         10  KEY-APPL             PIC 9(01).                      
012842         10  KEY-CUST             PIC 9(12).                      
012844         10  KEY-ACCT             PIC 9(10).                      
012846                                                                  
012848                                                                  
012850     05  HELP-SCREEN-AREA.                                        
012852         10  HELP-INVOKE-IND      PIC X(1)   VALUE "N".           
012854             88  HELP-IN-USE                 VALUE "Y".           
012856                                                                  
012858         10  HELP-RETURN-SCREEN   PIC X(2200).                    
012860         10  HELP-POS-START       PIC 9(4).                       
012862         10  HELP-POS-STOP        PIC 9(4).                       
012864         10  HELP-FIELD-VALU      PIC X(80).                      
012866         10  HELP-SCREEN-FORMAT   PIC X(12).                      
012868                                                                  
012870     05  SAVE-SCREEN-FORMAT       PIC X(12).                      
012872     05  SAVE-SCREEN-DATA         PIC X(2200).                    
012874                                                                  
012876     05  RECALL-SCREEN-FORMAT     PIC X(12).                      
012878                                                                  
012880     05  WS-CHECK-WARNING         PIC X(01) VALUE " ".            
012882         88 WS-CHECK-FOR-WARNING            VALUE "Y".            
012884                                                                  
012886     05  WS-KEY-CHANGED-IND       PIC X(01) VALUE "N".            
012888         88 WS-KEY-CHANGED                  VALUE "Y".            
012890                                                                  
012892     05  WS-BLANK-CDSUB-IND       PIC X(01) VALUE "N".            
012894         88 WS-BLANK-CDSUB                  VALUE "Y".            
012896                                                                  
012898     05  WS-REDISPLAY-IND         PIC X(01) VALUE "Y".            
012900         88 WS-REDISPLAY                    VALUE "Y".            
012902                                                                  
012904     05  WS-ACTION-LIST-IND       PIC X(01) VALUE " ".            
012906         88 WS-ADDITION-LIST                VALUE "A".            
012908         88 WS-DELETION-LIST                VALUE "D".            
012910         88 WS-CORRECTION-LIST              VALUE "C".            
012912                                                                  
012914     05  SCREEN-TOP-CODE          PIC 9(03) VALUE 0.              
012916     05  SCREEN-BOT-CODE          PIC 9(03) VALUE 0.              
012918                                                                  
012920     05  SCREEN-TOP-RPT-NBR       PIC 9(04) VALUE 0.              
012922     05  SCREEN-BOT-RPT-NBR       PIC 9(04) VALUE 0.              
012924                                                                  
012926     05  HOLD-SCREEN-KEY-X.                                       
012928         10  HOLD-REGION-X           PIC X(01).                   
012930         10  HOLD-START-RPT-NBR-X    PIC X(04).                   
012932         10  HOLD-START-CODE-X       PIC X(03).                   
012934         10  HOLD-START-EFF-DATE-X   PIC X(06).                   
012936         10  HOLD-LIST-CURRENT-X     PIC X(01).                   
012938         10  HOLD-CUST-X             PIC X(12).                   
012940         10  HOLD-ACCT-X             PIC X(10).                   
012942                                                                  
012944     05  INPUT-TDAIR-DATA.                                        
012946         10 INPUT-TDAIR-REGION        PIC 9(01) VALUE 0.          
012948         10 INPUT-TDAIR-INDX-CD       PIC 9(02) VALUE 0.          
012950         10 INPUT-TDAIR-EFF-DATE      PIC 9(06) VALUE 0.          
012952         10 INPUT-TDAIR-LIST-CURRENT  PIC X(01) VALUE "X".        
012954                                                                  
012956     05  INPUT-TDAMR-DATA.                                        
012958         10 INPUT-TDAMR-REGION        PIC 9(01) VALUE 0.          
012960         10 INPUT-TDAMR-MARG-CD       PIC 9(02) VALUE 0.          
012962         10 INPUT-TDAMR-EFF-DATE      PIC 9(06) VALUE 0.          
012964         10 INPUT-TDAMR-LIST-CURRENT  PIC X(01) VALUE "X".        
012966                                                                  
012968     05  INPUT-TDARR-DATA.                                        
012970         10 INPUT-TDARR-REGION        PIC 9(01) VALUE 0.          
012972         10 INPUT-TDARR-RISE-CD       PIC 9(02) VALUE 0.          
012974         10 INPUT-TDARR-EFF-DATE      PIC 9(06) VALUE 0.          
012976         10 INPUT-TDARR-LIST-CURRENT  PIC X(01) VALUE "X".        
012978                                                                  
012980     05  INPUT-TDATR-DATA.                                        
012982         10 INPUT-TDATR-REGION        PIC 9(01) VALUE 0.          
012984         10 INPUT-TDATR-TIER-CD       PIC 9(02) VALUE 0.          
012986         10 INPUT-TDATR-EFF-DATE      PIC 9(06) VALUE 0.          
012988         10 INPUT-TDATR-LIST-CURRENT  PIC X(01) VALUE "X".        
012990                                                                  
012992     05  INPUT-TDATT-DATA.                                        
012994         10  INPUT-TDATT-REGION       PIC 9(01) VALUE 0.          
012996         10  INPUT-TDATT-TOTAL-CD     PIC 999   VALUE 0.          
012998         10  INPUT-TDATT-LIST-CURRENT PIC X(01) VALUE "Y".        
013000                                                                  
013002     05  INPUT-TDAPC-DATA.                                        
013004         10  INPUT-TDAPC-RPT-NBR      PIC 9(04) VALUE 0.          
013006                                                                  
013008     05  HOLD-INPUT-DATE              PIC 9(08).                  
013010                                                                  
013012     05  HOLD-TDB-STANDARD-AREA       PIC X(50).                  
013014                                                                  
013016     05  HOLD-READ-DATE               PIC 9(08).                  
013018                                                                  
013020     05  HOLD-NEW-FOR-ACTVC.                                      
013022         10  HOLD-NEW-BANK              PIC 9(4).                 
013024         10  HOLD-NEW-CUST              PIC 9(12).                
013026         10  HOLD-NEW-ACCT              PIC 9(10).                
013028         10  HOLD-NEW-APPL              PIC 9(1).                 
013030         10  HOLD-NEW-BRCH              PIC 9(4).                 
013032         10  HOLD-NEW-OFFICER           PIC X(3).                 
013034         10  HOLD-NEW-PUB-ID            PIC X(8).                 
013036                                                                  
013038   05  OLD-TDAA-R-RT-INDX-CD-X        PIC XX.                     
013040   05  OLD-TDAA-R-RT-INDX-CD-RE REDEFINES OLD-TDAA-R-RT-INDX-CD-X.
013042       10  OLD-TDAA-R-RT-INDX-CD-9    PIC 99.                     
013044   05  OLD-TDAA-R-RT-MARG-CD-X        PIC XX.                     
013046   05  OLD-TDAA-R-RT-MARG-CD-RE REDEFINES OLD-TDAA-R-RT-MARG-CD-X.
013048       10  OLD-TDAA-R-RT-MARG-CD-9    PIC 99.                     
013050   05  OLD-TDAA-R-RT-TIER-CD-X        PIC XX.                     
013052   05  OLD-TDAA-R-RT-TIER-CD-RE REDEFINES OLD-TDAA-R-RT-TIER-CD-X.
013054       10  OLD-TDAA-R-RT-TIER-CD-9    PIC 99.                     
013056   05  OLD-TDAA-R-RT-SR-CD-X          PIC XX.                     
013058   05  OLD-TDAA-R-RT-SR-CD-RE REDEFINES OLD-TDAA-R-RT-SR-CD-X.    
013060       10  OLD-TDAA-R-RT-SR-CD-9      PIC 99.                     
013062   05  TDB-TDAA-R-RT-INDX-CD-X        PIC XX.                     
013064   05  TDB-TDAA-R-RT-INDX-CD-RE REDEFINES TDB-TDAA-R-RT-INDX-CD-X.
013066       10  TDB-TDAA-R-RT-INDX-CD-9    PIC 99.                     
013068   05  TDB-TDAA-R-RT-MARG-CD-X        PIC XX.                     
013070   05  TDB-TDAA-R-RT-MARG-CD-RE REDEFINES TDB-TDAA-R-RT-MARG-CD-X.
013072       10  TDB-TDAA-R-RT-MARG-CD-9    PIC 99.                     
013074   05  TDB-TDAA-R-RT-TIER-CD-X        PIC XX.                     
013076   05  TDB-TDAA-R-RT-TIER-CD-RE REDEFINES TDB-TDAA-R-RT-TIER-CD-X.
013078       10  TDB-TDAA-R-RT-TIER-CD-9    PIC 99.                     
013080   05  TDB-TDAA-R-RT-SR-CD-X          PIC XX.                     
013082   05  TDB-TDAA-R-RT-SR-CD-RE REDEFINES TDB-TDAA-R-RT-SR-CD-X.    
013084       10  TDB-TDAA-R-RT-SR-CD-9      PIC 99.                     
013086  05 HOLD-TDAA-R-RT-INDX-CD-X        PIC XX.                      
013088  05 HOLD-TDAA-R-RT-INDX-CD-RE REDEFINES HOLD-TDAA-R-RT-INDX-CD-X.
013090      10 HOLD-TDAA-R-RT-INDX-CD-9    PIC 99.                      
013092  05 HOLD-TDAA-R-RT-MARG-CD-X        PIC XX.                      
013094  05 HOLD-TDAA-R-RT-MARG-CD-RE REDEFINES HOLD-TDAA-R-RT-MARG-CD-X.
013096      10 HOLD-TDAA-R-RT-MARG-CD-9    PIC 99.                      
013098  05 HOLD-TDAA-R-RT-TIER-CD-X        PIC XX.                      
013100  05 HOLD-TDAA-R-RT-TIER-CD-RE REDEFINES HOLD-TDAA-R-RT-TIER-CD-X.
013102      10 HOLD-TDAA-R-RT-TIER-CD-9    PIC 99.                      
013104  05 HOLD-TDAA-R-RT-SR-CD-X          PIC XX.                      
013106  05 HOLD-TDAA-R-RT-SR-CD-RE REDEFINES HOLD-TDAA-R-RT-SR-CD-X.    
013108      10 HOLD-TDAA-R-RT-SR-CD-9      PIC 99.                      
013110                                                                  
013112*** PLEASE REMEMBER TO UPDATE THE TDB,AND OLD FIELDS WHEN         
013114*** UPDATING THE FOLLOWING HOLD FIELDS.                           
013116*** IF DATABASE STRUCTURES ARE EXPANDED, PLEASE VERIFY THE        
013118*** SORT-DATA FIELDS IN RPTWRK.XLIB ARE LARGE ENOUGH              
013120*************************************************************     
013122**  The hold areas for the database datsets are used in           
013124**  capturing the changes to the record.  We can't use the        
013126**  tdb record layouts because it has redefines for each          
013128**  record type and we will be using that layout for reads of     
013130**  multiple record types in a single process.                    
013132                                                                  
013134     05  HOLD-TDACUST.                                            
013136         10  HOLD-TDAC-BANK             PIC 9(4).                 
013138         10  HOLD-TDAC-CUST             PIC 9(12).                
013140         10  HOLD-TDAC-BRCH             PIC 9(4).                 
013142         10  HOLD-TDAC-STATUS           PIC X(1).                 
013144         10  HOLD-TDAC-NAME-1           PIC X(40).                
013146         10  HOLD-TDAC-NAME-AREA-1.                               
013148             15  HOLD-TDAC-N1-KEY       PIC X(14).                
013150             15  HOLD-TDAC-N1-FIRST     PIC X(40).                
013152             15  HOLD-TDAC-N1-MID       PIC X(20).                
013154             15  HOLD-TDAC-N1-LAST      PIC X(40).                
013156             15  HOLD-TDAC-N1-PREFIX    PIC X(12).                
013158             15  HOLD-TDAC-N1-SUFFIX    PIC X(12).                
013160             15  HOLD-TDAC-N1-FAMILIAR  PIC X(20).                
013162             15  HOLD-TDAC-N1-PRT-PFX   PIC X(01).                
013164             15  HOLD-TDAC-N1-PRT-SFX   PIC X(01).                
013166             15  HOLD-TDAC-N1-DESIGNAT  PIC X(20).                
013168         10  HOLD-TDAC-NAME-2           PIC X(40).                
013170         10  HOLD-TDAC-N2-MODIFIED      PIC X(01).                
013172         10  HOLD-TDAC-N2-PRINT-CD      PIC X(01).                
013174         10  HOLD-TDAC-NAME-AREA-2.                               
013176             15  HOLD-TDAC-N2-KEY       PIC X(14).                
013178             15  HOLD-TDAC-N2-FIRST     PIC X(40).                
013180             15  HOLD-TDAC-N2-MID       PIC X(20).                
013182             15  HOLD-TDAC-N2-LAST      PIC X(40).                
013184             15  HOLD-TDAC-N2-PREFIX    PIC X(12).                
013186             15  HOLD-TDAC-N2-SUFFIX    PIC X(12).                
013188             15  HOLD-TDAC-N2-FAMILIAR  PIC X(20).                
013190             15  HOLD-TDAC-N2-PRT-PFX   PIC X(01).                
013192             15  HOLD-TDAC-N2-PRT-SFX   PIC X(01).                
013194             15  HOLD-TDAC-N2-DESIGNAT  PIC X(20).                
013196         10  HOLD-TDAC-NAME-3           PIC X(40).                
013198         10  HOLD-TDAC-N3-MODIFIED      PIC X(01).                
013200         10  HOLD-TDAC-N3-PRINT-CD      PIC X(01).                
013202         10  HOLD-TDAC-NAME-AREA-3.                               
013204             15  HOLD-TDAC-N3-KEY       PIC X(14).                
013206             15  HOLD-TDAC-N3-FIRST     PIC X(40).                
013208             15  HOLD-TDAC-N3-MID       PIC X(20).                
013210             15  HOLD-TDAC-N3-LAST      PIC X(40).                
013212             15  HOLD-TDAC-N3-PREFIX    PIC X(12).                
013214             15  HOLD-TDAC-N3-SUFFIX    PIC X(12).                
013216             15  HOLD-TDAC-N3-FAMILIAR  PIC X(20).                
013218             15  HOLD-TDAC-N3-PRT-PFX   PIC X(01).                
013220             15  HOLD-TDAC-N3-PRT-SFX   PIC X(01).                
013222             15  HOLD-TDAC-N3-DESIGNAT  PIC X(20).                
013224         10  HOLD-TDAC-ADDR-KEY         PIC X(28).                
013226         10  HOLD-TDAC-ADDR-1           PIC X(40).                
013228         10  HOLD-TDAC-ADDR-2           PIC X(40).                
013230         10  HOLD-TDAC-CITY             PIC X(40).                
013232         10  HOLD-TDAC-STATE            PIC X(2).                 
013234         10  HOLD-TDAC-PROVINCE         PIC X(2).                 
013236         10  HOLD-TDAC-COUNTRY          PIC X(2).                 
013238         10  HOLD-TDAC-ZIP-CODE.                                  
013240             15  HOLD-TDAC-ZIP          PIC 9(5).                 
013242             15  HOLD-TDAC-ZIP-4        PIC 9(4).                 
013244         10  HOLD-TDAC-LONGITUDE        PIC S9(3)V9(6).           
013246         10  HOLD-TDAC-LATITUDE         PIC S9(3)V9(6).           
013248         10  HOLD-TDAC-MAIL-CD          PIC 9(1).                 
013250         10  HOLD-TDAC-TICKLER-FLAG     PIC 9(1).                 
013252         10  HOLD-TDAC-RESIDENT-CD      PIC 9(1).                 
013254         10  HOLD-TDAC-ALIEN-CD         PIC 9(1).                 
013256         10  HOLD-TDAC-SHT-NAME         PIC X(20).                
013258         10  HOLD-TDAC-BAR-CD           PIC 9(3).                 
013260         10  HOLD-TDAC-PHONE-1          PIC 9(10).                
013262         10  HOLD-TDAC-PHONE-2          PIC 9(10).                
013264         10  HOLD-TDAC-TIN-CD           PIC X(1).                 
013266         10  HOLD-TDAC-TIN-CERT-CD      PIC 9(1).                 
013268         10  HOLD-TDAC-TIN-CERT-DT      PIC 9(8).                 
013270         10  HOLD-TDAC-TIN-NBR          PIC 9(9).                 
013272         10  HOLD-TDAC-OFFICER          PIC X(3).                 
013274         10  HOLD-TDAC-EMP-CD           PIC X(1).                 
013276         10  HOLD-TDAC-FREE-MARK        PIC X(24).                
013278         10  HOLD-TDAC-INQ-SECR-CD      PIC 9(1).                 
013280         10  HOLD-TDAC-PRIVACY          PIC 9(1).                 
013282         10  HOLD-TDAC-BK-DEF-CD1       PIC X(1).                 
013284         10  HOLD-TDAC-BK-DEF-CD2       PIC X(1).                 
013286         10  HOLD-TDAC-BK-DEF-CD3       PIC X(1).                 
013288         10  HOLD-TDAC-BK-DEF-CD4       PIC X(1).                 
013290         10  HOLD-TDAC-BK-DEF-CD5       PIC X(1).                 
013292         10  HOLD-TDAC-EMPLOYEE-ID      PIC X(8).                 
013294         10  HOLD-TDAC-EMAIL-ADDR       PIC X(100).               
013296         10 HOLD-TDAC-EMAIL-ADDR-R REDEFINES HOLD-TDAC-EMAIL-ADDR.
013298             15  HOLD-TDAC-EMAIL-ADDR-1-30  PIC X(30).            
013300             15  HOLD-TDAC-EMAIL-ADDR-31-60 PIC X(30).            
013302             15  HOLD-TDAC-EMAIL-ADDR-61-90 PIC X(30).            
013304             15  HOLD-TDAC-EMAIL-ADDR-91-100                      
013306                                           PIC X(10).             
013308         10 HOLD-TDAC-EMAIL-ADDR-RR                               
013310                                   REDEFINES HOLD-TDAC-EMAIL-ADDR.
013312             15  HOLD-TDAC-EMAIL-ADDR-1-50  PIC X(50).            
013314             15  HOLD-TDAC-EMAIL-ADDR-51-100 PIC X(50).           
013316         10  HOLD-TDAC-EMAIL-PSSWRD     PIC X(12).                
013318         10  HOLD-TDAC-GENDER           PIC X(1).                 
013320         10  HOLD-TDAC-NEW-CUST         PIC 9(1).                 
013322         10  HOLD-TDAC-OPEN-DT          PIC 9(8).                 
013324         10  HOLD-TDAC-LUPD-DATE        PIC 9(8).                 
013326         10  HOLD-TDAC-LUPD-TIME        PIC 9(8).                 
013328         10  HOLD-TDAC-LST-CONTACT      PIC 9(8).                 
013330         10  HOLD-TDAC-BIRTH-DT         PIC 9(8).                 
013332         10  HOLD-TDAC-BIRTH-DT-2       PIC 9(8).                 
013334         10  HOLD-TDAC-BIRTH-DT-3       PIC 9(8).                 
013336         10  HOLD-TDAC-DEATH-DT         PIC 9(8).                 
013338         10  HOLD-TDAC-ADD-DT           PIC 9(8).                 
013340         10  HOLD-TDAC-ADD-TM           PIC 9(6).                 
013342         10  HOLD-TDAC-ROTH-DATE        PIC 9(8).                 
013344         10  HOLD-TDAC-CD-BAL           PIC S9(15)V9(2).          
013346         10  HOLD-TDAC-CD-BAL-BYR       PIC S9(15)V9(2).          
013348         10  HOLD-TDAC-CD-PENLTY        PIC S9(15)V9(2).          
013350         10  HOLD-TDAC-CD-WTHLD         PIC S9(15)V9(2).          
013352         10  HOLD-TDAC-CD-INT           PIC S9(15)V9(2).          
013354         10  HOLD-TDAC-CD-OID-INT       PIC S9(15)V9(2).          
013356         10  HOLD-TDAC-IRA-BAL          PIC S9(15)V9(2).          
013358         10  HOLD-TDAC-IRA-BAL-BYR      PIC S9(15)V9(2).          
013360         10  HOLD-TDAC-IRA-PENLTY       PIC S9(15)V9(2).          
013362         10  HOLD-TDAC-IRA-WTHLD        PIC S9(15)V9(2).          
013364         10  HOLD-TDAC-IRA-INT          PIC S9(15)V9(2).          
013366         10  HOLD-TDAC-IRA-CONTR        PIC S9(15)V9(2).          
013368         10  HOLD-TDAC-IRA-CONTR-LY     PIC S9(15)V9(2).          
013370         10  HOLD-TDAC-IRA-DISTR        PIC S9(15)V9(2).          
013372         10  HOLD-TDAC-IRA-DISTR-LY     PIC S9(15)V9(2).          
013374         10  HOLD-TDAC-IRA-ROLLOVER     PIC S9(15)V9(2).          
013376         10  HOLD-TDAC-IRA-TRF-IN       PIC S9(15)V9(2).          
013378         10  HOLD-TDAC-IRA-TRF-OUT      PIC S9(15)V9(2).          
013380         10  HOLD-TDAC-IRA-FAIR-MKT     PIC S9(15)V9(2).          
013382         10  HOLD-TDAC-CIF-REMARK       PIC X.                    
013384         10  HOLD-TDAC-CD-ST-WHLD       PIC S9(15)V9(2).          
013386         10  HOLD-TDAC-IRA-ST-WHLD      PIC S9(15)V9(2).          
013388         10  HOLD-TDAC-CURR-YR-AMT      PIC S9(15)V9(2)           
013390                                            OCCURS 12 TIMES.      
013392         10  HOLD-TDAC-LAST-YR-AMT      PIC S9(15)V9(2)           
013394                                            OCCURS 12 TIMES.      
013396         10  HOLD-TDAC-TIN-CD-2         PIC X(01).                
013398         10  HOLD-TDAC-TIN-CRT-CD-2     PIC 9(01).                
013400         10  HOLD-TDAC-TIN-CRT-DT-2     PIC 9(08).                
013402         10  HOLD-TDAC-TIN-NBR-2        PIC 9(09).                
013404         10  HOLD-TDAC-TIN-CD-3         PIC X(01).                
013406         10  HOLD-TDAC-TIN-CRT-CD-3     PIC 9(01).                
013408         10  HOLD-TDAC-TIN-CRT-DT-3     PIC 9(08).                
013410         10  HOLD-TDAC-TIN-NBR-3        PIC 9(09).                
013412         10  HOLD-TDAC-NAICS-CD         PIC 9(06).                
013414         10  HOLD-TDAC-CIF-PASS-THR     PIC 9(01).                
013416         10  HOLD-TDAC-EMAIL-NTC        PIC 9(01).                
013418         10  HOLD-TDAC-RMD-YR-AMT       PIC S9(15)V9(2).          
013420         10  HOLD-TDAC-ADDR-CHG-DT      PIC 9(08).                
013422         10  HOLD-TDAC-WTHLD-CD         PIC 9(01).                
013424         10  HOLD-TDAC-ST-WHLD-CD       PIC 9(01).                
013426         10  HOLD-TDAC-WTHLD-AMT        PIC S9(12)V9(2).          
013428         10  HOLD-TDAC-ST-WHLD-AMT      PIC S9(12)V9(2).          
013430         10  HOLD-TDAC-FOREIGN-LANG     PIC X(01).                
013432         10  HOLD-TDAC-L-ROLLOVR-DT     PIC 9(08).                
013434         10  HOLD-TDAC-CUSTM-FIELDS     PIC 9(01).                
013436         10  HOLD-TDAC-LLC-NAME         PIC X(40).                
013438         10  HOLD-TDAC-LLC-TIN-CD       PIC X(01).                
013440         10  HOLD-TDAC-LLC-TIN          PIC 9(09).                
013442         10  HOLD-TDAC-FOREIGN-PHN      PIC X(20).                
013444                                                                  
013446     05  HOLD-TDACHK.                                             
013448         10  HOLD-TDACK-BANK            PIC 9(04).                
013450         10  HOLD-TDACK-BRCH            PIC 9(04).                
013452         10  HOLD-TDACK-ADDR-CUST       PIC 9(12).                
013454         10  HOLD-TDACK-CUST            PIC 9(12)                 
013456                                                  OCCURS 10 TIMES.
013458         10  HOLD-TDACK-ACCT            PIC 9(10)                 
013460                                                  OCCURS 10 TIMES.
013462         10  HOLD-TDACK-LUPD-DATE       PIC 9(08).                
013464         10  HOLD-TDACK-LUPD-TIME       PIC 9(08).                
013466         10  HOLD-TDACK-PUB-ID          PIC X(08).                
013468                                                                  
013470     05  HOLD-TDAACCT.                                            
013472         10  HOLD-TDAA-G-KEY.                                     
013474             15  HOLD-TDAA-BANK           PIC 9(4).               
013476             15  HOLD-TDAA-BRCH           PIC 9(4).               
013478             15  HOLD-TDAA-APPL           PIC 9(1).               
013480             15  HOLD-TDAA-CUST           PIC 9(12).              
013482             15  HOLD-TDAA-ACCT           PIC 9(10).              
013484         10  HOLD-TDAA-G-DATA-OPT.                                
013486             15  HOLD-TDAA-STATUS         PIC X(1).               
013488             15  HOLD-TDAA-IRA-TYPE       PIC 9(2).               
013490             15  HOLD-TDAA-ACCT-OPTION    PIC 9(2).               
013492             15  HOLD-TDAA-DT-CONDENSED   PIC 9(8).               
013494             15  HOLD-TDAA-CERT           PIC 9(7).               
013496             15  HOLD-TDAA-SHT-NAME       PIC X(20).              
013498             15  HOLD-TDAA-TITLE          PIC X(40).              
013500             15  HOLD-TDAA-TITLE-PRINT    PIC X(1).               
013502             15  HOLD-TDAA-ADDR-USAGE     PIC X(01).              
013504             15  HOLD-TDAA-ADDR-ALT       PIC X(01).              
013506             15  HOLD-TDAA-ADDR-TEMP      PIC X(01).              
013508             15  HOLD-TDAA-TEMP-BEG-DT    PIC 9(04).              
013510             15  HOLD-TDAA-TEMP-END-DT    PIC 9(04).              
013512             15  HOLD-TDAA-TEMP-EFF-DT    PIC 9(08).              
013514             15  HOLD-TDAA-TEMP-EXP-DT    PIC 9(08).              
013516             15  HOLD-TDAA-END-OF-INT     PIC 9(1).               
013518             15  HOLD-TDAA-END-OF-MAT     PIC 9(1).               
013520             15  HOLD-TDAA-END-OF-STMT    PIC 9(1).               
013522             15  HOLD-TDAA-END-OF-CMPD    PIC 9(1).               
013524             15  HOLD-TDAA-END-OF-FEE     PIC 9(1).               
013526             15  HOLD-TDAA-OFFICER        PIC X(3).               
013528             15  HOLD-TDAA-OFFICER-2      PIC X(3).               
013530             15  HOLD-TDAA-OFFICER-3      PIC X(3).               
013532             15  HOLD-TDAA-FREE-MARK      PIC X(24).              
013534             15  HOLD-TDAA-CLASS-CD       PIC X(1).               
013536             15  HOLD-TDAA-CORR-BK-CD     PIC X(1).               
013538             15  HOLD-TDAA-PUBLIC-FUND    PIC X(1).               
013540             15  HOLD-TDAA-TRUST-CD       PIC X(1).               
013542             15  HOLD-TDAA-RT-CHG-ALLOW   PIC 9(1).               
013544             15  HOLD-TDAA-WTHDRW-ALLOW   PIC 9(1).               
013546             15  HOLD-TDAA-DPOSIT-ALLOW   PIC 9(1).               
013548             15  HOLD-TDAA-POST-MAT       PIC 9(1).               
013550             15  HOLD-TDAA-RT-FLOOR       PIC 9(1).               
013552             15  HOLD-TDAA-REPO-CD        PIC 9(1).               
013554             15  HOLD-TDAA-TOTAL-CD       PIC 999.                
013556             15 HOLD-TDAA-TOTAL-CD-R REDEFINES HOLD-TDAA-TOTAL-CD.
013558                 20  HOLD-TDAA-TOTAL-CD-9  PIC 9(1).              
013560                 20  HOLD-TDAA-TOTAL-CD-99 PIC 9(2).              
013562             15  HOLD-TDAA-REN-TOTAL-CD   PIC 9(3).               
013564             15  HOLD-TDAA-ORG-TOTAL-CD   PIC 9(3).               
013566             15  HOLD-TDAA-INQ-SECR-CD    PIC 9(1).               
013568             15  HOLD-TDAA-MAIL-CD        PIC 9(1).               
013570             15  HOLD-TDAA-WTHD-REQD-CD   PIC 9(1).               
013572             15  HOLD-TDAA-TICKLER-FLAG   PIC 9(1).               
013574             15  HOLD-TDAA-DISP-CD        PIC 9(1).               
013576             15  HOLD-TDAA-CLS-DISP-CD    PIC 9(1).               
013578             15  HOLD-TDAA-DIST-STATUS    PIC 9(1).               
013580             15  HOLD-TDAA-COMM-ACCT      PIC 9(1).               
013582             15  HOLD-TDAA-RENEW-CD       PIC 9(1).               
013584             15  HOLD-TDAA-PLEDGE-CD      PIC X(1).               
013586             15  HOLD-TDAA-NEGOT-CD       PIC X(1).               
013588             15  HOLD-TDAA-BENEF-CD       PIC 9(1).               
013590             15  HOLD-TDAA-COMM-MAT-CD    PIC 9(1).               
013592             15  HOLD-TDAA-NBR-BENEF      PIC 9(1).               
013594             15  HOLD-TDAA-OVERRIDE       PIC 9(1).               
013596             15  HOLD-TDAA-INT-CD         PIC 9(1).               
013598             15  HOLD-TDAA-WTHLD-CD       PIC 9(1).               
013600             15  HOLD-TDAA-WTHLD-AMT      PIC S9(12)V9(2).        
013602             15  HOLD-TDAA-IGL-GRP        PIC 9(2).               
013604             15  HOLD-TDAA-SUM-STMT-CD    PIC 9(1).               
013606             15  HOLD-TDAA-REN-NTC-CD     PIC 9(1).               
013608             15  HOLD-TDAA-PMAT-NTC-CD    PIC 9(1).               
013610             15  HOLD-TDAA-RTCHG-NTC-CD   PIC 9(1).               
013612             15  HOLD-TDAA-INT-NTC-CD     PIC 9(1).               
013614             15  HOLD-TDAA-CHG-NTC        PIC 9(1).               
013616             15  HOLD-TDAA-YIELD-NUM      PIC 9(3).               
013618             15  HOLD-TDAA-YIELD-DENOM    PIC 9(3).               
013620             15  HOLD-TDAA-CMPD-FREQ      PIC 9(1).               
013622             15  HOLD-TDAA-CMPD-NTRVL     PIC 9(4).               
013624             15  HOLD-TDAA-RT-CHG-LIMIT   PIC 9(1).               
013626             15  HOLD-TDAA-VAR-RT-IMMED   PIC 9(1).               
013628             15  HOLD-TDAA-VAR-RT-INT     PIC 9(1).               
013630             15  HOLD-TDAA-VAR-RT-SCHED   PIC 9(1).               
013632             15  HOLD-TDAA-VAR-RT-CUST    PIC 9(1).               
013634             15  HOLD-TDAA-VAR-RT-BAL     PIC 9(1).               
013636             15  HOLD-TDAA-RT-INDX-CD     PIC 9(2).               
013638             15  HOLD-TDAA-R-RT-INDX-CD   PIC XX.                 
013640             15  HOLD-TDAA-RT-MARG-CD     PIC 9(2).               
013642             15  HOLD-TDAA-R-RT-MARG-CD   PIC XX.                 
013644             15  HOLD-TDAA-RT-TIER-CD     PIC 9(2).               
013646             15  HOLD-TDAA-R-RT-TIER-CD   PIC XX.                 
013648             15  HOLD-TDAA-RT-SR-CD       PIC 9(2).               
013650             15  HOLD-TDAA-R-RT-SR-CD     PIC XX.                 
013652             15  HOLD-TDAA-RT-REGN-CD     PIC 9(2).               
013654             15  HOLD-TDAA-RT-CHG-NTRVL   PIC 9(3).               
013656             15  HOLD-TDAA-CAP-RT-CHG     PIC X.                  
013658             15  HOLD-TDAA-R-TIER-RT-CH   PIC X.                  
013660             15  HOLD-TDAA-ALERT-CD       PIC 9(2).               
013662             15  HOLD-TDAA-ALERT-CD-2     PIC 9(2).               
013664             15  HOLD-TDAA-ALERT-CD-3     PIC 9(2).               
013666             15  HOLD-TDAA-CENSUS-TRACT   PIC 9(4)V9(2).          
013668             15  HOLD-TDAA-MK-SEGMENT     PIC X(2).               
013670             15  HOLD-TDAA-BK-DEF-TOT     PIC X(3).               
013672             15  HOLD-TDAA-BK-DEF-CD1     PIC X(1).               
013674             15  HOLD-TDAA-BK-DEF-CD2     PIC X(1).               
013676             15  HOLD-TDAA-BK-DEF-CD3     PIC X(1).               
013678             15  HOLD-TDAA-BK-DEF-CD4     PIC X(1).               
013680             15  HOLD-TDAA-BK-DEF-CD5     PIC X(1).               
013682             15  HOLD-TDAA-OID-METH       PIC 9(1).               
013684             15  HOLD-TDAA-EOY-CD         PIC 9(1).               
013686             15  HOLD-TDAA-B-NOTC-YR1     PIC 9(1).               
013688             15  HOLD-TDAA-B-NOTC-YR2     PIC 9(1).               
013690             15  HOLD-TDAA-B-NOTC-YR3     PIC 9(1).               
013692             15  HOLD-TDAA-NO-COMB-IRS    PIC 9(1).               
013694             15  HOLD-TDAA-PENLTY-CD      PIC 999.                
013696             15  HOLD-TDAA-MONEY-SRC-CD   PIC X(1).               
013698             15  HOLD-TDAA-INTERNET-CD-R  PIC 999.                
013700             15  HOLD-TDAA-INTERNET-CD REDEFINES                  
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 592 lines from 6255 to 6846.

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

