# LLM Request Debug File
Generated: 2025-11-13T20:48:26.031067

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 24/55
- **Model**: gpt-4.1
- **Chunk Number**: 24
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~10,545 tokens
- **Total Input**: ~12,503 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 24/55" (ID: detailed-code-explanation)

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


**CHUNK 24 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 24 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 11087 to 11442 (356 lines)\nChunk Tokens (estimated): ~7,501\nActual Input Tokens: 8,907 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 11087-11442 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 24 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 24 of 55.\n\n\n=============================================================================\nCHUNK 24 SOURCE CODE (Lines 11087-11442)\n=============================================================================\n\n```cobol\n022182             TDB-TDAPC-BANK-SPECS.                                \n022184             15  TDB-TDAPC-CREATE-DT      PIC 9(07).              \n022186             15  TDB-TDAPC-CREATE-TM      PIC 9(12).              \n022188             15  TDB-TDAPC-DQVISTA        PIC X.                  \n022190             15  TDB-TDAPC-MSI            PIC X.                  \n022192             15  TDB-TDAPC-BK-TDA-STAT    PIC X.                  \n022194             15  TDB-TDAPC-TDA-PILOT REDEFINES                    \n022196                 TDB-TDAPC-BK-TDA-STAT    PIC X.                  \n022198             15  TDB-TDAPC-BK-STATUS      PIC X.                  \n022200             15  TDB-TDAPC-BR-NO          PIC XX.                 \n022202             15  TDB-TDAPC-CSI-BR-CODE REDEFINES                  \n022204                 TDB-TDAPC-BR-NO          PIC XX.                 \n022206             15  TDB-TDAPC-BK-PHONE-NUM.                          \n022208                 20  TDB-TDAPC-AREA-CODE  PIC XXX.                \n022210                 20  TDB-TDAPC-PHONE.                             \n022212                     25  TDB-TDAPC-PHONE-1ST-3 PIC XXX.           \n022214                     25  TDB-TDAPC-PHONE-LST-4 PIC X(04).         \n022216             15  TDB-TDAPC-PHN-NUMBER REDEFINES                   \n022218                 TDB-TDAPC-BK-PHONE-NUM   PIC X(10).              \n022220             15  TDB-TDAPC-TDA-ADD-DAY    PIC XXX.                \n022222             15  TDB-TDAPC-HOLIDAYS       OCCURS 18 TIMES.        \n022224                 20  TDB-TDAPC-HOL-MM     PIC XX.                 \n022226                 20  TDB-TDAPC-HOL-DD     PIC XX.                 \n022228             15  TDB-TDAPC-FM-SUPPRESS    PIC X.                  \n022230             15  TDB-TDAPC-RMT-BK-INDICATOR PIC XX.               \n022232             15  TDB-TDAPC-RMT-IND REDEFINES                      \n022234                 TDB-TDAPC-RMT-BK-INDICATOR PIC XX.               \n022236             15  TDB-TDAPC-BK-ADDR        PIC X(28).              \n022238             15  TDB-TDAPC-BK-ADDR-2      PIC X(27).              \n022240             15  TDB-TDAPC-FED-ID         PIC X(10).              \n022242             15  TDB-TDAPC-EOY-RPT-SEQ    PIC X.                  \n022244             15  TDB-TDAPC-EOY-EARLY-RUN  PIC X.                  \n022246             15  TDB-TDAPC-EOY-RETURN-TO-BK PIC X.                \n022248             15  TDB-TDAPC-EOY-RETURN-TO-BANK REDEFINES           \n022250                 TDB-TDAPC-EOY-RETURN-TO-BK PIC X.                \n022252             15  TDB-TDAPC-EOY-IRA-PHONE    PIC 9(10).            \n022254             15  TDB-TDAPC-EOY-DELETE-DATE  PIC 9(06).            \n022256             15  TDB-TDAPC-EOY-IRA-FICHE  PIC X.                  \n022258             15  TDB-TDAPC-EOY-IRA-PAPER  PIC X.                  \n022260             15  TDB-TDAPC-EOY-IRA-STMT-EARLY PIC X.              \n022262             15  TDB-TDAPC-NO-IRA-STMTS   PIC 9.                  \n022264             15  TDB-TDAPC-EOY-IRA-STMT   PIC X.                  \n022266             15  TDB-TDAPC-EOY-IRA-STMT-PRINT PIC X.              \n022268             15  TDB-TDAPC-EOY-EARLY-DATE PIC 9(06).              \n022270             15  TDB-TDAPC-CK21-TDA       PIC X.                  \n022272             15  TDB-TDAPC-MSI-OV-TDA     PIC 9.                  \n022274             15  TDB-TDAPC-BK-IMG-SERV    PIC X(01).              \n022276             15  TDB-TDAPC-EOY-APRIL-DATE PIC 9(06).              \n022278             15  TDB-TDAPC-EOY-COD-CLOSED-RPT PIC X(01).          \n022280             15  TDB-TDAPC-PRT-NEW        PIC 9(01).              \n022282             15  TDB-TDAPC-IMONITOR       PIC 9(01).              \n022284             15  TDB-TDAPC-ENTC-TDA       PIC X.                  \n022286             15  TDB-TDAPC-EV-3RD-PARTY-1 PIC X.                  \n022288             15  TDB-TDAPC-EV-3RD-PARTY-2 PIC X.                  \n022290             15  TDB-TDAPC-HSA-LOCATION   PIC X.                  \n022292             15  TDB-TDAPC-PROFITABILITY  PIC X.                  \n022294             15  TDB-TDAPC-BANCVUE        PIC X.                  \n022296             15  TDB-TDAPC-SPECIAL-DL-BILLING PIC X.              \n022298             15  TDB-TDAPC-CIF-NAME-ADDR      PIC 9.              \n022300             15  TDB-TDAPC-MAIL-ADDR-LINES    PIC X.              \n022302             15  TDB-TDAPC-WEB-ENABLED        PIC X(01).          \n022304             15  TDB-TDAPC-BRANCH-LENGTH      PIC 9.              \n022306             15  TDB-TDAPC-LOB                PIC 9.              \n022308             15  TDB-TDAPC-BILL-EDIT-TEMPLATES PIC 9.             \n022310             15  TDB-TDAPC-MCIF-PRIVACY-OPT   PIC 9.              \n022312             15  TDB-TDAPC-TRAIN-BK-FLG       PIC X.              \n022314             15  TDB-TDAPC-EOY-CIB-F-MERD     PIC X.              \n022316             15  FILLER                       PIC X(39).          \n022318             15  TDB-TDAPC-LAST-EOM-PROC      PIC 9(08).          \n022320             15  TDB-TDAPC-BUS-DT-AFT-NX      PIC 9(08).          \n022322             15  TDB-TDAPC-NEXT-BUS-DATE      PIC 9(08).          \n022324                                                                  \n022326     05  TDB-TDACHK.                                              \n022328         10  TDB-TDACK-BANK-X.                                    \n022330             15  TDB-TDACK-BANK           PIC 9(04).              \n022332         10  TDB-TDACK-BRCH-X.                                    \n022334             15  TDB-TDACK-BRCH           PIC 9(04).              \n022336         10  TDB-TDACK-ADDR-CUST-X.                               \n022338             15  TDB-TDACK-ADDR-CUST      PIC 9(12).              \n022340         10  TDB-TDACK-CUST-X OCCURS 10.                          \n022342             15  TDB-TDACK-CUST           PIC 9(12).              \n022344         10  TDB-TDACK-ACCT-X OCCURS 10.                          \n022346             15  TDB-TDACK-ACCT           PIC 9(10).              \n022348         10  TDB-TDACK-LUPD-DATE-X.                               \n022350             15  TDB-TDACK-LUPD-DATE      PIC 9(08).              \n022352         10  TDB-TDACK-LUPD-TIME-X.                               \n022354             15  TDB-TDACK-LUPD-TIME      PIC 9(08).              \n022356         10  TDB-TDACK-PUB-ID             PIC X(08).              \n022358         10  FILLER                       PIC X(12).              \n022360                                                                  \n022362     05  TDB-TDABENEF.                                            \n022364         10  TDB-TDAB-BANK-X.                                     \n022366             15  TDB-TDAB-BANK              PIC 9(04).            \n022368         10  TDB-TDAB-CUST-X.                                     \n022370             15  TDB-TDAB-CUST              PIC 9(12).            \n022372         10  TDB-TDAB-ACCT-X.                                     \n022374             15  TDB-TDAB-ACCT             PIC 9(10).             \n022376         10  TDB-TDAB-BENEF-NBR-X.                                \n022378             15  TDB-TDAB-BENEF-NBR        PIC 9(02).             \n022380         10  TDB-TDAB-NAME                 PIC X(40).             \n022382         10  TDB-TDAB-NAME-2               PIC X(40).             \n022384         10  TDB-TDAB-NAME-3               PIC X(40).             \n022386         10  TDB-TDAB-ADDR-1               PIC X(40).             \n022388         10  TDB-TDAB-ADDR-2               PIC X(40).             \n022390         10  TDB-TDAB-CITY                 PIC X(40).             \n022392         10  TDB-TDAB-STATE                PIC X(02).             \n022394         10  TDB-TDAB-PROVINCE             PIC X(02).             \n022396         10  TDB-TDAB-COUNTRY              PIC X(02).             \n022398         10  TDB-TDAB-ZIP-CODE.                                   \n022400             15  TDB-TDAB-ZIP-X.                                  \n022402                 20  TDB-TDAB-ZIP          PIC 9(05).             \n022404             15  TDB-TDAB-ZIP-4-X.                                \n022406                 20  TDB-TDAB-ZIP-4        PIC 9(04).             \n022408         10  TDB-TDAB-PHONE-X.                                    \n022410             15  TDB-TDAB-PHONE            PIC 9(10).             \n022412         10  TDB-TDAB-TIN-X.                                      \n022414             15  TDB-TDAB-TIN              PIC 9(09).             \n022416         10  TDB-TDAB-BIRTH-DT-X.                                 \n022418             15  TDB-TDAB-BIRTH-DT         PIC 9(08).             \n022420         10  TDB-TDAB-RELATION-X.                                 \n022422             15  TDB-TDAB-RELATION         PIC 9(01).             \n022424         10  TDB-TDAB-DESIGNATION-X.                              \n022426             15  TDB-TDAB-DESIGNATION      PIC 9(01).             \n022428         10  TDB-TDAB-PERCENT-X.                                  \n022430             15  TDB-TDAB-PERCENT          PIC 9(03).             \n022432         10  TDB-TDAB-FREE-REMARK          PIC X(24).             \n022434                                                                  \n022436     05  TDB-TDAADDR.                                             \n022438         07  TDB-TDADR-BANK-X.                                    \n022440             10  TDB-TDADR-BANK                PIC 9(04).         \n022442         07  TDB-TDADR-CUST-X.                                    \n022444             10  TDB-TDADR-CUST                PIC 9(12).         \n022446         07  TDB-TDADR-ACCT-X.                                    \n022448             10  TDB-TDADR-ACCT                PIC 9(10).         \n022450         07  TDB-TDADR-ADDR-USAGE              PIC X(01).         \n022452         07  TDB-TDADR-TEMP-BEG-DT-X.                             \n022454             10  TDB-TDADR-TEMP-BEG-DT         PIC 9(04).         \n022456         07  TDB-TDADR-TEMP-END-DT-X.                             \n022458             10  TDB-TDADR-TEMP-END-DT         PIC 9(04).         \n022460         07  TDB-TDADR-TEMP-EFF-DT-X.                             \n022462             10  TDB-TDADR-TEMP-EFF-DT         PIC 9(08).         \n022464         07  TDB-TDADR-TEMP-EXP-DT-X.                             \n022466             10  TDB-TDADR-TEMP-EXP-DT         PIC 9(08).         \n022468         07  TDB-TDADR-ADDR-GROUP.                                \n022470             10  TDB-TDADR-T-ADDR.                                \n022472                 15  TDB-TDADR-T-ADDR-1        PIC X(40).         \n022474                 15  TDB-TDADR-T-ADDR-2        PIC X(40).         \n022476                 15  TDB-TDADR-T-CITY          PIC X(40).         \n022478                 15  TDB-TDADR-T-STATE         PIC X(02).         \n022480                 15  TDB-TDADR-T-PROVINCE      PIC X(02).         \n022482                 15  TDB-TDADR-T-COUNTRY       PIC X(02).         \n022484                 15  TDB-TDADR-T-ZIP-CODE.                        \n022486                     20  TDB-TDADR-T-ZIP-X.                       \n022488                         25  TDB-TDADR-T-ZIP   PIC 9(05).         \n022490                     20  TDB-TDADR-T-ZIP-4-X.                     \n022492                         25  TDB-TDADR-T-ZIP-4 PIC 9(04).         \n022494                 15  TDB-TDADR-T-ALIEN-CD-X.                      \n022496                     20  TDB-TDADR-T-ALIEN-CD  PIC 9(01).         \n022498                 15  TDB-TDADR-T-BAR-CODE-X.                      \n022500                     20  TDB-TDADR-T-BAR-CODE  PIC 9(03).         \n022502                 15  TDB-TDADR-T-EMAIL-ADDR    PIC X(100).        \n022504                 15  TDB-TDADR-T-EMAIL-ADDR-R                     \n022506                                REDEFINES TDB-TDADR-T-EMAIL-ADDR. \n022508                     20  TDB-TDADR-T-EMAIL-ADDR-1-50   PIC X(50). \n022510                     20  TDB-TDADR-T-EMAIL-ADDR-51-100 PIC X(50). \n022512                 15  TDB-TDADR-T-MAIL-CD-X.                       \n022514                     20  TDB-TDADR-T-MAIL-CD   PIC 9(01).         \n022516                 15  TDB-TDADR-T-ADDR-KEY        PIC X(28).       \n022518             10  TDB-TDADR-A-ADDR.                                \n022520                 15  TDB-TDADR-A-NAME-1          PIC X(40).       \n022522                 15  TDB-TDADR-A-NAME-AREA-1.                     \n022524                     20  TDB-TDADR-A-N1-KEY      PIC X(14).       \n022526                     20  TDB-TDADR-A-N1-FIRST    PIC X(40).       \n022528                     20  TDB-TDADR-A-N1-MID      PIC X(20).       \n022530                     20  TDB-TDADR-A-N1-LAST     PIC X(40).       \n022532                     20  TDB-TDADR-A-N1-PREFIX   PIC X(12).       \n022534                     20  TDB-TDADR-A-N1-SUFFIX   PIC X(12).       \n022536                     20  TDB-TDADR-A-N1-FAMILIAR PIC X(20).       \n022538                     20  TDB-TDADR-A-N1-PRT-PFX  PIC X(01).       \n022540                     20  TDB-TDADR-A-N1-PRT-SFX  PIC X(01).       \n022542                     20  TDB-TDADR-A-N1-DESIGNAT PIC X(20).       \n022544                 15  TDB-TDADR-A-NAME-2          PIC X(40).       \n022546                 15  TDB-TDADR-A-N2-MODIFIED     PIC X(01).       \n022548                 15  TDB-TDADR-A-N2-PRINT-CD     PIC X(01).       \n022550                 15  TDB-TDADR-A-NAME-AREA-2.                     \n022552                     20  TDB-TDADR-A-N2-KEY      PIC X(14).       \n022554                     20  TDB-TDADR-A-N2-FIRST    PIC X(40).       \n022556                     20  TDB-TDADR-A-N2-MID      PIC X(20).       \n022558                     20  TDB-TDADR-A-N2-LAST     PIC X(40).       \n022560                     20  TDB-TDADR-A-N2-PREFIX   PIC X(12).       \n022562                     20  TDB-TDADR-A-N2-SUFFIX   PIC X(12).       \n022564                     20  TDB-TDADR-A-N2-FAMILIAR PIC X(20).       \n022566                     20  TDB-TDADR-A-N2-PRT-PFX  PIC X(01).       \n022568                     20  TDB-TDADR-A-N2-PRT-SFX  PIC X(01).       \n022570                     20  TDB-TDADR-A-N2-DESIGNAT PIC X(20).       \n022572                 15  TDB-TDADR-A-NAME-3          PIC X(40).       \n022574                 15  TDB-TDADR-A-N3-MODIFIED     PIC X(01).       \n022576                 15  TDB-TDADR-A-N3-PRINT-CD     PIC X(01).       \n022578                 15  TDB-TDADR-A-NAME-AREA-3.                     \n022580                     20  TDB-TDADR-A-N3-KEY      PIC X(14).       \n022582                     20  TDB-TDADR-A-N3-FIRST    PIC X(40).       \n022584                     20  TDB-TDADR-A-N3-MID      PIC X(20).       \n022586                     20  TDB-TDADR-A-N3-LAST     PIC X(40).       \n022588                     20  TDB-TDADR-A-N3-PREFIX   PIC X(12).       \n022590                     20  TDB-TDADR-A-N3-SUFFIX   PIC X(12).       \n022592                     20  TDB-TDADR-A-N3-FAMILIAR PIC X(20).       \n022594                     20  TDB-TDADR-A-N3-PRT-PFX  PIC X(01).       \n022596                     20  TDB-TDADR-A-N3-PRT-SFX  PIC X(01).       \n022598                     20  TDB-TDADR-A-N3-DESIGNAT PIC X(20).       \n022600                 15  TDB-TDADR-A-ADDR-KEY        PIC X(28).       \n022602                 15  TDB-TDADR-A-ADDR-1        PIC X(40).         \n022604                 15  TDB-TDADR-A-ADDR-2        PIC X(40).         \n022606                 15  TDB-TDADR-A-CITY          PIC X(40).         \n022608                 15  TDB-TDADR-A-STATE         PIC X(02).         \n022610                 15  TDB-TDADR-A-PROVINCE      PIC X(02).         \n022612                 15  TDB-TDADR-A-COUNTRY       PIC X(02).         \n022614                 15  TDB-TDADR-A-ZIP-CODE.                        \n022616                     20  TDB-TDADR-A-ZIP-X.                       \n022618                         25  TDB-TDADR-A-ZIP   PIC 9(05).         \n022620                     20  TDB-TDADR-A-ZIP-4-X.                     \n022622                         25  TDB-TDADR-A-ZIP-4 PIC 9(04).         \n022624                 15  TDB-TDADR-A-ALIEN-CD-X.                      \n022626                     20  TDB-TDADR-A-ALIEN-CD  PIC 9(01).         \n022628                 15  TDB-TDADR-A-BAR-CODE-X.                      \n022630                     20  TDB-TDADR-A-BAR-CODE  PIC 9(03).         \n022632                 15  TDB-TDADR-A-EMAIL-ADDR    PIC X(100).        \n022634                 15  TDB-TDADR-A-EMAIL-ADDR-R                     \n022636                                REDEFINES TDB-TDADR-A-EMAIL-ADDR. \n022638                     20  TDB-TDADR-A-EMAIL-ADDR-1-50   PIC X(50). \n022640                     20  TDB-TDADR-A-EMAIL-ADDR-51-100 PIC X(50). \n022642                 15  TDB-TDADR-A-MAIL-CD-X.                       \n022644                     20  TDB-TDADR-A-MAIL-CD   PIC 9(01).         \n022646         07  TDB-TDADR-SHT-NAME                PIC X(20).         \n022648         07  TDB-TDADR-LUPD-DATE               PIC 9(08).         \n022650         07  TDB-TDADR-LUPD-TIME               PIC 9(08).         \n022652         07  TDB-TDADR-PUB-ID                  PIC X(08).         \n022654         07  TDB-TDADR-TIN-CD                  PIC X.             \n022656         07  TDB-TDADR-TIN-NBR-X.                                 \n022658             10  TDB-TDADR-TIN-NBR             PIC 9(9).          \n022660         07  TDB-TDADR-TIN-CERT-CD-X.                             \n022662             10  TDB-TDADR-TIN-CERT-CD         PIC 9.             \n022664         07  TDB-TDADR-TIN-CD-2-X.                                \n022666             10  TDB-TDADR-TIN-CD-2            PIC X(01).         \n022668         07  TDB-TDADR-TIN-NBR-2-X.                               \n022670             10  TDB-TDADR-TIN-NBR-2           PIC 9(09).         \n022672         07  TDB-TDADR-TIN-CT-CD-2-X.                             \n022674             10  TDB-TDADR-TIN-CT-CD-2         PIC 9(01).         \n022676         07  TDB-TDADR-TIN-CD-3                PIC X(01).         \n022678         07  TDB-TDADR-TIN-NBR-3               PIC 9(09).         \n022680         07  TDB-TDADR-TIN-CT-CD-3             PIC 9(01).         \n022682         07  TDB-TDADR-ALT-ADDR-EOY            PIC 9(01).         \n022684                                                                  \n022686     05  TDB-TDAMESSAGE.                                          \n022688         10  TDB-TDAM-BANK-X.                                     \n022690             15  TDB-TDAM-BANK                 PIC 9(04).         \n022692         10  TDB-TDAM-APPL                     PIC 9(01).         \n022694         10  TDB-TDAM-CODE-TYPE-X.                                \n022696             15  TDB-TDAM-CODE-TYPE            PIC 9(01).         \n022698         10  TDB-TDAM-CODE-X.                                     \n022700             15  TDB-TDAM-CODE                 PIC 9(04).         \n022702         10  TDB-TDAM-RPT-NBR-X.                                  \n022704             15  TDB-TDAM-RPT-NBR              PIC 9(04).         \n022706         10  TDB-TDAM-TEST-MSG-X.                                 \n022708             15  TDB-TDAM-TEST-MSG             PIC 9(01).         \n022710         10  TDB-TDAM-MESSAGE-NBR-X.                              \n022712             15  TDB-TDAM-MESSAGE-NBR          PIC 9(03).         \n022714         10  TDB-TDAM-MESSAGE-GRP.                                \n022716             15  TDB-TDAM-MESSAGE              PIC X(60)          \n022718                                               OCCURS 6 TIMES.    \n022720         10  TDB-TDAM-STOP-DT                  PIC 9(08).         \n022722         10  TDB-TDAM-ADD-DT                   PIC 9(08).         \n022724         10  TDB-TDAM-ADD-TM                   PIC 9(08).         \n022726         10  TDB-TDAM-LUPD-DT                  PIC 9(08).         \n022728         10  TDB-TDAM-LUPD-TM                  PIC 9(08).         \n022730         10  TDB-TDAM-PUB-ID                   PIC X(08).         \n022732                                                                  \n022734                                                                  \n022736 01  BANK-REC.                                                    \n022738     05  BANK-NO                         PIC 9(04).               \n022740     05  BANK-NO-X REDEFINES BANK-NO.                             \n022742         10  BANK-NO-1                   PIC X(01).               \n022744         10  BANK-NO-3                   PIC 9(03).               \n022746     05  BANK-BR-3                       PIC 9(04).               \n022748     05  BANK-CSI-BR-CODE                PIC 9(02).               \n022750     05  BANK-NAME                       PIC X(30).               \n022752     05  BANK-ADDR                       PIC X(28).               \n022754     05  BANK-ADDR-2                     PIC X(27).               \n022756     05  BANK-FED-ID                     PIC X(10).               \n022758     05  BANK-INT-JRNL-BR-PRT            PIC 9(01).               \n022760     05  BANK-CK-PRT-FORMAT              PIC X(01).               \n022762     05  BANK-RESTRICT-REDEMP-TICKET     PIC X(01).               \n022764     05  BANK-CK-PRT-ACCTNO              PIC X(01).               \n022766     05  BANK-RESTRICT-RATE-PRT          PIC X(01).               \n022768     05  BANK-CK-PROTECT                 PIC X(01).               \n022770     05  BANK-SP-CK-REMARK               PIC 9(03).               \n022772     05  BANK-APPL                       PIC 9(01).               \n022774     05  BANK-RMT-IND                    PIC X(02).               \n022776     05  BANK-STATUS                     PIC X(01).               \n022778     05  BANK-TDA-PILOT                  PIC X(01).               \n022780     05  BANK-PHN-NUMBER.                                         \n022782         10  BANK-PHN-AREA               PIC 9(03).               \n022784         10  BANK-PHN-PREFIX             PIC 9(03).               \n022786         10  BANK-PHN-SUFFIX             PIC 9(04).               \n022788     05  BANK-EOY-IRA-PHONE.                                      \n022790         10  BANK-IRA-PHN-AREA           PIC 9(03).               \n022792         10  BANK-IRA-PHN-PREFIX         PIC 9(03).               \n022794         10  BANK-IRA-PHN-SUFFIX         PIC 9(04).               \n022796     05  BANK-EOY-IRA-STMT               PIC X(01).               \n022798     05  BANK-EOY-IRA-STMT-EARLY         PIC X(01).               \n022800     05  BANK-EOY-IRA-STMT-PRINT         PIC X(01).               \n022802     05  BANK-EOY-DELETE-DATE            PIC 9(08).               \n022804     05  BANK-EOY-APRIL-DATE             PIC 9(08).               \n022806     05  BANK-EOY-APRIL-DATE-R REDEFINES BANK-EOY-APRIL-DATE.     \n022808         10  BANK-EOY-APRIL-DATE-CCYY    PIC 9(04).               \n022810         10  BANK-EOY-APRIL-DATE-MMDD    PIC 9(04).               \n022812     05  BANK-EOY-EARLY-DATE             PIC 9(08).               \n022814     05  BANK-EOY-NO-IRA-STMTS           PIC 9(01).               \n022816     05  BANK-EOY-RETURN-TO-BANK         PIC X(01).               \n022818     05  BANK-EOY-EARLY-RUN              PIC X(01).               \n022820     05  BANK-EOY-RPT-SEQ                PIC X(01).               \n022822     05  BANK-EOY-IRA-FICHE              PIC X(01).               \n022824     05  BANK-EOY-IRA-PAPER              PIC X(01).               \n022826     05  BANK-NO-IRA-STMTS               PIC 9(01).               \n022828     05  BANK-OPT-HOL                    PIC X(01).               \n022830     05  BANK-CK21-TDA                   PIC X(01).               \n022832     05  BANK-DQVISTA                    PIC X(01).               \n022834     05  BANK-MSI                        PIC X(01).               \n022836     05  BANK-MSI-OV-TDA                 PIC X(01).               \n022838     05  BANK-BK-IMG-SERV                PIC X(01).               \n022840     05  BANK-FM-SUPPRESS                PIC X(01).               \n022842     05  BANK-EOY-COD-CLOSED-RPT         PIC X(01).               \n022844     05  BANK-PRT-NEW                    PIC X(01).               \n022846     05  BANK-IMONITOR                   PIC X(01).               \n022848     05  BANK-CENTERVIEW                 PIC X(01).               \n022850     05  BANK-TDA-ADD-DAY                PIC X(03).               \n022852     05  BANK-HOLIDAYS                   OCCURS 18 TIMES.         \n022854         10  BANK-HOL-MM                 PIC X(02).               \n022856         10  BANK-HOL-DD                 PIC X(02).               \n022858     05  BANK-CREATE-DT                  PIC 9(07).               \n022860     05  BANK-CREATE-TM                  PIC 9(12).               \n022862     05  BANK-ENTC-TDA                   PIC X(01).               \n022864     05  BANK-EV-3RD-PARTY-1             PIC X(01).               \n022866     05  BANK-EV-3RD-PARTY-2             PIC X(01).               \n022868     05  BANK-HSA-LOCATION               PIC X(01).               \n022870     05  BANK-PROFITABILITY              PIC X(01).               \n022872     05  BANK-BANCVUE                    PIC X(01).               \n022874     05  BANK-SPECIAL-DL-BILLING         PIC X(01).               \n022876     05  BANK-WEB-ENABLED                PIC X(01).               \n022878     05  BANK-CIF-NAME-ADDR              PIC 9(01).               \n022880     05  BANK-MAIL-ADDR-LINES            PIC X(01).               \n022882     05  BANK-BRANCH-LENGTH              PIC 9(01).               \n022884     05  BANK-LOB                        PIC 9(01).               \n022886     05  BANK-LAST-EOM-PROC              PIC 9(08).               \n022888     05  BANK-TRAIN-BK-FLG               PIC X(01).               \n022890     05  BANK-EOY-CIB-F-MERD             PIC X(01).               \n022892                                                                  \n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 356 lines from 11087 to 11442.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 24,
  "total_chunks": 55,
  "start_line": 11087,
  "end_line": 11442,
  "line_count": 356
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
- Source code length: 32891 characters

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
CHUNK 24 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 11087 to 11442 (356 lines)
Chunk Tokens (estimated): ~7,501
Actual Input Tokens: 8,907 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 11087-11442 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 24 of 55 chunks
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
      The source code below is only CHUNK 24 of 55.


=============================================================================
CHUNK 24 SOURCE CODE (Lines 11087-11442)
=============================================================================

```cobol
022182             TDB-TDAPC-BANK-SPECS.                                
022184             15  TDB-TDAPC-CREATE-DT      PIC 9(07).              
022186             15  TDB-TDAPC-CREATE-TM      PIC 9(12).              
022188             15  TDB-TDAPC-DQVISTA        PIC X.                  
022190             15  TDB-TDAPC-MSI            PIC X.                  
022192             15  TDB-TDAPC-BK-TDA-STAT    PIC X.                  
022194             15  TDB-TDAPC-TDA-PILOT REDEFINES                    
022196                 TDB-TDAPC-BK-TDA-STAT    PIC X.                  
022198             15  TDB-TDAPC-BK-STATUS      PIC X.                  
022200             15  TDB-TDAPC-BR-NO          PIC XX.                 
022202             15  TDB-TDAPC-CSI-BR-CODE REDEFINES                  
022204                 TDB-TDAPC-BR-NO          PIC XX.                 
022206             15  TDB-TDAPC-BK-PHONE-NUM.                          
022208                 20  TDB-TDAPC-AREA-CODE  PIC XXX.                
022210                 20  TDB-TDAPC-PHONE.                             
022212                     25  TDB-TDAPC-PHONE-1ST-3 PIC XXX.           
022214                     25  TDB-TDAPC-PHONE-LST-4 PIC X(04).         
022216             15  TDB-TDAPC-PHN-NUMBER REDEFINES                   
022218                 TDB-TDAPC-BK-PHONE-NUM   PIC X(10).              
022220             15  TDB-TDAPC-TDA-ADD-DAY    PIC XXX.                
022222             15  TDB-TDAPC-HOLIDAYS       OCCURS 18 TIMES.        
022224                 20  TDB-TDAPC-HOL-MM     PIC XX.                 
022226                 20  TDB-TDAPC-HOL-DD     PIC XX.                 
022228             15  TDB-TDAPC-FM-SUPPRESS    PIC X.                  
022230             15  TDB-TDAPC-RMT-BK-INDICATOR PIC XX.               
022232             15  TDB-TDAPC-RMT-IND REDEFINES                      
022234                 TDB-TDAPC-RMT-BK-INDICATOR PIC XX.               
022236             15  TDB-TDAPC-BK-ADDR        PIC X(28).              
022238             15  TDB-TDAPC-BK-ADDR-2      PIC X(27).              
022240             15  TDB-TDAPC-FED-ID         PIC X(10).              
022242             15  TDB-TDAPC-EOY-RPT-SEQ    PIC X.                  
022244             15  TDB-TDAPC-EOY-EARLY-RUN  PIC X.                  
022246             15  TDB-TDAPC-EOY-RETURN-TO-BK PIC X.                
022248             15  TDB-TDAPC-EOY-RETURN-TO-BANK REDEFINES           
022250                 TDB-TDAPC-EOY-RETURN-TO-BK PIC X.                
022252             15  TDB-TDAPC-EOY-IRA-PHONE    PIC 9(10).            
022254             15  TDB-TDAPC-EOY-DELETE-DATE  PIC 9(06).            
022256             15  TDB-TDAPC-EOY-IRA-FICHE  PIC X.                  
022258             15  TDB-TDAPC-EOY-IRA-PAPER  PIC X.                  
022260             15  TDB-TDAPC-EOY-IRA-STMT-EARLY PIC X.              
022262             15  TDB-TDAPC-NO-IRA-STMTS   PIC 9.                  
022264             15  TDB-TDAPC-EOY-IRA-STMT   PIC X.                  
022266             15  TDB-TDAPC-EOY-IRA-STMT-PRINT PIC X.              
022268             15  TDB-TDAPC-EOY-EARLY-DATE PIC 9(06).              
022270             15  TDB-TDAPC-CK21-TDA       PIC X.                  
022272             15  TDB-TDAPC-MSI-OV-TDA     PIC 9.                  
022274             15  TDB-TDAPC-BK-IMG-SERV    PIC X(01).              
022276             15  TDB-TDAPC-EOY-APRIL-DATE PIC 9(06).              
022278             15  TDB-TDAPC-EOY-COD-CLOSED-RPT PIC X(01).          
022280             15  TDB-TDAPC-PRT-NEW        PIC 9(01).              
022282             15  TDB-TDAPC-IMONITOR       PIC 9(01).              
022284             15  TDB-TDAPC-ENTC-TDA       PIC X.                  
022286             15  TDB-TDAPC-EV-3RD-PARTY-1 PIC X.                  
022288             15  TDB-TDAPC-EV-3RD-PARTY-2 PIC X.                  
022290             15  TDB-TDAPC-HSA-LOCATION   PIC X.                  
022292             15  TDB-TDAPC-PROFITABILITY  PIC X.                  
022294             15  TDB-TDAPC-BANCVUE        PIC X.                  
022296             15  TDB-TDAPC-SPECIAL-DL-BILLING PIC X.              
022298             15  TDB-TDAPC-CIF-NAME-ADDR      PIC 9.              
022300             15  TDB-TDAPC-MAIL-ADDR-LINES    PIC X.              
022302             15  TDB-TDAPC-WEB-ENABLED        PIC X(01).          
022304             15  TDB-TDAPC-BRANCH-LENGTH      PIC 9.              
022306             15  TDB-TDAPC-LOB                PIC 9.              
022308             15  TDB-TDAPC-BILL-EDIT-TEMPLATES PIC 9.             
022310             15  TDB-TDAPC-MCIF-PRIVACY-OPT   PIC 9.              
022312             15  TDB-TDAPC-TRAIN-BK-FLG       PIC X.              
022314             15  TDB-TDAPC-EOY-CIB-F-MERD     PIC X.              
022316             15  FILLER                       PIC X(39).          
022318             15  TDB-TDAPC-LAST-EOM-PROC      PIC 9(08).          
022320             15  TDB-TDAPC-BUS-DT-AFT-NX      PIC 9(08).          
022322             15  TDB-TDAPC-NEXT-BUS-DATE      PIC 9(08).          
022324                                                                  
022326     05  TDB-TDACHK.                                              
022328         10  TDB-TDACK-BANK-X.                                    
022330             15  TDB-TDACK-BANK           PIC 9(04).              
022332         10  TDB-TDACK-BRCH-X.                                    
022334             15  TDB-TDACK-BRCH           PIC 9(04).              
022336         10  TDB-TDACK-ADDR-CUST-X.                               
022338             15  TDB-TDACK-ADDR-CUST      PIC 9(12).              
022340         10  TDB-TDACK-CUST-X OCCURS 10.                          
022342             15  TDB-TDACK-CUST           PIC 9(12).              
022344         10  TDB-TDACK-ACCT-X OCCURS 10.                          
022346             15  TDB-TDACK-ACCT           PIC 9(10).              
022348         10  TDB-TDACK-LUPD-DATE-X.                               
022350             15  TDB-TDACK-LUPD-DATE      PIC 9(08).              
022352         10  TDB-TDACK-LUPD-TIME-X.                               
022354             15  TDB-TDACK-LUPD-TIME      PIC 9(08).              
022356         10  TDB-TDACK-PUB-ID             PIC X(08).              
022358         10  FILLER                       PIC X(12).              
022360                                                                  
022362     05  TDB-TDABENEF.                                            
022364         10  TDB-TDAB-BANK-X.                                     
022366             15  TDB-TDAB-BANK              PIC 9(04).            
022368         10  TDB-TDAB-CUST-X.                                     
022370             15  TDB-TDAB-CUST              PIC 9(12).            
022372         10  TDB-TDAB-ACCT-X.                                     
022374             15  TDB-TDAB-ACCT             PIC 9(10).             
022376         10  TDB-TDAB-BENEF-NBR-X.                                
022378             15  TDB-TDAB-BENEF-NBR        PIC 9(02).             
022380         10  TDB-TDAB-NAME                 PIC X(40).             
022382         10  TDB-TDAB-NAME-2               PIC X(40).             
022384         10  TDB-TDAB-NAME-3               PIC X(40).             
022386         10  TDB-TDAB-ADDR-1               PIC X(40).             
022388         10  TDB-TDAB-ADDR-2               PIC X(40).             
022390         10  TDB-TDAB-CITY                 PIC X(40).             
022392         10  TDB-TDAB-STATE                PIC X(02).             
022394         10  TDB-TDAB-PROVINCE             PIC X(02).             
022396         10  TDB-TDAB-COUNTRY              PIC X(02).             
022398         10  TDB-TDAB-ZIP-CODE.                                   
022400             15  TDB-TDAB-ZIP-X.                                  
022402                 20  TDB-TDAB-ZIP          PIC 9(05).             
022404             15  TDB-TDAB-ZIP-4-X.                                
022406                 20  TDB-TDAB-ZIP-4        PIC 9(04).             
022408         10  TDB-TDAB-PHONE-X.                                    
022410             15  TDB-TDAB-PHONE            PIC 9(10).             
022412         10  TDB-TDAB-TIN-X.                                      
022414             15  TDB-TDAB-TIN              PIC 9(09).             
022416         10  TDB-TDAB-BIRTH-DT-X.                                 
022418             15  TDB-TDAB-BIRTH-DT         PIC 9(08).             
022420         10  TDB-TDAB-RELATION-X.                                 
022422             15  TDB-TDAB-RELATION         PIC 9(01).             
022424         10  TDB-TDAB-DESIGNATION-X.                              
022426             15  TDB-TDAB-DESIGNATION      PIC 9(01).             
022428         10  TDB-TDAB-PERCENT-X.                                  
022430             15  TDB-TDAB-PERCENT          PIC 9(03).             
022432         10  TDB-TDAB-FREE-REMARK          PIC X(24).             
022434                                                                  
022436     05  TDB-TDAADDR.                                             
022438         07  TDB-TDADR-BANK-X.                                    
022440             10  TDB-TDADR-BANK                PIC 9(04).         
022442         07  TDB-TDADR-CUST-X.                                    
022444             10  TDB-TDADR-CUST                PIC 9(12).         
022446         07  TDB-TDADR-ACCT-X.                                    
022448             10  TDB-TDADR-ACCT                PIC 9(10).         
022450         07  TDB-TDADR-ADDR-USAGE              PIC X(01).         
022452         07  TDB-TDADR-TEMP-BEG-DT-X.                             
022454             10  TDB-TDADR-TEMP-BEG-DT         PIC 9(04).         
022456         07  TDB-TDADR-TEMP-END-DT-X.                             
022458             10  TDB-TDADR-TEMP-END-DT         PIC 9(04).         
022460         07  TDB-TDADR-TEMP-EFF-DT-X.                             
022462             10  TDB-TDADR-TEMP-EFF-DT         PIC 9(08).         
022464         07  TDB-TDADR-TEMP-EXP-DT-X.                             
022466             10  TDB-TDADR-TEMP-EXP-DT         PIC 9(08).         
022468         07  TDB-TDADR-ADDR-GROUP.                                
022470             10  TDB-TDADR-T-ADDR.                                
022472                 15  TDB-TDADR-T-ADDR-1        PIC X(40).         
022474                 15  TDB-TDADR-T-ADDR-2        PIC X(40).         
022476                 15  TDB-TDADR-T-CITY          PIC X(40).         
022478                 15  TDB-TDADR-T-STATE         PIC X(02).         
022480                 15  TDB-TDADR-T-PROVINCE      PIC X(02).         
022482                 15  TDB-TDADR-T-COUNTRY       PIC X(02).         
022484                 15  TDB-TDADR-T-ZIP-CODE.                        
022486                     20  TDB-TDADR-T-ZIP-X.                       
022488                         25  TDB-TDADR-T-ZIP   PIC 9(05).         
022490                     20  TDB-TDADR-T-ZIP-4-X.                     
022492                         25  TDB-TDADR-T-ZIP-4 PIC 9(04).         
022494                 15  TDB-TDADR-T-ALIEN-CD-X.                      
022496                     20  TDB-TDADR-T-ALIEN-CD  PIC 9(01).         
022498                 15  TDB-TDADR-T-BAR-CODE-X.                      
022500                     20  TDB-TDADR-T-BAR-CODE  PIC 9(03).         
022502                 15  TDB-TDADR-T-EMAIL-ADDR    PIC X(100).        
022504                 15  TDB-TDADR-T-EMAIL-ADDR-R                     
022506                                REDEFINES TDB-TDADR-T-EMAIL-ADDR. 
022508                     20  TDB-TDADR-T-EMAIL-ADDR-1-50   PIC X(50). 
022510                     20  TDB-TDADR-T-EMAIL-ADDR-51-100 PIC X(50). 
022512                 15  TDB-TDADR-T-MAIL-CD-X.                       
022514                     20  TDB-TDADR-T-MAIL-CD   PIC 9(01).         
022516                 15  TDB-TDADR-T-ADDR-KEY        PIC X(28).       
022518             10  TDB-TDADR-A-ADDR.                                
022520                 15  TDB-TDADR-A-NAME-1          PIC X(40).       
022522                 15  TDB-TDADR-A-NAME-AREA-1.                     
022524                     20  TDB-TDADR-A-N1-KEY      PIC X(14).       
022526                     20  TDB-TDADR-A-N1-FIRST    PIC X(40).       
022528                     20  TDB-TDADR-A-N1-MID      PIC X(20).       
022530                     20  TDB-TDADR-A-N1-LAST     PIC X(40).       
022532                     20  TDB-TDADR-A-N1-PREFIX   PIC X(12).       
022534                     20  TDB-TDADR-A-N1-SUFFIX   PIC X(12).       
022536                     20  TDB-TDADR-A-N1-FAMILIAR PIC X(20).       
022538                     20  TDB-TDADR-A-N1-PRT-PFX  PIC X(01).       
022540                     20  TDB-TDADR-A-N1-PRT-SFX  PIC X(01).       
022542                     20  TDB-TDADR-A-N1-DESIGNAT PIC X(20).       
022544                 15  TDB-TDADR-A-NAME-2          PIC X(40).       
022546                 15  TDB-TDADR-A-N2-MODIFIED     PIC X(01).       
022548                 15  TDB-TDADR-A-N2-PRINT-CD     PIC X(01).       
022550                 15  TDB-TDADR-A-NAME-AREA-2.                     
022552                     20  TDB-TDADR-A-N2-KEY      PIC X(14).       
022554                     20  TDB-TDADR-A-N2-FIRST    PIC X(40).       
022556                     20  TDB-TDADR-A-N2-MID      PIC X(20).       
022558                     20  TDB-TDADR-A-N2-LAST     PIC X(40).       
022560                     20  TDB-TDADR-A-N2-PREFIX   PIC X(12).       
022562                     20  TDB-TDADR-A-N2-SUFFIX   PIC X(12).       
022564                     20  TDB-TDADR-A-N2-FAMILIAR PIC X(20).       
022566                     20  TDB-TDADR-A-N2-PRT-PFX  PIC X(01).       
022568                     20  TDB-TDADR-A-N2-PRT-SFX  PIC X(01).       
022570                     20  TDB-TDADR-A-N2-DESIGNAT PIC X(20).       
022572                 15  TDB-TDADR-A-NAME-3          PIC X(40).       
022574                 15  TDB-TDADR-A-N3-MODIFIED     PIC X(01).       
022576                 15  TDB-TDADR-A-N3-PRINT-CD     PIC X(01).       
022578                 15  TDB-TDADR-A-NAME-AREA-3.                     
022580                     20  TDB-TDADR-A-N3-KEY      PIC X(14).       
022582                     20  TDB-TDADR-A-N3-FIRST    PIC X(40).       
022584                     20  TDB-TDADR-A-N3-MID      PIC X(20).       
022586                     20  TDB-TDADR-A-N3-LAST     PIC X(40).       
022588                     20  TDB-TDADR-A-N3-PREFIX   PIC X(12).       
022590                     20  TDB-TDADR-A-N3-SUFFIX   PIC X(12).       
022592                     20  TDB-TDADR-A-N3-FAMILIAR PIC X(20).       
022594                     20  TDB-TDADR-A-N3-PRT-PFX  PIC X(01).       
022596                     20  TDB-TDADR-A-N3-PRT-SFX  PIC X(01).       
022598                     20  TDB-TDADR-A-N3-DESIGNAT PIC X(20).       
022600                 15  TDB-TDADR-A-ADDR-KEY        PIC X(28).       
022602                 15  TDB-TDADR-A-ADDR-1        PIC X(40).         
022604                 15  TDB-TDADR-A-ADDR-2        PIC X(40).         
022606                 15  TDB-TDADR-A-CITY          PIC X(40).         
022608                 15  TDB-TDADR-A-STATE         PIC X(02).         
022610                 15  TDB-TDADR-A-PROVINCE      PIC X(02).         
022612                 15  TDB-TDADR-A-COUNTRY       PIC X(02).         
022614                 15  TDB-TDADR-A-ZIP-CODE.                        
022616                     20  TDB-TDADR-A-ZIP-X.                       
022618                         25  TDB-TDADR-A-ZIP   PIC 9(05).         
022620                     20  TDB-TDADR-A-ZIP-4-X.                     
022622                         25  TDB-TDADR-A-ZIP-4 PIC 9(04).         
022624                 15  TDB-TDADR-A-ALIEN-CD-X.                      
022626                     20  TDB-TDADR-A-ALIEN-CD  PIC 9(01).         
022628                 15  TDB-TDADR-A-BAR-CODE-X.                      
022630                     20  TDB-TDADR-A-BAR-CODE  PIC 9(03).         
022632                 15  TDB-TDADR-A-EMAIL-ADDR    PIC X(100).        
022634                 15  TDB-TDADR-A-EMAIL-ADDR-R                     
022636                                REDEFINES TDB-TDADR-A-EMAIL-ADDR. 
022638                     20  TDB-TDADR-A-EMAIL-ADDR-1-50   PIC X(50). 
022640                     20  TDB-TDADR-A-EMAIL-ADDR-51-100 PIC X(50). 
022642                 15  TDB-TDADR-A-MAIL-CD-X.                       
022644                     20  TDB-TDADR-A-MAIL-CD   PIC 9(01).         
022646         07  TDB-TDADR-SHT-NAME                PIC X(20).         
022648         07  TDB-TDADR-LUPD-DATE               PIC 9(08).         
022650         07  TDB-TDADR-LUPD-TIME               PIC 9(08).         
022652         07  TDB-TDADR-PUB-ID                  PIC X(08).         
022654         07  TDB-TDADR-TIN-CD                  PIC X.             
022656         07  TDB-TDADR-TIN-NBR-X.                                 
022658             10  TDB-TDADR-TIN-NBR             PIC 9(9).          
022660         07  TDB-TDADR-TIN-CERT-CD-X.                             
022662             10  TDB-TDADR-TIN-CERT-CD         PIC 9.             
022664         07  TDB-TDADR-TIN-CD-2-X.                                
022666             10  TDB-TDADR-TIN-CD-2            PIC X(01).         
022668         07  TDB-TDADR-TIN-NBR-2-X.                               
022670             10  TDB-TDADR-TIN-NBR-2           PIC 9(09).         
022672         07  TDB-TDADR-TIN-CT-CD-2-X.                             
022674             10  TDB-TDADR-TIN-CT-CD-2         PIC 9(01).         
022676         07  TDB-TDADR-TIN-CD-3                PIC X(01).         
022678         07  TDB-TDADR-TIN-NBR-3               PIC 9(09).         
022680         07  TDB-TDADR-TIN-CT-CD-3             PIC 9(01).         
022682         07  TDB-TDADR-ALT-ADDR-EOY            PIC 9(01).         
022684                                                                  
022686     05  TDB-TDAMESSAGE.                                          
022688         10  TDB-TDAM-BANK-X.                                     
022690             15  TDB-TDAM-BANK                 PIC 9(04).         
022692         10  TDB-TDAM-APPL                     PIC 9(01).         
022694         10  TDB-TDAM-CODE-TYPE-X.                                
022696             15  TDB-TDAM-CODE-TYPE            PIC 9(01).         
022698         10  TDB-TDAM-CODE-X.                                     
022700             15  TDB-TDAM-CODE                 PIC 9(04).         
022702         10  TDB-TDAM-RPT-NBR-X.                                  
022704             15  TDB-TDAM-RPT-NBR              PIC 9(04).         
022706         10  TDB-TDAM-TEST-MSG-X.                                 
022708             15  TDB-TDAM-TEST-MSG             PIC 9(01).         
022710         10  TDB-TDAM-MESSAGE-NBR-X.                              
022712             15  TDB-TDAM-MESSAGE-NBR          PIC 9(03).         
022714         10  TDB-TDAM-MESSAGE-GRP.                                
022716             15  TDB-TDAM-MESSAGE              PIC X(60)          
022718                                               OCCURS 6 TIMES.    
022720         10  TDB-TDAM-STOP-DT                  PIC 9(08).         
022722         10  TDB-TDAM-ADD-DT                   PIC 9(08).         
022724         10  TDB-TDAM-ADD-TM                   PIC 9(08).         
022726         10  TDB-TDAM-LUPD-DT                  PIC 9(08).         
022728         10  TDB-TDAM-LUPD-TM                  PIC 9(08).         
022730         10  TDB-TDAM-PUB-ID                   PIC X(08).         
022732                                                                  
022734                                                                  
022736 01  BANK-REC.                                                    
022738     05  BANK-NO                         PIC 9(04).               
022740     05  BANK-NO-X REDEFINES BANK-NO.                             
022742         10  BANK-NO-1                   PIC X(01).               
022744         10  BANK-NO-3                   PIC 9(03).               
022746     05  BANK-BR-3                       PIC 9(04).               
022748     05  BANK-CSI-BR-CODE                PIC 9(02).               
022750     05  BANK-NAME                       PIC X(30).               
022752     05  BANK-ADDR                       PIC X(28).               
022754     05  BANK-ADDR-2                     PIC X(27).               
022756     05  BANK-FED-ID                     PIC X(10).               
022758     05  BANK-INT-JRNL-BR-PRT            PIC 9(01).               
022760     05  BANK-CK-PRT-FORMAT              PIC X(01).               
022762     05  BANK-RESTRICT-REDEMP-TICKET     PIC X(01).               
022764     05  BANK-CK-PRT-ACCTNO              PIC X(01).               
022766     05  BANK-RESTRICT-RATE-PRT          PIC X(01).               
022768     05  BANK-CK-PROTECT                 PIC X(01).               
022770     05  BANK-SP-CK-REMARK               PIC 9(03).               
022772     05  BANK-APPL                       PIC 9(01).               
022774     05  BANK-RMT-IND                    PIC X(02).               
022776     05  BANK-STATUS                     PIC X(01).               
022778     05  BANK-TDA-PILOT                  PIC X(01).               
022780     05  BANK-PHN-NUMBER.                                         
022782         10  BANK-PHN-AREA               PIC 9(03).               
022784         10  BANK-PHN-PREFIX             PIC 9(03).               
022786         10  BANK-PHN-SUFFIX             PIC 9(04).               
022788     05  BANK-EOY-IRA-PHONE.                                      
022790         10  BANK-IRA-PHN-AREA           PIC 9(03).               
022792         10  BANK-IRA-PHN-PREFIX         PIC 9(03).               
022794         10  BANK-IRA-PHN-SUFFIX         PIC 9(04).               
022796     05  BANK-EOY-IRA-STMT               PIC X(01).               
022798     05  BANK-EOY-IRA-STMT-EARLY         PIC X(01).               
022800     05  BANK-EOY-IRA-STMT-PRINT         PIC X(01).               
022802     05  BANK-EOY-DELETE-DATE            PIC 9(08).               
022804     05  BANK-EOY-APRIL-DATE             PIC 9(08).               
022806     05  BANK-EOY-APRIL-DATE-R REDEFINES BANK-EOY-APRIL-DATE.     
022808         10  BANK-EOY-APRIL-DATE-CCYY    PIC 9(04).               
022810         10  BANK-EOY-APRIL-DATE-MMDD    PIC 9(04).               
022812     05  BANK-EOY-EARLY-DATE             PIC 9(08).               
022814     05  BANK-EOY-NO-IRA-STMTS           PIC 9(01).               
022816     05  BANK-EOY-RETURN-TO-BANK         PIC X(01).               
022818     05  BANK-EOY-EARLY-RUN              PIC X(01).               
022820     05  BANK-EOY-RPT-SEQ                PIC X(01).               
022822     05  BANK-EOY-IRA-FICHE              PIC X(01).               
022824     05  BANK-EOY-IRA-PAPER              PIC X(01).               
022826     05  BANK-NO-IRA-STMTS               PIC 9(01).               
022828     05  BANK-OPT-HOL                    PIC X(01).               
022830     05  BANK-CK21-TDA                   PIC X(01).               
022832     05  BANK-DQVISTA                    PIC X(01).               
022834     05  BANK-MSI                        PIC X(01).               
022836     05  BANK-MSI-OV-TDA                 PIC X(01).               
022838     05  BANK-BK-IMG-SERV                PIC X(01).               
022840     05  BANK-FM-SUPPRESS                PIC X(01).               
022842     05  BANK-EOY-COD-CLOSED-RPT         PIC X(01).               
022844     05  BANK-PRT-NEW                    PIC X(01).               
022846     05  BANK-IMONITOR                   PIC X(01).               
022848     05  BANK-CENTERVIEW                 PIC X(01).               
022850     05  BANK-TDA-ADD-DAY                PIC X(03).               
022852     05  BANK-HOLIDAYS                   OCCURS 18 TIMES.         
022854         10  BANK-HOL-MM                 PIC X(02).               
022856         10  BANK-HOL-DD                 PIC X(02).               
022858     05  BANK-CREATE-DT                  PIC 9(07).               
022860     05  BANK-CREATE-TM                  PIC 9(12).               
022862     05  BANK-ENTC-TDA                   PIC X(01).               
022864     05  BANK-EV-3RD-PARTY-1             PIC X(01).               
022866     05  BANK-EV-3RD-PARTY-2             PIC X(01).               
022868     05  BANK-HSA-LOCATION               PIC X(01).               
022870     05  BANK-PROFITABILITY              PIC X(01).               
022872     05  BANK-BANCVUE                    PIC X(01).               
022874     05  BANK-SPECIAL-DL-BILLING         PIC X(01).               
022876     05  BANK-WEB-ENABLED                PIC X(01).               
022878     05  BANK-CIF-NAME-ADDR              PIC 9(01).               
022880     05  BANK-MAIL-ADDR-LINES            PIC X(01).               
022882     05  BANK-BRANCH-LENGTH              PIC 9(01).               
022884     05  BANK-LOB                        PIC 9(01).               
022886     05  BANK-LAST-EOM-PROC              PIC 9(08).               
022888     05  BANK-TRAIN-BK-FLG               PIC X(01).               
022890     05  BANK-EOY-CIB-F-MERD             PIC X(01).               
022892                                                                  
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 356 lines from 11087 to 11442.

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

