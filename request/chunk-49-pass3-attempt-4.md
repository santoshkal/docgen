# LLM Request Debug File
Generated: 2025-11-18T20:32:44.620367

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 49/55
- **Model**: gpt-4.1
- **Chunk Number**: 49
- **Pass Number**: 3
- **Attempt Number**: 4 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,086 tokens
- **User Prompt**: ~7,434 tokens
- **Total Input**: ~9,520 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 49/55" (ID: detailed-code-explanation)

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


**CHUNK 49 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T18:05:37.383587", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 49 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 23417 to 23893 (477 lines)\nChunk Tokens (estimated): ~8,092\nActual Input Tokens: 9,498 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 23417-23893 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 49 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 49 of 55.\n\n\n=============================================================================\nCHUNK 49 SOURCE CODE (Lines 23417-23893)\n=============================================================================\n\n```cobol\n046842         TDB-TDACUST.\n046844     MOVE TDAC-IRA-INT OF TDACUST TO TDB-TDAC-IRA-INT OF          \n046846         TDB-TDACUST.\n046848     MOVE TDAC-IRA-CONTR OF TDACUST TO TDB-TDAC-IRA-CONTR OF      \n046850         TDB-TDACUST.\n046852     MOVE TDAC-IRA-CONTR-LY OF TDACUST TO TDB-TDAC-IRA-CONTR-LY   \n046854         OF TDB-TDACUST.\n046856     MOVE TDAC-IRA-DISTR OF TDACUST TO TDB-TDAC-IRA-DISTR OF      \n046858         TDB-TDACUST.\n046860     MOVE TDAC-IRA-DISTR-LY OF TDACUST TO TDB-TDAC-IRA-DISTR-LY   \n046862         OF TDB-TDACUST.\n046864     MOVE TDAC-IRA-ROLLOVER OF TDACUST TO TDB-TDAC-IRA-ROLLOVER   \n046866         OF TDB-TDACUST.\n046868     MOVE TDAC-IRA-TRF-IN OF TDACUST TO TDB-TDAC-IRA-TRF-IN OF    \n046870         TDB-TDACUST.\n046872     MOVE TDAC-IRA-TRF-OUT OF TDACUST TO TDB-TDAC-IRA-TRF-OUT OF  \n046874         TDB-TDACUST.\n046876     MOVE TDAC-IRA-FAIR-MKT OF TDACUST TO TDB-TDAC-IRA-FAIR-MKT   \n046878         OF TDB-TDACUST.\n046880     MOVE TDAC-CIF-REMARK OF TDACUST TO TDB-TDAC-CIF-REMARK OF    \n046882         TDB-TDACUST.\n046884     MOVE TDAC-CD-ST-WHLD OF TDACUST TO TDB-TDAC-CD-ST-WHLD OF    \n046886         TDB-TDACUST.\n046888     MOVE TDAC-IRA-ST-WHLD OF TDACUST TO TDB-TDAC-IRA-ST-WHLD OF  \n046890         TDB-TDACUST.\n046892     MOVE 1 TO Z-II.\n046894 Z-14-9-1-LOOP.\n046896     IF Z-II > 12\n046898         GO TO Z-14-9-1-LOOP-XIT.\n046900     MOVE TDAC-CURR-YR-AMT OF TDACUST (Z-II) TO                   \n046902         TDB-TDAC-CURR-YR-AMT OF TDB-TDACUST (Z-II).\n046904     MOVE TDAC-LAST-YR-AMT OF TDACUST (Z-II) TO                   \n046906         TDB-TDAC-LAST-YR-AMT OF TDB-TDACUST (Z-II).\n046908     ADD 1 TO Z-II.\n046910     GO TO Z-14-9-1-LOOP.\n046912 Z-14-9-1-LOOP-XIT.\n046914     MOVE TDAC-TIN-CD-2 OF TDACUST TO TDB-TDAC-TIN-CD-2 OF        \n046916         TDB-TDACUST.\n046918     MOVE TDAC-TIN-CRT-CD-2 OF TDACUST TO TDB-TDAC-TIN-CRT-CD-2   \n046920         OF TDB-TDACUST.\n046922     MOVE TDAC-TIN-CRT-DT-2 OF TDACUST TO TDB-TDAC-TIN-CRT-DT-2   \n046924         OF TDB-TDACUST.\n046926     MOVE TDAC-TIN-NBR-2 OF TDACUST TO TDB-TDAC-TIN-NBR-2 OF      \n046928         TDB-TDACUST.\n046930     MOVE TDAC-TIN-CD-3 OF TDACUST TO TDB-TDAC-TIN-CD-3 OF        \n046932         TDB-TDACUST.\n046934     MOVE TDAC-TIN-CRT-CD-3 OF TDACUST TO TDB-TDAC-TIN-CRT-CD-3   \n046936         OF TDB-TDACUST.\n046938     MOVE TDAC-TIN-CRT-DT-3 OF TDACUST TO TDB-TDAC-TIN-CRT-DT-3   \n046940         OF TDB-TDACUST.\n046942     MOVE TDAC-TIN-NBR-3 OF TDACUST TO TDB-TDAC-TIN-NBR-3 OF      \n046944         TDB-TDACUST.\n046946     MOVE TDAC-NAICS-CD OF TDACUST TO TDB-TDAC-NAICS-CD OF        \n046948         TDB-TDACUST.\n046950     MOVE TDAC-CIF-PASS-THR OF TDACUST TO TDB-TDAC-CIF-PASS-THR   \n046952         OF TDB-TDACUST.\n046954     MOVE TDAC-EMAIL-NTC OF TDACUST TO TDB-TDAC-EMAIL-NTC OF      \n046956         TDB-TDACUST.\n046958     MOVE TDAC-RMD-YR-AMT OF TDACUST TO TDB-TDAC-RMD-YR-AMT OF    \n046960         TDB-TDACUST.\n046962     MOVE TDAC-ADDR-CHG-DT OF TDACUST TO TDB-TDAC-ADDR-CHG-DT OF  \n046964         TDB-TDACUST.\n046966     MOVE TDAC-WTHLD-CD OF TDACUST TO TDB-TDAC-WTHLD-CD OF        \n046968         TDB-TDACUST.\n046970     MOVE TDAC-ST-WHLD-CD OF TDACUST TO TDB-TDAC-ST-WHLD-CD OF    \n046972         TDB-TDACUST.\n046974     MOVE TDAC-WTHLD-AMT OF TDACUST TO TDB-TDAC-WTHLD-AMT OF      \n046976         TDB-TDACUST.\n046978     MOVE TDAC-ST-WHLD-AMT OF TDACUST TO TDB-TDAC-ST-WHLD-AMT OF  \n046980         TDB-TDACUST.\n046982     MOVE TDAC-FOREIGN-LANG OF TDACUST TO TDB-TDAC-FOREIGN-LANG   \n046984         OF TDB-TDACUST.\n046986     MOVE TDAC-L-ROLLOVR-DT OF TDACUST TO TDB-TDAC-L-ROLLOVR-DT   \n046988         OF TDB-TDACUST.\n046990     MOVE TDAC-CUSTM-FIELDS OF TDACUST TO TDB-TDAC-CUSTM-FIELDS   \n046992         OF TDB-TDACUST.\n046994     MOVE TDAC-LLC-NAME OF TDACUST TO TDB-TDAC-LLC-NAME OF        \n046996         TDB-TDACUST.\n046998     MOVE TDAC-LLC-TIN-CD OF TDACUST TO TDB-TDAC-LLC-TIN-CD OF    \n047000         TDB-TDACUST.\n047002     MOVE TDAC-LLC-TIN OF TDACUST TO TDB-TDAC-LLC-TIN OF          \n047004         TDB-TDACUST.\n047006     MOVE TDAC-FOREIGN-PHN OF TDACUST TO TDB-TDAC-FOREIGN-PHN OF  \n047008         TDB-TDACUST.\n047010     MOVE 0350 TO TDB-MESSAGE-NBR.\n047012 Z-14-4-ENDIF.\n047014     GO TO Z-14-2-ENDIF.\n047016 Z-14-2-1-ELSE.\n047018     MOVE 0006 TO TDB-ERROR-NBR.\n047020 Z-14-2-ENDIF.\n047022 Z-14-END.\n047024     IF Z-EDIT-ERROR\n047026         GO TO Z-14-XIT.\n047028 Z-14-SKIP.\n047030     IF Z-EXIT-LEVEL NOT < 0\n047032         MOVE 0 TO Z-EXIT-CODE\n047034         MOVE 9999 TO Z-EXIT-LEVEL.\n047036 Z-14-XIT.\n047038     EXIT.\n047040*\n047042*****************************************************************\n047044*    PROCEDURE TDB-IRAUPD-INQ\n047046*****************************************************************\n047048 Z-15-PROCEDURE.\n047050*\n047052     MOVE 0 TO Z-EXIT-CODE.\n047054     MOVE 9999 TO Z-EXIT-LEVEL.\n047056     IF TDB-READ-INFO = \"01BAT4\"\n047058         NEXT SENTENCE ELSE\n047060         GO TO Z-15-1-1-ELSE.\n047062     MOVE ZERO TO Z-FLINFO12-PRES.\n047064     MOVE 14 TO Z-FLINFO12-LAST-SEQ.\n047066     MOVE ZERO TO Z-FLINFO12-SOME.\n047068 Z-15-2-READ.\n047070     FIND TDAIRA OF LDBTDADB VIA TDAIRASET OF TDAIRA OF LDBTDADB\n047072     AT TDAI-BANK = TDB-TDAI-BANK AND\n047074        TDAI-CUST = TDB-TDAI-CUST AND\n047076        TDAI-ACCT = TDB-TDAI-ACCT\n047078         ON EXCEPTION\n047080         MOVE 14 TO Z-DMS-EXCEPT-SEQ\n047082         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n047084             GO TO Z-15-2-XIT\n047086         ELSE\n047088             MOVE \"TDAIRASET OF TDAIRA OF LDBTDADB\" TO            \n047090                 Z-DMS-EXCEPT-STR\n047092             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n047094             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n047096\n047098 Z-15-2-PRESENT.\n047100*\n047102     MOVE 1 TO Z-FLINFO12-SOME.\n047104     MOVE 1 TO Z-FLINFO12-PRES.\n047106     GO TO Z-15-2-CONT.\n047108 Z-15-2-XIT.\n047110 Z-15-2-CONT.\n047112     IF Z-FLINFO12-ABSENT\n047114         NEXT SENTENCE ELSE\n047116         GO TO Z-15-3-1-ELSE.\n047118     MOVE 0340 TO TDB-ERROR-NBR.\n047120     GO TO Z-15-3-ENDIF.\n047122 Z-15-3-1-ELSE.\n047124     IF TDB-READ-DATE NOT = 0\n047126         NEXT SENTENCE ELSE\n047128         GO TO Z-15-3-2-ELSE.\n047130************ PERFORM TDB-IRA-01BAT4-ACTV-ADJ\n047132     PERFORM Z-33-PROCEDURE THRU Z-33-XIT.\n047134     IF  Z-EXIT-EDITEXIT\n047136         GO TO Z-15-XIT.\n047138     IF  Z-DMS2-ABORT-FLAG = 1\n047140         GO TO Z-15-XIT.\n047142     IF  Z-EXIT-LEVEL < 0\n047144         GO TO Z-15-END.\n047146*\n047148     MOVE HOLD-TDAI-BANK OF HOLD-TDAIRA TO TDB-TDAI-BANK OF       \n047150         TDB-TDAIRA.\n047152     MOVE HOLD-TDAI-BRCH OF HOLD-TDAIRA TO TDB-TDAI-BRCH OF       \n047154         TDB-TDAIRA.\n047156     MOVE HOLD-TDAI-APPL OF HOLD-TDAIRA TO TDB-TDAI-APPL OF       \n047158         TDB-TDAIRA.\n047160     MOVE HOLD-TDAI-CUST OF HOLD-TDAIRA TO TDB-TDAI-CUST OF       \n047162         TDB-TDAIRA.\n047164     MOVE HOLD-TDAI-ACCT OF HOLD-TDAIRA TO TDB-TDAI-ACCT OF       \n047166         TDB-TDAIRA.\n047168     MOVE HOLD-TDAI-PUB-ID OF HOLD-TDAIRA TO TDB-TDAI-PUB-ID OF   \n047170         TDB-TDAIRA.\n047172     MOVE HOLD-TDAI-ADD-DT OF HOLD-TDAIRA TO TDB-TDAI-ADD-DT OF   \n047174         TDB-TDAIRA.\n047176     MOVE HOLD-TDAI-ADD-TM OF HOLD-TDAIRA TO TDB-TDAI-ADD-TM OF   \n047178         TDB-TDAIRA.\n047180     MOVE 1 TO Z-II.\n047182 Z-15-6-1-LOOP.\n047184     IF Z-II > 20\n047186         GO TO Z-15-6-1-LOOP-XIT.\n047188     MOVE HOLD-TDAI-DS-TYPE OF HOLD-TDAIRA (Z-II) TO              \n047190         TDB-TDAI-DS-TYPE OF TDB-TDAIRA (Z-II).\n047192     MOVE HOLD-TDAI-CN-TYPE OF HOLD-TDAIRA (Z-II) TO              \n047194         TDB-TDAI-CN-TYPE OF TDB-TDAIRA (Z-II).\n047196     MOVE HOLD-TDAI-DS-CN-AMT OF HOLD-TDAIRA (Z-II) TO            \n047198         TDB-TDAI-DS-CN-AMT OF TDB-TDAIRA (Z-II).\n047200     MOVE HOLD-TDAI-DS-PEN-AMT OF HOLD-TDAIRA (Z-II) TO           \n047202         TDB-TDAI-DS-PEN-AMT OF TDB-TDAIRA (Z-II).\n047204     MOVE HOLD-TDAI-DS-WTHLD-AMT OF HOLD-TDAIRA (Z-II) TO         \n047206         TDB-TDAI-DS-WTHLD-AMT OF TDB-TDAIRA (Z-II).\n047208     MOVE HOLD-TDAI-DS-ST-WH-AMT OF HOLD-TDAIRA (Z-II) TO         \n047210         TDB-TDAI-DS-ST-WH-AMT OF TDB-TDAIRA (Z-II).\n047212     MOVE HOLD-TDAI-DS-EXC-EARN OF HOLD-TDAIRA (Z-II) TO          \n047214         TDB-TDAI-DS-EXC-EARN OF TDB-TDAIRA (Z-II).\n047216     ADD 1 TO Z-II.\n047218     GO TO Z-15-6-1-LOOP.\n047220 Z-15-6-1-LOOP-XIT.\n047222     MOVE HOLD-TDAI-DS-C-YTD-CNT OF HOLD-TDAIRA TO                \n047224         TDB-TDAI-DS-C-YTD-CNT OF TDB-TDAIRA.\n047226     MOVE HOLD-TDAI-DS-P-YTD-CNT OF HOLD-TDAIRA TO                \n047228         TDB-TDAI-DS-P-YTD-CNT OF TDB-TDAIRA.\n047230     MOVE HOLD-TDAI-DS-AMT-C-YTD OF HOLD-TDAIRA TO                \n047232         TDB-TDAI-DS-AMT-C-YTD OF TDB-TDAIRA.\n047234     MOVE HOLD-TDAI-DS-AMT-P-YTD OF HOLD-TDAIRA TO                \n047236         TDB-TDAI-DS-AMT-P-YTD OF TDB-TDAIRA.\n047238     MOVE HOLD-TDAI-DS-INT-AMT OF HOLD-TDAIRA TO                  \n047240         TDB-TDAI-DS-INT-AMT OF TDB-TDAIRA.\n047242     MOVE HOLD-TDAI-CN-YTD-CNT OF HOLD-TDAIRA TO                  \n047244         TDB-TDAI-CN-YTD-CNT OF TDB-TDAIRA.\n047246     MOVE HOLD-TDAI-CN-YTD-AMT OF HOLD-TDAIRA TO                  \n047248         TDB-TDAI-CN-YTD-AMT OF TDB-TDAIRA.\n047250     MOVE HOLD-TDAI-CN-LYTD-AMT OF HOLD-TDAIRA TO                 \n047252         TDB-TDAI-CN-LYTD-AMT OF TDB-TDAIRA.\n047254     MOVE HOLD-TDAI-EMP-CONT-LYR OF HOLD-TDAIRA TO                \n047256         TDB-TDAI-EMP-CONT-LYR OF TDB-TDAIRA.\n047258     MOVE HOLD-TDAI-REG-CONT-LYR OF HOLD-TDAIRA TO                \n047260         TDB-TDAI-REG-CONT-LYR OF TDB-TDAIRA.\n047262     MOVE HOLD-TDAI-UNINSURED OF HOLD-TDAIRA TO                   \n047264         TDB-TDAI-UNINSURED OF TDB-TDAIRA.\n047266     MOVE HOLD-TDAI-ROLLOVER OF HOLD-TDAIRA TO TDB-TDAI-ROLLOVER  \n047268         OF TDB-TDAIRA.\n047270     MOVE HOLD-TDAI-ROLLOVER-LYR OF HOLD-TDAIRA TO                \n047272         TDB-TDAI-ROLLOVER-LYR OF TDB-TDAIRA.\n047274     MOVE HOLD-TDAI-TRANSFER-IN OF HOLD-TDAIRA TO                 \n047276         TDB-TDAI-TRANSFER-IN OF TDB-TDAIRA.\n047278     MOVE HOLD-TDAI-TRANSFER-OUT OF HOLD-TDAIRA TO                \n047280         TDB-TDAI-TRANSFER-OUT OF TDB-TDAIRA.\n047282     MOVE HOLD-TDAI-1ST-CN-DATE OF HOLD-TDAIRA TO                 \n047284         TDB-TDAI-1ST-CN-DATE OF TDB-TDAIRA.\n047286     MOVE HOLD-TDAI-BASIS-C-LTD OF HOLD-TDAIRA TO                 \n047288         TDB-TDAI-BASIS-C-LTD OF TDB-TDAIRA.\n047290     MOVE HOLD-TDAI-BASIS-D-LTD OF HOLD-TDAIRA TO                 \n047292         TDB-TDAI-BASIS-D-LTD OF TDB-TDAIRA.\n047294     MOVE HOLD-TDAI-BASIS-D-YTD OF HOLD-TDAIRA TO                 \n047296         TDB-TDAI-BASIS-D-YTD OF TDB-TDAIRA.\n047298     MOVE HOLD-TDAI-CN-TYPE-EX OF HOLD-TDAIRA TO                  \n047300         TDB-TDAI-CN-TYPE-EX OF TDB-TDAIRA.\n047302     MOVE HOLD-TDAI-DS-TYPE-EX-1 OF HOLD-TDAIRA TO                \n047304         TDB-TDAI-DS-TYPE-EX-1 OF TDB-TDAIRA.\n047306     MOVE HOLD-TDAI-DS-TYPE-EX-2 OF HOLD-TDAIRA TO                \n047308         TDB-TDAI-DS-TYPE-EX-2 OF TDB-TDAIRA.\n047310     MOVE 0350 TO TDB-MESSAGE-NBR.\n047312     GO TO Z-15-3-ENDIF.\n047314 Z-15-3-2-ELSE.\n047316     MOVE TDAI-BANK OF TDAIRA TO TDB-TDAI-BANK OF TDB-TDAIRA.\n047318     MOVE TDAI-BRCH OF TDAIRA TO TDB-TDAI-BRCH OF TDB-TDAIRA.\n047320     MOVE TDAI-CUST OF TDAIRA TO TDB-TDAI-CUST OF TDB-TDAIRA.\n047322     MOVE TDAI-ACCT OF TDAIRA TO TDB-TDAI-ACCT OF TDB-TDAIRA.\n047324     MOVE TDAI-PUB-ID OF TDAIRA TO TDB-TDAI-PUB-ID OF TDB-TDAIRA.\n047326     MOVE TDAI-ADD-DT OF TDAIRA TO TDB-TDAI-ADD-DT OF TDB-TDAIRA.\n047328     MOVE TDAI-ADD-TM OF TDAIRA TO TDB-TDAI-ADD-TM OF TDB-TDAIRA.\n047330     MOVE 1 TO Z-II.\n047332 Z-15-8-1-LOOP.\n047334     IF Z-II > 20\n047336         GO TO Z-15-8-1-LOOP-XIT.\n047338     MOVE TDAI-DS-TYPE OF TDAIRA (Z-II) TO TDB-TDAI-DS-TYPE OF    \n047340         TDB-TDAIRA (Z-II).\n047342     MOVE TDAI-CN-TYPE OF TDAIRA (Z-II) TO TDB-TDAI-CN-TYPE OF    \n047344         TDB-TDAIRA (Z-II).\n047346     MOVE TDAI-DS-CN-AMT OF TDAIRA (Z-II) TO TDB-TDAI-DS-CN-AMT   \n047348         OF TDB-TDAIRA (Z-II).\n047350     MOVE TDAI-DS-PEN-AMT OF TDAIRA (Z-II) TO TDB-TDAI-DS-PEN-AMT \n047352         OF TDB-TDAIRA (Z-II).\n047354     MOVE TDAI-DS-WTHLD-AMT OF TDAIRA (Z-II) TO                   \n047356         TDB-TDAI-DS-WTHLD-AMT OF TDB-TDAIRA (Z-II).\n047358     MOVE TDAI-DS-ST-WH-AMT OF TDAIRA (Z-II) TO                   \n047360         TDB-TDAI-DS-ST-WH-AMT OF TDB-TDAIRA (Z-II).\n047362     MOVE TDAI-DS-EXC-EARN OF TDAIRA (Z-II) TO                    \n047364         TDB-TDAI-DS-EXC-EARN OF TDB-TDAIRA (Z-II).\n047366     ADD 1 TO Z-II.\n047368     GO TO Z-15-8-1-LOOP.\n047370 Z-15-8-1-LOOP-XIT.\n047372     MOVE TDAI-DS-C-YTD-CNT OF TDAIRA TO TDB-TDAI-DS-C-YTD-CNT OF \n047374         TDB-TDAIRA.\n047376     MOVE TDAI-DS-P-YTD-CNT OF TDAIRA TO TDB-TDAI-DS-P-YTD-CNT OF \n047378         TDB-TDAIRA.\n047380     MOVE TDAI-DS-AMT-C-YTD OF TDAIRA TO TDB-TDAI-DS-AMT-C-YTD OF \n047382         TDB-TDAIRA.\n047384     MOVE TDAI-DS-AMT-P-YTD OF TDAIRA TO TDB-TDAI-DS-AMT-P-YTD OF \n047386         TDB-TDAIRA.\n047388     MOVE TDAI-DS-INT-AMT OF TDAIRA TO TDB-TDAI-DS-INT-AMT OF     \n047390         TDB-TDAIRA.\n047392     MOVE TDAI-CN-YTD-CNT OF TDAIRA TO TDB-TDAI-CN-YTD-CNT OF     \n047394         TDB-TDAIRA.\n047396     MOVE TDAI-CN-YTD-AMT OF TDAIRA TO TDB-TDAI-CN-YTD-AMT OF     \n047398         TDB-TDAIRA.\n047400     MOVE TDAI-CN-LYTD-AMT OF TDAIRA TO TDB-TDAI-CN-LYTD-AMT OF   \n047402         TDB-TDAIRA.\n047404     MOVE TDAI-EMP-CONT-LYR OF TDAIRA TO TDB-TDAI-EMP-CONT-LYR OF \n047406         TDB-TDAIRA.\n047408     MOVE TDAI-REG-CONT-LYR OF TDAIRA TO TDB-TDAI-REG-CONT-LYR OF \n047410         TDB-TDAIRA.\n047412     MOVE TDAI-UNINSURED OF TDAIRA TO TDB-TDAI-UNINSURED OF       \n047414         TDB-TDAIRA.\n047416     MOVE TDAI-ROLLOVER OF TDAIRA TO TDB-TDAI-ROLLOVER OF         \n047418         TDB-TDAIRA.\n047420     MOVE TDAI-ROLLOVER-LYR OF TDAIRA TO TDB-TDAI-ROLLOVER-LYR OF \n047422         TDB-TDAIRA.\n047424     MOVE TDAI-TRANSFER-IN OF TDAIRA TO TDB-TDAI-TRANSFER-IN OF   \n047426         TDB-TDAIRA.\n047428     MOVE TDAI-TRANSFER-OUT OF TDAIRA TO TDB-TDAI-TRANSFER-OUT OF \n047430         TDB-TDAIRA.\n047432     MOVE TDAI-1ST-CN-DATE OF TDAIRA TO TDB-TDAI-1ST-CN-DATE OF   \n047434         TDB-TDAIRA.\n047436     MOVE TDAI-BASIS-C-LTD OF TDAIRA TO TDB-TDAI-BASIS-C-LTD OF   \n047438         TDB-TDAIRA.\n047440     MOVE TDAI-BASIS-D-LTD OF TDAIRA TO TDB-TDAI-BASIS-D-LTD OF   \n047442         TDB-TDAIRA.\n047444     MOVE TDAI-BASIS-D-YTD OF TDAIRA TO TDB-TDAI-BASIS-D-YTD OF   \n047446         TDB-TDAIRA.\n047448     MOVE 0350 TO TDB-MESSAGE-NBR.\n047450 Z-15-3-ENDIF.\n047452     GO TO Z-15-1-ENDIF.\n047454 Z-15-1-1-ELSE.\n047456     MOVE 3461 TO TDB-ERROR-NBR.\n047458 Z-15-1-ENDIF.\n047460 Z-15-END.\n047462     IF Z-EDIT-ERROR\n047464         GO TO Z-15-XIT.\n047466 Z-15-SKIP.\n047468     IF Z-EXIT-LEVEL NOT < 0\n047470         MOVE 0 TO Z-EXIT-CODE\n047472         MOVE 9999 TO Z-EXIT-LEVEL.\n047474 Z-15-XIT.\n047476     EXIT.\n047478*\n047480*****************************************************************\n047482*    PROCEDURE TDD-MINDIST-SETUP-AND-CALC\n047484*****************************************************************\n047486 Z-28-PROCEDURE.\n047488*\n047490     MOVE 0 TO Z-EXIT-CODE.\n047492     MOVE 9999 TO Z-EXIT-LEVEL.\n047494     IF ( TDB-TDAA-INHERIT-IRA = 2 ) AND ( TDB-TDAA-BNF-DEATH-DT  \n047496         NOT = ZEROS )\n047498         NEXT SENTENCE ELSE\n047500         GO TO Z-28-1-1-ELSE.\n047502*\n047504     PERFORM Z-DATE-INITIALIZE-REGS\n047506         THRU Z-DATE-INITIALIZE-REGS-EXIT.\n047508     PERFORM Z-DATE-INITIALIZE-CTRL\n047510        THRU Z-DATE-INITIALIZE-CTRL-EXIT.\n047512     MOVE TDB-TDAA-BNF-DEATH-DT TO Z-DATE2-FORMAT-9.\n047514*    DATE UNIT INITIALIZATION\n047516     COMPUTE Z-DATE-Y = 1.\n047518*    LOAD DATE REGISTERS FOR CALCULATIONS\n047520*    LOAD DATE REGISTER 1\n047522     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n047524     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n047526     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n047528     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n047530     PERFORM Z-DATE-CALC-LEAP-YEAR\n047532        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n047534     PERFORM Z-DATE-MDY-TO-JUL-CTRL\n047536        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.\n047538     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.\n047540*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS\n047542     IF Z-DATE-Y NOT = ZEROS\n047544         PERFORM Z-DATE-CALC-Y\n047546            THRU Z-DATE-CALC-Y-EXIT.\n047548     IF Z-DATE-C NOT = ZEROS\n047550         PERFORM Z-DATE-CALC-C\n047552            THRU Z-DATE-CALC-C-EXIT.\n047554*    RE-ADJUST AFTER CALCULATIONS\n047556     PERFORM Z-DATE-CALC-LEAP-YEAR\n047558        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.\n047560     PERFORM Z-DATE-CALC-MONTH-DAYS\n047562        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.\n047564*    PLACE THE RESULTS WHERE THEY BELONG\n047566     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.\n047568     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.\n047570     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.\n047572     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.\n047574     MOVE Z-DATE2-FORMAT-9 TO WS-CUST-YAD.\n047576     PERFORM Z-DATE-INITIALIZE-CTRL\n047578        THRU Z-DATE-INITIALIZE-CTRL-EXIT.\n047580     MOVE WS-CUST-YAD TO Z-DATE2-FORMAT-9.\n047582*    LOAD DATE REGISTER 1\n047584     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n047586     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n047588     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n047590     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n047592     MOVE Z-DATE-1 TO Z-DATE-2.\n047594     MOVE TDB-TDAC-BIRTH-DT TO Z-DATE2-FORMAT-9.\n047596*    LOAD DATE REGISTER 1\n047598     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n047600     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n047602     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n047604     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n047606     PERFORM Z-DATE-YY-DIFF THRU Z-DATE-YY-DIFF-EXIT.\n047608     MOVE Z-DATE-Y TO WS-MD-BN-AGE.\n047610     PERFORM Z-DATE-INITIALIZE-CTRL\n047612        THRU Z-DATE-INITIALIZE-CTRL-EXIT.\n047614     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.\n047616*    LOAD DATE REGISTER 1\n047618     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n047620     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n047622     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n047624     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n047626     MOVE Z-DATE-1 TO Z-DATE-2.\n047628     MOVE WS-CUST-YAD TO Z-DATE2-FORMAT-9.\n047630*    LOAD DATE REGISTER 1\n047632     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n047634     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n047636     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n047638     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n047640     PERFORM Z-DATE-YY-DIFF THRU Z-DATE-YY-DIFF-EXIT.\n047642     MOVE Z-DATE-Y TO WS-NUM-YR-YAD.\n047644 Z-28-1-1-ELSE.\n047646     IF ( TDB-TDAA-BENEF-CD = 1 ) AND ( TDB-TDAA-BNF-BIRTH-DT NOT \n047648         = ZEROS )\n047650         NEXT SENTENCE ELSE\n047652         GO TO Z-28-5-1-ELSE.\n047654     PERFORM Z-DATE-INITIALIZE-CTRL\n047656        THRU Z-DATE-INITIALIZE-CTRL-EXIT.\n047658     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.\n047660*    LOAD DATE REGISTER 1\n047662     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n047664     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n047666     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n047668     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n047670     MOVE Z-DATE-1 TO Z-DATE-2.\n047672     MOVE TDB-TDAA-BNF-BIRTH-DT TO Z-DATE2-FORMAT-9.\n047674*    LOAD DATE REGISTER 1\n047676     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.\n047678     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.\n047680     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.\n047682     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.\n047684     PERFORM Z-DATE-YY-DIFF THRU Z-DATE-YY-DIFF-EXIT.\n047686     MOVE Z-DATE-Y TO WS-MD-BN-AGE.\n047688     MOVE TDB-TDAA-BENEF-CD TO WS-MD-SPOUSE.\n047690 Z-28-5-1-ELSE.\n047692     COMPUTE WS-MD-FMV = TDB-TDAA-FAIR-MRKT .\n047694\n047696********* COMPUTE WHEN\n047698     IF TDB-TDAA-FAIR-MRKT = ZEROS\n047700        NEXT SENTENCE\n047702     ELSE\n047704        GO TO Z-28-9-COMPUTE-SKIP.\n047706     COMPUTE WS-MD-FMV = TDB-TDAA-CURR-BAL .\n047708\n047710 Z-28-9-COMPUTE-SKIP.\n047712     IF TDB-TDAA-RMD-MAN-CALC = ZERO\n047714         NEXT SENTENCE ELSE\n047716         GO TO Z-28-10-1-ELSE.\n047718************ PERFORM CALC-MINDIST-AMT\n047720     PERFORM Z-34-PROCEDURE THRU Z-34-XIT.\n047722     IF  Z-EXIT-EDITEXIT\n047724         GO TO Z-28-XIT.\n047726     IF  Z-DMS2-ABORT-FLAG = 1\n047728         GO TO Z-28-XIT.\n047730     IF  Z-EXIT-LEVEL < 0\n047732         GO TO Z-28-END.\n047734*\n047736     GO TO Z-28-10-ENDIF.\n047738 Z-28-10-1-ELSE.\n047740     MOVE TDB-TDAA-RMD-AMOUNT TO WS-MD-AMT.\n047742     MOVE TDB-TDAA-LIFE-FACTOR TO WS-MD-FACT.\n047744 Z-28-10-ENDIF.\n047746 Z-28-END.\n047748     IF Z-EDIT-ERROR\n047750         GO TO Z-28-XIT.\n047752 Z-28-SKIP.\n047754     IF Z-EXIT-LEVEL NOT < 0\n047756         MOVE 0 TO Z-EXIT-CODE\n047758         MOVE 9999 TO Z-EXIT-LEVEL.\n047760 Z-28-XIT.\n047762     EXIT.\n047764*\n047766*****************************************************************\n047768*    PROCEDURE TDB-CUST-01BAT2-ACTV-ADJ\n047770*****************************************************************\n047772 Z-32-PROCEDURE.\n047774*\n047776     MOVE TDAC-BANK OF TDACUST TO HOLD-TDAC-BANK OF HOLD-TDACUST.\n047778     MOVE TDAC-CUST OF TDACUST TO HOLD-TDAC-CUST OF HOLD-TDACUST.\n047780     MOVE TDAC-BRCH OF TDACUST TO HOLD-TDAC-BRCH OF HOLD-TDACUST.\n047782     MOVE TDAC-STATUS OF TDACUST TO HOLD-TDAC-STATUS OF           \n047784         HOLD-TDACUST.\n047786     MOVE TDAC-NAME-1 OF TDACUST TO HOLD-TDAC-NAME-1 OF           \n047788         HOLD-TDACUST.\n047790     MOVE TDAC-N1-KEY OF TDACUST TO HOLD-TDAC-N1-KEY OF           \n047792         HOLD-TDACUST.\n047794     MOVE TDAC-N1-FIRST OF TDACUST TO HOLD-TDAC-N1-FIRST OF       \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    477 lines from 23417 to 23893.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 49, "total_chunks": 55, "start_line": 23417, "end_line": 23893, "line_count": 477}

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
- Source code length: 26568 characters

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
CHUNK 49 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 23417 to 23893 (477 lines)
Chunk Tokens (estimated): ~8,092
Actual Input Tokens: 9,498 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 23417-23893 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 49 of 55 chunks
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
      The source code below is only CHUNK 49 of 55.


