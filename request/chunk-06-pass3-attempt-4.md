# LLM Request Debug File
Generated: 2025-11-18T16:37:19.729543

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 6/55
- **Model**: gpt-4.1
- **Chunk Number**: 6
- **Pass Number**: 3
- **Attempt Number**: 4 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,085 tokens
- **User Prompt**: ~9,330 tokens
- **Total Input**: ~11,415 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 6/55" (ID: detailed-code-explanation)

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


**CHUNK 6 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T16:24:14.514603", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 6 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 1970 to 2370 (401 lines)\nChunk Tokens (estimated): ~7,953\nActual Input Tokens: 9,359 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 1970-2370 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 6 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 6 of 55.\n\n\n=============================================================================\nCHUNK 6 SOURCE CODE (Lines 1970-2370)\n=============================================================================\n\n```cobol\n003948 01 WS-COMMON-VAR.                                                \n003950    05 WS-PRESENT                       PIC 9(01) VALUE 0.        \n003952    05 WS-TRAIL-204-CNT                 PIC 9(06) VALUE 0.        \n003954    05 WS-TRAIL-208-CNT                 PIC 9(06) VALUE 0.        \n003956    05 WS-TRAIL-212-CNT                 PIC 9(06) VALUE 0.        \n003958    05 WS-TRAIL-218-CNT                 PIC 9(06) VALUE 0.        \n003960    05 WS-TRAIL-220-CNT                 PIC 9(06) VALUE 0.        \n003962    05 WS-TRAIL-222-CNT                 PIC 9(06) VALUE 0.        \n003964    05 WS-TRAIL-240-CNT                 PIC 9(06) VALUE 0.        \n003966    05 WS-TRAIL-242-CNT                 PIC 9(06) VALUE 0.        \n003968    05 WS-TRAIL-244-CNT                 PIC 9(06) VALUE 0.        \n003970    05 WS-TRAIL-246-CNT                 PIC 9(06) VALUE 0.        \n003972    05 WS-TRAIL-247-CNT                 PIC 9(06) VALUE 0.        \n003974    05 WS-TRAIL-224-CNT                 PIC 9(06) VALUE 0.        \n003976    05 WS-TRAIL-248-CNT                 PIC 9(06) VALUE ZERO.     \n003978    05 WS-TRAIL-226-CNT                 PIC 9(06) VALUE ZERO.     \n003980    05 WS-TRAIL-228-CNT                 PIC 9(06) VALUE ZERO.     \n003982    05 WS-TRAIL-230-CNT                 PIC 9(06) VALUE ZERO.     \n003984    05 WS-TRAIL-250-CNT                 PIC 9(06) VALUE ZERO.     \n003986    05 WS-TRAIL-232-CNT                 PIC 9(06) VALUE ZERO.     \n003988    05 WS-TRAIL-252-CNT                 PIC 9(06) VALUE ZERO.     \n003990    05 WS-TRAIL-234-CNT                 PIC 9(06) VALUE ZERO.     \n003992    05 WS-LASER-TYPE                    PIC X(03) VALUE SPACES.   \n003994    05 WS-LASER-CITY                    PIC X(15) VALUE SPACES.   \n003996    05 WS-COUNT                         PIC 9(07) VALUE 0.        \n003998    05 WS-FORM-TYPE-X.                                            \n004000       10 WS-FORM-TYPE                  PIC 9(03) VALUE 0.        \n004002    05 WS-READ-FIRST                    PIC 9(01) VALUE 0.        \n004004    05 WS-END-DATE                      PIC 9(08) VALUE 0.        \n004006    05 WS-BEGIN-DATE                    PIC 9(08) VALUE 0.        \n004008    05 SHELL-PCR-END-DATE               PIC 9(08) VALUE 0.        \n004010    05 SHELL-PCR-BEGIN-DATE             PIC 9(08) VALUE 0.        \n004012    05 WS-BANK-NBR                      PIC 9(04) VALUE 0.        \n004014    05 WS-WORK-DATE                     PIC 9(08) VALUE 0.        \n004016    05 WS-DT-LST-POSTED-CCYYMMDD        PIC 9(08) VALUE 0.        \n004018    05 WS-NEW-RPT                       PIC 9(01) VALUE 1.        \n004020    05 WS-EOJ                           PIC 9(01) VALUE 0.        \n004022    05 WS-SUB                           PIC 9(02) VALUE 0.        \n004024    05 WS-SUB2                          PIC 9(02) VALUE 0.        \n004026    05 WS-FIRST-ACCT                    PIC 9(01) VALUE 0.        \n004028    05 WS-PROCESS-DATE                  PIC 9(08) VALUE 0.        \n004030    05 WS-TP-DLY-WKLY                   PIC X(08) VALUE \"TDA DLY\".\n004032    05 WS-SAVE-ACCT                     PIC 9(12) VALUE 0.        \n004034    05 WS-FICHE-RMT-PASS                PIC 9(01) VALUE 0.        \n004036       88 FICHE-RMT-PASS                VALUE 1.                  \n004038    05 WS-HEADER-PRINT                  PIC 9(01) VALUE 0.        \n004040       88 NEW-HEADER                    VALUE 0.                  \n004042       88 SAME-HEADER                   VALUE 1.                  \n004044    05 TABLE-POSITIONS.                                           \n004046       10 WS-TAB-POS                    PIC 9(03) VALUE 0.        \n004048       10 WS-POS                        PIC 9(04) VALUE 0.        \n004050       10 WS-POS2                       PIC 9(03) VALUE 0.        \n004052       10 WS-POS3                       PIC 9(03) VALUE 0.        \n004054    05 WS-TERM.                                                   \n004056       10 WS-MAT-TERM                   PIC X(04) VALUE SPACES.   \n004058       10 WS-MAT-TYPE                   PIC X(01) VALUE SPACES.   \n004060    05 WS-TOTALS.                                                 \n004062       10 WS-INTEREST                   PIC 9(11)V999 VALUE 0.    \n004064       10 WS-AVERAGE                    PIC 9(02)V999 VALUE 0.    \n004066       10 WS-AVG-RT                     PIC 9(02)V999 VALUE 0.    \n004068       10 WS-INT-TOT                    PIC 9(11)V99  VALUE 0.    \n004070       10 WS-TOTAL-PRCNT                PIC 9(03)V99  VALUE 0.    \n004072       10 WS-TOTAL-INT                  PIC 9(11)V99  VALUE 0.    \n004074       10 WS-TOTAL-NO                   PIC 9(06)     VALUE 0.    \n004076       10 WS-TOTAL-BAL                  PIC 9(11)V99  VALUE 0.    \n004078       10 WS-TOTAL-AMT                  PIC 9(12)     VALUE 0.    \n004080       10 WS-TOTAL-NET                  PIC 9(12)     VALUE 0.    \n004082       10 WS-TOTAL-TAX                  PIC 9(12)     VALUE 0.    \n004084       10 WS-TOTAL-TAX-V2 REDEFINES WS-TOTAL-TAX                  \n004086                                        PIC 9(10)V99.             \n004088       10 WS-TOTAL-ST-TAX               PIC 9(8)V99   VALUE 0.    \n004090       10 WS-TOTAL-TAX-YTD              PIC 9(12)     VALUE 0.    \n004092       10 WS-TOTAL-ST-TAX-YTD           PIC 9(8)V99   VALUE 0.    \n004094                                                                  \n004096    05 WS-LSR-PHN-NO                    PIC B999B999B9999.        \n004098    05 WS-LSR-PHN-NO-R REDEFINES WS-LSR-PHN-NO.                   \n004100       10 WS-LSR-PHONE-LB               PIC X(01).                \n004102       10 FILLER                        PIC 9(03).                \n004104       10 WS-LSR-PHONE-RB               PIC X(01).                \n004106       10 FILLER                        PIC 9(03).                \n004108       10 WS-LSR-PHONE-DASH             PIC X(01).                \n004110       10 FILLER                        PIC 9(04).                \n004112    05 WS-PAGE-CNT                      PIC 9(04).                \n004114    05 WS-PAGE-CNT-160                  PIC 9(04).                \n004116    05 WS-PAGE-CNT-TRIAL                PIC 9(04).                \n004118                                                                  \n004120 01 WS-EMAIL-NTC-FIELDS.                                          \n004122    05 WS-EML-T-NO-RECORDS              PIC 9(08)  VALUE 0.       \n004124    05 WS-EML-T-NO-NOTICES              PIC 9(08)  VALUE 0.       \n004126    05 WS-GENERIC-NTC-PRT               PIC 9(01)  VALUE 0.       \n004128    05 WS-EML-NTC-TYPE                  PIC 9(01)  VALUE 0.       \n004130       88 EML-NTC-G-LSR                   VALUE 1.                \n004132       88 EML-NTC-PREM                    VALUE 2.                \n004134       88 EML-NTC-PP-PLUS                 VALUE 4.                \n004136    05 WS-EML-NTC-BILL-CNT              PIC 9(04)  VALUE 0.       \n004138                                                                  \n004140 01 PRT-LIST-FILE-STATUS               PIC 9(01) VALUE 0.         \n004142    88 PRT-LIST-CLOSE                     VALUE 0.                \n004144    88 PRT-LIST-OPEN                      VALUE 1.                \n004146 01 PRT-LIST160-FILE-STATUS            PIC 9(01) VALUE 0.         \n004148    88 PRT-LIST160-CLOSE                  VALUE 0.                \n004150    88 PRT-LIST160-OPEN                   VALUE 1.                \n004152 01 PRT-LIST607-FILE-STATUS            PIC 9(01) VALUE 0.         \n004154    88 PRT-LIST607-CLOSE                  VALUE 0.                \n004156    88 PRT-LIST607-OPEN                   VALUE 1.                \n004158 01 PRT-CHECK-FILE-STATUS              PIC 9(01) VALUE 0.         \n004160    88 PRT-CHECK-CLOSE                    VALUE 0.                \n004162    88 PRT-CHECK-OPEN                     VALUE 1.                \n004164 01 PRT-LSR-CHK-FILE-STATUS            PIC 9(01) VALUE 0.         \n004166    88 PRT-LSR-CHK-CLOSE                  VALUE 0.                \n004168    88 PRT-LSR-CHK-OPEN                   VALUE 1.                \n004170 01 PRT-LSR-BANK-FILE-STATUS           PIC 9(01) VALUE 0.         \n004172    88 PRT-LSR-BANK-CLOSE                  VALUE 0.               \n004174    88 PRT-LSR-BANK-OPEN                   VALUE 1.               \n004176 01 PRT-G-LSR-BANK-FILE-STATUS         PIC 9(01) VALUE 0.         \n004178    88 PRT-G-LSR-BANK-CLOSE                VALUE 0.               \n004180    88 PRT-G-LSR-BANK-OPEN                 VALUE 1.               \n004182 01 PRT-LSR-BANK-STMT-FILE-STATUS      PIC 9(01) VALUE 0.         \n004184    88 PRT-LSR-BANK-STMT-CLOSE             VALUE 0.               \n004186    88 PRT-LSR-BANK-STMT-OPEN              VALUE 1.               \n004188 01 PRT-FICHE-FILE-STATUS              PIC 9(01) VALUE 0.         \n004190    88 PRT-FICHE-CLOSE                    VALUE 0.                \n004192    88 PRT-FICHE-OPEN                     VALUE 1.                \n004194 01 PRT-DSI-FILE-STATUS                PIC 9(01) VALUE 0.         \n004196    88 PRT-DSI-CLOSE                      VALUE 0.                \n004198    88 PRT-DSI-OPEN                       VALUE 1.                \n004200 01 PRT-LASER-FILE-STATUS              PIC 9(01) VALUE 0.         \n004202    88 PRT-LASER-CLOSE                    VALUE 0.                \n004204    88 PRT-LASER-OPEN                     VALUE 1.                \n004206 01 PRT-STATEMENT-FILE-STATUS          PIC 9(01) VALUE 0.         \n004208    88 PRT-STATEMENT-CLOSE                VALUE 0.                \n004210    88 PRT-STATEMENT-OPEN                 VALUE 1.                \n004212 01 PRT-TRIAL-FILE-STATUS              PIC 9(01) VALUE 0.         \n004214    88 PRT-TRIAL-CLOSE                    VALUE 0.                \n004216    88 PRT-TRIAL-OPEN                     VALUE 1.                \n004218 01 PRT-NOTICE-FILE-STATUS             PIC 9(01) VALUE 0.         \n004220    88 PRT-NOTICE-CLOSE                   VALUE 0.                \n004222    88 PRT-NOTICE-OPEN                    VALUE 1.                \n004224 01 PRT-CARD-FILE-STATUS               PIC 9(01) VALUE 0.         \n004226    88 PRT-CARD-CLOSE                     VALUE 0.                \n004228    88 PRT-CARD-OPEN                      VALUE 1.                \n004230 01 EMAIL-NTC-FILE-STATUS              PIC 9(01) VALUE 0.         \n004232    88 EMAIL-NTC-CLOSE                    VALUE 0.                \n004234    88 EMAIL-NTC-OPEN                     VALUE 1.                \n004236 01 BILLING-FILE-STATUS                PIC 9(01) VALUE 0.         \n004238    88 BILLING-CLOSE                      VALUE 0.                \n004240    88 BILLING-OPEN                       VALUE 1.                \n004242                                                                  \n004244 01  WS-NAME-REVERSION.                                           \n004246     05  WS-NAME-REV                 PIC X(30).                   \n004248     05  WS-NR-WKA1.                                              \n004250         10  WS-NR-WK1               PIC X(01) OCCURS 30 TIMES.   \n004252     05  WS-NR-WKA2.                                              \n004254         10  WS-NR-WK2               PIC X(01) OCCURS 30 TIMES.   \n004256     05  WS-NR-CTR1                  PIC 9(02).                   \n004258     05  WS-NR-CTR2                  PIC 9(02).                   \n004260     05  WS-NR-CTR3                  PIC 9(02).                   \n004262     05  WS-NR-CTR4                  PIC 9(02).                   \n004264 01  WS-EXTRA-NAME-REVERSION.                                     \n004266     05  WS-NR-WKA3.                                              \n004268         10  WS-NR-WK3               PIC X(01) OCCURS 30 TIMES.   \n004270 01  WS-STORE-NR-END                     PIC X(30) VALUE SPACES.  \n004272 01  WS-STORE-COUNT                      PIC 9(03) VALUE 0.       \n004274 01  WS-STORE-NR-CTR                     PIC 9(02) VALUE 0.       \n004276 01  WS-PARTIAL-NAME                     PIC X(30) VALUE SPACES.  \n004278 01  WS-STORE-NAME                       PIC X(30) VALUE SPACES.  \n004280 01  WS-NR-FLAG                          PIC 9(01) VALUE 0.       \n004282 01  WS-POST-TALLY                       PIC 9(03) VALUE 0.       \n004284 01  WS-POST-COUNT                       PIC 9(03) VALUE 0.       \n004286 01  WS-RPTSHELL-RESTART                 PIC 9(01) VALUE 0.       \n004288 01  WS-RESTART-ACCEPT                   PIC X(01) VALUE SPACE.   \n004290 01  WS-RPTSHELL-STMT-TODAY              PIC 9(01) VALUE 0.       \n004292 01  WS-RPTSHELL-STMT-REPLY              PIC X(01) VALUE SPACE.   \n004294 01  WS-CONTINUE                         PIC X(01) VALUE SPACE.   \n004296 01  WS-PPP-NTC-FLAG                     PIC 9(01) VALUE 0.       \n004298 01  WS-PREM-NTC-FLAG                    PIC 9(01) VALUE 0.       \n004300                                                                  \n004302 01  EML-NTC-RECORD                 PIC X(270).                   \n004304 01  EML-HEADER-REC.                                              \n004306     05  EML-H-REC-TYPE             PIC 9(02).                    \n004308     05  EML-H-BANK                 PIC 9(04).                    \n004310     05  EML-H-APPL                 PIC X(03).                    \n004312     05  EML-H-FILE-DATE            PIC 9(08).                    \n004314     05  EML-H-FILE-DATE-R     REDEFINES     EML-H-FILE-DATE.     \n004316         07  EML-H-FILE-DT-CC       PIC 9(02).                    \n004318         07  EML-H-FILE-DT-YY       PIC 9(02).                    \n004320         07  EML-H-FILE-DT-MM       PIC 9(02).                    \n004322         07  EML-H-FILE-DT-DD       PIC 9(02).                    \n004324     05  EML-H-RERUN-IND            PIC 9(01).                    \n004326     05  EML-H-BANK-NAME            PIC X(25).                    \n004328     05  FILLER                     PIC X(227).                   \n004330 01  EML-ACCT-HEADER-REC.                                         \n004332     05  EML-AH-REC-TYPE            PIC 9(02).                    \n004334     05  EML-AH-BANK                PIC 9(04).                    \n004336     05  EML-AH-APPL                PIC X(03).                    \n004338     05  EML-AH-ACCTNO              PIC 9(12).                    \n004340     05  EML-AH-SUBNO               PIC 9(10).                    \n004342     05  EML-AH-PREMIER-FLAG        PIC 9(01).                    \n004344     05  EML-AH-NTC-FORM-TYPE       PIC X(03).                    \n004346     05  EML-AH-NTC-TITLE           PIC X(40).                    \n004348     05  EML-AH-CUST-NAME           PIC X(25).                    \n004350     05  EML-AH-EMAIL-ADD           PIC X(120).                   \n004352     05  EML-AH-DIGITAL-FLAG        PIC X(01).                    \n004354     05  FILLER                     PIC X(49).                    \n004356 01  EML-ACCT-DETAIL-REC.                                         \n004358     05  EML-AD-REC-TYPE            PIC 9(02).                    \n004360     05  EML-AD-BANK                PIC 9(04).                    \n004362     05  EML-AD-APPL                PIC X(03).                    \n004364     05  EML-AD-ACCTNO              PIC 9(12).                    \n004366     05  EML-AD-SUBNO               PIC 9(10).                    \n004368     05  EML-AD-REC-NO              PIC 9(04).                    \n004370     05  EML-AD-REC-AREA            PIC X(140).                   \n004372     05  FILLER                     PIC X(95).                    \n004374 01  EML-ACCT-TRAILER-REC.                                        \n004376     05  EML-AT-REC-TYPE            PIC 9(02).                    \n004378     05  EML-AT-BANK                PIC 9(04).                    \n004380     05  EML-AT-APPL                PIC X(03).                    \n004382     05  EML-AT-ACCTNO              PIC 9(12).                    \n004384     05  EML-AT-SUBNO               PIC 9(10).                    \n004386     05  FILLER                     PIC X(239).                   \n004388 01  EML-TRAILER-REC.                                             \n004390     05  EML-T-REC-TYPE             PIC 9(02).                    \n004392     05  EML-T-BANK                 PIC 9(04).                    \n004394     05  EML-T-APPL                 PIC X(03).                    \n004396     05  EML-T-NO-RECORDS           PIC 9(08).                    \n004398     05  EML-T-NO-NOTICES           PIC 9(08).                    \n004400     05  FILLER                     PIC X(245).                   \n004402                                                                  \n004404 01  WS-MSG-TBL-MAX             PIC 99   VALUE 20.                \n004406 01  WS-MSG-TABLE.                                                \n004408     05  WS-MSG-TOT-CODE        PIC 9(4) OCCURS 20 TIMES.         \n004410 01  WS-MSG-TEST                PIC 9    VALUE 0.                 \n004412                                                                  \n004414 01  LSR-MESSAGE-FIELDS.                                          \n004416     05  LSR-MESSAGE-1               PIC X(100) VALUE SPACES.     \n004418     05  LSR-MESSAGE-2               PIC X(100) VALUE SPACES.     \n004420                                                                  \n004422 01  WS-BRCH-ADDR-FLAG               PIC 9    VALUE 0.            \n004424     88  BRCH-ADDR-FOUND             VALUE 1.                     \n004426                                                                  \n004428 01  FM-DOWNLOAD-RECORD              PIC X(540).                  \n004430 01  FM-DOWNLOAD-REC-CNT-X.                                       \n004432     05  FILLER                      PIC X(34)                    \n004434         VALUE \"0000000000000000000000000000000000\".              \n004436     05  FM-DOWNLOAD-REC-CNT         PIC 9(06)  VALUE 0.          \n004438 01  FM-DOWNLOAD-BANK-X.                                          \n004440     05  FM-DOWNLOAD-BANK            PIC 9(04)  VALUE 0.          \n004442                                                                  \n004444 01  SXLK-HDR-KEY.                                                \n004446     05  SXLK-HDR-BANK               PIC 9(04)  VALUE ZEROS.      \n004448     05  SXLK-HDR-APP                PIC X(03)  VALUE \"HDR\".      \n004450     05  SXLK-HDR-DATE               PIC 9(06)  VALUE ZEROS.      \n004452     05  FILLER                      PIC X(34)  VALUE SPACES.     \n004454                                                                  \n004456 01  CFDF-HDR-KEY.                                                \n004458     05  CFDF-HDR-BANK               PIC 9(04) VALUE ZEROS.       \n004460     05  CFDF-HDR-APP                PIC X(03) VALUE \"HDR\".       \n004462     05  CFDF-HDR-DATE               PIC 9(06) VALUE ZEROS.       \n004464     05  CFDF-HDR-L4                 PIC X(04) VALUE SPACES.      \n004466                                                                  \n004468                                                                  \n004470                                                                  \n004472 01  TDA-ACTIVITY-RECORD             PIC X(225).                  \n004474 01  TDA-ACTIVITY-REC.                                            \n004476     05  TDV-BANK-NO                 PIC 9(04).                   \n004478     05  TDV-BANK-NO-R REDEFINES TDV-BANK-NO.                     \n004480         10  FILLER                  PIC 9(01).                   \n004482         10  TDV-BANK-NO3            PIC 9(03).                   \n004484     05  TDV-CUST-NO                 PIC 9(12).                   \n004486     05  TDV-ACCT-NO                 PIC 9(10).                   \n004488     05  TDV-DATE-TRX                PIC 9(08).                   \n004490     05  TDV-DATE-TRX-R REDEFINES TDV-DATE-TRX.                   \n004492         10  TDV-TRXDT-CCYY          PIC 9(04).                   \n004494         10  TDV-TRXDT-MMDD          PIC 9(04).                   \n004496     05  TDV-DATE-EFF                PIC 9(08).                   \n004498     05  TDV-DATE-EFF-R REDEFINES TDV-DATE-EFF.                   \n004500         10  TDV-EFFDT-CCYY          PIC 9(04).                   \n004502         10  TDV-EFFDT-MMDD          PIC 9(04).                   \n004504     05  TDV-TRANCODE                PIC 9(04).                   \n004506     05  TDV-DR-CR                   PIC X(01).                   \n004508     05  TDV-ERR-FLAG                PIC X(02).                   \n004510     05  TDV-AMOUNT                  PIC 9(12)V99.                \n004512     05  TDV-ACH-CST                 PIC X(02).                   \n004514     05  TDV-DESC                    PIC X(80).                   \n004516     05  TDV-ACH-DESC REDEFINES TDV-DESC.                         \n004518         10  TDV-ACH-CO-NAME.                                     \n004520             15  TDV-ACH-TRANSFER    PIC X(10).                   \n004522             15  FILLER              PIC X(06).                   \n004524         10  TDV-ACH-CO-DESC         PIC X(10).                   \n004526         10  FILLER                  PIC X(54).                   \n004528     05  TDV-SEQUENCE                PIC 9(16).                   \n004530     05  TDV-SEQUENCE-R REDEFINES TDV-SEQUENCE.                   \n004532         10  TDV-SEQ-ID              PIC X(01).                   \n004534         10  TDV-SEQ-NO              PIC X(15).                   \n004536     05  TDV-SERIAL-NO               PIC 9(10).                   \n004538     05  TDV-SOURCE-CODE             PIC X(01).                   \n004540     05  TDV-ITEM-TIEBRK.                                         \n004542         10  TDV-ITEM-TIEBRK-9       PIC 9(20).                   \n004544     05  TDV-FORMAT-CODE             PIC X(01).                   \n004546     05  TDV-EMP-ACT-NBR             PIC 9(03).                   \n004548     05  TDV-EMP-ACT-AMT             PIC S9(09)V99.               \n004550     05  FILLER                      PIC X(18).                   \n004552 01  TDA-BATCH-RECORD.                                            \n004554     05  FILLER                      PIC X(26).                   \n004556     05  TDV-MNT-STRUCT              PIC 9(02).                   \n004558     05  TDV-MNT-TRANCODE            PIC 9(04).                   \n004560     05  TDV-MNT-CHGDATA             PIC X(30).                   \n004562     05  TDV-MNT-APPLY               PIC X(01).                   \n004564     05  TDV-MNT-ORIGIN              PIC X(08).                   \n004566     05  FILLER                      PIC X(01).                   \n004568     05  TDV-MNT-SYSUSE              PIC X(01).                   \n004570     05  FILLER                      PIC X(01).                   \n004572     05  TDV-DDA-FROM-ACCT           PIC 9(12).                   \n004574     05  TDV-DDA-FROM-SUB-IND        PIC 9(03).                   \n004576     05  FILLER                      PIC X(136).                  \n004578*                                                                 \n004580 01  TDA-NINES-ACTIVITY.                                          \n004582     05  TDT-BANK-NO                 PIC 9(04).                   \n004584     05  TDT-CUST-NO                 PIC 9(12).                   \n004586     05  TDT-ACCT-NO                 PIC 9(10).                   \n004588     05  TDT-DR-COUNT                PIC 9(06).                   \n004590     05  TDT-DR-AMOUNT               PIC 9(12)V99.                \n004592     05  TDT-CR-COUNT                PIC 9(06).                   \n004594     05  TDT-CR-AMOUNT               PIC 9(12)V99.                \n004596     05  TDT-APP-DESCRIPTION.                                     \n004598         10  TDT-APP                 PIC X(18).                   \n004600         10  TDT-FILE-DATE           PIC 9(06).                   \n004602     05  FILLER                      PIC X(135).                  \n004604*                                                                 \n004606                                                                  \n004608                                                                  \n004610 01  TDA-TDA-FILE-ID.                                             \n004612     05  TDA-TDA-APPL                PIC XXX.                     \n004614     05  TDA-TDA-FCTL-IND            PIC XXX VALUE \"XA2\".         \n004616     05  TDA-TDA-ID-DATE.                                         \n004618         10  TDA-TDA-ID-MM           PIC 99.                      \n004620         10  TDA-TDA-ID-DD           PIC 99.                      \n004622     05  FILLER                      PIC X(05) VALUE \"/TDA0\".     \n004624     05  TDA-TDA-ID-SUFF             PIC X.                       \n004626     05  TDA-TDA-ID-DC               PIC 99.                      \n004628     05  TDA-TDA-ID-BANK             PIC 999.                     \n004630     05  FILLER                      PIC X(01) VALUE \".\".         \n004632                                                                  \n004634 01  TDA-TDA-FILE-STATUS             PIC 9(01) VALUE 0.           \n004636 01  TDA-TDA-FILE-RECS               PIC 9(12) VALUE 0.           \n004638 01  TDA-OUTPUT-FILE-ID.                                          \n004640     05  FILLER                         PIC X(06).                \n004642     05  TDA-OUTPUT-FILE-DATE           PIC 9(04).                \n004644     05  FILLER                         PIC X(06).                \n004646     05  TDA-OUTPUT-FILE-DC             PIC 9(02).                \n004648     05  TDA-OUTPUT-FILE-BANK           PIC 9(03).                \n004650     05  TDA-OUTPUT-FILE-PERIOD         PIC X(01).                \n004652 01  WS-FCTL-RERUN-CODE              PIC X(01).                   \n004654 01  WS-FCTL-APP                     PIC X(03) VALUE SPACES.      \n004656 01  WS-FCTL-ATTRIB-CNT              PIC 9(12) VALUE 0.           \n004658 01  WS-FCTL-PILOT                   PIC 9(01) VALUE 0.           \n004660 01  WS-FCTL-USERCODE.                                            \n004662     05  WS-FCTL-USER                PIC X(03) VALUE SPACES.      \n004664     05  FILLER                      PIC X(14) VALUE SPACES.      \n004666                                                                  \n004668 01  FCTL-RECORD.                                                 \n004670    05  FCTL-PROCESS-DATE             PIC 9(08).                  \n004672    05  FCTL-PROCESS-DATE-R REDEFINES FCTL-PROCESS-DATE.          \n004674        10  FCTL-PROC-CC              PIC 9(02).                  \n004676        10  FCTL-PROC-YY              PIC 9(02).                  \n004678        10  FCTL-PROC-MMDD            PIC 9(04).                  \n004680    05  FCTL-DATE-CREATE              PIC 9(08).                  \n004682    05  FCTL-DATE-CREATE-X REDEFINES FCTL-DATE-CREATE.            \n004684        10  FCTL-CREATE-CC            PIC 9(02).                  \n004686        10  FCTL-CREATE-YY            PIC 9(02).                  \n004688        10  FCTL-CREATE-MMDD          PIC 9(04).                  \n004690    05  FCTL-TIME-CREATE              PIC 9(06).                  \n004692    05  FCTL-HASH-TOTAL               PIC 9(10)V99.               \n004694    05  FCTL-HASH-TOTAL9 REDEFINES FCTL-HASH-TOTAL                \n004696                                      PIC 9(12).                  \n004698    05  FCTL-BANK-NO                  PIC 9(03).                  \n004700    05  FCTL-FILE-CODE-X.                                         \n004702        10  FCTL-FILE-CODE            PIC 9(10).                  \n004704    05  FCTL-APPL                     PIC X(03).                  \n004706    05  FCTL-FILE-NAME.                                           \n004708        10  FCTL-FILE-NAME21          PIC X(21).                  \n004710        10  FILLER                    PIC X(11).                  \n004712    05  FCTL-PACK-NAME                PIC X(10).                  \n004714    05  FCTL-STATUS-IN                PIC X(01).                  \n004716    05  FCTL-STATUS-OUT               PIC X(01).                  \n004718    05  FCTL-ACTION                   PIC X(01).                  \n004720    05  FCTL-RESULT                   PIC X(72).                  \n004722    05  FCTL-SORT-DATE                PIC 9(08).                  \n004724    05  FCTL-BANK-NO-4                PIC 9(04).                  \n004726 01  FCTL-CALL-PROG                   PIC X(31)                   \n004728              VALUE \"CSI/FILECTL/LIB ON OBJ\".                     \n004730 01  FCTL-APPL-A17.                                               \n004732     05  FCTL-DDA-A17                 PIC 9(01) VALUE 0.          \n004734     05  FCTL-SAV-A17                 PIC 9(01) VALUE 0.          \n004736     05  FCTL-COD-A17                 PIC 9(01) VALUE 0.          \n004738     05  FCTL-IRA-A17                 PIC 9(01) VALUE 0.          \n004740     05  FCTL-CLN-A17                 PIC 9(01) VALUE 0.          \n004742     05  FCTL-ILN-A17                 PIC 9(01) VALUE 0.          \n004744     05  FCTL-ONL-A17                 PIC 9(01) VALUE 0.          \n004746     05  FCTL-MCR-A17                 PIC 9(01) VALUE 0.          \n004748     05  FCTL-GNL-A17                 PIC 9(01) VALUE 0.          \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    401 lines from 1970 to 2370.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 6, "total_chunks": 55, "start_line": 1970, "end_line": 2370, "line_count": 401}

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
- Source code length: 34221 characters

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
CHUNK 6 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 1970 to 2370 (401 lines)
Chunk Tokens (estimated): ~7,953
Actual Input Tokens: 9,359 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 1970-2370 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 6 of 55 chunks
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
      The source code below is only CHUNK 6 of 55.


