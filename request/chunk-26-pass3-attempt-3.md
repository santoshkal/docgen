# LLM Request Debug File
Generated: 2025-11-17T21:06:46.116871

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 26/55
- **Model**: gpt-4.1
- **Chunk Number**: 26
- **Pass Number**: 3
- **Attempt Number**: 3 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~9,100 tokens
- **Total Input**: ~11,058 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 26/55" (ID: detailed-code-explanation)

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


**CHUNK 26 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-17T19:50:50.832678", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 26 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 12142 to 12527 (386 lines)\nChunk Tokens (estimated): ~7,784\nActual Input Tokens: 9,190 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 12142-12527 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 26 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 26 of 55.\n\n\n=============================================================================\nCHUNK 26 SOURCE CODE (Lines 12142-12527)\n=============================================================================\n\n```cobol\n024292 01  WS-REPORT-NAMES.                                             \n024294     05  WS-REPORT-NAME              PIC X(40)                    \n024296                                         VALUE \"TDA/TEST/REPORT \".\n024298     05  WS-LISTING-NAME             PIC X(40)                    \n024300                                         VALUE \"TDA0P1SP00/0000 \".\n024302     05  WS-LISTING160-NAME          PIC X(40)                    \n024304                                         VALUE SPACES.            \n024306     05  WS-LISTING607-NAME          PIC X(40)                    \n024308                                         VALUE SPACES.            \n024310     05  WS-CHECKS-NAME              PIC X(40)                    \n024312                                         VALUE \"TDA0P1OD00/0000 \".\n024314     05  WS-LSR-CHK-NAME             PIC X(40)                    \n024316                                         VALUE \"RMT0DDCBBB/0000 \".\n024318     05  WS-LSR-BANK-NAME            PIC X(40)                    \n024320                                         VALUE \"RMT0DDCBBB/0000 \".\n024322     05  WS-G-LSR-BANK-NAME          PIC X(40)                    \n024324                                         VALUE \"RMT0DDCBBB/0000 \".\n024326     05  WS-LSR-BK-STMT-NM           PIC X(40)                    \n024328                                         VALUE \"RMT0DDCBBB/0000 \".\n024330     05  WS-LSR-BK-STMT-NM-R REDEFINES WS-LSR-BK-STMT-NM.         \n024332         07  WS-LSR-BK-STMT-NMPRE    PIC X(03).                   \n024334         07  FILLER                  PIC X(37).                   \n024336     05  WS-LSR-BK-STMT-PACK         PIC X(10).                   \n024338     05  WS-FICHE-NAME               PIC X(40)                    \n024340                                         VALUE \"TDA0P1SP00/1000 \".\n024342     05  WS-DSI-FILE-NAME            PIC X(40)                    \n024344                                         VALUE \"STMDMMDD/M000TDA\".\n024346     05  WS-LASER-NAME               PIC X(40)                    \n024348                                         VALUE \"LSRDMMDD/M000TDA\".\n024350     05  WS-NOTICE-NAME              PIC X(40)                    \n024352                                         VALUE \"TDA0P1SN00/0000 \".\n024354     05  WS-TRIAL-NAME               PIC X(40)                    \n024356                                         VALUE \"TDA0P1TB00/0000 \".\n024358     05  WS-STATEMENT-NAME           PIC X(40)                    \n024360                                         VALUE \"TDA0P1ST00/0000 \".\n024362     05  WS-STATEMENT-PACK           PIC X(10).                   \n024364     05  WS-CARDS-NAME               PIC X(40)                    \n024366                                         VALUE \"TDA0P1TF00/0000 \".\n024368     05  CHK-RECON-ID.                                            \n024370        10  FILLER                   PIC X(06) VALUE \"RMT0D/\".    \n024372        10  CHK-RECON-DC             PIC 9(02) VALUE 0.           \n024374        10  CHK-RECON-BK             PIC 9(04) VALUE 0.           \n024376        10  FILLER                   PIC X(01) VALUE \"/\".         \n024378        10  CHK-RC-EV                PIC X(01) VALUE \"0\".         \n024380        10  CHK-RC-R                 PIC X(01) VALUE \"R\".         \n024382        10  CHK-RC-I                 PIC X(01) VALUE \"0\".         \n024384        10  CHK-RC-M                 PIC X(01) VALUE \"0\".         \n024386        10  CHK-RC-T1                PIC X(01) VALUE \"0\".         \n024388        10  CHK-RC-T2                PIC X(01) VALUE \"0\".         \n024390        10  FILLER                   PIC X(01) VALUE \"/\".         \n024392        10  CHK-RECON-DAY            PIC 9(02) VALUE 0.           \n024394        10  FILLER                   PIC X(07) VALUE \"NER    \".   \n024396        10  CHK-RECON-PERIOD         PIC X(10) VALUE \".\".         \n024398                                                                  \n024400    05  WS-DSI-CSI-FILE-ID-X.                                     \n024402        10  FILLER                   PIC X(04) VALUE \"STMD\".      \n024404        10  DSI-ST-MMDD              PIC 9(04) VALUE 0.           \n024406        10  FILLER                   PIC X(02) VALUE \"/M\".        \n024408        10  DSI-ST-BANK              PIC 9(03) VALUE 0.           \n024410        10  DSI-ST-APP               PIC X(03) VALUE \"COD\".       \n024412        10  FILLER                   PIC X(04) VALUE \" ON \".      \n024414        10  DSI-ST-PACK              PIC X(20) VALUE \"LSR.\".      \n024416                                                                  \n024418    05  WS-DSI-CSI-FILE-ID-X-EOY.                                 \n024420        10  FILLER                   PIC X(04) VALUE \"STMD\".      \n024422        10  DSI-ST-MMDD-EOY          PIC 9(04) VALUE 0.           \n024424        10  FILLER                   PIC X(02) VALUE \"/M\".        \n024426        10  DSI-ST-BANK-EOY          PIC 9(03) VALUE 0.           \n024428        10  FILLER                   PIC X(03) VALUE \"IRA\".       \n024430        10  FILLER                   PIC X(04) VALUE \" ON \".      \n024432        10  DSI-ST-PACK-EOY          PIC X(20) VALUE \"EOYPRT.\".   \n024434                                                                  \n024436    05  WS-DSI-BANK-FILE-NAME-X.                                  \n024438        10  FILLER                   PIC X(05) VALUE \"RMT0D\".     \n024440        10  DSIB-BANK-DC             PIC 9(02).                   \n024442        10  DSIB-BANK-BANK           PIC 9(03).                   \n024444        10  FILLER                   PIC X(01) VALUE \"/\".         \n024446        10  DSIB-BANK-DD             PIC 9(02).                   \n024448        10  DSIB-BANK-APP            PIC X(01) VALUE \"R\".         \n024450        10  FILLER                   PIC X(06) VALUE \"IS0000\".    \n024452        10  FILLER                   PIC X(04) VALUE \" ON \".      \n024454        10  DSIB-ST-PACK             PIC X(16) VALUE \"RMT.\".      \n024456                                                                  \n024458    05  WS-DSI-BANK-FILE-NAME-X2.                                 \n024460        10  FILLER                   PIC X(05) VALUE \"RMT0D\".     \n024462        10  FILLER                   PIC X(01) VALUE \"/\".         \n024464        10  DSIB-BANK-DC2            PIC 9(02).                   \n024466        10  DSIB-BANK-BANK2          PIC 9(04).                   \n024468        10  FILLER                   PIC X(01) VALUE \"/\".         \n024470        10  DSIB-EV                  PIC X(01) VALUE \"0\".         \n024472        10  DSIB-R                   PIC X(01) VALUE \"R\".         \n024474        10  DSIB-I                   PIC X(01) VALUE \"0\".         \n024476        10  DSIB-M                   PIC X(01) VALUE \"0\".         \n024478        10  DSIB-T1                  PIC X(01) VALUE \"0\".         \n024480        10  DSIB-T2                  PIC X(01) VALUE \"0\".         \n024482        10  FILLER                   PIC X(01) VALUE \"/\".         \n024484        10  DSIB-BANK-DD2            PIC 9(02).                   \n024486        10  DSIB-BANK-APP2           PIC X(01) VALUE \"R\".         \n024488        10  FILLER                   PIC X(06) VALUE \"IS0000\".    \n024490        10  FILLER                   PIC X(04) VALUE \" ON \".      \n024492        10  DSIB-ST-PACK2            PIC X(16) VALUE \"RMT.\".      \n024494                                                                  \n024496    05  WS-DSI-BANK-FILE-NAME-X-EOY.                              \n024498        10  FILLER                   PIC X(05) VALUE \"EOY0D\".     \n024500        10  DSIB-BANK-DC-EOY         PIC 9(02).                   \n024502        10  DSIB-BANK-BANK-EOY       PIC 9(03).                   \n024504        10  FILLER                   PIC X(01) VALUE \"/\".         \n024506        10  DSIB-BANK-DD-EOY         PIC 9(02).                   \n024508        10  DSIB-BANK-APP-EOY        PIC X(01) VALUE \"R\".         \n024510        10  FILLER                   PIC X(06) VALUE \"IS0000\".    \n024512        10  FILLER                   PIC X(04) VALUE \" ON \".      \n024514        10  DSIB-ST-PACK-EOY         PIC X(16) VALUE \"EOY.\".      \n024516                                                                  \n024518    05  WS-LASER-NAME-X.                                          \n024520        10  FILLER                   PIC X(04) VALUE \"LSRD\".      \n024522        10  WS-LSR-MMDD              PIC 9(04) VALUE 0.           \n024524        10  FILLER                   PIC X(02) VALUE \"/M\".        \n024526        10  WS-LSR-BANK              PIC 9(03) VALUE 0.           \n024528        10  FILLER                   PIC X(03) VALUE \"TDA\".       \n024530        10  FILLER                   PIC X(04) VALUE \" ON \".      \n024532        10  WS-LSR-PACK              PIC X(10) VALUE \"LSR.\".      \n024534        10  WS-LSR-PERIOD            PIC X(01) VALUE SPACE.       \n024536                                                                  \n024538    05  WS-LSR-CHK-NAME-X.                                        \n024540        10  FILLER                   PIC X(05) VALUE \"RMT0P\".     \n024542        10  LSR-CHK-DC               PIC 9(02) VALUE 0.           \n024544        10  LSR-CHK-BANK             PIC 9(03) VALUE 0.           \n024546        10  FILLER                   PIC X(01) VALUE \"/\".         \n024548        10  LSR-CHK-DD               PIC 9(02) VALUE 0.           \n024550        10  FILLER                   PIC X(07) VALUE \"NLK1000\".   \n024552        10  FILLER                   PIC X(04) VALUE \" ON \".      \n024554        10  LSR-CHK-PACK             PIC X(10) VALUE \"GENERAL.\".  \n024556        10  LSR-CHK-PERIOD           PIC X(01) VALUE SPACE.       \n024558                                                                  \n024560    05  WS-LSR-BANK-NAME-X.                                       \n024562        10  FILLER                   PIC X(05) VALUE \"RMT0P\".     \n024564        10  SPC-DC                   PIC 9(02) VALUE 0.           \n024566        10  SPC-BANK                 PIC 9(03) VALUE 0.           \n024568        10  FILLER                   PIC X(01) VALUE \"/\".         \n024570        10  SPC-DD                   PIC 9(02) VALUE 0.           \n024572        10  FILLER                   PIC X(07) VALUE \"NLN2000\".   \n024574        10  FILLER                   PIC X(04) VALUE \" ON \".      \n024576        10  SPC-PACK                 PIC X(10) VALUE \"GENERAL.\".  \n024578        10  SPC-PERIOD               PIC X(01) VALUE SPACE.       \n024580                                                                  \n024582    05  WS-G-LSR-BANK-NAME-X.                                     \n024584        10  FILLER                   PIC X(05) VALUE \"RMT0P\".     \n024586        10  G-SPC-DC                 PIC 9(02) VALUE 0.           \n024588        10  G-SPC-BANK               PIC 9(03) VALUE 0.           \n024590        10  FILLER                   PIC X(01) VALUE \"/\".         \n024592        10  G-SPC-DD                 PIC 9(02) VALUE 0.           \n024594        10  FILLER                   PIC X(07) VALUE \"NLG2000\".   \n024596        10  FILLER                   PIC X(04) VALUE \" ON \".      \n024598        10  G-SPC-PACK               PIC X(10) VALUE \"GENERAL.\".  \n024600        10  G-SPC-PERIOD             PIC X(01) VALUE SPACE.       \n024602                                                                  \n024604    05  WS-LSR-BANK-STMT-NAME-X.                                  \n024606        10  FILLER                   PIC X(05) VALUE \"RMT0P\".     \n024608        10  SPCS-DC                  PIC 9(02) VALUE 0.           \n024610        10  SPCS-BANK                PIC 9(03) VALUE 0.           \n024612        10  FILLER                   PIC X(01) VALUE \"/\".         \n024614        10  SPCS-DD                  PIC 9(02) VALUE 0.           \n024616        10  FILLER                   PIC X(07) VALUE \"NLS2000\".   \n024618        10  FILLER                   PIC X(04) VALUE \" ON \".      \n024620        10  SPCS-PACK                PIC X(10) VALUE \"GENERAL.\".  \n024622        10  SPCS-PERIOD              PIC X(01) VALUE SPACE.       \n024624                                                                  \n024626    05  WS-LSR-BANK-STMT-NAME-X-EOY.                              \n024628        10  FILLER                   PIC X(05) VALUE \"RMT0P\".     \n024630        10  SPCS-DC-EOY              PIC 9(02) VALUE 0.           \n024632        10  SPCS-BANK-EOY            PIC 9(03) VALUE 0.           \n024634        10  FILLER                   PIC X(01) VALUE \"/\".         \n024636        10  SPCS-DD-EOY              PIC 9(02) VALUE 0.           \n024638        10  FILLER                   PIC X(07) VALUE \"NLS2000\".   \n024640        10  FILLER                   PIC X(04) VALUE \" ON \".      \n024642        10  SPCS-PACK-EOY            PIC X(10) VALUE \"EOY.    \".  \n024644        10  SPCS-PERIOD-EOY          PIC X(01) VALUE SPACE.       \n024646                                                                  \n024648 01  ID-PRINT-FILES-NT.                                           \n024650     05  FILLER                         PIC X(01) VALUE \"C\".      \n024652     05  FILLER                         PIC X(02) VALUE \":/\".     \n024654     05  ID-PRINT-DIR-NT                PIC X(05) VALUE \"PRINT\".  \n024656     05  FILLER                         PIC X(01) VALUE \"/\".      \n024658     05  ID-PRINT-NAME-NT               PIC X(52) VALUE SPACES.   \n024660                                                                  \n024662 01  RMDRPT-REC-3.                                                \n024664     02  Z-VA-RMDRPT-REC-3     PIC  X(00160) VALUE SPACES.        \n024666     02  Z-NX-RMDRPT-REC-3     REDEFINES Z-VA-RMDRPT-REC-3.       \n024668     05  FILLER                PIC X(0001).                       \n024670     05  RMDRPT-CUST-3         PIC XXXXXXXXXXXX.                  \n024672     05  FILLER                PIC X(0001).                       \n024674     05  RMDRPT-ACCT-3         PIC XXXXXXXXXX.                    \n024676     05  FILLER                PIC X(0001).                       \n024678     05  RMDRPT-BIRTH-DT-3     PIC XXXXXXXXXX.                    \n024680     05  FILLER                PIC X(0001).                       \n024682     05  RMDRPT-AGE-DATE-3     PIC XXXXXXXXXX.                    \n024684     05  FILLER                PIC X(0002).                       \n024686     05  RMDRPT-BEG-DATE-3     PIC XXXXXXXXXX.                    \n024688     05  FILLER                PIC X(0001).                       \n024690     05  RMDRPT-BAL-BEG-YR-3   PIC ZZ,ZZZ,ZZZ.99.                 \n024692     05  FILLER                PIC X(0001).                       \n024694     05  RMDRPT-CUR-BAL-IND-3  PIC X(0001).                       \n024696     05  FILLER                PIC X(0001).                       \n024698     05  RMDRPT-FACTOR-3       PIC 99.9.                          \n024700     05  FILLER                PIC X(0001).                       \n024702     05  RMDRPT-SLASH-3        PIC X(0001).                       \n024704     05  FILLER                PIC X(0001).                       \n024706     05  RMDRPT-TBL-3          PIC 9(0001).                       \n024708     05  FILLER                PIC X(0001).                       \n024710     05  RMDRPT-MINDIST-3      PIC Z,ZZZ,ZZZ.99.                  \n024712     05  FILLER                PIC X(0001).                       \n024714     05  RMDRPT-RMD-MAN-CALC-3 PIC X(0001).                       \n024716     05  FILLER                PIC X(0002).                       \n024718     05  RMDRPT-DIST-FREQ-3.                                      \n024720         10  RMDRPT-DS-NTRVL-3 PIC XXXX.                          \n024722         10  FILLER            PIC X.                             \n024724         10  RMDRPT-DS-FREQ-3  PIC X.                             \n024726     05  FILLER                PIC X(0001).                       \n024728     05  RMDRPT-OLD-DS-AMT-3   PIC Z,ZZZ,ZZZ.99.                  \n024730     05  FILLER                PIC X(0001).                       \n024732     05  RMDRPT-NEW-DS-AMT-3   PIC Z,ZZZ,ZZZ.99.                  \n024734     05  FILLER                PIC X(0028).                       \n024736* 004 LINE RECORD FOLLOWS                                         \n024738 01  RMDRPT-REC-4.                                                \n024740     02  Z-VA-RMDRPT-REC-4     PIC  X(00160) VALUE SPACES.        \n024742     02  Z-NX-RMDRPT-REC-4     REDEFINES Z-VA-RMDRPT-REC-4.       \n024744     05  FILLER                PIC X(0001).                       \n024746     05  RMDRPT-NAME-4         PIC X(0030).                       \n024748     05  FILLER                PIC X(0004).                       \n024750     05  RMDRPT-REMARK-4       PIC X(0040).                       \n024752     05  FILLER                PIC X(0001).                       \n024754     05  RMDRPT-REMARK2-4      PIC X(0023).                       \n024756     05  FILLER                PIC X(0001).                       \n024758     05  RMDRPT-DS-METH-4      PIC X(0004).                       \n024760     05  FILLER                PIC X(0017).                       \n024762     05  RMDRPT-WH-MSG-4       PIC X(0010).                       \n024764     05  FILLER                PIC X(0029).                       \n024766* 005 LINE RECORD FOLLOWS                                         \n024768 01  RMDRPT-REC-8.                                                \n024770     02  Z-VA-RMDRPT-REC-8     PIC  X(00160) VALUE SPACES.        \n024772     02  Z-NX-RMDRPT-REC-8     REDEFINES Z-VA-RMDRPT-REC-8.       \n024774     05  FILLER                PIC X(0001).                       \n024776     05  RMDRPT-NAME-8         PIC X(0030).                       \n024778     05  FILLER                PIC X(0129).                       \n024780* 009 LINE RECORD FOLLOWS                                         \n024782  01 WS-MINDIST.                                                  \n024784     05  WS-AGE                   PIC 9(03).                      \n024786     05  WS-SP-AGE                PIC 9(03).                      \n024788     05  WS-AGE-COUNT             PIC 9(03).                      \n024790     05  WS-MD-COUNT              PIC 9(04).                      \n024792     05  WS-FACTOR                PIC 99V9.                       \n024794     05  WS-MD-AGE-DIFF           PIC S9(03).                     \n024796     05  WS-BNF-AGE               PIC 9(03).                      \n024798     05  WS-MD-FMV                PIC S9(12)V99.                  \n024800     05  WS-MD-AGE                PIC 9(03).                      \n024802     05  WS-MD-BN-AGE             PIC 9(03).                      \n024804     05  WS-MD-SPOUSE             PIC X(01).                      \n024806     05  WS-MD-AMT                PIC S9(12)V99.                  \n024808     05  WS-MD-TBL                PIC 9(01).                      \n024810     05  WS-MD-FACT               PIC 9(02)V9.                    \n024812     05  WS-CUST-YAD              PIC 9(08) VALUE 0.              \n024814     05  WS-NUM-YR-YAD            PIC 9(03) VALUE 0.              \n024816 01  RMDRPT2-REC-3.                                               \n024818     02  Z-VA-RMDRPT2-REC-3    PIC  X(00160) VALUE SPACES.        \n024820     02  Z-NX-RMDRPT2-REC-3    REDEFINES Z-VA-RMDRPT2-REC-3.      \n024822     05  FILLER                PIC X(0001).                       \n024824     05  RMDRPT2-CUST-3        PIC XXXXXXXXXXXX.                  \n024826     05  FILLER                PIC X(0001).                       \n024828     05  RMDRPT2-ACCT-3        PIC XXXXXXXXXX.                    \n024830     05  FILLER                PIC X(0002).                       \n024832     05  RMDRPT2-BIRTH-DT-3    PIC XXXXXXXXXX.                    \n024834     05  FILLER                PIC X(0002).                       \n024836     05  RMDRPT2-AGE-DATE-3    PIC XXXXXXXXXX.                    \n024838     05  FILLER                PIC X(0002).                       \n024840     05  RMDRPT2-BEG-DATE-3    PIC XXXXXXXXXX.                    \n024842     05  FILLER                PIC X(0002).                       \n024844     05  RMDRPT2-DTH-DATE-3    PIC XXXXXXXXXX.                    \n024846     05  FILLER                PIC X(0001).                       \n024848     05  RMDRPT2-BAL-BEG-YR-3  PIC ZZ,ZZZ,ZZZ.99.                 \n024850     05  FILLER                PIC X(0001).                       \n024852     05  RMDRPT2-CUR-BAL-IND-3 PIC X(0001).                       \n024854     05  FILLER                PIC X(0001).                       \n024856     05  RMDRPT2-FACTOR-3      PIC 99.9.                          \n024858     05  FILLER                PIC X(0001).                       \n024860     05  RMDRPT2-SLASH-3       PIC X(0001).                       \n024862     05  FILLER                PIC X(0001).                       \n024864     05  RMDRPT2-TBL-3         PIC 9(0001).                       \n024866     05  FILLER                PIC X(0001).                       \n024868     05  RMDRPT2-MINDIST-3     PIC Z,ZZZ,ZZZ.99.                  \n024870     05  FILLER                PIC X(0001).                       \n024872     05  RMDRPT2-RMD-MAN-CALC-3                                   \n024874                               PIC X(0001).                       \n024876     05  FILLER                PIC X(0002).                       \n024878     05  RMDRPT2-DIST-FREQ-3.                                     \n024880         10  RMDRPT2-DS-NTRVL-3                                   \n024882                               PIC XXXX.                          \n024884         10  FILLER            PIC X.                             \n024886         10  RMDRPT2-DS-FREQ-3 PIC X.                             \n024888     05  FILLER                PIC X(0001).                       \n024890     05  RMDRPT2-OLD-DS-AMT-3  PIC Z,ZZZ,ZZZ.99.                  \n024892     05  FILLER                PIC X(0001).                       \n024894     05  RMDRPT2-NEW-DS-AMT-3  PIC Z,ZZZ,ZZZ.99.                  \n024896     05  FILLER                PIC X(0014).                       \n024898* 004 LINE RECORD FOLLOWS                                         \n024900 01  RMDRPT2-REC-4.                                               \n024902     02  Z-VA-RMDRPT2-REC-4    PIC  X(00160) VALUE SPACES.        \n024904     02  Z-NX-RMDRPT2-REC-4    REDEFINES Z-VA-RMDRPT2-REC-4.      \n024906     05  FILLER                PIC X(0001).                       \n024908     05  RMDRPT2-NAME-4        PIC X(0030).                       \n024910     05  FILLER                PIC X(0004).                       \n024912     05  RMDRPT2-REMARK-4      PIC X(0040).                       \n024914     05  FILLER                PIC X(0001).                       \n024916     05  RMDRPT2-REMARK2-4     PIC X(0023).                       \n024918     05  FILLER                PIC X(0001).                       \n024920     05  RMDRPT2-DS-METH-4     PIC X(0004).                       \n024922     05  FILLER                PIC X(0017).                       \n024924     05  RMDRPT2-WH-MSG-4      PIC X(0010).                       \n024926     05  FILLER                PIC X(0029).                       \n024928* 005 LINE RECORD FOLLOWS                                         \n024930 01  RMDRPT2-REC-8.                                               \n024932     02  Z-VA-RMDRPT2-REC-8    PIC  X(00160) VALUE SPACES.        \n024934     02  Z-NX-RMDRPT2-REC-8    REDEFINES Z-VA-RMDRPT2-REC-8.      \n024936     05  FILLER                PIC X(0001).                       \n024938     05  RMDRPT2-NAME-8        PIC X(0030).                       \n024940     05  FILLER                PIC X(0129).                       \n024942* 009 LINE RECORD FOLLOWS                                         \n024944 01 PCR-SPEC-RECORD.                                              \n024946                                                                  \n024948**  SPECS FOR 999 PCR                                             \n024950   05  SPECS-AREA.                                                \n024952     10  SPECS-GRACE-IN-PROC             PIC 9(2).                \n024954     10  SPECS-GRACE-CLOSE               PIC 9(2).                \n024956     10  SPECS-PRE-MAT                   PIC 9(2).                \n024958     10  SPECS-LSR-PILOT                 PIC X(1).                \n024960     10  SPECS-CHK-RECON                 PIC 9(8).                \n024962     10  SPECS-BR-ADDR                   PIC X(1).                \n024964     10  SPECS-TIN-SUPPRESS              PIC X(1).                \n024966     10  SPECS-NO-IN-PROC                PIC X(1).                \n024968     10  SPECS-RMD-OVERRIDE              PIC X(1).                \n024970     10  SPECS-PPP-PILOT                 PIC X(1).                \n024972     10  SPECS-RETURN-ENVELOPE           PIC X(1).                \n024974     10  SPECS-LSTCONT-DDACOMB           PIC X(1).                \n024976     10  SPECS-LSTCONT-TDASTMT           PIC X(1).                \n024978     10  SPECS-LSTCONT-INTNTC            PIC X(1).                \n024980     10  SPECS-LSTCONT-ALLNTC            PIC X(1).                \n024982     10  SPECS-LSTCONT-CHECKS            PIC X(1).                \n024984     10  SPECS-LSTCONT-DISTREC           PIC X(1).                \n024986     10  SPECS-COMB-AUTO-RMD-ADJUST      PIC X(1).                \n024988     10  SPECS-IGL-HIGH-BAL              PIC 9(6).                \n024990     10  SPECS-AVAIL-CAP-INT             PIC X(1).                \n024992     10  SPECS-CNV-TOT-DNLOAD            PIC 9(08).               \n024994     10  SPECS-CNV-TOT-DNLOAD-R REDEFINES                         \n024996         SPECS-CNV-TOT-DNLOAD.                                    \n024998         15 SPECS-CNV-TOT-DNLOAD-X       PIC X(08).               \n025000     10  FILLER                          PIC X(13).               \n025002     10  SPECS-ADDR-ALERT-DAYS           PIC 999.                 \n025004     10  SPECS-COMB-SEND-CERT            PIC X(1).                \n025006     10  SPECS-APPLY-GRACE-AT-SR         PIC X(1).                \n025008     10  SPECS-DB-SUFFIX                 PIC X(1).                \n025010     10  SPECS-EOY-YTD-ROLL              PIC X(1).                \n025012     10  SPECS-COMB-DDA-OPT              PIC X(1).                \n025014     10  SPECS-CONTINUE                  PIC X(1).                \n025016                                                                  \n025018   05  OLD-SPECS-AREA.                                            \n025020     10  OLD-SPECS-GRACE-IN-PROC         PIC 9(2).                \n025022     10  OLD-SPECS-GRACE-CLOSE           PIC 9(2).                \n025024     10  OLD-SPECS-PRE-MAT               PIC 9(2).                \n025026     10  OLD-SPECS-LSR-PILOT             PIC X(1).                \n025028     10  OLD-SPECS-CHK-RECON             PIC 9(8).                \n025030     10  OLD-SPECS-BR-ADDR               PIC X(1).                \n025032     10  OLD-SPECS-TIN-SUPPRESS          PIC X(1).                \n025034     10  OLD-SPECS-NO-IN-PROC            PIC X(1).                \n025036     10  OLD-SPECS-RMD-OVERRIDE          PIC X(1).                \n025038     10  OLD-SPECS-PPP-PILOT             PIC X(1).                \n025040     10  OLD-SPECS-RETURN-ENVELOPE       PIC X(1).                \n025042     10  OLD-SPECS-LSTCONT-DDACOMB       PIC X(1).                \n025044     10  OLD-SPECS-LSTCONT-TDASTMT       PIC X(1).                \n025046     10  OLD-SPECS-LSTCONT-INTNTC        PIC X(1).                \n025048     10  OLD-SPECS-LSTCONT-ALLNTC        PIC X(1).                \n025050     10  OLD-SPECS-LSTCONT-CHECKS        PIC X(1).                \n025052     10  OLD-SPECS-LSTCONT-DISTREC       PIC X(1).                \n025054     10  OLD-SPECS-COMB-AUTO-RMD-ADJUST  PIC X(1).                \n025056     10  OLD-SPECS-IGL-HIGH-BAL          PIC 9(6).                \n025058     10  OLD-SPECS-AVAIL-CAP-INT         PIC X(1).                \n025060     10  OLD-SPECS-CNV-TOT-DNLOAD        PIC 9(08).               \n025062     10  OLD-SPECS-CNV-TOT-DNLOAD-R REDEFINES                     \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    386 lines from 12142 to 12527.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 26, "total_chunks": 55, "start_line": 12142, "end_line": 12527, "line_count": 386}

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
- Source code length: 33138 characters

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
CHUNK 26 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 12142 to 12527 (386 lines)
Chunk Tokens (estimated): ~7,784
Actual Input Tokens: 9,190 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 12142-12527 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 26 of 55 chunks
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
      The source code below is only CHUNK 26 of 55.


