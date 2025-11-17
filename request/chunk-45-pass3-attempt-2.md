# LLM Request Debug File
Generated: 2025-11-14T19:35:58.981055

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 45/55
- **Model**: gpt-4.1
- **Chunk Number**: 45
- **Pass Number**: 3
- **Attempt Number**: 2 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~6,997 tokens
- **Total Input**: ~8,955 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 45/55" (ID: detailed-code-explanation)

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


**CHUNK 45 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-14T17:36:35.036798", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 45 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 21726 to 22122 (397 lines)\nChunk Tokens (estimated): ~8,094\nActual Input Tokens: 9,500 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 21726-22122 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 45 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 45 of 55.\n\n\n=============================================================================\nCHUNK 45 SOURCE CODE (Lines 21726-22122)\n=============================================================================\n\n```cobol\n043460         TDB-TDAACCT.\n043462     MOVE TDAA-DDA-ACCT-1 OF TDAACCT TO TDB-TDAA-DDA-ACCT-1 OF    \n043464         TDB-TDAACCT.\n043466     MOVE TDAA-DDA-ACCT-1-S OF TDAACCT TO TDB-TDAA-DDA-ACCT-1-S   \n043468         OF TDB-TDAACCT.\n043470     MOVE TDAA-DDA-ACCT-2 OF TDAACCT TO TDB-TDAA-DDA-ACCT-2 OF    \n043472         TDB-TDAACCT.\n043474     MOVE TDAA-DDA-ACCT-2-S OF TDAACCT TO TDB-TDAA-DDA-ACCT-2-S   \n043476         OF TDB-TDAACCT.\n043478     MOVE TDAA-DDA-ACCT-3 OF TDAACCT TO TDB-TDAA-DDA-ACCT-3 OF    \n043480         TDB-TDAACCT.\n043482     MOVE TDAA-DDA-ACCT-3-S OF TDAACCT TO TDB-TDAA-DDA-ACCT-3-S   \n043484         OF TDB-TDAACCT.\n043486     MOVE TDAA-INT-ACCT OF TDAACCT TO TDB-TDAA-INT-ACCT OF        \n043488         TDB-TDAACCT.\n043490     MOVE TDAA-INT-ACCT-S OF TDAACCT TO TDB-TDAA-INT-ACCT-S OF    \n043492         TDB-TDAACCT.\n043494     MOVE TDAA-CS-ACCT OF TDAACCT TO TDB-TDAA-CS-ACCT OF          \n043496         TDB-TDAACCT.\n043498     MOVE TDAA-CS-ACCT-S OF TDAACCT TO TDB-TDAA-CS-ACCT-S OF      \n043500         TDB-TDAACCT.\n043502     MOVE TDAA-CC-ACCT OF TDAACCT TO TDB-TDAA-CC-ACCT OF          \n043504         TDB-TDAACCT.\n043506     MOVE TDAA-LNS-BORROWER OF TDAACCT TO TDB-TDAA-LNS-BORROWER   \n043508         OF TDB-TDAACCT.\n043510     MOVE TDAA-LNS-NOTE OF TDAACCT TO TDB-TDAA-LNS-NOTE OF        \n043512         TDB-TDAACCT.\n043514     MOVE TDAA-CNV-OLD-ACCT OF TDAACCT TO TDB-TDAA-CNV-OLD-ACCT   \n043516         OF TDB-TDAACCT.\n043518     MOVE TDAA-CLS-ACCT OF TDAACCT TO TDB-TDAA-CLS-ACCT OF        \n043520         TDB-TDAACCT.\n043522     MOVE TDAA-CLS-ACCT-S OF TDAACCT TO TDB-TDAA-CLS-ACCT-S OF    \n043524         TDB-TDAACCT.\n043526     MOVE TDAA-DAYS-IN-PER OF TDAACCT TO TDB-TDAA-DAYS-IN-PER OF  \n043528         TDB-TDAACCT.\n043530     MOVE TDAA-RR-CYC-NBR OF TDAACCT TO TDB-TDAA-RR-CYC-NBR OF    \n043532         TDB-TDAACCT.\n043534     MOVE TDAA-CR-CNT-STD OF TDAACCT TO TDB-TDAA-CR-CNT-STD OF    \n043536         TDB-TDAACCT.\n043538     MOVE TDAA-CR-AMT-STD OF TDAACCT TO TDB-TDAA-CR-AMT-STD OF    \n043540         TDB-TDAACCT.\n043542     MOVE TDAA-DB-CNT-STD OF TDAACCT TO TDB-TDAA-DB-CNT-STD OF    \n043544         TDB-TDAACCT.\n043546     MOVE TDAA-DB-AMT-STD OF TDAACCT TO TDB-TDAA-DB-AMT-STD OF    \n043548         TDB-TDAACCT.\n043550     MOVE TDAA-CR-CNT-YTD OF TDAACCT TO TDB-TDAA-CR-CNT-YTD OF    \n043552         TDB-TDAACCT.\n043554     MOVE TDAA-CR-AMT-YTD OF TDAACCT TO TDB-TDAA-CR-AMT-YTD OF    \n043556         TDB-TDAACCT.\n043558     MOVE TDAA-DB-CNT-YTD OF TDAACCT TO TDB-TDAA-DB-CNT-YTD OF    \n043560         TDB-TDAACCT.\n043562     MOVE TDAA-DB-AMT-YTD OF TDAACCT TO TDB-TDAA-DB-AMT-YTD OF    \n043564         TDB-TDAACCT.\n043566     MOVE TDAA-DAYS-IN-TERM OF TDAACCT TO TDB-TDAA-DAYS-IN-TERM   \n043568         OF TDB-TDAACCT.\n043570     MOVE TDAA-BEG-INT-BAL OF TDAACCT TO TDB-TDAA-BEG-INT-BAL OF  \n043572         TDB-TDAACCT.\n043574     MOVE TDAA-PURCH-AMT OF TDAACCT TO TDB-TDAA-PURCH-AMT OF      \n043576         TDB-TDAACCT.\n043578     MOVE TDAA-CURR-BAL OF TDAACCT TO TDB-TDAA-CURR-BAL OF        \n043580         TDB-TDAACCT.\n043582     MOVE TDAA-AVAIL-BAL OF TDAACCT TO TDB-TDAA-AVAIL-BAL OF      \n043584         TDB-TDAACCT.\n043586     MOVE TDAA-BAL-BEG-MAT OF TDAACCT TO TDB-TDAA-BAL-BEG-MAT OF  \n043588         TDB-TDAACCT.\n043590     MOVE TDAA-CLOSE-AMT OF TDAACCT TO TDB-TDAA-CLOSE-AMT OF      \n043592         TDB-TDAACCT.\n043594     MOVE TDAA-MONEY-AMT OF TDAACCT TO TDB-TDAA-MONEY-AMT OF      \n043596         TDB-TDAACCT.\n043598     MOVE TDAA-BAL-BEG-STMT OF TDAACCT TO TDB-TDAA-BAL-BEG-STMT   \n043600         OF TDB-TDAACCT.\n043602     MOVE TDAA-ACCR-INT OF TDAACCT TO TDB-TDAA-ACCR-INT OF        \n043604         TDB-TDAACCT.\n043606     MOVE TDAA-ANTIC-INT OF TDAACCT TO TDB-TDAA-ANTIC-INT OF      \n043608         TDB-TDAACCT.\n043610     MOVE TDAA-INT-TO-POST OF TDAACCT TO TDB-TDAA-INT-TO-POST OF  \n043612         TDB-TDAACCT.\n043614     MOVE TDAA-1099-YTD OF TDAACCT TO TDB-TDAA-1099-YTD OF        \n043616         TDB-TDAACCT.\n043618     MOVE TDAA-1099-LST-YR OF TDAACCT TO TDB-TDAA-1099-LST-YR OF  \n043620         TDB-TDAACCT.\n043622     MOVE TDAA-CURR-PENLTY OF TDAACCT TO TDB-TDAA-CURR-PENLTY OF  \n043624         TDB-TDAACCT.\n043626     MOVE TDAA-PENLTY-STD OF TDAACCT TO TDB-TDAA-PENLTY-STD OF    \n043628         TDB-TDAACCT.\n043630     MOVE TDAA-PENLTY-YTD OF TDAACCT TO TDB-TDAA-PENLTY-YTD OF    \n043632         TDB-TDAACCT.\n043634     MOVE TDAA-LST-PENLTY OF TDAACCT TO TDB-TDAA-LST-PENLTY OF    \n043636         TDB-TDAACCT.\n043638     MOVE TDAA-CURR-INT-ADJ OF TDAACCT TO TDB-TDAA-CURR-INT-ADJ   \n043640         OF TDB-TDAACCT.\n043642     MOVE TDAA-TOTAMT-HOLDS OF TDAACCT TO TDB-TDAA-TOTAMT-HOLDS   \n043644         OF TDB-TDAACCT.\n043646     MOVE TDAA-NXT-INT-ADJ OF TDAACCT TO TDB-TDAA-NXT-INT-ADJ OF  \n043648         TDB-TDAACCT.\n043650     MOVE TDAA-FEE-AMT OF TDAACCT TO TDB-TDAA-FEE-AMT OF          \n043652         TDB-TDAACCT.\n043654     MOVE TDAA-OID-RPT-INT OF TDAACCT TO TDB-TDAA-OID-RPT-INT OF  \n043656         TDB-TDAACCT.\n043658     MOVE TDAA-FAIR-MRKT OF TDAACCT TO TDB-TDAA-FAIR-MRKT OF      \n043660         TDB-TDAACCT.\n043662     MOVE TDAA-CUR-WHLD-AMT OF TDAACCT TO TDB-TDAA-CUR-WHLD-AMT   \n043664         OF TDB-TDAACCT.\n043666     MOVE TDAA-LST-WHLD-AMT OF TDAACCT TO TDB-TDAA-LST-WHLD-AMT   \n043668         OF TDB-TDAACCT.\n043670     MOVE TDAA-WTHLD-STD OF TDAACCT TO TDB-TDAA-WTHLD-STD OF      \n043672         TDB-TDAACCT.\n043674     MOVE TDAA-WTHLD-YTD OF TDAACCT TO TDB-TDAA-WTHLD-YTD OF      \n043676         TDB-TDAACCT.\n043678     MOVE TDAA-LST-INT-PMT OF TDAACCT TO TDB-TDAA-LST-INT-PMT OF  \n043680         TDB-TDAACCT.\n043682     MOVE TDAA-BAL-BEG-YR OF TDAACCT TO TDB-TDAA-BAL-BEG-YR OF    \n043684         TDB-TDAACCT.\n043686     MOVE TDAA-BAL-AT-CONV OF TDAACCT TO TDB-TDAA-BAL-AT-CONV OF  \n043688         TDB-TDAACCT.\n043690     MOVE TDAA-BAL-BEG-LYR OF TDAACCT TO TDB-TDAA-BAL-BEG-LYR OF  \n043692         TDB-TDAACCT.\n043694     MOVE TDAA-MIN-BAL-STD OF TDAACCT TO TDB-TDAA-MIN-BAL-STD OF  \n043696         TDB-TDAACCT.\n043698     MOVE TDAA-MIN-BAL-YTD OF TDAACCT TO TDB-TDAA-MIN-BAL-YTD OF  \n043700         TDB-TDAACCT.\n043702     MOVE TDAA-MAX-BAL-YTD OF TDAACCT TO TDB-TDAA-MAX-BAL-YTD OF  \n043704         TDB-TDAACCT.\n043706     MOVE TDAA-LMINBAL-STD OF TDAACCT TO TDB-TDAA-LMINBAL-STD OF  \n043708         TDB-TDAACCT.\n043710     MOVE TDAA-CMPD-INT OF TDAACCT TO TDB-TDAA-CMPD-INT OF        \n043712         TDB-TDAACCT.\n043714     MOVE TDAA-PER-DIEM OF TDAACCT TO TDB-TDAA-PER-DIEM OF        \n043716         TDB-TDAACCT.\n043718     MOVE TDAA-AVG-PER-DIEM OF TDAACCT TO TDB-TDAA-AVG-PER-DIEM   \n043720         OF TDB-TDAACCT.\n043722     MOVE TDAA-EMAIL-MAXAMT OF TDAACCT TO TDB-TDAA-EMAIL-MAXAMT   \n043724         OF TDB-TDAACCT.\n043726     MOVE TDAA-EMAIL-MINAMT OF TDAACCT TO TDB-TDAA-EMAIL-MINAMT   \n043728         OF TDB-TDAACCT.\n043730     MOVE TDAA-DTH-FAIRMKT OF TDAACCT TO TDB-TDAA-DTH-FAIRMKT OF  \n043732         TDB-TDAACCT.\n043734     MOVE TDAA-PENLTY-WAIVE OF TDAACCT TO TDB-TDAA-PENLTY-WAIVE   \n043736         OF TDB-TDAACCT.\n043738     MOVE TDAA-BEG-INT-RT OF TDAACCT TO TDB-TDAA-BEG-INT-RT OF    \n043740         TDB-TDAACCT.\n043742     MOVE TDAA-CUR-INT-RT OF TDAACCT TO TDB-TDAA-CUR-INT-RT OF    \n043744         TDB-TDAACCT.\n043746     MOVE TDAA-FLOOR-RT OF TDAACCT TO TDB-TDAA-FLOOR-RT OF        \n043748         TDB-TDAACCT.\n043750     MOVE TDAA-FLOOR-INCR OF TDAACCT TO TDB-TDAA-FLOOR-INCR OF    \n043752         TDB-TDAACCT.\n043754     MOVE TDAA-YIELD-RT OF TDAACCT TO TDB-TDAA-YIELD-RT OF        \n043756         TDB-TDAACCT.\n043758     MOVE 1 TO Z-II.\n043760 Z-12-1-1-LOOP.\n043762     IF Z-II > 10\n043764         GO TO Z-12-1-1-LOOP-XIT.\n043766     MOVE TDAA-RISE-RATE OF TDAACCT (Z-II) TO TDB-TDAA-RISE-RATE  \n043768         OF TDB-TDAACCT (Z-II).\n043770     ADD 1 TO Z-II.\n043772     GO TO Z-12-1-1-LOOP.\n043774 Z-12-1-1-LOOP-XIT.\n043776     MOVE TDAA-LNS-INCRMNT OF TDAACCT TO TDB-TDAA-LNS-INCRMNT OF  \n043778         TDB-TDAACCT.\n043780     MOVE TDAA-RT-VARIANCE OF TDAACCT TO TDB-TDAA-RT-VARIANCE OF  \n043782         TDB-TDAACCT.\n043784     MOVE TDAA-CONST-RT-ADJ OF TDAACCT TO TDB-TDAA-CONST-RT-ADJ   \n043786         OF TDB-TDAACCT.\n043788     MOVE TDAA-RATE-AT-EOY OF TDAACCT TO TDB-TDAA-RATE-AT-EOY OF  \n043790         TDB-TDAACCT.\n043792     MOVE TDAA-RATE-LST-STM OF TDAACCT TO TDB-TDAA-RATE-LST-STM   \n043794         OF TDB-TDAACCT.\n043796     MOVE TDAA-ORG-YIELD-RT OF TDAACCT TO TDB-TDAA-ORG-YIELD-RT   \n043798         OF TDB-TDAACCT.\n043800     MOVE TDAA-REN-YIELD-RT OF TDAACCT TO TDB-TDAA-REN-YIELD-RT   \n043802         OF TDB-TDAACCT.\n043804     MOVE TDAA-SCHED-DT OF TDAACCT TO TDB-TDAA-SCHED-DT OF        \n043806         TDB-TDAACCT.\n043808     MOVE TDAA-ACCR-DT OF TDAACCT TO TDB-TDAA-ACCR-DT OF          \n043810         TDB-TDAACCT.\n043812     MOVE TDAA-OPEN-DT OF TDAACCT TO TDB-TDAA-OPEN-DT OF          \n043814         TDB-TDAACCT.\n043816     MOVE TDAA-CLSD-DT OF TDAACCT TO TDB-TDAA-CLSD-DT OF          \n043818         TDB-TDAACCT.\n043820     MOVE TDAA-LST-MAT-DT OF TDAACCT TO TDB-TDAA-LST-MAT-DT OF    \n043822         TDB-TDAACCT.\n043824     MOVE TDAA-LST-POST-DT OF TDAACCT TO TDB-TDAA-LST-POST-DT OF  \n043826         TDB-TDAACCT.\n043828     MOVE TDAA-LST-IN-PROC OF TDAACCT TO TDB-TDAA-LST-IN-PROC OF  \n043830         TDB-TDAACCT.\n043832     MOVE TDAA-LST-CONTACT OF TDAACCT TO TDB-TDAA-LST-CONTACT OF  \n043834         TDB-TDAACCT.\n043836     MOVE TDAA-LST-FEE-DT OF TDAACCT TO TDB-TDAA-LST-FEE-DT OF    \n043838         TDB-TDAACCT.\n043840     MOVE TDAA-LST-RTCHG-DT OF TDAACCT TO TDB-TDAA-LST-RTCHG-DT   \n043842         OF TDB-TDAACCT.\n043844     MOVE TDAA-LST-DIST-DT OF TDAACCT TO TDB-TDAA-LST-DIST-DT OF  \n043846         TDB-TDAACCT.\n043848     MOVE TDAA-LST-STMT-DT OF TDAACCT TO TDB-TDAA-LST-STMT-DT OF  \n043850         TDB-TDAACCT.\n043852     MOVE TDAA-LST-CMPD-DT OF TDAACCT TO TDB-TDAA-LST-CMPD-DT OF  \n043854         TDB-TDAACCT.\n043856     MOVE 1 TO Z-II.\n043858 Z-12-1-2-LOOP.\n043860     IF Z-II > 10\n043862         GO TO Z-12-1-2-LOOP-XIT.\n043864     MOVE TDAA-RR-CYC-DT OF TDAACCT (Z-II) TO TDB-TDAA-RR-CYC-DT  \n043866         OF TDB-TDAACCT (Z-II).\n043868     ADD 1 TO Z-II.\n043870     GO TO Z-12-1-2-LOOP.\n043872 Z-12-1-2-LOOP-XIT.\n043874     MOVE TDAA-BNF-BIRTH-DT OF TDAACCT TO TDB-TDAA-BNF-BIRTH-DT   \n043876         OF TDB-TDAACCT.\n043878     MOVE TDAA-BNF-DEATH-DT OF TDAACCT TO TDB-TDAA-BNF-DEATH-DT   \n043880         OF TDB-TDAACCT.\n043882     MOVE TDAA-LUPD-DATE OF TDAACCT TO TDB-TDAA-LUPD-DATE OF      \n043884         TDB-TDAACCT.\n043886     MOVE TDAA-LUPD-TIME OF TDAACCT TO TDB-TDAA-LUPD-TIME OF      \n043888         TDB-TDAACCT.\n043890     MOVE TDAA-ADD-DT OF TDAACCT TO TDB-TDAA-ADD-DT OF            \n043892         TDB-TDAACCT.\n043894     MOVE TDAA-ADD-TM OF TDAACCT TO TDB-TDAA-ADD-TM OF            \n043896         TDB-TDAACCT.\n043898     MOVE TDAA-CONV-DT OF TDAACCT TO TDB-TDAA-CONV-DT OF          \n043900         TDB-TDAACCT.\n043902     MOVE TDAA-ACT-CLOSE-DT OF TDAACCT TO TDB-TDAA-ACT-CLOSE-DT   \n043904         OF TDB-TDAACCT.\n043906     MOVE TDAA-LST-TBACT-DT OF TDAACCT TO TDB-TDAA-LST-TBACT-DT   \n043908         OF TDB-TDAACCT.\n043910     MOVE TDAA-ALERT-EXP-DT OF TDAACCT TO TDB-TDAA-ALERT-EXP-DT   \n043912         OF TDB-TDAACCT.\n043914     MOVE TDAA-ALRT2-EXP-DT OF TDAACCT TO TDB-TDAA-ALRT2-EXP-DT   \n043916         OF TDB-TDAACCT.\n043918     MOVE TDAA-ALRT3-EXP-DT OF TDAACCT TO TDB-TDAA-ALRT3-EXP-DT   \n043920         OF TDB-TDAACCT.\n043922     MOVE TDAA-NXT-FEE-DT OF TDAACCT TO TDB-TDAA-NXT-FEE-DT OF    \n043924         TDB-TDAACCT.\n043926     MOVE TDAA-NXT-POST-DT OF TDAACCT TO TDB-TDAA-NXT-POST-DT OF  \n043928         TDB-TDAACCT.\n043930     MOVE TDAA-NXT-MAT-DT OF TDAACCT TO TDB-TDAA-NXT-MAT-DT OF    \n043932         TDB-TDAACCT.\n043934     MOVE TDAA-NXT-DIST-DT OF TDAACCT TO TDB-TDAA-NXT-DIST-DT OF  \n043936         TDB-TDAACCT.\n043938     MOVE TDAA-NXT-RT-CHG OF TDAACCT TO TDB-TDAA-NXT-RT-CHG OF    \n043940         TDB-TDAACCT.\n043942     MOVE TDAA-NXT-IN-PROC OF TDAACCT TO TDB-TDAA-NXT-IN-PROC OF  \n043944         TDB-TDAACCT.\n043946     MOVE TDAA-NXT-CMPD-DT OF TDAACCT TO TDB-TDAA-NXT-CMPD-DT OF  \n043948         TDB-TDAACCT.\n043950     MOVE TDAA-NXT-STMT-DT OF TDAACCT TO TDB-TDAA-NXT-STMT-DT OF  \n043952         TDB-TDAACCT.\n043954     MOVE TDAA-NXT-DS-PROC OF TDAACCT TO TDB-TDAA-NXT-DS-PROC OF  \n043956         TDB-TDAACCT.\n043958     MOVE TDAA-ADV-NTC-DT OF TDAACCT TO TDB-TDAA-ADV-NTC-DT OF    \n043960         TDB-TDAACCT.\n043962     MOVE TDAA-NXT-29YR-DT OF TDAACCT TO TDB-TDAA-NXT-29YR-DT OF  \n043964         TDB-TDAACCT.\n043966     MOVE TDAA-FAIR-MRKT-DT OF TDAACCT TO TDB-TDAA-FAIR-MRKT-DT   \n043968         OF TDB-TDAACCT.\n043970     MOVE TDAA-SORT-FIELD-1 OF TDAACCT TO TDB-TDAA-SORT-FIELD-1   \n043972         OF TDB-TDAACCT.\n043974     MOVE TDAA-SORT-FIELD-2 OF TDAACCT TO TDB-TDAA-SORT-FIELD-2   \n043976         OF TDB-TDAACCT.\n043978     MOVE TDAA-SORT-FIELD-3 OF TDAACCT TO TDB-TDAA-SORT-FIELD-3   \n043980         OF TDB-TDAACCT.\n043982     MOVE TDAA-SORT-FIELD-4 OF TDAACCT TO TDB-TDAA-SORT-FIELD-4   \n043984         OF TDB-TDAACCT.\n043986     MOVE TDAA-CMAT-PUB-ID OF TDAACCT TO TDB-TDAA-CMAT-PUB-ID OF  \n043988         TDB-TDAACCT.\n043990     MOVE TDAA-MSA-CONTR OF TDAACCT TO TDB-TDAA-MSA-CONTR OF      \n043992         TDB-TDAACCT.\n043994     MOVE TDAA-MSA-CONTR-LY OF TDAACCT TO TDB-TDAA-MSA-CONTR-LY   \n043996         OF TDB-TDAACCT.\n043998     MOVE TDAA-AVG-ACCR-INT OF TDAACCT TO TDB-TDAA-AVG-ACCR-INT   \n044000         OF TDB-TDAACCT.\n044002     MOVE TDAA-LEVEL-PAY OF TDAACCT TO TDB-TDAA-LEVEL-PAY OF      \n044004         TDB-TDAACCT.\n044006     MOVE TDAA-ST-INT-CD OF TDAACCT TO TDB-TDAA-ST-INT-CD OF      \n044008         TDB-TDAACCT.\n044010     MOVE TDAA-ST-WHLD-CD OF TDAACCT TO TDB-TDAA-ST-WHLD-CD OF    \n044012         TDB-TDAACCT.\n044014     MOVE TDAA-ST-WHLD-AMT OF TDAACCT TO TDB-TDAA-ST-WHLD-AMT OF  \n044016         TDB-TDAACCT.\n044018     MOVE TDAA-ST-CUR-W-AMT OF TDAACCT TO TDB-TDAA-ST-CUR-W-AMT   \n044020         OF TDB-TDAACCT.\n044022     MOVE TDAA-ST-LST-W-AMT OF TDAACCT TO TDB-TDAA-ST-LST-W-AMT   \n044024         OF TDB-TDAACCT.\n044026     MOVE TDAA-ST-WHLD-STD OF TDAACCT TO TDB-TDAA-ST-WHLD-STD OF  \n044028         TDB-TDAACCT.\n044030     MOVE TDAA-ST-WHLD-YTD OF TDAACCT TO TDB-TDAA-ST-WHLD-YTD OF  \n044032         TDB-TDAACCT.\n044034     MOVE TDAA-CIF-REMARK OF TDAACCT TO TDB-TDAA-CIF-REMARK OF    \n044036         TDB-TDAACCT.\n044038     MOVE TDAA-CSR OF TDAACCT TO TDB-TDAA-CSR OF TDB-TDAACCT.\n044040     MOVE TDAA-BSA-O-RSK-CD OF TDAACCT TO TDB-TDAA-BSA-O-RSK-CD   \n044042         OF TDB-TDAACCT.\n044044     MOVE TDAA-BSA-C-RSK-CD OF TDAACCT TO TDB-TDAA-BSA-C-RSK-CD   \n044046         OF TDB-TDAACCT.\n044048     MOVE TDAA-LRG-TRX-DT OF TDAACCT TO TDB-TDAA-LRG-TRX-DT OF    \n044050         TDB-TDAACCT.\n044052     MOVE TDAA-HSA-FMLY-IND OF TDAACCT TO TDB-TDAA-HSA-FMLY-IND   \n044054         OF TDB-TDAACCT.\n044056     MOVE TDAA-STOP-PAY-IND OF TDAACCT TO TDB-TDAA-STOP-PAY-IND   \n044058         OF TDB-TDAACCT.\n044060     MOVE TDAA-IMG-PG-TYPE OF TDAACCT TO TDB-TDAA-IMG-PG-TYPE OF  \n044062         TDB-TDAACCT.\n044064     MOVE TDAA-CONT-LMT-CLC OF TDAACCT TO TDB-TDAA-CONT-LMT-CLC   \n044066         OF TDB-TDAACCT.\n044068     MOVE TDAA-CONT-LMT-ENT OF TDAACCT TO TDB-TDAA-CONT-LMT-ENT   \n044070         OF TDB-TDAACCT.\n044072     MOVE TDAA-MEMO-DB OF TDAACCT TO TDB-TDAA-MEMO-DB OF          \n044074         TDB-TDAACCT.\n044076     MOVE TDAA-MEMO-CR OF TDAACCT TO TDB-TDAA-MEMO-CR OF          \n044078         TDB-TDAACCT.\n044080     MOVE TDAA-MEMO-DB-2 OF TDAACCT TO TDB-TDAA-MEMO-DB-2 OF      \n044082         TDB-TDAACCT.\n044084     MOVE TDAA-MEMO-CR-2 OF TDAACCT TO TDB-TDAA-MEMO-CR-2 OF      \n044086         TDB-TDAACCT.\n044088     MOVE TDAA-RT-AT-CONV OF TDAACCT TO TDB-TDAA-RT-AT-CONV OF    \n044090         TDB-TDAACCT.\n044092     MOVE TDAA-ACCR-AT-CONV OF TDAACCT TO TDB-TDAA-ACCR-AT-CONV   \n044094         OF TDB-TDAACCT.\n044096     MOVE TDAA-RT-AT-ACRDT OF TDAACCT TO TDB-TDAA-RT-AT-ACRDT OF  \n044098         TDB-TDAACCT.\n044100     MOVE TDAA-BAL-AT-ACRDT OF TDAACCT TO TDB-TDAA-BAL-AT-ACRDT   \n044102         OF TDB-TDAACCT.\n044104     MOVE TDAA-ZERO-RT-ALLOW OF TDAACCT TO TDB-TDAA-ZERO-RT-ALLOW \n044106         OF TDB-TDAACCT.\n044108     MOVE TDAA-EMAIL-NTC OF TDAACCT TO TDB-TDAA-EMAIL-NTC OF      \n044110         TDB-TDAACCT.\n044112     MOVE TDAA-EMAIL-STMT OF TDAACCT TO TDB-TDAA-EMAIL-STMT OF    \n044114         TDB-TDAACCT.\n044116     MOVE TDAA-FRAUD-CK-DT OF TDAACCT TO TDB-TDAA-FRAUD-CK-DT OF  \n044118         TDB-TDAACCT.\n044120     MOVE TDAA-FRAUD-CK-CNT OF TDAACCT TO TDB-TDAA-FRAUD-CK-CNT   \n044122         OF TDB-TDAACCT.\n044124     MOVE TDAA-FRAUD-CK-AMT OF TDAACCT TO TDB-TDAA-FRAUD-CK-AMT   \n044126         OF TDB-TDAACCT.\n044128     MOVE TDAA-MISC-ACCTNO OF TDAACCT TO TDB-TDAA-MISC-ACCTNO OF  \n044130         TDB-TDAACCT.\n044132     MOVE TDAA-RMD-MAN-CALC OF TDAACCT TO TDB-TDAA-RMD-MAN-CALC   \n044134         OF TDB-TDAACCT.\n044136     MOVE TDAA-RMD-AMOUNT OF TDAACCT TO TDB-TDAA-RMD-AMOUNT OF    \n044138         TDB-TDAACCT.\n044140     MOVE TDAA-BROKERAGE-ID OF TDAACCT TO TDB-TDAA-BROKERAGE-ID   \n044142         OF TDB-TDAACCT.\n044144     MOVE TDAA-EV-LARGE-TRX OF TDAACCT TO TDB-TDAA-EV-LARGE-TRX   \n044146         OF TDB-TDAACCT.\n044148     MOVE TDAA-EV-MAT-AMT OF TDAACCT TO TDB-TDAA-EV-MAT-AMT OF    \n044150         TDB-TDAACCT.\n044152     MOVE TDAA-EV-DISP-ACCT OF TDAACCT TO TDB-TDAA-EV-DISP-ACCT   \n044154         OF TDB-TDAACCT.\n044156     MOVE TDAA-EV-COMP-ACCT OF TDAACCT TO TDB-TDAA-EV-COMP-ACCT   \n044158         OF TDB-TDAACCT.\n044160     MOVE TDAA-EV-PUBLIC-ID OF TDAACCT TO TDB-TDAA-EV-PUBLIC-ID   \n044162         OF TDB-TDAACCT.\n044164     MOVE TDAA-EV-MAT-TYPE OF TDAACCT TO TDB-TDAA-EV-MAT-TYPE OF  \n044166         TDB-TDAACCT.\n044168     MOVE TDAA-EV-INT-TYPE OF TDAACCT TO TDB-TDAA-EV-INT-TYPE OF  \n044170         TDB-TDAACCT.\n044172     MOVE TDAA-EV-ACCT-TYP OF TDAACCT TO TDB-TDAA-EV-ACCT-TYP OF  \n044174         TDB-TDAACCT.\n044176     MOVE TDAA-EV-WHLD-PCT OF TDAACCT TO TDB-TDAA-EV-WHLD-PCT OF  \n044178         TDB-TDAACCT.\n044180     MOVE TDAA-EV-NON-ACCR OF TDAACCT TO TDB-TDAA-EV-NON-ACCR OF  \n044182         TDB-TDAACCT.\n044184     MOVE TDAA-EV-CLOSED OF TDAACCT TO TDB-TDAA-EV-CLOSED OF      \n044186         TDB-TDAACCT.\n044188     MOVE TDAA-EV-CLOSE-MO OF TDAACCT TO TDB-TDAA-EV-CLOSE-MO OF  \n044190         TDB-TDAACCT.\n044192     MOVE TDAA-EV-OPEN-MO OF TDAACCT TO TDB-TDAA-EV-OPEN-MO OF    \n044194         TDB-TDAACCT.\n044196     MOVE TDAA-EV-ANN-INT OF TDAACCT TO TDB-TDAA-EV-ANN-INT OF    \n044198         TDB-TDAACCT.\n044200     MOVE TDAA-EV-ORIG-RT OF TDAACCT TO TDB-TDAA-EV-ORIG-RT OF    \n044202         TDB-TDAACCT.\n044204     MOVE TDAA-EV-DLY-INT OF TDAACCT TO TDB-TDAA-EV-DLY-INT OF    \n044206         TDB-TDAACCT.\n044208     MOVE TDAA-EV-INT-PAY OF TDAACCT TO TDB-TDAA-EV-INT-PAY OF    \n044210         TDB-TDAACCT.\n044212     MOVE TDAA-EV-AVAIL-BL OF TDAACCT TO TDB-TDAA-EV-AVAIL-BL OF  \n044214         TDB-TDAACCT.\n044216     MOVE TDAA-EV-RETAIN OF TDAACCT TO TDB-TDAA-EV-RETAIN OF      \n044218         TDB-TDAACCT.\n044220     MOVE TDAA-EV-CL-RETAIN OF TDAACCT TO TDB-TDAA-EV-CL-RETAIN   \n044222         OF TDB-TDAACCT.\n044224     MOVE TDAA-EV-TIMES-REN OF TDAACCT TO TDB-TDAA-EV-TIMES-REN   \n044226         OF TDB-TDAACCT.\n044228     MOVE TDAA-EV-CURR-BAL OF TDAACCT TO TDB-TDAA-EV-CURR-BAL OF  \n044230         TDB-TDAACCT.\n044232     MOVE TDAA-MONY-SRC-CD2 OF TDAACCT TO TDB-TDAA-MONY-SRC-CD2   \n044234         OF TDB-TDAACCT.\n044236     MOVE TDAA-INHERIT-IRA OF TDAACCT TO TDB-TDAA-INHERIT-IRA OF  \n044238         TDB-TDAACCT.\n044240     MOVE TDAA-LIFE-FACTOR OF TDAACCT TO TDB-TDAA-LIFE-FACTOR OF  \n044242         TDB-TDAACCT.\n044244     MOVE TDAA-BRKR-DEP-CAT OF TDAACCT TO TDB-TDAA-BRKR-DEP-CAT   \n044246         OF TDB-TDAACCT.\n044248     MOVE TDAA-LINE-OF-BUS OF TDAACCT TO TDB-TDAA-LINE-OF-BUS OF  \n044250         TDB-TDAACCT.\n044252     MOVE TDAA-1ST-STMT OF TDAACCT TO TDB-TDAA-1ST-STMT OF        \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    397 lines from 21726 to 22122.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 45, "total_chunks": 55, "start_line": 21726, "end_line": 22122, "line_count": 397}

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
- Source code length: 24904 characters

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
CHUNK 45 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 21726 to 22122 (397 lines)
Chunk Tokens (estimated): ~8,094
Actual Input Tokens: 9,500 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 21726-22122 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 45 of 55 chunks
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
      The source code below is only CHUNK 45 of 55.


