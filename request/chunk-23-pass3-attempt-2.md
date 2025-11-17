# LLM Request Debug File
Generated: 2025-11-14T18:37:50.318585

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 23/55
- **Model**: gpt-4.1
- **Chunk Number**: 23
- **Pass Number**: 3
- **Attempt Number**: 2 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~6,315 tokens
- **Total Input**: ~8,273 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 23/55" (ID: detailed-code-explanation)

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


**CHUNK 23 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-14T17:36:35.036798", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 23 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 10849 to 11086 (238 lines)\nChunk Tokens (estimated): ~5,064\nActual Input Tokens: 6,470 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 10849-11086 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 23 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 23 of 55.\n\n\n=============================================================================\nCHUNK 23 SOURCE CODE (Lines 10849-11086)\n=============================================================================\n\n```cobol\n021706             TDB-TDARPT-REMARKS.                                  \n021708             15  TDB-TDARPT-RMK-1          PIC X(01).             \n021710             15  TDB-TDARPT-RMK-FM-CD      PIC 9(04).             \n021712             15  TDB-TDARPT-RMK-FM-SRC     PIC X(08).             \n021714             15  TDB-TDARPT-RMK-FM-DDA     PIC 9(12).             \n021716             15  TDB-TDARPT-RMK-FM-DDA-SUB PIC 9(03).             \n021718             15  FILLER                    PIC X(72).             \n021720         10  TDB-TDARPT-SEQ-NBR-X.                                \n021722             15  TDB-TDARPT-SEQ-NBR        PIC 9(4).              \n021724         10  TDB-TDARPT-ADD-DT-X.                                 \n021726             15  TDB-TDARPT-ADD-DT         PIC 9(8).              \n021728         10  TDB-TDARPT-ADD-TM-X.                                 \n021730             15  TDB-TDARPT-ADD-TM         PIC 9(8).              \n021732         10  TDB-TDARPT-ACTV-DESC          PIC X(80).             \n021734         10  TDB-TDARPT-ACTV-SEQ-NBR-X.                           \n021736             15  TDB-TDARPT-ACTV-SEQ-NBR   PIC 9(16).             \n021738         10  TDB-TDARPT-ACTV-CHK-NBR-X.                           \n021740             15  TDB-TDARPT-ACTV-CHK-NBR   PIC 9(10).             \n021742         10  TDB-TDARPT-ACTV-SOURCE        PIC X(01).             \n021744         10  TDB-TDARPT-ACTV-AMT-X.                               \n021746             15  TDB-TDARPT-ACTV-AMT       PIC S9(12)V99.         \n021748                                                                  \n021750         10  TDB-TDARPT-NONDB-FIELDS.                             \n021752             15  TDB-TDARPT-NEW-PRT-DT     PIC 9(08).             \n021754                                                                  \n021756     05  TDB-TDATOTAL.                                            \n021758         10  TDB-TDATT-BANK-X.                                    \n021760             15  TDB-TDATT-BANK           PIC 9(4).               \n021762         10  TDB-TDATT-REGION-X.                                  \n021764             15  TDB-TDATT-REGION         PIC 9(2).               \n021766         10  TDB-TDATT-TOTAL-CD-X.                                \n021768             15  TDB-TDATT-TOTAL-CD       PIC 999.                \n021770         10  TDB-TDATT-APPL-X.                                    \n021772             15  TDB-TDATT-APPL           PIC 9.                  \n021774         10  TDB-TDATT-VOID-DATE-X.                               \n021776             15  TDB-TDATT-VOID-DATE      PIC 9(8).               \n021778         10  TDB-TDATT-ADD-DATE-X.                                \n021780             15  TDB-TDATT-ADD-DATE       PIC 9(8).               \n021782         10  TDB-TDATT-ADD-TIME-X.                                \n021784             15  TDB-TDATT-ADD-TIME       PIC 9(8).               \n021786         10  TDB-TDATT-PUB-ID             PIC X(8).               \n021788         10  TDB-TDATT-VOID-PUB-ID        PIC X(8).               \n021790         10  TDB-TDATT-DESC               PIC X(30).              \n021792         10  TDB-TDATT-RENEW-CD-X.                                \n021794             15  TDB-TDATT-RENEW-CD       PIC 9(1).               \n021796         10  TDB-TDATT-OVERRIDE-X.                                \n021798             15  TDB-TDATT-OVERRIDE       PIC 9(1).               \n021800         10  TDB-TDATT-REN-NTC-X.                                 \n021802             15  TDB-TDATT-REN-NTC        PIC 9(1).               \n021804         10  TDB-TDATT-PMAT-NTC-X.                                \n021806             15  TDB-TDATT-PMAT-NTC       PIC 9(1).               \n021808         10  TDB-TDATT-RTCHG-NTC-X.                               \n021810             15  TDB-TDATT-RTCHG-NTC      PIC 9(1).               \n021812         10  TDB-TDATT-INT-NTC-X.                                 \n021814             15  TDB-TDATT-INT-NTC        PIC 9(1).               \n021816         10  TDB-TDATT-YIELD-NUM-X.                               \n021818             15  TDB-TDATT-YIELD-NUM      PIC 9(3).               \n021820         10  TDB-TDATT-YIELD-DENOM-X.                             \n021822             15  TDB-TDATT-YIELD-DENOM    PIC 9(3).               \n021824         10  TDB-TDATT-CMPD-FREQ-X.                               \n021826             15  TDB-TDATT-CMPD-FREQ      PIC 9(1).               \n021828         10  TDB-TDATT-CMPD-NTRVL-X.                              \n021830             15  TDB-TDATT-CMPD-NTRVL     PIC 9(4).               \n021832         10  TDB-TDATT-RTCHG-LIMIT-X.                             \n021834             15  TDB-TDATT-RTCHG-LIMIT    PIC 9(1).               \n021836         10  TDB-TDATT-CHG-NTRVL-X.                               \n021838             15  TDB-TDATT-CHG-NTRVL      PIC 9(3).               \n021840         10  TDB-TDATT-PENALTY-CD-X.                              \n021842             15  TDB-TDATT-PENALTY-CD     PIC 999.                \n021844         10  TDB-TDATT-MAT-TYPE-X.                                \n021846             15  TDB-TDATT-MAT-TYPE       PIC 9(1).               \n021848         10  TDB-TDATT-MAT-TERM-X.                                \n021850             15  TDB-TDATT-MAT-TERM       PIC 9(4).               \n021852         10  TDB-TDATT-PAY-FREQ-X.                                \n021854             15  TDB-TDATT-PAY-FREQ       PIC 9(1).               \n021856         10  TDB-TDATT-PAY-NTRVL-X.                               \n021858             15  TDB-TDATT-PAY-NTRVL      PIC 9(4).               \n021860         10  TDB-TDATT-STMT-FREQ-X.                               \n021862             15  TDB-TDATT-STMT-FREQ      PIC 9(1).               \n021864         10  TDB-TDATT-STMT-NTRVL-X.                              \n021866             15  TDB-TDATT-STMT-NTRVL     PIC 9(4).               \n021868         10  TDB-TDATT-VAR-IMMED-X.                               \n021870             15  TDB-TDATT-VAR-IMMED      PIC 9(1).               \n021872         10  TDB-TDATT-VAR-INT-X.                                 \n021874             15  TDB-TDATT-VAR-INT        PIC 9(1).               \n021876         10  TDB-TDATT-VAR-STEP-X.                                \n021878             15  TDB-TDATT-VAR-STEP       PIC 9(1).               \n021880         10  TDB-TDATT-VAR-SCHED-X.                               \n021882             15  TDB-TDATT-VAR-SCHED      PIC 9(1).               \n021884         10  TDB-TDATT-VAR-BAL-X.                                 \n021886             15  TDB-TDATT-VAR-BAL        PIC 9(1).               \n021888         10  TDB-TDATT-VAR-CUST-X.                                \n021890             15  TDB-TDATT-VAR-CUST       PIC 9(1).               \n021892         10  TDB-TDATT-RT-CHG-ALOW-X.                             \n021894             15  TDB-TDATT-RT-CHG-ALOW    PIC 9(1).               \n021896         10  TDB-TDATT-WTHDRW-ALOW-X.                             \n021898             15  TDB-TDATT-WTHDRW-ALOW    PIC 9(1).               \n021900         10  TDB-TDATT-DPOSIT-ALOW-X.                             \n021902             15  TDB-TDATT-DPOSIT-ALOW    PIC 9(1).               \n021904         10  TDB-TDATT-ODD-PAYMENT-X.                             \n021906             15  TDB-TDATT-ODD-PAYMENT    PIC 9(1).               \n021908         10  TDB-TDATT-IGL-GRP-X.                                 \n021910             15  TDB-TDATT-IGL-GRP        PIC 9(2).               \n021912         10  TDB-TDATT-POST-MAT-X.                                \n021914             15  TDB-TDATT-POST-MAT       PIC 9(1).               \n021916         10  TDB-TDATT-END-OF-MAT-X.                              \n021918             15  TDB-TDATT-END-OF-MAT     PIC 9(1).               \n021920         10  TDB-TDATT-END-OF-INT-X.                              \n021922             15  TDB-TDATT-END-OF-INT     PIC 9(1).               \n021924         10  TDB-TDATT-END-OF-STMT-X.                             \n021926             15  TDB-TDATT-END-OF-STMT    PIC 9(1).               \n021928         10  TDB-TDATT-END-OF-CMPD-X.                             \n021930             15  TDB-TDATT-END-OF-CMPD    PIC 9(1).               \n021932         10  TDB-TDATT-FLOOR-RT-X.                                \n021934             15  TDB-TDATT-FLOOR-RT       PIC 99V999.             \n021936         10  TDB-TDATT-FLOOR-INCR-X.                              \n021938             15  TDB-TDATT-FLOOR-INCR     PIC 99V999.             \n021940         10  TDB-TDATT-CHG-NTC-X.                                 \n021942             15  TDB-TDATT-CHG-NTC        PIC 9(1).               \n021944         10  TDB-TDATT-IRA-BACKED-X.                              \n021946             15  TDB-TDATT-IRA-BACKED     PIC 9(1).               \n021948         10  TDB-TDATT-SAV-DEPOSIT        PIC 9(1).               \n021950         10  TDB-TDATT-LEVEL-PAY-X.                               \n021952             15  TDB-TDATT-LEVEL-PAY      PIC 9.                  \n021954         10  TDB-TDATT-CAP-RT-CHG         PIC X.                  \n021956         10  TDB-TDATT-FEE-FREQ-X.                                \n021958             15  TDB-TDATT-FEE-FREQ       PIC 9.                  \n021960         10  TDB-TDATT-FEE-NTRVL-X.                               \n021962             15  TDB-TDATT-FEE-NTRVL      PIC 9(4).               \n021964         10  TDB-TDATT-FEE-AMT-X.                                 \n021966             15  TDB-TDATT-FEE-AMT        PIC S9(12)V99.          \n021968         10  TDB-TDATT-END-OF-FEE-X.                              \n021970             15  TDB-TDATT-END-OF-FEE     PIC 9.                  \n021972         10  TDB-TDATT-ZERO-RT-ALLOW-X.                           \n021974             15  TDB-TDATT-ZERO-RT-ALLOW  PIC 9.                  \n021976         10  TDB-TDATT-RC-MAT-ONLY        PIC 9(1).               \n021978         10  TDB-TDATT-CLS-ON-MAT         PIC 9(1).               \n021980         10  TDB-TDATT-GRACE-DAYS         PIC 9(2).               \n021982         10  TDB-TDATT-IGL-GRP-2          PIC 9(2).               \n021984                                                                  \n021986                                                                  \n021988     05  TDB-TDAPENALTY.                                          \n021990         10  TDB-TDAP-BANK-X.                                     \n021992             15  TDB-TDAP-BANK            PIC 9(4).               \n021994         10  TDB-TDAP-ROUTINE             PIC 999.                \n021996         10  TDB-TDAP-STEP-NBR-X.                                 \n021998             15  TDB-TDAP-STEP-NBR        PIC 9(2).               \n022000         10  TDB-TDAP-FUNC                PIC X(1).               \n022002         10  TDB-TDAP-ADD-DATE-X.                                 \n022004             15  TDB-TDAP-ADD-DATE        PIC 9(8).               \n022006         10  TDB-TDAP-ADD-TIME-X.                                 \n022008             15  TDB-TDAP-ADD-TIME        PIC 9(8).               \n022010         10  TDB-TDAP-PUB-ID              PIC X(8).               \n022012         10  TDB-TDAP-VOID-PUB-ID         PIC X(8).               \n022014         10  TDB-TDAP-VOID-DATE-X.                                \n022016             15  TDB-TDAP-VOID-DATE       PIC 9(8).               \n022018         10  TDB-TDAP-DATE-X.                                     \n022020             15  TDB-TDAP-DATE            PIC 9(8).               \n022022         10  TDB-TDAP-DAYS-X.                                     \n022024             15  TDB-TDAP-DAYS            PIC 9(4).               \n022026         10  TDB-TDAP-MONTHS-X.                                   \n022028             15  TDB-TDAP-MONTHS          PIC 9(4).               \n022030         10  TDB-TDAP-PERCENT-X.                                  \n022032             15  TDB-TDAP-PERCENT         PIC 9(2)V9(2).          \n022034         10  TDB-TDAP-AMOUNT-X.                                   \n022036             15  TDB-TDAP-AMOUNT          PIC S9(12)V9(2).        \n022038         10  TDB-TDAP-USE-INT-X.                                  \n022040             15  TDB-TDAP-USE-INT         PIC 9(1).               \n022042         10  TDB-TDAP-USE-RED-X.                                  \n022044             15  TDB-TDAP-USE-RED         PIC 9(1).               \n022046         10  TDB-TDAP-USE-MONTH-X.                                \n022048             15  TDB-TDAP-USE-MONTH       PIC 9(1).               \n022050         10  TDB-TDAP-USE-DAY-X.                                  \n022052             15  TDB-TDAP-USE-DAY         PIC 9(1).               \n022054         10  TDB-TDAP-USE-AVL-INT-X.                              \n022056             15  TDB-TDAP-USE-AVL-INT     PIC 9(1).               \n022058                                                                  \n022060     05  TDB-TDAPCR.                                              \n022062         10  TDB-TDAPC-APPL               PIC X(03).              \n022064         10  TDB-TDAPC-TYPE-X.                                    \n022066             15  TDB-TDAPC-TYPE           PIC 9(1).               \n022068         10  TDB-TDAPC-BANK-X.                                    \n022070             15  TDB-TDAPC-BANK           PIC 9(04).              \n022072         10  TDB-TDAPC-RPT-NBR-X.                                 \n022074             15  TDB-TDAPC-RPT-NBR        PIC 9(04).              \n022076         10  TDB-TDAPC-CSI-ONLY           PIC X(1).               \n022078         10  TDB-TDAPC-RPT-DESC           PIC X(40).              \n022080         10  TDB-TDAPC-SPECS              PIC X(65).              \n022082         10  TDB-TDAPC-COPIES             PIC 9(02).              \n022084         10  TDB-TDAPC-LASER-PRT          PIC 9(02).              \n022086         10  TDB-TDAPC-FICHE-PRT          PIC 9(02).              \n022088         10  TDB-TDAPC-OPTICAL            PIC 9(02).              \n022090         10  TDB-TDAPC-PRT-DLY            PIC X(01).              \n022092         10  TDB-TDAPC-DLY-IND            PIC X(07).              \n022094         10  TDB-TDAPC-LST-PRT-D-X.                               \n022096             15  TDB-TDAPC-LST-PRT-D      PIC 9(08).              \n022098         10  TDB-TDAPC-PRT-WK             PIC X(01).              \n022100         10  TDB-TDAPC-WK-IND             PIC X(07).              \n022102         10  TDB-TDAPC-LST-PAY-W-X.                               \n022104             15  TDB-TDAPC-LST-PRT-W      PIC 9(08).              \n022106         10  TDB-TDAPC-PRT-MTH            PIC X(01).              \n022108         10  TDB-TDAPC-LST-DAY-M          PIC X(01).              \n022110         10  TDB-TDAPC-NXT-PRT-M-X.                               \n022112             15  TDB-TDAPC-NXT-PRT-M      PIC 9(08).              \n022114         10  TDB-TDAPC-LST-PRT-M-X.                               \n022116             15  TDB-TDAPC-LST-PRT-M      PIC 9(08).              \n022118         10  TDB-TDAPC-PRT-QTR            PIC X(01).              \n022120         10  TDB-TDAPC-LST-DAY-Q          PIC X(01).              \n022122         10  TDB-TDAPC-NXT-PRT-Q-X.                               \n022124             15  TDB-TDAPC-NXT-PRT-Q      PIC 9(08).              \n022126         10  TDB-TDAPC-LST-PRT-Q-X.                               \n022128             15  TDB-TDAPC-LST-PRT-Q      PIC 9(08).              \n022130         10  TDB-TDAPC-PRT-YR             PIC X(01).              \n022132         10  TDB-TDAPC-NXT-PRT-Y-X.                               \n022134             15  TDB-TDAPC-NXT-PRT-Y      PIC 9(08).              \n022136         10  TDB-TDAPC-LST-PRT-Y-X.                               \n022138             15  TDB-TDAPC-LST-PRT-Y      PIC 9(08).              \n022140         10  TDB-TDAPC-SPECL-REQ          PIC X(01).              \n022142         10  TDB-TDAPC-PRT-DAY-X.                                 \n022144             15  TDB-TDAPC-PRT-DAY        PIC 9(08).              \n022146         10  TDB-TDAPC-BEGIN-DATE-X.                              \n022148             15  TDB-TDAPC-BEGIN-DATE     PIC 9(06).              \n022150         10  TDB-TDAPC-END-DATE-X.                                \n022152             15  TDB-TDAPC-END-DATE       PIC 9(06).              \n022154         10  TDB-TDAPC-PRINTER            PIC X(17).              \n022156         10  TDB-TDAPC-SPECL-SPECS        PIC X(65).              \n022158         10  TDB-TDAPC-REQUESTOR          PIC X(08).              \n022160         10  TDB-TDAPC-LPROCESS-DT-X.                             \n022162             15  TDB-TDAPC-LPROCESS-DT    PIC 9(16).              \n022164         10  TDB-TDAPC-LUPD-DT-X.                                 \n022166             15  TDB-TDAPC-LUPD-DT        PIC 9(08).              \n022168         10  TDB-TDAPC-LUPD-TM-X.                                 \n022170             15  TDB-TDAPC-LUPD-TM        PIC 9(06).              \n022172         10  TDB-TDAPC-BP-LAST-RUN-X.                             \n022174             15  TDB-TDAPC-BP-LAST-RUN    PIC 9(16).              \n022176         10  TDB-TDAPC-PUB-ID             PIC X(08).              \n022178         10  TDB-TDAPC-BANK-SPECS         PIC X(300).             \n022180         10  TDB-TDAPC-BANK-SPECS-R REDEFINES                     \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    238 lines from 10849 to 11086.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 23, "total_chunks": 55, "start_line": 10849, "end_line": 11086, "line_count": 238}

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
- Source code length: 22334 characters

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
CHUNK 23 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 10849 to 11086 (238 lines)
Chunk Tokens (estimated): ~5,064
Actual Input Tokens: 6,470 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 10849-11086 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 23 of 55 chunks
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
      The source code below is only CHUNK 23 of 55.


