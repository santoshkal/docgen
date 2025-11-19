# LLM Request Debug File
Generated: 2025-11-17T20:50:52.664744

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 21/55
- **Model**: gpt-4.1
- **Chunk Number**: 21
- **Pass Number**: 3
- **Attempt Number**: 3 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~6,962 tokens
- **Total Input**: ~8,920 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 21/55" (ID: detailed-code-explanation)

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


**CHUNK 21 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-17T19:50:50.832678", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 21 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 10274 to 10546 (273 lines)\nChunk Tokens (estimated): ~5,865\nActual Input Tokens: 7,271 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 10274-10546 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 21 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 21 of 55.\n\n\n=============================================================================\nCHUNK 21 SOURCE CODE (Lines 10274-10546)\n=============================================================================\n\n```cobol\n020556                 TDB-TDA-ACTV-DATA.                               \n020558             15  TDB-TDA-ACTVI-F-INT-X.                           \n020560                 20  TDB-TDA-ACTVI-F-INT      PIC S9(12)V9(6).    \n020562             15  TDB-TDA-ACTVI-T-INT-X.                           \n020564                 20  TDB-TDA-ACTVI-T-INT      PIC S9(12)V9(6).    \n020566             15  TDB-TDA-ACTVI-F-INTA-X.                          \n020568                 20  TDB-TDA-ACTVI-F-INTA     PIC S9(12)V99.      \n020570             15  TDB-TDA-ACTVI-T-INTA-X.                          \n020572                 20  TDB-TDA-ACTVI-T-INTA     PIC S9(12)V99.      \n020574             15  TDB-TDA-ACTVI-F-PDAY-X.                          \n020576                 20  TDB-TDA-ACTVI-F-PDAY     PIC S9(12)V9(6).    \n020578             15  TDB-TDA-ACTVI-T-PDAY-X.                          \n020580                 20  TDB-TDA-ACTVI-T-PDAY     PIC S9(12)V9(6).    \n020582             15  TDB-TDA-ACTVI-RD-DT-X.                           \n020584                 20  TDB-TDA-ACTVI-RD-DT      PIC 9(08).          \n020586             15  FILLER                       PIC X(292).         \n020588                                                                  \n020590         10  TDB-TDA-ACTCK-CHECK    REDEFINES                     \n020592                 TDB-TDA-ACTV-DATA.                               \n020594             15  TDB-TDA-ACTCK-F-I-PT-X.                          \n020596                 20  TDB-TDA-ACTCK-F-I-PT      PIC S9(12)V99.     \n020598             15  TDB-TDA-ACTCK-T-I-PT-X.                          \n020600                 20  TDB-TDA-ACTCK-T-I-PT      PIC S9(12)V99.     \n020602             15  TDB-TDA-ACTCK-F-C-WA-X.                          \n020604                 20  TDB-TDA-ACTCK-F-C-WA      PIC S9(12)V99.     \n020606             15  TDB-TDA-ACTCK-T-C-WA-X.                          \n020608                 20  TDB-TDA-ACTCK-T-C-WA      PIC S9(12)V99.     \n020610             15  TDB-TDA-ACTCK-F-STAT-X.                          \n020612                 20  TDB-TDA-ACTCK-F-STAT      PIC X.             \n020614             15  TDB-TDA-ACTCK-T-STAT-X.                          \n020616                 20  TDB-TDA-ACTCK-T-STAT      PIC X.             \n020618             15  TDB-TDA-ACTCK-PRS-DT-X.                          \n020620                 20  TDB-TDA-ACTCK-PRS-DT      PIC 9(08).         \n020622             15  TDB-TDA-ACTCK-F-ST-WA-X.                         \n020624                 20  TDB-TDA-ACTCK-F-ST-WA     PIC S9(12)V99.     \n020626             15  TDB-TDA-ACTCK-T-ST-WA-X.                         \n020628                 20  TDB-TDA-ACTCK-T-ST-WA     PIC S9(12)V99.     \n020630             15  FILLER                        PIC X(306).        \n020632                                                                  \n020634         10  TDB-TDA-ACTWH-WITHHOLD REDEFINES                     \n020636                 TDB-TDA-ACTV-DATA.                               \n020638             15  TDB-TDA-ACTWH-F-YTD-X.                           \n020640                 20  TDB-TDA-ACTWH-F-YTD       PIC S9(12)V99.     \n020642             15  TDB-TDA-ACTWH-T-YTD-X.                           \n020644                 20  TDB-TDA-ACTWH-T-YTD       PIC S9(12)V99.     \n020646             15  TDB-TDA-ACTWH-F-STD-X.                           \n020648                 20  TDB-TDA-ACTWH-F-STD       PIC S9(12)V99.     \n020650             15  TDB-TDA-ACTWH-T-STD-X.                           \n020652                 20  TDB-TDA-ACTWH-T-STD       PIC S9(12)V99.     \n020654             15  TDB-TDA-ACTWH-F-L-AMT-X.                         \n020656                 20  TDB-TDA-ACTWH-F-L-AMT     PIC S9(12)V99.     \n020658             15  TDB-TDA-ACTWH-T-L-AMT-X.                         \n020660                 20  TDB-TDA-ACTWH-T-L-AMT     PIC S9(12)V99.     \n020662             15 FILLER                         PIC X(316).        \n020664                                                                  \n020666         10  TDB-TDA-ACTPT-INT-POST REDEFINES                     \n020668                 TDB-TDA-ACTV-DATA.                               \n020670             15  TDB-TDA-ACTPT-F-IP-L-X.                          \n020672                 20  TDB-TDA-ACTPT-F-IP-L      PIC S9(12)V99.     \n020674             15  TDB-TDA-ACTPT-T-IP-L-X.                          \n020676                 20  TDB-TDA-ACTPT-T-IP-L      PIC S9(12)V99.     \n020678             15  TDB-TDA-ACTPT-F-1099-X.                          \n020680                 20  TDB-TDA-ACTPT-F-1099      PIC S9(12)V99.     \n020682             15  TDB-TDA-ACTPT-T-1099-X.                          \n020684                 20  TDB-TDA-ACTPT-T-1099      PIC S9(12)V99.     \n020686             15  TDB-TDA-ACTPT-F-C-BL-X.                          \n020688                 20  TDB-TDA-ACTPT-F-C-BL      PIC S9(12)V99.     \n020690             15  TDB-TDA-ACTPT-T-C-BL-X.                          \n020692                 20  TDB-TDA-ACTPT-T-C-BL      PIC S9(12)V99.     \n020694             15  TDB-TDA-ACTPT-F-L-DT-X.                          \n020696                 20  TDB-TDA-ACTPT-F-L-DT      PIC 9(08).         \n020698             15  TDB-TDA-ACTPT-T-L-DT-X.                          \n020700                 20  TDB-TDA-ACTPT-T-L-DT      PIC 9(08).         \n020702             15  TDB-TDA-ACTPT-F-N-DT-X.                          \n020704                 20  TDB-TDA-ACTPT-F-N-DT      PIC 9(08).         \n020706             15  TDB-TDA-ACTPT-T-N-DT-X.                          \n020708                 20  TDB-TDA-ACTPT-T-N-DT      PIC 9(08).         \n020710             15  TDB-TDA-ACTPT-F-I-PT-X.                          \n020712                 20  TDB-TDA-ACTPT-F-I-PT      PIC S9(12)V99.     \n020714             15  TDB-TDA-ACTPT-T-I-PT-X.                          \n020716                 20  TDB-TDA-ACTPT-T-I-PT      PIC S9(12)V99.     \n020718             15  TDB-TDA-ACTPT-F-C-WA-X.                          \n020720                 20  TDB-TDA-ACTPT-F-C-WA      PIC S9(12)V99.     \n020722             15  TDB-TDA-ACTPT-T-C-WA-X.                          \n020724                 20  TDB-TDA-ACTPT-T-C-WA      PIC S9(12)V99.     \n020726             15  TDB-TDA-ACTPT-F-ACCR-X.                          \n020728                 20  TDB-TDA-ACTPT-F-ACCR      PIC S9(12)V9(06).  \n020730             15  TDB-TDA-ACTPT-T-ACCR-X.                          \n020732                 20  TDB-TDA-ACTPT-T-ACCR      PIC S9(12)V9(06).  \n020734             15  TDB-TDA-ACTPT-F-STAT          PIC X(01).         \n020736             15  TDB-TDA-ACTPT-T-STAT          PIC X(01).         \n020738             15  TDB-TDA-ACTPT-F-A-DT-X.                          \n020740                 20  TDB-TDA-ACTPT-F-A-DT      PIC 9(8).          \n020742             15  TDB-TDA-ACTPT-T-A-DT-X.                          \n020744                 20  TDB-TDA-ACTPT-T-A-DT      PIC 9(8).          \n020746             15  TDB-TDA-ACTPT-F-PDAY-X.                          \n020748                 20  TDB-TDA-ACTPT-F-PDAY      PIC S9(12)V9(6).   \n020750             15  TDB-TDA-ACTPT-T-PDAY-X.                          \n020752                 20  TDB-TDA-ACTPT-T-PDAY      PIC S9(12)V9(6).   \n020754             15  TDB-TDA-ACTPT-N-INT-X.                           \n020756                 20  TDB-TDA-ACTPT-N-INT       PIC S9(12)V99.     \n020758             15  TDB-TDA-ACTPT-C-INT-X.                           \n020760                 20  TDB-TDA-ACTPT-C-INT       PIC S9(12)V99.     \n020762             15  TDB-TDA-ACTPT-DISP-CD-X.                         \n020764                 20  TDB-TDA-ACTPT-DISP-CD     PIC 9(01).         \n020766             15  TDB-TDA-ACTPT-INT-ACCT-X.                        \n020768                 20  TDB-TDA-ACTPT-INT-ACCT    PIC 9(12).         \n020770             15  TDB-TDA-ACTPT-INT-ACCT-S-X.                      \n020772                 20  TDB-TDA-ACTPT-INT-ACCT-S  PIC 9(10).         \n020774             15  TDB-TDA-ACTPT-F-ST-WA-X.                         \n020776                 20  TDB-TDA-ACTPT-F-ST-WA     PIC S9(12)V99.     \n020778             15  TDB-TDA-ACTPT-T-ST-WA-X.                         \n020780                 20  TDB-TDA-ACTPT-T-ST-WA     PIC S9(12)V99.     \n020782             15  TDB-TDA-ACTPT-NEW-BAL-X.                         \n020784                 20  TDB-TDA-ACTPT-NEW-BAL     PIC S9(12)V99.     \n020786             15  TDB-TDA-ACTPT-CLO-MAT-X.                         \n020788                 20  TDB-TDA-ACTPT-CLO-MAT     PIC 9.             \n020790             15  FILLER                        PIC X(44).         \n020792                                                                  \n020794         10  TDB-TDA-ACTAC-CLOSE-ACCT REDEFINES                   \n020796                 TDB-TDA-ACTV-DATA.                               \n020798             15  TDB-TDA-ACTAC-AMT           PIC S9(12)V9(2).     \n020800             15  TDB-TDA-ACTAC-INT           PIC S9(12)V9(2).     \n020802             15  TDB-TDA-ACTAC-PENLTY        PIC S9(12)V9(2).     \n020804             15  TDB-TDA-ACTAC-WTHLD         PIC S9(12)V9(2).     \n020806             15  TDB-TDA-ACTAC-LST-INT       PIC S9(12)V9(2).     \n020808             15  TDB-TDA-ACTAC-W-ALLOW       PIC 9(1).            \n020810             15  TDB-TDA-ACTAC-D-ALLOW       PIC 9(1).            \n020812             15  TDB-TDA-ACTAC-CUR-PEN       PIC S9(12)V9(2).     \n020814             15  TDB-TDA-ACTAC-AVL-BAL       PIC S9(12)V9(2).     \n020816             15  TDB-TDA-ACTAC-DS-TYPE       PIC X(02).           \n020818             15  TDB-TDA-ACTAC-ST-WHLD       PIC S9(12)V99.       \n020820             15  TDB-TDA-ACTAC-DRP-INT       PIC S9(12)V99.       \n020822             15  TDB-TDA-ACTAC-DS-DISP       PIC 9.               \n020824             15  TDB-TDA-ACTAC-CLO-MAT       PIC 9.               \n020826             15  TDB-TDA-ACTAC-T-ACCT        PIC 9(12).           \n020828             15  TDB-TDA-ACTAC-T-ACCTS       PIC 9(10).           \n020830             15  TDB-TDA-ACTAC-DS-CODE       PIC 9(1).            \n020832             15  TDB-TDA-ACTAC-DS-NBR        PIC 9(2).            \n020834             15  TDB-TDA-ACTAC-DESC          PIC X(30).           \n020836             15  FILLER                      PIC X(213).          \n020838                                                                  \n020840         10  TDB-TDA-ACTDS-DISTRIBUTE REDEFINES                   \n020842                 TDB-TDA-ACTV-DATA.                               \n020844             15  TDB-TDA-ACTDS-TYPE          PIC XX.              \n020846             15  TDB-TDA-ACTDS-DISP-CD-X.                         \n020848                 20  TDB-TDA-ACTDS-DISP-CD   PIC 9(01).           \n020850             15  TDB-TDA-ACTDS-INT-X.                             \n020852                 20  TDB-TDA-ACTDS-INT       PIC 9(01).           \n020854             15  TDB-TDA-ACTDS-PRNCPAL-X.                         \n020856                 20  TDB-TDA-ACTDS-PRNCPAL   PIC 9(01).           \n020858             15  TDB-TDA-ACTDS-CD-X.                              \n020860                 20  TDB-TDA-ACTDS-CD        PIC 9(01).           \n020862             15  TDB-TDA-ACTDS-NXT-DT-X.                          \n020864                 20  TDB-TDA-ACTDS-NXT-DT    PIC 9(08).           \n020866             15  TDB-TDA-ACTDS-W-AMT-X.                           \n020868                 20  TDB-TDA-ACTDS-W-AMT     PIC S9(12)V99.       \n020870             15  TDB-TDA-ACTDS-W-CD-X.                            \n020872                 20  TDB-TDA-ACTDS-W-CD      PIC 9(01).           \n020874             15  TDB-TDA-ACTDS-AMT-X.                             \n020876                 20  TDB-TDA-ACTDS-AMT       PIC S9(12)V99.       \n020878             15  TDB-TDA-ACTDS-FREQ-X.                            \n020880                 20  TDB-TDA-ACTDS-FREQ      PIC 9(01).           \n020882             15  TDB-TDA-ACTDS-NTRVL-X.                           \n020884                 20  TDB-TDA-ACTDS-NTRVL     PIC 9(04).           \n020886             15  TDB-TDA-ACTDS-T-ACCT-X.                          \n020888                 20  TDB-TDA-ACTDS-T-ACCT    PIC 9(12).           \n020890             15  TDB-TDA-ACTDS-T-ACCTS-X.                         \n020892                 20  TDB-TDA-ACTDS-T-ACCTS   PIC 9(10).           \n020894             15  TDB-TDA-ACTDS-ST-WAMT-X.                         \n020896                 20  TDB-TDA-ACTDS-ST-WAMT   PIC S9(12)V99.       \n020898             15  TDB-TDA-ACTDS-ST-W-CD-X.                         \n020900                 20  TDB-TDA-ACTDS-ST-W-CD   PIC 9(01).           \n020902             15  TDB-TDA-ACTDS-NEW-BAL-X.                         \n020904                 20  TDB-TDA-ACTDS-NEW-BAL   PIC S9(12)V99.       \n020906             15  TDB-TDA-ACTDS-DS-NBR-X.                          \n020908                 20  TDB-TDA-ACTDS-DS-NBR    PIC 9(2).            \n020910             15  FILLER                      PIC X(299).          \n020912                                                                  \n020914         10  TDB-TDA-ACTE-ERASER REDEFINES                        \n020916                 TDB-TDA-ACTV-DATA.                               \n020918             15  TDB-TDA-ACTE-SERIAL-X.                           \n020920                 20  TDB-TDA-ACTE-SERIAL     PIC 9(12).           \n020922             15  TDB-TDA-ACTE-TYPE-X.                             \n020924                 20  TDB-TDA-ACTE-TYPE       PIC 9(02).           \n020926             15  TDB-TDA-ACTE-EFF-DT-X.                           \n020928                 20  TDB-TDA-ACTE-EFF-DT     PIC 9(08).           \n020930             15  TDB-TDA-ACTE-DATE-X.                             \n020932                 20  TDB-TDA-ACTE-DATE       PIC 9(08).           \n020934             15  TDB-TDA-ACTE-SEQ-NBR-X.                          \n020936                 20  TDB-TDA-ACTE-SEQ-NBR    PIC 9(02).           \n020938             15  FILLER                      PIC X(368).          \n020940                                                                  \n020942         10  TDB-TDA-ACTCP-COMPOUND REDEFINES                     \n020944                 TDB-TDA-ACTV-DATA.                               \n020946             15  TDB-TDA-ACTCP-P-INT-X.                           \n020948                 20  TDB-TDA-ACTCP-P-INT      PIC S9(12)V9(6).    \n020950             15  TDB-TDA-ACTCP-N-INT-X.                           \n020952                 20  TDB-TDA-ACTCP-N-INT      PIC S9(12)V9(6).    \n020954             15  TDB-TDA-ACTCP-P-PDAY-X.                          \n020956                 20  TDB-TDA-ACTCP-P-PDAY     PIC S9(12)V9(6).    \n020958             15  TDB-TDA-ACTCP-N-PDAY-X.                          \n020960                 20  TDB-TDA-ACTCP-N-PDAY     PIC S9(12)V9(6).    \n020962             15  TDB-TDA-ACTCP-P-INTA-X.                          \n020964                 20  TDB-TDA-ACTCP-P-INTA     PIC S9(12)V9(2).    \n020966             15  TDB-TDA-ACTCP-N-INTA-X.                          \n020968                 20  TDB-TDA-ACTCP-N-INTA     PIC S9(12)V9(2).    \n020970             15  TDB-TDA-ACTCP-P-A-DT-X.                          \n020972                 20  TDB-TDA-ACTCP-P-A-DT     PIC 9(08).          \n020974             15  TDB-TDA-ACTCP-N-A-DT-X.                          \n020976                 20  TDB-TDA-ACTCP-N-A-DT     PIC 9(08).          \n020978             15  TDB-TDA-ACTCP-P-DT-X.                            \n020980                 20  TDB-TDA-ACTCP-P-DT       PIC 9(08).          \n020982             15  TDB-TDA-ACTCP-N-DT-X.                            \n020984                 20  TDB-TDA-ACTCP-N-DT       PIC 9(08).          \n020986             15  TDB-TDA-ACTCP-BAL-X.                             \n020988                 20  TDB-TDA-ACTCP-BAL        PIC S9(12)V99.      \n020990             15  FILLER                       PIC X(254).         \n020992                                                                  \n020994         10  TDB-TDA-ACTS-STATEMENT REDEFINES                     \n020996                 TDB-TDA-ACTV-DATA.                               \n020998             15  TDB-TDA-ACTS-F-N-DT-X.                           \n021000                 20  TDB-TDA-ACTS-F-N-DT      PIC 9(08).          \n021002             15  TDB-TDA-ACTS-T-N-DT-X.                           \n021004                 20  TDB-TDA-ACTS-T-N-DT      PIC 9(08).          \n021006             15  TDB-TDA-ACTS-F-L-DT-X.                           \n021008                 20  TDB-TDA-ACTS-F-L-DT      PIC 9(08).          \n021010             15  TDB-TDA-ACTS-T-L-DT-X.                           \n021012                 20  TDB-TDA-ACTS-T-L-DT      PIC 9(08).          \n021014             15  TDB-TDA-ACTS-F-STD-X.                            \n021016                 20  TDB-TDA-ACTS-F-STD       PIC S9(12)V99.      \n021018             15  TDB-TDA-ACTS-T-STD-X.                            \n021020                 20  TDB-TDA-ACTS-T-STD       PIC S9(12)V99.      \n021022             15  FILLER                       PIC X(340).         \n021024                                                                  \n021026         10  TDB-TDA-ACTDB-CMAT  REDEFINES                        \n021028                 TDB-TDA-ACTV-DATA.                               \n021030             15  TDB-TDA-ACTDB-SERIAL-X.                          \n021032                 20  TDB-TDA-ACTDB-SERIAL     PIC 9(12).          \n021034             15  TDB-TDA-ACTDB-ACCR-INT-X.                        \n021036                 20  TDB-TDA-ACTDB-ACCR-INT   PIC S9(12)V9(6).    \n021038             15  TDB-TDA-ACTDB-CMPD-INT-X.                        \n021040                 20  TDB-TDA-ACTDB-CMPD-INT   PIC S9(6)V9(4).     \n021042             15  TDB-TDA-ACTDB-CURR-BAL-X.                        \n021044                 20  TDB-TDA-ACTDB-CURR-BAL   PIC S9(12)V99.      \n021046             15  TDB-TDA-ACTDB-PER-DIEM-X.                        \n021048                 20  TDB-TDA-ACTDB-PER-DIEM   PIC S9(12)V9(6).    \n021050             15  TDB-TDA-ACTDB-ANTC-INT-X.                        \n021052                 20  TDB-TDA-ACTDB-ANTC-INT   PIC S9(12)V99.      \n021054             15  TDB-TDA-ACTDB-ACCR-DT-X.                         \n021056                 20  TDB-TDA-ACTDB-ACCR-DT    PIC 9(8).           \n021058             15  FILLER                       PIC X(306).         \n021060                                                                  \n021062         10  TDB-TDA-ACTDE-HSA  REDEFINES                         \n021064                 TDB-TDA-ACTV-DATA.                               \n021066             15  TDB-TDA-ACTDE-DESCR          PIC X(80).          \n021068             15  TDB-TDA-ACTDE-DESCR-R                            \n021070                 REDEFINES TDB-TDA-ACTDE-DESCR.                   \n021072                 20  TDB-TDA-ACTDE-DESCR-1      PIC X(40).        \n021074                 20  TDB-TDA-ACTDE-DESCR-2      PIC X(40).        \n021076             15  FILLER                       PIC X(320).         \n021078                                                                  \n021080         10  TDB-TDA-ACTD-DIST-STATUS REDEFINES                   \n021082                 TDB-TDA-ACTV-DATA.                               \n021084             15  TDB-TDA-ACTD-FUNCTION        PIC 9(1).           \n021086             15  TDB-TDA-ACTD-AMT-CD          PIC 9(1).           \n021088             15  TDB-TDA-ACTD-DS-NBR          PIC 9(3).           \n021090             15  TDB-TDA-ACTD-DS-TYPE         PIC X(2).           \n021092             15  TDB-TDA-ACTD-AMT             PIC S9(12)V9(2).    \n021094             15  TDB-TDA-ACTD-NXT-DATE        PIC 9(8).           \n021096             15  FILLER                       PIC X(371).         \n021098                                                                  \n021100         10  TDB-TDA-ACTDI-DS-IN-PROC REDEFINES                   \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    273 lines from 10274 to 10546.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 21, "total_chunks": 55, "start_line": 10274, "end_line": 10546, "line_count": 273}

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
- Source code length: 24889 characters

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
CHUNK 21 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 10274 to 10546 (273 lines)
Chunk Tokens (estimated): ~5,865
Actual Input Tokens: 7,271 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 10274-10546 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 21 of 55 chunks
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
      The source code below is only CHUNK 21 of 55.


