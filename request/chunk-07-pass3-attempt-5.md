# LLM Request Debug File
Generated: 2025-11-18T18:22:25.987034

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 7/55
- **Model**: gpt-4.1
- **Chunk Number**: 7
- **Pass Number**: 3
- **Attempt Number**: 5 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,085 tokens
- **User Prompt**: ~9,318 tokens
- **Total Input**: ~11,403 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 7/55" (ID: detailed-code-explanation)

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


**CHUNK 7 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T18:05:37.383587", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 7 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 2371 to 2769 (399 lines)\nChunk Tokens (estimated): ~8,052\nActual Input Tokens: 9,458 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 2371-2769 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 7 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 7 of 55.\n\n\n=============================================================================\nCHUNK 7 SOURCE CODE (Lines 2371-2769)\n=============================================================================\n\n```cobol\n004750 01  FCTL-APPL-A16.                                               \n004752     05  FCTL-DDA-A16                 PIC 9(01) VALUE 0.          \n004754     05  FCTL-SAV-A16                 PIC 9(01) VALUE 0.          \n004756     05  FCTL-COD-A16                 PIC 9(01) VALUE 0.          \n004758     05  FCTL-IRA-A16                 PIC 9(01) VALUE 0.          \n004760     05  FCTL-CLN-A16                 PIC 9(01) VALUE 0.          \n004762     05  FCTL-ILN-A16                 PIC 9(01) VALUE 0.          \n004764     05  FCTL-ONL-A16                 PIC 9(01) VALUE 0.          \n004766     05  FCTL-MCR-A16                 PIC 9(01) VALUE 0.          \n004768     05  FCTL-GNL-A16                 PIC 9(01) VALUE 0.          \n004770                                                                  \n004772                                                                  \n004774 01  WS-MPH-DATES.                                                \n004776     05  WS-CONT-DATE-9               PIC 9(08).                  \n004778     05  WS-CONT-DATE-R REDEFINES WS-CONT-DATE-9.                 \n004780         10  WS-CONT-DATE-X           PIC X(08).                  \n004782                                                                  \n004784                                                                  \n004786 01  METALOAD-CALL-MSG.                                           \n004788     05  FILLER            PIC X(10) VALUE \"BEGIN JOB;\".          \n004790     05  FILLER            PIC X(24)                              \n004792                       VALUE \"RUN CSI/METALOAD ON OBJ;\".          \n004794     05  FILLER            PIC X(08) VALUE \"END JOB;\".            \n004796                                                                  \n004798 01  WS-CUSTM-TBL-MAX         PIC 999 VALUE 500.                  \n004800 01  WS-CUSTM-TBL-INDEX       PIC 999 VALUE 1.                    \n004802 01  WS-CUSTM-TBL-X.                                              \n004804     05  WS-CUSTM-DDN-TBLE-X    OCCURS 500 TIMES.                 \n004806         10 WS-CUSTM-TBL-DDN    PIC 9(10).                        \n004808         10 WS-CUSTM-TBL-DDN-R REDEFINES WS-CUSTM-TBL-DDN.        \n004810            15  WS-CUSTM-TBL-F7 PIC 9(07).                        \n004812            15  WS-CUSTM-TBL-L3 PIC 9(03).                        \n004814         10 WS-CUSTM-TBL-NAME   PIC X(40).                        \n004816         10 WS-CUSTM-TBL-VALUE  PIC X(40).                        \n004818         10 WS-CUSTM-TBL-FORMAT PIC X(01).                        \n004820                                                                  \n004822 01 CUSTM-MISC.                                                   \n004824    05 CSM-TAB-DP-POS            PIC 9(03)     VALUE 0.           \n004826    05 CSM-TAB-P                 PIC 9(03)     VALUE 0.           \n004828    05 CSM-B-POS                 PIC 9(03)     VALUE 0.           \n004830    05 CSM-B-POS2                PIC 9(03)     VALUE 0.           \n004832    05 CSM-B-POS3                PIC 9(03)     VALUE 0.           \n004834    05 HOLD-CSM-REC.                                              \n004836       10 CSM-DDN               PIC 9(10) VALUE 0.                \n004838       10 CSM-CUSTM-TBL-NAME    PIC X(40) VALUE SPACES.           \n004840       10 CSM-VALUE             PIC X(40) VALUE SPACES.           \n004842       10 CSM-FORMAT            PIC X(01) VALUE SPACE.            \n004844                                                                  \n004846    01  WS-CUSTM-RATE.                                            \n004848        05 WS-CUSTM-RATE-X      PIC X(9).                         \n004850        05 WS-CUSTM-RATE-R REDEFINES  WS-CUSTM-RATE-X.            \n004852           10 WS-CUSTM-RT-L     PIC 9(03).                        \n004854           10 WS-CUSTM-RT-R     PIC 9(06).                        \n004856    01  WS-CUSTM-RATE2.                                           \n004858        05 WS-CUSTM-RATE2-X    PIC X(10).                         \n004860        05 WS-CUSTM-RATE2-RD REDEFINES WS-CUSTM-RATE2-X.          \n004862           10 WS-CUSTM-RATE2-L PIC ZZ9.                           \n004864           10 WS-CUSTM-RATE2-D PIC X(01).                         \n004866           10 WS-CUSTM-RATE2-R PIC 9(06).                         \n004868                                                                  \n004870    01 WS-CUSTM-DATE1.                                            \n004872       10 WS-CUSTM-DT1          PIC X(08).                        \n004874       10 WS-CUSTM-DT1-R REDEFINES WS-CUSTM-DT1.                  \n004876          15 WS-CUSTM-DT1-CCYY  PIC 9(04).                        \n004878          15 WS-CUSTM-DT1-MM    PIC 9(02).                        \n004880          15 WS-CUSTM-DT1-DD    PIC 9(02).                        \n004882    01 WS-CUSTM-DATE2.                                            \n004884       10 WS-CUSTM-DT2          PIC X(10).                        \n004886       10 WS-CUSTM-DT2-R REDEFINES WS-CUSTM-DT2.                  \n004888          15 WS-CUSTM-DT2-MM    PIC 9(02).                        \n004890          15 WS-CUSTM-DT2-SL1   PIC X(01).                        \n004892          15 WS-CUSTM-DT2-DD    PIC 9(02).                        \n004894          15 WS-CUSTM-DT2-SL2   PIC X(01).                        \n004896          15 WS-CUSTM-DT2-CCYY  PIC 9(04).                        \n004898                                                                  \n004900    01 WS-CUSTM-PHONE1.                                           \n004902       10 WS-CUSTM-PH1          PIC X(10).                        \n004904       10 WS-CUSTM-PH1-R REDEFINES WS-CUSTM-PH1.                  \n004906          15 WS-CUSTM-PH1-AREA  PIC 9(03).                        \n004908          15 WS-CUSTM-PH1-PRE   PIC 9(03).                        \n004910          15 WS-CUSTM-PH1-SUFF  PIC 9(04).                        \n004912    01 WS-CUSTM-PHONE2.                                           \n004914       10 WS-CUSTM-PH2          PIC X(12).                        \n004916       10 WS-CUSTM-PH2-R REDEFINES WS-CUSTM-PH2.                  \n004918          15 WS-CUSTM-PH2-AREA  PIC 9(03).                        \n004920          15 WS-CUSTM-PH2-DSH1  PIC X(01).                        \n004922          15 WS-CUSTM-PH2-PRE   PIC 9(03).                        \n004924          15 WS-CUSTM-PH2-DSH2  PIC X(01).                        \n004926          15 WS-CUSTM-PH2-SUFF  PIC 9(04).                        \n004928    01 WS-CUSTM-NUMBER.                                           \n004930       10 WS-CUSTM-NBR-X        PIC X(14).                        \n004932       10 WS-CUSTM-NBR-R REDEFINES WS-CUSTM-NBR-X.                \n004934          15 WS-CUSTM-NBR       PIC ZZZZZZZZZZZZZ9.               \n004936                                                                  \n004938    01 WS-CUSTM-GRP.                                              \n004940       05 WS-CUSTM-DDN             PIC 9(10).                     \n004942       05 WS-CUSTM-VALUE           PIC X(40).                     \n004944       05 WS-CUSTM-FORMAT          PIC X(01).                     \n004946                                                                  \n004948    01 WS-CUSTM-S.                                                \n004950       03 WS-CUSTM-SIGNED.                                        \n004952          05 WS-CUST-SX               PIC X(13).                  \n004954          05 WS-CUST-SX-R REDEFINES WS-CUST-SX.                   \n004956             10 WS-CUST-SX-S9         PIC S9(11)V99.              \n004958          05 WS-CUST-SX-DISP          PIC ZZZZZZZZZZ9.99.         \n004960                                                                  \n004962                                                                  \n004964 01  WS-TP-IND                        PIC 9(2) VALUE 0.           \n004966*=================================================================\n004968*                    PRINTER WORKING-STORAGE                      \n004970*=================================================================\n004972 01  PRT-FILE-STATUS                 PIC 9(01) VALUE 0.           \n004974     88  PRT-CLOSE                   VALUE 0.                     \n004976     88  PRT-OPEN                    VALUE 1.                     \n004978 01  PRT-FILE-STATUS-160             PIC 9(01) VALUE 0.           \n004980     88  PRT-CLOSE-160               VALUE 0.                     \n004982     88  PRT-OPEN-160                VALUE 1.                     \n004984 01  PAGE-ADVANCE                    PIC 9(01) VALUE 0.           \n004986     88  NEW-PAGE                    VALUE 1.                     \n004988 01  COBOL74-CODE                    PIC 9(01) VALUE 0.           \n004990     88  COBOL-74                    VALUE 1.                     \n004992 01  CSI-DUP-PRT-FLG                 PIC 9(01) VALUE 0.           \n004994 01  CSI-DUP-LINES                   PIC 9(07) VALUE 0.           \n004996 01  ID-FILE-NAME.                                                \n004998     05 ID-FI-NAME                   PIC X(50).                   \n005000     05 FILLER                       PIC X(01) VALUE \".\".         \n005002 01  ID-FILE-NAME-160.                                            \n005004     05 ID-FI-NAME-160               PIC X(50).                   \n005006     05 FILLER                       PIC X(01) VALUE \".\".         \n005008 01  ID-FAMILY-NAME.                                              \n005010     05 ID-FAM-NAME                  PIC X(12).                   \n005012     05 FILLER                       PIC X(01) VALUE \".\".         \n005014 01  ID-FAMILY-NAME-160.                                          \n005016     05 ID-FAM-NAME-160              PIC X(12).                   \n005018     05 FILLER                       PIC X(01) VALUE \".\".         \n005020 01  HEADER-LINE1.                                                \n005022     05  H-BANK-DATA.                                             \n005024         10  FILLER                  PIC X(02)  VALUE \" /\".       \n005026         10  H-CSI-BR-NO             PIC X(02)  VALUE SPACES.     \n005028         10  H-BANK-NO-9             PIC Z999 VALUE ZEROS.        \n005030         10  H-BANK-NO-9X REDEFINES H-BANK-NO-9.                  \n005032             15  H-PERIOD            PIC X(01).                   \n005034             15  H-BANK-NO           PIC X(03).                   \n005036         10  FILLER                  PIC X(02)  VALUE \"/ \".       \n005038         10  H-BANK-NAME             PIC X(30)  VALUE SPACES.     \n005040         10  FILLER                  PIC X(01)  VALUE SPACES.     \n005042     05  H-REPORT-TITLE.                                          \n005044         10  H-RPT-TITLE.                                         \n005046             15  H-RPT-TITLE1X4      PIC X(04)  VALUE SPACES.     \n005048             15  H-RPT-TITLE5X39     PIC X(39)  VALUE SPACES.     \n005050         10  H-REPORT-NO             PIC X(07)  VALUE SPACES.     \n005052     05  FILLER                      PIC X(01)  VALUE SPACES.     \n005054     05  H-CSI-TIME.                                              \n005056         10  FILLER                  PIC X(03) VALUE \"CSI\".       \n005058         10  H-CSI-DD                PIC 9(02).                   \n005060         10  H-CSI-HHMM              PIC 9(04).                   \n005062     05  FILLER                      PIC X(01)  VALUE SPACES.     \n005064     05  H-COPIES                    PIC X(01)  VALUE SPACES.     \n005066     05  FILLER                      PIC X(01)  VALUE SPACES.     \n005068     05  H-DATE                      PIC 99/99/99.                \n005070     05  H-DATE-R                REDEFINES      H-DATE.           \n005072         10  H-MM                    PIC 9(02).                   \n005074         10  FILLER                  PIC X(01).                   \n005076         10  H-DD                    PIC 9(02).                   \n005078         10  FILLER                  PIC X(01).                   \n005080         10  H-YY                    PIC 9(02).                   \n005082     05  FILLER                      PIC X(02)  VALUE SPACES.     \n005084     05  H-DATE2                     PIC X(05)  VALUE SPACES.     \n005086*                                                                 \n005088     05  FILLER                      PIC X(02)  VALUE SPACES.     \n005090     05  HEADER-PAGE.                                             \n005092         10  H-PAGE-CST              PIC X(04)  VALUE \"PAGE\".     \n005094         10  H-PAGE-NO-X.                                         \n005096             15  H-PAGE-NO           PIC ZZZZ   VALUE SPACES.     \n005098     05  FILLER                      PIC X(03)  VALUE SPACES.     \n005100     05  FILLER                      PIC X(17)  VALUE SPACES.     \n005102     05  HEADER-PAGE-160.                                         \n005104         10  H-PAGE-CST-160          PIC X(04)  VALUE SPACES.     \n005106         10  H-PAGE-NO-160-X.                                     \n005108             15  H-PAGE-NO-160       PIC ZZZZ   VALUE SPACES.     \n005110     05  FILLER                      PIC X(03)  VALUE SPACES.     \n005112 01  HEADER-80-LINE1.                                             \n005114     05  H-80-BK-DATA.                                            \n005116         10  FILLER                  PIC X(10) VALUE SPACES.      \n005118         10  H-80-RPT-TITLE.                                      \n005120             15  FILLER              PIC X(32) VALUE SPACES.      \n005122             15  H-80-CSI-TIME       PIC X(09) VALUE SPACES.      \n005124             15  FILLER              PIC X(02) VALUE SPACES.      \n005126     05  H-80-RPT-NO                 PIC X(07) VALUE SPACES.      \n005128     05  FILLER                      PIC X(02) VALUE SPACES.      \n005130     05  H-80-DATE                   PIC X(08) VALUE SPACES.      \n005132     05  FILLER                      PIC X(06) VALUE \"  PAGE\".    \n005134     05  H-80-PAGE-NO                PIC X(04) VALUE SPACES.      \n005136 01  HEADER-LINE2                    PIC X(132)  VALUE SPACES.    \n005138 01  HEADER-LINE3                    PIC X(132)  VALUE SPACES.    \n005140 01  HEADER-LINE4                    PIC X(132)  VALUE SPACES.    \n005142 01  HEADER-LINE5                    PIC X(132)  VALUE SPACES.    \n005144 01  HEADER-LINE6                    PIC X(132)  VALUE SPACES.    \n005146 01  HEADER-LINE2-160                PIC X(160)  VALUE SPACES.    \n005148 01  HEADER-LINE3-160                PIC X(160)  VALUE SPACES.    \n005150 01  HEADER-LINE4-160                PIC X(160)  VALUE SPACES.    \n005152 01  HEADER-LINE5-160                PIC X(160)  VALUE SPACES.    \n005154 01  HEADER-LINE6-160                PIC X(160)  VALUE SPACES.    \n005156 01  WS-REDEFINE-AREA-1.                                          \n005158     02  ID-PRT74-2.                                              \n005160     05 ID-PRT.                                                   \n005162         10  PRT-ID-PACK             PIC X(10) VALUE SPACES.      \n005164         10  PRT-ID-FAMILY           PIC X(10) VALUE \"CSI0P1SP\".  \n005166         10  PRT-ID-ELEM.                                         \n005168             15  PRT-ID-ELEM1-4      PIC X(04) VALUE \"0000\".      \n005170             15  FILLER              PIC X(06) VALUE SPACES.      \n005172     05  FILLER                      PIC X(20) VALUE SPACES.      \n005174     05  ID-PRT74-PERIOD             PIC X(01) VALUE SPACE.       \n005176     02  ID-PRT74-R REDEFINES ID-PRT74-2.                         \n005178     05  ID-PRT74-1-20.                                           \n005180         10  ID-PRT74-1-15           PIC X(15).                   \n005182         10  FILLER                  PIC X(05).                   \n005184     05  FILLER                      PIC X(31).                   \n005186     02  ID-PRT74-R1 REDEFINES ID-PRT74-2.                        \n005188     05  ID-PRT74-PREFX              PIC X(21).                   \n005190     05  FILLER                      PIC X(30).                   \n005192     02  ID-PRT74-R2 REDEFINES ID-PRT74-2.                        \n005194     05  ID-PRT74-1-36               PIC X(36).                   \n005196     05  FILLER                      PIC X(15).                   \n005198     02  ID-PRT74-R3 REDEFINES ID-PRT74-2.                        \n005200     05  FILLER                      PIC X(33).                   \n005202     05  ID-PRT74-34-36              PIC X(03).                   \n005204     05  FILLER                      PIC X(15).                   \n005206     02  ID-PRT160.                                               \n005208     05  FILLER                      PIC X(15).                   \n005210     05  ID-PRT160-TYPE              PIC X(02).                   \n005212     05  FILLER                      PIC X(14).                   \n005214     05  ID-PRT160-TYPE2             PIC X(02).                   \n005216     05  FILLER                      PIC X(17).                   \n005218     05  ID-PRT160-PERIOD            PIC X(01) VALUE SPACE.       \n005220     02  GWS-PRINT-LABEL-LONG.                                    \n005222   03  GWS-LPRT-NAMES.                                            \n005224     05  GWS-LPRT-CST                PIC X(03) VALUE SPACES.      \n005226     05  GWS-LPRT-S1                 PIC X(01) VALUE SPACES.      \n005228     05  GWS-LPRT-DC                 PIC 9(02) VALUE ZEROES.      \n005230     05  GWS-LPRT-S2                 PIC X(01) VALUE SPACES.      \n005232     05  GWS-LPRT-APP                PIC X(03) VALUE SPACES.      \n005234     05  GWS-LPRT-S3                 PIC X(01) VALUE SPACES.      \n005236     05  GWS-LPRT-PART-1             PIC X(01) VALUE SPACES.      \n005238     05  GWS-LPRT-PART-2             PIC X(01) VALUE SPACES.      \n005240     05  GWS-LPRT-TYPE               PIC X(02) VALUE SPACES.      \n005242     05  GWS-LPRT-S4                 PIC X(01) VALUE SPACES.      \n005244     05  GWS-LPRT-BK                 PIC 9(03) VALUE ZEROES.      \n005246     05  GWS-LPRT-S5                 PIC X(01) VALUE SPACES.      \n005248     05  GWS-LPRT-FICHE              PIC X(01) VALUE SPACES.      \n005250     05  GWS-LPRT-TIMESTAMP          PIC X(06) VALUE SPACES.      \n005252     05  GWS-LPRT-ON                 PIC X(04) VALUE \" ON \".      \n005254     05  GWS-LPRT-PACK               PIC X(10) VALUE SPACES.      \n005256     05  FILLER                      PIC X(05) VALUE SPACES.      \n005258     05  GWS-LPRT-PERIOD             PIC X(01) VALUE SPACES.      \n005260     02  GWS-EOY-PRT-NAME  REDEFINES GWS-PRINT-LABEL-LONG.        \n005262     05  GWS-EOY-CST                 PIC X(03).                   \n005264     05  GWS-EOY-FICHE               PIC X(01).                   \n005266     05  GWS-EOY-P                   PIC X(01).                   \n005268     05  GWS-EOY-DC                  PIC 9(02).                   \n005270     05  GWS-EOY-BANK                PIC 9(03).                   \n005272     05  GWS-EOY-S1                  PIC X(01).                   \n005274     05  GWS-EOY-APP                 PIC X(03).                   \n005276     05  GWS-EOY-S2                  PIC X(01).                   \n005278     05  GWS-EOY-PART-1              PIC X(01).                   \n005280     05  GWS-EOY-PART-2              PIC X(01).                   \n005282     05  GWS-EOY-TYPE                PIC X(02).                   \n005284     05  GWS-EOY-S3                  PIC X(01).                   \n005286     05  GWS-EOY-MISC                PIC X(01).                   \n005288     05  GWS-EOY-TIMESTAMP           PIC X(06).                   \n005290     05  FILLER                      PIC X(20).                   \n005292     02  GWS-LPRT-LABEL REDEFINES GWS-PRINT-LABEL-LONG.           \n005294     05  GWS-LPRT-PREFX              PIC X(21).                   \n005296     05  GWS-LPRT-LABEL-ELEM         PIC X(06).                   \n005298     05  FILLER                      PIC X(20).                   \n005300     02  GWS-RMT-PRT-LABEL.                                       \n005302     05  GWS-RMT-FAMILY.                                          \n005304         10  FILLER                  PIC X(04) VALUE \"RMT0\".      \n005306         10  GWS-RMT-FILE-TYPE       PIC X(01) VALUE \"P\".         \n005308         10  GWS-RMT-LBL-BR          PIC X(02) VALUE \"00\".        \n005310         10  GWS-RMT-LBL-BK          PIC X(03) VALUE \"000\".       \n005312     05  FILLER                      PIC X(01) VALUE \"/\".         \n005314     05  GWS-RMT-ELEM.                                            \n005316         10  GWS-RMT-DD              PIC 9(02) VALUE 0.           \n005318         10  GWS-RMT-APPL            PIC X(01) VALUE \"0\".         \n005320         10  GWS-RMT-DESCRIPTOR      PIC X(02) VALUE \"SP\".        \n005322         10  GWS-RMT-FICHE-COPIES    PIC X(01) VALUE \"0\".         \n005324         10  GWS-RMT-RPT-NO          PIC X(03) VALUE SPACES.      \n005326     05  GWS-RMT-ON                  PIC X(04) VALUE \" ON\".       \n005328     05  GWS-RMT-PACK                PIC X(10) VALUE SPACES.      \n005330     05  GWS-RMT-PERIOD              PIC X(01) VALUE SPACES.      \n005332     02  GWS-RMT-LABEL   REDEFINES GWS-RMT-PRT-LABEL.             \n005334     05  GWS-RMT-LABEL-1-20          PIC X(20).                   \n005336     05  FILLER                      PIC X(15).                   \n005338 01  GWS-TIME-CTL                    PIC 9(01) VALUE 0.           \n005340 01  GWS-RMT-BK-SPEC-HOLD            PIC X(80).                   \n005342 01  GWS-RMT-BK-SPEC-HOLD-82X        PIC X(82).                   \n005344 01  GWS-AX-CHAR                     PIC X(01) VALUE SPACE.       \n005346 01  GWS-A12-PERIOD                  PIC X(01) VALUE \".\".         \n005348 01  GWS-A12-SYS                     PIC 9(01) VALUE 1.           \n005350 01  GWS-LONG-PRTNAMES               PIC 9(01) VALUE 0.           \n005352 01  GWS-CSI-DC                      PIC 9(02) VALUE 0.           \n005354 01  GWS-CSI-BK                      PIC 9(04) VALUE 0.           \n005356 01  RPT-CTR                         PIC 9(02) VALUE 0.           \n005358                                                                  \n005360 01  RPT-CTR2                        PIC 9(02) VALUE 0.           \n005362 01  GWS-PRT-PID                     PIC X(10) VALUE \"GENERAL\".   \n005364 01  GWS-PRT-PID-FICHE               PIC X(10) VALUE \"GENERAL\".   \n005366 01  GWS-PRT-PID-FLAG                PIC 9(01) VALUE 0.           \n005368 01  GWS-REL-DUMMY-AREA.                                          \n005370     05  GWS-PRT-REL-FLAG            PIC X(01) VALUE \"N\".         \n005372     05  GWS-PRT-DUMMY               PIC X(05) VALUE SPACES.      \n005374 01  GWS-PRT-EXC-FLAG                PIC X(01) VALUE SPACES.      \n005376 01  GWS-80-CHAR-PRT-FLAG            PIC 9(01) VALUE 0.           \n005378 01  GWS-SPEC-BK-NAME                    PIC X(30) VALUE SPACES.  \n005380 01  GWS-SPEC-BK-ADD1                    PIC X(30) VALUE SPACES.  \n005382 01  GWS-SPEC-BK-ADD2                    PIC X(30) VALUE SPACES.  \n005384 01  GWS-HOLD-NAME                       PIC X(30) VALUE SPACES.  \n005386 01  WS-REDEFINE-AREA-2.                                          \n005388     02  GWS-RPT-NO-PRT-LINE              PIC X(132).             \n005390     02  GWS-RPT-LINE    REDEFINES GWS-RPT-NO-PRT-LINE.           \n005392     05  GWS-RPT-BR-BK.                                           \n005394         10  FILLER                  PIC X(03).                   \n005396         10  GWS-RPT-BR              PIC X(02).                   \n005398         10  FILLER                  PIC X(04).                   \n005400         10  GWS-RPT-BK              PIC X(03).                   \n005402     05  FILLER                      PIC X(02).                   \n005404     05  GWS-RPT-NO-LINE OCCURS 8 TIMES.                          \n005406         10  GWS-RPT-PRT-REM         PIC X(07).                   \n005408         10  GWS-RPT-PRT-NO          PIC Z(06).                   \n005410         10  FILLER                  PIC X(01).                   \n005412     05  FILLER                      PIC X(06).                   \n005414                                                                  \n005416     02  GWS-RPT-TABLE                    PIC X(312).             \n005418     02  GWS-RPT-TABLE-R REDEFINES GWS-RPT-TABLE.                 \n005420     05  GWS-RPT-NO-CNT              OCCURS 24 TIMES.             \n005422         10  GWS-RPT-NO              PIC X(07).                   \n005424         10  GWS-RPT-LINES           PIC 9(06).                   \n005426     02  H-TIME                          PIC X(05).               \n005428     02  PRT-OPEN-TIME                   PIC 9(08) COMP.          \n005430     02  PRT-OPEN-TIME-R REDEFINES PRT-OPEN-TIME.                 \n005432     05  PRT-OPEN-HHMM               PIC 9(04) COMP.              \n005434     05  FILLER                      PIC 9(04) COMP.              \n005436     02  PRT-OPEN-DATE                   PIC 9(06) COMP.          \n005438     02  PRT-OPEN-DATE-R REDEFINES PRT-OPEN-DATE.                 \n005440     05  PRT-OPEN-MM                 PIC 9(02) COMP.              \n005442     05  PRT-OPEN-DD                 PIC 9(02) COMP.              \n005444     05  PRT-OPEN-YY                 PIC 9(02) COMP.              \n005446     02  TEAR-PAGE-IN.                                            \n005448     05  TP-LN1.                                                  \n005450         10  TP-LN-BANK              PIC X(04) VALUE \"BK\".        \n005452         10  TP-LN-BKNO              PIC X(04) VALUE SPACES.      \n005454     05  TP-LN2                      PIC X(08) VALUE SPACES.      \n005456     05  TP-LN-DATE REDEFINES TP-LN2 PIC 99/99/99.                \n005458     05  TP-LN3                      PIC X(08) VALUE SPACES.      \n005460     02  TEAR-PG-IN REDEFINES TEAR-PAGE-IN.                       \n005462     05  TP-IN-CHAR                  PIC X(01) OCCURS 24 TIMES.   \n005464     02  TP-CHAR-ARRAY.                                           \n005466    03 FILLER PIC X(33) VALUE \"A0102010202B0302010203C0104040401\".\n005468    03 FILLER PIC X(33) VALUE \"D0302020203E0104030401F0104030404\".\n005470    03 FILLER PIC X(33) VALUE \"G0104050601H0202010202I0708080807\".\n005472    03 FILLER PIC X(33) VALUE \"J0909090201K0210111002L0404040401\".\n005474    03 FILLER PIC X(33) VALUE \"M0112121313N0614120515O0102020201\".\n005476    03 FILLER PIC X(33) VALUE \"P0102010404Q0113131501R0106011002\".\n005478    03 FILLER PIC X(33) VALUE \"S0104010901T0108080808U0202020101\".\n005480    03 FILLER PIC X(33) VALUE \"V1313020708W1313121201X0207080702\".\n005482    03 FILLER PIC X(33) VALUE \"Y0202010808Z011608170100702020207\".\n005484    03 FILLER PIC X(33) VALUE \"118080808072010901040130109010901\".\n005486    03 FILLER PIC X(33) VALUE \"410100116165010401090160404010201\".\n005488    03 FILLER PIC X(33) VALUE \"701090909098010201020190102020709\".\n005490    03 FILLER PIC X(33) VALUE \",0827303030/0916081704+0808010808\".\n005492    03 FILLER PIC X(33) VALUE \"!0808083008#2223222322$0120012101\".\n005494    03 FILLER PIC X(33) VALUE \"%2425262724*2818031828-3030073030\".\n005496    03 FILLER PIC X(33) VALUE \"=3007300730:3008300830;3008300825\".\n005498    03 FILLER PIC X(33) VALUE \"?0329192626,3030301726.3030301717\".\n005500    03 FILLER PIC X(11) VALUE \" 3030303030\".                      \n005502     02  TP-DECODE-CHAR REDEFINES TP-CHAR-ARRAY.                  \n005504     05  TP-DECODE                   PIC X(11) OCCURS 52 TIMES.   \n005506     02  TP-FORM-CHAR.                                            \n005508 05 FILLER PIC X(36) VALUE \"****************    **************  \".\n005510 05 FILLER PIC X(36) VALUE \"****        ****  **********      **\".\n005512 05 FILLER PIC X(36) VALUE \"  ********      ****            ****\".\n005514 05 FILLER PIC X(36) VALUE \"****  ****  ********    **  ****  **\".\n005516 05 FILLER PIC X(36) VALUE \"**        ********    ****      ****\".\n005518 05 FILLER PIC X(36) VALUE \"      ****    ****        ******    \".\n005520 05 FILLER PIC X(36) VALUE \"    ******  **  ****        ****  **\".\n005522 05 FILLER PIC X(36) VALUE \"    **  **    ************      **  \".\n005524 05 FILLER PIC X(36) VALUE \"      **        **        **        \".\n005526 05 FILLER PIC X(36) VALUE \"**  **  **          **              \".\n005528     02  TP-FORMCHAR REDEFINES TP-FORM-CHAR.                      \n005530     05  TPFORMCHAR                  PIC X(12) OCCURS 30 TIMES.   \n005532                                                                  \n005534 01  GWS-PRT-EXCEPT-LINE.                                         \n005536     05  GWS-PRT-EXC-BLOCK-CTL       PIC 9(02).                   \n005538     05  GWS-PRT-EXC-PAGE-CTL        PIC 9(01).                   \n005540     05  GWS-PRT-EXC-NO-LINES        PIC 9(02).                   \n005542     05  GWS-PRT-EXC-DATA-160.                                    \n005544         10  GWS-PRT-EXC-DATA        PIC X(132).                  \n005546         10  FILLER                  PIC X(028).                  \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    399 lines from 2371 to 2769.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 7, "total_chunks": 55, "start_line": 2371, "end_line": 2769, "line_count": 399}

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
- Source code length: 34075 characters

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
CHUNK 7 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 2371 to 2769 (399 lines)
Chunk Tokens (estimated): ~8,052
Actual Input Tokens: 9,458 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 2371-2769 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 7 of 55 chunks
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
      The source code below is only CHUNK 7 of 55.


