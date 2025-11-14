# LLM Request Debug File
Generated: 2025-11-13T20:05:23.494881

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 5/55
- **Model**: gpt-4.1
- **Chunk Number**: 5
- **Pass Number**: 3
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~9,666 tokens
- **Total Input**: ~11,624 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 5/55" (ID: detailed-code-explanation)

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


**CHUNK 5 of 55**: Continue numbering from previous chunks.

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
  "source_code": "\n=============================================================================\nCHUNK 5 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 1616 to 1969 (354 lines)\nChunk Tokens (estimated): ~6,327\nActual Input Tokens: 7,733 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 1616-1969 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 5 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 5 of 55.\n\n\n=============================================================================\nCHUNK 5 SOURCE CODE (Lines 1616-1969)\n=============================================================================\n\n```cobol\n003240             Z-DATE-MDY-STRING.\n003242             15  Z-DATE-MDY-MM       PIC  9(02).\n003244             15  Z-DATE-MDY-DD       PIC  9(02).\n003246             15  Z-DATE-MDY-YY       PIC  9(02).\n003248         10  Z-DATE-ACCUM            PIC S9(04) BINARY.\n003250         10  Z-DATE-MONTH-LIMIT      PIC S9(04) BINARY.\n003252     05  Z-DATE-CC-CUTOFF            PIC  9(02) BINARY.\n003254     05  Z-DATE-DEFAULT-CC           PIC  9(02) BINARY.\n003256     05  Z-DATE-DEFAULT-YY           PIC  9(02) BINARY.\n003258     05  Z-DATE-DEFAULT-MM           PIC  9(02) BINARY.\n003260     05  Z-DATE-DEFAULT-DD           PIC  9(02) BINARY.\n003262     05  Z-DATE-LEAP-YEAR-WA.\n003264         10  Z-DATE-FORMAT-YEAR.\n003266             15  Z-DATE-FORMAT-CC    PIC  9(02).\n003268             15  Z-DATE-FORMAT-YY    PIC  9(02).\n003270         10  Z-DATE-FORMAT-CCYY\n003272             REDEFINES\n003274             Z-DATE-FORMAT-YEAR      PIC  9(04).\n003276         10  Z-DATE-YEAR-WORK        PIC S9(04) BINARY.\n003278         10  Z-DATE-DIVIDE-WORK      PIC S9(04) BINARY.\n003280         10  Z-DATE-QUOTIENT         PIC S9(04) BINARY.\n003282         10  Z-DATE-REMAINDER        PIC S9(04) BINARY.\n003284         10  Z-DATE-YEAR-MOD-4       PIC S9(04) BINARY.\n003286         10  Z-DATE-YEAR-MOD-100     PIC S9(04) BINARY.\n003288         10  Z-DATE-YEAR-MOD-400     PIC S9(04) BINARY.\n003290         10  Z-DATE-LEAP-YR-FLAG     PIC S9(01) BINARY.\n003292             88  Z-DATE-LEAP-YEAR                  VALUE +1.\n003294     05  Z-DATE-CONVERT-STATUS-FLAGS.\n003296         10  Z-DATE-CONVERT-STATUS   PIC S9(04) BINARY.\n003298             88  Z-DATE-CNVRT-SUCCESS              VALUE +0.\n003300             88  Z-DATE-CNVRT-UNEXPECTD-FAIL       VALUE -1.\n003302             88  Z-DATE-CNVRT-MM-2-MMM-FAIL        VALUE -10.\n003304             88  Z-DATE-CNVRT-MM-2-MONTH-FAIL      VALUE -11.\n003306             88  Z-DATE-CNVRT-MMM-2-MONTH-FAIL     VALUE -12.\n003308             88  Z-DATE-CNVRT-MMM-2-MM-FAIL        VALUE -13.\n003310             88  Z-DATE-CNVRT-MONTH-2-MM-FAIL      VALUE -14.\n003312             88  Z-DATE-CNVRT-MONTH-2-MMM-FAIL     VALUE -15.\n003314             88  Z-DATE-CNVRT-DD-2-DDD-FAIL        VALUE -16.\n003316             88  Z-DATE-CNVRT-DD-2-DAY-FAIL        VALUE -17.\n003318             88  Z-DATE-CNVRT-DDD-2-DAY-FAIL       VALUE -18.\n003320             88  Z-DATE-CNVRT-DDD-2-DD-FAIL        VALUE -19.\n003322             88  Z-DATE-CNVRT-DAY-2-DD-FAIL        VALUE -20.\n003324             88  Z-DATE-CNVRT-DAY-2-DDD-FAIL       VALUE -21.\n003326             88  Z-DATE-CNVRT-UU-2-SS-FAIL         VALUE -22.\n003328             88  Z-DATE-CNVRT-SS-2-UU-FAIL         VALUE -23.\n003330             88  Z-DATE-CNVRT-UU-2-ZZ-FAIL         VALUE -24.\n003332             88  Z-DATE-CNVRT-ZZ-2-DD-FAIL         VALUE -25.\n003334     05  Z-DATE-MONTH-TABLE-DATA.\n003336         10  FILLER          PIC  X(13) VALUE \"01JANUARY  31\".\n003338         10  FILLER          PIC  X(13) VALUE \"02FEBRUARY 28\".\n003340         10  FILLER          PIC  X(13) VALUE \"03MARCH    31\".\n003342         10  FILLER          PIC  X(13) VALUE \"04APRIL    30\".\n003344         10  FILLER          PIC  X(13) VALUE \"05MAY      31\".\n003346         10  FILLER          PIC  X(13) VALUE \"06JUNE     30\".\n003348         10  FILLER          PIC  X(13) VALUE \"07JULY     31\".\n003350         10  FILLER          PIC  X(13) VALUE \"08AUGUST   31\".\n003352         10  FILLER          PIC  X(13) VALUE \"09SEPTEMBER30\".\n003354         10  FILLER          PIC  X(13) VALUE \"10OCTOBER  31\".\n003356         10  FILLER          PIC  X(13) VALUE \"11NOVEMBER 30\".\n003358         10  FILLER          PIC  X(13) VALUE \"12DECEMBER 31\".\n003360         10  FILLER          PIC  X(13) VALUE \"99MMMOVFLOW99\".\n003362     05  Z-DATE-MONTH-TABLE REDEFINES\n003364         Z-DATE-MONTH-TABLE-DATA        OCCURS 13 TIMES\n003366                                        INDEXED BY Z-DATE-MM-I.\n003368         10  Z-DATE-TBL-MM           PIC  9(02).\n003370         10  Z-DATE-TBL-MONTH.\n003372             15  Z-DATE-TBL-MMM      PIC  X(03).\n003374             15  FILLER              PIC  X(06).\n003376         10  Z-DATE-TBL-DAYS-IN-MON  PIC  9(02).\n003378     05  Z-DATE0-FORMAT.\n003380         10  Z-DATE0-CC              PIC 99.\n003382         10  Z-DATE0-YYMMDD.\n003384             15  Z-DATE0-YY          PIC 99.\n003386             15  Z-DATE0-MM          PIC 99.\n003388             15  Z-DATE0-DD          PIC 99.\n003390         10  Z-DATE0-YYJJJ.\n003392             15  Z-DATE0-YYY         PIC 99.\n003394             15  Z-DATE0-JJJ         PIC 999.\n003396         10  Z-DATE0-TIME.\n003398             15  Z-DATE0-ZZ          PIC 99.\n003400             15  Z-DATE0-UU          PIC 99.\n003402             15  Z-DATE0-SS          PIC 99.\n003404             15  Z-DATE0-TT          PIC 99.\n003406     05  Z-DATE1-FORMAT.\n003408         10  Z-DATE1-CC              PIC 99.\n003410         10  Z-DATE1-YY              PIC 99.\n003412         10  Z-DATE1-JJJ             PIC 999.\n003414         10  Z-DATE1-ZZ              PIC 99.\n003416         10  Z-DATE1-UU              PIC 99.\n003418         10  Z-DATE1-SS              PIC 99.\n003420         10  Z-DATE1-TT              PIC 99.\n003422     05  Z-DATE1-FORMAT-9 REDEFINES Z-DATE1-FORMAT\n003424                                     PIC 9(15).\n003426     05  Z-DATE2-FORMAT.\n003428         10  Z-DATE2-CC              PIC 99.\n003430         10  Z-DATE2-YY              PIC 99.\n003432         10  Z-DATE2-MM              PIC 99.\n003434         10  Z-DATE2-DD              PIC 99.\n003436     05  Z-DATE2-FORMAT-9 REDEFINES Z-DATE2-FORMAT\n003438                                     PIC 9(8).\n003440     05  Z-DATE3-FORMAT.\n003442         10  Z-DATE3-MM              PIC 99.\n003444         10  Z-DATE3-DD              PIC 99.\n003446         10  Z-DATE3-YY              PIC 99.\n003448     05  Z-DATE3-FORMAT-9 REDEFINES Z-DATE3-FORMAT\n003450                                     PIC 9(6).\n003452     05  Z-DATE4-FORMAT.\n003454         10  Z-DATE4-ZZ              PIC 99.\n003456         10  Z-DATE4-UU              PIC 99.\n003458     05  Z-DATE4-FORMAT-9 REDEFINES Z-DATE4-FORMAT\n003460                                     PIC 9(4).\n003462     05  Z-DATE5-FORMAT.\n003464         10  Z-DATE5-DD              PIC 99.\n003466     05  Z-DATE5-FORMAT-9 REDEFINES Z-DATE5-FORMAT\n003468                                     PIC 9(2).\n003470     05  Z-DATE6-FORMAT.\n003472         10  Z-DATE6-MM              PIC 99.\n003474         10  Z-DATE6-CH1             PIC X.\n003476         10  Z-DATE6-DD              PIC 99.\n003478         10  Z-DATE6-CH2             PIC X.\n003480         10  Z-DATE6-CC              PIC 99.\n003482         10  Z-DATE6-YY              PIC 99.\n003484     05  Z-DATE7-FORMAT.\n003486         10  Z-DATE7-MM              PIC 99.\n003488         10  Z-DATE7-DD              PIC 99.\n003490     05  Z-DATE7-FORMAT-9 REDEFINES Z-DATE7-FORMAT\n003492                                     PIC 9(4).\n003494     05  Z-RESTART-BY-COUNT-LIMIT      PIC S9(8) VALUE 100.\n003496     05  Z-RESTART-FOR-COUNT-LIMIT     PIC S9(8) VALUE 100.\n003498     05  Z-CUSTOM-VALUED               PIC X.\n003500*\n003502**** FILE EXCEPTION\n003504*\n003506 01  Z-FL-EXCEPT-TITLE                 PIC X(200) VALUE SPACES.\n003508 01  Z-FL-EXCEPT-MSG.\n003510     05  Z-FL-EXCEPT-ERR                PIC X(27).\n003512     05  Z-FL-EXCEPT-LIT-PARN           PIC X.\n003514     05  Z-FL-EXCEPT-STATUS             PIC X(2).\n003516         88  Z-FILE-EOF                           VALUE \"10\".\n003518         88  Z-FILE-DUPLICATES                    VALUE \"22\".\n003520         88  Z-FILE-NOTFOUND                      VALUE \"23\".\n003522         88  Z-FILE-BOUNDARY                      VALUE \"24\".\n003524     05  Z-FL-EXCEPT-LIT-ON             PIC X(10).\n003526     05  Z-FL-EXCEPT-FILE               PIC X(30).\n003528     05  Z-FL-EXCEPT-LIT-AT             PIC X(4).\n003530     05  Z-FL-EXCEPT-SEQ                PIC 9(6).\n003532*\n003534**** DATABASE EXCEPTION\n003536*\n003538 01  Z-DMS-EXCEPT-MSG.\n003540     05  Z-DMS-EXCEPT-LIT-DMS                   PIC X(4).\n003542     05  Z-DMS-EXCEPT-CAT.\n003544         10  FILLER                             PIC X(11).\n003546         10  Z-DMS-EXCEPT-CAT-NO                PIC 9(2).\n003548         10  FILLER                             PIC X(7).\n003550     05  Z-DMS-EXCEPT-LIT-SUBCAT                PIC X(9).\n003552     05  Z-DMS-EXCEPT-SUBCAT                    PIC 9(3).\n003554     05  Z-DMS-EXCEPT-LIT-AT                    PIC X(5).\n003556     05  Z-DMS-EXCEPT-SEQ                       PIC 9(6).\n003558     05  Z-DMS-EXCEPT-LIT-ON                    PIC X(4).\n003560     05  Z-DMS-EXCEPT-STR                       PIC X(18).\n003562     05  Z-DMS-EXCEPT-LIT-OF                    PIC X(4).\n003564     05  Z-DMS-EXCEPT-DB                        PIC X(18).\n003566*\n003568**** SAVE RECORD\n003570*\n003572 01  Z-SAVE-REC.\n003574     05  FILLER                                 PIC X(1677).\n003576*\n003578 01  Z-SAVE-REC-FLAG                    PIC 9 VALUE 0.\n003580*\n003582****** USER AREA ******\n003584 01  SWT-1                       PIC 9(01) VALUE 0.               \n003586     88 SW1-0                              VALUE 0.               \n003588     88 SW1-1                              VALUE 1.               \n003590 01  SWT-2                       PIC 9(01) VALUE 0.               \n003592     88 SW2-0                              VALUE 0.               \n003594     88 SW2-1                              VALUE 1.               \n003596 01  SWT-3                       PIC 9(01) VALUE 0.               \n003598     88 SW3-0                              VALUE 0.               \n003600     88 SW3-1                              VALUE 1.               \n003602 01  SWT-4                       PIC 9(01) VALUE 0.               \n003604     88 SW4-0                              VALUE 0.               \n003606     88 SW4-1                              VALUE 1.               \n003608 01  SWT-5                       PIC 9(01) VALUE 0.               \n003610     88 SW5-0                              VALUE 0.               \n003612     88 SW5-1                              VALUE 1.               \n003614 01  SWT-6                       PIC 9(01) VALUE 0.               \n003616     88 SW6-0                              VALUE 0.               \n003618     88 SW6-1                              VALUE 1.               \n003620 01  SWT-7                       PIC 9(01) VALUE 0.               \n003622     88 SW7-0                              VALUE 0.               \n003624     88 SW7-1                              VALUE 1.               \n003626 01  SWT-8                       PIC 9(01) VALUE 0.               \n003628     88 SW8-0                              VALUE 0.               \n003630     88 SW8-1                              VALUE 1.               \n003632 01  WS-PRINT-ALL-FMTS           PIC 9(01) VALUE 0.               \n003634     88 PRINT-ALL-FMTS                     VALUE 1.               \n003636 01  RPT499-SW                   PIC 9(01) VALUE 0.               \n003638     88 PRINT-RPT499                       VALUE 1.               \n003640 01  SPECS-OPEN-IND               PIC 9(01) VALUE 0.              \n003642     88  SPECS-OPEN                         VALUE 1.              \n003644 01  WS-BUILD-A-DATE-01.                                          \n003646     05  WS-BUILD-A-DATE          PIC 9(08).                      \n003648     05  WS-BUILD-A-DATE-R REDEFINES WS-BUILD-A-DATE.             \n003650         10  WS-BUILD-A-DATE-CCYY PIC 9(04).                      \n003652         10  WS-BUILD-A-DATE-MM   PIC 9(02).                      \n003654         10  WS-BUILD-A-DATE-DD   PIC 9(02).                      \n003656                                                                  \n003658*=================================================================\n003660*                   PRINTER WORKING-STORAGE                       \n003662*=================================================================\n003664 01  PRINT-LINE                      PIC X(132) VALUE SPACES.     \n003666 01  PRINT-LINE-160                  PIC X(160) VALUE SPACES.     \n003668 01  PRINT-SPACES                    PIC X(132) VALUE SPACES.     \n003670 01  PRINT-SPACES-160                PIC X(160) VALUE SPACES.     \n003672 01  WS-HOLD-LSR-TIN-LINE            PIC X(132) VALUE SPACES.     \n003674 01  WS-HOLD-PRT-TIN-LINE            PIC X(132) VALUE SPACES.     \n003676 01  LISTING-RECORD                  PIC X(132) VALUE SPACES.     \n003678 01  TRIAL-RECORD                    PIC X(132) VALUE SPACES.     \n003680 01  FICHE-RECORD                    PIC X(132) VALUE SPACES.     \n003682 01  NOTICE-RECORD                   PIC X(132) VALUE SPACES.     \n003684 01  STATEMENT-RECORD                PIC X(132) VALUE SPACES.     \n003686 01  TDA-HEADER-LINE6                PIC X(132) VALUE SPACES.     \n003688 01  TDA-HEADER-LINE6-160            PIC X(160) VALUE SPACES.     \n003690 01  WS-BANK-STATE                   PIC XX     VALUE SPACES.     \n003692 01  WS-IN-SUFFIX.                                                \n003694     05  WS-IN-SUFFIX-1              PIC X.                       \n003696     05  WS-IN-SUFFIX-2              PIC X.                       \n003698     05  WS-IN-SUFFIX-3              PIC X.                       \n003700     05  WS-IN-SUFFIX-4              PIC X.                       \n003702 01  WS-READ-APPL-CODE               PIC 9.                       \n003704 01  WS-CONVERSION-CODE              PIC 9     VALUE 0.           \n003706 01  WS-TEAR-PAGE-TYPE               PIC X      VALUE SPACES.     \n003708 01  WK-I                            PIC 9(03) VALUE 0.           \n003710 01  WK-J                            PIC 9(03) VALUE 0.           \n003712 01  WS-REPORT-TYPE                  PIC 9     VALUE 1.           \n003714 01 EOM-INDICATOR-STARTS-EOM-WFL.                                 \n003716    05  EOM-FLAG-STARTS-EOM-WFL                                   \n003718                          PIC X(01)  VALUE SPACES.                \n003720      88 IT-IS-EOM-FLAG-SET          VALUE \"*\".                   \n003722 01 EOM-CALL-MSG.                                                 \n003724    05  FILLER            PIC X(80)  VALUE    \"BEGIN JOB;\".       \n003726    05  FILLER            PIC X(21)  VALUE                        \n003728                                 \"START WFL/TDA/MONTHLY\".         \n003730    05  FILLER            PIC X VALUE \"(\".                        \n003732    05  WS-OP-QT-1        PIC X      VALUE QUOTE.                 \n003734    05  WS-SUFFIX         PIC X(4)   VALUE SPACES.                \n003736    05  WS-SUFFIX-R REDEFINES WS-SUFFIX.                          \n003738        10  WS-SUFFIX-1   PIC X.                                  \n003740        10  WS-SUFFIX-2   PIC X.                                  \n003742        10  WS-SUFFIX-3   PIC X.                                  \n003744        10  WS-SUFFIX-4   PIC X.                                  \n003746    05  WS-CL-QT-1        PIC X      VALUE QUOTE.                 \n003748    05  WS-COMMA          PIC X      VALUE \",\".                   \n003750    05  WS-OP-QT-2        PIC X      VALUE QUOTE.                 \n003752    05  WS-DAY            PIC X(3).                               \n003754    05  WS-CL-QT-2        PIC X      VALUE QUOTE.                 \n003756    05  FILLER            PIC X      VALUE \")\".                   \n003758    05  FILLER            PIC X(01)  VALUE \";\".                   \n003760    05  FILLER            PIC X(44)  VALUE SPACES.                \n003762    05  FILLER            PIC X(80)  VALUE      \"END JOB;\".       \n003764                                                                  \n003766 01  WS-PRINT-REQUEST                PIC X(01) VALUE \"N\".         \n003768     88  PRINT-REPORT                     VALUE \"Y\".              \n003770 01  WS-CARD-REQUEST                 PIC X(01) VALUE SPACE.       \n003772     88  CARD-REQUEST                     VALUE \"Y\".              \n003774 01  WS-LIST-REQUEST                 PIC X(01) VALUE SPACE.       \n003776     88  LIST-REQUEST                     VALUE \"Y\".              \n003778 01  WS-LIST160-REQUEST              PIC X(01) VALUE SPACE.       \n003780     88  LIST160-REQUEST                  VALUE \"Y\".              \n003782 01  WS-CHECK-REQUEST                PIC X(01) VALUE SPACE.       \n003784     88  CHECK-REQUEST                    VALUE \"Y\".              \n003786 01  WS-LSR-CHK-REQUEST              PIC X(01) VALUE SPACE.       \n003788     88  LSR-CHK-REQUEST                  VALUE \"Y\".              \n003790 01  WS-LSR-BANK-REQUEST             PIC X(01) VALUE SPACE.       \n003792     88  LSR-BANK-REQUEST                 VALUE \"Y\".              \n003794 01  WS-G-LSR-BANK-REQUEST           PIC X(01) VALUE SPACE.       \n003796     88  G-LSR-BANK-REQUEST               VALUE \"Y\".              \n003798 01  WS-LASER-STMT-REQUEST           PIC X(01) VALUE SPACE.       \n003800     88  LASER-STMT-REQUEST               VALUE \"Y\".              \n003802 01  WS-LSR-BANK-STMT-REQUEST        PIC X(01) VALUE SPACE.       \n003804     88  LSR-BANK-STMT-REQUEST            VALUE \"Y\".              \n003806 01  WS-FICHE-REQUEST                PIC X(01) VALUE SPACE.       \n003808     88  FICHE-REQUEST                    VALUE \"Y\".              \n003810 01  WS-LASER-REQUEST                PIC X(01) VALUE SPACE.       \n003812     88 LASER-REQUEST                     VALUE \"Y\".              \n003814 01  WS-PP-PLUS-REQUEST              PIC X(01) VALUE SPACE.       \n003816     88 PP-PLUS-REQUEST                   VALUE \"Y\".              \n003818 01  WS-DSI-REQUEST                  PIC X(01) VALUE SPACE.       \n003820     88  DSI-REQUEST                      VALUE \"Y\".              \n003822 01  WS-NOTICE-REQUEST               PIC X(01) VALUE SPACE.       \n003824     88  NOTICE-REQUEST                   VALUE \"Y\".              \n003826 01  WS-TRIAL-FICHE-REQUEST          PIC X(01) VALUE SPACE.       \n003828     88  TRIAL-FICHE-REQUEST              VALUE \"Y\".              \n003830 01  WS-TRIAL-REQUEST                PIC X(01) VALUE SPACE.       \n003832     88  TRIAL-REQUEST                    VALUE \"Y\".              \n003834 01  WS-STATEMENT-REQUEST            PIC X(01) VALUE SPACE.       \n003836     88  STATEMENT-REQUEST                VALUE \"Y\".              \n003838 01  WS-PRT-FREQ                     PIC X(01).                   \n003840     88  DAILY-REPORT                     VALUE \"D\".              \n003842     88  WEEKLY-REPORT                    VALUE \"W\".              \n003844     88  MONTHLY-REPORT                   VALUE \"M\".              \n003846     88  QTR-REPORT                       VALUE \"Q\".              \n003848     88  YEARLY-REPORT                    VALUE \"Y\".              \n003850 01  BANK-OFF-1                      PIC X(01) VALUE SPACES.      \n003852 01  BANK-OFF-2                      PIC X(01) VALUE SPACES.      \n003854 01  WS-REDEFINE-AREA.                                            \n003856     05  WS-PRINT-IND                PIC X(07).                   \n003858     05  WS-PRINT-TODAY-R  REDEFINES WS-PRINT-IND.                \n003860         10  WS-PRINT-TODAY           OCCURS 7 TIMES              \n003862                                     PIC X(01).                   \n003864*=================================================================\n003866 01  WS-CHANGE-N-X.                                               \n003868     05  WK-NUMERIC-1                PIC 9.                       \n003870     05  WK-ALPHA-1 REDEFINES WK-NUMERIC-1                        \n003872                                     PIC X(1).                    \n003874     05  WK-NUMERIC-10               PIC 9(10).                   \n003876     05  WK-ALPHA-10 REDEFINES WK-NUMERIC-10                      \n003878                                     PIC X(10).                   \n003880     05  WK-NUMERIC-12               PIC 9(12).                   \n003882     05  WK-ALPHA-12 REDEFINES WK-NUMERIC-12                      \n003884                                     PIC X(12).                   \n003886 01 WS-BEGIN-DAY                        PIC S9.                   \n003888 01 WS-RPT-READ-DATE                    PIC 9(08).                \n003890 01 WS-PROC-DATE.                                                 \n003892    05  LST-PRC-DT-1                    PIC 9(08).                \n003894    05  LST-PRC-DT-2                    PIC 9(08).                \n003896                                                                  \n003898 01 CODES-REC.                                                    \n003900    05 CODE-DESC                        PIC X(40).                \n003902    05 CODE-NUM                         PIC 9(04).                \n003904                                                                  \n003906 01 DATA-PRESENT-IND                    PIC 9(01) VALUE 0.        \n003908    88 DATA-PRESENT                               VALUE 1.        \n003910                                                                  \n003912 01 SORT-REC-1.                                                   \n003914    05 SORT-KEY-1                       PIC X(52).                \n003916*   this area is used for the acct, totals and reports structures \n003918    05 SORT-DATA-1                      PIC X(2888).              \n003920    05 SORT-REAS-1                      PIC 9(4).                 \n003922                                                                  \n003924 01 SORT-REC-2.                                                   \n003926    05 SORT-KEY-2                       PIC X(80).                \n003928*   this area is used for the acct structure                      \n003930    05 SORT-DATA-21                     PIC X(2376).              \n003932*   this area is used for the cust structure                      \n003934    05 SORT-DATA-22                     PIC X(2064).              \n003936                                                                  \n003938 01  WS-CLOSE-FIELDS.                                             \n003940     05  WS-DDA-ACCT-1               PIC 9(12)       VALUE 0.     \n003942     05  WS-DDA-ACCT-2               PIC 9(12)       VALUE 0.     \n003944     05  WS-DDA-ACCT-3               PIC 9(12)       VALUE 0.     \n003946                                                                  \n```\n\n\u26a0\ufe0f  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.\n    It contains ALL 354 lines from 1616 to 1969.\n\n    You MUST include EVERY line from this code block in your documentation output.\n\n    \ud83d\udea8 COBOL-74 COMMENT PRESERVATION (ABSOLUTELY MANDATORY):\n    ============================================================================\n    COBOL-74 comments are marked with \"*\" in column 7 (after the 6-digit sequence number).\n\n    Example comment lines:\n      000020* This is a comment\n      000026*REMARKS.\n      000028*  SYSTEM    : TDAR\n\n    \u26a0\ufe0f  YOU MUST INCLUDE ALL COMMENT LINES IN YOUR CODE BLOCKS!\n\n    Comments are NOT \"already documented\" - they are SOURCE CODE that must be preserved.\n    Include EVERY comment line (marked with *) verbatim in your ```cobol code blocks.\n\n    DO NOT:\n    - Skip comment lines thinking they don't need documentation\n    - Omit comment blocks (even if they span 100+ lines)\n    - Exclude REMARKS sections, copyright notices, or build information\n    - Remove any line that starts with a * after the sequence number\n\n    DO:\n    - Include EVERY line starting with 000010* through 999999*\n    - Preserve all comment formatting exactly as shown\n    - Show complete comment blocks in their entirety\n    - Treat comments as essential source code content\n    ============================================================================\n\n    **IMPORTANT - Document ALL COBOL Divisions:**\n    - IDENTIFICATION DIVISION: Include program metadata verbatim\n    - ENVIRONMENT DIVISION: Include all FILE-CONTROL entries verbatim\n    - DATA DIVISION: Include ALL data definitions (FD, 01-level, FILLER, etc.) verbatim\n    - PROCEDURE DIVISION: Include all paragraphs with code and explanations\n\n    Do NOT skip:\n    - Data tables (even with thousands of FILLER definitions)\n    - WORKING-STORAGE variables\n    - FILE SECTION record layouts\n    - ANY lines from the source code above\n\n    Each line starts with a 6-digit sequence number (e.g., 003240).\n    Include these sequence numbers in your code blocks to prove coverage.\n",
  "chunk_number": 5,
  "total_chunks": 55,
  "start_line": 1616,
  "end_line": 1969,
  "line_count": 354
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
- Source code length: 29281 characters

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
CHUNK 5 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 1616 to 1969 (354 lines)
Chunk Tokens (estimated): ~6,327
Actual Input Tokens: 7,733 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 1616-1969 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 5 of 55 chunks
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
      The source code below is only CHUNK 5 of 55.


