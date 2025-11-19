# LLM Request Debug File
Generated: 2025-11-18T18:11:40.752191

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 2/55
- **Model**: gpt-4.1
- **Chunk Number**: 2
- **Pass Number**: 3
- **Attempt Number**: 5 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,085 tokens
- **User Prompt**: ~9,182 tokens
- **Total Input**: ~11,267 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 2/55" (ID: detailed-code-explanation)

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


**CHUNK 2 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T18:05:37.383587", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 2 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 485 to 944 (460 lines)\nChunk Tokens (estimated): ~8,011\nActual Input Tokens: 9,417 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 485-944 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 2 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 2 of 55.\n\n\n=============================================================================\nCHUNK 2 SOURCE CODE (Lines 485-944)\n=============================================================================\n\n```cobol\n000978 01  SPEC-CARD-8-N.                                               \n000980     05  FILLER                          PIC X(07).               \n000982     05  SPEC-WATCHDOG-WIRE-N            PIC X(01).               \n000984     05  SPEC-NO-FREE-NP-RPT-N           PIC 9(03).               \n000986     05  SPEC-EXSTREAM-PRINT-N           PIC X(01).               \n000988     05  SPEC-EOY-STH-RPT-FICHE-N        PIC X(01).               \n000990     05  SPEC-EOY-1098-SUBST-N           PIC X(01).               \n000992     05  SPEC-EOY-INT-PD-NTC-FOLD-N      PIC X(01).               \n000994     05  SPEC-EOY-CLN-RPT-CODES-N.                                \n000996         10  SPEC-EOY-CLN-RPT-CODE-N     PIC 9(01)                \n000998                                         OCCURS 6 TIMES.          \n001000     05  SPEC-EOY-ESC-TRX-STMT-N         PIC X(01).               \n001002     05  SPEC-EOY-CLN-PAID-NTC-N         PIC X(01).               \n001004     05  SPEC-EOY-ESC-TRX-OVRR-N         PIC X(01).               \n001006     05  SPEC-EOY-ZERO-BAL-ESC-STMT-N    PIC X(01).               \n001008     05  SPEC-LNS-FAX-NO-N               PIC X(10).               \n001010     05  SPEC-ACH-CBK-RET-N              PIC 9(01).               \n001012     05  SPEC-BILL-EDIT-TEMPLATES-N      PIC 9(01).               \n001014     05  SPEC-INIT-PW-OPT-N              PIC 9(01).               \n001016     05  SPEC-ALERT-EVENT-BUS-TRAFFIC-N  PIC X(01).               \n001018     05  SPEC-FMS-DIVISION-N             PIC 9(01).               \n001020     05  SPEC-AUTO-NOC-N                 PIC 9(01).               \n001022     05  SPEC-BRANCH-LENGTH-N            PIC 9(01).               \n001024     05  SPEC-LOB-N                      PIC 9(01).               \n001026     05  SPEC-INIT-EMP-N                 PIC 9(01).               \n001028     05  SPEC-INIT-CO-N                  PIC 9(01).               \n001030     05  SPEC-MAX-PASSWORD-LENGTH-N      PIC 9(02).               \n001032     05  SPEC-MIN-PASSWORD-LENGTH-N      PIC 9(02).               \n001034     05  SPEC-SPECIAL-CHAR-FLAG-N        PIC 9(01).               \n001036     05  SPEC-EOY-CLN-INT-RPT-METHOD-N   PIC X(01).               \n001038     05  SPEC-EOY-CLN-FORMULA-CHG-N      PIC 9(02).               \n001040     05  SPEC-EOY-CLN-DLR-REB-ADD-N      PIC X(01).               \n001042     05  SPEC-EOY-INT-PD-NTC-SOLD-N      PIC X(01).               \n001044     05  SPEC-PEPS-N                     PIC X(01).               \n001046     05  SPEC-DIST-CAPT-N                PIC X(01).               \n001048     05  SPEC-SQL-CIF-DUMP-N             PIC X(01).               \n001050     05  SPEC-EV-3RD-PARTY-1-N           PIC X(01).               \n001052     05  SPEC-EV-3RD-PARTY-2-N           PIC X(01).               \n001054     05  SPEC-BANCVUE-N                  PIC X(01).               \n001056     05  SPEC-CIF-RELATIONSHIP-DUMP-N    PIC 9(01).               \n001058     05  SPEC-PROFITABILITY-PHASE-N      PIC 9(01).               \n001060     05  SPEC-ONE-DAY-HOLD-MP-N          PIC X(01).               \n001062     05  SPEC-FINCEN-OFAC-INCL-AUX-N     PIC 9(01).               \n001064     05  SPEC-HSA-LOCATION-N             PIC X(01).               \n001066     05  SPEC-RVC-STMT-PRT-CTL-N         PIC X(01).               \n001068     05  SPEC-AGENCY-ID-NO-N             PIC 9(10).               \n001070     05  SPEC-AGENCY-CODE-N              PIC 9(01).               \n001072     05  SPEC-1098-PRT-RE-TAX-N          PIC 9(01).               \n001074     05  SPEC-EOY-CRA-NTC-PRT-N          PIC X(01).               \n001076     05  SPEC-EOY-BAL-PRT-N              PIC X(01).               \n001078     05  FILLER-UNAVAIL-08               PIC X(01).               \n001080*\n001082 01  SPEC-CARD-9-N.                                               \n001084     05  FILLER                          PIC X(07).               \n001086     05  SPEC-NUPOINT-REPORTER-N         PIC X(01).               \n001088     05  SPEC-NO-PREV-PASS-N             PIC 9(02).               \n001090     05  SPEC-CLN-PD-AMT-N               PIC 9(05).               \n001092     05  SPEC-MLN-PD-AMT-N               PIC 9(05).               \n001094     05  SPEC-RVC-PD-AMT-N               PIC 9(05).               \n001096     05  SPEC-AFFIL-OVER-SPC-AMT-N       PIC 9(08).               \n001098     05  SPEC-AFFIL-BRD-RPT-N            PIC X(01).               \n001100     05  SPEC-BRD-RPT-LINE-CHANGE-N      PIC X(01).               \n001102     05  SPEC-BRD-RPT-PAST-DUES-N        PIC X(01).               \n001104     05  SPEC-BRD-RPT-DELINQUENCY-N      PIC X(01).               \n001106     05  SPEC-BRD-RPT-NEW-LOANS-N        PIC X(01).               \n001108     05  SPEC-BRD-RPT-NOTES-PAID-N       PIC X(01).               \n001110     05  SPEC-BRD-RPT-NEW-LNS-EMPLOYEEN  PIC X(01).               \n001112     05  SPEC-BRD-RPT-CHRG-OFF-LNS-N     PIC X(01).               \n001114     05  SPEC-BRD-RPT-CHRG-OFF-RECVR-N   PIC X(01).               \n001116     05  SPEC-BRD-RPT-NON-ACCRUING-N     PIC X(01).               \n001118     05  SPEC-BRD-RPT-OVER-SPEC-AMT-N    PIC X(01).               \n001120     05  SPEC-BRD-RPT-AFFILIATION-N      PIC X(01).               \n001122     05  SPEC-BRD-RPT-NEW-CLSD-BY-OFF-N  PIC X(01).               \n001124     05  SPEC-MSI-OV-CIF-DUMP-N          PIC 9(01).               \n001126     05  SPEC-MSI-OV-SDB-DATA-N          PIC 9(01).               \n001128     05  SPEC-CK21-DDA-N                 PIC X(01).               \n001130     05  SPEC-CK21-LNS-N                 PIC X(01).               \n001132     05  SPEC-CK21-TDA-N                 PIC X(01).               \n001134     05  SPEC-CK21-SDB-N                 PIC X(01).               \n001136     05  SPEC-CK21-RSV4-N                PIC X(01).               \n001138     05  SPEC-CK21-RSV1-N                PIC X(01).               \n001140     05  SPEC-CK21-RSV2-N                PIC X(01).               \n001142     05  SPEC-CK21-RSV3-N                PIC X(01).               \n001144     05  SPEC-MSI-OV-TDA-N               PIC 9(01).               \n001146     05  SPEC-MSI-OV-COD-N               PIC 9(01).               \n001148     05  SPEC-MSI-OV-IRA-N               PIC 9(01).               \n001150     05  SPEC-MSI-OV-DDA-N               PIC 9(01).               \n001152     05  SPEC-MSI-OV-LNS-N               PIC 9(01).               \n001154     05  SPEC-ENTC-LNS-N                 PIC X(01).               \n001156     05  SPEC-ENTC-TDA-N                 PIC X(01).               \n001158     05  SPEC-ENTC-DDA-N                 PIC X(01).               \n001160     05  SPEC-ENTC-NSF-N                 PIC X(01).               \n001162     05  SPEC-ENTC-SDB-N                 PIC X(01).               \n001164     05  SPEC-ENTC-TKL-N                 PIC X(01).               \n001166     05  SPEC-ENTC-CIF-N                 PIC X(01).               \n001168     05  SPEC-IMONITOR-N                 PIC X(01).               \n001170     05  SPEC-PRT-NEW-N                  PIC 9(01).               \n001172     05  SPEC-FLOAT-TBL-N                PIC X(01).               \n001174     05  SPEC-DL-TOTALS-MCR-N            PIC 9(01).               \n001176     05  SPEC-DL-TOTALS-COD-N            PIC 9(01).               \n001178     05  SPEC-DL-TOTALS-DDA-N            PIC 9(01).               \n001180     05  SPEC-DL-TOTALS-IRA-N            PIC 9(01).               \n001182     05  SPEC-DL-TOTALS-LNS-N            PIC 9(01).               \n001184     05  SPEC-NEW-TOTAL-OWED-N           PIC 9(05).               \n001186     05  FILLER-UNAVAIL-09               PIC X(01).               \n001188*\n001190 01  SPEC-CARD-10-N.                                              \n001192     05  FILLER                          PIC X(07).               \n001194     05  SPEC-FFIEC-CERT-N               PIC X(08).               \n001196     05  SPEC-SAV-NEW-AMT-N              PIC X(05).               \n001198     05  SPEC-SAV-NEW-AMT-R-N    REDEFINES                        \n001200                                 SPEC-SAV-NEW-AMT-N               \n001202                                         PIC 9(05).               \n001204     05  SPEC-FCTL-APPL-A17-N.                                    \n001206         10  SPEC-FCTL-DDA-A17-N         PIC 9(01).               \n001208         10  SPEC-FCTL-SAV-A17-N         PIC 9(01).               \n001210         10  SPEC-FCTL-COD-A17-N         PIC 9(01).               \n001212         10  SPEC-FCTL-IRA-A17-N         PIC 9(01).               \n001214         10  SPEC-FCTL-CLN-A17-N         PIC 9(01).               \n001216         10  SPEC-FCTL-ILN-A17-N         PIC 9(01).               \n001218         10  SPEC-FCTL-ONL-A17-N         PIC 9(01).               \n001220         10  SPEC-FCTL-MCR-A17-N         PIC 9(01).               \n001222         10  SPEC-FCTL-GNL-A17-N         PIC 9(01).               \n001224     05  SPEC-FCTL-APPL-A16-N.                                    \n001226         10  SPEC-FCTL-DDA-A16-N         PIC 9(01).               \n001228         10  SPEC-FCTL-SAV-A16-N         PIC 9(01).               \n001230         10  SPEC-FCTL-COD-A16-N         PIC 9(01).               \n001232         10  SPEC-FCTL-IRA-A16-N         PIC 9(01).               \n001234         10  SPEC-FCTL-CLN-A16-N         PIC 9(01).               \n001236         10  SPEC-FCTL-ILN-A16-N         PIC 9(01).               \n001238         10  SPEC-FCTL-ONL-A16-N         PIC 9(01).               \n001240         10  SPEC-FCTL-MCR-A16-N         PIC 9(01).               \n001242         10  SPEC-FCTL-GNL-A16-N         PIC 9(01).               \n001244     05  SPEC-PREMIER-NTCS-N.                                     \n001246         10  SPEC-PNTC-LNS-N             PIC 9(01).               \n001248         10  SPEC-PNTC-COD-N             PIC 9(01).               \n001250         10  SPEC-PNTC-IRA-N             PIC 9(01).               \n001252         10  SPEC-PNTC-DDA-N             PIC 9(01).               \n001254         10  SPEC-PNTC-TDA-N             PIC 9(01).               \n001256         10  SPEC-PNTC-SDB-N             PIC 9(01).               \n001258         10  SPEC-PNTC-TKL-N             PIC 9(01).               \n001260     05  SPEC-EOY-LNS-TKT-ARC-N          PIC X(01).               \n001262     05  SPEC-TRAINING-BANKS-N.                                   \n001264         10  SPEC-TRAIN-FREQ-N           PIC X(01).               \n001266         10  SPEC-TRAIN-BK-FLG-N         PIC X(01).               \n001268         10  SPEC-TRAIN-BK-NUM-N         PIC 9(04).               \n001270         10  SPEC-TRAIN-MM-DD-CPY-N      PIC X(04).               \n001272*    05  SPEC-DB-STATE-N OCCURS 5 TIMES                           \n001274*                            PIC X(02).                           \n001276     05  SPEC-METAGON-CONV-DATE-N        PIC 9(06).               \n001278     05  SPEC-TRN-DELETE-DATE-N          PIC 9(06).               \n001280     05  SPEC-TRAINING-RESERVE-N         PIC X(13).               \n001282*     05  SPEC-TRAINING-RESERVE-N         PIC X(19).              \n001284*    05  SPEC-DBD-CONTACT-N  PIC X(19).                           \n001286     05  FILLER-UNAVAIL-10               PIC X(01).               \n001288***************************************************************   \n001290***  SPECS/BANK/NEW PIC X(82) CONTAINS CARDS 11-16                \n001292***  Cards 11 - 16 are only available in DMS and 4 digit bank     \n001294***  number flat spec file.  Layouts for these are found in       \n001296***  510000-519999.                                               \n001298***************************************************************   \n001300*L                                                                \n001302*\n001304 01  SPEC-CARD-11.                                                \n001306     05  FILLER                       PIC X(07).                  \n001308     05  SPEC-1042-CONTACT            PIC X(45).                  \n001310     05  SPEC-IMG-RETEN-FREQ          PIC X(03).                  \n001312     05  FILLER                       PIC X(06).                  \n001314     05  SPEC-BR-ADDR-ON-FORM         PIC X(01).                  \n001316     05  SPEC-RETAIN-MEMO-POST        PIC X(01).                  \n001318     05  SPEC-EOY-LNS-INT-PD-PRINT    PIC X(01).                  \n001320     05  SPEC-EOY-3RD-PARTY           PIC X(01).                  \n001322     05  SPEC-EOY-TRUNCATE-SSN        PIC X(01).                  \n001324     05  SPEC-EOY-SUB-DOC-CLN         PIC X(01).                  \n001326     05  SPEC-EOY-SUB-DOC-MTG         PIC X(01).                  \n001328     05  SPEC-EOY-SUB-DOC-ILN         PIC X(01).                  \n001330     05  SPEC-EOY-SUB-DOC-RVC         PIC X(01).                  \n001332     05  SPEC-5498-SA-FORM            PIC X(01).                  \n001334     05  SPEC-1098-FORMS-PRINT        PIC X(01).                  \n001336     05  SPEC-DECONV-DATE             PIC 9(06).                  \n001338     05  SPEC-SEND-PMI-TO-EOY         PIC X(01).                  \n001340     05  SPEC-EOY-CIB-FILE-MERIDIAN   PIC X(01).                  \n001342     05  SPEC-CECL-FILE-FREQ          PIC X(01).                  \n001344     05  FILLER-UNAVAIL-11            PIC X(01).                  \n001346*\n001348 01  SPEC-CARD-12.                                                \n001350     05  FILLER                       PIC X(07).                  \n001352     05  SPEC-1042-CONTACT-TITLE      PIC X(45).                  \n001354     05  SPEC-MAILER-ID               PIC X(09).                  \n001356     05  SPEC-1099R-STATE-TAX-ID      PIC X(20).                  \n001358     05  FILLER-UNAVAIL-12            PIC X(01).                  \n001360*\n001362 01  SPEC-CARD-13.                                                \n001364     05  FILLER                       PIC X(07).                  \n001366     05  FILLER                       PIC X(01).                  \n001368     05  SPEC-DDA-STMT-HAND           PIC X(03).                  \n001370     05  SPEC-SAV-STMT-HAND           PIC X(03).                  \n001372     05  SPEC-APA-STMT-HAND           PIC X(03).                  \n001374     05  SPEC-IRA-STMT-HAND           PIC X(03).                  \n001376     05  SPEC-COD-STMT-HAND           PIC X(03).                  \n001378     05  SPEC-LNS-STMT-HAND           PIC X(03).                  \n001380     05  SPEC-LNS-SUB-1098-STMT-HAND  PIC X(03).                  \n001382     05  SPEC-RVC-STMT-HAND           PIC X(03).                  \n001384     05  SPEC-ESC-PAYOFF-STMT-HAND    PIC X(03).                  \n001386     05  SPEC-ESC-STMT-HAND           PIC X(03).                  \n001388     05  SPEC-LNS-DMND-BILL-STMT-HAND PIC X(03).                  \n001390     05  SPEC-LNS-DLR-STMT-HAND       PIC X(03).                  \n001392     05  SPEC-LNS-BILL-STMT-HAND      PIC X(03).                  \n001394     05  SPEC-LNS-CMB-BILL-STMT-HAND  PIC X(03).                  \n001396     05  SPEC-SAV-MAILERS-HAND        PIC X(03).                  \n001398     05  SPEC-LNS-MTG-PERIOD-STMT-HAND PIC X(03).                 \n001400     05  SPEC-FLP-STMT-HAND           PIC X(03).                  \n001402     05  SPEC-MCIF-PRIVACY-OPT-OUT    PIC 9(01).                  \n001404     05  SPEC-BK-DASHBOARD-BILL       PIC X(01).                  \n001406     05  FILLER                       PIC X(20).                  \n001408     05  FILLER-UNAVAIL-13            PIC X(01).                  \n001410*\n001412* FILE DESCRIPTION FOR PROC-FILE ( 73 BYTES )\n001414*\n001416 FD  PROC-FILE\n001418     VALUE OF TITLE IS \"PROC-FILE\"\n001420     VALUE OF FAMILYNAME IS \"GENERAL\"\n001422     VALUE OF DEPENDENTSPECS IS TRUE.\n001424*\n001426 01  PROC-REC.                                                    \n001428     05  PROC-BANK                PIC 9(04).                      \n001430     05  PROC-BEGIN-DT            PIC 9(08).                      \n001432     05  PROC-BEGIN-DT-RE REDEFINES PROC-BEGIN-DT.                \n001434         10  PROC-BEG-YEAR        PIC 9(04).                      \n001436         10  PROC-BEG-MONTH-DAY   PIC 9(04).                      \n001438     05  PROC-BEGIN-DT-R REDEFINES PROC-BEGIN-DT.                 \n001440         10  PROC-BEG-YEAR-CC     PIC 9(02).                      \n001442         10  PROC-BEG-YEAR-YY     PIC 9(02).                      \n001444         10  PROC-BEG-MM          PIC 9(02).                      \n001446         10  PROC-BEG-DD          PIC 9(02).                      \n001448     05  PROC-END-DT              PIC 9(08).                      \n001450     05  PROC-END-DT-RE REDEFINES PROC-END-DT.                    \n001452         10  PROC-END-YEAR        PIC 9(04).                      \n001454         10  PROC-END-MONTH-DAY   PIC 9(04).                      \n001456     05  PROC-END-DT-R REDEFINES PROC-END-DT.                     \n001458         10  PROC-END-YEAR-CC     PIC 9(02).                      \n001460         10  PROC-END-YEAR-YY     PIC 9(02).                      \n001462         10  PROC-END-MM          PIC 9(02).                      \n001464         10  PROC-END-DD          PIC 9(02).                      \n001466     05  PROC-LAST-DT             PIC 9(08).                      \n001468     05  PROC-LAST-DT-R REDEFINES PROC-LAST-DT.                   \n001470         10  PROC-LAST-YEAR-CC    PIC 9(02).                      \n001472         10  PROC-LAST-YEAR-YY    PIC 9(02).                      \n001474         10  PROC-LAST-MM         PIC 9(02).                      \n001476         10  PROC-LAST-DD         PIC 9(02).                      \n001478     05  PROC-MSG-IND             PIC X(01).                      \n001480     05  PROC-MSG                 PIC X(44).                      \n001482                                                                  \n001484*\n001486* FILE DESCRIPTION FOR DST-FILE-MAINT ( 85 BYTES )\n001488*\n001490 FD  DST-FILE-MAINT\n001492     VALUE OF TITLE IS \"DST-FILE-MAINT\"\n001494     VALUE OF FAMILYNAME IS \"RMT\"\n001496     VALUE OF FILENAME IS WS-DSTFM-ID\n001498     VALUE OF DEPENDENTSPECS IS \"TRUE\".\n001500*\n001502 01  MASS-FM-RECORD.                                              \n001504     05  FM-BANK                 PIC 9(04).                       \n001506     05  FM-CUST                 PIC 9(12).                       \n001508     05  FM-ACCT                 PIC 9(10).                       \n001510     05  FM-STRUCT               PIC 9(02).                       \n001512     05  FM-RECORD-NBR           PIC 9(02).                       \n001514     05  FM-TRANCODE             PIC 9(04).                       \n001516     05  FM-CHANGE-DATA          PIC X(40).                       \n001518     05  FM-APPLY                PIC X(01).                       \n001520     05  FM-ORIGIN               PIC X(08).                       \n001522     05  FM-INT                  PIC X(01).                       \n001524     05  FM-SYSTEM-USE           PIC X(01).                       \n001526                                                                  \n001528                                                                  \n001530*\n001532* FILE DESCRIPTION FOR CST-FILE-MAINT ( 85 BYTES )\n001534*\n001536 FD  CST-FILE-MAINT\n001538     VALUE OF TITLE IS \"CST-FILE-MAINT\"\n001540     VALUE OF FAMILYNAME IS \"RMT\"\n001542     VALUE OF FILENAME IS WS-CSTFM-ID\n001544     VALUE OF DEPENDENTSPECS IS \"TRUE\".\n001546*\n001548 01  MASS-FM-RECORD2.                                             \n001550     05  FM2-BANK                 PIC 9(04).                      \n001552     05  FM2-CUST                 PIC 9(12).                      \n001554     05  FM2-ACCT                 PIC 9(10).                      \n001556     05  FM2-STRUCT               PIC 9(02).                      \n001558     05  FM2-RECORD-NBR           PIC 9(02).                      \n001560     05  FM2-TRANCODE             PIC 9(04).                      \n001562     05  FM2-CHANGE-DATA          PIC X(40).                      \n001564     05  FM2-APPLY                PIC X(01).                      \n001566     05  FM2-ORIGIN               PIC X(08).                      \n001568     05  FM2-INT                  PIC X(01).                      \n001570     05  FM2-SYSTEM-USE           PIC X(01).                      \n001572                                                                  \n001574*\n001576*    FILE DESCRIPTION FOR REPORT LISTING.\n001578*\n001580 FD  LISTING\n001582     VALUE OF TITLE IS \"LISTING\"\n001584     VALUE OF FAMILYNAME IS \"GENERAL\"\n001586     VALUE OF FILENAME IS WS-LISTING-NAME\n001588     VALUE OF USERBACKUPNAME IS \"TRUE\"\n001590     VALUE OF PRINTDISPOSITION IS \"DONTPRINT\"\n001592     VALUE OF SAVEPRINTFILE IS \"TRUE\"\n001594     VALUE OF PRINTDISPOSITION IS \"CLOSE\".\n001596 01  Z-RPT-1-BUFFER                             PIC X(160).\n001598*\n001600*    FILE DESCRIPTION FOR REPORT FICHE.\n001602*\n001604 FD  FICHE\n001606     VALUE OF TITLE IS \"FICHE\"\n001608     VALUE OF FAMILYNAME IS \"GENERAL\"\n001610     VALUE OF FILENAME IS WS-FICHE-NAME\n001612     VALUE OF USERBACKUPNAME IS \"TRUE\"\n001614     VALUE OF PRINTDISPOSITION IS \"DONTPRINT\"\n001616     VALUE OF SAVEPRINTFILE IS \"TRUE\"\n001618     VALUE OF PRINTDISPOSITION IS \"CLOSE\".\n001620 01  Z-RPT-2-BUFFER                             PIC X(160).\n001622*\n001624 DATA-BASE SECTION.\n001626*--------- -------\n001628*\n001630 DB  LDBSPCDB =  SPCDB.\n001632 01  SPCPRT\n001634         USING SPCPRTALL,\n001636               SPCPRTCURR.\n001638 DB  LDBTDADB =  TDADB.\n001640 01  TDARESTART\n001642         USING NONE.\n001644 01  TDAACCT\n001646         USING TDAAMSET.\n001648 01  TDAREPORTS\n001650         USING NONE.\n001652 01  TDAPCR\n001654         USING TDAPCRSET.\n001656 01  TDACUST\n001658         USING TDACMSET,\n001660               TDATINSET.\n001662 01  TDAIRA\n001664         USING TDAIRASET.\n001666 01  TDADISTR\n001668         USING TDADSSET,\n001670               TDADSNBRSET.\n001672 01  TDAACTV\n001674         USING TDAACTVBKSET.\n001676*\n001678 WORKING-STORAGE SECTION.\n001680*--------------- -------\n001682 77  Z-TIME-GENERATED         PIC X(16) VALUE \"20240410173653\".\n001684*                                     FORMAT = CCYYMMDDZZUUSS\n001686 77  Z-FLAG                                     PIC 9.\n001688 77  Z-II                                       PIC S9(11) BINARY.\n001690 77  Z-LU                                       PIC S9(11) BINARY.\n001692 77  Z-JJ                                       PIC S9(11) BINARY.\n001694 77  Z-KK                                       PIC S9(11) BINARY.\n001696 77  Z-LL                                       PIC S9(11) BINARY.\n001698 77  Z-DISP-SIZE                                PIC S9(11) BINARY.\n001700 77  Z-RPT-NUM                                  PIC 99.\n001702 77  Z-SYSTEM-NAME                              PIC X(30)\n001704     VALUE \"TDAR\".\n001706 77  Z-PROGRAM-NAME                             PIC X(30)\n001708     VALUE \"MINDISTCALC\".\n001710 77  Z-I-1                                      PIC S9(11) BINARY.\n001712 77  Z-I-2                                      PIC S9(11) BINARY.\n001714 77  Z-TO-1                                     PIC S9(11) BINARY.\n001716 77  Z-TO-2                                     PIC S9(11) BINARY.\n001718 77  Z-TO-3                                     PIC S9(11) BINARY.\n001720 77  J                                          PIC S9(11) BINARY.\n001722 77  WS-SPECS-BANK-DATE           PIC 9(07) VALUE 0.              \n001724 77  WS-SPECS-BANK-TIME           PIC 9(12) VALUE 0.              \n001726 77  NO-LINES                        PIC 9(02)   BINARY EXTENDED. \n001728 77  LINE-CTR                        PIC 9(04)   BINARY EXTENDED  \n001730                                                 VALUE 0.         \n001732 77  PAGE-CTR                        PIC 9(04)   BINARY EXTENDED  \n001734                                                 VALUE 0.         \n001736 77  END-PAGE                        PIC 9(04)   BINARY EXTENDED  \n001738                                                 VALUE 58.        \n001740 77  HDR-CTL                         PIC 9(01)   BINARY EXTENDED  \n001742                                                 VALUE 0.         \n001744 77  GWS-TP-CTL                      PIC 9(01) VALUE 0.           \n001746 77  TP-LN-CHAR                      PIC 9(02) VALUE 0.           \n001748 77  Z-LINT-1                                   PIC S9(11) BINARY.\n001750 77  Z-LINT-2                                   PIC S9(11) BINARY.\n001752 01  Z-LALPHA-1                                 PIC X(256).\n001754 01  Z-LALPHA-2                                 PIC X(256).\n001756 01  Z-LALPHA-3                                 PIC X(256).\n001758 77  Z-GINT-1 PIC S9(11) BINARY.\n001760 01  Z-GALPHA-1                                 PIC X(41).\n001762 77  Z-STR-INT-ZERO                             PIC S9(11) BINARY \n001764     VALUE 0.\n001766 77  Z-STR-INT-ONE                              PIC S9(11) BINARY \n001768     VALUE 1.\n001770 77  Z-STR-INT-DEFAULT                          PIC S9(11) BINARY \n001772     VALUE -1024.\n001774 77  Z-STR-INT-MAXSZ                            PIC S9(11) BINARY \n001776     VALUE 41.\n001778 01  Z-STR-ALPHA-SPACE                          PIC X VALUE SPACE.\n001780 01  Z-STR-ALPHA-ZERO                           PIC X VALUE ZERO.\n001782 01  Z-STR-ALPHA-HIGH-VALUE                     PIC X VALUE       \n001784     HIGH-VALUE.\n001786 01  Z-STR-ALPHA-LOW-VALUE                      PIC X VALUE       \n001788     LOW-VALUE.\n001790 01  Z-STR-ALPHA-QUOTE                          PIC X VALUE QUOTE.\n001792 01  Z-GSTRNUM-1.\n001794     05  Z-GSTRNUM-1-9                          PIC 9.\n001796 01  Z-GSTRNUM-2.\n001798     05  Z-GSTRNUM-2-9                          PIC 9.\n001800*\n001802****** FLAGS AREA ******\n001804 01  Z-FLAGS-AREA.\n001806     05  Z-FOUND-FLAG                           PIC 9.\n001808         88  Z-NOT-FOUND                          VALUE 0.\n001810         88  Z-FOUND                              VALUE 1.\n001812     05  Z-EDIT-ERROR-FLAG                      PIC 9.\n001814         88  Z-NO-EDIT-ERROR                      VALUE 0.\n001816         88  Z-EDIT-ERROR                         VALUE 1.\n001818     05  Z-EDIT-FIRSTERROR-FLAG                 PIC 9.\n001820         88  Z-EDIT-FIRSTERROR                    VALUE 0.\n001822     05  Z-EDIT-LASTERROR-FLAG                  PIC 9.\n001824         88  Z-NO-EDIT-LASTERROR                  VALUE 0.\n001826         88  Z-EDIT-LASTERROR                     VALUE 1.\n001828     05  Z-SIZE-ERROR-FLAG                      PIC 9.\n001830         88  Z-NO-SIZE-ERROR                      VALUE 0.\n001832         88  Z-SIZE-ERROR                         VALUE 1.\n001834     05  Z-FINISH-FLAG                          PIC 9.\n001836         88  Z-NOT-FINISHED                       VALUE 0.\n001838         88  Z-FINISHED                           VALUE 1.\n001840     05  Z-CONTINUE-FLAG                        PIC 9.\n001842         88  Z-NOT-CONTINUED                      VALUE 0.\n001844         88  Z-CONTINUED                          VALUE 1.\n001846         88  Z-REPROCESS                          VALUE 2.\n001848     05  Z-PROCESS-FLAG                         PIC 9.\n001850         88  Z-NO-PROCESS                         VALUE 0.\n001852         88  Z-PROCESS                            VALUE 1.\n001854     05  Z-EXIT-CODE                            PIC 9.\n001856         88  Z-EXIT-NORM                          VALUE 0.\n001858         88  Z-EXIT-NO-LABEL                      VALUE 1.\n001860         88  Z-EXIT-LABEL                         VALUE 2.\n001862         88  Z-EXIT-ALL                           VALUE 3.\n001864         88  Z-EXIT-EDITEXIT                      VALUE 4.\n001866         88  Z-EXIT-PROCESS                       VALUE 5.\n001868     05  Z-EXIT-LEVEL                           PIC S9(6).\n001870         88  Z-EXIT-ALL-LEVELS                    VALUE -1.\n001872     05  Z-EXIT-PROCEDURE-LABEL                 PIC X(30).\n001874     05  Z-EXIT-PERFORM-LABEL                   PIC X(30).\n001876     05  Z-LAST-KEY-PROC                        PIC 9.\n001878         88  Z-GET-LAST-KEY                       VALUE 0.\n001880         88  Z-DEL-LAST-KEY                       VALUE 1.\n001882         88  Z-UPDATE-LAST-KEY                    VALUE 2.\n001884     05  Z-DMS-ABORT-FLAG                       PIC 9.\n001886         88  Z-DMS-ABORT-OK                       VALUE 0.\n001888         88  Z-DMS-ABORT-SKIP                     VALUE 1.\n001890     05  Z-EDIT-NO-MSG                          PIC 9.\n001892     05  Z-EDIT-DEFAULT-SEEN                    PIC 9.\n001894*\n001896****** SAVE/RESTART AREA ******\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    460 lines from 485 to 944.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 2, "total_chunks": 55, "start_line": 485, "end_line": 944, "line_count": 460}

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
- Source code length: 33539 characters

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
CHUNK 2 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 485 to 944 (460 lines)
Chunk Tokens (estimated): ~8,011
Actual Input Tokens: 9,417 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 485-944 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 2 of 55 chunks
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
      The source code below is only CHUNK 2 of 55.