=============================================================================
CHUNK 7 SOURCE CODE (Lines 2371-2769)
=============================================================================

```cobol
004750 01  FCTL-APPL-A16.                                               
004752     05  FCTL-DDA-A16                 PIC 9(01) VALUE 0.          
004754     05  FCTL-SAV-A16                 PIC 9(01) VALUE 0.          
004756     05  FCTL-COD-A16                 PIC 9(01) VALUE 0.          
004758     05  FCTL-IRA-A16                 PIC 9(01) VALUE 0.          
004760     05  FCTL-CLN-A16                 PIC 9(01) VALUE 0.          
004762     05  FCTL-ILN-A16                 PIC 9(01) VALUE 0.          
004764     05  FCTL-ONL-A16                 PIC 9(01) VALUE 0.          
004766     05  FCTL-MCR-A16                 PIC 9(01) VALUE 0.          
004768     05  FCTL-GNL-A16                 PIC 9(01) VALUE 0.          
004770                                                                  
004772                                                                  
004774 01  WS-MPH-DATES.                                                
004776     05  WS-CONT-DATE-9               PIC 9(08).                  
004778     05  WS-CONT-DATE-R REDEFINES WS-CONT-DATE-9.                 
004780         10  WS-CONT-DATE-X           PIC X(08).                  
004782                                                                  
004784                                                                  
004786 01  METALOAD-CALL-MSG.                                           
004788     05  FILLER            PIC X(10) VALUE "BEGIN JOB;".          
004790     05  FILLER            PIC X(24)                              
004792                       VALUE "RUN CSI/METALOAD ON OBJ;".          
004794     05  FILLER            PIC X(08) VALUE "END JOB;".            
004796                                                                  
004798 01  WS-CUSTM-TBL-MAX         PIC 999 VALUE 500.                  
004800 01  WS-CUSTM-TBL-INDEX       PIC 999 VALUE 1.                    
004802 01  WS-CUSTM-TBL-X.                                              
004804     05  WS-CUSTM-DDN-TBLE-X    OCCURS 500 TIMES.                 
004806         10 WS-CUSTM-TBL-DDN    PIC 9(10).                        
004808         10 WS-CUSTM-TBL-DDN-R REDEFINES WS-CUSTM-TBL-DDN.        
004810            15  WS-CUSTM-TBL-F7 PIC 9(07).                        
004812            15  WS-CUSTM-TBL-L3 PIC 9(03).                        
004814         10 WS-CUSTM-TBL-NAME   PIC X(40).                        
004816         10 WS-CUSTM-TBL-VALUE  PIC X(40).                        
004818         10 WS-CUSTM-TBL-FORMAT PIC X(01).                        
004820                                                                  
004822 01 CUSTM-MISC.                                                   
004824    05 CSM-TAB-DP-POS            PIC 9(03)     VALUE 0.           
004826    05 CSM-TAB-P                 PIC 9(03)     VALUE 0.           
004828    05 CSM-B-POS                 PIC 9(03)     VALUE 0.           
004830    05 CSM-B-POS2                PIC 9(03)     VALUE 0.           
004832    05 CSM-B-POS3                PIC 9(03)     VALUE 0.           
004834    05 HOLD-CSM-REC.                                              
004836       10 CSM-DDN               PIC 9(10) VALUE 0.                
004838       10 CSM-CUSTM-TBL-NAME    PIC X(40) VALUE SPACES.           
004840       10 CSM-VALUE             PIC X(40) VALUE SPACES.           
004842       10 CSM-FORMAT            PIC X(01) VALUE SPACE.            
004844                                                                  
004846    01  WS-CUSTM-RATE.                                            
004848        05 WS-CUSTM-RATE-X      PIC X(9).                         
004850        05 WS-CUSTM-RATE-R REDEFINES  WS-CUSTM-RATE-X.            
004852           10 WS-CUSTM-RT-L     PIC 9(03).                        
004854           10 WS-CUSTM-RT-R     PIC 9(06).                        
004856    01  WS-CUSTM-RATE2.                                           
004858        05 WS-CUSTM-RATE2-X    PIC X(10).                         
004860        05 WS-CUSTM-RATE2-RD REDEFINES WS-CUSTM-RATE2-X.          
004862           10 WS-CUSTM-RATE2-L PIC ZZ9.                           
004864           10 WS-CUSTM-RATE2-D PIC X(01).                         
004866           10 WS-CUSTM-RATE2-R PIC 9(06).                         
004868                                                                  
004870    01 WS-CUSTM-DATE1.                                            
004872       10 WS-CUSTM-DT1          PIC X(08).                        
004874       10 WS-CUSTM-DT1-R REDEFINES WS-CUSTM-DT1.                  
004876          15 WS-CUSTM-DT1-CCYY  PIC 9(04).                        
004878          15 WS-CUSTM-DT1-MM    PIC 9(02).                        
004880          15 WS-CUSTM-DT1-DD    PIC 9(02).                        
004882    01 WS-CUSTM-DATE2.                                            
004884       10 WS-CUSTM-DT2          PIC X(10).                        
004886       10 WS-CUSTM-DT2-R REDEFINES WS-CUSTM-DT2.                  
004888          15 WS-CUSTM-DT2-MM    PIC 9(02).                        
004890          15 WS-CUSTM-DT2-SL1   PIC X(01).                        
004892          15 WS-CUSTM-DT2-DD    PIC 9(02).                        
004894          15 WS-CUSTM-DT2-SL2   PIC X(01).                        
004896          15 WS-CUSTM-DT2-CCYY  PIC 9(04).                        
004898                                                                  
004900    01 WS-CUSTM-PHONE1.                                           
004902       10 WS-CUSTM-PH1          PIC X(10).                        
004904       10 WS-CUSTM-PH1-R REDEFINES WS-CUSTM-PH1.                  
004906          15 WS-CUSTM-PH1-AREA  PIC 9(03).                        
004908          15 WS-CUSTM-PH1-PRE   PIC 9(03).                        
004910          15 WS-CUSTM-PH1-SUFF  PIC 9(04).                        
004912    01 WS-CUSTM-PHONE2.                                           
004914       10 WS-CUSTM-PH2          PIC X(12).                        
004916       10 WS-CUSTM-PH2-R REDEFINES WS-CUSTM-PH2.                  
004918          15 WS-CUSTM-PH2-AREA  PIC 9(03).                        
004920          15 WS-CUSTM-PH2-DSH1  PIC X(01).                        
004922          15 WS-CUSTM-PH2-PRE   PIC 9(03).                        
004924          15 WS-CUSTM-PH2-DSH2  PIC X(01).                        
004926          15 WS-CUSTM-PH2-SUFF  PIC 9(04).                        
004928    01 WS-CUSTM-NUMBER.                                           
004930       10 WS-CUSTM-NBR-X        PIC X(14).                        
004932       10 WS-CUSTM-NBR-R REDEFINES WS-CUSTM-NBR-X.                
004934          15 WS-CUSTM-NBR       PIC ZZZZZZZZZZZZZ9.               
004936                                                                  
004938    01 WS-CUSTM-GRP.                                              
004940       05 WS-CUSTM-DDN             PIC 9(10).                     
004942       05 WS-CUSTM-VALUE           PIC X(40).                     
004944       05 WS-CUSTM-FORMAT          PIC X(01).                     
004946                                                                  
004948    01 WS-CUSTM-S.                                                
004950       03 WS-CUSTM-SIGNED.                                        
004952          05 WS-CUST-SX               PIC X(13).                  
004954          05 WS-CUST-SX-R REDEFINES WS-CUST-SX.                   
004956             10 WS-CUST-SX-S9         PIC S9(11)V99.              
004958          05 WS-CUST-SX-DISP          PIC ZZZZZZZZZZ9.99.         
004960                                                                  
004962                                                                  
004964 01  WS-TP-IND                        PIC 9(2) VALUE 0.           
004966*=================================================================
004968*                    PRINTER WORKING-STORAGE                      
004970*=================================================================
004972 01  PRT-FILE-STATUS                 PIC 9(01) VALUE 0.           
004974     88  PRT-CLOSE                   VALUE 0.                     
004976     88  PRT-OPEN                    VALUE 1.                     
004978 01  PRT-FILE-STATUS-160             PIC 9(01) VALUE 0.           
004980     88  PRT-CLOSE-160               VALUE 0.                     
004982     88  PRT-OPEN-160                VALUE 1.                     
004984 01  PAGE-ADVANCE                    PIC 9(01) VALUE 0.           
004986     88  NEW-PAGE                    VALUE 1.                     
004988 01  COBOL74-CODE                    PIC 9(01) VALUE 0.           
004990     88  COBOL-74                    VALUE 1.                     
004992 01  CSI-DUP-PRT-FLG                 PIC 9(01) VALUE 0.           
004994 01  CSI-DUP-LINES                   PIC 9(07) VALUE 0.           
004996 01  ID-FILE-NAME.                                                
004998     05 ID-FI-NAME                   PIC X(50).                   
005000     05 FILLER                       PIC X(01) VALUE ".".         
005002 01  ID-FILE-NAME-160.                                            
005004     05 ID-FI-NAME-160               PIC X(50).                   
005006     05 FILLER                       PIC X(01) VALUE ".".         
005008 01  ID-FAMILY-NAME.                                              
005010     05 ID-FAM-NAME                  PIC X(12).                   
005012     05 FILLER                       PIC X(01) VALUE ".".         
005014 01  ID-FAMILY-NAME-160.                                          
005016     05 ID-FAM-NAME-160              PIC X(12).                   
005018     05 FILLER                       PIC X(01) VALUE ".".         
005020 01  HEADER-LINE1.                                                
005022     05  H-BANK-DATA.                                             
005024         10  FILLER                  PIC X(02)  VALUE " /".       
005026         10  H-CSI-BR-NO             PIC X(02)  VALUE SPACES.     
005028         10  H-BANK-NO-9             PIC Z999 VALUE ZEROS.        
005030         10  H-BANK-NO-9X REDEFINES H-BANK-NO-9.                  
005032             15  H-PERIOD            PIC X(01).                   
005034             15  H-BANK-NO           PIC X(03).                   
005036         10  FILLER                  PIC X(02)  VALUE "/ ".       
005038         10  H-BANK-NAME             PIC X(30)  VALUE SPACES.     
005040         10  FILLER                  PIC X(01)  VALUE SPACES.     
005042     05  H-REPORT-TITLE.                                          
005044         10  H-RPT-TITLE.                                         
005046             15  H-RPT-TITLE1X4      PIC X(04)  VALUE SPACES.     
005048             15  H-RPT-TITLE5X39     PIC X(39)  VALUE SPACES.     
005050         10  H-REPORT-NO             PIC X(07)  VALUE SPACES.     
005052     05  FILLER                      PIC X(01)  VALUE SPACES.     
005054     05  H-CSI-TIME.                                              
005056         10  FILLER                  PIC X(03) VALUE "CSI".       
005058         10  H-CSI-DD                PIC 9(02).                   
005060         10  H-CSI-HHMM              PIC 9(04).                   
005062     05  FILLER                      PIC X(01)  VALUE SPACES.     
005064     05  H-COPIES                    PIC X(01)  VALUE SPACES.     
005066     05  FILLER                      PIC X(01)  VALUE SPACES.     
005068     05  H-DATE                      PIC 99/99/99.                
005070     05  H-DATE-R                REDEFINES      H-DATE.           
005072         10  H-MM                    PIC 9(02).                   
005074         10  FILLER                  PIC X(01).                   
005076         10  H-DD                    PIC 9(02).                   
005078         10  FILLER                  PIC X(01).                   
005080         10  H-YY                    PIC 9(02).                   
005082     05  FILLER                      PIC X(02)  VALUE SPACES.     
005084     05  H-DATE2                     PIC X(05)  VALUE SPACES.     
005086*                                                                 
005088     05  FILLER                      PIC X(02)  VALUE SPACES.     
005090     05  HEADER-PAGE.                                             
005092         10  H-PAGE-CST              PIC X(04)  VALUE "PAGE".     
005094         10  H-PAGE-NO-X.                                         
005096             15  H-PAGE-NO           PIC ZZZZ   VALUE SPACES.     
005098     05  FILLER                      PIC X(03)  VALUE SPACES.     
005100     05  FILLER                      PIC X(17)  VALUE SPACES.     
005102     05  HEADER-PAGE-160.                                         
005104         10  H-PAGE-CST-160          PIC X(04)  VALUE SPACES.     
005106         10  H-PAGE-NO-160-X.                                     
005108             15  H-PAGE-NO-160       PIC ZZZZ   VALUE SPACES.     
005110     05  FILLER                      PIC X(03)  VALUE SPACES.     
005112 01  HEADER-80-LINE1.                                             
005114     05  H-80-BK-DATA.                                            
005116         10  FILLER                  PIC X(10) VALUE SPACES.      
005118         10  H-80-RPT-TITLE.                                      
005120             15  FILLER              PIC X(32) VALUE SPACES.      
005122             15  H-80-CSI-TIME       PIC X(09) VALUE SPACES.      
005124             15  FILLER              PIC X(02) VALUE SPACES.      
005126     05  H-80-RPT-NO                 PIC X(07) VALUE SPACES.      
005128     05  FILLER                      PIC X(02) VALUE SPACES.      
005130     05  H-80-DATE                   PIC X(08) VALUE SPACES.      
005132     05  FILLER                      PIC X(06) VALUE "  PAGE".    
005134     05  H-80-PAGE-NO                PIC X(04) VALUE SPACES.      
005136 01  HEADER-LINE2                    PIC X(132)  VALUE SPACES.    
005138 01  HEADER-LINE3                    PIC X(132)  VALUE SPACES.    
005140 01  HEADER-LINE4                    PIC X(132)  VALUE SPACES.    
005142 01  HEADER-LINE5                    PIC X(132)  VALUE SPACES.    
005144 01  HEADER-LINE6                    PIC X(132)  VALUE SPACES.    
005146 01  HEADER-LINE2-160                PIC X(160)  VALUE SPACES.    
005148 01  HEADER-LINE3-160                PIC X(160)  VALUE SPACES.    
005150 01  HEADER-LINE4-160                PIC X(160)  VALUE SPACES.    
005152 01  HEADER-LINE5-160                PIC X(160)  VALUE SPACES.    
005154 01  HEADER-LINE6-160                PIC X(160)  VALUE SPACES.    
005156 01  WS-REDEFINE-AREA-1.                                          
005158     02  ID-PRT74-2.                                              
005160     05 ID-PRT.                                                   
005162         10  PRT-ID-PACK             PIC X(10) VALUE SPACES.      
005164         10  PRT-ID-FAMILY           PIC X(10) VALUE "CSI0P1SP".  
005166         10  PRT-ID-ELEM.                                         
005168             15  PRT-ID-ELEM1-4      PIC X(04) VALUE "0000".      
005170             15  FILLER              PIC X(06) VALUE SPACES.      
005172     05  FILLER                      PIC X(20) VALUE SPACES.      
005174     05  ID-PRT74-PERIOD             PIC X(01) VALUE SPACE.       
005176     02  ID-PRT74-R REDEFINES ID-PRT74-2.                         
005178     05  ID-PRT74-1-20.                                           
005180         10  ID-PRT74-1-15           PIC X(15).                   
005182         10  FILLER                  PIC X(05).                   
005184     05  FILLER                      PIC X(31).                   
005186     02  ID-PRT74-R1 REDEFINES ID-PRT74-2.                        
005188     05  ID-PRT74-PREFX              PIC X(21).                   
005190     05  FILLER                      PIC X(30).                   
005192     02  ID-PRT74-R2 REDEFINES ID-PRT74-2.                        
005194     05  ID-PRT74-1-36               PIC X(36).                   
005196     05  FILLER                      PIC X(15).                   
005198     02  ID-PRT74-R3 REDEFINES ID-PRT74-2.                        
005200     05  FILLER                      PIC X(33).                   
005202     05  ID-PRT74-34-36              PIC X(03).                   
005204     05  FILLER                      PIC X(15).                   
005206     02  ID-PRT160.                                               
005208     05  FILLER                      PIC X(15).                   
005210     05  ID-PRT160-TYPE              PIC X(02).                   
005212     05  FILLER                      PIC X(14).                   
005214     05  ID-PRT160-TYPE2             PIC X(02).                   
005216     05  FILLER                      PIC X(17).                   
005218     05  ID-PRT160-PERIOD            PIC X(01) VALUE SPACE.       
005220     02  GWS-PRINT-LABEL-LONG.                                    
005222   03  GWS-LPRT-NAMES.                                            
005224     05  GWS-LPRT-CST                PIC X(03) VALUE SPACES.      
005226     05  GWS-LPRT-S1                 PIC X(01) VALUE SPACES.      
005228     05  GWS-LPRT-DC                 PIC 9(02) VALUE ZEROES.      
005230     05  GWS-LPRT-S2                 PIC X(01) VALUE SPACES.      
005232     05  GWS-LPRT-APP                PIC X(03) VALUE SPACES.      
005234     05  GWS-LPRT-S3                 PIC X(01) VALUE SPACES.      
005236     05  GWS-LPRT-PART-1             PIC X(01) VALUE SPACES.      
005238     05  GWS-LPRT-PART-2             PIC X(01) VALUE SPACES.      
005240     05  GWS-LPRT-TYPE               PIC X(02) VALUE SPACES.      
005242     05  GWS-LPRT-S4                 PIC X(01) VALUE SPACES.      
005244     05  GWS-LPRT-BK                 PIC 9(03) VALUE ZEROES.      
005246     05  GWS-LPRT-S5                 PIC X(01) VALUE SPACES.      
005248     05  GWS-LPRT-FICHE              PIC X(01) VALUE SPACES.      
005250     05  GWS-LPRT-TIMESTAMP          PIC X(06) VALUE SPACES.      
005252     05  GWS-LPRT-ON                 PIC X(04) VALUE " ON ".      
005254     05  GWS-LPRT-PACK               PIC X(10) VALUE SPACES.      
005256     05  FILLER                      PIC X(05) VALUE SPACES.      
005258     05  GWS-LPRT-PERIOD             PIC X(01) VALUE SPACES.      
005260     02  GWS-EOY-PRT-NAME  REDEFINES GWS-PRINT-LABEL-LONG.        
005262     05  GWS-EOY-CST                 PIC X(03).                   
005264     05  GWS-EOY-FICHE               PIC X(01).                   
005266     05  GWS-EOY-P                   PIC X(01).                   
005268     05  GWS-EOY-DC                  PIC 9(02).                   
005270     05  GWS-EOY-BANK                PIC 9(03).                   
005272     05  GWS-EOY-S1                  PIC X(01).                   
005274     05  GWS-EOY-APP                 PIC X(03).                   
005276     05  GWS-EOY-S2                  PIC X(01).                   
005278     05  GWS-EOY-PART-1              PIC X(01).                   
005280     05  GWS-EOY-PART-2              PIC X(01).                   
005282     05  GWS-EOY-TYPE                PIC X(02).                   
005284     05  GWS-EOY-S3                  PIC X(01).                   
005286     05  GWS-EOY-MISC                PIC X(01).                   
005288     05  GWS-EOY-TIMESTAMP           PIC X(06).                   
005290     05  FILLER                      PIC X(20).                   
005292     02  GWS-LPRT-LABEL REDEFINES GWS-PRINT-LABEL-LONG.           
005294     05  GWS-LPRT-PREFX              PIC X(21).                   
005296     05  GWS-LPRT-LABEL-ELEM         PIC X(06).                   
005298     05  FILLER                      PIC X(20).                   
005300     02  GWS-RMT-PRT-LABEL.                                       
005302     05  GWS-RMT-FAMILY.                                          
005304         10  FILLER                  PIC X(04) VALUE "RMT0".      
005306         10  GWS-RMT-FILE-TYPE       PIC X(01) VALUE "P".         
005308         10  GWS-RMT-LBL-BR          PIC X(02) VALUE "00".        
005310         10  GWS-RMT-LBL-BK          PIC X(03) VALUE "000".       
005312     05  FILLER                      PIC X(01) VALUE "/".         
005314     05  GWS-RMT-ELEM.                                            
005316         10  GWS-RMT-DD              PIC 9(02) VALUE 0.           
005318         10  GWS-RMT-APPL            PIC X(01) VALUE "0".         
005320         10  GWS-RMT-DESCRIPTOR      PIC X(02) VALUE "SP".        
005322         10  GWS-RMT-FICHE-COPIES    PIC X(01) VALUE "0".         
005324         10  GWS-RMT-RPT-NO          PIC X(03) VALUE SPACES.      
005326     05  GWS-RMT-ON                  PIC X(04) VALUE " ON".       
005328     05  GWS-RMT-PACK                PIC X(10) VALUE SPACES.      
005330     05  GWS-RMT-PERIOD              PIC X(01) VALUE SPACES.      
005332     02  GWS-RMT-LABEL   REDEFINES GWS-RMT-PRT-LABEL.             
005334     05  GWS-RMT-LABEL-1-20          PIC X(20).                   
005336     05  FILLER                      PIC X(15).                   
005338 01  GWS-TIME-CTL                    PIC 9(01) VALUE 0.           
005340 01  GWS-RMT-BK-SPEC-HOLD            PIC X(80).                   
005342 01  GWS-RMT-BK-SPEC-HOLD-82X        PIC X(82).                   
005344 01  GWS-AX-CHAR                     PIC X(01) VALUE SPACE.       
005346 01  GWS-A12-PERIOD                  PIC X(01) VALUE ".".         
005348 01  GWS-A12-SYS                     PIC 9(01) VALUE 1.           
005350 01  GWS-LONG-PRTNAMES               PIC 9(01) VALUE 0.           
005352 01  GWS-CSI-DC                      PIC 9(02) VALUE 0.           
005354 01  GWS-CSI-BK                      PIC 9(04) VALUE 0.           
005356 01  RPT-CTR                         PIC 9(02) VALUE 0.           
005358                                                                  
005360 01  RPT-CTR2                        PIC 9(02) VALUE 0.           
005362 01  GWS-PRT-PID                     PIC X(10) VALUE "GENERAL".   
005364 01  GWS-PRT-PID-FICHE               PIC X(10) VALUE "GENERAL".   
005366 01  GWS-PRT-PID-FLAG                PIC 9(01) VALUE 0.           
005368 01  GWS-REL-DUMMY-AREA.                                          
005370     05  GWS-PRT-REL-FLAG            PIC X(01) VALUE "N".         
005372     05  GWS-PRT-DUMMY               PIC X(05) VALUE SPACES.      
005374 01  GWS-PRT-EXC-FLAG                PIC X(01) VALUE SPACES.      
005376 01  GWS-80-CHAR-PRT-FLAG            PIC 9(01) VALUE 0.           
005378 01  GWS-SPEC-BK-NAME                    PIC X(30) VALUE SPACES.  
005380 01  GWS-SPEC-BK-ADD1                    PIC X(30) VALUE SPACES.  
005382 01  GWS-SPEC-BK-ADD2                    PIC X(30) VALUE SPACES.  
005384 01  GWS-HOLD-NAME                       PIC X(30) VALUE SPACES.  
005386 01  WS-REDEFINE-AREA-2.                                          
005388     02  GWS-RPT-NO-PRT-LINE              PIC X(132).             
005390     02  GWS-RPT-LINE    REDEFINES GWS-RPT-NO-PRT-LINE.           
005392     05  GWS-RPT-BR-BK.                                           
005394         10  FILLER                  PIC X(03).                   
005396         10  GWS-RPT-BR              PIC X(02).                   
005398         10  FILLER                  PIC X(04).                   
005400         10  GWS-RPT-BK              PIC X(03).                   
005402     05  FILLER                      PIC X(02).                   
005404     05  GWS-RPT-NO-LINE OCCURS 8 TIMES.                          
005406         10  GWS-RPT-PRT-REM         PIC X(07).                   
005408         10  GWS-RPT-PRT-NO          PIC Z(06).                   
005410         10  FILLER                  PIC X(01).                   
005412     05  FILLER                      PIC X(06).                   
005414                                                                  
005416     02  GWS-RPT-TABLE                    PIC X(312).             
005418     02  GWS-RPT-TABLE-R REDEFINES GWS-RPT-TABLE.                 
005420     05  GWS-RPT-NO-CNT              OCCURS 24 TIMES.             
005422         10  GWS-RPT-NO              PIC X(07).                   
005424         10  GWS-RPT-LINES           PIC 9(06).                   
005426     02  H-TIME                          PIC X(05).               
005428     02  PRT-OPEN-TIME                   PIC 9(08) COMP.          
005430     02  PRT-OPEN-TIME-R REDEFINES PRT-OPEN-TIME.                 
005432     05  PRT-OPEN-HHMM               PIC 9(04) COMP.              
005434     05  FILLER                      PIC 9(04) COMP.              
005436     02  PRT-OPEN-DATE                   PIC 9(06) COMP.          
005438     02  PRT-OPEN-DATE-R REDEFINES PRT-OPEN-DATE.                 
005440     05  PRT-OPEN-MM                 PIC 9(02) COMP.              
005442     05  PRT-OPEN-DD                 PIC 9(02) COMP.              
005444     05  PRT-OPEN-YY                 PIC 9(02) COMP.              
005446     02  TEAR-PAGE-IN.                                            
005448     05  TP-LN1.                                                  
005450         10  TP-LN-BANK              PIC X(04) VALUE "BK".        
005452         10  TP-LN-BKNO              PIC X(04) VALUE SPACES.      
005454     05  TP-LN2                      PIC X(08) VALUE SPACES.      
005456     05  TP-LN-DATE REDEFINES TP-LN2 PIC 99/99/99.                
005458     05  TP-LN3                      PIC X(08) VALUE SPACES.      
005460     02  TEAR-PG-IN REDEFINES TEAR-PAGE-IN.                       
005462     05  TP-IN-CHAR                  PIC X(01) OCCURS 24 TIMES.   
005464     02  TP-CHAR-ARRAY.                                           
005466    03 FILLER PIC X(33) VALUE "A0102010202B0302010203C0104040401".
005468    03 FILLER PIC X(33) VALUE "D0302020203E0104030401F0104030404".
005470    03 FILLER PIC X(33) VALUE "G0104050601H0202010202I0708080807".
005472    03 FILLER PIC X(33) VALUE "J0909090201K0210111002L0404040401".
005474    03 FILLER PIC X(33) VALUE "M0112121313N0614120515O0102020201".
005476    03 FILLER PIC X(33) VALUE "P0102010404Q0113131501R0106011002".
005478    03 FILLER PIC X(33) VALUE "S0104010901T0108080808U0202020101".
005480    03 FILLER PIC X(33) VALUE "V1313020708W1313121201X0207080702".
005482    03 FILLER PIC X(33) VALUE "Y0202010808Z011608170100702020207".
005484    03 FILLER PIC X(33) VALUE "118080808072010901040130109010901".
005486    03 FILLER PIC X(33) VALUE "410100116165010401090160404010201".
005488    03 FILLER PIC X(33) VALUE "701090909098010201020190102020709".
005490    03 FILLER PIC X(33) VALUE ",0827303030/0916081704+0808010808".
005492    03 FILLER PIC X(33) VALUE "!0808083008#2223222322$0120012101".
005494    03 FILLER PIC X(33) VALUE "%2425262724*2818031828-3030073030".
005496    03 FILLER PIC X(33) VALUE "=3007300730:3008300830;3008300825".
005498    03 FILLER PIC X(33) VALUE "?0329192626,3030301726.3030301717".
005500    03 FILLER PIC X(11) VALUE " 3030303030".                      
005502     02  TP-DECODE-CHAR REDEFINES TP-CHAR-ARRAY.                  
005504     05  TP-DECODE                   PIC X(11) OCCURS 52 TIMES.   
005506     02  TP-FORM-CHAR.                                            
005508 05 FILLER PIC X(36) VALUE "****************    **************  ".
005510 05 FILLER PIC X(36) VALUE "****        ****  **********      **".
005512 05 FILLER PIC X(36) VALUE "  ********      ****            ****".
005514 05 FILLER PIC X(36) VALUE "****  ****  ********    **  ****  **".
005516 05 FILLER PIC X(36) VALUE "**        ********    ****      ****".
005518 05 FILLER PIC X(36) VALUE "      ****    ****        ******    ".
005520 05 FILLER PIC X(36) VALUE "    ******  **  ****        ****  **".
005522 05 FILLER PIC X(36) VALUE "    **  **    ************      **  ".
005524 05 FILLER PIC X(36) VALUE "      **        **        **        ".
005526 05 FILLER PIC X(36) VALUE "**  **  **          **              ".
005528     02  TP-FORMCHAR REDEFINES TP-FORM-CHAR.                      
005530     05  TPFORMCHAR                  PIC X(12) OCCURS 30 TIMES.   
005532                                                                  
005534 01  GWS-PRT-EXCEPT-LINE.                                         
005536     05  GWS-PRT-EXC-BLOCK-CTL       PIC 9(02).                   
005538     05  GWS-PRT-EXC-PAGE-CTL        PIC 9(01).                   
005540     05  GWS-PRT-EXC-NO-LINES        PIC 9(02).                   
005542     05  GWS-PRT-EXC-DATA-160.                                    
005544         10  GWS-PRT-EXC-DATA        PIC X(132).                  
005546         10  FILLER                  PIC X(028).                  
```

⚠️  This is the source code you must document.
    399 lines from 2371 to 2769.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

