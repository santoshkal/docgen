# LLM Request Debug File
Generated: 2025-11-18T19:39:17.574480

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 32/55
- **Model**: gpt-4.1
- **Chunk Number**: 32
- **Pass Number**: 3
- **Attempt Number**: 5 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,086 tokens
- **User Prompt**: ~7,767 tokens
- **Total Input**: ~9,853 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 32/55" (ID: detailed-code-explanation)

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


**CHUNK 32 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T18:05:37.383587", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 32 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 15321 to 15848 (528 lines)\nChunk Tokens (estimated): ~8,085\nActual Input Tokens: 9,491 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 15321-15848 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 32 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 32 of 55.\n\n\n=============================================================================\nCHUNK 32 SOURCE CODE (Lines 15321-15848)\n=============================================================================\n\n```cobol\n030650 Z-8-5-1-ELSE.\n030652     MOVE \"0\" TO GWS-RMT-FICHE-COPIES.\n030654 Z-8-5-ENDIF.\n030656     GO TO Z-8-4-ENDIF.\n030658 Z-8-4-1-ELSE.\n030660     MOVE GWS-MICROFICHE-CODE TO GWS-RMT-FICHE-COPIES.\n030662 Z-8-4-ENDIF.\n030664     IF ( GWS-RMT-DESCRIPTOR = \"TR\" OR \"RJ\" OR \"TS\" ) AND         \n030666         GWS-RPT-TYPE NOT = 1\n030668         NEXT SENTENCE ELSE\n030670         GO TO Z-8-9-1-ELSE.\n030672     MOVE \"B\" TO GWS-RMT-FILE-TYPE.\n030674     GO TO Z-8-9-ENDIF.\n030676 Z-8-9-1-ELSE.\n030678     MOVE \"P\" TO GWS-RMT-FILE-TYPE.\n030680 Z-8-9-ENDIF.\n030682     MOVE PROCESS-DATE TO WS-DATE-CYMD.\n030684     MOVE WS-DATE-DD TO GWS-RMT-DD.\n030686     MOVE \"N\" TO GWS-RMT-APPL.\n030688     MOVE GWS-RMT-EXT TO GWS-RMT-RPT-NO.\n030690     MOVE GWS-PACK TO GWS-RMT-PACK.\n030692     IF (SW3-1) AND (GWS-PRT-PID-FLAG NOT = 2)                    \n030694         MOVE 2 TO GWS-PRT-PID-FLAG                               \n030696         DISPLAY \"ENTER PACK NAME FOR REMOTE PRINT FILES\"         \n030698         ACCEPT GWS-RMT-PACK.                                     \n030700     MOVE \" ON\" TO GWS-RMT-ON.\n030702     MOVE GWS-A12-PERIOD TO GWS-RMT-PERIOD.\n030704     MOVE GWS-RMT-PRT-LABEL TO ID-PRT74-2.\n030706     IF Z-EDIT-ERROR\n030708         GO TO Z-8-XIT.\n030710 Z-8-SKIP.\n030712 Z-8-XIT.\n030714     EXIT.\n030716*\n030718*****************************************************************\n030720*    PROCEDURE READ-SPECS\n030722*****************************************************************\n030724 Z-9-PROCEDURE.\n030726*\n030728     MOVE ZEROS TO BANK-BR-3 OF BANK-REC.\n030730     MOVE ZEROS TO BANK-CSI-BR-CODE OF BANK-REC.\n030732     MOVE SPACES TO BANK-NAME OF BANK-REC.\n030734     MOVE SPACES TO BANK-ADDR OF BANK-REC.\n030736     MOVE SPACES TO BANK-ADDR-2 OF BANK-REC.\n030738     MOVE SPACES TO BANK-FED-ID OF BANK-REC.\n030740     MOVE ZEROS TO BANK-INT-JRNL-BR-PRT OF BANK-REC.\n030742     MOVE SPACES TO BANK-CK-PRT-FORMAT OF BANK-REC.\n030744     MOVE SPACES TO BANK-RESTRICT-REDEMP-TICKET OF BANK-REC.\n030746     MOVE SPACES TO BANK-CK-PRT-ACCTNO OF BANK-REC.\n030748     MOVE SPACES TO BANK-RESTRICT-RATE-PRT OF BANK-REC.\n030750     MOVE SPACES TO BANK-CK-PROTECT OF BANK-REC.\n030752     MOVE ZEROS TO BANK-SP-CK-REMARK OF BANK-REC.\n030754     MOVE ZEROS TO BANK-APPL OF BANK-REC.\n030756     MOVE SPACES TO BANK-RMT-IND OF BANK-REC.\n030758     MOVE SPACES TO BANK-STATUS OF BANK-REC.\n030760     MOVE SPACES TO BANK-TDA-PILOT OF BANK-REC.\n030762     MOVE ZEROS TO BANK-PHN-AREA OF BANK-REC.\n030764     MOVE ZEROS TO BANK-PHN-PREFIX OF BANK-REC.\n030766     MOVE ZEROS TO BANK-PHN-SUFFIX OF BANK-REC.\n030768     MOVE ZEROS TO BANK-IRA-PHN-AREA OF BANK-REC.\n030770     MOVE ZEROS TO BANK-IRA-PHN-PREFIX OF BANK-REC.\n030772     MOVE ZEROS TO BANK-IRA-PHN-SUFFIX OF BANK-REC.\n030774     MOVE SPACES TO BANK-EOY-IRA-STMT OF BANK-REC.\n030776     MOVE SPACES TO BANK-EOY-IRA-STMT-EARLY OF BANK-REC.\n030778     MOVE SPACES TO BANK-EOY-IRA-STMT-PRINT OF BANK-REC.\n030780     MOVE ZEROS TO BANK-EOY-NO-IRA-STMTS OF BANK-REC.\n030782     MOVE SPACES TO BANK-EOY-RETURN-TO-BANK OF BANK-REC.\n030784     MOVE SPACES TO BANK-EOY-EARLY-RUN OF BANK-REC.\n030786     MOVE SPACES TO BANK-EOY-RPT-SEQ OF BANK-REC.\n030788     MOVE SPACES TO BANK-EOY-IRA-FICHE OF BANK-REC.\n030790     MOVE SPACES TO BANK-EOY-IRA-PAPER OF BANK-REC.\n030792     MOVE ZEROS TO BANK-NO-IRA-STMTS OF BANK-REC.\n030794     MOVE SPACES TO BANK-OPT-HOL OF BANK-REC.\n030796     MOVE SPACES TO BANK-CK21-TDA OF BANK-REC.\n030798     MOVE SPACES TO BANK-DQVISTA OF BANK-REC.\n030800     MOVE SPACES TO BANK-MSI OF BANK-REC.\n030802     MOVE SPACES TO BANK-MSI-OV-TDA OF BANK-REC.\n030804     MOVE SPACES TO BANK-BK-IMG-SERV OF BANK-REC.\n030806     MOVE SPACES TO BANK-FM-SUPPRESS OF BANK-REC.\n030808     MOVE SPACES TO BANK-EOY-COD-CLOSED-RPT OF BANK-REC.\n030810     MOVE SPACES TO BANK-PRT-NEW OF BANK-REC.\n030812     MOVE SPACES TO BANK-IMONITOR OF BANK-REC.\n030814     MOVE SPACES TO BANK-CENTERVIEW OF BANK-REC.\n030816     MOVE SPACES TO BANK-TDA-ADD-DAY OF BANK-REC.\n030818     MOVE 1 TO Z-II.\n030820 Z-9-1-1-LOOP.\n030822     IF Z-II > 18\n030824         GO TO Z-9-1-1-LOOP-XIT.\n030826     MOVE SPACES TO BANK-HOL-MM OF BANK-REC (Z-II).\n030828     MOVE SPACES TO BANK-HOL-DD OF BANK-REC (Z-II).\n030830     ADD 1 TO Z-II.\n030832     GO TO Z-9-1-1-LOOP.\n030834 Z-9-1-1-LOOP-XIT.\n030836     MOVE ZEROS TO BANK-CREATE-DT OF BANK-REC.\n030838     MOVE ZEROS TO BANK-CREATE-TM OF BANK-REC.\n030840     MOVE SPACES TO BANK-ENTC-TDA OF BANK-REC.\n030842     MOVE SPACES TO BANK-EV-3RD-PARTY-1 OF BANK-REC.\n030844     MOVE SPACES TO BANK-EV-3RD-PARTY-2 OF BANK-REC.\n030846     MOVE SPACES TO BANK-HSA-LOCATION OF BANK-REC.\n030848     MOVE SPACES TO BANK-PROFITABILITY OF BANK-REC.\n030850     MOVE SPACES TO BANK-BANCVUE OF BANK-REC.\n030852     MOVE SPACES TO BANK-SPECIAL-DL-BILLING OF BANK-REC.\n030854     MOVE SPACES TO BANK-WEB-ENABLED OF BANK-REC.\n030856     MOVE ZEROS TO BANK-CIF-NAME-ADDR OF BANK-REC.\n030858     MOVE SPACES TO BANK-MAIL-ADDR-LINES OF BANK-REC.\n030860     MOVE ZEROS TO BANK-BRANCH-LENGTH OF BANK-REC.\n030862     MOVE ZEROS TO BANK-LOB OF BANK-REC.\n030864     MOVE SPACES TO BANK-TRAIN-BK-FLG OF BANK-REC.\n030866     MOVE SPACES TO BANK-EOY-CIB-F-MERD OF BANK-REC.\n030868*\n030870******* OPEN FILE BK-SPEC-FILE\n030872*\n030874     IF Z-FLINFO3-OPEN = 0\n030876         CHANGE ATTRIBUTE DEPENDENTSPECS OF BK-SPEC-FILE TO TRUE \n030878         OPEN INPUT BK-SPEC-FILE \n030880         IF ATTRIBUTE FILESTATE OF BK-SPEC-FILE = VALUE OPENED\n030882             MOVE ZEROS TO Z-FILE3-KEY\n030884             MOVE ZEROS TO Z-FLINFO3-RS-KEY\n030886             MOVE 1 TO Z-FLINFO3-OPEN\n030888             MOVE 1 TO Z-FLINFO3-RS-OPEN\n030890         ELSE\n030892             DISPLAY \">>> FILE BK-SPEC-FILE FAILED TO OPEN\"\n030894             MOVE ATTRIBUTE TITLE OF BK-SPEC-FILE TO              \n030896                 Z-FL-EXCEPT-TITLE\n030898             DISPLAY \">>> OPEN FAIL, TITLE :\", Z-FL-EXCEPT-TITLE\n030900             DISPLAY \">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS\".\n030902     MOVE ZERO TO Z-FLINFO3-PRES.\n030904     MOVE ZERO TO Z-FLINFO3-SOME.\n030906     MOVE 4 TO Z-FLINFO3-LAST-SEQ.\n030908*\n030910 Z-9-2-LOOP.\n030912     MOVE ZERO TO Z-FLINFO3-PRES.\n030914*\n030916 Z-9-2-READ.\n030918     READ BK-SPEC-FILE RECORD \n030920         AT END\n030922         GO TO Z-9-2-XIT.\n030924     MOVE Z-FILE3-KEY TO Z-FLINFO3-RS-KEY.\n030926*\n030928     MOVE 1 TO Z-FLINFO3-PRES.\n030930     MOVE 1 TO Z-FLINFO3-SOME.\n030932     MOVE 1 TO Z-FLINFO3-MODIFY.\n030934     MOVE 0 TO Z-EXIT-CODE.\n030936     MOVE 9999 TO Z-EXIT-LEVEL.\n030938     IF ( SPEC-BK-NO-9-4-N = 0000 ) AND ( SPEC-SEQ-NO-N = 7 )\n030940         NEXT SENTENCE ELSE\n030942         GO TO Z-9-3-1-ELSE.\n030944     MOVE SPEC-EOY-EARLY-DATE-N TO Z-DATE3-FORMAT-9.\n030946     IF (Z-DATE3-YY NOT < ZERO AND\n030948         Z-DATE3-YY NOT > Z-DATE-CC-CUTOFF)\n030950         COMPUTE Z-DATE2-CC = +20\n030952     ELSE\n030954         COMPUTE Z-DATE2-CC = +19 .\n030956     MOVE Z-DATE3-YY TO Z-DATE2-YY.\n030958     MOVE Z-DATE3-MM TO Z-DATE2-MM.\n030960     MOVE Z-DATE3-DD TO Z-DATE2-DD.\n030962     IF Z-DATE3-MM = ZEROS\n030964         AND Z-DATE3-DD = ZEROS\n030966         AND Z-DATE3-YY = ZEROS\n030968         MOVE ZEROS TO Z-DATE2-CC \n030970     ELSE IF Z-DATE3-MM = ALL \"9\"\n030972         AND Z-DATE3-DD = ALL \"9\"\n030974         AND Z-DATE3-YY = ALL \"9\"\n030976         MOVE ALL \"9\" TO Z-DATE2-CC.\n030978     MOVE Z-DATE2-FORMAT-9 TO BANK-EOY-EARLY-DATE.\n030980     MOVE SPEC-EOY-DELETE-DATE-N TO Z-DATE3-FORMAT-9.\n030982     IF (Z-DATE3-YY NOT < ZERO AND\n030984         Z-DATE3-YY NOT > Z-DATE-CC-CUTOFF)\n030986         COMPUTE Z-DATE2-CC = +20\n030988     ELSE\n030990         COMPUTE Z-DATE2-CC = +19 .\n030992     MOVE Z-DATE3-YY TO Z-DATE2-YY.\n030994     MOVE Z-DATE3-MM TO Z-DATE2-MM.\n030996     MOVE Z-DATE3-DD TO Z-DATE2-DD.\n030998     IF Z-DATE3-MM = ZEROS\n031000         AND Z-DATE3-DD = ZEROS\n031002         AND Z-DATE3-YY = ZEROS\n031004         MOVE ZEROS TO Z-DATE2-CC \n031006     ELSE IF Z-DATE3-MM = ALL \"9\"\n031008         AND Z-DATE3-DD = ALL \"9\"\n031010         AND Z-DATE3-YY = ALL \"9\"\n031012         MOVE ALL \"9\" TO Z-DATE2-CC.\n031014     MOVE Z-DATE2-FORMAT-9 TO BANK-EOY-DELETE-DATE.\n031016     MOVE SPEC-EOY-DELETE-DATE-N TO Z-DATE3-FORMAT-9.\n031018     IF (Z-DATE3-YY NOT < ZERO AND\n031020         Z-DATE3-YY NOT > Z-DATE-CC-CUTOFF)\n031022         COMPUTE Z-DATE2-CC = +20\n031024     ELSE\n031026         COMPUTE Z-DATE2-CC = +19 .\n031028     MOVE Z-DATE3-YY TO Z-DATE2-YY.\n031030     MOVE Z-DATE3-MM TO Z-DATE2-MM.\n031032     MOVE Z-DATE3-DD TO Z-DATE2-DD.\n031034     IF Z-DATE3-MM = ZEROS\n031036         AND Z-DATE3-DD = ZEROS\n031038         AND Z-DATE3-YY = ZEROS\n031040         MOVE ZEROS TO Z-DATE2-CC \n031042     ELSE IF Z-DATE3-MM = ALL \"9\"\n031044         AND Z-DATE3-DD = ALL \"9\"\n031046         AND Z-DATE3-YY = ALL \"9\"\n031048         MOVE ALL \"9\" TO Z-DATE2-CC.\n031050     MOVE Z-DATE2-FORMAT-9 TO BANK-EOY-APRIL-DATE.\n031052     MOVE 1 TO Z-EXIT-LEVEL\n031054     GO TO Z-9-2-END.\n031056 Z-9-3-1-ELSE.\n031058     IF ( BANK-NO > SPEC-BK-NO-9-4-N )\n031060         NEXT SENTENCE ELSE\n031062         GO TO Z-9-8-1-ELSE.\n031064     MOVE 1 TO Z-EXIT-LEVEL\n031066     GO TO Z-9-2-END.\n031068 Z-9-8-1-ELSE.\n031070     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 10 )\n031072         NEXT SENTENCE ELSE\n031074         GO TO Z-9-8-2-ELSE.\n031076     MOVE 1 TO Z-EXIT-LEVEL.\n031078     MOVE 1 TO Z-EXIT-CODE.\n031080     GO TO Z-9-2-END.\n031082 Z-9-8-2-ELSE.\n031084     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 1 )\n031086         NEXT SENTENCE ELSE\n031088         GO TO Z-9-8-3-ELSE.\n031090     MOVE SPEC-BK-NAME-N TO BANK-NAME.\n031092     MOVE SPEC-MSI-N TO BANK-MSI.\n031094     MOVE SPEC-BK-TDA-STAT-N TO BANK-TDA-PILOT.\n031096     MOVE SPEC-BK-IMG-SERV-N TO BANK-BK-IMG-SERV.\n031098     GO TO Z-9-8-ENDIF.\n031100 Z-9-8-3-ELSE.\n031102     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 2 )\n031104         NEXT SENTENCE ELSE\n031106         GO TO Z-9-8-4-ELSE.\n031108     MOVE SPEC-AREA-CODE-N TO BANK-PHN-AREA.\n031110     MOVE SPEC-BR-NO-N TO BANK-CSI-BR-CODE\n031112       , GWS-RMT-BR (1)\n031114       , GWS-RMT-BR (2).\n031116     MOVE SPEC-BK-NO-N TO GWS-RMT-BK (1).\n031118     MOVE SPEC-GL-NO-N TO GWS-RMT-BK (2).\n031120     MOVE SPEC-PHONE-1ST-3-N TO BANK-PHN-PREFIX.\n031122     MOVE SPEC-PHONE-LST-4-N TO BANK-PHN-SUFFIX.\n031124     GO TO Z-9-8-ENDIF.\n031126 Z-9-8-4-ELSE.\n031128     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 3 )\n031130         NEXT SENTENCE ELSE\n031132         GO TO Z-9-8-5-ELSE.\n031134     MOVE 1 TO SUB.\n031136 Z-9-21-LOOP.\n031138     IF ( SPEC-HOLIDAYS-N (SUB) = SPACES ) OR ( SUB = 18 )\n031140         GO TO Z-9-21-XIT.\n031142     IF SPEC-HOLIDAYS-N (SUB) NOT < PROC-BEG-MONTH-DAY AND NOT >  \n031144         PROC-END-MONTH-DAY\n031146         NEXT SENTENCE ELSE\n031148         GO TO Z-9-22-1-ELSE.\n031150     MOVE \"Y\" TO BANK-OPT-HOL.\n031152 Z-9-22-1-ELSE.\n031154     IF Z-EDIT-ERROR\n031156         GO TO Z-9-XIT.\n031158 Z-9-21-SKIP.\n031160     ADD 1 TO SUB.\n031162     GO TO Z-9-21-LOOP.\n031164*\n031166 Z-9-21-XIT.\n031168     GO TO Z-9-8-ENDIF.\n031170 Z-9-8-5-ELSE.\n031172     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 4 )\n031174         NEXT SENTENCE ELSE\n031176         GO TO Z-9-8-6-ELSE.\n031178     MOVE SPEC-RMT-BK-INDICATOR-N TO BANK-RMT-IND.\n031180     GO TO Z-9-8-ENDIF.\n031182 Z-9-8-6-ELSE.\n031184     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 5 )\n031186         NEXT SENTENCE ELSE\n031188         GO TO Z-9-8-7-ELSE.\n031190     MOVE SPEC-BK-ADDR-N TO BANK-ADDR.\n031192     MOVE SPEC-BK-ADDR-2-N TO BANK-ADDR-2.\n031194     GO TO Z-9-8-ENDIF.\n031196 Z-9-8-7-ELSE.\n031198     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 7 )\n031200         NEXT SENTENCE ELSE\n031202         GO TO Z-9-8-8-ELSE.\n031204     MOVE SPEC-NO-IRA-STMTS-N TO BANK-NO-IRA-STMTS.\n031206     MOVE SPEC-EOY-IRA-STMT-N TO BANK-EOY-IRA-STMT.\n031208     MOVE SPEC-EOY-IRA-PHONE-N TO BANK-EOY-IRA-PHONE.\n031210     MOVE SPEC-EOY-IRA-STMT-EARLY-N TO BANK-EOY-IRA-STMT-EARLY.\n031212     MOVE SPEC-EOY-IRA-STMT-PRINT-N TO BANK-EOY-IRA-STMT-PRINT.\n031214     GO TO Z-9-8-ENDIF.\n031216 Z-9-8-8-ELSE.\n031218     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 8 )\n031220         NEXT SENTENCE ELSE\n031222         GO TO Z-9-8-9-ELSE.\n031224     MOVE SPEC-BRANCH-LENGTH-N TO BANK-BRANCH-LENGTH.\n031226     MOVE SPEC-LOB-N TO BANK-LOB.\n031228     GO TO Z-9-8-ENDIF.\n031230 Z-9-8-9-ELSE.\n031232     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 9 )\n031234         NEXT SENTENCE ELSE\n031236         GO TO Z-9-8-10-ELSE.\n031238     MOVE SPEC-CK21-TDA-N OF SPEC-CARD-9-N TO BANK-CK21-TDA OF    \n031240         BANK-REC.\n031242     MOVE SPEC-MSI-OV-TDA-N OF SPEC-CARD-9-N TO BANK-MSI-OV-TDA   \n031244         OF BANK-REC.\n031246     MOVE SPEC-PRT-NEW-N OF SPEC-CARD-9-N TO BANK-PRT-NEW OF      \n031248         BANK-REC.\n031250     MOVE SPEC-IMONITOR-N OF SPEC-CARD-9-N TO BANK-IMONITOR OF    \n031252         BANK-REC.\n031254     MOVE SPEC-ENTC-TDA-N OF SPEC-CARD-9-N TO BANK-ENTC-TDA OF    \n031256         BANK-REC.\n031258 Z-9-8-10-ELSE.\n031260 Z-9-8-ENDIF.\n031262 Z-9-2-END.\n031264     IF Z-EDIT-ERROR\n031266         GO TO Z-9-XIT.\n031268 Z-9-2-SKIP.\n031270     IF Z-EXIT-LEVEL < 1\n031272         GO TO Z-9-END.\n031274     IF Z-EXIT-CODE > 0\n031276         GO TO Z-9-2-XIT.\n031278     GO TO Z-9-2-LOOP.\n031280*\n031282 Z-9-2-XIT.\n031284     MOVE 0 TO Z-EXIT-CODE.\n031286     MOVE 9999 TO Z-EXIT-LEVEL.\n031288 Z-9-END.\n031290     IF Z-EDIT-ERROR\n031292         GO TO Z-9-XIT.\n031294 Z-9-SKIP.\n031296 Z-9-XIT.\n031298     EXIT.\n031300*\n031302*****************************************************************\n031304*    PROCEDURE SETUP-ACCT\n031306*****************************************************************\n031308 Z-10-PROCEDURE.\n031310*\n031312     MOVE 0 TO Z-EXIT-CODE.\n031314     MOVE 9999 TO Z-EXIT-LEVEL.\n031316     MOVE ZERO TO Z-FLINFO8-PRES.\n031318     MOVE 5 TO Z-FLINFO8-LAST-SEQ.\n031320     MOVE ZERO TO Z-FLINFO8-SOME.\n031322 Z-10-1-READ.\n031324     FIND TDAACCT OF LDBTDADB VIA TDAAMSET OF TDAACCT OF LDBTDADB\n031326     AT TDAA-BANK = TDARPT-BANK AND\n031328        TDAA-CUST = TDARPT-CUST AND\n031330        TDAA-ACCT = TDARPT-ACCT\n031332         ON EXCEPTION\n031334         MOVE 5 TO Z-DMS-EXCEPT-SEQ\n031336         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n031338             GO TO Z-10-1-XIT\n031340         ELSE\n031342             MOVE \"TDAAMSET OF TDAACCT OF LDBTDADB\" TO            \n031344                 Z-DMS-EXCEPT-STR\n031346             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n031348             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n031350\n031352 Z-10-1-PRESENT.\n031354*\n031356     MOVE 1 TO Z-FLINFO8-SOME.\n031358     MOVE 1 TO Z-FLINFO8-PRES.\n031360     GO TO Z-10-1-CONT.\n031362 Z-10-1-XIT.\n031364 Z-10-1-CONT.\n031366************ PERFORM SETUP-ACCT-NO-READ\n031368     PERFORM Z-11-PROCEDURE THRU Z-11-XIT.\n031370     IF  Z-EXIT-EDITEXIT\n031372         GO TO Z-10-XIT.\n031374     IF  Z-DMS2-ABORT-FLAG = 1\n031376         GO TO Z-10-XIT.\n031378     IF  Z-EXIT-LEVEL < 0\n031380         GO TO Z-10-END.\n031382*\n031384 Z-10-END.\n031386     IF Z-EDIT-ERROR\n031388         GO TO Z-10-XIT.\n031390 Z-10-SKIP.\n031392     IF Z-EXIT-LEVEL NOT < 0\n031394         MOVE 0 TO Z-EXIT-CODE\n031396         MOVE 9999 TO Z-EXIT-LEVEL.\n031398 Z-10-XIT.\n031400     EXIT.\n031402*\n031404*****************************************************************\n031406*    PROCEDURE SETUP-ACCT-NO-READ\n031408*****************************************************************\n031410 Z-11-PROCEDURE.\n031412*\n031414     MOVE 0 TO Z-EXIT-CODE.\n031416     MOVE 9999 TO Z-EXIT-LEVEL.\n031418     MOVE SPACES TO HOLD-TDACUST.\n031420     MOVE SPACES TO HOLD-TDAACCT.\n031422     MOVE SPACES TO HOLD-TDAIRA.\n031424     MOVE SPACES TO TDB-RECORD.\n031426************ PERFORM TDD-TDAA-MOVE-TO-TDB\n031428     PERFORM Z-12-PROCEDURE THRU Z-12-XIT.\n031430     IF  Z-EXIT-EDITEXIT\n031432         GO TO Z-11-XIT.\n031434     IF  Z-DMS2-ABORT-FLAG = 1\n031436         GO TO Z-11-XIT.\n031438     IF  Z-EXIT-LEVEL < 0\n031440         GO TO Z-11-END.\n031442*\n031444************ PERFORM TDD-TDAA-MOVE-TO-HOLD\n031446     PERFORM Z-13-PROCEDURE THRU Z-13-XIT.\n031448     IF  Z-EXIT-EDITEXIT\n031450         GO TO Z-11-XIT.\n031452     IF  Z-DMS2-ABORT-FLAG = 1\n031454         GO TO Z-11-XIT.\n031456     IF  Z-EXIT-LEVEL < 0\n031458         GO TO Z-11-END.\n031460*\n031462     MOVE SPACES TO TDB-RECORD.\n031464     MOVE \"TDA\" TO TDB-APPL-ID.\n031466     MOVE 00 TO TDB-FUNCTION-CD.\n031468     MOVE \"BR\" TO TDB-ORIGINATE-CLIENT.\n031470     MOVE 01 TO TDB-CLIENT-VER.\n031472     MOVE 01 TO TDB-STRUCT-NBR.\n031474     MOVE 0 TO TDB-ERROR-NBR.\n031476     MOVE 0 TO TDB-MESSAGE-NBR.\n031478     MOVE TDB-TDAA-BANK TO TDB-TDAC-BANK.\n031480     MOVE TDB-TDAA-CUST TO TDB-TDAC-CUST.\n031482     MOVE 01 TO TDB-READ-SET-NBR.\n031484     MOVE \"B\" TO TDB-READ-DIRECTION.\n031486     MOVE \"AT2\" TO TDB-READ-AT.\n031488     MOVE WS-PROCESS-DATE TO TDB-READ-DATE.\n031490************ PERFORM TDB-CUST-INQ\n031492     PERFORM Z-14-PROCEDURE THRU Z-14-XIT.\n031494     IF  Z-EXIT-EDITEXIT\n031496         GO TO Z-11-XIT.\n031498     IF  Z-DMS2-ABORT-FLAG = 1\n031500         GO TO Z-11-XIT.\n031502     IF  Z-EXIT-LEVEL < 0\n031504         GO TO Z-11-END.\n031506*\n031508     IF TDB-ERROR-NBR = 0\n031510         NEXT SENTENCE\n031512     ELSE\n031514         GO TO Z-11-22-END-MOVE.\n031516     MOVE TDB-TDAC-BANK OF TDB-TDACUST TO HOLD-TDAC-BANK OF       \n031518         HOLD-TDACUST.\n031520     MOVE TDB-TDAC-CUST OF TDB-TDACUST TO HOLD-TDAC-CUST OF       \n031522         HOLD-TDACUST.\n031524     MOVE TDB-TDAC-BRCH OF TDB-TDACUST TO HOLD-TDAC-BRCH OF       \n031526         HOLD-TDACUST.\n031528     MOVE TDB-TDAC-STATUS OF TDB-TDACUST TO HOLD-TDAC-STATUS OF   \n031530         HOLD-TDACUST.\n031532     MOVE TDB-TDAC-NAME-1 OF TDB-TDACUST TO HOLD-TDAC-NAME-1 OF   \n031534         HOLD-TDACUST.\n031536     MOVE TDB-TDAC-N1-KEY OF TDB-TDACUST TO HOLD-TDAC-N1-KEY OF   \n031538         HOLD-TDACUST.\n031540     MOVE TDB-TDAC-N1-FIRST OF TDB-TDACUST TO HOLD-TDAC-N1-FIRST  \n031542         OF HOLD-TDACUST.\n031544     MOVE TDB-TDAC-N1-MID OF TDB-TDACUST TO HOLD-TDAC-N1-MID OF   \n031546         HOLD-TDACUST.\n031548     MOVE TDB-TDAC-N1-LAST OF TDB-TDACUST TO HOLD-TDAC-N1-LAST OF \n031550         HOLD-TDACUST.\n031552     MOVE TDB-TDAC-N1-PREFIX OF TDB-TDACUST TO                    \n031554         HOLD-TDAC-N1-PREFIX OF HOLD-TDACUST.\n031556     MOVE TDB-TDAC-N1-SUFFIX OF TDB-TDACUST TO                    \n031558         HOLD-TDAC-N1-SUFFIX OF HOLD-TDACUST.\n031560     MOVE TDB-TDAC-N1-FAMILIAR OF TDB-TDACUST TO                  \n031562         HOLD-TDAC-N1-FAMILIAR OF HOLD-TDACUST.\n031564     MOVE TDB-TDAC-N1-PRT-PFX OF TDB-TDACUST TO                   \n031566         HOLD-TDAC-N1-PRT-PFX OF HOLD-TDACUST.\n031568     MOVE TDB-TDAC-N1-PRT-SFX OF TDB-TDACUST TO                   \n031570         HOLD-TDAC-N1-PRT-SFX OF HOLD-TDACUST.\n031572     MOVE TDB-TDAC-N1-DESIGNAT OF TDB-TDACUST TO                  \n031574         HOLD-TDAC-N1-DESIGNAT OF HOLD-TDACUST.\n031576     MOVE TDB-TDAC-NAME-2 OF TDB-TDACUST TO HOLD-TDAC-NAME-2 OF   \n031578         HOLD-TDACUST.\n031580     MOVE TDB-TDAC-N2-MODIFIED OF TDB-TDACUST TO                  \n031582         HOLD-TDAC-N2-MODIFIED OF HOLD-TDACUST.\n031584     MOVE TDB-TDAC-N2-PRINT-CD OF TDB-TDACUST TO                  \n031586         HOLD-TDAC-N2-PRINT-CD OF HOLD-TDACUST.\n031588     MOVE TDB-TDAC-N2-KEY OF TDB-TDACUST TO HOLD-TDAC-N2-KEY OF   \n031590         HOLD-TDACUST.\n031592     MOVE TDB-TDAC-N2-FIRST OF TDB-TDACUST TO HOLD-TDAC-N2-FIRST  \n031594         OF HOLD-TDACUST.\n031596     MOVE TDB-TDAC-N2-MID OF TDB-TDACUST TO HOLD-TDAC-N2-MID OF   \n031598         HOLD-TDACUST.\n031600     MOVE TDB-TDAC-N2-LAST OF TDB-TDACUST TO HOLD-TDAC-N2-LAST OF \n031602         HOLD-TDACUST.\n031604     MOVE TDB-TDAC-N2-PREFIX OF TDB-TDACUST TO                    \n031606         HOLD-TDAC-N2-PREFIX OF HOLD-TDACUST.\n031608     MOVE TDB-TDAC-N2-SUFFIX OF TDB-TDACUST TO                    \n031610         HOLD-TDAC-N2-SUFFIX OF HOLD-TDACUST.\n031612     MOVE TDB-TDAC-N2-FAMILIAR OF TDB-TDACUST TO                  \n031614         HOLD-TDAC-N2-FAMILIAR OF HOLD-TDACUST.\n031616     MOVE TDB-TDAC-N2-PRT-PFX OF TDB-TDACUST TO                   \n031618         HOLD-TDAC-N2-PRT-PFX OF HOLD-TDACUST.\n031620     MOVE TDB-TDAC-N2-PRT-SFX OF TDB-TDACUST TO                   \n031622         HOLD-TDAC-N2-PRT-SFX OF HOLD-TDACUST.\n031624     MOVE TDB-TDAC-N2-DESIGNAT OF TDB-TDACUST TO                  \n031626         HOLD-TDAC-N2-DESIGNAT OF HOLD-TDACUST.\n031628     MOVE TDB-TDAC-NAME-3 OF TDB-TDACUST TO HOLD-TDAC-NAME-3 OF   \n031630         HOLD-TDACUST.\n031632     MOVE TDB-TDAC-N3-MODIFIED OF TDB-TDACUST TO                  \n031634         HOLD-TDAC-N3-MODIFIED OF HOLD-TDACUST.\n031636     MOVE TDB-TDAC-N3-PRINT-CD OF TDB-TDACUST TO                  \n031638         HOLD-TDAC-N3-PRINT-CD OF HOLD-TDACUST.\n031640     MOVE TDB-TDAC-N3-KEY OF TDB-TDACUST TO HOLD-TDAC-N3-KEY OF   \n031642         HOLD-TDACUST.\n031644     MOVE TDB-TDAC-N3-FIRST OF TDB-TDACUST TO HOLD-TDAC-N3-FIRST  \n031646         OF HOLD-TDACUST.\n031648     MOVE TDB-TDAC-N3-MID OF TDB-TDACUST TO HOLD-TDAC-N3-MID OF   \n031650         HOLD-TDACUST.\n031652     MOVE TDB-TDAC-N3-LAST OF TDB-TDACUST TO HOLD-TDAC-N3-LAST OF \n031654         HOLD-TDACUST.\n031656     MOVE TDB-TDAC-N3-PREFIX OF TDB-TDACUST TO                    \n031658         HOLD-TDAC-N3-PREFIX OF HOLD-TDACUST.\n031660     MOVE TDB-TDAC-N3-SUFFIX OF TDB-TDACUST TO                    \n031662         HOLD-TDAC-N3-SUFFIX OF HOLD-TDACUST.\n031664     MOVE TDB-TDAC-N3-FAMILIAR OF TDB-TDACUST TO                  \n031666         HOLD-TDAC-N3-FAMILIAR OF HOLD-TDACUST.\n031668     MOVE TDB-TDAC-N3-PRT-PFX OF TDB-TDACUST TO                   \n031670         HOLD-TDAC-N3-PRT-PFX OF HOLD-TDACUST.\n031672     MOVE TDB-TDAC-N3-PRT-SFX OF TDB-TDACUST TO                   \n031674         HOLD-TDAC-N3-PRT-SFX OF HOLD-TDACUST.\n031676     MOVE TDB-TDAC-N3-DESIGNAT OF TDB-TDACUST TO                  \n031678         HOLD-TDAC-N3-DESIGNAT OF HOLD-TDACUST.\n031680     MOVE TDB-TDAC-ADDR-KEY OF TDB-TDACUST TO HOLD-TDAC-ADDR-KEY  \n031682         OF HOLD-TDACUST.\n031684     MOVE TDB-TDAC-ADDR-1 OF TDB-TDACUST TO HOLD-TDAC-ADDR-1 OF   \n031686         HOLD-TDACUST.\n031688     MOVE TDB-TDAC-ADDR-2 OF TDB-TDACUST TO HOLD-TDAC-ADDR-2 OF   \n031690         HOLD-TDACUST.\n031692     MOVE TDB-TDAC-CITY OF TDB-TDACUST TO HOLD-TDAC-CITY OF       \n031694         HOLD-TDACUST.\n031696     MOVE TDB-TDAC-STATE OF TDB-TDACUST TO HOLD-TDAC-STATE OF     \n031698         HOLD-TDACUST.\n031700     MOVE TDB-TDAC-PROVINCE OF TDB-TDACUST TO HOLD-TDAC-PROVINCE  \n031702         OF HOLD-TDACUST.\n031704     MOVE TDB-TDAC-COUNTRY OF TDB-TDACUST TO HOLD-TDAC-COUNTRY OF \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    528 lines from 15321 to 15848.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 32, "total_chunks": 55, "start_line": 15321, "end_line": 15848, "line_count": 528}

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
- Source code length: 27792 characters

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
CHUNK 32 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 15321 to 15848 (528 lines)
Chunk Tokens (estimated): ~8,085
Actual Input Tokens: 9,491 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 15321-15848 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 32 of 55 chunks
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
      The source code below is only CHUNK 32 of 55.


