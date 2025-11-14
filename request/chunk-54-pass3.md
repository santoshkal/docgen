# LLM Request Debug File
Generated: 2025-11-13T22:05:52.138650

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 54/55
- **Model**: gpt-4.1
- **Chunk Number**: 54
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~9,027 tokens
- **Total Input**: ~10,985 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 54/55" (ID: detailed-code-explanation)

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


**CHUNK 54 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 54 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 25988 to 26515 (528 lines)\nChunk Tokens (estimated): ~8,049\nActual Input Tokens: 9,455 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 25988-26515 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 54 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 54 of 55.\n\n\n=============================================================================\nCHUNK 54 SOURCE CODE (Lines 25988-26515)\n=============================================================================\n\n```cobol\n051984 Z-35-2-197-ELSE.\n051986     IF HOLD-TDA-ACTVC-CODE = 0513\n051988         NEXT SENTENCE ELSE\n051990         GO TO Z-35-2-198-ELSE.\n051992     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-CR-CNT-STD.\n051994     GO TO Z-35-2-ENDIF.\n051996 Z-35-2-198-ELSE.\n051998     IF HOLD-TDA-ACTVC-CODE = 0514\n052000         NEXT SENTENCE ELSE\n052002         GO TO Z-35-2-199-ELSE.\n052004     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-CR-AMT-STD.\n052006     GO TO Z-35-2-ENDIF.\n052008 Z-35-2-199-ELSE.\n052010     IF HOLD-TDA-ACTVC-CODE = 0515\n052012         NEXT SENTENCE ELSE\n052014         GO TO Z-35-2-200-ELSE.\n052016     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-DB-CNT-STD.\n052018     GO TO Z-35-2-ENDIF.\n052020 Z-35-2-200-ELSE.\n052022     IF HOLD-TDA-ACTVC-CODE = 0516\n052024         NEXT SENTENCE ELSE\n052026         GO TO Z-35-2-201-ELSE.\n052028     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-DB-AMT-STD.\n052030     GO TO Z-35-2-ENDIF.\n052032 Z-35-2-201-ELSE.\n052034     IF HOLD-TDA-ACTVC-CODE = 0525\n052036         NEXT SENTENCE ELSE\n052038         GO TO Z-35-2-202-ELSE.\n052040     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-CR-CNT-YTD.\n052042     GO TO Z-35-2-ENDIF.\n052044 Z-35-2-202-ELSE.\n052046     IF HOLD-TDA-ACTVC-CODE = 0526\n052048         NEXT SENTENCE ELSE\n052050         GO TO Z-35-2-203-ELSE.\n052052     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-CR-AMT-YTD.\n052054     GO TO Z-35-2-ENDIF.\n052056 Z-35-2-203-ELSE.\n052058     IF HOLD-TDA-ACTVC-CODE = 0527\n052060         NEXT SENTENCE ELSE\n052062         GO TO Z-35-2-204-ELSE.\n052064     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-DB-CNT-YTD.\n052066     GO TO Z-35-2-ENDIF.\n052068 Z-35-2-204-ELSE.\n052070     IF HOLD-TDA-ACTVC-CODE = 0528\n052072         NEXT SENTENCE ELSE\n052074         GO TO Z-35-2-205-ELSE.\n052076     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-DB-AMT-YTD.\n052078     GO TO Z-35-2-ENDIF.\n052080 Z-35-2-205-ELSE.\n052082     IF HOLD-TDA-ACTVC-CODE = 0533\n052084         NEXT SENTENCE ELSE\n052086         GO TO Z-35-2-206-ELSE.\n052088     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-AVAIL-BAL.\n052090     GO TO Z-35-2-ENDIF.\n052092 Z-35-2-206-ELSE.\n052094     IF HOLD-TDA-ACTVC-CODE = 0536\n052096         NEXT SENTENCE ELSE\n052098         GO TO Z-35-2-207-ELSE.\n052100     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-BAL-BEG-STMT.\n052102     GO TO Z-35-2-ENDIF.\n052104 Z-35-2-207-ELSE.\n052106     IF HOLD-TDA-ACTVC-CODE = 0538\n052108         NEXT SENTENCE ELSE\n052110         GO TO Z-35-2-208-ELSE.\n052112     MOVE WS-CHG-WK-9-S6V4 TO HOLD-TDAA-ACCR-INT.\n052114     GO TO Z-35-2-ENDIF.\n052116 Z-35-2-208-ELSE.\n052118     IF HOLD-TDA-ACTVC-CODE = 0539\n052120         NEXT SENTENCE ELSE\n052122         GO TO Z-35-2-209-ELSE.\n052124     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-INT-TO-POST.\n052126     GO TO Z-35-2-ENDIF.\n052128 Z-35-2-209-ELSE.\n052130     IF HOLD-TDA-ACTVC-CODE = 0544\n052132         NEXT SENTENCE ELSE\n052134         GO TO Z-35-2-210-ELSE.\n052136     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-1099-YTD.\n052138     GO TO Z-35-2-ENDIF.\n052140 Z-35-2-210-ELSE.\n052142     IF HOLD-TDA-ACTVC-CODE = 0545\n052144         NEXT SENTENCE ELSE\n052146         GO TO Z-35-2-211-ELSE.\n052148     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-1099-LST-YR.\n052150     GO TO Z-35-2-ENDIF.\n052152 Z-35-2-211-ELSE.\n052154     IF HOLD-TDA-ACTVC-CODE = 0546\n052156         NEXT SENTENCE ELSE\n052158         GO TO Z-35-2-212-ELSE.\n052160     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-CURR-PENLTY.\n052162     GO TO Z-35-2-ENDIF.\n052164 Z-35-2-212-ELSE.\n052166     IF HOLD-TDA-ACTVC-CODE = 0547\n052168         NEXT SENTENCE ELSE\n052170         GO TO Z-35-2-213-ELSE.\n052172     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-PENLTY-YTD.\n052174     GO TO Z-35-2-ENDIF.\n052176 Z-35-2-213-ELSE.\n052178     IF HOLD-TDA-ACTVC-CODE = 0548\n052180         NEXT SENTENCE ELSE\n052182         GO TO Z-35-2-214-ELSE.\n052184     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-PENLTY-STD.\n052186     GO TO Z-35-2-ENDIF.\n052188 Z-35-2-214-ELSE.\n052190     IF HOLD-TDA-ACTVC-CODE = 0553\n052192         NEXT SENTENCE ELSE\n052194         GO TO Z-35-2-215-ELSE.\n052196     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-OID-RPT-INT.\n052198     GO TO Z-35-2-ENDIF.\n052200 Z-35-2-215-ELSE.\n052202     IF HOLD-TDA-ACTVC-CODE = 0554\n052204         NEXT SENTENCE ELSE\n052206         GO TO Z-35-2-216-ELSE.\n052208     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-CUR-WHLD-AMT.\n052210     GO TO Z-35-2-ENDIF.\n052212 Z-35-2-216-ELSE.\n052214     IF HOLD-TDA-ACTVC-CODE = 0555\n052216         NEXT SENTENCE ELSE\n052218         GO TO Z-35-2-217-ELSE.\n052220     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-WTHLD-STD.\n052222     GO TO Z-35-2-ENDIF.\n052224 Z-35-2-217-ELSE.\n052226     IF HOLD-TDA-ACTVC-CODE = 0556\n052228         NEXT SENTENCE ELSE\n052230         GO TO Z-35-2-218-ELSE.\n052232     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-END-OF-INT.\n052234     GO TO Z-35-2-ENDIF.\n052236 Z-35-2-218-ELSE.\n052238     IF HOLD-TDA-ACTVC-CODE = 0557\n052240         NEXT SENTENCE ELSE\n052242         GO TO Z-35-2-219-ELSE.\n052244     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-END-OF-MAT.\n052246     GO TO Z-35-2-ENDIF.\n052248 Z-35-2-219-ELSE.\n052250     IF HOLD-TDA-ACTVC-CODE = 0558\n052252         NEXT SENTENCE ELSE\n052254         GO TO Z-35-2-220-ELSE.\n052256     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-WTHLD-YTD.\n052258     GO TO Z-35-2-ENDIF.\n052260 Z-35-2-220-ELSE.\n052262     IF HOLD-TDA-ACTVC-CODE = 0559\n052264         NEXT SENTENCE ELSE\n052266         GO TO Z-35-2-221-ELSE.\n052268     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-END-OF-STMT.\n052270     GO TO Z-35-2-ENDIF.\n052272 Z-35-2-221-ELSE.\n052274     IF HOLD-TDA-ACTVC-CODE = 0560\n052276         NEXT SENTENCE ELSE\n052278         GO TO Z-35-2-222-ELSE.\n052280     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-END-OF-CMPD.\n052282     GO TO Z-35-2-ENDIF.\n052284 Z-35-2-222-ELSE.\n052286     IF HOLD-TDA-ACTVC-CODE = 0562\n052288         NEXT SENTENCE ELSE\n052290         GO TO Z-35-2-223-ELSE.\n052292     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-LST-INT-PMT.\n052294     GO TO Z-35-2-ENDIF.\n052296 Z-35-2-223-ELSE.\n052298     IF HOLD-TDA-ACTVC-CODE = 0565\n052300         NEXT SENTENCE ELSE\n052302         GO TO Z-35-2-224-ELSE.\n052304     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-CMPD-INT.\n052306     GO TO Z-35-2-ENDIF.\n052308 Z-35-2-224-ELSE.\n052310     IF HOLD-TDA-ACTVC-CODE = 0566\n052312         NEXT SENTENCE ELSE\n052314         GO TO Z-35-2-225-ELSE.\n052316     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-BAL-BEG-YR.\n052318     GO TO Z-35-2-ENDIF.\n052320 Z-35-2-225-ELSE.\n052322     IF HOLD-TDA-ACTVC-CODE = 0567\n052324         NEXT SENTENCE ELSE\n052326         GO TO Z-35-2-226-ELSE.\n052328     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-BAL-BEG-LYR.\n052330     GO TO Z-35-2-ENDIF.\n052332 Z-35-2-226-ELSE.\n052334     IF HOLD-TDA-ACTVC-CODE = 0572\n052336         NEXT SENTENCE ELSE\n052338         GO TO Z-35-2-227-ELSE.\n052340     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-MIN-BAL-STD.\n052342     GO TO Z-35-2-ENDIF.\n052344 Z-35-2-227-ELSE.\n052346     IF HOLD-TDA-ACTVC-CODE = 0575\n052348         NEXT SENTENCE ELSE\n052350         GO TO Z-35-2-228-ELSE.\n052352     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-MIN-BAL-YTD.\n052354     GO TO Z-35-2-ENDIF.\n052356 Z-35-2-228-ELSE.\n052358     IF HOLD-TDA-ACTVC-CODE = 0577\n052360         NEXT SENTENCE ELSE\n052362         GO TO Z-35-2-229-ELSE.\n052364     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-LMINBAL-STD.\n052366     GO TO Z-35-2-ENDIF.\n052368 Z-35-2-229-ELSE.\n052370     IF HOLD-TDA-ACTVC-CODE = 0583\n052372         NEXT SENTENCE ELSE\n052374         GO TO Z-35-2-230-ELSE.\n052376     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-CONV-DT.\n052378     GO TO Z-35-2-ENDIF.\n052380 Z-35-2-230-ELSE.\n052382     IF HOLD-TDA-ACTVC-CODE = 0584\n052384         NEXT SENTENCE ELSE\n052386         GO TO Z-35-2-231-ELSE.\n052388     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-BNF-DEATH-DT.\n052390     GO TO Z-35-2-ENDIF.\n052392 Z-35-2-231-ELSE.\n052394     IF HOLD-TDA-ACTVC-CODE = 0592\n052396         NEXT SENTENCE ELSE\n052398         GO TO Z-35-2-232-ELSE.\n052400     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-FLOOR-RT.\n052402     GO TO Z-35-2-ENDIF.\n052404 Z-35-2-232-ELSE.\n052406     IF HOLD-TDA-ACTVC-CODE = 0593\n052408         NEXT SENTENCE ELSE\n052410         GO TO Z-35-2-233-ELSE.\n052412     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-FLOOR-INCR.\n052414     GO TO Z-35-2-ENDIF.\n052416 Z-35-2-233-ELSE.\n052418     IF HOLD-TDA-ACTVC-CODE = 0594\n052420         NEXT SENTENCE ELSE\n052422         GO TO Z-35-2-234-ELSE.\n052424     MOVE WS-CHG-WK-9-6V4 TO HOLD-TDAA-PER-DIEM.\n052426     GO TO Z-35-2-ENDIF.\n052428 Z-35-2-234-ELSE.\n052430     IF HOLD-TDA-ACTVC-CODE = 0600\n052432         NEXT SENTENCE ELSE\n052434         GO TO Z-35-2-235-ELSE.\n052436     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-IN-PROC.\n052438     GO TO Z-35-2-ENDIF.\n052440 Z-35-2-235-ELSE.\n052442     IF HOLD-TDA-ACTVC-CODE = 0601\n052444         NEXT SENTENCE ELSE\n052446         GO TO Z-35-2-236-ELSE.\n052448     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-ACCR-DT.\n052450     GO TO Z-35-2-ENDIF.\n052452 Z-35-2-236-ELSE.\n052454     IF HOLD-TDA-ACTVC-CODE = 0604\n052456         NEXT SENTENCE ELSE\n052458         GO TO Z-35-2-237-ELSE.\n052460     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-LST-MAT-DT.\n052462     GO TO Z-35-2-ENDIF.\n052464 Z-35-2-237-ELSE.\n052466     IF HOLD-TDA-ACTVC-CODE = 0610\n052468         NEXT SENTENCE ELSE\n052470         GO TO Z-35-2-238-ELSE.\n052472     MOVE WS-CHG-WK-X-10 TO HOLD-TDAA-SHT-NAME.\n052474     GO TO Z-35-2-ENDIF.\n052476 Z-35-2-238-ELSE.\n052478     IF HOLD-TDA-ACTVC-CODE = 0611\n052480         NEXT SENTENCE ELSE\n052482         GO TO Z-35-2-239-ELSE.\n052484     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-LST-POST-DT.\n052486     GO TO Z-35-2-ENDIF.\n052488 Z-35-2-239-ELSE.\n052490     IF HOLD-TDA-ACTVC-CODE = 0615\n052492         NEXT SENTENCE ELSE\n052494         GO TO Z-35-2-240-ELSE.\n052496     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-CLSD-DT.\n052498     GO TO Z-35-2-ENDIF.\n052500 Z-35-2-240-ELSE.\n052502     IF HOLD-TDA-ACTVC-CODE = 0616\n052504         NEXT SENTENCE ELSE\n052506         GO TO Z-35-2-241-ELSE.\n052508     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-LST-CONTACT.\n052510     GO TO Z-35-2-ENDIF.\n052512 Z-35-2-241-ELSE.\n052514     IF HOLD-TDA-ACTVC-CODE = 0617\n052516         NEXT SENTENCE ELSE\n052518         GO TO Z-35-2-242-ELSE.\n052520     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-LST-DIST-DT.\n052522     GO TO Z-35-2-ENDIF.\n052524 Z-35-2-242-ELSE.\n052526     IF HOLD-TDA-ACTVC-CODE = 0618\n052528         NEXT SENTENCE ELSE\n052530         GO TO Z-35-2-243-ELSE.\n052532     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-LST-RTCHG-DT.\n052534     GO TO Z-35-2-ENDIF.\n052536 Z-35-2-243-ELSE.\n052538     IF HOLD-TDA-ACTVC-CODE = 0619\n052540         NEXT SENTENCE ELSE\n052542         GO TO Z-35-2-244-ELSE.\n052544     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-LST-STMT-DT.\n052546     GO TO Z-35-2-ENDIF.\n052548 Z-35-2-244-ELSE.\n052550     IF HOLD-TDA-ACTVC-CODE = 0620\n052552         NEXT SENTENCE ELSE\n052554         GO TO Z-35-2-245-ELSE.\n052556     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-CMPD-DT.\n052558     GO TO Z-35-2-ENDIF.\n052560 Z-35-2-245-ELSE.\n052562     IF HOLD-TDA-ACTVC-CODE = 0621\n052564         NEXT SENTENCE ELSE\n052566         GO TO Z-35-2-246-ELSE.\n052568     MOVE WS-CHG-WK-9-4 TO HOLD-TDAA-BRCH.\n052570     GO TO Z-35-2-ENDIF.\n052572 Z-35-2-246-ELSE.\n052574     IF HOLD-TDA-ACTVC-CODE = 0622\n052576         NEXT SENTENCE ELSE\n052578         GO TO Z-35-2-247-ELSE.\n052580     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-EOY-CD.\n052582     GO TO Z-35-2-ENDIF.\n052584 Z-35-2-247-ELSE.\n052586     IF HOLD-TDA-ACTVC-CODE = 0623\n052588         NEXT SENTENCE ELSE\n052590         GO TO Z-35-2-248-ELSE.\n052592     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-INQ-SECR-CD.\n052594     GO TO Z-35-2-ENDIF.\n052596 Z-35-2-248-ELSE.\n052598     IF HOLD-TDA-ACTVC-CODE = 0626\n052600         NEXT SENTENCE ELSE\n052602         GO TO Z-35-2-249-ELSE.\n052604     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-LST-FEE-DT.\n052606     GO TO Z-35-2-ENDIF.\n052608 Z-35-2-249-ELSE.\n052610     IF HOLD-TDA-ACTVC-CODE = 0627\n052612         NEXT SENTENCE ELSE\n052614         GO TO Z-35-2-250-ELSE.\n052616     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-FEE-DT.\n052618     GO TO Z-35-2-ENDIF.\n052620 Z-35-2-250-ELSE.\n052622     IF HOLD-TDA-ACTVC-CODE = 0628\n052624         NEXT SENTENCE ELSE\n052626         GO TO Z-35-2-251-ELSE.\n052628     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-POST-DT.\n052630     GO TO Z-35-2-ENDIF.\n052632 Z-35-2-251-ELSE.\n052634     IF HOLD-TDA-ACTVC-CODE = 0629\n052636         NEXT SENTENCE ELSE\n052638         GO TO Z-35-2-252-ELSE.\n052640     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-DIST-DT.\n052642     GO TO Z-35-2-ENDIF.\n052644 Z-35-2-252-ELSE.\n052646     IF HOLD-TDA-ACTVC-CODE = 0630\n052648         NEXT SENTENCE ELSE\n052650         GO TO Z-35-2-253-ELSE.\n052652     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-DS-PROC.\n052654     GO TO Z-35-2-ENDIF.\n052656 Z-35-2-253-ELSE.\n052658     IF HOLD-TDA-ACTVC-CODE = 0636\n052660         NEXT SENTENCE ELSE\n052662         GO TO Z-35-2-254-ELSE.\n052664     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-RT-CHG.\n052666     GO TO Z-35-2-ENDIF.\n052668 Z-35-2-254-ELSE.\n052670     IF HOLD-TDA-ACTVC-CODE = 0638\n052672         NEXT SENTENCE ELSE\n052674         GO TO Z-35-2-255-ELSE.\n052676     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-BNF-BIRTH-DT.\n052678     GO TO Z-35-2-ENDIF.\n052680 Z-35-2-255-ELSE.\n052682     IF HOLD-TDA-ACTVC-CODE = 0639\n052684         NEXT SENTENCE ELSE\n052686         GO TO Z-35-2-256-ELSE.\n052688     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-STMT-DT.\n052690     GO TO Z-35-2-ENDIF.\n052692 Z-35-2-256-ELSE.\n052694     IF HOLD-TDA-ACTVC-CODE = 0641\n052696         NEXT SENTENCE ELSE\n052698         GO TO Z-35-2-257-ELSE.\n052700     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (1).\n052702     GO TO Z-35-2-ENDIF.\n052704 Z-35-2-257-ELSE.\n052706     IF HOLD-TDA-ACTVC-CODE = 0642\n052708         NEXT SENTENCE ELSE\n052710         GO TO Z-35-2-258-ELSE.\n052712     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (2).\n052714     GO TO Z-35-2-ENDIF.\n052716 Z-35-2-258-ELSE.\n052718     IF HOLD-TDA-ACTVC-CODE = 0643\n052720         NEXT SENTENCE ELSE\n052722         GO TO Z-35-2-259-ELSE.\n052724     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (3).\n052726     GO TO Z-35-2-ENDIF.\n052728 Z-35-2-259-ELSE.\n052730     IF HOLD-TDA-ACTVC-CODE = 0644\n052732         NEXT SENTENCE ELSE\n052734         GO TO Z-35-2-260-ELSE.\n052736     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (4).\n052738     GO TO Z-35-2-ENDIF.\n052740 Z-35-2-260-ELSE.\n052742     IF HOLD-TDA-ACTVC-CODE = 0645\n052744         NEXT SENTENCE ELSE\n052746         GO TO Z-35-2-261-ELSE.\n052748     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (5).\n052750     GO TO Z-35-2-ENDIF.\n052752 Z-35-2-261-ELSE.\n052754     IF HOLD-TDA-ACTVC-CODE = 0646\n052756         NEXT SENTENCE ELSE\n052758         GO TO Z-35-2-262-ELSE.\n052760     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (6).\n052762     GO TO Z-35-2-ENDIF.\n052764 Z-35-2-262-ELSE.\n052766     IF HOLD-TDA-ACTVC-CODE = 0647\n052768         NEXT SENTENCE ELSE\n052770         GO TO Z-35-2-263-ELSE.\n052772     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (7).\n052774     GO TO Z-35-2-ENDIF.\n052776 Z-35-2-263-ELSE.\n052778     IF HOLD-TDA-ACTVC-CODE = 0648\n052780         NEXT SENTENCE ELSE\n052782         GO TO Z-35-2-264-ELSE.\n052784     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (8).\n052786     GO TO Z-35-2-ENDIF.\n052788 Z-35-2-264-ELSE.\n052790     IF HOLD-TDA-ACTVC-CODE = 0649\n052792         NEXT SENTENCE ELSE\n052794         GO TO Z-35-2-265-ELSE.\n052796     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (9).\n052798     GO TO Z-35-2-ENDIF.\n052800 Z-35-2-265-ELSE.\n052802     IF HOLD-TDA-ACTVC-CODE = 0650\n052804         NEXT SENTENCE ELSE\n052806         GO TO Z-35-2-266-ELSE.\n052808     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (10).\n052810     GO TO Z-35-2-ENDIF.\n052812 Z-35-2-266-ELSE.\n052814     IF HOLD-TDA-ACTVC-CODE = 0651\n052816         NEXT SENTENCE ELSE\n052818         GO TO Z-35-2-267-ELSE.\n052820     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (1).\n052822     GO TO Z-35-2-ENDIF.\n052824 Z-35-2-267-ELSE.\n052826     IF HOLD-TDA-ACTVC-CODE = 0652\n052828         NEXT SENTENCE ELSE\n052830         GO TO Z-35-2-268-ELSE.\n052832     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (2).\n052834     GO TO Z-35-2-ENDIF.\n052836 Z-35-2-268-ELSE.\n052838     IF HOLD-TDA-ACTVC-CODE = 0653\n052840         NEXT SENTENCE ELSE\n052842         GO TO Z-35-2-269-ELSE.\n052844     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (3).\n052846     GO TO Z-35-2-ENDIF.\n052848 Z-35-2-269-ELSE.\n052850     IF HOLD-TDA-ACTVC-CODE = 0654\n052852         NEXT SENTENCE ELSE\n052854         GO TO Z-35-2-270-ELSE.\n052856     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (4).\n052858     GO TO Z-35-2-ENDIF.\n052860 Z-35-2-270-ELSE.\n052862     IF HOLD-TDA-ACTVC-CODE = 0655\n052864         NEXT SENTENCE ELSE\n052866         GO TO Z-35-2-271-ELSE.\n052868     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (5).\n052870     GO TO Z-35-2-ENDIF.\n052872 Z-35-2-271-ELSE.\n052874     IF HOLD-TDA-ACTVC-CODE = 0656\n052876         NEXT SENTENCE ELSE\n052878         GO TO Z-35-2-272-ELSE.\n052880     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (6).\n052882     GO TO Z-35-2-ENDIF.\n052884 Z-35-2-272-ELSE.\n052886     IF HOLD-TDA-ACTVC-CODE = 0657\n052888         NEXT SENTENCE ELSE\n052890         GO TO Z-35-2-273-ELSE.\n052892     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (7).\n052894     GO TO Z-35-2-ENDIF.\n052896 Z-35-2-273-ELSE.\n052898     IF HOLD-TDA-ACTVC-CODE = 0658\n052900         NEXT SENTENCE ELSE\n052902         GO TO Z-35-2-274-ELSE.\n052904     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (8).\n052906     GO TO Z-35-2-ENDIF.\n052908 Z-35-2-274-ELSE.\n052910     IF HOLD-TDA-ACTVC-CODE = 0659\n052912         NEXT SENTENCE ELSE\n052914         GO TO Z-35-2-275-ELSE.\n052916     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (9).\n052918     GO TO Z-35-2-ENDIF.\n052920 Z-35-2-275-ELSE.\n052922     IF HOLD-TDA-ACTVC-CODE = 0660\n052924         NEXT SENTENCE ELSE\n052926         GO TO Z-35-2-276-ELSE.\n052928     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (10).\n052930     GO TO Z-35-2-ENDIF.\n052932 Z-35-2-276-ELSE.\n052934     IF HOLD-TDA-ACTVC-CODE = 669\n052936         NEXT SENTENCE ELSE\n052938         GO TO Z-35-2-277-ELSE.\n052940     MOVE WS-CHG-WK-X-3 TO HOLD-TDAA-TICKLER-FLAG.\n052942     GO TO Z-35-2-ENDIF.\n052944 Z-35-2-277-ELSE.\n052946     IF HOLD-TDA-ACTVC-CODE = 0811\n052948         NEXT SENTENCE ELSE\n052950         GO TO Z-35-2-278-ELSE.\n052952     MOVE WS-CHG-WORK TO HOLD-TDAC-NAME-1.\n052954     GO TO Z-35-2-ENDIF.\n052956 Z-35-2-278-ELSE.\n052958     IF HOLD-TDA-ACTVC-CODE = 0812\n052960         NEXT SENTENCE ELSE\n052962         GO TO Z-35-2-279-ELSE.\n052964     MOVE WS-CHG-WORK TO HOLD-TDAC-NAME-2.\n052966     GO TO Z-35-2-ENDIF.\n052968 Z-35-2-279-ELSE.\n052970     IF HOLD-TDA-ACTVC-CODE = 0813\n052972         NEXT SENTENCE ELSE\n052974         GO TO Z-35-2-280-ELSE.\n052976     MOVE WS-CHG-WORK TO HOLD-TDAC-ADDR-1.\n052978     GO TO Z-35-2-ENDIF.\n052980 Z-35-2-280-ELSE.\n052982     IF HOLD-TDA-ACTVC-CODE = 0814\n052984         NEXT SENTENCE ELSE\n052986         GO TO Z-35-2-281-ELSE.\n052988     MOVE WS-CHG-WORK TO HOLD-TDAC-ADDR-2.\n052990     GO TO Z-35-2-ENDIF.\n052992 Z-35-2-281-ELSE.\n052994     IF HOLD-TDA-ACTVC-CODE = 0815\n052996         NEXT SENTENCE ELSE\n052998         GO TO Z-35-2-282-ELSE.\n053000     MOVE WS-CHG-WK-X-20 TO HOLD-TDAC-CITY.\n053002     GO TO Z-35-2-ENDIF.\n053004 Z-35-2-282-ELSE.\n053006     IF HOLD-TDA-ACTVC-CODE = 0816\n053008         NEXT SENTENCE ELSE\n053010         GO TO Z-35-2-283-ELSE.\n053012     MOVE WS-CHG-WK-X-9 TO HOLD-TDAC-ZIP-CODE.\n053014     GO TO Z-35-2-ENDIF.\n053016 Z-35-2-283-ELSE.\n053018     IF HOLD-TDA-ACTVC-CODE = 0817\n053020         NEXT SENTENCE ELSE\n053022         GO TO Z-35-2-284-ELSE.\n053024     MOVE WS-CHG-WK-9-9 TO HOLD-TDAC-TIN-NBR.\n053026     GO TO Z-35-2-ENDIF.\n053028 Z-35-2-284-ELSE.\n053030     IF HOLD-TDA-ACTVC-CODE = 0818\n053032         NEXT SENTENCE ELSE\n053034         GO TO Z-35-2-285-ELSE.\n053036     MOVE WS-CHG-WK-X-2 TO HOLD-TDAC-STATE.\n053038     GO TO Z-35-2-ENDIF.\n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 528 lines from 25988 to 26515.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 54,
  "total_chunks": 55,
  "start_line": 25988,
  "end_line": 26515,
  "line_count": 528
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
- Source code length: 26648 characters

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
CHUNK 54 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 25988 to 26515 (528 lines)
Chunk Tokens (estimated): ~8,049
Actual Input Tokens: 9,455 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 25988-26515 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 54 of 55 chunks
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
      The source code below is only CHUNK 54 of 55.


=============================================================================
CHUNK 54 SOURCE CODE (Lines 25988-26515)
=============================================================================

```cobol
051984 Z-35-2-197-ELSE.
051986     IF HOLD-TDA-ACTVC-CODE = 0513
051988         NEXT SENTENCE ELSE
051990         GO TO Z-35-2-198-ELSE.
051992     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-CR-CNT-STD.
051994     GO TO Z-35-2-ENDIF.
051996 Z-35-2-198-ELSE.
051998     IF HOLD-TDA-ACTVC-CODE = 0514
052000         NEXT SENTENCE ELSE
052002         GO TO Z-35-2-199-ELSE.
052004     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-CR-AMT-STD.
052006     GO TO Z-35-2-ENDIF.
052008 Z-35-2-199-ELSE.
052010     IF HOLD-TDA-ACTVC-CODE = 0515
052012         NEXT SENTENCE ELSE
052014         GO TO Z-35-2-200-ELSE.
052016     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-DB-CNT-STD.
052018     GO TO Z-35-2-ENDIF.
052020 Z-35-2-200-ELSE.
052022     IF HOLD-TDA-ACTVC-CODE = 0516
052024         NEXT SENTENCE ELSE
052026         GO TO Z-35-2-201-ELSE.
052028     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-DB-AMT-STD.
052030     GO TO Z-35-2-ENDIF.
052032 Z-35-2-201-ELSE.
052034     IF HOLD-TDA-ACTVC-CODE = 0525
052036         NEXT SENTENCE ELSE
052038         GO TO Z-35-2-202-ELSE.
052040     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-CR-CNT-YTD.
052042     GO TO Z-35-2-ENDIF.
052044 Z-35-2-202-ELSE.
052046     IF HOLD-TDA-ACTVC-CODE = 0526
052048         NEXT SENTENCE ELSE
052050         GO TO Z-35-2-203-ELSE.
052052     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-CR-AMT-YTD.
052054     GO TO Z-35-2-ENDIF.
052056 Z-35-2-203-ELSE.
052058     IF HOLD-TDA-ACTVC-CODE = 0527
052060         NEXT SENTENCE ELSE
052062         GO TO Z-35-2-204-ELSE.
052064     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-DB-CNT-YTD.
052066     GO TO Z-35-2-ENDIF.
052068 Z-35-2-204-ELSE.
052070     IF HOLD-TDA-ACTVC-CODE = 0528
052072         NEXT SENTENCE ELSE
052074         GO TO Z-35-2-205-ELSE.
052076     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-DB-AMT-YTD.
052078     GO TO Z-35-2-ENDIF.
052080 Z-35-2-205-ELSE.
052082     IF HOLD-TDA-ACTVC-CODE = 0533
052084         NEXT SENTENCE ELSE
052086         GO TO Z-35-2-206-ELSE.
052088     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-AVAIL-BAL.
052090     GO TO Z-35-2-ENDIF.
052092 Z-35-2-206-ELSE.
052094     IF HOLD-TDA-ACTVC-CODE = 0536
052096         NEXT SENTENCE ELSE
052098         GO TO Z-35-2-207-ELSE.
052100     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-BAL-BEG-STMT.
052102     GO TO Z-35-2-ENDIF.
052104 Z-35-2-207-ELSE.
052106     IF HOLD-TDA-ACTVC-CODE = 0538
052108         NEXT SENTENCE ELSE
052110         GO TO Z-35-2-208-ELSE.
052112     MOVE WS-CHG-WK-9-S6V4 TO HOLD-TDAA-ACCR-INT.
052114     GO TO Z-35-2-ENDIF.
052116 Z-35-2-208-ELSE.
052118     IF HOLD-TDA-ACTVC-CODE = 0539
052120         NEXT SENTENCE ELSE
052122         GO TO Z-35-2-209-ELSE.
052124     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-INT-TO-POST.
052126     GO TO Z-35-2-ENDIF.
052128 Z-35-2-209-ELSE.
052130     IF HOLD-TDA-ACTVC-CODE = 0544
052132         NEXT SENTENCE ELSE
052134         GO TO Z-35-2-210-ELSE.
052136     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-1099-YTD.
052138     GO TO Z-35-2-ENDIF.
052140 Z-35-2-210-ELSE.
052142     IF HOLD-TDA-ACTVC-CODE = 0545
052144         NEXT SENTENCE ELSE
052146         GO TO Z-35-2-211-ELSE.
052148     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-1099-LST-YR.
052150     GO TO Z-35-2-ENDIF.
052152 Z-35-2-211-ELSE.
052154     IF HOLD-TDA-ACTVC-CODE = 0546
052156         NEXT SENTENCE ELSE
052158         GO TO Z-35-2-212-ELSE.
052160     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-CURR-PENLTY.
052162     GO TO Z-35-2-ENDIF.
052164 Z-35-2-212-ELSE.
052166     IF HOLD-TDA-ACTVC-CODE = 0547
052168         NEXT SENTENCE ELSE
052170         GO TO Z-35-2-213-ELSE.
052172     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-PENLTY-YTD.
052174     GO TO Z-35-2-ENDIF.
052176 Z-35-2-213-ELSE.
052178     IF HOLD-TDA-ACTVC-CODE = 0548
052180         NEXT SENTENCE ELSE
052182         GO TO Z-35-2-214-ELSE.
052184     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-PENLTY-STD.
052186     GO TO Z-35-2-ENDIF.
052188 Z-35-2-214-ELSE.
052190     IF HOLD-TDA-ACTVC-CODE = 0553
052192         NEXT SENTENCE ELSE
052194         GO TO Z-35-2-215-ELSE.
052196     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-OID-RPT-INT.
052198     GO TO Z-35-2-ENDIF.
052200 Z-35-2-215-ELSE.
052202     IF HOLD-TDA-ACTVC-CODE = 0554
052204         NEXT SENTENCE ELSE
052206         GO TO Z-35-2-216-ELSE.
052208     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-CUR-WHLD-AMT.
052210     GO TO Z-35-2-ENDIF.
052212 Z-35-2-216-ELSE.
052214     IF HOLD-TDA-ACTVC-CODE = 0555
052216         NEXT SENTENCE ELSE
052218         GO TO Z-35-2-217-ELSE.
052220     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-WTHLD-STD.
052222     GO TO Z-35-2-ENDIF.
052224 Z-35-2-217-ELSE.
052226     IF HOLD-TDA-ACTVC-CODE = 0556
052228         NEXT SENTENCE ELSE
052230         GO TO Z-35-2-218-ELSE.
052232     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-END-OF-INT.
052234     GO TO Z-35-2-ENDIF.
052236 Z-35-2-218-ELSE.
052238     IF HOLD-TDA-ACTVC-CODE = 0557
052240         NEXT SENTENCE ELSE
052242         GO TO Z-35-2-219-ELSE.
052244     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-END-OF-MAT.
052246     GO TO Z-35-2-ENDIF.
052248 Z-35-2-219-ELSE.
052250     IF HOLD-TDA-ACTVC-CODE = 0558
052252         NEXT SENTENCE ELSE
052254         GO TO Z-35-2-220-ELSE.
052256     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-WTHLD-YTD.
052258     GO TO Z-35-2-ENDIF.
052260 Z-35-2-220-ELSE.
052262     IF HOLD-TDA-ACTVC-CODE = 0559
052264         NEXT SENTENCE ELSE
052266         GO TO Z-35-2-221-ELSE.
052268     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-END-OF-STMT.
052270     GO TO Z-35-2-ENDIF.
052272 Z-35-2-221-ELSE.
052274     IF HOLD-TDA-ACTVC-CODE = 0560
052276         NEXT SENTENCE ELSE
052278         GO TO Z-35-2-222-ELSE.
052280     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-END-OF-CMPD.
052282     GO TO Z-35-2-ENDIF.
052284 Z-35-2-222-ELSE.
052286     IF HOLD-TDA-ACTVC-CODE = 0562
052288         NEXT SENTENCE ELSE
052290         GO TO Z-35-2-223-ELSE.
052292     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-LST-INT-PMT.
052294     GO TO Z-35-2-ENDIF.
052296 Z-35-2-223-ELSE.
052298     IF HOLD-TDA-ACTVC-CODE = 0565
052300         NEXT SENTENCE ELSE
052302         GO TO Z-35-2-224-ELSE.
052304     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-CMPD-INT.
052306     GO TO Z-35-2-ENDIF.
052308 Z-35-2-224-ELSE.
052310     IF HOLD-TDA-ACTVC-CODE = 0566
052312         NEXT SENTENCE ELSE
052314         GO TO Z-35-2-225-ELSE.
052316     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-BAL-BEG-YR.
052318     GO TO Z-35-2-ENDIF.
052320 Z-35-2-225-ELSE.
052322     IF HOLD-TDA-ACTVC-CODE = 0567
052324         NEXT SENTENCE ELSE
052326         GO TO Z-35-2-226-ELSE.
052328     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-BAL-BEG-LYR.
052330     GO TO Z-35-2-ENDIF.
052332 Z-35-2-226-ELSE.
052334     IF HOLD-TDA-ACTVC-CODE = 0572
052336         NEXT SENTENCE ELSE
052338         GO TO Z-35-2-227-ELSE.
052340     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-MIN-BAL-STD.
052342     GO TO Z-35-2-ENDIF.
052344 Z-35-2-227-ELSE.
052346     IF HOLD-TDA-ACTVC-CODE = 0575
052348         NEXT SENTENCE ELSE
052350         GO TO Z-35-2-228-ELSE.
052352     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-MIN-BAL-YTD.
052354     GO TO Z-35-2-ENDIF.
052356 Z-35-2-228-ELSE.
052358     IF HOLD-TDA-ACTVC-CODE = 0577
052360         NEXT SENTENCE ELSE
052362         GO TO Z-35-2-229-ELSE.
052364     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-LMINBAL-STD.
052366     GO TO Z-35-2-ENDIF.
052368 Z-35-2-229-ELSE.
052370     IF HOLD-TDA-ACTVC-CODE = 0583
052372         NEXT SENTENCE ELSE
052374         GO TO Z-35-2-230-ELSE.
052376     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-CONV-DT.
052378     GO TO Z-35-2-ENDIF.
052380 Z-35-2-230-ELSE.
052382     IF HOLD-TDA-ACTVC-CODE = 0584
052384         NEXT SENTENCE ELSE
052386         GO TO Z-35-2-231-ELSE.
052388     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-BNF-DEATH-DT.
052390     GO TO Z-35-2-ENDIF.
052392 Z-35-2-231-ELSE.
052394     IF HOLD-TDA-ACTVC-CODE = 0592
052396         NEXT SENTENCE ELSE
052398         GO TO Z-35-2-232-ELSE.
052400     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-FLOOR-RT.
052402     GO TO Z-35-2-ENDIF.
052404 Z-35-2-232-ELSE.
052406     IF HOLD-TDA-ACTVC-CODE = 0593
052408         NEXT SENTENCE ELSE
052410         GO TO Z-35-2-233-ELSE.
052412     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-FLOOR-INCR.
052414     GO TO Z-35-2-ENDIF.
052416 Z-35-2-233-ELSE.
052418     IF HOLD-TDA-ACTVC-CODE = 0594
052420         NEXT SENTENCE ELSE
052422         GO TO Z-35-2-234-ELSE.
052424     MOVE WS-CHG-WK-9-6V4 TO HOLD-TDAA-PER-DIEM.
052426     GO TO Z-35-2-ENDIF.
052428 Z-35-2-234-ELSE.
052430     IF HOLD-TDA-ACTVC-CODE = 0600
052432         NEXT SENTENCE ELSE
052434         GO TO Z-35-2-235-ELSE.
052436     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-IN-PROC.
052438     GO TO Z-35-2-ENDIF.
052440 Z-35-2-235-ELSE.
052442     IF HOLD-TDA-ACTVC-CODE = 0601
052444         NEXT SENTENCE ELSE
052446         GO TO Z-35-2-236-ELSE.
052448     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-ACCR-DT.
052450     GO TO Z-35-2-ENDIF.
052452 Z-35-2-236-ELSE.
052454     IF HOLD-TDA-ACTVC-CODE = 0604
052456         NEXT SENTENCE ELSE
052458         GO TO Z-35-2-237-ELSE.
052460     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-LST-MAT-DT.
052462     GO TO Z-35-2-ENDIF.
052464 Z-35-2-237-ELSE.
052466     IF HOLD-TDA-ACTVC-CODE = 0610
052468         NEXT SENTENCE ELSE
052470         GO TO Z-35-2-238-ELSE.
052472     MOVE WS-CHG-WK-X-10 TO HOLD-TDAA-SHT-NAME.
052474     GO TO Z-35-2-ENDIF.
052476 Z-35-2-238-ELSE.
052478     IF HOLD-TDA-ACTVC-CODE = 0611
052480         NEXT SENTENCE ELSE
052482         GO TO Z-35-2-239-ELSE.
052484     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-LST-POST-DT.
052486     GO TO Z-35-2-ENDIF.
052488 Z-35-2-239-ELSE.
052490     IF HOLD-TDA-ACTVC-CODE = 0615
052492         NEXT SENTENCE ELSE
052494         GO TO Z-35-2-240-ELSE.
052496     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-CLSD-DT.
052498     GO TO Z-35-2-ENDIF.
052500 Z-35-2-240-ELSE.
052502     IF HOLD-TDA-ACTVC-CODE = 0616
052504         NEXT SENTENCE ELSE
052506         GO TO Z-35-2-241-ELSE.
052508     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-LST-CONTACT.
052510     GO TO Z-35-2-ENDIF.
052512 Z-35-2-241-ELSE.
052514     IF HOLD-TDA-ACTVC-CODE = 0617
052516         NEXT SENTENCE ELSE
052518         GO TO Z-35-2-242-ELSE.
052520     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-LST-DIST-DT.
052522     GO TO Z-35-2-ENDIF.
052524 Z-35-2-242-ELSE.
052526     IF HOLD-TDA-ACTVC-CODE = 0618
052528         NEXT SENTENCE ELSE
052530         GO TO Z-35-2-243-ELSE.
052532     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-LST-RTCHG-DT.
052534     GO TO Z-35-2-ENDIF.
052536 Z-35-2-243-ELSE.
052538     IF HOLD-TDA-ACTVC-CODE = 0619
052540         NEXT SENTENCE ELSE
052542         GO TO Z-35-2-244-ELSE.
052544     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-LST-STMT-DT.
052546     GO TO Z-35-2-ENDIF.
052548 Z-35-2-244-ELSE.
052550     IF HOLD-TDA-ACTVC-CODE = 0620
052552         NEXT SENTENCE ELSE
052554         GO TO Z-35-2-245-ELSE.
052556     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-CMPD-DT.
052558     GO TO Z-35-2-ENDIF.
052560 Z-35-2-245-ELSE.
052562     IF HOLD-TDA-ACTVC-CODE = 0621
052564         NEXT SENTENCE ELSE
052566         GO TO Z-35-2-246-ELSE.
052568     MOVE WS-CHG-WK-9-4 TO HOLD-TDAA-BRCH.
052570     GO TO Z-35-2-ENDIF.
052572 Z-35-2-246-ELSE.
052574     IF HOLD-TDA-ACTVC-CODE = 0622
052576         NEXT SENTENCE ELSE
052578         GO TO Z-35-2-247-ELSE.
052580     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-EOY-CD.
052582     GO TO Z-35-2-ENDIF.
052584 Z-35-2-247-ELSE.
052586     IF HOLD-TDA-ACTVC-CODE = 0623
052588         NEXT SENTENCE ELSE
052590         GO TO Z-35-2-248-ELSE.
052592     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-INQ-SECR-CD.
052594     GO TO Z-35-2-ENDIF.
052596 Z-35-2-248-ELSE.
052598     IF HOLD-TDA-ACTVC-CODE = 0626
052600         NEXT SENTENCE ELSE
052602         GO TO Z-35-2-249-ELSE.
052604     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-LST-FEE-DT.
052606     GO TO Z-35-2-ENDIF.
052608 Z-35-2-249-ELSE.
052610     IF HOLD-TDA-ACTVC-CODE = 0627
052612         NEXT SENTENCE ELSE
052614         GO TO Z-35-2-250-ELSE.
052616     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-FEE-DT.
052618     GO TO Z-35-2-ENDIF.
052620 Z-35-2-250-ELSE.
052622     IF HOLD-TDA-ACTVC-CODE = 0628
052624         NEXT SENTENCE ELSE
052626         GO TO Z-35-2-251-ELSE.
052628     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-POST-DT.
052630     GO TO Z-35-2-ENDIF.
052632 Z-35-2-251-ELSE.
052634     IF HOLD-TDA-ACTVC-CODE = 0629
052636         NEXT SENTENCE ELSE
052638         GO TO Z-35-2-252-ELSE.
052640     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-DIST-DT.
052642     GO TO Z-35-2-ENDIF.
052644 Z-35-2-252-ELSE.
052646     IF HOLD-TDA-ACTVC-CODE = 0630
052648         NEXT SENTENCE ELSE
052650         GO TO Z-35-2-253-ELSE.
052652     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-DS-PROC.
052654     GO TO Z-35-2-ENDIF.
052656 Z-35-2-253-ELSE.
052658     IF HOLD-TDA-ACTVC-CODE = 0636
052660         NEXT SENTENCE ELSE
052662         GO TO Z-35-2-254-ELSE.
052664     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-RT-CHG.
052666     GO TO Z-35-2-ENDIF.
052668 Z-35-2-254-ELSE.
052670     IF HOLD-TDA-ACTVC-CODE = 0638
052672         NEXT SENTENCE ELSE
052674         GO TO Z-35-2-255-ELSE.
052676     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-BNF-BIRTH-DT.
052678     GO TO Z-35-2-ENDIF.
052680 Z-35-2-255-ELSE.
052682     IF HOLD-TDA-ACTVC-CODE = 0639
052684         NEXT SENTENCE ELSE
052686         GO TO Z-35-2-256-ELSE.
052688     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-STMT-DT.
052690     GO TO Z-35-2-ENDIF.
052692 Z-35-2-256-ELSE.
052694     IF HOLD-TDA-ACTVC-CODE = 0641
052696         NEXT SENTENCE ELSE
052698         GO TO Z-35-2-257-ELSE.
052700     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (1).
052702     GO TO Z-35-2-ENDIF.
052704 Z-35-2-257-ELSE.
052706     IF HOLD-TDA-ACTVC-CODE = 0642
052708         NEXT SENTENCE ELSE
052710         GO TO Z-35-2-258-ELSE.
052712     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (2).
052714     GO TO Z-35-2-ENDIF.
052716 Z-35-2-258-ELSE.
052718     IF HOLD-TDA-ACTVC-CODE = 0643
052720         NEXT SENTENCE ELSE
052722         GO TO Z-35-2-259-ELSE.
052724     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (3).
052726     GO TO Z-35-2-ENDIF.
052728 Z-35-2-259-ELSE.
052730     IF HOLD-TDA-ACTVC-CODE = 0644
052732         NEXT SENTENCE ELSE
052734         GO TO Z-35-2-260-ELSE.
052736     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (4).
052738     GO TO Z-35-2-ENDIF.
052740 Z-35-2-260-ELSE.
052742     IF HOLD-TDA-ACTVC-CODE = 0645
052744         NEXT SENTENCE ELSE
052746         GO TO Z-35-2-261-ELSE.
052748     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (5).
052750     GO TO Z-35-2-ENDIF.
052752 Z-35-2-261-ELSE.
052754     IF HOLD-TDA-ACTVC-CODE = 0646
052756         NEXT SENTENCE ELSE
052758         GO TO Z-35-2-262-ELSE.
052760     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (6).
052762     GO TO Z-35-2-ENDIF.
052764 Z-35-2-262-ELSE.
052766     IF HOLD-TDA-ACTVC-CODE = 0647
052768         NEXT SENTENCE ELSE
052770         GO TO Z-35-2-263-ELSE.
052772     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (7).
052774     GO TO Z-35-2-ENDIF.
052776 Z-35-2-263-ELSE.
052778     IF HOLD-TDA-ACTVC-CODE = 0648
052780         NEXT SENTENCE ELSE
052782         GO TO Z-35-2-264-ELSE.
052784     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (8).
052786     GO TO Z-35-2-ENDIF.
052788 Z-35-2-264-ELSE.
052790     IF HOLD-TDA-ACTVC-CODE = 0649
052792         NEXT SENTENCE ELSE
052794         GO TO Z-35-2-265-ELSE.
052796     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (9).
052798     GO TO Z-35-2-ENDIF.
052800 Z-35-2-265-ELSE.
052802     IF HOLD-TDA-ACTVC-CODE = 0650
052804         NEXT SENTENCE ELSE
052806         GO TO Z-35-2-266-ELSE.
052808     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-RISE-RATE (10).
052810     GO TO Z-35-2-ENDIF.
052812 Z-35-2-266-ELSE.
052814     IF HOLD-TDA-ACTVC-CODE = 0651
052816         NEXT SENTENCE ELSE
052818         GO TO Z-35-2-267-ELSE.
052820     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (1).
052822     GO TO Z-35-2-ENDIF.
052824 Z-35-2-267-ELSE.
052826     IF HOLD-TDA-ACTVC-CODE = 0652
052828         NEXT SENTENCE ELSE
052830         GO TO Z-35-2-268-ELSE.
052832     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (2).
052834     GO TO Z-35-2-ENDIF.
052836 Z-35-2-268-ELSE.
052838     IF HOLD-TDA-ACTVC-CODE = 0653
052840         NEXT SENTENCE ELSE
052842         GO TO Z-35-2-269-ELSE.
052844     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (3).
052846     GO TO Z-35-2-ENDIF.
052848 Z-35-2-269-ELSE.
052850     IF HOLD-TDA-ACTVC-CODE = 0654
052852         NEXT SENTENCE ELSE
052854         GO TO Z-35-2-270-ELSE.
052856     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (4).
052858     GO TO Z-35-2-ENDIF.
052860 Z-35-2-270-ELSE.
052862     IF HOLD-TDA-ACTVC-CODE = 0655
052864         NEXT SENTENCE ELSE
052866         GO TO Z-35-2-271-ELSE.
052868     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (5).
052870     GO TO Z-35-2-ENDIF.
052872 Z-35-2-271-ELSE.
052874     IF HOLD-TDA-ACTVC-CODE = 0656
052876         NEXT SENTENCE ELSE
052878         GO TO Z-35-2-272-ELSE.
052880     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (6).
052882     GO TO Z-35-2-ENDIF.
052884 Z-35-2-272-ELSE.
052886     IF HOLD-TDA-ACTVC-CODE = 0657
052888         NEXT SENTENCE ELSE
052890         GO TO Z-35-2-273-ELSE.
052892     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (7).
052894     GO TO Z-35-2-ENDIF.
052896 Z-35-2-273-ELSE.
052898     IF HOLD-TDA-ACTVC-CODE = 0658
052900         NEXT SENTENCE ELSE
052902         GO TO Z-35-2-274-ELSE.
052904     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (8).
052906     GO TO Z-35-2-ENDIF.
052908 Z-35-2-274-ELSE.
052910     IF HOLD-TDA-ACTVC-CODE = 0659
052912         NEXT SENTENCE ELSE
052914         GO TO Z-35-2-275-ELSE.
052916     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (9).
052918     GO TO Z-35-2-ENDIF.
052920 Z-35-2-275-ELSE.
052922     IF HOLD-TDA-ACTVC-CODE = 0660
052924         NEXT SENTENCE ELSE
052926         GO TO Z-35-2-276-ELSE.
052928     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-RR-CYC-DT (10).
052930     GO TO Z-35-2-ENDIF.
052932 Z-35-2-276-ELSE.
052934     IF HOLD-TDA-ACTVC-CODE = 669
052936         NEXT SENTENCE ELSE
052938         GO TO Z-35-2-277-ELSE.
052940     MOVE WS-CHG-WK-X-3 TO HOLD-TDAA-TICKLER-FLAG.
052942     GO TO Z-35-2-ENDIF.
052944 Z-35-2-277-ELSE.
052946     IF HOLD-TDA-ACTVC-CODE = 0811
052948         NEXT SENTENCE ELSE
052950         GO TO Z-35-2-278-ELSE.
052952     MOVE WS-CHG-WORK TO HOLD-TDAC-NAME-1.
052954     GO TO Z-35-2-ENDIF.
052956 Z-35-2-278-ELSE.
052958     IF HOLD-TDA-ACTVC-CODE = 0812
052960         NEXT SENTENCE ELSE
052962         GO TO Z-35-2-279-ELSE.
052964     MOVE WS-CHG-WORK TO HOLD-TDAC-NAME-2.
052966     GO TO Z-35-2-ENDIF.
052968 Z-35-2-279-ELSE.
052970     IF HOLD-TDA-ACTVC-CODE = 0813
052972         NEXT SENTENCE ELSE
052974         GO TO Z-35-2-280-ELSE.
052976     MOVE WS-CHG-WORK TO HOLD-TDAC-ADDR-1.
052978     GO TO Z-35-2-ENDIF.
052980 Z-35-2-280-ELSE.
052982     IF HOLD-TDA-ACTVC-CODE = 0814
052984         NEXT SENTENCE ELSE
052986         GO TO Z-35-2-281-ELSE.
052988     MOVE WS-CHG-WORK TO HOLD-TDAC-ADDR-2.
052990     GO TO Z-35-2-ENDIF.
052992 Z-35-2-281-ELSE.
052994     IF HOLD-TDA-ACTVC-CODE = 0815
052996         NEXT SENTENCE ELSE
052998         GO TO Z-35-2-282-ELSE.
053000     MOVE WS-CHG-WK-X-20 TO HOLD-TDAC-CITY.
053002     GO TO Z-35-2-ENDIF.
053004 Z-35-2-282-ELSE.
053006     IF HOLD-TDA-ACTVC-CODE = 0816
053008         NEXT SENTENCE ELSE
053010         GO TO Z-35-2-283-ELSE.
053012     MOVE WS-CHG-WK-X-9 TO HOLD-TDAC-ZIP-CODE.
053014     GO TO Z-35-2-ENDIF.
053016 Z-35-2-283-ELSE.
053018     IF HOLD-TDA-ACTVC-CODE = 0817
053020         NEXT SENTENCE ELSE
053022         GO TO Z-35-2-284-ELSE.
053024     MOVE WS-CHG-WK-9-9 TO HOLD-TDAC-TIN-NBR.
053026     GO TO Z-35-2-ENDIF.
053028 Z-35-2-284-ELSE.
053030     IF HOLD-TDA-ACTVC-CODE = 0818
053032         NEXT SENTENCE ELSE
053034         GO TO Z-35-2-285-ELSE.
053036     MOVE WS-CHG-WK-X-2 TO HOLD-TDAC-STATE.
053038     GO TO Z-35-2-ENDIF.
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 528 lines from 25988 to 26515.

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

