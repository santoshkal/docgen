# LLM Request Debug File
Generated: 2025-11-18T20:46:01.076283

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 52/55
- **Model**: gpt-4.1
- **Chunk Number**: 52
- **Pass Number**: 3
- **Attempt Number**: 4 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,086 tokens
- **User Prompt**: ~6,973 tokens
- **Total Input**: ~9,059 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 52/55" (ID: detailed-code-explanation)

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


**CHUNK 52 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T18:05:37.383587", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 52 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 24926 to 25459 (534 lines)\nChunk Tokens (estimated): ~8,086\nActual Input Tokens: 9,492 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 24926-25459 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 52 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 52 of 55.\n\n\n=============================================================================\nCHUNK 52 SOURCE CODE (Lines 24926-25459)\n=============================================================================\n\n```cobol\n049860 Z-35-2-20-ELSE.\n049862     IF HOLD-TDA-ACTVC-CODE = 0030\n049864         NEXT SENTENCE ELSE\n049866         GO TO Z-35-2-21-ELSE.\n049868     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-CMPD-FREQ.\n049870     GO TO Z-35-2-ENDIF.\n049872 Z-35-2-21-ELSE.\n049874     IF HOLD-TDA-ACTVC-CODE = 0031\n049876         NEXT SENTENCE ELSE\n049878         GO TO Z-35-2-22-ELSE.\n049880     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-CURR-BAL.\n049882     GO TO Z-35-2-ENDIF.\n049884 Z-35-2-22-ELSE.\n049886     IF HOLD-TDA-ACTVC-CODE = 0032\n049888         NEXT SENTENCE ELSE\n049890         GO TO Z-35-2-23-ELSE.\n049892     MOVE WS-CHG-WK-9-4 TO HOLD-TDAA-CMPD-NTRVL.\n049894     GO TO Z-35-2-ENDIF.\n049896 Z-35-2-23-ELSE.\n049898     IF HOLD-TDA-ACTVC-CODE = 0033\n049900         NEXT SENTENCE ELSE\n049902         GO TO Z-35-2-24-ELSE.\n049904     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-VAR-RT-IMMED.\n049906     GO TO Z-35-2-ENDIF.\n049908 Z-35-2-24-ELSE.\n049910     IF HOLD-TDA-ACTVC-CODE = 0034\n049912         NEXT SENTENCE ELSE\n049914         GO TO Z-35-2-25-ELSE.\n049916     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-VAR-RT-INT.\n049918     GO TO Z-35-2-ENDIF.\n049920 Z-35-2-25-ELSE.\n049922     IF HOLD-TDA-ACTVC-CODE = 0035\n049924         NEXT SENTENCE ELSE\n049926         GO TO Z-35-2-26-ELSE.\n049928     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-VAR-RT-SCHED.\n049930     GO TO Z-35-2-ENDIF.\n049932 Z-35-2-26-ELSE.\n049934     IF HOLD-TDA-ACTVC-CODE = 0036\n049936         NEXT SENTENCE ELSE\n049938         GO TO Z-35-2-27-ELSE.\n049940     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-VAR-RT-CUST.\n049942     GO TO Z-35-2-ENDIF.\n049944 Z-35-2-27-ELSE.\n049946     IF HOLD-TDA-ACTVC-CODE = 0037\n049948         NEXT SENTENCE ELSE\n049950         GO TO Z-35-2-28-ELSE.\n049952     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-VAR-RT-BAL.\n049954     GO TO Z-35-2-ENDIF.\n049956 Z-35-2-28-ELSE.\n049958     IF HOLD-TDA-ACTVC-CODE = 0038\n049960         NEXT SENTENCE ELSE\n049962         GO TO Z-35-2-29-ELSE.\n049964     MOVE WS-CHG-WK-9-4V2 TO HOLD-TDAA-CENSUS-TRACT.\n049966     GO TO Z-35-2-ENDIF.\n049968 Z-35-2-29-ELSE.\n049970     IF HOLD-TDA-ACTVC-CODE = 0039\n049972         NEXT SENTENCE ELSE\n049974         GO TO Z-35-2-30-ELSE.\n049976     MOVE WS-CHG-WK-X-2 TO HOLD-TDAA-MK-SEGMENT.\n049978     GO TO Z-35-2-ENDIF.\n049980 Z-35-2-30-ELSE.\n049982     IF HOLD-TDA-ACTVC-CODE = 0040\n049984         NEXT SENTENCE ELSE\n049986         GO TO Z-35-2-31-ELSE.\n049988     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-B-NOTC-YR1.\n049990     GO TO Z-35-2-ENDIF.\n049992 Z-35-2-31-ELSE.\n049994     IF HOLD-TDA-ACTVC-CODE = 0041\n049996         NEXT SENTENCE ELSE\n049998         GO TO Z-35-2-32-ELSE.\n050000     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-B-NOTC-YR2.\n050002     GO TO Z-35-2-ENDIF.\n050004 Z-35-2-32-ELSE.\n050006     IF HOLD-TDA-ACTVC-CODE = 0042\n050008         NEXT SENTENCE ELSE\n050010         GO TO Z-35-2-33-ELSE.\n050012     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-B-NOTC-YR3.\n050014     GO TO Z-35-2-ENDIF.\n050016 Z-35-2-33-ELSE.\n050018     IF HOLD-TDA-ACTVC-CODE = 0043\n050020         NEXT SENTENCE ELSE\n050022         GO TO Z-35-2-34-ELSE.\n050024     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-ODD-PAYMENT.\n050026     GO TO Z-35-2-ENDIF.\n050028 Z-35-2-34-ELSE.\n050030     IF HOLD-TDA-ACTVC-CODE = 0044\n050032         NEXT SENTENCE ELSE\n050034         GO TO Z-35-2-35-ELSE.\n050036     MOVE WS-CHG-WK-X-8 TO HOLD-TDAA-EMPLOYEE-ID.\n050038     GO TO Z-35-2-ENDIF.\n050040 Z-35-2-35-ELSE.\n050042     IF HOLD-TDA-ACTVC-CODE = 0045\n050044         NEXT SENTENCE ELSE\n050046         GO TO Z-35-2-36-ELSE.\n050048     MOVE WS-CHG-WK-9-6 TO HOLD-TDAA-DDA-ACCT-1-S.\n050050     GO TO Z-35-2-ENDIF.\n050052 Z-35-2-36-ELSE.\n050054     IF HOLD-TDA-ACTVC-CODE = 0046\n050056         NEXT SENTENCE ELSE\n050058         GO TO Z-35-2-37-ELSE.\n050060     MOVE WS-CHG-WK-9-6 TO HOLD-TDAA-DDA-ACCT-2-S.\n050062     GO TO Z-35-2-ENDIF.\n050064 Z-35-2-37-ELSE.\n050066     IF HOLD-TDA-ACTVC-CODE = 0047\n050068         NEXT SENTENCE ELSE\n050070         GO TO Z-35-2-38-ELSE.\n050072     MOVE WS-CHG-WK-9-6 TO HOLD-TDAA-DDA-ACCT-3-S.\n050074     GO TO Z-35-2-ENDIF.\n050076 Z-35-2-38-ELSE.\n050078     IF HOLD-TDA-ACTVC-CODE = 0048\n050080         NEXT SENTENCE ELSE\n050082         GO TO Z-35-2-39-ELSE.\n050084     MOVE WS-CHG-WK-9-6 TO HOLD-TDAA-INT-ACCT-S.\n050086     GO TO Z-35-2-ENDIF.\n050088 Z-35-2-39-ELSE.\n050090     IF HOLD-TDA-ACTVC-CODE = 0049\n050092         NEXT SENTENCE ELSE\n050094         GO TO Z-35-2-40-ELSE.\n050096     MOVE WS-CHG-WK-9-6 TO HOLD-TDAA-CS-ACCT-S.\n050098     GO TO Z-35-2-ENDIF.\n050100 Z-35-2-40-ELSE.\n050102     IF HOLD-TDA-ACTVC-CODE = 0050\n050104         NEXT SENTENCE ELSE\n050106         GO TO Z-35-2-41-ELSE.\n050108     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-RENEW-CD.\n050110     GO TO Z-35-2-ENDIF.\n050112 Z-35-2-41-ELSE.\n050114     IF HOLD-TDA-ACTVC-CODE = 0051\n050116         NEXT SENTENCE ELSE\n050118         GO TO Z-35-2-42-ELSE.\n050120     MOVE WS-CHG-WK-9-5 TO HOLD-TDAA-DAYS-IN-PER.\n050122     GO TO Z-35-2-ENDIF.\n050124 Z-35-2-42-ELSE.\n050126     IF HOLD-TDA-ACTVC-CODE = 0052\n050128         NEXT SENTENCE ELSE\n050130         GO TO Z-35-2-43-ELSE.\n050132     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-BEG-INT-BAL.\n050134     GO TO Z-35-2-ENDIF.\n050136 Z-35-2-43-ELSE.\n050138     IF HOLD-TDA-ACTVC-CODE = 0053\n050140         NEXT SENTENCE ELSE\n050142         GO TO Z-35-2-44-ELSE.\n050144     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-CLOSE-AMT.\n050146     GO TO Z-35-2-ENDIF.\n050148 Z-35-2-44-ELSE.\n050150     IF HOLD-TDA-ACTVC-CODE = 0054\n050152         NEXT SENTENCE ELSE\n050154         GO TO Z-35-2-45-ELSE.\n050156     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-MONEY-AMT.\n050158     GO TO Z-35-2-ENDIF.\n050160 Z-35-2-45-ELSE.\n050162     IF HOLD-TDA-ACTVC-CODE = 0055\n050164         NEXT SENTENCE ELSE\n050166         GO TO Z-35-2-46-ELSE.\n050168     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-CURR-INT-ADJ.\n050170     GO TO Z-35-2-ENDIF.\n050172 Z-35-2-46-ELSE.\n050174     IF HOLD-TDA-ACTVC-CODE = 0056\n050176         NEXT SENTENCE ELSE\n050178         GO TO Z-35-2-47-ELSE.\n050180     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-TOTAMT-HOLDS.\n050182     GO TO Z-35-2-ENDIF.\n050184 Z-35-2-47-ELSE.\n050186     IF HOLD-TDA-ACTVC-CODE = 0057\n050188         NEXT SENTENCE ELSE\n050190         GO TO Z-35-2-48-ELSE.\n050192     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-NXT-INT-ADJ.\n050194     GO TO Z-35-2-ENDIF.\n050196 Z-35-2-48-ELSE.\n050198     IF HOLD-TDA-ACTVC-CODE = 0058\n050200         NEXT SENTENCE ELSE\n050202         GO TO Z-35-2-49-ELSE.\n050204     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-FEE-AMT.\n050206     GO TO Z-35-2-ENDIF.\n050208 Z-35-2-49-ELSE.\n050210     IF HOLD-TDA-ACTVC-CODE = 0059\n050212         NEXT SENTENCE ELSE\n050214         GO TO Z-35-2-50-ELSE.\n050216     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-BEG-INT-RT.\n050218     GO TO Z-35-2-ENDIF.\n050220 Z-35-2-50-ELSE.\n050222     IF HOLD-TDA-ACTVC-CODE = 0060\n050224         NEXT SENTENCE ELSE\n050226         GO TO Z-35-2-51-ELSE.\n050228     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-YIELD-RT.\n050230     GO TO Z-35-2-ENDIF.\n050232 Z-35-2-51-ELSE.\n050234     IF HOLD-TDA-ACTVC-CODE = 0061\n050236         NEXT SENTENCE ELSE\n050238         GO TO Z-35-2-52-ELSE.\n050240     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-SCHED-DT.\n050242     GO TO Z-35-2-ENDIF.\n050244 Z-35-2-52-ELSE.\n050246     IF HOLD-TDA-ACTVC-CODE = 0062\n050248         NEXT SENTENCE ELSE\n050250         GO TO Z-35-2-53-ELSE.\n050252     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-MAT-DT.\n050254     GO TO Z-35-2-ENDIF.\n050256 Z-35-2-53-ELSE.\n050258     IF HOLD-TDA-ACTVC-CODE = 0063\n050260         NEXT SENTENCE ELSE\n050262         GO TO Z-35-2-54-ELSE.\n050264     MOVE WS-CHG-WK-9-10 TO HOLD-TDAA-CC-ACCT.\n050266     GO TO Z-35-2-ENDIF.\n050268 Z-35-2-54-ELSE.\n050270     IF HOLD-TDA-ACTVC-CODE = 0064\n050272         NEXT SENTENCE ELSE\n050274         GO TO Z-35-2-55-ELSE.\n050276     MOVE WS-CHG-WK-X-3 TO HOLD-TDAA-BK-DEF-TOT.\n050278     GO TO Z-35-2-ENDIF.\n050280 Z-35-2-55-ELSE.\n050282     IF HOLD-TDA-ACTVC-CODE = 0065\n050284         NEXT SENTENCE ELSE\n050286         GO TO Z-35-2-56-ELSE.\n050288     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-ALERT-CD.\n050290     GO TO Z-35-2-ENDIF.\n050292 Z-35-2-56-ELSE.\n050294     IF HOLD-TDA-ACTVC-CODE = 0067\n050296         NEXT SENTENCE ELSE\n050298         GO TO Z-35-2-57-ELSE.\n050300     MOVE WS-CHG-WK-9-S15V2 TO HOLD-TDAA-RMD-AMOUNT.\n050302     GO TO Z-35-2-ENDIF.\n050304 Z-35-2-57-ELSE.\n050306     IF HOLD-TDA-ACTVC-CODE = 0099\n050308         NEXT SENTENCE ELSE\n050310         GO TO Z-35-2-58-ELSE.\n050312     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-MAIL-CD.\n050314     GO TO Z-35-2-ENDIF.\n050316 Z-35-2-58-ELSE.\n050318     IF HOLD-TDA-ACTVC-CODE = 0110\n050320         NEXT SENTENCE ELSE\n050322         GO TO Z-35-2-59-ELSE.\n050324     MOVE WS-CHG-WK-9-7 TO HOLD-TDAA-CERT.\n050326     GO TO Z-35-2-ENDIF.\n050328 Z-35-2-59-ELSE.\n050330     IF HOLD-TDA-ACTVC-CODE = 0111\n050332         NEXT SENTENCE ELSE\n050334         GO TO Z-35-2-60-ELSE.\n050336     MOVE WS-CHG-WK-9-10 TO HOLD-TDAC-PHONE-1.\n050338     GO TO Z-35-2-ENDIF.\n050340 Z-35-2-60-ELSE.\n050342     IF HOLD-TDA-ACTVC-CODE = 0112\n050344         NEXT SENTENCE ELSE\n050346         GO TO Z-35-2-61-ELSE.\n050348     MOVE WS-CHG-WK-9-10 TO HOLD-TDAC-PHONE-2.\n050350     GO TO Z-35-2-ENDIF.\n050352 Z-35-2-61-ELSE.\n050354     IF HOLD-TDA-ACTVC-CODE = 0113\n050356         NEXT SENTENCE ELSE\n050358         GO TO Z-35-2-62-ELSE.\n050360     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-STATUS.\n050362     GO TO Z-35-2-ENDIF.\n050364 Z-35-2-62-ELSE.\n050366     IF HOLD-TDA-ACTVC-CODE = 0116\n050368         NEXT SENTENCE ELSE\n050370         GO TO Z-35-2-63-ELSE.\n050372     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-OVERRIDE.\n050374     GO TO Z-35-2-ENDIF.\n050376 Z-35-2-63-ELSE.\n050378     IF HOLD-TDA-ACTVC-CODE = 0117\n050380         NEXT SENTENCE ELSE\n050382         GO TO Z-35-2-64-ELSE.\n050384     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-COMM-MAT-CD.\n050386     GO TO Z-35-2-ENDIF.\n050388 Z-35-2-64-ELSE.\n050390     IF HOLD-TDA-ACTVC-CODE = 0118\n050392         NEXT SENTENCE ELSE\n050394         GO TO Z-35-2-65-ELSE.\n050396     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-BENEF-CD.\n050398     GO TO Z-35-2-ENDIF.\n050400 Z-35-2-65-ELSE.\n050402     IF HOLD-TDA-ACTVC-CODE = 0119\n050404         NEXT SENTENCE ELSE\n050406         GO TO Z-35-2-66-ELSE.\n050408     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-NBR-BENEF.\n050410     GO TO Z-35-2-ENDIF.\n050412 Z-35-2-66-ELSE.\n050414     IF HOLD-TDA-ACTVC-CODE = 0121\n050416         NEXT SENTENCE ELSE\n050418         GO TO Z-35-2-67-ELSE.\n050420     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-REN-NTC-CD.\n050422     GO TO Z-35-2-ENDIF.\n050424 Z-35-2-67-ELSE.\n050426     IF HOLD-TDA-ACTVC-CODE = 0122\n050428         NEXT SENTENCE ELSE\n050430         GO TO Z-35-2-68-ELSE.\n050432     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-RTCHG-NTC-CD.\n050434     GO TO Z-35-2-ENDIF.\n050436 Z-35-2-68-ELSE.\n050438     IF HOLD-TDA-ACTVC-CODE = 0123\n050440         NEXT SENTENCE ELSE\n050442         GO TO Z-35-2-69-ELSE.\n050444     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-INT-NTC-CD.\n050446     GO TO Z-35-2-ENDIF.\n050448 Z-35-2-69-ELSE.\n050450     IF HOLD-TDA-ACTVC-CODE = 0125\n050452         NEXT SENTENCE ELSE\n050454         GO TO Z-35-2-70-ELSE.\n050456     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-PURCH-AMT.\n050458     GO TO Z-35-2-ENDIF.\n050460 Z-35-2-70-ELSE.\n050462     IF HOLD-TDA-ACTVC-CODE = 0127\n050464         NEXT SENTENCE ELSE\n050466         GO TO Z-35-2-71-ELSE.\n050468     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-RT-CHG-LIMIT.\n050470     GO TO Z-35-2-ENDIF.\n050472 Z-35-2-71-ELSE.\n050474     IF HOLD-TDA-ACTVC-CODE = 0133\n050476         NEXT SENTENCE ELSE\n050478         GO TO Z-35-2-72-ELSE.\n050480     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-OPEN-DT.\n050482     GO TO Z-35-2-ENDIF.\n050484 Z-35-2-72-ELSE.\n050486     IF HOLD-TDA-ACTVC-CODE = 0134\n050488         NEXT SENTENCE ELSE\n050490         GO TO Z-35-2-73-ELSE.\n050492     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-ORG-YIELD-RT.\n050494     GO TO Z-35-2-ENDIF.\n050496 Z-35-2-73-ELSE.\n050498     IF HOLD-TDA-ACTVC-CODE = 0135\n050500         NEXT SENTENCE ELSE\n050502         GO TO Z-35-2-74-ELSE.\n050504     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-ORG-MAT-TYPE.\n050506     GO TO Z-35-2-ENDIF.\n050508 Z-35-2-74-ELSE.\n050510     IF HOLD-TDA-ACTVC-CODE = 0136\n050512         NEXT SENTENCE ELSE\n050514         GO TO Z-35-2-75-ELSE.\n050516     MOVE WS-CHG-WK-9-4 TO HOLD-TDAA-ORG-MAT-TERM.\n050518     GO TO Z-35-2-ENDIF.\n050520 Z-35-2-75-ELSE.\n050522     IF HOLD-TDA-ACTVC-CODE = 0141\n050524         NEXT SENTENCE ELSE\n050526         GO TO Z-35-2-76-ELSE.\n050528     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-BK-DEF-CD1.\n050530     GO TO Z-35-2-ENDIF.\n050532 Z-35-2-76-ELSE.\n050534     IF HOLD-TDA-ACTVC-CODE = 0142\n050536         NEXT SENTENCE ELSE\n050538         GO TO Z-35-2-77-ELSE.\n050540     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-BK-DEF-CD2.\n050542     GO TO Z-35-2-ENDIF.\n050544 Z-35-2-77-ELSE.\n050546     IF HOLD-TDA-ACTVC-CODE = 0143\n050548         NEXT SENTENCE ELSE\n050550         GO TO Z-35-2-78-ELSE.\n050552     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-BK-DEF-CD3.\n050554     GO TO Z-35-2-ENDIF.\n050556 Z-35-2-78-ELSE.\n050558     IF HOLD-TDA-ACTVC-CODE = 0144\n050560         NEXT SENTENCE ELSE\n050562         GO TO Z-35-2-79-ELSE.\n050564     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-BK-DEF-CD4.\n050566     GO TO Z-35-2-ENDIF.\n050568 Z-35-2-79-ELSE.\n050570     IF HOLD-TDA-ACTVC-CODE = 0145\n050572         NEXT SENTENCE ELSE\n050574         GO TO Z-35-2-80-ELSE.\n050576     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-BK-DEF-CD5.\n050578     GO TO Z-35-2-ENDIF.\n050580 Z-35-2-80-ELSE.\n050582     IF HOLD-TDA-ACTVC-CODE = 0146\n050584         NEXT SENTENCE ELSE\n050586         GO TO Z-35-2-81-ELSE.\n050588     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-OID-METH.\n050590     GO TO Z-35-2-ENDIF.\n050592 Z-35-2-81-ELSE.\n050594     IF HOLD-TDA-ACTVC-CODE = 0150\n050596         NEXT SENTENCE ELSE\n050598         GO TO Z-35-2-82-ELSE.\n050600     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-DISP-CD.\n050602     GO TO Z-35-2-ENDIF.\n050604 Z-35-2-82-ELSE.\n050606     IF HOLD-TDA-ACTVC-CODE = 0161\n050608         NEXT SENTENCE ELSE\n050610         GO TO Z-35-2-83-ELSE.\n050612     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-PAY-FREQ.\n050614     GO TO Z-35-2-ENDIF.\n050616 Z-35-2-83-ELSE.\n050618     IF HOLD-TDA-ACTVC-CODE = 0163\n050620         NEXT SENTENCE ELSE\n050622         GO TO Z-35-2-84-ELSE.\n050624     MOVE WS-CHG-WK-9-4 TO HOLD-TDAA-PAY-NTRVL.\n050626     GO TO Z-35-2-ENDIF.\n050628 Z-35-2-84-ELSE.\n050630     IF HOLD-TDA-ACTVC-CODE = 0165\n050632         NEXT SENTENCE ELSE\n050634         GO TO Z-35-2-85-ELSE.\n050636     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-STMT-FREQ.\n050638     GO TO Z-35-2-ENDIF.\n050640 Z-35-2-85-ELSE.\n050642     IF HOLD-TDA-ACTVC-CODE = 0166\n050644         NEXT SENTENCE ELSE\n050646         GO TO Z-35-2-86-ELSE.\n050648     MOVE WS-CHG-WK-9-4 TO HOLD-TDAA-STMT-NTRVL.\n050650     GO TO Z-35-2-ENDIF.\n050652 Z-35-2-86-ELSE.\n050654     IF HOLD-TDA-ACTVC-CODE = 0189\n050656         NEXT SENTENCE ELSE\n050658         GO TO Z-35-2-87-ELSE.\n050660     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-MAT-TYPE.\n050662     GO TO Z-35-2-ENDIF.\n050664 Z-35-2-87-ELSE.\n050666     IF HOLD-TDA-ACTVC-CODE = 0192\n050668         NEXT SENTENCE ELSE\n050670         GO TO Z-35-2-88-ELSE.\n050672     MOVE WS-CHG-WK-9-4 TO HOLD-TDAA-MAT-TERM.\n050674     GO TO Z-35-2-ENDIF.\n050676 Z-35-2-88-ELSE.\n050678     IF HOLD-TDA-ACTVC-CODE = 0220\n050680         NEXT SENTENCE ELSE\n050682         GO TO Z-35-2-89-ELSE.\n050684     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-YIELD-NUM.\n050686     GO TO Z-35-2-ENDIF.\n050688 Z-35-2-89-ELSE.\n050690     IF HOLD-TDA-ACTVC-CODE = 0222\n050692         NEXT SENTENCE ELSE\n050694         GO TO Z-35-2-90-ELSE.\n050696     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-DIST-STATUS.\n050698     GO TO Z-35-2-ENDIF.\n050700 Z-35-2-90-ELSE.\n050702     IF HOLD-TDA-ACTVC-CODE = 0231\n050704         NEXT SENTENCE ELSE\n050706         GO TO Z-35-2-91-ELSE.\n050708     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-PLEDGE-CD.\n050710     GO TO Z-35-2-ENDIF.\n050712 Z-35-2-91-ELSE.\n050714     IF HOLD-TDA-ACTVC-CODE = 0236\n050716         NEXT SENTENCE ELSE\n050718         GO TO Z-35-2-92-ELSE.\n050720     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-NEGOT-CD.\n050722     GO TO Z-35-2-ENDIF.\n050724 Z-35-2-92-ELSE.\n050726     IF HOLD-TDA-ACTVC-CODE = 0237\n050728         NEXT SENTENCE ELSE\n050730         GO TO Z-35-2-93-ELSE.\n050732     MOVE WS-CHG-WK-9-10 TO HOLD-TDAA-DDA-ACCT-1.\n050734     GO TO Z-35-2-ENDIF.\n050736 Z-35-2-93-ELSE.\n050738     IF HOLD-TDA-ACTVC-CODE = 0238\n050740         NEXT SENTENCE ELSE\n050742         GO TO Z-35-2-94-ELSE.\n050744     MOVE WS-CHG-WK-9-10 TO HOLD-TDAA-DDA-ACCT-2.\n050746     GO TO Z-35-2-ENDIF.\n050748 Z-35-2-94-ELSE.\n050750     IF HOLD-TDA-ACTVC-CODE = 0239\n050752         NEXT SENTENCE ELSE\n050754         GO TO Z-35-2-95-ELSE.\n050756     MOVE WS-CHG-WK-9-10 TO HOLD-TDAA-DDA-ACCT-3.\n050758     GO TO Z-35-2-ENDIF.\n050760 Z-35-2-95-ELSE.\n050762     IF HOLD-TDA-ACTVC-CODE = 0240\n050764         NEXT SENTENCE ELSE\n050766         GO TO Z-35-2-96-ELSE.\n050768     MOVE WS-CHG-WK-9-10 TO HOLD-TDAA-INT-ACCT.\n050770     GO TO Z-35-2-ENDIF.\n050772 Z-35-2-96-ELSE.\n050774     IF HOLD-TDA-ACTVC-CODE = 0244\n050776         NEXT SENTENCE ELSE\n050778         GO TO Z-35-2-97-ELSE.\n050780     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-CUR-INT-RT.\n050782     GO TO Z-35-2-ENDIF.\n050784 Z-35-2-97-ELSE.\n050786     IF HOLD-TDA-ACTVC-CODE = 0246\n050788         NEXT SENTENCE ELSE\n050790         GO TO Z-35-2-98-ELSE.\n050792     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-RT-INDX-CD.\n050794     GO TO Z-35-2-ENDIF.\n050796 Z-35-2-98-ELSE.\n050798     IF HOLD-TDA-ACTVC-CODE = 0247\n050800         NEXT SENTENCE ELSE\n050802         GO TO Z-35-2-99-ELSE.\n050804     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-RT-REGN-CD.\n050806     GO TO Z-35-2-ENDIF.\n050808 Z-35-2-99-ELSE.\n050810     IF HOLD-TDA-ACTVC-CODE = 0248\n050812         NEXT SENTENCE ELSE\n050814         GO TO Z-35-2-100-ELSE.\n050816     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-RT-TIER-CD.\n050818     GO TO Z-35-2-ENDIF.\n050820 Z-35-2-100-ELSE.\n050822     IF HOLD-TDA-ACTVC-CODE = 0249\n050824         NEXT SENTENCE ELSE\n050826         GO TO Z-35-2-101-ELSE.\n050828     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-YIELD-DENOM.\n050830     GO TO Z-35-2-ENDIF.\n050832 Z-35-2-101-ELSE.\n050834     IF HOLD-TDA-ACTVC-CODE = 0250\n050836         NEXT SENTENCE ELSE\n050838         GO TO Z-35-2-102-ELSE.\n050840     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-RT-SR-CD.\n050842     GO TO Z-35-2-ENDIF.\n050844 Z-35-2-102-ELSE.\n050846     IF HOLD-TDA-ACTVC-CODE = 0251\n050848         NEXT SENTENCE ELSE\n050850         GO TO Z-35-2-103-ELSE.\n050852     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-RT-MARG-CD.\n050854     GO TO Z-35-2-ENDIF.\n050856 Z-35-2-103-ELSE.\n050858     IF HOLD-TDA-ACTVC-CODE = 0252\n050860         NEXT SENTENCE ELSE\n050862         GO TO Z-35-2-104-ELSE.\n050864     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-RT-CHG-NTRVL.\n050866     GO TO Z-35-2-ENDIF.\n050868 Z-35-2-104-ELSE.\n050870     IF HOLD-TDA-ACTVC-CODE = 0260\n050872         NEXT SENTENCE ELSE\n050874         GO TO Z-35-2-105-ELSE.\n050876     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-TOTAL-CD.\n050878     GO TO Z-35-2-ENDIF.\n050880 Z-35-2-105-ELSE.\n050882     IF HOLD-TDA-ACTVC-CODE = 0262\n050884         NEXT SENTENCE ELSE\n050886         GO TO Z-35-2-106-ELSE.\n050888     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-REN-TOTAL-CD.\n050890     GO TO Z-35-2-ENDIF.\n050892 Z-35-2-106-ELSE.\n050894     IF HOLD-TDA-ACTVC-CODE = 0263\n050896         NEXT SENTENCE ELSE\n050898         GO TO Z-35-2-107-ELSE.\n050900     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-REN-YIELD-RT.\n050902     GO TO Z-35-2-ENDIF.\n050904 Z-35-2-107-ELSE.\n050906     IF HOLD-TDA-ACTVC-CODE = 0267\n050908         NEXT SENTENCE ELSE\n050910         GO TO Z-35-2-108-ELSE.\n050912     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-MONEY-SRC-CD.\n050914     GO TO Z-35-2-ENDIF.\n050916 Z-35-2-108-ELSE.\n050918     IF HOLD-TDA-ACTVC-CODE = 0284\n050920         NEXT SENTENCE ELSE\n050922         GO TO Z-35-2-109-ELSE.\n050924     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-PMAT-NTC-CD.\n050926     GO TO Z-35-2-ENDIF.\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    534 lines from 24926 to 25459.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 52, "total_chunks": 55, "start_line": 24926, "end_line": 25459, "line_count": 534}

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
- Source code length: 24671 characters

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
CHUNK 52 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 24926 to 25459 (534 lines)
Chunk Tokens (estimated): ~8,086
Actual Input Tokens: 9,492 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 24926-25459 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 52 of 55 chunks
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
      The source code below is only CHUNK 52 of 55.


