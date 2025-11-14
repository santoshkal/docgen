# LLM Request Debug File
Generated: 2025-11-13T20:37:01.182165

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 18/55
- **Model**: gpt-4.1
- **Chunk Number**: 18
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~7,434 tokens
- **Total Input**: ~9,392 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 18/55" (ID: detailed-code-explanation)

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


**CHUNK 18 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 18 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 8652 to 8839 (188 lines)\nChunk Tokens (estimated): ~4,154\nActual Input Tokens: 5,560 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 8652-8839 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 18 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 18 of 55.\n\n\n=============================================================================\nCHUNK 18 SOURCE CODE (Lines 8652-8839)\n=============================================================================\n\n```cobol\n017312                         OLD-TDAA-MANUAL-RT-X.                    \n017314                 20  OLD-TDAA-MANUAL-RT  PIC 9(2)V9(3).           \n017316                                                                  \n017318     05  OLD-TDAIRA-DATA               PIC X(1400).               \n017320     05  OLD-TDAIRA.                                              \n017322         10  OLD-TDAI-BANK             PIC 9(4).                  \n017324         10  OLD-TDAI-BRCH             PIC 9(4).                  \n017326         10  OLD-TDAI-APPL             PIC 9(1).                  \n017328         10  OLD-TDAI-CUST             PIC 9(12).                 \n017330         10  OLD-TDAI-ACCT             PIC 9(10).                 \n017332         10  OLD-TDAI-PUB-ID           PIC X(8).                  \n017334         10  OLD-TDAI-ADD-DT           PIC 9(8).                  \n017336         10  OLD-TDAI-ADD-TM           PIC 9(6).                  \n017338         10  OLD-TDAI-DS-TYPE          PIC X(2)                   \n017340                          OCCURS 20 TIMES.                        \n017342         10  OLD-TDAI-CN-TYPE          PIC 9(2)                   \n017344                          OCCURS 20 TIMES.                        \n017346         10  OLD-TDAI-DS-CN-AMT        PIC S9(12)V99              \n017348                          OCCURS 20 TIMES.                        \n017350         10  OLD-TDAI-DS-PEN-AMT       PIC S9(12)V99              \n017352                          OCCURS 20 TIMES.                        \n017354         10  OLD-TDAI-DS-WTHLD-AMT     PIC S9(12)V99              \n017356                          OCCURS 20 TIMES.                        \n017358         10  OLD-TDAI-DS-ST-WH-AMT     PIC S9(12)V99              \n017360                          OCCURS 20 TIMES.                        \n017362         10  OLD-TDAI-DS-EXC-EARN      PIC S9(12)V9(2)            \n017364                          OCCURS 20 TIMES.                        \n017366         10  OLD-TDAI-DS-C-YTD-CNT     PIC 9(5).                  \n017368         10  OLD-TDAI-DS-P-YTD-CNT     PIC 9(5).                  \n017370         10  OLD-TDAI-DS-AMT-C-YTD     PIC S9(12)V9(2).           \n017372         10  OLD-TDAI-DS-AMT-P-YTD     PIC S9(12)V9(2).           \n017374         10  OLD-TDAI-DS-INT-AMT       PIC S9(12)V9(2).           \n017376         10  OLD-TDAI-CN-YTD-CNT       PIC 9(5).                  \n017378         10  OLD-TDAI-CN-YTD-AMT       PIC S9(12)V9(2).           \n017380         10  OLD-TDAI-CN-LYTD-AMT      PIC S9(12)V9(2).           \n017382         10  OLD-TDAI-EMP-CONT-LYR     PIC S9(12)V9(2).           \n017384         10  OLD-TDAI-REG-CONT-LYR     PIC S9(12)V9(2).           \n017386         10  OLD-TDAI-UNINSURED        PIC X(1).                  \n017388         10  OLD-TDAI-ROLLOVER         PIC S9(12)V9(2).           \n017390         10  OLD-TDAI-ROLLOVER-LYR     PIC S9(12)V9(2).           \n017392         10  OLD-TDAI-TRANSFER-IN      PIC S9(12)V9(2).           \n017394         10  OLD-TDAI-TRANSFER-OUT     PIC S9(12)V9(2).           \n017396         10  OLD-TDAI-1ST-CN-DATE      PIC 9(8).                  \n017398         10  OLD-TDAI-BASIS-C-LTD      PIC S9(12)V99.             \n017400         10  OLD-TDAI-BASIS-D-LTD      PIC S9(12)V99.             \n017402         10  OLD-TDAI-BASIS-D-YTD      PIC S9(12)V99.             \n017404         10  OLD-TDAI-EXTRA-FIELDS.                               \n017406             15  OLD-TDAI-CN-TYPE-EX   PIC 9(2).                  \n017408             15  OLD-TDAI-DS-TYPE-EX.                             \n017410               20  OLD-TDAI-DS-TYPE-EX-1       PIC X.             \n017412               20  OLD-TDAI-DS-TYPE-EX-2       PIC X.             \n017414                                                                  \n017416      05 OLD-TDADISTR-DATA                     PIC X(500).        \n017418      05 OLD-TDADISTR.                                            \n017420         10 OLD-TDAD-BANK                      PIC 9(04).         \n017422         10 OLD-TDAD-BRCH                      PIC 9(04).         \n017424         10 OLD-TDAD-APPL                      PIC 9(01).         \n017426         10 OLD-TDAD-CUST                      PIC 9(12).         \n017428         10 OLD-TDAD-ACCT                      PIC 9(10).         \n017430         10 OLD-TDAD-NXT-ACCT-P                PIC 9(10).         \n017432         10 OLD-TDAD-NXT-ACCT-S                PIC 9(10).         \n017434         10 OLD-TDAD-N-ACCT-BY-RT              PIC 9(1).          \n017436         10 OLD-TDAD-SERIAL                    PIC 9(12).         \n017438         10 OLD-TDAD-SER-NEXT                  PIC 9(12).         \n017440         10 OLD-TDAD-DISP-CD                   PIC 9(01).         \n017442         10 OLD-TDAD-TYPE                      PIC X(02).         \n017444         10 OLD-TDAD-PRINCIPAL                 PIC 9(01).         \n017446         10 OLD-TDAD-INTEREST                  PIC 9(01).         \n017448         10 OLD-TDAD-DS-CODE                   PIC 9(01).         \n017450         10 OLD-TDAD-WTHLD-CD                  PIC 9(01).         \n017452         10 OLD-TDAD-WHLD-AMT                  PIC S9(12)V99.     \n017454         10 OLD-TDAD-ST-WHLD-CD                PIC 9(01).         \n017456         10 OLD-TDAD-ST-WHLD-AMT               PIC S9(12)V99.     \n017458         10 OLD-TDAD-TRF-ACCT                  PIC 9(12).         \n017460         10 OLD-TDAD-TRF-ACCT-S                PIC 9(10).         \n017462         10 OLD-TDAD-AMT-CD                    PIC 9(01).         \n017464         10 OLD-TDAD-DS-AMT                    PIC S9(12)V99.     \n017466         10 OLD-TDAD-DS-FREQ                   PIC 9(01).         \n017468         10 OLD-TDAD-DS-NTRVL                  PIC 9(04).         \n017470         10 OLD-TDAD-END-OF-DIST               PIC 9(1).          \n017472         10 OLD-TDAD-DIST-NTC-CD               PIC 9(01).         \n017474         10 OLD-TDAD-EOY-DS-FORM               PIC 9(01).         \n017476         10 OLD-TDAD-5-YR-RULE                 PIC 9(01).         \n017478         10 OLD-TDAD-ANUAL-RECALC              PIC 9(01).         \n017480         10 OLD-TDAD-JOINT-CD                  PIC 9(01).         \n017482         10 OLD-TDAD-PUB-ID                    PIC X(08).         \n017484         10 OLD-TDAD-LST-DIST-DT               PIC 9(08).         \n017486         10 OLD-TDAD-IN-PROC-DT                PIC 9(8).          \n017488         10 OLD-TDAD-NXT-DIST-DT               PIC 9(8).          \n017490         10 OLD-TDAD-NXT-DS-PROC               PIC 9(8).          \n017492         10 OLD-TDAD-ADD-DT                    PIC 9(08).         \n017494         10 OLD-TDAD-ADD-TM                    PIC 9(08).         \n017496                                                                  \n017498         10 OLD-TDAD-MIN-AMT                   PIC S9(12)V99.     \n017500         10 OLD-TDAD-AMT                       PIC S9(12)V99.     \n017502         10 OLD-TDAD-LST-AMT                   PIC S9(12)V99.     \n017504         10 OLD-TDAD-CUR-WHLD-AMT              PIC S9(12)V99.     \n017506         10 OLD-TDAD-WHLD-YTD                  PIC S9(12)V99.     \n017508         10 OLD-TDAD-LST-WHLD-AMT              PIC S9(12)V99.     \n017510         10 OLD-TDAD-PRINCPL-AMT               PIC S9(12)V99.     \n017512         10 OLD-TDAD-INT-AMT                   PIC S9(12)V99.     \n017514         10 OLD-TDAD-INT-YTD                   PIC S9(12)V99.     \n017516         10 OLD-TDAD-ST-CUR-W-AMT              PIC S9(12)V99.     \n017518         10 OLD-TDAD-ST-LST-W-AMT              PIC S9(12)V99.     \n017520         10 OLD-TDAD-CK-IND-1                  PIC X(01).         \n017522         10 OLD-TDAD-CK-IND-2                  PIC X(01).         \n017524         10 OLD-TDAD-LUPD-DT                   PIC 9(08).         \n017526         10 OLD-TDAD-LUPD-TM                   PIC 9(06).         \n017528         10 OLD-TDAD-RMD-OVERRIDE              PIC 9.             \n017530         10 OLD-TDAD-RMD-AMOUNT                PIC S9(12)V9(2).   \n017532         10 OLD-TDAD-DS-NBR                    PIC 9(2).          \n017534                                                                  \n017536     05  OLD-TDAHMS.                                              \n017538         10  OLD-TDAHMS-BANK              PIC  9(4).              \n017540         10  OLD-TDAHMS-APPL              PIC  9(1).              \n017542         10  OLD-TDAHMS-CUST              PIC  9(12).             \n017544         10  OLD-TDAHMS-ACCT              PIC  9(10).             \n017546         10  OLD-TDAHMS-TYPE              PIC  X(1).              \n017548         10  OLD-TDAHMS-BK-TYPE           PIC  X(1).              \n017550         10  OLD-TDAHMS-DR-CR-IND         PIC  X(1).              \n017552         10  OLD-TDAHMS-SOURCE            PIC  9(2).              \n017554         10  OLD-TDAHMS-HOLD-NBR          PIC  9(4).              \n017556         10  OLD-TDAHMS-AMT               PIC S9(12)V99.          \n017558         10  OLD-TDAHMS-ORIG-AMT          PIC  9(12)V99.          \n017560         10  OLD-TDAHMS-COMMENT           PIC  X(40).             \n017562         10  OLD-TDAHMS-PUB-ID            PIC  X(8).              \n017564         10  OLD-TDAHMS-VD-PUB-ID         PIC  X(8).              \n017566         10  OLD-TDAHMS-ADD-DATE          PIC  9(8).              \n017568         10  OLD-TDAHMS-ADD-TIME          PIC  9(8).              \n017570         10  OLD-TDAHMS-VOID-DATE         PIC  9(8).              \n017572         10  OLD-TDAHMS-PLG-ACCT          PIC  9(12).             \n017574         10  OLD-TDAHMS-PLG-ACCT-S        PIC  9(10).             \n017576         10  OLD-TDAHMS-EXPIRE-DT         PIC  9(8).              \n017578         10  OLD-TDAHMS-AVAIL-BAL         PIC S9(12)V99.          \n017580         10  OLD-TDAHMS-SERIAL-NUM        PIC  9(10).             \n017582         10  OLD-TDAHMS-END-SERIAL        PIC  9(10).             \n017584         10  OLD-TDAHMS-NAME              PIC  X(10).             \n017586         10  OLD-TDAHMS-START-DATE        PIC  9(8).              \n017588         10  OLD-TDAHMS-DAILY-ACCR        PIC S9(12)V9(6).        \n017590         10  OLD-TDAHMS-ORG-ADD-DT        PIC  9(8).              \n017592         10  OLD-TDAHMS-ORG-ADD-TM        PIC  9(8).              \n017594         10  OLD-TDAHMS-ORG-PUB-ID        PIC  X(8).              \n017596         10  OLD-TDAHMS-AMT-LAST-UPD      PIC S9(12)V9(2).        \n017598         10  OLD-TDAHMS-DATE-LAST-UPD     PIC  9(8).              \n017600                                                                  \n017602     05  OLD-TDAPCR.                                              \n017604         10  OLD-TDAPC-APPL                    PIC X(03).         \n017606         10  OLD-TDAPC-TYPE                    PIC 9(1).          \n017608         10  OLD-TDAPC-BANK                    PIC 9(04).         \n017610         10  OLD-TDAPC-RPT-NBR                 PIC 9(04).         \n017612         10  OLD-TDAPC-CSI-ONLY                PIC X(01).         \n017614         10  OLD-TDAPC-RPT-DESC                PIC X(40).         \n017616         10  OLD-TDAPC-SPECS                   PIC X(65).         \n017618         10  OLD-TDAPC-COPIES                  PIC 9(02).         \n017620         10  OLD-TDAPC-LASER-PRT               PIC 9(02).         \n017622         10  OLD-TDAPC-FICHE-PRT               PIC 9(02).         \n017624         10  OLD-TDAPC-OPTICAL                 PIC 9(02).         \n017626         10  OLD-TDAPC-PRT-DLY                 PIC X(01).         \n017628         10  OLD-TDAPC-DLY-IND                 PIC X(07).         \n017630         10  OLD-TDAPC-LST-PRT-D               PIC 9(08).         \n017632         10  OLD-TDAPC-PRT-WK                  PIC X(01).         \n017634         10  OLD-TDAPC-WK-IND                  PIC X(07).         \n017636         10  OLD-TDAPC-LST-PRT-W               PIC 9(08).         \n017638         10  OLD-TDAPC-PRT-MTH                 PIC X(01).         \n017640         10  OLD-TDAPC-LST-DAY-M               PIC X(01).         \n017642         10  OLD-TDAPC-NXT-PRT-M               PIC 9(08).         \n017644         10  OLD-TDAPC-LST-PRT-M               PIC 9(08).         \n017646         10  OLD-TDAPC-PRT-QTR                 PIC X(01).         \n017648         10  OLD-TDAPC-LST-DAY-Q               PIC X(01).         \n017650         10  OLD-TDAPC-NXT-PRT-Q               PIC 9(08).         \n017652         10  OLD-TDAPC-LST-PRT-Q               PIC 9(08).         \n017654         10  OLD-TDAPC-PRT-YR                  PIC X(01).         \n017656         10  OLD-TDAPC-NXT-PRT-Y               PIC 9(08).         \n017658         10  OLD-TDAPC-LST-PRT-Y               PIC 9(08).         \n017660         10  OLD-TDAPC-SPECL-REQ               PIC X(01).         \n017662         10  OLD-TDAPC-PRT-DAY                 PIC 9(08).         \n017664         10  OLD-TDAPC-BEGIN-DATE              PIC 9(06).         \n017666         10  OLD-TDAPC-END-DATE                PIC 9(06).         \n017668         10  OLD-TDAPC-PRINTER                 PIC X(17).         \n017670         10  OLD-TDAPC-SPECL-SPECS             PIC X(65).         \n017672         10  OLD-TDAPC-REQUESTOR               PIC X(08).         \n017674         10  OLD-TDAPC-LPROCESS-DT             PIC 9(16).         \n017676         10  OLD-TDAPC-LUPD-DT                 PIC 9(08).         \n017678         10  OLD-TDAPC-LUPD-TM                 PIC 9(06).         \n017680         10  OLD-TDAPC-BP-LAST-RUN             PIC 9(16).         \n017682         10  OLD-TDAPC-PUB-ID                  PIC X(08).         \n017684         10  OLD-TDAPC-BANK-SPECS              PIC X(300).        \n017686         10  OLD-TDAPC-BANK-SPECS-R REDEFINES                     \n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 188 lines from 8652 to 8839.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 18,
  "total_chunks": 55,
  "start_line": 8652,
  "end_line": 8839,
  "line_count": 188
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
- Source code length: 20619 characters

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
CHUNK 18 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 8652 to 8839 (188 lines)
Chunk Tokens (estimated): ~4,154
Actual Input Tokens: 5,560 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 8652-8839 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 18 of 55 chunks
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
      The source code below is only CHUNK 18 of 55.


=============================================================================
CHUNK 18 SOURCE CODE (Lines 8652-8839)
=============================================================================

```cobol
017312                         OLD-TDAA-MANUAL-RT-X.                    
017314                 20  OLD-TDAA-MANUAL-RT  PIC 9(2)V9(3).           
017316                                                                  
017318     05  OLD-TDAIRA-DATA               PIC X(1400).               
017320     05  OLD-TDAIRA.                                              
017322         10  OLD-TDAI-BANK             PIC 9(4).                  
017324         10  OLD-TDAI-BRCH             PIC 9(4).                  
017326         10  OLD-TDAI-APPL             PIC 9(1).                  
017328         10  OLD-TDAI-CUST             PIC 9(12).                 
017330         10  OLD-TDAI-ACCT             PIC 9(10).                 
017332         10  OLD-TDAI-PUB-ID           PIC X(8).                  
017334         10  OLD-TDAI-ADD-DT           PIC 9(8).                  
017336         10  OLD-TDAI-ADD-TM           PIC 9(6).                  
017338         10  OLD-TDAI-DS-TYPE          PIC X(2)                   
017340                          OCCURS 20 TIMES.                        
017342         10  OLD-TDAI-CN-TYPE          PIC 9(2)                   
017344                          OCCURS 20 TIMES.                        
017346         10  OLD-TDAI-DS-CN-AMT        PIC S9(12)V99              
017348                          OCCURS 20 TIMES.                        
017350         10  OLD-TDAI-DS-PEN-AMT       PIC S9(12)V99              
017352                          OCCURS 20 TIMES.                        
017354         10  OLD-TDAI-DS-WTHLD-AMT     PIC S9(12)V99              
017356                          OCCURS 20 TIMES.                        
017358         10  OLD-TDAI-DS-ST-WH-AMT     PIC S9(12)V99              
017360                          OCCURS 20 TIMES.                        
017362         10  OLD-TDAI-DS-EXC-EARN      PIC S9(12)V9(2)            
017364                          OCCURS 20 TIMES.                        
017366         10  OLD-TDAI-DS-C-YTD-CNT     PIC 9(5).                  
017368         10  OLD-TDAI-DS-P-YTD-CNT     PIC 9(5).                  
017370         10  OLD-TDAI-DS-AMT-C-YTD     PIC S9(12)V9(2).           
017372         10  OLD-TDAI-DS-AMT-P-YTD     PIC S9(12)V9(2).           
017374         10  OLD-TDAI-DS-INT-AMT       PIC S9(12)V9(2).           
017376         10  OLD-TDAI-CN-YTD-CNT       PIC 9(5).                  
017378         10  OLD-TDAI-CN-YTD-AMT       PIC S9(12)V9(2).           
017380         10  OLD-TDAI-CN-LYTD-AMT      PIC S9(12)V9(2).           
017382         10  OLD-TDAI-EMP-CONT-LYR     PIC S9(12)V9(2).           
017384         10  OLD-TDAI-REG-CONT-LYR     PIC S9(12)V9(2).           
017386         10  OLD-TDAI-UNINSURED        PIC X(1).                  
017388         10  OLD-TDAI-ROLLOVER         PIC S9(12)V9(2).           
017390         10  OLD-TDAI-ROLLOVER-LYR     PIC S9(12)V9(2).           
017392         10  OLD-TDAI-TRANSFER-IN      PIC S9(12)V9(2).           
017394         10  OLD-TDAI-TRANSFER-OUT     PIC S9(12)V9(2).           
017396         10  OLD-TDAI-1ST-CN-DATE      PIC 9(8).                  
017398         10  OLD-TDAI-BASIS-C-LTD      PIC S9(12)V99.             
017400         10  OLD-TDAI-BASIS-D-LTD      PIC S9(12)V99.             
017402         10  OLD-TDAI-BASIS-D-YTD      PIC S9(12)V99.             
017404         10  OLD-TDAI-EXTRA-FIELDS.                               
017406             15  OLD-TDAI-CN-TYPE-EX   PIC 9(2).                  
017408             15  OLD-TDAI-DS-TYPE-EX.                             
017410               20  OLD-TDAI-DS-TYPE-EX-1       PIC X.             
017412               20  OLD-TDAI-DS-TYPE-EX-2       PIC X.             
017414                                                                  
017416      05 OLD-TDADISTR-DATA                     PIC X(500).        
017418      05 OLD-TDADISTR.                                            
017420         10 OLD-TDAD-BANK                      PIC 9(04).         
017422         10 OLD-TDAD-BRCH                      PIC 9(04).         
017424         10 OLD-TDAD-APPL                      PIC 9(01).         
017426         10 OLD-TDAD-CUST                      PIC 9(12).         
017428         10 OLD-TDAD-ACCT                      PIC 9(10).         
017430         10 OLD-TDAD-NXT-ACCT-P                PIC 9(10).         
017432         10 OLD-TDAD-NXT-ACCT-S                PIC 9(10).         
017434         10 OLD-TDAD-N-ACCT-BY-RT              PIC 9(1).          
017436         10 OLD-TDAD-SERIAL                    PIC 9(12).         
017438         10 OLD-TDAD-SER-NEXT                  PIC 9(12).         
017440         10 OLD-TDAD-DISP-CD                   PIC 9(01).         
017442         10 OLD-TDAD-TYPE                      PIC X(02).         
017444         10 OLD-TDAD-PRINCIPAL                 PIC 9(01).         
017446         10 OLD-TDAD-INTEREST                  PIC 9(01).         
017448         10 OLD-TDAD-DS-CODE                   PIC 9(01).         
017450         10 OLD-TDAD-WTHLD-CD                  PIC 9(01).         
017452         10 OLD-TDAD-WHLD-AMT                  PIC S9(12)V99.     
017454         10 OLD-TDAD-ST-WHLD-CD                PIC 9(01).         
017456         10 OLD-TDAD-ST-WHLD-AMT               PIC S9(12)V99.     
017458         10 OLD-TDAD-TRF-ACCT                  PIC 9(12).         
017460         10 OLD-TDAD-TRF-ACCT-S                PIC 9(10).         
017462         10 OLD-TDAD-AMT-CD                    PIC 9(01).         
017464         10 OLD-TDAD-DS-AMT                    PIC S9(12)V99.     
017466         10 OLD-TDAD-DS-FREQ                   PIC 9(01).         
017468         10 OLD-TDAD-DS-NTRVL                  PIC 9(04).         
017470         10 OLD-TDAD-END-OF-DIST               PIC 9(1).          
017472         10 OLD-TDAD-DIST-NTC-CD               PIC 9(01).         
017474         10 OLD-TDAD-EOY-DS-FORM               PIC 9(01).         
017476         10 OLD-TDAD-5-YR-RULE                 PIC 9(01).         
017478         10 OLD-TDAD-ANUAL-RECALC              PIC 9(01).         
017480         10 OLD-TDAD-JOINT-CD                  PIC 9(01).         
017482         10 OLD-TDAD-PUB-ID                    PIC X(08).         
017484         10 OLD-TDAD-LST-DIST-DT               PIC 9(08).         
017486         10 OLD-TDAD-IN-PROC-DT                PIC 9(8).          
017488         10 OLD-TDAD-NXT-DIST-DT               PIC 9(8).          
017490         10 OLD-TDAD-NXT-DS-PROC               PIC 9(8).          
017492         10 OLD-TDAD-ADD-DT                    PIC 9(08).         
017494         10 OLD-TDAD-ADD-TM                    PIC 9(08).         
017496                                                                  
017498         10 OLD-TDAD-MIN-AMT                   PIC S9(12)V99.     
017500         10 OLD-TDAD-AMT                       PIC S9(12)V99.     
017502         10 OLD-TDAD-LST-AMT                   PIC S9(12)V99.     
017504         10 OLD-TDAD-CUR-WHLD-AMT              PIC S9(12)V99.     
017506         10 OLD-TDAD-WHLD-YTD                  PIC S9(12)V99.     
017508         10 OLD-TDAD-LST-WHLD-AMT              PIC S9(12)V99.     
017510         10 OLD-TDAD-PRINCPL-AMT               PIC S9(12)V99.     
017512         10 OLD-TDAD-INT-AMT                   PIC S9(12)V99.     
017514         10 OLD-TDAD-INT-YTD                   PIC S9(12)V99.     
017516         10 OLD-TDAD-ST-CUR-W-AMT              PIC S9(12)V99.     
017518         10 OLD-TDAD-ST-LST-W-AMT              PIC S9(12)V99.     
017520         10 OLD-TDAD-CK-IND-1                  PIC X(01).         
017522         10 OLD-TDAD-CK-IND-2                  PIC X(01).         
017524         10 OLD-TDAD-LUPD-DT                   PIC 9(08).         
017526         10 OLD-TDAD-LUPD-TM                   PIC 9(06).         
017528         10 OLD-TDAD-RMD-OVERRIDE              PIC 9.             
017530         10 OLD-TDAD-RMD-AMOUNT                PIC S9(12)V9(2).   
017532         10 OLD-TDAD-DS-NBR                    PIC 9(2).          
017534                                                                  
017536     05  OLD-TDAHMS.                                              
017538         10  OLD-TDAHMS-BANK              PIC  9(4).              
017540         10  OLD-TDAHMS-APPL              PIC  9(1).              
017542         10  OLD-TDAHMS-CUST              PIC  9(12).             
017544         10  OLD-TDAHMS-ACCT              PIC  9(10).             
017546         10  OLD-TDAHMS-TYPE              PIC  X(1).              
017548         10  OLD-TDAHMS-BK-TYPE           PIC  X(1).              
017550         10  OLD-TDAHMS-DR-CR-IND         PIC  X(1).              
017552         10  OLD-TDAHMS-SOURCE            PIC  9(2).              
017554         10  OLD-TDAHMS-HOLD-NBR          PIC  9(4).              
017556         10  OLD-TDAHMS-AMT               PIC S9(12)V99.          
017558         10  OLD-TDAHMS-ORIG-AMT          PIC  9(12)V99.          
017560         10  OLD-TDAHMS-COMMENT           PIC  X(40).             
017562         10  OLD-TDAHMS-PUB-ID            PIC  X(8).              
017564         10  OLD-TDAHMS-VD-PUB-ID         PIC  X(8).              
017566         10  OLD-TDAHMS-ADD-DATE          PIC  9(8).              
017568         10  OLD-TDAHMS-ADD-TIME          PIC  9(8).              
017570         10  OLD-TDAHMS-VOID-DATE         PIC  9(8).              
017572         10  OLD-TDAHMS-PLG-ACCT          PIC  9(12).             
017574         10  OLD-TDAHMS-PLG-ACCT-S        PIC  9(10).             
017576         10  OLD-TDAHMS-EXPIRE-DT         PIC  9(8).              
017578         10  OLD-TDAHMS-AVAIL-BAL         PIC S9(12)V99.          
017580         10  OLD-TDAHMS-SERIAL-NUM        PIC  9(10).             
017582         10  OLD-TDAHMS-END-SERIAL        PIC  9(10).             
017584         10  OLD-TDAHMS-NAME              PIC  X(10).             
017586         10  OLD-TDAHMS-START-DATE        PIC  9(8).              
017588         10  OLD-TDAHMS-DAILY-ACCR        PIC S9(12)V9(6).        
017590         10  OLD-TDAHMS-ORG-ADD-DT        PIC  9(8).              
017592         10  OLD-TDAHMS-ORG-ADD-TM        PIC  9(8).              
017594         10  OLD-TDAHMS-ORG-PUB-ID        PIC  X(8).              
017596         10  OLD-TDAHMS-AMT-LAST-UPD      PIC S9(12)V9(2).        
017598         10  OLD-TDAHMS-DATE-LAST-UPD     PIC  9(8).              
017600                                                                  
017602     05  OLD-TDAPCR.                                              
017604         10  OLD-TDAPC-APPL                    PIC X(03).         
017606         10  OLD-TDAPC-TYPE                    PIC 9(1).          
017608         10  OLD-TDAPC-BANK                    PIC 9(04).         
017610         10  OLD-TDAPC-RPT-NBR                 PIC 9(04).         
017612         10  OLD-TDAPC-CSI-ONLY                PIC X(01).         
017614         10  OLD-TDAPC-RPT-DESC                PIC X(40).         
017616         10  OLD-TDAPC-SPECS                   PIC X(65).         
017618         10  OLD-TDAPC-COPIES                  PIC 9(02).         
017620         10  OLD-TDAPC-LASER-PRT               PIC 9(02).         
017622         10  OLD-TDAPC-FICHE-PRT               PIC 9(02).         
017624         10  OLD-TDAPC-OPTICAL                 PIC 9(02).         
017626         10  OLD-TDAPC-PRT-DLY                 PIC X(01).         
017628         10  OLD-TDAPC-DLY-IND                 PIC X(07).         
017630         10  OLD-TDAPC-LST-PRT-D               PIC 9(08).         
017632         10  OLD-TDAPC-PRT-WK                  PIC X(01).         
017634         10  OLD-TDAPC-WK-IND                  PIC X(07).         
017636         10  OLD-TDAPC-LST-PRT-W               PIC 9(08).         
017638         10  OLD-TDAPC-PRT-MTH                 PIC X(01).         
017640         10  OLD-TDAPC-LST-DAY-M               PIC X(01).         
017642         10  OLD-TDAPC-NXT-PRT-M               PIC 9(08).         
017644         10  OLD-TDAPC-LST-PRT-M               PIC 9(08).         
017646         10  OLD-TDAPC-PRT-QTR                 PIC X(01).         
017648         10  OLD-TDAPC-LST-DAY-Q               PIC X(01).         
017650         10  OLD-TDAPC-NXT-PRT-Q               PIC 9(08).         
017652         10  OLD-TDAPC-LST-PRT-Q               PIC 9(08).         
017654         10  OLD-TDAPC-PRT-YR                  PIC X(01).         
017656         10  OLD-TDAPC-NXT-PRT-Y               PIC 9(08).         
017658         10  OLD-TDAPC-LST-PRT-Y               PIC 9(08).         
017660         10  OLD-TDAPC-SPECL-REQ               PIC X(01).         
017662         10  OLD-TDAPC-PRT-DAY                 PIC 9(08).         
017664         10  OLD-TDAPC-BEGIN-DATE              PIC 9(06).         
017666         10  OLD-TDAPC-END-DATE                PIC 9(06).         
017668         10  OLD-TDAPC-PRINTER                 PIC X(17).         
017670         10  OLD-TDAPC-SPECL-SPECS             PIC X(65).         
017672         10  OLD-TDAPC-REQUESTOR               PIC X(08).         
017674         10  OLD-TDAPC-LPROCESS-DT             PIC 9(16).         
017676         10  OLD-TDAPC-LUPD-DT                 PIC 9(08).         
017678         10  OLD-TDAPC-LUPD-TM                 PIC 9(06).         
017680         10  OLD-TDAPC-BP-LAST-RUN             PIC 9(16).         
017682         10  OLD-TDAPC-PUB-ID                  PIC X(08).         
017684         10  OLD-TDAPC-BANK-SPECS              PIC X(300).        
017686         10  OLD-TDAPC-BANK-SPECS-R REDEFINES                     
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 188 lines from 8652 to 8839.

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

