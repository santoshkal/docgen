# LLM Request Debug File
Generated: 2025-11-14T18:18:33.185925

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 16/55
- **Model**: gpt-4.1
- **Chunk Number**: 16
- **Pass Number**: 3
- **Attempt Number**: 2 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~19,226 tokens
- **Total Input**: ~21,184 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 16/55" (ID: detailed-code-explanation)

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


**CHUNK 16 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-14T17:36:35.036798", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 16 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 7097 to 8032 (936 lines)\nChunk Tokens (estimated): ~19,904\nActual Input Tokens: 21,310 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 7097-8032 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 16 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 16 of 55.\n\n\n=============================================================================\nCHUNK 16 SOURCE CODE (Lines 7097-8032)\n=============================================================================\n\n```cobol\n014202                         HOLD-TDAA-MANUAL-RT-X.                   \n014204                 20  HOLD-TDAA-MANUAL-RT  PIC 9(2)V9(3).          \n014206                                                                  \n014208     05  HOLD-TDAIRA.                                             \n014210         10  HOLD-TDAI-BANK             PIC 9(4).                 \n014212         10  HOLD-TDAI-BRCH             PIC 9(4).                 \n014214         10  HOLD-TDAI-APPL             PIC 9(1).                 \n014216         10  HOLD-TDAI-CUST             PIC 9(12).                \n014218         10  HOLD-TDAI-ACCT             PIC 9(10).                \n014220         10  HOLD-TDAI-PUB-ID           PIC X(8).                 \n014222         10  HOLD-TDAI-ADD-DT           PIC 9(8).                 \n014224         10  HOLD-TDAI-ADD-TM           PIC 9(6).                 \n014226         10  HOLD-TDAI-DS-TYPE          PIC X(2)                  \n014228                          OCCURS 20 TIMES.                        \n014230         10  HOLD-TDAI-CN-TYPE          PIC 9(2)                  \n014232                          OCCURS 20 TIMES.                        \n014234         10  HOLD-TDAI-DS-CN-AMT        PIC S9(12)V99             \n014236                          OCCURS 20 TIMES.                        \n014238         10  HOLD-TDAI-DS-PEN-AMT       PIC S9(12)V99             \n014240                          OCCURS 20 TIMES.                        \n014242         10  HOLD-TDAI-DS-WTHLD-AMT     PIC S9(12)V99             \n014244                          OCCURS 20 TIMES.                        \n014246         10  HOLD-TDAI-DS-ST-WH-AMT     PIC S9(12)V99             \n014248                          OCCURS 20 TIMES.                        \n014250         10  HOLD-TDAI-DS-EXC-EARN      PIC S9(12)V9(2)           \n014252                          OCCURS 20 TIMES.                        \n014254         10  HOLD-TDAI-DS-C-YTD-CNT     PIC 9(5).                 \n014256         10  HOLD-TDAI-DS-P-YTD-CNT     PIC 9(5).                 \n014258         10  HOLD-TDAI-DS-AMT-C-YTD     PIC S9(12)V9(2).          \n014260         10  HOLD-TDAI-DS-AMT-P-YTD     PIC S9(12)V9(2).          \n014262         10  HOLD-TDAI-DS-INT-AMT       PIC S9(12)V9(2).          \n014264         10  HOLD-TDAI-CN-YTD-CNT       PIC 9(5).                 \n014266         10  HOLD-TDAI-CN-YTD-AMT       PIC S9(12)V9(2).          \n014268         10  HOLD-TDAI-CN-LYTD-AMT      PIC S9(12)V9(2).          \n014270         10  HOLD-TDAI-EMP-CONT-LYR     PIC S9(12)V9(2).          \n014272         10  HOLD-TDAI-REG-CONT-LYR     PIC S9(12)V9(2).          \n014274         10  HOLD-TDAI-UNINSURED        PIC X(1).                 \n014276         10  HOLD-TDAI-ROLLOVER         PIC S9(12)V9(2).          \n014278         10  HOLD-TDAI-ROLLOVER-LYR     PIC S9(12)V9(2).          \n014280         10  HOLD-TDAI-TRANSFER-IN      PIC S9(12)V9(2).          \n014282         10  HOLD-TDAI-TRANSFER-OUT     PIC S9(12)V9(2).          \n014284         10  HOLD-TDAI-1ST-CN-DATE      PIC 9(8).                 \n014286         10  HOLD-TDAI-BASIS-C-LTD      PIC S9(12)V99.            \n014288         10  HOLD-TDAI-BASIS-D-LTD      PIC S9(12)V99.            \n014290         10  HOLD-TDAI-BASIS-D-YTD      PIC S9(12)V99.            \n014292         10  HOLD-TDAI-EXTRA-FIELDS.                              \n014294             15  HOLD-TDAI-CN-TYPE-EX   PIC 9(2).                 \n014296             15  HOLD-TDAI-DS-TYPE-EX.                            \n014298               20  HOLD-TDAI-DS-TYPE-EX-1       PIC X.            \n014300               20  HOLD-TDAI-DS-TYPE-EX-2       PIC X.            \n014302                                                                  \n014304      05 HOLD-TDADISTR.                                           \n014306         10 HOLD-TDAD-BANK                      PIC 9(04).        \n014308         10 HOLD-TDAD-BRCH                      PIC 9(04).        \n014310         10 HOLD-TDAD-APPL                      PIC 9(01).        \n014312         10 HOLD-TDAD-CUST                      PIC 9(12).        \n014314         10 HOLD-TDAD-ACCT                      PIC 9(10).        \n014316         10 HOLD-TDAD-NXT-ACCT-P                PIC 9(10).        \n014318         10 HOLD-TDAD-NXT-ACCT-S                PIC 9(10).        \n014320         10 HOLD-TDAD-N-ACCT-BY-RT              PIC 9(1).         \n014322         10 HOLD-TDAD-SERIAL                    PIC 9(12).        \n014324         10 HOLD-TDAD-SER-NEXT                  PIC 9(12).        \n014326         10 HOLD-TDAD-DISP-CD                   PIC 9(01).        \n014328         10 HOLD-TDAD-TYPE                      PIC X(02).        \n014330         10 HOLD-TDAD-PRINCIPAL                 PIC 9(01).        \n014332         10 HOLD-TDAD-INTEREST                  PIC 9(01).        \n014334         10 HOLD-TDAD-DS-CODE                   PIC 9(01).        \n014336         10 HOLD-TDAD-WTHLD-CD                  PIC 9(01).        \n014338         10 HOLD-TDAD-WHLD-AMT                  PIC S9(12)V99.    \n014340         10 HOLD-TDAD-ST-WHLD-CD                PIC 9(01).        \n014342         10 HOLD-TDAD-ST-WHLD-AMT               PIC S9(12)V99.    \n014344         10 HOLD-TDAD-TRF-ACCT                  PIC 9(12).        \n014346         10 HOLD-TDAD-TRF-ACCT-S                PIC 9(10).        \n014348         10 HOLD-TDAD-AMT-CD                    PIC 9(01).        \n014350         10 HOLD-TDAD-DS-AMT                    PIC S9(12)V99.    \n014352         10 HOLD-TDAD-DS-FREQ                   PIC 9(01).        \n014354         10 HOLD-TDAD-DS-NTRVL                  PIC 9(04).        \n014356         10 HOLD-TDAD-END-OF-DIST               PIC 9(1).         \n014358         10 HOLD-TDAD-DIST-NTC-CD               PIC 9(01).        \n014360         10 HOLD-TDAD-EOY-DS-FORM               PIC 9(01).        \n014362         10 HOLD-TDAD-5-YR-RULE                 PIC 9(01).        \n014364         10 HOLD-TDAD-ANUAL-RECALC              PIC 9(01).        \n014366         10 HOLD-TDAD-JOINT-CD                  PIC 9(01).        \n014368         10 HOLD-TDAD-PUB-ID                    PIC X(08).        \n014370         10 HOLD-TDAD-LST-DIST-DT               PIC 9(8).         \n014372         10 HOLD-TDAD-IN-PROC-DT                PIC 9(8).         \n014374         10 HOLD-TDAD-NXT-DIST-DT               PIC 9(8).         \n014376         10 HOLD-TDAD-NXT-DS-PROC               PIC 9(8).         \n014378         10 HOLD-TDAD-ADD-DT                    PIC 9(08).        \n014380         10 HOLD-TDAD-ADD-TM                    PIC 9(08).        \n014382                                                                  \n014384         10 HOLD-TDAD-MIN-AMT                   PIC S9(12)V99.    \n014386         10 HOLD-TDAD-AMT                       PIC S9(12)V99.    \n014388         10 HOLD-TDAD-LST-AMT                   PIC S9(12)V99.    \n014390         10 HOLD-TDAD-CUR-WHLD-AMT              PIC S9(12)V99.    \n014392         10 HOLD-TDAD-WHLD-YTD                  PIC S9(12)V99.    \n014394         10 HOLD-TDAD-LST-WHLD-AMT              PIC S9(12)V99.    \n014396         10 HOLD-TDAD-PRINCPL-AMT               PIC S9(12)V99.    \n014398         10 HOLD-TDAD-INT-AMT                   PIC S9(12)V99.    \n014400         10 HOLD-TDAD-INT-YTD                   PIC S9(12)V99.    \n014402         10 HOLD-TDAD-ST-CUR-W-AMT              PIC S9(12)V99.    \n014404         10 HOLD-TDAD-ST-LST-W-AMT              PIC S9(12)V99.    \n014406         10 HOLD-TDAD-CK-IND-1                  PIC X(1).         \n014408         10 HOLD-TDAD-CK-IND-2                  PIC X(1).         \n014410         10 HOLD-TDAD-LUPD-DT                   PIC 9(8).         \n014412         10 HOLD-TDAD-LUPD-TM                   PIC 9(6).         \n014414         10 HOLD-TDAD-RMD-OVERRIDE              PIC 9.            \n014416         10 HOLD-TDAD-RMD-AMOUNT                PIC S9(12)V9(2).  \n014418         10 HOLD-TDAD-DS-NBR                    PIC 9(2).         \n014420         10 HOLD-TDAD-NONDB-FIELDS.                               \n014422             15  HOLD-TDAI-DS-NTC-TYPE          PIC 9(1).         \n014424                                                                  \n014426     05  HOLD-TDAACTV.                                            \n014428         10  HOLD-TDA-ACTV-BANK         PIC 9(4).                 \n014430         10  HOLD-TDA-ACTV-BRCH         PIC 9(4).                 \n014432         10  HOLD-TDA-ACTV-APPL         PIC 9(1).                 \n014434         10  HOLD-TDA-ACTV-CUST         PIC 9(12).                \n014436         10  HOLD-TDA-ACTV-ACCT         PIC 9(10).                \n014438         10  HOLD-TDA-ACTV-TOT-CD       PIC 9(3).                 \n014440         10  HOLD-TDA-ACTV-IGL-GRP      PIC 9(2).                 \n014442         10  HOLD-TDA-ACTV-OFFICER      PIC X(3).                 \n014444         10  HOLD-TDA-ACTV-NC-INDC      PIC 9(1).                 \n014446         10  HOLD-TDA-ACTV-PROC-FG      PIC 9(1).                 \n014448         10  HOLD-TDA-ACTV-TYPE         PIC 9(4).                 \n014450         10  HOLD-TDA-ACTV-EFF-DT       PIC 9(8).                 \n014452         10  HOLD-TDA-ACTV-DATE         PIC 9(8).                 \n014454         10  HOLD-TDA-ACTV-MAINT        PIC 9(8).                 \n014456         10  HOLD-TDA-ACTV-TIME         PIC 9(8).                 \n014458         10  HOLD-TDA-ACTV-SEQ-NBR      PIC 9(2).                 \n014460         10  HOLD-TDA-ACTV-SERIAL       PIC 9(12).                \n014462         10  HOLD-TDA-ACTV-SOURCE       PIC 9(2).                 \n014464         10  HOLD-TDA-ACTV-ERASED       PIC 9(1).                 \n014466         10  HOLD-TDA-ACTV-DR-CR        PIC 9(1).                 \n014468         10  HOLD-TDA-ACTV-E-PUBID      PIC X(8).                 \n014470         10  HOLD-TDA-ACTV-PUB-ID       PIC X(8).                 \n014472         10  HOLD-TDA-ACTV-SUB          PIC 9(3).                 \n014474                                                                  \n014476         10  HOLD-TDA-ACTVT-MONETARY.                             \n014478             15  HOLD-TDA-ACTVT-CODE       PIC 9(3).              \n014480             15  HOLD-TDA-ACTVT-AMT        PIC S9(12)V9(2).       \n014482             15  HOLD-TDA-ACTVT-DESC       PIC X(80).             \n014484             15  HOLD-TDA-ACTVT-DESC-R                            \n014486                 REDEFINES HOLD-TDA-ACTVT-DESC.                   \n014488                 20  HOLD-TDA-ACTVT-DESC-1 PIC X(40).             \n014490                 20  HOLD-TDA-ACTVT-DESC-2 PIC X(40).             \n014492             15  HOLD-TDA-ACTVT-UNPOST     PIC 9(1).              \n014494             15  HOLD-TDA-ACTVT-RATE       PIC 9(2)V999.          \n014496             15  HOLD-TDA-ACTVT-YIELD      PIC 9(2)V999.          \n014498             15  HOLD-TDA-ACTVT-P-DIEM     PIC S9(12)V9(6).       \n014500             15  HOLD-TDA-ACTVT-WTHLD      PIC S9(12)V9(2).       \n014502             15  HOLD-TDA-ACTVT-PENLTY     PIC S9(12)V9(2).       \n014504             15  HOLD-TDA-ACTVT-EX-EARN    PIC S9(12)V9(2).       \n014506             15  HOLD-TDA-ACTVT-DS-TYPE.                          \n014508               20 HOLD-TDA-ACTVT-DS-TYPE-1 PIC X.                 \n014510               20 HOLD-TDA-ACTVT-DS-TYPE-2 PIC X.                 \n014512             15  HOLD-TDA-ACTVT-CN-CUST    PIC 9(12).             \n014514             15  HOLD-TDA-ACTVT-CN-TYPE    PIC 9(2).              \n014516             15  HOLD-TDA-ACTVT-ST-WHLD    PIC S9(12)V9(2).       \n014518             15  HOLD-TDA-ACTVT-NEW-BAL    PIC S9(12)V9(2).       \n014520             15  HOLD-TDA-ACTVT-CHK-NBR    PIC 9(10).             \n014522             15  HOLD-TDA-ACTVT-SEQ-NBR    PIC 9(16).             \n014524             15  HOLD-TDA-ACTVT-PRIDAY     PIC X.                 \n014526             15  HOLD-TDA-ACTVT-INT-COR    PIC 9(1).              \n014528             15  HOLD-TDA-ACTVT-DISP-CD    PIC 9(1).              \n014530             15  HOLD-TDA-ACTVT-QRP-ROL    PIC 9(1).              \n014532                                                                  \n014534         10  HOLD-TDA-ACTVC-CHANGE.                               \n014536             15  HOLD-TDA-ACTVC-CODE       PIC 9(4).              \n014538             15  HOLD-TDA-ACTVC-EXCPT      PIC 9(3).              \n014540             15  HOLD-TDA-ACTVC-CHG-FRM    PIC X(40).             \n014542             15  HOLD-TDA-ACTVC-CHG-TO     PIC X(40).             \n014544             15  HOLD-TDA-ACTVC-NCREOPN    PIC 9(1).              \n014546             15  HOLD-TDA-ACTVC-DDN        PIC 9(10).             \n014548             15  HOLD-TDA-ACTVC-TMPLATE    PIC 9(4).              \n014550                                                                  \n014552         10  HOLD-TDA-ACTMT-MAT.                                  \n014554             15  HOLD-TDA-ACTMT-LMAT-DT    PIC 9(08).             \n014556             15  HOLD-TDA-ACTMT-NMAT-DT    PIC 9(08).             \n014558             15  HOLD-TDA-ACTMT-PMAT-DT    PIC 9(08).             \n014560             15  HOLD-TDA-ACTMT-TOTL-CD    PIC 9(03).             \n014562                                                                  \n014564         10  HOLD-TDA-ACTCL-CALC.                                 \n014566             15  HOLD-TDA-ACTCL-P-DIEM     PIC S9(12)V9(6).       \n014568             15  HOLD-TDA-ACTCL-N-DIEM     PIC S9(12)V9(6).       \n014570             15  HOLD-TDA-ACTCL-P-ACCR     PIC S9(12)V9(6).       \n014572             15  HOLD-TDA-ACTCL-N-ACCR     PIC S9(12)V9(6).       \n014574             15  HOLD-TDA-ACTCL-P-ACRDT    PIC 9(8).              \n014576             15  HOLD-TDA-ACTCL-N-ACRDT    PIC 9(8).              \n014578             15  HOLD-TDA-ACTCL-P-WTHLD    PIC S9(12)V99.         \n014580             15  HOLD-TDA-ACTCL-N-WTHLD    PIC S9(12)V99.         \n014582             15  HOLD-TDA-ACTCL-P-PENAL    PIC S9(12)V99.         \n014584             15  HOLD-TDA-ACTCL-N-PENAL    PIC S9(12)V99.         \n014586             15  HOLD-TDA-ACTCL-P-PAYOF    PIC S9(12)V99.         \n014588             15  HOLD-TDA-ACTCL-N-PAYOF    PIC S9(12)V99.         \n014590             15  HOLD-TDA-ACTCL-ST-P-WD    PIC S9(12)V99.         \n014592             15  HOLD-TDA-ACTCL-ST-N-WD    PIC S9(12)V99.         \n014594                                                                  \n014596         10  HOLD-TDA-ACTHT-HIST.                                 \n014598             15  HOLD-TDA-ACTHT-DATE       PIC 9(8).              \n014600             15  HOLD-TDA-ACTHT-CODE       PIC 9(4).              \n014602             15  HOLD-TDA-ACTHT-AMOUNT     PIC S9(12)V99.         \n014604             15  HOLD-TDA-ACTHT-TAX-AMT    PIC S9(12)V99.         \n014606             15  HOLD-TDA-ACTHT-FM-RATE    PIC S99V999.           \n014608             15  HOLD-TDA-ACTHT-FM-DESC    PIC X(26).             \n014610                                                                  \n014612         10  HOLD-TDA-ACTVN-NEW.                                  \n014614             15  HOLD-TDA-ACTVN-STR-NBR    PIC 9(2).              \n014616             15  HOLD-TDA-ACTVN-PUR-AMT    PIC S9(12)V99.         \n014618             15  HOLD-TDA-ACTVN-BASE-RT    PIC S9(2)V9(3).        \n014620             15  HOLD-TDA-ACTVN-RT-IND     PIC X(1).              \n014622             15  HOLD-TDA-ACTVN-TYPE       PIC 9(2).              \n014624                                                                  \n014626         10  HOLD-TDA-ACTVR-RATES.                                \n014628             15  HOLD-TDA-ACTVR-CUR-RT     PIC S99V999.           \n014630             15  HOLD-TDA-ACTVR-F-L-RT     PIC S99V999.           \n014632             15  HOLD-TDA-ACTVR-T-L-RT     PIC S99V999.           \n014634             15  HOLD-TDA-ACTVR-F-Y-RT     PIC S99V999.           \n014636             15  HOLD-TDA-ACTVR-T-Y-RT     PIC S99V999.           \n014638             15  HOLD-TDA-ACTVR-F-L-DT     PIC 9(08).             \n014640             15  HOLD-TDA-ACTVR-T-L-DT     PIC 9(08).             \n014642             15  HOLD-TDA-ACTVR-F-RCYC     PIC 9(02).             \n014644             15  HOLD-TDA-ACTVR-T-RCYC     PIC 9(02).             \n014646             15  HOLD-TDA-ACTVR-PRS-DT     PIC 9(08).             \n014648             15  HOLD-TDA-ACTVR-RT-IND     PIC X.                 \n014650                                                                  \n014652         10  HOLD-TDA-ACTRR-RATES.                                \n014654             15  HOLD-TDA-ACTRR-F-RG       PIC 9(2).              \n014656             15  HOLD-TDA-ACTRR-T-RG       PIC 9(2).              \n014658             15  HOLD-TDA-ACTRR-F-CD       PIC 9(2).              \n014660             15  HOLD-TDA-ACTRR-T-CD       PIC 9(2).              \n014662             15  HOLD-TDA-ACTRR-F-RT       PIC S99V999            \n014664                                           OCCURS 10 TIMES.       \n014666             15  HOLD-TDA-ACTRR-T-RT       PIC S99V999            \n014668                                           OCCURS 10 TIMES.       \n014670             15  HOLD-TDA-ACTRR-F-DT       PIC 9(08)              \n014672                                           OCCURS 10 TIMES.       \n014674             15  HOLD-TDA-ACTRR-T-DT       PIC 9(08)              \n014676                                           OCCURS 10 TIMES.       \n014678                                                                  \n014680         10  HOLD-TDA-ACTVI-INTEREST.                             \n014682             15  HOLD-TDA-ACTVI-F-INT      PIC S9(12)V9(6).       \n014684             15  HOLD-TDA-ACTVI-T-INT      PIC S9(12)V9(6).       \n014686             15  HOLD-TDA-ACTVI-F-INTA     PIC S9(12)V99.         \n014688             15  HOLD-TDA-ACTVI-T-INTA     PIC S9(12)V99.         \n014690             15  HOLD-TDA-ACTVI-F-PDAY     PIC S9(12)V9(6).       \n014692             15  HOLD-TDA-ACTVI-T-PDAY     PIC S9(12)V9(6).       \n014694             15  HOLD-TDA-ACTVI-RD-DT      PIC 9(08).             \n014696                                                                  \n014698         10  HOLD-TDA-ACTCK-CHECK.                                \n014700             15 HOLD-TDA-ACTCK-F-I-PT      PIC S9(12)V99.         \n014702             15 HOLD-TDA-ACTCK-T-I-PT      PIC S9(12)V99.         \n014704             15 HOLD-TDA-ACTCK-F-C-WA      PIC S9(12)V99.         \n014706             15 HOLD-TDA-ACTCK-T-C-WA      PIC S9(12)V99.         \n014708             15 HOLD-TDA-ACTCK-F-STAT      PIC X.                 \n014710             15 HOLD-TDA-ACTCK-T-STAT      PIC X.                 \n014712             15 HOLD-TDA-ACTCK-PRS-DT      PIC 9(08).             \n014714             15 HOLD-TDA-ACTCK-F-ST-WA     PIC S9(12)V99.         \n014716             15 HOLD-TDA-ACTCK-T-ST-WA     PIC S9(12)V99.         \n014718                                                                  \n014720         10  HOLD-TDA-ACTWH-WITHHOLD.                             \n014722             15 HOLD-TDA-ACTWH-F-YTD       PIC S9(12)V99.         \n014724             15 HOLD-TDA-ACTWH-T-YTD       PIC S9(12)V99.         \n014726             15 HOLD-TDA-ACTWH-F-STD       PIC S9(12)V99.         \n014728             15 HOLD-TDA-ACTWH-T-STD       PIC S9(12)V99.         \n014730             15 HOLD-TDA-ACTWH-F-L-AMT     PIC S9(12)V99.         \n014732             15 HOLD-TDA-ACTWH-T-L-AMT     PIC S9(12)V99.         \n014734                                                                  \n014736         10  HOLD-TDA-ACTPT-INT-POST.                             \n014738             15 HOLD-TDA-ACTPT-F-IP-L      PIC S9(12)V99.         \n014740             15 HOLD-TDA-ACTPT-T-IP-L      PIC S9(12)V99.         \n014742             15 HOLD-TDA-ACTPT-F-1099      PIC S9(12)V99.         \n014744             15 HOLD-TDA-ACTPT-T-1099      PIC S9(12)V99.         \n014746             15 HOLD-TDA-ACTPT-F-C-BL      PIC S9(12)V99.         \n014748             15 HOLD-TDA-ACTPT-T-C-BL      PIC S9(12)V99.         \n014750             15 HOLD-TDA-ACTPT-F-L-DT      PIC 9(08).             \n014752             15 HOLD-TDA-ACTPT-T-L-DT      PIC 9(08).             \n014754             15 HOLD-TDA-ACTPT-F-N-DT      PIC 9(08).             \n014756             15 HOLD-TDA-ACTPT-T-N-DT      PIC 9(08).             \n014758             15 HOLD-TDA-ACTPT-F-I-PT      PIC S9(12)V99.         \n014760             15 HOLD-TDA-ACTPT-T-I-PT      PIC S9(12)V99.         \n014762             15 HOLD-TDA-ACTPT-F-C-WA      PIC S9(12)V99.         \n014764             15 HOLD-TDA-ACTPT-T-C-WA      PIC S9(12)V99.         \n014766             15 HOLD-TDA-ACTPT-F-ACCR      PIC S9(12)V9(06).      \n014768             15 HOLD-TDA-ACTPT-T-ACCR      PIC S9(12)V9(06).      \n014770             15 HOLD-TDA-ACTPT-F-STAT      PIC X(01).             \n014772             15 HOLD-TDA-ACTPT-T-STAT      PIC X(01).             \n014774             15 HOLD-TDA-ACTPT-F-A-DT      PIC 9(08).             \n014776             15 HOLD-TDA-ACTPT-T-A-DT      PIC 9(08).             \n014778             15 HOLD-TDA-ACTPT-F-PDAY      PIC S9(12)V9(6).       \n014780             15 HOLD-TDA-ACTPT-T-PDAY      PIC S9(12)V9(6).       \n014782             15 HOLD-TDA-ACTPT-N-INT       PIC S9(12)V99.         \n014784             15 HOLD-TDA-ACTPT-C-INT       PIC S9(12)V99.         \n014786             15 HOLD-TDA-ACTPT-DISP-CD     PIC 9(01).             \n014788             15 HOLD-TDA-ACTPT-INT-ACCT    PIC 9(12).             \n014790             15 HOLD-TDA-ACTPT-INT-ACCT-S  PIC 9(10).             \n014792             15 HOLD-TDA-ACTPT-F-ST-WA     PIC S9(12)V9(2).       \n014794             15 HOLD-TDA-ACTPT-T-ST-WA     PIC S9(12)V9(2).       \n014796             15 HOLD-TDA-ACTPT-NEW-BAL     PIC S9(9)V99.          \n014798             15 HOLD-TDA-ACTPT-CLO-MAT     PIC 9.                 \n014800                                                                  \n014802         10  HOLD-TDA-ACTAC-CLOSE-ACCT.                           \n014804             15 HOLD-TDA-ACTAC-AMT         PIC S9(12)V9(2).       \n014806             15 HOLD-TDA-ACTAC-INT         PIC S9(12)V9(2).       \n014808             15 HOLD-TDA-ACTAC-PENLTY      PIC S9(12)V9(2).       \n014810             15 HOLD-TDA-ACTAC-WTHLD       PIC S9(12)V9(2).       \n014812             15 HOLD-TDA-ACTAC-LST-INT     PIC S9(12)V9(2).       \n014814             15 HOLD-TDA-ACTAC-W-ALLOW     PIC 9(1).              \n014816             15 HOLD-TDA-ACTAC-D-ALLOW     PIC 9(1).              \n014818             15 HOLD-TDA-ACTAC-CUR-PEN     PIC S9(12)V9(2).       \n014820             15 HOLD-TDA-ACTAC-AVL-BAL     PIC S9(12)V9(2).       \n014822             15 HOLD-TDA-ACTAC-DS-TYPE     PIC X(2).              \n014824             15 HOLD-TDA-ACTAC-ST-WHLD     PIC S9(12)V9(2).       \n014826             15 HOLD-TDA-ACTAC-DRP-INT     PIC S9(12)V99.         \n014828             15 HOLD-TDA-ACTAC-DS-DISP     PIC 9.                 \n014830             15 HOLD-TDA-ACTAC-CLO-MAT     PIC 9.                 \n014832             15 HOLD-TDA-ACTAC-T-ACCT      PIC 9(12).             \n014834             15 HOLD-TDA-ACTAC-T-ACCTS     PIC 9(10).             \n014836             15 HOLD-TDA-ACTAC-DS-CODE     PIC 9(1).              \n014838             15 HOLD-TDA-ACTAC-DS-NBR      PIC 9(2).              \n014840             15 HOLD-TDA-ACTAC-DESC        PIC X(30).             \n014842                                                                  \n014844         10  HOLD-TDA-ACTDS-DISTRIBUTE.                           \n014846             15 HOLD-TDA-ACTDS-TYPE        PIC XX.                \n014848             15 HOLD-TDA-ACTDS-DISP-CD     PIC 9.                 \n014850             15 HOLD-TDA-ACTDS-INT         PIC 9.                 \n014852             15 HOLD-TDA-ACTDS-PRNCPAL     PIC 9.                 \n014854             15 HOLD-TDA-ACTDS-CD          PIC 9.                 \n014856             15 HOLD-TDA-ACTDS-NXT-DT      PIC 9(8).              \n014858             15 HOLD-TDA-ACTDS-W-AMT       PIC S9(12)V99.         \n014860             15 HOLD-TDA-ACTDS-W-CD        PIC 9.                 \n014862             15 HOLD-TDA-ACTDS-AMT         PIC S9(12)V99.         \n014864             15 HOLD-TDA-ACTDS-FREQ        PIC 9.                 \n014866             15 HOLD-TDA-ACTDS-NTRVL       PIC 9(4).              \n014868             15 HOLD-TDA-ACTDS-T-ACCT      PIC 9(12).             \n014870             15 HOLD-TDA-ACTDS-T-ACCTS     PIC 9(10).             \n014872             15 HOLD-TDA-ACTDS-ST-WAMT     PIC S9(12)V99.         \n014874             15 HOLD-TDA-ACTDS-ST-W-CD     PIC 9(01).             \n014876             15 HOLD-TDA-ACTDS-NEW-BAL     PIC S9(12)V99.         \n014878             15 HOLD-TDA-ACTDS-DS-NBR      PIC 9(2).              \n014880                                                                  \n014882         10  HOLD-TDA-ACTE-ERASER.                                \n014884             15 HOLD-TDA-ACTE-SERIAL       PIC 9(12).             \n014886             15 HOLD-TDA-ACTE-TYPE         PIC 99.                \n014888             15 HOLD-TDA-ACTE-EFF-DT       PIC 9(8).              \n014890             15 HOLD-TDA-ACTE-DATE         PIC 9(8).              \n014892             15 HOLD-TDA-ACTE-SEQ-NBR      PIC 99.                \n014894                                                                  \n014896         10  HOLD-TDA-ACTCP-COMPOUND.                             \n014898             15 HOLD-TDA-ACTCP-P-INT       PIC S9(12)V9(6).       \n014900             15 HOLD-TDA-ACTCP-N-INT       PIC S9(12)V9(6).       \n014902             15 HOLD-TDA-ACTCP-P-PDAY      PIC S9(12)V9(6).       \n014904             15 HOLD-TDA-ACTCP-N-PDAY      PIC S9(12)V9(6).       \n014906             15 HOLD-TDA-ACTCP-P-INTA      PIC S9(12)V99.         \n014908             15 HOLD-TDA-ACTCP-N-INTA      PIC S9(12)V99.         \n014910             15 HOLD-TDA-ACTCP-P-A-DT      PIC 9(08).             \n014912             15 HOLD-TDA-ACTCP-N-A-DT      PIC 9(08).             \n014914             15 HOLD-TDA-ACTCP-P-DT        PIC 9(08).             \n014916             15 HOLD-TDA-ACTCP-N-DT        PIC 9(08).             \n014918             15 HOLD-TDA-ACTCP-BAL         PIC S9(12)V99.         \n014920                                                                  \n014922         10  HOLD-TDA-ACTS-ACCT-STMT.                             \n014924             15 HOLD-TDA-ACTS-F-N-DT       PIC 9(08).             \n014926             15 HOLD-TDA-ACTS-T-N-DT       PIC 9(08).             \n014928             15 HOLD-TDA-ACTS-F-L-DT       PIC 9(08).             \n014930             15 HOLD-TDA-ACTS-T-L-DT       PIC 9(08).             \n014932             15 HOLD-TDA-ACTS-F-STD        PIC S9(12)V99.         \n014934             15 HOLD-TDA-ACTS-T-STD        PIC S9(12)V99.         \n014936                                                                  \n014938         10  HOLD-TDA-ACTDB-CMAT.                                 \n014940             15 HOLD-TDA-ACTDB-SERIAL      PIC 9(12).             \n014942             15 HOLD-TDA-ACTDB-ACCR-INT    PIC S9(12)V9(6).       \n014944             15 HOLD-TDA-ACTDB-CMPD-INT    PIC S9(6)V9(4).        \n014946             15 HOLD-TDA-ACTDB-CURR-BAL    PIC S9(12)V9(2).       \n014948             15 HOLD-TDA-ACTDB-PER-DIEM    PIC S9(12)V9(6).       \n014950             15 HOLD-TDA-ACTDB-ANTC-INT    PIC S9(12)V9(2).       \n014952             15 HOLD-TDA-ACTDB-ACCR-DT     PIC 9(8).              \n014954                                                                  \n014956         10  HOLD-TDA-ACTDE-HSA.                                  \n014958             15  HOLD-TDA-ACTDE-DESCR      PIC X(80).             \n014960             15  HOLD-TDA-ACTDE-DESCR-R                           \n014962                 REDEFINES HOLD-TDA-ACTDE-DESCR.                  \n014964                 20  HOLD-TDA-ACTDE-DESCR-1 PIC X(40).            \n014966                 20  HOLD-TDA-ACTDE-DESCR-2 PIC X(40).            \n014968             15  FILLER                    PIC X(40).             \n014970                                                                  \n014972         10  HOLD-TDA-ACTD-DIST-STATUS.                           \n014974             15  HOLD-TDA-ACTD-FUNCTION        PIC 9(1).          \n014976             15  HOLD-TDA-ACTD-AMT-CD          PIC 9(1).          \n014978             15  HOLD-TDA-ACTD-DS-NBR          PIC 9(3).          \n014980             15  HOLD-TDA-ACTD-DS-TYPE         PIC X(2).          \n014982             15  HOLD-TDA-ACTD-AMT             PIC S9(12)V9(2).   \n014984             15  HOLD-TDA-ACTD-NXT-DATE        PIC 9(8).          \n014986                                                                  \n014988         10  HOLD-TDA-ACTDI-DS-IN-PROC.                           \n014990             15  HOLD-TDA-ACTDI-DS-NBR     PIC 9(2).              \n014992             15  HOLD-TDA-ACTDI-HLD-NBR    PIC 9(4).              \n014994             15  HOLD-TDA-ACTDI-CLS-DS     PIC 9(1).              \n014996             15  HOLD-TDA-ACTDI-DS-AMT     PIC S9(12)V9(2).       \n014998             15  HOLD-TDA-ACTDI-PR-AMT     PIC S9(12)V9(2).       \n015000             15  HOLD-TDA-ACTDI-INT-AMT    PIC S9(12)V9(2).       \n015002             15  HOLD-TDA-ACTDI-WH-AMT     PIC S9(12)V9(2).       \n015004             15  HOLD-TDA-ACTDI-ST-AMT     PIC S9(12)V9(2).       \n015006             15  HOLD-TDA-ACTDI-DISP-CD    PIC 9(1).              \n015008             15  HOLD-TDA-ACTDI-T-ACCT     PIC 9(12).             \n015010             15  HOLD-TDA-ACTDI-T-ACCTS    PIC 9(10).             \n015012             15  HOLD-TDA-ACTDI-N-PRC-D    PIC 9(8).              \n015014                                                                  \n015016     05  HOLD-TDAINDXRT.                                          \n015018         10  HOLD-TDAIR-BANK-X.                                   \n015020             15  HOLD-TDAIR-BANK            PIC 9(4).             \n015022         10  HOLD-TDAIR-REGION-X.                                 \n015024             15  HOLD-TDAIR-REGION          PIC 9(2).             \n015026         10  HOLD-TDAIR-INDX-CD-X.                                \n015028             15  HOLD-TDAIR-INDX-CD         PIC 9(2).             \n015030         10  HOLD-TDAIR-EFF-DATE-X.                               \n015032             15  HOLD-TDAIR-EFF-DATE        PIC 9(8).             \n015034         10  HOLD-TDAIR-END-DATE-X.                               \n015036             15  HOLD-TDAIR-END-DATE        PIC 9(8).             \n015038         10  HOLD-TDAIR-VOID-DATE-X.                              \n015040             15  HOLD-TDAIR-VOID-DATE       PIC 9(8).             \n015042         10  HOLD-TDAIR-ADD-DATE-X.                               \n015044             15  HOLD-TDAIR-ADD-DATE        PIC 9(8).             \n015046         10  HOLD-TDAIR-ADD-TIME-X.                               \n015048             15  HOLD-TDAIR-ADD-TIME        PIC 9(8).             \n015050         10  HOLD-TDAIR-PUB-ID              PIC X(8).             \n015052         10  HOLD-TDAIR-VOID-PUB-ID         PIC X(8).             \n015054         10  HOLD-TDAIR-DESC                PIC X(20).            \n015056         10  HOLD-TDAIR-RATE-X.                                   \n015058             15  HOLD-TDAIR-RATE            PIC S9(2)V9(3).       \n015060                                                                  \n015062     05  HOLD-TDAMARGRT.                                          \n015064         10  HOLD-TDAMR-BANK-X.                                   \n015066             15  HOLD-TDAMR-BANK            PIC 9(4).             \n015068         10  HOLD-TDAMR-REGION-X.                                 \n015070             15  HOLD-TDAMR-REGION          PIC 9(2).             \n015072         10  HOLD-TDAMR-MARG-CD-X.                                \n015074             15  HOLD-TDAMR-MARG-CD         PIC 9(2).             \n015076         10  HOLD-TDAMR-EFF-DATE-X.                               \n015078             15  HOLD-TDAMR-EFF-DATE        PIC 9(8).             \n015080         10  HOLD-TDAMR-END-DATE-X.                               \n015082             15  HOLD-TDAMR-END-DATE        PIC 9(8).             \n015084         10  HOLD-TDAMR-VOID-DATE-X.                              \n015086             15  HOLD-TDAMR-VOID-DATE       PIC 9(8).             \n015088         10  HOLD-TDAMR-ADD-DATE-X.                               \n015090             15  HOLD-TDAMR-ADD-DATE        PIC 9(8).             \n015092         10  HOLD-TDAMR-ADD-TIME-X.                               \n015094             15  HOLD-TDAMR-ADD-TIME        PIC 9(8).             \n015096         10  HOLD-TDAMR-PUB-ID              PIC X(8).             \n015098         10  HOLD-TDAMR-VOID-PUB-ID         PIC X(8).             \n015100         10  HOLD-TDAMR-DESC                PIC X(20).            \n015102         10  HOLD-TDAMR-RATE-X.                                   \n015104             15  HOLD-TDAMR-RATE            PIC S9(2)V9(3).       \n015106                                                                  \n015108     05  HOLD-TDATIERRT.                                          \n015110         10  HOLD-TDATR-BANK-X.                                   \n015112             15  HOLD-TDATR-BANK            PIC 9(4).             \n015114         10  HOLD-TDATR-REGION-X.                                 \n015116             15  HOLD-TDATR-REGION          PIC 9(2).             \n015118         10  HOLD-TDATR-TIER-CD-X.                                \n015120             15  HOLD-TDATR-TIER-CD         PIC 9(2).             \n015122         10  HOLD-TDATR-EFF-DATE-X.                               \n015124             15  HOLD-TDATR-EFF-DATE        PIC 9(8).             \n015126         10  HOLD-TDATR-END-DATE-X.                               \n015128             15  HOLD-TDATR-END-DATE        PIC 9(8).             \n015130         10  HOLD-TDATR-VOID-DATE-X.                              \n015132             15  HOLD-TDATR-VOID-DATE       PIC 9(8).             \n015134         10  HOLD-TDATR-ADD-DATE-X.                               \n015136             15  HOLD-TDATR-ADD-DATE        PIC 9(8).             \n015138         10  HOLD-TDATR-ADD-TIME-X.                               \n015140             15  HOLD-TDATR-ADD-TIME        PIC 9(8).             \n015142         10  HOLD-TDATR-PUB-ID              PIC X(8).             \n015144         10  HOLD-TDATR-VOID-PUB-ID         PIC X(8).             \n015146         10  HOLD-TDATR-DESC                PIC X(20).            \n015148         10  HOLD-TDATR-TIER-INCR1-X.                             \n015150             15  HOLD-TDATR-TIER-INCR1      PIC S9(2)V9(3).       \n015152         10  HOLD-TDATR-TIER-BAL1-X.                              \n015154             15  HOLD-TDATR-TIER-BAL1       PIC S9(12)V9(2).      \n015156         10  HOLD-TDATR-TIER-INCR2-X.                             \n015158             15  HOLD-TDATR-TIER-INCR2      PIC S9(2)V9(3).       \n015160         10  HOLD-TDATR-TIER-BAL2-X.                              \n015162             15  HOLD-TDATR-TIER-BAL2       PIC S9(12)V9(2).      \n015164         10  HOLD-TDATR-TIER-INCR3-X.                             \n015166             15  HOLD-TDATR-TIER-INCR3      PIC S9(2)V9(3).       \n015168         10  HOLD-TDATR-TIER-BAL3-X.                              \n015170             15  HOLD-TDATR-TIER-BAL3       PIC S9(12)V9(2).      \n015172         10  HOLD-TDATR-TIER-INCR4-X.                             \n015174             15  HOLD-TDATR-TIER-INCR4      PIC S9(2)V9(3).       \n015176         10  HOLD-TDATR-TIER-BAL4-X.                              \n015178             15  HOLD-TDATR-TIER-BAL4       PIC S9(12)V9(2).      \n015180         10  HOLD-TDATR-TIER-INCR5-X.                             \n015182             15  HOLD-TDATR-TIER-INCR5      PIC S9(2)V9(3).       \n015184         10  HOLD-TDATR-TIER-BAL5-X.                              \n015186             15  HOLD-TDATR-TIER-BAL5       PIC S9(12)V9(2).      \n015188         10  HOLD-TDATR-TIER-INCR6-X.                             \n015190             15  HOLD-TDATR-TIER-INCR6      PIC S9(2)V9(3).       \n015192         10  HOLD-TDATR-TIER-BAL6-X.                              \n015194             15  HOLD-TDATR-TIER-BAL6       PIC S9(12)V9(2).      \n015196         10  HOLD-TDATR-TIER-INCR7-X.                             \n015198             15  HOLD-TDATR-TIER-INCR7      PIC S9(2)V9(3).       \n015200         10  HOLD-TDATR-TIER-BAL7-X.                              \n015202             15  HOLD-TDATR-TIER-BAL7       PIC S9(12)V9(2).      \n015204         10  HOLD-TDATR-TIER-INCR8-X.                             \n015206             15  HOLD-TDATR-TIER-INCR8      PIC S9(2)V9(3).       \n015208         10  HOLD-TDATR-TIER-BAL8-X.                              \n015210             15  HOLD-TDATR-TIER-BAL8       PIC S9(12)V9(2).      \n015212         10  HOLD-TDATR-TIER-INCR9-X.                             \n015214             15  HOLD-TDATR-TIER-INCR9      PIC S9(2)V9(3).       \n015216         10  HOLD-TDATR-TIER-BAL9-X.                              \n015218             15  HOLD-TDATR-TIER-BAL9       PIC S9(12)V9(2).      \n015220         10  HOLD-TDATR-TIER-INCR10-X.                            \n015222             15  HOLD-TDATR-TIER-INCR10     PIC S9(2)V9(3).       \n015224         10  HOLD-TDATR-TIER-BAL10-X.                             \n015226             15  HOLD-TDATR-TIER-BAL10      PIC S9(12)V9(2).      \n015228         10  HOLD-TDATR-TIER-INCR11-X.                            \n015230             15  HOLD-TDATR-TIER-INCR11     PIC S9(2)V9(3).       \n015232         10  HOLD-TDATR-TIER-BAL11-X.                             \n015234             15  HOLD-TDATR-TIER-BAL11      PIC S9(12)V9(2).      \n015236         10  HOLD-TDATR-TIER-INCR12-X.                            \n015238             15  HOLD-TDATR-TIER-INCR12     PIC S9(2)V9(3).       \n015240         10  HOLD-TDATR-TIER-BAL12-X.                             \n015242             15  HOLD-TDATR-TIER-BAL12      PIC S9(12)V9(2).      \n015244         10  HOLD-TDATR-TIER-INCR13-X.                            \n015246             15  HOLD-TDATR-TIER-INCR13     PIC S9(2)V9(3).       \n015248         10  HOLD-TDATR-TIER-BAL13-X.                             \n015250             15  HOLD-TDATR-TIER-BAL13      PIC S9(12)V9(2).      \n015252         10  HOLD-TDATR-TIER-INCR14-X.                            \n015254             15  HOLD-TDATR-TIER-INCR14     PIC S9(2)V9(3).       \n015256         10  HOLD-TDATR-TIER-BAL14-X.                             \n015258             15  HOLD-TDATR-TIER-BAL14      PIC S9(12)V9(2).      \n015260         10  HOLD-TDATR-TIER-INCR15-X.                            \n015262             15  HOLD-TDATR-TIER-INCR15     PIC S9(2)V9(3).       \n015264         10  HOLD-TDATR-TIER-BAL15-X.                             \n015266             15  HOLD-TDATR-TIER-BAL15      PIC S9(12)V9(2).      \n015268                                                                  \n015270     05  HOLD-TDARISERT.                                          \n015272         10  HOLD-TDARR-BANK-X.                                   \n015274             15  HOLD-TDARR-BANK            PIC 9(4).             \n015276         10  HOLD-TDARR-REGION-X.                                 \n015278             15  HOLD-TDARR-REGION          PIC 9(2).             \n015280         10  HOLD-TDARR-RISE-CD-X.                                \n015282             15  HOLD-TDARR-RISE-CD         PIC 9(2).             \n015284         10  HOLD-TDARR-EFF-DATE-X.                               \n015286             15  HOLD-TDARR-EFF-DATE        PIC 9(8).             \n015288         10  HOLD-TDARR-END-DATE-X.                               \n015290             15  HOLD-TDARR-END-DATE        PIC 9(8).             \n015292         10  HOLD-TDARR-VOID-DATE-X.                              \n015294             15  HOLD-TDARR-VOID-DATE       PIC 9(8).             \n015296         10  HOLD-TDARR-ADD-DATE-X.                               \n015298             15  HOLD-TDARR-ADD-DATE        PIC 9(8).             \n015300         10  HOLD-TDARR-ADD-TIME-X.                               \n015302             15  HOLD-TDARR-ADD-TIME        PIC 9(8).             \n015304         10  HOLD-TDARR-PUB-ID              PIC X(8).             \n015306         10  HOLD-TDARR-VOID-PUB-ID         PIC X(8).             \n015308         10  HOLD-TDARR-DESC                PIC X(20).            \n015310         10  HOLD-TDARR-FRQ-TYPE-X.                               \n015312             15  HOLD-TDARR-FRQ-TYPE        PIC 9(1).             \n015314         10  HOLD-TDARR-CYC-FRQ1-X.                               \n015316             15  HOLD-TDARR-CYC-FRQ1        PIC 9(3).             \n015318         10  HOLD-TDARR-CYC-INC1-X.                               \n015320             15  HOLD-TDARR-CYC-INC1        PIC S9(2)V9(3).       \n015322         10  HOLD-TDARR-CYC-FRQ2-X.                               \n015324             15  HOLD-TDARR-CYC-FRQ2        PIC 9(3).             \n015326         10  HOLD-TDARR-CYC-INC2-X.                               \n015328             15  HOLD-TDARR-CYC-INC2        PIC S9(2)V9(3).       \n015330         10  HOLD-TDARR-CYC-FRQ3-X.                               \n015332             15  HOLD-TDARR-CYC-FRQ3        PIC 9(3).             \n015334         10  HOLD-TDARR-CYC-INC3-X.                               \n015336             15  HOLD-TDARR-CYC-INC3        PIC S9(2)V9(3).       \n015338         10  HOLD-TDARR-CYC-FRQ4-X.                               \n015340             15  HOLD-TDARR-CYC-FRQ4        PIC 9(3).             \n015342         10  HOLD-TDARR-CYC-INC4-X.                               \n015344             15  HOLD-TDARR-CYC-INC4        PIC S9(2)V9(3).       \n015346         10  HOLD-TDARR-CYC-FRQ5-X.                               \n015348             15  HOLD-TDARR-CYC-FRQ5        PIC 9(3).             \n015350         10  HOLD-TDARR-CYC-INC5-X.                               \n015352             15  HOLD-TDARR-CYC-INC5        PIC S9(2)V9(3).       \n015354         10  HOLD-TDARR-CYC-FRQ6-X.                               \n015356             15  HOLD-TDARR-CYC-FRQ6        PIC 9(3).             \n015358         10  HOLD-TDARR-CYC-INC6-X.                               \n015360             15  HOLD-TDARR-CYC-INC6        PIC S9(2)V9(3).       \n015362         10  HOLD-TDARR-CYC-FRQ7-X.                               \n015364             15  HOLD-TDARR-CYC-FRQ7        PIC 9(3).             \n015366         10  HOLD-TDARR-CYC-INC7-X.                               \n015368             15  HOLD-TDARR-CYC-INC7        PIC S9(2)V9(3).       \n015370         10  HOLD-TDARR-CYC-FRQ8-X.                               \n015372             15  HOLD-TDARR-CYC-FRQ8        PIC 9(3).             \n015374         10  HOLD-TDARR-CYC-INC8-X.                               \n015376             15  HOLD-TDARR-CYC-INC8        PIC S9(2)V9(3).       \n015378         10  HOLD-TDARR-CYC-FRQ9-X.                               \n015380             15  HOLD-TDARR-CYC-FRQ9        PIC 9(3).             \n015382         10  HOLD-TDARR-CYC-INC9-X.                               \n015384             15  HOLD-TDARR-CYC-INC9        PIC S9(2)V9(3).       \n015386         10  HOLD-TDARR-CYC-FRQ10-X.                              \n015388             15  HOLD-TDARR-CYC-FRQ10       PIC 9(3).             \n015390         10  HOLD-TDARR-CYC-INC10-X.                              \n015392             15  HOLD-TDARR-CYC-INC10       PIC S9(2)V9(3).       \n015394                                                                  \n015396     05  HOLD-TDATOTAL.                                           \n015398         10  HOLD-TDATT-BANK-X.                                   \n015400             15  HOLD-TDATT-BANK           PIC 9(4).              \n015402         10  HOLD-TDATT-REGION-X.                                 \n015404             15  HOLD-TDATT-REGION         PIC 9(2).              \n015406         10  HOLD-TDATT-TOTAL-CD-X.                               \n015408             15  HOLD-TDATT-TOTAL-CD       PIC 999.               \n015410         10  HOLD-TDATT-APPL-X.                                   \n015412             15  HOLD-TDATT-APPL           PIC 9.                 \n015414         10  HOLD-TDATT-VOID-DATE-X.                              \n015416             15  HOLD-TDATT-VOID-DATE      PIC 9(8).              \n015418         10  HOLD-TDATT-ADD-DATE-X.                               \n015420             15  HOLD-TDATT-ADD-DATE       PIC 9(8).              \n015422         10  HOLD-TDATT-ADD-TIME-X.                               \n015424             15  HOLD-TDATT-ADD-TIME       PIC 9(8).              \n015426         10  HOLD-TDATT-PUB-ID             PIC X(8).              \n015428         10  HOLD-TDATT-VOID-PUB-ID        PIC X(8).              \n015430         10  HOLD-TDATT-DESC               PIC X(30).             \n015432         10  HOLD-TDATT-RENEW-CD-X.                               \n015434             15  HOLD-TDATT-RENEW-CD       PIC 9(1).              \n015436         10  HOLD-TDATT-OVERRIDE-X.                               \n015438             15  HOLD-TDATT-OVERRIDE       PIC 9(1).              \n015440         10  HOLD-TDATT-REN-NTC-X.                                \n015442             15  HOLD-TDATT-REN-NTC        PIC 9(1).              \n015444         10  HOLD-TDATT-PMAT-NTC-X.                               \n015446             15  HOLD-TDATT-PMAT-NTC       PIC 9(1).              \n015448         10  HOLD-TDATT-RTCHG-NTC-X.                              \n015450             15  HOLD-TDATT-RTCHG-NTC      PIC 9(1).              \n015452         10  HOLD-TDATT-INT-NTC-X.                                \n015454             15  HOLD-TDATT-INT-NTC        PIC 9(1).              \n015456         10  HOLD-TDATT-YIELD-NUM-X.                              \n015458             15  HOLD-TDATT-YIELD-NUM      PIC 9(3).              \n015460         10  HOLD-TDATT-YIELD-DENOM-X.                            \n015462             15  HOLD-TDATT-YIELD-DENOM    PIC 9(3).              \n015464         10  HOLD-TDATT-CMPD-FREQ-X.                              \n015466             15  HOLD-TDATT-CMPD-FREQ      PIC 9(1).              \n015468         10  HOLD-TDATT-CMPD-NTRVL-X.                             \n015470             15  HOLD-TDATT-CMPD-NTRVL     PIC 9(4).              \n015472         10  HOLD-TDATT-RTCHG-LIMIT-X.                            \n015474             15  HOLD-TDATT-RTCHG-LIMIT    PIC 9(1).              \n015476         10  HOLD-TDATT-CHG-NTRVL-X.                              \n015478             15  HOLD-TDATT-CHG-NTRVL      PIC 9(3).              \n015480         10  HOLD-TDATT-PENALTY-CD-X.                             \n015482             15  HOLD-TDATT-PENALTY-CD     PIC 999.               \n015484         10  HOLD-TDATT-MAT-TYPE-X.                               \n015486             15  HOLD-TDATT-MAT-TYPE       PIC 9(1).              \n015488         10  HOLD-TDATT-MAT-TERM-X.                               \n015490             15  HOLD-TDATT-MAT-TERM       PIC 9(4).              \n015492         10  HOLD-TDATT-PAY-FREQ-X.                               \n015494             15  HOLD-TDATT-PAY-FREQ       PIC 9(1).              \n015496         10  HOLD-TDATT-PAY-NTRVL-X.                              \n015498             15  HOLD-TDATT-PAY-NTRVL      PIC 9(4).              \n015500         10  HOLD-TDATT-STMT-FREQ-X.                              \n015502             15  HOLD-TDATT-STMT-FREQ      PIC 9(1).              \n015504         10  HOLD-TDATT-STMT-NTRVL-X.                             \n015506             15  HOLD-TDATT-STMT-NTRVL     PIC 9(4).              \n015508         10  HOLD-TDATT-VAR-IMMED-X.                              \n015510             15  HOLD-TDATT-VAR-IMMED      PIC 9(1).              \n015512         10  HOLD-TDATT-VAR-INT-X.                                \n015514             15  HOLD-TDATT-VAR-INT        PIC 9(1).              \n015516         10  HOLD-TDATT-VAR-STEP-X.                               \n015518             15  HOLD-TDATT-VAR-STEP       PIC 9(1).              \n015520         10  HOLD-TDATT-VAR-SCHED-X.                              \n015522             15  HOLD-TDATT-VAR-SCHED      PIC 9(1).              \n015524         10  HOLD-TDATT-VAR-BAL-X.                                \n015526             15  HOLD-TDATT-VAR-BAL        PIC 9(1).              \n015528         10  HOLD-TDATT-VAR-CUST-X.                               \n015530             15  HOLD-TDATT-VAR-CUST       PIC 9(1).              \n015532         10  HOLD-TDATT-RT-CHG-ALOW-X.                            \n015534             15  HOLD-TDATT-RT-CHG-ALOW    PIC 9(1).              \n015536         10  HOLD-TDATT-WTHDRW-ALOW-X.                            \n015538             15  HOLD-TDATT-WTHDRW-ALOW    PIC 9(1).              \n015540         10  HOLD-TDATT-DPOSIT-ALOW-X.                            \n015542             15  HOLD-TDATT-DPOSIT-ALOW    PIC 9(1).              \n015544         10  HOLD-TDATT-ODD-PAYMENT-X.                            \n015546             15  HOLD-TDATT-ODD-PAYMENT    PIC 9(1).              \n015548         10  HOLD-TDATT-IGL-GRP-X.                                \n015550             15  HOLD-TDATT-IGL-GRP        PIC 9(2).              \n015552         10  HOLD-TDATT-POST-MAT-X.                               \n015554             15  HOLD-TDATT-POST-MAT       PIC 9(1).              \n015556         10  HOLD-TDATT-END-OF-MAT-X.                             \n015558             15  HOLD-TDATT-END-OF-MAT     PIC 9(1).              \n015560         10  HOLD-TDATT-END-OF-INT-X.                             \n015562             15  HOLD-TDATT-END-OF-INT     PIC 9(1).              \n015564         10  HOLD-TDATT-END-OF-STMT-X.                            \n015566             15  HOLD-TDATT-END-OF-STMT    PIC 9(1).              \n015568         10  HOLD-TDATT-END-OF-CMPD-X.                            \n015570             15  HOLD-TDATT-END-OF-CMPD    PIC 9(1).              \n015572         10  HOLD-TDATT-FLOOR-RT-X.                               \n015574             15  HOLD-TDATT-FLOOR-RT       PIC 99V999.            \n015576         10  HOLD-TDATT-FLOOR-INCR-X.                             \n015578             15  HOLD-TDATT-FLOOR-INCR     PIC 99V999.            \n015580         10  HOLD-TDATT-CHG-NTC-X.                                \n015582             15  HOLD-TDATT-CHG-NTC        PIC 9(1).              \n015584         10  HOLD-TDATT-IRA-BACKED-X.                             \n015586             15  HOLD-TDATT-IRA-BACKED     PIC 9(1).              \n015588         10  HOLD-TDATT-SAV-DEPOSIT        PIC 9(1).              \n015590         10  HOLD-TDATT-LEVEL-PAY-X.                              \n015592             15  HOLD-TDATT-LEVEL-PAY      PIC 9.                 \n015594         10  HOLD-TDATT-CAP-RT-CHG         PIC X.                 \n015596         10  HOLD-TDATT-FEE-FREQ-X.                               \n015598             15  HOLD-TDATT-FEE-FREQ       PIC 9.                 \n015600         10  HOLD-TDATT-FEE-NTRVL-X.                              \n015602             15  HOLD-TDATT-FEE-NTRVL      PIC 9(4).              \n015604         10  HOLD-TDATT-FEE-AMT-X.                                \n015606             15  HOLD-TDATT-FEE-AMT        PIC S9(12)V99.         \n015608         10  HOLD-TDATT-END-OF-FEE-X.                             \n015610             15  HOLD-TDATT-END-OF-FEE     PIC 9.                 \n015612         10  HOLD-TDATT-ZERO-RT-ALLOW-X.                          \n015614             15  HOLD-TDATT-ZERO-RT-ALLOW  PIC 9.                 \n015616         10  HOLD-TDATT-RC-MAT-ONLY        PIC 9(1).              \n015618         10  HOLD-TDATT-CLS-ON-MAT         PIC 9(1).              \n015620         10  HOLD-TDATT-GRACE-DAYS         PIC 9(2).              \n015622         10  HOLD-TDATT-IGL-GRP-2          PIC 9(2).              \n015624                                                                  \n015626     05  HOLD-TDAHMS.                                             \n015628         10  HOLD-TDAHMS-BANK              PIC  9(4).             \n015630         10  HOLD-TDAHMS-APPL              PIC  9(1).             \n015632         10  HOLD-TDAHMS-CUST              PIC  9(12).            \n015634         10  HOLD-TDAHMS-ACCT              PIC  9(10).            \n015636         10  HOLD-TDAHMS-TYPE              PIC  X(1).             \n015638         10  HOLD-TDAHMS-BK-TYPE           PIC  X(1).             \n015640         10  HOLD-TDAHMS-DR-CR-IND         PIC  X(1).             \n015642         10  HOLD-TDAHMS-SOURCE            PIC  9(2).             \n015644         10  HOLD-TDAHMS-HOLD-NBR          PIC  9(4).             \n015646         10  HOLD-TDAHMS-AMT               PIC S9(12)V99.         \n015648         10  HOLD-TDAHMS-ORIG-AMT          PIC  9(12)V99.         \n015650         10  HOLD-TDAHMS-COMMENT           PIC  X(40).            \n015652         10  HOLD-TDAHMS-PUB-ID            PIC  X(8).             \n015654         10  HOLD-TDAHMS-VD-PUB-ID         PIC  X(8).             \n015656         10  HOLD-TDAHMS-ADD-DATE          PIC  9(8).             \n015658         10  HOLD-TDAHMS-ADD-TIME          PIC  9(8).             \n015660         10  HOLD-TDAHMS-VOID-DATE         PIC  9(8).             \n015662         10  HOLD-TDAHMS-PLG-ACCT          PIC  9(12).            \n015664         10  HOLD-TDAHMS-PLG-ACCT-S        PIC  9(10).            \n015666         10  HOLD-TDAHMS-EXPIRE-DT         PIC  9(8).             \n015668         10  HOLD-TDAHMS-AVAIL-BAL         PIC S9(12)V99.         \n015670         10  HOLD-TDAHMS-SERIAL-NUM        PIC  9(10).            \n015672         10  HOLD-TDAHMS-END-SERIAL        PIC  9(10).            \n015674         10  HOLD-TDAHMS-NAME              PIC  X(10).            \n015676         10  HOLD-TDAHMS-START-DATE        PIC  9(8).             \n015678         10  HOLD-TDAHMS-DAILY-ACCR        PIC S9(12)V9(6).       \n015680         10  HOLD-TDAHMS-ORG-ADD-DT        PIC  9(8).             \n015682         10  HOLD-TDAHMS-ORG-ADD-TM        PIC  9(8).             \n015684         10  HOLD-TDAHMS-ORG-PUB-ID        PIC  X(8).             \n015686         10  HOLD-TDAHMS-AMT-LAST-UPD      PIC S9(12)V9(2).       \n015688         10  HOLD-TDAHMS-DATE-LAST-UPD     PIC  9(8).             \n015690                                                                  \n015692     05  HOLD-TDABENEF.                                           \n015694         10  HOLD-TDAB-BANK                PIC 9(04).             \n015696         10  HOLD-TDAB-CUST                PIC 9(12).             \n015698         10  HOLD-TDAB-ACCT                PIC 9(10).             \n015700         10  HOLD-TDAB-BENEF-NBR           PIC 9(02).             \n015702         10  HOLD-TDAB-NAME                PIC X(40).             \n015704         10  HOLD-TDAB-NAME-2              PIC X(40).             \n015706         10  HOLD-TDAB-NAME-3              PIC X(40).             \n015708         10  HOLD-TDAB-ADDR-1              PIC X(40).             \n015710         10  HOLD-TDAB-ADDR-2              PIC X(40).             \n015712         10  HOLD-TDAB-CITY                PIC X(40).             \n015714         10  HOLD-TDAB-STATE               PIC X(02).             \n015716         10  HOLD-TDAB-PROVINCE            PIC X(02).             \n015718         10  HOLD-TDAB-COUNTRY             PIC X(02).             \n015720         10  HOLD-TDAB-ZIP-CODE.                                  \n015722             15  HOLD-TDAB-ZIP             PIC 9(05).             \n015724             15  HOLD-TDAB-ZIP-4           PIC 9(04).             \n015726         10  HOLD-TDAB-PHONE               PIC 9(10).             \n015728         10  HOLD-TDAB-TIN                 PIC 9(09).             \n015730         10  HOLD-TDAB-BIRTH-DT            PIC 9(08).             \n015732         10  HOLD-TDAB-RELATION            PIC 9(01).             \n015734         10  HOLD-TDAB-DESIGNATION         PIC 9(01).             \n015736         10  HOLD-TDAB-PERCENT             PIC 9(03).             \n015738         10  HOLD-TDAB-FREE-REMARK         PIC X(24).             \n015740                                                                  \n015742     05  HOLD-TDAADDR.                                            \n015744         10  HOLD-TDADR-BANK               PIC 9(04).             \n015746         10  HOLD-TDADR-CUST               PIC 9(12).             \n015748         10  HOLD-TDADR-ACCT               PIC 9(10).             \n015750         10  HOLD-TDADR-ADDR-USAGE         PIC X(01).             \n015752         10  HOLD-TDADR-TEMP-BEG-DT        PIC 9(04).             \n015754         10  HOLD-TDADR-TEMP-END-DT        PIC 9(04).             \n015756         10  HOLD-TDADR-TEMP-EFF-DT        PIC 9(08).             \n015758         10  HOLD-TDADR-TEMP-EXP-DT        PIC 9(08).             \n015760         10  HOLD-TDADR-ADDR-GROUP.                               \n015762             15  HOLD-TDADR-T-ADDR.                               \n015764                 20  HOLD-TDADR-T-ADDR-1   PIC X(40).             \n015766                 20  HOLD-TDADR-T-ADDR-2   PIC X(40).             \n015768                 20  HOLD-TDADR-T-CITY     PIC X(40).             \n015770                 20  HOLD-TDADR-T-STATE    PIC X(02).             \n015772                 20  HOLD-TDADR-T-PROVINCE PIC X(02).             \n015774                 20  HOLD-TDADR-T-COUNTRY  PIC X(02).             \n015776                 20  HOLD-TDADR-T-ZIP-CODE.                       \n015778                     25  HOLD-TDADR-T-ZIP  PIC 9(05).             \n015780                     25  HOLD-TDADR-T-ZIP-4 PIC 9(04).            \n015782                 20  HOLD-TDADR-T-ALIEN-CD PIC 9(01).             \n015784                 20  HOLD-TDADR-T-BAR-CODE PIC 9(03).             \n015786                 20  HOLD-TDADR-T-EMAIL-ADDR PIC X(100).          \n015788                 20  HOLD-TDADR-T-EMAIL-ADDR-R                    \n015790                                REDEFINES HOLD-TDADR-T-EMAIL-ADDR.\n015792                     25  HOLD-TDADR-T-EMAIL-ADDR-1-50   PIC X(50).\n015794                     25  HOLD-TDADR-T-EMAIL-ADDR-51-100 PIC X(50).\n015796                 20  HOLD-TDADR-T-MAIL-CD    PIC 9(01).           \n015798                 20  HOLD-TDADR-T-ADDR-KEY   PIC X(28).           \n015800             15  HOLD-TDADR-A-ADDR.                               \n015802                 20  HOLD-TDADR-A-NAME-1          PIC X(40).      \n015804                 20  HOLD-TDADR-A-NAME-AREA-1.                    \n015806                     25  HOLD-TDADR-A-N1-KEY      PIC X(14).      \n015808                     25  HOLD-TDADR-A-N1-FIRST    PIC X(40).      \n015810                     25  HOLD-TDADR-A-N1-MID      PIC X(20).      \n015812                     25  HOLD-TDADR-A-N1-LAST     PIC X(40).      \n015814                     25  HOLD-TDADR-A-N1-PREFIX   PIC X(12).      \n015816                     25  HOLD-TDADR-A-N1-SUFFIX   PIC X(12).      \n015818                     25  HOLD-TDADR-A-N1-FAMILIAR PIC X(20).      \n015820                     25  HOLD-TDADR-A-N1-PRT-PFX  PIC X(01).      \n015822                     25  HOLD-TDADR-A-N1-PRT-SFX  PIC X(01).      \n015824                     25  HOLD-TDADR-A-N1-DESIGNAT PIC X(20).      \n015826                 20  HOLD-TDADR-A-NAME-2          PIC X(40).      \n015828                 20  HOLD-TDADR-A-N2-MODIFIED     PIC X(01).      \n015830                 20  HOLD-TDADR-A-N2-PRINT-CD     PIC X(01).      \n015832                 20  HOLD-TDADR-A-NAME-AREA-2.                    \n015834                     25  HOLD-TDADR-A-N2-KEY      PIC X(14).      \n015836                     25  HOLD-TDADR-A-N2-FIRST    PIC X(40).      \n015838                     25  HOLD-TDADR-A-N2-MID      PIC X(20).      \n015840                     25  HOLD-TDADR-A-N2-LAST     PIC X(40).      \n015842                     25  HOLD-TDADR-A-N2-PREFIX   PIC X(12).      \n015844                     25  HOLD-TDADR-A-N2-SUFFIX   PIC X(12).      \n015846                     25  HOLD-TDADR-A-N2-FAMILIAR PIC X(20).      \n015848                     25  HOLD-TDADR-A-N2-PRT-PFX  PIC X(01).      \n015850                     25  HOLD-TDADR-A-N2-PRT-SFX  PIC X(01).      \n015852                     25  HOLD-TDADR-A-N2-DESIGNAT PIC X(20).      \n015854                 20  HOLD-TDADR-A-NAME-3          PIC X(40).      \n015856                 20  HOLD-TDADR-A-N3-MODIFIED     PIC X(01).      \n015858                 20  HOLD-TDADR-A-N3-PRINT-CD     PIC X(01).      \n015860                 20  HOLD-TDADR-A-NAME-AREA-3.                    \n015862                     25  HOLD-TDADR-A-N3-KEY      PIC X(14).      \n015864                     25  HOLD-TDADR-A-N3-FIRST    PIC X(40).      \n015866                     25  HOLD-TDADR-A-N3-MID      PIC X(20).      \n015868                     25  HOLD-TDADR-A-N3-LAST     PIC X(40).      \n015870                     25  HOLD-TDADR-A-N3-PREFIX   PIC X(12).      \n015872                     25  HOLD-TDADR-A-N3-SUFFIX   PIC X(12).      \n015874                     25  HOLD-TDADR-A-N3-FAMILIAR PIC X(20).      \n015876                     25  HOLD-TDADR-A-N3-PRT-PFX  PIC X(01).      \n015878                     25  HOLD-TDADR-A-N3-PRT-SFX  PIC X(01).      \n015880                     25  HOLD-TDADR-A-N3-DESIGNAT PIC X(20).      \n015882                 20  HOLD-TDADR-A-ADDR-KEY        PIC X(28).      \n015884                 20  HOLD-TDADR-A-ADDR-1   PIC X(40).             \n015886                 20  HOLD-TDADR-A-ADDR-2   PIC X(40).             \n015888                 20  HOLD-TDADR-A-CITY     PIC X(40).             \n015890                 20  HOLD-TDADR-A-STATE    PIC X(02).             \n015892                 20  HOLD-TDADR-A-PROVINCE PIC X(02).             \n015894                 20  HOLD-TDADR-A-COUNTRY  PIC X(02).             \n015896                 20  HOLD-TDADR-A-ZIP-CODE.                       \n015898                     25  HOLD-TDADR-A-ZIP  PIC 9(05).             \n015900                     25  HOLD-TDADR-A-ZIP-4 PIC 9(04).            \n015902                 20  HOLD-TDADR-A-ALIEN-CD PIC 9(01).             \n015904                 20  HOLD-TDADR-A-BAR-CODE PIC 9(03).             \n015906                 20  HOLD-TDADR-A-EMAIL-ADDR PIC X(100).          \n015908                 20  HOLD-TDADR-A-EMAIL-ADDR-R                    \n015910                                REDEFINES HOLD-TDADR-A-EMAIL-ADDR.\n015912                     25  HOLD-TDADR-A-EMAIL-ADDR-1-50   PIC X(50).\n015914                     25  HOLD-TDADR-A-EMAIL-ADDR-51-100 PIC X(50).\n015916                 20  HOLD-TDADR-A-MAIL-CD      PIC 9(01).         \n015918         10  HOLD-TDADR-SHT-NAME           PIC X(20).             \n015920         10  HOLD-TDADR-LUPD-DATE          PIC 9(08).             \n015922         10  HOLD-TDADR-LUPD-TIME          PIC 9(08).             \n015924         10  HOLD-TDADR-PUB-ID             PIC X(08).             \n015926         10  HOLD-TDADR-TIN-CD             PIC X.                 \n015928         10  HOLD-TDADR-TIN-NBR            PIC 9(9).              \n015930         10  HOLD-TDADR-TIN-CERT-CD        PIC 9.                 \n015932         10  HOLD-TDADR-TIN-CD-2           PIC X(01).             \n015934         10  HOLD-TDADR-TIN-NBR-2          PIC 9(09).             \n015936         10  HOLD-TDADR-TIN-CT-CD-2        PIC 9(01).             \n015938         10  HOLD-TDADR-TIN-CD-3           PIC X(01).             \n015940         10  HOLD-TDADR-TIN-NBR-3          PIC 9(09).             \n015942         10  HOLD-TDADR-TIN-CT-CD-3        PIC 9(01).             \n015944                                                                  \n015946     05  HOLD-TDAPENALTY.                                         \n015948         10  HOLD-TDAP-BANK                PIC 9(4).              \n015950         10  HOLD-TDAP-ROUTINE             PIC 999.               \n015952         10  HOLD-TDAP-STEP-NBR            PIC 9(2).              \n015954         10  HOLD-TDAP-FUNC                PIC X(1).              \n015956         10  HOLD-TDAP-ADD-DATE            PIC 9(8).              \n015958         10  HOLD-TDAP-ADD-TIME            PIC 9(8).              \n015960         10  HOLD-TDAP-PUB-ID              PIC X(8).              \n015962         10  HOLD-TDAP-VOID-PUB-ID         PIC X(8).              \n015964         10  HOLD-TDAP-VOID-DATE           PIC 9(8).              \n015966         10  HOLD-TDAP-DATE                PIC 9(8).              \n015968         10  HOLD-TDAP-DAYS                PIC 9(4).              \n015970         10  HOLD-TDAP-MONTHS              PIC 9(4).              \n015972         10  HOLD-TDAP-PERCENT             PIC 9(2)V9(2).         \n015974         10  HOLD-TDAP-AMOUNT              PIC S9(12)V9(2).       \n015976         10  HOLD-TDAP-USE-INT             PIC 9(1).              \n015978         10  HOLD-TDAP-USE-RED             PIC 9(1).              \n015980         10  HOLD-TDAP-USE-MONTH           PIC 9(1).              \n015982         10  HOLD-TDAP-USE-DAY             PIC 9(1).              \n015984         10  HOLD-TDAP-USE-AVL-INT         PIC 9(1).              \n015986                                                                  \n015988     05  HOLD-TDAPCR.                                             \n015990         10  HOLD-TDAPC-APPL               PIC X(03).             \n015992         10  HOLD-TDAPC-TYPE               PIC 9(1).              \n015994         10  HOLD-TDAPC-BANK               PIC 9(04).             \n015996         10  HOLD-TDAPC-RPT-NBR            PIC 9(04).             \n015998         10  HOLD-TDAPC-CSI-ONLY           PIC X(01).             \n016000         10  HOLD-TDAPC-RPT-DESC           PIC X(40).             \n016002         10  HOLD-TDAPC-SPECS              PIC X(65).             \n016004         10  HOLD-TDAPC-COPIES             PIC 9(02).             \n016006         10  HOLD-TDAPC-LASER-PRT          PIC 9(02).             \n016008         10  HOLD-TDAPC-FICHE-PRT          PIC 9(02).             \n016010         10  HOLD-TDAPC-OPTICAL            PIC 9(02).             \n016012         10  HOLD-TDAPC-PRT-DLY            PIC X(01).             \n016014         10  HOLD-TDAPC-DLY-IND            PIC X(07).             \n016016         10  HOLD-TDAPC-LST-PRT-D          PIC 9(08).             \n016018         10  HOLD-TDAPC-PRT-WK             PIC X(01).             \n016020         10  HOLD-TDAPC-WK-IND             PIC X(07).             \n016022         10  HOLD-TDAPC-LST-PRT-W          PIC 9(08).             \n016024         10  HOLD-TDAPC-PRT-MTH            PIC X(01).             \n016026         10  HOLD-TDAPC-LST-DAY-M          PIC X(01).             \n016028         10  HOLD-TDAPC-NXT-PRT-M          PIC 9(08).             \n016030         10  HOLD-TDAPC-LST-PRT-M          PIC 9(08).             \n016032         10  HOLD-TDAPC-PRT-QTR            PIC X(01).             \n016034         10  HOLD-TDAPC-LST-DAY-Q          PIC X(01).             \n016036         10  HOLD-TDAPC-NXT-PRT-Q          PIC 9(08).             \n016038         10  HOLD-TDAPC-LST-PRT-Q          PIC 9(08).             \n016040         10  HOLD-TDAPC-PRT-YR             PIC X(01).             \n016042         10  HOLD-TDAPC-NXT-PRT-Y          PIC 9(08).             \n016044         10  HOLD-TDAPC-LST-PRT-Y          PIC 9(08).             \n016046         10  HOLD-TDAPC-SPECL-REQ          PIC X(01).             \n016048         10  HOLD-TDAPC-PRT-DAY            PIC 9(08).             \n016050         10  HOLD-TDAPC-BEGIN-DATE         PIC 9(06).             \n016052         10  HOLD-TDAPC-END-DATE           PIC 9(06).             \n016054         10  HOLD-TDAPC-PRINTER            PIC X(17).             \n016056         10  HOLD-TDAPC-SPECL-SPECS        PIC X(65).             \n016058         10  HOLD-TDAPC-REQUESTOR          PIC X(08).             \n016060         10  HOLD-TDAPC-LPROCESS-DT        PIC 9(16).             \n016062         10  HOLD-TDAPC-LUPD-DT            PIC 9(08).             \n016064         10  HOLD-TDAPC-LUPD-TM            PIC 9(06).             \n016066         10  HOLD-TDAPC-BP-LAST-RUN        PIC 9(16).             \n016068         10  HOLD-TDAPC-PUB-ID             PIC X(08).             \n016070         10  HOLD-TDAPC-BANK-SPECS         PIC X(300).            \n016072         10  HOLD-TDAPC-BANK-SPECS-R REDEFINES                    \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    936 lines from 7097 to 8032.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 16, "total_chunks": 55, "start_line": 7097, "end_line": 8032, "line_count": 936}

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
- Source code length: 73282 characters

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
CHUNK 16 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 7097 to 8032 (936 lines)
Chunk Tokens (estimated): ~19,904
Actual Input Tokens: 21,310 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 7097-8032 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 16 of 55 chunks
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
      The source code below is only CHUNK 16 of 55.