=============================================================================
CHUNK 52 SOURCE CODE (Lines 24926-25459)
=============================================================================

```cobol
049860 Z-35-2-20-ELSE.
049862     IF HOLD-TDA-ACTVC-CODE = 0030
049864         NEXT SENTENCE ELSE
049866         GO TO Z-35-2-21-ELSE.
049868     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-CMPD-FREQ.
049870     GO TO Z-35-2-ENDIF.
049872 Z-35-2-21-ELSE.
049874     IF HOLD-TDA-ACTVC-CODE = 0031
049876         NEXT SENTENCE ELSE
049878         GO TO Z-35-2-22-ELSE.
049880     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-CURR-BAL.
049882     GO TO Z-35-2-ENDIF.
049884 Z-35-2-22-ELSE.
049886     IF HOLD-TDA-ACTVC-CODE = 0032
049888         NEXT SENTENCE ELSE
049890         GO TO Z-35-2-23-ELSE.
049892     MOVE WS-CHG-WK-9-4 TO HOLD-TDAA-CMPD-NTRVL.
049894     GO TO Z-35-2-ENDIF.
049896 Z-35-2-23-ELSE.
049898     IF HOLD-TDA-ACTVC-CODE = 0033
049900         NEXT SENTENCE ELSE
049902         GO TO Z-35-2-24-ELSE.
049904     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-VAR-RT-IMMED.
049906     GO TO Z-35-2-ENDIF.
049908 Z-35-2-24-ELSE.
049910     IF HOLD-TDA-ACTVC-CODE = 0034
049912         NEXT SENTENCE ELSE
049914         GO TO Z-35-2-25-ELSE.
049916     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-VAR-RT-INT.
049918     GO TO Z-35-2-ENDIF.
049920 Z-35-2-25-ELSE.
049922     IF HOLD-TDA-ACTVC-CODE = 0035
049924         NEXT SENTENCE ELSE
049926         GO TO Z-35-2-26-ELSE.
049928     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-VAR-RT-SCHED.
049930     GO TO Z-35-2-ENDIF.
049932 Z-35-2-26-ELSE.
049934     IF HOLD-TDA-ACTVC-CODE = 0036
049936         NEXT SENTENCE ELSE
049938         GO TO Z-35-2-27-ELSE.
049940     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-VAR-RT-CUST.
049942     GO TO Z-35-2-ENDIF.
049944 Z-35-2-27-ELSE.
049946     IF HOLD-TDA-ACTVC-CODE = 0037
049948         NEXT SENTENCE ELSE
049950         GO TO Z-35-2-28-ELSE.
049952     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-VAR-RT-BAL.
049954     GO TO Z-35-2-ENDIF.
049956 Z-35-2-28-ELSE.
049958     IF HOLD-TDA-ACTVC-CODE = 0038
049960         NEXT SENTENCE ELSE
049962         GO TO Z-35-2-29-ELSE.
049964     MOVE WS-CHG-WK-9-4V2 TO HOLD-TDAA-CENSUS-TRACT.
049966     GO TO Z-35-2-ENDIF.
049968 Z-35-2-29-ELSE.
049970     IF HOLD-TDA-ACTVC-CODE = 0039
049972         NEXT SENTENCE ELSE
049974         GO TO Z-35-2-30-ELSE.
049976     MOVE WS-CHG-WK-X-2 TO HOLD-TDAA-MK-SEGMENT.
049978     GO TO Z-35-2-ENDIF.
049980 Z-35-2-30-ELSE.
049982     IF HOLD-TDA-ACTVC-CODE = 0040
049984         NEXT SENTENCE ELSE
049986         GO TO Z-35-2-31-ELSE.
049988     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-B-NOTC-YR1.
049990     GO TO Z-35-2-ENDIF.
049992 Z-35-2-31-ELSE.
049994     IF HOLD-TDA-ACTVC-CODE = 0041
049996         NEXT SENTENCE ELSE
049998         GO TO Z-35-2-32-ELSE.
050000     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-B-NOTC-YR2.
050002     GO TO Z-35-2-ENDIF.
050004 Z-35-2-32-ELSE.
050006     IF HOLD-TDA-ACTVC-CODE = 0042
050008         NEXT SENTENCE ELSE
050010         GO TO Z-35-2-33-ELSE.
050012     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-B-NOTC-YR3.
050014     GO TO Z-35-2-ENDIF.
050016 Z-35-2-33-ELSE.
050018     IF HOLD-TDA-ACTVC-CODE = 0043
050020         NEXT SENTENCE ELSE
050022         GO TO Z-35-2-34-ELSE.
050024     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-ODD-PAYMENT.
050026     GO TO Z-35-2-ENDIF.
050028 Z-35-2-34-ELSE.
050030     IF HOLD-TDA-ACTVC-CODE = 0044
050032         NEXT SENTENCE ELSE
050034         GO TO Z-35-2-35-ELSE.
050036     MOVE WS-CHG-WK-X-8 TO HOLD-TDAA-EMPLOYEE-ID.
050038     GO TO Z-35-2-ENDIF.
050040 Z-35-2-35-ELSE.
050042     IF HOLD-TDA-ACTVC-CODE = 0045
050044         NEXT SENTENCE ELSE
050046         GO TO Z-35-2-36-ELSE.
050048     MOVE WS-CHG-WK-9-6 TO HOLD-TDAA-DDA-ACCT-1-S.
050050     GO TO Z-35-2-ENDIF.
050052 Z-35-2-36-ELSE.
050054     IF HOLD-TDA-ACTVC-CODE = 0046
050056         NEXT SENTENCE ELSE
050058         GO TO Z-35-2-37-ELSE.
050060     MOVE WS-CHG-WK-9-6 TO HOLD-TDAA-DDA-ACCT-2-S.
050062     GO TO Z-35-2-ENDIF.
050064 Z-35-2-37-ELSE.
050066     IF HOLD-TDA-ACTVC-CODE = 0047
050068         NEXT SENTENCE ELSE
050070         GO TO Z-35-2-38-ELSE.
050072     MOVE WS-CHG-WK-9-6 TO HOLD-TDAA-DDA-ACCT-3-S.
050074     GO TO Z-35-2-ENDIF.
050076 Z-35-2-38-ELSE.
050078     IF HOLD-TDA-ACTVC-CODE = 0048
050080         NEXT SENTENCE ELSE
050082         GO TO Z-35-2-39-ELSE.
050084     MOVE WS-CHG-WK-9-6 TO HOLD-TDAA-INT-ACCT-S.
050086     GO TO Z-35-2-ENDIF.
050088 Z-35-2-39-ELSE.
050090     IF HOLD-TDA-ACTVC-CODE = 0049
050092         NEXT SENTENCE ELSE
050094         GO TO Z-35-2-40-ELSE.
050096     MOVE WS-CHG-WK-9-6 TO HOLD-TDAA-CS-ACCT-S.
050098     GO TO Z-35-2-ENDIF.
050100 Z-35-2-40-ELSE.
050102     IF HOLD-TDA-ACTVC-CODE = 0050
050104         NEXT SENTENCE ELSE
050106         GO TO Z-35-2-41-ELSE.
050108     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-RENEW-CD.
050110     GO TO Z-35-2-ENDIF.
050112 Z-35-2-41-ELSE.
050114     IF HOLD-TDA-ACTVC-CODE = 0051
050116         NEXT SENTENCE ELSE
050118         GO TO Z-35-2-42-ELSE.
050120     MOVE WS-CHG-WK-9-5 TO HOLD-TDAA-DAYS-IN-PER.
050122     GO TO Z-35-2-ENDIF.
050124 Z-35-2-42-ELSE.
050126     IF HOLD-TDA-ACTVC-CODE = 0052
050128         NEXT SENTENCE ELSE
050130         GO TO Z-35-2-43-ELSE.
050132     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-BEG-INT-BAL.
050134     GO TO Z-35-2-ENDIF.
050136 Z-35-2-43-ELSE.
050138     IF HOLD-TDA-ACTVC-CODE = 0053
050140         NEXT SENTENCE ELSE
050142         GO TO Z-35-2-44-ELSE.
050144     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-CLOSE-AMT.
050146     GO TO Z-35-2-ENDIF.
050148 Z-35-2-44-ELSE.
050150     IF HOLD-TDA-ACTVC-CODE = 0054
050152         NEXT SENTENCE ELSE
050154         GO TO Z-35-2-45-ELSE.
050156     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-MONEY-AMT.
050158     GO TO Z-35-2-ENDIF.
050160 Z-35-2-45-ELSE.
050162     IF HOLD-TDA-ACTVC-CODE = 0055
050164         NEXT SENTENCE ELSE
050166         GO TO Z-35-2-46-ELSE.
050168     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-CURR-INT-ADJ.
050170     GO TO Z-35-2-ENDIF.
050172 Z-35-2-46-ELSE.
050174     IF HOLD-TDA-ACTVC-CODE = 0056
050176         NEXT SENTENCE ELSE
050178         GO TO Z-35-2-47-ELSE.
050180     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-TOTAMT-HOLDS.
050182     GO TO Z-35-2-ENDIF.
050184 Z-35-2-47-ELSE.
050186     IF HOLD-TDA-ACTVC-CODE = 0057
050188         NEXT SENTENCE ELSE
050190         GO TO Z-35-2-48-ELSE.
050192     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-NXT-INT-ADJ.
050194     GO TO Z-35-2-ENDIF.
050196 Z-35-2-48-ELSE.
050198     IF HOLD-TDA-ACTVC-CODE = 0058
050200         NEXT SENTENCE ELSE
050202         GO TO Z-35-2-49-ELSE.
050204     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-FEE-AMT.
050206     GO TO Z-35-2-ENDIF.
050208 Z-35-2-49-ELSE.
050210     IF HOLD-TDA-ACTVC-CODE = 0059
050212         NEXT SENTENCE ELSE
050214         GO TO Z-35-2-50-ELSE.
050216     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-BEG-INT-RT.
050218     GO TO Z-35-2-ENDIF.
050220 Z-35-2-50-ELSE.
050222     IF HOLD-TDA-ACTVC-CODE = 0060
050224         NEXT SENTENCE ELSE
050226         GO TO Z-35-2-51-ELSE.
050228     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-YIELD-RT.
050230     GO TO Z-35-2-ENDIF.
050232 Z-35-2-51-ELSE.
050234     IF HOLD-TDA-ACTVC-CODE = 0061
050236         NEXT SENTENCE ELSE
050238         GO TO Z-35-2-52-ELSE.
050240     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-SCHED-DT.
050242     GO TO Z-35-2-ENDIF.
050244 Z-35-2-52-ELSE.
050246     IF HOLD-TDA-ACTVC-CODE = 0062
050248         NEXT SENTENCE ELSE
050250         GO TO Z-35-2-53-ELSE.
050252     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-NXT-MAT-DT.
050254     GO TO Z-35-2-ENDIF.
050256 Z-35-2-53-ELSE.
050258     IF HOLD-TDA-ACTVC-CODE = 0063
050260         NEXT SENTENCE ELSE
050262         GO TO Z-35-2-54-ELSE.
050264     MOVE WS-CHG-WK-9-10 TO HOLD-TDAA-CC-ACCT.
050266     GO TO Z-35-2-ENDIF.
050268 Z-35-2-54-ELSE.
050270     IF HOLD-TDA-ACTVC-CODE = 0064
050272         NEXT SENTENCE ELSE
050274         GO TO Z-35-2-55-ELSE.
050276     MOVE WS-CHG-WK-X-3 TO HOLD-TDAA-BK-DEF-TOT.
050278     GO TO Z-35-2-ENDIF.
050280 Z-35-2-55-ELSE.
050282     IF HOLD-TDA-ACTVC-CODE = 0065
050284         NEXT SENTENCE ELSE
050286         GO TO Z-35-2-56-ELSE.
050288     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-ALERT-CD.
050290     GO TO Z-35-2-ENDIF.
050292 Z-35-2-56-ELSE.
050294     IF HOLD-TDA-ACTVC-CODE = 0067
050296         NEXT SENTENCE ELSE
050298         GO TO Z-35-2-57-ELSE.
050300     MOVE WS-CHG-WK-9-S15V2 TO HOLD-TDAA-RMD-AMOUNT.
050302     GO TO Z-35-2-ENDIF.
050304 Z-35-2-57-ELSE.
050306     IF HOLD-TDA-ACTVC-CODE = 0099
050308         NEXT SENTENCE ELSE
050310         GO TO Z-35-2-58-ELSE.
050312     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-MAIL-CD.
050314     GO TO Z-35-2-ENDIF.
050316 Z-35-2-58-ELSE.
050318     IF HOLD-TDA-ACTVC-CODE = 0110
050320         NEXT SENTENCE ELSE
050322         GO TO Z-35-2-59-ELSE.
050324     MOVE WS-CHG-WK-9-7 TO HOLD-TDAA-CERT.
050326     GO TO Z-35-2-ENDIF.
050328 Z-35-2-59-ELSE.
050330     IF HOLD-TDA-ACTVC-CODE = 0111
050332         NEXT SENTENCE ELSE
050334         GO TO Z-35-2-60-ELSE.
050336     MOVE WS-CHG-WK-9-10 TO HOLD-TDAC-PHONE-1.
050338     GO TO Z-35-2-ENDIF.
050340 Z-35-2-60-ELSE.
050342     IF HOLD-TDA-ACTVC-CODE = 0112
050344         NEXT SENTENCE ELSE
050346         GO TO Z-35-2-61-ELSE.
050348     MOVE WS-CHG-WK-9-10 TO HOLD-TDAC-PHONE-2.
050350     GO TO Z-35-2-ENDIF.
050352 Z-35-2-61-ELSE.
050354     IF HOLD-TDA-ACTVC-CODE = 0113
050356         NEXT SENTENCE ELSE
050358         GO TO Z-35-2-62-ELSE.
050360     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-STATUS.
050362     GO TO Z-35-2-ENDIF.
050364 Z-35-2-62-ELSE.
050366     IF HOLD-TDA-ACTVC-CODE = 0116
050368         NEXT SENTENCE ELSE
050370         GO TO Z-35-2-63-ELSE.
050372     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-OVERRIDE.
050374     GO TO Z-35-2-ENDIF.
050376 Z-35-2-63-ELSE.
050378     IF HOLD-TDA-ACTVC-CODE = 0117
050380         NEXT SENTENCE ELSE
050382         GO TO Z-35-2-64-ELSE.
050384     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-COMM-MAT-CD.
050386     GO TO Z-35-2-ENDIF.
050388 Z-35-2-64-ELSE.
050390     IF HOLD-TDA-ACTVC-CODE = 0118
050392         NEXT SENTENCE ELSE
050394         GO TO Z-35-2-65-ELSE.
050396     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-BENEF-CD.
050398     GO TO Z-35-2-ENDIF.
050400 Z-35-2-65-ELSE.
050402     IF HOLD-TDA-ACTVC-CODE = 0119
050404         NEXT SENTENCE ELSE
050406         GO TO Z-35-2-66-ELSE.
050408     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-NBR-BENEF.
050410     GO TO Z-35-2-ENDIF.
050412 Z-35-2-66-ELSE.
050414     IF HOLD-TDA-ACTVC-CODE = 0121
050416         NEXT SENTENCE ELSE
050418         GO TO Z-35-2-67-ELSE.
050420     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-REN-NTC-CD.
050422     GO TO Z-35-2-ENDIF.
050424 Z-35-2-67-ELSE.
050426     IF HOLD-TDA-ACTVC-CODE = 0122
050428         NEXT SENTENCE ELSE
050430         GO TO Z-35-2-68-ELSE.
050432     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-RTCHG-NTC-CD.
050434     GO TO Z-35-2-ENDIF.
050436 Z-35-2-68-ELSE.
050438     IF HOLD-TDA-ACTVC-CODE = 0123
050440         NEXT SENTENCE ELSE
050442         GO TO Z-35-2-69-ELSE.
050444     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-INT-NTC-CD.
050446     GO TO Z-35-2-ENDIF.
050448 Z-35-2-69-ELSE.
050450     IF HOLD-TDA-ACTVC-CODE = 0125
050452         NEXT SENTENCE ELSE
050454         GO TO Z-35-2-70-ELSE.
050456     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-PURCH-AMT.
050458     GO TO Z-35-2-ENDIF.
050460 Z-35-2-70-ELSE.
050462     IF HOLD-TDA-ACTVC-CODE = 0127
050464         NEXT SENTENCE ELSE
050466         GO TO Z-35-2-71-ELSE.
050468     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-RT-CHG-LIMIT.
050470     GO TO Z-35-2-ENDIF.
050472 Z-35-2-71-ELSE.
050474     IF HOLD-TDA-ACTVC-CODE = 0133
050476         NEXT SENTENCE ELSE
050478         GO TO Z-35-2-72-ELSE.
050480     MOVE WS-CHG-WK-9-8 TO HOLD-TDAA-OPEN-DT.
050482     GO TO Z-35-2-ENDIF.
050484 Z-35-2-72-ELSE.
050486     IF HOLD-TDA-ACTVC-CODE = 0134
050488         NEXT SENTENCE ELSE
050490         GO TO Z-35-2-73-ELSE.
050492     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-ORG-YIELD-RT.
050494     GO TO Z-35-2-ENDIF.
050496 Z-35-2-73-ELSE.
050498     IF HOLD-TDA-ACTVC-CODE = 0135
050500         NEXT SENTENCE ELSE
050502         GO TO Z-35-2-74-ELSE.
050504     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-ORG-MAT-TYPE.
050506     GO TO Z-35-2-ENDIF.
050508 Z-35-2-74-ELSE.
050510     IF HOLD-TDA-ACTVC-CODE = 0136
050512         NEXT SENTENCE ELSE
050514         GO TO Z-35-2-75-ELSE.
050516     MOVE WS-CHG-WK-9-4 TO HOLD-TDAA-ORG-MAT-TERM.
050518     GO TO Z-35-2-ENDIF.
050520 Z-35-2-75-ELSE.
050522     IF HOLD-TDA-ACTVC-CODE = 0141
050524         NEXT SENTENCE ELSE
050526         GO TO Z-35-2-76-ELSE.
050528     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-BK-DEF-CD1.
050530     GO TO Z-35-2-ENDIF.
050532 Z-35-2-76-ELSE.
050534     IF HOLD-TDA-ACTVC-CODE = 0142
050536         NEXT SENTENCE ELSE
050538         GO TO Z-35-2-77-ELSE.
050540     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-BK-DEF-CD2.
050542     GO TO Z-35-2-ENDIF.
050544 Z-35-2-77-ELSE.
050546     IF HOLD-TDA-ACTVC-CODE = 0143
050548         NEXT SENTENCE ELSE
050550         GO TO Z-35-2-78-ELSE.
050552     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-BK-DEF-CD3.
050554     GO TO Z-35-2-ENDIF.
050556 Z-35-2-78-ELSE.
050558     IF HOLD-TDA-ACTVC-CODE = 0144
050560         NEXT SENTENCE ELSE
050562         GO TO Z-35-2-79-ELSE.
050564     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-BK-DEF-CD4.
050566     GO TO Z-35-2-ENDIF.
050568 Z-35-2-79-ELSE.
050570     IF HOLD-TDA-ACTVC-CODE = 0145
050572         NEXT SENTENCE ELSE
050574         GO TO Z-35-2-80-ELSE.
050576     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-BK-DEF-CD5.
050578     GO TO Z-35-2-ENDIF.
050580 Z-35-2-80-ELSE.
050582     IF HOLD-TDA-ACTVC-CODE = 0146
050584         NEXT SENTENCE ELSE
050586         GO TO Z-35-2-81-ELSE.
050588     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-OID-METH.
050590     GO TO Z-35-2-ENDIF.
050592 Z-35-2-81-ELSE.
050594     IF HOLD-TDA-ACTVC-CODE = 0150
050596         NEXT SENTENCE ELSE
050598         GO TO Z-35-2-82-ELSE.
050600     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-DISP-CD.
050602     GO TO Z-35-2-ENDIF.
050604 Z-35-2-82-ELSE.
050606     IF HOLD-TDA-ACTVC-CODE = 0161
050608         NEXT SENTENCE ELSE
050610         GO TO Z-35-2-83-ELSE.
050612     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-PAY-FREQ.
050614     GO TO Z-35-2-ENDIF.
050616 Z-35-2-83-ELSE.
050618     IF HOLD-TDA-ACTVC-CODE = 0163
050620         NEXT SENTENCE ELSE
050622         GO TO Z-35-2-84-ELSE.
050624     MOVE WS-CHG-WK-9-4 TO HOLD-TDAA-PAY-NTRVL.
050626     GO TO Z-35-2-ENDIF.
050628 Z-35-2-84-ELSE.
050630     IF HOLD-TDA-ACTVC-CODE = 0165
050632         NEXT SENTENCE ELSE
050634         GO TO Z-35-2-85-ELSE.
050636     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-STMT-FREQ.
050638     GO TO Z-35-2-ENDIF.
050640 Z-35-2-85-ELSE.
050642     IF HOLD-TDA-ACTVC-CODE = 0166
050644         NEXT SENTENCE ELSE
050646         GO TO Z-35-2-86-ELSE.
050648     MOVE WS-CHG-WK-9-4 TO HOLD-TDAA-STMT-NTRVL.
050650     GO TO Z-35-2-ENDIF.
050652 Z-35-2-86-ELSE.
050654     IF HOLD-TDA-ACTVC-CODE = 0189
050656         NEXT SENTENCE ELSE
050658         GO TO Z-35-2-87-ELSE.
050660     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-MAT-TYPE.
050662     GO TO Z-35-2-ENDIF.
050664 Z-35-2-87-ELSE.
050666     IF HOLD-TDA-ACTVC-CODE = 0192
050668         NEXT SENTENCE ELSE
050670         GO TO Z-35-2-88-ELSE.
050672     MOVE WS-CHG-WK-9-4 TO HOLD-TDAA-MAT-TERM.
050674     GO TO Z-35-2-ENDIF.
050676 Z-35-2-88-ELSE.
050678     IF HOLD-TDA-ACTVC-CODE = 0220
050680         NEXT SENTENCE ELSE
050682         GO TO Z-35-2-89-ELSE.
050684     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-YIELD-NUM.
050686     GO TO Z-35-2-ENDIF.
050688 Z-35-2-89-ELSE.
050690     IF HOLD-TDA-ACTVC-CODE = 0222
050692         NEXT SENTENCE ELSE
050694         GO TO Z-35-2-90-ELSE.
050696     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-DIST-STATUS.
050698     GO TO Z-35-2-ENDIF.
050700 Z-35-2-90-ELSE.
050702     IF HOLD-TDA-ACTVC-CODE = 0231
050704         NEXT SENTENCE ELSE
050706         GO TO Z-35-2-91-ELSE.
050708     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-PLEDGE-CD.
050710     GO TO Z-35-2-ENDIF.
050712 Z-35-2-91-ELSE.
050714     IF HOLD-TDA-ACTVC-CODE = 0236
050716         NEXT SENTENCE ELSE
050718         GO TO Z-35-2-92-ELSE.
050720     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-NEGOT-CD.
050722     GO TO Z-35-2-ENDIF.
050724 Z-35-2-92-ELSE.
050726     IF HOLD-TDA-ACTVC-CODE = 0237
050728         NEXT SENTENCE ELSE
050730         GO TO Z-35-2-93-ELSE.
050732     MOVE WS-CHG-WK-9-10 TO HOLD-TDAA-DDA-ACCT-1.
050734     GO TO Z-35-2-ENDIF.
050736 Z-35-2-93-ELSE.
050738     IF HOLD-TDA-ACTVC-CODE = 0238
050740         NEXT SENTENCE ELSE
050742         GO TO Z-35-2-94-ELSE.
050744     MOVE WS-CHG-WK-9-10 TO HOLD-TDAA-DDA-ACCT-2.
050746     GO TO Z-35-2-ENDIF.
050748 Z-35-2-94-ELSE.
050750     IF HOLD-TDA-ACTVC-CODE = 0239
050752         NEXT SENTENCE ELSE
050754         GO TO Z-35-2-95-ELSE.
050756     MOVE WS-CHG-WK-9-10 TO HOLD-TDAA-DDA-ACCT-3.
050758     GO TO Z-35-2-ENDIF.
050760 Z-35-2-95-ELSE.
050762     IF HOLD-TDA-ACTVC-CODE = 0240
050764         NEXT SENTENCE ELSE
050766         GO TO Z-35-2-96-ELSE.
050768     MOVE WS-CHG-WK-9-10 TO HOLD-TDAA-INT-ACCT.
050770     GO TO Z-35-2-ENDIF.
050772 Z-35-2-96-ELSE.
050774     IF HOLD-TDA-ACTVC-CODE = 0244
050776         NEXT SENTENCE ELSE
050778         GO TO Z-35-2-97-ELSE.
050780     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-CUR-INT-RT.
050782     GO TO Z-35-2-ENDIF.
050784 Z-35-2-97-ELSE.
050786     IF HOLD-TDA-ACTVC-CODE = 0246
050788         NEXT SENTENCE ELSE
050790         GO TO Z-35-2-98-ELSE.
050792     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-RT-INDX-CD.
050794     GO TO Z-35-2-ENDIF.
050796 Z-35-2-98-ELSE.
050798     IF HOLD-TDA-ACTVC-CODE = 0247
050800         NEXT SENTENCE ELSE
050802         GO TO Z-35-2-99-ELSE.
050804     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-RT-REGN-CD.
050806     GO TO Z-35-2-ENDIF.
050808 Z-35-2-99-ELSE.
050810     IF HOLD-TDA-ACTVC-CODE = 0248
050812         NEXT SENTENCE ELSE
050814         GO TO Z-35-2-100-ELSE.
050816     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-RT-TIER-CD.
050818     GO TO Z-35-2-ENDIF.
050820 Z-35-2-100-ELSE.
050822     IF HOLD-TDA-ACTVC-CODE = 0249
050824         NEXT SENTENCE ELSE
050826         GO TO Z-35-2-101-ELSE.
050828     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-YIELD-DENOM.
050830     GO TO Z-35-2-ENDIF.
050832 Z-35-2-101-ELSE.
050834     IF HOLD-TDA-ACTVC-CODE = 0250
050836         NEXT SENTENCE ELSE
050838         GO TO Z-35-2-102-ELSE.
050840     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-RT-SR-CD.
050842     GO TO Z-35-2-ENDIF.
050844 Z-35-2-102-ELSE.
050846     IF HOLD-TDA-ACTVC-CODE = 0251
050848         NEXT SENTENCE ELSE
050850         GO TO Z-35-2-103-ELSE.
050852     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-RT-MARG-CD.
050854     GO TO Z-35-2-ENDIF.
050856 Z-35-2-103-ELSE.
050858     IF HOLD-TDA-ACTVC-CODE = 0252
050860         NEXT SENTENCE ELSE
050862         GO TO Z-35-2-104-ELSE.
050864     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-RT-CHG-NTRVL.
050866     GO TO Z-35-2-ENDIF.
050868 Z-35-2-104-ELSE.
050870     IF HOLD-TDA-ACTVC-CODE = 0260
050872         NEXT SENTENCE ELSE
050874         GO TO Z-35-2-105-ELSE.
050876     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-TOTAL-CD.
050878     GO TO Z-35-2-ENDIF.
050880 Z-35-2-105-ELSE.
050882     IF HOLD-TDA-ACTVC-CODE = 0262
050884         NEXT SENTENCE ELSE
050886         GO TO Z-35-2-106-ELSE.
050888     MOVE WS-CHG-WK-9-3 TO HOLD-TDAA-REN-TOTAL-CD.
050890     GO TO Z-35-2-ENDIF.
050892 Z-35-2-106-ELSE.
050894     IF HOLD-TDA-ACTVC-CODE = 0263
050896         NEXT SENTENCE ELSE
050898         GO TO Z-35-2-107-ELSE.
050900     MOVE WS-CHG-WK-9-2V3 TO HOLD-TDAA-REN-YIELD-RT.
050902     GO TO Z-35-2-ENDIF.
050904 Z-35-2-107-ELSE.
050906     IF HOLD-TDA-ACTVC-CODE = 0267
050908         NEXT SENTENCE ELSE
050910         GO TO Z-35-2-108-ELSE.
050912     MOVE WS-CHG-WK-X-1 TO HOLD-TDAA-MONEY-SRC-CD.
050914     GO TO Z-35-2-ENDIF.
050916 Z-35-2-108-ELSE.
050918     IF HOLD-TDA-ACTVC-CODE = 0284
050920         NEXT SENTENCE ELSE
050922         GO TO Z-35-2-109-ELSE.
050924     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-PMAT-NTC-CD.
050926     GO TO Z-35-2-ENDIF.
```

⚠️  This is the source code you must document.
    534 lines from 24926 to 25459.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

