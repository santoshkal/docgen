# LLM Request Debug File
Generated: 2025-11-13T21:18:19.853638

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 36/55
- **Model**: gpt-4.1
- **Chunk Number**: 36
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~9,137 tokens
- **Total Input**: ~11,095 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 36/55" (ID: detailed-code-explanation)

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


**CHUNK 36 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 36 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 17408 to 17909 (502 lines)\nChunk Tokens (estimated): ~8,084\nActual Input Tokens: 9,490 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 17408-17909 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 36 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 36 of 55.\n\n\n=============================================================================\nCHUNK 36 SOURCE CODE (Lines 17408-17909)\n=============================================================================\n\n```cobol\n034824 Z-23-78-1-ELSE.\n034826     IF WS-DSREC-FLAG = 1\n034828         NEXT SENTENCE ELSE\n034830         GO TO Z-23-81-1-ELSE.\n034832     IF TDB-TDAD-INTEREST = 1\n034834         NEXT SENTENCE ELSE\n034836         GO TO Z-23-82-1-ELSE.\n034838     MOVE \"I\" TO RMDRPT-DS-FREQ-3\n034840       , WS-RMDRPT-DS-FREQ.\n034842     MOVE ZEROS TO RMDRPT-OLD-DS-AMT-3\n034844       , RMDRPT-NEW-DS-AMT-3\n034846       , RMDRPT-DS-NTRVL-3\n034848       , WS-RMDRPT-OLD-DS-AMT\n034850       , WS-RMDRPT-DS-NTRVL\n034852       , RMDRPT2-OLD-DS-AMT-3\n034854       , RMDRPT2-NEW-DS-AMT-3.\n034856     MOVE SPACES TO RMDRPT-WH-MSG-4.\n034858     GO TO Z-23-82-ENDIF.\n034860 Z-23-82-1-ELSE.\n034862     MOVE SPACES TO RMDRPT-DS-METH-4\n034864       , WS-RMDRPT-DS-METH.\n034866     IF TDB-TDAD-DISP-CD = 1\n034868         NEXT SENTENCE\n034870     ELSE\n034872         GO TO Z-23-87-END-MOVE.\n034874     MOVE \"CHK\" TO RMDRPT-DS-METH-4\n034876       , WS-RMDRPT-DS-METH.\n034878 Z-23-87-END-MOVE.\n034880     IF TDB-TDAD-DISP-CD = 2\n034882         NEXT SENTENCE\n034884     ELSE\n034886         GO TO Z-23-88-END-MOVE.\n034888     MOVE \"DDA\" TO RMDRPT-DS-METH-4\n034890       , WS-RMDRPT-DS-METH.\n034892 Z-23-88-END-MOVE.\n034894     IF TDB-TDAD-DISP-CD = 3\n034896         NEXT SENTENCE\n034898     ELSE\n034900         GO TO Z-23-89-END-MOVE.\n034902     MOVE \"SAV\" TO RMDRPT-DS-METH-4\n034904       , WS-RMDRPT-DS-METH.\n034906 Z-23-89-END-MOVE.\n034908     IF TDB-TDAD-DISP-CD = 4\n034910         NEXT SENTENCE\n034912     ELSE\n034914         GO TO Z-23-90-END-MOVE.\n034916     MOVE \"LIST\" TO RMDRPT-DS-METH-4\n034918       , WS-RMDRPT-DS-METH.\n034920 Z-23-90-END-MOVE.\n034922     IF TDB-TDAD-DISP-CD = 5\n034924         NEXT SENTENCE\n034926     ELSE\n034928         GO TO Z-23-91-END-MOVE.\n034930     MOVE \"COD\" TO RMDRPT-DS-METH-4\n034932       , WS-RMDRPT-DS-METH.\n034934 Z-23-91-END-MOVE.\n034936     IF TDB-TDAD-DISP-CD = 9\n034938         NEXT SENTENCE\n034940     ELSE\n034942         GO TO Z-23-92-END-MOVE.\n034944     MOVE \"MAN\" TO RMDRPT-DS-METH-4\n034946       , WS-RMDRPT-DS-METH.\n034948 Z-23-92-END-MOVE.\n034950     MOVE TDB-TDAD-DS-NTRVL TO RMDRPT-DS-NTRVL-3\n034952       , WS-RMDRPT-DS-NTRVL.\n034954     MOVE TDB-TDAD-DS-AMT TO RMDRPT-OLD-DS-AMT-3\n034956       , RMDRPT2-OLD-DS-AMT-3\n034958       , WS-RMDRPT-OLD-DS-AMT.\n034960     IF TDB-TDAD-DS-FREQ = 2\n034962         NEXT SENTENCE ELSE\n034964         GO TO Z-23-95-1-ELSE.\n034966     MOVE \"M\" TO RMDRPT-DS-FREQ-3\n034968       , WS-RMDRPT-DS-FREQ.\n034970     COMPUTE WS-NEW-DS-AMT ROUNDED = ( ( WS-MD-AMT / 12 ) *       \n034972         TDB-TDAD-DS-NTRVL ) .\n034974\n034976     GO TO Z-23-95-ENDIF.\n034978 Z-23-95-1-ELSE.\n034980     IF TDB-TDAD-DS-FREQ = 1\n034982         NEXT SENTENCE ELSE\n034984         GO TO Z-23-95-2-ELSE.\n034986     MOVE \"D\" TO RMDRPT-DS-FREQ-3\n034988       , WS-RMDRPT-DS-FREQ.\n034990     COMPUTE WS-NEW-DS-AMT ROUNDED = ( ( WS-MD-AMT / 365 ) *      \n034992         TDB-TDAD-DS-NTRVL ) .\n034994\n034996     GO TO Z-23-95-ENDIF.\n034998 Z-23-95-2-ELSE.\n035000     IF TDB-TDAD-DS-FREQ = 9\n035002         NEXT SENTENCE ELSE\n035004         GO TO Z-23-95-3-ELSE.\n035006     MOVE \"ONCE  \" TO RMDRPT-DIST-FREQ-3.\n035008     COMPUTE WS-NEW-DS-AMT = WS-MD-AMT .\n035010\n035012 Z-23-95-3-ELSE.\n035014 Z-23-95-ENDIF.\n035016     IF ( WS-NEW-DS-AMT < TDB-TDAD-WHLD-AMT ) AND (               \n035018         TDB-TDAD-WTHLD-CD = 0 )\n035020         NEXT SENTENCE ELSE\n035022         GO TO Z-23-102-1-ELSE.\n035024     MOVE \"W/H > DIST\" TO RMDRPT-WH-MSG-4.\n035026     GO TO Z-23-102-ENDIF.\n035028 Z-23-102-1-ELSE.\n035030     MOVE SPACES TO RMDRPT-WH-MSG-4.\n035032 Z-23-102-ENDIF.\n035034     MOVE WS-NEW-DS-AMT TO RMDRPT-NEW-DS-AMT-3\n035036       , RMDRPT2-NEW-DS-AMT-3.\n035038 Z-23-82-ENDIF.\n035040     GO TO Z-23-81-ENDIF.\n035042 Z-23-81-1-ELSE.\n035044     MOVE \"NONE\" TO RMDRPT-DS-NTRVL-3\n035046       , WS-RMDRPT-DS-NTRVL.\n035048     MOVE SPACE TO RMDRPT-DS-FREQ-3\n035050       , WS-RMDRPT-DS-FREQ.\n035052     MOVE ZEROS TO RMDRPT-OLD-DS-AMT-3\n035054       , RMDRPT-NEW-DS-AMT-3\n035056       , WS-RMDRPT-OLD-DS-AMT\n035058       , RMDRPT2-OLD-DS-AMT-3\n035060       , RMDRPT2-NEW-DS-AMT-3.\n035062 Z-23-81-ENDIF.\n035064     IF ( TDB-TDAA-INHERIT-IRA > 0 ) AND ( NOT Z-SW3 )\n035066         NEXT SENTENCE ELSE\n035068         GO TO Z-23-109-1-ELSE.\n035070     MOVE 1 TO WS-INHERIT-IRA-ON-TIN.\n035072     MOVE RMDRPT-CUST-3 OF RMDRPT-REC-3 TO RMDRPT2-CUST-3 OF      \n035074         RMDRPT2-REC-3.\n035076     MOVE RMDRPT-ACCT-3 OF RMDRPT-REC-3 TO RMDRPT2-ACCT-3 OF      \n035078         RMDRPT2-REC-3.\n035080     MOVE RMDRPT-BIRTH-DT-3 OF RMDRPT-REC-3 TO RMDRPT2-BIRTH-DT-3 \n035082         OF RMDRPT2-REC-3.\n035084     MOVE RMDRPT-AGE-DATE-3 OF RMDRPT-REC-3 TO RMDRPT2-AGE-DATE-3 \n035086         OF RMDRPT2-REC-3.\n035088     MOVE RMDRPT-BEG-DATE-3 OF RMDRPT-REC-3 TO RMDRPT2-BEG-DATE-3 \n035090         OF RMDRPT2-REC-3.\n035092     MOVE RMDRPT-CUR-BAL-IND-3 OF RMDRPT-REC-3 TO                 \n035094         RMDRPT2-CUR-BAL-IND-3 OF RMDRPT2-REC-3.\n035096     MOVE RMDRPT-SLASH-3 OF RMDRPT-REC-3 TO RMDRPT2-SLASH-3 OF    \n035098         RMDRPT2-REC-3.\n035100     MOVE RMDRPT-TBL-3 OF RMDRPT-REC-3 TO RMDRPT2-TBL-3 OF        \n035102         RMDRPT2-REC-3.\n035104     MOVE RMDRPT-RMD-MAN-CALC-3 OF RMDRPT-REC-3 TO                \n035106         RMDRPT2-RMD-MAN-CALC-3 OF RMDRPT2-REC-3.\n035108     MOVE RMDRPT-DS-NTRVL-3 OF RMDRPT-REC-3 TO RMDRPT2-DS-NTRVL-3 \n035110         OF RMDRPT2-REC-3.\n035112     MOVE RMDRPT-DS-FREQ-3 OF RMDRPT-REC-3 TO RMDRPT2-DS-FREQ-3   \n035114         OF RMDRPT2-REC-3.\n035116     IF TDB-TDAA-BNF-DEATH-DT > 0\n035118         NEXT SENTENCE ELSE\n035120         GO TO Z-23-112-1-ELSE.\n035122     MOVE TDB-TDAA-BNF-DEATH-DT TO Z-DATE2-FORMAT-9.\n035124*\n035126     PERFORM Z-DATE-INITIALIZE-REGS\n035128         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n035130     MOVE Z-DATE2-MM TO Z-DATE6-MM.\n035132     MOVE \"/\" TO Z-DATE6-CH1.\n035134     MOVE Z-DATE2-DD TO Z-DATE6-DD.\n035136     MOVE \"/\" TO Z-DATE6-CH2.\n035138     MOVE Z-DATE2-CC TO Z-DATE6-CC.\n035140     MOVE Z-DATE2-YY TO Z-DATE6-YY.\n035142     MOVE Z-DATE6-FORMAT TO RMDRPT2-DTH-DATE-3.\n035144     GO TO Z-23-112-ENDIF.\n035146 Z-23-112-1-ELSE.\n035148     MOVE \"   NONE   \" TO RMDRPT2-DTH-DATE-3.\n035150 Z-23-112-ENDIF.\n035152     COMPUTE Z-LINES-HOLD = 1.\n035154     COMPUTE Z-LINES = 1.\n035156     IF Z-RPT-2-TRAP > ZERO\n035158         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.\n035160     IF Z-LINES > Z-RPT-2-TRAP\n035162       IF Z-RPTINFO2-INBLOCK = ZERO\n035164         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1\n035166         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT\n035168         COMPUTE Z-LINES = 1.\n035170     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).\n035172     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).\n035174     MOVE RMDRPT2-REC-3 TO Z-RPT-2-BUFFER.\n035176     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.\n035178     MOVE RMDRPT-NAME-4 OF RMDRPT-REC-4 TO RMDRPT2-NAME-4 OF      \n035180         RMDRPT2-REC-4.\n035182     MOVE RMDRPT-REMARK-4 OF RMDRPT-REC-4 TO RMDRPT2-REMARK-4 OF  \n035184         RMDRPT2-REC-4.\n035186     MOVE RMDRPT-REMARK2-4 OF RMDRPT-REC-4 TO RMDRPT2-REMARK2-4   \n035188         OF RMDRPT2-REC-4.\n035190     MOVE RMDRPT-DS-METH-4 OF RMDRPT-REC-4 TO RMDRPT2-DS-METH-4   \n035192         OF RMDRPT2-REC-4.\n035194     MOVE RMDRPT-WH-MSG-4 OF RMDRPT-REC-4 TO RMDRPT2-WH-MSG-4 OF  \n035196         RMDRPT2-REC-4.\n035198     COMPUTE Z-LINES-HOLD = 1.\n035200     COMPUTE Z-LINES = 1.\n035202     IF Z-RPT-2-TRAP > ZERO\n035204         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.\n035206     IF Z-LINES > Z-RPT-2-TRAP\n035208       IF Z-RPTINFO2-INBLOCK = ZERO\n035210         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1\n035212         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT\n035214         COMPUTE Z-LINES = 1.\n035216     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).\n035218     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).\n035220     MOVE RMDRPT2-REC-4 TO Z-RPT-2-BUFFER.\n035222     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.\n035224     IF RMDRPT-NAME-8 NOT = SPACES\n035226         NEXT SENTENCE ELSE\n035228         GO TO Z-23-118-1-ELSE.\n035230     MOVE RMDRPT-NAME-8 OF RMDRPT-REC-8 TO RMDRPT2-NAME-8 OF      \n035232         RMDRPT2-REC-8.\n035234     COMPUTE Z-LINES-HOLD = 1.\n035236     COMPUTE Z-LINES = 1.\n035238     IF Z-RPT-2-TRAP > ZERO\n035240         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.\n035242     IF Z-LINES > Z-RPT-2-TRAP\n035244       IF Z-RPTINFO2-INBLOCK = ZERO\n035246         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1\n035248         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT\n035250         COMPUTE Z-LINES = 1.\n035252     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).\n035254     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).\n035256     MOVE RMDRPT2-REC-8 TO Z-RPT-2-BUFFER.\n035258     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.\n035260 Z-23-118-1-ELSE.\n035262********* ADD WHEN\n035264     IF ( WS-MULTI-DISTR = 1 ) OR ( WS-DSREC-FLAG = 0 )\n035266        NEXT SENTENCE\n035268     ELSE\n035270        GO TO Z-23-121-ADD-SKIP.\n035272     ADD 1 TO RMD-COUNT-INHERIT .\n035274 Z-23-121-ADD-SKIP.\n035276     GO TO Z-23-109-ENDIF.\n035278 Z-23-109-1-ELSE.\n035280     MOVE 1 TO WS-NON-INHERIT-IRA-ON-TIN.\n035282     IF ( ( WS-MULTI-DISTR = 1 ) OR ( WS-DSREC-FLAG = 0 ) ) AND ( \n035284         NOT Z-SW3 )\n035286         NEXT SENTENCE ELSE\n035288         GO TO Z-23-123-1-ELSE.\n035290     IF ( SPECS-COMB-AUTO-RMD-ADJUST = \"Y\" )\n035292         NEXT SENTENCE ELSE\n035294         GO TO Z-23-124-1-ELSE.\n035296     ADD 1 TO WS-TIN-DETAIL-INDEX .\n035298     IF WS-TIN-DETAIL-INDEX NOT > WS-TIN-DETAIL-MAX\n035300         NEXT SENTENCE ELSE\n035302         GO TO Z-23-126-1-ELSE.\n035304     MOVE RMDRPT-REC-3 TO WS-TIN-DET-LINE-3 (WS-TIN-DETAIL-INDEX).\n035306     MOVE RMDRPT-REC-4 TO WS-TIN-DET-LINE-4 (WS-TIN-DETAIL-INDEX).\n035308     MOVE RMDRPT-REC-8 TO WS-TIN-DET-LINE-8 (WS-TIN-DETAIL-INDEX).\n035310 Z-23-126-1-ELSE.\n035312     GO TO Z-23-124-ENDIF.\n035314 Z-23-124-1-ELSE.\n035316     COMPUTE Z-LINES-HOLD = 1.\n035318     COMPUTE Z-LINES = 1.\n035320     IF Z-RPT-1-TRAP > ZERO\n035322         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n035324     IF Z-LINES > Z-RPT-1-TRAP\n035326       IF Z-RPTINFO1-INBLOCK = ZERO\n035328         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n035330         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n035332         COMPUTE Z-LINES = 1.\n035334     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n035336     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n035338     MOVE RMDRPT-REC-3 TO Z-RPT-1-BUFFER.\n035340     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n035342     COMPUTE Z-LINES-HOLD = 1.\n035344     COMPUTE Z-LINES = 1.\n035346     IF Z-RPT-1-TRAP > ZERO\n035348         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n035350     IF Z-LINES > Z-RPT-1-TRAP\n035352       IF Z-RPTINFO1-INBLOCK = ZERO\n035354         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n035356         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n035358         COMPUTE Z-LINES = 1.\n035360     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n035362     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n035364     MOVE RMDRPT-REC-4 TO Z-RPT-1-BUFFER.\n035366     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n035368     IF RMDRPT-NAME-8 NOT = SPACES\n035370         NEXT SENTENCE ELSE\n035372         GO TO Z-23-132-1-ELSE.\n035374     COMPUTE Z-LINES-HOLD = 1.\n035376     COMPUTE Z-LINES = 1.\n035378     IF Z-RPT-1-TRAP > ZERO\n035380         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n035382     IF Z-LINES > Z-RPT-1-TRAP\n035384       IF Z-RPTINFO1-INBLOCK = ZERO\n035386         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n035388         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n035390         COMPUTE Z-LINES = 1.\n035392     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n035394     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n035396     MOVE RMDRPT-REC-8 TO Z-RPT-1-BUFFER.\n035398     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n035400 Z-23-132-1-ELSE.\n035402 Z-23-124-ENDIF.\n035404     GO TO Z-23-123-ENDIF.\n035406 Z-23-123-1-ELSE.\n035408     MOVE RMDRPT-CUST-3 TO HOLD-TDAC-CUST.\n035410     MOVE SPACES TO RMDRPT-REC-3.\n035412     MOVE WS-RMDRPT-DS-FREQ TO RMDRPT-DS-FREQ-3.\n035414     MOVE WS-RMDRPT-DS-NTRVL TO RMDRPT-DS-NTRVL-3.\n035416     MOVE WS-RMDRPT-OLD-DS-AMT TO RMDRPT-OLD-DS-AMT-3.\n035418     IF ( NOT Z-SW3 )\n035420         NEXT SENTENCE ELSE\n035422         GO TO Z-23-139-1-ELSE.\n035424     IF ( SPECS-COMB-AUTO-RMD-ADJUST = \"Y\" )\n035426         NEXT SENTENCE ELSE\n035428         GO TO Z-23-140-1-ELSE.\n035430     ADD 1 TO WS-TIN-DETAIL-INDEX .\n035432     IF WS-TIN-DETAIL-INDEX NOT > WS-TIN-DETAIL-MAX\n035434         NEXT SENTENCE ELSE\n035436         GO TO Z-23-142-1-ELSE.\n035438     MOVE RMDRPT-REC-3 TO WS-TIN-DET-LINE-3 (WS-TIN-DETAIL-INDEX).\n035440 Z-23-142-1-ELSE.\n035442     GO TO Z-23-140-ENDIF.\n035444 Z-23-140-1-ELSE.\n035446     COMPUTE Z-LINES-HOLD = 1.\n035448     COMPUTE Z-LINES = 1.\n035450     IF Z-RPT-1-TRAP > ZERO\n035452         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n035454     IF Z-LINES > Z-RPT-1-TRAP\n035456       IF Z-RPTINFO1-INBLOCK = ZERO\n035458         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n035460         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n035462         COMPUTE Z-LINES = 1.\n035464     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n035466     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n035468     MOVE RMDRPT-REC-3 TO Z-RPT-1-BUFFER.\n035470     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n035472 Z-23-140-ENDIF.\n035474 Z-23-139-1-ELSE.\n035476     MOVE HOLD-TDAC-CUST TO RMDRPT-CUST-3.\n035478     MOVE SPACES TO RMDRPT-REC-4.\n035480     MOVE WS-RMDRPT-DS-METH TO RMDRPT-DS-METH-4.\n035482     IF ( WS-MULTI-DISTR = 2 ) AND ( SPECS-RMD-OVERRIDE = \"Y\" )   \n035484         AND ( TDB-TDAD-RMD-OVERRIDE = 0 )\n035486         NEXT SENTENCE ELSE\n035488         GO TO Z-23-148-1-ELSE.\n035490     MOVE \"MULTIPLE DIST - ADJUST DIST AMT MANUALLY\" TO           \n035492         RMDRPT-REMARK-4.\n035494 Z-23-148-1-ELSE.\n035496     IF ( NOT Z-SW3 )\n035498         NEXT SENTENCE ELSE\n035500         GO TO Z-23-150-1-ELSE.\n035502     IF ( SPECS-COMB-AUTO-RMD-ADJUST = \"Y\" )\n035504         NEXT SENTENCE ELSE\n035506         GO TO Z-23-151-1-ELSE.\n035508     IF WS-TIN-DETAIL-INDEX NOT > WS-TIN-DETAIL-MAX\n035510         NEXT SENTENCE ELSE\n035512         GO TO Z-23-152-1-ELSE.\n035514     MOVE RMDRPT-REC-4 TO WS-TIN-DET-LINE-4 (WS-TIN-DETAIL-INDEX).\n035516 Z-23-152-1-ELSE.\n035518     GO TO Z-23-151-ENDIF.\n035520 Z-23-151-1-ELSE.\n035522     COMPUTE Z-LINES-HOLD = 1.\n035524     COMPUTE Z-LINES = 1.\n035526     IF Z-RPT-1-TRAP > ZERO\n035528         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n035530     IF Z-LINES > Z-RPT-1-TRAP\n035532       IF Z-RPTINFO1-INBLOCK = ZERO\n035534         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n035536         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n035538         COMPUTE Z-LINES = 1.\n035540     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n035542     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n035544     MOVE RMDRPT-REC-4 TO Z-RPT-1-BUFFER.\n035546     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n035548 Z-23-151-ENDIF.\n035550 Z-23-150-1-ELSE.\n035552 Z-23-123-ENDIF.\n035554********* ADD WHEN\n035556     IF ( WS-MULTI-DISTR = 1 ) OR ( WS-DSREC-FLAG = 0 )\n035558        NEXT SENTENCE\n035560     ELSE\n035562        GO TO Z-23-155-ADD-SKIP.\n035564     ADD 1 TO RMD-COUNT .\n035566 Z-23-155-ADD-SKIP.\n035568 Z-23-109-ENDIF.\n035570 Z-23-END.\n035572     IF Z-EDIT-ERROR\n035574         GO TO Z-23-XIT.\n035576 Z-23-SKIP.\n035578     IF Z-EXIT-LEVEL NOT < 0\n035580         MOVE 0 TO Z-EXIT-CODE\n035582         MOVE 9999 TO Z-EXIT-LEVEL.\n035584 Z-23-XIT.\n035586     EXIT.\n035588*\n035590*****************************************************************\n035592*    PROCEDURE CLOSE-FM-FILE-RPT\n035594*****************************************************************\n035596 Z-6-PROCEDURE.\n035598*\n035600     MOVE 0 TO Z-EXIT-CODE.\n035602     MOVE 9999 TO Z-EXIT-LEVEL.\n035604     IF ( WS-MDRPT-OPEN > 0 ) OR ( WS-MDRPT2-OPEN > 0 )\n035606         NEXT SENTENCE ELSE\n035608         GO TO Z-6-1-1-ELSE.\n035610     MOVE SPACES TO HEADER-LINE2-160\n035612       , HEADER-LINE3-160\n035614       , HEADER-LINE4-160\n035616       , HEADER-LINE5-160.\n035618     MOVE 1 TO HDR-CTL.\n035620     IF WS-MDRPT-OPEN > 0\n035622         NEXT SENTENCE ELSE\n035624         GO TO Z-6-4-1-ELSE.\n035626     IF Z-RPTINFO1-INBLOCK = ZERO\n035628       PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT.\n035630     MOVE 0 TO PRT-FICHE-FILE-STATUS.\n035632************ PERFORM CLOSE-PRT-FILE\n035634     PERFORM Z-22-PROCEDURE THRU Z-22-XIT.\n035636     IF  Z-EXIT-EDITEXIT\n035638         GO TO Z-6-XIT.\n035640     IF  Z-DMS2-ABORT-FLAG = 1\n035642         GO TO Z-6-XIT.\n035644     IF  Z-EXIT-LEVEL < 0\n035646         GO TO Z-6-END.\n035648*\n035650 Z-6-4-1-ELSE.\n035652     IF WS-MDRPT2-OPEN > 0\n035654         NEXT SENTENCE ELSE\n035656         GO TO Z-6-8-1-ELSE.\n035658     IF Z-RPTINFO2-INBLOCK = ZERO\n035660       PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT.\n035662     MOVE 1 TO PRT-FICHE-FILE-STATUS.\n035664************ PERFORM CLOSE-PRT-FILE\n035666     PERFORM Z-22-PROCEDURE THRU Z-22-XIT.\n035668     IF  Z-EXIT-EDITEXIT\n035670         GO TO Z-6-XIT.\n035672     IF  Z-DMS2-ABORT-FLAG = 1\n035674         GO TO Z-6-XIT.\n035676     IF  Z-EXIT-LEVEL < 0\n035678         GO TO Z-6-END.\n035680*\n035682 Z-6-8-1-ELSE.\n035684     MOVE 0 TO WS-MDRPT-OPEN\n035686       , WS-MDRPT2-OPEN.\n035688 Z-6-1-1-ELSE.\n035690     IF ( WS-DSTFM-OPEN > 0 ) AND ( WS-BANK-OPT = 1 )\n035692         NEXT SENTENCE ELSE\n035694         GO TO Z-6-13-1-ELSE.\n035696     MOVE 0 TO WS-DSTFM-OPEN.\n035698*\n035700***********  CLOSE OF FILE DST-FILE-MAINT WITH CRUNCH\n035702*\n035704     IF Z-FLINFO5-OPEN NOT = 0\n035706         CLOSE DST-FILE-MAINT WITH CRUNCH\n035708         MOVE 0 TO Z-FLINFO5-OPEN\n035710         MOVE 0 TO Z-FLINFO5-RS-OPEN.\n035712     MOVE 1 TO WS-FM-OPS-DISP.\n035714 Z-6-13-1-ELSE.\n035716 Z-6-END.\n035718     IF Z-EDIT-ERROR\n035720         GO TO Z-6-XIT.\n035722 Z-6-SKIP.\n035724     IF Z-EXIT-LEVEL NOT < 0\n035726         MOVE 0 TO Z-EXIT-CODE\n035728         MOVE 9999 TO Z-EXIT-LEVEL.\n035730 Z-6-XIT.\n035732     EXIT.\n035734*\n035736*****************************************************************\n035738*    PROCEDURE GET-BANK-INFO\n035740*****************************************************************\n035742 Z-4-PROCEDURE.\n035744*\n035746     MOVE ZERO TO Z-FLINFO10-PRES.\n035748     MOVE 6 TO Z-FLINFO10-LAST-SEQ.\n035750     MOVE ZERO TO Z-FLINFO10-SOME.\n035752 Z-4-1-READ.\n035754     FIND TDAPCR OF LDBTDADB VIA TDAPCRSET OF TDAPCR OF LDBTDADB\n035756     AT TDAPC-APPL = \"TDA\" AND\n035758        TDAPC-BANK = PROC-BANK AND\n035760        TDAPC-TYPE = 0 AND\n035762        TDAPC-RPT-NBR = 999\n035764         ON EXCEPTION\n035766         MOVE 6 TO Z-DMS-EXCEPT-SEQ\n035768         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n035770             GO TO Z-4-1-XIT\n035772         ELSE\n035774             MOVE \"TDAPCRSET OF TDAPCR OF LDBTDADB\" TO            \n035776                 Z-DMS-EXCEPT-STR\n035778             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n035780             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n035782\n035784 Z-4-1-PRESENT.\n035786*\n035788     MOVE 1 TO Z-FLINFO10-SOME.\n035790     MOVE 1 TO Z-FLINFO10-PRES.\n035792     GO TO Z-4-1-CONT.\n035794 Z-4-1-XIT.\n035796 Z-4-1-CONT.\n035798     IF Z-FLINFO10-ABSENT\n035800         NEXT SENTENCE ELSE\n035802         GO TO Z-4-2-1-ELSE.\n035804     MOVE \"NO PRINT CONTROL RECORD FOR BANK \" TO Z-DISP-FIELD-1-1.\n035806     MOVE PROC-BANK TO Z-DISP-FIELD-1-2.\n035808     DISPLAY Z-DISP-FORMAT-1.\n035810 Z-4-2-1-ELSE.\n035812     MOVE TDAPC-APPL OF TDAPCR TO HOLD-TDAPC-APPL OF HOLD-TDAPCR.\n035814     MOVE TDAPC-TYPE OF TDAPCR TO HOLD-TDAPC-TYPE OF HOLD-TDAPCR.\n035816     MOVE TDAPC-BANK OF TDAPCR TO HOLD-TDAPC-BANK OF HOLD-TDAPCR.\n035818     MOVE TDAPC-RPT-NBR OF TDAPCR TO HOLD-TDAPC-RPT-NBR OF        \n035820         HOLD-TDAPCR.\n035822     MOVE TDAPC-CSI-ONLY OF TDAPCR TO HOLD-TDAPC-CSI-ONLY OF      \n035824         HOLD-TDAPCR.\n035826     MOVE TDAPC-RPT-DESC OF TDAPCR TO HOLD-TDAPC-RPT-DESC OF      \n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 502 lines from 17408 to 17909.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 36,
  "total_chunks": 55,
  "start_line": 17408,
  "end_line": 17909,
  "line_count": 502
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
- Source code length: 27064 characters

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
CHUNK 36 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 17408 to 17909 (502 lines)
Chunk Tokens (estimated): ~8,084
Actual Input Tokens: 9,490 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 17408-17909 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 36 of 55 chunks
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
      The source code below is only CHUNK 36 of 55.


=============================================================================
CHUNK 36 SOURCE CODE (Lines 17408-17909)
=============================================================================

```cobol
034824 Z-23-78-1-ELSE.
034826     IF WS-DSREC-FLAG = 1
034828         NEXT SENTENCE ELSE
034830         GO TO Z-23-81-1-ELSE.
034832     IF TDB-TDAD-INTEREST = 1
034834         NEXT SENTENCE ELSE
034836         GO TO Z-23-82-1-ELSE.
034838     MOVE "I" TO RMDRPT-DS-FREQ-3
034840       , WS-RMDRPT-DS-FREQ.
034842     MOVE ZEROS TO RMDRPT-OLD-DS-AMT-3
034844       , RMDRPT-NEW-DS-AMT-3
034846       , RMDRPT-DS-NTRVL-3
034848       , WS-RMDRPT-OLD-DS-AMT
034850       , WS-RMDRPT-DS-NTRVL
034852       , RMDRPT2-OLD-DS-AMT-3
034854       , RMDRPT2-NEW-DS-AMT-3.
034856     MOVE SPACES TO RMDRPT-WH-MSG-4.
034858     GO TO Z-23-82-ENDIF.
034860 Z-23-82-1-ELSE.
034862     MOVE SPACES TO RMDRPT-DS-METH-4
034864       , WS-RMDRPT-DS-METH.
034866     IF TDB-TDAD-DISP-CD = 1
034868         NEXT SENTENCE
034870     ELSE
034872         GO TO Z-23-87-END-MOVE.
034874     MOVE "CHK" TO RMDRPT-DS-METH-4
034876       , WS-RMDRPT-DS-METH.
034878 Z-23-87-END-MOVE.
034880     IF TDB-TDAD-DISP-CD = 2
034882         NEXT SENTENCE
034884     ELSE
034886         GO TO Z-23-88-END-MOVE.
034888     MOVE "DDA" TO RMDRPT-DS-METH-4
034890       , WS-RMDRPT-DS-METH.
034892 Z-23-88-END-MOVE.
034894     IF TDB-TDAD-DISP-CD = 3
034896         NEXT SENTENCE
034898     ELSE
034900         GO TO Z-23-89-END-MOVE.
034902     MOVE "SAV" TO RMDRPT-DS-METH-4
034904       , WS-RMDRPT-DS-METH.
034906 Z-23-89-END-MOVE.
034908     IF TDB-TDAD-DISP-CD = 4
034910         NEXT SENTENCE
034912     ELSE
034914         GO TO Z-23-90-END-MOVE.
034916     MOVE "LIST" TO RMDRPT-DS-METH-4
034918       , WS-RMDRPT-DS-METH.
034920 Z-23-90-END-MOVE.
034922     IF TDB-TDAD-DISP-CD = 5
034924         NEXT SENTENCE
034926     ELSE
034928         GO TO Z-23-91-END-MOVE.
034930     MOVE "COD" TO RMDRPT-DS-METH-4
034932       , WS-RMDRPT-DS-METH.
034934 Z-23-91-END-MOVE.
034936     IF TDB-TDAD-DISP-CD = 9
034938         NEXT SENTENCE
034940     ELSE
034942         GO TO Z-23-92-END-MOVE.
034944     MOVE "MAN" TO RMDRPT-DS-METH-4
034946       , WS-RMDRPT-DS-METH.
034948 Z-23-92-END-MOVE.
034950     MOVE TDB-TDAD-DS-NTRVL TO RMDRPT-DS-NTRVL-3
034952       , WS-RMDRPT-DS-NTRVL.
034954     MOVE TDB-TDAD-DS-AMT TO RMDRPT-OLD-DS-AMT-3
034956       , RMDRPT2-OLD-DS-AMT-3
034958       , WS-RMDRPT-OLD-DS-AMT.
034960     IF TDB-TDAD-DS-FREQ = 2
034962         NEXT SENTENCE ELSE
034964         GO TO Z-23-95-1-ELSE.
034966     MOVE "M" TO RMDRPT-DS-FREQ-3
034968       , WS-RMDRPT-DS-FREQ.
034970     COMPUTE WS-NEW-DS-AMT ROUNDED = ( ( WS-MD-AMT / 12 ) *       
034972         TDB-TDAD-DS-NTRVL ) .
034974
034976     GO TO Z-23-95-ENDIF.
034978 Z-23-95-1-ELSE.
034980     IF TDB-TDAD-DS-FREQ = 1
034982         NEXT SENTENCE ELSE
034984         GO TO Z-23-95-2-ELSE.
034986     MOVE "D" TO RMDRPT-DS-FREQ-3
034988       , WS-RMDRPT-DS-FREQ.
034990     COMPUTE WS-NEW-DS-AMT ROUNDED = ( ( WS-MD-AMT / 365 ) *      
034992         TDB-TDAD-DS-NTRVL ) .
034994
034996     GO TO Z-23-95-ENDIF.
034998 Z-23-95-2-ELSE.
035000     IF TDB-TDAD-DS-FREQ = 9
035002         NEXT SENTENCE ELSE
035004         GO TO Z-23-95-3-ELSE.
035006     MOVE "ONCE  " TO RMDRPT-DIST-FREQ-3.
035008     COMPUTE WS-NEW-DS-AMT = WS-MD-AMT .
035010
035012 Z-23-95-3-ELSE.
035014 Z-23-95-ENDIF.
035016     IF ( WS-NEW-DS-AMT < TDB-TDAD-WHLD-AMT ) AND (               
035018         TDB-TDAD-WTHLD-CD = 0 )
035020         NEXT SENTENCE ELSE
035022         GO TO Z-23-102-1-ELSE.
035024     MOVE "W/H > DIST" TO RMDRPT-WH-MSG-4.
035026     GO TO Z-23-102-ENDIF.
035028 Z-23-102-1-ELSE.
035030     MOVE SPACES TO RMDRPT-WH-MSG-4.
035032 Z-23-102-ENDIF.
035034     MOVE WS-NEW-DS-AMT TO RMDRPT-NEW-DS-AMT-3
035036       , RMDRPT2-NEW-DS-AMT-3.
035038 Z-23-82-ENDIF.
035040     GO TO Z-23-81-ENDIF.
035042 Z-23-81-1-ELSE.
035044     MOVE "NONE" TO RMDRPT-DS-NTRVL-3
035046       , WS-RMDRPT-DS-NTRVL.
035048     MOVE SPACE TO RMDRPT-DS-FREQ-3
035050       , WS-RMDRPT-DS-FREQ.
035052     MOVE ZEROS TO RMDRPT-OLD-DS-AMT-3
035054       , RMDRPT-NEW-DS-AMT-3
035056       , WS-RMDRPT-OLD-DS-AMT
035058       , RMDRPT2-OLD-DS-AMT-3
035060       , RMDRPT2-NEW-DS-AMT-3.
035062 Z-23-81-ENDIF.
035064     IF ( TDB-TDAA-INHERIT-IRA > 0 ) AND ( NOT Z-SW3 )
035066         NEXT SENTENCE ELSE
035068         GO TO Z-23-109-1-ELSE.
035070     MOVE 1 TO WS-INHERIT-IRA-ON-TIN.
035072     MOVE RMDRPT-CUST-3 OF RMDRPT-REC-3 TO RMDRPT2-CUST-3 OF      
035074         RMDRPT2-REC-3.
035076     MOVE RMDRPT-ACCT-3 OF RMDRPT-REC-3 TO RMDRPT2-ACCT-3 OF      
035078         RMDRPT2-REC-3.
035080     MOVE RMDRPT-BIRTH-DT-3 OF RMDRPT-REC-3 TO RMDRPT2-BIRTH-DT-3 
035082         OF RMDRPT2-REC-3.
035084     MOVE RMDRPT-AGE-DATE-3 OF RMDRPT-REC-3 TO RMDRPT2-AGE-DATE-3 
035086         OF RMDRPT2-REC-3.
035088     MOVE RMDRPT-BEG-DATE-3 OF RMDRPT-REC-3 TO RMDRPT2-BEG-DATE-3 
035090         OF RMDRPT2-REC-3.
035092     MOVE RMDRPT-CUR-BAL-IND-3 OF RMDRPT-REC-3 TO                 
035094         RMDRPT2-CUR-BAL-IND-3 OF RMDRPT2-REC-3.
035096     MOVE RMDRPT-SLASH-3 OF RMDRPT-REC-3 TO RMDRPT2-SLASH-3 OF    
035098         RMDRPT2-REC-3.
035100     MOVE RMDRPT-TBL-3 OF RMDRPT-REC-3 TO RMDRPT2-TBL-3 OF        
035102         RMDRPT2-REC-3.
035104     MOVE RMDRPT-RMD-MAN-CALC-3 OF RMDRPT-REC-3 TO                
035106         RMDRPT2-RMD-MAN-CALC-3 OF RMDRPT2-REC-3.
035108     MOVE RMDRPT-DS-NTRVL-3 OF RMDRPT-REC-3 TO RMDRPT2-DS-NTRVL-3 
035110         OF RMDRPT2-REC-3.
035112     MOVE RMDRPT-DS-FREQ-3 OF RMDRPT-REC-3 TO RMDRPT2-DS-FREQ-3   
035114         OF RMDRPT2-REC-3.
035116     IF TDB-TDAA-BNF-DEATH-DT > 0
035118         NEXT SENTENCE ELSE
035120         GO TO Z-23-112-1-ELSE.
035122     MOVE TDB-TDAA-BNF-DEATH-DT TO Z-DATE2-FORMAT-9.
035124*
035126     PERFORM Z-DATE-INITIALIZE-REGS
035128         THRU Z-DATE-INITIALIZE-REGS-EXIT.
035130     MOVE Z-DATE2-MM TO Z-DATE6-MM.
035132     MOVE "/" TO Z-DATE6-CH1.
035134     MOVE Z-DATE2-DD TO Z-DATE6-DD.
035136     MOVE "/" TO Z-DATE6-CH2.
035138     MOVE Z-DATE2-CC TO Z-DATE6-CC.
035140     MOVE Z-DATE2-YY TO Z-DATE6-YY.
035142     MOVE Z-DATE6-FORMAT TO RMDRPT2-DTH-DATE-3.
035144     GO TO Z-23-112-ENDIF.
035146 Z-23-112-1-ELSE.
035148     MOVE "   NONE   " TO RMDRPT2-DTH-DATE-3.
035150 Z-23-112-ENDIF.
035152     COMPUTE Z-LINES-HOLD = 1.
035154     COMPUTE Z-LINES = 1.
035156     IF Z-RPT-2-TRAP > ZERO
035158         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.
035160     IF Z-LINES > Z-RPT-2-TRAP
035162       IF Z-RPTINFO2-INBLOCK = ZERO
035164         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1
035166         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT
035168         COMPUTE Z-LINES = 1.
035170     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).
035172     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).
035174     MOVE RMDRPT2-REC-3 TO Z-RPT-2-BUFFER.
035176     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.
035178     MOVE RMDRPT-NAME-4 OF RMDRPT-REC-4 TO RMDRPT2-NAME-4 OF      
035180         RMDRPT2-REC-4.
035182     MOVE RMDRPT-REMARK-4 OF RMDRPT-REC-4 TO RMDRPT2-REMARK-4 OF  
035184         RMDRPT2-REC-4.
035186     MOVE RMDRPT-REMARK2-4 OF RMDRPT-REC-4 TO RMDRPT2-REMARK2-4   
035188         OF RMDRPT2-REC-4.
035190     MOVE RMDRPT-DS-METH-4 OF RMDRPT-REC-4 TO RMDRPT2-DS-METH-4   
035192         OF RMDRPT2-REC-4.
035194     MOVE RMDRPT-WH-MSG-4 OF RMDRPT-REC-4 TO RMDRPT2-WH-MSG-4 OF  
035196         RMDRPT2-REC-4.
035198     COMPUTE Z-LINES-HOLD = 1.
035200     COMPUTE Z-LINES = 1.
035202     IF Z-RPT-2-TRAP > ZERO
035204         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.
035206     IF Z-LINES > Z-RPT-2-TRAP
035208       IF Z-RPTINFO2-INBLOCK = ZERO
035210         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1
035212         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT
035214         COMPUTE Z-LINES = 1.
035216     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).
035218     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).
035220     MOVE RMDRPT2-REC-4 TO Z-RPT-2-BUFFER.
035222     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.
035224     IF RMDRPT-NAME-8 NOT = SPACES
035226         NEXT SENTENCE ELSE
035228         GO TO Z-23-118-1-ELSE.
035230     MOVE RMDRPT-NAME-8 OF RMDRPT-REC-8 TO RMDRPT2-NAME-8 OF      
035232         RMDRPT2-REC-8.
035234     COMPUTE Z-LINES-HOLD = 1.
035236     COMPUTE Z-LINES = 1.
035238     IF Z-RPT-2-TRAP > ZERO
035240         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.
035242     IF Z-LINES > Z-RPT-2-TRAP
035244       IF Z-RPTINFO2-INBLOCK = ZERO
035246         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1
035248         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT
035250         COMPUTE Z-LINES = 1.
035252     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).
035254     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).
035256     MOVE RMDRPT2-REC-8 TO Z-RPT-2-BUFFER.
035258     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.
035260 Z-23-118-1-ELSE.
035262********* ADD WHEN
035264     IF ( WS-MULTI-DISTR = 1 ) OR ( WS-DSREC-FLAG = 0 )
035266        NEXT SENTENCE
035268     ELSE
035270        GO TO Z-23-121-ADD-SKIP.
035272     ADD 1 TO RMD-COUNT-INHERIT .
035274 Z-23-121-ADD-SKIP.
035276     GO TO Z-23-109-ENDIF.
035278 Z-23-109-1-ELSE.
035280     MOVE 1 TO WS-NON-INHERIT-IRA-ON-TIN.
035282     IF ( ( WS-MULTI-DISTR = 1 ) OR ( WS-DSREC-FLAG = 0 ) ) AND ( 
035284         NOT Z-SW3 )
035286         NEXT SENTENCE ELSE
035288         GO TO Z-23-123-1-ELSE.
035290     IF ( SPECS-COMB-AUTO-RMD-ADJUST = "Y" )
035292         NEXT SENTENCE ELSE
035294         GO TO Z-23-124-1-ELSE.
035296     ADD 1 TO WS-TIN-DETAIL-INDEX .
035298     IF WS-TIN-DETAIL-INDEX NOT > WS-TIN-DETAIL-MAX
035300         NEXT SENTENCE ELSE
035302         GO TO Z-23-126-1-ELSE.
035304     MOVE RMDRPT-REC-3 TO WS-TIN-DET-LINE-3 (WS-TIN-DETAIL-INDEX).
035306     MOVE RMDRPT-REC-4 TO WS-TIN-DET-LINE-4 (WS-TIN-DETAIL-INDEX).
035308     MOVE RMDRPT-REC-8 TO WS-TIN-DET-LINE-8 (WS-TIN-DETAIL-INDEX).
035310 Z-23-126-1-ELSE.
035312     GO TO Z-23-124-ENDIF.
035314 Z-23-124-1-ELSE.
035316     COMPUTE Z-LINES-HOLD = 1.
035318     COMPUTE Z-LINES = 1.
035320     IF Z-RPT-1-TRAP > ZERO
035322         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
035324     IF Z-LINES > Z-RPT-1-TRAP
035326       IF Z-RPTINFO1-INBLOCK = ZERO
035328         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
035330         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
035332         COMPUTE Z-LINES = 1.
035334     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
035336     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
035338     MOVE RMDRPT-REC-3 TO Z-RPT-1-BUFFER.
035340     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
035342     COMPUTE Z-LINES-HOLD = 1.
035344     COMPUTE Z-LINES = 1.
035346     IF Z-RPT-1-TRAP > ZERO
035348         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
035350     IF Z-LINES > Z-RPT-1-TRAP
035352       IF Z-RPTINFO1-INBLOCK = ZERO
035354         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
035356         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
035358         COMPUTE Z-LINES = 1.
035360     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
035362     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
035364     MOVE RMDRPT-REC-4 TO Z-RPT-1-BUFFER.
035366     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
035368     IF RMDRPT-NAME-8 NOT = SPACES
035370         NEXT SENTENCE ELSE
035372         GO TO Z-23-132-1-ELSE.
035374     COMPUTE Z-LINES-HOLD = 1.
035376     COMPUTE Z-LINES = 1.
035378     IF Z-RPT-1-TRAP > ZERO
035380         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
035382     IF Z-LINES > Z-RPT-1-TRAP
035384       IF Z-RPTINFO1-INBLOCK = ZERO
035386         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
035388         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
035390         COMPUTE Z-LINES = 1.
035392     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
035394     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
035396     MOVE RMDRPT-REC-8 TO Z-RPT-1-BUFFER.
035398     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
035400 Z-23-132-1-ELSE.
035402 Z-23-124-ENDIF.
035404     GO TO Z-23-123-ENDIF.
035406 Z-23-123-1-ELSE.
035408     MOVE RMDRPT-CUST-3 TO HOLD-TDAC-CUST.
035410     MOVE SPACES TO RMDRPT-REC-3.
035412     MOVE WS-RMDRPT-DS-FREQ TO RMDRPT-DS-FREQ-3.
035414     MOVE WS-RMDRPT-DS-NTRVL TO RMDRPT-DS-NTRVL-3.
035416     MOVE WS-RMDRPT-OLD-DS-AMT TO RMDRPT-OLD-DS-AMT-3.
035418     IF ( NOT Z-SW3 )
035420         NEXT SENTENCE ELSE
035422         GO TO Z-23-139-1-ELSE.
035424     IF ( SPECS-COMB-AUTO-RMD-ADJUST = "Y" )
035426         NEXT SENTENCE ELSE
035428         GO TO Z-23-140-1-ELSE.
035430     ADD 1 TO WS-TIN-DETAIL-INDEX .
035432     IF WS-TIN-DETAIL-INDEX NOT > WS-TIN-DETAIL-MAX
035434         NEXT SENTENCE ELSE
035436         GO TO Z-23-142-1-ELSE.
035438     MOVE RMDRPT-REC-3 TO WS-TIN-DET-LINE-3 (WS-TIN-DETAIL-INDEX).
035440 Z-23-142-1-ELSE.
035442     GO TO Z-23-140-ENDIF.
035444 Z-23-140-1-ELSE.
035446     COMPUTE Z-LINES-HOLD = 1.
035448     COMPUTE Z-LINES = 1.
035450     IF Z-RPT-1-TRAP > ZERO
035452         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
035454     IF Z-LINES > Z-RPT-1-TRAP
035456       IF Z-RPTINFO1-INBLOCK = ZERO
035458         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
035460         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
035462         COMPUTE Z-LINES = 1.
035464     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
035466     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
035468     MOVE RMDRPT-REC-3 TO Z-RPT-1-BUFFER.
035470     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
035472 Z-23-140-ENDIF.
035474 Z-23-139-1-ELSE.
035476     MOVE HOLD-TDAC-CUST TO RMDRPT-CUST-3.
035478     MOVE SPACES TO RMDRPT-REC-4.
035480     MOVE WS-RMDRPT-DS-METH TO RMDRPT-DS-METH-4.
035482     IF ( WS-MULTI-DISTR = 2 ) AND ( SPECS-RMD-OVERRIDE = "Y" )   
035484         AND ( TDB-TDAD-RMD-OVERRIDE = 0 )
035486         NEXT SENTENCE ELSE
035488         GO TO Z-23-148-1-ELSE.
035490     MOVE "MULTIPLE DIST - ADJUST DIST AMT MANUALLY" TO           
035492         RMDRPT-REMARK-4.
035494 Z-23-148-1-ELSE.
035496     IF ( NOT Z-SW3 )
035498         NEXT SENTENCE ELSE
035500         GO TO Z-23-150-1-ELSE.
035502     IF ( SPECS-COMB-AUTO-RMD-ADJUST = "Y" )
035504         NEXT SENTENCE ELSE
035506         GO TO Z-23-151-1-ELSE.
035508     IF WS-TIN-DETAIL-INDEX NOT > WS-TIN-DETAIL-MAX
035510         NEXT SENTENCE ELSE
035512         GO TO Z-23-152-1-ELSE.
035514     MOVE RMDRPT-REC-4 TO WS-TIN-DET-LINE-4 (WS-TIN-DETAIL-INDEX).
035516 Z-23-152-1-ELSE.
035518     GO TO Z-23-151-ENDIF.
035520 Z-23-151-1-ELSE.
035522     COMPUTE Z-LINES-HOLD = 1.
035524     COMPUTE Z-LINES = 1.
035526     IF Z-RPT-1-TRAP > ZERO
035528         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
035530     IF Z-LINES > Z-RPT-1-TRAP
035532       IF Z-RPTINFO1-INBLOCK = ZERO
035534         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
035536         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
035538         COMPUTE Z-LINES = 1.
035540     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
035542     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
035544     MOVE RMDRPT-REC-4 TO Z-RPT-1-BUFFER.
035546     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
035548 Z-23-151-ENDIF.
035550 Z-23-150-1-ELSE.
035552 Z-23-123-ENDIF.
035554********* ADD WHEN
035556     IF ( WS-MULTI-DISTR = 1 ) OR ( WS-DSREC-FLAG = 0 )
035558        NEXT SENTENCE
035560     ELSE
035562        GO TO Z-23-155-ADD-SKIP.
035564     ADD 1 TO RMD-COUNT .
035566 Z-23-155-ADD-SKIP.
035568 Z-23-109-ENDIF.
035570 Z-23-END.
035572     IF Z-EDIT-ERROR
035574         GO TO Z-23-XIT.
035576 Z-23-SKIP.
035578     IF Z-EXIT-LEVEL NOT < 0
035580         MOVE 0 TO Z-EXIT-CODE
035582         MOVE 9999 TO Z-EXIT-LEVEL.
035584 Z-23-XIT.
035586     EXIT.
035588*
035590*****************************************************************
035592*    PROCEDURE CLOSE-FM-FILE-RPT
035594*****************************************************************
035596 Z-6-PROCEDURE.
035598*
035600     MOVE 0 TO Z-EXIT-CODE.
035602     MOVE 9999 TO Z-EXIT-LEVEL.
035604     IF ( WS-MDRPT-OPEN > 0 ) OR ( WS-MDRPT2-OPEN > 0 )
035606         NEXT SENTENCE ELSE
035608         GO TO Z-6-1-1-ELSE.
035610     MOVE SPACES TO HEADER-LINE2-160
035612       , HEADER-LINE3-160
035614       , HEADER-LINE4-160
035616       , HEADER-LINE5-160.
035618     MOVE 1 TO HDR-CTL.
035620     IF WS-MDRPT-OPEN > 0
035622         NEXT SENTENCE ELSE
035624         GO TO Z-6-4-1-ELSE.
035626     IF Z-RPTINFO1-INBLOCK = ZERO
035628       PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT.
035630     MOVE 0 TO PRT-FICHE-FILE-STATUS.
035632************ PERFORM CLOSE-PRT-FILE
035634     PERFORM Z-22-PROCEDURE THRU Z-22-XIT.
035636     IF  Z-EXIT-EDITEXIT
035638         GO TO Z-6-XIT.
035640     IF  Z-DMS2-ABORT-FLAG = 1
035642         GO TO Z-6-XIT.
035644     IF  Z-EXIT-LEVEL < 0
035646         GO TO Z-6-END.
035648*
035650 Z-6-4-1-ELSE.
035652     IF WS-MDRPT2-OPEN > 0
035654         NEXT SENTENCE ELSE
035656         GO TO Z-6-8-1-ELSE.
035658     IF Z-RPTINFO2-INBLOCK = ZERO
035660       PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT.
035662     MOVE 1 TO PRT-FICHE-FILE-STATUS.
035664************ PERFORM CLOSE-PRT-FILE
035666     PERFORM Z-22-PROCEDURE THRU Z-22-XIT.
035668     IF  Z-EXIT-EDITEXIT
035670         GO TO Z-6-XIT.
035672     IF  Z-DMS2-ABORT-FLAG = 1
035674         GO TO Z-6-XIT.
035676     IF  Z-EXIT-LEVEL < 0
035678         GO TO Z-6-END.
035680*
035682 Z-6-8-1-ELSE.
035684     MOVE 0 TO WS-MDRPT-OPEN
035686       , WS-MDRPT2-OPEN.
035688 Z-6-1-1-ELSE.
035690     IF ( WS-DSTFM-OPEN > 0 ) AND ( WS-BANK-OPT = 1 )
035692         NEXT SENTENCE ELSE
035694         GO TO Z-6-13-1-ELSE.
035696     MOVE 0 TO WS-DSTFM-OPEN.
035698*
035700***********  CLOSE OF FILE DST-FILE-MAINT WITH CRUNCH
035702*
035704     IF Z-FLINFO5-OPEN NOT = 0
035706         CLOSE DST-FILE-MAINT WITH CRUNCH
035708         MOVE 0 TO Z-FLINFO5-OPEN
035710         MOVE 0 TO Z-FLINFO5-RS-OPEN.
035712     MOVE 1 TO WS-FM-OPS-DISP.
035714 Z-6-13-1-ELSE.
035716 Z-6-END.
035718     IF Z-EDIT-ERROR
035720         GO TO Z-6-XIT.
035722 Z-6-SKIP.
035724     IF Z-EXIT-LEVEL NOT < 0
035726         MOVE 0 TO Z-EXIT-CODE
035728         MOVE 9999 TO Z-EXIT-LEVEL.
035730 Z-6-XIT.
035732     EXIT.
035734*
035736*****************************************************************
035738*    PROCEDURE GET-BANK-INFO
035740*****************************************************************
035742 Z-4-PROCEDURE.
035744*
035746     MOVE ZERO TO Z-FLINFO10-PRES.
035748     MOVE 6 TO Z-FLINFO10-LAST-SEQ.
035750     MOVE ZERO TO Z-FLINFO10-SOME.
035752 Z-4-1-READ.
035754     FIND TDAPCR OF LDBTDADB VIA TDAPCRSET OF TDAPCR OF LDBTDADB
035756     AT TDAPC-APPL = "TDA" AND
035758        TDAPC-BANK = PROC-BANK AND
035760        TDAPC-TYPE = 0 AND
035762        TDAPC-RPT-NBR = 999
035764         ON EXCEPTION
035766         MOVE 6 TO Z-DMS-EXCEPT-SEQ
035768         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
035770             GO TO Z-4-1-XIT
035772         ELSE
035774             MOVE "TDAPCRSET OF TDAPCR OF LDBTDADB" TO            
035776                 Z-DMS-EXCEPT-STR
035778             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
035780             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
035782
035784 Z-4-1-PRESENT.
035786*
035788     MOVE 1 TO Z-FLINFO10-SOME.
035790     MOVE 1 TO Z-FLINFO10-PRES.
035792     GO TO Z-4-1-CONT.
035794 Z-4-1-XIT.
035796 Z-4-1-CONT.
035798     IF Z-FLINFO10-ABSENT
035800         NEXT SENTENCE ELSE
035802         GO TO Z-4-2-1-ELSE.
035804     MOVE "NO PRINT CONTROL RECORD FOR BANK " TO Z-DISP-FIELD-1-1.
035806     MOVE PROC-BANK TO Z-DISP-FIELD-1-2.
035808     DISPLAY Z-DISP-FORMAT-1.
035810 Z-4-2-1-ELSE.
035812     MOVE TDAPC-APPL OF TDAPCR TO HOLD-TDAPC-APPL OF HOLD-TDAPCR.
035814     MOVE TDAPC-TYPE OF TDAPCR TO HOLD-TDAPC-TYPE OF HOLD-TDAPCR.
035816     MOVE TDAPC-BANK OF TDAPCR TO HOLD-TDAPC-BANK OF HOLD-TDAPCR.
035818     MOVE TDAPC-RPT-NBR OF TDAPCR TO HOLD-TDAPC-RPT-NBR OF        
035820         HOLD-TDAPCR.
035822     MOVE TDAPC-CSI-ONLY OF TDAPCR TO HOLD-TDAPC-CSI-ONLY OF      
035824         HOLD-TDAPCR.
035826     MOVE TDAPC-RPT-DESC OF TDAPCR TO HOLD-TDAPC-RPT-DESC OF      
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 502 lines from 17408 to 17909.

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

