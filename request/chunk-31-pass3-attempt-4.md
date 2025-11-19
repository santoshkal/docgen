# LLM Request Debug File
Generated: 2025-11-18T19:29:46.106600

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 31/55
- **Model**: gpt-4.1
- **Chunk Number**: 31
- **Pass Number**: 3
- **Attempt Number**: 4 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,086 tokens
- **User Prompt**: ~10,263 tokens
- **Total Input**: ~12,349 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 31/55" (ID: detailed-code-explanation)

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


**CHUNK 31 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T18:05:37.383587", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 31 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 14845 to 15320 (476 lines)\nChunk Tokens (estimated): ~8,067\nActual Input Tokens: 9,473 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 14845-15320 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 31 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 31 of 55.\n\n\n=============================================================================\nCHUNK 31 SOURCE CODE (Lines 14845-15320)\n=============================================================================\n\n```cobol\n029698 99-PRT-LABEL-INIT.                                               \n029700     ACCEPT PRT-OPEN-DATE FROM TODAYS-DATE.                       \n029702     ACCEPT PRT-OPEN-TIME FROM TIME.                              \n029704     MOVE PRT-OPEN-DD TO H-CSI-DD.                                \n029706     MOVE PRT-OPEN-HHMM TO H-CSI-HHMM.                            \n029708     IF SW3-1 AND GWS-PRT-PID-FLAG = 0                            \n029710         MOVE 1 TO GWS-PRT-PID-FLAG                               \n029712*        DISPLAY \"ENTER PACK NAME FOR MICROFICHE PRINT FILES\"     \n029714*        ACCEPT GWS-PRT-PID-FICHE                                 \n029716         DISPLAY \"ENTER PACK NAME FOR PRINT FILES\"                \n029718         ACCEPT GWS-PRT-PID                                       \n029720         MOVE GWS-PRT-PID TO GWS-PRT-PID-FICHE                    \n029722*        DISPLAY \"ENTER Y IF PRINT FILES ARE TO BE RELEASED\"      \n029724*        DISPLAY \"AFTER EACH BANK\"                                \n029726         MOVE \"Y\" TO GWS-REL-DUMMY-AREA.                          \n029728*        DISPLAY \"ENTER N IF SPOOLER IS TO BE DISABLE\"            \n029730*        ACCEPT SPOOLER-ENABLE.                                   \n029732*=============================================================    \n029734*  NOTE : TO USE THE REMOTE FILE NAME SETUP REPLACE               \n029736*         'PERFORM 99-PRT-REMOTE-LBL-CHK' WITH                    \n029738*         'PERFORM 99-PRT-RMT-LBL-CHK' USING COPY REPLACING       \n029740*         REFER TO PRINT RTN SETUP NARRATIVE FOR PROCEDURE        \n029742*=============================================================    \n029744     MOVE 0 TO Z-EXIT-CODE.\n029746     MOVE 9999 TO Z-EXIT-LEVEL.\n029748     IF GWS-LONG-PRTNAMES-NEW = 1 AND GWS-PRT-NEW = 1\n029750         NEXT SENTENCE ELSE\n029752         GO TO Z-7-1-1-ELSE.\n029754         PERFORM 99-PRT-NEW-NAME-CHK                              \n029756     GO TO Z-7-1-ENDIF.\n029758 Z-7-1-1-ELSE.\n029760     IF GWS-RMT-PRT-OPTION = 1\n029762         NEXT SENTENCE ELSE\n029764         GO TO Z-7-1-2-ELSE.\n029766         PERFORM 99-PRT-REMOTE-LBL-CHK.                           \n029768************ PERFORM TPR-REMOTE-BANK\n029770     PERFORM Z-8-PROCEDURE THRU Z-8-XIT.\n029772     IF  Z-EXIT-EDITEXIT\n029774         GO TO Z-7-XIT.\n029776     IF  Z-DMS2-ABORT-FLAG = 1\n029778         GO TO Z-7-XIT.\n029780     IF  Z-EXIT-LEVEL < 0\n029782         GO TO Z-7-END.\n029784*\n029786         GO TO 99-PRT-LABEL-END.                                  \n029788 Z-7-1-2-ELSE.\n029790 Z-7-1-ENDIF.\n029792     IF (GWS-CST-PERIOD = \"0\" OR SPACE)                           \n029794         MOVE \"0\" TO GWS-CST-PERIOD.                              \n029796     MOVE \"/\" TO GWS-SLASH. MOVE \" ON \" TO GWS-ON.                \n029798     IF GWS-APPL = SPACES MOVE \"CSI\" TO GWS-APPL.                 \n029800     IF GWS-FILE-TYPE = SPACE MOVE \"P\" TO GWS-FILE-TYPE.          \n029802     IF GWS-NO-PARTS = SPACE MOVE \"1\" TO GWS-NO-PARTS.            \n029804     IF GWS-PRT-DESCRIPTOR = SPACES                               \n029806         MOVE \"SP\" TO GWS-PRT-DESCRIPTOR.                         \n029808     IF GWS-BRANCH-CODE = SPACES MOVE \"00\" TO GWS-BRANCH-CODE.    \n029810     IF GWS-MICROFICHE-CODE = SPACE MOVE 0 TO GWS-MICROFICHE-CODE.\n029812     IF (GWS-MICROFICHE-CODE > ZERO) OR                           \n029814         (GWS-MICROFICHE-CODE ALPHABETIC)                         \n029816         IF  GWS-NO-PARTS = \"1\"                                   \n029818             MOVE \"A\" TO GWS-NO-PARTS                             \n029820             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n029822         ELSE                                                     \n029824         IF  GWS-NO-PARTS = \"2\"                                   \n029826             MOVE \"B\" TO GWS-NO-PARTS                             \n029828             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n029830         ELSE                                                     \n029832         IF  GWS-NO-PARTS = \"3\"                                   \n029834             MOVE \"C\" TO GWS-NO-PARTS                             \n029836             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n029838         ELSE                                                     \n029840         IF  GWS-NO-PARTS = \"4\"                                   \n029842             MOVE \"D\" TO GWS-NO-PARTS                             \n029844             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n029846         ELSE                                                     \n029848         IF  GWS-NO-PARTS = \"5\"                                   \n029850             MOVE \"E\" TO GWS-NO-PARTS                             \n029852             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n029854         ELSE                                                     \n029856         IF  GWS-NO-PARTS = \"6\"                                   \n029858             MOVE \"F\" TO GWS-NO-PARTS                             \n029860             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n029862         ELSE                                                     \n029864         IF  GWS-NO-PARTS = \"7\"                                   \n029866             MOVE \"G\" TO GWS-NO-PARTS                             \n029868             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n029870         ELSE                                                     \n029872         IF  GWS-NO-PARTS = \"8\"                                   \n029874             MOVE \"H\" TO GWS-NO-PARTS                             \n029876             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n029878         ELSE                                                     \n029880         IF  GWS-NO-PARTS = \"9\"                                   \n029882             MOVE \"I\" TO GWS-NO-PARTS                             \n029884             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n029886         ELSE                                                     \n029888         IF  GWS-NO-PARTS = \"0\"                                   \n029890             MOVE \"0\" TO GWS-NO-PARTS                             \n029892             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n029894         ELSE                                                     \n029896             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n029898     ELSE                                                         \n029900         MOVE GWS-PRT-PID TO GWS-PACK.                            \n029902     IF GWS-NO-PARTS = \"{\" MOVE \"0\" TO GWS-NO-PARTS.              \n029904     IF GWS-BANK-NO-X = SPACES MOVE \"000\" TO GWS-BANK-NO-X.       \n029906     IF (GWS-TIME-CTL = 0) AND (GWS-TIME NOT = SPACES)            \n029908         ACCEPT GWS-TIME FROM TIME.                               \n029910     IF GWS-TIME = \"......\" MOVE SPACES TO GWS-TIME.              \n029912     IF GWS-BRANCH-CODE = \"..\" MOVE \"00\" TO GWS-BRANCH-CODE.      \n029914     MOVE GWS-A12-PERIOD TO GWS-PERIOD GWS-RMT-PERIOD.            \n029916     IF (GWS-LONG-PRTNAMES-NEW = 1) AND (GWS-PRT-NEW = 1)         \n029918         GO TO 99-PRT-LABEL-END.                                  \n029920     IF (GWS-RMT-PRT-OPTION = 1) AND (GWS-RMT-BK-FLAG = 1)        \n029922         GO TO 99-PRT-LABEL-END.                                  \n029924     IF GWS-LONG-PRTNAMES NOT = 0                                 \n029926         GO TO 99-LONG-LABEL-CHK                                  \n029928     ELSE                                                         \n029930         MOVE SPACES TO GWS-LPRT-NAMES.                           \n029932     IF GWS-PRT-REL-FLAG = \"Y\" MOVE SPACES TO ID-PRT74-2.         \n029934     IF COBOL-74 AND ID-PRT74-1-15 = GWS-PRT-LABEL-1-15           \n029936         GO TO 99-PRT-LABEL-END.                                  \n029938     IF NOT COBOL-74 AND GWS-FAMILY = PRT-ID-FAMILY AND           \n029940       GWS-MICRO-BANK = PRT-ID-ELEM1-4   GO TO 99-PRT-LABEL-END.  \n029942     IF COBOL-74 MOVE GWS-PRINT-LABEL TO ID-PRT74-2 ELSE          \n029944       MOVE GWS-PACK TO PRT-ID-PACK MOVE GWS-ELEM TO PRT-ID-ELEM  \n029946       MOVE GWS-FAMILY TO PRT-ID-FAMILY.                          \n029948     GO TO 99-PRT-LABEL-END.                                      \n029950 99-LONG-LABEL-CHK.                                               \n029952     MOVE \"PRT\" TO GWS-LPRT-CST.                                  \n029954     IF GWS-LONG-PRTNAMES = 2                                     \n029956         MOVE \"EOM\" TO GWS-LPRT-CST.                              \n029958     IF GWS-LONG-PRTNAMES = 3                                     \n029960         MOVE \"EOY\" TO GWS-LPRT-CST.                              \n029962     MOVE GWS-CSI-BK TO GWS-LPRT-BK.                              \n029964     MOVE GWS-CSI-DC TO GWS-LPRT-DC.                              \n029966     MOVE GWS-APPL TO GWS-LPRT-APP.                               \n029968     MOVE GWS-CST-PERIOD TO GWS-LPRT-PART-1.                      \n029970     MOVE GWS-NO-PARTS TO GWS-LPRT-PART-2.                        \n029972     MOVE GWS-PRT-DESCRIPTOR TO GWS-LPRT-TYPE.                    \n029974     MOVE GWS-MICROFICHE-CODE TO GWS-LPRT-FICHE.                  \n029976     MOVE GWS-TIME TO GWS-LPRT-TIMESTAMP.                         \n029978     MOVE \"/\" TO GWS-LPRT-S1, GWS-LPRT-S2, GWS-LPRT-S3,           \n029980       GWS-LPRT-S4, GWS-LPRT-S5.                                  \n029982     MOVE GWS-ON TO GWS-LPRT-ON.                                  \n029984     MOVE GWS-PACK TO GWS-LPRT-PACK.                              \n029986     MOVE GWS-PERIOD TO GWS-LPRT-PERIOD.                          \n029988     IF GWS-PRT-REL-FLAG = \"Y\"                                    \n029990         MOVE SPACES TO ID-PRT74-2.                               \n029992     IF (GWS-LPRT-PREFX = ID-PRT74-PREFX)                         \n029994         GO TO 99-PRT-LABEL-END.                                  \n029996     MOVE GWS-PRINT-LABEL-LONG TO ID-PRT74-2.                     \n029998 99-PRT-LABEL-END.                                                \n030000 99-PRT-LABEL-EXIT.                                               \n030002*                                                                 \n030004 99-PRT-REMOTE-LBL-CHK     SECTION 51.                            \n030006 99-PRT-REMOTE-LBL-INIT.                                          \n030008     EXIT.                                                        \n030010*=================================================================\n030012 99-PRT-EXCEPT-RTN                                    SECTION 00. \n030014 99-PRT-EXC-REC.                                                  \n030016     IF GWS-PRT-EXC-BLOCK-CTL = 97 OR 95                          \n030018         MOVE 0 TO HDR-CTL.                                       \n030020     MOVE GWS-PRT-EXC-PAGE-CTL TO PAGE-ADVANCE.                   \n030022     MOVE GWS-PRT-EXC-NO-LINES TO NO-LINES.                       \n030024     MOVE GWS-PRT-EXC-DATA     TO PRINT-LINE.                     \n030026 99-PRT-EXC-CREATE-REC.                                           \n030028     IF GWS-PRT-EXC-BLOCK-CTL NOT = 97                            \n030030         MOVE 98           TO GWS-PRT-EXC-BLOCK-CTL.              \n030032     MOVE PAGE-ADVANCE     TO GWS-PRT-EXC-PAGE-CTL.               \n030034     MOVE NO-LINES         TO GWS-PRT-EXC-NO-LINES.               \n030036     MOVE PRINT-LINE       TO GWS-PRT-EXC-DATA.                   \n030038*L                                                                \n030040*L\"S\"/\"GEN.L\"/\"RMTPRTLBL\".                                        \n030042 99-PRT-NEW-NAME-CHK                                  SECTION 51. \n030044 99-PRT-NEW-NAME.                                                 \n030046     MOVE 0 TO GWS-CTR, GWS-RMT-BK-FLAG, GWS-RPT-TYPE.            \n030048     IF GWS-APPL = SPACES                                         \n030050         MOVE \"CSI\"              TO GWS-APPL.                     \n030052     IF GWS-NO-PARTS = SPACES                                     \n030054         MOVE \"1\"                TO GWS-NO-PARTS.                 \n030056     MOVE \"PRINT\"                TO GWS-NPRT-CST.                 \n030058     MOVE \"/\"        TO GWS-NPRT-S1, GWS-NPRT-S2, GWS-NPRT-S3,    \n030060                        GWS-NPRT-S4, GWS-NPRT-S5, GWS-NPRT-S6.    \n030062     MOVE GWS-CSI-BK             TO GWS-NPRT-BK.                  \n030064     MOVE GWS-CSI-DC             TO GWS-NPRT-DC.                  \n030066     MOVE GWS-APPL               TO GWS-NPRT-APP.                 \n030068     MOVE GWS-PRT-DESCRIPTOR     TO GWS-NPRT-TYPE, GWS-NPRT-TYPE2.\n030070     MOVE 01                     TO GWS-NPRT-COPIES.              \n030072     MOVE 00                     TO GWS-NPRT-EXP.                 \n030074     MOVE H-DD                   TO GWS-NPRT-DD.                  \n030076     MOVE GWS-RMT-EXT            TO GWS-NPRT-RPT-NO.              \n030078     MOVE 0                      TO GWS-NPRT-RP.                  \n030080     MOVE \"I\"                    TO GWS-NPRT-CNTRV.               \n030082     MOVE GWS-APPL               TO GWS-RMT-WORK-APPL.            \n030084     IF GWS-RMT-WORK-APPL = \"ACH\" MOVE \"H\" TO GWS-NPRT-APP2       \n030086     ELSE IF GWS-RMT-WORK-APPL = \"ATM\" MOVE \"A\" TO GWS-NPRT-APP2  \n030088     ELSE IF GWS-RMT-WORK-APPL = \"BDS\" MOVE \"B\" TO GWS-NPRT-APP2  \n030090     ELSE IF GWS-RMT-WORK-APPL = \"CSI\" MOVE \"Z\" TO GWS-NPRT-APP2  \n030092     ELSE IF GWS-RMT-WORK-APPL = \"CLN\" MOVE \"L\" TO GWS-NPRT-APP2  \n030094     ELSE IF GWS-RMT-WORK-APPL = \"CIF\" MOVE \"K\" TO GWS-NPRT-APP2  \n030096     ELSE IF GWS-RMT-WORK-APPL = \"CLB\" MOVE \"X\" TO GWS-NPRT-APP2  \n030098     ELSE IF GWS-RMT-WORK-APPL = \"CKR\" MOVE \"J\" TO GWS-NPRT-APP2  \n030100     ELSE IF GWS-RMT-WORK-APPL = \"COD\" MOVE \"C\" TO GWS-NPRT-APP2  \n030102     ELSE IF GWS-RMT-WORK-APPL = \"DDA\" MOVE \"D\" TO GWS-NPRT-APP2  \n030104     ELSE IF GWS-RMT-WORK-APPL = \"FLP\" MOVE \"Y\" TO GWS-NPRT-APP2  \n030106     ELSE IF GWS-RMT-WORK-APPL = \"GNL\" OR \"GL2\"                   \n030108                                       MOVE \"G\" TO GWS-NPRT-APP2  \n030110     ELSE IF GWS-RMT-WORK-APPL = \"ILN\" MOVE \"I\" TO GWS-NPRT-APP2  \n030112     ELSE IF GWS-RMT-WORK-APPL = \"IRA\" MOVE \"R\" TO GWS-NPRT-APP2  \n030114     ELSE IF GWS-RMT-WORK-APPL = \"MCR\" MOVE \"P\" TO GWS-NPRT-APP2  \n030116     ELSE IF GWS-RMT-WORK-APPL = \"ONL\" MOVE \"O\" TO GWS-NPRT-APP2  \n030118     ELSE IF GWS-RMT-WORK-APPL = \"PAY\" MOVE \"W\" TO GWS-NPRT-APP2  \n030120     ELSE IF GWS-RMT-WORK-APPL = \"SAV\" MOVE \"S\" TO GWS-NPRT-APP2  \n030122     ELSE IF GWS-RMT-WORK-APPL = \"SDB\" MOVE \"Q\" TO GWS-NPRT-APP2  \n030124     ELSE IF GWS-RMT-WORK-APPL = \"STH\" MOVE \"H\" TO GWS-NPRT-APP2  \n030126     ELSE IF GWS-RMT-WORK-APPL = \"TFR\" MOVE \"T\" TO GWS-NPRT-APP2  \n030128     ELSE IF GWS-RMT-WORK-APPL = \"TDA\" MOVE \"N\" TO GWS-NPRT-APP2  \n030130     ELSE IF GWS-RMT-WORK-APPL = \"TKL\" MOVE \"U\" TO GWS-NPRT-APP2  \n030132     ELSE IF GWS-RMT-WORK-APPL = \"EOY\" MOVE \"E\" TO GWS-NPRT-APP2  \n030134     ELSE MOVE GWS-RMT-WORK-APPL-1X  TO GWS-NPRT-APP2.            \n030136     IF GWS-CNTR-VIEW = 0                                         \n030138         MOVE \"I\"                TO GWS-NPRT-CNTRV                \n030140     ELSE                                                         \n030142         MOVE \"C\"                TO GWS-NPRT-CNTRV                \n030144         IF GWS-CNTR-VIEW = 2 OR 3                                \n030146              MOVE \"R\"           TO GWS-NPRT-RP.                  \n030148     IF (GWS-MICROFICHE-CODE > ZERO) OR                           \n030150         (GWS-MICROFICHE-CODE ALPHABETIC)                         \n030152         IF  GWS-NO-PARTS = \"1\"                                   \n030154             MOVE \"A\" TO GWS-NO-PARTS                             \n030156             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n030158         ELSE                                                     \n030160         IF  GWS-NO-PARTS = \"2\"                                   \n030162             MOVE \"B\" TO GWS-NO-PARTS                             \n030164             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n030166         ELSE                                                     \n030168         IF  GWS-NO-PARTS = \"3\"                                   \n030170             MOVE \"C\" TO GWS-NO-PARTS                             \n030172             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n030174         ELSE                                                     \n030176         IF  GWS-NO-PARTS = \"4\"                                   \n030178             MOVE \"D\" TO GWS-NO-PARTS                             \n030180             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n030182         ELSE                                                     \n030184         IF  GWS-NO-PARTS = \"5\"                                   \n030186             MOVE \"E\" TO GWS-NO-PARTS                             \n030188             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n030190         ELSE                                                     \n030192         IF  GWS-NO-PARTS = \"6\"                                   \n030194             MOVE \"F\" TO GWS-NO-PARTS                             \n030196             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n030198         ELSE                                                     \n030200         IF  GWS-NO-PARTS = \"7\"                                   \n030202             MOVE \"G\" TO GWS-NO-PARTS                             \n030204             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n030206         ELSE                                                     \n030208         IF  GWS-NO-PARTS = \"8\"                                   \n030210             MOVE \"H\" TO GWS-NO-PARTS                             \n030212             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n030214         ELSE                                                     \n030216         IF  GWS-NO-PARTS = \"9\"                                   \n030218             MOVE \"I\" TO GWS-NO-PARTS                             \n030220             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n030222         ELSE                                                     \n030224         IF  GWS-NO-PARTS = \"0\"                                   \n030226             MOVE \"0\" TO GWS-NO-PARTS                             \n030228             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n030230         ELSE                                                     \n030232             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   \n030234     ELSE                                                         \n030236         MOVE GWS-PRT-PID TO GWS-PACK.                            \n030238     MOVE GWS-PACK TO GWS-NPRT-PACK.                              \n030240     IF ( ( WS-SYS-HOST = \"CSIA\" ) OR ( WS-SYS-HOST = \"CSID\" ) OR \n030242         ( WS-SYS-HOST = \"CSIB\" ) )\n030244         NEXT SENTENCE ELSE\n030246         GO TO Z-7-3-1-ELSE.\n030248     GO TO Z-7-3-ENDIF.\n030250 Z-7-3-1-ELSE.\n030252     MOVE SPACES TO GWS-NPRT-PACK.\n030254     MOVE SPACES TO GWS-PACK.\n030256 Z-7-3-ENDIF.\n030258     IF WS-DMS-ERROR = 5                                          \n030260         GO TO 99-NEW-END.                                        \n030262     FIND SPCPRT VIA FIRST SPCPRTCURR                             \n030264       AT SPCP-BANK = GWS-CSI-BK AND                              \n030266          SPCP-APP = GWS-APPL AND                                 \n030268          SPCP-TYPE = GWS-PRT-DESCRIPTOR AND                      \n030270          SPCP-RPT-NUM = GWS-RMT-EXT ON EXCEPTION                 \n030272          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             \n030274              GO TO 99-PRT-NEW-FIND2                              \n030276          ELSE                                                    \n030278              GO TO 99-NEW-END.                                   \n030280     GO TO 99-PRT-NEW-FOUND.                                      \n030282 99-PRT-NEW-FIND2.                                                \n030284     FIND SPCPRT VIA FIRST SPCPRTCURR                             \n030286       AT SPCP-BANK = GWS-CSI-BK AND                              \n030288          SPCP-APP = GWS-APPL AND                                 \n030290          SPCP-TYPE = GWS-PRT-DESCRIPTOR AND                      \n030292          SPCP-RPT-NUM = \"   \" ON EXCEPTION                       \n030294          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             \n030296              GO TO 99-PRT-NEW-FIND3                              \n030298          ELSE                                                    \n030300              GO TO 99-NEW-END.                                   \n030302     GO TO 99-PRT-NEW-FOUND.                                      \n030304 99-PRT-NEW-FIND3.                                                \n030306     FIND SPCPRT VIA FIRST SPCPRTCURR                             \n030308       AT SPCP-BANK = GWS-CSI-BK AND                              \n030310          SPCP-APP = GWS-APPL AND                                 \n030312          SPCP-TYPE = \"  \" AND                                    \n030314          SPCP-RPT-NUM = \"   \" ON EXCEPTION                       \n030316          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             \n030318              GO TO 99-PRT-NEW-FIND4                              \n030320          ELSE                                                    \n030322              GO TO 99-NEW-END.                                   \n030324     GO TO 99-PRT-NEW-FOUND.                                      \n030326 99-PRT-NEW-FIND4.                                                \n030328     FIND SPCPRT VIA FIRST SPCPRTCURR                             \n030330       AT SPCP-BANK = GWS-CSI-BK AND                              \n030332          SPCP-APP = \"   \" AND                                    \n030334          SPCP-TYPE = GWS-PRT-DESCRIPTOR AND                      \n030336          SPCP-RPT-NUM = GWS-RMT-EXT ON EXCEPTION                 \n030338          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             \n030340              GO TO 99-PRT-NEW-FIND5                              \n030342          ELSE                                                    \n030344              GO TO 99-NEW-END.                                   \n030346     GO TO 99-PRT-NEW-FOUND.                                      \n030348 99-PRT-NEW-FIND5.                                                \n030350     FIND SPCPRT VIA FIRST SPCPRTCURR                             \n030352       AT SPCP-BANK = GWS-CSI-BK AND                              \n030354          SPCP-APP = \"   \" AND                                    \n030356          SPCP-TYPE = GWS-PRT-DESCRIPTOR AND                      \n030358          SPCP-RPT-NUM = \"   \" ON EXCEPTION                       \n030360          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             \n030362              GO TO 99-PRT-NEW-FIND6                              \n030364          ELSE                                                    \n030366              GO TO 99-NEW-END.                                   \n030368     GO TO 99-PRT-NEW-FOUND.                                      \n030370 99-PRT-NEW-FIND6.                                                \n030372     FIND SPCPRT VIA FIRST SPCPRTCURR                             \n030374       AT SPCP-BANK = GWS-CSI-BK AND                              \n030376          SPCP-APP = \"   \" AND                                    \n030378          SPCP-TYPE = \"  \" AND                                    \n030380          SPCP-RPT-NUM = \"   \" ON EXCEPTION                       \n030382          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             \n030384              GO TO 99-NEW-END                                    \n030386          ELSE                                                    \n030388              GO TO 99-NEW-END.                                   \n030390 99-PRT-NEW-FOUND.                                                \n030392     MOVE SPCP-NUM-COPIES        TO GWS-NPRT-COPIES.              \n030394     IF SPCP-CENTERVIEW = \"1\"                                     \n030396         MOVE \"C\"                TO GWS-NPRT-CNTRV                \n030398     ELSE                                                         \n030400         MOVE \"I\"                TO GWS-NPRT-CNTRV.               \n030402     IF SPCP-REMOTE = \"1\"                                         \n030404         MOVE \"R\"                TO GWS-NPRT-RP                   \n030406     ELSE                                                         \n030408         MOVE \"0\"                TO GWS-NPRT-RP.                  \n030410 99-NEW-END.                                                      \n030412     IF GWS-CNTR-VIEW = 9                                         \n030414         MOVE 0                  TO GWS-NPRT-CNTRV.               \n030416     IF GWS-NPRT-PACK NOT = SPACES MOVE \" ON \" TO GWS-NPRT-ON     \n030418     ELSE MOVE SPACES            TO GWS-NPRT-ON.                  \n030420     MOVE GWS-A12-PERIOD         TO GWS-NPRT-PERIOD.              \n030422     IF (GWS-NEW-LABEL-1-36 = ID-PRT74-1-36)                      \n030424          GO TO 99-PRT-NEW-NAME-EXIT.                             \n030426     MOVE GWS-NEW-PRT-LABEL      TO ID-PRT74-2.                   \n030428     MOVE 1                      TO GWS-PREV-OPEN.                \n030430 99-PRT-NEW-NAME-EXIT.                                            \n030432     EXIT.                                                        \n030434                                                                  \n030436 99-PRT-NEW-LABEL-CHG                                 SECTION 51. \n030438 99-PRT-NEW-CHG.                                                  \n030440     FIND SPCPRT VIA FIRST SPCPRTCURR                             \n030442       AT SPCP-BANK = GWS-NP-BK AND                               \n030444          SPCP-APP = GWS-NP-APPL AND                              \n030446          SPCP-TYPE = GWS-NP-TYPE AND                             \n030448          SPCP-RPT-NUM = GWS-NP-RPT-NO ON EXCEPTION               \n030450          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             \n030452              GO TO 99-PRT-NEW-CHG-FIND2                          \n030454          ELSE                                                    \n030456              GO TO 99-PRT-NEW-CHG-EXIT.                          \n030458     GO TO 99-PRT-NEW-CHG-FOUND.                                  \n030460 99-PRT-NEW-CHG-FIND2.                                            \n030462     FIND SPCPRT VIA FIRST SPCPRTCURR                             \n030464       AT SPCP-BANK = GWS-NP-BK AND                               \n030466          SPCP-APP = GWS-NP-APPL AND                              \n030468          SPCP-TYPE = GWS-NP-TYPE AND                             \n030470          SPCP-RPT-NUM = \"    \" ON EXCEPTION                      \n030472          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             \n030474              GO TO 99-PRT-NEW-CHG-FIND3                          \n030476          ELSE                                                    \n030478              GO TO 99-PRT-NEW-CHG-EXIT.                          \n030480     GO TO 99-PRT-NEW-CHG-FOUND.                                  \n030482 99-PRT-NEW-CHG-FIND3.                                            \n030484     FIND SPCPRT VIA FIRST SPCPRTCURR                             \n030486       AT SPCP-BANK = GWS-NP-BK AND                               \n030488          SPCP-APP = GWS-NP-APPL AND                              \n030490          SPCP-TYPE = \"  \" AND                                    \n030492          SPCP-RPT-NUM = \"    \" ON EXCEPTION                      \n030494          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             \n030496              GO TO 99-PRT-NEW-CHG-FIND4                          \n030498          ELSE                                                    \n030500              GO TO 99-PRT-NEW-CHG-EXIT.                          \n030502     GO TO 99-PRT-NEW-CHG-FOUND.                                  \n030504 99-PRT-NEW-CHG-FIND4.                                            \n030506     FIND SPCPRT VIA FIRST SPCPRTCURR                             \n030508       AT SPCP-BANK = GWS-NP-BK AND                               \n030510          SPCP-APP = \"   \" AND                                    \n030512          SPCP-TYPE = GWS-NP-TYPE AND                             \n030514          SPCP-RPT-NUM = GWS-NP-RPT-NO ON EXCEPTION               \n030516          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             \n030518              GO TO 99-PRT-NEW-CHG-FIND5                          \n030520          ELSE                                                    \n030522              GO TO 99-PRT-NEW-CHG-EXIT.                          \n030524     GO TO 99-PRT-NEW-CHG-FOUND.                                  \n030526 99-PRT-NEW-CHG-FIND5.                                            \n030528     FIND SPCPRT VIA FIRST SPCPRTCURR                             \n030530       AT SPCP-BANK = GWS-NP-BK AND                               \n030532          SPCP-APP = \"   \" AND                                    \n030534          SPCP-TYPE = GWS-NP-TYPE AND                             \n030536          SPCP-RPT-NUM = \"    \" ON EXCEPTION                      \n030538          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             \n030540              GO TO 99-PRT-NEW-CHG-FIND6                          \n030542          ELSE                                                    \n030544              GO TO 99-PRT-NEW-CHG-EXIT.                          \n030546     GO TO 99-PRT-NEW-CHG-FOUND.                                  \n030548 99-PRT-NEW-CHG-FIND6.                                            \n030550     FIND SPCPRT VIA FIRST SPCPRTCURR                             \n030552       AT SPCP-BANK = GWS-NP-BK AND                               \n030554          SPCP-APP = \"   \" AND                                    \n030556          SPCP-TYPE = \"  \" AND                                    \n030558          SPCP-RPT-NUM = \"    \" ON EXCEPTION                      \n030560          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             \n030562              GO TO 99-PRT-NEW-CHG-EXIT                           \n030564          ELSE                                                    \n030566              GO TO 99-PRT-NEW-CHG-EXIT.                          \n030568 99-PRT-NEW-CHG-FOUND.                                            \n030570     MOVE SPCP-NUM-COPIES        TO GWS-NP-COPIES.                \n030572     IF SPCP-CENTERVIEW = \"1\"                                     \n030574         MOVE \"C\"                TO GWS-NP-CNTRV                  \n030576     ELSE                                                         \n030578         MOVE \"I\"                TO GWS-NP-CNTRV.                 \n030580     IF SPCP-REMOTE = \"1\"                                         \n030582         MOVE \"R\"                TO GWS-NP-RP                     \n030584     ELSE                                                         \n030586         MOVE \"0\"                TO GWS-NP-RP.                    \n030588     IF GWS-CNTR-VIEW = 9                                         \n030590         MOVE 0                  TO GWS-NP-CNTRV.                 \n030592 99-PRT-NEW-CHG-EXIT.                                             \n030594     EXIT.                                                        \n030596 99-FOR-XGEN-EXIT.                                                \n030598 Z-7-END.\n030600     IF Z-EDIT-ERROR\n030602         GO TO Z-7-XIT.\n030604 Z-7-SKIP.\n030606     IF Z-EXIT-LEVEL NOT < 0\n030608         MOVE 0 TO Z-EXIT-CODE\n030610         MOVE 9999 TO Z-EXIT-LEVEL.\n030612 Z-7-XIT.\n030614     EXIT.\n030616*\n030618*****************************************************************\n030620*    PROCEDURE TPR-REMOTE-BANK\n030622*****************************************************************\n030624 Z-8-PROCEDURE.\n030626*\n030628     MOVE BANK-CSI-BR-CODE TO GWS-RMT-LBL-BR.\n030630     MOVE BANK-NO-3 TO GWS-RMT-LBL-BK.\n030632     MOVE GWS-PRT-DESCRIPTOR TO GWS-RMT-DESCRIPTOR.\n030634     IF GWS-MICROFICHE-CODE = \" \" OR \"0\"\n030636         NEXT SENTENCE ELSE\n030638         GO TO Z-8-4-1-ELSE.\n030640     IF GWS-RMT-DESCRIPTOR = \"SP\" OR \"ST\"\n030642         NEXT SENTENCE ELSE\n030644         GO TO Z-8-5-1-ELSE.\n030646     MOVE \"2\" TO GWS-RMT-FICHE-COPIES.\n030648     GO TO Z-8-5-ENDIF.\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    476 lines from 14845 to 15320.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 31, "total_chunks": 55, "start_line": 14845, "end_line": 15320, "line_count": 476}

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
- Source code length: 37558 characters

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
CHUNK 31 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 14845 to 15320 (476 lines)
Chunk Tokens (estimated): ~8,067
Actual Input Tokens: 9,473 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 14845-15320 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 31 of 55 chunks
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
      The source code below is only CHUNK 31 of 55.