=============================================================================
CHUNK 6 SOURCE CODE (Lines 1970-2370)
=============================================================================

```cobol
003948 01 WS-COMMON-VAR.                                                
003950    05 WS-PRESENT                       PIC 9(01) VALUE 0.        
003952    05 WS-TRAIL-204-CNT                 PIC 9(06) VALUE 0.        
003954    05 WS-TRAIL-208-CNT                 PIC 9(06) VALUE 0.        
003956    05 WS-TRAIL-212-CNT                 PIC 9(06) VALUE 0.        
003958    05 WS-TRAIL-218-CNT                 PIC 9(06) VALUE 0.        
003960    05 WS-TRAIL-220-CNT                 PIC 9(06) VALUE 0.        
003962    05 WS-TRAIL-222-CNT                 PIC 9(06) VALUE 0.        
003964    05 WS-TRAIL-240-CNT                 PIC 9(06) VALUE 0.        
003966    05 WS-TRAIL-242-CNT                 PIC 9(06) VALUE 0.        
003968    05 WS-TRAIL-244-CNT                 PIC 9(06) VALUE 0.        
003970    05 WS-TRAIL-246-CNT                 PIC 9(06) VALUE 0.        
003972    05 WS-TRAIL-247-CNT                 PIC 9(06) VALUE 0.        
003974    05 WS-TRAIL-224-CNT                 PIC 9(06) VALUE 0.        
003976    05 WS-TRAIL-248-CNT                 PIC 9(06) VALUE ZERO.     
003978    05 WS-TRAIL-226-CNT                 PIC 9(06) VALUE ZERO.     
003980    05 WS-TRAIL-228-CNT                 PIC 9(06) VALUE ZERO.     
003982    05 WS-TRAIL-230-CNT                 PIC 9(06) VALUE ZERO.     
003984    05 WS-TRAIL-250-CNT                 PIC 9(06) VALUE ZERO.     
003986    05 WS-TRAIL-232-CNT                 PIC 9(06) VALUE ZERO.     
003988    05 WS-TRAIL-252-CNT                 PIC 9(06) VALUE ZERO.     
003990    05 WS-TRAIL-234-CNT                 PIC 9(06) VALUE ZERO.     
003992    05 WS-LASER-TYPE                    PIC X(03) VALUE SPACES.   
003994    05 WS-LASER-CITY                    PIC X(15) VALUE SPACES.   
003996    05 WS-COUNT                         PIC 9(07) VALUE 0.        
003998    05 WS-FORM-TYPE-X.                                            
004000       10 WS-FORM-TYPE                  PIC 9(03) VALUE 0.        
004002    05 WS-READ-FIRST                    PIC 9(01) VALUE 0.        
004004    05 WS-END-DATE                      PIC 9(08) VALUE 0.        
004006    05 WS-BEGIN-DATE                    PIC 9(08) VALUE 0.        
004008    05 SHELL-PCR-END-DATE               PIC 9(08) VALUE 0.        
004010    05 SHELL-PCR-BEGIN-DATE             PIC 9(08) VALUE 0.        
004012    05 WS-BANK-NBR                      PIC 9(04) VALUE 0.        
004014    05 WS-WORK-DATE                     PIC 9(08) VALUE 0.        
004016    05 WS-DT-LST-POSTED-CCYYMMDD        PIC 9(08) VALUE 0.        
004018    05 WS-NEW-RPT                       PIC 9(01) VALUE 1.        
004020    05 WS-EOJ                           PIC 9(01) VALUE 0.        
004022    05 WS-SUB                           PIC 9(02) VALUE 0.        
004024    05 WS-SUB2                          PIC 9(02) VALUE 0.        
004026    05 WS-FIRST-ACCT                    PIC 9(01) VALUE 0.        
004028    05 WS-PROCESS-DATE                  PIC 9(08) VALUE 0.        
004030    05 WS-TP-DLY-WKLY                   PIC X(08) VALUE "TDA DLY".
004032    05 WS-SAVE-ACCT                     PIC 9(12) VALUE 0.        
004034    05 WS-FICHE-RMT-PASS                PIC 9(01) VALUE 0.        
004036       88 FICHE-RMT-PASS                VALUE 1.                  
004038    05 WS-HEADER-PRINT                  PIC 9(01) VALUE 0.        
004040       88 NEW-HEADER                    VALUE 0.                  
004042       88 SAME-HEADER                   VALUE 1.                  
004044    05 TABLE-POSITIONS.                                           
004046       10 WS-TAB-POS                    PIC 9(03) VALUE 0.        
004048       10 WS-POS                        PIC 9(04) VALUE 0.        
004050       10 WS-POS2                       PIC 9(03) VALUE 0.        
004052       10 WS-POS3                       PIC 9(03) VALUE 0.        
004054    05 WS-TERM.                                                   
004056       10 WS-MAT-TERM                   PIC X(04) VALUE SPACES.   
004058       10 WS-MAT-TYPE                   PIC X(01) VALUE SPACES.   
004060    05 WS-TOTALS.                                                 
004062       10 WS-INTEREST                   PIC 9(11)V999 VALUE 0.    
004064       10 WS-AVERAGE                    PIC 9(02)V999 VALUE 0.    
004066       10 WS-AVG-RT                     PIC 9(02)V999 VALUE 0.    
004068       10 WS-INT-TOT                    PIC 9(11)V99  VALUE 0.    
004070       10 WS-TOTAL-PRCNT                PIC 9(03)V99  VALUE 0.    
004072       10 WS-TOTAL-INT                  PIC 9(11)V99  VALUE 0.    
004074       10 WS-TOTAL-NO                   PIC 9(06)     VALUE 0.    
004076       10 WS-TOTAL-BAL                  PIC 9(11)V99  VALUE 0.    
004078       10 WS-TOTAL-AMT                  PIC 9(12)     VALUE 0.    
004080       10 WS-TOTAL-NET                  PIC 9(12)     VALUE 0.    
004082       10 WS-TOTAL-TAX                  PIC 9(12)     VALUE 0.    
004084       10 WS-TOTAL-TAX-V2 REDEFINES WS-TOTAL-TAX                  
004086                                        PIC 9(10)V99.             
004088       10 WS-TOTAL-ST-TAX               PIC 9(8)V99   VALUE 0.    
004090       10 WS-TOTAL-TAX-YTD              PIC 9(12)     VALUE 0.    
004092       10 WS-TOTAL-ST-TAX-YTD           PIC 9(8)V99   VALUE 0.    
004094                                                                  
004096    05 WS-LSR-PHN-NO                    PIC B999B999B9999.        
004098    05 WS-LSR-PHN-NO-R REDEFINES WS-LSR-PHN-NO.                   
004100       10 WS-LSR-PHONE-LB               PIC X(01).                
004102       10 FILLER                        PIC 9(03).                
004104       10 WS-LSR-PHONE-RB               PIC X(01).                
004106       10 FILLER                        PIC 9(03).                
004108       10 WS-LSR-PHONE-DASH             PIC X(01).                
004110       10 FILLER                        PIC 9(04).                
004112    05 WS-PAGE-CNT                      PIC 9(04).                
004114    05 WS-PAGE-CNT-160                  PIC 9(04).                
004116    05 WS-PAGE-CNT-TRIAL                PIC 9(04).                
004118                                                                  
004120 01 WS-EMAIL-NTC-FIELDS.                                          
004122    05 WS-EML-T-NO-RECORDS              PIC 9(08)  VALUE 0.       
004124    05 WS-EML-T-NO-NOTICES              PIC 9(08)  VALUE 0.       
004126    05 WS-GENERIC-NTC-PRT               PIC 9(01)  VALUE 0.       
004128    05 WS-EML-NTC-TYPE                  PIC 9(01)  VALUE 0.       
004130       88 EML-NTC-G-LSR                   VALUE 1.                
004132       88 EML-NTC-PREM                    VALUE 2.                
004134       88 EML-NTC-PP-PLUS                 VALUE 4.                
004136    05 WS-EML-NTC-BILL-CNT              PIC 9(04)  VALUE 0.       
004138                                                                  
004140 01 PRT-LIST-FILE-STATUS               PIC 9(01) VALUE 0.         
004142    88 PRT-LIST-CLOSE                     VALUE 0.                
004144    88 PRT-LIST-OPEN                      VALUE 1.                
004146 01 PRT-LIST160-FILE-STATUS            PIC 9(01) VALUE 0.         
004148    88 PRT-LIST160-CLOSE                  VALUE 0.                
004150    88 PRT-LIST160-OPEN                   VALUE 1.                
004152 01 PRT-LIST607-FILE-STATUS            PIC 9(01) VALUE 0.         
004154    88 PRT-LIST607-CLOSE                  VALUE 0.                
004156    88 PRT-LIST607-OPEN                   VALUE 1.                
004158 01 PRT-CHECK-FILE-STATUS              PIC 9(01) VALUE 0.         
004160    88 PRT-CHECK-CLOSE                    VALUE 0.                
004162    88 PRT-CHECK-OPEN                     VALUE 1.                
004164 01 PRT-LSR-CHK-FILE-STATUS            PIC 9(01) VALUE 0.         
004166    88 PRT-LSR-CHK-CLOSE                  VALUE 0.                
004168    88 PRT-LSR-CHK-OPEN                   VALUE 1.                
004170 01 PRT-LSR-BANK-FILE-STATUS           PIC 9(01) VALUE 0.         
004172    88 PRT-LSR-BANK-CLOSE                  VALUE 0.               
004174    88 PRT-LSR-BANK-OPEN                   VALUE 1.               
004176 01 PRT-G-LSR-BANK-FILE-STATUS         PIC 9(01) VALUE 0.         
004178    88 PRT-G-LSR-BANK-CLOSE                VALUE 0.               
004180    88 PRT-G-LSR-BANK-OPEN                 VALUE 1.               
004182 01 PRT-LSR-BANK-STMT-FILE-STATUS      PIC 9(01) VALUE 0.         
004184    88 PRT-LSR-BANK-STMT-CLOSE             VALUE 0.               
004186    88 PRT-LSR-BANK-STMT-OPEN              VALUE 1.               
004188 01 PRT-FICHE-FILE-STATUS              PIC 9(01) VALUE 0.         
004190    88 PRT-FICHE-CLOSE                    VALUE 0.                
004192    88 PRT-FICHE-OPEN                     VALUE 1.                
004194 01 PRT-DSI-FILE-STATUS                PIC 9(01) VALUE 0.         
004196    88 PRT-DSI-CLOSE                      VALUE 0.                
004198    88 PRT-DSI-OPEN                       VALUE 1.                
004200 01 PRT-LASER-FILE-STATUS              PIC 9(01) VALUE 0.         
004202    88 PRT-LASER-CLOSE                    VALUE 0.                
004204    88 PRT-LASER-OPEN                     VALUE 1.                
004206 01 PRT-STATEMENT-FILE-STATUS          PIC 9(01) VALUE 0.         
004208    88 PRT-STATEMENT-CLOSE                VALUE 0.                
004210    88 PRT-STATEMENT-OPEN                 VALUE 1.                
004212 01 PRT-TRIAL-FILE-STATUS              PIC 9(01) VALUE 0.         
004214    88 PRT-TRIAL-CLOSE                    VALUE 0.                
004216    88 PRT-TRIAL-OPEN                     VALUE 1.                
004218 01 PRT-NOTICE-FILE-STATUS             PIC 9(01) VALUE 0.         
004220    88 PRT-NOTICE-CLOSE                   VALUE 0.                
004222    88 PRT-NOTICE-OPEN                    VALUE 1.                
004224 01 PRT-CARD-FILE-STATUS               PIC 9(01) VALUE 0.         
004226    88 PRT-CARD-CLOSE                     VALUE 0.                
004228    88 PRT-CARD-OPEN                      VALUE 1.                
004230 01 EMAIL-NTC-FILE-STATUS              PIC 9(01) VALUE 0.         
004232    88 EMAIL-NTC-CLOSE                    VALUE 0.                
004234    88 EMAIL-NTC-OPEN                     VALUE 1.                
004236 01 BILLING-FILE-STATUS                PIC 9(01) VALUE 0.         
004238    88 BILLING-CLOSE                      VALUE 0.                
004240    88 BILLING-OPEN                       VALUE 1.                
004242                                                                  
004244 01  WS-NAME-REVERSION.                                           
004246     05  WS-NAME-REV                 PIC X(30).                   
004248     05  WS-NR-WKA1.                                              
004250         10  WS-NR-WK1               PIC X(01) OCCURS 30 TIMES.   
004252     05  WS-NR-WKA2.                                              
004254         10  WS-NR-WK2               PIC X(01) OCCURS 30 TIMES.   
004256     05  WS-NR-CTR1                  PIC 9(02).                   
004258     05  WS-NR-CTR2                  PIC 9(02).                   
004260     05  WS-NR-CTR3                  PIC 9(02).                   
004262     05  WS-NR-CTR4                  PIC 9(02).                   
004264 01  WS-EXTRA-NAME-REVERSION.                                     
004266     05  WS-NR-WKA3.                                              
004268         10  WS-NR-WK3               PIC X(01) OCCURS 30 TIMES.   
004270 01  WS-STORE-NR-END                     PIC X(30) VALUE SPACES.  
004272 01  WS-STORE-COUNT                      PIC 9(03) VALUE 0.       
004274 01  WS-STORE-NR-CTR                     PIC 9(02) VALUE 0.       
004276 01  WS-PARTIAL-NAME                     PIC X(30) VALUE SPACES.  
004278 01  WS-STORE-NAME                       PIC X(30) VALUE SPACES.  
004280 01  WS-NR-FLAG                          PIC 9(01) VALUE 0.       
004282 01  WS-POST-TALLY                       PIC 9(03) VALUE 0.       
004284 01  WS-POST-COUNT                       PIC 9(03) VALUE 0.       
004286 01  WS-RPTSHELL-RESTART                 PIC 9(01) VALUE 0.       
004288 01  WS-RESTART-ACCEPT                   PIC X(01) VALUE SPACE.   
004290 01  WS-RPTSHELL-STMT-TODAY              PIC 9(01) VALUE 0.       
004292 01  WS-RPTSHELL-STMT-REPLY              PIC X(01) VALUE SPACE.   
004294 01  WS-CONTINUE                         PIC X(01) VALUE SPACE.   
004296 01  WS-PPP-NTC-FLAG                     PIC 9(01) VALUE 0.       
004298 01  WS-PREM-NTC-FLAG                    PIC 9(01) VALUE 0.       
004300                                                                  
004302 01  EML-NTC-RECORD                 PIC X(270).                   
004304 01  EML-HEADER-REC.                                              
004306     05  EML-H-REC-TYPE             PIC 9(02).                    
004308     05  EML-H-BANK                 PIC 9(04).                    
004310     05  EML-H-APPL                 PIC X(03).                    
004312     05  EML-H-FILE-DATE            PIC 9(08).                    
004314     05  EML-H-FILE-DATE-R     REDEFINES     EML-H-FILE-DATE.     
004316         07  EML-H-FILE-DT-CC       PIC 9(02).                    
004318         07  EML-H-FILE-DT-YY       PIC 9(02).                    
004320         07  EML-H-FILE-DT-MM       PIC 9(02).                    
004322         07  EML-H-FILE-DT-DD       PIC 9(02).                    
004324     05  EML-H-RERUN-IND            PIC 9(01).                    
004326     05  EML-H-BANK-NAME            PIC X(25).                    
004328     05  FILLER                     PIC X(227).                   
004330 01  EML-ACCT-HEADER-REC.                                         
004332     05  EML-AH-REC-TYPE            PIC 9(02).                    
004334     05  EML-AH-BANK                PIC 9(04).                    
004336     05  EML-AH-APPL                PIC X(03).                    
004338     05  EML-AH-ACCTNO              PIC 9(12).                    
004340     05  EML-AH-SUBNO               PIC 9(10).                    
004342     05  EML-AH-PREMIER-FLAG        PIC 9(01).                    
004344     05  EML-AH-NTC-FORM-TYPE       PIC X(03).                    
004346     05  EML-AH-NTC-TITLE           PIC X(40).                    
004348     05  EML-AH-CUST-NAME           PIC X(25).                    
004350     05  EML-AH-EMAIL-ADD           PIC X(120).                   
004352     05  EML-AH-DIGITAL-FLAG        PIC X(01).                    
004354     05  FILLER                     PIC X(49).                    
004356 01  EML-ACCT-DETAIL-REC.                                         
004358     05  EML-AD-REC-TYPE            PIC 9(02).                    
004360     05  EML-AD-BANK                PIC 9(04).                    
004362     05  EML-AD-APPL                PIC X(03).                    
004364     05  EML-AD-ACCTNO              PIC 9(12).                    
004366     05  EML-AD-SUBNO               PIC 9(10).                    
004368     05  EML-AD-REC-NO              PIC 9(04).                    
004370     05  EML-AD-REC-AREA            PIC X(140).                   
004372     05  FILLER                     PIC X(95).                    
004374 01  EML-ACCT-TRAILER-REC.                                        
004376     05  EML-AT-REC-TYPE            PIC 9(02).                    
004378     05  EML-AT-BANK                PIC 9(04).                    
004380     05  EML-AT-APPL                PIC X(03).                    
004382     05  EML-AT-ACCTNO              PIC 9(12).                    
004384     05  EML-AT-SUBNO               PIC 9(10).                    
004386     05  FILLER                     PIC X(239).                   
004388 01  EML-TRAILER-REC.                                             
004390     05  EML-T-REC-TYPE             PIC 9(02).                    
004392     05  EML-T-BANK                 PIC 9(04).                    
004394     05  EML-T-APPL                 PIC X(03).                    
004396     05  EML-T-NO-RECORDS           PIC 9(08).                    
004398     05  EML-T-NO-NOTICES           PIC 9(08).                    
004400     05  FILLER                     PIC X(245).                   
004402                                                                  
004404 01  WS-MSG-TBL-MAX             PIC 99   VALUE 20.                
004406 01  WS-MSG-TABLE.                                                
004408     05  WS-MSG-TOT-CODE        PIC 9(4) OCCURS 20 TIMES.         
004410 01  WS-MSG-TEST                PIC 9    VALUE 0.                 
004412                                                                  
004414 01  LSR-MESSAGE-FIELDS.                                          
004416     05  LSR-MESSAGE-1               PIC X(100) VALUE SPACES.     
004418     05  LSR-MESSAGE-2               PIC X(100) VALUE SPACES.     
004420                                                                  
004422 01  WS-BRCH-ADDR-FLAG               PIC 9    VALUE 0.            
004424     88  BRCH-ADDR-FOUND             VALUE 1.                     
004426                                                                  
004428 01  FM-DOWNLOAD-RECORD              PIC X(540).                  
004430 01  FM-DOWNLOAD-REC-CNT-X.                                       
004432     05  FILLER                      PIC X(34)                    
004434         VALUE "0000000000000000000000000000000000".              
004436     05  FM-DOWNLOAD-REC-CNT         PIC 9(06)  VALUE 0.          
004438 01  FM-DOWNLOAD-BANK-X.                                          
004440     05  FM-DOWNLOAD-BANK            PIC 9(04)  VALUE 0.          
004442                                                                  
004444 01  SXLK-HDR-KEY.                                                
004446     05  SXLK-HDR-BANK               PIC 9(04)  VALUE ZEROS.      
004448     05  SXLK-HDR-APP                PIC X(03)  VALUE "HDR".      
004450     05  SXLK-HDR-DATE               PIC 9(06)  VALUE ZEROS.      
004452     05  FILLER                      PIC X(34)  VALUE SPACES.     
004454                                                                  
004456 01  CFDF-HDR-KEY.                                                
004458     05  CFDF-HDR-BANK               PIC 9(04) VALUE ZEROS.       
004460     05  CFDF-HDR-APP                PIC X(03) VALUE "HDR".       
004462     05  CFDF-HDR-DATE               PIC 9(06) VALUE ZEROS.       
004464     05  CFDF-HDR-L4                 PIC X(04) VALUE SPACES.      
004466                                                                  
004468                                                                  
004470                                                                  
004472 01  TDA-ACTIVITY-RECORD             PIC X(225).                  
004474 01  TDA-ACTIVITY-REC.                                            
004476     05  TDV-BANK-NO                 PIC 9(04).                   
004478     05  TDV-BANK-NO-R REDEFINES TDV-BANK-NO.                     
004480         10  FILLER                  PIC 9(01).                   
004482         10  TDV-BANK-NO3            PIC 9(03).                   
004484     05  TDV-CUST-NO                 PIC 9(12).                   
004486     05  TDV-ACCT-NO                 PIC 9(10).                   
004488     05  TDV-DATE-TRX                PIC 9(08).                   
004490     05  TDV-DATE-TRX-R REDEFINES TDV-DATE-TRX.                   
004492         10  TDV-TRXDT-CCYY          PIC 9(04).                   
004494         10  TDV-TRXDT-MMDD          PIC 9(04).                   
004496     05  TDV-DATE-EFF                PIC 9(08).                   
004498     05  TDV-DATE-EFF-R REDEFINES TDV-DATE-EFF.                   
004500         10  TDV-EFFDT-CCYY          PIC 9(04).                   
004502         10  TDV-EFFDT-MMDD          PIC 9(04).                   
004504     05  TDV-TRANCODE                PIC 9(04).                   
004506     05  TDV-DR-CR                   PIC X(01).                   
004508     05  TDV-ERR-FLAG                PIC X(02).                   
004510     05  TDV-AMOUNT                  PIC 9(12)V99.                
004512     05  TDV-ACH-CST                 PIC X(02).                   
004514     05  TDV-DESC                    PIC X(80).                   
004516     05  TDV-ACH-DESC REDEFINES TDV-DESC.                         
004518         10  TDV-ACH-CO-NAME.                                     
004520             15  TDV-ACH-TRANSFER    PIC X(10).                   
004522             15  FILLER              PIC X(06).                   
004524         10  TDV-ACH-CO-DESC         PIC X(10).                   
004526         10  FILLER                  PIC X(54).                   
004528     05  TDV-SEQUENCE                PIC 9(16).                   
004530     05  TDV-SEQUENCE-R REDEFINES TDV-SEQUENCE.                   
004532         10  TDV-SEQ-ID              PIC X(01).                   
004534         10  TDV-SEQ-NO              PIC X(15).                   
004536     05  TDV-SERIAL-NO               PIC 9(10).                   
004538     05  TDV-SOURCE-CODE             PIC X(01).                   
004540     05  TDV-ITEM-TIEBRK.                                         
004542         10  TDV-ITEM-TIEBRK-9       PIC 9(20).                   
004544     05  TDV-FORMAT-CODE             PIC X(01).                   
004546     05  TDV-EMP-ACT-NBR             PIC 9(03).                   
004548     05  TDV-EMP-ACT-AMT             PIC S9(09)V99.               
004550     05  FILLER                      PIC X(18).                   
004552 01  TDA-BATCH-RECORD.                                            
004554     05  FILLER                      PIC X(26).                   
004556     05  TDV-MNT-STRUCT              PIC 9(02).                   
004558     05  TDV-MNT-TRANCODE            PIC 9(04).                   
004560     05  TDV-MNT-CHGDATA             PIC X(30).                   
004562     05  TDV-MNT-APPLY               PIC X(01).                   
004564     05  TDV-MNT-ORIGIN              PIC X(08).                   
004566     05  FILLER                      PIC X(01).                   
004568     05  TDV-MNT-SYSUSE              PIC X(01).                   
004570     05  FILLER                      PIC X(01).                   
004572     05  TDV-DDA-FROM-ACCT           PIC 9(12).                   
004574     05  TDV-DDA-FROM-SUB-IND        PIC 9(03).                   
004576     05  FILLER                      PIC X(136).                  
004578*                                                                 
004580 01  TDA-NINES-ACTIVITY.                                          
004582     05  TDT-BANK-NO                 PIC 9(04).                   
004584     05  TDT-CUST-NO                 PIC 9(12).                   
004586     05  TDT-ACCT-NO                 PIC 9(10).                   
004588     05  TDT-DR-COUNT                PIC 9(06).                   
004590     05  TDT-DR-AMOUNT               PIC 9(12)V99.                
004592     05  TDT-CR-COUNT                PIC 9(06).                   
004594     05  TDT-CR-AMOUNT               PIC 9(12)V99.                
004596     05  TDT-APP-DESCRIPTION.                                     
004598         10  TDT-APP                 PIC X(18).                   
004600         10  TDT-FILE-DATE           PIC 9(06).                   
004602     05  FILLER                      PIC X(135).                  
004604*                                                                 
004606                                                                  
004608                                                                  
004610 01  TDA-TDA-FILE-ID.                                             
004612     05  TDA-TDA-APPL                PIC XXX.                     
004614     05  TDA-TDA-FCTL-IND            PIC XXX VALUE "XA2".         
004616     05  TDA-TDA-ID-DATE.                                         
004618         10  TDA-TDA-ID-MM           PIC 99.                      
004620         10  TDA-TDA-ID-DD           PIC 99.                      
004622     05  FILLER                      PIC X(05) VALUE "/TDA0".     
004624     05  TDA-TDA-ID-SUFF             PIC X.                       
004626     05  TDA-TDA-ID-DC               PIC 99.                      
004628     05  TDA-TDA-ID-BANK             PIC 999.                     
004630     05  FILLER                      PIC X(01) VALUE ".".         
004632                                                                  
004634 01  TDA-TDA-FILE-STATUS             PIC 9(01) VALUE 0.           
004636 01  TDA-TDA-FILE-RECS               PIC 9(12) VALUE 0.           
004638 01  TDA-OUTPUT-FILE-ID.                                          
004640     05  FILLER                         PIC X(06).                
004642     05  TDA-OUTPUT-FILE-DATE           PIC 9(04).                
004644     05  FILLER                         PIC X(06).                
004646     05  TDA-OUTPUT-FILE-DC             PIC 9(02).                
004648     05  TDA-OUTPUT-FILE-BANK           PIC 9(03).                
004650     05  TDA-OUTPUT-FILE-PERIOD         PIC X(01).                
004652 01  WS-FCTL-RERUN-CODE              PIC X(01).                   
004654 01  WS-FCTL-APP                     PIC X(03) VALUE SPACES.      
004656 01  WS-FCTL-ATTRIB-CNT              PIC 9(12) VALUE 0.           
004658 01  WS-FCTL-PILOT                   PIC 9(01) VALUE 0.           
004660 01  WS-FCTL-USERCODE.                                            
004662     05  WS-FCTL-USER                PIC X(03) VALUE SPACES.      
004664     05  FILLER                      PIC X(14) VALUE SPACES.      
004666                                                                  
004668 01  FCTL-RECORD.                                                 
004670    05  FCTL-PROCESS-DATE             PIC 9(08).                  
004672    05  FCTL-PROCESS-DATE-R REDEFINES FCTL-PROCESS-DATE.          
004674        10  FCTL-PROC-CC              PIC 9(02).                  
004676        10  FCTL-PROC-YY              PIC 9(02).                  
004678        10  FCTL-PROC-MMDD            PIC 9(04).                  
004680    05  FCTL-DATE-CREATE              PIC 9(08).                  
004682    05  FCTL-DATE-CREATE-X REDEFINES FCTL-DATE-CREATE.            
004684        10  FCTL-CREATE-CC            PIC 9(02).                  
004686        10  FCTL-CREATE-YY            PIC 9(02).                  
004688        10  FCTL-CREATE-MMDD          PIC 9(04).                  
004690    05  FCTL-TIME-CREATE              PIC 9(06).                  
004692    05  FCTL-HASH-TOTAL               PIC 9(10)V99.               
004694    05  FCTL-HASH-TOTAL9 REDEFINES FCTL-HASH-TOTAL                
004696                                      PIC 9(12).                  
004698    05  FCTL-BANK-NO                  PIC 9(03).                  
004700    05  FCTL-FILE-CODE-X.                                         
004702        10  FCTL-FILE-CODE            PIC 9(10).                  
004704    05  FCTL-APPL                     PIC X(03).                  
004706    05  FCTL-FILE-NAME.                                           
004708        10  FCTL-FILE-NAME21          PIC X(21).                  
004710        10  FILLER                    PIC X(11).                  
004712    05  FCTL-PACK-NAME                PIC X(10).                  
004714    05  FCTL-STATUS-IN                PIC X(01).                  
004716    05  FCTL-STATUS-OUT               PIC X(01).                  
004718    05  FCTL-ACTION                   PIC X(01).                  
004720    05  FCTL-RESULT                   PIC X(72).                  
004722    05  FCTL-SORT-DATE                PIC 9(08).                  
004724    05  FCTL-BANK-NO-4                PIC 9(04).                  
004726 01  FCTL-CALL-PROG                   PIC X(31)                   
004728              VALUE "CSI/FILECTL/LIB ON OBJ".                     
004730 01  FCTL-APPL-A17.                                               
004732     05  FCTL-DDA-A17                 PIC 9(01) VALUE 0.          
004734     05  FCTL-SAV-A17                 PIC 9(01) VALUE 0.          
004736     05  FCTL-COD-A17                 PIC 9(01) VALUE 0.          
004738     05  FCTL-IRA-A17                 PIC 9(01) VALUE 0.          
004740     05  FCTL-CLN-A17                 PIC 9(01) VALUE 0.          
004742     05  FCTL-ILN-A17                 PIC 9(01) VALUE 0.          
004744     05  FCTL-ONL-A17                 PIC 9(01) VALUE 0.          
004746     05  FCTL-MCR-A17                 PIC 9(01) VALUE 0.          
004748     05  FCTL-GNL-A17                 PIC 9(01) VALUE 0.          
```

⚠️  This is the source code you must document.
    401 lines from 1970 to 2370.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