=============================================================================
CHUNK 2 SOURCE CODE (Lines 485-944)
=============================================================================

```cobol
000978 01  SPEC-CARD-8-N.                                               
000980     05  FILLER                          PIC X(07).               
000982     05  SPEC-WATCHDOG-WIRE-N            PIC X(01).               
000984     05  SPEC-NO-FREE-NP-RPT-N           PIC 9(03).               
000986     05  SPEC-EXSTREAM-PRINT-N           PIC X(01).               
000988     05  SPEC-EOY-STH-RPT-FICHE-N        PIC X(01).               
000990     05  SPEC-EOY-1098-SUBST-N           PIC X(01).               
000992     05  SPEC-EOY-INT-PD-NTC-FOLD-N      PIC X(01).               
000994     05  SPEC-EOY-CLN-RPT-CODES-N.                                
000996         10  SPEC-EOY-CLN-RPT-CODE-N     PIC 9(01)                
000998                                         OCCURS 6 TIMES.          
001000     05  SPEC-EOY-ESC-TRX-STMT-N         PIC X(01).               
001002     05  SPEC-EOY-CLN-PAID-NTC-N         PIC X(01).               
001004     05  SPEC-EOY-ESC-TRX-OVRR-N         PIC X(01).               
001006     05  SPEC-EOY-ZERO-BAL-ESC-STMT-N    PIC X(01).               
001008     05  SPEC-LNS-FAX-NO-N               PIC X(10).               
001010     05  SPEC-ACH-CBK-RET-N              PIC 9(01).               
001012     05  SPEC-BILL-EDIT-TEMPLATES-N      PIC 9(01).               
001014     05  SPEC-INIT-PW-OPT-N              PIC 9(01).               
001016     05  SPEC-ALERT-EVENT-BUS-TRAFFIC-N  PIC X(01).               
001018     05  SPEC-FMS-DIVISION-N             PIC 9(01).               
001020     05  SPEC-AUTO-NOC-N                 PIC 9(01).               
001022     05  SPEC-BRANCH-LENGTH-N            PIC 9(01).               
001024     05  SPEC-LOB-N                      PIC 9(01).               
001026     05  SPEC-INIT-EMP-N                 PIC 9(01).               
001028     05  SPEC-INIT-CO-N                  PIC 9(01).               
001030     05  SPEC-MAX-PASSWORD-LENGTH-N      PIC 9(02).               
001032     05  SPEC-MIN-PASSWORD-LENGTH-N      PIC 9(02).               
001034     05  SPEC-SPECIAL-CHAR-FLAG-N        PIC 9(01).               
001036     05  SPEC-EOY-CLN-INT-RPT-METHOD-N   PIC X(01).               
001038     05  SPEC-EOY-CLN-FORMULA-CHG-N      PIC 9(02).               
001040     05  SPEC-EOY-CLN-DLR-REB-ADD-N      PIC X(01).               
001042     05  SPEC-EOY-INT-PD-NTC-SOLD-N      PIC X(01).               
001044     05  SPEC-PEPS-N                     PIC X(01).               
001046     05  SPEC-DIST-CAPT-N                PIC X(01).               
001048     05  SPEC-SQL-CIF-DUMP-N             PIC X(01).               
001050     05  SPEC-EV-3RD-PARTY-1-N           PIC X(01).               
001052     05  SPEC-EV-3RD-PARTY-2-N           PIC X(01).               
001054     05  SPEC-BANCVUE-N                  PIC X(01).               
001056     05  SPEC-CIF-RELATIONSHIP-DUMP-N    PIC 9(01).               
001058     05  SPEC-PROFITABILITY-PHASE-N      PIC 9(01).               
001060     05  SPEC-ONE-DAY-HOLD-MP-N          PIC X(01).               
001062     05  SPEC-FINCEN-OFAC-INCL-AUX-N     PIC 9(01).               
001064     05  SPEC-HSA-LOCATION-N             PIC X(01).               
001066     05  SPEC-RVC-STMT-PRT-CTL-N         PIC X(01).               
001068     05  SPEC-AGENCY-ID-NO-N             PIC 9(10).               
001070     05  SPEC-AGENCY-CODE-N              PIC 9(01).               
001072     05  SPEC-1098-PRT-RE-TAX-N          PIC 9(01).               
001074     05  SPEC-EOY-CRA-NTC-PRT-N          PIC X(01).               
001076     05  SPEC-EOY-BAL-PRT-N              PIC X(01).               
001078     05  FILLER-UNAVAIL-08               PIC X(01).               
001080*
001082 01  SPEC-CARD-9-N.                                               
001084     05  FILLER                          PIC X(07).               
001086     05  SPEC-NUPOINT-REPORTER-N         PIC X(01).               
001088     05  SPEC-NO-PREV-PASS-N             PIC 9(02).               
001090     05  SPEC-CLN-PD-AMT-N               PIC 9(05).               
001092     05  SPEC-MLN-PD-AMT-N               PIC 9(05).               
001094     05  SPEC-RVC-PD-AMT-N               PIC 9(05).               
001096     05  SPEC-AFFIL-OVER-SPC-AMT-N       PIC 9(08).               
001098     05  SPEC-AFFIL-BRD-RPT-N            PIC X(01).               
001100     05  SPEC-BRD-RPT-LINE-CHANGE-N      PIC X(01).               
001102     05  SPEC-BRD-RPT-PAST-DUES-N        PIC X(01).               
001104     05  SPEC-BRD-RPT-DELINQUENCY-N      PIC X(01).               
001106     05  SPEC-BRD-RPT-NEW-LOANS-N        PIC X(01).               
001108     05  SPEC-BRD-RPT-NOTES-PAID-N       PIC X(01).               
001110     05  SPEC-BRD-RPT-NEW-LNS-EMPLOYEEN  PIC X(01).               
001112     05  SPEC-BRD-RPT-CHRG-OFF-LNS-N     PIC X(01).               
001114     05  SPEC-BRD-RPT-CHRG-OFF-RECVR-N   PIC X(01).               
001116     05  SPEC-BRD-RPT-NON-ACCRUING-N     PIC X(01).               
001118     05  SPEC-BRD-RPT-OVER-SPEC-AMT-N    PIC X(01).               
001120     05  SPEC-BRD-RPT-AFFILIATION-N      PIC X(01).               
001122     05  SPEC-BRD-RPT-NEW-CLSD-BY-OFF-N  PIC X(01).               
001124     05  SPEC-MSI-OV-CIF-DUMP-N          PIC 9(01).               
001126     05  SPEC-MSI-OV-SDB-DATA-N          PIC 9(01).               
001128     05  SPEC-CK21-DDA-N                 PIC X(01).               
001130     05  SPEC-CK21-LNS-N                 PIC X(01).               
001132     05  SPEC-CK21-TDA-N                 PIC X(01).               
001134     05  SPEC-CK21-SDB-N                 PIC X(01).               
001136     05  SPEC-CK21-RSV4-N                PIC X(01).               
001138     05  SPEC-CK21-RSV1-N                PIC X(01).               
001140     05  SPEC-CK21-RSV2-N                PIC X(01).               
001142     05  SPEC-CK21-RSV3-N                PIC X(01).               
001144     05  SPEC-MSI-OV-TDA-N               PIC 9(01).               
001146     05  SPEC-MSI-OV-COD-N               PIC 9(01).               
001148     05  SPEC-MSI-OV-IRA-N               PIC 9(01).               
001150     05  SPEC-MSI-OV-DDA-N               PIC 9(01).               
001152     05  SPEC-MSI-OV-LNS-N               PIC 9(01).               
001154     05  SPEC-ENTC-LNS-N                 PIC X(01).               
001156     05  SPEC-ENTC-TDA-N                 PIC X(01).               
001158     05  SPEC-ENTC-DDA-N                 PIC X(01).               
001160     05  SPEC-ENTC-NSF-N                 PIC X(01).               
001162     05  SPEC-ENTC-SDB-N                 PIC X(01).               
001164     05  SPEC-ENTC-TKL-N                 PIC X(01).               
001166     05  SPEC-ENTC-CIF-N                 PIC X(01).               
001168     05  SPEC-IMONITOR-N                 PIC X(01).               
001170     05  SPEC-PRT-NEW-N                  PIC 9(01).               
001172     05  SPEC-FLOAT-TBL-N                PIC X(01).               
001174     05  SPEC-DL-TOTALS-MCR-N            PIC 9(01).               
001176     05  SPEC-DL-TOTALS-COD-N            PIC 9(01).               
001178     05  SPEC-DL-TOTALS-DDA-N            PIC 9(01).               
001180     05  SPEC-DL-TOTALS-IRA-N            PIC 9(01).               
001182     05  SPEC-DL-TOTALS-LNS-N            PIC 9(01).               
001184     05  SPEC-NEW-TOTAL-OWED-N           PIC 9(05).               
001186     05  FILLER-UNAVAIL-09               PIC X(01).               
001188*
001190 01  SPEC-CARD-10-N.                                              
001192     05  FILLER                          PIC X(07).               
001194     05  SPEC-FFIEC-CERT-N               PIC X(08).               
001196     05  SPEC-SAV-NEW-AMT-N              PIC X(05).               
001198     05  SPEC-SAV-NEW-AMT-R-N    REDEFINES                        
001200                                 SPEC-SAV-NEW-AMT-N               
001202                                         PIC 9(05).               
001204     05  SPEC-FCTL-APPL-A17-N.                                    
001206         10  SPEC-FCTL-DDA-A17-N         PIC 9(01).               
001208         10  SPEC-FCTL-SAV-A17-N         PIC 9(01).               
001210         10  SPEC-FCTL-COD-A17-N         PIC 9(01).               
001212         10  SPEC-FCTL-IRA-A17-N         PIC 9(01).               
001214         10  SPEC-FCTL-CLN-A17-N         PIC 9(01).               
001216         10  SPEC-FCTL-ILN-A17-N         PIC 9(01).               
001218         10  SPEC-FCTL-ONL-A17-N         PIC 9(01).               
001220         10  SPEC-FCTL-MCR-A17-N         PIC 9(01).               
001222         10  SPEC-FCTL-GNL-A17-N         PIC 9(01).               
001224     05  SPEC-FCTL-APPL-A16-N.                                    
001226         10  SPEC-FCTL-DDA-A16-N         PIC 9(01).               
001228         10  SPEC-FCTL-SAV-A16-N         PIC 9(01).               
001230         10  SPEC-FCTL-COD-A16-N         PIC 9(01).               
001232         10  SPEC-FCTL-IRA-A16-N         PIC 9(01).               
001234         10  SPEC-FCTL-CLN-A16-N         PIC 9(01).               
001236         10  SPEC-FCTL-ILN-A16-N         PIC 9(01).               
001238         10  SPEC-FCTL-ONL-A16-N         PIC 9(01).               
001240         10  SPEC-FCTL-MCR-A16-N         PIC 9(01).               
001242         10  SPEC-FCTL-GNL-A16-N         PIC 9(01).               
001244     05  SPEC-PREMIER-NTCS-N.                                     
001246         10  SPEC-PNTC-LNS-N             PIC 9(01).               
001248         10  SPEC-PNTC-COD-N             PIC 9(01).               
001250         10  SPEC-PNTC-IRA-N             PIC 9(01).               
001252         10  SPEC-PNTC-DDA-N             PIC 9(01).               
001254         10  SPEC-PNTC-TDA-N             PIC 9(01).               
001256         10  SPEC-PNTC-SDB-N             PIC 9(01).               
001258         10  SPEC-PNTC-TKL-N             PIC 9(01).               
001260     05  SPEC-EOY-LNS-TKT-ARC-N          PIC X(01).               
001262     05  SPEC-TRAINING-BANKS-N.                                   
001264         10  SPEC-TRAIN-FREQ-N           PIC X(01).               
001266         10  SPEC-TRAIN-BK-FLG-N         PIC X(01).               
001268         10  SPEC-TRAIN-BK-NUM-N         PIC 9(04).               
001270         10  SPEC-TRAIN-MM-DD-CPY-N      PIC X(04).               
001272*    05  SPEC-DB-STATE-N OCCURS 5 TIMES                           
001274*                            PIC X(02).                           
001276     05  SPEC-METAGON-CONV-DATE-N        PIC 9(06).               
001278     05  SPEC-TRN-DELETE-DATE-N          PIC 9(06).               
001280     05  SPEC-TRAINING-RESERVE-N         PIC X(13).               
001282*     05  SPEC-TRAINING-RESERVE-N         PIC X(19).              
001284*    05  SPEC-DBD-CONTACT-N  PIC X(19).                           
001286     05  FILLER-UNAVAIL-10               PIC X(01).               
001288***************************************************************   
001290***  SPECS/BANK/NEW PIC X(82) CONTAINS CARDS 11-16                
001292***  Cards 11 - 16 are only available in DMS and 4 digit bank     
001294***  number flat spec file.  Layouts for these are found in       
001296***  510000-519999.                                               
001298***************************************************************   
001300*L                                                                
001302*
001304 01  SPEC-CARD-11.                                                
001306     05  FILLER                       PIC X(07).                  
001308     05  SPEC-1042-CONTACT            PIC X(45).                  
001310     05  SPEC-IMG-RETEN-FREQ          PIC X(03).                  
001312     05  FILLER                       PIC X(06).                  
001314     05  SPEC-BR-ADDR-ON-FORM         PIC X(01).                  
001316     05  SPEC-RETAIN-MEMO-POST        PIC X(01).                  
001318     05  SPEC-EOY-LNS-INT-PD-PRINT    PIC X(01).                  
001320     05  SPEC-EOY-3RD-PARTY           PIC X(01).                  
001322     05  SPEC-EOY-TRUNCATE-SSN        PIC X(01).                  
001324     05  SPEC-EOY-SUB-DOC-CLN         PIC X(01).                  
001326     05  SPEC-EOY-SUB-DOC-MTG         PIC X(01).                  
001328     05  SPEC-EOY-SUB-DOC-ILN         PIC X(01).                  
001330     05  SPEC-EOY-SUB-DOC-RVC         PIC X(01).                  
001332     05  SPEC-5498-SA-FORM            PIC X(01).                  
001334     05  SPEC-1098-FORMS-PRINT        PIC X(01).                  
001336     05  SPEC-DECONV-DATE             PIC 9(06).                  
001338     05  SPEC-SEND-PMI-TO-EOY         PIC X(01).                  
001340     05  SPEC-EOY-CIB-FILE-MERIDIAN   PIC X(01).                  
001342     05  SPEC-CECL-FILE-FREQ          PIC X(01).                  
001344     05  FILLER-UNAVAIL-11            PIC X(01).                  
001346*
001348 01  SPEC-CARD-12.                                                
001350     05  FILLER                       PIC X(07).                  
001352     05  SPEC-1042-CONTACT-TITLE      PIC X(45).                  
001354     05  SPEC-MAILER-ID               PIC X(09).                  
001356     05  SPEC-1099R-STATE-TAX-ID      PIC X(20).                  
001358     05  FILLER-UNAVAIL-12            PIC X(01).                  
001360*
001362 01  SPEC-CARD-13.                                                
001364     05  FILLER                       PIC X(07).                  
001366     05  FILLER                       PIC X(01).                  
001368     05  SPEC-DDA-STMT-HAND           PIC X(03).                  
001370     05  SPEC-SAV-STMT-HAND           PIC X(03).                  
001372     05  SPEC-APA-STMT-HAND           PIC X(03).                  
001374     05  SPEC-IRA-STMT-HAND           PIC X(03).                  
001376     05  SPEC-COD-STMT-HAND           PIC X(03).                  
001378     05  SPEC-LNS-STMT-HAND           PIC X(03).                  
001380     05  SPEC-LNS-SUB-1098-STMT-HAND  PIC X(03).                  
001382     05  SPEC-RVC-STMT-HAND           PIC X(03).                  
001384     05  SPEC-ESC-PAYOFF-STMT-HAND    PIC X(03).                  
001386     05  SPEC-ESC-STMT-HAND           PIC X(03).                  
001388     05  SPEC-LNS-DMND-BILL-STMT-HAND PIC X(03).                  
001390     05  SPEC-LNS-DLR-STMT-HAND       PIC X(03).                  
001392     05  SPEC-LNS-BILL-STMT-HAND      PIC X(03).                  
001394     05  SPEC-LNS-CMB-BILL-STMT-HAND  PIC X(03).                  
001396     05  SPEC-SAV-MAILERS-HAND        PIC X(03).                  
001398     05  SPEC-LNS-MTG-PERIOD-STMT-HAND PIC X(03).                 
001400     05  SPEC-FLP-STMT-HAND           PIC X(03).                  
001402     05  SPEC-MCIF-PRIVACY-OPT-OUT    PIC 9(01).                  
001404     05  SPEC-BK-DASHBOARD-BILL       PIC X(01).                  
001406     05  FILLER                       PIC X(20).                  
001408     05  FILLER-UNAVAIL-13            PIC X(01).                  
001410*
001412* FILE DESCRIPTION FOR PROC-FILE ( 73 BYTES )
001414*
001416 FD  PROC-FILE
001418     VALUE OF TITLE IS "PROC-FILE"
001420     VALUE OF FAMILYNAME IS "GENERAL"
001422     VALUE OF DEPENDENTSPECS IS TRUE.
001424*
001426 01  PROC-REC.                                                    
001428     05  PROC-BANK                PIC 9(04).                      
001430     05  PROC-BEGIN-DT            PIC 9(08).                      
001432     05  PROC-BEGIN-DT-RE REDEFINES PROC-BEGIN-DT.                
001434         10  PROC-BEG-YEAR        PIC 9(04).                      
001436         10  PROC-BEG-MONTH-DAY   PIC 9(04).                      
001438     05  PROC-BEGIN-DT-R REDEFINES PROC-BEGIN-DT.                 
001440         10  PROC-BEG-YEAR-CC     PIC 9(02).                      
001442         10  PROC-BEG-YEAR-YY     PIC 9(02).                      
001444         10  PROC-BEG-MM          PIC 9(02).                      
001446         10  PROC-BEG-DD          PIC 9(02).                      
001448     05  PROC-END-DT              PIC 9(08).                      
001450     05  PROC-END-DT-RE REDEFINES PROC-END-DT.                    
001452         10  PROC-END-YEAR        PIC 9(04).                      
001454         10  PROC-END-MONTH-DAY   PIC 9(04).                      
001456     05  PROC-END-DT-R REDEFINES PROC-END-DT.                     
001458         10  PROC-END-YEAR-CC     PIC 9(02).                      
001460         10  PROC-END-YEAR-YY     PIC 9(02).                      
001462         10  PROC-END-MM          PIC 9(02).                      
001464         10  PROC-END-DD          PIC 9(02).                      
001466     05  PROC-LAST-DT             PIC 9(08).                      
001468     05  PROC-LAST-DT-R REDEFINES PROC-LAST-DT.                   
001470         10  PROC-LAST-YEAR-CC    PIC 9(02).                      
001472         10  PROC-LAST-YEAR-YY    PIC 9(02).                      
001474         10  PROC-LAST-MM         PIC 9(02).                      
001476         10  PROC-LAST-DD         PIC 9(02).                      
001478     05  PROC-MSG-IND             PIC X(01).                      
001480     05  PROC-MSG                 PIC X(44).                      
001482                                                                  
001484*
001486* FILE DESCRIPTION FOR DST-FILE-MAINT ( 85 BYTES )
001488*
001490 FD  DST-FILE-MAINT
001492     VALUE OF TITLE IS "DST-FILE-MAINT"
001494     VALUE OF FAMILYNAME IS "RMT"
001496     VALUE OF FILENAME IS WS-DSTFM-ID
001498     VALUE OF DEPENDENTSPECS IS "TRUE".
001500*
001502 01  MASS-FM-RECORD.                                              
001504     05  FM-BANK                 PIC 9(04).                       
001506     05  FM-CUST                 PIC 9(12).                       
001508     05  FM-ACCT                 PIC 9(10).                       
001510     05  FM-STRUCT               PIC 9(02).                       
001512     05  FM-RECORD-NBR           PIC 9(02).                       
001514     05  FM-TRANCODE             PIC 9(04).                       
001516     05  FM-CHANGE-DATA          PIC X(40).                       
001518     05  FM-APPLY                PIC X(01).                       
001520     05  FM-ORIGIN               PIC X(08).                       
001522     05  FM-INT                  PIC X(01).                       
001524     05  FM-SYSTEM-USE           PIC X(01).                       
001526                                                                  
001528                                                                  
001530*
001532* FILE DESCRIPTION FOR CST-FILE-MAINT ( 85 BYTES )
001534*
001536 FD  CST-FILE-MAINT
001538     VALUE OF TITLE IS "CST-FILE-MAINT"
001540     VALUE OF FAMILYNAME IS "RMT"
001542     VALUE OF FILENAME IS WS-CSTFM-ID
001544     VALUE OF DEPENDENTSPECS IS "TRUE".
001546*
001548 01  MASS-FM-RECORD2.                                             
001550     05  FM2-BANK                 PIC 9(04).                      
001552     05  FM2-CUST                 PIC 9(12).                      
001554     05  FM2-ACCT                 PIC 9(10).                      
001556     05  FM2-STRUCT               PIC 9(02).                      
001558     05  FM2-RECORD-NBR           PIC 9(02).                      
001560     05  FM2-TRANCODE             PIC 9(04).                      
001562     05  FM2-CHANGE-DATA          PIC X(40).                      
001564     05  FM2-APPLY                PIC X(01).                      
001566     05  FM2-ORIGIN               PIC X(08).                      
001568     05  FM2-INT                  PIC X(01).                      
001570     05  FM2-SYSTEM-USE           PIC X(01).                      
001572                                                                  
001574*
001576*    FILE DESCRIPTION FOR REPORT LISTING.
001578*
001580 FD  LISTING
001582     VALUE OF TITLE IS "LISTING"
001584     VALUE OF FAMILYNAME IS "GENERAL"
001586     VALUE OF FILENAME IS WS-LISTING-NAME
001588     VALUE OF USERBACKUPNAME IS "TRUE"
001590     VALUE OF PRINTDISPOSITION IS "DONTPRINT"
001592     VALUE OF SAVEPRINTFILE IS "TRUE"
001594     VALUE OF PRINTDISPOSITION IS "CLOSE".
001596 01  Z-RPT-1-BUFFER                             PIC X(160).
001598*
001600*    FILE DESCRIPTION FOR REPORT FICHE.
001602*
001604 FD  FICHE
001606     VALUE OF TITLE IS "FICHE"
001608     VALUE OF FAMILYNAME IS "GENERAL"
001610     VALUE OF FILENAME IS WS-FICHE-NAME
001612     VALUE OF USERBACKUPNAME IS "TRUE"
001614     VALUE OF PRINTDISPOSITION IS "DONTPRINT"
001616     VALUE OF SAVEPRINTFILE IS "TRUE"
001618     VALUE OF PRINTDISPOSITION IS "CLOSE".
001620 01  Z-RPT-2-BUFFER                             PIC X(160).
001622*
001624 DATA-BASE SECTION.
001626*--------- -------
001628*
001630 DB  LDBSPCDB =  SPCDB.
001632 01  SPCPRT
001634         USING SPCPRTALL,
001636               SPCPRTCURR.
001638 DB  LDBTDADB =  TDADB.
001640 01  TDARESTART
001642         USING NONE.
001644 01  TDAACCT
001646         USING TDAAMSET.
001648 01  TDAREPORTS
001650         USING NONE.
001652 01  TDAPCR
001654         USING TDAPCRSET.
001656 01  TDACUST
001658         USING TDACMSET,
001660               TDATINSET.
001662 01  TDAIRA
001664         USING TDAIRASET.
001666 01  TDADISTR
001668         USING TDADSSET,
001670               TDADSNBRSET.
001672 01  TDAACTV
001674         USING TDAACTVBKSET.
001676*
001678 WORKING-STORAGE SECTION.
001680*--------------- -------
001682 77  Z-TIME-GENERATED         PIC X(16) VALUE "20240410173653".
001684*                                     FORMAT = CCYYMMDDZZUUSS
001686 77  Z-FLAG                                     PIC 9.
001688 77  Z-II                                       PIC S9(11) BINARY.
001690 77  Z-LU                                       PIC S9(11) BINARY.
001692 77  Z-JJ                                       PIC S9(11) BINARY.
001694 77  Z-KK                                       PIC S9(11) BINARY.
001696 77  Z-LL                                       PIC S9(11) BINARY.
001698 77  Z-DISP-SIZE                                PIC S9(11) BINARY.
001700 77  Z-RPT-NUM                                  PIC 99.
001702 77  Z-SYSTEM-NAME                              PIC X(30)
001704     VALUE "TDAR".
001706 77  Z-PROGRAM-NAME                             PIC X(30)
001708     VALUE "MINDISTCALC".
001710 77  Z-I-1                                      PIC S9(11) BINARY.
001712 77  Z-I-2                                      PIC S9(11) BINARY.
001714 77  Z-TO-1                                     PIC S9(11) BINARY.
001716 77  Z-TO-2                                     PIC S9(11) BINARY.
001718 77  Z-TO-3                                     PIC S9(11) BINARY.
001720 77  J                                          PIC S9(11) BINARY.
001722 77  WS-SPECS-BANK-DATE           PIC 9(07) VALUE 0.              
001724 77  WS-SPECS-BANK-TIME           PIC 9(12) VALUE 0.              
001726 77  NO-LINES                        PIC 9(02)   BINARY EXTENDED. 
001728 77  LINE-CTR                        PIC 9(04)   BINARY EXTENDED  
001730                                                 VALUE 0.         
001732 77  PAGE-CTR                        PIC 9(04)   BINARY EXTENDED  
001734                                                 VALUE 0.         
001736 77  END-PAGE                        PIC 9(04)   BINARY EXTENDED  
001738                                                 VALUE 58.        
001740 77  HDR-CTL                         PIC 9(01)   BINARY EXTENDED  
001742                                                 VALUE 0.         
001744 77  GWS-TP-CTL                      PIC 9(01) VALUE 0.           
001746 77  TP-LN-CHAR                      PIC 9(02) VALUE 0.           
001748 77  Z-LINT-1                                   PIC S9(11) BINARY.
001750 77  Z-LINT-2                                   PIC S9(11) BINARY.
001752 01  Z-LALPHA-1                                 PIC X(256).
001754 01  Z-LALPHA-2                                 PIC X(256).
001756 01  Z-LALPHA-3                                 PIC X(256).
001758 77  Z-GINT-1 PIC S9(11) BINARY.
001760 01  Z-GALPHA-1                                 PIC X(41).
001762 77  Z-STR-INT-ZERO                             PIC S9(11) BINARY 
001764     VALUE 0.
001766 77  Z-STR-INT-ONE                              PIC S9(11) BINARY 
001768     VALUE 1.
001770 77  Z-STR-INT-DEFAULT                          PIC S9(11) BINARY 
001772     VALUE -1024.
001774 77  Z-STR-INT-MAXSZ                            PIC S9(11) BINARY 
001776     VALUE 41.
001778 01  Z-STR-ALPHA-SPACE                          PIC X VALUE SPACE.
001780 01  Z-STR-ALPHA-ZERO                           PIC X VALUE ZERO.
001782 01  Z-STR-ALPHA-HIGH-VALUE                     PIC X VALUE       
001784     HIGH-VALUE.
001786 01  Z-STR-ALPHA-LOW-VALUE                      PIC X VALUE       
001788     LOW-VALUE.
001790 01  Z-STR-ALPHA-QUOTE                          PIC X VALUE QUOTE.
001792 01  Z-GSTRNUM-1.
001794     05  Z-GSTRNUM-1-9                          PIC 9.
001796 01  Z-GSTRNUM-2.
001798     05  Z-GSTRNUM-2-9                          PIC 9.
001800*
001802****** FLAGS AREA ******
001804 01  Z-FLAGS-AREA.
001806     05  Z-FOUND-FLAG                           PIC 9.
001808         88  Z-NOT-FOUND                          VALUE 0.
001810         88  Z-FOUND                              VALUE 1.
001812     05  Z-EDIT-ERROR-FLAG                      PIC 9.
001814         88  Z-NO-EDIT-ERROR                      VALUE 0.
001816         88  Z-EDIT-ERROR                         VALUE 1.
001818     05  Z-EDIT-FIRSTERROR-FLAG                 PIC 9.
001820         88  Z-EDIT-FIRSTERROR                    VALUE 0.
001822     05  Z-EDIT-LASTERROR-FLAG                  PIC 9.
001824         88  Z-NO-EDIT-LASTERROR                  VALUE 0.
001826         88  Z-EDIT-LASTERROR                     VALUE 1.
001828     05  Z-SIZE-ERROR-FLAG                      PIC 9.
001830         88  Z-NO-SIZE-ERROR                      VALUE 0.
001832         88  Z-SIZE-ERROR                         VALUE 1.
001834     05  Z-FINISH-FLAG                          PIC 9.
001836         88  Z-NOT-FINISHED                       VALUE 0.
001838         88  Z-FINISHED                           VALUE 1.
001840     05  Z-CONTINUE-FLAG                        PIC 9.
001842         88  Z-NOT-CONTINUED                      VALUE 0.
001844         88  Z-CONTINUED                          VALUE 1.
001846         88  Z-REPROCESS                          VALUE 2.
001848     05  Z-PROCESS-FLAG                         PIC 9.
001850         88  Z-NO-PROCESS                         VALUE 0.
001852         88  Z-PROCESS                            VALUE 1.
001854     05  Z-EXIT-CODE                            PIC 9.
001856         88  Z-EXIT-NORM                          VALUE 0.
001858         88  Z-EXIT-NO-LABEL                      VALUE 1.
001860         88  Z-EXIT-LABEL                         VALUE 2.
001862         88  Z-EXIT-ALL                           VALUE 3.
001864         88  Z-EXIT-EDITEXIT                      VALUE 4.
001866         88  Z-EXIT-PROCESS                       VALUE 5.
001868     05  Z-EXIT-LEVEL                           PIC S9(6).
001870         88  Z-EXIT-ALL-LEVELS                    VALUE -1.
001872     05  Z-EXIT-PROCEDURE-LABEL                 PIC X(30).
001874     05  Z-EXIT-PERFORM-LABEL                   PIC X(30).
001876     05  Z-LAST-KEY-PROC                        PIC 9.
001878         88  Z-GET-LAST-KEY                       VALUE 0.
001880         88  Z-DEL-LAST-KEY                       VALUE 1.
001882         88  Z-UPDATE-LAST-KEY                    VALUE 2.
001884     05  Z-DMS-ABORT-FLAG                       PIC 9.
001886         88  Z-DMS-ABORT-OK                       VALUE 0.
001888         88  Z-DMS-ABORT-SKIP                     VALUE 1.
001890     05  Z-EDIT-NO-MSG                          PIC 9.
001892     05  Z-EDIT-DEFAULT-SEEN                    PIC 9.
001894*
001896****** SAVE/RESTART AREA ******
```

⚠️  This is the source code you must document.
    460 lines from 485 to 944.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

