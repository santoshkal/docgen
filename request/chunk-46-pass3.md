# LLM Request Debug File
Generated: 2025-11-13T21:46:21.009150

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 46/55
- **Model**: gpt-4.1
- **Chunk Number**: 46
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~9,473 tokens
- **Total Input**: ~11,431 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 46/55" (ID: detailed-code-explanation)

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


**CHUNK 46 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 46 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 22123 to 22545 (423 lines)\nChunk Tokens (estimated): ~8,093\nActual Input Tokens: 9,499 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 22123-22545 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 46 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 46 of 55.\n\n\n=============================================================================\nCHUNK 46 SOURCE CODE (Lines 22123-22545)\n=============================================================================\n\n```cobol\n044254         TDB-TDAACCT.\n044256     MOVE TDAA-POSTAL-CITY OF TDAACCT TO TDB-TDAA-POSTAL-CITY OF  \n044258         TDB-TDAACCT.\n044260     MOVE TDAA-POSTAL-CNTRY OF TDAACCT TO TDB-TDAA-POSTAL-CNTRY   \n044262         OF TDB-TDAACCT.\n044264     MOVE TDAA-CITIZN-CNTRY OF TDAACCT TO TDB-TDAA-CITIZN-CNTRY   \n044266         OF TDB-TDAACCT.\n044268     MOVE TDAA-CUSTM-FIELDS OF TDAACCT TO TDB-TDAA-CUSTM-FIELDS   \n044270         OF TDB-TDAACCT.\n044272     MOVE TDAA-AVG-STEP-RT OF TDAACCT TO TDB-TDAA-AVG-STEP-RT OF  \n044274         TDB-TDAACCT.\n044276     MOVE TDAA-MONITOR-INQ OF TDAACCT TO TDB-TDAA-MONITOR-INQ OF  \n044278         TDB-TDAACCT.\n044280     MOVE TDAA-IGL-GRP-2 OF TDAACCT TO TDB-TDAA-IGL-GRP-2 OF      \n044282         TDB-TDAACCT.\n044284     MOVE TDAA-AGG-DAYS-QTD OF TDAACCT TO TDB-TDAA-AGG-DAYS-QTD   \n044286         OF TDB-TDAACCT.\n044288     MOVE TDAA-AGG-BAL-QTD OF TDAACCT TO TDB-TDAA-AGG-BAL-QTD OF  \n044290         TDB-TDAACCT.\n044292     MOVE TDAA-IGL-GRP-3 OF TDAACCT TO TDB-TDAA-IGL-GRP-3 OF      \n044294         TDB-TDAACCT.\n044296     MOVE TDAA-ALT-ADDR-EOY OF TDAACCT TO TDB-TDAA-ALT-ADDR-EOY   \n044298         OF TDB-TDAACCT.\n044300     MOVE TDAA-1042S-TAX-ID OF TDAACCT TO TDB-TDAA-1042S-TAX-ID   \n044302         OF TDB-TDAACCT.\n044304     MOVE TDAA-LEC OF TDAACCT TO TDB-TDAA-LEC OF TDB-TDAACCT.\n044306     MOVE TDAA-BAL-AT-CLOSE OF TDAACCT TO TDB-TDAA-BAL-AT-CLOSE   \n044308         OF TDB-TDAACCT.\n044310     MOVE TDAA-AVL-CAP-INT OF TDAACCT TO TDB-TDAA-AVL-CAP-INT OF  \n044312         TDB-TDAACCT.\n044314     MOVE TDAA-FIDM-TR-FUND OF TDAACCT TO TDB-TDAA-FIDM-TR-FUND   \n044316         OF TDB-TDAACCT.\n044318     MOVE TDAA-IRS-FRM-DLVR OF TDAACCT TO TDB-TDAA-IRS-FRM-DLVR   \n044320         OF TDB-TDAACCT.\n044322     MOVE TDAA-PROVINCE OF TDAACCT TO TDB-TDAA-PROVINCE OF        \n044324         TDB-TDAACCT.\n044326     MOVE TDAA-PROMOTION OF TDAACCT TO TDB-TDAA-PROMOTION OF      \n044328         TDB-TDAACCT.\n044330*THE FOLLOWING MOVES FOR SQL ONLY                                 \n044332     IF Z-EDIT-ERROR\n044334         GO TO Z-12-XIT.\n044336 Z-12-SKIP.\n044338 Z-12-XIT.\n044340     EXIT.\n044342*\n044344*****************************************************************\n044346*    PROCEDURE TDD-TDAA-MOVE-TO-HOLD\n044348*****************************************************************\n044350 Z-13-PROCEDURE.\n044352*\n044354     MOVE TDAA-BANK OF TDAACCT TO HOLD-TDAA-BANK OF HOLD-TDAACCT.\n044356     MOVE TDAA-BRCH OF TDAACCT TO HOLD-TDAA-BRCH OF HOLD-TDAACCT.\n044358     MOVE TDAA-APPL OF TDAACCT TO HOLD-TDAA-APPL OF HOLD-TDAACCT.\n044360     MOVE TDAA-CUST OF TDAACCT TO HOLD-TDAA-CUST OF HOLD-TDAACCT.\n044362     MOVE TDAA-ACCT OF TDAACCT TO HOLD-TDAA-ACCT OF HOLD-TDAACCT.\n044364     MOVE TDAA-STATUS OF TDAACCT TO HOLD-TDAA-STATUS OF           \n044366         HOLD-TDAACCT.\n044368     MOVE TDAA-IRA-TYPE OF TDAACCT TO HOLD-TDAA-IRA-TYPE OF       \n044370         HOLD-TDAACCT.\n044372     MOVE TDAA-ACCT-OPTION OF TDAACCT TO HOLD-TDAA-ACCT-OPTION OF \n044374         HOLD-TDAACCT.\n044376     MOVE TDAA-DT-CONDENSED OF TDAACCT TO HOLD-TDAA-DT-CONDENSED  \n044378         OF HOLD-TDAACCT.\n044380     MOVE TDAA-CERT OF TDAACCT TO HOLD-TDAA-CERT OF HOLD-TDAACCT.\n044382     MOVE TDAA-SHT-NAME OF TDAACCT TO HOLD-TDAA-SHT-NAME OF       \n044384         HOLD-TDAACCT.\n044386     MOVE TDAA-TITLE OF TDAACCT TO HOLD-TDAA-TITLE OF             \n044388         HOLD-TDAACCT.\n044390     MOVE TDAA-TITLE-PRINT OF TDAACCT TO HOLD-TDAA-TITLE-PRINT OF \n044392         HOLD-TDAACCT.\n044394     MOVE TDAA-ADDR-USAGE OF TDAACCT TO HOLD-TDAA-ADDR-USAGE OF   \n044396         HOLD-TDAACCT.\n044398     MOVE TDAA-ADDR-ALT OF TDAACCT TO HOLD-TDAA-ADDR-ALT OF       \n044400         HOLD-TDAACCT.\n044402     MOVE TDAA-ADDR-TEMP OF TDAACCT TO HOLD-TDAA-ADDR-TEMP OF     \n044404         HOLD-TDAACCT.\n044406     MOVE TDAA-TEMP-BEG-DT OF TDAACCT TO HOLD-TDAA-TEMP-BEG-DT OF \n044408         HOLD-TDAACCT.\n044410     MOVE TDAA-TEMP-END-DT OF TDAACCT TO HOLD-TDAA-TEMP-END-DT OF \n044412         HOLD-TDAACCT.\n044414     MOVE TDAA-TEMP-EFF-DT OF TDAACCT TO HOLD-TDAA-TEMP-EFF-DT OF \n044416         HOLD-TDAACCT.\n044418     MOVE TDAA-TEMP-EXP-DT OF TDAACCT TO HOLD-TDAA-TEMP-EXP-DT OF \n044420         HOLD-TDAACCT.\n044422     MOVE TDAA-END-OF-INT OF TDAACCT TO HOLD-TDAA-END-OF-INT OF   \n044424         HOLD-TDAACCT.\n044426     MOVE TDAA-END-OF-MAT OF TDAACCT TO HOLD-TDAA-END-OF-MAT OF   \n044428         HOLD-TDAACCT.\n044430     MOVE TDAA-END-OF-STMT OF TDAACCT TO HOLD-TDAA-END-OF-STMT OF \n044432         HOLD-TDAACCT.\n044434     MOVE TDAA-END-OF-CMPD OF TDAACCT TO HOLD-TDAA-END-OF-CMPD OF \n044436         HOLD-TDAACCT.\n044438     MOVE TDAA-END-OF-FEE OF TDAACCT TO HOLD-TDAA-END-OF-FEE OF   \n044440         HOLD-TDAACCT.\n044442     MOVE TDAA-OFFICER OF TDAACCT TO HOLD-TDAA-OFFICER OF         \n044444         HOLD-TDAACCT.\n044446     MOVE TDAA-OFFICER-2 OF TDAACCT TO HOLD-TDAA-OFFICER-2 OF     \n044448         HOLD-TDAACCT.\n044450     MOVE TDAA-OFFICER-3 OF TDAACCT TO HOLD-TDAA-OFFICER-3 OF     \n044452         HOLD-TDAACCT.\n044454     MOVE TDAA-FREE-MARK OF TDAACCT TO HOLD-TDAA-FREE-MARK OF     \n044456         HOLD-TDAACCT.\n044458     MOVE TDAA-CLASS-CD OF TDAACCT TO HOLD-TDAA-CLASS-CD OF       \n044460         HOLD-TDAACCT.\n044462     MOVE TDAA-CORR-BK-CD OF TDAACCT TO HOLD-TDAA-CORR-BK-CD OF   \n044464         HOLD-TDAACCT.\n044466     MOVE TDAA-PUBLIC-FUND OF TDAACCT TO HOLD-TDAA-PUBLIC-FUND OF \n044468         HOLD-TDAACCT.\n044470     MOVE TDAA-TRUST-CD OF TDAACCT TO HOLD-TDAA-TRUST-CD OF       \n044472         HOLD-TDAACCT.\n044474     MOVE TDAA-RT-CHG-ALLOW OF TDAACCT TO HOLD-TDAA-RT-CHG-ALLOW  \n044476         OF HOLD-TDAACCT.\n044478     MOVE TDAA-WTHDRW-ALLOW OF TDAACCT TO HOLD-TDAA-WTHDRW-ALLOW  \n044480         OF HOLD-TDAACCT.\n044482     MOVE TDAA-DPOSIT-ALLOW OF TDAACCT TO HOLD-TDAA-DPOSIT-ALLOW  \n044484         OF HOLD-TDAACCT.\n044486     MOVE TDAA-POST-MAT OF TDAACCT TO HOLD-TDAA-POST-MAT OF       \n044488         HOLD-TDAACCT.\n044490     MOVE TDAA-RT-FLOOR OF TDAACCT TO HOLD-TDAA-RT-FLOOR OF       \n044492         HOLD-TDAACCT.\n044494     MOVE TDAA-REPO-CD OF TDAACCT TO HOLD-TDAA-REPO-CD OF         \n044496         HOLD-TDAACCT.\n044498     MOVE TDAA-TOTAL-CD OF TDAACCT TO HOLD-TDAA-TOTAL-CD OF       \n044500         HOLD-TDAACCT.\n044502     MOVE TDAA-REN-TOTAL-CD OF TDAACCT TO HOLD-TDAA-REN-TOTAL-CD  \n044504         OF HOLD-TDAACCT.\n044506     MOVE TDAA-ORG-TOTAL-CD OF TDAACCT TO HOLD-TDAA-ORG-TOTAL-CD  \n044508         OF HOLD-TDAACCT.\n044510     MOVE TDAA-INQ-SECR-CD OF TDAACCT TO HOLD-TDAA-INQ-SECR-CD OF \n044512         HOLD-TDAACCT.\n044514     MOVE TDAA-MAIL-CD OF TDAACCT TO HOLD-TDAA-MAIL-CD OF         \n044516         HOLD-TDAACCT.\n044518     MOVE TDAA-WTHD-REQD-CD OF TDAACCT TO HOLD-TDAA-WTHD-REQD-CD  \n044520         OF HOLD-TDAACCT.\n044522     MOVE TDAA-TICKLER-FLAG OF TDAACCT TO HOLD-TDAA-TICKLER-FLAG  \n044524         OF HOLD-TDAACCT.\n044526     MOVE TDAA-DISP-CD OF TDAACCT TO HOLD-TDAA-DISP-CD OF         \n044528         HOLD-TDAACCT.\n044530     MOVE TDAA-CLS-DISP-CD OF TDAACCT TO HOLD-TDAA-CLS-DISP-CD OF \n044532         HOLD-TDAACCT.\n044534     MOVE TDAA-DIST-STATUS OF TDAACCT TO HOLD-TDAA-DIST-STATUS OF \n044536         HOLD-TDAACCT.\n044538     MOVE TDAA-COMM-ACCT OF TDAACCT TO HOLD-TDAA-COMM-ACCT OF     \n044540         HOLD-TDAACCT.\n044542     MOVE TDAA-RENEW-CD OF TDAACCT TO HOLD-TDAA-RENEW-CD OF       \n044544         HOLD-TDAACCT.\n044546     MOVE TDAA-PLEDGE-CD OF TDAACCT TO HOLD-TDAA-PLEDGE-CD OF     \n044548         HOLD-TDAACCT.\n044550     MOVE TDAA-NEGOT-CD OF TDAACCT TO HOLD-TDAA-NEGOT-CD OF       \n044552         HOLD-TDAACCT.\n044554     MOVE TDAA-BENEF-CD OF TDAACCT TO HOLD-TDAA-BENEF-CD OF       \n044556         HOLD-TDAACCT.\n044558     MOVE TDAA-COMM-MAT-CD OF TDAACCT TO HOLD-TDAA-COMM-MAT-CD OF \n044560         HOLD-TDAACCT.\n044562     MOVE TDAA-NBR-BENEF OF TDAACCT TO HOLD-TDAA-NBR-BENEF OF     \n044564         HOLD-TDAACCT.\n044566     MOVE TDAA-OVERRIDE OF TDAACCT TO HOLD-TDAA-OVERRIDE OF       \n044568         HOLD-TDAACCT.\n044570     MOVE TDAA-INT-CD OF TDAACCT TO HOLD-TDAA-INT-CD OF           \n044572         HOLD-TDAACCT.\n044574     MOVE TDAA-WTHLD-CD OF TDAACCT TO HOLD-TDAA-WTHLD-CD OF       \n044576         HOLD-TDAACCT.\n044578     MOVE TDAA-WTHLD-AMT OF TDAACCT TO HOLD-TDAA-WTHLD-AMT OF     \n044580         HOLD-TDAACCT.\n044582     MOVE TDAA-IGL-GRP OF TDAACCT TO HOLD-TDAA-IGL-GRP OF         \n044584         HOLD-TDAACCT.\n044586     MOVE TDAA-SUM-STMT-CD OF TDAACCT TO HOLD-TDAA-SUM-STMT-CD OF \n044588         HOLD-TDAACCT.\n044590     MOVE TDAA-REN-NTC-CD OF TDAACCT TO HOLD-TDAA-REN-NTC-CD OF   \n044592         HOLD-TDAACCT.\n044594     MOVE TDAA-PMAT-NTC-CD OF TDAACCT TO HOLD-TDAA-PMAT-NTC-CD OF \n044596         HOLD-TDAACCT.\n044598     MOVE TDAA-RTCHG-NTC-CD OF TDAACCT TO HOLD-TDAA-RTCHG-NTC-CD  \n044600         OF HOLD-TDAACCT.\n044602     MOVE TDAA-INT-NTC-CD OF TDAACCT TO HOLD-TDAA-INT-NTC-CD OF   \n044604         HOLD-TDAACCT.\n044606     MOVE TDAA-CHG-NTC OF TDAACCT TO HOLD-TDAA-CHG-NTC OF         \n044608         HOLD-TDAACCT.\n044610     MOVE TDAA-YIELD-NUM OF TDAACCT TO HOLD-TDAA-YIELD-NUM OF     \n044612         HOLD-TDAACCT.\n044614     MOVE TDAA-YIELD-DENOM OF TDAACCT TO HOLD-TDAA-YIELD-DENOM OF \n044616         HOLD-TDAACCT.\n044618     MOVE TDAA-CMPD-FREQ OF TDAACCT TO HOLD-TDAA-CMPD-FREQ OF     \n044620         HOLD-TDAACCT.\n044622     MOVE TDAA-CMPD-NTRVL OF TDAACCT TO HOLD-TDAA-CMPD-NTRVL OF   \n044624         HOLD-TDAACCT.\n044626     MOVE TDAA-RT-CHG-LIMIT OF TDAACCT TO HOLD-TDAA-RT-CHG-LIMIT  \n044628         OF HOLD-TDAACCT.\n044630     MOVE TDAA-VAR-RT-IMMED OF TDAACCT TO HOLD-TDAA-VAR-RT-IMMED  \n044632         OF HOLD-TDAACCT.\n044634     MOVE TDAA-VAR-RT-INT OF TDAACCT TO HOLD-TDAA-VAR-RT-INT OF   \n044636         HOLD-TDAACCT.\n044638     MOVE TDAA-VAR-RT-SCHED OF TDAACCT TO HOLD-TDAA-VAR-RT-SCHED  \n044640         OF HOLD-TDAACCT.\n044642     MOVE TDAA-VAR-RT-CUST OF TDAACCT TO HOLD-TDAA-VAR-RT-CUST OF \n044644         HOLD-TDAACCT.\n044646     MOVE TDAA-VAR-RT-BAL OF TDAACCT TO HOLD-TDAA-VAR-RT-BAL OF   \n044648         HOLD-TDAACCT.\n044650     MOVE TDAA-RT-INDX-CD OF TDAACCT TO HOLD-TDAA-RT-INDX-CD OF   \n044652         HOLD-TDAACCT.\n044654     MOVE TDAA-R-RT-INDX-CD OF TDAACCT TO HOLD-TDAA-R-RT-INDX-CD  \n044656         OF HOLD-TDAACCT.\n044658     MOVE TDAA-RT-MARG-CD OF TDAACCT TO HOLD-TDAA-RT-MARG-CD OF   \n044660         HOLD-TDAACCT.\n044662     MOVE TDAA-R-RT-MARG-CD OF TDAACCT TO HOLD-TDAA-R-RT-MARG-CD  \n044664         OF HOLD-TDAACCT.\n044666     MOVE TDAA-RT-TIER-CD OF TDAACCT TO HOLD-TDAA-RT-TIER-CD OF   \n044668         HOLD-TDAACCT.\n044670     MOVE TDAA-R-RT-TIER-CD OF TDAACCT TO HOLD-TDAA-R-RT-TIER-CD  \n044672         OF HOLD-TDAACCT.\n044674     MOVE TDAA-RT-SR-CD OF TDAACCT TO HOLD-TDAA-RT-SR-CD OF       \n044676         HOLD-TDAACCT.\n044678     MOVE TDAA-R-RT-SR-CD OF TDAACCT TO HOLD-TDAA-R-RT-SR-CD OF   \n044680         HOLD-TDAACCT.\n044682     MOVE TDAA-RT-REGN-CD OF TDAACCT TO HOLD-TDAA-RT-REGN-CD OF   \n044684         HOLD-TDAACCT.\n044686     MOVE TDAA-RT-CHG-NTRVL OF TDAACCT TO HOLD-TDAA-RT-CHG-NTRVL  \n044688         OF HOLD-TDAACCT.\n044690     MOVE TDAA-CAP-RT-CHG OF TDAACCT TO HOLD-TDAA-CAP-RT-CHG OF   \n044692         HOLD-TDAACCT.\n044694     MOVE TDAA-R-TIER-RT-CH OF TDAACCT TO HOLD-TDAA-R-TIER-RT-CH  \n044696         OF HOLD-TDAACCT.\n044698     MOVE TDAA-ALERT-CD OF TDAACCT TO HOLD-TDAA-ALERT-CD OF       \n044700         HOLD-TDAACCT.\n044702     MOVE TDAA-ALERT-CD-2 OF TDAACCT TO HOLD-TDAA-ALERT-CD-2 OF   \n044704         HOLD-TDAACCT.\n044706     MOVE TDAA-ALERT-CD-3 OF TDAACCT TO HOLD-TDAA-ALERT-CD-3 OF   \n044708         HOLD-TDAACCT.\n044710     MOVE TDAA-CENSUS-TRACT OF TDAACCT TO HOLD-TDAA-CENSUS-TRACT  \n044712         OF HOLD-TDAACCT.\n044714     MOVE TDAA-MK-SEGMENT OF TDAACCT TO HOLD-TDAA-MK-SEGMENT OF   \n044716         HOLD-TDAACCT.\n044718     MOVE TDAA-BK-DEF-TOT OF TDAACCT TO HOLD-TDAA-BK-DEF-TOT OF   \n044720         HOLD-TDAACCT.\n044722     MOVE TDAA-BK-DEF-CD1 OF TDAACCT TO HOLD-TDAA-BK-DEF-CD1 OF   \n044724         HOLD-TDAACCT.\n044726     MOVE TDAA-BK-DEF-CD2 OF TDAACCT TO HOLD-TDAA-BK-DEF-CD2 OF   \n044728         HOLD-TDAACCT.\n044730     MOVE TDAA-BK-DEF-CD3 OF TDAACCT TO HOLD-TDAA-BK-DEF-CD3 OF   \n044732         HOLD-TDAACCT.\n044734     MOVE TDAA-BK-DEF-CD4 OF TDAACCT TO HOLD-TDAA-BK-DEF-CD4 OF   \n044736         HOLD-TDAACCT.\n044738     MOVE TDAA-BK-DEF-CD5 OF TDAACCT TO HOLD-TDAA-BK-DEF-CD5 OF   \n044740         HOLD-TDAACCT.\n044742     MOVE TDAA-OID-METH OF TDAACCT TO HOLD-TDAA-OID-METH OF       \n044744         HOLD-TDAACCT.\n044746     MOVE TDAA-EOY-CD OF TDAACCT TO HOLD-TDAA-EOY-CD OF           \n044748         HOLD-TDAACCT.\n044750     MOVE TDAA-B-NOTC-YR1 OF TDAACCT TO HOLD-TDAA-B-NOTC-YR1 OF   \n044752         HOLD-TDAACCT.\n044754     MOVE TDAA-B-NOTC-YR2 OF TDAACCT TO HOLD-TDAA-B-NOTC-YR2 OF   \n044756         HOLD-TDAACCT.\n044758     MOVE TDAA-B-NOTC-YR3 OF TDAACCT TO HOLD-TDAA-B-NOTC-YR3 OF   \n044760         HOLD-TDAACCT.\n044762     MOVE TDAA-NO-COMB-IRS OF TDAACCT TO HOLD-TDAA-NO-COMB-IRS OF \n044764         HOLD-TDAACCT.\n044766     MOVE TDAA-PENLTY-CD OF TDAACCT TO HOLD-TDAA-PENLTY-CD OF     \n044768         HOLD-TDAACCT.\n044770     MOVE TDAA-MONEY-SRC-CD OF TDAACCT TO HOLD-TDAA-MONEY-SRC-CD  \n044772         OF HOLD-TDAACCT.\n044774     MOVE TDAA-INTERNET-BPY OF TDAACCT TO HOLD-TDAA-INTERNET-BPY  \n044776         OF HOLD-TDAACCT.\n044778     MOVE TDAA-INTERNET-TFR OF TDAACCT TO HOLD-TDAA-INTERNET-TFR  \n044780         OF HOLD-TDAACCT.\n044782     MOVE TDAA-INTERNET-INQ OF TDAACCT TO HOLD-TDAA-INTERNET-INQ  \n044784         OF HOLD-TDAACCT.\n044786     MOVE TDAA-IRA-BACKED OF TDAACCT TO HOLD-TDAA-IRA-BACKED OF   \n044788         HOLD-TDAACCT.\n044790     MOVE TDAA-SAV-DEPOSIT OF TDAACCT TO HOLD-TDAA-SAV-DEPOSIT OF \n044792         HOLD-TDAACCT.\n044794     MOVE TDAA-MAT-TYPE OF TDAACCT TO HOLD-TDAA-MAT-TYPE OF       \n044796         HOLD-TDAACCT.\n044798     MOVE TDAA-MAT-TERM OF TDAACCT TO HOLD-TDAA-MAT-TERM OF       \n044800         HOLD-TDAACCT.\n044802     MOVE TDAA-ORG-MAT-TYPE OF TDAACCT TO HOLD-TDAA-ORG-MAT-TYPE  \n044804         OF HOLD-TDAACCT.\n044806     MOVE TDAA-ORG-MAT-TERM OF TDAACCT TO HOLD-TDAA-ORG-MAT-TERM  \n044808         OF HOLD-TDAACCT.\n044810     MOVE TDAA-ODD-PAYMENT OF TDAACCT TO HOLD-TDAA-ODD-PAYMENT OF \n044812         HOLD-TDAACCT.\n044814     MOVE TDAA-PAY-FREQ OF TDAACCT TO HOLD-TDAA-PAY-FREQ OF       \n044816         HOLD-TDAACCT.\n044818     MOVE TDAA-PAY-NTRVL OF TDAACCT TO HOLD-TDAA-PAY-NTRVL OF     \n044820         HOLD-TDAACCT.\n044822     MOVE TDAA-FEE-FREQ OF TDAACCT TO HOLD-TDAA-FEE-FREQ OF       \n044824         HOLD-TDAACCT.\n044826     MOVE TDAA-FEE-NTRVL OF TDAACCT TO HOLD-TDAA-FEE-NTRVL OF     \n044828         HOLD-TDAACCT.\n044830     MOVE TDAA-STMT-FREQ OF TDAACCT TO HOLD-TDAA-STMT-FREQ OF     \n044832         HOLD-TDAACCT.\n044834     MOVE TDAA-STMT-NTRVL OF TDAACCT TO HOLD-TDAA-STMT-NTRVL OF   \n044836         HOLD-TDAACCT.\n044838     MOVE TDAA-EMPLOYEE-ID OF TDAACCT TO HOLD-TDAA-EMPLOYEE-ID OF \n044840         HOLD-TDAACCT.\n044842     MOVE TDAA-EFT-CARD OF TDAACCT TO HOLD-TDAA-EFT-CARD OF       \n044844         HOLD-TDAACCT.\n044846     MOVE TDAA-PEN-WAV-RESN OF TDAACCT TO HOLD-TDAA-PEN-WAV-RESN  \n044848         OF HOLD-TDAACCT.\n044850     MOVE TDAA-CLOSED-RESN OF TDAACCT TO HOLD-TDAA-CLOSED-RESN OF \n044852         HOLD-TDAACCT.\n044854     MOVE TDAA-SPECIAL-STMT OF TDAACCT TO HOLD-TDAA-SPECIAL-STMT  \n044856         OF HOLD-TDAACCT.\n044858     MOVE TDAA-CLS-THIS-MTH OF TDAACCT TO HOLD-TDAA-CLS-THIS-MTH  \n044860         OF HOLD-TDAACCT.\n044862     MOVE TDAA-RC-MAT-ONLY OF TDAACCT TO HOLD-TDAA-RC-MAT-ONLY OF \n044864         HOLD-TDAACCT.\n044866     MOVE TDAA-GRACE-DAYS OF TDAACCT TO HOLD-TDAA-GRACE-DAYS OF   \n044868         HOLD-TDAACCT.\n044870     MOVE TDAA-CLS-ON-MAT OF TDAACCT TO HOLD-TDAA-CLS-ON-MAT OF   \n044872         HOLD-TDAACCT.\n044874     MOVE TDAA-DDA-ACCT-1 OF TDAACCT TO HOLD-TDAA-DDA-ACCT-1 OF   \n044876         HOLD-TDAACCT.\n044878     MOVE TDAA-DDA-ACCT-1-S OF TDAACCT TO HOLD-TDAA-DDA-ACCT-1-S  \n044880         OF HOLD-TDAACCT.\n044882     MOVE TDAA-DDA-ACCT-2 OF TDAACCT TO HOLD-TDAA-DDA-ACCT-2 OF   \n044884         HOLD-TDAACCT.\n044886     MOVE TDAA-DDA-ACCT-2-S OF TDAACCT TO HOLD-TDAA-DDA-ACCT-2-S  \n044888         OF HOLD-TDAACCT.\n044890     MOVE TDAA-DDA-ACCT-3 OF TDAACCT TO HOLD-TDAA-DDA-ACCT-3 OF   \n044892         HOLD-TDAACCT.\n044894     MOVE TDAA-DDA-ACCT-3-S OF TDAACCT TO HOLD-TDAA-DDA-ACCT-3-S  \n044896         OF HOLD-TDAACCT.\n044898     MOVE TDAA-INT-ACCT OF TDAACCT TO HOLD-TDAA-INT-ACCT OF       \n044900         HOLD-TDAACCT.\n044902     MOVE TDAA-INT-ACCT-S OF TDAACCT TO HOLD-TDAA-INT-ACCT-S OF   \n044904         HOLD-TDAACCT.\n044906     MOVE TDAA-CS-ACCT OF TDAACCT TO HOLD-TDAA-CS-ACCT OF         \n044908         HOLD-TDAACCT.\n044910     MOVE TDAA-CS-ACCT-S OF TDAACCT TO HOLD-TDAA-CS-ACCT-S OF     \n044912         HOLD-TDAACCT.\n044914     MOVE TDAA-CC-ACCT OF TDAACCT TO HOLD-TDAA-CC-ACCT OF         \n044916         HOLD-TDAACCT.\n044918     MOVE TDAA-LNS-BORROWER OF TDAACCT TO HOLD-TDAA-LNS-BORROWER  \n044920         OF HOLD-TDAACCT.\n044922     MOVE TDAA-LNS-NOTE OF TDAACCT TO HOLD-TDAA-LNS-NOTE OF       \n044924         HOLD-TDAACCT.\n044926     MOVE TDAA-CNV-OLD-ACCT OF TDAACCT TO HOLD-TDAA-CNV-OLD-ACCT  \n044928         OF HOLD-TDAACCT.\n044930     MOVE TDAA-CLS-ACCT OF TDAACCT TO HOLD-TDAA-CLS-ACCT OF       \n044932         HOLD-TDAACCT.\n044934     MOVE TDAA-CLS-ACCT-S OF TDAACCT TO HOLD-TDAA-CLS-ACCT-S OF   \n044936         HOLD-TDAACCT.\n044938     MOVE TDAA-DAYS-IN-PER OF TDAACCT TO HOLD-TDAA-DAYS-IN-PER OF \n044940         HOLD-TDAACCT.\n044942     MOVE TDAA-RR-CYC-NBR OF TDAACCT TO HOLD-TDAA-RR-CYC-NBR OF   \n044944         HOLD-TDAACCT.\n044946     MOVE TDAA-CR-CNT-STD OF TDAACCT TO HOLD-TDAA-CR-CNT-STD OF   \n044948         HOLD-TDAACCT.\n044950     MOVE TDAA-CR-AMT-STD OF TDAACCT TO HOLD-TDAA-CR-AMT-STD OF   \n044952         HOLD-TDAACCT.\n044954     MOVE TDAA-DB-CNT-STD OF TDAACCT TO HOLD-TDAA-DB-CNT-STD OF   \n044956         HOLD-TDAACCT.\n044958     MOVE TDAA-DB-AMT-STD OF TDAACCT TO HOLD-TDAA-DB-AMT-STD OF   \n044960         HOLD-TDAACCT.\n044962     MOVE TDAA-CR-CNT-YTD OF TDAACCT TO HOLD-TDAA-CR-CNT-YTD OF   \n044964         HOLD-TDAACCT.\n044966     MOVE TDAA-CR-AMT-YTD OF TDAACCT TO HOLD-TDAA-CR-AMT-YTD OF   \n044968         HOLD-TDAACCT.\n044970     MOVE TDAA-DB-CNT-YTD OF TDAACCT TO HOLD-TDAA-DB-CNT-YTD OF   \n044972         HOLD-TDAACCT.\n044974     MOVE TDAA-DB-AMT-YTD OF TDAACCT TO HOLD-TDAA-DB-AMT-YTD OF   \n044976         HOLD-TDAACCT.\n044978     MOVE TDAA-DAYS-IN-TERM OF TDAACCT TO HOLD-TDAA-DAYS-IN-TERM  \n044980         OF HOLD-TDAACCT.\n044982     MOVE TDAA-BEG-INT-BAL OF TDAACCT TO HOLD-TDAA-BEG-INT-BAL OF \n044984         HOLD-TDAACCT.\n044986     MOVE TDAA-PURCH-AMT OF TDAACCT TO HOLD-TDAA-PURCH-AMT OF     \n044988         HOLD-TDAACCT.\n044990     MOVE TDAA-CURR-BAL OF TDAACCT TO HOLD-TDAA-CURR-BAL OF       \n044992         HOLD-TDAACCT.\n044994     MOVE TDAA-AVAIL-BAL OF TDAACCT TO HOLD-TDAA-AVAIL-BAL OF     \n044996         HOLD-TDAACCT.\n044998     MOVE TDAA-BAL-BEG-MAT OF TDAACCT TO HOLD-TDAA-BAL-BEG-MAT OF \n045000         HOLD-TDAACCT.\n045002     MOVE TDAA-CLOSE-AMT OF TDAACCT TO HOLD-TDAA-CLOSE-AMT OF     \n045004         HOLD-TDAACCT.\n045006     MOVE TDAA-MONEY-AMT OF TDAACCT TO HOLD-TDAA-MONEY-AMT OF     \n045008         HOLD-TDAACCT.\n045010     MOVE TDAA-BAL-BEG-STMT OF TDAACCT TO HOLD-TDAA-BAL-BEG-STMT  \n045012         OF HOLD-TDAACCT.\n045014     MOVE TDAA-ACCR-INT OF TDAACCT TO HOLD-TDAA-ACCR-INT OF       \n045016         HOLD-TDAACCT.\n045018     MOVE TDAA-ANTIC-INT OF TDAACCT TO HOLD-TDAA-ANTIC-INT OF     \n045020         HOLD-TDAACCT.\n045022     MOVE TDAA-INT-TO-POST OF TDAACCT TO HOLD-TDAA-INT-TO-POST OF \n045024         HOLD-TDAACCT.\n045026     MOVE TDAA-1099-YTD OF TDAACCT TO HOLD-TDAA-1099-YTD OF       \n045028         HOLD-TDAACCT.\n045030     MOVE TDAA-1099-LST-YR OF TDAACCT TO HOLD-TDAA-1099-LST-YR OF \n045032         HOLD-TDAACCT.\n045034     MOVE TDAA-CURR-PENLTY OF TDAACCT TO HOLD-TDAA-CURR-PENLTY OF \n045036         HOLD-TDAACCT.\n045038     MOVE TDAA-PENLTY-STD OF TDAACCT TO HOLD-TDAA-PENLTY-STD OF   \n045040         HOLD-TDAACCT.\n045042     MOVE TDAA-PENLTY-YTD OF TDAACCT TO HOLD-TDAA-PENLTY-YTD OF   \n045044         HOLD-TDAACCT.\n045046     MOVE TDAA-LST-PENLTY OF TDAACCT TO HOLD-TDAA-LST-PENLTY OF   \n045048         HOLD-TDAACCT.\n045050     MOVE TDAA-CURR-INT-ADJ OF TDAACCT TO HOLD-TDAA-CURR-INT-ADJ  \n045052         OF HOLD-TDAACCT.\n045054     MOVE TDAA-TOTAMT-HOLDS OF TDAACCT TO HOLD-TDAA-TOTAMT-HOLDS  \n045056         OF HOLD-TDAACCT.\n045058     MOVE TDAA-NXT-INT-ADJ OF TDAACCT TO HOLD-TDAA-NXT-INT-ADJ OF \n045060         HOLD-TDAACCT.\n045062     MOVE TDAA-FEE-AMT OF TDAACCT TO HOLD-TDAA-FEE-AMT OF         \n045064         HOLD-TDAACCT.\n045066     MOVE TDAA-OID-RPT-INT OF TDAACCT TO HOLD-TDAA-OID-RPT-INT OF \n045068         HOLD-TDAACCT.\n045070     MOVE TDAA-FAIR-MRKT OF TDAACCT TO HOLD-TDAA-FAIR-MRKT OF     \n045072         HOLD-TDAACCT.\n045074     MOVE TDAA-CUR-WHLD-AMT OF TDAACCT TO HOLD-TDAA-CUR-WHLD-AMT  \n045076         OF HOLD-TDAACCT.\n045078     MOVE TDAA-LST-WHLD-AMT OF TDAACCT TO HOLD-TDAA-LST-WHLD-AMT  \n045080         OF HOLD-TDAACCT.\n045082     MOVE TDAA-WTHLD-STD OF TDAACCT TO HOLD-TDAA-WTHLD-STD OF     \n045084         HOLD-TDAACCT.\n045086     MOVE TDAA-WTHLD-YTD OF TDAACCT TO HOLD-TDAA-WTHLD-YTD OF     \n045088         HOLD-TDAACCT.\n045090     MOVE TDAA-LST-INT-PMT OF TDAACCT TO HOLD-TDAA-LST-INT-PMT OF \n045092         HOLD-TDAACCT.\n045094     MOVE TDAA-BAL-BEG-YR OF TDAACCT TO HOLD-TDAA-BAL-BEG-YR OF   \n045096         HOLD-TDAACCT.\n045098     MOVE TDAA-BAL-AT-CONV OF TDAACCT TO HOLD-TDAA-BAL-AT-CONV OF \n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 423 lines from 22123 to 22545.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 46,
  "total_chunks": 55,
  "start_line": 22123,
  "end_line": 22545,
  "line_count": 423
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
- Source code length: 28538 characters

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
CHUNK 46 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 22123 to 22545 (423 lines)
Chunk Tokens (estimated): ~8,093
Actual Input Tokens: 9,499 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 22123-22545 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 46 of 55 chunks
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
      The source code below is only CHUNK 46 of 55.


=============================================================================
CHUNK 46 SOURCE CODE (Lines 22123-22545)
=============================================================================

```cobol
044254         TDB-TDAACCT.
044256     MOVE TDAA-POSTAL-CITY OF TDAACCT TO TDB-TDAA-POSTAL-CITY OF  
044258         TDB-TDAACCT.
044260     MOVE TDAA-POSTAL-CNTRY OF TDAACCT TO TDB-TDAA-POSTAL-CNTRY   
044262         OF TDB-TDAACCT.
044264     MOVE TDAA-CITIZN-CNTRY OF TDAACCT TO TDB-TDAA-CITIZN-CNTRY   
044266         OF TDB-TDAACCT.
044268     MOVE TDAA-CUSTM-FIELDS OF TDAACCT TO TDB-TDAA-CUSTM-FIELDS   
044270         OF TDB-TDAACCT.
044272     MOVE TDAA-AVG-STEP-RT OF TDAACCT TO TDB-TDAA-AVG-STEP-RT OF  
044274         TDB-TDAACCT.
044276     MOVE TDAA-MONITOR-INQ OF TDAACCT TO TDB-TDAA-MONITOR-INQ OF  
044278         TDB-TDAACCT.
044280     MOVE TDAA-IGL-GRP-2 OF TDAACCT TO TDB-TDAA-IGL-GRP-2 OF      
044282         TDB-TDAACCT.
044284     MOVE TDAA-AGG-DAYS-QTD OF TDAACCT TO TDB-TDAA-AGG-DAYS-QTD   
044286         OF TDB-TDAACCT.
044288     MOVE TDAA-AGG-BAL-QTD OF TDAACCT TO TDB-TDAA-AGG-BAL-QTD OF  
044290         TDB-TDAACCT.
044292     MOVE TDAA-IGL-GRP-3 OF TDAACCT TO TDB-TDAA-IGL-GRP-3 OF      
044294         TDB-TDAACCT.
044296     MOVE TDAA-ALT-ADDR-EOY OF TDAACCT TO TDB-TDAA-ALT-ADDR-EOY   
044298         OF TDB-TDAACCT.
044300     MOVE TDAA-1042S-TAX-ID OF TDAACCT TO TDB-TDAA-1042S-TAX-ID   
044302         OF TDB-TDAACCT.
044304     MOVE TDAA-LEC OF TDAACCT TO TDB-TDAA-LEC OF TDB-TDAACCT.
044306     MOVE TDAA-BAL-AT-CLOSE OF TDAACCT TO TDB-TDAA-BAL-AT-CLOSE   
044308         OF TDB-TDAACCT.
044310     MOVE TDAA-AVL-CAP-INT OF TDAACCT TO TDB-TDAA-AVL-CAP-INT OF  
044312         TDB-TDAACCT.
044314     MOVE TDAA-FIDM-TR-FUND OF TDAACCT TO TDB-TDAA-FIDM-TR-FUND   
044316         OF TDB-TDAACCT.
044318     MOVE TDAA-IRS-FRM-DLVR OF TDAACCT TO TDB-TDAA-IRS-FRM-DLVR   
044320         OF TDB-TDAACCT.
044322     MOVE TDAA-PROVINCE OF TDAACCT TO TDB-TDAA-PROVINCE OF        
044324         TDB-TDAACCT.
044326     MOVE TDAA-PROMOTION OF TDAACCT TO TDB-TDAA-PROMOTION OF      
044328         TDB-TDAACCT.
044330*THE FOLLOWING MOVES FOR SQL ONLY                                 
044332     IF Z-EDIT-ERROR
044334         GO TO Z-12-XIT.
044336 Z-12-SKIP.
044338 Z-12-XIT.
044340     EXIT.
044342*
044344*****************************************************************
044346*    PROCEDURE TDD-TDAA-MOVE-TO-HOLD
044348*****************************************************************
044350 Z-13-PROCEDURE.
044352*
044354     MOVE TDAA-BANK OF TDAACCT TO HOLD-TDAA-BANK OF HOLD-TDAACCT.
044356     MOVE TDAA-BRCH OF TDAACCT TO HOLD-TDAA-BRCH OF HOLD-TDAACCT.
044358     MOVE TDAA-APPL OF TDAACCT TO HOLD-TDAA-APPL OF HOLD-TDAACCT.
044360     MOVE TDAA-CUST OF TDAACCT TO HOLD-TDAA-CUST OF HOLD-TDAACCT.
044362     MOVE TDAA-ACCT OF TDAACCT TO HOLD-TDAA-ACCT OF HOLD-TDAACCT.
044364     MOVE TDAA-STATUS OF TDAACCT TO HOLD-TDAA-STATUS OF           
044366         HOLD-TDAACCT.
044368     MOVE TDAA-IRA-TYPE OF TDAACCT TO HOLD-TDAA-IRA-TYPE OF       
044370         HOLD-TDAACCT.
044372     MOVE TDAA-ACCT-OPTION OF TDAACCT TO HOLD-TDAA-ACCT-OPTION OF 
044374         HOLD-TDAACCT.
044376     MOVE TDAA-DT-CONDENSED OF TDAACCT TO HOLD-TDAA-DT-CONDENSED  
044378         OF HOLD-TDAACCT.
044380     MOVE TDAA-CERT OF TDAACCT TO HOLD-TDAA-CERT OF HOLD-TDAACCT.
044382     MOVE TDAA-SHT-NAME OF TDAACCT TO HOLD-TDAA-SHT-NAME OF       
044384         HOLD-TDAACCT.
044386     MOVE TDAA-TITLE OF TDAACCT TO HOLD-TDAA-TITLE OF             
044388         HOLD-TDAACCT.
044390     MOVE TDAA-TITLE-PRINT OF TDAACCT TO HOLD-TDAA-TITLE-PRINT OF 
044392         HOLD-TDAACCT.
044394     MOVE TDAA-ADDR-USAGE OF TDAACCT TO HOLD-TDAA-ADDR-USAGE OF   
044396         HOLD-TDAACCT.
044398     MOVE TDAA-ADDR-ALT OF TDAACCT TO HOLD-TDAA-ADDR-ALT OF       
044400         HOLD-TDAACCT.
044402     MOVE TDAA-ADDR-TEMP OF TDAACCT TO HOLD-TDAA-ADDR-TEMP OF     
044404         HOLD-TDAACCT.
044406     MOVE TDAA-TEMP-BEG-DT OF TDAACCT TO HOLD-TDAA-TEMP-BEG-DT OF 
044408         HOLD-TDAACCT.
044410     MOVE TDAA-TEMP-END-DT OF TDAACCT TO HOLD-TDAA-TEMP-END-DT OF 
044412         HOLD-TDAACCT.
044414     MOVE TDAA-TEMP-EFF-DT OF TDAACCT TO HOLD-TDAA-TEMP-EFF-DT OF 
044416         HOLD-TDAACCT.
044418     MOVE TDAA-TEMP-EXP-DT OF TDAACCT TO HOLD-TDAA-TEMP-EXP-DT OF 
044420         HOLD-TDAACCT.
044422     MOVE TDAA-END-OF-INT OF TDAACCT TO HOLD-TDAA-END-OF-INT OF   
044424         HOLD-TDAACCT.
044426     MOVE TDAA-END-OF-MAT OF TDAACCT TO HOLD-TDAA-END-OF-MAT OF   
044428         HOLD-TDAACCT.
044430     MOVE TDAA-END-OF-STMT OF TDAACCT TO HOLD-TDAA-END-OF-STMT OF 
044432         HOLD-TDAACCT.
044434     MOVE TDAA-END-OF-CMPD OF TDAACCT TO HOLD-TDAA-END-OF-CMPD OF 
044436         HOLD-TDAACCT.
044438     MOVE TDAA-END-OF-FEE OF TDAACCT TO HOLD-TDAA-END-OF-FEE OF   
044440         HOLD-TDAACCT.
044442     MOVE TDAA-OFFICER OF TDAACCT TO HOLD-TDAA-OFFICER OF         
044444         HOLD-TDAACCT.
044446     MOVE TDAA-OFFICER-2 OF TDAACCT TO HOLD-TDAA-OFFICER-2 OF     
044448         HOLD-TDAACCT.
044450     MOVE TDAA-OFFICER-3 OF TDAACCT TO HOLD-TDAA-OFFICER-3 OF     
044452         HOLD-TDAACCT.
044454     MOVE TDAA-FREE-MARK OF TDAACCT TO HOLD-TDAA-FREE-MARK OF     
044456         HOLD-TDAACCT.
044458     MOVE TDAA-CLASS-CD OF TDAACCT TO HOLD-TDAA-CLASS-CD OF       
044460         HOLD-TDAACCT.
044462     MOVE TDAA-CORR-BK-CD OF TDAACCT TO HOLD-TDAA-CORR-BK-CD OF   
044464         HOLD-TDAACCT.
044466     MOVE TDAA-PUBLIC-FUND OF TDAACCT TO HOLD-TDAA-PUBLIC-FUND OF 
044468         HOLD-TDAACCT.
044470     MOVE TDAA-TRUST-CD OF TDAACCT TO HOLD-TDAA-TRUST-CD OF       
044472         HOLD-TDAACCT.
044474     MOVE TDAA-RT-CHG-ALLOW OF TDAACCT TO HOLD-TDAA-RT-CHG-ALLOW  
044476         OF HOLD-TDAACCT.
044478     MOVE TDAA-WTHDRW-ALLOW OF TDAACCT TO HOLD-TDAA-WTHDRW-ALLOW  
044480         OF HOLD-TDAACCT.
044482     MOVE TDAA-DPOSIT-ALLOW OF TDAACCT TO HOLD-TDAA-DPOSIT-ALLOW  
044484         OF HOLD-TDAACCT.
044486     MOVE TDAA-POST-MAT OF TDAACCT TO HOLD-TDAA-POST-MAT OF       
044488         HOLD-TDAACCT.
044490     MOVE TDAA-RT-FLOOR OF TDAACCT TO HOLD-TDAA-RT-FLOOR OF       
044492         HOLD-TDAACCT.
044494     MOVE TDAA-REPO-CD OF TDAACCT TO HOLD-TDAA-REPO-CD OF         
044496         HOLD-TDAACCT.
044498     MOVE TDAA-TOTAL-CD OF TDAACCT TO HOLD-TDAA-TOTAL-CD OF       
044500         HOLD-TDAACCT.
044502     MOVE TDAA-REN-TOTAL-CD OF TDAACCT TO HOLD-TDAA-REN-TOTAL-CD  
044504         OF HOLD-TDAACCT.
044506     MOVE TDAA-ORG-TOTAL-CD OF TDAACCT TO HOLD-TDAA-ORG-TOTAL-CD  
044508         OF HOLD-TDAACCT.
044510     MOVE TDAA-INQ-SECR-CD OF TDAACCT TO HOLD-TDAA-INQ-SECR-CD OF 
044512         HOLD-TDAACCT.
044514     MOVE TDAA-MAIL-CD OF TDAACCT TO HOLD-TDAA-MAIL-CD OF         
044516         HOLD-TDAACCT.
044518     MOVE TDAA-WTHD-REQD-CD OF TDAACCT TO HOLD-TDAA-WTHD-REQD-CD  
044520         OF HOLD-TDAACCT.
044522     MOVE TDAA-TICKLER-FLAG OF TDAACCT TO HOLD-TDAA-TICKLER-FLAG  
044524         OF HOLD-TDAACCT.
044526     MOVE TDAA-DISP-CD OF TDAACCT TO HOLD-TDAA-DISP-CD OF         
044528         HOLD-TDAACCT.
044530     MOVE TDAA-CLS-DISP-CD OF TDAACCT TO HOLD-TDAA-CLS-DISP-CD OF 
044532         HOLD-TDAACCT.
044534     MOVE TDAA-DIST-STATUS OF TDAACCT TO HOLD-TDAA-DIST-STATUS OF 
044536         HOLD-TDAACCT.
044538     MOVE TDAA-COMM-ACCT OF TDAACCT TO HOLD-TDAA-COMM-ACCT OF     
044540         HOLD-TDAACCT.
044542     MOVE TDAA-RENEW-CD OF TDAACCT TO HOLD-TDAA-RENEW-CD OF       
044544         HOLD-TDAACCT.
044546     MOVE TDAA-PLEDGE-CD OF TDAACCT TO HOLD-TDAA-PLEDGE-CD OF     
044548         HOLD-TDAACCT.
044550     MOVE TDAA-NEGOT-CD OF TDAACCT TO HOLD-TDAA-NEGOT-CD OF       
044552         HOLD-TDAACCT.
044554     MOVE TDAA-BENEF-CD OF TDAACCT TO HOLD-TDAA-BENEF-CD OF       
044556         HOLD-TDAACCT.
044558     MOVE TDAA-COMM-MAT-CD OF TDAACCT TO HOLD-TDAA-COMM-MAT-CD OF 
044560         HOLD-TDAACCT.
044562     MOVE TDAA-NBR-BENEF OF TDAACCT TO HOLD-TDAA-NBR-BENEF OF     
044564         HOLD-TDAACCT.
044566     MOVE TDAA-OVERRIDE OF TDAACCT TO HOLD-TDAA-OVERRIDE OF       
044568         HOLD-TDAACCT.
044570     MOVE TDAA-INT-CD OF TDAACCT TO HOLD-TDAA-INT-CD OF           
044572         HOLD-TDAACCT.
044574     MOVE TDAA-WTHLD-CD OF TDAACCT TO HOLD-TDAA-WTHLD-CD OF       
044576         HOLD-TDAACCT.
044578     MOVE TDAA-WTHLD-AMT OF TDAACCT TO HOLD-TDAA-WTHLD-AMT OF     
044580         HOLD-TDAACCT.
044582     MOVE TDAA-IGL-GRP OF TDAACCT TO HOLD-TDAA-IGL-GRP OF         
044584         HOLD-TDAACCT.
044586     MOVE TDAA-SUM-STMT-CD OF TDAACCT TO HOLD-TDAA-SUM-STMT-CD OF 
044588         HOLD-TDAACCT.
044590     MOVE TDAA-REN-NTC-CD OF TDAACCT TO HOLD-TDAA-REN-NTC-CD OF   
044592         HOLD-TDAACCT.
044594     MOVE TDAA-PMAT-NTC-CD OF TDAACCT TO HOLD-TDAA-PMAT-NTC-CD OF 
044596         HOLD-TDAACCT.
044598     MOVE TDAA-RTCHG-NTC-CD OF TDAACCT TO HOLD-TDAA-RTCHG-NTC-CD  
044600         OF HOLD-TDAACCT.
044602     MOVE TDAA-INT-NTC-CD OF TDAACCT TO HOLD-TDAA-INT-NTC-CD OF   
044604         HOLD-TDAACCT.
044606     MOVE TDAA-CHG-NTC OF TDAACCT TO HOLD-TDAA-CHG-NTC OF         
044608         HOLD-TDAACCT.
044610     MOVE TDAA-YIELD-NUM OF TDAACCT TO HOLD-TDAA-YIELD-NUM OF     
044612         HOLD-TDAACCT.
044614     MOVE TDAA-YIELD-DENOM OF TDAACCT TO HOLD-TDAA-YIELD-DENOM OF 
044616         HOLD-TDAACCT.
044618     MOVE TDAA-CMPD-FREQ OF TDAACCT TO HOLD-TDAA-CMPD-FREQ OF     
044620         HOLD-TDAACCT.
044622     MOVE TDAA-CMPD-NTRVL OF TDAACCT TO HOLD-TDAA-CMPD-NTRVL OF   
044624         HOLD-TDAACCT.
044626     MOVE TDAA-RT-CHG-LIMIT OF TDAACCT TO HOLD-TDAA-RT-CHG-LIMIT  
044628         OF HOLD-TDAACCT.
044630     MOVE TDAA-VAR-RT-IMMED OF TDAACCT TO HOLD-TDAA-VAR-RT-IMMED  
044632         OF HOLD-TDAACCT.
044634     MOVE TDAA-VAR-RT-INT OF TDAACCT TO HOLD-TDAA-VAR-RT-INT OF   
044636         HOLD-TDAACCT.
044638     MOVE TDAA-VAR-RT-SCHED OF TDAACCT TO HOLD-TDAA-VAR-RT-SCHED  
044640         OF HOLD-TDAACCT.
044642     MOVE TDAA-VAR-RT-CUST OF TDAACCT TO HOLD-TDAA-VAR-RT-CUST OF 
044644         HOLD-TDAACCT.
044646     MOVE TDAA-VAR-RT-BAL OF TDAACCT TO HOLD-TDAA-VAR-RT-BAL OF   
044648         HOLD-TDAACCT.
044650     MOVE TDAA-RT-INDX-CD OF TDAACCT TO HOLD-TDAA-RT-INDX-CD OF   
044652         HOLD-TDAACCT.
044654     MOVE TDAA-R-RT-INDX-CD OF TDAACCT TO HOLD-TDAA-R-RT-INDX-CD  
044656         OF HOLD-TDAACCT.
044658     MOVE TDAA-RT-MARG-CD OF TDAACCT TO HOLD-TDAA-RT-MARG-CD OF   
044660         HOLD-TDAACCT.
044662     MOVE TDAA-R-RT-MARG-CD OF TDAACCT TO HOLD-TDAA-R-RT-MARG-CD  
044664         OF HOLD-TDAACCT.
044666     MOVE TDAA-RT-TIER-CD OF TDAACCT TO HOLD-TDAA-RT-TIER-CD OF   
044668         HOLD-TDAACCT.
044670     MOVE TDAA-R-RT-TIER-CD OF TDAACCT TO HOLD-TDAA-R-RT-TIER-CD  
044672         OF HOLD-TDAACCT.
044674     MOVE TDAA-RT-SR-CD OF TDAACCT TO HOLD-TDAA-RT-SR-CD OF       
044676         HOLD-TDAACCT.
044678     MOVE TDAA-R-RT-SR-CD OF TDAACCT TO HOLD-TDAA-R-RT-SR-CD OF   
044680         HOLD-TDAACCT.
044682     MOVE TDAA-RT-REGN-CD OF TDAACCT TO HOLD-TDAA-RT-REGN-CD OF   
044684         HOLD-TDAACCT.
044686     MOVE TDAA-RT-CHG-NTRVL OF TDAACCT TO HOLD-TDAA-RT-CHG-NTRVL  
044688         OF HOLD-TDAACCT.
044690     MOVE TDAA-CAP-RT-CHG OF TDAACCT TO HOLD-TDAA-CAP-RT-CHG OF   
044692         HOLD-TDAACCT.
044694     MOVE TDAA-R-TIER-RT-CH OF TDAACCT TO HOLD-TDAA-R-TIER-RT-CH  
044696         OF HOLD-TDAACCT.
044698     MOVE TDAA-ALERT-CD OF TDAACCT TO HOLD-TDAA-ALERT-CD OF       
044700         HOLD-TDAACCT.
044702     MOVE TDAA-ALERT-CD-2 OF TDAACCT TO HOLD-TDAA-ALERT-CD-2 OF   
044704         HOLD-TDAACCT.
044706     MOVE TDAA-ALERT-CD-3 OF TDAACCT TO HOLD-TDAA-ALERT-CD-3 OF   
044708         HOLD-TDAACCT.
044710     MOVE TDAA-CENSUS-TRACT OF TDAACCT TO HOLD-TDAA-CENSUS-TRACT  
044712         OF HOLD-TDAACCT.
044714     MOVE TDAA-MK-SEGMENT OF TDAACCT TO HOLD-TDAA-MK-SEGMENT OF   
044716         HOLD-TDAACCT.
044718     MOVE TDAA-BK-DEF-TOT OF TDAACCT TO HOLD-TDAA-BK-DEF-TOT OF   
044720         HOLD-TDAACCT.
044722     MOVE TDAA-BK-DEF-CD1 OF TDAACCT TO HOLD-TDAA-BK-DEF-CD1 OF   
044724         HOLD-TDAACCT.
044726     MOVE TDAA-BK-DEF-CD2 OF TDAACCT TO HOLD-TDAA-BK-DEF-CD2 OF   
044728         HOLD-TDAACCT.
044730     MOVE TDAA-BK-DEF-CD3 OF TDAACCT TO HOLD-TDAA-BK-DEF-CD3 OF   
044732         HOLD-TDAACCT.
044734     MOVE TDAA-BK-DEF-CD4 OF TDAACCT TO HOLD-TDAA-BK-DEF-CD4 OF   
044736         HOLD-TDAACCT.
044738     MOVE TDAA-BK-DEF-CD5 OF TDAACCT TO HOLD-TDAA-BK-DEF-CD5 OF   
044740         HOLD-TDAACCT.
044742     MOVE TDAA-OID-METH OF TDAACCT TO HOLD-TDAA-OID-METH OF       
044744         HOLD-TDAACCT.
044746     MOVE TDAA-EOY-CD OF TDAACCT TO HOLD-TDAA-EOY-CD OF           
044748         HOLD-TDAACCT.
044750     MOVE TDAA-B-NOTC-YR1 OF TDAACCT TO HOLD-TDAA-B-NOTC-YR1 OF   
044752         HOLD-TDAACCT.
044754     MOVE TDAA-B-NOTC-YR2 OF TDAACCT TO HOLD-TDAA-B-NOTC-YR2 OF   
044756         HOLD-TDAACCT.
044758     MOVE TDAA-B-NOTC-YR3 OF TDAACCT TO HOLD-TDAA-B-NOTC-YR3 OF   
044760         HOLD-TDAACCT.
044762     MOVE TDAA-NO-COMB-IRS OF TDAACCT TO HOLD-TDAA-NO-COMB-IRS OF 
044764         HOLD-TDAACCT.
044766     MOVE TDAA-PENLTY-CD OF TDAACCT TO HOLD-TDAA-PENLTY-CD OF     
044768         HOLD-TDAACCT.
044770     MOVE TDAA-MONEY-SRC-CD OF TDAACCT TO HOLD-TDAA-MONEY-SRC-CD  
044772         OF HOLD-TDAACCT.
044774     MOVE TDAA-INTERNET-BPY OF TDAACCT TO HOLD-TDAA-INTERNET-BPY  
044776         OF HOLD-TDAACCT.
044778     MOVE TDAA-INTERNET-TFR OF TDAACCT TO HOLD-TDAA-INTERNET-TFR  
044780         OF HOLD-TDAACCT.
044782     MOVE TDAA-INTERNET-INQ OF TDAACCT TO HOLD-TDAA-INTERNET-INQ  
044784         OF HOLD-TDAACCT.
044786     MOVE TDAA-IRA-BACKED OF TDAACCT TO HOLD-TDAA-IRA-BACKED OF   
044788         HOLD-TDAACCT.
044790     MOVE TDAA-SAV-DEPOSIT OF TDAACCT TO HOLD-TDAA-SAV-DEPOSIT OF 
044792         HOLD-TDAACCT.
044794     MOVE TDAA-MAT-TYPE OF TDAACCT TO HOLD-TDAA-MAT-TYPE OF       
044796         HOLD-TDAACCT.
044798     MOVE TDAA-MAT-TERM OF TDAACCT TO HOLD-TDAA-MAT-TERM OF       
044800         HOLD-TDAACCT.
044802     MOVE TDAA-ORG-MAT-TYPE OF TDAACCT TO HOLD-TDAA-ORG-MAT-TYPE  
044804         OF HOLD-TDAACCT.
044806     MOVE TDAA-ORG-MAT-TERM OF TDAACCT TO HOLD-TDAA-ORG-MAT-TERM  
044808         OF HOLD-TDAACCT.
044810     MOVE TDAA-ODD-PAYMENT OF TDAACCT TO HOLD-TDAA-ODD-PAYMENT OF 
044812         HOLD-TDAACCT.
044814     MOVE TDAA-PAY-FREQ OF TDAACCT TO HOLD-TDAA-PAY-FREQ OF       
044816         HOLD-TDAACCT.
044818     MOVE TDAA-PAY-NTRVL OF TDAACCT TO HOLD-TDAA-PAY-NTRVL OF     
044820         HOLD-TDAACCT.
044822     MOVE TDAA-FEE-FREQ OF TDAACCT TO HOLD-TDAA-FEE-FREQ OF       
044824         HOLD-TDAACCT.
044826     MOVE TDAA-FEE-NTRVL OF TDAACCT TO HOLD-TDAA-FEE-NTRVL OF     
044828         HOLD-TDAACCT.
044830     MOVE TDAA-STMT-FREQ OF TDAACCT TO HOLD-TDAA-STMT-FREQ OF     
044832         HOLD-TDAACCT.
044834     MOVE TDAA-STMT-NTRVL OF TDAACCT TO HOLD-TDAA-STMT-NTRVL OF   
044836         HOLD-TDAACCT.
044838     MOVE TDAA-EMPLOYEE-ID OF TDAACCT TO HOLD-TDAA-EMPLOYEE-ID OF 
044840         HOLD-TDAACCT.
044842     MOVE TDAA-EFT-CARD OF TDAACCT TO HOLD-TDAA-EFT-CARD OF       
044844         HOLD-TDAACCT.
044846     MOVE TDAA-PEN-WAV-RESN OF TDAACCT TO HOLD-TDAA-PEN-WAV-RESN  
044848         OF HOLD-TDAACCT.
044850     MOVE TDAA-CLOSED-RESN OF TDAACCT TO HOLD-TDAA-CLOSED-RESN OF 
044852         HOLD-TDAACCT.
044854     MOVE TDAA-SPECIAL-STMT OF TDAACCT TO HOLD-TDAA-SPECIAL-STMT  
044856         OF HOLD-TDAACCT.
044858     MOVE TDAA-CLS-THIS-MTH OF TDAACCT TO HOLD-TDAA-CLS-THIS-MTH  
044860         OF HOLD-TDAACCT.
044862     MOVE TDAA-RC-MAT-ONLY OF TDAACCT TO HOLD-TDAA-RC-MAT-ONLY OF 
044864         HOLD-TDAACCT.
044866     MOVE TDAA-GRACE-DAYS OF TDAACCT TO HOLD-TDAA-GRACE-DAYS OF   
044868         HOLD-TDAACCT.
044870     MOVE TDAA-CLS-ON-MAT OF TDAACCT TO HOLD-TDAA-CLS-ON-MAT OF   
044872         HOLD-TDAACCT.
044874     MOVE TDAA-DDA-ACCT-1 OF TDAACCT TO HOLD-TDAA-DDA-ACCT-1 OF   
044876         HOLD-TDAACCT.
044878     MOVE TDAA-DDA-ACCT-1-S OF TDAACCT TO HOLD-TDAA-DDA-ACCT-1-S  
044880         OF HOLD-TDAACCT.
044882     MOVE TDAA-DDA-ACCT-2 OF TDAACCT TO HOLD-TDAA-DDA-ACCT-2 OF   
044884         HOLD-TDAACCT.
044886     MOVE TDAA-DDA-ACCT-2-S OF TDAACCT TO HOLD-TDAA-DDA-ACCT-2-S  
044888         OF HOLD-TDAACCT.
044890     MOVE TDAA-DDA-ACCT-3 OF TDAACCT TO HOLD-TDAA-DDA-ACCT-3 OF   
044892         HOLD-TDAACCT.
044894     MOVE TDAA-DDA-ACCT-3-S OF TDAACCT TO HOLD-TDAA-DDA-ACCT-3-S  
044896         OF HOLD-TDAACCT.
044898     MOVE TDAA-INT-ACCT OF TDAACCT TO HOLD-TDAA-INT-ACCT OF       
044900         HOLD-TDAACCT.
044902     MOVE TDAA-INT-ACCT-S OF TDAACCT TO HOLD-TDAA-INT-ACCT-S OF   
044904         HOLD-TDAACCT.
044906     MOVE TDAA-CS-ACCT OF TDAACCT TO HOLD-TDAA-CS-ACCT OF         
044908         HOLD-TDAACCT.
044910     MOVE TDAA-CS-ACCT-S OF TDAACCT TO HOLD-TDAA-CS-ACCT-S OF     
044912         HOLD-TDAACCT.
044914     MOVE TDAA-CC-ACCT OF TDAACCT TO HOLD-TDAA-CC-ACCT OF         
044916         HOLD-TDAACCT.
044918     MOVE TDAA-LNS-BORROWER OF TDAACCT TO HOLD-TDAA-LNS-BORROWER  
044920         OF HOLD-TDAACCT.
044922     MOVE TDAA-LNS-NOTE OF TDAACCT TO HOLD-TDAA-LNS-NOTE OF       
044924         HOLD-TDAACCT.
044926     MOVE TDAA-CNV-OLD-ACCT OF TDAACCT TO HOLD-TDAA-CNV-OLD-ACCT  
044928         OF HOLD-TDAACCT.
044930     MOVE TDAA-CLS-ACCT OF TDAACCT TO HOLD-TDAA-CLS-ACCT OF       
044932         HOLD-TDAACCT.
044934     MOVE TDAA-CLS-ACCT-S OF TDAACCT TO HOLD-TDAA-CLS-ACCT-S OF   
044936         HOLD-TDAACCT.
044938     MOVE TDAA-DAYS-IN-PER OF TDAACCT TO HOLD-TDAA-DAYS-IN-PER OF 
044940         HOLD-TDAACCT.
044942     MOVE TDAA-RR-CYC-NBR OF TDAACCT TO HOLD-TDAA-RR-CYC-NBR OF   
044944         HOLD-TDAACCT.
044946     MOVE TDAA-CR-CNT-STD OF TDAACCT TO HOLD-TDAA-CR-CNT-STD OF   
044948         HOLD-TDAACCT.
044950     MOVE TDAA-CR-AMT-STD OF TDAACCT TO HOLD-TDAA-CR-AMT-STD OF   
044952         HOLD-TDAACCT.
044954     MOVE TDAA-DB-CNT-STD OF TDAACCT TO HOLD-TDAA-DB-CNT-STD OF   
044956         HOLD-TDAACCT.
044958     MOVE TDAA-DB-AMT-STD OF TDAACCT TO HOLD-TDAA-DB-AMT-STD OF   
044960         HOLD-TDAACCT.
044962     MOVE TDAA-CR-CNT-YTD OF TDAACCT TO HOLD-TDAA-CR-CNT-YTD OF   
044964         HOLD-TDAACCT.
044966     MOVE TDAA-CR-AMT-YTD OF TDAACCT TO HOLD-TDAA-CR-AMT-YTD OF   
044968         HOLD-TDAACCT.
044970     MOVE TDAA-DB-CNT-YTD OF TDAACCT TO HOLD-TDAA-DB-CNT-YTD OF   
044972         HOLD-TDAACCT.
044974     MOVE TDAA-DB-AMT-YTD OF TDAACCT TO HOLD-TDAA-DB-AMT-YTD OF   
044976         HOLD-TDAACCT.
044978     MOVE TDAA-DAYS-IN-TERM OF TDAACCT TO HOLD-TDAA-DAYS-IN-TERM  
044980         OF HOLD-TDAACCT.
044982     MOVE TDAA-BEG-INT-BAL OF TDAACCT TO HOLD-TDAA-BEG-INT-BAL OF 
044984         HOLD-TDAACCT.
044986     MOVE TDAA-PURCH-AMT OF TDAACCT TO HOLD-TDAA-PURCH-AMT OF     
044988         HOLD-TDAACCT.
044990     MOVE TDAA-CURR-BAL OF TDAACCT TO HOLD-TDAA-CURR-BAL OF       
044992         HOLD-TDAACCT.
044994     MOVE TDAA-AVAIL-BAL OF TDAACCT TO HOLD-TDAA-AVAIL-BAL OF     
044996         HOLD-TDAACCT.
044998     MOVE TDAA-BAL-BEG-MAT OF TDAACCT TO HOLD-TDAA-BAL-BEG-MAT OF 
045000         HOLD-TDAACCT.
045002     MOVE TDAA-CLOSE-AMT OF TDAACCT TO HOLD-TDAA-CLOSE-AMT OF     
045004         HOLD-TDAACCT.
045006     MOVE TDAA-MONEY-AMT OF TDAACCT TO HOLD-TDAA-MONEY-AMT OF     
045008         HOLD-TDAACCT.
045010     MOVE TDAA-BAL-BEG-STMT OF TDAACCT TO HOLD-TDAA-BAL-BEG-STMT  
045012         OF HOLD-TDAACCT.
045014     MOVE TDAA-ACCR-INT OF TDAACCT TO HOLD-TDAA-ACCR-INT OF       
045016         HOLD-TDAACCT.
045018     MOVE TDAA-ANTIC-INT OF TDAACCT TO HOLD-TDAA-ANTIC-INT OF     
045020         HOLD-TDAACCT.
045022     MOVE TDAA-INT-TO-POST OF TDAACCT TO HOLD-TDAA-INT-TO-POST OF 
045024         HOLD-TDAACCT.
045026     MOVE TDAA-1099-YTD OF TDAACCT TO HOLD-TDAA-1099-YTD OF       
045028         HOLD-TDAACCT.
045030     MOVE TDAA-1099-LST-YR OF TDAACCT TO HOLD-TDAA-1099-LST-YR OF 
045032         HOLD-TDAACCT.
045034     MOVE TDAA-CURR-PENLTY OF TDAACCT TO HOLD-TDAA-CURR-PENLTY OF 
045036         HOLD-TDAACCT.
045038     MOVE TDAA-PENLTY-STD OF TDAACCT TO HOLD-TDAA-PENLTY-STD OF   
045040         HOLD-TDAACCT.
045042     MOVE TDAA-PENLTY-YTD OF TDAACCT TO HOLD-TDAA-PENLTY-YTD OF   
045044         HOLD-TDAACCT.
045046     MOVE TDAA-LST-PENLTY OF TDAACCT TO HOLD-TDAA-LST-PENLTY OF   
045048         HOLD-TDAACCT.
045050     MOVE TDAA-CURR-INT-ADJ OF TDAACCT TO HOLD-TDAA-CURR-INT-ADJ  
045052         OF HOLD-TDAACCT.
045054     MOVE TDAA-TOTAMT-HOLDS OF TDAACCT TO HOLD-TDAA-TOTAMT-HOLDS  
045056         OF HOLD-TDAACCT.
045058     MOVE TDAA-NXT-INT-ADJ OF TDAACCT TO HOLD-TDAA-NXT-INT-ADJ OF 
045060         HOLD-TDAACCT.
045062     MOVE TDAA-FEE-AMT OF TDAACCT TO HOLD-TDAA-FEE-AMT OF         
045064         HOLD-TDAACCT.
045066     MOVE TDAA-OID-RPT-INT OF TDAACCT TO HOLD-TDAA-OID-RPT-INT OF 
045068         HOLD-TDAACCT.
045070     MOVE TDAA-FAIR-MRKT OF TDAACCT TO HOLD-TDAA-FAIR-MRKT OF     
045072         HOLD-TDAACCT.
045074     MOVE TDAA-CUR-WHLD-AMT OF TDAACCT TO HOLD-TDAA-CUR-WHLD-AMT  
045076         OF HOLD-TDAACCT.
045078     MOVE TDAA-LST-WHLD-AMT OF TDAACCT TO HOLD-TDAA-LST-WHLD-AMT  
045080         OF HOLD-TDAACCT.
045082     MOVE TDAA-WTHLD-STD OF TDAACCT TO HOLD-TDAA-WTHLD-STD OF     
045084         HOLD-TDAACCT.
045086     MOVE TDAA-WTHLD-YTD OF TDAACCT TO HOLD-TDAA-WTHLD-YTD OF     
045088         HOLD-TDAACCT.
045090     MOVE TDAA-LST-INT-PMT OF TDAACCT TO HOLD-TDAA-LST-INT-PMT OF 
045092         HOLD-TDAACCT.
045094     MOVE TDAA-BAL-BEG-YR OF TDAACCT TO HOLD-TDAA-BAL-BEG-YR OF   
045096         HOLD-TDAACCT.
045098     MOVE TDAA-BAL-AT-CONV OF TDAACCT TO HOLD-TDAA-BAL-AT-CONV OF 
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 423 lines from 22123 to 22545.

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

