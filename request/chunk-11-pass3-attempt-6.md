# LLM Request Debug File
Generated: 2025-11-18T16:54:16.570848

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 11/55
- **Model**: gpt-4.1
- **Chunk Number**: 11
- **Pass Number**: 3
- **Attempt Number**: 6 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,086 tokens
- **User Prompt**: ~33,803 tokens
- **Total Input**: ~35,889 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 11/55" (ID: detailed-code-explanation)

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


**CHUNK 11 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T16:24:14.514603", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 11 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 4062 to 5762 (1,701 lines)\nChunk Tokens (estimated): ~31,847\nActual Input Tokens: 33,253 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 4062-5762 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 11 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 11 of 55.\n\n\n=============================================================================\nCHUNK 11 SOURCE CODE (Lines 4062-5762)\n=============================================================================\n\n```cobol\n008132 01  RMD-LEF-TABLE-2-2022-X.                                      \n008134   05  RMD-LEF-TABLE-2-2022.                                      \n008136     10 FILLER PIC X(54) VALUE                                    \n008138         \"919914910905901897894890887884882879877875873871869868\".\n008140     10 FILLER PIC X(54) VALUE                                    \n008142         \"866865864862861860859859858857856856855854854853853853\".\n008144     10 FILLER PIC X(54) VALUE                                    \n008146         \"852852852851851851850850850850849849849849849848848848\".\n008148     10 FILLER PIC X(54) VALUE                                    \n008150         \"848848848848848847847847847847847847847847847847847847\".\n008152     10 FILLER PIC X(54) VALUE                                    \n008154         \"847846846846846846846846846846846846846846846846846846\".\n008156     10 FILLER PIC X(54) VALUE                                    \n008158         \"846846846846846846846846846846846846846846846846846846\".\n008160     10 FILLER PIC X(39) VALUE                                    \n008162         \"846846846846846846846846846846846846846\".               \n008164     10 FILLER PIC X(54) VALUE                                    \n008166         \"914909904900895891888884881878875872870867865863861860\".\n008168     10 FILLER PIC X(54) VALUE                                    \n008170         \"858857855854853852851850849848847847846846845845844844\".\n008172     10 FILLER PIC X(54) VALUE                                    \n008174         \"843843843842842842841841841841840840840840840840839839\".\n008176     10 FILLER PIC X(54) VALUE                                    \n008178         \"839839839839839839838838838838838838838838838838838838\".\n008180     10 FILLER PIC X(54) VALUE                                    \n008182         \"838838838838838838838838838838838837837837837837837837\".\n008184     10 FILLER PIC X(54) VALUE                                    \n008186         \"837837837837837837837837837837837837837837837837837837\".\n008188     10 FILLER PIC X(39) VALUE                                    \n008190         \"837837837837837837837837837837837837837\".               \n008192     10 FILLER PIC X(54) VALUE                                    \n008194         \"910904899894890885881878874871868865862860857855853851\".\n008196     10 FILLER PIC X(54) VALUE                                    \n008198         \"850848847845844843842841840839838838837836836835835834\".\n008200     10 FILLER PIC X(54) VALUE                                    \n008202         \"834833833833832832832831831831831831830830830830830830\".\n008204     10 FILLER PIC X(54) VALUE                                    \n008206         \"829829829829829829829829829829828828828828828828828828\".\n008208     10 FILLER PIC X(54) VALUE                                    \n008210         \"828828828828828828828828828828828828828828828828828828\".\n008212     10 FILLER PIC X(54) VALUE                                    \n008214         \"828828828828828828828828828828828828828828828828828828\".\n008216     10 FILLER PIC X(39) VALUE                                    \n008218         \"828828828828828828828828828828828828828\".               \n008220     10 FILLER PIC X(54) VALUE                                    \n008222         \"905900894889884880876871868864861858855852850847845843\".\n008224     10 FILLER PIC X(54) VALUE                                    \n008226         \"841840838837835834833832831830829828828827826826825825\".\n008228     10 FILLER PIC X(54) VALUE                                    \n008230         \"824824823823823822822822822821821821821821820820820820\".\n008232     10 FILLER PIC X(54) VALUE                                    \n008234         \"820820819819819819819819819819819819819819818818818818\".\n008236     10 FILLER PIC X(54) VALUE                                    \n008238         \"818818818818818818818818818818818818818818818818818818\".\n008240     10 FILLER PIC X(54) VALUE                                    \n008242         \"818818818818818818818818818818818818818818818818818818\".\n008244     10 FILLER PIC X(39) VALUE                                    \n008246         \"818818818818818818818818818818818818818\".               \n008248     10 FILLER PIC X(54) VALUE                                    \n008250         \"901895890884879874870866862858854851848845842840837835\".\n008252     10 FILLER PIC X(54) VALUE                                    \n008254         \"833831830828827825824823822821820819818818817816816815\".\n008256     10 FILLER PIC X(54) VALUE                                    \n008258         \"815814814814813813813812812812811811811811811810810810\".\n008260     10 FILLER PIC X(54) VALUE                                    \n008262         \"810810810810809809809809809809809809809809809809809808\".\n008264     10 FILLER PIC X(54) VALUE                                    \n008266         \"809808808808808808808808808808808808808808808808808808\".\n008268     10 FILLER PIC X(54) VALUE                                    \n008270         \"808808808808808808808808808808808808808808808808808808\".\n008272     10 FILLER PIC X(39) VALUE                                    \n008274         \"808808808808808808808808808808808808808\".               \n008276     10 FILLER PIC X(54) VALUE                                    \n008278         \"897891886880874869865860856852848844841838835832830827\".\n008280     10 FILLER PIC X(54) VALUE                                    \n008282         \"825823822820818817816814813812811810809809808807807806\".\n008284     10 FILLER PIC X(54) VALUE                                    \n008286         \"805805804804804803803803802802802802801801801801801800\".\n008288     10 FILLER PIC X(54) VALUE                                    \n008290         \"800800800800800800799799799799799799799799799799799798\".\n008292     10 FILLER PIC X(54) VALUE                                    \n008294         \"799799799799799798798798798798798798798798798798798798\".\n008296     10 FILLER PIC X(54) VALUE                                    \n008298         \"798798798798798798798798798798798798798798798798798798\".\n008300     10 FILLER PIC X(39) VALUE                                    \n008302         \"798798798798798798798798798798798798798\".               \n008304     10 FILLER PIC X(54) VALUE                                    \n008306         \"894888881876870865859855850846842838834831828825822820\".\n008308     10 FILLER PIC X(54) VALUE                                    \n008310         \"817815813812810808807806804803802801800799799798797797\".\n008312     10 FILLER PIC X(54) VALUE                                    \n008314         \"796795795795794794793793793792792792792791791791791791\".\n008316     10 FILLER PIC X(54) VALUE                                    \n008318         \"790790790790790790790790789789789789789789789789789789\".\n008320     10 FILLER PIC X(54) VALUE                                    \n008322         \"789789789789789789789789789789789789789788788788788788\".\n008324     10 FILLER PIC X(54) VALUE                                    \n008326         \"788788788788788788788788788788788788788788788788788788\".\n008328     10 FILLER PIC X(39) VALUE                                    \n008330         \"788788788788788788788788788788788788788\".               \n008332     10 FILLER PIC X(54) VALUE                                    \n008334         \"890884878871866860855849845840836832828824821818815812\".\n008336     10 FILLER PIC X(54) VALUE                                    \n008338         \"810807805803802800798797796794793792791790789789788787\".\n008340     10 FILLER PIC X(54) VALUE                                    \n008342         \"787786786785785784784783783783782782782782781781781781\".\n008344     10 FILLER PIC X(54) VALUE                                    \n008346         \"781781780780780780780780780780779779779779779779779779\".\n008348     10 FILLER PIC X(54) VALUE                                    \n008350         \"779779779779779779779779779779779779779779779779779779\".\n008352     10 FILLER PIC X(54) VALUE                                    \n008354         \"779779779779779779779779779779779779779779779779779779\".\n008356     10 FILLER PIC X(39) VALUE                                    \n008358         \"779779779779779779779779779779779779779\".               \n008360     10 FILLER PIC X(54) VALUE                                    \n008362         \"887881874868862856850845839835830826822818814811808805\".\n008364     10 FILLER PIC X(54) VALUE                                    \n008366         \"802800798795793792790788787786784783782781780779779778\".\n008368     10 FILLER PIC X(54) VALUE                                    \n008370         \"777777776776775775774774773773773773772772772772771771\".\n008372     10 FILLER PIC X(54) VALUE                                    \n008374         \"771771771770770770770770770770770770769769769769769769\".\n008376     10 FILLER PIC X(54) VALUE                                    \n008378         \"769769769769769769769769769769769769769769769769769769\".\n008380     10 FILLER PIC X(54) VALUE                                    \n008382         \"769769769769769769769769769769769769769769769769769769\".\n008384     10 FILLER PIC X(39) VALUE                                    \n008386         \"769769769769769769769769769769769769769\".               \n008388     10 FILLER PIC X(54) VALUE                                    \n008390         \"884878871864858852846840835829825820816812808804801798\".\n008392     10 FILLER PIC X(54) VALUE                                    \n008394         \"795792790788785783782780778777776774773772771770770769\".\n008396     10 FILLER PIC X(54) VALUE                                    \n008398         \"768767767766766765765764764764763763763762762762762761\".\n008400     10 FILLER PIC X(54) VALUE                                    \n008402         \"761761761761761760760760760760760760760760759759759759\".\n008404     10 FILLER PIC X(54) VALUE                                    \n008406         \"759759759759759759759759759759759759759759759759759759\".\n008408     10 FILLER PIC X(54) VALUE                                    \n008410         \"759759759759759759759759759759759759759759759759759759\".\n008412     10 FILLER PIC X(39) VALUE                                    \n008414         \"759759759759759759759759759759759759759\".               \n008416     10 FILLER PIC X(54) VALUE                                    \n008418         \"882875868861854848842836830825819815810806802798794791\".\n008420     10 FILLER PIC X(54) VALUE                                    \n008422         \"788785782780778775773772770768767766764763762761760760\".\n008424     10 FILLER PIC X(54) VALUE                                    \n008426         \"759758757757756756755755754754754753753753752752752752\".\n008428     10 FILLER PIC X(54) VALUE                                    \n008430         \"751751751751751751750750750750750750750750750750749749\".\n008432     10 FILLER PIC X(54) VALUE                                    \n008434         \"749749749749749749749749749749749749749749749749749749\".\n008436     10 FILLER PIC X(54) VALUE                                    \n008438         \"749749749749749749749749749749749749749749749749749749\".\n008440     10 FILLER PIC X(39) VALUE                                    \n008442         \"749749749749749749749749749749749749749\".               \n008444     10 FILLER PIC X(54) VALUE                                    \n008446         \"879872865858851844838832826820815809805800796792788784\".\n008448     10 FILLER PIC X(54) VALUE                                    \n008450         \"781778775772770468765764762760758757756755753752751750\".\n008452     10 FILLER PIC X(54) VALUE                                    \n008454         \"750749748747747746746745745744744744743743743742742742\".\n008456     10 FILLER PIC X(54) VALUE                                    \n008458         \"742742741741741741741741740740740740740740740740740740\".\n008460     10 FILLER PIC X(54) VALUE                                    \n008462         \"739739739739739739739739739739739739739739739739739739\".\n008464     10 FILLER PIC X(54) VALUE                                    \n008466         \"739739739739739739739739739739739739739739739739739739\".\n008468     10 FILLER PIC X(39) VALUE                                    \n008470         \"739739739739739739739739739739739739739\".               \n008472     10 FILLER PIC X(54) VALUE                                    \n008474         \"877870862855848841834828822816810805799795790786782778\".\n008476     10 FILLER PIC X(54) VALUE                                    \n008478         \"774771768765762760758756754752750749747746745743742741\".\n008480     10 FILLER PIC X(54) VALUE                                    \n008482         \"740740739738737737736736735735734734734733733733732732\".\n008484     10 FILLER PIC X(54) VALUE                                    \n008486         \"732732732731731731731731731730730730730730730730730730\".\n008488     10 FILLER PIC X(54) VALUE                                    \n008490         \"730730730729729729729729729729729729729729729729729729\".\n008492     10 FILLER PIC X(54) VALUE                                    \n008494         \"729729729729729729729729729729729729729729729729729729\".\n008496     10 FILLER PIC X(39) VALUE                                    \n008498         \"729729729729729729729729729729729729729\".               \n008500     10 FILLER PIC X(54) VALUE                                    \n008502         \"875867860852845838831824818812806800795790785780776772\".\n008504     10 FILLER PIC X(54) VALUE                                    \n008506         \"768764761758755752750748746744742740739737736735733732\".\n008508     10 FILLER PIC X(54) VALUE                                    \n008510         \"731731730729728728727726726725725724724724723723723723\".\n008512     10 FILLER PIC X(54) VALUE                                    \n008514         \"722722722722721721721721721721721720720720720720720720\".\n008516     10 FILLER PIC X(54) VALUE                                    \n008518         \"720720720720720720719719719719719719719719719719719719\".\n008520     10 FILLER PIC X(54) VALUE                                    \n008522         \"719719719719719719719719719719719719719719719719719719\".\n008524     10 FILLER PIC X(39) VALUE                                    \n008526         \"719719719719719719719719719719719719719\".               \n008528     10 FILLER PIC X(54) VALUE                                    \n008530         \"873865857850842835828821814808802796790785780775770766\".\n008532     10 FILLER PIC X(54) VALUE                                    \n008534         \"762758754751748745742740738736734732730729727726725724\".\n008536     10 FILLER PIC X(54) VALUE                                    \n008538         \"722721721720719718718717716716715715715714714713713713\".\n008540     10 FILLER PIC X(54) VALUE                                    \n008542         \"713712712712712712711711711711711711711710710710710710\".\n008544     10 FILLER PIC X(54) VALUE                                    \n008546         \"710710710710710710710710710710709709709709709709709709\".\n008548     10 FILLER PIC X(54) VALUE                                    \n008550         \"709709709709709709709709709709709709709709709709709709\".\n008552     10 FILLER PIC X(39) VALUE                                    \n008554         \"709709709709709709709709709709709709709\".               \n008556     10 FILLER PIC X(54) VALUE                                    \n008558         \"871863855847840832825818811804798792786780775770765760\".\n008560     10 FILLER PIC X(54) VALUE                                    \n008562         \"756752748744741738735733730728726724722720719717716715\".\n008564     10 FILLER PIC X(54) VALUE                                    \n008566         \"714713712711710709708708707706706705705705704704704703\".\n008568     10 FILLER PIC X(54) VALUE                                    \n008570         \"703703702702702702702701701701701701701701701700700700\".\n008572     10 FILLER PIC X(54) VALUE                                    \n008574         \"700700700700700700700700700700700700700700700700699699\".\n008576     10 FILLER PIC X(54) VALUE                                    \n008578         \"699699699699699699699699699699699699699699699699699699\".\n008580     10 FILLER PIC X(39) VALUE                                    \n008582         \"699699699699699699699699699699699699699\".               \n008584     10 FILLER PIC X(54) VALUE                                    \n008586         \"869861853845837830822815808801794788782776770765760755\".\n008588     10 FILLER PIC X(54) VALUE                                    \n008590         \"750746742738734731728725723720718716714712710709707706\".\n008592     10 FILLER PIC X(54) VALUE                                    \n008594         \"705704703702701700699698698697697696696695695694694694\".\n008596     10 FILLER PIC X(54) VALUE                                    \n008598         \"693693693693692692692692692691691691691691691691691690\".\n008600     10 FILLER PIC X(54) VALUE                                    \n008602         \"690690690690690690690690690690690690690690690690690690\".\n008604     10 FILLER PIC X(54) VALUE                                    \n008606         \"690690690690690690690690690690690690690690690690690690\".\n008608     10 FILLER PIC X(39) VALUE                                    \n008610         \"689689689689689689689689689690690690690\".               \n008612     10 FILLER PIC X(54) VALUE                                    \n008614         \"868860851843835827820812805798791784778772766760755750\".\n008616     10 FILLER PIC X(54) VALUE                                    \n008618         \"745740736732728725721718715713710708706704702700699697\".\n008620     10 FILLER PIC X(54) VALUE                                    \n008622         \"696695694693692691690689688688687687686686685685684684\".\n008624     10 FILLER PIC X(54) VALUE                                    \n008626         \"684683683683683682682682682682682681681681681681681681\".\n008628     10 FILLER PIC X(54) VALUE                                    \n008630         \"681681680680680680680680680680680680680680680680680680\".\n008632     10 FILLER PIC X(54) VALUE                                    \n008634         \"680680680680680680680680680680680680680680680680680680\".\n008636     10 FILLER PIC X(39) VALUE                                    \n008638         \"680680680680680680680680680680680680680\".               \n008640     10 FILLER PIC X(54) VALUE                                    \n008642         \"866858850841833825817810802795788781774768762756750745\".\n008644     10 FILLER PIC X(54) VALUE                                    \n008646         \"740735730726722718715711708705703700698696694692690689\".\n008648     10 FILLER PIC X(54) VALUE                                    \n008650         \"687686685684683682681680679679678677677676676675675674\".\n008652     10 FILLER PIC X(54) VALUE                                    \n008654         \"674674674673673673673672672672672672672671671671671671\".\n008656     10 FILLER PIC X(54) VALUE                                    \n008658         \"671671671671671670670670670670670670670670670670670670\".\n008660     10 FILLER PIC X(54) VALUE                                    \n008662         \"670670670670670670670670670670670670670670670670670670\".\n008664     10 FILLER PIC X(39) VALUE                                    \n008666         \"670670670670670670670670670670670670670\".               \n008668     10 FILLER PIC X(54) VALUE                                    \n008670         \"865857848840831823815807800792785778771764758752746740\".\n008672     10 FILLER PIC X(54) VALUE                                    \n008674         \"735730725720716712708705701698695693690688686684682681\".\n008676     10 FILLER PIC X(54) VALUE                                    \n008678         \"679677676675674673672671670669669668667667666666665665\".\n008680     10 FILLER PIC X(54) VALUE                                    \n008682         \"665664664664663663663663662662662662662662662661661661\".\n008684     10 FILLER PIC X(54) VALUE                                    \n008686         \"661661661661661661661661661660660660660660660660660660\".\n008688     10 FILLER PIC X(54) VALUE                                    \n008690         \"660660660660660660660660660660660660660660660660660660\".\n008692     10 FILLER PIC X(39) VALUE                                    \n008694         \"660660660660660660660660660660660660660\".               \n008696     10 FILLER PIC X(54) VALUE                                    \n008698         \"864855847838830822813805798790782775768761754748742736\".\n008700     10 FILLER PIC X(54) VALUE                                    \n008702         \"730725715710706702698695694691688685683680678676674672\".\n008704     10 FILLER PIC X(54) VALUE                                    \n008706         \"671669668666665664663662661660659659658657657656656655\".\n008708     10 FILLER PIC X(54) VALUE                                    \n008710         \"655655654654654654653653653653652652652652652652652651\".\n008712     10 FILLER PIC X(54) VALUE                                    \n008714         \"651651651651651651651651651651651651651651651650650650\".\n008716     10 FILLER PIC X(54) VALUE                                    \n008718         \"650650650650650650650650650650650650650650650650650650\".\n008720     10 FILLER PIC X(39) VALUE                                    \n008722         \"650650650650650650650650650650650650650\".               \n008724     10 FILLER PIC X(54) VALUE                                    \n008726         \"862854845837828820812803795788780772765758751744738732\".\n008728     10 FILLER PIC X(54) VALUE                                    \n008730         \"726720715710705700696692688685681678675673670668666664\".\n008732     10 FILLER PIC X(54) VALUE                                    \n008734         \"662661659658656655654653652651650650649648648647647646\".\n008736     10 FILLER PIC X(54) VALUE                                    \n008738         \"646645645645644644644643643643643643642642642642642642\".\n008740     10 FILLER PIC X(54) VALUE                                    \n008742         \"642642641641641641641641641641641641641641641641641641\".\n008744     10 FILLER PIC X(54) VALUE                                    \n008746         \"641641641641641641641641641641641641641641641641641641\".\n008748     10 FILLER PIC X(39) VALUE                                    \n008750         \"641641641641641641641641641641641641641\".               \n008752     10 FILLER PIC X(54) VALUE                                    \n008754         \"861853844835827818810802793785778770762755748741734728\".\n008756     10 FILLER PIC X(54) VALUE                                    \n008758         \"722716710705700695690686682678675671668666663660658656\".\n008760     10 FILLER PIC X(54) VALUE                                    \n008762         \"654652651649648646645644643642641640640639638638637637\".\n008764     10 FILLER PIC X(54) VALUE                                    \n008766         \"636636635635635634634634634633633633633633632632632632\".\n008768     10 FILLER PIC X(54) VALUE                                    \n008770         \"632632632632632631631631631631631631631631631631631631\".\n008772     10 FILLER PIC X(54) VALUE                                    \n008774         \"631631631631631631631631631631631631631631631631631631\".\n008776     10 FILLER PIC X(39) VALUE                                    \n008778         \"631631631631631631631631631631631631631\".               \n008780     10 FILLER PIC X(54) VALUE                                    \n008782         \"860852843834825817808800792783775768760752745738731725\".\n008784     10 FILLER PIC X(54) VALUE                                    \n008786         \"718712706700695690685680676672668665662658655653651648\".\n008788     10 FILLER PIC X(54) VALUE                                    \n008790         \"646644642641639638636635634633632631630630629628628627\".\n008792     10 FILLER PIC X(54) VALUE                                    \n008794         \"627626626625625625624624624624623623623623623623622622\".\n008796     10 FILLER PIC X(54) VALUE                                    \n008798         \"622622622622622622622622621621621621621621621621621621\".\n008800     10 FILLER PIC X(54) VALUE                                    \n008802         \"621621621621621621621621621621621621621621621621621621\".\n008804     10 FILLER PIC X(39) VALUE                                    \n008806         \"621621621621621621621621621621621621621\".               \n008808     10 FILLER PIC X(54) VALUE                                    \n008810         \"859851842833824816807798790782773765758750742735728721\".\n008812     10 FILLER PIC X(54) VALUE                                    \n008814         \"715708702696690685680675671666662658655652649646643641\".\n008816     10 FILLER PIC X(54) VALUE                                    \n008818         \"638636634633631629628627625624623622621621620619619618\".\n008820     10 FILLER PIC X(54) VALUE                                    \n008822         \"617617616616616615615615614614614614613613613613613613\".\n008824     10 FILLER PIC X(54) VALUE                                    \n008826         \"613612612612612612612612612612612612612612611611611611\".\n008828     10 FILLER PIC X(54) VALUE                                    \n008830         \"611611611611611611611611611611611611611611611611611611\".\n008832     10 FILLER PIC X(39) VALUE                                    \n008834         \"611611611611611611611611611611611611611\".               \n008836     10 FILLER PIC X(54) VALUE                                    \n008838         \"859850841832823814806797788780772764756748740733725718\".\n008840     10 FILLER PIC X(54) VALUE                                    \n008842         \"711705698692686680675670665661656652649645642639636633\".\n008844     10 FILLER PIC X(54) VALUE                                    \n008846         \"631628626624623621619618617615614613612612611610609609\".\n008848     10 FILLER PIC X(54) VALUE                                    \n008850         \"608608607607606606605605605605604604604604603603603603\".\n008852     10 FILLER PIC X(54) VALUE                                    \n008854         \"603603603603602602602602602602602602602602602602602602\".\n008856     10 FILLER PIC X(54) VALUE                                    \n008858         \"602602602602602602602602602602602602602602602602602602\".\n008860     10 FILLER PIC X(39) VALUE                                    \n008862         \"602602602602602602602602602602602602602\".               \n008864     10 FILLER PIC X(54) VALUE                                    \n008866         \"858849840831822813804796787778770762754746738730723715\".\n008868     10 FILLER PIC X(54) VALUE                                    \n008870         \"708701695688682676671665660655651646642639635632629626\".\n008872     10 FILLER PIC X(54) VALUE                                    \n008874         \"623621619616615613611610608607606605603603602601600599\".\n008876     10 FILLER PIC X(54) VALUE                                    \n008878         \"599598598597597596596596595595595595594594594594594593\".\n008880     10 FILLER PIC X(54) VALUE                                    \n008882         \"593593593593593593593593592592592592592592592592592592\".\n008884     10 FILLER PIC X(54) VALUE                                    \n008886         \"592592592592592592592592592592592592592592592592592592\".\n008888     10 FILLER PIC X(39) VALUE                                    \n008890         \"592592592592592592592592592592592592592\".               \n008892     10 FILLER PIC X(54) VALUE                                    \n008894         \"857848839830821812803794786777768760752744736728720713\".\n008896     10 FILLER PIC X(54) VALUE                                    \n008898         \"705698691685678672666661655650645641637632629625622619\".\n008900     10 FILLER PIC X(54) VALUE                                    \n008902         \"616613611609607605603601600598597596595594593592591590\".\n008904     10 FILLER PIC X(54) VALUE                                    \n008906         \"590589588588587587587586586586585585585585584584584584\".\n008908     10 FILLER PIC X(54) VALUE                                    \n008910         \"584584583583583583583583583583583583583583582582582582\".\n008912     10 FILLER PIC X(54) VALUE                                    \n008914         \"582582582582582582582582582582582582582582582582582582\".\n008916     10 FILLER PIC X(39) VALUE                                    \n008918         \"582582582582582582582582582582582582582\".               \n008920     10 FILLER PIC X(54) VALUE                                    \n008922         \"856847838829820811802793784776767758750742734726718710\".\n008924     10 FILLER PIC X(54) VALUE                                    \n008926         \"703695688681675668662656651645640635631627623619615612\".\n008928     10 FILLER PIC X(54) VALUE                                    \n008930         \"609606603601599597595593591590588587586585584583582581\".\n008932     10 FILLER PIC X(54) VALUE                                    \n008934         \"580580579579578578577577576576576575575575575575574574\".\n008936     10 FILLER PIC X(54) VALUE                                    \n008938         \"574574574574574573573573573573573573573573573573573573\".\n008940     10 FILLER PIC X(54) VALUE                                    \n008942         \"573573573573573573573573573573573573573573573573573573\".\n008944     10 FILLER PIC X(39) VALUE                                    \n008946         \"573573573573573573573573573573573573573\".               \n008948     10 FILLER PIC X(54) VALUE                                    \n008950         \"856847838828819810801792783774766757749740732724716708\".\n008952     10 FILLER PIC X(54) VALUE                                    \n008954         \"700693685678671665658652646641635630626621617613609605\".\n008956     10 FILLER PIC X(54) VALUE                                    \n008958         \"602599596594591589587585583581580579577576575574573572\".\n008960     10 FILLER PIC X(54) VALUE                                    \n008962         \"571571570569569568568567567567566566566565565565565565\".\n008964     10 FILLER PIC X(54) VALUE                                    \n008966         \"565564564564564564564564564564563563563563563563563563\".\n008968     10 FILLER PIC X(54) VALUE                                    \n008970         \"563563563563563563563563563563563563563563563563563563\".\n008972     10 FILLER PIC X(39) VALUE                                    \n008974         \"563563563563563563563563563563563563563\".               \n008976     10 FILLER PIC X(54) VALUE                                    \n008978         \"855846837828818809800791782773764756747739730722714706\".\n008980     10 FILLER PIC X(54) VALUE                                    \n008982         \"698690683675668662655649642637631626620616611607603599\".\n008984     10 FILLER PIC X(54) VALUE                                    \n008986         \"595592589586584581579577575573572570569567566565564563\".\n008988     10 FILLER PIC X(54) VALUE                                    \n008990         \"562562561560560559559558558557557557556556556556555555\".\n008992     10 FILLER PIC X(54) VALUE                                    \n008994         \"555555555555554554554554554554554554554554554554554554\".\n008996     10 FILLER PIC X(54) VALUE                                    \n008998         \"554553553553553553553553553553553553553553553553553553\".\n009000     10 FILLER PIC X(39) VALUE                                    \n009002         \"553553553553553553553553553553553553553\".               \n009004     10 FILLER PIC X(54) VALUE                                    \n009006         \"854846836827818809799790781772763755746737729720712704\".\n009008     10 FILLER PIC X(54) VALUE                                    \n009010         \"696688680673666658652645639632627621616611606601597593\".\n009012     10 FILLER PIC X(54) VALUE                                    \n009014         \"589586582579576574571569567565563562560559558556555554\".\n009016     10 FILLER PIC X(54) VALUE                                    \n009018         \"553553552551550550549549548548548547547547546546546546\".\n009020     10 FILLER PIC X(54) VALUE                                    \n009022         \"545545545545545545545545544544544544544544544544544544\".\n009024     10 FILLER PIC X(54) VALUE                                    \n009026         \"544544544544544544544544544544544544544544544544544544\".\n009028     10 FILLER PIC X(39) VALUE                                    \n009030         \"544544544544544544544544544544544544544\".               \n009032     10 FILLER PIC X(54) VALUE                                    \n009034         \"854845836826817808799789780771762753745736727719710702\".\n009036     10 FILLER PIC X(54) VALUE                                    \n009038         \"694686678670663656649642635629623617611606601596591587\".\n009040     10 FILLER PIC X(54) VALUE                                    \n009042         \"583579576572569567564562559557555554552550549548547546\".\n009044     10 FILLER PIC X(54) VALUE                                    \n009046         \"545544543542541541540540539539538538537537537537536536\".\n009048     10 FILLER PIC X(54) VALUE                                    \n009050         \"536536536535535535535535535535535535535535535534534534\".\n009052     10 FILLER PIC X(54) VALUE                                    \n009054         \"534534534534534534534534534534534534534534534534534534\".\n009056     10 FILLER PIC X(39) VALUE                                    \n009058         \"534534534534534534534534534534534534534\".               \n009060     10 FILLER PIC X(54) VALUE                                    \n009062         \"853845835826816807798789779770761752743735726717709700\".\n009064     10 FILLER PIC X(54) VALUE                                    \n009066         \"692684676668660653646639632625619613607601596591586581\".\n009068     10 FILLER PIC X(54) VALUE                                    \n009070         \"577573569566563560557554552549547545544542541539538537\".\n009072     10 FILLER PIC X(54) VALUE                                    \n009074         \"536535534533532532531530530529529528528528527527527527\".\n009076     10 FILLER PIC X(54) VALUE                                    \n009078         \"526526526526526526526525525525525525525525525525525525\".\n009080     10 FILLER PIC X(54) VALUE                                    \n009082         \"525525525525525525525525525525525525525525525525525525\".\n009084     10 FILLER PIC X(39) VALUE                                    \n009086         \"525525525525525525525525525525525525525\".               \n009088     10 FILLER PIC X(54) VALUE                                    \n009090         \"853844835825816807797788779770760751742733725716707699\".\n009092     10 FILLER PIC X(54) VALUE                                    \n009094         \"690682674666658651643636629622615609603597591586581576\".\n009096     10 FILLER PIC X(54) VALUE                                    \n009098         \"572567563559556553550547544542540537536534532531529528\".\n009100     10 FILLER PIC X(54) VALUE                                    \n009102         \"527526525524523522522521521520520519519518518518517517\".\n009104     10 FILLER PIC X(54) VALUE                                    \n009106         \"517517517516516516516516516516516516515515515515515515\".\n009108     10 FILLER PIC X(54) VALUE                                    \n009110         \"515515515515515515515515515515515515515515515515515515\".\n009112     10 FILLER PIC X(39) VALUE                                    \n009114         \"515515515515515515515515515515515515515\".               \n009116     10 FILLER PIC X(54) VALUE                                    \n009118         \"853844834825815806797787778769760750741732724715706697\".\n009120     10 FILLER PIC X(54) VALUE                                    \n009122         \"689680672664656648641633626619612605599593587581576571\".\n009124     10 FILLER PIC X(54) VALUE                                    \n009126         \"566562557553550546543540537534532530528526524522521520\".\n009128     10 FILLER PIC X(54) VALUE                                    \n009130         \"518517516515514513513512511511510510509509509508508508\".\n009132     10 FILLER PIC X(54) VALUE                                    \n009134         \"508507507507507507506506506506506506506506506506506506\".\n009136     10 FILLER PIC X(54) VALUE                                    \n009138         \"506506506506506506506506506506506506506505505505505505\".\n009140     10 FILLER PIC X(39) VALUE                                    \n009142         \"505505505505505505505505505505505505505\".               \n009144     10 FILLER PIC X(54) VALUE                                    \n009146         \"852843834824815805796787777768759750740731722714705696\".\n009148     10 FILLER PIC X(54) VALUE                                    \n009150         \"687679671662654646638631623616609602595589583577572566\".\n009152     10 FILLER PIC X(54) VALUE                                    \n009154         \"561556552547543540536533530527524522520518516514513511\".\n009156     10 FILLER PIC X(54) VALUE                                    \n009158         \"510509507506505505504503502502501501500500499499499498\".\n009160     10 FILLER PIC X(54) VALUE                                    \n009162         \"498498498497497497497497497497497496496496496496496496\".\n009164     10 FILLER PIC X(54) VALUE                                    \n009166         \"496496496496496496496496496496496496496496496496496496\".\n009168     10 FILLER PIC X(39) VALUE                                    \n009170         \"496496496496496496496496496496496496496\".               \n009172     10 FILLER PIC X(54) VALUE                                    \n009174         \"852843833824814804795786777767758749740731721713704695\".\n009176     10 FILLER PIC X(54) VALUE                                    \n009178         \"686677669661652644636628621613606599592586579573567562\".\n009180     10 FILLER PIC X(54) VALUE                                    \n009182         \"556551546542538534530526523520517515512510508506504503\".\n009184     10 FILLER PIC X(54) VALUE                                    \n009186         \"501500499498497496495494493493492491491490490490489489\".\n009188     10 FILLER PIC X(54) VALUE                                    \n009190         \"489488488488488488487487487487487487487487487487487487\".\n009192     10 FILLER PIC X(54) VALUE                                    \n009194         \"486486486486486486486486486486486486486486486486486486\".\n009196     10 FILLER PIC X(39) VALUE                                    \n009198         \"486486486486486486486486486486486486486\".               \n009200     10 FILLER PIC X(54) VALUE                                    \n009202         \"852843833823814804795786776767757748739730721712703694\".\n009204     10 FILLER PIC X(54) VALUE                                    \n009206         \"685676668659651642634626619611603596589582576569563557\".\n009208     10 FILLER PIC X(54) VALUE                                    \n009210         \"552546541536532528524520516513510507505502500498496495\".\n009212     10 FILLER PIC X(54) VALUE                                    \n009214         \"493491490489488487486485484483483482482481481480480479\".\n009216     10 FILLER PIC X(54) VALUE                                    \n009218         \"479479479478478478478478478477477477477477477477477477\".\n009220     10 FILLER PIC X(54) VALUE                                    \n009222         \"477477477477477477477477477477477477477477477477477477\".\n009224     10 FILLER PIC X(39) VALUE                                    \n009226         \"477477477477477477477477477477477477477\".               \n009228     10 FILLER PIC X(54) VALUE                                    \n009230         \"851842833823814804795785776766757747738729720711702693\".\n009232     10 FILLER PIC X(54) VALUE                                    \n009234         \"684675666658649641633624616609601594586579572566559553\".\n009236     10 FILLER PIC X(54) VALUE                                    \n009238         \"547542536531527522518514510507503500497495492490488486\".\n009240     10 FILLER PIC X(54) VALUE                                    \n009242         \"485483482480479478477476475474474473472472471471470470\".\n009244     10 FILLER PIC X(54) VALUE                                    \n009246         \"470469469469469469468468468468468468468468467467467467\".\n009248     10 FILLER PIC X(54) VALUE                                    \n009250         \"467467467467467467467467467467467467467467467467467467\".\n009252     10 FILLER PIC X(39) VALUE                                    \n009254         \"467467467467467467467467467467467467467\".               \n009256     10 FILLER PIC X(54) VALUE                                    \n009258         \"851842832823813804794785775766756747737728719710701692\".\n009260     10 FILLER PIC X(54) VALUE                                    \n009262         \"683674665656648639631623615607599591584576569563556550\".\n009264     10 FILLER PIC X(54) VALUE                                    \n009266         \"543538532527522517512508504500497493490488485483480478\".\n009268     10 FILLER PIC X(54) VALUE                                    \n009270         \"477475473472471469468467466465465464463463462462461461\".\n009272     10 FILLER PIC X(54) VALUE                                    \n009274         \"460460460459459459459459459458458458458458458458458458\".\n009276     10 FILLER PIC X(54) VALUE                                    \n009278         \"458458458458458458458458458458458458458458458457457457\".\n009280     10 FILLER PIC X(39) VALUE                                    \n009282         \"457457457457457457457457457457457457457\".               \n009284     10 FILLER PIC X(54) VALUE                                    \n009286         \"851842832822813803794784775765756746737728718709700691\".\n009288     10 FILLER PIC X(54) VALUE                                    \n009290         \"682673664655646638629621613605597589581574567560553546\".\n009292     10 FILLER PIC X(54) VALUE                                    \n009294         \"540534528522517512507502498494490487484481478475473471\".\n009296     10 FILLER PIC X(54) VALUE                                    \n009298         \"469467465463462461460458457457456455454454453452452451\".\n009300     10 FILLER PIC X(54) VALUE                                    \n009302         \"451451450450450450449449449449449449449448448448448448\".\n009304     10 FILLER PIC X(54) VALUE                                    \n009306         \"448448448448448448448448448448448448448448448448448448\".\n009308     10 FILLER PIC X(39) VALUE                                    \n009310         \"448448448448448448448448448448448448448\".               \n009312     10 FILLER PIC X(54) VALUE                                    \n009314         \"850841832822813803793784774765755746736727718708699690\".\n009316     10 FILLER PIC X(54) VALUE                                    \n009318         \"681672663654645636628619611603595587579571564557550543\".\n009320     10 FILLER PIC X(54) VALUE                                    \n009322         \"536530524518512507502497492488484480477474471468465463\".\n009324     10 FILLER PIC X(54) VALUE                                    \n009326         \"461459457455454452451450449448447446445444444443443442\".\n009328     10 FILLER PIC X(54) VALUE                                    \n009330         \"442441441441440440440440439439439439439439439439439439\".\n009332     10 FILLER PIC X(54) VALUE                                    \n009334         \"439439438438438438438438438438438438438438438438438438\".\n009336     10 FILLER PIC X(39) VALUE                                    \n009338         \"438438438438438438438438438438438438438\".               \n009340     10 FILLER PIC X(54) VALUE                                    \n009342         \"850841831822812803793783774764755745736726717708698689\".\n009344     10 FILLER PIC X(54) VALUE                                    \n009346         \"680671662653644635627618610601593585577569562554547540\".\n009348     10 FILLER PIC X(54) VALUE                                    \n009350         \"533526520514508502497492487483478474471467464461458456\".\n009352     10 FILLER PIC X(54) VALUE                                    \n009354         \"453451449447445444443441440439438437436435435434433433\".\n009356     10 FILLER PIC X(54) VALUE                                    \n009358         \"432432432431431431430430430430430430429429429429429429\".\n009360     10 FILLER PIC X(54) VALUE                                    \n009362         \"429429429429429429429429429429429429429429429429429429\".\n009364     10 FILLER PIC X(39) VALUE                                    \n009366         \"429429429429429429429429429429429429429\".               \n009368     10 FILLER PIC X(54) VALUE                                    \n009370         \"850841831822812802793783773764754745735726716707698688\".\n009372     10 FILLER PIC X(54) VALUE                                    \n009374         \"679670661652643634625617608600591583575567559552544537\".\n009376     10 FILLER PIC X(54) VALUE                                    \n009378         \"530523516510504498492487482477473468464461457454451448\".\n009380     10 FILLER PIC X(54) VALUE                                    \n009382         \"446443441439437436434433431430429428427426426425424424\".\n009384     10 FILLER PIC X(54) VALUE                                    \n009386         \"423423422422422421421421421420420420420420420420420419\".\n009388     10 FILLER PIC X(54) VALUE                                    \n009390         \"419419419419419419419419419419419419419419419419419419\".\n009392     10 FILLER PIC X(39) VALUE                                    \n009394         \"419419419419419419419419419419419419419\".               \n009396     10 FILLER PIC X(54) VALUE                                    \n009398         \"850841831821812802792783773764754744735725716706697688\".\n009400     10 FILLER PIC X(54) VALUE                                    \n009402         \"679669660651642633624615607598590581573565557549542534\".\n009404     10 FILLER PIC X(54) VALUE                                    \n009406         \"527520513507500494488483477472467463459455451447444441\".\n009408     10 FILLER PIC X(54) VALUE                                    \n009410         \"438436434431429428426424423422421419418418417416415415\".\n009412     10 FILLER PIC X(54) VALUE                                    \n009414         \"414414413413412412412411411411411411410410410410410410\".\n009416     10 FILLER PIC X(54) VALUE                                    \n009418         \"410410410410410410410410410410410410410410410410410410\".\n009420     10 FILLER PIC X(39) VALUE                                    \n009422         \"410410410410410410410410410410410410410\".               \n009424     10 FILLER PIC X(54) VALUE                                    \n009426         \"849840831821811802792782773763754744734725715706697687\".\n009428     10 FILLER PIC X(54) VALUE                                    \n009430         \"678669659650641632623614606597588580572563555547540532\".\n009432     10 FILLER PIC X(54) VALUE                                    \n009434         \"524517510503497490484478473467462457453449445441438434\".\n009436     10 FILLER PIC X(54) VALUE                                    \n009438         \"431429426424422420418416415413412411410409408407406406\".\n009440     10 FILLER PIC X(54) VALUE                                    \n009442         \"405404404403403403402402402401401401401401401401400400\".\n009444     10 FILLER PIC X(54) VALUE                                    \n009446         \"400400400400400400400400400400400400400400400400400400\".\n009448     10 FILLER PIC X(39) VALUE                                    \n009450         \"400400400400400400400400400400400400400\".               \n009452     10 FILLER PIC X(54) VALUE                                    \n009454         \"849840831821811802792782773763753744734724715705696687\".\n009456     10 FILLER PIC X(54) VALUE                                    \n009458         \"677668659650640631622613605596587579570562554545537530\".\n009460     10 FILLER PIC X(54) VALUE                                    \n009462         \"522515507500493487480474468463457452448443439435431428\".\n009464     10 FILLER PIC X(54) VALUE                                    \n009466         \"425422419416414412410408406405404402401400399398397397\".\n009468     10 FILLER PIC X(54) VALUE                                    \n009470         \"396395395394394393393393392392392392392391391391391391\".\n009472     10 FILLER PIC X(54) VALUE                                    \n009474         \"391391391391391391391391391391390390390390390390390390\".\n009476     10 FILLER PIC X(39) VALUE                                    \n009478         \"390390390390390390390390390390390390390\".               \n009480     10 FILLER PIC X(54) VALUE                                    \n009482         \"849840830821811801792782772763753743734724715705696686\".\n009484     10 FILLER PIC X(54) VALUE                                    \n009486         \"677667658649640630621612603595586577569560552544536528\".\n009488     10 FILLER PIC X(54) VALUE                                    \n009490         \"520512505497490484477471464459453448443438433429425421\".\n009492     10 FILLER PIC X(54) VALUE                                    \n009494         \"418415412409407404402400398397395394393391390389388388\".\n009496     10 FILLER PIC X(54) VALUE                                    \n009498         \"387386386385385384384383383383383382382382382382382381\".\n009500     10 FILLER PIC X(54) VALUE                                    \n009502         \"381381381381381381381381381381381381381381381381381381\".\n009504     10 FILLER PIC X(39) VALUE                                    \n009506         \"381381381381381381381381381381381381381\".               \n009508     10 FILLER PIC X(54) VALUE                                    \n009510         \"849840830821811801791782772762753743733724714705695686\".\n009512     10 FILLER PIC X(54) VALUE                                    \n009514         \"676667657648639630621612603594585576567559550542534526\".\n009516     10 FILLER PIC X(54) VALUE                                    \n009518         \"518510502495488481474467461455449443438433428423419415\".\n009520     10 FILLER PIC X(54) VALUE                                    \n009522         \"412408405402399397395392390389387386384383382381380379\".\n009524     10 FILLER PIC X(54) VALUE                                    \n009526         \"378377377376375375375374374373373373373373372372372372\".\n009528     10 FILLER PIC X(54) VALUE                                    \n009530         \"372372372372372372372372372372371371371371371371371371\".\n009532     10 FILLER PIC X(39) VALUE                                    \n009534         \"371371371371371371371371371371371371371\".               \n009536     10 FILLER PIC X(54) VALUE                                    \n009538         \"849840830820811801791781772762752743733723714704695685\".\n009540     10 FILLER PIC X(54) VALUE                                    \n009542         \"676666657648638629620611602593584575566558549541532524\".\n009544     10 FILLER PIC X(54) VALUE                                    \n009546         \"516508500492485478471464457451445439433428423418414409\".\n009548     10 FILLER PIC X(54) VALUE                                    \n009550         \"406402398395392390387385383381379377376375373372371370\".\n009552     10 FILLER PIC X(54) VALUE                                    \n009554         \"369368368367366366365365365364364364363363363363363363\".\n009556     10 FILLER PIC X(54) VALUE                                    \n009558         \"363362362362362362362362362362362362362362362362362362\".\n009560     10 FILLER PIC X(39) VALUE                                    \n009562         \"362362362362362362362362362362362362362\".               \n009564     10 FILLER PIC X(54) VALUE                                    \n009566         \"848840830820810801791781772762752742733723713704694685\".\n009568     10 FILLER PIC X(54) VALUE                                    \n009570         \"675666656647638628619610601592583574565556548539531522\".\n009572     10 FILLER PIC X(54) VALUE                                    \n009574         \"514506498490483475468461454447441435429423418413408404\".\n009576     10 FILLER PIC X(54) VALUE                                    \n009578         \"400396392389386383380377375373371369368366365364362361\".\n009580     10 FILLER PIC X(54) VALUE                                    \n009582         \"360360359358357357356356355355355354354354354354353353\".\n009584     10 FILLER PIC X(54) VALUE                                    \n009586         \"353353353353353353353353353353353353353353353353353353\".\n009588     10 FILLER PIC X(39) VALUE                                    \n009590         \"353353353353353353353353353353353353353\".               \n009592     10 FILLER PIC X(54) VALUE                                    \n009594         \"848839830820810801791781771762752742732723713704694684\".\n009596     10 FILLER PIC X(54) VALUE                                    \n009598         \"675665656647637628619609600591582573564555547538529521\".\n009600     10 FILLER PIC X(54) VALUE                                    \n009602         \"513504496488480473465458451444438431425419414408403399\".\n009604     10 FILLER PIC X(54) VALUE                                    \n009606         \"394390386382379376373370368366363362360358357355354353\".\n009608     10 FILLER PIC X(54) VALUE                                    \n009610         \"352351350349349348347347346346346345345345345344344344\".\n009612     10 FILLER PIC X(54) VALUE                                    \n009614         \"344344344344344344343343343343343343343343343343343343\".\n009616     10 FILLER PIC X(39) VALUE                                    \n009618         \"343343343343343343343343343343343343343\".               \n009620     10 FILLER PIC X(54) VALUE                                    \n009622         \"848839830820810800791781771761752742732723713703694684\".\n009624     10 FILLER PIC X(54) VALUE                                    \n009626         \"674665655646637627618609599590581572563554546537528520\".\n009628     10 FILLER PIC X(54) VALUE                                    \n009630         \"511503495486478471463456448441434428421415409404399394\".\n009632     10 FILLER PIC X(54) VALUE                                    \n009634         \"389384380376373369366363361358356354352350349347346345\".\n009636     10 FILLER PIC X(54) VALUE                                    \n009638         \"343342341341340339339338337337337336336336335335335335\".\n009640     10 FILLER PIC X(54) VALUE                                    \n009642         \"335335335334334334334334334334334334334334334334334334\".\n009644     10 FILLER PIC X(39) VALUE                                    \n009646         \"334334334334334334334334334334334334334\".               \n009648     10 FILLER PIC X(54) VALUE                                    \n009650         \"848839829820810800790781771761751742732722713703693684\".\n009652     10 FILLER PIC X(54) VALUE                                    \n009654         \"674665655646636627617608599590580571562553545536527518\".\n009656     10 FILLER PIC X(54) VALUE                                    \n009658         \"510501493485477469461453446438431425418412406400394389\".\n009660     10 FILLER PIC X(54) VALUE                                    \n009662         \"384379375371367363360357354351349346344342341339338336\".\n009664     10 FILLER PIC X(54) VALUE                                    \n009666         \"335334333332331330330329329328328327327327326326326326\".\n009668     10 FILLER PIC X(54) VALUE                                    \n009670         \"326325325325325325325325325325325325325325325325325325\".\n009672     10 FILLER PIC X(39) VALUE                                    \n009674         \"325325325325325325325325325325325325325\".               \n009676     10 FILLER PIC X(54) VALUE                                    \n009678         \"848839829820810800790781771761751742732722712703693683\".\n009680     10 FILLER PIC X(54) VALUE                                    \n009682         \"674664655645636626617608598589580571562553544535526517\".\n009684     10 FILLER PIC X(54) VALUE                                    \n009686         \"509500491483475467459451443436429422415408402396390384\".\n009688     10 FILLER PIC X(54) VALUE                                    \n009690         \"379374369365361357353350347344342339337335333331330328\".\n009692     10 FILLER PIC X(54) VALUE                                    \n009694         \"327326324324323322321320320319319318318318317317317317\".\n009696     10 FILLER PIC X(54) VALUE                                    \n009698         \"317316316316316316316316316316316316316316316316316316\".\n009700     10 FILLER PIC X(39) VALUE                                    \n009702         \"316316316316316316316316316316316316316\".               \n009704     10 FILLER PIC X(54) VALUE                                    \n009706         \"848839829819810800790780771761751741732722712702693683\".\n009708     10 FILLER PIC X(54) VALUE                                    \n009710         \"674664654645635626616607598588579570561552543534525516\".\n009712     10 FILLER PIC X(54) VALUE                                    \n009714         \"507499490482473465457449441434426419412405398392386380\".\n009716     10 FILLER PIC X(54) VALUE                                    \n009718         \"375369365360355351348344341338335332330327325323322320\".\n009720     10 FILLER PIC X(54) VALUE                                    \n009722         \"319317316315314313312312311311310310309309309308308308\".\n009724     10 FILLER PIC X(54) VALUE                                    \n009726         \"308307307307307307307307307307307307307307307307307307\".\n009728     10 FILLER PIC X(39) VALUE                                    \n009730         \"307307307307307307307307307307307307306\".               \n009732     10 FILLER PIC X(54) VALUE                                    \n009734         \"848839829819810800790780770761751741731722712702693683\".\n009736     10 FILLER PIC X(54) VALUE                                    \n009738         \"673664654645635625616607597588579569560551542533524515\".\n009740     10 FILLER PIC X(54) VALUE                                    \n009742         \"506498489480472463455447439431424416409402395389382376\".\n009744     10 FILLER PIC X(54) VALUE                                    \n009746         \"371365360355350346342338334331328325323320318316314312\".\n009748     10 FILLER PIC X(54) VALUE                                    \n009750         \"311309308307306305304303303302301301300300300299299299\".\n009752     10 FILLER PIC X(54) VALUE                                    \n009754         \"299299298298298298298298298298298298298298298298298298\".\n009756     10 FILLER PIC X(39) VALUE                                    \n009758         \"298298298298298298298298298298298298298\".               \n009760     10 FILLER PIC X(54) VALUE                                    \n009762         \"848839829819809800790780770761751741731721712702692683\".\n009764     10 FILLER PIC X(54) VALUE                                    \n009766         \"673663654644635625616606597587578569560550541532523514\".\n009768     10 FILLER PIC X(54) VALUE                                    \n009770         \"505497488479471462454445437429422414407399392386379373\".\n009772     10 FILLER PIC X(54) VALUE                                    \n009774         \"367361355350345341336332328325322319316313311309307305\".\n009776     10 FILLER PIC X(54) VALUE                                    \n009778         \"303301300299298297296295294293293292292291291291290290\".\n009780     10 FILLER PIC X(54) VALUE                                    \n009782         \"290290290290289289289289289289289289289289289289289289\".\n009784     10 FILLER PIC X(39) VALUE                                    \n009786         \"289289289289289289289289289289289289289\".               \n009788     10 FILLER PIC X(54) VALUE                                    \n009790         \"847839829819809800790780770760751741731721712702692682\".\n009792     10 FILLER PIC X(54) VALUE                                    \n009794         \"673663654644634625615606596587578568559550541532522513\".\n009796     10 FILLER PIC X(54) VALUE                                    \n009798         \"505496487478469461452444436428420412404397390383376369\".\n009800     10 FILLER PIC X(54) VALUE                                    \n009802         \"363357351346341336331327323319315312309306304301299297\".\n009804     10 FILLER PIC X(54) VALUE                                    \n009806         \"295294292291290288287287286285284284283283282282282282\".\n009808     10 FILLER PIC X(54) VALUE                                    \n009810         \"281281281281281281280280280280280280280280280280280280\".\n009812     10 FILLER PIC X(39) VALUE                                    \n009814         \"280280280280280280280280280280280280280\".               \n009816     10 FILLER PIC X(54) VALUE                                    \n009818         \"847838829819809799790780770760750741731721711702692682\".\n009820     10 FILLER PIC X(54) VALUE                                    \n009822         \"672663653644634624615605596587577568559549540531522513\".\n009824     10 FILLER PIC X(54) VALUE                                    \n009826         \"504495486477468460451443434426418410402395387380373366\".\n009828     10 FILLER PIC X(54) VALUE                                    \n009830         \"360353348342336331326322317313310306303300297294292290\".\n009832     10 FILLER PIC X(54) VALUE                                    \n009834         \"288286284283282280279278278277276275275274274274273273\".\n009836     10 FILLER PIC X(54) VALUE                                    \n009838         \"273273272272272272272272272272271271271271271271271271\".\n009840     10 FILLER PIC X(39) VALUE                                    \n009842         \"271271271271271271271271271271271271271\".               \n009844     10 FILLER PIC X(54) VALUE                                    \n009846         \"847838829819809799790780770760750741731721711701692682\".\n009848     10 FILLER PIC X(54) VALUE                                    \n009850         \"672663653643634624615605596586577567558549540530521512\".\n009852     10 FILLER PIC X(54) VALUE                                    \n009854         \"503494485476467458450441433424416408400392385377370363\".\n009856     10 FILLER PIC X(54) VALUE                                    \n009858         \"357350344338332327322317312308304300297294291288285283\".\n009860     10 FILLER PIC X(54) VALUE                                    \n009862         \"281279277275274273271270269269268267267266266265265264\".\n009864     10 FILLER PIC X(54) VALUE                                    \n009866         \"264264264264263263263263263263263263263263263263263263\".\n009868     10 FILLER PIC X(39) VALUE                                    \n009870         \"263263263263263263263263263263263262262\".               \n009872     10 FILLER PIC X(54) VALUE                                    \n009874         \"847838829819809799789780770760750740731721711701692682\".\n009876     10 FILLER PIC X(54) VALUE                                    \n009878         \"672662653643634624614605595586576567558548539530521511\".\n009880     10 FILLER PIC X(54) VALUE                                    \n009882         \"502493484475466457449440431423415406398390383375368361\".\n009884     10 FILLER PIC X(54) VALUE                                    \n009886         \"354347341334328323317312308303299295291287284281279276\".\n009888     10 FILLER PIC X(54) VALUE                                    \n009890         \"274272270268266265264262261260260259258258257257256256\".\n009892     10 FILLER PIC X(54) VALUE                                    \n009894         \"256256255255255255255255255254254254254254254254254254\".\n009896     10 FILLER PIC X(39) VALUE                                    \n009898         \"254254254254254254254254253254254254254\".               \n009900     10 FILLER PIC X(54) VALUE                                    \n009902         \"847838829819809799789780770760750740730721711701691682\".\n009904     10 FILLER PIC X(54) VALUE                                    \n009906         \"672662653643633624614605595586576567557548539529520511\".\n009908     10 FILLER PIC X(54) VALUE                                    \n009910         \"502493483474465457448439430422413405397389381373366358\".\n009912     10 FILLER PIC X(54) VALUE                                    \n009914         \"351344338331325319313308303298294289285282278275272269\".\n009916     10 FILLER PIC X(54) VALUE                                    \n009918         \"267265262261259257256255253252252251250250249249248248\".\n009920     10 FILLER PIC X(54) VALUE                                    \n009922         \"247247247247247246246246246246246246246246246246246246\".\n009924     10 FILLER PIC X(39) VALUE                                    \n009926         \"246246246246246246246246246246245245245\".               \n009928     10 FILLER PIC X(54) VALUE                                    \n009930         \"847838828819809799789779770760750740730721711701691682\".\n009932     10 FILLER PIC X(54) VALUE                                    \n009934         \"672662652643633623614604595585576566557548538529520510\".\n009936     10 FILLER PIC X(54) VALUE                                    \n009938         \"501492483474465456447438429421412404395387379371363356\".\n009940     10 FILLER PIC X(54) VALUE                                    \n009942         \"349342335328322315310304299294289284280276272269266263\".\n009944     10 FILLER PIC X(54) VALUE                                    \n009946         \"260258255253252250248247246245244243242241241240240240\".\n009948     10 FILLER PIC X(54) VALUE                                    \n009950         \"239239239238238238238238238238238238237237237237237237\".\n009952     10 FILLER PIC X(39) VALUE                                    \n009954         \"237237237237237237237237237237237237237\".               \n009956     10 FILLER PIC X(54) VALUE                                    \n009958         \"847838828819809799789779770760750740730720711701691681\".\n009960     10 FILLER PIC X(54) VALUE                                    \n009962         \"672662652643633623614604595585575566557547538528519510\".\n009964     10 FILLER PIC X(54) VALUE                                    \n009966         \"501491482473464455446437428419411402394386377369362354\".\n009968     10 FILLER PIC X(54) VALUE                                    \n009970         \"346339332325319312306300295289284280275271267263260257\".\n009972     10 FILLER PIC X(54) VALUE                                    \n009974         \"254251249246244243241239238237236235234233233232232231\".\n009976     10 FILLER PIC X(54) VALUE                                    \n009978         \"231231230230230230230230229229229229229229229229229229\".\n009980     10 FILLER PIC X(39) VALUE                                    \n009982         \"229229229229229229229229229229229229229\".               \n009984     10 FILLER PIC X(54) VALUE                                    \n009986         \"847838828819809799789779769760750740730720711701691681\".\n009988     10 FILLER PIC X(54) VALUE                                    \n009990         \"672662652642633623613604594585575566556547537528519509\".\n009992     10 FILLER PIC X(54) VALUE                                    \n009994         \"500491482472463454445436427418410401393384376368360352\".\n009996     10 FILLER PIC X(54) VALUE                                    \n009998         \"344337330323316309303297291285280275270266262258254251\".\n010000     10 FILLER PIC X(54) VALUE                                    \n010002         \"248245242240237235234232231229228227226226225224224223\".\n010004     10 FILLER PIC X(54) VALUE                                    \n010006         \"223223222222222222222221221221221221221221221221221221\".\n010008     10 FILLER PIC X(39) VALUE                                    \n010010         \"221221221221221221221221221221221221220\".               \n010012     10 FILLER PIC X(54) VALUE                                    \n010014         \"847838828819809799789779769760750740730720710701691681\".\n010016     10 FILLER PIC X(54) VALUE                                    \n010018         \"671662652642633623613604594585575565556547537528518509\".\n010020     10 FILLER PIC X(54) VALUE                                    \n010022         \"500490481472463454444435426418409400391383375366358350\".\n010024     10 FILLER PIC X(54) VALUE                                    \n010026         \"342335327320313306300294287282276271266261257253249245\".\n010028     10 FILLER PIC X(54) VALUE                                    \n010030         \"242239236233231229227225223222221220219218217216216215\".\n010032     10 FILLER PIC X(54) VALUE                                    \n010034         \"215215214214214214213213213213213213213213213213213213\".\n010036     10 FILLER PIC X(39) VALUE                                    \n010038         \"213213213213213213213213213212212212212\".               \n010040     10 FILLER PIC X(54) VALUE                                    \n010042         \"847838828818809799789779769759750740730720710701691681\".\n010044     10 FILLER PIC X(54) VALUE                                    \n010046         \"671662652642632623613603594584575565556546537527518509\".\n010048     10 FILLER PIC X(54) VALUE                                    \n010050         \"499490481471462453444435426417408399390382373365357349\".\n010052     10 FILLER PIC X(54) VALUE                                    \n010054         \"341333325318311304297291284278272267262257252248243240\".\n010056     10 FILLER PIC X(54) VALUE                                    \n010058         \"236233230227224222220218216215213212211210209209208207\".\n010060     10 FILLER PIC X(54) VALUE                                    \n010062         \"207207206206206206205205205205205205205205205205205205\".\n010064     10 FILLER PIC X(39) VALUE                                    \n010066         \"205204204204204204204204204204204204204\".               \n010068     10 FILLER PIC X(54) VALUE                                    \n010070         \"847838828818809799789779769759750740730720710700691681\".\n010072     10 FILLER PIC X(54) VALUE                                    \n010074         \"671661652642632623613603594584575565556546537527518508\".\n010076     10 FILLER PIC X(54) VALUE                                    \n010078         \"499490480471462452443434425416407398389381372364355347\".\n010080     10 FILLER PIC X(54) VALUE                                    \n010082         \"339331323316309301294288281275269263258253248243239234\".\n010084     10 FILLER PIC X(54) VALUE                                    \n010086         \"231227224221218215213211209207206205204203202201200200\".\n010088     10 FILLER PIC X(54) VALUE                                    \n010090         \"199199198198198197197197197197197197197196196196196196\".\n010092     10 FILLER PIC X(39) VALUE                                    \n010094         \"196196196196196196196196196196196196196\".               \n010096     10 FILLER PIC X(54) VALUE                                    \n010098         \"847838828818809799789779769759749740730720710700691681\".\n010100     10 FILLER PIC X(54) VALUE                                    \n010102         \"671661652642632622613603594584574565555546536527517508\".\n010104     10 FILLER PIC X(54) VALUE                                    \n010106         \"499489480470461452443433424415406397388380371362354346\".\n010108     10 FILLER PIC X(54) VALUE                                    \n010110         \"338330322314307299292285279272266260254249243239234229\".\n010112     10 FILLER PIC X(54) VALUE                                    \n010114         \"225222218215212209206204202200199197196195194193192192\".\n010116     10 FILLER PIC X(54) VALUE                                    \n010118         \"191191190190190189189189189189189189188188188188188188\".\n010120     10 FILLER PIC X(39) VALUE                                    \n010122         \"188188188188188188188188188188188188188\".               \n010124     10 FILLER PIC X(54) VALUE                                    \n010126         \"847838828818809799789779769759749740730720710700690681\".\n010128     10 FILLER PIC X(54) VALUE                                    \n010130         \"671661651642632622613603593584574565555546536527517508\".\n010132     10 FILLER PIC X(54) VALUE                                    \n010134         \"498489479470461451442433424415406397388379370361353345\".\n010136     10 FILLER PIC X(54) VALUE                                    \n010138         \"336328320312305297290283276269263257251245240234229225\".\n010140     10 FILLER PIC X(54) VALUE                                    \n010142         \"220216213209206203200198196194192190189188187186185184\".\n010144     10 FILLER PIC X(54) VALUE                                    \n010146         \"184183183182182182181181181181181181180180180180180180\".\n010148     10 FILLER PIC X(39) VALUE                                    \n010150         \"180180180180180180180180180180180180180\".               \n010152     10 FILLER PIC X(54) VALUE                                    \n010154         \"847838828818809799789779769759749739730720710700690681\".\n010156     10 FILLER PIC X(54) VALUE                                    \n010158         \"671661651642632622613603593584574565555545536526517508\".\n010160     10 FILLER PIC X(54) VALUE                                    \n010162         \"498489479470460451442432423414405396387378369360352343\".\n010164     10 FILLER PIC X(54) VALUE                                    \n010166         \"335327319311303295288281274267260254248242236231225220\".\n010168     10 FILLER PIC X(54) VALUE                                    \n010170         \"216211207204200197194192189187185183182181179178177177\".\n010172     10 FILLER PIC X(54) VALUE                                    \n010174         \"176175175174174174174173173173173173173173172172172172\".\n010176     10 FILLER PIC X(39) VALUE                                    \n010178         \"172172172172172172172172172172172172172\".               \n010180     10 FILLER PIC X(54) VALUE                                    \n010182         \"846838828818808799789779769759749739730720710700690681\".\n010184     10 FILLER PIC X(54) VALUE                                    \n010186         \"671661651642632622612603593584574564555545536526517507\".\n010188     10 FILLER PIC X(54) VALUE                                    \n010190         \"498488479469460451441432423414404395386377368360351342\".\n010192     10 FILLER PIC X(54) VALUE                                    \n010194         \"334326317309301294286279272265258251245239233227222216\".\n010196     10 FILLER PIC X(54) VALUE                                    \n010198         \"211207203199195191188186183181179177175174172171170169\".\n010200     10 FILLER PIC X(54) VALUE                                    \n010202         \"169168167167166166166166165165165165165165165165165165\".\n010204     10 FILLER PIC X(39) VALUE                                    \n010206         \"156164164164164164164164164164164164164\".               \n010208     10 FILLER PIC X(54) VALUE                                    \n010210         \"846838828818808799789779769759749739729720710700690680\".\n010212     10 FILLER PIC X(54) VALUE                                    \n010214         \"671661651641632622612603593583574564555545536526517507\".\n010216     10 FILLER PIC X(54) VALUE                                    \n010218         \"498488479469460450441432422413404395386377368359350341\".\n010220     10 FILLER PIC X(54) VALUE                                    \n010222         \"333324316308300292284277270262255249242236230224218213\".\n010224     10 FILLER PIC X(54) VALUE                                    \n010226         \"207203198194190186183180177174172170168167165164163162\".\n010228     10 FILLER PIC X(54) VALUE                                    \n010230         \"161161160159159159158158158157157157157157157157157157\".\n010232     10 FILLER PIC X(39) VALUE                                    \n010234         \"157157157157157157157157156156156156156\".               \n010236     10 FILLER PIC X(54) VALUE                                    \n010238         \"846838828818808799789779769759749739729720710700690680\".\n010240     10 FILLER PIC X(54) VALUE                                    \n010242         \"671661651641632622612603593583574564555545535526516507\".\n010244     10 FILLER PIC X(54) VALUE                                    \n010246         \"497488478469459450441431422413403394385376367358349341\".\n010248     10 FILLER PIC X(54) VALUE                                    \n010250         \"332324315307299291283275268261253246240233227221215209\".\n010252     10 FILLER PIC X(54) VALUE                                    \n010254         \"204199194189185181178174171169166164162160159157156155\".\n010256     10 FILLER PIC X(54) VALUE                                    \n010258         \"154153153152152151151150150150150150149149149149149149\".\n010260     10 FILLER PIC X(39) VALUE                                    \n010262         \"149149149149149149149149149149149148148\".               \n010264     10 FILLER PIC X(54) VALUE                                    \n010266         \"846838828818808798789779769759749739729720710700690680\".\n010268     10 FILLER PIC X(54) VALUE                                    \n010270         \"671661651641632622612602593583574564554545535526516507\".\n010272     10 FILLER PIC X(54) VALUE                                    \n010274         \"497487478468459449440430421412403394385375366357349340\".\n010276     10 FILLER PIC X(54) VALUE                                    \n010278         \"331323314306298290282274266259252244237231224218212206\".\n010280     10 FILLER PIC X(54) VALUE                                    \n010282         \"200195190185181177173169166163160158156154152151149148\".\n010284     10 FILLER PIC X(54) VALUE                                    \n010286         \"147146146145144144143143143143142142142142142142142142\".\n010288     10 FILLER PIC X(39) VALUE                                    \n010290         \"142142142142142142141141141141141141141\".               \n010292     10 FILLER PIC X(54) VALUE                                    \n010294         \"846838828818808798789779769759749739729720710700690680\".\n010296     10 FILLER PIC X(54) VALUE                                    \n010298         \"670661651641631622612602593583573564554545535526516507\".\n010300     10 FILLER PIC X(54) VALUE                                    \n010302         \"497488478469459450440431421412403393384375366357348339\".\n010304     10 FILLER PIC X(54) VALUE                                    \n010306         \"330322313305297288280273265257250243235229222215209203\".\n010308     10 FILLER PIC X(54) VALUE                                    \n010310         \"197191186181177172168164161158155152150148146144143142\".\n010312     10 FILLER PIC X(54) VALUE                                    \n010314         \"141140139138137137136136136135135135135135135134134134\".\n010316     10 FILLER PIC X(39) VALUE                                    \n010318         \"134134134134134134134134134134134134133\".               \n010320     10 FILLER PIC X(54) VALUE                                    \n010322         \"846838828818808798789779769759749739729719710700690680\".\n010324     10 FILLER PIC X(54) VALUE                                    \n010326         \"670661651641631622612602593583573564554545535526516506\".\n010328     10 FILLER PIC X(54) VALUE                                    \n010330         \"497487478468459449440430421412402393384375365356347339\".\n010332     10 FILLER PIC X(54) VALUE                                    \n010334         \"330321312304296287279271264256248241234227220213206200\".\n010336     10 FILLER PIC X(54) VALUE                                    \n010338         \"194188183178173168164160156153150147144142140138137135\".\n010340     10 FILLER PIC X(54) VALUE                                    \n010342         \"134133132131131130129129129128128128128128127127127127\".\n010344     10 FILLER PIC X(39) VALUE                                    \n010346         \"127127127127127127127127127127126126126\".               \n010348     10 FILLER PIC X(54) VALUE                                    \n010350         \"846838828818808798789779769759749739729719710700690680\".\n010352     10 FILLER PIC X(54) VALUE                                    \n010354         \"670661651641631622612602593583573564554545535525516506\".\n010356     10 FILLER PIC X(54) VALUE                                    \n010358         \"497487478468459449440430421411402393383374365356347338\".\n010360     10 FILLER PIC X(54) VALUE                                    \n010362         \"329320312303295287278270262255247239232225218211204198\".\n010364     10 FILLER PIC X(54) VALUE                                    \n010366         \"192186180174169164160156152148145142139136134132131129\".\n010368     10 FILLER PIC X(54) VALUE                                    \n010370         \"128127126125124123123122122122121121121121120120120120\".\n010372     10 FILLER PIC X(39) VALUE                                    \n010374         \"120120120120120120120120120120119119119\".               \n010376     10 FILLER PIC X(54) VALUE                                    \n010378         \"846838828818808798789779769759749739729719710700690680\".\n010380     10 FILLER PIC X(54) VALUE                                    \n010382         \"670661651641631621612602592583573564554544535525516506\".\n010384     10 FILLER PIC X(54) VALUE                                    \n010386         \"497487478468459449439430421411402392383374365355346337\".\n010388     10 FILLER PIC X(54) VALUE                                    \n010390         \"329320311303294286278269261253246238231223216209202196\".\n010392     10 FILLER PIC X(54) VALUE                                    \n010394         \"189183177171166161156152147144140137134131129127125123\".\n010396     10 FILLER PIC X(54) VALUE                                    \n010398         \"122121119119118117116116115115115114114114114114114114\".\n010400     10 FILLER PIC X(39) VALUE                                    \n010402         \"114113113113113113113113113113113112112\".               \n010404     10 FILLER PIC X(54) VALUE                                    \n010406         \"846838828818808798789779769759749739729719710700690680\".\n010408     10 FILLER PIC X(54) VALUE                                    \n010410         \"670660651641631621612602592583573564554544535525516506\".\n010412     10 FILLER PIC X(54) VALUE                                    \n010414         \"497487477468458449439430420411401392383373364355346337\".\n010416     10 FILLER PIC X(54) VALUE                                    \n010418         \"328319311302293285277269260252245237229222215207200194\".\n010420     10 FILLER PIC X(54) VALUE                                    \n010422         \"187181174169163158153148144140136132129126124122120118\".\n010424     10 FILLER PIC X(54) VALUE                                    \n010426         \"116115114113112111110110109109108108108107107107107107\".\n010428     10 FILLER PIC X(39) VALUE                                    \n010430         \"107107107107107107107107106106106106105\".               \n010432     10 FILLER PIC X(54) VALUE                                    \n010434         \"846838828818808798789779769759749739729719709700690680\".\n010436     10 FILLER PIC X(54) VALUE                                    \n010438         \"670660651641631621612602592583573563554544535525516506\".\n010440     10 FILLER PIC X(54) VALUE                                    \n010442         \"497487477468458449439430420411401392383373364355346337\".\n010444     10 FILLER PIC X(54) VALUE                                    \n010446         \"328319310301293284276268260252244236228221213206199192\".\n010448     10 FILLER PIC X(54) VALUE                                    \n010450         \"185179172166160155150145140136132128125122119117115113\".\n010452     10 FILLER PIC X(54) VALUE                                    \n010454         \"111109108107106105104104103102102102101101101101101101\".\n010456     10 FILLER PIC X(39) VALUE                                    \n010458         \"101101101101101100100100100100100099099\".               \n010460     10 FILLER PIC X(54) VALUE                                    \n010462         \"846837828818808798789779769759749739729719709700690680\".\n010464     10 FILLER PIC X(54) VALUE                                    \n010466         \"670660651641631621612602592583573563554544535525516506\".\n010468     10 FILLER PIC X(54) VALUE                                    \n010470         \"496487477468458449439430420411401392382373364354345336\".\n010472     10 FILLER PIC X(54) VALUE                                    \n010474         \"327318310301292284275267259251243235227220212205197190\".\n010476     10 FILLER PIC X(54) VALUE                                    \n010478         \"183177170164158152147142137132128124121118115112110108\".\n010480     10 FILLER PIC X(54) VALUE                                    \n010482         \"106104103101100099099098097097096096096095095095095095\".\n010484     10 FILLER PIC X(39) VALUE                                    \n010486         \"095095095095095094094094094094093093093\".               \n010488     10 FILLER PIC X(54) VALUE                                    \n010490         \"846837828818808798789779769759749739729719709700690680\".\n010492     10 FILLER PIC X(54) VALUE                                    \n010494         \"670660651641631621612602592583573563554544535525515506\".\n010496     10 FILLER PIC X(54) VALUE                                    \n010498         \"496487477468458449439429420410401392382373363354345336\".\n010500     10 FILLER PIC X(54) VALUE                                    \n010502         \"327318309300292283275267258250242234226219211204196189\".\n010504     10 FILLER PIC X(54) VALUE                                    \n010506         \"182175168162156150144139134129125121117114111108105103\".\n010508     10 FILLER PIC X(54) VALUE                                    \n010510         \"101099098096095094093092092091091090090090089089089089\".\n010512     10 FILLER PIC X(39) VALUE                                    \n010514         \"089089089089089089089088088088088087087\".               \n010516     10 FILLER PIC X(54) VALUE                                    \n010518         \"846837828818808798788779769759749739729719709700690680\".\n010520     10 FILLER PIC X(54) VALUE                                    \n010522         \"670660651641631621612602592583573563554544535525515506\".\n010524     10 FILLER PIC X(54) VALUE                                    \n010526         \"496487477468458448439429420410401391382373363354345336\".\n010528     10 FILLER PIC X(54) VALUE                                    \n010530         \"327318309300291283274266258250241233226218210203195188\".\n010532     10 FILLER PIC X(54) VALUE                                    \n010534         \"181174167160154148142136131126122118114110107104101099\".\n010536     10 FILLER PIC X(54) VALUE                                    \n010538         \"097095093092090089088087087086085085085084084084084084\".\n010540     10 FILLER PIC X(39) VALUE                                    \n010542         \"084084083083083083083083083082082082081\".               \n010544     10 FILLER PIC X(54) VALUE                                    \n010546         \"846837828818808798788779769759749739729719709700690680\".\n010548     10 FILLER PIC X(54) VALUE                                    \n010550         \"670660651641631621611602592582573563554544535525515506\".\n010552     10 FILLER PIC X(54) VALUE                                    \n010554         \"496487477467458448439429420410401391382372363354345335\".\n010556     10 FILLER PIC X(54) VALUE                                    \n010558         \"326317309300291282274266257249241233225217209202194187\".\n010560     10 FILLER PIC X(54) VALUE                                    \n010562         \"179172165159152146140134129124119115111107104100098095\".\n010564     10 FILLER PIC X(54) VALUE                                    \n010566         \"093091089087086085084083082081080080080079079079079079\".\n010568     10 FILLER PIC X(39) VALUE                                    \n010570         \"078078078078078078078078077077077076076\".               \n010572     10 FILLER PIC X(54) VALUE                                    \n010574         \"846837828818808798788779769759749739729719709700690680\".\n010576     10 FILLER PIC X(54) VALUE                                    \n010578         \"670660650641631621611602592582573563554544534525515506\".\n010580     10 FILLER PIC X(54) VALUE                                    \n010582         \"496487477467458448439429420410401391382372363354344335\".\n010584     10 FILLER PIC X(54) VALUE                                    \n010586         \"326317308299291282274265257249240232224216209201193186\".\n010588     10 FILLER PIC X(54) VALUE                                    \n010590         \"178171164157151144138132127122117112108104100097094091\".\n010592     10 FILLER PIC X(54) VALUE                                    \n010594         \"089087085083082080079078077076076075075074074074074074\".\n010596     10 FILLER PIC X(39) VALUE                                    \n010598         \"074074074073073073073073073072072071071\".               \n010600     10 FILLER PIC X(54) VALUE                                    \n010602         \"846837828818808798788779769759749739729719709699690680\".\n010604     10 FILLER PIC X(54) VALUE                                    \n010606         \"670660650641631621611602592582573563554544534525515506\".\n010608     10 FILLER PIC X(54) VALUE                                    \n010610         \"496487477467458448439429420410400391382372363353344335\".\n010612     10 FILLER PIC X(54) VALUE                                    \n010614         \"326317308299290282273265256248240232224216208200192185\".\n010616     10 FILLER PIC X(54) VALUE                                    \n010618         \"177170163156149143137131125120115110105101098094091088\".\n010620     10 FILLER PIC X(54) VALUE                                    \n010622         \"086083081079078076075074073072072071070070070069069069\".\n010624     10 FILLER PIC X(39) VALUE                                    \n010626         \"069069069069069069069068068068067066066\".               \n010628     10 FILLER PIC X(54) VALUE                                    \n010630         \"846837828818808798788779769759749739729719709699690680\".\n010632     10 FILLER PIC X(54) VALUE                                    \n010634         \"670660650641631621611602592582573563554544534525515506\".\n010636     10 FILLER PIC X(54) VALUE                                    \n010638         \"496487477467458448439429419410400391381372363353344335\".\n010640     10 FILLER PIC X(54) VALUE                                    \n010642         \"326317308299290282273264256248240231223215207200192184\".\n010644     10 FILLER PIC X(54) VALUE                                    \n010646         \"177169162155148142135129123118113108103099095091088085\".\n010648     10 FILLER PIC X(54) VALUE                                    \n010650         \"083080078076074073071070069068068067066066066065065065\".\n010652     10 FILLER PIC X(39) VALUE                                    \n010654         \"065065065065065064064064064063063062061\".               \n010656     10 FILLER PIC X(54) VALUE                                    \n010658         \"846837828818808798788779769759749739729719709699690680\".\n010660     10 FILLER PIC X(54) VALUE                                    \n010662         \"670660650641631621611602592582573563554544534525515506\".\n010664     10 FILLER PIC X(54) VALUE                                    \n010666         \"496486477467458448439429419410400391381372363353344335\".\n010668     10 FILLER PIC X(54) VALUE                                    \n010670         \"326317308299290281273264256247239231223215207199191184\".\n010672     10 FILLER PIC X(54) VALUE                                    \n010674         \"176169161154147141134128122116111106101097093089086083\".\n010676     10 FILLER PIC X(54) VALUE                                    \n010678         \"080077075073071069068067066065064063063062062061061061\".\n010680     10 FILLER PIC X(39) VALUE                                    \n010682         \"061061061061061061060060060059058058057\".               \n010684     10 FILLER PIC X(54) VALUE                                    \n010686         \"846837828818808798788779769759749739729719709699690680\".\n010688     10 FILLER PIC X(54) VALUE                                    \n010690         \"670660650641631621611602592582573563553544534525515506\".\n010692     10 FILLER PIC X(54) VALUE                                    \n010694         \"496486477467458448439429419410400391381372362353344335\".\n010696     10 FILLER PIC X(54) VALUE                                    \n010698         \"325316307299290281273264256247239231223215207199191183\".\n010700     10 FILLER PIC X(54) VALUE                                    \n010702         \"175168161153146140133127121115109104099095091087083080\".\n010704     10 FILLER PIC X(54) VALUE                                    \n010706         \"077075072070068066065064062061060060059059058058058058\".\n010708     10 FILLER PIC X(39) VALUE                                    \n010710         \"057057057057057057057056056055055054053\".               \n010712     10 FILLER PIC X(54) VALUE                                    \n010714         \"846837828818808798788779769759749739729719709699690680\".\n010716     10 FILLER PIC X(54) VALUE                                    \n010718         \"670660650641631621611602592582573563553544534525515506\".\n010720     10 FILLER PIC X(54) VALUE                                    \n010722         \"496486477467458448438429419410400391381372362353344335\".\n010724     10 FILLER PIC X(54) VALUE                                    \n010726         \"325316307298290281272264255247239230222214206198190183\".\n010728     10 FILLER PIC X(54) VALUE                                    \n010730         \"175167160153146139132126119114108103098093089085081078\".\n010732     10 FILLER PIC X(54) VALUE                                    \n010734         \"075072070067065064062061059058057056056055055054054054\".\n010736     10 FILLER PIC X(39) VALUE                                    \n010738         \"054054054054054053053053052052051050049\".               \n010740     10 FILLER PIC X(54) VALUE                                    \n010742         \"846837828818808798788779769759749739729719709699690680\".\n010744     10 FILLER PIC X(54) VALUE                                    \n010746         \"670660650641631621611602592582573563553544534525515506\".\n010748     10 FILLER PIC X(54) VALUE                                    \n010750         \"496486477467458448438429419410400391381372362353344334\".\n010752     10 FILLER PIC X(54) VALUE                                    \n010754         \"325316307298290281272264255247238230222214206198190182\".\n010756     10 FILLER PIC X(54) VALUE                                    \n010758         \"174167159152145138131125119113107101096092087083079076\".\n010760     10 FILLER PIC X(54) VALUE                                    \n010762         \"073070067065063061059058057055054053053052052051051051\".\n010764     10 FILLER PIC X(39) VALUE                                    \n010766         \"051051051051051050050050049049048047046\".               \n010768     10 FILLER PIC X(54) VALUE                                    \n010770         \"846837828818808798788779769759749739729719709699690680\".\n010772     10 FILLER PIC X(54) VALUE                                    \n010774         \"670660650641631621611602592582573563553544534525515506\".\n010776     10 FILLER PIC X(54) VALUE                                    \n010778         \"496486477467458448438429419410400391381372362353344334\".\n010780     10 FILLER PIC X(54) VALUE                                    \n010782         \"325316307298289281272263255247238230222214206198190182\".\n010784     10 FILLER PIC X(54) VALUE                                    \n010786         \"174166159152144137131124118112106100095090086082078074\".\n010788     10 FILLER PIC X(54) VALUE                                    \n010790         \"071068065063061059057055054053052051050049049049048048\".\n010792     10 FILLER PIC X(39) VALUE                                    \n010794         \"048048048048048047047047046046045044043\".               \n010796     10 FILLER PIC X(54) VALUE                                    \n010798         \"846837828818808798788779769759749739729719709699690680\".\n010800     10 FILLER PIC X(54) VALUE                                    \n010802         \"670660650641631621611602592582573563553544534525515506\".\n010804     10 FILLER PIC X(54) VALUE                                    \n010806         \"496486477467458448438429419410400391381372362353344334\".\n010808     10 FILLER PIC X(54) VALUE                                    \n010810         \"325316307298289281272263255246238230222214206197189182\".\n010812     10 FILLER PIC X(54) VALUE                                    \n010814         \"174166159151144137130123117111105099094089085080076073\".\n010816     10 FILLER PIC X(54) VALUE                                    \n010818         \"069066064061059057055053052050049048047047046046046046\".\n010820     10 FILLER PIC X(39) VALUE                                    \n010822         \"045045045045045045044044044043042041040\".               \n010824     10 FILLER PIC X(54) VALUE                                    \n010826         \"846837828818808798788779769759749739729719709699690680\".\n010828     10 FILLER PIC X(54) VALUE                                    \n010830         \"670660650641631621611602592582573563553544534525515506\".\n010832     10 FILLER PIC X(54) VALUE                                    \n010834         \"496486477467458448438429419410400391381372362353343334\".\n010836     10 FILLER PIC X(54) VALUE                                    \n010838         \"325316307298289280272263255246238230222213205197189181\".\n010840     10 FILLER PIC X(54) VALUE                                    \n010842         \"174166158151143136129123116110104099093088084079075071\".\n010844     10 FILLER PIC X(54) VALUE                                    \n010846         \"068065062059057055053051050048047046045045044044043043\".\n010848     10 FILLER PIC X(39) VALUE                                    \n010850         \"043043043043043042042042041040039038037\".               \n010852     10 FILLER PIC X(54) VALUE                                    \n010854         \"846837828818808798788779769759749739729719709699690680\".\n010856     10 FILLER PIC X(54) VALUE                                    \n010858         \"670660650641631621611602592582573563553544534525515506\".\n010860     10 FILLER PIC X(54) VALUE                                    \n010862         \"496486477467458448438429419410400391381372362353343334\".\n010864     10 FILLER PIC X(54) VALUE                                    \n010866         \"325316307298289280272263255246238230221213205197189181\".\n010868     10 FILLER PIC X(54) VALUE                                    \n010870         \"173166158150143136129122116110104098092087083078074070\".\n010872     10 FILLER PIC X(54) VALUE                                    \n010874         \"067064061058055053051049048046045044043042042041041041\".\n010876     10 FILLER PIC X(39) VALUE                                    \n010878         \"041041041041040040040040039038037035034\".               \n010880     10 FILLER PIC X(54) VALUE                                    \n010882         \"846837828818808798788779769759749739729719709699690680\".\n010884     10 FILLER PIC X(54) VALUE                                    \n010886         \"670660650641631621611602592582573563553544534525515506\".\n010888     10 FILLER PIC X(54) VALUE                                    \n010890         \"496486477467458448438429419410400391381372362353343334\".\n010892     10 FILLER PIC X(54) VALUE                                    \n010894         \"325316307298289280272263255246238229221213205197189181\".\n010896     10 FILLER PIC X(54) VALUE                                    \n010898         \"173165158150143136129122115109103097092087082077073069\".\n010900     10 FILLER PIC X(54) VALUE                                    \n010902         \"066062059057054052050048046045043042041041040040039039\".\n010904     10 FILLER PIC X(39) VALUE                                    \n010906         \"039039039039038038038038037036035033032\".               \n010908     10 FILLER PIC X(54) VALUE                                    \n010910         \"846837828818808798788779769759749739729719709699690680\".\n010912     10 FILLER PIC X(54) VALUE                                    \n010914         \"670660650641631621611602592582573563553544534525515506\".\n010916     10 FILLER PIC X(54) VALUE                                    \n010918         \"496486477467458448438429419410400391381372362353343334\".\n010920     10 FILLER PIC X(54) VALUE                                    \n010922         \"325316307298289280272263254246238229221213205197189181\".\n010924     10 FILLER PIC X(54) VALUE                                    \n010926         \"173165157150143135128122115109102097091086081076072068\".\n010928     10 FILLER PIC X(54) VALUE                                    \n010930         \"065061058055053050048046045043042041040039038038038037\".\n010932     10 FILLER PIC X(39) VALUE                                    \n010934         \"037037037037037036036036035034033031030\".               \n010936     10 FILLER PIC X(54) VALUE                                    \n010938         \"846837828818808798788779769759749739729719709699690680\".\n010940     10 FILLER PIC X(54) VALUE                                    \n010942         \"670660650641631621611602592582573563553544534525515506\".\n010944     10 FILLER PIC X(54) VALUE                                    \n010946         \"496486477467458448438429419410400390381371362353343334\".\n010948     10 FILLER PIC X(54) VALUE                                    \n010950         \"325316307298289280271263254246238229221213205197189181\".\n010952     10 FILLER PIC X(54) VALUE                                    \n010954         \"173165157150142135128121115108102096091085080076072068\".\n010956     10 FILLER PIC X(54) VALUE                                    \n010958         \"064060057054052049047045043042041039038037037036036036\".\n010960     10 FILLER PIC X(39) VALUE                                    \n010962         \"036036035035035035035034033033031029028\".               \n010964     10 FILLER PIC X(54) VALUE                                    \n010966         \"846837828818808798788779769759749739729719709699690680\".\n010968     10 FILLER PIC X(54) VALUE                                    \n010970         \"670660650641631621611602592582573563553544534525515506\".\n010972     10 FILLER PIC X(54) VALUE                                    \n010974         \"496486477467458448438429419410400390381371362353343334\".\n010976     10 FILLER PIC X(54) VALUE                                    \n010978         \"325316307298289280271263254246238229221213205196188180\".\n010980     10 FILLER PIC X(54) VALUE                                    \n010982         \"173165157150142135128121114108102096090085080075071067\".\n010984     10 FILLER PIC X(54) VALUE                                    \n010986         \"063060056053051048046044042041039038037036035035035034\".\n010988     10 FILLER PIC X(39) VALUE                                    \n010990         \"036036035035035035035034033031030028026\".               \n010992     10 FILLER PIC X(54) VALUE                                    \n010994         \"846837828818808798788779769759749739729719709699690680\".\n010996     10 FILLER PIC X(54) VALUE                                    \n010998         \"670660650641631621611602592582573563553544534525515506\".\n011000     10 FILLER PIC X(54) VALUE                                    \n011002         \"496486477467458448438429419410400390381371362353343334\".\n011004     10 FILLER PIC X(54) VALUE                                    \n011006         \"325316307298289280271263254246237229221213205196188180\".\n011008     10 FILLER PIC X(54) VALUE                                    \n011010         \"173165157149142135128121114108101096090085080075070066\".\n011012     10 FILLER PIC X(54) VALUE                                    \n011014         \"063059056053050047045043041040038037036035034034033033\".\n011016     10 FILLER PIC X(39) VALUE                                    \n011018         \"033033033033033032032032031030028026025\".               \n011020     10 FILLER PIC X(54) VALUE                                    \n011022         \"846837828818808798788779769759749739729719709699690680\".\n011024     10 FILLER PIC X(54) VALUE                                    \n011026         \"670660650641631621611602592582573563553544534525515505\".\n011028     10 FILLER PIC X(54) VALUE                                    \n011030         \"496486477467458448438429419410400390381371362353343334\".\n011032     10 FILLER PIC X(54) VALUE                                    \n011034         \"325316307298289280271263254246237229221213205196188180\".\n011036     10 FILLER PIC X(54) VALUE                                    \n011038         \"173165157149142135128121114107101095090084079074070066\".\n011040     10 FILLER PIC X(54) VALUE                                    \n011042         \"062059055052049047045042041039037036035034033033032032\".\n011044     10 FILLER PIC X(39) VALUE                                    \n011046         \"032032032032032031031031030029027025023\".               \n011048     10 FILLER PIC X(54) VALUE                                    \n011050         \"846837828818808798788779769759749739729719709699690680\".\n011052     10 FILLER PIC X(54) VALUE                                    \n011054         \"670660650641631621611602592582573563553544534525515505\".\n011056     10 FILLER PIC X(54) VALUE                                    \n011058         \"496486477467458448438429419410400390381371362353343334\".\n011060     10 FILLER PIC X(54) VALUE                                    \n011062         \"325316307298289280271263254246237229221213205196188180\".\n011064     10 FILLER PIC X(54) VALUE                                    \n011066         \"172165157149142135127120114107101095089084079074070066\".\n011068     10 FILLER PIC X(54) VALUE                                    \n011070         \"062058055052049046044042040038037035034033033032032032\".\n011072     10 FILLER PIC X(39) VALUE                                    \n011074         \"031031031031031031030030029028026024021\".               \n011076     10 FILLER PIC X(54) VALUE                                    \n011078         \"846837828818808798788779769759749739729719709699690680\".\n011080     10 FILLER PIC X(54) VALUE                                    \n011082         \"670660650641631621611602592582573563553544534525515505\".\n011084     10 FILLER PIC X(54) VALUE                                    \n011086         \"496486477467457448438429419410400390381371362353343334\".\n011088     10 FILLER PIC X(54) VALUE                                    \n011090         \"325316307298289280271263254246237229221213205196188180\".\n011092     10 FILLER PIC X(54) VALUE                                    \n011094         \"172165157149142134127120114107101095089084079074069065\".\n011096     10 FILLER PIC X(54) VALUE                                    \n011098         \"061058054051049046044041040038036035034033032031031031\".\n011100     10 FILLER PIC X(39) VALUE                                    \n011102         \"031031031030030030030029028027026024021\".               \n011104     10 FILLER PIC X(54) VALUE                                    \n011106         \"846837828818808798788779769759749739729719709699690680\".\n011108     10 FILLER PIC X(54) VALUE                                    \n011110         \"670660650641631621611602592582573563553544534525515505\".\n011112     10 FILLER PIC X(54) VALUE                                    \n011114         \"496486477467457448438429419410400390381371362353343334\".\n011116     10 FILLER PIC X(54) VALUE                                    \n011118         \"325316307298289280271263254246237229221213205196188180\".\n011120     10 FILLER PIC X(54) VALUE                                    \n011122         \"172165157149142134127120114107101095089084079074069065\".\n011124     10 FILLER PIC X(54) VALUE                                    \n011126         \"061058054051048046043041039038036035033032032031031031\".\n011128     10 FILLER PIC X(39) VALUE                                    \n011130         \"030030030030030030029029028027025023021\".               \n011132     10 FILLER PIC X(54) VALUE                                    \n011134         \"846837828818808798788779769759749739729719709699690680\".\n011136     10 FILLER PIC X(54) VALUE                                    \n011138         \"670660650641631621611602592582573563553544534525515505\".\n011140     10 FILLER PIC X(54) VALUE                                    \n011142         \"496486477467457448438429419410400390381371362353343334\".\n011144     10 FILLER PIC X(54) VALUE                                    \n011146         \"325316307298289280271263254246237229221213205196188180\".\n011148     10 FILLER PIC X(54) VALUE                                    \n011150         \"172165157149142134127120114107101095089084079074069065\".\n011152     10 FILLER PIC X(54) VALUE                                    \n011154         \"061058054051048046043041039037036034033032032031031030\".\n011156     10 FILLER PIC X(39) VALUE                                    \n011158         \"030030030030030029029029028027025023021\".               \n011160     10 FILLER PIC X(54) VALUE                                    \n011162         \"846837828818808798788779769759749739729719709699690680\".\n011164     10 FILLER PIC X(54) VALUE                                    \n011166         \"670660650641631621611602592582573563553544534525515505\".\n011168     10 FILLER PIC X(54) VALUE                                    \n011170         \"496486477467457448438429419410400390381371362353343334\".\n011172     10 FILLER PIC X(54) VALUE                                    \n011174         \"325316307298289280271263254246237229221213205196188180\".\n011176     10 FILLER PIC X(54) VALUE                                    \n011178         \"172165157149142134127120114107101095089084078074069065\".\n011180     10 FILLER PIC X(54) VALUE                                    \n011182         \"061057054051048045043041039037036034033032031031030030\".\n011184     10 FILLER PIC X(39) VALUE                                    \n011186         \"030030030030029029029028028027025023020\".               \n011188     10 FILLER PIC X(54) VALUE                                    \n011190         \"846837828818808798788779769759749739729719709699690680\".\n011192     10 FILLER PIC X(54) VALUE                                    \n011194         \"670660650641631621611602592582573563553544534525515505\".\n011196     10 FILLER PIC X(54) VALUE                                    \n011198         \"496486477467457448438429419410400390381371362353343334\".\n011200     10 FILLER PIC X(54) VALUE                                    \n011202         \"325316307298289280271263254246237229221213204196188180\".\n011204     10 FILLER PIC X(54) VALUE                                    \n011206         \"172164157149142134127120113107101095089084078074069065\".\n011208     10 FILLER PIC X(54) VALUE                                    \n011210         \"061057054051048045043041039037036034033032031031030030\".\n011212     10 FILLER PIC X(39) VALUE                                    \n011214         \"030030030030029029029028028026025023020\".               \n011216     10 FILLER PIC X(54) VALUE                                    \n011218         \"846837828818808798788779769759749739729719709699690680\".\n011220     10 FILLER PIC X(54) VALUE                                    \n011222         \"670660650641631621611602592582573563553544534525515505\".\n011224     10 FILLER PIC X(54) VALUE                                    \n011226         \"496486477467457448438429419410400390381371362353343334\".\n011228     10 FILLER PIC X(54) VALUE                                    \n011230         \"325316307298289280271263254246237229221213204196188180\".\n011232     10 FILLER PIC X(54) VALUE                                    \n011234         \"172164157149142134127120113107101095089083078074069065\".\n011236     10 FILLER PIC X(54) VALUE                                    \n011238         \"061057054051048045043041039037035034033032031031030030\".\n011240     10 FILLER PIC X(39) VALUE                                    \n011242         \"030030030029029029029028027026025022020\".               \n011244     10 FILLER PIC X(54) VALUE                                    \n011246         \"846837828818808798788779769759749739729719709699690680\".\n011248     10 FILLER PIC X(54) VALUE                                    \n011250         \"670660650641631621611602592582573563553544534525515505\".\n011252     10 FILLER PIC X(54) VALUE                                    \n011254         \"496486477467457448438429419410400390381371362353343334\".\n011256     10 FILLER PIC X(54) VALUE                                    \n011258         \"325316307298289280271263254246237229221213204196188180\".\n011260     10 FILLER PIC X(54) VALUE                                    \n011262         \"172164157149142134127120113107101095089083078073069065\".\n011264     10 FILLER PIC X(54) VALUE                                    \n011266         \"061057054051048045043041039037035034033032031030030030\".\n011268     10 FILLER PIC X(39) VALUE                                    \n011270         \"030030029029029029028028027026024022020\".               \n011272     10 FILLER PIC X(54) VALUE                                    \n011274         \"846837828818808798788779769759749739729719709699690680\".\n011276     10 FILLER PIC X(54) VALUE                                    \n011278         \"670660650641631621611602592582573563553544534525515505\".\n011280     10 FILLER PIC X(54) VALUE                                    \n011282         \"496486477467457448438429419410400390381371362353343334\".\n011284     10 FILLER PIC X(54) VALUE                                    \n011286         \"325316307298289280271263254246237229221213204196188180\".\n011288     10 FILLER PIC X(54) VALUE                                    \n011290         \"172164157149142134127120113107101095089083078073069065\".\n011292     10 FILLER PIC X(54) VALUE                                    \n011294         \"061057054051048045043040038037035034033032031030030030\".\n011296     10 FILLER PIC X(39) VALUE                                    \n011298         \"029029029029029029028028027026024022020\".               \n011300     10 FILLER PIC X(54) VALUE                                    \n011302         \"846837828818808798788779769759749739729719709699690680\".\n011304     10 FILLER PIC X(54) VALUE                                    \n011306         \"670660650641631621611602592582573563553544534525515505\".\n011308     10 FILLER PIC X(54) VALUE                                    \n011310         \"496486477467457448438429419410400390381371362353343334\".\n011312     10 FILLER PIC X(54) VALUE                                    \n011314         \"325316307298289280271263254246237229221213204196188180\".\n011316     10 FILLER PIC X(54) VALUE                                    \n011318         \"172164157149142134127120113107100094089083078073069064\".\n011320     10 FILLER PIC X(54) VALUE                                    \n011322         \"061057053050047045042040038036035034032031031030030029\".\n011324     10 FILLER PIC X(39) VALUE                                    \n011326         \"029029029029029028028028027026024022019\".               \n011328     10 FILLER PIC X(54) VALUE                                    \n011330         \"846837828818808798788779769759749739729719709699690680\".\n011332     10 FILLER PIC X(54) VALUE                                    \n011334         \"670660650641631621611602592582573563553544534525515505\".\n011336     10 FILLER PIC X(54) VALUE                                    \n011338         \"496486477467457448438429419410400390381371362353343334\".\n011340     10 FILLER PIC X(54) VALUE                                    \n011342         \"325316307298289280271263254246237229221213204196188180\".\n011344     10 FILLER PIC X(54) VALUE                                    \n011346         \"172164157149141134127120113107100094089083078073069064\".\n011348     10 FILLER PIC X(54) VALUE                                    \n011350         \"060057053050047044042040038036035033032031030030029029\".\n011352     10 FILLER PIC X(39) VALUE                                    \n011354         \"029029029028028028028027026025024021019\".               \n011356     10 FILLER PIC X(54) VALUE                                    \n011358         \"846837828818808798788779769759749739729719709699690680\".\n011360     10 FILLER PIC X(54) VALUE                                    \n011362         \"670660650641631621611602592582573563553544534525515505\".\n011364     10 FILLER PIC X(54) VALUE                                    \n011366         \"496486477467457448438429419410400390381371362353343334\".\n011368     10 FILLER PIC X(54) VALUE                                    \n011370         \"325316307298289280271263254246237229221213204196188180\".\n011372     10 FILLER PIC X(54) VALUE                                    \n011374         \"172164157149141134127120113107100094088083078073068064\".\n011376     10 FILLER PIC X(54) VALUE                                    \n011378         \"060056053050047044042040038036034033032031030029029029\".\n011380     10 FILLER PIC X(39) VALUE                                    \n011382         \"028028028028028028027027026025023021018\".               \n011384     10 FILLER PIC X(54) VALUE                                    \n011386         \"846837828818808798788779769759749739729719709699690680\".\n011388     10 FILLER PIC X(54) VALUE                                    \n011390         \"670660650641631621611602592582573563553544534525515505\".\n011392     10 FILLER PIC X(54) VALUE                                    \n011394         \"496486477467457448438429419410400390381371362353343334\".\n011396     10 FILLER PIC X(54) VALUE                                    \n011398         \"325316307298289280271263254246237229221213204196188180\".\n011400     10 FILLER PIC X(54) VALUE                                    \n011402         \"172164156149141134127120113106100094088083077073068064\".\n011404     10 FILLER PIC X(54) VALUE                                    \n011406         \"060056052049046044041039037035033032031030029028028028\".\n011408     10 FILLER PIC X(39) VALUE                                    \n011410         \"028028027027027027026026025024022020018\".               \n011412     10 FILLER PIC X(54) VALUE                                    \n011414         \"846837828818808798788779769759749739729719709699690680\".\n011416     10 FILLER PIC X(54) VALUE                                    \n011418         \"670660650641631621611602592582573563553544534525515505\".\n011420     10 FILLER PIC X(54) VALUE                                    \n011422         \"496486477467457448438429419410400390381371362353343334\".\n011424     10 FILLER PIC X(54) VALUE                                    \n011426         \"325316307298289280271263254246237229221212204196188180\".\n011428     10 FILLER PIC X(54) VALUE                                    \n011430         \"172164156149141134127120113106100094088082077072068063\".\n011432     10 FILLER PIC X(54) VALUE                                    \n011434         \"059055052049046043040038036034033031030029028027027027\".\n011436     10 FILLER PIC X(39) VALUE                                    \n011438         \"027026026026026026025025024023021019016\".               \n011440     10 FILLER PIC X(54) VALUE                                    \n011442         \"846837828818808798788779769759749739729719709699690680\".\n011444     10 FILLER PIC X(54) VALUE                                    \n011446         \"670660650641631621611602592582573563553544534525515505\".\n011448     10 FILLER PIC X(54) VALUE                                    \n011450         \"496486477467457448438429419410400390381371362353343334\".\n011452     10 FILLER PIC X(54) VALUE                                    \n011454         \"325316307298289280271263254245237229221212204196188180\".\n011456     10 FILLER PIC X(54) VALUE                                    \n011458         \"172164156149141134126119113106100093088082077072067063\".\n011460     10 FILLER PIC X(54) VALUE                                    \n011462         \"058055051048045042039037035033031030028027026026025025\".\n011464     10 FILLER PIC X(39) VALUE                                    \n011466         \"025025025024024024024023022021019017014\".               \n011468     10 FILLER PIC X(54) VALUE                                    \n011470         \"846837828818808798788779769759749739729719709699690680\".\n011472     10 FILLER PIC X(54) VALUE                                    \n011474         \"670660650641631621611602592582573563553544534525515505\".\n011476     10 FILLER PIC X(54) VALUE                                    \n011478         \"496486477467457448438429419410400390381371362353343334\".\n011480     10 FILLER PIC X(54) VALUE                                    \n011482         \"325316307298289280271263254245237229221212204196188180\".\n011484     10 FILLER PIC X(54) VALUE                                    \n011486         \"172164156148141134126119112106099093087082076071066062\".\n011488     10 FILLER PIC X(54) VALUE                                    \n011490         \"058054050047044041038036033031029028026025024024023023\".\n011492     10 FILLER PIC X(39) VALUE                                    \n011494         \"023023022022022022021021020019017013011\".               \n011496     10 FILLER PIC X(54) VALUE                                    \n011498         \"846837828818808798788779769759749739729719709699690680\".\n011500     10 FILLER PIC X(54) VALUE                                    \n011502         \"670660650641631620611602592582573563553544534525515505\".\n011504     10 FILLER PIC X(54) VALUE                                    \n011506         \"496486477467457448438429419410400390381371362353343334\".\n011508     10 FILLER PIC X(54) VALUE                                    \n011510         \"325316307298288279271263254245237229220212204196188180\".\n011512     10 FILLER PIC X(54) VALUE                                    \n011514         \"172164156148141133126119112105099093087081076071066061\".\n011516     10 FILLER PIC X(54) VALUE                                    \n011518         \"057053049046043040037034032030028026025023022021021021\".\n011520     10 FILLER PIC X(39) VALUE                                    \n011522         \"020020020020020019019018018016014011010\".               \n011524                                                                  \n011526   05  WS-RMD-LEF-TABLE-2-2022 REDEFINES RMD-LEF-TABLE-2-2022.    \n011528       10  WS-RMD-LEF-TBL-2-2022-REC OCCURS 121 TIMES.            \n011530           15  WS-RMD-TBL2-2022-LEF  PIC 999 OCCURS 121 TIMES.    \n011532                                                                  \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    1,701 lines from 4062 to 5762.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 11, "total_chunks": 55, "start_line": 4062, "end_line": 5762, "line_count": 1701}

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
- Source code length: 129131 characters

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
CHUNK 11 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 4062 to 5762 (1,701 lines)
Chunk Tokens (estimated): ~31,847
Actual Input Tokens: 33,253 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 4062-5762 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 11 of 55 chunks
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
      The source code below is only CHUNK 11 of 55.