=============================================================================
CHUNK 49 SOURCE CODE (Lines 23417-23893)
=============================================================================

```cobol
046842         TDB-TDACUST.
046844     MOVE TDAC-IRA-INT OF TDACUST TO TDB-TDAC-IRA-INT OF          
046846         TDB-TDACUST.
046848     MOVE TDAC-IRA-CONTR OF TDACUST TO TDB-TDAC-IRA-CONTR OF      
046850         TDB-TDACUST.
046852     MOVE TDAC-IRA-CONTR-LY OF TDACUST TO TDB-TDAC-IRA-CONTR-LY   
046854         OF TDB-TDACUST.
046856     MOVE TDAC-IRA-DISTR OF TDACUST TO TDB-TDAC-IRA-DISTR OF      
046858         TDB-TDACUST.
046860     MOVE TDAC-IRA-DISTR-LY OF TDACUST TO TDB-TDAC-IRA-DISTR-LY   
046862         OF TDB-TDACUST.
046864     MOVE TDAC-IRA-ROLLOVER OF TDACUST TO TDB-TDAC-IRA-ROLLOVER   
046866         OF TDB-TDACUST.
046868     MOVE TDAC-IRA-TRF-IN OF TDACUST TO TDB-TDAC-IRA-TRF-IN OF    
046870         TDB-TDACUST.
046872     MOVE TDAC-IRA-TRF-OUT OF TDACUST TO TDB-TDAC-IRA-TRF-OUT OF  
046874         TDB-TDACUST.
046876     MOVE TDAC-IRA-FAIR-MKT OF TDACUST TO TDB-TDAC-IRA-FAIR-MKT   
046878         OF TDB-TDACUST.
046880     MOVE TDAC-CIF-REMARK OF TDACUST TO TDB-TDAC-CIF-REMARK OF    
046882         TDB-TDACUST.
046884     MOVE TDAC-CD-ST-WHLD OF TDACUST TO TDB-TDAC-CD-ST-WHLD OF    
046886         TDB-TDACUST.
046888     MOVE TDAC-IRA-ST-WHLD OF TDACUST TO TDB-TDAC-IRA-ST-WHLD OF  
046890         TDB-TDACUST.
046892     MOVE 1 TO Z-II.
046894 Z-14-9-1-LOOP.
046896     IF Z-II > 12
046898         GO TO Z-14-9-1-LOOP-XIT.
046900     MOVE TDAC-CURR-YR-AMT OF TDACUST (Z-II) TO                   
046902         TDB-TDAC-CURR-YR-AMT OF TDB-TDACUST (Z-II).
046904     MOVE TDAC-LAST-YR-AMT OF TDACUST (Z-II) TO                   
046906         TDB-TDAC-LAST-YR-AMT OF TDB-TDACUST (Z-II).
046908     ADD 1 TO Z-II.
046910     GO TO Z-14-9-1-LOOP.
046912 Z-14-9-1-LOOP-XIT.
046914     MOVE TDAC-TIN-CD-2 OF TDACUST TO TDB-TDAC-TIN-CD-2 OF        
046916         TDB-TDACUST.
046918     MOVE TDAC-TIN-CRT-CD-2 OF TDACUST TO TDB-TDAC-TIN-CRT-CD-2   
046920         OF TDB-TDACUST.
046922     MOVE TDAC-TIN-CRT-DT-2 OF TDACUST TO TDB-TDAC-TIN-CRT-DT-2   
046924         OF TDB-TDACUST.
046926     MOVE TDAC-TIN-NBR-2 OF TDACUST TO TDB-TDAC-TIN-NBR-2 OF      
046928         TDB-TDACUST.
046930     MOVE TDAC-TIN-CD-3 OF TDACUST TO TDB-TDAC-TIN-CD-3 OF        
046932         TDB-TDACUST.
046934     MOVE TDAC-TIN-CRT-CD-3 OF TDACUST TO TDB-TDAC-TIN-CRT-CD-3   
046936         OF TDB-TDACUST.
046938     MOVE TDAC-TIN-CRT-DT-3 OF TDACUST TO TDB-TDAC-TIN-CRT-DT-3   
046940         OF TDB-TDACUST.
046942     MOVE TDAC-TIN-NBR-3 OF TDACUST TO TDB-TDAC-TIN-NBR-3 OF      
046944         TDB-TDACUST.
046946     MOVE TDAC-NAICS-CD OF TDACUST TO TDB-TDAC-NAICS-CD OF        
046948         TDB-TDACUST.
046950     MOVE TDAC-CIF-PASS-THR OF TDACUST TO TDB-TDAC-CIF-PASS-THR   
046952         OF TDB-TDACUST.
046954     MOVE TDAC-EMAIL-NTC OF TDACUST TO TDB-TDAC-EMAIL-NTC OF      
046956         TDB-TDACUST.
046958     MOVE TDAC-RMD-YR-AMT OF TDACUST TO TDB-TDAC-RMD-YR-AMT OF    
046960         TDB-TDACUST.
046962     MOVE TDAC-ADDR-CHG-DT OF TDACUST TO TDB-TDAC-ADDR-CHG-DT OF  
046964         TDB-TDACUST.
046966     MOVE TDAC-WTHLD-CD OF TDACUST TO TDB-TDAC-WTHLD-CD OF        
046968         TDB-TDACUST.
046970     MOVE TDAC-ST-WHLD-CD OF TDACUST TO TDB-TDAC-ST-WHLD-CD OF    
046972         TDB-TDACUST.
046974     MOVE TDAC-WTHLD-AMT OF TDACUST TO TDB-TDAC-WTHLD-AMT OF      
046976         TDB-TDACUST.
046978     MOVE TDAC-ST-WHLD-AMT OF TDACUST TO TDB-TDAC-ST-WHLD-AMT OF  
046980         TDB-TDACUST.
046982     MOVE TDAC-FOREIGN-LANG OF TDACUST TO TDB-TDAC-FOREIGN-LANG   
046984         OF TDB-TDACUST.
046986     MOVE TDAC-L-ROLLOVR-DT OF TDACUST TO TDB-TDAC-L-ROLLOVR-DT   
046988         OF TDB-TDACUST.
046990     MOVE TDAC-CUSTM-FIELDS OF TDACUST TO TDB-TDAC-CUSTM-FIELDS   
046992         OF TDB-TDACUST.
046994     MOVE TDAC-LLC-NAME OF TDACUST TO TDB-TDAC-LLC-NAME OF        
046996         TDB-TDACUST.
046998     MOVE TDAC-LLC-TIN-CD OF TDACUST TO TDB-TDAC-LLC-TIN-CD OF    
047000         TDB-TDACUST.
047002     MOVE TDAC-LLC-TIN OF TDACUST TO TDB-TDAC-LLC-TIN OF          
047004         TDB-TDACUST.
047006     MOVE TDAC-FOREIGN-PHN OF TDACUST TO TDB-TDAC-FOREIGN-PHN OF  
047008         TDB-TDACUST.
047010     MOVE 0350 TO TDB-MESSAGE-NBR.
047012 Z-14-4-ENDIF.
047014     GO TO Z-14-2-ENDIF.
047016 Z-14-2-1-ELSE.
047018     MOVE 0006 TO TDB-ERROR-NBR.
047020 Z-14-2-ENDIF.
047022 Z-14-END.
047024     IF Z-EDIT-ERROR
047026         GO TO Z-14-XIT.
047028 Z-14-SKIP.
047030     IF Z-EXIT-LEVEL NOT < 0
047032         MOVE 0 TO Z-EXIT-CODE
047034         MOVE 9999 TO Z-EXIT-LEVEL.
047036 Z-14-XIT.
047038     EXIT.
047040*
047042*****************************************************************
047044*    PROCEDURE TDB-IRAUPD-INQ
047046*****************************************************************
047048 Z-15-PROCEDURE.
047050*
047052     MOVE 0 TO Z-EXIT-CODE.
047054     MOVE 9999 TO Z-EXIT-LEVEL.
047056     IF TDB-READ-INFO = "01BAT4"
047058         NEXT SENTENCE ELSE
047060         GO TO Z-15-1-1-ELSE.
047062     MOVE ZERO TO Z-FLINFO12-PRES.
047064     MOVE 14 TO Z-FLINFO12-LAST-SEQ.
047066     MOVE ZERO TO Z-FLINFO12-SOME.
047068 Z-15-2-READ.
047070     FIND TDAIRA OF LDBTDADB VIA TDAIRASET OF TDAIRA OF LDBTDADB
047072     AT TDAI-BANK = TDB-TDAI-BANK AND
047074        TDAI-CUST = TDB-TDAI-CUST AND
047076        TDAI-ACCT = TDB-TDAI-ACCT
047078         ON EXCEPTION
047080         MOVE 14 TO Z-DMS-EXCEPT-SEQ
047082         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
047084             GO TO Z-15-2-XIT
047086         ELSE
047088             MOVE "TDAIRASET OF TDAIRA OF LDBTDADB" TO            
047090                 Z-DMS-EXCEPT-STR
047092             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
047094             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
047096
047098 Z-15-2-PRESENT.
047100*
047102     MOVE 1 TO Z-FLINFO12-SOME.
047104     MOVE 1 TO Z-FLINFO12-PRES.
047106     GO TO Z-15-2-CONT.
047108 Z-15-2-XIT.
047110 Z-15-2-CONT.
047112     IF Z-FLINFO12-ABSENT
047114         NEXT SENTENCE ELSE
047116         GO TO Z-15-3-1-ELSE.
047118     MOVE 0340 TO TDB-ERROR-NBR.
047120     GO TO Z-15-3-ENDIF.
047122 Z-15-3-1-ELSE.
047124     IF TDB-READ-DATE NOT = 0
047126         NEXT SENTENCE ELSE
047128         GO TO Z-15-3-2-ELSE.
047130************ PERFORM TDB-IRA-01BAT4-ACTV-ADJ
047132     PERFORM Z-33-PROCEDURE THRU Z-33-XIT.
047134     IF  Z-EXIT-EDITEXIT
047136         GO TO Z-15-XIT.
047138     IF  Z-DMS2-ABORT-FLAG = 1
047140         GO TO Z-15-XIT.
047142     IF  Z-EXIT-LEVEL < 0
047144         GO TO Z-15-END.
047146*
047148     MOVE HOLD-TDAI-BANK OF HOLD-TDAIRA TO TDB-TDAI-BANK OF       
047150         TDB-TDAIRA.
047152     MOVE HOLD-TDAI-BRCH OF HOLD-TDAIRA TO TDB-TDAI-BRCH OF       
047154         TDB-TDAIRA.
047156     MOVE HOLD-TDAI-APPL OF HOLD-TDAIRA TO TDB-TDAI-APPL OF       
047158         TDB-TDAIRA.
047160     MOVE HOLD-TDAI-CUST OF HOLD-TDAIRA TO TDB-TDAI-CUST OF       
047162         TDB-TDAIRA.
047164     MOVE HOLD-TDAI-ACCT OF HOLD-TDAIRA TO TDB-TDAI-ACCT OF       
047166         TDB-TDAIRA.
047168     MOVE HOLD-TDAI-PUB-ID OF HOLD-TDAIRA TO TDB-TDAI-PUB-ID OF   
047170         TDB-TDAIRA.
047172     MOVE HOLD-TDAI-ADD-DT OF HOLD-TDAIRA TO TDB-TDAI-ADD-DT OF   
047174         TDB-TDAIRA.
047176     MOVE HOLD-TDAI-ADD-TM OF HOLD-TDAIRA TO TDB-TDAI-ADD-TM OF   
047178         TDB-TDAIRA.
047180     MOVE 1 TO Z-II.
047182 Z-15-6-1-LOOP.
047184     IF Z-II > 20
047186         GO TO Z-15-6-1-LOOP-XIT.
047188     MOVE HOLD-TDAI-DS-TYPE OF HOLD-TDAIRA (Z-II) TO              
047190         TDB-TDAI-DS-TYPE OF TDB-TDAIRA (Z-II).
047192     MOVE HOLD-TDAI-CN-TYPE OF HOLD-TDAIRA (Z-II) TO              
047194         TDB-TDAI-CN-TYPE OF TDB-TDAIRA (Z-II).
047196     MOVE HOLD-TDAI-DS-CN-AMT OF HOLD-TDAIRA (Z-II) TO            
047198         TDB-TDAI-DS-CN-AMT OF TDB-TDAIRA (Z-II).
047200     MOVE HOLD-TDAI-DS-PEN-AMT OF HOLD-TDAIRA (Z-II) TO           
047202         TDB-TDAI-DS-PEN-AMT OF TDB-TDAIRA (Z-II).
047204     MOVE HOLD-TDAI-DS-WTHLD-AMT OF HOLD-TDAIRA (Z-II) TO         
047206         TDB-TDAI-DS-WTHLD-AMT OF TDB-TDAIRA (Z-II).
047208     MOVE HOLD-TDAI-DS-ST-WH-AMT OF HOLD-TDAIRA (Z-II) TO         
047210         TDB-TDAI-DS-ST-WH-AMT OF TDB-TDAIRA (Z-II).
047212     MOVE HOLD-TDAI-DS-EXC-EARN OF HOLD-TDAIRA (Z-II) TO          
047214         TDB-TDAI-DS-EXC-EARN OF TDB-TDAIRA (Z-II).
047216     ADD 1 TO Z-II.
047218     GO TO Z-15-6-1-LOOP.
047220 Z-15-6-1-LOOP-XIT.
047222     MOVE HOLD-TDAI-DS-C-YTD-CNT OF HOLD-TDAIRA TO                
047224         TDB-TDAI-DS-C-YTD-CNT OF TDB-TDAIRA.
047226     MOVE HOLD-TDAI-DS-P-YTD-CNT OF HOLD-TDAIRA TO                
047228         TDB-TDAI-DS-P-YTD-CNT OF TDB-TDAIRA.
047230     MOVE HOLD-TDAI-DS-AMT-C-YTD OF HOLD-TDAIRA TO                
047232         TDB-TDAI-DS-AMT-C-YTD OF TDB-TDAIRA.
047234     MOVE HOLD-TDAI-DS-AMT-P-YTD OF HOLD-TDAIRA TO                
047236         TDB-TDAI-DS-AMT-P-YTD OF TDB-TDAIRA.
047238     MOVE HOLD-TDAI-DS-INT-AMT OF HOLD-TDAIRA TO                  
047240         TDB-TDAI-DS-INT-AMT OF TDB-TDAIRA.
047242     MOVE HOLD-TDAI-CN-YTD-CNT OF HOLD-TDAIRA TO                  
047244         TDB-TDAI-CN-YTD-CNT OF TDB-TDAIRA.
047246     MOVE HOLD-TDAI-CN-YTD-AMT OF HOLD-TDAIRA TO                  
047248         TDB-TDAI-CN-YTD-AMT OF TDB-TDAIRA.
047250     MOVE HOLD-TDAI-CN-LYTD-AMT OF HOLD-TDAIRA TO                 
047252         TDB-TDAI-CN-LYTD-AMT OF TDB-TDAIRA.
047254     MOVE HOLD-TDAI-EMP-CONT-LYR OF HOLD-TDAIRA TO                
047256         TDB-TDAI-EMP-CONT-LYR OF TDB-TDAIRA.
047258     MOVE HOLD-TDAI-REG-CONT-LYR OF HOLD-TDAIRA TO                
047260         TDB-TDAI-REG-CONT-LYR OF TDB-TDAIRA.
047262     MOVE HOLD-TDAI-UNINSURED OF HOLD-TDAIRA TO                   
047264         TDB-TDAI-UNINSURED OF TDB-TDAIRA.
047266     MOVE HOLD-TDAI-ROLLOVER OF HOLD-TDAIRA TO TDB-TDAI-ROLLOVER  
047268         OF TDB-TDAIRA.
047270     MOVE HOLD-TDAI-ROLLOVER-LYR OF HOLD-TDAIRA TO                
047272         TDB-TDAI-ROLLOVER-LYR OF TDB-TDAIRA.
047274     MOVE HOLD-TDAI-TRANSFER-IN OF HOLD-TDAIRA TO                 
047276         TDB-TDAI-TRANSFER-IN OF TDB-TDAIRA.
047278     MOVE HOLD-TDAI-TRANSFER-OUT OF HOLD-TDAIRA TO                
047280         TDB-TDAI-TRANSFER-OUT OF TDB-TDAIRA.
047282     MOVE HOLD-TDAI-1ST-CN-DATE OF HOLD-TDAIRA TO                 
047284         TDB-TDAI-1ST-CN-DATE OF TDB-TDAIRA.
047286     MOVE HOLD-TDAI-BASIS-C-LTD OF HOLD-TDAIRA TO                 
047288         TDB-TDAI-BASIS-C-LTD OF TDB-TDAIRA.
047290     MOVE HOLD-TDAI-BASIS-D-LTD OF HOLD-TDAIRA TO                 
047292         TDB-TDAI-BASIS-D-LTD OF TDB-TDAIRA.
047294     MOVE HOLD-TDAI-BASIS-D-YTD OF HOLD-TDAIRA TO                 
047296         TDB-TDAI-BASIS-D-YTD OF TDB-TDAIRA.
047298     MOVE HOLD-TDAI-CN-TYPE-EX OF HOLD-TDAIRA TO                  
047300         TDB-TDAI-CN-TYPE-EX OF TDB-TDAIRA.
047302     MOVE HOLD-TDAI-DS-TYPE-EX-1 OF HOLD-TDAIRA TO                
047304         TDB-TDAI-DS-TYPE-EX-1 OF TDB-TDAIRA.
047306     MOVE HOLD-TDAI-DS-TYPE-EX-2 OF HOLD-TDAIRA TO                
047308         TDB-TDAI-DS-TYPE-EX-2 OF TDB-TDAIRA.
047310     MOVE 0350 TO TDB-MESSAGE-NBR.
047312     GO TO Z-15-3-ENDIF.
047314 Z-15-3-2-ELSE.
047316     MOVE TDAI-BANK OF TDAIRA TO TDB-TDAI-BANK OF TDB-TDAIRA.
047318     MOVE TDAI-BRCH OF TDAIRA TO TDB-TDAI-BRCH OF TDB-TDAIRA.
047320     MOVE TDAI-CUST OF TDAIRA TO TDB-TDAI-CUST OF TDB-TDAIRA.
047322     MOVE TDAI-ACCT OF TDAIRA TO TDB-TDAI-ACCT OF TDB-TDAIRA.
047324     MOVE TDAI-PUB-ID OF TDAIRA TO TDB-TDAI-PUB-ID OF TDB-TDAIRA.
047326     MOVE TDAI-ADD-DT OF TDAIRA TO TDB-TDAI-ADD-DT OF TDB-TDAIRA.
047328     MOVE TDAI-ADD-TM OF TDAIRA TO TDB-TDAI-ADD-TM OF TDB-TDAIRA.
047330     MOVE 1 TO Z-II.
047332 Z-15-8-1-LOOP.
047334     IF Z-II > 20
047336         GO TO Z-15-8-1-LOOP-XIT.
047338     MOVE TDAI-DS-TYPE OF TDAIRA (Z-II) TO TDB-TDAI-DS-TYPE OF    
047340         TDB-TDAIRA (Z-II).
047342     MOVE TDAI-CN-TYPE OF TDAIRA (Z-II) TO TDB-TDAI-CN-TYPE OF    
047344         TDB-TDAIRA (Z-II).
047346     MOVE TDAI-DS-CN-AMT OF TDAIRA (Z-II) TO TDB-TDAI-DS-CN-AMT   
047348         OF TDB-TDAIRA (Z-II).
047350     MOVE TDAI-DS-PEN-AMT OF TDAIRA (Z-II) TO TDB-TDAI-DS-PEN-AMT 
047352         OF TDB-TDAIRA (Z-II).
047354     MOVE TDAI-DS-WTHLD-AMT OF TDAIRA (Z-II) TO                   
047356         TDB-TDAI-DS-WTHLD-AMT OF TDB-TDAIRA (Z-II).
047358     MOVE TDAI-DS-ST-WH-AMT OF TDAIRA (Z-II) TO                   
047360         TDB-TDAI-DS-ST-WH-AMT OF TDB-TDAIRA (Z-II).
047362     MOVE TDAI-DS-EXC-EARN OF TDAIRA (Z-II) TO                    
047364         TDB-TDAI-DS-EXC-EARN OF TDB-TDAIRA (Z-II).
047366     ADD 1 TO Z-II.
047368     GO TO Z-15-8-1-LOOP.
047370 Z-15-8-1-LOOP-XIT.
047372     MOVE TDAI-DS-C-YTD-CNT OF TDAIRA TO TDB-TDAI-DS-C-YTD-CNT OF 
047374         TDB-TDAIRA.
047376     MOVE TDAI-DS-P-YTD-CNT OF TDAIRA TO TDB-TDAI-DS-P-YTD-CNT OF 
047378         TDB-TDAIRA.
047380     MOVE TDAI-DS-AMT-C-YTD OF TDAIRA TO TDB-TDAI-DS-AMT-C-YTD OF 
047382         TDB-TDAIRA.
047384     MOVE TDAI-DS-AMT-P-YTD OF TDAIRA TO TDB-TDAI-DS-AMT-P-YTD OF 
047386         TDB-TDAIRA.
047388     MOVE TDAI-DS-INT-AMT OF TDAIRA TO TDB-TDAI-DS-INT-AMT OF     
047390         TDB-TDAIRA.
047392     MOVE TDAI-CN-YTD-CNT OF TDAIRA TO TDB-TDAI-CN-YTD-CNT OF     
047394         TDB-TDAIRA.
047396     MOVE TDAI-CN-YTD-AMT OF TDAIRA TO TDB-TDAI-CN-YTD-AMT OF     
047398         TDB-TDAIRA.
047400     MOVE TDAI-CN-LYTD-AMT OF TDAIRA TO TDB-TDAI-CN-LYTD-AMT OF   
047402         TDB-TDAIRA.
047404     MOVE TDAI-EMP-CONT-LYR OF TDAIRA TO TDB-TDAI-EMP-CONT-LYR OF 
047406         TDB-TDAIRA.
047408     MOVE TDAI-REG-CONT-LYR OF TDAIRA TO TDB-TDAI-REG-CONT-LYR OF 
047410         TDB-TDAIRA.
047412     MOVE TDAI-UNINSURED OF TDAIRA TO TDB-TDAI-UNINSURED OF       
047414         TDB-TDAIRA.
047416     MOVE TDAI-ROLLOVER OF TDAIRA TO TDB-TDAI-ROLLOVER OF         
047418         TDB-TDAIRA.
047420     MOVE TDAI-ROLLOVER-LYR OF TDAIRA TO TDB-TDAI-ROLLOVER-LYR OF 
047422         TDB-TDAIRA.
047424     MOVE TDAI-TRANSFER-IN OF TDAIRA TO TDB-TDAI-TRANSFER-IN OF   
047426         TDB-TDAIRA.
047428     MOVE TDAI-TRANSFER-OUT OF TDAIRA TO TDB-TDAI-TRANSFER-OUT OF 
047430         TDB-TDAIRA.
047432     MOVE TDAI-1ST-CN-DATE OF TDAIRA TO TDB-TDAI-1ST-CN-DATE OF   
047434         TDB-TDAIRA.
047436     MOVE TDAI-BASIS-C-LTD OF TDAIRA TO TDB-TDAI-BASIS-C-LTD OF   
047438         TDB-TDAIRA.
047440     MOVE TDAI-BASIS-D-LTD OF TDAIRA TO TDB-TDAI-BASIS-D-LTD OF   
047442         TDB-TDAIRA.
047444     MOVE TDAI-BASIS-D-YTD OF TDAIRA TO TDB-TDAI-BASIS-D-YTD OF   
047446         TDB-TDAIRA.
047448     MOVE 0350 TO TDB-MESSAGE-NBR.
047450 Z-15-3-ENDIF.
047452     GO TO Z-15-1-ENDIF.
047454 Z-15-1-1-ELSE.
047456     MOVE 3461 TO TDB-ERROR-NBR.
047458 Z-15-1-ENDIF.
047460 Z-15-END.
047462     IF Z-EDIT-ERROR
047464         GO TO Z-15-XIT.
047466 Z-15-SKIP.
047468     IF Z-EXIT-LEVEL NOT < 0
047470         MOVE 0 TO Z-EXIT-CODE
047472         MOVE 9999 TO Z-EXIT-LEVEL.
047474 Z-15-XIT.
047476     EXIT.
047478*
047480*****************************************************************
047482*    PROCEDURE TDD-MINDIST-SETUP-AND-CALC
047484*****************************************************************
047486 Z-28-PROCEDURE.
047488*
047490     MOVE 0 TO Z-EXIT-CODE.
047492     MOVE 9999 TO Z-EXIT-LEVEL.
047494     IF ( TDB-TDAA-INHERIT-IRA = 2 ) AND ( TDB-TDAA-BNF-DEATH-DT  
047496         NOT = ZEROS )
047498         NEXT SENTENCE ELSE
047500         GO TO Z-28-1-1-ELSE.
047502*
047504     PERFORM Z-DATE-INITIALIZE-REGS
047506         THRU Z-DATE-INITIALIZE-REGS-EXIT.
047508     PERFORM Z-DATE-INITIALIZE-CTRL
047510        THRU Z-DATE-INITIALIZE-CTRL-EXIT.
047512     MOVE TDB-TDAA-BNF-DEATH-DT TO Z-DATE2-FORMAT-9.
047514*    DATE UNIT INITIALIZATION
047516     COMPUTE Z-DATE-Y = 1.
047518*    LOAD DATE REGISTERS FOR CALCULATIONS
047520*    LOAD DATE REGISTER 1
047522     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
047524     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
047526     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
047528     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
047530     PERFORM Z-DATE-CALC-LEAP-YEAR
047532        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
047534     PERFORM Z-DATE-MDY-TO-JUL-CTRL
047536        THRU Z-DATE-MDY-TO-JUL-CTRL-EXIT.
047538     MOVE Z-DATE-JJJ-3 TO Z-DATE-JJJ-1.
047540*    PERFORM CALCULATIONS OF INDIVIDUAL DATE UNITS
047542     IF Z-DATE-Y NOT = ZEROS
047544         PERFORM Z-DATE-CALC-Y
047546            THRU Z-DATE-CALC-Y-EXIT.
047548     IF Z-DATE-C NOT = ZEROS
047550         PERFORM Z-DATE-CALC-C
047552            THRU Z-DATE-CALC-C-EXIT.
047554*    RE-ADJUST AFTER CALCULATIONS
047556     PERFORM Z-DATE-CALC-LEAP-YEAR
047558        THRU Z-DATE-CALC-LEAP-YEAR-EXIT.
047560     PERFORM Z-DATE-CALC-MONTH-DAYS
047562        THRU Z-DATE-CALC-MONTH-DAYS-EXIT.
047564*    PLACE THE RESULTS WHERE THEY BELONG
047566     MOVE Z-DATE-CC-1 TO Z-DATE2-CC.
047568     MOVE Z-DATE-YY-1 TO Z-DATE2-YY.
047570     MOVE Z-DATE-MM-1 TO Z-DATE2-MM.
047572     MOVE Z-DATE-DD-1 TO Z-DATE2-DD.
047574     MOVE Z-DATE2-FORMAT-9 TO WS-CUST-YAD.
047576     PERFORM Z-DATE-INITIALIZE-CTRL
047578        THRU Z-DATE-INITIALIZE-CTRL-EXIT.
047580     MOVE WS-CUST-YAD TO Z-DATE2-FORMAT-9.
047582*    LOAD DATE REGISTER 1
047584     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
047586     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
047588     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
047590     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
047592     MOVE Z-DATE-1 TO Z-DATE-2.
047594     MOVE TDB-TDAC-BIRTH-DT TO Z-DATE2-FORMAT-9.
047596*    LOAD DATE REGISTER 1
047598     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
047600     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
047602     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
047604     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
047606     PERFORM Z-DATE-YY-DIFF THRU Z-DATE-YY-DIFF-EXIT.
047608     MOVE Z-DATE-Y TO WS-MD-BN-AGE.
047610     PERFORM Z-DATE-INITIALIZE-CTRL
047612        THRU Z-DATE-INITIALIZE-CTRL-EXIT.
047614     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.
047616*    LOAD DATE REGISTER 1
047618     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
047620     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
047622     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
047624     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
047626     MOVE Z-DATE-1 TO Z-DATE-2.
047628     MOVE WS-CUST-YAD TO Z-DATE2-FORMAT-9.
047630*    LOAD DATE REGISTER 1
047632     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
047634     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
047636     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
047638     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
047640     PERFORM Z-DATE-YY-DIFF THRU Z-DATE-YY-DIFF-EXIT.
047642     MOVE Z-DATE-Y TO WS-NUM-YR-YAD.
047644 Z-28-1-1-ELSE.
047646     IF ( TDB-TDAA-BENEF-CD = 1 ) AND ( TDB-TDAA-BNF-BIRTH-DT NOT 
047648         = ZEROS )
047650         NEXT SENTENCE ELSE
047652         GO TO Z-28-5-1-ELSE.
047654     PERFORM Z-DATE-INITIALIZE-CTRL
047656        THRU Z-DATE-INITIALIZE-CTRL-EXIT.
047658     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.
047660*    LOAD DATE REGISTER 1
047662     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
047664     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
047666     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
047668     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
047670     MOVE Z-DATE-1 TO Z-DATE-2.
047672     MOVE TDB-TDAA-BNF-BIRTH-DT TO Z-DATE2-FORMAT-9.
047674*    LOAD DATE REGISTER 1
047676     COMPUTE Z-DATE-CC-1 = Z-DATE2-CC.
047678     COMPUTE Z-DATE-YY-1 = Z-DATE2-YY.
047680     COMPUTE Z-DATE-MM-1 = Z-DATE2-MM.
047682     COMPUTE Z-DATE-DD-1 = Z-DATE2-DD.
047684     PERFORM Z-DATE-YY-DIFF THRU Z-DATE-YY-DIFF-EXIT.
047686     MOVE Z-DATE-Y TO WS-MD-BN-AGE.
047688     MOVE TDB-TDAA-BENEF-CD TO WS-MD-SPOUSE.
047690 Z-28-5-1-ELSE.
047692     COMPUTE WS-MD-FMV = TDB-TDAA-FAIR-MRKT .
047694
047696********* COMPUTE WHEN
047698     IF TDB-TDAA-FAIR-MRKT = ZEROS
047700        NEXT SENTENCE
047702     ELSE
047704        GO TO Z-28-9-COMPUTE-SKIP.
047706     COMPUTE WS-MD-FMV = TDB-TDAA-CURR-BAL .
047708
047710 Z-28-9-COMPUTE-SKIP.
047712     IF TDB-TDAA-RMD-MAN-CALC = ZERO
047714         NEXT SENTENCE ELSE
047716         GO TO Z-28-10-1-ELSE.
047718************ PERFORM CALC-MINDIST-AMT
047720     PERFORM Z-34-PROCEDURE THRU Z-34-XIT.
047722     IF  Z-EXIT-EDITEXIT
047724         GO TO Z-28-XIT.
047726     IF  Z-DMS2-ABORT-FLAG = 1
047728         GO TO Z-28-XIT.
047730     IF  Z-EXIT-LEVEL < 0
047732         GO TO Z-28-END.
047734*
047736     GO TO Z-28-10-ENDIF.
047738 Z-28-10-1-ELSE.
047740     MOVE TDB-TDAA-RMD-AMOUNT TO WS-MD-AMT.
047742     MOVE TDB-TDAA-LIFE-FACTOR TO WS-MD-FACT.
047744 Z-28-10-ENDIF.
047746 Z-28-END.
047748     IF Z-EDIT-ERROR
047750         GO TO Z-28-XIT.
047752 Z-28-SKIP.
047754     IF Z-EXIT-LEVEL NOT < 0
047756         MOVE 0 TO Z-EXIT-CODE
047758         MOVE 9999 TO Z-EXIT-LEVEL.
047760 Z-28-XIT.
047762     EXIT.
047764*
047766*****************************************************************
047768*    PROCEDURE TDB-CUST-01BAT2-ACTV-ADJ
047770*****************************************************************
047772 Z-32-PROCEDURE.
047774*
047776     MOVE TDAC-BANK OF TDACUST TO HOLD-TDAC-BANK OF HOLD-TDACUST.
047778     MOVE TDAC-CUST OF TDACUST TO HOLD-TDAC-CUST OF HOLD-TDACUST.
047780     MOVE TDAC-BRCH OF TDACUST TO HOLD-TDAC-BRCH OF HOLD-TDACUST.
047782     MOVE TDAC-STATUS OF TDACUST TO HOLD-TDAC-STATUS OF           
047784         HOLD-TDACUST.
047786     MOVE TDAC-NAME-1 OF TDACUST TO HOLD-TDAC-NAME-1 OF           
047788         HOLD-TDACUST.
047790     MOVE TDAC-N1-KEY OF TDACUST TO HOLD-TDAC-N1-KEY OF           
047792         HOLD-TDACUST.
047794     MOVE TDAC-N1-FIRST OF TDACUST TO HOLD-TDAC-N1-FIRST OF       
```

⚠️  This is the source code you must document.
    477 lines from 23417 to 23893.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

