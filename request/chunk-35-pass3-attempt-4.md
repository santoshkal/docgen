# LLM Request Debug File
Generated: 2025-11-18T19:47:57.407420

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 35/55
- **Model**: gpt-4.1
- **Chunk Number**: 35
- **Pass Number**: 3
- **Attempt Number**: 4 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,086 tokens
- **User Prompt**: ~7,105 tokens
- **Total Input**: ~9,191 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 35/55" (ID: detailed-code-explanation)

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
⚠️  CRITICAL MASTER INSTRUCTIONS — READ CAREFULLY
═══════════════════════════════════════════════════════════════════════════

You will receive *raw COBOL-74 source code* from lines {{start_line}} to 
{{end_line}} exactly as it appears in the input.

You have **TWO CRITICAL JOBS**.  
BOTH jobs are mandatory. BOTH must succeed for output to be valid.

⭐ CRITICAL JOB #1 — VERBATIM CODE REPRODUCTION  
   You MUST output the ENTIRE original COBOL source code, exactly as 
   provided, inside ```cobol``` fenced code blocks.  
   This includes every character, every sequence number, every space, 
   every comment, every filler, every table entry, every period, and 
   every division.

⭐ CRITICAL JOB #2 — BLOCK-BY-BLOCK CODE EXPLANATION  
   You MUST provide a complete, accurate, and detailed explanation for 
   each logical block (paragraph, section, data group, etc.), and you 
   MUST include a second verbatim code snippet for each block.

If token limits prevent complete execution of both jobs, apply **Task 
Priority Rules** below.

═══════════════════════════════════════════════════════════════════════════
🚨 TASK PRIORITY IN CASE OF TOKEN LIMIT PRESSURE
═══════════════════════════════════════════════════════════════════════════

1. CRITICAL JOB #1 — Verbatim reproduction of ALL COBOL lines  
   (This must ALWAYS be completed. If you cannot complete this, you must 
   truncate **explanations**, NOT code.)

2. CRITICAL JOB #2 — Block-by-block verbatim code + explanation  
   (If token pressure exists, explanations may be shortened, but code 
   reproduction remains mandatory.)

⚠️ Under NO circumstances may you:
   - Modify the input code,
   - Omit code,
   - Summarize code,
   - Skip blocks,
   - Produce only explanations without code.

═══════════════════════════════════════════════════════════════════════════
📐 GLOBAL OUTPUT STRUCTURE (MUST FOLLOW THIS EXACT ORDER)
═══════════════════════════════════════════════════════════════════════════

--------------------------------------------------------------------------
## COBOL Code (Complete Verbatim Copy)

```cobol
[EVERY LINE EXACTLY AS RECEIVED IN INPUT — VERBATIM, NO CHANGES]
```

--------------------------------------------------------------------------
## Explanation by Block

For EACH logical block in the program:

### Block N: [BLOCK-NAME] (Lines X–Y)

```cobol
[EXACT LINES X–Y FROM THE ORIGINAL INPUT — VERBATIM]
```

**Purpose:**
- High-level summary of what the block accomplishes.

**Detailed Explanation:**
- What each line does  
- Functional role  
- Execution flow  
- Conditional logic and branches  
- Variables and data elements used  
- Data transformations  
- File interactions  
- External calls  
- Error handling (if any)

**Technical Details:**
- Variables used  
- Called by  
- Calls  
- Side effects  

--------------------------------------------------------------------------
## Coverage Self-Assessment

Use the EXACT template below:

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
- Source chunk contained: {{line_count}} total lines (lines {{start_line}}–{{end_line}})
- I included: [NUMBER] executable lines in my code blocks
- I excluded: [NUMBER] comment/page-break lines
- Expected executable: {{line_count}} – [excluded count]
- My self-assessed coverage: [NUMBER]%

⚠️ This section must appear LAST. No text may follow it.
---