=============================================================================
CHUNK 5 SOURCE CODE (Lines 1616-1969)
=============================================================================

```cobol
003240             Z-DATE-MDY-STRING.
003242             15  Z-DATE-MDY-MM       PIC  9(02).
003244             15  Z-DATE-MDY-DD       PIC  9(02).
003246             15  Z-DATE-MDY-YY       PIC  9(02).
003248         10  Z-DATE-ACCUM            PIC S9(04) BINARY.
003250         10  Z-DATE-MONTH-LIMIT      PIC S9(04) BINARY.
003252     05  Z-DATE-CC-CUTOFF            PIC  9(02) BINARY.
003254     05  Z-DATE-DEFAULT-CC           PIC  9(02) BINARY.
003256     05  Z-DATE-DEFAULT-YY           PIC  9(02) BINARY.
003258     05  Z-DATE-DEFAULT-MM           PIC  9(02) BINARY.
003260     05  Z-DATE-DEFAULT-DD           PIC  9(02) BINARY.
003262     05  Z-DATE-LEAP-YEAR-WA.
003264         10  Z-DATE-FORMAT-YEAR.
003266             15  Z-DATE-FORMAT-CC    PIC  9(02).
003268             15  Z-DATE-FORMAT-YY    PIC  9(02).
003270         10  Z-DATE-FORMAT-CCYY
003272             REDEFINES
003274             Z-DATE-FORMAT-YEAR      PIC  9(04).
003276         10  Z-DATE-YEAR-WORK        PIC S9(04) BINARY.
003278         10  Z-DATE-DIVIDE-WORK      PIC S9(04) BINARY.
003280         10  Z-DATE-QUOTIENT         PIC S9(04) BINARY.
003282         10  Z-DATE-REMAINDER        PIC S9(04) BINARY.
003284         10  Z-DATE-YEAR-MOD-4       PIC S9(04) BINARY.
003286         10  Z-DATE-YEAR-MOD-100     PIC S9(04) BINARY.
003288         10  Z-DATE-YEAR-MOD-400     PIC S9(04) BINARY.
003290         10  Z-DATE-LEAP-YR-FLAG     PIC S9(01) BINARY.
003292             88  Z-DATE-LEAP-YEAR                  VALUE +1.
003294     05  Z-DATE-CONVERT-STATUS-FLAGS.
003296         10  Z-DATE-CONVERT-STATUS   PIC S9(04) BINARY.
003298             88  Z-DATE-CNVRT-SUCCESS              VALUE +0.
003300             88  Z-DATE-CNVRT-UNEXPECTD-FAIL       VALUE -1.
003302             88  Z-DATE-CNVRT-MM-2-MMM-FAIL        VALUE -10.
003304             88  Z-DATE-CNVRT-MM-2-MONTH-FAIL      VALUE -11.
003306             88  Z-DATE-CNVRT-MMM-2-MONTH-FAIL     VALUE -12.
003308             88  Z-DATE-CNVRT-MMM-2-MM-FAIL        VALUE -13.
003310             88  Z-DATE-CNVRT-MONTH-2-MM-FAIL      VALUE -14.
003312             88  Z-DATE-CNVRT-MONTH-2-MMM-FAIL     VALUE -15.
003314             88  Z-DATE-CNVRT-DD-2-DDD-FAIL        VALUE -16.
003316             88  Z-DATE-CNVRT-DD-2-DAY-FAIL        VALUE -17.
003318             88  Z-DATE-CNVRT-DDD-2-DAY-FAIL       VALUE -18.
003320             88  Z-DATE-CNVRT-DDD-2-DD-FAIL        VALUE -19.
003322             88  Z-DATE-CNVRT-DAY-2-DD-FAIL        VALUE -20.
003324             88  Z-DATE-CNVRT-DAY-2-DDD-FAIL       VALUE -21.
003326             88  Z-DATE-CNVRT-UU-2-SS-FAIL         VALUE -22.
003328             88  Z-DATE-CNVRT-SS-2-UU-FAIL         VALUE -23.
003330             88  Z-DATE-CNVRT-UU-2-ZZ-FAIL         VALUE -24.
003332             88  Z-DATE-CNVRT-ZZ-2-DD-FAIL         VALUE -25.
003334     05  Z-DATE-MONTH-TABLE-DATA.
003336         10  FILLER          PIC  X(13) VALUE "01JANUARY  31".
003338         10  FILLER          PIC  X(13) VALUE "02FEBRUARY 28".
003340         10  FILLER          PIC  X(13) VALUE "03MARCH    31".
003342         10  FILLER          PIC  X(13) VALUE "04APRIL    30".
003344         10  FILLER          PIC  X(13) VALUE "05MAY      31".
003346         10  FILLER          PIC  X(13) VALUE "06JUNE     30".
003348         10  FILLER          PIC  X(13) VALUE "07JULY     31".
003350         10  FILLER          PIC  X(13) VALUE "08AUGUST   31".
003352         10  FILLER          PIC  X(13) VALUE "09SEPTEMBER30".
003354         10  FILLER          PIC  X(13) VALUE "10OCTOBER  31".
003356         10  FILLER          PIC  X(13) VALUE "11NOVEMBER 30".
003358         10  FILLER          PIC  X(13) VALUE "12DECEMBER 31".
003360         10  FILLER          PIC  X(13) VALUE "99MMMOVFLOW99".
003362     05  Z-DATE-MONTH-TABLE REDEFINES
003364         Z-DATE-MONTH-TABLE-DATA        OCCURS 13 TIMES
003366                                        INDEXED BY Z-DATE-MM-I.
003368         10  Z-DATE-TBL-MM           PIC  9(02).
003370         10  Z-DATE-TBL-MONTH.
003372             15  Z-DATE-TBL-MMM      PIC  X(03).
003374             15  FILLER              PIC  X(06).
003376         10  Z-DATE-TBL-DAYS-IN-MON  PIC  9(02).
003378     05  Z-DATE0-FORMAT.
003380         10  Z-DATE0-CC              PIC 99.
003382         10  Z-DATE0-YYMMDD.
003384             15  Z-DATE0-YY          PIC 99.
003386             15  Z-DATE0-MM          PIC 99.
003388             15  Z-DATE0-DD          PIC 99.
003390         10  Z-DATE0-YYJJJ.
003392             15  Z-DATE0-YYY         PIC 99.
003394             15  Z-DATE0-JJJ         PIC 999.
003396         10  Z-DATE0-TIME.
003398             15  Z-DATE0-ZZ          PIC 99.
003400             15  Z-DATE0-UU          PIC 99.
003402             15  Z-DATE0-SS          PIC 99.
003404             15  Z-DATE0-TT          PIC 99.
003406     05  Z-DATE1-FORMAT.
003408         10  Z-DATE1-CC              PIC 99.
003410         10  Z-DATE1-YY              PIC 99.
003412         10  Z-DATE1-JJJ             PIC 999.
003414         10  Z-DATE1-ZZ              PIC 99.
003416         10  Z-DATE1-UU              PIC 99.
003418         10  Z-DATE1-SS              PIC 99.
003420         10  Z-DATE1-TT              PIC 99.
003422     05  Z-DATE1-FORMAT-9 REDEFINES Z-DATE1-FORMAT
003424                                     PIC 9(15).
003426     05  Z-DATE2-FORMAT.
003428         10  Z-DATE2-CC              PIC 99.
003430         10  Z-DATE2-YY              PIC 99.
003432         10  Z-DATE2-MM              PIC 99.
003434         10  Z-DATE2-DD              PIC 99.
003436     05  Z-DATE2-FORMAT-9 REDEFINES Z-DATE2-FORMAT
003438                                     PIC 9(8).
003440     05  Z-DATE3-FORMAT.
003442         10  Z-DATE3-MM              PIC 99.
003444         10  Z-DATE3-DD              PIC 99.
003446         10  Z-DATE3-YY              PIC 99.
003448     05  Z-DATE3-FORMAT-9 REDEFINES Z-DATE3-FORMAT
003450                                     PIC 9(6).
003452     05  Z-DATE4-FORMAT.
003454         10  Z-DATE4-ZZ              PIC 99.
003456         10  Z-DATE4-UU              PIC 99.
003458     05  Z-DATE4-FORMAT-9 REDEFINES Z-DATE4-FORMAT
003460                                     PIC 9(4).
003462     05  Z-DATE5-FORMAT.
003464         10  Z-DATE5-DD              PIC 99.
003466     05  Z-DATE5-FORMAT-9 REDEFINES Z-DATE5-FORMAT
003468                                     PIC 9(2).
003470     05  Z-DATE6-FORMAT.
003472         10  Z-DATE6-MM              PIC 99.
003474         10  Z-DATE6-CH1             PIC X.
003476         10  Z-DATE6-DD              PIC 99.
003478         10  Z-DATE6-CH2             PIC X.
003480         10  Z-DATE6-CC              PIC 99.
003482         10  Z-DATE6-YY              PIC 99.
003484     05  Z-DATE7-FORMAT.
003486         10  Z-DATE7-MM              PIC 99.
003488         10  Z-DATE7-DD              PIC 99.
003490     05  Z-DATE7-FORMAT-9 REDEFINES Z-DATE7-FORMAT
003492                                     PIC 9(4).
003494     05  Z-RESTART-BY-COUNT-LIMIT      PIC S9(8) VALUE 100.
003496     05  Z-RESTART-FOR-COUNT-LIMIT     PIC S9(8) VALUE 100.
003498     05  Z-CUSTOM-VALUED               PIC X.
003500*
003502**** FILE EXCEPTION
003504*
003506 01  Z-FL-EXCEPT-TITLE                 PIC X(200) VALUE SPACES.
003508 01  Z-FL-EXCEPT-MSG.
003510     05  Z-FL-EXCEPT-ERR                PIC X(27).
003512     05  Z-FL-EXCEPT-LIT-PARN           PIC X.
003514     05  Z-FL-EXCEPT-STATUS             PIC X(2).
003516         88  Z-FILE-EOF                           VALUE "10".
003518         88  Z-FILE-DUPLICATES                    VALUE "22".
003520         88  Z-FILE-NOTFOUND                      VALUE "23".
003522         88  Z-FILE-BOUNDARY                      VALUE "24".
003524     05  Z-FL-EXCEPT-LIT-ON             PIC X(10).
003526     05  Z-FL-EXCEPT-FILE               PIC X(30).
003528     05  Z-FL-EXCEPT-LIT-AT             PIC X(4).
003530     05  Z-FL-EXCEPT-SEQ                PIC 9(6).
003532*
003534**** DATABASE EXCEPTION
003536*
003538 01  Z-DMS-EXCEPT-MSG.
003540     05  Z-DMS-EXCEPT-LIT-DMS                   PIC X(4).
003542     05  Z-DMS-EXCEPT-CAT.
003544         10  FILLER                             PIC X(11).
003546         10  Z-DMS-EXCEPT-CAT-NO                PIC 9(2).
003548         10  FILLER                             PIC X(7).
003550     05  Z-DMS-EXCEPT-LIT-SUBCAT                PIC X(9).
003552     05  Z-DMS-EXCEPT-SUBCAT                    PIC 9(3).
003554     05  Z-DMS-EXCEPT-LIT-AT                    PIC X(5).
003556     05  Z-DMS-EXCEPT-SEQ                       PIC 9(6).
003558     05  Z-DMS-EXCEPT-LIT-ON                    PIC X(4).
003560     05  Z-DMS-EXCEPT-STR                       PIC X(18).
003562     05  Z-DMS-EXCEPT-LIT-OF                    PIC X(4).
003564     05  Z-DMS-EXCEPT-DB                        PIC X(18).
003566*
003568**** SAVE RECORD
003570*
003572 01  Z-SAVE-REC.
003574     05  FILLER                                 PIC X(1677).
003576*
003578 01  Z-SAVE-REC-FLAG                    PIC 9 VALUE 0.
003580*
003582****** USER AREA ******
003584 01  SWT-1                       PIC 9(01) VALUE 0.               
003586     88 SW1-0                              VALUE 0.               
003588     88 SW1-1                              VALUE 1.               
003590 01  SWT-2                       PIC 9(01) VALUE 0.               
003592     88 SW2-0                              VALUE 0.               
003594     88 SW2-1                              VALUE 1.               
003596 01  SWT-3                       PIC 9(01) VALUE 0.               
003598     88 SW3-0                              VALUE 0.               
003600     88 SW3-1                              VALUE 1.               
003602 01  SWT-4                       PIC 9(01) VALUE 0.               
003604     88 SW4-0                              VALUE 0.               
003606     88 SW4-1                              VALUE 1.               
003608 01  SWT-5                       PIC 9(01) VALUE 0.               
003610     88 SW5-0                              VALUE 0.               
003612     88 SW5-1                              VALUE 1.               
003614 01  SWT-6                       PIC 9(01) VALUE 0.               
003616     88 SW6-0                              VALUE 0.               
003618     88 SW6-1                              VALUE 1.               
003620 01  SWT-7                       PIC 9(01) VALUE 0.               
003622     88 SW7-0                              VALUE 0.               
003624     88 SW7-1                              VALUE 1.               
003626 01  SWT-8                       PIC 9(01) VALUE 0.               
003628     88 SW8-0                              VALUE 0.               
003630     88 SW8-1                              VALUE 1.               
003632 01  WS-PRINT-ALL-FMTS           PIC 9(01) VALUE 0.               
003634     88 PRINT-ALL-FMTS                     VALUE 1.               
003636 01  RPT499-SW                   PIC 9(01) VALUE 0.               
003638     88 PRINT-RPT499                       VALUE 1.               
003640 01  SPECS-OPEN-IND               PIC 9(01) VALUE 0.              
003642     88  SPECS-OPEN                         VALUE 1.              
003644 01  WS-BUILD-A-DATE-01.                                          
003646     05  WS-BUILD-A-DATE          PIC 9(08).                      
003648     05  WS-BUILD-A-DATE-R REDEFINES WS-BUILD-A-DATE.             
003650         10  WS-BUILD-A-DATE-CCYY PIC 9(04).                      
003652         10  WS-BUILD-A-DATE-MM   PIC 9(02).                      
003654         10  WS-BUILD-A-DATE-DD   PIC 9(02).                      
003656                                                                  
003658*=================================================================
003660*                   PRINTER WORKING-STORAGE                       
003662*=================================================================
003664 01  PRINT-LINE                      PIC X(132) VALUE SPACES.     
003666 01  PRINT-LINE-160                  PIC X(160) VALUE SPACES.     
003668 01  PRINT-SPACES                    PIC X(132) VALUE SPACES.     
003670 01  PRINT-SPACES-160                PIC X(160) VALUE SPACES.     
003672 01  WS-HOLD-LSR-TIN-LINE            PIC X(132) VALUE SPACES.     
003674 01  WS-HOLD-PRT-TIN-LINE            PIC X(132) VALUE SPACES.     
003676 01  LISTING-RECORD                  PIC X(132) VALUE SPACES.     
003678 01  TRIAL-RECORD                    PIC X(132) VALUE SPACES.     
003680 01  FICHE-RECORD                    PIC X(132) VALUE SPACES.     
003682 01  NOTICE-RECORD                   PIC X(132) VALUE SPACES.     
003684 01  STATEMENT-RECORD                PIC X(132) VALUE SPACES.     
003686 01  TDA-HEADER-LINE6                PIC X(132) VALUE SPACES.     
003688 01  TDA-HEADER-LINE6-160            PIC X(160) VALUE SPACES.     
003690 01  WS-BANK-STATE                   PIC XX     VALUE SPACES.     
003692 01  WS-IN-SUFFIX.                                                
003694     05  WS-IN-SUFFIX-1              PIC X.                       
003696     05  WS-IN-SUFFIX-2              PIC X.                       
003698     05  WS-IN-SUFFIX-3              PIC X.                       
003700     05  WS-IN-SUFFIX-4              PIC X.                       
003702 01  WS-READ-APPL-CODE               PIC 9.                       
003704 01  WS-CONVERSION-CODE              PIC 9     VALUE 0.           
003706 01  WS-TEAR-PAGE-TYPE               PIC X      VALUE SPACES.     
003708 01  WK-I                            PIC 9(03) VALUE 0.           
003710 01  WK-J                            PIC 9(03) VALUE 0.           
003712 01  WS-REPORT-TYPE                  PIC 9     VALUE 1.           
003714 01 EOM-INDICATOR-STARTS-EOM-WFL.                                 
003716    05  EOM-FLAG-STARTS-EOM-WFL                                   
003718                          PIC X(01)  VALUE SPACES.                
003720      88 IT-IS-EOM-FLAG-SET          VALUE "*".                   
003722 01 EOM-CALL-MSG.                                                 
003724    05  FILLER            PIC X(80)  VALUE    "BEGIN JOB;".       
003726    05  FILLER            PIC X(21)  VALUE                        
003728                                 "START WFL/TDA/MONTHLY".         
003730    05  FILLER            PIC X VALUE "(".                        
003732    05  WS-OP-QT-1        PIC X      VALUE QUOTE.                 
003734    05  WS-SUFFIX         PIC X(4)   VALUE SPACES.                
003736    05  WS-SUFFIX-R REDEFINES WS-SUFFIX.                          
003738        10  WS-SUFFIX-1   PIC X.                                  
003740        10  WS-SUFFIX-2   PIC X.                                  
003742        10  WS-SUFFIX-3   PIC X.                                  
003744        10  WS-SUFFIX-4   PIC X.                                  
003746    05  WS-CL-QT-1        PIC X      VALUE QUOTE.                 
003748    05  WS-COMMA          PIC X      VALUE ",".                   
003750    05  WS-OP-QT-2        PIC X      VALUE QUOTE.                 
003752    05  WS-DAY            PIC X(3).                               
003754    05  WS-CL-QT-2        PIC X      VALUE QUOTE.                 
003756    05  FILLER            PIC X      VALUE ")".                   
003758    05  FILLER            PIC X(01)  VALUE ";".                   
003760    05  FILLER            PIC X(44)  VALUE SPACES.                
003762    05  FILLER            PIC X(80)  VALUE      "END JOB;".       
003764                                                                  
003766 01  WS-PRINT-REQUEST                PIC X(01) VALUE "N".         
003768     88  PRINT-REPORT                     VALUE "Y".              
003770 01  WS-CARD-REQUEST                 PIC X(01) VALUE SPACE.       
003772     88  CARD-REQUEST                     VALUE "Y".              
003774 01  WS-LIST-REQUEST                 PIC X(01) VALUE SPACE.       
003776     88  LIST-REQUEST                     VALUE "Y".              
003778 01  WS-LIST160-REQUEST              PIC X(01) VALUE SPACE.       
003780     88  LIST160-REQUEST                  VALUE "Y".              
003782 01  WS-CHECK-REQUEST                PIC X(01) VALUE SPACE.       
003784     88  CHECK-REQUEST                    VALUE "Y".              
003786 01  WS-LSR-CHK-REQUEST              PIC X(01) VALUE SPACE.       
003788     88  LSR-CHK-REQUEST                  VALUE "Y".              
003790 01  WS-LSR-BANK-REQUEST             PIC X(01) VALUE SPACE.       
003792     88  LSR-BANK-REQUEST                 VALUE "Y".              
003794 01  WS-G-LSR-BANK-REQUEST           PIC X(01) VALUE SPACE.       
003796     88  G-LSR-BANK-REQUEST               VALUE "Y".              
003798 01  WS-LASER-STMT-REQUEST           PIC X(01) VALUE SPACE.       
003800     88  LASER-STMT-REQUEST               VALUE "Y".              
003802 01  WS-LSR-BANK-STMT-REQUEST        PIC X(01) VALUE SPACE.       
003804     88  LSR-BANK-STMT-REQUEST            VALUE "Y".              
003806 01  WS-FICHE-REQUEST                PIC X(01) VALUE SPACE.       
003808     88  FICHE-REQUEST                    VALUE "Y".              
003810 01  WS-LASER-REQUEST                PIC X(01) VALUE SPACE.       
003812     88 LASER-REQUEST                     VALUE "Y".              
003814 01  WS-PP-PLUS-REQUEST              PIC X(01) VALUE SPACE.       
003816     88 PP-PLUS-REQUEST                   VALUE "Y".              
003818 01  WS-DSI-REQUEST                  PIC X(01) VALUE SPACE.       
003820     88  DSI-REQUEST                      VALUE "Y".              
003822 01  WS-NOTICE-REQUEST               PIC X(01) VALUE SPACE.       
003824     88  NOTICE-REQUEST                   VALUE "Y".              
003826 01  WS-TRIAL-FICHE-REQUEST          PIC X(01) VALUE SPACE.       
003828     88  TRIAL-FICHE-REQUEST              VALUE "Y".              
003830 01  WS-TRIAL-REQUEST                PIC X(01) VALUE SPACE.       
003832     88  TRIAL-REQUEST                    VALUE "Y".              
003834 01  WS-STATEMENT-REQUEST            PIC X(01) VALUE SPACE.       
003836     88  STATEMENT-REQUEST                VALUE "Y".              
003838 01  WS-PRT-FREQ                     PIC X(01).                   
003840     88  DAILY-REPORT                     VALUE "D".              
003842     88  WEEKLY-REPORT                    VALUE "W".              
003844     88  MONTHLY-REPORT                   VALUE "M".              
003846     88  QTR-REPORT                       VALUE "Q".              
003848     88  YEARLY-REPORT                    VALUE "Y".              
003850 01  BANK-OFF-1                      PIC X(01) VALUE SPACES.      
003852 01  BANK-OFF-2                      PIC X(01) VALUE SPACES.      
003854 01  WS-REDEFINE-AREA.                                            
003856     05  WS-PRINT-IND                PIC X(07).                   
003858     05  WS-PRINT-TODAY-R  REDEFINES WS-PRINT-IND.                
003860         10  WS-PRINT-TODAY           OCCURS 7 TIMES              
003862                                     PIC X(01).                   
003864*=================================================================
003866 01  WS-CHANGE-N-X.                                               
003868     05  WK-NUMERIC-1                PIC 9.                       
003870     05  WK-ALPHA-1 REDEFINES WK-NUMERIC-1                        
003872                                     PIC X(1).                    
003874     05  WK-NUMERIC-10               PIC 9(10).                   
003876     05  WK-ALPHA-10 REDEFINES WK-NUMERIC-10                      
003878                                     PIC X(10).                   
003880     05  WK-NUMERIC-12               PIC 9(12).                   
003882     05  WK-ALPHA-12 REDEFINES WK-NUMERIC-12                      
003884                                     PIC X(12).                   
003886 01 WS-BEGIN-DAY                        PIC S9.                   
003888 01 WS-RPT-READ-DATE                    PIC 9(08).                
003890 01 WS-PROC-DATE.                                                 
003892    05  LST-PRC-DT-1                    PIC 9(08).                
003894    05  LST-PRC-DT-2                    PIC 9(08).                
003896                                                                  
003898 01 CODES-REC.                                                    
003900    05 CODE-DESC                        PIC X(40).                
003902    05 CODE-NUM                         PIC 9(04).                
003904                                                                  
003906 01 DATA-PRESENT-IND                    PIC 9(01) VALUE 0.        
003908    88 DATA-PRESENT                               VALUE 1.        
003910                                                                  
003912 01 SORT-REC-1.                                                   
003914    05 SORT-KEY-1                       PIC X(52).                
003916*   this area is used for the acct, totals and reports structures 
003918    05 SORT-DATA-1                      PIC X(2888).              
003920    05 SORT-REAS-1                      PIC 9(4).                 
003922                                                                  
003924 01 SORT-REC-2.                                                   
003926    05 SORT-KEY-2                       PIC X(80).                
003928*   this area is used for the acct structure                      
003930    05 SORT-DATA-21                     PIC X(2376).              
003932*   this area is used for the cust structure                      
003934    05 SORT-DATA-22                     PIC X(2064).              
003936                                                                  
003938 01  WS-CLOSE-FIELDS.                                             
003940     05  WS-DDA-ACCT-1               PIC 9(12)       VALUE 0.     
003942     05  WS-DDA-ACCT-2               PIC 9(12)       VALUE 0.     
003944     05  WS-DDA-ACCT-3               PIC 9(12)       VALUE 0.     
003946                                                                  
```

⚠️  CRITICAL: The source code above (within the ```cobol code block) is what you MUST document.
    It contains ALL 354 lines from 1616 to 1969.

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