=============================================================================
CHUNK 31 SOURCE CODE (Lines 14845-15320)
=============================================================================

```cobol
029698 99-PRT-LABEL-INIT.                                               
029700     ACCEPT PRT-OPEN-DATE FROM TODAYS-DATE.                       
029702     ACCEPT PRT-OPEN-TIME FROM TIME.                              
029704     MOVE PRT-OPEN-DD TO H-CSI-DD.                                
029706     MOVE PRT-OPEN-HHMM TO H-CSI-HHMM.                            
029708     IF SW3-1 AND GWS-PRT-PID-FLAG = 0                            
029710         MOVE 1 TO GWS-PRT-PID-FLAG                               
029712*        DISPLAY "ENTER PACK NAME FOR MICROFICHE PRINT FILES"     
029714*        ACCEPT GWS-PRT-PID-FICHE                                 
029716         DISPLAY "ENTER PACK NAME FOR PRINT FILES"                
029718         ACCEPT GWS-PRT-PID                                       
029720         MOVE GWS-PRT-PID TO GWS-PRT-PID-FICHE                    
029722*        DISPLAY "ENTER Y IF PRINT FILES ARE TO BE RELEASED"      
029724*        DISPLAY "AFTER EACH BANK"                                
029726         MOVE "Y" TO GWS-REL-DUMMY-AREA.                          
029728*        DISPLAY "ENTER N IF SPOOLER IS TO BE DISABLE"            
029730*        ACCEPT SPOOLER-ENABLE.                                   
029732*=============================================================    
029734*  NOTE : TO USE THE REMOTE FILE NAME SETUP REPLACE               
029736*         'PERFORM 99-PRT-REMOTE-LBL-CHK' WITH                    
029738*         'PERFORM 99-PRT-RMT-LBL-CHK' USING COPY REPLACING       
029740*         REFER TO PRINT RTN SETUP NARRATIVE FOR PROCEDURE        
029742*=============================================================    
029744     MOVE 0 TO Z-EXIT-CODE.
029746     MOVE 9999 TO Z-EXIT-LEVEL.
029748     IF GWS-LONG-PRTNAMES-NEW = 1 AND GWS-PRT-NEW = 1
029750         NEXT SENTENCE ELSE
029752         GO TO Z-7-1-1-ELSE.
029754         PERFORM 99-PRT-NEW-NAME-CHK                              
029756     GO TO Z-7-1-ENDIF.
029758 Z-7-1-1-ELSE.
029760     IF GWS-RMT-PRT-OPTION = 1
029762         NEXT SENTENCE ELSE
029764         GO TO Z-7-1-2-ELSE.
029766         PERFORM 99-PRT-REMOTE-LBL-CHK.                           
029768************ PERFORM TPR-REMOTE-BANK
029770     PERFORM Z-8-PROCEDURE THRU Z-8-XIT.
029772     IF  Z-EXIT-EDITEXIT
029774         GO TO Z-7-XIT.
029776     IF  Z-DMS2-ABORT-FLAG = 1
029778         GO TO Z-7-XIT.
029780     IF  Z-EXIT-LEVEL < 0
029782         GO TO Z-7-END.
029784*
029786         GO TO 99-PRT-LABEL-END.                                  
029788 Z-7-1-2-ELSE.
029790 Z-7-1-ENDIF.
029792     IF (GWS-CST-PERIOD = "0" OR SPACE)                           
029794         MOVE "0" TO GWS-CST-PERIOD.                              
029796     MOVE "/" TO GWS-SLASH. MOVE " ON " TO GWS-ON.                
029798     IF GWS-APPL = SPACES MOVE "CSI" TO GWS-APPL.                 
029800     IF GWS-FILE-TYPE = SPACE MOVE "P" TO GWS-FILE-TYPE.          
029802     IF GWS-NO-PARTS = SPACE MOVE "1" TO GWS-NO-PARTS.            
029804     IF GWS-PRT-DESCRIPTOR = SPACES                               
029806         MOVE "SP" TO GWS-PRT-DESCRIPTOR.                         
029808     IF GWS-BRANCH-CODE = SPACES MOVE "00" TO GWS-BRANCH-CODE.    
029810     IF GWS-MICROFICHE-CODE = SPACE MOVE 0 TO GWS-MICROFICHE-CODE.
029812     IF (GWS-MICROFICHE-CODE > ZERO) OR                           
029814         (GWS-MICROFICHE-CODE ALPHABETIC)                         
029816         IF  GWS-NO-PARTS = "1"                                   
029818             MOVE "A" TO GWS-NO-PARTS                             
029820             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
029822         ELSE                                                     
029824         IF  GWS-NO-PARTS = "2"                                   
029826             MOVE "B" TO GWS-NO-PARTS                             
029828             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
029830         ELSE                                                     
029832         IF  GWS-NO-PARTS = "3"                                   
029834             MOVE "C" TO GWS-NO-PARTS                             
029836             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
029838         ELSE                                                     
029840         IF  GWS-NO-PARTS = "4"                                   
029842             MOVE "D" TO GWS-NO-PARTS                             
029844             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
029846         ELSE                                                     
029848         IF  GWS-NO-PARTS = "5"                                   
029850             MOVE "E" TO GWS-NO-PARTS                             
029852             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
029854         ELSE                                                     
029856         IF  GWS-NO-PARTS = "6"                                   
029858             MOVE "F" TO GWS-NO-PARTS                             
029860             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
029862         ELSE                                                     
029864         IF  GWS-NO-PARTS = "7"                                   
029866             MOVE "G" TO GWS-NO-PARTS                             
029868             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
029870         ELSE                                                     
029872         IF  GWS-NO-PARTS = "8"                                   
029874             MOVE "H" TO GWS-NO-PARTS                             
029876             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
029878         ELSE                                                     
029880         IF  GWS-NO-PARTS = "9"                                   
029882             MOVE "I" TO GWS-NO-PARTS                             
029884             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
029886         ELSE                                                     
029888         IF  GWS-NO-PARTS = "0"                                   
029890             MOVE "0" TO GWS-NO-PARTS                             
029892             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
029894         ELSE                                                     
029896             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
029898     ELSE                                                         
029900         MOVE GWS-PRT-PID TO GWS-PACK.                            
029902     IF GWS-NO-PARTS = "{" MOVE "0" TO GWS-NO-PARTS.              
029904     IF GWS-BANK-NO-X = SPACES MOVE "000" TO GWS-BANK-NO-X.       
029906     IF (GWS-TIME-CTL = 0) AND (GWS-TIME NOT = SPACES)            
029908         ACCEPT GWS-TIME FROM TIME.                               
029910     IF GWS-TIME = "......" MOVE SPACES TO GWS-TIME.              
029912     IF GWS-BRANCH-CODE = ".." MOVE "00" TO GWS-BRANCH-CODE.      
029914     MOVE GWS-A12-PERIOD TO GWS-PERIOD GWS-RMT-PERIOD.            
029916     IF (GWS-LONG-PRTNAMES-NEW = 1) AND (GWS-PRT-NEW = 1)         
029918         GO TO 99-PRT-LABEL-END.                                  
029920     IF (GWS-RMT-PRT-OPTION = 1) AND (GWS-RMT-BK-FLAG = 1)        
029922         GO TO 99-PRT-LABEL-END.                                  
029924     IF GWS-LONG-PRTNAMES NOT = 0                                 
029926         GO TO 99-LONG-LABEL-CHK                                  
029928     ELSE                                                         
029930         MOVE SPACES TO GWS-LPRT-NAMES.                           
029932     IF GWS-PRT-REL-FLAG = "Y" MOVE SPACES TO ID-PRT74-2.         
029934     IF COBOL-74 AND ID-PRT74-1-15 = GWS-PRT-LABEL-1-15           
029936         GO TO 99-PRT-LABEL-END.                                  
029938     IF NOT COBOL-74 AND GWS-FAMILY = PRT-ID-FAMILY AND           
029940       GWS-MICRO-BANK = PRT-ID-ELEM1-4   GO TO 99-PRT-LABEL-END.  
029942     IF COBOL-74 MOVE GWS-PRINT-LABEL TO ID-PRT74-2 ELSE          
029944       MOVE GWS-PACK TO PRT-ID-PACK MOVE GWS-ELEM TO PRT-ID-ELEM  
029946       MOVE GWS-FAMILY TO PRT-ID-FAMILY.                          
029948     GO TO 99-PRT-LABEL-END.                                      
029950 99-LONG-LABEL-CHK.                                               
029952     MOVE "PRT" TO GWS-LPRT-CST.                                  
029954     IF GWS-LONG-PRTNAMES = 2                                     
029956         MOVE "EOM" TO GWS-LPRT-CST.                              
029958     IF GWS-LONG-PRTNAMES = 3                                     
029960         MOVE "EOY" TO GWS-LPRT-CST.                              
029962     MOVE GWS-CSI-BK TO GWS-LPRT-BK.                              
029964     MOVE GWS-CSI-DC TO GWS-LPRT-DC.                              
029966     MOVE GWS-APPL TO GWS-LPRT-APP.                               
029968     MOVE GWS-CST-PERIOD TO GWS-LPRT-PART-1.                      
029970     MOVE GWS-NO-PARTS TO GWS-LPRT-PART-2.                        
029972     MOVE GWS-PRT-DESCRIPTOR TO GWS-LPRT-TYPE.                    
029974     MOVE GWS-MICROFICHE-CODE TO GWS-LPRT-FICHE.                  
029976     MOVE GWS-TIME TO GWS-LPRT-TIMESTAMP.                         
029978     MOVE "/" TO GWS-LPRT-S1, GWS-LPRT-S2, GWS-LPRT-S3,           
029980       GWS-LPRT-S4, GWS-LPRT-S5.                                  
029982     MOVE GWS-ON TO GWS-LPRT-ON.                                  
029984     MOVE GWS-PACK TO GWS-LPRT-PACK.                              
029986     MOVE GWS-PERIOD TO GWS-LPRT-PERIOD.                          
029988     IF GWS-PRT-REL-FLAG = "Y"                                    
029990         MOVE SPACES TO ID-PRT74-2.                               
029992     IF (GWS-LPRT-PREFX = ID-PRT74-PREFX)                         
029994         GO TO 99-PRT-LABEL-END.                                  
029996     MOVE GWS-PRINT-LABEL-LONG TO ID-PRT74-2.                     
029998 99-PRT-LABEL-END.                                                
030000 99-PRT-LABEL-EXIT.                                               
030002*                                                                 
030004 99-PRT-REMOTE-LBL-CHK     SECTION 51.                            
030006 99-PRT-REMOTE-LBL-INIT.                                          
030008     EXIT.                                                        
030010*=================================================================
030012 99-PRT-EXCEPT-RTN                                    SECTION 00. 
030014 99-PRT-EXC-REC.                                                  
030016     IF GWS-PRT-EXC-BLOCK-CTL = 97 OR 95                          
030018         MOVE 0 TO HDR-CTL.                                       
030020     MOVE GWS-PRT-EXC-PAGE-CTL TO PAGE-ADVANCE.                   
030022     MOVE GWS-PRT-EXC-NO-LINES TO NO-LINES.                       
030024     MOVE GWS-PRT-EXC-DATA     TO PRINT-LINE.                     
030026 99-PRT-EXC-CREATE-REC.                                           
030028     IF GWS-PRT-EXC-BLOCK-CTL NOT = 97                            
030030         MOVE 98           TO GWS-PRT-EXC-BLOCK-CTL.              
030032     MOVE PAGE-ADVANCE     TO GWS-PRT-EXC-PAGE-CTL.               
030034     MOVE NO-LINES         TO GWS-PRT-EXC-NO-LINES.               
030036     MOVE PRINT-LINE       TO GWS-PRT-EXC-DATA.                   
030038*L                                                                
030040*L"S"/"GEN.L"/"RMTPRTLBL".                                        
030042 99-PRT-NEW-NAME-CHK                                  SECTION 51. 
030044 99-PRT-NEW-NAME.                                                 
030046     MOVE 0 TO GWS-CTR, GWS-RMT-BK-FLAG, GWS-RPT-TYPE.            
030048     IF GWS-APPL = SPACES                                         
030050         MOVE "CSI"              TO GWS-APPL.                     
030052     IF GWS-NO-PARTS = SPACES                                     
030054         MOVE "1"                TO GWS-NO-PARTS.                 
030056     MOVE "PRINT"                TO GWS-NPRT-CST.                 
030058     MOVE "/"        TO GWS-NPRT-S1, GWS-NPRT-S2, GWS-NPRT-S3,    
030060                        GWS-NPRT-S4, GWS-NPRT-S5, GWS-NPRT-S6.    
030062     MOVE GWS-CSI-BK             TO GWS-NPRT-BK.                  
030064     MOVE GWS-CSI-DC             TO GWS-NPRT-DC.                  
030066     MOVE GWS-APPL               TO GWS-NPRT-APP.                 
030068     MOVE GWS-PRT-DESCRIPTOR     TO GWS-NPRT-TYPE, GWS-NPRT-TYPE2.
030070     MOVE 01                     TO GWS-NPRT-COPIES.              
030072     MOVE 00                     TO GWS-NPRT-EXP.                 
030074     MOVE H-DD                   TO GWS-NPRT-DD.                  
030076     MOVE GWS-RMT-EXT            TO GWS-NPRT-RPT-NO.              
030078     MOVE 0                      TO GWS-NPRT-RP.                  
030080     MOVE "I"                    TO GWS-NPRT-CNTRV.               
030082     MOVE GWS-APPL               TO GWS-RMT-WORK-APPL.            
030084     IF GWS-RMT-WORK-APPL = "ACH" MOVE "H" TO GWS-NPRT-APP2       
030086     ELSE IF GWS-RMT-WORK-APPL = "ATM" MOVE "A" TO GWS-NPRT-APP2  
030088     ELSE IF GWS-RMT-WORK-APPL = "BDS" MOVE "B" TO GWS-NPRT-APP2  
030090     ELSE IF GWS-RMT-WORK-APPL = "CSI" MOVE "Z" TO GWS-NPRT-APP2  
030092     ELSE IF GWS-RMT-WORK-APPL = "CLN" MOVE "L" TO GWS-NPRT-APP2  
030094     ELSE IF GWS-RMT-WORK-APPL = "CIF" MOVE "K" TO GWS-NPRT-APP2  
030096     ELSE IF GWS-RMT-WORK-APPL = "CLB" MOVE "X" TO GWS-NPRT-APP2  
030098     ELSE IF GWS-RMT-WORK-APPL = "CKR" MOVE "J" TO GWS-NPRT-APP2  
030100     ELSE IF GWS-RMT-WORK-APPL = "COD" MOVE "C" TO GWS-NPRT-APP2  
030102     ELSE IF GWS-RMT-WORK-APPL = "DDA" MOVE "D" TO GWS-NPRT-APP2  
030104     ELSE IF GWS-RMT-WORK-APPL = "FLP" MOVE "Y" TO GWS-NPRT-APP2  
030106     ELSE IF GWS-RMT-WORK-APPL = "GNL" OR "GL2"                   
030108                                       MOVE "G" TO GWS-NPRT-APP2  
030110     ELSE IF GWS-RMT-WORK-APPL = "ILN" MOVE "I" TO GWS-NPRT-APP2  
030112     ELSE IF GWS-RMT-WORK-APPL = "IRA" MOVE "R" TO GWS-NPRT-APP2  
030114     ELSE IF GWS-RMT-WORK-APPL = "MCR" MOVE "P" TO GWS-NPRT-APP2  
030116     ELSE IF GWS-RMT-WORK-APPL = "ONL" MOVE "O" TO GWS-NPRT-APP2  
030118     ELSE IF GWS-RMT-WORK-APPL = "PAY" MOVE "W" TO GWS-NPRT-APP2  
030120     ELSE IF GWS-RMT-WORK-APPL = "SAV" MOVE "S" TO GWS-NPRT-APP2  
030122     ELSE IF GWS-RMT-WORK-APPL = "SDB" MOVE "Q" TO GWS-NPRT-APP2  
030124     ELSE IF GWS-RMT-WORK-APPL = "STH" MOVE "H" TO GWS-NPRT-APP2  
030126     ELSE IF GWS-RMT-WORK-APPL = "TFR" MOVE "T" TO GWS-NPRT-APP2  
030128     ELSE IF GWS-RMT-WORK-APPL = "TDA" MOVE "N" TO GWS-NPRT-APP2  
030130     ELSE IF GWS-RMT-WORK-APPL = "TKL" MOVE "U" TO GWS-NPRT-APP2  
030132     ELSE IF GWS-RMT-WORK-APPL = "EOY" MOVE "E" TO GWS-NPRT-APP2  
030134     ELSE MOVE GWS-RMT-WORK-APPL-1X  TO GWS-NPRT-APP2.            
030136     IF GWS-CNTR-VIEW = 0                                         
030138         MOVE "I"                TO GWS-NPRT-CNTRV                
030140     ELSE                                                         
030142         MOVE "C"                TO GWS-NPRT-CNTRV                
030144         IF GWS-CNTR-VIEW = 2 OR 3                                
030146              MOVE "R"           TO GWS-NPRT-RP.                  
030148     IF (GWS-MICROFICHE-CODE > ZERO) OR                           
030150         (GWS-MICROFICHE-CODE ALPHABETIC)                         
030152         IF  GWS-NO-PARTS = "1"                                   
030154             MOVE "A" TO GWS-NO-PARTS                             
030156             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
030158         ELSE                                                     
030160         IF  GWS-NO-PARTS = "2"                                   
030162             MOVE "B" TO GWS-NO-PARTS                             
030164             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
030166         ELSE                                                     
030168         IF  GWS-NO-PARTS = "3"                                   
030170             MOVE "C" TO GWS-NO-PARTS                             
030172             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
030174         ELSE                                                     
030176         IF  GWS-NO-PARTS = "4"                                   
030178             MOVE "D" TO GWS-NO-PARTS                             
030180             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
030182         ELSE                                                     
030184         IF  GWS-NO-PARTS = "5"                                   
030186             MOVE "E" TO GWS-NO-PARTS                             
030188             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
030190         ELSE                                                     
030192         IF  GWS-NO-PARTS = "6"                                   
030194             MOVE "F" TO GWS-NO-PARTS                             
030196             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
030198         ELSE                                                     
030200         IF  GWS-NO-PARTS = "7"                                   
030202             MOVE "G" TO GWS-NO-PARTS                             
030204             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
030206         ELSE                                                     
030208         IF  GWS-NO-PARTS = "8"                                   
030210             MOVE "H" TO GWS-NO-PARTS                             
030212             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
030214         ELSE                                                     
030216         IF  GWS-NO-PARTS = "9"                                   
030218             MOVE "I" TO GWS-NO-PARTS                             
030220             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
030222         ELSE                                                     
030224         IF  GWS-NO-PARTS = "0"                                   
030226             MOVE "0" TO GWS-NO-PARTS                             
030228             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
030230         ELSE                                                     
030232             MOVE GWS-PRT-PID-FICHE TO GWS-PACK                   
030234     ELSE                                                         
030236         MOVE GWS-PRT-PID TO GWS-PACK.                            
030238     MOVE GWS-PACK TO GWS-NPRT-PACK.                              
030240     IF ( ( WS-SYS-HOST = "CSIA" ) OR ( WS-SYS-HOST = "CSID" ) OR 
030242         ( WS-SYS-HOST = "CSIB" ) )
030244         NEXT SENTENCE ELSE
030246         GO TO Z-7-3-1-ELSE.
030248     GO TO Z-7-3-ENDIF.
030250 Z-7-3-1-ELSE.
030252     MOVE SPACES TO GWS-NPRT-PACK.
030254     MOVE SPACES TO GWS-PACK.
030256 Z-7-3-ENDIF.
030258     IF WS-DMS-ERROR = 5                                          
030260         GO TO 99-NEW-END.                                        
030262     FIND SPCPRT VIA FIRST SPCPRTCURR                             
030264       AT SPCP-BANK = GWS-CSI-BK AND                              
030266          SPCP-APP = GWS-APPL AND                                 
030268          SPCP-TYPE = GWS-PRT-DESCRIPTOR AND                      
030270          SPCP-RPT-NUM = GWS-RMT-EXT ON EXCEPTION                 
030272          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             
030274              GO TO 99-PRT-NEW-FIND2                              
030276          ELSE                                                    
030278              GO TO 99-NEW-END.                                   
030280     GO TO 99-PRT-NEW-FOUND.                                      
030282 99-PRT-NEW-FIND2.                                                
030284     FIND SPCPRT VIA FIRST SPCPRTCURR                             
030286       AT SPCP-BANK = GWS-CSI-BK AND                              
030288          SPCP-APP = GWS-APPL AND                                 
030290          SPCP-TYPE = GWS-PRT-DESCRIPTOR AND                      
030292          SPCP-RPT-NUM = "   " ON EXCEPTION                       
030294          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             
030296              GO TO 99-PRT-NEW-FIND3                              
030298          ELSE                                                    
030300              GO TO 99-NEW-END.                                   
030302     GO TO 99-PRT-NEW-FOUND.                                      
030304 99-PRT-NEW-FIND3.                                                
030306     FIND SPCPRT VIA FIRST SPCPRTCURR                             
030308       AT SPCP-BANK = GWS-CSI-BK AND                              
030310          SPCP-APP = GWS-APPL AND                                 
030312          SPCP-TYPE = "  " AND                                    
030314          SPCP-RPT-NUM = "   " ON EXCEPTION                       
030316          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             
030318              GO TO 99-PRT-NEW-FIND4                              
030320          ELSE                                                    
030322              GO TO 99-NEW-END.                                   
030324     GO TO 99-PRT-NEW-FOUND.                                      
030326 99-PRT-NEW-FIND4.                                                
030328     FIND SPCPRT VIA FIRST SPCPRTCURR                             
030330       AT SPCP-BANK = GWS-CSI-BK AND                              
030332          SPCP-APP = "   " AND                                    
030334          SPCP-TYPE = GWS-PRT-DESCRIPTOR AND                      
030336          SPCP-RPT-NUM = GWS-RMT-EXT ON EXCEPTION                 
030338          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             
030340              GO TO 99-PRT-NEW-FIND5                              
030342          ELSE                                                    
030344              GO TO 99-NEW-END.                                   
030346     GO TO 99-PRT-NEW-FOUND.                                      
030348 99-PRT-NEW-FIND5.                                                
030350     FIND SPCPRT VIA FIRST SPCPRTCURR                             
030352       AT SPCP-BANK = GWS-CSI-BK AND                              
030354          SPCP-APP = "   " AND                                    
030356          SPCP-TYPE = GWS-PRT-DESCRIPTOR AND                      
030358          SPCP-RPT-NUM = "   " ON EXCEPTION                       
030360          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             
030362              GO TO 99-PRT-NEW-FIND6                              
030364          ELSE                                                    
030366              GO TO 99-NEW-END.                                   
030368     GO TO 99-PRT-NEW-FOUND.                                      
030370 99-PRT-NEW-FIND6.                                                
030372     FIND SPCPRT VIA FIRST SPCPRTCURR                             
030374       AT SPCP-BANK = GWS-CSI-BK AND                              
030376          SPCP-APP = "   " AND                                    
030378          SPCP-TYPE = "  " AND                                    
030380          SPCP-RPT-NUM = "   " ON EXCEPTION                       
030382          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             
030384              GO TO 99-NEW-END                                    
030386          ELSE                                                    
030388              GO TO 99-NEW-END.                                   
030390 99-PRT-NEW-FOUND.                                                
030392     MOVE SPCP-NUM-COPIES        TO GWS-NPRT-COPIES.              
030394     IF SPCP-CENTERVIEW = "1"                                     
030396         MOVE "C"                TO GWS-NPRT-CNTRV                
030398     ELSE                                                         
030400         MOVE "I"                TO GWS-NPRT-CNTRV.               
030402     IF SPCP-REMOTE = "1"                                         
030404         MOVE "R"                TO GWS-NPRT-RP                   
030406     ELSE                                                         
030408         MOVE "0"                TO GWS-NPRT-RP.                  
030410 99-NEW-END.                                                      
030412     IF GWS-CNTR-VIEW = 9                                         
030414         MOVE 0                  TO GWS-NPRT-CNTRV.               
030416     IF GWS-NPRT-PACK NOT = SPACES MOVE " ON " TO GWS-NPRT-ON     
030418     ELSE MOVE SPACES            TO GWS-NPRT-ON.                  
030420     MOVE GWS-A12-PERIOD         TO GWS-NPRT-PERIOD.              
030422     IF (GWS-NEW-LABEL-1-36 = ID-PRT74-1-36)                      
030424          GO TO 99-PRT-NEW-NAME-EXIT.                             
030426     MOVE GWS-NEW-PRT-LABEL      TO ID-PRT74-2.                   
030428     MOVE 1                      TO GWS-PREV-OPEN.                
030430 99-PRT-NEW-NAME-EXIT.                                            
030432     EXIT.                                                        
030434                                                                  
030436 99-PRT-NEW-LABEL-CHG                                 SECTION 51. 
030438 99-PRT-NEW-CHG.                                                  
030440     FIND SPCPRT VIA FIRST SPCPRTCURR                             
030442       AT SPCP-BANK = GWS-NP-BK AND                               
030444          SPCP-APP = GWS-NP-APPL AND                              
030446          SPCP-TYPE = GWS-NP-TYPE AND                             
030448          SPCP-RPT-NUM = GWS-NP-RPT-NO ON EXCEPTION               
030450          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             
030452              GO TO 99-PRT-NEW-CHG-FIND2                          
030454          ELSE                                                    
030456              GO TO 99-PRT-NEW-CHG-EXIT.                          
030458     GO TO 99-PRT-NEW-CHG-FOUND.                                  
030460 99-PRT-NEW-CHG-FIND2.                                            
030462     FIND SPCPRT VIA FIRST SPCPRTCURR                             
030464       AT SPCP-BANK = GWS-NP-BK AND                               
030466          SPCP-APP = GWS-NP-APPL AND                              
030468          SPCP-TYPE = GWS-NP-TYPE AND                             
030470          SPCP-RPT-NUM = "    " ON EXCEPTION                      
030472          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             
030474              GO TO 99-PRT-NEW-CHG-FIND3                          
030476          ELSE                                                    
030478              GO TO 99-PRT-NEW-CHG-EXIT.                          
030480     GO TO 99-PRT-NEW-CHG-FOUND.                                  
030482 99-PRT-NEW-CHG-FIND3.                                            
030484     FIND SPCPRT VIA FIRST SPCPRTCURR                             
030486       AT SPCP-BANK = GWS-NP-BK AND                               
030488          SPCP-APP = GWS-NP-APPL AND                              
030490          SPCP-TYPE = "  " AND                                    
030492          SPCP-RPT-NUM = "    " ON EXCEPTION                      
030494          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             
030496              GO TO 99-PRT-NEW-CHG-FIND4                          
030498          ELSE                                                    
030500              GO TO 99-PRT-NEW-CHG-EXIT.                          
030502     GO TO 99-PRT-NEW-CHG-FOUND.                                  
030504 99-PRT-NEW-CHG-FIND4.                                            
030506     FIND SPCPRT VIA FIRST SPCPRTCURR                             
030508       AT SPCP-BANK = GWS-NP-BK AND                               
030510          SPCP-APP = "   " AND                                    
030512          SPCP-TYPE = GWS-NP-TYPE AND                             
030514          SPCP-RPT-NUM = GWS-NP-RPT-NO ON EXCEPTION               
030516          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             
030518              GO TO 99-PRT-NEW-CHG-FIND5                          
030520          ELSE                                                    
030522              GO TO 99-PRT-NEW-CHG-EXIT.                          
030524     GO TO 99-PRT-NEW-CHG-FOUND.                                  
030526 99-PRT-NEW-CHG-FIND5.                                            
030528     FIND SPCPRT VIA FIRST SPCPRTCURR                             
030530       AT SPCP-BANK = GWS-NP-BK AND                               
030532          SPCP-APP = "   " AND                                    
030534          SPCP-TYPE = GWS-NP-TYPE AND                             
030536          SPCP-RPT-NUM = "    " ON EXCEPTION                      
030538          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             
030540              GO TO 99-PRT-NEW-CHG-FIND6                          
030542          ELSE                                                    
030544              GO TO 99-PRT-NEW-CHG-EXIT.                          
030546     GO TO 99-PRT-NEW-CHG-FOUND.                                  
030548 99-PRT-NEW-CHG-FIND6.                                            
030550     FIND SPCPRT VIA FIRST SPCPRTCURR                             
030552       AT SPCP-BANK = GWS-NP-BK AND                               
030554          SPCP-APP = "   " AND                                    
030556          SPCP-TYPE = "  " AND                                    
030558          SPCP-RPT-NUM = "    " ON EXCEPTION                      
030560          IF DMSTATUS(NOTFOUND) OR DMSTATUS(NORECORD)             
030562              GO TO 99-PRT-NEW-CHG-EXIT                           
030564          ELSE                                                    
030566              GO TO 99-PRT-NEW-CHG-EXIT.                          
030568 99-PRT-NEW-CHG-FOUND.                                            
030570     MOVE SPCP-NUM-COPIES        TO GWS-NP-COPIES.                
030572     IF SPCP-CENTERVIEW = "1"                                     
030574         MOVE "C"                TO GWS-NP-CNTRV                  
030576     ELSE                                                         
030578         MOVE "I"                TO GWS-NP-CNTRV.                 
030580     IF SPCP-REMOTE = "1"                                         
030582         MOVE "R"                TO GWS-NP-RP                     
030584     ELSE                                                         
030586         MOVE "0"                TO GWS-NP-RP.                    
030588     IF GWS-CNTR-VIEW = 9                                         
030590         MOVE 0                  TO GWS-NP-CNTRV.                 
030592 99-PRT-NEW-CHG-EXIT.                                             
030594     EXIT.                                                        
030596 99-FOR-XGEN-EXIT.                                                
030598 Z-7-END.
030600     IF Z-EDIT-ERROR
030602         GO TO Z-7-XIT.
030604 Z-7-SKIP.
030606     IF Z-EXIT-LEVEL NOT < 0
030608         MOVE 0 TO Z-EXIT-CODE
030610         MOVE 9999 TO Z-EXIT-LEVEL.
030612 Z-7-XIT.
030614     EXIT.
030616*
030618*****************************************************************
030620*    PROCEDURE TPR-REMOTE-BANK
030622*****************************************************************
030624 Z-8-PROCEDURE.
030626*
030628     MOVE BANK-CSI-BR-CODE TO GWS-RMT-LBL-BR.
030630     MOVE BANK-NO-3 TO GWS-RMT-LBL-BK.
030632     MOVE GWS-PRT-DESCRIPTOR TO GWS-RMT-DESCRIPTOR.
030634     IF GWS-MICROFICHE-CODE = " " OR "0"
030636         NEXT SENTENCE ELSE
030638         GO TO Z-8-4-1-ELSE.
030640     IF GWS-RMT-DESCRIPTOR = "SP" OR "ST"
030642         NEXT SENTENCE ELSE
030644         GO TO Z-8-5-1-ELSE.
030646     MOVE "2" TO GWS-RMT-FICHE-COPIES.
030648     GO TO Z-8-5-ENDIF.
```

⚠️  This is the source code you must document.
    476 lines from 14845 to 15320.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

