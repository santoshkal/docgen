# LLM Request Debug File
Generated: 2025-11-17T20:23:57.209638

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 13/55
- **Model**: gpt-4.1
- **Chunk Number**: 13
- **Pass Number**: 3
- **Attempt Number**: 5 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,146 tokens
- **User Prompt**: ~4,806 tokens
- **Total Input**: ~6,952 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 13/55" (ID: detailed-code-explanation)

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

**RETRY REQUIRED - Previous attempt had 87.2% coverage**
You missed 19 executable lines.

🚨 ANALYSIS: This chunk has 149 executable lines (excluding 0 comments/page-breaks).
You returned 130 lines. You're missing 19 executable lines.

COMMON ISSUES:
- Skipping repetitive FILLER definitions (FORBIDDEN!)
- Summarizing data tables with "..." (FORBIDDEN!)
- Omitting "boring" sections for brevity (FORBIDDEN!)
- Using phrases like "similar pattern continues" (FORBIDDEN!)

YOU MUST:
- Include EVERY executable line with its sequence number
- Show ALL FILLERs even if there are 500+ repetitive ones
- Show ALL data table entries completely
- Never use abbreviation, summarization, or ellipsis
- Include complete WORKING-STORAGE and FILE SECTION layouts

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


**CHUNK 13 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-17T19:50:50.832678", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 13 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 6106 to 6254 (149 lines)\nChunk Tokens (estimated): ~2,637\nActual Input Tokens: 4,043 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 6106-6254 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 13 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 13 of 55.\n\n\n=============================================================================\nCHUNK 13 SOURCE CODE (Lines 6106-6254)\n=============================================================================\n\n```cobol\n012220        OLD-ADDR-TEMP-EMAIL.                                      \n012222        10 OLD-ADDR-TEMP-EMAIL-1  PIC X(40).                      \n012224        10 OLD-ADDR-TEMP-EMAIL-2  PIC X(40).                      \n012226        10 OLD-ADDR-TEMP-EMAIL-3  PIC X(20).                      \n012228                                                                  \n012230     05 WS-TDH-AREA.                                              \n012232       10 WS-TDH-SOURCE          PIC 9(02) VALUE 0.               \n012234       10 WS-TDH-ERROR           PIC 9(04) VALUE 0.               \n012236       10 WS-TDH-BORROWER-NO     PIC 9(12) VALUE 0.               \n012238       10 WS-TDH-NOTE-NO         PIC 9(10) VALUE 0.               \n012240       10 FILLER                 PIC X(72) VALUE SPACES.          \n012242                                                                  \n012244     05  ACCTB-OLD-ERROR         PIC 9(04).                       \n012246     05  ERASE-TARGET-KEYS.                                       \n012248         10  ERASE-TARG-BANK     PIC 9(04).                       \n012250         10  ERASE-TARG-DATE     PIC 9(08).                       \n012252         10  ERASE-TARG-CUST     PIC 9(12).                       \n012254         10  ERASE-TARG-ACCT     PIC 9(10).                       \n012256         10  ERASE-TARG-TIME     PIC 9(08).                       \n012258         10  ERASE-TARG-SEQ-NBR  PIC 9(02).                       \n012260     05  ERASE2-TARGET-KEYS.                                      \n012262         10  ERASE2-TARG-BANK     PIC 9(04).                      \n012264         10  ERASE2-TARG-DATE     PIC 9(08).                      \n012266         10  ERASE2-TARG-CUST     PIC 9(12).                      \n012268         10  ERASE2-TARG-ACCT     PIC 9(10).                      \n012270         10  ERASE2-TARG-TIME     PIC 9(08).                      \n012272         10  ERASE2-TARG-SEQ-NBR  PIC 9(02).                      \n012274                                                                  \n012276     05  WS-ERASER-IRA-WARN       PIC 9(01).                      \n012278     05  WS-APPLY-ALT             PIC 9     VALUE 0.              \n012280     05  WS-EMAIL-COUNT           PIC 9     VALUE 0.              \n012282                                                                  \n012284                                                                  \n012286                                                                  \n012288     05  PROCESS-DATE             PIC 9(08) VALUE 0.              \n012290     05  PROCESS-DATE-R REDEFINES PROCESS-DATE.                   \n012292         10  PROCESS-DATE-CCYY    PIC 9(04).                      \n012294         10  PROCESS-DATE-CCYY-R REDEFINES PROCESS-DATE-CCYY.     \n012296             15  PROCESS-DATE-CC  PIC 99.                         \n012298             15  PROCESS-DATE-YY  PIC 99.                         \n012300         10  PROCESS-DATE-MMDD    PIC 9(04).                      \n012302         10  PROCESS-DATE-MMDD-R REDEFINES PROCESS-DATE-MMDD.     \n012304             15  PROCESS-DATE-MM  PIC 99.                         \n012306             15  PROCESS-DATE-DD  PIC 99.                         \n012308                                                                  \n012310     05  EFFECTIVE-DATE           PIC 9(08) VALUE 0.              \n012312     05  EFFECTIVE-DATE-R REDEFINES EFFECTIVE-DATE.               \n012314         10  EFFECTIVE-DATE-CY    PIC 9(04).                      \n012316         10  EFFECTIVE-DATE-CY-R REDEFINES EFFECTIVE-DATE-CY.     \n012318             15 EFFECTIVE-DATE-C  PIC 99.                         \n012320             15 EFFECTIVE-DATE-Y  PIC 99.                         \n012322         10  EFFECTIVE-DATE-MD    PIC 9(04).                      \n012324         10  EFFECTIVE-DATE-MD-R REDEFINES EFFECTIVE-DATE-MD.     \n012326             15  EFFECTIVE-DATE-M PIC 99.                         \n012328             15  EFFECTIVE-DATE-D PIC 99.                         \n012330                                                                  \n012332     05  WS-IND                   PIC 9     VALUE 0.              \n012334     05  WS-MISSED-EVENT          PIC 9     VALUE 0.              \n012336                                                                  \n012338     05  WS-LAST-DAY-LIST         PIC X(24)                       \n012340                                VALUE \"312831303130313130313031\". \n012342     05  WS-LAST-DAY-R  REDEFINES  WS-LAST-DAY-LIST.              \n012344         10  WS-LAST-DAY              OCCURS 12 TIMES             \n012346                                  PIC 9(2).                       \n012348                                                                  \n012350     05  WS-DAY-OF-WEEK-LIST      VALUE                           \n012352                                      \"SUNMONTUEWEDTHUFRISAT\".    \n012354         10  WS-DAY-OF-WEEK       OCCURS 07 TIMES                 \n012356                                  PIC X(03).                      \n012358                                                                  \n012360     05  WS-IRA-CONTR-OVR-LIMIT   PIC S9(09)V99.                  \n012362     05  WS-IRA-TOTAL-CONTR       PIC S9(09)V99.                  \n012364     05  WS-IRA-CONTR-LIMIT-AMT   PIC S9(09)V99.                  \n012366                                                                  \n012368     05  WS-MONETARY-FIELDS.                                      \n012370         10  WS-MONETARY-AMT      PIC S9(09)V99.                  \n012372         10  WS-MONETARY-RT       PIC 9(2)V9(3).                  \n012374         10  WS-MONETARY-DESC     PIC X(50).                      \n012376         10  WS-MONETARY-FLAG     PIC 9.                          \n012378                                                                  \n012380     05  WS-FUNCTION-CD           PIC 99 VALUE 0.                 \n012382                                                                  \n012384     05  WS-PAGE-FIELDS.                                          \n012386         10  WS-PAGE-COUNT        PIC 99.                         \n012388                                                                  \n012390     05  REPORT-FIELDS.                                           \n012392         10  REPORT-REAS          PIC 9(04).                      \n012394         10  REPORT-REMARKS       PIC X(30).                      \n012396                                                                  \n012398     05  FM-SCREEN.                                               \n012400         10  FM-SCREEN-CUST       PIC 9(12).                      \n012402         10  FM-SCREEN-ACCT       PIC 9(10).                      \n012404         10  FM-SCREEN-CODE       PIC 9(04).                      \n012406         10  FM-SCREEN-DATA       PIC X(40).                      \n012408         10  FM-SCREEN-APPLY      PIC X(01).                      \n012410     05  FM-SCREEN-FROM-DATA      PIC X(40).                      \n012412     05  FM-SCREEN-DDN            PIC 9(10).                      \n012414     05  FM-SCREEN-TEMPLATE       PIC 9(04).                      \n012416                                                                  \n012418     05  RATE-SCREEN-DATA.                                        \n012420         10  RATE-SUB                       PIC 9(02) VALUE 0.    \n012422         10  RATE-TDAIR-MAX                 PIC 9(02) VALUE 10.   \n012424         10  RATE-TDAMR-MAX                 PIC 9(02) VALUE 10.   \n012426         10  RATE-TDARR-MAX                 PIC 9(02) VALUE 10.   \n012428         10  RATE-TDATR-MAX                 PIC 9(02) VALUE 10.   \n012430         10  RATE-ENTRIES                   PIC 9(02) VALUE 0.    \n012432         10  RATE-TABLE OCCURS 11 TIMES.                          \n012434             15  RATE-REGION                PIC 9(01).            \n012436             15  RATE-RATE-CD               PIC 9(02).            \n012438             15  RATE-EFF-DATE              PIC 9(08).            \n012440             15  RATE-VOID-DATE             PIC 9(08).            \n012442             15  RATE-VOID-PUB-ID           PIC X(08).            \n012444             15  RATE-ADD-DATE              PIC 9(8).             \n012446             15  RATE-ADD-TIME              PIC 9(8).             \n012448             15  RATE-TDARR-RATE-DATA.                            \n012450                 20 RATE-TDARR-CYC-FRQ1     PIC 9(03).            \n012452                 20 FILLER                  PIC X(07).            \n012454                 20 RATE-TDARR-CYC-INC1     PIC S99V999.          \n012456                 20 RATE-TDARR-CYC-FRQ2     PIC 9(03).            \n012458                 20 FILLER                  PIC X(07).            \n012460                 20 RATE-TDARR-CYC-INC2     PIC S99V999.          \n012462                 20 RATE-TDARR-CYC-FRQ3     PIC 9(03).            \n012464                 20 FILLER                  PIC X(07).            \n012466                 20 RATE-TDARR-CYC-INC3     PIC S99V999.          \n012468                 20 RATE-TDARR-CYC-FRQ4     PIC 9(03).            \n012470                 20 FILLER                  PIC X(07).            \n012472                 20 RATE-TDARR-CYC-INC4     PIC S99V999.          \n012474                 20 RATE-TDARR-CYC-FRQ5     PIC 9(03).            \n012476                 20 FILLER                  PIC X(07).            \n012478                 20 RATE-TDARR-CYC-INC5     PIC S99V999.          \n012480                 20 RATE-TDARR-CYC-FRQ6     PIC 9(03).            \n012482                 20 FILLER                  PIC X(07).            \n012484                 20 RATE-TDARR-CYC-INC6     PIC S99V999.          \n012486                 20 RATE-TDARR-CYC-FRQ7     PIC 9(03).            \n012488                 20 FILLER                  PIC X(07).            \n012490                 20 RATE-TDARR-CYC-INC7     PIC S99V999.          \n012492                 20 RATE-TDARR-CYC-FRQ8     PIC 9(03).            \n012494                 20 FILLER                  PIC X(07).            \n012496                 20 RATE-TDARR-CYC-INC8     PIC S99V999.          \n012498                 20 RATE-TDARR-CYC-FRQ9     PIC 9(03).            \n012500                 20 FILLER                  PIC X(07).            \n012502                 20 RATE-TDARR-CYC-INC9     PIC S99V999.          \n012504                 20 RATE-TDARR-CYC-FRQ10    PIC 9(03).            \n012506                 20 FILLER                  PIC X(07).            \n012508                 20 RATE-TDARR-CYC-INC10    PIC S99V999.          \n012510                 20 RATE-TDARR-FREQ         PIC 9(01).            \n012512                 20 FILLER                  PIC X(74).            \n012514                                                                  \n012516             15  RATE-TDATR-RATE-DATA REDEFINES                   \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    149 lines from 6106 to 6254.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 13, "total_chunks": 55, "start_line": 6106, "end_line": 6254, "line_count": 149}


