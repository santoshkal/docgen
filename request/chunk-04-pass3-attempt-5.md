# LLM Request Debug File
Generated: 2025-11-18T18:16:06.908627

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 4/55
- **Model**: gpt-4.1
- **Chunk Number**: 4
- **Pass Number**: 3
- **Attempt Number**: 5 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,085 tokens
- **User Prompt**: ~5,721 tokens
- **Total Input**: ~7,806 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 4/55" (ID: detailed-code-explanation)

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


**CHUNK 4 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T18:05:37.383587", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 4 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 1333 to 1615 (283 lines)\nChunk Tokens (estimated): ~5,572\nActual Input Tokens: 6,978 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 1333-1615 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 4 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 4 of 55.\n\n\n=============================================================================\nCHUNK 4 SOURCE CODE (Lines 1333-1615)\n=============================================================================\n\n```cobol\n002674 01  Z-VALUED-AREA.\n002676*\n002678     05  Z-FILE1-FILENAME       PIC X(30) VALUE \"TDARESTART\".\n002680     05  Z-FILE3-FILENAME       PIC X(30) VALUE \"BK-SPEC-FILE\".\n002682     05  Z-FILE4-FILENAME       PIC X(30) VALUE \"PROC-FILE\".\n002684     05  Z-FILE5-FILENAME       PIC X(30) VALUE \"DST-FILE-MAINT\".\n002686     05  Z-FILE6-FILENAME       PIC X(30) VALUE \"CST-FILE-MAINT\".\n002688     05  Z-FILE7-FILENAME       PIC X(30) VALUE \"SPCPRT\".\n002690     05  Z-FILE8-FILENAME       PIC X(30) VALUE \"TDAACCT\".\n002692     05  Z-FILE9-FILENAME       PIC X(30) VALUE \"TDAREPORTS\".\n002694     05  Z-FILE10-FILENAME      PIC X(30) VALUE \"TDAPCR\".\n002696     05  Z-FILE11-FILENAME      PIC X(30) VALUE \"TDACUST\".\n002698     05  Z-FILE12-FILENAME      PIC X(30) VALUE \"TDAIRA\".\n002700     05  Z-FILE13-FILENAME      PIC X(30) VALUE \"TDADISTR\".\n002702     05  Z-FILE14-FILENAME      PIC X(30) VALUE \"TDAACTV\".\n002704*\n002706     05  Z-FL-MSG-LIT-1.\n002708         10  FILLER     PIC X(17) VALUE \"CORRUPT KEY FILE \".\n002710         10  Z-FL-MSG-LIT-1-1 PIC X(30).\n002712     05  Z-FL-MSG-LIT-2.\n002714         10  FILLER     PIC X(32) VALUE\n002716                        \"INVALID REWRITE OF FIRST RECORD.\".\n002718     05  Z-FL-MSG-LIT-3.\n002720         10  FILLER     PIC X(18) VALUE \"MUST REBUILD KEYS.\".\n002722     05  Z-FL-MSG-LIT-4.\n002724         10  FILLER     PIC X(24) VALUE\n002726                        \"PRIOR READ REQUIRED FOR \".\n002728         10  Z-FL-MSG-LIT-4-1 PIC X(30).\n002730         10  FILLER     PIC X(06) VALUE \" AT   \".\n002732         10  Z-FL-MSG-LIT-4-2 PIC 9(8).\n002734         10  FILLER     PIC X(12) VALUE SPACES.\n002736     05  Z-FL-MSG-LIT-5.\n002738         10  FILLER     PIC X(22) VALUE \">>>>>> ABORT PROGRAM: \".\n002740         10  Z-FL-MSG-LIT-5-1 PIC X(30).\n002742     05  Z-FL-MSG-LIT-6.\n002744         10  FILLER     PIC X(22) VALUE \"SIZE ERROR DETECTED,  \".\n002746         10  Z-FL-MSG-LIT-6-1 PIC X(30).\n002748         10  FILLER     PIC X(12) VALUE \" STATEMENT: \".\n002750         10  Z-FL-MSG-LIT-6-2 PIC 9(8).\n002752     05  Z-FL-MSG-LIT-7.\n002754         10  FILLER     PIC X(12) VALUE \"PROGRAM ID: \".\n002756         10  Z-FL-MSG-LIT-7-1 PIC X(30).\n002758     05  Z-FL-MSG-LIT-8.\n002760         10  FILLER     PIC X(22) VALUE \" STATEMENT TYPE     : \".\n002762         10  Z-FL-MSG-LIT-8-1 PIC X(58).\n002764     05  Z-FL-MSG-LIT-9.\n002766         10  FILLER     PIC X(22) VALUE \" STATEMENT NUMBER   : \".\n002768         10  Z-FL-MSG-LIT-9-1 PIC 9(8).\n002770     05  Z-FL-MSG-LIT-12.\n002772         10  FILLER     PIC X(24) VALUE\n002774                        \"CURRENT PROCEDURE     : \".\n002776         10  Z-FL-MSG-LIT-12-1 PIC X(56).\n002778     05  Z-FL-MSG-LIT-13.\n002780         10  FILLER     PIC X(24) VALUE\n002782                        \"CURRENT PROCESS       : \".\n002784         10  Z-FL-MSG-LIT-13-1 PIC X(56).\n002786     05  Z-FL-MSG-LIT-14.\n002788         10  FILLER     PIC X(24) VALUE\n002790                        \"PRIOR READ REQUIRED FOR \".\n002792         10  Z-FL-MSG-LIT-14-1 PIC X(30).\n002794         10  FILLER     PIC X(4)  VALUE \" AT \".\n002796         10  Z-FL-MSG-LIT-14-2 PIC 9(8).\n002798     05  Z-FL-MSG-LIT-10.\n002800         10  FILLER     PIC X(24) VALUE\n002802                        \"KEY ALTERED ON CHANGE : \".\n002804         10  Z-FL-MSG-LIT-10-1 PIC X(56).\n002806         10  FILLER     PIC X(4)  VALUE \" AT \".\n002808         10  Z-FL-MSG-LIT-10-2 PIC 9(8).\n002810     05  Z-FL-MSG-LIT-11.\n002812         10  FILLER     PIC X(32) VALUE\n002814                       \"REWRITE SKIPPED FROM REQUEST AT \".\n002816         10  Z-FL-MSG-LIT-11-1 PIC 9(8).\n002818     05  Z-FL-MSG-LIT-15.\n002820         10  FILLER     PIC X(13) VALUE \">>>> REQUEST \".\n002822         10  Z-FL-MSG-LIT-15-1 PIC X(10).\n002824         10  FILLER     PIC X(10) VALUE \" FILE     \".\n002826         10  Z-FL-MSG-LIT-15-2 PIC X(30).\n002828         10  FILLER     PIC X(11) VALUE \" FAILED AT \".\n002830         10  Z-FL-MSG-LIT-15-3 PIC 9(8).\n002832     05  Z-FL-MSG-LIT-16.\n002834         10  FILLER     PIC X(37) VALUE\n002836                        \">>>> INVALID VARIABLE FORMAT NUMBER: \".\n002838         10  Z-FL-MSG-LIT-16-1 PIC 9(8).\n002840     05  Z-FL-MSG-LIT-17.\n002842         10  FILLER     PIC X(20) VALUE \"PRIOR READ REQUIRED \".\n002844     05  Z-FL-MSG-LIT-18.\n002846         10  FILLER     PIC X(24) VALUE\n002848                        \"ERROR READING BASE FILE \".\n002850         10  Z-FL-MSG-LIT-18-1 PIC X(30).\n002852     05  Z-FL-MSG-LIT-19.\n002854         10  FILLER     PIC X(24) VALUE\n002856                        \"ERROR BUILDING KEYS FOR \".\n002858         10  Z-FL-MSG-LIT-19-1 PIC X(30).\n002860*\n002862     05  Z-FL-MSG-LIT-REQS.\n002864         10  FILLER     PIC X(9) VALUE \"CHANGEKEY\".\n002866         10  FILLER     PIC X(9) VALUE \"CHANGE   \".\n002868         10  FILLER     PIC X(9) VALUE \"DELETE   \".\n002870         10  FILLER     PIC X(9) VALUE \"DELETEADD\".\n002872         10  FILLER     PIC X(9) VALUE \"LINK     \".\n002874         10  FILLER     PIC X(9) VALUE \"ADD      \".\n002876     05  Z-FL-MSG-LIT-REDEF REDEFINES Z-FL-MSG-LIT-REQS.\n002878         10  Z-FL-MSG-LIT-OCC OCCURS 6 PIC X(9).\n002880*\n002882     05  Z-ERR-MSG-LIT-1.\n002884         10  FILLER     PIC X(22) VALUE \">>>>>> ABORT PROGRAM: \".\n002886         10  Z-ERR-MSG-LIT-1-1 PIC X(30).\n002888     05  Z-ERR-MSG-LIT-2.\n002890         10  FILLER     PIC X(22) VALUE \"SIZE ERROR DETECTED,  \".\n002892         10  Z-ERR-MSG-LIT-2-1 PIC X(10).\n002894         10  FILLER     PIC X(12) VALUE \" STATEMENT: \".\n002896         10  Z-ERR-MSG-LIT-2-2 PIC 9(8).\n002898     05  Z-ERR-MSG-LIT-3.\n002900         10  FILLER     PIC X(12) VALUE \"PROGRAM ID: \".\n002902         10  Z-ERR-MSG-LIT-3-1 PIC X(30).\n002904     05  Z-ERR-MSG-LIT-4.\n002906         10  FILLER     PIC X(22) VALUE \" STATEMENT TYPE     : \".\n002908         10  Z-ERR-MSG-LIT-4-1 PIC X(58).\n002910     05  Z-ERR-MSG-LIT-5.\n002912         10  FILLER     PIC X(22) VALUE \" STATEMENT NUMBER   : \".\n002914         10  Z-ERR-MSG-LIT-5-1 PIC 9(8).\n002916*\n002918     05  Z-ERR-MSG-STMTS.\n002920         10  FILLER     PIC X(8) VALUE \"     ADD\".\n002922         10  FILLER     PIC X(8) VALUE \" COMPUTE\".\n002924         10  FILLER     PIC X(8) VALUE \"  DIVIDE\".\n002926         10  FILLER     PIC X(8) VALUE \"MULTIPLY\".\n002928         10  FILLER     PIC X(8) VALUE \"SUBTRACT\".\n002930         10  FILLER     PIC X(8) VALUE \" UNKNOWN\".\n002932     05  Z-ERR-MSG-STMTS-REDEF REDEFINES Z-ERR-MSG-STMTS.\n002934         10  Z-ERR-STMT-OCC OCCURS 6 PIC X(8).\n002936     05  Z-RPT-1-PAGE-SIZE                      PIC S9(6)\n002938                                                VALUE +57.\n002940     05  Z-RPT-2-PAGE-SIZE                      PIC S9(6)\n002942                                                VALUE +57.\n002944******         WORKING-STORAGE FOR ALL DATE ROUTINES    ******\n002946     05  Z-MINUS-ONE                 PIC S9(01).\n002948     05  Z-DATE-1-HOLD-AREA          PIC X(100).\n002950     05  Z-DATE-1.\n002952         10  Z-DATE-CC-1             PIC S9(02) BINARY.\n002954         10  Z-DATE-YY-MM-DD-1.\n002956             15  Z-DATE-YY-1         PIC S9(02) BINARY.\n002958             15  Z-DATE-MM-1         PIC S9(02) BINARY.\n002960             15  Z-DATE-DD-1         PIC S9(02) BINARY.\n002962         10  Z-DATE-JJJ-1            PIC S9(03) BINARY.\n002964         10  Z-DATE-ZZ-UU-SS-TT-1.\n002966             15  Z-DATE-ZZ-1         PIC S9(02) BINARY.\n002968             15  Z-DATE-UU-1         PIC S9(02) BINARY.\n002970             15  Z-DATE-SS-1         PIC S9(02) BINARY.\n002972             15  Z-DATE-TT-1         PIC S9(02) BINARY.\n002974         10  Z-DATE-HH-1             PIC S9(02) BINARY.\n002976         10  Z-DATE-AP-1             PIC S9(01) BINARY.\n002978             88  Z-DATE-AM-1                       VALUE +1.\n002980             88  Z-DATE-PM-1                       VALUE +2.\n002982         10  Z-DATE-MX-1             PIC S9(02) BINARY.\n002984         10  Z-DATE-DOW-1            PIC 9.\n002986         10  Z-DATE-CHARS-1.\n002988             15  Z-DATE-MMM-1        PIC  X(03).\n002990             15  Z-DATE-MONTH-1      PIC  X(09).\n002992             15  Z-DATE-DDD-1        PIC  X(03).\n002994             15  Z-DATE-DAY-1        PIC  X(09).\n002996     05  Z-DATE-2.\n002998         10  Z-DATE-CC-2             PIC S9(02) BINARY.\n003000         10  Z-DATE-YY-MM-DD-2.\n003002             15  Z-DATE-YY-2         PIC S9(02) BINARY.\n003004             15  Z-DATE-MM-2         PIC S9(02) BINARY.\n003006             15  Z-DATE-DD-2         PIC S9(02) BINARY.\n003008         10  Z-DATE-JJJ-2            PIC S9(03) BINARY.\n003010         10  Z-DATE-ZZ-UU-SS-TT-2.\n003012             15  Z-DATE-ZZ-2         PIC S9(02) BINARY.\n003014             15  Z-DATE-UU-2         PIC S9(02) BINARY.\n003016             15  Z-DATE-SS-2         PIC S9(02) BINARY.\n003018             15  Z-DATE-TT-2         PIC S9(02) BINARY.\n003020         10  Z-DATE-HH-2             PIC S9(02) BINARY.\n003022         10  Z-DATE-AP-2             PIC S9(01) BINARY.\n003024             88  Z-DATE-AM-2                       VALUE +1.\n003026             88  Z-DATE-PM-2                       VALUE +2.\n003028         10  Z-DATE-MX-2             PIC S9(02) BINARY.\n003030         10  Z-DATE-DOW-2            PIC 9.\n003032         10  Z-DATE-CHARS-2.\n003034             15  Z-DATE-MMM-2        PIC  X(03).\n003036             15  Z-DATE-MONTH-2      PIC  X(09).\n003038             15  Z-DATE-DDD-2        PIC  X(03).\n003040             15  Z-DATE-DAY-2        PIC  X(09).\n003042     05  Z-DATE-3.\n003044         10  Z-DATE-CC-3             PIC S9(02) BINARY.\n003046         10  Z-DATE-YY-MM-DD-3.\n003048             15  Z-DATE-YY-3         PIC S9(02) BINARY.\n003050             15  Z-DATE-MM-3         PIC S9(02) BINARY.\n003052             15  Z-DATE-DD-3         PIC S9(02) BINARY.\n003054         10  Z-DATE-JJJ-3            PIC S9(03) BINARY.\n003056         10  Z-DATE-ZZ-UU-SS-TT-3.\n003058             15  Z-DATE-ZZ-3         PIC S9(02) BINARY.\n003060             15  Z-DATE-UU-3         PIC S9(02) BINARY.\n003062             15  Z-DATE-SS-3         PIC S9(02) BINARY.\n003064             15  Z-DATE-TT-3         PIC S9(02) BINARY.\n003066         10  Z-DATE-HH-3             PIC S9(02) BINARY.\n003068         10  Z-DATE-AP-3             PIC S9(01) BINARY.\n003070             88  Z-DATE-AM-3                       VALUE +1.\n003072             88  Z-DATE-PM-3                       VALUE +2.\n003074         10  Z-DATE-MX-3             PIC S9(02) BINARY.\n003076         10  Z-DATE-DOW-3            PIC 9.\n003078         10  Z-DATE-CHARS-3.\n003080             15  Z-DATE-MMM-3        PIC  X(03).\n003082             15  Z-DATE-MONTH-3      PIC  X(09).\n003084             15  Z-DATE-DDD-3        PIC  X(03).\n003086             15  Z-DATE-DAY-3        PIC  X(09).\n003088     05  Z-DATE-UNIT-X               PIC  X(11) JUST RIGHT.\n003090     05  Z-DATE-UNIT-9 REDEFINES Z-DATE-UNIT-X\n003092                                     PIC  9(11).\n003094     05  Z-DATE-UNITS.\n003096         10  Z-DATE-C                PIC S9(11) COMP.\n003098         10  Z-DATE-Y                PIC S9(11) COMP.\n003100         10  Z-DATE-M                PIC S9(11) COMP.\n003102         10  Z-DATE-D                PIC S9(11) COMP.\n003104         10  Z-DATE-W                PIC S9(11) COMP.\n003106         10  Z-DATE-Z                PIC S9(11) COMP.\n003108         10  Z-DATE-U                PIC S9(11) COMP.\n003110         10  Z-DATE-S                PIC S9(11) COMP.\n003112         10  Z-DATE-T                PIC S9(11) COMP.\n003114     05  Z-DATE-MATH-WA.\n003116         10  Z-DATE-UNITS-WORK       PIC S9(11) COMP.\n003118         10  Z-DATE-FORMAT-WORK.\n003120             15  Z-DATE-FORMAT-CEN   PIC  9(02).\n003122             15  Z-DATE-FORMAT-YR    PIC  9(02).\n003124             15  Z-DATE-FORMAT-DAYS  PIC  9(03).\n003126         10  Z-DATE-FORMAT-JULIAN\n003128             REDEFINES\n003130             Z-DATE-FORMAT-WORK.\n003132             15  Z-DATE-JUL-YR-WORK  PIC  9(04).\n003134             15  Z-DATE-JULIAN-WORK  PIC  9(03).\n003136         10  Z-DATE-X-TO-9           PIC  9(07).\n003138         10  Z-DATE-NEG-INDICATOR    PIC S9(01)\n003140                        BINARY.\n003142             88  Z-DATE-NEGATIVE-DIFF              VALUE -1.\n003144         10  Z-DATE-JULIAN-1         PIC S9(07) COMP.\n003146         10  Z-DATE-JULIAN-2         PIC S9(07) COMP.\n003148         10  Z-DATE-TEMP-HOLD        PIC S9(04) BINARY.\n003150         10  Z-DATE-HOLD-JJJ         PIC S9(03) BINARY.\n003152         10  Z-DATE-JJJ-1-WORK       PIC S9(03) BINARY.\n003154         10  Z-DATE-JJJ-2-WORK       PIC S9(03) BINARY.\n003156         10  Z-DATE-WORK-YR-1        PIC S9(04) BINARY.\n003158         10  Z-DATE-WORK-YR-2        PIC S9(04) BINARY.\n003160         10  Z-DATE-HOLD-YEAR        PIC S9(04) BINARY.\n003162         10  Z-DATE-COMPARE-1.\n003164             15 Z-DATE-CC-1-COMPARE  PIC  9(02).\n003166             15 Z-DATE-YY-1-COMPARE  PIC  9(02).\n003168             15 Z-DATE-JJ-1-COMPARE  PIC  9(03).\n003170             15 Z-DATE-MM-1-COMPARE  PIC  9(02).\n003172             15 Z-DATE-MX-1-COMPARE  PIC  9(02).\n003174             15 Z-DATE-DD-1-COMPARE  PIC  9(02).\n003176             15 Z-DATE-ZZ-1-COMPARE  PIC  9(02).\n003178             15 Z-DATE-UU-1-COMPARE  PIC  9(02).\n003180             15 Z-DATE-SS-1-COMPARE  PIC  9(02).\n003182             15 Z-DATE-TT-1-COMPARE  PIC  9(02).\n003184         10  Z-DATE-COMPARE-TEMP REDEFINES\n003186             Z-DATE-COMPARE-1        PIC  X(21).\n003188         10  Z-DATE-COMPARE-2.\n003190             15 Z-DATE-CC-2-COMPARE  PIC  9(02).\n003192             15 Z-DATE-YY-2-COMPARE  PIC  9(02).\n003194             15 Z-DATE-JJ-2-COMPARE  PIC  9(03).\n003196             15 Z-DATE-MM-2-COMPARE  PIC  9(02).\n003198             15 Z-DATE-MX-2-COMPARE  PIC  9(02).\n003200             15 Z-DATE-DD-2-COMPARE  PIC  9(02).\n003202             15 Z-DATE-ZZ-2-COMPARE  PIC  9(02).\n003204             15 Z-DATE-UU-2-COMPARE  PIC  9(02).\n003206             15 Z-DATE-SS-2-COMPARE  PIC  9(02).\n003208             15 Z-DATE-TT-2-COMPARE  PIC  9(02).\n003210         10  Z-DATE-COMPARE-3.\n003212             15 Z-DATE-CC-3-COMPARE  PIC  9(02).\n003214             15 Z-DATE-YY-3-COMPARE  PIC  9(02).\n003216             15 Z-DATE-JJ-3-COMPARE  PIC  9(03).\n003218             15 Z-DATE-MM-3-COMPARE  PIC  9(02).\n003220             15 Z-DATE-MX-3-COMPARE  PIC  9(02).\n003222             15 Z-DATE-DD-3-COMPARE  PIC  9(02).\n003224             15 Z-DATE-ZZ-3-COMPARE  PIC  9(02).\n003226             15 Z-DATE-UU-3-COMPARE  PIC  9(02).\n003228             15 Z-DATE-SS-3-COMPARE  PIC  9(02).\n003230             15 Z-DATE-TT-3-COMPARE  PIC  9(02).\n003232     05  Z-DATE-JUL-MDY-CONVERSIONS-WA.\n003234         10  Z-DATE-MDY-STRING       PIC  9(06).\n003236         10  Z-DATE-MDY\n003238             REDEFINES\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    283 lines from 1333 to 1615.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 4, "total_chunks": 55, "start_line": 1333, "end_line": 1615, "line_count": 283}

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
- Source code length: 19805 characters

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
CHUNK 4 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 1333 to 1615 (283 lines)
Chunk Tokens (estimated): ~5,572
Actual Input Tokens: 6,978 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 1333-1615 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 4 of 55 chunks
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
      The source code below is only CHUNK 4 of 55.


