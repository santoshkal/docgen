# LLM Request Debug File
Generated: 2025-11-17T22:18:41.506244

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 42/55
- **Model**: gpt-4.1
- **Chunk Number**: 42
- **Pass Number**: 3
- **Attempt Number**: 4 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~7,113 tokens
- **Total Input**: ~9,071 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 42/55" (ID: detailed-code-explanation)

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


**CHUNK 42 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-17T19:50:50.832678", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 42 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 20134 to 20666 (533 lines)\nChunk Tokens (estimated): ~7,836\nActual Input Tokens: 9,242 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 20134-20666 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 42 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 42 of 55.\n\n\n=============================================================================\nCHUNK 42 SOURCE CODE (Lines 20134-20666)\n=============================================================================\n\n```cobol\n040276 Z-5-86-1-ELSE.\n040278************ PERFORM WRITE-REPORT\n040280     PERFORM Z-23-PROCEDURE THRU Z-23-XIT.\n040282     IF  Z-EXIT-EDITEXIT\n040284         GO TO Z-5-XIT.\n040286     IF  Z-DMS2-ABORT-FLAG = 1\n040288         GO TO Z-5-XIT.\n040290     IF  Z-EXIT-LEVEL < 0\n040292         GO TO Z-5-82-END.\n040294*\n040296     IF ( SPECS-RMD-OVERRIDE = \"Y\" ) AND ( WS-NEW-DS-AMT > 0 )    \n040298         AND ( TDB-TDAD-RMD-OVERRIDE = 0 ) AND (                  \n040300         WS-IRA-DISTR-RECS = 1 )\n040302         NEXT SENTENCE ELSE\n040304         GO TO Z-5-127-1-ELSE.\n040306     IF WS-DSTFM-OPEN = 0\n040308         NEXT SENTENCE ELSE\n040310         GO TO Z-5-128-1-ELSE.\n040312     MOVE PROCESS-DATE-MMDD TO WS-DSTFM-DT.\n040314     IF WS-BANK-OPT = 1\n040316         NEXT SENTENCE ELSE\n040318         GO TO Z-5-130-1-ELSE.\n040320     MOVE WS-BANK-NO TO WS-DSTFM-BK.\n040322     MOVE SPACES TO WS-DSTFM-TIME.\n040324     GO TO Z-5-130-ENDIF.\n040326 Z-5-130-1-ELSE.\n040328     IF WS-BANK-OPT = 2\n040330         NEXT SENTENCE ELSE\n040332         GO TO Z-5-130-2-ELSE.\n040334     MOVE 000 TO WS-DSTFM-BK.\n040336*    RETRIEVE TODAY'S DATE\n040338     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n040340          USING Z-CALL-CURRENTDATE.\n040342     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n040344     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n040346     ACCEPT Z-DATE0-TIME   FROM TIME.\n040348     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.\n040350     MOVE Z-DATE0-UU TO Z-DATE4-UU.\n040352     MOVE Z-DATE4-FORMAT TO WS-DSTFM-TIME.\n040354     GO TO Z-5-130-ENDIF.\n040356 Z-5-130-2-ELSE.\n040358     IF WS-BANK-OPT = 3\n040360         NEXT SENTENCE ELSE\n040362         GO TO Z-5-130-3-ELSE.\n040364     MOVE 000 TO WS-DSTFM-BK.\n040366     MOVE SPACES TO WS-DSTFM-SUFF-R.\n040368     MOVE WS-SUFFIX-IN TO WS-DSTFM-SUFF.\n040370 Z-5-130-3-ELSE.\n040372 Z-5-130-ENDIF.\n040374*\n040376******* OPEN FILE DST-FILE-MAINT\n040378*\n040380     IF Z-FLINFO5-OPEN = 0\n040382         CHANGE ATTRIBUTE NEWFILE OF DST-FILE-MAINT TO VALUE TRUE\n040384         OPEN OUTPUT DST-FILE-MAINT \n040386         IF ATTRIBUTE FILESTATE OF DST-FILE-MAINT = VALUE OPENED\n040388             MOVE ZEROS TO Z-FILE5-KEY\n040390             MOVE ZEROS TO Z-FLINFO5-RS-KEY\n040392             MOVE 3 TO Z-FLINFO5-OPEN\n040394             MOVE 3 TO Z-FLINFO5-RS-OPEN\n040396         ELSE\n040398             DISPLAY \">>> FILE DST-FILE-MAINT FAILED TO OPEN\"\n040400             MOVE ATTRIBUTE TITLE OF DST-FILE-MAINT TO            \n040402                 Z-FL-EXCEPT-TITLE\n040404             DISPLAY \">>> OPEN FAIL, TITLE :\", Z-FL-EXCEPT-TITLE\n040406             DISPLAY \">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS\".\n040408     MOVE 1 TO WS-DSTFM-OPEN.\n040410 Z-5-128-1-ELSE.\n040412     IF ( SPECS-COMB-AUTO-RMD-ADJUST = \"Y\" ) AND (                \n040414         TDB-TDAA-INHERIT-IRA = 0 )\n040416         NEXT SENTENCE ELSE\n040418         GO TO Z-5-140-1-ELSE.\n040420     ADD 1 TO WS-TIN-RMD-INDEX .\n040422     IF WS-TIN-RMD-INDEX NOT > WS-TIN-RMD-MAX\n040424         NEXT SENTENCE ELSE\n040426         GO TO Z-5-142-1-ELSE.\n040428     MOVE TDB-TDAI-CUST TO WS-TIN-RMD-CUST (WS-TIN-RMD-INDEX).\n040430     MOVE TDB-TDAI-ACCT TO WS-TIN-RMD-ACCT (WS-TIN-RMD-INDEX).\n040432     MOVE TDB-TDAD-DS-NBR TO WS-TIN-RMD-DS-NBR (WS-TIN-RMD-INDEX).\n040434     MOVE TDB-TDAD-DS-FREQ TO WS-TIN-RMD-DS-FREQ                  \n040436         (WS-TIN-RMD-INDEX).\n040438     MOVE TDB-TDAD-DS-NTRVL TO WS-TIN-RMD-DS-NTRVL                \n040440         (WS-TIN-RMD-INDEX).\n040442     MOVE WS-NEW-DS-AMT TO WS-TIN-RMD-AMT (WS-TIN-RMD-INDEX).\n040444 Z-5-142-1-ELSE.\n040446     GO TO Z-5-140-ENDIF.\n040448 Z-5-140-1-ELSE.\n040450 Z-5-149-BEGIN.\n040452*      REQUESTED UPDATE OF FILE DST-FILE-MAINT\n040454     MOVE 3 TO Z-FLINFO5-UPDATE.\n040456     MOVE WS-BANK-NO TO FM-BANK.\n040458     MOVE TDB-TDAI-CUST TO FM-CUST.\n040460     MOVE TDB-TDAI-ACCT TO FM-ACCT.\n040462     MOVE 15 TO FM-STRUCT.\n040464     MOVE TDB-TDAD-DS-NBR TO FM-RECORD-NBR.\n040466     MOVE 0712 TO FM-TRANCODE.\n040468     MOVE WS-NEW-DS-AMT TO WS-FM-AMT.\n040470     MOVE WS-FM-AMT-X TO FM-CHANGE-DATA.\n040472     MOVE \"R\" TO FM-APPLY.\n040474     MOVE \"RMDRPT\" TO FM-ORIGIN.\n040476     MOVE SPACE TO FM-INT.\n040478     MOVE SPACE TO FM-SYSTEM-USE.\n040480     IF Z-EDIT-ERROR\n040482         GO TO Z-5-XIT.\n040484     IF Z-FLINFO5-UPDATE = 3\n040486         NEXT SENTENCE ELSE\n040488         GO TO Z-5-150-SKIP.\n040490     WRITE MASS-FM-RECORD\n040492         INVALID KEY\n040494         MOVE Z-FLINFO5-STATUS TO Z-FL-EXCEPT-STATUS\n040496         MOVE \"DST-FILE-MAINT\" TO Z-FL-EXCEPT-FILE\n040498         MOVE 1354 TO Z-FL-EXCEPT-SEQ\n040500         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.\n040502     MOVE Z-FILE5-KEY TO Z-FLINFO5-RS-KEY.\n040504     MOVE ZERO TO Z-FLINFO5-UPDATE.\n040506     MOVE ZERO TO Z-FLINFO5-LAST-SEQ.\n040508 Z-5-150-SKIP.\n040510 Z-5-149-SKIP.\n040512*\n040514 Z-5-149-XIT.\n040516     MOVE 0 TO Z-EXIT-CODE.\n040518     MOVE 9999 TO Z-EXIT-LEVEL.\n040520 Z-5-140-ENDIF.\n040522     IF TDB-TDAA-INHERIT-IRA > 0\n040524         NEXT SENTENCE ELSE\n040526         GO TO Z-5-163-1-ELSE.\n040528     ADD 1 TO RMD-TOT-CHGD-INHERIT .\n040530     GO TO Z-5-163-ENDIF.\n040532 Z-5-163-1-ELSE.\n040534     ADD 1 TO RMD-TOT-CHGD .\n040536 Z-5-163-ENDIF.\n040538     IF TDB-TDAD-AMT-CD = 1\n040540         NEXT SENTENCE ELSE\n040542         GO TO Z-5-166-1-ELSE.\n040544 Z-5-167-BEGIN.\n040546*      REQUESTED UPDATE OF FILE DST-FILE-MAINT\n040548     MOVE 4 TO Z-FLINFO5-UPDATE.\n040550     MOVE WS-BANK-NO TO FM-BANK.\n040552     MOVE TDB-TDAI-CUST TO FM-CUST.\n040554     MOVE TDB-TDAI-ACCT TO FM-ACCT.\n040556     MOVE 15 TO FM-STRUCT.\n040558     MOVE TDB-TDAD-DS-NBR TO FM-RECORD-NBR.\n040560     MOVE 0711 TO FM-TRANCODE.\n040562     MOVE 0 TO WS-FM-AMT-CD.\n040564     MOVE WS-FM-AMT-CD-X TO FM-CHANGE-DATA.\n040566     MOVE \"R\" TO FM-APPLY.\n040568     MOVE \"RMDRPT\" TO FM-ORIGIN.\n040570     MOVE SPACE TO FM-INT.\n040572     MOVE SPACE TO FM-SYSTEM-USE.\n040574     IF Z-EDIT-ERROR\n040576         GO TO Z-5-XIT.\n040578     IF Z-FLINFO5-UPDATE = 4\n040580         NEXT SENTENCE ELSE\n040582         GO TO Z-5-168-SKIP.\n040584     WRITE MASS-FM-RECORD\n040586         INVALID KEY\n040588         MOVE Z-FLINFO5-STATUS TO Z-FL-EXCEPT-STATUS\n040590         MOVE \"DST-FILE-MAINT\" TO Z-FL-EXCEPT-FILE\n040592         MOVE 1378 TO Z-FL-EXCEPT-SEQ\n040594         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.\n040596     MOVE Z-FILE5-KEY TO Z-FLINFO5-RS-KEY.\n040598     MOVE ZERO TO Z-FLINFO5-UPDATE.\n040600     MOVE ZERO TO Z-FLINFO5-LAST-SEQ.\n040602 Z-5-168-SKIP.\n040604 Z-5-167-SKIP.\n040606*\n040608 Z-5-167-XIT.\n040610     MOVE 0 TO Z-EXIT-CODE.\n040612     MOVE 9999 TO Z-EXIT-LEVEL.\n040614 Z-5-166-1-ELSE.\n040616 Z-5-127-1-ELSE.\n040618     MOVE ZEROS TO WS-NEW-DS-AMT.\n040620     MOVE SPACES TO MASS-FM-RECORD.\n040622 Z-5-82-END.\n040624     IF Z-EDIT-ERROR\n040626         GO TO Z-5-XIT.\n040628 Z-5-82-SKIP.\n040630     IF Z-EXIT-LEVEL < 3\n040632         GO TO Z-5-14-END.\n040634     IF Z-EXIT-CODE > 0\n040636         GO TO Z-5-82-XIT.\n040638     GO TO Z-5-82-LOOP.\n040640*\n040642 Z-5-82-XIT.\n040644     MOVE 0 TO Z-EXIT-CODE.\n040646     MOVE 9999 TO Z-EXIT-LEVEL.\n040648     IF WS-DSREC-FLAG = 0\n040650         NEXT SENTENCE ELSE\n040652         GO TO Z-5-183-1-ELSE.\n040654************ PERFORM TDD-MINDIST-SETUP-AND-CALC\n040656     PERFORM Z-28-PROCEDURE THRU Z-28-XIT.\n040658     IF  Z-EXIT-EDITEXIT\n040660         GO TO Z-5-XIT.\n040662     IF  Z-DMS2-ABORT-FLAG = 1\n040664         GO TO Z-5-XIT.\n040666     IF  Z-EXIT-LEVEL < 0\n040668         GO TO Z-5-14-END.\n040670*\n040672     IF ( TDB-TDAA-INHERIT-IRA = 2 ) AND ( TDB-TDAA-RMD-MAN-CALC  \n040674         = 0 )\n040676         NEXT SENTENCE ELSE\n040678         GO TO Z-5-185-1-ELSE.\n040680     IF ( TDB-TDAA-BNF-DEATH-DT > 20191231 ) OR ( (               \n040682         TDB-TDAA-IRA-TYPE = 13 OR 15 OR 17 ) AND (               \n040684         TDB-TDAA-BNF-DEATH-DT > 0 ) AND ( TDB-TDAA-BNF-DEATH-DT  \n040686         NOT > 20191231 ) )\n040688         NEXT SENTENCE ELSE\n040690         GO TO Z-5-186-1-ELSE.\n040692     MOVE ZEROS TO WS-MD-FACT\n040694       , WS-MD-TBL\n040696       , WS-MD-AMT.\n040698 Z-5-186-1-ELSE.\n040700 Z-5-185-1-ELSE.\n040702     IF TDB-TDAA-INHERIT-IRA = 0\n040704         NEXT SENTENCE ELSE\n040706         GO TO Z-5-188-1-ELSE.\n040708     ADD WS-MD-FMV TO WS-TIN-BAL-TOT .\n040710     ADD WS-MD-AMT TO WS-TIN-RMD-TOT .\n040712 Z-5-188-1-ELSE.\n040714     IF ( WS-BANK-OPT = 3 ) AND ( TDB-TDAA-RMD-MAN-CALC = ZERO )  \n040716         AND ( WS-MD-AMT > 0 )\n040718         NEXT SENTENCE ELSE\n040720         GO TO Z-5-191-1-ELSE.\n040722 Z-5-192-BEGIN.\n040724*      REQUESTED UPDATE OF FILE CST-FILE-MAINT\n040726     MOVE 5 TO Z-FLINFO6-UPDATE.\n040728     MOVE WS-BANK-NO TO FM2-BANK.\n040730     MOVE TDB-TDAA-CUST TO FM2-CUST.\n040732     MOVE TDB-TDAA-ACCT TO FM2-ACCT.\n040734     MOVE 02 TO FM2-STRUCT.\n040736     MOVE 00 TO FM2-RECORD-NBR.\n040738     MOVE 0067 TO FM2-TRANCODE.\n040740     MOVE WS-MD-AMT TO WS-FM-AMT.\n040742     MOVE WS-FM-AMT-X TO FM2-CHANGE-DATA.\n040744     MOVE \"R\" TO FM2-APPLY.\n040746     MOVE \"RMDRPT\" TO FM2-ORIGIN.\n040748     MOVE SPACE TO FM2-INT.\n040750     MOVE SPACE TO FM2-SYSTEM-USE.\n040752     IF Z-EDIT-ERROR\n040754         GO TO Z-5-XIT.\n040756     IF Z-FLINFO6-UPDATE = 5\n040758         NEXT SENTENCE ELSE\n040760         GO TO Z-5-193-SKIP.\n040762     WRITE MASS-FM-RECORD2\n040764         INVALID KEY\n040766         MOVE Z-FLINFO6-STATUS TO Z-FL-EXCEPT-STATUS\n040768         MOVE \"CST-FILE-MAINT\" TO Z-FL-EXCEPT-FILE\n040770         MOVE 1422 TO Z-FL-EXCEPT-SEQ\n040772         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.\n040774     MOVE Z-FILE6-KEY TO Z-FLINFO6-RS-KEY.\n040776     MOVE ZERO TO Z-FLINFO6-UPDATE.\n040778     MOVE ZERO TO Z-FLINFO6-LAST-SEQ.\n040780 Z-5-193-SKIP.\n040782 Z-5-192-SKIP.\n040784*\n040786 Z-5-192-XIT.\n040788     MOVE 0 TO Z-EXIT-CODE.\n040790     MOVE 9999 TO Z-EXIT-LEVEL.\n040792     MOVE SPACES TO MASS-FM-RECORD2.\n040794 Z-5-207-BEGIN.\n040796*      REQUESTED UPDATE OF FILE CST-FILE-MAINT\n040798     MOVE 6 TO Z-FLINFO6-UPDATE.\n040800     MOVE WS-BANK-NO TO FM2-BANK.\n040802     MOVE TDB-TDAA-CUST TO FM2-CUST.\n040804     MOVE TDB-TDAA-ACCT TO FM2-ACCT.\n040806     MOVE 02 TO FM2-STRUCT.\n040808     MOVE 00 TO FM2-RECORD-NBR.\n040810     MOVE 0397 TO FM2-TRANCODE.\n040812     MOVE WS-MD-FACT TO WS-FM-LEF.\n040814     MOVE WS-FM-LEF-X TO FM2-CHANGE-DATA.\n040816     MOVE \"R\" TO FM2-APPLY.\n040818     MOVE \"RMDRPT\" TO FM2-ORIGIN.\n040820     MOVE SPACE TO FM2-INT\n040822       , FM2-SYSTEM-USE.\n040824     IF Z-EDIT-ERROR\n040826         GO TO Z-5-XIT.\n040828     IF Z-FLINFO6-UPDATE = 6\n040830         NEXT SENTENCE ELSE\n040832         GO TO Z-5-208-SKIP.\n040834     WRITE MASS-FM-RECORD2\n040836         INVALID KEY\n040838         MOVE Z-FLINFO6-STATUS TO Z-FL-EXCEPT-STATUS\n040840         MOVE \"CST-FILE-MAINT\" TO Z-FL-EXCEPT-FILE\n040842         MOVE 1440 TO Z-FL-EXCEPT-SEQ\n040844         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.\n040846     MOVE Z-FILE6-KEY TO Z-FLINFO6-RS-KEY.\n040848     MOVE ZERO TO Z-FLINFO6-UPDATE.\n040850     MOVE ZERO TO Z-FLINFO6-LAST-SEQ.\n040852 Z-5-208-SKIP.\n040854 Z-5-207-SKIP.\n040856*\n040858 Z-5-207-XIT.\n040860     MOVE 0 TO Z-EXIT-CODE.\n040862     MOVE 9999 TO Z-EXIT-LEVEL.\n040864     MOVE SPACES TO MASS-FM-RECORD2.\n040866     IF WS-RMDFM2-CUST-IND = 0\n040868         NEXT SENTENCE ELSE\n040870         GO TO Z-5-221-1-ELSE.\n040872     MOVE 1 TO WS-RMDFM2-CUST-IND.\n040874 Z-5-221-1-ELSE.\n040876 Z-5-191-1-ELSE.\n040878************ PERFORM WRITE-REPORT\n040880     PERFORM Z-23-PROCEDURE THRU Z-23-XIT.\n040882     IF  Z-EXIT-EDITEXIT\n040884         GO TO Z-5-XIT.\n040886     IF  Z-DMS2-ABORT-FLAG = 1\n040888         GO TO Z-5-XIT.\n040890     IF  Z-EXIT-LEVEL < 0\n040892         GO TO Z-5-14-END.\n040894*\n040896 Z-5-183-1-ELSE.\n040898 Z-5-14-END.\n040900     IF Z-EDIT-ERROR\n040902         GO TO Z-5-XIT.\n040904 Z-5-14-SKIP.\n040906     IF Z-EXIT-LEVEL < 2\n040908         GO TO Z-5-3-END.\n040910     IF Z-EXIT-CODE > 0\n040912         GO TO Z-5-14-XIT.\n040914     GO TO Z-5-14-LOOP.\n040916*\n040918 Z-5-14-XIT.\n040920     MOVE 0 TO Z-EXIT-CODE.\n040922     MOVE 9999 TO Z-EXIT-LEVEL.\n040924     IF ( WS-BANK-OPT = 3 ) AND ( ( WS-RMDFM2-CUST-IND = 1 ) OR ( \n040926         TDB-TDAC-RMD-YR-AMT > 0 ) )\n040928         NEXT SENTENCE ELSE\n040930         GO TO Z-5-224-1-ELSE.\n040932     ADD 1 TO WS-TIN-CUST-INDEX .\n040934     IF WS-TIN-CUST-INDEX NOT > 50\n040936         NEXT SENTENCE\n040938     ELSE\n040940         GO TO Z-5-226-END-MOVE.\n040942     MOVE TDB-TDAC-CUST TO WS-TIN-CUST (WS-TIN-CUST-INDEX).\n040944 Z-5-226-END-MOVE.\n040946 Z-5-224-1-ELSE.\n040948 Z-5-3-END.\n040950     IF Z-EDIT-ERROR\n040952         GO TO Z-5-XIT.\n040954 Z-5-3-SKIP.\n040956     IF Z-EXIT-LEVEL < 1\n040958         GO TO Z-5-END.\n040960     IF Z-EXIT-CODE > 0\n040962         GO TO Z-5-3-XIT.\n040964     GO TO Z-5-3-LOOP.\n040966*\n040968 Z-5-3-XIT.\n040970     MOVE 0 TO Z-EXIT-CODE.\n040972     MOVE 9999 TO Z-EXIT-LEVEL.\n040974************ PERFORM WRITE-CUST-FM-REC\n040976     PERFORM Z-26-PROCEDURE THRU Z-26-XIT.\n040978     IF  Z-EXIT-EDITEXIT\n040980         GO TO Z-5-XIT.\n040982     IF  Z-DMS2-ABORT-FLAG = 1\n040984         GO TO Z-5-XIT.\n040986     IF  Z-EXIT-LEVEL < 0\n040988         GO TO Z-5-END.\n040990*\n040992     MOVE 0 TO WS-TIN-CUST-INDEX.\n040994     IF WS-MDRPT-OPEN > 0\n040996         NEXT SENTENCE ELSE\n040998         GO TO Z-5-229-1-ELSE.\n041000     IF ( SPECS-COMB-AUTO-RMD-ADJUST = \"Y\" )\n041002         NEXT SENTENCE ELSE\n041004         GO TO Z-5-230-1-ELSE.\n041006     MOVE 1 TO J.\n041008     COMPUTE Z-TO-2 = WS-TIN-DETAIL-MAX.\n041010 Z-5-231-LOOP.\n041012     IF J > Z-TO-2\n041014         GO TO Z-5-231-XIT.\n041016     MOVE 0 TO Z-EXIT-CODE.\n041018     MOVE 9999 TO Z-EXIT-LEVEL.\n041020********* EXIT WHEN\n041022     IF WS-TIN-DET-LINE-3 (J) = SPACES\n041024        NEXT SENTENCE\n041026     ELSE\n041028        GO TO Z-5-232-EXIT-SKIP.\n041030     MOVE 1 TO Z-EXIT-LEVEL.\n041032     MOVE 1 TO Z-EXIT-CODE.\n041034     GO TO Z-5-231-END.\n041036 Z-5-232-EXIT-SKIP.\n041038     MOVE SPACES TO RMDRPT-REC-3.\n041040     MOVE WS-TIN-DET-LINE-3 (J) TO RMDRPT-REC-3.\n041042     IF ( RMDRPT-DS-NTRVL-3 NOT = \"NONE\" ) AND ( RMDRPT-DS-FREQ-3 \n041044         NOT = \"I\" ) AND ( WS-TIN-DISTR-RECS = 1 )\n041046         NEXT SENTENCE ELSE\n041048         GO TO Z-5-235-1-ELSE.\n041050     IF WS-TIN-DET-DIST-FREQ (J) = \"D\"\n041052         NEXT SENTENCE ELSE\n041054         GO TO Z-5-236-1-ELSE.\n041056     COMPUTE RMDRPT-NEW-DS-AMT-3 ROUNDED = ( ( WS-TIN-RMD-TOT /   \n041058         365 ) * WS-TIN-DET-DS-NTRVL (J) ) .\n041060\n041062     GO TO Z-5-236-ENDIF.\n041064 Z-5-236-1-ELSE.\n041066     IF WS-TIN-DET-DIST-FREQ (J) = \"M\"\n041068         NEXT SENTENCE ELSE\n041070         GO TO Z-5-236-2-ELSE.\n041072     COMPUTE RMDRPT-NEW-DS-AMT-3 ROUNDED = ( ( WS-TIN-RMD-TOT /   \n041074         12 ) * WS-TIN-DET-DS-NTRVL (J) ) .\n041076\n041078     GO TO Z-5-236-ENDIF.\n041080 Z-5-236-2-ELSE.\n041082     COMPUTE RMDRPT-NEW-DS-AMT-3 = WS-TIN-RMD-TOT .\n041084\n041086 Z-5-236-ENDIF.\n041088 Z-5-235-1-ELSE.\n041090     IF NOT Z-SW3\n041092         NEXT SENTENCE ELSE\n041094         GO TO Z-5-240-1-ELSE.\n041096     COMPUTE Z-LINES-HOLD = 1.\n041098     COMPUTE Z-LINES = 1.\n041100     IF Z-RPT-1-TRAP > ZERO\n041102         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n041104     IF Z-LINES > Z-RPT-1-TRAP\n041106       IF Z-RPTINFO1-INBLOCK = ZERO\n041108         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n041110         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n041112         COMPUTE Z-LINES = 1.\n041114     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n041116     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n041118     MOVE RMDRPT-REC-3 TO Z-RPT-1-BUFFER.\n041120     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n041122 Z-5-240-1-ELSE.\n041124     MOVE SPACES TO RMDRPT-REC-4.\n041126     MOVE WS-TIN-DET-LINE-4 (J) TO RMDRPT-REC-4.\n041128     IF NOT Z-SW3\n041130         NEXT SENTENCE ELSE\n041132         GO TO Z-5-244-1-ELSE.\n041134     COMPUTE Z-LINES-HOLD = 1.\n041136     COMPUTE Z-LINES = 1.\n041138     IF Z-RPT-1-TRAP > ZERO\n041140         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n041142     IF Z-LINES > Z-RPT-1-TRAP\n041144       IF Z-RPTINFO1-INBLOCK = ZERO\n041146         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n041148         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n041150         COMPUTE Z-LINES = 1.\n041152     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n041154     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n041156     MOVE RMDRPT-REC-4 TO Z-RPT-1-BUFFER.\n041158     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n041160 Z-5-244-1-ELSE.\n041162     MOVE SPACES TO RMDRPT-REC-8.\n041164     IF ( WS-TIN-DET-LINE-8 (J) NOT = SPACES ) AND ( NOT Z-SW3 )\n041166         NEXT SENTENCE ELSE\n041168         GO TO Z-5-247-1-ELSE.\n041170     MOVE WS-TIN-DET-LINE-8 (J) TO RMDRPT-REC-8.\n041172     COMPUTE Z-LINES-HOLD = 1.\n041174     COMPUTE Z-LINES = 1.\n041176     IF Z-RPT-1-TRAP > ZERO\n041178         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n041180     IF Z-LINES > Z-RPT-1-TRAP\n041182       IF Z-RPTINFO1-INBLOCK = ZERO\n041184         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n041186         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n041188         COMPUTE Z-LINES = 1.\n041190     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n041192     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n041194     MOVE RMDRPT-REC-8 TO Z-RPT-1-BUFFER.\n041196     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n041198 Z-5-247-1-ELSE.\n041200 Z-5-231-END.\n041202     IF Z-EDIT-ERROR\n041204         GO TO Z-5-XIT.\n041206 Z-5-231-SKIP.\n041208     IF Z-EXIT-LEVEL < 1\n041210         GO TO Z-5-END.\n041212     IF Z-EXIT-CODE > 0\n041214         GO TO Z-5-231-XIT.\n041216     ADD 1 TO J.\n041218     GO TO Z-5-231-LOOP.\n041220*\n041222 Z-5-231-XIT.\n041224     MOVE 0 TO Z-EXIT-CODE.\n041226     MOVE 9999 TO Z-EXIT-LEVEL.\n041228     MOVE SPACES TO WS-TIN-DETAIL-TABLE.\n041230     MOVE 0 TO WS-TIN-DETAIL-INDEX.\n041232************ PERFORM COMB-AUTO-RMD-ADJ\n041234     IF ( SPECS-COMB-AUTO-RMD-ADJUST = \"Y\" )\n041236        NEXT SENTENCE ELSE\n041238        GO TO Z-5-252-SKIPPROC.\n041240************ PERFORM COMB-AUTO-RMD-ADJ\n041242     PERFORM Z-27-PROCEDURE THRU Z-27-XIT.\n041244     IF  Z-EXIT-EDITEXIT\n041246         GO TO Z-5-XIT.\n041248     IF  Z-DMS2-ABORT-FLAG = 1\n041250         GO TO Z-5-XIT.\n041252     IF  Z-EXIT-LEVEL < 0\n041254         GO TO Z-5-END.\n041256*\n041258 Z-5-252-SKIPPROC.\n041260     MOVE 0 TO WS-TIN-DISTR-RECS.\n041262 Z-5-230-1-ELSE.\n041264     IF WS-NON-INHERIT-IRA-ON-TIN = 1\n041266         NEXT SENTENCE ELSE\n041268         GO TO Z-5-254-1-ELSE.\n041270     MOVE WS-PREV-TIN TO WS-RMDRPT-TIN.\n041272     MOVE \"-\" TO WS-RMDRPT-TIN-LDASH\n041274       , WS-RMDRPT-TIN-RDASH.\n041276     MOVE WS-RMDRPT-TIN TO RMDRPT-TOT-TIN-9.\n041278     MOVE WS-TIN-BAL-TOT TO RMDRPT-TIN-TOT-BAL-9.\n041280     MOVE WS-TIN-RMD-TOT TO RMDRPT-TIN-TOT-RMD-9.\n041282     IF NOT Z-SW3\n041284         NEXT SENTENCE ELSE\n041286         GO TO Z-5-260-1-ELSE.\n041288     COMPUTE Z-LINES-HOLD = 1.\n041290     COMPUTE Z-LINES = 1.\n041292     IF Z-RPT-1-TRAP > ZERO\n041294         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n041296     IF Z-LINES > Z-RPT-1-TRAP\n041298       IF Z-RPTINFO1-INBLOCK = ZERO\n041300         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n041302         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n041304         COMPUTE Z-LINES = 1.\n041306     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n041308     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n041310     MOVE RMDRPT-REC-9 TO Z-RPT-1-BUFFER.\n041312     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n041314     COMPUTE Z-LINES-HOLD = 1.\n041316     COMPUTE Z-LINES = 1.\n041318     IF Z-RPT-1-TRAP > ZERO\n041320         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n041322     IF Z-LINES > Z-RPT-1-TRAP\n041324       IF Z-RPTINFO1-INBLOCK = ZERO\n041326         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n041328         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n041330         COMPUTE Z-LINES = 1.\n041332     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n041334     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n041336     MOVE SPACES TO Z-RPT-1-BUFFER.\n041338     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n041340 Z-5-260-1-ELSE.\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    533 lines from 20134 to 20666.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 42, "total_chunks": 55, "start_line": 20134, "end_line": 20666, "line_count": 533}

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
- Source code length: 25184 characters

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
CHUNK 42 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 20134 to 20666 (533 lines)
Chunk Tokens (estimated): ~7,836
Actual Input Tokens: 9,242 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 20134-20666 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 42 of 55 chunks
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
      The source code below is only CHUNK 42 of 55.