═══════════════════════════════════════════════════════════════════════════
📌 ABSOLUTE REQUIREMENTS FOR CODE REPRODUCTION (CRITICAL JOB #1)
═══════════════════════════════════════════════════════════════════════════

✔ MUST copy every character exactly as input  
✔ MUST preserve spacing, indentation, alignment, sequence numbers  
✔ MUST include:
   - IDENTIFICATION DIVISION (ALL lines)
   - ENVIRONMENT DIVISION (ALL lines)
   - DATA DIVISION (ALL lines)
       → All FD’s  
       → All 01/05/10/15/77 levels  
       → All FILLER lines  
       → All OCCURS tables  
       → All REDEFINES  
   - PROCEDURE DIVISION (ALL lines)
       → Every statement  
       → Every continuation line  
       → Every period

✔ MUST wrap all code in ```cobol``` blocks
✔ MUST include at least one ```cobol``` code block

❌ MUST NOT:
   - Alter code  
   - Summarize code  
   - Compress or combine lines  
   - Invent missing lines  
   - Add or remove spaces  
   - Add commentary inside ```cobol``` blocks  

═══════════════════════════════════════════════════════════════════════════
📌 REQUIREMENTS FOR BLOCK EXPLANATIONS (CRITICAL JOB #2)
═══════════════════════════════════════════════════════════════════════════

✔ MUST include each block’s code (verbatim) in its own ```cobol``` block  
✔ MUST provide a detailed explanation for each block  
✔ MUST cover: logic, flow, variables, I/O, calls, transformations  

⚠️ Explanation content may be shortened ONLY if token limits force it.

❌ Explanations may NOT replace code.  
❌ Blocks may NOT be skipped.  

═══════════════════════════════════════════════════════════════════════════
🚫 FORBIDDEN KEYWORDS (CAUSES AUTOMATIC VALIDATION FAILURE)
═══════════════════════════════════════════════════════════════════════════

The following MUST NOT appear in ANY code section:

- “omitted”  
- “skipped”  
- “similar”  
- “pattern continues”  
- “pattern repeats”  
- “...” for omission  

═══════════════════════════════════════════════════════════════════════════
🔍 EXECUTABLE LINE COVERAGE REQUIREMENT
═══════════════════════════════════════════════════════════════════════════

- Automated validation counts every executable COBOL line in your output.
- Expected executable lines = {{line_count}} – [excluded comment/page-break lines]
- Your included lines / expected lines must be == 100%.

═══════════════════════════════════════════════════════════════════════════
🧠 FINAL REMINDERS
═══════════════════════════════════════════════════════════════════════════

- You must always complete BOTH CRITICAL JOBS unless token limits are exceeded.
- If forced to choose due to output length, ALWAYS complete CRITICAL JOB #1 first.
- Never alter or summarize code.
- Never omit explanations unless token limit requires — and even then, reproduce all code.
- The validator checks code fidelity, block coverage, and == 100% line coverage.

═══════════════════════════════════════════════════════════════════════════
🎯 SUCCESS METRIC: Perfect Verbatim Code + Complete Block Explanations
═══════════════════════════════════════════════════════════════════════════


**CHUNK 35 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T18:05:37.383587", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 35 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 16897 to 17407 (511 lines)\nChunk Tokens (estimated): ~7,875\nActual Input Tokens: 9,281 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 16897-17407 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 35 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 35 of 55.\n\n\n=============================================================================\nCHUNK 35 SOURCE CODE (Lines 16897-17407)\n=============================================================================\n\n```cobol\n033802 Z-23-PROCEDURE.\n033804*\n033806     MOVE 0 TO Z-EXIT-CODE.\n033808     MOVE 9999 TO Z-EXIT-LEVEL.\n033810     IF WS-MDRPT-OPEN = 0\n033812         NEXT SENTENCE ELSE\n033814         GO TO Z-23-1-1-ELSE.\n033816     IF NOT Z-SW3\n033818         NEXT SENTENCE ELSE\n033820         GO TO Z-23-2-1-ELSE.\n033822     MOVE 1 TO WS-NEW-RPT.\n033824     MOVE \"Y\" TO WS-LIST-REQUEST.\n033826************ PERFORM RMDRPT-SETUP\n033828     PERFORM Z-24-PROCEDURE THRU Z-24-XIT.\n033830     IF  Z-EXIT-EDITEXIT\n033832         GO TO Z-23-XIT.\n033834     IF  Z-DMS2-ABORT-FLAG = 1\n033836         GO TO Z-23-XIT.\n033838     IF  Z-EXIT-LEVEL < 0\n033840         GO TO Z-23-END.\n033842*\n033844     MOVE 1 TO WS-MDRPT-OPEN.\n033846 Z-23-2-1-ELSE.\n033848 Z-23-1-1-ELSE.\n033850     IF WS-MDRPT2-OPEN = 0\n033852         NEXT SENTENCE ELSE\n033854         GO TO Z-23-7-1-ELSE.\n033856     IF NOT Z-SW3\n033858         NEXT SENTENCE ELSE\n033860         GO TO Z-23-8-1-ELSE.\n033862     MOVE 1 TO WS-NEW-RPT.\n033864     MOVE \"Y\" TO WS-FICHE-REQUEST.\n033866************ PERFORM RMDRPT2-SETUP\n033868     PERFORM Z-25-PROCEDURE THRU Z-25-XIT.\n033870     IF  Z-EXIT-EDITEXIT\n033872         GO TO Z-23-XIT.\n033874     IF  Z-DMS2-ABORT-FLAG = 1\n033876         GO TO Z-23-XIT.\n033878     IF  Z-EXIT-LEVEL < 0\n033880         GO TO Z-23-END.\n033882*\n033884     MOVE 1 TO WS-MDRPT2-OPEN.\n033886 Z-23-8-1-ELSE.\n033888 Z-23-7-1-ELSE.\n033890     IF WS-1ST-TIME = 0\n033892         NEXT SENTENCE ELSE\n033894         GO TO Z-23-13-1-ELSE.\n033896     MOVE 1 TO WS-1ST-TIME.\n033898     MOVE TDB-TDAC-TIN-NBR TO WS-PREV-TIN.\n033900 Z-23-13-1-ELSE.\n033902     MOVE TDB-TDAI-CUST TO RMDRPT-CUST-3.\n033904     MOVE TDB-TDAI-ACCT TO RMDRPT-ACCT-3.\n033906     MOVE TDB-TDAC-NAME-1 TO RMDRPT-NAME-4.\n033908     MOVE TDB-TDAC-NAME-2 TO RMDRPT-NAME-8.\n033910     MOVE TDB-TDAC-BIRTH-DT TO Z-DATE2-FORMAT-9.\n033912*\n033914     PERFORM Z-DATE-INITIALIZE-REGS\n033916         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n033918     MOVE Z-DATE2-MM TO Z-DATE6-MM.\n033920     MOVE \"/\" TO Z-DATE6-CH1.\n033922     MOVE Z-DATE2-DD TO Z-DATE6-DD.\n033924     MOVE \"/\" TO Z-DATE6-CH2.\n033926     MOVE Z-DATE2-CC TO Z-DATE6-CC.\n033928     MOVE Z-DATE2-YY TO Z-DATE6-YY.\n033930     MOVE Z-DATE6-FORMAT TO RMDRPT-BIRTH-DT-3.\n033932     IF TDB-TDAC-BIRTH-DT > 0\n033934         NEXT SENTENCE ELSE\n033936         GO TO Z-23-21-1-ELSE.\n033938     IF TDB-TDAC-BIRTH-DT < 19490701\n033940         NEXT SENTENCE ELSE\n033942         GO TO Z-23-22-1-ELSE.\n033944*\n033946     PERFORM Z-DATE-INITIALIZE-REGS\n033948         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n033950     PERFORM Z-DATE-INITIALIZE-CTRL\n033952        THRU Z-DATE-INITIALIZE-CTRL-EXIT.\n033954     MOVE TDB-TDAC-BIRTH-DT TO Z-DATE2-FORMAT-9.\n033956*    DATE UNIT INITIALIZATION\n033958     COMPUTE Z-DATE-Y = 70.\n033960*    LOAD DATE REGISTERS FOR CALCULATIONS\n033962*    LOAD DATE REGISTER 1\n033964     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n033966     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n033968     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n033970     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n033972     PERFORM Z-DATE-CALC-LEAP-YEAR\n033974        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n033976     PERFORM Z-DATE-MDY-TO-JUL-CTRL\n033978        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.\n033980     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.\n033982*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS\n033984     IF Z-DATE-Y NOT = ZEROS\n033986         PERFORM Z-DATE-CALC-Y\n033988            THRU Z-DATE-CALC-Y-EXIT.\n033990     IF Z-DATE-C NOT = ZEROS\n033992         PERFORM Z-DATE-CALC-C\n033994            THRU Z-DATE-CALC-C-EXIT.\n033996*    RE-ADJUST AFTER CALCULATIONS\n033998     PERFORM Z-DATE-CALC-LEAP-YEAR\n034000        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n034002     PERFORM Z-DATE-CALC-MONTH-DAYS\n034004        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.\n034006*    PLACE THE RESULTS WHERE THEY BELONG\n034008     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.\n034010     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.\n034012     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.\n034014     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.\n034016     MOVE Z-DATE2-FORMAT TO WS-RMD-DATE.\n034018*\n034020     PERFORM Z-DATE-INITIALIZE-REGS\n034022         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n034024     PERFORM Z-DATE-INITIALIZE-CTRL\n034026        THRU Z-DATE-INITIALIZE-CTRL-EXIT.\n034028     MOVE WS-RMD-DATE TO Z-DATE2-FORMAT.\n034030*    DATE UNIT INITIALIZATION\n034032     COMPUTE Z-DATE-M = 6.\n034034*    LOAD DATE REGISTERS FOR CALCULATIONS\n034036*    LOAD DATE REGISTER 1\n034038     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n034040     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n034042     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n034044     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n034046     PERFORM Z-DATE-CALC-LEAP-YEAR\n034048        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n034050     PERFORM Z-DATE-MDY-TO-JUL-CTRL\n034052        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.\n034054     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.\n034056*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS\n034058     IF Z-DATE-M NOT = ZEROS\n034060         PERFORM Z-DATE-CALC-M\n034062            THRU Z-DATE-CALC-M-EXIT.\n034064     IF Z-DATE-Y NOT = ZEROS\n034066         PERFORM Z-DATE-CALC-Y\n034068            THRU Z-DATE-CALC-Y-EXIT.\n034070     IF Z-DATE-C NOT = ZEROS\n034072         PERFORM Z-DATE-CALC-C\n034074            THRU Z-DATE-CALC-C-EXIT.\n034076*    RE-ADJUST AFTER CALCULATIONS\n034078     PERFORM Z-DATE-CALC-LEAP-YEAR\n034080        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n034082     PERFORM Z-DATE-CALC-MONTH-DAYS\n034084        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.\n034086*    PLACE THE RESULTS WHERE THEY BELONG\n034088     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.\n034090     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.\n034092     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.\n034094     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.\n034096     MOVE Z-DATE2-FORMAT TO WS-RMD-DATE.\n034098     MOVE WS-RMD-DATE TO Z-DATE2-FORMAT.\n034100*\n034102     PERFORM Z-DATE-INITIALIZE-REGS\n034104         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n034106     MOVE Z-DATE2-MM TO Z-DATE6-MM.\n034108     MOVE \"/\" TO Z-DATE6-CH1.\n034110     MOVE Z-DATE2-DD TO Z-DATE6-DD.\n034112     MOVE \"/\" TO Z-DATE6-CH2.\n034114     MOVE Z-DATE2-CC TO Z-DATE6-CC.\n034116     MOVE Z-DATE2-YY TO Z-DATE6-YY.\n034118     MOVE Z-DATE6-FORMAT TO RMDRPT-AGE-DATE-3.\n034120     GO TO Z-23-22-ENDIF.\n034122 Z-23-22-1-ELSE.\n034124     IF TDB-TDAC-BIRTH-DT < 19510101\n034126         NEXT SENTENCE ELSE\n034128         GO TO Z-23-22-2-ELSE.\n034130*\n034132     PERFORM Z-DATE-INITIALIZE-REGS\n034134         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n034136     PERFORM Z-DATE-INITIALIZE-CTRL\n034138        THRU Z-DATE-INITIALIZE-CTRL-EXIT.\n034140     MOVE TDB-TDAC-BIRTH-DT TO Z-DATE2-FORMAT-9.\n034142*    DATE UNIT INITIALIZATION\n034144     COMPUTE Z-DATE-Y = 72.\n034146*    LOAD DATE REGISTERS FOR CALCULATIONS\n034148*    LOAD DATE REGISTER 1\n034150     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n034152     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n034154     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n034156     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n034158     PERFORM Z-DATE-CALC-LEAP-YEAR\n034160        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n034162     PERFORM Z-DATE-MDY-TO-JUL-CTRL\n034164        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.\n034166     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.\n034168*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS\n034170     IF Z-DATE-Y NOT = ZEROS\n034172         PERFORM Z-DATE-CALC-Y\n034174            THRU Z-DATE-CALC-Y-EXIT.\n034176     IF Z-DATE-C NOT = ZEROS\n034178         PERFORM Z-DATE-CALC-C\n034180            THRU Z-DATE-CALC-C-EXIT.\n034182*    RE-ADJUST AFTER CALCULATIONS\n034184     PERFORM Z-DATE-CALC-LEAP-YEAR\n034186        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n034188     PERFORM Z-DATE-CALC-MONTH-DAYS\n034190        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.\n034192*    PLACE THE RESULTS WHERE THEY BELONG\n034194     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.\n034196     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.\n034198     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.\n034200     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.\n034202     MOVE Z-DATE2-FORMAT TO WS-RMD-DATE.\n034204     MOVE WS-RMD-DATE TO Z-DATE2-FORMAT.\n034206*\n034208     PERFORM Z-DATE-INITIALIZE-REGS\n034210         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n034212     MOVE Z-DATE2-MM TO Z-DATE6-MM.\n034214     MOVE \"/\" TO Z-DATE6-CH1.\n034216     MOVE Z-DATE2-DD TO Z-DATE6-DD.\n034218     MOVE \"/\" TO Z-DATE6-CH2.\n034220     MOVE Z-DATE2-CC TO Z-DATE6-CC.\n034222     MOVE Z-DATE2-YY TO Z-DATE6-YY.\n034224     MOVE Z-DATE6-FORMAT TO RMDRPT-AGE-DATE-3.\n034226     GO TO Z-23-22-ENDIF.\n034228 Z-23-22-2-ELSE.\n034230*\n034232     PERFORM Z-DATE-INITIALIZE-REGS\n034234         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n034236     PERFORM Z-DATE-INITIALIZE-CTRL\n034238        THRU Z-DATE-INITIALIZE-CTRL-EXIT.\n034240     MOVE TDB-TDAC-BIRTH-DT TO Z-DATE2-FORMAT-9.\n034242*    DATE UNIT INITIALIZATION\n034244     COMPUTE Z-DATE-Y = 73.\n034246*    LOAD DATE REGISTERS FOR CALCULATIONS\n034248*    LOAD DATE REGISTER 1\n034250     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n034252     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n034254     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n034256     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n034258     PERFORM Z-DATE-CALC-LEAP-YEAR\n034260        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n034262     PERFORM Z-DATE-MDY-TO-JUL-CTRL\n034264        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.\n034266     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.\n034268*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS\n034270     IF Z-DATE-Y NOT = ZEROS\n034272         PERFORM Z-DATE-CALC-Y\n034274            THRU Z-DATE-CALC-Y-EXIT.\n034276     IF Z-DATE-C NOT = ZEROS\n034278         PERFORM Z-DATE-CALC-C\n034280            THRU Z-DATE-CALC-C-EXIT.\n034282*    RE-ADJUST AFTER CALCULATIONS\n034284     PERFORM Z-DATE-CALC-LEAP-YEAR\n034286        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n034288     PERFORM Z-DATE-CALC-MONTH-DAYS\n034290        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.\n034292*    PLACE THE RESULTS WHERE THEY BELONG\n034294     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.\n034296     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.\n034298     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.\n034300     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.\n034302     MOVE Z-DATE2-FORMAT TO WS-RMD-DATE.\n034304     MOVE WS-RMD-DATE TO Z-DATE2-FORMAT.\n034306*\n034308     PERFORM Z-DATE-INITIALIZE-REGS\n034310         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n034312     MOVE Z-DATE2-MM TO Z-DATE6-MM.\n034314     MOVE \"/\" TO Z-DATE6-CH1.\n034316     MOVE Z-DATE2-DD TO Z-DATE6-DD.\n034318     MOVE \"/\" TO Z-DATE6-CH2.\n034320     MOVE Z-DATE2-CC TO Z-DATE6-CC.\n034322     MOVE Z-DATE2-YY TO Z-DATE6-YY.\n034324     MOVE Z-DATE6-FORMAT TO RMDRPT-AGE-DATE-3.\n034326 Z-23-22-ENDIF.\n034328 Z-23-21-1-ELSE.\n034330     MOVE PROCESS-DATE TO WS-DATE-CCYYMMDD.\n034332     IF WS-RMD-DATE-CCYY < WS-DATE-CCYY\n034334         NEXT SENTENCE ELSE\n034336         GO TO Z-23-31-1-ELSE.\n034338     MOVE 1231 TO WS-DATE-MMDD.\n034340     GO TO Z-23-31-ENDIF.\n034342 Z-23-31-1-ELSE.\n034344*\n034346     PERFORM Z-DATE-INITIALIZE-REGS\n034348         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n034350     PERFORM Z-DATE-INITIALIZE-CTRL\n034352        THRU Z-DATE-INITIALIZE-CTRL-EXIT.\n034354     MOVE WS-DATE-CCYYMMDD TO Z-DATE2-FORMAT.\n034356*    DATE UNIT INITIALIZATION\n034358     COMPUTE Z-DATE-Y = 1.\n034360*    LOAD DATE REGISTERS FOR CALCULATIONS\n034362*    LOAD DATE REGISTER 1\n034364     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n034366     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n034368     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n034370     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n034372     PERFORM Z-DATE-CALC-LEAP-YEAR\n034374        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n034376     PERFORM Z-DATE-MDY-TO-JUL-CTRL\n034378        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.\n034380     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.\n034382*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS\n034384     IF Z-DATE-Y NOT = ZEROS\n034386         PERFORM Z-DATE-CALC-Y\n034388            THRU Z-DATE-CALC-Y-EXIT.\n034390     IF Z-DATE-C NOT = ZEROS\n034392         PERFORM Z-DATE-CALC-C\n034394            THRU Z-DATE-CALC-C-EXIT.\n034396*    RE-ADJUST AFTER CALCULATIONS\n034398     PERFORM Z-DATE-CALC-LEAP-YEAR\n034400        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n034402     PERFORM Z-DATE-CALC-MONTH-DAYS\n034404        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.\n034406*    PLACE THE RESULTS WHERE THEY BELONG\n034408     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.\n034410     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.\n034412     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.\n034414     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.\n034416     MOVE Z-DATE2-FORMAT TO WS-DATE-CCYYMMDD.\n034418     MOVE 0401 TO WS-DATE-MMDD.\n034420 Z-23-31-ENDIF.\n034422     IF TDB-TDAA-INHERIT-IRA > 0\n034424         NEXT SENTENCE ELSE\n034426         GO TO Z-23-35-1-ELSE.\n034428     MOVE \"          \" TO RMDRPT-BEG-DATE-3.\n034430     IF TDB-TDAA-INHERIT-IRA = 1\n034432         NEXT SENTENCE ELSE\n034434         GO TO Z-23-37-1-ELSE.\n034436     MOVE PROCESS-DATE-CCYY TO WS-DATE-CCYY.\n034438     MOVE 1231 TO WS-DATE-MMDD.\n034440     MOVE WS-DATE-CCYYMMDD TO Z-DATE2-FORMAT.\n034442*\n034444     PERFORM Z-DATE-INITIALIZE-REGS\n034446         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n034448     MOVE Z-DATE2-MM TO Z-DATE6-MM.\n034450     MOVE \"/\" TO Z-DATE6-CH1.\n034452     MOVE Z-DATE2-DD TO Z-DATE6-DD.\n034454     MOVE \"/\" TO Z-DATE6-CH2.\n034456     MOVE Z-DATE2-CC TO Z-DATE6-CC.\n034458     MOVE Z-DATE2-YY TO Z-DATE6-YY.\n034460     MOVE Z-DATE6-FORMAT TO RMDRPT-BEG-DATE-3.\n034462     GO TO Z-23-37-ENDIF.\n034464 Z-23-37-1-ELSE.\n034466     IF ( TDB-TDAA-INHERIT-IRA = 2 ) AND ( TDB-TDAA-BNF-DEATH-DT  \n034468         > 20191231 )\n034470         NEXT SENTENCE ELSE\n034472         GO TO Z-23-37-2-ELSE.\n034474*\n034476     PERFORM Z-DATE-INITIALIZE-REGS\n034478         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n034480     PERFORM Z-DATE-INITIALIZE-CTRL\n034482        THRU Z-DATE-INITIALIZE-CTRL-EXIT.\n034484     MOVE TDB-TDAA-BNF-DEATH-DT TO Z-DATE2-FORMAT-9.\n034486*    DATE UNIT INITIALIZATION\n034488     COMPUTE Z-DATE-Y = 10.\n034490*    LOAD DATE REGISTERS FOR CALCULATIONS\n034492*    LOAD DATE REGISTER 1\n034494     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n034496     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n034498     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n034500     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n034502     PERFORM Z-DATE-CALC-LEAP-YEAR\n034504        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n034506     PERFORM Z-DATE-MDY-TO-JUL-CTRL\n034508        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.\n034510     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.\n034512*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS\n034514     IF Z-DATE-Y NOT = ZEROS\n034516         PERFORM Z-DATE-CALC-Y\n034518            THRU Z-DATE-CALC-Y-EXIT.\n034520     IF Z-DATE-C NOT = ZEROS\n034522         PERFORM Z-DATE-CALC-C\n034524            THRU Z-DATE-CALC-C-EXIT.\n034526*    RE-ADJUST AFTER CALCULATIONS\n034528     PERFORM Z-DATE-CALC-LEAP-YEAR\n034530        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n034532     PERFORM Z-DATE-CALC-MONTH-DAYS\n034534        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.\n034536*    PLACE THE RESULTS WHERE THEY BELONG\n034538     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.\n034540     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.\n034542     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.\n034544     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.\n034546     MOVE Z-DATE2-FORMAT TO WS-DATE-CYMD.\n034548     MOVE 1231 TO WS-DATE-MD.\n034550     MOVE WS-DATE-CYMD TO Z-DATE2-FORMAT.\n034552*\n034554     PERFORM Z-DATE-INITIALIZE-REGS\n034556         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n034558     MOVE Z-DATE2-MM TO Z-DATE6-MM.\n034560     MOVE \"/\" TO Z-DATE6-CH1.\n034562     MOVE Z-DATE2-DD TO Z-DATE6-DD.\n034564     MOVE \"/\" TO Z-DATE6-CH2.\n034566     MOVE Z-DATE2-CC TO Z-DATE6-CC.\n034568     MOVE Z-DATE2-YY TO Z-DATE6-YY.\n034570     MOVE Z-DATE6-FORMAT TO RMDRPT-BEG-DATE-3.\n034572     GO TO Z-23-37-ENDIF.\n034574 Z-23-37-2-ELSE.\n034576     MOVE PROCESS-DATE-CCYY TO WS-DATE-CCYY.\n034578     MOVE 1231 TO WS-DATE-MMDD.\n034580     MOVE WS-DATE-CCYYMMDD TO Z-DATE2-FORMAT.\n034582*\n034584     PERFORM Z-DATE-INITIALIZE-REGS\n034586         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n034588     MOVE Z-DATE2-MM TO Z-DATE6-MM.\n034590     MOVE \"/\" TO Z-DATE6-CH1.\n034592     MOVE Z-DATE2-DD TO Z-DATE6-DD.\n034594     MOVE \"/\" TO Z-DATE6-CH2.\n034596     MOVE Z-DATE2-CC TO Z-DATE6-CC.\n034598     MOVE Z-DATE2-YY TO Z-DATE6-YY.\n034600     MOVE Z-DATE6-FORMAT TO RMDRPT-BEG-DATE-3.\n034602 Z-23-37-ENDIF.\n034604     IF TDB-TDAA-IRA-TYPE = 13\n034606         NEXT SENTENCE ELSE\n034608         GO TO Z-23-47-1-ELSE.\n034610     IF TDB-TDAA-INHERIT-IRA = 1\n034612         NEXT SENTENCE ELSE\n034614         GO TO Z-23-48-1-ELSE.\n034616     MOVE \"SPOUSE INHERITED ROTH  \" TO RMDRPT-REMARK2-4.\n034618     GO TO Z-23-48-ENDIF.\n034620 Z-23-48-1-ELSE.\n034622     MOVE \"NON-SP INHERITED ROTH  \" TO RMDRPT-REMARK2-4.\n034624 Z-23-48-ENDIF.\n034626     GO TO Z-23-47-ENDIF.\n034628 Z-23-47-1-ELSE.\n034630     IF TDB-TDAA-IRA-TYPE = 15\n034632         NEXT SENTENCE ELSE\n034634         GO TO Z-23-47-2-ELSE.\n034636     IF TDB-TDAA-INHERIT-IRA = 1\n034638         NEXT SENTENCE ELSE\n034640         GO TO Z-23-51-1-ELSE.\n034642     MOVE \"SPOUSE INHERIT CNV ROTH\" TO RMDRPT-REMARK2-4.\n034644     GO TO Z-23-51-ENDIF.\n034646 Z-23-51-1-ELSE.\n034648     MOVE \"NON-SP INHERIT CNV ROTH\" TO RMDRPT-REMARK2-4.\n034650 Z-23-51-ENDIF.\n034652     GO TO Z-23-47-ENDIF.\n034654 Z-23-47-2-ELSE.\n034656     IF TDB-TDAA-IRA-TYPE = 17\n034658         NEXT SENTENCE ELSE\n034660         GO TO Z-23-47-3-ELSE.\n034662     IF TDB-TDAA-INHERIT-IRA = 1\n034664         NEXT SENTENCE ELSE\n034666         GO TO Z-23-54-1-ELSE.\n034668     MOVE \"SP INHERIT S-DIR ROTH  \" TO RMDRPT-REMARK2-4.\n034670     GO TO Z-23-54-ENDIF.\n034672 Z-23-54-1-ELSE.\n034674     MOVE \"NON-SP INH S-DIR ROTH  \" TO RMDRPT-REMARK2-4.\n034676 Z-23-54-ENDIF.\n034678     GO TO Z-23-47-ENDIF.\n034680 Z-23-47-3-ELSE.\n034682     IF TDB-TDAA-INHERIT-IRA = 1\n034684         NEXT SENTENCE ELSE\n034686         GO TO Z-23-57-1-ELSE.\n034688     MOVE \"SPOUSE INHERITED IRA   \" TO RMDRPT-REMARK2-4.\n034690     GO TO Z-23-57-ENDIF.\n034692 Z-23-57-1-ELSE.\n034694     MOVE \"NON-SP INHERITED IRA   \" TO RMDRPT-REMARK2-4.\n034696 Z-23-57-ENDIF.\n034698 Z-23-47-ENDIF.\n034700     GO TO Z-23-35-ENDIF.\n034702 Z-23-35-1-ELSE.\n034704     MOVE WS-DATE-CCYYMMDD TO Z-DATE2-FORMAT.\n034706*\n034708     PERFORM Z-DATE-INITIALIZE-REGS\n034710         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n034712     MOVE Z-DATE2-MM TO Z-DATE6-MM.\n034714     MOVE \"/\" TO Z-DATE6-CH1.\n034716     MOVE Z-DATE2-DD TO Z-DATE6-DD.\n034718     MOVE \"/\" TO Z-DATE6-CH2.\n034720     MOVE Z-DATE2-CC TO Z-DATE6-CC.\n034722     MOVE Z-DATE2-YY TO Z-DATE6-YY.\n034724     MOVE Z-DATE6-FORMAT TO RMDRPT-BEG-DATE-3.\n034726     MOVE SPACES TO RMDRPT-REMARK2-4.\n034728 Z-23-35-ENDIF.\n034730     MOVE WS-MD-FMV TO RMDRPT-BAL-BEG-YR-3\n034732       , RMDRPT2-BAL-BEG-YR-3.\n034734     IF TDB-TDAA-FAIR-MRKT = ZEROS\n034736         NEXT SENTENCE ELSE\n034738         GO TO Z-23-63-1-ELSE.\n034740     MOVE \"*\" TO RMDRPT-CUR-BAL-IND-3.\n034742     GO TO Z-23-63-ENDIF.\n034744 Z-23-63-1-ELSE.\n034746     MOVE SPACE TO RMDRPT-CUR-BAL-IND-3.\n034748 Z-23-63-ENDIF.\n034750     MOVE WS-MD-FACT TO RMDRPT-FACTOR-3\n034752       , RMDRPT2-FACTOR-3.\n034754     MOVE WS-MD-TBL TO RMDRPT-TBL-3.\n034756     MOVE WS-MD-AMT TO RMDRPT-MINDIST-3\n034758       , RMDRPT2-MINDIST-3.\n034760     IF TDB-TDAA-RMD-MAN-CALC = ZERO\n034762         NEXT SENTENCE ELSE\n034764         GO TO Z-23-69-1-ELSE.\n034766     MOVE SPACE TO RMDRPT-RMD-MAN-CALC-3.\n034768     GO TO Z-23-69-ENDIF.\n034770 Z-23-69-1-ELSE.\n034772     MOVE \"*\" TO RMDRPT-RMD-MAN-CALC-3.\n034774 Z-23-69-ENDIF.\n034776     MOVE \"/\" TO RMDRPT-SLASH-3.\n034778     MOVE SPACES TO RMDRPT-DS-METH-4\n034780       , RMDRPT-WH-MSG-4.\n034782     MOVE ZEROS TO WS-NEW-DS-AMT.\n034784     IF ( TDB-TDAA-BENEF-CD = 1 ) AND ( TDB-TDAA-BNF-BIRTH-DT =   \n034786         ZEROS )\n034788         NEXT SENTENCE ELSE\n034790         GO TO Z-23-75-1-ELSE.\n034792     MOVE \"CANNOT USE JOINT LIFE, MISSING SPOUSE BD\" TO           \n034794         RMDRPT-REMARK-4.\n034796     GO TO Z-23-75-ENDIF.\n034798 Z-23-75-1-ELSE.\n034800     MOVE SPACES TO RMDRPT-REMARK-4.\n034802 Z-23-75-ENDIF.\n034804     IF ( TDB-TDAA-INHERIT-IRA = 2 ) AND ( TDB-TDAA-RMD-MAN-CALC  \n034806         = 0 )\n034808         NEXT SENTENCE ELSE\n034810         GO TO Z-23-78-1-ELSE.\n034812     IF ( TDB-TDAA-BNF-DEATH-DT = 0 ) OR ( TDB-TDAA-BNF-DEATH-DT  \n034814         > 20191231 ) OR ( TDB-TDAA-IRA-TYPE = 13 OR 15 OR 17 )\n034816         NEXT SENTENCE ELSE\n034818         GO TO Z-23-79-1-ELSE.\n034820     MOVE \"UNABLE TO CALCULATE RMD\" TO RMDRPT-REMARK-4.\n034822 Z-23-79-1-ELSE.\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    511 lines from 16897 to 17407.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 35, "total_chunks": 55, "start_line": 16897, "end_line": 17407, "line_count": 511}

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
- Source code length: 25157 characters

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
CHUNK 35 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 16897 to 17407 (511 lines)
Chunk Tokens (estimated): ~7,875
Actual Input Tokens: 9,281 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 16897-17407 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 35 of 55 chunks
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
      The source code below is only CHUNK 35 of 55.


=============================================================================
CHUNK 35 SOURCE CODE (Lines 16897-17407)
=============================================================================

```cobol
033802 Z-23-PROCEDURE.
033804*
033806     MOVE 0 TO Z-EXIT-CODE.
033808     MOVE 9999 TO Z-EXIT-LEVEL.
033810     IF WS-MDRPT-OPEN = 0
033812         NEXT SENTENCE ELSE
033814         GO TO Z-23-1-1-ELSE.
033816     IF NOT Z-SW3
033818         NEXT SENTENCE ELSE
033820         GO TO Z-23-2-1-ELSE.
033822     MOVE 1 TO WS-NEW-RPT.
033824     MOVE "Y" TO WS-LIST-REQUEST.
033826************ PERFORM RMDRPT-SETUP
033828     PERFORM Z-24-PROCEDURE THRU Z-24-XIT.
033830     IF  Z-EXIT-EDITEXIT
033832         GO TO Z-23-XIT.
033834     IF  Z-DMS2-ABORT-FLAG = 1
033836         GO TO Z-23-XIT.
033838     IF  Z-EXIT-LEVEL < 0
033840         GO TO Z-23-END.
033842*
033844     MOVE 1 TO WS-MDRPT-OPEN.
033846 Z-23-2-1-ELSE.
033848 Z-23-1-1-ELSE.
033850     IF WS-MDRPT2-OPEN = 0
033852         NEXT SENTENCE ELSE
033854         GO TO Z-23-7-1-ELSE.
033856     IF NOT Z-SW3
033858         NEXT SENTENCE ELSE
033860         GO TO Z-23-8-1-ELSE.
033862     MOVE 1 TO WS-NEW-RPT.
033864     MOVE "Y" TO WS-FICHE-REQUEST.
033866************ PERFORM RMDRPT2-SETUP
033868     PERFORM Z-25-PROCEDURE THRU Z-25-XIT.
033870     IF  Z-EXIT-EDITEXIT
033872         GO TO Z-23-XIT.
033874     IF  Z-DMS2-ABORT-FLAG = 1
033876         GO TO Z-23-XIT.
033878     IF  Z-EXIT-LEVEL < 0
033880         GO TO Z-23-END.
033882*
033884     MOVE 1 TO WS-MDRPT2-OPEN.
033886 Z-23-8-1-ELSE.
033888 Z-23-7-1-ELSE.
033890     IF WS-1ST-TIME = 0
033892         NEXT SENTENCE ELSE
033894         GO TO Z-23-13-1-ELSE.
033896     MOVE 1 TO WS-1ST-TIME.
033898     MOVE TDB-TDAC-TIN-NBR TO WS-PREV-TIN.
033900 Z-23-13-1-ELSE.
033902     MOVE TDB-TDAI-CUST TO RMDRPT-CUST-3.
033904     MOVE TDB-TDAI-ACCT TO RMDRPT-ACCT-3.
033906     MOVE TDB-TDAC-NAME-1 TO RMDRPT-NAME-4.
033908     MOVE TDB-TDAC-NAME-2 TO RMDRPT-NAME-8.
033910     MOVE TDB-TDAC-BIRTH-DT TO Z-DATE2-FORMAT-9.
033912*
033914     PERFORM Z-DATE-INITIALIZE-REGS
033916         THRU Z-DATE-INITIALIZE-REGS-EXIT.
033918     MOVE Z-DATE2-MM TO Z-DATE6-MM.
033920     MOVE "/" TO Z-DATE6-CH1.
033922     MOVE Z-DATE2-DD TO Z-DATE6-DD.
033924     MOVE "/" TO Z-DATE6-CH2.
033926     MOVE Z-DATE2-CC TO Z-DATE6-CC.
033928     MOVE Z-DATE2-YY TO Z-DATE6-YY.
033930     MOVE Z-DATE6-FORMAT TO RMDRPT-BIRTH-DT-3.
033932     IF TDB-TDAC-BIRTH-DT > 0
033934         NEXT SENTENCE ELSE
033936         GO TO Z-23-21-1-ELSE.
033938     IF TDB-TDAC-BIRTH-DT < 19490701
033940         NEXT SENTENCE ELSE
033942         GO TO Z-23-22-1-ELSE.
033944*
033946     PERFORM Z-DATE-INITIALIZE-REGS
033948         THRU Z-DATE-INITIALIZE-REGS-EXIT.
033950     PERFORM Z-DATE-INITIALIZE-CTRL
033952        THRU Z-DATE-INITIALIZE-CTRL-EXIT.
033954     MOVE TDB-TDAC-BIRTH-DT TO Z-DATE2-FORMAT-9.
033956*    DATE UNIT INITIALIZATION
033958     COMPUTE Z-DATE-Y = 70.
033960*    LOAD DATE REGISTERS FOR CALCULATIONS
033962*    LOAD DATE REGISTER 1
033964     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
033966     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
033968     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
033970     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
033972     PERFORM Z-DATE-CALC-LEAP-YEAR
033974        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
033976     PERFORM Z-DATE-MDY-TO-JUL-CTRL
033978        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.
033980     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.
033982*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS
033984     IF Z-DATE-Y NOT = ZEROS
033986         PERFORM Z-DATE-CALC-Y
033988            THRU Z-DATE-CALC-Y-EXIT.
033990     IF Z-DATE-C NOT = ZEROS
033992         PERFORM Z-DATE-CALC-C
033994            THRU Z-DATE-CALC-C-EXIT.
033996*    RE-ADJUST AFTER CALCULATIONS
033998     PERFORM Z-DATE-CALC-LEAP-YEAR
034000        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
034002     PERFORM Z-DATE-CALC-MONTH-DAYS
034004        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.
034006*    PLACE THE RESULTS WHERE THEY BELONG
034008     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.
034010     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.
034012     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.
034014     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.
034016     MOVE Z-DATE2-FORMAT TO WS-RMD-DATE.
034018*
034020     PERFORM Z-DATE-INITIALIZE-REGS
034022         THRU Z-DATE-INITIALIZE-REGS-EXIT.
034024     PERFORM Z-DATE-INITIALIZE-CTRL
034026        THRU Z-DATE-INITIALIZE-CTRL-EXIT.
034028     MOVE WS-RMD-DATE TO Z-DATE2-FORMAT.
034030*    DATE UNIT INITIALIZATION
034032     COMPUTE Z-DATE-M = 6.
034034*    LOAD DATE REGISTERS FOR CALCULATIONS
034036*    LOAD DATE REGISTER 1
034038     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
034040     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
034042     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
034044     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
034046     PERFORM Z-DATE-CALC-LEAP-YEAR
034048        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
034050     PERFORM Z-DATE-MDY-TO-JUL-CTRL
034052        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.
034054     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.
034056*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS
034058     IF Z-DATE-M NOT = ZEROS
034060         PERFORM Z-DATE-CALC-M
034062            THRU Z-DATE-CALC-M-EXIT.
034064     IF Z-DATE-Y NOT = ZEROS
034066         PERFORM Z-DATE-CALC-Y
034068            THRU Z-DATE-CALC-Y-EXIT.
034070     IF Z-DATE-C NOT = ZEROS
034072         PERFORM Z-DATE-CALC-C
034074            THRU Z-DATE-CALC-C-EXIT.
034076*    RE-ADJUST AFTER CALCULATIONS
034078     PERFORM Z-DATE-CALC-LEAP-YEAR
034080        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
034082     PERFORM Z-DATE-CALC-MONTH-DAYS
034084        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.
034086*    PLACE THE RESULTS WHERE THEY BELONG
034088     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.
034090     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.
034092     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.
034094     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.
034096     MOVE Z-DATE2-FORMAT TO WS-RMD-DATE.
034098     MOVE WS-RMD-DATE TO Z-DATE2-FORMAT.
034100*
034102     PERFORM Z-DATE-INITIALIZE-REGS
034104         THRU Z-DATE-INITIALIZE-REGS-EXIT.
034106     MOVE Z-DATE2-MM TO Z-DATE6-MM.
034108     MOVE "/" TO Z-DATE6-CH1.
034110     MOVE Z-DATE2-DD TO Z-DATE6-DD.
034112     MOVE "/" TO Z-DATE6-CH2.
034114     MOVE Z-DATE2-CC TO Z-DATE6-CC.
034116     MOVE Z-DATE2-YY TO Z-DATE6-YY.
034118     MOVE Z-DATE6-FORMAT TO RMDRPT-AGE-DATE-3.
034120     GO TO Z-23-22-ENDIF.
034122 Z-23-22-1-ELSE.
034124     IF TDB-TDAC-BIRTH-DT < 19510101
034126         NEXT SENTENCE ELSE
034128         GO TO Z-23-22-2-ELSE.
034130*
034132     PERFORM Z-DATE-INITIALIZE-REGS
034134         THRU Z-DATE-INITIALIZE-REGS-EXIT.
034136     PERFORM Z-DATE-INITIALIZE-CTRL
034138        THRU Z-DATE-INITIALIZE-CTRL-EXIT.
034140     MOVE TDB-TDAC-BIRTH-DT TO Z-DATE2-FORMAT-9.
034142*    DATE UNIT INITIALIZATION
034144     COMPUTE Z-DATE-Y = 72.
034146*    LOAD DATE REGISTERS FOR CALCULATIONS
034148*    LOAD DATE REGISTER 1
034150     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
034152     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
034154     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
034156     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
034158     PERFORM Z-DATE-CALC-LEAP-YEAR
034160        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
034162     PERFORM Z-DATE-MDY-TO-JUL-CTRL
034164        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.
034166     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.
034168*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS
034170     IF Z-DATE-Y NOT = ZEROS
034172         PERFORM Z-DATE-CALC-Y
034174            THRU Z-DATE-CALC-Y-EXIT.
034176     IF Z-DATE-C NOT = ZEROS
034178         PERFORM Z-DATE-CALC-C
034180            THRU Z-DATE-CALC-C-EXIT.
034182*    RE-ADJUST AFTER CALCULATIONS
034184     PERFORM Z-DATE-CALC-LEAP-YEAR
034186        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
034188     PERFORM Z-DATE-CALC-MONTH-DAYS
034190        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.
034192*    PLACE THE RESULTS WHERE THEY BELONG
034194     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.
034196     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.
034198     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.
034200     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.
034202     MOVE Z-DATE2-FORMAT TO WS-RMD-DATE.
034204     MOVE WS-RMD-DATE TO Z-DATE2-FORMAT.
034206*
034208     PERFORM Z-DATE-INITIALIZE-REGS
034210         THRU Z-DATE-INITIALIZE-REGS-EXIT.
034212     MOVE Z-DATE2-MM TO Z-DATE6-MM.
034214     MOVE "/" TO Z-DATE6-CH1.
034216     MOVE Z-DATE2-DD TO Z-DATE6-DD.
034218     MOVE "/" TO Z-DATE6-CH2.
034220     MOVE Z-DATE2-CC TO Z-DATE6-CC.
034222     MOVE Z-DATE2-YY TO Z-DATE6-YY.
034224     MOVE Z-DATE6-FORMAT TO RMDRPT-AGE-DATE-3.
034226     GO TO Z-23-22-ENDIF.
034228 Z-23-22-2-ELSE.
034230*
034232     PERFORM Z-DATE-INITIALIZE-REGS
034234         THRU Z-DATE-INITIALIZE-REGS-EXIT.
034236     PERFORM Z-DATE-INITIALIZE-CTRL
034238        THRU Z-DATE-INITIALIZE-CTRL-EXIT.
034240     MOVE TDB-TDAC-BIRTH-DT TO Z-DATE2-FORMAT-9.
034242*    DATE UNIT INITIALIZATION
034244     COMPUTE Z-DATE-Y = 73.
034246*    LOAD DATE REGISTERS FOR CALCULATIONS
034248*    LOAD DATE REGISTER 1
034250     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
034252     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
034254     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
034256     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
034258     PERFORM Z-DATE-CALC-LEAP-YEAR
034260        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
034262     PERFORM Z-DATE-MDY-TO-JUL-CTRL
034264        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.
034266     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.
034268*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS
034270     IF Z-DATE-Y NOT = ZEROS
034272         PERFORM Z-DATE-CALC-Y
034274            THRU Z-DATE-CALC-Y-EXIT.
034276     IF Z-DATE-C NOT = ZEROS
034278         PERFORM Z-DATE-CALC-C
034280            THRU Z-DATE-CALC-C-EXIT.
034282*    RE-ADJUST AFTER CALCULATIONS
034284     PERFORM Z-DATE-CALC-LEAP-YEAR
034286        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
034288     PERFORM Z-DATE-CALC-MONTH-DAYS
034290        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.
034292*    PLACE THE RESULTS WHERE THEY BELONG
034294     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.
034296     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.
034298     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.
034300     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.
034302     MOVE Z-DATE2-FORMAT TO WS-RMD-DATE.
034304     MOVE WS-RMD-DATE TO Z-DATE2-FORMAT.
034306*
034308     PERFORM Z-DATE-INITIALIZE-REGS
034310         THRU Z-DATE-INITIALIZE-REGS-EXIT.
034312     MOVE Z-DATE2-MM TO Z-DATE6-MM.
034314     MOVE "/" TO Z-DATE6-CH1.
034316     MOVE Z-DATE2-DD TO Z-DATE6-DD.
034318     MOVE "/" TO Z-DATE6-CH2.
034320     MOVE Z-DATE2-CC TO Z-DATE6-CC.
034322     MOVE Z-DATE2-YY TO Z-DATE6-YY.
034324     MOVE Z-DATE6-FORMAT TO RMDRPT-AGE-DATE-3.
034326 Z-23-22-ENDIF.
034328 Z-23-21-1-ELSE.
034330     MOVE PROCESS-DATE TO WS-DATE-CCYYMMDD.
034332     IF WS-RMD-DATE-CCYY < WS-DATE-CCYY
034334         NEXT SENTENCE ELSE
034336         GO TO Z-23-31-1-ELSE.
034338     MOVE 1231 TO WS-DATE-MMDD.
034340     GO TO Z-23-31-ENDIF.
034342 Z-23-31-1-ELSE.
034344*
034346     PERFORM Z-DATE-INITIALIZE-REGS
034348         THRU Z-DATE-INITIALIZE-REGS-EXIT.
034350     PERFORM Z-DATE-INITIALIZE-CTRL
034352        THRU Z-DATE-INITIALIZE-CTRL-EXIT.
034354     MOVE WS-DATE-CCYYMMDD TO Z-DATE2-FORMAT.
034356*    DATE UNIT INITIALIZATION
034358     COMPUTE Z-DATE-Y = 1.
034360*    LOAD DATE REGISTERS FOR CALCULATIONS
034362*    LOAD DATE REGISTER 1
034364     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
034366     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
034368     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
034370     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
034372     PERFORM Z-DATE-CALC-LEAP-YEAR
034374        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
034376     PERFORM Z-DATE-MDY-TO-JUL-CTRL
034378        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.
034380     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.
034382*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS
034384     IF Z-DATE-Y NOT = ZEROS
034386         PERFORM Z-DATE-CALC-Y
034388            THRU Z-DATE-CALC-Y-EXIT.
034390     IF Z-DATE-C NOT = ZEROS
034392         PERFORM Z-DATE-CALC-C
034394            THRU Z-DATE-CALC-C-EXIT.
034396*    RE-ADJUST AFTER CALCULATIONS
034398     PERFORM Z-DATE-CALC-LEAP-YEAR
034400        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
034402     PERFORM Z-DATE-CALC-MONTH-DAYS
034404        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.
034406*    PLACE THE RESULTS WHERE THEY BELONG
034408     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.
034410     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.
034412     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.
034414     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.
034416     MOVE Z-DATE2-FORMAT TO WS-DATE-CCYYMMDD.
034418     MOVE 0401 TO WS-DATE-MMDD.
034420 Z-23-31-ENDIF.
034422     IF TDB-TDAA-INHERIT-IRA > 0
034424         NEXT SENTENCE ELSE
034426         GO TO Z-23-35-1-ELSE.
034428     MOVE "          " TO RMDRPT-BEG-DATE-3.
034430     IF TDB-TDAA-INHERIT-IRA = 1
034432         NEXT SENTENCE ELSE
034434         GO TO Z-23-37-1-ELSE.
034436     MOVE PROCESS-DATE-CCYY TO WS-DATE-CCYY.
034438     MOVE 1231 TO WS-DATE-MMDD.
034440     MOVE WS-DATE-CCYYMMDD TO Z-DATE2-FORMAT.
034442*
034444     PERFORM Z-DATE-INITIALIZE-REGS
034446         THRU Z-DATE-INITIALIZE-REGS-EXIT.
034448     MOVE Z-DATE2-MM TO Z-DATE6-MM.
034450     MOVE "/" TO Z-DATE6-CH1.
034452     MOVE Z-DATE2-DD TO Z-DATE6-DD.
034454     MOVE "/" TO Z-DATE6-CH2.
034456     MOVE Z-DATE2-CC TO Z-DATE6-CC.
034458     MOVE Z-DATE2-YY TO Z-DATE6-YY.
034460     MOVE Z-DATE6-FORMAT TO RMDRPT-BEG-DATE-3.
034462     GO TO Z-23-37-ENDIF.
034464 Z-23-37-1-ELSE.
034466     IF ( TDB-TDAA-INHERIT-IRA = 2 ) AND ( TDB-TDAA-BNF-DEATH-DT  
034468         > 20191231 )
034470         NEXT SENTENCE ELSE
034472         GO TO Z-23-37-2-ELSE.
034474*
034476     PERFORM Z-DATE-INITIALIZE-REGS
034478         THRU Z-DATE-INITIALIZE-REGS-EXIT.
034480     PERFORM Z-DATE-INITIALIZE-CTRL
034482        THRU Z-DATE-INITIALIZE-CTRL-EXIT.
034484     MOVE TDB-TDAA-BNF-DEATH-DT TO Z-DATE2-FORMAT-9.
034486*    DATE UNIT INITIALIZATION
034488     COMPUTE Z-DATE-Y = 10.
034490*    LOAD DATE REGISTERS FOR CALCULATIONS
034492*    LOAD DATE REGISTER 1
034494     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
034496     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
034498     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
034500     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
034502     PERFORM Z-DATE-CALC-LEAP-YEAR
034504        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
034506     PERFORM Z-DATE-MDY-TO-JUL-CTRL
034508        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.
034510     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.
034512*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS
034514     IF Z-DATE-Y NOT = ZEROS
034516         PERFORM Z-DATE-CALC-Y
034518            THRU Z-DATE-CALC-Y-EXIT.
034520     IF Z-DATE-C NOT = ZEROS
034522         PERFORM Z-DATE-CALC-C
034524            THRU Z-DATE-CALC-C-EXIT.
034526*    RE-ADJUST AFTER CALCULATIONS
034528     PERFORM Z-DATE-CALC-LEAP-YEAR
034530        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
034532     PERFORM Z-DATE-CALC-MONTH-DAYS
034534        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.
034536*    PLACE THE RESULTS WHERE THEY BELONG
034538     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.
034540     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.
034542     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.
034544     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.
034546     MOVE Z-DATE2-FORMAT TO WS-DATE-CYMD.
034548     MOVE 1231 TO WS-DATE-MD.
034550     MOVE WS-DATE-CYMD TO Z-DATE2-FORMAT.
034552*
034554     PERFORM Z-DATE-INITIALIZE-REGS
034556         THRU Z-DATE-INITIALIZE-REGS-EXIT.
034558     MOVE Z-DATE2-MM TO Z-DATE6-MM.
034560     MOVE "/" TO Z-DATE6-CH1.
034562     MOVE Z-DATE2-DD TO Z-DATE6-DD.
034564     MOVE "/" TO Z-DATE6-CH2.
034566     MOVE Z-DATE2-CC TO Z-DATE6-CC.
034568     MOVE Z-DATE2-YY TO Z-DATE6-YY.
034570     MOVE Z-DATE6-FORMAT TO RMDRPT-BEG-DATE-3.
034572     GO TO Z-23-37-ENDIF.
034574 Z-23-37-2-ELSE.
034576     MOVE PROCESS-DATE-CCYY TO WS-DATE-CCYY.
034578     MOVE 1231 TO WS-DATE-MMDD.
034580     MOVE WS-DATE-CCYYMMDD TO Z-DATE2-FORMAT.
034582*
034584     PERFORM Z-DATE-INITIALIZE-REGS
034586         THRU Z-DATE-INITIALIZE-REGS-EXIT.
034588     MOVE Z-DATE2-MM TO Z-DATE6-MM.
034590     MOVE "/" TO Z-DATE6-CH1.
034592     MOVE Z-DATE2-DD TO Z-DATE6-DD.
034594     MOVE "/" TO Z-DATE6-CH2.
034596     MOVE Z-DATE2-CC TO Z-DATE6-CC.
034598     MOVE Z-DATE2-YY TO Z-DATE6-YY.
034600     MOVE Z-DATE6-FORMAT TO RMDRPT-BEG-DATE-3.
034602 Z-23-37-ENDIF.
034604     IF TDB-TDAA-IRA-TYPE = 13
034606         NEXT SENTENCE ELSE
034608         GO TO Z-23-47-1-ELSE.
034610     IF TDB-TDAA-INHERIT-IRA = 1
034612         NEXT SENTENCE ELSE
034614         GO TO Z-23-48-1-ELSE.
034616     MOVE "SPOUSE INHERITED ROTH  " TO RMDRPT-REMARK2-4.
034618     GO TO Z-23-48-ENDIF.
034620 Z-23-48-1-ELSE.
034622     MOVE "NON-SP INHERITED ROTH  " TO RMDRPT-REMARK2-4.
034624 Z-23-48-ENDIF.
034626     GO TO Z-23-47-ENDIF.
034628 Z-23-47-1-ELSE.
034630     IF TDB-TDAA-IRA-TYPE = 15
034632         NEXT SENTENCE ELSE
034634         GO TO Z-23-47-2-ELSE.
034636     IF TDB-TDAA-INHERIT-IRA = 1
034638         NEXT SENTENCE ELSE
034640         GO TO Z-23-51-1-ELSE.
034642     MOVE "SPOUSE INHERIT CNV ROTH" TO RMDRPT-REMARK2-4.
034644     GO TO Z-23-51-ENDIF.
034646 Z-23-51-1-ELSE.
034648     MOVE "NON-SP INHERIT CNV ROTH" TO RMDRPT-REMARK2-4.
034650 Z-23-51-ENDIF.
034652     GO TO Z-23-47-ENDIF.
034654 Z-23-47-2-ELSE.
034656     IF TDB-TDAA-IRA-TYPE = 17
034658         NEXT SENTENCE ELSE
034660         GO TO Z-23-47-3-ELSE.
034662     IF TDB-TDAA-INHERIT-IRA = 1
034664         NEXT SENTENCE ELSE
034666         GO TO Z-23-54-1-ELSE.
034668     MOVE "SP INHERIT S-DIR ROTH  " TO RMDRPT-REMARK2-4.
034670     GO TO Z-23-54-ENDIF.
034672 Z-23-54-1-ELSE.
034674     MOVE "NON-SP INH S-DIR ROTH  " TO RMDRPT-REMARK2-4.
034676 Z-23-54-ENDIF.
034678     GO TO Z-23-47-ENDIF.
034680 Z-23-47-3-ELSE.
034682     IF TDB-TDAA-INHERIT-IRA = 1
034684         NEXT SENTENCE ELSE
034686         GO TO Z-23-57-1-ELSE.
034688     MOVE "SPOUSE INHERITED IRA   " TO RMDRPT-REMARK2-4.
034690     GO TO Z-23-57-ENDIF.
034692 Z-23-57-1-ELSE.
034694     MOVE "NON-SP INHERITED IRA   " TO RMDRPT-REMARK2-4.
034696 Z-23-57-ENDIF.
034698 Z-23-47-ENDIF.
034700     GO TO Z-23-35-ENDIF.
034702 Z-23-35-1-ELSE.
034704     MOVE WS-DATE-CCYYMMDD TO Z-DATE2-FORMAT.
034706*
034708     PERFORM Z-DATE-INITIALIZE-REGS
034710         THRU Z-DATE-INITIALIZE-REGS-EXIT.
034712     MOVE Z-DATE2-MM TO Z-DATE6-MM.
034714     MOVE "/" TO Z-DATE6-CH1.
034716     MOVE Z-DATE2-DD TO Z-DATE6-DD.
034718     MOVE "/" TO Z-DATE6-CH2.
034720     MOVE Z-DATE2-CC TO Z-DATE6-CC.
034722     MOVE Z-DATE2-YY TO Z-DATE6-YY.
034724     MOVE Z-DATE6-FORMAT TO RMDRPT-BEG-DATE-3.
034726     MOVE SPACES TO RMDRPT-REMARK2-4.
034728 Z-23-35-ENDIF.
034730     MOVE WS-MD-FMV TO RMDRPT-BAL-BEG-YR-3
034732       , RMDRPT2-BAL-BEG-YR-3.
034734     IF TDB-TDAA-FAIR-MRKT = ZEROS
034736         NEXT SENTENCE ELSE
034738         GO TO Z-23-63-1-ELSE.
034740     MOVE "*" TO RMDRPT-CUR-BAL-IND-3.
034742     GO TO Z-23-63-ENDIF.
034744 Z-23-63-1-ELSE.
034746     MOVE SPACE TO RMDRPT-CUR-BAL-IND-3.
034748 Z-23-63-ENDIF.
034750     MOVE WS-MD-FACT TO RMDRPT-FACTOR-3
034752       , RMDRPT2-FACTOR-3.
034754     MOVE WS-MD-TBL TO RMDRPT-TBL-3.
034756     MOVE WS-MD-AMT TO RMDRPT-MINDIST-3
034758       , RMDRPT2-MINDIST-3.
034760     IF TDB-TDAA-RMD-MAN-CALC = ZERO
034762         NEXT SENTENCE ELSE
034764         GO TO Z-23-69-1-ELSE.
034766     MOVE SPACE TO RMDRPT-RMD-MAN-CALC-3.
034768     GO TO Z-23-69-ENDIF.
034770 Z-23-69-1-ELSE.
034772     MOVE "*" TO RMDRPT-RMD-MAN-CALC-3.
034774 Z-23-69-ENDIF.
034776     MOVE "/" TO RMDRPT-SLASH-3.
034778     MOVE SPACES TO RMDRPT-DS-METH-4
034780       , RMDRPT-WH-MSG-4.
034782     MOVE ZEROS TO WS-NEW-DS-AMT.
034784     IF ( TDB-TDAA-BENEF-CD = 1 ) AND ( TDB-TDAA-BNF-BIRTH-DT =   
034786         ZEROS )
034788         NEXT SENTENCE ELSE
034790         GO TO Z-23-75-1-ELSE.
034792     MOVE "CANNOT USE JOINT LIFE, MISSING SPOUSE BD" TO           
034794         RMDRPT-REMARK-4.
034796     GO TO Z-23-75-ENDIF.
034798 Z-23-75-1-ELSE.
034800     MOVE SPACES TO RMDRPT-REMARK-4.
034802 Z-23-75-ENDIF.
034804     IF ( TDB-TDAA-INHERIT-IRA = 2 ) AND ( TDB-TDAA-RMD-MAN-CALC  
034806         = 0 )
034808         NEXT SENTENCE ELSE
034810         GO TO Z-23-78-1-ELSE.
034812     IF ( TDB-TDAA-BNF-DEATH-DT = 0 ) OR ( TDB-TDAA-BNF-DEATH-DT  
034814         > 20191231 ) OR ( TDB-TDAA-IRA-TYPE = 13 OR 15 OR 17 )
034816         NEXT SENTENCE ELSE
034818         GO TO Z-23-79-1-ELSE.
034820     MOVE "UNABLE TO CALCULATE RMD" TO RMDRPT-REMARK-4.
034822 Z-23-79-1-ELSE.
```

⚠️  This is the source code you must document.
    511 lines from 16897 to 17407.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

