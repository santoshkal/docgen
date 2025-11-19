# LLM Request Debug File
Generated: 2025-11-17T22:13:50.254571

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 41/55
- **Model**: gpt-4.1
- **Chunk Number**: 41
- **Pass Number**: 3
- **Attempt Number**: 3 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~7,250 tokens
- **Total Input**: ~9,208 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 41/55" (ID: detailed-code-explanation)

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


**CHUNK 41 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-17T19:50:50.832678", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 41 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 19648 to 20133 (486 lines)\nChunk Tokens (estimated): ~8,075\nActual Input Tokens: 9,481 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 19648-20133 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 41 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 41 of 55.\n\n\n=============================================================================\nCHUNK 41 SOURCE CODE (Lines 19648-20133)\n=============================================================================\n\n```cobol\n039304 Z-5-40-1-ELSE.\n039306     IF NOT Z-SW3\n039308         NEXT SENTENCE ELSE\n039310         GO TO Z-5-45-1-ELSE.\n039312     COMPUTE Z-LINES-HOLD = 1.\n039314     COMPUTE Z-LINES = 1.\n039316     IF Z-RPT-1-TRAP > ZERO\n039318         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n039320     IF Z-LINES > Z-RPT-1-TRAP\n039322       IF Z-RPTINFO1-INBLOCK = ZERO\n039324         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n039326         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n039328         COMPUTE Z-LINES = 1.\n039330     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n039332     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n039334     MOVE RMDRPT-REC-3 TO Z-RPT-1-BUFFER.\n039336     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n039338 Z-5-45-1-ELSE.\n039340     MOVE SPACES TO RMDRPT-REC-4.\n039342     MOVE WS-TIN-DET-LINE-4 (J) TO RMDRPT-REC-4.\n039344     IF NOT Z-SW3\n039346         NEXT SENTENCE ELSE\n039348         GO TO Z-5-49-1-ELSE.\n039350     COMPUTE Z-LINES-HOLD = 1.\n039352     COMPUTE Z-LINES = 1.\n039354     IF Z-RPT-1-TRAP > ZERO\n039356         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n039358     IF Z-LINES > Z-RPT-1-TRAP\n039360       IF Z-RPTINFO1-INBLOCK = ZERO\n039362         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n039364         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n039366         COMPUTE Z-LINES = 1.\n039368     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n039370     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n039372     MOVE RMDRPT-REC-4 TO Z-RPT-1-BUFFER.\n039374     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n039376 Z-5-49-1-ELSE.\n039378     MOVE SPACES TO RMDRPT-REC-8.\n039380     IF ( WS-TIN-DET-LINE-8 (J) NOT = SPACES ) AND ( NOT Z-SW3 )\n039382         NEXT SENTENCE ELSE\n039384         GO TO Z-5-52-1-ELSE.\n039386     MOVE WS-TIN-DET-LINE-8 (J) TO RMDRPT-REC-8.\n039388     COMPUTE Z-LINES-HOLD = 1.\n039390     COMPUTE Z-LINES = 1.\n039392     IF Z-RPT-1-TRAP > ZERO\n039394         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n039396     IF Z-LINES > Z-RPT-1-TRAP\n039398       IF Z-RPTINFO1-INBLOCK = ZERO\n039400         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n039402         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n039404         COMPUTE Z-LINES = 1.\n039406     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n039408     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n039410     MOVE RMDRPT-REC-8 TO Z-RPT-1-BUFFER.\n039412     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n039414 Z-5-52-1-ELSE.\n039416 Z-5-36-END.\n039418     IF Z-EDIT-ERROR\n039420         GO TO Z-5-XIT.\n039422 Z-5-36-SKIP.\n039424     IF Z-EXIT-LEVEL < 3\n039426         GO TO Z-5-14-END.\n039428     IF Z-EXIT-CODE > 0\n039430         GO TO Z-5-36-XIT.\n039432     ADD 1 TO J.\n039434     GO TO Z-5-36-LOOP.\n039436*\n039438 Z-5-36-XIT.\n039440     MOVE 0 TO Z-EXIT-CODE.\n039442     MOVE 9999 TO Z-EXIT-LEVEL.\n039444     MOVE SPACES TO WS-TIN-DETAIL-TABLE.\n039446     MOVE 0 TO WS-TIN-DETAIL-INDEX.\n039448************ PERFORM COMB-AUTO-RMD-ADJ\n039450     IF ( SPECS-COMB-AUTO-RMD-ADJUST = \"Y\" )\n039452        NEXT SENTENCE ELSE\n039454        GO TO Z-5-57-SKIPPROC.\n039456************ PERFORM COMB-AUTO-RMD-ADJ\n039458     PERFORM Z-27-PROCEDURE THRU Z-27-XIT.\n039460     IF  Z-EXIT-EDITEXIT\n039462         GO TO Z-5-XIT.\n039464     IF  Z-DMS2-ABORT-FLAG = 1\n039466         GO TO Z-5-XIT.\n039468     IF  Z-EXIT-LEVEL < 0\n039470         GO TO Z-5-14-END.\n039472*\n039474 Z-5-57-SKIPPROC.\n039476     MOVE 0 TO WS-TIN-DISTR-RECS.\n039478 Z-5-35-1-ELSE.\n039480     IF WS-NON-INHERIT-IRA-ON-TIN = 1\n039482         NEXT SENTENCE ELSE\n039484         GO TO Z-5-59-1-ELSE.\n039486     MOVE WS-PREV-TIN TO WS-RMDRPT-TIN.\n039488     MOVE \"-\" TO WS-RMDRPT-TIN-LDASH\n039490       , WS-RMDRPT-TIN-RDASH.\n039492     MOVE WS-RMDRPT-TIN TO RMDRPT-TOT-TIN-9.\n039494     MOVE WS-TIN-BAL-TOT TO RMDRPT-TIN-TOT-BAL-9.\n039496     MOVE WS-TIN-RMD-TOT TO RMDRPT-TIN-TOT-RMD-9.\n039498     IF NOT Z-SW3\n039500         NEXT SENTENCE ELSE\n039502         GO TO Z-5-65-1-ELSE.\n039504     COMPUTE Z-LINES-HOLD = 1.\n039506     COMPUTE Z-LINES = 1.\n039508     IF Z-RPT-1-TRAP > ZERO\n039510         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n039512     IF Z-LINES > Z-RPT-1-TRAP\n039514       IF Z-RPTINFO1-INBLOCK = ZERO\n039516         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n039518         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n039520         COMPUTE Z-LINES = 1.\n039522     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n039524     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n039526     MOVE RMDRPT-REC-9 TO Z-RPT-1-BUFFER.\n039528     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n039530     COMPUTE Z-LINES-HOLD = 1.\n039532     COMPUTE Z-LINES = 1.\n039534     IF Z-RPT-1-TRAP > ZERO\n039536         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n039538     IF Z-LINES > Z-RPT-1-TRAP\n039540       IF Z-RPTINFO1-INBLOCK = ZERO\n039542         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n039544         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n039546         COMPUTE Z-LINES = 1.\n039548     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n039550     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n039552     MOVE SPACES TO Z-RPT-1-BUFFER.\n039554     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n039556 Z-5-65-1-ELSE.\n039558 Z-5-59-1-ELSE.\n039560     IF WS-INHERIT-IRA-ON-TIN = 1\n039562         NEXT SENTENCE ELSE\n039564         GO TO Z-5-68-1-ELSE.\n039566     MOVE WS-PREV-TIN TO WS-RMDRPT2-TIN.\n039568     MOVE \"-\" TO WS-RMDRPT2-TIN-LDASH\n039570       , WS-RMDRPT2-TIN-RDASH.\n039572     MOVE WS-RMDRPT2-TIN TO RMDRPT-TOT-TIN-10.\n039574     IF NOT Z-SW3\n039576         NEXT SENTENCE ELSE\n039578         GO TO Z-5-72-1-ELSE.\n039580     COMPUTE Z-LINES-HOLD = 1.\n039582     COMPUTE Z-LINES = 1.\n039584     IF Z-RPT-2-TRAP > ZERO\n039586         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.\n039588     IF Z-LINES > Z-RPT-2-TRAP\n039590       IF Z-RPTINFO2-INBLOCK = ZERO\n039592         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1\n039594         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT\n039596         COMPUTE Z-LINES = 1.\n039598     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).\n039600     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).\n039602     MOVE RMDRPT-REC-10 TO Z-RPT-2-BUFFER.\n039604     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.\n039606     COMPUTE Z-LINES-HOLD = 1.\n039608     COMPUTE Z-LINES = 1.\n039610     IF Z-RPT-2-TRAP > ZERO\n039612         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.\n039614     IF Z-LINES > Z-RPT-2-TRAP\n039616       IF Z-RPTINFO2-INBLOCK = ZERO\n039618         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1\n039620         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT\n039622         COMPUTE Z-LINES = 1.\n039624     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).\n039626     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).\n039628     MOVE SPACES TO Z-RPT-2-BUFFER.\n039630     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.\n039632 Z-5-72-1-ELSE.\n039634 Z-5-68-1-ELSE.\n039636     MOVE ZEROS TO WS-TIN-TOTALS\n039638       , WS-INHERIT-IRA-ON-TIN\n039640       , WS-NON-INHERIT-IRA-ON-TIN.\n039642     IF ( WS-TIN-RMD-TOT NOT = 0 ) AND ( NOT Z-SW3 )\n039644         NEXT SENTENCE ELSE\n039646         GO TO Z-5-76-1-ELSE.\n039648     COMPUTE Z-LINES-HOLD = 1.\n039650     COMPUTE Z-LINES = 1.\n039652     IF Z-RPT-1-TRAP > ZERO\n039654         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.\n039656     IF Z-LINES > Z-RPT-1-TRAP\n039658       IF Z-RPTINFO1-INBLOCK = ZERO\n039660         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1\n039662         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT\n039664         COMPUTE Z-LINES = 1.\n039666     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).\n039668     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).\n039670     MOVE SPACES TO Z-RPT-1-BUFFER.\n039672     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.\n039674 Z-5-76-1-ELSE.\n039676     MOVE TDB-TDAC-TIN-NBR TO WS-PREV-TIN.\n039678 Z-5-34-1-ELSE.\n039680     MOVE 0 TO WS-MULTI-DISTR\n039682       , WS-IRA-DISTR-RECS.\n039684     MOVE ZERO TO Z-FLINFO13-PRES.\n039686     MOVE ZERO TO Z-FLINFO13-SOME.\n039688     MOVE 11 TO Z-FLINFO13-LAST-SEQ.\n039690*\n039692     SET TDADSNBRSET OF TDADISTR OF LDBTDADB TO BEGINNING\n039694         ON EXCEPTION\n039696         MOVE \"TDADSNBRSET OF TDADISTR OF LDBTDADB\" TO            \n039698             Z-DMS-EXCEPT-STR\n039700         MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n039702         MOVE 11 TO Z-DMS-EXCEPT-SEQ\n039704         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT\n039706         GO TO Z-5-80-XIT.\n039708 Z-5-80-LOOP.\n039710     MOVE ZERO TO Z-FLINFO13-PRES.\n039712 Z-5-80-READ.\n039714     FIND KEY OF NEXT TDADSNBRSET OF TDADISTR OF LDBTDADB\n039716     AT TDAD-BANK = WS-BANK-NO AND\n039718        TDAD-CUST = TDB-TDAI-CUST AND\n039720        TDAD-ACCT = TDB-TDAI-ACCT\n039722         ON EXCEPTION\n039724         MOVE 11 TO Z-DMS-EXCEPT-SEQ\n039726         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n039728             GO TO Z-5-80-XIT\n039730         ELSE\n039732             MOVE \"TDADSNBRSET OF TDADISTR OF LDBTDADB\" TO        \n039734                 Z-DMS-EXCEPT-STR\n039736             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n039738             MOVE 11 TO Z-DMS-EXCEPT-SEQ\n039740             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n039742\n039744*\n039746     MOVE 1 TO Z-FLINFO13-PRES.\n039748     MOVE 1 TO Z-FLINFO13-SOME.\n039750     ADD 1 TO WS-IRA-DISTR-RECS , WS-TIN-DISTR-RECS .\n039752     IF Z-EDIT-ERROR\n039754         GO TO Z-5-XIT.\n039756 Z-5-80-SKIP.\n039758     GO TO Z-5-80-LOOP.\n039760*\n039762 Z-5-80-XIT.\n039764     MOVE ZERO TO Z-FLINFO13-PRES.\n039766     MOVE ZERO TO Z-FLINFO13-SOME.\n039768     MOVE 12 TO Z-FLINFO13-LAST-SEQ.\n039770*\n039772     SET TDADSSET OF TDADISTR OF LDBTDADB TO BEGINNING\n039774         ON EXCEPTION\n039776         MOVE \"TDADSSET OF TDADISTR OF LDBTDADB\" TO               \n039778             Z-DMS-EXCEPT-STR\n039780         MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n039782         MOVE 12 TO Z-DMS-EXCEPT-SEQ\n039784         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT\n039786         GO TO Z-5-82-XIT.\n039788 Z-5-82-LOOP.\n039790     MOVE ZERO TO Z-FLINFO13-PRES.\n039792 Z-5-82-READ.\n039794     FIND TDADISTR OF LDBTDADB VIA NEXT TDADSSET OF TDADISTR OF   \n039796         LDBTDADB\n039798     AT TDAD-BANK = WS-BANK-NO AND\n039800        TDAD-CUST = TDB-TDAI-CUST AND\n039802        TDAD-ACCT = TDB-TDAI-ACCT\n039804         ON EXCEPTION\n039806         MOVE 12 TO Z-DMS-EXCEPT-SEQ\n039808         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n039810             GO TO Z-5-82-XIT\n039812         ELSE\n039814             MOVE \"TDADSSET OF TDADISTR OF LDBTDADB\" TO           \n039816                 Z-DMS-EXCEPT-STR\n039818             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n039820             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n039822\n039824*\n039826     MOVE 1 TO Z-FLINFO13-PRES.\n039828     MOVE 1 TO Z-FLINFO13-SOME.\n039830     MOVE 0 TO Z-EXIT-CODE.\n039832     MOVE 9999 TO Z-EXIT-LEVEL.\n039834     MOVE 1 TO WS-DSREC-FLAG.\n039836     ADD 1 TO WS-MULTI-DISTR .\n039838     MOVE TDAD-BANK OF TDADISTR TO TDB-TDAD-BANK OF TDB-TDADISTR.\n039840     MOVE TDAD-BRCH OF TDADISTR TO TDB-TDAD-BRCH OF TDB-TDADISTR.\n039842     MOVE TDAD-APPL OF TDADISTR TO TDB-TDAD-APPL OF TDB-TDADISTR.\n039844     MOVE TDAD-CUST OF TDADISTR TO TDB-TDAD-CUST OF TDB-TDADISTR.\n039846     MOVE TDAD-ACCT OF TDADISTR TO TDB-TDAD-ACCT OF TDB-TDADISTR.\n039848     MOVE TDAD-NXT-ACCT-P OF TDADISTR TO TDB-TDAD-NXT-ACCT-P OF   \n039850         TDB-TDADISTR.\n039852     MOVE TDAD-NXT-ACCT-S OF TDADISTR TO TDB-TDAD-NXT-ACCT-S OF   \n039854         TDB-TDADISTR.\n039856     MOVE TDAD-N-ACCT-BY-RT OF TDADISTR TO TDB-TDAD-N-ACCT-BY-RT  \n039858         OF TDB-TDADISTR.\n039860     MOVE TDAD-SERIAL OF TDADISTR TO TDB-TDAD-SERIAL OF           \n039862         TDB-TDADISTR.\n039864     MOVE TDAD-SER-NEXT OF TDADISTR TO TDB-TDAD-SER-NEXT OF       \n039866         TDB-TDADISTR.\n039868     MOVE TDAD-DISP-CD OF TDADISTR TO TDB-TDAD-DISP-CD OF         \n039870         TDB-TDADISTR.\n039872     MOVE TDAD-TYPE OF TDADISTR TO TDB-TDAD-TYPE OF TDB-TDADISTR.\n039874     MOVE TDAD-PRINCIPAL OF TDADISTR TO TDB-TDAD-PRINCIPAL OF     \n039876         TDB-TDADISTR.\n039878     MOVE TDAD-INTEREST OF TDADISTR TO TDB-TDAD-INTEREST OF       \n039880         TDB-TDADISTR.\n039882     MOVE TDAD-DS-CODE OF TDADISTR TO TDB-TDAD-DS-CODE OF         \n039884         TDB-TDADISTR.\n039886     MOVE TDAD-WTHLD-CD OF TDADISTR TO TDB-TDAD-WTHLD-CD OF       \n039888         TDB-TDADISTR.\n039890     MOVE TDAD-WHLD-AMT OF TDADISTR TO TDB-TDAD-WHLD-AMT OF       \n039892         TDB-TDADISTR.\n039894     MOVE TDAD-ST-WHLD-CD OF TDADISTR TO TDB-TDAD-ST-WHLD-CD OF   \n039896         TDB-TDADISTR.\n039898     MOVE TDAD-ST-WHLD-AMT OF TDADISTR TO TDB-TDAD-ST-WHLD-AMT OF \n039900         TDB-TDADISTR.\n039902     MOVE TDAD-TRF-ACCT OF TDADISTR TO TDB-TDAD-TRF-ACCT OF       \n039904         TDB-TDADISTR.\n039906     MOVE TDAD-TRF-ACCT-S OF TDADISTR TO TDB-TDAD-TRF-ACCT-S OF   \n039908         TDB-TDADISTR.\n039910     MOVE TDAD-AMT-CD OF TDADISTR TO TDB-TDAD-AMT-CD OF           \n039912         TDB-TDADISTR.\n039914     MOVE TDAD-DS-AMT OF TDADISTR TO TDB-TDAD-DS-AMT OF           \n039916         TDB-TDADISTR.\n039918     MOVE TDAD-DS-FREQ OF TDADISTR TO TDB-TDAD-DS-FREQ OF         \n039920         TDB-TDADISTR.\n039922     MOVE TDAD-DS-NTRVL OF TDADISTR TO TDB-TDAD-DS-NTRVL OF       \n039924         TDB-TDADISTR.\n039926     MOVE TDAD-END-OF-DIST OF TDADISTR TO TDB-TDAD-END-OF-DIST OF \n039928         TDB-TDADISTR.\n039930     MOVE TDAD-DIST-NTC-CD OF TDADISTR TO TDB-TDAD-DIST-NTC-CD OF \n039932         TDB-TDADISTR.\n039934     MOVE TDAD-EOY-DS-FORM OF TDADISTR TO TDB-TDAD-EOY-DS-FORM OF \n039936         TDB-TDADISTR.\n039938     MOVE TDAD-5-YR-RULE OF TDADISTR TO TDB-TDAD-5-YR-RULE OF     \n039940         TDB-TDADISTR.\n039942     MOVE TDAD-ANUAL-RECALC OF TDADISTR TO TDB-TDAD-ANUAL-RECALC  \n039944         OF TDB-TDADISTR.\n039946     MOVE TDAD-JOINT-CD OF TDADISTR TO TDB-TDAD-JOINT-CD OF       \n039948         TDB-TDADISTR.\n039950     MOVE TDAD-PUB-ID OF TDADISTR TO TDB-TDAD-PUB-ID OF           \n039952         TDB-TDADISTR.\n039954     MOVE TDAD-LST-DIST-DT OF TDADISTR TO TDB-TDAD-LST-DIST-DT OF \n039956         TDB-TDADISTR.\n039958     MOVE TDAD-IN-PROC-DT OF TDADISTR TO TDB-TDAD-IN-PROC-DT OF   \n039960         TDB-TDADISTR.\n039962     MOVE TDAD-NXT-DIST-DT OF TDADISTR TO TDB-TDAD-NXT-DIST-DT OF \n039964         TDB-TDADISTR.\n039966     MOVE TDAD-NXT-DS-PROC OF TDADISTR TO TDB-TDAD-NXT-DS-PROC OF \n039968         TDB-TDADISTR.\n039970     MOVE TDAD-ADD-DT OF TDADISTR TO TDB-TDAD-ADD-DT OF           \n039972         TDB-TDADISTR.\n039974     MOVE TDAD-ADD-TM OF TDADISTR TO TDB-TDAD-ADD-TM OF           \n039976         TDB-TDADISTR.\n039978     MOVE TDAD-MIN-AMT OF TDADISTR TO TDB-TDAD-MIN-AMT OF         \n039980         TDB-TDADISTR.\n039982     MOVE TDAD-AMT OF TDADISTR TO TDB-TDAD-AMT OF TDB-TDADISTR.\n039984     MOVE TDAD-LST-AMT OF TDADISTR TO TDB-TDAD-LST-AMT OF         \n039986         TDB-TDADISTR.\n039988     MOVE TDAD-CUR-WHLD-AMT OF TDADISTR TO TDB-TDAD-CUR-WHLD-AMT  \n039990         OF TDB-TDADISTR.\n039992     MOVE TDAD-WHLD-YTD OF TDADISTR TO TDB-TDAD-WHLD-YTD OF       \n039994         TDB-TDADISTR.\n039996     MOVE TDAD-LST-WHLD-AMT OF TDADISTR TO TDB-TDAD-LST-WHLD-AMT  \n039998         OF TDB-TDADISTR.\n040000     MOVE TDAD-PRINCPL-AMT OF TDADISTR TO TDB-TDAD-PRINCPL-AMT OF \n040002         TDB-TDADISTR.\n040004     MOVE TDAD-INT-AMT OF TDADISTR TO TDB-TDAD-INT-AMT OF         \n040006         TDB-TDADISTR.\n040008     MOVE TDAD-INT-YTD OF TDADISTR TO TDB-TDAD-INT-YTD OF         \n040010         TDB-TDADISTR.\n040012     MOVE TDAD-ST-CUR-W-AMT OF TDADISTR TO TDB-TDAD-ST-CUR-W-AMT  \n040014         OF TDB-TDADISTR.\n040016     MOVE TDAD-ST-LST-W-AMT OF TDADISTR TO TDB-TDAD-ST-LST-W-AMT  \n040018         OF TDB-TDADISTR.\n040020     MOVE TDAD-CK-IND-1 OF TDADISTR TO TDB-TDAD-CK-IND-1 OF       \n040022         TDB-TDADISTR.\n040024     MOVE TDAD-CK-IND-2 OF TDADISTR TO TDB-TDAD-CK-IND-2 OF       \n040026         TDB-TDADISTR.\n040028     MOVE TDAD-LUPD-DT OF TDADISTR TO TDB-TDAD-LUPD-DT OF         \n040030         TDB-TDADISTR.\n040032     MOVE TDAD-LUPD-TM OF TDADISTR TO TDB-TDAD-LUPD-TM OF         \n040034         TDB-TDADISTR.\n040036     MOVE TDAD-RMD-OVERRIDE OF TDADISTR TO TDB-TDAD-RMD-OVERRIDE  \n040038         OF TDB-TDADISTR.\n040040     MOVE TDAD-RMD-AMOUNT OF TDADISTR TO TDB-TDAD-RMD-AMOUNT OF   \n040042         TDB-TDADISTR.\n040044     MOVE TDAD-DS-NBR OF TDADISTR TO TDB-TDAD-DS-NBR OF           \n040046         TDB-TDADISTR.\n040048     IF WS-MULTI-DISTR = 1\n040050         NEXT SENTENCE ELSE\n040052         GO TO Z-5-86-1-ELSE.\n040054************ PERFORM TDD-MINDIST-SETUP-AND-CALC\n040056     PERFORM Z-28-PROCEDURE THRU Z-28-XIT.\n040058     IF  Z-EXIT-EDITEXIT\n040060         GO TO Z-5-XIT.\n040062     IF  Z-DMS2-ABORT-FLAG = 1\n040064         GO TO Z-5-XIT.\n040066     IF  Z-EXIT-LEVEL < 0\n040068         GO TO Z-5-82-END.\n040070*\n040072     IF ( TDB-TDAA-INHERIT-IRA = 2 ) AND ( TDB-TDAA-RMD-MAN-CALC  \n040074         = 0 )\n040076         NEXT SENTENCE ELSE\n040078         GO TO Z-5-88-1-ELSE.\n040080     IF ( TDB-TDAA-BNF-DEATH-DT > 20191231 ) OR ( (               \n040082         TDB-TDAA-IRA-TYPE = 13 OR 15 OR 17 ) AND (               \n040084         TDB-TDAA-BNF-DEATH-DT > 0 ) AND ( TDB-TDAA-BNF-DEATH-DT  \n040086         NOT > 20191231 ) )\n040088         NEXT SENTENCE ELSE\n040090         GO TO Z-5-89-1-ELSE.\n040092     MOVE ZEROS TO WS-MD-FACT\n040094       , WS-MD-TBL\n040096       , WS-MD-AMT.\n040098 Z-5-89-1-ELSE.\n040100 Z-5-88-1-ELSE.\n040102     IF TDB-TDAA-INHERIT-IRA = 0\n040104         NEXT SENTENCE ELSE\n040106         GO TO Z-5-91-1-ELSE.\n040108     ADD WS-MD-FMV TO WS-TIN-BAL-TOT .\n040110     ADD WS-MD-AMT TO WS-TIN-RMD-TOT .\n040112 Z-5-91-1-ELSE.\n040114     IF ( WS-BANK-OPT = 3 ) AND ( TDB-TDAA-RMD-MAN-CALC = ZERO )\n040116         NEXT SENTENCE ELSE\n040118         GO TO Z-5-94-1-ELSE.\n040120 Z-5-95-BEGIN.\n040122*      REQUESTED UPDATE OF FILE CST-FILE-MAINT\n040124     MOVE 1 TO Z-FLINFO6-UPDATE.\n040126     MOVE WS-BANK-NO TO FM2-BANK.\n040128     MOVE TDB-TDAA-CUST TO FM2-CUST.\n040130     MOVE TDB-TDAA-ACCT TO FM2-ACCT.\n040132     MOVE 02 TO FM2-STRUCT.\n040134     MOVE 00 TO FM2-RECORD-NBR.\n040136     MOVE 0067 TO FM2-TRANCODE.\n040138     MOVE WS-MD-AMT TO WS-FM-AMT.\n040140     MOVE WS-FM-AMT-X TO FM2-CHANGE-DATA.\n040142     MOVE \"R\" TO FM2-APPLY.\n040144     MOVE \"RMDRPT\" TO FM2-ORIGIN.\n040146     MOVE SPACE TO FM2-INT.\n040148     MOVE SPACE TO FM2-SYSTEM-USE.\n040150     IF Z-EDIT-ERROR\n040152         GO TO Z-5-XIT.\n040154     IF Z-FLINFO6-UPDATE = 1\n040156         NEXT SENTENCE ELSE\n040158         GO TO Z-5-96-SKIP.\n040160     WRITE MASS-FM-RECORD2\n040162         INVALID KEY\n040164         MOVE Z-FLINFO6-STATUS TO Z-FL-EXCEPT-STATUS\n040166         MOVE \"CST-FILE-MAINT\" TO Z-FL-EXCEPT-FILE\n040168         MOVE 1273 TO Z-FL-EXCEPT-SEQ\n040170         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.\n040172     MOVE Z-FILE6-KEY TO Z-FLINFO6-RS-KEY.\n040174     MOVE ZERO TO Z-FLINFO6-UPDATE.\n040176     MOVE ZERO TO Z-FLINFO6-LAST-SEQ.\n040178 Z-5-96-SKIP.\n040180 Z-5-95-SKIP.\n040182*\n040184 Z-5-95-XIT.\n040186     MOVE 0 TO Z-EXIT-CODE.\n040188     MOVE 9999 TO Z-EXIT-LEVEL.\n040190     MOVE SPACES TO MASS-FM-RECORD2.\n040192 Z-5-110-BEGIN.\n040194*      REQUESTED UPDATE OF FILE CST-FILE-MAINT\n040196     MOVE 2 TO Z-FLINFO6-UPDATE.\n040198     MOVE WS-BANK-NO TO FM2-BANK.\n040200     MOVE TDB-TDAA-CUST TO FM2-CUST.\n040202     MOVE TDB-TDAA-ACCT TO FM2-ACCT.\n040204     MOVE 02 TO FM2-STRUCT.\n040206     MOVE 00 TO FM2-RECORD-NBR.\n040208     MOVE 0397 TO FM2-TRANCODE.\n040210     MOVE WS-MD-FACT TO WS-FM-LEF.\n040212     MOVE WS-FM-LEF-X TO FM2-CHANGE-DATA.\n040214     MOVE \"R\" TO FM2-APPLY.\n040216     MOVE \"RMDRPT\" TO FM2-ORIGIN.\n040218     MOVE SPACE TO FM2-INT\n040220       , FM2-SYSTEM-USE.\n040222     IF Z-EDIT-ERROR\n040224         GO TO Z-5-XIT.\n040226     IF Z-FLINFO6-UPDATE = 2\n040228         NEXT SENTENCE ELSE\n040230         GO TO Z-5-111-SKIP.\n040232     WRITE MASS-FM-RECORD2\n040234         INVALID KEY\n040236         MOVE Z-FLINFO6-STATUS TO Z-FL-EXCEPT-STATUS\n040238         MOVE \"CST-FILE-MAINT\" TO Z-FL-EXCEPT-FILE\n040240         MOVE 1291 TO Z-FL-EXCEPT-SEQ\n040242         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.\n040244     MOVE Z-FILE6-KEY TO Z-FLINFO6-RS-KEY.\n040246     MOVE ZERO TO Z-FLINFO6-UPDATE.\n040248     MOVE ZERO TO Z-FLINFO6-LAST-SEQ.\n040250 Z-5-111-SKIP.\n040252 Z-5-110-SKIP.\n040254*\n040256 Z-5-110-XIT.\n040258     MOVE 0 TO Z-EXIT-CODE.\n040260     MOVE 9999 TO Z-EXIT-LEVEL.\n040262     MOVE SPACES TO MASS-FM-RECORD2.\n040264     IF WS-RMDFM2-CUST-IND = 0\n040266         NEXT SENTENCE ELSE\n040268         GO TO Z-5-124-1-ELSE.\n040270     MOVE 1 TO WS-RMDFM2-CUST-IND.\n040272 Z-5-124-1-ELSE.\n040274 Z-5-94-1-ELSE.\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    486 lines from 19648 to 20133.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 41, "total_chunks": 55, "start_line": 19648, "end_line": 20133, "line_count": 486}

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
- Source code length: 25795 characters

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
CHUNK 41 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 19648 to 20133 (486 lines)
Chunk Tokens (estimated): ~8,075
Actual Input Tokens: 9,481 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 19648-20133 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 41 of 55 chunks
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
      The source code below is only CHUNK 41 of 55.


