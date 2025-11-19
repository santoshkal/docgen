# LLM Request Debug File
Generated: 2025-11-17T19:50:51.582802

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 1/55
- **Model**: gpt-4.1
- **Chunk Number**: 1
- **Pass Number**: 3
- **Attempt Number**: 3 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~9,290 tokens
- **Total Input**: ~11,248 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 1/55" (ID: detailed-code-explanation)

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


**CHUNK 1 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-17T19:50:50.832678", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 1 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 1 to 484 (484 lines)\nChunk Tokens (estimated): ~7,935\nActual Input Tokens: 9,341 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 1-484 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 1 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 1 of 55.\n\n\n=============================================================================\nCHUNK 1 SOURCE CODE (Lines 1-484)\n=============================================================================\n\n```cobol\n000010$ RESET LIST SET LINEINFO ERRORLIST\n000012$ SET AUTOINSERT\n000014 IDENTIFICATION DIVISION.\n000016 PROGRAM-ID.    MINDISTCALC.\n000018 AUTHOR.        \"XGEN Generator -- Version 45A.001 (Sep-10-12)\".\n000020* Build ID: 1.16 (Tue Mar 12 09:22:26 EDT 2013)\n000022 DATE-WRITTEN. 10-Apr-2024 17:36:53.\n000024 DATE-COMPILED.\n000026*REMARKS.\n000028*  SYSTEM    : TDAR\n000030*  XGEN FILE : TDA/XGEN/mindistcalc.xgn\n000032*  SRC FILE  : TDAR/SOURCE/TDAS-MINDISTCALC.c74\n000034*  OBJ FILE  : TDAR/SOURCE/MINDISTCALC\n000036*  COMPILER  : COBOL74\n000038*  REPORTS   :\n000040*     RMDRPT2             RMDRPT\n000042*  END OF REPORTS\n000044*\n000046*  COPY FILES  :\n000048*    X:\\DEV\\\n000050*         TDA/LIB/EOYTEARPAGE.XLIB\n000052*         TDA/LIB/XGEN-PRINT-ROUTINES.XLIB\n000054*         TDA/LIB/RMD-LEF-TBL.XLIB\n000056*         TDA/LIB/GENLCOPY.XLIB\n000058*         TDA/LIB/ACH.XLIB\n000060*         TDA/LIB/GENLCOPY.XLIB\n000062*         TDA/LIB/RPTWRK.XLIB\n000064*    \n000066*         TDA/LIB/REPORTS.XLIB\n000068*         TDA/LIB/REPORTS.XLIB\n000070*         TDA/LIB/REPORTS.XLIB\n000072*         TDA/LIB/REPORTS.XLIB\n000074*         TDA/LIB/REPORTS.XLIB\n000076*         TDA/LIB/REPORTS.XLIB\n000078*         TDA/LIB/REPORTS.XLIB\n000080*         TDA/LIB/REPORTS.XLIB\n000082*         TDA/LIB/REPORTS.XLIB\n000084*         TDA/LIB/REPORTS.XLIB\n000086*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000088*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000090*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000092*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000094*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000096*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000098*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000100*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000102*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000104*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000106*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000108*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000110*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000112*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000114*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000116*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000118*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000120*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000122*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000124*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000126*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000128*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000130*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000132*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000134*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000136*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000138*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000140*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000142*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000144*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000146*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000148*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000150*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000152*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000154*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000156*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000158*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000160*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000162*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000164*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000166*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000168*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000170*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000172*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000174*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB\n000176*         TDA/LIB/COPYGENLCOPY.XLIB\n000178*  END OF COPY FILES\n000180*END OF REMARKS.\n000182*\n000184*****************************************************************\n000186******************************************************************\n000188*                Proprietary Software Material                   *\n000190* This material is proprietary to Computer Services, Inc.and is  *\n000192* not to be reproduced, used or disclosed except in accordance   *\n000194* with software license or upon written authorization of:        *\n000196*     Computer Services, Inc.                                    *\n000198*     3901 Technology Drive Paducah, KY 42001                    *\n000200******************************************************************\n000202*COMPUTER SERVICES A SERIES OPERATING INSTRUCTIONS               H\n000204*                                                                O\n000206* PROGRAM NAME             RUN FREQUENCY                DATE     H\n000208* ----------------------  --------------            ------------ O\n000210* ! TDA/MINDISTCALC    !  ! AS NEEDED  !            !          ! D\n000212* ----------------------  --------------            ------------ O\n000214*                                                     APPROVED   H\n000216*                                                   ------------ O\n000218* PROGRAM NARRATIVE OR DESCRIPTION                  !          ! H\n000220*                                                   ------------ O\n000222* -------------------------------------------------------------- O\n000224* !              MINIMUM DISTRIBUTION CALCULATION              ! O\n000226* !                                                            ! O\n000228* ! THIS PROGRAM CALCULATES THE REQUIRED MINIMUM DISTRIBUTION  ! O\n000230* ! FOR IRA ACCOUNTS WHOSE CUSTOMERS ARE AT RMD AGE SET BY THE ! O\n000232* ! THE IRS. REPORT IS GENERATED TO SHOW RESULTS OF            ! O\n000234* ! CALCULATION.                                               ! O\n000236* !                                                            ! O\n000238* !                                                            ! O\n000240* ! UPLOAD FILE IS CREATED TO UPDATE THE MINIMUM DISTRIBUTION  ! O\n000242* ! IF THE PCR AND ACCOUNT ARE SET TO ACCEPT THE F/M.  A       ! O\n000244* ! SEPARATE UPLOAD FILE IS ALSO CREATED IF OPTION 3 (ALL      ! O\n000246* ! BANKS) IS SELECTED.  THIS FILE UPDATES THE RMD ON BOTH THE ! O\n000248* ! CUSTOMER AND ACCOUNT RECORDS.                              ! O\n000250* !                                                            ! O\n000252* !                                                            ! O\n000254* ! INPUT FILES:                                               ! O\n000256* !    PROC-FILE  :  TDA/DAILY/ddd ON GENERAL                  ! O\n000258* !                  ddd = DAY OF WK (MON, TUE, WED, THU, FRI) ! O\n000260* !                                                            ! O\n000262* !    BK-SPEC-FILE  :  SPECS/BANK/NEW                         ! O\n000264* !                                                            ! O\n000266* ! OUTPUT FILES:                                              ! O\n000268* !    RMDRPT (FOR NON-INHERITED IRA'S):                       ! O\n000270* !             PRINT/cc/TDA/00SP/bbbb/xxxx/ddNSP700 ON GENERAL! O\n000272* !               cc   = DATA CENTER                           ! O\n000274* !               bbbb = BANK                                  ! O\n000276* !               xxxx = SERVER INDICATORS                     ! O\n000278* !               dd   = DAY (01 - 31)                         ! O\n000280* !                                                            ! O\n000282* !    RMDRPT2 (FOR INHERITED IRA'S):                          ! O\n000284* !             PRINT/cc/TDA/00SP/bbbb/xxxx/ddNSP701 ON GENERAL! O\n000286* !               cc   = DATA CENTER                           ! O\n000288* !               bbbb = BANK                                  ! O\n000290* !               xxxx = SERVER INDICATORS                     ! O\n000292* !               dd   = DAY (01 - 31)                         ! O\n000294* !                                                            ! O\n000296* !    MASS FILE MAINT:                                        ! O\n000298* !       'DST' FILES ARE AUTO DISTRIBUTION FM RECORDS         ! O\n000300* !       'CST' FILES ARE CUSTOMER/ACCOUNT FM RECORDS          ! O\n000302* !                                                            ! O\n000304* !       SINGLE BANK:    RIN0D/TDA/mmdd/bbb/RMDDST ON RMT     ! O\n000306* !                       RIN0D/TDA/mmdd/bbb/RMDCST ON RMT     ! O\n000308* !                         mmdd = MONTH/DAY                   ! O\n000310* !                         bbb  = BANK                        ! O\n000312* !                                                            ! O\n000314* !       LIST OF BANKS: RIN0D/TDA/mmdd/000/RMDDSThhmm ON RMT  ! O\n000316* !                      RIN0D/TDA/mmdd/000/RMDCSThhmm ON RMT  ! O\n000318* !                        mmdd = MONTH/DAY                    ! O\n000320* !                        hhmm = HOUR/MIN                     ! O\n000322* !                                                            ! O\n000324* !       ALL BANKS:     RIN0D/TDA/mmdd/000/RMDDSTs ON RMT     ! O\n000326* !                      RIN0D/TDA/mmdd/000/RMDCSTs ON RMT     ! O\n000328* !                        mmdd = MONTH/DAY                    ! O\n000330* !                        s    = TDA SUFFIX                   ! O\n000332* !                                                            ! O\n000334* !              - - - - - - - - - - - - - - -                 ! O\n000336* !                                                            ! O\n000338* ! PROGRAM FLOW:                                              ! O\n000340* !                                                            ! O\n000342* ! -> ENTER BANK OPTION                                       ! O\n000344* !    1 - ONE BANK                                            ! O\n000346* !    2 - LIST OF BANKS                                       ! O\n000348* !    3 - ALL BANKS (USES PROC-FILE)                          ! O\n000350* !                                                            ! O\n000352* ! -> CONFIRM BANK OPTION (Y/N)                               ! O\n000354* !                                                            ! O\n000356* ! IF ONE BANK:                                               ! O\n000358* !                                                            ! O\n000360* !    -> ENTER BANK NUMBER (4-DIGIT)                          ! O\n000362* !                                                            ! O\n000364* ! IF LIST OF BANKS:                                          ! O\n000366* !                                                            ! O\n000368* !    -> ENTER LIST (000100020003...) MAX 20 BANKS            ! O\n000370* !                                                            ! O\n000372* -------------------------------------------------------------- O\n000374*                                                                O\n000376* DATE CONTROL :  MCP               OTHER   XXX                  O\n000378*                          -----           -----                 O\n000380*  ENTER VIA      CONSOLE                   N/A                  O\n000382*                          -----           --------------------- O\n000384* FILE DATA                                                      H\n000386*                                                                F\n000388* SPECIAL FEATURES                                               H\n000390*                                                                O\n000392* -------------------------------------------------------------- S\n000394* ! SW3 - BYPASS RMD REPORT CREATION                           ! O\n000396* !       RMD REPORTS WILL NOT BE CREATED WHEN SW3 SET         ! O\n000398* -------------------------------------------------------------- O\n000400/                                                                 \n000402*****************************************************************\n000404*\n000406*****************************************************************\n000408 ENVIRONMENT DIVISION.\n000410*****************************************************************\n000412 CONFIGURATION SECTION.\n000414*------------- -------\n000416 SOURCE-COMPUTER. UNISYS-A-SERIES.\n000418 OBJECT-COMPUTER. UNISYS-A-SERIES\n000420     SEGMENT-LIMIT IS 25 .\n000422*\n000424 SPECIAL-NAMES.\n000426     SW1 ON IS Z-SW1\n000428     SW2 ON IS Z-SW2\n000430     SW3 ON IS Z-SW3\n000432     SW4 ON IS Z-SW4\n000434     SW5 ON IS Z-SW5\n000436     SW6 ON IS Z-SW6\n000438     SW7 ON IS Z-SW7\n000440     SW8 ON IS Z-SW8.\n000442 INPUT-OUTPUT SECTION.\n000444*------------ -------\n000446 FILE-CONTROL.\n000448*------------\n000450*\n000452     SELECT BK-SPEC-FILE\n000454         ASSIGN TO DISK\n000456         ORGANIZATION IS SEQUENTIAL\n000458         ACCESS IS SEQUENTIAL\n000460         ACTUAL KEY IS Z-FILE3-KEY\n000462         FILE STATUS IS Z-FLINFO3-STATUS.\n000464*\n000466     SELECT PROC-FILE\n000468         ASSIGN TO DISK\n000470         ORGANIZATION IS SEQUENTIAL\n000472         ACCESS IS SEQUENTIAL\n000474         ACTUAL KEY IS Z-FILE4-KEY\n000476         FILE STATUS IS Z-FLINFO4-STATUS.\n000478*\n000480     SELECT DST-FILE-MAINT\n000482         ASSIGN TO DISK\n000484         ORGANIZATION IS SEQUENTIAL\n000486         ACCESS IS SEQUENTIAL\n000488         ACTUAL KEY IS Z-FILE5-KEY\n000490         FILE STATUS IS Z-FLINFO5-STATUS.\n000492*\n000494     SELECT CST-FILE-MAINT\n000496         ASSIGN TO DISK\n000498         ORGANIZATION IS SEQUENTIAL\n000500         ACCESS IS SEQUENTIAL\n000502         ACTUAL KEY IS Z-FILE6-KEY\n000504         FILE STATUS IS Z-FLINFO6-STATUS.\n000506*\n000508     SELECT LISTING\n000510         ASSIGN TO PRINTER.\n000512*\n000514     SELECT FICHE\n000516         ASSIGN TO PRINTER.\n000518*\n000520*****************************************************************\n000522 DATA DIVISION.\n000524*****************************************************************\n000526*\n000528 FILE SECTION.\n000530*---- -------\n000532*\n000534* FILE DESCRIPTION FOR BK-SPEC-FILE ( 82 BYTES )\n000536*\n000538 FD  BK-SPEC-FILE\n000540     VALUE OF TITLE IS \"SPECS/BANK/NEW\"\n000542     VALUE OF DEPENDENTSPECS IS TRUE.\n000544*\n000546 01  SPEC-RECORD-N                       PIC X(82).               \n000548*\n000550 01  SPEC-CARD-1-N.                                               \n000552     05  SPEC-BK-NO-N                    PIC X(04).               \n000554     05  SPEC-BK-NO-R REDEFINES SPEC-BK-NO-N.                     \n000556         10  FILLER                      PIC 9(01).               \n000558         10  SPEC-BK-NO-LST-3-N.                                  \n000560             15  SPEC-BK-NO-9-N          PIC 9(03).               \n000562     05  SPEC-BK-NO-R1 REDEFINES SPEC-BK-NO-N.                    \n000564         10 SPEC-BK-NO-9-4-N             PIC 9(04).               \n000566     05  SPEC-BR-CODE-MSD-N              PIC 9(01).               \n000568     05  SPEC-SEQ-NO-N                   PIC 9(02).               \n000570     05  SPEC-FILE-ID-VERSION-N.                                  \n000572         10  SPEC-FILE-ID-N              PIC X(03).               \n000574         10  SPEC-FILE-VERSION-N         PIC X(03).               \n000576     05  SPEC-BK-NAME-N                  PIC X(30).               \n000578     05  SPEC-REND-SITE-N                PIC 9(02).               \n000580     05  SPEC-MAIL-CENTER-N              PIC 9(02).               \n000582     05  SPEC-TIMEZONE-N                 PIC X(01).               \n000584     05  SPEC-PP-MICR-PRT-N              PIC X(01).               \n000586     05  FILLER                          PIC X(01).               \n000588     05  SPEC-DQVISTA-N                  PIC X(01).               \n000590     05  SPEC-MSI-N                      PIC X(01).               \n000592     05  SPEC-CENTERVIEW-N               PIC X(01).               \n000594     05  SPEC-FDIC-UNINSURE-N            PIC X(01).               \n000596     05  SPEC-OFAC-FREQ-N                PIC X(01).               \n000598     05  SPEC-OFAC-FREQ-MONTH-N          PIC X(01).               \n000600     05  SPEC-CBI-LNS-TICKLER-N          PIC X(01).               \n000602     05  SPEC-PRIV-EXCLUDE-CUST-N        PIC 9(01).               \n000604     05  SPEC-MULTI-CUT-OPTION-N         PIC 9(01).               \n000606     05  SPEC-PRIV-NTC-BUSINESS-N        PIC X(01).               \n000608     05  SPEC-PRIV-NTC-DNM-N             PIC X(01).               \n000610     05  SPEC-PRIV-NTC-MAIL-MONTH-N      PIC 9(02).               \n000612     05  SPEC-PRIV-NTC-OUTPUT-FMT-N      PIC 9(01).               \n000614     05  SPEC-PRIV-LABELS-TYPE-N         PIC 9(01).               \n000616     05  SPEC-PRIV-NTC-APPLS-N           PIC 9(04).               \n000618     05  SPEC-PRIV-PP-PLUS-N             PIC X(01).               \n000620     05  SPEC-PRIV-NTC-REL-CDS-N         PIC X(01).               \n000622     05  SPEC-WEB-ENABLED-N              PIC X(01).               \n000624     05  SPEC-NEW-MCIF-SYS-N             PIC X(01).               \n000626     05  SPEC-BK-IMG-SITE-N              PIC X(01).               \n000628     05  SPEC-BK-IMG-SERV-N              PIC X(01).               \n000630     05  SPEC-BK-STATUS-N                PIC X(01).               \n000632     05  SPEC-BK-TDA-STAT-N              PIC X(01).               \n000634     05  SPEC-HOLDING-CO-N               PIC X(01).               \n000636     05  SPEC-NEW-ACH-N                  PIC 9(01).               \n000638     05  SPEC-CSI-HOST-N                 PIC 9(02).               \n000640     05  FILLER-UNAVAIL-01               PIC X(01).               \n000642*\n000644 01  SPEC-CARD-2-N.                                               \n000646     03  SPEC-BK-DATA-N.                                          \n000648         05  FILLER                      PIC X(07).               \n000650         05  SPEC-BR-NO-N                PIC X(02).               \n000652         05  SPEC-GL-NO-N.                                        \n000654             10  SPEC-GL-NO-LST-2-N      PIC X(03).               \n000656         05  SPEC-GL-NO-9-N              REDEFINES                \n000658                                         SPEC-GL-NO-N             \n000660                                         PIC 9(03).               \n000662         05  SPEC-MERGE-FLAG-N           PIC 9(01).               \n000664         05  SPEC-ACCT-LENGTH-N          PIC X(01).               \n000666         05  SPEC-EIS-FILES-N            PIC 9(01).               \n000668         05  SPEC-FINCEN-PULL-N          PIC 9(01).               \n000670         05  SPEC-NEW-GL-N               PIC X(01).               \n000672         05  SPEC-BK-REP-N               PIC X(03).               \n000674         05  SPEC-BK-PHONE-NUM-N.                                 \n000676             10  SPEC-AREA-CODE-N        PIC X(03).               \n000678             10  SPEC-PHONE-N.                                    \n000680                 15  SPEC-PHONE-1ST-3-N  PIC X(03).               \n000682                 15  SPEC-PHONE-LST-4-N  PIC X(04).               \n000684         05  SPEC-NOR-DAY-CLOS-N         PIC 9(01).               \n000686         05  SPEC-NOR-SUFF-N             PIC X(01).               \n000688*=========================================================        \n000690*            APPLICATION CLOSE DAYS OTHER THAN NORMAL             \n000692*            EACH APPLICATION HAS A DAY OF WEEK CODE              \n000694*            AND SUFFIX (IF OTHER THAN NORMAL)                    \n000696*                                                                 \n000698*========================================================         \n000700     03  SPEC-ADDL-DAYS-CLOSED-N.                                 \n000702         05  DDA-ADD-DAY-N               PIC X(03).               \n000704         05  SAV-ADD-DAY-N               PIC X(03).               \n000706         05  CD-ADD-DAY-N                PIC X(03).               \n000708         05  ILN-ADD-DAY-N               PIC X(03).               \n000710         05  LD-ADD-DAY-N                PIC X(03).               \n000712         05  FILLER                      PIC X(06).               \n000714         05  AGL-ADD-DAY-N               PIC X(03).               \n000716         05  FILLER                      PIC X(03).               \n000718         05  IRA-ADD-DAY-N               PIC X(03).               \n000720         05  SDB-ADD-DAY-N               PIC X(03).               \n000722         05  TDA-ADD-DAY-N               PIC X(03).               \n000724         05  TFR-ADD-DAY-N               PIC X(03).               \n000726     03  SPEC-GL-FMT-N                   PIC X(01).               \n000728     03  SPEC-NCC-GL-N                   PIC X(04).               \n000730     03  SPEC-PTS-GL-N                   PIC 9(03).               \n000732     03  SPEC-DDA-SORT-IND-N             PIC 9(01).               \n000734     03  SPEC-MOMENTUM-N                 PIC 9(01).               \n000736     03  FILLER-UNAVAIL-02               PIC X(01).               \n000738*\n000740 01  SPEC-CARD-3-N.                                               \n000742     05  FILLER                          PIC X(07).               \n000744     05  SPEC-HOLIDAYS-N         OCCURS                           \n000746                                 18 TIMES.                        \n000748         10  SPEC-HOL-MM-N               PIC X(02).               \n000750         10  SPEC-HOL-DD-N               PIC X(02).               \n000752     05  SPEC-FM-SUPPRESS-N              PIC X(01).               \n000754     05  SPEC-COMBINE-SAV-N              PIC X(01).               \n000756     05  FILLER-UNAVAIL-03               PIC X(01).               \n000758*\n000760 01  SPEC-CARD-4-N.                                               \n000762     05  FILLER                          PIC X(07).               \n000764     05  SPEC-RMT-BK-INDICATOR-N         PIC X(02).               \n000766     05  SPEC-RMT-RPT-TYPE-N             PIC 9(01).               \n000768     05  SPEC-RMT-SPCL-HANDLING-N        PIC X(01).               \n000770     05  SPEC-RMT-STATION-NAME-N         PIC X(10).               \n000772     05  SPEC-LINE-CHG-CODE-N            PIC X(01).               \n000774     05  SPEC-SEPARATE-TYPE-5-N          PIC X(01).               \n000776     05  SPEC-INCLUDE-PART-N             PIC X(01).               \n000778     05  SPEC-INCLUDE-NEW-N              PIC X(01).               \n000780     05  SPEC-PRT-PROP-DESC-N            PIC X(01).               \n000782     05  SPEC-DDA-NEW-AMT-N              PIC X(05).               \n000784     05  SPEC-DDA-NEW-AMT-R-N    REDEFINES                        \n000786                                 SPEC-DDA-NEW-AMT-N               \n000788                                         PIC 9(05).               \n000790     05  SPEC-ALPHA-BOARDRPT-SEQ-N       PIC X(01).               \n000792     05  SPEC-LD-DAYS-PD-N               PIC 9(03).               \n000794     05  SPEC-MORT-DAYS-PD-N             PIC 9(03).               \n000796     05  SPEC-ILN-DAYS-PD-N              PIC 9(03).               \n000798     05  SPEC-LD-OVER-SPC-AMT-N          PIC 9(05).               \n000800     05  SPEC-MORT-OVER-SPC-AMT-N        PIC 9(05).               \n000802     05  SPEC-LD-LINE-CHG-AMT-N          PIC 9(05).               \n000804     05  SPEC-MORT-LINE-CHG-AMT-N        PIC 9(05).               \n000806     05  SPEC-LD-NEW-AMT-N               PIC 9(05).               \n000808     05  SPEC-MORT-NEW-AMT-N             PIC 9(05).               \n000810     05  SPEC-ILN-NEW-AMT-N              PIC 9(05).               \n000812     05  SPEC-ILN-PD-AMT-N               PIC 9(05).               \n000814     05  FILLER-UNAVAIL-04               PIC X(01).               \n000816*\n000818 01  SPEC-CARD-5-N.                                               \n000820     05  FILLER                          PIC X(07).               \n000822     05  SPEC-BK-ADDR-N                  PIC X(28).               \n000824     05  SPEC-BK-ADDR-2-N                PIC X(27).               \n000826     05  SPEC-ANCILLARY-SERV-N           PIC 9(01).               \n000828     05  SPEC-FED-ID-N                   PIC X(10).               \n000830     05  SPEC-ATM-OPTION-N               PIC X(01).               \n000832     05  SPEC-THS-MTH-ACT-N              PIC X(01).               \n000834     05  SPEC-COMB-NON-ACCR-N            PIC X(01).               \n000836     05  SPEC-PD-NON-ACCR-N              PIC X(01).               \n000838     05  SPEC-MORT-DETERMINANT-N         PIC X(01).               \n000840     05  SPEC-BOARDRPT-BR-SORT-N         PIC 9(01).               \n000842     05  SPEC-TKL-N                      PIC X(01).               \n000844     05  SPEC-CLN-DDA-N                  PIC X(01).               \n000846     05  FILLER-UNAVAIL-05               PIC X(01).               \n000848*\n000850 01  SPEC-CARD-6-N.                                               \n000852     05  FILLER                          PIC X(07).               \n000854     05  SPEC-RMT-TFR-STATION-N          PIC X(10).               \n000856     05  SPEC-LNS-ACCOUNT-LENGTH-N       PIC 9(02).               \n000858     05  SPEC-LNS-SUB-ACCT-LENGTH-N      PIC 9(02).               \n000860     05  SPEC-PRIV-ADDL-REL-CODES-N      PIC X(02).               \n000862     05  SPEC-PRIV-ADDL-REL-CD-N REDEFINES                        \n000864                                 SPEC-PRIV-ADDL-REL-CODES-N.      \n000866         10  SPEC-PRIV-ADDL-REL-CD1-N    PIC X(01).               \n000868         10  SPEC-PRIV-ADDL-REL-CD2-N    PIC X(01).               \n000870     05  SPEC-LEGAL-LEND-LIMIT-RPT-N     PIC 9(01).               \n000872     05  SPEC-CTS-IND-N                  PIC X(01).               \n000874     05  SPEC-AGL-BOND-N                 PIC 9(01).               \n000876     05  SPEC-LINE-CHG-OFF-SORT-N        PIC X(01).               \n000878     05  SPEC-CD-BRKRD-DEP-CLASS-CDS-N   PIC X(03).               \n000880     05  SPEC-EOY-PHONE-N                PIC 9(10).               \n000882     05  SPEC-POSTAL-PERMIT-N            PIC X(06).               \n000884     05  SPEC-POSTAL-CITY-ST-N           PIC X(25).               \n000886     05  SPEC-EOY-RPT-SEQ-N              PIC X(01).               \n000888     05  SPEC-MBL-BK-NTC-OPT-N           PIC X(01).               \n000890     05  SPEC-EOY-EARLY-RUN-N            PIC X(01).               \n000892     05  SPEC-CNTRVIEW-ARCHIVE-NTC-N     PIC X(01).               \n000894     05  SPEC-EOY-RETURN-TO-BK-N         PIC X(01).               \n000896     05  SPEC-NEW-TFR-N                  PIC 9(01).               \n000898     05  SPEC-IRS-MAG-TAPE-RPT-N         PIC X(01).               \n000900     05  SPEC-IRS-HOME-BK-N              PIC 9(03).               \n000902     05  FILLER-UNAVAIL-06               PIC X(01).               \n000904*\n000906 01  SPEC-CARD-7-N.                                               \n000908     05  FILLER                          PIC X(07).               \n000910     05  SPEC-CFF-FLAG-N                 PIC X(01).               \n000912     05  SPEC-MBL-BNK-NTC-N              PIC X(01).               \n000914     05  SPEC-IEIP-PHASE-N               PIC X(01).               \n000916     05  SPEC-ZIPPROC-PROP-ADDR-N        PIC 9(01).               \n000918     05  SPEC-FTPFI-CUST-TYPE-N          PIC X(01).               \n000920     05  SPEC-LPLUS-N                    PIC X(01).               \n000922     05  SPEC-TEMP-DAILY-COD-N           PIC X(01).               \n000924     05  SPEC-MAIL-ADDR-LINES-N          PIC X(01).               \n000926     05  SPEC-EOY-IRA-PHONE-N            PIC 9(10).               \n000928     05  SPEC-EOY-1098-PHONE-N           PIC 9(10).               \n000930     05  SPEC-EOY-DELETE-DATE-N          PIC 9(06).               \n000932     05  SPEC-EOY-IRA-FICHE-N            PIC X(01).               \n000934     05  SPEC-EOY-IRA-PAPER-N            PIC X(01).               \n000936     05  SPEC-EOY-IRA-STMT-EARLY-N       PIC X(01).               \n000938     05  SPEC-FDIC-TAGP-N                PIC X(01).               \n000940     05  SPEC-NO-IRA-STMTS-N             PIC 9(01).               \n000942     05  SPEC-TES-NTM-N                  PIC 9(01).               \n000944     05  SPEC-CIF-NAME-ADDR-N            PIC 9(01).               \n000946     05  SPEC-EOY-IRA-STMT-N             PIC X(01).               \n000948     05  SPEC-5498-FORM-PRT-N            PIC 9(01).               \n000950     05  SPEC-EOY-COD-CLOSED-RPT-N       PIC X(01).               \n000952     05  SPEC-EOY-IRA-STMT-PRINT-N       PIC X(01).               \n000954     05  SPEC-EIP-IP-N                   PIC X(15).               \n000956     05  SPEC-ERASERS-OFF-N              PIC 9(01).               \n000958     05  SPEC-SPECIAL-DL-BILLING-N       PIC X(01).               \n000960     05  SPEC-PROFITABILITY-N            PIC X(01).               \n000962     05  SPEC-EOY-ESC-TYPE-N             PIC X(01).               \n000964     05  SPEC-EOY-EARLY-DATE-N           PIC 9(06).               \n000966     05  SPEC-PROFIT-CUST-TYPE-N         PIC X(01).               \n000968     05  SPEC-NUFUND-N                   PIC 9(01).               \n000970     05  SPEC-EOY-ESC-STMT-PAPER-N       PIC 9(01).               \n000972     05  SPEC-SDP-FMS-EXCLUDE-N          PIC X(01).               \n000974     05  FILLER-UNAVAIL-07               PIC X(01).               \n000976*\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    484 lines from 1 to 484.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 1, "total_chunks": 55, "start_line": 1, "end_line": 484, "line_count": 484}

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
- Source code length: 33992 characters

