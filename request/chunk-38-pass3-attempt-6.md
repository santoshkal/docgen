# LLM Request Debug File
Generated: 2025-11-18T19:55:13.913023

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 38/55
- **Model**: gpt-4.1
- **Chunk Number**: 38
- **Pass Number**: 3
- **Attempt Number**: 6 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,086 tokens
- **User Prompt**: ~7,481 tokens
- **Total Input**: ~9,567 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 38/55" (ID: detailed-code-explanation)

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


**CHUNK 38 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T18:05:37.383587", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 38 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 18377 to 18826 (450 lines)\nChunk Tokens (estimated): ~8,081\nActual Input Tokens: 9,487 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 18377-18826 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 38 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 38 of 55.\n\n\n=============================================================================\nCHUNK 38 SOURCE CODE (Lines 18377-18826)\n=============================================================================\n\n```cobol\n036762         TDB-TDACUST.\n036764     MOVE TDAC-N1-MID OF TDACUST TO TDB-TDAC-N1-MID OF            \n036766         TDB-TDACUST.\n036768     MOVE TDAC-N1-LAST OF TDACUST TO TDB-TDAC-N1-LAST OF          \n036770         TDB-TDACUST.\n036772     MOVE TDAC-N1-PREFIX OF TDACUST TO TDB-TDAC-N1-PREFIX OF      \n036774         TDB-TDACUST.\n036776     MOVE TDAC-N1-SUFFIX OF TDACUST TO TDB-TDAC-N1-SUFFIX OF      \n036778         TDB-TDACUST.\n036780     MOVE TDAC-N1-FAMILIAR OF TDACUST TO TDB-TDAC-N1-FAMILIAR OF  \n036782         TDB-TDACUST.\n036784     MOVE TDAC-N1-PRT-PFX OF TDACUST TO TDB-TDAC-N1-PRT-PFX OF    \n036786         TDB-TDACUST.\n036788     MOVE TDAC-N1-PRT-SFX OF TDACUST TO TDB-TDAC-N1-PRT-SFX OF    \n036790         TDB-TDACUST.\n036792     MOVE TDAC-N1-DESIGNAT OF TDACUST TO TDB-TDAC-N1-DESIGNAT OF  \n036794         TDB-TDACUST.\n036796     MOVE TDAC-NAME-2 OF TDACUST TO TDB-TDAC-NAME-2 OF            \n036798         TDB-TDACUST.\n036800     MOVE TDAC-N2-MODIFIED OF TDACUST TO TDB-TDAC-N2-MODIFIED OF  \n036802         TDB-TDACUST.\n036804     MOVE TDAC-N2-PRINT-CD OF TDACUST TO TDB-TDAC-N2-PRINT-CD OF  \n036806         TDB-TDACUST.\n036808     MOVE TDAC-N2-KEY OF TDACUST TO TDB-TDAC-N2-KEY OF            \n036810         TDB-TDACUST.\n036812     MOVE TDAC-N2-FIRST OF TDACUST TO TDB-TDAC-N2-FIRST OF        \n036814         TDB-TDACUST.\n036816     MOVE TDAC-N2-MID OF TDACUST TO TDB-TDAC-N2-MID OF            \n036818         TDB-TDACUST.\n036820     MOVE TDAC-N2-LAST OF TDACUST TO TDB-TDAC-N2-LAST OF          \n036822         TDB-TDACUST.\n036824     MOVE TDAC-N2-PREFIX OF TDACUST TO TDB-TDAC-N2-PREFIX OF      \n036826         TDB-TDACUST.\n036828     MOVE TDAC-N2-SUFFIX OF TDACUST TO TDB-TDAC-N2-SUFFIX OF      \n036830         TDB-TDACUST.\n036832     MOVE TDAC-N2-FAMILIAR OF TDACUST TO TDB-TDAC-N2-FAMILIAR OF  \n036834         TDB-TDACUST.\n036836     MOVE TDAC-N2-PRT-PFX OF TDACUST TO TDB-TDAC-N2-PRT-PFX OF    \n036838         TDB-TDACUST.\n036840     MOVE TDAC-N2-PRT-SFX OF TDACUST TO TDB-TDAC-N2-PRT-SFX OF    \n036842         TDB-TDACUST.\n036844     MOVE TDAC-N2-DESIGNAT OF TDACUST TO TDB-TDAC-N2-DESIGNAT OF  \n036846         TDB-TDACUST.\n036848     MOVE TDAC-NAME-3 OF TDACUST TO TDB-TDAC-NAME-3 OF            \n036850         TDB-TDACUST.\n036852     MOVE TDAC-N3-MODIFIED OF TDACUST TO TDB-TDAC-N3-MODIFIED OF  \n036854         TDB-TDACUST.\n036856     MOVE TDAC-N3-PRINT-CD OF TDACUST TO TDB-TDAC-N3-PRINT-CD OF  \n036858         TDB-TDACUST.\n036860     MOVE TDAC-N3-KEY OF TDACUST TO TDB-TDAC-N3-KEY OF            \n036862         TDB-TDACUST.\n036864     MOVE TDAC-N3-FIRST OF TDACUST TO TDB-TDAC-N3-FIRST OF        \n036866         TDB-TDACUST.\n036868     MOVE TDAC-N3-MID OF TDACUST TO TDB-TDAC-N3-MID OF            \n036870         TDB-TDACUST.\n036872     MOVE TDAC-N3-LAST OF TDACUST TO TDB-TDAC-N3-LAST OF          \n036874         TDB-TDACUST.\n036876     MOVE TDAC-N3-PREFIX OF TDACUST TO TDB-TDAC-N3-PREFIX OF      \n036878         TDB-TDACUST.\n036880     MOVE TDAC-N3-SUFFIX OF TDACUST TO TDB-TDAC-N3-SUFFIX OF      \n036882         TDB-TDACUST.\n036884     MOVE TDAC-N3-FAMILIAR OF TDACUST TO TDB-TDAC-N3-FAMILIAR OF  \n036886         TDB-TDACUST.\n036888     MOVE TDAC-N3-PRT-PFX OF TDACUST TO TDB-TDAC-N3-PRT-PFX OF    \n036890         TDB-TDACUST.\n036892     MOVE TDAC-N3-PRT-SFX OF TDACUST TO TDB-TDAC-N3-PRT-SFX OF    \n036894         TDB-TDACUST.\n036896     MOVE TDAC-N3-DESIGNAT OF TDACUST TO TDB-TDAC-N3-DESIGNAT OF  \n036898         TDB-TDACUST.\n036900     MOVE TDAC-ADDR-KEY OF TDACUST TO TDB-TDAC-ADDR-KEY OF        \n036902         TDB-TDACUST.\n036904     MOVE TDAC-ADDR-1 OF TDACUST TO TDB-TDAC-ADDR-1 OF            \n036906         TDB-TDACUST.\n036908     MOVE TDAC-ADDR-2 OF TDACUST TO TDB-TDAC-ADDR-2 OF            \n036910         TDB-TDACUST.\n036912     MOVE TDAC-CITY OF TDACUST TO TDB-TDAC-CITY OF TDB-TDACUST.\n036914     MOVE TDAC-STATE OF TDACUST TO TDB-TDAC-STATE OF TDB-TDACUST.\n036916     MOVE TDAC-PROVINCE OF TDACUST TO TDB-TDAC-PROVINCE OF        \n036918         TDB-TDACUST.\n036920     MOVE TDAC-COUNTRY OF TDACUST TO TDB-TDAC-COUNTRY OF          \n036922         TDB-TDACUST.\n036924     MOVE TDAC-ZIP OF TDACUST TO TDB-TDAC-ZIP OF TDB-TDACUST.\n036926     MOVE TDAC-ZIP-4 OF TDACUST TO TDB-TDAC-ZIP-4 OF TDB-TDACUST.\n036928     MOVE TDAC-LONGITUDE OF TDACUST TO TDB-TDAC-LONGITUDE OF      \n036930         TDB-TDACUST.\n036932     MOVE TDAC-LATITUDE OF TDACUST TO TDB-TDAC-LATITUDE OF        \n036934         TDB-TDACUST.\n036936     MOVE TDAC-MAIL-CD OF TDACUST TO TDB-TDAC-MAIL-CD OF          \n036938         TDB-TDACUST.\n036940     MOVE TDAC-TICKLER-FLAG OF TDACUST TO TDB-TDAC-TICKLER-FLAG   \n036942         OF TDB-TDACUST.\n036944     MOVE TDAC-RESIDENT-CD OF TDACUST TO TDB-TDAC-RESIDENT-CD OF  \n036946         TDB-TDACUST.\n036948     MOVE TDAC-ALIEN-CD OF TDACUST TO TDB-TDAC-ALIEN-CD OF        \n036950         TDB-TDACUST.\n036952     MOVE TDAC-SHT-NAME OF TDACUST TO TDB-TDAC-SHT-NAME OF        \n036954         TDB-TDACUST.\n036956     MOVE TDAC-BAR-CD OF TDACUST TO TDB-TDAC-BAR-CD OF            \n036958         TDB-TDACUST.\n036960     MOVE TDAC-PHONE-1 OF TDACUST TO TDB-TDAC-PHONE-1 OF          \n036962         TDB-TDACUST.\n036964     MOVE TDAC-PHONE-2 OF TDACUST TO TDB-TDAC-PHONE-2 OF          \n036966         TDB-TDACUST.\n036968     MOVE TDAC-TIN-CD OF TDACUST TO TDB-TDAC-TIN-CD OF            \n036970         TDB-TDACUST.\n036972     MOVE TDAC-TIN-CERT-CD OF TDACUST TO TDB-TDAC-TIN-CERT-CD OF  \n036974         TDB-TDACUST.\n036976     MOVE TDAC-TIN-CERT-DT OF TDACUST TO TDB-TDAC-TIN-CERT-DT OF  \n036978         TDB-TDACUST.\n036980     MOVE TDAC-TIN-NBR OF TDACUST TO TDB-TDAC-TIN-NBR OF          \n036982         TDB-TDACUST.\n036984     MOVE TDAC-OFFICER OF TDACUST TO TDB-TDAC-OFFICER OF          \n036986         TDB-TDACUST.\n036988     MOVE TDAC-EMP-CD OF TDACUST TO TDB-TDAC-EMP-CD OF            \n036990         TDB-TDACUST.\n036992     MOVE TDAC-FREE-MARK OF TDACUST TO TDB-TDAC-FREE-MARK OF      \n036994         TDB-TDACUST.\n036996     MOVE TDAC-INQ-SECR-CD OF TDACUST TO TDB-TDAC-INQ-SECR-CD OF  \n036998         TDB-TDACUST.\n037000     MOVE TDAC-PRIVACY OF TDACUST TO TDB-TDAC-PRIVACY OF          \n037002         TDB-TDACUST.\n037004     MOVE TDAC-BK-DEF-CD1 OF TDACUST TO TDB-TDAC-BK-DEF-CD1 OF    \n037006         TDB-TDACUST.\n037008     MOVE TDAC-BK-DEF-CD2 OF TDACUST TO TDB-TDAC-BK-DEF-CD2 OF    \n037010         TDB-TDACUST.\n037012     MOVE TDAC-BK-DEF-CD3 OF TDACUST TO TDB-TDAC-BK-DEF-CD3 OF    \n037014         TDB-TDACUST.\n037016     MOVE TDAC-BK-DEF-CD4 OF TDACUST TO TDB-TDAC-BK-DEF-CD4 OF    \n037018         TDB-TDACUST.\n037020     MOVE TDAC-BK-DEF-CD5 OF TDACUST TO TDB-TDAC-BK-DEF-CD5 OF    \n037022         TDB-TDACUST.\n037024     MOVE TDAC-EMPLOYEE-ID OF TDACUST TO TDB-TDAC-EMPLOYEE-ID OF  \n037026         TDB-TDACUST.\n037028     MOVE TDAC-EMAIL-ADDR OF TDACUST TO TDB-TDAC-EMAIL-ADDR OF    \n037030         TDB-TDACUST.\n037032     MOVE TDAC-EMAIL-PSSWRD OF TDACUST TO TDB-TDAC-EMAIL-PSSWRD   \n037034         OF TDB-TDACUST.\n037036     MOVE TDAC-GENDER OF TDACUST TO TDB-TDAC-GENDER OF            \n037038         TDB-TDACUST.\n037040     MOVE TDAC-NEW-CUST OF TDACUST TO TDB-TDAC-NEW-CUST OF        \n037042         TDB-TDACUST.\n037044     MOVE TDAC-OPEN-DT OF TDACUST TO TDB-TDAC-OPEN-DT OF          \n037046         TDB-TDACUST.\n037048     MOVE TDAC-LUPD-DATE OF TDACUST TO TDB-TDAC-LUPD-DATE OF      \n037050         TDB-TDACUST.\n037052     MOVE TDAC-LUPD-TIME OF TDACUST TO TDB-TDAC-LUPD-TIME OF      \n037054         TDB-TDACUST.\n037056     MOVE TDAC-LST-CONTACT OF TDACUST TO TDB-TDAC-LST-CONTACT OF  \n037058         TDB-TDACUST.\n037060     MOVE TDAC-BIRTH-DT OF TDACUST TO TDB-TDAC-BIRTH-DT OF        \n037062         TDB-TDACUST.\n037064     MOVE TDAC-BIRTH-DT-2 OF TDACUST TO TDB-TDAC-BIRTH-DT-2 OF    \n037066         TDB-TDACUST.\n037068     MOVE TDAC-BIRTH-DT-3 OF TDACUST TO TDB-TDAC-BIRTH-DT-3 OF    \n037070         TDB-TDACUST.\n037072     MOVE TDAC-DEATH-DT OF TDACUST TO TDB-TDAC-DEATH-DT OF        \n037074         TDB-TDACUST.\n037076     MOVE TDAC-ADD-DT OF TDACUST TO TDB-TDAC-ADD-DT OF            \n037078         TDB-TDACUST.\n037080     MOVE TDAC-ADD-TM OF TDACUST TO TDB-TDAC-ADD-TM OF            \n037082         TDB-TDACUST.\n037084     MOVE TDAC-ROTH-DATE OF TDACUST TO TDB-TDAC-ROTH-DATE OF      \n037086         TDB-TDACUST.\n037088     MOVE TDAC-CD-BAL OF TDACUST TO TDB-TDAC-CD-BAL OF            \n037090         TDB-TDACUST.\n037092     MOVE TDAC-CD-BAL-BYR OF TDACUST TO TDB-TDAC-CD-BAL-BYR OF    \n037094         TDB-TDACUST.\n037096     MOVE TDAC-CD-PENLTY OF TDACUST TO TDB-TDAC-CD-PENLTY OF      \n037098         TDB-TDACUST.\n037100     MOVE TDAC-CD-WTHLD OF TDACUST TO TDB-TDAC-CD-WTHLD OF        \n037102         TDB-TDACUST.\n037104     MOVE TDAC-CD-INT OF TDACUST TO TDB-TDAC-CD-INT OF            \n037106         TDB-TDACUST.\n037108     MOVE TDAC-CD-OID-INT OF TDACUST TO TDB-TDAC-CD-OID-INT OF    \n037110         TDB-TDACUST.\n037112     MOVE TDAC-IRA-BAL OF TDACUST TO TDB-TDAC-IRA-BAL OF          \n037114         TDB-TDACUST.\n037116     MOVE TDAC-IRA-BAL-BYR OF TDACUST TO TDB-TDAC-IRA-BAL-BYR OF  \n037118         TDB-TDACUST.\n037120     MOVE TDAC-IRA-PENLTY OF TDACUST TO TDB-TDAC-IRA-PENLTY OF    \n037122         TDB-TDACUST.\n037124     MOVE TDAC-IRA-WTHLD OF TDACUST TO TDB-TDAC-IRA-WTHLD OF      \n037126         TDB-TDACUST.\n037128     MOVE TDAC-IRA-INT OF TDACUST TO TDB-TDAC-IRA-INT OF          \n037130         TDB-TDACUST.\n037132     MOVE TDAC-IRA-CONTR OF TDACUST TO TDB-TDAC-IRA-CONTR OF      \n037134         TDB-TDACUST.\n037136     MOVE TDAC-IRA-CONTR-LY OF TDACUST TO TDB-TDAC-IRA-CONTR-LY   \n037138         OF TDB-TDACUST.\n037140     MOVE TDAC-IRA-DISTR OF TDACUST TO TDB-TDAC-IRA-DISTR OF      \n037142         TDB-TDACUST.\n037144     MOVE TDAC-IRA-DISTR-LY OF TDACUST TO TDB-TDAC-IRA-DISTR-LY   \n037146         OF TDB-TDACUST.\n037148     MOVE TDAC-IRA-ROLLOVER OF TDACUST TO TDB-TDAC-IRA-ROLLOVER   \n037150         OF TDB-TDACUST.\n037152     MOVE TDAC-IRA-TRF-IN OF TDACUST TO TDB-TDAC-IRA-TRF-IN OF    \n037154         TDB-TDACUST.\n037156     MOVE TDAC-IRA-TRF-OUT OF TDACUST TO TDB-TDAC-IRA-TRF-OUT OF  \n037158         TDB-TDACUST.\n037160     MOVE TDAC-IRA-FAIR-MKT OF TDACUST TO TDB-TDAC-IRA-FAIR-MKT   \n037162         OF TDB-TDACUST.\n037164     MOVE TDAC-CIF-REMARK OF TDACUST TO TDB-TDAC-CIF-REMARK OF    \n037166         TDB-TDACUST.\n037168     MOVE TDAC-CD-ST-WHLD OF TDACUST TO TDB-TDAC-CD-ST-WHLD OF    \n037170         TDB-TDACUST.\n037172     MOVE TDAC-IRA-ST-WHLD OF TDACUST TO TDB-TDAC-IRA-ST-WHLD OF  \n037174         TDB-TDACUST.\n037176     MOVE 1 TO Z-II.\n037178 Z-5-8-1-LOOP.\n037180     IF Z-II > 12\n037182         GO TO Z-5-8-1-LOOP-XIT.\n037184     MOVE TDAC-CURR-YR-AMT OF TDACUST (Z-II) TO                   \n037186         TDB-TDAC-CURR-YR-AMT OF TDB-TDACUST (Z-II).\n037188     MOVE TDAC-LAST-YR-AMT OF TDACUST (Z-II) TO                   \n037190         TDB-TDAC-LAST-YR-AMT OF TDB-TDACUST (Z-II).\n037192     ADD 1 TO Z-II.\n037194     GO TO Z-5-8-1-LOOP.\n037196 Z-5-8-1-LOOP-XIT.\n037198     MOVE TDAC-TIN-CD-2 OF TDACUST TO TDB-TDAC-TIN-CD-2 OF        \n037200         TDB-TDACUST.\n037202     MOVE TDAC-TIN-CRT-CD-2 OF TDACUST TO TDB-TDAC-TIN-CRT-CD-2   \n037204         OF TDB-TDACUST.\n037206     MOVE TDAC-TIN-CRT-DT-2 OF TDACUST TO TDB-TDAC-TIN-CRT-DT-2   \n037208         OF TDB-TDACUST.\n037210     MOVE TDAC-TIN-NBR-2 OF TDACUST TO TDB-TDAC-TIN-NBR-2 OF      \n037212         TDB-TDACUST.\n037214     MOVE TDAC-TIN-CD-3 OF TDACUST TO TDB-TDAC-TIN-CD-3 OF        \n037216         TDB-TDACUST.\n037218     MOVE TDAC-TIN-CRT-CD-3 OF TDACUST TO TDB-TDAC-TIN-CRT-CD-3   \n037220         OF TDB-TDACUST.\n037222     MOVE TDAC-TIN-CRT-DT-3 OF TDACUST TO TDB-TDAC-TIN-CRT-DT-3   \n037224         OF TDB-TDACUST.\n037226     MOVE TDAC-TIN-NBR-3 OF TDACUST TO TDB-TDAC-TIN-NBR-3 OF      \n037228         TDB-TDACUST.\n037230     MOVE TDAC-NAICS-CD OF TDACUST TO TDB-TDAC-NAICS-CD OF        \n037232         TDB-TDACUST.\n037234     MOVE TDAC-CIF-PASS-THR OF TDACUST TO TDB-TDAC-CIF-PASS-THR   \n037236         OF TDB-TDACUST.\n037238     MOVE TDAC-EMAIL-NTC OF TDACUST TO TDB-TDAC-EMAIL-NTC OF      \n037240         TDB-TDACUST.\n037242     MOVE TDAC-RMD-YR-AMT OF TDACUST TO TDB-TDAC-RMD-YR-AMT OF    \n037244         TDB-TDACUST.\n037246     MOVE TDAC-ADDR-CHG-DT OF TDACUST TO TDB-TDAC-ADDR-CHG-DT OF  \n037248         TDB-TDACUST.\n037250     MOVE TDAC-WTHLD-CD OF TDACUST TO TDB-TDAC-WTHLD-CD OF        \n037252         TDB-TDACUST.\n037254     MOVE TDAC-ST-WHLD-CD OF TDACUST TO TDB-TDAC-ST-WHLD-CD OF    \n037256         TDB-TDACUST.\n037258     MOVE TDAC-WTHLD-AMT OF TDACUST TO TDB-TDAC-WTHLD-AMT OF      \n037260         TDB-TDACUST.\n037262     MOVE TDAC-ST-WHLD-AMT OF TDACUST TO TDB-TDAC-ST-WHLD-AMT OF  \n037264         TDB-TDACUST.\n037266     MOVE TDAC-FOREIGN-LANG OF TDACUST TO TDB-TDAC-FOREIGN-LANG   \n037268         OF TDB-TDACUST.\n037270     MOVE TDAC-L-ROLLOVR-DT OF TDACUST TO TDB-TDAC-L-ROLLOVR-DT   \n037272         OF TDB-TDACUST.\n037274     MOVE TDAC-CUSTM-FIELDS OF TDACUST TO TDB-TDAC-CUSTM-FIELDS   \n037276         OF TDB-TDACUST.\n037278     MOVE TDAC-LLC-NAME OF TDACUST TO TDB-TDAC-LLC-NAME OF        \n037280         TDB-TDACUST.\n037282     MOVE TDAC-LLC-TIN-CD OF TDACUST TO TDB-TDAC-LLC-TIN-CD OF    \n037284         TDB-TDACUST.\n037286     MOVE TDAC-LLC-TIN OF TDACUST TO TDB-TDAC-LLC-TIN OF          \n037288         TDB-TDACUST.\n037290     MOVE TDAC-FOREIGN-PHN OF TDACUST TO TDB-TDAC-FOREIGN-PHN OF  \n037292         TDB-TDACUST.\n037294     IF ( TDAC-TIN-NBR NOT = WS-PREV-TIN ) AND ( WS-1ST-TIME = 1 )\n037296         NEXT SENTENCE ELSE\n037298         GO TO Z-5-9-1-ELSE.\n037300************ PERFORM WRITE-CUST-FM-REC\n037302     PERFORM Z-26-PROCEDURE THRU Z-26-XIT.\n037304     IF  Z-EXIT-EDITEXIT\n037306         GO TO Z-5-XIT.\n037308     IF  Z-DMS2-ABORT-FLAG = 1\n037310         GO TO Z-5-XIT.\n037312     IF  Z-EXIT-LEVEL < 0\n037314         GO TO Z-5-3-END.\n037316*\n037318     MOVE SPACES TO WS-TIN-CUST-TABLE.\n037320     MOVE 0 TO WS-TIN-CUST-INDEX.\n037322 Z-5-9-1-ELSE.\n037324     MOVE 0 TO WS-RMDFM2-CUST-IND.\n037326     MOVE ZERO TO Z-FLINFO12-PRES.\n037328     MOVE ZERO TO Z-FLINFO12-SOME.\n037330     MOVE 9 TO Z-FLINFO12-LAST-SEQ.\n037332*\n037334     SET TDAIRASET OF TDAIRA OF LDBTDADB TO BEGINNING\n037336         ON EXCEPTION\n037338         MOVE \"TDAIRASET OF TDAIRA OF LDBTDADB\" TO                \n037340             Z-DMS-EXCEPT-STR\n037342         MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n037344         MOVE 9 TO Z-DMS-EXCEPT-SEQ\n037346         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT\n037348         GO TO Z-5-14-XIT.\n037350 Z-5-14-LOOP.\n037352     MOVE ZERO TO Z-FLINFO12-PRES.\n037354 Z-5-14-READ.\n037356     FIND TDAIRA OF LDBTDADB VIA NEXT TDAIRASET OF TDAIRA OF      \n037358         LDBTDADB\n037360     AT TDAI-BANK = WS-BANK-NO AND\n037362        TDAI-CUST = TDB-TDAC-CUST\n037364         ON EXCEPTION\n037366         MOVE 9 TO Z-DMS-EXCEPT-SEQ\n037368         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n037370             GO TO Z-5-14-XIT\n037372         ELSE\n037374             MOVE \"TDAIRASET OF TDAIRA OF LDBTDADB\" TO            \n037376                 Z-DMS-EXCEPT-STR\n037378             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n037380             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n037382\n037384*\n037386     MOVE 1 TO Z-FLINFO12-PRES.\n037388     MOVE 1 TO Z-FLINFO12-SOME.\n037390     MOVE 0 TO Z-EXIT-CODE.\n037392     MOVE 9999 TO Z-EXIT-LEVEL.\n037394     IF Z-FLINFO12-ABSENT\n037396         NEXT SENTENCE ELSE\n037398         GO TO Z-5-15-1-ELSE.\n037400     MOVE 2 TO Z-EXIT-LEVEL\n037402     GO TO Z-5-14-END.\n037404 Z-5-15-1-ELSE.\n037406     MOVE TDAI-BANK OF TDAIRA TO TDB-TDAI-BANK OF TDB-TDAIRA.\n037408     MOVE TDAI-BRCH OF TDAIRA TO TDB-TDAI-BRCH OF TDB-TDAIRA.\n037410     MOVE TDAI-CUST OF TDAIRA TO TDB-TDAI-CUST OF TDB-TDAIRA.\n037412     MOVE TDAI-ACCT OF TDAIRA TO TDB-TDAI-ACCT OF TDB-TDAIRA.\n037414     MOVE TDAI-PUB-ID OF TDAIRA TO TDB-TDAI-PUB-ID OF TDB-TDAIRA.\n037416     MOVE TDAI-ADD-DT OF TDAIRA TO TDB-TDAI-ADD-DT OF TDB-TDAIRA.\n037418     MOVE TDAI-ADD-TM OF TDAIRA TO TDB-TDAI-ADD-TM OF TDB-TDAIRA.\n037420     MOVE 1 TO Z-II.\n037422 Z-5-17-1-LOOP.\n037424     IF Z-II > 20\n037426         GO TO Z-5-17-1-LOOP-XIT.\n037428     MOVE TDAI-DS-TYPE OF TDAIRA (Z-II) TO TDB-TDAI-DS-TYPE OF    \n037430         TDB-TDAIRA (Z-II).\n037432     MOVE TDAI-CN-TYPE OF TDAIRA (Z-II) TO TDB-TDAI-CN-TYPE OF    \n037434         TDB-TDAIRA (Z-II).\n037436     MOVE TDAI-DS-CN-AMT OF TDAIRA (Z-II) TO TDB-TDAI-DS-CN-AMT   \n037438         OF TDB-TDAIRA (Z-II).\n037440     MOVE TDAI-DS-PEN-AMT OF TDAIRA (Z-II) TO TDB-TDAI-DS-PEN-AMT \n037442         OF TDB-TDAIRA (Z-II).\n037444     MOVE TDAI-DS-WTHLD-AMT OF TDAIRA (Z-II) TO                   \n037446         TDB-TDAI-DS-WTHLD-AMT OF TDB-TDAIRA (Z-II).\n037448     MOVE TDAI-DS-ST-WH-AMT OF TDAIRA (Z-II) TO                   \n037450         TDB-TDAI-DS-ST-WH-AMT OF TDB-TDAIRA (Z-II).\n037452     MOVE TDAI-DS-EXC-EARN OF TDAIRA (Z-II) TO                    \n037454         TDB-TDAI-DS-EXC-EARN OF TDB-TDAIRA (Z-II).\n037456     ADD 1 TO Z-II.\n037458     GO TO Z-5-17-1-LOOP.\n037460 Z-5-17-1-LOOP-XIT.\n037462     MOVE TDAI-DS-C-YTD-CNT OF TDAIRA TO TDB-TDAI-DS-C-YTD-CNT OF \n037464         TDB-TDAIRA.\n037466     MOVE TDAI-DS-P-YTD-CNT OF TDAIRA TO TDB-TDAI-DS-P-YTD-CNT OF \n037468         TDB-TDAIRA.\n037470     MOVE TDAI-DS-AMT-C-YTD OF TDAIRA TO TDB-TDAI-DS-AMT-C-YTD OF \n037472         TDB-TDAIRA.\n037474     MOVE TDAI-DS-AMT-P-YTD OF TDAIRA TO TDB-TDAI-DS-AMT-P-YTD OF \n037476         TDB-TDAIRA.\n037478     MOVE TDAI-DS-INT-AMT OF TDAIRA TO TDB-TDAI-DS-INT-AMT OF     \n037480         TDB-TDAIRA.\n037482     MOVE TDAI-CN-YTD-CNT OF TDAIRA TO TDB-TDAI-CN-YTD-CNT OF     \n037484         TDB-TDAIRA.\n037486     MOVE TDAI-CN-YTD-AMT OF TDAIRA TO TDB-TDAI-CN-YTD-AMT OF     \n037488         TDB-TDAIRA.\n037490     MOVE TDAI-CN-LYTD-AMT OF TDAIRA TO TDB-TDAI-CN-LYTD-AMT OF   \n037492         TDB-TDAIRA.\n037494     MOVE TDAI-EMP-CONT-LYR OF TDAIRA TO TDB-TDAI-EMP-CONT-LYR OF \n037496         TDB-TDAIRA.\n037498     MOVE TDAI-REG-CONT-LYR OF TDAIRA TO TDB-TDAI-REG-CONT-LYR OF \n037500         TDB-TDAIRA.\n037502     MOVE TDAI-UNINSURED OF TDAIRA TO TDB-TDAI-UNINSURED OF       \n037504         TDB-TDAIRA.\n037506     MOVE TDAI-ROLLOVER OF TDAIRA TO TDB-TDAI-ROLLOVER OF         \n037508         TDB-TDAIRA.\n037510     MOVE TDAI-ROLLOVER-LYR OF TDAIRA TO TDB-TDAI-ROLLOVER-LYR OF \n037512         TDB-TDAIRA.\n037514     MOVE TDAI-TRANSFER-IN OF TDAIRA TO TDB-TDAI-TRANSFER-IN OF   \n037516         TDB-TDAIRA.\n037518     MOVE TDAI-TRANSFER-OUT OF TDAIRA TO TDB-TDAI-TRANSFER-OUT OF \n037520         TDB-TDAIRA.\n037522     MOVE TDAI-1ST-CN-DATE OF TDAIRA TO TDB-TDAI-1ST-CN-DATE OF   \n037524         TDB-TDAIRA.\n037526     MOVE TDAI-BASIS-C-LTD OF TDAIRA TO TDB-TDAI-BASIS-C-LTD OF   \n037528         TDB-TDAIRA.\n037530     MOVE TDAI-BASIS-D-LTD OF TDAIRA TO TDB-TDAI-BASIS-D-LTD OF   \n037532         TDB-TDAIRA.\n037534     MOVE TDAI-BASIS-D-YTD OF TDAIRA TO TDB-TDAI-BASIS-D-YTD OF   \n037536         TDB-TDAIRA.\n037538     MOVE ZERO TO Z-FLINFO8-PRES.\n037540     MOVE 10 TO Z-FLINFO8-LAST-SEQ.\n037542     MOVE ZERO TO Z-FLINFO8-SOME.\n037544 Z-5-18-READ.\n037546     FIND TDAACCT OF LDBTDADB VIA FIRST TDAAMSET OF TDAACCT OF    \n037548         LDBTDADB\n037550     AT TDAA-BANK = WS-BANK-NO AND\n037552        TDAA-CUST = TDB-TDAI-CUST AND\n037554        TDAA-ACCT = TDB-TDAI-ACCT\n037556         ON EXCEPTION\n037558         MOVE 10 TO Z-DMS-EXCEPT-SEQ\n037560         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n037562             GO TO Z-5-18-XIT\n037564         ELSE\n037566             MOVE \"TDAAMSET OF TDAACCT OF LDBTDADB\" TO            \n037568                 Z-DMS-EXCEPT-STR\n037570             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n037572             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n037574\n037576 Z-5-18-PRESENT.\n037578*\n037580     MOVE 1 TO Z-FLINFO8-SOME.\n037582     MOVE 1 TO Z-FLINFO8-PRES.\n037584     GO TO Z-5-18-CONT.\n037586 Z-5-18-XIT.\n037588 Z-5-18-CONT.\n037590     IF Z-FLINFO8-ABSENT\n037592         NEXT SENTENCE ELSE\n037594         GO TO Z-5-19-1-ELSE.\n037596     MOVE 2 TO Z-EXIT-LEVEL\n037598     GO TO Z-5-14-END.\n037600 Z-5-19-1-ELSE.\n037602     MOVE TDAA-BANK OF TDAACCT TO TDB-TDAA-BANK OF TDB-TDAACCT.\n037604     MOVE TDAA-BRCH OF TDAACCT TO TDB-TDAA-BRCH OF TDB-TDAACCT.\n037606     MOVE TDAA-APPL OF TDAACCT TO TDB-TDAA-APPL OF TDB-TDAACCT.\n037608     MOVE TDAA-CUST OF TDAACCT TO TDB-TDAA-CUST OF TDB-TDAACCT.\n037610     MOVE TDAA-ACCT OF TDAACCT TO TDB-TDAA-ACCT OF TDB-TDAACCT.\n037612     MOVE TDAA-STATUS OF TDAACCT TO TDB-TDAA-STATUS OF            \n037614         TDB-TDAACCT.\n037616     MOVE TDAA-IRA-TYPE OF TDAACCT TO TDB-TDAA-IRA-TYPE OF        \n037618         TDB-TDAACCT.\n037620     MOVE TDAA-ACCT-OPTION OF TDAACCT TO TDB-TDAA-ACCT-OPTION OF  \n037622         TDB-TDAACCT.\n037624     MOVE TDAA-DT-CONDENSED OF TDAACCT TO TDB-TDAA-DT-CONDENSED   \n037626         OF TDB-TDAACCT.\n037628     MOVE TDAA-CERT OF TDAACCT TO TDB-TDAA-CERT OF TDB-TDAACCT.\n037630     MOVE TDAA-SHT-NAME OF TDAACCT TO TDB-TDAA-SHT-NAME OF        \n037632         TDB-TDAACCT.\n037634     MOVE TDAA-TITLE OF TDAACCT TO TDB-TDAA-TITLE OF TDB-TDAACCT.\n037636     MOVE TDAA-TITLE-PRINT OF TDAACCT TO TDB-TDAA-TITLE-PRINT OF  \n037638         TDB-TDAACCT.\n037640     MOVE TDAA-ADDR-USAGE OF TDAACCT TO TDB-TDAA-ADDR-USAGE OF    \n037642         TDB-TDAACCT.\n037644     MOVE TDAA-ADDR-ALT OF TDAACCT TO TDB-TDAA-ADDR-ALT OF        \n037646         TDB-TDAACCT.\n037648     MOVE TDAA-ADDR-TEMP OF TDAACCT TO TDB-TDAA-ADDR-TEMP OF      \n037650         TDB-TDAACCT.\n037652     MOVE TDAA-TEMP-BEG-DT OF TDAACCT TO TDB-TDAA-TEMP-BEG-DT OF  \n037654         TDB-TDAACCT.\n037656     MOVE TDAA-TEMP-END-DT OF TDAACCT TO TDB-TDAA-TEMP-END-DT OF  \n037658         TDB-TDAACCT.\n037660     MOVE TDAA-TEMP-EFF-DT OF TDAACCT TO TDB-TDAA-TEMP-EFF-DT OF  \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    450 lines from 18377 to 18826.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 38, "total_chunks": 55, "start_line": 18377, "end_line": 18826, "line_count": 450}

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
- Source code length: 26775 characters

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
CHUNK 38 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 18377 to 18826 (450 lines)
Chunk Tokens (estimated): ~8,081
Actual Input Tokens: 9,487 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 18377-18826 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 38 of 55 chunks
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
      The source code below is only CHUNK 38 of 55.


