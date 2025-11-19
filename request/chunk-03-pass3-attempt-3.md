# LLM Request Debug File
Generated: 2025-11-17T19:56:15.780865

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 3/55
- **Model**: gpt-4.1
- **Chunk Number**: 3
- **Pass Number**: 3
- **Attempt Number**: 3 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~7,306 tokens
- **Total Input**: ~9,264 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 3/55" (ID: detailed-code-explanation)

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


**CHUNK 3 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-17T19:50:50.832678", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 3 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 945 to 1332 (388 lines)\nChunk Tokens (estimated): ~6,708\nActual Input Tokens: 8,114 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 945-1332 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 3 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 3 of 55.\n\n\n=============================================================================\nCHUNK 3 SOURCE CODE (Lines 945-1332)\n=============================================================================\n\n```cobol\n001898 01  Z-SAVE-AREA.\n001900     05  Z-RESTART-FLAG                         PIC 9 VALUE 0.\n001902     05  Z-RESTART-POINT                        PIC 9(6).\n001904     05  Z-RESTART-PROCESS                      PIC 9(6).\n001906     05  Z-DMS-SAVE-ENTRY.\n001908         10  Z-DMS1-RS-OPEN                     PIC 9.\n001910         10  Z-DMS2-RS-OPEN                     PIC 9.\n001912*******  BK-SPEC-FILE\n001914     05  Z-FLINFO3-RS-OPEN                      PIC 9.\n001916*******  PROC-FILE\n001918     05  Z-FLINFO4-RS-OPEN                      PIC 9.\n001920*******  DST-FILE-MAINT\n001922     05  Z-FLINFO5-RS-OPEN                      PIC 9.\n001924*******  CST-FILE-MAINT\n001926     05  Z-FLINFO6-RS-OPEN                      PIC 9.\n001928     05  Z-RPTINFO1-RS-OPEN                     PIC 9.\n001930     05  Z-RPTINFO2-RS-OPEN                     PIC 9.\n001932     05  Z-CUSTOM-SAVE-RESTART                  PIC X.\n001934*\n001936****** TEMPORARY AREA ******\n001938 01  Z-TEMPORARY-AREA.\n001940     05  Z-RUNNING-FLAG                         PIC 9 VALUE 0.\n001942     05  Z-PROCESS-NAME                         PIC X(30)\n001944                                                VALUE SPACES.\n001946     05  Z-RESTART-BY-COUNT                     PIC S9(8).\n001948     05  Z-RESTART-FOR-COUNT                    PIC S9(8).\n001950     05  Z-DMS-TEMP-ENTRY.\n001952         10  Z-DMS1-TRANS-STATE                 PIC 9.\n001954         10  Z-DMS1-OPEN                        PIC 9.\n001956         10  Z-DMS1-ET-TYPE                     PIC 9.\n001958         10  Z-DMS1-BT-TYPE                     PIC 9.\n001960         10  Z-DMS1-ABORT-FLAG                  PIC 9.\n001962         10  Z-DMS1-UPDATES                     PIC 9(8).\n001964         10  Z-DMS1-FOUND-LOCK                  PIC 9.\n001966         10  Z-DMS2-TRANS-STATE                 PIC 9.\n001968         10  Z-DMS2-OPEN                        PIC 9.\n001970         10  Z-DMS2-ET-TYPE                     PIC 9.\n001972         10  Z-DMS2-BT-TYPE                     PIC 9.\n001974         10  Z-DMS2-ABORT-FLAG                  PIC 9.\n001976         10  Z-DMS2-UPDATES                     PIC 9(8).\n001978         10  Z-DMS2-FOUND-LOCK                  PIC 9.\n001980         10  Z-DMS2-FOUND-DEADLOCK              PIC 9.\n001982*******  BK-SPEC-FILE ***  NO-RESTART\n001984     05  Z-FLINFO3-SAVE-ENTRY.\n001986         10  Z-FLINFO3-RS-PATH                  PIC 999.\n001988         10  Z-FLINFO3-RS-KEY                   PIC 9(8).\n001990*******  PROC-FILE ***  NO-RESTART\n001992     05  Z-FLINFO4-SAVE-ENTRY.\n001994         10  Z-FLINFO4-RS-PATH                  PIC 999.\n001996         10  Z-FLINFO4-RS-KEY                   PIC 9(8).\n001998*******  DST-FILE-MAINT ***  NO-RESTART\n002000     05  Z-FLINFO5-SAVE-ENTRY.\n002002         10  Z-FLINFO5-RS-PATH                  PIC 999.\n002004         10  Z-FLINFO5-RS-KEY                   PIC 9(8).\n002006*******  CST-FILE-MAINT ***  NO-RESTART\n002008     05  Z-FLINFO6-SAVE-ENTRY.\n002010         10  Z-FLINFO6-RS-PATH                  PIC 999.\n002012         10  Z-FLINFO6-RS-KEY                   PIC 9(8).\n002014*******  TDARESTART\n002016     05  Z-FLINFO1-TEMP-ENTRY.\n002018         10  Z-FLINFO1-FLAGS.\n002020             15  Z-FLINFO1-PRES                 PIC 9.\n002022                 88  Z-FLINFO1-ABSENT            VALUE 0.\n002024                 88  Z-FLINFO1-PRESENT           VALUE 1.\n002026             15  Z-FLINFO1-SOME                 PIC 9.\n002028             15  Z-FLINFO1-RESIDENT-FLAG        PIC 9.\n002030                 88  Z-FLINFO1-RESIDENT          VALUE 1.\n002032         10  Z-FLINFO1-FLAGS-2 REDEFINES\n002034             Z-FLINFO1-FLAGS.\n002036             15  Z-FLINFO1-NONE-DONE            PIC 99.\n002038                 88  Z-FLINFO1-NONE              VALUE 0.\n002040                 88  Z-FLINFO1-DONE              VALUE 1.\n002042             15  FILLER                         PIC X.\n002044         10  Z-FLINFO1-LAST-SEQ                 PIC 9(6).\n002046         10  Z-FLINFO1-SELECT                   PIC 9(8).\n002048*******  BK-SPEC-FILE\n002050     05  Z-FLINFO3-TEMP-ENTRY.\n002052         10  Z-FLINFO3-FLAGS.\n002054             15  Z-FLINFO3-PRES                 PIC 9.\n002056                 88  Z-FLINFO3-ABSENT            VALUE 0.\n002058                 88  Z-FLINFO3-PRESENT           VALUE 1.\n002060             15  Z-FLINFO3-SOME                 PIC 9.\n002062             15  Z-FLINFO3-RESIDENT-FLAG        PIC 9.\n002064                 88  Z-FLINFO3-RESIDENT          VALUE 1.\n002066         10  Z-FLINFO3-FLAGS-2 REDEFINES\n002068             Z-FLINFO3-FLAGS.\n002070             15  Z-FLINFO3-NONE-DONE            PIC 99.\n002072                 88  Z-FLINFO3-NONE              VALUE 0.\n002074                 88  Z-FLINFO3-DONE              VALUE 1.\n002076             15  FILLER                         PIC X.\n002078         10  Z-FLINFO3-LAST-SEQ                 PIC 9(6).\n002080         10  Z-FLINFO3-SELECT                   PIC 9(8).\n002082         10  Z-FLINFO3-OPEN                     PIC 9.\n002084             88  Z-FLINFO3-ISCLOSED              VALUE 0.\n002086             88  Z-FLINFO3-ISOPEN                VALUES 1 THRU 9.\n002088         10  Z-FLINFO3-STATUS                   PIC X(2).\n002090         10  Z-FILE3-KEY                        PIC 9(8) COMP.\n002092*******  PROC-FILE\n002094     05  Z-FLINFO4-TEMP-ENTRY.\n002096         10  Z-FLINFO4-FLAGS.\n002098             15  Z-FLINFO4-PRES                 PIC 9.\n002100                 88  Z-FLINFO4-ABSENT            VALUE 0.\n002102                 88  Z-FLINFO4-PRESENT           VALUE 1.\n002104             15  Z-FLINFO4-SOME                 PIC 9.\n002106             15  Z-FLINFO4-RESIDENT-FLAG        PIC 9.\n002108                 88  Z-FLINFO4-RESIDENT          VALUE 1.\n002110         10  Z-FLINFO4-FLAGS-2 REDEFINES\n002112             Z-FLINFO4-FLAGS.\n002114             15  Z-FLINFO4-NONE-DONE            PIC 99.\n002116                 88  Z-FLINFO4-NONE              VALUE 0.\n002118                 88  Z-FLINFO4-DONE              VALUE 1.\n002120             15  FILLER                         PIC X.\n002122         10  Z-FLINFO4-LAST-SEQ                 PIC 9(6).\n002124         10  Z-FLINFO4-SELECT                   PIC 9(8).\n002126         10  Z-FLINFO4-OPEN                     PIC 9.\n002128             88  Z-FLINFO4-ISCLOSED              VALUE 0.\n002130             88  Z-FLINFO4-ISOPEN                VALUES 1 THRU 9.\n002132         10  Z-FLINFO4-STATUS                   PIC X(2).\n002134         10  Z-FILE4-KEY                        PIC 9(8) COMP.\n002136*******  DST-FILE-MAINT\n002138     05  Z-FLINFO5-TEMP-ENTRY.\n002140         10  Z-FLINFO5-FLAGS.\n002142             15  Z-FLINFO5-PRES                 PIC 9.\n002144                 88  Z-FLINFO5-ABSENT            VALUE 0.\n002146                 88  Z-FLINFO5-PRESENT           VALUE 1.\n002148             15  Z-FLINFO5-SOME                 PIC 9.\n002150             15  Z-FLINFO5-RESIDENT-FLAG        PIC 9.\n002152                 88  Z-FLINFO5-RESIDENT          VALUE 1.\n002154         10  Z-FLINFO5-FLAGS-2 REDEFINES\n002156             Z-FLINFO5-FLAGS.\n002158             15  Z-FLINFO5-NONE-DONE            PIC 99.\n002160                 88  Z-FLINFO5-NONE              VALUE 0.\n002162                 88  Z-FLINFO5-DONE              VALUE 1.\n002164             15  FILLER                         PIC X.\n002166         10  Z-FLINFO5-LAST-SEQ                 PIC 9(6).\n002168         10  Z-FLINFO5-SELECT                   PIC 9(8).\n002170         10  Z-FLINFO5-OPEN                     PIC 9.\n002172             88  Z-FLINFO5-ISCLOSED              VALUE 0.\n002174             88  Z-FLINFO5-ISOPEN                VALUES 1 THRU 9.\n002176         10  Z-FLINFO5-STATUS                   PIC X(2).\n002178         10  Z-FILE5-KEY                        PIC 9(8) COMP.\n002180*******  CST-FILE-MAINT\n002182     05  Z-FLINFO6-TEMP-ENTRY.\n002184         10  Z-FLINFO6-FLAGS.\n002186             15  Z-FLINFO6-PRES                 PIC 9.\n002188                 88  Z-FLINFO6-ABSENT            VALUE 0.\n002190                 88  Z-FLINFO6-PRESENT           VALUE 1.\n002192             15  Z-FLINFO6-SOME                 PIC 9.\n002194             15  Z-FLINFO6-RESIDENT-FLAG        PIC 9.\n002196                 88  Z-FLINFO6-RESIDENT          VALUE 1.\n002198         10  Z-FLINFO6-FLAGS-2 REDEFINES\n002200             Z-FLINFO6-FLAGS.\n002202             15  Z-FLINFO6-NONE-DONE            PIC 99.\n002204                 88  Z-FLINFO6-NONE              VALUE 0.\n002206                 88  Z-FLINFO6-DONE              VALUE 1.\n002208             15  FILLER                         PIC X.\n002210         10  Z-FLINFO6-LAST-SEQ                 PIC 9(6).\n002212         10  Z-FLINFO6-SELECT                   PIC 9(8).\n002214         10  Z-FLINFO6-OPEN                     PIC 9.\n002216             88  Z-FLINFO6-ISCLOSED              VALUE 0.\n002218             88  Z-FLINFO6-ISOPEN                VALUES 1 THRU 9.\n002220         10  Z-FLINFO6-STATUS                   PIC X(2).\n002222         10  Z-FILE6-KEY                        PIC 9(8) COMP.\n002224*******  SPCPRT\n002226     05  Z-FLINFO7-TEMP-ENTRY.\n002228         10  Z-FLINFO7-FLAGS.\n002230             15  Z-FLINFO7-PRES                 PIC 9.\n002232                 88  Z-FLINFO7-ABSENT            VALUE 0.\n002234                 88  Z-FLINFO7-PRESENT           VALUE 1.\n002236             15  Z-FLINFO7-SOME                 PIC 9.\n002238             15  Z-FLINFO7-RESIDENT-FLAG        PIC 9.\n002240                 88  Z-FLINFO7-RESIDENT          VALUE 1.\n002242         10  Z-FLINFO7-FLAGS-2 REDEFINES\n002244             Z-FLINFO7-FLAGS.\n002246             15  Z-FLINFO7-NONE-DONE            PIC 99.\n002248                 88  Z-FLINFO7-NONE              VALUE 0.\n002250                 88  Z-FLINFO7-DONE              VALUE 1.\n002252             15  FILLER                         PIC X.\n002254         10  Z-FLINFO7-LAST-SEQ                 PIC 9(6).\n002256         10  Z-FLINFO7-SELECT                   PIC 9(8).\n002258*******  TDAACCT\n002260     05  Z-FLINFO8-TEMP-ENTRY.\n002262         10  Z-FLINFO8-FLAGS.\n002264             15  Z-FLINFO8-PRES                 PIC 9.\n002266                 88  Z-FLINFO8-ABSENT            VALUE 0.\n002268                 88  Z-FLINFO8-PRESENT           VALUE 1.\n002270             15  Z-FLINFO8-SOME                 PIC 9.\n002272             15  Z-FLINFO8-RESIDENT-FLAG        PIC 9.\n002274                 88  Z-FLINFO8-RESIDENT          VALUE 1.\n002276         10  Z-FLINFO8-FLAGS-2 REDEFINES\n002278             Z-FLINFO8-FLAGS.\n002280             15  Z-FLINFO8-NONE-DONE            PIC 99.\n002282                 88  Z-FLINFO8-NONE              VALUE 0.\n002284                 88  Z-FLINFO8-DONE              VALUE 1.\n002286             15  FILLER                         PIC X.\n002288         10  Z-FLINFO8-LAST-SEQ                 PIC 9(6).\n002290         10  Z-FLINFO8-SELECT                   PIC 9(8).\n002292*******  TDAREPORTS\n002294     05  Z-FLINFO9-TEMP-ENTRY.\n002296         10  Z-FLINFO9-FLAGS.\n002298             15  Z-FLINFO9-PRES                 PIC 9.\n002300                 88  Z-FLINFO9-ABSENT            VALUE 0.\n002302                 88  Z-FLINFO9-PRESENT           VALUE 1.\n002304             15  Z-FLINFO9-SOME                 PIC 9.\n002306             15  Z-FLINFO9-RESIDENT-FLAG        PIC 9.\n002308                 88  Z-FLINFO9-RESIDENT          VALUE 1.\n002310         10  Z-FLINFO9-FLAGS-2 REDEFINES\n002312             Z-FLINFO9-FLAGS.\n002314             15  Z-FLINFO9-NONE-DONE            PIC 99.\n002316                 88  Z-FLINFO9-NONE              VALUE 0.\n002318                 88  Z-FLINFO9-DONE              VALUE 1.\n002320             15  FILLER                         PIC X.\n002322         10  Z-FLINFO9-LAST-SEQ                 PIC 9(6).\n002324         10  Z-FLINFO9-SELECT                   PIC 9(8).\n002326*******  TDAPCR\n002328     05  Z-FLINFO10-TEMP-ENTRY.\n002330         10  Z-FLINFO10-FLAGS.\n002332             15  Z-FLINFO10-PRES                PIC 9.\n002334                 88  Z-FLINFO10-ABSENT           VALUE 0.\n002336                 88  Z-FLINFO10-PRESENT          VALUE 1.\n002338             15  Z-FLINFO10-SOME                PIC 9.\n002340             15  Z-FLINFO10-RESIDENT-FLAG       PIC 9.\n002342                 88  Z-FLINFO10-RESIDENT         VALUE 1.\n002344         10  Z-FLINFO10-FLAGS-2 REDEFINES\n002346             Z-FLINFO10-FLAGS.\n002348             15  Z-FLINFO10-NONE-DONE           PIC 99.\n002350                 88  Z-FLINFO10-NONE             VALUE 0.\n002352                 88  Z-FLINFO10-DONE             VALUE 1.\n002354             15  FILLER                         PIC X.\n002356         10  Z-FLINFO10-LAST-SEQ                PIC 9(6).\n002358         10  Z-FLINFO10-SELECT                  PIC 9(8).\n002360*******  TDACUST\n002362     05  Z-FLINFO11-TEMP-ENTRY.\n002364         10  Z-FLINFO11-FLAGS.\n002366             15  Z-FLINFO11-PRES                PIC 9.\n002368                 88  Z-FLINFO11-ABSENT           VALUE 0.\n002370                 88  Z-FLINFO11-PRESENT          VALUE 1.\n002372             15  Z-FLINFO11-SOME                PIC 9.\n002374             15  Z-FLINFO11-RESIDENT-FLAG       PIC 9.\n002376                 88  Z-FLINFO11-RESIDENT         VALUE 1.\n002378         10  Z-FLINFO11-FLAGS-2 REDEFINES\n002380             Z-FLINFO11-FLAGS.\n002382             15  Z-FLINFO11-NONE-DONE           PIC 99.\n002384                 88  Z-FLINFO11-NONE             VALUE 0.\n002386                 88  Z-FLINFO11-DONE             VALUE 1.\n002388             15  FILLER                         PIC X.\n002390         10  Z-FLINFO11-LAST-SEQ                PIC 9(6).\n002392         10  Z-FLINFO11-SELECT                  PIC 9(8).\n002394*******  TDAIRA\n002396     05  Z-FLINFO12-TEMP-ENTRY.\n002398         10  Z-FLINFO12-FLAGS.\n002400             15  Z-FLINFO12-PRES                PIC 9.\n002402                 88  Z-FLINFO12-ABSENT           VALUE 0.\n002404                 88  Z-FLINFO12-PRESENT          VALUE 1.\n002406             15  Z-FLINFO12-SOME                PIC 9.\n002408             15  Z-FLINFO12-RESIDENT-FLAG       PIC 9.\n002410                 88  Z-FLINFO12-RESIDENT         VALUE 1.\n002412         10  Z-FLINFO12-FLAGS-2 REDEFINES\n002414             Z-FLINFO12-FLAGS.\n002416             15  Z-FLINFO12-NONE-DONE           PIC 99.\n002418                 88  Z-FLINFO12-NONE             VALUE 0.\n002420                 88  Z-FLINFO12-DONE             VALUE 1.\n002422             15  FILLER                         PIC X.\n002424         10  Z-FLINFO12-LAST-SEQ                PIC 9(6).\n002426         10  Z-FLINFO12-SELECT                  PIC 9(8).\n002428*******  TDADISTR\n002430     05  Z-FLINFO13-TEMP-ENTRY.\n002432         10  Z-FLINFO13-FLAGS.\n002434             15  Z-FLINFO13-PRES                PIC 9.\n002436                 88  Z-FLINFO13-ABSENT           VALUE 0.\n002438                 88  Z-FLINFO13-PRESENT          VALUE 1.\n002440             15  Z-FLINFO13-SOME                PIC 9.\n002442             15  Z-FLINFO13-RESIDENT-FLAG       PIC 9.\n002444                 88  Z-FLINFO13-RESIDENT         VALUE 1.\n002446         10  Z-FLINFO13-FLAGS-2 REDEFINES\n002448             Z-FLINFO13-FLAGS.\n002450             15  Z-FLINFO13-NONE-DONE           PIC 99.\n002452                 88  Z-FLINFO13-NONE             VALUE 0.\n002454                 88  Z-FLINFO13-DONE             VALUE 1.\n002456             15  FILLER                         PIC X.\n002458         10  Z-FLINFO13-LAST-SEQ                PIC 9(6).\n002460         10  Z-FLINFO13-SELECT                  PIC 9(8).\n002462*******  TDAACTV\n002464     05  Z-FLINFO14-TEMP-ENTRY.\n002466         10  Z-FLINFO14-FLAGS.\n002468             15  Z-FLINFO14-PRES                PIC 9.\n002470                 88  Z-FLINFO14-ABSENT           VALUE 0.\n002472                 88  Z-FLINFO14-PRESENT          VALUE 1.\n002474             15  Z-FLINFO14-SOME                PIC 9.\n002476             15  Z-FLINFO14-RESIDENT-FLAG       PIC 9.\n002478                 88  Z-FLINFO14-RESIDENT         VALUE 1.\n002480         10  Z-FLINFO14-FLAGS-2 REDEFINES\n002482             Z-FLINFO14-FLAGS.\n002484             15  Z-FLINFO14-NONE-DONE           PIC 99.\n002486                 88  Z-FLINFO14-NONE             VALUE 0.\n002488                 88  Z-FLINFO14-DONE             VALUE 1.\n002490             15  FILLER                         PIC X.\n002492         10  Z-FLINFO14-LAST-SEQ                PIC 9(6).\n002494         10  Z-FLINFO14-SELECT                  PIC 9(8).\n002496*\n002498**** UPDATES\n002500*\n002502     05  Z-FLINFO-UPDATES.\n002504         10  Z-FLINFO1-UPDATE                   PIC 9(8).\n002506         10  Z-FLINFO3-UPDATE                   PIC 9(8).\n002508         10  Z-FLINFO4-UPDATE                   PIC 9(8).\n002510         10  Z-FLINFO5-UPDATE                   PIC 9(8).\n002512         10  Z-FLINFO6-UPDATE                   PIC 9(8).\n002514         10  Z-FLINFO7-UPDATE                   PIC 9(8).\n002516         10  Z-FLINFO8-UPDATE                   PIC 9(8).\n002518         10  Z-FLINFO9-UPDATE                   PIC 9(8).\n002520         10  Z-FLINFO10-UPDATE                  PIC 9(8).\n002522         10  Z-FLINFO11-UPDATE                  PIC 9(8).\n002524         10  Z-FLINFO12-UPDATE                  PIC 9(8).\n002526         10  Z-FLINFO13-UPDATE                  PIC 9(8).\n002528         10  Z-FLINFO14-UPDATE                  PIC 9(8).\n002530*\n002532**** MODIFIES\n002534*\n002536     05  Z-FLINFO-MODIFIES.\n002538         10  Z-FLINFO1-MODIFY                   PIC 9 VALUE 0.\n002540         10  Z-FLINFO3-MODIFY                   PIC 9 VALUE 0.\n002542         10  Z-FLINFO4-MODIFY                   PIC 9 VALUE 0.\n002544         10  Z-FLINFO5-MODIFY                   PIC 9 VALUE 0.\n002546         10  Z-FLINFO6-MODIFY                   PIC 9 VALUE 0.\n002548         10  Z-FLINFO7-MODIFY                   PIC 9 VALUE 0.\n002550         10  Z-FLINFO8-MODIFY                   PIC 9 VALUE 0.\n002552         10  Z-FLINFO9-MODIFY                   PIC 9 VALUE 0.\n002554         10  Z-FLINFO10-MODIFY                  PIC 9 VALUE 0.\n002556         10  Z-FLINFO11-MODIFY                  PIC 9 VALUE 0.\n002558         10  Z-FLINFO12-MODIFY                  PIC 9 VALUE 0.\n002560         10  Z-FLINFO13-MODIFY                  PIC 9 VALUE 0.\n002562         10  Z-FLINFO14-MODIFY                  PIC 9 VALUE 0.\n002564******  REPORT LISTING\n002566     05  Z-RPT-1-SAVE-ENTRY.\n002568         10  Z-RPT-1-PAGE                       PIC S9(6).\n002570         10  Z-RPT-1-LINE                       PIC S9(6).\n002572         10  Z-RPT-1-TRAP                       PIC S9(6).\n002574******  REPORT FICHE\n002576     05  Z-RPT-2-SAVE-ENTRY.\n002578         10  Z-RPT-2-PAGE                       PIC S9(6).\n002580         10  Z-RPT-2-LINE                       PIC S9(6).\n002582         10  Z-RPT-2-TRAP                       PIC S9(6).\n002584     05  Z-WRITE-PARAMS.\n002586         10  Z-LINES                            PIC S9(11) BINARY.\n002588         10  Z-LINES-HOLD                       PIC S9(11) BINARY.\n002590******  REPORT LISTING\n002592     05  Z-RPTINFO1-STATUS                      PIC X(2).\n002594     05  Z-RPTINFO1-KEY                         PIC 9(8) COMP.\n002596     05  Z-RPTINFO1-TEMP-ENTRY.\n002598         10  Z-RPTINFO1-OPEN                    PIC 9.\n002600             88  Z-RPTINFO1-ISCLOSED             VALUE 0.\n002602             88  Z-RPTINFO1-ISOPEN               VALUES 1 THRU 9.\n002604         10  Z-RPTINFO1-INBLOCK                 PIC 9.\n002606******  REPORT FICHE\n002608     05  Z-RPTINFO2-STATUS                      PIC X(2).\n002610     05  Z-RPTINFO2-KEY                         PIC 9(8) COMP.\n002612     05  Z-RPTINFO2-TEMP-ENTRY.\n002614         10  Z-RPTINFO2-OPEN                    PIC 9.\n002616             88  Z-RPTINFO2-ISCLOSED             VALUE 0.\n002618             88  Z-RPTINFO2-ISOPEN               VALUES 1 THRU 9.\n002620         10  Z-RPTINFO2-INBLOCK                 PIC 9.\n002622*\n002624**** DISPLAY COMPRESS\n002626*\n002628     05  Z-DISP-COMPACT-BUFFER.\n002630         10  Z-DISP-CHAR  OCCURS  80            PIC X.\n002632     05  Z-DISP-COMPACT-1  REDEFINES  Z-DISP-COMPACT-BUFFER.\n002634         10  Z-DISP-COMPACT-1-79                PIC X(79).\n002636         10  FILLER                             PIC X(1).\n002638     05  Z-CUSTOM-TEMPORARY                     PIC X.\n002640*\n002642**** DISPLAY STATEMENT WORK AREAS\n002644 01  Z-DISPLAY-WORK-AREA.\n002646     05  Z-DISP-FORMAT-1-GRP.\n002648         07  Z-DISP-FORMAT-1.\n002650             10  Z-DISP-FIELD-1-1               PIC X(33).\n002652             10  Z-DISP-FIELD-1-2               PIC Z(3)9.\n002654     05  Z-DISP-FORMAT-2-GRP REDEFINES Z-DISP-FORMAT-1-GRP.\n002656         07  Z-DISP-FORMAT-2.\n002658             10  Z-DISP-FIELD-2-1               PIC X(31).\n002660             10  Z-DISP-FIELD-2-2               PIC Z(3)9.\n002662         07  FILLER                             PIC X(2).\n002664*\n002666****** CALL FOR CURRENT DATE ******\n002668 01  Z-CALL-CURRENTDATE   PIC X(21) DISPLAY WITH LOWER-BOUNDS.\n002670*\n002672****** VALUED AREA ******\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    388 lines from 945 to 1332.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 3, "total_chunks": 55, "start_line": 945, "end_line": 1332, "line_count": 388}

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
- Source code length: 26155 characters

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
CHUNK 3 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 945 to 1332 (388 lines)
Chunk Tokens (estimated): ~6,708
Actual Input Tokens: 8,114 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 945-1332 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 3 of 55 chunks
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
      The source code below is only CHUNK 3 of 55.


