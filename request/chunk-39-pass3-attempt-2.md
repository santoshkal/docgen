# LLM Request Debug File
Generated: 2025-11-14T19:21:20.291338

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 39/55
- **Model**: gpt-4.1
- **Chunk Number**: 39
- **Pass Number**: 3
- **Attempt Number**: 2 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~7,072 tokens
- **Total Input**: ~9,030 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 39/55" (ID: detailed-code-explanation)

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


**CHUNK 39 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-14T17:36:35.036798", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 39 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 18827 to 19227 (401 lines)\nChunk Tokens (estimated): ~8,084\nActual Input Tokens: 9,490 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 18827-19227 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 39 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 39 of 55.\n\n\n=============================================================================\nCHUNK 39 SOURCE CODE (Lines 18827-19227)\n=============================================================================\n\n```cobol\n037662         TDB-TDAACCT.\n037664     MOVE TDAA-TEMP-EXP-DT OF TDAACCT TO TDB-TDAA-TEMP-EXP-DT OF  \n037666         TDB-TDAACCT.\n037668     MOVE TDAA-END-OF-INT OF TDAACCT TO TDB-TDAA-END-OF-INT OF    \n037670         TDB-TDAACCT.\n037672     MOVE TDAA-END-OF-MAT OF TDAACCT TO TDB-TDAA-END-OF-MAT OF    \n037674         TDB-TDAACCT.\n037676     MOVE TDAA-END-OF-STMT OF TDAACCT TO TDB-TDAA-END-OF-STMT OF  \n037678         TDB-TDAACCT.\n037680     MOVE TDAA-END-OF-CMPD OF TDAACCT TO TDB-TDAA-END-OF-CMPD OF  \n037682         TDB-TDAACCT.\n037684     MOVE TDAA-END-OF-FEE OF TDAACCT TO TDB-TDAA-END-OF-FEE OF    \n037686         TDB-TDAACCT.\n037688     MOVE TDAA-OFFICER OF TDAACCT TO TDB-TDAA-OFFICER OF          \n037690         TDB-TDAACCT.\n037692     MOVE TDAA-OFFICER-2 OF TDAACCT TO TDB-TDAA-OFFICER-2 OF      \n037694         TDB-TDAACCT.\n037696     MOVE TDAA-OFFICER-3 OF TDAACCT TO TDB-TDAA-OFFICER-3 OF      \n037698         TDB-TDAACCT.\n037700     MOVE TDAA-FREE-MARK OF TDAACCT TO TDB-TDAA-FREE-MARK OF      \n037702         TDB-TDAACCT.\n037704     MOVE TDAA-CLASS-CD OF TDAACCT TO TDB-TDAA-CLASS-CD OF        \n037706         TDB-TDAACCT.\n037708     MOVE TDAA-CORR-BK-CD OF TDAACCT TO TDB-TDAA-CORR-BK-CD OF    \n037710         TDB-TDAACCT.\n037712     MOVE TDAA-PUBLIC-FUND OF TDAACCT TO TDB-TDAA-PUBLIC-FUND OF  \n037714         TDB-TDAACCT.\n037716     MOVE TDAA-TRUST-CD OF TDAACCT TO TDB-TDAA-TRUST-CD OF        \n037718         TDB-TDAACCT.\n037720     MOVE TDAA-RT-CHG-ALLOW OF TDAACCT TO TDB-TDAA-RT-CHG-ALLOW   \n037722         OF TDB-TDAACCT.\n037724     MOVE TDAA-WTHDRW-ALLOW OF TDAACCT TO TDB-TDAA-WTHDRW-ALLOW   \n037726         OF TDB-TDAACCT.\n037728     MOVE TDAA-DPOSIT-ALLOW OF TDAACCT TO TDB-TDAA-DPOSIT-ALLOW   \n037730         OF TDB-TDAACCT.\n037732     MOVE TDAA-POST-MAT OF TDAACCT TO TDB-TDAA-POST-MAT OF        \n037734         TDB-TDAACCT.\n037736     MOVE TDAA-RT-FLOOR OF TDAACCT TO TDB-TDAA-RT-FLOOR OF        \n037738         TDB-TDAACCT.\n037740     MOVE TDAA-REPO-CD OF TDAACCT TO TDB-TDAA-REPO-CD OF          \n037742         TDB-TDAACCT.\n037744     MOVE TDAA-TOTAL-CD OF TDAACCT TO TDB-TDAA-TOTAL-CD OF        \n037746         TDB-TDAACCT.\n037748     MOVE TDAA-REN-TOTAL-CD OF TDAACCT TO TDB-TDAA-REN-TOTAL-CD   \n037750         OF TDB-TDAACCT.\n037752     MOVE TDAA-ORG-TOTAL-CD OF TDAACCT TO TDB-TDAA-ORG-TOTAL-CD   \n037754         OF TDB-TDAACCT.\n037756     MOVE TDAA-INQ-SECR-CD OF TDAACCT TO TDB-TDAA-INQ-SECR-CD OF  \n037758         TDB-TDAACCT.\n037760     MOVE TDAA-MAIL-CD OF TDAACCT TO TDB-TDAA-MAIL-CD OF          \n037762         TDB-TDAACCT.\n037764     MOVE TDAA-WTHD-REQD-CD OF TDAACCT TO TDB-TDAA-WTHD-REQD-CD   \n037766         OF TDB-TDAACCT.\n037768     MOVE TDAA-TICKLER-FLAG OF TDAACCT TO TDB-TDAA-TICKLER-FLAG   \n037770         OF TDB-TDAACCT.\n037772     MOVE TDAA-DISP-CD OF TDAACCT TO TDB-TDAA-DISP-CD OF          \n037774         TDB-TDAACCT.\n037776     MOVE TDAA-CLS-DISP-CD OF TDAACCT TO TDB-TDAA-CLS-DISP-CD OF  \n037778         TDB-TDAACCT.\n037780     MOVE TDAA-DIST-STATUS OF TDAACCT TO TDB-TDAA-DIST-STATUS OF  \n037782         TDB-TDAACCT.\n037784     MOVE TDAA-COMM-ACCT OF TDAACCT TO TDB-TDAA-COMM-ACCT OF      \n037786         TDB-TDAACCT.\n037788     MOVE TDAA-RENEW-CD OF TDAACCT TO TDB-TDAA-RENEW-CD OF        \n037790         TDB-TDAACCT.\n037792     MOVE TDAA-PLEDGE-CD OF TDAACCT TO TDB-TDAA-PLEDGE-CD OF      \n037794         TDB-TDAACCT.\n037796     MOVE TDAA-NEGOT-CD OF TDAACCT TO TDB-TDAA-NEGOT-CD OF        \n037798         TDB-TDAACCT.\n037800     MOVE TDAA-BENEF-CD OF TDAACCT TO TDB-TDAA-BENEF-CD OF        \n037802         TDB-TDAACCT.\n037804     MOVE TDAA-COMM-MAT-CD OF TDAACCT TO TDB-TDAA-COMM-MAT-CD OF  \n037806         TDB-TDAACCT.\n037808     MOVE TDAA-NBR-BENEF OF TDAACCT TO TDB-TDAA-NBR-BENEF OF      \n037810         TDB-TDAACCT.\n037812     MOVE TDAA-OVERRIDE OF TDAACCT TO TDB-TDAA-OVERRIDE OF        \n037814         TDB-TDAACCT.\n037816     MOVE TDAA-INT-CD OF TDAACCT TO TDB-TDAA-INT-CD OF            \n037818         TDB-TDAACCT.\n037820     MOVE TDAA-WTHLD-CD OF TDAACCT TO TDB-TDAA-WTHLD-CD OF        \n037822         TDB-TDAACCT.\n037824     MOVE TDAA-WTHLD-AMT OF TDAACCT TO TDB-TDAA-WTHLD-AMT OF      \n037826         TDB-TDAACCT.\n037828     MOVE TDAA-IGL-GRP OF TDAACCT TO TDB-TDAA-IGL-GRP OF          \n037830         TDB-TDAACCT.\n037832     MOVE TDAA-SUM-STMT-CD OF TDAACCT TO TDB-TDAA-SUM-STMT-CD OF  \n037834         TDB-TDAACCT.\n037836     MOVE TDAA-REN-NTC-CD OF TDAACCT TO TDB-TDAA-REN-NTC-CD OF    \n037838         TDB-TDAACCT.\n037840     MOVE TDAA-PMAT-NTC-CD OF TDAACCT TO TDB-TDAA-PMAT-NTC-CD OF  \n037842         TDB-TDAACCT.\n037844     MOVE TDAA-RTCHG-NTC-CD OF TDAACCT TO TDB-TDAA-RTCHG-NTC-CD   \n037846         OF TDB-TDAACCT.\n037848     MOVE TDAA-INT-NTC-CD OF TDAACCT TO TDB-TDAA-INT-NTC-CD OF    \n037850         TDB-TDAACCT.\n037852     MOVE TDAA-CHG-NTC OF TDAACCT TO TDB-TDAA-CHG-NTC OF          \n037854         TDB-TDAACCT.\n037856     MOVE TDAA-YIELD-NUM OF TDAACCT TO TDB-TDAA-YIELD-NUM OF      \n037858         TDB-TDAACCT.\n037860     MOVE TDAA-YIELD-DENOM OF TDAACCT TO TDB-TDAA-YIELD-DENOM OF  \n037862         TDB-TDAACCT.\n037864     MOVE TDAA-CMPD-FREQ OF TDAACCT TO TDB-TDAA-CMPD-FREQ OF      \n037866         TDB-TDAACCT.\n037868     MOVE TDAA-CMPD-NTRVL OF TDAACCT TO TDB-TDAA-CMPD-NTRVL OF    \n037870         TDB-TDAACCT.\n037872     MOVE TDAA-RT-CHG-LIMIT OF TDAACCT TO TDB-TDAA-RT-CHG-LIMIT   \n037874         OF TDB-TDAACCT.\n037876     MOVE TDAA-VAR-RT-IMMED OF TDAACCT TO TDB-TDAA-VAR-RT-IMMED   \n037878         OF TDB-TDAACCT.\n037880     MOVE TDAA-VAR-RT-INT OF TDAACCT TO TDB-TDAA-VAR-RT-INT OF    \n037882         TDB-TDAACCT.\n037884     MOVE TDAA-VAR-RT-SCHED OF TDAACCT TO TDB-TDAA-VAR-RT-SCHED   \n037886         OF TDB-TDAACCT.\n037888     MOVE TDAA-VAR-RT-CUST OF TDAACCT TO TDB-TDAA-VAR-RT-CUST OF  \n037890         TDB-TDAACCT.\n037892     MOVE TDAA-VAR-RT-BAL OF TDAACCT TO TDB-TDAA-VAR-RT-BAL OF    \n037894         TDB-TDAACCT.\n037896     MOVE TDAA-RT-INDX-CD OF TDAACCT TO TDB-TDAA-RT-INDX-CD OF    \n037898         TDB-TDAACCT.\n037900     MOVE TDAA-R-RT-INDX-CD OF TDAACCT TO TDB-TDAA-R-RT-INDX-CD   \n037902         OF TDB-TDAACCT.\n037904     MOVE TDAA-RT-MARG-CD OF TDAACCT TO TDB-TDAA-RT-MARG-CD OF    \n037906         TDB-TDAACCT.\n037908     MOVE TDAA-R-RT-MARG-CD OF TDAACCT TO TDB-TDAA-R-RT-MARG-CD   \n037910         OF TDB-TDAACCT.\n037912     MOVE TDAA-RT-TIER-CD OF TDAACCT TO TDB-TDAA-RT-TIER-CD OF    \n037914         TDB-TDAACCT.\n037916     MOVE TDAA-R-RT-TIER-CD OF TDAACCT TO TDB-TDAA-R-RT-TIER-CD   \n037918         OF TDB-TDAACCT.\n037920     MOVE TDAA-RT-SR-CD OF TDAACCT TO TDB-TDAA-RT-SR-CD OF        \n037922         TDB-TDAACCT.\n037924     MOVE TDAA-R-RT-SR-CD OF TDAACCT TO TDB-TDAA-R-RT-SR-CD OF    \n037926         TDB-TDAACCT.\n037928     MOVE TDAA-RT-REGN-CD OF TDAACCT TO TDB-TDAA-RT-REGN-CD OF    \n037930         TDB-TDAACCT.\n037932     MOVE TDAA-RT-CHG-NTRVL OF TDAACCT TO TDB-TDAA-RT-CHG-NTRVL   \n037934         OF TDB-TDAACCT.\n037936     MOVE TDAA-CAP-RT-CHG OF TDAACCT TO TDB-TDAA-CAP-RT-CHG OF    \n037938         TDB-TDAACCT.\n037940     MOVE TDAA-R-TIER-RT-CH OF TDAACCT TO TDB-TDAA-R-TIER-RT-CH   \n037942         OF TDB-TDAACCT.\n037944     MOVE TDAA-ALERT-CD OF TDAACCT TO TDB-TDAA-ALERT-CD OF        \n037946         TDB-TDAACCT.\n037948     MOVE TDAA-ALERT-CD-2 OF TDAACCT TO TDB-TDAA-ALERT-CD-2 OF    \n037950         TDB-TDAACCT.\n037952     MOVE TDAA-ALERT-CD-3 OF TDAACCT TO TDB-TDAA-ALERT-CD-3 OF    \n037954         TDB-TDAACCT.\n037956     MOVE TDAA-CENSUS-TRACT OF TDAACCT TO TDB-TDAA-CENSUS-TRACT   \n037958         OF TDB-TDAACCT.\n037960     MOVE TDAA-MK-SEGMENT OF TDAACCT TO TDB-TDAA-MK-SEGMENT OF    \n037962         TDB-TDAACCT.\n037964     MOVE TDAA-BK-DEF-TOT OF TDAACCT TO TDB-TDAA-BK-DEF-TOT OF    \n037966         TDB-TDAACCT.\n037968     MOVE TDAA-BK-DEF-CD1 OF TDAACCT TO TDB-TDAA-BK-DEF-CD1 OF    \n037970         TDB-TDAACCT.\n037972     MOVE TDAA-BK-DEF-CD2 OF TDAACCT TO TDB-TDAA-BK-DEF-CD2 OF    \n037974         TDB-TDAACCT.\n037976     MOVE TDAA-BK-DEF-CD3 OF TDAACCT TO TDB-TDAA-BK-DEF-CD3 OF    \n037978         TDB-TDAACCT.\n037980     MOVE TDAA-BK-DEF-CD4 OF TDAACCT TO TDB-TDAA-BK-DEF-CD4 OF    \n037982         TDB-TDAACCT.\n037984     MOVE TDAA-BK-DEF-CD5 OF TDAACCT TO TDB-TDAA-BK-DEF-CD5 OF    \n037986         TDB-TDAACCT.\n037988     MOVE TDAA-OID-METH OF TDAACCT TO TDB-TDAA-OID-METH OF        \n037990         TDB-TDAACCT.\n037992     MOVE TDAA-EOY-CD OF TDAACCT TO TDB-TDAA-EOY-CD OF            \n037994         TDB-TDAACCT.\n037996     MOVE TDAA-B-NOTC-YR1 OF TDAACCT TO TDB-TDAA-B-NOTC-YR1 OF    \n037998         TDB-TDAACCT.\n038000     MOVE TDAA-B-NOTC-YR2 OF TDAACCT TO TDB-TDAA-B-NOTC-YR2 OF    \n038002         TDB-TDAACCT.\n038004     MOVE TDAA-B-NOTC-YR3 OF TDAACCT TO TDB-TDAA-B-NOTC-YR3 OF    \n038006         TDB-TDAACCT.\n038008     MOVE TDAA-NO-COMB-IRS OF TDAACCT TO TDB-TDAA-NO-COMB-IRS OF  \n038010         TDB-TDAACCT.\n038012     MOVE TDAA-PENLTY-CD OF TDAACCT TO TDB-TDAA-PENLTY-CD OF      \n038014         TDB-TDAACCT.\n038016     MOVE TDAA-MONEY-SRC-CD OF TDAACCT TO TDB-TDAA-MONEY-SRC-CD   \n038018         OF TDB-TDAACCT.\n038020     MOVE TDAA-INTERNET-BPY OF TDAACCT TO TDB-TDAA-INTERNET-BPY   \n038022         OF TDB-TDAACCT.\n038024     MOVE TDAA-INTERNET-TFR OF TDAACCT TO TDB-TDAA-INTERNET-TFR   \n038026         OF TDB-TDAACCT.\n038028     MOVE TDAA-INTERNET-INQ OF TDAACCT TO TDB-TDAA-INTERNET-INQ   \n038030         OF TDB-TDAACCT.\n038032     MOVE TDAA-IRA-BACKED OF TDAACCT TO TDB-TDAA-IRA-BACKED OF    \n038034         TDB-TDAACCT.\n038036     MOVE TDAA-SAV-DEPOSIT OF TDAACCT TO TDB-TDAA-SAV-DEPOSIT OF  \n038038         TDB-TDAACCT.\n038040     MOVE TDAA-MAT-TYPE OF TDAACCT TO TDB-TDAA-MAT-TYPE OF        \n038042         TDB-TDAACCT.\n038044     MOVE TDAA-MAT-TERM OF TDAACCT TO TDB-TDAA-MAT-TERM OF        \n038046         TDB-TDAACCT.\n038048     MOVE TDAA-ORG-MAT-TYPE OF TDAACCT TO TDB-TDAA-ORG-MAT-TYPE   \n038050         OF TDB-TDAACCT.\n038052     MOVE TDAA-ORG-MAT-TERM OF TDAACCT TO TDB-TDAA-ORG-MAT-TERM   \n038054         OF TDB-TDAACCT.\n038056     MOVE TDAA-ODD-PAYMENT OF TDAACCT TO TDB-TDAA-ODD-PAYMENT OF  \n038058         TDB-TDAACCT.\n038060     MOVE TDAA-PAY-FREQ OF TDAACCT TO TDB-TDAA-PAY-FREQ OF        \n038062         TDB-TDAACCT.\n038064     MOVE TDAA-PAY-NTRVL OF TDAACCT TO TDB-TDAA-PAY-NTRVL OF      \n038066         TDB-TDAACCT.\n038068     MOVE TDAA-FEE-FREQ OF TDAACCT TO TDB-TDAA-FEE-FREQ OF        \n038070         TDB-TDAACCT.\n038072     MOVE TDAA-FEE-NTRVL OF TDAACCT TO TDB-TDAA-FEE-NTRVL OF      \n038074         TDB-TDAACCT.\n038076     MOVE TDAA-STMT-FREQ OF TDAACCT TO TDB-TDAA-STMT-FREQ OF      \n038078         TDB-TDAACCT.\n038080     MOVE TDAA-STMT-NTRVL OF TDAACCT TO TDB-TDAA-STMT-NTRVL OF    \n038082         TDB-TDAACCT.\n038084     MOVE TDAA-EMPLOYEE-ID OF TDAACCT TO TDB-TDAA-EMPLOYEE-ID OF  \n038086         TDB-TDAACCT.\n038088     MOVE TDAA-EFT-CARD OF TDAACCT TO TDB-TDAA-EFT-CARD OF        \n038090         TDB-TDAACCT.\n038092     MOVE TDAA-PEN-WAV-RESN OF TDAACCT TO TDB-TDAA-PEN-WAV-RESN   \n038094         OF TDB-TDAACCT.\n038096     MOVE TDAA-CLOSED-RESN OF TDAACCT TO TDB-TDAA-CLOSED-RESN OF  \n038098         TDB-TDAACCT.\n038100     MOVE TDAA-SPECIAL-STMT OF TDAACCT TO TDB-TDAA-SPECIAL-STMT   \n038102         OF TDB-TDAACCT.\n038104     MOVE TDAA-CLS-THIS-MTH OF TDAACCT TO TDB-TDAA-CLS-THIS-MTH   \n038106         OF TDB-TDAACCT.\n038108     MOVE TDAA-RC-MAT-ONLY OF TDAACCT TO TDB-TDAA-RC-MAT-ONLY OF  \n038110         TDB-TDAACCT.\n038112     MOVE TDAA-GRACE-DAYS OF TDAACCT TO TDB-TDAA-GRACE-DAYS OF    \n038114         TDB-TDAACCT.\n038116     MOVE TDAA-CLS-ON-MAT OF TDAACCT TO TDB-TDAA-CLS-ON-MAT OF    \n038118         TDB-TDAACCT.\n038120     MOVE TDAA-DDA-ACCT-1 OF TDAACCT TO TDB-TDAA-DDA-ACCT-1 OF    \n038122         TDB-TDAACCT.\n038124     MOVE TDAA-DDA-ACCT-1-S OF TDAACCT TO TDB-TDAA-DDA-ACCT-1-S   \n038126         OF TDB-TDAACCT.\n038128     MOVE TDAA-DDA-ACCT-2 OF TDAACCT TO TDB-TDAA-DDA-ACCT-2 OF    \n038130         TDB-TDAACCT.\n038132     MOVE TDAA-DDA-ACCT-2-S OF TDAACCT TO TDB-TDAA-DDA-ACCT-2-S   \n038134         OF TDB-TDAACCT.\n038136     MOVE TDAA-DDA-ACCT-3 OF TDAACCT TO TDB-TDAA-DDA-ACCT-3 OF    \n038138         TDB-TDAACCT.\n038140     MOVE TDAA-DDA-ACCT-3-S OF TDAACCT TO TDB-TDAA-DDA-ACCT-3-S   \n038142         OF TDB-TDAACCT.\n038144     MOVE TDAA-INT-ACCT OF TDAACCT TO TDB-TDAA-INT-ACCT OF        \n038146         TDB-TDAACCT.\n038148     MOVE TDAA-INT-ACCT-S OF TDAACCT TO TDB-TDAA-INT-ACCT-S OF    \n038150         TDB-TDAACCT.\n038152     MOVE TDAA-CS-ACCT OF TDAACCT TO TDB-TDAA-CS-ACCT OF          \n038154         TDB-TDAACCT.\n038156     MOVE TDAA-CS-ACCT-S OF TDAACCT TO TDB-TDAA-CS-ACCT-S OF      \n038158         TDB-TDAACCT.\n038160     MOVE TDAA-CC-ACCT OF TDAACCT TO TDB-TDAA-CC-ACCT OF          \n038162         TDB-TDAACCT.\n038164     MOVE TDAA-LNS-BORROWER OF TDAACCT TO TDB-TDAA-LNS-BORROWER   \n038166         OF TDB-TDAACCT.\n038168     MOVE TDAA-LNS-NOTE OF TDAACCT TO TDB-TDAA-LNS-NOTE OF        \n038170         TDB-TDAACCT.\n038172     MOVE TDAA-CNV-OLD-ACCT OF TDAACCT TO TDB-TDAA-CNV-OLD-ACCT   \n038174         OF TDB-TDAACCT.\n038176     MOVE TDAA-CLS-ACCT OF TDAACCT TO TDB-TDAA-CLS-ACCT OF        \n038178         TDB-TDAACCT.\n038180     MOVE TDAA-CLS-ACCT-S OF TDAACCT TO TDB-TDAA-CLS-ACCT-S OF    \n038182         TDB-TDAACCT.\n038184     MOVE TDAA-DAYS-IN-PER OF TDAACCT TO TDB-TDAA-DAYS-IN-PER OF  \n038186         TDB-TDAACCT.\n038188     MOVE TDAA-RR-CYC-NBR OF TDAACCT TO TDB-TDAA-RR-CYC-NBR OF    \n038190         TDB-TDAACCT.\n038192     MOVE TDAA-CR-CNT-STD OF TDAACCT TO TDB-TDAA-CR-CNT-STD OF    \n038194         TDB-TDAACCT.\n038196     MOVE TDAA-CR-AMT-STD OF TDAACCT TO TDB-TDAA-CR-AMT-STD OF    \n038198         TDB-TDAACCT.\n038200     MOVE TDAA-DB-CNT-STD OF TDAACCT TO TDB-TDAA-DB-CNT-STD OF    \n038202         TDB-TDAACCT.\n038204     MOVE TDAA-DB-AMT-STD OF TDAACCT TO TDB-TDAA-DB-AMT-STD OF    \n038206         TDB-TDAACCT.\n038208     MOVE TDAA-CR-CNT-YTD OF TDAACCT TO TDB-TDAA-CR-CNT-YTD OF    \n038210         TDB-TDAACCT.\n038212     MOVE TDAA-CR-AMT-YTD OF TDAACCT TO TDB-TDAA-CR-AMT-YTD OF    \n038214         TDB-TDAACCT.\n038216     MOVE TDAA-DB-CNT-YTD OF TDAACCT TO TDB-TDAA-DB-CNT-YTD OF    \n038218         TDB-TDAACCT.\n038220     MOVE TDAA-DB-AMT-YTD OF TDAACCT TO TDB-TDAA-DB-AMT-YTD OF    \n038222         TDB-TDAACCT.\n038224     MOVE TDAA-DAYS-IN-TERM OF TDAACCT TO TDB-TDAA-DAYS-IN-TERM   \n038226         OF TDB-TDAACCT.\n038228     MOVE TDAA-BEG-INT-BAL OF TDAACCT TO TDB-TDAA-BEG-INT-BAL OF  \n038230         TDB-TDAACCT.\n038232     MOVE TDAA-PURCH-AMT OF TDAACCT TO TDB-TDAA-PURCH-AMT OF      \n038234         TDB-TDAACCT.\n038236     MOVE TDAA-CURR-BAL OF TDAACCT TO TDB-TDAA-CURR-BAL OF        \n038238         TDB-TDAACCT.\n038240     MOVE TDAA-AVAIL-BAL OF TDAACCT TO TDB-TDAA-AVAIL-BAL OF      \n038242         TDB-TDAACCT.\n038244     MOVE TDAA-BAL-BEG-MAT OF TDAACCT TO TDB-TDAA-BAL-BEG-MAT OF  \n038246         TDB-TDAACCT.\n038248     MOVE TDAA-CLOSE-AMT OF TDAACCT TO TDB-TDAA-CLOSE-AMT OF      \n038250         TDB-TDAACCT.\n038252     MOVE TDAA-MONEY-AMT OF TDAACCT TO TDB-TDAA-MONEY-AMT OF      \n038254         TDB-TDAACCT.\n038256     MOVE TDAA-BAL-BEG-STMT OF TDAACCT TO TDB-TDAA-BAL-BEG-STMT   \n038258         OF TDB-TDAACCT.\n038260     MOVE TDAA-ACCR-INT OF TDAACCT TO TDB-TDAA-ACCR-INT OF        \n038262         TDB-TDAACCT.\n038264     MOVE TDAA-ANTIC-INT OF TDAACCT TO TDB-TDAA-ANTIC-INT OF      \n038266         TDB-TDAACCT.\n038268     MOVE TDAA-INT-TO-POST OF TDAACCT TO TDB-TDAA-INT-TO-POST OF  \n038270         TDB-TDAACCT.\n038272     MOVE TDAA-1099-YTD OF TDAACCT TO TDB-TDAA-1099-YTD OF        \n038274         TDB-TDAACCT.\n038276     MOVE TDAA-1099-LST-YR OF TDAACCT TO TDB-TDAA-1099-LST-YR OF  \n038278         TDB-TDAACCT.\n038280     MOVE TDAA-CURR-PENLTY OF TDAACCT TO TDB-TDAA-CURR-PENLTY OF  \n038282         TDB-TDAACCT.\n038284     MOVE TDAA-PENLTY-STD OF TDAACCT TO TDB-TDAA-PENLTY-STD OF    \n038286         TDB-TDAACCT.\n038288     MOVE TDAA-PENLTY-YTD OF TDAACCT TO TDB-TDAA-PENLTY-YTD OF    \n038290         TDB-TDAACCT.\n038292     MOVE TDAA-LST-PENLTY OF TDAACCT TO TDB-TDAA-LST-PENLTY OF    \n038294         TDB-TDAACCT.\n038296     MOVE TDAA-CURR-INT-ADJ OF TDAACCT TO TDB-TDAA-CURR-INT-ADJ   \n038298         OF TDB-TDAACCT.\n038300     MOVE TDAA-TOTAMT-HOLDS OF TDAACCT TO TDB-TDAA-TOTAMT-HOLDS   \n038302         OF TDB-TDAACCT.\n038304     MOVE TDAA-NXT-INT-ADJ OF TDAACCT TO TDB-TDAA-NXT-INT-ADJ OF  \n038306         TDB-TDAACCT.\n038308     MOVE TDAA-FEE-AMT OF TDAACCT TO TDB-TDAA-FEE-AMT OF          \n038310         TDB-TDAACCT.\n038312     MOVE TDAA-OID-RPT-INT OF TDAACCT TO TDB-TDAA-OID-RPT-INT OF  \n038314         TDB-TDAACCT.\n038316     MOVE TDAA-FAIR-MRKT OF TDAACCT TO TDB-TDAA-FAIR-MRKT OF      \n038318         TDB-TDAACCT.\n038320     MOVE TDAA-CUR-WHLD-AMT OF TDAACCT TO TDB-TDAA-CUR-WHLD-AMT   \n038322         OF TDB-TDAACCT.\n038324     MOVE TDAA-LST-WHLD-AMT OF TDAACCT TO TDB-TDAA-LST-WHLD-AMT   \n038326         OF TDB-TDAACCT.\n038328     MOVE TDAA-WTHLD-STD OF TDAACCT TO TDB-TDAA-WTHLD-STD OF      \n038330         TDB-TDAACCT.\n038332     MOVE TDAA-WTHLD-YTD OF TDAACCT TO TDB-TDAA-WTHLD-YTD OF      \n038334         TDB-TDAACCT.\n038336     MOVE TDAA-LST-INT-PMT OF TDAACCT TO TDB-TDAA-LST-INT-PMT OF  \n038338         TDB-TDAACCT.\n038340     MOVE TDAA-BAL-BEG-YR OF TDAACCT TO TDB-TDAA-BAL-BEG-YR OF    \n038342         TDB-TDAACCT.\n038344     MOVE TDAA-BAL-AT-CONV OF TDAACCT TO TDB-TDAA-BAL-AT-CONV OF  \n038346         TDB-TDAACCT.\n038348     MOVE TDAA-BAL-BEG-LYR OF TDAACCT TO TDB-TDAA-BAL-BEG-LYR OF  \n038350         TDB-TDAACCT.\n038352     MOVE TDAA-MIN-BAL-STD OF TDAACCT TO TDB-TDAA-MIN-BAL-STD OF  \n038354         TDB-TDAACCT.\n038356     MOVE TDAA-MIN-BAL-YTD OF TDAACCT TO TDB-TDAA-MIN-BAL-YTD OF  \n038358         TDB-TDAACCT.\n038360     MOVE TDAA-MAX-BAL-YTD OF TDAACCT TO TDB-TDAA-MAX-BAL-YTD OF  \n038362         TDB-TDAACCT.\n038364     MOVE TDAA-LMINBAL-STD OF TDAACCT TO TDB-TDAA-LMINBAL-STD OF  \n038366         TDB-TDAACCT.\n038368     MOVE TDAA-CMPD-INT OF TDAACCT TO TDB-TDAA-CMPD-INT OF        \n038370         TDB-TDAACCT.\n038372     MOVE TDAA-PER-DIEM OF TDAACCT TO TDB-TDAA-PER-DIEM OF        \n038374         TDB-TDAACCT.\n038376     MOVE TDAA-AVG-PER-DIEM OF TDAACCT TO TDB-TDAA-AVG-PER-DIEM   \n038378         OF TDB-TDAACCT.\n038380     MOVE TDAA-EMAIL-MAXAMT OF TDAACCT TO TDB-TDAA-EMAIL-MAXAMT   \n038382         OF TDB-TDAACCT.\n038384     MOVE TDAA-EMAIL-MINAMT OF TDAACCT TO TDB-TDAA-EMAIL-MINAMT   \n038386         OF TDB-TDAACCT.\n038388     MOVE TDAA-DTH-FAIRMKT OF TDAACCT TO TDB-TDAA-DTH-FAIRMKT OF  \n038390         TDB-TDAACCT.\n038392     MOVE TDAA-PENLTY-WAIVE OF TDAACCT TO TDB-TDAA-PENLTY-WAIVE   \n038394         OF TDB-TDAACCT.\n038396     MOVE TDAA-BEG-INT-RT OF TDAACCT TO TDB-TDAA-BEG-INT-RT OF    \n038398         TDB-TDAACCT.\n038400     MOVE TDAA-CUR-INT-RT OF TDAACCT TO TDB-TDAA-CUR-INT-RT OF    \n038402         TDB-TDAACCT.\n038404     MOVE TDAA-FLOOR-RT OF TDAACCT TO TDB-TDAA-FLOOR-RT OF        \n038406         TDB-TDAACCT.\n038408     MOVE TDAA-FLOOR-INCR OF TDAACCT TO TDB-TDAA-FLOOR-INCR OF    \n038410         TDB-TDAACCT.\n038412     MOVE TDAA-YIELD-RT OF TDAACCT TO TDB-TDAA-YIELD-RT OF        \n038414         TDB-TDAACCT.\n038416     MOVE 1 TO Z-II.\n038418 Z-5-21-1-LOOP.\n038420     IF Z-II > 10\n038422         GO TO Z-5-21-1-LOOP-XIT.\n038424     MOVE TDAA-RISE-RATE OF TDAACCT (Z-II) TO TDB-TDAA-RISE-RATE  \n038426         OF TDB-TDAACCT (Z-II).\n038428     ADD 1 TO Z-II.\n038430     GO TO Z-5-21-1-LOOP.\n038432 Z-5-21-1-LOOP-XIT.\n038434     MOVE TDAA-LNS-INCRMNT OF TDAACCT TO TDB-TDAA-LNS-INCRMNT OF  \n038436         TDB-TDAACCT.\n038438     MOVE TDAA-RT-VARIANCE OF TDAACCT TO TDB-TDAA-RT-VARIANCE OF  \n038440         TDB-TDAACCT.\n038442     MOVE TDAA-CONST-RT-ADJ OF TDAACCT TO TDB-TDAA-CONST-RT-ADJ   \n038444         OF TDB-TDAACCT.\n038446     MOVE TDAA-RATE-AT-EOY OF TDAACCT TO TDB-TDAA-RATE-AT-EOY OF  \n038448         TDB-TDAACCT.\n038450     MOVE TDAA-RATE-LST-STM OF TDAACCT TO TDB-TDAA-RATE-LST-STM   \n038452         OF TDB-TDAACCT.\n038454     MOVE TDAA-ORG-YIELD-RT OF TDAACCT TO TDB-TDAA-ORG-YIELD-RT   \n038456         OF TDB-TDAACCT.\n038458     MOVE TDAA-REN-YIELD-RT OF TDAACCT TO TDB-TDAA-REN-YIELD-RT   \n038460         OF TDB-TDAACCT.\n038462     MOVE TDAA-SCHED-DT OF TDAACCT TO TDB-TDAA-SCHED-DT OF        \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    401 lines from 18827 to 19227.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 39, "total_chunks": 55, "start_line": 18827, "end_line": 19227, "line_count": 401}

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
- Source code length: 25199 characters

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
CHUNK 39 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 18827 to 19227 (401 lines)
Chunk Tokens (estimated): ~8,084
Actual Input Tokens: 9,490 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 18827-19227 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 39 of 55 chunks
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
      The source code below is only CHUNK 39 of 55.


