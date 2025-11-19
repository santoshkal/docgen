# LLM Request Debug File
Generated: 2025-11-18T20:14:46.175330

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 44/55
- **Model**: gpt-4.1
- **Chunk Number**: 44
- **Pass Number**: 3
- **Attempt Number**: 4 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~2,086 tokens
- **User Prompt**: ~7,293 tokens
- **Total Input**: ~9,379 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 44/55" (ID: detailed-code-explanation)

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


**CHUNK 44 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-18T18:05:37.383587", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 44 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 21246 to 21725 (480 lines)\nChunk Tokens (estimated): ~8,074\nActual Input Tokens: 9,480 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 21246-21725 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 44 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 44 of 55.\n\n\n=============================================================================\nCHUNK 44 SOURCE CODE (Lines 21246-21725)\n=============================================================================\n\n```cobol\n042500 Z-26-4-BEGIN.\n042502*      REQUESTED UPDATE OF FILE CST-FILE-MAINT\n042504     MOVE 7 TO Z-FLINFO6-UPDATE.\n042506     MOVE WS-BANK-NO TO FM2-BANK.\n042508     MOVE WS-TIN-CUST (J) TO FM2-CUST.\n042510     MOVE ZEROS TO FM2-ACCT.\n042512     MOVE 01 TO FM2-STRUCT.\n042514     MOVE 00 TO FM2-RECORD-NBR.\n042516     MOVE 0863 TO FM2-TRANCODE.\n042518     MOVE WS-TIN-RMD-TOT TO WS-FM-AMT.\n042520     MOVE WS-FM-AMT-X TO FM2-CHANGE-DATA.\n042522     MOVE \"R\" TO FM2-APPLY.\n042524     MOVE \"RMDRPT\" TO FM2-ORIGIN.\n042526     MOVE SPACE TO FM2-INT\n042528       , FM2-SYSTEM-USE.\n042530     IF Z-EDIT-ERROR\n042532         GO TO Z-26-XIT.\n042534     IF Z-FLINFO6-UPDATE = 7\n042536         NEXT SENTENCE ELSE\n042538         GO TO Z-26-5-SKIP.\n042540     WRITE MASS-FM-RECORD2\n042542         INVALID KEY\n042544         MOVE Z-FLINFO6-STATUS TO Z-FL-EXCEPT-STATUS\n042546         MOVE \"CST-FILE-MAINT\" TO Z-FL-EXCEPT-FILE\n042548         MOVE 1761 TO Z-FL-EXCEPT-SEQ\n042550         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.\n042552     MOVE Z-FILE6-KEY TO Z-FLINFO6-RS-KEY.\n042554     MOVE ZERO TO Z-FLINFO6-UPDATE.\n042556     MOVE ZERO TO Z-FLINFO6-LAST-SEQ.\n042558 Z-26-5-SKIP.\n042560 Z-26-4-SKIP.\n042562*\n042564 Z-26-4-XIT.\n042566     MOVE 0 TO Z-EXIT-CODE.\n042568     MOVE 9999 TO Z-EXIT-LEVEL.\n042570     MOVE SPACES TO MASS-FM-RECORD2.\n042572 Z-26-2-END.\n042574     IF Z-EDIT-ERROR\n042576         GO TO Z-26-XIT.\n042578 Z-26-2-SKIP.\n042580     IF Z-EXIT-LEVEL < 1\n042582         GO TO Z-26-END.\n042584     IF Z-EXIT-CODE > 0\n042586         GO TO Z-26-2-XIT.\n042588     ADD 1 TO J.\n042590     GO TO Z-26-2-LOOP.\n042592*\n042594 Z-26-2-XIT.\n042596     MOVE 0 TO Z-EXIT-CODE.\n042598     MOVE 9999 TO Z-EXIT-LEVEL.\n042600     MOVE SPACES TO WS-TIN-CUST-TABLE.\n042602     MOVE 0 TO WS-TIN-CUST-INDEX.\n042604 Z-26-1-1-ELSE.\n042606 Z-26-END.\n042608     IF Z-EDIT-ERROR\n042610         GO TO Z-26-XIT.\n042612 Z-26-SKIP.\n042614 Z-26-XIT.\n042616     EXIT.\n042618*\n042620*****************************************************************\n042622*    PROCEDURE COMB-AUTO-RMD-ADJ\n042624*****************************************************************\n042626 Z-27-PROCEDURE.\n042628*\n042630     IF WS-DSTFM-OPEN = 0\n042632         NEXT SENTENCE ELSE\n042634         GO TO Z-27-1-1-ELSE.\n042636     MOVE PROCESS-DATE-MMDD TO WS-DSTFM-DT.\n042638     IF WS-BANK-OPT = 1\n042640         NEXT SENTENCE ELSE\n042642         GO TO Z-27-3-1-ELSE.\n042644     MOVE WS-BANK-NO TO WS-DSTFM-BK.\n042646     MOVE SPACES TO WS-DSTFM-TIME.\n042648     GO TO Z-27-3-ENDIF.\n042650 Z-27-3-1-ELSE.\n042652     IF WS-BANK-OPT = 2\n042654         NEXT SENTENCE ELSE\n042656         GO TO Z-27-3-2-ELSE.\n042658     MOVE 000 TO WS-DSTFM-BK.\n042660*    RETRIEVE TODAY'S DATE\n042662     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n042664          USING Z-CALL-CURRENTDATE.\n042666     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n042668     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n042670     ACCEPT Z-DATE0-TIME   FROM TIME.\n042672     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.\n042674     MOVE Z-DATE0-UU TO Z-DATE4-UU.\n042676     MOVE Z-DATE4-FORMAT TO WS-DSTFM-TIME.\n042678     GO TO Z-27-3-ENDIF.\n042680 Z-27-3-2-ELSE.\n042682     IF WS-BANK-OPT = 3\n042684         NEXT SENTENCE ELSE\n042686         GO TO Z-27-3-3-ELSE.\n042688     MOVE 000 TO WS-DSTFM-BK.\n042690     MOVE SPACES TO WS-DSTFM-SUFF-R.\n042692     MOVE WS-SUFFIX-IN TO WS-DSTFM-SUFF.\n042694 Z-27-3-3-ELSE.\n042696 Z-27-3-ENDIF.\n042698*\n042700******* OPEN FILE DST-FILE-MAINT\n042702*\n042704     IF Z-FLINFO5-OPEN = 0\n042706         CHANGE ATTRIBUTE NEWFILE OF DST-FILE-MAINT TO VALUE TRUE\n042708         OPEN OUTPUT DST-FILE-MAINT \n042710         IF ATTRIBUTE FILESTATE OF DST-FILE-MAINT = VALUE OPENED\n042712             MOVE ZEROS TO Z-FILE5-KEY\n042714             MOVE ZEROS TO Z-FLINFO5-RS-KEY\n042716             MOVE 3 TO Z-FLINFO5-OPEN\n042718             MOVE 3 TO Z-FLINFO5-RS-OPEN\n042720         ELSE\n042722             DISPLAY \">>> FILE DST-FILE-MAINT FAILED TO OPEN\"\n042724             MOVE ATTRIBUTE TITLE OF DST-FILE-MAINT TO            \n042726                 Z-FL-EXCEPT-TITLE\n042728             DISPLAY \">>> OPEN FAIL, TITLE :\", Z-FL-EXCEPT-TITLE\n042730             DISPLAY \">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS\".\n042732     MOVE 1 TO WS-DSTFM-OPEN.\n042734 Z-27-1-1-ELSE.\n042736     MOVE 1 TO J.\n042738     COMPUTE Z-TO-3 = WS-TIN-RMD-MAX.\n042740 Z-27-13-LOOP.\n042742     IF J > Z-TO-3\n042744         GO TO Z-27-13-XIT.\n042746     MOVE 0 TO Z-EXIT-CODE.\n042748     MOVE 9999 TO Z-EXIT-LEVEL.\n042750********* EXIT WHEN\n042752     IF WS-TIN-RMD-CUST (J) = 0\n042754        NEXT SENTENCE\n042756     ELSE\n042758        GO TO Z-27-14-EXIT-SKIP.\n042760     MOVE 1 TO Z-EXIT-LEVEL.\n042762     MOVE 1 TO Z-EXIT-CODE.\n042764     GO TO Z-27-13-END.\n042766 Z-27-14-EXIT-SKIP.\n042768 Z-27-15-BEGIN.\n042770*      REQUESTED UPDATE OF FILE DST-FILE-MAINT\n042772     MOVE 8 TO Z-FLINFO5-UPDATE.\n042774     MOVE WS-BANK-NO TO FM-BANK.\n042776     MOVE WS-TIN-RMD-CUST (J) TO FM-CUST.\n042778     MOVE WS-TIN-RMD-ACCT (J) TO FM-ACCT.\n042780     MOVE 15 TO FM-STRUCT.\n042782     MOVE WS-TIN-RMD-DS-NBR (J) TO FM-RECORD-NBR.\n042784     MOVE 0712 TO FM-TRANCODE.\n042786     IF WS-TIN-DISTR-RECS = 1\n042788         NEXT SENTENCE ELSE\n042790         GO TO Z-27-23-1-ELSE.\n042792     IF WS-TIN-RMD-DS-FREQ (J) = 1\n042794         NEXT SENTENCE ELSE\n042796         GO TO Z-27-24-1-ELSE.\n042798     COMPUTE WS-FM-AMT ROUNDED = ( ( WS-TIN-RMD-TOT / 365 ) *     \n042800         WS-TIN-RMD-DS-NTRVL (J) ) .\n042802\n042804     GO TO Z-27-24-ENDIF.\n042806 Z-27-24-1-ELSE.\n042808     IF WS-TIN-RMD-DS-FREQ (J) = 2\n042810         NEXT SENTENCE ELSE\n042812         GO TO Z-27-24-2-ELSE.\n042814     COMPUTE WS-FM-AMT ROUNDED = ( ( WS-TIN-RMD-TOT / 12 ) *      \n042816         WS-TIN-RMD-DS-NTRVL (J) ) .\n042818\n042820     GO TO Z-27-24-ENDIF.\n042822 Z-27-24-2-ELSE.\n042824     COMPUTE WS-FM-AMT = WS-TIN-RMD-TOT .\n042826\n042828 Z-27-24-ENDIF.\n042830     GO TO Z-27-23-ENDIF.\n042832 Z-27-23-1-ELSE.\n042834     MOVE WS-TIN-RMD-AMT (J) TO WS-FM-AMT.\n042836 Z-27-23-ENDIF.\n042838     MOVE WS-FM-AMT-X TO FM-CHANGE-DATA.\n042840     MOVE \"R\" TO FM-APPLY.\n042842     MOVE \"RMDRPT\" TO FM-ORIGIN.\n042844     MOVE SPACE TO FM-INT.\n042846     MOVE SPACE TO FM-SYSTEM-USE.\n042848     IF Z-EDIT-ERROR\n042850         GO TO Z-27-XIT.\n042852     IF Z-FLINFO5-UPDATE = 8\n042854         NEXT SENTENCE ELSE\n042856         GO TO Z-27-16-SKIP.\n042858     WRITE MASS-FM-RECORD\n042860         INVALID KEY\n042862         MOVE Z-FLINFO5-STATUS TO Z-FL-EXCEPT-STATUS\n042864         MOVE \"DST-FILE-MAINT\" TO Z-FL-EXCEPT-FILE\n042866         MOVE 1821 TO Z-FL-EXCEPT-SEQ\n042868         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.\n042870     MOVE Z-FILE5-KEY TO Z-FLINFO5-RS-KEY.\n042872     MOVE ZERO TO Z-FLINFO5-UPDATE.\n042874     MOVE ZERO TO Z-FLINFO5-LAST-SEQ.\n042876 Z-27-16-SKIP.\n042878 Z-27-15-SKIP.\n042880*\n042882 Z-27-15-XIT.\n042884     MOVE 0 TO Z-EXIT-CODE.\n042886     MOVE 9999 TO Z-EXIT-LEVEL.\n042888 Z-27-13-END.\n042890     IF Z-EDIT-ERROR\n042892         GO TO Z-27-XIT.\n042894 Z-27-13-SKIP.\n042896     IF Z-EXIT-LEVEL < 1\n042898         GO TO Z-27-END.\n042900     IF Z-EXIT-CODE > 0\n042902         GO TO Z-27-13-XIT.\n042904     ADD 1 TO J.\n042906     GO TO Z-27-13-LOOP.\n042908*\n042910 Z-27-13-XIT.\n042912     MOVE 0 TO Z-EXIT-CODE.\n042914     MOVE 9999 TO Z-EXIT-LEVEL.\n042916     MOVE SPACES TO WS-TIN-RMD-TABLE.\n042918     MOVE 0 TO WS-TIN-RMD-INDEX.\n042920 Z-27-END.\n042922     IF Z-EDIT-ERROR\n042924         GO TO Z-27-XIT.\n042926 Z-27-SKIP.\n042928 Z-27-XIT.\n042930     EXIT.\n042932*\n042934*****************************************************************\n042936*    PROCEDURE TDD-TDAA-MOVE-TO-TDB\n042938*****************************************************************\n042940 Z-12-PROCEDURE.\n042942*\n042944     MOVE TDAA-BANK OF TDAACCT TO TDB-TDAA-BANK OF TDB-TDAACCT.\n042946     MOVE TDAA-BRCH OF TDAACCT TO TDB-TDAA-BRCH OF TDB-TDAACCT.\n042948     MOVE TDAA-APPL OF TDAACCT TO TDB-TDAA-APPL OF TDB-TDAACCT.\n042950     MOVE TDAA-CUST OF TDAACCT TO TDB-TDAA-CUST OF TDB-TDAACCT.\n042952     MOVE TDAA-ACCT OF TDAACCT TO TDB-TDAA-ACCT OF TDB-TDAACCT.\n042954     MOVE TDAA-STATUS OF TDAACCT TO TDB-TDAA-STATUS OF            \n042956         TDB-TDAACCT.\n042958     MOVE TDAA-IRA-TYPE OF TDAACCT TO TDB-TDAA-IRA-TYPE OF        \n042960         TDB-TDAACCT.\n042962     MOVE TDAA-ACCT-OPTION OF TDAACCT TO TDB-TDAA-ACCT-OPTION OF  \n042964         TDB-TDAACCT.\n042966     MOVE TDAA-DT-CONDENSED OF TDAACCT TO TDB-TDAA-DT-CONDENSED   \n042968         OF TDB-TDAACCT.\n042970     MOVE TDAA-CERT OF TDAACCT TO TDB-TDAA-CERT OF TDB-TDAACCT.\n042972     MOVE TDAA-SHT-NAME OF TDAACCT TO TDB-TDAA-SHT-NAME OF        \n042974         TDB-TDAACCT.\n042976     MOVE TDAA-TITLE OF TDAACCT TO TDB-TDAA-TITLE OF TDB-TDAACCT.\n042978     MOVE TDAA-TITLE-PRINT OF TDAACCT TO TDB-TDAA-TITLE-PRINT OF  \n042980         TDB-TDAACCT.\n042982     MOVE TDAA-ADDR-USAGE OF TDAACCT TO TDB-TDAA-ADDR-USAGE OF    \n042984         TDB-TDAACCT.\n042986     MOVE TDAA-ADDR-ALT OF TDAACCT TO TDB-TDAA-ADDR-ALT OF        \n042988         TDB-TDAACCT.\n042990     MOVE TDAA-ADDR-TEMP OF TDAACCT TO TDB-TDAA-ADDR-TEMP OF      \n042992         TDB-TDAACCT.\n042994     MOVE TDAA-TEMP-BEG-DT OF TDAACCT TO TDB-TDAA-TEMP-BEG-DT OF  \n042996         TDB-TDAACCT.\n042998     MOVE TDAA-TEMP-END-DT OF TDAACCT TO TDB-TDAA-TEMP-END-DT OF  \n043000         TDB-TDAACCT.\n043002     MOVE TDAA-TEMP-EFF-DT OF TDAACCT TO TDB-TDAA-TEMP-EFF-DT OF  \n043004         TDB-TDAACCT.\n043006     MOVE TDAA-TEMP-EXP-DT OF TDAACCT TO TDB-TDAA-TEMP-EXP-DT OF  \n043008         TDB-TDAACCT.\n043010     MOVE TDAA-END-OF-INT OF TDAACCT TO TDB-TDAA-END-OF-INT OF    \n043012         TDB-TDAACCT.\n043014     MOVE TDAA-END-OF-MAT OF TDAACCT TO TDB-TDAA-END-OF-MAT OF    \n043016         TDB-TDAACCT.\n043018     MOVE TDAA-END-OF-STMT OF TDAACCT TO TDB-TDAA-END-OF-STMT OF  \n043020         TDB-TDAACCT.\n043022     MOVE TDAA-END-OF-CMPD OF TDAACCT TO TDB-TDAA-END-OF-CMPD OF  \n043024         TDB-TDAACCT.\n043026     MOVE TDAA-END-OF-FEE OF TDAACCT TO TDB-TDAA-END-OF-FEE OF    \n043028         TDB-TDAACCT.\n043030     MOVE TDAA-OFFICER OF TDAACCT TO TDB-TDAA-OFFICER OF          \n043032         TDB-TDAACCT.\n043034     MOVE TDAA-OFFICER-2 OF TDAACCT TO TDB-TDAA-OFFICER-2 OF      \n043036         TDB-TDAACCT.\n043038     MOVE TDAA-OFFICER-3 OF TDAACCT TO TDB-TDAA-OFFICER-3 OF      \n043040         TDB-TDAACCT.\n043042     MOVE TDAA-FREE-MARK OF TDAACCT TO TDB-TDAA-FREE-MARK OF      \n043044         TDB-TDAACCT.\n043046     MOVE TDAA-CLASS-CD OF TDAACCT TO TDB-TDAA-CLASS-CD OF        \n043048         TDB-TDAACCT.\n043050     MOVE TDAA-CORR-BK-CD OF TDAACCT TO TDB-TDAA-CORR-BK-CD OF    \n043052         TDB-TDAACCT.\n043054     MOVE TDAA-PUBLIC-FUND OF TDAACCT TO TDB-TDAA-PUBLIC-FUND OF  \n043056         TDB-TDAACCT.\n043058     MOVE TDAA-TRUST-CD OF TDAACCT TO TDB-TDAA-TRUST-CD OF        \n043060         TDB-TDAACCT.\n043062     MOVE TDAA-RT-CHG-ALLOW OF TDAACCT TO TDB-TDAA-RT-CHG-ALLOW   \n043064         OF TDB-TDAACCT.\n043066     MOVE TDAA-WTHDRW-ALLOW OF TDAACCT TO TDB-TDAA-WTHDRW-ALLOW   \n043068         OF TDB-TDAACCT.\n043070     MOVE TDAA-DPOSIT-ALLOW OF TDAACCT TO TDB-TDAA-DPOSIT-ALLOW   \n043072         OF TDB-TDAACCT.\n043074     MOVE TDAA-POST-MAT OF TDAACCT TO TDB-TDAA-POST-MAT OF        \n043076         TDB-TDAACCT.\n043078     MOVE TDAA-RT-FLOOR OF TDAACCT TO TDB-TDAA-RT-FLOOR OF        \n043080         TDB-TDAACCT.\n043082     MOVE TDAA-REPO-CD OF TDAACCT TO TDB-TDAA-REPO-CD OF          \n043084         TDB-TDAACCT.\n043086     MOVE TDAA-TOTAL-CD OF TDAACCT TO TDB-TDAA-TOTAL-CD OF        \n043088         TDB-TDAACCT.\n043090     MOVE TDAA-REN-TOTAL-CD OF TDAACCT TO TDB-TDAA-REN-TOTAL-CD   \n043092         OF TDB-TDAACCT.\n043094     MOVE TDAA-ORG-TOTAL-CD OF TDAACCT TO TDB-TDAA-ORG-TOTAL-CD   \n043096         OF TDB-TDAACCT.\n043098     MOVE TDAA-INQ-SECR-CD OF TDAACCT TO TDB-TDAA-INQ-SECR-CD OF  \n043100         TDB-TDAACCT.\n043102     MOVE TDAA-MAIL-CD OF TDAACCT TO TDB-TDAA-MAIL-CD OF          \n043104         TDB-TDAACCT.\n043106     MOVE TDAA-WTHD-REQD-CD OF TDAACCT TO TDB-TDAA-WTHD-REQD-CD   \n043108         OF TDB-TDAACCT.\n043110     MOVE TDAA-TICKLER-FLAG OF TDAACCT TO TDB-TDAA-TICKLER-FLAG   \n043112         OF TDB-TDAACCT.\n043114     MOVE TDAA-DISP-CD OF TDAACCT TO TDB-TDAA-DISP-CD OF          \n043116         TDB-TDAACCT.\n043118     MOVE TDAA-CLS-DISP-CD OF TDAACCT TO TDB-TDAA-CLS-DISP-CD OF  \n043120         TDB-TDAACCT.\n043122     MOVE TDAA-DIST-STATUS OF TDAACCT TO TDB-TDAA-DIST-STATUS OF  \n043124         TDB-TDAACCT.\n043126     MOVE TDAA-COMM-ACCT OF TDAACCT TO TDB-TDAA-COMM-ACCT OF      \n043128         TDB-TDAACCT.\n043130     MOVE TDAA-RENEW-CD OF TDAACCT TO TDB-TDAA-RENEW-CD OF        \n043132         TDB-TDAACCT.\n043134     MOVE TDAA-PLEDGE-CD OF TDAACCT TO TDB-TDAA-PLEDGE-CD OF      \n043136         TDB-TDAACCT.\n043138     MOVE TDAA-NEGOT-CD OF TDAACCT TO TDB-TDAA-NEGOT-CD OF        \n043140         TDB-TDAACCT.\n043142     MOVE TDAA-BENEF-CD OF TDAACCT TO TDB-TDAA-BENEF-CD OF        \n043144         TDB-TDAACCT.\n043146     MOVE TDAA-COMM-MAT-CD OF TDAACCT TO TDB-TDAA-COMM-MAT-CD OF  \n043148         TDB-TDAACCT.\n043150     MOVE TDAA-NBR-BENEF OF TDAACCT TO TDB-TDAA-NBR-BENEF OF      \n043152         TDB-TDAACCT.\n043154     MOVE TDAA-OVERRIDE OF TDAACCT TO TDB-TDAA-OVERRIDE OF        \n043156         TDB-TDAACCT.\n043158     MOVE TDAA-INT-CD OF TDAACCT TO TDB-TDAA-INT-CD OF            \n043160         TDB-TDAACCT.\n043162     MOVE TDAA-WTHLD-CD OF TDAACCT TO TDB-TDAA-WTHLD-CD OF        \n043164         TDB-TDAACCT.\n043166     MOVE TDAA-WTHLD-AMT OF TDAACCT TO TDB-TDAA-WTHLD-AMT OF      \n043168         TDB-TDAACCT.\n043170     MOVE TDAA-IGL-GRP OF TDAACCT TO TDB-TDAA-IGL-GRP OF          \n043172         TDB-TDAACCT.\n043174     MOVE TDAA-SUM-STMT-CD OF TDAACCT TO TDB-TDAA-SUM-STMT-CD OF  \n043176         TDB-TDAACCT.\n043178     MOVE TDAA-REN-NTC-CD OF TDAACCT TO TDB-TDAA-REN-NTC-CD OF    \n043180         TDB-TDAACCT.\n043182     MOVE TDAA-PMAT-NTC-CD OF TDAACCT TO TDB-TDAA-PMAT-NTC-CD OF  \n043184         TDB-TDAACCT.\n043186     MOVE TDAA-RTCHG-NTC-CD OF TDAACCT TO TDB-TDAA-RTCHG-NTC-CD   \n043188         OF TDB-TDAACCT.\n043190     MOVE TDAA-INT-NTC-CD OF TDAACCT TO TDB-TDAA-INT-NTC-CD OF    \n043192         TDB-TDAACCT.\n043194     MOVE TDAA-CHG-NTC OF TDAACCT TO TDB-TDAA-CHG-NTC OF          \n043196         TDB-TDAACCT.\n043198     MOVE TDAA-YIELD-NUM OF TDAACCT TO TDB-TDAA-YIELD-NUM OF      \n043200         TDB-TDAACCT.\n043202     MOVE TDAA-YIELD-DENOM OF TDAACCT TO TDB-TDAA-YIELD-DENOM OF  \n043204         TDB-TDAACCT.\n043206     MOVE TDAA-CMPD-FREQ OF TDAACCT TO TDB-TDAA-CMPD-FREQ OF      \n043208         TDB-TDAACCT.\n043210     MOVE TDAA-CMPD-NTRVL OF TDAACCT TO TDB-TDAA-CMPD-NTRVL OF    \n043212         TDB-TDAACCT.\n043214     MOVE TDAA-RT-CHG-LIMIT OF TDAACCT TO TDB-TDAA-RT-CHG-LIMIT   \n043216         OF TDB-TDAACCT.\n043218     MOVE TDAA-VAR-RT-IMMED OF TDAACCT TO TDB-TDAA-VAR-RT-IMMED   \n043220         OF TDB-TDAACCT.\n043222     MOVE TDAA-VAR-RT-INT OF TDAACCT TO TDB-TDAA-VAR-RT-INT OF    \n043224         TDB-TDAACCT.\n043226     MOVE TDAA-VAR-RT-SCHED OF TDAACCT TO TDB-TDAA-VAR-RT-SCHED   \n043228         OF TDB-TDAACCT.\n043230     MOVE TDAA-VAR-RT-CUST OF TDAACCT TO TDB-TDAA-VAR-RT-CUST OF  \n043232         TDB-TDAACCT.\n043234     MOVE TDAA-VAR-RT-BAL OF TDAACCT TO TDB-TDAA-VAR-RT-BAL OF    \n043236         TDB-TDAACCT.\n043238     MOVE TDAA-RT-INDX-CD OF TDAACCT TO TDB-TDAA-RT-INDX-CD OF    \n043240         TDB-TDAACCT.\n043242     MOVE TDAA-R-RT-INDX-CD OF TDAACCT TO TDB-TDAA-R-RT-INDX-CD   \n043244         OF TDB-TDAACCT.\n043246     MOVE TDAA-RT-MARG-CD OF TDAACCT TO TDB-TDAA-RT-MARG-CD OF    \n043248         TDB-TDAACCT.\n043250     MOVE TDAA-R-RT-MARG-CD OF TDAACCT TO TDB-TDAA-R-RT-MARG-CD   \n043252         OF TDB-TDAACCT.\n043254     MOVE TDAA-RT-TIER-CD OF TDAACCT TO TDB-TDAA-RT-TIER-CD OF    \n043256         TDB-TDAACCT.\n043258     MOVE TDAA-R-RT-TIER-CD OF TDAACCT TO TDB-TDAA-R-RT-TIER-CD   \n043260         OF TDB-TDAACCT.\n043262     MOVE TDAA-RT-SR-CD OF TDAACCT TO TDB-TDAA-RT-SR-CD OF        \n043264         TDB-TDAACCT.\n043266     MOVE TDAA-R-RT-SR-CD OF TDAACCT TO TDB-TDAA-R-RT-SR-CD OF    \n043268         TDB-TDAACCT.\n043270     MOVE TDAA-RT-REGN-CD OF TDAACCT TO TDB-TDAA-RT-REGN-CD OF    \n043272         TDB-TDAACCT.\n043274     MOVE TDAA-RT-CHG-NTRVL OF TDAACCT TO TDB-TDAA-RT-CHG-NTRVL   \n043276         OF TDB-TDAACCT.\n043278     MOVE TDAA-CAP-RT-CHG OF TDAACCT TO TDB-TDAA-CAP-RT-CHG OF    \n043280         TDB-TDAACCT.\n043282     MOVE TDAA-R-TIER-RT-CH OF TDAACCT TO TDB-TDAA-R-TIER-RT-CH   \n043284         OF TDB-TDAACCT.\n043286     MOVE TDAA-ALERT-CD OF TDAACCT TO TDB-TDAA-ALERT-CD OF        \n043288         TDB-TDAACCT.\n043290     MOVE TDAA-ALERT-CD-2 OF TDAACCT TO TDB-TDAA-ALERT-CD-2 OF    \n043292         TDB-TDAACCT.\n043294     MOVE TDAA-ALERT-CD-3 OF TDAACCT TO TDB-TDAA-ALERT-CD-3 OF    \n043296         TDB-TDAACCT.\n043298     MOVE TDAA-CENSUS-TRACT OF TDAACCT TO TDB-TDAA-CENSUS-TRACT   \n043300         OF TDB-TDAACCT.\n043302     MOVE TDAA-MK-SEGMENT OF TDAACCT TO TDB-TDAA-MK-SEGMENT OF    \n043304         TDB-TDAACCT.\n043306     MOVE TDAA-BK-DEF-TOT OF TDAACCT TO TDB-TDAA-BK-DEF-TOT OF    \n043308         TDB-TDAACCT.\n043310     MOVE TDAA-BK-DEF-CD1 OF TDAACCT TO TDB-TDAA-BK-DEF-CD1 OF    \n043312         TDB-TDAACCT.\n043314     MOVE TDAA-BK-DEF-CD2 OF TDAACCT TO TDB-TDAA-BK-DEF-CD2 OF    \n043316         TDB-TDAACCT.\n043318     MOVE TDAA-BK-DEF-CD3 OF TDAACCT TO TDB-TDAA-BK-DEF-CD3 OF    \n043320         TDB-TDAACCT.\n043322     MOVE TDAA-BK-DEF-CD4 OF TDAACCT TO TDB-TDAA-BK-DEF-CD4 OF    \n043324         TDB-TDAACCT.\n043326     MOVE TDAA-BK-DEF-CD5 OF TDAACCT TO TDB-TDAA-BK-DEF-CD5 OF    \n043328         TDB-TDAACCT.\n043330     MOVE TDAA-OID-METH OF TDAACCT TO TDB-TDAA-OID-METH OF        \n043332         TDB-TDAACCT.\n043334     MOVE TDAA-EOY-CD OF TDAACCT TO TDB-TDAA-EOY-CD OF            \n043336         TDB-TDAACCT.\n043338     MOVE TDAA-B-NOTC-YR1 OF TDAACCT TO TDB-TDAA-B-NOTC-YR1 OF    \n043340         TDB-TDAACCT.\n043342     MOVE TDAA-B-NOTC-YR2 OF TDAACCT TO TDB-TDAA-B-NOTC-YR2 OF    \n043344         TDB-TDAACCT.\n043346     MOVE TDAA-B-NOTC-YR3 OF TDAACCT TO TDB-TDAA-B-NOTC-YR3 OF    \n043348         TDB-TDAACCT.\n043350     MOVE TDAA-NO-COMB-IRS OF TDAACCT TO TDB-TDAA-NO-COMB-IRS OF  \n043352         TDB-TDAACCT.\n043354     MOVE TDAA-PENLTY-CD OF TDAACCT TO TDB-TDAA-PENLTY-CD OF      \n043356         TDB-TDAACCT.\n043358     MOVE TDAA-MONEY-SRC-CD OF TDAACCT TO TDB-TDAA-MONEY-SRC-CD   \n043360         OF TDB-TDAACCT.\n043362     MOVE TDAA-INTERNET-BPY OF TDAACCT TO TDB-TDAA-INTERNET-BPY   \n043364         OF TDB-TDAACCT.\n043366     MOVE TDAA-INTERNET-TFR OF TDAACCT TO TDB-TDAA-INTERNET-TFR   \n043368         OF TDB-TDAACCT.\n043370     MOVE TDAA-INTERNET-INQ OF TDAACCT TO TDB-TDAA-INTERNET-INQ   \n043372         OF TDB-TDAACCT.\n043374     MOVE TDAA-IRA-BACKED OF TDAACCT TO TDB-TDAA-IRA-BACKED OF    \n043376         TDB-TDAACCT.\n043378     MOVE TDAA-SAV-DEPOSIT OF TDAACCT TO TDB-TDAA-SAV-DEPOSIT OF  \n043380         TDB-TDAACCT.\n043382     MOVE TDAA-MAT-TYPE OF TDAACCT TO TDB-TDAA-MAT-TYPE OF        \n043384         TDB-TDAACCT.\n043386     MOVE TDAA-MAT-TERM OF TDAACCT TO TDB-TDAA-MAT-TERM OF        \n043388         TDB-TDAACCT.\n043390     MOVE TDAA-ORG-MAT-TYPE OF TDAACCT TO TDB-TDAA-ORG-MAT-TYPE   \n043392         OF TDB-TDAACCT.\n043394     MOVE TDAA-ORG-MAT-TERM OF TDAACCT TO TDB-TDAA-ORG-MAT-TERM   \n043396         OF TDB-TDAACCT.\n043398     MOVE TDAA-ODD-PAYMENT OF TDAACCT TO TDB-TDAA-ODD-PAYMENT OF  \n043400         TDB-TDAACCT.\n043402     MOVE TDAA-PAY-FREQ OF TDAACCT TO TDB-TDAA-PAY-FREQ OF        \n043404         TDB-TDAACCT.\n043406     MOVE TDAA-PAY-NTRVL OF TDAACCT TO TDB-TDAA-PAY-NTRVL OF      \n043408         TDB-TDAACCT.\n043410     MOVE TDAA-FEE-FREQ OF TDAACCT TO TDB-TDAA-FEE-FREQ OF        \n043412         TDB-TDAACCT.\n043414     MOVE TDAA-FEE-NTRVL OF TDAACCT TO TDB-TDAA-FEE-NTRVL OF      \n043416         TDB-TDAACCT.\n043418     MOVE TDAA-STMT-FREQ OF TDAACCT TO TDB-TDAA-STMT-FREQ OF      \n043420         TDB-TDAACCT.\n043422     MOVE TDAA-STMT-NTRVL OF TDAACCT TO TDB-TDAA-STMT-NTRVL OF    \n043424         TDB-TDAACCT.\n043426     MOVE TDAA-EMPLOYEE-ID OF TDAACCT TO TDB-TDAA-EMPLOYEE-ID OF  \n043428         TDB-TDAACCT.\n043430     MOVE TDAA-EFT-CARD OF TDAACCT TO TDB-TDAA-EFT-CARD OF        \n043432         TDB-TDAACCT.\n043434     MOVE TDAA-PEN-WAV-RESN OF TDAACCT TO TDB-TDAA-PEN-WAV-RESN   \n043436         OF TDB-TDAACCT.\n043438     MOVE TDAA-CLOSED-RESN OF TDAACCT TO TDB-TDAA-CLOSED-RESN OF  \n043440         TDB-TDAACCT.\n043442     MOVE TDAA-SPECIAL-STMT OF TDAACCT TO TDB-TDAA-SPECIAL-STMT   \n043444         OF TDB-TDAACCT.\n043446     MOVE TDAA-CLS-THIS-MTH OF TDAACCT TO TDB-TDAA-CLS-THIS-MTH   \n043448         OF TDB-TDAACCT.\n043450     MOVE TDAA-RC-MAT-ONLY OF TDAACCT TO TDB-TDAA-RC-MAT-ONLY OF  \n043452         TDB-TDAACCT.\n043454     MOVE TDAA-GRACE-DAYS OF TDAACCT TO TDB-TDAA-GRACE-DAYS OF    \n043456         TDB-TDAACCT.\n043458     MOVE TDAA-CLS-ON-MAT OF TDAACCT TO TDB-TDAA-CLS-ON-MAT OF    \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    480 lines from 21246 to 21725.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 44, "total_chunks": 55, "start_line": 21246, "end_line": 21725, "line_count": 480}

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
- Source code length: 25986 characters

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
CHUNK 44 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 21246 to 21725 (480 lines)
Chunk Tokens (estimated): ~8,074
Actual Input Tokens: 9,480 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 21246-21725 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 44 of 55 chunks
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
      The source code below is only CHUNK 44 of 55.


