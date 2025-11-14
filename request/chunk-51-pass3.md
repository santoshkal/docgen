# LLM Request Debug File
Generated: 2025-11-13T21:58:26.211334

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 51/55
- **Model**: gpt-4.1
- **Chunk Number**: 51
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~9,293 tokens
- **Total Input**: ~11,251 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 51/55" (ID: detailed-code-explanation)

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


**CHUNK 51 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 51 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 24376 to 24925 (550 lines)\nChunk Tokens (estimated): ~8,057\nActual Input Tokens: 9,463 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 24376-24925 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 51 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 51 of 55.\n\n\n=============================================================================\nCHUNK 51 SOURCE CODE (Lines 24376-24925)\n=============================================================================\n\n```cobol\n048760         HOLD-TDAIRA.\n048762     MOVE TDAI-CN-LYTD-AMT OF TDAIRA TO HOLD-TDAI-CN-LYTD-AMT OF  \n048764         HOLD-TDAIRA.\n048766     MOVE TDAI-EMP-CONT-LYR OF TDAIRA TO HOLD-TDAI-EMP-CONT-LYR   \n048768         OF HOLD-TDAIRA.\n048770     MOVE TDAI-REG-CONT-LYR OF TDAIRA TO HOLD-TDAI-REG-CONT-LYR   \n048772         OF HOLD-TDAIRA.\n048774     MOVE TDAI-UNINSURED OF TDAIRA TO HOLD-TDAI-UNINSURED OF      \n048776         HOLD-TDAIRA.\n048778     MOVE TDAI-ROLLOVER OF TDAIRA TO HOLD-TDAI-ROLLOVER OF        \n048780         HOLD-TDAIRA.\n048782     MOVE TDAI-ROLLOVER-LYR OF TDAIRA TO HOLD-TDAI-ROLLOVER-LYR   \n048784         OF HOLD-TDAIRA.\n048786     MOVE TDAI-TRANSFER-IN OF TDAIRA TO HOLD-TDAI-TRANSFER-IN OF  \n048788         HOLD-TDAIRA.\n048790     MOVE TDAI-TRANSFER-OUT OF TDAIRA TO HOLD-TDAI-TRANSFER-OUT   \n048792         OF HOLD-TDAIRA.\n048794     MOVE TDAI-1ST-CN-DATE OF TDAIRA TO HOLD-TDAI-1ST-CN-DATE OF  \n048796         HOLD-TDAIRA.\n048798     MOVE TDAI-BASIS-C-LTD OF TDAIRA TO HOLD-TDAI-BASIS-C-LTD OF  \n048800         HOLD-TDAIRA.\n048802     MOVE TDAI-BASIS-D-LTD OF TDAIRA TO HOLD-TDAI-BASIS-D-LTD OF  \n048804         HOLD-TDAIRA.\n048806     MOVE TDAI-BASIS-D-YTD OF TDAIRA TO HOLD-TDAI-BASIS-D-YTD OF  \n048808         HOLD-TDAIRA.\n048810     MOVE TDB-READ-DATE TO HOLD-READ-DATE.\n048812     MOVE 00 TO TDB-STRUCT-NBR.\n048814     MOVE SPACES TO TDB-DATA-AREA.\n048816     MOVE ZERO TO Z-FLINFO14-PRES.\n048818     MOVE 17 TO Z-FLINFO14-LAST-SEQ.\n048820     MOVE ZERO TO Z-FLINFO14-SOME.\n048822     SET TDAACTVBKSET OF TDAACTV OF LDBTDADB TO ENDING\n048824         ON EXCEPTION\n048826         MOVE \"TDAACTVBKSET OF TDAACTV OF LDBTDADB\" TO            \n048828             Z-DMS-EXCEPT-STR\n048830         MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n048832         MOVE 17 TO Z-DMS-EXCEPT-SEQ\n048834         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT\n048836         GO TO Z-33-5-XIT.\n048838 Z-33-5-READ.\n048840     FIND TDAACTV OF LDBTDADB VIA PRIOR TDAACTVBKSET OF TDAACTV   \n048842         OF LDBTDADB\n048844     AT TDA-ACTV-BANK = HOLD-TDAI-BANK AND\n048846        TDA-ACTV-CUST = HOLD-TDAI-CUST AND\n048848        TDA-ACTV-ACCT = HOLD-TDAI-ACCT\n048850         ON EXCEPTION\n048852         MOVE 17 TO Z-DMS-EXCEPT-SEQ\n048854         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n048856             GO TO Z-33-5-XIT\n048858         ELSE\n048860             MOVE \"TDAACTVBKSET OF TDAACTV OF LDBTDADB\" TO        \n048862                 Z-DMS-EXCEPT-STR\n048864             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n048866             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n048868\n048870 Z-33-5-PRESENT.\n048872*\n048874     MOVE 1 TO Z-FLINFO14-SOME.\n048876     MOVE 1 TO Z-FLINFO14-PRES.\n048878     GO TO Z-33-5-CONT.\n048880 Z-33-5-XIT.\n048882 Z-33-5-CONT.\n048884 Z-33-6-LOOP.\n048886     IF Z-FLINFO14-ABSENT OR TDA-ACTV-DATE < TDB-READ-DATE\n048888         GO TO Z-33-6-XIT.\n048890     MOVE 0 TO Z-EXIT-CODE.\n048892     MOVE 9999 TO Z-EXIT-LEVEL.\n048894     MOVE TDA-ACTV-BANK OF TDAACTV TO HOLD-TDA-ACTV-BANK OF       \n048896         HOLD-TDAACTV.\n048898     MOVE TDA-ACTV-BRCH OF TDAACTV TO HOLD-TDA-ACTV-BRCH OF       \n048900         HOLD-TDAACTV.\n048902     MOVE TDA-ACTV-APPL OF TDAACTV TO HOLD-TDA-ACTV-APPL OF       \n048904         HOLD-TDAACTV.\n048906     MOVE TDA-ACTV-CUST OF TDAACTV TO HOLD-TDA-ACTV-CUST OF       \n048908         HOLD-TDAACTV.\n048910     MOVE TDA-ACTV-ACCT OF TDAACTV TO HOLD-TDA-ACTV-ACCT OF       \n048912         HOLD-TDAACTV.\n048914     MOVE TDA-ACTV-TOT-CD OF TDAACTV TO HOLD-TDA-ACTV-TOT-CD OF   \n048916         HOLD-TDAACTV.\n048918     MOVE TDA-ACTV-IGL-GRP OF TDAACTV TO HOLD-TDA-ACTV-IGL-GRP OF \n048920         HOLD-TDAACTV.\n048922     MOVE TDA-ACTV-OFFICER OF TDAACTV TO HOLD-TDA-ACTV-OFFICER OF \n048924         HOLD-TDAACTV.\n048926     MOVE TDA-ACTV-NC-INDC OF TDAACTV TO HOLD-TDA-ACTV-NC-INDC OF \n048928         HOLD-TDAACTV.\n048930     MOVE TDA-ACTV-PROC-FG OF TDAACTV TO HOLD-TDA-ACTV-PROC-FG OF \n048932         HOLD-TDAACTV.\n048934     MOVE TDA-ACTV-EFF-DT OF TDAACTV TO HOLD-TDA-ACTV-EFF-DT OF   \n048936         HOLD-TDAACTV.\n048938     MOVE TDA-ACTV-DATE OF TDAACTV TO HOLD-TDA-ACTV-DATE OF       \n048940         HOLD-TDAACTV.\n048942     MOVE TDA-ACTV-MAINT OF TDAACTV TO HOLD-TDA-ACTV-MAINT OF     \n048944         HOLD-TDAACTV.\n048946     MOVE TDA-ACTV-TIME OF TDAACTV TO HOLD-TDA-ACTV-TIME OF       \n048948         HOLD-TDAACTV.\n048950     MOVE TDA-ACTV-SEQ-NBR OF TDAACTV TO HOLD-TDA-ACTV-SEQ-NBR OF \n048952         HOLD-TDAACTV.\n048954     MOVE TDA-ACTV-SERIAL OF TDAACTV TO HOLD-TDA-ACTV-SERIAL OF   \n048956         HOLD-TDAACTV.\n048958     MOVE TDA-ACTV-SOURCE OF TDAACTV TO HOLD-TDA-ACTV-SOURCE OF   \n048960         HOLD-TDAACTV.\n048962     MOVE TDA-ACTV-ERASED OF TDAACTV TO HOLD-TDA-ACTV-ERASED OF   \n048964         HOLD-TDAACTV.\n048966     MOVE TDA-ACTV-DR-CR OF TDAACTV TO HOLD-TDA-ACTV-DR-CR OF     \n048968         HOLD-TDAACTV.\n048970     MOVE TDA-ACTV-E-PUBID OF TDAACTV TO HOLD-TDA-ACTV-E-PUBID OF \n048972         HOLD-TDAACTV.\n048974     MOVE TDA-ACTV-PUB-ID OF TDAACTV TO HOLD-TDA-ACTV-PUB-ID OF   \n048976         HOLD-TDAACTV.\n048978     MOVE TDA-ACTV-SUB OF TDAACTV TO HOLD-TDA-ACTV-SUB OF         \n048980         HOLD-TDAACTV.\n048982     IF TDAACTV (TDA-ACTV-TYPE ) = 2\n048984         NEXT SENTENCE ELSE\n048986         GO TO Z-33-8-1-ELSE.\n048988     MOVE \"A\" TO WS-ADJUSTED-IND.\n048990     MOVE TDA-ACTVC-CODE TO HOLD-TDA-ACTVC-CODE.\n048992     MOVE TDA-ACTVC-EXCPT TO HOLD-TDA-ACTVC-EXCPT.\n048994     MOVE TDA-ACTVC-CHG-FRM TO HOLD-TDA-ACTVC-CHG-FRM.\n048996     MOVE TDA-ACTVC-CHG-TO TO HOLD-TDA-ACTVC-CHG-TO.\n048998     MOVE TDA-ACTVC-NCREOPN TO HOLD-TDA-ACTVC-NCREOPN.\n049000************ PERFORM TDB-ACTV-ADJUSTMENT\n049002     PERFORM Z-35-PROCEDURE THRU Z-35-XIT.\n049004     IF  Z-EXIT-EDITEXIT\n049006         GO TO Z-33-XIT.\n049008     IF  Z-DMS2-ABORT-FLAG = 1\n049010         GO TO Z-33-XIT.\n049012     IF  Z-EXIT-LEVEL < 0\n049014         GO TO Z-33-6-END.\n049016*\n049018 Z-33-8-1-ELSE.\n049020     MOVE ZERO TO Z-FLINFO14-PRES.\n049022     MOVE 18 TO Z-FLINFO14-LAST-SEQ.\n049024     MOVE ZERO TO Z-FLINFO14-SOME.\n049026 Z-33-16-READ.\n049028     FIND TDAACTV OF LDBTDADB VIA PRIOR TDAACTVBKSET OF TDAACTV   \n049030         OF LDBTDADB\n049032     AT TDA-ACTV-BANK = HOLD-TDAI-BANK AND\n049034        TDA-ACTV-CUST = HOLD-TDAI-CUST AND\n049036        TDA-ACTV-ACCT = HOLD-TDAI-ACCT\n049038         ON EXCEPTION\n049040         MOVE 18 TO Z-DMS-EXCEPT-SEQ\n049042         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n049044             GO TO Z-33-16-XIT\n049046         ELSE\n049048             MOVE \"TDAACTVBKSET OF TDAACTV OF LDBTDADB\" TO        \n049050                 Z-DMS-EXCEPT-STR\n049052             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n049054             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n049056\n049058 Z-33-16-PRESENT.\n049060*\n049062     MOVE 1 TO Z-FLINFO14-SOME.\n049064     MOVE 1 TO Z-FLINFO14-PRES.\n049066     GO TO Z-33-16-CONT.\n049068 Z-33-16-XIT.\n049070 Z-33-16-CONT.\n049072 Z-33-6-END.\n049074     IF Z-EDIT-ERROR\n049076         GO TO Z-33-XIT.\n049078 Z-33-6-SKIP.\n049080     IF Z-EXIT-LEVEL < 1\n049082         GO TO Z-33-END.\n049084     IF Z-EXIT-CODE > 0\n049086         GO TO Z-33-6-XIT.\n049088     GO TO Z-33-6-LOOP.\n049090*\n049092 Z-33-6-XIT.\n049094     MOVE 0 TO Z-EXIT-CODE.\n049096     MOVE 9999 TO Z-EXIT-LEVEL.\n049098 Z-33-END.\n049100     IF Z-EDIT-ERROR\n049102         GO TO Z-33-XIT.\n049104 Z-33-SKIP.\n049106     IF Z-EXIT-LEVEL NOT < 0\n049108         MOVE 0 TO Z-EXIT-CODE\n049110         MOVE 9999 TO Z-EXIT-LEVEL.\n049112 Z-33-XIT.\n049114     EXIT.\n049116*\n049118*****************************************************************\n049120*    PROCEDURE CALC-MINDIST-AMT\n049122*****************************************************************\n049124 Z-34-PROCEDURE.\n049126*\n049128     MOVE 0 TO Z-EXIT-CODE.\n049130     MOVE 9999 TO Z-EXIT-LEVEL.\n049132     MOVE SPACES TO WS-LE-FACTOR.\n049134     MOVE 0 TO WS-LE-FACT-1\n049136       , WS-LE-FACT-2.\n049138     COMPUTE WS-AGE-COUNT = ( WS-MD-AGE - 35 ) + 1 .\n049140\n049142     MOVE ZEROS TO WS-MD-AGE-DIFF.\n049144     IF WS-MD-BN-AGE > 0\n049146         NEXT SENTENCE ELSE\n049148         GO TO Z-34-5-1-ELSE.\n049150     COMPUTE WS-SP-AGE = ( WS-MD-BN-AGE - 35 ) + 1 .\n049152\n049154     IF WS-MD-BN-AGE < 35\n049156         NEXT SENTENCE\n049158     ELSE\n049160         GO TO Z-34-7-END-MOVE.\n049162     MOVE 1 TO WS-SP-AGE.\n049164 Z-34-7-END-MOVE.\n049166     COMPUTE WS-MD-AGE-DIFF = WS-MD-AGE - WS-MD-BN-AGE .\n049168\n049170 Z-34-5-1-ELSE.\n049172     IF TDB-TDAA-INHERIT-IRA = 1\n049174         NEXT SENTENCE ELSE\n049176         GO TO Z-34-9-1-ELSE.\n049178     COMPUTE WS-AGE-COUNT = WS-MD-AGE + 1 .\n049180\n049182     IF PROCESS-DATE-CCYY < WS-RMD-LEF-CUTOFF-YR\n049184         NEXT SENTENCE ELSE\n049186         GO TO Z-34-11-1-ELSE.\n049188     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 112 )\n049190         NEXT SENTENCE ELSE\n049192         GO TO Z-34-12-1-ELSE.\n049194     MOVE WS-RMD-TBL1-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.\n049196 Z-34-12-1-ELSE.\n049198     GO TO Z-34-11-ENDIF.\n049200 Z-34-11-1-ELSE.\n049202     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 121 )\n049204         NEXT SENTENCE ELSE\n049206         GO TO Z-34-14-1-ELSE.\n049208     MOVE WS-RMD-TBL1-2022-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.\n049210 Z-34-14-1-ELSE.\n049212 Z-34-11-ENDIF.\n049214     IF WS-LE-FACTOR9 > 0\n049216         NEXT SENTENCE ELSE\n049218         GO TO Z-34-16-1-ELSE.\n049220     COMPUTE WS-FACTOR = WS-LE-FACTOR9 / 10 .\n049222\n049224 Z-34-16-1-ELSE.\n049226     IF WS-FACTOR NOT = 0\n049228         NEXT SENTENCE\n049230     ELSE\n049232         GO TO Z-34-18-END-MOVE.\n049234     MOVE 1 TO WS-MD-TBL.\n049236 Z-34-18-END-MOVE.\n049238     MOVE ZERO TO WS-MD-AMT.\n049240     IF WS-FACTOR > 0\n049242         NEXT SENTENCE ELSE\n049244         GO TO Z-34-20-1-ELSE.\n049246     COMPUTE WS-MD-AMT ROUNDED = WS-MD-FMV / WS-FACTOR .\n049248\n049250 Z-34-20-1-ELSE.\n049252     MOVE WS-FACTOR TO WS-MD-FACT.\n049254     MOVE 0 TO Z-EXIT-LEVEL.\n049256     MOVE 2 TO Z-EXIT-CODE.\n049258     GO TO Z-34-END.\n049260 Z-34-9-1-ELSE.\n049262     IF TDB-TDAA-INHERIT-IRA = 2\n049264         NEXT SENTENCE ELSE\n049266         GO TO Z-34-24-1-ELSE.\n049268     IF WS-MD-BN-AGE > 0\n049270         NEXT SENTENCE ELSE\n049272         GO TO Z-34-25-1-ELSE.\n049274     COMPUTE WS-AGE-COUNT = WS-MD-BN-AGE + 1 .\n049276\n049278     GO TO Z-34-25-ENDIF.\n049280 Z-34-25-1-ELSE.\n049282     MOVE 0 TO WS-AGE-COUNT.\n049284 Z-34-25-ENDIF.\n049286     IF PROCESS-DATE-CCYY < WS-RMD-LEF-CUTOFF-YR\n049288         NEXT SENTENCE ELSE\n049290         GO TO Z-34-28-1-ELSE.\n049292     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 112 )\n049294         NEXT SENTENCE ELSE\n049296         GO TO Z-34-29-1-ELSE.\n049298     MOVE WS-RMD-TBL1-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.\n049300 Z-34-29-1-ELSE.\n049302     GO TO Z-34-28-ENDIF.\n049304 Z-34-28-1-ELSE.\n049306     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 121 )\n049308         NEXT SENTENCE ELSE\n049310         GO TO Z-34-31-1-ELSE.\n049312     MOVE WS-RMD-TBL1-2022-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.\n049314 Z-34-31-1-ELSE.\n049316 Z-34-28-ENDIF.\n049318     IF WS-LE-FACTOR9 > 0\n049320         NEXT SENTENCE ELSE\n049322         GO TO Z-34-33-1-ELSE.\n049324     COMPUTE WS-FACTOR = WS-LE-FACTOR9 / 10 .\n049326\n049328 Z-34-33-1-ELSE.\n049330     SUBTRACT WS-NUM-YR-YAD FROM WS-FACTOR .\n049332     IF WS-FACTOR NOT = 0\n049334         NEXT SENTENCE\n049336     ELSE\n049338         GO TO Z-34-36-END-MOVE.\n049340     MOVE 1 TO WS-MD-TBL.\n049342 Z-34-36-END-MOVE.\n049344     MOVE ZERO TO WS-MD-AMT.\n049346     IF WS-FACTOR > 0\n049348         NEXT SENTENCE ELSE\n049350         GO TO Z-34-38-1-ELSE.\n049352     COMPUTE WS-MD-AMT ROUNDED = WS-MD-FMV / WS-FACTOR .\n049354\n049356 Z-34-38-1-ELSE.\n049358     MOVE WS-FACTOR TO WS-MD-FACT.\n049360     MOVE 0 TO Z-EXIT-LEVEL.\n049362     MOVE 2 TO Z-EXIT-CODE.\n049364     GO TO Z-34-END.\n049366 Z-34-24-1-ELSE.\n049368     IF ( WS-MD-AGE-DIFF > 10 ) AND ( WS-MD-AGE > 71 )\n049370         NEXT SENTENCE ELSE\n049372         GO TO Z-34-42-1-ELSE.\n049374     IF ( WS-AGE-COUNT > 0 ) AND ( WS-SP-AGE > 0 )\n049376         NEXT SENTENCE ELSE\n049378         GO TO Z-34-43-1-ELSE.\n049380     IF PROCESS-DATE-CCYY < WS-RMD-LEF-CUTOFF-YR\n049382         NEXT SENTENCE ELSE\n049384         GO TO Z-34-44-1-ELSE.\n049386     IF ( WS-AGE-COUNT NOT > 81 ) AND ( WS-SP-AGE NOT > 81 )\n049388         NEXT SENTENCE ELSE\n049390         GO TO Z-34-45-1-ELSE.\n049392     MOVE WS-RMD-TBL2-LEF (WS-AGE-COUNT, WS-SP-AGE) TO            \n049394         WS-LE-FACTOR9.\n049396 Z-34-45-1-ELSE.\n049398     GO TO Z-34-44-ENDIF.\n049400 Z-34-44-1-ELSE.\n049402     IF ( ( WS-MD-AGE + 1 ) NOT > 121 ) AND ( ( WS-MD-BN-AGE + 1  \n049404         ) NOT > 121 )\n049406         NEXT SENTENCE ELSE\n049408         GO TO Z-34-47-1-ELSE.\n049410     MOVE WS-RMD-TBL2-2022-LEF (WS-MD-AGE + 1, WS-MD-BN-AGE + 1)  \n049412         TO WS-LE-FACTOR9.\n049414 Z-34-47-1-ELSE.\n049416 Z-34-44-ENDIF.\n049418 Z-34-43-1-ELSE.\n049420     IF WS-LE-FACTOR9 > 0\n049422         NEXT SENTENCE ELSE\n049424         GO TO Z-34-49-1-ELSE.\n049426     COMPUTE WS-FACTOR = WS-LE-FACTOR9 / 10 .\n049428\n049430 Z-34-49-1-ELSE.\n049432     MOVE 2 TO WS-MD-TBL.\n049434     GO TO Z-34-42-ENDIF.\n049436 Z-34-42-1-ELSE.\n049438     IF WS-MD-AGE < 72\n049440         NEXT SENTENCE ELSE\n049442         GO TO Z-34-42-2-ELSE.\n049444     COMPUTE WS-AGE-COUNT = WS-MD-AGE + 1 .\n049446\n049448     IF WS-MD-AGE < 01\n049450         NEXT SENTENCE\n049452     ELSE\n049454         GO TO Z-34-53-END-MOVE.\n049456     MOVE 1 TO WS-AGE-COUNT.\n049458 Z-34-53-END-MOVE.\n049460     IF PROCESS-DATE-CCYY < WS-RMD-LEF-CUTOFF-YR\n049462         NEXT SENTENCE ELSE\n049464         GO TO Z-34-54-1-ELSE.\n049466     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 112 )\n049468         NEXT SENTENCE ELSE\n049470         GO TO Z-34-55-1-ELSE.\n049472     MOVE WS-RMD-TBL1-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.\n049474 Z-34-55-1-ELSE.\n049476     GO TO Z-34-54-ENDIF.\n049478 Z-34-54-1-ELSE.\n049480     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 121 )\n049482         NEXT SENTENCE ELSE\n049484         GO TO Z-34-57-1-ELSE.\n049486     MOVE WS-RMD-TBL1-2022-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.\n049488 Z-34-57-1-ELSE.\n049490 Z-34-54-ENDIF.\n049492     IF WS-LE-FACTOR9 > 0\n049494         NEXT SENTENCE ELSE\n049496         GO TO Z-34-59-1-ELSE.\n049498     COMPUTE WS-FACTOR = WS-LE-FACTOR9 / 10 .\n049500\n049502 Z-34-59-1-ELSE.\n049504     MOVE 1 TO WS-MD-TBL.\n049506     GO TO Z-34-42-ENDIF.\n049508 Z-34-42-2-ELSE.\n049510     IF WS-MD-AGE > 71\n049512         NEXT SENTENCE ELSE\n049514         GO TO Z-34-42-3-ELSE.\n049516     IF PROCESS-DATE-CCYY < WS-RMD-LEF-CUTOFF-YR\n049518         NEXT SENTENCE ELSE\n049520         GO TO Z-34-62-1-ELSE.\n049522     COMPUTE WS-AGE-COUNT = WS-MD-AGE - 70 + 1 .\n049524\n049526     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 46 )\n049528         NEXT SENTENCE ELSE\n049530         GO TO Z-34-64-1-ELSE.\n049532     MOVE WS-RMD-TBL3-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.\n049534 Z-34-64-1-ELSE.\n049536     GO TO Z-34-62-ENDIF.\n049538 Z-34-62-1-ELSE.\n049540     COMPUTE WS-AGE-COUNT = WS-MD-AGE - 72 + 1 .\n049542\n049544     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 49 )\n049546         NEXT SENTENCE ELSE\n049548         GO TO Z-34-67-1-ELSE.\n049550     MOVE WS-RMD-TBL3-2022-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.\n049552 Z-34-67-1-ELSE.\n049554 Z-34-62-ENDIF.\n049556     IF WS-LE-FACTOR9 > 0\n049558         NEXT SENTENCE ELSE\n049560         GO TO Z-34-69-1-ELSE.\n049562     COMPUTE WS-FACTOR = WS-LE-FACTOR9 / 10 .\n049564\n049566 Z-34-69-1-ELSE.\n049568     MOVE 3 TO WS-MD-TBL.\n049570 Z-34-42-3-ELSE.\n049572 Z-34-42-ENDIF.\n049574     MOVE ZERO TO WS-MD-AMT.\n049576     IF WS-FACTOR > 0\n049578         NEXT SENTENCE ELSE\n049580         GO TO Z-34-73-1-ELSE.\n049582     COMPUTE WS-MD-AMT ROUNDED = WS-MD-FMV / WS-FACTOR .\n049584\n049586 Z-34-73-1-ELSE.\n049588     MOVE WS-FACTOR TO WS-MD-FACT.\n049590 Z-34-END.\n049592     IF Z-EDIT-ERROR\n049594         GO TO Z-34-XIT.\n049596 Z-34-SKIP.\n049598     IF Z-EXIT-LEVEL NOT < 0\n049600         MOVE 0 TO Z-EXIT-CODE\n049602         MOVE 9999 TO Z-EXIT-LEVEL.\n049604 Z-34-XIT.\n049606     EXIT.\n049608*\n049610*****************************************************************\n049612*    PROCEDURE TDB-ACTV-ADJUSTMENT\n049614*****************************************************************\n049616 Z-35-PROCEDURE.\n049618*\n049620     MOVE HOLD-TDA-ACTVC-CHG-FRM TO WS-CHG-WORK.\n049622     IF HOLD-TDA-ACTVC-CODE = 0010\n049624         NEXT SENTENCE ELSE\n049626         GO TO Z-35-2-1-ELSE.\n049628     MOVE WS-CHG-WK-X-3 TO HOLD-TDAA-CSR.\n049630     GO TO Z-35-2-ENDIF.\n049632 Z-35-2-1-ELSE.\n049634     IF HOLD-TDA-ACTVC-CODE = 0011\n049636         NEXT SENTENCE ELSE\n049638         GO TO Z-35-2-2-ELSE.\n049640     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-WTHLD-CD.\n049642     GO TO Z-35-2-ENDIF.\n049644 Z-35-2-2-ELSE.\n049646     IF HOLD-TDA-ACTVC-CODE = 0012\n049648         NEXT SENTENCE ELSE\n049650         GO TO Z-35-2-3-ELSE.\n049652     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-DT-CONDENSED.\n049654     GO TO Z-35-2-ENDIF.\n049656 Z-35-2-3-ELSE.\n049658     IF HOLD-TDA-ACTVC-CODE = 0013\n049660         NEXT SENTENCE ELSE\n049662         GO TO Z-35-2-4-ELSE.\n049664     MOVE WS-CHG-WK-X-24 TO HOLD-TDAA-FREE-MARK.\n049666     GO TO Z-35-2-ENDIF.\n049668 Z-35-2-4-ELSE.\n049670     IF HOLD-TDA-ACTVC-CODE = 0014\n049672         NEXT SENTENCE ELSE\n049674         GO TO Z-35-2-5-ELSE.\n049676     MOVE WS-CHG-WK-X-3 TO HOLD-TDAA-OFFICER.\n049678     GO TO Z-35-2-ENDIF.\n049680 Z-35-2-5-ELSE.\n049682     IF HOLD-TDA-ACTVC-CODE = 0015\n049684         NEXT SENTENCE ELSE\n049686         GO TO Z-35-2-6-ELSE.\n049688     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-CLASS-CD.\n049690     GO TO Z-35-2-ENDIF.\n049692 Z-35-2-6-ELSE.\n049694     IF HOLD-TDA-ACTVC-CODE = 0016\n049696         NEXT SENTENCE ELSE\n049698         GO TO Z-35-2-7-ELSE.\n049700     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-CORR-BK-CD.\n049702     GO TO Z-35-2-ENDIF.\n049704 Z-35-2-7-ELSE.\n049706     IF HOLD-TDA-ACTVC-CODE = 0017\n049708         NEXT SENTENCE ELSE\n049710         GO TO Z-35-2-8-ELSE.\n049712     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-PUBLIC-FUND.\n049714     GO TO Z-35-2-ENDIF.\n049716 Z-35-2-8-ELSE.\n049718     IF HOLD-TDA-ACTVC-CODE = 0018\n049720         NEXT SENTENCE ELSE\n049722         GO TO Z-35-2-9-ELSE.\n049724     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-TRUST-CD.\n049726     GO TO Z-35-2-ENDIF.\n049728 Z-35-2-9-ELSE.\n049730     IF HOLD-TDA-ACTVC-CODE = 0019\n049732         NEXT SENTENCE ELSE\n049734         GO TO Z-35-2-10-ELSE.\n049736     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-WTHDRW-ALLOW.\n049738     GO TO Z-35-2-ENDIF.\n049740 Z-35-2-10-ELSE.\n049742     IF HOLD-TDA-ACTVC-CODE = 0020\n049744         NEXT SENTENCE ELSE\n049746         GO TO Z-35-2-11-ELSE.\n049748     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-DPOSIT-ALLOW.\n049750     GO TO Z-35-2-ENDIF.\n049752 Z-35-2-11-ELSE.\n049754     IF HOLD-TDA-ACTVC-CODE = 0021\n049756         NEXT SENTENCE ELSE\n049758         GO TO Z-35-2-12-ELSE.\n049760     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-COMM-ACCT.\n049762     GO TO Z-35-2-ENDIF.\n049764 Z-35-2-12-ELSE.\n049766     IF HOLD-TDA-ACTVC-CODE = 0022\n049768         NEXT SENTENCE ELSE\n049770         GO TO Z-35-2-13-ELSE.\n049772     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-RT-FLOOR.\n049774     GO TO Z-35-2-ENDIF.\n049776 Z-35-2-13-ELSE.\n049778     IF HOLD-TDA-ACTVC-CODE = 0023\n049780         NEXT SENTENCE ELSE\n049782         GO TO Z-35-2-14-ELSE.\n049784     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-REPO-CD.\n049786     GO TO Z-35-2-ENDIF.\n049788 Z-35-2-14-ELSE.\n049790     IF HOLD-TDA-ACTVC-CODE = 0024\n049792         NEXT SENTENCE ELSE\n049794         GO TO Z-35-2-15-ELSE.\n049796     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-WTHD-REQD-CD.\n049798     GO TO Z-35-2-ENDIF.\n049800 Z-35-2-15-ELSE.\n049802     IF HOLD-TDA-ACTVC-CODE = 0025\n049804         NEXT SENTENCE ELSE\n049806         GO TO Z-35-2-16-ELSE.\n049808     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-POST-MAT.\n049810     GO TO Z-35-2-ENDIF.\n049812 Z-35-2-16-ELSE.\n049814     IF HOLD-TDA-ACTVC-CODE = 0026\n049816         NEXT SENTENCE ELSE\n049818         GO TO Z-35-2-17-ELSE.\n049820     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-INT-CD.\n049822     GO TO Z-35-2-ENDIF.\n049824 Z-35-2-17-ELSE.\n049826     IF HOLD-TDA-ACTVC-CODE = 0027\n049828         NEXT SENTENCE ELSE\n049830         GO TO Z-35-2-18-ELSE.\n049832     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-WTHLD-AMT.\n049834     GO TO Z-35-2-ENDIF.\n049836 Z-35-2-18-ELSE.\n049838     IF HOLD-TDA-ACTVC-CODE = 0028\n049840         NEXT SENTENCE ELSE\n049842         GO TO Z-35-2-19-ELSE.\n049844     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-SUM-STMT-CD.\n049846     GO TO Z-35-2-ENDIF.\n049848 Z-35-2-19-ELSE.\n049850     IF HOLD-TDA-ACTVC-CODE = 0029\n049852         NEXT SENTENCE ELSE\n049854         GO TO Z-35-2-20-ELSE.\n049856     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-RT-CHG-ALLOW.\n049858     GO TO Z-35-2-ENDIF.\n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 550 lines from 24376 to 24925.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 51,
  "total_chunks": 55,
  "start_line": 24376,
  "end_line": 24925,
  "line_count": 550
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
- Source code length: 27675 characters

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
CHUNK 51 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 24376 to 24925 (550 lines)
Chunk Tokens (estimated): ~8,057
Actual Input Tokens: 9,463 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 24376-24925 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 51 of 55 chunks
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
      The source code below is only CHUNK 51 of 55.


=============================================================================
CHUNK 51 SOURCE CODE (Lines 24376-24925)
=============================================================================

```cobol
048760         HOLD-TDAIRA.
048762     MOVE TDAI-CN-LYTD-AMT OF TDAIRA TO HOLD-TDAI-CN-LYTD-AMT OF  
048764         HOLD-TDAIRA.
048766     MOVE TDAI-EMP-CONT-LYR OF TDAIRA TO HOLD-TDAI-EMP-CONT-LYR   
048768         OF HOLD-TDAIRA.
048770     MOVE TDAI-REG-CONT-LYR OF TDAIRA TO HOLD-TDAI-REG-CONT-LYR   
048772         OF HOLD-TDAIRA.
048774     MOVE TDAI-UNINSURED OF TDAIRA TO HOLD-TDAI-UNINSURED OF      
048776         HOLD-TDAIRA.
048778     MOVE TDAI-ROLLOVER OF TDAIRA TO HOLD-TDAI-ROLLOVER OF        
048780         HOLD-TDAIRA.
048782     MOVE TDAI-ROLLOVER-LYR OF TDAIRA TO HOLD-TDAI-ROLLOVER-LYR   
048784         OF HOLD-TDAIRA.
048786     MOVE TDAI-TRANSFER-IN OF TDAIRA TO HOLD-TDAI-TRANSFER-IN OF  
048788         HOLD-TDAIRA.
048790     MOVE TDAI-TRANSFER-OUT OF TDAIRA TO HOLD-TDAI-TRANSFER-OUT   
048792         OF HOLD-TDAIRA.
048794     MOVE TDAI-1ST-CN-DATE OF TDAIRA TO HOLD-TDAI-1ST-CN-DATE OF  
048796         HOLD-TDAIRA.
048798     MOVE TDAI-BASIS-C-LTD OF TDAIRA TO HOLD-TDAI-BASIS-C-LTD OF  
048800         HOLD-TDAIRA.
048802     MOVE TDAI-BASIS-D-LTD OF TDAIRA TO HOLD-TDAI-BASIS-D-LTD OF  
048804         HOLD-TDAIRA.
048806     MOVE TDAI-BASIS-D-YTD OF TDAIRA TO HOLD-TDAI-BASIS-D-YTD OF  
048808         HOLD-TDAIRA.
048810     MOVE TDB-READ-DATE TO HOLD-READ-DATE.
048812     MOVE 00 TO TDB-STRUCT-NBR.
048814     MOVE SPACES TO TDB-DATA-AREA.
048816     MOVE ZERO TO Z-FLINFO14-PRES.
048818     MOVE 17 TO Z-FLINFO14-LAST-SEQ.
048820     MOVE ZERO TO Z-FLINFO14-SOME.
048822     SET TDAACTVBKSET OF TDAACTV OF LDBTDADB TO ENDING
048824         ON EXCEPTION
048826         MOVE "TDAACTVBKSET OF TDAACTV OF LDBTDADB" TO            
048828             Z-DMS-EXCEPT-STR
048830         MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
048832         MOVE 17 TO Z-DMS-EXCEPT-SEQ
048834         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT
048836         GO TO Z-33-5-XIT.
048838 Z-33-5-READ.
048840     FIND TDAACTV OF LDBTDADB VIA PRIOR TDAACTVBKSET OF TDAACTV   
048842         OF LDBTDADB
048844     AT TDA-ACTV-BANK = HOLD-TDAI-BANK AND
048846        TDA-ACTV-CUST = HOLD-TDAI-CUST AND
048848        TDA-ACTV-ACCT = HOLD-TDAI-ACCT
048850         ON EXCEPTION
048852         MOVE 17 TO Z-DMS-EXCEPT-SEQ
048854         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
048856             GO TO Z-33-5-XIT
048858         ELSE
048860             MOVE "TDAACTVBKSET OF TDAACTV OF LDBTDADB" TO        
048862                 Z-DMS-EXCEPT-STR
048864             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
048866             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
048868
048870 Z-33-5-PRESENT.
048872*
048874     MOVE 1 TO Z-FLINFO14-SOME.
048876     MOVE 1 TO Z-FLINFO14-PRES.
048878     GO TO Z-33-5-CONT.
048880 Z-33-5-XIT.
048882 Z-33-5-CONT.
048884 Z-33-6-LOOP.
048886     IF Z-FLINFO14-ABSENT OR TDA-ACTV-DATE < TDB-READ-DATE
048888         GO TO Z-33-6-XIT.
048890     MOVE 0 TO Z-EXIT-CODE.
048892     MOVE 9999 TO Z-EXIT-LEVEL.
048894     MOVE TDA-ACTV-BANK OF TDAACTV TO HOLD-TDA-ACTV-BANK OF       
048896         HOLD-TDAACTV.
048898     MOVE TDA-ACTV-BRCH OF TDAACTV TO HOLD-TDA-ACTV-BRCH OF       
048900         HOLD-TDAACTV.
048902     MOVE TDA-ACTV-APPL OF TDAACTV TO HOLD-TDA-ACTV-APPL OF       
048904         HOLD-TDAACTV.
048906     MOVE TDA-ACTV-CUST OF TDAACTV TO HOLD-TDA-ACTV-CUST OF       
048908         HOLD-TDAACTV.
048910     MOVE TDA-ACTV-ACCT OF TDAACTV TO HOLD-TDA-ACTV-ACCT OF       
048912         HOLD-TDAACTV.
048914     MOVE TDA-ACTV-TOT-CD OF TDAACTV TO HOLD-TDA-ACTV-TOT-CD OF   
048916         HOLD-TDAACTV.
048918     MOVE TDA-ACTV-IGL-GRP OF TDAACTV TO HOLD-TDA-ACTV-IGL-GRP OF 
048920         HOLD-TDAACTV.
048922     MOVE TDA-ACTV-OFFICER OF TDAACTV TO HOLD-TDA-ACTV-OFFICER OF 
048924         HOLD-TDAACTV.
048926     MOVE TDA-ACTV-NC-INDC OF TDAACTV TO HOLD-TDA-ACTV-NC-INDC OF 
048928         HOLD-TDAACTV.
048930     MOVE TDA-ACTV-PROC-FG OF TDAACTV TO HOLD-TDA-ACTV-PROC-FG OF 
048932         HOLD-TDAACTV.
048934     MOVE TDA-ACTV-EFF-DT OF TDAACTV TO HOLD-TDA-ACTV-EFF-DT OF   
048936         HOLD-TDAACTV.
048938     MOVE TDA-ACTV-DATE OF TDAACTV TO HOLD-TDA-ACTV-DATE OF       
048940         HOLD-TDAACTV.
048942     MOVE TDA-ACTV-MAINT OF TDAACTV TO HOLD-TDA-ACTV-MAINT OF     
048944         HOLD-TDAACTV.
048946     MOVE TDA-ACTV-TIME OF TDAACTV TO HOLD-TDA-ACTV-TIME OF       
048948         HOLD-TDAACTV.
048950     MOVE TDA-ACTV-SEQ-NBR OF TDAACTV TO HOLD-TDA-ACTV-SEQ-NBR OF 
048952         HOLD-TDAACTV.
048954     MOVE TDA-ACTV-SERIAL OF TDAACTV TO HOLD-TDA-ACTV-SERIAL OF   
048956         HOLD-TDAACTV.
048958     MOVE TDA-ACTV-SOURCE OF TDAACTV TO HOLD-TDA-ACTV-SOURCE OF   
048960         HOLD-TDAACTV.
048962     MOVE TDA-ACTV-ERASED OF TDAACTV TO HOLD-TDA-ACTV-ERASED OF   
048964         HOLD-TDAACTV.
048966     MOVE TDA-ACTV-DR-CR OF TDAACTV TO HOLD-TDA-ACTV-DR-CR OF     
048968         HOLD-TDAACTV.
048970     MOVE TDA-ACTV-E-PUBID OF TDAACTV TO HOLD-TDA-ACTV-E-PUBID OF 
048972         HOLD-TDAACTV.
048974     MOVE TDA-ACTV-PUB-ID OF TDAACTV TO HOLD-TDA-ACTV-PUB-ID OF   
048976         HOLD-TDAACTV.
048978     MOVE TDA-ACTV-SUB OF TDAACTV TO HOLD-TDA-ACTV-SUB OF         
048980         HOLD-TDAACTV.
048982     IF TDAACTV (TDA-ACTV-TYPE ) = 2
048984         NEXT SENTENCE ELSE
048986         GO TO Z-33-8-1-ELSE.
048988     MOVE "A" TO WS-ADJUSTED-IND.
048990     MOVE TDA-ACTVC-CODE TO HOLD-TDA-ACTVC-CODE.
048992     MOVE TDA-ACTVC-EXCPT TO HOLD-TDA-ACTVC-EXCPT.
048994     MOVE TDA-ACTVC-CHG-FRM TO HOLD-TDA-ACTVC-CHG-FRM.
048996     MOVE TDA-ACTVC-CHG-TO TO HOLD-TDA-ACTVC-CHG-TO.
048998     MOVE TDA-ACTVC-NCREOPN TO HOLD-TDA-ACTVC-NCREOPN.
049000************ PERFORM TDB-ACTV-ADJUSTMENT
049002     PERFORM Z-35-PROCEDURE THRU Z-35-XIT.
049004     IF  Z-EXIT-EDITEXIT
049006         GO TO Z-33-XIT.
049008     IF  Z-DMS2-ABORT-FLAG = 1
049010         GO TO Z-33-XIT.
049012     IF  Z-EXIT-LEVEL < 0
049014         GO TO Z-33-6-END.
049016*
049018 Z-33-8-1-ELSE.
049020     MOVE ZERO TO Z-FLINFO14-PRES.
049022     MOVE 18 TO Z-FLINFO14-LAST-SEQ.
049024     MOVE ZERO TO Z-FLINFO14-SOME.
049026 Z-33-16-READ.
049028     FIND TDAACTV OF LDBTDADB VIA PRIOR TDAACTVBKSET OF TDAACTV   
049030         OF LDBTDADB
049032     AT TDA-ACTV-BANK = HOLD-TDAI-BANK AND
049034        TDA-ACTV-CUST = HOLD-TDAI-CUST AND
049036        TDA-ACTV-ACCT = HOLD-TDAI-ACCT
049038         ON EXCEPTION
049040         MOVE 18 TO Z-DMS-EXCEPT-SEQ
049042         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
049044             GO TO Z-33-16-XIT
049046         ELSE
049048             MOVE "TDAACTVBKSET OF TDAACTV OF LDBTDADB" TO        
049050                 Z-DMS-EXCEPT-STR
049052             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
049054             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
049056
049058 Z-33-16-PRESENT.
049060*
049062     MOVE 1 TO Z-FLINFO14-SOME.
049064     MOVE 1 TO Z-FLINFO14-PRES.
049066     GO TO Z-33-16-CONT.
049068 Z-33-16-XIT.
049070 Z-33-16-CONT.
049072 Z-33-6-END.
049074     IF Z-EDIT-ERROR
049076         GO TO Z-33-XIT.
049078 Z-33-6-SKIP.
049080     IF Z-EXIT-LEVEL < 1
049082         GO TO Z-33-END.
049084     IF Z-EXIT-CODE > 0
049086         GO TO Z-33-6-XIT.
049088     GO TO Z-33-6-LOOP.
049090*
049092 Z-33-6-XIT.
049094     MOVE 0 TO Z-EXIT-CODE.
049096     MOVE 9999 TO Z-EXIT-LEVEL.
049098 Z-33-END.
049100     IF Z-EDIT-ERROR
049102         GO TO Z-33-XIT.
049104 Z-33-SKIP.
049106     IF Z-EXIT-LEVEL NOT < 0
049108         MOVE 0 TO Z-EXIT-CODE
049110         MOVE 9999 TO Z-EXIT-LEVEL.
049112 Z-33-XIT.
049114     EXIT.
049116*
049118*****************************************************************
049120*    PROCEDURE CALC-MINDIST-AMT
049122*****************************************************************
049124 Z-34-PROCEDURE.
049126*
049128     MOVE 0 TO Z-EXIT-CODE.
049130     MOVE 9999 TO Z-EXIT-LEVEL.
049132     MOVE SPACES TO WS-LE-FACTOR.
049134     MOVE 0 TO WS-LE-FACT-1
049136       , WS-LE-FACT-2.
049138     COMPUTE WS-AGE-COUNT = ( WS-MD-AGE - 35 ) + 1 .
049140
049142     MOVE ZEROS TO WS-MD-AGE-DIFF.
049144     IF WS-MD-BN-AGE > 0
049146         NEXT SENTENCE ELSE
049148         GO TO Z-34-5-1-ELSE.
049150     COMPUTE WS-SP-AGE = ( WS-MD-BN-AGE - 35 ) + 1 .
049152
049154     IF WS-MD-BN-AGE < 35
049156         NEXT SENTENCE
049158     ELSE
049160         GO TO Z-34-7-END-MOVE.
049162     MOVE 1 TO WS-SP-AGE.
049164 Z-34-7-END-MOVE.
049166     COMPUTE WS-MD-AGE-DIFF = WS-MD-AGE - WS-MD-BN-AGE .
049168
049170 Z-34-5-1-ELSE.
049172     IF TDB-TDAA-INHERIT-IRA = 1
049174         NEXT SENTENCE ELSE
049176         GO TO Z-34-9-1-ELSE.
049178     COMPUTE WS-AGE-COUNT = WS-MD-AGE + 1 .
049180
049182     IF PROCESS-DATE-CCYY < WS-RMD-LEF-CUTOFF-YR
049184         NEXT SENTENCE ELSE
049186         GO TO Z-34-11-1-ELSE.
049188     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 112 )
049190         NEXT SENTENCE ELSE
049192         GO TO Z-34-12-1-ELSE.
049194     MOVE WS-RMD-TBL1-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.
049196 Z-34-12-1-ELSE.
049198     GO TO Z-34-11-ENDIF.
049200 Z-34-11-1-ELSE.
049202     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 121 )
049204         NEXT SENTENCE ELSE
049206         GO TO Z-34-14-1-ELSE.
049208     MOVE WS-RMD-TBL1-2022-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.
049210 Z-34-14-1-ELSE.
049212 Z-34-11-ENDIF.
049214     IF WS-LE-FACTOR9 > 0
049216         NEXT SENTENCE ELSE
049218         GO TO Z-34-16-1-ELSE.
049220     COMPUTE WS-FACTOR = WS-LE-FACTOR9 / 10 .
049222
049224 Z-34-16-1-ELSE.
049226     IF WS-FACTOR NOT = 0
049228         NEXT SENTENCE
049230     ELSE
049232         GO TO Z-34-18-END-MOVE.
049234     MOVE 1 TO WS-MD-TBL.
049236 Z-34-18-END-MOVE.
049238     MOVE ZERO TO WS-MD-AMT.
049240     IF WS-FACTOR > 0
049242         NEXT SENTENCE ELSE
049244         GO TO Z-34-20-1-ELSE.
049246     COMPUTE WS-MD-AMT ROUNDED = WS-MD-FMV / WS-FACTOR .
049248
049250 Z-34-20-1-ELSE.
049252     MOVE WS-FACTOR TO WS-MD-FACT.
049254     MOVE 0 TO Z-EXIT-LEVEL.
049256     MOVE 2 TO Z-EXIT-CODE.
049258     GO TO Z-34-END.
049260 Z-34-9-1-ELSE.
049262     IF TDB-TDAA-INHERIT-IRA = 2
049264         NEXT SENTENCE ELSE
049266         GO TO Z-34-24-1-ELSE.
049268     IF WS-MD-BN-AGE > 0
049270         NEXT SENTENCE ELSE
049272         GO TO Z-34-25-1-ELSE.
049274     COMPUTE WS-AGE-COUNT = WS-MD-BN-AGE + 1 .
049276
049278     GO TO Z-34-25-ENDIF.
049280 Z-34-25-1-ELSE.
049282     MOVE 0 TO WS-AGE-COUNT.
049284 Z-34-25-ENDIF.
049286     IF PROCESS-DATE-CCYY < WS-RMD-LEF-CUTOFF-YR
049288         NEXT SENTENCE ELSE
049290         GO TO Z-34-28-1-ELSE.
049292     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 112 )
049294         NEXT SENTENCE ELSE
049296         GO TO Z-34-29-1-ELSE.
049298     MOVE WS-RMD-TBL1-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.
049300 Z-34-29-1-ELSE.
049302     GO TO Z-34-28-ENDIF.
049304 Z-34-28-1-ELSE.
049306     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 121 )
049308         NEXT SENTENCE ELSE
049310         GO TO Z-34-31-1-ELSE.
049312     MOVE WS-RMD-TBL1-2022-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.
049314 Z-34-31-1-ELSE.
049316 Z-34-28-ENDIF.
049318     IF WS-LE-FACTOR9 > 0
049320         NEXT SENTENCE ELSE
049322         GO TO Z-34-33-1-ELSE.
049324     COMPUTE WS-FACTOR = WS-LE-FACTOR9 / 10 .
049326
049328 Z-34-33-1-ELSE.
049330     SUBTRACT WS-NUM-YR-YAD FROM WS-FACTOR .
049332     IF WS-FACTOR NOT = 0
049334         NEXT SENTENCE
049336     ELSE
049338         GO TO Z-34-36-END-MOVE.
049340     MOVE 1 TO WS-MD-TBL.
049342 Z-34-36-END-MOVE.
049344     MOVE ZERO TO WS-MD-AMT.
049346     IF WS-FACTOR > 0
049348         NEXT SENTENCE ELSE
049350         GO TO Z-34-38-1-ELSE.
049352     COMPUTE WS-MD-AMT ROUNDED = WS-MD-FMV / WS-FACTOR .
049354
049356 Z-34-38-1-ELSE.
049358     MOVE WS-FACTOR TO WS-MD-FACT.
049360     MOVE 0 TO Z-EXIT-LEVEL.
049362     MOVE 2 TO Z-EXIT-CODE.
049364     GO TO Z-34-END.
049366 Z-34-24-1-ELSE.
049368     IF ( WS-MD-AGE-DIFF > 10 ) AND ( WS-MD-AGE > 71 )
049370         NEXT SENTENCE ELSE
049372         GO TO Z-34-42-1-ELSE.
049374     IF ( WS-AGE-COUNT > 0 ) AND ( WS-SP-AGE > 0 )
049376         NEXT SENTENCE ELSE
049378         GO TO Z-34-43-1-ELSE.
049380     IF PROCESS-DATE-CCYY < WS-RMD-LEF-CUTOFF-YR
049382         NEXT SENTENCE ELSE
049384         GO TO Z-34-44-1-ELSE.
049386     IF ( WS-AGE-COUNT NOT > 81 ) AND ( WS-SP-AGE NOT > 81 )
049388         NEXT SENTENCE ELSE
049390         GO TO Z-34-45-1-ELSE.
049392     MOVE WS-RMD-TBL2-LEF (WS-AGE-COUNT, WS-SP-AGE) TO            
049394         WS-LE-FACTOR9.
049396 Z-34-45-1-ELSE.
049398     GO TO Z-34-44-ENDIF.
049400 Z-34-44-1-ELSE.
049402     IF ( ( WS-MD-AGE + 1 ) NOT > 121 ) AND ( ( WS-MD-BN-AGE + 1  
049404         ) NOT > 121 )
049406         NEXT SENTENCE ELSE
049408         GO TO Z-34-47-1-ELSE.
049410     MOVE WS-RMD-TBL2-2022-LEF (WS-MD-AGE + 1, WS-MD-BN-AGE + 1)  
049412         TO WS-LE-FACTOR9.
049414 Z-34-47-1-ELSE.
049416 Z-34-44-ENDIF.
049418 Z-34-43-1-ELSE.
049420     IF WS-LE-FACTOR9 > 0
049422         NEXT SENTENCE ELSE
049424         GO TO Z-34-49-1-ELSE.
049426     COMPUTE WS-FACTOR = WS-LE-FACTOR9 / 10 .
049428
049430 Z-34-49-1-ELSE.
049432     MOVE 2 TO WS-MD-TBL.
049434     GO TO Z-34-42-ENDIF.
049436 Z-34-42-1-ELSE.
049438     IF WS-MD-AGE < 72
049440         NEXT SENTENCE ELSE
049442         GO TO Z-34-42-2-ELSE.
049444     COMPUTE WS-AGE-COUNT = WS-MD-AGE + 1 .
049446
049448     IF WS-MD-AGE < 01
049450         NEXT SENTENCE
049452     ELSE
049454         GO TO Z-34-53-END-MOVE.
049456     MOVE 1 TO WS-AGE-COUNT.
049458 Z-34-53-END-MOVE.
049460     IF PROCESS-DATE-CCYY < WS-RMD-LEF-CUTOFF-YR
049462         NEXT SENTENCE ELSE
049464         GO TO Z-34-54-1-ELSE.
049466     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 112 )
049468         NEXT SENTENCE ELSE
049470         GO TO Z-34-55-1-ELSE.
049472     MOVE WS-RMD-TBL1-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.
049474 Z-34-55-1-ELSE.
049476     GO TO Z-34-54-ENDIF.
049478 Z-34-54-1-ELSE.
049480     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 121 )
049482         NEXT SENTENCE ELSE
049484         GO TO Z-34-57-1-ELSE.
049486     MOVE WS-RMD-TBL1-2022-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.
049488 Z-34-57-1-ELSE.
049490 Z-34-54-ENDIF.
049492     IF WS-LE-FACTOR9 > 0
049494         NEXT SENTENCE ELSE
049496         GO TO Z-34-59-1-ELSE.
049498     COMPUTE WS-FACTOR = WS-LE-FACTOR9 / 10 .
049500
049502 Z-34-59-1-ELSE.
049504     MOVE 1 TO WS-MD-TBL.
049506     GO TO Z-34-42-ENDIF.
049508 Z-34-42-2-ELSE.
049510     IF WS-MD-AGE > 71
049512         NEXT SENTENCE ELSE
049514         GO TO Z-34-42-3-ELSE.
049516     IF PROCESS-DATE-CCYY < WS-RMD-LEF-CUTOFF-YR
049518         NEXT SENTENCE ELSE
049520         GO TO Z-34-62-1-ELSE.
049522     COMPUTE WS-AGE-COUNT = WS-MD-AGE - 70 + 1 .
049524
049526     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 46 )
049528         NEXT SENTENCE ELSE
049530         GO TO Z-34-64-1-ELSE.
049532     MOVE WS-RMD-TBL3-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.
049534 Z-34-64-1-ELSE.
049536     GO TO Z-34-62-ENDIF.
049538 Z-34-62-1-ELSE.
049540     COMPUTE WS-AGE-COUNT = WS-MD-AGE - 72 + 1 .
049542
049544     IF ( WS-AGE-COUNT > 0 ) AND ( WS-AGE-COUNT NOT > 49 )
049546         NEXT SENTENCE ELSE
049548         GO TO Z-34-67-1-ELSE.
049550     MOVE WS-RMD-TBL3-2022-LEF (WS-AGE-COUNT) TO WS-LE-FACTOR9.
049552 Z-34-67-1-ELSE.
049554 Z-34-62-ENDIF.
049556     IF WS-LE-FACTOR9 > 0
049558         NEXT SENTENCE ELSE
049560         GO TO Z-34-69-1-ELSE.
049562     COMPUTE WS-FACTOR = WS-LE-FACTOR9 / 10 .
049564
049566 Z-34-69-1-ELSE.
049568     MOVE 3 TO WS-MD-TBL.
049570 Z-34-42-3-ELSE.
049572 Z-34-42-ENDIF.
049574     MOVE ZERO TO WS-MD-AMT.
049576     IF WS-FACTOR > 0
049578         NEXT SENTENCE ELSE
049580         GO TO Z-34-73-1-ELSE.
049582     COMPUTE WS-MD-AMT ROUNDED = WS-MD-FMV / WS-FACTOR .
049584
049586 Z-34-73-1-ELSE.
049588     MOVE WS-FACTOR TO WS-MD-FACT.
049590 Z-34-END.
049592     IF Z-EDIT-ERROR
049594         GO TO Z-34-XIT.
049596 Z-34-SKIP.
049598     IF Z-EXIT-LEVEL NOT < 0
049600         MOVE 0 TO Z-EXIT-CODE
049602         MOVE 9999 TO Z-EXIT-LEVEL.
049604 Z-34-XIT.
049606     EXIT.
049608*
049610*****************************************************************
049612*    PROCEDURE TDB-ACTV-ADJUSTMENT
049614*****************************************************************
049616 Z-35-PROCEDURE.
049618*
049620     MOVE HOLD-TDA-ACTVC-CHG-FRM TO WS-CHG-WORK.
049622     IF HOLD-TDA-ACTVC-CODE = 0010
049624         NEXT SENTENCE ELSE
049626         GO TO Z-35-2-1-ELSE.
049628     MOVE WS-CHG-WK-X-3 TO HOLD-TDAA-CSR.
049630     GO TO Z-35-2-ENDIF.
049632 Z-35-2-1-ELSE.
049634     IF HOLD-TDA-ACTVC-CODE = 0011
049636         NEXT SENTENCE ELSE
049638         GO TO Z-35-2-2-ELSE.
049640     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-WTHLD-CD.
049642     GO TO Z-35-2-ENDIF.
049644 Z-35-2-2-ELSE.
049646     IF HOLD-TDA-ACTVC-CODE = 0012
049648         NEXT SENTENCE ELSE
049650         GO TO Z-35-2-3-ELSE.
049652     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-DT-CONDENSED.
049654     GO TO Z-35-2-ENDIF.
049656 Z-35-2-3-ELSE.
049658     IF HOLD-TDA-ACTVC-CODE = 0013
049660         NEXT SENTENCE ELSE
049662         GO TO Z-35-2-4-ELSE.
049664     MOVE WS-CHG-WK-X-24 TO HOLD-TDAA-FREE-MARK.
049666     GO TO Z-35-2-ENDIF.
049668 Z-35-2-4-ELSE.
049670     IF HOLD-TDA-ACTVC-CODE = 0014
049672         NEXT SENTENCE ELSE
049674         GO TO Z-35-2-5-ELSE.
049676     MOVE WS-CHG-WK-X-3 TO HOLD-TDAA-OFFICER.
049678     GO TO Z-35-2-ENDIF.
049680 Z-35-2-5-ELSE.
049682     IF HOLD-TDA-ACTVC-CODE = 0015
049684         NEXT SENTENCE ELSE
049686         GO TO Z-35-2-6-ELSE.
049688     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-CLASS-CD.
049690     GO TO Z-35-2-ENDIF.
049692 Z-35-2-6-ELSE.
049694     IF HOLD-TDA-ACTVC-CODE = 0016
049696         NEXT SENTENCE ELSE
049698         GO TO Z-35-2-7-ELSE.
049700     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-CORR-BK-CD.
049702     GO TO Z-35-2-ENDIF.
049704 Z-35-2-7-ELSE.
049706     IF HOLD-TDA-ACTVC-CODE = 0017
049708         NEXT SENTENCE ELSE
049710         GO TO Z-35-2-8-ELSE.
049712     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-PUBLIC-FUND.
049714     GO TO Z-35-2-ENDIF.
049716 Z-35-2-8-ELSE.
049718     IF HOLD-TDA-ACTVC-CODE = 0018
049720         NEXT SENTENCE ELSE
049722         GO TO Z-35-2-9-ELSE.
049724     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-TRUST-CD.
049726     GO TO Z-35-2-ENDIF.
049728 Z-35-2-9-ELSE.
049730     IF HOLD-TDA-ACTVC-CODE = 0019
049732         NEXT SENTENCE ELSE
049734         GO TO Z-35-2-10-ELSE.
049736     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-WTHDRW-ALLOW.
049738     GO TO Z-35-2-ENDIF.
049740 Z-35-2-10-ELSE.
049742     IF HOLD-TDA-ACTVC-CODE = 0020
049744         NEXT SENTENCE ELSE
049746         GO TO Z-35-2-11-ELSE.
049748     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-DPOSIT-ALLOW.
049750     GO TO Z-35-2-ENDIF.
049752 Z-35-2-11-ELSE.
049754     IF HOLD-TDA-ACTVC-CODE = 0021
049756         NEXT SENTENCE ELSE
049758         GO TO Z-35-2-12-ELSE.
049760     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-COMM-ACCT.
049762     GO TO Z-35-2-ENDIF.
049764 Z-35-2-12-ELSE.
049766     IF HOLD-TDA-ACTVC-CODE = 0022
049768         NEXT SENTENCE ELSE
049770         GO TO Z-35-2-13-ELSE.
049772     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-RT-FLOOR.
049774     GO TO Z-35-2-ENDIF.
049776 Z-35-2-13-ELSE.
049778     IF HOLD-TDA-ACTVC-CODE = 0023
049780         NEXT SENTENCE ELSE
049782         GO TO Z-35-2-14-ELSE.
049784     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-REPO-CD.
049786     GO TO Z-35-2-ENDIF.
049788 Z-35-2-14-ELSE.
049790     IF HOLD-TDA-ACTVC-CODE = 0024
049792         NEXT SENTENCE ELSE
049794         GO TO Z-35-2-15-ELSE.
049796     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-WTHD-REQD-CD.
049798     GO TO Z-35-2-ENDIF.
049800 Z-35-2-15-ELSE.
049802     IF HOLD-TDA-ACTVC-CODE = 0025
049804         NEXT SENTENCE ELSE
049806         GO TO Z-35-2-16-ELSE.
049808     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-POST-MAT.
049810     GO TO Z-35-2-ENDIF.
049812 Z-35-2-16-ELSE.
049814     IF HOLD-TDA-ACTVC-CODE = 0026
049816         NEXT SENTENCE ELSE
049818         GO TO Z-35-2-17-ELSE.
049820     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-INT-CD.
049822     GO TO Z-35-2-ENDIF.
049824 Z-35-2-17-ELSE.
049826     IF HOLD-TDA-ACTVC-CODE = 0027
049828         NEXT SENTENCE ELSE
049830         GO TO Z-35-2-18-ELSE.
049832     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-WTHLD-AMT.
049834     GO TO Z-35-2-ENDIF.
049836 Z-35-2-18-ELSE.
049838     IF HOLD-TDA-ACTVC-CODE = 0028
049840         NEXT SENTENCE ELSE
049842         GO TO Z-35-2-19-ELSE.
049844     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-SUM-STMT-CD.
049846     GO TO Z-35-2-ENDIF.
049848 Z-35-2-19-ELSE.
049850     IF HOLD-TDA-ACTVC-CODE = 0029
049852         NEXT SENTENCE ELSE
049854         GO TO Z-35-2-20-ELSE.
049856     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-RT-CHG-ALLOW.
049858     GO TO Z-35-2-ENDIF.
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 550 lines from 24376 to 24925.

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

