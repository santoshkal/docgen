# LLM Request Debug File
Generated: 2025-11-18T19:52:59.187065

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 37/55
- **Model**: gpt-4.1
- **Chunk Number**: 37
- **Pass Number**: 3
- **Attempt Number**: 7 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,086 tokens
- **User Prompt**: ~7,612 tokens
- **Total Input**: ~9,698 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 37/55" (ID: detailed-code-explanation)

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


**CHUNK 37 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T18:05:37.383587", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 37 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 17910 to 18376 (467 lines)\nChunk Tokens (estimated): ~8,068\nActual Input Tokens: 9,474 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 17910-18376 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 37 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 37 of 55.\n\n\n=============================================================================\nCHUNK 37 SOURCE CODE (Lines 17910-18376)\n=============================================================================\n\n```cobol\n035828         HOLD-TDAPCR.\n035830     MOVE TDAPC-SPECS OF TDAPCR TO HOLD-TDAPC-SPECS OF            \n035832         HOLD-TDAPCR.\n035834     MOVE TDAPC-COPIES OF TDAPCR TO HOLD-TDAPC-COPIES OF          \n035836         HOLD-TDAPCR.\n035838     MOVE TDAPC-LASER-PRT OF TDAPCR TO HOLD-TDAPC-LASER-PRT OF    \n035840         HOLD-TDAPCR.\n035842     MOVE TDAPC-FICHE-PRT OF TDAPCR TO HOLD-TDAPC-FICHE-PRT OF    \n035844         HOLD-TDAPCR.\n035846     MOVE TDAPC-OPTICAL OF TDAPCR TO HOLD-TDAPC-OPTICAL OF        \n035848         HOLD-TDAPCR.\n035850     MOVE TDAPC-PRT-DLY OF TDAPCR TO HOLD-TDAPC-PRT-DLY OF        \n035852         HOLD-TDAPCR.\n035854     MOVE TDAPC-DLY-IND OF TDAPCR TO HOLD-TDAPC-DLY-IND OF        \n035856         HOLD-TDAPCR.\n035858     MOVE TDAPC-LST-PRT-D OF TDAPCR TO HOLD-TDAPC-LST-PRT-D OF    \n035860         HOLD-TDAPCR.\n035862     MOVE TDAPC-PRT-WK OF TDAPCR TO HOLD-TDAPC-PRT-WK OF          \n035864         HOLD-TDAPCR.\n035866     MOVE TDAPC-WK-IND OF TDAPCR TO HOLD-TDAPC-WK-IND OF          \n035868         HOLD-TDAPCR.\n035870     MOVE TDAPC-LST-PRT-W OF TDAPCR TO HOLD-TDAPC-LST-PRT-W OF    \n035872         HOLD-TDAPCR.\n035874     MOVE TDAPC-PRT-MTH OF TDAPCR TO HOLD-TDAPC-PRT-MTH OF        \n035876         HOLD-TDAPCR.\n035878     MOVE TDAPC-LST-DAY-M OF TDAPCR TO HOLD-TDAPC-LST-DAY-M OF    \n035880         HOLD-TDAPCR.\n035882     MOVE TDAPC-NXT-PRT-M OF TDAPCR TO HOLD-TDAPC-NXT-PRT-M OF    \n035884         HOLD-TDAPCR.\n035886     MOVE TDAPC-LST-PRT-M OF TDAPCR TO HOLD-TDAPC-LST-PRT-M OF    \n035888         HOLD-TDAPCR.\n035890     MOVE TDAPC-PRT-QTR OF TDAPCR TO HOLD-TDAPC-PRT-QTR OF        \n035892         HOLD-TDAPCR.\n035894     MOVE TDAPC-LST-DAY-Q OF TDAPCR TO HOLD-TDAPC-LST-DAY-Q OF    \n035896         HOLD-TDAPCR.\n035898     MOVE TDAPC-NXT-PRT-Q OF TDAPCR TO HOLD-TDAPC-NXT-PRT-Q OF    \n035900         HOLD-TDAPCR.\n035902     MOVE TDAPC-LST-PRT-Q OF TDAPCR TO HOLD-TDAPC-LST-PRT-Q OF    \n035904         HOLD-TDAPCR.\n035906     MOVE TDAPC-PRT-YR OF TDAPCR TO HOLD-TDAPC-PRT-YR OF          \n035908         HOLD-TDAPCR.\n035910     MOVE TDAPC-NXT-PRT-Y OF TDAPCR TO HOLD-TDAPC-NXT-PRT-Y OF    \n035912         HOLD-TDAPCR.\n035914     MOVE TDAPC-LST-PRT-Y OF TDAPCR TO HOLD-TDAPC-LST-PRT-Y OF    \n035916         HOLD-TDAPCR.\n035918     MOVE TDAPC-SPECL-REQ OF TDAPCR TO HOLD-TDAPC-SPECL-REQ OF    \n035920         HOLD-TDAPCR.\n035922     MOVE TDAPC-PRT-DAY OF TDAPCR TO HOLD-TDAPC-PRT-DAY OF        \n035924         HOLD-TDAPCR.\n035926     MOVE TDAPC-BEGIN-DATE OF TDAPCR TO HOLD-TDAPC-BEGIN-DATE OF  \n035928         HOLD-TDAPCR.\n035930     MOVE TDAPC-END-DATE OF TDAPCR TO HOLD-TDAPC-END-DATE OF      \n035932         HOLD-TDAPCR.\n035934     MOVE TDAPC-PRINTER OF TDAPCR TO HOLD-TDAPC-PRINTER OF        \n035936         HOLD-TDAPCR.\n035938     MOVE TDAPC-SPECL-SPECS OF TDAPCR TO HOLD-TDAPC-SPECL-SPECS   \n035940         OF HOLD-TDAPCR.\n035942     MOVE TDAPC-REQUESTOR OF TDAPCR TO HOLD-TDAPC-REQUESTOR OF    \n035944         HOLD-TDAPCR.\n035946     MOVE TDAPC-LPROCESS-DT OF TDAPCR TO HOLD-TDAPC-LPROCESS-DT   \n035948         OF HOLD-TDAPCR.\n035950     MOVE TDAPC-LUPD-DT OF TDAPCR TO HOLD-TDAPC-LUPD-DT OF        \n035952         HOLD-TDAPCR.\n035954     MOVE TDAPC-LUPD-TM OF TDAPCR TO HOLD-TDAPC-LUPD-TM OF        \n035956         HOLD-TDAPCR.\n035958     MOVE TDAPC-BP-LAST-RUN OF TDAPCR TO HOLD-TDAPC-BP-LAST-RUN   \n035960         OF HOLD-TDAPCR.\n035962     MOVE TDAPC-PUB-ID OF TDAPCR TO HOLD-TDAPC-PUB-ID OF          \n035964         HOLD-TDAPCR.\n035966     MOVE TDAPC-BANK-SPECS OF TDAPCR TO HOLD-TDAPC-BANK-SPECS OF  \n035968         HOLD-TDAPCR.\n035970     MOVE ZEROS TO BANK-BR-3 OF BANK-REC.\n035972     MOVE ZEROS TO BANK-CSI-BR-CODE OF BANK-REC.\n035974     MOVE SPACES TO BANK-NAME OF BANK-REC.\n035976     MOVE SPACES TO BANK-ADDR OF BANK-REC.\n035978     MOVE SPACES TO BANK-ADDR-2 OF BANK-REC.\n035980     MOVE SPACES TO BANK-FED-ID OF BANK-REC.\n035982     MOVE ZEROS TO BANK-INT-JRNL-BR-PRT OF BANK-REC.\n035984     MOVE SPACES TO BANK-CK-PRT-FORMAT OF BANK-REC.\n035986     MOVE SPACES TO BANK-RESTRICT-REDEMP-TICKET OF BANK-REC.\n035988     MOVE SPACES TO BANK-CK-PRT-ACCTNO OF BANK-REC.\n035990     MOVE SPACES TO BANK-RESTRICT-RATE-PRT OF BANK-REC.\n035992     MOVE SPACES TO BANK-CK-PROTECT OF BANK-REC.\n035994     MOVE ZEROS TO BANK-SP-CK-REMARK OF BANK-REC.\n035996     MOVE ZEROS TO BANK-APPL OF BANK-REC.\n035998     MOVE SPACES TO BANK-RMT-IND OF BANK-REC.\n036000     MOVE SPACES TO BANK-STATUS OF BANK-REC.\n036002     MOVE SPACES TO BANK-TDA-PILOT OF BANK-REC.\n036004     MOVE ZEROS TO BANK-PHN-AREA OF BANK-REC.\n036006     MOVE ZEROS TO BANK-PHN-PREFIX OF BANK-REC.\n036008     MOVE ZEROS TO BANK-PHN-SUFFIX OF BANK-REC.\n036010     MOVE ZEROS TO BANK-IRA-PHN-AREA OF BANK-REC.\n036012     MOVE ZEROS TO BANK-IRA-PHN-PREFIX OF BANK-REC.\n036014     MOVE ZEROS TO BANK-IRA-PHN-SUFFIX OF BANK-REC.\n036016     MOVE SPACES TO BANK-EOY-IRA-STMT OF BANK-REC.\n036018     MOVE SPACES TO BANK-EOY-IRA-STMT-EARLY OF BANK-REC.\n036020     MOVE SPACES TO BANK-EOY-IRA-STMT-PRINT OF BANK-REC.\n036022     MOVE ZEROS TO BANK-EOY-DELETE-DATE OF BANK-REC.\n036024     MOVE ZEROS TO BANK-EOY-APRIL-DATE OF BANK-REC.\n036026     MOVE ZEROS TO BANK-EOY-APRIL-DATE-CCYY OF BANK-REC.\n036028     MOVE ZEROS TO BANK-EOY-APRIL-DATE-MMDD OF BANK-REC.\n036030     MOVE ZEROS TO BANK-EOY-EARLY-DATE OF BANK-REC.\n036032     MOVE ZEROS TO BANK-EOY-NO-IRA-STMTS OF BANK-REC.\n036034     MOVE SPACES TO BANK-EOY-RETURN-TO-BANK OF BANK-REC.\n036036     MOVE SPACES TO BANK-EOY-EARLY-RUN OF BANK-REC.\n036038     MOVE SPACES TO BANK-EOY-RPT-SEQ OF BANK-REC.\n036040     MOVE SPACES TO BANK-EOY-IRA-FICHE OF BANK-REC.\n036042     MOVE SPACES TO BANK-EOY-IRA-PAPER OF BANK-REC.\n036044     MOVE ZEROS TO BANK-NO-IRA-STMTS OF BANK-REC.\n036046     MOVE SPACES TO BANK-OPT-HOL OF BANK-REC.\n036048     MOVE SPACES TO BANK-CK21-TDA OF BANK-REC.\n036050     MOVE SPACES TO BANK-DQVISTA OF BANK-REC.\n036052     MOVE SPACES TO BANK-MSI OF BANK-REC.\n036054     MOVE SPACES TO BANK-MSI-OV-TDA OF BANK-REC.\n036056     MOVE SPACES TO BANK-BK-IMG-SERV OF BANK-REC.\n036058     MOVE SPACES TO BANK-FM-SUPPRESS OF BANK-REC.\n036060     MOVE SPACES TO BANK-EOY-COD-CLOSED-RPT OF BANK-REC.\n036062     MOVE SPACES TO BANK-PRT-NEW OF BANK-REC.\n036064     MOVE SPACES TO BANK-IMONITOR OF BANK-REC.\n036066     MOVE SPACES TO BANK-CENTERVIEW OF BANK-REC.\n036068     MOVE SPACES TO BANK-TDA-ADD-DAY OF BANK-REC.\n036070     MOVE 1 TO Z-II.\n036072 Z-4-5-1-LOOP.\n036074     IF Z-II > 18\n036076         GO TO Z-4-5-1-LOOP-XIT.\n036078     MOVE SPACES TO BANK-HOL-MM OF BANK-REC (Z-II).\n036080     MOVE SPACES TO BANK-HOL-DD OF BANK-REC (Z-II).\n036082     ADD 1 TO Z-II.\n036084     GO TO Z-4-5-1-LOOP.\n036086 Z-4-5-1-LOOP-XIT.\n036088     MOVE ZEROS TO BANK-CREATE-DT OF BANK-REC.\n036090     MOVE ZEROS TO BANK-CREATE-TM OF BANK-REC.\n036092     MOVE SPACES TO BANK-ENTC-TDA OF BANK-REC.\n036094     MOVE SPACES TO BANK-EV-3RD-PARTY-1 OF BANK-REC.\n036096     MOVE SPACES TO BANK-EV-3RD-PARTY-2 OF BANK-REC.\n036098     MOVE SPACES TO BANK-HSA-LOCATION OF BANK-REC.\n036100     MOVE SPACES TO BANK-PROFITABILITY OF BANK-REC.\n036102     MOVE SPACES TO BANK-BANCVUE OF BANK-REC.\n036104     MOVE SPACES TO BANK-SPECIAL-DL-BILLING OF BANK-REC.\n036106     MOVE SPACES TO BANK-WEB-ENABLED OF BANK-REC.\n036108     MOVE ZEROS TO BANK-CIF-NAME-ADDR OF BANK-REC.\n036110     MOVE SPACES TO BANK-MAIL-ADDR-LINES OF BANK-REC.\n036112     MOVE ZEROS TO BANK-BRANCH-LENGTH OF BANK-REC.\n036114     MOVE ZEROS TO BANK-LOB OF BANK-REC.\n036116     MOVE ZEROS TO BANK-LAST-EOM-PROC OF BANK-REC.\n036118     MOVE SPACES TO BANK-TRAIN-BK-FLG OF BANK-REC.\n036120     MOVE SPACES TO BANK-EOY-CIB-F-MERD OF BANK-REC.\n036122     MOVE ZEROS TO SPECS-GRACE-IN-PROC OF SPECS-AREA.\n036124     MOVE ZEROS TO SPECS-GRACE-CLOSE OF SPECS-AREA.\n036126     MOVE ZEROS TO SPECS-PRE-MAT OF SPECS-AREA.\n036128     MOVE SPACES TO SPECS-LSR-PILOT OF SPECS-AREA.\n036130     MOVE ZEROS TO SPECS-CHK-RECON OF SPECS-AREA.\n036132     MOVE SPACES TO SPECS-BR-ADDR OF SPECS-AREA.\n036134     MOVE SPACES TO SPECS-TIN-SUPPRESS OF SPECS-AREA.\n036136     MOVE SPACES TO SPECS-NO-IN-PROC OF SPECS-AREA.\n036138     MOVE SPACES TO SPECS-RMD-OVERRIDE OF SPECS-AREA.\n036140     MOVE SPACES TO SPECS-PPP-PILOT OF SPECS-AREA.\n036142     MOVE SPACES TO SPECS-RETURN-ENVELOPE OF SPECS-AREA.\n036144     MOVE SPACES TO SPECS-LSTCONT-DDACOMB OF SPECS-AREA.\n036146     MOVE SPACES TO SPECS-LSTCONT-TDASTMT OF SPECS-AREA.\n036148     MOVE SPACES TO SPECS-LSTCONT-INTNTC OF SPECS-AREA.\n036150     MOVE SPACES TO SPECS-LSTCONT-ALLNTC OF SPECS-AREA.\n036152     MOVE SPACES TO SPECS-LSTCONT-CHECKS OF SPECS-AREA.\n036154     MOVE SPACES TO SPECS-LSTCONT-DISTREC OF SPECS-AREA.\n036156     MOVE SPACES TO SPECS-COMB-AUTO-RMD-ADJUST OF SPECS-AREA.\n036158     MOVE ZEROS TO SPECS-IGL-HIGH-BAL OF SPECS-AREA.\n036160     MOVE SPACES TO SPECS-AVAIL-CAP-INT OF SPECS-AREA.\n036162     MOVE ZEROS TO SPECS-CNV-TOT-DNLOAD OF SPECS-AREA.\n036164     MOVE SPACES TO SPECS-CNV-TOT-DNLOAD-X OF SPECS-AREA.\n036166     MOVE ZEROS TO SPECS-ADDR-ALERT-DAYS OF SPECS-AREA.\n036168     MOVE SPACES TO SPECS-COMB-SEND-CERT OF SPECS-AREA.\n036170     MOVE SPACES TO SPECS-APPLY-GRACE-AT-SR OF SPECS-AREA.\n036172     MOVE SPACES TO SPECS-DB-SUFFIX OF SPECS-AREA.\n036174     MOVE SPACES TO SPECS-EOY-YTD-ROLL OF SPECS-AREA.\n036176     MOVE SPACES TO SPECS-COMB-DDA-OPT OF SPECS-AREA.\n036178     MOVE SPACES TO SPECS-CONTINUE OF SPECS-AREA.\n036180     MOVE TDAPC-SPECS TO SPECS-AREA.\n036182     MOVE TDAPC-BANK-SPECS TO TDB-TDAPC-BANK-SPECS.\n036184     MOVE TDB-TDAPC-CSI-BR-CODE OF TDB-TDAPC-BANK-SPECS-R TO      \n036186         BANK-CSI-BR-CODE OF BANK-REC.\n036188     MOVE TDB-TDAPC-FED-ID OF TDB-TDAPC-BANK-SPECS-R TO           \n036190         BANK-FED-ID OF BANK-REC.\n036192     MOVE TDB-TDAPC-RMT-IND OF TDB-TDAPC-BANK-SPECS-R TO          \n036194         BANK-RMT-IND OF BANK-REC.\n036196     MOVE TDB-TDAPC-TDA-PILOT OF TDB-TDAPC-BANK-SPECS-R TO        \n036198         BANK-TDA-PILOT OF BANK-REC.\n036200     MOVE TDB-TDAPC-EOY-IRA-STMT OF TDB-TDAPC-BANK-SPECS-R TO     \n036202         BANK-EOY-IRA-STMT OF BANK-REC.\n036204     MOVE TDB-TDAPC-EOY-IRA-STMT-EARLY OF TDB-TDAPC-BANK-SPECS-R  \n036206         TO BANK-EOY-IRA-STMT-EARLY OF BANK-REC.\n036208     MOVE TDB-TDAPC-EOY-IRA-STMT-PRINT OF TDB-TDAPC-BANK-SPECS-R  \n036210         TO BANK-EOY-IRA-STMT-PRINT OF BANK-REC.\n036212     MOVE TDB-TDAPC-EOY-DELETE-DATE OF TDB-TDAPC-BANK-SPECS-R TO  \n036214         BANK-EOY-DELETE-DATE OF BANK-REC.\n036216     MOVE TDB-TDAPC-EOY-APRIL-DATE OF TDB-TDAPC-BANK-SPECS-R TO   \n036218         BANK-EOY-APRIL-DATE OF BANK-REC.\n036220     MOVE TDB-TDAPC-EOY-EARLY-DATE OF TDB-TDAPC-BANK-SPECS-R TO   \n036222         BANK-EOY-EARLY-DATE OF BANK-REC.\n036224     MOVE TDB-TDAPC-EOY-RETURN-TO-BANK OF TDB-TDAPC-BANK-SPECS-R  \n036226         TO BANK-EOY-RETURN-TO-BANK OF BANK-REC.\n036228     MOVE TDB-TDAPC-EOY-EARLY-RUN OF TDB-TDAPC-BANK-SPECS-R TO    \n036230         BANK-EOY-EARLY-RUN OF BANK-REC.\n036232     MOVE TDB-TDAPC-EOY-RPT-SEQ OF TDB-TDAPC-BANK-SPECS-R TO      \n036234         BANK-EOY-RPT-SEQ OF BANK-REC.\n036236     MOVE TDB-TDAPC-EOY-IRA-FICHE OF TDB-TDAPC-BANK-SPECS-R TO    \n036238         BANK-EOY-IRA-FICHE OF BANK-REC.\n036240     MOVE TDB-TDAPC-EOY-IRA-PAPER OF TDB-TDAPC-BANK-SPECS-R TO    \n036242         BANK-EOY-IRA-PAPER OF BANK-REC.\n036244     MOVE TDB-TDAPC-NO-IRA-STMTS OF TDB-TDAPC-BANK-SPECS-R TO     \n036246         BANK-NO-IRA-STMTS OF BANK-REC.\n036248     MOVE TDB-TDAPC-CK21-TDA OF TDB-TDAPC-BANK-SPECS-R TO         \n036250         BANK-CK21-TDA OF BANK-REC.\n036252     MOVE TDB-TDAPC-DQVISTA OF TDB-TDAPC-BANK-SPECS-R TO          \n036254         BANK-DQVISTA OF BANK-REC.\n036256     MOVE TDB-TDAPC-MSI OF TDB-TDAPC-BANK-SPECS-R TO BANK-MSI OF  \n036258         BANK-REC.\n036260     MOVE TDB-TDAPC-MSI-OV-TDA OF TDB-TDAPC-BANK-SPECS-R TO       \n036262         BANK-MSI-OV-TDA OF BANK-REC.\n036264     MOVE TDB-TDAPC-BK-IMG-SERV OF TDB-TDAPC-BANK-SPECS-R TO      \n036266         BANK-BK-IMG-SERV OF BANK-REC.\n036268     MOVE TDB-TDAPC-FM-SUPPRESS OF TDB-TDAPC-BANK-SPECS-R TO      \n036270         BANK-FM-SUPPRESS OF BANK-REC.\n036272     MOVE TDB-TDAPC-EOY-COD-CLOSED-RPT OF TDB-TDAPC-BANK-SPECS-R  \n036274         TO BANK-EOY-COD-CLOSED-RPT OF BANK-REC.\n036276     MOVE TDB-TDAPC-PRT-NEW OF TDB-TDAPC-BANK-SPECS-R TO          \n036278         BANK-PRT-NEW OF BANK-REC.\n036280     MOVE TDB-TDAPC-IMONITOR OF TDB-TDAPC-BANK-SPECS-R TO         \n036282         BANK-IMONITOR OF BANK-REC.\n036284     MOVE TDB-TDAPC-TDA-ADD-DAY OF TDB-TDAPC-BANK-SPECS-R TO      \n036286         BANK-TDA-ADD-DAY OF BANK-REC.\n036288     MOVE 1 TO Z-II.\n036290 Z-4-9-1-LOOP.\n036292     IF Z-II > 18\n036294         GO TO Z-4-9-1-LOOP-XIT.\n036296     MOVE TDB-TDAPC-HOL-MM OF TDB-TDAPC-BANK-SPECS-R (Z-II) TO    \n036298         BANK-HOL-MM OF BANK-REC (Z-II).\n036300     MOVE TDB-TDAPC-HOL-DD OF TDB-TDAPC-BANK-SPECS-R (Z-II) TO    \n036302         BANK-HOL-DD OF BANK-REC (Z-II).\n036304     ADD 1 TO Z-II.\n036306     GO TO Z-4-9-1-LOOP.\n036308 Z-4-9-1-LOOP-XIT.\n036310     MOVE TDB-TDAPC-CREATE-DT OF TDB-TDAPC-BANK-SPECS-R TO        \n036312         BANK-CREATE-DT OF BANK-REC.\n036314     MOVE TDB-TDAPC-CREATE-TM OF TDB-TDAPC-BANK-SPECS-R TO        \n036316         BANK-CREATE-TM OF BANK-REC.\n036318     MOVE TDB-TDAPC-ENTC-TDA OF TDB-TDAPC-BANK-SPECS-R TO         \n036320         BANK-ENTC-TDA OF BANK-REC.\n036322     MOVE TDB-TDAPC-EV-3RD-PARTY-1 OF TDB-TDAPC-BANK-SPECS-R TO   \n036324         BANK-EV-3RD-PARTY-1 OF BANK-REC.\n036326     MOVE TDB-TDAPC-EV-3RD-PARTY-2 OF TDB-TDAPC-BANK-SPECS-R TO   \n036328         BANK-EV-3RD-PARTY-2 OF BANK-REC.\n036330     MOVE TDB-TDAPC-HSA-LOCATION OF TDB-TDAPC-BANK-SPECS-R TO     \n036332         BANK-HSA-LOCATION OF BANK-REC.\n036334     MOVE TDB-TDAPC-PROFITABILITY OF TDB-TDAPC-BANK-SPECS-R TO    \n036336         BANK-PROFITABILITY OF BANK-REC.\n036338     MOVE TDB-TDAPC-BANCVUE OF TDB-TDAPC-BANK-SPECS-R TO          \n036340         BANK-BANCVUE OF BANK-REC.\n036342     MOVE TDB-TDAPC-SPECIAL-DL-BILLING OF TDB-TDAPC-BANK-SPECS-R  \n036344         TO BANK-SPECIAL-DL-BILLING OF BANK-REC.\n036346     MOVE TDB-TDAPC-WEB-ENABLED OF TDB-TDAPC-BANK-SPECS-R TO      \n036348         BANK-WEB-ENABLED OF BANK-REC.\n036350     MOVE TDB-TDAPC-CIF-NAME-ADDR OF TDB-TDAPC-BANK-SPECS-R TO    \n036352         BANK-CIF-NAME-ADDR OF BANK-REC.\n036354     MOVE TDB-TDAPC-MAIL-ADDR-LINES OF TDB-TDAPC-BANK-SPECS-R TO  \n036356         BANK-MAIL-ADDR-LINES OF BANK-REC.\n036358     MOVE TDB-TDAPC-BRANCH-LENGTH OF TDB-TDAPC-BANK-SPECS-R TO    \n036360         BANK-BRANCH-LENGTH OF BANK-REC.\n036362     MOVE TDB-TDAPC-LOB OF TDB-TDAPC-BANK-SPECS-R TO BANK-LOB OF  \n036364         BANK-REC.\n036366     MOVE TDB-TDAPC-LAST-EOM-PROC OF TDB-TDAPC-BANK-SPECS-R TO    \n036368         BANK-LAST-EOM-PROC OF BANK-REC.\n036370     MOVE TDB-TDAPC-TRAIN-BK-FLG OF TDB-TDAPC-BANK-SPECS-R TO     \n036372         BANK-TRAIN-BK-FLG OF BANK-REC.\n036374     MOVE TDB-TDAPC-EOY-CIB-F-MERD OF TDB-TDAPC-BANK-SPECS-R TO   \n036376         BANK-EOY-CIB-F-MERD OF BANK-REC.\n036378     MOVE TDAPC-RPT-DESC TO BANK-NAME.\n036380     IF ( WS-SPECS-BANK-DATE > BANK-CREATE-DT ) OR ( (            \n036382         WS-SPECS-BANK-DATE = BANK-CREATE-DT ) AND (              \n036384         WS-SPECS-BANK-TIME > BANK-CREATE-TM ) )\n036386         NEXT SENTENCE ELSE\n036388         GO TO Z-4-11-1-ELSE.\n036390*\n036392******* OPEN FILE BK-SPEC-FILE\n036394*\n036396     IF Z-FLINFO3-OPEN = 0\n036398         CHANGE ATTRIBUTE DEPENDENTSPECS OF BK-SPEC-FILE TO TRUE \n036400         OPEN INPUT BK-SPEC-FILE \n036402         IF ATTRIBUTE FILESTATE OF BK-SPEC-FILE = VALUE OPENED\n036404             MOVE ZEROS TO Z-FILE3-KEY\n036406             MOVE ZEROS TO Z-FLINFO3-RS-KEY\n036408             MOVE 1 TO Z-FLINFO3-OPEN\n036410             MOVE 1 TO Z-FLINFO3-RS-OPEN\n036412         ELSE\n036414             DISPLAY \">>> FILE BK-SPEC-FILE FAILED TO OPEN\"\n036416             MOVE ATTRIBUTE TITLE OF BK-SPEC-FILE TO              \n036418                 Z-FL-EXCEPT-TITLE\n036420             DISPLAY \">>> OPEN FAIL, TITLE :\", Z-FL-EXCEPT-TITLE\n036422             DISPLAY \">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS\".\n036424*\n036426******* OPEN FILE BK-SPEC-FILE\n036428*\n036430     IF Z-FLINFO3-OPEN = 0\n036432         CHANGE ATTRIBUTE DEPENDENTSPECS OF BK-SPEC-FILE TO TRUE \n036434         OPEN INPUT BK-SPEC-FILE \n036436         IF ATTRIBUTE FILESTATE OF BK-SPEC-FILE = VALUE OPENED\n036438             MOVE ZEROS TO Z-FILE3-KEY\n036440             MOVE ZEROS TO Z-FLINFO3-RS-KEY\n036442             MOVE 1 TO Z-FLINFO3-OPEN\n036444             MOVE 1 TO Z-FLINFO3-RS-OPEN\n036446         ELSE\n036448             DISPLAY \">>> FILE BK-SPEC-FILE FAILED TO OPEN\"\n036450             MOVE ATTRIBUTE TITLE OF BK-SPEC-FILE TO              \n036452                 Z-FL-EXCEPT-TITLE\n036454             DISPLAY \">>> OPEN FAIL, TITLE :\", Z-FL-EXCEPT-TITLE\n036456             DISPLAY \">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS\".\n036458     MOVE ZERO TO Z-FLINFO3-PRES.\n036460     MOVE ZERO TO Z-FLINFO3-SOME.\n036462     MOVE 7 TO Z-FLINFO3-LAST-SEQ.\n036464*\n036466 Z-4-13-LOOP.\n036468     MOVE ZERO TO Z-FLINFO3-PRES.\n036470*\n036472 Z-4-13-READ.\n036474     READ BK-SPEC-FILE RECORD \n036476         AT END\n036478         GO TO Z-4-13-XIT.\n036480     MOVE Z-FILE3-KEY TO Z-FLINFO3-RS-KEY.\n036482*\n036484     IF SPEC-BK-NO-9-4-N = WS-BANK-NO\n036486         NEXT SENTENCE ELSE\n036488         MOVE 1 TO Z-EXIT-LEVEL\n036490         GO TO Z-4-13-END.\n036492*\n036494     MOVE 1 TO Z-FLINFO3-PRES.\n036496     MOVE 1 TO Z-FLINFO3-SOME.\n036498     MOVE 1 TO Z-FLINFO3-MODIFY.\n036500     MOVE 0 TO Z-EXIT-CODE.\n036502     MOVE 9999 TO Z-EXIT-LEVEL.\n036504     IF SPEC-SEQ-NO-N = 01\n036506         NEXT SENTENCE ELSE\n036508         GO TO Z-4-14-1-ELSE.\n036510     MOVE SPEC-BK-NAME-N TO RMD-BK-NAME.\n036512     MOVE SPEC-BK-NO-9-4-N TO RMD-BK.\n036514     GO TO Z-4-14-ENDIF.\n036516 Z-4-14-1-ELSE.\n036518     IF SPEC-SEQ-NO-N = 02\n036520         NEXT SENTENCE ELSE\n036522         GO TO Z-4-14-2-ELSE.\n036524     MOVE SPEC-BR-NO-N TO RMD-DC.\n036526     GO TO Z-4-14-ENDIF.\n036528 Z-4-14-2-ELSE.\n036530     IF SPEC-SEQ-NO-N = 04\n036532         NEXT SENTENCE ELSE\n036534         GO TO Z-4-14-3-ELSE.\n036536     MOVE SPEC-RMT-BK-INDICATOR-N TO BANK-RMT-IND.\n036538     MOVE 1 TO Z-EXIT-LEVEL.\n036540     MOVE 1 TO Z-EXIT-CODE.\n036542     GO TO Z-4-13-END.\n036544 Z-4-14-3-ELSE.\n036546 Z-4-14-ENDIF.\n036548 Z-4-13-END.\n036550     IF Z-EDIT-ERROR\n036552         GO TO Z-4-XIT.\n036554 Z-4-13-SKIP.\n036556     IF Z-EXIT-LEVEL < 1\n036558         GO TO Z-4-END.\n036560     IF Z-EXIT-CODE > 0\n036562         GO TO Z-4-13-XIT.\n036564     GO TO Z-4-13-LOOP.\n036566*\n036568 Z-4-13-XIT.\n036570     MOVE 0 TO Z-EXIT-CODE.\n036572     MOVE 9999 TO Z-EXIT-LEVEL.\n036574*\n036576***********  CLOSE OF FILE BK-SPEC-FILE WITH RELEASE\n036578*\n036580     IF Z-FLINFO3-OPEN NOT = 0\n036582         CLOSE BK-SPEC-FILE WITH RELEASE\n036584         MOVE 0 TO Z-FLINFO3-OPEN\n036586         MOVE 0 TO Z-FLINFO3-RS-OPEN.\n036588     GO TO Z-4-11-ENDIF.\n036590 Z-4-11-1-ELSE.\n036592     MOVE BANK-NAME TO RMD-BK-NAME.\n036594     MOVE PROC-BANK TO RMD-BK.\n036596     MOVE BANK-CSI-BR-CODE TO RMD-DC.\n036598 Z-4-11-ENDIF.\n036600 Z-4-END.\n036602     IF Z-EDIT-ERROR\n036604         GO TO Z-4-XIT.\n036606 Z-4-SKIP.\n036608     IF Z-EXIT-LEVEL NOT < 0\n036610         MOVE 0 TO Z-EXIT-CODE\n036612         MOVE 9999 TO Z-EXIT-LEVEL.\n036614 Z-4-XIT.\n036616     EXIT.\n036618*\n036620*****************************************************************\n036622*    PROCEDURE GET-ACCT-INFO\n036624*****************************************************************\n036626 Z-5-PROCEDURE.\n036628*\n036630     MOVE 0 TO Z-EXIT-CODE.\n036632     MOVE 9999 TO Z-EXIT-LEVEL.\n036634     MOVE SPACES TO WS-TIN-CUST-TABLE\n036636       , WS-TIN-DETAIL-TABLE.\n036638     MOVE 0 TO WS-TIN-DISTR-RECS.\n036640     MOVE ZERO TO Z-FLINFO11-PRES.\n036642     MOVE ZERO TO Z-FLINFO11-SOME.\n036644     MOVE 8 TO Z-FLINFO11-LAST-SEQ.\n036646*\n036648     SET TDATINSET OF TDACUST OF LDBTDADB TO BEGINNING\n036650         ON EXCEPTION\n036652         MOVE \"TDATINSET OF TDACUST OF LDBTDADB\" TO               \n036654             Z-DMS-EXCEPT-STR\n036656         MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n036658         MOVE 8 TO Z-DMS-EXCEPT-SEQ\n036660         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT\n036662         GO TO Z-5-3-XIT.\n036664 Z-5-3-LOOP.\n036666     MOVE ZERO TO Z-FLINFO11-PRES.\n036668 Z-5-3-READ.\n036670     FIND TDACUST OF LDBTDADB VIA NEXT TDATINSET OF TDACUST OF    \n036672         LDBTDADB\n036674     AT TDAC-BANK = WS-BANK-NO\n036676         ON EXCEPTION\n036678         MOVE 8 TO Z-DMS-EXCEPT-SEQ\n036680         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n036682             GO TO Z-5-3-XIT\n036684         ELSE\n036686             MOVE \"TDATINSET OF TDACUST OF LDBTDADB\" TO           \n036688                 Z-DMS-EXCEPT-STR\n036690             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n036692             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n036694\n036696*\n036698     MOVE 1 TO Z-FLINFO11-PRES.\n036700     MOVE 1 TO Z-FLINFO11-SOME.\n036702     MOVE 0 TO Z-EXIT-CODE.\n036704     MOVE 9999 TO Z-EXIT-LEVEL.\n036706     IF Z-FLINFO11-ABSENT\n036708         NEXT SENTENCE ELSE\n036710         GO TO Z-5-4-1-ELSE.\n036712     MOVE \"NO CUSTOMER INFORMATION FOR BK \" TO Z-DISP-FIELD-2-1.\n036714     MOVE WS-BANK-NO TO Z-DISP-FIELD-2-2.\n036716     DISPLAY Z-DISP-FORMAT-2.\n036718     MOVE 1 TO Z-EXIT-LEVEL.\n036720     MOVE 1 TO Z-EXIT-CODE.\n036722     GO TO Z-5-3-END.\n036724 Z-5-4-1-ELSE.\n036726********* NEXT WHEN\n036728     IF TDAC-TIN-NBR = 0 OR 999999999\n036730        NEXT SENTENCE\n036732     ELSE\n036734        GO TO Z-5-7-NEXT-SKIP.\n036736     MOVE 1 TO Z-EXIT-LEVEL\n036738     GO TO Z-5-3-END.\n036740 Z-5-7-NEXT-SKIP.\n036742     MOVE TDAC-BANK OF TDACUST TO TDB-TDAC-BANK OF TDB-TDACUST.\n036744     MOVE TDAC-CUST OF TDACUST TO TDB-TDAC-CUST OF TDB-TDACUST.\n036746     MOVE TDAC-BRCH OF TDACUST TO TDB-TDAC-BRCH OF TDB-TDACUST.\n036748     MOVE TDAC-STATUS OF TDACUST TO TDB-TDAC-STATUS OF            \n036750         TDB-TDACUST.\n036752     MOVE TDAC-NAME-1 OF TDACUST TO TDB-TDAC-NAME-1 OF            \n036754         TDB-TDACUST.\n036756     MOVE TDAC-N1-KEY OF TDACUST TO TDB-TDAC-N1-KEY OF            \n036758         TDB-TDACUST.\n036760     MOVE TDAC-N1-FIRST OF TDACUST TO TDB-TDAC-N1-FIRST OF        \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    467 lines from 17910 to 18376.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 37, "total_chunks": 55, "start_line": 17910, "end_line": 18376, "line_count": 467}

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
- Source code length: 27271 characters

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
CHUNK 37 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 17910 to 18376 (467 lines)
Chunk Tokens (estimated): ~8,068
Actual Input Tokens: 9,474 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 17910-18376 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 37 of 55 chunks
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
      The source code below is only CHUNK 37 of 55.


