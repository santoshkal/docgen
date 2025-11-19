# LLM Request Debug File
Generated: 2025-11-18T19:04:50.734128

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 22/55
- **Model**: gpt-4.1
- **Chunk Number**: 22
- **Pass Number**: 3
- **Attempt Number**: 4 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,086 tokens
- **User Prompt**: ~7,499 tokens
- **Total Input**: ~9,585 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 22/55" (ID: detailed-code-explanation)

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


**CHUNK 22 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T18:05:37.383587", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 22 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 10547 to 10848 (302 lines)\nChunk Tokens (estimated): ~6,563\nActual Input Tokens: 7,969 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 10547-10848 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 22 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 22 of 55.\n\n\n=============================================================================\nCHUNK 22 SOURCE CODE (Lines 10547-10848)\n=============================================================================\n\n```cobol\n021102                 TDB-TDA-ACTV-DATA.                               \n021104             15  TDB-TDA-ACTDI-DS-NBR         PIC 9(2).           \n021106             15  TDB-TDA-ACTDI-HLD-NBR        PIC 9(4).           \n021108             15  TDB-TDA-ACTDI-CLS-DS         PIC 9(1).           \n021110             15  TDB-TDA-ACTDI-DS-AMT         PIC S9(12)V9(2).    \n021112             15  TDB-TDA-ACTDI-PR-AMT         PIC S9(12)V9(2).    \n021114             15  TDB-TDA-ACTDI-INT-AMT        PIC S9(12)V9(2).    \n021116             15  TDB-TDA-ACTDI-WH-AMT         PIC S9(12)V9(2).    \n021118             15  TDB-TDA-ACTDI-ST-AMT         PIC S9(12)V9(2).    \n021120             15  TDB-TDA-ACTDI-DISP-CD        PIC 9(1).           \n021122             15  TDB-TDA-ACTDI-T-ACCT         PIC 9(12).          \n021124             15  TDB-TDA-ACTDI-T-ACCTS        PIC 9(10).          \n021126             15  TDB-TDA-ACTDI-N-PRC-D        PIC 9(8).           \n021128             15  FILLER                       PIC X(292).         \n021130                                                                  \n021132         10  TDB-TDA-NONDB-FIELDS.                                \n021134             15  TDB-TDA-ACTV-NEW-SERIAL-X.                       \n021136                 20  TDB-TDA-ACTV-NEW-SERIAL  PIC 9(12).          \n021138                                                                  \n021140     05  TDB-TDAINDXRT.                                           \n021142         10  TDB-TDAIR-BANK-X.                                    \n021144             15  TDB-TDAIR-BANK            PIC 9(4).              \n021146         10  TDB-TDAIR-REGION-X.                                  \n021148             15  TDB-TDAIR-REGION          PIC 9(2).              \n021150         10  TDB-TDAIR-INDX-CD-X.                                 \n021152             15  TDB-TDAIR-INDX-CD         PIC 9(2).              \n021154         10  TDB-TDAIR-EFF-DATE-X.                                \n021156             15  TDB-TDAIR-EFF-DATE        PIC 9(8).              \n021158         10  TDB-TDAIR-END-DATE-X.                                \n021160             15  TDB-TDAIR-END-DATE        PIC 9(8).              \n021162         10  TDB-TDAIR-VOID-DATE-X.                               \n021164             15  TDB-TDAIR-VOID-DATE       PIC 9(8).              \n021166         10  TDB-TDAIR-ADD-DATE-X.                                \n021168             15  TDB-TDAIR-ADD-DATE        PIC 9(8).              \n021170         10  TDB-TDAIR-ADD-TIME-X.                                \n021172             15  TDB-TDAIR-ADD-TIME        PIC 9(8).              \n021174         10  TDB-TDAIR-PUB-ID              PIC X(8).              \n021176         10  TDB-TDAIR-VOID-PUB-ID         PIC X(8).              \n021178         10  TDB-TDAIR-DESC                PIC X(20).             \n021180         10  TDB-TDAIR-RATE-X.                                    \n021182             15  TDB-TDAIR-RATE            PIC S9(2)V9(3).        \n021184                                                                  \n021186     05  TDB-TDAMARGRT.                                           \n021188         10  TDB-TDAMR-BANK-X.                                    \n021190             15  TDB-TDAMR-BANK            PIC 9(4).              \n021192         10  TDB-TDAMR-REGION-X.                                  \n021194             15  TDB-TDAMR-REGION          PIC 9(2).              \n021196         10  TDB-TDAMR-MARG-CD-X.                                 \n021198             15  TDB-TDAMR-MARG-CD         PIC 9(2).              \n021200         10  TDB-TDAMR-EFF-DATE-X.                                \n021202             15  TDB-TDAMR-EFF-DATE        PIC 9(8).              \n021204         10  TDB-TDAMR-END-DATE-X.                                \n021206             15  TDB-TDAMR-END-DATE        PIC 9(8).              \n021208         10  TDB-TDAMR-VOID-DATE-X.                               \n021210             15  TDB-TDAMR-VOID-DATE       PIC 9(8).              \n021212         10  TDB-TDAMR-ADD-DATE-X.                                \n021214             15  TDB-TDAMR-ADD-DATE        PIC 9(8).              \n021216         10  TDB-TDAMR-ADD-TIME-X.                                \n021218             15  TDB-TDAMR-ADD-TIME        PIC 9(8).              \n021220         10  TDB-TDAMR-PUB-ID              PIC X(8).              \n021222         10  TDB-TDAMR-VOID-PUB-ID         PIC X(8).              \n021224         10  TDB-TDAMR-DESC                PIC X(20).             \n021226         10  TDB-TDAMR-RATE-X.                                    \n021228             15  TDB-TDAMR-RATE            PIC S9(2)V9(3).        \n021230                                                                  \n021232     05  TDB-TDATIERRT.                                           \n021234         10  TDB-TDATR-BANK-X.                                    \n021236             15  TDB-TDATR-BANK            PIC 9(4).              \n021238         10  TDB-TDATR-REGION-X.                                  \n021240             15  TDB-TDATR-REGION          PIC 9(2).              \n021242         10  TDB-TDATR-TIER-CD-X.                                 \n021244             15  TDB-TDATR-TIER-CD         PIC 9(2).              \n021246         10  TDB-TDATR-EFF-DATE-X.                                \n021248             15  TDB-TDATR-EFF-DATE        PIC 9(8).              \n021250         10  TDB-TDATR-END-DATE-X.                                \n021252             15  TDB-TDATR-END-DATE        PIC 9(8).              \n021254         10  TDB-TDATR-VOID-DATE-X.                               \n021256             15  TDB-TDATR-VOID-DATE       PIC 9(8).              \n021258         10  TDB-TDATR-ADD-DATE-X.                                \n021260             15  TDB-TDATR-ADD-DATE        PIC 9(8).              \n021262         10  TDB-TDATR-ADD-TIME-X.                                \n021264             15  TDB-TDATR-ADD-TIME        PIC 9(8).              \n021266         10  TDB-TDATR-PUB-ID              PIC X(8).              \n021268         10  TDB-TDATR-VOID-PUB-ID         PIC X(8).              \n021270         10  TDB-TDATR-DESC                PIC X(20).             \n021272         10  TDB-TDATR-TIER-INCR1-X.                              \n021274             15  TDB-TDATR-TIER-INCR1      PIC S9(2)V9(3).        \n021276         10  TDB-TDATR-TIER-BAL1-X.                               \n021278             15  TDB-TDATR-TIER-BAL1       PIC S9(12)V9(2).       \n021280         10  TDB-TDATR-TIER-INCR2-X.                              \n021282             15  TDB-TDATR-TIER-INCR2      PIC S9(2)V9(3).        \n021284         10  TDB-TDATR-TIER-BAL2-X.                               \n021286             15  TDB-TDATR-TIER-BAL2       PIC S9(12)V9(2).       \n021288         10  TDB-TDATR-TIER-INCR3-X.                              \n021290             15  TDB-TDATR-TIER-INCR3      PIC S9(2)V9(3).        \n021292         10  TDB-TDATR-TIER-BAL3-X.                               \n021294             15  TDB-TDATR-TIER-BAL3       PIC S9(12)V9(2).       \n021296         10  TDB-TDATR-TIER-INCR4-X.                              \n021298             15  TDB-TDATR-TIER-INCR4      PIC S9(2)V9(3).        \n021300         10  TDB-TDATR-TIER-BAL4-X.                               \n021302             15  TDB-TDATR-TIER-BAL4       PIC S9(12)V9(2).       \n021304         10  TDB-TDATR-TIER-INCR5-X.                              \n021306             15  TDB-TDATR-TIER-INCR5      PIC S9(2)V9(3).        \n021308         10  TDB-TDATR-TIER-BAL5-X.                               \n021310             15  TDB-TDATR-TIER-BAL5       PIC S9(12)V9(2).       \n021312         10  TDB-TDATR-TIER-INCR6-X.                              \n021314             15  TDB-TDATR-TIER-INCR6      PIC S9(2)V9(3).        \n021316         10  TDB-TDATR-TIER-BAL6-X.                               \n021318             15  TDB-TDATR-TIER-BAL6       PIC S9(12)V9(2).       \n021320         10  TDB-TDATR-TIER-INCR7-X.                              \n021322             15  TDB-TDATR-TIER-INCR7      PIC S9(2)V9(3).        \n021324         10  TDB-TDATR-TIER-BAL7-X.                               \n021326             15  TDB-TDATR-TIER-BAL7       PIC S9(12)V9(2).       \n021328         10  TDB-TDATR-TIER-INCR8-X.                              \n021330             15  TDB-TDATR-TIER-INCR8      PIC S9(2)V9(3).        \n021332         10  TDB-TDATR-TIER-BAL8-X.                               \n021334             15  TDB-TDATR-TIER-BAL8       PIC S9(12)V9(2).       \n021336         10  TDB-TDATR-TIER-INCR9-X.                              \n021338             15  TDB-TDATR-TIER-INCR9      PIC S9(2)V9(3).        \n021340         10  TDB-TDATR-TIER-BAL9-X.                               \n021342             15  TDB-TDATR-TIER-BAL9       PIC S9(12)V9(2).       \n021344         10  TDB-TDATR-TIER-INCR10-X.                             \n021346             15  TDB-TDATR-TIER-INCR10     PIC S9(2)V9(3).        \n021348         10  TDB-TDATR-TIER-BAL10-X.                              \n021350             15  TDB-TDATR-TIER-BAL10      PIC S9(12)V9(2).       \n021352         10  TDB-TDATR-TIER-INCR11-X.                             \n021354             15  TDB-TDATR-TIER-INCR11     PIC S9(2)V9(3).        \n021356         10  TDB-TDATR-TIER-BAL11-X.                              \n021358             15  TDB-TDATR-TIER-BAL11      PIC S9(12)V9(2).       \n021360         10  TDB-TDATR-TIER-INCR12-X.                             \n021362             15  TDB-TDATR-TIER-INCR12     PIC S9(2)V9(3).        \n021364         10  TDB-TDATR-TIER-BAL12-X.                              \n021366             15  TDB-TDATR-TIER-BAL12      PIC S9(12)V9(2).       \n021368         10  TDB-TDATR-TIER-INCR13-X.                             \n021370             15  TDB-TDATR-TIER-INCR13     PIC S9(2)V9(3).        \n021372         10  TDB-TDATR-TIER-BAL13-X.                              \n021374             15  TDB-TDATR-TIER-BAL13      PIC S9(12)V9(2).       \n021376         10  TDB-TDATR-TIER-INCR14-X.                             \n021378             15  TDB-TDATR-TIER-INCR14     PIC S9(2)V9(3).        \n021380         10  TDB-TDATR-TIER-BAL14-X.                              \n021382             15  TDB-TDATR-TIER-BAL14      PIC S9(12)V9(2).       \n021384         10  TDB-TDATR-TIER-INCR15-X.                             \n021386             15  TDB-TDATR-TIER-INCR15     PIC S9(2)V9(3).        \n021388         10  TDB-TDATR-TIER-BAL15-X.                              \n021390             15  TDB-TDATR-TIER-BAL15      PIC S9(12)V9(2).       \n021392                                                                  \n021394     05  TDB-TDARISERT.                                           \n021396         10  TDB-TDARR-BANK-X.                                    \n021398             15  TDB-TDARR-BANK            PIC 9(4).              \n021400         10  TDB-TDARR-REGION-X.                                  \n021402             15  TDB-TDARR-REGION          PIC 9(2).              \n021404         10  TDB-TDARR-RISE-CD-X.                                 \n021406             15  TDB-TDARR-RISE-CD         PIC 9(2).              \n021408         10  TDB-TDARR-EFF-DATE-X.                                \n021410             15  TDB-TDARR-EFF-DATE        PIC 9(8).              \n021412         10  TDB-TDARR-END-DATE-X.                                \n021414             15  TDB-TDARR-END-DATE        PIC 9(8).              \n021416         10  TDB-TDARR-VOID-DATE-X.                               \n021418             15  TDB-TDARR-VOID-DATE       PIC 9(8).              \n021420         10  TDB-TDARR-ADD-DATE-X.                                \n021422             15  TDB-TDARR-ADD-DATE        PIC 9(8).              \n021424         10  TDB-TDARR-ADD-TIME-X.                                \n021426             15  TDB-TDARR-ADD-TIME        PIC 9(8).              \n021428         10  TDB-TDARR-PUB-ID              PIC X(8).              \n021430         10  TDB-TDARR-VOID-PUB-ID         PIC X(8).              \n021432         10  TDB-TDARR-DESC                PIC X(20).             \n021434         10  TDB-TDARR-FRQ-TYPE-X.                                \n021436             15  TDB-TDARR-FRQ-TYPE        PIC 9(1).              \n021438         10  TDB-TDARR-CYC-FRQ1-X.                                \n021440             15  TDB-TDARR-CYC-FRQ1        PIC 9(3).              \n021442         10  TDB-TDARR-CYC-INC1-X.                                \n021444             15  TDB-TDARR-CYC-INC1        PIC S9(2)V9(3).        \n021446         10  TDB-TDARR-CYC-FRQ2-X.                                \n021448             15  TDB-TDARR-CYC-FRQ2        PIC 9(3).              \n021450         10  TDB-TDARR-CYC-INC2-X.                                \n021452             15  TDB-TDARR-CYC-INC2        PIC S9(2)V9(3).        \n021454         10  TDB-TDARR-CYC-FRQ3-X.                                \n021456             15  TDB-TDARR-CYC-FRQ3        PIC 9(3).              \n021458         10  TDB-TDARR-CYC-INC3-X.                                \n021460             15  TDB-TDARR-CYC-INC3        PIC S9(2)V9(3).        \n021462         10  TDB-TDARR-CYC-FRQ4-X.                                \n021464             15  TDB-TDARR-CYC-FRQ4        PIC 9(3).              \n021466         10  TDB-TDARR-CYC-INC4-X.                                \n021468             15  TDB-TDARR-CYC-INC4        PIC S9(2)V9(3).        \n021470         10  TDB-TDARR-CYC-FRQ5-X.                                \n021472             15  TDB-TDARR-CYC-FRQ5        PIC 9(3).              \n021474         10  TDB-TDARR-CYC-INC5-X.                                \n021476             15  TDB-TDARR-CYC-INC5        PIC S9(2)V9(3).        \n021478         10  TDB-TDARR-CYC-FRQ6-X.                                \n021480             15  TDB-TDARR-CYC-FRQ6        PIC 9(3).              \n021482         10  TDB-TDARR-CYC-INC6-X.                                \n021484             15  TDB-TDARR-CYC-INC6        PIC S9(2)V9(3).        \n021486         10  TDB-TDARR-CYC-FRQ7-X.                                \n021488             15  TDB-TDARR-CYC-FRQ7        PIC 9(3).              \n021490         10  TDB-TDARR-CYC-INC7-X.                                \n021492             15  TDB-TDARR-CYC-INC7        PIC S9(2)V9(3).        \n021494         10  TDB-TDARR-CYC-FRQ8-X.                                \n021496             15  TDB-TDARR-CYC-FRQ8        PIC 9(3).              \n021498         10  TDB-TDARR-CYC-INC8-X.                                \n021500             15  TDB-TDARR-CYC-INC8        PIC S9(2)V9(3).        \n021502         10  TDB-TDARR-CYC-FRQ9-X.                                \n021504             15  TDB-TDARR-CYC-FRQ9        PIC 9(3).              \n021506         10  TDB-TDARR-CYC-INC9-X.                                \n021508             15  TDB-TDARR-CYC-INC9        PIC S9(2)V9(3).        \n021510         10  TDB-TDARR-CYC-FRQ10-X.                               \n021512             15  TDB-TDARR-CYC-FRQ10       PIC 9(3).              \n021514         10  TDB-TDARR-CYC-INC10-X.                               \n021516             15  TDB-TDARR-CYC-INC10       PIC S9(2)V9(3).        \n021518                                                                  \n021520     05  TDB-TDAHMS.                                              \n021522         10  TDB-TDAHMS-BANK-X.                                   \n021524             15  TDB-TDAHMS-BANK           PIC  9(4).             \n021526         10  TDB-TDAHMS-APPL-X.                                   \n021528             15  TDB-TDAHMS-APPL           PIC  9(1).             \n021530         10  TDB-TDAHMS-CUST-X.                                   \n021532             15  TDB-TDAHMS-CUST           PIC  9(12).            \n021534         10  TDB-TDAHMS-ACCT-X.                                   \n021536             15  TDB-TDAHMS-ACCT           PIC  9(10).            \n021538         10  TDB-TDAHMS-TYPE-X.                                   \n021540             15  TDB-TDAHMS-TYPE           PIC  X(1).             \n021542         10  TDB-TDAHMS-BK-TYPE-X.                                \n021544             15  TDB-TDAHMS-BK-TYPE        PIC  X(1).             \n021546         10  TDB-TDAHMS-DR-CR-IND-X.                              \n021548             15  TDB-TDAHMS-DR-CR-IND      PIC  X(1).             \n021550         10  TDB-TDAHMS-SOURCE-X.                                 \n021552             15  TDB-TDAHMS-SOURCE         PIC  9(2).             \n021554         10  TDB-TDAHMS-HOLD-NBR-X.                               \n021556             15  TDB-TDAHMS-HOLD-NBR       PIC  9(4).             \n021558         10  TDB-TDAHMS-AMT-X.                                    \n021560             15  TDB-TDAHMS-AMT            PIC S9(12)V99.         \n021562         10  TDB-TDAHMS-ORIG-AMT-X.                               \n021564             15  TDB-TDAHMS-ORIG-AMT       PIC  9(12)V99.         \n021566         10  TDB-TDAHMS-COMMENT-X.                                \n021568             15  TDB-TDAHMS-COMMENT        PIC  X(40).            \n021570         10  TDB-TDAHMS-PUB-ID-X.                                 \n021572             15  TDB-TDAHMS-PUB-ID         PIC  X(8).             \n021574         10  TDB-TDAHMS-VOID-PUB-ID-X.                            \n021576             15  TDB-TDAHMS-VD-PUB-ID      PIC  X(8).             \n021578         10  TDB-TDAHMS-ADD-DATE-X.                               \n021580             15  TDB-TDAHMS-ADD-DATE       PIC  9(8).             \n021582         10  TDB-TDAHMS-ADD-TIME-X.                               \n021584             15  TDB-TDAHMS-ADD-TIME       PIC  9(8).             \n021586         10  TDB-TDAHMS-VOID-DATE-X.                              \n021588             15  TDB-TDAHMS-VOID-DATE      PIC  9(8).             \n021590         10  TDB-TDAHMS-PLG-ACCT-X.                               \n021592             15  TDB-TDAHMS-PLG-ACCT       PIC  9(12).            \n021594         10  TDB-TDAHMS-PLG-ACCT-S-X.                             \n021596             15  TDB-TDAHMS-PLG-ACCT-S     PIC  9(10).            \n021598         10  TDB-TDAHMS-EXPIRE-DT-X.                              \n021600             15  TDB-TDAHMS-EXPIRE-DT      PIC  9(8).             \n021602         10  TDB-TDAHMS-AVAIL-BAL-X.                              \n021604             15  TDB-TDAHMS-AVAIL-BAL      PIC S9(12)V99.         \n021606         10  TDB-TDAHMS-SERIAL-NUM-X.                             \n021608             15  TDB-TDAHMS-SERIAL-NUM     PIC  9(10).            \n021610         10  TDB-TDAHMS-END-SERIAL-X.                             \n021612             15  TDB-TDAHMS-END-SERIAL     PIC  9(10).            \n021614         10  TDB-TDAHMS-NAME-X.                                   \n021616             15  TDB-TDAHMS-NAME           PIC  X(10).            \n021618         10  TDB-TDAHMS-START-DATE-X.                             \n021620             15  TDB-TDAHMS-START-DATE     PIC  9(8).             \n021622         10  TDB-TDAHMS-DAILY-ACCR-X.                             \n021624             15  TDB-TDAHMS-DAILY-ACCR     PIC S9(12)V9(6).       \n021626         10  TDB-TDAHMS-ORG-ADD-DT         PIC  9(8).             \n021628         10  TDB-TDAHMS-ORG-ADD-TM         PIC  9(8).             \n021630         10  TDB-TDAHMS-ORG-PUB-ID         PIC  X(8).             \n021632         10  TDB-TDAHMS-AMT-LAST-UPD       PIC S9(12)V9(2).       \n021634         10  TDB-TDAHMS-DATE-LAST-UPD      PIC  9(8).             \n021636                                                                  \n021638     05  TDB-TDAREPORTS.                                          \n021640         10  TDB-TDARPT-PRT-DT-X.                                 \n021642             15  TDB-TDARPT-PRT-DT         PIC 9(8).              \n021644         10  TDB-TDARPT-BANK-X.                                   \n021646             15  TDB-TDARPT-BANK           PIC 9(4).              \n021648         10  TDB-TDARPT-BRCH-X.                                   \n021650             15  TDB-TDARPT-BRCH           PIC 9(4).              \n021652         10  TDB-TDARPT-APPL-X.                                   \n021654             15  TDB-TDARPT-APPL           PIC 9(1).              \n021656         10  TDB-TDARPT-RPT-NBR-X.                                \n021658             15  TDB-TDARPT-RPT-NBR        PIC 9(3).              \n021660         10  TDB-TDARPT-ACCT-X.                                   \n021662             15  TDB-TDARPT-ACCT           PIC 9(10).             \n021664         10  TDB-TDARPT-CUST-R.                                   \n021666             15  TDB-TDARPT-CUST           PIC 9(12).             \n021668         10  TDB-TDARPT-EXP-DT-X.                                 \n021670             15  TDB-TDARPT-EXP-DT         PIC 9(8).              \n021672         10  TDB-TDARPT-REAS-X.                                   \n021674             15  TDB-TDARPT-REAS           PIC 9(4).              \n021676         10  TDB-TDARPT-REMARKS            PIC X(100).            \n021678         10  TDB-TDARPT-REMARKS-NUMERIC REDEFINES                 \n021680             TDB-TDARPT-REMARKS.                                  \n021682             15  TDB-TDARPT-ACH-AMT        PIC 9(8)V99.           \n021684             15  TDB-TDARPT-DR-CR          PIC X.                 \n021686             15  TDB-TDARPT-SOURCE         PIC X.                 \n021688             15  TDB-TDARPT-CHECK-NBR      PIC X(10).             \n021690             15  TDB-TDARPT-DS-NBR         PIC 9(2).              \n021692             15  TDB-TDARPT-AUTO-DIST      PIC X.                 \n021694             15  TDB-TDARPT-EMAIL-IND      PIC 9(01).             \n021696             15  TDB-TDARPT-DS-DISP-CD     PIC 9.                 \n021698             15  TDB-TDARPT-DS-DISP-ACCT   PIC 9(12).             \n021700             15  TDB-TDARPT-DS-DISP-ACCT-S PIC 9(10).             \n021702             15  FILLER                    PIC X(51).             \n021704         10  TDB-TDARPT-REMARKS-FM REDEFINES                      \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    302 lines from 10547 to 10848.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 22, "total_chunks": 55, "start_line": 10547, "end_line": 10848, "line_count": 302}

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
- Source code length: 27006 characters

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
CHUNK 22 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 10547 to 10848 (302 lines)
Chunk Tokens (estimated): ~6,563
Actual Input Tokens: 7,969 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 10547-10848 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 22 of 55 chunks
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
      The source code below is only CHUNK 22 of 55.


