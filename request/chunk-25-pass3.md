# LLM Request Debug File
Generated: 2025-11-13T20:51:00.550555

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 25/55
- **Model**: gpt-4.1
- **Chunk Number**: 25
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~16,899 tokens
- **Total Input**: ~18,857 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 25/55" (ID: detailed-code-explanation)

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


**CHUNK 25 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 25 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 11443 to 12141 (699 lines)\nChunk Tokens (estimated): ~13,304\nActual Input Tokens: 14,710 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 11443-12141 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 25 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 25 of 55.\n\n\n=============================================================================\nCHUNK 25 SOURCE CODE (Lines 11443-12141)\n=============================================================================\n\n```cobol\n022894 01  WS-SCREEN-AREA.                                              \n022896**  The following data items are used within a single process.    \n022898**  None of this data will be tranfered to any other processes.   \n022900                                                                  \n022902     05  WS-HEADER                PIC X(23).                      \n022904     05  WS-TODAY                 PIC X(08).                      \n022906     05  WS-TIME                  PIC X(05).                      \n022908                                                                  \n022910     05  WS-POP-UP                PIC 9       VALUE ZERO.         \n022912     05  WS-MISC-EDIT-TRIG        PIC 9       VALUE ZERO.         \n022914                                                                  \n022916     05  WS-MAX-TDB-TABLE         PIC 99.                         \n022918     05  WS-FM-INDEX              PIC 9(04).                      \n022920     05  WS-VALID-FM              PIC 9.                          \n022922                                                                  \n022924     05  MAX-SUB                  PIC 9(04).                      \n022926     05  SUB                      PIC 9(04).                      \n022928     05  SUB-2                    PIC 9(04).                      \n022930     05  WS-DDN                   PIC 9(05).                      \n022932     05  WS-FIELD-NAME            PIC X(30).                      \n022934                                                                  \n022936     05  EXCLUDE-RAW-VALUE        PIC 9       VALUE 0.            \n022938     05  INCLUDE-RAW-VALUE        PIC 9       VALUE 1.            \n022940                                                                  \n022942                                                                  \n022944     05  WS-NEW-BNF-NBR           PIC 99.                         \n022946     05  WS-PRI-BNF-TOTAL         PIC 999.                        \n022948     05  WS-CONT-BNF-TOTAL        PIC 9999.                       \n022950                                                                  \n022952     05  WS-UPDATE-DISTR-RECORD   PIC 9       VALUE 0.            \n022954     05  WS-UPDATE-IRA-RECORD     PIC 9       VALUE 0.            \n022956     05  WS-UPDATE-CUST-RECORD    PIC 9       VALUE 0.            \n022958     05  WS-UPDATE-HOLD-RECORDS   PIC 9       VALUE 0.            \n022960     05  WS-RECALC-RUNNING-BAL    PIC 9       VALUE 0.            \n022962                                                                  \n022964     05  SPECS-MIN-PROC-DAYS      PIC 9     VALUE 4.              \n022966                                                                  \n022968**  These fields are used to determine proper processing date     \n022970**  from operations.  They are used in TDD-VERIFY-PROCESS-DATE.   \n022972     05  ENTER-DATE               PIC 9(6).                       \n022974     05  DISPLAY-DATE             PIC X(12).                      \n022976     05  NEXT-DATE                PIC 9(6).                       \n022978     05  WS-END-OF                PIC 9(1).                       \n022980     05  WS-RESPONSE              PIC X(1).                       \n022982                                                                  \n022984     05  WS-ADJUSTED-IND          PIC X(01) VALUE \" \".            \n022986         88  WS-ADJUSTED                    VALUE \"A\".            \n022988         88  WS-ADJUSTED-NEW                VALUE \"N\".            \n022990         88  WS-ADJUSTED-CURRENT            VALUE \"C\".            \n022992                                                                  \n022994     05  WS-RECORD-CHANGED-IND    PIC X(01) VALUE \"N\".            \n022996         88  WS-RECORD-CHANGED              VALUE \"Y\".            \n022998                                                                  \n023000     05  WS-DIRECTION-IND         PIC X(01) VALUE \" \".            \n023002         88  WS-FORWARD                     VALUE \"F\".            \n023004         88  WS-BACKWARD                    VALUE \"B\".            \n023006                                                                  \n023008     05  WS-RENEW-IND             PIC X(01) VALUE \" \".            \n023010         88  WS-RENEW                       VALUE \"R\".            \n023012         88  WS-NEW                         VALUE \"N\".            \n023014                                                                  \n023016     05  WS-ACTION-CODE-CONSTANTS.                                \n023018         10  WS-ACTION-ADD        PIC 99    VALUE 01.             \n023020         10  WS-ACTION-CHANGE     PIC 99    VALUE 02.             \n023022         10  WS-ACTION-DELETE     PIC 99    VALUE 03.             \n023024         10  WS-ACTION-CHG-KEY    PIC 99    VALUE 04.             \n023026                                                                  \n023028     05  WS-DATE                  PIC X(08).                      \n023030                                                                  \n023032     05  WS-CD-HOLD-DT            PIC 9(08).                      \n023034     05  WS-IRA-HOLD-DT           PIC 9(08).                      \n023036                                                                  \n023038     05  WS-DATE-CYMD.                                            \n023040         10  WS-DATE-CY           PIC 9(04).                      \n023042         10  WS-DATE-CY-R REDEFINES WS-DATE-CY.                   \n023044             15  WS-DATE-CC       PIC 99.                         \n023046             15  WS-DATE-YY       PIC 99.                         \n023048         10  WS-DATE-MD           PIC 9(04).                      \n023050         10  WS-DATE-MD-R REDEFINES WS-DATE-MD.                   \n023052             15  WS-DATE-MM       PIC 9(02).                      \n023054             15  WS-DATE-DD       PIC 9(02).                      \n023056     05  WS-DATE-CYMD-R REDEFINES WS-DATE-CYMD.                   \n023058         10  WS-DATE-C            PIC XX.                         \n023060         10  WS-DATE-YMD          PIC X(06).                      \n023062                                                                  \n023064     05  WS-TIME-HMST.                                            \n023066         10  WS-TIME-HMS.                                         \n023068             15  WS-TIME-HH       PIC 9(02).                      \n023070             15  WS-TIME-MM       PIC 9(02).                      \n023072             15  WS-TIME-SS       PIC 9(02).                      \n023074         10  WS-TIME-TT           PIC 9(02).                      \n023076                                                                  \n023078     05  WS-DAILY-PATTERN.                                        \n023080         10  WS-DLY-PATTERN    OCCURS 7 TIMES     PIC X(1).       \n023082                                                                  \n023084     05  DATE-DEFINES-FIELDS.                                     \n023086         10  FILLER               PIC 9(18)  VALUE ZEROES.        \n023088         10  FILLER               PIC 9(18)  VALUE ZEROES.        \n023090         10  FILLER               PIC 9(18)  VALUE ZEROES.        \n023092         10  FILLER               PIC 9(02)  VALUE ZEROES.        \n023094     05  DATE-DEFINES-FIELDS-R    REDEFINES DATE-DEFINES-FIELDS.  \n023096         10  DD-DT-CONV-DAYS      PIC 9(06).                      \n023098         10  DD-DT-CONV-MMM       PIC 9(03).                      \n023100         10  DD-DT-CONV-YY        PIC 9(02).                      \n023102         10  DD-DT-CONV-GEG       PIC 9(08).                      \n023104         10  DD-DT-CONV-JUL       PIC 9(07).                      \n023106         10  DD-DT-CONV-GEG-ERLY  PIC 9(08).                      \n023108         10  DD-DT-CONV-GEG-LATE  PIC 9(08).                      \n023110         10  DD-DT-CONV-JUL-ERLY  PIC 9(07).                      \n023112         10  DD-DT-CONV-JUL-LATE  PIC 9(07).                      \n023114     05  DD-DAY-OF-WEEK           PIC X(03)       VALUE SPACES.   \n023116                                                                  \n023118     05  WS-PRIOR-YEAR-CUTOFF     PIC 9(04)  VALUE 0430.          \n023120                                                                  \n023122     05  WS-SIZE                  PIC 9(2).                       \n023124     05  WS-OFFSET                PIC 9(2).                       \n023126                                                                  \n023128     05  WS-IN-STRING             PIC X(18).                      \n023130     05  WS-OUT-NUMERIC-X.                                        \n023132         10  WS-OUT-NUMERIC       PIC S9(18).                     \n023134                                                                  \n023136     05  WS-RATE.                                                 \n023138         10  WS-RATE-1-5-GRP.                                     \n023140             15  WS-RATE-1-5      PIC 99V999.                     \n023142             15  WS-RATE-6        PIC X(01).                      \n023144         10  WS-RATE-2-6-GRP REDEFINES WS-RATE-1-5-GRP.           \n023146             15  WS-RATE-1        PIC X(01).                      \n023148             15  WS-RATE-2-6      PIC 99V999.                     \n023150                                                                  \n023152     05  WS-RATE-KEY-FIELDS.                                      \n023154         10  WS-RATE-EFF-DATE     PIC 9(08).                      \n023156         10  WS-RATE-ADD-DATE     PIC 9(08).                      \n023158         10  WS-RATE-ADD-TIME     PIC 9(08).                      \n023160          10 WS-RATE-ACTION-CD    PIC X(01).                      \n023162         10  WS-RATE-TDAP-FUNC        PIC X(01).                  \n023164         10  WS-RATE-TDAP-PUB-ID      PIC X(08).                  \n023166         10  WS-RATE-TDAP-DATE        PIC 9(08).                  \n023168         10  WS-RATE-TDAP-DAYS        PIC 9(04).                  \n023170         10  WS-RATE-TDAP-MONTHS      PIC 9(04).                  \n023172         10  WS-RATE-TDAP-PERCENT     PIC 99V99.                  \n023174         10  WS-RATE-TDAP-AMOUNT      PIC 9(12)V99.               \n023176         10  WS-RATE-TDAP-USE-INT     PIC 9(01).                  \n023178         10  WS-RATE-TDAP-USE-RED     PIC 9(01).                  \n023180         10  WS-RATE-TDAP-USE-MONTH   PIC 9(01).                  \n023182         10  WS-RATE-TDAP-USE-DAY     PIC 9(01).                  \n023184         10  WS-RATE-TDAP-USE-AVL-INT PIC 9(01).                  \n023186         10  FILLER                   PIC X(27).                  \n023188                                                                  \n023190     05  WS-TDAPC-TYPE            PIC X(4).                       \n023192     05  WS-PCR-KEY-FIELDS.                                       \n023194         10  WS-PCR-PUB-ID        PIC X(08).                      \n023196         10  WS-PCR-LUPD-DT       PIC 9(08).                      \n023198         10  WS-PCR-LUPD-TM       PIC 9(06).                      \n023200         10  WS-PCR-RPT-FIELD     PIC X(40).                      \n023202                                                                  \n023204     05  WS-ADD-DATE              PIC 9(08).                      \n023206     05  WS-ADD-TIME              PIC 9(08).                      \n023208                                                                  \n023210     05  IRA-INDX                 PIC 99.                         \n023212     05  TOTL-INDX                PIC 99.                         \n023214                                                                  \n023216     05  WS-PER-RATIO             PIC 9(03)V9(12).                \n023218     05  WS-CMPD-PER-YR           PIC 9(03)V9(06).                \n023220     05  WS-BASE                  PIC 9(06)V9(12).                \n023222     05  WS-EXP                   PIC 9(06)V9(12).                \n023224                                                                  \n023226     05  DISPLAY-FIELDS.                                          \n023228         10  DISPLAY-AMT          PIC Z,ZZZ,ZZZ,ZZ9.99-.          \n023230         10  DISPLAY-RATE         PIC Z9.999-.                    \n023232         10  DISPLAY-YIELD        PIC Z9.999-.                    \n023234         10  DISPLAY-TIME         PIC XXXXXXXX.                   \n023236         10  DISPLAY-PUB-ID       PIC X(8).                       \n023238                                                                  \n023240     05  ACCT-WARNING   OCCURS 4 TIMES.                           \n023242         10  WARNING-DATE         PIC X(5).                       \n023244         10  FILLER               PIC X(1).                       \n023246         10  WARNING-DESC         PIC X(19).                      \n023248                                                                  \n023250     05  WS-TDAA-INTEREST-PAY.                                    \n023252         10  WS-TDAA-LST-PAY-BAL  PIC S9(12)V99.                  \n023254         10  WS-TDAA-LST-YIELD    PIC S9(12)V9(06).               \n023256         10  WS-YIELD             PIC S9(06)V9999.                \n023258*$$SET OMIT = TDASQLFLAG                                          \n023260         10  WS-ACCR-PER-ACTV     PIC S9(12)V9(06).               \n023262         10  WS-ACCR-PER-INT      PIC S9(12)V9(06).               \n023264*$$POP OMIT                                                       \n023266*$$SET OMIT = NOT TDASQLFLAG                                      \n023268*         10  WS-ACCR-PER-ACTV     PIC S9(08)V9(08).              \n023270*         10  WS-ACCR-PER-INT      PIC S9(08)V9(08).              \n023272*$$POP OMIT                                                       \n023274         10  WS-ANTIC-INT         PIC S9(12)V99.                  \n023276         10  WS-ANTIC-INT-V4      PIC S9(12)V9(06).               \n023278         10  WS-ACCR-YIELD        PIC S9(12)V9(06).               \n023280         10  WS-END-PERIOD        PIC 9(08).                      \n023282         10  WS-TDAA-NXT-CMPD-DT  PIC 9(08).                      \n023284         10  WS-NXT-CMPD-DT       PIC 9(08).                      \n023286         10  WS-CUR-PRS-EFF-DT    PIC 9(08).                      \n023288         10  WS-TDAA-INTERVAL     PIC 9(03).                      \n023290         10  WS-NBR-DAYS          PIC S9(05).                     \n023292         10  WS-CMPD-PER-INT      PIC S9(12)V9(06).               \n023294         10  WS-CMPD-INT          PIC S9(12)V99.                  \n023296         10  WS-ACCR-DT           PIC 9(08).                      \n023298         10  WS-YIELD-DENOM       PIC 9(03).                      \n023300         10  WS-YIELD-NUM         PIC 9(03).                      \n023302         10  WS-START-DATE        PIC 9(08).                      \n023304         10  WS-FINISH-DATE       PIC 9(08).                      \n023306         10  WS-ACCR-END-DT       PIC 9(08).                      \n023308         10  WS-PER-DIEM          PIC S9(12)V9(06).               \n023310         10  WS-ACCR-INT          PIC S9(12)V9(06).               \n023312         10  WS-NXT-POST-DT       PIC 9(08).                      \n023314                                                                  \n023316     05  WS-TDAA-INT-IN-PRC.                                      \n023318         10  WS-WITHHOLD-RATE-TABLE.                              \n023320             15  FILLER              PIC 9(08)    VALUE 20062800. \n023322             15  FILLER              PIC 9(08)    VALUE 20182400. \n023324         10  WS-WITHHOLD-RT-TABLE REDEFINES WS-WITHHOLD-RATE-TABLE\n023326                                     OCCURS 2 TIMES.              \n023328             15  WS-WTHLD-YEAR       PIC 9(04).                   \n023330             15  WS-WTHLD-RATE       PIC 99V99.                   \n023332             15  WS-WTHLD-PERCENT REDEFINES WS-WTHLD-RATE         \n023334                                     PIC   V9(04).                \n023336         10  WS-WTHLD-INDEX          PIC 99.                      \n023338         10  WS-WTHLD-MAX-INDEX      PIC 99         VALUE 02.     \n023340         10  WS-TDAA-NXT-POST-DT     PIC 9(08).                   \n023342         10  WS-NXT-IN-PRC-DT        PIC 9(08).                   \n023344         10  WS-MAX-DAYS             PIC 9(02)      VALUE 15.     \n023346         10  WS-WITHHOLD-AMT         PIC S9(12)V99.               \n023348         10  WS-ST-WHLD-AMT          PIC S9(12)V99.               \n023350         10  WS-DAY-OF-WEEK          PIC X(03).                   \n023352         10  WS-IN-PROCESS-DAY       PIC X(03)      VALUE \"FRI\".  \n023354                                                                  \n023356     05  WS-PENALTY-FIELDS.                                       \n023358         10  WS-PEN-LST-POST-DT      PIC 9(08).                   \n023360         10  WS-PEN-CURR-BAL         PIC S9(12)V99.               \n023362         10  WS-PEN-NXT-POST-DT      PIC 9(08).                   \n023364         10  WS-PEN-DAYS-INTO-PER    PIC 9(4).                    \n023366         10  WS-PEN-DAYS-IN-PER      PIC 9(4).                    \n023368         10  WS-PEN-NXT-IN-PROC      PIC 9(08).                   \n023370         10  WS-PEN-PENALTY-AMT      PIC 9(12)V99.                \n023372         10  WS-PEN-AMOUNT           PIC 9(12)V99.                \n023374         10  WS-PEN-PERCENT          PIC 9(02)V999.               \n023376         10  WS-PEN-FUNC             PIC X         VALUE SPACE.   \n023378         10  WS-PEN-FUNC-DESC        PIC X(14)     VALUE SPACES.  \n023380         10  WSP-FLAG                PIC 9(04)     VALUE 0.       \n023382         10  WSP-FLAG-A              REDEFINES  WSP-FLAG.         \n023384             15  WSP-FLAG-AMOUNT     PIC 9(01).                   \n023386             15  WSP-FLAG-MAT-INT    PIC 9(01).                   \n023388             15  WSP-FLAG-REN-DT     PIC 9(01).                   \n023390             15  WSP-FLAG-DT         PIC 9(01).                   \n023392                                                                  \n023394         10  WSP-FLAG-B               PIC 9(01).                  \n023396                                                                  \n023398     05  WS-TDAA-INT-POSTING.                                     \n023400         10  WS-ACCR-ADJ             PIC S9(12)V9(06).            \n023402         10  WS-POST-INT             PIC S9(12)V99.               \n023404                                                                  \n023406     05  WS-OLD-NEW-ANTIC-INT.                                    \n023408         10  WS-OLD-ANTIC-INT        PIC S9(12)V99.               \n023410         10  WS-NEW-ANTIC-INT        PIC S9(12)V99.               \n023412                                                                  \n023414     05  WS-TDAA-DISTR.                                           \n023416         10  WS-AMT                  PIC 9(12)V99.                \n023418         10  WS-DIST-DIFF            PIC 9(12)V99.                \n023420         10  WS-DIST-TOT             PIC 9(15)V99.                \n023422         10  WS-DIST-PRINCPL-AMT     PIC S9(12)V99.               \n023424         10  WS-DIST-NXT-DIST-DT     PIC 9(8).                    \n023426         10  WS-DIST-CALC-ANTIC      PIC 9.                       \n023428                                                                  \n023430     05  WS-DS-AVAIL-BAL             PIC S9(12)V99.               \n023432     05  WS-SAVE-AVAIL-BAL           PIC S9(12)V99.               \n023434                                                                  \n023436     05  WS-APY-CALC.                                             \n023438         10  WS-APY-QUO              PIC 9(4)        VALUE 0.     \n023440         10  WS-APY-REM              PIC 9(4)        VALUE 0.     \n023442         10  WS-APY                  PIC 9(04)V99.                \n023444         10  WS-APY-INT              PIC 9(12)V9(06).             \n023446         10  WS-APY-FLAG             PIC 9(01)       VALUE 0.     \n023448         10  WS-FREQ-MONTHS          PIC 9(03).                   \n023450         10  WS-APY-START            PIC 9(08).                   \n023452         10  WS-APY-END              PIC 9(08).                   \n023454         10  WS-APY-BAL              PIC S9(12)V99.               \n023456         10  WS-APY-YIELD            PIC S99V999.                 \n023458         10  WS-PAY-DATE             PIC 9(06).                   \n023460         10  WS-PAY-DATE2            PIC 9(06).                   \n023462         10  WS-APY-INT-HOLD         PIC 9(12)V99.                \n023464         10  WS-FREQ-DAYS            PIC 9(04).                   \n023466         10  WS-FREQ-DAYS-HOLD       PIC 9(04).                   \n023468         10  WS-INT-INTVL            PIC 9(04)       VALUE 0.     \n023470         10  WS-RED-INTVL            PIC 9(04)       VALUE 0.     \n023472                                                                  \n023474         10  WS-ACCT-DAILY-COMP      PIC 9(04)       VALUE 0.     \n023476             88  ACCT-DAILY-COMP                     VALUE 1.     \n023478                                                                  \n023480         10  WS-TDA-APY-FLAG         PIC 9(01)       VALUE 0.     \n023482             88  WS-TDA-DAYS                         VALUE 1.     \n023484             88  WS-TDA-MONTHS                       VALUE 2.     \n023486                                                                  \n023488     05  WS-COMBINE-CHECKS.                                       \n023490         10  WS-CHG-CURR              PIC 9(02).                  \n023492         10  WS-CHG-OLD               PIC 9(02).                  \n023494         10  WS-HOLD-TBL-CUST.                                    \n023496             15  WS-HOLD-TBL-CUSTOMER OCCURS 10 TIMES.            \n023498                 20  WS-HOLD-TDACK-CUST   PIC 9(12).              \n023500                 20  WS-HOLD-TDACK-ACCT   PIC 9(10).              \n023502         10  WS-DUPL-TDACK-CUST           PIC 9(12).              \n023504         10  WS-DUPL-TDACK-ACCT           PIC 9(10).              \n023506                                                                  \n023508     05  WS-ACTVC-CODE            PIC 9(04).                      \n023510     05  WS-ACTVC-CHG-FRM         PIC X(40).                      \n023512     05  WS-ACTVC-CHG-TO          PIC X(40).                      \n023514     05  WS-ACTVC-CHG-FRM-XLATE.                                  \n023516         10  WS-ACTVC-CHG-FRM-XLATE-X PIC X(40).                  \n023518     05  WS-ACTVC-CHG-TO-XLATE.                                   \n023520         10  WS-ACTVC-CHG-TO-XLATE-X  PIC X(40).                  \n023522     05  WS-ACTVC-LEF.                                            \n023524         10 WS-ACTVC-LEF-X            PIC X(40).                  \n023526         10 WS-ACTVC-LEF1-R REDEFINES WS-ACTVC-LEF-X.             \n023528            15 FILLER                       PIC X(36).            \n023530            15 WS-ACTVC-LEF-FORMATED        PIC 99.9.             \n023532                                                                  \n023534     05  9-FIELD                  PIC S9(16)V99.                  \n023536     05  9-FIELD-NS               PIC 9(16)V99.                   \n023538     05  9-FIELD-V3               PIC S9(15)V999.                 \n023540     05  9-FIELD-V3-NS            PIC 9(15)V999.                  \n023542     05  9-FIELD-V4               PIC S9(14)V9999.                \n023544     05  9-FIELD-V4-NS            PIC 9(14)V9999.                 \n023546     05  9-FIELD-V6               PIC S9(12)V9(6).                \n023548     05  9-FIELD-V6-NS            PIC 9(12)V9(6).                 \n023550                                                                  \n023552     05  WS-EIRA-DATE             PIC 9(08).                      \n023554                                                                  \n023556     05  WS-HOLD-NBR              PIC 99                          \n023558                                  OCCURS 99 TIMES.                \n023560     05  WS-TRANS-AMT-X.                                          \n023562         10  WS-TRANS-AMT         PIC S9(12)V99.                  \n023564                                                                  \n023566     05  WS-TRANS-RT-X.                                           \n023568         10  WS-TRANS-RT          PIC 9(2)V9(3).                  \n023570                                                                  \n023572     05  WS-HOLDS-AMT-X.                                          \n023574         10  WS-HOLDS-AMT         PIC S9(12)V99.                  \n023576                                                                  \n023578     05  WS-ACTV-SEQ-NBR          PIC 9(02)          VALUE 0.     \n023580                                                                  \n023582     05  WS-QUOTIENT              PIC 9(04)          VALUE 0.     \n023584     05  WS-REMAINDER             PIC 9(04)          VALUE 0.     \n023586                                                                  \n023588     05  WS-DESC                  PIC X(72).                      \n023590                                                                  \n023592     05  WS-ACTION                PIC X(01).                      \n023594                                                                  \n023596     05  WS-FILE-MAINT.                                           \n023598         10  INPUT-DATA           PIC X(40).                      \n023600         10  IRA-FLG              PIC 9(01).                      \n023602         10  ACCT-FLG             PIC 9(01).                      \n023604                                                                  \n023606     05  WS-MESSAGE-NBR           PIC 9(04).                      \n023608     05  WS-MESSAGE               PIC X(65).                      \n023610     05  WS-ERROR-NBR             PIC 9(04).                      \n023612      05  WS-UNSIGNED-ADJUST       PIC 9(09)V99.                  \n023614                                                                  \n023616     05  WS-NEXT-DATE.                                            \n023618         10  WS-FREQUENCY         PIC 9(04).                      \n023620         10  WS-FREQUENCY-TYPE    PIC 9(01).                      \n023622         10  WS-RSLT-DT           PIC 9(08).                      \n023624         10  WS-NXT-DATE-CYMD.                                    \n023626             15  WS-NXT-DATE-CY             PIC 9(04).            \n023628             15  WS-NXT-DATE-CY-R REDEFINES WS-NXT-DATE-CY.       \n023630                 20 WS-NXT-DATE-CC          PIC 99.               \n023632                 20 WS-NXT-DATE-YY          PIC 99.               \n023634             15  WS-NXT-DATE-MD             PIC 9(04).            \n023636             15  WS-NXT-DATE-MD-R REDEFINES WS-NXT-DATE-MD.       \n023638                 20 WS-NXT-DATE-MM          PIC 99.               \n023640                 20 WS-NXT-DATE-DD          PIC 99.               \n023642                                                                  \n023644     05  WS-NXT-DT                PIC 9(08).                      \n023646     05  WS-CUR-DT                PIC 9(08).                      \n023648     05  WS-TIN-CONVERT.                                          \n023650         10  WS-TIN-BEFORE        PIC 9(09).                      \n023652         10  WS-TIN-MASK          REDEFINES WS-TIN-BEFORE.        \n023654             15  WS-E-TIN.                                        \n023656                 20  WS-E2        PIC 9(02).                      \n023658                 20  WS-E7        PIC 9(07).                      \n023660             15  WS-S-TIN         REDEFINES WS-E-TIN.             \n023662                 20  WS-S3        PIC 9(03).                      \n023664                 20  WS-S2        PIC 9(02).                      \n023666                 20  WS-S4        PIC 9(04).                      \n023668         10  WS-TIN               PIC X(11).                      \n023670                                                                  \n023672     05  WS-INTERVAL-CONVERT.                                     \n023674         10  WS-TYPE-CD           PIC 9(01).                      \n023676         10  WS-INTERVAL          PIC X(01).                      \n023678                                                                  \n023680     05  WS-TOTAL-TYPE-CD.                                        \n023682         10  WS-TYPE-12-34.                                       \n023684             15  WS-TYPE-12       PIC X(2).                       \n023686             15  WS-TYPE-34       PIC X(3).                       \n023688         10  WS-TYPE-1-24  REDEFINES  WS-TYPE-12-34.              \n023690             15  WS-TYPE-1        PIC X(2).                       \n023692             15  WS-TYPE-24       PIC X(3).                       \n023694         10  WS-TYPE-13-4  REDEFINES  WS-TYPE-12-34.              \n023696             15  WS-TYPE-13       PIC X(4).                       \n023698             15  WS-TYPE-4        PIC X(1).                       \n023700     05  WS-TOTAL-TYPE-CD-NEW.                                    \n023702         10  WS-TYPE-CD-11.                                       \n023704             15 WS-TYPE-CD-1      PIC X(1).                       \n023706             15 WS-TYPE-CD-23     PIC X(2).                       \n023708             15 WS-TYPE-CD-4567   PIC X(4).                       \n023710             15 FILLER            PIC X(4).                       \n023712         10  WS-TYPE-CD-12345-67-8901 REDEFINES WS-TYPE-CD-11.    \n023714             15 WS-TYPE-CD-12345  PIC X(5).                       \n023716             15 WS-TYPE-CD-67     PIC X(2).                       \n023718             15 FILLER            PIC X(4).                       \n023720         10  WS-TYPE-CD-123456-7-8901 REDEFINES WS-TYPE-CD-11.    \n023722             15 WS-TYPE-CD-123456 PIC X(6).                       \n023724             15 WS-TYPE-CD-7      PIC X(1).                       \n023726             15 FILLER            PIC X(4).                       \n023728         10  WS-TYPE-CD-1234-567-8901 REDEFINES WS-TYPE-CD-11.    \n023730             15 WS-TYPE-CD-1234   PIC X(4).                       \n023732             15 WS-TYPE-CD-567    PIC X(3).                       \n023734             15 FILLER            PIC X(4).                       \n023736         10  WS-TYPE-CD-1234567-8901 REDEFINES WS-TYPE-CD-11.     \n023738             15 FILLER            PIC X(1).                       \n023740             15 WS-TYPE-CD-234567 PIC X(6).                       \n023742             15 FILLER            PIC X(4).                       \n023744     05  WS-TOTAL-TYPE-CD-LGB.                                    \n023746         10  FILLER                PIC X(1).                      \n023748         10  WS-TYPE-CD-LGB-2345   PIC X(4).                      \n023750         10  WS-TYPE-CD-LGB-678901 PIC X(6).                      \n023752                                                                  \n023754     05  WS-DISP-CONVERT.                                         \n023756         10  WS-DISP-CODE         PIC 9(01).                      \n023758         10  WS-DISP-DESC         PIC X(03).                      \n023760                                                                  \n023762     05  WS-CUR-INT-RT-X.                                         \n023764         10  WS-CUR-INT-RT        PIC S99V999.                    \n023766     05  WS-BASE-RT-X.                                            \n023768         10 WS-BASE-RT            PIC S99V999.                    \n023770     05  WS-STEPPED-RATE-VARIABLES.                               \n023772         10  WS-CURR-STEP-RATE    PIC  99V999.                    \n023774         10  WS-CURR-STEP-DATE    PIC 9(08).                      \n023776         10  WS-CURR-CYCLE-NBR    PIC 99.                         \n023778                                                                  \n023780     05  WS-HOLD-CHG-CODE         PIC 9(006).                     \n023782     05  WS-HOLD-CHG-CODE-R  REDEFINES WS-HOLD-CHG-CODE.          \n023784         10  WS-CHANGE-CODE       PIC 9(004)V99.                  \n023786     05  WS-CHG-WORK-EXP          PIC X(100).                     \n023788     05  WS-CHG-WORK              PIC X(040).                     \n023790     05  WS-CHG-WORK-R1      REDEFINES WS-CHG-WORK.               \n023792         10  WS-CHG-WK-X-1        PIC X(001).                     \n023794         10  FILLER               PIC X(039).                     \n023796     05  WS-CHG-WORK-R2      REDEFINES WS-CHG-WORK.               \n023798         10  WS-CHG-WK-X-2        PIC X(002).                     \n023800         10  FILLER               PIC X(038).                     \n023802     05  WS-CHG-WORK-R3      REDEFINES WS-CHG-WORK.               \n023804         10  WS-CHG-WK-X-3        PIC X(003).                     \n023806         10  FILLER               PIC X(037).                     \n023808     05  WS-CHG-WORK-R4      REDEFINES WS-CHG-WORK.               \n023810         10  WS-CHG-WK-X-4        PIC X(004).                     \n023812         10  FILLER               PIC X(036).                     \n023814     05  WS-CHG-WORK-R5      REDEFINES WS-CHG-WORK.               \n023816         10  WS-CHG-WK-X-5        PIC X(005).                     \n023818         10  FILLER               PIC X(035).                     \n023820     05  WS-CHG-WORK-R6      REDEFINES WS-CHG-WORK.               \n023822         10  WS-CHG-WK-X-6        PIC X(006).                     \n023824         10  FILLER               PIC X(034).                     \n023826     05  WS-CHG-WORK-R30     REDEFINES WS-CHG-WORK.               \n023828         10  WS-CHG-WK-X-8        PIC X(008).                     \n023830         10  FILLER               PIC X(032).                     \n023832     05  WS-CHG-WORK-R35     REDEFINES WS-CHG-WORK.               \n023834         10  WS-CHG-WK-X-9        PIC X(009).                     \n023836         10  FILLER               PIC X(031).                     \n023838     05  WS-CHG-WORK-R7      REDEFINES WS-CHG-WORK.               \n023840         10  WS-CHG-WK-X-10       PIC X(010).                     \n023842         10  FILLER               PIC X(030).                     \n023844     05  WS-CHG-WORK-R79     REDEFINES WS-CHG-WORK.               \n023846         10  WS-CHG-WK-X-12       PIC X(012).                     \n023848         10  FILLER               PIC X(028).                     \n023850     05  WS-CHG-WORK-R46     REDEFINES WS-CHG-WORK.               \n023852         10  WS-CHG-WK-X-14       PIC X(14).                      \n023854         10  FILLER               PIC X(26).                      \n023856     05  WS-CHG-WORK-R8      REDEFINES WS-CHG-WORK.               \n023858         10  WS-CHG-WK-X-20       PIC X(020).                     \n023860         10  FILLER               PIC X(020).                     \n023862     05  WS-CHG-WORK-R9      REDEFINES WS-CHG-WORK.               \n023864         10  WS-CHG-WK-X-24       PIC X(024).                     \n023866         10  FILLER               PIC X(016).                     \n023868     05  WS-CHG-WORK-R49     REDEFINES WS-CHG-WORK.               \n023870         10  WS-CHG-WK-X-25       PIC X(025).                     \n023872         10  FILLER               PIC X(015).                     \n023874     05  WS-CHG-WORK-R45     REDEFINES WS-CHG-WORK.               \n023876         10  WS-CHG-WK-X-28       PIC X(28).                      \n023878         10  FILLER               PIC X(12).                      \n023880     05  WS-CHG-WORK-R38     REDEFINES WS-CHG-WORK.               \n023882         10  WS-CHG-WK-X-29       PIC X(29).                      \n023884         10  FILLER               PIC X(11).                      \n023886     05  WS-CHG-WORK-R10     REDEFINES WS-CHG-WORK.               \n023888         10  FILLER               PIC X(039).                     \n023890         10  WS-CHG-WK-9-1        PIC 9(001).                     \n023892     05  WS-CHG-WORK-R11     REDEFINES WS-CHG-WORK.               \n023894         10  FILLER               PIC X(038).                     \n023896         10  WS-CHG-WK-9-2        PIC 9(002).                     \n023898     05  WS-CHG-WORK-R12     REDEFINES WS-CHG-WORK.               \n023900         10  FILLER               PIC X(037).                     \n023902         10  WS-CHG-WK-9-3        PIC 9(003).                     \n023904     05  WS-CHG-WORK-R13     REDEFINES WS-CHG-WORK.               \n023906         10  FILLER               PIC X(036).                     \n023908         10  WS-CHG-WK-9-4        PIC 9(004).                     \n023910     05  WS-CHG-WORK-R14     REDEFINES WS-CHG-WORK.               \n023912         10  FILLER               PIC X(035).                     \n023914         10  WS-CHG-WK-9-5        PIC 9(005).                     \n023916     05  WS-CHG-WORK-R15     REDEFINES WS-CHG-WORK.               \n023918         10  FILLER               PIC X(034).                     \n023920         10  WS-CHG-WK-9-6        PIC 9(006).                     \n023922     05  WS-CHG-WORK-R31     REDEFINES WS-CHG-WORK.               \n023924         10  FILLER               PIC X(033).                     \n023926         10  WS-CHG-WK-9-7        PIC 9(007).                     \n023928     05  WS-CHG-WORK-R16     REDEFINES WS-CHG-WORK.               \n023930         10  FILLER               PIC X(032).                     \n023932         10  WS-CHG-WK-9-8        PIC 9(008).                     \n023934     05  WS-CHG-WORK-R17     REDEFINES WS-CHG-WORK.               \n023936         10  FILLER               PIC X(031).                     \n023938         10  WS-CHG-WK-9-9        PIC 9(009).                     \n023940     05  WS-CHG-WORK-R18     REDEFINES WS-CHG-WORK.               \n023942         10  FILLER               PIC X(030).                     \n023944         10  WS-CHG-WK-9-10       PIC 9(010).                     \n023946     05  WS-CHG-WORK-R19     REDEFINES WS-CHG-WORK.               \n023948         10  FILLER               PIC X(028).                     \n023950         10  WS-CHG-WK-9-12       PIC 9(012).                     \n023952     05  WS-CHG-WORK-R20     REDEFINES WS-CHG-WORK.               \n023954         10  FILLER               PIC X(030).                     \n023956         10  WS-CHG-WK-9-8V2      PIC 9(008)V99.                  \n023958     05  WS-CHG-WORK-R21     REDEFINES WS-CHG-WORK.               \n023960         10  FILLER               PIC X(030).                     \n023962         10  WS-CHG-WK-9-S8V2     PIC S9(008)V99.                 \n023964     05  WS-CHG-WORK-R37     REDEFINES WS-CHG-WORK.               \n023966         10  FILLER               PIC X(037).                     \n023968         10  WS-CHG-WK-9-S1V2     PIC S9V99.                      \n023970     05  WS-CHG-WORK-R42     REDEFINES WS-CHG-WORK.               \n023972         10  FILLER               PIC X(037).                     \n023974         10  WS-CHG-WK-9-2V1      PIC 99V9.                       \n023976     05  WS-CHG-WORK-R22     REDEFINES WS-CHG-WORK.               \n023978         10  FILLER               PIC X(035).                     \n023980         10  WS-CHG-WK-9-2V3      PIC 9(002)V999.                 \n023982     05  WS-CHG-WORK-R39     REDEFINES WS-CHG-WORK.               \n023984         10  FILLER               PIC X(035).                     \n023986         10  WS-CHG-WK-9-S2V3     PIC S9(002)V999.                \n023988     05  WS-CHG-WORK-R23     REDEFINES WS-CHG-WORK.               \n023990         10  FILLER               PIC X(034).                     \n023992         10  WS-CHG-WK-9-2V4      PIC 9(002)V9999.                \n023994     05  WS-CHG-WORK-R24     REDEFINES WS-CHG-WORK.               \n023996         10  FILLER               PIC X(032).                     \n023998         10  WS-CHG-WK-9-2V6      PIC 9(002)V999999.              \n024000     05  WS-CHG-WORK-R32     REDEFINES WS-CHG-WORK.               \n024002         10  FILLER               PIC X(034).                     \n024004         10  WS-CHG-WK-9-4V2      PIC 9(004)V99.                  \n024006     05  WS-CHG-WORK-R36     REDEFINES WS-CHG-WORK.               \n024008         10  FILLER               PIC X(033).                     \n024010         10  WS-CHG-WK-9-5V2      PIC 9(005)V99.                  \n024012     05  WS-CHG-WORK-R25     REDEFINES WS-CHG-WORK.               \n024014         10  FILLER               PIC X(030).                     \n024016         10  WS-CHG-WK-9-6V4      PIC 9(006)V9999.                \n024018     05  WS-CHG-WORK-R26     REDEFINES WS-CHG-WORK.               \n024020         10  FILLER               PIC X(030).                     \n024022         10  WS-CHG-WK-9-S6V4     PIC S9(006)V9999.               \n024024     05  WS-CHG-WORK-R27     REDEFINES WS-CHG-WORK.               \n024026         10  FILLER               PIC X(029).                     \n024028         10  WS-CHG-WK-9-S9V2     PIC S9(009)V99.                 \n024030     05  WS-CHG-WORK-R28     REDEFINES WS-CHG-WORK.               \n024032         10  FILLER               PIC X(027).                     \n024034         10  WS-CHG-WK-9-S11V2    PIC S9(011)V99.                 \n024036     05  WS-CHG-WORK-R41     REDEFINES WS-CHG-WORK.               \n024038         10  FILLER               PIC X(26).                      \n024040         10  WS-CHG-WK-9-S12V2    PIC S9(12)V99.                  \n024042     05  WS-CHG-WORK-R34     REDEFINES WS-CHG-WORK.               \n024044         10  FILLER               PIC X(025).                     \n024046         10  WS-CHG-WK-9-13V2     PIC 9(013)V99.                  \n024048     05  WS-CHG-WORK-R33     REDEFINES WS-CHG-WORK.               \n024050         10  FILLER               PIC X(025).                     \n024052         10  WS-CHG-WK-9-S13V2    PIC S9(013)V99.                 \n024054     05  WS-CHG-WORK-R29     REDEFINES WS-CHG-WORK.               \n024056         10  WS-CHG-WK-CC         PIC 9(002).                     \n024058         10  WS-CHG-WK-YY         PIC 9(002).                     \n024060         10  WS-CHG-WK-MM         PIC 9(002).                     \n024062         10  WS-CHG-WK-DD         PIC 9(002).                     \n024064         10  FILLER               PIC X(032).                     \n024066     05  WS-CHG-WORK-R40    REDEFINES WS-CHG-WORK.                \n024068         10  FILLER               PIC X(023).                     \n024070         10  WS-CHG-WK-9-S15V2    PIC S9(015)V99.                 \n024072     05  WS-CHG-WORK-R43    REDEFINES WS-CHG-WORK.                \n024074         10  FILLER               PIC X(022).                     \n024076         10  WS-CHG-WK-9-S12V6    PIC S9(012)V9(06).              \n024078     05  WS-CHG-WORK-R44    REDEFINES WS-CHG-WORK.                \n024080         10  FILLER               PIC X(024).                     \n024082         10  WS-CHG-WK-9-S12V4    PIC S9(012)V9(04).              \n024084     05  WS-CHG-WORK-R47    REDEFINES WS-CHG-WORK.                \n024086         10  WS-CHG-WK-X-22       PIC X(022).                     \n024088         10  FILLER               PIC X(018).                     \n024090     05  WS-CHG-WORK-R48    REDEFINES WS-CHG-WORK.                \n024092         10  FILLER               PIC X(32).                      \n024094         10  WS-CHG-WK-9-S6V2     PIC S9(6)V9(2).                 \n024096                                                                  \n024098     05  WS-TRCD                  PIC 9(004)   COMP VALUE ZEROES. \n024100         88  CREDIT-TRANS         VALUE 31 113 114 115 116 117 118\n024102             119 120 121 122 123 124 128 129.                     \n024104     05  WS-MODDER                PIC 9(01).                      \n024106     05  WS-MODDER2               PIC 9(04).                      \n024108         88  DEBIT-TRANS          VALUE 39 110 132 133 135 137 138\n024110               139 140 141 142 143 144 145 146 147 148 149 151 152\n024112               153 154 155.                                       \n024114         88  IRA-CONTRIB          VALUE 31 113 118.               \n024116         88  IRA-DISTRIB          VALUE 132 133 135 139 141 142   \n024118                                        146 151 155.              \n024120         88  CLOSING-TRANS        VALUE 110 111.                  \n024122         88  REQ-STMT             VALUE 112.                      \n024124         88  REQ-HOLD             VALUE 035 036.                  \n024126                                                                  \n024128     05  HOLD-DATE-MDY            PIC 9(06).                      \n024130     05  HOLD-RATE-X.                                             \n024132         10  HOLD-RATE            PIC S99V999.                    \n024134     05  HOLD-EFF-DATE            PIC 9(08).                      \n024136     05  HOLD-END-DATE            PIC 9(08).                      \n024138     05  HOLD-CYC-INCREMENT.                                      \n024140         10  HOLD-CYC-INC1        PIC S99V999.                    \n024142         10  HOLD-CYC-INC2        PIC S99V999.                    \n024144         10  HOLD-CYC-INC3        PIC S99V999.                    \n024146         10  HOLD-CYC-INC4        PIC S99V999.                    \n024148         10  HOLD-CYC-INC5        PIC S99V999.                    \n024150         10  HOLD-CYC-INC6        PIC S99V999.                    \n024152         10  HOLD-CYC-INC7        PIC S99V999.                    \n024154         10  HOLD-CYC-INC8        PIC S99V999.                    \n024156         10  HOLD-CYC-INC9        PIC S99V999.                    \n024158         10  HOLD-CYC-INC10       PIC S99V999.                    \n024160                                                                  \n024162     05  HOLD-TIER-BALANCE.                                       \n024164         10  HOLD-TIER-BAL1       PIC 9(12)V99.                   \n024166         10  HOLD-TIER-BAL2       PIC 9(12)V99.                   \n024168         10  HOLD-TIER-BAL3       PIC 9(12)V99.                   \n024170         10  HOLD-TIER-BAL4       PIC 9(12)V99.                   \n024172         10  HOLD-TIER-BAL5       PIC 9(12)V99.                   \n024174         10  HOLD-TIER-BAL6       PIC 9(12)V99.                   \n024176         10  HOLD-TIER-BAL7       PIC 9(12)V99.                   \n024178         10  HOLD-TIER-BAL8       PIC 9(12)V99.                   \n024180         10  HOLD-TIER-BAL9       PIC 9(12)V99.                   \n024182         10  HOLD-TIER-BAL10      PIC 9(12)V99.                   \n024184         10  HOLD-TIER-BAL11      PIC 9(12)V99.                   \n024186         10  HOLD-TIER-BAL12      PIC 9(12)V99.                   \n024188         10  HOLD-TIER-BAL13      PIC 9(12)V99.                   \n024190         10  HOLD-TIER-BAL14      PIC 9(12)V99.                   \n024192         10  HOLD-TIER-BAL15      PIC 9(12)V99.                   \n024194                                                                  \n024196     05  HOLD-TIER-INCREMENT.                                     \n024198         10  HOLD-TIER-INCR1      PIC S99V999.                    \n024200         10  HOLD-TIER-INCR2      PIC S99V999.                    \n024202         10  HOLD-TIER-INCR3      PIC S99V999.                    \n024204         10  HOLD-TIER-INCR4      PIC S99V999.                    \n024206         10  HOLD-TIER-INCR5      PIC S99V999.                    \n024208         10  HOLD-TIER-INCR6      PIC S99V999.                    \n024210         10  HOLD-TIER-INCR7      PIC S99V999.                    \n024212         10  HOLD-TIER-INCR8      PIC S99V999.                    \n024214         10  HOLD-TIER-INCR9      PIC S99V999.                    \n024216         10  HOLD-TIER-INCR10     PIC S99V999.                    \n024218         10  HOLD-TIER-INCR11     PIC S99V999.                    \n024220         10  HOLD-TIER-INCR12     PIC S99V999.                    \n024222         10  HOLD-TIER-INCR13     PIC S99V999.                    \n024224         10  HOLD-TIER-INCR14     PIC S99V999.                    \n024226         10  HOLD-TIER-INCR15     PIC S99V999.                    \n024228                                                                  \n024230     05  KEY-DATA.                                                \n024232         10 KEY-RPT-NBR           PIC 9(04).                      \n024234         10 KEY-REGION            PIC 9(01).                      \n024236         10 KEY-CODE              PIC 9(03).                      \n024238         10 KEY-DATE              PIC 9(08).                      \n024240                                                                  \n024242     05  TDA-ONLACT-FILE-ID.                                      \n024244         10  FILLER               PIC X(05) VALUE \"TDA0B\".        \n024246         10  TDA-ONLACT-DATE-MMDD PIC 9(04).                      \n024248         10  FILLER               PIC X(07) VALUE \"/ONLACT\".      \n024250         10  TDA-ONLACT-SUFFIX    PIC X(01) VALUE SPACE.          \n024252         10  FILLER               PIC X(01) VALUE \"/\".            \n024254         10  TDA-ONLACT-TIME      PIC 9(08).                      \n024256         10  FILLER               PIC X(01) VALUE \".\".            \n024258                                                                  \n024260     05  TDA-PCR-I                PIC 9(03).                      \n024262     05  TDA-PCR-RPT-NUM          PIC 9(03).                      \n024264     05  TDA-PCR-REQ              PIC 9(01).                      \n024266     05  TDA-PCR-RPT-TYPE         PIC 9(01).                      \n024268     05  TDA-PCR-USE-PILOT        PIC 9(01).                      \n024270     05  TDA-PILOT-TYPE           PIC X(01).                      \n024272     05  WS-HOLD-CN-TYPE-EX       PIC 9(02).                      \n024274     05  WS-SKIP-OPEN-TRANS       PIC 9.                          \n024276     05  WS-CALC-BANK             PIC 9(04).                      \n024278     05  WS-CALC-CUST             PIC 9(10).                      \n024280     05  WS-CALC-ACCT             PIC 9(12).                      \n024282     05  WS-CALC-LST-DT           PIC 9(08).                      \n024284     05  WS-CALC-NXT-DT           PIC 9(08).                      \n024286     05  WS-CALC-CURR-BAL         PIC S9(12)V99.                  \n024288     05  WS-CALC-AMT              PIC S9(12)V99.                  \n024290                                                                  \n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 699 lines from 11443 to 12141.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 25,
  "total_chunks": 55,
  "start_line": 11443,
  "end_line": 12141,
  "line_count": 699
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
- Source code length: 57932 characters

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
CHUNK 25 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 11443 to 12141 (699 lines)
Chunk Tokens (estimated): ~13,304
Actual Input Tokens: 14,710 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 11443-12141 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 25 of 55 chunks
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
      The source code below is only CHUNK 25 of 55.


=============================================================================
CHUNK 25 SOURCE CODE (Lines 11443-12141)
=============================================================================

```cobol
022894 01  WS-SCREEN-AREA.                                              
022896**  The following data items are used within a single process.    
022898**  None of this data will be tranfered to any other processes.   
022900                                                                  
022902     05  WS-HEADER                PIC X(23).                      
022904     05  WS-TODAY                 PIC X(08).                      
022906     05  WS-TIME                  PIC X(05).                      
022908                                                                  
022910     05  WS-POP-UP                PIC 9       VALUE ZERO.         
022912     05  WS-MISC-EDIT-TRIG        PIC 9       VALUE ZERO.         
022914                                                                  
022916     05  WS-MAX-TDB-TABLE         PIC 99.                         
022918     05  WS-FM-INDEX              PIC 9(04).                      
022920     05  WS-VALID-FM              PIC 9.                          
022922                                                                  
022924     05  MAX-SUB                  PIC 9(04).                      
022926     05  SUB                      PIC 9(04).                      
022928     05  SUB-2                    PIC 9(04).                      
022930     05  WS-DDN                   PIC 9(05).                      
022932     05  WS-FIELD-NAME            PIC X(30).                      
022934                                                                  
022936     05  EXCLUDE-RAW-VALUE        PIC 9       VALUE 0.            
022938     05  INCLUDE-RAW-VALUE        PIC 9       VALUE 1.            
022940                                                                  
022942                                                                  
022944     05  WS-NEW-BNF-NBR           PIC 99.                         
022946     05  WS-PRI-BNF-TOTAL         PIC 999.                        
022948     05  WS-CONT-BNF-TOTAL        PIC 9999.                       
022950                                                                  
022952     05  WS-UPDATE-DISTR-RECORD   PIC 9       VALUE 0.            
022954     05  WS-UPDATE-IRA-RECORD     PIC 9       VALUE 0.            
022956     05  WS-UPDATE-CUST-RECORD    PIC 9       VALUE 0.            
022958     05  WS-UPDATE-HOLD-RECORDS   PIC 9       VALUE 0.            
022960     05  WS-RECALC-RUNNING-BAL    PIC 9       VALUE 0.            
022962                                                                  
022964     05  SPECS-MIN-PROC-DAYS      PIC 9     VALUE 4.              
022966                                                                  
022968**  These fields are used to determine proper processing date     
022970**  from operations.  They are used in TDD-VERIFY-PROCESS-DATE.   
022972     05  ENTER-DATE               PIC 9(6).                       
022974     05  DISPLAY-DATE             PIC X(12).                      
022976     05  NEXT-DATE                PIC 9(6).                       
022978     05  WS-END-OF                PIC 9(1).                       
022980     05  WS-RESPONSE              PIC X(1).                       
022982                                                                  
022984     05  WS-ADJUSTED-IND          PIC X(01) VALUE " ".            
022986         88  WS-ADJUSTED                    VALUE "A".            
022988         88  WS-ADJUSTED-NEW                VALUE "N".            
022990         88  WS-ADJUSTED-CURRENT            VALUE "C".            
022992                                                                  
022994     05  WS-RECORD-CHANGED-IND    PIC X(01) VALUE "N".            
022996         88  WS-RECORD-CHANGED              VALUE "Y".            
022998                                                                  
023000     05  WS-DIRECTION-IND         PIC X(01) VALUE " ".            
023002         88  WS-FORWARD                     VALUE "F".            
023004         88  WS-BACKWARD                    VALUE "B".            
023006                                                                  
023008     05  WS-RENEW-IND             PIC X(01) VALUE " ".            
023010         88  WS-RENEW                       VALUE "R".            
023012         88  WS-NEW                         VALUE "N".            
023014                                                                  
023016     05  WS-ACTION-CODE-CONSTANTS.                                
023018         10  WS-ACTION-ADD        PIC 99    VALUE 01.             
023020         10  WS-ACTION-CHANGE     PIC 99    VALUE 02.             
023022         10  WS-ACTION-DELETE     PIC 99    VALUE 03.             
023024         10  WS-ACTION-CHG-KEY    PIC 99    VALUE 04.             
023026                                                                  
023028     05  WS-DATE                  PIC X(08).                      
023030                                                                  
023032     05  WS-CD-HOLD-DT            PIC 9(08).                      
023034     05  WS-IRA-HOLD-DT           PIC 9(08).                      
023036                                                                  
023038     05  WS-DATE-CYMD.                                            
023040         10  WS-DATE-CY           PIC 9(04).                      
023042         10  WS-DATE-CY-R REDEFINES WS-DATE-CY.                   
023044             15  WS-DATE-CC       PIC 99.                         
023046             15  WS-DATE-YY       PIC 99.                         
023048         10  WS-DATE-MD           PIC 9(04).                      
023050         10  WS-DATE-MD-R REDEFINES WS-DATE-MD.                   
023052             15  WS-DATE-MM       PIC 9(02).                      
023054             15  WS-DATE-DD       PIC 9(02).                      
023056     05  WS-DATE-CYMD-R REDEFINES WS-DATE-CYMD.                   
023058         10  WS-DATE-C            PIC XX.                         
023060         10  WS-DATE-YMD          PIC X(06).                      
023062                                                                  
023064     05  WS-TIME-HMST.                                            
023066         10  WS-TIME-HMS.                                         
023068             15  WS-TIME-HH       PIC 9(02).                      
023070             15  WS-TIME-MM       PIC 9(02).                      
023072             15  WS-TIME-SS       PIC 9(02).                      
023074         10  WS-TIME-TT           PIC 9(02).                      
023076                                                                  
023078     05  WS-DAILY-PATTERN.                                        
023080         10  WS-DLY-PATTERN    OCCURS 7 TIMES     PIC X(1).       
023082                                                                  
023084     05  DATE-DEFINES-FIELDS.                                     
023086         10  FILLER               PIC 9(18)  VALUE ZEROES.        
023088         10  FILLER               PIC 9(18)  VALUE ZEROES.        
023090         10  FILLER               PIC 9(18)  VALUE ZEROES.        
023092         10  FILLER               PIC 9(02)  VALUE ZEROES.        
023094     05  DATE-DEFINES-FIELDS-R    REDEFINES DATE-DEFINES-FIELDS.  
023096         10  DD-DT-CONV-DAYS      PIC 9(06).                      
023098         10  DD-DT-CONV-MMM       PIC 9(03).                      
023100         10  DD-DT-CONV-YY        PIC 9(02).                      
023102         10  DD-DT-CONV-GEG       PIC 9(08).                      
023104         10  DD-DT-CONV-JUL       PIC 9(07).                      
023106         10  DD-DT-CONV-GEG-ERLY  PIC 9(08).                      
023108         10  DD-DT-CONV-GEG-LATE  PIC 9(08).                      
023110         10  DD-DT-CONV-JUL-ERLY  PIC 9(07).                      
023112         10  DD-DT-CONV-JUL-LATE  PIC 9(07).                      
023114     05  DD-DAY-OF-WEEK           PIC X(03)       VALUE SPACES.   
023116                                                                  
023118     05  WS-PRIOR-YEAR-CUTOFF     PIC 9(04)  VALUE 0430.          
023120                                                                  
023122     05  WS-SIZE                  PIC 9(2).                       
023124     05  WS-OFFSET                PIC 9(2).                       
023126                                                                  
023128     05  WS-IN-STRING             PIC X(18).                      
023130     05  WS-OUT-NUMERIC-X.                                        
023132         10  WS-OUT-NUMERIC       PIC S9(18).                     
023134                                                                  
023136     05  WS-RATE.                                                 
023138         10  WS-RATE-1-5-GRP.                                     
023140             15  WS-RATE-1-5      PIC 99V999.                     
023142             15  WS-RATE-6        PIC X(01).                      
023144         10  WS-RATE-2-6-GRP REDEFINES WS-RATE-1-5-GRP.           
023146             15  WS-RATE-1        PIC X(01).                      
023148             15  WS-RATE-2-6      PIC 99V999.                     
023150                                                                  
023152     05  WS-RATE-KEY-FIELDS.                                      
023154         10  WS-RATE-EFF-DATE     PIC 9(08).                      
023156         10  WS-RATE-ADD-DATE     PIC 9(08).                      
023158         10  WS-RATE-ADD-TIME     PIC 9(08).                      
023160          10 WS-RATE-ACTION-CD    PIC X(01).                      
023162         10  WS-RATE-TDAP-FUNC        PIC X(01).                  
023164         10  WS-RATE-TDAP-PUB-ID      PIC X(08).                  
023166         10  WS-RATE-TDAP-DATE        PIC 9(08).                  
023168         10  WS-RATE-TDAP-DAYS        PIC 9(04).                  
023170         10  WS-RATE-TDAP-MONTHS      PIC 9(04).                  
023172         10  WS-RATE-TDAP-PERCENT     PIC 99V99.                  
023174         10  WS-RATE-TDAP-AMOUNT      PIC 9(12)V99.               
023176         10  WS-RATE-TDAP-USE-INT     PIC 9(01).                  
023178         10  WS-RATE-TDAP-USE-RED     PIC 9(01).                  
023180         10  WS-RATE-TDAP-USE-MONTH   PIC 9(01).                  
023182         10  WS-RATE-TDAP-USE-DAY     PIC 9(01).                  
023184         10  WS-RATE-TDAP-USE-AVL-INT PIC 9(01).                  
023186         10  FILLER                   PIC X(27).                  
023188                                                                  
023190     05  WS-TDAPC-TYPE            PIC X(4).                       
023192     05  WS-PCR-KEY-FIELDS.                                       
023194         10  WS-PCR-PUB-ID        PIC X(08).                      
023196         10  WS-PCR-LUPD-DT       PIC 9(08).                      
023198         10  WS-PCR-LUPD-TM       PIC 9(06).                      
023200         10  WS-PCR-RPT-FIELD     PIC X(40).                      
023202                                                                  
023204     05  WS-ADD-DATE              PIC 9(08).                      
023206     05  WS-ADD-TIME              PIC 9(08).                      
023208                                                                  
023210     05  IRA-INDX                 PIC 99.                         
023212     05  TOTL-INDX                PIC 99.                         
023214                                                                  
023216     05  WS-PER-RATIO             PIC 9(03)V9(12).                
023218     05  WS-CMPD-PER-YR           PIC 9(03)V9(06).                
023220     05  WS-BASE                  PIC 9(06)V9(12).                
023222     05  WS-EXP                   PIC 9(06)V9(12).                
023224                                                                  
023226     05  DISPLAY-FIELDS.                                          
023228         10  DISPLAY-AMT          PIC Z,ZZZ,ZZZ,ZZ9.99-.          
023230         10  DISPLAY-RATE         PIC Z9.999-.                    
023232         10  DISPLAY-YIELD        PIC Z9.999-.                    
023234         10  DISPLAY-TIME         PIC XXXXXXXX.                   
023236         10  DISPLAY-PUB-ID       PIC X(8).                       
023238                                                                  
023240     05  ACCT-WARNING   OCCURS 4 TIMES.                           
023242         10  WARNING-DATE         PIC X(5).                       
023244         10  FILLER               PIC X(1).                       
023246         10  WARNING-DESC         PIC X(19).                      
023248                                                                  
023250     05  WS-TDAA-INTEREST-PAY.                                    
023252         10  WS-TDAA-LST-PAY-BAL  PIC S9(12)V99.                  
023254         10  WS-TDAA-LST-YIELD    PIC S9(12)V9(06).               
023256         10  WS-YIELD             PIC S9(06)V9999.                
023258*$$SET OMIT = TDASQLFLAG                                          
023260         10  WS-ACCR-PER-ACTV     PIC S9(12)V9(06).               
023262         10  WS-ACCR-PER-INT      PIC S9(12)V9(06).               
023264*$$POP OMIT                                                       
023266*$$SET OMIT = NOT TDASQLFLAG                                      
023268*         10  WS-ACCR-PER-ACTV     PIC S9(08)V9(08).              
023270*         10  WS-ACCR-PER-INT      PIC S9(08)V9(08).              
023272*$$POP OMIT                                                       
023274         10  WS-ANTIC-INT         PIC S9(12)V99.                  
023276         10  WS-ANTIC-INT-V4      PIC S9(12)V9(06).               
023278         10  WS-ACCR-YIELD        PIC S9(12)V9(06).               
023280         10  WS-END-PERIOD        PIC 9(08).                      
023282         10  WS-TDAA-NXT-CMPD-DT  PIC 9(08).                      
023284         10  WS-NXT-CMPD-DT       PIC 9(08).                      
023286         10  WS-CUR-PRS-EFF-DT    PIC 9(08).                      
023288         10  WS-TDAA-INTERVAL     PIC 9(03).                      
023290         10  WS-NBR-DAYS          PIC S9(05).                     
023292         10  WS-CMPD-PER-INT      PIC S9(12)V9(06).               
023294         10  WS-CMPD-INT          PIC S9(12)V99.                  
023296         10  WS-ACCR-DT           PIC 9(08).                      
023298         10  WS-YIELD-DENOM       PIC 9(03).                      
023300         10  WS-YIELD-NUM         PIC 9(03).                      
023302         10  WS-START-DATE        PIC 9(08).                      
023304         10  WS-FINISH-DATE       PIC 9(08).                      
023306         10  WS-ACCR-END-DT       PIC 9(08).                      
023308         10  WS-PER-DIEM          PIC S9(12)V9(06).               
023310         10  WS-ACCR-INT          PIC S9(12)V9(06).               
023312         10  WS-NXT-POST-DT       PIC 9(08).                      
023314                                                                  
023316     05  WS-TDAA-INT-IN-PRC.                                      
023318         10  WS-WITHHOLD-RATE-TABLE.                              
023320             15  FILLER              PIC 9(08)    VALUE 20062800. 
023322             15  FILLER              PIC 9(08)    VALUE 20182400. 
023324         10  WS-WITHHOLD-RT-TABLE REDEFINES WS-WITHHOLD-RATE-TABLE
023326                                     OCCURS 2 TIMES.              
023328             15  WS-WTHLD-YEAR       PIC 9(04).                   
023330             15  WS-WTHLD-RATE       PIC 99V99.                   
023332             15  WS-WTHLD-PERCENT REDEFINES WS-WTHLD-RATE         
023334                                     PIC   V9(04).                
023336         10  WS-WTHLD-INDEX          PIC 99.                      
023338         10  WS-WTHLD-MAX-INDEX      PIC 99         VALUE 02.     
023340         10  WS-TDAA-NXT-POST-DT     PIC 9(08).                   
023342         10  WS-NXT-IN-PRC-DT        PIC 9(08).                   
023344         10  WS-MAX-DAYS             PIC 9(02)      VALUE 15.     
023346         10  WS-WITHHOLD-AMT         PIC S9(12)V99.               
023348         10  WS-ST-WHLD-AMT          PIC S9(12)V99.               
023350         10  WS-DAY-OF-WEEK          PIC X(03).                   
023352         10  WS-IN-PROCESS-DAY       PIC X(03)      VALUE "FRI".  
023354                                                                  
023356     05  WS-PENALTY-FIELDS.                                       
023358         10  WS-PEN-LST-POST-DT      PIC 9(08).                   
023360         10  WS-PEN-CURR-BAL         PIC S9(12)V99.               
023362         10  WS-PEN-NXT-POST-DT      PIC 9(08).                   
023364         10  WS-PEN-DAYS-INTO-PER    PIC 9(4).                    
023366         10  WS-PEN-DAYS-IN-PER      PIC 9(4).                    
023368         10  WS-PEN-NXT-IN-PROC      PIC 9(08).                   
023370         10  WS-PEN-PENALTY-AMT      PIC 9(12)V99.                
023372         10  WS-PEN-AMOUNT           PIC 9(12)V99.                
023374         10  WS-PEN-PERCENT          PIC 9(02)V999.               
023376         10  WS-PEN-FUNC             PIC X         VALUE SPACE.   
023378         10  WS-PEN-FUNC-DESC        PIC X(14)     VALUE SPACES.  
023380         10  WSP-FLAG                PIC 9(04)     VALUE 0.       
023382         10  WSP-FLAG-A              REDEFINES  WSP-FLAG.         
023384             15  WSP-FLAG-AMOUNT     PIC 9(01).                   
023386             15  WSP-FLAG-MAT-INT    PIC 9(01).                   
023388             15  WSP-FLAG-REN-DT     PIC 9(01).                   
023390             15  WSP-FLAG-DT         PIC 9(01).                   
023392                                                                  
023394         10  WSP-FLAG-B               PIC 9(01).                  
023396                                                                  
023398     05  WS-TDAA-INT-POSTING.                                     
023400         10  WS-ACCR-ADJ             PIC S9(12)V9(06).            
023402         10  WS-POST-INT             PIC S9(12)V99.               
023404                                                                  
023406     05  WS-OLD-NEW-ANTIC-INT.                                    
023408         10  WS-OLD-ANTIC-INT        PIC S9(12)V99.               
023410         10  WS-NEW-ANTIC-INT        PIC S9(12)V99.               
023412                                                                  
023414     05  WS-TDAA-DISTR.                                           
023416         10  WS-AMT                  PIC 9(12)V99.                
023418         10  WS-DIST-DIFF            PIC 9(12)V99.                
023420         10  WS-DIST-TOT             PIC 9(15)V99.                
023422         10  WS-DIST-PRINCPL-AMT     PIC S9(12)V99.               
023424         10  WS-DIST-NXT-DIST-DT     PIC 9(8).                    
023426         10  WS-DIST-CALC-ANTIC      PIC 9.                       
023428                                                                  
023430     05  WS-DS-AVAIL-BAL             PIC S9(12)V99.               
023432     05  WS-SAVE-AVAIL-BAL           PIC S9(12)V99.               
023434                                                                  
023436     05  WS-APY-CALC.                                             
023438         10  WS-APY-QUO              PIC 9(4)        VALUE 0.     
023440         10  WS-APY-REM              PIC 9(4)        VALUE 0.     
023442         10  WS-APY                  PIC 9(04)V99.                
023444         10  WS-APY-INT              PIC 9(12)V9(06).             
023446         10  WS-APY-FLAG             PIC 9(01)       VALUE 0.     
023448         10  WS-FREQ-MONTHS          PIC 9(03).                   
023450         10  WS-APY-START            PIC 9(08).                   
023452         10  WS-APY-END              PIC 9(08).                   
023454         10  WS-APY-BAL              PIC S9(12)V99.               
023456         10  WS-APY-YIELD            PIC S99V999.                 
023458         10  WS-PAY-DATE             PIC 9(06).                   
023460         10  WS-PAY-DATE2            PIC 9(06).                   
023462         10  WS-APY-INT-HOLD         PIC 9(12)V99.                
023464         10  WS-FREQ-DAYS            PIC 9(04).                   
023466         10  WS-FREQ-DAYS-HOLD       PIC 9(04).                   
023468         10  WS-INT-INTVL            PIC 9(04)       VALUE 0.     
023470         10  WS-RED-INTVL            PIC 9(04)       VALUE 0.     
023472                                                                  
023474         10  WS-ACCT-DAILY-COMP      PIC 9(04)       VALUE 0.     
023476             88  ACCT-DAILY-COMP                     VALUE 1.     
023478                                                                  
023480         10  WS-TDA-APY-FLAG         PIC 9(01)       VALUE 0.     
023482             88  WS-TDA-DAYS                         VALUE 1.     
023484             88  WS-TDA-MONTHS                       VALUE 2.     
023486                                                                  
023488     05  WS-COMBINE-CHECKS.                                       
023490         10  WS-CHG-CURR              PIC 9(02).                  
023492         10  WS-CHG-OLD               PIC 9(02).                  
023494         10  WS-HOLD-TBL-CUST.                                    
023496             15  WS-HOLD-TBL-CUSTOMER OCCURS 10 TIMES.            
023498                 20  WS-HOLD-TDACK-CUST   PIC 9(12).              
023500                 20  WS-HOLD-TDACK-ACCT   PIC 9(10).              
023502         10  WS-DUPL-TDACK-CUST           PIC 9(12).              
023504         10  WS-DUPL-TDACK-ACCT           PIC 9(10).              
023506                                                                  
023508     05  WS-ACTVC-CODE            PIC 9(04).                      
023510     05  WS-ACTVC-CHG-FRM         PIC X(40).                      
023512     05  WS-ACTVC-CHG-TO          PIC X(40).                      
023514     05  WS-ACTVC-CHG-FRM-XLATE.                                  
023516         10  WS-ACTVC-CHG-FRM-XLATE-X PIC X(40).                  
023518     05  WS-ACTVC-CHG-TO-XLATE.                                   
023520         10  WS-ACTVC-CHG-TO-XLATE-X  PIC X(40).                  
023522     05  WS-ACTVC-LEF.                                            
023524         10 WS-ACTVC-LEF-X            PIC X(40).                  
023526         10 WS-ACTVC-LEF1-R REDEFINES WS-ACTVC-LEF-X.             
023528            15 FILLER                       PIC X(36).            
023530            15 WS-ACTVC-LEF-FORMATED        PIC 99.9.             
023532                                                                  
023534     05  9-FIELD                  PIC S9(16)V99.                  
023536     05  9-FIELD-NS               PIC 9(16)V99.                   
023538     05  9-FIELD-V3               PIC S9(15)V999.                 
023540     05  9-FIELD-V3-NS            PIC 9(15)V999.                  
023542     05  9-FIELD-V4               PIC S9(14)V9999.                
023544     05  9-FIELD-V4-NS            PIC 9(14)V9999.                 
023546     05  9-FIELD-V6               PIC S9(12)V9(6).                
023548     05  9-FIELD-V6-NS            PIC 9(12)V9(6).                 
023550                                                                  
023552     05  WS-EIRA-DATE             PIC 9(08).                      
023554                                                                  
023556     05  WS-HOLD-NBR              PIC 99                          
023558                                  OCCURS 99 TIMES.                
023560     05  WS-TRANS-AMT-X.                                          
023562         10  WS-TRANS-AMT         PIC S9(12)V99.                  
023564                                                                  
023566     05  WS-TRANS-RT-X.                                           
023568         10  WS-TRANS-RT          PIC 9(2)V9(3).                  
023570                                                                  
023572     05  WS-HOLDS-AMT-X.                                          
023574         10  WS-HOLDS-AMT         PIC S9(12)V99.                  
023576                                                                  
023578     05  WS-ACTV-SEQ-NBR          PIC 9(02)          VALUE 0.     
023580                                                                  
023582     05  WS-QUOTIENT              PIC 9(04)          VALUE 0.     
023584     05  WS-REMAINDER             PIC 9(04)          VALUE 0.     
023586                                                                  
023588     05  WS-DESC                  PIC X(72).                      
023590                                                                  
023592     05  WS-ACTION                PIC X(01).                      
023594                                                                  
023596     05  WS-FILE-MAINT.                                           
023598         10  INPUT-DATA           PIC X(40).                      
023600         10  IRA-FLG              PIC 9(01).                      
023602         10  ACCT-FLG             PIC 9(01).                      
023604                                                                  
023606     05  WS-MESSAGE-NBR           PIC 9(04).                      
023608     05  WS-MESSAGE               PIC X(65).                      
023610     05  WS-ERROR-NBR             PIC 9(04).                      
023612      05  WS-UNSIGNED-ADJUST       PIC 9(09)V99.                  
023614                                                                  
023616     05  WS-NEXT-DATE.                                            
023618         10  WS-FREQUENCY         PIC 9(04).                      
023620         10  WS-FREQUENCY-TYPE    PIC 9(01).                      
023622         10  WS-RSLT-DT           PIC 9(08).                      
023624         10  WS-NXT-DATE-CYMD.                                    
023626             15  WS-NXT-DATE-CY             PIC 9(04).            
023628             15  WS-NXT-DATE-CY-R REDEFINES WS-NXT-DATE-CY.       
023630                 20 WS-NXT-DATE-CC          PIC 99.               
023632                 20 WS-NXT-DATE-YY          PIC 99.               
023634             15  WS-NXT-DATE-MD             PIC 9(04).            
023636             15  WS-NXT-DATE-MD-R REDEFINES WS-NXT-DATE-MD.       
023638                 20 WS-NXT-DATE-MM          PIC 99.               
023640                 20 WS-NXT-DATE-DD          PIC 99.               
023642                                                                  
023644     05  WS-NXT-DT                PIC 9(08).                      
023646     05  WS-CUR-DT                PIC 9(08).                      
023648     05  WS-TIN-CONVERT.                                          
023650         10  WS-TIN-BEFORE        PIC 9(09).                      
023652         10  WS-TIN-MASK          REDEFINES WS-TIN-BEFORE.        
023654             15  WS-E-TIN.                                        
023656                 20  WS-E2        PIC 9(02).                      
023658                 20  WS-E7        PIC 9(07).                      
023660             15  WS-S-TIN         REDEFINES WS-E-TIN.             
023662                 20  WS-S3        PIC 9(03).                      
023664                 20  WS-S2        PIC 9(02).                      
023666                 20  WS-S4        PIC 9(04).                      
023668         10  WS-TIN               PIC X(11).                      
023670                                                                  
023672     05  WS-INTERVAL-CONVERT.                                     
023674         10  WS-TYPE-CD           PIC 9(01).                      
023676         10  WS-INTERVAL          PIC X(01).                      
023678                                                                  
023680     05  WS-TOTAL-TYPE-CD.                                        
023682         10  WS-TYPE-12-34.                                       
023684             15  WS-TYPE-12       PIC X(2).                       
023686             15  WS-TYPE-34       PIC X(3).                       
023688         10  WS-TYPE-1-24  REDEFINES  WS-TYPE-12-34.              
023690             15  WS-TYPE-1        PIC X(2).                       
023692             15  WS-TYPE-24       PIC X(3).                       
023694         10  WS-TYPE-13-4  REDEFINES  WS-TYPE-12-34.              
023696             15  WS-TYPE-13       PIC X(4).                       
023698             15  WS-TYPE-4        PIC X(1).                       
023700     05  WS-TOTAL-TYPE-CD-NEW.                                    
023702         10  WS-TYPE-CD-11.                                       
023704             15 WS-TYPE-CD-1      PIC X(1).                       
023706             15 WS-TYPE-CD-23     PIC X(2).                       
023708             15 WS-TYPE-CD-4567   PIC X(4).                       
023710             15 FILLER            PIC X(4).                       
023712         10  WS-TYPE-CD-12345-67-8901 REDEFINES WS-TYPE-CD-11.    
023714             15 WS-TYPE-CD-12345  PIC X(5).                       
023716             15 WS-TYPE-CD-67     PIC X(2).                       
023718             15 FILLER            PIC X(4).                       
023720         10  WS-TYPE-CD-123456-7-8901 REDEFINES WS-TYPE-CD-11.    
023722             15 WS-TYPE-CD-123456 PIC X(6).                       
023724             15 WS-TYPE-CD-7      PIC X(1).                       
023726             15 FILLER            PIC X(4).                       
023728         10  WS-TYPE-CD-1234-567-8901 REDEFINES WS-TYPE-CD-11.    
023730             15 WS-TYPE-CD-1234   PIC X(4).                       
023732             15 WS-TYPE-CD-567    PIC X(3).                       
023734             15 FILLER            PIC X(4).                       
023736         10  WS-TYPE-CD-1234567-8901 REDEFINES WS-TYPE-CD-11.     
023738             15 FILLER            PIC X(1).                       
023740             15 WS-TYPE-CD-234567 PIC X(6).                       
023742             15 FILLER            PIC X(4).                       
023744     05  WS-TOTAL-TYPE-CD-LGB.                                    
023746         10  FILLER                PIC X(1).                      
023748         10  WS-TYPE-CD-LGB-2345   PIC X(4).                      
023750         10  WS-TYPE-CD-LGB-678901 PIC X(6).                      
023752                                                                  
023754     05  WS-DISP-CONVERT.                                         
023756         10  WS-DISP-CODE         PIC 9(01).                      
023758         10  WS-DISP-DESC         PIC X(03).                      
023760                                                                  
023762     05  WS-CUR-INT-RT-X.                                         
023764         10  WS-CUR-INT-RT        PIC S99V999.                    
023766     05  WS-BASE-RT-X.                                            
023768         10 WS-BASE-RT            PIC S99V999.                    
023770     05  WS-STEPPED-RATE-VARIABLES.                               
023772         10  WS-CURR-STEP-RATE    PIC  99V999.                    
023774         10  WS-CURR-STEP-DATE    PIC 9(08).                      
023776         10  WS-CURR-CYCLE-NBR    PIC 99.                         
023778                                                                  
023780     05  WS-HOLD-CHG-CODE         PIC 9(006).                     
023782     05  WS-HOLD-CHG-CODE-R  REDEFINES WS-HOLD-CHG-CODE.          
023784         10  WS-CHANGE-CODE       PIC 9(004)V99.                  
023786     05  WS-CHG-WORK-EXP          PIC X(100).                     
023788     05  WS-CHG-WORK              PIC X(040).                     
023790     05  WS-CHG-WORK-R1      REDEFINES WS-CHG-WORK.               
023792         10  WS-CHG-WK-X-1        PIC X(001).                     
023794         10  FILLER               PIC X(039).                     
023796     05  WS-CHG-WORK-R2      REDEFINES WS-CHG-WORK.               
023798         10  WS-CHG-WK-X-2        PIC X(002).                     
023800         10  FILLER               PIC X(038).                     
023802     05  WS-CHG-WORK-R3      REDEFINES WS-CHG-WORK.               
023804         10  WS-CHG-WK-X-3        PIC X(003).                     
023806         10  FILLER               PIC X(037).                     
023808     05  WS-CHG-WORK-R4      REDEFINES WS-CHG-WORK.               
023810         10  WS-CHG-WK-X-4        PIC X(004).                     
023812         10  FILLER               PIC X(036).                     
023814     05  WS-CHG-WORK-R5      REDEFINES WS-CHG-WORK.               
023816         10  WS-CHG-WK-X-5        PIC X(005).                     
023818         10  FILLER               PIC X(035).                     
023820     05  WS-CHG-WORK-R6      REDEFINES WS-CHG-WORK.               
023822         10  WS-CHG-WK-X-6        PIC X(006).                     
023824         10  FILLER               PIC X(034).                     
023826     05  WS-CHG-WORK-R30     REDEFINES WS-CHG-WORK.               
023828         10  WS-CHG-WK-X-8        PIC X(008).                     
023830         10  FILLER               PIC X(032).                     
023832     05  WS-CHG-WORK-R35     REDEFINES WS-CHG-WORK.               
023834         10  WS-CHG-WK-X-9        PIC X(009).                     
023836         10  FILLER               PIC X(031).                     
023838     05  WS-CHG-WORK-R7      REDEFINES WS-CHG-WORK.               
023840         10  WS-CHG-WK-X-10       PIC X(010).                     
023842         10  FILLER               PIC X(030).                     
023844     05  WS-CHG-WORK-R79     REDEFINES WS-CHG-WORK.               
023846         10  WS-CHG-WK-X-12       PIC X(012).                     
023848         10  FILLER               PIC X(028).                     
023850     05  WS-CHG-WORK-R46     REDEFINES WS-CHG-WORK.               
023852         10  WS-CHG-WK-X-14       PIC X(14).                      
023854         10  FILLER               PIC X(26).                      
023856     05  WS-CHG-WORK-R8      REDEFINES WS-CHG-WORK.               
023858         10  WS-CHG-WK-X-20       PIC X(020).                     
023860         10  FILLER               PIC X(020).                     
023862     05  WS-CHG-WORK-R9      REDEFINES WS-CHG-WORK.               
023864         10  WS-CHG-WK-X-24       PIC X(024).                     
023866         10  FILLER               PIC X(016).                     
023868     05  WS-CHG-WORK-R49     REDEFINES WS-CHG-WORK.               
023870         10  WS-CHG-WK-X-25       PIC X(025).                     
023872         10  FILLER               PIC X(015).                     
023874     05  WS-CHG-WORK-R45     REDEFINES WS-CHG-WORK.               
023876         10  WS-CHG-WK-X-28       PIC X(28).                      
023878         10  FILLER               PIC X(12).                      
023880     05  WS-CHG-WORK-R38     REDEFINES WS-CHG-WORK.               
023882         10  WS-CHG-WK-X-29       PIC X(29).                      
023884         10  FILLER               PIC X(11).                      
023886     05  WS-CHG-WORK-R10     REDEFINES WS-CHG-WORK.               
023888         10  FILLER               PIC X(039).                     
023890         10  WS-CHG-WK-9-1        PIC 9(001).                     
023892     05  WS-CHG-WORK-R11     REDEFINES WS-CHG-WORK.               
023894         10  FILLER               PIC X(038).                     
023896         10  WS-CHG-WK-9-2        PIC 9(002).                     
023898     05  WS-CHG-WORK-R12     REDEFINES WS-CHG-WORK.               
023900         10  FILLER               PIC X(037).                     
023902         10  WS-CHG-WK-9-3        PIC 9(003).                     
023904     05  WS-CHG-WORK-R13     REDEFINES WS-CHG-WORK.               
023906         10  FILLER               PIC X(036).                     
023908         10  WS-CHG-WK-9-4        PIC 9(004).                     
023910     05  WS-CHG-WORK-R14     REDEFINES WS-CHG-WORK.               
023912         10  FILLER               PIC X(035).                     
023914         10  WS-CHG-WK-9-5        PIC 9(005).                     
023916     05  WS-CHG-WORK-R15     REDEFINES WS-CHG-WORK.               
023918         10  FILLER               PIC X(034).                     
023920         10  WS-CHG-WK-9-6        PIC 9(006).                     
023922     05  WS-CHG-WORK-R31     REDEFINES WS-CHG-WORK.               
023924         10  FILLER               PIC X(033).                     
023926         10  WS-CHG-WK-9-7        PIC 9(007).                     
023928     05  WS-CHG-WORK-R16     REDEFINES WS-CHG-WORK.               
023930         10  FILLER               PIC X(032).                     
023932         10  WS-CHG-WK-9-8        PIC 9(008).                     
023934     05  WS-CHG-WORK-R17     REDEFINES WS-CHG-WORK.               
023936         10  FILLER               PIC X(031).                     
023938         10  WS-CHG-WK-9-9        PIC 9(009).                     
023940     05  WS-CHG-WORK-R18     REDEFINES WS-CHG-WORK.               
023942         10  FILLER               PIC X(030).                     
023944         10  WS-CHG-WK-9-10       PIC 9(010).                     
023946     05  WS-CHG-WORK-R19     REDEFINES WS-CHG-WORK.               
023948         10  FILLER               PIC X(028).                     
023950         10  WS-CHG-WK-9-12       PIC 9(012).                     
023952     05  WS-CHG-WORK-R20     REDEFINES WS-CHG-WORK.               
023954         10  FILLER               PIC X(030).                     
023956         10  WS-CHG-WK-9-8V2      PIC 9(008)V99.                  
023958     05  WS-CHG-WORK-R21     REDEFINES WS-CHG-WORK.               
023960         10  FILLER               PIC X(030).                     
023962         10  WS-CHG-WK-9-S8V2     PIC S9(008)V99.                 
023964     05  WS-CHG-WORK-R37     REDEFINES WS-CHG-WORK.               
023966         10  FILLER               PIC X(037).                     
023968         10  WS-CHG-WK-9-S1V2     PIC S9V99.                      
023970     05  WS-CHG-WORK-R42     REDEFINES WS-CHG-WORK.               
023972         10  FILLER               PIC X(037).                     
023974         10  WS-CHG-WK-9-2V1      PIC 99V9.                       
023976     05  WS-CHG-WORK-R22     REDEFINES WS-CHG-WORK.               
023978         10  FILLER               PIC X(035).                     
023980         10  WS-CHG-WK-9-2V3      PIC 9(002)V999.                 
023982     05  WS-CHG-WORK-R39     REDEFINES WS-CHG-WORK.               
023984         10  FILLER               PIC X(035).                     
023986         10  WS-CHG-WK-9-S2V3     PIC S9(002)V999.                
023988     05  WS-CHG-WORK-R23     REDEFINES WS-CHG-WORK.               
023990         10  FILLER               PIC X(034).                     
023992         10  WS-CHG-WK-9-2V4      PIC 9(002)V9999.                
023994     05  WS-CHG-WORK-R24     REDEFINES WS-CHG-WORK.               
023996         10  FILLER               PIC X(032).                     
023998         10  WS-CHG-WK-9-2V6      PIC 9(002)V999999.              
024000     05  WS-CHG-WORK-R32     REDEFINES WS-CHG-WORK.               
024002         10  FILLER               PIC X(034).                     
024004         10  WS-CHG-WK-9-4V2      PIC 9(004)V99.                  
024006     05  WS-CHG-WORK-R36     REDEFINES WS-CHG-WORK.               
024008         10  FILLER               PIC X(033).                     
024010         10  WS-CHG-WK-9-5V2      PIC 9(005)V99.                  
024012     05  WS-CHG-WORK-R25     REDEFINES WS-CHG-WORK.               
024014         10  FILLER               PIC X(030).                     
024016         10  WS-CHG-WK-9-6V4      PIC 9(006)V9999.                
024018     05  WS-CHG-WORK-R26     REDEFINES WS-CHG-WORK.               
024020         10  FILLER               PIC X(030).                     
024022         10  WS-CHG-WK-9-S6V4     PIC S9(006)V9999.               
024024     05  WS-CHG-WORK-R27     REDEFINES WS-CHG-WORK.               
024026         10  FILLER               PIC X(029).                     
024028         10  WS-CHG-WK-9-S9V2     PIC S9(009)V99.                 
024030     05  WS-CHG-WORK-R28     REDEFINES WS-CHG-WORK.               
024032         10  FILLER               PIC X(027).                     
024034         10  WS-CHG-WK-9-S11V2    PIC S9(011)V99.                 
024036     05  WS-CHG-WORK-R41     REDEFINES WS-CHG-WORK.               
024038         10  FILLER               PIC X(26).                      
024040         10  WS-CHG-WK-9-S12V2    PIC S9(12)V99.                  
024042     05  WS-CHG-WORK-R34     REDEFINES WS-CHG-WORK.               
024044         10  FILLER               PIC X(025).                     
024046         10  WS-CHG-WK-9-13V2     PIC 9(013)V99.                  
024048     05  WS-CHG-WORK-R33     REDEFINES WS-CHG-WORK.               
024050         10  FILLER               PIC X(025).                     
024052         10  WS-CHG-WK-9-S13V2    PIC S9(013)V99.                 
024054     05  WS-CHG-WORK-R29     REDEFINES WS-CHG-WORK.               
024056         10  WS-CHG-WK-CC         PIC 9(002).                     
024058         10  WS-CHG-WK-YY         PIC 9(002).                     
024060         10  WS-CHG-WK-MM         PIC 9(002).                     
024062         10  WS-CHG-WK-DD         PIC 9(002).                     
024064         10  FILLER               PIC X(032).                     
024066     05  WS-CHG-WORK-R40    REDEFINES WS-CHG-WORK.                
024068         10  FILLER               PIC X(023).                     
024070         10  WS-CHG-WK-9-S15V2    PIC S9(015)V99.                 
024072     05  WS-CHG-WORK-R43    REDEFINES WS-CHG-WORK.                
024074         10  FILLER               PIC X(022).                     
024076         10  WS-CHG-WK-9-S12V6    PIC S9(012)V9(06).              
024078     05  WS-CHG-WORK-R44    REDEFINES WS-CHG-WORK.                
024080         10  FILLER               PIC X(024).                     
024082         10  WS-CHG-WK-9-S12V4    PIC S9(012)V9(04).              
024084     05  WS-CHG-WORK-R47    REDEFINES WS-CHG-WORK.                
024086         10  WS-CHG-WK-X-22       PIC X(022).                     
024088         10  FILLER               PIC X(018).                     
024090     05  WS-CHG-WORK-R48    REDEFINES WS-CHG-WORK.                
024092         10  FILLER               PIC X(32).                      
024094         10  WS-CHG-WK-9-S6V2     PIC S9(6)V9(2).                 
024096                                                                  
024098     05  WS-TRCD                  PIC 9(004)   COMP VALUE ZEROES. 
024100         88  CREDIT-TRANS         VALUE 31 113 114 115 116 117 118
024102             119 120 121 122 123 124 128 129.                     
024104     05  WS-MODDER                PIC 9(01).                      
024106     05  WS-MODDER2               PIC 9(04).                      
024108         88  DEBIT-TRANS          VALUE 39 110 132 133 135 137 138
024110               139 140 141 142 143 144 145 146 147 148 149 151 152
024112               153 154 155.                                       
024114         88  IRA-CONTRIB          VALUE 31 113 118.               
024116         88  IRA-DISTRIB          VALUE 132 133 135 139 141 142   
024118                                        146 151 155.              
024120         88  CLOSING-TRANS        VALUE 110 111.                  
024122         88  REQ-STMT             VALUE 112.                      
024124         88  REQ-HOLD             VALUE 035 036.                  
024126                                                                  
024128     05  HOLD-DATE-MDY            PIC 9(06).                      
024130     05  HOLD-RATE-X.                                             
024132         10  HOLD-RATE            PIC S99V999.                    
024134     05  HOLD-EFF-DATE            PIC 9(08).                      
024136     05  HOLD-END-DATE            PIC 9(08).                      
024138     05  HOLD-CYC-INCREMENT.                                      
024140         10  HOLD-CYC-INC1        PIC S99V999.                    
024142         10  HOLD-CYC-INC2        PIC S99V999.                    
024144         10  HOLD-CYC-INC3        PIC S99V999.                    
024146         10  HOLD-CYC-INC4        PIC S99V999.                    
024148         10  HOLD-CYC-INC5        PIC S99V999.                    
024150         10  HOLD-CYC-INC6        PIC S99V999.                    
024152         10  HOLD-CYC-INC7        PIC S99V999.                    
024154         10  HOLD-CYC-INC8        PIC S99V999.                    
024156         10  HOLD-CYC-INC9        PIC S99V999.                    
024158         10  HOLD-CYC-INC10       PIC S99V999.                    
024160                                                                  
024162     05  HOLD-TIER-BALANCE.                                       
024164         10  HOLD-TIER-BAL1       PIC 9(12)V99.                   
024166         10  HOLD-TIER-BAL2       PIC 9(12)V99.                   
024168         10  HOLD-TIER-BAL3       PIC 9(12)V99.                   
024170         10  HOLD-TIER-BAL4       PIC 9(12)V99.                   
024172         10  HOLD-TIER-BAL5       PIC 9(12)V99.                   
024174         10  HOLD-TIER-BAL6       PIC 9(12)V99.                   
024176         10  HOLD-TIER-BAL7       PIC 9(12)V99.                   
024178         10  HOLD-TIER-BAL8       PIC 9(12)V99.                   
024180         10  HOLD-TIER-BAL9       PIC 9(12)V99.                   
024182         10  HOLD-TIER-BAL10      PIC 9(12)V99.                   
024184         10  HOLD-TIER-BAL11      PIC 9(12)V99.                   
024186         10  HOLD-TIER-BAL12      PIC 9(12)V99.                   
024188         10  HOLD-TIER-BAL13      PIC 9(12)V99.                   
024190         10  HOLD-TIER-BAL14      PIC 9(12)V99.                   
024192         10  HOLD-TIER-BAL15      PIC 9(12)V99.                   
024194                                                                  
024196     05  HOLD-TIER-INCREMENT.                                     
024198         10  HOLD-TIER-INCR1      PIC S99V999.                    
024200         10  HOLD-TIER-INCR2      PIC S99V999.                    
024202         10  HOLD-TIER-INCR3      PIC S99V999.                    
024204         10  HOLD-TIER-INCR4      PIC S99V999.                    
024206         10  HOLD-TIER-INCR5      PIC S99V999.                    
024208         10  HOLD-TIER-INCR6      PIC S99V999.                    
024210         10  HOLD-TIER-INCR7      PIC S99V999.                    
024212         10  HOLD-TIER-INCR8      PIC S99V999.                    
024214         10  HOLD-TIER-INCR9      PIC S99V999.                    
024216         10  HOLD-TIER-INCR10     PIC S99V999.                    
024218         10  HOLD-TIER-INCR11     PIC S99V999.                    
024220         10  HOLD-TIER-INCR12     PIC S99V999.                    
024222         10  HOLD-TIER-INCR13     PIC S99V999.                    
024224         10  HOLD-TIER-INCR14     PIC S99V999.                    
024226         10  HOLD-TIER-INCR15     PIC S99V999.                    
024228                                                                  
024230     05  KEY-DATA.                                                
024232         10 KEY-RPT-NBR           PIC 9(04).                      
024234         10 KEY-REGION            PIC 9(01).                      
024236         10 KEY-CODE              PIC 9(03).                      
024238         10 KEY-DATE              PIC 9(08).                      
024240                                                                  
024242     05  TDA-ONLACT-FILE-ID.                                      
024244         10  FILLER               PIC X(05) VALUE "TDA0B".        
024246         10  TDA-ONLACT-DATE-MMDD PIC 9(04).                      
024248         10  FILLER               PIC X(07) VALUE "/ONLACT".      
024250         10  TDA-ONLACT-SUFFIX    PIC X(01) VALUE SPACE.          
024252         10  FILLER               PIC X(01) VALUE "/".            
024254         10  TDA-ONLACT-TIME      PIC 9(08).                      
024256         10  FILLER               PIC X(01) VALUE ".".            
024258                                                                  
024260     05  TDA-PCR-I                PIC 9(03).                      
024262     05  TDA-PCR-RPT-NUM          PIC 9(03).                      
024264     05  TDA-PCR-REQ              PIC 9(01).                      
024266     05  TDA-PCR-RPT-TYPE         PIC 9(01).                      
024268     05  TDA-PCR-USE-PILOT        PIC 9(01).                      
024270     05  TDA-PILOT-TYPE           PIC X(01).                      
024272     05  WS-HOLD-CN-TYPE-EX       PIC 9(02).                      
024274     05  WS-SKIP-OPEN-TRANS       PIC 9.                          
024276     05  WS-CALC-BANK             PIC 9(04).                      
024278     05  WS-CALC-CUST             PIC 9(10).                      
024280     05  WS-CALC-ACCT             PIC 9(12).                      
024282     05  WS-CALC-LST-DT           PIC 9(08).                      
024284     05  WS-CALC-NXT-DT           PIC 9(08).                      
024286     05  WS-CALC-CURR-BAL         PIC S9(12)V99.                  
024288     05  WS-CALC-AMT              PIC S9(12)V99.                  
024290                                                                  
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 699 lines from 11443 to 12141.

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

