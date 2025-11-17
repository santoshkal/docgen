# LLM Request Debug File
Generated: 2025-11-14T17:52:42.533145

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 8/55
- **Model**: gpt-4.1
- **Chunk Number**: 8
- **Pass Number**: 3
- **Attempt Number**: 2 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~10,125 tokens
- **Total Input**: ~12,083 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 8/55" (ID: detailed-code-explanation)

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


**CHUNK 8 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-14T17:36:35.036798", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 8 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 2770 to 3211 (442 lines)\nChunk Tokens (estimated): ~7,792\nActual Input Tokens: 9,198 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 2770-3211 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 8 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 8 of 55.\n\n\n=============================================================================\nCHUNK 8 SOURCE CODE (Lines 2770-3211)\n=============================================================================\n\n```cobol\n005548 01  GWS-PRT-RMT-TABLE.                                           \n005550     05  GWS-PRT-RMT-TBL             OCCURS 999 TIMES.            \n005552         10  GWS-RMT-BR-BK.                                       \n005554             15  GWS-RMT-BR          PIC X(02).                   \n005556             15  GWS-RMT-BK          PIC X(03).                   \n005558         10  GWS-RMT-RPT-TYPE        PIC 9(01).                   \n005560 01  GWS-PRT-RMT-TABLE-NEW1.                                      \n005562     05  GWS-PRT-RMT-TBL-NEW1        OCCURS 9998 TIMES.           \n005564         10  GWS-RMT-BR-BK-NEW.                                   \n005566             15  GWS-RMT-BR-NEW      PIC X(02).                   \n005568             15  GWS-RMT-BK-NEW      PIC X(04).                   \n005570 01  GWS-PRT-RMT-TABLE-NEW2.                                      \n005572     05  GWS-PRT-RMT-TBL-NEW2        OCCURS 9998 TIMES.           \n005574         10  GWS-RMT-RPT-TYPE-NEW    PIC 9(01).                   \n005576 01  GWS-RPT-TYPE                    PIC 9(01) VALUE 0.           \n005578 01  GWS-RMT-PRT-OPTION              PIC 9(01) VALUE 0.           \n005580 01  GWS-RMT-SPEC-APPL               PIC X(03) VALUE SPACES.      \n005582 01  GWS-RMT-WORK-APPL.                                           \n005584     05  GWS-RMT-WORK-APPL-1X        PIC X(01) VALUE SPACE.       \n005586     05  FILLER                      PIC X(02) VALUE SPACES.      \n005588 01  GWS-RMT-BK-FLAG                 PIC 9(01) VALUE 0.           \n005590 01  GWS-BKFILE-OPEN                 PIC 9(01) VALUE 0.           \n005592 01  GWS-RMT-EXT                     PIC X(03) VALUE \"000\".       \n005594 01  GWS-CTR                         PIC 9(03) VALUE 0.           \n005596 01  GWS-CTR-NEW                     PIC 9(04) VALUE 0.           \n005598 01  GWS-HDG-WRNING-FLAG             PIC 9(01) VALUE 0.           \n005600 01  GWS-BK-HLD                      PIC 9(03).                   \n005602 01  GWS-BK-HLD-NEW                  PIC 9(04).                   \n005604 01  GWS-GL-HLD                      PIC X(03).                   \n005606 01  GWS-BR-HLD                      PIC 9(02).                   \n005608 01  TPDECODE-WKA.                                                \n005610     05  TP-DECODE-WKA OCCURS 9 TIMES.                            \n005612         10  TP-SUBSCRIPT            PIC X(01).                   \n005614         10  TP-SUB                  PIC 9(02) OCCURS 5 TIMES.    \n005616*=================================================================\n005618 01  PR-LINE-TP.                                                  \n005620     05  PR-LN-LTR                   PIC X(16) OCCURS 8 TIMES.    \n005622 01  TP-SUB-CNT                      PIC 9(02).                   \n005624 01  TP-LN-CT                        PIC 9(02) VALUE 1.           \n005626 01  TP-AR                           PIC 9(02).                   \n005628 01  TP-LN-DPTH                      PIC 9(02) VALUE 1.           \n005630 01  TP-LN-POS                       PIC 9(02) VALUE 0.           \n005632 01  TP-SKIP                         PIC 9(01) VALUE 1.           \n005634 01  GWS-NEW-PRT-LABEL-AREA.                                      \n005636     05  GWS-NEW-PRT-LABEL.                                       \n005638         10  GWS-NPRT-NAMES.                                      \n005640             15  GWS-NPRT-CST        PIC X(05) VALUE \"PRINT\".     \n005642             15  GWS-NPRT-S1         PIC X(01) VALUE \"/\".         \n005644             15  GWS-NPRT-DC         PIC 9(02) VALUE ZEROS.       \n005646             15  GWS-NPRT-S2         PIC X(01) VALUE \"/\".         \n005648             15  GWS-NPRT-APP        PIC X(03) VALUE \"000\".       \n005650             15  GWS-NPRT-S3         PIC X(01) VALUE \"/\".         \n005652             15  GWS-NPRT-COPIES     PIC 9(02) VALUE ZEROS.       \n005654             15  GWS-NPRT-TYPE       PIC X(02) VALUE \"SP\".        \n005656             15  GWS-NPRT-S4         PIC X(01) VALUE \"/\".         \n005658             15  GWS-NPRT-BK         PIC 9(04) VALUE ZEROS.       \n005660             15  GWS-NPRT-S5         PIC X(01) VALUE \"/\".         \n005662             15  GWS-NPRT-CNTRV      PIC X(01) VALUE \"I\".         \n005664             15  GWS-NPRT-RP         PIC X(01) VALUE \"0\".         \n005666             15  GWS-NPRT-EXP        PIC X(02) VALUE \"00\".        \n005668             15  GWS-NPRT-S6         PIC X(01) VALUE \"/\".         \n005670             15  GWS-NPRT-LNODE.                                  \n005672                 20  GWS-NPRT-DD     PIC 9(02) VALUE 0.           \n005674                 20  GWS-NPRT-APP2   PIC X(01) VALUE \"0\".         \n005676                 20  GWS-NPRT-TYPE2  PIC X(02) VALUE \"SP\".        \n005678                 20  GWS-NPRT-RPT-NO PIC X(03) VALUE SPACES.      \n005680             15  GWS-NPRT-ON         PIC X(04) VALUE \" ON \".      \n005682             15  GWS-NPRT-PACK       PIC X(10) VALUE SPACES.      \n005684             15  GWS-NPRT-PERIOD     PIC X(01) VALUE SPACE.       \n005686     05  GWS-NEW-LABEL REDEFINES GWS-NEW-PRT-LABEL.               \n005688         10  GWS-NEW-LABEL-1-36      PIC X(36).                   \n005690         10  FILLER                  PIC X(15).                   \n005692 01  GWS-NEW-PRT-LABEL-CHG-AREA.                                  \n005694     05  GWS-NEW-LABEL-CHG.                                       \n005696         10  GWS-NP-CHG-NAMES.                                    \n005698             15  FILLER              PIC X(09).                   \n005700             15  GWS-NP-APPL         PIC X(03).                   \n005702             15  FILLER              PIC X(01).                   \n005704             15  GWS-NP-COPIES       PIC 9(02).                   \n005706             15  GWS-NP-TYPE         PIC X(02).                   \n005708             15  FILLER              PIC X(01).                   \n005710             15  GWS-NP-BK           PIC 9(04).                   \n005712             15  FILLER              PIC X(01).                   \n005714             15  GWS-NP-CNTRV        PIC X(01).                   \n005716             15  GWS-NP-RP           PIC X(01).                   \n005718             15  FILLER              PIC X(08).                   \n005720             15  GWS-NP-RPT-NO       PIC X(03).                   \n005722             15  FILLER              PIC X(15).                   \n005724 01  GWS-LONG-PRTNAMES-NEW           PIC 9(01) VALUE 0.           \n005726 01  GWS-EOM-FLAG                    PIC X(01) VALUE SPACES.      \n005728 01  GWS-CNTR-VIEW                   PIC 9(01) VALUE 0.           \n005730 01  GWS-PRT-NEW                     PIC 9(01) VALUE 0.           \n005732 01  GWS-APPL-NO                     PIC 9(02) VALUE 0.           \n005734 01  GWS-PREV-OPEN                   PIC 9(01) VALUE 0.           \n005736 01  GWS-PREV-OPENX                  PIC 9(01) VALUE 0.           \n005738 01  GWS-SPCDB-OPEN                  PIC 9(01) VALUE 0.           \n005740 01  GWS-PREV-OPEN1                  PIC 9(01) VALUE 0.           \n005742 01  GWS-PREV-OPEN2                  PIC 9(01) VALUE 0.           \n005744 01  GWS-PREV-OPEN3                  PIC 9(01) VALUE 0.           \n005746 01  GWS-PREV-OPEN4                  PIC 9(01) VALUE 0.           \n005748 01  GWS-PREV-OPEN5                  PIC 9(01) VALUE 0.           \n005750 01  GWS-PREV-OPEN6                  PIC 9(01) VALUE 0.           \n005752 01  GWS-PREV-OPEN7                  PIC 9(01) VALUE 0.           \n005754 01  GWS-PREV-OPEN8                  PIC 9(01) VALUE 0.           \n005756 01  GWS-PREV-OPEN9                  PIC 9(01) VALUE 0.           \n005758 01  GWS-PREV-OPEN10                 PIC 9(01) VALUE 0.           \n005760                                                                  \n005762 01  WS-REDEFINE-AREA-3.                                          \n005764     02  AD-ADDRESS-AREA.                                         \n005766     05  ADD-ADDR-G.                                              \n005768         10  AD-ADDRESS-1                PIC X(40).               \n005770         10  AD-ADDRESS-2                PIC X(40).               \n005772         10  AD-ADDRESS-3                PIC X(40).               \n005774         10  AD-ADDRESS-4                PIC X(40).               \n005776     02  AD-ADDRESS-AREA-R REDEFINES AD-ADDRESS-AREA.             \n005778     05  AD-STR-TABLE                  PIC X(40) OCCURS 4 TIMES.  \n005780     02  ST-ABBRE-TABLE.                                          \n005782     05 STATE-ABBRE-LINE.                                         \n005784         10  FILLER                      PIC X(05)                \n005786             VALUE \"ALAAL\".                                       \n005788         10  FILLER                      PIC X(05)                \n005790             VALUE \"ALAAK\".                                       \n005792         10  FILLER                      PIC X(05)                \n005794             VALUE \"ARIAZ\".                                       \n005796         10  FILLER                      PIC X(05)                \n005798             VALUE \"ARKAR\".                                       \n005800         10  FILLER                      PIC X(05)                \n005802             VALUE \"CALCA\".                                       \n005804         10  FILLER                      PIC X(05)                \n005806             VALUE \"COLCO\".                                       \n005808         10  FILLER                      PIC X(05)                \n005810             VALUE \"CONCT\".                                       \n005812         10  FILLER                      PIC X(05)                \n005814             VALUE \"DELDE\".                                       \n005816         10  FILLER                      PIC X(05)                \n005818             VALUE \"FLAFL\".                                       \n005820         10  FILLER                      PIC X(05)                \n005822             VALUE \"FLOFL\".                                       \n005824         10  FILLER                      PIC X(05)                \n005826             VALUE \"GEOGA\".                                       \n005828         10  FILLER                      PIC X(05)                \n005830             VALUE \"HAWHI\".                                       \n005832         10  FILLER                      PIC X(05)                \n005834             VALUE \"IDAID\".                                       \n005836         10  FILLER                      PIC X(05)                \n005838             VALUE \"ILLIL\".                                       \n005840         10  FILLER                      PIC X(05)                \n005842             VALUE \"INDIN\".                                       \n005844         10  FILLER                      PIC X(05)                \n005846             VALUE \"IOWIA\".                                       \n005848         10  FILLER                      PIC X(05)                \n005850             VALUE \"KANKA\".                                       \n005852         10  FILLER                      PIC X(05)                \n005854             VALUE \"KENKY\".                                       \n005856         10  FILLER                      PIC X(05)                \n005858             VALUE \"LOULA\".                                       \n005860         10  FILLER                      PIC X(05)                \n005862             VALUE \"MAIME\".                                       \n005864         10  FILLER                      PIC X(05)                \n005866             VALUE \"MARMD\".                                       \n005868         10  FILLER                      PIC X(05)                \n005870             VALUE \"MASMA\".                                       \n005872         10  FILLER                      PIC X(05)                \n005874             VALUE \"MICMI\".                                       \n005876         10  FILLER                      PIC X(05)                \n005878             VALUE \"MINMN\".                                       \n005880         10  FILLER                      PIC X(05)                \n005882             VALUE \"MISMS\".                                       \n005884         10  FILLER                      PIC X(05)                \n005886             VALUE \"MISMO\".                                       \n005888         10  FILLER                      PIC X(05)                \n005890             VALUE \"MONMT\".                                       \n005892         10  FILLER                      PIC X(05)                \n005894             VALUE \"NEBNE\".                                       \n005896         10  FILLER                      PIC X(05)                \n005898             VALUE \"NEVNV\".                                       \n005900         10  FILLER                      PIC X(05)                \n005902             VALUE \"NHANH\".                                       \n005904         10  FILLER                      PIC X(05)                \n005906             VALUE \"NJENJ\".                                       \n005908         10  FILLER                      PIC X(05)                \n005910             VALUE \"NMENM\".                                       \n005912         10  FILLER                      PIC X(05)                \n005914             VALUE \"NYONY\".                                       \n005916         10  FILLER                      PIC X(05)                \n005918             VALUE \"NCANC\".                                       \n005920         10  FILLER                      PIC X(05)                \n005922             VALUE \"NDAND\".                                       \n005924         10  FILLER                      PIC X(05)                \n005926             VALUE \"OHIOH\".                                       \n005928         10  FILLER                      PIC X(05)                \n005930             VALUE \"OKLOK\".                                       \n005932         10  FILLER                      PIC X(05)                \n005934             VALUE \"OREOR\".                                       \n005936         10  FILLER                      PIC X(05)                \n005938             VALUE \"PENPA\".                                       \n005940         10  FILLER                      PIC X(05)                \n005942             VALUE \"RHORI\".                                       \n005944         10  FILLER                      PIC X(05)                \n005946             VALUE \"SCASC\".                                       \n005948         10  FILLER                      PIC X(05)                \n005950             VALUE \"SDASD\".                                       \n005952         10  FILLER                      PIC X(05)                \n005954             VALUE \"TENTN\".                                       \n005956         10  FILLER                      PIC X(05)                \n005958             VALUE \"TEXTX\".                                       \n005960         10  FILLER                      PIC X(05)                \n005962             VALUE \"UTAUT\".                                       \n005964         10  FILLER                      PIC X(05)                \n005966             VALUE \"VERVT\".                                       \n005968         10  FILLER                      PIC X(05)                \n005970             VALUE \"VIRVA\".                                       \n005972         10  FILLER                      PIC X(05)                \n005974             VALUE \"WASWA\".                                       \n005976         10  FILLER                      PIC X(05)                \n005978             VALUE \"WVIWV\".                                       \n005980         10  FILLER                      PIC X(05)                \n005982             VALUE \"WISWI\".                                       \n005984         10  FILLER                      PIC X(05)                \n005986             VALUE \"WYOWY\".                                       \n005988     02  STATE-ABBRE-TABLE-R REDEFINES ST-ABBRE-TABLE.            \n005990     05  ST-AND-ABBRE                    OCCURS 51 TIMES          \n005992                                             INDEXED BY ST-SUB.   \n005994         10  WS-STATE                    PIC X(03).               \n005996         10  WS-ST-ABBRE                 PIC X(02).               \n005998     02  FULL-ST-ABBRE-TABLE.                                     \n006000     05  FULL-ST-LINE.                                            \n006002         10  FILLER                      PIC X(07)                \n006004             VALUE \"ALABAAL\".                                     \n006006         10  FILLER                      PIC X(07)                \n006008             VALUE \"ALASKAK\".                                     \n006010         10  FILLER                      PIC X(07)                \n006012             VALUE \"MISSIMS\".                                     \n006014         10  FILLER                      PIC X(07)                \n006016             VALUE \"MISSOMO\".                                     \n006018     02  FULL-ST-ABBRE-TABLE-R REDEFINES FULL-ST-ABBRE-TABLE.     \n006020     05  FULL-ST-AND-ABBRE               OCCURS 4 TIMES           \n006022                                           INDEXED BY FULL-ST-SUB.\n006024         10  WS-FULL-STATE               PIC X(05).               \n006026         10  WS-FULL-ST-ABBRE            PIC X(02).               \n006028 01  WS-SUB-ADDR                         PIC 9(01) VALUE 0.       \n006030 01  AD-ADDRESS                          PIC X(40).               \n006032 01  AD-WORK-TABLE.                                               \n006034     05  AD-ADDR-TABLE OCCURS 10 TIMES.                           \n006036         10  AD-TABLE-1ST-TEN.                                    \n006038             15  AD-TABLE-1ST-NINE.                               \n006040                 20  AD-TABLE-1ST-FIVE.                           \n006042                     25  AD-TABLE-1ST-CHAR   PIC X(01).           \n006044                     25  AD-TABLE-2ND-CHAR   PIC X(01).           \n006046                     25  FILLER              PIC X(03).           \n006048                 20  FILLER                  PIC X(04).           \n006050             15  FILLER                      PIC X(01).           \n006052         10  AD-TABLE-1ST-TEN-R REDEFINES AD-TABLE-1ST-TEN.       \n006054             15  FILLER                      PIC X(06).           \n006056             15  AD-TABLE-LST-FOUR           PIC X(04).           \n006058         10  AD-TABLE-LST-30             PIC X(30).               \n006060 01  AD-FINISHED-ADDRESS.                                         \n006062     05  AD-CITY                         PIC X(40).               \n006064     05  FILLER                          PIC X(02).               \n006066     05  AD-STATE.                                                \n006068         10  AD-STATE-1ST-5.                                      \n006070             15  AD-STATE-1ST-4.                                  \n006072                 20  AD-STATE-1ST-3      PIC X(03).               \n006074                 20  FILLER              PIC X(01).               \n006076             15  FILLER                  PIC X(01).               \n006078         10  FILLER                      PIC X(05).               \n006080     05  FILLER                          PIC X(02).               \n006082     05  AD-ZIP-CODE.                                             \n006084         10  AD-ZIP-CODE1X5              PIC X(05).               \n006086         10  AD-ZIP-CODE-LST4            PIC X(04).               \n006088 01  AD-TEMP-CITY-TABLE.                                          \n006090     05  AD-TEMP-TABLE                  PIC X(40) OCCURS 4 TIMES. \n006092 01  AD-ALPHA-WORK-FIELDS.                                        \n006094     05  AD-ERROR-MESSAGE                PIC X(20).               \n006096     05  AD-ZIP-ERROR-MESSG              PIC X(20).               \n006098 01  AD-NUMERIC-WORK-FIELDS.                                      \n006100     05  AD-NO-LINES                     PIC 9(01).               \n006102     05  AD-SUB-1                        PIC 9(02).               \n006104     05  WS-STORE-AD-SUB                 PIC 9(02).               \n006106     05  WS-ST-SUB                       PIC 9(02).               \n006108     05  AD-SUB-A                        PIC 9(02).               \n006110     05  AD-SUB-MAX                      PIC 9(02).               \n006112     05  AD-ERROR-FLAG                   PIC 9(01).               \n006114     05  AD-NO-ALPHA-ENTRIES             PIC 9(02).               \n006116     05  AD-NO-NUMERIC-ENTRIES           PIC 9(02).               \n006118     05  AD-ZIPCD-ERROR-FLAG             PIC 9(01).               \n006120     05  AD-NO-FIELDS                    PIC 9(02).               \n006122     05  AD-WORK-FLAG                    PIC 9(02).               \n006124     05  AD-SUB-N                        PIC 9(02).               \n006126     05  AD-GOOD-ZIP-SW                  PIC 9(01).               \n006128     05  AD-SUB-UNSTR                    PIC 9(02).               \n006130     05  AD-SUB-P                        PIC 9(02).               \n006132     05  ZIP-SUB                         PIC 9(02).               \n006134 01  AD-STREET-ADDRESS-1                 PIC X(40).               \n006136 01  AD-STREET-ADDRESS                   PIC X(40).               \n006138 01  AD-NUMERIC-STREET-WK-FIELDS.                                 \n006140     05  AD-STREET-ERROR-FLAG            PIC 9(01).               \n006142     05  AD-SUB-ST                       PIC 9(02).               \n006144     05  AD-SUB-ST-1                     PIC 9(02).               \n006146     05  AD-CITY-SUB-HOLD                PIC 9(02).               \n006148     05  AD-WARN-FLAG                    PIC 9(01).               \n006150 01  AD-ALPHA-STREET-WK-FIELDS.                                   \n006152     05  AD-STREET-ERROR-MESSAGE         PIC X(18).               \n006154     05  AD-WARN-MESSG                   PIC X(18).               \n006156 01  AD-STATE-ABBRE                      PIC X(02).               \n006158 01  WS-STORE-STATE.                                              \n006160     05  WS-STATE-FIRST-2                PIC X(02).               \n006162     05  WS-STATE-FILLER                 PIC X(08).               \n006164 01  ABBRE-FLAG                          PIC 9(01) VALUE 0.       \n006166                                                                  \n006168 01  WS-REDEFINE-AREA-4.                                          \n006170     02  WS-BUILD-NAME-INPUT-AREA.                                \n006172     05  WS-BNI-KEY                   PIC X(14).                  \n006174     05  WS-BNI-FIRST                 PIC X(40).                  \n006176     05  WS-BNI-MID                   PIC X(20).                  \n006178     05  WS-BNI-LAST                  PIC X(40).                  \n006180     05  WS-BNI-PREFIX                PIC X(12).                  \n006182     05  WS-BNI-SUFFIX                PIC X(12).                  \n006184     05  WS-BNI-FAMILIAR              PIC X(20).                  \n006186     05  WS-BNI-PRINT-PREFIX-FLAG     PIC X(01).                  \n006188     05  WS-BNI-PRINT-SUFFIX-FLAG     PIC X(01).                  \n006190     05  WS-BNI-DESIGNATION           PIC X(20).                  \n006192     02  WS-BUILD-NAME-TRIM-VALUES       PIC X(18) VALUE          \n006194         \"401240201220HDTTDD\".                                    \n006196     02  WS-BUILD-NAME-TRIM REDEFINES WS-BUILD-NAME-TRIM-VALUES.  \n006198     05  WS-BNA-MAXLEN OCCURS 6 TIMES PIC 9(02).                  \n006200     05  WS-BNA-TRIM   OCCURS 6 TIMES PIC X(01).                  \n006202     02  WS-BUILD-NAME-POINTER-VALUES    PIC X(28) VALUE          \n006204         \"6123456623415621644443134555\".                          \n006206     02  WS-BUILD-NAME-POINTER REDEFINES                          \n006208                                   WS-BUILD-NAME-POINTER-VALUES.  \n006210     05  WS-BNA-POINTER-SET           OCCURS 4 TIMES.             \n006212         10  WS-BNA-MAXITEMS          PIC 9(01).                  \n006214         10  WS-BNA-POINTER           OCCURS 6 TIMES              \n006216                                      PIC 9(01).                  \n006218     02  WS-BUILD-NAME-ARRAY-NUM.                                 \n006220     05  WS-BNA-ACTLEN OCCURS 6 TIMES PIC  9(02) COMP.            \n006222     05  WS-BNW-REMAIN                PIC S9(03) COMP.            \n006224     05  WS-BNS-ORDR                  PIC  9(02) COMP.            \n006226     05  WS-BNS-PASS                  PIC  9(02) COMP.            \n006228     05  WS-BNS-VALU                  PIC  9(02) COMP.            \n006230     05  WS-BNS-CHRI                  PIC  9(02) COMP.            \n006232     05  WS-BNS-CHRO                  PIC  9(02) COMP.            \n006234     02  WS-BUILD-NAME-ARRAY-ALPHA.                               \n006236     05  WS-BNA-VALUE                 OCCURS  6 TIMES.            \n006238         10  WS-BNA-CHAR              OCCURS 40 TIMES             \n006240                                      PIC X(01).                  \n006242     02  WS-BUILD-NAME-ARRAY-OUTPUT.                              \n006244     05  WS-BNO-OUTPUT.                                           \n006246         10  WS-BNO-NAME              OCCURS 4 TIMES.             \n006248             15  WS-BNO-CHAR          OCCURS 40 TIMES             \n006250                                      PIC X(01).                  \n006252     05  WS-BNO-OUTPUT-AREA REDEFINES WS-BNO-OUTPUT.              \n006254         10  WS-BNO-NAME-LNF          PIC X(40).                  \n006256         10  WS-BNO-NAME-FNF          PIC X(40).                  \n006258         10  WS-BNO-NAME-BUSINESS     PIC X(40).                  \n006260         10  WS-BNO-RPT-NAME          PIC X(40).                  \n006262     02  WS-BNO-MAXLEN                   PIC 9(02) COMP VALUE 40. \n006264                                                                  \n006266 01  SPEC-CARD-14.                                                \n006268     05  FILLER                       PIC X(07).                  \n006270     05  SPEC-SEGMINT                 PIC X(01).                  \n006272     05  SPEC-SHELTERED-HRBR          PIC X(01).                  \n006274     05  SPEC-VOICE-RESPONSE-PHONE-NO PIC 9(10).                  \n006276     05  SPEC-BANK-URL.                                           \n006278         10  SPEC-BANK-URL-1          PIC X(30).                  \n006280         10  SPEC-BANK-URL-2          PIC X(20).                  \n006282     05  SPEC-LNS-ALT-FMT-DLQ-NTC-PHONE PIC 9(10).                \n006284     05  SPEC-CSIWIRE-BILLING         PIC X(01).                  \n006286     05  FILLER                       PIC X(01).                  \n006288     05  FILLER-UNAVAIL-14            PIC X(01).                  \n006290 01  SPEC-CARD-15.                                                \n006292     05  FILLER                       PIC X(07).                  \n006294     05  FILLER                       PIC X(74).                  \n006296     05  FILLER-UNAVAIL-15            PIC X(01).                  \n006298 01  SPEC-CARD-16.                                                \n006300     05  FILLER                       PIC X(07).                  \n006302     05  FILLER                       PIC X(74).                  \n006304     05  FILLER-UNAVAIL-16            PIC X(01).                  \n006306*L                                                                \n006308                                                                  \n006310*=================================================================\n006312*                      DMS ROUTINE WORKING STORAGE                \n006314*=================================================================\n006316 01  WS-DMS-NAMES.                                                \n006318     05  DMS-SUB                 PIC 9(02).                       \n006320     05  WS-DMS-BKNO             PIC 9(03).                       \n006322     05  WS-APPL-CODE            PIC 9(02).                       \n006324     05  WS-RUN-DTE-ENT          PIC 9(06).                       \n006326     05  WS-RUN-DTE-ENT-R REDEFINES WS-RUN-DTE-ENT.               \n006328         10  WS-RUND-MM           PIC 9(02).                      \n006330         10  WS-RUND-DD           PIC 9(02).                      \n006332         10  WS-RUND-YY           PIC 9(02).                      \n006334     05  WS-DATE-RUN.                                             \n006336         10  WS-DMS-CC            PIC 9(02).                      \n006338         10  WS-DMS-YY            PIC 9(02).                      \n006340         10  WS-DMS-MM            PIC 9(02).                      \n006342         10  WS-DMS-DD            PIC 9(02).                      \n006344     05  WS-DATE-RUN-R REDEFINES WS-DATE-RUN                      \n006346                                 PIC 9(08).                       \n006348     05  WS-VER-SAVE             PIC 9(02).                       \n006350     05  WS-DATE-SAVE            PIC 9(08).                       \n006352     05  WS-DATE-SAVE-R REDEFINES WS-DATE-SAVE.                   \n006354       10  WS-DATE-SAVE-CC       PIC 9(02).                       \n006356       10  WS-DATE-SAVE-YY       PIC 9(02).                       \n006358       10  WS-DATE-SAVE-MM       PIC 9(02).                       \n006360       10  WS-DATE-SAVE-DD       PIC 9(02).                       \n006362     05  WS-SAVE-DATE-MMDDYY.                                     \n006364       10  WS-SAVE-MM            PIC 9(02).                       \n006366       10  WS-SAVE-DD            PIC 9(02).                       \n006368       10  WS-SAVE-YY            PIC 9(02).                       \n006370     05  WS-DMS-ERROR            PIC 9(01).                       \n006372         88  DMS-AOK                 VALUE 0.                     \n006374         88  DMS-NEXT-ERROR          VALUE 2.                     \n006376         88  DMS-FIND-ERROR          VALUE 3.                     \n006378         88  DMS-CLOSE-ERROR         VALUE 4.                     \n006380         88  DMS-OPEN-ERROR          VALUE 5.                     \n006382 01 WS-DMS-DATA-TABLE.                                            \n006384     05  WS-DMS-RECORD   OCCURS 25 TIMES.                         \n006386         10  WS-DMS-CARDS   OCCURS 25 TIMES                       \n006388                             PIC X(74).                           \n006390*                                                                 \n006392 01  RMD-LEF-TABLE-1-X.                                           \n006394   05  RMD-LEF-TABLE-1.                                           \n006396     10 FILLER PIC X(54) VALUE                                    \n006398         \"824816806797787777767758748738728718708699689679669660\".\n006400     10 FILLER PIC X(54) VALUE                                    \n006402         \"650640630621611601591582572562553543533524514504494485\".\n006404     10 FILLER PIC X(54) VALUE                                    \n006406         \"475465456446436427417407398388379370360351342333323314\".\n006408     10 FILLER PIC X(54) VALUE                                    \n006410         \"305296287279270261252244235227218210202194186178170163\".\n006412     10 FILLER PIC X(54) VALUE                                    \n006414         \"155148141134127121114108102097091086081076071067063059\".\n006416     10 FILLER PIC X(54) VALUE                                    \n006418         \"055052049046043041038036034031029027025023021019017015\".\n006420     10 FILLER PIC X(12) VALUE                                    \n006422         \"014012011010\".                                          \n006424                                                                  \n006426   05  WS-RMD-LEF-TABLE-1 REDEFINES RMD-LEF-TABLE-1.              \n006428       10  WS-RMD-TBL1-LEF           PIC 999 OCCURS 112 TIMES.    \n006430                                                                  \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    442 lines from 2770 to 3211.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 8, "total_chunks": 55, "start_line": 2770, "end_line": 3211, "line_count": 442}

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
- Source code length: 37214 characters

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
CHUNK 8 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 2770 to 3211 (442 lines)
Chunk Tokens (estimated): ~7,792
Actual Input Tokens: 9,198 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 2770-3211 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 8 of 55 chunks
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
      The source code below is only CHUNK 8 of 55.


