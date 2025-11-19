# LLM Request Debug File
Generated: 2025-11-17T20:30:05.632447

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 15/55
- **Model**: gpt-4.1
- **Chunk Number**: 15
- **Pass Number**: 3
- **Attempt Number**: 3 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~6,534 tokens
- **Total Input**: ~8,492 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 15/55" (ID: detailed-code-explanation)

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


**CHUNK 15 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-17T19:50:50.832678", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 15 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 6847 to 7096 (250 lines)\nChunk Tokens (estimated): ~6,162\nActual Input Tokens: 7,568 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 6847-7096 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 15 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 15 of 55.\n\n\n=============================================================================\nCHUNK 15 SOURCE CODE (Lines 6847-7096)\n=============================================================================\n\n```cobol\n013702                    HOLD-TDAA-INTERNET-CD-R.                      \n013704                 20  HOLD-TDAA-INTERNET-BPY   PIC 9(1).           \n013706                 20  HOLD-TDAA-INTERNET-TFR   PIC 9(1).           \n013708                 20  HOLD-TDAA-INTERNET-INQ   PIC 9(1).           \n013710             15  HOLD-TDAA-IRA-BACKED     PIC 9(1).               \n013712             15  HOLD-TDAA-SAV-DEPOSIT    PIC 9(1).               \n013714             15  HOLD-TDAA-MAT-TYPE       PIC 9(1).               \n013716             15  HOLD-TDAA-MAT-TERM       PIC 9(4).               \n013718             15  HOLD-TDAA-ORG-MAT-TYPE   PIC 9(1).               \n013720             15  HOLD-TDAA-ORG-MAT-TERM   PIC 9(4).               \n013722             15  HOLD-TDAA-ODD-PAYMENT    PIC 9(1).               \n013724             15  HOLD-TDAA-PAY-FREQ       PIC 9(1).               \n013726             15  HOLD-TDAA-PAY-NTRVL      PIC 9(4).               \n013728             15  HOLD-TDAA-FEE-FREQ       PIC 9(1).               \n013730             15  HOLD-TDAA-FEE-NTRVL      PIC 9(4).               \n013732             15  HOLD-TDAA-STMT-FREQ      PIC 9(1).               \n013734             15  HOLD-TDAA-STMT-NTRVL     PIC 9(4).               \n013736             15  HOLD-TDAA-EMPLOYEE-ID    PIC X(8).               \n013738             15  HOLD-TDAA-EFT-CARD       PIC X(01).              \n013740             15  HOLD-TDAA-PEN-WAV-RESN   PIC X(01).              \n013742             15  HOLD-TDAA-CLOSED-RESN    PIC X(01).              \n013744             15  HOLD-TDAA-SPECIAL-STMT   PIC 9(01).              \n013746             15  HOLD-TDAA-CLS-THIS-MTH   PIC 9(01).              \n013748             15  HOLD-TDAA-RC-MAT-ONLY    PIC 9(1).               \n013750             15  HOLD-TDAA-GRACE-DAYS     PIC 9(2).               \n013752             15  HOLD-TDAA-CLS-ON-MAT     PIC 9(1).               \n013754                                                                  \n013756         10  HOLD-TDAA-G-ACCT-NBR.                                \n013758             15  HOLD-TDAA-DDA-ACCT-1     PIC 9(12).              \n013760             15  HOLD-TDAA-DDA-ACCT-1-S   PIC 9(10).              \n013762             15  HOLD-TDAA-DDA-ACCT-2     PIC 9(12).              \n013764             15  HOLD-TDAA-DDA-ACCT-2-S   PIC 9(10).              \n013766             15  HOLD-TDAA-DDA-ACCT-3     PIC 9(12).              \n013768             15  HOLD-TDAA-DDA-ACCT-3-S   PIC 9(10).              \n013770             15  HOLD-TDAA-INT-ACCT       PIC 9(12).              \n013772             15  HOLD-TDAA-INT-ACCT-S     PIC 9(10).              \n013774             15  HOLD-TDAA-CS-ACCT        PIC 9(12).              \n013776             15  HOLD-TDAA-CS-ACCT-S      PIC 9(10).              \n013778             15  HOLD-TDAA-CC-ACCT        PIC 9(12).              \n013780             15  HOLD-TDAA-LNS-BORROWER   PIC 9(12).              \n013782             15  HOLD-TDAA-LNS-NOTE       PIC 9(10).              \n013784             15  HOLD-TDAA-CNV-OLD-ACCT   PIC X(15).              \n013786             15  HOLD-TDAA-CLS-ACCT       PIC 9(12).              \n013788             15  HOLD-TDAA-CLS-ACCT-S     PIC 9(10).              \n013790         10  HOLD-TDAA-G-CNTR.                                    \n013792             15  HOLD-TDAA-DAYS-IN-PER    PIC 9(5).               \n013794             15  HOLD-TDAA-RR-CYC-NBR     PIC 9(2).               \n013796             15  HOLD-TDAA-CR-CNT-STD     PIC 9(5).               \n013798             15  HOLD-TDAA-CR-AMT-STD     PIC S9(12)V9(2).        \n013800             15  HOLD-TDAA-DB-CNT-STD     PIC 9(5).               \n013802             15  HOLD-TDAA-DB-AMT-STD     PIC S9(12)V9(2).        \n013804             15  HOLD-TDAA-CR-CNT-YTD     PIC 9(5).               \n013806             15  HOLD-TDAA-CR-AMT-YTD     PIC S9(12)V9(2).        \n013808             15  HOLD-TDAA-DB-CNT-YTD     PIC 9(5).               \n013810             15  HOLD-TDAA-DB-AMT-YTD     PIC S9(12)V9(2).        \n013812             15  HOLD-TDAA-DAYS-IN-TERM   PIC 9(5).               \n013814         10  HOLD-TDAA-G-AMT.                                     \n013816             15  HOLD-TDAA-BEG-INT-BAL    PIC S9(12)V9(2).        \n013818             15  HOLD-TDAA-PURCH-AMT      PIC S9(12)V9(2).        \n013820             15  HOLD-TDAA-CURR-BAL       PIC S9(12)V9(2).        \n013822             15  HOLD-TDAA-AVAIL-BAL      PIC S9(12)V9(2).        \n013824             15  HOLD-TDAA-BAL-BEG-MAT    PIC S9(12)V9(2).        \n013826             15  HOLD-TDAA-CLOSE-AMT      PIC S9(12)V9(2).        \n013828             15  HOLD-TDAA-MONEY-AMT      PIC S9(12)V9(2).        \n013830             15  HOLD-TDAA-BAL-BEG-STMT   PIC S9(12)V9(2).        \n013832             15  HOLD-TDAA-ACCR-INT       PIC S9(12)V9(6).        \n013834             15  HOLD-TDAA-ANTIC-INT      PIC S9(12)V9(2).        \n013836             15  HOLD-TDAA-INT-TO-POST    PIC S9(12)V9(2).        \n013838             15  HOLD-TDAA-1099-YTD       PIC S9(12)V9(2).        \n013840             15  HOLD-TDAA-1099-LST-YR    PIC S9(12)V9(2).        \n013842             15  HOLD-TDAA-CURR-PENLTY    PIC S9(12)V9(2).        \n013844             15  HOLD-TDAA-PENLTY-STD     PIC S9(12)V9(2).        \n013846             15  HOLD-TDAA-PENLTY-YTD     PIC S9(12)V9(2).        \n013848             15  HOLD-TDAA-LST-PENLTY     PIC S9(12)V9(2).        \n013850             15  HOLD-TDAA-CURR-INT-ADJ   PIC S9(12)V9(2).        \n013852             15  HOLD-TDAA-TOTAMT-HOLDS   PIC S9(12)V9(2).        \n013854             15  HOLD-TDAA-NXT-INT-ADJ    PIC S9(12)V9(2).        \n013856             15  HOLD-TDAA-FEE-AMT        PIC S9(12)V9(2).        \n013858             15  HOLD-TDAA-OID-RPT-INT    PIC S9(12)V9(2).        \n013860             15  HOLD-TDAA-FAIR-MRKT      PIC S9(12)V9(2).        \n013862             15  HOLD-TDAA-CUR-WHLD-AMT   PIC S9(12)V9(2).        \n013864             15  HOLD-TDAA-LST-WHLD-AMT   PIC S9(12)V9(2).        \n013866             15  HOLD-TDAA-WTHLD-STD      PIC S9(12)V9(2).        \n013868             15  HOLD-TDAA-WTHLD-YTD      PIC S9(12)V9(2).        \n013870             15  HOLD-TDAA-LST-INT-PMT    PIC S9(12)V9(2).        \n013872             15  HOLD-TDAA-BAL-BEG-YR     PIC S9(12)V9(2).        \n013874             15  HOLD-TDAA-BAL-AT-CONV    PIC S9(12)V9(2).        \n013876             15  HOLD-TDAA-BAL-BEG-LYR    PIC S9(12)V9(2).        \n013878             15  HOLD-TDAA-MIN-BAL-STD    PIC S9(12)V9(2).        \n013880             15  HOLD-TDAA-MIN-BAL-YTD    PIC S9(12)V9(2).        \n013882             15  HOLD-TDAA-MAX-BAL-YTD    PIC S9(12)V9(2).        \n013884             15  HOLD-TDAA-LMINBAL-STD    PIC S9(12)V9(2).        \n013886             15  HOLD-TDAA-CMPD-INT       PIC S9(12)V9(2).        \n013888             15  HOLD-TDAA-PER-DIEM       PIC S9(12)V9(6).        \n013890             15  HOLD-TDAA-AVG-PER-DIEM   PIC S9(12)V9(6).        \n013892             15  HOLD-TDAA-EMAIL-MAXAMT   PIC 9(10).              \n013894             15  HOLD-TDAA-EMAIL-MINAMT   PIC 9(10).              \n013896             15  HOLD-TDAA-DTH-FAIRMKT    PIC S9(12)V9(2).        \n013898             15  HOLD-TDAA-PENLTY-WAIVE   PIC S9(12)V9(2).        \n013900         10  HOLD-TDAA-G-RATES.                                   \n013902             15  HOLD-TDAA-BEG-INT-RT     PIC 9(2)V9(3).          \n013904             15  HOLD-TDAA-CUR-INT-RT     PIC 9(2)V9(3).          \n013906             15  HOLD-TDAA-FLOOR-RT       PIC 9(2)V9(3).          \n013908             15  HOLD-TDAA-FLOOR-INCR     PIC 9(2)V9(3).          \n013910             15  HOLD-TDAA-YIELD-RT       PIC 9(2)V9(3).          \n013912             15  HOLD-TDAA-RISE-RATE      PIC 9(2)V9(3)           \n013914                               OCCURS 10.                         \n013916             15  HOLD-TDAA-LNS-INCRMNT    PIC 9(2)V9(4).          \n013918             15  HOLD-TDAA-RT-VARIANCE    PIC S9(1)V9(2).         \n013920             15  HOLD-TDAA-CONST-RT-ADJ   PIC S9(2)V9(3).         \n013922             15  HOLD-TDAA-RATE-AT-EOY    PIC 9(2)V9(3).          \n013924             15  HOLD-TDAA-RATE-LST-STM   PIC 9(2)V9(3).          \n013926             15  HOLD-TDAA-ORG-YIELD-RT   PIC 9(2)V9(3).          \n013928             15  HOLD-TDAA-REN-YIELD-RT   PIC 9(2)V9(3).          \n013930         10  HOLD-TDAA-G-DATES.                                   \n013932             15  HOLD-TDAA-SCHED-DT       PIC 9(8).               \n013934             15  HOLD-TDAA-ACCR-DT        PIC 9(8).               \n013936             15  HOLD-TDAA-OPEN-DT        PIC 9(8).               \n013938             15  HOLD-TDAA-CLSD-DT        PIC 9(8).               \n013940             15  HOLD-TDAA-LST-MAT-DT     PIC 9(8).               \n013942             15  HOLD-TDAA-LST-POST-DT    PIC 9(8).               \n013944             15  HOLD-TDAA-LST-IN-PROC    PIC 9(8).               \n013946             15  HOLD-TDAA-LST-CONTACT    PIC 9(8).               \n013948             15  HOLD-TDAA-LST-FEE-DT     PIC 9(8).               \n013950             15  HOLD-TDAA-LST-RTCHG-DT   PIC 9(8).               \n013952             15  HOLD-TDAA-LST-DIST-DT    PIC 9(8).               \n013954             15  HOLD-TDAA-LST-STMT-DT    PIC 9(8).               \n013956             15  HOLD-TDAA-LST-CMPD-DT    PIC 9(8).               \n013958             15  HOLD-TDAA-RR-CYC-DT      PIC 9(8)                \n013960                               OCCURS 10.                         \n013962             15  HOLD-TDAA-BNF-BIRTH-DT   PIC 9(8).               \n013964             15  HOLD-TDAA-BNF-DEATH-DT   PIC 9(8).               \n013966             15  HOLD-TDAA-LUPD-DATE      PIC 9(8).               \n013968             15  HOLD-TDAA-LUPD-TIME      PIC 9(6).               \n013970             15  HOLD-TDAA-ADD-DT         PIC 9(8).               \n013972             15  HOLD-TDAA-ADD-TM         PIC 9(6).               \n013974             15  HOLD-TDAA-CONV-DT        PIC 9(8).               \n013976             15  HOLD-TDAA-ACT-CLOSE-DT   PIC 9(8).               \n013978             15  HOLD-TDAA-LST-TBACT-DT   PIC 9(8).               \n013980             15  HOLD-TDAA-ALERT-EXP-DT   PIC 9(8).               \n013982             15  HOLD-TDAA-ALRT2-EXP-DT   PIC 9(8).               \n013984             15  HOLD-TDAA-ALRT3-EXP-DT   PIC 9(8).               \n013986             15  HOLD-TDAA-NXT-FEE-DT     PIC 9(8).               \n013988             15  HOLD-TDAA-NXT-POST-DT    PIC 9(8).               \n013990             15  HOLD-TDAA-NXT-MAT-DT     PIC 9(8).               \n013992             15  HOLD-TDAA-NXT-DIST-DT    PIC 9(8).               \n013994             15  HOLD-TDAA-NXT-RT-CHG     PIC 9(8).               \n013996             15  HOLD-TDAA-NXT-IN-PROC    PIC 9(8).               \n013998             15  HOLD-TDAA-NXT-CMPD-DT    PIC 9(8).               \n014000             15  HOLD-TDAA-NXT-STMT-DT    PIC 9(8).               \n014002             15  HOLD-TDAA-NXT-DS-PROC    PIC 9(8).               \n014004             15  HOLD-TDAA-ADV-NTC-DT     PIC 9(8).               \n014006             15  HOLD-TDAA-NXT-29YR-DT    PIC 9(8).               \n014008             15  HOLD-TDAA-FAIR-MRKT-DT   PIC 9(8).               \n014010             15  HOLD-TDAA-SORT-FIELD-1   PIC X(36).              \n014012             15  HOLD-TDAA-SORT-FIELD-2   PIC X(36).              \n014014             15  HOLD-TDAA-SORT-FIELD-3   PIC X(36).              \n014016             15  HOLD-TDAA-SORT-FIELD-4   PIC X(36).              \n014018         10  HOLD-TDAA-CMAT-PUB-ID        PIC X(8).               \n014020         10  HOLD-TDAA-MSA-CONTR          PIC 9.                  \n014022         10  HOLD-TDAA-MSA-CONTR-LY       PIC 9.                  \n014024         10  HOLD-TDAA-AVG-ACCR-INT       PIC S9(12)V9(6).        \n014026         10  HOLD-TDAA-LEVEL-PAY          PIC 9.                  \n014028         10  HOLD-TDAA-ST-INT-CD          PIC 9.                  \n014030         10  HOLD-TDAA-ST-WHLD-CD         PIC 9.                  \n014032         10  HOLD-TDAA-ST-WHLD-AMT        PIC S9(12)V99.          \n014034         10  HOLD-TDAA-ST-CUR-W-AMT       PIC S9(12)V99.          \n014036         10  HOLD-TDAA-ST-LST-W-AMT       PIC S9(12)V99.          \n014038         10  HOLD-TDAA-ST-WHLD-STD        PIC S9(12)V99.          \n014040         10  HOLD-TDAA-ST-WHLD-YTD        PIC S9(12)V99.          \n014042         10  HOLD-TDAA-CIF-REMARK         PIC X.                  \n014044         10  HOLD-TDAA-CSR                PIC X(3).               \n014046         10  HOLD-TDAA-BSA-O-RSK-CD       PIC 9(1).               \n014048         10  HOLD-TDAA-BSA-C-RSK-CD       PIC 9(1).               \n014050         10  HOLD-TDAA-LRG-TRX-DT         PIC 9(8).               \n014052         10  HOLD-TDAA-HSA-FMLY-IND       PIC 9(01).              \n014054         10  HOLD-TDAA-STOP-PAY-IND       PIC 9(01).              \n014056         10  HOLD-TDAA-IMG-PG-TYPE        PIC X(01).              \n014058         10  HOLD-TDAA-CONT-LMT-CLC       PIC 9(5)V99.            \n014060         10  HOLD-TDAA-CONT-LMT-ENT       PIC 9(5)V99.            \n014062         10  HOLD-TDAA-MEMO-DB            PIC S9(12)V99.          \n014064         10  HOLD-TDAA-MEMO-CR            PIC S9(12)V99.          \n014066         10  HOLD-TDAA-MEMO-DB-2          PIC S9(12)V99.          \n014068         10  HOLD-TDAA-MEMO-CR-2          PIC S9(12)V99.          \n014070         10  HOLD-TDAA-RT-AT-CONV         PIC 9(2)V9(3).          \n014072         10  HOLD-TDAA-ACCR-AT-CONV       PIC S9(12)V9(6).        \n014074         10  HOLD-TDAA-RT-AT-ACRDT        PIC 9(2)V9(3).          \n014076         10  HOLD-TDAA-BAL-AT-ACRDT       PIC S9(12)V9(2).        \n014078         10  HOLD-TDAA-ZERO-RT-ALLOW      PIC 9.                  \n014080         10  HOLD-TDAA-EMAIL-NTC          PIC 9.                  \n014082         10  HOLD-TDAA-EMAIL-STMT         PIC 9.                  \n014084         10  HOLD-TDAA-FRAUD-CK-DT        PIC 9(8).               \n014086         10  HOLD-TDAA-FRAUD-CK-CNT       PIC 9(3).               \n014088         10  HOLD-TDAA-FRAUD-CK-AMT       PIC S9(12)V9(2).        \n014090         10  HOLD-TDAA-MISC-ACCTNO        PIC 9(8).               \n014092         10  HOLD-TDAA-RMD-MAN-CALC       PIC 9(1).               \n014094         10  HOLD-TDAA-RMD-AMOUNT         PIC S9(12)V9(2).        \n014096         10  HOLD-TDAA-BROKERAGE-ID       PIC X(10).              \n014098         10  HOLD-TDAA-MONY-SRC-CD2       PIC X(03).              \n014100         10  HOLD-TDAA-INHERIT-IRA        PIC 9(01).              \n014102         10  HOLD-TDAA-LIFE-FACTOR        PIC 9(02)V9(1).         \n014104         10  HOLD-TDAA-EV-LARGE-TRX       PIC X(01).              \n014106         10  HOLD-TDAA-EV-MAT-AMT         PIC S9(12)V9(2).        \n014108         10  HOLD-TDAA-EV-DISP-ACCT       PIC 9(22).              \n014110         10  HOLD-TDAA-EV-COMP-ACCT       PIC 9(22).              \n014112         10  HOLD-TDAA-EV-PUBLIC-ID       PIC X(08).              \n014114         10  HOLD-TDAA-EV-MAT-TYPE        PIC X(01).              \n014116         10  HOLD-TDAA-EV-INT-TYPE        PIC X(01).              \n014118         10  HOLD-TDAA-EV-ACCT-TYP        PIC X(01).              \n014120         10  HOLD-TDAA-EV-WHLD-PCT        PIC 9(02).              \n014122         10  HOLD-TDAA-EV-NON-ACCR        PIC X(01).              \n014124         10  HOLD-TDAA-EV-CLOSED          PIC X(01).              \n014126         10  HOLD-TDAA-EV-CLOSE-MO        PIC X(01).              \n014128         10  HOLD-TDAA-EV-OPEN-MO         PIC X(01).              \n014130         10  HOLD-TDAA-EV-ANN-INT         PIC S9(12)V9(2).        \n014132         10  HOLD-TDAA-EV-ORIG-RT         PIC 9(2)V9(3).          \n014134         10  HOLD-TDAA-EV-DLY-INT         PIC S9(12)V9(6).        \n014136         10  HOLD-TDAA-EV-INT-PAY         PIC S9(12)V9(6).        \n014138         10  HOLD-TDAA-EV-AVAIL-BL        PIC S9(12)V9(2).        \n014140         10  HOLD-TDAA-EV-RETAIN          PIC X(01).              \n014142         10  HOLD-TDAA-EV-CL-RETAIN       PIC X(01).              \n014144         10  HOLD-TDAA-EV-TIMES-REN       PIC 9(05).              \n014146         10  HOLD-TDAA-EV-CURR-BAL        PIC S9(12)V9(2).        \n014148         10  HOLD-TDAA-BRKR-DEP-CAT       PIC 9(01).              \n014150         10  HOLD-TDAA-LINE-OF-BUS        PIC 9(4).               \n014152         10  HOLD-TDAA-1ST-STMT           PIC 9(01).              \n014154         10  HOLD-TDAA-POSTAL-CITY        PIC X(40).              \n014156         10  HOLD-TDAA-POSTAL-CNTRY       PIC X(02).              \n014158         10  HOLD-TDAA-CITIZN-CNTRY       PIC X(02).              \n014160         10  HOLD-TDAA-CUSTM-FIELDS       PIC 9(01).              \n014162         10  HOLD-TDAA-AVG-STEP-RT        PIC 9(2)V9(3).          \n014164         10  HOLD-TDAA-MONITOR-INQ        PIC 9(01).              \n014166         10  HOLD-TDAA-IGL-GRP-2          PIC 9(02).              \n014168         10  HOLD-TDAA-AGG-DAYS-QTD       PIC 9(03).              \n014170         10  HOLD-TDAA-AGG-BAL-QTD        PIC S9(15)V9(2).        \n014172         10  HOLD-TDAA-IGL-GRP-3          PIC 9(02).              \n014174         10  HOLD-TDAA-ALT-ADDR-EOY       PIC 9(01).              \n014176         10  HOLD-TDAA-1042S-TAX-ID       PIC X(22).              \n014178         10  HOLD-TDAA-LEC                PIC X(01).              \n014180         10  HOLD-TDAA-BAL-AT-CLOSE       PIC S9(12)V9(2).        \n014182         10  HOLD-TDAA-AVL-CAP-INT        PIC S9(6)V9(2).         \n014184         10  HOLD-TDAA-FIDM-TR-FUND       PIC 9(01).              \n014186         10  HOLD-TDAA-IRS-FRM-DLVR       PIC 9(01).              \n014188         10  HOLD-TDAA-PROVINCE           PIC X(02).              \n014190         10  HOLD-TDAA-PROMOTION          PIC X(25).              \n014192         10  HOLD-EXTRA-FIELDS.                                   \n014194             15  HOLD-TDAA-DAYS-INTO-PER  PIC 9(5).               \n014196             15  HOLD-TDAA-CURR-PAYOFF    PIC S9(9)V9(2).         \n014198             15  HOLD-TDAA-MANUAL-RT-X    PIC X(5).               \n014200             15  HOLD-TDAA-MANUAL-RT-RE   REDEFINES               \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    250 lines from 6847 to 7096.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 15, "total_chunks": 55, "start_line": 6847, "end_line": 7096, "line_count": 250}

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
- Source code length: 23202 characters

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
CHUNK 15 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 6847 to 7096 (250 lines)
Chunk Tokens (estimated): ~6,162
Actual Input Tokens: 7,568 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 6847-7096 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 15 of 55 chunks
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
      The source code below is only CHUNK 15 of 55.