=============================================================================
CHUNK 4 SOURCE CODE (Lines 1333-1615)
=============================================================================

```cobol
002674 01  Z-VALUED-AREA.
002676*
002678     05  Z-FILE1-FILENAME       PIC X(30) VALUE "TDARESTART".
002680     05  Z-FILE3-FILENAME       PIC X(30) VALUE "BK-SPEC-FILE".
002682     05  Z-FILE4-FILENAME       PIC X(30) VALUE "PROC-FILE".
002684     05  Z-FILE5-FILENAME       PIC X(30) VALUE "DST-FILE-MAINT".
002686     05  Z-FILE6-FILENAME       PIC X(30) VALUE "CST-FILE-MAINT".
002688     05  Z-FILE7-FILENAME       PIC X(30) VALUE "SPCPRT".
002690     05  Z-FILE8-FILENAME       PIC X(30) VALUE "TDAACCT".
002692     05  Z-FILE9-FILENAME       PIC X(30) VALUE "TDAREPORTS".
002694     05  Z-FILE10-FILENAME      PIC X(30) VALUE "TDAPCR".
002696     05  Z-FILE11-FILENAME      PIC X(30) VALUE "TDACUST".
002698     05  Z-FILE12-FILENAME      PIC X(30) VALUE "TDAIRA".
002700     05  Z-FILE13-FILENAME      PIC X(30) VALUE "TDADISTR".
002702     05  Z-FILE14-FILENAME      PIC X(30) VALUE "TDAACTV".
002704*
002706     05  Z-FL-MSG-LIT-1.
002708         10  FILLER     PIC X(17) VALUE "CORRUPT KEY FILE ".
002710         10  Z-FL-MSG-LIT-1-1 PIC X(30).
002712     05  Z-FL-MSG-LIT-2.
002714         10  FILLER     PIC X(32) VALUE
002716                        "INVALID REWRITE OF FIRST RECORD.".
002718     05  Z-FL-MSG-LIT-3.
002720         10  FILLER     PIC X(18) VALUE "MUST REBUILD KEYS.".
002722     05  Z-FL-MSG-LIT-4.
002724         10  FILLER     PIC X(24) VALUE
002726                        "PRIOR READ REQUIRED FOR ".
002728         10  Z-FL-MSG-LIT-4-1 PIC X(30).
002730         10  FILLER     PIC X(06) VALUE " AT   ".
002732         10  Z-FL-MSG-LIT-4-2 PIC 9(8).
002734         10  FILLER     PIC X(12) VALUE SPACES.
002736     05  Z-FL-MSG-LIT-5.
002738         10  FILLER     PIC X(22) VALUE ">>>>>> ABORT PROGRAM: ".
002740         10  Z-FL-MSG-LIT-5-1 PIC X(30).
002742     05  Z-FL-MSG-LIT-6.
002744         10  FILLER     PIC X(22) VALUE "SIZE ERROR DETECTED,  ".
002746         10  Z-FL-MSG-LIT-6-1 PIC X(30).
002748         10  FILLER     PIC X(12) VALUE " STATEMENT: ".
002750         10  Z-FL-MSG-LIT-6-2 PIC 9(8).
002752     05  Z-FL-MSG-LIT-7.
002754         10  FILLER     PIC X(12) VALUE "PROGRAM ID: ".
002756         10  Z-FL-MSG-LIT-7-1 PIC X(30).
002758     05  Z-FL-MSG-LIT-8.
002760         10  FILLER     PIC X(22) VALUE " STATEMENT TYPE     : ".
002762         10  Z-FL-MSG-LIT-8-1 PIC X(58).
002764     05  Z-FL-MSG-LIT-9.
002766         10  FILLER     PIC X(22) VALUE " STATEMENT NUMBER   : ".
002768         10  Z-FL-MSG-LIT-9-1 PIC 9(8).
002770     05  Z-FL-MSG-LIT-12.
002772         10  FILLER     PIC X(24) VALUE
002774                        "CURRENT PROCEDURE     : ".
002776         10  Z-FL-MSG-LIT-12-1 PIC X(56).
002778     05  Z-FL-MSG-LIT-13.
002780         10  FILLER     PIC X(24) VALUE
002782                        "CURRENT PROCESS       : ".
002784         10  Z-FL-MSG-LIT-13-1 PIC X(56).
002786     05  Z-FL-MSG-LIT-14.
002788         10  FILLER     PIC X(24) VALUE
002790                        "PRIOR READ REQUIRED FOR ".
002792         10  Z-FL-MSG-LIT-14-1 PIC X(30).
002794         10  FILLER     PIC X(4)  VALUE " AT ".
002796         10  Z-FL-MSG-LIT-14-2 PIC 9(8).
002798     05  Z-FL-MSG-LIT-10.
002800         10  FILLER     PIC X(24) VALUE
002802                        "KEY ALTERED ON CHANGE : ".
002804         10  Z-FL-MSG-LIT-10-1 PIC X(56).
002806         10  FILLER     PIC X(4)  VALUE " AT ".
002808         10  Z-FL-MSG-LIT-10-2 PIC 9(8).
002810     05  Z-FL-MSG-LIT-11.
002812         10  FILLER     PIC X(32) VALUE
002814                       "REWRITE SKIPPED FROM REQUEST AT ".
002816         10  Z-FL-MSG-LIT-11-1 PIC 9(8).
002818     05  Z-FL-MSG-LIT-15.
002820         10  FILLER     PIC X(13) VALUE ">>>> REQUEST ".
002822         10  Z-FL-MSG-LIT-15-1 PIC X(10).
002824         10  FILLER     PIC X(10) VALUE " FILE     ".
002826         10  Z-FL-MSG-LIT-15-2 PIC X(30).
002828         10  FILLER     PIC X(11) VALUE " FAILED AT ".
002830         10  Z-FL-MSG-LIT-15-3 PIC 9(8).
002832     05  Z-FL-MSG-LIT-16.
002834         10  FILLER     PIC X(37) VALUE
002836                        ">>>> INVALID VARIABLE FORMAT NUMBER: ".
002838         10  Z-FL-MSG-LIT-16-1 PIC 9(8).
002840     05  Z-FL-MSG-LIT-17.
002842         10  FILLER     PIC X(20) VALUE "PRIOR READ REQUIRED ".
002844     05  Z-FL-MSG-LIT-18.
002846         10  FILLER     PIC X(24) VALUE
002848                        "ERROR READING BASE FILE ".
002850         10  Z-FL-MSG-LIT-18-1 PIC X(30).
002852     05  Z-FL-MSG-LIT-19.
002854         10  FILLER     PIC X(24) VALUE
002856                        "ERROR BUILDING KEYS FOR ".
002858         10  Z-FL-MSG-LIT-19-1 PIC X(30).
002860*
002862     05  Z-FL-MSG-LIT-REQS.
002864         10  FILLER     PIC X(9) VALUE "CHANGEKEY".
002866         10  FILLER     PIC X(9) VALUE "CHANGE   ".
002868         10  FILLER     PIC X(9) VALUE "DELETE   ".
002870         10  FILLER     PIC X(9) VALUE "DELETEADD".
002872         10  FILLER     PIC X(9) VALUE "LINK     ".
002874         10  FILLER     PIC X(9) VALUE "ADD      ".
002876     05  Z-FL-MSG-LIT-REDEF REDEFINES Z-FL-MSG-LIT-REQS.
002878         10  Z-FL-MSG-LIT-OCC OCCURS 6 PIC X(9).
002880*
002882     05  Z-ERR-MSG-LIT-1.
002884         10  FILLER     PIC X(22) VALUE ">>>>>> ABORT PROGRAM: ".
002886         10  Z-ERR-MSG-LIT-1-1 PIC X(30).
002888     05  Z-ERR-MSG-LIT-2.
002890         10  FILLER     PIC X(22) VALUE "SIZE ERROR DETECTED,  ".
002892         10  Z-ERR-MSG-LIT-2-1 PIC X(10).
002894         10  FILLER     PIC X(12) VALUE " STATEMENT: ".
002896         10  Z-ERR-MSG-LIT-2-2 PIC 9(8).
002898     05  Z-ERR-MSG-LIT-3.
002900         10  FILLER     PIC X(12) VALUE "PROGRAM ID: ".
002902         10  Z-ERR-MSG-LIT-3-1 PIC X(30).
002904     05  Z-ERR-MSG-LIT-4.
002906         10  FILLER     PIC X(22) VALUE " STATEMENT TYPE     : ".
002908         10  Z-ERR-MSG-LIT-4-1 PIC X(58).
002910     05  Z-ERR-MSG-LIT-5.
002912         10  FILLER     PIC X(22) VALUE " STATEMENT NUMBER   : ".
002914         10  Z-ERR-MSG-LIT-5-1 PIC 9(8).
002916*
002918     05  Z-ERR-MSG-STMTS.
002920         10  FILLER     PIC X(8) VALUE "     ADD".
002922         10  FILLER     PIC X(8) VALUE " COMPUTE".
002924         10  FILLER     PIC X(8) VALUE "  DIVIDE".
002926         10  FILLER     PIC X(8) VALUE "MULTIPLY".
002928         10  FILLER     PIC X(8) VALUE "SUBTRACT".
002930         10  FILLER     PIC X(8) VALUE " UNKNOWN".
002932     05  Z-ERR-MSG-STMTS-REDEF REDEFINES Z-ERR-MSG-STMTS.
002934         10  Z-ERR-STMT-OCC OCCURS 6 PIC X(8).
002936     05  Z-RPT-1-PAGE-SIZE                      PIC S9(6)
002938                                                VALUE +57.
002940     05  Z-RPT-2-PAGE-SIZE                      PIC S9(6)
002942                                                VALUE +57.
002944******         WORKING-STORAGE FOR ALL DATE ROUTINES    ******
002946     05  Z-MINUS-ONE                 PIC S9(01).
002948     05  Z-DATE-1-HOLD-AREA          PIC X(100).
002950     05  Z-DATE-1.
002952         10  Z-DATE-CC-1             PIC S9(02) BINARY.
002954         10  Z-DATE-YY-MM-DD-1.
002956             15  Z-DATE-YY-1         PIC S9(02) BINARY.
002958             15  Z-DATE-MM-1         PIC S9(02) BINARY.
002960             15  Z-DATE-DD-1         PIC S9(02) BINARY.
002962         10  Z-DATE-JJJ-1            PIC S9(03) BINARY.
002964         10  Z-DATE-ZZ-UU-SS-TT-1.
002966             15  Z-DATE-ZZ-1         PIC S9(02) BINARY.
002968             15  Z-DATE-UU-1         PIC S9(02) BINARY.
002970             15  Z-DATE-SS-1         PIC S9(02) BINARY.
002972             15  Z-DATE-TT-1         PIC S9(02) BINARY.
002974         10  Z-DATE-HH-1             PIC S9(02) BINARY.
002976         10  Z-DATE-AP-1             PIC S9(01) BINARY.
002978             88  Z-DATE-AM-1                       VALUE +1.
002980             88  Z-DATE-PM-1                       VALUE +2.
002982         10  Z-DATE-MX-1             PIC S9(02) BINARY.
002984         10  Z-DATE-DOW-1            PIC 9.
002986         10  Z-DATE-CHARS-1.
002988             15  Z-DATE-MMM-1        PIC  X(03).
002990             15  Z-DATE-MONTH-1      PIC  X(09).
002992             15  Z-DATE-DDD-1        PIC  X(03).
002994             15  Z-DATE-DAY-1        PIC  X(09).
002996     05  Z-DATE-2.
002998         10  Z-DATE-CC-2             PIC S9(02) BINARY.
003000         10  Z-DATE-YY-MM-DD-2.
003002             15  Z-DATE-YY-2         PIC S9(02) BINARY.
003004             15  Z-DATE-MM-2         PIC S9(02) BINARY.
003006             15  Z-DATE-DD-2         PIC S9(02) BINARY.
003008         10  Z-DATE-JJJ-2            PIC S9(03) BINARY.
003010         10  Z-DATE-ZZ-UU-SS-TT-2.
003012             15  Z-DATE-ZZ-2         PIC S9(02) BINARY.
003014             15  Z-DATE-UU-2         PIC S9(02) BINARY.
003016             15  Z-DATE-SS-2         PIC S9(02) BINARY.
003018             15  Z-DATE-TT-2         PIC S9(02) BINARY.
003020         10  Z-DATE-HH-2             PIC S9(02) BINARY.
003022         10  Z-DATE-AP-2             PIC S9(01) BINARY.
003024             88  Z-DATE-AM-2                       VALUE +1.
003026             88  Z-DATE-PM-2                       VALUE +2.
003028         10  Z-DATE-MX-2             PIC S9(02) BINARY.
003030         10  Z-DATE-DOW-2            PIC 9.
003032         10  Z-DATE-CHARS-2.
003034             15  Z-DATE-MMM-2        PIC  X(03).
003036             15  Z-DATE-MONTH-2      PIC  X(09).
003038             15  Z-DATE-DDD-2        PIC  X(03).
003040             15  Z-DATE-DAY-2        PIC  X(09).
003042     05  Z-DATE-3.
003044         10  Z-DATE-CC-3             PIC S9(02) BINARY.
003046         10  Z-DATE-YY-MM-DD-3.
003048             15  Z-DATE-YY-3         PIC S9(02) BINARY.
003050             15  Z-DATE-MM-3         PIC S9(02) BINARY.
003052             15  Z-DATE-DD-3         PIC S9(02) BINARY.
003054         10  Z-DATE-JJJ-3            PIC S9(03) BINARY.
003056         10  Z-DATE-ZZ-UU-SS-TT-3.
003058             15  Z-DATE-ZZ-3         PIC S9(02) BINARY.
003060             15  Z-DATE-UU-3         PIC S9(02) BINARY.
003062             15  Z-DATE-SS-3         PIC S9(02) BINARY.
003064             15  Z-DATE-TT-3         PIC S9(02) BINARY.
003066         10  Z-DATE-HH-3             PIC S9(02) BINARY.
003068         10  Z-DATE-AP-3             PIC S9(01) BINARY.
003070             88  Z-DATE-AM-3                       VALUE +1.
003072             88  Z-DATE-PM-3                       VALUE +2.
003074         10  Z-DATE-MX-3             PIC S9(02) BINARY.
003076         10  Z-DATE-DOW-3            PIC 9.
003078         10  Z-DATE-CHARS-3.
003080             15  Z-DATE-MMM-3        PIC  X(03).
003082             15  Z-DATE-MONTH-3      PIC  X(09).
003084             15  Z-DATE-DDD-3        PIC  X(03).
003086             15  Z-DATE-DAY-3        PIC  X(09).
003088     05  Z-DATE-UNIT-X               PIC  X(11) JUST RIGHT.
003090     05  Z-DATE-UNIT-9 REDEFINES Z-DATE-UNIT-X
003092                                     PIC  9(11).
003094     05  Z-DATE-UNITS.
003096         10  Z-DATE-C                PIC S9(11) COMP.
003098         10  Z-DATE-Y                PIC S9(11) COMP.
003100         10  Z-DATE-M                PIC S9(11) COMP.
003102         10  Z-DATE-D                PIC S9(11) COMP.
003104         10  Z-DATE-W                PIC S9(11) COMP.
003106         10  Z-DATE-Z                PIC S9(11) COMP.
003108         10  Z-DATE-U                PIC S9(11) COMP.
003110         10  Z-DATE-S                PIC S9(11) COMP.
003112         10  Z-DATE-T                PIC S9(11) COMP.
003114     05  Z-DATE-MATH-WA.
003116         10  Z-DATE-UNITS-WORK       PIC S9(11) COMP.
003118         10  Z-DATE-FORMAT-WORK.
003120             15  Z-DATE-FORMAT-CEN   PIC  9(02).
003122             15  Z-DATE-FORMAT-YR    PIC  9(02).
003124             15  Z-DATE-FORMAT-DAYS  PIC  9(03).
003126         10  Z-DATE-FORMAT-JULIAN
003128             REDEFINES
003130             Z-DATE-FORMAT-WORK.
003132             15  Z-DATE-JUL-YR-WORK  PIC  9(04).
003134             15  Z-DATE-JULIAN-WORK  PIC  9(03).
003136         10  Z-DATE-X-TO-9           PIC  9(07).
003138         10  Z-DATE-NEG-INDICATOR    PIC S9(01)
003140                        BINARY.
003142             88  Z-DATE-NEGATIVE-DIFF              VALUE -1.
003144         10  Z-DATE-JULIAN-1         PIC S9(07) COMP.
003146         10  Z-DATE-JULIAN-2         PIC S9(07) COMP.
003148         10  Z-DATE-TEMP-HOLD        PIC S9(04) BINARY.
003150         10  Z-DATE-HOLD-JJJ         PIC S9(03) BINARY.
003152         10  Z-DATE-JJJ-1-WORK       PIC S9(03) BINARY.
003154         10  Z-DATE-JJJ-2-WORK       PIC S9(03) BINARY.
003156         10  Z-DATE-WORK-YR-1        PIC S9(04) BINARY.
003158         10  Z-DATE-WORK-YR-2        PIC S9(04) BINARY.
003160         10  Z-DATE-HOLD-YEAR        PIC S9(04) BINARY.
003162         10  Z-DATE-COMPARE-1.
003164             15 Z-DATE-CC-1-COMPARE  PIC  9(02).
003166             15 Z-DATE-YY-1-COMPARE  PIC  9(02).
003168             15 Z-DATE-JJ-1-COMPARE  PIC  9(03).
003170             15 Z-DATE-MM-1-COMPARE  PIC  9(02).
003172             15 Z-DATE-MX-1-COMPARE  PIC  9(02).
003174             15 Z-DATE-DD-1-COMPARE  PIC  9(02).
003176             15 Z-DATE-ZZ-1-COMPARE  PIC  9(02).
003178             15 Z-DATE-UU-1-COMPARE  PIC  9(02).
003180             15 Z-DATE-SS-1-COMPARE  PIC  9(02).
003182             15 Z-DATE-TT-1-COMPARE  PIC  9(02).
003184         10  Z-DATE-COMPARE-TEMP REDEFINES
003186             Z-DATE-COMPARE-1        PIC  X(21).
003188         10  Z-DATE-COMPARE-2.
003190             15 Z-DATE-CC-2-COMPARE  PIC  9(02).
003192             15 Z-DATE-YY-2-COMPARE  PIC  9(02).
003194             15 Z-DATE-JJ-2-COMPARE  PIC  9(03).
003196             15 Z-DATE-MM-2-COMPARE  PIC  9(02).
003198             15 Z-DATE-MX-2-COMPARE  PIC  9(02).
003200             15 Z-DATE-DD-2-COMPARE  PIC  9(02).
003202             15 Z-DATE-ZZ-2-COMPARE  PIC  9(02).
003204             15 Z-DATE-UU-2-COMPARE  PIC  9(02).
003206             15 Z-DATE-SS-2-COMPARE  PIC  9(02).
003208             15 Z-DATE-TT-2-COMPARE  PIC  9(02).
003210         10  Z-DATE-COMPARE-3.
003212             15 Z-DATE-CC-3-COMPARE  PIC  9(02).
003214             15 Z-DATE-YY-3-COMPARE  PIC  9(02).
003216             15 Z-DATE-JJ-3-COMPARE  PIC  9(03).
003218             15 Z-DATE-MM-3-COMPARE  PIC  9(02).
003220             15 Z-DATE-MX-3-COMPARE  PIC  9(02).
003222             15 Z-DATE-DD-3-COMPARE  PIC  9(02).
003224             15 Z-DATE-ZZ-3-COMPARE  PIC  9(02).
003226             15 Z-DATE-UU-3-COMPARE  PIC  9(02).
003228             15 Z-DATE-SS-3-COMPARE  PIC  9(02).
003230             15 Z-DATE-TT-3-COMPARE  PIC  9(02).
003232     05  Z-DATE-JUL-MDY-CONVERSIONS-WA.
003234         10  Z-DATE-MDY-STRING       PIC  9(06).
003236         10  Z-DATE-MDY
003238             REDEFINES
```

⚠️  This is the source code you must document.
    283 lines from 1333 to 1615.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

