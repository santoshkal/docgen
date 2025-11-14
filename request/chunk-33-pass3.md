# LLM Request Debug File
Generated: 2025-11-13T21:13:04.771387

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 33/55
- **Model**: gpt-4.1
- **Chunk Number**: 33
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~10,021 tokens
- **Total Input**: ~11,979 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 33/55" (ID: detailed-code-explanation)

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


**CHUNK 33 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 33 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 15849 to 16330 (482 lines)\nChunk Tokens (estimated): ~8,040\nActual Input Tokens: 9,446 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 15849-16330 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 33 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 33 of 55.\n\n\n=============================================================================\nCHUNK 33 SOURCE CODE (Lines 15849-16330)\n=============================================================================\n\n```cobol\n031706         HOLD-TDACUST.\n031708     MOVE TDB-TDAC-ZIP OF TDB-TDACUST TO HOLD-TDAC-ZIP OF         \n031710         HOLD-TDACUST.\n031712     MOVE TDB-TDAC-ZIP-4 OF TDB-TDACUST TO HOLD-TDAC-ZIP-4 OF     \n031714         HOLD-TDACUST.\n031716     MOVE TDB-TDAC-LONGITUDE OF TDB-TDACUST TO                    \n031718         HOLD-TDAC-LONGITUDE OF HOLD-TDACUST.\n031720     MOVE TDB-TDAC-LATITUDE OF TDB-TDACUST TO HOLD-TDAC-LATITUDE  \n031722         OF HOLD-TDACUST.\n031724     MOVE TDB-TDAC-MAIL-CD OF TDB-TDACUST TO HOLD-TDAC-MAIL-CD OF \n031726         HOLD-TDACUST.\n031728     MOVE TDB-TDAC-TICKLER-FLAG OF TDB-TDACUST TO                 \n031730         HOLD-TDAC-TICKLER-FLAG OF HOLD-TDACUST.\n031732     MOVE TDB-TDAC-RESIDENT-CD OF TDB-TDACUST TO                  \n031734         HOLD-TDAC-RESIDENT-CD OF HOLD-TDACUST.\n031736     MOVE TDB-TDAC-ALIEN-CD OF TDB-TDACUST TO HOLD-TDAC-ALIEN-CD  \n031738         OF HOLD-TDACUST.\n031740     MOVE TDB-TDAC-SHT-NAME OF TDB-TDACUST TO HOLD-TDAC-SHT-NAME  \n031742         OF HOLD-TDACUST.\n031744     MOVE TDB-TDAC-BAR-CD OF TDB-TDACUST TO HOLD-TDAC-BAR-CD OF   \n031746         HOLD-TDACUST.\n031748     MOVE TDB-TDAC-PHONE-1 OF TDB-TDACUST TO HOLD-TDAC-PHONE-1 OF \n031750         HOLD-TDACUST.\n031752     MOVE TDB-TDAC-PHONE-2 OF TDB-TDACUST TO HOLD-TDAC-PHONE-2 OF \n031754         HOLD-TDACUST.\n031756     MOVE TDB-TDAC-TIN-CD OF TDB-TDACUST TO HOLD-TDAC-TIN-CD OF   \n031758         HOLD-TDACUST.\n031760     MOVE TDB-TDAC-TIN-CERT-CD OF TDB-TDACUST TO                  \n031762         HOLD-TDAC-TIN-CERT-CD OF HOLD-TDACUST.\n031764     MOVE TDB-TDAC-TIN-CERT-DT OF TDB-TDACUST TO                  \n031766         HOLD-TDAC-TIN-CERT-DT OF HOLD-TDACUST.\n031768     MOVE TDB-TDAC-TIN-NBR OF TDB-TDACUST TO HOLD-TDAC-TIN-NBR OF \n031770         HOLD-TDACUST.\n031772     MOVE TDB-TDAC-OFFICER OF TDB-TDACUST TO HOLD-TDAC-OFFICER OF \n031774         HOLD-TDACUST.\n031776     MOVE TDB-TDAC-EMP-CD OF TDB-TDACUST TO HOLD-TDAC-EMP-CD OF   \n031778         HOLD-TDACUST.\n031780     MOVE TDB-TDAC-FREE-MARK OF TDB-TDACUST TO                    \n031782         HOLD-TDAC-FREE-MARK OF HOLD-TDACUST.\n031784     MOVE TDB-TDAC-INQ-SECR-CD OF TDB-TDACUST TO                  \n031786         HOLD-TDAC-INQ-SECR-CD OF HOLD-TDACUST.\n031788     MOVE TDB-TDAC-PRIVACY OF TDB-TDACUST TO HOLD-TDAC-PRIVACY OF \n031790         HOLD-TDACUST.\n031792     MOVE TDB-TDAC-BK-DEF-CD1 OF TDB-TDACUST TO                   \n031794         HOLD-TDAC-BK-DEF-CD1 OF HOLD-TDACUST.\n031796     MOVE TDB-TDAC-BK-DEF-CD2 OF TDB-TDACUST TO                   \n031798         HOLD-TDAC-BK-DEF-CD2 OF HOLD-TDACUST.\n031800     MOVE TDB-TDAC-BK-DEF-CD3 OF TDB-TDACUST TO                   \n031802         HOLD-TDAC-BK-DEF-CD3 OF HOLD-TDACUST.\n031804     MOVE TDB-TDAC-BK-DEF-CD4 OF TDB-TDACUST TO                   \n031806         HOLD-TDAC-BK-DEF-CD4 OF HOLD-TDACUST.\n031808     MOVE TDB-TDAC-BK-DEF-CD5 OF TDB-TDACUST TO                   \n031810         HOLD-TDAC-BK-DEF-CD5 OF HOLD-TDACUST.\n031812     MOVE TDB-TDAC-EMPLOYEE-ID OF TDB-TDACUST TO                  \n031814         HOLD-TDAC-EMPLOYEE-ID OF HOLD-TDACUST.\n031816     MOVE TDB-TDAC-EMAIL-ADDR OF TDB-TDACUST TO                   \n031818         HOLD-TDAC-EMAIL-ADDR OF HOLD-TDACUST.\n031820     MOVE TDB-TDAC-EMAIL-ADDR-1-30 OF TDB-TDACUST TO              \n031822         HOLD-TDAC-EMAIL-ADDR-1-30 OF HOLD-TDACUST.\n031824     MOVE TDB-TDAC-EMAIL-ADDR-31-60 OF TDB-TDACUST TO             \n031826         HOLD-TDAC-EMAIL-ADDR-31-60 OF HOLD-TDACUST.\n031828     MOVE TDB-TDAC-EMAIL-ADDR-61-90 OF TDB-TDACUST TO             \n031830         HOLD-TDAC-EMAIL-ADDR-61-90 OF HOLD-TDACUST.\n031832     MOVE TDB-TDAC-EMAIL-ADDR-91-100 OF TDB-TDACUST TO            \n031834         HOLD-TDAC-EMAIL-ADDR-91-100 OF HOLD-TDACUST.\n031836     MOVE TDB-TDAC-EMAIL-ADDR-1-50 OF TDB-TDACUST TO              \n031838         HOLD-TDAC-EMAIL-ADDR-1-50 OF HOLD-TDACUST.\n031840     MOVE TDB-TDAC-EMAIL-ADDR-51-100 OF TDB-TDACUST TO            \n031842         HOLD-TDAC-EMAIL-ADDR-51-100 OF HOLD-TDACUST.\n031844     MOVE TDB-TDAC-EMAIL-PSSWRD OF TDB-TDACUST TO                 \n031846         HOLD-TDAC-EMAIL-PSSWRD OF HOLD-TDACUST.\n031848     MOVE TDB-TDAC-GENDER OF TDB-TDACUST TO HOLD-TDAC-GENDER OF   \n031850         HOLD-TDACUST.\n031852     MOVE TDB-TDAC-NEW-CUST OF TDB-TDACUST TO HOLD-TDAC-NEW-CUST  \n031854         OF HOLD-TDACUST.\n031856     MOVE TDB-TDAC-OPEN-DT OF TDB-TDACUST TO HOLD-TDAC-OPEN-DT OF \n031858         HOLD-TDACUST.\n031860     MOVE TDB-TDAC-LUPD-DATE OF TDB-TDACUST TO                    \n031862         HOLD-TDAC-LUPD-DATE OF HOLD-TDACUST.\n031864     MOVE TDB-TDAC-LUPD-TIME OF TDB-TDACUST TO                    \n031866         HOLD-TDAC-LUPD-TIME OF HOLD-TDACUST.\n031868     MOVE TDB-TDAC-LST-CONTACT OF TDB-TDACUST TO                  \n031870         HOLD-TDAC-LST-CONTACT OF HOLD-TDACUST.\n031872     MOVE TDB-TDAC-BIRTH-DT OF TDB-TDACUST TO HOLD-TDAC-BIRTH-DT  \n031874         OF HOLD-TDACUST.\n031876     MOVE TDB-TDAC-BIRTH-DT-2 OF TDB-TDACUST TO                   \n031878         HOLD-TDAC-BIRTH-DT-2 OF HOLD-TDACUST.\n031880     MOVE TDB-TDAC-BIRTH-DT-3 OF TDB-TDACUST TO                   \n031882         HOLD-TDAC-BIRTH-DT-3 OF HOLD-TDACUST.\n031884     MOVE TDB-TDAC-DEATH-DT OF TDB-TDACUST TO HOLD-TDAC-DEATH-DT  \n031886         OF HOLD-TDACUST.\n031888     MOVE TDB-TDAC-ADD-DT OF TDB-TDACUST TO HOLD-TDAC-ADD-DT OF   \n031890         HOLD-TDACUST.\n031892     MOVE TDB-TDAC-ADD-TM OF TDB-TDACUST TO HOLD-TDAC-ADD-TM OF   \n031894         HOLD-TDACUST.\n031896     MOVE TDB-TDAC-ROTH-DATE OF TDB-TDACUST TO                    \n031898         HOLD-TDAC-ROTH-DATE OF HOLD-TDACUST.\n031900     MOVE TDB-TDAC-CD-BAL OF TDB-TDACUST TO HOLD-TDAC-CD-BAL OF   \n031902         HOLD-TDACUST.\n031904     MOVE TDB-TDAC-CD-BAL-BYR OF TDB-TDACUST TO                   \n031906         HOLD-TDAC-CD-BAL-BYR OF HOLD-TDACUST.\n031908     MOVE TDB-TDAC-CD-PENLTY OF TDB-TDACUST TO                    \n031910         HOLD-TDAC-CD-PENLTY OF HOLD-TDACUST.\n031912     MOVE TDB-TDAC-CD-WTHLD OF TDB-TDACUST TO HOLD-TDAC-CD-WTHLD  \n031914         OF HOLD-TDACUST.\n031916     MOVE TDB-TDAC-CD-INT OF TDB-TDACUST TO HOLD-TDAC-CD-INT OF   \n031918         HOLD-TDACUST.\n031920     MOVE TDB-TDAC-CD-OID-INT OF TDB-TDACUST TO                   \n031922         HOLD-TDAC-CD-OID-INT OF HOLD-TDACUST.\n031924     MOVE TDB-TDAC-IRA-BAL OF TDB-TDACUST TO HOLD-TDAC-IRA-BAL OF \n031926         HOLD-TDACUST.\n031928     MOVE TDB-TDAC-IRA-BAL-BYR OF TDB-TDACUST TO                  \n031930         HOLD-TDAC-IRA-BAL-BYR OF HOLD-TDACUST.\n031932     MOVE TDB-TDAC-IRA-PENLTY OF TDB-TDACUST TO                   \n031934         HOLD-TDAC-IRA-PENLTY OF HOLD-TDACUST.\n031936     MOVE TDB-TDAC-IRA-WTHLD OF TDB-TDACUST TO                    \n031938         HOLD-TDAC-IRA-WTHLD OF HOLD-TDACUST.\n031940     MOVE TDB-TDAC-IRA-INT OF TDB-TDACUST TO HOLD-TDAC-IRA-INT OF \n031942         HOLD-TDACUST.\n031944     MOVE TDB-TDAC-IRA-CONTR OF TDB-TDACUST TO                    \n031946         HOLD-TDAC-IRA-CONTR OF HOLD-TDACUST.\n031948     MOVE TDB-TDAC-IRA-CONTR-LY OF TDB-TDACUST TO                 \n031950         HOLD-TDAC-IRA-CONTR-LY OF HOLD-TDACUST.\n031952     MOVE TDB-TDAC-IRA-DISTR OF TDB-TDACUST TO                    \n031954         HOLD-TDAC-IRA-DISTR OF HOLD-TDACUST.\n031956     MOVE TDB-TDAC-IRA-DISTR-LY OF TDB-TDACUST TO                 \n031958         HOLD-TDAC-IRA-DISTR-LY OF HOLD-TDACUST.\n031960     MOVE TDB-TDAC-IRA-ROLLOVER OF TDB-TDACUST TO                 \n031962         HOLD-TDAC-IRA-ROLLOVER OF HOLD-TDACUST.\n031964     MOVE TDB-TDAC-IRA-TRF-IN OF TDB-TDACUST TO                   \n031966         HOLD-TDAC-IRA-TRF-IN OF HOLD-TDACUST.\n031968     MOVE TDB-TDAC-IRA-TRF-OUT OF TDB-TDACUST TO                  \n031970         HOLD-TDAC-IRA-TRF-OUT OF HOLD-TDACUST.\n031972     MOVE TDB-TDAC-IRA-FAIR-MKT OF TDB-TDACUST TO                 \n031974         HOLD-TDAC-IRA-FAIR-MKT OF HOLD-TDACUST.\n031976     MOVE TDB-TDAC-CIF-REMARK OF TDB-TDACUST TO                   \n031978         HOLD-TDAC-CIF-REMARK OF HOLD-TDACUST.\n031980     MOVE TDB-TDAC-CD-ST-WHLD OF TDB-TDACUST TO                   \n031982         HOLD-TDAC-CD-ST-WHLD OF HOLD-TDACUST.\n031984     MOVE TDB-TDAC-IRA-ST-WHLD OF TDB-TDACUST TO                  \n031986         HOLD-TDAC-IRA-ST-WHLD OF HOLD-TDACUST.\n031988     MOVE 1 TO Z-II.\n031990 Z-11-22-1-LOOP.\n031992     IF Z-II > 12\n031994         GO TO Z-11-22-1-LOOP-XIT.\n031996     MOVE TDB-TDAC-CURR-YR-AMT OF TDB-TDACUST (Z-II) TO           \n031998         HOLD-TDAC-CURR-YR-AMT OF HOLD-TDACUST (Z-II).\n032000     MOVE TDB-TDAC-LAST-YR-AMT OF TDB-TDACUST (Z-II) TO           \n032002         HOLD-TDAC-LAST-YR-AMT OF HOLD-TDACUST (Z-II).\n032004     ADD 1 TO Z-II.\n032006     GO TO Z-11-22-1-LOOP.\n032008 Z-11-22-1-LOOP-XIT.\n032010     MOVE TDB-TDAC-TIN-CD-2 OF TDB-TDACUST TO HOLD-TDAC-TIN-CD-2  \n032012         OF HOLD-TDACUST.\n032014     MOVE TDB-TDAC-TIN-CRT-CD-2 OF TDB-TDACUST TO                 \n032016         HOLD-TDAC-TIN-CRT-CD-2 OF HOLD-TDACUST.\n032018     MOVE TDB-TDAC-TIN-CRT-DT-2 OF TDB-TDACUST TO                 \n032020         HOLD-TDAC-TIN-CRT-DT-2 OF HOLD-TDACUST.\n032022     MOVE TDB-TDAC-TIN-NBR-2 OF TDB-TDACUST TO                    \n032024         HOLD-TDAC-TIN-NBR-2 OF HOLD-TDACUST.\n032026     MOVE TDB-TDAC-TIN-CD-3 OF TDB-TDACUST TO HOLD-TDAC-TIN-CD-3  \n032028         OF HOLD-TDACUST.\n032030     MOVE TDB-TDAC-TIN-CRT-CD-3 OF TDB-TDACUST TO                 \n032032         HOLD-TDAC-TIN-CRT-CD-3 OF HOLD-TDACUST.\n032034     MOVE TDB-TDAC-TIN-CRT-DT-3 OF TDB-TDACUST TO                 \n032036         HOLD-TDAC-TIN-CRT-DT-3 OF HOLD-TDACUST.\n032038     MOVE TDB-TDAC-TIN-NBR-3 OF TDB-TDACUST TO                    \n032040         HOLD-TDAC-TIN-NBR-3 OF HOLD-TDACUST.\n032042     MOVE TDB-TDAC-NAICS-CD OF TDB-TDACUST TO HOLD-TDAC-NAICS-CD  \n032044         OF HOLD-TDACUST.\n032046     MOVE TDB-TDAC-CIF-PASS-THR OF TDB-TDACUST TO                 \n032048         HOLD-TDAC-CIF-PASS-THR OF HOLD-TDACUST.\n032050     MOVE TDB-TDAC-EMAIL-NTC OF TDB-TDACUST TO                    \n032052         HOLD-TDAC-EMAIL-NTC OF HOLD-TDACUST.\n032054     MOVE TDB-TDAC-RMD-YR-AMT OF TDB-TDACUST TO                   \n032056         HOLD-TDAC-RMD-YR-AMT OF HOLD-TDACUST.\n032058     MOVE TDB-TDAC-ADDR-CHG-DT OF TDB-TDACUST TO                  \n032060         HOLD-TDAC-ADDR-CHG-DT OF HOLD-TDACUST.\n032062     MOVE TDB-TDAC-WTHLD-CD OF TDB-TDACUST TO HOLD-TDAC-WTHLD-CD  \n032064         OF HOLD-TDACUST.\n032066     MOVE TDB-TDAC-ST-WHLD-CD OF TDB-TDACUST TO                   \n032068         HOLD-TDAC-ST-WHLD-CD OF HOLD-TDACUST.\n032070     MOVE TDB-TDAC-WTHLD-AMT OF TDB-TDACUST TO                    \n032072         HOLD-TDAC-WTHLD-AMT OF HOLD-TDACUST.\n032074     MOVE TDB-TDAC-ST-WHLD-AMT OF TDB-TDACUST TO                  \n032076         HOLD-TDAC-ST-WHLD-AMT OF HOLD-TDACUST.\n032078     MOVE TDB-TDAC-FOREIGN-LANG OF TDB-TDACUST TO                 \n032080         HOLD-TDAC-FOREIGN-LANG OF HOLD-TDACUST.\n032082     MOVE TDB-TDAC-L-ROLLOVR-DT OF TDB-TDACUST TO                 \n032084         HOLD-TDAC-L-ROLLOVR-DT OF HOLD-TDACUST.\n032086     MOVE TDB-TDAC-CUSTM-FIELDS OF TDB-TDACUST TO                 \n032088         HOLD-TDAC-CUSTM-FIELDS OF HOLD-TDACUST.\n032090     MOVE TDB-TDAC-LLC-NAME OF TDB-TDACUST TO HOLD-TDAC-LLC-NAME  \n032092         OF HOLD-TDACUST.\n032094     MOVE TDB-TDAC-LLC-TIN-CD OF TDB-TDACUST TO                   \n032096         HOLD-TDAC-LLC-TIN-CD OF HOLD-TDACUST.\n032098     MOVE TDB-TDAC-LLC-TIN OF TDB-TDACUST TO HOLD-TDAC-LLC-TIN OF \n032100         HOLD-TDACUST.\n032102     MOVE TDB-TDAC-FOREIGN-PHN OF TDB-TDACUST TO                  \n032104         HOLD-TDAC-FOREIGN-PHN OF HOLD-TDACUST.\n032106 Z-11-22-END-MOVE.\n032108     IF HOLD-TDAA-APPL = 1\n032110         NEXT SENTENCE ELSE\n032112         GO TO Z-11-23-1-ELSE.\n032114     MOVE SPACES TO TDB-RECORD.\n032116     MOVE \"TDA\" TO TDB-APPL-ID.\n032118     MOVE 00 TO TDB-FUNCTION-CD.\n032120     MOVE \"BR\" TO TDB-ORIGINATE-CLIENT.\n032122     MOVE 01 TO TDB-CLIENT-VER.\n032124     MOVE 03 TO TDB-STRUCT-NBR.\n032126     MOVE 0 TO TDB-ERROR-NBR.\n032128     MOVE 0 TO TDB-MESSAGE-NBR.\n032130     MOVE 01 TO TDB-READ-SET-NBR.\n032132     MOVE \"B\" TO TDB-READ-DIRECTION.\n032134     MOVE \"AT4\" TO TDB-READ-AT.\n032136     MOVE WS-PROCESS-DATE TO TDB-READ-DATE.\n032138     MOVE HOLD-TDAA-BANK TO TDB-TDAI-BANK.\n032140     MOVE HOLD-TDAA-APPL TO TDB-TDAI-APPL.\n032142     MOVE HOLD-TDAA-CUST TO TDB-TDAI-CUST.\n032144     MOVE HOLD-TDAA-ACCT TO TDB-TDAI-ACCT.\n032146************ PERFORM TDB-IRAUPD-INQ\n032148     PERFORM Z-15-PROCEDURE THRU Z-15-XIT.\n032150     IF  Z-EXIT-EDITEXIT\n032152         GO TO Z-11-XIT.\n032154     IF  Z-DMS2-ABORT-FLAG = 1\n032156         GO TO Z-11-XIT.\n032158     IF  Z-EXIT-LEVEL < 0\n032160         GO TO Z-11-END.\n032162*\n032164     IF TDB-ERROR-NBR = 0\n032166         NEXT SENTENCE ELSE\n032168         GO TO Z-11-41-1-ELSE.\n032170     MOVE TDB-TDAI-BANK OF TDB-TDAIRA TO HOLD-TDAI-BANK OF        \n032172         HOLD-TDAIRA.\n032174     MOVE TDB-TDAI-BRCH OF TDB-TDAIRA TO HOLD-TDAI-BRCH OF        \n032176         HOLD-TDAIRA.\n032178     MOVE TDB-TDAI-APPL OF TDB-TDAIRA TO HOLD-TDAI-APPL OF        \n032180         HOLD-TDAIRA.\n032182     MOVE TDB-TDAI-CUST OF TDB-TDAIRA TO HOLD-TDAI-CUST OF        \n032184         HOLD-TDAIRA.\n032186     MOVE TDB-TDAI-ACCT OF TDB-TDAIRA TO HOLD-TDAI-ACCT OF        \n032188         HOLD-TDAIRA.\n032190     MOVE TDB-TDAI-PUB-ID OF TDB-TDAIRA TO HOLD-TDAI-PUB-ID OF    \n032192         HOLD-TDAIRA.\n032194     MOVE TDB-TDAI-ADD-DT OF TDB-TDAIRA TO HOLD-TDAI-ADD-DT OF    \n032196         HOLD-TDAIRA.\n032198     MOVE TDB-TDAI-ADD-TM OF TDB-TDAIRA TO HOLD-TDAI-ADD-TM OF    \n032200         HOLD-TDAIRA.\n032202     MOVE 1 TO Z-II.\n032204 Z-11-42-1-LOOP.\n032206     IF Z-II > 20\n032208         GO TO Z-11-42-1-LOOP-XIT.\n032210     MOVE TDB-TDAI-DS-TYPE OF TDB-TDAIRA (Z-II) TO                \n032212         HOLD-TDAI-DS-TYPE OF HOLD-TDAIRA (Z-II).\n032214     MOVE TDB-TDAI-CN-TYPE OF TDB-TDAIRA (Z-II) TO                \n032216         HOLD-TDAI-CN-TYPE OF HOLD-TDAIRA (Z-II).\n032218     MOVE TDB-TDAI-DS-CN-AMT OF TDB-TDAIRA (Z-II) TO              \n032220         HOLD-TDAI-DS-CN-AMT OF HOLD-TDAIRA (Z-II).\n032222     MOVE TDB-TDAI-DS-PEN-AMT OF TDB-TDAIRA (Z-II) TO             \n032224         HOLD-TDAI-DS-PEN-AMT OF HOLD-TDAIRA (Z-II).\n032226     MOVE TDB-TDAI-DS-WTHLD-AMT OF TDB-TDAIRA (Z-II) TO           \n032228         HOLD-TDAI-DS-WTHLD-AMT OF HOLD-TDAIRA (Z-II).\n032230     MOVE TDB-TDAI-DS-ST-WH-AMT OF TDB-TDAIRA (Z-II) TO           \n032232         HOLD-TDAI-DS-ST-WH-AMT OF HOLD-TDAIRA (Z-II).\n032234     MOVE TDB-TDAI-DS-EXC-EARN OF TDB-TDAIRA (Z-II) TO            \n032236         HOLD-TDAI-DS-EXC-EARN OF HOLD-TDAIRA (Z-II).\n032238     ADD 1 TO Z-II.\n032240     GO TO Z-11-42-1-LOOP.\n032242 Z-11-42-1-LOOP-XIT.\n032244     MOVE TDB-TDAI-DS-C-YTD-CNT OF TDB-TDAIRA TO                  \n032246         HOLD-TDAI-DS-C-YTD-CNT OF HOLD-TDAIRA.\n032248     MOVE TDB-TDAI-DS-P-YTD-CNT OF TDB-TDAIRA TO                  \n032250         HOLD-TDAI-DS-P-YTD-CNT OF HOLD-TDAIRA.\n032252     MOVE TDB-TDAI-DS-AMT-C-YTD OF TDB-TDAIRA TO                  \n032254         HOLD-TDAI-DS-AMT-C-YTD OF HOLD-TDAIRA.\n032256     MOVE TDB-TDAI-DS-AMT-P-YTD OF TDB-TDAIRA TO                  \n032258         HOLD-TDAI-DS-AMT-P-YTD OF HOLD-TDAIRA.\n032260     MOVE TDB-TDAI-DS-INT-AMT OF TDB-TDAIRA TO                    \n032262         HOLD-TDAI-DS-INT-AMT OF HOLD-TDAIRA.\n032264     MOVE TDB-TDAI-CN-YTD-CNT OF TDB-TDAIRA TO                    \n032266         HOLD-TDAI-CN-YTD-CNT OF HOLD-TDAIRA.\n032268     MOVE TDB-TDAI-CN-YTD-AMT OF TDB-TDAIRA TO                    \n032270         HOLD-TDAI-CN-YTD-AMT OF HOLD-TDAIRA.\n032272     MOVE TDB-TDAI-CN-LYTD-AMT OF TDB-TDAIRA TO                   \n032274         HOLD-TDAI-CN-LYTD-AMT OF HOLD-TDAIRA.\n032276     MOVE TDB-TDAI-EMP-CONT-LYR OF TDB-TDAIRA TO                  \n032278         HOLD-TDAI-EMP-CONT-LYR OF HOLD-TDAIRA.\n032280     MOVE TDB-TDAI-REG-CONT-LYR OF TDB-TDAIRA TO                  \n032282         HOLD-TDAI-REG-CONT-LYR OF HOLD-TDAIRA.\n032284     MOVE TDB-TDAI-UNINSURED OF TDB-TDAIRA TO HOLD-TDAI-UNINSURED \n032286         OF HOLD-TDAIRA.\n032288     MOVE TDB-TDAI-ROLLOVER OF TDB-TDAIRA TO HOLD-TDAI-ROLLOVER   \n032290         OF HOLD-TDAIRA.\n032292     MOVE TDB-TDAI-ROLLOVER-LYR OF TDB-TDAIRA TO                  \n032294         HOLD-TDAI-ROLLOVER-LYR OF HOLD-TDAIRA.\n032296     MOVE TDB-TDAI-TRANSFER-IN OF TDB-TDAIRA TO                   \n032298         HOLD-TDAI-TRANSFER-IN OF HOLD-TDAIRA.\n032300     MOVE TDB-TDAI-TRANSFER-OUT OF TDB-TDAIRA TO                  \n032302         HOLD-TDAI-TRANSFER-OUT OF HOLD-TDAIRA.\n032304     MOVE TDB-TDAI-1ST-CN-DATE OF TDB-TDAIRA TO                   \n032306         HOLD-TDAI-1ST-CN-DATE OF HOLD-TDAIRA.\n032308     MOVE TDB-TDAI-BASIS-C-LTD OF TDB-TDAIRA TO                   \n032310         HOLD-TDAI-BASIS-C-LTD OF HOLD-TDAIRA.\n032312     MOVE TDB-TDAI-BASIS-D-LTD OF TDB-TDAIRA TO                   \n032314         HOLD-TDAI-BASIS-D-LTD OF HOLD-TDAIRA.\n032316     MOVE TDB-TDAI-BASIS-D-YTD OF TDB-TDAIRA TO                   \n032318         HOLD-TDAI-BASIS-D-YTD OF HOLD-TDAIRA.\n032320     MOVE TDB-TDAI-CN-TYPE-EX OF TDB-TDAIRA TO                    \n032322         HOLD-TDAI-CN-TYPE-EX OF HOLD-TDAIRA.\n032324     MOVE TDB-TDAI-DS-TYPE-EX-1 OF TDB-TDAIRA TO                  \n032326         HOLD-TDAI-DS-TYPE-EX-1 OF HOLD-TDAIRA.\n032328     MOVE TDB-TDAI-DS-TYPE-EX-2 OF TDB-TDAIRA TO                  \n032330         HOLD-TDAI-DS-TYPE-EX-2 OF HOLD-TDAIRA.\n032332 Z-11-41-1-ELSE.\n032334 Z-11-23-1-ELSE.\n032336 Z-11-END.\n032338     IF Z-EDIT-ERROR\n032340         GO TO Z-11-XIT.\n032342 Z-11-SKIP.\n032344     IF Z-EXIT-LEVEL NOT < 0\n032346         MOVE 0 TO Z-EXIT-CODE\n032348         MOVE 9999 TO Z-EXIT-LEVEL.\n032350 Z-11-XIT.\n032352     EXIT.\n032354*\n032356*****************************************************************\n032358*    PROCEDURE HEADING-SETUP\n032360*****************************************************************\n032362 Z-16-PROCEDURE.\n032364*\n032366     IF Z-EDIT-ERROR\n032368         GO TO Z-16-XIT.\n032370 Z-16-SKIP.\n032372 Z-16-XIT.\n032374     EXIT.\n032376*\n032378*****************************************************************\n032380*    PROCEDURE SETUP-80-HEADER\n032382*****************************************************************\n032384 Z-17-PROCEDURE.\n032386*\n032388     MOVE H-BANK-DATA TO H-80-BK-DATA.\n032390     MOVE H-REPORT-NO TO H-80-RPT-NO.\n032392     MOVE H-CSI-TIME TO H-80-CSI-TIME.\n032394     MOVE H-DATE TO H-80-DATE.\n032396     MOVE H-PAGE-NO-X TO H-80-PAGE-NO.\n032398     IF Z-EDIT-ERROR\n032400         GO TO Z-17-XIT.\n032402 Z-17-SKIP.\n032404 Z-17-XIT.\n032406     EXIT.\n032408*\n032410*****************************************************************\n032412*    PROCEDURE SETUP-NEW-REPORT\n032414*****************************************************************\n032416 Z-18-PROCEDURE.\n032418*\n032420     MOVE BANK-CSI-BR-CODE TO H-CSI-BR-NO.\n032422     MOVE BANK-NO TO H-BANK-NO-9.\n032424     MOVE BANK-NAME TO H-BANK-NAME.\n032426     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.\n032428     MOVE Z-DATE2-MM TO Z-DATE3-MM.\n032430     MOVE Z-DATE2-DD TO Z-DATE3-DD.\n032432     MOVE Z-DATE2-YY TO Z-DATE3-YY.\n032434     MOVE Z-DATE3-FORMAT-9 TO H-DATE.\n032436*    RETRIEVE TODAY'S DATE\n032438     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n032440          USING Z-CALL-CURRENTDATE.\n032442     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n032444     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n032446     ACCEPT Z-DATE0-TIME   FROM TIME.\n032448     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.\n032450     MOVE Z-DATE0-UU TO Z-DATE4-UU.\n032452     MOVE Z-DATE4-FORMAT-9 TO H-CSI-HHMM.\n032454*    RETRIEVE TODAY'S DATE\n032456     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n032458          USING Z-CALL-CURRENTDATE.\n032460     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n032462     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n032464     ACCEPT Z-DATE0-TIME   FROM TIME.\n032466     MOVE Z-DATE0-DD TO Z-DATE5-DD.\n032468     MOVE Z-DATE5-FORMAT-9 TO H-CSI-DD.\n032470     MOVE 0 TO WS-NEW-RPT.\n032472     MOVE 1 TO PAGE-ADVANCE.\n032474     IF Z-EDIT-ERROR\n032476         GO TO Z-18-XIT.\n032478 Z-18-SKIP.\n032480 Z-18-XIT.\n032482     EXIT.\n032484*\n032486*****************************************************************\n032488*    PROCEDURE CLEAR-HEADINGS\n032490*****************************************************************\n032492 Z-19-PROCEDURE.\n032494*\n032496     MOVE SPACES TO HEADER-LINE2.\n032498     MOVE SPACES TO HEADER-LINE3.\n032500     MOVE SPACES TO HEADER-LINE4.\n032502     MOVE SPACES TO HEADER-LINE5.\n032504     IF Z-EDIT-ERROR\n032506         GO TO Z-19-XIT.\n032508 Z-19-SKIP.\n032510 Z-19-XIT.\n032512     EXIT.\n032514*\n032516*****************************************************************\n032518*    PROCEDURE CHECK-PRT-FILE\n032520*****************************************************************\n032522 Z-20-PROCEDURE.\n032524*\n032526     MOVE 0 TO Z-EXIT-CODE.\n032528     MOVE 9999 TO Z-EXIT-LEVEL.\n032530     IF H-REPORT-NO = \"TD-4920\" OR \"TD-4720\"\n032532         NEXT SENTENCE ELSE\n032534         GO TO Z-20-1-1-ELSE.\n032536     MOVE \"CSI\" TO GWS-APPL.\n032538     GO TO Z-20-1-ENDIF.\n032540 Z-20-1-1-ELSE.\n032542     MOVE \"TDA\" TO GWS-APPL.\n032544 Z-20-1-ENDIF.\n032546     MOVE BANK-NO TO GWS-BANK-NUMBER.\n032548     MOVE BANK-CSI-BR-CODE TO GWS-BRANCH-CODE.\n032550     MOVE \"PRT\" TO GWS-LPRT-CST.\n032552     MOVE 1 TO GWS-NO-PARTS.\n032554     MOVE 0 TO GWS-MICROFICHE-CODE.\n032556     MOVE 0 TO GWS-TIME.\n032558     MOVE 1 TO COBOL74-CODE.\n032560     MOVE 1 TO GWS-LONG-PRTNAMES.\n032562     MOVE 1 TO GWS-BKFILE-OPEN.\n032564     MOVE BANK-CSI-BR-CODE TO GWS-CSI-DC.\n032566     MOVE BANK-CSI-BR-CODE TO H-CSI-BR-NO.\n032568     MOVE BANK-NO TO H-BANK-NO-9.\n032570     MOVE BANK-NAME TO H-BANK-NAME.\n032572     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.\n032574     MOVE Z-DATE2-MM TO Z-DATE3-MM.\n032576     MOVE Z-DATE2-DD TO Z-DATE3-DD.\n032578     MOVE Z-DATE2-YY TO Z-DATE3-YY.\n032580     MOVE Z-DATE3-FORMAT-9 TO H-DATE.\n032582*    RETRIEVE TODAY'S DATE\n032584     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n032586          USING Z-CALL-CURRENTDATE.\n032588     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n032590     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n032592     ACCEPT Z-DATE0-TIME   FROM TIME.\n032594     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.\n032596     MOVE Z-DATE0-UU TO Z-DATE4-UU.\n032598     MOVE Z-DATE4-FORMAT-9 TO H-CSI-HHMM.\n032600*    RETRIEVE TODAY'S DATE\n032602     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n032604          USING Z-CALL-CURRENTDATE.\n032606     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n032608     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n032610     ACCEPT Z-DATE0-TIME   FROM TIME.\n032612     MOVE Z-DATE0-DD TO Z-DATE5-DD.\n032614     MOVE Z-DATE5-FORMAT-9 TO H-CSI-DD.\n032616     MOVE 1 TO GWS-LONG-PRTNAMES-NEW.\n032618     MOVE \"GENERAL.\" TO GWS-PACK.\n032620     IF BANK-RMT-IND = SPACES\n032622         NEXT SENTENCE ELSE\n032624         GO TO Z-20-22-1-ELSE.\n032626     MOVE 0 TO GWS-RMT-PRT-OPTION.\n032628     GO TO Z-20-22-ENDIF.\n032630 Z-20-22-1-ELSE.\n032632     MOVE 1 TO GWS-RMT-PRT-OPTION.\n032634 Z-20-22-ENDIF.\n032636     MOVE BANK-PRT-NEW TO GWS-PRT-NEW.\n032638     MOVE \"000\" TO GWS-RMT-EXT.\n032640     IF LIST-REQUEST AND PRT-LIST-CLOSE\n032642         NEXT SENTENCE ELSE\n032644         GO TO Z-20-27-1-ELSE.\n032646     MOVE \"SP\" TO GWS-PRT-DESCRIPTOR.\n032648     IF H-REPORT-NO = \"TD-4920\"\n032650         NEXT SENTENCE ELSE\n032652         GO TO Z-20-29-1-ELSE.\n032654     MOVE \"492\" TO GWS-RMT-EXT.\n032656     GO TO Z-20-29-ENDIF.\n032658 Z-20-29-1-ELSE.\n032660     IF H-REPORT-NO = \"TDA-054\"\n032662         NEXT SENTENCE ELSE\n032664         GO TO Z-20-29-2-ELSE.\n032666     MOVE \"054\" TO GWS-RMT-EXT.\n032668     GO TO Z-20-29-ENDIF.\n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 482 lines from 15849 to 16330.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 33,
  "total_chunks": 55,
  "start_line": 15849,
  "end_line": 16330,
  "line_count": 482
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
- Source code length: 30630 characters

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
CHUNK 33 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 15849 to 16330 (482 lines)
Chunk Tokens (estimated): ~8,040
Actual Input Tokens: 9,446 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 15849-16330 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 33 of 55 chunks
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
      The source code below is only CHUNK 33 of 55.


=============================================================================
CHUNK 33 SOURCE CODE (Lines 15849-16330)
=============================================================================

```cobol
031706         HOLD-TDACUST.
031708     MOVE TDB-TDAC-ZIP OF TDB-TDACUST TO HOLD-TDAC-ZIP OF         
031710         HOLD-TDACUST.
031712     MOVE TDB-TDAC-ZIP-4 OF TDB-TDACUST TO HOLD-TDAC-ZIP-4 OF     
031714         HOLD-TDACUST.
031716     MOVE TDB-TDAC-LONGITUDE OF TDB-TDACUST TO                    
031718         HOLD-TDAC-LONGITUDE OF HOLD-TDACUST.
031720     MOVE TDB-TDAC-LATITUDE OF TDB-TDACUST TO HOLD-TDAC-LATITUDE  
031722         OF HOLD-TDACUST.
031724     MOVE TDB-TDAC-MAIL-CD OF TDB-TDACUST TO HOLD-TDAC-MAIL-CD OF 
031726         HOLD-TDACUST.
031728     MOVE TDB-TDAC-TICKLER-FLAG OF TDB-TDACUST TO                 
031730         HOLD-TDAC-TICKLER-FLAG OF HOLD-TDACUST.
031732     MOVE TDB-TDAC-RESIDENT-CD OF TDB-TDACUST TO                  
031734         HOLD-TDAC-RESIDENT-CD OF HOLD-TDACUST.
031736     MOVE TDB-TDAC-ALIEN-CD OF TDB-TDACUST TO HOLD-TDAC-ALIEN-CD  
031738         OF HOLD-TDACUST.
031740     MOVE TDB-TDAC-SHT-NAME OF TDB-TDACUST TO HOLD-TDAC-SHT-NAME  
031742         OF HOLD-TDACUST.
031744     MOVE TDB-TDAC-BAR-CD OF TDB-TDACUST TO HOLD-TDAC-BAR-CD OF   
031746         HOLD-TDACUST.
031748     MOVE TDB-TDAC-PHONE-1 OF TDB-TDACUST TO HOLD-TDAC-PHONE-1 OF 
031750         HOLD-TDACUST.
031752     MOVE TDB-TDAC-PHONE-2 OF TDB-TDACUST TO HOLD-TDAC-PHONE-2 OF 
031754         HOLD-TDACUST.
031756     MOVE TDB-TDAC-TIN-CD OF TDB-TDACUST TO HOLD-TDAC-TIN-CD OF   
031758         HOLD-TDACUST.
031760     MOVE TDB-TDAC-TIN-CERT-CD OF TDB-TDACUST TO                  
031762         HOLD-TDAC-TIN-CERT-CD OF HOLD-TDACUST.
031764     MOVE TDB-TDAC-TIN-CERT-DT OF TDB-TDACUST TO                  
031766         HOLD-TDAC-TIN-CERT-DT OF HOLD-TDACUST.
031768     MOVE TDB-TDAC-TIN-NBR OF TDB-TDACUST TO HOLD-TDAC-TIN-NBR OF 
031770         HOLD-TDACUST.
031772     MOVE TDB-TDAC-OFFICER OF TDB-TDACUST TO HOLD-TDAC-OFFICER OF 
031774         HOLD-TDACUST.
031776     MOVE TDB-TDAC-EMP-CD OF TDB-TDACUST TO HOLD-TDAC-EMP-CD OF   
031778         HOLD-TDACUST.
031780     MOVE TDB-TDAC-FREE-MARK OF TDB-TDACUST TO                    
031782         HOLD-TDAC-FREE-MARK OF HOLD-TDACUST.
031784     MOVE TDB-TDAC-INQ-SECR-CD OF TDB-TDACUST TO                  
031786         HOLD-TDAC-INQ-SECR-CD OF HOLD-TDACUST.
031788     MOVE TDB-TDAC-PRIVACY OF TDB-TDACUST TO HOLD-TDAC-PRIVACY OF 
031790         HOLD-TDACUST.
031792     MOVE TDB-TDAC-BK-DEF-CD1 OF TDB-TDACUST TO                   
031794         HOLD-TDAC-BK-DEF-CD1 OF HOLD-TDACUST.
031796     MOVE TDB-TDAC-BK-DEF-CD2 OF TDB-TDACUST TO                   
031798         HOLD-TDAC-BK-DEF-CD2 OF HOLD-TDACUST.
031800     MOVE TDB-TDAC-BK-DEF-CD3 OF TDB-TDACUST TO                   
031802         HOLD-TDAC-BK-DEF-CD3 OF HOLD-TDACUST.
031804     MOVE TDB-TDAC-BK-DEF-CD4 OF TDB-TDACUST TO                   
031806         HOLD-TDAC-BK-DEF-CD4 OF HOLD-TDACUST.
031808     MOVE TDB-TDAC-BK-DEF-CD5 OF TDB-TDACUST TO                   
031810         HOLD-TDAC-BK-DEF-CD5 OF HOLD-TDACUST.
031812     MOVE TDB-TDAC-EMPLOYEE-ID OF TDB-TDACUST TO                  
031814         HOLD-TDAC-EMPLOYEE-ID OF HOLD-TDACUST.
031816     MOVE TDB-TDAC-EMAIL-ADDR OF TDB-TDACUST TO                   
031818         HOLD-TDAC-EMAIL-ADDR OF HOLD-TDACUST.
031820     MOVE TDB-TDAC-EMAIL-ADDR-1-30 OF TDB-TDACUST TO              
031822         HOLD-TDAC-EMAIL-ADDR-1-30 OF HOLD-TDACUST.
031824     MOVE TDB-TDAC-EMAIL-ADDR-31-60 OF TDB-TDACUST TO             
031826         HOLD-TDAC-EMAIL-ADDR-31-60 OF HOLD-TDACUST.
031828     MOVE TDB-TDAC-EMAIL-ADDR-61-90 OF TDB-TDACUST TO             
031830         HOLD-TDAC-EMAIL-ADDR-61-90 OF HOLD-TDACUST.
031832     MOVE TDB-TDAC-EMAIL-ADDR-91-100 OF TDB-TDACUST TO            
031834         HOLD-TDAC-EMAIL-ADDR-91-100 OF HOLD-TDACUST.
031836     MOVE TDB-TDAC-EMAIL-ADDR-1-50 OF TDB-TDACUST TO              
031838         HOLD-TDAC-EMAIL-ADDR-1-50 OF HOLD-TDACUST.
031840     MOVE TDB-TDAC-EMAIL-ADDR-51-100 OF TDB-TDACUST TO            
031842         HOLD-TDAC-EMAIL-ADDR-51-100 OF HOLD-TDACUST.
031844     MOVE TDB-TDAC-EMAIL-PSSWRD OF TDB-TDACUST TO                 
031846         HOLD-TDAC-EMAIL-PSSWRD OF HOLD-TDACUST.
031848     MOVE TDB-TDAC-GENDER OF TDB-TDACUST TO HOLD-TDAC-GENDER OF   
031850         HOLD-TDACUST.
031852     MOVE TDB-TDAC-NEW-CUST OF TDB-TDACUST TO HOLD-TDAC-NEW-CUST  
031854         OF HOLD-TDACUST.
031856     MOVE TDB-TDAC-OPEN-DT OF TDB-TDACUST TO HOLD-TDAC-OPEN-DT OF 
031858         HOLD-TDACUST.
031860     MOVE TDB-TDAC-LUPD-DATE OF TDB-TDACUST TO                    
031862         HOLD-TDAC-LUPD-DATE OF HOLD-TDACUST.
031864     MOVE TDB-TDAC-LUPD-TIME OF TDB-TDACUST TO                    
031866         HOLD-TDAC-LUPD-TIME OF HOLD-TDACUST.
031868     MOVE TDB-TDAC-LST-CONTACT OF TDB-TDACUST TO                  
031870         HOLD-TDAC-LST-CONTACT OF HOLD-TDACUST.
031872     MOVE TDB-TDAC-BIRTH-DT OF TDB-TDACUST TO HOLD-TDAC-BIRTH-DT  
031874         OF HOLD-TDACUST.
031876     MOVE TDB-TDAC-BIRTH-DT-2 OF TDB-TDACUST TO                   
031878         HOLD-TDAC-BIRTH-DT-2 OF HOLD-TDACUST.
031880     MOVE TDB-TDAC-BIRTH-DT-3 OF TDB-TDACUST TO                   
031882         HOLD-TDAC-BIRTH-DT-3 OF HOLD-TDACUST.
031884     MOVE TDB-TDAC-DEATH-DT OF TDB-TDACUST TO HOLD-TDAC-DEATH-DT  
031886         OF HOLD-TDACUST.
031888     MOVE TDB-TDAC-ADD-DT OF TDB-TDACUST TO HOLD-TDAC-ADD-DT OF   
031890         HOLD-TDACUST.
031892     MOVE TDB-TDAC-ADD-TM OF TDB-TDACUST TO HOLD-TDAC-ADD-TM OF   
031894         HOLD-TDACUST.
031896     MOVE TDB-TDAC-ROTH-DATE OF TDB-TDACUST TO                    
031898         HOLD-TDAC-ROTH-DATE OF HOLD-TDACUST.
031900     MOVE TDB-TDAC-CD-BAL OF TDB-TDACUST TO HOLD-TDAC-CD-BAL OF   
031902         HOLD-TDACUST.
031904     MOVE TDB-TDAC-CD-BAL-BYR OF TDB-TDACUST TO                   
031906         HOLD-TDAC-CD-BAL-BYR OF HOLD-TDACUST.
031908     MOVE TDB-TDAC-CD-PENLTY OF TDB-TDACUST TO                    
031910         HOLD-TDAC-CD-PENLTY OF HOLD-TDACUST.
031912     MOVE TDB-TDAC-CD-WTHLD OF TDB-TDACUST TO HOLD-TDAC-CD-WTHLD  
031914         OF HOLD-TDACUST.
031916     MOVE TDB-TDAC-CD-INT OF TDB-TDACUST TO HOLD-TDAC-CD-INT OF   
031918         HOLD-TDACUST.
031920     MOVE TDB-TDAC-CD-OID-INT OF TDB-TDACUST TO                   
031922         HOLD-TDAC-CD-OID-INT OF HOLD-TDACUST.
031924     MOVE TDB-TDAC-IRA-BAL OF TDB-TDACUST TO HOLD-TDAC-IRA-BAL OF 
031926         HOLD-TDACUST.
031928     MOVE TDB-TDAC-IRA-BAL-BYR OF TDB-TDACUST TO                  
031930         HOLD-TDAC-IRA-BAL-BYR OF HOLD-TDACUST.
031932     MOVE TDB-TDAC-IRA-PENLTY OF TDB-TDACUST TO                   
031934         HOLD-TDAC-IRA-PENLTY OF HOLD-TDACUST.
031936     MOVE TDB-TDAC-IRA-WTHLD OF TDB-TDACUST TO                    
031938         HOLD-TDAC-IRA-WTHLD OF HOLD-TDACUST.
031940     MOVE TDB-TDAC-IRA-INT OF TDB-TDACUST TO HOLD-TDAC-IRA-INT OF 
031942         HOLD-TDACUST.
031944     MOVE TDB-TDAC-IRA-CONTR OF TDB-TDACUST TO                    
031946         HOLD-TDAC-IRA-CONTR OF HOLD-TDACUST.
031948     MOVE TDB-TDAC-IRA-CONTR-LY OF TDB-TDACUST TO                 
031950         HOLD-TDAC-IRA-CONTR-LY OF HOLD-TDACUST.
031952     MOVE TDB-TDAC-IRA-DISTR OF TDB-TDACUST TO                    
031954         HOLD-TDAC-IRA-DISTR OF HOLD-TDACUST.
031956     MOVE TDB-TDAC-IRA-DISTR-LY OF TDB-TDACUST TO                 
031958         HOLD-TDAC-IRA-DISTR-LY OF HOLD-TDACUST.
031960     MOVE TDB-TDAC-IRA-ROLLOVER OF TDB-TDACUST TO                 
031962         HOLD-TDAC-IRA-ROLLOVER OF HOLD-TDACUST.
031964     MOVE TDB-TDAC-IRA-TRF-IN OF TDB-TDACUST TO                   
031966         HOLD-TDAC-IRA-TRF-IN OF HOLD-TDACUST.
031968     MOVE TDB-TDAC-IRA-TRF-OUT OF TDB-TDACUST TO                  
031970         HOLD-TDAC-IRA-TRF-OUT OF HOLD-TDACUST.
031972     MOVE TDB-TDAC-IRA-FAIR-MKT OF TDB-TDACUST TO                 
031974         HOLD-TDAC-IRA-FAIR-MKT OF HOLD-TDACUST.
031976     MOVE TDB-TDAC-CIF-REMARK OF TDB-TDACUST TO                   
031978         HOLD-TDAC-CIF-REMARK OF HOLD-TDACUST.
031980     MOVE TDB-TDAC-CD-ST-WHLD OF TDB-TDACUST TO                   
031982         HOLD-TDAC-CD-ST-WHLD OF HOLD-TDACUST.
031984     MOVE TDB-TDAC-IRA-ST-WHLD OF TDB-TDACUST TO                  
031986         HOLD-TDAC-IRA-ST-WHLD OF HOLD-TDACUST.
031988     MOVE 1 TO Z-II.
031990 Z-11-22-1-LOOP.
031992     IF Z-II > 12
031994         GO TO Z-11-22-1-LOOP-XIT.
031996     MOVE TDB-TDAC-CURR-YR-AMT OF TDB-TDACUST (Z-II) TO           
031998         HOLD-TDAC-CURR-YR-AMT OF HOLD-TDACUST (Z-II).
032000     MOVE TDB-TDAC-LAST-YR-AMT OF TDB-TDACUST (Z-II) TO           
032002         HOLD-TDAC-LAST-YR-AMT OF HOLD-TDACUST (Z-II).
032004     ADD 1 TO Z-II.
032006     GO TO Z-11-22-1-LOOP.
032008 Z-11-22-1-LOOP-XIT.
032010     MOVE TDB-TDAC-TIN-CD-2 OF TDB-TDACUST TO HOLD-TDAC-TIN-CD-2  
032012         OF HOLD-TDACUST.
032014     MOVE TDB-TDAC-TIN-CRT-CD-2 OF TDB-TDACUST TO                 
032016         HOLD-TDAC-TIN-CRT-CD-2 OF HOLD-TDACUST.
032018     MOVE TDB-TDAC-TIN-CRT-DT-2 OF TDB-TDACUST TO                 
032020         HOLD-TDAC-TIN-CRT-DT-2 OF HOLD-TDACUST.
032022     MOVE TDB-TDAC-TIN-NBR-2 OF TDB-TDACUST TO                    
032024         HOLD-TDAC-TIN-NBR-2 OF HOLD-TDACUST.
032026     MOVE TDB-TDAC-TIN-CD-3 OF TDB-TDACUST TO HOLD-TDAC-TIN-CD-3  
032028         OF HOLD-TDACUST.
032030     MOVE TDB-TDAC-TIN-CRT-CD-3 OF TDB-TDACUST TO                 
032032         HOLD-TDAC-TIN-CRT-CD-3 OF HOLD-TDACUST.
032034     MOVE TDB-TDAC-TIN-CRT-DT-3 OF TDB-TDACUST TO                 
032036         HOLD-TDAC-TIN-CRT-DT-3 OF HOLD-TDACUST.
032038     MOVE TDB-TDAC-TIN-NBR-3 OF TDB-TDACUST TO                    
032040         HOLD-TDAC-TIN-NBR-3 OF HOLD-TDACUST.
032042     MOVE TDB-TDAC-NAICS-CD OF TDB-TDACUST TO HOLD-TDAC-NAICS-CD  
032044         OF HOLD-TDACUST.
032046     MOVE TDB-TDAC-CIF-PASS-THR OF TDB-TDACUST TO                 
032048         HOLD-TDAC-CIF-PASS-THR OF HOLD-TDACUST.
032050     MOVE TDB-TDAC-EMAIL-NTC OF TDB-TDACUST TO                    
032052         HOLD-TDAC-EMAIL-NTC OF HOLD-TDACUST.
032054     MOVE TDB-TDAC-RMD-YR-AMT OF TDB-TDACUST TO                   
032056         HOLD-TDAC-RMD-YR-AMT OF HOLD-TDACUST.
032058     MOVE TDB-TDAC-ADDR-CHG-DT OF TDB-TDACUST TO                  
032060         HOLD-TDAC-ADDR-CHG-DT OF HOLD-TDACUST.
032062     MOVE TDB-TDAC-WTHLD-CD OF TDB-TDACUST TO HOLD-TDAC-WTHLD-CD  
032064         OF HOLD-TDACUST.
032066     MOVE TDB-TDAC-ST-WHLD-CD OF TDB-TDACUST TO                   
032068         HOLD-TDAC-ST-WHLD-CD OF HOLD-TDACUST.
032070     MOVE TDB-TDAC-WTHLD-AMT OF TDB-TDACUST TO                    
032072         HOLD-TDAC-WTHLD-AMT OF HOLD-TDACUST.
032074     MOVE TDB-TDAC-ST-WHLD-AMT OF TDB-TDACUST TO                  
032076         HOLD-TDAC-ST-WHLD-AMT OF HOLD-TDACUST.
032078     MOVE TDB-TDAC-FOREIGN-LANG OF TDB-TDACUST TO                 
032080         HOLD-TDAC-FOREIGN-LANG OF HOLD-TDACUST.
032082     MOVE TDB-TDAC-L-ROLLOVR-DT OF TDB-TDACUST TO                 
032084         HOLD-TDAC-L-ROLLOVR-DT OF HOLD-TDACUST.
032086     MOVE TDB-TDAC-CUSTM-FIELDS OF TDB-TDACUST TO                 
032088         HOLD-TDAC-CUSTM-FIELDS OF HOLD-TDACUST.
032090     MOVE TDB-TDAC-LLC-NAME OF TDB-TDACUST TO HOLD-TDAC-LLC-NAME  
032092         OF HOLD-TDACUST.
032094     MOVE TDB-TDAC-LLC-TIN-CD OF TDB-TDACUST TO                   
032096         HOLD-TDAC-LLC-TIN-CD OF HOLD-TDACUST.
032098     MOVE TDB-TDAC-LLC-TIN OF TDB-TDACUST TO HOLD-TDAC-LLC-TIN OF 
032100         HOLD-TDACUST.
032102     MOVE TDB-TDAC-FOREIGN-PHN OF TDB-TDACUST TO                  
032104         HOLD-TDAC-FOREIGN-PHN OF HOLD-TDACUST.
032106 Z-11-22-END-MOVE.
032108     IF HOLD-TDAA-APPL = 1
032110         NEXT SENTENCE ELSE
032112         GO TO Z-11-23-1-ELSE.
032114     MOVE SPACES TO TDB-RECORD.
032116     MOVE "TDA" TO TDB-APPL-ID.
032118     MOVE 00 TO TDB-FUNCTION-CD.
032120     MOVE "BR" TO TDB-ORIGINATE-CLIENT.
032122     MOVE 01 TO TDB-CLIENT-VER.
032124     MOVE 03 TO TDB-STRUCT-NBR.
032126     MOVE 0 TO TDB-ERROR-NBR.
032128     MOVE 0 TO TDB-MESSAGE-NBR.
032130     MOVE 01 TO TDB-READ-SET-NBR.
032132     MOVE "B" TO TDB-READ-DIRECTION.
032134     MOVE "AT4" TO TDB-READ-AT.
032136     MOVE WS-PROCESS-DATE TO TDB-READ-DATE.
032138     MOVE HOLD-TDAA-BANK TO TDB-TDAI-BANK.
032140     MOVE HOLD-TDAA-APPL TO TDB-TDAI-APPL.
032142     MOVE HOLD-TDAA-CUST TO TDB-TDAI-CUST.
032144     MOVE HOLD-TDAA-ACCT TO TDB-TDAI-ACCT.
032146************ PERFORM TDB-IRAUPD-INQ
032148     PERFORM Z-15-PROCEDURE THRU Z-15-XIT.
032150     IF  Z-EXIT-EDITEXIT
032152         GO TO Z-11-XIT.
032154     IF  Z-DMS2-ABORT-FLAG = 1
032156         GO TO Z-11-XIT.
032158     IF  Z-EXIT-LEVEL < 0
032160         GO TO Z-11-END.
032162*
032164     IF TDB-ERROR-NBR = 0
032166         NEXT SENTENCE ELSE
032168         GO TO Z-11-41-1-ELSE.
032170     MOVE TDB-TDAI-BANK OF TDB-TDAIRA TO HOLD-TDAI-BANK OF        
032172         HOLD-TDAIRA.
032174     MOVE TDB-TDAI-BRCH OF TDB-TDAIRA TO HOLD-TDAI-BRCH OF        
032176         HOLD-TDAIRA.
032178     MOVE TDB-TDAI-APPL OF TDB-TDAIRA TO HOLD-TDAI-APPL OF        
032180         HOLD-TDAIRA.
032182     MOVE TDB-TDAI-CUST OF TDB-TDAIRA TO HOLD-TDAI-CUST OF        
032184         HOLD-TDAIRA.
032186     MOVE TDB-TDAI-ACCT OF TDB-TDAIRA TO HOLD-TDAI-ACCT OF        
032188         HOLD-TDAIRA.
032190     MOVE TDB-TDAI-PUB-ID OF TDB-TDAIRA TO HOLD-TDAI-PUB-ID OF    
032192         HOLD-TDAIRA.
032194     MOVE TDB-TDAI-ADD-DT OF TDB-TDAIRA TO HOLD-TDAI-ADD-DT OF    
032196         HOLD-TDAIRA.
032198     MOVE TDB-TDAI-ADD-TM OF TDB-TDAIRA TO HOLD-TDAI-ADD-TM OF    
032200         HOLD-TDAIRA.
032202     MOVE 1 TO Z-II.
032204 Z-11-42-1-LOOP.
032206     IF Z-II > 20
032208         GO TO Z-11-42-1-LOOP-XIT.
032210     MOVE TDB-TDAI-DS-TYPE OF TDB-TDAIRA (Z-II) TO                
032212         HOLD-TDAI-DS-TYPE OF HOLD-TDAIRA (Z-II).
032214     MOVE TDB-TDAI-CN-TYPE OF TDB-TDAIRA (Z-II) TO                
032216         HOLD-TDAI-CN-TYPE OF HOLD-TDAIRA (Z-II).
032218     MOVE TDB-TDAI-DS-CN-AMT OF TDB-TDAIRA (Z-II) TO              
032220         HOLD-TDAI-DS-CN-AMT OF HOLD-TDAIRA (Z-II).
032222     MOVE TDB-TDAI-DS-PEN-AMT OF TDB-TDAIRA (Z-II) TO             
032224         HOLD-TDAI-DS-PEN-AMT OF HOLD-TDAIRA (Z-II).
032226     MOVE TDB-TDAI-DS-WTHLD-AMT OF TDB-TDAIRA (Z-II) TO           
032228         HOLD-TDAI-DS-WTHLD-AMT OF HOLD-TDAIRA (Z-II).
032230     MOVE TDB-TDAI-DS-ST-WH-AMT OF TDB-TDAIRA (Z-II) TO           
032232         HOLD-TDAI-DS-ST-WH-AMT OF HOLD-TDAIRA (Z-II).
032234     MOVE TDB-TDAI-DS-EXC-EARN OF TDB-TDAIRA (Z-II) TO            
032236         HOLD-TDAI-DS-EXC-EARN OF HOLD-TDAIRA (Z-II).
032238     ADD 1 TO Z-II.
032240     GO TO Z-11-42-1-LOOP.
032242 Z-11-42-1-LOOP-XIT.
032244     MOVE TDB-TDAI-DS-C-YTD-CNT OF TDB-TDAIRA TO                  
032246         HOLD-TDAI-DS-C-YTD-CNT OF HOLD-TDAIRA.
032248     MOVE TDB-TDAI-DS-P-YTD-CNT OF TDB-TDAIRA TO                  
032250         HOLD-TDAI-DS-P-YTD-CNT OF HOLD-TDAIRA.
032252     MOVE TDB-TDAI-DS-AMT-C-YTD OF TDB-TDAIRA TO                  
032254         HOLD-TDAI-DS-AMT-C-YTD OF HOLD-TDAIRA.
032256     MOVE TDB-TDAI-DS-AMT-P-YTD OF TDB-TDAIRA TO                  
032258         HOLD-TDAI-DS-AMT-P-YTD OF HOLD-TDAIRA.
032260     MOVE TDB-TDAI-DS-INT-AMT OF TDB-TDAIRA TO                    
032262         HOLD-TDAI-DS-INT-AMT OF HOLD-TDAIRA.
032264     MOVE TDB-TDAI-CN-YTD-CNT OF TDB-TDAIRA TO                    
032266         HOLD-TDAI-CN-YTD-CNT OF HOLD-TDAIRA.
032268     MOVE TDB-TDAI-CN-YTD-AMT OF TDB-TDAIRA TO                    
032270         HOLD-TDAI-CN-YTD-AMT OF HOLD-TDAIRA.
032272     MOVE TDB-TDAI-CN-LYTD-AMT OF TDB-TDAIRA TO                   
032274         HOLD-TDAI-CN-LYTD-AMT OF HOLD-TDAIRA.
032276     MOVE TDB-TDAI-EMP-CONT-LYR OF TDB-TDAIRA TO                  
032278         HOLD-TDAI-EMP-CONT-LYR OF HOLD-TDAIRA.
032280     MOVE TDB-TDAI-REG-CONT-LYR OF TDB-TDAIRA TO                  
032282         HOLD-TDAI-REG-CONT-LYR OF HOLD-TDAIRA.
032284     MOVE TDB-TDAI-UNINSURED OF TDB-TDAIRA TO HOLD-TDAI-UNINSURED 
032286         OF HOLD-TDAIRA.
032288     MOVE TDB-TDAI-ROLLOVER OF TDB-TDAIRA TO HOLD-TDAI-ROLLOVER   
032290         OF HOLD-TDAIRA.
032292     MOVE TDB-TDAI-ROLLOVER-LYR OF TDB-TDAIRA TO                  
032294         HOLD-TDAI-ROLLOVER-LYR OF HOLD-TDAIRA.
032296     MOVE TDB-TDAI-TRANSFER-IN OF TDB-TDAIRA TO                   
032298         HOLD-TDAI-TRANSFER-IN OF HOLD-TDAIRA.
032300     MOVE TDB-TDAI-TRANSFER-OUT OF TDB-TDAIRA TO                  
032302         HOLD-TDAI-TRANSFER-OUT OF HOLD-TDAIRA.
032304     MOVE TDB-TDAI-1ST-CN-DATE OF TDB-TDAIRA TO                   
032306         HOLD-TDAI-1ST-CN-DATE OF HOLD-TDAIRA.
032308     MOVE TDB-TDAI-BASIS-C-LTD OF TDB-TDAIRA TO                   
032310         HOLD-TDAI-BASIS-C-LTD OF HOLD-TDAIRA.
032312     MOVE TDB-TDAI-BASIS-D-LTD OF TDB-TDAIRA TO                   
032314         HOLD-TDAI-BASIS-D-LTD OF HOLD-TDAIRA.
032316     MOVE TDB-TDAI-BASIS-D-YTD OF TDB-TDAIRA TO                   
032318         HOLD-TDAI-BASIS-D-YTD OF HOLD-TDAIRA.
032320     MOVE TDB-TDAI-CN-TYPE-EX OF TDB-TDAIRA TO                    
032322         HOLD-TDAI-CN-TYPE-EX OF HOLD-TDAIRA.
032324     MOVE TDB-TDAI-DS-TYPE-EX-1 OF TDB-TDAIRA TO                  
032326         HOLD-TDAI-DS-TYPE-EX-1 OF HOLD-TDAIRA.
032328     MOVE TDB-TDAI-DS-TYPE-EX-2 OF TDB-TDAIRA TO                  
032330         HOLD-TDAI-DS-TYPE-EX-2 OF HOLD-TDAIRA.
032332 Z-11-41-1-ELSE.
032334 Z-11-23-1-ELSE.
032336 Z-11-END.
032338     IF Z-EDIT-ERROR
032340         GO TO Z-11-XIT.
032342 Z-11-SKIP.
032344     IF Z-EXIT-LEVEL NOT < 0
032346         MOVE 0 TO Z-EXIT-CODE
032348         MOVE 9999 TO Z-EXIT-LEVEL.
032350 Z-11-XIT.
032352     EXIT.
032354*
032356*****************************************************************
032358*    PROCEDURE HEADING-SETUP
032360*****************************************************************
032362 Z-16-PROCEDURE.
032364*
032366     IF Z-EDIT-ERROR
032368         GO TO Z-16-XIT.
032370 Z-16-SKIP.
032372 Z-16-XIT.
032374     EXIT.
032376*
032378*****************************************************************
032380*    PROCEDURE SETUP-80-HEADER
032382*****************************************************************
032384 Z-17-PROCEDURE.
032386*
032388     MOVE H-BANK-DATA TO H-80-BK-DATA.
032390     MOVE H-REPORT-NO TO H-80-RPT-NO.
032392     MOVE H-CSI-TIME TO H-80-CSI-TIME.
032394     MOVE H-DATE TO H-80-DATE.
032396     MOVE H-PAGE-NO-X TO H-80-PAGE-NO.
032398     IF Z-EDIT-ERROR
032400         GO TO Z-17-XIT.
032402 Z-17-SKIP.
032404 Z-17-XIT.
032406     EXIT.
032408*
032410*****************************************************************
032412*    PROCEDURE SETUP-NEW-REPORT
032414*****************************************************************
032416 Z-18-PROCEDURE.
032418*
032420     MOVE BANK-CSI-BR-CODE TO H-CSI-BR-NO.
032422     MOVE BANK-NO TO H-BANK-NO-9.
032424     MOVE BANK-NAME TO H-BANK-NAME.
032426     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.
032428     MOVE Z-DATE2-MM TO Z-DATE3-MM.
032430     MOVE Z-DATE2-DD TO Z-DATE3-DD.
032432     MOVE Z-DATE2-YY TO Z-DATE3-YY.
032434     MOVE Z-DATE3-FORMAT-9 TO H-DATE.
032436*    RETRIEVE TODAY'S DATE
032438     CALL "CURRENT_DATE OF GENERALSUPPORT"
032440          USING Z-CALL-CURRENTDATE.
032442     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
032444     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
032446     ACCEPT Z-DATE0-TIME   FROM TIME.
032448     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.
032450     MOVE Z-DATE0-UU TO Z-DATE4-UU.
032452     MOVE Z-DATE4-FORMAT-9 TO H-CSI-HHMM.
032454*    RETRIEVE TODAY'S DATE
032456     CALL "CURRENT_DATE OF GENERALSUPPORT"
032458          USING Z-CALL-CURRENTDATE.
032460     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
032462     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
032464     ACCEPT Z-DATE0-TIME   FROM TIME.
032466     MOVE Z-DATE0-DD TO Z-DATE5-DD.
032468     MOVE Z-DATE5-FORMAT-9 TO H-CSI-DD.
032470     MOVE 0 TO WS-NEW-RPT.
032472     MOVE 1 TO PAGE-ADVANCE.
032474     IF Z-EDIT-ERROR
032476         GO TO Z-18-XIT.
032478 Z-18-SKIP.
032480 Z-18-XIT.
032482     EXIT.
032484*
032486*****************************************************************
032488*    PROCEDURE CLEAR-HEADINGS
032490*****************************************************************
032492 Z-19-PROCEDURE.
032494*
032496     MOVE SPACES TO HEADER-LINE2.
032498     MOVE SPACES TO HEADER-LINE3.
032500     MOVE SPACES TO HEADER-LINE4.
032502     MOVE SPACES TO HEADER-LINE5.
032504     IF Z-EDIT-ERROR
032506         GO TO Z-19-XIT.
032508 Z-19-SKIP.
032510 Z-19-XIT.
032512     EXIT.
032514*
032516*****************************************************************
032518*    PROCEDURE CHECK-PRT-FILE
032520*****************************************************************
032522 Z-20-PROCEDURE.
032524*
032526     MOVE 0 TO Z-EXIT-CODE.
032528     MOVE 9999 TO Z-EXIT-LEVEL.
032530     IF H-REPORT-NO = "TD-4920" OR "TD-4720"
032532         NEXT SENTENCE ELSE
032534         GO TO Z-20-1-1-ELSE.
032536     MOVE "CSI" TO GWS-APPL.
032538     GO TO Z-20-1-ENDIF.
032540 Z-20-1-1-ELSE.
032542     MOVE "TDA" TO GWS-APPL.
032544 Z-20-1-ENDIF.
032546     MOVE BANK-NO TO GWS-BANK-NUMBER.
032548     MOVE BANK-CSI-BR-CODE TO GWS-BRANCH-CODE.
032550     MOVE "PRT" TO GWS-LPRT-CST.
032552     MOVE 1 TO GWS-NO-PARTS.
032554     MOVE 0 TO GWS-MICROFICHE-CODE.
032556     MOVE 0 TO GWS-TIME.
032558     MOVE 1 TO COBOL74-CODE.
032560     MOVE 1 TO GWS-LONG-PRTNAMES.
032562     MOVE 1 TO GWS-BKFILE-OPEN.
032564     MOVE BANK-CSI-BR-CODE TO GWS-CSI-DC.
032566     MOVE BANK-CSI-BR-CODE TO H-CSI-BR-NO.
032568     MOVE BANK-NO TO H-BANK-NO-9.
032570     MOVE BANK-NAME TO H-BANK-NAME.
032572     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.
032574     MOVE Z-DATE2-MM TO Z-DATE3-MM.
032576     MOVE Z-DATE2-DD TO Z-DATE3-DD.
032578     MOVE Z-DATE2-YY TO Z-DATE3-YY.
032580     MOVE Z-DATE3-FORMAT-9 TO H-DATE.
032582*    RETRIEVE TODAY'S DATE
032584     CALL "CURRENT_DATE OF GENERALSUPPORT"
032586          USING Z-CALL-CURRENTDATE.
032588     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
032590     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
032592     ACCEPT Z-DATE0-TIME   FROM TIME.
032594     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.
032596     MOVE Z-DATE0-UU TO Z-DATE4-UU.
032598     MOVE Z-DATE4-FORMAT-9 TO H-CSI-HHMM.
032600*    RETRIEVE TODAY'S DATE
032602     CALL "CURRENT_DATE OF GENERALSUPPORT"
032604          USING Z-CALL-CURRENTDATE.
032606     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
032608     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
032610     ACCEPT Z-DATE0-TIME   FROM TIME.
032612     MOVE Z-DATE0-DD TO Z-DATE5-DD.
032614     MOVE Z-DATE5-FORMAT-9 TO H-CSI-DD.
032616     MOVE 1 TO GWS-LONG-PRTNAMES-NEW.
032618     MOVE "GENERAL." TO GWS-PACK.
032620     IF BANK-RMT-IND = SPACES
032622         NEXT SENTENCE ELSE
032624         GO TO Z-20-22-1-ELSE.
032626     MOVE 0 TO GWS-RMT-PRT-OPTION.
032628     GO TO Z-20-22-ENDIF.
032630 Z-20-22-1-ELSE.
032632     MOVE 1 TO GWS-RMT-PRT-OPTION.
032634 Z-20-22-ENDIF.
032636     MOVE BANK-PRT-NEW TO GWS-PRT-NEW.
032638     MOVE "000" TO GWS-RMT-EXT.
032640     IF LIST-REQUEST AND PRT-LIST-CLOSE
032642         NEXT SENTENCE ELSE
032644         GO TO Z-20-27-1-ELSE.
032646     MOVE "SP" TO GWS-PRT-DESCRIPTOR.
032648     IF H-REPORT-NO = "TD-4920"
032650         NEXT SENTENCE ELSE
032652         GO TO Z-20-29-1-ELSE.
032654     MOVE "492" TO GWS-RMT-EXT.
032656     GO TO Z-20-29-ENDIF.
032658 Z-20-29-1-ELSE.
032660     IF H-REPORT-NO = "TDA-054"
032662         NEXT SENTENCE ELSE
032664         GO TO Z-20-29-2-ELSE.
032666     MOVE "054" TO GWS-RMT-EXT.
032668     GO TO Z-20-29-ENDIF.
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 482 lines from 15849 to 16330.

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