=============================================================================
CHUNK 15 SOURCE CODE (Lines 6847-7096)
=============================================================================

```cobol
013702                    HOLD-TDAA-INTERNET-CD-R.                      
013704                 20  HOLD-TDAA-INTERNET-BPY   PIC 9(1).           
013706                 20  HOLD-TDAA-INTERNET-TFR   PIC 9(1).           
013708                 20  HOLD-TDAA-INTERNET-INQ   PIC 9(1).           
013710             15  HOLD-TDAA-IRA-BACKED     PIC 9(1).               
013712             15  HOLD-TDAA-SAV-DEPOSIT    PIC 9(1).               
013714             15  HOLD-TDAA-MAT-TYPE       PIC 9(1).               
013716             15  HOLD-TDAA-MAT-TERM       PIC 9(4).               
013718             15  HOLD-TDAA-ORG-MAT-TYPE   PIC 9(1).               
013720             15  HOLD-TDAA-ORG-MAT-TERM   PIC 9(4).               
013722             15  HOLD-TDAA-ODD-PAYMENT    PIC 9(1).               
013724             15  HOLD-TDAA-PAY-FREQ       PIC 9(1).               
013726             15  HOLD-TDAA-PAY-NTRVL      PIC 9(4).               
013728             15  HOLD-TDAA-FEE-FREQ       PIC 9(1).               
013730             15  HOLD-TDAA-FEE-NTRVL      PIC 9(4).               
013732             15  HOLD-TDAA-STMT-FREQ      PIC 9(1).               
013734             15  HOLD-TDAA-STMT-NTRVL     PIC 9(4).               
013736             15  HOLD-TDAA-EMPLOYEE-ID    PIC X(8).               
013738             15  HOLD-TDAA-EFT-CARD       PIC X(01).              
013740             15  HOLD-TDAA-PEN-WAV-RESN   PIC X(01).              
013742             15  HOLD-TDAA-CLOSED-RESN    PIC X(01).              
013744             15  HOLD-TDAA-SPECIAL-STMT   PIC 9(01).              
013746             15  HOLD-TDAA-CLS-THIS-MTH   PIC 9(01).              
013748             15  HOLD-TDAA-RC-MAT-ONLY    PIC 9(1).               
013750             15  HOLD-TDAA-GRACE-DAYS     PIC 9(2).               
013752             15  HOLD-TDAA-CLS-ON-MAT     PIC 9(1).               
013754                                                                  
013756         10  HOLD-TDAA-G-ACCT-NBR.                                
013758             15  HOLD-TDAA-DDA-ACCT-1     PIC 9(12).              
013760             15  HOLD-TDAA-DDA-ACCT-1-S   PIC 9(10).              
013762             15  HOLD-TDAA-DDA-ACCT-2     PIC 9(12).              
013764             15  HOLD-TDAA-DDA-ACCT-2-S   PIC 9(10).              
013766             15  HOLD-TDAA-DDA-ACCT-3     PIC 9(12).              
013768             15  HOLD-TDAA-DDA-ACCT-3-S   PIC 9(10).              
013770             15  HOLD-TDAA-INT-ACCT       PIC 9(12).              
013772             15  HOLD-TDAA-INT-ACCT-S     PIC 9(10).              
013774             15  HOLD-TDAA-CS-ACCT        PIC 9(12).              
013776             15  HOLD-TDAA-CS-ACCT-S      PIC 9(10).              
013778             15  HOLD-TDAA-CC-ACCT        PIC 9(12).              
013780             15  HOLD-TDAA-LNS-BORROWER   PIC 9(12).              
013782             15  HOLD-TDAA-LNS-NOTE       PIC 9(10).              
013784             15  HOLD-TDAA-CNV-OLD-ACCT   PIC X(15).              
013786             15  HOLD-TDAA-CLS-ACCT       PIC 9(12).              
013788             15  HOLD-TDAA-CLS-ACCT-S     PIC 9(10).              
013790         10  HOLD-TDAA-G-CNTR.                                    
013792             15  HOLD-TDAA-DAYS-IN-PER    PIC 9(5).               
013794             15  HOLD-TDAA-RR-CYC-NBR     PIC 9(2).               
013796             15  HOLD-TDAA-CR-CNT-STD     PIC 9(5).               
013798             15  HOLD-TDAA-CR-AMT-STD     PIC S9(12)V9(2).        
013800             15  HOLD-TDAA-DB-CNT-STD     PIC 9(5).               
013802             15  HOLD-TDAA-DB-AMT-STD     PIC S9(12)V9(2).        
013804             15  HOLD-TDAA-CR-CNT-YTD     PIC 9(5).               
013806             15  HOLD-TDAA-CR-AMT-YTD     PIC S9(12)V9(2).        
013808             15  HOLD-TDAA-DB-CNT-YTD     PIC 9(5).               
013810             15  HOLD-TDAA-DB-AMT-YTD     PIC S9(12)V9(2).        
013812             15  HOLD-TDAA-DAYS-IN-TERM   PIC 9(5).               
013814         10  HOLD-TDAA-G-AMT.                                     
013816             15  HOLD-TDAA-BEG-INT-BAL    PIC S9(12)V9(2).        
013818             15  HOLD-TDAA-PURCH-AMT      PIC S9(12)V9(2).        
013820             15  HOLD-TDAA-CURR-BAL       PIC S9(12)V9(2).        
013822             15  HOLD-TDAA-AVAIL-BAL      PIC S9(12)V9(2).        
013824             15  HOLD-TDAA-BAL-BEG-MAT    PIC S9(12)V9(2).        
013826             15  HOLD-TDAA-CLOSE-AMT      PIC S9(12)V9(2).        
013828             15  HOLD-TDAA-MONEY-AMT      PIC S9(12)V9(2).        
013830             15  HOLD-TDAA-BAL-BEG-STMT   PIC S9(12)V9(2).        
013832             15  HOLD-TDAA-ACCR-INT       PIC S9(12)V9(6).        
013834             15  HOLD-TDAA-ANTIC-INT      PIC S9(12)V9(2).        
013836             15  HOLD-TDAA-INT-TO-POST    PIC S9(12)V9(2).        
013838             15  HOLD-TDAA-1099-YTD       PIC S9(12)V9(2).        
013840             15  HOLD-TDAA-1099-LST-YR    PIC S9(12)V9(2).        
013842             15  HOLD-TDAA-CURR-PENLTY    PIC S9(12)V9(2).        
013844             15  HOLD-TDAA-PENLTY-STD     PIC S9(12)V9(2).        
013846             15  HOLD-TDAA-PENLTY-YTD     PIC S9(12)V9(2).        
013848             15  HOLD-TDAA-LST-PENLTY     PIC S9(12)V9(2).        
013850             15  HOLD-TDAA-CURR-INT-ADJ   PIC S9(12)V9(2).        
013852             15  HOLD-TDAA-TOTAMT-HOLDS   PIC S9(12)V9(2).        
013854             15  HOLD-TDAA-NXT-INT-ADJ    PIC S9(12)V9(2).        
013856             15  HOLD-TDAA-FEE-AMT        PIC S9(12)V9(2).        
013858             15  HOLD-TDAA-OID-RPT-INT    PIC S9(12)V9(2).        
013860             15  HOLD-TDAA-FAIR-MRKT      PIC S9(12)V9(2).        
013862             15  HOLD-TDAA-CUR-WHLD-AMT   PIC S9(12)V9(2).        
013864             15  HOLD-TDAA-LST-WHLD-AMT   PIC S9(12)V9(2).        
013866             15  HOLD-TDAA-WTHLD-STD      PIC S9(12)V9(2).        
013868             15  HOLD-TDAA-WTHLD-YTD      PIC S9(12)V9(2).        
013870             15  HOLD-TDAA-LST-INT-PMT    PIC S9(12)V9(2).        
013872             15  HOLD-TDAA-BAL-BEG-YR     PIC S9(12)V9(2).        
013874             15  HOLD-TDAA-BAL-AT-CONV    PIC S9(12)V9(2).        
013876             15  HOLD-TDAA-BAL-BEG-LYR    PIC S9(12)V9(2).        
013878             15  HOLD-TDAA-MIN-BAL-STD    PIC S9(12)V9(2).        
013880             15  HOLD-TDAA-MIN-BAL-YTD    PIC S9(12)V9(2).        
013882             15  HOLD-TDAA-MAX-BAL-YTD    PIC S9(12)V9(2).        
013884             15  HOLD-TDAA-LMINBAL-STD    PIC S9(12)V9(2).        
013886             15  HOLD-TDAA-CMPD-INT       PIC S9(12)V9(2).        
013888             15  HOLD-TDAA-PER-DIEM       PIC S9(12)V9(6).        
013890             15  HOLD-TDAA-AVG-PER-DIEM   PIC S9(12)V9(6).        
013892             15  HOLD-TDAA-EMAIL-MAXAMT   PIC 9(10).              
013894             15  HOLD-TDAA-EMAIL-MINAMT   PIC 9(10).              
013896             15  HOLD-TDAA-DTH-FAIRMKT    PIC S9(12)V9(2).        
013898             15  HOLD-TDAA-PENLTY-WAIVE   PIC S9(12)V9(2).        
013900         10  HOLD-TDAA-G-RATES.                                   
013902             15  HOLD-TDAA-BEG-INT-RT     PIC 9(2)V9(3).          
013904             15  HOLD-TDAA-CUR-INT-RT     PIC 9(2)V9(3).          
013906             15  HOLD-TDAA-FLOOR-RT       PIC 9(2)V9(3).          
013908             15  HOLD-TDAA-FLOOR-INCR     PIC 9(2)V9(3).          
013910             15  HOLD-TDAA-YIELD-RT       PIC 9(2)V9(3).          
013912             15  HOLD-TDAA-RISE-RATE      PIC 9(2)V9(3)           
013914                               OCCURS 10.                         
013916             15  HOLD-TDAA-LNS-INCRMNT    PIC 9(2)V9(4).          
013918             15  HOLD-TDAA-RT-VARIANCE    PIC S9(1)V9(2).         
013920             15  HOLD-TDAA-CONST-RT-ADJ   PIC S9(2)V9(3).         
013922             15  HOLD-TDAA-RATE-AT-EOY    PIC 9(2)V9(3).          
013924             15  HOLD-TDAA-RATE-LST-STM   PIC 9(2)V9(3).          
013926             15  HOLD-TDAA-ORG-YIELD-RT   PIC 9(2)V9(3).          
013928             15  HOLD-TDAA-REN-YIELD-RT   PIC 9(2)V9(3).          
013930         10  HOLD-TDAA-G-DATES.                                   
013932             15  HOLD-TDAA-SCHED-DT       PIC 9(8).               
013934             15  HOLD-TDAA-ACCR-DT        PIC 9(8).               
013936             15  HOLD-TDAA-OPEN-DT        PIC 9(8).               
013938             15  HOLD-TDAA-CLSD-DT        PIC 9(8).               
013940             15  HOLD-TDAA-LST-MAT-DT     PIC 9(8).               
013942             15  HOLD-TDAA-LST-POST-DT    PIC 9(8).               
013944             15  HOLD-TDAA-LST-IN-PROC    PIC 9(8).               
013946             15  HOLD-TDAA-LST-CONTACT    PIC 9(8).               
013948             15  HOLD-TDAA-LST-FEE-DT     PIC 9(8).               
013950             15  HOLD-TDAA-LST-RTCHG-DT   PIC 9(8).               
013952             15  HOLD-TDAA-LST-DIST-DT    PIC 9(8).               
013954             15  HOLD-TDAA-LST-STMT-DT    PIC 9(8).               
013956             15  HOLD-TDAA-LST-CMPD-DT    PIC 9(8).               
013958             15  HOLD-TDAA-RR-CYC-DT      PIC 9(8)                
013960                               OCCURS 10.                         
013962             15  HOLD-TDAA-BNF-BIRTH-DT   PIC 9(8).               
013964             15  HOLD-TDAA-BNF-DEATH-DT   PIC 9(8).               
013966             15  HOLD-TDAA-LUPD-DATE      PIC 9(8).               
013968             15  HOLD-TDAA-LUPD-TIME      PIC 9(6).               
013970             15  HOLD-TDAA-ADD-DT         PIC 9(8).               
013972             15  HOLD-TDAA-ADD-TM         PIC 9(6).               
013974             15  HOLD-TDAA-CONV-DT        PIC 9(8).               
013976             15  HOLD-TDAA-ACT-CLOSE-DT   PIC 9(8).               
013978             15  HOLD-TDAA-LST-TBACT-DT   PIC 9(8).               
013980             15  HOLD-TDAA-ALERT-EXP-DT   PIC 9(8).               
013982             15  HOLD-TDAA-ALRT2-EXP-DT   PIC 9(8).               
013984             15  HOLD-TDAA-ALRT3-EXP-DT   PIC 9(8).               
013986             15  HOLD-TDAA-NXT-FEE-DT     PIC 9(8).               
013988             15  HOLD-TDAA-NXT-POST-DT    PIC 9(8).               
013990             15  HOLD-TDAA-NXT-MAT-DT     PIC 9(8).               
013992             15  HOLD-TDAA-NXT-DIST-DT    PIC 9(8).               
013994             15  HOLD-TDAA-NXT-RT-CHG     PIC 9(8).               
013996             15  HOLD-TDAA-NXT-IN-PROC    PIC 9(8).               
013998             15  HOLD-TDAA-NXT-CMPD-DT    PIC 9(8).               
014000             15  HOLD-TDAA-NXT-STMT-DT    PIC 9(8).               
014002             15  HOLD-TDAA-NXT-DS-PROC    PIC 9(8).               
014004             15  HOLD-TDAA-ADV-NTC-DT     PIC 9(8).               
014006             15  HOLD-TDAA-NXT-29YR-DT    PIC 9(8).               
014008             15  HOLD-TDAA-FAIR-MRKT-DT   PIC 9(8).               
014010             15  HOLD-TDAA-SORT-FIELD-1   PIC X(36).              
014012             15  HOLD-TDAA-SORT-FIELD-2   PIC X(36).              
014014             15  HOLD-TDAA-SORT-FIELD-3   PIC X(36).              
014016             15  HOLD-TDAA-SORT-FIELD-4   PIC X(36).              
014018         10  HOLD-TDAA-CMAT-PUB-ID        PIC X(8).               
014020         10  HOLD-TDAA-MSA-CONTR          PIC 9.                  
014022         10  HOLD-TDAA-MSA-CONTR-LY       PIC 9.                  
014024         10  HOLD-TDAA-AVG-ACCR-INT       PIC S9(12)V9(6).        
014026         10  HOLD-TDAA-LEVEL-PAY          PIC 9.                  
014028         10  HOLD-TDAA-ST-INT-CD          PIC 9.                  
014030         10  HOLD-TDAA-ST-WHLD-CD         PIC 9.                  
014032         10  HOLD-TDAA-ST-WHLD-AMT        PIC S9(12)V99.          
014034         10  HOLD-TDAA-ST-CUR-W-AMT       PIC S9(12)V99.          
014036         10  HOLD-TDAA-ST-LST-W-AMT       PIC S9(12)V99.          
014038         10  HOLD-TDAA-ST-WHLD-STD        PIC S9(12)V99.          
014040         10  HOLD-TDAA-ST-WHLD-YTD        PIC S9(12)V99.          
014042         10  HOLD-TDAA-CIF-REMARK         PIC X.                  
014044         10  HOLD-TDAA-CSR                PIC X(3).               
014046         10  HOLD-TDAA-BSA-O-RSK-CD       PIC 9(1).               
014048         10  HOLD-TDAA-BSA-C-RSK-CD       PIC 9(1).               
014050         10  HOLD-TDAA-LRG-TRX-DT         PIC 9(8).               
014052         10  HOLD-TDAA-HSA-FMLY-IND       PIC 9(01).              
014054         10  HOLD-TDAA-STOP-PAY-IND       PIC 9(01).              
014056         10  HOLD-TDAA-IMG-PG-TYPE        PIC X(01).              
014058         10  HOLD-TDAA-CONT-LMT-CLC       PIC 9(5)V99.            
014060         10  HOLD-TDAA-CONT-LMT-ENT       PIC 9(5)V99.            
014062         10  HOLD-TDAA-MEMO-DB            PIC S9(12)V99.          
014064         10  HOLD-TDAA-MEMO-CR            PIC S9(12)V99.          
014066         10  HOLD-TDAA-MEMO-DB-2          PIC S9(12)V99.          
014068         10  HOLD-TDAA-MEMO-CR-2          PIC S9(12)V99.          
014070         10  HOLD-TDAA-RT-AT-CONV         PIC 9(2)V9(3).          
014072         10  HOLD-TDAA-ACCR-AT-CONV       PIC S9(12)V9(6).        
014074         10  HOLD-TDAA-RT-AT-ACRDT        PIC 9(2)V9(3).          
014076         10  HOLD-TDAA-BAL-AT-ACRDT       PIC S9(12)V9(2).        
014078         10  HOLD-TDAA-ZERO-RT-ALLOW      PIC 9.                  
014080         10  HOLD-TDAA-EMAIL-NTC          PIC 9.                  
014082         10  HOLD-TDAA-EMAIL-STMT         PIC 9.                  
014084         10  HOLD-TDAA-FRAUD-CK-DT        PIC 9(8).               
014086         10  HOLD-TDAA-FRAUD-CK-CNT       PIC 9(3).               
014088         10  HOLD-TDAA-FRAUD-CK-AMT       PIC S9(12)V9(2).        
014090         10  HOLD-TDAA-MISC-ACCTNO        PIC 9(8).               
014092         10  HOLD-TDAA-RMD-MAN-CALC       PIC 9(1).               
014094         10  HOLD-TDAA-RMD-AMOUNT         PIC S9(12)V9(2).        
014096         10  HOLD-TDAA-BROKERAGE-ID       PIC X(10).              
014098         10  HOLD-TDAA-MONY-SRC-CD2       PIC X(03).              
014100         10  HOLD-TDAA-INHERIT-IRA        PIC 9(01).              
014102         10  HOLD-TDAA-LIFE-FACTOR        PIC 9(02)V9(1).         
014104         10  HOLD-TDAA-EV-LARGE-TRX       PIC X(01).              
014106         10  HOLD-TDAA-EV-MAT-AMT         PIC S9(12)V9(2).        
014108         10  HOLD-TDAA-EV-DISP-ACCT       PIC 9(22).              
014110         10  HOLD-TDAA-EV-COMP-ACCT       PIC 9(22).              
014112         10  HOLD-TDAA-EV-PUBLIC-ID       PIC X(08).              
014114         10  HOLD-TDAA-EV-MAT-TYPE        PIC X(01).              
014116         10  HOLD-TDAA-EV-INT-TYPE        PIC X(01).              
014118         10  HOLD-TDAA-EV-ACCT-TYP        PIC X(01).              
014120         10  HOLD-TDAA-EV-WHLD-PCT        PIC 9(02).              
014122         10  HOLD-TDAA-EV-NON-ACCR        PIC X(01).              
014124         10  HOLD-TDAA-EV-CLOSED          PIC X(01).              
014126         10  HOLD-TDAA-EV-CLOSE-MO        PIC X(01).              
014128         10  HOLD-TDAA-EV-OPEN-MO         PIC X(01).              
014130         10  HOLD-TDAA-EV-ANN-INT         PIC S9(12)V9(2).        
014132         10  HOLD-TDAA-EV-ORIG-RT         PIC 9(2)V9(3).          
014134         10  HOLD-TDAA-EV-DLY-INT         PIC S9(12)V9(6).        
014136         10  HOLD-TDAA-EV-INT-PAY         PIC S9(12)V9(6).        
014138         10  HOLD-TDAA-EV-AVAIL-BL        PIC S9(12)V9(2).        
014140         10  HOLD-TDAA-EV-RETAIN          PIC X(01).              
014142         10  HOLD-TDAA-EV-CL-RETAIN       PIC X(01).              
014144         10  HOLD-TDAA-EV-TIMES-REN       PIC 9(05).              
014146         10  HOLD-TDAA-EV-CURR-BAL        PIC S9(12)V9(2).        
014148         10  HOLD-TDAA-BRKR-DEP-CAT       PIC 9(01).              
014150         10  HOLD-TDAA-LINE-OF-BUS        PIC 9(4).               
014152         10  HOLD-TDAA-1ST-STMT           PIC 9(01).              
014154         10  HOLD-TDAA-POSTAL-CITY        PIC X(40).              
014156         10  HOLD-TDAA-POSTAL-CNTRY       PIC X(02).              
014158         10  HOLD-TDAA-CITIZN-CNTRY       PIC X(02).              
014160         10  HOLD-TDAA-CUSTM-FIELDS       PIC 9(01).              
014162         10  HOLD-TDAA-AVG-STEP-RT        PIC 9(2)V9(3).          
014164         10  HOLD-TDAA-MONITOR-INQ        PIC 9(01).              
014166         10  HOLD-TDAA-IGL-GRP-2          PIC 9(02).              
014168         10  HOLD-TDAA-AGG-DAYS-QTD       PIC 9(03).              
014170         10  HOLD-TDAA-AGG-BAL-QTD        PIC S9(15)V9(2).        
014172         10  HOLD-TDAA-IGL-GRP-3          PIC 9(02).              
014174         10  HOLD-TDAA-ALT-ADDR-EOY       PIC 9(01).              
014176         10  HOLD-TDAA-1042S-TAX-ID       PIC X(22).              
014178         10  HOLD-TDAA-LEC                PIC X(01).              
014180         10  HOLD-TDAA-BAL-AT-CLOSE       PIC S9(12)V9(2).        
014182         10  HOLD-TDAA-AVL-CAP-INT        PIC S9(6)V9(2).         
014184         10  HOLD-TDAA-FIDM-TR-FUND       PIC 9(01).              
014186         10  HOLD-TDAA-IRS-FRM-DLVR       PIC 9(01).              
014188         10  HOLD-TDAA-PROVINCE           PIC X(02).              
014190         10  HOLD-TDAA-PROMOTION          PIC X(25).              
014192         10  HOLD-EXTRA-FIELDS.                                   
014194             15  HOLD-TDAA-DAYS-INTO-PER  PIC 9(5).               
014196             15  HOLD-TDAA-CURR-PAYOFF    PIC S9(9)V9(2).         
014198             15  HOLD-TDAA-MANUAL-RT-X    PIC X(5).               
014200             15  HOLD-TDAA-MANUAL-RT-RE   REDEFINES               
```

⚠️  This is the source code you must document.
    250 lines from 6847 to 7096.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

