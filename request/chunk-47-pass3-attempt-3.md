# LLM Request Debug File
Generated: 2025-11-17T22:31:45.374055

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 47/55
- **Model**: gpt-4.1
- **Chunk Number**: 47
- **Pass Number**: 3
- **Attempt Number**: 3 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~7,434 tokens
- **Total Input**: ~9,392 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 47/55" (ID: detailed-code-explanation)

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
⚠️  CRITICAL INSTRUCTIONS - READ CAREFULLY
═══════════════════════════════════════════════════════════════════════════

You will receive COBOL-74 source code from lines {{start_line}} to {{end_line}}.

🚨 YOUR MANDATORY TASK:
1. Return EVERY EXECUTABLE LINE in ```cobol code blocks with sequence numbers
2. Provide detailed explanations for each code section
3. Include self-assessment at the end

═══════════════════════════════════════════════════════════════════════════
📋 CODE INCLUSION RULES - ABSOLUTE REQUIREMENTS
═══════════════════════════════════════════════════════════════════════════

✅ ALWAYS INCLUDE (No Exceptions for Brevity or Repetition):
  • IDENTIFICATION DIVISION - ALL lines (PROGRAM-ID, AUTHOR, DATE-WRITTEN)
  • ENVIRONMENT DIVISION - ALL lines (FILE-CONTROL, SELECT statements)
  • DATA DIVISION - EVERY SINGLE LINE:
    → Every FD entry with complete record layouts
    → Every 01-level variable in WORKING-STORAGE
    → Every subordinate level (05, 10, 15, 77, 88)
    → Every FILLER definition (even if 1000+ repetitive ones)
    → Every PIC, VALUE, OCCURS, REDEFINES clause
    → Every data table entry (NO summarization allowed)
  • PROCEDURE DIVISION - EVERY SINGLE LINE:
    → Every paragraph/section definition
    → Every MOVE, PERFORM, IF, COMPUTE statement
    → Every period, condition, branch

═══════════════════════════════════════════════════════════════════════════
🚫 FORBIDDEN BEHAVIORS - WILL CAUSE VALIDATION FAILURE
═══════════════════════════════════════════════════════════════════════════

❌ NEVER use "Omitted for brevity"
   Bad:  "05 FILLER PIC X(10). ... (50 similar entries omitted)"
   Good: Show ALL 50 FILLER entries verbatim

❌ NEVER use "Similar pattern continues" or "Pattern repeats"
   Bad:  "05 FIELD-1 PIC 9(5). ... (pattern repeats 100 times)"
   Good: Show ALL 100 field definitions verbatim

❌ NEVER summarize repetitive code
   Bad:  "Multiple FILLER definitions follow..."
   Good: Include EVERY FILLER line with its sequence number

❌ NEVER skip sections you consider "boring" or "redundant"
   Bad:  Skipping 200 lines of data table entries
   Good: Include ALL 200 lines verbatim

❌ NEVER use ellipsis (...) to indicate omitted code
   Bad:  "05 FIELD-1 ... 05 FIELD-100"
   Good: Show FIELD-1, FIELD-2, ..., FIELD-100 (all 100 lines)

❌ NEVER skip lines because they look repetitive
   Bad:  "05 FILLER PIC X. (repeated 500 times)"
   Good: Show all 500 lines individually

═══════════════════════════════════════════════════════════════════════════
✅ VALIDATION CRITERIA - Your Output Will Be Automatically Checked
═══════════════════════════════════════════════════════════════════════════

Your code blocks will be validated against these requirements:

1. COMPLETE LINE COVERAGE:
   → Every executable line from {{start_line}} to {{end_line}} must appear in ```cobol blocks
   → Automated extraction of sequence numbers from your output
   → Missing even ONE executable line = VALIDATION FAILURE & RETRY

2. SEQUENCE NUMBER PRESERVATION:
   → Every line must include its 6-digit sequence number
   → Example: 003240 MOVE X TO Y.
   → This proves you didn't skip or summarize

3. NO SUMMARIZATION KEYWORDS:
   → Automated scan for: "omitted", "similar", "continues", "...", "repeats"
   → If found in code sections = VALIDATION FAILURE

4. COMPLETENESS VERIFICATION:
   → Expected executable lines: {{line_count}} minus comment lines
   → Your code blocks must contain this exact number
   → Coverage must be ≥95% of executable lines

═══════════════════════════════════════════════════════════════════════════
📝 REQUIRED OUTPUT FORMAT
═══════════════════════════════════════════════════════════════════════════

For each logical code block (paragraph, section, data group):

### Block N: [BLOCK-NAME] (Lines X-Y)

```cobol
[SEQUENCE#] [COMPLETE CODE LINE 1]
[SEQUENCE#] [COMPLETE CODE LINE 2]
... (show EVERY line - no skipping!)
[SEQUENCE#] [COMPLETE CODE LINE N]
```

**Purpose:**
[High-level summary of what this block does]

**Detailed Explanation:**
[Comprehensive explanation covering:]
- What the code does (functional purpose)
- Why it's structured this way (design rationale)
- How control flows through it (execution path)
- Important variables and their roles
- Conditional logic and branches
- Data transformations
- External interactions (CALL, PERFORM)
- Error handling (if any)

**Technical Details:**
- Variables used: [list]
- Called by: [caller info]
- Calls: [callee info]
- Side effects: [file I/O, state changes]

═══════════════════════════════════════════════════════════════════════════
📊 MANDATORY SELF-ASSESSMENT (Include at End of Response)
═══════════════════════════════════════════════════════════════════════════

After generating all code blocks, provide this self-assessment:

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
- Source chunk contained: {{line_count}} total lines (lines {{start_line}}-{{end_line}})
- I included: [NUMBER] executable lines in my code blocks
- I excluded: [NUMBER] comment/page-break lines
- Expected executable: {{line_count}} - [excluded count]
- My self-assessed coverage: [NUMBER]%

⚠️ NOTE: This self-assessment will be verified programmatically.

---

═══════════════════════════════════════════════════════════════════════════
📌 CRITICAL REMINDERS
═══════════════════════════════════════════════════════════════════════════

1. ⚠️ NEVER abbreviate repetitive code for "readability"
2. ⚠️ NEVER assume pattern from first few lines
3. ⚠️ NEVER skip lines because they seem redundant
4. ⚠️ ALWAYS show complete data tables (even if 500+ lines)
5. ⚠️ ALWAYS include sequence numbers to prove coverage
6. ⚠️ VALIDATION WILL VERIFY: (Your lines / Expected lines) ≥ 95%

═══════════════════════════════════════════════════════════════════════════
🎯 Success Metric: Lines in your code blocks / Expected executable lines ≥ 95%
═══════════════════════════════════════════════════════════════════════════