=============================================================================
CHUNK 32 SOURCE CODE (Lines 15321-15848)
=============================================================================

```cobol
030650 Z-8-5-1-ELSE.
030652     MOVE "0" TO GWS-RMT-FICHE-COPIES.
030654 Z-8-5-ENDIF.
030656     GO TO Z-8-4-ENDIF.
030658 Z-8-4-1-ELSE.
030660     MOVE GWS-MICROFICHE-CODE TO GWS-RMT-FICHE-COPIES.
030662 Z-8-4-ENDIF.
030664     IF ( GWS-RMT-DESCRIPTOR = "TR" OR "RJ" OR "TS" ) AND         
030666         GWS-RPT-TYPE NOT = 1
030668         NEXT SENTENCE ELSE
030670         GO TO Z-8-9-1-ELSE.
030672     MOVE "B" TO GWS-RMT-FILE-TYPE.
030674     GO TO Z-8-9-ENDIF.
030676 Z-8-9-1-ELSE.
030678     MOVE "P" TO GWS-RMT-FILE-TYPE.
030680 Z-8-9-ENDIF.
030682     MOVE PROCESS-DATE TO WS-DATE-CYMD.
030684     MOVE WS-DATE-DD TO GWS-RMT-DD.
030686     MOVE "N" TO GWS-RMT-APPL.
030688     MOVE GWS-RMT-EXT TO GWS-RMT-RPT-NO.
030690     MOVE GWS-PACK TO GWS-RMT-PACK.
030692     IF (SW3-1) AND (GWS-PRT-PID-FLAG NOT = 2)                    
030694         MOVE 2 TO GWS-PRT-PID-FLAG                               
030696         DISPLAY "ENTER PACK NAME FOR REMOTE PRINT FILES"         
030698         ACCEPT GWS-RMT-PACK.                                     
030700     MOVE " ON" TO GWS-RMT-ON.
030702     MOVE GWS-A12-PERIOD TO GWS-RMT-PERIOD.
030704     MOVE GWS-RMT-PRT-LABEL TO ID-PRT74-2.
030706     IF Z-EDIT-ERROR
030708         GO TO Z-8-XIT.
030710 Z-8-SKIP.
030712 Z-8-XIT.
030714     EXIT.
030716*
030718*****************************************************************
030720*    PROCEDURE READ-SPECS
030722*****************************************************************
030724 Z-9-PROCEDURE.
030726*
030728     MOVE ZEROS TO BANK-BR-3 OF BANK-REC.
030730     MOVE ZEROS TO BANK-CSI-BR-CODE OF BANK-REC.
030732     MOVE SPACES TO BANK-NAME OF BANK-REC.
030734     MOVE SPACES TO BANK-ADDR OF BANK-REC.
030736     MOVE SPACES TO BANK-ADDR-2 OF BANK-REC.
030738     MOVE SPACES TO BANK-FED-ID OF BANK-REC.
030740     MOVE ZEROS TO BANK-INT-JRNL-BR-PRT OF BANK-REC.
030742     MOVE SPACES TO BANK-CK-PRT-FORMAT OF BANK-REC.
030744     MOVE SPACES TO BANK-RESTRICT-REDEMP-TICKET OF BANK-REC.
030746     MOVE SPACES TO BANK-CK-PRT-ACCTNO OF BANK-REC.
030748     MOVE SPACES TO BANK-RESTRICT-RATE-PRT OF BANK-REC.
030750     MOVE SPACES TO BANK-CK-PROTECT OF BANK-REC.
030752     MOVE ZEROS TO BANK-SP-CK-REMARK OF BANK-REC.
030754     MOVE ZEROS TO BANK-APPL OF BANK-REC.
030756     MOVE SPACES TO BANK-RMT-IND OF BANK-REC.
030758     MOVE SPACES TO BANK-STATUS OF BANK-REC.
030760     MOVE SPACES TO BANK-TDA-PILOT OF BANK-REC.
030762     MOVE ZEROS TO BANK-PHN-AREA OF BANK-REC.
030764     MOVE ZEROS TO BANK-PHN-PREFIX OF BANK-REC.
030766     MOVE ZEROS TO BANK-PHN-SUFFIX OF BANK-REC.
030768     MOVE ZEROS TO BANK-IRA-PHN-AREA OF BANK-REC.
030770     MOVE ZEROS TO BANK-IRA-PHN-PREFIX OF BANK-REC.
030772     MOVE ZEROS TO BANK-IRA-PHN-SUFFIX OF BANK-REC.
030774     MOVE SPACES TO BANK-EOY-IRA-STMT OF BANK-REC.
030776     MOVE SPACES TO BANK-EOY-IRA-STMT-EARLY OF BANK-REC.
030778     MOVE SPACES TO BANK-EOY-IRA-STMT-PRINT OF BANK-REC.
030780     MOVE ZEROS TO BANK-EOY-NO-IRA-STMTS OF BANK-REC.
030782     MOVE SPACES TO BANK-EOY-RETURN-TO-BANK OF BANK-REC.
030784     MOVE SPACES TO BANK-EOY-EARLY-RUN OF BANK-REC.
030786     MOVE SPACES TO BANK-EOY-RPT-SEQ OF BANK-REC.
030788     MOVE SPACES TO BANK-EOY-IRA-FICHE OF BANK-REC.
030790     MOVE SPACES TO BANK-EOY-IRA-PAPER OF BANK-REC.
030792     MOVE ZEROS TO BANK-NO-IRA-STMTS OF BANK-REC.
030794     MOVE SPACES TO BANK-OPT-HOL OF BANK-REC.
030796     MOVE SPACES TO BANK-CK21-TDA OF BANK-REC.
030798     MOVE SPACES TO BANK-DQVISTA OF BANK-REC.
030800     MOVE SPACES TO BANK-MSI OF BANK-REC.
030802     MOVE SPACES TO BANK-MSI-OV-TDA OF BANK-REC.
030804     MOVE SPACES TO BANK-BK-IMG-SERV OF BANK-REC.
030806     MOVE SPACES TO BANK-FM-SUPPRESS OF BANK-REC.
030808     MOVE SPACES TO BANK-EOY-COD-CLOSED-RPT OF BANK-REC.
030810     MOVE SPACES TO BANK-PRT-NEW OF BANK-REC.
030812     MOVE SPACES TO BANK-IMONITOR OF BANK-REC.
030814     MOVE SPACES TO BANK-CENTERVIEW OF BANK-REC.
030816     MOVE SPACES TO BANK-TDA-ADD-DAY OF BANK-REC.
030818     MOVE 1 TO Z-II.
030820 Z-9-1-1-LOOP.
030822     IF Z-II > 18
030824         GO TO Z-9-1-1-LOOP-XIT.
030826     MOVE SPACES TO BANK-HOL-MM OF BANK-REC (Z-II).
030828     MOVE SPACES TO BANK-HOL-DD OF BANK-REC (Z-II).
030830     ADD 1 TO Z-II.
030832     GO TO Z-9-1-1-LOOP.
030834 Z-9-1-1-LOOP-XIT.
030836     MOVE ZEROS TO BANK-CREATE-DT OF BANK-REC.
030838     MOVE ZEROS TO BANK-CREATE-TM OF BANK-REC.
030840     MOVE SPACES TO BANK-ENTC-TDA OF BANK-REC.
030842     MOVE SPACES TO BANK-EV-3RD-PARTY-1 OF BANK-REC.
030844     MOVE SPACES TO BANK-EV-3RD-PARTY-2 OF BANK-REC.
030846     MOVE SPACES TO BANK-HSA-LOCATION OF BANK-REC.
030848     MOVE SPACES TO BANK-PROFITABILITY OF BANK-REC.
030850     MOVE SPACES TO BANK-BANCVUE OF BANK-REC.
030852     MOVE SPACES TO BANK-SPECIAL-DL-BILLING OF BANK-REC.
030854     MOVE SPACES TO BANK-WEB-ENABLED OF BANK-REC.
030856     MOVE ZEROS TO BANK-CIF-NAME-ADDR OF BANK-REC.
030858     MOVE SPACES TO BANK-MAIL-ADDR-LINES OF BANK-REC.
030860     MOVE ZEROS TO BANK-BRANCH-LENGTH OF BANK-REC.
030862     MOVE ZEROS TO BANK-LOB OF BANK-REC.
030864     MOVE SPACES TO BANK-TRAIN-BK-FLG OF BANK-REC.
030866     MOVE SPACES TO BANK-EOY-CIB-F-MERD OF BANK-REC.
030868*
030870******* OPEN FILE BK-SPEC-FILE
030872*
030874     IF Z-FLINFO3-OPEN = 0
030876         CHANGE ATTRIBUTE DEPENDENTSPECS OF BK-SPEC-FILE TO TRUE 
030878         OPEN INPUT BK-SPEC-FILE 
030880         IF ATTRIBUTE FILESTATE OF BK-SPEC-FILE = VALUE OPENED
030882             MOVE ZEROS TO Z-FILE3-KEY
030884             MOVE ZEROS TO Z-FLINFO3-RS-KEY
030886             MOVE 1 TO Z-FLINFO3-OPEN
030888             MOVE 1 TO Z-FLINFO3-RS-OPEN
030890         ELSE
030892             DISPLAY ">>> FILE BK-SPEC-FILE FAILED TO OPEN"
030894             MOVE ATTRIBUTE TITLE OF BK-SPEC-FILE TO              
030896                 Z-FL-EXCEPT-TITLE
030898             DISPLAY ">>> OPEN FAIL, TITLE :", Z-FL-EXCEPT-TITLE
030900             DISPLAY ">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS".
030902     MOVE ZERO TO Z-FLINFO3-PRES.
030904     MOVE ZERO TO Z-FLINFO3-SOME.
030906     MOVE 4 TO Z-FLINFO3-LAST-SEQ.
030908*
030910 Z-9-2-LOOP.
030912     MOVE ZERO TO Z-FLINFO3-PRES.
030914*
030916 Z-9-2-READ.
030918     READ BK-SPEC-FILE RECORD 
030920         AT END
030922         GO TO Z-9-2-XIT.
030924     MOVE Z-FILE3-KEY TO Z-FLINFO3-RS-KEY.
030926*
030928     MOVE 1 TO Z-FLINFO3-PRES.
030930     MOVE 1 TO Z-FLINFO3-SOME.
030932     MOVE 1 TO Z-FLINFO3-MODIFY.
030934     MOVE 0 TO Z-EXIT-CODE.
030936     MOVE 9999 TO Z-EXIT-LEVEL.
030938     IF ( SPEC-BK-NO-9-4-N = 0000 ) AND ( SPEC-SEQ-NO-N = 7 )
030940         NEXT SENTENCE ELSE
030942         GO TO Z-9-3-1-ELSE.
030944     MOVE SPEC-EOY-EARLY-DATE-N TO Z-DATE3-FORMAT-9.
030946     IF (Z-DATE3-YY NOT < ZERO AND
030948         Z-DATE3-YY NOT > Z-DATE-CC-CUTOFF)
030950         COMPUTE Z-DATE2-CC = +20
030952     ELSE
030954         COMPUTE Z-DATE2-CC = +19 .
030956     MOVE Z-DATE3-YY TO Z-DATE2-YY.
030958     MOVE Z-DATE3-MM TO Z-DATE2-MM.
030960     MOVE Z-DATE3-DD TO Z-DATE2-DD.
030962     IF Z-DATE3-MM = ZEROS
030964         AND Z-DATE3-DD = ZEROS
030966         AND Z-DATE3-YY = ZEROS
030968         MOVE ZEROS TO Z-DATE2-CC 
030970     ELSE IF Z-DATE3-MM = ALL "9"
030972         AND Z-DATE3-DD = ALL "9"
030974         AND Z-DATE3-YY = ALL "9"
030976         MOVE ALL "9" TO Z-DATE2-CC.
030978     MOVE Z-DATE2-FORMAT-9 TO BANK-EOY-EARLY-DATE.
030980     MOVE SPEC-EOY-DELETE-DATE-N TO Z-DATE3-FORMAT-9.
030982     IF (Z-DATE3-YY NOT < ZERO AND
030984         Z-DATE3-YY NOT > Z-DATE-CC-CUTOFF)
030986         COMPUTE Z-DATE2-CC = +20
030988     ELSE
030990         COMPUTE Z-DATE2-CC = +19 .
030992     MOVE Z-DATE3-YY TO Z-DATE2-YY.
030994     MOVE Z-DATE3-MM TO Z-DATE2-MM.
030996     MOVE Z-DATE3-DD TO Z-DATE2-DD.
030998     IF Z-DATE3-MM = ZEROS
031000         AND Z-DATE3-DD = ZEROS
031002         AND Z-DATE3-YY = ZEROS
031004         MOVE ZEROS TO Z-DATE2-CC 
031006     ELSE IF Z-DATE3-MM = ALL "9"
031008         AND Z-DATE3-DD = ALL "9"
031010         AND Z-DATE3-YY = ALL "9"
031012         MOVE ALL "9" TO Z-DATE2-CC.
031014     MOVE Z-DATE2-FORMAT-9 TO BANK-EOY-DELETE-DATE.
031016     MOVE SPEC-EOY-DELETE-DATE-N TO Z-DATE3-FORMAT-9.
031018     IF (Z-DATE3-YY NOT < ZERO AND
031020         Z-DATE3-YY NOT > Z-DATE-CC-CUTOFF)
031022         COMPUTE Z-DATE2-CC = +20
031024     ELSE
031026         COMPUTE Z-DATE2-CC = +19 .
031028     MOVE Z-DATE3-YY TO Z-DATE2-YY.
031030     MOVE Z-DATE3-MM TO Z-DATE2-MM.
031032     MOVE Z-DATE3-DD TO Z-DATE2-DD.
031034     IF Z-DATE3-MM = ZEROS
031036         AND Z-DATE3-DD = ZEROS
031038         AND Z-DATE3-YY = ZEROS
031040         MOVE ZEROS TO Z-DATE2-CC 
031042     ELSE IF Z-DATE3-MM = ALL "9"
031044         AND Z-DATE3-DD = ALL "9"
031046         AND Z-DATE3-YY = ALL "9"
031048         MOVE ALL "9" TO Z-DATE2-CC.
031050     MOVE Z-DATE2-FORMAT-9 TO BANK-EOY-APRIL-DATE.
031052     MOVE 1 TO Z-EXIT-LEVEL
031054     GO TO Z-9-2-END.
031056 Z-9-3-1-ELSE.
031058     IF ( BANK-NO > SPEC-BK-NO-9-4-N )
031060         NEXT SENTENCE ELSE
031062         GO TO Z-9-8-1-ELSE.
031064     MOVE 1 TO Z-EXIT-LEVEL
031066     GO TO Z-9-2-END.
031068 Z-9-8-1-ELSE.
031070     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 10 )
031072         NEXT SENTENCE ELSE
031074         GO TO Z-9-8-2-ELSE.
031076     MOVE 1 TO Z-EXIT-LEVEL.
031078     MOVE 1 TO Z-EXIT-CODE.
031080     GO TO Z-9-2-END.
031082 Z-9-8-2-ELSE.
031084     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 1 )
031086         NEXT SENTENCE ELSE
031088         GO TO Z-9-8-3-ELSE.
031090     MOVE SPEC-BK-NAME-N TO BANK-NAME.
031092     MOVE SPEC-MSI-N TO BANK-MSI.
031094     MOVE SPEC-BK-TDA-STAT-N TO BANK-TDA-PILOT.
031096     MOVE SPEC-BK-IMG-SERV-N TO BANK-BK-IMG-SERV.
031098     GO TO Z-9-8-ENDIF.
031100 Z-9-8-3-ELSE.
031102     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 2 )
031104         NEXT SENTENCE ELSE
031106         GO TO Z-9-8-4-ELSE.
031108     MOVE SPEC-AREA-CODE-N TO BANK-PHN-AREA.
031110     MOVE SPEC-BR-NO-N TO BANK-CSI-BR-CODE
031112       , GWS-RMT-BR (1)
031114       , GWS-RMT-BR (2).
031116     MOVE SPEC-BK-NO-N TO GWS-RMT-BK (1).
031118     MOVE SPEC-GL-NO-N TO GWS-RMT-BK (2).
031120     MOVE SPEC-PHONE-1ST-3-N TO BANK-PHN-PREFIX.
031122     MOVE SPEC-PHONE-LST-4-N TO BANK-PHN-SUFFIX.
031124     GO TO Z-9-8-ENDIF.
031126 Z-9-8-4-ELSE.
031128     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 3 )
031130         NEXT SENTENCE ELSE
031132         GO TO Z-9-8-5-ELSE.
031134     MOVE 1 TO SUB.
031136 Z-9-21-LOOP.
031138     IF ( SPEC-HOLIDAYS-N (SUB) = SPACES ) OR ( SUB = 18 )
031140         GO TO Z-9-21-XIT.
031142     IF SPEC-HOLIDAYS-N (SUB) NOT < PROC-BEG-MONTH-DAY AND NOT >  
031144         PROC-END-MONTH-DAY
031146         NEXT SENTENCE ELSE
031148         GO TO Z-9-22-1-ELSE.
031150     MOVE "Y" TO BANK-OPT-HOL.
031152 Z-9-22-1-ELSE.
031154     IF Z-EDIT-ERROR
031156         GO TO Z-9-XIT.
031158 Z-9-21-SKIP.
031160     ADD 1 TO SUB.
031162     GO TO Z-9-21-LOOP.
031164*
031166 Z-9-21-XIT.
031168     GO TO Z-9-8-ENDIF.
031170 Z-9-8-5-ELSE.
031172     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 4 )
031174         NEXT SENTENCE ELSE
031176         GO TO Z-9-8-6-ELSE.
031178     MOVE SPEC-RMT-BK-INDICATOR-N TO BANK-RMT-IND.
031180     GO TO Z-9-8-ENDIF.
031182 Z-9-8-6-ELSE.
031184     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 5 )
031186         NEXT SENTENCE ELSE
031188         GO TO Z-9-8-7-ELSE.
031190     MOVE SPEC-BK-ADDR-N TO BANK-ADDR.
031192     MOVE SPEC-BK-ADDR-2-N TO BANK-ADDR-2.
031194     GO TO Z-9-8-ENDIF.
031196 Z-9-8-7-ELSE.
031198     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 7 )
031200         NEXT SENTENCE ELSE
031202         GO TO Z-9-8-8-ELSE.
031204     MOVE SPEC-NO-IRA-STMTS-N TO BANK-NO-IRA-STMTS.
031206     MOVE SPEC-EOY-IRA-STMT-N TO BANK-EOY-IRA-STMT.
031208     MOVE SPEC-EOY-IRA-PHONE-N TO BANK-EOY-IRA-PHONE.
031210     MOVE SPEC-EOY-IRA-STMT-EARLY-N TO BANK-EOY-IRA-STMT-EARLY.
031212     MOVE SPEC-EOY-IRA-STMT-PRINT-N TO BANK-EOY-IRA-STMT-PRINT.
031214     GO TO Z-9-8-ENDIF.
031216 Z-9-8-8-ELSE.
031218     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 8 )
031220         NEXT SENTENCE ELSE
031222         GO TO Z-9-8-9-ELSE.
031224     MOVE SPEC-BRANCH-LENGTH-N TO BANK-BRANCH-LENGTH.
031226     MOVE SPEC-LOB-N TO BANK-LOB.
031228     GO TO Z-9-8-ENDIF.
031230 Z-9-8-9-ELSE.
031232     IF ( BANK-NO = SPEC-BK-NO-9-4-N ) AND ( SPEC-SEQ-NO-N = 9 )
031234         NEXT SENTENCE ELSE
031236         GO TO Z-9-8-10-ELSE.
031238     MOVE SPEC-CK21-TDA-N OF SPEC-CARD-9-N TO BANK-CK21-TDA OF    
031240         BANK-REC.
031242     MOVE SPEC-MSI-OV-TDA-N OF SPEC-CARD-9-N TO BANK-MSI-OV-TDA   
031244         OF BANK-REC.
031246     MOVE SPEC-PRT-NEW-N OF SPEC-CARD-9-N TO BANK-PRT-NEW OF      
031248         BANK-REC.
031250     MOVE SPEC-IMONITOR-N OF SPEC-CARD-9-N TO BANK-IMONITOR OF    
031252         BANK-REC.
031254     MOVE SPEC-ENTC-TDA-N OF SPEC-CARD-9-N TO BANK-ENTC-TDA OF    
031256         BANK-REC.
031258 Z-9-8-10-ELSE.
031260 Z-9-8-ENDIF.
031262 Z-9-2-END.
031264     IF Z-EDIT-ERROR
031266         GO TO Z-9-XIT.
031268 Z-9-2-SKIP.
031270     IF Z-EXIT-LEVEL < 1
031272         GO TO Z-9-END.
031274     IF Z-EXIT-CODE > 0
031276         GO TO Z-9-2-XIT.
031278     GO TO Z-9-2-LOOP.
031280*
031282 Z-9-2-XIT.
031284     MOVE 0 TO Z-EXIT-CODE.
031286     MOVE 9999 TO Z-EXIT-LEVEL.
031288 Z-9-END.
031290     IF Z-EDIT-ERROR
031292         GO TO Z-9-XIT.
031294 Z-9-SKIP.
031296 Z-9-XIT.
031298     EXIT.
031300*
031302*****************************************************************
031304*    PROCEDURE SETUP-ACCT
031306*****************************************************************
031308 Z-10-PROCEDURE.
031310*
031312     MOVE 0 TO Z-EXIT-CODE.
031314     MOVE 9999 TO Z-EXIT-LEVEL.
031316     MOVE ZERO TO Z-FLINFO8-PRES.
031318     MOVE 5 TO Z-FLINFO8-LAST-SEQ.
031320     MOVE ZERO TO Z-FLINFO8-SOME.
031322 Z-10-1-READ.
031324     FIND TDAACCT OF LDBTDADB VIA TDAAMSET OF TDAACCT OF LDBTDADB
031326     AT TDAA-BANK = TDARPT-BANK AND
031328        TDAA-CUST = TDARPT-CUST AND
031330        TDAA-ACCT = TDARPT-ACCT
031332         ON EXCEPTION
031334         MOVE 5 TO Z-DMS-EXCEPT-SEQ
031336         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
031338             GO TO Z-10-1-XIT
031340         ELSE
031342             MOVE "TDAAMSET OF TDAACCT OF LDBTDADB" TO            
031344                 Z-DMS-EXCEPT-STR
031346             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
031348             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
031350
031352 Z-10-1-PRESENT.
031354*
031356     MOVE 1 TO Z-FLINFO8-SOME.
031358     MOVE 1 TO Z-FLINFO8-PRES.
031360     GO TO Z-10-1-CONT.
031362 Z-10-1-XIT.
031364 Z-10-1-CONT.
031366************ PERFORM SETUP-ACCT-NO-READ
031368     PERFORM Z-11-PROCEDURE THRU Z-11-XIT.
031370     IF  Z-EXIT-EDITEXIT
031372         GO TO Z-10-XIT.
031374     IF  Z-DMS2-ABORT-FLAG = 1
031376         GO TO Z-10-XIT.
031378     IF  Z-EXIT-LEVEL < 0
031380         GO TO Z-10-END.
031382*
031384 Z-10-END.
031386     IF Z-EDIT-ERROR
031388         GO TO Z-10-XIT.
031390 Z-10-SKIP.
031392     IF Z-EXIT-LEVEL NOT < 0
031394         MOVE 0 TO Z-EXIT-CODE
031396         MOVE 9999 TO Z-EXIT-LEVEL.
031398 Z-10-XIT.
031400     EXIT.
031402*
031404*****************************************************************
031406*    PROCEDURE SETUP-ACCT-NO-READ
031408*****************************************************************
031410 Z-11-PROCEDURE.
031412*
031414     MOVE 0 TO Z-EXIT-CODE.
031416     MOVE 9999 TO Z-EXIT-LEVEL.
031418     MOVE SPACES TO HOLD-TDACUST.
031420     MOVE SPACES TO HOLD-TDAACCT.
031422     MOVE SPACES TO HOLD-TDAIRA.
031424     MOVE SPACES TO TDB-RECORD.
031426************ PERFORM TDD-TDAA-MOVE-TO-TDB
031428     PERFORM Z-12-PROCEDURE THRU Z-12-XIT.
031430     IF  Z-EXIT-EDITEXIT
031432         GO TO Z-11-XIT.
031434     IF  Z-DMS2-ABORT-FLAG = 1
031436         GO TO Z-11-XIT.
031438     IF  Z-EXIT-LEVEL < 0
031440         GO TO Z-11-END.
031442*
031444************ PERFORM TDD-TDAA-MOVE-TO-HOLD
031446     PERFORM Z-13-PROCEDURE THRU Z-13-XIT.
031448     IF  Z-EXIT-EDITEXIT
031450         GO TO Z-11-XIT.
031452     IF  Z-DMS2-ABORT-FLAG = 1
031454         GO TO Z-11-XIT.
031456     IF  Z-EXIT-LEVEL < 0
031458         GO TO Z-11-END.
031460*
031462     MOVE SPACES TO TDB-RECORD.
031464     MOVE "TDA" TO TDB-APPL-ID.
031466     MOVE 00 TO TDB-FUNCTION-CD.
031468     MOVE "BR" TO TDB-ORIGINATE-CLIENT.
031470     MOVE 01 TO TDB-CLIENT-VER.
031472     MOVE 01 TO TDB-STRUCT-NBR.
031474     MOVE 0 TO TDB-ERROR-NBR.
031476     MOVE 0 TO TDB-MESSAGE-NBR.
031478     MOVE TDB-TDAA-BANK TO TDB-TDAC-BANK.
031480     MOVE TDB-TDAA-CUST TO TDB-TDAC-CUST.
031482     MOVE 01 TO TDB-READ-SET-NBR.
031484     MOVE "B" TO TDB-READ-DIRECTION.
031486     MOVE "AT2" TO TDB-READ-AT.
031488     MOVE WS-PROCESS-DATE TO TDB-READ-DATE.
031490************ PERFORM TDB-CUST-INQ
031492     PERFORM Z-14-PROCEDURE THRU Z-14-XIT.
031494     IF  Z-EXIT-EDITEXIT
031496         GO TO Z-11-XIT.
031498     IF  Z-DMS2-ABORT-FLAG = 1
031500         GO TO Z-11-XIT.
031502     IF  Z-EXIT-LEVEL < 0
031504         GO TO Z-11-END.
031506*
031508     IF TDB-ERROR-NBR = 0
031510         NEXT SENTENCE
031512     ELSE
031514         GO TO Z-11-22-END-MOVE.
031516     MOVE TDB-TDAC-BANK OF TDB-TDACUST TO HOLD-TDAC-BANK OF       
031518         HOLD-TDACUST.
031520     MOVE TDB-TDAC-CUST OF TDB-TDACUST TO HOLD-TDAC-CUST OF       
031522         HOLD-TDACUST.
031524     MOVE TDB-TDAC-BRCH OF TDB-TDACUST TO HOLD-TDAC-BRCH OF       
031526         HOLD-TDACUST.
031528     MOVE TDB-TDAC-STATUS OF TDB-TDACUST TO HOLD-TDAC-STATUS OF   
031530         HOLD-TDACUST.
031532     MOVE TDB-TDAC-NAME-1 OF TDB-TDACUST TO HOLD-TDAC-NAME-1 OF   
031534         HOLD-TDACUST.
031536     MOVE TDB-TDAC-N1-KEY OF TDB-TDACUST TO HOLD-TDAC-N1-KEY OF   
031538         HOLD-TDACUST.
031540     MOVE TDB-TDAC-N1-FIRST OF TDB-TDACUST TO HOLD-TDAC-N1-FIRST  
031542         OF HOLD-TDACUST.
031544     MOVE TDB-TDAC-N1-MID OF TDB-TDACUST TO HOLD-TDAC-N1-MID OF   
031546         HOLD-TDACUST.
031548     MOVE TDB-TDAC-N1-LAST OF TDB-TDACUST TO HOLD-TDAC-N1-LAST OF 
031550         HOLD-TDACUST.
031552     MOVE TDB-TDAC-N1-PREFIX OF TDB-TDACUST TO                    
031554         HOLD-TDAC-N1-PREFIX OF HOLD-TDACUST.
031556     MOVE TDB-TDAC-N1-SUFFIX OF TDB-TDACUST TO                    
031558         HOLD-TDAC-N1-SUFFIX OF HOLD-TDACUST.
031560     MOVE TDB-TDAC-N1-FAMILIAR OF TDB-TDACUST TO                  
031562         HOLD-TDAC-N1-FAMILIAR OF HOLD-TDACUST.
031564     MOVE TDB-TDAC-N1-PRT-PFX OF TDB-TDACUST TO                   
031566         HOLD-TDAC-N1-PRT-PFX OF HOLD-TDACUST.
031568     MOVE TDB-TDAC-N1-PRT-SFX OF TDB-TDACUST TO                   
031570         HOLD-TDAC-N1-PRT-SFX OF HOLD-TDACUST.
031572     MOVE TDB-TDAC-N1-DESIGNAT OF TDB-TDACUST TO                  
031574         HOLD-TDAC-N1-DESIGNAT OF HOLD-TDACUST.
031576     MOVE TDB-TDAC-NAME-2 OF TDB-TDACUST TO HOLD-TDAC-NAME-2 OF   
031578         HOLD-TDACUST.
031580     MOVE TDB-TDAC-N2-MODIFIED OF TDB-TDACUST TO                  
031582         HOLD-TDAC-N2-MODIFIED OF HOLD-TDACUST.
031584     MOVE TDB-TDAC-N2-PRINT-CD OF TDB-TDACUST TO                  
031586         HOLD-TDAC-N2-PRINT-CD OF HOLD-TDACUST.
031588     MOVE TDB-TDAC-N2-KEY OF TDB-TDACUST TO HOLD-TDAC-N2-KEY OF   
031590         HOLD-TDACUST.
031592     MOVE TDB-TDAC-N2-FIRST OF TDB-TDACUST TO HOLD-TDAC-N2-FIRST  
031594         OF HOLD-TDACUST.
031596     MOVE TDB-TDAC-N2-MID OF TDB-TDACUST TO HOLD-TDAC-N2-MID OF   
031598         HOLD-TDACUST.
031600     MOVE TDB-TDAC-N2-LAST OF TDB-TDACUST TO HOLD-TDAC-N2-LAST OF 
031602         HOLD-TDACUST.
031604     MOVE TDB-TDAC-N2-PREFIX OF TDB-TDACUST TO                    
031606         HOLD-TDAC-N2-PREFIX OF HOLD-TDACUST.
031608     MOVE TDB-TDAC-N2-SUFFIX OF TDB-TDACUST TO                    
031610         HOLD-TDAC-N2-SUFFIX OF HOLD-TDACUST.
031612     MOVE TDB-TDAC-N2-FAMILIAR OF TDB-TDACUST TO                  
031614         HOLD-TDAC-N2-FAMILIAR OF HOLD-TDACUST.
031616     MOVE TDB-TDAC-N2-PRT-PFX OF TDB-TDACUST TO                   
031618         HOLD-TDAC-N2-PRT-PFX OF HOLD-TDACUST.
031620     MOVE TDB-TDAC-N2-PRT-SFX OF TDB-TDACUST TO                   
031622         HOLD-TDAC-N2-PRT-SFX OF HOLD-TDACUST.
031624     MOVE TDB-TDAC-N2-DESIGNAT OF TDB-TDACUST TO                  
031626         HOLD-TDAC-N2-DESIGNAT OF HOLD-TDACUST.
031628     MOVE TDB-TDAC-NAME-3 OF TDB-TDACUST TO HOLD-TDAC-NAME-3 OF   
031630         HOLD-TDACUST.
031632     MOVE TDB-TDAC-N3-MODIFIED OF TDB-TDACUST TO                  
031634         HOLD-TDAC-N3-MODIFIED OF HOLD-TDACUST.
031636     MOVE TDB-TDAC-N3-PRINT-CD OF TDB-TDACUST TO                  
031638         HOLD-TDAC-N3-PRINT-CD OF HOLD-TDACUST.
031640     MOVE TDB-TDAC-N3-KEY OF TDB-TDACUST TO HOLD-TDAC-N3-KEY OF   
031642         HOLD-TDACUST.
031644     MOVE TDB-TDAC-N3-FIRST OF TDB-TDACUST TO HOLD-TDAC-N3-FIRST  
031646         OF HOLD-TDACUST.
031648     MOVE TDB-TDAC-N3-MID OF TDB-TDACUST TO HOLD-TDAC-N3-MID OF   
031650         HOLD-TDACUST.
031652     MOVE TDB-TDAC-N3-LAST OF TDB-TDACUST TO HOLD-TDAC-N3-LAST OF 
031654         HOLD-TDACUST.
031656     MOVE TDB-TDAC-N3-PREFIX OF TDB-TDACUST TO                    
031658         HOLD-TDAC-N3-PREFIX OF HOLD-TDACUST.
031660     MOVE TDB-TDAC-N3-SUFFIX OF TDB-TDACUST TO                    
031662         HOLD-TDAC-N3-SUFFIX OF HOLD-TDACUST.
031664     MOVE TDB-TDAC-N3-FAMILIAR OF TDB-TDACUST TO                  
031666         HOLD-TDAC-N3-FAMILIAR OF HOLD-TDACUST.
031668     MOVE TDB-TDAC-N3-PRT-PFX OF TDB-TDACUST TO                   
031670         HOLD-TDAC-N3-PRT-PFX OF HOLD-TDACUST.
031672     MOVE TDB-TDAC-N3-PRT-SFX OF TDB-TDACUST TO                   
031674         HOLD-TDAC-N3-PRT-SFX OF HOLD-TDACUST.
031676     MOVE TDB-TDAC-N3-DESIGNAT OF TDB-TDACUST TO                  
031678         HOLD-TDAC-N3-DESIGNAT OF HOLD-TDACUST.
031680     MOVE TDB-TDAC-ADDR-KEY OF TDB-TDACUST TO HOLD-TDAC-ADDR-KEY  
031682         OF HOLD-TDACUST.
031684     MOVE TDB-TDAC-ADDR-1 OF TDB-TDACUST TO HOLD-TDAC-ADDR-1 OF   
031686         HOLD-TDACUST.
031688     MOVE TDB-TDAC-ADDR-2 OF TDB-TDACUST TO HOLD-TDAC-ADDR-2 OF   
031690         HOLD-TDACUST.
031692     MOVE TDB-TDAC-CITY OF TDB-TDACUST TO HOLD-TDAC-CITY OF       
031694         HOLD-TDACUST.
031696     MOVE TDB-TDAC-STATE OF TDB-TDACUST TO HOLD-TDAC-STATE OF     
031698         HOLD-TDACUST.
031700     MOVE TDB-TDAC-PROVINCE OF TDB-TDACUST TO HOLD-TDAC-PROVINCE  
031702         OF HOLD-TDACUST.
031704     MOVE TDB-TDAC-COUNTRY OF TDB-TDACUST TO HOLD-TDAC-COUNTRY OF 
```

⚠️  This is the source code you must document.
    528 lines from 15321 to 15848.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