=============================================================================
CHUNK 41 SOURCE CODE (Lines 19648-20133)
=============================================================================

```cobol
039304 Z-5-40-1-ELSE.
039306     IF NOT Z-SW3
039308         NEXT SENTENCE ELSE
039310         GO TO Z-5-45-1-ELSE.
039312     COMPUTE Z-LINES-HOLD = 1.
039314     COMPUTE Z-LINES = 1.
039316     IF Z-RPT-1-TRAP > ZERO
039318         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
039320     IF Z-LINES > Z-RPT-1-TRAP
039322       IF Z-RPTINFO1-INBLOCK = ZERO
039324         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
039326         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
039328         COMPUTE Z-LINES = 1.
039330     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
039332     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
039334     MOVE RMDRPT-REC-3 TO Z-RPT-1-BUFFER.
039336     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
039338 Z-5-45-1-ELSE.
039340     MOVE SPACES TO RMDRPT-REC-4.
039342     MOVE WS-TIN-DET-LINE-4 (J) TO RMDRPT-REC-4.
039344     IF NOT Z-SW3
039346         NEXT SENTENCE ELSE
039348         GO TO Z-5-49-1-ELSE.
039350     COMPUTE Z-LINES-HOLD = 1.
039352     COMPUTE Z-LINES = 1.
039354     IF Z-RPT-1-TRAP > ZERO
039356         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
039358     IF Z-LINES > Z-RPT-1-TRAP
039360       IF Z-RPTINFO1-INBLOCK = ZERO
039362         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
039364         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
039366         COMPUTE Z-LINES = 1.
039368     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
039370     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
039372     MOVE RMDRPT-REC-4 TO Z-RPT-1-BUFFER.
039374     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
039376 Z-5-49-1-ELSE.
039378     MOVE SPACES TO RMDRPT-REC-8.
039380     IF ( WS-TIN-DET-LINE-8 (J) NOT = SPACES ) AND ( NOT Z-SW3 )
039382         NEXT SENTENCE ELSE
039384         GO TO Z-5-52-1-ELSE.
039386     MOVE WS-TIN-DET-LINE-8 (J) TO RMDRPT-REC-8.
039388     COMPUTE Z-LINES-HOLD = 1.
039390     COMPUTE Z-LINES = 1.
039392     IF Z-RPT-1-TRAP > ZERO
039394         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
039396     IF Z-LINES > Z-RPT-1-TRAP
039398       IF Z-RPTINFO1-INBLOCK = ZERO
039400         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
039402         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
039404         COMPUTE Z-LINES = 1.
039406     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
039408     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
039410     MOVE RMDRPT-REC-8 TO Z-RPT-1-BUFFER.
039412     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
039414 Z-5-52-1-ELSE.
039416 Z-5-36-END.
039418     IF Z-EDIT-ERROR
039420         GO TO Z-5-XIT.
039422 Z-5-36-SKIP.
039424     IF Z-EXIT-LEVEL < 3
039426         GO TO Z-5-14-END.
039428     IF Z-EXIT-CODE > 0
039430         GO TO Z-5-36-XIT.
039432     ADD 1 TO J.
039434     GO TO Z-5-36-LOOP.
039436*
039438 Z-5-36-XIT.
039440     MOVE 0 TO Z-EXIT-CODE.
039442     MOVE 9999 TO Z-EXIT-LEVEL.
039444     MOVE SPACES TO WS-TIN-DETAIL-TABLE.
039446     MOVE 0 TO WS-TIN-DETAIL-INDEX.
039448************ PERFORM COMB-AUTO-RMD-ADJ
039450     IF ( SPECS-COMB-AUTO-RMD-ADJUST = "Y" )
039452        NEXT SENTENCE ELSE
039454        GO TO Z-5-57-SKIPPROC.
039456************ PERFORM COMB-AUTO-RMD-ADJ
039458     PERFORM Z-27-PROCEDURE THRU Z-27-XIT.
039460     IF  Z-EXIT-EDITEXIT
039462         GO TO Z-5-XIT.
039464     IF  Z-DMS2-ABORT-FLAG = 1
039466         GO TO Z-5-XIT.
039468     IF  Z-EXIT-LEVEL < 0
039470         GO TO Z-5-14-END.
039472*
039474 Z-5-57-SKIPPROC.
039476     MOVE 0 TO WS-TIN-DISTR-RECS.
039478 Z-5-35-1-ELSE.
039480     IF WS-NON-INHERIT-IRA-ON-TIN = 1
039482         NEXT SENTENCE ELSE
039484         GO TO Z-5-59-1-ELSE.
039486     MOVE WS-PREV-TIN TO WS-RMDRPT-TIN.
039488     MOVE "-" TO WS-RMDRPT-TIN-LDASH
039490       , WS-RMDRPT-TIN-RDASH.
039492     MOVE WS-RMDRPT-TIN TO RMDRPT-TOT-TIN-9.
039494     MOVE WS-TIN-BAL-TOT TO RMDRPT-TIN-TOT-BAL-9.
039496     MOVE WS-TIN-RMD-TOT TO RMDRPT-TIN-TOT-RMD-9.
039498     IF NOT Z-SW3
039500         NEXT SENTENCE ELSE
039502         GO TO Z-5-65-1-ELSE.
039504     COMPUTE Z-LINES-HOLD = 1.
039506     COMPUTE Z-LINES = 1.
039508     IF Z-RPT-1-TRAP > ZERO
039510         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
039512     IF Z-LINES > Z-RPT-1-TRAP
039514       IF Z-RPTINFO1-INBLOCK = ZERO
039516         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
039518         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
039520         COMPUTE Z-LINES = 1.
039522     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
039524     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
039526     MOVE RMDRPT-REC-9 TO Z-RPT-1-BUFFER.
039528     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
039530     COMPUTE Z-LINES-HOLD = 1.
039532     COMPUTE Z-LINES = 1.
039534     IF Z-RPT-1-TRAP > ZERO
039536         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
039538     IF Z-LINES > Z-RPT-1-TRAP
039540       IF Z-RPTINFO1-INBLOCK = ZERO
039542         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
039544         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
039546         COMPUTE Z-LINES = 1.
039548     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
039550     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
039552     MOVE SPACES TO Z-RPT-1-BUFFER.
039554     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
039556 Z-5-65-1-ELSE.
039558 Z-5-59-1-ELSE.
039560     IF WS-INHERIT-IRA-ON-TIN = 1
039562         NEXT SENTENCE ELSE
039564         GO TO Z-5-68-1-ELSE.
039566     MOVE WS-PREV-TIN TO WS-RMDRPT2-TIN.
039568     MOVE "-" TO WS-RMDRPT2-TIN-LDASH
039570       , WS-RMDRPT2-TIN-RDASH.
039572     MOVE WS-RMDRPT2-TIN TO RMDRPT-TOT-TIN-10.
039574     IF NOT Z-SW3
039576         NEXT SENTENCE ELSE
039578         GO TO Z-5-72-1-ELSE.
039580     COMPUTE Z-LINES-HOLD = 1.
039582     COMPUTE Z-LINES = 1.
039584     IF Z-RPT-2-TRAP > ZERO
039586         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.
039588     IF Z-LINES > Z-RPT-2-TRAP
039590       IF Z-RPTINFO2-INBLOCK = ZERO
039592         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1
039594         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT
039596         COMPUTE Z-LINES = 1.
039598     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).
039600     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).
039602     MOVE RMDRPT-REC-10 TO Z-RPT-2-BUFFER.
039604     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.
039606     COMPUTE Z-LINES-HOLD = 1.
039608     COMPUTE Z-LINES = 1.
039610     IF Z-RPT-2-TRAP > ZERO
039612         COMPUTE Z-RPT-2-TRAP = Z-RPT-2-PAGE-SIZE - Z-RPT-2-LINE.
039614     IF Z-LINES > Z-RPT-2-TRAP
039616       IF Z-RPTINFO2-INBLOCK = ZERO
039618         COMPUTE Z-LINES = Z-RPT-2-TRAP + 1
039620         PERFORM Z-RPT-2-NEWPAGE THRU Z-RPT-2-NEWPAGE-XIT
039622         COMPUTE Z-LINES = 1.
039624     COMPUTE Z-RPT-2-LINE = Z-RPT-2-LINE + (Z-LINES).
039626     COMPUTE Z-RPT-2-TRAP = Z-RPT-2-TRAP - (Z-LINES).
039628     MOVE SPACES TO Z-RPT-2-BUFFER.
039630     WRITE Z-RPT-2-BUFFER AFTER ADVANCING Z-LINES.
039632 Z-5-72-1-ELSE.
039634 Z-5-68-1-ELSE.
039636     MOVE ZEROS TO WS-TIN-TOTALS
039638       , WS-INHERIT-IRA-ON-TIN
039640       , WS-NON-INHERIT-IRA-ON-TIN.
039642     IF ( WS-TIN-RMD-TOT NOT = 0 ) AND ( NOT Z-SW3 )
039644         NEXT SENTENCE ELSE
039646         GO TO Z-5-76-1-ELSE.
039648     COMPUTE Z-LINES-HOLD = 1.
039650     COMPUTE Z-LINES = 1.
039652     IF Z-RPT-1-TRAP > ZERO
039654         COMPUTE Z-RPT-1-TRAP = Z-RPT-1-PAGE-SIZE - Z-RPT-1-LINE.
039656     IF Z-LINES > Z-RPT-1-TRAP
039658       IF Z-RPTINFO1-INBLOCK = ZERO
039660         COMPUTE Z-LINES = Z-RPT-1-TRAP + 1
039662         PERFORM Z-RPT-1-NEWPAGE THRU Z-RPT-1-NEWPAGE-XIT
039664         COMPUTE Z-LINES = 1.
039666     COMPUTE Z-RPT-1-LINE = Z-RPT-1-LINE + (Z-LINES).
039668     COMPUTE Z-RPT-1-TRAP = Z-RPT-1-TRAP - (Z-LINES).
039670     MOVE SPACES TO Z-RPT-1-BUFFER.
039672     WRITE Z-RPT-1-BUFFER AFTER ADVANCING Z-LINES.
039674 Z-5-76-1-ELSE.
039676     MOVE TDB-TDAC-TIN-NBR TO WS-PREV-TIN.
039678 Z-5-34-1-ELSE.
039680     MOVE 0 TO WS-MULTI-DISTR
039682       , WS-IRA-DISTR-RECS.
039684     MOVE ZERO TO Z-FLINFO13-PRES.
039686     MOVE ZERO TO Z-FLINFO13-SOME.
039688     MOVE 11 TO Z-FLINFO13-LAST-SEQ.
039690*
039692     SET TDADSNBRSET OF TDADISTR OF LDBTDADB TO BEGINNING
039694         ON EXCEPTION
039696         MOVE "TDADSNBRSET OF TDADISTR OF LDBTDADB" TO            
039698             Z-DMS-EXCEPT-STR
039700         MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
039702         MOVE 11 TO Z-DMS-EXCEPT-SEQ
039704         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT
039706         GO TO Z-5-80-XIT.
039708 Z-5-80-LOOP.
039710     MOVE ZERO TO Z-FLINFO13-PRES.
039712 Z-5-80-READ.
039714     FIND KEY OF NEXT TDADSNBRSET OF TDADISTR OF LDBTDADB
039716     AT TDAD-BANK = WS-BANK-NO AND
039718        TDAD-CUST = TDB-TDAI-CUST AND
039720        TDAD-ACCT = TDB-TDAI-ACCT
039722         ON EXCEPTION
039724         MOVE 11 TO Z-DMS-EXCEPT-SEQ
039726         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
039728             GO TO Z-5-80-XIT
039730         ELSE
039732             MOVE "TDADSNBRSET OF TDADISTR OF LDBTDADB" TO        
039734                 Z-DMS-EXCEPT-STR
039736             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
039738             MOVE 11 TO Z-DMS-EXCEPT-SEQ
039740             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
039742
039744*
039746     MOVE 1 TO Z-FLINFO13-PRES.
039748     MOVE 1 TO Z-FLINFO13-SOME.
039750     ADD 1 TO WS-IRA-DISTR-RECS , WS-TIN-DISTR-RECS .
039752     IF Z-EDIT-ERROR
039754         GO TO Z-5-XIT.
039756 Z-5-80-SKIP.
039758     GO TO Z-5-80-LOOP.
039760*
039762 Z-5-80-XIT.
039764     MOVE ZERO TO Z-FLINFO13-PRES.
039766     MOVE ZERO TO Z-FLINFO13-SOME.
039768     MOVE 12 TO Z-FLINFO13-LAST-SEQ.
039770*
039772     SET TDADSSET OF TDADISTR OF LDBTDADB TO BEGINNING
039774         ON EXCEPTION
039776         MOVE "TDADSSET OF TDADISTR OF LDBTDADB" TO               
039778             Z-DMS-EXCEPT-STR
039780         MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
039782         MOVE 12 TO Z-DMS-EXCEPT-SEQ
039784         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT
039786         GO TO Z-5-82-XIT.
039788 Z-5-82-LOOP.
039790     MOVE ZERO TO Z-FLINFO13-PRES.
039792 Z-5-82-READ.
039794     FIND TDADISTR OF LDBTDADB VIA NEXT TDADSSET OF TDADISTR OF   
039796         LDBTDADB
039798     AT TDAD-BANK = WS-BANK-NO AND
039800        TDAD-CUST = TDB-TDAI-CUST AND
039802        TDAD-ACCT = TDB-TDAI-ACCT
039804         ON EXCEPTION
039806         MOVE 12 TO Z-DMS-EXCEPT-SEQ
039808         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
039810             GO TO Z-5-82-XIT
039812         ELSE
039814             MOVE "TDADSSET OF TDADISTR OF LDBTDADB" TO           
039816                 Z-DMS-EXCEPT-STR
039818             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
039820             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
039822
039824*
039826     MOVE 1 TO Z-FLINFO13-PRES.
039828     MOVE 1 TO Z-FLINFO13-SOME.
039830     MOVE 0 TO Z-EXIT-CODE.
039832     MOVE 9999 TO Z-EXIT-LEVEL.
039834     MOVE 1 TO WS-DSREC-FLAG.
039836     ADD 1 TO WS-MULTI-DISTR .
039838     MOVE TDAD-BANK OF TDADISTR TO TDB-TDAD-BANK OF TDB-TDADISTR.
039840     MOVE TDAD-BRCH OF TDADISTR TO TDB-TDAD-BRCH OF TDB-TDADISTR.
039842     MOVE TDAD-APPL OF TDADISTR TO TDB-TDAD-APPL OF TDB-TDADISTR.
039844     MOVE TDAD-CUST OF TDADISTR TO TDB-TDAD-CUST OF TDB-TDADISTR.
039846     MOVE TDAD-ACCT OF TDADISTR TO TDB-TDAD-ACCT OF TDB-TDADISTR.
039848     MOVE TDAD-NXT-ACCT-P OF TDADISTR TO TDB-TDAD-NXT-ACCT-P OF   
039850         TDB-TDADISTR.
039852     MOVE TDAD-NXT-ACCT-S OF TDADISTR TO TDB-TDAD-NXT-ACCT-S OF   
039854         TDB-TDADISTR.
039856     MOVE TDAD-N-ACCT-BY-RT OF TDADISTR TO TDB-TDAD-N-ACCT-BY-RT  
039858         OF TDB-TDADISTR.
039860     MOVE TDAD-SERIAL OF TDADISTR TO TDB-TDAD-SERIAL OF           
039862         TDB-TDADISTR.
039864     MOVE TDAD-SER-NEXT OF TDADISTR TO TDB-TDAD-SER-NEXT OF       
039866         TDB-TDADISTR.
039868     MOVE TDAD-DISP-CD OF TDADISTR TO TDB-TDAD-DISP-CD OF         
039870         TDB-TDADISTR.
039872     MOVE TDAD-TYPE OF TDADISTR TO TDB-TDAD-TYPE OF TDB-TDADISTR.
039874     MOVE TDAD-PRINCIPAL OF TDADISTR TO TDB-TDAD-PRINCIPAL OF     
039876         TDB-TDADISTR.
039878     MOVE TDAD-INTEREST OF TDADISTR TO TDB-TDAD-INTEREST OF       
039880         TDB-TDADISTR.
039882     MOVE TDAD-DS-CODE OF TDADISTR TO TDB-TDAD-DS-CODE OF         
039884         TDB-TDADISTR.
039886     MOVE TDAD-WTHLD-CD OF TDADISTR TO TDB-TDAD-WTHLD-CD OF       
039888         TDB-TDADISTR.
039890     MOVE TDAD-WHLD-AMT OF TDADISTR TO TDB-TDAD-WHLD-AMT OF       
039892         TDB-TDADISTR.
039894     MOVE TDAD-ST-WHLD-CD OF TDADISTR TO TDB-TDAD-ST-WHLD-CD OF   
039896         TDB-TDADISTR.
039898     MOVE TDAD-ST-WHLD-AMT OF TDADISTR TO TDB-TDAD-ST-WHLD-AMT OF 
039900         TDB-TDADISTR.
039902     MOVE TDAD-TRF-ACCT OF TDADISTR TO TDB-TDAD-TRF-ACCT OF       
039904         TDB-TDADISTR.
039906     MOVE TDAD-TRF-ACCT-S OF TDADISTR TO TDB-TDAD-TRF-ACCT-S OF   
039908         TDB-TDADISTR.
039910     MOVE TDAD-AMT-CD OF TDADISTR TO TDB-TDAD-AMT-CD OF           
039912         TDB-TDADISTR.
039914     MOVE TDAD-DS-AMT OF TDADISTR TO TDB-TDAD-DS-AMT OF           
039916         TDB-TDADISTR.
039918     MOVE TDAD-DS-FREQ OF TDADISTR TO TDB-TDAD-DS-FREQ OF         
039920         TDB-TDADISTR.
039922     MOVE TDAD-DS-NTRVL OF TDADISTR TO TDB-TDAD-DS-NTRVL OF       
039924         TDB-TDADISTR.
039926     MOVE TDAD-END-OF-DIST OF TDADISTR TO TDB-TDAD-END-OF-DIST OF 
039928         TDB-TDADISTR.
039930     MOVE TDAD-DIST-NTC-CD OF TDADISTR TO TDB-TDAD-DIST-NTC-CD OF 
039932         TDB-TDADISTR.
039934     MOVE TDAD-EOY-DS-FORM OF TDADISTR TO TDB-TDAD-EOY-DS-FORM OF 
039936         TDB-TDADISTR.
039938     MOVE TDAD-5-YR-RULE OF TDADISTR TO TDB-TDAD-5-YR-RULE OF     
039940         TDB-TDADISTR.
039942     MOVE TDAD-ANUAL-RECALC OF TDADISTR TO TDB-TDAD-ANUAL-RECALC  
039944         OF TDB-TDADISTR.
039946     MOVE TDAD-JOINT-CD OF TDADISTR TO TDB-TDAD-JOINT-CD OF       
039948         TDB-TDADISTR.
039950     MOVE TDAD-PUB-ID OF TDADISTR TO TDB-TDAD-PUB-ID OF           
039952         TDB-TDADISTR.
039954     MOVE TDAD-LST-DIST-DT OF TDADISTR TO TDB-TDAD-LST-DIST-DT OF 
039956         TDB-TDADISTR.
039958     MOVE TDAD-IN-PROC-DT OF TDADISTR TO TDB-TDAD-IN-PROC-DT OF   
039960         TDB-TDADISTR.
039962     MOVE TDAD-NXT-DIST-DT OF TDADISTR TO TDB-TDAD-NXT-DIST-DT OF 
039964         TDB-TDADISTR.
039966     MOVE TDAD-NXT-DS-PROC OF TDADISTR TO TDB-TDAD-NXT-DS-PROC OF 
039968         TDB-TDADISTR.
039970     MOVE TDAD-ADD-DT OF TDADISTR TO TDB-TDAD-ADD-DT OF           
039972         TDB-TDADISTR.
039974     MOVE TDAD-ADD-TM OF TDADISTR TO TDB-TDAD-ADD-TM OF           
039976         TDB-TDADISTR.
039978     MOVE TDAD-MIN-AMT OF TDADISTR TO TDB-TDAD-MIN-AMT OF         
039980         TDB-TDADISTR.
039982     MOVE TDAD-AMT OF TDADISTR TO TDB-TDAD-AMT OF TDB-TDADISTR.
039984     MOVE TDAD-LST-AMT OF TDADISTR TO TDB-TDAD-LST-AMT OF         
039986         TDB-TDADISTR.
039988     MOVE TDAD-CUR-WHLD-AMT OF TDADISTR TO TDB-TDAD-CUR-WHLD-AMT  
039990         OF TDB-TDADISTR.
039992     MOVE TDAD-WHLD-YTD OF TDADISTR TO TDB-TDAD-WHLD-YTD OF       
039994         TDB-TDADISTR.
039996     MOVE TDAD-LST-WHLD-AMT OF TDADISTR TO TDB-TDAD-LST-WHLD-AMT  
039998         OF TDB-TDADISTR.
040000     MOVE TDAD-PRINCPL-AMT OF TDADISTR TO TDB-TDAD-PRINCPL-AMT OF 
040002         TDB-TDADISTR.
040004     MOVE TDAD-INT-AMT OF TDADISTR TO TDB-TDAD-INT-AMT OF         
040006         TDB-TDADISTR.
040008     MOVE TDAD-INT-YTD OF TDADISTR TO TDB-TDAD-INT-YTD OF         
040010         TDB-TDADISTR.
040012     MOVE TDAD-ST-CUR-W-AMT OF TDADISTR TO TDB-TDAD-ST-CUR-W-AMT  
040014         OF TDB-TDADISTR.
040016     MOVE TDAD-ST-LST-W-AMT OF TDADISTR TO TDB-TDAD-ST-LST-W-AMT  
040018         OF TDB-TDADISTR.
040020     MOVE TDAD-CK-IND-1 OF TDADISTR TO TDB-TDAD-CK-IND-1 OF       
040022         TDB-TDADISTR.
040024     MOVE TDAD-CK-IND-2 OF TDADISTR TO TDB-TDAD-CK-IND-2 OF       
040026         TDB-TDADISTR.
040028     MOVE TDAD-LUPD-DT OF TDADISTR TO TDB-TDAD-LUPD-DT OF         
040030         TDB-TDADISTR.
040032     MOVE TDAD-LUPD-TM OF TDADISTR TO TDB-TDAD-LUPD-TM OF         
040034         TDB-TDADISTR.
040036     MOVE TDAD-RMD-OVERRIDE OF TDADISTR TO TDB-TDAD-RMD-OVERRIDE  
040038         OF TDB-TDADISTR.
040040     MOVE TDAD-RMD-AMOUNT OF TDADISTR TO TDB-TDAD-RMD-AMOUNT OF   
040042         TDB-TDADISTR.
040044     MOVE TDAD-DS-NBR OF TDADISTR TO TDB-TDAD-DS-NBR OF           
040046         TDB-TDADISTR.
040048     IF WS-MULTI-DISTR = 1
040050         NEXT SENTENCE ELSE
040052         GO TO Z-5-86-1-ELSE.
040054************ PERFORM TDD-MINDIST-SETUP-AND-CALC
040056     PERFORM Z-28-PROCEDURE THRU Z-28-XIT.
040058     IF  Z-EXIT-EDITEXIT
040060         GO TO Z-5-XIT.
040062     IF  Z-DMS2-ABORT-FLAG = 1
040064         GO TO Z-5-XIT.
040066     IF  Z-EXIT-LEVEL < 0
040068         GO TO Z-5-82-END.
040070*
040072     IF ( TDB-TDAA-INHERIT-IRA = 2 ) AND ( TDB-TDAA-RMD-MAN-CALC  
040074         = 0 )
040076         NEXT SENTENCE ELSE
040078         GO TO Z-5-88-1-ELSE.
040080     IF ( TDB-TDAA-BNF-DEATH-DT > 20191231 ) OR ( (               
040082         TDB-TDAA-IRA-TYPE = 13 OR 15 OR 17 ) AND (               
040084         TDB-TDAA-BNF-DEATH-DT > 0 ) AND ( TDB-TDAA-BNF-DEATH-DT  
040086         NOT > 20191231 ) )
040088         NEXT SENTENCE ELSE
040090         GO TO Z-5-89-1-ELSE.
040092     MOVE ZEROS TO WS-MD-FACT
040094       , WS-MD-TBL
040096       , WS-MD-AMT.
040098 Z-5-89-1-ELSE.
040100 Z-5-88-1-ELSE.
040102     IF TDB-TDAA-INHERIT-IRA = 0
040104         NEXT SENTENCE ELSE
040106         GO TO Z-5-91-1-ELSE.
040108     ADD WS-MD-FMV TO WS-TIN-BAL-TOT .
040110     ADD WS-MD-AMT TO WS-TIN-RMD-TOT .
040112 Z-5-91-1-ELSE.
040114     IF ( WS-BANK-OPT = 3 ) AND ( TDB-TDAA-RMD-MAN-CALC = ZERO )
040116         NEXT SENTENCE ELSE
040118         GO TO Z-5-94-1-ELSE.
040120 Z-5-95-BEGIN.
040122*      REQUESTED UPDATE OF FILE CST-FILE-MAINT
040124     MOVE 1 TO Z-FLINFO6-UPDATE.
040126     MOVE WS-BANK-NO TO FM2-BANK.
040128     MOVE TDB-TDAA-CUST TO FM2-CUST.
040130     MOVE TDB-TDAA-ACCT TO FM2-ACCT.
040132     MOVE 02 TO FM2-STRUCT.
040134     MOVE 00 TO FM2-RECORD-NBR.
040136     MOVE 0067 TO FM2-TRANCODE.
040138     MOVE WS-MD-AMT TO WS-FM-AMT.
040140     MOVE WS-FM-AMT-X TO FM2-CHANGE-DATA.
040142     MOVE "R" TO FM2-APPLY.
040144     MOVE "RMDRPT" TO FM2-ORIGIN.
040146     MOVE SPACE TO FM2-INT.
040148     MOVE SPACE TO FM2-SYSTEM-USE.
040150     IF Z-EDIT-ERROR
040152         GO TO Z-5-XIT.
040154     IF Z-FLINFO6-UPDATE = 1
040156         NEXT SENTENCE ELSE
040158         GO TO Z-5-96-SKIP.
040160     WRITE MASS-FM-RECORD2
040162         INVALID KEY
040164         MOVE Z-FLINFO6-STATUS TO Z-FL-EXCEPT-STATUS
040166         MOVE "CST-FILE-MAINT" TO Z-FL-EXCEPT-FILE
040168         MOVE 1273 TO Z-FL-EXCEPT-SEQ
040170         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.
040172     MOVE Z-FILE6-KEY TO Z-FLINFO6-RS-KEY.
040174     MOVE ZERO TO Z-FLINFO6-UPDATE.
040176     MOVE ZERO TO Z-FLINFO6-LAST-SEQ.
040178 Z-5-96-SKIP.
040180 Z-5-95-SKIP.
040182*
040184 Z-5-95-XIT.
040186     MOVE 0 TO Z-EXIT-CODE.
040188     MOVE 9999 TO Z-EXIT-LEVEL.
040190     MOVE SPACES TO MASS-FM-RECORD2.
040192 Z-5-110-BEGIN.
040194*      REQUESTED UPDATE OF FILE CST-FILE-MAINT
040196     MOVE 2 TO Z-FLINFO6-UPDATE.
040198     MOVE WS-BANK-NO TO FM2-BANK.
040200     MOVE TDB-TDAA-CUST TO FM2-CUST.
040202     MOVE TDB-TDAA-ACCT TO FM2-ACCT.
040204     MOVE 02 TO FM2-STRUCT.
040206     MOVE 00 TO FM2-RECORD-NBR.
040208     MOVE 0397 TO FM2-TRANCODE.
040210     MOVE WS-MD-FACT TO WS-FM-LEF.
040212     MOVE WS-FM-LEF-X TO FM2-CHANGE-DATA.
040214     MOVE "R" TO FM2-APPLY.
040216     MOVE "RMDRPT" TO FM2-ORIGIN.
040218     MOVE SPACE TO FM2-INT
040220       , FM2-SYSTEM-USE.
040222     IF Z-EDIT-ERROR
040224         GO TO Z-5-XIT.
040226     IF Z-FLINFO6-UPDATE = 2
040228         NEXT SENTENCE ELSE
040230         GO TO Z-5-111-SKIP.
040232     WRITE MASS-FM-RECORD2
040234         INVALID KEY
040236         MOVE Z-FLINFO6-STATUS TO Z-FL-EXCEPT-STATUS
040238         MOVE "CST-FILE-MAINT" TO Z-FL-EXCEPT-FILE
040240         MOVE 1291 TO Z-FL-EXCEPT-SEQ
040242         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.
040244     MOVE Z-FILE6-KEY TO Z-FLINFO6-RS-KEY.
040246     MOVE ZERO TO Z-FLINFO6-UPDATE.
040248     MOVE ZERO TO Z-FLINFO6-LAST-SEQ.
040250 Z-5-111-SKIP.
040252 Z-5-110-SKIP.
040254*
040256 Z-5-110-XIT.
040258     MOVE 0 TO Z-EXIT-CODE.
040260     MOVE 9999 TO Z-EXIT-LEVEL.
040262     MOVE SPACES TO MASS-FM-RECORD2.
040264     IF WS-RMDFM2-CUST-IND = 0
040266         NEXT SENTENCE ELSE
040268         GO TO Z-5-124-1-ELSE.
040270     MOVE 1 TO WS-RMDFM2-CUST-IND.
040272 Z-5-124-1-ELSE.
040274 Z-5-94-1-ELSE.
```

⚠️  This is the source code you must document.
    486 lines from 19648 to 20133.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