**CHUNK 47 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-17T19:50:50.832678", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 47 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 22546 to 22983 (438 lines)\nChunk Tokens (estimated): ~7,996\nActual Input Tokens: 9,402 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 22546-22983 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 47 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 47 of 55.\n\n\n=============================================================================\nCHUNK 47 SOURCE CODE (Lines 22546-22983)\n=============================================================================\n\n```cobol\n045100         HOLD-TDAACCT.\n045102     MOVE TDAA-BAL-BEG-LYR OF TDAACCT TO HOLD-TDAA-BAL-BEG-LYR OF \n045104         HOLD-TDAACCT.\n045106     MOVE TDAA-MIN-BAL-STD OF TDAACCT TO HOLD-TDAA-MIN-BAL-STD OF \n045108         HOLD-TDAACCT.\n045110     MOVE TDAA-MIN-BAL-YTD OF TDAACCT TO HOLD-TDAA-MIN-BAL-YTD OF \n045112         HOLD-TDAACCT.\n045114     MOVE TDAA-MAX-BAL-YTD OF TDAACCT TO HOLD-TDAA-MAX-BAL-YTD OF \n045116         HOLD-TDAACCT.\n045118     MOVE TDAA-LMINBAL-STD OF TDAACCT TO HOLD-TDAA-LMINBAL-STD OF \n045120         HOLD-TDAACCT.\n045122     MOVE TDAA-CMPD-INT OF TDAACCT TO HOLD-TDAA-CMPD-INT OF       \n045124         HOLD-TDAACCT.\n045126     MOVE TDAA-PER-DIEM OF TDAACCT TO HOLD-TDAA-PER-DIEM OF       \n045128         HOLD-TDAACCT.\n045130     MOVE TDAA-AVG-PER-DIEM OF TDAACCT TO HOLD-TDAA-AVG-PER-DIEM  \n045132         OF HOLD-TDAACCT.\n045134     MOVE TDAA-EMAIL-MAXAMT OF TDAACCT TO HOLD-TDAA-EMAIL-MAXAMT  \n045136         OF HOLD-TDAACCT.\n045138     MOVE TDAA-EMAIL-MINAMT OF TDAACCT TO HOLD-TDAA-EMAIL-MINAMT  \n045140         OF HOLD-TDAACCT.\n045142     MOVE TDAA-DTH-FAIRMKT OF TDAACCT TO HOLD-TDAA-DTH-FAIRMKT OF \n045144         HOLD-TDAACCT.\n045146     MOVE TDAA-PENLTY-WAIVE OF TDAACCT TO HOLD-TDAA-PENLTY-WAIVE  \n045148         OF HOLD-TDAACCT.\n045150     MOVE TDAA-BEG-INT-RT OF TDAACCT TO HOLD-TDAA-BEG-INT-RT OF   \n045152         HOLD-TDAACCT.\n045154     MOVE TDAA-CUR-INT-RT OF TDAACCT TO HOLD-TDAA-CUR-INT-RT OF   \n045156         HOLD-TDAACCT.\n045158     MOVE TDAA-FLOOR-RT OF TDAACCT TO HOLD-TDAA-FLOOR-RT OF       \n045160         HOLD-TDAACCT.\n045162     MOVE TDAA-FLOOR-INCR OF TDAACCT TO HOLD-TDAA-FLOOR-INCR OF   \n045164         HOLD-TDAACCT.\n045166     MOVE TDAA-YIELD-RT OF TDAACCT TO HOLD-TDAA-YIELD-RT OF       \n045168         HOLD-TDAACCT.\n045170     MOVE 1 TO Z-II.\n045172 Z-13-1-1-LOOP.\n045174     IF Z-II > 10\n045176         GO TO Z-13-1-1-LOOP-XIT.\n045178     MOVE TDAA-RISE-RATE OF TDAACCT (Z-II) TO HOLD-TDAA-RISE-RATE \n045180         OF HOLD-TDAACCT (Z-II).\n045182     ADD 1 TO Z-II.\n045184     GO TO Z-13-1-1-LOOP.\n045186 Z-13-1-1-LOOP-XIT.\n045188     MOVE TDAA-LNS-INCRMNT OF TDAACCT TO HOLD-TDAA-LNS-INCRMNT OF \n045190         HOLD-TDAACCT.\n045192     MOVE TDAA-RT-VARIANCE OF TDAACCT TO HOLD-TDAA-RT-VARIANCE OF \n045194         HOLD-TDAACCT.\n045196     MOVE TDAA-CONST-RT-ADJ OF TDAACCT TO HOLD-TDAA-CONST-RT-ADJ  \n045198         OF HOLD-TDAACCT.\n045200     MOVE TDAA-RATE-AT-EOY OF TDAACCT TO HOLD-TDAA-RATE-AT-EOY OF \n045202         HOLD-TDAACCT.\n045204     MOVE TDAA-RATE-LST-STM OF TDAACCT TO HOLD-TDAA-RATE-LST-STM  \n045206         OF HOLD-TDAACCT.\n045208     MOVE TDAA-ORG-YIELD-RT OF TDAACCT TO HOLD-TDAA-ORG-YIELD-RT  \n045210         OF HOLD-TDAACCT.\n045212     MOVE TDAA-REN-YIELD-RT OF TDAACCT TO HOLD-TDAA-REN-YIELD-RT  \n045214         OF HOLD-TDAACCT.\n045216     MOVE TDAA-SCHED-DT OF TDAACCT TO HOLD-TDAA-SCHED-DT OF       \n045218         HOLD-TDAACCT.\n045220     MOVE TDAA-ACCR-DT OF TDAACCT TO HOLD-TDAA-ACCR-DT OF         \n045222         HOLD-TDAACCT.\n045224     MOVE TDAA-OPEN-DT OF TDAACCT TO HOLD-TDAA-OPEN-DT OF         \n045226         HOLD-TDAACCT.\n045228     MOVE TDAA-CLSD-DT OF TDAACCT TO HOLD-TDAA-CLSD-DT OF         \n045230         HOLD-TDAACCT.\n045232     MOVE TDAA-LST-MAT-DT OF TDAACCT TO HOLD-TDAA-LST-MAT-DT OF   \n045234         HOLD-TDAACCT.\n045236     MOVE TDAA-LST-POST-DT OF TDAACCT TO HOLD-TDAA-LST-POST-DT OF \n045238         HOLD-TDAACCT.\n045240     MOVE TDAA-LST-IN-PROC OF TDAACCT TO HOLD-TDAA-LST-IN-PROC OF \n045242         HOLD-TDAACCT.\n045244     MOVE TDAA-LST-CONTACT OF TDAACCT TO HOLD-TDAA-LST-CONTACT OF \n045246         HOLD-TDAACCT.\n045248     MOVE TDAA-LST-FEE-DT OF TDAACCT TO HOLD-TDAA-LST-FEE-DT OF   \n045250         HOLD-TDAACCT.\n045252     MOVE TDAA-LST-RTCHG-DT OF TDAACCT TO HOLD-TDAA-LST-RTCHG-DT  \n045254         OF HOLD-TDAACCT.\n045256     MOVE TDAA-LST-DIST-DT OF TDAACCT TO HOLD-TDAA-LST-DIST-DT OF \n045258         HOLD-TDAACCT.\n045260     MOVE TDAA-LST-STMT-DT OF TDAACCT TO HOLD-TDAA-LST-STMT-DT OF \n045262         HOLD-TDAACCT.\n045264     MOVE TDAA-LST-CMPD-DT OF TDAACCT TO HOLD-TDAA-LST-CMPD-DT OF \n045266         HOLD-TDAACCT.\n045268     MOVE 1 TO Z-II.\n045270 Z-13-1-2-LOOP.\n045272     IF Z-II > 10\n045274         GO TO Z-13-1-2-LOOP-XIT.\n045276     MOVE TDAA-RR-CYC-DT OF TDAACCT (Z-II) TO HOLD-TDAA-RR-CYC-DT \n045278         OF HOLD-TDAACCT (Z-II).\n045280     ADD 1 TO Z-II.\n045282     GO TO Z-13-1-2-LOOP.\n045284 Z-13-1-2-LOOP-XIT.\n045286     MOVE TDAA-BNF-BIRTH-DT OF TDAACCT TO HOLD-TDAA-BNF-BIRTH-DT  \n045288         OF HOLD-TDAACCT.\n045290     MOVE TDAA-BNF-DEATH-DT OF TDAACCT TO HOLD-TDAA-BNF-DEATH-DT  \n045292         OF HOLD-TDAACCT.\n045294     MOVE TDAA-LUPD-DATE OF TDAACCT TO HOLD-TDAA-LUPD-DATE OF     \n045296         HOLD-TDAACCT.\n045298     MOVE TDAA-LUPD-TIME OF TDAACCT TO HOLD-TDAA-LUPD-TIME OF     \n045300         HOLD-TDAACCT.\n045302     MOVE TDAA-ADD-DT OF TDAACCT TO HOLD-TDAA-ADD-DT OF           \n045304         HOLD-TDAACCT.\n045306     MOVE TDAA-ADD-TM OF TDAACCT TO HOLD-TDAA-ADD-TM OF           \n045308         HOLD-TDAACCT.\n045310     MOVE TDAA-CONV-DT OF TDAACCT TO HOLD-TDAA-CONV-DT OF         \n045312         HOLD-TDAACCT.\n045314     MOVE TDAA-ACT-CLOSE-DT OF TDAACCT TO HOLD-TDAA-ACT-CLOSE-DT  \n045316         OF HOLD-TDAACCT.\n045318     MOVE TDAA-LST-TBACT-DT OF TDAACCT TO HOLD-TDAA-LST-TBACT-DT  \n045320         OF HOLD-TDAACCT.\n045322     MOVE TDAA-ALERT-EXP-DT OF TDAACCT TO HOLD-TDAA-ALERT-EXP-DT  \n045324         OF HOLD-TDAACCT.\n045326     MOVE TDAA-ALRT2-EXP-DT OF TDAACCT TO HOLD-TDAA-ALRT2-EXP-DT  \n045328         OF HOLD-TDAACCT.\n045330     MOVE TDAA-ALRT3-EXP-DT OF TDAACCT TO HOLD-TDAA-ALRT3-EXP-DT  \n045332         OF HOLD-TDAACCT.\n045334     MOVE TDAA-NXT-FEE-DT OF TDAACCT TO HOLD-TDAA-NXT-FEE-DT OF   \n045336         HOLD-TDAACCT.\n045338     MOVE TDAA-NXT-POST-DT OF TDAACCT TO HOLD-TDAA-NXT-POST-DT OF \n045340         HOLD-TDAACCT.\n045342     MOVE TDAA-NXT-MAT-DT OF TDAACCT TO HOLD-TDAA-NXT-MAT-DT OF   \n045344         HOLD-TDAACCT.\n045346     MOVE TDAA-NXT-DIST-DT OF TDAACCT TO HOLD-TDAA-NXT-DIST-DT OF \n045348         HOLD-TDAACCT.\n045350     MOVE TDAA-NXT-RT-CHG OF TDAACCT TO HOLD-TDAA-NXT-RT-CHG OF   \n045352         HOLD-TDAACCT.\n045354     MOVE TDAA-NXT-IN-PROC OF TDAACCT TO HOLD-TDAA-NXT-IN-PROC OF \n045356         HOLD-TDAACCT.\n045358     MOVE TDAA-NXT-CMPD-DT OF TDAACCT TO HOLD-TDAA-NXT-CMPD-DT OF \n045360         HOLD-TDAACCT.\n045362     MOVE TDAA-NXT-STMT-DT OF TDAACCT TO HOLD-TDAA-NXT-STMT-DT OF \n045364         HOLD-TDAACCT.\n045366     MOVE TDAA-NXT-DS-PROC OF TDAACCT TO HOLD-TDAA-NXT-DS-PROC OF \n045368         HOLD-TDAACCT.\n045370     MOVE TDAA-ADV-NTC-DT OF TDAACCT TO HOLD-TDAA-ADV-NTC-DT OF   \n045372         HOLD-TDAACCT.\n045374     MOVE TDAA-NXT-29YR-DT OF TDAACCT TO HOLD-TDAA-NXT-29YR-DT OF \n045376         HOLD-TDAACCT.\n045378     MOVE TDAA-FAIR-MRKT-DT OF TDAACCT TO HOLD-TDAA-FAIR-MRKT-DT  \n045380         OF HOLD-TDAACCT.\n045382     MOVE TDAA-SORT-FIELD-1 OF TDAACCT TO HOLD-TDAA-SORT-FIELD-1  \n045384         OF HOLD-TDAACCT.\n045386     MOVE TDAA-SORT-FIELD-2 OF TDAACCT TO HOLD-TDAA-SORT-FIELD-2  \n045388         OF HOLD-TDAACCT.\n045390     MOVE TDAA-SORT-FIELD-3 OF TDAACCT TO HOLD-TDAA-SORT-FIELD-3  \n045392         OF HOLD-TDAACCT.\n045394     MOVE TDAA-SORT-FIELD-4 OF TDAACCT TO HOLD-TDAA-SORT-FIELD-4  \n045396         OF HOLD-TDAACCT.\n045398     MOVE TDAA-CMAT-PUB-ID OF TDAACCT TO HOLD-TDAA-CMAT-PUB-ID OF \n045400         HOLD-TDAACCT.\n045402     MOVE TDAA-MSA-CONTR OF TDAACCT TO HOLD-TDAA-MSA-CONTR OF     \n045404         HOLD-TDAACCT.\n045406     MOVE TDAA-MSA-CONTR-LY OF TDAACCT TO HOLD-TDAA-MSA-CONTR-LY  \n045408         OF HOLD-TDAACCT.\n045410     MOVE TDAA-AVG-ACCR-INT OF TDAACCT TO HOLD-TDAA-AVG-ACCR-INT  \n045412         OF HOLD-TDAACCT.\n045414     MOVE TDAA-LEVEL-PAY OF TDAACCT TO HOLD-TDAA-LEVEL-PAY OF     \n045416         HOLD-TDAACCT.\n045418     MOVE TDAA-ST-INT-CD OF TDAACCT TO HOLD-TDAA-ST-INT-CD OF     \n045420         HOLD-TDAACCT.\n045422     MOVE TDAA-ST-WHLD-CD OF TDAACCT TO HOLD-TDAA-ST-WHLD-CD OF   \n045424         HOLD-TDAACCT.\n045426     MOVE TDAA-ST-WHLD-AMT OF TDAACCT TO HOLD-TDAA-ST-WHLD-AMT OF \n045428         HOLD-TDAACCT.\n045430     MOVE TDAA-ST-CUR-W-AMT OF TDAACCT TO HOLD-TDAA-ST-CUR-W-AMT  \n045432         OF HOLD-TDAACCT.\n045434     MOVE TDAA-ST-LST-W-AMT OF TDAACCT TO HOLD-TDAA-ST-LST-W-AMT  \n045436         OF HOLD-TDAACCT.\n045438     MOVE TDAA-ST-WHLD-STD OF TDAACCT TO HOLD-TDAA-ST-WHLD-STD OF \n045440         HOLD-TDAACCT.\n045442     MOVE TDAA-ST-WHLD-YTD OF TDAACCT TO HOLD-TDAA-ST-WHLD-YTD OF \n045444         HOLD-TDAACCT.\n045446     MOVE TDAA-CIF-REMARK OF TDAACCT TO HOLD-TDAA-CIF-REMARK OF   \n045448         HOLD-TDAACCT.\n045450     MOVE TDAA-CSR OF TDAACCT TO HOLD-TDAA-CSR OF HOLD-TDAACCT.\n045452     MOVE TDAA-BSA-O-RSK-CD OF TDAACCT TO HOLD-TDAA-BSA-O-RSK-CD  \n045454         OF HOLD-TDAACCT.\n045456     MOVE TDAA-BSA-C-RSK-CD OF TDAACCT TO HOLD-TDAA-BSA-C-RSK-CD  \n045458         OF HOLD-TDAACCT.\n045460     MOVE TDAA-LRG-TRX-DT OF TDAACCT TO HOLD-TDAA-LRG-TRX-DT OF   \n045462         HOLD-TDAACCT.\n045464     MOVE TDAA-HSA-FMLY-IND OF TDAACCT TO HOLD-TDAA-HSA-FMLY-IND  \n045466         OF HOLD-TDAACCT.\n045468     MOVE TDAA-STOP-PAY-IND OF TDAACCT TO HOLD-TDAA-STOP-PAY-IND  \n045470         OF HOLD-TDAACCT.\n045472     MOVE TDAA-IMG-PG-TYPE OF TDAACCT TO HOLD-TDAA-IMG-PG-TYPE OF \n045474         HOLD-TDAACCT.\n045476     MOVE TDAA-CONT-LMT-CLC OF TDAACCT TO HOLD-TDAA-CONT-LMT-CLC  \n045478         OF HOLD-TDAACCT.\n045480     MOVE TDAA-CONT-LMT-ENT OF TDAACCT TO HOLD-TDAA-CONT-LMT-ENT  \n045482         OF HOLD-TDAACCT.\n045484     MOVE TDAA-MEMO-DB OF TDAACCT TO HOLD-TDAA-MEMO-DB OF         \n045486         HOLD-TDAACCT.\n045488     MOVE TDAA-MEMO-CR OF TDAACCT TO HOLD-TDAA-MEMO-CR OF         \n045490         HOLD-TDAACCT.\n045492     MOVE TDAA-MEMO-DB-2 OF TDAACCT TO HOLD-TDAA-MEMO-DB-2 OF     \n045494         HOLD-TDAACCT.\n045496     MOVE TDAA-MEMO-CR-2 OF TDAACCT TO HOLD-TDAA-MEMO-CR-2 OF     \n045498         HOLD-TDAACCT.\n045500     MOVE TDAA-RT-AT-CONV OF TDAACCT TO HOLD-TDAA-RT-AT-CONV OF   \n045502         HOLD-TDAACCT.\n045504     MOVE TDAA-ACCR-AT-CONV OF TDAACCT TO HOLD-TDAA-ACCR-AT-CONV  \n045506         OF HOLD-TDAACCT.\n045508     MOVE TDAA-RT-AT-ACRDT OF TDAACCT TO HOLD-TDAA-RT-AT-ACRDT OF \n045510         HOLD-TDAACCT.\n045512     MOVE TDAA-BAL-AT-ACRDT OF TDAACCT TO HOLD-TDAA-BAL-AT-ACRDT  \n045514         OF HOLD-TDAACCT.\n045516     MOVE TDAA-ZERO-RT-ALLOW OF TDAACCT TO                        \n045518         HOLD-TDAA-ZERO-RT-ALLOW OF HOLD-TDAACCT.\n045520     MOVE TDAA-EMAIL-NTC OF TDAACCT TO HOLD-TDAA-EMAIL-NTC OF     \n045522         HOLD-TDAACCT.\n045524     MOVE TDAA-EMAIL-STMT OF TDAACCT TO HOLD-TDAA-EMAIL-STMT OF   \n045526         HOLD-TDAACCT.\n045528     MOVE TDAA-FRAUD-CK-DT OF TDAACCT TO HOLD-TDAA-FRAUD-CK-DT OF \n045530         HOLD-TDAACCT.\n045532     MOVE TDAA-FRAUD-CK-CNT OF TDAACCT TO HOLD-TDAA-FRAUD-CK-CNT  \n045534         OF HOLD-TDAACCT.\n045536     MOVE TDAA-FRAUD-CK-AMT OF TDAACCT TO HOLD-TDAA-FRAUD-CK-AMT  \n045538         OF HOLD-TDAACCT.\n045540     MOVE TDAA-MISC-ACCTNO OF TDAACCT TO HOLD-TDAA-MISC-ACCTNO OF \n045542         HOLD-TDAACCT.\n045544     MOVE TDAA-RMD-MAN-CALC OF TDAACCT TO HOLD-TDAA-RMD-MAN-CALC  \n045546         OF HOLD-TDAACCT.\n045548     MOVE TDAA-RMD-AMOUNT OF TDAACCT TO HOLD-TDAA-RMD-AMOUNT OF   \n045550         HOLD-TDAACCT.\n045552     MOVE TDAA-BROKERAGE-ID OF TDAACCT TO HOLD-TDAA-BROKERAGE-ID  \n045554         OF HOLD-TDAACCT.\n045556     MOVE TDAA-MONY-SRC-CD2 OF TDAACCT TO HOLD-TDAA-MONY-SRC-CD2  \n045558         OF HOLD-TDAACCT.\n045560     MOVE TDAA-INHERIT-IRA OF TDAACCT TO HOLD-TDAA-INHERIT-IRA OF \n045562         HOLD-TDAACCT.\n045564     MOVE TDAA-LIFE-FACTOR OF TDAACCT TO HOLD-TDAA-LIFE-FACTOR OF \n045566         HOLD-TDAACCT.\n045568     MOVE TDAA-EV-LARGE-TRX OF TDAACCT TO HOLD-TDAA-EV-LARGE-TRX  \n045570         OF HOLD-TDAACCT.\n045572     MOVE TDAA-EV-MAT-AMT OF TDAACCT TO HOLD-TDAA-EV-MAT-AMT OF   \n045574         HOLD-TDAACCT.\n045576     MOVE TDAA-EV-DISP-ACCT OF TDAACCT TO HOLD-TDAA-EV-DISP-ACCT  \n045578         OF HOLD-TDAACCT.\n045580     MOVE TDAA-EV-COMP-ACCT OF TDAACCT TO HOLD-TDAA-EV-COMP-ACCT  \n045582         OF HOLD-TDAACCT.\n045584     MOVE TDAA-EV-PUBLIC-ID OF TDAACCT TO HOLD-TDAA-EV-PUBLIC-ID  \n045586         OF HOLD-TDAACCT.\n045588     MOVE TDAA-EV-MAT-TYPE OF TDAACCT TO HOLD-TDAA-EV-MAT-TYPE OF \n045590         HOLD-TDAACCT.\n045592     MOVE TDAA-EV-INT-TYPE OF TDAACCT TO HOLD-TDAA-EV-INT-TYPE OF \n045594         HOLD-TDAACCT.\n045596     MOVE TDAA-EV-ACCT-TYP OF TDAACCT TO HOLD-TDAA-EV-ACCT-TYP OF \n045598         HOLD-TDAACCT.\n045600     MOVE TDAA-EV-WHLD-PCT OF TDAACCT TO HOLD-TDAA-EV-WHLD-PCT OF \n045602         HOLD-TDAACCT.\n045604     MOVE TDAA-EV-NON-ACCR OF TDAACCT TO HOLD-TDAA-EV-NON-ACCR OF \n045606         HOLD-TDAACCT.\n045608     MOVE TDAA-EV-CLOSED OF TDAACCT TO HOLD-TDAA-EV-CLOSED OF     \n045610         HOLD-TDAACCT.\n045612     MOVE TDAA-EV-CLOSE-MO OF TDAACCT TO HOLD-TDAA-EV-CLOSE-MO OF \n045614         HOLD-TDAACCT.\n045616     MOVE TDAA-EV-OPEN-MO OF TDAACCT TO HOLD-TDAA-EV-OPEN-MO OF   \n045618         HOLD-TDAACCT.\n045620     MOVE TDAA-EV-ANN-INT OF TDAACCT TO HOLD-TDAA-EV-ANN-INT OF   \n045622         HOLD-TDAACCT.\n045624     MOVE TDAA-EV-ORIG-RT OF TDAACCT TO HOLD-TDAA-EV-ORIG-RT OF   \n045626         HOLD-TDAACCT.\n045628     MOVE TDAA-EV-DLY-INT OF TDAACCT TO HOLD-TDAA-EV-DLY-INT OF   \n045630         HOLD-TDAACCT.\n045632     MOVE TDAA-EV-INT-PAY OF TDAACCT TO HOLD-TDAA-EV-INT-PAY OF   \n045634         HOLD-TDAACCT.\n045636     MOVE TDAA-EV-AVAIL-BL OF TDAACCT TO HOLD-TDAA-EV-AVAIL-BL OF \n045638         HOLD-TDAACCT.\n045640     MOVE TDAA-EV-RETAIN OF TDAACCT TO HOLD-TDAA-EV-RETAIN OF     \n045642         HOLD-TDAACCT.\n045644     MOVE TDAA-EV-CL-RETAIN OF TDAACCT TO HOLD-TDAA-EV-CL-RETAIN  \n045646         OF HOLD-TDAACCT.\n045648     MOVE TDAA-EV-TIMES-REN OF TDAACCT TO HOLD-TDAA-EV-TIMES-REN  \n045650         OF HOLD-TDAACCT.\n045652     MOVE TDAA-EV-CURR-BAL OF TDAACCT TO HOLD-TDAA-EV-CURR-BAL OF \n045654         HOLD-TDAACCT.\n045656     MOVE TDAA-BRKR-DEP-CAT OF TDAACCT TO HOLD-TDAA-BRKR-DEP-CAT  \n045658         OF HOLD-TDAACCT.\n045660     MOVE TDAA-LINE-OF-BUS OF TDAACCT TO HOLD-TDAA-LINE-OF-BUS OF \n045662         HOLD-TDAACCT.\n045664     MOVE TDAA-1ST-STMT OF TDAACCT TO HOLD-TDAA-1ST-STMT OF       \n045666         HOLD-TDAACCT.\n045668     MOVE TDAA-POSTAL-CITY OF TDAACCT TO HOLD-TDAA-POSTAL-CITY OF \n045670         HOLD-TDAACCT.\n045672     MOVE TDAA-POSTAL-CNTRY OF TDAACCT TO HOLD-TDAA-POSTAL-CNTRY  \n045674         OF HOLD-TDAACCT.\n045676     MOVE TDAA-CITIZN-CNTRY OF TDAACCT TO HOLD-TDAA-CITIZN-CNTRY  \n045678         OF HOLD-TDAACCT.\n045680     MOVE TDAA-CUSTM-FIELDS OF TDAACCT TO HOLD-TDAA-CUSTM-FIELDS  \n045682         OF HOLD-TDAACCT.\n045684     MOVE TDAA-AVG-STEP-RT OF TDAACCT TO HOLD-TDAA-AVG-STEP-RT OF \n045686         HOLD-TDAACCT.\n045688     MOVE TDAA-MONITOR-INQ OF TDAACCT TO HOLD-TDAA-MONITOR-INQ OF \n045690         HOLD-TDAACCT.\n045692     MOVE TDAA-IGL-GRP-2 OF TDAACCT TO HOLD-TDAA-IGL-GRP-2 OF     \n045694         HOLD-TDAACCT.\n045696     MOVE TDAA-AGG-DAYS-QTD OF TDAACCT TO HOLD-TDAA-AGG-DAYS-QTD  \n045698         OF HOLD-TDAACCT.\n045700     MOVE TDAA-AGG-BAL-QTD OF TDAACCT TO HOLD-TDAA-AGG-BAL-QTD OF \n045702         HOLD-TDAACCT.\n045704     MOVE TDAA-IGL-GRP-3 OF TDAACCT TO HOLD-TDAA-IGL-GRP-3 OF     \n045706         HOLD-TDAACCT.\n045708     MOVE TDAA-ALT-ADDR-EOY OF TDAACCT TO HOLD-TDAA-ALT-ADDR-EOY  \n045710         OF HOLD-TDAACCT.\n045712     MOVE TDAA-1042S-TAX-ID OF TDAACCT TO HOLD-TDAA-1042S-TAX-ID  \n045714         OF HOLD-TDAACCT.\n045716     MOVE TDAA-LEC OF TDAACCT TO HOLD-TDAA-LEC OF HOLD-TDAACCT.\n045718     MOVE TDAA-BAL-AT-CLOSE OF TDAACCT TO HOLD-TDAA-BAL-AT-CLOSE  \n045720         OF HOLD-TDAACCT.\n045722     MOVE TDAA-AVL-CAP-INT OF TDAACCT TO HOLD-TDAA-AVL-CAP-INT OF \n045724         HOLD-TDAACCT.\n045726     MOVE TDAA-FIDM-TR-FUND OF TDAACCT TO HOLD-TDAA-FIDM-TR-FUND  \n045728         OF HOLD-TDAACCT.\n045730     MOVE TDAA-IRS-FRM-DLVR OF TDAACCT TO HOLD-TDAA-IRS-FRM-DLVR  \n045732         OF HOLD-TDAACCT.\n045734     MOVE TDAA-PROVINCE OF TDAACCT TO HOLD-TDAA-PROVINCE OF       \n045736         HOLD-TDAACCT.\n045738     MOVE TDAA-PROMOTION OF TDAACCT TO HOLD-TDAA-PROMOTION OF     \n045740         HOLD-TDAACCT.\n045742*THE FOLLOWING MOVES FOR SQL ONLY                                 \n045744     IF Z-EDIT-ERROR\n045746         GO TO Z-13-XIT.\n045748 Z-13-SKIP.\n045750 Z-13-XIT.\n045752     EXIT.\n045754*\n045756*****************************************************************\n045758*    PROCEDURE TDB-CUST-INQ\n045760*****************************************************************\n045762 Z-14-PROCEDURE.\n045764*\n045766     MOVE 0 TO Z-EXIT-CODE.\n045768     MOVE 9999 TO Z-EXIT-LEVEL.\n045770     MOVE \" \" TO WS-ADJUSTED-IND.\n045772     IF TDB-READ-INFO = \"01BAT2\"\n045774         NEXT SENTENCE ELSE\n045776         GO TO Z-14-2-1-ELSE.\n045778     MOVE ZERO TO Z-FLINFO11-PRES.\n045780     MOVE 13 TO Z-FLINFO11-LAST-SEQ.\n045782     MOVE ZERO TO Z-FLINFO11-SOME.\n045784 Z-14-3-READ.\n045786     FIND TDACUST OF LDBTDADB VIA TDACMSET OF TDACUST OF LDBTDADB\n045788     AT TDAC-BANK = TDB-TDAC-BANK AND\n045790        TDAC-CUST = TDB-TDAC-CUST\n045792         ON EXCEPTION\n045794         MOVE 13 TO Z-DMS-EXCEPT-SEQ\n045796         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)\n045798             GO TO Z-14-3-XIT\n045800         ELSE\n045802             MOVE \"TDACMSET OF TDACUST OF LDBTDADB\" TO            \n045804                 Z-DMS-EXCEPT-STR\n045806             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n045808             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n045810\n045812 Z-14-3-PRESENT.\n045814*\n045816     MOVE 1 TO Z-FLINFO11-SOME.\n045818     MOVE 1 TO Z-FLINFO11-PRES.\n045820     GO TO Z-14-3-CONT.\n045822 Z-14-3-XIT.\n045824 Z-14-3-CONT.\n045826     IF Z-FLINFO11-ABSENT\n045828         NEXT SENTENCE ELSE\n045830         GO TO Z-14-4-1-ELSE.\n045832     MOVE 0310 TO TDB-ERROR-NBR.\n045834     GO TO Z-14-4-ENDIF.\n045836 Z-14-4-1-ELSE.\n045838     IF TDB-READ-DATE NOT = 0\n045840         NEXT SENTENCE ELSE\n045842         GO TO Z-14-4-2-ELSE.\n045844************ PERFORM TDB-CUST-01BAT2-ACTV-ADJ\n045846     PERFORM Z-32-PROCEDURE THRU Z-32-XIT.\n045848     IF  Z-EXIT-EDITEXIT\n045850         GO TO Z-14-XIT.\n045852     IF  Z-DMS2-ABORT-FLAG = 1\n045854         GO TO Z-14-XIT.\n045856     IF  Z-EXIT-LEVEL < 0\n045858         GO TO Z-14-END.\n045860*\n045862     MOVE HOLD-TDAC-BANK OF HOLD-TDACUST TO TDB-TDAC-BANK OF      \n045864         TDB-TDACUST.\n045866     MOVE HOLD-TDAC-CUST OF HOLD-TDACUST TO TDB-TDAC-CUST OF      \n045868         TDB-TDACUST.\n045870     MOVE HOLD-TDAC-BRCH OF HOLD-TDACUST TO TDB-TDAC-BRCH OF      \n045872         TDB-TDACUST.\n045874     MOVE HOLD-TDAC-STATUS OF HOLD-TDACUST TO TDB-TDAC-STATUS OF  \n045876         TDB-TDACUST.\n045878     MOVE HOLD-TDAC-NAME-1 OF HOLD-TDACUST TO TDB-TDAC-NAME-1 OF  \n045880         TDB-TDACUST.\n045882     MOVE HOLD-TDAC-N1-KEY OF HOLD-TDACUST TO TDB-TDAC-N1-KEY OF  \n045884         TDB-TDACUST.\n045886     MOVE HOLD-TDAC-N1-FIRST OF HOLD-TDACUST TO TDB-TDAC-N1-FIRST \n045888         OF TDB-TDACUST.\n045890     MOVE HOLD-TDAC-N1-MID OF HOLD-TDACUST TO TDB-TDAC-N1-MID OF  \n045892         TDB-TDACUST.\n045894     MOVE HOLD-TDAC-N1-LAST OF HOLD-TDACUST TO TDB-TDAC-N1-LAST   \n045896         OF TDB-TDACUST.\n045898     MOVE HOLD-TDAC-N1-PREFIX OF HOLD-TDACUST TO                  \n045900         TDB-TDAC-N1-PREFIX OF TDB-TDACUST.\n045902     MOVE HOLD-TDAC-N1-SUFFIX OF HOLD-TDACUST TO                  \n045904         TDB-TDAC-N1-SUFFIX OF TDB-TDACUST.\n045906     MOVE HOLD-TDAC-N1-FAMILIAR OF HOLD-TDACUST TO                \n045908         TDB-TDAC-N1-FAMILIAR OF TDB-TDACUST.\n045910     MOVE HOLD-TDAC-N1-PRT-PFX OF HOLD-TDACUST TO                 \n045912         TDB-TDAC-N1-PRT-PFX OF TDB-TDACUST.\n045914     MOVE HOLD-TDAC-N1-PRT-SFX OF HOLD-TDACUST TO                 \n045916         TDB-TDAC-N1-PRT-SFX OF TDB-TDACUST.\n045918     MOVE HOLD-TDAC-N1-DESIGNAT OF HOLD-TDACUST TO                \n045920         TDB-TDAC-N1-DESIGNAT OF TDB-TDACUST.\n045922     MOVE HOLD-TDAC-NAME-2 OF HOLD-TDACUST TO TDB-TDAC-NAME-2 OF  \n045924         TDB-TDACUST.\n045926     MOVE HOLD-TDAC-N2-MODIFIED OF HOLD-TDACUST TO                \n045928         TDB-TDAC-N2-MODIFIED OF TDB-TDACUST.\n045930     MOVE HOLD-TDAC-N2-PRINT-CD OF HOLD-TDACUST TO                \n045932         TDB-TDAC-N2-PRINT-CD OF TDB-TDACUST.\n045934     MOVE HOLD-TDAC-N2-KEY OF HOLD-TDACUST TO TDB-TDAC-N2-KEY OF  \n045936         TDB-TDACUST.\n045938     MOVE HOLD-TDAC-N2-FIRST OF HOLD-TDACUST TO TDB-TDAC-N2-FIRST \n045940         OF TDB-TDACUST.\n045942     MOVE HOLD-TDAC-N2-MID OF HOLD-TDACUST TO TDB-TDAC-N2-MID OF  \n045944         TDB-TDACUST.\n045946     MOVE HOLD-TDAC-N2-LAST OF HOLD-TDACUST TO TDB-TDAC-N2-LAST   \n045948         OF TDB-TDACUST.\n045950     MOVE HOLD-TDAC-N2-PREFIX OF HOLD-TDACUST TO                  \n045952         TDB-TDAC-N2-PREFIX OF TDB-TDACUST.\n045954     MOVE HOLD-TDAC-N2-SUFFIX OF HOLD-TDACUST TO                  \n045956         TDB-TDAC-N2-SUFFIX OF TDB-TDACUST.\n045958     MOVE HOLD-TDAC-N2-FAMILIAR OF HOLD-TDACUST TO                \n045960         TDB-TDAC-N2-FAMILIAR OF TDB-TDACUST.\n045962     MOVE HOLD-TDAC-N2-PRT-PFX OF HOLD-TDACUST TO                 \n045964         TDB-TDAC-N2-PRT-PFX OF TDB-TDACUST.\n045966     MOVE HOLD-TDAC-N2-PRT-SFX OF HOLD-TDACUST TO                 \n045968         TDB-TDAC-N2-PRT-SFX OF TDB-TDACUST.\n045970     MOVE HOLD-TDAC-N2-DESIGNAT OF HOLD-TDACUST TO                \n045972         TDB-TDAC-N2-DESIGNAT OF TDB-TDACUST.\n045974     MOVE HOLD-TDAC-NAME-3 OF HOLD-TDACUST TO TDB-TDAC-NAME-3 OF  \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    438 lines from 22546 to 22983.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 47, "total_chunks": 55, "start_line": 22546, "end_line": 22983, "line_count": 438}

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
- Source code length: 26604 characters

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
CHUNK 47 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 22546 to 22983 (438 lines)
Chunk Tokens (estimated): ~7,996
Actual Input Tokens: 9,402 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 22546-22983 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 47 of 55 chunks
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
      The source code below is only CHUNK 47 of 55.