=============================================================================
CHUNK 8 SOURCE CODE (Lines 2770-3211)
=============================================================================

```cobol
005548 01  GWS-PRT-RMT-TABLE.                                           
005550     05  GWS-PRT-RMT-TBL             OCCURS 999 TIMES.            
005552         10  GWS-RMT-BR-BK.                                       
005554             15  GWS-RMT-BR          PIC X(02).                   
005556             15  GWS-RMT-BK          PIC X(03).                   
005558         10  GWS-RMT-RPT-TYPE        PIC 9(01).                   
005560 01  GWS-PRT-RMT-TABLE-NEW1.                                      
005562     05  GWS-PRT-RMT-TBL-NEW1        OCCURS 9998 TIMES.           
005564         10  GWS-RMT-BR-BK-NEW.                                   
005566             15  GWS-RMT-BR-NEW      PIC X(02).                   
005568             15  GWS-RMT-BK-NEW      PIC X(04).                   
005570 01  GWS-PRT-RMT-TABLE-NEW2.                                      
005572     05  GWS-PRT-RMT-TBL-NEW2        OCCURS 9998 TIMES.           
005574         10  GWS-RMT-RPT-TYPE-NEW    PIC 9(01).                   
005576 01  GWS-RPT-TYPE                    PIC 9(01) VALUE 0.           
005578 01  GWS-RMT-PRT-OPTION              PIC 9(01) VALUE 0.           
005580 01  GWS-RMT-SPEC-APPL               PIC X(03) VALUE SPACES.      
005582 01  GWS-RMT-WORK-APPL.                                           
005584     05  GWS-RMT-WORK-APPL-1X        PIC X(01) VALUE SPACE.       
005586     05  FILLER                      PIC X(02) VALUE SPACES.      
005588 01  GWS-RMT-BK-FLAG                 PIC 9(01) VALUE 0.           
005590 01  GWS-BKFILE-OPEN                 PIC 9(01) VALUE 0.           
005592 01  GWS-RMT-EXT                     PIC X(03) VALUE "000".       
005594 01  GWS-CTR                         PIC 9(03) VALUE 0.           
005596 01  GWS-CTR-NEW                     PIC 9(04) VALUE 0.           
005598 01  GWS-HDG-WRNING-FLAG             PIC 9(01) VALUE 0.           
005600 01  GWS-BK-HLD                      PIC 9(03).                   
005602 01  GWS-BK-HLD-NEW                  PIC 9(04).                   
005604 01  GWS-GL-HLD                      PIC X(03).                   
005606 01  GWS-BR-HLD                      PIC 9(02).                   
005608 01  TPDECODE-WKA.                                                
005610     05  TP-DECODE-WKA OCCURS 9 TIMES.                            
005612         10  TP-SUBSCRIPT            PIC X(01).                   
005614         10  TP-SUB                  PIC 9(02) OCCURS 5 TIMES.    
005616*=================================================================
005618 01  PR-LINE-TP.                                                  
005620     05  PR-LN-LTR                   PIC X(16) OCCURS 8 TIMES.    
005622 01  TP-SUB-CNT                      PIC 9(02).                   
005624 01  TP-LN-CT                        PIC 9(02) VALUE 1.           
005626 01  TP-AR                           PIC 9(02).                   
005628 01  TP-LN-DPTH                      PIC 9(02) VALUE 1.           
005630 01  TP-LN-POS                       PIC 9(02) VALUE 0.           
005632 01  TP-SKIP                         PIC 9(01) VALUE 1.           
005634 01  GWS-NEW-PRT-LABEL-AREA.                                      
005636     05  GWS-NEW-PRT-LABEL.                                       
005638         10  GWS-NPRT-NAMES.                                      
005640             15  GWS-NPRT-CST        PIC X(05) VALUE "PRINT".     
005642             15  GWS-NPRT-S1         PIC X(01) VALUE "/".         
005644             15  GWS-NPRT-DC         PIC 9(02) VALUE ZEROS.       
005646             15  GWS-NPRT-S2         PIC X(01) VALUE "/".         
005648             15  GWS-NPRT-APP        PIC X(03) VALUE "000".       
005650             15  GWS-NPRT-S3         PIC X(01) VALUE "/".         
005652             15  GWS-NPRT-COPIES     PIC 9(02) VALUE ZEROS.       
005654             15  GWS-NPRT-TYPE       PIC X(02) VALUE "SP".        
005656             15  GWS-NPRT-S4         PIC X(01) VALUE "/".         
005658             15  GWS-NPRT-BK         PIC 9(04) VALUE ZEROS.       
005660             15  GWS-NPRT-S5         PIC X(01) VALUE "/".         
005662             15  GWS-NPRT-CNTRV      PIC X(01) VALUE "I".         
005664             15  GWS-NPRT-RP         PIC X(01) VALUE "0".         
005666             15  GWS-NPRT-EXP        PIC X(02) VALUE "00".        
005668             15  GWS-NPRT-S6         PIC X(01) VALUE "/".         
005670             15  GWS-NPRT-LNODE.                                  
005672                 20  GWS-NPRT-DD     PIC 9(02) VALUE 0.           
005674                 20  GWS-NPRT-APP2   PIC X(01) VALUE "0".         
005676                 20  GWS-NPRT-TYPE2  PIC X(02) VALUE "SP".        
005678                 20  GWS-NPRT-RPT-NO PIC X(03) VALUE SPACES.      
005680             15  GWS-NPRT-ON         PIC X(04) VALUE " ON ".      
005682             15  GWS-NPRT-PACK       PIC X(10) VALUE SPACES.      
005684             15  GWS-NPRT-PERIOD     PIC X(01) VALUE SPACE.       
005686     05  GWS-NEW-LABEL REDEFINES GWS-NEW-PRT-LABEL.               
005688         10  GWS-NEW-LABEL-1-36      PIC X(36).                   
005690         10  FILLER                  PIC X(15).                   
005692 01  GWS-NEW-PRT-LABEL-CHG-AREA.                                  
005694     05  GWS-NEW-LABEL-CHG.                                       
005696         10  GWS-NP-CHG-NAMES.                                    
005698             15  FILLER              PIC X(09).                   
005700             15  GWS-NP-APPL         PIC X(03).                   
005702             15  FILLER              PIC X(01).                   
005704             15  GWS-NP-COPIES       PIC 9(02).                   
005706             15  GWS-NP-TYPE         PIC X(02).                   
005708             15  FILLER              PIC X(01).                   
005710             15  GWS-NP-BK           PIC 9(04).                   
005712             15  FILLER              PIC X(01).                   
005714             15  GWS-NP-CNTRV        PIC X(01).                   
005716             15  GWS-NP-RP           PIC X(01).                   
005718             15  FILLER              PIC X(08).                   
005720             15  GWS-NP-RPT-NO       PIC X(03).                   
005722             15  FILLER              PIC X(15).                   
005724 01  GWS-LONG-PRTNAMES-NEW           PIC 9(01) VALUE 0.           
005726 01  GWS-EOM-FLAG                    PIC X(01) VALUE SPACES.      
005728 01  GWS-CNTR-VIEW                   PIC 9(01) VALUE 0.           
005730 01  GWS-PRT-NEW                     PIC 9(01) VALUE 0.           
005732 01  GWS-APPL-NO                     PIC 9(02) VALUE 0.           
005734 01  GWS-PREV-OPEN                   PIC 9(01) VALUE 0.           
005736 01  GWS-PREV-OPENX                  PIC 9(01) VALUE 0.           
005738 01  GWS-SPCDB-OPEN                  PIC 9(01) VALUE 0.           
005740 01  GWS-PREV-OPEN1                  PIC 9(01) VALUE 0.           
005742 01  GWS-PREV-OPEN2                  PIC 9(01) VALUE 0.           
005744 01  GWS-PREV-OPEN3                  PIC 9(01) VALUE 0.           
005746 01  GWS-PREV-OPEN4                  PIC 9(01) VALUE 0.           
005748 01  GWS-PREV-OPEN5                  PIC 9(01) VALUE 0.           
005750 01  GWS-PREV-OPEN6                  PIC 9(01) VALUE 0.           
005752 01  GWS-PREV-OPEN7                  PIC 9(01) VALUE 0.           
005754 01  GWS-PREV-OPEN8                  PIC 9(01) VALUE 0.           
005756 01  GWS-PREV-OPEN9                  PIC 9(01) VALUE 0.           
005758 01  GWS-PREV-OPEN10                 PIC 9(01) VALUE 0.           
005760                                                                  
005762 01  WS-REDEFINE-AREA-3.                                          
005764     02  AD-ADDRESS-AREA.                                         
005766     05  ADD-ADDR-G.                                              
005768         10  AD-ADDRESS-1                PIC X(40).               
005770         10  AD-ADDRESS-2                PIC X(40).               
005772         10  AD-ADDRESS-3                PIC X(40).               
005774         10  AD-ADDRESS-4                PIC X(40).               
005776     02  AD-ADDRESS-AREA-R REDEFINES AD-ADDRESS-AREA.             
005778     05  AD-STR-TABLE                  PIC X(40) OCCURS 4 TIMES.  
005780     02  ST-ABBRE-TABLE.                                          
005782     05 STATE-ABBRE-LINE.                                         
005784         10  FILLER                      PIC X(05)                
005786             VALUE "ALAAL".                                       
005788         10  FILLER                      PIC X(05)                
005790             VALUE "ALAAK".                                       
005792         10  FILLER                      PIC X(05)                
005794             VALUE "ARIAZ".                                       
005796         10  FILLER                      PIC X(05)                
005798             VALUE "ARKAR".                                       
005800         10  FILLER                      PIC X(05)                
005802             VALUE "CALCA".                                       
005804         10  FILLER                      PIC X(05)                
005806             VALUE "COLCO".                                       
005808         10  FILLER                      PIC X(05)                
005810             VALUE "CONCT".                                       
005812         10  FILLER                      PIC X(05)                
005814             VALUE "DELDE".                                       
005816         10  FILLER                      PIC X(05)                
005818             VALUE "FLAFL".                                       
005820         10  FILLER                      PIC X(05)                
005822             VALUE "FLOFL".                                       
005824         10  FILLER                      PIC X(05)                
005826             VALUE "GEOGA".                                       
005828         10  FILLER                      PIC X(05)                
005830             VALUE "HAWHI".                                       
005832         10  FILLER                      PIC X(05)                
005834             VALUE "IDAID".                                       
005836         10  FILLER                      PIC X(05)                
005838             VALUE "ILLIL".                                       
005840         10  FILLER                      PIC X(05)                
005842             VALUE "INDIN".                                       
005844         10  FILLER                      PIC X(05)                
005846             VALUE "IOWIA".                                       
005848         10  FILLER                      PIC X(05)                
005850             VALUE "KANKA".                                       
005852         10  FILLER                      PIC X(05)                
005854             VALUE "KENKY".                                       
005856         10  FILLER                      PIC X(05)                
005858             VALUE "LOULA".                                       
005860         10  FILLER                      PIC X(05)                
005862             VALUE "MAIME".                                       
005864         10  FILLER                      PIC X(05)                
005866             VALUE "MARMD".                                       
005868         10  FILLER                      PIC X(05)                
005870             VALUE "MASMA".                                       
005872         10  FILLER                      PIC X(05)                
005874             VALUE "MICMI".                                       
005876         10  FILLER                      PIC X(05)                
005878             VALUE "MINMN".                                       
005880         10  FILLER                      PIC X(05)                
005882             VALUE "MISMS".                                       
005884         10  FILLER                      PIC X(05)                
005886             VALUE "MISMO".                                       
005888         10  FILLER                      PIC X(05)                
005890             VALUE "MONMT".                                       
005892         10  FILLER                      PIC X(05)                
005894             VALUE "NEBNE".                                       
005896         10  FILLER                      PIC X(05)                
005898             VALUE "NEVNV".                                       
005900         10  FILLER                      PIC X(05)                
005902             VALUE "NHANH".                                       
005904         10  FILLER                      PIC X(05)                
005906             VALUE "NJENJ".                                       
005908         10  FILLER                      PIC X(05)                
005910             VALUE "NMENM".                                       
005912         10  FILLER                      PIC X(05)                
005914             VALUE "NYONY".                                       
005916         10  FILLER                      PIC X(05)                
005918             VALUE "NCANC".                                       
005920         10  FILLER                      PIC X(05)                
005922             VALUE "NDAND".                                       
005924         10  FILLER                      PIC X(05)                
005926             VALUE "OHIOH".                                       
005928         10  FILLER                      PIC X(05)                
005930             VALUE "OKLOK".                                       
005932         10  FILLER                      PIC X(05)                
005934             VALUE "OREOR".                                       
005936         10  FILLER                      PIC X(05)                
005938             VALUE "PENPA".                                       
005940         10  FILLER                      PIC X(05)                
005942             VALUE "RHORI".                                       
005944         10  FILLER                      PIC X(05)                
005946             VALUE "SCASC".                                       
005948         10  FILLER                      PIC X(05)                
005950             VALUE "SDASD".                                       
005952         10  FILLER                      PIC X(05)                
005954             VALUE "TENTN".                                       
005956         10  FILLER                      PIC X(05)                
005958             VALUE "TEXTX".                                       
005960         10  FILLER                      PIC X(05)                
005962             VALUE "UTAUT".                                       
005964         10  FILLER                      PIC X(05)                
005966             VALUE "VERVT".                                       
005968         10  FILLER                      PIC X(05)                
005970             VALUE "VIRVA".                                       
005972         10  FILLER                      PIC X(05)                
005974             VALUE "WASWA".                                       
005976         10  FILLER                      PIC X(05)                
005978             VALUE "WVIWV".                                       
005980         10  FILLER                      PIC X(05)                
005982             VALUE "WISWI".                                       
005984         10  FILLER                      PIC X(05)                
005986             VALUE "WYOWY".                                       
005988     02  STATE-ABBRE-TABLE-R REDEFINES ST-ABBRE-TABLE.            
005990     05  ST-AND-ABBRE                    OCCURS 51 TIMES          
005992                                             INDEXED BY ST-SUB.   
005994         10  WS-STATE                    PIC X(03).               
005996         10  WS-ST-ABBRE                 PIC X(02).               
005998     02  FULL-ST-ABBRE-TABLE.                                     
006000     05  FULL-ST-LINE.                                            
006002         10  FILLER                      PIC X(07)                
006004             VALUE "ALABAAL".                                     
006006         10  FILLER                      PIC X(07)                
006008             VALUE "ALASKAK".                                     
006010         10  FILLER                      PIC X(07)                
006012             VALUE "MISSIMS".                                     
006014         10  FILLER                      PIC X(07)                
006016             VALUE "MISSOMO".                                     
006018     02  FULL-ST-ABBRE-TABLE-R REDEFINES FULL-ST-ABBRE-TABLE.     
006020     05  FULL-ST-AND-ABBRE               OCCURS 4 TIMES           
006022                                           INDEXED BY FULL-ST-SUB.
006024         10  WS-FULL-STATE               PIC X(05).               
006026         10  WS-FULL-ST-ABBRE            PIC X(02).               
006028 01  WS-SUB-ADDR                         PIC 9(01) VALUE 0.       
006030 01  AD-ADDRESS                          PIC X(40).               
006032 01  AD-WORK-TABLE.                                               
006034     05  AD-ADDR-TABLE OCCURS 10 TIMES.                           
006036         10  AD-TABLE-1ST-TEN.                                    
006038             15  AD-TABLE-1ST-NINE.                               
006040                 20  AD-TABLE-1ST-FIVE.                           
006042                     25  AD-TABLE-1ST-CHAR   PIC X(01).           
006044                     25  AD-TABLE-2ND-CHAR   PIC X(01).           
006046                     25  FILLER              PIC X(03).           
006048                 20  FILLER                  PIC X(04).           
006050             15  FILLER                      PIC X(01).           
006052         10  AD-TABLE-1ST-TEN-R REDEFINES AD-TABLE-1ST-TEN.       
006054             15  FILLER                      PIC X(06).           
006056             15  AD-TABLE-LST-FOUR           PIC X(04).           
006058         10  AD-TABLE-LST-30             PIC X(30).               
006060 01  AD-FINISHED-ADDRESS.                                         
006062     05  AD-CITY                         PIC X(40).               
006064     05  FILLER                          PIC X(02).               
006066     05  AD-STATE.                                                
006068         10  AD-STATE-1ST-5.                                      
006070             15  AD-STATE-1ST-4.                                  
006072                 20  AD-STATE-1ST-3      PIC X(03).               
006074                 20  FILLER              PIC X(01).               
006076             15  FILLER                  PIC X(01).               
006078         10  FILLER                      PIC X(05).               
006080     05  FILLER                          PIC X(02).               
006082     05  AD-ZIP-CODE.                                             
006084         10  AD-ZIP-CODE1X5              PIC X(05).               
006086         10  AD-ZIP-CODE-LST4            PIC X(04).               
006088 01  AD-TEMP-CITY-TABLE.                                          
006090     05  AD-TEMP-TABLE                  PIC X(40) OCCURS 4 TIMES. 
006092 01  AD-ALPHA-WORK-FIELDS.                                        
006094     05  AD-ERROR-MESSAGE                PIC X(20).               
006096     05  AD-ZIP-ERROR-MESSG              PIC X(20).               
006098 01  AD-NUMERIC-WORK-FIELDS.                                      
006100     05  AD-NO-LINES                     PIC 9(01).               
006102     05  AD-SUB-1                        PIC 9(02).               
006104     05  WS-STORE-AD-SUB                 PIC 9(02).               
006106     05  WS-ST-SUB                       PIC 9(02).               
006108     05  AD-SUB-A                        PIC 9(02).               
006110     05  AD-SUB-MAX                      PIC 9(02).               
006112     05  AD-ERROR-FLAG                   PIC 9(01).               
006114     05  AD-NO-ALPHA-ENTRIES             PIC 9(02).               
006116     05  AD-NO-NUMERIC-ENTRIES           PIC 9(02).               
006118     05  AD-ZIPCD-ERROR-FLAG             PIC 9(01).               
006120     05  AD-NO-FIELDS                    PIC 9(02).               
006122     05  AD-WORK-FLAG                    PIC 9(02).               
006124     05  AD-SUB-N                        PIC 9(02).               
006126     05  AD-GOOD-ZIP-SW                  PIC 9(01).               
006128     05  AD-SUB-UNSTR                    PIC 9(02).               
006130     05  AD-SUB-P                        PIC 9(02).               
006132     05  ZIP-SUB                         PIC 9(02).               
006134 01  AD-STREET-ADDRESS-1                 PIC X(40).               
006136 01  AD-STREET-ADDRESS                   PIC X(40).               
006138 01  AD-NUMERIC-STREET-WK-FIELDS.                                 
006140     05  AD-STREET-ERROR-FLAG            PIC 9(01).               
006142     05  AD-SUB-ST                       PIC 9(02).               
006144     05  AD-SUB-ST-1                     PIC 9(02).               
006146     05  AD-CITY-SUB-HOLD                PIC 9(02).               
006148     05  AD-WARN-FLAG                    PIC 9(01).               
006150 01  AD-ALPHA-STREET-WK-FIELDS.                                   
006152     05  AD-STREET-ERROR-MESSAGE         PIC X(18).               
006154     05  AD-WARN-MESSG                   PIC X(18).               
006156 01  AD-STATE-ABBRE                      PIC X(02).               
006158 01  WS-STORE-STATE.                                              
006160     05  WS-STATE-FIRST-2                PIC X(02).               
006162     05  WS-STATE-FILLER                 PIC X(08).               
006164 01  ABBRE-FLAG                          PIC 9(01) VALUE 0.       
006166                                                                  
006168 01  WS-REDEFINE-AREA-4.                                          
006170     02  WS-BUILD-NAME-INPUT-AREA.                                
006172     05  WS-BNI-KEY                   PIC X(14).                  
006174     05  WS-BNI-FIRST                 PIC X(40).                  
006176     05  WS-BNI-MID                   PIC X(20).                  
006178     05  WS-BNI-LAST                  PIC X(40).                  
006180     05  WS-BNI-PREFIX                PIC X(12).                  
006182     05  WS-BNI-SUFFIX                PIC X(12).                  
006184     05  WS-BNI-FAMILIAR              PIC X(20).                  
006186     05  WS-BNI-PRINT-PREFIX-FLAG     PIC X(01).                  
006188     05  WS-BNI-PRINT-SUFFIX-FLAG     PIC X(01).                  
006190     05  WS-BNI-DESIGNATION           PIC X(20).                  
006192     02  WS-BUILD-NAME-TRIM-VALUES       PIC X(18) VALUE          
006194         "401240201220HDTTDD".                                    
006196     02  WS-BUILD-NAME-TRIM REDEFINES WS-BUILD-NAME-TRIM-VALUES.  
006198     05  WS-BNA-MAXLEN OCCURS 6 TIMES PIC 9(02).                  
006200     05  WS-BNA-TRIM   OCCURS 6 TIMES PIC X(01).                  
006202     02  WS-BUILD-NAME-POINTER-VALUES    PIC X(28) VALUE          
006204         "6123456623415621644443134555".                          
006206     02  WS-BUILD-NAME-POINTER REDEFINES                          
006208                                   WS-BUILD-NAME-POINTER-VALUES.  
006210     05  WS-BNA-POINTER-SET           OCCURS 4 TIMES.             
006212         10  WS-BNA-MAXITEMS          PIC 9(01).                  
006214         10  WS-BNA-POINTER           OCCURS 6 TIMES              
006216                                      PIC 9(01).                  
006218     02  WS-BUILD-NAME-ARRAY-NUM.                                 
006220     05  WS-BNA-ACTLEN OCCURS 6 TIMES PIC  9(02) COMP.            
006222     05  WS-BNW-REMAIN                PIC S9(03) COMP.            
006224     05  WS-BNS-ORDR                  PIC  9(02) COMP.            
006226     05  WS-BNS-PASS                  PIC  9(02) COMP.            
006228     05  WS-BNS-VALU                  PIC  9(02) COMP.            
006230     05  WS-BNS-CHRI                  PIC  9(02) COMP.            
006232     05  WS-BNS-CHRO                  PIC  9(02) COMP.            
006234     02  WS-BUILD-NAME-ARRAY-ALPHA.                               
006236     05  WS-BNA-VALUE                 OCCURS  6 TIMES.            
006238         10  WS-BNA-CHAR              OCCURS 40 TIMES             
006240                                      PIC X(01).                  
006242     02  WS-BUILD-NAME-ARRAY-OUTPUT.                              
006244     05  WS-BNO-OUTPUT.                                           
006246         10  WS-BNO-NAME              OCCURS 4 TIMES.             
006248             15  WS-BNO-CHAR          OCCURS 40 TIMES             
006250                                      PIC X(01).                  
006252     05  WS-BNO-OUTPUT-AREA REDEFINES WS-BNO-OUTPUT.              
006254         10  WS-BNO-NAME-LNF          PIC X(40).                  
006256         10  WS-BNO-NAME-FNF          PIC X(40).                  
006258         10  WS-BNO-NAME-BUSINESS     PIC X(40).                  
006260         10  WS-BNO-RPT-NAME          PIC X(40).                  
006262     02  WS-BNO-MAXLEN                   PIC 9(02) COMP VALUE 40. 
006264                                                                  
006266 01  SPEC-CARD-14.                                                
006268     05  FILLER                       PIC X(07).                  
006270     05  SPEC-SEGMINT                 PIC X(01).                  
006272     05  SPEC-SHELTERED-HRBR          PIC X(01).                  
006274     05  SPEC-VOICE-RESPONSE-PHONE-NO PIC 9(10).                  
006276     05  SPEC-BANK-URL.                                           
006278         10  SPEC-BANK-URL-1          PIC X(30).                  
006280         10  SPEC-BANK-URL-2          PIC X(20).                  
006282     05  SPEC-LNS-ALT-FMT-DLQ-NTC-PHONE PIC 9(10).                
006284     05  SPEC-CSIWIRE-BILLING         PIC X(01).                  
006286     05  FILLER                       PIC X(01).                  
006288     05  FILLER-UNAVAIL-14            PIC X(01).                  
006290 01  SPEC-CARD-15.                                                
006292     05  FILLER                       PIC X(07).                  
006294     05  FILLER                       PIC X(74).                  
006296     05  FILLER-UNAVAIL-15            PIC X(01).                  
006298 01  SPEC-CARD-16.                                                
006300     05  FILLER                       PIC X(07).                  
006302     05  FILLER                       PIC X(74).                  
006304     05  FILLER-UNAVAIL-16            PIC X(01).                  
006306*L                                                                
006308                                                                  
006310*=================================================================
006312*                      DMS ROUTINE WORKING STORAGE                
006314*=================================================================
006316 01  WS-DMS-NAMES.                                                
006318     05  DMS-SUB                 PIC 9(02).                       
006320     05  WS-DMS-BKNO             PIC 9(03).                       
006322     05  WS-APPL-CODE            PIC 9(02).                       
006324     05  WS-RUN-DTE-ENT          PIC 9(06).                       
006326     05  WS-RUN-DTE-ENT-R REDEFINES WS-RUN-DTE-ENT.               
006328         10  WS-RUND-MM           PIC 9(02).                      
006330         10  WS-RUND-DD           PIC 9(02).                      
006332         10  WS-RUND-YY           PIC 9(02).                      
006334     05  WS-DATE-RUN.                                             
006336         10  WS-DMS-CC            PIC 9(02).                      
006338         10  WS-DMS-YY            PIC 9(02).                      
006340         10  WS-DMS-MM            PIC 9(02).                      
006342         10  WS-DMS-DD            PIC 9(02).                      
006344     05  WS-DATE-RUN-R REDEFINES WS-DATE-RUN                      
006346                                 PIC 9(08).                       
006348     05  WS-VER-SAVE             PIC 9(02).                       
006350     05  WS-DATE-SAVE            PIC 9(08).                       
006352     05  WS-DATE-SAVE-R REDEFINES WS-DATE-SAVE.                   
006354       10  WS-DATE-SAVE-CC       PIC 9(02).                       
006356       10  WS-DATE-SAVE-YY       PIC 9(02).                       
006358       10  WS-DATE-SAVE-MM       PIC 9(02).                       
006360       10  WS-DATE-SAVE-DD       PIC 9(02).                       
006362     05  WS-SAVE-DATE-MMDDYY.                                     
006364       10  WS-SAVE-MM            PIC 9(02).                       
006366       10  WS-SAVE-DD            PIC 9(02).                       
006368       10  WS-SAVE-YY            PIC 9(02).                       
006370     05  WS-DMS-ERROR            PIC 9(01).                       
006372         88  DMS-AOK                 VALUE 0.                     
006374         88  DMS-NEXT-ERROR          VALUE 2.                     
006376         88  DMS-FIND-ERROR          VALUE 3.                     
006378         88  DMS-CLOSE-ERROR         VALUE 4.                     
006380         88  DMS-OPEN-ERROR          VALUE 5.                     
006382 01 WS-DMS-DATA-TABLE.                                            
006384     05  WS-DMS-RECORD   OCCURS 25 TIMES.                         
006386         10  WS-DMS-CARDS   OCCURS 25 TIMES                       
006388                             PIC X(74).                           
006390*                                                                 
006392 01  RMD-LEF-TABLE-1-X.                                           
006394   05  RMD-LEF-TABLE-1.                                           
006396     10 FILLER PIC X(54) VALUE                                    
006398         "824816806797787777767758748738728718708699689679669660".
006400     10 FILLER PIC X(54) VALUE                                    
006402         "650640630621611601591582572562553543533524514504494485".
006404     10 FILLER PIC X(54) VALUE                                    
006406         "475465456446436427417407398388379370360351342333323314".
006408     10 FILLER PIC X(54) VALUE                                    
006410         "305296287279270261252244235227218210202194186178170163".
006412     10 FILLER PIC X(54) VALUE                                    
006414         "155148141134127121114108102097091086081076071067063059".
006416     10 FILLER PIC X(54) VALUE                                    
006418         "055052049046043041038036034031029027025023021019017015".
006420     10 FILLER PIC X(12) VALUE                                    
006422         "014012011010".                                          
006424                                                                  
006426   05  WS-RMD-LEF-TABLE-1 REDEFINES RMD-LEF-TABLE-1.              
006428       10  WS-RMD-TBL1-LEF           PIC 999 OCCURS 112 TIMES.    
006430                                                                  
```

⚠️  This is the source code you must document.
    442 lines from 2770 to 3211.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