=============================================================================
CHUNK 26 SOURCE CODE (Lines 12142-12527)
=============================================================================

```cobol
024292 01  WS-REPORT-NAMES.                                             
024294     05  WS-REPORT-NAME              PIC X(40)                    
024296                                         VALUE "TDA/TEST/REPORT ".
024298     05  WS-LISTING-NAME             PIC X(40)                    
024300                                         VALUE "TDA0P1SP00/0000 ".
024302     05  WS-LISTING160-NAME          PIC X(40)                    
024304                                         VALUE SPACES.            
024306     05  WS-LISTING607-NAME          PIC X(40)                    
024308                                         VALUE SPACES.            
024310     05  WS-CHECKS-NAME              PIC X(40)                    
024312                                         VALUE "TDA0P1OD00/0000 ".
024314     05  WS-LSR-CHK-NAME             PIC X(40)                    
024316                                         VALUE "RMT0DDCBBB/0000 ".
024318     05  WS-LSR-BANK-NAME            PIC X(40)                    
024320                                         VALUE "RMT0DDCBBB/0000 ".
024322     05  WS-G-LSR-BANK-NAME          PIC X(40)                    
024324                                         VALUE "RMT0DDCBBB/0000 ".
024326     05  WS-LSR-BK-STMT-NM           PIC X(40)                    
024328                                         VALUE "RMT0DDCBBB/0000 ".
024330     05  WS-LSR-BK-STMT-NM-R REDEFINES WS-LSR-BK-STMT-NM.         
024332         07  WS-LSR-BK-STMT-NMPRE    PIC X(03).                   
024334         07  FILLER                  PIC X(37).                   
024336     05  WS-LSR-BK-STMT-PACK         PIC X(10).                   
024338     05  WS-FICHE-NAME               PIC X(40)                    
024340                                         VALUE "TDA0P1SP00/1000 ".
024342     05  WS-DSI-FILE-NAME            PIC X(40)                    
024344                                         VALUE "STMDMMDD/M000TDA".
024346     05  WS-LASER-NAME               PIC X(40)                    
024348                                         VALUE "LSRDMMDD/M000TDA".
024350     05  WS-NOTICE-NAME              PIC X(40)                    
024352                                         VALUE "TDA0P1SN00/0000 ".
024354     05  WS-TRIAL-NAME               PIC X(40)                    
024356                                         VALUE "TDA0P1TB00/0000 ".
024358     05  WS-STATEMENT-NAME           PIC X(40)                    
024360                                         VALUE "TDA0P1ST00/0000 ".
024362     05  WS-STATEMENT-PACK           PIC X(10).                   
024364     05  WS-CARDS-NAME               PIC X(40)                    
024366                                         VALUE "TDA0P1TF00/0000 ".
024368     05  CHK-RECON-ID.                                            
024370        10  FILLER                   PIC X(06) VALUE "RMT0D/".    
024372        10  CHK-RECON-DC             PIC 9(02) VALUE 0.           
024374        10  CHK-RECON-BK             PIC 9(04) VALUE 0.           
024376        10  FILLER                   PIC X(01) VALUE "/".         
024378        10  CHK-RC-EV                PIC X(01) VALUE "0".         
024380        10  CHK-RC-R                 PIC X(01) VALUE "R".         
024382        10  CHK-RC-I                 PIC X(01) VALUE "0".         
024384        10  CHK-RC-M                 PIC X(01) VALUE "0".         
024386        10  CHK-RC-T1                PIC X(01) VALUE "0".         
024388        10  CHK-RC-T2                PIC X(01) VALUE "0".         
024390        10  FILLER                   PIC X(01) VALUE "/".         
024392        10  CHK-RECON-DAY            PIC 9(02) VALUE 0.           
024394        10  FILLER                   PIC X(07) VALUE "NER    ".   
024396        10  CHK-RECON-PERIOD         PIC X(10) VALUE ".".         
024398                                                                  
024400    05  WS-DSI-CSI-FILE-ID-X.                                     
024402        10  FILLER                   PIC X(04) VALUE "STMD".      
024404        10  DSI-ST-MMDD              PIC 9(04) VALUE 0.           
024406        10  FILLER                   PIC X(02) VALUE "/M".        
024408        10  DSI-ST-BANK              PIC 9(03) VALUE 0.           
024410        10  DSI-ST-APP               PIC X(03) VALUE "COD".       
024412        10  FILLER                   PIC X(04) VALUE " ON ".      
024414        10  DSI-ST-PACK              PIC X(20) VALUE "LSR.".      
024416                                                                  
024418    05  WS-DSI-CSI-FILE-ID-X-EOY.                                 
024420        10  FILLER                   PIC X(04) VALUE "STMD".      
024422        10  DSI-ST-MMDD-EOY          PIC 9(04) VALUE 0.           
024424        10  FILLER                   PIC X(02) VALUE "/M".        
024426        10  DSI-ST-BANK-EOY          PIC 9(03) VALUE 0.           
024428        10  FILLER                   PIC X(03) VALUE "IRA".       
024430        10  FILLER                   PIC X(04) VALUE " ON ".      
024432        10  DSI-ST-PACK-EOY          PIC X(20) VALUE "EOYPRT.".   
024434                                                                  
024436    05  WS-DSI-BANK-FILE-NAME-X.                                  
024438        10  FILLER                   PIC X(05) VALUE "RMT0D".     
024440        10  DSIB-BANK-DC             PIC 9(02).                   
024442        10  DSIB-BANK-BANK           PIC 9(03).                   
024444        10  FILLER                   PIC X(01) VALUE "/".         
024446        10  DSIB-BANK-DD             PIC 9(02).                   
024448        10  DSIB-BANK-APP            PIC X(01) VALUE "R".         
024450        10  FILLER                   PIC X(06) VALUE "IS0000".    
024452        10  FILLER                   PIC X(04) VALUE " ON ".      
024454        10  DSIB-ST-PACK             PIC X(16) VALUE "RMT.".      
024456                                                                  
024458    05  WS-DSI-BANK-FILE-NAME-X2.                                 
024460        10  FILLER                   PIC X(05) VALUE "RMT0D".     
024462        10  FILLER                   PIC X(01) VALUE "/".         
024464        10  DSIB-BANK-DC2            PIC 9(02).                   
024466        10  DSIB-BANK-BANK2          PIC 9(04).                   
024468        10  FILLER                   PIC X(01) VALUE "/".         
024470        10  DSIB-EV                  PIC X(01) VALUE "0".         
024472        10  DSIB-R                   PIC X(01) VALUE "R".         
024474        10  DSIB-I                   PIC X(01) VALUE "0".         
024476        10  DSIB-M                   PIC X(01) VALUE "0".         
024478        10  DSIB-T1                  PIC X(01) VALUE "0".         
024480        10  DSIB-T2                  PIC X(01) VALUE "0".         
024482        10  FILLER                   PIC X(01) VALUE "/".         
024484        10  DSIB-BANK-DD2            PIC 9(02).                   
024486        10  DSIB-BANK-APP2           PIC X(01) VALUE "R".         
024488        10  FILLER                   PIC X(06) VALUE "IS0000".    
024490        10  FILLER                   PIC X(04) VALUE " ON ".      
024492        10  DSIB-ST-PACK2            PIC X(16) VALUE "RMT.".      
024494                                                                  
024496    05  WS-DSI-BANK-FILE-NAME-X-EOY.                              
024498        10  FILLER                   PIC X(05) VALUE "EOY0D".     
024500        10  DSIB-BANK-DC-EOY         PIC 9(02).                   
024502        10  DSIB-BANK-BANK-EOY       PIC 9(03).                   
024504        10  FILLER                   PIC X(01) VALUE "/".         
024506        10  DSIB-BANK-DD-EOY         PIC 9(02).                   
024508        10  DSIB-BANK-APP-EOY        PIC X(01) VALUE "R".         
024510        10  FILLER                   PIC X(06) VALUE "IS0000".    
024512        10  FILLER                   PIC X(04) VALUE " ON ".      
024514        10  DSIB-ST-PACK-EOY         PIC X(16) VALUE "EOY.".      
024516                                                                  
024518    05  WS-LASER-NAME-X.                                          
024520        10  FILLER                   PIC X(04) VALUE "LSRD".      
024522        10  WS-LSR-MMDD              PIC 9(04) VALUE 0.           
024524        10  FILLER                   PIC X(02) VALUE "/M".        
024526        10  WS-LSR-BANK              PIC 9(03) VALUE 0.           
024528        10  FILLER                   PIC X(03) VALUE "TDA".       
024530        10  FILLER                   PIC X(04) VALUE " ON ".      
024532        10  WS-LSR-PACK              PIC X(10) VALUE "LSR.".      
024534        10  WS-LSR-PERIOD            PIC X(01) VALUE SPACE.       
024536                                                                  
024538    05  WS-LSR-CHK-NAME-X.                                        
024540        10  FILLER                   PIC X(05) VALUE "RMT0P".     
024542        10  LSR-CHK-DC               PIC 9(02) VALUE 0.           
024544        10  LSR-CHK-BANK             PIC 9(03) VALUE 0.           
024546        10  FILLER                   PIC X(01) VALUE "/".         
024548        10  LSR-CHK-DD               PIC 9(02) VALUE 0.           
024550        10  FILLER                   PIC X(07) VALUE "NLK1000".   
024552        10  FILLER                   PIC X(04) VALUE " ON ".      
024554        10  LSR-CHK-PACK             PIC X(10) VALUE "GENERAL.".  
024556        10  LSR-CHK-PERIOD           PIC X(01) VALUE SPACE.       
024558                                                                  
024560    05  WS-LSR-BANK-NAME-X.                                       
024562        10  FILLER                   PIC X(05) VALUE "RMT0P".     
024564        10  SPC-DC                   PIC 9(02) VALUE 0.           
024566        10  SPC-BANK                 PIC 9(03) VALUE 0.           
024568        10  FILLER                   PIC X(01) VALUE "/".         
024570        10  SPC-DD                   PIC 9(02) VALUE 0.           
024572        10  FILLER                   PIC X(07) VALUE "NLN2000".   
024574        10  FILLER                   PIC X(04) VALUE " ON ".      
024576        10  SPC-PACK                 PIC X(10) VALUE "GENERAL.".  
024578        10  SPC-PERIOD               PIC X(01) VALUE SPACE.       
024580                                                                  
024582    05  WS-G-LSR-BANK-NAME-X.                                     
024584        10  FILLER                   PIC X(05) VALUE "RMT0P".     
024586        10  G-SPC-DC                 PIC 9(02) VALUE 0.           
024588        10  G-SPC-BANK               PIC 9(03) VALUE 0.           
024590        10  FILLER                   PIC X(01) VALUE "/".         
024592        10  G-SPC-DD                 PIC 9(02) VALUE 0.           
024594        10  FILLER                   PIC X(07) VALUE "NLG2000".   
024596        10  FILLER                   PIC X(04) VALUE " ON ".      
024598        10  G-SPC-PACK               PIC X(10) VALUE "GENERAL.".  
024600        10  G-SPC-PERIOD             PIC X(01) VALUE SPACE.       
024602                                                                  
024604    05  WS-LSR-BANK-STMT-NAME-X.                                  
024606        10  FILLER                   PIC X(05) VALUE "RMT0P".     
024608        10  SPCS-DC                  PIC 9(02) VALUE 0.           
024610        10  SPCS-BANK                PIC 9(03) VALUE 0.           
024612        10  FILLER                   PIC X(01) VALUE "/".         
024614        10  SPCS-DD                  PIC 9(02) VALUE 0.           
024616        10  FILLER                   PIC X(07) VALUE "NLS2000".   
024618        10  FILLER                   PIC X(04) VALUE " ON ".      
024620        10  SPCS-PACK                PIC X(10) VALUE "GENERAL.".  
024622        10  SPCS-PERIOD              PIC X(01) VALUE SPACE.       
024624                                                                  
024626    05  WS-LSR-BANK-STMT-NAME-X-EOY.                              
024628        10  FILLER                   PIC X(05) VALUE "RMT0P".     
024630        10  SPCS-DC-EOY              PIC 9(02) VALUE 0.           
024632        10  SPCS-BANK-EOY            PIC 9(03) VALUE 0.           
024634        10  FILLER                   PIC X(01) VALUE "/".         
024636        10  SPCS-DD-EOY              PIC 9(02) VALUE 0.           
024638        10  FILLER                   PIC X(07) VALUE "NLS2000".   
024640        10  FILLER                   PIC X(04) VALUE " ON ".      
024642        10  SPCS-PACK-EOY            PIC X(10) VALUE "EOY.    ".  
024644        10  SPCS-PERIOD-EOY          PIC X(01) VALUE SPACE.       
024646                                                                  
024648 01  ID-PRINT-FILES-NT.                                           
024650     05  FILLER                         PIC X(01) VALUE "C".      
024652     05  FILLER                         PIC X(02) VALUE ":/".     
024654     05  ID-PRINT-DIR-NT                PIC X(05) VALUE "PRINT".  
024656     05  FILLER                         PIC X(01) VALUE "/".      
024658     05  ID-PRINT-NAME-NT               PIC X(52) VALUE SPACES.   
024660                                                                  
024662 01  RMDRPT-REC-3.                                                
024664     02  Z-VA-RMDRPT-REC-3     PIC  X(00160) VALUE SPACES.        
024666     02  Z-NX-RMDRPT-REC-3     REDEFINES Z-VA-RMDRPT-REC-3.       
024668     05  FILLER                PIC X(0001).                       
024670     05  RMDRPT-CUST-3         PIC XXXXXXXXXXXX.                  
024672     05  FILLER                PIC X(0001).                       
024674     05  RMDRPT-ACCT-3         PIC XXXXXXXXXX.                    
024676     05  FILLER                PIC X(0001).                       
024678     05  RMDRPT-BIRTH-DT-3     PIC XXXXXXXXXX.                    
024680     05  FILLER                PIC X(0001).                       
024682     05  RMDRPT-AGE-DATE-3     PIC XXXXXXXXXX.                    
024684     05  FILLER                PIC X(0002).                       
024686     05  RMDRPT-BEG-DATE-3     PIC XXXXXXXXXX.                    
024688     05  FILLER                PIC X(0001).                       
024690     05  RMDRPT-BAL-BEG-YR-3   PIC ZZ,ZZZ,ZZZ.99.                 
024692     05  FILLER                PIC X(0001).                       
024694     05  RMDRPT-CUR-BAL-IND-3  PIC X(0001).                       
024696     05  FILLER                PIC X(0001).                       
024698     05  RMDRPT-FACTOR-3       PIC 99.9.                          
024700     05  FILLER                PIC X(0001).                       
024702     05  RMDRPT-SLASH-3        PIC X(0001).                       
024704     05  FILLER                PIC X(0001).                       
024706     05  RMDRPT-TBL-3          PIC 9(0001).                       
024708     05  FILLER                PIC X(0001).                       
024710     05  RMDRPT-MINDIST-3      PIC Z,ZZZ,ZZZ.99.                  
024712     05  FILLER                PIC X(0001).                       
024714     05  RMDRPT-RMD-MAN-CALC-3 PIC X(0001).                       
024716     05  FILLER                PIC X(0002).                       
024718     05  RMDRPT-DIST-FREQ-3.                                      
024720         10  RMDRPT-DS-NTRVL-3 PIC XXXX.                          
024722         10  FILLER            PIC X.                             
024724         10  RMDRPT-DS-FREQ-3  PIC X.                             
024726     05  FILLER                PIC X(0001).                       
024728     05  RMDRPT-OLD-DS-AMT-3   PIC Z,ZZZ,ZZZ.99.                  
024730     05  FILLER                PIC X(0001).                       
024732     05  RMDRPT-NEW-DS-AMT-3   PIC Z,ZZZ,ZZZ.99.                  
024734     05  FILLER                PIC X(0028).                       
024736* 004 LINE RECORD FOLLOWS                                         
024738 01  RMDRPT-REC-4.                                                
024740     02  Z-VA-RMDRPT-REC-4     PIC  X(00160) VALUE SPACES.        
024742     02  Z-NX-RMDRPT-REC-4     REDEFINES Z-VA-RMDRPT-REC-4.       
024744     05  FILLER                PIC X(0001).                       
024746     05  RMDRPT-NAME-4         PIC X(0030).                       
024748     05  FILLER                PIC X(0004).                       
024750     05  RMDRPT-REMARK-4       PIC X(0040).                       
024752     05  FILLER                PIC X(0001).                       
024754     05  RMDRPT-REMARK2-4      PIC X(0023).                       
024756     05  FILLER                PIC X(0001).                       
024758     05  RMDRPT-DS-METH-4      PIC X(0004).                       
024760     05  FILLER                PIC X(0017).                       
024762     05  RMDRPT-WH-MSG-4       PIC X(0010).                       
024764     05  FILLER                PIC X(0029).                       
024766* 005 LINE RECORD FOLLOWS                                         
024768 01  RMDRPT-REC-8.                                                
024770     02  Z-VA-RMDRPT-REC-8     PIC  X(00160) VALUE SPACES.        
024772     02  Z-NX-RMDRPT-REC-8     REDEFINES Z-VA-RMDRPT-REC-8.       
024774     05  FILLER                PIC X(0001).                       
024776     05  RMDRPT-NAME-8         PIC X(0030).                       
024778     05  FILLER                PIC X(0129).                       
024780* 009 LINE RECORD FOLLOWS                                         
024782  01 WS-MINDIST.                                                  
024784     05  WS-AGE                   PIC 9(03).                      
024786     05  WS-SP-AGE                PIC 9(03).                      
024788     05  WS-AGE-COUNT             PIC 9(03).                      
024790     05  WS-MD-COUNT              PIC 9(04).                      
024792     05  WS-FACTOR                PIC 99V9.                       
024794     05  WS-MD-AGE-DIFF           PIC S9(03).                     
024796     05  WS-BNF-AGE               PIC 9(03).                      
024798     05  WS-MD-FMV                PIC S9(12)V99.                  
024800     05  WS-MD-AGE                PIC 9(03).                      
024802     05  WS-MD-BN-AGE             PIC 9(03).                      
024804     05  WS-MD-SPOUSE             PIC X(01).                      
024806     05  WS-MD-AMT                PIC S9(12)V99.                  
024808     05  WS-MD-TBL                PIC 9(01).                      
024810     05  WS-MD-FACT               PIC 9(02)V9.                    
024812     05  WS-CUST-YAD              PIC 9(08) VALUE 0.              
024814     05  WS-NUM-YR-YAD            PIC 9(03) VALUE 0.              
024816 01  RMDRPT2-REC-3.                                               
024818     02  Z-VA-RMDRPT2-REC-3    PIC  X(00160) VALUE SPACES.        
024820     02  Z-NX-RMDRPT2-REC-3    REDEFINES Z-VA-RMDRPT2-REC-3.      
024822     05  FILLER                PIC X(0001).                       
024824     05  RMDRPT2-CUST-3        PIC XXXXXXXXXXXX.                  
024826     05  FILLER                PIC X(0001).                       
024828     05  RMDRPT2-ACCT-3        PIC XXXXXXXXXX.                    
024830     05  FILLER                PIC X(0002).                       
024832     05  RMDRPT2-BIRTH-DT-3    PIC XXXXXXXXXX.                    
024834     05  FILLER                PIC X(0002).                       
024836     05  RMDRPT2-AGE-DATE-3    PIC XXXXXXXXXX.                    
024838     05  FILLER                PIC X(0002).                       
024840     05  RMDRPT2-BEG-DATE-3    PIC XXXXXXXXXX.                    
024842     05  FILLER                PIC X(0002).                       
024844     05  RMDRPT2-DTH-DATE-3    PIC XXXXXXXXXX.                    
024846     05  FILLER                PIC X(0001).                       
024848     05  RMDRPT2-BAL-BEG-YR-3  PIC ZZ,ZZZ,ZZZ.99.                 
024850     05  FILLER                PIC X(0001).                       
024852     05  RMDRPT2-CUR-BAL-IND-3 PIC X(0001).                       
024854     05  FILLER                PIC X(0001).                       
024856     05  RMDRPT2-FACTOR-3      PIC 99.9.                          
024858     05  FILLER                PIC X(0001).                       
024860     05  RMDRPT2-SLASH-3       PIC X(0001).                       
024862     05  FILLER                PIC X(0001).                       
024864     05  RMDRPT2-TBL-3         PIC 9(0001).                       
024866     05  FILLER                PIC X(0001).                       
024868     05  RMDRPT2-MINDIST-3     PIC Z,ZZZ,ZZZ.99.                  
024870     05  FILLER                PIC X(0001).                       
024872     05  RMDRPT2-RMD-MAN-CALC-3                                   
024874                               PIC X(0001).                       
024876     05  FILLER                PIC X(0002).                       
024878     05  RMDRPT2-DIST-FREQ-3.                                     
024880         10  RMDRPT2-DS-NTRVL-3                                   
024882                               PIC XXXX.                          
024884         10  FILLER            PIC X.                             
024886         10  RMDRPT2-DS-FREQ-3 PIC X.                             
024888     05  FILLER                PIC X(0001).                       
024890     05  RMDRPT2-OLD-DS-AMT-3  PIC Z,ZZZ,ZZZ.99.                  
024892     05  FILLER                PIC X(0001).                       
024894     05  RMDRPT2-NEW-DS-AMT-3  PIC Z,ZZZ,ZZZ.99.                  
024896     05  FILLER                PIC X(0014).                       
024898* 004 LINE RECORD FOLLOWS                                         
024900 01  RMDRPT2-REC-4.                                               
024902     02  Z-VA-RMDRPT2-REC-4    PIC  X(00160) VALUE SPACES.        
024904     02  Z-NX-RMDRPT2-REC-4    REDEFINES Z-VA-RMDRPT2-REC-4.      
024906     05  FILLER                PIC X(0001).                       
024908     05  RMDRPT2-NAME-4        PIC X(0030).                       
024910     05  FILLER                PIC X(0004).                       
024912     05  RMDRPT2-REMARK-4      PIC X(0040).                       
024914     05  FILLER                PIC X(0001).                       
024916     05  RMDRPT2-REMARK2-4     PIC X(0023).                       
024918     05  FILLER                PIC X(0001).                       
024920     05  RMDRPT2-DS-METH-4     PIC X(0004).                       
024922     05  FILLER                PIC X(0017).                       
024924     05  RMDRPT2-WH-MSG-4      PIC X(0010).                       
024926     05  FILLER                PIC X(0029).                       
024928* 005 LINE RECORD FOLLOWS                                         
024930 01  RMDRPT2-REC-8.                                               
024932     02  Z-VA-RMDRPT2-REC-8    PIC  X(00160) VALUE SPACES.        
024934     02  Z-NX-RMDRPT2-REC-8    REDEFINES Z-VA-RMDRPT2-REC-8.      
024936     05  FILLER                PIC X(0001).                       
024938     05  RMDRPT2-NAME-8        PIC X(0030).                       
024940     05  FILLER                PIC X(0129).                       
024942* 009 LINE RECORD FOLLOWS                                         
024944 01 PCR-SPEC-RECORD.                                              
024946                                                                  
024948**  SPECS FOR 999 PCR                                             
024950   05  SPECS-AREA.                                                
024952     10  SPECS-GRACE-IN-PROC             PIC 9(2).                
024954     10  SPECS-GRACE-CLOSE               PIC 9(2).                
024956     10  SPECS-PRE-MAT                   PIC 9(2).                
024958     10  SPECS-LSR-PILOT                 PIC X(1).                
024960     10  SPECS-CHK-RECON                 PIC 9(8).                
024962     10  SPECS-BR-ADDR                   PIC X(1).                
024964     10  SPECS-TIN-SUPPRESS              PIC X(1).                
024966     10  SPECS-NO-IN-PROC                PIC X(1).                
024968     10  SPECS-RMD-OVERRIDE              PIC X(1).                
024970     10  SPECS-PPP-PILOT                 PIC X(1).                
024972     10  SPECS-RETURN-ENVELOPE           PIC X(1).                
024974     10  SPECS-LSTCONT-DDACOMB           PIC X(1).                
024976     10  SPECS-LSTCONT-TDASTMT           PIC X(1).                
024978     10  SPECS-LSTCONT-INTNTC            PIC X(1).                
024980     10  SPECS-LSTCONT-ALLNTC            PIC X(1).                
024982     10  SPECS-LSTCONT-CHECKS            PIC X(1).                
024984     10  SPECS-LSTCONT-DISTREC           PIC X(1).                
024986     10  SPECS-COMB-AUTO-RMD-ADJUST      PIC X(1).                
024988     10  SPECS-IGL-HIGH-BAL              PIC 9(6).                
024990     10  SPECS-AVAIL-CAP-INT             PIC X(1).                
024992     10  SPECS-CNV-TOT-DNLOAD            PIC 9(08).               
024994     10  SPECS-CNV-TOT-DNLOAD-R REDEFINES                         
024996         SPECS-CNV-TOT-DNLOAD.                                    
024998         15 SPECS-CNV-TOT-DNLOAD-X       PIC X(08).               
025000     10  FILLER                          PIC X(13).               
025002     10  SPECS-ADDR-ALERT-DAYS           PIC 999.                 
025004     10  SPECS-COMB-SEND-CERT            PIC X(1).                
025006     10  SPECS-APPLY-GRACE-AT-SR         PIC X(1).                
025008     10  SPECS-DB-SUFFIX                 PIC X(1).                
025010     10  SPECS-EOY-YTD-ROLL              PIC X(1).                
025012     10  SPECS-COMB-DDA-OPT              PIC X(1).                
025014     10  SPECS-CONTINUE                  PIC X(1).                
025016                                                                  
025018   05  OLD-SPECS-AREA.                                            
025020     10  OLD-SPECS-GRACE-IN-PROC         PIC 9(2).                
025022     10  OLD-SPECS-GRACE-CLOSE           PIC 9(2).                
025024     10  OLD-SPECS-PRE-MAT               PIC 9(2).                
025026     10  OLD-SPECS-LSR-PILOT             PIC X(1).                
025028     10  OLD-SPECS-CHK-RECON             PIC 9(8).                
025030     10  OLD-SPECS-BR-ADDR               PIC X(1).                
025032     10  OLD-SPECS-TIN-SUPPRESS          PIC X(1).                
025034     10  OLD-SPECS-NO-IN-PROC            PIC X(1).                
025036     10  OLD-SPECS-RMD-OVERRIDE          PIC X(1).                
025038     10  OLD-SPECS-PPP-PILOT             PIC X(1).                
025040     10  OLD-SPECS-RETURN-ENVELOPE       PIC X(1).                
025042     10  OLD-SPECS-LSTCONT-DDACOMB       PIC X(1).                
025044     10  OLD-SPECS-LSTCONT-TDASTMT       PIC X(1).                
025046     10  OLD-SPECS-LSTCONT-INTNTC        PIC X(1).                
025048     10  OLD-SPECS-LSTCONT-ALLNTC        PIC X(1).                
025050     10  OLD-SPECS-LSTCONT-CHECKS        PIC X(1).                
025052     10  OLD-SPECS-LSTCONT-DISTREC       PIC X(1).                
025054     10  OLD-SPECS-COMB-AUTO-RMD-ADJUST  PIC X(1).                
025056     10  OLD-SPECS-IGL-HIGH-BAL          PIC 9(6).                
025058     10  OLD-SPECS-AVAIL-CAP-INT         PIC X(1).                
025060     10  OLD-SPECS-CNV-TOT-DNLOAD        PIC 9(08).               
025062     10  OLD-SPECS-CNV-TOT-DNLOAD-R REDEFINES                     
```

⚠️  This is the source code you must document.
    386 lines from 12142 to 12527.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