=============================================================================
CHUNK 44 SOURCE CODE (Lines 21246-21725)
=============================================================================

```cobol
042500 Z-26-4-BEGIN.
042502*      REQUESTED UPDATE OF FILE CST-FILE-MAINT
042504     MOVE 7 TO Z-FLINFO6-UPDATE.
042506     MOVE WS-BANK-NO TO FM2-BANK.
042508     MOVE WS-TIN-CUST (J) TO FM2-CUST.
042510     MOVE ZEROS TO FM2-ACCT.
042512     MOVE 01 TO FM2-STRUCT.
042514     MOVE 00 TO FM2-RECORD-NBR.
042516     MOVE 0863 TO FM2-TRANCODE.
042518     MOVE WS-TIN-RMD-TOT TO WS-FM-AMT.
042520     MOVE WS-FM-AMT-X TO FM2-CHANGE-DATA.
042522     MOVE "R" TO FM2-APPLY.
042524     MOVE "RMDRPT" TO FM2-ORIGIN.
042526     MOVE SPACE TO FM2-INT
042528       , FM2-SYSTEM-USE.
042530     IF Z-EDIT-ERROR
042532         GO TO Z-26-XIT.
042534     IF Z-FLINFO6-UPDATE = 7
042536         NEXT SENTENCE ELSE
042538         GO TO Z-26-5-SKIP.
042540     WRITE MASS-FM-RECORD2
042542         INVALID KEY
042544         MOVE Z-FLINFO6-STATUS TO Z-FL-EXCEPT-STATUS
042546         MOVE "CST-FILE-MAINT" TO Z-FL-EXCEPT-FILE
042548         MOVE 1761 TO Z-FL-EXCEPT-SEQ
042550         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.
042552     MOVE Z-FILE6-KEY TO Z-FLINFO6-RS-KEY.
042554     MOVE ZERO TO Z-FLINFO6-UPDATE.
042556     MOVE ZERO TO Z-FLINFO6-LAST-SEQ.
042558 Z-26-5-SKIP.
042560 Z-26-4-SKIP.
042562*
042564 Z-26-4-XIT.
042566     MOVE 0 TO Z-EXIT-CODE.
042568     MOVE 9999 TO Z-EXIT-LEVEL.
042570     MOVE SPACES TO MASS-FM-RECORD2.
042572 Z-26-2-END.
042574     IF Z-EDIT-ERROR
042576         GO TO Z-26-XIT.
042578 Z-26-2-SKIP.
042580     IF Z-EXIT-LEVEL < 1
042582         GO TO Z-26-END.
042584     IF Z-EXIT-CODE > 0
042586         GO TO Z-26-2-XIT.
042588     ADD 1 TO J.
042590     GO TO Z-26-2-LOOP.
042592*
042594 Z-26-2-XIT.
042596     MOVE 0 TO Z-EXIT-CODE.
042598     MOVE 9999 TO Z-EXIT-LEVEL.
042600     MOVE SPACES TO WS-TIN-CUST-TABLE.
042602     MOVE 0 TO WS-TIN-CUST-INDEX.
042604 Z-26-1-1-ELSE.
042606 Z-26-END.
042608     IF Z-EDIT-ERROR
042610         GO TO Z-26-XIT.
042612 Z-26-SKIP.
042614 Z-26-XIT.
042616     EXIT.
042618*
042620*****************************************************************
042622*    PROCEDURE COMB-AUTO-RMD-ADJ
042624*****************************************************************
042626 Z-27-PROCEDURE.
042628*
042630     IF WS-DSTFM-OPEN = 0
042632         NEXT SENTENCE ELSE
042634         GO TO Z-27-1-1-ELSE.
042636     MOVE PROCESS-DATE-MMDD TO WS-DSTFM-DT.
042638     IF WS-BANK-OPT = 1
042640         NEXT SENTENCE ELSE
042642         GO TO Z-27-3-1-ELSE.
042644     MOVE WS-BANK-NO TO WS-DSTFM-BK.
042646     MOVE SPACES TO WS-DSTFM-TIME.
042648     GO TO Z-27-3-ENDIF.
042650 Z-27-3-1-ELSE.
042652     IF WS-BANK-OPT = 2
042654         NEXT SENTENCE ELSE
042656         GO TO Z-27-3-2-ELSE.
042658     MOVE 000 TO WS-DSTFM-BK.
042660*    RETRIEVE TODAY'S DATE
042662     CALL "CURRENT_DATE OF GENERALSUPPORT"
042664          USING Z-CALL-CURRENTDATE.
042666     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
042668     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
042670     ACCEPT Z-DATE0-TIME   FROM TIME.
042672     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.
042674     MOVE Z-DATE0-UU TO Z-DATE4-UU.
042676     MOVE Z-DATE4-FORMAT TO WS-DSTFM-TIME.
042678     GO TO Z-27-3-ENDIF.
042680 Z-27-3-2-ELSE.
042682     IF WS-BANK-OPT = 3
042684         NEXT SENTENCE ELSE
042686         GO TO Z-27-3-3-ELSE.
042688     MOVE 000 TO WS-DSTFM-BK.
042690     MOVE SPACES TO WS-DSTFM-SUFF-R.
042692     MOVE WS-SUFFIX-IN TO WS-DSTFM-SUFF.
042694 Z-27-3-3-ELSE.
042696 Z-27-3-ENDIF.
042698*
042700******* OPEN FILE DST-FILE-MAINT
042702*
042704     IF Z-FLINFO5-OPEN = 0
042706         CHANGE ATTRIBUTE NEWFILE OF DST-FILE-MAINT TO VALUE TRUE
042708         OPEN OUTPUT DST-FILE-MAINT 
042710         IF ATTRIBUTE FILESTATE OF DST-FILE-MAINT = VALUE OPENED
042712             MOVE ZEROS TO Z-FILE5-KEY
042714             MOVE ZEROS TO Z-FLINFO5-RS-KEY
042716             MOVE 3 TO Z-FLINFO5-OPEN
042718             MOVE 3 TO Z-FLINFO5-RS-OPEN
042720         ELSE
042722             DISPLAY ">>> FILE DST-FILE-MAINT FAILED TO OPEN"
042724             MOVE ATTRIBUTE TITLE OF DST-FILE-MAINT TO            
042726                 Z-FL-EXCEPT-TITLE
042728             DISPLAY ">>> OPEN FAIL, TITLE :", Z-FL-EXCEPT-TITLE
042730             DISPLAY ">>>>>> SUBSEQUENT I/O WILL CAUSE ERRORS".
042732     MOVE 1 TO WS-DSTFM-OPEN.
042734 Z-27-1-1-ELSE.
042736     MOVE 1 TO J.
042738     COMPUTE Z-TO-3 = WS-TIN-RMD-MAX.
042740 Z-27-13-LOOP.
042742     IF J > Z-TO-3
042744         GO TO Z-27-13-XIT.
042746     MOVE 0 TO Z-EXIT-CODE.
042748     MOVE 9999 TO Z-EXIT-LEVEL.
042750********* EXIT WHEN
042752     IF WS-TIN-RMD-CUST (J) = 0
042754        NEXT SENTENCE
042756     ELSE
042758        GO TO Z-27-14-EXIT-SKIP.
042760     MOVE 1 TO Z-EXIT-LEVEL.
042762     MOVE 1 TO Z-EXIT-CODE.
042764     GO TO Z-27-13-END.
042766 Z-27-14-EXIT-SKIP.
042768 Z-27-15-BEGIN.
042770*      REQUESTED UPDATE OF FILE DST-FILE-MAINT
042772     MOVE 8 TO Z-FLINFO5-UPDATE.
042774     MOVE WS-BANK-NO TO FM-BANK.
042776     MOVE WS-TIN-RMD-CUST (J) TO FM-CUST.
042778     MOVE WS-TIN-RMD-ACCT (J) TO FM-ACCT.
042780     MOVE 15 TO FM-STRUCT.
042782     MOVE WS-TIN-RMD-DS-NBR (J) TO FM-RECORD-NBR.
042784     MOVE 0712 TO FM-TRANCODE.
042786     IF WS-TIN-DISTR-RECS = 1
042788         NEXT SENTENCE ELSE
042790         GO TO Z-27-23-1-ELSE.
042792     IF WS-TIN-RMD-DS-FREQ (J) = 1
042794         NEXT SENTENCE ELSE
042796         GO TO Z-27-24-1-ELSE.
042798     COMPUTE WS-FM-AMT ROUNDED = ( ( WS-TIN-RMD-TOT / 365 ) *     
042800         WS-TIN-RMD-DS-NTRVL (J) ) .
042802
042804     GO TO Z-27-24-ENDIF.
042806 Z-27-24-1-ELSE.
042808     IF WS-TIN-RMD-DS-FREQ (J) = 2
042810         NEXT SENTENCE ELSE
042812         GO TO Z-27-24-2-ELSE.
042814     COMPUTE WS-FM-AMT ROUNDED = ( ( WS-TIN-RMD-TOT / 12 ) *      
042816         WS-TIN-RMD-DS-NTRVL (J) ) .
042818
042820     GO TO Z-27-24-ENDIF.
042822 Z-27-24-2-ELSE.
042824     COMPUTE WS-FM-AMT = WS-TIN-RMD-TOT .
042826
042828 Z-27-24-ENDIF.
042830     GO TO Z-27-23-ENDIF.
042832 Z-27-23-1-ELSE.
042834     MOVE WS-TIN-RMD-AMT (J) TO WS-FM-AMT.
042836 Z-27-23-ENDIF.
042838     MOVE WS-FM-AMT-X TO FM-CHANGE-DATA.
042840     MOVE "R" TO FM-APPLY.
042842     MOVE "RMDRPT" TO FM-ORIGIN.
042844     MOVE SPACE TO FM-INT.
042846     MOVE SPACE TO FM-SYSTEM-USE.
042848     IF Z-EDIT-ERROR
042850         GO TO Z-27-XIT.
042852     IF Z-FLINFO5-UPDATE = 8
042854         NEXT SENTENCE ELSE
042856         GO TO Z-27-16-SKIP.
042858     WRITE MASS-FM-RECORD
042860         INVALID KEY
042862         MOVE Z-FLINFO5-STATUS TO Z-FL-EXCEPT-STATUS
042864         MOVE "DST-FILE-MAINT" TO Z-FL-EXCEPT-FILE
042866         MOVE 1821 TO Z-FL-EXCEPT-SEQ
042868         PERFORM Z-FL-EXCEPTION THRU Z-FL-EXCEPTION-XIT.
042870     MOVE Z-FILE5-KEY TO Z-FLINFO5-RS-KEY.
042872     MOVE ZERO TO Z-FLINFO5-UPDATE.
042874     MOVE ZERO TO Z-FLINFO5-LAST-SEQ.
042876 Z-27-16-SKIP.
042878 Z-27-15-SKIP.
042880*
042882 Z-27-15-XIT.
042884     MOVE 0 TO Z-EXIT-CODE.
042886     MOVE 9999 TO Z-EXIT-LEVEL.
042888 Z-27-13-END.
042890     IF Z-EDIT-ERROR
042892         GO TO Z-27-XIT.
042894 Z-27-13-SKIP.
042896     IF Z-EXIT-LEVEL < 1
042898         GO TO Z-27-END.
042900     IF Z-EXIT-CODE > 0
042902         GO TO Z-27-13-XIT.
042904     ADD 1 TO J.
042906     GO TO Z-27-13-LOOP.
042908*
042910 Z-27-13-XIT.
042912     MOVE 0 TO Z-EXIT-CODE.
042914     MOVE 9999 TO Z-EXIT-LEVEL.
042916     MOVE SPACES TO WS-TIN-RMD-TABLE.
042918     MOVE 0 TO WS-TIN-RMD-INDEX.
042920 Z-27-END.
042922     IF Z-EDIT-ERROR
042924         GO TO Z-27-XIT.
042926 Z-27-SKIP.
042928 Z-27-XIT.
042930     EXIT.
042932*
042934*****************************************************************
042936*    PROCEDURE TDD-TDAA-MOVE-TO-TDB
042938*****************************************************************
042940 Z-12-PROCEDURE.
042942*
042944     MOVE TDAA-BANK OF TDAACCT TO TDB-TDAA-BANK OF TDB-TDAACCT.
042946     MOVE TDAA-BRCH OF TDAACCT TO TDB-TDAA-BRCH OF TDB-TDAACCT.
042948     MOVE TDAA-APPL OF TDAACCT TO TDB-TDAA-APPL OF TDB-TDAACCT.
042950     MOVE TDAA-CUST OF TDAACCT TO TDB-TDAA-CUST OF TDB-TDAACCT.
042952     MOVE TDAA-ACCT OF TDAACCT TO TDB-TDAA-ACCT OF TDB-TDAACCT.
042954     MOVE TDAA-STATUS OF TDAACCT TO TDB-TDAA-STATUS OF            
042956         TDB-TDAACCT.
042958     MOVE TDAA-IRA-TYPE OF TDAACCT TO TDB-TDAA-IRA-TYPE OF        
042960         TDB-TDAACCT.
042962     MOVE TDAA-ACCT-OPTION OF TDAACCT TO TDB-TDAA-ACCT-OPTION OF  
042964         TDB-TDAACCT.
042966     MOVE TDAA-DT-CONDENSED OF TDAACCT TO TDB-TDAA-DT-CONDENSED   
042968         OF TDB-TDAACCT.
042970     MOVE TDAA-CERT OF TDAACCT TO TDB-TDAA-CERT OF TDB-TDAACCT.
042972     MOVE TDAA-SHT-NAME OF TDAACCT TO TDB-TDAA-SHT-NAME OF        
042974         TDB-TDAACCT.
042976     MOVE TDAA-TITLE OF TDAACCT TO TDB-TDAA-TITLE OF TDB-TDAACCT.
042978     MOVE TDAA-TITLE-PRINT OF TDAACCT TO TDB-TDAA-TITLE-PRINT OF  
042980         TDB-TDAACCT.
042982     MOVE TDAA-ADDR-USAGE OF TDAACCT TO TDB-TDAA-ADDR-USAGE OF    
042984         TDB-TDAACCT.
042986     MOVE TDAA-ADDR-ALT OF TDAACCT TO TDB-TDAA-ADDR-ALT OF        
042988         TDB-TDAACCT.
042990     MOVE TDAA-ADDR-TEMP OF TDAACCT TO TDB-TDAA-ADDR-TEMP OF      
042992         TDB-TDAACCT.
042994     MOVE TDAA-TEMP-BEG-DT OF TDAACCT TO TDB-TDAA-TEMP-BEG-DT OF  
042996         TDB-TDAACCT.
042998     MOVE TDAA-TEMP-END-DT OF TDAACCT TO TDB-TDAA-TEMP-END-DT OF  
043000         TDB-TDAACCT.
043002     MOVE TDAA-TEMP-EFF-DT OF TDAACCT TO TDB-TDAA-TEMP-EFF-DT OF  
043004         TDB-TDAACCT.
043006     MOVE TDAA-TEMP-EXP-DT OF TDAACCT TO TDB-TDAA-TEMP-EXP-DT OF  
043008         TDB-TDAACCT.
043010     MOVE TDAA-END-OF-INT OF TDAACCT TO TDB-TDAA-END-OF-INT OF    
043012         TDB-TDAACCT.
043014     MOVE TDAA-END-OF-MAT OF TDAACCT TO TDB-TDAA-END-OF-MAT OF    
043016         TDB-TDAACCT.
043018     MOVE TDAA-END-OF-STMT OF TDAACCT TO TDB-TDAA-END-OF-STMT OF  
043020         TDB-TDAACCT.
043022     MOVE TDAA-END-OF-CMPD OF TDAACCT TO TDB-TDAA-END-OF-CMPD OF  
043024         TDB-TDAACCT.
043026     MOVE TDAA-END-OF-FEE OF TDAACCT TO TDB-TDAA-END-OF-FEE OF    
043028         TDB-TDAACCT.
043030     MOVE TDAA-OFFICER OF TDAACCT TO TDB-TDAA-OFFICER OF          
043032         TDB-TDAACCT.
043034     MOVE TDAA-OFFICER-2 OF TDAACCT TO TDB-TDAA-OFFICER-2 OF      
043036         TDB-TDAACCT.
043038     MOVE TDAA-OFFICER-3 OF TDAACCT TO TDB-TDAA-OFFICER-3 OF      
043040         TDB-TDAACCT.
043042     MOVE TDAA-FREE-MARK OF TDAACCT TO TDB-TDAA-FREE-MARK OF      
043044         TDB-TDAACCT.
043046     MOVE TDAA-CLASS-CD OF TDAACCT TO TDB-TDAA-CLASS-CD OF        
043048         TDB-TDAACCT.
043050     MOVE TDAA-CORR-BK-CD OF TDAACCT TO TDB-TDAA-CORR-BK-CD OF    
043052         TDB-TDAACCT.
043054     MOVE TDAA-PUBLIC-FUND OF TDAACCT TO TDB-TDAA-PUBLIC-FUND OF  
043056         TDB-TDAACCT.
043058     MOVE TDAA-TRUST-CD OF TDAACCT TO TDB-TDAA-TRUST-CD OF        
043060         TDB-TDAACCT.
043062     MOVE TDAA-RT-CHG-ALLOW OF TDAACCT TO TDB-TDAA-RT-CHG-ALLOW   
043064         OF TDB-TDAACCT.
043066     MOVE TDAA-WTHDRW-ALLOW OF TDAACCT TO TDB-TDAA-WTHDRW-ALLOW   
043068         OF TDB-TDAACCT.
043070     MOVE TDAA-DPOSIT-ALLOW OF TDAACCT TO TDB-TDAA-DPOSIT-ALLOW   
043072         OF TDB-TDAACCT.
043074     MOVE TDAA-POST-MAT OF TDAACCT TO TDB-TDAA-POST-MAT OF        
043076         TDB-TDAACCT.
043078     MOVE TDAA-RT-FLOOR OF TDAACCT TO TDB-TDAA-RT-FLOOR OF        
043080         TDB-TDAACCT.
043082     MOVE TDAA-REPO-CD OF TDAACCT TO TDB-TDAA-REPO-CD OF          
043084         TDB-TDAACCT.
043086     MOVE TDAA-TOTAL-CD OF TDAACCT TO TDB-TDAA-TOTAL-CD OF        
043088         TDB-TDAACCT.
043090     MOVE TDAA-REN-TOTAL-CD OF TDAACCT TO TDB-TDAA-REN-TOTAL-CD   
043092         OF TDB-TDAACCT.
043094     MOVE TDAA-ORG-TOTAL-CD OF TDAACCT TO TDB-TDAA-ORG-TOTAL-CD   
043096         OF TDB-TDAACCT.
043098     MOVE TDAA-INQ-SECR-CD OF TDAACCT TO TDB-TDAA-INQ-SECR-CD OF  
043100         TDB-TDAACCT.
043102     MOVE TDAA-MAIL-CD OF TDAACCT TO TDB-TDAA-MAIL-CD OF          
043104         TDB-TDAACCT.
043106     MOVE TDAA-WTHD-REQD-CD OF TDAACCT TO TDB-TDAA-WTHD-REQD-CD   
043108         OF TDB-TDAACCT.
043110     MOVE TDAA-TICKLER-FLAG OF TDAACCT TO TDB-TDAA-TICKLER-FLAG   
043112         OF TDB-TDAACCT.
043114     MOVE TDAA-DISP-CD OF TDAACCT TO TDB-TDAA-DISP-CD OF          
043116         TDB-TDAACCT.
043118     MOVE TDAA-CLS-DISP-CD OF TDAACCT TO TDB-TDAA-CLS-DISP-CD OF  
043120         TDB-TDAACCT.
043122     MOVE TDAA-DIST-STATUS OF TDAACCT TO TDB-TDAA-DIST-STATUS OF  
043124         TDB-TDAACCT.
043126     MOVE TDAA-COMM-ACCT OF TDAACCT TO TDB-TDAA-COMM-ACCT OF      
043128         TDB-TDAACCT.
043130     MOVE TDAA-RENEW-CD OF TDAACCT TO TDB-TDAA-RENEW-CD OF        
043132         TDB-TDAACCT.
043134     MOVE TDAA-PLEDGE-CD OF TDAACCT TO TDB-TDAA-PLEDGE-CD OF      
043136         TDB-TDAACCT.
043138     MOVE TDAA-NEGOT-CD OF TDAACCT TO TDB-TDAA-NEGOT-CD OF        
043140         TDB-TDAACCT.
043142     MOVE TDAA-BENEF-CD OF TDAACCT TO TDB-TDAA-BENEF-CD OF        
043144         TDB-TDAACCT.
043146     MOVE TDAA-COMM-MAT-CD OF TDAACCT TO TDB-TDAA-COMM-MAT-CD OF  
043148         TDB-TDAACCT.
043150     MOVE TDAA-NBR-BENEF OF TDAACCT TO TDB-TDAA-NBR-BENEF OF      
043152         TDB-TDAACCT.
043154     MOVE TDAA-OVERRIDE OF TDAACCT TO TDB-TDAA-OVERRIDE OF        
043156         TDB-TDAACCT.
043158     MOVE TDAA-INT-CD OF TDAACCT TO TDB-TDAA-INT-CD OF            
043160         TDB-TDAACCT.
043162     MOVE TDAA-WTHLD-CD OF TDAACCT TO TDB-TDAA-WTHLD-CD OF        
043164         TDB-TDAACCT.
043166     MOVE TDAA-WTHLD-AMT OF TDAACCT TO TDB-TDAA-WTHLD-AMT OF      
043168         TDB-TDAACCT.
043170     MOVE TDAA-IGL-GRP OF TDAACCT TO TDB-TDAA-IGL-GRP OF          
043172         TDB-TDAACCT.
043174     MOVE TDAA-SUM-STMT-CD OF TDAACCT TO TDB-TDAA-SUM-STMT-CD OF  
043176         TDB-TDAACCT.
043178     MOVE TDAA-REN-NTC-CD OF TDAACCT TO TDB-TDAA-REN-NTC-CD OF    
043180         TDB-TDAACCT.
043182     MOVE TDAA-PMAT-NTC-CD OF TDAACCT TO TDB-TDAA-PMAT-NTC-CD OF  
043184         TDB-TDAACCT.
043186     MOVE TDAA-RTCHG-NTC-CD OF TDAACCT TO TDB-TDAA-RTCHG-NTC-CD   
043188         OF TDB-TDAACCT.
043190     MOVE TDAA-INT-NTC-CD OF TDAACCT TO TDB-TDAA-INT-NTC-CD OF    
043192         TDB-TDAACCT.
043194     MOVE TDAA-CHG-NTC OF TDAACCT TO TDB-TDAA-CHG-NTC OF          
043196         TDB-TDAACCT.
043198     MOVE TDAA-YIELD-NUM OF TDAACCT TO TDB-TDAA-YIELD-NUM OF      
043200         TDB-TDAACCT.
043202     MOVE TDAA-YIELD-DENOM OF TDAACCT TO TDB-TDAA-YIELD-DENOM OF  
043204         TDB-TDAACCT.
043206     MOVE TDAA-CMPD-FREQ OF TDAACCT TO TDB-TDAA-CMPD-FREQ OF      
043208         TDB-TDAACCT.
043210     MOVE TDAA-CMPD-NTRVL OF TDAACCT TO TDB-TDAA-CMPD-NTRVL OF    
043212         TDB-TDAACCT.
043214     MOVE TDAA-RT-CHG-LIMIT OF TDAACCT TO TDB-TDAA-RT-CHG-LIMIT   
043216         OF TDB-TDAACCT.
043218     MOVE TDAA-VAR-RT-IMMED OF TDAACCT TO TDB-TDAA-VAR-RT-IMMED   
043220         OF TDB-TDAACCT.
043222     MOVE TDAA-VAR-RT-INT OF TDAACCT TO TDB-TDAA-VAR-RT-INT OF    
043224         TDB-TDAACCT.
043226     MOVE TDAA-VAR-RT-SCHED OF TDAACCT TO TDB-TDAA-VAR-RT-SCHED   
043228         OF TDB-TDAACCT.
043230     MOVE TDAA-VAR-RT-CUST OF TDAACCT TO TDB-TDAA-VAR-RT-CUST OF  
043232         TDB-TDAACCT.
043234     MOVE TDAA-VAR-RT-BAL OF TDAACCT TO TDB-TDAA-VAR-RT-BAL OF    
043236         TDB-TDAACCT.
043238     MOVE TDAA-RT-INDX-CD OF TDAACCT TO TDB-TDAA-RT-INDX-CD OF    
043240         TDB-TDAACCT.
043242     MOVE TDAA-R-RT-INDX-CD OF TDAACCT TO TDB-TDAA-R-RT-INDX-CD   
043244         OF TDB-TDAACCT.
043246     MOVE TDAA-RT-MARG-CD OF TDAACCT TO TDB-TDAA-RT-MARG-CD OF    
043248         TDB-TDAACCT.
043250     MOVE TDAA-R-RT-MARG-CD OF TDAACCT TO TDB-TDAA-R-RT-MARG-CD   
043252         OF TDB-TDAACCT.
043254     MOVE TDAA-RT-TIER-CD OF TDAACCT TO TDB-TDAA-RT-TIER-CD OF    
043256         TDB-TDAACCT.
043258     MOVE TDAA-R-RT-TIER-CD OF TDAACCT TO TDB-TDAA-R-RT-TIER-CD   
043260         OF TDB-TDAACCT.
043262     MOVE TDAA-RT-SR-CD OF TDAACCT TO TDB-TDAA-RT-SR-CD OF        
043264         TDB-TDAACCT.
043266     MOVE TDAA-R-RT-SR-CD OF TDAACCT TO TDB-TDAA-R-RT-SR-CD OF    
043268         TDB-TDAACCT.
043270     MOVE TDAA-RT-REGN-CD OF TDAACCT TO TDB-TDAA-RT-REGN-CD OF    
043272         TDB-TDAACCT.
043274     MOVE TDAA-RT-CHG-NTRVL OF TDAACCT TO TDB-TDAA-RT-CHG-NTRVL   
043276         OF TDB-TDAACCT.
043278     MOVE TDAA-CAP-RT-CHG OF TDAACCT TO TDB-TDAA-CAP-RT-CHG OF    
043280         TDB-TDAACCT.
043282     MOVE TDAA-R-TIER-RT-CH OF TDAACCT TO TDB-TDAA-R-TIER-RT-CH   
043284         OF TDB-TDAACCT.
043286     MOVE TDAA-ALERT-CD OF TDAACCT TO TDB-TDAA-ALERT-CD OF        
043288         TDB-TDAACCT.
043290     MOVE TDAA-ALERT-CD-2 OF TDAACCT TO TDB-TDAA-ALERT-CD-2 OF    
043292         TDB-TDAACCT.
043294     MOVE TDAA-ALERT-CD-3 OF TDAACCT TO TDB-TDAA-ALERT-CD-3 OF    
043296         TDB-TDAACCT.
043298     MOVE TDAA-CENSUS-TRACT OF TDAACCT TO TDB-TDAA-CENSUS-TRACT   
043300         OF TDB-TDAACCT.
043302     MOVE TDAA-MK-SEGMENT OF TDAACCT TO TDB-TDAA-MK-SEGMENT OF    
043304         TDB-TDAACCT.
043306     MOVE TDAA-BK-DEF-TOT OF TDAACCT TO TDB-TDAA-BK-DEF-TOT OF    
043308         TDB-TDAACCT.
043310     MOVE TDAA-BK-DEF-CD1 OF TDAACCT TO TDB-TDAA-BK-DEF-CD1 OF    
043312         TDB-TDAACCT.
043314     MOVE TDAA-BK-DEF-CD2 OF TDAACCT TO TDB-TDAA-BK-DEF-CD2 OF    
043316         TDB-TDAACCT.
043318     MOVE TDAA-BK-DEF-CD3 OF TDAACCT TO TDB-TDAA-BK-DEF-CD3 OF    
043320         TDB-TDAACCT.
043322     MOVE TDAA-BK-DEF-CD4 OF TDAACCT TO TDB-TDAA-BK-DEF-CD4 OF    
043324         TDB-TDAACCT.
043326     MOVE TDAA-BK-DEF-CD5 OF TDAACCT TO TDB-TDAA-BK-DEF-CD5 OF    
043328         TDB-TDAACCT.
043330     MOVE TDAA-OID-METH OF TDAACCT TO TDB-TDAA-OID-METH OF        
043332         TDB-TDAACCT.
043334     MOVE TDAA-EOY-CD OF TDAACCT TO TDB-TDAA-EOY-CD OF            
043336         TDB-TDAACCT.
043338     MOVE TDAA-B-NOTC-YR1 OF TDAACCT TO TDB-TDAA-B-NOTC-YR1 OF    
043340         TDB-TDAACCT.
043342     MOVE TDAA-B-NOTC-YR2 OF TDAACCT TO TDB-TDAA-B-NOTC-YR2 OF    
043344         TDB-TDAACCT.
043346     MOVE TDAA-B-NOTC-YR3 OF TDAACCT TO TDB-TDAA-B-NOTC-YR3 OF    
043348         TDB-TDAACCT.
043350     MOVE TDAA-NO-COMB-IRS OF TDAACCT TO TDB-TDAA-NO-COMB-IRS OF  
043352         TDB-TDAACCT.
043354     MOVE TDAA-PENLTY-CD OF TDAACCT TO TDB-TDAA-PENLTY-CD OF      
043356         TDB-TDAACCT.
043358     MOVE TDAA-MONEY-SRC-CD OF TDAACCT TO TDB-TDAA-MONEY-SRC-CD   
043360         OF TDB-TDAACCT.
043362     MOVE TDAA-INTERNET-BPY OF TDAACCT TO TDB-TDAA-INTERNET-BPY   
043364         OF TDB-TDAACCT.
043366     MOVE TDAA-INTERNET-TFR OF TDAACCT TO TDB-TDAA-INTERNET-TFR   
043368         OF TDB-TDAACCT.
043370     MOVE TDAA-INTERNET-INQ OF TDAACCT TO TDB-TDAA-INTERNET-INQ   
043372         OF TDB-TDAACCT.
043374     MOVE TDAA-IRA-BACKED OF TDAACCT TO TDB-TDAA-IRA-BACKED OF    
043376         TDB-TDAACCT.
043378     MOVE TDAA-SAV-DEPOSIT OF TDAACCT TO TDB-TDAA-SAV-DEPOSIT OF  
043380         TDB-TDAACCT.
043382     MOVE TDAA-MAT-TYPE OF TDAACCT TO TDB-TDAA-MAT-TYPE OF        
043384         TDB-TDAACCT.
043386     MOVE TDAA-MAT-TERM OF TDAACCT TO TDB-TDAA-MAT-TERM OF        
043388         TDB-TDAACCT.
043390     MOVE TDAA-ORG-MAT-TYPE OF TDAACCT TO TDB-TDAA-ORG-MAT-TYPE   
043392         OF TDB-TDAACCT.
043394     MOVE TDAA-ORG-MAT-TERM OF TDAACCT TO TDB-TDAA-ORG-MAT-TERM   
043396         OF TDB-TDAACCT.
043398     MOVE TDAA-ODD-PAYMENT OF TDAACCT TO TDB-TDAA-ODD-PAYMENT OF  
043400         TDB-TDAACCT.
043402     MOVE TDAA-PAY-FREQ OF TDAACCT TO TDB-TDAA-PAY-FREQ OF        
043404         TDB-TDAACCT.
043406     MOVE TDAA-PAY-NTRVL OF TDAACCT TO TDB-TDAA-PAY-NTRVL OF      
043408         TDB-TDAACCT.
043410     MOVE TDAA-FEE-FREQ OF TDAACCT TO TDB-TDAA-FEE-FREQ OF        
043412         TDB-TDAACCT.
043414     MOVE TDAA-FEE-NTRVL OF TDAACCT TO TDB-TDAA-FEE-NTRVL OF      
043416         TDB-TDAACCT.
043418     MOVE TDAA-STMT-FREQ OF TDAACCT TO TDB-TDAA-STMT-FREQ OF      
043420         TDB-TDAACCT.
043422     MOVE TDAA-STMT-NTRVL OF TDAACCT TO TDB-TDAA-STMT-NTRVL OF    
043424         TDB-TDAACCT.
043426     MOVE TDAA-EMPLOYEE-ID OF TDAACCT TO TDB-TDAA-EMPLOYEE-ID OF  
043428         TDB-TDAACCT.
043430     MOVE TDAA-EFT-CARD OF TDAACCT TO TDB-TDAA-EFT-CARD OF        
043432         TDB-TDAACCT.
043434     MOVE TDAA-PEN-WAV-RESN OF TDAACCT TO TDB-TDAA-PEN-WAV-RESN   
043436         OF TDB-TDAACCT.
043438     MOVE TDAA-CLOSED-RESN OF TDAACCT TO TDB-TDAA-CLOSED-RESN OF  
043440         TDB-TDAACCT.
043442     MOVE TDAA-SPECIAL-STMT OF TDAACCT TO TDB-TDAA-SPECIAL-STMT   
043444         OF TDB-TDAACCT.
043446     MOVE TDAA-CLS-THIS-MTH OF TDAACCT TO TDB-TDAA-CLS-THIS-MTH   
043448         OF TDB-TDAACCT.
043450     MOVE TDAA-RC-MAT-ONLY OF TDAACCT TO TDB-TDAA-RC-MAT-ONLY OF  
043452         TDB-TDAACCT.
043454     MOVE TDAA-GRACE-DAYS OF TDAACCT TO TDB-TDAA-GRACE-DAYS OF    
043456         TDB-TDAACCT.
043458     MOVE TDAA-CLS-ON-MAT OF TDAACCT TO TDB-TDAA-CLS-ON-MAT OF    
```

⚠️  This is the source code you must document.
    480 lines from 21246 to 21725.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