=============================================================================
CHUNK 38 SOURCE CODE (Lines 18377-18826)
=============================================================================

```cobol
036762         TDB-TDACUST.
036764     MOVE TDAC-N1-MID OF TDACUST TO TDB-TDAC-N1-MID OF            
036766         TDB-TDACUST.
036768     MOVE TDAC-N1-LAST OF TDACUST TO TDB-TDAC-N1-LAST OF          
036770         TDB-TDACUST.
036772     MOVE TDAC-N1-PREFIX OF TDACUST TO TDB-TDAC-N1-PREFIX OF      
036774         TDB-TDACUST.
036776     MOVE TDAC-N1-SUFFIX OF TDACUST TO TDB-TDAC-N1-SUFFIX OF      
036778         TDB-TDACUST.
036780     MOVE TDAC-N1-FAMILIAR OF TDACUST TO TDB-TDAC-N1-FAMILIAR OF  
036782         TDB-TDACUST.
036784     MOVE TDAC-N1-PRT-PFX OF TDACUST TO TDB-TDAC-N1-PRT-PFX OF    
036786         TDB-TDACUST.
036788     MOVE TDAC-N1-PRT-SFX OF TDACUST TO TDB-TDAC-N1-PRT-SFX OF    
036790         TDB-TDACUST.
036792     MOVE TDAC-N1-DESIGNAT OF TDACUST TO TDB-TDAC-N1-DESIGNAT OF  
036794         TDB-TDACUST.
036796     MOVE TDAC-NAME-2 OF TDACUST TO TDB-TDAC-NAME-2 OF            
036798         TDB-TDACUST.
036800     MOVE TDAC-N2-MODIFIED OF TDACUST TO TDB-TDAC-N2-MODIFIED OF  
036802         TDB-TDACUST.
036804     MOVE TDAC-N2-PRINT-CD OF TDACUST TO TDB-TDAC-N2-PRINT-CD OF  
036806         TDB-TDACUST.
036808     MOVE TDAC-N2-KEY OF TDACUST TO TDB-TDAC-N2-KEY OF            
036810         TDB-TDACUST.
036812     MOVE TDAC-N2-FIRST OF TDACUST TO TDB-TDAC-N2-FIRST OF        
036814         TDB-TDACUST.
036816     MOVE TDAC-N2-MID OF TDACUST TO TDB-TDAC-N2-MID OF            
036818         TDB-TDACUST.
036820     MOVE TDAC-N2-LAST OF TDACUST TO TDB-TDAC-N2-LAST OF          
036822         TDB-TDACUST.
036824     MOVE TDAC-N2-PREFIX OF TDACUST TO TDB-TDAC-N2-PREFIX OF      
036826         TDB-TDACUST.
036828     MOVE TDAC-N2-SUFFIX OF TDACUST TO TDB-TDAC-N2-SUFFIX OF      
036830         TDB-TDACUST.
036832     MOVE TDAC-N2-FAMILIAR OF TDACUST TO TDB-TDAC-N2-FAMILIAR OF  
036834         TDB-TDACUST.
036836     MOVE TDAC-N2-PRT-PFX OF TDACUST TO TDB-TDAC-N2-PRT-PFX OF    
036838         TDB-TDACUST.
036840     MOVE TDAC-N2-PRT-SFX OF TDACUST TO TDB-TDAC-N2-PRT-SFX OF    
036842         TDB-TDACUST.
036844     MOVE TDAC-N2-DESIGNAT OF TDACUST TO TDB-TDAC-N2-DESIGNAT OF  
036846         TDB-TDACUST.
036848     MOVE TDAC-NAME-3 OF TDACUST TO TDB-TDAC-NAME-3 OF            
036850         TDB-TDACUST.
036852     MOVE TDAC-N3-MODIFIED OF TDACUST TO TDB-TDAC-N3-MODIFIED OF  
036854         TDB-TDACUST.
036856     MOVE TDAC-N3-PRINT-CD OF TDACUST TO TDB-TDAC-N3-PRINT-CD OF  
036858         TDB-TDACUST.
036860     MOVE TDAC-N3-KEY OF TDACUST TO TDB-TDAC-N3-KEY OF            
036862         TDB-TDACUST.
036864     MOVE TDAC-N3-FIRST OF TDACUST TO TDB-TDAC-N3-FIRST OF        
036866         TDB-TDACUST.
036868     MOVE TDAC-N3-MID OF TDACUST TO TDB-TDAC-N3-MID OF            
036870         TDB-TDACUST.
036872     MOVE TDAC-N3-LAST OF TDACUST TO TDB-TDAC-N3-LAST OF          
036874         TDB-TDACUST.
036876     MOVE TDAC-N3-PREFIX OF TDACUST TO TDB-TDAC-N3-PREFIX OF      
036878         TDB-TDACUST.
036880     MOVE TDAC-N3-SUFFIX OF TDACUST TO TDB-TDAC-N3-SUFFIX OF      
036882         TDB-TDACUST.
036884     MOVE TDAC-N3-FAMILIAR OF TDACUST TO TDB-TDAC-N3-FAMILIAR OF  
036886         TDB-TDACUST.
036888     MOVE TDAC-N3-PRT-PFX OF TDACUST TO TDB-TDAC-N3-PRT-PFX OF    
036890         TDB-TDACUST.
036892     MOVE TDAC-N3-PRT-SFX OF TDACUST TO TDB-TDAC-N3-PRT-SFX OF    
036894         TDB-TDACUST.
036896     MOVE TDAC-N3-DESIGNAT OF TDACUST TO TDB-TDAC-N3-DESIGNAT OF  
036898         TDB-TDACUST.
036900     MOVE TDAC-ADDR-KEY OF TDACUST TO TDB-TDAC-ADDR-KEY OF        
036902         TDB-TDACUST.
036904     MOVE TDAC-ADDR-1 OF TDACUST TO TDB-TDAC-ADDR-1 OF            
036906         TDB-TDACUST.
036908     MOVE TDAC-ADDR-2 OF TDACUST TO TDB-TDAC-ADDR-2 OF            
036910         TDB-TDACUST.
036912     MOVE TDAC-CITY OF TDACUST TO TDB-TDAC-CITY OF TDB-TDACUST.
036914     MOVE TDAC-STATE OF TDACUST TO TDB-TDAC-STATE OF TDB-TDACUST.
036916     MOVE TDAC-PROVINCE OF TDACUST TO TDB-TDAC-PROVINCE OF        
036918         TDB-TDACUST.
036920     MOVE TDAC-COUNTRY OF TDACUST TO TDB-TDAC-COUNTRY OF          
036922         TDB-TDACUST.
036924     MOVE TDAC-ZIP OF TDACUST TO TDB-TDAC-ZIP OF TDB-TDACUST.
036926     MOVE TDAC-ZIP-4 OF TDACUST TO TDB-TDAC-ZIP-4 OF TDB-TDACUST.
036928     MOVE TDAC-LONGITUDE OF TDACUST TO TDB-TDAC-LONGITUDE OF      
036930         TDB-TDACUST.
036932     MOVE TDAC-LATITUDE OF TDACUST TO TDB-TDAC-LATITUDE OF        
036934         TDB-TDACUST.
036936     MOVE TDAC-MAIL-CD OF TDACUST TO TDB-TDAC-MAIL-CD OF          
036938         TDB-TDACUST.
036940     MOVE TDAC-TICKLER-FLAG OF TDACUST TO TDB-TDAC-TICKLER-FLAG   
036942         OF TDB-TDACUST.
036944     MOVE TDAC-RESIDENT-CD OF TDACUST TO TDB-TDAC-RESIDENT-CD OF  
036946         TDB-TDACUST.
036948     MOVE TDAC-ALIEN-CD OF TDACUST TO TDB-TDAC-ALIEN-CD OF        
036950         TDB-TDACUST.
036952     MOVE TDAC-SHT-NAME OF TDACUST TO TDB-TDAC-SHT-NAME OF        
036954         TDB-TDACUST.
036956     MOVE TDAC-BAR-CD OF TDACUST TO TDB-TDAC-BAR-CD OF            
036958         TDB-TDACUST.
036960     MOVE TDAC-PHONE-1 OF TDACUST TO TDB-TDAC-PHONE-1 OF          
036962         TDB-TDACUST.
036964     MOVE TDAC-PHONE-2 OF TDACUST TO TDB-TDAC-PHONE-2 OF          
036966         TDB-TDACUST.
036968     MOVE TDAC-TIN-CD OF TDACUST TO TDB-TDAC-TIN-CD OF            
036970         TDB-TDACUST.
036972     MOVE TDAC-TIN-CERT-CD OF TDACUST TO TDB-TDAC-TIN-CERT-CD OF  
036974         TDB-TDACUST.
036976     MOVE TDAC-TIN-CERT-DT OF TDACUST TO TDB-TDAC-TIN-CERT-DT OF  
036978         TDB-TDACUST.
036980     MOVE TDAC-TIN-NBR OF TDACUST TO TDB-TDAC-TIN-NBR OF          
036982         TDB-TDACUST.
036984     MOVE TDAC-OFFICER OF TDACUST TO TDB-TDAC-OFFICER OF          
036986         TDB-TDACUST.
036988     MOVE TDAC-EMP-CD OF TDACUST TO TDB-TDAC-EMP-CD OF            
036990         TDB-TDACUST.
036992     MOVE TDAC-FREE-MARK OF TDACUST TO TDB-TDAC-FREE-MARK OF      
036994         TDB-TDACUST.
036996     MOVE TDAC-INQ-SECR-CD OF TDACUST TO TDB-TDAC-INQ-SECR-CD OF  
036998         TDB-TDACUST.
037000     MOVE TDAC-PRIVACY OF TDACUST TO TDB-TDAC-PRIVACY OF          
037002         TDB-TDACUST.
037004     MOVE TDAC-BK-DEF-CD1 OF TDACUST TO TDB-TDAC-BK-DEF-CD1 OF    
037006         TDB-TDACUST.
037008     MOVE TDAC-BK-DEF-CD2 OF TDACUST TO TDB-TDAC-BK-DEF-CD2 OF    
037010         TDB-TDACUST.
037012     MOVE TDAC-BK-DEF-CD3 OF TDACUST TO TDB-TDAC-BK-DEF-CD3 OF    
037014         TDB-TDACUST.
037016     MOVE TDAC-BK-DEF-CD4 OF TDACUST TO TDB-TDAC-BK-DEF-CD4 OF    
037018         TDB-TDACUST.
037020     MOVE TDAC-BK-DEF-CD5 OF TDACUST TO TDB-TDAC-BK-DEF-CD5 OF    
037022         TDB-TDACUST.
037024     MOVE TDAC-EMPLOYEE-ID OF TDACUST TO TDB-TDAC-EMPLOYEE-ID OF  
037026         TDB-TDACUST.
037028     MOVE TDAC-EMAIL-ADDR OF TDACUST TO TDB-TDAC-EMAIL-ADDR OF    
037030         TDB-TDACUST.
037032     MOVE TDAC-EMAIL-PSSWRD OF TDACUST TO TDB-TDAC-EMAIL-PSSWRD   
037034         OF TDB-TDACUST.
037036     MOVE TDAC-GENDER OF TDACUST TO TDB-TDAC-GENDER OF            
037038         TDB-TDACUST.
037040     MOVE TDAC-NEW-CUST OF TDACUST TO TDB-TDAC-NEW-CUST OF        
037042         TDB-TDACUST.
037044     MOVE TDAC-OPEN-DT OF TDACUST TO TDB-TDAC-OPEN-DT OF          
037046         TDB-TDACUST.
037048     MOVE TDAC-LUPD-DATE OF TDACUST TO TDB-TDAC-LUPD-DATE OF      
037050         TDB-TDACUST.
037052     MOVE TDAC-LUPD-TIME OF TDACUST TO TDB-TDAC-LUPD-TIME OF      
037054         TDB-TDACUST.
037056     MOVE TDAC-LST-CONTACT OF TDACUST TO TDB-TDAC-LST-CONTACT OF  
037058         TDB-TDACUST.
037060     MOVE TDAC-BIRTH-DT OF TDACUST TO TDB-TDAC-BIRTH-DT OF        
037062         TDB-TDACUST.
037064     MOVE TDAC-BIRTH-DT-2 OF TDACUST TO TDB-TDAC-BIRTH-DT-2 OF    
037066         TDB-TDACUST.
037068     MOVE TDAC-BIRTH-DT-3 OF TDACUST TO TDB-TDAC-BIRTH-DT-3 OF    
037070         TDB-TDACUST.
037072     MOVE TDAC-DEATH-DT OF TDACUST TO TDB-TDAC-DEATH-DT OF        
037074         TDB-TDACUST.
037076     MOVE TDAC-ADD-DT OF TDACUST TO TDB-TDAC-ADD-DT OF            
037078         TDB-TDACUST.
037080     MOVE TDAC-ADD-TM OF TDACUST TO TDB-TDAC-ADD-TM OF            
037082         TDB-TDACUST.
037084     MOVE TDAC-ROTH-DATE OF TDACUST TO TDB-TDAC-ROTH-DATE OF      
037086         TDB-TDACUST.
037088     MOVE TDAC-CD-BAL OF TDACUST TO TDB-TDAC-CD-BAL OF            
037090         TDB-TDACUST.
037092     MOVE TDAC-CD-BAL-BYR OF TDACUST TO TDB-TDAC-CD-BAL-BYR OF    
037094         TDB-TDACUST.
037096     MOVE TDAC-CD-PENLTY OF TDACUST TO TDB-TDAC-CD-PENLTY OF      
037098         TDB-TDACUST.
037100     MOVE TDAC-CD-WTHLD OF TDACUST TO TDB-TDAC-CD-WTHLD OF        
037102         TDB-TDACUST.
037104     MOVE TDAC-CD-INT OF TDACUST TO TDB-TDAC-CD-INT OF            
037106         TDB-TDACUST.
037108     MOVE TDAC-CD-OID-INT OF TDACUST TO TDB-TDAC-CD-OID-INT OF    
037110         TDB-TDACUST.
037112     MOVE TDAC-IRA-BAL OF TDACUST TO TDB-TDAC-IRA-BAL OF          
037114         TDB-TDACUST.
037116     MOVE TDAC-IRA-BAL-BYR OF TDACUST TO TDB-TDAC-IRA-BAL-BYR OF  
037118         TDB-TDACUST.
037120     MOVE TDAC-IRA-PENLTY OF TDACUST TO TDB-TDAC-IRA-PENLTY OF    
037122         TDB-TDACUST.
037124     MOVE TDAC-IRA-WTHLD OF TDACUST TO TDB-TDAC-IRA-WTHLD OF      
037126         TDB-TDACUST.
037128     MOVE TDAC-IRA-INT OF TDACUST TO TDB-TDAC-IRA-INT OF          
037130         TDB-TDACUST.
037132     MOVE TDAC-IRA-CONTR OF TDACUST TO TDB-TDAC-IRA-CONTR OF      
037134         TDB-TDACUST.
037136     MOVE TDAC-IRA-CONTR-LY OF TDACUST TO TDB-TDAC-IRA-CONTR-LY   
037138         OF TDB-TDACUST.
037140     MOVE TDAC-IRA-DISTR OF TDACUST TO TDB-TDAC-IRA-DISTR OF      
037142         TDB-TDACUST.
037144     MOVE TDAC-IRA-DISTR-LY OF TDACUST TO TDB-TDAC-IRA-DISTR-LY   
037146         OF TDB-TDACUST.
037148     MOVE TDAC-IRA-ROLLOVER OF TDACUST TO TDB-TDAC-IRA-ROLLOVER   
037150         OF TDB-TDACUST.
037152     MOVE TDAC-IRA-TRF-IN OF TDACUST TO TDB-TDAC-IRA-TRF-IN OF    
037154         TDB-TDACUST.
037156     MOVE TDAC-IRA-TRF-OUT OF TDACUST TO TDB-TDAC-IRA-TRF-OUT OF  
037158         TDB-TDACUST.
037160     MOVE TDAC-IRA-FAIR-MKT OF TDACUST TO TDB-TDAC-IRA-FAIR-MKT   
037162         OF TDB-TDACUST.
037164     MOVE TDAC-CIF-REMARK OF TDACUST TO TDB-TDAC-CIF-REMARK OF    
037166         TDB-TDACUST.
037168     MOVE TDAC-CD-ST-WHLD OF TDACUST TO TDB-TDAC-CD-ST-WHLD OF    
037170         TDB-TDACUST.
037172     MOVE TDAC-IRA-ST-WHLD OF TDACUST TO TDB-TDAC-IRA-ST-WHLD OF  
037174         TDB-TDACUST.
037176     MOVE 1 TO Z-II.
037178 Z-5-8-1-LOOP.
037180     IF Z-II > 12
037182         GO TO Z-5-8-1-LOOP-XIT.
037184     MOVE TDAC-CURR-YR-AMT OF TDACUST (Z-II) TO                   
037186         TDB-TDAC-CURR-YR-AMT OF TDB-TDACUST (Z-II).
037188     MOVE TDAC-LAST-YR-AMT OF TDACUST (Z-II) TO                   
037190         TDB-TDAC-LAST-YR-AMT OF TDB-TDACUST (Z-II).
037192     ADD 1 TO Z-II.
037194     GO TO Z-5-8-1-LOOP.
037196 Z-5-8-1-LOOP-XIT.
037198     MOVE TDAC-TIN-CD-2 OF TDACUST TO TDB-TDAC-TIN-CD-2 OF        
037200         TDB-TDACUST.
037202     MOVE TDAC-TIN-CRT-CD-2 OF TDACUST TO TDB-TDAC-TIN-CRT-CD-2   
037204         OF TDB-TDACUST.
037206     MOVE TDAC-TIN-CRT-DT-2 OF TDACUST TO TDB-TDAC-TIN-CRT-DT-2   
037208         OF TDB-TDACUST.
037210     MOVE TDAC-TIN-NBR-2 OF TDACUST TO TDB-TDAC-TIN-NBR-2 OF      
037212         TDB-TDACUST.
037214     MOVE TDAC-TIN-CD-3 OF TDACUST TO TDB-TDAC-TIN-CD-3 OF        
037216         TDB-TDACUST.
037218     MOVE TDAC-TIN-CRT-CD-3 OF TDACUST TO TDB-TDAC-TIN-CRT-CD-3   
037220         OF TDB-TDACUST.
037222     MOVE TDAC-TIN-CRT-DT-3 OF TDACUST TO TDB-TDAC-TIN-CRT-DT-3   
037224         OF TDB-TDACUST.
037226     MOVE TDAC-TIN-NBR-3 OF TDACUST TO TDB-TDAC-TIN-NBR-3 OF      
037228         TDB-TDACUST.
037230     MOVE TDAC-NAICS-CD OF TDACUST TO TDB-TDAC-NAICS-CD OF        
037232         TDB-TDACUST.
037234     MOVE TDAC-CIF-PASS-THR OF TDACUST TO TDB-TDAC-CIF-PASS-THR   
037236         OF TDB-TDACUST.
037238     MOVE TDAC-EMAIL-NTC OF TDACUST TO TDB-TDAC-EMAIL-NTC OF      
037240         TDB-TDACUST.
037242     MOVE TDAC-RMD-YR-AMT OF TDACUST TO TDB-TDAC-RMD-YR-AMT OF    
037244         TDB-TDACUST.
037246     MOVE TDAC-ADDR-CHG-DT OF TDACUST TO TDB-TDAC-ADDR-CHG-DT OF  
037248         TDB-TDACUST.
037250     MOVE TDAC-WTHLD-CD OF TDACUST TO TDB-TDAC-WTHLD-CD OF        
037252         TDB-TDACUST.
037254     MOVE TDAC-ST-WHLD-CD OF TDACUST TO TDB-TDAC-ST-WHLD-CD OF    
037256         TDB-TDACUST.
037258     MOVE TDAC-WTHLD-AMT OF TDACUST TO TDB-TDAC-WTHLD-AMT OF      
037260         TDB-TDACUST.
037262     MOVE TDAC-ST-WHLD-AMT OF TDACUST TO TDB-TDAC-ST-WHLD-AMT OF  
037264         TDB-TDACUST.
037266     MOVE TDAC-FOREIGN-LANG OF TDACUST TO TDB-TDAC-FOREIGN-LANG   
037268         OF TDB-TDACUST.
037270     MOVE TDAC-L-ROLLOVR-DT OF TDACUST TO TDB-TDAC-L-ROLLOVR-DT   
037272         OF TDB-TDACUST.
037274     MOVE TDAC-CUSTM-FIELDS OF TDACUST TO TDB-TDAC-CUSTM-FIELDS   
037276         OF TDB-TDACUST.
037278     MOVE TDAC-LLC-NAME OF TDACUST TO TDB-TDAC-LLC-NAME OF        
037280         TDB-TDACUST.
037282     MOVE TDAC-LLC-TIN-CD OF TDACUST TO TDB-TDAC-LLC-TIN-CD OF    
037284         TDB-TDACUST.
037286     MOVE TDAC-LLC-TIN OF TDACUST TO TDB-TDAC-LLC-TIN OF          
037288         TDB-TDACUST.
037290     MOVE TDAC-FOREIGN-PHN OF TDACUST TO TDB-TDAC-FOREIGN-PHN OF  
037292         TDB-TDACUST.
037294     IF ( TDAC-TIN-NBR NOT = WS-PREV-TIN ) AND ( WS-1ST-TIME = 1 )
037296         NEXT SENTENCE ELSE
037298         GO TO Z-5-9-1-ELSE.
037300************ PERFORM WRITE-CUST-FM-REC
037302     PERFORM Z-26-PROCEDURE THRU Z-26-XIT.
037304     IF  Z-EXIT-EDITEXIT
037306         GO TO Z-5-XIT.
037308     IF  Z-DMS2-ABORT-FLAG = 1
037310         GO TO Z-5-XIT.
037312     IF  Z-EXIT-LEVEL < 0
037314         GO TO Z-5-3-END.
037316*
037318     MOVE SPACES TO WS-TIN-CUST-TABLE.
037320     MOVE 0 TO WS-TIN-CUST-INDEX.
037322 Z-5-9-1-ELSE.
037324     MOVE 0 TO WS-RMDFM2-CUST-IND.
037326     MOVE ZERO TO Z-FLINFO12-PRES.
037328     MOVE ZERO TO Z-FLINFO12-SOME.
037330     MOVE 9 TO Z-FLINFO12-LAST-SEQ.
037332*
037334     SET TDAIRASET OF TDAIRA OF LDBTDADB TO BEGINNING
037336         ON EXCEPTION
037338         MOVE "TDAIRASET OF TDAIRA OF LDBTDADB" TO                
037340             Z-DMS-EXCEPT-STR
037342         MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
037344         MOVE 9 TO Z-DMS-EXCEPT-SEQ
037346         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT
037348         GO TO Z-5-14-XIT.
037350 Z-5-14-LOOP.
037352     MOVE ZERO TO Z-FLINFO12-PRES.
037354 Z-5-14-READ.
037356     FIND TDAIRA OF LDBTDADB VIA NEXT TDAIRASET OF TDAIRA OF      
037358         LDBTDADB
037360     AT TDAI-BANK = WS-BANK-NO AND
037362        TDAI-CUST = TDB-TDAC-CUST
037364         ON EXCEPTION
037366         MOVE 9 TO Z-DMS-EXCEPT-SEQ
037368         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
037370             GO TO Z-5-14-XIT
037372         ELSE
037374             MOVE "TDAIRASET OF TDAIRA OF LDBTDADB" TO            
037376                 Z-DMS-EXCEPT-STR
037378             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
037380             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
037382
037384*
037386     MOVE 1 TO Z-FLINFO12-PRES.
037388     MOVE 1 TO Z-FLINFO12-SOME.
037390     MOVE 0 TO Z-EXIT-CODE.
037392     MOVE 9999 TO Z-EXIT-LEVEL.
037394     IF Z-FLINFO12-ABSENT
037396         NEXT SENTENCE ELSE
037398         GO TO Z-5-15-1-ELSE.
037400     MOVE 2 TO Z-EXIT-LEVEL
037402     GO TO Z-5-14-END.
037404 Z-5-15-1-ELSE.
037406     MOVE TDAI-BANK OF TDAIRA TO TDB-TDAI-BANK OF TDB-TDAIRA.
037408     MOVE TDAI-BRCH OF TDAIRA TO TDB-TDAI-BRCH OF TDB-TDAIRA.
037410     MOVE TDAI-CUST OF TDAIRA TO TDB-TDAI-CUST OF TDB-TDAIRA.
037412     MOVE TDAI-ACCT OF TDAIRA TO TDB-TDAI-ACCT OF TDB-TDAIRA.
037414     MOVE TDAI-PUB-ID OF TDAIRA TO TDB-TDAI-PUB-ID OF TDB-TDAIRA.
037416     MOVE TDAI-ADD-DT OF TDAIRA TO TDB-TDAI-ADD-DT OF TDB-TDAIRA.
037418     MOVE TDAI-ADD-TM OF TDAIRA TO TDB-TDAI-ADD-TM OF TDB-TDAIRA.
037420     MOVE 1 TO Z-II.
037422 Z-5-17-1-LOOP.
037424     IF Z-II > 20
037426         GO TO Z-5-17-1-LOOP-XIT.
037428     MOVE TDAI-DS-TYPE OF TDAIRA (Z-II) TO TDB-TDAI-DS-TYPE OF    
037430         TDB-TDAIRA (Z-II).
037432     MOVE TDAI-CN-TYPE OF TDAIRA (Z-II) TO TDB-TDAI-CN-TYPE OF    
037434         TDB-TDAIRA (Z-II).
037436     MOVE TDAI-DS-CN-AMT OF TDAIRA (Z-II) TO TDB-TDAI-DS-CN-AMT   
037438         OF TDB-TDAIRA (Z-II).
037440     MOVE TDAI-DS-PEN-AMT OF TDAIRA (Z-II) TO TDB-TDAI-DS-PEN-AMT 
037442         OF TDB-TDAIRA (Z-II).
037444     MOVE TDAI-DS-WTHLD-AMT OF TDAIRA (Z-II) TO                   
037446         TDB-TDAI-DS-WTHLD-AMT OF TDB-TDAIRA (Z-II).
037448     MOVE TDAI-DS-ST-WH-AMT OF TDAIRA (Z-II) TO                   
037450         TDB-TDAI-DS-ST-WH-AMT OF TDB-TDAIRA (Z-II).
037452     MOVE TDAI-DS-EXC-EARN OF TDAIRA (Z-II) TO                    
037454         TDB-TDAI-DS-EXC-EARN OF TDB-TDAIRA (Z-II).
037456     ADD 1 TO Z-II.
037458     GO TO Z-5-17-1-LOOP.
037460 Z-5-17-1-LOOP-XIT.
037462     MOVE TDAI-DS-C-YTD-CNT OF TDAIRA TO TDB-TDAI-DS-C-YTD-CNT OF 
037464         TDB-TDAIRA.
037466     MOVE TDAI-DS-P-YTD-CNT OF TDAIRA TO TDB-TDAI-DS-P-YTD-CNT OF 
037468         TDB-TDAIRA.
037470     MOVE TDAI-DS-AMT-C-YTD OF TDAIRA TO TDB-TDAI-DS-AMT-C-YTD OF 
037472         TDB-TDAIRA.
037474     MOVE TDAI-DS-AMT-P-YTD OF TDAIRA TO TDB-TDAI-DS-AMT-P-YTD OF 
037476         TDB-TDAIRA.
037478     MOVE TDAI-DS-INT-AMT OF TDAIRA TO TDB-TDAI-DS-INT-AMT OF     
037480         TDB-TDAIRA.
037482     MOVE TDAI-CN-YTD-CNT OF TDAIRA TO TDB-TDAI-CN-YTD-CNT OF     
037484         TDB-TDAIRA.
037486     MOVE TDAI-CN-YTD-AMT OF TDAIRA TO TDB-TDAI-CN-YTD-AMT OF     
037488         TDB-TDAIRA.
037490     MOVE TDAI-CN-LYTD-AMT OF TDAIRA TO TDB-TDAI-CN-LYTD-AMT OF   
037492         TDB-TDAIRA.
037494     MOVE TDAI-EMP-CONT-LYR OF TDAIRA TO TDB-TDAI-EMP-CONT-LYR OF 
037496         TDB-TDAIRA.
037498     MOVE TDAI-REG-CONT-LYR OF TDAIRA TO TDB-TDAI-REG-CONT-LYR OF 
037500         TDB-TDAIRA.
037502     MOVE TDAI-UNINSURED OF TDAIRA TO TDB-TDAI-UNINSURED OF       
037504         TDB-TDAIRA.
037506     MOVE TDAI-ROLLOVER OF TDAIRA TO TDB-TDAI-ROLLOVER OF         
037508         TDB-TDAIRA.
037510     MOVE TDAI-ROLLOVER-LYR OF TDAIRA TO TDB-TDAI-ROLLOVER-LYR OF 
037512         TDB-TDAIRA.
037514     MOVE TDAI-TRANSFER-IN OF TDAIRA TO TDB-TDAI-TRANSFER-IN OF   
037516         TDB-TDAIRA.
037518     MOVE TDAI-TRANSFER-OUT OF TDAIRA TO TDB-TDAI-TRANSFER-OUT OF 
037520         TDB-TDAIRA.
037522     MOVE TDAI-1ST-CN-DATE OF TDAIRA TO TDB-TDAI-1ST-CN-DATE OF   
037524         TDB-TDAIRA.
037526     MOVE TDAI-BASIS-C-LTD OF TDAIRA TO TDB-TDAI-BASIS-C-LTD OF   
037528         TDB-TDAIRA.
037530     MOVE TDAI-BASIS-D-LTD OF TDAIRA TO TDB-TDAI-BASIS-D-LTD OF   
037532         TDB-TDAIRA.
037534     MOVE TDAI-BASIS-D-YTD OF TDAIRA TO TDB-TDAI-BASIS-D-YTD OF   
037536         TDB-TDAIRA.
037538     MOVE ZERO TO Z-FLINFO8-PRES.
037540     MOVE 10 TO Z-FLINFO8-LAST-SEQ.
037542     MOVE ZERO TO Z-FLINFO8-SOME.
037544 Z-5-18-READ.
037546     FIND TDAACCT OF LDBTDADB VIA FIRST TDAAMSET OF TDAACCT OF    
037548         LDBTDADB
037550     AT TDAA-BANK = WS-BANK-NO AND
037552        TDAA-CUST = TDB-TDAI-CUST AND
037554        TDAA-ACCT = TDB-TDAI-ACCT
037556         ON EXCEPTION
037558         MOVE 10 TO Z-DMS-EXCEPT-SEQ
037560         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
037562             GO TO Z-5-18-XIT
037564         ELSE
037566             MOVE "TDAAMSET OF TDAACCT OF LDBTDADB" TO            
037568                 Z-DMS-EXCEPT-STR
037570             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
037572             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
037574
037576 Z-5-18-PRESENT.
037578*
037580     MOVE 1 TO Z-FLINFO8-SOME.
037582     MOVE 1 TO Z-FLINFO8-PRES.
037584     GO TO Z-5-18-CONT.
037586 Z-5-18-XIT.
037588 Z-5-18-CONT.
037590     IF Z-FLINFO8-ABSENT
037592         NEXT SENTENCE ELSE
037594         GO TO Z-5-19-1-ELSE.
037596     MOVE 2 TO Z-EXIT-LEVEL
037598     GO TO Z-5-14-END.
037600 Z-5-19-1-ELSE.
037602     MOVE TDAA-BANK OF TDAACCT TO TDB-TDAA-BANK OF TDB-TDAACCT.
037604     MOVE TDAA-BRCH OF TDAACCT TO TDB-TDAA-BRCH OF TDB-TDAACCT.
037606     MOVE TDAA-APPL OF TDAACCT TO TDB-TDAA-APPL OF TDB-TDAACCT.
037608     MOVE TDAA-CUST OF TDAACCT TO TDB-TDAA-CUST OF TDB-TDAACCT.
037610     MOVE TDAA-ACCT OF TDAACCT TO TDB-TDAA-ACCT OF TDB-TDAACCT.
037612     MOVE TDAA-STATUS OF TDAACCT TO TDB-TDAA-STATUS OF            
037614         TDB-TDAACCT.
037616     MOVE TDAA-IRA-TYPE OF TDAACCT TO TDB-TDAA-IRA-TYPE OF        
037618         TDB-TDAACCT.
037620     MOVE TDAA-ACCT-OPTION OF TDAACCT TO TDB-TDAA-ACCT-OPTION OF  
037622         TDB-TDAACCT.
037624     MOVE TDAA-DT-CONDENSED OF TDAACCT TO TDB-TDAA-DT-CONDENSED   
037626         OF TDB-TDAACCT.
037628     MOVE TDAA-CERT OF TDAACCT TO TDB-TDAA-CERT OF TDB-TDAACCT.
037630     MOVE TDAA-SHT-NAME OF TDAACCT TO TDB-TDAA-SHT-NAME OF        
037632         TDB-TDAACCT.
037634     MOVE TDAA-TITLE OF TDAACCT TO TDB-TDAA-TITLE OF TDB-TDAACCT.
037636     MOVE TDAA-TITLE-PRINT OF TDAACCT TO TDB-TDAA-TITLE-PRINT OF  
037638         TDB-TDAACCT.
037640     MOVE TDAA-ADDR-USAGE OF TDAACCT TO TDB-TDAA-ADDR-USAGE OF    
037642         TDB-TDAACCT.
037644     MOVE TDAA-ADDR-ALT OF TDAACCT TO TDB-TDAA-ADDR-ALT OF        
037646         TDB-TDAACCT.
037648     MOVE TDAA-ADDR-TEMP OF TDAACCT TO TDB-TDAA-ADDR-TEMP OF      
037650         TDB-TDAACCT.
037652     MOVE TDAA-TEMP-BEG-DT OF TDAACCT TO TDB-TDAA-TEMP-BEG-DT OF  
037654         TDB-TDAACCT.
037656     MOVE TDAA-TEMP-END-DT OF TDAACCT TO TDB-TDAA-TEMP-END-DT OF  
037658         TDB-TDAACCT.
037660     MOVE TDAA-TEMP-EFF-DT OF TDAACCT TO TDB-TDAA-TEMP-EFF-DT OF  
```

⚠️  This is the source code you must document.
    450 lines from 18377 to 18826.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