### Program Map Present
- Has program_map: No
- Program map length: 0 characters

### Other Context Keys
- program_name: str
- timestamp: str
- source_file_path: str
- chunk_number: int
- total_chunks: int
- start_line: int
- end_line: int
- line_count: int

---

## Full Source Code (if present)


```cobol

=============================================================================
CHUNK 1 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 1 to 484 (484 lines)
Chunk Tokens (estimated): ~7,935
Actual Input Tokens: 9,341 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 1-484 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 1 of 55 chunks
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
      The source code below is only CHUNK 1 of 55.


=============================================================================
CHUNK 1 SOURCE CODE (Lines 1-484)
=============================================================================

```cobol
000010$ RESET LIST SET LINEINFO ERRORLIST
000012$ SET AUTOINSERT
000014 IDENTIFICATION DIVISION.
000016 PROGRAM-ID.    MINDISTCALC.
000018 AUTHOR.        "XGEN Generator -- Version 45A.001 (Sep-10-12)".
000020* Build ID: 1.16 (Tue Mar 12 09:22:26 EDT 2013)
000022 DATE-WRITTEN. 10-Apr-2024 17:36:53.
000024 DATE-COMPILED.
000026*REMARKS.
000028*  SYSTEM    : TDAR
000030*  XGEN FILE : TDA/XGEN/mindistcalc.xgn
000032*  SRC FILE  : TDAR/SOURCE/TDAS-MINDISTCALC.c74
000034*  OBJ FILE  : TDAR/SOURCE/MINDISTCALC
000036*  COMPILER  : COBOL74
000038*  REPORTS   :
000040*     RMDRPT2             RMDRPT
000042*  END OF REPORTS
000044*
000046*  COPY FILES  :
000048*    X:\DEV\
000050*         TDA/LIB/EOYTEARPAGE.XLIB
000052*         TDA/LIB/XGEN-PRINT-ROUTINES.XLIB
000054*         TDA/LIB/RMD-LEF-TBL.XLIB
000056*         TDA/LIB/GENLCOPY.XLIB
000058*         TDA/LIB/ACH.XLIB
000060*         TDA/LIB/GENLCOPY.XLIB
000062*         TDA/LIB/RPTWRK.XLIB
000064*    
000066*         TDA/LIB/REPORTS.XLIB
000068*         TDA/LIB/REPORTS.XLIB
000070*         TDA/LIB/REPORTS.XLIB
000072*         TDA/LIB/REPORTS.XLIB
000074*         TDA/LIB/REPORTS.XLIB
000076*         TDA/LIB/REPORTS.XLIB
000078*         TDA/LIB/REPORTS.XLIB
000080*         TDA/LIB/REPORTS.XLIB
000082*         TDA/LIB/REPORTS.XLIB
000084*         TDA/LIB/REPORTS.XLIB
000086*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000088*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000090*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000092*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000094*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000096*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000098*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000100*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000102*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000104*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000106*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000108*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000110*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000112*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000114*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000116*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000118*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000120*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000122*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000124*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000126*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000128*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000130*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000132*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000134*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000136*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000138*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000140*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000142*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000144*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000146*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000148*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000150*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000152*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000154*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000156*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000158*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000160*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000162*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000164*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000166*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000168*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000170*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000172*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000174*         TDA/LIB/GENL-COPYBANK-4DGT.XLIB
000176*         TDA/LIB/COPYGENLCOPY.XLIB
000178*  END OF COPY FILES
000180*END OF REMARKS.
000182*
000184*****************************************************************
000186******************************************************************
000188*                Proprietary Software Material                   *
000190* This material is proprietary to Computer Services, Inc.and is  *
000192* not to be reproduced, used or disclosed except in accordance   *
000194* with software license or upon written authorization of:        *
000196*     Computer Services, Inc.                                    *
000198*     3901 Technology Drive Paducah, KY 42001                    *
000200******************************************************************
000202*COMPUTER SERVICES A SERIES OPERATING INSTRUCTIONS               H
000204*                                                                O
000206* PROGRAM NAME             RUN FREQUENCY                DATE     H
000208* ----------------------  --------------            ------------ O
000210* ! TDA/MINDISTCALC    !  ! AS NEEDED  !            !          ! D
000212* ----------------------  --------------            ------------ O
000214*                                                     APPROVED   H
000216*                                                   ------------ O
000218* PROGRAM NARRATIVE OR DESCRIPTION                  !          ! H
000220*                                                   ------------ O
000222* -------------------------------------------------------------- O
000224* !              MINIMUM DISTRIBUTION CALCULATION              ! O
000226* !                                                            ! O
000228* ! THIS PROGRAM CALCULATES THE REQUIRED MINIMUM DISTRIBUTION  ! O
000230* ! FOR IRA ACCOUNTS WHOSE CUSTOMERS ARE AT RMD AGE SET BY THE ! O
000232* ! THE IRS. REPORT IS GENERATED TO SHOW RESULTS OF            ! O
000234* ! CALCULATION.                                               ! O
000236* !                                                            ! O
000238* !                                                            ! O
000240* ! UPLOAD FILE IS CREATED TO UPDATE THE MINIMUM DISTRIBUTION  ! O
000242* ! IF THE PCR AND ACCOUNT ARE SET TO ACCEPT THE F/M.  A       ! O
000244* ! SEPARATE UPLOAD FILE IS ALSO CREATED IF OPTION 3 (ALL      ! O
000246* ! BANKS) IS SELECTED.  THIS FILE UPDATES THE RMD ON BOTH THE ! O
000248* ! CUSTOMER AND ACCOUNT RECORDS.                              ! O
000250* !                                                            ! O
000252* !                                                            ! O
000254* ! INPUT FILES:                                               ! O
000256* !    PROC-FILE  :  TDA/DAILY/ddd ON GENERAL                  ! O
000258* !                  ddd = DAY OF WK (MON, TUE, WED, THU, FRI) ! O
000260* !                                                            ! O
000262* !    BK-SPEC-FILE  :  SPECS/BANK/NEW                         ! O
000264* !                                                            ! O
000266* ! OUTPUT FILES:                                              ! O
000268* !    RMDRPT (FOR NON-INHERITED IRA'S):                       ! O
000270* !             PRINT/cc/TDA/00SP/bbbb/xxxx/ddNSP700 ON GENERAL! O
000272* !               cc   = DATA CENTER                           ! O
000274* !               bbbb = BANK                                  ! O
000276* !               xxxx = SERVER INDICATORS                     ! O
000278* !               dd   = DAY (01 - 31)                         ! O
000280* !                                                            ! O
000282* !    RMDRPT2 (FOR INHERITED IRA'S):                          ! O
000284* !             PRINT/cc/TDA/00SP/bbbb/xxxx/ddNSP701 ON GENERAL! O
000286* !               cc   = DATA CENTER                           ! O
000288* !               bbbb = BANK                                  ! O
000290* !               xxxx = SERVER INDICATORS                     ! O
000292* !               dd   = DAY (01 - 31)                         ! O
000294* !                                                            ! O
000296* !    MASS FILE MAINT:                                        ! O
000298* !       'DST' FILES ARE AUTO DISTRIBUTION FM RECORDS         ! O
000300* !       'CST' FILES ARE CUSTOMER/ACCOUNT FM RECORDS          ! O
000302* !                                                            ! O
000304* !       SINGLE BANK:    RIN0D/TDA/mmdd/bbb/RMDDST ON RMT     ! O
000306* !                       RIN0D/TDA/mmdd/bbb/RMDCST ON RMT     ! O
000308* !                         mmdd = MONTH/DAY                   ! O
000310* !                         bbb  = BANK                        ! O
000312* !                                                            ! O
000314* !       LIST OF BANKS: RIN0D/TDA/mmdd/000/RMDDSThhmm ON RMT  ! O
000316* !                      RIN0D/TDA/mmdd/000/RMDCSThhmm ON RMT  ! O
000318* !                        mmdd = MONTH/DAY                    ! O
000320* !                        hhmm = HOUR/MIN                     ! O
000322* !                                                            ! O
000324* !       ALL BANKS:     RIN0D/TDA/mmdd/000/RMDDSTs ON RMT     ! O
000326* !                      RIN0D/TDA/mmdd/000/RMDCSTs ON RMT     ! O
000328* !                        mmdd = MONTH/DAY                    ! O
000330* !                        s    = TDA SUFFIX                   ! O
000332* !                                                            ! O
000334* !              - - - - - - - - - - - - - - -                 ! O
000336* !                                                            ! O
000338* ! PROGRAM FLOW:                                              ! O
000340* !                                                            ! O
000342* ! -> ENTER BANK OPTION                                       ! O
000344* !    1 - ONE BANK                                            ! O
000346* !    2 - LIST OF BANKS                                       ! O
000348* !    3 - ALL BANKS (USES PROC-FILE)                          ! O
000350* !                                                            ! O
000352* ! -> CONFIRM BANK OPTION (Y/N)                               ! O
000354* !                                                            ! O
000356* ! IF ONE BANK:                                               ! O
000358* !                                                            ! O
000360* !    -> ENTER BANK NUMBER (4-DIGIT)                          ! O
000362* !                                                            ! O
000364* ! IF LIST OF BANKS:                                          ! O
000366* !                                                            ! O
000368* !    -> ENTER LIST (000100020003...) MAX 20 BANKS            ! O
000370* !                                                            ! O
000372* -------------------------------------------------------------- O
000374*                                                                O
000376* DATE CONTROL :  MCP               OTHER   XXX                  O
000378*                          -----           -----                 O
000380*  ENTER VIA      CONSOLE                   N/A                  O
000382*                          -----           --------------------- O
000384* FILE DATA                                                      H
000386*                                                                F
000388* SPECIAL FEATURES                                               H
000390*                                                                O
000392* -------------------------------------------------------------- S
000394* ! SW3 - BYPASS RMD REPORT CREATION                           ! O
000396* !       RMD REPORTS WILL NOT BE CREATED WHEN SW3 SET         ! O
000398* -------------------------------------------------------------- O
000400/                                                                 
000402*****************************************************************
000404*
000406*****************************************************************
000408 ENVIRONMENT DIVISION.
000410*****************************************************************
000412 CONFIGURATION SECTION.
000414*------------- -------
000416 SOURCE-COMPUTER. UNISYS-A-SERIES.
000418 OBJECT-COMPUTER. UNISYS-A-SERIES
000420     SEGMENT-LIMIT IS 25 .
000422*
000424 SPECIAL-NAMES.
000426     SW1 ON IS Z-SW1
000428     SW2 ON IS Z-SW2
000430     SW3 ON IS Z-SW3
000432     SW4 ON IS Z-SW4
000434     SW5 ON IS Z-SW5
000436     SW6 ON IS Z-SW6
000438     SW7 ON IS Z-SW7
000440     SW8 ON IS Z-SW8.
000442 INPUT-OUTPUT SECTION.
000444*------------ -------
000446 FILE-CONTROL.
000448*------------
000450*
000452     SELECT BK-SPEC-FILE
000454         ASSIGN TO DISK
000456         ORGANIZATION IS SEQUENTIAL
000458         ACCESS IS SEQUENTIAL
000460         ACTUAL KEY IS Z-FILE3-KEY
000462         FILE STATUS IS Z-FLINFO3-STATUS.
000464*
000466     SELECT PROC-FILE
000468         ASSIGN TO DISK
000470         ORGANIZATION IS SEQUENTIAL
000472         ACCESS IS SEQUENTIAL
000474         ACTUAL KEY IS Z-FILE4-KEY
000476         FILE STATUS IS Z-FLINFO4-STATUS.
000478*
000480     SELECT DST-FILE-MAINT
000482         ASSIGN TO DISK
000484         ORGANIZATION IS SEQUENTIAL
000486         ACCESS IS SEQUENTIAL
000488         ACTUAL KEY IS Z-FILE5-KEY
000490         FILE STATUS IS Z-FLINFO5-STATUS.
000492*
000494     SELECT CST-FILE-MAINT
000496         ASSIGN TO DISK
000498         ORGANIZATION IS SEQUENTIAL
000500         ACCESS IS SEQUENTIAL
000502         ACTUAL KEY IS Z-FILE6-KEY
000504         FILE STATUS IS Z-FLINFO6-STATUS.
000506*
000508     SELECT LISTING
000510         ASSIGN TO PRINTER.
000512*
000514     SELECT FICHE
000516         ASSIGN TO PRINTER.
000518*
000520*****************************************************************
000522 DATA DIVISION.
000524*****************************************************************
000526*
000528 FILE SECTION.
000530*---- -------
000532*
000534* FILE DESCRIPTION FOR BK-SPEC-FILE ( 82 BYTES )
000536*
000538 FD  BK-SPEC-FILE
000540     VALUE OF TITLE IS "SPECS/BANK/NEW"
000542     VALUE OF DEPENDENTSPECS IS TRUE.
000544*
000546 01  SPEC-RECORD-N                       PIC X(82).               
000548*
000550 01  SPEC-CARD-1-N.                                               
000552     05  SPEC-BK-NO-N                    PIC X(04).               
000554     05  SPEC-BK-NO-R REDEFINES SPEC-BK-NO-N.                     
000556         10  FILLER                      PIC 9(01).               
000558         10  SPEC-BK-NO-LST-3-N.                                  
000560             15  SPEC-BK-NO-9-N          PIC 9(03).               
000562     05  SPEC-BK-NO-R1 REDEFINES SPEC-BK-NO-N.                    
000564         10 SPEC-BK-NO-9-4-N             PIC 9(04).               
000566     05  SPEC-BR-CODE-MSD-N              PIC 9(01).               
000568     05  SPEC-SEQ-NO-N                   PIC 9(02).               
000570     05  SPEC-FILE-ID-VERSION-N.                                  
000572         10  SPEC-FILE-ID-N              PIC X(03).               
000574         10  SPEC-FILE-VERSION-N         PIC X(03).               
000576     05  SPEC-BK-NAME-N                  PIC X(30).               
000578     05  SPEC-REND-SITE-N                PIC 9(02).               
000580     05  SPEC-MAIL-CENTER-N              PIC 9(02).               
000582     05  SPEC-TIMEZONE-N                 PIC X(01).               
000584     05  SPEC-PP-MICR-PRT-N              PIC X(01).               
000586     05  FILLER                          PIC X(01).               
000588     05  SPEC-DQVISTA-N                  PIC X(01).               
000590     05  SPEC-MSI-N                      PIC X(01).               
000592     05  SPEC-CENTERVIEW-N               PIC X(01).               
000594     05  SPEC-FDIC-UNINSURE-N            PIC X(01).               
000596     05  SPEC-OFAC-FREQ-N                PIC X(01).               
000598     05  SPEC-OFAC-FREQ-MONTH-N          PIC X(01).               
000600     05  SPEC-CBI-LNS-TICKLER-N          PIC X(01).               
000602     05  SPEC-PRIV-EXCLUDE-CUST-N        PIC 9(01).               
000604     05  SPEC-MULTI-CUT-OPTION-N         PIC 9(01).               
000606     05  SPEC-PRIV-NTC-BUSINESS-N        PIC X(01).               
000608     05  SPEC-PRIV-NTC-DNM-N             PIC X(01).               
000610     05  SPEC-PRIV-NTC-MAIL-MONTH-N      PIC 9(02).               
000612     05  SPEC-PRIV-NTC-OUTPUT-FMT-N      PIC 9(01).               
000614     05  SPEC-PRIV-LABELS-TYPE-N         PIC 9(01).               
000616     05  SPEC-PRIV-NTC-APPLS-N           PIC 9(04).               
000618     05  SPEC-PRIV-PP-PLUS-N             PIC X(01).               
000620     05  SPEC-PRIV-NTC-REL-CDS-N         PIC X(01).               
000622     05  SPEC-WEB-ENABLED-N              PIC X(01).               
000624     05  SPEC-NEW-MCIF-SYS-N             PIC X(01).               
000626     05  SPEC-BK-IMG-SITE-N              PIC X(01).               
000628     05  SPEC-BK-IMG-SERV-N              PIC X(01).               
000630     05  SPEC-BK-STATUS-N                PIC X(01).               
000632     05  SPEC-BK-TDA-STAT-N              PIC X(01).               
000634     05  SPEC-HOLDING-CO-N               PIC X(01).               
000636     05  SPEC-NEW-ACH-N                  PIC 9(01).               
000638     05  SPEC-CSI-HOST-N                 PIC 9(02).               
000640     05  FILLER-UNAVAIL-01               PIC X(01).               
000642*
000644 01  SPEC-CARD-2-N.                                               
000646     03  SPEC-BK-DATA-N.                                          
000648         05  FILLER                      PIC X(07).               
000650         05  SPEC-BR-NO-N                PIC X(02).               
000652         05  SPEC-GL-NO-N.                                        
000654             10  SPEC-GL-NO-LST-2-N      PIC X(03).               
000656         05  SPEC-GL-NO-9-N              REDEFINES                
000658                                         SPEC-GL-NO-N             
000660                                         PIC 9(03).               
000662         05  SPEC-MERGE-FLAG-N           PIC 9(01).               
000664         05  SPEC-ACCT-LENGTH-N          PIC X(01).               
000666         05  SPEC-EIS-FILES-N            PIC 9(01).               
000668         05  SPEC-FINCEN-PULL-N          PIC 9(01).               
000670         05  SPEC-NEW-GL-N               PIC X(01).               
000672         05  SPEC-BK-REP-N               PIC X(03).               
000674         05  SPEC-BK-PHONE-NUM-N.                                 
000676             10  SPEC-AREA-CODE-N        PIC X(03).               
000678             10  SPEC-PHONE-N.                                    
000680                 15  SPEC-PHONE-1ST-3-N  PIC X(03).               
000682                 15  SPEC-PHONE-LST-4-N  PIC X(04).               
000684         05  SPEC-NOR-DAY-CLOS-N         PIC 9(01).               
000686         05  SPEC-NOR-SUFF-N             PIC X(01).               
000688*=========================================================        
000690*            APPLICATION CLOSE DAYS OTHER THAN NORMAL             
000692*            EACH APPLICATION HAS A DAY OF WEEK CODE              
000694*            AND SUFFIX (IF OTHER THAN NORMAL)                    
000696*                                                                 
000698*========================================================         
000700     03  SPEC-ADDL-DAYS-CLOSED-N.                                 
000702         05  DDA-ADD-DAY-N               PIC X(03).               
000704         05  SAV-ADD-DAY-N               PIC X(03).               
000706         05  CD-ADD-DAY-N                PIC X(03).               
000708         05  ILN-ADD-DAY-N               PIC X(03).               
000710         05  LD-ADD-DAY-N                PIC X(03).               
000712         05  FILLER                      PIC X(06).               
000714         05  AGL-ADD-DAY-N               PIC X(03).               
000716         05  FILLER                      PIC X(03).               
000718         05  IRA-ADD-DAY-N               PIC X(03).               
000720         05  SDB-ADD-DAY-N               PIC X(03).               
000722         05  TDA-ADD-DAY-N               PIC X(03).               
000724         05  TFR-ADD-DAY-N               PIC X(03).               
000726     03  SPEC-GL-FMT-N                   PIC X(01).               
000728     03  SPEC-NCC-GL-N                   PIC X(04).               
000730     03  SPEC-PTS-GL-N                   PIC 9(03).               
000732     03  SPEC-DDA-SORT-IND-N             PIC 9(01).               
000734     03  SPEC-MOMENTUM-N                 PIC 9(01).               
000736     03  FILLER-UNAVAIL-02               PIC X(01).               
000738*
000740 01  SPEC-CARD-3-N.                                               
000742     05  FILLER                          PIC X(07).               
000744     05  SPEC-HOLIDAYS-N         OCCURS                           
000746                                 18 TIMES.                        
000748         10  SPEC-HOL-MM-N               PIC X(02).               
000750         10  SPEC-HOL-DD-N               PIC X(02).               
000752     05  SPEC-FM-SUPPRESS-N              PIC X(01).               
000754     05  SPEC-COMBINE-SAV-N              PIC X(01).               
000756     05  FILLER-UNAVAIL-03               PIC X(01).               
000758*
000760 01  SPEC-CARD-4-N.                                               
000762     05  FILLER                          PIC X(07).               
000764     05  SPEC-RMT-BK-INDICATOR-N         PIC X(02).               
000766     05  SPEC-RMT-RPT-TYPE-N             PIC 9(01).               
000768     05  SPEC-RMT-SPCL-HANDLING-N        PIC X(01).               
000770     05  SPEC-RMT-STATION-NAME-N         PIC X(10).               
000772     05  SPEC-LINE-CHG-CODE-N            PIC X(01).               
000774     05  SPEC-SEPARATE-TYPE-5-N          PIC X(01).               
000776     05  SPEC-INCLUDE-PART-N             PIC X(01).               
000778     05  SPEC-INCLUDE-NEW-N              PIC X(01).               
000780     05  SPEC-PRT-PROP-DESC-N            PIC X(01).               
000782     05  SPEC-DDA-NEW-AMT-N              PIC X(05).               
000784     05  SPEC-DDA-NEW-AMT-R-N    REDEFINES                        
000786                                 SPEC-DDA-NEW-AMT-N               
000788                                         PIC 9(05).               
000790     05  SPEC-ALPHA-BOARDRPT-SEQ-N       PIC X(01).               
000792     05  SPEC-LD-DAYS-PD-N               PIC 9(03).               
000794     05  SPEC-MORT-DAYS-PD-N             PIC 9(03).               
000796     05  SPEC-ILN-DAYS-PD-N              PIC 9(03).               
000798     05  SPEC-LD-OVER-SPC-AMT-N          PIC 9(05).               
000800     05  SPEC-MORT-OVER-SPC-AMT-N        PIC 9(05).               
000802     05  SPEC-LD-LINE-CHG-AMT-N          PIC 9(05).               
000804     05  SPEC-MORT-LINE-CHG-AMT-N        PIC 9(05).               
000806     05  SPEC-LD-NEW-AMT-N               PIC 9(05).               
000808     05  SPEC-MORT-NEW-AMT-N             PIC 9(05).               
000810     05  SPEC-ILN-NEW-AMT-N              PIC 9(05).               
000812     05  SPEC-ILN-PD-AMT-N               PIC 9(05).               
000814     05  FILLER-UNAVAIL-04               PIC X(01).               
000816*
000818 01  SPEC-CARD-5-N.                                               
000820     05  FILLER                          PIC X(07).               
000822     05  SPEC-BK-ADDR-N                  PIC X(28).               
000824     05  SPEC-BK-ADDR-2-N                PIC X(27).               
000826     05  SPEC-ANCILLARY-SERV-N           PIC 9(01).               
000828     05  SPEC-FED-ID-N                   PIC X(10).               
000830     05  SPEC-ATM-OPTION-N               PIC X(01).               
000832     05  SPEC-THS-MTH-ACT-N              PIC X(01).               
000834     05  SPEC-COMB-NON-ACCR-N            PIC X(01).               
000836     05  SPEC-PD-NON-ACCR-N              PIC X(01).               
000838     05  SPEC-MORT-DETERMINANT-N         PIC X(01).               
000840     05  SPEC-BOARDRPT-BR-SORT-N         PIC 9(01).               
000842     05  SPEC-TKL-N                      PIC X(01).               
000844     05  SPEC-CLN-DDA-N                  PIC X(01).               
000846     05  FILLER-UNAVAIL-05               PIC X(01).               
000848*
000850 01  SPEC-CARD-6-N.                                               
000852     05  FILLER                          PIC X(07).               
000854     05  SPEC-RMT-TFR-STATION-N          PIC X(10).               
000856     05  SPEC-LNS-ACCOUNT-LENGTH-N       PIC 9(02).               
000858     05  SPEC-LNS-SUB-ACCT-LENGTH-N      PIC 9(02).               
000860     05  SPEC-PRIV-ADDL-REL-CODES-N      PIC X(02).               
000862     05  SPEC-PRIV-ADDL-REL-CD-N REDEFINES                        
000864                                 SPEC-PRIV-ADDL-REL-CODES-N.      
000866         10  SPEC-PRIV-ADDL-REL-CD1-N    PIC X(01).               
000868         10  SPEC-PRIV-ADDL-REL-CD2-N    PIC X(01).               
000870     05  SPEC-LEGAL-LEND-LIMIT-RPT-N     PIC 9(01).               
000872     05  SPEC-CTS-IND-N                  PIC X(01).               
000874     05  SPEC-AGL-BOND-N                 PIC 9(01).               
000876     05  SPEC-LINE-CHG-OFF-SORT-N        PIC X(01).               
000878     05  SPEC-CD-BRKRD-DEP-CLASS-CDS-N   PIC X(03).               
000880     05  SPEC-EOY-PHONE-N                PIC 9(10).               
000882     05  SPEC-POSTAL-PERMIT-N            PIC X(06).               
000884     05  SPEC-POSTAL-CITY-ST-N           PIC X(25).               
000886     05  SPEC-EOY-RPT-SEQ-N              PIC X(01).               
000888     05  SPEC-MBL-BK-NTC-OPT-N           PIC X(01).               
000890     05  SPEC-EOY-EARLY-RUN-N            PIC X(01).               
000892     05  SPEC-CNTRVIEW-ARCHIVE-NTC-N     PIC X(01).               
000894     05  SPEC-EOY-RETURN-TO-BK-N         PIC X(01).               
000896     05  SPEC-NEW-TFR-N                  PIC 9(01).               
000898     05  SPEC-IRS-MAG-TAPE-RPT-N         PIC X(01).               
000900     05  SPEC-IRS-HOME-BK-N              PIC 9(03).               
000902     05  FILLER-UNAVAIL-06               PIC X(01).               
000904*
000906 01  SPEC-CARD-7-N.                                               
000908     05  FILLER                          PIC X(07).               
000910     05  SPEC-CFF-FLAG-N                 PIC X(01).               
000912     05  SPEC-MBL-BNK-NTC-N              PIC X(01).               
000914     05  SPEC-IEIP-PHASE-N               PIC X(01).               
000916     05  SPEC-ZIPPROC-PROP-ADDR-N        PIC 9(01).               
000918     05  SPEC-FTPFI-CUST-TYPE-N          PIC X(01).               
000920     05  SPEC-LPLUS-N                    PIC X(01).               
000922     05  SPEC-TEMP-DAILY-COD-N           PIC X(01).               
000924     05  SPEC-MAIL-ADDR-LINES-N          PIC X(01).               
000926     05  SPEC-EOY-IRA-PHONE-N            PIC 9(10).               
000928     05  SPEC-EOY-1098-PHONE-N           PIC 9(10).               
000930     05  SPEC-EOY-DELETE-DATE-N          PIC 9(06).               
000932     05  SPEC-EOY-IRA-FICHE-N            PIC X(01).               
000934     05  SPEC-EOY-IRA-PAPER-N            PIC X(01).               
000936     05  SPEC-EOY-IRA-STMT-EARLY-N       PIC X(01).               
000938     05  SPEC-FDIC-TAGP-N                PIC X(01).               
000940     05  SPEC-NO-IRA-STMTS-N             PIC 9(01).               
000942     05  SPEC-TES-NTM-N                  PIC 9(01).               
000944     05  SPEC-CIF-NAME-ADDR-N            PIC 9(01).               
000946     05  SPEC-EOY-IRA-STMT-N             PIC X(01).               
000948     05  SPEC-5498-FORM-PRT-N            PIC 9(01).               
000950     05  SPEC-EOY-COD-CLOSED-RPT-N       PIC X(01).               
000952     05  SPEC-EOY-IRA-STMT-PRINT-N       PIC X(01).               
000954     05  SPEC-EIP-IP-N                   PIC X(15).               
000956     05  SPEC-ERASERS-OFF-N              PIC 9(01).               
000958     05  SPEC-SPECIAL-DL-BILLING-N       PIC X(01).               
000960     05  SPEC-PROFITABILITY-N            PIC X(01).               
000962     05  SPEC-EOY-ESC-TYPE-N             PIC X(01).               
000964     05  SPEC-EOY-EARLY-DATE-N           PIC 9(06).               
000966     05  SPEC-PROFIT-CUST-TYPE-N         PIC X(01).               
000968     05  SPEC-NUFUND-N                   PIC 9(01).               
000970     05  SPEC-EOY-ESC-STMT-PAPER-N       PIC 9(01).               
000972     05  SPEC-SDP-FMS-EXCLUDE-N          PIC X(01).               
000974     05  FILLER-UNAVAIL-07               PIC X(01).               
000976*
```

⚠️  This is the source code you must document.
    484 lines from 1 to 484.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