=============================================================================
🚨 CRITICAL RETRY INSTRUCTION 🚨
=============================================================================

You were asked to READ and RETURN the COBOL source code in response.
But you have returned INCOMPLETE COBOL source code.

RETURN the COMPLETE COBOL source code THIS TIME.

DO NOT skip lines, summarize, or use ellipsis (...).
INCLUDE EVERY SINGLE LINE from the source code provided above.

=============================================================================

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
- Source code length: 15829 characters

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
CHUNK 13 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 6106 to 6254 (149 lines)
Chunk Tokens (estimated): ~2,637
Actual Input Tokens: 4,043 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 6106-6254 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 13 of 55 chunks
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
      The source code below is only CHUNK 13 of 55.


=============================================================================
CHUNK 13 SOURCE CODE (Lines 6106-6254)
=============================================================================

```cobol
012220        OLD-ADDR-TEMP-EMAIL.                                      
012222        10 OLD-ADDR-TEMP-EMAIL-1  PIC X(40).                      
012224        10 OLD-ADDR-TEMP-EMAIL-2  PIC X(40).                      
012226        10 OLD-ADDR-TEMP-EMAIL-3  PIC X(20).                      
012228                                                                  
012230     05 WS-TDH-AREA.                                              
012232       10 WS-TDH-SOURCE          PIC 9(02) VALUE 0.               
012234       10 WS-TDH-ERROR           PIC 9(04) VALUE 0.               
012236       10 WS-TDH-BORROWER-NO     PIC 9(12) VALUE 0.               
012238       10 WS-TDH-NOTE-NO         PIC 9(10) VALUE 0.               
012240       10 FILLER                 PIC X(72) VALUE SPACES.          
012242                                                                  
012244     05  ACCTB-OLD-ERROR         PIC 9(04).                       
012246     05  ERASE-TARGET-KEYS.                                       
012248         10  ERASE-TARG-BANK     PIC 9(04).                       
012250         10  ERASE-TARG-DATE     PIC 9(08).                       
012252         10  ERASE-TARG-CUST     PIC 9(12).                       
012254         10  ERASE-TARG-ACCT     PIC 9(10).                       
012256         10  ERASE-TARG-TIME     PIC 9(08).                       
012258         10  ERASE-TARG-SEQ-NBR  PIC 9(02).                       
012260     05  ERASE2-TARGET-KEYS.                                      
012262         10  ERASE2-TARG-BANK     PIC 9(04).                      
012264         10  ERASE2-TARG-DATE     PIC 9(08).                      
012266         10  ERASE2-TARG-CUST     PIC 9(12).                      
012268         10  ERASE2-TARG-ACCT     PIC 9(10).                      
012270         10  ERASE2-TARG-TIME     PIC 9(08).                      
012272         10  ERASE2-TARG-SEQ-NBR  PIC 9(02).                      
012274                                                                  
012276     05  WS-ERASER-IRA-WARN       PIC 9(01).                      
012278     05  WS-APPLY-ALT             PIC 9     VALUE 0.              
012280     05  WS-EMAIL-COUNT           PIC 9     VALUE 0.              
012282                                                                  
012284                                                                  
012286                                                                  
012288     05  PROCESS-DATE             PIC 9(08) VALUE 0.              
012290     05  PROCESS-DATE-R REDEFINES PROCESS-DATE.                   
012292         10  PROCESS-DATE-CCYY    PIC 9(04).                      
012294         10  PROCESS-DATE-CCYY-R REDEFINES PROCESS-DATE-CCYY.     
012296             15  PROCESS-DATE-CC  PIC 99.                         
012298             15  PROCESS-DATE-YY  PIC 99.                         
012300         10  PROCESS-DATE-MMDD    PIC 9(04).                      
012302         10  PROCESS-DATE-MMDD-R REDEFINES PROCESS-DATE-MMDD.     
012304             15  PROCESS-DATE-MM  PIC 99.                         
012306             15  PROCESS-DATE-DD  PIC 99.                         
012308                                                                  
012310     05  EFFECTIVE-DATE           PIC 9(08) VALUE 0.              
012312     05  EFFECTIVE-DATE-R REDEFINES EFFECTIVE-DATE.               
012314         10  EFFECTIVE-DATE-CY    PIC 9(04).                      
012316         10  EFFECTIVE-DATE-CY-R REDEFINES EFFECTIVE-DATE-CY.     
012318             15 EFFECTIVE-DATE-C  PIC 99.                         
012320             15 EFFECTIVE-DATE-Y  PIC 99.                         
012322         10  EFFECTIVE-DATE-MD    PIC 9(04).                      
012324         10  EFFECTIVE-DATE-MD-R REDEFINES EFFECTIVE-DATE-MD.     
012326             15  EFFECTIVE-DATE-M PIC 99.                         
012328             15  EFFECTIVE-DATE-D PIC 99.                         
012330                                                                  
012332     05  WS-IND                   PIC 9     VALUE 0.              
012334     05  WS-MISSED-EVENT          PIC 9     VALUE 0.              
012336                                                                  
012338     05  WS-LAST-DAY-LIST         PIC X(24)                       
012340                                VALUE "312831303130313130313031". 
012342     05  WS-LAST-DAY-R  REDEFINES  WS-LAST-DAY-LIST.              
012344         10  WS-LAST-DAY              OCCURS 12 TIMES             
012346                                  PIC 9(2).                       
012348                                                                  
012350     05  WS-DAY-OF-WEEK-LIST      VALUE                           
012352                                      "SUNMONTUEWEDTHUFRISAT".    
012354         10  WS-DAY-OF-WEEK       OCCURS 07 TIMES                 
012356                                  PIC X(03).                      
012358                                                                  
012360     05  WS-IRA-CONTR-OVR-LIMIT   PIC S9(09)V99.                  
012362     05  WS-IRA-TOTAL-CONTR       PIC S9(09)V99.                  
012364     05  WS-IRA-CONTR-LIMIT-AMT   PIC S9(09)V99.                  
012366                                                                  
012368     05  WS-MONETARY-FIELDS.                                      
012370         10  WS-MONETARY-AMT      PIC S9(09)V99.                  
012372         10  WS-MONETARY-RT       PIC 9(2)V9(3).                  
012374         10  WS-MONETARY-DESC     PIC X(50).                      
012376         10  WS-MONETARY-FLAG     PIC 9.                          
012378                                                                  
012380     05  WS-FUNCTION-CD           PIC 99 VALUE 0.                 
012382                                                                  
012384     05  WS-PAGE-FIELDS.                                          
012386         10  WS-PAGE-COUNT        PIC 99.                         
012388                                                                  
012390     05  REPORT-FIELDS.                                           
012392         10  REPORT-REAS          PIC 9(04).                      
012394         10  REPORT-REMARKS       PIC X(30).                      
012396                                                                  
012398     05  FM-SCREEN.                                               
012400         10  FM-SCREEN-CUST       PIC 9(12).                      
012402         10  FM-SCREEN-ACCT       PIC 9(10).                      
012404         10  FM-SCREEN-CODE       PIC 9(04).                      
012406         10  FM-SCREEN-DATA       PIC X(40).                      
012408         10  FM-SCREEN-APPLY      PIC X(01).                      
012410     05  FM-SCREEN-FROM-DATA      PIC X(40).                      
012412     05  FM-SCREEN-DDN            PIC 9(10).                      
012414     05  FM-SCREEN-TEMPLATE       PIC 9(04).                      
012416                                                                  
012418     05  RATE-SCREEN-DATA.                                        
012420         10  RATE-SUB                       PIC 9(02) VALUE 0.    
012422         10  RATE-TDAIR-MAX                 PIC 9(02) VALUE 10.   
012424         10  RATE-TDAMR-MAX                 PIC 9(02) VALUE 10.   
012426         10  RATE-TDARR-MAX                 PIC 9(02) VALUE 10.   
012428         10  RATE-TDATR-MAX                 PIC 9(02) VALUE 10.   
012430         10  RATE-ENTRIES                   PIC 9(02) VALUE 0.    
012432         10  RATE-TABLE OCCURS 11 TIMES.                          
012434             15  RATE-REGION                PIC 9(01).            
012436             15  RATE-RATE-CD               PIC 9(02).            
012438             15  RATE-EFF-DATE              PIC 9(08).            
012440             15  RATE-VOID-DATE             PIC 9(08).            
012442             15  RATE-VOID-PUB-ID           PIC X(08).            
012444             15  RATE-ADD-DATE              PIC 9(8).             
012446             15  RATE-ADD-TIME              PIC 9(8).             
012448             15  RATE-TDARR-RATE-DATA.                            
012450                 20 RATE-TDARR-CYC-FRQ1     PIC 9(03).            
012452                 20 FILLER                  PIC X(07).            
012454                 20 RATE-TDARR-CYC-INC1     PIC S99V999.          
012456                 20 RATE-TDARR-CYC-FRQ2     PIC 9(03).            
012458                 20 FILLER                  PIC X(07).            
012460                 20 RATE-TDARR-CYC-INC2     PIC S99V999.          
012462                 20 RATE-TDARR-CYC-FRQ3     PIC 9(03).            
012464                 20 FILLER                  PIC X(07).            
012466                 20 RATE-TDARR-CYC-INC3     PIC S99V999.          
012468                 20 RATE-TDARR-CYC-FRQ4     PIC 9(03).            
012470                 20 FILLER                  PIC X(07).            
012472                 20 RATE-TDARR-CYC-INC4     PIC S99V999.          
012474                 20 RATE-TDARR-CYC-FRQ5     PIC 9(03).            
012476                 20 FILLER                  PIC X(07).            
012478                 20 RATE-TDARR-CYC-INC5     PIC S99V999.          
012480                 20 RATE-TDARR-CYC-FRQ6     PIC 9(03).            
012482                 20 FILLER                  PIC X(07).            
012484                 20 RATE-TDARR-CYC-INC6     PIC S99V999.          
012486                 20 RATE-TDARR-CYC-FRQ7     PIC 9(03).            
012488                 20 FILLER                  PIC X(07).            
012490                 20 RATE-TDARR-CYC-INC7     PIC S99V999.          
012492                 20 RATE-TDARR-CYC-FRQ8     PIC 9(03).            
012494                 20 FILLER                  PIC X(07).            
012496                 20 RATE-TDARR-CYC-INC8     PIC S99V999.          
012498                 20 RATE-TDARR-CYC-FRQ9     PIC 9(03).            
012500                 20 FILLER                  PIC X(07).            
012502                 20 RATE-TDARR-CYC-INC9     PIC S99V999.          
012504                 20 RATE-TDARR-CYC-FRQ10    PIC 9(03).            
012506                 20 FILLER                  PIC X(07).            
012508                 20 RATE-TDARR-CYC-INC10    PIC S99V999.          
012510                 20 RATE-TDARR-FREQ         PIC 9(01).            
012512                 20 FILLER                  PIC X(74).            
012514                                                                  
012516             15  RATE-TDATR-RATE-DATA REDEFINES                   
```

⚠️  This is the source code you must document.
    149 lines from 6106 to 6254.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