=============================================================================
CHUNK 37 SOURCE CODE (Lines 17910-18376)
=============================================================================

```cobol
035828         HOLD-TDAPCR.
035830     MOVE TDAPC-SPECS OF TDAPCR TO HOLD-TDAPC-SPECS OF            
035832         HOLD-TDAPCR.
035834     MOVE TDAPC-COPIES OF TDAPCR TO HOLD-TDAPC-COPIES OF          
035836         HOLD-TDAPCR.
035838     MOVE TDAPC-LASER-PRT OF TDAPCR TO HOLD-TDAPC-LASER-PRT OF    
035840         HOLD-TDAPCR.
035842     MOVE TDAPC-FICHE-PRT OF TDAPCR TO HOLD-TDAPC-FICHE-PRT OF    
035844         HOLD-TDAPCR.
035846     MOVE TDAPC-OPTICAL OF TDAPCR TO HOLD-TDAPC-OPTICAL OF        
035848         HOLD-TDAPCR.
035850     MOVE TDAPC-PRT-DLY OF TDAPCR TO HOLD-TDAPC-PRT-DLY OF        
035852         HOLD-TDAPCR.
035854     MOVE TDAPC-DLY-IND OF TDAPCR TO HOLD-TDAPC-DLY-IND OF        
035856         HOLD-TDAPCR.
035858     MOVE TDAPC-LST-PRT-D OF TDAPCR TO HOLD-TDAPC-LST-PRT-D OF    
035860         HOLD-TDAPCR.
035862     MOVE TDAPC-PRT-WK OF TDAPCR TO HOLD-TDAPC-PRT-WK OF          
035864         HOLD-TDAPCR.
035866     MOVE TDAPC-WK-IND OF TDAPCR TO HOLD-TDAPC-WK-IND OF          
035868         HOLD-TDAPCR.
035870     MOVE TDAPC-LST-PRT-W OF TDAPCR TO HOLD-TDAPC-LST-PRT-W OF    
035872         HOLD-TDAPCR.
035874     MOVE TDAPC-PRT-MTH OF TDAPCR TO HOLD-TDAPC-PRT-MTH OF        
035876         HOLD-TDAPCR.
035878     MOVE TDAPC-LST-DAY-M OF TDAPCR TO HOLD-TDAPC-LST-DAY-M OF    
035880         HOLD-TDAPCR.
035882     MOVE TDAPC-NXT-PRT-M OF TDAPCR TO HOLD-TDAPC-NXT-PRT-M OF    
035884         HOLD-TDAPCR.
035886     MOVE TDAPC-LST-PRT-M OF TDAPCR TO HOLD-TDAPC-LST-PRT-M OF    
035888         HOLD-TDAPCR.
035890     MOVE TDAPC-PRT-QTR OF TDAPCR TO HOLD-TDAPC-PRT-QTR OF        
035892         HOLD-TDAPCR.
035894     MOVE TDAPC-LST-DAY-Q OF TDAPCR TO HOLD-TDAPC-LST-DAY-Q OF    
035896         HOLD-TDAPCR.
035898     MOVE TDAPC-NXT-PRT-Q OF TDAPCR TO HOLD-TDAPC-NXT-PRT-Q OF    
035900         HOLD-TDAPCR.
035902     MOVE TDAPC-LST-PRT-Q OF TDAPCR TO HOLD-TDAPC-LST-PRT-Q OF    
035904         HOLD-TDAPCR.
035906     MOVE TDAPC-PRT-YR OF TDAPCR TO HOLD-TDAPC-PRT-YR OF          
035908         HOLD-TDAPCR.
035910     MOVE TDAPC-NXT-PRT-Y OF TDAPCR TO HOLD-TDAPC-NXT-PRT-Y OF    
035912         HOLD-TDAPCR.
035914     MOVE TDAPC-LST-PRT-Y OF TDAPCR TO HOLD-TDAPC-LST-PRT-Y OF    
035916         HOLD-TDAPCR.
035918     MOVE TDAPC-SPECL-REQ OF TDAPCR TO HOLD-TDAPC-SPECL-REQ OF    
035920         HOLD-TDAPCR.
035922     MOVE TDAPC-PRT-DAY OF TDAPCR TO HOLD-TDAPC-PRT-DAY OF        
035924         HOLD-TDAPCR.
035926     MOVE TDAPC-BEGIN-DATE OF TDAPCR TO HOLD-TDAPC-BEGIN-DATE OF  
035928         HOLD-TDAPCR.
035930     MOVE TDAPC-END-DATE OF TDAPCR TO HOLD-TDAPC-END-DATE OF      
035932         HOLD-TDAPCR.
035934     MOVE TDAPC-PRINTER OF TDAPCR TO HOLD-TDAPC-PRINTER OF        
035936         HOLD-TDAPCR.
035938     MOVE TDAPC-SPECL-SPECS OF TDAPCR TO HOLD-TDAPC-SPECL-SPECS   
035940         OF HOLD-TDAPCR.
035942     MOVE TDAPC-REQUESTOR OF TDAPCR TO HOLD-TDAPC-REQUESTOR OF    
035944         HOLD-TDAPCR.
035946     MOVE TDAPC-LPROCESS-DT OF TDAPCR TO HOLD-TDAPC-LPROCESS-DT   
035948         OF HOLD-TDAPCR.
035950     MOVE TDAPC-LUPD-DT OF TDAPCR TO HOLD-TDAPC-LUPD-DT OF        
035952         HOLD-TDAPCR.
035954     MOVE TDAPC-LUPD-TM OF TDAPCR TO HOLD-TDAPC-LUPD-TM OF        
035956         HOLD-TDAPCR.
035958     MOVE TDAPC-BP-LAST-RUN OF TDAPCR TO HOLD-TDAPC-BP-LAST-RUN   
035960         OF HOLD-TDAPCR.
035962     MOVE TDAPC-PUB-ID OF TDAPCR TO HOLD-TDAPC-PUB-ID OF          
035964         HOLD-TDAPCR.
035966     MOVE TDAPC-BANK-SPECS OF TDAPCR TO HOLD-TDAPC-BANK-SPECS OF  
035968         HOLD-TDAPCR.
035970     MOVE ZEROS TO BANK-BR-3 OF BANK-REC.
035972     MOVE ZEROS TO BANK-CSI-BR-CODE OF BANK-REC.
035974     MOVE SPACES TO BANK-NAME OF BANK-REC.
035976     MOVE SPACES TO BANK-ADDR OF BANK-REC.
035978     MOVE SPACES TO BANK-ADDR-2 OF BANK-REC.
035980     MOVE SPACES TO BANK-FED-ID OF BANK-REC.
035982     MOVE ZEROS TO BANK-INT-JRNL-BR-PRT OF BANK-REC.
035984     MOVE SPACES TO BANK-CK-PRT-FORMAT OF BANK-REC.
035986     MOVE SPACES TO BANK-RESTRICT-REDEMP-TICKET OF BANK-REC.
035988     MOVE SPACES TO BANK-CK-PRT-ACCTNO OF BANK-REC.
035990     MOVE SPACES TO BANK-RESTRICT-RATE-PRT OF BANK-REC.
035992     MOVE SPACES TO BANK-CK-PROTECT OF BANK-REC.
035994     MOVE ZEROS TO BANK-SP-CK-REMARK OF BANK-REC.
035996     MOVE ZEROS TO BANK-APPL OF BANK-REC.
035998     MOVE SPACES TO BANK-RMT-IND OF BANK-REC.
036000     MOVE SPACES TO BANK-STATUS OF BANK-REC.
036002     MOVE SPACES TO BANK-TDA-PILOT OF BANK-REC.
036004     MOVE ZEROS TO BANK-PHN-AREA OF BANK-REC.
036006     MOVE ZEROS TO BANK-PHN-PREFIX OF BANK-REC.
036008     MOVE ZEROS TO BANK-PHN-SUFFIX OF BANK-REC.
036010     MOVE ZEROS TO BANK-IRA-PHN-AREA OF BANK-REC.
036012     MOVE ZEROS TO BANK-IRA-PHN-PREFIX OF BANK-REC.
036014     MOVE ZEROS TO BANK-IRA-PHN-SUFFIX OF BANK-REC.
036016     MOVE SPACES TO BANK-EOY-IRA-STMT OF BANK-REC.
036018     MOVE SPACES TO BANK-EOY-IRA-STMT-EARLY OF BANK-REC.
036020     MOVE SPACES TO BANK-EOY-IRA-STMT-PRINT OF BANK-REC.
036022     MOVE ZEROS TO BANK-EOY-DELETE-DATE OF BANK-REC.
036024     MOVE ZEROS TO BANK-EOY-APRIL-DATE OF BANK-REC.
036026     MOVE ZEROS TO BANK-EOY-APRIL-DATE-CCYY OF BANK-REC.
036028     MOVE ZEROS TO BANK-EOY-APRIL-DATE-MMDD OF BANK-REC.
036030     MOVE ZEROS TO BANK-EOY-EARLY-DATE OF BANK-REC.
036032     MOVE ZEROS TO BANK-EOY-NO-IRA-STMTS OF BANK-REC.
036034     MOVE SPACES TO BANK-EOY-RETURN-TO-BANK OF BANK-REC.
036036     MOVE SPACES TO BANK-EOY-EARLY-RUN OF BANK-REC.
036038     MOVE SPACES TO BANK-EOY-RPT-SEQ OF BANK-REC.
036040     MOVE SPACES TO BANK-EOY-IRA-FICHE OF BANK-REC.
036042     MOVE SPACES TO BANK-EOY-IRA-PAPER OF BANK-REC.
036044     MOVE ZEROS TO BANK-NO-IRA-STMTS OF BANK-REC.
036046     MOVE SPACES TO BANK-OPT-HOL OF BANK-REC.
036048     MOVE SPACES TO BANK-CK21-TDA OF BANK-REC.
036050     MOVE SPACES TO BANK-DQVISTA OF BANK-REC.
036052     MOVE SPACES TO BANK-MSI OF BANK-REC.
036054     MOVE SPACES TO BANK-MSI-OV-TDA OF BANK-REC.
036056     MOVE SPACES TO BANK-BK-IMG-SERV OF BANK-REC.
036058     MOVE SPACES TO BANK-FM-SUPPRESS OF BANK-REC.
036060     MOVE SPACES TO BANK-EOY-COD-CLOSED-RPT OF BANK-REC.
036062     MOVE SPACES TO BANK-PRT-NEW OF BANK-REC.
036064     MOVE SPACES TO BANK-IMONITOR OF BANK-REC.
036066     MOVE SPACES TO BANK-CENTERVIEW OF BANK-REC.
036068     MOVE SPACES TO BANK-TDA-ADD-DAY OF BANK-REC.
036070     MOVE 1 TO Z-II.
036072 Z-4-5-1-LOOP.
036074     IF Z-II > 18
036076         GO TO Z-4-5-1-LOOP-XIT.
036078     MOVE SPACES TO BANK-HOL-MM OF BANK-REC (Z-II).
036080     MOVE SPACES TO BANK-HOL-DD OF BANK-REC (Z-II).
036082     ADD 1 TO Z-II.
036084     GO TO Z-4-5-1-LOOP.
036086 Z-4-5-1-LOOP-XIT.
036088     MOVE ZEROS TO BANK-CREATE-DT OF BANK-REC.
036090     MOVE ZEROS TO BANK-CREATE-TM OF BANK-REC.
036092     MOVE SPACES TO BANK-ENTC-TDA OF BANK-REC.
036094     MOVE SPACES TO BANK-EV-3RD-PARTY-1 OF BANK-REC.
036096     MOVE SPACES TO BANK-EV-3RD-PARTY-2 OF BANK-REC.
036098     MOVE SPACES TO BANK-HSA-LOCATION OF BANK-REC.
036100     MOVE SPACES TO BANK-PROFITABILITY OF BANK-REC.
036102     MOVE SPACES TO BANK-BANCVUE OF BANK-REC.
036104     MOVE SPACES TO BANK-SPECIAL-DL-BILLING OF BANK-REC.
036106     MOVE SPACES TO BANK-WEB-ENABLED OF BANK-REC.
036108     MOVE ZEROS TO BANK-CIF-NAME-ADDR OF BANK-REC.
036110     MOVE SPACES TO BANK-MAIL-ADDR-LINES OF BANK-REC.
036112     MOVE ZEROS TO BANK-BRANCH-LENGTH OF BANK-REC.
036114     MOVE ZEROS TO BANK-LOB OF BANK-REC.
036116     MOVE ZEROS TO BANK-LAST-EOM-PROC OF BANK-REC.
036118     MOVE SPACES TO BANK-TRAIN-BK-FLG OF BANK-REC.
036120     MOVE SPACES TO BANK-EOY-CIB-F-MERD OF BANK-REC.
036122     MOVE ZEROS TO SPECS-GRACE-IN-PROC OF SPECS-AREA.
036124     MOVE ZEROS TO SPECS-GRACE-CLOSE OF SPECS-AREA.
036126     MOVE ZEROS TO SPECS-PRE-MAT OF SPECS-AREA.
036128     MOVE SPACES TO SPECS-LSR-PILOT OF SPECS-AREA.
036130     MOVE ZEROS TO SPECS-CHK-RECON OF SPECS-AREA.
036132     MOVE SPACES TO SPECS-BR-ADDR OF SPECS-AREA.
036134     MOVE SPACES TO SPECS-TIN-SUPPRESS OF SPECS-AREA.
036136     MOVE SPACES TO SPECS-NO-IN-PROC OF SPECS-AREA.
036138     MOVE SPACES TO SPECS-RMD-OVERRIDE OF SPECS-AREA.
036140     MOVE SPACES TO SPECS-PPP-PILOT OF SPECS-AREA.
036142     MOVE SPACES TO SPECS-RETURN-ENVELOPE OF SPECS-AREA.
036144     MOVE SPACES TO SPECS-LSTCONT-DDACOMB OF SPECS-AREA.
036146     MOVE SPACES TO SPECS-LSTCONT-TDASTMT OF SPECS-AREA.
036148     MOVE SPACES TO SPECS-LSTCONT-INTNTC OF SPECS-AREA.
036150     MOVE SPACES TO SPECS-LSTCONT-ALLNTC OF SPECS-AREA.
036152     MOVE SPACES TO SPECS-LSTCONT-CHECKS OF SPECS-AREA.
036154     MOVE SPACES TO SPECS-LSTCONT-DISTREC OF SPECS-AREA.
036156     MOVE SPACES TO SPECS-COMB-AUTO-RMD-ADJUST OF SPECS-AREA.
036158     MOVE ZEROS TO SPECS-IGL-HIGH-BAL OF SPECS-AREA.
036160     MOVE SPACES TO SPECS-AVAIL-CAP-INT OF SPECS-AREA.
036162     MOVE ZEROS TO SPECS-CNV-TOT-DNLOAD OF SPECS-AREA.
036164     MOVE SPACES TO SPECS-CNV-TOT-DNLOAD-X OF SPECS-AREA.
036166     MOVE ZEROS TO SPECS-ADDR-ALERT-DAYS OF SPECS-AREA.
036168     MOVE SPACES TO SPECS-COMB-SEND-CERT OF SPECS-AREA.
036170     MOVE SPACES TO SPECS-APPLY-GRACE-AT-SR OF SPECS-AREA.
036172     MOVE SPACES TO SPECS-DB-SUFFIX OF SPECS-AREA.
036174     MOVE SPACES TO SPECS-EOY-YTD-ROLL OF SPECS-AREA.
036176     MOVE SPACES TO SPECS-COMB-DDA-OPT OF SPECS-AREA.
036178     MOVE SPACES TO SPECS-CONTINUE OF SPECS-AREA.
036180     MOVE TDAPC-SPECS TO SPECS-AREA.
036182     MOVE TDAPC-BANK-SPECS TO TDB-TDAPC-BANK-SPECS.
036184     MOVE TDB-TDAPC-CSI-BR-CODE OF TDB-TDAPC-BANK-SPECS-R TO      
036186         BANK-CSI-BR-CODE OF BANK-REC.
036188     MOVE TDB-TDAPC-FED-ID OF TDB-TDAPC-BANK-SPECS-R TO           
036190         BANK-FED-ID OF BANK-REC.
036192     MOVE TDB-TDAPC-RMT-IND OF TDB-TDAPC-BANK-SPECS-R TO          
036194         BANK-RMT-IND OF BANK-REC.
036196     MOVE TDB-TDAPC-TDA-PILOT OF TDB-TDAPC-BANK-SPECS-R TO        
036198         BANK-TDA-PILOT OF BANK-REC.
036200     MOVE TDB-TDAPC-EOY-IRA-STMT OF TDB-TDAPC-BANK-SPECS-R TO     
036202         BANK-EOY-IRA-STMT OF BANK-REC.
036204     MOVE TDB-TDAPC-EOY-IRA-STMT-EARLY OF TDB-TDAPC-BANK-SPECS-R  
036206         TO BANK-EOY-IRA-STMT-EARLY OF BANK-REC.
036208     MOVE TDB-TDAPC-EOY-IRA-STMT-PRINT OF TDB-TDAPC-BANK-SPECS-R  
036210         TO BANK-EOY-IRA-STMT-PRINT OF BANK-REC.
036212     MOVE TDB-TDAPC-EOY-DELETE-DATE OF TDB-TDAPC-BANK-SPECS-R TO  
036214         BANK-EOY-DELETE-DATE OF BANK-REC.
036216     MOVE TDB-TDAPC-EOY-APRIL-DATE OF TDB-TDAPC-BANK-SPECS-R TO   
036218         BANK-EOY-APRIL-DATE OF BANK-REC.
036220     MOVE TDB-TDAPC-EOY-EARLY-DATE OF TDB-TDAPC-BANK-SPECS-R TO   
036222         BANK-EOY-EARLY-DATE OF BANK-REC.
036224     MOVE TDB-TDAPC-EOY-RETURN-TO-BANK OF TDB-TDAPC-BANK-SPECS-R  
036226         TO BANK-EOY-RETURN-TO-BANK OF BANK-REC.
036228     MOVE TDB-TDAPC-EOY-EARLY-RUN OF TDB-TDAPC-BANK-SPECS-R TO    
036230         BANK-EOY-EARLY-RUN OF BANK-REC.
036232     MOVE TDB-TDAPC-EOY-RPT-SEQ OF TDB-TDAPC-BANK-SPECS-R TO      
036234         BANK-EOY-RPT-SEQ OF BANK-REC.
036236     MOVE TDB-TDAPC-EOY-IRA-FICHE OF TDB-TDAPC-BANK-SPECS-R TO    
036238         BANK-EOY-IRA-FICHE OF BANK-REC.
036240     MOVE TDB-TDAPC-EOY-IRA-PAPER OF TDB-TDAPC-BANK-SPECS-R TO    
036242         BANK-EOY-IRA-PAPER OF BANK-REC.
036244     MOVE TDB-TDAPC-NO-IRA-STMTS OF TDB-TDAPC-BANK-SPECS-R TO     
036246         BANK-NO-IRA-STMTS OF BANK-REC.
036248     MOVE TDB-TDAPC-CK21-TDA OF TDB-TDAPC-BANK-SPECS-R TO         
036250         BANK-CK21-TDA OF BANK-REC.
036252     MOVE TDB-TDAPC-DQVISTA OF TDB-TDAPC-BANK-SPECS-R TO          
036254         BANK-DQVISTA OF BANK-REC.
036256     MOVE TDB-TDAPC-MSI OF TDB-TDAPC-BANK-SPECS-R TO BANK-MSI OF  
036258         BANK-REC.
036260     MOVE TDB-TDAPC-MSI-OV-TDA OF TDB-TDAPC-BANK-SPECS-R TO       
036262         BANK-MSI-OV-TDA OF BANK-REC.
036264     MOVE TDB-TDAPC-BK-IMG-SERV OF TDB-TDAPC-BANK-SPECS-R TO      
036266         BANK-BK-IMG-SERV OF BANK-REC.
036268     MOVE TDB-TDAPC-FM-SUPPRESS OF TDB-TDAPC-BANK-SPECS-R TO      
036270         BANK-FM-SUPPRESS OF BANK-REC.
036272     MOVE TDB-TDAPC-EOY-COD-CLOSED-RPT OF TDB-TDAPC-BANK-SPECS-R  
036274         TO BANK-EOY-COD-CLOSED-RPT OF BANK-REC.
036276     MOVE TDB-TDAPC-PRT-NEW OF TDB-TDAPC-BANK-SPECS-R TO          
036278         BANK-PRT-NEW OF BANK-REC.
036280     MOVE TDB-TDAPC-IMONITOR OF TDB-TDAPC-BANK-SPECS-R TO         
036282         BANK-IMONITOR OF BANK-REC.
036284     MOVE TDB-TDAPC-TDA-ADD-DAY OF TDB-TDAPC-BANK-SPECS-R TO      
036286         BANK-TDA-ADD-DAY OF BANK-REC.
036288     MOVE 1 TO Z-II.
036290 Z-4-9-1-LOOP.
036292     IF Z-II > 18
036294         GO TO Z-4-9-1-LOOP-XIT.
036296     MOVE TDB-TDAPC-HOL-MM OF TDB-TDAPC-BANK-SPECS-R (Z-II) TO    
036298         BANK-HOL-MM OF BANK-REC (Z-II).
036300     MOVE TDB-TDAPC-HOL-DD OF TDB-TDAPC-BANK-SPECS-R (Z-II) TO    
036302         BANK-HOL-DD OF BANK-REC (Z-II).
036304     ADD 1 TO Z-II.
036306     GO TO Z-4-9-1-LOOP.
036308 Z-4-9-1-LOOP-XIT.
036310     MOVE TDB-TDAPC-CREATE-DT OF TDB-TDAPC-BANK-SPECS-R TO        
036312         BANK-CREATE-DT OF BANK-REC.
036314     MOVE TDB-TDAPC-CREATE-TM OF TDB-TDAPC-BANK-SPECS-R TO        
036316         BANK-CREATE-TM OF BANK-REC.
036318     MOVE TDB-TDAPC-ENTC-TDA OF TDB-TDAPC-BANK-SPECS-R TO         
036320         BANK-ENTC-TDA OF BANK-REC.
036322     MOVE TDB-TDAPC-EV-3RD-PARTY-1 OF TDB-TDAPC-BANK-SPECS-R TO   
036324         BANK-EV-3RD-PARTY-1 OF BANK-REC.
036326     MOVE TDB-TDAPC-EV-3RD-PARTY-2 OF TDB-TDAPC-BANK-SPECS-R TO   
036328         BANK-EV-3RD-PARTY-2 OF BANK-REC.
036330     MOVE TDB-TDAPC-HSA-LOCATION OF TDB-TDAPC-BANK-SPECS-R TO     
036332         BANK-HSA-LOCATION OF BANK-REC.
036334     MOVE TDB-TDAPC-PROFITABILITY OF TDB-TDAPC-BANK-SPECS-R TO    
036336         BANK-PROFITABILITY OF BANK-REC.
036338     MOVE TDB-TDAPC-BANCVUE OF TDB-TDAPC-BANK-SPECS-R TO          
036340         BANK-BANCVUE OF BANK-REC.
036342     MOVE TDB-TDAPC-SPECIAL-DL-BILLING OF TDB-TDAPC-BANK-SPECS-R  
036344         TO BANK-SPECIAL-DL-BILLING OF BANK-REC.
036346     MOVE TDB-TDAPC-WEB-ENABLED OF TDB-TDAPC-BANK-SPECS-R TO      
036348         BANK-WEB-ENABLED OF BANK-REC.
036350     MOVE TDB-TDAPC-CIF-NAME-ADDR OF TDB-TDAPC-BANK-SPECS-R TO    
036352         BANK-CIF-NAME-ADDR OF BANK-REC.
036354     MOVE TDB-TDAPC-MAIL-ADDR-LINES OF TDB-TDAPC-BANK-SPECS-R TO  
036356         BANK-MAIL-ADDR-LINES OF BANK-REC.
036358     MOVE TDB-TDAPC-BRANCH-LENGTH OF TDB-TDAPC-BANK-SPECS-R TO    
036360         BANK-BRANCH-LENGTH OF BANK-REC.
036362     MOVE TDB-TDAPC-LOB OF TDB-TDAPC-BANK-SPECS-R TO BANK-LOB OF  
036364         BANK-REC.
036366     MOVE TDB-TDAPC-LAST-EOM-PROC OF TDB-TDAPC-BANK-SPECS-R TO    
036368         BANK-LAST-EOM-PROC OF BANK-REC.
036370     MOVE TDB-TDAPC-TRAIN-BK-FLG OF TDB-TDAPC-BANK-SPECS-R TO     
036372         BANK-TRAIN-BK-FLG OF BANK-REC.
036374     MOVE TDB-TDAPC-EOY-CIB-F-MERD OF TDB-TDAPC-BANK-SPECS-R TO   
036376         BANK-EOY-CIB-F-MERD OF BANK-REC.
036378     MOVE TDAPC-RPT-DESC TO BANK-NAME.
036380     IF ( WS-SPECS-BANK-DATE > BANK-CREATE-DT ) OR ( (            
036382         WS-SPECS-BANK-DATE = BANK-CREATE-DT ) AND (              
036384         WS-SPECS-BANK-TIME > BANK-CREATE-TM ) )
036386         NEXT SENTENCE ELSE
036388         GO TO Z-4-11-1-ELSE.
036390*
036392******* OPEN FILE BK-SPEC-FILE
036394*
036396     IF Z-FLINFO3-OPEN = 0
036398         CHANGE ATTRIBUTE DEPENDENTSPECS OF BK-SPEC-FILE TO TRUE 
036400         OPEN INPUT BK-SPEC-FILE 
036402         IF ATTRIBUTE FILESTATE OF BK-SPEC-FILE = VALUE OPENED
036404             MOVE ZEROS TO Z-FILE3-KEY
036406             MOVE ZEROS TO Z-FLINFO3-RS-KEY
036408             MOVE 1 TO Z-FLINFO3-OPEN
036410             MOVE 1 TO Z-FLINFO3-RS-OPEN
036412         ELSE
036414             DISPLAY ">>> FILE BK-SPEC-FILE FAILED TO OPEN"
036416             MOVE ATTRIBUTE TITLE OF BK-SPEC-FILE TO              
036418                 Z-FL-EXCEPT-TITLE
036420             DISPLAY ">>> OPEN FAIL, TITLE :", Z-FL-EXCEPT-TITLE
036422             DISPLAY ">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS".
036424*
036426******* OPEN FILE BK-SPEC-FILE
036428*
036430     IF Z-FLINFO3-OPEN = 0
036432         CHANGE ATTRIBUTE DEPENDENTSPECS OF BK-SPEC-FILE TO TRUE 
036434         OPEN INPUT BK-SPEC-FILE 
036436         IF ATTRIBUTE FILESTATE OF BK-SPEC-FILE = VALUE OPENED
036438             MOVE ZEROS TO Z-FILE3-KEY
036440             MOVE ZEROS TO Z-FLINFO3-RS-KEY
036442             MOVE 1 TO Z-FLINFO3-OPEN
036444             MOVE 1 TO Z-FLINFO3-RS-OPEN
036446         ELSE
036448             DISPLAY ">>> FILE BK-SPEC-FILE FAILED TO OPEN"
036450             MOVE ATTRIBUTE TITLE OF BK-SPEC-FILE TO              
036452                 Z-FL-EXCEPT-TITLE
036454             DISPLAY ">>> OPEN FAIL, TITLE :", Z-FL-EXCEPT-TITLE
036456             DISPLAY ">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS".
036458     MOVE ZERO TO Z-FLINFO3-PRES.
036460     MOVE ZERO TO Z-FLINFO3-SOME.
036462     MOVE 7 TO Z-FLINFO3-LAST-SEQ.
036464*
036466 Z-4-13-LOOP.
036468     MOVE ZERO TO Z-FLINFO3-PRES.
036470*
036472 Z-4-13-READ.
036474     READ BK-SPEC-FILE RECORD 
036476         AT END
036478         GO TO Z-4-13-XIT.
036480     MOVE Z-FILE3-KEY TO Z-FLINFO3-RS-KEY.
036482*
036484     IF SPEC-BK-NO-9-4-N = WS-BANK-NO
036486         NEXT SENTENCE ELSE
036488         MOVE 1 TO Z-EXIT-LEVEL
036490         GO TO Z-4-13-END.
036492*
036494     MOVE 1 TO Z-FLINFO3-PRES.
036496     MOVE 1 TO Z-FLINFO3-SOME.
036498     MOVE 1 TO Z-FLINFO3-MODIFY.
036500     MOVE 0 TO Z-EXIT-CODE.
036502     MOVE 9999 TO Z-EXIT-LEVEL.
036504     IF SPEC-SEQ-NO-N = 01
036506         NEXT SENTENCE ELSE
036508         GO TO Z-4-14-1-ELSE.
036510     MOVE SPEC-BK-NAME-N TO RMD-BK-NAME.
036512     MOVE SPEC-BK-NO-9-4-N TO RMD-BK.
036514     GO TO Z-4-14-ENDIF.
036516 Z-4-14-1-ELSE.
036518     IF SPEC-SEQ-NO-N = 02
036520         NEXT SENTENCE ELSE
036522         GO TO Z-4-14-2-ELSE.
036524     MOVE SPEC-BR-NO-N TO RMD-DC.
036526     GO TO Z-4-14-ENDIF.
036528 Z-4-14-2-ELSE.
036530     IF SPEC-SEQ-NO-N = 04
036532         NEXT SENTENCE ELSE
036534         GO TO Z-4-14-3-ELSE.
036536     MOVE SPEC-RMT-BK-INDICATOR-N TO BANK-RMT-IND.
036538     MOVE 1 TO Z-EXIT-LEVEL.
036540     MOVE 1 TO Z-EXIT-CODE.
036542     GO TO Z-4-13-END.
036544 Z-4-14-3-ELSE.
036546 Z-4-14-ENDIF.
036548 Z-4-13-END.
036550     IF Z-EDIT-ERROR
036552         GO TO Z-4-XIT.
036554 Z-4-13-SKIP.
036556     IF Z-EXIT-LEVEL < 1
036558         GO TO Z-4-END.
036560     IF Z-EXIT-CODE > 0
036562         GO TO Z-4-13-XIT.
036564     GO TO Z-4-13-LOOP.
036566*
036568 Z-4-13-XIT.
036570     MOVE 0 TO Z-EXIT-CODE.
036572     MOVE 9999 TO Z-EXIT-LEVEL.
036574*
036576***********  CLOSE OF FILE BK-SPEC-FILE WITH RELEASE
036578*
036580     IF Z-FLINFO3-OPEN NOT = 0
036582         CLOSE BK-SPEC-FILE WITH RELEASE
036584         MOVE 0 TO Z-FLINFO3-OPEN
036586         MOVE 0 TO Z-FLINFO3-RS-OPEN.
036588     GO TO Z-4-11-ENDIF.
036590 Z-4-11-1-ELSE.
036592     MOVE BANK-NAME TO RMD-BK-NAME.
036594     MOVE PROC-BANK TO RMD-BK.
036596     MOVE BANK-CSI-BR-CODE TO RMD-DC.
036598 Z-4-11-ENDIF.
036600 Z-4-END.
036602     IF Z-EDIT-ERROR
036604         GO TO Z-4-XIT.
036606 Z-4-SKIP.
036608     IF Z-EXIT-LEVEL NOT < 0
036610         MOVE 0 TO Z-EXIT-CODE
036612         MOVE 9999 TO Z-EXIT-LEVEL.
036614 Z-4-XIT.
036616     EXIT.
036618*
036620*****************************************************************
036622*    PROCEDURE GET-ACCT-INFO
036624*****************************************************************
036626 Z-5-PROCEDURE.
036628*
036630     MOVE 0 TO Z-EXIT-CODE.
036632     MOVE 9999 TO Z-EXIT-LEVEL.
036634     MOVE SPACES TO WS-TIN-CUST-TABLE
036636       , WS-TIN-DETAIL-TABLE.
036638     MOVE 0 TO WS-TIN-DISTR-RECS.
036640     MOVE ZERO TO Z-FLINFO11-PRES.
036642     MOVE ZERO TO Z-FLINFO11-SOME.
036644     MOVE 8 TO Z-FLINFO11-LAST-SEQ.
036646*
036648     SET TDATINSET OF TDACUST OF LDBTDADB TO BEGINNING
036650         ON EXCEPTION
036652         MOVE "TDATINSET OF TDACUST OF LDBTDADB" TO               
036654             Z-DMS-EXCEPT-STR
036656         MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
036658         MOVE 8 TO Z-DMS-EXCEPT-SEQ
036660         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT
036662         GO TO Z-5-3-XIT.
036664 Z-5-3-LOOP.
036666     MOVE ZERO TO Z-FLINFO11-PRES.
036668 Z-5-3-READ.
036670     FIND TDACUST OF LDBTDADB VIA NEXT TDATINSET OF TDACUST OF    
036672         LDBTDADB
036674     AT TDAC-BANK = WS-BANK-NO
036676         ON EXCEPTION
036678         MOVE 8 TO Z-DMS-EXCEPT-SEQ
036680         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
036682             GO TO Z-5-3-XIT
036684         ELSE
036686             MOVE "TDATINSET OF TDACUST OF LDBTDADB" TO           
036688                 Z-DMS-EXCEPT-STR
036690             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
036692             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
036694
036696*
036698     MOVE 1 TO Z-FLINFO11-PRES.
036700     MOVE 1 TO Z-FLINFO11-SOME.
036702     MOVE 0 TO Z-EXIT-CODE.
036704     MOVE 9999 TO Z-EXIT-LEVEL.
036706     IF Z-FLINFO11-ABSENT
036708         NEXT SENTENCE ELSE
036710         GO TO Z-5-4-1-ELSE.
036712     MOVE "NO CUSTOMER INFORMATION FOR BK " TO Z-DISP-FIELD-2-1.
036714     MOVE WS-BANK-NO TO Z-DISP-FIELD-2-2.
036716     DISPLAY Z-DISP-FORMAT-2.
036718     MOVE 1 TO Z-EXIT-LEVEL.
036720     MOVE 1 TO Z-EXIT-CODE.
036722     GO TO Z-5-3-END.
036724 Z-5-4-1-ELSE.
036726********* NEXT WHEN
036728     IF TDAC-TIN-NBR = 0 OR 999999999
036730        NEXT SENTENCE
036732     ELSE
036734        GO TO Z-5-7-NEXT-SKIP.
036736     MOVE 1 TO Z-EXIT-LEVEL
036738     GO TO Z-5-3-END.
036740 Z-5-7-NEXT-SKIP.
036742     MOVE TDAC-BANK OF TDACUST TO TDB-TDAC-BANK OF TDB-TDACUST.
036744     MOVE TDAC-CUST OF TDACUST TO TDB-TDAC-CUST OF TDB-TDACUST.
036746     MOVE TDAC-BRCH OF TDACUST TO TDB-TDAC-BRCH OF TDB-TDACUST.
036748     MOVE TDAC-STATUS OF TDACUST TO TDB-TDAC-STATUS OF            
036750         TDB-TDACUST.
036752     MOVE TDAC-NAME-1 OF TDACUST TO TDB-TDAC-NAME-1 OF            
036754         TDB-TDACUST.
036756     MOVE TDAC-N1-KEY OF TDACUST TO TDB-TDAC-N1-KEY OF            
036758         TDB-TDACUST.
036760     MOVE TDAC-N1-FIRST OF TDACUST TO TDB-TDAC-N1-FIRST OF        
```

⚠️  This is the source code you must document.
    467 lines from 17910 to 18376.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