=============================================================================
CHUNK 39 SOURCE CODE (Lines 18827-19227)
=============================================================================

```cobol
037662         TDB-TDAACCT.
037664     MOVE TDAA-TEMP-EXP-DT OF TDAACCT TO TDB-TDAA-TEMP-EXP-DT OF  
037666         TDB-TDAACCT.
037668     MOVE TDAA-END-OF-INT OF TDAACCT TO TDB-TDAA-END-OF-INT OF    
037670         TDB-TDAACCT.
037672     MOVE TDAA-END-OF-MAT OF TDAACCT TO TDB-TDAA-END-OF-MAT OF    
037674         TDB-TDAACCT.
037676     MOVE TDAA-END-OF-STMT OF TDAACCT TO TDB-TDAA-END-OF-STMT OF  
037678         TDB-TDAACCT.
037680     MOVE TDAA-END-OF-CMPD OF TDAACCT TO TDB-TDAA-END-OF-CMPD OF  
037682         TDB-TDAACCT.
037684     MOVE TDAA-END-OF-FEE OF TDAACCT TO TDB-TDAA-END-OF-FEE OF    
037686         TDB-TDAACCT.
037688     MOVE TDAA-OFFICER OF TDAACCT TO TDB-TDAA-OFFICER OF          
037690         TDB-TDAACCT.
037692     MOVE TDAA-OFFICER-2 OF TDAACCT TO TDB-TDAA-OFFICER-2 OF      
037694         TDB-TDAACCT.
037696     MOVE TDAA-OFFICER-3 OF TDAACCT TO TDB-TDAA-OFFICER-3 OF      
037698         TDB-TDAACCT.
037700     MOVE TDAA-FREE-MARK OF TDAACCT TO TDB-TDAA-FREE-MARK OF      
037702         TDB-TDAACCT.
037704     MOVE TDAA-CLASS-CD OF TDAACCT TO TDB-TDAA-CLASS-CD OF        
037706         TDB-TDAACCT.
037708     MOVE TDAA-CORR-BK-CD OF TDAACCT TO TDB-TDAA-CORR-BK-CD OF    
037710         TDB-TDAACCT.
037712     MOVE TDAA-PUBLIC-FUND OF TDAACCT TO TDB-TDAA-PUBLIC-FUND OF  
037714         TDB-TDAACCT.
037716     MOVE TDAA-TRUST-CD OF TDAACCT TO TDB-TDAA-TRUST-CD OF        
037718         TDB-TDAACCT.
037720     MOVE TDAA-RT-CHG-ALLOW OF TDAACCT TO TDB-TDAA-RT-CHG-ALLOW   
037722         OF TDB-TDAACCT.
037724     MOVE TDAA-WTHDRW-ALLOW OF TDAACCT TO TDB-TDAA-WTHDRW-ALLOW   
037726         OF TDB-TDAACCT.
037728     MOVE TDAA-DPOSIT-ALLOW OF TDAACCT TO TDB-TDAA-DPOSIT-ALLOW   
037730         OF TDB-TDAACCT.
037732     MOVE TDAA-POST-MAT OF TDAACCT TO TDB-TDAA-POST-MAT OF        
037734         TDB-TDAACCT.
037736     MOVE TDAA-RT-FLOOR OF TDAACCT TO TDB-TDAA-RT-FLOOR OF        
037738         TDB-TDAACCT.
037740     MOVE TDAA-REPO-CD OF TDAACCT TO TDB-TDAA-REPO-CD OF          
037742         TDB-TDAACCT.
037744     MOVE TDAA-TOTAL-CD OF TDAACCT TO TDB-TDAA-TOTAL-CD OF        
037746         TDB-TDAACCT.
037748     MOVE TDAA-REN-TOTAL-CD OF TDAACCT TO TDB-TDAA-REN-TOTAL-CD   
037750         OF TDB-TDAACCT.
037752     MOVE TDAA-ORG-TOTAL-CD OF TDAACCT TO TDB-TDAA-ORG-TOTAL-CD   
037754         OF TDB-TDAACCT.
037756     MOVE TDAA-INQ-SECR-CD OF TDAACCT TO TDB-TDAA-INQ-SECR-CD OF  
037758         TDB-TDAACCT.
037760     MOVE TDAA-MAIL-CD OF TDAACCT TO TDB-TDAA-MAIL-CD OF          
037762         TDB-TDAACCT.
037764     MOVE TDAA-WTHD-REQD-CD OF TDAACCT TO TDB-TDAA-WTHD-REQD-CD   
037766         OF TDB-TDAACCT.
037768     MOVE TDAA-TICKLER-FLAG OF TDAACCT TO TDB-TDAA-TICKLER-FLAG   
037770         OF TDB-TDAACCT.
037772     MOVE TDAA-DISP-CD OF TDAACCT TO TDB-TDAA-DISP-CD OF          
037774         TDB-TDAACCT.
037776     MOVE TDAA-CLS-DISP-CD OF TDAACCT TO TDB-TDAA-CLS-DISP-CD OF  
037778         TDB-TDAACCT.
037780     MOVE TDAA-DIST-STATUS OF TDAACCT TO TDB-TDAA-DIST-STATUS OF  
037782         TDB-TDAACCT.
037784     MOVE TDAA-COMM-ACCT OF TDAACCT TO TDB-TDAA-COMM-ACCT OF      
037786         TDB-TDAACCT.
037788     MOVE TDAA-RENEW-CD OF TDAACCT TO TDB-TDAA-RENEW-CD OF        
037790         TDB-TDAACCT.
037792     MOVE TDAA-PLEDGE-CD OF TDAACCT TO TDB-TDAA-PLEDGE-CD OF      
037794         TDB-TDAACCT.
037796     MOVE TDAA-NEGOT-CD OF TDAACCT TO TDB-TDAA-NEGOT-CD OF        
037798         TDB-TDAACCT.
037800     MOVE TDAA-BENEF-CD OF TDAACCT TO TDB-TDAA-BENEF-CD OF        
037802         TDB-TDAACCT.
037804     MOVE TDAA-COMM-MAT-CD OF TDAACCT TO TDB-TDAA-COMM-MAT-CD OF  
037806         TDB-TDAACCT.
037808     MOVE TDAA-NBR-BENEF OF TDAACCT TO TDB-TDAA-NBR-BENEF OF      
037810         TDB-TDAACCT.
037812     MOVE TDAA-OVERRIDE OF TDAACCT TO TDB-TDAA-OVERRIDE OF        
037814         TDB-TDAACCT.
037816     MOVE TDAA-INT-CD OF TDAACCT TO TDB-TDAA-INT-CD OF            
037818         TDB-TDAACCT.
037820     MOVE TDAA-WTHLD-CD OF TDAACCT TO TDB-TDAA-WTHLD-CD OF        
037822         TDB-TDAACCT.
037824     MOVE TDAA-WTHLD-AMT OF TDAACCT TO TDB-TDAA-WTHLD-AMT OF      
037826         TDB-TDAACCT.
037828     MOVE TDAA-IGL-GRP OF TDAACCT TO TDB-TDAA-IGL-GRP OF          
037830         TDB-TDAACCT.
037832     MOVE TDAA-SUM-STMT-CD OF TDAACCT TO TDB-TDAA-SUM-STMT-CD OF  
037834         TDB-TDAACCT.
037836     MOVE TDAA-REN-NTC-CD OF TDAACCT TO TDB-TDAA-REN-NTC-CD OF    
037838         TDB-TDAACCT.
037840     MOVE TDAA-PMAT-NTC-CD OF TDAACCT TO TDB-TDAA-PMAT-NTC-CD OF  
037842         TDB-TDAACCT.
037844     MOVE TDAA-RTCHG-NTC-CD OF TDAACCT TO TDB-TDAA-RTCHG-NTC-CD   
037846         OF TDB-TDAACCT.
037848     MOVE TDAA-INT-NTC-CD OF TDAACCT TO TDB-TDAA-INT-NTC-CD OF    
037850         TDB-TDAACCT.
037852     MOVE TDAA-CHG-NTC OF TDAACCT TO TDB-TDAA-CHG-NTC OF          
037854         TDB-TDAACCT.
037856     MOVE TDAA-YIELD-NUM OF TDAACCT TO TDB-TDAA-YIELD-NUM OF      
037858         TDB-TDAACCT.
037860     MOVE TDAA-YIELD-DENOM OF TDAACCT TO TDB-TDAA-YIELD-DENOM OF  
037862         TDB-TDAACCT.
037864     MOVE TDAA-CMPD-FREQ OF TDAACCT TO TDB-TDAA-CMPD-FREQ OF      
037866         TDB-TDAACCT.
037868     MOVE TDAA-CMPD-NTRVL OF TDAACCT TO TDB-TDAA-CMPD-NTRVL OF    
037870         TDB-TDAACCT.
037872     MOVE TDAA-RT-CHG-LIMIT OF TDAACCT TO TDB-TDAA-RT-CHG-LIMIT   
037874         OF TDB-TDAACCT.
037876     MOVE TDAA-VAR-RT-IMMED OF TDAACCT TO TDB-TDAA-VAR-RT-IMMED   
037878         OF TDB-TDAACCT.
037880     MOVE TDAA-VAR-RT-INT OF TDAACCT TO TDB-TDAA-VAR-RT-INT OF    
037882         TDB-TDAACCT.
037884     MOVE TDAA-VAR-RT-SCHED OF TDAACCT TO TDB-TDAA-VAR-RT-SCHED   
037886         OF TDB-TDAACCT.
037888     MOVE TDAA-VAR-RT-CUST OF TDAACCT TO TDB-TDAA-VAR-RT-CUST OF  
037890         TDB-TDAACCT.
037892     MOVE TDAA-VAR-RT-BAL OF TDAACCT TO TDB-TDAA-VAR-RT-BAL OF    
037894         TDB-TDAACCT.
037896     MOVE TDAA-RT-INDX-CD OF TDAACCT TO TDB-TDAA-RT-INDX-CD OF    
037898         TDB-TDAACCT.
037900     MOVE TDAA-R-RT-INDX-CD OF TDAACCT TO TDB-TDAA-R-RT-INDX-CD   
037902         OF TDB-TDAACCT.
037904     MOVE TDAA-RT-MARG-CD OF TDAACCT TO TDB-TDAA-RT-MARG-CD OF    
037906         TDB-TDAACCT.
037908     MOVE TDAA-R-RT-MARG-CD OF TDAACCT TO TDB-TDAA-R-RT-MARG-CD   
037910         OF TDB-TDAACCT.
037912     MOVE TDAA-RT-TIER-CD OF TDAACCT TO TDB-TDAA-RT-TIER-CD OF    
037914         TDB-TDAACCT.
037916     MOVE TDAA-R-RT-TIER-CD OF TDAACCT TO TDB-TDAA-R-RT-TIER-CD   
037918         OF TDB-TDAACCT.
037920     MOVE TDAA-RT-SR-CD OF TDAACCT TO TDB-TDAA-RT-SR-CD OF        
037922         TDB-TDAACCT.
037924     MOVE TDAA-R-RT-SR-CD OF TDAACCT TO TDB-TDAA-R-RT-SR-CD OF    
037926         TDB-TDAACCT.
037928     MOVE TDAA-RT-REGN-CD OF TDAACCT TO TDB-TDAA-RT-REGN-CD OF    
037930         TDB-TDAACCT.
037932     MOVE TDAA-RT-CHG-NTRVL OF TDAACCT TO TDB-TDAA-RT-CHG-NTRVL   
037934         OF TDB-TDAACCT.
037936     MOVE TDAA-CAP-RT-CHG OF TDAACCT TO TDB-TDAA-CAP-RT-CHG OF    
037938         TDB-TDAACCT.
037940     MOVE TDAA-R-TIER-RT-CH OF TDAACCT TO TDB-TDAA-R-TIER-RT-CH   
037942         OF TDB-TDAACCT.
037944     MOVE TDAA-ALERT-CD OF TDAACCT TO TDB-TDAA-ALERT-CD OF        
037946         TDB-TDAACCT.
037948     MOVE TDAA-ALERT-CD-2 OF TDAACCT TO TDB-TDAA-ALERT-CD-2 OF    
037950         TDB-TDAACCT.
037952     MOVE TDAA-ALERT-CD-3 OF TDAACCT TO TDB-TDAA-ALERT-CD-3 OF    
037954         TDB-TDAACCT.
037956     MOVE TDAA-CENSUS-TRACT OF TDAACCT TO TDB-TDAA-CENSUS-TRACT   
037958         OF TDB-TDAACCT.
037960     MOVE TDAA-MK-SEGMENT OF TDAACCT TO TDB-TDAA-MK-SEGMENT OF    
037962         TDB-TDAACCT.
037964     MOVE TDAA-BK-DEF-TOT OF TDAACCT TO TDB-TDAA-BK-DEF-TOT OF    
037966         TDB-TDAACCT.
037968     MOVE TDAA-BK-DEF-CD1 OF TDAACCT TO TDB-TDAA-BK-DEF-CD1 OF    
037970         TDB-TDAACCT.
037972     MOVE TDAA-BK-DEF-CD2 OF TDAACCT TO TDB-TDAA-BK-DEF-CD2 OF    
037974         TDB-TDAACCT.
037976     MOVE TDAA-BK-DEF-CD3 OF TDAACCT TO TDB-TDAA-BK-DEF-CD3 OF    
037978         TDB-TDAACCT.
037980     MOVE TDAA-BK-DEF-CD4 OF TDAACCT TO TDB-TDAA-BK-DEF-CD4 OF    
037982         TDB-TDAACCT.
037984     MOVE TDAA-BK-DEF-CD5 OF TDAACCT TO TDB-TDAA-BK-DEF-CD5 OF    
037986         TDB-TDAACCT.
037988     MOVE TDAA-OID-METH OF TDAACCT TO TDB-TDAA-OID-METH OF        
037990         TDB-TDAACCT.
037992     MOVE TDAA-EOY-CD OF TDAACCT TO TDB-TDAA-EOY-CD OF            
037994         TDB-TDAACCT.
037996     MOVE TDAA-B-NOTC-YR1 OF TDAACCT TO TDB-TDAA-B-NOTC-YR1 OF    
037998         TDB-TDAACCT.
038000     MOVE TDAA-B-NOTC-YR2 OF TDAACCT TO TDB-TDAA-B-NOTC-YR2 OF    
038002         TDB-TDAACCT.
038004     MOVE TDAA-B-NOTC-YR3 OF TDAACCT TO TDB-TDAA-B-NOTC-YR3 OF    
038006         TDB-TDAACCT.
038008     MOVE TDAA-NO-COMB-IRS OF TDAACCT TO TDB-TDAA-NO-COMB-IRS OF  
038010         TDB-TDAACCT.
038012     MOVE TDAA-PENLTY-CD OF TDAACCT TO TDB-TDAA-PENLTY-CD OF      
038014         TDB-TDAACCT.
038016     MOVE TDAA-MONEY-SRC-CD OF TDAACCT TO TDB-TDAA-MONEY-SRC-CD   
038018         OF TDB-TDAACCT.
038020     MOVE TDAA-INTERNET-BPY OF TDAACCT TO TDB-TDAA-INTERNET-BPY   
038022         OF TDB-TDAACCT.
038024     MOVE TDAA-INTERNET-TFR OF TDAACCT TO TDB-TDAA-INTERNET-TFR   
038026         OF TDB-TDAACCT.
038028     MOVE TDAA-INTERNET-INQ OF TDAACCT TO TDB-TDAA-INTERNET-INQ   
038030         OF TDB-TDAACCT.
038032     MOVE TDAA-IRA-BACKED OF TDAACCT TO TDB-TDAA-IRA-BACKED OF    
038034         TDB-TDAACCT.
038036     MOVE TDAA-SAV-DEPOSIT OF TDAACCT TO TDB-TDAA-SAV-DEPOSIT OF  
038038         TDB-TDAACCT.
038040     MOVE TDAA-MAT-TYPE OF TDAACCT TO TDB-TDAA-MAT-TYPE OF        
038042         TDB-TDAACCT.
038044     MOVE TDAA-MAT-TERM OF TDAACCT TO TDB-TDAA-MAT-TERM OF        
038046         TDB-TDAACCT.
038048     MOVE TDAA-ORG-MAT-TYPE OF TDAACCT TO TDB-TDAA-ORG-MAT-TYPE   
038050         OF TDB-TDAACCT.
038052     MOVE TDAA-ORG-MAT-TERM OF TDAACCT TO TDB-TDAA-ORG-MAT-TERM   
038054         OF TDB-TDAACCT.
038056     MOVE TDAA-ODD-PAYMENT OF TDAACCT TO TDB-TDAA-ODD-PAYMENT OF  
038058         TDB-TDAACCT.
038060     MOVE TDAA-PAY-FREQ OF TDAACCT TO TDB-TDAA-PAY-FREQ OF        
038062         TDB-TDAACCT.
038064     MOVE TDAA-PAY-NTRVL OF TDAACCT TO TDB-TDAA-PAY-NTRVL OF      
038066         TDB-TDAACCT.
038068     MOVE TDAA-FEE-FREQ OF TDAACCT TO TDB-TDAA-FEE-FREQ OF        
038070         TDB-TDAACCT.
038072     MOVE TDAA-FEE-NTRVL OF TDAACCT TO TDB-TDAA-FEE-NTRVL OF      
038074         TDB-TDAACCT.
038076     MOVE TDAA-STMT-FREQ OF TDAACCT TO TDB-TDAA-STMT-FREQ OF      
038078         TDB-TDAACCT.
038080     MOVE TDAA-STMT-NTRVL OF TDAACCT TO TDB-TDAA-STMT-NTRVL OF    
038082         TDB-TDAACCT.
038084     MOVE TDAA-EMPLOYEE-ID OF TDAACCT TO TDB-TDAA-EMPLOYEE-ID OF  
038086         TDB-TDAACCT.
038088     MOVE TDAA-EFT-CARD OF TDAACCT TO TDB-TDAA-EFT-CARD OF        
038090         TDB-TDAACCT.
038092     MOVE TDAA-PEN-WAV-RESN OF TDAACCT TO TDB-TDAA-PEN-WAV-RESN   
038094         OF TDB-TDAACCT.
038096     MOVE TDAA-CLOSED-RESN OF TDAACCT TO TDB-TDAA-CLOSED-RESN OF  
038098         TDB-TDAACCT.
038100     MOVE TDAA-SPECIAL-STMT OF TDAACCT TO TDB-TDAA-SPECIAL-STMT   
038102         OF TDB-TDAACCT.
038104     MOVE TDAA-CLS-THIS-MTH OF TDAACCT TO TDB-TDAA-CLS-THIS-MTH   
038106         OF TDB-TDAACCT.
038108     MOVE TDAA-RC-MAT-ONLY OF TDAACCT TO TDB-TDAA-RC-MAT-ONLY OF  
038110         TDB-TDAACCT.
038112     MOVE TDAA-GRACE-DAYS OF TDAACCT TO TDB-TDAA-GRACE-DAYS OF    
038114         TDB-TDAACCT.
038116     MOVE TDAA-CLS-ON-MAT OF TDAACCT TO TDB-TDAA-CLS-ON-MAT OF    
038118         TDB-TDAACCT.
038120     MOVE TDAA-DDA-ACCT-1 OF TDAACCT TO TDB-TDAA-DDA-ACCT-1 OF    
038122         TDB-TDAACCT.
038124     MOVE TDAA-DDA-ACCT-1-S OF TDAACCT TO TDB-TDAA-DDA-ACCT-1-S   
038126         OF TDB-TDAACCT.
038128     MOVE TDAA-DDA-ACCT-2 OF TDAACCT TO TDB-TDAA-DDA-ACCT-2 OF    
038130         TDB-TDAACCT.
038132     MOVE TDAA-DDA-ACCT-2-S OF TDAACCT TO TDB-TDAA-DDA-ACCT-2-S   
038134         OF TDB-TDAACCT.
038136     MOVE TDAA-DDA-ACCT-3 OF TDAACCT TO TDB-TDAA-DDA-ACCT-3 OF    
038138         TDB-TDAACCT.
038140     MOVE TDAA-DDA-ACCT-3-S OF TDAACCT TO TDB-TDAA-DDA-ACCT-3-S   
038142         OF TDB-TDAACCT.
038144     MOVE TDAA-INT-ACCT OF TDAACCT TO TDB-TDAA-INT-ACCT OF        
038146         TDB-TDAACCT.
038148     MOVE TDAA-INT-ACCT-S OF TDAACCT TO TDB-TDAA-INT-ACCT-S OF    
038150         TDB-TDAACCT.
038152     MOVE TDAA-CS-ACCT OF TDAACCT TO TDB-TDAA-CS-ACCT OF          
038154         TDB-TDAACCT.
038156     MOVE TDAA-CS-ACCT-S OF TDAACCT TO TDB-TDAA-CS-ACCT-S OF      
038158         TDB-TDAACCT.
038160     MOVE TDAA-CC-ACCT OF TDAACCT TO TDB-TDAA-CC-ACCT OF          
038162         TDB-TDAACCT.
038164     MOVE TDAA-LNS-BORROWER OF TDAACCT TO TDB-TDAA-LNS-BORROWER   
038166         OF TDB-TDAACCT.
038168     MOVE TDAA-LNS-NOTE OF TDAACCT TO TDB-TDAA-LNS-NOTE OF        
038170         TDB-TDAACCT.
038172     MOVE TDAA-CNV-OLD-ACCT OF TDAACCT TO TDB-TDAA-CNV-OLD-ACCT   
038174         OF TDB-TDAACCT.
038176     MOVE TDAA-CLS-ACCT OF TDAACCT TO TDB-TDAA-CLS-ACCT OF        
038178         TDB-TDAACCT.
038180     MOVE TDAA-CLS-ACCT-S OF TDAACCT TO TDB-TDAA-CLS-ACCT-S OF    
038182         TDB-TDAACCT.
038184     MOVE TDAA-DAYS-IN-PER OF TDAACCT TO TDB-TDAA-DAYS-IN-PER OF  
038186         TDB-TDAACCT.
038188     MOVE TDAA-RR-CYC-NBR OF TDAACCT TO TDB-TDAA-RR-CYC-NBR OF    
038190         TDB-TDAACCT.
038192     MOVE TDAA-CR-CNT-STD OF TDAACCT TO TDB-TDAA-CR-CNT-STD OF    
038194         TDB-TDAACCT.
038196     MOVE TDAA-CR-AMT-STD OF TDAACCT TO TDB-TDAA-CR-AMT-STD OF    
038198         TDB-TDAACCT.
038200     MOVE TDAA-DB-CNT-STD OF TDAACCT TO TDB-TDAA-DB-CNT-STD OF    
038202         TDB-TDAACCT.
038204     MOVE TDAA-DB-AMT-STD OF TDAACCT TO TDB-TDAA-DB-AMT-STD OF    
038206         TDB-TDAACCT.
038208     MOVE TDAA-CR-CNT-YTD OF TDAACCT TO TDB-TDAA-CR-CNT-YTD OF    
038210         TDB-TDAACCT.
038212     MOVE TDAA-CR-AMT-YTD OF TDAACCT TO TDB-TDAA-CR-AMT-YTD OF    
038214         TDB-TDAACCT.
038216     MOVE TDAA-DB-CNT-YTD OF TDAACCT TO TDB-TDAA-DB-CNT-YTD OF    
038218         TDB-TDAACCT.
038220     MOVE TDAA-DB-AMT-YTD OF TDAACCT TO TDB-TDAA-DB-AMT-YTD OF    
038222         TDB-TDAACCT.
038224     MOVE TDAA-DAYS-IN-TERM OF TDAACCT TO TDB-TDAA-DAYS-IN-TERM   
038226         OF TDB-TDAACCT.
038228     MOVE TDAA-BEG-INT-BAL OF TDAACCT TO TDB-TDAA-BEG-INT-BAL OF  
038230         TDB-TDAACCT.
038232     MOVE TDAA-PURCH-AMT OF TDAACCT TO TDB-TDAA-PURCH-AMT OF      
038234         TDB-TDAACCT.
038236     MOVE TDAA-CURR-BAL OF TDAACCT TO TDB-TDAA-CURR-BAL OF        
038238         TDB-TDAACCT.
038240     MOVE TDAA-AVAIL-BAL OF TDAACCT TO TDB-TDAA-AVAIL-BAL OF      
038242         TDB-TDAACCT.
038244     MOVE TDAA-BAL-BEG-MAT OF TDAACCT TO TDB-TDAA-BAL-BEG-MAT OF  
038246         TDB-TDAACCT.
038248     MOVE TDAA-CLOSE-AMT OF TDAACCT TO TDB-TDAA-CLOSE-AMT OF      
038250         TDB-TDAACCT.
038252     MOVE TDAA-MONEY-AMT OF TDAACCT TO TDB-TDAA-MONEY-AMT OF      
038254         TDB-TDAACCT.
038256     MOVE TDAA-BAL-BEG-STMT OF TDAACCT TO TDB-TDAA-BAL-BEG-STMT   
038258         OF TDB-TDAACCT.
038260     MOVE TDAA-ACCR-INT OF TDAACCT TO TDB-TDAA-ACCR-INT OF        
038262         TDB-TDAACCT.
038264     MOVE TDAA-ANTIC-INT OF TDAACCT TO TDB-TDAA-ANTIC-INT OF      
038266         TDB-TDAACCT.
038268     MOVE TDAA-INT-TO-POST OF TDAACCT TO TDB-TDAA-INT-TO-POST OF  
038270         TDB-TDAACCT.
038272     MOVE TDAA-1099-YTD OF TDAACCT TO TDB-TDAA-1099-YTD OF        
038274         TDB-TDAACCT.
038276     MOVE TDAA-1099-LST-YR OF TDAACCT TO TDB-TDAA-1099-LST-YR OF  
038278         TDB-TDAACCT.
038280     MOVE TDAA-CURR-PENLTY OF TDAACCT TO TDB-TDAA-CURR-PENLTY OF  
038282         TDB-TDAACCT.
038284     MOVE TDAA-PENLTY-STD OF TDAACCT TO TDB-TDAA-PENLTY-STD OF    
038286         TDB-TDAACCT.
038288     MOVE TDAA-PENLTY-YTD OF TDAACCT TO TDB-TDAA-PENLTY-YTD OF    
038290         TDB-TDAACCT.
038292     MOVE TDAA-LST-PENLTY OF TDAACCT TO TDB-TDAA-LST-PENLTY OF    
038294         TDB-TDAACCT.
038296     MOVE TDAA-CURR-INT-ADJ OF TDAACCT TO TDB-TDAA-CURR-INT-ADJ   
038298         OF TDB-TDAACCT.
038300     MOVE TDAA-TOTAMT-HOLDS OF TDAACCT TO TDB-TDAA-TOTAMT-HOLDS   
038302         OF TDB-TDAACCT.
038304     MOVE TDAA-NXT-INT-ADJ OF TDAACCT TO TDB-TDAA-NXT-INT-ADJ OF  
038306         TDB-TDAACCT.
038308     MOVE TDAA-FEE-AMT OF TDAACCT TO TDB-TDAA-FEE-AMT OF          
038310         TDB-TDAACCT.
038312     MOVE TDAA-OID-RPT-INT OF TDAACCT TO TDB-TDAA-OID-RPT-INT OF  
038314         TDB-TDAACCT.
038316     MOVE TDAA-FAIR-MRKT OF TDAACCT TO TDB-TDAA-FAIR-MRKT OF      
038318         TDB-TDAACCT.
038320     MOVE TDAA-CUR-WHLD-AMT OF TDAACCT TO TDB-TDAA-CUR-WHLD-AMT   
038322         OF TDB-TDAACCT.
038324     MOVE TDAA-LST-WHLD-AMT OF TDAACCT TO TDB-TDAA-LST-WHLD-AMT   
038326         OF TDB-TDAACCT.
038328     MOVE TDAA-WTHLD-STD OF TDAACCT TO TDB-TDAA-WTHLD-STD OF      
038330         TDB-TDAACCT.
038332     MOVE TDAA-WTHLD-YTD OF TDAACCT TO TDB-TDAA-WTHLD-YTD OF      
038334         TDB-TDAACCT.
038336     MOVE TDAA-LST-INT-PMT OF TDAACCT TO TDB-TDAA-LST-INT-PMT OF  
038338         TDB-TDAACCT.
038340     MOVE TDAA-BAL-BEG-YR OF TDAACCT TO TDB-TDAA-BAL-BEG-YR OF    
038342         TDB-TDAACCT.
038344     MOVE TDAA-BAL-AT-CONV OF TDAACCT TO TDB-TDAA-BAL-AT-CONV OF  
038346         TDB-TDAACCT.
038348     MOVE TDAA-BAL-BEG-LYR OF TDAACCT TO TDB-TDAA-BAL-BEG-LYR OF  
038350         TDB-TDAACCT.
038352     MOVE TDAA-MIN-BAL-STD OF TDAACCT TO TDB-TDAA-MIN-BAL-STD OF  
038354         TDB-TDAACCT.
038356     MOVE TDAA-MIN-BAL-YTD OF TDAACCT TO TDB-TDAA-MIN-BAL-YTD OF  
038358         TDB-TDAACCT.
038360     MOVE TDAA-MAX-BAL-YTD OF TDAACCT TO TDB-TDAA-MAX-BAL-YTD OF  
038362         TDB-TDAACCT.
038364     MOVE TDAA-LMINBAL-STD OF TDAACCT TO TDB-TDAA-LMINBAL-STD OF  
038366         TDB-TDAACCT.
038368     MOVE TDAA-CMPD-INT OF TDAACCT TO TDB-TDAA-CMPD-INT OF        
038370         TDB-TDAACCT.
038372     MOVE TDAA-PER-DIEM OF TDAACCT TO TDB-TDAA-PER-DIEM OF        
038374         TDB-TDAACCT.
038376     MOVE TDAA-AVG-PER-DIEM OF TDAACCT TO TDB-TDAA-AVG-PER-DIEM   
038378         OF TDB-TDAACCT.
038380     MOVE TDAA-EMAIL-MAXAMT OF TDAACCT TO TDB-TDAA-EMAIL-MAXAMT   
038382         OF TDB-TDAACCT.
038384     MOVE TDAA-EMAIL-MINAMT OF TDAACCT TO TDB-TDAA-EMAIL-MINAMT   
038386         OF TDB-TDAACCT.
038388     MOVE TDAA-DTH-FAIRMKT OF TDAACCT TO TDB-TDAA-DTH-FAIRMKT OF  
038390         TDB-TDAACCT.
038392     MOVE TDAA-PENLTY-WAIVE OF TDAACCT TO TDB-TDAA-PENLTY-WAIVE   
038394         OF TDB-TDAACCT.
038396     MOVE TDAA-BEG-INT-RT OF TDAACCT TO TDB-TDAA-BEG-INT-RT OF    
038398         TDB-TDAACCT.
038400     MOVE TDAA-CUR-INT-RT OF TDAACCT TO TDB-TDAA-CUR-INT-RT OF    
038402         TDB-TDAACCT.
038404     MOVE TDAA-FLOOR-RT OF TDAACCT TO TDB-TDAA-FLOOR-RT OF        
038406         TDB-TDAACCT.
038408     MOVE TDAA-FLOOR-INCR OF TDAACCT TO TDB-TDAA-FLOOR-INCR OF    
038410         TDB-TDAACCT.
038412     MOVE TDAA-YIELD-RT OF TDAACCT TO TDB-TDAA-YIELD-RT OF        
038414         TDB-TDAACCT.
038416     MOVE 1 TO Z-II.
038418 Z-5-21-1-LOOP.
038420     IF Z-II > 10
038422         GO TO Z-5-21-1-LOOP-XIT.
038424     MOVE TDAA-RISE-RATE OF TDAACCT (Z-II) TO TDB-TDAA-RISE-RATE  
038426         OF TDB-TDAACCT (Z-II).
038428     ADD 1 TO Z-II.
038430     GO TO Z-5-21-1-LOOP.
038432 Z-5-21-1-LOOP-XIT.
038434     MOVE TDAA-LNS-INCRMNT OF TDAACCT TO TDB-TDAA-LNS-INCRMNT OF  
038436         TDB-TDAACCT.
038438     MOVE TDAA-RT-VARIANCE OF TDAACCT TO TDB-TDAA-RT-VARIANCE OF  
038440         TDB-TDAACCT.
038442     MOVE TDAA-CONST-RT-ADJ OF TDAACCT TO TDB-TDAA-CONST-RT-ADJ   
038444         OF TDB-TDAACCT.
038446     MOVE TDAA-RATE-AT-EOY OF TDAACCT TO TDB-TDAA-RATE-AT-EOY OF  
038448         TDB-TDAACCT.
038450     MOVE TDAA-RATE-LST-STM OF TDAACCT TO TDB-TDAA-RATE-LST-STM   
038452         OF TDB-TDAACCT.
038454     MOVE TDAA-ORG-YIELD-RT OF TDAACCT TO TDB-TDAA-ORG-YIELD-RT   
038456         OF TDB-TDAACCT.
038458     MOVE TDAA-REN-YIELD-RT OF TDAACCT TO TDB-TDAA-REN-YIELD-RT   
038460         OF TDB-TDAACCT.
038462     MOVE TDAA-SCHED-DT OF TDAACCT TO TDB-TDAA-SCHED-DT OF        
```

⚠️  This is the source code you must document.
    401 lines from 18827 to 19227.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

