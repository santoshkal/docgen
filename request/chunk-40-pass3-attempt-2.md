# LLM Request Debug File
Generated: 2025-11-14T19:22:50.529816

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 40/55
- **Model**: gpt-4.1
- **Chunk Number**: 40
- **Pass Number**: 3
- **Attempt Number**: 2 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~6,895 tokens
- **Total Input**: ~8,853 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 40/55" (ID: detailed-code-explanation)

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


**CHUNK 40 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-14T17:36:35.036798", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 40 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 19228 to 19647 (420 lines)\nChunk Tokens (estimated): ~7,818\nActual Input Tokens: 9,224 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 19228-19647 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 40 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 40 of 55.\n\n\n=============================================================================\nCHUNK 40 SOURCE CODE (Lines 19228-19647)\n=============================================================================\n\n```cobol\n038464         TDB-TDAACCT.\n038466     MOVE TDAA-ACCR-DT OF TDAACCT TO TDB-TDAA-ACCR-DT OF          \n038468         TDB-TDAACCT.\n038470     MOVE TDAA-OPEN-DT OF TDAACCT TO TDB-TDAA-OPEN-DT OF          \n038472         TDB-TDAACCT.\n038474     MOVE TDAA-CLSD-DT OF TDAACCT TO TDB-TDAA-CLSD-DT OF          \n038476         TDB-TDAACCT.\n038478     MOVE TDAA-LST-MAT-DT OF TDAACCT TO TDB-TDAA-LST-MAT-DT OF    \n038480         TDB-TDAACCT.\n038482     MOVE TDAA-LST-POST-DT OF TDAACCT TO TDB-TDAA-LST-POST-DT OF  \n038484         TDB-TDAACCT.\n038486     MOVE TDAA-LST-IN-PROC OF TDAACCT TO TDB-TDAA-LST-IN-PROC OF  \n038488         TDB-TDAACCT.\n038490     MOVE TDAA-LST-CONTACT OF TDAACCT TO TDB-TDAA-LST-CONTACT OF  \n038492         TDB-TDAACCT.\n038494     MOVE TDAA-LST-FEE-DT OF TDAACCT TO TDB-TDAA-LST-FEE-DT OF    \n038496         TDB-TDAACCT.\n038498     MOVE TDAA-LST-RTCHG-DT OF TDAACCT TO TDB-TDAA-LST-RTCHG-DT   \n038500         OF TDB-TDAACCT.\n038502     MOVE TDAA-LST-DIST-DT OF TDAACCT TO TDB-TDAA-LST-DIST-DT OF  \n038504         TDB-TDAACCT.\n038506     MOVE TDAA-LST-STMT-DT OF TDAACCT TO TDB-TDAA-LST-STMT-DT OF  \n038508         TDB-TDAACCT.\n038510     MOVE TDAA-LST-CMPD-DT OF TDAACCT TO TDB-TDAA-LST-CMPD-DT OF  \n038512         TDB-TDAACCT.\n038514     MOVE 1 TO Z-II.\n038516 Z-5-21-2-LOOP.\n038518     IF Z-II > 10\n038520         GO TO Z-5-21-2-LOOP-XIT.\n038522     MOVE TDAA-RR-CYC-DT OF TDAACCT (Z-II) TO TDB-TDAA-RR-CYC-DT  \n038524         OF TDB-TDAACCT (Z-II).\n038526     ADD 1 TO Z-II.\n038528     GO TO Z-5-21-2-LOOP.\n038530 Z-5-21-2-LOOP-XIT.\n038532     MOVE TDAA-BNF-BIRTH-DT OF TDAACCT TO TDB-TDAA-BNF-BIRTH-DT   \n038534         OF TDB-TDAACCT.\n038536     MOVE TDAA-BNF-DEATH-DT OF TDAACCT TO TDB-TDAA-BNF-DEATH-DT   \n038538         OF TDB-TDAACCT.\n038540     MOVE TDAA-LUPD-DATE OF TDAACCT TO TDB-TDAA-LUPD-DATE OF      \n038542         TDB-TDAACCT.\n038544     MOVE TDAA-LUPD-TIME OF TDAACCT TO TDB-TDAA-LUPD-TIME OF      \n038546         TDB-TDAACCT.\n038548     MOVE TDAA-ADD-DT OF TDAACCT TO TDB-TDAA-ADD-DT OF            \n038550         TDB-TDAACCT.\n038552     MOVE TDAA-ADD-TM OF TDAACCT TO TDB-TDAA-ADD-TM OF            \n038554         TDB-TDAACCT.\n038556     MOVE TDAA-CONV-DT OF TDAACCT TO TDB-TDAA-CONV-DT OF          \n038558         TDB-TDAACCT.\n038560     MOVE TDAA-ACT-CLOSE-DT OF TDAACCT TO TDB-TDAA-ACT-CLOSE-DT   \n038562         OF TDB-TDAACCT.\n038564     MOVE TDAA-LST-TBACT-DT OF TDAACCT TO TDB-TDAA-LST-TBACT-DT   \n038566         OF TDB-TDAACCT.\n038568     MOVE TDAA-ALERT-EXP-DT OF TDAACCT TO TDB-TDAA-ALERT-EXP-DT   \n038570         OF TDB-TDAACCT.\n038572     MOVE TDAA-ALRT2-EXP-DT OF TDAACCT TO TDB-TDAA-ALRT2-EXP-DT   \n038574         OF TDB-TDAACCT.\n038576     MOVE TDAA-ALRT3-EXP-DT OF TDAACCT TO TDB-TDAA-ALRT3-EXP-DT   \n038578         OF TDB-TDAACCT.\n038580     MOVE TDAA-NXT-FEE-DT OF TDAACCT TO TDB-TDAA-NXT-FEE-DT OF    \n038582         TDB-TDAACCT.\n038584     MOVE TDAA-NXT-POST-DT OF TDAACCT TO TDB-TDAA-NXT-POST-DT OF  \n038586         TDB-TDAACCT.\n038588     MOVE TDAA-NXT-MAT-DT OF TDAACCT TO TDB-TDAA-NXT-MAT-DT OF    \n038590         TDB-TDAACCT.\n038592     MOVE TDAA-NXT-DIST-DT OF TDAACCT TO TDB-TDAA-NXT-DIST-DT OF  \n038594         TDB-TDAACCT.\n038596     MOVE TDAA-NXT-RT-CHG OF TDAACCT TO TDB-TDAA-NXT-RT-CHG OF    \n038598         TDB-TDAACCT.\n038600     MOVE TDAA-NXT-IN-PROC OF TDAACCT TO TDB-TDAA-NXT-IN-PROC OF  \n038602         TDB-TDAACCT.\n038604     MOVE TDAA-NXT-CMPD-DT OF TDAACCT TO TDB-TDAA-NXT-CMPD-DT OF  \n038606         TDB-TDAACCT.\n038608     MOVE TDAA-NXT-STMT-DT OF TDAACCT TO TDB-TDAA-NXT-STMT-DT OF  \n038610         TDB-TDAACCT.\n038612     MOVE TDAA-NXT-DS-PROC OF TDAACCT TO TDB-TDAA-NXT-DS-PROC OF  \n038614         TDB-TDAACCT.\n038616     MOVE TDAA-ADV-NTC-DT OF TDAACCT TO TDB-TDAA-ADV-NTC-DT OF    \n038618         TDB-TDAACCT.\n038620     MOVE TDAA-NXT-29YR-DT OF TDAACCT TO TDB-TDAA-NXT-29YR-DT OF  \n038622         TDB-TDAACCT.\n038624     MOVE TDAA-FAIR-MRKT-DT OF TDAACCT TO TDB-TDAA-FAIR-MRKT-DT   \n038626         OF TDB-TDAACCT.\n038628     MOVE TDAA-SORT-FIELD-1 OF TDAACCT TO TDB-TDAA-SORT-FIELD-1   \n038630         OF TDB-TDAACCT.\n038632     MOVE TDAA-SORT-FIELD-2 OF TDAACCT TO TDB-TDAA-SORT-FIELD-2   \n038634         OF TDB-TDAACCT.\n038636     MOVE TDAA-SORT-FIELD-3 OF TDAACCT TO TDB-TDAA-SORT-FIELD-3   \n038638         OF TDB-TDAACCT.\n038640     MOVE TDAA-SORT-FIELD-4 OF TDAACCT TO TDB-TDAA-SORT-FIELD-4   \n038642         OF TDB-TDAACCT.\n038644     MOVE TDAA-CMAT-PUB-ID OF TDAACCT TO TDB-TDAA-CMAT-PUB-ID OF  \n038646         TDB-TDAACCT.\n038648     MOVE TDAA-MSA-CONTR OF TDAACCT TO TDB-TDAA-MSA-CONTR OF      \n038650         TDB-TDAACCT.\n038652     MOVE TDAA-MSA-CONTR-LY OF TDAACCT TO TDB-TDAA-MSA-CONTR-LY   \n038654         OF TDB-TDAACCT.\n038656     MOVE TDAA-AVG-ACCR-INT OF TDAACCT TO TDB-TDAA-AVG-ACCR-INT   \n038658         OF TDB-TDAACCT.\n038660     MOVE TDAA-LEVEL-PAY OF TDAACCT TO TDB-TDAA-LEVEL-PAY OF      \n038662         TDB-TDAACCT.\n038664     MOVE TDAA-ST-INT-CD OF TDAACCT TO TDB-TDAA-ST-INT-CD OF      \n038666         TDB-TDAACCT.\n038668     MOVE TDAA-ST-WHLD-CD OF TDAACCT TO TDB-TDAA-ST-WHLD-CD OF    \n038670         TDB-TDAACCT.\n038672     MOVE TDAA-ST-WHLD-AMT OF TDAACCT TO TDB-TDAA-ST-WHLD-AMT OF  \n038674         TDB-TDAACCT.\n038676     MOVE TDAA-ST-CUR-W-AMT OF TDAACCT TO TDB-TDAA-ST-CUR-W-AMT   \n038678         OF TDB-TDAACCT.\n038680     MOVE TDAA-ST-LST-W-AMT OF TDAACCT TO TDB-TDAA-ST-LST-W-AMT   \n038682         OF TDB-TDAACCT.\n038684     MOVE TDAA-ST-WHLD-STD OF TDAACCT TO TDB-TDAA-ST-WHLD-STD OF  \n038686         TDB-TDAACCT.\n038688     MOVE TDAA-ST-WHLD-YTD OF TDAACCT TO TDB-TDAA-ST-WHLD-YTD OF  \n038690         TDB-TDAACCT.\n038692     MOVE TDAA-CIF-REMARK OF TDAACCT TO TDB-TDAA-CIF-REMARK OF    \n038694         TDB-TDAACCT.\n038696     MOVE TDAA-CSR OF TDAACCT TO TDB-TDAA-CSR OF TDB-TDAACCT.\n038698     MOVE TDAA-BSA-O-RSK-CD OF TDAACCT TO TDB-TDAA-BSA-O-RSK-CD   \n038700         OF TDB-TDAACCT.\n038702     MOVE TDAA-BSA-C-RSK-CD OF TDAACCT TO TDB-TDAA-BSA-C-RSK-CD   \n038704         OF TDB-TDAACCT.\n038706     MOVE TDAA-LRG-TRX-DT OF TDAACCT TO TDB-TDAA-LRG-TRX-DT OF    \n038708         TDB-TDAACCT.\n038710     MOVE TDAA-HSA-FMLY-IND OF TDAACCT TO TDB-TDAA-HSA-FMLY-IND   \n038712         OF TDB-TDAACCT.\n038714     MOVE TDAA-STOP-PAY-IND OF TDAACCT TO TDB-TDAA-STOP-PAY-IND   \n038716         OF TDB-TDAACCT.\n038718     MOVE TDAA-IMG-PG-TYPE OF TDAACCT TO TDB-TDAA-IMG-PG-TYPE OF  \n038720         TDB-TDAACCT.\n038722     MOVE TDAA-CONT-LMT-CLC OF TDAACCT TO TDB-TDAA-CONT-LMT-CLC   \n038724         OF TDB-TDAACCT.\n038726     MOVE TDAA-CONT-LMT-ENT OF TDAACCT TO TDB-TDAA-CONT-LMT-ENT   \n038728         OF TDB-TDAACCT.\n038730     MOVE TDAA-MEMO-DB OF TDAACCT TO TDB-TDAA-MEMO-DB OF          \n038732         TDB-TDAACCT.\n038734     MOVE TDAA-MEMO-CR OF TDAACCT TO TDB-TDAA-MEMO-CR OF          \n038736         TDB-TDAACCT.\n038738     MOVE TDAA-MEMO-DB-2 OF TDAACCT TO TDB-TDAA-MEMO-DB-2 OF      \n038740         TDB-TDAACCT.\n038742     MOVE TDAA-MEMO-CR-2 OF TDAACCT TO TDB-TDAA-MEMO-CR-2 OF      \n038744         TDB-TDAACCT.\n038746     MOVE TDAA-RT-AT-CONV OF TDAACCT TO TDB-TDAA-RT-AT-CONV OF    \n038748         TDB-TDAACCT.\n038750     MOVE TDAA-ACCR-AT-CONV OF TDAACCT TO TDB-TDAA-ACCR-AT-CONV   \n038752         OF TDB-TDAACCT.\n038754     MOVE TDAA-RT-AT-ACRDT OF TDAACCT TO TDB-TDAA-RT-AT-ACRDT OF  \n038756         TDB-TDAACCT.\n038758     MOVE TDAA-BAL-AT-ACRDT OF TDAACCT TO TDB-TDAA-BAL-AT-ACRDT   \n038760         OF TDB-TDAACCT.\n038762     MOVE TDAA-ZERO-RT-ALLOW OF TDAACCT TO TDB-TDAA-ZERO-RT-ALLOW \n038764         OF TDB-TDAACCT.\n038766     MOVE TDAA-EMAIL-NTC OF TDAACCT TO TDB-TDAA-EMAIL-NTC OF      \n038768         TDB-TDAACCT.\n038770     MOVE TDAA-EMAIL-STMT OF TDAACCT TO TDB-TDAA-EMAIL-STMT OF    \n038772         TDB-TDAACCT.\n038774     MOVE TDAA-FRAUD-CK-DT OF TDAACCT TO TDB-TDAA-FRAUD-CK-DT OF  \n038776         TDB-TDAACCT.\n038778     MOVE TDAA-FRAUD-CK-CNT OF TDAACCT TO TDB-TDAA-FRAUD-CK-CNT   \n038780         OF TDB-TDAACCT.\n038782     MOVE TDAA-FRAUD-CK-AMT OF TDAACCT TO TDB-TDAA-FRAUD-CK-AMT   \n038784         OF TDB-TDAACCT.\n038786     MOVE TDAA-MISC-ACCTNO OF TDAACCT TO TDB-TDAA-MISC-ACCTNO OF  \n038788         TDB-TDAACCT.\n038790     MOVE TDAA-RMD-MAN-CALC OF TDAACCT TO TDB-TDAA-RMD-MAN-CALC   \n038792         OF TDB-TDAACCT.\n038794     MOVE TDAA-RMD-AMOUNT OF TDAACCT TO TDB-TDAA-RMD-AMOUNT OF    \n038796         TDB-TDAACCT.\n038798     MOVE TDAA-BROKERAGE-ID OF TDAACCT TO TDB-TDAA-BROKERAGE-ID   \n038800         OF TDB-TDAACCT.\n038802     MOVE TDAA-EV-LARGE-TRX OF TDAACCT TO TDB-TDAA-EV-LARGE-TRX   \n038804         OF TDB-TDAACCT.\n038806     MOVE TDAA-EV-MAT-AMT OF TDAACCT TO TDB-TDAA-EV-MAT-AMT OF    \n038808         TDB-TDAACCT.\n038810     MOVE TDAA-EV-DISP-ACCT OF TDAACCT TO TDB-TDAA-EV-DISP-ACCT   \n038812         OF TDB-TDAACCT.\n038814     MOVE TDAA-EV-COMP-ACCT OF TDAACCT TO TDB-TDAA-EV-COMP-ACCT   \n038816         OF TDB-TDAACCT.\n038818     MOVE TDAA-EV-PUBLIC-ID OF TDAACCT TO TDB-TDAA-EV-PUBLIC-ID   \n038820         OF TDB-TDAACCT.\n038822     MOVE TDAA-EV-MAT-TYPE OF TDAACCT TO TDB-TDAA-EV-MAT-TYPE OF  \n038824         TDB-TDAACCT.\n038826     MOVE TDAA-EV-INT-TYPE OF TDAACCT TO TDB-TDAA-EV-INT-TYPE OF  \n038828         TDB-TDAACCT.\n038830     MOVE TDAA-EV-ACCT-TYP OF TDAACCT TO TDB-TDAA-EV-ACCT-TYP OF  \n038832         TDB-TDAACCT.\n038834     MOVE TDAA-EV-WHLD-PCT OF TDAACCT TO TDB-TDAA-EV-WHLD-PCT OF  \n038836         TDB-TDAACCT.\n038838     MOVE TDAA-EV-NON-ACCR OF TDAACCT TO TDB-TDAA-EV-NON-ACCR OF  \n038840         TDB-TDAACCT.\n038842     MOVE TDAA-EV-CLOSED OF TDAACCT TO TDB-TDAA-EV-CLOSED OF      \n038844         TDB-TDAACCT.\n038846     MOVE TDAA-EV-CLOSE-MO OF TDAACCT TO TDB-TDAA-EV-CLOSE-MO OF  \n038848         TDB-TDAACCT.\n038850     MOVE TDAA-EV-OPEN-MO OF TDAACCT TO TDB-TDAA-EV-OPEN-MO OF    \n038852         TDB-TDAACCT.\n038854     MOVE TDAA-EV-ANN-INT OF TDAACCT TO TDB-TDAA-EV-ANN-INT OF    \n038856         TDB-TDAACCT.\n038858     MOVE TDAA-EV-ORIG-RT OF TDAACCT TO TDB-TDAA-EV-ORIG-RT OF    \n038860         TDB-TDAACCT.\n038862     MOVE TDAA-EV-DLY-INT OF TDAACCT TO TDB-TDAA-EV-DLY-INT OF    \n038864         TDB-TDAACCT.\n038866     MOVE TDAA-EV-INT-PAY OF TDAACCT TO TDB-TDAA-EV-INT-PAY OF    \n038868         TDB-TDAACCT.\n038870     MOVE TDAA-EV-AVAIL-BL OF TDAACCT TO TDB-TDAA-EV-AVAIL-BL OF  \n038872         TDB-TDAACCT.\n038874     MOVE TDAA-EV-RETAIN OF TDAACCT TO TDB-TDAA-EV-RETAIN OF      \n038876         TDB-TDAACCT.\n038878     MOVE TDAA-EV-CL-RETAIN OF TDAACCT TO TDB-TDAA-EV-CL-RETAIN   \n038880         OF TDB-TDAACCT.\n038882     MOVE TDAA-EV-TIMES-REN OF TDAACCT TO TDB-TDAA-EV-TIMES-REN   \n038884         OF TDB-TDAACCT.\n038886     MOVE TDAA-EV-CURR-BAL OF TDAACCT TO TDB-TDAA-EV-CURR-BAL OF  \n038888         TDB-TDAACCT.\n038890     MOVE TDAA-MONY-SRC-CD2 OF TDAACCT TO TDB-TDAA-MONY-SRC-CD2   \n038892         OF TDB-TDAACCT.\n038894     MOVE TDAA-INHERIT-IRA OF TDAACCT TO TDB-TDAA-INHERIT-IRA OF  \n038896         TDB-TDAACCT.\n038898     MOVE TDAA-LIFE-FACTOR OF TDAACCT TO TDB-TDAA-LIFE-FACTOR OF  \n038900         TDB-TDAACCT.\n038902     MOVE TDAA-BRKR-DEP-CAT OF TDAACCT TO TDB-TDAA-BRKR-DEP-CAT   \n038904         OF TDB-TDAACCT.\n038906     MOVE TDAA-LINE-OF-BUS OF TDAACCT TO TDB-TDAA-LINE-OF-BUS OF  \n038908         TDB-TDAACCT.\n038910     MOVE TDAA-1ST-STMT OF TDAACCT TO TDB-TDAA-1ST-STMT OF        \n038912         TDB-TDAACCT.\n038914     MOVE TDAA-POSTAL-CITY OF TDAACCT TO TDB-TDAA-POSTAL-CITY OF  \n038916         TDB-TDAACCT.\n038918     MOVE TDAA-POSTAL-CNTRY OF TDAACCT TO TDB-TDAA-POSTAL-CNTRY   \n038920         OF TDB-TDAACCT.\n038922     MOVE TDAA-CITIZN-CNTRY OF TDAACCT TO TDB-TDAA-CITIZN-CNTRY   \n038924         OF TDB-TDAACCT.\n038926     MOVE TDAA-CUSTM-FIELDS OF TDAACCT TO TDB-TDAA-CUSTM-FIELDS   \n038928         OF TDB-TDAACCT.\n038930     MOVE TDAA-AVG-STEP-RT OF TDAACCT TO TDB-TDAA-AVG-STEP-RT OF  \n038932         TDB-TDAACCT.\n038934     MOVE TDAA-MONITOR-INQ OF TDAACCT TO TDB-TDAA-MONITOR-INQ OF  \n038936         TDB-TDAACCT.\n038938     MOVE TDAA-IGL-GRP-2 OF TDAACCT TO TDB-TDAA-IGL-GRP-2 OF      \n038940         TDB-TDAACCT.\n038942     MOVE TDAA-AGG-DAYS-QTD OF TDAACCT TO TDB-TDAA-AGG-DAYS-QTD   \n038944         OF TDB-TDAACCT.\n038946     MOVE TDAA-AGG-BAL-QTD OF TDAACCT TO TDB-TDAA-AGG-BAL-QTD OF  \n038948         TDB-TDAACCT.\n038950     MOVE TDAA-IGL-GRP-3 OF TDAACCT TO TDB-TDAA-IGL-GRP-3 OF      \n038952         TDB-TDAACCT.\n038954     MOVE TDAA-ALT-ADDR-EOY OF TDAACCT TO TDB-TDAA-ALT-ADDR-EOY   \n038956         OF TDB-TDAACCT.\n038958     MOVE TDAA-1042S-TAX-ID OF TDAACCT TO TDB-TDAA-1042S-TAX-ID   \n038960         OF TDB-TDAACCT.\n038962     MOVE TDAA-LEC OF TDAACCT TO TDB-TDAA-LEC OF TDB-TDAACCT.\n038964     MOVE TDAA-BAL-AT-CLOSE OF TDAACCT TO TDB-TDAA-BAL-AT-CLOSE   \n038966         OF TDB-TDAACCT.\n038968     MOVE TDAA-AVL-CAP-INT OF TDAACCT TO TDB-TDAA-AVL-CAP-INT OF  \n038970         TDB-TDAACCT.\n038972     MOVE TDAA-FIDM-TR-FUND OF TDAACCT TO TDB-TDAA-FIDM-TR-FUND   \n038974         OF TDB-TDAACCT.\n038976     MOVE TDAA-IRS-FRM-DLVR OF TDAACCT TO TDB-TDAA-IRS-FRM-DLVR   \n038978         OF TDB-TDAACCT.\n038980     MOVE TDAA-PROVINCE OF TDAACCT TO TDB-TDAA-PROVINCE OF        \n038982         TDB-TDAACCT.\n038984     MOVE TDAA-PROMOTION OF TDAACCT TO TDB-TDAA-PROMOTION OF      \n038986         TDB-TDAACCT.\n038988     MOVE ZEROS TO WS-AGE OF WS-MINDIST.\n038990     MOVE ZEROS TO WS-SP-AGE OF WS-MINDIST.\n038992     MOVE ZEROS TO WS-AGE-COUNT OF WS-MINDIST.\n038994     MOVE ZEROS TO WS-MD-COUNT OF WS-MINDIST.\n038996     MOVE ZEROS TO WS-FACTOR OF WS-MINDIST.\n038998     MOVE ZEROS TO WS-MD-AGE-DIFF OF WS-MINDIST.\n039000     MOVE ZEROS TO WS-BNF-AGE OF WS-MINDIST.\n039002     MOVE ZEROS TO WS-MD-FMV OF WS-MINDIST.\n039004     MOVE ZEROS TO WS-MD-AGE OF WS-MINDIST.\n039006     MOVE ZEROS TO WS-MD-BN-AGE OF WS-MINDIST.\n039008     MOVE SPACES TO WS-MD-SPOUSE OF WS-MINDIST.\n039010     MOVE ZEROS TO WS-MD-AMT OF WS-MINDIST.\n039012     MOVE ZEROS TO WS-MD-TBL OF WS-MINDIST.\n039014     MOVE ZEROS TO WS-MD-FACT OF WS-MINDIST.\n039016     MOVE ZEROS TO WS-CUST-YAD OF WS-MINDIST.\n039018     MOVE ZEROS TO WS-NUM-YR-YAD OF WS-MINDIST.\n039020     IF ( TDB-TDAA-INHERIT-IRA = 0 ) AND ( TDB-TDAA-IRA-TYPE = 13 \n039022         OR 15 OR 17 )\n039024         NEXT SENTENCE ELSE\n039026         GO TO Z-5-23-1-ELSE.\n039028     MOVE 2 TO Z-EXIT-LEVEL\n039030     GO TO Z-5-14-END.\n039032 Z-5-23-1-ELSE.\n039034     IF TDB-TDAA-IRA-TYPE = 11 OR 16\n039036         NEXT SENTENCE ELSE\n039038         GO TO Z-5-23-2-ELSE.\n039040     MOVE 2 TO Z-EXIT-LEVEL\n039042     GO TO Z-5-14-END.\n039044 Z-5-23-2-ELSE.\n039046 Z-5-23-ENDIF.\n039048********* NEXT WHEN\n039050     IF TDB-TDAA-STATUS = \"C\"\n039052        NEXT SENTENCE\n039054     ELSE\n039056        GO TO Z-5-26-NEXT-SKIP.\n039058     MOVE 2 TO Z-EXIT-LEVEL\n039060     GO TO Z-5-14-END.\n039062 Z-5-26-NEXT-SKIP.\n039064     PERFORM Z-DATE-INITIALIZE-CTRL\n039066        THRU Z-DATE-INITIALIZE-CTRL-EXIT.\n039068     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.\n039070*    LOAD DATE REGISTER 1\n039072     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n039074     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n039076     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n039078     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n039080     MOVE Z-DATE-1 TO Z-DATE-2.\n039082     MOVE TDB-TDAC-BIRTH-DT TO Z-DATE2-FORMAT-9.\n039084*    LOAD DATE REGISTER 1\n039086     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n039088     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n039090     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n039092     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n039094     PERFORM Z-DATE-YY-DIFF THRU Z-DATE-YY-DIFF-EXIT.\n039096     MOVE Z-DATE-Y TO WS-MD-AGE.\n039098********* NEXT WHEN\n039100     IF ( TDB-TDAC-BIRTH-DT = ZEROS ) AND ( TDB-TDAA-INHERIT-IRA  \n039102         = 0 )\n039104        NEXT SENTENCE\n039106     ELSE\n039108        GO TO Z-5-28-NEXT-SKIP.\n039110     MOVE 2 TO Z-EXIT-LEVEL\n039112     GO TO Z-5-14-END.\n039114 Z-5-28-NEXT-SKIP.\n039116*\n039118     PERFORM Z-DATE-INITIALIZE-REGS\n039120         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n039122     PERFORM Z-DATE-INITIALIZE-CTRL\n039124        THRU Z-DATE-INITIALIZE-CTRL-EXIT.\n039126     MOVE TDB-TDAC-BIRTH-DT TO Z-DATE2-FORMAT-9.\n039128*    DATE UNIT INITIALIZATION\n039130     COMPUTE Z-DATE-Y = 73.\n039132*    LOAD DATE REGISTERS FOR CALCULATIONS\n039134*    LOAD DATE REGISTER 1\n039136     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n039138     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n039140     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n039142     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n039144     PERFORM Z-DATE-CALC-LEAP-YEAR\n039146        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n039148     PERFORM Z-DATE-MDY-TO-JUL-CTRL\n039150        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.\n039152     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.\n039154*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS\n039156     IF Z-DATE-Y NOT = ZEROS\n039158         PERFORM Z-DATE-CALC-Y\n039160            THRU Z-DATE-CALC-Y-EXIT.\n039162     IF Z-DATE-C NOT = ZEROS\n039164         PERFORM Z-DATE-CALC-C\n039166            THRU Z-DATE-CALC-C-EXIT.\n039168*    RE-ADJUST AFTER CALCULATIONS\n039170     PERFORM Z-DATE-CALC-LEAP-YEAR\n039172        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n039174     PERFORM Z-DATE-CALC-MONTH-DAYS\n039176        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.\n039178*    PLACE THE RESULTS WHERE THEY BELONG\n039180     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.\n039182     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.\n039184     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.\n039186     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.\n039188     MOVE Z-DATE2-FORMAT TO WS-RMD-DATE.\n039190     MOVE PROCESS-DATE TO WS-DATE-CCYYMMDD.\n039192     IF ( WS-RMD-DATE-CCYY > WS-DATE-CCYY ) AND (                 \n039194         TDB-TDAA-INHERIT-IRA = 0 )\n039196         NEXT SENTENCE ELSE\n039198         GO TO Z-5-31-1-ELSE.\n039200     MOVE 2 TO Z-EXIT-LEVEL\n039202     GO TO Z-5-14-END.\n039204 Z-5-31-1-ELSE.\n039206     MOVE ZERO TO WS-DSREC-FLAG.\n039208     IF ( TDB-TDAC-TIN-NBR NOT = WS-PREV-TIN ) AND ( WS-1ST-TIME  \n039210         = 1 )\n039212         NEXT SENTENCE ELSE\n039214         GO TO Z-5-34-1-ELSE.\n039216     IF ( SPECS-COMB-AUTO-RMD-ADJUST = \"Y\" )\n039218         NEXT SENTENCE ELSE\n039220         GO TO Z-5-35-1-ELSE.\n039222     MOVE 1 TO J.\n039224     COMPUTE Z-TO-1 = WS-TIN-DETAIL-MAX.\n039226 Z-5-36-LOOP.\n039228     IF J > Z-TO-1\n039230         GO TO Z-5-36-XIT.\n039232     MOVE 0 TO Z-EXIT-CODE.\n039234     MOVE 9999 TO Z-EXIT-LEVEL.\n039236********* EXIT WHEN\n039238     IF WS-TIN-DET-LINE-3 (J) = SPACES\n039240        NEXT SENTENCE\n039242     ELSE\n039244        GO TO Z-5-37-EXIT-SKIP.\n039246     MOVE 3 TO Z-EXIT-LEVEL.\n039248     MOVE 1 TO Z-EXIT-CODE.\n039250     GO TO Z-5-36-END.\n039252 Z-5-37-EXIT-SKIP.\n039254     MOVE SPACES TO RMDRPT-REC-3.\n039256     MOVE WS-TIN-DET-LINE-3 (J) TO RMDRPT-REC-3.\n039258     IF ( RMDRPT-DS-NTRVL-3 NOT = \"NONE\" ) AND ( RMDRPT-DS-FREQ-3 \n039260         NOT = \"I\" ) AND ( WS-TIN-DISTR-RECS = 1 )\n039262         NEXT SENTENCE ELSE\n039264         GO TO Z-5-40-1-ELSE.\n039266     IF WS-TIN-DET-DIST-FREQ (J) = \"D\"\n039268         NEXT SENTENCE ELSE\n039270         GO TO Z-5-41-1-ELSE.\n039272     COMPUTE RMDRPT-NEW-DS-AMT-3 ROUNDED = ( ( WS-TIN-RMD-TOT /   \n039274         365 ) * WS-TIN-DET-DS-NTRVL (J) ) .\n039276\n039278     GO TO Z-5-41-ENDIF.\n039280 Z-5-41-1-ELSE.\n039282     IF WS-TIN-DET-DIST-FREQ (J) = \"M\"\n039284         NEXT SENTENCE ELSE\n039286         GO TO Z-5-41-2-ELSE.\n039288     COMPUTE RMDRPT-NEW-DS-AMT-3 ROUNDED = ( ( WS-TIN-RMD-TOT /   \n039290         12 ) * WS-TIN-DET-DS-NTRVL (J) ) .\n039292\n039294     GO TO Z-5-41-ENDIF.\n039296 Z-5-41-2-ELSE.\n039298     COMPUTE RMDRPT-NEW-DS-AMT-3 = WS-TIN-RMD-TOT .\n039300\n039302 Z-5-41-ENDIF.\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    420 lines from 19228 to 19647.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 40, "total_chunks": 55, "start_line": 19228, "end_line": 19647, "line_count": 420}

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
- Source code length: 24462 characters

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
CHUNK 40 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 19228 to 19647 (420 lines)
Chunk Tokens (estimated): ~7,818
Actual Input Tokens: 9,224 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 19228-19647 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 40 of 55 chunks
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
      The source code below is only CHUNK 40 of 55.


