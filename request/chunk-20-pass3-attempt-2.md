# LLM Request Debug File
Generated: 2025-11-14T18:31:50.835058

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 20/55
- **Model**: gpt-4.1
- **Chunk Number**: 20
- **Pass Number**: 3
- **Attempt Number**: 2 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~8,774 tokens
- **Total Input**: ~10,732 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 20/55" (ID: detailed-code-explanation)

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


**CHUNK 20 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-14T17:36:35.036798", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 20 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 9903 to 10273 (371 lines)\nChunk Tokens (estimated): ~7,914\nActual Input Tokens: 9,320 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 9903-10273 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 20 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 20 of 55.\n\n\n=============================================================================\nCHUNK 20 SOURCE CODE (Lines 9903-10273)\n=============================================================================\n\n```cobol\n019814                          TDB-TDAA-MANUAL-RT-X.                   \n019816                 20  TDB-TDAA-MAN-RATE     PIC 9(2)V9(3).         \n019818                                                                  \n019820     05  TDB-TDAIRA.                                              \n019822         10  TDB-TDAI-BANK-X.                                     \n019824             15  TDB-TDAI-BANK             PIC 9(4).              \n019826         10  TDB-TDAI-BRCH-X.                                     \n019828             15  TDB-TDAI-BRCH             PIC 9(4).              \n019830         10  TDB-TDAI-APPL-X.                                     \n019832             15  TDB-TDAI-APPL             PIC 9(1).              \n019834         10  TDB-TDAI-CUST-X.                                     \n019836             15  TDB-TDAI-CUST             PIC 9(12).             \n019838         10  TDB-TDAI-ACCT-X.                                     \n019840             15  TDB-TDAI-ACCT             PIC 9(10).             \n019842         10  TDB-TDAI-PUB-ID               PIC X(8).              \n019844         10  TDB-TDAI-ADD-DT-X.                                   \n019846             15  TDB-TDAI-ADD-DT           PIC 9(8).              \n019848         10  TDB-TDAI-ADD-TM-X.                                   \n019850             15  TDB-TDAI-ADD-TM           PIC 9(6).              \n019852         10  TDB-TDAI-DS-TYPE              PIC X(2)               \n019854                          OCCURS 20 TIMES.                        \n019856         10  TDB-TDAI-CN-TYPE-X.                                  \n019858             15  TDB-TDAI-CN-TYPE          PIC 9(2)               \n019860                          OCCURS 20 TIMES.                        \n019862         10  TDB-TDAI-DS-CN-AMT-X.                                \n019864             15  TDB-TDAI-DS-CN-AMT        PIC S9(12)V99          \n019866                          OCCURS 20 TIMES.                        \n019868         10  TDB-TDAI-DS-PEN-AMT-X.                               \n019870             15  TDB-TDAI-DS-PEN-AMT       PIC S9(12)V99          \n019872                          OCCURS 20 TIMES.                        \n019874         10  TDB-TDAI-DS-WTHLD-AMT-X.                             \n019876             15  TDB-TDAI-DS-WTHLD-AMT     PIC S9(12)V99          \n019878                          OCCURS 20 TIMES.                        \n019880         10  TDB-TDAI-DS-ST-WH-AMT-X.                             \n019882             15  TDB-TDAI-DS-ST-WH-AMT     PIC S9(12)V99          \n019884                          OCCURS 20 TIMES.                        \n019886         10  TDB-TDAI-DS-EXC-EARN          PIC S9(12)V9(2)        \n019888                          OCCURS 20 TIMES.                        \n019890         10  TDB-TDAI-DS-C-YTD-CNT-X.                             \n019892             15  TDB-TDAI-DS-C-YTD-CNT     PIC 9(5).              \n019894         10  TDB-TDAI-DS-P-YTD-CNT-X.                             \n019896             15  TDB-TDAI-DS-P-YTD-CNT     PIC 9(5).              \n019898         10  TDB-TDAI-DS-AMT-C-YTD-X.                             \n019900             15  TDB-TDAI-DS-AMT-C-YTD     PIC S9(12)V9(2).       \n019902         10  TDB-TDAI-DS-AMT-P-YTD-X.                             \n019904             15  TDB-TDAI-DS-AMT-P-YTD     PIC S9(12)V9(2).       \n019906         10  TDB-TDAI-DS-INT-AMT-X.                               \n019908             15  TDB-TDAI-DS-INT-AMT       PIC S9(12)V9(2).       \n019910         10  TDB-TDAI-CN-YTD-CNT-X.                               \n019912             15  TDB-TDAI-CN-YTD-CNT       PIC 9(5).              \n019914         10  TDB-TDAI-CN-YTD-AMT-X.                               \n019916             15  TDB-TDAI-CN-YTD-AMT       PIC S9(12)V9(2).       \n019918         10  TDB-TDAI-CN-LYTD-AMT-X.                              \n019920             15  TDB-TDAI-CN-LYTD-AMT      PIC S9(12)V9(2).       \n019922         10  TDB-TDAI-EMP-CONT-LYR-X.                             \n019924             15  TDB-TDAI-EMP-CONT-LYR     PIC S9(12)V9(2).       \n019926         10  TDB-TDAI-REG-CONT-LYR-X.                             \n019928             15  TDB-TDAI-REG-CONT-LYR     PIC S9(12)V9(2).       \n019930         10  TDB-TDAI-UNINSURED            PIC X(1).              \n019932         10  TDB-TDAI-ROLLOVER-X.                                 \n019934             15  TDB-TDAI-ROLLOVER         PIC S9(12)V9(2).       \n019936         10  TDB-TDAI-ROLLOVER-LYR-X.                             \n019938             15  TDB-TDAI-ROLLOVER-LYR     PIC S9(12)V9(2).       \n019940         10  TDB-TDAI-TRANSFER-IN-X.                              \n019942             15  TDB-TDAI-TRANSFER-IN      PIC S9(12)V9(2).       \n019944         10  TDB-TDAI-TRANSFER-OUT-X.                             \n019946             15  TDB-TDAI-TRANSFER-OUT     PIC S9(12)V9(2).       \n019948         10  TDB-TDAI-1ST-CN-DATE-X.                              \n019950             15  TDB-TDAI-1ST-CN-DATE      PIC 9(8).              \n019952         10  TDB-TDAI-BASIS-C-LTD-X.                              \n019954             15  TDB-TDAI-BASIS-C-LTD      PIC S9(12)V99.         \n019956         10  TDB-TDAI-BASIS-D-LTD-X.                              \n019958             15  TDB-TDAI-BASIS-D-LTD      PIC S9(12)V99.         \n019960         10  TDB-TDAI-BASIS-D-YTD-X.                              \n019962             15  TDB-TDAI-BASIS-D-YTD      PIC S9(12)V99.         \n019964                                                                  \n019966         10  TDB-TDAI-NONDB-FIELDS.                               \n019968             15  TDB-TDAI-CN-TYPE-EX       PIC 9(2).              \n019970             15  TDB-TDAI-CN-TYPE-R REDEFINES TDB-TDAI-CN-TYPE-EX.\n019972                 20  TDB-TDAI-CN-TYPE-EX-1 PIC X.                 \n019974                 20  TDB-TDAI-CN-TYPE-EX-2 PIC X.                 \n019976             15  TDB-TDAI-DS-TYPE-EX.                             \n019978                20  TDB-TDAI-DS-TYPE-EX-1      PIC X.             \n019980                20  TDB-TDAI-DS-TYPE-EX-2      PIC X.             \n019982                                                                  \n019984      05 TDB-TDADISTR.                                            \n019986         10 TDB-TDAD-BANK                      PIC 9(04).         \n019988         10 TDB-TDAD-BRCH                      PIC 9(04).         \n019990         10 TDB-TDAD-APPL                      PIC 9(01).         \n019992         10 TDB-TDAD-CUST                      PIC 9(12).         \n019994         10 TDB-TDAD-ACCT                      PIC 9(10).         \n019996         10 TDB-TDAD-NXT-ACCT-P                PIC 9(10).         \n019998         10 TDB-TDAD-NXT-ACCT-S                PIC 9(10).         \n020000         10 TDB-TDAD-N-ACCT-BY-RT              PIC 9(1).          \n020002         10 TDB-TDAD-SERIAL                    PIC 9(12).         \n020004         10 TDB-TDAD-SER-NEXT                  PIC 9(12).         \n020006         10 TDB-TDAD-DISP-CD                   PIC 9(01).         \n020008         10 TDB-TDAD-TYPE                      PIC X(02).         \n020010         10 TDB-TDAD-PRINCIPAL                 PIC 9(01).         \n020012         10 TDB-TDAD-INTEREST                  PIC 9(01).         \n020014         10 TDB-TDAD-DS-CODE                   PIC 9(01).         \n020016         10 TDB-TDAD-WTHLD-CD                  PIC 9(01).         \n020018         10 TDB-TDAD-WHLD-AMT                  PIC S9(12)V99.     \n020020         10 TDB-TDAD-ST-WHLD-CD                PIC 9(01).         \n020022         10 TDB-TDAD-ST-WHLD-AMT               PIC S9(12)V99.     \n020024         10 TDB-TDAD-TRF-ACCT                  PIC 9(12).         \n020026         10 TDB-TDAD-TRF-ACCT-S                PIC 9(10).         \n020028         10 TDB-TDAD-AMT-CD                    PIC 9(01).         \n020030         10 TDB-TDAD-DS-AMT                    PIC S9(12)V99.     \n020032         10 TDB-TDAD-DS-FREQ                   PIC 9(01).         \n020034         10 TDB-TDAD-DS-NTRVL                  PIC 9(04).         \n020036         10 TDB-TDAD-END-OF-DIST-X.                               \n020038            15  TDB-TDAD-END-OF-DIST           PIC 9(1).          \n020040         10 TDB-TDAD-DIST-NTC-CD               PIC 9(01).         \n020042         10 TDB-TDAD-EOY-DS-FORM               PIC 9(01).         \n020044         10 TDB-TDAD-5-YR-RULE                 PIC 9(01).         \n020046         10 TDB-TDAD-ANUAL-RECALC              PIC 9(01).         \n020048         10 TDB-TDAD-JOINT-CD                  PIC 9(01).         \n020050         10 TDB-TDAD-PUB-ID                    PIC X(08).         \n020052         10 TDB-TDAD-LST-DIST-DT               PIC 9(08).         \n020054         10 TDB-TDAD-IN-PROC-DT                PIC 9(8).          \n020056         10 TDB-TDAD-NXT-DIST-DT               PIC 9(08).         \n020058         10 TDB-TDAD-NXT-DS-PROC               PIC 9(08).         \n020060         10 TDB-TDAD-ADD-DT                    PIC 9(08).         \n020062         10 TDB-TDAD-ADD-TM                    PIC 9(08).         \n020064                                                                  \n020066         10 TDB-TDAD-MIN-AMT                   PIC S9(12)V99.     \n020068         10 TDB-TDAD-AMT                       PIC S9(12)V99.     \n020070         10 TDB-TDAD-LST-AMT                   PIC S9(12)V99.     \n020072         10 TDB-TDAD-CUR-WHLD-AMT              PIC S9(12)V99.     \n020074         10 TDB-TDAD-WHLD-YTD                  PIC S9(12)V99.     \n020076         10 TDB-TDAD-LST-WHLD-AMT              PIC S9(12)V99.     \n020078         10 TDB-TDAD-PRINCPL-AMT               PIC S9(12)V99.     \n020080         10 TDB-TDAD-INT-AMT                   PIC S9(12)V99.     \n020082         10 TDB-TDAD-INT-YTD                   PIC S9(12)V99.     \n020084         10 TDB-TDAD-ST-CUR-W-AMT              PIC S9(12)V99.     \n020086         10 TDB-TDAD-ST-LST-W-AMT              PIC S9(12)V99.     \n020088         10 TDB-TDAD-CK-IND-1                  PIC X(1).          \n020090         10 TDB-TDAD-CK-IND-2                  PIC X(1).          \n020092         10 TDB-TDAD-LUPD-DT                   PIC 9(8).          \n020094         10 TDB-TDAD-LUPD-TM                   PIC 9(6).          \n020096         10 TDB-TDAD-RMD-OVERRIDE-X.                              \n020098            15 TDB-TDAD-RMD-OVERRIDE           PIC 9.             \n020100         10 TDB-TDAD-RMD-AMOUNT-X.                                \n020102            15 TDB-TDAD-RMD-AMOUNT             PIC S9(12)V9(2).   \n020104         10 TDB-TDAD-DS-NBR-X.                                    \n020106            15 TDB-TDAD-DS-NBR                 PIC 9(2).          \n020108                                                                  \n020110         10  TDB-TDAD-NONDB-FIELDS.                               \n020112             15  TDB-TDAD-DS-NTC-TYPE          PIC 9(1).          \n020114                                                                  \n020116     05  TDB-TDAACTV.                                             \n020118         10  TDB-TDA-ACTV-BANK-X.                                 \n020120             15  TDB-TDA-ACTV-BANK         PIC 9(4).              \n020122         10  TDB-TDA-ACTV-BRCH-X.                                 \n020124             15  TDB-TDA-ACTV-BRCH         PIC 9(4).              \n020126         10  TDB-TDA-ACTV-APPL-X.                                 \n020128             15  TDB-TDA-ACTV-APPL         PIC 9(1).              \n020130         10  TDB-TDA-ACTV-CUST-X.                                 \n020132             15  TDB-TDA-ACTV-CUST         PIC 9(12).             \n020134         10  TDB-TDA-ACTV-ACCT-X.                                 \n020136             15  TDB-TDA-ACTV-ACCT         PIC 9(10).             \n020138         10  TDB-TDA-ACTV-TOT-CD-X.                               \n020140             15  TDB-TDA-ACTV-TOT-CD       PIC 9(3).              \n020142         10  TDB-TDA-ACTV-IGL-GRP-X.                              \n020144             15  TDB-TDA-ACTV-IGL-GRP      PIC 9(2).              \n020146         10  TDB-TDA-ACTV-OFFICER          PIC X(3).              \n020148         10  TDB-TDA-ACTV-NC-INDC-X.                              \n020150             15  TDB-TDA-ACTV-NC-INDC      PIC 9(1).              \n020152         10  TDB-TDA-ACTV-PROC-FG-X.                              \n020154             15  TDB-TDA-ACTV-PROC-FG      PIC 9(1).              \n020156         10  TDB-TDA-ACTV-TYPE-X.                                 \n020158             15  TDB-TDA-ACTV-TYPE         PIC 9(4).              \n020160         10  TDB-TDA-ACTV-EFF-DT-X.                               \n020162             15  TDB-TDA-ACTV-EFF-DT       PIC 9(8).              \n020164         10  TDB-TDA-ACTV-DATE-X.                                 \n020166             15  TDB-TDA-ACTV-DATE         PIC 9(8).              \n020168         10  TDB-TDA-ACTV-MAINT-X.                                \n020170             15  TDB-TDA-ACTV-MAINT        PIC 9(8).              \n020172         10  TDB-TDA-ACTV-TIME-X.                                 \n020174             15  TDB-TDA-ACTV-TIME         PIC 9(8).              \n020176         10  TDB-TDA-ACTV-SEQ-NBR-X.                              \n020178             15  TDB-TDA-ACTV-SEQ-NBR      PIC 9(2).              \n020180         10  TDB-TDA-ACTV-SERIAL-X.                               \n020182             15  TDB-TDA-ACTV-SERIAL       PIC 9(12).             \n020184         10  TDB-TDA-ACTV-SOURCE-X.                               \n020186             15  TDB-TDA-ACTV-SOURCE       PIC 9(2).              \n020188         10  TDB-TDA-ACTV-ERASED-X.                               \n020190             15  TDB-TDA-ACTV-ERASED       PIC 9(1).              \n020192         10  TDB-TDA-ACTV-DR-CR-X.                                \n020194             15  TDB-TDA-ACTV-DR-CR        PIC 9(1).              \n020196         10  TDB-TDA-ACTV-E-PUBID          PIC X(8).              \n020198         10  TDB-TDA-ACTV-PUB-ID           PIC X(8).              \n020200         10  TDB-TDA-ACTV-SUB-X.                                  \n020202             15  TDB-TDA-ACTV-SUB          PIC 9(3).              \n020204         10  TDB-TDA-ACTV-DATA             PIC X(400).            \n020206                                                                  \n020208         10  TDB-TDA-ACTVT-MONETARY REDEFINES                     \n020210                 TDB-TDA-ACTV-DATA.                               \n020212             15  TDB-TDA-ACTVT-CODE-X.                            \n020214                 20  TDB-TDA-ACTVT-CODE        PIC 9(3).          \n020216             15  TDB-TDA-ACTVT-AMT-X.                             \n020218                 20  TDB-TDA-ACTVT-AMT         PIC S9(12)V99.     \n020220             15  TDB-TDA-ACTVT-DESC            PIC X(80).         \n020222             15  TDB-TDA-ACTVT-DESC-R                             \n020224                 REDEFINES TDB-TDA-ACTVT-DESC.                    \n020226                 20  TDB-TDA-ACTVT-DESC-1      PIC X(40).         \n020228                 20  TDB-TDA-ACTVT-DESC-2      PIC X(40).         \n020230             15  TDB-TDA-ACTVT-UNPOST-X.                          \n020232                 20  TDB-TDA-ACTVT-UNPOST      PIC 9(1).          \n020234             15  TDB-TDA-ACTVT-RATE-X.                            \n020236                 20  TDB-TDA-ACTVT-RATE        PIC 9(2)V999.      \n020238             15  TDB-TDA-ACTVT-YIELD-X.                           \n020240                 20  TDB-TDA-ACTVT-YIELD       PIC 9(2)V999.      \n020242             15  TDB-TDA-ACTVT-P-DIEM-X.                          \n020244                 20  TDB-TDA-ACTVT-P-DIEM      PIC S9(12)V9(6).   \n020246             15  TDB-TDA-ACTVT-WTHLD-X.                           \n020248                 20  TDB-TDA-ACTVT-WTHLD       PIC S9(12)V99.     \n020250             15  TDB-TDA-ACTVT-PENLTY-X.                          \n020252                 20  TDB-TDA-ACTVT-PENLTY      PIC S9(12)V99.     \n020254             15  TDB-TDA-ACTVT-EX-EARN         PIC S9(12)V9(2).   \n020256             15  TDB-TDA-ACTVT-DS-TYPE.                           \n020258               20 TDB-TDA-ACTVT-DS-TYPE-1      PIC X.             \n020260               20 TDB-TDA-ACTVT-DS-TYPE-2      PIC X.             \n020262             15  TDB-TDA-ACTVT-CN-CUST-X.                         \n020264                 20  TDB-TDA-ACTVT-CN-CUST     PIC 9(12).         \n020266             15  TDB-TDA-ACTVT-CN-TYPE-X.                         \n020268                 20  TDB-TDA-ACTVT-CN-TYPE     PIC 9(2).          \n020270             15  TDB-TDA-ACTVT-ST-WHLD-X.                         \n020272                 20  TDB-TDA-ACTVT-ST-WHLD     PIC S9(12)V99.     \n020274             15  TDB-TDA-ACTVT-NEW-BAL-X.                         \n020276                 20  TDB-TDA-ACTVT-NEW-BAL     PIC S9(12)V99.     \n020278             15  TDB-TDA-ACTVT-CHK-NBR-X.                         \n020280                 20  TDB-TDA-ACTVT-CHK-NBR     PIC 9(10).         \n020282             15  TDB-TDA-ACTVT-SEQ-NBR-X.                         \n020284                 20  TDB-TDA-ACTVT-SEQ-NBR     PIC 9(16).         \n020286             15  TDB-TDA-ACTVT-PRIDAY          PIC X.             \n020288             15  TDB-TDA-ACTVT-INT-COR         PIC 9(1).          \n020290             15  TDB-TDA-ACTVT-DISP-CD         PIC 9(1).          \n020292             15  TDB-TDA-ACTVT-QRP-ROL         PIC 9(1).          \n020294             15  FILLER                        PIC X(158).        \n020296                                                                  \n020298         10  TDB-TDA-ACTVC-CHANGE REDEFINES                       \n020300                 TDB-TDA-ACTV-DATA.                               \n020302             15  TDB-TDA-ACTVC-CODE-X.                            \n020304                 20  TDB-TDA-ACTVC-CODE        PIC 9(4).          \n020306             15  TDB-TDA-ACTVC-EXCPT-X.                           \n020308                 20  TDB-TDA-ACTVC-EXCPT       PIC 9(3).          \n020310             15  TDB-TDA-ACTVC-CHG-FRM         PIC X(40).         \n020312             15  TDB-TDA-ACTVC-CHG-TO          PIC X(40).         \n020314             15  TDB-TDA-ACTVC-NCREOPN-X.                         \n020316                 20  TDB-TDA-ACTVC-NCREOPN     PIC 9(1).          \n020318             15  TDB-TDA-ACTVC-DDN             PIC 9(10).         \n020320             15  TDB-TDA-ACTVC-TMPLATE         PIC 9(4).          \n020322             15  FILLER                        PIC X(298).        \n020324                                                                  \n020326         10  TDB-TDA-ACTMT-MAT REDEFINES                          \n020328                 TDB-TDA-ACTV-DATA.                               \n020330             15  TDB-TDA-ACTMT-LMAT-DT         PIC 9(08).         \n020332             15  TDB-TDA-ACTMT-NMAT-DT         PIC 9(08).         \n020334             15  TDB-TDA-ACTMT-TOTL-CD         PIC 9(03).         \n020336             15  TDB-TDA-ACTMT-PMAT-DT         PIC 9(08).         \n020338             15  FILLER                        PIC X(373).        \n020340                                                                  \n020342         10  TDB-TDA-ACTCL-CALC REDEFINES                         \n020344                 TDB-TDA-ACTV-DATA.                               \n020346             15  TDB-TDA-ACTCL-P-DIEM-X.                          \n020348                 20  TDB-TDA-ACTCL-P-DIEM      PIC S9(12)V9(6).   \n020350             15  TDB-TDA-ACTCL-N-DIEM-X.                          \n020352                 20  TDB-TDA-ACTCL-N-DIEM      PIC S9(12)V9(6).   \n020354             15  TDB-TDA-ACTCL-P-ACCR-X.                          \n020356                 20  TDB-TDA-ACTCL-P-ACCR      PIC S9(12)V9(6).   \n020358             15  TDB-TDA-ACTCL-N-ACCR-X.                          \n020360                 20  TDB-TDA-ACTCL-N-ACCR      PIC S9(12)V9(6).   \n020362             15  TDB-TDA-ACTCL-P-ACRDT-X.                         \n020364                 20  TDB-TDA-ACTCL-P-ACRDT     PIC 9(8).          \n020366             15  TDB-TDA-ACTCL-N-ACRDT-X.                         \n020368                 20  TDB-TDA-ACTCL-N-ACRDT     PIC 9(8).          \n020370             15  TDB-TDA-ACTCL-P-WTHLD-X.                         \n020372                 20  TDB-TDA-ACTCL-P-WTHLD     PIC S9(12)V99.     \n020374             15  TDB-TDA-ACTCL-N-WTHLD-X.                         \n020376                 20  TDB-TDA-ACTCL-N-WTHLD     PIC S9(12)V99.     \n020378             15  TDB-TDA-ACTCL-P-PENAL-X.                         \n020380                 20  TDB-TDA-ACTCL-P-PENAL     PIC S9(12)V99.     \n020382             15  TDB-TDA-ACTCL-N-PENAL-X.                         \n020384                 20  TDB-TDA-ACTCL-N-PENAL     PIC S9(12)V99.     \n020386             15  TDB-TDA-ACTCL-P-PAYOF-X.                         \n020388                 20  TDB-TDA-ACTCL-P-PAYOF     PIC S9(12)V99.     \n020390             15  TDB-TDA-ACTCL-N-PAYOF-X.                         \n020392                 20  TDB-TDA-ACTCL-N-PAYOF     PIC S9(12)V99.     \n020394             15  TDB-TDA-ACTCL-ST-P-WD-X.                         \n020396                 20  TDB-TDA-ACTCL-ST-P-WD     PIC S9(12)V99.     \n020398             15  TDB-TDA-ACTCL-ST-N-WD-X.                         \n020400                 20  TDB-TDA-ACTCL-ST-N-WD     PIC S9(12)V99.     \n020402             15  FILLER                        PIC X(200).        \n020404                                                                  \n020406         10  TDB-TDA-ACTHT-HIST REDEFINES                         \n020408                 TDB-TDA-ACTV-DATA.                               \n020410             15  TDB-TDA-ACTHT-DATE-X.                            \n020412                 20  TDB-TDA-ACTHT-DATE        PIC 9(8).          \n020414             15  TDB-TDA-ACTHT-CODE-X.                            \n020416                 20  TDB-TDA-ACTHT-CODE        PIC 9(4).          \n020418             15  TDB-TDA-ACTHT-AMOUNT-X.                          \n020420                 20  TDB-TDA-ACTHT-AMOUNT      PIC S9(12)V99.     \n020422             15  TDB-TDA-ACTHT-TAX-AMT-X.                         \n020424                 20  TDB-TDA-ACTHT-TAX-AMT     PIC S9(12)V99.     \n020426             15  TDB-TDA-ACTHT-FM-RATE-X.                         \n020428                 20  TDB-TDA-ACTHT-FM-RATE     PIC S9(2)V9(3).    \n020430             15  TDB-TDA-ACTHT-FM-DESC         PIC X(26).         \n020432             15  FILLER                        PIC X(329).        \n020434                                                                  \n020436         10  TDB-TDA-ACTVN-NEW  REDEFINES                         \n020438                 TDB-TDA-ACTV-DATA.                               \n020440             15  TDB-TDA-ACTVN-STR-NBR-X.                         \n020442                 20  TDB-TDA-ACTVN-STR-NBR     PIC 9(2).          \n020444             15  TDB-TDA-ACTVN-PUR-AMT-X.                         \n020446                 20  TDB-TDA-ACTVN-PUR-AMT     PIC S9(12)V99.     \n020448             15  TDB-TDA-ACTVN-BASE-RT-X.                         \n020450                 20  TDB-TDA-ACTVN-BASE-RT     PIC S9(2)V9(3).    \n020452             15  TDB-TDA-ACTVN-RT-IND          PIC X(1).          \n020454             15  TDB-TDA-ACTVN-TYPE-X.                            \n020456                 20  TDB-TDA-ACTVN-TYPE        PIC 9(2).          \n020458             15  FILLER                        PIC X(376).        \n020460                                                                  \n020462         10  TDB-TDA-ACTVR-RATE REDEFINES                         \n020464                 TDB-TDA-ACTV-DATA.                               \n020466             15  TDB-TDA-ACTVR-CUR-RT-X.                          \n020468                 20  TDB-TDA-ACTVR-CUR-RT      PIC S99V999.       \n020470             15  TDB-TDA-ACTVR-F-L-RT-X.                          \n020472                 20  TDB-TDA-ACTVR-F-L-RT      PIC S99V999.       \n020474             15  TDB-TDA-ACTVR-T-L-RT-X.                          \n020476                 20  TDB-TDA-ACTVR-T-L-RT      PIC S99V999.       \n020478             15  TDB-TDA-ACTVR-F-Y-RT-X.                          \n020480                 20  TDB-TDA-ACTVR-F-Y-RT      PIC S99V999.       \n020482             15  TDB-TDA-ACTVR-T-Y-RT-X.                          \n020484                 20  TDB-TDA-ACTVR-T-Y-RT      PIC S99V999.       \n020486             15  TDB-TDA-ACTVR-F-L-DT-X.                          \n020488                 20  TDB-TDA-ACTVR-F-L-DT      PIC 9(8).          \n020490             15  TDB-TDA-ACTVR-T-L-DT-X.                          \n020492                 20  TDB-TDA-ACTVR-T-L-DT      PIC 9(8).          \n020494             15  TDB-TDA-ACTVR-F-RCYC-X.                          \n020496                 20  TDB-TDA-ACTVR-F-RCYC      PIC 9(2).          \n020498             15  TDB-TDA-ACTVR-T-RCYC-X.                          \n020500                 20  TDB-TDA-ACTVR-T-RCYC      PIC 9(2).          \n020502             15  TDB-TDA-ACTVR-PRS-DT-X.                          \n020504                 20  TDB-TDA-ACTVR-PRS-DT      PIC 9(8).          \n020506             15  TDB-TDA-ACTVR-RT-IND          PIC X.             \n020508             15  FILLER                        PIC X(346).        \n020510                                                                  \n020512         10  TDB-TDA-ACTRR-RISE REDEFINES                         \n020514                 TDB-TDA-ACTV-DATA.                               \n020516             15  TDB-TDA-ACTRR-F-RG-X.                            \n020518                 20  TDB-TDA-ACTRR-F-RG        PIC 9(2).          \n020520             15  TDB-TDA-ACTRR-T-RG-X.                            \n020522                 20  TDB-TDA-ACTRR-T-RG        PIC 9(2).          \n020524             15  TDB-TDA-ACTRR-F-CD-X.                            \n020526                 20  TDB-TDA-ACTRR-F-CD        PIC 9(2).          \n020528             15  TDB-TDA-ACTRR-T-CD-X.                            \n020530                 20  TDB-TDA-ACTRR-T-CD        PIC 9(2).          \n020532             15  TDB-TDA-ACTRR-TABLE         OCCURS 10 TIMES.     \n020534                 20  TDB-TDA-ACTRR-F-RT-X.                        \n020536                         30  TDB-TDA-ACTRR-F-RT    PIC S99V999.   \n020538                 20  TDB-TDA-ACTRR-T-RT-X.                        \n020540                         30  TDB-TDA-ACTRR-T-RT    PIC S99V999.   \n020542                 20  TDB-TDA-ACTRR-F-DT-X.                        \n020544                         30  TDB-TDA-ACTRR-F-DT    PIC 9(8).      \n020546                 20  TDB-TDA-ACTRR-T-DT-X.                        \n020548                         30  TDB-TDA-ACTRR-T-DT    PIC 9(8).      \n020550             15  FILLER                        PIC X(132).        \n020552                                                                  \n020554         10  TDB-TDA-ACTVI-INTEREST REDEFINES                     \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    371 lines from 9903 to 10273.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 20, "total_chunks": 55, "start_line": 9903, "end_line": 10273, "line_count": 371}

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
- Source code length: 32039 characters

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
CHUNK 20 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 9903 to 10273 (371 lines)
Chunk Tokens (estimated): ~7,914
Actual Input Tokens: 9,320 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 9903-10273 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 20 of 55 chunks
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
      The source code below is only CHUNK 20 of 55.