=============================================================================
CHUNK 22 SOURCE CODE (Lines 10547-10848)
=============================================================================

```cobol
021102                 TDB-TDA-ACTV-DATA.                               
021104             15  TDB-TDA-ACTDI-DS-NBR         PIC 9(2).           
021106             15  TDB-TDA-ACTDI-HLD-NBR        PIC 9(4).           
021108             15  TDB-TDA-ACTDI-CLS-DS         PIC 9(1).           
021110             15  TDB-TDA-ACTDI-DS-AMT         PIC S9(12)V9(2).    
021112             15  TDB-TDA-ACTDI-PR-AMT         PIC S9(12)V9(2).    
021114             15  TDB-TDA-ACTDI-INT-AMT        PIC S9(12)V9(2).    
021116             15  TDB-TDA-ACTDI-WH-AMT         PIC S9(12)V9(2).    
021118             15  TDB-TDA-ACTDI-ST-AMT         PIC S9(12)V9(2).    
021120             15  TDB-TDA-ACTDI-DISP-CD        PIC 9(1).           
021122             15  TDB-TDA-ACTDI-T-ACCT         PIC 9(12).          
021124             15  TDB-TDA-ACTDI-T-ACCTS        PIC 9(10).          
021126             15  TDB-TDA-ACTDI-N-PRC-D        PIC 9(8).           
021128             15  FILLER                       PIC X(292).         
021130                                                                  
021132         10  TDB-TDA-NONDB-FIELDS.                                
021134             15  TDB-TDA-ACTV-NEW-SERIAL-X.                       
021136                 20  TDB-TDA-ACTV-NEW-SERIAL  PIC 9(12).          
021138                                                                  
021140     05  TDB-TDAINDXRT.                                           
021142         10  TDB-TDAIR-BANK-X.                                    
021144             15  TDB-TDAIR-BANK            PIC 9(4).              
021146         10  TDB-TDAIR-REGION-X.                                  
021148             15  TDB-TDAIR-REGION          PIC 9(2).              
021150         10  TDB-TDAIR-INDX-CD-X.                                 
021152             15  TDB-TDAIR-INDX-CD         PIC 9(2).              
021154         10  TDB-TDAIR-EFF-DATE-X.                                
021156             15  TDB-TDAIR-EFF-DATE        PIC 9(8).              
021158         10  TDB-TDAIR-END-DATE-X.                                
021160             15  TDB-TDAIR-END-DATE        PIC 9(8).              
021162         10  TDB-TDAIR-VOID-DATE-X.                               
021164             15  TDB-TDAIR-VOID-DATE       PIC 9(8).              
021166         10  TDB-TDAIR-ADD-DATE-X.                                
021168             15  TDB-TDAIR-ADD-DATE        PIC 9(8).              
021170         10  TDB-TDAIR-ADD-TIME-X.                                
021172             15  TDB-TDAIR-ADD-TIME        PIC 9(8).              
021174         10  TDB-TDAIR-PUB-ID              PIC X(8).              
021176         10  TDB-TDAIR-VOID-PUB-ID         PIC X(8).              
021178         10  TDB-TDAIR-DESC                PIC X(20).             
021180         10  TDB-TDAIR-RATE-X.                                    
021182             15  TDB-TDAIR-RATE            PIC S9(2)V9(3).        
021184                                                                  
021186     05  TDB-TDAMARGRT.                                           
021188         10  TDB-TDAMR-BANK-X.                                    
021190             15  TDB-TDAMR-BANK            PIC 9(4).              
021192         10  TDB-TDAMR-REGION-X.                                  
021194             15  TDB-TDAMR-REGION          PIC 9(2).              
021196         10  TDB-TDAMR-MARG-CD-X.                                 
021198             15  TDB-TDAMR-MARG-CD         PIC 9(2).              
021200         10  TDB-TDAMR-EFF-DATE-X.                                
021202             15  TDB-TDAMR-EFF-DATE        PIC 9(8).              
021204         10  TDB-TDAMR-END-DATE-X.                                
021206             15  TDB-TDAMR-END-DATE        PIC 9(8).              
021208         10  TDB-TDAMR-VOID-DATE-X.                               
021210             15  TDB-TDAMR-VOID-DATE       PIC 9(8).              
021212         10  TDB-TDAMR-ADD-DATE-X.                                
021214             15  TDB-TDAMR-ADD-DATE        PIC 9(8).              
021216         10  TDB-TDAMR-ADD-TIME-X.                                
021218             15  TDB-TDAMR-ADD-TIME        PIC 9(8).              
021220         10  TDB-TDAMR-PUB-ID              PIC X(8).              
021222         10  TDB-TDAMR-VOID-PUB-ID         PIC X(8).              
021224         10  TDB-TDAMR-DESC                PIC X(20).             
021226         10  TDB-TDAMR-RATE-X.                                    
021228             15  TDB-TDAMR-RATE            PIC S9(2)V9(3).        
021230                                                                  
021232     05  TDB-TDATIERRT.                                           
021234         10  TDB-TDATR-BANK-X.                                    
021236             15  TDB-TDATR-BANK            PIC 9(4).              
021238         10  TDB-TDATR-REGION-X.                                  
021240             15  TDB-TDATR-REGION          PIC 9(2).              
021242         10  TDB-TDATR-TIER-CD-X.                                 
021244             15  TDB-TDATR-TIER-CD         PIC 9(2).              
021246         10  TDB-TDATR-EFF-DATE-X.                                
021248             15  TDB-TDATR-EFF-DATE        PIC 9(8).              
021250         10  TDB-TDATR-END-DATE-X.                                
021252             15  TDB-TDATR-END-DATE        PIC 9(8).              
021254         10  TDB-TDATR-VOID-DATE-X.                               
021256             15  TDB-TDATR-VOID-DATE       PIC 9(8).              
021258         10  TDB-TDATR-ADD-DATE-X.                                
021260             15  TDB-TDATR-ADD-DATE        PIC 9(8).              
021262         10  TDB-TDATR-ADD-TIME-X.                                
021264             15  TDB-TDATR-ADD-TIME        PIC 9(8).              
021266         10  TDB-TDATR-PUB-ID              PIC X(8).              
021268         10  TDB-TDATR-VOID-PUB-ID         PIC X(8).              
021270         10  TDB-TDATR-DESC                PIC X(20).             
021272         10  TDB-TDATR-TIER-INCR1-X.                              
021274             15  TDB-TDATR-TIER-INCR1      PIC S9(2)V9(3).        
021276         10  TDB-TDATR-TIER-BAL1-X.                               
021278             15  TDB-TDATR-TIER-BAL1       PIC S9(12)V9(2).       
021280         10  TDB-TDATR-TIER-INCR2-X.                              
021282             15  TDB-TDATR-TIER-INCR2      PIC S9(2)V9(3).        
021284         10  TDB-TDATR-TIER-BAL2-X.                               
021286             15  TDB-TDATR-TIER-BAL2       PIC S9(12)V9(2).       
021288         10  TDB-TDATR-TIER-INCR3-X.                              
021290             15  TDB-TDATR-TIER-INCR3      PIC S9(2)V9(3).        
021292         10  TDB-TDATR-TIER-BAL3-X.                               
021294             15  TDB-TDATR-TIER-BAL3       PIC S9(12)V9(2).       
021296         10  TDB-TDATR-TIER-INCR4-X.                              
021298             15  TDB-TDATR-TIER-INCR4      PIC S9(2)V9(3).        
021300         10  TDB-TDATR-TIER-BAL4-X.                               
021302             15  TDB-TDATR-TIER-BAL4       PIC S9(12)V9(2).       
021304         10  TDB-TDATR-TIER-INCR5-X.                              
021306             15  TDB-TDATR-TIER-INCR5      PIC S9(2)V9(3).        
021308         10  TDB-TDATR-TIER-BAL5-X.                               
021310             15  TDB-TDATR-TIER-BAL5       PIC S9(12)V9(2).       
021312         10  TDB-TDATR-TIER-INCR6-X.                              
021314             15  TDB-TDATR-TIER-INCR6      PIC S9(2)V9(3).        
021316         10  TDB-TDATR-TIER-BAL6-X.                               
021318             15  TDB-TDATR-TIER-BAL6       PIC S9(12)V9(2).       
021320         10  TDB-TDATR-TIER-INCR7-X.                              
021322             15  TDB-TDATR-TIER-INCR7      PIC S9(2)V9(3).        
021324         10  TDB-TDATR-TIER-BAL7-X.                               
021326             15  TDB-TDATR-TIER-BAL7       PIC S9(12)V9(2).       
021328         10  TDB-TDATR-TIER-INCR8-X.                              
021330             15  TDB-TDATR-TIER-INCR8      PIC S9(2)V9(3).        
021332         10  TDB-TDATR-TIER-BAL8-X.                               
021334             15  TDB-TDATR-TIER-BAL8       PIC S9(12)V9(2).       
021336         10  TDB-TDATR-TIER-INCR9-X.                              
021338             15  TDB-TDATR-TIER-INCR9      PIC S9(2)V9(3).        
021340         10  TDB-TDATR-TIER-BAL9-X.                               
021342             15  TDB-TDATR-TIER-BAL9       PIC S9(12)V9(2).       
021344         10  TDB-TDATR-TIER-INCR10-X.                             
021346             15  TDB-TDATR-TIER-INCR10     PIC S9(2)V9(3).        
021348         10  TDB-TDATR-TIER-BAL10-X.                              
021350             15  TDB-TDATR-TIER-BAL10      PIC S9(12)V9(2).       
021352         10  TDB-TDATR-TIER-INCR11-X.                             
021354             15  TDB-TDATR-TIER-INCR11     PIC S9(2)V9(3).        
021356         10  TDB-TDATR-TIER-BAL11-X.                              
021358             15  TDB-TDATR-TIER-BAL11      PIC S9(12)V9(2).       
021360         10  TDB-TDATR-TIER-INCR12-X.                             
021362             15  TDB-TDATR-TIER-INCR12     PIC S9(2)V9(3).        
021364         10  TDB-TDATR-TIER-BAL12-X.                              
021366             15  TDB-TDATR-TIER-BAL12      PIC S9(12)V9(2).       
021368         10  TDB-TDATR-TIER-INCR13-X.                             
021370             15  TDB-TDATR-TIER-INCR13     PIC S9(2)V9(3).        
021372         10  TDB-TDATR-TIER-BAL13-X.                              
021374             15  TDB-TDATR-TIER-BAL13      PIC S9(12)V9(2).       
021376         10  TDB-TDATR-TIER-INCR14-X.                             
021378             15  TDB-TDATR-TIER-INCR14     PIC S9(2)V9(3).        
021380         10  TDB-TDATR-TIER-BAL14-X.                              
021382             15  TDB-TDATR-TIER-BAL14      PIC S9(12)V9(2).       
021384         10  TDB-TDATR-TIER-INCR15-X.                             
021386             15  TDB-TDATR-TIER-INCR15     PIC S9(2)V9(3).        
021388         10  TDB-TDATR-TIER-BAL15-X.                              
021390             15  TDB-TDATR-TIER-BAL15      PIC S9(12)V9(2).       
021392                                                                  
021394     05  TDB-TDARISERT.                                           
021396         10  TDB-TDARR-BANK-X.                                    
021398             15  TDB-TDARR-BANK            PIC 9(4).              
021400         10  TDB-TDARR-REGION-X.                                  
021402             15  TDB-TDARR-REGION          PIC 9(2).              
021404         10  TDB-TDARR-RISE-CD-X.                                 
021406             15  TDB-TDARR-RISE-CD         PIC 9(2).              
021408         10  TDB-TDARR-EFF-DATE-X.                                
021410             15  TDB-TDARR-EFF-DATE        PIC 9(8).              
021412         10  TDB-TDARR-END-DATE-X.                                
021414             15  TDB-TDARR-END-DATE        PIC 9(8).              
021416         10  TDB-TDARR-VOID-DATE-X.                               
021418             15  TDB-TDARR-VOID-DATE       PIC 9(8).              
021420         10  TDB-TDARR-ADD-DATE-X.                                
021422             15  TDB-TDARR-ADD-DATE        PIC 9(8).              
021424         10  TDB-TDARR-ADD-TIME-X.                                
021426             15  TDB-TDARR-ADD-TIME        PIC 9(8).              
021428         10  TDB-TDARR-PUB-ID              PIC X(8).              
021430         10  TDB-TDARR-VOID-PUB-ID         PIC X(8).              
021432         10  TDB-TDARR-DESC                PIC X(20).             
021434         10  TDB-TDARR-FRQ-TYPE-X.                                
021436             15  TDB-TDARR-FRQ-TYPE        PIC 9(1).              
021438         10  TDB-TDARR-CYC-FRQ1-X.                                
021440             15  TDB-TDARR-CYC-FRQ1        PIC 9(3).              
021442         10  TDB-TDARR-CYC-INC1-X.                                
021444             15  TDB-TDARR-CYC-INC1        PIC S9(2)V9(3).        
021446         10  TDB-TDARR-CYC-FRQ2-X.                                
021448             15  TDB-TDARR-CYC-FRQ2        PIC 9(3).              
021450         10  TDB-TDARR-CYC-INC2-X.                                
021452             15  TDB-TDARR-CYC-INC2        PIC S9(2)V9(3).        
021454         10  TDB-TDARR-CYC-FRQ3-X.                                
021456             15  TDB-TDARR-CYC-FRQ3        PIC 9(3).              
021458         10  TDB-TDARR-CYC-INC3-X.                                
021460             15  TDB-TDARR-CYC-INC3        PIC S9(2)V9(3).        
021462         10  TDB-TDARR-CYC-FRQ4-X.                                
021464             15  TDB-TDARR-CYC-FRQ4        PIC 9(3).              
021466         10  TDB-TDARR-CYC-INC4-X.                                
021468             15  TDB-TDARR-CYC-INC4        PIC S9(2)V9(3).        
021470         10  TDB-TDARR-CYC-FRQ5-X.                                
021472             15  TDB-TDARR-CYC-FRQ5        PIC 9(3).              
021474         10  TDB-TDARR-CYC-INC5-X.                                
021476             15  TDB-TDARR-CYC-INC5        PIC S9(2)V9(3).        
021478         10  TDB-TDARR-CYC-FRQ6-X.                                
021480             15  TDB-TDARR-CYC-FRQ6        PIC 9(3).              
021482         10  TDB-TDARR-CYC-INC6-X.                                
021484             15  TDB-TDARR-CYC-INC6        PIC S9(2)V9(3).        
021486         10  TDB-TDARR-CYC-FRQ7-X.                                
021488             15  TDB-TDARR-CYC-FRQ7        PIC 9(3).              
021490         10  TDB-TDARR-CYC-INC7-X.                                
021492             15  TDB-TDARR-CYC-INC7        PIC S9(2)V9(3).        
021494         10  TDB-TDARR-CYC-FRQ8-X.                                
021496             15  TDB-TDARR-CYC-FRQ8        PIC 9(3).              
021498         10  TDB-TDARR-CYC-INC8-X.                                
021500             15  TDB-TDARR-CYC-INC8        PIC S9(2)V9(3).        
021502         10  TDB-TDARR-CYC-FRQ9-X.                                
021504             15  TDB-TDARR-CYC-FRQ9        PIC 9(3).              
021506         10  TDB-TDARR-CYC-INC9-X.                                
021508             15  TDB-TDARR-CYC-INC9        PIC S9(2)V9(3).        
021510         10  TDB-TDARR-CYC-FRQ10-X.                               
021512             15  TDB-TDARR-CYC-FRQ10       PIC 9(3).              
021514         10  TDB-TDARR-CYC-INC10-X.                               
021516             15  TDB-TDARR-CYC-INC10       PIC S9(2)V9(3).        
021518                                                                  
021520     05  TDB-TDAHMS.                                              
021522         10  TDB-TDAHMS-BANK-X.                                   
021524             15  TDB-TDAHMS-BANK           PIC  9(4).             
021526         10  TDB-TDAHMS-APPL-X.                                   
021528             15  TDB-TDAHMS-APPL           PIC  9(1).             
021530         10  TDB-TDAHMS-CUST-X.                                   
021532             15  TDB-TDAHMS-CUST           PIC  9(12).            
021534         10  TDB-TDAHMS-ACCT-X.                                   
021536             15  TDB-TDAHMS-ACCT           PIC  9(10).            
021538         10  TDB-TDAHMS-TYPE-X.                                   
021540             15  TDB-TDAHMS-TYPE           PIC  X(1).             
021542         10  TDB-TDAHMS-BK-TYPE-X.                                
021544             15  TDB-TDAHMS-BK-TYPE        PIC  X(1).             
021546         10  TDB-TDAHMS-DR-CR-IND-X.                              
021548             15  TDB-TDAHMS-DR-CR-IND      PIC  X(1).             
021550         10  TDB-TDAHMS-SOURCE-X.                                 
021552             15  TDB-TDAHMS-SOURCE         PIC  9(2).             
021554         10  TDB-TDAHMS-HOLD-NBR-X.                               
021556             15  TDB-TDAHMS-HOLD-NBR       PIC  9(4).             
021558         10  TDB-TDAHMS-AMT-X.                                    
021560             15  TDB-TDAHMS-AMT            PIC S9(12)V99.         
021562         10  TDB-TDAHMS-ORIG-AMT-X.                               
021564             15  TDB-TDAHMS-ORIG-AMT       PIC  9(12)V99.         
021566         10  TDB-TDAHMS-COMMENT-X.                                
021568             15  TDB-TDAHMS-COMMENT        PIC  X(40).            
021570         10  TDB-TDAHMS-PUB-ID-X.                                 
021572             15  TDB-TDAHMS-PUB-ID         PIC  X(8).             
021574         10  TDB-TDAHMS-VOID-PUB-ID-X.                            
021576             15  TDB-TDAHMS-VD-PUB-ID      PIC  X(8).             
021578         10  TDB-TDAHMS-ADD-DATE-X.                               
021580             15  TDB-TDAHMS-ADD-DATE       PIC  9(8).             
021582         10  TDB-TDAHMS-ADD-TIME-X.                               
021584             15  TDB-TDAHMS-ADD-TIME       PIC  9(8).             
021586         10  TDB-TDAHMS-VOID-DATE-X.                              
021588             15  TDB-TDAHMS-VOID-DATE      PIC  9(8).             
021590         10  TDB-TDAHMS-PLG-ACCT-X.                               
021592             15  TDB-TDAHMS-PLG-ACCT       PIC  9(12).            
021594         10  TDB-TDAHMS-PLG-ACCT-S-X.                             
021596             15  TDB-TDAHMS-PLG-ACCT-S     PIC  9(10).            
021598         10  TDB-TDAHMS-EXPIRE-DT-X.                              
021600             15  TDB-TDAHMS-EXPIRE-DT      PIC  9(8).             
021602         10  TDB-TDAHMS-AVAIL-BAL-X.                              
021604             15  TDB-TDAHMS-AVAIL-BAL      PIC S9(12)V99.         
021606         10  TDB-TDAHMS-SERIAL-NUM-X.                             
021608             15  TDB-TDAHMS-SERIAL-NUM     PIC  9(10).            
021610         10  TDB-TDAHMS-END-SERIAL-X.                             
021612             15  TDB-TDAHMS-END-SERIAL     PIC  9(10).            
021614         10  TDB-TDAHMS-NAME-X.                                   
021616             15  TDB-TDAHMS-NAME           PIC  X(10).            
021618         10  TDB-TDAHMS-START-DATE-X.                             
021620             15  TDB-TDAHMS-START-DATE     PIC  9(8).             
021622         10  TDB-TDAHMS-DAILY-ACCR-X.                             
021624             15  TDB-TDAHMS-DAILY-ACCR     PIC S9(12)V9(6).       
021626         10  TDB-TDAHMS-ORG-ADD-DT         PIC  9(8).             
021628         10  TDB-TDAHMS-ORG-ADD-TM         PIC  9(8).             
021630         10  TDB-TDAHMS-ORG-PUB-ID         PIC  X(8).             
021632         10  TDB-TDAHMS-AMT-LAST-UPD       PIC S9(12)V9(2).       
021634         10  TDB-TDAHMS-DATE-LAST-UPD      PIC  9(8).             
021636                                                                  
021638     05  TDB-TDAREPORTS.                                          
021640         10  TDB-TDARPT-PRT-DT-X.                                 
021642             15  TDB-TDARPT-PRT-DT         PIC 9(8).              
021644         10  TDB-TDARPT-BANK-X.                                   
021646             15  TDB-TDARPT-BANK           PIC 9(4).              
021648         10  TDB-TDARPT-BRCH-X.                                   
021650             15  TDB-TDARPT-BRCH           PIC 9(4).              
021652         10  TDB-TDARPT-APPL-X.                                   
021654             15  TDB-TDARPT-APPL           PIC 9(1).              
021656         10  TDB-TDARPT-RPT-NBR-X.                                
021658             15  TDB-TDARPT-RPT-NBR        PIC 9(3).              
021660         10  TDB-TDARPT-ACCT-X.                                   
021662             15  TDB-TDARPT-ACCT           PIC 9(10).             
021664         10  TDB-TDARPT-CUST-R.                                   
021666             15  TDB-TDARPT-CUST           PIC 9(12).             
021668         10  TDB-TDARPT-EXP-DT-X.                                 
021670             15  TDB-TDARPT-EXP-DT         PIC 9(8).              
021672         10  TDB-TDARPT-REAS-X.                                   
021674             15  TDB-TDARPT-REAS           PIC 9(4).              
021676         10  TDB-TDARPT-REMARKS            PIC X(100).            
021678         10  TDB-TDARPT-REMARKS-NUMERIC REDEFINES                 
021680             TDB-TDARPT-REMARKS.                                  
021682             15  TDB-TDARPT-ACH-AMT        PIC 9(8)V99.           
021684             15  TDB-TDARPT-DR-CR          PIC X.                 
021686             15  TDB-TDARPT-SOURCE         PIC X.                 
021688             15  TDB-TDARPT-CHECK-NBR      PIC X(10).             
021690             15  TDB-TDARPT-DS-NBR         PIC 9(2).              
021692             15  TDB-TDARPT-AUTO-DIST      PIC X.                 
021694             15  TDB-TDARPT-EMAIL-IND      PIC 9(01).             
021696             15  TDB-TDARPT-DS-DISP-CD     PIC 9.                 
021698             15  TDB-TDARPT-DS-DISP-ACCT   PIC 9(12).             
021700             15  TDB-TDARPT-DS-DISP-ACCT-S PIC 9(10).             
021702             15  FILLER                    PIC X(51).             
021704         10  TDB-TDARPT-REMARKS-FM REDEFINES                      
```

⚠️  This is the source code you must document.
    302 lines from 10547 to 10848.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