=============================================================================
CHUNK 23 SOURCE CODE (Lines 10849-11086)
=============================================================================

```cobol
021706             TDB-TDARPT-REMARKS.                                  
021708             15  TDB-TDARPT-RMK-1          PIC X(01).             
021710             15  TDB-TDARPT-RMK-FM-CD      PIC 9(04).             
021712             15  TDB-TDARPT-RMK-FM-SRC     PIC X(08).             
021714             15  TDB-TDARPT-RMK-FM-DDA     PIC 9(12).             
021716             15  TDB-TDARPT-RMK-FM-DDA-SUB PIC 9(03).             
021718             15  FILLER                    PIC X(72).             
021720         10  TDB-TDARPT-SEQ-NBR-X.                                
021722             15  TDB-TDARPT-SEQ-NBR        PIC 9(4).              
021724         10  TDB-TDARPT-ADD-DT-X.                                 
021726             15  TDB-TDARPT-ADD-DT         PIC 9(8).              
021728         10  TDB-TDARPT-ADD-TM-X.                                 
021730             15  TDB-TDARPT-ADD-TM         PIC 9(8).              
021732         10  TDB-TDARPT-ACTV-DESC          PIC X(80).             
021734         10  TDB-TDARPT-ACTV-SEQ-NBR-X.                           
021736             15  TDB-TDARPT-ACTV-SEQ-NBR   PIC 9(16).             
021738         10  TDB-TDARPT-ACTV-CHK-NBR-X.                           
021740             15  TDB-TDARPT-ACTV-CHK-NBR   PIC 9(10).             
021742         10  TDB-TDARPT-ACTV-SOURCE        PIC X(01).             
021744         10  TDB-TDARPT-ACTV-AMT-X.                               
021746             15  TDB-TDARPT-ACTV-AMT       PIC S9(12)V99.         
021748                                                                  
021750         10  TDB-TDARPT-NONDB-FIELDS.                             
021752             15  TDB-TDARPT-NEW-PRT-DT     PIC 9(08).             
021754                                                                  
021756     05  TDB-TDATOTAL.                                            
021758         10  TDB-TDATT-BANK-X.                                    
021760             15  TDB-TDATT-BANK           PIC 9(4).               
021762         10  TDB-TDATT-REGION-X.                                  
021764             15  TDB-TDATT-REGION         PIC 9(2).               
021766         10  TDB-TDATT-TOTAL-CD-X.                                
021768             15  TDB-TDATT-TOTAL-CD       PIC 999.                
021770         10  TDB-TDATT-APPL-X.                                    
021772             15  TDB-TDATT-APPL           PIC 9.                  
021774         10  TDB-TDATT-VOID-DATE-X.                               
021776             15  TDB-TDATT-VOID-DATE      PIC 9(8).               
021778         10  TDB-TDATT-ADD-DATE-X.                                
021780             15  TDB-TDATT-ADD-DATE       PIC 9(8).               
021782         10  TDB-TDATT-ADD-TIME-X.                                
021784             15  TDB-TDATT-ADD-TIME       PIC 9(8).               
021786         10  TDB-TDATT-PUB-ID             PIC X(8).               
021788         10  TDB-TDATT-VOID-PUB-ID        PIC X(8).               
021790         10  TDB-TDATT-DESC               PIC X(30).              
021792         10  TDB-TDATT-RENEW-CD-X.                                
021794             15  TDB-TDATT-RENEW-CD       PIC 9(1).               
021796         10  TDB-TDATT-OVERRIDE-X.                                
021798             15  TDB-TDATT-OVERRIDE       PIC 9(1).               
021800         10  TDB-TDATT-REN-NTC-X.                                 
021802             15  TDB-TDATT-REN-NTC        PIC 9(1).               
021804         10  TDB-TDATT-PMAT-NTC-X.                                
021806             15  TDB-TDATT-PMAT-NTC       PIC 9(1).               
021808         10  TDB-TDATT-RTCHG-NTC-X.                               
021810             15  TDB-TDATT-RTCHG-NTC      PIC 9(1).               
021812         10  TDB-TDATT-INT-NTC-X.                                 
021814             15  TDB-TDATT-INT-NTC        PIC 9(1).               
021816         10  TDB-TDATT-YIELD-NUM-X.                               
021818             15  TDB-TDATT-YIELD-NUM      PIC 9(3).               
021820         10  TDB-TDATT-YIELD-DENOM-X.                             
021822             15  TDB-TDATT-YIELD-DENOM    PIC 9(3).               
021824         10  TDB-TDATT-CMPD-FREQ-X.                               
021826             15  TDB-TDATT-CMPD-FREQ      PIC 9(1).               
021828         10  TDB-TDATT-CMPD-NTRVL-X.                              
021830             15  TDB-TDATT-CMPD-NTRVL     PIC 9(4).               
021832         10  TDB-TDATT-RTCHG-LIMIT-X.                             
021834             15  TDB-TDATT-RTCHG-LIMIT    PIC 9(1).               
021836         10  TDB-TDATT-CHG-NTRVL-X.                               
021838             15  TDB-TDATT-CHG-NTRVL      PIC 9(3).               
021840         10  TDB-TDATT-PENALTY-CD-X.                              
021842             15  TDB-TDATT-PENALTY-CD     PIC 999.                
021844         10  TDB-TDATT-MAT-TYPE-X.                                
021846             15  TDB-TDATT-MAT-TYPE       PIC 9(1).               
021848         10  TDB-TDATT-MAT-TERM-X.                                
021850             15  TDB-TDATT-MAT-TERM       PIC 9(4).               
021852         10  TDB-TDATT-PAY-FREQ-X.                                
021854             15  TDB-TDATT-PAY-FREQ       PIC 9(1).               
021856         10  TDB-TDATT-PAY-NTRVL-X.                               
021858             15  TDB-TDATT-PAY-NTRVL      PIC 9(4).               
021860         10  TDB-TDATT-STMT-FREQ-X.                               
021862             15  TDB-TDATT-STMT-FREQ      PIC 9(1).               
021864         10  TDB-TDATT-STMT-NTRVL-X.                              
021866             15  TDB-TDATT-STMT-NTRVL     PIC 9(4).               
021868         10  TDB-TDATT-VAR-IMMED-X.                               
021870             15  TDB-TDATT-VAR-IMMED      PIC 9(1).               
021872         10  TDB-TDATT-VAR-INT-X.                                 
021874             15  TDB-TDATT-VAR-INT        PIC 9(1).               
021876         10  TDB-TDATT-VAR-STEP-X.                                
021878             15  TDB-TDATT-VAR-STEP       PIC 9(1).               
021880         10  TDB-TDATT-VAR-SCHED-X.                               
021882             15  TDB-TDATT-VAR-SCHED      PIC 9(1).               
021884         10  TDB-TDATT-VAR-BAL-X.                                 
021886             15  TDB-TDATT-VAR-BAL        PIC 9(1).               
021888         10  TDB-TDATT-VAR-CUST-X.                                
021890             15  TDB-TDATT-VAR-CUST       PIC 9(1).               
021892         10  TDB-TDATT-RT-CHG-ALOW-X.                             
021894             15  TDB-TDATT-RT-CHG-ALOW    PIC 9(1).               
021896         10  TDB-TDATT-WTHDRW-ALOW-X.                             
021898             15  TDB-TDATT-WTHDRW-ALOW    PIC 9(1).               
021900         10  TDB-TDATT-DPOSIT-ALOW-X.                             
021902             15  TDB-TDATT-DPOSIT-ALOW    PIC 9(1).               
021904         10  TDB-TDATT-ODD-PAYMENT-X.                             
021906             15  TDB-TDATT-ODD-PAYMENT    PIC 9(1).               
021908         10  TDB-TDATT-IGL-GRP-X.                                 
021910             15  TDB-TDATT-IGL-GRP        PIC 9(2).               
021912         10  TDB-TDATT-POST-MAT-X.                                
021914             15  TDB-TDATT-POST-MAT       PIC 9(1).               
021916         10  TDB-TDATT-END-OF-MAT-X.                              
021918             15  TDB-TDATT-END-OF-MAT     PIC 9(1).               
021920         10  TDB-TDATT-END-OF-INT-X.                              
021922             15  TDB-TDATT-END-OF-INT     PIC 9(1).               
021924         10  TDB-TDATT-END-OF-STMT-X.                             
021926             15  TDB-TDATT-END-OF-STMT    PIC 9(1).               
021928         10  TDB-TDATT-END-OF-CMPD-X.                             
021930             15  TDB-TDATT-END-OF-CMPD    PIC 9(1).               
021932         10  TDB-TDATT-FLOOR-RT-X.                                
021934             15  TDB-TDATT-FLOOR-RT       PIC 99V999.             
021936         10  TDB-TDATT-FLOOR-INCR-X.                              
021938             15  TDB-TDATT-FLOOR-INCR     PIC 99V999.             
021940         10  TDB-TDATT-CHG-NTC-X.                                 
021942             15  TDB-TDATT-CHG-NTC        PIC 9(1).               
021944         10  TDB-TDATT-IRA-BACKED-X.                              
021946             15  TDB-TDATT-IRA-BACKED     PIC 9(1).               
021948         10  TDB-TDATT-SAV-DEPOSIT        PIC 9(1).               
021950         10  TDB-TDATT-LEVEL-PAY-X.                               
021952             15  TDB-TDATT-LEVEL-PAY      PIC 9.                  
021954         10  TDB-TDATT-CAP-RT-CHG         PIC X.                  
021956         10  TDB-TDATT-FEE-FREQ-X.                                
021958             15  TDB-TDATT-FEE-FREQ       PIC 9.                  
021960         10  TDB-TDATT-FEE-NTRVL-X.                               
021962             15  TDB-TDATT-FEE-NTRVL      PIC 9(4).               
021964         10  TDB-TDATT-FEE-AMT-X.                                 
021966             15  TDB-TDATT-FEE-AMT        PIC S9(12)V99.          
021968         10  TDB-TDATT-END-OF-FEE-X.                              
021970             15  TDB-TDATT-END-OF-FEE     PIC 9.                  
021972         10  TDB-TDATT-ZERO-RT-ALLOW-X.                           
021974             15  TDB-TDATT-ZERO-RT-ALLOW  PIC 9.                  
021976         10  TDB-TDATT-RC-MAT-ONLY        PIC 9(1).               
021978         10  TDB-TDATT-CLS-ON-MAT         PIC 9(1).               
021980         10  TDB-TDATT-GRACE-DAYS         PIC 9(2).               
021982         10  TDB-TDATT-IGL-GRP-2          PIC 9(2).               
021984                                                                  
021986                                                                  
021988     05  TDB-TDAPENALTY.                                          
021990         10  TDB-TDAP-BANK-X.                                     
021992             15  TDB-TDAP-BANK            PIC 9(4).               
021994         10  TDB-TDAP-ROUTINE             PIC 999.                
021996         10  TDB-TDAP-STEP-NBR-X.                                 
021998             15  TDB-TDAP-STEP-NBR        PIC 9(2).               
022000         10  TDB-TDAP-FUNC                PIC X(1).               
022002         10  TDB-TDAP-ADD-DATE-X.                                 
022004             15  TDB-TDAP-ADD-DATE        PIC 9(8).               
022006         10  TDB-TDAP-ADD-TIME-X.                                 
022008             15  TDB-TDAP-ADD-TIME        PIC 9(8).               
022010         10  TDB-TDAP-PUB-ID              PIC X(8).               
022012         10  TDB-TDAP-VOID-PUB-ID         PIC X(8).               
022014         10  TDB-TDAP-VOID-DATE-X.                                
022016             15  TDB-TDAP-VOID-DATE       PIC 9(8).               
022018         10  TDB-TDAP-DATE-X.                                     
022020             15  TDB-TDAP-DATE            PIC 9(8).               
022022         10  TDB-TDAP-DAYS-X.                                     
022024             15  TDB-TDAP-DAYS            PIC 9(4).               
022026         10  TDB-TDAP-MONTHS-X.                                   
022028             15  TDB-TDAP-MONTHS          PIC 9(4).               
022030         10  TDB-TDAP-PERCENT-X.                                  
022032             15  TDB-TDAP-PERCENT         PIC 9(2)V9(2).          
022034         10  TDB-TDAP-AMOUNT-X.                                   
022036             15  TDB-TDAP-AMOUNT          PIC S9(12)V9(2).        
022038         10  TDB-TDAP-USE-INT-X.                                  
022040             15  TDB-TDAP-USE-INT         PIC 9(1).               
022042         10  TDB-TDAP-USE-RED-X.                                  
022044             15  TDB-TDAP-USE-RED         PIC 9(1).               
022046         10  TDB-TDAP-USE-MONTH-X.                                
022048             15  TDB-TDAP-USE-MONTH       PIC 9(1).               
022050         10  TDB-TDAP-USE-DAY-X.                                  
022052             15  TDB-TDAP-USE-DAY         PIC 9(1).               
022054         10  TDB-TDAP-USE-AVL-INT-X.                              
022056             15  TDB-TDAP-USE-AVL-INT     PIC 9(1).               
022058                                                                  
022060     05  TDB-TDAPCR.                                              
022062         10  TDB-TDAPC-APPL               PIC X(03).              
022064         10  TDB-TDAPC-TYPE-X.                                    
022066             15  TDB-TDAPC-TYPE           PIC 9(1).               
022068         10  TDB-TDAPC-BANK-X.                                    
022070             15  TDB-TDAPC-BANK           PIC 9(04).              
022072         10  TDB-TDAPC-RPT-NBR-X.                                 
022074             15  TDB-TDAPC-RPT-NBR        PIC 9(04).              
022076         10  TDB-TDAPC-CSI-ONLY           PIC X(1).               
022078         10  TDB-TDAPC-RPT-DESC           PIC X(40).              
022080         10  TDB-TDAPC-SPECS              PIC X(65).              
022082         10  TDB-TDAPC-COPIES             PIC 9(02).              
022084         10  TDB-TDAPC-LASER-PRT          PIC 9(02).              
022086         10  TDB-TDAPC-FICHE-PRT          PIC 9(02).              
022088         10  TDB-TDAPC-OPTICAL            PIC 9(02).              
022090         10  TDB-TDAPC-PRT-DLY            PIC X(01).              
022092         10  TDB-TDAPC-DLY-IND            PIC X(07).              
022094         10  TDB-TDAPC-LST-PRT-D-X.                               
022096             15  TDB-TDAPC-LST-PRT-D      PIC 9(08).              
022098         10  TDB-TDAPC-PRT-WK             PIC X(01).              
022100         10  TDB-TDAPC-WK-IND             PIC X(07).              
022102         10  TDB-TDAPC-LST-PAY-W-X.                               
022104             15  TDB-TDAPC-LST-PRT-W      PIC 9(08).              
022106         10  TDB-TDAPC-PRT-MTH            PIC X(01).              
022108         10  TDB-TDAPC-LST-DAY-M          PIC X(01).              
022110         10  TDB-TDAPC-NXT-PRT-M-X.                               
022112             15  TDB-TDAPC-NXT-PRT-M      PIC 9(08).              
022114         10  TDB-TDAPC-LST-PRT-M-X.                               
022116             15  TDB-TDAPC-LST-PRT-M      PIC 9(08).              
022118         10  TDB-TDAPC-PRT-QTR            PIC X(01).              
022120         10  TDB-TDAPC-LST-DAY-Q          PIC X(01).              
022122         10  TDB-TDAPC-NXT-PRT-Q-X.                               
022124             15  TDB-TDAPC-NXT-PRT-Q      PIC 9(08).              
022126         10  TDB-TDAPC-LST-PRT-Q-X.                               
022128             15  TDB-TDAPC-LST-PRT-Q      PIC 9(08).              
022130         10  TDB-TDAPC-PRT-YR             PIC X(01).              
022132         10  TDB-TDAPC-NXT-PRT-Y-X.                               
022134             15  TDB-TDAPC-NXT-PRT-Y      PIC 9(08).              
022136         10  TDB-TDAPC-LST-PRT-Y-X.                               
022138             15  TDB-TDAPC-LST-PRT-Y      PIC 9(08).              
022140         10  TDB-TDAPC-SPECL-REQ          PIC X(01).              
022142         10  TDB-TDAPC-PRT-DAY-X.                                 
022144             15  TDB-TDAPC-PRT-DAY        PIC 9(08).              
022146         10  TDB-TDAPC-BEGIN-DATE-X.                              
022148             15  TDB-TDAPC-BEGIN-DATE     PIC 9(06).              
022150         10  TDB-TDAPC-END-DATE-X.                                
022152             15  TDB-TDAPC-END-DATE       PIC 9(06).              
022154         10  TDB-TDAPC-PRINTER            PIC X(17).              
022156         10  TDB-TDAPC-SPECL-SPECS        PIC X(65).              
022158         10  TDB-TDAPC-REQUESTOR          PIC X(08).              
022160         10  TDB-TDAPC-LPROCESS-DT-X.                             
022162             15  TDB-TDAPC-LPROCESS-DT    PIC 9(16).              
022164         10  TDB-TDAPC-LUPD-DT-X.                                 
022166             15  TDB-TDAPC-LUPD-DT        PIC 9(08).              
022168         10  TDB-TDAPC-LUPD-TM-X.                                 
022170             15  TDB-TDAPC-LUPD-TM        PIC 9(06).              
022172         10  TDB-TDAPC-BP-LAST-RUN-X.                             
022174             15  TDB-TDAPC-BP-LAST-RUN    PIC 9(16).              
022176         10  TDB-TDAPC-PUB-ID             PIC X(08).              
022178         10  TDB-TDAPC-BANK-SPECS         PIC X(300).             
022180         10  TDB-TDAPC-BANK-SPECS-R REDEFINES                     
```

⚠️  This is the source code you must document.
    238 lines from 10849 to 11086.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

