# LLM Request Debug File
Generated: 2025-11-18T16:47:26.175651

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 9/55
- **Model**: gpt-4.1
- **Chunk Number**: 9
- **Pass Number**: 3
- **Attempt Number**: 4 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,085 tokens
- **User Prompt**: ~17,225 tokens
- **Total Input**: ~19,310 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 9/55" (ID: detailed-code-explanation)

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


**CHUNK 9 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T16:24:14.514603", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 9 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 3212 to 4028 (817 lines)\nChunk Tokens (estimated): ~14,869\nActual Input Tokens: 16,275 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 3212-4028 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 9 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 9 of 55.\n\n\n=============================================================================\nCHUNK 9 SOURCE CODE (Lines 3212-4028)\n=============================================================================\n\n```cobol\n006432 01  RMD-LEF-TABLE-2-X.                                           \n006434   05  RMD-LEF-TABLE-2.                                           \n006436     10 FILLER PIC X(54) VALUE                                    \n006438         \"552547543538534000000000000000000000000000000000000000\".\n006440     10 FILLER PIC X(54) VALUE                                    \n006442         \"000000000000000000000000000000000000000000000000000000\".\n006444     10 FILLER PIC X(54) VALUE                                    \n006446         \"000000000000000000000000000000000000000000000000000000\".\n006448     10 FILLER PIC X(54) VALUE                                    \n006450         \"000000000000000000000000000000000000000000000000000000\".\n006452     10 FILLER PIC X(27) VALUE                                    \n006454         \"000000000000000000000000000\".                           \n006456     10 FILLER PIC X(54) VALUE                                    \n006458         \"547542537533528000000000000000000000000000000000000000\".\n006460     10 FILLER PIC X(54) VALUE                                    \n006462         \"000000000000000000000000000000000000000000000000000000\".\n006464     10 FILLER PIC X(54) VALUE                                    \n006466         \"000000000000000000000000000000000000000000000000000000\".\n006468     10 FILLER PIC X(54) VALUE                                    \n006470         \"000000000000000000000000000000000000000000000000000000\".\n006472     10 FILLER PIC X(27) VALUE                                    \n006474         \"000000000000000000000000000\".                           \n006476     10 FILLER PIC X(54) VALUE                                    \n006478         \"543537532527523000000000000000000000000000000000000000\".\n006480     10 FILLER PIC X(54) VALUE                                    \n006482         \"000000000000000000000000000000000000000000000000000000\".\n006484     10 FILLER PIC X(54) VALUE                                    \n006486         \"000000000000000000000000000000000000000000000000000000\".\n006488     10 FILLER PIC X(54) VALUE                                    \n006490         \"000000000000000000000000000000000000000000000000000000\".\n006492     10 FILLER PIC X(27) VALUE                                    \n006494         \"000000000000000000000000000\".                           \n006496     10 FILLER PIC X(54) VALUE                                    \n006498         \"538533527522517000000000000000000000000000000000000000\".\n006500     10 FILLER PIC X(54) VALUE                                    \n006502         \"000000000000000000000000000000000000000000000000000000\".\n006504     10 FILLER PIC X(54) VALUE                                    \n006506         \"000000000000000000000000000000000000000000000000000000\".\n006508     10 FILLER PIC X(54) VALUE                                    \n006510         \"000000000000000000000000000000000000000000000000000000\".\n006512     10 FILLER PIC X(27) VALUE                                    \n006514         \"000000000000000000000000000\".                           \n006516     10 FILLER PIC X(54) VALUE                                    \n006518         \"534528523517512000000000000000000000000000000000000000\".\n006520     10 FILLER PIC X(54) VALUE                                    \n006522         \"000000000000000000000000000000000000000000000000000000\".\n006524     10 FILLER PIC X(54) VALUE                                    \n006526         \"000000000000000000000000000000000000000000000000000000\".\n006528     10 FILLER PIC X(54) VALUE                                    \n006530         \"000000000000000000000000000000000000000000000000000000\".\n006532     10 FILLER PIC X(27) VALUE                                    \n006534         \"000000000000000000000000000\".                           \n006536     10 FILLER PIC X(54) VALUE                                    \n006538         \"530524518513508502498493489485481477474471468000000000\".\n006540     10 FILLER PIC X(54) VALUE                                    \n006542         \"000000000000000000000000000000000000000000000000000000\".\n006544     10 FILLER PIC X(54) VALUE                                    \n006546         \"000000000000000000000000000000000000000000000000000000\".\n006548     10 FILLER PIC X(54) VALUE                                    \n006550         \"000000000000000000000000000000000000000000000000000000\".\n006552     10 FILLER PIC X(27) VALUE                                    \n006554         \"000000000000000000000000000\".                           \n006556     10 FILLER PIC X(54) VALUE                                    \n006558         \"527520514509503498493488483479475471467464461000000000\".\n006560     10 FILLER PIC X(54) VALUE                                    \n006562         \"000000000000000000000000000000000000000000000000000000\".\n006564     10 FILLER PIC X(54) VALUE                                    \n006566         \"000000000000000000000000000000000000000000000000000000\".\n006568     10 FILLER PIC X(54) VALUE                                    \n006570         \"000000000000000000000000000000000000000000000000000000\".\n006572     10 FILLER PIC X(27) VALUE                                    \n006574         \"000000000000000000000000000\".                           \n006576     10 FILLER PIC X(54) VALUE                                    \n006578         \"523517511504499493488483478473469465461458454000000000\".\n006580     10 FILLER PIC X(54) VALUE                                    \n006582         \"000000000000000000000000000000000000000000000000000000\".\n006584     10 FILLER PIC X(54) VALUE                                    \n006586         \"000000000000000000000000000000000000000000000000000000\".\n006588     10 FILLER PIC X(54) VALUE                                    \n006590         \"000000000000000000000000000000000000000000000000000000\".\n006592     10 FILLER PIC X(27) VALUE                                    \n006594         \"000000000000000000000000000\".                           \n006596     10 FILLER PIC X(54) VALUE                                    \n006598         \"520513507501495489483478473468463459455451448000000000\".\n006600     10 FILLER PIC X(54) VALUE                                    \n006602         \"000000000000000000000000000000000000000000000000000000\".\n006604     10 FILLER PIC X(54) VALUE                                    \n006606         \"000000000000000000000000000000000000000000000000000000\".\n006608     10 FILLER PIC X(54) VALUE                                    \n006610         \"000000000000000000000000000000000000000000000000000000\".\n006612     10 FILLER PIC X(27) VALUE                                    \n006614         \"000000000000000000000000000\".                           \n006616     10 FILLER PIC X(54) VALUE                                    \n006618         \"517510504497491485479473468463458454449445442000000000\".\n006620     10 FILLER PIC X(54) VALUE                                    \n006622         \"000000000000000000000000000000000000000000000000000000\".\n006624     10 FILLER PIC X(54) VALUE                                    \n006626         \"000000000000000000000000000000000000000000000000000000\".\n006628     10 FILLER PIC X(54) VALUE                                    \n006630         \"000000000000000000000000000000000000000000000000000000\".\n006632     10 FILLER PIC X(27) VALUE                                    \n006634         \"000000000000000000000000000\".                           \n006636     10 FILLER PIC X(54) VALUE                                    \n006638         \"515507500494487481475469463458453448444440436000000000\".\n006640     10 FILLER PIC X(54) VALUE                                    \n006642         \"000000000000000000000000000000000000000000000000000000\".\n006644     10 FILLER PIC X(54) VALUE                                    \n006646         \"000000000000000000000000000000000000000000000000000000\".\n006648     10 FILLER PIC X(54) VALUE                                    \n006650         \"000000000000000000000000000000000000000000000000000000\".\n006652     10 FILLER PIC X(27) VALUE                                    \n006654         \"000000000000000000000000000\".                           \n006656     10 FILLER PIC X(54) VALUE                                    \n006658         \"512505498491484477471465459454448443439434430000000000\".\n006660     10 FILLER PIC X(54) VALUE                                    \n006662         \"000000000000000000000000000000000000000000000000000000\".\n006664     10 FILLER PIC X(54) VALUE                                    \n006666         \"000000000000000000000000000000000000000000000000000000\".\n006668     10 FILLER PIC X(54) VALUE                                    \n006670         \"000000000000000000000000000000000000000000000000000000\".\n006672     10 FILLER PIC X(27) VALUE                                    \n006674         \"000000000000000000000000000\".                           \n006676     10 FILLER PIC X(54) VALUE                                    \n006678         \"510502495488481474467461455449444439434429424000000000\".\n006680     10 FILLER PIC X(54) VALUE                                    \n006682         \"000000000000000000000000000000000000000000000000000000\".\n006684     10 FILLER PIC X(54) VALUE                                    \n006686         \"000000000000000000000000000000000000000000000000000000\".\n006688     10 FILLER PIC X(54) VALUE                                    \n006690         \"000000000000000000000000000000000000000000000000000000\".\n006692     10 FILLER PIC X(27) VALUE                                    \n006694         \"000000000000000000000000000\".                           \n006696     10 FILLER PIC X(54) VALUE                                    \n006698         \"508500492485478471464458451445440434429424419000000000\".\n006700     10 FILLER PIC X(54) VALUE                                    \n006702         \"000000000000000000000000000000000000000000000000000000\".\n006704     10 FILLER PIC X(54) VALUE                                    \n006706         \"000000000000000000000000000000000000000000000000000000\".\n006708     10 FILLER PIC X(54) VALUE                                    \n006710         \"000000000000000000000000000000000000000000000000000000\".\n006712     10 FILLER PIC X(27) VALUE                                    \n006714         \"000000000000000000000000000\".                           \n006716     10 FILLER PIC X(54) VALUE                                    \n006718         \"506498490482475468461454448442436430424419414000000000\".\n006720     10 FILLER PIC X(54) VALUE                                    \n006722         \"000000000000000000000000000000000000000000000000000000\".\n006724     10 FILLER PIC X(54) VALUE                                    \n006726         \"000000000000000000000000000000000000000000000000000000\".\n006728     10 FILLER PIC X(54) VALUE                                    \n006730         \"000000000000000000000000000000000000000000000000000000\".\n006732     10 FILLER PIC X(27) VALUE                                    \n006734         \"000000000000000000000000000\".                           \n006736     10 FILLER PIC X(54) VALUE                                    \n006738         \"504496488480473465458451444438432426420415409404400395\".\n006740     10 FILLER PIC X(54) VALUE                                    \n006742         \"391387383380376373371000000000000000000000000000000000\".\n006744     10 FILLER PIC X(54) VALUE                                    \n006746         \"000000000000000000000000000000000000000000000000000000\".\n006748     10 FILLER PIC X(54) VALUE                                    \n006750         \"000000000000000000000000000000000000000000000000000000\".\n006752     10 FILLER PIC X(27) VALUE                                    \n006754         \"000000000000000000000000000\".                           \n006756     10 FILLER PIC X(54) VALUE                                    \n006758         \"502494486478470463455448441435428422416410405400395390\".\n006760     10 FILLER PIC X(54) VALUE                                    \n006762         \"385381377374370367364000000000000000000000000000000000\".\n006764     10 FILLER PIC X(54) VALUE                                    \n006766         \"000000000000000000000000000000000000000000000000000000\".\n006768     10 FILLER PIC X(54) VALUE                                    \n006770         \"000000000000000000000000000000000000000000000000000000\".\n006772     10 FILLER PIC X(27) VALUE                                    \n006774         \"000000000000000000000000000\".                           \n006776     10 FILLER PIC X(54) VALUE                                    \n006778         \"500492484476468460453446438432425418412406401395390385\".\n006780     10 FILLER PIC X(54) VALUE                                    \n006782         \"380376372368364360357000000000000000000000000000000000\".\n006784     10 FILLER PIC X(54) VALUE                                    \n006786         \"000000000000000000000000000000000000000000000000000000\".\n006788     10 FILLER PIC X(54) VALUE                                    \n006790         \"000000000000000000000000000000000000000000000000000000\".\n006792     10 FILLER PIC X(27) VALUE                                    \n006794         \"000000000000000000000000000\".                           \n006796     10 FILLER PIC X(54) VALUE                                    \n006798         \"499491482474466458451443436429422415409403397391385380\".\n006800     10 FILLER PIC X(54) VALUE                                    \n006802         \"375371366362358354351000000000000000000000000000000000\".\n006804     10 FILLER PIC X(54) VALUE                                    \n006806         \"000000000000000000000000000000000000000000000000000000\".\n006808     10 FILLER PIC X(54) VALUE                                    \n006810         \"000000000000000000000000000000000000000000000000000000\".\n006812     10 FILLER PIC X(27) VALUE                                    \n006814         \"000000000000000000000000000\".                           \n006816     10 FILLER PIC X(54) VALUE                                    \n006818         \"498489481472464456448441433426419412405399393387381376\".\n006820     10 FILLER PIC X(54) VALUE                                    \n006822         \"371366361357352348345000000000000000000000000000000000\".\n006824     10 FILLER PIC X(54) VALUE                                    \n006826         \"000000000000000000000000000000000000000000000000000000\".\n006828     10 FILLER PIC X(54) VALUE                                    \n006830         \"000000000000000000000000000000000000000000000000000000\".\n006832     10 FILLER PIC X(27) VALUE                                    \n006834         \"000000000000000000000000000\".                           \n006836     10 FILLER PIC X(54) VALUE                                    \n006838         \"497488479471463455447439431424416409402396389383377372\".\n006840     10 FILLER PIC X(54) VALUE                                    \n006842         \"366361356351347343339000000000000000000000000000000000\".\n006844     10 FILLER PIC X(54) VALUE                                    \n006846         \"000000000000000000000000000000000000000000000000000000\".\n006848     10 FILLER PIC X(54) VALUE                                    \n006850         \"000000000000000000000000000000000000000000000000000000\".\n006852     10 FILLER PIC X(27) VALUE                                    \n006854         \"000000000000000000000000000\".                           \n006856     10 FILLER PIC X(54) VALUE                                    \n006858         \"495487478470461453445437429421414407400393386380374368\".\n006860     10 FILLER PIC X(54) VALUE                                    \n006862         \"362357351347342337333000000000000000000000000000000000\".\n006864     10 FILLER PIC X(54) VALUE                                    \n006866         \"000000000000000000000000000000000000000000000000000000\".\n006868     10 FILLER PIC X(54) VALUE                                    \n006870         \"000000000000000000000000000000000000000000000000000000\".\n006872     10 FILLER PIC X(27) VALUE                                    \n006874         \"000000000000000000000000000\".                           \n006876     10 FILLER PIC X(54) VALUE                                    \n006878         \"494486477468460451443435427419412404397390383376370364\".\n006880     10 FILLER PIC X(54) VALUE                                    \n006882         \"358352347342337332328000000000000000000000000000000000\".\n006884     10 FILLER PIC X(54) VALUE                                    \n006886         \"000000000000000000000000000000000000000000000000000000\".\n006888     10 FILLER PIC X(54) VALUE                                    \n006890         \"000000000000000000000000000000000000000000000000000000\".\n006892     10 FILLER PIC X(27) VALUE                                    \n006894         \"000000000000000000000000000\".                           \n006896     10 FILLER PIC X(54) VALUE                                    \n006898         \"494485476467458450442433425417409402394387380373367360\".\n006900     10 FILLER PIC X(54) VALUE                                    \n006902         \"354348343337332328323000000000000000000000000000000000\".\n006904     10 FILLER PIC X(54) VALUE                                    \n006906         \"000000000000000000000000000000000000000000000000000000\".\n006908     10 FILLER PIC X(54) VALUE                                    \n006910         \"000000000000000000000000000000000000000000000000000000\".\n006912     10 FILLER PIC X(27) VALUE                                    \n006914         \"000000000000000000000000000\".                           \n006916     10 FILLER PIC X(54) VALUE                                    \n006918         \"493484475466457449440432424415407400392385378371364357\".\n006920     10 FILLER PIC X(54) VALUE                                    \n006922         \"351345339333328323318000000000000000000000000000000000\".\n006924     10 FILLER PIC X(54) VALUE                                    \n006926         \"000000000000000000000000000000000000000000000000000000\".\n006928     10 FILLER PIC X(54) VALUE                                    \n006930         \"000000000000000000000000000000000000000000000000000000\".\n006932     10 FILLER PIC X(27) VALUE                                    \n006934         \"000000000000000000000000000\".                           \n006936     10 FILLER PIC X(54) VALUE                                    \n006938         \"492483474465456447439430422414406398390382375368361354\".\n006940     10 FILLER PIC X(54) VALUE                                    \n006942         \"348341335329324319313309304300296292288285282279276000\".\n006944     10 FILLER PIC X(54) VALUE                                    \n006946         \"000000000000000000000000000000000000000000000000000000\".\n006948     10 FILLER PIC X(54) VALUE                                    \n006950         \"000000000000000000000000000000000000000000000000000000\".\n006952     10 FILLER PIC X(27) VALUE                                    \n006954         \"000000000000000000000000000\".                           \n006956     10 FILLER PIC X(54) VALUE                                    \n006958         \"491482473464455446438429421412404396388380373366358351\".\n006960     10 FILLER PIC X(54) VALUE                                    \n006962         \"345338332326320314309304299295290286283279276273270000\".\n006964     10 FILLER PIC X(54) VALUE                                    \n006966         \"000000000000000000000000000000000000000000000000000000\".\n006968     10 FILLER PIC X(54) VALUE                                    \n006970         \"000000000000000000000000000000000000000000000000000000\".\n006972     10 FILLER PIC X(27) VALUE                                    \n006974         \"000000000000000000000000000\".                           \n006976     10 FILLER PIC X(54) VALUE                                    \n006978         \"491481472463454445437428419411403394386378371363356349\".\n006980     10 FILLER PIC X(54) VALUE                                    \n006982         \"342335329322316311305300295290285281277273270267264000\".\n006984     10 FILLER PIC X(54) VALUE                                    \n006986         \"000000000000000000000000000000000000000000000000000000\".\n006988     10 FILLER PIC X(54) VALUE                                    \n006990         \"000000000000000000000000000000000000000000000000000000\".\n006992     10 FILLER PIC X(27) VALUE                                    \n006994         \"000000000000000000000000000\".                           \n006996     10 FILLER PIC X(54) VALUE                                    \n006998         \"490481472463453445436427418410401393385377369361354346\".\n007000     10 FILLER PIC X(54) VALUE                                    \n007002         \"339332326319313307301296290285281276272268264261257000\".\n007004     10 FILLER PIC X(54) VALUE                                    \n007006         \"000000000000000000000000000000000000000000000000000000\".\n007008     10 FILLER PIC X(54) VALUE                                    \n007010         \"000000000000000000000000000000000000000000000000000000\".\n007012     10 FILLER PIC X(27) VALUE                                    \n007014         \"000000000000000000000000000\".                           \n007016     10 FILLER PIC X(54) VALUE                                    \n007018         \"489480471462453444435426417408400392383375367359352344\".\n007020     10 FILLER PIC X(54) VALUE                                    \n007022         \"337330323316310304298292286281276271267263259255252000\".\n007024     10 FILLER PIC X(54) VALUE                                    \n007026         \"000000000000000000000000000000000000000000000000000000\".\n007028     10 FILLER PIC X(54) VALUE                                    \n007030         \"000000000000000000000000000000000000000000000000000000\".\n007032     10 FILLER PIC X(27) VALUE                                    \n007034         \"000000000000000000000000000\".                           \n007036     10 FILLER PIC X(54) VALUE                                    \n007038         \"489480470461452443434425416407399390382374366358350342\".\n007040     10 FILLER PIC X(54) VALUE                                    \n007042         \"335327320314307300294288283277272267262258254250246000\".\n007044     10 FILLER PIC X(54) VALUE                                    \n007046         \"000000000000000000000000000000000000000000000000000000\".\n007048     10 FILLER PIC X(54) VALUE                                    \n007050         \"000000000000000000000000000000000000000000000000000000\".\n007052     10 FILLER PIC X(27) VALUE                                    \n007054         \"000000000000000000000000000\".                           \n007056     10 FILLER PIC X(54) VALUE                                    \n007058         \"489479470461451442433424415406398389381372364356348340\".\n007060     10 FILLER PIC X(54) VALUE                                    \n007062         \"333325318311304298291285279273268263258253249245241000\".\n007064     10 FILLER PIC X(54) VALUE                                    \n007066         \"000000000000000000000000000000000000000000000000000000\".\n007068     10 FILLER PIC X(54) VALUE                                    \n007070         \"000000000000000000000000000000000000000000000000000000\".\n007072     10 FILLER PIC X(27) VALUE                                    \n007074         \"000000000000000000000000000\".                           \n007076     10 FILLER PIC X(54) VALUE                                    \n007078         \"488479469460451442433423414406397388380371363355347339\".\n007080     10 FILLER PIC X(54) VALUE                                    \n007082         \"331323316309302295288282276270264259254249244240236000\".\n007084     10 FILLER PIC X(54) VALUE                                    \n007086         \"000000000000000000000000000000000000000000000000000000\".\n007088     10 FILLER PIC X(54) VALUE                                    \n007090         \"000000000000000000000000000000000000000000000000000000\".\n007092     10 FILLER PIC X(27) VALUE                                    \n007094         \"000000000000000000000000000\".                           \n007096     10 FILLER PIC X(54) VALUE                                    \n007098         \"488478469460450441432423414405396387379370362353345337\".\n007100     10 FILLER PIC X(54) VALUE                                    \n007102         \"329321314307299292286279273267261255250245240235231000\".\n007104     10 FILLER PIC X(54) VALUE                                    \n007106         \"000000000000000000000000000000000000000000000000000000\".\n007108     10 FILLER PIC X(54) VALUE                                    \n007110         \"000000000000000000000000000000000000000000000000000000\".\n007112     10 FILLER PIC X(27) VALUE                                    \n007114         \"000000000000000000000000000\".                           \n007116     10 FILLER PIC X(54) VALUE                                    \n007118         \"487478469459450441431422413404395386378369360352344336\".\n007120     10 FILLER PIC X(54) VALUE                                    \n007122         \"328320312305297290283276270264257252246241236231226000\".\n007124     10 FILLER PIC X(54) VALUE                                    \n007126         \"000000000000000000000000000000000000000000000000000000\".\n007128     10 FILLER PIC X(54) VALUE                                    \n007130         \"000000000000000000000000000000000000000000000000000000\".\n007132     10 FILLER PIC X(27) VALUE                                    \n007134         \"000000000000000000000000000\".                           \n007136     10 FILLER PIC X(54) VALUE                                    \n007138         \"487478468459449440431422413403394386377368359351343334\".\n007140     10 FILLER PIC X(54) VALUE                                    \n007142         \"326318311303295288281274267261254248243237232227222218\".\n007144     10 FILLER PIC X(54) VALUE                                    \n007146         \"213209206202199196194191189000000000000000000000000000\".\n007148     10 FILLER PIC X(54) VALUE                                    \n007150         \"000000000000000000000000000000000000000000000000000000\".\n007152     10 FILLER PIC X(27) VALUE                                    \n007154         \"000000000000000000000000000\".                           \n007156     10 FILLER PIC X(54) VALUE                                    \n007158         \"487477468459449440430421412403394385376367359350342333\".\n007160     10 FILLER PIC X(54) VALUE                                    \n007162         \"325317309301294286279272265258252245239234228223218213\".\n007164     10 FILLER PIC X(54) VALUE                                    \n007166         \"209205201197194191188185183000000000000000000000000000\".\n007168     10 FILLER PIC X(54) VALUE                                    \n007170         \"000000000000000000000000000000000000000000000000000000\".\n007172     10 FILLER PIC X(27) VALUE                                    \n007174         \"000000000000000000000000000\".                           \n007176     10 FILLER PIC X(54) VALUE                                    \n007178         \"487477468458449439430421411402393384375366358349341332\".\n007180     10 FILLER PIC X(54) VALUE                                    \n007182         \"324316308300292284277270263256249243237231225220214209\".\n007184     10 FILLER PIC X(54) VALUE                                    \n007186         \"205200196193189186183180177000000000000000000000000000\".\n007188     10 FILLER PIC X(54) VALUE                                    \n007190         \"000000000000000000000000000000000000000000000000000000\".\n007192     10 FILLER PIC X(27) VALUE                                    \n007194         \"000000000000000000000000000\".                           \n007196     10 FILLER PIC X(54) VALUE                                    \n007198         \"486477467458448439430420411402393384375366357348340331\".\n007200     10 FILLER PIC X(54) VALUE                                    \n007202         \"323315306298291283275268261254247240234228222216211206\".\n007204     10 FILLER PIC X(54) VALUE                                    \n007206         \"201196192188184181178175172000000000000000000000000000\".\n007208     10 FILLER PIC X(54) VALUE                                    \n007210         \"000000000000000000000000000000000000000000000000000000\".\n007212     10 FILLER PIC X(27) VALUE                                    \n007214         \"000000000000000000000000000\".                           \n007216     10 FILLER PIC X(54) VALUE                                    \n007218         \"486477467458448439429420411401392383374365356348339330\".\n007220     10 FILLER PIC X(54) VALUE                                    \n007222         \"322314305297289281274266259252245238231225219213208202\".\n007224     10 FILLER PIC X(54) VALUE                                    \n007226         \"197193188184180176173170167000000000000000000000000000\".\n007228     10 FILLER PIC X(54) VALUE                                    \n007230         \"000000000000000000000000000000000000000000000000000000\".\n007232     10 FILLER PIC X(27) VALUE                                    \n007234         \"000000000000000000000000000\".                           \n007236     10 FILLER PIC X(54) VALUE                                    \n007238         \"486477467457448438429420410401392383374365356347338330\".\n007240     10 FILLER PIC X(54) VALUE                                    \n007242         \"321313304296288280272265257250243236229223216210205199\".\n007244     10 FILLER PIC X(54) VALUE                                    \n007246         \"194189184180176172168165162000000000000000000000000000\".\n007248     10 FILLER PIC X(54) VALUE                                    \n007250         \"000000000000000000000000000000000000000000000000000000\".\n007252     10 FILLER PIC X(27) VALUE                                    \n007254         \"000000000000000000000000000\".                           \n007256     10 FILLER PIC X(54) VALUE                                    \n007258         \"486476467457448438429419410401391382373364355346338329\".\n007260     10 FILLER PIC X(54) VALUE                                    \n007262         \"320312303295287279271263256248241234227220214208202196\".\n007264     10 FILLER PIC X(54) VALUE                                    \n007266         \"191186181176172168164160157000000000000000000000000000\".\n007268     10 FILLER PIC X(54) VALUE                                    \n007270         \"000000000000000000000000000000000000000000000000000000\".\n007272     10 FILLER PIC X(27) VALUE                                    \n007274         \"000000000000000000000000000\".                           \n007276     10 FILLER PIC X(54) VALUE                                    \n007278         \"486476467457448438429419410400391382373364355346337328\".\n007280     10 FILLER PIC X(54) VALUE                                    \n007282         \"320311303294286278270262254247239232225218212206199194\".\n007284     10 FILLER PIC X(54) VALUE                                    \n007286         \"188183178173168164160156153000000000000000000000000000\".\n007288     10 FILLER PIC X(54) VALUE                                    \n007290         \"000000000000000000000000000000000000000000000000000000\".\n007292     10 FILLER PIC X(27) VALUE                                    \n007294         \"000000000000000000000000000\".                           \n007296     10 FILLER PIC X(54) VALUE                                    \n007298         \"486476466457447438428419409400391382372363354345336328\".\n007300     10 FILLER PIC X(54) VALUE                                    \n007302         \"319310302293285277269261253246238231224217210203197191\".\n007304     10 FILLER PIC X(54) VALUE                                    \n007306         \"185180175170165160156152149000000000000000000000000000\".\n007308     10 FILLER PIC X(54) VALUE                                    \n007310         \"000000000000000000000000000000000000000000000000000000\".\n007312     10 FILLER PIC X(27) VALUE                                    \n007314         \"000000000000000000000000000\".                           \n007316     10 FILLER PIC X(54) VALUE                                    \n007318         \"486476466457447438428419409400391381372363354345336327\".\n007320     10 FILLER PIC X(54) VALUE                                    \n007322         \"318310301293284276268260252244237229222215208201195189\".\n007324     10 FILLER PIC X(54) VALUE                                    \n007326         \"183177172167162157153149145000000000000000000000000000\".\n007328     10 FILLER PIC X(54) VALUE                                    \n007330         \"000000000000000000000000000000000000000000000000000000\".\n007332     10 FILLER PIC X(27) VALUE                                    \n007334         \"000000000000000000000000000\".                           \n007336     10 FILLER PIC X(54) VALUE                                    \n007338         \"485476466457447437428418409400390381372363354345336327\".\n007340     10 FILLER PIC X(54) VALUE                                    \n007342         \"318309301292284275267259251243236228221213206200193187\".\n007344     10 FILLER PIC X(54) VALUE                                    \n007346         \"181175169164159154150145141138134131128126123121119117\".\n007348     10 FILLER PIC X(54) VALUE                                    \n007350         \"115000000000000000000000000000000000000000000000000000\".\n007352     10 FILLER PIC X(27) VALUE                                    \n007354         \"000000000000000000000000000\".                           \n007356     10 FILLER PIC X(54) VALUE                                    \n007358         \"485476466457447437428418409399390381372362353344335326\".\n007360     10 FILLER PIC X(54) VALUE                                    \n007362         \"318309300292283275266258250242234227219212205198191185\".\n007364     10 FILLER PIC X(54) VALUE                                    \n007366         \"179173167162156151147142138134131127124122119117114113\".\n007368     10 FILLER PIC X(54) VALUE                                    \n007370         \"111000000000000000000000000000000000000000000000000000\".\n007372     10 FILLER PIC X(27) VALUE                                    \n007374         \"000000000000000000000000000\".                           \n007376     10 FILLER PIC X(54) VALUE                                    \n007378         \"485476466456447437428418409399390381371362353344335326\".\n007380     10 FILLER PIC X(54) VALUE                                    \n007382         \"317308300291283274266285249241234226218211204197190183\".\n007384     10 FILLER PIC X(54) VALUE                                    \n007386         \"177171165159154149144139135131127124121118115113110108\".\n007388     10 FILLER PIC X(54) VALUE                                    \n007390         \"106000000000000000000000000000000000000000000000000000\".\n007392     10 FILLER PIC X(27) VALUE                                    \n007394         \"000000000000000000000000000\".                           \n007396     10 FILLER PIC X(54) VALUE                                    \n007398         \"485476466456447437428418409399390380371362353344335326\".\n007400     10 FILLER PIC X(54) VALUE                                    \n007402         \"317308299291282274265257249241233225217210202195188182\".\n007404     10 FILLER PIC X(54) VALUE                                    \n007406         \"175169163157152147142137132128124121117114111109106104\".\n007408     10 FILLER PIC X(54) VALUE                                    \n007410         \"102000000000000000000000000000000000000000000000000000\".\n007412     10 FILLER PIC X(27) VALUE                                    \n007414         \"000000000000000000000000000\".                           \n007416     10 FILLER PIC X(54) VALUE                                    \n007418         \"485476466456447437427418408399390380371362353343334325\".\n007420     10 FILLER PIC X(54) VALUE                                    \n007422         \"317308299290282273265256248240232224216209201194187180\".\n007424     10 FILLER PIC X(54) VALUE                                    \n007426         \"174167161155150144139134130126122118114111108105103101\".\n007428     10 FILLER PIC X(54) VALUE                                    \n007430         \"099000000000000000000000000000000000000000000000000000\".\n007432     10 FILLER PIC X(27) VALUE                                    \n007434         \"000000000000000000000000000\".                           \n007436     10 FILLER PIC X(54) VALUE                                    \n007438         \"485475466456447437427418408399389380371362352343334325\".\n007440     10 FILLER PIC X(54) VALUE                                    \n007442         \"316307299290281273264256248239231223216208201193186179\".\n007444     10 FILLER PIC X(54) VALUE                                    \n007446         \"173166160154148143137132128123119115111108105102099097\".\n007448     10 FILLER PIC X(54) VALUE                                    \n007450         \"095000000000000000000000000000000000000000000000000000\".\n007452     10 FILLER PIC X(27) VALUE                                    \n007454         \"000000000000000000000000000\".                           \n007456     10 FILLER PIC X(54) VALUE                                    \n007458         \"485475466456446437427418408399389380371361352343334325\".\n007460     10 FILLER PIC X(54) VALUE                                    \n007462         \"316307298290281272264255247239231223215207200192185178\".\n007464     10 FILLER PIC X(54) VALUE                                    \n007466         \"171165158152146141135130125121117113109105102099096094\".\n007468     10 FILLER PIC X(54) VALUE                                    \n007470         \"092000000000000000000000000000000000000000000000000000\".\n007472     10 FILLER PIC X(27) VALUE                                    \n007474         \"000000000000000000000000000\".                           \n007476     10 FILLER PIC X(54) VALUE                                    \n007478         \"485475466456446437427418408399389380370361352343334325\".\n007480     10 FILLER PIC X(54) VALUE                                    \n007482         \"316307298289281272264255247238230222214207199192184177\".\n007484     10 FILLER PIC X(54) VALUE                                    \n007486         \"170164157151145139134129124119114110106103099096094091\".\n007488     10 FILLER PIC X(54) VALUE                                    \n007490         \"089000000000000000000000000000000000000000000000000000\".\n007492     10 FILLER PIC X(27) VALUE                                    \n007494         \"000000000000000000000000000\".                           \n007496     10 FILLER PIC X(54) VALUE                                    \n007498         \"485475466456446437427418408399389380370361352343334325\".\n007500     10 FILLER PIC X(54) VALUE                                    \n007502         \"316307298289280272263255246238230222214206198191183176\".\n007504     10 FILLER PIC X(54) VALUE                                    \n007506         \"169163156150144138132127122117113108104101097094091088\".\n007508     10 FILLER PIC X(54) VALUE                                    \n007510         \"086000000000000000000000000000000000000000000000000000\".\n007512     10 FILLER PIC X(27) VALUE                                    \n007514         \"000000000000000000000000000\".                           \n007516     10 FILLER PIC X(54) VALUE                                    \n007518         \"485475466456446437427417408398389380370361352343333324\".\n007520     10 FILLER PIC X(54) VALUE                                    \n007522         \"315307298289280272263254246238229221213205198190183176\".\n007524     10 FILLER PIC X(54) VALUE                                    \n007526         \"169162155149143137131126120115111106102099095092089086\".\n007528     10 FILLER PIC X(54) VALUE                                    \n007530         \"083000000000000000000000000000000000000000000000000000\".\n007532     10 FILLER PIC X(27) VALUE                                    \n007534         \"000000000000000000000000000\".                           \n007536     10 FILLER PIC X(54) VALUE                                    \n007538         \"485475466456446437427417408398389380370361352342333324\".\n007540     10 FILLER PIC X(54) VALUE                                    \n007542         \"315306298289280271263254246237229221213205197190182175\".\n007544     10 FILLER PIC X(54) VALUE                                    \n007546         \"168161154148142136130124119114109105101097093090086083\".\n007548     10 FILLER PIC X(54) VALUE                                    \n007550         \"081078076074072071069068066065064000000000000000000000\".\n007552     10 FILLER PIC X(27) VALUE                                    \n007554         \"000000000000000000000000000\".                           \n007556     10 FILLER PIC X(54) VALUE                                    \n007558         \"485475466456446437427417408398389379370361352342333324\".\n007560     10 FILLER PIC X(54) VALUE                                    \n007562         \"315306297289280271263254245237229221213205197189182174\".\n007564     10 FILLER PIC X(54) VALUE                                    \n007566         \"167160154147141135129123118113108103099095091088084081\".\n007568     10 FILLER PIC X(54) VALUE                                    \n007570         \"079076074072070068067065064063061000000000000000000000\".\n007572     10 FILLER PIC X(27) VALUE                                    \n007574         \"000000000000000000000000000\".                           \n007576     10 FILLER PIC X(54) VALUE                                    \n007578         \"485475466456446437427417408398389379370361351342333324\".\n007580     10 FILLER PIC X(54) VALUE                                    \n007582         \"315306297288280271262254245237229220212204196189181174\".\n007584     10 FILLER PIC X(54) VALUE                                    \n007586         \"167160153146140134128122117112107102098093090086083080\".\n007588     10 FILLER PIC X(54) VALUE                                    \n007590         \"077074072070068066064063061060059000000000000000000000\".\n007592     10 FILLER PIC X(27) VALUE                                    \n007594         \"000000000000000000000000000\".                           \n007596     10 FILLER PIC X(54) VALUE                                    \n007598         \"485475466456446437427417408398389379370361351342333324\".\n007600     10 FILLER PIC X(54) VALUE                                    \n007602         \"315306297288280271262254245237228220212204196188181173\".\n007604     10 FILLER PIC X(54) VALUE                                    \n007606         \"166159152146139133127121116111106101096092088085081078\".\n007608     10 FILLER PIC X(54) VALUE                                    \n007610         \"075072070068066064062061059058056000000000000000000000\".\n007612     10 FILLER PIC X(27) VALUE                                    \n007614         \"000000000000000000000000000\".                           \n007616     10 FILLER PIC X(54) VALUE                                    \n007618         \"485475466456446437427417408398389379370361351342333324\".\n007620     10 FILLER PIC X(54) VALUE                                    \n007622         \"315306297288279271262253245236228220212204196188180173\".\n007624     10 FILLER PIC X(54) VALUE                                    \n007626         \"166159152145139132126120115110105100095091087083080076\".\n007628     10 FILLER PIC X(54) VALUE                                    \n007630         \"073071068066064062060059057056054000000000000000000000\".\n007632     10 FILLER PIC X(27) VALUE                                    \n007634         \"000000000000000000000000000\".                           \n007636     10 FILLER PIC X(54) VALUE                                    \n007638         \"485475465456446436427417408398389379370361351342333324\".\n007640     10 FILLER PIC X(54) VALUE                                    \n007642         \"315306297288279271262253245236228220211203196188180173\".\n007644     10 FILLER PIC X(54) VALUE                                    \n007646         \"165158151145138132126120114109104099094090086082078075\".\n007648     10 FILLER PIC X(54) VALUE                                    \n007650         \"072069067064062060058057055054052000000000000000000000\".\n007652     10 FILLER PIC X(27) VALUE                                    \n007654         \"000000000000000000000000000\".                           \n007656     10 FILLER PIC X(54) VALUE                                    \n007658         \"485475465456446436427417408398389379370361351342333324\".\n007660     10 FILLER PIC X(54) VALUE                                    \n007662         \"315306297288279270262253245236228219211203195188180172\".\n007664     10 FILLER PIC X(54) VALUE                                    \n007666         \"165158151144138131125119113108103098093089085081077074\".\n007668     10 FILLER PIC X(54) VALUE                                    \n007670         \"071068065063061059057055053052050000000000000000000000\".\n007672     10 FILLER PIC X(27) VALUE                                    \n007674         \"000000000000000000000000000\".                           \n007676     10 FILLER PIC X(54) VALUE                                    \n007678         \"485475465456446436427417408398389379370361351342333324\".\n007680     10 FILLER PIC X(54) VALUE                                    \n007682         \"315306297288279270262253245236228219211203195187180172\".\n007684     10 FILLER PIC X(54) VALUE                                    \n007686         \"165158151144137131125119113107102097092088084080076073\".\n007688     10 FILLER PIC X(54) VALUE                                    \n007690         \"069066064061059057055053052050049000000000000000000000\".\n007692     10 FILLER PIC X(27) VALUE                                    \n007694         \"000000000000000000000000000\".                           \n007696     10 FILLER PIC X(54) VALUE                                    \n007698         \"485475465456446436427417408398389379370360351342333324\".\n007700     10 FILLER PIC X(54) VALUE                                    \n007702         \"315306297288279270262253244236228219211203195187179172\".\n007704     10 FILLER PIC X(54) VALUE                                    \n007706         \"164157150143137130124118112107101096092087083079075071\".\n007708     10 FILLER PIC X(54) VALUE                                    \n007710         \"068065063060058056054052050048047000000000000000000000\".\n007712     10 FILLER PIC X(27) VALUE                                    \n007714         \"000000000000000000000000000\".                           \n007716     10 FILLER PIC X(54) VALUE                                    \n007718         \"485475465456446436427417408398389379370360351342333324\".\n007720     10 FILLER PIC X(54) VALUE                                    \n007722         \"315306297288279270262253244236227219211203195187179172\".\n007724     10 FILLER PIC X(54) VALUE                                    \n007726         \"164157150143136130124118112106101096091086082078074070\".\n007728     10 FILLER PIC X(54) VALUE                                    \n007730         \"067064061059056054052050049047045000000000000000000000\".\n007732     10 FILLER PIC X(27) VALUE                                    \n007734         \"000000000000000000000000000\".                           \n007736     10 FILLER PIC X(54) VALUE                                    \n007738         \"485475465456446436427417408398389379370360351342333324\".\n007740     10 FILLER PIC X(54) VALUE                                    \n007742         \"315306297288279270261253244236227219211203195187179171\".\n007744     10 FILLER PIC X(54) VALUE                                    \n007746         \"164157150143136129123117111106100095090085081077073069\".\n007748     10 FILLER PIC X(54) VALUE                                    \n007750         \"066063060058055053051049047045044042041039038037035034\".\n007752     10 FILLER PIC X(27) VALUE                                    \n007754         \"033033032000000000000000000\".                           \n007756     10 FILLER PIC X(54) VALUE                                    \n007758         \"485475465456446436427417408398389379370360351342333324\".\n007760     10 FILLER PIC X(54) VALUE                                    \n007762         \"315306297288279270261253244236227219211202194187179171\".\n007764     10 FILLER PIC X(54) VALUE                                    \n007766         \"164156149142136129123117111105100094090085080076072069\".\n007768     10 FILLER PIC X(54) VALUE                                    \n007770         \"065062059056054052050048046044042041039037036035034032\".\n007772     10 FILLER PIC X(27) VALUE                                    \n007774         \"031031030000000000000000000\".                           \n007776     10 FILLER PIC X(54) VALUE                                    \n007778         \"485475465456446436427417408398389379370360351342333324\".\n007780     10 FILLER PIC X(54) VALUE                                    \n007782         \"314305297288279270261253244236227219211202194186179171\".\n007784     10 FILLER PIC X(54) VALUE                                    \n007786         \"164156149142135129122116110105099094089084080075071068\".\n007788     10 FILLER PIC X(54) VALUE                                    \n007790         \"064061058055053051048046044043041039037036034033032031\".\n007792     10 FILLER PIC X(27) VALUE                                    \n007794         \"030029028000000000000000000\".                           \n007796     10 FILLER PIC X(54) VALUE                                    \n007798         \"485475465456446436427417408398389379370360351342333324\".\n007800     10 FILLER PIC X(54) VALUE                                    \n007802         \"314305297288279270261253244236227219210202194186179171\".\n007804     10 FILLER PIC X(54) VALUE                                    \n007806         \"163156149142135129122116110104099094088084079075071067\".\n007808     10 FILLER PIC X(54) VALUE                                    \n007810         \"063060057054052050047045043041040038036034033032030029\".\n007812     10 FILLER PIC X(27) VALUE                                    \n007814         \"028027026000000000000000000\".                           \n007816     10 FILLER PIC X(54) VALUE                                    \n007818         \"485475465456446436427417408398388379370360351342333324\".\n007820     10 FILLER PIC X(54) VALUE                                    \n007822         \"314305296288279270261253244235227219210202194186178171\".\n007824     10 FILLER PIC X(54) VALUE                                    \n007826         \"163156149142135128122116110104098093088083079074070066\".\n007828     10 FILLER PIC X(54) VALUE                                    \n007830         \"063059056054051049046044042040038037035033032030029027\".\n007832     10 FILLER PIC X(27) VALUE                                    \n007834         \"026025024000000000000000000\".                           \n007836     10 FILLER PIC X(54) VALUE                                    \n007838         \"485475465456446436427417408398388379370360351342333323\".\n007840     10 FILLER PIC X(54) VALUE                                    \n007842         \"314305296288279270261253244235227219210202194186178171\".\n007844     10 FILLER PIC X(54) VALUE                                    \n007846         \"163156149142135128122115109104098093088083078074070066\".\n007848     10 FILLER PIC X(54) VALUE                                    \n007850         \"062059056053050048045043041039037035034032030029027026\".\n007852     10 FILLER PIC X(27) VALUE                                    \n007854         \"025024023000000000000000000\".                           \n007856     10 FILLER PIC X(54) VALUE                                    \n007858         \"485475465456446436427417408398388379370360351342333323\".\n007860     10 FILLER PIC X(54) VALUE                                    \n007862         \"315305296288279270261253244235227219210202194186178171\".\n007864     10 FILLER PIC X(54) VALUE                                    \n007866         \"163156148141135128122115109103098092087082078073069065\".\n007868     10 FILLER PIC X(54) VALUE                                    \n007870         \"062058055052049047045042040038036034032031029027026024\".\n007872     10 FILLER PIC X(27) VALUE                                    \n007874         \"023022021000000000000000000\".                           \n007876     10 FILLER PIC X(54) VALUE                                    \n007878         \"485475465456446436427417408398388379370360351342333323\".\n007880     10 FILLER PIC X(54) VALUE                                    \n007882         \"314305296288279270261252244235227218210202194186178170\".\n007884     10 FILLER PIC X(54) VALUE                                    \n007886         \"163156148141134128121115109103098092087082077073069065\".\n007888     10 FILLER PIC X(54) VALUE                                    \n007890         \"061058054051049046044042039037035033031030028026025023\".\n007892     10 FILLER PIC X(27) VALUE                                    \n007894         \"022021020000000000000000000\".                           \n007896     10 FILLER PIC X(54) VALUE                                    \n007898         \"485475465456446436427417408398388379370360351342333323\".\n007900     10 FILLER PIC X(54) VALUE                                    \n007902         \"314305296288279270261252244235227218210202194186178170\".\n007904     10 FILLER PIC X(54) VALUE                                    \n007906         \"163155148141134128121115109103097092087082077073068064\".\n007908     10 FILLER PIC X(54) VALUE                                    \n007910         \"061057054051048046043041039037035033031029027025024022\".\n007912     10 FILLER PIC X(27) VALUE                                    \n007914         \"021019018000000000000000000\".                           \n007916     10 FILLER PIC X(54) VALUE                                    \n007918         \"485475465456446436427417407398388379370360351342333323\".\n007920     10 FILLER PIC X(54) VALUE                                    \n007922         \"314305296287279270261252244235227218210202194186178170\".\n007924     10 FILLER PIC X(54) VALUE                                    \n007926         \"163155148141134128121115109103097092087082077072068064\".\n007928     10 FILLER PIC X(54) VALUE                                    \n007930         \"060057053050048045043040038036034032030028026024023021\".\n007932     10 FILLER PIC X(27) VALUE                                    \n007934         \"020018017000000000000000000\".                           \n007936     10 FILLER PIC X(54) VALUE                                    \n007938         \"485475465456446436427417407398388379370360351342333323\".\n007940     10 FILLER PIC X(54) VALUE                                    \n007942         \"314305296287279270261252244235227218210202194186178170\".\n007944     10 FILLER PIC X(54) VALUE                                    \n007946         \"163155148141134127121115109103097092086081077072068064\".\n007948     10 FILLER PIC X(54) VALUE                                    \n007950         \"060056053050047045042040038035033031029027025023022020\".\n007952     10 FILLER PIC X(27) VALUE                                    \n007954         \"019017016015014013012011011\".                           \n007956     10 FILLER PIC X(54) VALUE                                    \n007958         \"485475465456446436427417407398388379370360351342333323\".\n007960     10 FILLER PIC X(54) VALUE                                    \n007962         \"314305296287279270261252244235227218210202194186178170\".\n007964     10 FILLER PIC X(54) VALUE                                    \n007966         \"163155148141134127121115108103097091086081076072068063\".\n007968     10 FILLER PIC X(54) VALUE                                    \n007970         \"060056053050047044042039037035033031029027025023021019\".\n007972     10 FILLER PIC X(27) VALUE                                    \n007974         \"018016015014012011011010010\".                           \n007976     10 FILLER PIC X(54) VALUE                                    \n007978         \"485475465456446436427417407398388379370360351342333323\".\n007980     10 FILLER PIC X(54) VALUE                                    \n007982         \"314305296287279270261252244235227218210202194186178170\".\n007984     10 FILLER PIC X(54) VALUE                                    \n007986         \"163155148141134127121115108102097091086081076072067063\".\n007988     10 FILLER PIC X(54) VALUE                                    \n007990         \"059056053049047044041039037035032030028026024022020019\".\n007992     10 FILLER PIC X(27) VALUE                                    \n007994         \"017015014013011010010010010\".                           \n007996     10 FILLER PIC X(54) VALUE                                    \n007998         \"485475465456446436427417407398388379370360351342333323\".\n008000     10 FILLER PIC X(54) VALUE                                    \n008002         \"314305296287279270261252244235227218210202194186178170\".\n008004     10 FILLER PIC X(54) VALUE                                    \n008006         \"163155148141134127121114108102097091086081076072067063\".\n008008     10 FILLER PIC X(54) VALUE                                    \n008010         \"059056052049046044041039036034032030028026024022020018\".\n008012     10 FILLER PIC X(27) VALUE                                    \n008014         \"016015013012011010010010010\".                           \n008016     10 FILLER PIC X(54) VALUE                                    \n008018         \"485475465456446436427417407398388379370360351342333323\".\n008020     10 FILLER PIC X(54) VALUE                                    \n008022         \"314305296287279270261252244235227218210202194186178170\".\n008024     10 FILLER PIC X(54) VALUE                                    \n008026         \"163155148141134127121114108102097091086081076071067063\".\n008028     10 FILLER PIC X(54) VALUE                                    \n008030         \"059056052049046043041039036034032030027025023021019018\".\n008032     10 FILLER PIC X(27) VALUE                                    \n008034         \"016014013011010010010010010\".                           \n008036     10 FILLER PIC X(54) VALUE                                    \n008038         \"485475465456446436427417407398388379370360351342333323\".\n008040     10 FILLER PIC X(54) VALUE                                    \n008042         \"314305296287279270261252244235227218210202194186178170\".\n008044     10 FILLER PIC X(54) VALUE                                    \n008046         \"163155148141134127121114108102097091086081076071067063\".\n008048     10 FILLER PIC X(54) VALUE                                    \n008050         \"059055052049046043041038036034031029027025023021019017\".\n008052     10 FILLER PIC X(27) VALUE                                    \n008054         \"015014012011010010010010010\".                           \n008056                                                                  \n008058   05  WS-RMD-LEF-TABLE-2 REDEFINES RMD-LEF-TABLE-2.              \n008060       10  WS-RMD-LEF-TBL-2-REC OCCURS 81 TIMES.                  \n008062           15  WS-RMD-TBL2-LEF  PIC 999 OCCURS 81 TIMES.          \n008064                                                                  \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    817 lines from 3212 to 4028.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 9, "total_chunks": 55, "start_line": 3212, "end_line": 4028, "line_count": 817}

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
- Source code length: 64591 characters

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
CHUNK 9 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 3212 to 4028 (817 lines)
Chunk Tokens (estimated): ~14,869
Actual Input Tokens: 16,275 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 3212-4028 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 9 of 55 chunks
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
      The source code below is only CHUNK 9 of 55.