=============================================================================
CHUNK 16 SOURCE CODE (Lines 7097-8032)
=============================================================================

```cobol
014202                         HOLD-TDAA-MANUAL-RT-X.                   
014204                 20  HOLD-TDAA-MANUAL-RT  PIC 9(2)V9(3).          
014206                                                                  
014208     05  HOLD-TDAIRA.                                             
014210         10  HOLD-TDAI-BANK             PIC 9(4).                 
014212         10  HOLD-TDAI-BRCH             PIC 9(4).                 
014214         10  HOLD-TDAI-APPL             PIC 9(1).                 
014216         10  HOLD-TDAI-CUST             PIC 9(12).                
014218         10  HOLD-TDAI-ACCT             PIC 9(10).                
014220         10  HOLD-TDAI-PUB-ID           PIC X(8).                 
014222         10  HOLD-TDAI-ADD-DT           PIC 9(8).                 
014224         10  HOLD-TDAI-ADD-TM           PIC 9(6).                 
014226         10  HOLD-TDAI-DS-TYPE          PIC X(2)                  
014228                          OCCURS 20 TIMES.                        
014230         10  HOLD-TDAI-CN-TYPE          PIC 9(2)                  
014232                          OCCURS 20 TIMES.                        
014234         10  HOLD-TDAI-DS-CN-AMT        PIC S9(12)V99             
014236                          OCCURS 20 TIMES.                        
014238         10  HOLD-TDAI-DS-PEN-AMT       PIC S9(12)V99             
014240                          OCCURS 20 TIMES.                        
014242         10  HOLD-TDAI-DS-WTHLD-AMT     PIC S9(12)V99             
014244                          OCCURS 20 TIMES.                        
014246         10  HOLD-TDAI-DS-ST-WH-AMT     PIC S9(12)V99             
014248                          OCCURS 20 TIMES.                        
014250         10  HOLD-TDAI-DS-EXC-EARN      PIC S9(12)V9(2)           
014252                          OCCURS 20 TIMES.                        
014254         10  HOLD-TDAI-DS-C-YTD-CNT     PIC 9(5).                 
014256         10  HOLD-TDAI-DS-P-YTD-CNT     PIC 9(5).                 
014258         10  HOLD-TDAI-DS-AMT-C-YTD     PIC S9(12)V9(2).          
014260         10  HOLD-TDAI-DS-AMT-P-YTD     PIC S9(12)V9(2).          
014262         10  HOLD-TDAI-DS-INT-AMT       PIC S9(12)V9(2).          
014264         10  HOLD-TDAI-CN-YTD-CNT       PIC 9(5).                 
014266         10  HOLD-TDAI-CN-YTD-AMT       PIC S9(12)V9(2).          
014268         10  HOLD-TDAI-CN-LYTD-AMT      PIC S9(12)V9(2).          
014270         10  HOLD-TDAI-EMP-CONT-LYR     PIC S9(12)V9(2).          
014272         10  HOLD-TDAI-REG-CONT-LYR     PIC S9(12)V9(2).          
014274         10  HOLD-TDAI-UNINSURED        PIC X(1).                 
014276         10  HOLD-TDAI-ROLLOVER         PIC S9(12)V9(2).          
014278         10  HOLD-TDAI-ROLLOVER-LYR     PIC S9(12)V9(2).          
014280         10  HOLD-TDAI-TRANSFER-IN      PIC S9(12)V9(2).          
014282         10  HOLD-TDAI-TRANSFER-OUT     PIC S9(12)V9(2).          
014284         10  HOLD-TDAI-1ST-CN-DATE      PIC 9(8).                 
014286         10  HOLD-TDAI-BASIS-C-LTD      PIC S9(12)V99.            
014288         10  HOLD-TDAI-BASIS-D-LTD      PIC S9(12)V99.            
014290         10  HOLD-TDAI-BASIS-D-YTD      PIC S9(12)V99.            
014292         10  HOLD-TDAI-EXTRA-FIELDS.                              
014294             15  HOLD-TDAI-CN-TYPE-EX   PIC 9(2).                 
014296             15  HOLD-TDAI-DS-TYPE-EX.                            
014298               20  HOLD-TDAI-DS-TYPE-EX-1       PIC X.            
014300               20  HOLD-TDAI-DS-TYPE-EX-2       PIC X.            
014302                                                                  
014304      05 HOLD-TDADISTR.                                           
014306         10 HOLD-TDAD-BANK                      PIC 9(04).        
014308         10 HOLD-TDAD-BRCH                      PIC 9(04).        
014310         10 HOLD-TDAD-APPL                      PIC 9(01).        
014312         10 HOLD-TDAD-CUST                      PIC 9(12).        
014314         10 HOLD-TDAD-ACCT                      PIC 9(10).        
014316         10 HOLD-TDAD-NXT-ACCT-P                PIC 9(10).        
014318         10 HOLD-TDAD-NXT-ACCT-S                PIC 9(10).        
014320         10 HOLD-TDAD-N-ACCT-BY-RT              PIC 9(1).         
014322         10 HOLD-TDAD-SERIAL                    PIC 9(12).        
014324         10 HOLD-TDAD-SER-NEXT                  PIC 9(12).        
014326         10 HOLD-TDAD-DISP-CD                   PIC 9(01).        
014328         10 HOLD-TDAD-TYPE                      PIC X(02).        
014330         10 HOLD-TDAD-PRINCIPAL                 PIC 9(01).        
014332         10 HOLD-TDAD-INTEREST                  PIC 9(01).        
014334         10 HOLD-TDAD-DS-CODE                   PIC 9(01).        
014336         10 HOLD-TDAD-WTHLD-CD                  PIC 9(01).        
014338         10 HOLD-TDAD-WHLD-AMT                  PIC S9(12)V99.    
014340         10 HOLD-TDAD-ST-WHLD-CD                PIC 9(01).        
014342         10 HOLD-TDAD-ST-WHLD-AMT               PIC S9(12)V99.    
014344         10 HOLD-TDAD-TRF-ACCT                  PIC 9(12).        
014346         10 HOLD-TDAD-TRF-ACCT-S                PIC 9(10).        
014348         10 HOLD-TDAD-AMT-CD                    PIC 9(01).        
014350         10 HOLD-TDAD-DS-AMT                    PIC S9(12)V99.    
014352         10 HOLD-TDAD-DS-FREQ                   PIC 9(01).        
014354         10 HOLD-TDAD-DS-NTRVL                  PIC 9(04).        
014356         10 HOLD-TDAD-END-OF-DIST               PIC 9(1).         
014358         10 HOLD-TDAD-DIST-NTC-CD               PIC 9(01).        
014360         10 HOLD-TDAD-EOY-DS-FORM               PIC 9(01).        
014362         10 HOLD-TDAD-5-YR-RULE                 PIC 9(01).        
014364         10 HOLD-TDAD-ANUAL-RECALC              PIC 9(01).        
014366         10 HOLD-TDAD-JOINT-CD                  PIC 9(01).        
014368         10 HOLD-TDAD-PUB-ID                    PIC X(08).        
014370         10 HOLD-TDAD-LST-DIST-DT               PIC 9(8).         
014372         10 HOLD-TDAD-IN-PROC-DT                PIC 9(8).         
014374         10 HOLD-TDAD-NXT-DIST-DT               PIC 9(8).         
014376         10 HOLD-TDAD-NXT-DS-PROC               PIC 9(8).         
014378         10 HOLD-TDAD-ADD-DT                    PIC 9(08).        
014380         10 HOLD-TDAD-ADD-TM                    PIC 9(08).        
014382                                                                  
014384         10 HOLD-TDAD-MIN-AMT                   PIC S9(12)V99.    
014386         10 HOLD-TDAD-AMT                       PIC S9(12)V99.    
014388         10 HOLD-TDAD-LST-AMT                   PIC S9(12)V99.    
014390         10 HOLD-TDAD-CUR-WHLD-AMT              PIC S9(12)V99.    
014392         10 HOLD-TDAD-WHLD-YTD                  PIC S9(12)V99.    
014394         10 HOLD-TDAD-LST-WHLD-AMT              PIC S9(12)V99.    
014396         10 HOLD-TDAD-PRINCPL-AMT               PIC S9(12)V99.    
014398         10 HOLD-TDAD-INT-AMT                   PIC S9(12)V99.    
014400         10 HOLD-TDAD-INT-YTD                   PIC S9(12)V99.    
014402         10 HOLD-TDAD-ST-CUR-W-AMT              PIC S9(12)V99.    
014404         10 HOLD-TDAD-ST-LST-W-AMT              PIC S9(12)V99.    
014406         10 HOLD-TDAD-CK-IND-1                  PIC X(1).         
014408         10 HOLD-TDAD-CK-IND-2                  PIC X(1).         
014410         10 HOLD-TDAD-LUPD-DT                   PIC 9(8).         
014412         10 HOLD-TDAD-LUPD-TM                   PIC 9(6).         
014414         10 HOLD-TDAD-RMD-OVERRIDE              PIC 9.            
014416         10 HOLD-TDAD-RMD-AMOUNT                PIC S9(12)V9(2).  
014418         10 HOLD-TDAD-DS-NBR                    PIC 9(2).         
014420         10 HOLD-TDAD-NONDB-FIELDS.                               
014422             15  HOLD-TDAI-DS-NTC-TYPE          PIC 9(1).         
014424                                                                  
014426     05  HOLD-TDAACTV.                                            
014428         10  HOLD-TDA-ACTV-BANK         PIC 9(4).                 
014430         10  HOLD-TDA-ACTV-BRCH         PIC 9(4).                 
014432         10  HOLD-TDA-ACTV-APPL         PIC 9(1).                 
014434         10  HOLD-TDA-ACTV-CUST         PIC 9(12).                
014436         10  HOLD-TDA-ACTV-ACCT         PIC 9(10).                
014438         10  HOLD-TDA-ACTV-TOT-CD       PIC 9(3).                 
014440         10  HOLD-TDA-ACTV-IGL-GRP      PIC 9(2).                 
014442         10  HOLD-TDA-ACTV-OFFICER      PIC X(3).                 
014444         10  HOLD-TDA-ACTV-NC-INDC      PIC 9(1).                 
014446         10  HOLD-TDA-ACTV-PROC-FG      PIC 9(1).                 
014448         10  HOLD-TDA-ACTV-TYPE         PIC 9(4).                 
014450         10  HOLD-TDA-ACTV-EFF-DT       PIC 9(8).                 
014452         10  HOLD-TDA-ACTV-DATE         PIC 9(8).                 
014454         10  HOLD-TDA-ACTV-MAINT        PIC 9(8).                 
014456         10  HOLD-TDA-ACTV-TIME         PIC 9(8).                 
014458         10  HOLD-TDA-ACTV-SEQ-NBR      PIC 9(2).                 
014460         10  HOLD-TDA-ACTV-SERIAL       PIC 9(12).                
014462         10  HOLD-TDA-ACTV-SOURCE       PIC 9(2).                 
014464         10  HOLD-TDA-ACTV-ERASED       PIC 9(1).                 
014466         10  HOLD-TDA-ACTV-DR-CR        PIC 9(1).                 
014468         10  HOLD-TDA-ACTV-E-PUBID      PIC X(8).                 
014470         10  HOLD-TDA-ACTV-PUB-ID       PIC X(8).                 
014472         10  HOLD-TDA-ACTV-SUB          PIC 9(3).                 
014474                                                                  
014476         10  HOLD-TDA-ACTVT-MONETARY.                             
014478             15  HOLD-TDA-ACTVT-CODE       PIC 9(3).              
014480             15  HOLD-TDA-ACTVT-AMT        PIC S9(12)V9(2).       
014482             15  HOLD-TDA-ACTVT-DESC       PIC X(80).             
014484             15  HOLD-TDA-ACTVT-DESC-R                            
014486                 REDEFINES HOLD-TDA-ACTVT-DESC.                   
014488                 20  HOLD-TDA-ACTVT-DESC-1 PIC X(40).             
014490                 20  HOLD-TDA-ACTVT-DESC-2 PIC X(40).             
014492             15  HOLD-TDA-ACTVT-UNPOST     PIC 9(1).              
014494             15  HOLD-TDA-ACTVT-RATE       PIC 9(2)V999.          
014496             15  HOLD-TDA-ACTVT-YIELD      PIC 9(2)V999.          
014498             15  HOLD-TDA-ACTVT-P-DIEM     PIC S9(12)V9(6).       
014500             15  HOLD-TDA-ACTVT-WTHLD      PIC S9(12)V9(2).       
014502             15  HOLD-TDA-ACTVT-PENLTY     PIC S9(12)V9(2).       
014504             15  HOLD-TDA-ACTVT-EX-EARN    PIC S9(12)V9(2).       
014506             15  HOLD-TDA-ACTVT-DS-TYPE.                          
014508               20 HOLD-TDA-ACTVT-DS-TYPE-1 PIC X.                 
014510               20 HOLD-TDA-ACTVT-DS-TYPE-2 PIC X.                 
014512             15  HOLD-TDA-ACTVT-CN-CUST    PIC 9(12).             
014514             15  HOLD-TDA-ACTVT-CN-TYPE    PIC 9(2).              
014516             15  HOLD-TDA-ACTVT-ST-WHLD    PIC S9(12)V9(2).       
014518             15  HOLD-TDA-ACTVT-NEW-BAL    PIC S9(12)V9(2).       
014520             15  HOLD-TDA-ACTVT-CHK-NBR    PIC 9(10).             
014522             15  HOLD-TDA-ACTVT-SEQ-NBR    PIC 9(16).             
014524             15  HOLD-TDA-ACTVT-PRIDAY     PIC X.                 
014526             15  HOLD-TDA-ACTVT-INT-COR    PIC 9(1).              
014528             15  HOLD-TDA-ACTVT-DISP-CD    PIC 9(1).              
014530             15  HOLD-TDA-ACTVT-QRP-ROL    PIC 9(1).              
014532                                                                  
014534         10  HOLD-TDA-ACTVC-CHANGE.                               
014536             15  HOLD-TDA-ACTVC-CODE       PIC 9(4).              
014538             15  HOLD-TDA-ACTVC-EXCPT      PIC 9(3).              
014540             15  HOLD-TDA-ACTVC-CHG-FRM    PIC X(40).             
014542             15  HOLD-TDA-ACTVC-CHG-TO     PIC X(40).             
014544             15  HOLD-TDA-ACTVC-NCREOPN    PIC 9(1).              
014546             15  HOLD-TDA-ACTVC-DDN        PIC 9(10).             
014548             15  HOLD-TDA-ACTVC-TMPLATE    PIC 9(4).              
014550                                                                  
014552         10  HOLD-TDA-ACTMT-MAT.                                  
014554             15  HOLD-TDA-ACTMT-LMAT-DT    PIC 9(08).             
014556             15  HOLD-TDA-ACTMT-NMAT-DT    PIC 9(08).             
014558             15  HOLD-TDA-ACTMT-PMAT-DT    PIC 9(08).             
014560             15  HOLD-TDA-ACTMT-TOTL-CD    PIC 9(03).             
014562                                                                  
014564         10  HOLD-TDA-ACTCL-CALC.                                 
014566             15  HOLD-TDA-ACTCL-P-DIEM     PIC S9(12)V9(6).       
014568             15  HOLD-TDA-ACTCL-N-DIEM     PIC S9(12)V9(6).       
014570             15  HOLD-TDA-ACTCL-P-ACCR     PIC S9(12)V9(6).       
014572             15  HOLD-TDA-ACTCL-N-ACCR     PIC S9(12)V9(6).       
014574             15  HOLD-TDA-ACTCL-P-ACRDT    PIC 9(8).              
014576             15  HOLD-TDA-ACTCL-N-ACRDT    PIC 9(8).              
014578             15  HOLD-TDA-ACTCL-P-WTHLD    PIC S9(12)V99.         
014580             15  HOLD-TDA-ACTCL-N-WTHLD    PIC S9(12)V99.         
014582             15  HOLD-TDA-ACTCL-P-PENAL    PIC S9(12)V99.         
014584             15  HOLD-TDA-ACTCL-N-PENAL    PIC S9(12)V99.         
014586             15  HOLD-TDA-ACTCL-P-PAYOF    PIC S9(12)V99.         
014588             15  HOLD-TDA-ACTCL-N-PAYOF    PIC S9(12)V99.         
014590             15  HOLD-TDA-ACTCL-ST-P-WD    PIC S9(12)V99.         
014592             15  HOLD-TDA-ACTCL-ST-N-WD    PIC S9(12)V99.         
014594                                                                  
014596         10  HOLD-TDA-ACTHT-HIST.                                 
014598             15  HOLD-TDA-ACTHT-DATE       PIC 9(8).              
014600             15  HOLD-TDA-ACTHT-CODE       PIC 9(4).              
014602             15  HOLD-TDA-ACTHT-AMOUNT     PIC S9(12)V99.         
014604             15  HOLD-TDA-ACTHT-TAX-AMT    PIC S9(12)V99.         
014606             15  HOLD-TDA-ACTHT-FM-RATE    PIC S99V999.           
014608             15  HOLD-TDA-ACTHT-FM-DESC    PIC X(26).             
014610                                                                  
014612         10  HOLD-TDA-ACTVN-NEW.                                  
014614             15  HOLD-TDA-ACTVN-STR-NBR    PIC 9(2).              
014616             15  HOLD-TDA-ACTVN-PUR-AMT    PIC S9(12)V99.         
014618             15  HOLD-TDA-ACTVN-BASE-RT    PIC S9(2)V9(3).        
014620             15  HOLD-TDA-ACTVN-RT-IND     PIC X(1).              
014622             15  HOLD-TDA-ACTVN-TYPE       PIC 9(2).              
014624                                                                  
014626         10  HOLD-TDA-ACTVR-RATES.                                
014628             15  HOLD-TDA-ACTVR-CUR-RT     PIC S99V999.           
014630             15  HOLD-TDA-ACTVR-F-L-RT     PIC S99V999.           
014632             15  HOLD-TDA-ACTVR-T-L-RT     PIC S99V999.           
014634             15  HOLD-TDA-ACTVR-F-Y-RT     PIC S99V999.           
014636             15  HOLD-TDA-ACTVR-T-Y-RT     PIC S99V999.           
014638             15  HOLD-TDA-ACTVR-F-L-DT     PIC 9(08).             
014640             15  HOLD-TDA-ACTVR-T-L-DT     PIC 9(08).             
014642             15  HOLD-TDA-ACTVR-F-RCYC     PIC 9(02).             
014644             15  HOLD-TDA-ACTVR-T-RCYC     PIC 9(02).             
014646             15  HOLD-TDA-ACTVR-PRS-DT     PIC 9(08).             
014648             15  HOLD-TDA-ACTVR-RT-IND     PIC X.                 
014650                                                                  
014652         10  HOLD-TDA-ACTRR-RATES.                                
014654             15  HOLD-TDA-ACTRR-F-RG       PIC 9(2).              
014656             15  HOLD-TDA-ACTRR-T-RG       PIC 9(2).              
014658             15  HOLD-TDA-ACTRR-F-CD       PIC 9(2).              
014660             15  HOLD-TDA-ACTRR-T-CD       PIC 9(2).              
014662             15  HOLD-TDA-ACTRR-F-RT       PIC S99V999            
014664                                           OCCURS 10 TIMES.       
014666             15  HOLD-TDA-ACTRR-T-RT       PIC S99V999            
014668                                           OCCURS 10 TIMES.       
014670             15  HOLD-TDA-ACTRR-F-DT       PIC 9(08)              
014672                                           OCCURS 10 TIMES.       
014674             15  HOLD-TDA-ACTRR-T-DT       PIC 9(08)              
014676                                           OCCURS 10 TIMES.       
014678                                                                  
014680         10  HOLD-TDA-ACTVI-INTEREST.                             
014682             15  HOLD-TDA-ACTVI-F-INT      PIC S9(12)V9(6).       
014684             15  HOLD-TDA-ACTVI-T-INT      PIC S9(12)V9(6).       
014686             15  HOLD-TDA-ACTVI-F-INTA     PIC S9(12)V99.         
014688             15  HOLD-TDA-ACTVI-T-INTA     PIC S9(12)V99.         
014690             15  HOLD-TDA-ACTVI-F-PDAY     PIC S9(12)V9(6).       
014692             15  HOLD-TDA-ACTVI-T-PDAY     PIC S9(12)V9(6).       
014694             15  HOLD-TDA-ACTVI-RD-DT      PIC 9(08).             
014696                                                                  
014698         10  HOLD-TDA-ACTCK-CHECK.                                
014700             15 HOLD-TDA-ACTCK-F-I-PT      PIC S9(12)V99.         
014702             15 HOLD-TDA-ACTCK-T-I-PT      PIC S9(12)V99.         
014704             15 HOLD-TDA-ACTCK-F-C-WA      PIC S9(12)V99.         
014706             15 HOLD-TDA-ACTCK-T-C-WA      PIC S9(12)V99.         
014708             15 HOLD-TDA-ACTCK-F-STAT      PIC X.                 
014710             15 HOLD-TDA-ACTCK-T-STAT      PIC X.                 
014712             15 HOLD-TDA-ACTCK-PRS-DT      PIC 9(08).             
014714             15 HOLD-TDA-ACTCK-F-ST-WA     PIC S9(12)V99.         
014716             15 HOLD-TDA-ACTCK-T-ST-WA     PIC S9(12)V99.         
014718                                                                  
014720         10  HOLD-TDA-ACTWH-WITHHOLD.                             
014722             15 HOLD-TDA-ACTWH-F-YTD       PIC S9(12)V99.         
014724             15 HOLD-TDA-ACTWH-T-YTD       PIC S9(12)V99.         
014726             15 HOLD-TDA-ACTWH-F-STD       PIC S9(12)V99.         
014728             15 HOLD-TDA-ACTWH-T-STD       PIC S9(12)V99.         
014730             15 HOLD-TDA-ACTWH-F-L-AMT     PIC S9(12)V99.         
014732             15 HOLD-TDA-ACTWH-T-L-AMT     PIC S9(12)V99.         
014734                                                                  
014736         10  HOLD-TDA-ACTPT-INT-POST.                             
014738             15 HOLD-TDA-ACTPT-F-IP-L      PIC S9(12)V99.         
014740             15 HOLD-TDA-ACTPT-T-IP-L      PIC S9(12)V99.         
014742             15 HOLD-TDA-ACTPT-F-1099      PIC S9(12)V99.         
014744             15 HOLD-TDA-ACTPT-T-1099      PIC S9(12)V99.         
014746             15 HOLD-TDA-ACTPT-F-C-BL      PIC S9(12)V99.         
014748             15 HOLD-TDA-ACTPT-T-C-BL      PIC S9(12)V99.         
014750             15 HOLD-TDA-ACTPT-F-L-DT      PIC 9(08).             
014752             15 HOLD-TDA-ACTPT-T-L-DT      PIC 9(08).             
014754             15 HOLD-TDA-ACTPT-F-N-DT      PIC 9(08).             
014756             15 HOLD-TDA-ACTPT-T-N-DT      PIC 9(08).             
014758             15 HOLD-TDA-ACTPT-F-I-PT      PIC S9(12)V99.         
014760             15 HOLD-TDA-ACTPT-T-I-PT      PIC S9(12)V99.         
014762             15 HOLD-TDA-ACTPT-F-C-WA      PIC S9(12)V99.         
014764             15 HOLD-TDA-ACTPT-T-C-WA      PIC S9(12)V99.         
014766             15 HOLD-TDA-ACTPT-F-ACCR      PIC S9(12)V9(06).      
014768             15 HOLD-TDA-ACTPT-T-ACCR      PIC S9(12)V9(06).      
014770             15 HOLD-TDA-ACTPT-F-STAT      PIC X(01).             
014772             15 HOLD-TDA-ACTPT-T-STAT      PIC X(01).             
014774             15 HOLD-TDA-ACTPT-F-A-DT      PIC 9(08).             
014776             15 HOLD-TDA-ACTPT-T-A-DT      PIC 9(08).             
014778             15 HOLD-TDA-ACTPT-F-PDAY      PIC S9(12)V9(6).       
014780             15 HOLD-TDA-ACTPT-T-PDAY      PIC S9(12)V9(6).       
014782             15 HOLD-TDA-ACTPT-N-INT       PIC S9(12)V99.         
014784             15 HOLD-TDA-ACTPT-C-INT       PIC S9(12)V99.         
014786             15 HOLD-TDA-ACTPT-DISP-CD     PIC 9(01).             
014788             15 HOLD-TDA-ACTPT-INT-ACCT    PIC 9(12).             
014790             15 HOLD-TDA-ACTPT-INT-ACCT-S  PIC 9(10).             
014792             15 HOLD-TDA-ACTPT-F-ST-WA     PIC S9(12)V9(2).       
014794             15 HOLD-TDA-ACTPT-T-ST-WA     PIC S9(12)V9(2).       
014796             15 HOLD-TDA-ACTPT-NEW-BAL     PIC S9(9)V99.          
014798             15 HOLD-TDA-ACTPT-CLO-MAT     PIC 9.                 
014800                                                                  
014802         10  HOLD-TDA-ACTAC-CLOSE-ACCT.                           
014804             15 HOLD-TDA-ACTAC-AMT         PIC S9(12)V9(2).       
014806             15 HOLD-TDA-ACTAC-INT         PIC S9(12)V9(2).       
014808             15 HOLD-TDA-ACTAC-PENLTY      PIC S9(12)V9(2).       
014810             15 HOLD-TDA-ACTAC-WTHLD       PIC S9(12)V9(2).       
014812             15 HOLD-TDA-ACTAC-LST-INT     PIC S9(12)V9(2).       
014814             15 HOLD-TDA-ACTAC-W-ALLOW     PIC 9(1).              
014816             15 HOLD-TDA-ACTAC-D-ALLOW     PIC 9(1).              
014818             15 HOLD-TDA-ACTAC-CUR-PEN     PIC S9(12)V9(2).       
014820             15 HOLD-TDA-ACTAC-AVL-BAL     PIC S9(12)V9(2).       
014822             15 HOLD-TDA-ACTAC-DS-TYPE     PIC X(2).              
014824             15 HOLD-TDA-ACTAC-ST-WHLD     PIC S9(12)V9(2).       
014826             15 HOLD-TDA-ACTAC-DRP-INT     PIC S9(12)V99.         
014828             15 HOLD-TDA-ACTAC-DS-DISP     PIC 9.                 
014830             15 HOLD-TDA-ACTAC-CLO-MAT     PIC 9.                 
014832             15 HOLD-TDA-ACTAC-T-ACCT      PIC 9(12).             
014834             15 HOLD-TDA-ACTAC-T-ACCTS     PIC 9(10).             
014836             15 HOLD-TDA-ACTAC-DS-CODE     PIC 9(1).              
014838             15 HOLD-TDA-ACTAC-DS-NBR      PIC 9(2).              
014840             15 HOLD-TDA-ACTAC-DESC        PIC X(30).             
014842                                                                  
014844         10  HOLD-TDA-ACTDS-DISTRIBUTE.                           
014846             15 HOLD-TDA-ACTDS-TYPE        PIC XX.                
014848             15 HOLD-TDA-ACTDS-DISP-CD     PIC 9.                 
014850             15 HOLD-TDA-ACTDS-INT         PIC 9.                 
014852             15 HOLD-TDA-ACTDS-PRNCPAL     PIC 9.                 
014854             15 HOLD-TDA-ACTDS-CD          PIC 9.                 
014856             15 HOLD-TDA-ACTDS-NXT-DT      PIC 9(8).              
014858             15 HOLD-TDA-ACTDS-W-AMT       PIC S9(12)V99.         
014860             15 HOLD-TDA-ACTDS-W-CD        PIC 9.                 
014862             15 HOLD-TDA-ACTDS-AMT         PIC S9(12)V99.         
014864             15 HOLD-TDA-ACTDS-FREQ        PIC 9.                 
014866             15 HOLD-TDA-ACTDS-NTRVL       PIC 9(4).              
014868             15 HOLD-TDA-ACTDS-T-ACCT      PIC 9(12).             
014870             15 HOLD-TDA-ACTDS-T-ACCTS     PIC 9(10).             
014872             15 HOLD-TDA-ACTDS-ST-WAMT     PIC S9(12)V99.         
014874             15 HOLD-TDA-ACTDS-ST-W-CD     PIC 9(01).             
014876             15 HOLD-TDA-ACTDS-NEW-BAL     PIC S9(12)V99.         
014878             15 HOLD-TDA-ACTDS-DS-NBR      PIC 9(2).              
014880                                                                  
014882         10  HOLD-TDA-ACTE-ERASER.                                
014884             15 HOLD-TDA-ACTE-SERIAL       PIC 9(12).             
014886             15 HOLD-TDA-ACTE-TYPE         PIC 99.                
014888             15 HOLD-TDA-ACTE-EFF-DT       PIC 9(8).              
014890             15 HOLD-TDA-ACTE-DATE         PIC 9(8).              
014892             15 HOLD-TDA-ACTE-SEQ-NBR      PIC 99.                
014894                                                                  
014896         10  HOLD-TDA-ACTCP-COMPOUND.                             
014898             15 HOLD-TDA-ACTCP-P-INT       PIC S9(12)V9(6).       
014900             15 HOLD-TDA-ACTCP-N-INT       PIC S9(12)V9(6).       
014902             15 HOLD-TDA-ACTCP-P-PDAY      PIC S9(12)V9(6).       
014904             15 HOLD-TDA-ACTCP-N-PDAY      PIC S9(12)V9(6).       
014906             15 HOLD-TDA-ACTCP-P-INTA      PIC S9(12)V99.         
014908             15 HOLD-TDA-ACTCP-N-INTA      PIC S9(12)V99.         
014910             15 HOLD-TDA-ACTCP-P-A-DT      PIC 9(08).             
014912             15 HOLD-TDA-ACTCP-N-A-DT      PIC 9(08).             
014914             15 HOLD-TDA-ACTCP-P-DT        PIC 9(08).             
014916             15 HOLD-TDA-ACTCP-N-DT        PIC 9(08).             
014918             15 HOLD-TDA-ACTCP-BAL         PIC S9(12)V99.         
014920                                                                  
014922         10  HOLD-TDA-ACTS-ACCT-STMT.                             
014924             15 HOLD-TDA-ACTS-F-N-DT       PIC 9(08).             
014926             15 HOLD-TDA-ACTS-T-N-DT       PIC 9(08).             
014928             15 HOLD-TDA-ACTS-F-L-DT       PIC 9(08).             
014930             15 HOLD-TDA-ACTS-T-L-DT       PIC 9(08).             
014932             15 HOLD-TDA-ACTS-F-STD        PIC S9(12)V99.         
014934             15 HOLD-TDA-ACTS-T-STD        PIC S9(12)V99.         
014936                                                                  
014938         10  HOLD-TDA-ACTDB-CMAT.                                 
014940             15 HOLD-TDA-ACTDB-SERIAL      PIC 9(12).             
014942             15 HOLD-TDA-ACTDB-ACCR-INT    PIC S9(12)V9(6).       
014944             15 HOLD-TDA-ACTDB-CMPD-INT    PIC S9(6)V9(4).        
014946             15 HOLD-TDA-ACTDB-CURR-BAL    PIC S9(12)V9(2).       
014948             15 HOLD-TDA-ACTDB-PER-DIEM    PIC S9(12)V9(6).       
014950             15 HOLD-TDA-ACTDB-ANTC-INT    PIC S9(12)V9(2).       
014952             15 HOLD-TDA-ACTDB-ACCR-DT     PIC 9(8).              
014954                                                                  
014956         10  HOLD-TDA-ACTDE-HSA.                                  
014958             15  HOLD-TDA-ACTDE-DESCR      PIC X(80).             
014960             15  HOLD-TDA-ACTDE-DESCR-R                           
014962                 REDEFINES HOLD-TDA-ACTDE-DESCR.                  
014964                 20  HOLD-TDA-ACTDE-DESCR-1 PIC X(40).            
014966                 20  HOLD-TDA-ACTDE-DESCR-2 PIC X(40).            
014968             15  FILLER                    PIC X(40).             
014970                                                                  
014972         10  HOLD-TDA-ACTD-DIST-STATUS.                           
014974             15  HOLD-TDA-ACTD-FUNCTION        PIC 9(1).          
014976             15  HOLD-TDA-ACTD-AMT-CD          PIC 9(1).          
014978             15  HOLD-TDA-ACTD-DS-NBR          PIC 9(3).          
014980             15  HOLD-TDA-ACTD-DS-TYPE         PIC X(2).          
014982             15  HOLD-TDA-ACTD-AMT             PIC S9(12)V9(2).   
014984             15  HOLD-TDA-ACTD-NXT-DATE        PIC 9(8).          
014986                                                                  
014988         10  HOLD-TDA-ACTDI-DS-IN-PROC.                           
014990             15  HOLD-TDA-ACTDI-DS-NBR     PIC 9(2).              
014992             15  HOLD-TDA-ACTDI-HLD-NBR    PIC 9(4).              
014994             15  HOLD-TDA-ACTDI-CLS-DS     PIC 9(1).              
014996             15  HOLD-TDA-ACTDI-DS-AMT     PIC S9(12)V9(2).       
014998             15  HOLD-TDA-ACTDI-PR-AMT     PIC S9(12)V9(2).       
015000             15  HOLD-TDA-ACTDI-INT-AMT    PIC S9(12)V9(2).       
015002             15  HOLD-TDA-ACTDI-WH-AMT     PIC S9(12)V9(2).       
015004             15  HOLD-TDA-ACTDI-ST-AMT     PIC S9(12)V9(2).       
015006             15  HOLD-TDA-ACTDI-DISP-CD    PIC 9(1).              
015008             15  HOLD-TDA-ACTDI-T-ACCT     PIC 9(12).             
015010             15  HOLD-TDA-ACTDI-T-ACCTS    PIC 9(10).             
015012             15  HOLD-TDA-ACTDI-N-PRC-D    PIC 9(8).              
015014                                                                  
015016     05  HOLD-TDAINDXRT.                                          
015018         10  HOLD-TDAIR-BANK-X.                                   
015020             15  HOLD-TDAIR-BANK            PIC 9(4).             
015022         10  HOLD-TDAIR-REGION-X.                                 
015024             15  HOLD-TDAIR-REGION          PIC 9(2).             
015026         10  HOLD-TDAIR-INDX-CD-X.                                
015028             15  HOLD-TDAIR-INDX-CD         PIC 9(2).             
015030         10  HOLD-TDAIR-EFF-DATE-X.                               
015032             15  HOLD-TDAIR-EFF-DATE        PIC 9(8).             
015034         10  HOLD-TDAIR-END-DATE-X.                               
015036             15  HOLD-TDAIR-END-DATE        PIC 9(8).             
015038         10  HOLD-TDAIR-VOID-DATE-X.                              
015040             15  HOLD-TDAIR-VOID-DATE       PIC 9(8).             
015042         10  HOLD-TDAIR-ADD-DATE-X.                               
015044             15  HOLD-TDAIR-ADD-DATE        PIC 9(8).             
015046         10  HOLD-TDAIR-ADD-TIME-X.                               
015048             15  HOLD-TDAIR-ADD-TIME        PIC 9(8).             
015050         10  HOLD-TDAIR-PUB-ID              PIC X(8).             
015052         10  HOLD-TDAIR-VOID-PUB-ID         PIC X(8).             
015054         10  HOLD-TDAIR-DESC                PIC X(20).            
015056         10  HOLD-TDAIR-RATE-X.                                   
015058             15  HOLD-TDAIR-RATE            PIC S9(2)V9(3).       
015060                                                                  
015062     05  HOLD-TDAMARGRT.                                          
015064         10  HOLD-TDAMR-BANK-X.                                   
015066             15  HOLD-TDAMR-BANK            PIC 9(4).             
015068         10  HOLD-TDAMR-REGION-X.                                 
015070             15  HOLD-TDAMR-REGION          PIC 9(2).             
015072         10  HOLD-TDAMR-MARG-CD-X.                                
015074             15  HOLD-TDAMR-MARG-CD         PIC 9(2).             
015076         10  HOLD-TDAMR-EFF-DATE-X.                               
015078             15  HOLD-TDAMR-EFF-DATE        PIC 9(8).             
015080         10  HOLD-TDAMR-END-DATE-X.                               
015082             15  HOLD-TDAMR-END-DATE        PIC 9(8).             
015084         10  HOLD-TDAMR-VOID-DATE-X.                              
015086             15  HOLD-TDAMR-VOID-DATE       PIC 9(8).             
015088         10  HOLD-TDAMR-ADD-DATE-X.                               
015090             15  HOLD-TDAMR-ADD-DATE        PIC 9(8).             
015092         10  HOLD-TDAMR-ADD-TIME-X.                               
015094             15  HOLD-TDAMR-ADD-TIME        PIC 9(8).             
015096         10  HOLD-TDAMR-PUB-ID              PIC X(8).             
015098         10  HOLD-TDAMR-VOID-PUB-ID         PIC X(8).             
015100         10  HOLD-TDAMR-DESC                PIC X(20).            
015102         10  HOLD-TDAMR-RATE-X.                                   
015104             15  HOLD-TDAMR-RATE            PIC S9(2)V9(3).       
015106                                                                  
015108     05  HOLD-TDATIERRT.                                          
015110         10  HOLD-TDATR-BANK-X.                                   
015112             15  HOLD-TDATR-BANK            PIC 9(4).             
015114         10  HOLD-TDATR-REGION-X.                                 
015116             15  HOLD-TDATR-REGION          PIC 9(2).             
015118         10  HOLD-TDATR-TIER-CD-X.                                
015120             15  HOLD-TDATR-TIER-CD         PIC 9(2).             
015122         10  HOLD-TDATR-EFF-DATE-X.                               
015124             15  HOLD-TDATR-EFF-DATE        PIC 9(8).             
015126         10  HOLD-TDATR-END-DATE-X.                               
015128             15  HOLD-TDATR-END-DATE        PIC 9(8).             
015130         10  HOLD-TDATR-VOID-DATE-X.                              
015132             15  HOLD-TDATR-VOID-DATE       PIC 9(8).             
015134         10  HOLD-TDATR-ADD-DATE-X.                               
015136             15  HOLD-TDATR-ADD-DATE        PIC 9(8).             
015138         10  HOLD-TDATR-ADD-TIME-X.                               
015140             15  HOLD-TDATR-ADD-TIME        PIC 9(8).             
015142         10  HOLD-TDATR-PUB-ID              PIC X(8).             
015144         10  HOLD-TDATR-VOID-PUB-ID         PIC X(8).             
015146         10  HOLD-TDATR-DESC                PIC X(20).            
015148         10  HOLD-TDATR-TIER-INCR1-X.                             
015150             15  HOLD-TDATR-TIER-INCR1      PIC S9(2)V9(3).       
015152         10  HOLD-TDATR-TIER-BAL1-X.                              
015154             15  HOLD-TDATR-TIER-BAL1       PIC S9(12)V9(2).      
015156         10  HOLD-TDATR-TIER-INCR2-X.                             
015158             15  HOLD-TDATR-TIER-INCR2      PIC S9(2)V9(3).       
015160         10  HOLD-TDATR-TIER-BAL2-X.                              
015162             15  HOLD-TDATR-TIER-BAL2       PIC S9(12)V9(2).      
015164         10  HOLD-TDATR-TIER-INCR3-X.                             
015166             15  HOLD-TDATR-TIER-INCR3      PIC S9(2)V9(3).       
015168         10  HOLD-TDATR-TIER-BAL3-X.                              
015170             15  HOLD-TDATR-TIER-BAL3       PIC S9(12)V9(2).      
015172         10  HOLD-TDATR-TIER-INCR4-X.                             
015174             15  HOLD-TDATR-TIER-INCR4      PIC S9(2)V9(3).       
015176         10  HOLD-TDATR-TIER-BAL4-X.                              
015178             15  HOLD-TDATR-TIER-BAL4       PIC S9(12)V9(2).      
015180         10  HOLD-TDATR-TIER-INCR5-X.                             
015182             15  HOLD-TDATR-TIER-INCR5      PIC S9(2)V9(3).       
015184         10  HOLD-TDATR-TIER-BAL5-X.                              
015186             15  HOLD-TDATR-TIER-BAL5       PIC S9(12)V9(2).      
015188         10  HOLD-TDATR-TIER-INCR6-X.                             
015190             15  HOLD-TDATR-TIER-INCR6      PIC S9(2)V9(3).       
015192         10  HOLD-TDATR-TIER-BAL6-X.                              
015194             15  HOLD-TDATR-TIER-BAL6       PIC S9(12)V9(2).      
015196         10  HOLD-TDATR-TIER-INCR7-X.                             
015198             15  HOLD-TDATR-TIER-INCR7      PIC S9(2)V9(3).       
015200         10  HOLD-TDATR-TIER-BAL7-X.                              
015202             15  HOLD-TDATR-TIER-BAL7       PIC S9(12)V9(2).      
015204         10  HOLD-TDATR-TIER-INCR8-X.                             
015206             15  HOLD-TDATR-TIER-INCR8      PIC S9(2)V9(3).       
015208         10  HOLD-TDATR-TIER-BAL8-X.                              
015210             15  HOLD-TDATR-TIER-BAL8       PIC S9(12)V9(2).      
015212         10  HOLD-TDATR-TIER-INCR9-X.                             
015214             15  HOLD-TDATR-TIER-INCR9      PIC S9(2)V9(3).       
015216         10  HOLD-TDATR-TIER-BAL9-X.                              
015218             15  HOLD-TDATR-TIER-BAL9       PIC S9(12)V9(2).      
015220         10  HOLD-TDATR-TIER-INCR10-X.                            
015222             15  HOLD-TDATR-TIER-INCR10     PIC S9(2)V9(3).       
015224         10  HOLD-TDATR-TIER-BAL10-X.                             
015226             15  HOLD-TDATR-TIER-BAL10      PIC S9(12)V9(2).      
015228         10  HOLD-TDATR-TIER-INCR11-X.                            
015230             15  HOLD-TDATR-TIER-INCR11     PIC S9(2)V9(3).       
015232         10  HOLD-TDATR-TIER-BAL11-X.                             
015234             15  HOLD-TDATR-TIER-BAL11      PIC S9(12)V9(2).      
015236         10  HOLD-TDATR-TIER-INCR12-X.                            
015238             15  HOLD-TDATR-TIER-INCR12     PIC S9(2)V9(3).       
015240         10  HOLD-TDATR-TIER-BAL12-X.                             
015242             15  HOLD-TDATR-TIER-BAL12      PIC S9(12)V9(2).      
015244         10  HOLD-TDATR-TIER-INCR13-X.                            
015246             15  HOLD-TDATR-TIER-INCR13     PIC S9(2)V9(3).       
015248         10  HOLD-TDATR-TIER-BAL13-X.                             
015250             15  HOLD-TDATR-TIER-BAL13      PIC S9(12)V9(2).      
015252         10  HOLD-TDATR-TIER-INCR14-X.                            
015254             15  HOLD-TDATR-TIER-INCR14     PIC S9(2)V9(3).       
015256         10  HOLD-TDATR-TIER-BAL14-X.                             
015258             15  HOLD-TDATR-TIER-BAL14      PIC S9(12)V9(2).      
015260         10  HOLD-TDATR-TIER-INCR15-X.                            
015262             15  HOLD-TDATR-TIER-INCR15     PIC S9(2)V9(3).       
015264         10  HOLD-TDATR-TIER-BAL15-X.                             
015266             15  HOLD-TDATR-TIER-BAL15      PIC S9(12)V9(2).      
015268                                                                  
015270     05  HOLD-TDARISERT.                                          
015272         10  HOLD-TDARR-BANK-X.                                   
015274             15  HOLD-TDARR-BANK            PIC 9(4).             
015276         10  HOLD-TDARR-REGION-X.                                 
015278             15  HOLD-TDARR-REGION          PIC 9(2).             
015280         10  HOLD-TDARR-RISE-CD-X.                                
015282             15  HOLD-TDARR-RISE-CD         PIC 9(2).             
015284         10  HOLD-TDARR-EFF-DATE-X.                               
015286             15  HOLD-TDARR-EFF-DATE        PIC 9(8).             
015288         10  HOLD-TDARR-END-DATE-X.                               
015290             15  HOLD-TDARR-END-DATE        PIC 9(8).             
015292         10  HOLD-TDARR-VOID-DATE-X.                              
015294             15  HOLD-TDARR-VOID-DATE       PIC 9(8).             
015296         10  HOLD-TDARR-ADD-DATE-X.                               
015298             15  HOLD-TDARR-ADD-DATE        PIC 9(8).             
015300         10  HOLD-TDARR-ADD-TIME-X.                               
015302             15  HOLD-TDARR-ADD-TIME        PIC 9(8).             
015304         10  HOLD-TDARR-PUB-ID              PIC X(8).             
015306         10  HOLD-TDARR-VOID-PUB-ID         PIC X(8).             
015308         10  HOLD-TDARR-DESC                PIC X(20).            
015310         10  HOLD-TDARR-FRQ-TYPE-X.                               
015312             15  HOLD-TDARR-FRQ-TYPE        PIC 9(1).             
015314         10  HOLD-TDARR-CYC-FRQ1-X.                               
015316             15  HOLD-TDARR-CYC-FRQ1        PIC 9(3).             
015318         10  HOLD-TDARR-CYC-INC1-X.                               
015320             15  HOLD-TDARR-CYC-INC1        PIC S9(2)V9(3).       
015322         10  HOLD-TDARR-CYC-FRQ2-X.                               
015324             15  HOLD-TDARR-CYC-FRQ2        PIC 9(3).             
015326         10  HOLD-TDARR-CYC-INC2-X.                               
015328             15  HOLD-TDARR-CYC-INC2        PIC S9(2)V9(3).       
015330         10  HOLD-TDARR-CYC-FRQ3-X.                               
015332             15  HOLD-TDARR-CYC-FRQ3        PIC 9(3).             
015334         10  HOLD-TDARR-CYC-INC3-X.                               
015336             15  HOLD-TDARR-CYC-INC3        PIC S9(2)V9(3).       
015338         10  HOLD-TDARR-CYC-FRQ4-X.                               
015340             15  HOLD-TDARR-CYC-FRQ4        PIC 9(3).             
015342         10  HOLD-TDARR-CYC-INC4-X.                               
015344             15  HOLD-TDARR-CYC-INC4        PIC S9(2)V9(3).       
015346         10  HOLD-TDARR-CYC-FRQ5-X.                               
015348             15  HOLD-TDARR-CYC-FRQ5        PIC 9(3).             
015350         10  HOLD-TDARR-CYC-INC5-X.                               
015352             15  HOLD-TDARR-CYC-INC5        PIC S9(2)V9(3).       
015354         10  HOLD-TDARR-CYC-FRQ6-X.                               
015356             15  HOLD-TDARR-CYC-FRQ6        PIC 9(3).             
015358         10  HOLD-TDARR-CYC-INC6-X.                               
015360             15  HOLD-TDARR-CYC-INC6        PIC S9(2)V9(3).       
015362         10  HOLD-TDARR-CYC-FRQ7-X.                               
015364             15  HOLD-TDARR-CYC-FRQ7        PIC 9(3).             
015366         10  HOLD-TDARR-CYC-INC7-X.                               
015368             15  HOLD-TDARR-CYC-INC7        PIC S9(2)V9(3).       
015370         10  HOLD-TDARR-CYC-FRQ8-X.                               
015372             15  HOLD-TDARR-CYC-FRQ8        PIC 9(3).             
015374         10  HOLD-TDARR-CYC-INC8-X.                               
015376             15  HOLD-TDARR-CYC-INC8        PIC S9(2)V9(3).       
015378         10  HOLD-TDARR-CYC-FRQ9-X.                               
015380             15  HOLD-TDARR-CYC-FRQ9        PIC 9(3).             
015382         10  HOLD-TDARR-CYC-INC9-X.                               
015384             15  HOLD-TDARR-CYC-INC9        PIC S9(2)V9(3).       
015386         10  HOLD-TDARR-CYC-FRQ10-X.                              
015388             15  HOLD-TDARR-CYC-FRQ10       PIC 9(3).             
015390         10  HOLD-TDARR-CYC-INC10-X.                              
015392             15  HOLD-TDARR-CYC-INC10       PIC S9(2)V9(3).       
015394                                                                  
015396     05  HOLD-TDATOTAL.                                           
015398         10  HOLD-TDATT-BANK-X.                                   
015400             15  HOLD-TDATT-BANK           PIC 9(4).              
015402         10  HOLD-TDATT-REGION-X.                                 
015404             15  HOLD-TDATT-REGION         PIC 9(2).              
015406         10  HOLD-TDATT-TOTAL-CD-X.                               
015408             15  HOLD-TDATT-TOTAL-CD       PIC 999.               
015410         10  HOLD-TDATT-APPL-X.                                   
015412             15  HOLD-TDATT-APPL           PIC 9.                 
015414         10  HOLD-TDATT-VOID-DATE-X.                              
015416             15  HOLD-TDATT-VOID-DATE      PIC 9(8).              
015418         10  HOLD-TDATT-ADD-DATE-X.                               
015420             15  HOLD-TDATT-ADD-DATE       PIC 9(8).              
015422         10  HOLD-TDATT-ADD-TIME-X.                               
015424             15  HOLD-TDATT-ADD-TIME       PIC 9(8).              
015426         10  HOLD-TDATT-PUB-ID             PIC X(8).              
015428         10  HOLD-TDATT-VOID-PUB-ID        PIC X(8).              
015430         10  HOLD-TDATT-DESC               PIC X(30).             
015432         10  HOLD-TDATT-RENEW-CD-X.                               
015434             15  HOLD-TDATT-RENEW-CD       PIC 9(1).              
015436         10  HOLD-TDATT-OVERRIDE-X.                               
015438             15  HOLD-TDATT-OVERRIDE       PIC 9(1).              
015440         10  HOLD-TDATT-REN-NTC-X.                                
015442             15  HOLD-TDATT-REN-NTC        PIC 9(1).              
015444         10  HOLD-TDATT-PMAT-NTC-X.                               
015446             15  HOLD-TDATT-PMAT-NTC       PIC 9(1).              
015448         10  HOLD-TDATT-RTCHG-NTC-X.                              
015450             15  HOLD-TDATT-RTCHG-NTC      PIC 9(1).              
015452         10  HOLD-TDATT-INT-NTC-X.                                
015454             15  HOLD-TDATT-INT-NTC        PIC 9(1).              
015456         10  HOLD-TDATT-YIELD-NUM-X.                              
015458             15  HOLD-TDATT-YIELD-NUM      PIC 9(3).              
015460         10  HOLD-TDATT-YIELD-DENOM-X.                            
015462             15  HOLD-TDATT-YIELD-DENOM    PIC 9(3).              
015464         10  HOLD-TDATT-CMPD-FREQ-X.                              
015466             15  HOLD-TDATT-CMPD-FREQ      PIC 9(1).              
015468         10  HOLD-TDATT-CMPD-NTRVL-X.                             
015470             15  HOLD-TDATT-CMPD-NTRVL     PIC 9(4).              
015472         10  HOLD-TDATT-RTCHG-LIMIT-X.                            
015474             15  HOLD-TDATT-RTCHG-LIMIT    PIC 9(1).              
015476         10  HOLD-TDATT-CHG-NTRVL-X.                              
015478             15  HOLD-TDATT-CHG-NTRVL      PIC 9(3).              
015480         10  HOLD-TDATT-PENALTY-CD-X.                             
015482             15  HOLD-TDATT-PENALTY-CD     PIC 999.               
015484         10  HOLD-TDATT-MAT-TYPE-X.                               
015486             15  HOLD-TDATT-MAT-TYPE       PIC 9(1).              
015488         10  HOLD-TDATT-MAT-TERM-X.                               
015490             15  HOLD-TDATT-MAT-TERM       PIC 9(4).              
015492         10  HOLD-TDATT-PAY-FREQ-X.                               
015494             15  HOLD-TDATT-PAY-FREQ       PIC 9(1).              
015496         10  HOLD-TDATT-PAY-NTRVL-X.                              
015498             15  HOLD-TDATT-PAY-NTRVL      PIC 9(4).              
015500         10  HOLD-TDATT-STMT-FREQ-X.                              
015502             15  HOLD-TDATT-STMT-FREQ      PIC 9(1).              
015504         10  HOLD-TDATT-STMT-NTRVL-X.                             
015506             15  HOLD-TDATT-STMT-NTRVL     PIC 9(4).              
015508         10  HOLD-TDATT-VAR-IMMED-X.                              
015510             15  HOLD-TDATT-VAR-IMMED      PIC 9(1).              
015512         10  HOLD-TDATT-VAR-INT-X.                                
015514             15  HOLD-TDATT-VAR-INT        PIC 9(1).              
015516         10  HOLD-TDATT-VAR-STEP-X.                               
015518             15  HOLD-TDATT-VAR-STEP       PIC 9(1).              
015520         10  HOLD-TDATT-VAR-SCHED-X.                              
015522             15  HOLD-TDATT-VAR-SCHED      PIC 9(1).              
015524         10  HOLD-TDATT-VAR-BAL-X.                                
015526             15  HOLD-TDATT-VAR-BAL        PIC 9(1).              
015528         10  HOLD-TDATT-VAR-CUST-X.                               
015530             15  HOLD-TDATT-VAR-CUST       PIC 9(1).              
015532         10  HOLD-TDATT-RT-CHG-ALOW-X.                            
015534             15  HOLD-TDATT-RT-CHG-ALOW    PIC 9(1).              
015536         10  HOLD-TDATT-WTHDRW-ALOW-X.                            
015538             15  HOLD-TDATT-WTHDRW-ALOW    PIC 9(1).              
015540         10  HOLD-TDATT-DPOSIT-ALOW-X.                            
015542             15  HOLD-TDATT-DPOSIT-ALOW    PIC 9(1).              
015544         10  HOLD-TDATT-ODD-PAYMENT-X.                            
015546             15  HOLD-TDATT-ODD-PAYMENT    PIC 9(1).              
015548         10  HOLD-TDATT-IGL-GRP-X.                                
015550             15  HOLD-TDATT-IGL-GRP        PIC 9(2).              
015552         10  HOLD-TDATT-POST-MAT-X.                               
015554             15  HOLD-TDATT-POST-MAT       PIC 9(1).              
015556         10  HOLD-TDATT-END-OF-MAT-X.                             
015558             15  HOLD-TDATT-END-OF-MAT     PIC 9(1).              
015560         10  HOLD-TDATT-END-OF-INT-X.                             
015562             15  HOLD-TDATT-END-OF-INT     PIC 9(1).              
015564         10  HOLD-TDATT-END-OF-STMT-X.                            
015566             15  HOLD-TDATT-END-OF-STMT    PIC 9(1).              
015568         10  HOLD-TDATT-END-OF-CMPD-X.                            
015570             15  HOLD-TDATT-END-OF-CMPD    PIC 9(1).              
015572         10  HOLD-TDATT-FLOOR-RT-X.                               
015574             15  HOLD-TDATT-FLOOR-RT       PIC 99V999.            
015576         10  HOLD-TDATT-FLOOR-INCR-X.                             
015578             15  HOLD-TDATT-FLOOR-INCR     PIC 99V999.            
015580         10  HOLD-TDATT-CHG-NTC-X.                                
015582             15  HOLD-TDATT-CHG-NTC        PIC 9(1).              
015584         10  HOLD-TDATT-IRA-BACKED-X.                             
015586             15  HOLD-TDATT-IRA-BACKED     PIC 9(1).              
015588         10  HOLD-TDATT-SAV-DEPOSIT        PIC 9(1).              
015590         10  HOLD-TDATT-LEVEL-PAY-X.                              
015592             15  HOLD-TDATT-LEVEL-PAY      PIC 9.                 
015594         10  HOLD-TDATT-CAP-RT-CHG         PIC X.                 
015596         10  HOLD-TDATT-FEE-FREQ-X.                               
015598             15  HOLD-TDATT-FEE-FREQ       PIC 9.                 
015600         10  HOLD-TDATT-FEE-NTRVL-X.                              
015602             15  HOLD-TDATT-FEE-NTRVL      PIC 9(4).              
015604         10  HOLD-TDATT-FEE-AMT-X.                                
015606             15  HOLD-TDATT-FEE-AMT        PIC S9(12)V99.         
015608         10  HOLD-TDATT-END-OF-FEE-X.                             
015610             15  HOLD-TDATT-END-OF-FEE     PIC 9.                 
015612         10  HOLD-TDATT-ZERO-RT-ALLOW-X.                          
015614             15  HOLD-TDATT-ZERO-RT-ALLOW  PIC 9.                 
015616         10  HOLD-TDATT-RC-MAT-ONLY        PIC 9(1).              
015618         10  HOLD-TDATT-CLS-ON-MAT         PIC 9(1).              
015620         10  HOLD-TDATT-GRACE-DAYS         PIC 9(2).              
015622         10  HOLD-TDATT-IGL-GRP-2          PIC 9(2).              
015624                                                                  
015626     05  HOLD-TDAHMS.                                             
015628         10  HOLD-TDAHMS-BANK              PIC  9(4).             
015630         10  HOLD-TDAHMS-APPL              PIC  9(1).             
015632         10  HOLD-TDAHMS-CUST              PIC  9(12).            
015634         10  HOLD-TDAHMS-ACCT              PIC  9(10).            
015636         10  HOLD-TDAHMS-TYPE              PIC  X(1).             
015638         10  HOLD-TDAHMS-BK-TYPE           PIC  X(1).             
015640         10  HOLD-TDAHMS-DR-CR-IND         PIC  X(1).             
015642         10  HOLD-TDAHMS-SOURCE            PIC  9(2).             
015644         10  HOLD-TDAHMS-HOLD-NBR          PIC  9(4).             
015646         10  HOLD-TDAHMS-AMT               PIC S9(12)V99.         
015648         10  HOLD-TDAHMS-ORIG-AMT          PIC  9(12)V99.         
015650         10  HOLD-TDAHMS-COMMENT           PIC  X(40).            
015652         10  HOLD-TDAHMS-PUB-ID            PIC  X(8).             
015654         10  HOLD-TDAHMS-VD-PUB-ID         PIC  X(8).             
015656         10  HOLD-TDAHMS-ADD-DATE          PIC  9(8).             
015658         10  HOLD-TDAHMS-ADD-TIME          PIC  9(8).             
015660         10  HOLD-TDAHMS-VOID-DATE         PIC  9(8).             
015662         10  HOLD-TDAHMS-PLG-ACCT          PIC  9(12).            
015664         10  HOLD-TDAHMS-PLG-ACCT-S        PIC  9(10).            
015666         10  HOLD-TDAHMS-EXPIRE-DT         PIC  9(8).             
015668         10  HOLD-TDAHMS-AVAIL-BAL         PIC S9(12)V99.         
015670         10  HOLD-TDAHMS-SERIAL-NUM        PIC  9(10).            
015672         10  HOLD-TDAHMS-END-SERIAL        PIC  9(10).            
015674         10  HOLD-TDAHMS-NAME              PIC  X(10).            
015676         10  HOLD-TDAHMS-START-DATE        PIC  9(8).             
015678         10  HOLD-TDAHMS-DAILY-ACCR        PIC S9(12)V9(6).       
015680         10  HOLD-TDAHMS-ORG-ADD-DT        PIC  9(8).             
015682         10  HOLD-TDAHMS-ORG-ADD-TM        PIC  9(8).             
015684         10  HOLD-TDAHMS-ORG-PUB-ID        PIC  X(8).             
015686         10  HOLD-TDAHMS-AMT-LAST-UPD      PIC S9(12)V9(2).       
015688         10  HOLD-TDAHMS-DATE-LAST-UPD     PIC  9(8).             
015690                                                                  
015692     05  HOLD-TDABENEF.                                           
015694         10  HOLD-TDAB-BANK                PIC 9(04).             
015696         10  HOLD-TDAB-CUST                PIC 9(12).             
015698         10  HOLD-TDAB-ACCT                PIC 9(10).             
015700         10  HOLD-TDAB-BENEF-NBR           PIC 9(02).             
015702         10  HOLD-TDAB-NAME                PIC X(40).             
015704         10  HOLD-TDAB-NAME-2              PIC X(40).             
015706         10  HOLD-TDAB-NAME-3              PIC X(40).             
015708         10  HOLD-TDAB-ADDR-1              PIC X(40).             
015710         10  HOLD-TDAB-ADDR-2              PIC X(40).             
015712         10  HOLD-TDAB-CITY                PIC X(40).             
015714         10  HOLD-TDAB-STATE               PIC X(02).             
015716         10  HOLD-TDAB-PROVINCE            PIC X(02).             
015718         10  HOLD-TDAB-COUNTRY             PIC X(02).             
015720         10  HOLD-TDAB-ZIP-CODE.                                  
015722             15  HOLD-TDAB-ZIP             PIC 9(05).             
015724             15  HOLD-TDAB-ZIP-4           PIC 9(04).             
015726         10  HOLD-TDAB-PHONE               PIC 9(10).             
015728         10  HOLD-TDAB-TIN                 PIC 9(09).             
015730         10  HOLD-TDAB-BIRTH-DT            PIC 9(08).             
015732         10  HOLD-TDAB-RELATION            PIC 9(01).             
015734         10  HOLD-TDAB-DESIGNATION         PIC 9(01).             
015736         10  HOLD-TDAB-PERCENT             PIC 9(03).             
015738         10  HOLD-TDAB-FREE-REMARK         PIC X(24).             
015740                                                                  
015742     05  HOLD-TDAADDR.                                            
015744         10  HOLD-TDADR-BANK               PIC 9(04).             
015746         10  HOLD-TDADR-CUST               PIC 9(12).             
015748         10  HOLD-TDADR-ACCT               PIC 9(10).             
015750         10  HOLD-TDADR-ADDR-USAGE         PIC X(01).             
015752         10  HOLD-TDADR-TEMP-BEG-DT        PIC 9(04).             
015754         10  HOLD-TDADR-TEMP-END-DT        PIC 9(04).             
015756         10  HOLD-TDADR-TEMP-EFF-DT        PIC 9(08).             
015758         10  HOLD-TDADR-TEMP-EXP-DT        PIC 9(08).             
015760         10  HOLD-TDADR-ADDR-GROUP.                               
015762             15  HOLD-TDADR-T-ADDR.                               
015764                 20  HOLD-TDADR-T-ADDR-1   PIC X(40).             
015766                 20  HOLD-TDADR-T-ADDR-2   PIC X(40).             
015768                 20  HOLD-TDADR-T-CITY     PIC X(40).             
015770                 20  HOLD-TDADR-T-STATE    PIC X(02).             
015772                 20  HOLD-TDADR-T-PROVINCE PIC X(02).             
015774                 20  HOLD-TDADR-T-COUNTRY  PIC X(02).             
015776                 20  HOLD-TDADR-T-ZIP-CODE.                       
015778                     25  HOLD-TDADR-T-ZIP  PIC 9(05).             
015780                     25  HOLD-TDADR-T-ZIP-4 PIC 9(04).            
015782                 20  HOLD-TDADR-T-ALIEN-CD PIC 9(01).             
015784                 20  HOLD-TDADR-T-BAR-CODE PIC 9(03).             
015786                 20  HOLD-TDADR-T-EMAIL-ADDR PIC X(100).          
015788                 20  HOLD-TDADR-T-EMAIL-ADDR-R                    
015790                                REDEFINES HOLD-TDADR-T-EMAIL-ADDR.
015792                     25  HOLD-TDADR-T-EMAIL-ADDR-1-50   PIC X(50).
015794                     25  HOLD-TDADR-T-EMAIL-ADDR-51-100 PIC X(50).
015796                 20  HOLD-TDADR-T-MAIL-CD    PIC 9(01).           
015798                 20  HOLD-TDADR-T-ADDR-KEY   PIC X(28).           
015800             15  HOLD-TDADR-A-ADDR.                               
015802                 20  HOLD-TDADR-A-NAME-1          PIC X(40).      
015804                 20  HOLD-TDADR-A-NAME-AREA-1.                    
015806                     25  HOLD-TDADR-A-N1-KEY      PIC X(14).      
015808                     25  HOLD-TDADR-A-N1-FIRST    PIC X(40).      
015810                     25  HOLD-TDADR-A-N1-MID      PIC X(20).      
015812                     25  HOLD-TDADR-A-N1-LAST     PIC X(40).      
015814                     25  HOLD-TDADR-A-N1-PREFIX   PIC X(12).      
015816                     25  HOLD-TDADR-A-N1-SUFFIX   PIC X(12).      
015818                     25  HOLD-TDADR-A-N1-FAMILIAR PIC X(20).      
015820                     25  HOLD-TDADR-A-N1-PRT-PFX  PIC X(01).      
015822                     25  HOLD-TDADR-A-N1-PRT-SFX  PIC X(01).      
015824                     25  HOLD-TDADR-A-N1-DESIGNAT PIC X(20).      
015826                 20  HOLD-TDADR-A-NAME-2          PIC X(40).      
015828                 20  HOLD-TDADR-A-N2-MODIFIED     PIC X(01).      
015830                 20  HOLD-TDADR-A-N2-PRINT-CD     PIC X(01).      
015832                 20  HOLD-TDADR-A-NAME-AREA-2.                    
015834                     25  HOLD-TDADR-A-N2-KEY      PIC X(14).      
015836                     25  HOLD-TDADR-A-N2-FIRST    PIC X(40).      
015838                     25  HOLD-TDADR-A-N2-MID      PIC X(20).      
015840                     25  HOLD-TDADR-A-N2-LAST     PIC X(40).      
015842                     25  HOLD-TDADR-A-N2-PREFIX   PIC X(12).      
015844                     25  HOLD-TDADR-A-N2-SUFFIX   PIC X(12).      
015846                     25  HOLD-TDADR-A-N2-FAMILIAR PIC X(20).      
015848                     25  HOLD-TDADR-A-N2-PRT-PFX  PIC X(01).      
015850                     25  HOLD-TDADR-A-N2-PRT-SFX  PIC X(01).      
015852                     25  HOLD-TDADR-A-N2-DESIGNAT PIC X(20).      
015854                 20  HOLD-TDADR-A-NAME-3          PIC X(40).      
015856                 20  HOLD-TDADR-A-N3-MODIFIED     PIC X(01).      
015858                 20  HOLD-TDADR-A-N3-PRINT-CD     PIC X(01).      
015860                 20  HOLD-TDADR-A-NAME-AREA-3.                    
015862                     25  HOLD-TDADR-A-N3-KEY      PIC X(14).      
015864                     25  HOLD-TDADR-A-N3-FIRST    PIC X(40).      
015866                     25  HOLD-TDADR-A-N3-MID      PIC X(20).      
015868                     25  HOLD-TDADR-A-N3-LAST     PIC X(40).      
015870                     25  HOLD-TDADR-A-N3-PREFIX   PIC X(12).      
015872                     25  HOLD-TDADR-A-N3-SUFFIX   PIC X(12).      
015874                     25  HOLD-TDADR-A-N3-FAMILIAR PIC X(20).      
015876                     25  HOLD-TDADR-A-N3-PRT-PFX  PIC X(01).      
015878                     25  HOLD-TDADR-A-N3-PRT-SFX  PIC X(01).      
015880                     25  HOLD-TDADR-A-N3-DESIGNAT PIC X(20).      
015882                 20  HOLD-TDADR-A-ADDR-KEY        PIC X(28).      
015884                 20  HOLD-TDADR-A-ADDR-1   PIC X(40).             
015886                 20  HOLD-TDADR-A-ADDR-2   PIC X(40).             
015888                 20  HOLD-TDADR-A-CITY     PIC X(40).             
015890                 20  HOLD-TDADR-A-STATE    PIC X(02).             
015892                 20  HOLD-TDADR-A-PROVINCE PIC X(02).             
015894                 20  HOLD-TDADR-A-COUNTRY  PIC X(02).             
015896                 20  HOLD-TDADR-A-ZIP-CODE.                       
015898                     25  HOLD-TDADR-A-ZIP  PIC 9(05).             
015900                     25  HOLD-TDADR-A-ZIP-4 PIC 9(04).            
015902                 20  HOLD-TDADR-A-ALIEN-CD PIC 9(01).             
015904                 20  HOLD-TDADR-A-BAR-CODE PIC 9(03).             
015906                 20  HOLD-TDADR-A-EMAIL-ADDR PIC X(100).          
015908                 20  HOLD-TDADR-A-EMAIL-ADDR-R                    
015910                                REDEFINES HOLD-TDADR-A-EMAIL-ADDR.
015912                     25  HOLD-TDADR-A-EMAIL-ADDR-1-50   PIC X(50).
015914                     25  HOLD-TDADR-A-EMAIL-ADDR-51-100 PIC X(50).
015916                 20  HOLD-TDADR-A-MAIL-CD      PIC 9(01).         
015918         10  HOLD-TDADR-SHT-NAME           PIC X(20).             
015920         10  HOLD-TDADR-LUPD-DATE          PIC 9(08).             
015922         10  HOLD-TDADR-LUPD-TIME          PIC 9(08).             
015924         10  HOLD-TDADR-PUB-ID             PIC X(08).             
015926         10  HOLD-TDADR-TIN-CD             PIC X.                 
015928         10  HOLD-TDADR-TIN-NBR            PIC 9(9).              
015930         10  HOLD-TDADR-TIN-CERT-CD        PIC 9.                 
015932         10  HOLD-TDADR-TIN-CD-2           PIC X(01).             
015934         10  HOLD-TDADR-TIN-NBR-2          PIC 9(09).             
015936         10  HOLD-TDADR-TIN-CT-CD-2        PIC 9(01).             
015938         10  HOLD-TDADR-TIN-CD-3           PIC X(01).             
015940         10  HOLD-TDADR-TIN-NBR-3          PIC 9(09).             
015942         10  HOLD-TDADR-TIN-CT-CD-3        PIC 9(01).             
015944                                                                  
015946     05  HOLD-TDAPENALTY.                                         
015948         10  HOLD-TDAP-BANK                PIC 9(4).              
015950         10  HOLD-TDAP-ROUTINE             PIC 999.               
015952         10  HOLD-TDAP-STEP-NBR            PIC 9(2).              
015954         10  HOLD-TDAP-FUNC                PIC X(1).              
015956         10  HOLD-TDAP-ADD-DATE            PIC 9(8).              
015958         10  HOLD-TDAP-ADD-TIME            PIC 9(8).              
015960         10  HOLD-TDAP-PUB-ID              PIC X(8).              
015962         10  HOLD-TDAP-VOID-PUB-ID         PIC X(8).              
015964         10  HOLD-TDAP-VOID-DATE           PIC 9(8).              
015966         10  HOLD-TDAP-DATE                PIC 9(8).              
015968         10  HOLD-TDAP-DAYS                PIC 9(4).              
015970         10  HOLD-TDAP-MONTHS              PIC 9(4).              
015972         10  HOLD-TDAP-PERCENT             PIC 9(2)V9(2).         
015974         10  HOLD-TDAP-AMOUNT              PIC S9(12)V9(2).       
015976         10  HOLD-TDAP-USE-INT             PIC 9(1).              
015978         10  HOLD-TDAP-USE-RED             PIC 9(1).              
015980         10  HOLD-TDAP-USE-MONTH           PIC 9(1).              
015982         10  HOLD-TDAP-USE-DAY             PIC 9(1).              
015984         10  HOLD-TDAP-USE-AVL-INT         PIC 9(1).              
015986                                                                  
015988     05  HOLD-TDAPCR.                                             
015990         10  HOLD-TDAPC-APPL               PIC X(03).             
015992         10  HOLD-TDAPC-TYPE               PIC 9(1).              
015994         10  HOLD-TDAPC-BANK               PIC 9(04).             
015996         10  HOLD-TDAPC-RPT-NBR            PIC 9(04).             
015998         10  HOLD-TDAPC-CSI-ONLY           PIC X(01).             
016000         10  HOLD-TDAPC-RPT-DESC           PIC X(40).             
016002         10  HOLD-TDAPC-SPECS              PIC X(65).             
016004         10  HOLD-TDAPC-COPIES             PIC 9(02).             
016006         10  HOLD-TDAPC-LASER-PRT          PIC 9(02).             
016008         10  HOLD-TDAPC-FICHE-PRT          PIC 9(02).             
016010         10  HOLD-TDAPC-OPTICAL            PIC 9(02).             
016012         10  HOLD-TDAPC-PRT-DLY            PIC X(01).             
016014         10  HOLD-TDAPC-DLY-IND            PIC X(07).             
016016         10  HOLD-TDAPC-LST-PRT-D          PIC 9(08).             
016018         10  HOLD-TDAPC-PRT-WK             PIC X(01).             
016020         10  HOLD-TDAPC-WK-IND             PIC X(07).             
016022         10  HOLD-TDAPC-LST-PRT-W          PIC 9(08).             
016024         10  HOLD-TDAPC-PRT-MTH            PIC X(01).             
016026         10  HOLD-TDAPC-LST-DAY-M          PIC X(01).             
016028         10  HOLD-TDAPC-NXT-PRT-M          PIC 9(08).             
016030         10  HOLD-TDAPC-LST-PRT-M          PIC 9(08).             
016032         10  HOLD-TDAPC-PRT-QTR            PIC X(01).             
016034         10  HOLD-TDAPC-LST-DAY-Q          PIC X(01).             
016036         10  HOLD-TDAPC-NXT-PRT-Q          PIC 9(08).             
016038         10  HOLD-TDAPC-LST-PRT-Q          PIC 9(08).             
016040         10  HOLD-TDAPC-PRT-YR             PIC X(01).             
016042         10  HOLD-TDAPC-NXT-PRT-Y          PIC 9(08).             
016044         10  HOLD-TDAPC-LST-PRT-Y          PIC 9(08).             
016046         10  HOLD-TDAPC-SPECL-REQ          PIC X(01).             
016048         10  HOLD-TDAPC-PRT-DAY            PIC 9(08).             
016050         10  HOLD-TDAPC-BEGIN-DATE         PIC 9(06).             
016052         10  HOLD-TDAPC-END-DATE           PIC 9(06).             
016054         10  HOLD-TDAPC-PRINTER            PIC X(17).             
016056         10  HOLD-TDAPC-SPECL-SPECS        PIC X(65).             
016058         10  HOLD-TDAPC-REQUESTOR          PIC X(08).             
016060         10  HOLD-TDAPC-LPROCESS-DT        PIC 9(16).             
016062         10  HOLD-TDAPC-LUPD-DT            PIC 9(08).             
016064         10  HOLD-TDAPC-LUPD-TM            PIC 9(06).             
016066         10  HOLD-TDAPC-BP-LAST-RUN        PIC 9(16).             
016068         10  HOLD-TDAPC-PUB-ID             PIC X(08).             
016070         10  HOLD-TDAPC-BANK-SPECS         PIC X(300).            
016072         10  HOLD-TDAPC-BANK-SPECS-R REDEFINES                    
```

⚠️  This is the source code you must document.
    936 lines from 7097 to 8032.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