=============================================================================
CHUNK 40 SOURCE CODE (Lines 19228-19647)
=============================================================================

```cobol
038464         TDB-TDAACCT.
038466     MOVE TDAA-ACCR-DT OF TDAACCT TO TDB-TDAA-ACCR-DT OF          
038468         TDB-TDAACCT.
038470     MOVE TDAA-OPEN-DT OF TDAACCT TO TDB-TDAA-OPEN-DT OF          
038472         TDB-TDAACCT.
038474     MOVE TDAA-CLSD-DT OF TDAACCT TO TDB-TDAA-CLSD-DT OF          
038476         TDB-TDAACCT.
038478     MOVE TDAA-LST-MAT-DT OF TDAACCT TO TDB-TDAA-LST-MAT-DT OF    
038480         TDB-TDAACCT.
038482     MOVE TDAA-LST-POST-DT OF TDAACCT TO TDB-TDAA-LST-POST-DT OF  
038484         TDB-TDAACCT.
038486     MOVE TDAA-LST-IN-PROC OF TDAACCT TO TDB-TDAA-LST-IN-PROC OF  
038488         TDB-TDAACCT.
038490     MOVE TDAA-LST-CONTACT OF TDAACCT TO TDB-TDAA-LST-CONTACT OF  
038492         TDB-TDAACCT.
038494     MOVE TDAA-LST-FEE-DT OF TDAACCT TO TDB-TDAA-LST-FEE-DT OF    
038496         TDB-TDAACCT.
038498     MOVE TDAA-LST-RTCHG-DT OF TDAACCT TO TDB-TDAA-LST-RTCHG-DT   
038500         OF TDB-TDAACCT.
038502     MOVE TDAA-LST-DIST-DT OF TDAACCT TO TDB-TDAA-LST-DIST-DT OF  
038504         TDB-TDAACCT.
038506     MOVE TDAA-LST-STMT-DT OF TDAACCT TO TDB-TDAA-LST-STMT-DT OF  
038508         TDB-TDAACCT.
038510     MOVE TDAA-LST-CMPD-DT OF TDAACCT TO TDB-TDAA-LST-CMPD-DT OF  
038512         TDB-TDAACCT.
038514     MOVE 1 TO Z-II.
038516 Z-5-21-2-LOOP.
038518     IF Z-II > 10
038520         GO TO Z-5-21-2-LOOP-XIT.
038522     MOVE TDAA-RR-CYC-DT OF TDAACCT (Z-II) TO TDB-TDAA-RR-CYC-DT  
038524         OF TDB-TDAACCT (Z-II).
038526     ADD 1 TO Z-II.
038528     GO TO Z-5-21-2-LOOP.
038530 Z-5-21-2-LOOP-XIT.
038532     MOVE TDAA-BNF-BIRTH-DT OF TDAACCT TO TDB-TDAA-BNF-BIRTH-DT   
038534         OF TDB-TDAACCT.
038536     MOVE TDAA-BNF-DEATH-DT OF TDAACCT TO TDB-TDAA-BNF-DEATH-DT   
038538         OF TDB-TDAACCT.
038540     MOVE TDAA-LUPD-DATE OF TDAACCT TO TDB-TDAA-LUPD-DATE OF      
038542         TDB-TDAACCT.
038544     MOVE TDAA-LUPD-TIME OF TDAACCT TO TDB-TDAA-LUPD-TIME OF      
038546         TDB-TDAACCT.
038548     MOVE TDAA-ADD-DT OF TDAACCT TO TDB-TDAA-ADD-DT OF            
038550         TDB-TDAACCT.
038552     MOVE TDAA-ADD-TM OF TDAACCT TO TDB-TDAA-ADD-TM OF            
038554         TDB-TDAACCT.
038556     MOVE TDAA-CONV-DT OF TDAACCT TO TDB-TDAA-CONV-DT OF          
038558         TDB-TDAACCT.
038560     MOVE TDAA-ACT-CLOSE-DT OF TDAACCT TO TDB-TDAA-ACT-CLOSE-DT   
038562         OF TDB-TDAACCT.
038564     MOVE TDAA-LST-TBACT-DT OF TDAACCT TO TDB-TDAA-LST-TBACT-DT   
038566         OF TDB-TDAACCT.
038568     MOVE TDAA-ALERT-EXP-DT OF TDAACCT TO TDB-TDAA-ALERT-EXP-DT   
038570         OF TDB-TDAACCT.
038572     MOVE TDAA-ALRT2-EXP-DT OF TDAACCT TO TDB-TDAA-ALRT2-EXP-DT   
038574         OF TDB-TDAACCT.
038576     MOVE TDAA-ALRT3-EXP-DT OF TDAACCT TO TDB-TDAA-ALRT3-EXP-DT   
038578         OF TDB-TDAACCT.
038580     MOVE TDAA-NXT-FEE-DT OF TDAACCT TO TDB-TDAA-NXT-FEE-DT OF    
038582         TDB-TDAACCT.
038584     MOVE TDAA-NXT-POST-DT OF TDAACCT TO TDB-TDAA-NXT-POST-DT OF  
038586         TDB-TDAACCT.
038588     MOVE TDAA-NXT-MAT-DT OF TDAACCT TO TDB-TDAA-NXT-MAT-DT OF    
038590         TDB-TDAACCT.
038592     MOVE TDAA-NXT-DIST-DT OF TDAACCT TO TDB-TDAA-NXT-DIST-DT OF  
038594         TDB-TDAACCT.
038596     MOVE TDAA-NXT-RT-CHG OF TDAACCT TO TDB-TDAA-NXT-RT-CHG OF    
038598         TDB-TDAACCT.
038600     MOVE TDAA-NXT-IN-PROC OF TDAACCT TO TDB-TDAA-NXT-IN-PROC OF  
038602         TDB-TDAACCT.
038604     MOVE TDAA-NXT-CMPD-DT OF TDAACCT TO TDB-TDAA-NXT-CMPD-DT OF  
038606         TDB-TDAACCT.
038608     MOVE TDAA-NXT-STMT-DT OF TDAACCT TO TDB-TDAA-NXT-STMT-DT OF  
038610         TDB-TDAACCT.
038612     MOVE TDAA-NXT-DS-PROC OF TDAACCT TO TDB-TDAA-NXT-DS-PROC OF  
038614         TDB-TDAACCT.
038616     MOVE TDAA-ADV-NTC-DT OF TDAACCT TO TDB-TDAA-ADV-NTC-DT OF    
038618         TDB-TDAACCT.
038620     MOVE TDAA-NXT-29YR-DT OF TDAACCT TO TDB-TDAA-NXT-29YR-DT OF  
038622         TDB-TDAACCT.
038624     MOVE TDAA-FAIR-MRKT-DT OF TDAACCT TO TDB-TDAA-FAIR-MRKT-DT   
038626         OF TDB-TDAACCT.
038628     MOVE TDAA-SORT-FIELD-1 OF TDAACCT TO TDB-TDAA-SORT-FIELD-1   
038630         OF TDB-TDAACCT.
038632     MOVE TDAA-SORT-FIELD-2 OF TDAACCT TO TDB-TDAA-SORT-FIELD-2   
038634         OF TDB-TDAACCT.
038636     MOVE TDAA-SORT-FIELD-3 OF TDAACCT TO TDB-TDAA-SORT-FIELD-3   
038638         OF TDB-TDAACCT.
038640     MOVE TDAA-SORT-FIELD-4 OF TDAACCT TO TDB-TDAA-SORT-FIELD-4   
038642         OF TDB-TDAACCT.
038644     MOVE TDAA-CMAT-PUB-ID OF TDAACCT TO TDB-TDAA-CMAT-PUB-ID OF  
038646         TDB-TDAACCT.
038648     MOVE TDAA-MSA-CONTR OF TDAACCT TO TDB-TDAA-MSA-CONTR OF      
038650         TDB-TDAACCT.
038652     MOVE TDAA-MSA-CONTR-LY OF TDAACCT TO TDB-TDAA-MSA-CONTR-LY   
038654         OF TDB-TDAACCT.
038656     MOVE TDAA-AVG-ACCR-INT OF TDAACCT TO TDB-TDAA-AVG-ACCR-INT   
038658         OF TDB-TDAACCT.
038660     MOVE TDAA-LEVEL-PAY OF TDAACCT TO TDB-TDAA-LEVEL-PAY OF      
038662         TDB-TDAACCT.
038664     MOVE TDAA-ST-INT-CD OF TDAACCT TO TDB-TDAA-ST-INT-CD OF      
038666         TDB-TDAACCT.
038668     MOVE TDAA-ST-WHLD-CD OF TDAACCT TO TDB-TDAA-ST-WHLD-CD OF    
038670         TDB-TDAACCT.
038672     MOVE TDAA-ST-WHLD-AMT OF TDAACCT TO TDB-TDAA-ST-WHLD-AMT OF  
038674         TDB-TDAACCT.
038676     MOVE TDAA-ST-CUR-W-AMT OF TDAACCT TO TDB-TDAA-ST-CUR-W-AMT   
038678         OF TDB-TDAACCT.
038680     MOVE TDAA-ST-LST-W-AMT OF TDAACCT TO TDB-TDAA-ST-LST-W-AMT   
038682         OF TDB-TDAACCT.
038684     MOVE TDAA-ST-WHLD-STD OF TDAACCT TO TDB-TDAA-ST-WHLD-STD OF  
038686         TDB-TDAACCT.
038688     MOVE TDAA-ST-WHLD-YTD OF TDAACCT TO TDB-TDAA-ST-WHLD-YTD OF  
038690         TDB-TDAACCT.
038692     MOVE TDAA-CIF-REMARK OF TDAACCT TO TDB-TDAA-CIF-REMARK OF    
038694         TDB-TDAACCT.
038696     MOVE TDAA-CSR OF TDAACCT TO TDB-TDAA-CSR OF TDB-TDAACCT.
038698     MOVE TDAA-BSA-O-RSK-CD OF TDAACCT TO TDB-TDAA-BSA-O-RSK-CD   
038700         OF TDB-TDAACCT.
038702     MOVE TDAA-BSA-C-RSK-CD OF TDAACCT TO TDB-TDAA-BSA-C-RSK-CD   
038704         OF TDB-TDAACCT.
038706     MOVE TDAA-LRG-TRX-DT OF TDAACCT TO TDB-TDAA-LRG-TRX-DT OF    
038708         TDB-TDAACCT.
038710     MOVE TDAA-HSA-FMLY-IND OF TDAACCT TO TDB-TDAA-HSA-FMLY-IND   
038712         OF TDB-TDAACCT.
038714     MOVE TDAA-STOP-PAY-IND OF TDAACCT TO TDB-TDAA-STOP-PAY-IND   
038716         OF TDB-TDAACCT.
038718     MOVE TDAA-IMG-PG-TYPE OF TDAACCT TO TDB-TDAA-IMG-PG-TYPE OF  
038720         TDB-TDAACCT.
038722     MOVE TDAA-CONT-LMT-CLC OF TDAACCT TO TDB-TDAA-CONT-LMT-CLC   
038724         OF TDB-TDAACCT.
038726     MOVE TDAA-CONT-LMT-ENT OF TDAACCT TO TDB-TDAA-CONT-LMT-ENT   
038728         OF TDB-TDAACCT.
038730     MOVE TDAA-MEMO-DB OF TDAACCT TO TDB-TDAA-MEMO-DB OF          
038732         TDB-TDAACCT.
038734     MOVE TDAA-MEMO-CR OF TDAACCT TO TDB-TDAA-MEMO-CR OF          
038736         TDB-TDAACCT.
038738     MOVE TDAA-MEMO-DB-2 OF TDAACCT TO TDB-TDAA-MEMO-DB-2 OF      
038740         TDB-TDAACCT.
038742     MOVE TDAA-MEMO-CR-2 OF TDAACCT TO TDB-TDAA-MEMO-CR-2 OF      
038744         TDB-TDAACCT.
038746     MOVE TDAA-RT-AT-CONV OF TDAACCT TO TDB-TDAA-RT-AT-CONV OF    
038748         TDB-TDAACCT.
038750     MOVE TDAA-ACCR-AT-CONV OF TDAACCT TO TDB-TDAA-ACCR-AT-CONV   
038752         OF TDB-TDAACCT.
038754     MOVE TDAA-RT-AT-ACRDT OF TDAACCT TO TDB-TDAA-RT-AT-ACRDT OF  
038756         TDB-TDAACCT.
038758     MOVE TDAA-BAL-AT-ACRDT OF TDAACCT TO TDB-TDAA-BAL-AT-ACRDT   
038760         OF TDB-TDAACCT.
038762     MOVE TDAA-ZERO-RT-ALLOW OF TDAACCT TO TDB-TDAA-ZERO-RT-ALLOW 
038764         OF TDB-TDAACCT.
038766     MOVE TDAA-EMAIL-NTC OF TDAACCT TO TDB-TDAA-EMAIL-NTC OF      
038768         TDB-TDAACCT.
038770     MOVE TDAA-EMAIL-STMT OF TDAACCT TO TDB-TDAA-EMAIL-STMT OF    
038772         TDB-TDAACCT.
038774     MOVE TDAA-FRAUD-CK-DT OF TDAACCT TO TDB-TDAA-FRAUD-CK-DT OF  
038776         TDB-TDAACCT.
038778     MOVE TDAA-FRAUD-CK-CNT OF TDAACCT TO TDB-TDAA-FRAUD-CK-CNT   
038780         OF TDB-TDAACCT.
038782     MOVE TDAA-FRAUD-CK-AMT OF TDAACCT TO TDB-TDAA-FRAUD-CK-AMT   
038784         OF TDB-TDAACCT.
038786     MOVE TDAA-MISC-ACCTNO OF TDAACCT TO TDB-TDAA-MISC-ACCTNO OF  
038788         TDB-TDAACCT.
038790     MOVE TDAA-RMD-MAN-CALC OF TDAACCT TO TDB-TDAA-RMD-MAN-CALC   
038792         OF TDB-TDAACCT.
038794     MOVE TDAA-RMD-AMOUNT OF TDAACCT TO TDB-TDAA-RMD-AMOUNT OF    
038796         TDB-TDAACCT.
038798     MOVE TDAA-BROKERAGE-ID OF TDAACCT TO TDB-TDAA-BROKERAGE-ID   
038800         OF TDB-TDAACCT.
038802     MOVE TDAA-EV-LARGE-TRX OF TDAACCT TO TDB-TDAA-EV-LARGE-TRX   
038804         OF TDB-TDAACCT.
038806     MOVE TDAA-EV-MAT-AMT OF TDAACCT TO TDB-TDAA-EV-MAT-AMT OF    
038808         TDB-TDAACCT.
038810     MOVE TDAA-EV-DISP-ACCT OF TDAACCT TO TDB-TDAA-EV-DISP-ACCT   
038812         OF TDB-TDAACCT.
038814     MOVE TDAA-EV-COMP-ACCT OF TDAACCT TO TDB-TDAA-EV-COMP-ACCT   
038816         OF TDB-TDAACCT.
038818     MOVE TDAA-EV-PUBLIC-ID OF TDAACCT TO TDB-TDAA-EV-PUBLIC-ID   
038820         OF TDB-TDAACCT.
038822     MOVE TDAA-EV-MAT-TYPE OF TDAACCT TO TDB-TDAA-EV-MAT-TYPE OF  
038824         TDB-TDAACCT.
038826     MOVE TDAA-EV-INT-TYPE OF TDAACCT TO TDB-TDAA-EV-INT-TYPE OF  
038828         TDB-TDAACCT.
038830     MOVE TDAA-EV-ACCT-TYP OF TDAACCT TO TDB-TDAA-EV-ACCT-TYP OF  
038832         TDB-TDAACCT.
038834     MOVE TDAA-EV-WHLD-PCT OF TDAACCT TO TDB-TDAA-EV-WHLD-PCT OF  
038836         TDB-TDAACCT.
038838     MOVE TDAA-EV-NON-ACCR OF TDAACCT TO TDB-TDAA-EV-NON-ACCR OF  
038840         TDB-TDAACCT.
038842     MOVE TDAA-EV-CLOSED OF TDAACCT TO TDB-TDAA-EV-CLOSED OF      
038844         TDB-TDAACCT.
038846     MOVE TDAA-EV-CLOSE-MO OF TDAACCT TO TDB-TDAA-EV-CLOSE-MO OF  
038848         TDB-TDAACCT.
038850     MOVE TDAA-EV-OPEN-MO OF TDAACCT TO TDB-TDAA-EV-OPEN-MO OF    
038852         TDB-TDAACCT.
038854     MOVE TDAA-EV-ANN-INT OF TDAACCT TO TDB-TDAA-EV-ANN-INT OF    
038856         TDB-TDAACCT.
038858     MOVE TDAA-EV-ORIG-RT OF TDAACCT TO TDB-TDAA-EV-ORIG-RT OF    
038860         TDB-TDAACCT.
038862     MOVE TDAA-EV-DLY-INT OF TDAACCT TO TDB-TDAA-EV-DLY-INT OF    
038864         TDB-TDAACCT.
038866     MOVE TDAA-EV-INT-PAY OF TDAACCT TO TDB-TDAA-EV-INT-PAY OF    
038868         TDB-TDAACCT.
038870     MOVE TDAA-EV-AVAIL-BL OF TDAACCT TO TDB-TDAA-EV-AVAIL-BL OF  
038872         TDB-TDAACCT.
038874     MOVE TDAA-EV-RETAIN OF TDAACCT TO TDB-TDAA-EV-RETAIN OF      
038876         TDB-TDAACCT.
038878     MOVE TDAA-EV-CL-RETAIN OF TDAACCT TO TDB-TDAA-EV-CL-RETAIN   
038880         OF TDB-TDAACCT.
038882     MOVE TDAA-EV-TIMES-REN OF TDAACCT TO TDB-TDAA-EV-TIMES-REN   
038884         OF TDB-TDAACCT.
038886     MOVE TDAA-EV-CURR-BAL OF TDAACCT TO TDB-TDAA-EV-CURR-BAL OF  
038888         TDB-TDAACCT.
038890     MOVE TDAA-MONY-SRC-CD2 OF TDAACCT TO TDB-TDAA-MONY-SRC-CD2   
038892         OF TDB-TDAACCT.
038894     MOVE TDAA-INHERIT-IRA OF TDAACCT TO TDB-TDAA-INHERIT-IRA OF  
038896         TDB-TDAACCT.
038898     MOVE TDAA-LIFE-FACTOR OF TDAACCT TO TDB-TDAA-LIFE-FACTOR OF  
038900         TDB-TDAACCT.
038902     MOVE TDAA-BRKR-DEP-CAT OF TDAACCT TO TDB-TDAA-BRKR-DEP-CAT   
038904         OF TDB-TDAACCT.
038906     MOVE TDAA-LINE-OF-BUS OF TDAACCT TO TDB-TDAA-LINE-OF-BUS OF  
038908         TDB-TDAACCT.
038910     MOVE TDAA-1ST-STMT OF TDAACCT TO TDB-TDAA-1ST-STMT OF        
038912         TDB-TDAACCT.
038914     MOVE TDAA-POSTAL-CITY OF TDAACCT TO TDB-TDAA-POSTAL-CITY OF  
038916         TDB-TDAACCT.
038918     MOVE TDAA-POSTAL-CNTRY OF TDAACCT TO TDB-TDAA-POSTAL-CNTRY   
038920         OF TDB-TDAACCT.
038922     MOVE TDAA-CITIZN-CNTRY OF TDAACCT TO TDB-TDAA-CITIZN-CNTRY   
038924         OF TDB-TDAACCT.
038926     MOVE TDAA-CUSTM-FIELDS OF TDAACCT TO TDB-TDAA-CUSTM-FIELDS   
038928         OF TDB-TDAACCT.
038930     MOVE TDAA-AVG-STEP-RT OF TDAACCT TO TDB-TDAA-AVG-STEP-RT OF  
038932         TDB-TDAACCT.
038934     MOVE TDAA-MONITOR-INQ OF TDAACCT TO TDB-TDAA-MONITOR-INQ OF  
038936         TDB-TDAACCT.
038938     MOVE TDAA-IGL-GRP-2 OF TDAACCT TO TDB-TDAA-IGL-GRP-2 OF      
038940         TDB-TDAACCT.
038942     MOVE TDAA-AGG-DAYS-QTD OF TDAACCT TO TDB-TDAA-AGG-DAYS-QTD   
038944         OF TDB-TDAACCT.
038946     MOVE TDAA-AGG-BAL-QTD OF TDAACCT TO TDB-TDAA-AGG-BAL-QTD OF  
038948         TDB-TDAACCT.
038950     MOVE TDAA-IGL-GRP-3 OF TDAACCT TO TDB-TDAA-IGL-GRP-3 OF      
038952         TDB-TDAACCT.
038954     MOVE TDAA-ALT-ADDR-EOY OF TDAACCT TO TDB-TDAA-ALT-ADDR-EOY   
038956         OF TDB-TDAACCT.
038958     MOVE TDAA-1042S-TAX-ID OF TDAACCT TO TDB-TDAA-1042S-TAX-ID   
038960         OF TDB-TDAACCT.
038962     MOVE TDAA-LEC OF TDAACCT TO TDB-TDAA-LEC OF TDB-TDAACCT.
038964     MOVE TDAA-BAL-AT-CLOSE OF TDAACCT TO TDB-TDAA-BAL-AT-CLOSE   
038966         OF TDB-TDAACCT.
038968     MOVE TDAA-AVL-CAP-INT OF TDAACCT TO TDB-TDAA-AVL-CAP-INT OF  
038970         TDB-TDAACCT.
038972     MOVE TDAA-FIDM-TR-FUND OF TDAACCT TO TDB-TDAA-FIDM-TR-FUND   
038974         OF TDB-TDAACCT.
038976     MOVE TDAA-IRS-FRM-DLVR OF TDAACCT TO TDB-TDAA-IRS-FRM-DLVR   
038978         OF TDB-TDAACCT.
038980     MOVE TDAA-PROVINCE OF TDAACCT TO TDB-TDAA-PROVINCE OF        
038982         TDB-TDAACCT.
038984     MOVE TDAA-PROMOTION OF TDAACCT TO TDB-TDAA-PROMOTION OF      
038986         TDB-TDAACCT.
038988     MOVE ZEROS TO WS-AGE OF WS-MINDIST.
038990     MOVE ZEROS TO WS-SP-AGE OF WS-MINDIST.
038992     MOVE ZEROS TO WS-AGE-COUNT OF WS-MINDIST.
038994     MOVE ZEROS TO WS-MD-COUNT OF WS-MINDIST.
038996     MOVE ZEROS TO WS-FACTOR OF WS-MINDIST.
038998     MOVE ZEROS TO WS-MD-AGE-DIFF OF WS-MINDIST.
039000     MOVE ZEROS TO WS-BNF-AGE OF WS-MINDIST.
039002     MOVE ZEROS TO WS-MD-FMV OF WS-MINDIST.
039004     MOVE ZEROS TO WS-MD-AGE OF WS-MINDIST.
039006     MOVE ZEROS TO WS-MD-BN-AGE OF WS-MINDIST.
039008     MOVE SPACES TO WS-MD-SPOUSE OF WS-MINDIST.
039010     MOVE ZEROS TO WS-MD-AMT OF WS-MINDIST.
039012     MOVE ZEROS TO WS-MD-TBL OF WS-MINDIST.
039014     MOVE ZEROS TO WS-MD-FACT OF WS-MINDIST.
039016     MOVE ZEROS TO WS-CUST-YAD OF WS-MINDIST.
039018     MOVE ZEROS TO WS-NUM-YR-YAD OF WS-MINDIST.
039020     IF ( TDB-TDAA-INHERIT-IRA = 0 ) AND ( TDB-TDAA-IRA-TYPE = 13 
039022         OR 15 OR 17 )
039024         NEXT SENTENCE ELSE
039026         GO TO Z-5-23-1-ELSE.
039028     MOVE 2 TO Z-EXIT-LEVEL
039030     GO TO Z-5-14-END.
039032 Z-5-23-1-ELSE.
039034     IF TDB-TDAA-IRA-TYPE = 11 OR 16
039036         NEXT SENTENCE ELSE
039038         GO TO Z-5-23-2-ELSE.
039040     MOVE 2 TO Z-EXIT-LEVEL
039042     GO TO Z-5-14-END.
039044 Z-5-23-2-ELSE.
039046 Z-5-23-ENDIF.
039048********* NEXT WHEN
039050     IF TDB-TDAA-STATUS = "C"
039052        NEXT SENTENCE
039054     ELSE
039056        GO TO Z-5-26-NEXT-SKIP.
039058     MOVE 2 TO Z-EXIT-LEVEL
039060     GO TO Z-5-14-END.
039062 Z-5-26-NEXT-SKIP.
039064     PERFORM Z-DATE-INITIALIZE-CTRL
039066        THRU Z-DATE-INITIALIZE-CTRL-EXIT.
039068     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.
039070*    LOAD DATE REGISTER 1
039072     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
039074     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
039076     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
039078     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
039080     MOVE Z-DATE-1 TO Z-DATE-2.
039082     MOVE TDB-TDAC-BIRTH-DT TO Z-DATE2-FORMAT-9.
039084*    LOAD DATE REGISTER 1
039086     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
039088     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
039090     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
039092     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
039094     PERFORM Z-DATE-YY-DIFF THRU Z-DATE-YY-DIFF-EXIT.
039096     MOVE Z-DATE-Y TO WS-MD-AGE.
039098********* NEXT WHEN
039100     IF ( TDB-TDAC-BIRTH-DT = ZEROS ) AND ( TDB-TDAA-INHERIT-IRA  
039102         = 0 )
039104        NEXT SENTENCE
039106     ELSE
039108        GO TO Z-5-28-NEXT-SKIP.
039110     MOVE 2 TO Z-EXIT-LEVEL
039112     GO TO Z-5-14-END.
039114 Z-5-28-NEXT-SKIP.
039116*
039118     PERFORM Z-DATE-INITIALIZE-REGS
039120         THRU Z-DATE-INITIALIZE-REGS-EXIT.
039122     PERFORM Z-DATE-INITIALIZE-CTRL
039124        THRU Z-DATE-INITIALIZE-CTRL-EXIT.
039126     MOVE TDB-TDAC-BIRTH-DT TO Z-DATE2-FORMAT-9.
039128*    DATE UNIT INITIALIZATION
039130     COMPUTE Z-DATE-Y = 73.
039132*    LOAD DATE REGISTERS FOR CALCULATIONS
039134*    LOAD DATE REGISTER 1
039136     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
039138     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
039140     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
039142     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
039144     PERFORM Z-DATE-CALC-LEAP-YEAR
039146        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
039148     PERFORM Z-DATE-MDY-TO-JUL-CTRL
039150        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.
039152     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.
039154*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS
039156     IF Z-DATE-Y NOT = ZEROS
039158         PERFORM Z-DATE-CALC-Y
039160            THRU Z-DATE-CALC-Y-EXIT.
039162     IF Z-DATE-C NOT = ZEROS
039164         PERFORM Z-DATE-CALC-C
039166            THRU Z-DATE-CALC-C-EXIT.
039168*    RE-ADJUST AFTER CALCULATIONS
039170     PERFORM Z-DATE-CALC-LEAP-YEAR
039172        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
039174     PERFORM Z-DATE-CALC-MONTH-DAYS
039176        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.
039178*    PLACE THE RESULTS WHERE THEY BELONG
039180     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.
039182     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.
039184     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.
039186     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.
039188     MOVE Z-DATE2-FORMAT TO WS-RMD-DATE.
039190     MOVE PROCESS-DATE TO WS-DATE-CCYYMMDD.
039192     IF ( WS-RMD-DATE-CCYY > WS-DATE-CCYY ) AND (                 
039194         TDB-TDAA-INHERIT-IRA = 0 )
039196         NEXT SENTENCE ELSE
039198         GO TO Z-5-31-1-ELSE.
039200     MOVE 2 TO Z-EXIT-LEVEL
039202     GO TO Z-5-14-END.
039204 Z-5-31-1-ELSE.
039206     MOVE ZERO TO WS-DSREC-FLAG.
039208     IF ( TDB-TDAC-TIN-NBR NOT = WS-PREV-TIN ) AND ( WS-1ST-TIME  
039210         = 1 )
039212         NEXT SENTENCE ELSE
039214         GO TO Z-5-34-1-ELSE.
039216     IF ( SPECS-COMB-AUTO-RMD-ADJUST = "Y" )
039218         NEXT SENTENCE ELSE
039220         GO TO Z-5-35-1-ELSE.
039222     MOVE 1 TO J.
039224     COMPUTE Z-TO-1 = WS-TIN-DETAIL-MAX.
039226 Z-5-36-LOOP.
039228     IF J > Z-TO-1
039230         GO TO Z-5-36-XIT.
039232     MOVE 0 TO Z-EXIT-CODE.
039234     MOVE 9999 TO Z-EXIT-LEVEL.
039236********* EXIT WHEN
039238     IF WS-TIN-DET-LINE-3 (J) = SPACES
039240        NEXT SENTENCE
039242     ELSE
039244        GO TO Z-5-37-EXIT-SKIP.
039246     MOVE 3 TO Z-EXIT-LEVEL.
039248     MOVE 1 TO Z-EXIT-CODE.
039250     GO TO Z-5-36-END.
039252 Z-5-37-EXIT-SKIP.
039254     MOVE SPACES TO RMDRPT-REC-3.
039256     MOVE WS-TIN-DET-LINE-3 (J) TO RMDRPT-REC-3.
039258     IF ( RMDRPT-DS-NTRVL-3 NOT = "NONE" ) AND ( RMDRPT-DS-FREQ-3 
039260         NOT = "I" ) AND ( WS-TIN-DISTR-RECS = 1 )
039262         NEXT SENTENCE ELSE
039264         GO TO Z-5-40-1-ELSE.
039266     IF WS-TIN-DET-DIST-FREQ (J) = "D"
039268         NEXT SENTENCE ELSE
039270         GO TO Z-5-41-1-ELSE.
039272     COMPUTE RMDRPT-NEW-DS-AMT-3 ROUNDED = ( ( WS-TIN-RMD-TOT /   
039274         365 ) * WS-TIN-DET-DS-NTRVL (J) ) .
039276
039278     GO TO Z-5-41-ENDIF.
039280 Z-5-41-1-ELSE.
039282     IF WS-TIN-DET-DIST-FREQ (J) = "M"
039284         NEXT SENTENCE ELSE
039286         GO TO Z-5-41-2-ELSE.
039288     COMPUTE RMDRPT-NEW-DS-AMT-3 ROUNDED = ( ( WS-TIN-RMD-TOT /   
039290         12 ) * WS-TIN-DET-DS-NTRVL (J) ) .
039292
039294     GO TO Z-5-41-ENDIF.
039296 Z-5-41-2-ELSE.
039298     COMPUTE RMDRPT-NEW-DS-AMT-3 = WS-TIN-RMD-TOT .
039300
039302 Z-5-41-ENDIF.
```

⚠️  This is the source code you must document.
    420 lines from 19228 to 19647.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

