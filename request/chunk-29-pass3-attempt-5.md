# LLM Request Debug File
Generated: 2025-11-17T21:20:03.540378

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 29/55
- **Model**: gpt-4.1
- **Chunk Number**: 29
- **Pass Number**: 3
- **Attempt Number**: 5 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~7,647 tokens
- **Total Input**: ~9,605 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 29/55" (ID: detailed-code-explanation)

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


**CHUNK 29 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-17T19:50:50.832678", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 29 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 13673 to 14252 (580 lines)\nChunk Tokens (estimated): ~8,063\nActual Input Tokens: 9,469 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 13673-14252 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 29 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 29 of 55.\n\n\n=============================================================================\nCHUNK 29 SOURCE CODE (Lines 13673-14252)\n=============================================================================\n\n```cobol\n027354 Z-DATE-CALC-LEAP-YEAR.\n027356     MOVE Z-DATE-CC-1        TO Z-DATE-FORMAT-CC.\n027358     MOVE Z-DATE-YY-1        TO Z-DATE-FORMAT-YY.\n027360     MOVE Z-DATE-FORMAT-CCYY TO Z-DATE-YEAR-WORK.\n027362     DIVIDE Z-DATE-YEAR-WORK BY +4 GIVING Z-DATE-DIVIDE-WORK\n027364         REMAINDER Z-DATE-YEAR-MOD-4.\n027366     DIVIDE Z-DATE-YEAR-WORK BY +100 GIVING Z-DATE-DIVIDE-WORK\n027368         REMAINDER Z-DATE-YEAR-MOD-100.\n027370     DIVIDE Z-DATE-YEAR-WORK BY +400 GIVING Z-DATE-DIVIDE-WORK\n027372         REMAINDER Z-DATE-YEAR-MOD-400.\n027374     IF Z-DATE-YEAR-MOD-4 = ZERO\n027376         IF Z-DATE-YEAR-MOD-100 NOT = ZERO OR\n027378            Z-DATE-YEAR-MOD-400 = ZERO\n027380              SET Z-DATE-MM-I TO +2\n027382              MOVE 29 TO Z-DATE-TBL-DAYS-IN-MON ( Z-DATE-MM-I )\n027384              MOVE +1 TO Z-DATE-LEAP-YR-FLAG\n027386              GO TO Z-DATE-CALC-LEAP-YEAR-EXIT.\n027388     SET Z-DATE-MM-I TO +2.\n027390     MOVE 28 TO Z-DATE-TBL-DAYS-IN-MON ( Z-DATE-MM-I ).\n027392     MOVE +0 TO Z-DATE-LEAP-YR-FLAG.\n027394*\n027396 Z-DATE-CALC-LEAP-YEAR-EXIT.\n027398     EXIT.\n027400*\n027402 Z-DATE-CALC-MONTH-DAYS.\n027404*    FIX THE DAYS IF > THAN DAYS IN MONTH\n027406     IF Z-DATE-DD-1 > 0 AND Z-DATE-MM-1 > 0 AND Z-DATE-MM-1 < +13\n027408        IF Z-DATE-DD-1 > Z-DATE-TBL-DAYS-IN-MON ( Z-DATE-MM-1 )\n027410           MOVE Z-DATE-TBL-DAYS-IN-MON ( Z-DATE-MM-1 ) TO\n027412                Z-DATE-DD-1\n027414           PERFORM Z-DATE-MDY-TO-JUL-CTRL\n027416              THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT\n027418           MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.\n027420*\n027422 Z-DATE-CALC-MONTH-DAYS-EXIT.\n027424     EXIT.\n027426*\n027428 Z-DATE-MDY-TO-JUL-CTRL.\n027430     MOVE ZEROS TO Z-DATE-ACCUM.\n027432     MOVE ZEROS TO Z-DATE-JJJ-3.\n027434     IF Z-DATE-MM-1 > +12\n027436         MOVE 12 TO Z-DATE-MONTH-LIMIT\n027438     ELSE\n027440         SUBTRACT +1 FROM Z-DATE-MM-1\n027442           GIVING Z-DATE-MONTH-LIMIT.\n027444     PERFORM Z-DATE-CONVERT-MDY-TO-JUL\n027446        THRU Z-DATE-CONVERT-MDY-TO-JUL-EXIT\n027448     VARYING Z-DATE-MM-I FROM +1 BY +1\n027450        UNTIL Z-DATE-MM-I > Z-DATE-MONTH-LIMIT.\n027452     ADD Z-DATE-DD-1 TO Z-DATE-JJJ-3.\n027454     MOVE Z-DATE-CC-1 TO Z-DATE-CC-3.\n027456     MOVE Z-DATE-YY-1 TO Z-DATE-YY-3.\n027458     ADD Z-DATE-ACCUM TO Z-DATE-JJJ-3.\n027460 Z-DATE-MDY-TO-JUL-CTRL-EXIT.\n027462     EXIT.\n027464*\n027466 Z-DATE-CONVERT-MDY-TO-JUL.\n027468     ADD Z-DATE-ACCUM, Z-DATE-TBL-DAYS-IN-MON ( Z-DATE-MM-I )\n027470       GIVING Z-DATE-ACCUM.\n027472 Z-DATE-CONVERT-MDY-TO-JUL-EXIT.\n027474     EXIT.\n027476*\n027478 Z-DATE-CC-DIFF.\n027480     SUBTRACT Z-DATE-CC-1 FROM Z-DATE-CC-2 GIVING Z-DATE-C.\n027482 Z-DATE-CC-DIFF-EXIT.\n027484     EXIT.\n027486*\n027488 Z-DATE-YY-DIFF.\n027490     COMPUTE Z-DATE-Y = (( Z-DATE-CC-2 * 100 ) + Z-DATE-YY-2 )\n027492                      - (( Z-DATE-CC-1 * 100 ) + Z-DATE-YY-1 ).\n027494 Z-DATE-YY-DIFF-EXIT.\n027496     EXIT.\n027498*\n027500 Z-DATE-INITIALIZE-REGS.\n027502     PERFORM Z-DATE-INIT-DATE-1\n027504        THRU Z-DATE-INIT-DATE-1-EXIT.\n027506     PERFORM Z-DATE-INIT-DATE-2\n027508        THRU Z-DATE-INIT-DATE-2-EXIT.\n027510     PERFORM Z-DATE-INIT-DATE-3\n027512        THRU Z-DATE-INIT-DATE-3-EXIT.\n027514 Z-DATE-INITIALIZE-REGS-EXIT.\n027516     EXIT.\n027518*\n027520 Z-DATE-INITIALIZE-CTRL.\n027522     PERFORM Z-DATE-INIT-UNITS\n027524        THRU Z-DATE-INIT-UNITS-EXIT.\n027526     PERFORM Z-DATE-INIT-MATH-WA\n027528        THRU Z-DATE-INIT-MATH-WA-EXIT.\n027530     PERFORM Z-DATE-INIT-JUL-MDY\n027532        THRU Z-DATE-INIT-JUL-MDY-EXIT.\n027534     PERFORM Z-DATE-INIT-LEAP-YR\n027536        THRU Z-DATE-INIT-LEAP-YR-EXIT.\n027538     PERFORM Z-DATE-INIT-CVRT-STATUS\n027540        THRU Z-DATE-INIT-CVRT-STATUS-EXIT.\n027542*\n027544 Z-DATE-INITIALIZE-CTRL-EXIT.\n027546     EXIT.\n027548*\n027550 Z-DATE-INIT-DATE-1.\n027552     MOVE ZEROS  TO Z-DATE-CC-1.\n027554     MOVE ZEROS  TO Z-DATE-YY-1.\n027556     MOVE ZEROS  TO Z-DATE-MM-1.\n027558     MOVE ZEROS  TO Z-DATE-DD-1.\n027560     MOVE ZEROS  TO Z-DATE-JJJ-1.\n027562     MOVE ZEROS  TO Z-DATE-HH-1.\n027564     MOVE ZEROS  TO Z-DATE-UU-1.\n027566     MOVE ZEROS  TO Z-DATE-SS-1.\n027568     MOVE ZEROS  TO Z-DATE-TT-1.\n027570     MOVE ZEROS  TO Z-DATE-ZZ-1.\n027572     MOVE ZEROS  TO Z-DATE-AP-1.\n027574     MOVE ZEROS  TO Z-DATE-MX-1.\n027576     MOVE SPACES TO Z-DATE-CHARS-1.\n027578 Z-DATE-INIT-DATE-1-EXIT.\n027580     EXIT.\n027582*\n027584 Z-DATE-INIT-DATE-2.\n027586     MOVE ZEROS  TO Z-DATE-CC-2.\n027588     MOVE ZEROS  TO Z-DATE-YY-2.\n027590     MOVE ZEROS  TO Z-DATE-MM-2.\n027592     MOVE ZEROS  TO Z-DATE-DD-2.\n027594     MOVE ZEROS  TO Z-DATE-JJJ-2.\n027596     MOVE ZEROS  TO Z-DATE-HH-2.\n027598     MOVE ZEROS  TO Z-DATE-UU-2.\n027600     MOVE ZEROS  TO Z-DATE-SS-2.\n027602     MOVE ZEROS  TO Z-DATE-TT-2.\n027604     MOVE ZEROS  TO Z-DATE-ZZ-2.\n027606     MOVE ZEROS  TO Z-DATE-AP-2.\n027608     MOVE ZEROS  TO Z-DATE-MX-2.\n027610     MOVE SPACES TO Z-DATE-CHARS-2.\n027612 Z-DATE-INIT-DATE-2-EXIT.\n027614     EXIT.\n027616*\n027618 Z-DATE-INIT-DATE-3.\n027620     MOVE ZEROS  TO Z-DATE-CC-3.\n027622     MOVE ZEROS  TO Z-DATE-YY-3.\n027624     MOVE ZEROS  TO Z-DATE-MM-3.\n027626     MOVE ZEROS  TO Z-DATE-DD-3.\n027628     MOVE ZEROS  TO Z-DATE-JJJ-3.\n027630     MOVE ZEROS  TO Z-DATE-HH-3.\n027632     MOVE ZEROS  TO Z-DATE-UU-3.\n027634     MOVE ZEROS  TO Z-DATE-SS-3.\n027636     MOVE ZEROS  TO Z-DATE-TT-3.\n027638     MOVE ZEROS  TO Z-DATE-ZZ-3.\n027640     MOVE ZEROS  TO Z-DATE-AP-3.\n027642     MOVE ZEROS  TO Z-DATE-MX-3.\n027644     MOVE SPACES TO Z-DATE-CHARS-3.\n027646 Z-DATE-INIT-DATE-3-EXIT.\n027648     EXIT.\n027650*\n027652 Z-DATE-INIT-UNITS.\n027654     MOVE ZEROS  TO Z-DATE-C.\n027656     MOVE ZEROS  TO Z-DATE-Y.\n027658     MOVE ZEROS  TO Z-DATE-M.\n027660     MOVE ZEROS  TO Z-DATE-D.\n027662     MOVE ZEROS  TO Z-DATE-W.\n027664     MOVE ZEROS  TO Z-DATE-Z.\n027666     MOVE ZEROS  TO Z-DATE-U.\n027668     MOVE ZEROS  TO Z-DATE-S.\n027670     MOVE ZEROS  TO Z-DATE-T.\n027672 Z-DATE-INIT-UNITS-EXIT.\n027674     EXIT.\n027676*\n027678 Z-DATE-INIT-MATH-WA.\n027680     MOVE ZEROS  TO Z-DATE-UNITS-WORK.\n027682     MOVE ZEROS  TO Z-DATE-FORMAT-CEN.\n027684     MOVE ZEROS  TO Z-DATE-FORMAT-YR.\n027686     MOVE ZEROS  TO Z-DATE-FORMAT-DAYS.\n027688     MOVE ZEROS  TO Z-DATE-JUL-YR-WORK.\n027690     MOVE ZEROS  TO Z-DATE-JULIAN-WORK.\n027692     MOVE ZEROS  TO Z-DATE-X-TO-9.\n027694     MOVE ZEROS  TO Z-DATE-NEG-INDICATOR.\n027696     MOVE ZEROS  TO Z-DATE-JULIAN-1.\n027698     MOVE ZEROS  TO Z-DATE-JULIAN-2.\n027700     MOVE ZEROS  TO Z-DATE-TEMP-HOLD.\n027702     MOVE ZEROS  TO Z-DATE-HOLD-JJJ.\n027704     MOVE ZEROS  TO Z-DATE-JJJ-1-WORK.\n027706     MOVE ZEROS  TO Z-DATE-JJJ-2-WORK.\n027708     MOVE ZEROS  TO Z-DATE-WORK-YR-1.\n027710     MOVE ZEROS  TO Z-DATE-WORK-YR-2.\n027712     MOVE ZEROS  TO Z-DATE-HOLD-YEAR.\n027714 Z-DATE-INIT-MATH-WA-EXIT.\n027716     EXIT.\n027718*\n027720 Z-DATE-INIT-JUL-MDY.\n027722     MOVE ZEROS  TO Z-DATE-MDY-STRING.\n027724     MOVE ZEROS  TO Z-DATE-ACCUM.\n027726     MOVE ZEROS  TO Z-DATE-MONTH-LIMIT.\n027728 Z-DATE-INIT-JUL-MDY-EXIT.\n027730     EXIT.\n027732*\n027734 Z-DATE-INIT-LEAP-YR.\n027736     MOVE ZEROS  TO Z-DATE-FORMAT-CC.\n027738     MOVE ZEROS  TO Z-DATE-FORMAT-YY.\n027740     MOVE ZEROS  TO Z-DATE-FORMAT-YEAR.\n027742     MOVE ZEROS  TO Z-DATE-YEAR-WORK.\n027744     MOVE ZEROS  TO Z-DATE-DIVIDE-WORK.\n027746     MOVE ZEROS  TO Z-DATE-QUOTIENT.\n027748     MOVE ZEROS  TO Z-DATE-REMAINDER.\n027750     MOVE ZEROS  TO Z-DATE-YEAR-MOD-4.\n027752     MOVE ZEROS  TO Z-DATE-YEAR-MOD-100.\n027754     MOVE ZEROS  TO Z-DATE-YEAR-MOD-400.\n027756     MOVE ZEROS  TO Z-DATE-LEAP-YR-FLAG.\n027758 Z-DATE-INIT-LEAP-YR-EXIT.\n027760     EXIT.\n027762*\n027764 Z-DATE-INIT-CVRT-STATUS.\n027766     MOVE ZEROS  TO Z-DATE-CONVERT-STATUS.\n027768 Z-DATE-INIT-CVRT-STATUS-EXIT.\n027770     EXIT.\n027772*\n027774*****************************************************************\n027776*Z-USERS-DECLARATIONS SECTION.\n027778*****************************************************************\n027780*\n027782*Z-USERS-DECLARATIONS-PARAGRAPH.\n027784*\n027786*\n027788****************************************************************\n027790* EACH-HEADING FOR REPORT LISTING\n027792****************************************************************\n027794 Z-1-PROCEDURE.\n027796\n027798     MOVE 1 TO Z-RPTINFO1-INBLOCK.\n027800     MOVE Z-RPT-1-PAGE TO WS-PAGE-CNT.\n027802     MOVE \"TDA-700\" TO H-REPORT-NO.\n027804     MOVE \"RMD CALCULATION REPORT\" TO H-RPT-TITLE.\n027806     MOVE SPACES TO HEADER-PAGE.\n027808     IF H-PAGE-CST-160 = SPACES\n027810         NEXT SENTENCE\n027812     ELSE\n027814         GO TO Z-1-4-END-MOVE.\n027816     MOVE \"PAGE\" TO H-PAGE-CST-160.\n027818 Z-1-4-END-MOVE.\n027820     MOVE WS-PAGE-CNT TO H-PAGE-NO-160.\n027822     IF HDR-CTL NOT = 0\n027824         NEXT SENTENCE ELSE\n027826         GO TO Z-1-6-1-ELSE.\n027828     MOVE 1 TO Z-RPT-1-LINE.\n027830     MOVE HEADER-LINE1 TO Z-RPT-1-BUFFER.\n027832     WRITE Z-RPT-1-BUFFER AFTER ADVANCING PAGE.\n027834     COMPUTE Z-LINES-HOLD = 1.\n027836     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES-HOLD).\n027838     IF Z-RPT-1-LINE > Z-RPT-1-PAGE-SIZE\n027840         SUBTRACT Z-RPT-1-PAGE-SIZE FROM Z-RPT-1-LINE.\n027842     MOVE PRINT-SPACES-160 TO Z-RPT-1-BUFFER.\n027844     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES-HOLD.\n027846 Z-1-6-1-ELSE.\n027848     MOVE RMDRPT-REC-2 TO HEADER-LINE2-160.\n027850     MOVE RMDRPT-REC-6 TO HEADER-LINE3-160.\n027852     IF HDR-CTL > 1\n027854         NEXT SENTENCE ELSE\n027856         GO TO Z-1-11-1-ELSE.\n027858     COMPUTE Z-LINES-HOLD = 1.\n027860     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES-HOLD).\n027862     IF Z-RPT-1-LINE > Z-RPT-1-PAGE-SIZE\n027864         SUBTRACT Z-RPT-1-PAGE-SIZE FROM Z-RPT-1-LINE.\n027866     MOVE HEADER-LINE2-160 TO Z-RPT-1-BUFFER.\n027868     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES-HOLD.\n027870 Z-1-11-1-ELSE.\n027872     IF HDR-CTL > 2\n027874         NEXT SENTENCE ELSE\n027876         GO TO Z-1-13-1-ELSE.\n027878     COMPUTE Z-LINES-HOLD = 1.\n027880     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES-HOLD).\n027882     IF Z-RPT-1-LINE > Z-RPT-1-PAGE-SIZE\n027884         SUBTRACT Z-RPT-1-PAGE-SIZE FROM Z-RPT-1-LINE.\n027886     MOVE HEADER-LINE3-160 TO Z-RPT-1-BUFFER.\n027888     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES-HOLD.\n027890 Z-1-13-1-ELSE.\n027892     IF HDR-CTL > 3\n027894         NEXT SENTENCE ELSE\n027896         GO TO Z-1-15-1-ELSE.\n027898     COMPUTE Z-LINES-HOLD = 1.\n027900     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES-HOLD).\n027902     IF Z-RPT-1-LINE > Z-RPT-1-PAGE-SIZE\n027904         SUBTRACT Z-RPT-1-PAGE-SIZE FROM Z-RPT-1-LINE.\n027906     MOVE HEADER-LINE4-160 TO Z-RPT-1-BUFFER.\n027908     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES-HOLD.\n027910 Z-1-15-1-ELSE.\n027912     IF Z-EDIT-ERROR\n027914         MOVE 0 TO Z-RPTINFO1-INBLOCK\n027916         GO TO Z-1-XIT.\n027918 Z-1-SKIP.\n027920     MOVE 0 TO Z-RPTINFO1-INBLOCK.\n027922 Z-1-XIT.\n027924     EXIT.\n027926*\n027928*****************************************************************\n027930*    SUPPORT ROUTINES FOR REPORT LISTING\n027932*****************************************************************\n027934*\n027936 Z-RPT-1-ADV-PAGE-CNT.\n027938     ADD 1 TO Z-RPT-1-PAGE.\n027940*\n027942 Z-RPT-1-NEWPAGE.\n027944     PERFORM Z-RPT-1-ADV-PAGE-CNT.\n027946*\n027948************ REPORT 1 EACH HEADING\n027950     PERFORM Z-1-PROCEDURE THRU Z-1-XIT.\n027952*\n027954 Z-RPT-1-SET-TRAP.\n027956     IF Z-RPT-1-LINE > (Z-RPT-1-PAGE-SIZE - 1)\n027958         COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE - (Z-RPT-1-PAGE-SIZE \n027960             - 1).\n027962     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n027964*\n027966 Z-RPT-1-NEWPAGE-XIT.\n027968     EXIT.\n027970*\n027972*\n027974*\n027976****************************************************************\n027978* EACH-HEADING FOR REPORT FICHE\n027980****************************************************************\n027982 Z-2-PROCEDURE.\n027984\n027986     MOVE 1 TO Z-RPTINFO2-INBLOCK.\n027988     MOVE Z-RPT-2-PAGE TO WS-PAGE-CNT-FICHE.\n027990     MOVE \"TDA-701\" TO H-REPORT-NO.\n027992     MOVE \"RMD CALCULATION REPORT FOR INHERITED IRA'S\" TO         \n027994         H-RPT-TITLE.\n027996     MOVE SPACES TO HEADER-PAGE.\n027998     IF H-PAGE-CST-160 = SPACES\n028000         NEXT SENTENCE\n028002     ELSE\n028004         GO TO Z-2-4-END-MOVE.\n028006     MOVE \"PAGE\" TO H-PAGE-CST-160.\n028008 Z-2-4-END-MOVE.\n028010     MOVE WS-PAGE-CNT-FICHE TO H-PAGE-NO-160.\n028012     IF HDR-CTL NOT = 0\n028014         NEXT SENTENCE ELSE\n028016         GO TO Z-2-6-1-ELSE.\n028018     MOVE 1 TO Z-RPT-2-LINE.\n028020     MOVE HEADER-LINE1 TO Z-RPT-2-BUFFER.\n028022     WRITE Z-RPT-2-BUFFER AFTER ADVANCING PAGE.\n028024     COMPUTE Z-LINES-HOLD = 1.\n028026     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES-HOLD).\n028028     IF Z-RPT-2-LINE > Z-RPT-2-PAGE-SIZE\n028030         SUBTRACT Z-RPT-2-PAGE-SIZE FROM Z-RPT-2-LINE.\n028032     MOVE PRINT-SPACES-160 TO Z-RPT-2-BUFFER.\n028034     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES-HOLD.\n028036 Z-2-6-1-ELSE.\n028038     MOVE RMDRPT2-REC-2 TO HEADER-LINE2-160.\n028040     MOVE RMDRPT2-REC-6 TO HEADER-LINE3-160.\n028042     IF HDR-CTL > 1\n028044         NEXT SENTENCE ELSE\n028046         GO TO Z-2-11-1-ELSE.\n028048     COMPUTE Z-LINES-HOLD = 1.\n028050     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES-HOLD).\n028052     IF Z-RPT-2-LINE > Z-RPT-2-PAGE-SIZE\n028054         SUBTRACT Z-RPT-2-PAGE-SIZE FROM Z-RPT-2-LINE.\n028056     MOVE HEADER-LINE2-160 TO Z-RPT-2-BUFFER.\n028058     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES-HOLD.\n028060 Z-2-11-1-ELSE.\n028062     IF HDR-CTL > 2\n028064         NEXT SENTENCE ELSE\n028066         GO TO Z-2-13-1-ELSE.\n028068     COMPUTE Z-LINES-HOLD = 1.\n028070     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES-HOLD).\n028072     IF Z-RPT-2-LINE > Z-RPT-2-PAGE-SIZE\n028074         SUBTRACT Z-RPT-2-PAGE-SIZE FROM Z-RPT-2-LINE.\n028076     MOVE HEADER-LINE3-160 TO Z-RPT-2-BUFFER.\n028078     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES-HOLD.\n028080 Z-2-13-1-ELSE.\n028082     IF HDR-CTL > 3\n028084         NEXT SENTENCE ELSE\n028086         GO TO Z-2-15-1-ELSE.\n028088     COMPUTE Z-LINES-HOLD = 1.\n028090     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES-HOLD).\n028092     IF Z-RPT-2-LINE > Z-RPT-2-PAGE-SIZE\n028094         SUBTRACT Z-RPT-2-PAGE-SIZE FROM Z-RPT-2-LINE.\n028096     MOVE HEADER-LINE4-160 TO Z-RPT-2-BUFFER.\n028098     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES-HOLD.\n028100 Z-2-15-1-ELSE.\n028102     IF Z-EDIT-ERROR\n028104         MOVE 0 TO Z-RPTINFO2-INBLOCK\n028106         GO TO Z-2-XIT.\n028108 Z-2-SKIP.\n028110     MOVE 0 TO Z-RPTINFO2-INBLOCK.\n028112 Z-2-XIT.\n028114     EXIT.\n028116*\n028118*****************************************************************\n028120*    SUPPORT ROUTINES FOR REPORT FICHE\n028122*****************************************************************\n028124*\n028126 Z-RPT-2-ADV-PAGE-CNT.\n028128     ADD 1 TO Z-RPT-2-PAGE.\n028130*\n028132 Z-RPT-2-NEWPAGE.\n028134     PERFORM Z-RPT-2-ADV-PAGE-CNT.\n028136*\n028138************ REPORT 2 EACH HEADING\n028140     PERFORM Z-2-PROCEDURE THRU Z-2-XIT.\n028142*\n028144 Z-RPT-2-SET-TRAP.\n028146     IF Z-RPT-2-LINE > (Z-RPT-2-PAGE-SIZE - 1)\n028148         COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE - (Z-RPT-2-PAGE-SIZE \n028150             - 1).\n028152     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.\n028154*\n028156 Z-RPT-2-NEWPAGE-XIT.\n028158     EXIT.\n028160*\n028162*\n028164*\n028166*****************************************************************\n028168 Z-USERS-ROUTINES SECTION.\n028170*****************************************************************\n028172*\n028174 Z-USERS-ROUTINES-PARAGRAPH.\n028176*\n028178*\n028180*****************************************************************\n028182*    PROCESS MAIN\n028184*****************************************************************\n028186*\n028188 Z-3-PROCESS.\n028190*\n028192     MOVE 1 TO Z-PROCESS-FLAG.\n028194     MOVE \"MAIN\" TO Z-PROCESS-NAME.\n028196     MOVE 0 TO Z-CONTINUE-FLAG.\n028198     IF Z-RESTART-FLAG = 1\n028200         MOVE ZERO TO Z-RESTART-FLAG\n028202         GO TO Z-3-RESTART.\n028204     MOVE ZERO TO Z-RESTART-POINT.\n028206     MOVE 3 TO Z-RESTART-PROCESS.\n028208 MOVE ATTRIBUTE HOSTNAME OF MYSELF TO WS-WORK-AREA-HOST.          \n028210 STRING WS-WORK-AREA-HOST DELIMITED BY \".\" INTO WS-SYS-HOST.      \n028212     MOVE 0 TO Z-EXIT-CODE.\n028214     MOVE 9999 TO Z-EXIT-LEVEL.\n028216*    RETRIEVE TODAY'S DATE\n028218     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n028220          USING Z-CALL-CURRENTDATE.\n028222     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n028224     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n028226     ACCEPT Z-DATE0-TIME   FROM TIME.\n028228     MOVE Z-DATE0-CC TO Z-DATE2-CC.\n028230     MOVE Z-DATE0-YY TO Z-DATE2-YY.\n028232     MOVE Z-DATE0-MM TO Z-DATE2-MM.\n028234     MOVE Z-DATE0-DD TO Z-DATE2-DD.\n028236     MOVE Z-DATE2-FORMAT-9 TO PROCESS-DATE.\n028238     MOVE ZERO TO Z-FLINFO7-PRES.\n028240     MOVE 1 TO Z-FLINFO7-LAST-SEQ.\n028242     MOVE ZERO TO Z-FLINFO7-SOME.\n028244     SET SPCPRTALL OF SPCPRT OF LDBSPCDB TO ENDING\n028246         ON EXCEPTION\n028248         MOVE \"SPCPRTALL OF SPCPRT OF LDBSPCDB\" TO                \n028250             Z-DMS-EXCEPT-STR\n028252         MOVE \"LDBSPCDB\" TO Z-DMS-EXCEPT-DB\n028254         MOVE 1 TO Z-DMS-EXCEPT-SEQ\n028256         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT\n028258         GO TO Z-3-2-XIT.\n028260 Z-3-2-READ.\n028262     FIND SPCPRT OF LDBSPCDB VIA PRIOR SPCPRTALL OF SPCPRT OF     \n028264         LDBSPCDB\n028266         ON EXCEPTION\n028268         MOVE 1 TO Z-DMS-EXCEPT-SEQ\n028270         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n028272             GO TO Z-3-2-XIT\n028274         ELSE\n028276             MOVE \"SPCPRTALL OF SPCPRT OF LDBSPCDB\" TO            \n028278                 Z-DMS-EXCEPT-STR\n028280             MOVE \"LDBSPCDB\" TO Z-DMS-EXCEPT-DB\n028282             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n028284\n028286 Z-3-2-PRESENT.\n028288*\n028290     MOVE 1 TO Z-FLINFO7-SOME.\n028292     MOVE 1 TO Z-FLINFO7-PRES.\n028294     GO TO Z-3-2-CONT.\n028296 Z-3-2-XIT.\n028298 Z-3-2-CONT.\n028300     MOVE ZERO TO Z-FLINFO7-PRES.\n028302     MOVE 2 TO Z-FLINFO7-LAST-SEQ.\n028304     MOVE ZERO TO Z-FLINFO7-SOME.\n028306     SET SPCPRTCURR OF SPCPRT OF LDBSPCDB TO ENDING\n028308         ON EXCEPTION\n028310         MOVE \"SPCPRTCURR OF SPCPRT OF LDBSPCDB\" TO               \n028312             Z-DMS-EXCEPT-STR\n028314         MOVE \"LDBSPCDB\" TO Z-DMS-EXCEPT-DB\n028316         MOVE 2 TO Z-DMS-EXCEPT-SEQ\n028318         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT\n028320         GO TO Z-3-3-XIT.\n028322 Z-3-3-READ.\n028324     FIND SPCPRT OF LDBSPCDB VIA PRIOR SPCPRTCURR OF SPCPRT OF    \n028326         LDBSPCDB\n028328         ON EXCEPTION\n028330         MOVE 2 TO Z-DMS-EXCEPT-SEQ\n028332         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n028334             GO TO Z-3-3-XIT\n028336         ELSE\n028338             MOVE \"SPCPRTCURR OF SPCPRT OF LDBSPCDB\" TO           \n028340                 Z-DMS-EXCEPT-STR\n028342             MOVE \"LDBSPCDB\" TO Z-DMS-EXCEPT-DB\n028344             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n028346\n028348 Z-3-3-PRESENT.\n028350*\n028352     MOVE 1 TO Z-FLINFO7-SOME.\n028354     MOVE 1 TO Z-FLINFO7-PRES.\n028356     GO TO Z-3-3-CONT.\n028358 Z-3-3-XIT.\n028360 Z-3-3-CONT.\n028362*\n028364******* OPEN FILE BK-SPEC-FILE\n028366*\n028368     IF Z-FLINFO3-OPEN = 0\n028370         CHANGE ATTRIBUTE DEPENDENTSPECS OF BK-SPEC-FILE TO TRUE \n028372         OPEN INPUT BK-SPEC-FILE \n028374         IF ATTRIBUTE FILESTATE OF BK-SPEC-FILE = VALUE OPENED\n028376             MOVE ZEROS TO Z-FILE3-KEY\n028378             MOVE ZEROS TO Z-FLINFO3-RS-KEY\n028380             MOVE 1 TO Z-FLINFO3-OPEN\n028382             MOVE 1 TO Z-FLINFO3-RS-OPEN\n028384         ELSE\n028386             DISPLAY \">>> FILE BK-SPEC-FILE FAILED TO OPEN\"\n028388             MOVE ATTRIBUTE TITLE OF BK-SPEC-FILE TO              \n028390                 Z-FL-EXCEPT-TITLE\n028392             DISPLAY \">>> OPEN FAIL, TITLE :\", Z-FL-EXCEPT-TITLE\n028394             DISPLAY \">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS\".\n028396     MOVE ATTRIBUTE CREATIONDATE OF BK-SPEC-FILE TO               \n028398          WS-SPECS-BANK-DATE.                                     \n028400     MOVE ATTRIBUTE CREATIONTIME OF BK-SPEC-FILE TO               \n028402          WS-SPECS-BANK-TIME.                                     \n028404 Z-3-5-LOOP.\n028406     MOVE 0 TO Z-EXIT-CODE.\n028408     MOVE 9999 TO Z-EXIT-LEVEL.\n028410     DISPLAY \"*************************************************\".\n028412     DISPLAY \"* 1 - PROCESS ONE BANK                          *\".\n028414     DISPLAY \"* 2 - LIST OF BANKS (UP TO 20 BANKS- 00010002   *\".\n028416     DISPLAY \"* 3 - PROCESS ALL BANKS -TDA/DAILY/day FILE     *\".\n028418     DISPLAY \"*************************************************\".\n028420     ACCEPT WS-BANK-OPT.\n028422     IF WS-BANK-OPT NOT = 1 AND 2 AND 3\n028424         NEXT SENTENCE ELSE\n028426         GO TO Z-3-12-1-ELSE.\n028428     DISPLAY \"INVALID BANK OPTION - ENTER 1, 2, OR 3\".\n028430     MOVE 1 TO Z-EXIT-LEVEL\n028432     GO TO Z-3-5-END.\n028434 Z-3-12-1-ELSE.\n028436     IF WS-BANK-OPT = 1\n028438         NEXT SENTENCE ELSE\n028440         GO TO Z-3-15-1-ELSE.\n028442     DISPLAY \"*** YOU SELECTED - PROCESS ONE BANK ***\".\n028444     GO TO Z-3-15-ENDIF.\n028446 Z-3-15-1-ELSE.\n028448     IF WS-BANK-OPT = 2\n028450         NEXT SENTENCE ELSE\n028452         GO TO Z-3-15-2-ELSE.\n028454     DISPLAY \"*** YOU SELECTED - LIST OF BANKS    ***\".\n028456     GO TO Z-3-15-ENDIF.\n028458 Z-3-15-2-ELSE.\n028460     IF WS-BANK-OPT = 3\n028462         NEXT SENTENCE ELSE\n028464         GO TO Z-3-15-3-ELSE.\n028466     DISPLAY \"*** YOU SELECTED - ALL BANKS        ***\".\n028468 Z-3-15-3-ELSE.\n028470 Z-3-15-ENDIF.\n028472     DISPLAY \"**** IS THIS CORRECT?  Y OR N  *********\".\n028474     ACCEPT WS-ACCEPT.\n028476     IF WS-ACCEPT = \"Y\"\n028478         NEXT SENTENCE ELSE\n028480         GO TO Z-3-21-1-ELSE.\n028482     MOVE 1 TO Z-EXIT-LEVEL.\n028484     MOVE 1 TO Z-EXIT-CODE.\n028486     GO TO Z-3-5-END.\n028488 Z-3-21-1-ELSE.\n028490 Z-3-5-END.\n028492     IF Z-EDIT-ERROR\n028494         GO TO Z-3-XIT.\n028496 Z-3-5-SKIP.\n028498     IF Z-EXIT-LEVEL < 0\n028500         GO TO Z-3-5-XIT.\n028502     IF Z-EXIT-LEVEL < 1\n028504         GO TO Z-3-END.\n028506     IF Z-EXIT-CODE > 0\n028508         GO TO Z-3-5-XIT.\n028510     GO TO Z-3-5-LOOP.\n028512*\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    580 lines from 13673 to 14252.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 29, "total_chunks": 55, "start_line": 13673, "end_line": 14252, "line_count": 580}

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
- Source code length: 27259 characters

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
CHUNK 29 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 13673 to 14252 (580 lines)
Chunk Tokens (estimated): ~8,063
Actual Input Tokens: 9,469 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 13673-14252 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 29 of 55 chunks
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
      The source code below is only CHUNK 29 of 55.