=============================================================================
CHUNK 42 SOURCE CODE (Lines 20134-20666)
=============================================================================

```cobol
040276 Z-5-86-1-ELSE.
040278************ PERFORM WRITE-REPORT
040280     PERFORM Z-23-PROCEDURE THRU Z-23-XIT.
040282     IF  Z-EXIT-EDITEXIT
040284         GO TO Z-5-XIT.
040286     IF  Z-DMS2-ABORT-FLAG = 1
040288         GO TO Z-5-XIT.
040290     IF  Z-EXIT-LEVEL < 0
040292         GO TO Z-5-82-END.
040294*
040296     IF ( SPECS-RMD-OVERRIDE = "Y" ) AND ( WS-NEW-DS-AMT > 0 )    
040298         AND ( TDB-TDAD-RMD-OVERRIDE = 0 ) AND (                  
040300         WS-IRA-DISTR-RECS = 1 )
040302         NEXT SENTENCE ELSE
040304         GO TO Z-5-127-1-ELSE.
040306     IF WS-DSTFM-OPEN = 0
040308         NEXT SENTENCE ELSE
040310         GO TO Z-5-128-1-ELSE.
040312     MOVE PROCESS-DATE-MMDD TO WS-DSTFM-DT.
040314     IF WS-BANK-OPT = 1
040316         NEXT SENTENCE ELSE
040318         GO TO Z-5-130-1-ELSE.
040320     MOVE WS-BANK-NO TO WS-DSTFM-BK.
040322     MOVE SPACES TO WS-DSTFM-TIME.
040324     GO TO Z-5-130-ENDIF.
040326 Z-5-130-1-ELSE.
040328     IF WS-BANK-OPT = 2
040330         NEXT SENTENCE ELSE
040332         GO TO Z-5-130-2-ELSE.
040334     MOVE 000 TO WS-DSTFM-BK.
040336*    RETRIEVE TODAY'S DATE
040338     CALL "CURRENT_DATE OF GENERALSUPPORT"
040340          USING Z-CALL-CURRENTDATE.
040342     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
040344     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
040346     ACCEPT Z-DATE0-TIME   FROM TIME.
040348     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.
040350     MOVE Z-DATE0-UU TO Z-DATE4-UU.
040352     MOVE Z-DATE4-FORMAT TO WS-DSTFM-TIME.
040354     GO TO Z-5-130-ENDIF.
040356 Z-5-130-2-ELSE.
040358     IF WS-BANK-OPT = 3
040360         NEXT SENTENCE ELSE
040362         GO TO Z-5-130-3-ELSE.
040364     MOVE 000 TO WS-DSTFM-BK.
040366     MOVE SPACES TO WS-DSTFM-SUFF-R.
040368     MOVE WS-SUFFIX-IN TO WS-DSTFM-SUFF.
040370 Z-5-130-3-ELSE.
040372 Z-5-130-ENDIF.
040374*
040376******* OPEN FILE DST-FILE-MAINT
040378*
040380     IF Z-FLINFO5-OPEN = 0
040382         CHANGE ATTRIBUTE NEWFILE OF DST-FILE-MAINT TO VALUE TRUE
040384         OPEN OUTPUT DST-FILE-MAINT 
040386         IF ATTRIBUTE FILESTATE OF DST-FILE-MAINT = VALUE OPENED
040388             MOVE ZEROS TO Z-FILE5-KEY
040390             MOVE ZEROS TO Z-FLINFO5-RS-KEY
040392             MOVE 3 TO Z-FLINFO5-OPEN
040394             MOVE 3 TO Z-FLINFO5-RS-OPEN
040396         ELSE
040398             DISPLAY ">>> FILE DST-FILE-MAINT FAILED TO OPEN"
040400             MOVE ATTRIBUTE TITLE OF DST-FILE-MAINT TO            
040402                 Z-FL-EXCEPT-TITLE
040404             DISPLAY ">>> OPEN FAIL, TITLE :", Z-FL-EXCEPT-TITLE
040406             DISPLAY ">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS".
040408     MOVE 1 TO WS-DSTFM-OPEN.
040410 Z-5-128-1-ELSE.
040412     IF ( SPECS-COMB-AUTO-RMD-ADJUST = "Y" ) AND (                
040414         TDB-TDAA-INHERIT-IRA = 0 )
040416         NEXT SENTENCE ELSE
040418         GO TO Z-5-140-1-ELSE.
040420     ADD 1 TO WS-TIN-RMD-INDEX .
040422     IF WS-TIN-RMD-INDEX NOT > WS-TIN-RMD-MAX
040424         NEXT SENTENCE ELSE
040426         GO TO Z-5-142-1-ELSE.
040428     MOVE TDB-TDAI-CUST TO WS-TIN-RMD-CUST (WS-TIN-RMD-INDEX).
040430     MOVE TDB-TDAI-ACCT TO WS-TIN-RMD-ACCT (WS-TIN-RMD-INDEX).
040432     MOVE TDB-TDAD-DS-NBR TO WS-TIN-RMD-DS-NBR (WS-TIN-RMD-INDEX).
040434     MOVE TDB-TDAD-DS-FREQ TO WS-TIN-RMD-DS-FREQ                  
040436         (WS-TIN-RMD-INDEX).
040438     MOVE TDB-TDAD-DS-NTRVL TO WS-TIN-RMD-DS-NTRVL                
040440         (WS-TIN-RMD-INDEX).
040442     MOVE WS-NEW-DS-AMT TO WS-TIN-RMD-AMT (WS-TIN-RMD-INDEX).
040444 Z-5-142-1-ELSE.
040446     GO TO Z-5-140-ENDIF.
040448 Z-5-140-1-ELSE.
040450 Z-5-149-BEGIN.
040452*      REQUESTED UPDATE OF FILE DST-FILE-MAINT
040454     MOVE 3 TO Z-FLINFO5-UPDATE.
040456     MOVE WS-BANK-NO TO FM-BANK.
040458     MOVE TDB-TDAI-CUST TO FM-CUST.
040460     MOVE TDB-TDAI-ACCT TO FM-ACCT.
040462     MOVE 15 TO FM-STRUCT.
040464     MOVE TDB-TDAD-DS-NBR TO FM-RECORD-NBR.
040466     MOVE 0712 TO FM-TRANCODE.
040468     MOVE WS-NEW-DS-AMT TO WS-FM-AMT.
040470     MOVE WS-FM-AMT-X TO FM-CHANGE-DATA.
040472     MOVE "R" TO FM-APPLY.
040474     MOVE "RMDRPT" TO FM-ORIGIN.
040476     MOVE SPACE TO FM-INT.
040478     MOVE SPACE TO FM-SYSTEM-USE.
040480     IF Z-EDIT-ERROR
040482         GO TO Z-5-XIT.
040484     IF Z-FLINFO5-UPDATE = 3
040486         NEXT SENTENCE ELSE
040488         GO TO Z-5-150-SKIP.
040490     WRITE MASS-FM-RECORD
040492         INVALID KEY
040494         MOVE Z-FLINFO5-STATUS TO Z-FL-EXCEPT-STATUS
040496         MOVE "DST-FILE-MAINT" TO Z-FL-EXCEPT-FILE
040498         MOVE 1354 TO Z-FL-EXCEPT-SEQ
040500         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.
040502     MOVE Z-FILE5-KEY TO Z-FLINFO5-RS-KEY.
040504     MOVE ZERO TO Z-FLINFO5-UPDATE.
040506     MOVE ZERO TO Z-FLINFO5-LAST-SEQ.
040508 Z-5-150-SKIP.
040510 Z-5-149-SKIP.
040512*
040514 Z-5-149-XIT.
040516     MOVE 0 TO Z-EXIT-CODE.
040518     MOVE 9999 TO Z-EXIT-LEVEL.
040520 Z-5-140-ENDIF.
040522     IF TDB-TDAA-INHERIT-IRA > 0
040524         NEXT SENTENCE ELSE
040526         GO TO Z-5-163-1-ELSE.
040528     ADD 1 TO RMD-TOT-CHGD-INHERIT .
040530     GO TO Z-5-163-ENDIF.
040532 Z-5-163-1-ELSE.
040534     ADD 1 TO RMD-TOT-CHGD .
040536 Z-5-163-ENDIF.
040538     IF TDB-TDAD-AMT-CD = 1
040540         NEXT SENTENCE ELSE
040542         GO TO Z-5-166-1-ELSE.
040544 Z-5-167-BEGIN.
040546*      REQUESTED UPDATE OF FILE DST-FILE-MAINT
040548     MOVE 4 TO Z-FLINFO5-UPDATE.
040550     MOVE WS-BANK-NO TO FM-BANK.
040552     MOVE TDB-TDAI-CUST TO FM-CUST.
040554     MOVE TDB-TDAI-ACCT TO FM-ACCT.
040556     MOVE 15 TO FM-STRUCT.
040558     MOVE TDB-TDAD-DS-NBR TO FM-RECORD-NBR.
040560     MOVE 0711 TO FM-TRANCODE.
040562     MOVE 0 TO WS-FM-AMT-CD.
040564     MOVE WS-FM-AMT-CD-X TO FM-CHANGE-DATA.
040566     MOVE "R" TO FM-APPLY.
040568     MOVE "RMDRPT" TO FM-ORIGIN.
040570     MOVE SPACE TO FM-INT.
040572     MOVE SPACE TO FM-SYSTEM-USE.
040574     IF Z-EDIT-ERROR
040576         GO TO Z-5-XIT.
040578     IF Z-FLINFO5-UPDATE = 4
040580         NEXT SENTENCE ELSE
040582         GO TO Z-5-168-SKIP.
040584     WRITE MASS-FM-RECORD
040586         INVALID KEY
040588         MOVE Z-FLINFO5-STATUS TO Z-FL-EXCEPT-STATUS
040590         MOVE "DST-FILE-MAINT" TO Z-FL-EXCEPT-FILE
040592         MOVE 1378 TO Z-FL-EXCEPT-SEQ
040594         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.
040596     MOVE Z-FILE5-KEY TO Z-FLINFO5-RS-KEY.
040598     MOVE ZERO TO Z-FLINFO5-UPDATE.
040600     MOVE ZERO TO Z-FLINFO5-LAST-SEQ.
040602 Z-5-168-SKIP.
040604 Z-5-167-SKIP.
040606*
040608 Z-5-167-XIT.
040610     MOVE 0 TO Z-EXIT-CODE.
040612     MOVE 9999 TO Z-EXIT-LEVEL.
040614 Z-5-166-1-ELSE.
040616 Z-5-127-1-ELSE.
040618     MOVE ZEROS TO WS-NEW-DS-AMT.
040620     MOVE SPACES TO MASS-FM-RECORD.
040622 Z-5-82-END.
040624     IF Z-EDIT-ERROR
040626         GO TO Z-5-XIT.
040628 Z-5-82-SKIP.
040630     IF Z-EXIT-LEVEL < 3
040632         GO TO Z-5-14-END.
040634     IF Z-EXIT-CODE > 0
040636         GO TO Z-5-82-XIT.
040638     GO TO Z-5-82-LOOP.
040640*
040642 Z-5-82-XIT.
040644     MOVE 0 TO Z-EXIT-CODE.
040646     MOVE 9999 TO Z-EXIT-LEVEL.
040648     IF WS-DSREC-FLAG = 0
040650         NEXT SENTENCE ELSE
040652         GO TO Z-5-183-1-ELSE.
040654************ PERFORM TDD-MINDIST-SETUP-AND-CALC
040656     PERFORM Z-28-PROCEDURE THRU Z-28-XIT.
040658     IF  Z-EXIT-EDITEXIT
040660         GO TO Z-5-XIT.
040662     IF  Z-DMS2-ABORT-FLAG = 1
040664         GO TO Z-5-XIT.
040666     IF  Z-EXIT-LEVEL < 0
040668         GO TO Z-5-14-END.
040670*
040672     IF ( TDB-TDAA-INHERIT-IRA = 2 ) AND ( TDB-TDAA-RMD-MAN-CALC  
040674         = 0 )
040676         NEXT SENTENCE ELSE
040678         GO TO Z-5-185-1-ELSE.
040680     IF ( TDB-TDAA-BNF-DEATH-DT > 20191231 ) OR ( (               
040682         TDB-TDAA-IRA-TYPE = 13 OR 15 OR 17 ) AND (               
040684         TDB-TDAA-BNF-DEATH-DT > 0 ) AND ( TDB-TDAA-BNF-DEATH-DT  
040686         NOT > 20191231 ) )
040688         NEXT SENTENCE ELSE
040690         GO TO Z-5-186-1-ELSE.
040692     MOVE ZEROS TO WS-MD-FACT
040694       , WS-MD-TBL
040696       , WS-MD-AMT.
040698 Z-5-186-1-ELSE.
040700 Z-5-185-1-ELSE.
040702     IF TDB-TDAA-INHERIT-IRA = 0
040704         NEXT SENTENCE ELSE
040706         GO TO Z-5-188-1-ELSE.
040708     ADD WS-MD-FMV TO WS-TIN-BAL-TOT .
040710     ADD WS-MD-AMT TO WS-TIN-RMD-TOT .
040712 Z-5-188-1-ELSE.
040714     IF ( WS-BANK-OPT = 3 ) AND ( TDB-TDAA-RMD-MAN-CALC = ZERO )  
040716         AND ( WS-MD-AMT > 0 )
040718         NEXT SENTENCE ELSE
040720         GO TO Z-5-191-1-ELSE.
040722 Z-5-192-BEGIN.
040724*      REQUESTED UPDATE OF FILE CST-FILE-MAINT
040726     MOVE 5 TO Z-FLINFO6-UPDATE.
040728     MOVE WS-BANK-NO TO FM2-BANK.
040730     MOVE TDB-TDAA-CUST TO FM2-CUST.
040732     MOVE TDB-TDAA-ACCT TO FM2-ACCT.
040734     MOVE 02 TO FM2-STRUCT.
040736     MOVE 00 TO FM2-RECORD-NBR.
040738     MOVE 0067 TO FM2-TRANCODE.
040740     MOVE WS-MD-AMT TO WS-FM-AMT.
040742     MOVE WS-FM-AMT-X TO FM2-CHANGE-DATA.
040744     MOVE "R" TO FM2-APPLY.
040746     MOVE "RMDRPT" TO FM2-ORIGIN.
040748     MOVE SPACE TO FM2-INT.
040750     MOVE SPACE TO FM2-SYSTEM-USE.
040752     IF Z-EDIT-ERROR
040754         GO TO Z-5-XIT.
040756     IF Z-FLINFO6-UPDATE = 5
040758         NEXT SENTENCE ELSE
040760         GO TO Z-5-193-SKIP.
040762     WRITE MASS-FM-RECORD2
040764         INVALID KEY
040766         MOVE Z-FLINFO6-STATUS TO Z-FL-EXCEPT-STATUS
040768         MOVE "CST-FILE-MAINT" TO Z-FL-EXCEPT-FILE
040770         MOVE 1422 TO Z-FL-EXCEPT-SEQ
040772         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.
040774     MOVE Z-FILE6-KEY TO Z-FLINFO6-RS-KEY.
040776     MOVE ZERO TO Z-FLINFO6-UPDATE.
040778     MOVE ZERO TO Z-FLINFO6-LAST-SEQ.
040780 Z-5-193-SKIP.
040782 Z-5-192-SKIP.
040784*
040786 Z-5-192-XIT.
040788     MOVE 0 TO Z-EXIT-CODE.
040790     MOVE 9999 TO Z-EXIT-LEVEL.
040792     MOVE SPACES TO MASS-FM-RECORD2.
040794 Z-5-207-BEGIN.
040796*      REQUESTED UPDATE OF FILE CST-FILE-MAINT
040798     MOVE 6 TO Z-FLINFO6-UPDATE.
040800     MOVE WS-BANK-NO TO FM2-BANK.
040802     MOVE TDB-TDAA-CUST TO FM2-CUST.
040804     MOVE TDB-TDAA-ACCT TO FM2-ACCT.
040806     MOVE 02 TO FM2-STRUCT.
040808     MOVE 00 TO FM2-RECORD-NBR.
040810     MOVE 0397 TO FM2-TRANCODE.
040812     MOVE WS-MD-FACT TO WS-FM-LEF.
040814     MOVE WS-FM-LEF-X TO FM2-CHANGE-DATA.
040816     MOVE "R" TO FM2-APPLY.
040818     MOVE "RMDRPT" TO FM2-ORIGIN.
040820     MOVE SPACE TO FM2-INT
040822       , FM2-SYSTEM-USE.
040824     IF Z-EDIT-ERROR
040826         GO TO Z-5-XIT.
040828     IF Z-FLINFO6-UPDATE = 6
040830         NEXT SENTENCE ELSE
040832         GO TO Z-5-208-SKIP.
040834     WRITE MASS-FM-RECORD2
040836         INVALID KEY
040838         MOVE Z-FLINFO6-STATUS TO Z-FL-EXCEPT-STATUS
040840         MOVE "CST-FILE-MAINT" TO Z-FL-EXCEPT-FILE
040842         MOVE 1440 TO Z-FL-EXCEPT-SEQ
040844         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.
040846     MOVE Z-FILE6-KEY TO Z-FLINFO6-RS-KEY.
040848     MOVE ZERO TO Z-FLINFO6-UPDATE.
040850     MOVE ZERO TO Z-FLINFO6-LAST-SEQ.
040852 Z-5-208-SKIP.
040854 Z-5-207-SKIP.
040856*
040858 Z-5-207-XIT.
040860     MOVE 0 TO Z-EXIT-CODE.
040862     MOVE 9999 TO Z-EXIT-LEVEL.
040864     MOVE SPACES TO MASS-FM-RECORD2.
040866     IF WS-RMDFM2-CUST-IND = 0
040868         NEXT SENTENCE ELSE
040870         GO TO Z-5-221-1-ELSE.
040872     MOVE 1 TO WS-RMDFM2-CUST-IND.
040874 Z-5-221-1-ELSE.
040876 Z-5-191-1-ELSE.
040878************ PERFORM WRITE-REPORT
040880     PERFORM Z-23-PROCEDURE THRU Z-23-XIT.
040882     IF  Z-EXIT-EDITEXIT
040884         GO TO Z-5-XIT.
040886     IF  Z-DMS2-ABORT-FLAG = 1
040888         GO TO Z-5-XIT.
040890     IF  Z-EXIT-LEVEL < 0
040892         GO TO Z-5-14-END.
040894*
040896 Z-5-183-1-ELSE.
040898 Z-5-14-END.
040900     IF Z-EDIT-ERROR
040902         GO TO Z-5-XIT.
040904 Z-5-14-SKIP.
040906     IF Z-EXIT-LEVEL < 2
040908         GO TO Z-5-3-END.
040910     IF Z-EXIT-CODE > 0
040912         GO TO Z-5-14-XIT.
040914     GO TO Z-5-14-LOOP.
040916*
040918 Z-5-14-XIT.
040920     MOVE 0 TO Z-EXIT-CODE.
040922     MOVE 9999 TO Z-EXIT-LEVEL.
040924     IF ( WS-BANK-OPT = 3 ) AND ( ( WS-RMDFM2-CUST-IND = 1 ) OR ( 
040926         TDB-TDAC-RMD-YR-AMT > 0 ) )
040928         NEXT SENTENCE ELSE
040930         GO TO Z-5-224-1-ELSE.
040932     ADD 1 TO WS-TIN-CUST-INDEX .
040934     IF WS-TIN-CUST-INDEX NOT > 50
040936         NEXT SENTENCE
040938     ELSE
040940         GO TO Z-5-226-END-MOVE.
040942     MOVE TDB-TDAC-CUST TO WS-TIN-CUST (WS-TIN-CUST-INDEX).
040944 Z-5-226-END-MOVE.
040946 Z-5-224-1-ELSE.
040948 Z-5-3-END.
040950     IF Z-EDIT-ERROR
040952         GO TO Z-5-XIT.
040954 Z-5-3-SKIP.
040956     IF Z-EXIT-LEVEL < 1
040958         GO TO Z-5-END.
040960     IF Z-EXIT-CODE > 0
040962         GO TO Z-5-3-XIT.
040964     GO TO Z-5-3-LOOP.
040966*
040968 Z-5-3-XIT.
040970     MOVE 0 TO Z-EXIT-CODE.
040972     MOVE 9999 TO Z-EXIT-LEVEL.
040974************ PERFORM WRITE-CUST-FM-REC
040976     PERFORM Z-26-PROCEDURE THRU Z-26-XIT.
040978     IF  Z-EXIT-EDITEXIT
040980         GO TO Z-5-XIT.
040982     IF  Z-DMS2-ABORT-FLAG = 1
040984         GO TO Z-5-XIT.
040986     IF  Z-EXIT-LEVEL < 0
040988         GO TO Z-5-END.
040990*
040992     MOVE 0 TO WS-TIN-CUST-INDEX.
040994     IF WS-MDRPT-OPEN > 0
040996         NEXT SENTENCE ELSE
040998         GO TO Z-5-229-1-ELSE.
041000     IF ( SPECS-COMB-AUTO-RMD-ADJUST = "Y" )
041002         NEXT SENTENCE ELSE
041004         GO TO Z-5-230-1-ELSE.
041006     MOVE 1 TO J.
041008     COMPUTE Z-TO-2 = WS-TIN-DETAIL-MAX.
041010 Z-5-231-LOOP.
041012     IF J > Z-TO-2
041014         GO TO Z-5-231-XIT.
041016     MOVE 0 TO Z-EXIT-CODE.
041018     MOVE 9999 TO Z-EXIT-LEVEL.
041020********* EXIT WHEN
041022     IF WS-TIN-DET-LINE-3 (J) = SPACES
041024        NEXT SENTENCE
041026     ELSE
041028        GO TO Z-5-232-EXIT-SKIP.
041030     MOVE 1 TO Z-EXIT-LEVEL.
041032     MOVE 1 TO Z-EXIT-CODE.
041034     GO TO Z-5-231-END.
041036 Z-5-232-EXIT-SKIP.
041038     MOVE SPACES TO RMDRPT-REC-3.
041040     MOVE WS-TIN-DET-LINE-3 (J) TO RMDRPT-REC-3.
041042     IF ( RMDRPT-DS-NTRVL-3 NOT = "NONE" ) AND ( RMDRPT-DS-FREQ-3 
041044         NOT = "I" ) AND ( WS-TIN-DISTR-RECS = 1 )
041046         NEXT SENTENCE ELSE
041048         GO TO Z-5-235-1-ELSE.
041050     IF WS-TIN-DET-DIST-FREQ (J) = "D"
041052         NEXT SENTENCE ELSE
041054         GO TO Z-5-236-1-ELSE.
041056     COMPUTE RMDRPT-NEW-DS-AMT-3 ROUNDED = ( ( WS-TIN-RMD-TOT /   
041058         365 ) * WS-TIN-DET-DS-NTRVL (J) ) .
041060
041062     GO TO Z-5-236-ENDIF.
041064 Z-5-236-1-ELSE.
041066     IF WS-TIN-DET-DIST-FREQ (J) = "M"
041068         NEXT SENTENCE ELSE
041070         GO TO Z-5-236-2-ELSE.
041072     COMPUTE RMDRPT-NEW-DS-AMT-3 ROUNDED = ( ( WS-TIN-RMD-TOT /   
041074         12 ) * WS-TIN-DET-DS-NTRVL (J) ) .
041076
041078     GO TO Z-5-236-ENDIF.
041080 Z-5-236-2-ELSE.
041082     COMPUTE RMDRPT-NEW-DS-AMT-3 = WS-TIN-RMD-TOT .
041084
041086 Z-5-236-ENDIF.
041088 Z-5-235-1-ELSE.
041090     IF NOT Z-SW3
041092         NEXT SENTENCE ELSE
041094         GO TO Z-5-240-1-ELSE.
041096     COMPUTE Z-LINES-HOLD = 1.
041098     COMPUTE Z-LINES = 1.
041100     IF Z-RPT-1-TRAP > ZERO
041102         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
041104     IF Z-LINES > Z-RPT-1-TRAP
041106       IF Z-RPTINFO1-INBLOCK = ZERO
041108         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
041110         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
041112         COMPUTE Z-LINES = 1.
041114     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
041116     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
041118     MOVE RMDRPT-REC-3 TO Z-RPT-1-BUFFER.
041120     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
041122 Z-5-240-1-ELSE.
041124     MOVE SPACES TO RMDRPT-REC-4.
041126     MOVE WS-TIN-DET-LINE-4 (J) TO RMDRPT-REC-4.
041128     IF NOT Z-SW3
041130         NEXT SENTENCE ELSE
041132         GO TO Z-5-244-1-ELSE.
041134     COMPUTE Z-LINES-HOLD = 1.
041136     COMPUTE Z-LINES = 1.
041138     IF Z-RPT-1-TRAP > ZERO
041140         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
041142     IF Z-LINES > Z-RPT-1-TRAP
041144       IF Z-RPTINFO1-INBLOCK = ZERO
041146         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
041148         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
041150         COMPUTE Z-LINES = 1.
041152     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
041154     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
041156     MOVE RMDRPT-REC-4 TO Z-RPT-1-BUFFER.
041158     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
041160 Z-5-244-1-ELSE.
041162     MOVE SPACES TO RMDRPT-REC-8.
041164     IF ( WS-TIN-DET-LINE-8 (J) NOT = SPACES ) AND ( NOT Z-SW3 )
041166         NEXT SENTENCE ELSE
041168         GO TO Z-5-247-1-ELSE.
041170     MOVE WS-TIN-DET-LINE-8 (J) TO RMDRPT-REC-8.
041172     COMPUTE Z-LINES-HOLD = 1.
041174     COMPUTE Z-LINES = 1.
041176     IF Z-RPT-1-TRAP > ZERO
041178         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
041180     IF Z-LINES > Z-RPT-1-TRAP
041182       IF Z-RPTINFO1-INBLOCK = ZERO
041184         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
041186         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
041188         COMPUTE Z-LINES = 1.
041190     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
041192     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
041194     MOVE RMDRPT-REC-8 TO Z-RPT-1-BUFFER.
041196     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
041198 Z-5-247-1-ELSE.
041200 Z-5-231-END.
041202     IF Z-EDIT-ERROR
041204         GO TO Z-5-XIT.
041206 Z-5-231-SKIP.
041208     IF Z-EXIT-LEVEL < 1
041210         GO TO Z-5-END.
041212     IF Z-EXIT-CODE > 0
041214         GO TO Z-5-231-XIT.
041216     ADD 1 TO J.
041218     GO TO Z-5-231-LOOP.
041220*
041222 Z-5-231-XIT.
041224     MOVE 0 TO Z-EXIT-CODE.
041226     MOVE 9999 TO Z-EXIT-LEVEL.
041228     MOVE SPACES TO WS-TIN-DETAIL-TABLE.
041230     MOVE 0 TO WS-TIN-DETAIL-INDEX.
041232************ PERFORM COMB-AUTO-RMD-ADJ
041234     IF ( SPECS-COMB-AUTO-RMD-ADJUST = "Y" )
041236        NEXT SENTENCE ELSE
041238        GO TO Z-5-252-SKIPPROC.
041240************ PERFORM COMB-AUTO-RMD-ADJ
041242     PERFORM Z-27-PROCEDURE THRU Z-27-XIT.
041244     IF  Z-EXIT-EDITEXIT
041246         GO TO Z-5-XIT.
041248     IF  Z-DMS2-ABORT-FLAG = 1
041250         GO TO Z-5-XIT.
041252     IF  Z-EXIT-LEVEL < 0
041254         GO TO Z-5-END.
041256*
041258 Z-5-252-SKIPPROC.
041260     MOVE 0 TO WS-TIN-DISTR-RECS.
041262 Z-5-230-1-ELSE.
041264     IF WS-NON-INHERIT-IRA-ON-TIN = 1
041266         NEXT SENTENCE ELSE
041268         GO TO Z-5-254-1-ELSE.
041270     MOVE WS-PREV-TIN TO WS-RMDRPT-TIN.
041272     MOVE "-" TO WS-RMDRPT-TIN-LDASH
041274       , WS-RMDRPT-TIN-RDASH.
041276     MOVE WS-RMDRPT-TIN TO RMDRPT-TOT-TIN-9.
041278     MOVE WS-TIN-BAL-TOT TO RMDRPT-TIN-TOT-BAL-9.
041280     MOVE WS-TIN-RMD-TOT TO RMDRPT-TIN-TOT-RMD-9.
041282     IF NOT Z-SW3
041284         NEXT SENTENCE ELSE
041286         GO TO Z-5-260-1-ELSE.
041288     COMPUTE Z-LINES-HOLD = 1.
041290     COMPUTE Z-LINES = 1.
041292     IF Z-RPT-1-TRAP > ZERO
041294         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
041296     IF Z-LINES > Z-RPT-1-TRAP
041298       IF Z-RPTINFO1-INBLOCK = ZERO
041300         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
041302         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
041304         COMPUTE Z-LINES = 1.
041306     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
041308     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
041310     MOVE RMDRPT-REC-9 TO Z-RPT-1-BUFFER.
041312     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
041314     COMPUTE Z-LINES-HOLD = 1.
041316     COMPUTE Z-LINES = 1.
041318     IF Z-RPT-1-TRAP > ZERO
041320         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
041322     IF Z-LINES > Z-RPT-1-TRAP
041324       IF Z-RPTINFO1-INBLOCK = ZERO
041326         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
041328         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
041330         COMPUTE Z-LINES = 1.
041332     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
041334     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
041336     MOVE SPACES TO Z-RPT-1-BUFFER.
041338     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
041340 Z-5-260-1-ELSE.
```

⚠️  This is the source code you must document.
    533 lines from 20134 to 20666.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