=============================================================================
CHUNK 45 SOURCE CODE (Lines 21726-22122)
=============================================================================

```cobol
043460         TDB-TDAACCT.
043462     MOVE TDAA-DDA-ACCT-1 OF TDAACCT TO TDB-TDAA-DDA-ACCT-1 OF    
043464         TDB-TDAACCT.
043466     MOVE TDAA-DDA-ACCT-1-S OF TDAACCT TO TDB-TDAA-DDA-ACCT-1-S   
043468         OF TDB-TDAACCT.
043470     MOVE TDAA-DDA-ACCT-2 OF TDAACCT TO TDB-TDAA-DDA-ACCT-2 OF    
043472         TDB-TDAACCT.
043474     MOVE TDAA-DDA-ACCT-2-S OF TDAACCT TO TDB-TDAA-DDA-ACCT-2-S   
043476         OF TDB-TDAACCT.
043478     MOVE TDAA-DDA-ACCT-3 OF TDAACCT TO TDB-TDAA-DDA-ACCT-3 OF    
043480         TDB-TDAACCT.
043482     MOVE TDAA-DDA-ACCT-3-S OF TDAACCT TO TDB-TDAA-DDA-ACCT-3-S   
043484         OF TDB-TDAACCT.
043486     MOVE TDAA-INT-ACCT OF TDAACCT TO TDB-TDAA-INT-ACCT OF        
043488         TDB-TDAACCT.
043490     MOVE TDAA-INT-ACCT-S OF TDAACCT TO TDB-TDAA-INT-ACCT-S OF    
043492         TDB-TDAACCT.
043494     MOVE TDAA-CS-ACCT OF TDAACCT TO TDB-TDAA-CS-ACCT OF          
043496         TDB-TDAACCT.
043498     MOVE TDAA-CS-ACCT-S OF TDAACCT TO TDB-TDAA-CS-ACCT-S OF      
043500         TDB-TDAACCT.
043502     MOVE TDAA-CC-ACCT OF TDAACCT TO TDB-TDAA-CC-ACCT OF          
043504         TDB-TDAACCT.
043506     MOVE TDAA-LNS-BORROWER OF TDAACCT TO TDB-TDAA-LNS-BORROWER   
043508         OF TDB-TDAACCT.
043510     MOVE TDAA-LNS-NOTE OF TDAACCT TO TDB-TDAA-LNS-NOTE OF        
043512         TDB-TDAACCT.
043514     MOVE TDAA-CNV-OLD-ACCT OF TDAACCT TO TDB-TDAA-CNV-OLD-ACCT   
043516         OF TDB-TDAACCT.
043518     MOVE TDAA-CLS-ACCT OF TDAACCT TO TDB-TDAA-CLS-ACCT OF        
043520         TDB-TDAACCT.
043522     MOVE TDAA-CLS-ACCT-S OF TDAACCT TO TDB-TDAA-CLS-ACCT-S OF    
043524         TDB-TDAACCT.
043526     MOVE TDAA-DAYS-IN-PER OF TDAACCT TO TDB-TDAA-DAYS-IN-PER OF  
043528         TDB-TDAACCT.
043530     MOVE TDAA-RR-CYC-NBR OF TDAACCT TO TDB-TDAA-RR-CYC-NBR OF    
043532         TDB-TDAACCT.
043534     MOVE TDAA-CR-CNT-STD OF TDAACCT TO TDB-TDAA-CR-CNT-STD OF    
043536         TDB-TDAACCT.
043538     MOVE TDAA-CR-AMT-STD OF TDAACCT TO TDB-TDAA-CR-AMT-STD OF    
043540         TDB-TDAACCT.
043542     MOVE TDAA-DB-CNT-STD OF TDAACCT TO TDB-TDAA-DB-CNT-STD OF    
043544         TDB-TDAACCT.
043546     MOVE TDAA-DB-AMT-STD OF TDAACCT TO TDB-TDAA-DB-AMT-STD OF    
043548         TDB-TDAACCT.
043550     MOVE TDAA-CR-CNT-YTD OF TDAACCT TO TDB-TDAA-CR-CNT-YTD OF    
043552         TDB-TDAACCT.
043554     MOVE TDAA-CR-AMT-YTD OF TDAACCT TO TDB-TDAA-CR-AMT-YTD OF    
043556         TDB-TDAACCT.
043558     MOVE TDAA-DB-CNT-YTD OF TDAACCT TO TDB-TDAA-DB-CNT-YTD OF    
043560         TDB-TDAACCT.
043562     MOVE TDAA-DB-AMT-YTD OF TDAACCT TO TDB-TDAA-DB-AMT-YTD OF    
043564         TDB-TDAACCT.
043566     MOVE TDAA-DAYS-IN-TERM OF TDAACCT TO TDB-TDAA-DAYS-IN-TERM   
043568         OF TDB-TDAACCT.
043570     MOVE TDAA-BEG-INT-BAL OF TDAACCT TO TDB-TDAA-BEG-INT-BAL OF  
043572         TDB-TDAACCT.
043574     MOVE TDAA-PURCH-AMT OF TDAACCT TO TDB-TDAA-PURCH-AMT OF      
043576         TDB-TDAACCT.
043578     MOVE TDAA-CURR-BAL OF TDAACCT TO TDB-TDAA-CURR-BAL OF        
043580         TDB-TDAACCT.
043582     MOVE TDAA-AVAIL-BAL OF TDAACCT TO TDB-TDAA-AVAIL-BAL OF      
043584         TDB-TDAACCT.
043586     MOVE TDAA-BAL-BEG-MAT OF TDAACCT TO TDB-TDAA-BAL-BEG-MAT OF  
043588         TDB-TDAACCT.
043590     MOVE TDAA-CLOSE-AMT OF TDAACCT TO TDB-TDAA-CLOSE-AMT OF      
043592         TDB-TDAACCT.
043594     MOVE TDAA-MONEY-AMT OF TDAACCT TO TDB-TDAA-MONEY-AMT OF      
043596         TDB-TDAACCT.
043598     MOVE TDAA-BAL-BEG-STMT OF TDAACCT TO TDB-TDAA-BAL-BEG-STMT   
043600         OF TDB-TDAACCT.
043602     MOVE TDAA-ACCR-INT OF TDAACCT TO TDB-TDAA-ACCR-INT OF        
043604         TDB-TDAACCT.
043606     MOVE TDAA-ANTIC-INT OF TDAACCT TO TDB-TDAA-ANTIC-INT OF      
043608         TDB-TDAACCT.
043610     MOVE TDAA-INT-TO-POST OF TDAACCT TO TDB-TDAA-INT-TO-POST OF  
043612         TDB-TDAACCT.
043614     MOVE TDAA-1099-YTD OF TDAACCT TO TDB-TDAA-1099-YTD OF        
043616         TDB-TDAACCT.
043618     MOVE TDAA-1099-LST-YR OF TDAACCT TO TDB-TDAA-1099-LST-YR OF  
043620         TDB-TDAACCT.
043622     MOVE TDAA-CURR-PENLTY OF TDAACCT TO TDB-TDAA-CURR-PENLTY OF  
043624         TDB-TDAACCT.
043626     MOVE TDAA-PENLTY-STD OF TDAACCT TO TDB-TDAA-PENLTY-STD OF    
043628         TDB-TDAACCT.
043630     MOVE TDAA-PENLTY-YTD OF TDAACCT TO TDB-TDAA-PENLTY-YTD OF    
043632         TDB-TDAACCT.
043634     MOVE TDAA-LST-PENLTY OF TDAACCT TO TDB-TDAA-LST-PENLTY OF    
043636         TDB-TDAACCT.
043638     MOVE TDAA-CURR-INT-ADJ OF TDAACCT TO TDB-TDAA-CURR-INT-ADJ   
043640         OF TDB-TDAACCT.
043642     MOVE TDAA-TOTAMT-HOLDS OF TDAACCT TO TDB-TDAA-TOTAMT-HOLDS   
043644         OF TDB-TDAACCT.
043646     MOVE TDAA-NXT-INT-ADJ OF TDAACCT TO TDB-TDAA-NXT-INT-ADJ OF  
043648         TDB-TDAACCT.
043650     MOVE TDAA-FEE-AMT OF TDAACCT TO TDB-TDAA-FEE-AMT OF          
043652         TDB-TDAACCT.
043654     MOVE TDAA-OID-RPT-INT OF TDAACCT TO TDB-TDAA-OID-RPT-INT OF  
043656         TDB-TDAACCT.
043658     MOVE TDAA-FAIR-MRKT OF TDAACCT TO TDB-TDAA-FAIR-MRKT OF      
043660         TDB-TDAACCT.
043662     MOVE TDAA-CUR-WHLD-AMT OF TDAACCT TO TDB-TDAA-CUR-WHLD-AMT   
043664         OF TDB-TDAACCT.
043666     MOVE TDAA-LST-WHLD-AMT OF TDAACCT TO TDB-TDAA-LST-WHLD-AMT   
043668         OF TDB-TDAACCT.
043670     MOVE TDAA-WTHLD-STD OF TDAACCT TO TDB-TDAA-WTHLD-STD OF      
043672         TDB-TDAACCT.
043674     MOVE TDAA-WTHLD-YTD OF TDAACCT TO TDB-TDAA-WTHLD-YTD OF      
043676         TDB-TDAACCT.
043678     MOVE TDAA-LST-INT-PMT OF TDAACCT TO TDB-TDAA-LST-INT-PMT OF  
043680         TDB-TDAACCT.
043682     MOVE TDAA-BAL-BEG-YR OF TDAACCT TO TDB-TDAA-BAL-BEG-YR OF    
043684         TDB-TDAACCT.
043686     MOVE TDAA-BAL-AT-CONV OF TDAACCT TO TDB-TDAA-BAL-AT-CONV OF  
043688         TDB-TDAACCT.
043690     MOVE TDAA-BAL-BEG-LYR OF TDAACCT TO TDB-TDAA-BAL-BEG-LYR OF  
043692         TDB-TDAACCT.
043694     MOVE TDAA-MIN-BAL-STD OF TDAACCT TO TDB-TDAA-MIN-BAL-STD OF  
043696         TDB-TDAACCT.
043698     MOVE TDAA-MIN-BAL-YTD OF TDAACCT TO TDB-TDAA-MIN-BAL-YTD OF  
043700         TDB-TDAACCT.
043702     MOVE TDAA-MAX-BAL-YTD OF TDAACCT TO TDB-TDAA-MAX-BAL-YTD OF  
043704         TDB-TDAACCT.
043706     MOVE TDAA-LMINBAL-STD OF TDAACCT TO TDB-TDAA-LMINBAL-STD OF  
043708         TDB-TDAACCT.
043710     MOVE TDAA-CMPD-INT OF TDAACCT TO TDB-TDAA-CMPD-INT OF        
043712         TDB-TDAACCT.
043714     MOVE TDAA-PER-DIEM OF TDAACCT TO TDB-TDAA-PER-DIEM OF        
043716         TDB-TDAACCT.
043718     MOVE TDAA-AVG-PER-DIEM OF TDAACCT TO TDB-TDAA-AVG-PER-DIEM   
043720         OF TDB-TDAACCT.
043722     MOVE TDAA-EMAIL-MAXAMT OF TDAACCT TO TDB-TDAA-EMAIL-MAXAMT   
043724         OF TDB-TDAACCT.
043726     MOVE TDAA-EMAIL-MINAMT OF TDAACCT TO TDB-TDAA-EMAIL-MINAMT   
043728         OF TDB-TDAACCT.
043730     MOVE TDAA-DTH-FAIRMKT OF TDAACCT TO TDB-TDAA-DTH-FAIRMKT OF  
043732         TDB-TDAACCT.
043734     MOVE TDAA-PENLTY-WAIVE OF TDAACCT TO TDB-TDAA-PENLTY-WAIVE   
043736         OF TDB-TDAACCT.
043738     MOVE TDAA-BEG-INT-RT OF TDAACCT TO TDB-TDAA-BEG-INT-RT OF    
043740         TDB-TDAACCT.
043742     MOVE TDAA-CUR-INT-RT OF TDAACCT TO TDB-TDAA-CUR-INT-RT OF    
043744         TDB-TDAACCT.
043746     MOVE TDAA-FLOOR-RT OF TDAACCT TO TDB-TDAA-FLOOR-RT OF        
043748         TDB-TDAACCT.
043750     MOVE TDAA-FLOOR-INCR OF TDAACCT TO TDB-TDAA-FLOOR-INCR OF    
043752         TDB-TDAACCT.
043754     MOVE TDAA-YIELD-RT OF TDAACCT TO TDB-TDAA-YIELD-RT OF        
043756         TDB-TDAACCT.
043758     MOVE 1 TO Z-II.
043760 Z-12-1-1-LOOP.
043762     IF Z-II > 10
043764         GO TO Z-12-1-1-LOOP-XIT.
043766     MOVE TDAA-RISE-RATE OF TDAACCT (Z-II) TO TDB-TDAA-RISE-RATE  
043768         OF TDB-TDAACCT (Z-II).
043770     ADD 1 TO Z-II.
043772     GO TO Z-12-1-1-LOOP.
043774 Z-12-1-1-LOOP-XIT.
043776     MOVE TDAA-LNS-INCRMNT OF TDAACCT TO TDB-TDAA-LNS-INCRMNT OF  
043778         TDB-TDAACCT.
043780     MOVE TDAA-RT-VARIANCE OF TDAACCT TO TDB-TDAA-RT-VARIANCE OF  
043782         TDB-TDAACCT.
043784     MOVE TDAA-CONST-RT-ADJ OF TDAACCT TO TDB-TDAA-CONST-RT-ADJ   
043786         OF TDB-TDAACCT.
043788     MOVE TDAA-RATE-AT-EOY OF TDAACCT TO TDB-TDAA-RATE-AT-EOY OF  
043790         TDB-TDAACCT.
043792     MOVE TDAA-RATE-LST-STM OF TDAACCT TO TDB-TDAA-RATE-LST-STM   
043794         OF TDB-TDAACCT.
043796     MOVE TDAA-ORG-YIELD-RT OF TDAACCT TO TDB-TDAA-ORG-YIELD-RT   
043798         OF TDB-TDAACCT.
043800     MOVE TDAA-REN-YIELD-RT OF TDAACCT TO TDB-TDAA-REN-YIELD-RT   
043802         OF TDB-TDAACCT.
043804     MOVE TDAA-SCHED-DT OF TDAACCT TO TDB-TDAA-SCHED-DT OF        
043806         TDB-TDAACCT.
043808     MOVE TDAA-ACCR-DT OF TDAACCT TO TDB-TDAA-ACCR-DT OF          
043810         TDB-TDAACCT.
043812     MOVE TDAA-OPEN-DT OF TDAACCT TO TDB-TDAA-OPEN-DT OF          
043814         TDB-TDAACCT.
043816     MOVE TDAA-CLSD-DT OF TDAACCT TO TDB-TDAA-CLSD-DT OF          
043818         TDB-TDAACCT.
043820     MOVE TDAA-LST-MAT-DT OF TDAACCT TO TDB-TDAA-LST-MAT-DT OF    
043822         TDB-TDAACCT.
043824     MOVE TDAA-LST-POST-DT OF TDAACCT TO TDB-TDAA-LST-POST-DT OF  
043826         TDB-TDAACCT.
043828     MOVE TDAA-LST-IN-PROC OF TDAACCT TO TDB-TDAA-LST-IN-PROC OF  
043830         TDB-TDAACCT.
043832     MOVE TDAA-LST-CONTACT OF TDAACCT TO TDB-TDAA-LST-CONTACT OF  
043834         TDB-TDAACCT.
043836     MOVE TDAA-LST-FEE-DT OF TDAACCT TO TDB-TDAA-LST-FEE-DT OF    
043838         TDB-TDAACCT.
043840     MOVE TDAA-LST-RTCHG-DT OF TDAACCT TO TDB-TDAA-LST-RTCHG-DT   
043842         OF TDB-TDAACCT.
043844     MOVE TDAA-LST-DIST-DT OF TDAACCT TO TDB-TDAA-LST-DIST-DT OF  
043846         TDB-TDAACCT.
043848     MOVE TDAA-LST-STMT-DT OF TDAACCT TO TDB-TDAA-LST-STMT-DT OF  
043850         TDB-TDAACCT.
043852     MOVE TDAA-LST-CMPD-DT OF TDAACCT TO TDB-TDAA-LST-CMPD-DT OF  
043854         TDB-TDAACCT.
043856     MOVE 1 TO Z-II.
043858 Z-12-1-2-LOOP.
043860     IF Z-II > 10
043862         GO TO Z-12-1-2-LOOP-XIT.
043864     MOVE TDAA-RR-CYC-DT OF TDAACCT (Z-II) TO TDB-TDAA-RR-CYC-DT  
043866         OF TDB-TDAACCT (Z-II).
043868     ADD 1 TO Z-II.
043870     GO TO Z-12-1-2-LOOP.
043872 Z-12-1-2-LOOP-XIT.
043874     MOVE TDAA-BNF-BIRTH-DT OF TDAACCT TO TDB-TDAA-BNF-BIRTH-DT   
043876         OF TDB-TDAACCT.
043878     MOVE TDAA-BNF-DEATH-DT OF TDAACCT TO TDB-TDAA-BNF-DEATH-DT   
043880         OF TDB-TDAACCT.
043882     MOVE TDAA-LUPD-DATE OF TDAACCT TO TDB-TDAA-LUPD-DATE OF      
043884         TDB-TDAACCT.
043886     MOVE TDAA-LUPD-TIME OF TDAACCT TO TDB-TDAA-LUPD-TIME OF      
043888         TDB-TDAACCT.
043890     MOVE TDAA-ADD-DT OF TDAACCT TO TDB-TDAA-ADD-DT OF            
043892         TDB-TDAACCT.
043894     MOVE TDAA-ADD-TM OF TDAACCT TO TDB-TDAA-ADD-TM OF            
043896         TDB-TDAACCT.
043898     MOVE TDAA-CONV-DT OF TDAACCT TO TDB-TDAA-CONV-DT OF          
043900         TDB-TDAACCT.
043902     MOVE TDAA-ACT-CLOSE-DT OF TDAACCT TO TDB-TDAA-ACT-CLOSE-DT   
043904         OF TDB-TDAACCT.
043906     MOVE TDAA-LST-TBACT-DT OF TDAACCT TO TDB-TDAA-LST-TBACT-DT   
043908         OF TDB-TDAACCT.
043910     MOVE TDAA-ALERT-EXP-DT OF TDAACCT TO TDB-TDAA-ALERT-EXP-DT   
043912         OF TDB-TDAACCT.
043914     MOVE TDAA-ALRT2-EXP-DT OF TDAACCT TO TDB-TDAA-ALRT2-EXP-DT   
043916         OF TDB-TDAACCT.
043918     MOVE TDAA-ALRT3-EXP-DT OF TDAACCT TO TDB-TDAA-ALRT3-EXP-DT   
043920         OF TDB-TDAACCT.
043922     MOVE TDAA-NXT-FEE-DT OF TDAACCT TO TDB-TDAA-NXT-FEE-DT OF    
043924         TDB-TDAACCT.
043926     MOVE TDAA-NXT-POST-DT OF TDAACCT TO TDB-TDAA-NXT-POST-DT OF  
043928         TDB-TDAACCT.
043930     MOVE TDAA-NXT-MAT-DT OF TDAACCT TO TDB-TDAA-NXT-MAT-DT OF    
043932         TDB-TDAACCT.
043934     MOVE TDAA-NXT-DIST-DT OF TDAACCT TO TDB-TDAA-NXT-DIST-DT OF  
043936         TDB-TDAACCT.
043938     MOVE TDAA-NXT-RT-CHG OF TDAACCT TO TDB-TDAA-NXT-RT-CHG OF    
043940         TDB-TDAACCT.
043942     MOVE TDAA-NXT-IN-PROC OF TDAACCT TO TDB-TDAA-NXT-IN-PROC OF  
043944         TDB-TDAACCT.
043946     MOVE TDAA-NXT-CMPD-DT OF TDAACCT TO TDB-TDAA-NXT-CMPD-DT OF  
043948         TDB-TDAACCT.
043950     MOVE TDAA-NXT-STMT-DT OF TDAACCT TO TDB-TDAA-NXT-STMT-DT OF  
043952         TDB-TDAACCT.
043954     MOVE TDAA-NXT-DS-PROC OF TDAACCT TO TDB-TDAA-NXT-DS-PROC OF  
043956         TDB-TDAACCT.
043958     MOVE TDAA-ADV-NTC-DT OF TDAACCT TO TDB-TDAA-ADV-NTC-DT OF    
043960         TDB-TDAACCT.
043962     MOVE TDAA-NXT-29YR-DT OF TDAACCT TO TDB-TDAA-NXT-29YR-DT OF  
043964         TDB-TDAACCT.
043966     MOVE TDAA-FAIR-MRKT-DT OF TDAACCT TO TDB-TDAA-FAIR-MRKT-DT   
043968         OF TDB-TDAACCT.
043970     MOVE TDAA-SORT-FIELD-1 OF TDAACCT TO TDB-TDAA-SORT-FIELD-1   
043972         OF TDB-TDAACCT.
043974     MOVE TDAA-SORT-FIELD-2 OF TDAACCT TO TDB-TDAA-SORT-FIELD-2   
043976         OF TDB-TDAACCT.
043978     MOVE TDAA-SORT-FIELD-3 OF TDAACCT TO TDB-TDAA-SORT-FIELD-3   
043980         OF TDB-TDAACCT.
043982     MOVE TDAA-SORT-FIELD-4 OF TDAACCT TO TDB-TDAA-SORT-FIELD-4   
043984         OF TDB-TDAACCT.
043986     MOVE TDAA-CMAT-PUB-ID OF TDAACCT TO TDB-TDAA-CMAT-PUB-ID OF  
043988         TDB-TDAACCT.
043990     MOVE TDAA-MSA-CONTR OF TDAACCT TO TDB-TDAA-MSA-CONTR OF      
043992         TDB-TDAACCT.
043994     MOVE TDAA-MSA-CONTR-LY OF TDAACCT TO TDB-TDAA-MSA-CONTR-LY   
043996         OF TDB-TDAACCT.
043998     MOVE TDAA-AVG-ACCR-INT OF TDAACCT TO TDB-TDAA-AVG-ACCR-INT   
044000         OF TDB-TDAACCT.
044002     MOVE TDAA-LEVEL-PAY OF TDAACCT TO TDB-TDAA-LEVEL-PAY OF      
044004         TDB-TDAACCT.
044006     MOVE TDAA-ST-INT-CD OF TDAACCT TO TDB-TDAA-ST-INT-CD OF      
044008         TDB-TDAACCT.
044010     MOVE TDAA-ST-WHLD-CD OF TDAACCT TO TDB-TDAA-ST-WHLD-CD OF    
044012         TDB-TDAACCT.
044014     MOVE TDAA-ST-WHLD-AMT OF TDAACCT TO TDB-TDAA-ST-WHLD-AMT OF  
044016         TDB-TDAACCT.
044018     MOVE TDAA-ST-CUR-W-AMT OF TDAACCT TO TDB-TDAA-ST-CUR-W-AMT   
044020         OF TDB-TDAACCT.
044022     MOVE TDAA-ST-LST-W-AMT OF TDAACCT TO TDB-TDAA-ST-LST-W-AMT   
044024         OF TDB-TDAACCT.
044026     MOVE TDAA-ST-WHLD-STD OF TDAACCT TO TDB-TDAA-ST-WHLD-STD OF  
044028         TDB-TDAACCT.
044030     MOVE TDAA-ST-WHLD-YTD OF TDAACCT TO TDB-TDAA-ST-WHLD-YTD OF  
044032         TDB-TDAACCT.
044034     MOVE TDAA-CIF-REMARK OF TDAACCT TO TDB-TDAA-CIF-REMARK OF    
044036         TDB-TDAACCT.
044038     MOVE TDAA-CSR OF TDAACCT TO TDB-TDAA-CSR OF TDB-TDAACCT.
044040     MOVE TDAA-BSA-O-RSK-CD OF TDAACCT TO TDB-TDAA-BSA-O-RSK-CD   
044042         OF TDB-TDAACCT.
044044     MOVE TDAA-BSA-C-RSK-CD OF TDAACCT TO TDB-TDAA-BSA-C-RSK-CD   
044046         OF TDB-TDAACCT.
044048     MOVE TDAA-LRG-TRX-DT OF TDAACCT TO TDB-TDAA-LRG-TRX-DT OF    
044050         TDB-TDAACCT.
044052     MOVE TDAA-HSA-FMLY-IND OF TDAACCT TO TDB-TDAA-HSA-FMLY-IND   
044054         OF TDB-TDAACCT.
044056     MOVE TDAA-STOP-PAY-IND OF TDAACCT TO TDB-TDAA-STOP-PAY-IND   
044058         OF TDB-TDAACCT.
044060     MOVE TDAA-IMG-PG-TYPE OF TDAACCT TO TDB-TDAA-IMG-PG-TYPE OF  
044062         TDB-TDAACCT.
044064     MOVE TDAA-CONT-LMT-CLC OF TDAACCT TO TDB-TDAA-CONT-LMT-CLC   
044066         OF TDB-TDAACCT.
044068     MOVE TDAA-CONT-LMT-ENT OF TDAACCT TO TDB-TDAA-CONT-LMT-ENT   
044070         OF TDB-TDAACCT.
044072     MOVE TDAA-MEMO-DB OF TDAACCT TO TDB-TDAA-MEMO-DB OF          
044074         TDB-TDAACCT.
044076     MOVE TDAA-MEMO-CR OF TDAACCT TO TDB-TDAA-MEMO-CR OF          
044078         TDB-TDAACCT.
044080     MOVE TDAA-MEMO-DB-2 OF TDAACCT TO TDB-TDAA-MEMO-DB-2 OF      
044082         TDB-TDAACCT.
044084     MOVE TDAA-MEMO-CR-2 OF TDAACCT TO TDB-TDAA-MEMO-CR-2 OF      
044086         TDB-TDAACCT.
044088     MOVE TDAA-RT-AT-CONV OF TDAACCT TO TDB-TDAA-RT-AT-CONV OF    
044090         TDB-TDAACCT.
044092     MOVE TDAA-ACCR-AT-CONV OF TDAACCT TO TDB-TDAA-ACCR-AT-CONV   
044094         OF TDB-TDAACCT.
044096     MOVE TDAA-RT-AT-ACRDT OF TDAACCT TO TDB-TDAA-RT-AT-ACRDT OF  
044098         TDB-TDAACCT.
044100     MOVE TDAA-BAL-AT-ACRDT OF TDAACCT TO TDB-TDAA-BAL-AT-ACRDT   
044102         OF TDB-TDAACCT.
044104     MOVE TDAA-ZERO-RT-ALLOW OF TDAACCT TO TDB-TDAA-ZERO-RT-ALLOW 
044106         OF TDB-TDAACCT.
044108     MOVE TDAA-EMAIL-NTC OF TDAACCT TO TDB-TDAA-EMAIL-NTC OF      
044110         TDB-TDAACCT.
044112     MOVE TDAA-EMAIL-STMT OF TDAACCT TO TDB-TDAA-EMAIL-STMT OF    
044114         TDB-TDAACCT.
044116     MOVE TDAA-FRAUD-CK-DT OF TDAACCT TO TDB-TDAA-FRAUD-CK-DT OF  
044118         TDB-TDAACCT.
044120     MOVE TDAA-FRAUD-CK-CNT OF TDAACCT TO TDB-TDAA-FRAUD-CK-CNT   
044122         OF TDB-TDAACCT.
044124     MOVE TDAA-FRAUD-CK-AMT OF TDAACCT TO TDB-TDAA-FRAUD-CK-AMT   
044126         OF TDB-TDAACCT.
044128     MOVE TDAA-MISC-ACCTNO OF TDAACCT TO TDB-TDAA-MISC-ACCTNO OF  
044130         TDB-TDAACCT.
044132     MOVE TDAA-RMD-MAN-CALC OF TDAACCT TO TDB-TDAA-RMD-MAN-CALC   
044134         OF TDB-TDAACCT.
044136     MOVE TDAA-RMD-AMOUNT OF TDAACCT TO TDB-TDAA-RMD-AMOUNT OF    
044138         TDB-TDAACCT.
044140     MOVE TDAA-BROKERAGE-ID OF TDAACCT TO TDB-TDAA-BROKERAGE-ID   
044142         OF TDB-TDAACCT.
044144     MOVE TDAA-EV-LARGE-TRX OF TDAACCT TO TDB-TDAA-EV-LARGE-TRX   
044146         OF TDB-TDAACCT.
044148     MOVE TDAA-EV-MAT-AMT OF TDAACCT TO TDB-TDAA-EV-MAT-AMT OF    
044150         TDB-TDAACCT.
044152     MOVE TDAA-EV-DISP-ACCT OF TDAACCT TO TDB-TDAA-EV-DISP-ACCT   
044154         OF TDB-TDAACCT.
044156     MOVE TDAA-EV-COMP-ACCT OF TDAACCT TO TDB-TDAA-EV-COMP-ACCT   
044158         OF TDB-TDAACCT.
044160     MOVE TDAA-EV-PUBLIC-ID OF TDAACCT TO TDB-TDAA-EV-PUBLIC-ID   
044162         OF TDB-TDAACCT.
044164     MOVE TDAA-EV-MAT-TYPE OF TDAACCT TO TDB-TDAA-EV-MAT-TYPE OF  
044166         TDB-TDAACCT.
044168     MOVE TDAA-EV-INT-TYPE OF TDAACCT TO TDB-TDAA-EV-INT-TYPE OF  
044170         TDB-TDAACCT.
044172     MOVE TDAA-EV-ACCT-TYP OF TDAACCT TO TDB-TDAA-EV-ACCT-TYP OF  
044174         TDB-TDAACCT.
044176     MOVE TDAA-EV-WHLD-PCT OF TDAACCT TO TDB-TDAA-EV-WHLD-PCT OF  
044178         TDB-TDAACCT.
044180     MOVE TDAA-EV-NON-ACCR OF TDAACCT TO TDB-TDAA-EV-NON-ACCR OF  
044182         TDB-TDAACCT.
044184     MOVE TDAA-EV-CLOSED OF TDAACCT TO TDB-TDAA-EV-CLOSED OF      
044186         TDB-TDAACCT.
044188     MOVE TDAA-EV-CLOSE-MO OF TDAACCT TO TDB-TDAA-EV-CLOSE-MO OF  
044190         TDB-TDAACCT.
044192     MOVE TDAA-EV-OPEN-MO OF TDAACCT TO TDB-TDAA-EV-OPEN-MO OF    
044194         TDB-TDAACCT.
044196     MOVE TDAA-EV-ANN-INT OF TDAACCT TO TDB-TDAA-EV-ANN-INT OF    
044198         TDB-TDAACCT.
044200     MOVE TDAA-EV-ORIG-RT OF TDAACCT TO TDB-TDAA-EV-ORIG-RT OF    
044202         TDB-TDAACCT.
044204     MOVE TDAA-EV-DLY-INT OF TDAACCT TO TDB-TDAA-EV-DLY-INT OF    
044206         TDB-TDAACCT.
044208     MOVE TDAA-EV-INT-PAY OF TDAACCT TO TDB-TDAA-EV-INT-PAY OF    
044210         TDB-TDAACCT.
044212     MOVE TDAA-EV-AVAIL-BL OF TDAACCT TO TDB-TDAA-EV-AVAIL-BL OF  
044214         TDB-TDAACCT.
044216     MOVE TDAA-EV-RETAIN OF TDAACCT TO TDB-TDAA-EV-RETAIN OF      
044218         TDB-TDAACCT.
044220     MOVE TDAA-EV-CL-RETAIN OF TDAACCT TO TDB-TDAA-EV-CL-RETAIN   
044222         OF TDB-TDAACCT.
044224     MOVE TDAA-EV-TIMES-REN OF TDAACCT TO TDB-TDAA-EV-TIMES-REN   
044226         OF TDB-TDAACCT.
044228     MOVE TDAA-EV-CURR-BAL OF TDAACCT TO TDB-TDAA-EV-CURR-BAL OF  
044230         TDB-TDAACCT.
044232     MOVE TDAA-MONY-SRC-CD2 OF TDAACCT TO TDB-TDAA-MONY-SRC-CD2   
044234         OF TDB-TDAACCT.
044236     MOVE TDAA-INHERIT-IRA OF TDAACCT TO TDB-TDAA-INHERIT-IRA OF  
044238         TDB-TDAACCT.
044240     MOVE TDAA-LIFE-FACTOR OF TDAACCT TO TDB-TDAA-LIFE-FACTOR OF  
044242         TDB-TDAACCT.
044244     MOVE TDAA-BRKR-DEP-CAT OF TDAACCT TO TDB-TDAA-BRKR-DEP-CAT   
044246         OF TDB-TDAACCT.
044248     MOVE TDAA-LINE-OF-BUS OF TDAACCT TO TDB-TDAA-LINE-OF-BUS OF  
044250         TDB-TDAACCT.
044252     MOVE TDAA-1ST-STMT OF TDAACCT TO TDB-TDAA-1ST-STMT OF        
```

⚠️  This is the source code you must document.
    397 lines from 21726 to 22122.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