=============================================================================
CHUNK 29 SOURCE CODE (Lines 13673-14252)
=============================================================================

```cobol
027354 Z-DATE-CALC-LEAP-YEAR.
027356     MOVE Z-DATE-CC-1        TO Z-DATE-FORMAT-CC.
027358     MOVE Z-DATE-YY-1        TO Z-DATE-FORMAT-YY.
027360     MOVE Z-DATE-FORMAT-CCYY TO Z-DATE-YEAR-WORK.
027362     DIVIDE Z-DATE-YEAR-WORK BY +4 GIVING Z-DATE-DIVIDE-WORK
027364         REMAINDER Z-DATE-YEAR-MOD-4.
027366     DIVIDE Z-DATE-YEAR-WORK BY +100 GIVING Z-DATE-DIVIDE-WORK
027368         REMAINDER Z-DATE-YEAR-MOD-100.
027370     DIVIDE Z-DATE-YEAR-WORK BY +400 GIVING Z-DATE-DIVIDE-WORK
027372         REMAINDER Z-DATE-YEAR-MOD-400.
027374     IF Z-DATE-YEAR-MOD-4 = ZERO
027376         IF Z-DATE-YEAR-MOD-100 NOT = ZERO OR
027378            Z-DATE-YEAR-MOD-400 = ZERO
027380              SET Z-DATE-MM-I TO +2
027382              MOVE 29 TO Z-DATE-TBL-DAYS-IN-MON ( Z-DATE-MM-I )
027384              MOVE +1 TO Z-DATE-LEAP-YR-FLAG
027386              GO TO Z-DATE-CALC-LEAP-YEAR-EXIT.
027388     SET Z-DATE-MM-I TO +2.
027390     MOVE 28 TO Z-DATE-TBL-DAYS-IN-MON ( Z-DATE-MM-I ).
027392     MOVE +0 TO Z-DATE-LEAP-YR-FLAG.
027394*
027396 Z-DATE-CALC-LEAP-YEAR-EXIT.
027398     EXIT.
027400*
027402 Z-DATE-CALC-MONTH-DAYS.
027404*    FIX THE DAYS IF > THAN DAYS IN MONTH
027406     IF Z-DATE-DD-1 > 0 AND Z-DATE-MM-1 > 0 AND Z-DATE-MM-1 < +13
027408        IF Z-DATE-DD-1 > Z-DATE-TBL-DAYS-IN-MON ( Z-DATE-MM-1 )
027410           MOVE Z-DATE-TBL-DAYS-IN-MON ( Z-DATE-MM-1 ) TO
027412                Z-DATE-DD-1
027414           PERFORM Z-DATE-MDY-TO-JUL-CTRL
027416              THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT
027418           MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.
027420*
027422 Z-DATE-CALC-MONTH-DAYS-EXIT.
027424     EXIT.
027426*
027428 Z-DATE-MDY-TO-JUL-CTRL.
027430     MOVE ZEROS TO Z-DATE-ACCUM.
027432     MOVE ZEROS TO Z-DATE-JJJ-3.
027434     IF Z-DATE-MM-1 > +12
027436         MOVE 12 TO Z-DATE-MONTH-LIMIT
027438     ELSE
027440         SUBTRACT +1 FROM Z-DATE-MM-1
027442           GIVING Z-DATE-MONTH-LIMIT.
027444     PERFORM Z-DATE-CONVERT-MDY-TO-JUL
027446        THRU Z-DATE-CONVERT-MDY-TO-JUL-EXIT
027448     VARYING Z-DATE-MM-I FROM +1 BY +1
027450        UNTIL Z-DATE-MM-I > Z-DATE-MONTH-LIMIT.
027452     ADD Z-DATE-DD-1 TO Z-DATE-JJJ-3.
027454     MOVE Z-DATE-CC-1 TO Z-DATE-CC-3.
027456     MOVE Z-DATE-YY-1 TO Z-DATE-YY-3.
027458     ADD Z-DATE-ACCUM TO Z-DATE-JJJ-3.
027460 Z-DATE-MDY-TO-JUL-CTRL-EXIT.
027462     EXIT.
027464*
027466 Z-DATE-CONVERT-MDY-TO-JUL.
027468     ADD Z-DATE-ACCUM, Z-DATE-TBL-DAYS-IN-MON ( Z-DATE-MM-I )
027470       GIVING Z-DATE-ACCUM.
027472 Z-DATE-CONVERT-MDY-TO-JUL-EXIT.
027474     EXIT.
027476*
027478 Z-DATE-CC-DIFF.
027480     SUBTRACT Z-DATE-CC-1 FROM Z-DATE-CC-2 GIVING Z-DATE-C.
027482 Z-DATE-CC-DIFF-EXIT.
027484     EXIT.
027486*
027488 Z-DATE-YY-DIFF.
027490     COMPUTE Z-DATE-Y = (( Z-DATE-CC-2 * 100 ) + Z-DATE-YY-2 )
027492                      - (( Z-DATE-CC-1 * 100 ) + Z-DATE-YY-1 ).
027494 Z-DATE-YY-DIFF-EXIT.
027496     EXIT.
027498*
027500 Z-DATE-INITIALIZE-REGS.
027502     PERFORM Z-DATE-INIT-DATE-1
027504        THRU Z-DATE-INIT-DATE-1-EXIT.
027506     PERFORM Z-DATE-INIT-DATE-2
027508        THRU Z-DATE-INIT-DATE-2-EXIT.
027510     PERFORM Z-DATE-INIT-DATE-3
027512        THRU Z-DATE-INIT-DATE-3-EXIT.
027514 Z-DATE-INITIALIZE-REGS-EXIT.
027516     EXIT.
027518*
027520 Z-DATE-INITIALIZE-CTRL.
027522     PERFORM Z-DATE-INIT-UNITS
027524        THRU Z-DATE-INIT-UNITS-EXIT.
027526     PERFORM Z-DATE-INIT-MATH-WA
027528        THRU Z-DATE-INIT-MATH-WA-EXIT.
027530     PERFORM Z-DATE-INIT-JUL-MDY
027532        THRU Z-DATE-INIT-JUL-MDY-EXIT.
027534     PERFORM Z-DATE-INIT-LEAP-YR
027536        THRU Z-DATE-INIT-LEAP-YR-EXIT.
027538     PERFORM Z-DATE-INIT-CVRT-STATUS
027540        THRU Z-DATE-INIT-CVRT-STATUS-EXIT.
027542*
027544 Z-DATE-INITIALIZE-CTRL-EXIT.
027546     EXIT.
027548*
027550 Z-DATE-INIT-DATE-1.
027552     MOVE ZEROS  TO Z-DATE-CC-1.
027554     MOVE ZEROS  TO Z-DATE-YY-1.
027556     MOVE ZEROS  TO Z-DATE-MM-1.
027558     MOVE ZEROS  TO Z-DATE-DD-1.
027560     MOVE ZEROS  TO Z-DATE-JJJ-1.
027562     MOVE ZEROS  TO Z-DATE-HH-1.
027564     MOVE ZEROS  TO Z-DATE-UU-1.
027566     MOVE ZEROS  TO Z-DATE-SS-1.
027568     MOVE ZEROS  TO Z-DATE-TT-1.
027570     MOVE ZEROS  TO Z-DATE-ZZ-1.
027572     MOVE ZEROS  TO Z-DATE-AP-1.
027574     MOVE ZEROS  TO Z-DATE-MX-1.
027576     MOVE SPACES TO Z-DATE-CHARS-1.
027578 Z-DATE-INIT-DATE-1-EXIT.
027580     EXIT.
027582*
027584 Z-DATE-INIT-DATE-2.
027586     MOVE ZEROS  TO Z-DATE-CC-2.
027588     MOVE ZEROS  TO Z-DATE-YY-2.
027590     MOVE ZEROS  TO Z-DATE-MM-2.
027592     MOVE ZEROS  TO Z-DATE-DD-2.
027594     MOVE ZEROS  TO Z-DATE-JJJ-2.
027596     MOVE ZEROS  TO Z-DATE-HH-2.
027598     MOVE ZEROS  TO Z-DATE-UU-2.
027600     MOVE ZEROS  TO Z-DATE-SS-2.
027602     MOVE ZEROS  TO Z-DATE-TT-2.
027604     MOVE ZEROS  TO Z-DATE-ZZ-2.
027606     MOVE ZEROS  TO Z-DATE-AP-2.
027608     MOVE ZEROS  TO Z-DATE-MX-2.
027610     MOVE SPACES TO Z-DATE-CHARS-2.
027612 Z-DATE-INIT-DATE-2-EXIT.
027614     EXIT.
027616*
027618 Z-DATE-INIT-DATE-3.
027620     MOVE ZEROS  TO Z-DATE-CC-3.
027622     MOVE ZEROS  TO Z-DATE-YY-3.
027624     MOVE ZEROS  TO Z-DATE-MM-3.
027626     MOVE ZEROS  TO Z-DATE-DD-3.
027628     MOVE ZEROS  TO Z-DATE-JJJ-3.
027630     MOVE ZEROS  TO Z-DATE-HH-3.
027632     MOVE ZEROS  TO Z-DATE-UU-3.
027634     MOVE ZEROS  TO Z-DATE-SS-3.
027636     MOVE ZEROS  TO Z-DATE-TT-3.
027638     MOVE ZEROS  TO Z-DATE-ZZ-3.
027640     MOVE ZEROS  TO Z-DATE-AP-3.
027642     MOVE ZEROS  TO Z-DATE-MX-3.
027644     MOVE SPACES TO Z-DATE-CHARS-3.
027646 Z-DATE-INIT-DATE-3-EXIT.
027648     EXIT.
027650*
027652 Z-DATE-INIT-UNITS.
027654     MOVE ZEROS  TO Z-DATE-C.
027656     MOVE ZEROS  TO Z-DATE-Y.
027658     MOVE ZEROS  TO Z-DATE-M.
027660     MOVE ZEROS  TO Z-DATE-D.
027662     MOVE ZEROS  TO Z-DATE-W.
027664     MOVE ZEROS  TO Z-DATE-Z.
027666     MOVE ZEROS  TO Z-DATE-U.
027668     MOVE ZEROS  TO Z-DATE-S.
027670     MOVE ZEROS  TO Z-DATE-T.
027672 Z-DATE-INIT-UNITS-EXIT.
027674     EXIT.
027676*
027678 Z-DATE-INIT-MATH-WA.
027680     MOVE ZEROS  TO Z-DATE-UNITS-WORK.
027682     MOVE ZEROS  TO Z-DATE-FORMAT-CEN.
027684     MOVE ZEROS  TO Z-DATE-FORMAT-YR.
027686     MOVE ZEROS  TO Z-DATE-FORMAT-DAYS.
027688     MOVE ZEROS  TO Z-DATE-JUL-YR-WORK.
027690     MOVE ZEROS  TO Z-DATE-JULIAN-WORK.
027692     MOVE ZEROS  TO Z-DATE-X-TO-9.
027694     MOVE ZEROS  TO Z-DATE-NEG-INDICATOR.
027696     MOVE ZEROS  TO Z-DATE-JULIAN-1.
027698     MOVE ZEROS  TO Z-DATE-JULIAN-2.
027700     MOVE ZEROS  TO Z-DATE-TEMP-HOLD.
027702     MOVE ZEROS  TO Z-DATE-HOLD-JJJ.
027704     MOVE ZEROS  TO Z-DATE-JJJ-1-WORK.
027706     MOVE ZEROS  TO Z-DATE-JJJ-2-WORK.
027708     MOVE ZEROS  TO Z-DATE-WORK-YR-1.
027710     MOVE ZEROS  TO Z-DATE-WORK-YR-2.
027712     MOVE ZEROS  TO Z-DATE-HOLD-YEAR.
027714 Z-DATE-INIT-MATH-WA-EXIT.
027716     EXIT.
027718*
027720 Z-DATE-INIT-JUL-MDY.
027722     MOVE ZEROS  TO Z-DATE-MDY-STRING.
027724     MOVE ZEROS  TO Z-DATE-ACCUM.
027726     MOVE ZEROS  TO Z-DATE-MONTH-LIMIT.
027728 Z-DATE-INIT-JUL-MDY-EXIT.
027730     EXIT.
027732*
027734 Z-DATE-INIT-LEAP-YR.
027736     MOVE ZEROS  TO Z-DATE-FORMAT-CC.
027738     MOVE ZEROS  TO Z-DATE-FORMAT-YY.
027740     MOVE ZEROS  TO Z-DATE-FORMAT-YEAR.
027742     MOVE ZEROS  TO Z-DATE-YEAR-WORK.
027744     MOVE ZEROS  TO Z-DATE-DIVIDE-WORK.
027746     MOVE ZEROS  TO Z-DATE-QUOTIENT.
027748     MOVE ZEROS  TO Z-DATE-REMAINDER.
027750     MOVE ZEROS  TO Z-DATE-YEAR-MOD-4.
027752     MOVE ZEROS  TO Z-DATE-YEAR-MOD-100.
027754     MOVE ZEROS  TO Z-DATE-YEAR-MOD-400.
027756     MOVE ZEROS  TO Z-DATE-LEAP-YR-FLAG.
027758 Z-DATE-INIT-LEAP-YR-EXIT.
027760     EXIT.
027762*
027764 Z-DATE-INIT-CVRT-STATUS.
027766     MOVE ZEROS  TO Z-DATE-CONVERT-STATUS.
027768 Z-DATE-INIT-CVRT-STATUS-EXIT.
027770     EXIT.
027772*
027774*****************************************************************
027776*Z-USERS-DECLARATIONS SECTION.
027778*****************************************************************
027780*
027782*Z-USERS-DECLARATIONS-PARAGRAPH.
027784*
027786*
027788****************************************************************
027790* EACH-HEADING FOR REPORT LISTING
027792****************************************************************
027794 Z-1-PROCEDURE.
027796
027798     MOVE 1 TO Z-RPTINFO1-INBLOCK.
027800     MOVE Z-RPT-1-PAGE TO WS-PAGE-CNT.
027802     MOVE "TDA-700" TO H-REPORT-NO.
027804     MOVE "RMD CALCULATION REPORT" TO H-RPT-TITLE.
027806     MOVE SPACES TO HEADER-PAGE.
027808     IF H-PAGE-CST-160 = SPACES
027810         NEXT SENTENCE
027812     ELSE
027814         GO TO Z-1-4-END-MOVE.
027816     MOVE "PAGE" TO H-PAGE-CST-160.
027818 Z-1-4-END-MOVE.
027820     MOVE WS-PAGE-CNT TO H-PAGE-NO-160.
027822     IF HDR-CTL NOT = 0
027824         NEXT SENTENCE ELSE
027826         GO TO Z-1-6-1-ELSE.
027828     MOVE 1 TO Z-RPT-1-LINE.
027830     MOVE HEADER-LINE1 TO Z-RPT-1-BUFFER.
027832     WRITE Z-RPT-1-BUFFER AFTER ADVANCING PAGE.
027834     COMPUTE Z-LINES-HOLD = 1.
027836     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES-HOLD).
027838     IF Z-RPT-1-LINE > Z-RPT-1-PAGE-SIZE
027840         SUBTRACT Z-RPT-1-PAGE-SIZE FROM Z-RPT-1-LINE.
027842     MOVE PRINT-SPACES-160 TO Z-RPT-1-BUFFER.
027844     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES-HOLD.
027846 Z-1-6-1-ELSE.
027848     MOVE RMDRPT-REC-2 TO HEADER-LINE2-160.
027850     MOVE RMDRPT-REC-6 TO HEADER-LINE3-160.
027852     IF HDR-CTL > 1
027854         NEXT SENTENCE ELSE
027856         GO TO Z-1-11-1-ELSE.
027858     COMPUTE Z-LINES-HOLD = 1.
027860     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES-HOLD).
027862     IF Z-RPT-1-LINE > Z-RPT-1-PAGE-SIZE
027864         SUBTRACT Z-RPT-1-PAGE-SIZE FROM Z-RPT-1-LINE.
027866     MOVE HEADER-LINE2-160 TO Z-RPT-1-BUFFER.
027868     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES-HOLD.
027870 Z-1-11-1-ELSE.
027872     IF HDR-CTL > 2
027874         NEXT SENTENCE ELSE
027876         GO TO Z-1-13-1-ELSE.
027878     COMPUTE Z-LINES-HOLD = 1.
027880     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES-HOLD).
027882     IF Z-RPT-1-LINE > Z-RPT-1-PAGE-SIZE
027884         SUBTRACT Z-RPT-1-PAGE-SIZE FROM Z-RPT-1-LINE.
027886     MOVE HEADER-LINE3-160 TO Z-RPT-1-BUFFER.
027888     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES-HOLD.
027890 Z-1-13-1-ELSE.
027892     IF HDR-CTL > 3
027894         NEXT SENTENCE ELSE
027896         GO TO Z-1-15-1-ELSE.
027898     COMPUTE Z-LINES-HOLD = 1.
027900     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES-HOLD).
027902     IF Z-RPT-1-LINE > Z-RPT-1-PAGE-SIZE
027904         SUBTRACT Z-RPT-1-PAGE-SIZE FROM Z-RPT-1-LINE.
027906     MOVE HEADER-LINE4-160 TO Z-RPT-1-BUFFER.
027908     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES-HOLD.
027910 Z-1-15-1-ELSE.
027912     IF Z-EDIT-ERROR
027914         MOVE 0 TO Z-RPTINFO1-INBLOCK
027916         GO TO Z-1-XIT.
027918 Z-1-SKIP.
027920     MOVE 0 TO Z-RPTINFO1-INBLOCK.
027922 Z-1-XIT.
027924     EXIT.
027926*
027928*****************************************************************
027930*    SUPPORT ROUTINES FOR REPORT LISTING
027932*****************************************************************
027934*
027936 Z-RPT-1-ADV-PAGE-CNT.
027938     ADD 1 TO Z-RPT-1-PAGE.
027940*
027942 Z-RPT-1-NEWPAGE.
027944     PERFORM Z-RPT-1-ADV-PAGE-CNT.
027946*
027948************ REPORT 1 EACH HEADING
027950     PERFORM Z-1-PROCEDURE THRU Z-1-XIT.
027952*
027954 Z-RPT-1-SET-TRAP.
027956     IF Z-RPT-1-LINE > (Z-RPT-1-PAGE-SIZE - 1)
027958         COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE - (Z-RPT-1-PAGE-SIZE 
027960             - 1).
027962     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
027964*
027966 Z-RPT-1-NEWPAGE-XIT.
027968     EXIT.
027970*
027972*
027974*
027976****************************************************************
027978* EACH-HEADING FOR REPORT FICHE
027980****************************************************************
027982 Z-2-PROCEDURE.
027984
027986     MOVE 1 TO Z-RPTINFO2-INBLOCK.
027988     MOVE Z-RPT-2-PAGE TO WS-PAGE-CNT-FICHE.
027990     MOVE "TDA-701" TO H-REPORT-NO.
027992     MOVE "RMD CALCULATION REPORT FOR INHERITED IRA'S" TO         
027994         H-RPT-TITLE.
027996     MOVE SPACES TO HEADER-PAGE.
027998     IF H-PAGE-CST-160 = SPACES
028000         NEXT SENTENCE
028002     ELSE
028004         GO TO Z-2-4-END-MOVE.
028006     MOVE "PAGE" TO H-PAGE-CST-160.
028008 Z-2-4-END-MOVE.
028010     MOVE WS-PAGE-CNT-FICHE TO H-PAGE-NO-160.
028012     IF HDR-CTL NOT = 0
028014         NEXT SENTENCE ELSE
028016         GO TO Z-2-6-1-ELSE.
028018     MOVE 1 TO Z-RPT-2-LINE.
028020     MOVE HEADER-LINE1 TO Z-RPT-2-BUFFER.
028022     WRITE Z-RPT-2-BUFFER AFTER ADVANCING PAGE.
028024     COMPUTE Z-LINES-HOLD = 1.
028026     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES-HOLD).
028028     IF Z-RPT-2-LINE > Z-RPT-2-PAGE-SIZE
028030         SUBTRACT Z-RPT-2-PAGE-SIZE FROM Z-RPT-2-LINE.
028032     MOVE PRINT-SPACES-160 TO Z-RPT-2-BUFFER.
028034     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES-HOLD.
028036 Z-2-6-1-ELSE.
028038     MOVE RMDRPT2-REC-2 TO HEADER-LINE2-160.
028040     MOVE RMDRPT2-REC-6 TO HEADER-LINE3-160.
028042     IF HDR-CTL > 1
028044         NEXT SENTENCE ELSE
028046         GO TO Z-2-11-1-ELSE.
028048     COMPUTE Z-LINES-HOLD = 1.
028050     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES-HOLD).
028052     IF Z-RPT-2-LINE > Z-RPT-2-PAGE-SIZE
028054         SUBTRACT Z-RPT-2-PAGE-SIZE FROM Z-RPT-2-LINE.
028056     MOVE HEADER-LINE2-160 TO Z-RPT-2-BUFFER.
028058     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES-HOLD.
028060 Z-2-11-1-ELSE.
028062     IF HDR-CTL > 2
028064         NEXT SENTENCE ELSE
028066         GO TO Z-2-13-1-ELSE.
028068     COMPUTE Z-LINES-HOLD = 1.
028070     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES-HOLD).
028072     IF Z-RPT-2-LINE > Z-RPT-2-PAGE-SIZE
028074         SUBTRACT Z-RPT-2-PAGE-SIZE FROM Z-RPT-2-LINE.
028076     MOVE HEADER-LINE3-160 TO Z-RPT-2-BUFFER.
028078     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES-HOLD.
028080 Z-2-13-1-ELSE.
028082     IF HDR-CTL > 3
028084         NEXT SENTENCE ELSE
028086         GO TO Z-2-15-1-ELSE.
028088     COMPUTE Z-LINES-HOLD = 1.
028090     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES-HOLD).
028092     IF Z-RPT-2-LINE > Z-RPT-2-PAGE-SIZE
028094         SUBTRACT Z-RPT-2-PAGE-SIZE FROM Z-RPT-2-LINE.
028096     MOVE HEADER-LINE4-160 TO Z-RPT-2-BUFFER.
028098     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES-HOLD.
028100 Z-2-15-1-ELSE.
028102     IF Z-EDIT-ERROR
028104         MOVE 0 TO Z-RPTINFO2-INBLOCK
028106         GO TO Z-2-XIT.
028108 Z-2-SKIP.
028110     MOVE 0 TO Z-RPTINFO2-INBLOCK.
028112 Z-2-XIT.
028114     EXIT.
028116*
028118*****************************************************************
028120*    SUPPORT ROUTINES FOR REPORT FICHE
028122*****************************************************************
028124*
028126 Z-RPT-2-ADV-PAGE-CNT.
028128     ADD 1 TO Z-RPT-2-PAGE.
028130*
028132 Z-RPT-2-NEWPAGE.
028134     PERFORM Z-RPT-2-ADV-PAGE-CNT.
028136*
028138************ REPORT 2 EACH HEADING
028140     PERFORM Z-2-PROCEDURE THRU Z-2-XIT.
028142*
028144 Z-RPT-2-SET-TRAP.
028146     IF Z-RPT-2-LINE > (Z-RPT-2-PAGE-SIZE - 1)
028148         COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE - (Z-RPT-2-PAGE-SIZE 
028150             - 1).
028152     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.
028154*
028156 Z-RPT-2-NEWPAGE-XIT.
028158     EXIT.
028160*
028162*
028164*
028166*****************************************************************
028168 Z-USERS-ROUTINES SECTION.
028170*****************************************************************
028172*
028174 Z-USERS-ROUTINES-PARAGRAPH.
028176*
028178*
028180*****************************************************************
028182*    PROCESS MAIN
028184*****************************************************************
028186*
028188 Z-3-PROCESS.
028190*
028192     MOVE 1 TO Z-PROCESS-FLAG.
028194     MOVE "MAIN" TO Z-PROCESS-NAME.
028196     MOVE 0 TO Z-CONTINUE-FLAG.
028198     IF Z-RESTART-FLAG = 1
028200         MOVE ZERO TO Z-RESTART-FLAG
028202         GO TO Z-3-RESTART.
028204     MOVE ZERO TO Z-RESTART-POINT.
028206     MOVE 3 TO Z-RESTART-PROCESS.
028208 MOVE ATTRIBUTE HOSTNAME OF MYSELF TO WS-WORK-AREA-HOST.          
028210 STRING WS-WORK-AREA-HOST DELIMITED BY "." INTO WS-SYS-HOST.      
028212     MOVE 0 TO Z-EXIT-CODE.
028214     MOVE 9999 TO Z-EXIT-LEVEL.
028216*    RETRIEVE TODAY'S DATE
028218     CALL "CURRENT_DATE OF GENERALSUPPORT"
028220          USING Z-CALL-CURRENTDATE.
028222     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
028224     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
028226     ACCEPT Z-DATE0-TIME   FROM TIME.
028228     MOVE Z-DATE0-CC TO Z-DATE2-CC.
028230     MOVE Z-DATE0-YY TO Z-DATE2-YY.
028232     MOVE Z-DATE0-MM TO Z-DATE2-MM.
028234     MOVE Z-DATE0-DD TO Z-DATE2-DD.
028236     MOVE Z-DATE2-FORMAT-9 TO PROCESS-DATE.
028238     MOVE ZERO TO Z-FLINFO7-PRES.
028240     MOVE 1 TO Z-FLINFO7-LAST-SEQ.
028242     MOVE ZERO TO Z-FLINFO7-SOME.
028244     SET SPCPRTALL OF SPCPRT OF LDBSPCDB TO ENDING
028246         ON EXCEPTION
028248         MOVE "SPCPRTALL OF SPCPRT OF LDBSPCDB" TO                
028250             Z-DMS-EXCEPT-STR
028252         MOVE "LDBSPCDB" TO Z-DMS-EXCEPT-DB
028254         MOVE 1 TO Z-DMS-EXCEPT-SEQ
028256         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT
028258         GO TO Z-3-2-XIT.
028260 Z-3-2-READ.
028262     FIND SPCPRT OF LDBSPCDB VIA PRIOR SPCPRTALL OF SPCPRT OF     
028264         LDBSPCDB
028266         ON EXCEPTION
028268         MOVE 1 TO Z-DMS-EXCEPT-SEQ
028270         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
028272             GO TO Z-3-2-XIT
028274         ELSE
028276             MOVE "SPCPRTALL OF SPCPRT OF LDBSPCDB" TO            
028278                 Z-DMS-EXCEPT-STR
028280             MOVE "LDBSPCDB" TO Z-DMS-EXCEPT-DB
028282             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
028284
028286 Z-3-2-PRESENT.
028288*
028290     MOVE 1 TO Z-FLINFO7-SOME.
028292     MOVE 1 TO Z-FLINFO7-PRES.
028294     GO TO Z-3-2-CONT.
028296 Z-3-2-XIT.
028298 Z-3-2-CONT.
028300     MOVE ZERO TO Z-FLINFO7-PRES.
028302     MOVE 2 TO Z-FLINFO7-LAST-SEQ.
028304     MOVE ZERO TO Z-FLINFO7-SOME.
028306     SET SPCPRTCURR OF SPCPRT OF LDBSPCDB TO ENDING
028308         ON EXCEPTION
028310         MOVE "SPCPRTCURR OF SPCPRT OF LDBSPCDB" TO               
028312             Z-DMS-EXCEPT-STR
028314         MOVE "LDBSPCDB" TO Z-DMS-EXCEPT-DB
028316         MOVE 2 TO Z-DMS-EXCEPT-SEQ
028318         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT
028320         GO TO Z-3-3-XIT.
028322 Z-3-3-READ.
028324     FIND SPCPRT OF LDBSPCDB VIA PRIOR SPCPRTCURR OF SPCPRT OF    
028326         LDBSPCDB
028328         ON EXCEPTION
028330         MOVE 2 TO Z-DMS-EXCEPT-SEQ
028332         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
028334             GO TO Z-3-3-XIT
028336         ELSE
028338             MOVE "SPCPRTCURR OF SPCPRT OF LDBSPCDB" TO           
028340                 Z-DMS-EXCEPT-STR
028342             MOVE "LDBSPCDB" TO Z-DMS-EXCEPT-DB
028344             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
028346
028348 Z-3-3-PRESENT.
028350*
028352     MOVE 1 TO Z-FLINFO7-SOME.
028354     MOVE 1 TO Z-FLINFO7-PRES.
028356     GO TO Z-3-3-CONT.
028358 Z-3-3-XIT.
028360 Z-3-3-CONT.
028362*
028364******* OPEN FILE BK-SPEC-FILE
028366*
028368     IF Z-FLINFO3-OPEN = 0
028370         CHANGE ATTRIBUTE DEPENDENTSPECS OF BK-SPEC-FILE TO TRUE 
028372         OPEN INPUT BK-SPEC-FILE 
028374         IF ATTRIBUTE FILESTATE OF BK-SPEC-FILE = VALUE OPENED
028376             MOVE ZEROS TO Z-FILE3-KEY
028378             MOVE ZEROS TO Z-FLINFO3-RS-KEY
028380             MOVE 1 TO Z-FLINFO3-OPEN
028382             MOVE 1 TO Z-FLINFO3-RS-OPEN
028384         ELSE
028386             DISPLAY ">>> FILE BK-SPEC-FILE FAILED TO OPEN"
028388             MOVE ATTRIBUTE TITLE OF BK-SPEC-FILE TO              
028390                 Z-FL-EXCEPT-TITLE
028392             DISPLAY ">>> OPEN FAIL, TITLE :", Z-FL-EXCEPT-TITLE
028394             DISPLAY ">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS".
028396     MOVE ATTRIBUTE CREATIONDATE OF BK-SPEC-FILE TO               
028398          WS-SPECS-BANK-DATE.                                     
028400     MOVE ATTRIBUTE CREATIONTIME OF BK-SPEC-FILE TO               
028402          WS-SPECS-BANK-TIME.                                     
028404 Z-3-5-LOOP.
028406     MOVE 0 TO Z-EXIT-CODE.
028408     MOVE 9999 TO Z-EXIT-LEVEL.
028410     DISPLAY "*************************************************".
028412     DISPLAY "* 1 - PROCESS ONE BANK                          *".
028414     DISPLAY "* 2 - LIST OF BANKS (UP TO 20 BANKS- 00010002   *".
028416     DISPLAY "* 3 - PROCESS ALL BANKS -TDA/DAILY/day FILE     *".
028418     DISPLAY "*************************************************".
028420     ACCEPT WS-BANK-OPT.
028422     IF WS-BANK-OPT NOT = 1 AND 2 AND 3
028424         NEXT SENTENCE ELSE
028426         GO TO Z-3-12-1-ELSE.
028428     DISPLAY "INVALID BANK OPTION - ENTER 1, 2, OR 3".
028430     MOVE 1 TO Z-EXIT-LEVEL
028432     GO TO Z-3-5-END.
028434 Z-3-12-1-ELSE.
028436     IF WS-BANK-OPT = 1
028438         NEXT SENTENCE ELSE
028440         GO TO Z-3-15-1-ELSE.
028442     DISPLAY "*** YOU SELECTED - PROCESS ONE BANK ***".
028444     GO TO Z-3-15-ENDIF.
028446 Z-3-15-1-ELSE.
028448     IF WS-BANK-OPT = 2
028450         NEXT SENTENCE ELSE
028452         GO TO Z-3-15-2-ELSE.
028454     DISPLAY "*** YOU SELECTED - LIST OF BANKS    ***".
028456     GO TO Z-3-15-ENDIF.
028458 Z-3-15-2-ELSE.
028460     IF WS-BANK-OPT = 3
028462         NEXT SENTENCE ELSE
028464         GO TO Z-3-15-3-ELSE.
028466     DISPLAY "*** YOU SELECTED - ALL BANKS        ***".
028468 Z-3-15-3-ELSE.
028470 Z-3-15-ENDIF.
028472     DISPLAY "**** IS THIS CORRECT?  Y OR N  *********".
028474     ACCEPT WS-ACCEPT.
028476     IF WS-ACCEPT = "Y"
028478         NEXT SENTENCE ELSE
028480         GO TO Z-3-21-1-ELSE.
028482     MOVE 1 TO Z-EXIT-LEVEL.
028484     MOVE 1 TO Z-EXIT-CODE.
028486     GO TO Z-3-5-END.
028488 Z-3-21-1-ELSE.
028490 Z-3-5-END.
028492     IF Z-EDIT-ERROR
028494         GO TO Z-3-XIT.
028496 Z-3-5-SKIP.
028498     IF Z-EXIT-LEVEL < 0
028500         GO TO Z-3-5-XIT.
028502     IF Z-EXIT-LEVEL < 1
028504         GO TO Z-3-END.
028506     IF Z-EXIT-CODE > 0
028508         GO TO Z-3-5-XIT.
028510     GO TO Z-3-5-LOOP.
028512*
```

⚠️  This is the source code you must document.
    580 lines from 13673 to 14252.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