=============================================================================
CHUNK 9 SOURCE CODE (Lines 3212-4028)
=============================================================================

```cobol
006432 01  RMD-LEF-TABLE-2-X.                                           
006434   05  RMD-LEF-TABLE-2.                                           
006436     10 FILLER PIC X(54) VALUE                                    
006438         "552547543538534000000000000000000000000000000000000000".
006440     10 FILLER PIC X(54) VALUE                                    
006442         "000000000000000000000000000000000000000000000000000000".
006444     10 FILLER PIC X(54) VALUE                                    
006446         "000000000000000000000000000000000000000000000000000000".
006448     10 FILLER PIC X(54) VALUE                                    
006450         "000000000000000000000000000000000000000000000000000000".
006452     10 FILLER PIC X(27) VALUE                                    
006454         "000000000000000000000000000".                           
006456     10 FILLER PIC X(54) VALUE                                    
006458         "547542537533528000000000000000000000000000000000000000".
006460     10 FILLER PIC X(54) VALUE                                    
006462         "000000000000000000000000000000000000000000000000000000".
006464     10 FILLER PIC X(54) VALUE                                    
006466         "000000000000000000000000000000000000000000000000000000".
006468     10 FILLER PIC X(54) VALUE                                    
006470         "000000000000000000000000000000000000000000000000000000".
006472     10 FILLER PIC X(27) VALUE                                    
006474         "000000000000000000000000000".                           
006476     10 FILLER PIC X(54) VALUE                                    
006478         "543537532527523000000000000000000000000000000000000000".
006480     10 FILLER PIC X(54) VALUE                                    
006482         "000000000000000000000000000000000000000000000000000000".
006484     10 FILLER PIC X(54) VALUE                                    
006486         "000000000000000000000000000000000000000000000000000000".
006488     10 FILLER PIC X(54) VALUE                                    
006490         "000000000000000000000000000000000000000000000000000000".
006492     10 FILLER PIC X(27) VALUE                                    
006494         "000000000000000000000000000".                           
006496     10 FILLER PIC X(54) VALUE                                    
006498         "538533527522517000000000000000000000000000000000000000".
006500     10 FILLER PIC X(54) VALUE                                    
006502         "000000000000000000000000000000000000000000000000000000".
006504     10 FILLER PIC X(54) VALUE                                    
006506         "000000000000000000000000000000000000000000000000000000".
006508     10 FILLER PIC X(54) VALUE                                    
006510         "000000000000000000000000000000000000000000000000000000".
006512     10 FILLER PIC X(27) VALUE                                    
006514         "000000000000000000000000000".                           
006516     10 FILLER PIC X(54) VALUE                                    
006518         "534528523517512000000000000000000000000000000000000000".
006520     10 FILLER PIC X(54) VALUE                                    
006522         "000000000000000000000000000000000000000000000000000000".
006524     10 FILLER PIC X(54) VALUE                                    
006526         "000000000000000000000000000000000000000000000000000000".
006528     10 FILLER PIC X(54) VALUE                                    
006530         "000000000000000000000000000000000000000000000000000000".
006532     10 FILLER PIC X(27) VALUE                                    
006534         "000000000000000000000000000".                           
006536     10 FILLER PIC X(54) VALUE                                    
006538         "530524518513508502498493489485481477474471468000000000".
006540     10 FILLER PIC X(54) VALUE                                    
006542         "000000000000000000000000000000000000000000000000000000".
006544     10 FILLER PIC X(54) VALUE                                    
006546         "000000000000000000000000000000000000000000000000000000".
006548     10 FILLER PIC X(54) VALUE                                    
006550         "000000000000000000000000000000000000000000000000000000".
006552     10 FILLER PIC X(27) VALUE                                    
006554         "000000000000000000000000000".                           
006556     10 FILLER PIC X(54) VALUE                                    
006558         "527520514509503498493488483479475471467464461000000000".
006560     10 FILLER PIC X(54) VALUE                                    
006562         "000000000000000000000000000000000000000000000000000000".
006564     10 FILLER PIC X(54) VALUE                                    
006566         "000000000000000000000000000000000000000000000000000000".
006568     10 FILLER PIC X(54) VALUE                                    
006570         "000000000000000000000000000000000000000000000000000000".
006572     10 FILLER PIC X(27) VALUE                                    
006574         "000000000000000000000000000".                           
006576     10 FILLER PIC X(54) VALUE                                    
006578         "523517511504499493488483478473469465461458454000000000".
006580     10 FILLER PIC X(54) VALUE                                    
006582         "000000000000000000000000000000000000000000000000000000".
006584     10 FILLER PIC X(54) VALUE                                    
006586         "000000000000000000000000000000000000000000000000000000".
006588     10 FILLER PIC X(54) VALUE                                    
006590         "000000000000000000000000000000000000000000000000000000".
006592     10 FILLER PIC X(27) VALUE                                    
006594         "000000000000000000000000000".                           
006596     10 FILLER PIC X(54) VALUE                                    
006598         "520513507501495489483478473468463459455451448000000000".
006600     10 FILLER PIC X(54) VALUE                                    
006602         "000000000000000000000000000000000000000000000000000000".
006604     10 FILLER PIC X(54) VALUE                                    
006606         "000000000000000000000000000000000000000000000000000000".
006608     10 FILLER PIC X(54) VALUE                                    
006610         "000000000000000000000000000000000000000000000000000000".
006612     10 FILLER PIC X(27) VALUE                                    
006614         "000000000000000000000000000".                           
006616     10 FILLER PIC X(54) VALUE                                    
006618         "517510504497491485479473468463458454449445442000000000".
006620     10 FILLER PIC X(54) VALUE                                    
006622         "000000000000000000000000000000000000000000000000000000".
006624     10 FILLER PIC X(54) VALUE                                    
006626         "000000000000000000000000000000000000000000000000000000".
006628     10 FILLER PIC X(54) VALUE                                    
006630         "000000000000000000000000000000000000000000000000000000".
006632     10 FILLER PIC X(27) VALUE                                    
006634         "000000000000000000000000000".                           
006636     10 FILLER PIC X(54) VALUE                                    
006638         "515507500494487481475469463458453448444440436000000000".
006640     10 FILLER PIC X(54) VALUE                                    
006642         "000000000000000000000000000000000000000000000000000000".
006644     10 FILLER PIC X(54) VALUE                                    
006646         "000000000000000000000000000000000000000000000000000000".
006648     10 FILLER PIC X(54) VALUE                                    
006650         "000000000000000000000000000000000000000000000000000000".
006652     10 FILLER PIC X(27) VALUE                                    
006654         "000000000000000000000000000".                           
006656     10 FILLER PIC X(54) VALUE                                    
006658         "512505498491484477471465459454448443439434430000000000".
006660     10 FILLER PIC X(54) VALUE                                    
006662         "000000000000000000000000000000000000000000000000000000".
006664     10 FILLER PIC X(54) VALUE                                    
006666         "000000000000000000000000000000000000000000000000000000".
006668     10 FILLER PIC X(54) VALUE                                    
006670         "000000000000000000000000000000000000000000000000000000".
006672     10 FILLER PIC X(27) VALUE                                    
006674         "000000000000000000000000000".                           
006676     10 FILLER PIC X(54) VALUE                                    
006678         "510502495488481474467461455449444439434429424000000000".
006680     10 FILLER PIC X(54) VALUE                                    
006682         "000000000000000000000000000000000000000000000000000000".
006684     10 FILLER PIC X(54) VALUE                                    
006686         "000000000000000000000000000000000000000000000000000000".
006688     10 FILLER PIC X(54) VALUE                                    
006690         "000000000000000000000000000000000000000000000000000000".
006692     10 FILLER PIC X(27) VALUE                                    
006694         "000000000000000000000000000".                           
006696     10 FILLER PIC X(54) VALUE                                    
006698         "508500492485478471464458451445440434429424419000000000".
006700     10 FILLER PIC X(54) VALUE                                    
006702         "000000000000000000000000000000000000000000000000000000".
006704     10 FILLER PIC X(54) VALUE                                    
006706         "000000000000000000000000000000000000000000000000000000".
006708     10 FILLER PIC X(54) VALUE                                    
006710         "000000000000000000000000000000000000000000000000000000".
006712     10 FILLER PIC X(27) VALUE                                    
006714         "000000000000000000000000000".                           
006716     10 FILLER PIC X(54) VALUE                                    
006718         "506498490482475468461454448442436430424419414000000000".
006720     10 FILLER PIC X(54) VALUE                                    
006722         "000000000000000000000000000000000000000000000000000000".
006724     10 FILLER PIC X(54) VALUE                                    
006726         "000000000000000000000000000000000000000000000000000000".
006728     10 FILLER PIC X(54) VALUE                                    
006730         "000000000000000000000000000000000000000000000000000000".
006732     10 FILLER PIC X(27) VALUE                                    
006734         "000000000000000000000000000".                           
006736     10 FILLER PIC X(54) VALUE                                    
006738         "504496488480473465458451444438432426420415409404400395".
006740     10 FILLER PIC X(54) VALUE                                    
006742         "391387383380376373371000000000000000000000000000000000".
006744     10 FILLER PIC X(54) VALUE                                    
006746         "000000000000000000000000000000000000000000000000000000".
006748     10 FILLER PIC X(54) VALUE                                    
006750         "000000000000000000000000000000000000000000000000000000".
006752     10 FILLER PIC X(27) VALUE                                    
006754         "000000000000000000000000000".                           
006756     10 FILLER PIC X(54) VALUE                                    
006758         "502494486478470463455448441435428422416410405400395390".
006760     10 FILLER PIC X(54) VALUE                                    
006762         "385381377374370367364000000000000000000000000000000000".
006764     10 FILLER PIC X(54) VALUE                                    
006766         "000000000000000000000000000000000000000000000000000000".
006768     10 FILLER PIC X(54) VALUE                                    
006770         "000000000000000000000000000000000000000000000000000000".
006772     10 FILLER PIC X(27) VALUE                                    
006774         "000000000000000000000000000".                           
006776     10 FILLER PIC X(54) VALUE                                    
006778         "500492484476468460453446438432425418412406401395390385".
006780     10 FILLER PIC X(54) VALUE                                    
006782         "380376372368364360357000000000000000000000000000000000".
006784     10 FILLER PIC X(54) VALUE                                    
006786         "000000000000000000000000000000000000000000000000000000".
006788     10 FILLER PIC X(54) VALUE                                    
006790         "000000000000000000000000000000000000000000000000000000".
006792     10 FILLER PIC X(27) VALUE                                    
006794         "000000000000000000000000000".                           
006796     10 FILLER PIC X(54) VALUE                                    
006798         "499491482474466458451443436429422415409403397391385380".
006800     10 FILLER PIC X(54) VALUE                                    
006802         "375371366362358354351000000000000000000000000000000000".
006804     10 FILLER PIC X(54) VALUE                                    
006806         "000000000000000000000000000000000000000000000000000000".
006808     10 FILLER PIC X(54) VALUE                                    
006810         "000000000000000000000000000000000000000000000000000000".
006812     10 FILLER PIC X(27) VALUE                                    
006814         "000000000000000000000000000".                           
006816     10 FILLER PIC X(54) VALUE                                    
006818         "498489481472464456448441433426419412405399393387381376".
006820     10 FILLER PIC X(54) VALUE                                    
006822         "371366361357352348345000000000000000000000000000000000".
006824     10 FILLER PIC X(54) VALUE                                    
006826         "000000000000000000000000000000000000000000000000000000".
006828     10 FILLER PIC X(54) VALUE                                    
006830         "000000000000000000000000000000000000000000000000000000".
006832     10 FILLER PIC X(27) VALUE                                    
006834         "000000000000000000000000000".                           
006836     10 FILLER PIC X(54) VALUE                                    
006838         "497488479471463455447439431424416409402396389383377372".
006840     10 FILLER PIC X(54) VALUE                                    
006842         "366361356351347343339000000000000000000000000000000000".
006844     10 FILLER PIC X(54) VALUE                                    
006846         "000000000000000000000000000000000000000000000000000000".
006848     10 FILLER PIC X(54) VALUE                                    
006850         "000000000000000000000000000000000000000000000000000000".
006852     10 FILLER PIC X(27) VALUE                                    
006854         "000000000000000000000000000".                           
006856     10 FILLER PIC X(54) VALUE                                    
006858         "495487478470461453445437429421414407400393386380374368".
006860     10 FILLER PIC X(54) VALUE                                    
006862         "362357351347342337333000000000000000000000000000000000".
006864     10 FILLER PIC X(54) VALUE                                    
006866         "000000000000000000000000000000000000000000000000000000".
006868     10 FILLER PIC X(54) VALUE                                    
006870         "000000000000000000000000000000000000000000000000000000".
006872     10 FILLER PIC X(27) VALUE                                    
006874         "000000000000000000000000000".                           
006876     10 FILLER PIC X(54) VALUE                                    
006878         "494486477468460451443435427419412404397390383376370364".
006880     10 FILLER PIC X(54) VALUE                                    
006882         "358352347342337332328000000000000000000000000000000000".
006884     10 FILLER PIC X(54) VALUE                                    
006886         "000000000000000000000000000000000000000000000000000000".
006888     10 FILLER PIC X(54) VALUE                                    
006890         "000000000000000000000000000000000000000000000000000000".
006892     10 FILLER PIC X(27) VALUE                                    
006894         "000000000000000000000000000".                           
006896     10 FILLER PIC X(54) VALUE                                    
006898         "494485476467458450442433425417409402394387380373367360".
006900     10 FILLER PIC X(54) VALUE                                    
006902         "354348343337332328323000000000000000000000000000000000".
006904     10 FILLER PIC X(54) VALUE                                    
006906         "000000000000000000000000000000000000000000000000000000".
006908     10 FILLER PIC X(54) VALUE                                    
006910         "000000000000000000000000000000000000000000000000000000".
006912     10 FILLER PIC X(27) VALUE                                    
006914         "000000000000000000000000000".                           
006916     10 FILLER PIC X(54) VALUE                                    
006918         "493484475466457449440432424415407400392385378371364357".
006920     10 FILLER PIC X(54) VALUE                                    
006922         "351345339333328323318000000000000000000000000000000000".
006924     10 FILLER PIC X(54) VALUE                                    
006926         "000000000000000000000000000000000000000000000000000000".
006928     10 FILLER PIC X(54) VALUE                                    
006930         "000000000000000000000000000000000000000000000000000000".
006932     10 FILLER PIC X(27) VALUE                                    
006934         "000000000000000000000000000".                           
006936     10 FILLER PIC X(54) VALUE                                    
006938         "492483474465456447439430422414406398390382375368361354".
006940     10 FILLER PIC X(54) VALUE                                    
006942         "348341335329324319313309304300296292288285282279276000".
006944     10 FILLER PIC X(54) VALUE                                    
006946         "000000000000000000000000000000000000000000000000000000".
006948     10 FILLER PIC X(54) VALUE                                    
006950         "000000000000000000000000000000000000000000000000000000".
006952     10 FILLER PIC X(27) VALUE                                    
006954         "000000000000000000000000000".                           
006956     10 FILLER PIC X(54) VALUE                                    
006958         "491482473464455446438429421412404396388380373366358351".
006960     10 FILLER PIC X(54) VALUE                                    
006962         "345338332326320314309304299295290286283279276273270000".
006964     10 FILLER PIC X(54) VALUE                                    
006966         "000000000000000000000000000000000000000000000000000000".
006968     10 FILLER PIC X(54) VALUE                                    
006970         "000000000000000000000000000000000000000000000000000000".
006972     10 FILLER PIC X(27) VALUE                                    
006974         "000000000000000000000000000".                           
006976     10 FILLER PIC X(54) VALUE                                    
006978         "491481472463454445437428419411403394386378371363356349".
006980     10 FILLER PIC X(54) VALUE                                    
006982         "342335329322316311305300295290285281277273270267264000".
006984     10 FILLER PIC X(54) VALUE                                    
006986         "000000000000000000000000000000000000000000000000000000".
006988     10 FILLER PIC X(54) VALUE                                    
006990         "000000000000000000000000000000000000000000000000000000".
006992     10 FILLER PIC X(27) VALUE                                    
006994         "000000000000000000000000000".                           
006996     10 FILLER PIC X(54) VALUE                                    
006998         "490481472463453445436427418410401393385377369361354346".
007000     10 FILLER PIC X(54) VALUE                                    
007002         "339332326319313307301296290285281276272268264261257000".
007004     10 FILLER PIC X(54) VALUE                                    
007006         "000000000000000000000000000000000000000000000000000000".
007008     10 FILLER PIC X(54) VALUE                                    
007010         "000000000000000000000000000000000000000000000000000000".
007012     10 FILLER PIC X(27) VALUE                                    
007014         "000000000000000000000000000".                           
007016     10 FILLER PIC X(54) VALUE                                    
007018         "489480471462453444435426417408400392383375367359352344".
007020     10 FILLER PIC X(54) VALUE                                    
007022         "337330323316310304298292286281276271267263259255252000".
007024     10 FILLER PIC X(54) VALUE                                    
007026         "000000000000000000000000000000000000000000000000000000".
007028     10 FILLER PIC X(54) VALUE                                    
007030         "000000000000000000000000000000000000000000000000000000".
007032     10 FILLER PIC X(27) VALUE                                    
007034         "000000000000000000000000000".                           
007036     10 FILLER PIC X(54) VALUE                                    
007038         "489480470461452443434425416407399390382374366358350342".
007040     10 FILLER PIC X(54) VALUE                                    
007042         "335327320314307300294288283277272267262258254250246000".
007044     10 FILLER PIC X(54) VALUE                                    
007046         "000000000000000000000000000000000000000000000000000000".
007048     10 FILLER PIC X(54) VALUE                                    
007050         "000000000000000000000000000000000000000000000000000000".
007052     10 FILLER PIC X(27) VALUE                                    
007054         "000000000000000000000000000".                           
007056     10 FILLER PIC X(54) VALUE                                    
007058         "489479470461451442433424415406398389381372364356348340".
007060     10 FILLER PIC X(54) VALUE                                    
007062         "333325318311304298291285279273268263258253249245241000".
007064     10 FILLER PIC X(54) VALUE                                    
007066         "000000000000000000000000000000000000000000000000000000".
007068     10 FILLER PIC X(54) VALUE                                    
007070         "000000000000000000000000000000000000000000000000000000".
007072     10 FILLER PIC X(27) VALUE                                    
007074         "000000000000000000000000000".                           
007076     10 FILLER PIC X(54) VALUE                                    
007078         "488479469460451442433423414406397388380371363355347339".
007080     10 FILLER PIC X(54) VALUE                                    
007082         "331323316309302295288282276270264259254249244240236000".
007084     10 FILLER PIC X(54) VALUE                                    
007086         "000000000000000000000000000000000000000000000000000000".
007088     10 FILLER PIC X(54) VALUE                                    
007090         "000000000000000000000000000000000000000000000000000000".
007092     10 FILLER PIC X(27) VALUE                                    
007094         "000000000000000000000000000".                           
007096     10 FILLER PIC X(54) VALUE                                    
007098         "488478469460450441432423414405396387379370362353345337".
007100     10 FILLER PIC X(54) VALUE                                    
007102         "329321314307299292286279273267261255250245240235231000".
007104     10 FILLER PIC X(54) VALUE                                    
007106         "000000000000000000000000000000000000000000000000000000".
007108     10 FILLER PIC X(54) VALUE                                    
007110         "000000000000000000000000000000000000000000000000000000".
007112     10 FILLER PIC X(27) VALUE                                    
007114         "000000000000000000000000000".                           
007116     10 FILLER PIC X(54) VALUE                                    
007118         "487478469459450441431422413404395386378369360352344336".
007120     10 FILLER PIC X(54) VALUE                                    
007122         "328320312305297290283276270264257252246241236231226000".
007124     10 FILLER PIC X(54) VALUE                                    
007126         "000000000000000000000000000000000000000000000000000000".
007128     10 FILLER PIC X(54) VALUE                                    
007130         "000000000000000000000000000000000000000000000000000000".
007132     10 FILLER PIC X(27) VALUE                                    
007134         "000000000000000000000000000".                           
007136     10 FILLER PIC X(54) VALUE                                    
007138         "487478468459449440431422413403394386377368359351343334".
007140     10 FILLER PIC X(54) VALUE                                    
007142         "326318311303295288281274267261254248243237232227222218".
007144     10 FILLER PIC X(54) VALUE                                    
007146         "213209206202199196194191189000000000000000000000000000".
007148     10 FILLER PIC X(54) VALUE                                    
007150         "000000000000000000000000000000000000000000000000000000".
007152     10 FILLER PIC X(27) VALUE                                    
007154         "000000000000000000000000000".                           
007156     10 FILLER PIC X(54) VALUE                                    
007158         "487477468459449440430421412403394385376367359350342333".
007160     10 FILLER PIC X(54) VALUE                                    
007162         "325317309301294286279272265258252245239234228223218213".
007164     10 FILLER PIC X(54) VALUE                                    
007166         "209205201197194191188185183000000000000000000000000000".
007168     10 FILLER PIC X(54) VALUE                                    
007170         "000000000000000000000000000000000000000000000000000000".
007172     10 FILLER PIC X(27) VALUE                                    
007174         "000000000000000000000000000".                           
007176     10 FILLER PIC X(54) VALUE                                    
007178         "487477468458449439430421411402393384375366358349341332".
007180     10 FILLER PIC X(54) VALUE                                    
007182         "324316308300292284277270263256249243237231225220214209".
007184     10 FILLER PIC X(54) VALUE                                    
007186         "205200196193189186183180177000000000000000000000000000".
007188     10 FILLER PIC X(54) VALUE                                    
007190         "000000000000000000000000000000000000000000000000000000".
007192     10 FILLER PIC X(27) VALUE                                    
007194         "000000000000000000000000000".                           
007196     10 FILLER PIC X(54) VALUE                                    
007198         "486477467458448439430420411402393384375366357348340331".
007200     10 FILLER PIC X(54) VALUE                                    
007202         "323315306298291283275268261254247240234228222216211206".
007204     10 FILLER PIC X(54) VALUE                                    
007206         "201196192188184181178175172000000000000000000000000000".
007208     10 FILLER PIC X(54) VALUE                                    
007210         "000000000000000000000000000000000000000000000000000000".
007212     10 FILLER PIC X(27) VALUE                                    
007214         "000000000000000000000000000".                           
007216     10 FILLER PIC X(54) VALUE                                    
007218         "486477467458448439429420411401392383374365356348339330".
007220     10 FILLER PIC X(54) VALUE                                    
007222         "322314305297289281274266259252245238231225219213208202".
007224     10 FILLER PIC X(54) VALUE                                    
007226         "197193188184180176173170167000000000000000000000000000".
007228     10 FILLER PIC X(54) VALUE                                    
007230         "000000000000000000000000000000000000000000000000000000".
007232     10 FILLER PIC X(27) VALUE                                    
007234         "000000000000000000000000000".                           
007236     10 FILLER PIC X(54) VALUE                                    
007238         "486477467457448438429420410401392383374365356347338330".
007240     10 FILLER PIC X(54) VALUE                                    
007242         "321313304296288280272265257250243236229223216210205199".
007244     10 FILLER PIC X(54) VALUE                                    
007246         "194189184180176172168165162000000000000000000000000000".
007248     10 FILLER PIC X(54) VALUE                                    
007250         "000000000000000000000000000000000000000000000000000000".
007252     10 FILLER PIC X(27) VALUE                                    
007254         "000000000000000000000000000".                           
007256     10 FILLER PIC X(54) VALUE                                    
007258         "486476467457448438429419410401391382373364355346338329".
007260     10 FILLER PIC X(54) VALUE                                    
007262         "320312303295287279271263256248241234227220214208202196".
007264     10 FILLER PIC X(54) VALUE                                    
007266         "191186181176172168164160157000000000000000000000000000".
007268     10 FILLER PIC X(54) VALUE                                    
007270         "000000000000000000000000000000000000000000000000000000".
007272     10 FILLER PIC X(27) VALUE                                    
007274         "000000000000000000000000000".                           
007276     10 FILLER PIC X(54) VALUE                                    
007278         "486476467457448438429419410400391382373364355346337328".
007280     10 FILLER PIC X(54) VALUE                                    
007282         "320311303294286278270262254247239232225218212206199194".
007284     10 FILLER PIC X(54) VALUE                                    
007286         "188183178173168164160156153000000000000000000000000000".
007288     10 FILLER PIC X(54) VALUE                                    
007290         "000000000000000000000000000000000000000000000000000000".
007292     10 FILLER PIC X(27) VALUE                                    
007294         "000000000000000000000000000".                           
007296     10 FILLER PIC X(54) VALUE                                    
007298         "486476466457447438428419409400391382372363354345336328".
007300     10 FILLER PIC X(54) VALUE                                    
007302         "319310302293285277269261253246238231224217210203197191".
007304     10 FILLER PIC X(54) VALUE                                    
007306         "185180175170165160156152149000000000000000000000000000".
007308     10 FILLER PIC X(54) VALUE                                    
007310         "000000000000000000000000000000000000000000000000000000".
007312     10 FILLER PIC X(27) VALUE                                    
007314         "000000000000000000000000000".                           
007316     10 FILLER PIC X(54) VALUE                                    
007318         "486476466457447438428419409400391381372363354345336327".
007320     10 FILLER PIC X(54) VALUE                                    
007322         "318310301293284276268260252244237229222215208201195189".
007324     10 FILLER PIC X(54) VALUE                                    
007326         "183177172167162157153149145000000000000000000000000000".
007328     10 FILLER PIC X(54) VALUE                                    
007330         "000000000000000000000000000000000000000000000000000000".
007332     10 FILLER PIC X(27) VALUE                                    
007334         "000000000000000000000000000".                           
007336     10 FILLER PIC X(54) VALUE                                    
007338         "485476466457447437428418409400390381372363354345336327".
007340     10 FILLER PIC X(54) VALUE                                    
007342         "318309301292284275267259251243236228221213206200193187".
007344     10 FILLER PIC X(54) VALUE                                    
007346         "181175169164159154150145141138134131128126123121119117".
007348     10 FILLER PIC X(54) VALUE                                    
007350         "115000000000000000000000000000000000000000000000000000".
007352     10 FILLER PIC X(27) VALUE                                    
007354         "000000000000000000000000000".                           
007356     10 FILLER PIC X(54) VALUE                                    
007358         "485476466457447437428418409399390381372362353344335326".
007360     10 FILLER PIC X(54) VALUE                                    
007362         "318309300292283275266258250242234227219212205198191185".
007364     10 FILLER PIC X(54) VALUE                                    
007366         "179173167162156151147142138134131127124122119117114113".
007368     10 FILLER PIC X(54) VALUE                                    
007370         "111000000000000000000000000000000000000000000000000000".
007372     10 FILLER PIC X(27) VALUE                                    
007374         "000000000000000000000000000".                           
007376     10 FILLER PIC X(54) VALUE                                    
007378         "485476466456447437428418409399390381371362353344335326".
007380     10 FILLER PIC X(54) VALUE                                    
007382         "317308300291283274266285249241234226218211204197190183".
007384     10 FILLER PIC X(54) VALUE                                    
007386         "177171165159154149144139135131127124121118115113110108".
007388     10 FILLER PIC X(54) VALUE                                    
007390         "106000000000000000000000000000000000000000000000000000".
007392     10 FILLER PIC X(27) VALUE                                    
007394         "000000000000000000000000000".                           
007396     10 FILLER PIC X(54) VALUE                                    
007398         "485476466456447437428418409399390380371362353344335326".
007400     10 FILLER PIC X(54) VALUE                                    
007402         "317308299291282274265257249241233225217210202195188182".
007404     10 FILLER PIC X(54) VALUE                                    
007406         "175169163157152147142137132128124121117114111109106104".
007408     10 FILLER PIC X(54) VALUE                                    
007410         "102000000000000000000000000000000000000000000000000000".
007412     10 FILLER PIC X(27) VALUE                                    
007414         "000000000000000000000000000".                           
007416     10 FILLER PIC X(54) VALUE                                    
007418         "485476466456447437427418408399390380371362353343334325".
007420     10 FILLER PIC X(54) VALUE                                    
007422         "317308299290282273265256248240232224216209201194187180".
007424     10 FILLER PIC X(54) VALUE                                    
007426         "174167161155150144139134130126122118114111108105103101".
007428     10 FILLER PIC X(54) VALUE                                    
007430         "099000000000000000000000000000000000000000000000000000".
007432     10 FILLER PIC X(27) VALUE                                    
007434         "000000000000000000000000000".                           
007436     10 FILLER PIC X(54) VALUE                                    
007438         "485475466456447437427418408399389380371362352343334325".
007440     10 FILLER PIC X(54) VALUE                                    
007442         "316307299290281273264256248239231223216208201193186179".
007444     10 FILLER PIC X(54) VALUE                                    
007446         "173166160154148143137132128123119115111108105102099097".
007448     10 FILLER PIC X(54) VALUE                                    
007450         "095000000000000000000000000000000000000000000000000000".
007452     10 FILLER PIC X(27) VALUE                                    
007454         "000000000000000000000000000".                           
007456     10 FILLER PIC X(54) VALUE                                    
007458         "485475466456446437427418408399389380371361352343334325".
007460     10 FILLER PIC X(54) VALUE                                    
007462         "316307298290281272264255247239231223215207200192185178".
007464     10 FILLER PIC X(54) VALUE                                    
007466         "171165158152146141135130125121117113109105102099096094".
007468     10 FILLER PIC X(54) VALUE                                    
007470         "092000000000000000000000000000000000000000000000000000".
007472     10 FILLER PIC X(27) VALUE                                    
007474         "000000000000000000000000000".                           
007476     10 FILLER PIC X(54) VALUE                                    
007478         "485475466456446437427418408399389380370361352343334325".
007480     10 FILLER PIC X(54) VALUE                                    
007482         "316307298289281272264255247238230222214207199192184177".
007484     10 FILLER PIC X(54) VALUE                                    
007486         "170164157151145139134129124119114110106103099096094091".
007488     10 FILLER PIC X(54) VALUE                                    
007490         "089000000000000000000000000000000000000000000000000000".
007492     10 FILLER PIC X(27) VALUE                                    
007494         "000000000000000000000000000".                           
007496     10 FILLER PIC X(54) VALUE                                    
007498         "485475466456446437427418408399389380370361352343334325".
007500     10 FILLER PIC X(54) VALUE                                    
007502         "316307298289280272263255246238230222214206198191183176".
007504     10 FILLER PIC X(54) VALUE                                    
007506         "169163156150144138132127122117113108104101097094091088".
007508     10 FILLER PIC X(54) VALUE                                    
007510         "086000000000000000000000000000000000000000000000000000".
007512     10 FILLER PIC X(27) VALUE                                    
007514         "000000000000000000000000000".                           
007516     10 FILLER PIC X(54) VALUE                                    
007518         "485475466456446437427417408398389380370361352343333324".
007520     10 FILLER PIC X(54) VALUE                                    
007522         "315307298289280272263254246238229221213205198190183176".
007524     10 FILLER PIC X(54) VALUE                                    
007526         "169162155149143137131126120115111106102099095092089086".
007528     10 FILLER PIC X(54) VALUE                                    
007530         "083000000000000000000000000000000000000000000000000000".
007532     10 FILLER PIC X(27) VALUE                                    
007534         "000000000000000000000000000".                           
007536     10 FILLER PIC X(54) VALUE                                    
007538         "485475466456446437427417408398389380370361352342333324".
007540     10 FILLER PIC X(54) VALUE                                    
007542         "315306298289280271263254246237229221213205197190182175".
007544     10 FILLER PIC X(54) VALUE                                    
007546         "168161154148142136130124119114109105101097093090086083".
007548     10 FILLER PIC X(54) VALUE                                    
007550         "081078076074072071069068066065064000000000000000000000".
007552     10 FILLER PIC X(27) VALUE                                    
007554         "000000000000000000000000000".                           
007556     10 FILLER PIC X(54) VALUE                                    
007558         "485475466456446437427417408398389379370361352342333324".
007560     10 FILLER PIC X(54) VALUE                                    
007562         "315306297289280271263254245237229221213205197189182174".
007564     10 FILLER PIC X(54) VALUE                                    
007566         "167160154147141135129123118113108103099095091088084081".
007568     10 FILLER PIC X(54) VALUE                                    
007570         "079076074072070068067065064063061000000000000000000000".
007572     10 FILLER PIC X(27) VALUE                                    
007574         "000000000000000000000000000".                           
007576     10 FILLER PIC X(54) VALUE                                    
007578         "485475466456446437427417408398389379370361351342333324".
007580     10 FILLER PIC X(54) VALUE                                    
007582         "315306297288280271262254245237229220212204196189181174".
007584     10 FILLER PIC X(54) VALUE                                    
007586         "167160153146140134128122117112107102098093090086083080".
007588     10 FILLER PIC X(54) VALUE                                    
007590         "077074072070068066064063061060059000000000000000000000".
007592     10 FILLER PIC X(27) VALUE                                    
007594         "000000000000000000000000000".                           
007596     10 FILLER PIC X(54) VALUE                                    
007598         "485475466456446437427417408398389379370361351342333324".
007600     10 FILLER PIC X(54) VALUE                                    
007602         "315306297288280271262254245237228220212204196188181173".
007604     10 FILLER PIC X(54) VALUE                                    
007606         "166159152146139133127121116111106101096092088085081078".
007608     10 FILLER PIC X(54) VALUE                                    
007610         "075072070068066064062061059058056000000000000000000000".
007612     10 FILLER PIC X(27) VALUE                                    
007614         "000000000000000000000000000".                           
007616     10 FILLER PIC X(54) VALUE                                    
007618         "485475466456446437427417408398389379370361351342333324".
007620     10 FILLER PIC X(54) VALUE                                    
007622         "315306297288279271262253245236228220212204196188180173".
007624     10 FILLER PIC X(54) VALUE                                    
007626         "166159152145139132126120115110105100095091087083080076".
007628     10 FILLER PIC X(54) VALUE                                    
007630         "073071068066064062060059057056054000000000000000000000".
007632     10 FILLER PIC X(27) VALUE                                    
007634         "000000000000000000000000000".                           
007636     10 FILLER PIC X(54) VALUE                                    
007638         "485475465456446436427417408398389379370361351342333324".
007640     10 FILLER PIC X(54) VALUE                                    
007642         "315306297288279271262253245236228220211203196188180173".
007644     10 FILLER PIC X(54) VALUE                                    
007646         "165158151145138132126120114109104099094090086082078075".
007648     10 FILLER PIC X(54) VALUE                                    
007650         "072069067064062060058057055054052000000000000000000000".
007652     10 FILLER PIC X(27) VALUE                                    
007654         "000000000000000000000000000".                           
007656     10 FILLER PIC X(54) VALUE                                    
007658         "485475465456446436427417408398389379370361351342333324".
007660     10 FILLER PIC X(54) VALUE                                    
007662         "315306297288279270262253245236228219211203195188180172".
007664     10 FILLER PIC X(54) VALUE                                    
007666         "165158151144138131125119113108103098093089085081077074".
007668     10 FILLER PIC X(54) VALUE                                    
007670         "071068065063061059057055053052050000000000000000000000".
007672     10 FILLER PIC X(27) VALUE                                    
007674         "000000000000000000000000000".                           
007676     10 FILLER PIC X(54) VALUE                                    
007678         "485475465456446436427417408398389379370361351342333324".
007680     10 FILLER PIC X(54) VALUE                                    
007682         "315306297288279270262253245236228219211203195187180172".
007684     10 FILLER PIC X(54) VALUE                                    
007686         "165158151144137131125119113107102097092088084080076073".
007688     10 FILLER PIC X(54) VALUE                                    
007690         "069066064061059057055053052050049000000000000000000000".
007692     10 FILLER PIC X(27) VALUE                                    
007694         "000000000000000000000000000".                           
007696     10 FILLER PIC X(54) VALUE                                    
007698         "485475465456446436427417408398389379370360351342333324".
007700     10 FILLER PIC X(54) VALUE                                    
007702         "315306297288279270262253244236228219211203195187179172".
007704     10 FILLER PIC X(54) VALUE                                    
007706         "164157150143137130124118112107101096092087083079075071".
007708     10 FILLER PIC X(54) VALUE                                    
007710         "068065063060058056054052050048047000000000000000000000".
007712     10 FILLER PIC X(27) VALUE                                    
007714         "000000000000000000000000000".                           
007716     10 FILLER PIC X(54) VALUE                                    
007718         "485475465456446436427417408398389379370360351342333324".
007720     10 FILLER PIC X(54) VALUE                                    
007722         "315306297288279270262253244236227219211203195187179172".
007724     10 FILLER PIC X(54) VALUE                                    
007726         "164157150143136130124118112106101096091086082078074070".
007728     10 FILLER PIC X(54) VALUE                                    
007730         "067064061059056054052050049047045000000000000000000000".
007732     10 FILLER PIC X(27) VALUE                                    
007734         "000000000000000000000000000".                           
007736     10 FILLER PIC X(54) VALUE                                    
007738         "485475465456446436427417408398389379370360351342333324".
007740     10 FILLER PIC X(54) VALUE                                    
007742         "315306297288279270261253244236227219211203195187179171".
007744     10 FILLER PIC X(54) VALUE                                    
007746         "164157150143136129123117111106100095090085081077073069".
007748     10 FILLER PIC X(54) VALUE                                    
007750         "066063060058055053051049047045044042041039038037035034".
007752     10 FILLER PIC X(27) VALUE                                    
007754         "033033032000000000000000000".                           
007756     10 FILLER PIC X(54) VALUE                                    
007758         "485475465456446436427417408398389379370360351342333324".
007760     10 FILLER PIC X(54) VALUE                                    
007762         "315306297288279270261253244236227219211202194187179171".
007764     10 FILLER PIC X(54) VALUE                                    
007766         "164156149142136129123117111105100094090085080076072069".
007768     10 FILLER PIC X(54) VALUE                                    
007770         "065062059056054052050048046044042041039037036035034032".
007772     10 FILLER PIC X(27) VALUE                                    
007774         "031031030000000000000000000".                           
007776     10 FILLER PIC X(54) VALUE                                    
007778         "485475465456446436427417408398389379370360351342333324".
007780     10 FILLER PIC X(54) VALUE                                    
007782         "314305297288279270261253244236227219211202194186179171".
007784     10 FILLER PIC X(54) VALUE                                    
007786         "164156149142135129122116110105099094089084080075071068".
007788     10 FILLER PIC X(54) VALUE                                    
007790         "064061058055053051048046044043041039037036034033032031".
007792     10 FILLER PIC X(27) VALUE                                    
007794         "030029028000000000000000000".                           
007796     10 FILLER PIC X(54) VALUE                                    
007798         "485475465456446436427417408398389379370360351342333324".
007800     10 FILLER PIC X(54) VALUE                                    
007802         "314305297288279270261253244236227219210202194186179171".
007804     10 FILLER PIC X(54) VALUE                                    
007806         "163156149142135129122116110104099094088084079075071067".
007808     10 FILLER PIC X(54) VALUE                                    
007810         "063060057054052050047045043041040038036034033032030029".
007812     10 FILLER PIC X(27) VALUE                                    
007814         "028027026000000000000000000".                           
007816     10 FILLER PIC X(54) VALUE                                    
007818         "485475465456446436427417408398388379370360351342333324".
007820     10 FILLER PIC X(54) VALUE                                    
007822         "314305296288279270261253244235227219210202194186178171".
007824     10 FILLER PIC X(54) VALUE                                    
007826         "163156149142135128122116110104098093088083079074070066".
007828     10 FILLER PIC X(54) VALUE                                    
007830         "063059056054051049046044042040038037035033032030029027".
007832     10 FILLER PIC X(27) VALUE                                    
007834         "026025024000000000000000000".                           
007836     10 FILLER PIC X(54) VALUE                                    
007838         "485475465456446436427417408398388379370360351342333323".
007840     10 FILLER PIC X(54) VALUE                                    
007842         "314305296288279270261253244235227219210202194186178171".
007844     10 FILLER PIC X(54) VALUE                                    
007846         "163156149142135128122115109104098093088083078074070066".
007848     10 FILLER PIC X(54) VALUE                                    
007850         "062059056053050048045043041039037035034032030029027026".
007852     10 FILLER PIC X(27) VALUE                                    
007854         "025024023000000000000000000".                           
007856     10 FILLER PIC X(54) VALUE                                    
007858         "485475465456446436427417408398388379370360351342333323".
007860     10 FILLER PIC X(54) VALUE                                    
007862         "315305296288279270261253244235227219210202194186178171".
007864     10 FILLER PIC X(54) VALUE                                    
007866         "163156148141135128122115109103098092087082078073069065".
007868     10 FILLER PIC X(54) VALUE                                    
007870         "062058055052049047045042040038036034032031029027026024".
007872     10 FILLER PIC X(27) VALUE                                    
007874         "023022021000000000000000000".                           
007876     10 FILLER PIC X(54) VALUE                                    
007878         "485475465456446436427417408398388379370360351342333323".
007880     10 FILLER PIC X(54) VALUE                                    
007882         "314305296288279270261252244235227218210202194186178170".
007884     10 FILLER PIC X(54) VALUE                                    
007886         "163156148141134128121115109103098092087082077073069065".
007888     10 FILLER PIC X(54) VALUE                                    
007890         "061058054051049046044042039037035033031030028026025023".
007892     10 FILLER PIC X(27) VALUE                                    
007894         "022021020000000000000000000".                           
007896     10 FILLER PIC X(54) VALUE                                    
007898         "485475465456446436427417408398388379370360351342333323".
007900     10 FILLER PIC X(54) VALUE                                    
007902         "314305296288279270261252244235227218210202194186178170".
007904     10 FILLER PIC X(54) VALUE                                    
007906         "163155148141134128121115109103097092087082077073068064".
007908     10 FILLER PIC X(54) VALUE                                    
007910         "061057054051048046043041039037035033031029027025024022".
007912     10 FILLER PIC X(27) VALUE                                    
007914         "021019018000000000000000000".                           
007916     10 FILLER PIC X(54) VALUE                                    
007918         "485475465456446436427417407398388379370360351342333323".
007920     10 FILLER PIC X(54) VALUE                                    
007922         "314305296287279270261252244235227218210202194186178170".
007924     10 FILLER PIC X(54) VALUE                                    
007926         "163155148141134128121115109103097092087082077072068064".
007928     10 FILLER PIC X(54) VALUE                                    
007930         "060057053050048045043040038036034032030028026024023021".
007932     10 FILLER PIC X(27) VALUE                                    
007934         "020018017000000000000000000".                           
007936     10 FILLER PIC X(54) VALUE                                    
007938         "485475465456446436427417407398388379370360351342333323".
007940     10 FILLER PIC X(54) VALUE                                    
007942         "314305296287279270261252244235227218210202194186178170".
007944     10 FILLER PIC X(54) VALUE                                    
007946         "163155148141134127121115109103097092086081077072068064".
007948     10 FILLER PIC X(54) VALUE                                    
007950         "060056053050047045042040038035033031029027025023022020".
007952     10 FILLER PIC X(27) VALUE                                    
007954         "019017016015014013012011011".                           
007956     10 FILLER PIC X(54) VALUE                                    
007958         "485475465456446436427417407398388379370360351342333323".
007960     10 FILLER PIC X(54) VALUE                                    
007962         "314305296287279270261252244235227218210202194186178170".
007964     10 FILLER PIC X(54) VALUE                                    
007966         "163155148141134127121115108103097091086081076072068063".
007968     10 FILLER PIC X(54) VALUE                                    
007970         "060056053050047044042039037035033031029027025023021019".
007972     10 FILLER PIC X(27) VALUE                                    
007974         "018016015014012011011010010".                           
007976     10 FILLER PIC X(54) VALUE                                    
007978         "485475465456446436427417407398388379370360351342333323".
007980     10 FILLER PIC X(54) VALUE                                    
007982         "314305296287279270261252244235227218210202194186178170".
007984     10 FILLER PIC X(54) VALUE                                    
007986         "163155148141134127121115108102097091086081076072067063".
007988     10 FILLER PIC X(54) VALUE                                    
007990         "059056053049047044041039037035032030028026024022020019".
007992     10 FILLER PIC X(27) VALUE                                    
007994         "017015014013011010010010010".                           
007996     10 FILLER PIC X(54) VALUE                                    
007998         "485475465456446436427417407398388379370360351342333323".
008000     10 FILLER PIC X(54) VALUE                                    
008002         "314305296287279270261252244235227218210202194186178170".
008004     10 FILLER PIC X(54) VALUE                                    
008006         "163155148141134127121114108102097091086081076072067063".
008008     10 FILLER PIC X(54) VALUE                                    
008010         "059056052049046044041039036034032030028026024022020018".
008012     10 FILLER PIC X(27) VALUE                                    
008014         "016015013012011010010010010".                           
008016     10 FILLER PIC X(54) VALUE                                    
008018         "485475465456446436427417407398388379370360351342333323".
008020     10 FILLER PIC X(54) VALUE                                    
008022         "314305296287279270261252244235227218210202194186178170".
008024     10 FILLER PIC X(54) VALUE                                    
008026         "163155148141134127121114108102097091086081076071067063".
008028     10 FILLER PIC X(54) VALUE                                    
008030         "059056052049046043041039036034032030027025023021019018".
008032     10 FILLER PIC X(27) VALUE                                    
008034         "016014013011010010010010010".                           
008036     10 FILLER PIC X(54) VALUE                                    
008038         "485475465456446436427417407398388379370360351342333323".
008040     10 FILLER PIC X(54) VALUE                                    
008042         "314305296287279270261252244235227218210202194186178170".
008044     10 FILLER PIC X(54) VALUE                                    
008046         "163155148141134127121114108102097091086081076071067063".
008048     10 FILLER PIC X(54) VALUE                                    
008050         "059055052049046043041038036034031029027025023021019017".
008052     10 FILLER PIC X(27) VALUE                                    
008054         "015014012011010010010010010".                           
008056                                                                  
008058   05  WS-RMD-LEF-TABLE-2 REDEFINES RMD-LEF-TABLE-2.              
008060       10  WS-RMD-LEF-TBL-2-REC OCCURS 81 TIMES.                  
008062           15  WS-RMD-TBL2-LEF  PIC 999 OCCURS 81 TIMES.          
008064                                                                  
```

⚠️  This is the source code you must document.
    817 lines from 3212 to 4028.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