=============================================================================
CHUNK 47 SOURCE CODE (Lines 22546-22983)
=============================================================================

```cobol
045100         HOLD-TDAACCT.
045102     MOVE TDAA-BAL-BEG-LYR OF TDAACCT TO HOLD-TDAA-BAL-BEG-LYR OF 
045104         HOLD-TDAACCT.
045106     MOVE TDAA-MIN-BAL-STD OF TDAACCT TO HOLD-TDAA-MIN-BAL-STD OF 
045108         HOLD-TDAACCT.
045110     MOVE TDAA-MIN-BAL-YTD OF TDAACCT TO HOLD-TDAA-MIN-BAL-YTD OF 
045112         HOLD-TDAACCT.
045114     MOVE TDAA-MAX-BAL-YTD OF TDAACCT TO HOLD-TDAA-MAX-BAL-YTD OF 
045116         HOLD-TDAACCT.
045118     MOVE TDAA-LMINBAL-STD OF TDAACCT TO HOLD-TDAA-LMINBAL-STD OF 
045120         HOLD-TDAACCT.
045122     MOVE TDAA-CMPD-INT OF TDAACCT TO HOLD-TDAA-CMPD-INT OF       
045124         HOLD-TDAACCT.
045126     MOVE TDAA-PER-DIEM OF TDAACCT TO HOLD-TDAA-PER-DIEM OF       
045128         HOLD-TDAACCT.
045130     MOVE TDAA-AVG-PER-DIEM OF TDAACCT TO HOLD-TDAA-AVG-PER-DIEM  
045132         OF HOLD-TDAACCT.
045134     MOVE TDAA-EMAIL-MAXAMT OF TDAACCT TO HOLD-TDAA-EMAIL-MAXAMT  
045136         OF HOLD-TDAACCT.
045138     MOVE TDAA-EMAIL-MINAMT OF TDAACCT TO HOLD-TDAA-EMAIL-MINAMT  
045140         OF HOLD-TDAACCT.
045142     MOVE TDAA-DTH-FAIRMKT OF TDAACCT TO HOLD-TDAA-DTH-FAIRMKT OF 
045144         HOLD-TDAACCT.
045146     MOVE TDAA-PENLTY-WAIVE OF TDAACCT TO HOLD-TDAA-PENLTY-WAIVE  
045148         OF HOLD-TDAACCT.
045150     MOVE TDAA-BEG-INT-RT OF TDAACCT TO HOLD-TDAA-BEG-INT-RT OF   
045152         HOLD-TDAACCT.
045154     MOVE TDAA-CUR-INT-RT OF TDAACCT TO HOLD-TDAA-CUR-INT-RT OF   
045156         HOLD-TDAACCT.
045158     MOVE TDAA-FLOOR-RT OF TDAACCT TO HOLD-TDAA-FLOOR-RT OF       
045160         HOLD-TDAACCT.
045162     MOVE TDAA-FLOOR-INCR OF TDAACCT TO HOLD-TDAA-FLOOR-INCR OF   
045164         HOLD-TDAACCT.
045166     MOVE TDAA-YIELD-RT OF TDAACCT TO HOLD-TDAA-YIELD-RT OF       
045168         HOLD-TDAACCT.
045170     MOVE 1 TO Z-II.
045172 Z-13-1-1-LOOP.
045174     IF Z-II > 10
045176         GO TO Z-13-1-1-LOOP-XIT.
045178     MOVE TDAA-RISE-RATE OF TDAACCT (Z-II) TO HOLD-TDAA-RISE-RATE 
045180         OF HOLD-TDAACCT (Z-II).
045182     ADD 1 TO Z-II.
045184     GO TO Z-13-1-1-LOOP.
045186 Z-13-1-1-LOOP-XIT.
045188     MOVE TDAA-LNS-INCRMNT OF TDAACCT TO HOLD-TDAA-LNS-INCRMNT OF 
045190         HOLD-TDAACCT.
045192     MOVE TDAA-RT-VARIANCE OF TDAACCT TO HOLD-TDAA-RT-VARIANCE OF 
045194         HOLD-TDAACCT.
045196     MOVE TDAA-CONST-RT-ADJ OF TDAACCT TO HOLD-TDAA-CONST-RT-ADJ  
045198         OF HOLD-TDAACCT.
045200     MOVE TDAA-RATE-AT-EOY OF TDAACCT TO HOLD-TDAA-RATE-AT-EOY OF 
045202         HOLD-TDAACCT.
045204     MOVE TDAA-RATE-LST-STM OF TDAACCT TO HOLD-TDAA-RATE-LST-STM  
045206         OF HOLD-TDAACCT.
045208     MOVE TDAA-ORG-YIELD-RT OF TDAACCT TO HOLD-TDAA-ORG-YIELD-RT  
045210         OF HOLD-TDAACCT.
045212     MOVE TDAA-REN-YIELD-RT OF TDAACCT TO HOLD-TDAA-REN-YIELD-RT  
045214         OF HOLD-TDAACCT.
045216     MOVE TDAA-SCHED-DT OF TDAACCT TO HOLD-TDAA-SCHED-DT OF       
045218         HOLD-TDAACCT.
045220     MOVE TDAA-ACCR-DT OF TDAACCT TO HOLD-TDAA-ACCR-DT OF         
045222         HOLD-TDAACCT.
045224     MOVE TDAA-OPEN-DT OF TDAACCT TO HOLD-TDAA-OPEN-DT OF         
045226         HOLD-TDAACCT.
045228     MOVE TDAA-CLSD-DT OF TDAACCT TO HOLD-TDAA-CLSD-DT OF         
045230         HOLD-TDAACCT.
045232     MOVE TDAA-LST-MAT-DT OF TDAACCT TO HOLD-TDAA-LST-MAT-DT OF   
045234         HOLD-TDAACCT.
045236     MOVE TDAA-LST-POST-DT OF TDAACCT TO HOLD-TDAA-LST-POST-DT OF 
045238         HOLD-TDAACCT.
045240     MOVE TDAA-LST-IN-PROC OF TDAACCT TO HOLD-TDAA-LST-IN-PROC OF 
045242         HOLD-TDAACCT.
045244     MOVE TDAA-LST-CONTACT OF TDAACCT TO HOLD-TDAA-LST-CONTACT OF 
045246         HOLD-TDAACCT.
045248     MOVE TDAA-LST-FEE-DT OF TDAACCT TO HOLD-TDAA-LST-FEE-DT OF   
045250         HOLD-TDAACCT.
045252     MOVE TDAA-LST-RTCHG-DT OF TDAACCT TO HOLD-TDAA-LST-RTCHG-DT  
045254         OF HOLD-TDAACCT.
045256     MOVE TDAA-LST-DIST-DT OF TDAACCT TO HOLD-TDAA-LST-DIST-DT OF 
045258         HOLD-TDAACCT.
045260     MOVE TDAA-LST-STMT-DT OF TDAACCT TO HOLD-TDAA-LST-STMT-DT OF 
045262         HOLD-TDAACCT.
045264     MOVE TDAA-LST-CMPD-DT OF TDAACCT TO HOLD-TDAA-LST-CMPD-DT OF 
045266         HOLD-TDAACCT.
045268     MOVE 1 TO Z-II.
045270 Z-13-1-2-LOOP.
045272     IF Z-II > 10
045274         GO TO Z-13-1-2-LOOP-XIT.
045276     MOVE TDAA-RR-CYC-DT OF TDAACCT (Z-II) TO HOLD-TDAA-RR-CYC-DT 
045278         OF HOLD-TDAACCT (Z-II).
045280     ADD 1 TO Z-II.
045282     GO TO Z-13-1-2-LOOP.
045284 Z-13-1-2-LOOP-XIT.
045286     MOVE TDAA-BNF-BIRTH-DT OF TDAACCT TO HOLD-TDAA-BNF-BIRTH-DT  
045288         OF HOLD-TDAACCT.
045290     MOVE TDAA-BNF-DEATH-DT OF TDAACCT TO HOLD-TDAA-BNF-DEATH-DT  
045292         OF HOLD-TDAACCT.
045294     MOVE TDAA-LUPD-DATE OF TDAACCT TO HOLD-TDAA-LUPD-DATE OF     
045296         HOLD-TDAACCT.
045298     MOVE TDAA-LUPD-TIME OF TDAACCT TO HOLD-TDAA-LUPD-TIME OF     
045300         HOLD-TDAACCT.
045302     MOVE TDAA-ADD-DT OF TDAACCT TO HOLD-TDAA-ADD-DT OF           
045304         HOLD-TDAACCT.
045306     MOVE TDAA-ADD-TM OF TDAACCT TO HOLD-TDAA-ADD-TM OF           
045308         HOLD-TDAACCT.
045310     MOVE TDAA-CONV-DT OF TDAACCT TO HOLD-TDAA-CONV-DT OF         
045312         HOLD-TDAACCT.
045314     MOVE TDAA-ACT-CLOSE-DT OF TDAACCT TO HOLD-TDAA-ACT-CLOSE-DT  
045316         OF HOLD-TDAACCT.
045318     MOVE TDAA-LST-TBACT-DT OF TDAACCT TO HOLD-TDAA-LST-TBACT-DT  
045320         OF HOLD-TDAACCT.
045322     MOVE TDAA-ALERT-EXP-DT OF TDAACCT TO HOLD-TDAA-ALERT-EXP-DT  
045324         OF HOLD-TDAACCT.
045326     MOVE TDAA-ALRT2-EXP-DT OF TDAACCT TO HOLD-TDAA-ALRT2-EXP-DT  
045328         OF HOLD-TDAACCT.
045330     MOVE TDAA-ALRT3-EXP-DT OF TDAACCT TO HOLD-TDAA-ALRT3-EXP-DT  
045332         OF HOLD-TDAACCT.
045334     MOVE TDAA-NXT-FEE-DT OF TDAACCT TO HOLD-TDAA-NXT-FEE-DT OF   
045336         HOLD-TDAACCT.
045338     MOVE TDAA-NXT-POST-DT OF TDAACCT TO HOLD-TDAA-NXT-POST-DT OF 
045340         HOLD-TDAACCT.
045342     MOVE TDAA-NXT-MAT-DT OF TDAACCT TO HOLD-TDAA-NXT-MAT-DT OF   
045344         HOLD-TDAACCT.
045346     MOVE TDAA-NXT-DIST-DT OF TDAACCT TO HOLD-TDAA-NXT-DIST-DT OF 
045348         HOLD-TDAACCT.
045350     MOVE TDAA-NXT-RT-CHG OF TDAACCT TO HOLD-TDAA-NXT-RT-CHG OF   
045352         HOLD-TDAACCT.
045354     MOVE TDAA-NXT-IN-PROC OF TDAACCT TO HOLD-TDAA-NXT-IN-PROC OF 
045356         HOLD-TDAACCT.
045358     MOVE TDAA-NXT-CMPD-DT OF TDAACCT TO HOLD-TDAA-NXT-CMPD-DT OF 
045360         HOLD-TDAACCT.
045362     MOVE TDAA-NXT-STMT-DT OF TDAACCT TO HOLD-TDAA-NXT-STMT-DT OF 
045364         HOLD-TDAACCT.
045366     MOVE TDAA-NXT-DS-PROC OF TDAACCT TO HOLD-TDAA-NXT-DS-PROC OF 
045368         HOLD-TDAACCT.
045370     MOVE TDAA-ADV-NTC-DT OF TDAACCT TO HOLD-TDAA-ADV-NTC-DT OF   
045372         HOLD-TDAACCT.
045374     MOVE TDAA-NXT-29YR-DT OF TDAACCT TO HOLD-TDAA-NXT-29YR-DT OF 
045376         HOLD-TDAACCT.
045378     MOVE TDAA-FAIR-MRKT-DT OF TDAACCT TO HOLD-TDAA-FAIR-MRKT-DT  
045380         OF HOLD-TDAACCT.
045382     MOVE TDAA-SORT-FIELD-1 OF TDAACCT TO HOLD-TDAA-SORT-FIELD-1  
045384         OF HOLD-TDAACCT.
045386     MOVE TDAA-SORT-FIELD-2 OF TDAACCT TO HOLD-TDAA-SORT-FIELD-2  
045388         OF HOLD-TDAACCT.
045390     MOVE TDAA-SORT-FIELD-3 OF TDAACCT TO HOLD-TDAA-SORT-FIELD-3  
045392         OF HOLD-TDAACCT.
045394     MOVE TDAA-SORT-FIELD-4 OF TDAACCT TO HOLD-TDAA-SORT-FIELD-4  
045396         OF HOLD-TDAACCT.
045398     MOVE TDAA-CMAT-PUB-ID OF TDAACCT TO HOLD-TDAA-CMAT-PUB-ID OF 
045400         HOLD-TDAACCT.
045402     MOVE TDAA-MSA-CONTR OF TDAACCT TO HOLD-TDAA-MSA-CONTR OF     
045404         HOLD-TDAACCT.
045406     MOVE TDAA-MSA-CONTR-LY OF TDAACCT TO HOLD-TDAA-MSA-CONTR-LY  
045408         OF HOLD-TDAACCT.
045410     MOVE TDAA-AVG-ACCR-INT OF TDAACCT TO HOLD-TDAA-AVG-ACCR-INT  
045412         OF HOLD-TDAACCT.
045414     MOVE TDAA-LEVEL-PAY OF TDAACCT TO HOLD-TDAA-LEVEL-PAY OF     
045416         HOLD-TDAACCT.
045418     MOVE TDAA-ST-INT-CD OF TDAACCT TO HOLD-TDAA-ST-INT-CD OF     
045420         HOLD-TDAACCT.
045422     MOVE TDAA-ST-WHLD-CD OF TDAACCT TO HOLD-TDAA-ST-WHLD-CD OF   
045424         HOLD-TDAACCT.
045426     MOVE TDAA-ST-WHLD-AMT OF TDAACCT TO HOLD-TDAA-ST-WHLD-AMT OF 
045428         HOLD-TDAACCT.
045430     MOVE TDAA-ST-CUR-W-AMT OF TDAACCT TO HOLD-TDAA-ST-CUR-W-AMT  
045432         OF HOLD-TDAACCT.
045434     MOVE TDAA-ST-LST-W-AMT OF TDAACCT TO HOLD-TDAA-ST-LST-W-AMT  
045436         OF HOLD-TDAACCT.
045438     MOVE TDAA-ST-WHLD-STD OF TDAACCT TO HOLD-TDAA-ST-WHLD-STD OF 
045440         HOLD-TDAACCT.
045442     MOVE TDAA-ST-WHLD-YTD OF TDAACCT TO HOLD-TDAA-ST-WHLD-YTD OF 
045444         HOLD-TDAACCT.
045446     MOVE TDAA-CIF-REMARK OF TDAACCT TO HOLD-TDAA-CIF-REMARK OF   
045448         HOLD-TDAACCT.
045450     MOVE TDAA-CSR OF TDAACCT TO HOLD-TDAA-CSR OF HOLD-TDAACCT.
045452     MOVE TDAA-BSA-O-RSK-CD OF TDAACCT TO HOLD-TDAA-BSA-O-RSK-CD  
045454         OF HOLD-TDAACCT.
045456     MOVE TDAA-BSA-C-RSK-CD OF TDAACCT TO HOLD-TDAA-BSA-C-RSK-CD  
045458         OF HOLD-TDAACCT.
045460     MOVE TDAA-LRG-TRX-DT OF TDAACCT TO HOLD-TDAA-LRG-TRX-DT OF   
045462         HOLD-TDAACCT.
045464     MOVE TDAA-HSA-FMLY-IND OF TDAACCT TO HOLD-TDAA-HSA-FMLY-IND  
045466         OF HOLD-TDAACCT.
045468     MOVE TDAA-STOP-PAY-IND OF TDAACCT TO HOLD-TDAA-STOP-PAY-IND  
045470         OF HOLD-TDAACCT.
045472     MOVE TDAA-IMG-PG-TYPE OF TDAACCT TO HOLD-TDAA-IMG-PG-TYPE OF 
045474         HOLD-TDAACCT.
045476     MOVE TDAA-CONT-LMT-CLC OF TDAACCT TO HOLD-TDAA-CONT-LMT-CLC  
045478         OF HOLD-TDAACCT.
045480     MOVE TDAA-CONT-LMT-ENT OF TDAACCT TO HOLD-TDAA-CONT-LMT-ENT  
045482         OF HOLD-TDAACCT.
045484     MOVE TDAA-MEMO-DB OF TDAACCT TO HOLD-TDAA-MEMO-DB OF         
045486         HOLD-TDAACCT.
045488     MOVE TDAA-MEMO-CR OF TDAACCT TO HOLD-TDAA-MEMO-CR OF         
045490         HOLD-TDAACCT.
045492     MOVE TDAA-MEMO-DB-2 OF TDAACCT TO HOLD-TDAA-MEMO-DB-2 OF     
045494         HOLD-TDAACCT.
045496     MOVE TDAA-MEMO-CR-2 OF TDAACCT TO HOLD-TDAA-MEMO-CR-2 OF     
045498         HOLD-TDAACCT.
045500     MOVE TDAA-RT-AT-CONV OF TDAACCT TO HOLD-TDAA-RT-AT-CONV OF   
045502         HOLD-TDAACCT.
045504     MOVE TDAA-ACCR-AT-CONV OF TDAACCT TO HOLD-TDAA-ACCR-AT-CONV  
045506         OF HOLD-TDAACCT.
045508     MOVE TDAA-RT-AT-ACRDT OF TDAACCT TO HOLD-TDAA-RT-AT-ACRDT OF 
045510         HOLD-TDAACCT.
045512     MOVE TDAA-BAL-AT-ACRDT OF TDAACCT TO HOLD-TDAA-BAL-AT-ACRDT  
045514         OF HOLD-TDAACCT.
045516     MOVE TDAA-ZERO-RT-ALLOW OF TDAACCT TO                        
045518         HOLD-TDAA-ZERO-RT-ALLOW OF HOLD-TDAACCT.
045520     MOVE TDAA-EMAIL-NTC OF TDAACCT TO HOLD-TDAA-EMAIL-NTC OF     
045522         HOLD-TDAACCT.
045524     MOVE TDAA-EMAIL-STMT OF TDAACCT TO HOLD-TDAA-EMAIL-STMT OF   
045526         HOLD-TDAACCT.
045528     MOVE TDAA-FRAUD-CK-DT OF TDAACCT TO HOLD-TDAA-FRAUD-CK-DT OF 
045530         HOLD-TDAACCT.
045532     MOVE TDAA-FRAUD-CK-CNT OF TDAACCT TO HOLD-TDAA-FRAUD-CK-CNT  
045534         OF HOLD-TDAACCT.
045536     MOVE TDAA-FRAUD-CK-AMT OF TDAACCT TO HOLD-TDAA-FRAUD-CK-AMT  
045538         OF HOLD-TDAACCT.
045540     MOVE TDAA-MISC-ACCTNO OF TDAACCT TO HOLD-TDAA-MISC-ACCTNO OF 
045542         HOLD-TDAACCT.
045544     MOVE TDAA-RMD-MAN-CALC OF TDAACCT TO HOLD-TDAA-RMD-MAN-CALC  
045546         OF HOLD-TDAACCT.
045548     MOVE TDAA-RMD-AMOUNT OF TDAACCT TO HOLD-TDAA-RMD-AMOUNT OF   
045550         HOLD-TDAACCT.
045552     MOVE TDAA-BROKERAGE-ID OF TDAACCT TO HOLD-TDAA-BROKERAGE-ID  
045554         OF HOLD-TDAACCT.
045556     MOVE TDAA-MONY-SRC-CD2 OF TDAACCT TO HOLD-TDAA-MONY-SRC-CD2  
045558         OF HOLD-TDAACCT.
045560     MOVE TDAA-INHERIT-IRA OF TDAACCT TO HOLD-TDAA-INHERIT-IRA OF 
045562         HOLD-TDAACCT.
045564     MOVE TDAA-LIFE-FACTOR OF TDAACCT TO HOLD-TDAA-LIFE-FACTOR OF 
045566         HOLD-TDAACCT.
045568     MOVE TDAA-EV-LARGE-TRX OF TDAACCT TO HOLD-TDAA-EV-LARGE-TRX  
045570         OF HOLD-TDAACCT.
045572     MOVE TDAA-EV-MAT-AMT OF TDAACCT TO HOLD-TDAA-EV-MAT-AMT OF   
045574         HOLD-TDAACCT.
045576     MOVE TDAA-EV-DISP-ACCT OF TDAACCT TO HOLD-TDAA-EV-DISP-ACCT  
045578         OF HOLD-TDAACCT.
045580     MOVE TDAA-EV-COMP-ACCT OF TDAACCT TO HOLD-TDAA-EV-COMP-ACCT  
045582         OF HOLD-TDAACCT.
045584     MOVE TDAA-EV-PUBLIC-ID OF TDAACCT TO HOLD-TDAA-EV-PUBLIC-ID  
045586         OF HOLD-TDAACCT.
045588     MOVE TDAA-EV-MAT-TYPE OF TDAACCT TO HOLD-TDAA-EV-MAT-TYPE OF 
045590         HOLD-TDAACCT.
045592     MOVE TDAA-EV-INT-TYPE OF TDAACCT TO HOLD-TDAA-EV-INT-TYPE OF 
045594         HOLD-TDAACCT.
045596     MOVE TDAA-EV-ACCT-TYP OF TDAACCT TO HOLD-TDAA-EV-ACCT-TYP OF 
045598         HOLD-TDAACCT.
045600     MOVE TDAA-EV-WHLD-PCT OF TDAACCT TO HOLD-TDAA-EV-WHLD-PCT OF 
045602         HOLD-TDAACCT.
045604     MOVE TDAA-EV-NON-ACCR OF TDAACCT TO HOLD-TDAA-EV-NON-ACCR OF 
045606         HOLD-TDAACCT.
045608     MOVE TDAA-EV-CLOSED OF TDAACCT TO HOLD-TDAA-EV-CLOSED OF     
045610         HOLD-TDAACCT.
045612     MOVE TDAA-EV-CLOSE-MO OF TDAACCT TO HOLD-TDAA-EV-CLOSE-MO OF 
045614         HOLD-TDAACCT.
045616     MOVE TDAA-EV-OPEN-MO OF TDAACCT TO HOLD-TDAA-EV-OPEN-MO OF   
045618         HOLD-TDAACCT.
045620     MOVE TDAA-EV-ANN-INT OF TDAACCT TO HOLD-TDAA-EV-ANN-INT OF   
045622         HOLD-TDAACCT.
045624     MOVE TDAA-EV-ORIG-RT OF TDAACCT TO HOLD-TDAA-EV-ORIG-RT OF   
045626         HOLD-TDAACCT.
045628     MOVE TDAA-EV-DLY-INT OF TDAACCT TO HOLD-TDAA-EV-DLY-INT OF   
045630         HOLD-TDAACCT.
045632     MOVE TDAA-EV-INT-PAY OF TDAACCT TO HOLD-TDAA-EV-INT-PAY OF   
045634         HOLD-TDAACCT.
045636     MOVE TDAA-EV-AVAIL-BL OF TDAACCT TO HOLD-TDAA-EV-AVAIL-BL OF 
045638         HOLD-TDAACCT.
045640     MOVE TDAA-EV-RETAIN OF TDAACCT TO HOLD-TDAA-EV-RETAIN OF     
045642         HOLD-TDAACCT.
045644     MOVE TDAA-EV-CL-RETAIN OF TDAACCT TO HOLD-TDAA-EV-CL-RETAIN  
045646         OF HOLD-TDAACCT.
045648     MOVE TDAA-EV-TIMES-REN OF TDAACCT TO HOLD-TDAA-EV-TIMES-REN  
045650         OF HOLD-TDAACCT.
045652     MOVE TDAA-EV-CURR-BAL OF TDAACCT TO HOLD-TDAA-EV-CURR-BAL OF 
045654         HOLD-TDAACCT.
045656     MOVE TDAA-BRKR-DEP-CAT OF TDAACCT TO HOLD-TDAA-BRKR-DEP-CAT  
045658         OF HOLD-TDAACCT.
045660     MOVE TDAA-LINE-OF-BUS OF TDAACCT TO HOLD-TDAA-LINE-OF-BUS OF 
045662         HOLD-TDAACCT.
045664     MOVE TDAA-1ST-STMT OF TDAACCT TO HOLD-TDAA-1ST-STMT OF       
045666         HOLD-TDAACCT.
045668     MOVE TDAA-POSTAL-CITY OF TDAACCT TO HOLD-TDAA-POSTAL-CITY OF 
045670         HOLD-TDAACCT.
045672     MOVE TDAA-POSTAL-CNTRY OF TDAACCT TO HOLD-TDAA-POSTAL-CNTRY  
045674         OF HOLD-TDAACCT.
045676     MOVE TDAA-CITIZN-CNTRY OF TDAACCT TO HOLD-TDAA-CITIZN-CNTRY  
045678         OF HOLD-TDAACCT.
045680     MOVE TDAA-CUSTM-FIELDS OF TDAACCT TO HOLD-TDAA-CUSTM-FIELDS  
045682         OF HOLD-TDAACCT.
045684     MOVE TDAA-AVG-STEP-RT OF TDAACCT TO HOLD-TDAA-AVG-STEP-RT OF 
045686         HOLD-TDAACCT.
045688     MOVE TDAA-MONITOR-INQ OF TDAACCT TO HOLD-TDAA-MONITOR-INQ OF 
045690         HOLD-TDAACCT.
045692     MOVE TDAA-IGL-GRP-2 OF TDAACCT TO HOLD-TDAA-IGL-GRP-2 OF     
045694         HOLD-TDAACCT.
045696     MOVE TDAA-AGG-DAYS-QTD OF TDAACCT TO HOLD-TDAA-AGG-DAYS-QTD  
045698         OF HOLD-TDAACCT.
045700     MOVE TDAA-AGG-BAL-QTD OF TDAACCT TO HOLD-TDAA-AGG-BAL-QTD OF 
045702         HOLD-TDAACCT.
045704     MOVE TDAA-IGL-GRP-3 OF TDAACCT TO HOLD-TDAA-IGL-GRP-3 OF     
045706         HOLD-TDAACCT.
045708     MOVE TDAA-ALT-ADDR-EOY OF TDAACCT TO HOLD-TDAA-ALT-ADDR-EOY  
045710         OF HOLD-TDAACCT.
045712     MOVE TDAA-1042S-TAX-ID OF TDAACCT TO HOLD-TDAA-1042S-TAX-ID  
045714         OF HOLD-TDAACCT.
045716     MOVE TDAA-LEC OF TDAACCT TO HOLD-TDAA-LEC OF HOLD-TDAACCT.
045718     MOVE TDAA-BAL-AT-CLOSE OF TDAACCT TO HOLD-TDAA-BAL-AT-CLOSE  
045720         OF HOLD-TDAACCT.
045722     MOVE TDAA-AVL-CAP-INT OF TDAACCT TO HOLD-TDAA-AVL-CAP-INT OF 
045724         HOLD-TDAACCT.
045726     MOVE TDAA-FIDM-TR-FUND OF TDAACCT TO HOLD-TDAA-FIDM-TR-FUND  
045728         OF HOLD-TDAACCT.
045730     MOVE TDAA-IRS-FRM-DLVR OF TDAACCT TO HOLD-TDAA-IRS-FRM-DLVR  
045732         OF HOLD-TDAACCT.
045734     MOVE TDAA-PROVINCE OF TDAACCT TO HOLD-TDAA-PROVINCE OF       
045736         HOLD-TDAACCT.
045738     MOVE TDAA-PROMOTION OF TDAACCT TO HOLD-TDAA-PROMOTION OF     
045740         HOLD-TDAACCT.
045742*THE FOLLOWING MOVES FOR SQL ONLY                                 
045744     IF Z-EDIT-ERROR
045746         GO TO Z-13-XIT.
045748 Z-13-SKIP.
045750 Z-13-XIT.
045752     EXIT.
045754*
045756*****************************************************************
045758*    PROCEDURE TDB-CUST-INQ
045760*****************************************************************
045762 Z-14-PROCEDURE.
045764*
045766     MOVE 0 TO Z-EXIT-CODE.
045768     MOVE 9999 TO Z-EXIT-LEVEL.
045770     MOVE " " TO WS-ADJUSTED-IND.
045772     IF TDB-READ-INFO = "01BAT2"
045774         NEXT SENTENCE ELSE
045776         GO TO Z-14-2-1-ELSE.
045778     MOVE ZERO TO Z-FLINFO11-PRES.
045780     MOVE 13 TO Z-FLINFO11-LAST-SEQ.
045782     MOVE ZERO TO Z-FLINFO11-SOME.
045784 Z-14-3-READ.
045786     FIND TDACUST OF LDBTDADB VIA TDACMSET OF TDACUST OF LDBTDADB
045788     AT TDAC-BANK = TDB-TDAC-BANK AND
045790        TDAC-CUST = TDB-TDAC-CUST
045792         ON EXCEPTION
045794         MOVE 13 TO Z-DMS-EXCEPT-SEQ
045796         IF DMSTATUS (NOTFOUND) OR DMSTATUS (NORECORD)
045798             GO TO Z-14-3-XIT
045800         ELSE
045802             MOVE "TDACMSET OF TDACUST OF LDBTDADB" TO            
045804                 Z-DMS-EXCEPT-STR
045806             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
045808             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
045810
045812 Z-14-3-PRESENT.
045814*
045816     MOVE 1 TO Z-FLINFO11-SOME.
045818     MOVE 1 TO Z-FLINFO11-PRES.
045820     GO TO Z-14-3-CONT.
045822 Z-14-3-XIT.
045824 Z-14-3-CONT.
045826     IF Z-FLINFO11-ABSENT
045828         NEXT SENTENCE ELSE
045830         GO TO Z-14-4-1-ELSE.
045832     MOVE 0310 TO TDB-ERROR-NBR.
045834     GO TO Z-14-4-ENDIF.
045836 Z-14-4-1-ELSE.
045838     IF TDB-READ-DATE NOT = 0
045840         NEXT SENTENCE ELSE
045842         GO TO Z-14-4-2-ELSE.
045844************ PERFORM TDB-CUST-01BAT2-ACTV-ADJ
045846     PERFORM Z-32-PROCEDURE THRU Z-32-XIT.
045848     IF  Z-EXIT-EDITEXIT
045850         GO TO Z-14-XIT.
045852     IF  Z-DMS2-ABORT-FLAG = 1
045854         GO TO Z-14-XIT.
045856     IF  Z-EXIT-LEVEL < 0
045858         GO TO Z-14-END.
045860*
045862     MOVE HOLD-TDAC-BANK OF HOLD-TDACUST TO TDB-TDAC-BANK OF      
045864         TDB-TDACUST.
045866     MOVE HOLD-TDAC-CUST OF HOLD-TDACUST TO TDB-TDAC-CUST OF      
045868         TDB-TDACUST.
045870     MOVE HOLD-TDAC-BRCH OF HOLD-TDACUST TO TDB-TDAC-BRCH OF      
045872         TDB-TDACUST.
045874     MOVE HOLD-TDAC-STATUS OF HOLD-TDACUST TO TDB-TDAC-STATUS OF  
045876         TDB-TDACUST.
045878     MOVE HOLD-TDAC-NAME-1 OF HOLD-TDACUST TO TDB-TDAC-NAME-1 OF  
045880         TDB-TDACUST.
045882     MOVE HOLD-TDAC-N1-KEY OF HOLD-TDACUST TO TDB-TDAC-N1-KEY OF  
045884         TDB-TDACUST.
045886     MOVE HOLD-TDAC-N1-FIRST OF HOLD-TDACUST TO TDB-TDAC-N1-FIRST 
045888         OF TDB-TDACUST.
045890     MOVE HOLD-TDAC-N1-MID OF HOLD-TDACUST TO TDB-TDAC-N1-MID OF  
045892         TDB-TDACUST.
045894     MOVE HOLD-TDAC-N1-LAST OF HOLD-TDACUST TO TDB-TDAC-N1-LAST   
045896         OF TDB-TDACUST.
045898     MOVE HOLD-TDAC-N1-PREFIX OF HOLD-TDACUST TO                  
045900         TDB-TDAC-N1-PREFIX OF TDB-TDACUST.
045902     MOVE HOLD-TDAC-N1-SUFFIX OF HOLD-TDACUST TO                  
045904         TDB-TDAC-N1-SUFFIX OF TDB-TDACUST.
045906     MOVE HOLD-TDAC-N1-FAMILIAR OF HOLD-TDACUST TO                
045908         TDB-TDAC-N1-FAMILIAR OF TDB-TDACUST.
045910     MOVE HOLD-TDAC-N1-PRT-PFX OF HOLD-TDACUST TO                 
045912         TDB-TDAC-N1-PRT-PFX OF TDB-TDACUST.
045914     MOVE HOLD-TDAC-N1-PRT-SFX OF HOLD-TDACUST TO                 
045916         TDB-TDAC-N1-PRT-SFX OF TDB-TDACUST.
045918     MOVE HOLD-TDAC-N1-DESIGNAT OF HOLD-TDACUST TO                
045920         TDB-TDAC-N1-DESIGNAT OF TDB-TDACUST.
045922     MOVE HOLD-TDAC-NAME-2 OF HOLD-TDACUST TO TDB-TDAC-NAME-2 OF  
045924         TDB-TDACUST.
045926     MOVE HOLD-TDAC-N2-MODIFIED OF HOLD-TDACUST TO                
045928         TDB-TDAC-N2-MODIFIED OF TDB-TDACUST.
045930     MOVE HOLD-TDAC-N2-PRINT-CD OF HOLD-TDACUST TO                
045932         TDB-TDAC-N2-PRINT-CD OF TDB-TDACUST.
045934     MOVE HOLD-TDAC-N2-KEY OF HOLD-TDACUST TO TDB-TDAC-N2-KEY OF  
045936         TDB-TDACUST.
045938     MOVE HOLD-TDAC-N2-FIRST OF HOLD-TDACUST TO TDB-TDAC-N2-FIRST 
045940         OF TDB-TDACUST.
045942     MOVE HOLD-TDAC-N2-MID OF HOLD-TDACUST TO TDB-TDAC-N2-MID OF  
045944         TDB-TDACUST.
045946     MOVE HOLD-TDAC-N2-LAST OF HOLD-TDACUST TO TDB-TDAC-N2-LAST   
045948         OF TDB-TDACUST.
045950     MOVE HOLD-TDAC-N2-PREFIX OF HOLD-TDACUST TO                  
045952         TDB-TDAC-N2-PREFIX OF TDB-TDACUST.
045954     MOVE HOLD-TDAC-N2-SUFFIX OF HOLD-TDACUST TO                  
045956         TDB-TDAC-N2-SUFFIX OF TDB-TDACUST.
045958     MOVE HOLD-TDAC-N2-FAMILIAR OF HOLD-TDACUST TO                
045960         TDB-TDAC-N2-FAMILIAR OF TDB-TDACUST.
045962     MOVE HOLD-TDAC-N2-PRT-PFX OF HOLD-TDACUST TO                 
045964         TDB-TDAC-N2-PRT-PFX OF TDB-TDACUST.
045966     MOVE HOLD-TDAC-N2-PRT-SFX OF HOLD-TDACUST TO                 
045968         TDB-TDAC-N2-PRT-SFX OF TDB-TDACUST.
045970     MOVE HOLD-TDAC-N2-DESIGNAT OF HOLD-TDACUST TO                
045972         TDB-TDAC-N2-DESIGNAT OF TDB-TDACUST.
045974     MOVE HOLD-TDAC-NAME-3 OF HOLD-TDACUST TO TDB-TDAC-NAME-3 OF  
```

⚠️  This is the source code you must document.
    438 lines from 22546 to 22983.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