=============================================================================
CHUNK 21 SOURCE CODE (Lines 10274-10546)
=============================================================================

```cobol
020556                 TDB-TDA-ACTV-DATA.                               
020558             15  TDB-TDA-ACTVI-F-INT-X.                           
020560                 20  TDB-TDA-ACTVI-F-INT      PIC S9(12)V9(6).    
020562             15  TDB-TDA-ACTVI-T-INT-X.                           
020564                 20  TDB-TDA-ACTVI-T-INT      PIC S9(12)V9(6).    
020566             15  TDB-TDA-ACTVI-F-INTA-X.                          
020568                 20  TDB-TDA-ACTVI-F-INTA     PIC S9(12)V99.      
020570             15  TDB-TDA-ACTVI-T-INTA-X.                          
020572                 20  TDB-TDA-ACTVI-T-INTA     PIC S9(12)V99.      
020574             15  TDB-TDA-ACTVI-F-PDAY-X.                          
020576                 20  TDB-TDA-ACTVI-F-PDAY     PIC S9(12)V9(6).    
020578             15  TDB-TDA-ACTVI-T-PDAY-X.                          
020580                 20  TDB-TDA-ACTVI-T-PDAY     PIC S9(12)V9(6).    
020582             15  TDB-TDA-ACTVI-RD-DT-X.                           
020584                 20  TDB-TDA-ACTVI-RD-DT      PIC 9(08).          
020586             15  FILLER                       PIC X(292).         
020588                                                                  
020590         10  TDB-TDA-ACTCK-CHECK    REDEFINES                     
020592                 TDB-TDA-ACTV-DATA.                               
020594             15  TDB-TDA-ACTCK-F-I-PT-X.                          
020596                 20  TDB-TDA-ACTCK-F-I-PT      PIC S9(12)V99.     
020598             15  TDB-TDA-ACTCK-T-I-PT-X.                          
020600                 20  TDB-TDA-ACTCK-T-I-PT      PIC S9(12)V99.     
020602             15  TDB-TDA-ACTCK-F-C-WA-X.                          
020604                 20  TDB-TDA-ACTCK-F-C-WA      PIC S9(12)V99.     
020606             15  TDB-TDA-ACTCK-T-C-WA-X.                          
020608                 20  TDB-TDA-ACTCK-T-C-WA      PIC S9(12)V99.     
020610             15  TDB-TDA-ACTCK-F-STAT-X.                          
020612                 20  TDB-TDA-ACTCK-F-STAT      PIC X.             
020614             15  TDB-TDA-ACTCK-T-STAT-X.                          
020616                 20  TDB-TDA-ACTCK-T-STAT      PIC X.             
020618             15  TDB-TDA-ACTCK-PRS-DT-X.                          
020620                 20  TDB-TDA-ACTCK-PRS-DT      PIC 9(08).         
020622             15  TDB-TDA-ACTCK-F-ST-WA-X.                         
020624                 20  TDB-TDA-ACTCK-F-ST-WA     PIC S9(12)V99.     
020626             15  TDB-TDA-ACTCK-T-ST-WA-X.                         
020628                 20  TDB-TDA-ACTCK-T-ST-WA     PIC S9(12)V99.     
020630             15  FILLER                        PIC X(306).        
020632                                                                  
020634         10  TDB-TDA-ACTWH-WITHHOLD REDEFINES                     
020636                 TDB-TDA-ACTV-DATA.                               
020638             15  TDB-TDA-ACTWH-F-YTD-X.                           
020640                 20  TDB-TDA-ACTWH-F-YTD       PIC S9(12)V99.     
020642             15  TDB-TDA-ACTWH-T-YTD-X.                           
020644                 20  TDB-TDA-ACTWH-T-YTD       PIC S9(12)V99.     
020646             15  TDB-TDA-ACTWH-F-STD-X.                           
020648                 20  TDB-TDA-ACTWH-F-STD       PIC S9(12)V99.     
020650             15  TDB-TDA-ACTWH-T-STD-X.                           
020652                 20  TDB-TDA-ACTWH-T-STD       PIC S9(12)V99.     
020654             15  TDB-TDA-ACTWH-F-L-AMT-X.                         
020656                 20  TDB-TDA-ACTWH-F-L-AMT     PIC S9(12)V99.     
020658             15  TDB-TDA-ACTWH-T-L-AMT-X.                         
020660                 20  TDB-TDA-ACTWH-T-L-AMT     PIC S9(12)V99.     
020662             15 FILLER                         PIC X(316).        
020664                                                                  
020666         10  TDB-TDA-ACTPT-INT-POST REDEFINES                     
020668                 TDB-TDA-ACTV-DATA.                               
020670             15  TDB-TDA-ACTPT-F-IP-L-X.                          
020672                 20  TDB-TDA-ACTPT-F-IP-L      PIC S9(12)V99.     
020674             15  TDB-TDA-ACTPT-T-IP-L-X.                          
020676                 20  TDB-TDA-ACTPT-T-IP-L      PIC S9(12)V99.     
020678             15  TDB-TDA-ACTPT-F-1099-X.                          
020680                 20  TDB-TDA-ACTPT-F-1099      PIC S9(12)V99.     
020682             15  TDB-TDA-ACTPT-T-1099-X.                          
020684                 20  TDB-TDA-ACTPT-T-1099      PIC S9(12)V99.     
020686             15  TDB-TDA-ACTPT-F-C-BL-X.                          
020688                 20  TDB-TDA-ACTPT-F-C-BL      PIC S9(12)V99.     
020690             15  TDB-TDA-ACTPT-T-C-BL-X.                          
020692                 20  TDB-TDA-ACTPT-T-C-BL      PIC S9(12)V99.     
020694             15  TDB-TDA-ACTPT-F-L-DT-X.                          
020696                 20  TDB-TDA-ACTPT-F-L-DT      PIC 9(08).         
020698             15  TDB-TDA-ACTPT-T-L-DT-X.                          
020700                 20  TDB-TDA-ACTPT-T-L-DT      PIC 9(08).         
020702             15  TDB-TDA-ACTPT-F-N-DT-X.                          
020704                 20  TDB-TDA-ACTPT-F-N-DT      PIC 9(08).         
020706             15  TDB-TDA-ACTPT-T-N-DT-X.                          
020708                 20  TDB-TDA-ACTPT-T-N-DT      PIC 9(08).         
020710             15  TDB-TDA-ACTPT-F-I-PT-X.                          
020712                 20  TDB-TDA-ACTPT-F-I-PT      PIC S9(12)V99.     
020714             15  TDB-TDA-ACTPT-T-I-PT-X.                          
020716                 20  TDB-TDA-ACTPT-T-I-PT      PIC S9(12)V99.     
020718             15  TDB-TDA-ACTPT-F-C-WA-X.                          
020720                 20  TDB-TDA-ACTPT-F-C-WA      PIC S9(12)V99.     
020722             15  TDB-TDA-ACTPT-T-C-WA-X.                          
020724                 20  TDB-TDA-ACTPT-T-C-WA      PIC S9(12)V99.     
020726             15  TDB-TDA-ACTPT-F-ACCR-X.                          
020728                 20  TDB-TDA-ACTPT-F-ACCR      PIC S9(12)V9(06).  
020730             15  TDB-TDA-ACTPT-T-ACCR-X.                          
020732                 20  TDB-TDA-ACTPT-T-ACCR      PIC S9(12)V9(06).  
020734             15  TDB-TDA-ACTPT-F-STAT          PIC X(01).         
020736             15  TDB-TDA-ACTPT-T-STAT          PIC X(01).         
020738             15  TDB-TDA-ACTPT-F-A-DT-X.                          
020740                 20  TDB-TDA-ACTPT-F-A-DT      PIC 9(8).          
020742             15  TDB-TDA-ACTPT-T-A-DT-X.                          
020744                 20  TDB-TDA-ACTPT-T-A-DT      PIC 9(8).          
020746             15  TDB-TDA-ACTPT-F-PDAY-X.                          
020748                 20  TDB-TDA-ACTPT-F-PDAY      PIC S9(12)V9(6).   
020750             15  TDB-TDA-ACTPT-T-PDAY-X.                          
020752                 20  TDB-TDA-ACTPT-T-PDAY      PIC S9(12)V9(6).   
020754             15  TDB-TDA-ACTPT-N-INT-X.                           
020756                 20  TDB-TDA-ACTPT-N-INT       PIC S9(12)V99.     
020758             15  TDB-TDA-ACTPT-C-INT-X.                           
020760                 20  TDB-TDA-ACTPT-C-INT       PIC S9(12)V99.     
020762             15  TDB-TDA-ACTPT-DISP-CD-X.                         
020764                 20  TDB-TDA-ACTPT-DISP-CD     PIC 9(01).         
020766             15  TDB-TDA-ACTPT-INT-ACCT-X.                        
020768                 20  TDB-TDA-ACTPT-INT-ACCT    PIC 9(12).         
020770             15  TDB-TDA-ACTPT-INT-ACCT-S-X.                      
020772                 20  TDB-TDA-ACTPT-INT-ACCT-S  PIC 9(10).         
020774             15  TDB-TDA-ACTPT-F-ST-WA-X.                         
020776                 20  TDB-TDA-ACTPT-F-ST-WA     PIC S9(12)V99.     
020778             15  TDB-TDA-ACTPT-T-ST-WA-X.                         
020780                 20  TDB-TDA-ACTPT-T-ST-WA     PIC S9(12)V99.     
020782             15  TDB-TDA-ACTPT-NEW-BAL-X.                         
020784                 20  TDB-TDA-ACTPT-NEW-BAL     PIC S9(12)V99.     
020786             15  TDB-TDA-ACTPT-CLO-MAT-X.                         
020788                 20  TDB-TDA-ACTPT-CLO-MAT     PIC 9.             
020790             15  FILLER                        PIC X(44).         
020792                                                                  
020794         10  TDB-TDA-ACTAC-CLOSE-ACCT REDEFINES                   
020796                 TDB-TDA-ACTV-DATA.                               
020798             15  TDB-TDA-ACTAC-AMT           PIC S9(12)V9(2).     
020800             15  TDB-TDA-ACTAC-INT           PIC S9(12)V9(2).     
020802             15  TDB-TDA-ACTAC-PENLTY        PIC S9(12)V9(2).     
020804             15  TDB-TDA-ACTAC-WTHLD         PIC S9(12)V9(2).     
020806             15  TDB-TDA-ACTAC-LST-INT       PIC S9(12)V9(2).     
020808             15  TDB-TDA-ACTAC-W-ALLOW       PIC 9(1).            
020810             15  TDB-TDA-ACTAC-D-ALLOW       PIC 9(1).            
020812             15  TDB-TDA-ACTAC-CUR-PEN       PIC S9(12)V9(2).     
020814             15  TDB-TDA-ACTAC-AVL-BAL       PIC S9(12)V9(2).     
020816             15  TDB-TDA-ACTAC-DS-TYPE       PIC X(02).           
020818             15  TDB-TDA-ACTAC-ST-WHLD       PIC S9(12)V99.       
020820             15  TDB-TDA-ACTAC-DRP-INT       PIC S9(12)V99.       
020822             15  TDB-TDA-ACTAC-DS-DISP       PIC 9.               
020824             15  TDB-TDA-ACTAC-CLO-MAT       PIC 9.               
020826             15  TDB-TDA-ACTAC-T-ACCT        PIC 9(12).           
020828             15  TDB-TDA-ACTAC-T-ACCTS       PIC 9(10).           
020830             15  TDB-TDA-ACTAC-DS-CODE       PIC 9(1).            
020832             15  TDB-TDA-ACTAC-DS-NBR        PIC 9(2).            
020834             15  TDB-TDA-ACTAC-DESC          PIC X(30).           
020836             15  FILLER                      PIC X(213).          
020838                                                                  
020840         10  TDB-TDA-ACTDS-DISTRIBUTE REDEFINES                   
020842                 TDB-TDA-ACTV-DATA.                               
020844             15  TDB-TDA-ACTDS-TYPE          PIC XX.              
020846             15  TDB-TDA-ACTDS-DISP-CD-X.                         
020848                 20  TDB-TDA-ACTDS-DISP-CD   PIC 9(01).           
020850             15  TDB-TDA-ACTDS-INT-X.                             
020852                 20  TDB-TDA-ACTDS-INT       PIC 9(01).           
020854             15  TDB-TDA-ACTDS-PRNCPAL-X.                         
020856                 20  TDB-TDA-ACTDS-PRNCPAL   PIC 9(01).           
020858             15  TDB-TDA-ACTDS-CD-X.                              
020860                 20  TDB-TDA-ACTDS-CD        PIC 9(01).           
020862             15  TDB-TDA-ACTDS-NXT-DT-X.                          
020864                 20  TDB-TDA-ACTDS-NXT-DT    PIC 9(08).           
020866             15  TDB-TDA-ACTDS-W-AMT-X.                           
020868                 20  TDB-TDA-ACTDS-W-AMT     PIC S9(12)V99.       
020870             15  TDB-TDA-ACTDS-W-CD-X.                            
020872                 20  TDB-TDA-ACTDS-W-CD      PIC 9(01).           
020874             15  TDB-TDA-ACTDS-AMT-X.                             
020876                 20  TDB-TDA-ACTDS-AMT       PIC S9(12)V99.       
020878             15  TDB-TDA-ACTDS-FREQ-X.                            
020880                 20  TDB-TDA-ACTDS-FREQ      PIC 9(01).           
020882             15  TDB-TDA-ACTDS-NTRVL-X.                           
020884                 20  TDB-TDA-ACTDS-NTRVL     PIC 9(04).           
020886             15  TDB-TDA-ACTDS-T-ACCT-X.                          
020888                 20  TDB-TDA-ACTDS-T-ACCT    PIC 9(12).           
020890             15  TDB-TDA-ACTDS-T-ACCTS-X.                         
020892                 20  TDB-TDA-ACTDS-T-ACCTS   PIC 9(10).           
020894             15  TDB-TDA-ACTDS-ST-WAMT-X.                         
020896                 20  TDB-TDA-ACTDS-ST-WAMT   PIC S9(12)V99.       
020898             15  TDB-TDA-ACTDS-ST-W-CD-X.                         
020900                 20  TDB-TDA-ACTDS-ST-W-CD   PIC 9(01).           
020902             15  TDB-TDA-ACTDS-NEW-BAL-X.                         
020904                 20  TDB-TDA-ACTDS-NEW-BAL   PIC S9(12)V99.       
020906             15  TDB-TDA-ACTDS-DS-NBR-X.                          
020908                 20  TDB-TDA-ACTDS-DS-NBR    PIC 9(2).            
020910             15  FILLER                      PIC X(299).          
020912                                                                  
020914         10  TDB-TDA-ACTE-ERASER REDEFINES                        
020916                 TDB-TDA-ACTV-DATA.                               
020918             15  TDB-TDA-ACTE-SERIAL-X.                           
020920                 20  TDB-TDA-ACTE-SERIAL     PIC 9(12).           
020922             15  TDB-TDA-ACTE-TYPE-X.                             
020924                 20  TDB-TDA-ACTE-TYPE       PIC 9(02).           
020926             15  TDB-TDA-ACTE-EFF-DT-X.                           
020928                 20  TDB-TDA-ACTE-EFF-DT     PIC 9(08).           
020930             15  TDB-TDA-ACTE-DATE-X.                             
020932                 20  TDB-TDA-ACTE-DATE       PIC 9(08).           
020934             15  TDB-TDA-ACTE-SEQ-NBR-X.                          
020936                 20  TDB-TDA-ACTE-SEQ-NBR    PIC 9(02).           
020938             15  FILLER                      PIC X(368).          
020940                                                                  
020942         10  TDB-TDA-ACTCP-COMPOUND REDEFINES                     
020944                 TDB-TDA-ACTV-DATA.                               
020946             15  TDB-TDA-ACTCP-P-INT-X.                           
020948                 20  TDB-TDA-ACTCP-P-INT      PIC S9(12)V9(6).    
020950             15  TDB-TDA-ACTCP-N-INT-X.                           
020952                 20  TDB-TDA-ACTCP-N-INT      PIC S9(12)V9(6).    
020954             15  TDB-TDA-ACTCP-P-PDAY-X.                          
020956                 20  TDB-TDA-ACTCP-P-PDAY     PIC S9(12)V9(6).    
020958             15  TDB-TDA-ACTCP-N-PDAY-X.                          
020960                 20  TDB-TDA-ACTCP-N-PDAY     PIC S9(12)V9(6).    
020962             15  TDB-TDA-ACTCP-P-INTA-X.                          
020964                 20  TDB-TDA-ACTCP-P-INTA     PIC S9(12)V9(2).    
020966             15  TDB-TDA-ACTCP-N-INTA-X.                          
020968                 20  TDB-TDA-ACTCP-N-INTA     PIC S9(12)V9(2).    
020970             15  TDB-TDA-ACTCP-P-A-DT-X.                          
020972                 20  TDB-TDA-ACTCP-P-A-DT     PIC 9(08).          
020974             15  TDB-TDA-ACTCP-N-A-DT-X.                          
020976                 20  TDB-TDA-ACTCP-N-A-DT     PIC 9(08).          
020978             15  TDB-TDA-ACTCP-P-DT-X.                            
020980                 20  TDB-TDA-ACTCP-P-DT       PIC 9(08).          
020982             15  TDB-TDA-ACTCP-N-DT-X.                            
020984                 20  TDB-TDA-ACTCP-N-DT       PIC 9(08).          
020986             15  TDB-TDA-ACTCP-BAL-X.                             
020988                 20  TDB-TDA-ACTCP-BAL        PIC S9(12)V99.      
020990             15  FILLER                       PIC X(254).         
020992                                                                  
020994         10  TDB-TDA-ACTS-STATEMENT REDEFINES                     
020996                 TDB-TDA-ACTV-DATA.                               
020998             15  TDB-TDA-ACTS-F-N-DT-X.                           
021000                 20  TDB-TDA-ACTS-F-N-DT      PIC 9(08).          
021002             15  TDB-TDA-ACTS-T-N-DT-X.                           
021004                 20  TDB-TDA-ACTS-T-N-DT      PIC 9(08).          
021006             15  TDB-TDA-ACTS-F-L-DT-X.                           
021008                 20  TDB-TDA-ACTS-F-L-DT      PIC 9(08).          
021010             15  TDB-TDA-ACTS-T-L-DT-X.                           
021012                 20  TDB-TDA-ACTS-T-L-DT      PIC 9(08).          
021014             15  TDB-TDA-ACTS-F-STD-X.                            
021016                 20  TDB-TDA-ACTS-F-STD       PIC S9(12)V99.      
021018             15  TDB-TDA-ACTS-T-STD-X.                            
021020                 20  TDB-TDA-ACTS-T-STD       PIC S9(12)V99.      
021022             15  FILLER                       PIC X(340).         
021024                                                                  
021026         10  TDB-TDA-ACTDB-CMAT  REDEFINES                        
021028                 TDB-TDA-ACTV-DATA.                               
021030             15  TDB-TDA-ACTDB-SERIAL-X.                          
021032                 20  TDB-TDA-ACTDB-SERIAL     PIC 9(12).          
021034             15  TDB-TDA-ACTDB-ACCR-INT-X.                        
021036                 20  TDB-TDA-ACTDB-ACCR-INT   PIC S9(12)V9(6).    
021038             15  TDB-TDA-ACTDB-CMPD-INT-X.                        
021040                 20  TDB-TDA-ACTDB-CMPD-INT   PIC S9(6)V9(4).     
021042             15  TDB-TDA-ACTDB-CURR-BAL-X.                        
021044                 20  TDB-TDA-ACTDB-CURR-BAL   PIC S9(12)V99.      
021046             15  TDB-TDA-ACTDB-PER-DIEM-X.                        
021048                 20  TDB-TDA-ACTDB-PER-DIEM   PIC S9(12)V9(6).    
021050             15  TDB-TDA-ACTDB-ANTC-INT-X.                        
021052                 20  TDB-TDA-ACTDB-ANTC-INT   PIC S9(12)V99.      
021054             15  TDB-TDA-ACTDB-ACCR-DT-X.                         
021056                 20  TDB-TDA-ACTDB-ACCR-DT    PIC 9(8).           
021058             15  FILLER                       PIC X(306).         
021060                                                                  
021062         10  TDB-TDA-ACTDE-HSA  REDEFINES                         
021064                 TDB-TDA-ACTV-DATA.                               
021066             15  TDB-TDA-ACTDE-DESCR          PIC X(80).          
021068             15  TDB-TDA-ACTDE-DESCR-R                            
021070                 REDEFINES TDB-TDA-ACTDE-DESCR.                   
021072                 20  TDB-TDA-ACTDE-DESCR-1      PIC X(40).        
021074                 20  TDB-TDA-ACTDE-DESCR-2      PIC X(40).        
021076             15  FILLER                       PIC X(320).         
021078                                                                  
021080         10  TDB-TDA-ACTD-DIST-STATUS REDEFINES                   
021082                 TDB-TDA-ACTV-DATA.                               
021084             15  TDB-TDA-ACTD-FUNCTION        PIC 9(1).           
021086             15  TDB-TDA-ACTD-AMT-CD          PIC 9(1).           
021088             15  TDB-TDA-ACTD-DS-NBR          PIC 9(3).           
021090             15  TDB-TDA-ACTD-DS-TYPE         PIC X(2).           
021092             15  TDB-TDA-ACTD-AMT             PIC S9(12)V9(2).    
021094             15  TDB-TDA-ACTD-NXT-DATE        PIC 9(8).           
021096             15  FILLER                       PIC X(371).         
021098                                                                  
021100         10  TDB-TDA-ACTDI-DS-IN-PROC REDEFINES                   
```

⚠️  This is the source code you must document.
    273 lines from 10274 to 10546.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