=============================================================================
CHUNK 11 SOURCE CODE (Lines 4062-5762)
=============================================================================

```cobol
008132 01  RMD-LEF-TABLE-2-2022-X.                                      
008134   05  RMD-LEF-TABLE-2-2022.                                      
008136     10 FILLER PIC X(54) VALUE                                    
008138         "919914910905901897894890887884882879877875873871869868".
008140     10 FILLER PIC X(54) VALUE                                    
008142         "866865864862861860859859858857856856855854854853853853".
008144     10 FILLER PIC X(54) VALUE                                    
008146         "852852852851851851850850850850849849849849849848848848".
008148     10 FILLER PIC X(54) VALUE                                    
008150         "848848848848848847847847847847847847847847847847847847".
008152     10 FILLER PIC X(54) VALUE                                    
008154         "847846846846846846846846846846846846846846846846846846".
008156     10 FILLER PIC X(54) VALUE                                    
008158         "846846846846846846846846846846846846846846846846846846".
008160     10 FILLER PIC X(39) VALUE                                    
008162         "846846846846846846846846846846846846846".               
008164     10 FILLER PIC X(54) VALUE                                    
008166         "914909904900895891888884881878875872870867865863861860".
008168     10 FILLER PIC X(54) VALUE                                    
008170         "858857855854853852851850849848847847846846845845844844".
008172     10 FILLER PIC X(54) VALUE                                    
008174         "843843843842842842841841841841840840840840840840839839".
008176     10 FILLER PIC X(54) VALUE                                    
008178         "839839839839839839838838838838838838838838838838838838".
008180     10 FILLER PIC X(54) VALUE                                    
008182         "838838838838838838838838838838838837837837837837837837".
008184     10 FILLER PIC X(54) VALUE                                    
008186         "837837837837837837837837837837837837837837837837837837".
008188     10 FILLER PIC X(39) VALUE                                    
008190         "837837837837837837837837837837837837837".               
008192     10 FILLER PIC X(54) VALUE                                    
008194         "910904899894890885881878874871868865862860857855853851".
008196     10 FILLER PIC X(54) VALUE                                    
008198         "850848847845844843842841840839838838837836836835835834".
008200     10 FILLER PIC X(54) VALUE                                    
008202         "834833833833832832832831831831831831830830830830830830".
008204     10 FILLER PIC X(54) VALUE                                    
008206         "829829829829829829829829829829828828828828828828828828".
008208     10 FILLER PIC X(54) VALUE                                    
008210         "828828828828828828828828828828828828828828828828828828".
008212     10 FILLER PIC X(54) VALUE                                    
008214         "828828828828828828828828828828828828828828828828828828".
008216     10 FILLER PIC X(39) VALUE                                    
008218         "828828828828828828828828828828828828828".               
008220     10 FILLER PIC X(54) VALUE                                    
008222         "905900894889884880876871868864861858855852850847845843".
008224     10 FILLER PIC X(54) VALUE                                    
008226         "841840838837835834833832831830829828828827826826825825".
008228     10 FILLER PIC X(54) VALUE                                    
008230         "824824823823823822822822822821821821821821820820820820".
008232     10 FILLER PIC X(54) VALUE                                    
008234         "820820819819819819819819819819819819819819818818818818".
008236     10 FILLER PIC X(54) VALUE                                    
008238         "818818818818818818818818818818818818818818818818818818".
008240     10 FILLER PIC X(54) VALUE                                    
008242         "818818818818818818818818818818818818818818818818818818".
008244     10 FILLER PIC X(39) VALUE                                    
008246         "818818818818818818818818818818818818818".               
008248     10 FILLER PIC X(54) VALUE                                    
008250         "901895890884879874870866862858854851848845842840837835".
008252     10 FILLER PIC X(54) VALUE                                    
008254         "833831830828827825824823822821820819818818817816816815".
008256     10 FILLER PIC X(54) VALUE                                    
008258         "815814814814813813813812812812811811811811811810810810".
008260     10 FILLER PIC X(54) VALUE                                    
008262         "810810810810809809809809809809809809809809809809809808".
008264     10 FILLER PIC X(54) VALUE                                    
008266         "809808808808808808808808808808808808808808808808808808".
008268     10 FILLER PIC X(54) VALUE                                    
008270         "808808808808808808808808808808808808808808808808808808".
008272     10 FILLER PIC X(39) VALUE                                    
008274         "808808808808808808808808808808808808808".               
008276     10 FILLER PIC X(54) VALUE                                    
008278         "897891886880874869865860856852848844841838835832830827".
008280     10 FILLER PIC X(54) VALUE                                    
008282         "825823822820818817816814813812811810809809808807807806".
008284     10 FILLER PIC X(54) VALUE                                    
008286         "805805804804804803803803802802802802801801801801801800".
008288     10 FILLER PIC X(54) VALUE                                    
008290         "800800800800800800799799799799799799799799799799799798".
008292     10 FILLER PIC X(54) VALUE                                    
008294         "799799799799799798798798798798798798798798798798798798".
008296     10 FILLER PIC X(54) VALUE                                    
008298         "798798798798798798798798798798798798798798798798798798".
008300     10 FILLER PIC X(39) VALUE                                    
008302         "798798798798798798798798798798798798798".               
008304     10 FILLER PIC X(54) VALUE                                    
008306         "894888881876870865859855850846842838834831828825822820".
008308     10 FILLER PIC X(54) VALUE                                    
008310         "817815813812810808807806804803802801800799799798797797".
008312     10 FILLER PIC X(54) VALUE                                    
008314         "796795795795794794793793793792792792792791791791791791".
008316     10 FILLER PIC X(54) VALUE                                    
008318         "790790790790790790790790789789789789789789789789789789".
008320     10 FILLER PIC X(54) VALUE                                    
008322         "789789789789789789789789789789789789789788788788788788".
008324     10 FILLER PIC X(54) VALUE                                    
008326         "788788788788788788788788788788788788788788788788788788".
008328     10 FILLER PIC X(39) VALUE                                    
008330         "788788788788788788788788788788788788788".               
008332     10 FILLER PIC X(54) VALUE                                    
008334         "890884878871866860855849845840836832828824821818815812".
008336     10 FILLER PIC X(54) VALUE                                    
008338         "810807805803802800798797796794793792791790789789788787".
008340     10 FILLER PIC X(54) VALUE                                    
008342         "787786786785785784784783783783782782782782781781781781".
008344     10 FILLER PIC X(54) VALUE                                    
008346         "781781780780780780780780780780779779779779779779779779".
008348     10 FILLER PIC X(54) VALUE                                    
008350         "779779779779779779779779779779779779779779779779779779".
008352     10 FILLER PIC X(54) VALUE                                    
008354         "779779779779779779779779779779779779779779779779779779".
008356     10 FILLER PIC X(39) VALUE                                    
008358         "779779779779779779779779779779779779779".               
008360     10 FILLER PIC X(54) VALUE                                    
008362         "887881874868862856850845839835830826822818814811808805".
008364     10 FILLER PIC X(54) VALUE                                    
008366         "802800798795793792790788787786784783782781780779779778".
008368     10 FILLER PIC X(54) VALUE                                    
008370         "777777776776775775774774773773773773772772772772771771".
008372     10 FILLER PIC X(54) VALUE                                    
008374         "771771771770770770770770770770770770769769769769769769".
008376     10 FILLER PIC X(54) VALUE                                    
008378         "769769769769769769769769769769769769769769769769769769".
008380     10 FILLER PIC X(54) VALUE                                    
008382         "769769769769769769769769769769769769769769769769769769".
008384     10 FILLER PIC X(39) VALUE                                    
008386         "769769769769769769769769769769769769769".               
008388     10 FILLER PIC X(54) VALUE                                    
008390         "884878871864858852846840835829825820816812808804801798".
008392     10 FILLER PIC X(54) VALUE                                    
008394         "795792790788785783782780778777776774773772771770770769".
008396     10 FILLER PIC X(54) VALUE                                    
008398         "768767767766766765765764764764763763763762762762762761".
008400     10 FILLER PIC X(54) VALUE                                    
008402         "761761761761761760760760760760760760760760759759759759".
008404     10 FILLER PIC X(54) VALUE                                    
008406         "759759759759759759759759759759759759759759759759759759".
008408     10 FILLER PIC X(54) VALUE                                    
008410         "759759759759759759759759759759759759759759759759759759".
008412     10 FILLER PIC X(39) VALUE                                    
008414         "759759759759759759759759759759759759759".               
008416     10 FILLER PIC X(54) VALUE                                    
008418         "882875868861854848842836830825819815810806802798794791".
008420     10 FILLER PIC X(54) VALUE                                    
008422         "788785782780778775773772770768767766764763762761760760".
008424     10 FILLER PIC X(54) VALUE                                    
008426         "759758757757756756755755754754754753753753752752752752".
008428     10 FILLER PIC X(54) VALUE                                    
008430         "751751751751751751750750750750750750750750750750749749".
008432     10 FILLER PIC X(54) VALUE                                    
008434         "749749749749749749749749749749749749749749749749749749".
008436     10 FILLER PIC X(54) VALUE                                    
008438         "749749749749749749749749749749749749749749749749749749".
008440     10 FILLER PIC X(39) VALUE                                    
008442         "749749749749749749749749749749749749749".               
008444     10 FILLER PIC X(54) VALUE                                    
008446         "879872865858851844838832826820815809805800796792788784".
008448     10 FILLER PIC X(54) VALUE                                    
008450         "781778775772770468765764762760758757756755753752751750".
008452     10 FILLER PIC X(54) VALUE                                    
008454         "750749748747747746746745745744744744743743743742742742".
008456     10 FILLER PIC X(54) VALUE                                    
008458         "742742741741741741741741740740740740740740740740740740".
008460     10 FILLER PIC X(54) VALUE                                    
008462         "739739739739739739739739739739739739739739739739739739".
008464     10 FILLER PIC X(54) VALUE                                    
008466         "739739739739739739739739739739739739739739739739739739".
008468     10 FILLER PIC X(39) VALUE                                    
008470         "739739739739739739739739739739739739739".               
008472     10 FILLER PIC X(54) VALUE                                    
008474         "877870862855848841834828822816810805799795790786782778".
008476     10 FILLER PIC X(54) VALUE                                    
008478         "774771768765762760758756754752750749747746745743742741".
008480     10 FILLER PIC X(54) VALUE                                    
008482         "740740739738737737736736735735734734734733733733732732".
008484     10 FILLER PIC X(54) VALUE                                    
008486         "732732732731731731731731731730730730730730730730730730".
008488     10 FILLER PIC X(54) VALUE                                    
008490         "730730730729729729729729729729729729729729729729729729".
008492     10 FILLER PIC X(54) VALUE                                    
008494         "729729729729729729729729729729729729729729729729729729".
008496     10 FILLER PIC X(39) VALUE                                    
008498         "729729729729729729729729729729729729729".               
008500     10 FILLER PIC X(54) VALUE                                    
008502         "875867860852845838831824818812806800795790785780776772".
008504     10 FILLER PIC X(54) VALUE                                    
008506         "768764761758755752750748746744742740739737736735733732".
008508     10 FILLER PIC X(54) VALUE                                    
008510         "731731730729728728727726726725725724724724723723723723".
008512     10 FILLER PIC X(54) VALUE                                    
008514         "722722722722721721721721721721721720720720720720720720".
008516     10 FILLER PIC X(54) VALUE                                    
008518         "720720720720720720719719719719719719719719719719719719".
008520     10 FILLER PIC X(54) VALUE                                    
008522         "719719719719719719719719719719719719719719719719719719".
008524     10 FILLER PIC X(39) VALUE                                    
008526         "719719719719719719719719719719719719719".               
008528     10 FILLER PIC X(54) VALUE                                    
008530         "873865857850842835828821814808802796790785780775770766".
008532     10 FILLER PIC X(54) VALUE                                    
008534         "762758754751748745742740738736734732730729727726725724".
008536     10 FILLER PIC X(54) VALUE                                    
008538         "722721721720719718718717716716715715715714714713713713".
008540     10 FILLER PIC X(54) VALUE                                    
008542         "713712712712712712711711711711711711711710710710710710".
008544     10 FILLER PIC X(54) VALUE                                    
008546         "710710710710710710710710710710709709709709709709709709".
008548     10 FILLER PIC X(54) VALUE                                    
008550         "709709709709709709709709709709709709709709709709709709".
008552     10 FILLER PIC X(39) VALUE                                    
008554         "709709709709709709709709709709709709709".               
008556     10 FILLER PIC X(54) VALUE                                    
008558         "871863855847840832825818811804798792786780775770765760".
008560     10 FILLER PIC X(54) VALUE                                    
008562         "756752748744741738735733730728726724722720719717716715".
008564     10 FILLER PIC X(54) VALUE                                    
008566         "714713712711710709708708707706706705705705704704704703".
008568     10 FILLER PIC X(54) VALUE                                    
008570         "703703702702702702702701701701701701701701701700700700".
008572     10 FILLER PIC X(54) VALUE                                    
008574         "700700700700700700700700700700700700700700700700699699".
008576     10 FILLER PIC X(54) VALUE                                    
008578         "699699699699699699699699699699699699699699699699699699".
008580     10 FILLER PIC X(39) VALUE                                    
008582         "699699699699699699699699699699699699699".               
008584     10 FILLER PIC X(54) VALUE                                    
008586         "869861853845837830822815808801794788782776770765760755".
008588     10 FILLER PIC X(54) VALUE                                    
008590         "750746742738734731728725723720718716714712710709707706".
008592     10 FILLER PIC X(54) VALUE                                    
008594         "705704703702701700699698698697697696696695695694694694".
008596     10 FILLER PIC X(54) VALUE                                    
008598         "693693693693692692692692692691691691691691691691691690".
008600     10 FILLER PIC X(54) VALUE                                    
008602         "690690690690690690690690690690690690690690690690690690".
008604     10 FILLER PIC X(54) VALUE                                    
008606         "690690690690690690690690690690690690690690690690690690".
008608     10 FILLER PIC X(39) VALUE                                    
008610         "689689689689689689689689689690690690690".               
008612     10 FILLER PIC X(54) VALUE                                    
008614         "868860851843835827820812805798791784778772766760755750".
008616     10 FILLER PIC X(54) VALUE                                    
008618         "745740736732728725721718715713710708706704702700699697".
008620     10 FILLER PIC X(54) VALUE                                    
008622         "696695694693692691690689688688687687686686685685684684".
008624     10 FILLER PIC X(54) VALUE                                    
008626         "684683683683683682682682682682682681681681681681681681".
008628     10 FILLER PIC X(54) VALUE                                    
008630         "681681680680680680680680680680680680680680680680680680".
008632     10 FILLER PIC X(54) VALUE                                    
008634         "680680680680680680680680680680680680680680680680680680".
008636     10 FILLER PIC X(39) VALUE                                    
008638         "680680680680680680680680680680680680680".               
008640     10 FILLER PIC X(54) VALUE                                    
008642         "866858850841833825817810802795788781774768762756750745".
008644     10 FILLER PIC X(54) VALUE                                    
008646         "740735730726722718715711708705703700698696694692690689".
008648     10 FILLER PIC X(54) VALUE                                    
008650         "687686685684683682681680679679678677677676676675675674".
008652     10 FILLER PIC X(54) VALUE                                    
008654         "674674674673673673673672672672672672672671671671671671".
008656     10 FILLER PIC X(54) VALUE                                    
008658         "671671671671671670670670670670670670670670670670670670".
008660     10 FILLER PIC X(54) VALUE                                    
008662         "670670670670670670670670670670670670670670670670670670".
008664     10 FILLER PIC X(39) VALUE                                    
008666         "670670670670670670670670670670670670670".               
008668     10 FILLER PIC X(54) VALUE                                    
008670         "865857848840831823815807800792785778771764758752746740".
008672     10 FILLER PIC X(54) VALUE                                    
008674         "735730725720716712708705701698695693690688686684682681".
008676     10 FILLER PIC X(54) VALUE                                    
008678         "679677676675674673672671670669669668667667666666665665".
008680     10 FILLER PIC X(54) VALUE                                    
008682         "665664664664663663663663662662662662662662662661661661".
008684     10 FILLER PIC X(54) VALUE                                    
008686         "661661661661661661661661661660660660660660660660660660".
008688     10 FILLER PIC X(54) VALUE                                    
008690         "660660660660660660660660660660660660660660660660660660".
008692     10 FILLER PIC X(39) VALUE                                    
008694         "660660660660660660660660660660660660660".               
008696     10 FILLER PIC X(54) VALUE                                    
008698         "864855847838830822813805798790782775768761754748742736".
008700     10 FILLER PIC X(54) VALUE                                    
008702         "730725715710706702698695694691688685683680678676674672".
008704     10 FILLER PIC X(54) VALUE                                    
008706         "671669668666665664663662661660659659658657657656656655".
008708     10 FILLER PIC X(54) VALUE                                    
008710         "655655654654654654653653653653652652652652652652652651".
008712     10 FILLER PIC X(54) VALUE                                    
008714         "651651651651651651651651651651651651651651651650650650".
008716     10 FILLER PIC X(54) VALUE                                    
008718         "650650650650650650650650650650650650650650650650650650".
008720     10 FILLER PIC X(39) VALUE                                    
008722         "650650650650650650650650650650650650650".               
008724     10 FILLER PIC X(54) VALUE                                    
008726         "862854845837828820812803795788780772765758751744738732".
008728     10 FILLER PIC X(54) VALUE                                    
008730         "726720715710705700696692688685681678675673670668666664".
008732     10 FILLER PIC X(54) VALUE                                    
008734         "662661659658656655654653652651650650649648648647647646".
008736     10 FILLER PIC X(54) VALUE                                    
008738         "646645645645644644644643643643643643642642642642642642".
008740     10 FILLER PIC X(54) VALUE                                    
008742         "642642641641641641641641641641641641641641641641641641".
008744     10 FILLER PIC X(54) VALUE                                    
008746         "641641641641641641641641641641641641641641641641641641".
008748     10 FILLER PIC X(39) VALUE                                    
008750         "641641641641641641641641641641641641641".               
008752     10 FILLER PIC X(54) VALUE                                    
008754         "861853844835827818810802793785778770762755748741734728".
008756     10 FILLER PIC X(54) VALUE                                    
008758         "722716710705700695690686682678675671668666663660658656".
008760     10 FILLER PIC X(54) VALUE                                    
008762         "654652651649648646645644643642641640640639638638637637".
008764     10 FILLER PIC X(54) VALUE                                    
008766         "636636635635635634634634634633633633633633632632632632".
008768     10 FILLER PIC X(54) VALUE                                    
008770         "632632632632632631631631631631631631631631631631631631".
008772     10 FILLER PIC X(54) VALUE                                    
008774         "631631631631631631631631631631631631631631631631631631".
008776     10 FILLER PIC X(39) VALUE                                    
008778         "631631631631631631631631631631631631631".               
008780     10 FILLER PIC X(54) VALUE                                    
008782         "860852843834825817808800792783775768760752745738731725".
008784     10 FILLER PIC X(54) VALUE                                    
008786         "718712706700695690685680676672668665662658655653651648".
008788     10 FILLER PIC X(54) VALUE                                    
008790         "646644642641639638636635634633632631630630629628628627".
008792     10 FILLER PIC X(54) VALUE                                    
008794         "627626626625625625624624624624623623623623623623622622".
008796     10 FILLER PIC X(54) VALUE                                    
008798         "622622622622622622622622621621621621621621621621621621".
008800     10 FILLER PIC X(54) VALUE                                    
008802         "621621621621621621621621621621621621621621621621621621".
008804     10 FILLER PIC X(39) VALUE                                    
008806         "621621621621621621621621621621621621621".               
008808     10 FILLER PIC X(54) VALUE                                    
008810         "859851842833824816807798790782773765758750742735728721".
008812     10 FILLER PIC X(54) VALUE                                    
008814         "715708702696690685680675671666662658655652649646643641".
008816     10 FILLER PIC X(54) VALUE                                    
008818         "638636634633631629628627625624623622621621620619619618".
008820     10 FILLER PIC X(54) VALUE                                    
008822         "617617616616616615615615614614614614613613613613613613".
008824     10 FILLER PIC X(54) VALUE                                    
008826         "613612612612612612612612612612612612612612611611611611".
008828     10 FILLER PIC X(54) VALUE                                    
008830         "611611611611611611611611611611611611611611611611611611".
008832     10 FILLER PIC X(39) VALUE                                    
008834         "611611611611611611611611611611611611611".               
008836     10 FILLER PIC X(54) VALUE                                    
008838         "859850841832823814806797788780772764756748740733725718".
008840     10 FILLER PIC X(54) VALUE                                    
008842         "711705698692686680675670665661656652649645642639636633".
008844     10 FILLER PIC X(54) VALUE                                    
008846         "631628626624623621619618617615614613612612611610609609".
008848     10 FILLER PIC X(54) VALUE                                    
008850         "608608607607606606605605605605604604604604603603603603".
008852     10 FILLER PIC X(54) VALUE                                    
008854         "603603603603602602602602602602602602602602602602602602".
008856     10 FILLER PIC X(54) VALUE                                    
008858         "602602602602602602602602602602602602602602602602602602".
008860     10 FILLER PIC X(39) VALUE                                    
008862         "602602602602602602602602602602602602602".               
008864     10 FILLER PIC X(54) VALUE                                    
008866         "858849840831822813804796787778770762754746738730723715".
008868     10 FILLER PIC X(54) VALUE                                    
008870         "708701695688682676671665660655651646642639635632629626".
008872     10 FILLER PIC X(54) VALUE                                    
008874         "623621619616615613611610608607606605603603602601600599".
008876     10 FILLER PIC X(54) VALUE                                    
008878         "599598598597597596596596595595595595594594594594594593".
008880     10 FILLER PIC X(54) VALUE                                    
008882         "593593593593593593593593592592592592592592592592592592".
008884     10 FILLER PIC X(54) VALUE                                    
008886         "592592592592592592592592592592592592592592592592592592".
008888     10 FILLER PIC X(39) VALUE                                    
008890         "592592592592592592592592592592592592592".               
008892     10 FILLER PIC X(54) VALUE                                    
008894         "857848839830821812803794786777768760752744736728720713".
008896     10 FILLER PIC X(54) VALUE                                    
008898         "705698691685678672666661655650645641637632629625622619".
008900     10 FILLER PIC X(54) VALUE                                    
008902         "616613611609607605603601600598597596595594593592591590".
008904     10 FILLER PIC X(54) VALUE                                    
008906         "590589588588587587587586586586585585585585584584584584".
008908     10 FILLER PIC X(54) VALUE                                    
008910         "584584583583583583583583583583583583583583582582582582".
008912     10 FILLER PIC X(54) VALUE                                    
008914         "582582582582582582582582582582582582582582582582582582".
008916     10 FILLER PIC X(39) VALUE                                    
008918         "582582582582582582582582582582582582582".               
008920     10 FILLER PIC X(54) VALUE                                    
008922         "856847838829820811802793784776767758750742734726718710".
008924     10 FILLER PIC X(54) VALUE                                    
008926         "703695688681675668662656651645640635631627623619615612".
008928     10 FILLER PIC X(54) VALUE                                    
008930         "609606603601599597595593591590588587586585584583582581".
008932     10 FILLER PIC X(54) VALUE                                    
008934         "580580579579578578577577576576576575575575575575574574".
008936     10 FILLER PIC X(54) VALUE                                    
008938         "574574574574574573573573573573573573573573573573573573".
008940     10 FILLER PIC X(54) VALUE                                    
008942         "573573573573573573573573573573573573573573573573573573".
008944     10 FILLER PIC X(39) VALUE                                    
008946         "573573573573573573573573573573573573573".               
008948     10 FILLER PIC X(54) VALUE                                    
008950         "856847838828819810801792783774766757749740732724716708".
008952     10 FILLER PIC X(54) VALUE                                    
008954         "700693685678671665658652646641635630626621617613609605".
008956     10 FILLER PIC X(54) VALUE                                    
008958         "602599596594591589587585583581580579577576575574573572".
008960     10 FILLER PIC X(54) VALUE                                    
008962         "571571570569569568568567567567566566566565565565565565".
008964     10 FILLER PIC X(54) VALUE                                    
008966         "565564564564564564564564564564563563563563563563563563".
008968     10 FILLER PIC X(54) VALUE                                    
008970         "563563563563563563563563563563563563563563563563563563".
008972     10 FILLER PIC X(39) VALUE                                    
008974         "563563563563563563563563563563563563563".               
008976     10 FILLER PIC X(54) VALUE                                    
008978         "855846837828818809800791782773764756747739730722714706".
008980     10 FILLER PIC X(54) VALUE                                    
008982         "698690683675668662655649642637631626620616611607603599".
008984     10 FILLER PIC X(54) VALUE                                    
008986         "595592589586584581579577575573572570569567566565564563".
008988     10 FILLER PIC X(54) VALUE                                    
008990         "562562561560560559559558558557557557556556556556555555".
008992     10 FILLER PIC X(54) VALUE                                    
008994         "555555555555554554554554554554554554554554554554554554".
008996     10 FILLER PIC X(54) VALUE                                    
008998         "554553553553553553553553553553553553553553553553553553".
009000     10 FILLER PIC X(39) VALUE                                    
009002         "553553553553553553553553553553553553553".               
009004     10 FILLER PIC X(54) VALUE                                    
009006         "854846836827818809799790781772763755746737729720712704".
009008     10 FILLER PIC X(54) VALUE                                    
009010         "696688680673666658652645639632627621616611606601597593".
009012     10 FILLER PIC X(54) VALUE                                    
009014         "589586582579576574571569567565563562560559558556555554".
009016     10 FILLER PIC X(54) VALUE                                    
009018         "553553552551550550549549548548548547547547546546546546".
009020     10 FILLER PIC X(54) VALUE                                    
009022         "545545545545545545545545544544544544544544544544544544".
009024     10 FILLER PIC X(54) VALUE                                    
009026         "544544544544544544544544544544544544544544544544544544".
009028     10 FILLER PIC X(39) VALUE                                    
009030         "544544544544544544544544544544544544544".               
009032     10 FILLER PIC X(54) VALUE                                    
009034         "854845836826817808799789780771762753745736727719710702".
009036     10 FILLER PIC X(54) VALUE                                    
009038         "694686678670663656649642635629623617611606601596591587".
009040     10 FILLER PIC X(54) VALUE                                    
009042         "583579576572569567564562559557555554552550549548547546".
009044     10 FILLER PIC X(54) VALUE                                    
009046         "545544543542541541540540539539538538537537537537536536".
009048     10 FILLER PIC X(54) VALUE                                    
009050         "536536536535535535535535535535535535535535535534534534".
009052     10 FILLER PIC X(54) VALUE                                    
009054         "534534534534534534534534534534534534534534534534534534".
009056     10 FILLER PIC X(39) VALUE                                    
009058         "534534534534534534534534534534534534534".               
009060     10 FILLER PIC X(54) VALUE                                    
009062         "853845835826816807798789779770761752743735726717709700".
009064     10 FILLER PIC X(54) VALUE                                    
009066         "692684676668660653646639632625619613607601596591586581".
009068     10 FILLER PIC X(54) VALUE                                    
009070         "577573569566563560557554552549547545544542541539538537".
009072     10 FILLER PIC X(54) VALUE                                    
009074         "536535534533532532531530530529529528528528527527527527".
009076     10 FILLER PIC X(54) VALUE                                    
009078         "526526526526526526526525525525525525525525525525525525".
009080     10 FILLER PIC X(54) VALUE                                    
009082         "525525525525525525525525525525525525525525525525525525".
009084     10 FILLER PIC X(39) VALUE                                    
009086         "525525525525525525525525525525525525525".               
009088     10 FILLER PIC X(54) VALUE                                    
009090         "853844835825816807797788779770760751742733725716707699".
009092     10 FILLER PIC X(54) VALUE                                    
009094         "690682674666658651643636629622615609603597591586581576".
009096     10 FILLER PIC X(54) VALUE                                    
009098         "572567563559556553550547544542540537536534532531529528".
009100     10 FILLER PIC X(54) VALUE                                    
009102         "527526525524523522522521521520520519519518518518517517".
009104     10 FILLER PIC X(54) VALUE                                    
009106         "517517517516516516516516516516516516515515515515515515".
009108     10 FILLER PIC X(54) VALUE                                    
009110         "515515515515515515515515515515515515515515515515515515".
009112     10 FILLER PIC X(39) VALUE                                    
009114         "515515515515515515515515515515515515515".               
009116     10 FILLER PIC X(54) VALUE                                    
009118         "853844834825815806797787778769760750741732724715706697".
009120     10 FILLER PIC X(54) VALUE                                    
009122         "689680672664656648641633626619612605599593587581576571".
009124     10 FILLER PIC X(54) VALUE                                    
009126         "566562557553550546543540537534532530528526524522521520".
009128     10 FILLER PIC X(54) VALUE                                    
009130         "518517516515514513513512511511510510509509509508508508".
009132     10 FILLER PIC X(54) VALUE                                    
009134         "508507507507507507506506506506506506506506506506506506".
009136     10 FILLER PIC X(54) VALUE                                    
009138         "506506506506506506506506506506506506506505505505505505".
009140     10 FILLER PIC X(39) VALUE                                    
009142         "505505505505505505505505505505505505505".               
009144     10 FILLER PIC X(54) VALUE                                    
009146         "852843834824815805796787777768759750740731722714705696".
009148     10 FILLER PIC X(54) VALUE                                    
009150         "687679671662654646638631623616609602595589583577572566".
009152     10 FILLER PIC X(54) VALUE                                    
009154         "561556552547543540536533530527524522520518516514513511".
009156     10 FILLER PIC X(54) VALUE                                    
009158         "510509507506505505504503502502501501500500499499499498".
009160     10 FILLER PIC X(54) VALUE                                    
009162         "498498498497497497497497497497497496496496496496496496".
009164     10 FILLER PIC X(54) VALUE                                    
009166         "496496496496496496496496496496496496496496496496496496".
009168     10 FILLER PIC X(39) VALUE                                    
009170         "496496496496496496496496496496496496496".               
009172     10 FILLER PIC X(54) VALUE                                    
009174         "852843833824814804795786777767758749740731721713704695".
009176     10 FILLER PIC X(54) VALUE                                    
009178         "686677669661652644636628621613606599592586579573567562".
009180     10 FILLER PIC X(54) VALUE                                    
009182         "556551546542538534530526523520517515512510508506504503".
009184     10 FILLER PIC X(54) VALUE                                    
009186         "501500499498497496495494493493492491491490490490489489".
009188     10 FILLER PIC X(54) VALUE                                    
009190         "489488488488488488487487487487487487487487487487487487".
009192     10 FILLER PIC X(54) VALUE                                    
009194         "486486486486486486486486486486486486486486486486486486".
009196     10 FILLER PIC X(39) VALUE                                    
009198         "486486486486486486486486486486486486486".               
009200     10 FILLER PIC X(54) VALUE                                    
009202         "852843833823814804795786776767757748739730721712703694".
009204     10 FILLER PIC X(54) VALUE                                    
009206         "685676668659651642634626619611603596589582576569563557".
009208     10 FILLER PIC X(54) VALUE                                    
009210         "552546541536532528524520516513510507505502500498496495".
009212     10 FILLER PIC X(54) VALUE                                    
009214         "493491490489488487486485484483483482482481481480480479".
009216     10 FILLER PIC X(54) VALUE                                    
009218         "479479479478478478478478478477477477477477477477477477".
009220     10 FILLER PIC X(54) VALUE                                    
009222         "477477477477477477477477477477477477477477477477477477".
009224     10 FILLER PIC X(39) VALUE                                    
009226         "477477477477477477477477477477477477477".               
009228     10 FILLER PIC X(54) VALUE                                    
009230         "851842833823814804795785776766757747738729720711702693".
009232     10 FILLER PIC X(54) VALUE                                    
009234         "684675666658649641633624616609601594586579572566559553".
009236     10 FILLER PIC X(54) VALUE                                    
009238         "547542536531527522518514510507503500497495492490488486".
009240     10 FILLER PIC X(54) VALUE                                    
009242         "485483482480479478477476475474474473472472471471470470".
009244     10 FILLER PIC X(54) VALUE                                    
009246         "470469469469469469468468468468468468468468467467467467".
009248     10 FILLER PIC X(54) VALUE                                    
009250         "467467467467467467467467467467467467467467467467467467".
009252     10 FILLER PIC X(39) VALUE                                    
009254         "467467467467467467467467467467467467467".               
009256     10 FILLER PIC X(54) VALUE                                    
009258         "851842832823813804794785775766756747737728719710701692".
009260     10 FILLER PIC X(54) VALUE                                    
009262         "683674665656648639631623615607599591584576569563556550".
009264     10 FILLER PIC X(54) VALUE                                    
009266         "543538532527522517512508504500497493490488485483480478".
009268     10 FILLER PIC X(54) VALUE                                    
009270         "477475473472471469468467466465465464463463462462461461".
009272     10 FILLER PIC X(54) VALUE                                    
009274         "460460460459459459459459459458458458458458458458458458".
009276     10 FILLER PIC X(54) VALUE                                    
009278         "458458458458458458458458458458458458458458458457457457".
009280     10 FILLER PIC X(39) VALUE                                    
009282         "457457457457457457457457457457457457457".               
009284     10 FILLER PIC X(54) VALUE                                    
009286         "851842832822813803794784775765756746737728718709700691".
009288     10 FILLER PIC X(54) VALUE                                    
009290         "682673664655646638629621613605597589581574567560553546".
009292     10 FILLER PIC X(54) VALUE                                    
009294         "540534528522517512507502498494490487484481478475473471".
009296     10 FILLER PIC X(54) VALUE                                    
009298         "469467465463462461460458457457456455454454453452452451".
009300     10 FILLER PIC X(54) VALUE                                    
009302         "451451450450450450449449449449449449449448448448448448".
009304     10 FILLER PIC X(54) VALUE                                    
009306         "448448448448448448448448448448448448448448448448448448".
009308     10 FILLER PIC X(39) VALUE                                    
009310         "448448448448448448448448448448448448448".               
009312     10 FILLER PIC X(54) VALUE                                    
009314         "850841832822813803793784774765755746736727718708699690".
009316     10 FILLER PIC X(54) VALUE                                    
009318         "681672663654645636628619611603595587579571564557550543".
009320     10 FILLER PIC X(54) VALUE                                    
009322         "536530524518512507502497492488484480477474471468465463".
009324     10 FILLER PIC X(54) VALUE                                    
009326         "461459457455454452451450449448447446445444444443443442".
009328     10 FILLER PIC X(54) VALUE                                    
009330         "442441441441440440440440439439439439439439439439439439".
009332     10 FILLER PIC X(54) VALUE                                    
009334         "439439438438438438438438438438438438438438438438438438".
009336     10 FILLER PIC X(39) VALUE                                    
009338         "438438438438438438438438438438438438438".               
009340     10 FILLER PIC X(54) VALUE                                    
009342         "850841831822812803793783774764755745736726717708698689".
009344     10 FILLER PIC X(54) VALUE                                    
009346         "680671662653644635627618610601593585577569562554547540".
009348     10 FILLER PIC X(54) VALUE                                    
009350         "533526520514508502497492487483478474471467464461458456".
009352     10 FILLER PIC X(54) VALUE                                    
009354         "453451449447445444443441440439438437436435435434433433".
009356     10 FILLER PIC X(54) VALUE                                    
009358         "432432432431431431430430430430430430429429429429429429".
009360     10 FILLER PIC X(54) VALUE                                    
009362         "429429429429429429429429429429429429429429429429429429".
009364     10 FILLER PIC X(39) VALUE                                    
009366         "429429429429429429429429429429429429429".               
009368     10 FILLER PIC X(54) VALUE                                    
009370         "850841831822812802793783773764754745735726716707698688".
009372     10 FILLER PIC X(54) VALUE                                    
009374         "679670661652643634625617608600591583575567559552544537".
009376     10 FILLER PIC X(54) VALUE                                    
009378         "530523516510504498492487482477473468464461457454451448".
009380     10 FILLER PIC X(54) VALUE                                    
009382         "446443441439437436434433431430429428427426426425424424".
009384     10 FILLER PIC X(54) VALUE                                    
009386         "423423422422422421421421421420420420420420420420420419".
009388     10 FILLER PIC X(54) VALUE                                    
009390         "419419419419419419419419419419419419419419419419419419".
009392     10 FILLER PIC X(39) VALUE                                    
009394         "419419419419419419419419419419419419419".               
009396     10 FILLER PIC X(54) VALUE                                    
009398         "850841831821812802792783773764754744735725716706697688".
009400     10 FILLER PIC X(54) VALUE                                    
009402         "679669660651642633624615607598590581573565557549542534".
009404     10 FILLER PIC X(54) VALUE                                    
009406         "527520513507500494488483477472467463459455451447444441".
009408     10 FILLER PIC X(54) VALUE                                    
009410         "438436434431429428426424423422421419418418417416415415".
009412     10 FILLER PIC X(54) VALUE                                    
009414         "414414413413412412412411411411411411410410410410410410".
009416     10 FILLER PIC X(54) VALUE                                    
009418         "410410410410410410410410410410410410410410410410410410".
009420     10 FILLER PIC X(39) VALUE                                    
009422         "410410410410410410410410410410410410410".               
009424     10 FILLER PIC X(54) VALUE                                    
009426         "849840831821811802792782773763754744734725715706697687".
009428     10 FILLER PIC X(54) VALUE                                    
009430         "678669659650641632623614606597588580572563555547540532".
009432     10 FILLER PIC X(54) VALUE                                    
009434         "524517510503497490484478473467462457453449445441438434".
009436     10 FILLER PIC X(54) VALUE                                    
009438         "431429426424422420418416415413412411410409408407406406".
009440     10 FILLER PIC X(54) VALUE                                    
009442         "405404404403403403402402402401401401401401401401400400".
009444     10 FILLER PIC X(54) VALUE                                    
009446         "400400400400400400400400400400400400400400400400400400".
009448     10 FILLER PIC X(39) VALUE                                    
009450         "400400400400400400400400400400400400400".               
009452     10 FILLER PIC X(54) VALUE                                    
009454         "849840831821811802792782773763753744734724715705696687".
009456     10 FILLER PIC X(54) VALUE                                    
009458         "677668659650640631622613605596587579570562554545537530".
009460     10 FILLER PIC X(54) VALUE                                    
009462         "522515507500493487480474468463457452448443439435431428".
009464     10 FILLER PIC X(54) VALUE                                    
009466         "425422419416414412410408406405404402401400399398397397".
009468     10 FILLER PIC X(54) VALUE                                    
009470         "396395395394394393393393392392392392392391391391391391".
009472     10 FILLER PIC X(54) VALUE                                    
009474         "391391391391391391391391391391390390390390390390390390".
009476     10 FILLER PIC X(39) VALUE                                    
009478         "390390390390390390390390390390390390390".               
009480     10 FILLER PIC X(54) VALUE                                    
009482         "849840830821811801792782772763753743734724715705696686".
009484     10 FILLER PIC X(54) VALUE                                    
009486         "677667658649640630621612603595586577569560552544536528".
009488     10 FILLER PIC X(54) VALUE                                    
009490         "520512505497490484477471464459453448443438433429425421".
009492     10 FILLER PIC X(54) VALUE                                    
009494         "418415412409407404402400398397395394393391390389388388".
009496     10 FILLER PIC X(54) VALUE                                    
009498         "387386386385385384384383383383383382382382382382382381".
009500     10 FILLER PIC X(54) VALUE                                    
009502         "381381381381381381381381381381381381381381381381381381".
009504     10 FILLER PIC X(39) VALUE                                    
009506         "381381381381381381381381381381381381381".               
009508     10 FILLER PIC X(54) VALUE                                    
009510         "849840830821811801791782772762753743733724714705695686".
009512     10 FILLER PIC X(54) VALUE                                    
009514         "676667657648639630621612603594585576567559550542534526".
009516     10 FILLER PIC X(54) VALUE                                    
009518         "518510502495488481474467461455449443438433428423419415".
009520     10 FILLER PIC X(54) VALUE                                    
009522         "412408405402399397395392390389387386384383382381380379".
009524     10 FILLER PIC X(54) VALUE                                    
009526         "378377377376375375375374374373373373373373372372372372".
009528     10 FILLER PIC X(54) VALUE                                    
009530         "372372372372372372372372372372371371371371371371371371".
009532     10 FILLER PIC X(39) VALUE                                    
009534         "371371371371371371371371371371371371371".               
009536     10 FILLER PIC X(54) VALUE                                    
009538         "849840830820811801791781772762752743733723714704695685".
009540     10 FILLER PIC X(54) VALUE                                    
009542         "676666657648638629620611602593584575566558549541532524".
009544     10 FILLER PIC X(54) VALUE                                    
009546         "516508500492485478471464457451445439433428423418414409".
009548     10 FILLER PIC X(54) VALUE                                    
009550         "406402398395392390387385383381379377376375373372371370".
009552     10 FILLER PIC X(54) VALUE                                    
009554         "369368368367366366365365365364364364363363363363363363".
009556     10 FILLER PIC X(54) VALUE                                    
009558         "363362362362362362362362362362362362362362362362362362".
009560     10 FILLER PIC X(39) VALUE                                    
009562         "362362362362362362362362362362362362362".               
009564     10 FILLER PIC X(54) VALUE                                    
009566         "848840830820810801791781772762752742733723713704694685".
009568     10 FILLER PIC X(54) VALUE                                    
009570         "675666656647638628619610601592583574565556548539531522".
009572     10 FILLER PIC X(54) VALUE                                    
009574         "514506498490483475468461454447441435429423418413408404".
009576     10 FILLER PIC X(54) VALUE                                    
009578         "400396392389386383380377375373371369368366365364362361".
009580     10 FILLER PIC X(54) VALUE                                    
009582         "360360359358357357356356355355355354354354354354353353".
009584     10 FILLER PIC X(54) VALUE                                    
009586         "353353353353353353353353353353353353353353353353353353".
009588     10 FILLER PIC X(39) VALUE                                    
009590         "353353353353353353353353353353353353353".               
009592     10 FILLER PIC X(54) VALUE                                    
009594         "848839830820810801791781771762752742732723713704694684".
009596     10 FILLER PIC X(54) VALUE                                    
009598         "675665656647637628619609600591582573564555547538529521".
009600     10 FILLER PIC X(54) VALUE                                    
009602         "513504496488480473465458451444438431425419414408403399".
009604     10 FILLER PIC X(54) VALUE                                    
009606         "394390386382379376373370368366363362360358357355354353".
009608     10 FILLER PIC X(54) VALUE                                    
009610         "352351350349349348347347346346346345345345345344344344".
009612     10 FILLER PIC X(54) VALUE                                    
009614         "344344344344344344343343343343343343343343343343343343".
009616     10 FILLER PIC X(39) VALUE                                    
009618         "343343343343343343343343343343343343343".               
009620     10 FILLER PIC X(54) VALUE                                    
009622         "848839830820810800791781771761752742732723713703694684".
009624     10 FILLER PIC X(54) VALUE                                    
009626         "674665655646637627618609599590581572563554546537528520".
009628     10 FILLER PIC X(54) VALUE                                    
009630         "511503495486478471463456448441434428421415409404399394".
009632     10 FILLER PIC X(54) VALUE                                    
009634         "389384380376373369366363361358356354352350349347346345".
009636     10 FILLER PIC X(54) VALUE                                    
009638         "343342341341340339339338337337337336336336335335335335".
009640     10 FILLER PIC X(54) VALUE                                    
009642         "335335335334334334334334334334334334334334334334334334".
009644     10 FILLER PIC X(39) VALUE                                    
009646         "334334334334334334334334334334334334334".               
009648     10 FILLER PIC X(54) VALUE                                    
009650         "848839829820810800790781771761751742732722713703693684".
009652     10 FILLER PIC X(54) VALUE                                    
009654         "674665655646636627617608599590580571562553545536527518".
009656     10 FILLER PIC X(54) VALUE                                    
009658         "510501493485477469461453446438431425418412406400394389".
009660     10 FILLER PIC X(54) VALUE                                    
009662         "384379375371367363360357354351349346344342341339338336".
009664     10 FILLER PIC X(54) VALUE                                    
009666         "335334333332331330330329329328328327327327326326326326".
009668     10 FILLER PIC X(54) VALUE                                    
009670         "326325325325325325325325325325325325325325325325325325".
009672     10 FILLER PIC X(39) VALUE                                    
009674         "325325325325325325325325325325325325325".               
009676     10 FILLER PIC X(54) VALUE                                    
009678         "848839829820810800790781771761751742732722712703693683".
009680     10 FILLER PIC X(54) VALUE                                    
009682         "674664655645636626617608598589580571562553544535526517".
009684     10 FILLER PIC X(54) VALUE                                    
009686         "509500491483475467459451443436429422415408402396390384".
009688     10 FILLER PIC X(54) VALUE                                    
009690         "379374369365361357353350347344342339337335333331330328".
009692     10 FILLER PIC X(54) VALUE                                    
009694         "327326324324323322321320320319319318318318317317317317".
009696     10 FILLER PIC X(54) VALUE                                    
009698         "317316316316316316316316316316316316316316316316316316".
009700     10 FILLER PIC X(39) VALUE                                    
009702         "316316316316316316316316316316316316316".               
009704     10 FILLER PIC X(54) VALUE                                    
009706         "848839829819810800790780771761751741732722712702693683".
009708     10 FILLER PIC X(54) VALUE                                    
009710         "674664654645635626616607598588579570561552543534525516".
009712     10 FILLER PIC X(54) VALUE                                    
009714         "507499490482473465457449441434426419412405398392386380".
009716     10 FILLER PIC X(54) VALUE                                    
009718         "375369365360355351348344341338335332330327325323322320".
009720     10 FILLER PIC X(54) VALUE                                    
009722         "319317316315314313312312311311310310309309309308308308".
009724     10 FILLER PIC X(54) VALUE                                    
009726         "308307307307307307307307307307307307307307307307307307".
009728     10 FILLER PIC X(39) VALUE                                    
009730         "307307307307307307307307307307307307306".               
009732     10 FILLER PIC X(54) VALUE                                    
009734         "848839829819810800790780770761751741731722712702693683".
009736     10 FILLER PIC X(54) VALUE                                    
009738         "673664654645635625616607597588579569560551542533524515".
009740     10 FILLER PIC X(54) VALUE                                    
009742         "506498489480472463455447439431424416409402395389382376".
009744     10 FILLER PIC X(54) VALUE                                    
009746         "371365360355350346342338334331328325323320318316314312".
009748     10 FILLER PIC X(54) VALUE                                    
009750         "311309308307306305304303303302301301300300300299299299".
009752     10 FILLER PIC X(54) VALUE                                    
009754         "299299298298298298298298298298298298298298298298298298".
009756     10 FILLER PIC X(39) VALUE                                    
009758         "298298298298298298298298298298298298298".               
009760     10 FILLER PIC X(54) VALUE                                    
009762         "848839829819809800790780770761751741731721712702692683".
009764     10 FILLER PIC X(54) VALUE                                    
009766         "673663654644635625616606597587578569560550541532523514".
009768     10 FILLER PIC X(54) VALUE                                    
009770         "505497488479471462454445437429422414407399392386379373".
009772     10 FILLER PIC X(54) VALUE                                    
009774         "367361355350345341336332328325322319316313311309307305".
009776     10 FILLER PIC X(54) VALUE                                    
009778         "303301300299298297296295294293293292292291291291290290".
009780     10 FILLER PIC X(54) VALUE                                    
009782         "290290290290289289289289289289289289289289289289289289".
009784     10 FILLER PIC X(39) VALUE                                    
009786         "289289289289289289289289289289289289289".               
009788     10 FILLER PIC X(54) VALUE                                    
009790         "847839829819809800790780770760751741731721712702692682".
009792     10 FILLER PIC X(54) VALUE                                    
009794         "673663654644634625615606596587578568559550541532522513".
009796     10 FILLER PIC X(54) VALUE                                    
009798         "505496487478469461452444436428420412404397390383376369".
009800     10 FILLER PIC X(54) VALUE                                    
009802         "363357351346341336331327323319315312309306304301299297".
009804     10 FILLER PIC X(54) VALUE                                    
009806         "295294292291290288287287286285284284283283282282282282".
009808     10 FILLER PIC X(54) VALUE                                    
009810         "281281281281281281280280280280280280280280280280280280".
009812     10 FILLER PIC X(39) VALUE                                    
009814         "280280280280280280280280280280280280280".               
009816     10 FILLER PIC X(54) VALUE                                    
009818         "847838829819809799790780770760750741731721711702692682".
009820     10 FILLER PIC X(54) VALUE                                    
009822         "672663653644634624615605596587577568559549540531522513".
009824     10 FILLER PIC X(54) VALUE                                    
009826         "504495486477468460451443434426418410402395387380373366".
009828     10 FILLER PIC X(54) VALUE                                    
009830         "360353348342336331326322317313310306303300297294292290".
009832     10 FILLER PIC X(54) VALUE                                    
009834         "288286284283282280279278278277276275275274274274273273".
009836     10 FILLER PIC X(54) VALUE                                    
009838         "273273272272272272272272272272271271271271271271271271".
009840     10 FILLER PIC X(39) VALUE                                    
009842         "271271271271271271271271271271271271271".               
009844     10 FILLER PIC X(54) VALUE                                    
009846         "847838829819809799790780770760750741731721711701692682".
009848     10 FILLER PIC X(54) VALUE                                    
009850         "672663653643634624615605596586577567558549540530521512".
009852     10 FILLER PIC X(54) VALUE                                    
009854         "503494485476467458450441433424416408400392385377370363".
009856     10 FILLER PIC X(54) VALUE                                    
009858         "357350344338332327322317312308304300297294291288285283".
009860     10 FILLER PIC X(54) VALUE                                    
009862         "281279277275274273271270269269268267267266266265265264".
009864     10 FILLER PIC X(54) VALUE                                    
009866         "264264264264263263263263263263263263263263263263263263".
009868     10 FILLER PIC X(39) VALUE                                    
009870         "263263263263263263263263263263263262262".               
009872     10 FILLER PIC X(54) VALUE                                    
009874         "847838829819809799789780770760750740731721711701692682".
009876     10 FILLER PIC X(54) VALUE                                    
009878         "672662653643634624614605595586576567558548539530521511".
009880     10 FILLER PIC X(54) VALUE                                    
009882         "502493484475466457449440431423415406398390383375368361".
009884     10 FILLER PIC X(54) VALUE                                    
009886         "354347341334328323317312308303299295291287284281279276".
009888     10 FILLER PIC X(54) VALUE                                    
009890         "274272270268266265264262261260260259258258257257256256".
009892     10 FILLER PIC X(54) VALUE                                    
009894         "256256255255255255255255255254254254254254254254254254".
009896     10 FILLER PIC X(39) VALUE                                    
009898         "254254254254254254254254253254254254254".               
009900     10 FILLER PIC X(54) VALUE                                    
009902         "847838829819809799789780770760750740730721711701691682".
009904     10 FILLER PIC X(54) VALUE                                    
009906         "672662653643633624614605595586576567557548539529520511".
009908     10 FILLER PIC X(54) VALUE                                    
009910         "502493483474465457448439430422413405397389381373366358".
009912     10 FILLER PIC X(54) VALUE                                    
009914         "351344338331325319313308303298294289285282278275272269".
009916     10 FILLER PIC X(54) VALUE                                    
009918         "267265262261259257256255253252252251250250249249248248".
009920     10 FILLER PIC X(54) VALUE                                    
009922         "247247247247247246246246246246246246246246246246246246".
009924     10 FILLER PIC X(39) VALUE                                    
009926         "246246246246246246246246246246245245245".               
009928     10 FILLER PIC X(54) VALUE                                    
009930         "847838828819809799789779770760750740730721711701691682".
009932     10 FILLER PIC X(54) VALUE                                    
009934         "672662652643633623614604595585576566557548538529520510".
009936     10 FILLER PIC X(54) VALUE                                    
009938         "501492483474465456447438429421412404395387379371363356".
009940     10 FILLER PIC X(54) VALUE                                    
009942         "349342335328322315310304299294289284280276272269266263".
009944     10 FILLER PIC X(54) VALUE                                    
009946         "260258255253252250248247246245244243242241241240240240".
009948     10 FILLER PIC X(54) VALUE                                    
009950         "239239239238238238238238238238238238237237237237237237".
009952     10 FILLER PIC X(39) VALUE                                    
009954         "237237237237237237237237237237237237237".               
009956     10 FILLER PIC X(54) VALUE                                    
009958         "847838828819809799789779770760750740730720711701691681".
009960     10 FILLER PIC X(54) VALUE                                    
009962         "672662652643633623614604595585575566557547538528519510".
009964     10 FILLER PIC X(54) VALUE                                    
009966         "501491482473464455446437428419411402394386377369362354".
009968     10 FILLER PIC X(54) VALUE                                    
009970         "346339332325319312306300295289284280275271267263260257".
009972     10 FILLER PIC X(54) VALUE                                    
009974         "254251249246244243241239238237236235234233233232232231".
009976     10 FILLER PIC X(54) VALUE                                    
009978         "231231230230230230230230229229229229229229229229229229".
009980     10 FILLER PIC X(39) VALUE                                    
009982         "229229229229229229229229229229229229229".               
009984     10 FILLER PIC X(54) VALUE                                    
009986         "847838828819809799789779769760750740730720711701691681".
009988     10 FILLER PIC X(54) VALUE                                    
009990         "672662652642633623613604594585575566556547537528519509".
009992     10 FILLER PIC X(54) VALUE                                    
009994         "500491482472463454445436427418410401393384376368360352".
009996     10 FILLER PIC X(54) VALUE                                    
009998         "344337330323316309303297291285280275270266262258254251".
010000     10 FILLER PIC X(54) VALUE                                    
010002         "248245242240237235234232231229228227226226225224224223".
010004     10 FILLER PIC X(54) VALUE                                    
010006         "223223222222222222222221221221221221221221221221221221".
010008     10 FILLER PIC X(39) VALUE                                    
010010         "221221221221221221221221221221221221220".               
010012     10 FILLER PIC X(54) VALUE                                    
010014         "847838828819809799789779769760750740730720710701691681".
010016     10 FILLER PIC X(54) VALUE                                    
010018         "671662652642633623613604594585575565556547537528518509".
010020     10 FILLER PIC X(54) VALUE                                    
010022         "500490481472463454444435426418409400391383375366358350".
010024     10 FILLER PIC X(54) VALUE                                    
010026         "342335327320313306300294287282276271266261257253249245".
010028     10 FILLER PIC X(54) VALUE                                    
010030         "242239236233231229227225223222221220219218217216216215".
010032     10 FILLER PIC X(54) VALUE                                    
010034         "215215214214214214213213213213213213213213213213213213".
010036     10 FILLER PIC X(39) VALUE                                    
010038         "213213213213213213213213213212212212212".               
010040     10 FILLER PIC X(54) VALUE                                    
010042         "847838828818809799789779769759750740730720710701691681".
010044     10 FILLER PIC X(54) VALUE                                    
010046         "671662652642632623613603594584575565556546537527518509".
010048     10 FILLER PIC X(54) VALUE                                    
010050         "499490481471462453444435426417408399390382373365357349".
010052     10 FILLER PIC X(54) VALUE                                    
010054         "341333325318311304297291284278272267262257252248243240".
010056     10 FILLER PIC X(54) VALUE                                    
010058         "236233230227224222220218216215213212211210209209208207".
010060     10 FILLER PIC X(54) VALUE                                    
010062         "207207206206206206205205205205205205205205205205205205".
010064     10 FILLER PIC X(39) VALUE                                    
010066         "205204204204204204204204204204204204204".               
010068     10 FILLER PIC X(54) VALUE                                    
010070         "847838828818809799789779769759750740730720710700691681".
010072     10 FILLER PIC X(54) VALUE                                    
010074         "671661652642632623613603594584575565556546537527518508".
010076     10 FILLER PIC X(54) VALUE                                    
010078         "499490480471462452443434425416407398389381372364355347".
010080     10 FILLER PIC X(54) VALUE                                    
010082         "339331323316309301294288281275269263258253248243239234".
010084     10 FILLER PIC X(54) VALUE                                    
010086         "231227224221218215213211209207206205204203202201200200".
010088     10 FILLER PIC X(54) VALUE                                    
010090         "199199198198198197197197197197197197197196196196196196".
010092     10 FILLER PIC X(39) VALUE                                    
010094         "196196196196196196196196196196196196196".               
010096     10 FILLER PIC X(54) VALUE                                    
010098         "847838828818809799789779769759749740730720710700691681".
010100     10 FILLER PIC X(54) VALUE                                    
010102         "671661652642632622613603594584574565555546536527517508".
010104     10 FILLER PIC X(54) VALUE                                    
010106         "499489480470461452443433424415406397388380371362354346".
010108     10 FILLER PIC X(54) VALUE                                    
010110         "338330322314307299292285279272266260254249243239234229".
010112     10 FILLER PIC X(54) VALUE                                    
010114         "225222218215212209206204202200199197196195194193192192".
010116     10 FILLER PIC X(54) VALUE                                    
010118         "191191190190190189189189189189189189188188188188188188".
010120     10 FILLER PIC X(39) VALUE                                    
010122         "188188188188188188188188188188188188188".               
010124     10 FILLER PIC X(54) VALUE                                    
010126         "847838828818809799789779769759749740730720710700690681".
010128     10 FILLER PIC X(54) VALUE                                    
010130         "671661651642632622613603593584574565555546536527517508".
010132     10 FILLER PIC X(54) VALUE                                    
010134         "498489479470461451442433424415406397388379370361353345".
010136     10 FILLER PIC X(54) VALUE                                    
010138         "336328320312305297290283276269263257251245240234229225".
010140     10 FILLER PIC X(54) VALUE                                    
010142         "220216213209206203200198196194192190189188187186185184".
010144     10 FILLER PIC X(54) VALUE                                    
010146         "184183183182182182181181181181181181180180180180180180".
010148     10 FILLER PIC X(39) VALUE                                    
010150         "180180180180180180180180180180180180180".               
010152     10 FILLER PIC X(54) VALUE                                    
010154         "847838828818809799789779769759749739730720710700690681".
010156     10 FILLER PIC X(54) VALUE                                    
010158         "671661651642632622613603593584574565555545536526517508".
010160     10 FILLER PIC X(54) VALUE                                    
010162         "498489479470460451442432423414405396387378369360352343".
010164     10 FILLER PIC X(54) VALUE                                    
010166         "335327319311303295288281274267260254248242236231225220".
010168     10 FILLER PIC X(54) VALUE                                    
010170         "216211207204200197194192189187185183182181179178177177".
010172     10 FILLER PIC X(54) VALUE                                    
010174         "176175175174174174174173173173173173173173172172172172".
010176     10 FILLER PIC X(39) VALUE                                    
010178         "172172172172172172172172172172172172172".               
010180     10 FILLER PIC X(54) VALUE                                    
010182         "846838828818808799789779769759749739730720710700690681".
010184     10 FILLER PIC X(54) VALUE                                    
010186         "671661651642632622612603593584574564555545536526517507".
010188     10 FILLER PIC X(54) VALUE                                    
010190         "498488479469460451441432423414404395386377368360351342".
010192     10 FILLER PIC X(54) VALUE                                    
010194         "334326317309301294286279272265258251245239233227222216".
010196     10 FILLER PIC X(54) VALUE                                    
010198         "211207203199195191188186183181179177175174172171170169".
010200     10 FILLER PIC X(54) VALUE                                    
010202         "169168167167166166166166165165165165165165165165165165".
010204     10 FILLER PIC X(39) VALUE                                    
010206         "156164164164164164164164164164164164164".               
010208     10 FILLER PIC X(54) VALUE                                    
010210         "846838828818808799789779769759749739729720710700690680".
010212     10 FILLER PIC X(54) VALUE                                    
010214         "671661651641632622612603593583574564555545536526517507".
010216     10 FILLER PIC X(54) VALUE                                    
010218         "498488479469460450441432422413404395386377368359350341".
010220     10 FILLER PIC X(54) VALUE                                    
010222         "333324316308300292284277270262255249242236230224218213".
010224     10 FILLER PIC X(54) VALUE                                    
010226         "207203198194190186183180177174172170168167165164163162".
010228     10 FILLER PIC X(54) VALUE                                    
010230         "161161160159159159158158158157157157157157157157157157".
010232     10 FILLER PIC X(39) VALUE                                    
010234         "157157157157157157157157156156156156156".               
010236     10 FILLER PIC X(54) VALUE                                    
010238         "846838828818808799789779769759749739729720710700690680".
010240     10 FILLER PIC X(54) VALUE                                    
010242         "671661651641632622612603593583574564555545535526516507".
010244     10 FILLER PIC X(54) VALUE                                    
010246         "497488478469459450441431422413403394385376367358349341".
010248     10 FILLER PIC X(54) VALUE                                    
010250         "332324315307299291283275268261253246240233227221215209".
010252     10 FILLER PIC X(54) VALUE                                    
010254         "204199194189185181178174171169166164162160159157156155".
010256     10 FILLER PIC X(54) VALUE                                    
010258         "154153153152152151151150150150150150149149149149149149".
010260     10 FILLER PIC X(39) VALUE                                    
010262         "149149149149149149149149149149149148148".               
010264     10 FILLER PIC X(54) VALUE                                    
010266         "846838828818808798789779769759749739729720710700690680".
010268     10 FILLER PIC X(54) VALUE                                    
010270         "671661651641632622612602593583574564554545535526516507".
010272     10 FILLER PIC X(54) VALUE                                    
010274         "497487478468459449440430421412403394385375366357349340".
010276     10 FILLER PIC X(54) VALUE                                    
010278         "331323314306298290282274266259252244237231224218212206".
010280     10 FILLER PIC X(54) VALUE                                    
010282         "200195190185181177173169166163160158156154152151149148".
010284     10 FILLER PIC X(54) VALUE                                    
010286         "147146146145144144143143143143142142142142142142142142".
010288     10 FILLER PIC X(39) VALUE                                    
010290         "142142142142142142141141141141141141141".               
010292     10 FILLER PIC X(54) VALUE                                    
010294         "846838828818808798789779769759749739729720710700690680".
010296     10 FILLER PIC X(54) VALUE                                    
010298         "670661651641631622612602593583573564554545535526516507".
010300     10 FILLER PIC X(54) VALUE                                    
010302         "497488478469459450440431421412403393384375366357348339".
010304     10 FILLER PIC X(54) VALUE                                    
010306         "330322313305297288280273265257250243235229222215209203".
010308     10 FILLER PIC X(54) VALUE                                    
010310         "197191186181177172168164161158155152150148146144143142".
010312     10 FILLER PIC X(54) VALUE                                    
010314         "141140139138137137136136136135135135135135135134134134".
010316     10 FILLER PIC X(39) VALUE                                    
010318         "134134134134134134134134134134134134133".               
010320     10 FILLER PIC X(54) VALUE                                    
010322         "846838828818808798789779769759749739729719710700690680".
010324     10 FILLER PIC X(54) VALUE                                    
010326         "670661651641631622612602593583573564554545535526516506".
010328     10 FILLER PIC X(54) VALUE                                    
010330         "497487478468459449440430421412402393384375365356347339".
010332     10 FILLER PIC X(54) VALUE                                    
010334         "330321312304296287279271264256248241234227220213206200".
010336     10 FILLER PIC X(54) VALUE                                    
010338         "194188183178173168164160156153150147144142140138137135".
010340     10 FILLER PIC X(54) VALUE                                    
010342         "134133132131131130129129129128128128128128127127127127".
010344     10 FILLER PIC X(39) VALUE                                    
010346         "127127127127127127127127127127126126126".               
010348     10 FILLER PIC X(54) VALUE                                    
010350         "846838828818808798789779769759749739729719710700690680".
010352     10 FILLER PIC X(54) VALUE                                    
010354         "670661651641631622612602593583573564554545535525516506".
010356     10 FILLER PIC X(54) VALUE                                    
010358         "497487478468459449440430421411402393383374365356347338".
010360     10 FILLER PIC X(54) VALUE                                    
010362         "329320312303295287278270262255247239232225218211204198".
010364     10 FILLER PIC X(54) VALUE                                    
010366         "192186180174169164160156152148145142139136134132131129".
010368     10 FILLER PIC X(54) VALUE                                    
010370         "128127126125124123123122122122121121121121120120120120".
010372     10 FILLER PIC X(39) VALUE                                    
010374         "120120120120120120120120120120119119119".               
010376     10 FILLER PIC X(54) VALUE                                    
010378         "846838828818808798789779769759749739729719710700690680".
010380     10 FILLER PIC X(54) VALUE                                    
010382         "670661651641631621612602592583573564554544535525516506".
010384     10 FILLER PIC X(54) VALUE                                    
010386         "497487478468459449439430421411402392383374365355346337".
010388     10 FILLER PIC X(54) VALUE                                    
010390         "329320311303294286278269261253246238231223216209202196".
010392     10 FILLER PIC X(54) VALUE                                    
010394         "189183177171166161156152147144140137134131129127125123".
010396     10 FILLER PIC X(54) VALUE                                    
010398         "122121119119118117116116115115115114114114114114114114".
010400     10 FILLER PIC X(39) VALUE                                    
010402         "114113113113113113113113113113113112112".               
010404     10 FILLER PIC X(54) VALUE                                    
010406         "846838828818808798789779769759749739729719710700690680".
010408     10 FILLER PIC X(54) VALUE                                    
010410         "670660651641631621612602592583573564554544535525516506".
010412     10 FILLER PIC X(54) VALUE                                    
010414         "497487477468458449439430420411401392383373364355346337".
010416     10 FILLER PIC X(54) VALUE                                    
010418         "328319311302293285277269260252245237229222215207200194".
010420     10 FILLER PIC X(54) VALUE                                    
010422         "187181174169163158153148144140136132129126124122120118".
010424     10 FILLER PIC X(54) VALUE                                    
010426         "116115114113112111110110109109108108108107107107107107".
010428     10 FILLER PIC X(39) VALUE                                    
010430         "107107107107107107107107106106106106105".               
010432     10 FILLER PIC X(54) VALUE                                    
010434         "846838828818808798789779769759749739729719709700690680".
010436     10 FILLER PIC X(54) VALUE                                    
010438         "670660651641631621612602592583573563554544535525516506".
010440     10 FILLER PIC X(54) VALUE                                    
010442         "497487477468458449439430420411401392383373364355346337".
010444     10 FILLER PIC X(54) VALUE                                    
010446         "328319310301293284276268260252244236228221213206199192".
010448     10 FILLER PIC X(54) VALUE                                    
010450         "185179172166160155150145140136132128125122119117115113".
010452     10 FILLER PIC X(54) VALUE                                    
010454         "111109108107106105104104103102102102101101101101101101".
010456     10 FILLER PIC X(39) VALUE                                    
010458         "101101101101101100100100100100100099099".               
010460     10 FILLER PIC X(54) VALUE                                    
010462         "846837828818808798789779769759749739729719709700690680".
010464     10 FILLER PIC X(54) VALUE                                    
010466         "670660651641631621612602592583573563554544535525516506".
010468     10 FILLER PIC X(54) VALUE                                    
010470         "496487477468458449439430420411401392382373364354345336".
010472     10 FILLER PIC X(54) VALUE                                    
010474         "327318310301292284275267259251243235227220212205197190".
010476     10 FILLER PIC X(54) VALUE                                    
010478         "183177170164158152147142137132128124121118115112110108".
010480     10 FILLER PIC X(54) VALUE                                    
010482         "106104103101100099099098097097096096096095095095095095".
010484     10 FILLER PIC X(39) VALUE                                    
010486         "095095095095095094094094094094093093093".               
010488     10 FILLER PIC X(54) VALUE                                    
010490         "846837828818808798789779769759749739729719709700690680".
010492     10 FILLER PIC X(54) VALUE                                    
010494         "670660651641631621612602592583573563554544535525515506".
010496     10 FILLER PIC X(54) VALUE                                    
010498         "496487477468458449439429420410401392382373363354345336".
010500     10 FILLER PIC X(54) VALUE                                    
010502         "327318309300292283275267258250242234226219211204196189".
010504     10 FILLER PIC X(54) VALUE                                    
010506         "182175168162156150144139134129125121117114111108105103".
010508     10 FILLER PIC X(54) VALUE                                    
010510         "101099098096095094093092092091091090090090089089089089".
010512     10 FILLER PIC X(39) VALUE                                    
010514         "089089089089089089089088088088088087087".               
010516     10 FILLER PIC X(54) VALUE                                    
010518         "846837828818808798788779769759749739729719709700690680".
010520     10 FILLER PIC X(54) VALUE                                    
010522         "670660651641631621612602592583573563554544535525515506".
010524     10 FILLER PIC X(54) VALUE                                    
010526         "496487477468458448439429420410401391382373363354345336".
010528     10 FILLER PIC X(54) VALUE                                    
010530         "327318309300291283274266258250241233226218210203195188".
010532     10 FILLER PIC X(54) VALUE                                    
010534         "181174167160154148142136131126122118114110107104101099".
010536     10 FILLER PIC X(54) VALUE                                    
010538         "097095093092090089088087087086085085085084084084084084".
010540     10 FILLER PIC X(39) VALUE                                    
010542         "084084083083083083083083083082082082081".               
010544     10 FILLER PIC X(54) VALUE                                    
010546         "846837828818808798788779769759749739729719709700690680".
010548     10 FILLER PIC X(54) VALUE                                    
010550         "670660651641631621611602592582573563554544535525515506".
010552     10 FILLER PIC X(54) VALUE                                    
010554         "496487477467458448439429420410401391382372363354345335".
010556     10 FILLER PIC X(54) VALUE                                    
010558         "326317309300291282274266257249241233225217209202194187".
010560     10 FILLER PIC X(54) VALUE                                    
010562         "179172165159152146140134129124119115111107104100098095".
010564     10 FILLER PIC X(54) VALUE                                    
010566         "093091089087086085084083082081080080080079079079079079".
010568     10 FILLER PIC X(39) VALUE                                    
010570         "078078078078078078078078077077077076076".               
010572     10 FILLER PIC X(54) VALUE                                    
010574         "846837828818808798788779769759749739729719709700690680".
010576     10 FILLER PIC X(54) VALUE                                    
010578         "670660650641631621611602592582573563554544534525515506".
010580     10 FILLER PIC X(54) VALUE                                    
010582         "496487477467458448439429420410401391382372363354344335".
010584     10 FILLER PIC X(54) VALUE                                    
010586         "326317308299291282274265257249240232224216209201193186".
010588     10 FILLER PIC X(54) VALUE                                    
010590         "178171164157151144138132127122117112108104100097094091".
010592     10 FILLER PIC X(54) VALUE                                    
010594         "089087085083082080079078077076076075075074074074074074".
010596     10 FILLER PIC X(39) VALUE                                    
010598         "074074074073073073073073073072072071071".               
010600     10 FILLER PIC X(54) VALUE                                    
010602         "846837828818808798788779769759749739729719709699690680".
010604     10 FILLER PIC X(54) VALUE                                    
010606         "670660650641631621611602592582573563554544534525515506".
010608     10 FILLER PIC X(54) VALUE                                    
010610         "496487477467458448439429420410400391382372363353344335".
010612     10 FILLER PIC X(54) VALUE                                    
010614         "326317308299290282273265256248240232224216208200192185".
010616     10 FILLER PIC X(54) VALUE                                    
010618         "177170163156149143137131125120115110105101098094091088".
010620     10 FILLER PIC X(54) VALUE                                    
010622         "086083081079078076075074073072072071070070070069069069".
010624     10 FILLER PIC X(39) VALUE                                    
010626         "069069069069069069069068068068067066066".               
010628     10 FILLER PIC X(54) VALUE                                    
010630         "846837828818808798788779769759749739729719709699690680".
010632     10 FILLER PIC X(54) VALUE                                    
010634         "670660650641631621611602592582573563554544534525515506".
010636     10 FILLER PIC X(54) VALUE                                    
010638         "496487477467458448439429419410400391381372363353344335".
010640     10 FILLER PIC X(54) VALUE                                    
010642         "326317308299290282273264256248240231223215207200192184".
010644     10 FILLER PIC X(54) VALUE                                    
010646         "177169162155148142135129123118113108103099095091088085".
010648     10 FILLER PIC X(54) VALUE                                    
010650         "083080078076074073071070069068068067066066066065065065".
010652     10 FILLER PIC X(39) VALUE                                    
010654         "065065065065065064064064064063063062061".               
010656     10 FILLER PIC X(54) VALUE                                    
010658         "846837828818808798788779769759749739729719709699690680".
010660     10 FILLER PIC X(54) VALUE                                    
010662         "670660650641631621611602592582573563554544534525515506".
010664     10 FILLER PIC X(54) VALUE                                    
010666         "496486477467458448439429419410400391381372363353344335".
010668     10 FILLER PIC X(54) VALUE                                    
010670         "326317308299290281273264256247239231223215207199191184".
010672     10 FILLER PIC X(54) VALUE                                    
010674         "176169161154147141134128122116111106101097093089086083".
010676     10 FILLER PIC X(54) VALUE                                    
010678         "080077075073071069068067066065064063063062062061061061".
010680     10 FILLER PIC X(39) VALUE                                    
010682         "061061061061061061060060060059058058057".               
010684     10 FILLER PIC X(54) VALUE                                    
010686         "846837828818808798788779769759749739729719709699690680".
010688     10 FILLER PIC X(54) VALUE                                    
010690         "670660650641631621611602592582573563553544534525515506".
010692     10 FILLER PIC X(54) VALUE                                    
010694         "496486477467458448439429419410400391381372362353344335".
010696     10 FILLER PIC X(54) VALUE                                    
010698         "325316307299290281273264256247239231223215207199191183".
010700     10 FILLER PIC X(54) VALUE                                    
010702         "175168161153146140133127121115109104099095091087083080".
010704     10 FILLER PIC X(54) VALUE                                    
010706         "077075072070068066065064062061060060059059058058058058".
010708     10 FILLER PIC X(39) VALUE                                    
010710         "057057057057057057057056056055055054053".               
010712     10 FILLER PIC X(54) VALUE                                    
010714         "846837828818808798788779769759749739729719709699690680".
010716     10 FILLER PIC X(54) VALUE                                    
010718         "670660650641631621611602592582573563553544534525515506".
010720     10 FILLER PIC X(54) VALUE                                    
010722         "496486477467458448438429419410400391381372362353344335".
010724     10 FILLER PIC X(54) VALUE                                    
010726         "325316307298290281272264255247239230222214206198190183".
010728     10 FILLER PIC X(54) VALUE                                    
010730         "175167160153146139132126119114108103098093089085081078".
010732     10 FILLER PIC X(54) VALUE                                    
010734         "075072070067065064062061059058057056056055055054054054".
010736     10 FILLER PIC X(39) VALUE                                    
010738         "054054054054054053053053052052051050049".               
010740     10 FILLER PIC X(54) VALUE                                    
010742         "846837828818808798788779769759749739729719709699690680".
010744     10 FILLER PIC X(54) VALUE                                    
010746         "670660650641631621611602592582573563553544534525515506".
010748     10 FILLER PIC X(54) VALUE                                    
010750         "496486477467458448438429419410400391381372362353344334".
010752     10 FILLER PIC X(54) VALUE                                    
010754         "325316307298290281272264255247238230222214206198190182".
010756     10 FILLER PIC X(54) VALUE                                    
010758         "174167159152145138131125119113107101096092087083079076".
010760     10 FILLER PIC X(54) VALUE                                    
010762         "073070067065063061059058057055054053053052052051051051".
010764     10 FILLER PIC X(39) VALUE                                    
010766         "051051051051051050050050049049048047046".               
010768     10 FILLER PIC X(54) VALUE                                    
010770         "846837828818808798788779769759749739729719709699690680".
010772     10 FILLER PIC X(54) VALUE                                    
010774         "670660650641631621611602592582573563553544534525515506".
010776     10 FILLER PIC X(54) VALUE                                    
010778         "496486477467458448438429419410400391381372362353344334".
010780     10 FILLER PIC X(54) VALUE                                    
010782         "325316307298289281272263255247238230222214206198190182".
010784     10 FILLER PIC X(54) VALUE                                    
010786         "174166159152144137131124118112106100095090086082078074".
010788     10 FILLER PIC X(54) VALUE                                    
010790         "071068065063061059057055054053052051050049049049048048".
010792     10 FILLER PIC X(39) VALUE                                    
010794         "048048048048048047047047046046045044043".               
010796     10 FILLER PIC X(54) VALUE                                    
010798         "846837828818808798788779769759749739729719709699690680".
010800     10 FILLER PIC X(54) VALUE                                    
010802         "670660650641631621611602592582573563553544534525515506".
010804     10 FILLER PIC X(54) VALUE                                    
010806         "496486477467458448438429419410400391381372362353344334".
010808     10 FILLER PIC X(54) VALUE                                    
010810         "325316307298289281272263255246238230222214206197189182".
010812     10 FILLER PIC X(54) VALUE                                    
010814         "174166159151144137130123117111105099094089085080076073".
010816     10 FILLER PIC X(54) VALUE                                    
010818         "069066064061059057055053052050049048047047046046046046".
010820     10 FILLER PIC X(39) VALUE                                    
010822         "045045045045045045044044044043042041040".               
010824     10 FILLER PIC X(54) VALUE                                    
010826         "846837828818808798788779769759749739729719709699690680".
010828     10 FILLER PIC X(54) VALUE                                    
010830         "670660650641631621611602592582573563553544534525515506".
010832     10 FILLER PIC X(54) VALUE                                    
010834         "496486477467458448438429419410400391381372362353343334".
010836     10 FILLER PIC X(54) VALUE                                    
010838         "325316307298289280272263255246238230222213205197189181".
010840     10 FILLER PIC X(54) VALUE                                    
010842         "174166158151143136129123116110104099093088084079075071".
010844     10 FILLER PIC X(54) VALUE                                    
010846         "068065062059057055053051050048047046045045044044043043".
010848     10 FILLER PIC X(39) VALUE                                    
010850         "043043043043043042042042041040039038037".               
010852     10 FILLER PIC X(54) VALUE                                    
010854         "846837828818808798788779769759749739729719709699690680".
010856     10 FILLER PIC X(54) VALUE                                    
010858         "670660650641631621611602592582573563553544534525515506".
010860     10 FILLER PIC X(54) VALUE                                    
010862         "496486477467458448438429419410400391381372362353343334".
010864     10 FILLER PIC X(54) VALUE                                    
010866         "325316307298289280272263255246238230221213205197189181".
010868     10 FILLER PIC X(54) VALUE                                    
010870         "173166158150143136129122116110104098092087083078074070".
010872     10 FILLER PIC X(54) VALUE                                    
010874         "067064061058055053051049048046045044043042042041041041".
010876     10 FILLER PIC X(39) VALUE                                    
010878         "041041041041040040040040039038037035034".               
010880     10 FILLER PIC X(54) VALUE                                    
010882         "846837828818808798788779769759749739729719709699690680".
010884     10 FILLER PIC X(54) VALUE                                    
010886         "670660650641631621611602592582573563553544534525515506".
010888     10 FILLER PIC X(54) VALUE                                    
010890         "496486477467458448438429419410400391381372362353343334".
010892     10 FILLER PIC X(54) VALUE                                    
010894         "325316307298289280272263255246238229221213205197189181".
010896     10 FILLER PIC X(54) VALUE                                    
010898         "173165158150143136129122115109103097092087082077073069".
010900     10 FILLER PIC X(54) VALUE                                    
010902         "066062059057054052050048046045043042041041040040039039".
010904     10 FILLER PIC X(39) VALUE                                    
010906         "039039039039038038038038037036035033032".               
010908     10 FILLER PIC X(54) VALUE                                    
010910         "846837828818808798788779769759749739729719709699690680".
010912     10 FILLER PIC X(54) VALUE                                    
010914         "670660650641631621611602592582573563553544534525515506".
010916     10 FILLER PIC X(54) VALUE                                    
010918         "496486477467458448438429419410400391381372362353343334".
010920     10 FILLER PIC X(54) VALUE                                    
010922         "325316307298289280272263254246238229221213205197189181".
010924     10 FILLER PIC X(54) VALUE                                    
010926         "173165157150143135128122115109102097091086081076072068".
010928     10 FILLER PIC X(54) VALUE                                    
010930         "065061058055053050048046045043042041040039038038038037".
010932     10 FILLER PIC X(39) VALUE                                    
010934         "037037037037037036036036035034033031030".               
010936     10 FILLER PIC X(54) VALUE                                    
010938         "846837828818808798788779769759749739729719709699690680".
010940     10 FILLER PIC X(54) VALUE                                    
010942         "670660650641631621611602592582573563553544534525515506".
010944     10 FILLER PIC X(54) VALUE                                    
010946         "496486477467458448438429419410400390381371362353343334".
010948     10 FILLER PIC X(54) VALUE                                    
010950         "325316307298289280271263254246238229221213205197189181".
010952     10 FILLER PIC X(54) VALUE                                    
010954         "173165157150142135128121115108102096091085080076072068".
010956     10 FILLER PIC X(54) VALUE                                    
010958         "064060057054052049047045043042041039038037037036036036".
010960     10 FILLER PIC X(39) VALUE                                    
010962         "036036035035035035035034033033031029028".               
010964     10 FILLER PIC X(54) VALUE                                    
010966         "846837828818808798788779769759749739729719709699690680".
010968     10 FILLER PIC X(54) VALUE                                    
010970         "670660650641631621611602592582573563553544534525515506".
010972     10 FILLER PIC X(54) VALUE                                    
010974         "496486477467458448438429419410400390381371362353343334".
010976     10 FILLER PIC X(54) VALUE                                    
010978         "325316307298289280271263254246238229221213205196188180".
010980     10 FILLER PIC X(54) VALUE                                    
010982         "173165157150142135128121114108102096090085080075071067".
010984     10 FILLER PIC X(54) VALUE                                    
010986         "063060056053051048046044042041039038037036035035035034".
010988     10 FILLER PIC X(39) VALUE                                    
010990         "036036035035035035035034033031030028026".               
010992     10 FILLER PIC X(54) VALUE                                    
010994         "846837828818808798788779769759749739729719709699690680".
010996     10 FILLER PIC X(54) VALUE                                    
010998         "670660650641631621611602592582573563553544534525515506".
011000     10 FILLER PIC X(54) VALUE                                    
011002         "496486477467458448438429419410400390381371362353343334".
011004     10 FILLER PIC X(54) VALUE                                    
011006         "325316307298289280271263254246237229221213205196188180".
011008     10 FILLER PIC X(54) VALUE                                    
011010         "173165157149142135128121114108101096090085080075070066".
011012     10 FILLER PIC X(54) VALUE                                    
011014         "063059056053050047045043041040038037036035034034033033".
011016     10 FILLER PIC X(39) VALUE                                    
011018         "033033033033033032032032031030028026025".               
011020     10 FILLER PIC X(54) VALUE                                    
011022         "846837828818808798788779769759749739729719709699690680".
011024     10 FILLER PIC X(54) VALUE                                    
011026         "670660650641631621611602592582573563553544534525515505".
011028     10 FILLER PIC X(54) VALUE                                    
011030         "496486477467458448438429419410400390381371362353343334".
011032     10 FILLER PIC X(54) VALUE                                    
011034         "325316307298289280271263254246237229221213205196188180".
011036     10 FILLER PIC X(54) VALUE                                    
011038         "173165157149142135128121114107101095090084079074070066".
011040     10 FILLER PIC X(54) VALUE                                    
011042         "062059055052049047045042041039037036035034033033032032".
011044     10 FILLER PIC X(39) VALUE                                    
011046         "032032032032032031031031030029027025023".               
011048     10 FILLER PIC X(54) VALUE                                    
011050         "846837828818808798788779769759749739729719709699690680".
011052     10 FILLER PIC X(54) VALUE                                    
011054         "670660650641631621611602592582573563553544534525515505".
011056     10 FILLER PIC X(54) VALUE                                    
011058         "496486477467458448438429419410400390381371362353343334".
011060     10 FILLER PIC X(54) VALUE                                    
011062         "325316307298289280271263254246237229221213205196188180".
011064     10 FILLER PIC X(54) VALUE                                    
011066         "172165157149142135127120114107101095089084079074070066".
011068     10 FILLER PIC X(54) VALUE                                    
011070         "062058055052049046044042040038037035034033033032032032".
011072     10 FILLER PIC X(39) VALUE                                    
011074         "031031031031031031030030029028026024021".               
011076     10 FILLER PIC X(54) VALUE                                    
011078         "846837828818808798788779769759749739729719709699690680".
011080     10 FILLER PIC X(54) VALUE                                    
011082         "670660650641631621611602592582573563553544534525515505".
011084     10 FILLER PIC X(54) VALUE                                    
011086         "496486477467457448438429419410400390381371362353343334".
011088     10 FILLER PIC X(54) VALUE                                    
011090         "325316307298289280271263254246237229221213205196188180".
011092     10 FILLER PIC X(54) VALUE                                    
011094         "172165157149142134127120114107101095089084079074069065".
011096     10 FILLER PIC X(54) VALUE                                    
011098         "061058054051049046044041040038036035034033032031031031".
011100     10 FILLER PIC X(39) VALUE                                    
011102         "031031031030030030030029028027026024021".               
011104     10 FILLER PIC X(54) VALUE                                    
011106         "846837828818808798788779769759749739729719709699690680".
011108     10 FILLER PIC X(54) VALUE                                    
011110         "670660650641631621611602592582573563553544534525515505".
011112     10 FILLER PIC X(54) VALUE                                    
011114         "496486477467457448438429419410400390381371362353343334".
011116     10 FILLER PIC X(54) VALUE                                    
011118         "325316307298289280271263254246237229221213205196188180".
011120     10 FILLER PIC X(54) VALUE                                    
011122         "172165157149142134127120114107101095089084079074069065".
011124     10 FILLER PIC X(54) VALUE                                    
011126         "061058054051048046043041039038036035033032032031031031".
011128     10 FILLER PIC X(39) VALUE                                    
011130         "030030030030030030029029028027025023021".               
011132     10 FILLER PIC X(54) VALUE                                    
011134         "846837828818808798788779769759749739729719709699690680".
011136     10 FILLER PIC X(54) VALUE                                    
011138         "670660650641631621611602592582573563553544534525515505".
011140     10 FILLER PIC X(54) VALUE                                    
011142         "496486477467457448438429419410400390381371362353343334".
011144     10 FILLER PIC X(54) VALUE                                    
011146         "325316307298289280271263254246237229221213205196188180".
011148     10 FILLER PIC X(54) VALUE                                    
011150         "172165157149142134127120114107101095089084079074069065".
011152     10 FILLER PIC X(54) VALUE                                    
011154         "061058054051048046043041039037036034033032032031031030".
011156     10 FILLER PIC X(39) VALUE                                    
011158         "030030030030030029029029028027025023021".               
011160     10 FILLER PIC X(54) VALUE                                    
011162         "846837828818808798788779769759749739729719709699690680".
011164     10 FILLER PIC X(54) VALUE                                    
011166         "670660650641631621611602592582573563553544534525515505".
011168     10 FILLER PIC X(54) VALUE                                    
011170         "496486477467457448438429419410400390381371362353343334".
011172     10 FILLER PIC X(54) VALUE                                    
011174         "325316307298289280271263254246237229221213205196188180".
011176     10 FILLER PIC X(54) VALUE                                    
011178         "172165157149142134127120114107101095089084078074069065".
011180     10 FILLER PIC X(54) VALUE                                    
011182         "061057054051048045043041039037036034033032031031030030".
011184     10 FILLER PIC X(39) VALUE                                    
011186         "030030030030029029029028028027025023020".               
011188     10 FILLER PIC X(54) VALUE                                    
011190         "846837828818808798788779769759749739729719709699690680".
011192     10 FILLER PIC X(54) VALUE                                    
011194         "670660650641631621611602592582573563553544534525515505".
011196     10 FILLER PIC X(54) VALUE                                    
011198         "496486477467457448438429419410400390381371362353343334".
011200     10 FILLER PIC X(54) VALUE                                    
011202         "325316307298289280271263254246237229221213204196188180".
011204     10 FILLER PIC X(54) VALUE                                    
011206         "172164157149142134127120113107101095089084078074069065".
011208     10 FILLER PIC X(54) VALUE                                    
011210         "061057054051048045043041039037036034033032031031030030".
011212     10 FILLER PIC X(39) VALUE                                    
011214         "030030030030029029029028028026025023020".               
011216     10 FILLER PIC X(54) VALUE                                    
011218         "846837828818808798788779769759749739729719709699690680".
011220     10 FILLER PIC X(54) VALUE                                    
011222         "670660650641631621611602592582573563553544534525515505".
011224     10 FILLER PIC X(54) VALUE                                    
011226         "496486477467457448438429419410400390381371362353343334".
011228     10 FILLER PIC X(54) VALUE                                    
011230         "325316307298289280271263254246237229221213204196188180".
011232     10 FILLER PIC X(54) VALUE                                    
011234         "172164157149142134127120113107101095089083078074069065".
011236     10 FILLER PIC X(54) VALUE                                    
011238         "061057054051048045043041039037035034033032031031030030".
011240     10 FILLER PIC X(39) VALUE                                    
011242         "030030030029029029029028027026025022020".               
011244     10 FILLER PIC X(54) VALUE                                    
011246         "846837828818808798788779769759749739729719709699690680".
011248     10 FILLER PIC X(54) VALUE                                    
011250         "670660650641631621611602592582573563553544534525515505".
011252     10 FILLER PIC X(54) VALUE                                    
011254         "496486477467457448438429419410400390381371362353343334".
011256     10 FILLER PIC X(54) VALUE                                    
011258         "325316307298289280271263254246237229221213204196188180".
011260     10 FILLER PIC X(54) VALUE                                    
011262         "172164157149142134127120113107101095089083078073069065".
011264     10 FILLER PIC X(54) VALUE                                    
011266         "061057054051048045043041039037035034033032031030030030".
011268     10 FILLER PIC X(39) VALUE                                    
011270         "030030029029029029028028027026024022020".               
011272     10 FILLER PIC X(54) VALUE                                    
011274         "846837828818808798788779769759749739729719709699690680".
011276     10 FILLER PIC X(54) VALUE                                    
011278         "670660650641631621611602592582573563553544534525515505".
011280     10 FILLER PIC X(54) VALUE                                    
011282         "496486477467457448438429419410400390381371362353343334".
011284     10 FILLER PIC X(54) VALUE                                    
011286         "325316307298289280271263254246237229221213204196188180".
011288     10 FILLER PIC X(54) VALUE                                    
011290         "172164157149142134127120113107101095089083078073069065".
011292     10 FILLER PIC X(54) VALUE                                    
011294         "061057054051048045043040038037035034033032031030030030".
011296     10 FILLER PIC X(39) VALUE                                    
011298         "029029029029029029028028027026024022020".               
011300     10 FILLER PIC X(54) VALUE                                    
011302         "846837828818808798788779769759749739729719709699690680".
011304     10 FILLER PIC X(54) VALUE                                    
011306         "670660650641631621611602592582573563553544534525515505".
011308     10 FILLER PIC X(54) VALUE                                    
011310         "496486477467457448438429419410400390381371362353343334".
011312     10 FILLER PIC X(54) VALUE                                    
011314         "325316307298289280271263254246237229221213204196188180".
011316     10 FILLER PIC X(54) VALUE                                    
011318         "172164157149142134127120113107100094089083078073069064".
011320     10 FILLER PIC X(54) VALUE                                    
011322         "061057053050047045042040038036035034032031031030030029".
011324     10 FILLER PIC X(39) VALUE                                    
011326         "029029029029029028028028027026024022019".               
011328     10 FILLER PIC X(54) VALUE                                    
011330         "846837828818808798788779769759749739729719709699690680".
011332     10 FILLER PIC X(54) VALUE                                    
011334         "670660650641631621611602592582573563553544534525515505".
011336     10 FILLER PIC X(54) VALUE                                    
011338         "496486477467457448438429419410400390381371362353343334".
011340     10 FILLER PIC X(54) VALUE                                    
011342         "325316307298289280271263254246237229221213204196188180".
011344     10 FILLER PIC X(54) VALUE                                    
011346         "172164157149141134127120113107100094089083078073069064".
011348     10 FILLER PIC X(54) VALUE                                    
011350         "060057053050047044042040038036035033032031030030029029".
011352     10 FILLER PIC X(39) VALUE                                    
011354         "029029029028028028028027026025024021019".               
011356     10 FILLER PIC X(54) VALUE                                    
011358         "846837828818808798788779769759749739729719709699690680".
011360     10 FILLER PIC X(54) VALUE                                    
011362         "670660650641631621611602592582573563553544534525515505".
011364     10 FILLER PIC X(54) VALUE                                    
011366         "496486477467457448438429419410400390381371362353343334".
011368     10 FILLER PIC X(54) VALUE                                    
011370         "325316307298289280271263254246237229221213204196188180".
011372     10 FILLER PIC X(54) VALUE                                    
011374         "172164157149141134127120113107100094088083078073068064".
011376     10 FILLER PIC X(54) VALUE                                    
011378         "060056053050047044042040038036034033032031030029029029".
011380     10 FILLER PIC X(39) VALUE                                    
011382         "028028028028028028027027026025023021018".               
011384     10 FILLER PIC X(54) VALUE                                    
011386         "846837828818808798788779769759749739729719709699690680".
011388     10 FILLER PIC X(54) VALUE                                    
011390         "670660650641631621611602592582573563553544534525515505".
011392     10 FILLER PIC X(54) VALUE                                    
011394         "496486477467457448438429419410400390381371362353343334".
011396     10 FILLER PIC X(54) VALUE                                    
011398         "325316307298289280271263254246237229221213204196188180".
011400     10 FILLER PIC X(54) VALUE                                    
011402         "172164156149141134127120113106100094088083077073068064".
011404     10 FILLER PIC X(54) VALUE                                    
011406         "060056052049046044041039037035033032031030029028028028".
011408     10 FILLER PIC X(39) VALUE                                    
011410         "028028027027027027026026025024022020018".               
011412     10 FILLER PIC X(54) VALUE                                    
011414         "846837828818808798788779769759749739729719709699690680".
011416     10 FILLER PIC X(54) VALUE                                    
011418         "670660650641631621611602592582573563553544534525515505".
011420     10 FILLER PIC X(54) VALUE                                    
011422         "496486477467457448438429419410400390381371362353343334".
011424     10 FILLER PIC X(54) VALUE                                    
011426         "325316307298289280271263254246237229221212204196188180".
011428     10 FILLER PIC X(54) VALUE                                    
011430         "172164156149141134127120113106100094088082077072068063".
011432     10 FILLER PIC X(54) VALUE                                    
011434         "059055052049046043040038036034033031030029028027027027".
011436     10 FILLER PIC X(39) VALUE                                    
011438         "027026026026026026025025024023021019016".               
011440     10 FILLER PIC X(54) VALUE                                    
011442         "846837828818808798788779769759749739729719709699690680".
011444     10 FILLER PIC X(54) VALUE                                    
011446         "670660650641631621611602592582573563553544534525515505".
011448     10 FILLER PIC X(54) VALUE                                    
011450         "496486477467457448438429419410400390381371362353343334".
011452     10 FILLER PIC X(54) VALUE                                    
011454         "325316307298289280271263254245237229221212204196188180".
011456     10 FILLER PIC X(54) VALUE                                    
011458         "172164156149141134126119113106100093088082077072067063".
011460     10 FILLER PIC X(54) VALUE                                    
011462         "058055051048045042039037035033031030028027026026025025".
011464     10 FILLER PIC X(39) VALUE                                    
011466         "025025025024024024024023022021019017014".               
011468     10 FILLER PIC X(54) VALUE                                    
011470         "846837828818808798788779769759749739729719709699690680".
011472     10 FILLER PIC X(54) VALUE                                    
011474         "670660650641631621611602592582573563553544534525515505".
011476     10 FILLER PIC X(54) VALUE                                    
011478         "496486477467457448438429419410400390381371362353343334".
011480     10 FILLER PIC X(54) VALUE                                    
011482         "325316307298289280271263254245237229221212204196188180".
011484     10 FILLER PIC X(54) VALUE                                    
011486         "172164156148141134126119112106099093087082076071066062".
011488     10 FILLER PIC X(54) VALUE                                    
011490         "058054050047044041038036033031029028026025024024023023".
011492     10 FILLER PIC X(39) VALUE                                    
011494         "023023022022022022021021020019017013011".               
011496     10 FILLER PIC X(54) VALUE                                    
011498         "846837828818808798788779769759749739729719709699690680".
011500     10 FILLER PIC X(54) VALUE                                    
011502         "670660650641631620611602592582573563553544534525515505".
011504     10 FILLER PIC X(54) VALUE                                    
011506         "496486477467457448438429419410400390381371362353343334".
011508     10 FILLER PIC X(54) VALUE                                    
011510         "325316307298288279271263254245237229220212204196188180".
011512     10 FILLER PIC X(54) VALUE                                    
011514         "172164156148141133126119112105099093087081076071066061".
011516     10 FILLER PIC X(54) VALUE                                    
011518         "057053049046043040037034032030028026025023022021021021".
011520     10 FILLER PIC X(39) VALUE                                    
011522         "020020020020020019019018018016014011010".               
011524                                                                  
011526   05  WS-RMD-LEF-TABLE-2-2022 REDEFINES RMD-LEF-TABLE-2-2022.    
011528       10  WS-RMD-LEF-TBL-2-2022-REC OCCURS 121 TIMES.            
011530           15  WS-RMD-TBL2-2022-LEF  PIC 999 OCCURS 121 TIMES.    
011532                                                                  
```

⚠️  This is the source code you must document.
    1,701 lines from 4062 to 5762.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