=============================================================================
CHUNK 3 SOURCE CODE (Lines 945-1332)
=============================================================================

```cobol
001898 01  Z-SAVE-AREA.
001900     05  Z-RESTART-FLAG                         PIC 9 VALUE 0.
001902     05  Z-RESTART-POINT                        PIC 9(6).
001904     05  Z-RESTART-PROCESS                      PIC 9(6).
001906     05  Z-DMS-SAVE-ENTRY.
001908         10  Z-DMS1-RS-OPEN                     PIC 9.
001910         10  Z-DMS2-RS-OPEN                     PIC 9.
001912*******  BK-SPEC-FILE
001914     05  Z-FLINFO3-RS-OPEN                      PIC 9.
001916*******  PROC-FILE
001918     05  Z-FLINFO4-RS-OPEN                      PIC 9.
001920*******  DST-FILE-MAINT
001922     05  Z-FLINFO5-RS-OPEN                      PIC 9.
001924*******  CST-FILE-MAINT
001926     05  Z-FLINFO6-RS-OPEN                      PIC 9.
001928     05  Z-RPTINFO1-RS-OPEN                     PIC 9.
001930     05  Z-RPTINFO2-RS-OPEN                     PIC 9.
001932     05  Z-CUSTOM-SAVE-RESTART                  PIC X.
001934*
001936****** TEMPORARY AREA ******
001938 01  Z-TEMPORARY-AREA.
001940     05  Z-RUNNING-FLAG                         PIC 9 VALUE 0.
001942     05  Z-PROCESS-NAME                         PIC X(30)
001944                                                VALUE SPACES.
001946     05  Z-RESTART-BY-COUNT                     PIC S9(8).
001948     05  Z-RESTART-FOR-COUNT                    PIC S9(8).
001950     05  Z-DMS-TEMP-ENTRY.
001952         10  Z-DMS1-TRANS-STATE                 PIC 9.
001954         10  Z-DMS1-OPEN                        PIC 9.
001956         10  Z-DMS1-ET-TYPE                     PIC 9.
001958         10  Z-DMS1-BT-TYPE                     PIC 9.
001960         10  Z-DMS1-ABORT-FLAG                  PIC 9.
001962         10  Z-DMS1-UPDATES                     PIC 9(8).
001964         10  Z-DMS1-FOUND-LOCK                  PIC 9.
001966         10  Z-DMS2-TRANS-STATE                 PIC 9.
001968         10  Z-DMS2-OPEN                        PIC 9.
001970         10  Z-DMS2-ET-TYPE                     PIC 9.
001972         10  Z-DMS2-BT-TYPE                     PIC 9.
001974         10  Z-DMS2-ABORT-FLAG                  PIC 9.
001976         10  Z-DMS2-UPDATES                     PIC 9(8).
001978         10  Z-DMS2-FOUND-LOCK                  PIC 9.
001980         10  Z-DMS2-FOUND-DEADLOCK              PIC 9.
001982*******  BK-SPEC-FILE ***  NO-RESTART
001984     05  Z-FLINFO3-SAVE-ENTRY.
001986         10  Z-FLINFO3-RS-PATH                  PIC 999.
001988         10  Z-FLINFO3-RS-KEY                   PIC 9(8).
001990*******  PROC-FILE ***  NO-RESTART
001992     05  Z-FLINFO4-SAVE-ENTRY.
001994         10  Z-FLINFO4-RS-PATH                  PIC 999.
001996         10  Z-FLINFO4-RS-KEY                   PIC 9(8).
001998*******  DST-FILE-MAINT ***  NO-RESTART
002000     05  Z-FLINFO5-SAVE-ENTRY.
002002         10  Z-FLINFO5-RS-PATH                  PIC 999.
002004         10  Z-FLINFO5-RS-KEY                   PIC 9(8).
002006*******  CST-FILE-MAINT ***  NO-RESTART
002008     05  Z-FLINFO6-SAVE-ENTRY.
002010         10  Z-FLINFO6-RS-PATH                  PIC 999.
002012         10  Z-FLINFO6-RS-KEY                   PIC 9(8).
002014*******  TDARESTART
002016     05  Z-FLINFO1-TEMP-ENTRY.
002018         10  Z-FLINFO1-FLAGS.
002020             15  Z-FLINFO1-PRES                 PIC 9.
002022                 88  Z-FLINFO1-ABSENT            VALUE 0.
002024                 88  Z-FLINFO1-PRESENT           VALUE 1.
002026             15  Z-FLINFO1-SOME                 PIC 9.
002028             15  Z-FLINFO1-RESIDENT-FLAG        PIC 9.
002030                 88  Z-FLINFO1-RESIDENT          VALUE 1.
002032         10  Z-FLINFO1-FLAGS-2 REDEFINES
002034             Z-FLINFO1-FLAGS.
002036             15  Z-FLINFO1-NONE-DONE            PIC 99.
002038                 88  Z-FLINFO1-NONE              VALUE 0.
002040                 88  Z-FLINFO1-DONE              VALUE 1.
002042             15  FILLER                         PIC X.
002044         10  Z-FLINFO1-LAST-SEQ                 PIC 9(6).
002046         10  Z-FLINFO1-SELECT                   PIC 9(8).
002048*******  BK-SPEC-FILE
002050     05  Z-FLINFO3-TEMP-ENTRY.
002052         10  Z-FLINFO3-FLAGS.
002054             15  Z-FLINFO3-PRES                 PIC 9.
002056                 88  Z-FLINFO3-ABSENT            VALUE 0.
002058                 88  Z-FLINFO3-PRESENT           VALUE 1.
002060             15  Z-FLINFO3-SOME                 PIC 9.
002062             15  Z-FLINFO3-RESIDENT-FLAG        PIC 9.
002064                 88  Z-FLINFO3-RESIDENT          VALUE 1.
002066         10  Z-FLINFO3-FLAGS-2 REDEFINES
002068             Z-FLINFO3-FLAGS.
002070             15  Z-FLINFO3-NONE-DONE            PIC 99.
002072                 88  Z-FLINFO3-NONE              VALUE 0.
002074                 88  Z-FLINFO3-DONE              VALUE 1.
002076             15  FILLER                         PIC X.
002078         10  Z-FLINFO3-LAST-SEQ                 PIC 9(6).
002080         10  Z-FLINFO3-SELECT                   PIC 9(8).
002082         10  Z-FLINFO3-OPEN                     PIC 9.
002084             88  Z-FLINFO3-ISCLOSED              VALUE 0.
002086             88  Z-FLINFO3-ISOPEN                VALUES 1 THRU 9.
002088         10  Z-FLINFO3-STATUS                   PIC X(2).
002090         10  Z-FILE3-KEY                        PIC 9(8) COMP.
002092*******  PROC-FILE
002094     05  Z-FLINFO4-TEMP-ENTRY.
002096         10  Z-FLINFO4-FLAGS.
002098             15  Z-FLINFO4-PRES                 PIC 9.
002100                 88  Z-FLINFO4-ABSENT            VALUE 0.
002102                 88  Z-FLINFO4-PRESENT           VALUE 1.
002104             15  Z-FLINFO4-SOME                 PIC 9.
002106             15  Z-FLINFO4-RESIDENT-FLAG        PIC 9.
002108                 88  Z-FLINFO4-RESIDENT          VALUE 1.
002110         10  Z-FLINFO4-FLAGS-2 REDEFINES
002112             Z-FLINFO4-FLAGS.
002114             15  Z-FLINFO4-NONE-DONE            PIC 99.
002116                 88  Z-FLINFO4-NONE              VALUE 0.
002118                 88  Z-FLINFO4-DONE              VALUE 1.
002120             15  FILLER                         PIC X.
002122         10  Z-FLINFO4-LAST-SEQ                 PIC 9(6).
002124         10  Z-FLINFO4-SELECT                   PIC 9(8).
002126         10  Z-FLINFO4-OPEN                     PIC 9.
002128             88  Z-FLINFO4-ISCLOSED              VALUE 0.
002130             88  Z-FLINFO4-ISOPEN                VALUES 1 THRU 9.
002132         10  Z-FLINFO4-STATUS                   PIC X(2).
002134         10  Z-FILE4-KEY                        PIC 9(8) COMP.
002136*******  DST-FILE-MAINT
002138     05  Z-FLINFO5-TEMP-ENTRY.
002140         10  Z-FLINFO5-FLAGS.
002142             15  Z-FLINFO5-PRES                 PIC 9.
002144                 88  Z-FLINFO5-ABSENT            VALUE 0.
002146                 88  Z-FLINFO5-PRESENT           VALUE 1.
002148             15  Z-FLINFO5-SOME                 PIC 9.
002150             15  Z-FLINFO5-RESIDENT-FLAG        PIC 9.
002152                 88  Z-FLINFO5-RESIDENT          VALUE 1.
002154         10  Z-FLINFO5-FLAGS-2 REDEFINES
002156             Z-FLINFO5-FLAGS.
002158             15  Z-FLINFO5-NONE-DONE            PIC 99.
002160                 88  Z-FLINFO5-NONE              VALUE 0.
002162                 88  Z-FLINFO5-DONE              VALUE 1.
002164             15  FILLER                         PIC X.
002166         10  Z-FLINFO5-LAST-SEQ                 PIC 9(6).
002168         10  Z-FLINFO5-SELECT                   PIC 9(8).
002170         10  Z-FLINFO5-OPEN                     PIC 9.
002172             88  Z-FLINFO5-ISCLOSED              VALUE 0.
002174             88  Z-FLINFO5-ISOPEN                VALUES 1 THRU 9.
002176         10  Z-FLINFO5-STATUS                   PIC X(2).
002178         10  Z-FILE5-KEY                        PIC 9(8) COMP.
002180*******  CST-FILE-MAINT
002182     05  Z-FLINFO6-TEMP-ENTRY.
002184         10  Z-FLINFO6-FLAGS.
002186             15  Z-FLINFO6-PRES                 PIC 9.
002188                 88  Z-FLINFO6-ABSENT            VALUE 0.
002190                 88  Z-FLINFO6-PRESENT           VALUE 1.
002192             15  Z-FLINFO6-SOME                 PIC 9.
002194             15  Z-FLINFO6-RESIDENT-FLAG        PIC 9.
002196                 88  Z-FLINFO6-RESIDENT          VALUE 1.
002198         10  Z-FLINFO6-FLAGS-2 REDEFINES
002200             Z-FLINFO6-FLAGS.
002202             15  Z-FLINFO6-NONE-DONE            PIC 99.
002204                 88  Z-FLINFO6-NONE              VALUE 0.
002206                 88  Z-FLINFO6-DONE              VALUE 1.
002208             15  FILLER                         PIC X.
002210         10  Z-FLINFO6-LAST-SEQ                 PIC 9(6).
002212         10  Z-FLINFO6-SELECT                   PIC 9(8).
002214         10  Z-FLINFO6-OPEN                     PIC 9.
002216             88  Z-FLINFO6-ISCLOSED              VALUE 0.
002218             88  Z-FLINFO6-ISOPEN                VALUES 1 THRU 9.
002220         10  Z-FLINFO6-STATUS                   PIC X(2).
002222         10  Z-FILE6-KEY                        PIC 9(8) COMP.
002224*******  SPCPRT
002226     05  Z-FLINFO7-TEMP-ENTRY.
002228         10  Z-FLINFO7-FLAGS.
002230             15  Z-FLINFO7-PRES                 PIC 9.
002232                 88  Z-FLINFO7-ABSENT            VALUE 0.
002234                 88  Z-FLINFO7-PRESENT           VALUE 1.
002236             15  Z-FLINFO7-SOME                 PIC 9.
002238             15  Z-FLINFO7-RESIDENT-FLAG        PIC 9.
002240                 88  Z-FLINFO7-RESIDENT          VALUE 1.
002242         10  Z-FLINFO7-FLAGS-2 REDEFINES
002244             Z-FLINFO7-FLAGS.
002246             15  Z-FLINFO7-NONE-DONE            PIC 99.
002248                 88  Z-FLINFO7-NONE              VALUE 0.
002250                 88  Z-FLINFO7-DONE              VALUE 1.
002252             15  FILLER                         PIC X.
002254         10  Z-FLINFO7-LAST-SEQ                 PIC 9(6).
002256         10  Z-FLINFO7-SELECT                   PIC 9(8).
002258*******  TDAACCT
002260     05  Z-FLINFO8-TEMP-ENTRY.
002262         10  Z-FLINFO8-FLAGS.
002264             15  Z-FLINFO8-PRES                 PIC 9.
002266                 88  Z-FLINFO8-ABSENT            VALUE 0.
002268                 88  Z-FLINFO8-PRESENT           VALUE 1.
002270             15  Z-FLINFO8-SOME                 PIC 9.
002272             15  Z-FLINFO8-RESIDENT-FLAG        PIC 9.
002274                 88  Z-FLINFO8-RESIDENT          VALUE 1.
002276         10  Z-FLINFO8-FLAGS-2 REDEFINES
002278             Z-FLINFO8-FLAGS.
002280             15  Z-FLINFO8-NONE-DONE            PIC 99.
002282                 88  Z-FLINFO8-NONE              VALUE 0.
002284                 88  Z-FLINFO8-DONE              VALUE 1.
002286             15  FILLER                         PIC X.
002288         10  Z-FLINFO8-LAST-SEQ                 PIC 9(6).
002290         10  Z-FLINFO8-SELECT                   PIC 9(8).
002292*******  TDAREPORTS
002294     05  Z-FLINFO9-TEMP-ENTRY.
002296         10  Z-FLINFO9-FLAGS.
002298             15  Z-FLINFO9-PRES                 PIC 9.
002300                 88  Z-FLINFO9-ABSENT            VALUE 0.
002302                 88  Z-FLINFO9-PRESENT           VALUE 1.
002304             15  Z-FLINFO9-SOME                 PIC 9.
002306             15  Z-FLINFO9-RESIDENT-FLAG        PIC 9.
002308                 88  Z-FLINFO9-RESIDENT          VALUE 1.
002310         10  Z-FLINFO9-FLAGS-2 REDEFINES
002312             Z-FLINFO9-FLAGS.
002314             15  Z-FLINFO9-NONE-DONE            PIC 99.
002316                 88  Z-FLINFO9-NONE              VALUE 0.
002318                 88  Z-FLINFO9-DONE              VALUE 1.
002320             15  FILLER                         PIC X.
002322         10  Z-FLINFO9-LAST-SEQ                 PIC 9(6).
002324         10  Z-FLINFO9-SELECT                   PIC 9(8).
002326*******  TDAPCR
002328     05  Z-FLINFO10-TEMP-ENTRY.
002330         10  Z-FLINFO10-FLAGS.
002332             15  Z-FLINFO10-PRES                PIC 9.
002334                 88  Z-FLINFO10-ABSENT           VALUE 0.
002336                 88  Z-FLINFO10-PRESENT          VALUE 1.
002338             15  Z-FLINFO10-SOME                PIC 9.
002340             15  Z-FLINFO10-RESIDENT-FLAG       PIC 9.
002342                 88  Z-FLINFO10-RESIDENT         VALUE 1.
002344         10  Z-FLINFO10-FLAGS-2 REDEFINES
002346             Z-FLINFO10-FLAGS.
002348             15  Z-FLINFO10-NONE-DONE           PIC 99.
002350                 88  Z-FLINFO10-NONE             VALUE 0.
002352                 88  Z-FLINFO10-DONE             VALUE 1.
002354             15  FILLER                         PIC X.
002356         10  Z-FLINFO10-LAST-SEQ                PIC 9(6).
002358         10  Z-FLINFO10-SELECT                  PIC 9(8).
002360*******  TDACUST
002362     05  Z-FLINFO11-TEMP-ENTRY.
002364         10  Z-FLINFO11-FLAGS.
002366             15  Z-FLINFO11-PRES                PIC 9.
002368                 88  Z-FLINFO11-ABSENT           VALUE 0.
002370                 88  Z-FLINFO11-PRESENT          VALUE 1.
002372             15  Z-FLINFO11-SOME                PIC 9.
002374             15  Z-FLINFO11-RESIDENT-FLAG       PIC 9.
002376                 88  Z-FLINFO11-RESIDENT         VALUE 1.
002378         10  Z-FLINFO11-FLAGS-2 REDEFINES
002380             Z-FLINFO11-FLAGS.
002382             15  Z-FLINFO11-NONE-DONE           PIC 99.
002384                 88  Z-FLINFO11-NONE             VALUE 0.
002386                 88  Z-FLINFO11-DONE             VALUE 1.
002388             15  FILLER                         PIC X.
002390         10  Z-FLINFO11-LAST-SEQ                PIC 9(6).
002392         10  Z-FLINFO11-SELECT                  PIC 9(8).
002394*******  TDAIRA
002396     05  Z-FLINFO12-TEMP-ENTRY.
002398         10  Z-FLINFO12-FLAGS.
002400             15  Z-FLINFO12-PRES                PIC 9.
002402                 88  Z-FLINFO12-ABSENT           VALUE 0.
002404                 88  Z-FLINFO12-PRESENT          VALUE 1.
002406             15  Z-FLINFO12-SOME                PIC 9.
002408             15  Z-FLINFO12-RESIDENT-FLAG       PIC 9.
002410                 88  Z-FLINFO12-RESIDENT         VALUE 1.
002412         10  Z-FLINFO12-FLAGS-2 REDEFINES
002414             Z-FLINFO12-FLAGS.
002416             15  Z-FLINFO12-NONE-DONE           PIC 99.
002418                 88  Z-FLINFO12-NONE             VALUE 0.
002420                 88  Z-FLINFO12-DONE             VALUE 1.
002422             15  FILLER                         PIC X.
002424         10  Z-FLINFO12-LAST-SEQ                PIC 9(6).
002426         10  Z-FLINFO12-SELECT                  PIC 9(8).
002428*******  TDADISTR
002430     05  Z-FLINFO13-TEMP-ENTRY.
002432         10  Z-FLINFO13-FLAGS.
002434             15  Z-FLINFO13-PRES                PIC 9.
002436                 88  Z-FLINFO13-ABSENT           VALUE 0.
002438                 88  Z-FLINFO13-PRESENT          VALUE 1.
002440             15  Z-FLINFO13-SOME                PIC 9.
002442             15  Z-FLINFO13-RESIDENT-FLAG       PIC 9.
002444                 88  Z-FLINFO13-RESIDENT         VALUE 1.
002446         10  Z-FLINFO13-FLAGS-2 REDEFINES
002448             Z-FLINFO13-FLAGS.
002450             15  Z-FLINFO13-NONE-DONE           PIC 99.
002452                 88  Z-FLINFO13-NONE             VALUE 0.
002454                 88  Z-FLINFO13-DONE             VALUE 1.
002456             15  FILLER                         PIC X.
002458         10  Z-FLINFO13-LAST-SEQ                PIC 9(6).
002460         10  Z-FLINFO13-SELECT                  PIC 9(8).
002462*******  TDAACTV
002464     05  Z-FLINFO14-TEMP-ENTRY.
002466         10  Z-FLINFO14-FLAGS.
002468             15  Z-FLINFO14-PRES                PIC 9.
002470                 88  Z-FLINFO14-ABSENT           VALUE 0.
002472                 88  Z-FLINFO14-PRESENT          VALUE 1.
002474             15  Z-FLINFO14-SOME                PIC 9.
002476             15  Z-FLINFO14-RESIDENT-FLAG       PIC 9.
002478                 88  Z-FLINFO14-RESIDENT         VALUE 1.
002480         10  Z-FLINFO14-FLAGS-2 REDEFINES
002482             Z-FLINFO14-FLAGS.
002484             15  Z-FLINFO14-NONE-DONE           PIC 99.
002486                 88  Z-FLINFO14-NONE             VALUE 0.
002488                 88  Z-FLINFO14-DONE             VALUE 1.
002490             15  FILLER                         PIC X.
002492         10  Z-FLINFO14-LAST-SEQ                PIC 9(6).
002494         10  Z-FLINFO14-SELECT                  PIC 9(8).
002496*
002498**** UPDATES
002500*
002502     05  Z-FLINFO-UPDATES.
002504         10  Z-FLINFO1-UPDATE                   PIC 9(8).
002506         10  Z-FLINFO3-UPDATE                   PIC 9(8).
002508         10  Z-FLINFO4-UPDATE                   PIC 9(8).
002510         10  Z-FLINFO5-UPDATE                   PIC 9(8).
002512         10  Z-FLINFO6-UPDATE                   PIC 9(8).
002514         10  Z-FLINFO7-UPDATE                   PIC 9(8).
002516         10  Z-FLINFO8-UPDATE                   PIC 9(8).
002518         10  Z-FLINFO9-UPDATE                   PIC 9(8).
002520         10  Z-FLINFO10-UPDATE                  PIC 9(8).
002522         10  Z-FLINFO11-UPDATE                  PIC 9(8).
002524         10  Z-FLINFO12-UPDATE                  PIC 9(8).
002526         10  Z-FLINFO13-UPDATE                  PIC 9(8).
002528         10  Z-FLINFO14-UPDATE                  PIC 9(8).
002530*
002532**** MODIFIES
002534*
002536     05  Z-FLINFO-MODIFIES.
002538         10  Z-FLINFO1-MODIFY                   PIC 9 VALUE 0.
002540         10  Z-FLINFO3-MODIFY                   PIC 9 VALUE 0.
002542         10  Z-FLINFO4-MODIFY                   PIC 9 VALUE 0.
002544         10  Z-FLINFO5-MODIFY                   PIC 9 VALUE 0.
002546         10  Z-FLINFO6-MODIFY                   PIC 9 VALUE 0.
002548         10  Z-FLINFO7-MODIFY                   PIC 9 VALUE 0.
002550         10  Z-FLINFO8-MODIFY                   PIC 9 VALUE 0.
002552         10  Z-FLINFO9-MODIFY                   PIC 9 VALUE 0.
002554         10  Z-FLINFO10-MODIFY                  PIC 9 VALUE 0.
002556         10  Z-FLINFO11-MODIFY                  PIC 9 VALUE 0.
002558         10  Z-FLINFO12-MODIFY                  PIC 9 VALUE 0.
002560         10  Z-FLINFO13-MODIFY                  PIC 9 VALUE 0.
002562         10  Z-FLINFO14-MODIFY                  PIC 9 VALUE 0.
002564******  REPORT LISTING
002566     05  Z-RPT-1-SAVE-ENTRY.
002568         10  Z-RPT-1-PAGE                       PIC S9(6).
002570         10  Z-RPT-1-LINE                       PIC S9(6).
002572         10  Z-RPT-1-TRAP                       PIC S9(6).
002574******  REPORT FICHE
002576     05  Z-RPT-2-SAVE-ENTRY.
002578         10  Z-RPT-2-PAGE                       PIC S9(6).
002580         10  Z-RPT-2-LINE                       PIC S9(6).
002582         10  Z-RPT-2-TRAP                       PIC S9(6).
002584     05  Z-WRITE-PARAMS.
002586         10  Z-LINES                            PIC S9(11) BINARY.
002588         10  Z-LINES-HOLD                       PIC S9(11) BINARY.
002590******  REPORT LISTING
002592     05  Z-RPTINFO1-STATUS                      PIC X(2).
002594     05  Z-RPTINFO1-KEY                         PIC 9(8) COMP.
002596     05  Z-RPTINFO1-TEMP-ENTRY.
002598         10  Z-RPTINFO1-OPEN                    PIC 9.
002600             88  Z-RPTINFO1-ISCLOSED             VALUE 0.
002602             88  Z-RPTINFO1-ISOPEN               VALUES 1 THRU 9.
002604         10  Z-RPTINFO1-INBLOCK                 PIC 9.
002606******  REPORT FICHE
002608     05  Z-RPTINFO2-STATUS                      PIC X(2).
002610     05  Z-RPTINFO2-KEY                         PIC 9(8) COMP.
002612     05  Z-RPTINFO2-TEMP-ENTRY.
002614         10  Z-RPTINFO2-OPEN                    PIC 9.
002616             88  Z-RPTINFO2-ISCLOSED             VALUE 0.
002618             88  Z-RPTINFO2-ISOPEN               VALUES 1 THRU 9.
002620         10  Z-RPTINFO2-INBLOCK                 PIC 9.
002622*
002624**** DISPLAY COMPRESS
002626*
002628     05  Z-DISP-COMPACT-BUFFER.
002630         10  Z-DISP-CHAR  OCCURS  80            PIC X.
002632     05  Z-DISP-COMPACT-1  REDEFINES  Z-DISP-COMPACT-BUFFER.
002634         10  Z-DISP-COMPACT-1-79                PIC X(79).
002636         10  FILLER                             PIC X(1).
002638     05  Z-CUSTOM-TEMPORARY                     PIC X.
002640*
002642**** DISPLAY STATEMENT WORK AREAS
002644 01  Z-DISPLAY-WORK-AREA.
002646     05  Z-DISP-FORMAT-1-GRP.
002648         07  Z-DISP-FORMAT-1.
002650             10  Z-DISP-FIELD-1-1               PIC X(33).
002652             10  Z-DISP-FIELD-1-2               PIC Z(3)9.
002654     05  Z-DISP-FORMAT-2-GRP REDEFINES Z-DISP-FORMAT-1-GRP.
002656         07  Z-DISP-FORMAT-2.
002658             10  Z-DISP-FIELD-2-1               PIC X(31).
002660             10  Z-DISP-FIELD-2-2               PIC Z(3)9.
002662         07  FILLER                             PIC X(2).
002664*
002666****** CALL FOR CURRENT DATE ******
002668 01  Z-CALL-CURRENTDATE   PIC X(21) DISPLAY WITH LOWER-BOUNDS.
002670*
002672****** VALUED AREA ******
```

⚠️  This is the source code you must document.
    388 lines from 945 to 1332.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