=============================================================================
CHUNK 20 SOURCE CODE (Lines 9903-10273)
=============================================================================

```cobol
019814                          TDB-TDAA-MANUAL-RT-X.                   
019816                 20  TDB-TDAA-MAN-RATE     PIC 9(2)V9(3).         
019818                                                                  
019820     05  TDB-TDAIRA.                                              
019822         10  TDB-TDAI-BANK-X.                                     
019824             15  TDB-TDAI-BANK             PIC 9(4).              
019826         10  TDB-TDAI-BRCH-X.                                     
019828             15  TDB-TDAI-BRCH             PIC 9(4).              
019830         10  TDB-TDAI-APPL-X.                                     
019832             15  TDB-TDAI-APPL             PIC 9(1).              
019834         10  TDB-TDAI-CUST-X.                                     
019836             15  TDB-TDAI-CUST             PIC 9(12).             
019838         10  TDB-TDAI-ACCT-X.                                     
019840             15  TDB-TDAI-ACCT             PIC 9(10).             
019842         10  TDB-TDAI-PUB-ID               PIC X(8).              
019844         10  TDB-TDAI-ADD-DT-X.                                   
019846             15  TDB-TDAI-ADD-DT           PIC 9(8).              
019848         10  TDB-TDAI-ADD-TM-X.                                   
019850             15  TDB-TDAI-ADD-TM           PIC 9(6).              
019852         10  TDB-TDAI-DS-TYPE              PIC X(2)               
019854                          OCCURS 20 TIMES.                        
019856         10  TDB-TDAI-CN-TYPE-X.                                  
019858             15  TDB-TDAI-CN-TYPE          PIC 9(2)               
019860                          OCCURS 20 TIMES.                        
019862         10  TDB-TDAI-DS-CN-AMT-X.                                
019864             15  TDB-TDAI-DS-CN-AMT        PIC S9(12)V99          
019866                          OCCURS 20 TIMES.                        
019868         10  TDB-TDAI-DS-PEN-AMT-X.                               
019870             15  TDB-TDAI-DS-PEN-AMT       PIC S9(12)V99          
019872                          OCCURS 20 TIMES.                        
019874         10  TDB-TDAI-DS-WTHLD-AMT-X.                             
019876             15  TDB-TDAI-DS-WTHLD-AMT     PIC S9(12)V99          
019878                          OCCURS 20 TIMES.                        
019880         10  TDB-TDAI-DS-ST-WH-AMT-X.                             
019882             15  TDB-TDAI-DS-ST-WH-AMT     PIC S9(12)V99          
019884                          OCCURS 20 TIMES.                        
019886         10  TDB-TDAI-DS-EXC-EARN          PIC S9(12)V9(2)        
019888                          OCCURS 20 TIMES.                        
019890         10  TDB-TDAI-DS-C-YTD-CNT-X.                             
019892             15  TDB-TDAI-DS-C-YTD-CNT     PIC 9(5).              
019894         10  TDB-TDAI-DS-P-YTD-CNT-X.                             
019896             15  TDB-TDAI-DS-P-YTD-CNT     PIC 9(5).              
019898         10  TDB-TDAI-DS-AMT-C-YTD-X.                             
019900             15  TDB-TDAI-DS-AMT-C-YTD     PIC S9(12)V9(2).       
019902         10  TDB-TDAI-DS-AMT-P-YTD-X.                             
019904             15  TDB-TDAI-DS-AMT-P-YTD     PIC S9(12)V9(2).       
019906         10  TDB-TDAI-DS-INT-AMT-X.                               
019908             15  TDB-TDAI-DS-INT-AMT       PIC S9(12)V9(2).       
019910         10  TDB-TDAI-CN-YTD-CNT-X.                               
019912             15  TDB-TDAI-CN-YTD-CNT       PIC 9(5).              
019914         10  TDB-TDAI-CN-YTD-AMT-X.                               
019916             15  TDB-TDAI-CN-YTD-AMT       PIC S9(12)V9(2).       
019918         10  TDB-TDAI-CN-LYTD-AMT-X.                              
019920             15  TDB-TDAI-CN-LYTD-AMT      PIC S9(12)V9(2).       
019922         10  TDB-TDAI-EMP-CONT-LYR-X.                             
019924             15  TDB-TDAI-EMP-CONT-LYR     PIC S9(12)V9(2).       
019926         10  TDB-TDAI-REG-CONT-LYR-X.                             
019928             15  TDB-TDAI-REG-CONT-LYR     PIC S9(12)V9(2).       
019930         10  TDB-TDAI-UNINSURED            PIC X(1).              
019932         10  TDB-TDAI-ROLLOVER-X.                                 
019934             15  TDB-TDAI-ROLLOVER         PIC S9(12)V9(2).       
019936         10  TDB-TDAI-ROLLOVER-LYR-X.                             
019938             15  TDB-TDAI-ROLLOVER-LYR     PIC S9(12)V9(2).       
019940         10  TDB-TDAI-TRANSFER-IN-X.                              
019942             15  TDB-TDAI-TRANSFER-IN      PIC S9(12)V9(2).       
019944         10  TDB-TDAI-TRANSFER-OUT-X.                             
019946             15  TDB-TDAI-TRANSFER-OUT     PIC S9(12)V9(2).       
019948         10  TDB-TDAI-1ST-CN-DATE-X.                              
019950             15  TDB-TDAI-1ST-CN-DATE      PIC 9(8).              
019952         10  TDB-TDAI-BASIS-C-LTD-X.                              
019954             15  TDB-TDAI-BASIS-C-LTD      PIC S9(12)V99.         
019956         10  TDB-TDAI-BASIS-D-LTD-X.                              
019958             15  TDB-TDAI-BASIS-D-LTD      PIC S9(12)V99.         
019960         10  TDB-TDAI-BASIS-D-YTD-X.                              
019962             15  TDB-TDAI-BASIS-D-YTD      PIC S9(12)V99.         
019964                                                                  
019966         10  TDB-TDAI-NONDB-FIELDS.                               
019968             15  TDB-TDAI-CN-TYPE-EX       PIC 9(2).              
019970             15  TDB-TDAI-CN-TYPE-R REDEFINES TDB-TDAI-CN-TYPE-EX.
019972                 20  TDB-TDAI-CN-TYPE-EX-1 PIC X.                 
019974                 20  TDB-TDAI-CN-TYPE-EX-2 PIC X.                 
019976             15  TDB-TDAI-DS-TYPE-EX.                             
019978                20  TDB-TDAI-DS-TYPE-EX-1      PIC X.             
019980                20  TDB-TDAI-DS-TYPE-EX-2      PIC X.             
019982                                                                  
019984      05 TDB-TDADISTR.                                            
019986         10 TDB-TDAD-BANK                      PIC 9(04).         
019988         10 TDB-TDAD-BRCH                      PIC 9(04).         
019990         10 TDB-TDAD-APPL                      PIC 9(01).         
019992         10 TDB-TDAD-CUST                      PIC 9(12).         
019994         10 TDB-TDAD-ACCT                      PIC 9(10).         
019996         10 TDB-TDAD-NXT-ACCT-P                PIC 9(10).         
019998         10 TDB-TDAD-NXT-ACCT-S                PIC 9(10).         
020000         10 TDB-TDAD-N-ACCT-BY-RT              PIC 9(1).          
020002         10 TDB-TDAD-SERIAL                    PIC 9(12).         
020004         10 TDB-TDAD-SER-NEXT                  PIC 9(12).         
020006         10 TDB-TDAD-DISP-CD                   PIC 9(01).         
020008         10 TDB-TDAD-TYPE                      PIC X(02).         
020010         10 TDB-TDAD-PRINCIPAL                 PIC 9(01).         
020012         10 TDB-TDAD-INTEREST                  PIC 9(01).         
020014         10 TDB-TDAD-DS-CODE                   PIC 9(01).         
020016         10 TDB-TDAD-WTHLD-CD                  PIC 9(01).         
020018         10 TDB-TDAD-WHLD-AMT                  PIC S9(12)V99.     
020020         10 TDB-TDAD-ST-WHLD-CD                PIC 9(01).         
020022         10 TDB-TDAD-ST-WHLD-AMT               PIC S9(12)V99.     
020024         10 TDB-TDAD-TRF-ACCT                  PIC 9(12).         
020026         10 TDB-TDAD-TRF-ACCT-S                PIC 9(10).         
020028         10 TDB-TDAD-AMT-CD                    PIC 9(01).         
020030         10 TDB-TDAD-DS-AMT                    PIC S9(12)V99.     
020032         10 TDB-TDAD-DS-FREQ                   PIC 9(01).         
020034         10 TDB-TDAD-DS-NTRVL                  PIC 9(04).         
020036         10 TDB-TDAD-END-OF-DIST-X.                               
020038            15  TDB-TDAD-END-OF-DIST           PIC 9(1).          
020040         10 TDB-TDAD-DIST-NTC-CD               PIC 9(01).         
020042         10 TDB-TDAD-EOY-DS-FORM               PIC 9(01).         
020044         10 TDB-TDAD-5-YR-RULE                 PIC 9(01).         
020046         10 TDB-TDAD-ANUAL-RECALC              PIC 9(01).         
020048         10 TDB-TDAD-JOINT-CD                  PIC 9(01).         
020050         10 TDB-TDAD-PUB-ID                    PIC X(08).         
020052         10 TDB-TDAD-LST-DIST-DT               PIC 9(08).         
020054         10 TDB-TDAD-IN-PROC-DT                PIC 9(8).          
020056         10 TDB-TDAD-NXT-DIST-DT               PIC 9(08).         
020058         10 TDB-TDAD-NXT-DS-PROC               PIC 9(08).         
020060         10 TDB-TDAD-ADD-DT                    PIC 9(08).         
020062         10 TDB-TDAD-ADD-TM                    PIC 9(08).         
020064                                                                  
020066         10 TDB-TDAD-MIN-AMT                   PIC S9(12)V99.     
020068         10 TDB-TDAD-AMT                       PIC S9(12)V99.     
020070         10 TDB-TDAD-LST-AMT                   PIC S9(12)V99.     
020072         10 TDB-TDAD-CUR-WHLD-AMT              PIC S9(12)V99.     
020074         10 TDB-TDAD-WHLD-YTD                  PIC S9(12)V99.     
020076         10 TDB-TDAD-LST-WHLD-AMT              PIC S9(12)V99.     
020078         10 TDB-TDAD-PRINCPL-AMT               PIC S9(12)V99.     
020080         10 TDB-TDAD-INT-AMT                   PIC S9(12)V99.     
020082         10 TDB-TDAD-INT-YTD                   PIC S9(12)V99.     
020084         10 TDB-TDAD-ST-CUR-W-AMT              PIC S9(12)V99.     
020086         10 TDB-TDAD-ST-LST-W-AMT              PIC S9(12)V99.     
020088         10 TDB-TDAD-CK-IND-1                  PIC X(1).          
020090         10 TDB-TDAD-CK-IND-2                  PIC X(1).          
020092         10 TDB-TDAD-LUPD-DT                   PIC 9(8).          
020094         10 TDB-TDAD-LUPD-TM                   PIC 9(6).          
020096         10 TDB-TDAD-RMD-OVERRIDE-X.                              
020098            15 TDB-TDAD-RMD-OVERRIDE           PIC 9.             
020100         10 TDB-TDAD-RMD-AMOUNT-X.                                
020102            15 TDB-TDAD-RMD-AMOUNT             PIC S9(12)V9(2).   
020104         10 TDB-TDAD-DS-NBR-X.                                    
020106            15 TDB-TDAD-DS-NBR                 PIC 9(2).          
020108                                                                  
020110         10  TDB-TDAD-NONDB-FIELDS.                               
020112             15  TDB-TDAD-DS-NTC-TYPE          PIC 9(1).          
020114                                                                  
020116     05  TDB-TDAACTV.                                             
020118         10  TDB-TDA-ACTV-BANK-X.                                 
020120             15  TDB-TDA-ACTV-BANK         PIC 9(4).              
020122         10  TDB-TDA-ACTV-BRCH-X.                                 
020124             15  TDB-TDA-ACTV-BRCH         PIC 9(4).              
020126         10  TDB-TDA-ACTV-APPL-X.                                 
020128             15  TDB-TDA-ACTV-APPL         PIC 9(1).              
020130         10  TDB-TDA-ACTV-CUST-X.                                 
020132             15  TDB-TDA-ACTV-CUST         PIC 9(12).             
020134         10  TDB-TDA-ACTV-ACCT-X.                                 
020136             15  TDB-TDA-ACTV-ACCT         PIC 9(10).             
020138         10  TDB-TDA-ACTV-TOT-CD-X.                               
020140             15  TDB-TDA-ACTV-TOT-CD       PIC 9(3).              
020142         10  TDB-TDA-ACTV-IGL-GRP-X.                              
020144             15  TDB-TDA-ACTV-IGL-GRP      PIC 9(2).              
020146         10  TDB-TDA-ACTV-OFFICER          PIC X(3).              
020148         10  TDB-TDA-ACTV-NC-INDC-X.                              
020150             15  TDB-TDA-ACTV-NC-INDC      PIC 9(1).              
020152         10  TDB-TDA-ACTV-PROC-FG-X.                              
020154             15  TDB-TDA-ACTV-PROC-FG      PIC 9(1).              
020156         10  TDB-TDA-ACTV-TYPE-X.                                 
020158             15  TDB-TDA-ACTV-TYPE         PIC 9(4).              
020160         10  TDB-TDA-ACTV-EFF-DT-X.                               
020162             15  TDB-TDA-ACTV-EFF-DT       PIC 9(8).              
020164         10  TDB-TDA-ACTV-DATE-X.                                 
020166             15  TDB-TDA-ACTV-DATE         PIC 9(8).              
020168         10  TDB-TDA-ACTV-MAINT-X.                                
020170             15  TDB-TDA-ACTV-MAINT        PIC 9(8).              
020172         10  TDB-TDA-ACTV-TIME-X.                                 
020174             15  TDB-TDA-ACTV-TIME         PIC 9(8).              
020176         10  TDB-TDA-ACTV-SEQ-NBR-X.                              
020178             15  TDB-TDA-ACTV-SEQ-NBR      PIC 9(2).              
020180         10  TDB-TDA-ACTV-SERIAL-X.                               
020182             15  TDB-TDA-ACTV-SERIAL       PIC 9(12).             
020184         10  TDB-TDA-ACTV-SOURCE-X.                               
020186             15  TDB-TDA-ACTV-SOURCE       PIC 9(2).              
020188         10  TDB-TDA-ACTV-ERASED-X.                               
020190             15  TDB-TDA-ACTV-ERASED       PIC 9(1).              
020192         10  TDB-TDA-ACTV-DR-CR-X.                                
020194             15  TDB-TDA-ACTV-DR-CR        PIC 9(1).              
020196         10  TDB-TDA-ACTV-E-PUBID          PIC X(8).              
020198         10  TDB-TDA-ACTV-PUB-ID           PIC X(8).              
020200         10  TDB-TDA-ACTV-SUB-X.                                  
020202             15  TDB-TDA-ACTV-SUB          PIC 9(3).              
020204         10  TDB-TDA-ACTV-DATA             PIC X(400).            
020206                                                                  
020208         10  TDB-TDA-ACTVT-MONETARY REDEFINES                     
020210                 TDB-TDA-ACTV-DATA.                               
020212             15  TDB-TDA-ACTVT-CODE-X.                            
020214                 20  TDB-TDA-ACTVT-CODE        PIC 9(3).          
020216             15  TDB-TDA-ACTVT-AMT-X.                             
020218                 20  TDB-TDA-ACTVT-AMT         PIC S9(12)V99.     
020220             15  TDB-TDA-ACTVT-DESC            PIC X(80).         
020222             15  TDB-TDA-ACTVT-DESC-R                             
020224                 REDEFINES TDB-TDA-ACTVT-DESC.                    
020226                 20  TDB-TDA-ACTVT-DESC-1      PIC X(40).         
020228                 20  TDB-TDA-ACTVT-DESC-2      PIC X(40).         
020230             15  TDB-TDA-ACTVT-UNPOST-X.                          
020232                 20  TDB-TDA-ACTVT-UNPOST      PIC 9(1).          
020234             15  TDB-TDA-ACTVT-RATE-X.                            
020236                 20  TDB-TDA-ACTVT-RATE        PIC 9(2)V999.      
020238             15  TDB-TDA-ACTVT-YIELD-X.                           
020240                 20  TDB-TDA-ACTVT-YIELD       PIC 9(2)V999.      
020242             15  TDB-TDA-ACTVT-P-DIEM-X.                          
020244                 20  TDB-TDA-ACTVT-P-DIEM      PIC S9(12)V9(6).   
020246             15  TDB-TDA-ACTVT-WTHLD-X.                           
020248                 20  TDB-TDA-ACTVT-WTHLD       PIC S9(12)V99.     
020250             15  TDB-TDA-ACTVT-PENLTY-X.                          
020252                 20  TDB-TDA-ACTVT-PENLTY      PIC S9(12)V99.     
020254             15  TDB-TDA-ACTVT-EX-EARN         PIC S9(12)V9(2).   
020256             15  TDB-TDA-ACTVT-DS-TYPE.                           
020258               20 TDB-TDA-ACTVT-DS-TYPE-1      PIC X.             
020260               20 TDB-TDA-ACTVT-DS-TYPE-2      PIC X.             
020262             15  TDB-TDA-ACTVT-CN-CUST-X.                         
020264                 20  TDB-TDA-ACTVT-CN-CUST     PIC 9(12).         
020266             15  TDB-TDA-ACTVT-CN-TYPE-X.                         
020268                 20  TDB-TDA-ACTVT-CN-TYPE     PIC 9(2).          
020270             15  TDB-TDA-ACTVT-ST-WHLD-X.                         
020272                 20  TDB-TDA-ACTVT-ST-WHLD     PIC S9(12)V99.     
020274             15  TDB-TDA-ACTVT-NEW-BAL-X.                         
020276                 20  TDB-TDA-ACTVT-NEW-BAL     PIC S9(12)V99.     
020278             15  TDB-TDA-ACTVT-CHK-NBR-X.                         
020280                 20  TDB-TDA-ACTVT-CHK-NBR     PIC 9(10).         
020282             15  TDB-TDA-ACTVT-SEQ-NBR-X.                         
020284                 20  TDB-TDA-ACTVT-SEQ-NBR     PIC 9(16).         
020286             15  TDB-TDA-ACTVT-PRIDAY          PIC X.             
020288             15  TDB-TDA-ACTVT-INT-COR         PIC 9(1).          
020290             15  TDB-TDA-ACTVT-DISP-CD         PIC 9(1).          
020292             15  TDB-TDA-ACTVT-QRP-ROL         PIC 9(1).          
020294             15  FILLER                        PIC X(158).        
020296                                                                  
020298         10  TDB-TDA-ACTVC-CHANGE REDEFINES                       
020300                 TDB-TDA-ACTV-DATA.                               
020302             15  TDB-TDA-ACTVC-CODE-X.                            
020304                 20  TDB-TDA-ACTVC-CODE        PIC 9(4).          
020306             15  TDB-TDA-ACTVC-EXCPT-X.                           
020308                 20  TDB-TDA-ACTVC-EXCPT       PIC 9(3).          
020310             15  TDB-TDA-ACTVC-CHG-FRM         PIC X(40).         
020312             15  TDB-TDA-ACTVC-CHG-TO          PIC X(40).         
020314             15  TDB-TDA-ACTVC-NCREOPN-X.                         
020316                 20  TDB-TDA-ACTVC-NCREOPN     PIC 9(1).          
020318             15  TDB-TDA-ACTVC-DDN             PIC 9(10).         
020320             15  TDB-TDA-ACTVC-TMPLATE         PIC 9(4).          
020322             15  FILLER                        PIC X(298).        
020324                                                                  
020326         10  TDB-TDA-ACTMT-MAT REDEFINES                          
020328                 TDB-TDA-ACTV-DATA.                               
020330             15  TDB-TDA-ACTMT-LMAT-DT         PIC 9(08).         
020332             15  TDB-TDA-ACTMT-NMAT-DT         PIC 9(08).         
020334             15  TDB-TDA-ACTMT-TOTL-CD         PIC 9(03).         
020336             15  TDB-TDA-ACTMT-PMAT-DT         PIC 9(08).         
020338             15  FILLER                        PIC X(373).        
020340                                                                  
020342         10  TDB-TDA-ACTCL-CALC REDEFINES                         
020344                 TDB-TDA-ACTV-DATA.                               
020346             15  TDB-TDA-ACTCL-P-DIEM-X.                          
020348                 20  TDB-TDA-ACTCL-P-DIEM      PIC S9(12)V9(6).   
020350             15  TDB-TDA-ACTCL-N-DIEM-X.                          
020352                 20  TDB-TDA-ACTCL-N-DIEM      PIC S9(12)V9(6).   
020354             15  TDB-TDA-ACTCL-P-ACCR-X.                          
020356                 20  TDB-TDA-ACTCL-P-ACCR      PIC S9(12)V9(6).   
020358             15  TDB-TDA-ACTCL-N-ACCR-X.                          
020360                 20  TDB-TDA-ACTCL-N-ACCR      PIC S9(12)V9(6).   
020362             15  TDB-TDA-ACTCL-P-ACRDT-X.                         
020364                 20  TDB-TDA-ACTCL-P-ACRDT     PIC 9(8).          
020366             15  TDB-TDA-ACTCL-N-ACRDT-X.                         
020368                 20  TDB-TDA-ACTCL-N-ACRDT     PIC 9(8).          
020370             15  TDB-TDA-ACTCL-P-WTHLD-X.                         
020372                 20  TDB-TDA-ACTCL-P-WTHLD     PIC S9(12)V99.     
020374             15  TDB-TDA-ACTCL-N-WTHLD-X.                         
020376                 20  TDB-TDA-ACTCL-N-WTHLD     PIC S9(12)V99.     
020378             15  TDB-TDA-ACTCL-P-PENAL-X.                         
020380                 20  TDB-TDA-ACTCL-P-PENAL     PIC S9(12)V99.     
020382             15  TDB-TDA-ACTCL-N-PENAL-X.                         
020384                 20  TDB-TDA-ACTCL-N-PENAL     PIC S9(12)V99.     
020386             15  TDB-TDA-ACTCL-P-PAYOF-X.                         
020388                 20  TDB-TDA-ACTCL-P-PAYOF     PIC S9(12)V99.     
020390             15  TDB-TDA-ACTCL-N-PAYOF-X.                         
020392                 20  TDB-TDA-ACTCL-N-PAYOF     PIC S9(12)V99.     
020394             15  TDB-TDA-ACTCL-ST-P-WD-X.                         
020396                 20  TDB-TDA-ACTCL-ST-P-WD     PIC S9(12)V99.     
020398             15  TDB-TDA-ACTCL-ST-N-WD-X.                         
020400                 20  TDB-TDA-ACTCL-ST-N-WD     PIC S9(12)V99.     
020402             15  FILLER                        PIC X(200).        
020404                                                                  
020406         10  TDB-TDA-ACTHT-HIST REDEFINES                         
020408                 TDB-TDA-ACTV-DATA.                               
020410             15  TDB-TDA-ACTHT-DATE-X.                            
020412                 20  TDB-TDA-ACTHT-DATE        PIC 9(8).          
020414             15  TDB-TDA-ACTHT-CODE-X.                            
020416                 20  TDB-TDA-ACTHT-CODE        PIC 9(4).          
020418             15  TDB-TDA-ACTHT-AMOUNT-X.                          
020420                 20  TDB-TDA-ACTHT-AMOUNT      PIC S9(12)V99.     
020422             15  TDB-TDA-ACTHT-TAX-AMT-X.                         
020424                 20  TDB-TDA-ACTHT-TAX-AMT     PIC S9(12)V99.     
020426             15  TDB-TDA-ACTHT-FM-RATE-X.                         
020428                 20  TDB-TDA-ACTHT-FM-RATE     PIC S9(2)V9(3).    
020430             15  TDB-TDA-ACTHT-FM-DESC         PIC X(26).         
020432             15  FILLER                        PIC X(329).        
020434                                                                  
020436         10  TDB-TDA-ACTVN-NEW  REDEFINES                         
020438                 TDB-TDA-ACTV-DATA.                               
020440             15  TDB-TDA-ACTVN-STR-NBR-X.                         
020442                 20  TDB-TDA-ACTVN-STR-NBR     PIC 9(2).          
020444             15  TDB-TDA-ACTVN-PUR-AMT-X.                         
020446                 20  TDB-TDA-ACTVN-PUR-AMT     PIC S9(12)V99.     
020448             15  TDB-TDA-ACTVN-BASE-RT-X.                         
020450                 20  TDB-TDA-ACTVN-BASE-RT     PIC S9(2)V9(3).    
020452             15  TDB-TDA-ACTVN-RT-IND          PIC X(1).          
020454             15  TDB-TDA-ACTVN-TYPE-X.                            
020456                 20  TDB-TDA-ACTVN-TYPE        PIC 9(2).          
020458             15  FILLER                        PIC X(376).        
020460                                                                  
020462         10  TDB-TDA-ACTVR-RATE REDEFINES                         
020464                 TDB-TDA-ACTV-DATA.                               
020466             15  TDB-TDA-ACTVR-CUR-RT-X.                          
020468                 20  TDB-TDA-ACTVR-CUR-RT      PIC S99V999.       
020470             15  TDB-TDA-ACTVR-F-L-RT-X.                          
020472                 20  TDB-TDA-ACTVR-F-L-RT      PIC S99V999.       
020474             15  TDB-TDA-ACTVR-T-L-RT-X.                          
020476                 20  TDB-TDA-ACTVR-T-L-RT      PIC S99V999.       
020478             15  TDB-TDA-ACTVR-F-Y-RT-X.                          
020480                 20  TDB-TDA-ACTVR-F-Y-RT      PIC S99V999.       
020482             15  TDB-TDA-ACTVR-T-Y-RT-X.                          
020484                 20  TDB-TDA-ACTVR-T-Y-RT      PIC S99V999.       
020486             15  TDB-TDA-ACTVR-F-L-DT-X.                          
020488                 20  TDB-TDA-ACTVR-F-L-DT      PIC 9(8).          
020490             15  TDB-TDA-ACTVR-T-L-DT-X.                          
020492                 20  TDB-TDA-ACTVR-T-L-DT      PIC 9(8).          
020494             15  TDB-TDA-ACTVR-F-RCYC-X.                          
020496                 20  TDB-TDA-ACTVR-F-RCYC      PIC 9(2).          
020498             15  TDB-TDA-ACTVR-T-RCYC-X.                          
020500                 20  TDB-TDA-ACTVR-T-RCYC      PIC 9(2).          
020502             15  TDB-TDA-ACTVR-PRS-DT-X.                          
020504                 20  TDB-TDA-ACTVR-PRS-DT      PIC 9(8).          
020506             15  TDB-TDA-ACTVR-RT-IND          PIC X.             
020508             15  FILLER                        PIC X(346).        
020510                                                                  
020512         10  TDB-TDA-ACTRR-RISE REDEFINES                         
020514                 TDB-TDA-ACTV-DATA.                               
020516             15  TDB-TDA-ACTRR-F-RG-X.                            
020518                 20  TDB-TDA-ACTRR-F-RG        PIC 9(2).          
020520             15  TDB-TDA-ACTRR-T-RG-X.                            
020522                 20  TDB-TDA-ACTRR-T-RG        PIC 9(2).          
020524             15  TDB-TDA-ACTRR-F-CD-X.                            
020526                 20  TDB-TDA-ACTRR-F-CD        PIC 9(2).          
020528             15  TDB-TDA-ACTRR-T-CD-X.                            
020530                 20  TDB-TDA-ACTRR-T-CD        PIC 9(2).          
020532             15  TDB-TDA-ACTRR-TABLE         OCCURS 10 TIMES.     
020534                 20  TDB-TDA-ACTRR-F-RT-X.                        
020536                         30  TDB-TDA-ACTRR-F-RT    PIC S99V999.   
020538                 20  TDB-TDA-ACTRR-T-RT-X.                        
020540                         30  TDB-TDA-ACTRR-T-RT    PIC S99V999.   
020542                 20  TDB-TDA-ACTRR-F-DT-X.                        
020544                         30  TDB-TDA-ACTRR-F-DT    PIC 9(8).      
020546                 20  TDB-TDA-ACTRR-T-DT-X.                        
020548                         30  TDB-TDA-ACTRR-T-DT    PIC 9(8).      
020550             15  FILLER                        PIC X(132).        
020552                                                                  
020554         10  TDB-TDA-ACTVI-INTEREST REDEFINES                     
```

⚠️  This is the source code you must document.
    371 lines from 9903 to 10273.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

