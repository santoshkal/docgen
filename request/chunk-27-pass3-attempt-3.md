# LLM Request Debug File
Generated: 2025-11-17T21:09:57.820632

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 27/55
- **Model**: gpt-4.1
- **Chunk Number**: 27
- **Pass Number**: 3
- **Attempt Number**: 3 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~9,310 tokens
- **Total Input**: ~11,268 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 27/55" (ID: detailed-code-explanation)

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


**CHUNK 27 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-17T19:50:50.832678", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 27 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 12528 to 13039 (512 lines)\nChunk Tokens (estimated): ~7,889\nActual Input Tokens: 9,295 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 12528-13039 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 27 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 27 of 55.\n\n\n=============================================================================\nCHUNK 27 SOURCE CODE (Lines 12528-13039)\n=============================================================================\n\n```cobol\n025064         OLD-SPECS-CNV-TOT-DNLOAD.                                \n025066         15 OLD-SPECS-CNV-TOT-DNLOAD-X   PIC X(08).               \n025068     10  FILLER                          PIC X(13).               \n025070     10  OLD-SPECS-ADDR-ALERT-DAYS       PIC 999.                 \n025072     10  OLD-SPECS-COMB-SEND-CERT        PIC X(1).                \n025074     10  OLD-SPECS-APPLY-GRACE-AT-SR     PIC X(1).                \n025076     10  OLD-SPECS-DB-SUFFIX             PIC X(1).                \n025078     10  OLD-SPECS-EOY-YTD-ROLL          PIC X(1).                \n025080     10  OLD-SPECS-COMB-DDA-OPT          PIC X(1).                \n025082     10  OLD-SPECS-CONTINUE              PIC X(1).                \n025084                                                                  \n025086**  SPECS FOR 580 PCR                                             \n025088   05  SPECS-580-AREA.                                            \n025090     10  SPECS-580-PRT-FORMAT            PIC X(1).                \n025092     10  SPECS-580-PRT-ACCT              PIC X(1).                \n025094     10  SPECS-580-PROTECT               PIC X(1).                \n025096     10  SPECS-580-RATE-1                PIC X(1).                \n025098     10  SPECS-580-RATE-2                PIC X(1).                \n025100     10  SPECS-580-MAT-DT                PIC X(1).                \n025102     10  SPECS-580-GRACE-IN-PROC         PIC X(3).                \n025104     10  SPECS-580-SUPPRESS-TIN          PIC X(1).                \n025106     10  SPECS-580-PRT-MAT               PIC X(1).                \n025108     10  SPECS-580-PRT-DESC              PIC X(1).                \n025110     10  SPECS-580-SUPPRESS-TRAILER      PIC X(1).                \n025112     10  SPECS-580-PRT-DAYS-IN-CYCLE     PIC X(1).                \n025114     10  SPECS-580-PRT-CUST-NO           PIC X(1).                \n025116     10  FILLER                          PIC X(50).               \n025118   05  OLD-580-AREA.                                              \n025120     10  OLD-580-PRT-FORMAT            PIC X(1).                  \n025122     10  OLD-580-PRT-ACCT              PIC X(1).                  \n025124     10  OLD-580-PROTECT               PIC X(1).                  \n025126     10  OLD-580-RATE-1                PIC X(1).                  \n025128     10  OLD-580-RATE-2                PIC X(1).                  \n025130     10  OLD-580-MAT-DT                PIC X(1).                  \n025132     10  OLD-580-GRACE-IN-PROC         PIC X(3).                  \n025134     10  OLD-580-SUPPRESS-TIN          PIC X(1).                  \n025136     10  OLD-580-PRT-MAT               PIC X(1).                  \n025138     10  OLD-580-PRT-DESC              PIC X(1).                  \n025140     10  OLD-580-SUPPRESS-TRAILER      PIC X(1).                  \n025142     10  OLD-580-PRT-DAYS-IN-CYCLE     PIC X(1).                  \n025144     10  OLD-580-PRT-CUST-NO           PIC X(1).                  \n025146     10  FILLER                          PIC X(50).               \n025148                                                                  \n025150**  SPECS FOR 560 PCR                                             \n025152   05  WS-SPEC-OPTION.                                            \n025154     10  WS-DISPLAY-RATE                 PIC X(01) VALUE \"X\".     \n025156     10  WS-DISP-PRT.                                             \n025158         15  WS-PRT-DISP-1               PIC X(01).               \n025160         15  WS-PRT-DISP-2               PIC X(01).               \n025162         15  WS-PRT-DISP-3               PIC X(01).               \n025164         15  WS-PRT-DISP-4               PIC X(01).               \n025166         15  WS-PRT-DISP-5               PIC X(01).               \n025168         15  WS-PRT-DISP-6               PIC X(01).               \n025170     10  WS-NOTICE-TIN-PRT               PIC X(01).               \n025172     10  FILLER                          PIC X(57).               \n025174   05 OLD-560-AREA.                                               \n025176     10  OLD-560-DISPLAY-RATE                 PIC X(01).          \n025178     10  OLD-560-DISP-PRT.                                        \n025180         15  OLD-560-PRT-DISP-1               PIC X(01).          \n025182         15  OLD-560-PRT-DISP-2               PIC X(01).          \n025184         15  OLD-560-PRT-DISP-3               PIC X(01).          \n025186         15  OLD-560-PRT-DISP-4               PIC X(01).          \n025188         15  OLD-560-PRT-DISP-5               PIC X(01).          \n025190         15  OLD-560-PRT-DISP-6               PIC X(01).          \n025192     10  OLD-560-NOTICE-TIN-PRT               PIC X(01).          \n025194     10  FILLER                          PIC X(57).               \n025196                                                                  \n025198                                                                  \n025200**  SPECS FOR 601 PCR                                             \n025202   05  RPT601-SPECS.                                              \n025204     10  RPT601-APR                      PIC X(01) VALUE \" \".     \n025206     10  RPT601-NO-TIN                   PIC X(01) VALUE \" \".     \n025208     10  RPT601-BEG-DT-1                 PIC 9(08) VALUE 0.       \n025210     10  RPT601-END-DT-1                 PIC 9(08) VALUE 0.       \n025212     10  RPT601-OPT-1                    PIC X(01) VALUE SPACES.  \n025214     10  RPT601-BEG-DT-2                 PIC 9(08) VALUE 0.       \n025216     10  RPT601-END-DT-2                 PIC 9(08) VALUE 0.       \n025218     10  RPT601-OPT-2                    PIC X(01) VALUE SPACE.   \n025220     10  RPT601-BEG-DT-3                 PIC 9(08) VALUE 0.       \n025222     10  RPT601-END-DT-3                 PIC 9(08) VALUE 0.       \n025224     10  RPT601-OPT-3                    PIC X(01) VALUE SPACE.   \n025226     10  RPT601-SUPP-DOB                 PIC X(01) VALUE SPACE.   \n025228     10  RPT601-SUPP-ACCT                PIC 9(01) VALUE 0.       \n025230     10  RPT601-MASK-OPTION              PIC X(01) VALUE SPACE.   \n025232     10  RPT601-MASK-CHAR                PIC X(01) VALUE SPACE.   \n025234     10  RPT601-MASK-LENGTH              PIC X(01) VALUE SPACE.   \n025236     10  FILLER                          PIC X(03) VALUE \"   \".   \n025238     10  RPT601-TRUNC-TIN                PIC X(01) VALUE \" \".     \n025240     10  RPT601-PRT-RATE                 PIC X(01) VALUE \" \".     \n025242     10  RPT601-PRT-APYE-EOY             PIC X(01) VALUE \" \".     \n025244     10  RPT601-STMT-DET-PRT             PIC X(01) VALUE \" \".     \n025246                                                                  \n025248   05 OLD-601-AREA.                                               \n025250     10  OLD-601-APR                     PIC X(01) VALUE SPACES.  \n025252     10  OLD-601-NO-TIN                  PIC X(01) VALUE SPACES.  \n025254     10  OLD-601-BEG-DT-1                PIC 9(08) VALUE ZEROES.  \n025256     10  OLD-601-END-DT-1                PIC 9(08) VALUE ZEROES.  \n025258     10  OLD-601-OPT-1                   PIC X(01) VALUE SPACES.  \n025260     10  OLD-601-BEG-DT-2                PIC 9(08) VALUE ZEROES.  \n025262     10  OLD-601-END-DT-2                PIC 9(08) VALUE ZEROES.  \n025264     10  OLD-601-OPT-2                   PIC X(01) VALUE SPACES.  \n025266     10  OLD-601-BEG-DT-3                PIC 9(08) VALUE ZEROES.  \n025268     10  OLD-601-END-DT-3                PIC 9(08) VALUE ZEROES.  \n025270     10  OLD-601-OPT-3                   PIC X(01) VALUE SPACES.  \n025272     10  OLD-601-SUPP-DOB                PIC X(01) VALUE SPACES.  \n025274     10  OLD-601-SUPP-ACCT               PIC 9(01) VALUE ZEROES.  \n025276     10  OLD-601-MASK-OPTION             PIC X(01) VALUE SPACE.   \n025278     10  OLD-601-MASK-CHAR               PIC X(01) VALUE SPACE.   \n025280     10  OLD-601-MASK-LENGTH             PIC X(01) VALUE SPACE.   \n025282     10  FILLER                          PIC X(03) VALUE SPACES.  \n025284     10  OLD-601-TRUNC-TIN               PIC X(01) VALUE SPACES.  \n025286     10  OLD-601-PRT-RATE                PIC X(01) VALUE SPACES.  \n025288     10  OLD-601-PRT-APYE-EOY            PIC X(01) VALUE SPACES.  \n025290     10  OLD-601-STMT-DET-PRT            PIC X(01) VALUE SPACES.  \n025292                                                                  \n025294                                                                  \n025296**  SPECS FOR 601 PCR BANK 0000                                   \n025298   05  RPT601-CSI-OPTIONS.                                        \n025300     10  RPT601-CSI-APR                  PIC X(01) VALUE \" \".     \n025302     10  RPT601-CSI-TIN                  PIC X(01) VALUE \" \".     \n025304     10  RPT601-CSI-BEG-DT-1             PIC 9(08) VALUE 0.       \n025306     10  RPT601-CSI-END-DT-1             PIC 9(08) VALUE 0.       \n025308     10  RPT601-CSI-OPT-1                PIC X(01) VALUE \" \".     \n025310     10  RPT601-CSI-BEG-DT-2             PIC 9(08) VALUE 0.       \n025312     10  RPT601-CSI-END-DT-2             PIC 9(08) VALUE 0.       \n025314     10  RPT601-CSI-OPT-2                PIC X(01) VALUE \" \".     \n025316     10  RPT601-CSI-BEG-DT-3             PIC 9(08) VALUE 0.       \n025318     10  RPT601-CSI-END-DT-3             PIC 9(08) VALUE 0.       \n025320     10  RPT601-CSI-OPT-3                PIC X(01) VALUE \" \".     \n025322     10  FILLER                          PIC X(07) VALUE \" \".     \n025324     10  RPT601-CSI-TRUNC-TIN            PIC X(01) VALUE \" \".     \n025326     10  RPT601-CSI-PRT-RATE             PIC X(01) VALUE \" \".     \n025328     10  RPT601-CSI-PRT-APYE-EOY         PIC X(01) VALUE \" \".     \n025330     10  RPT601-CSI-STMT-DET-PRT         PIC X(01) VALUE \" \".     \n025332                                                                  \n025334**  SPECS FOR 140, 640 PCR                                        \n025336   05  WS-RPT640-SPECS-FIELDS.                                    \n025338     10  WS-RPT640-SPECS                 PIC X(1).                \n025340     10  FILLER                          PIC X(64).               \n025342   05 OLD-640-AREA.                                               \n025344     10  OLD-640-SPECS                   PIC X(1).                \n025346     10  FILLER                          PIC X(64).               \n025348                                                                  \n025350**  SPECS FOR 090, 091, AND 092 PCRS                              \n025352   05  WS-RPT-OPTIONS.                                            \n025354     10  WS-SORT-OPT                     PIC X(01) VALUE SPACES.  \n025356     10  FILLER                          PIC X(64).               \n025358   05  OLD-RPT-OPTIONS.                                           \n025360     10  OLD-SORT-OPT                    PIC X(01).               \n025362     10  FILLER                          PIC X(64).               \n025364                                                                  \n025366   05  WS-090-OPTIONS.                                            \n025368     10  WS-090-SORT                     PIC X(01) VALUE SPACES.  \n025370     10  WS-REQUEST-TRIAL                PIC X(01) VALUE SPACES.  \n025372     10  FILLER                          PIC X(63) VALUE SPACES.  \n025374   05  OLD-090-AREA.                                              \n025376     10  OLD-090-SORT                    PIC X(01).               \n025378     10  OLD-090-REQUEST-TRIAL           PIC X(01).               \n025380     10  FILLER                          PIC X(63).               \n025382                                                                  \n025384   05  RPT311-SPECS.                                              \n025386     10  RPT311-MONTHLY                  PIC X(01) VALUE SPACES.  \n025388     10  FILLER                          PIC X(64).               \n025390   05  OLD-RPT311-SPECS.                                          \n025392     10  OLD-RPT311-MONTHLY              PIC X(01) VALUE SPACES.  \n025394     10  FILLER                          PIC X(64).               \n025396                                                                  \n025398   05  RPT408-SPECS.                                              \n025400     10  RPT408-TOTCD-BYBRCH             PIC X(01) VALUE SPACES.  \n025402     10  FILLER                          PIC X(64).               \n025404   05  OLD-408-AREA.                                              \n025406     10  OLD-408-TOTCD-BYBRCH            PIC X(01).               \n025408     10  FILLER                          PIC X(64).               \n025410                                                                  \n025412   05 RPT410-CLASS-TABLE.                                         \n025414    10 RPT410-TABLE OCCURS 65 TIMES.                              \n025416       15 TBL410-CLASS-CODE       PIC X(01).                      \n025418                                                                  \n025420   05  RPT465-SPECS.                                              \n025422     10 RPT465-LARGE-TRX-AMT             PIC 9(9)V99 VALUE ZEROS. \n025424     10 RPT465-LARGE-TRX-AMT-9S                                   \n025426         REDEFINES RPT465-LARGE-TRX-AMT  PIC 9(11).               \n025428     10 FILLER                           PIC X(54).               \n025430   05  OLD-465-AREA.                                              \n025432     10 OLD-465-LARGE-TRX-AMT            PIC 9(9)V99.             \n025434     10 OLD-465-LARGE-TRX-AMT-9S                                  \n025436         REDEFINES OLD-465-LARGE-TRX-AMT PIC 9(11).               \n025438     10 FILLER                           PIC X(54).               \n025440                                                                  \n025442                                                                  \n025444   05  RPT651-SPECS.                                              \n025446     10  RPT651-MMDD-1                   PIC 9(04).               \n025448     10  RPT651-MMDD-2                   PIC 9(04).               \n025450     10  FILLER                          PIC X(57).               \n025452   05  OLD-651-AREA.                                              \n025454     10  OLD-651-MMDD-1                  PIC 9(04).               \n025456     10  OLD-651-MMDD-2                  PIC 9(04).               \n025458     10  FILLER                          PIC X(57).               \n025460                                                                  \n025462   05  RPT592-SPECS.                                              \n025464       10  RPT592-OCT                    PIC X.                   \n025466       10  RPT592-NOV                    PIC X.                   \n025468       10  FILLER                        PIC X(63).               \n025470   05  OLD-RPT592-SPECS.                                          \n025472       10  OLD-RPT592-OCT                PIC X.                   \n025474       10  OLD-RPT592-NOV                PIC X.                   \n025476       10  FILLER                        PIC X(63).               \n025478                                                                  \n025480   05  RPT412-SPECS.                                              \n025482       10  RPT412-ADDL-RPTS-TTLS         PIC X.                   \n025484       10  FILLER                        PIC X(64).               \n025486   05  OLD-412-AREA.                                              \n025488       10  OLD-412-ADDL-RPTS-TTLS        PIC X.                   \n025490       10  FILLER                        PIC X(64).               \n025492                                                                  \n025494   05  RPT550-SPECS.                                              \n025496       10  RPT550-GEN-AFTER-GRACE        PIC X.                   \n025498       10  FILLER                        PIC X(64).               \n025500   05  OLD-RPT550-SPECS.                                          \n025502       10  OLD-RPT550-GEN-AFTER-GRACE    PIC X.                   \n025504       10  FILLER                        PIC X(64).               \n025506                                                                  \n025508   05  EOYR-SPECS-AREA.                                           \n025510     10  FILLER                          PIC 9(7).                \n025512     10  EOYR-CHK-RECON                  PIC 9(8).                \n025514     10  FILLER                          PIC X(13).               \n025516 01  RMDRPT-REC-9.                                                \n025518     02  Z-VA-RMDRPT-REC-9.                                       \n025520     05  FILLER                PIC  X(00050) VALUE                \n025522     \"*** TIN NUMBER:             TOTALS                \".        \n025524     05  FILLER                PIC  X(00050) VALUE                \n025526     \"                                                  \".        \n025528     05  FILLER                PIC  X(00050) VALUE                \n025530     \"                                                  \".        \n025532     05  FILLER                PIC  X(00010) VALUE                \n025534     \"          \".                                                \n025536     02  Z-NX-RMDRPT-REC-9     REDEFINES Z-VA-RMDRPT-REC-9.       \n025538     05  FILLER                PIC X(0016).                       \n025540     05  RMDRPT-TOT-TIN-9      PIC X(11).                         \n025542     05  FILLER                PIC X(0031).                       \n025544     05  RMDRPT-TIN-TOT-BAL-9  PIC ZZZ,ZZZ,ZZZ.99.                \n025546     05  FILLER                PIC X(0011).                       \n025548     05  RMDRPT-TIN-TOT-RMD-9  PIC ZZ,ZZZ,ZZZ.99.                 \n025550     05  FILLER                PIC X(0064).                       \n025552* 010 LINE RECORD FOLLOWS                                         \n025554 01  RMDRPT-REC-10.                                               \n025556     02  Z-VA-RMDRPT-REC-10.                                      \n025558     05  FILLER                PIC  X(00050) VALUE                \n025560     \"*** TIN NUMBER:                                   \".        \n025562     05  FILLER                PIC  X(00050) VALUE                \n025564     \"                                                  \".        \n025566     05  FILLER                PIC  X(00050) VALUE                \n025568     \"                                                  \".        \n025570     05  FILLER                PIC  X(00010) VALUE                \n025572     \"          \".                                                \n025574     02  Z-NX-RMDRPT-REC-10    REDEFINES Z-VA-RMDRPT-REC-10.      \n025576     05  FILLER                PIC X(0016).                       \n025578     05  RMDRPT-TOT-TIN-10     PIC XXXXXXXXXXX.                   \n025580     05  FILLER                PIC X(0133).                       \n025582 01  RMDRPT-REC-5.                                                \n025584     02  Z-VA-RMDRPT-REC-5.                                       \n025586     05  FILLER                PIC  X(00050) VALUE                \n025588     \" TOTAL # OF ACCTS =                               \".        \n025590     05  FILLER                PIC  X(00050) VALUE                \n025592     \"                                                  \".        \n025594     05  FILLER                PIC  X(00050) VALUE                \n025596     \"                                                  \".        \n025598     05  FILLER                PIC  X(00010) VALUE                \n025600     \"          \".                                                \n025602     02  Z-NX-RMDRPT-REC-5     REDEFINES Z-VA-RMDRPT-REC-5.       \n025604     05  FILLER                PIC X(0020).                       \n025606     05  RMDRPT-CNT-5          PIC ZZZZZZZ9.                      \n025608     05  FILLER                PIC X(0132).                       \n025610* 006 LINE RECORD FOLLOWS                                         \n025612 01  RMDRPT-REC-7.                                                \n025614     02  Z-VA-RMDRPT-REC-7.                                       \n025616     05  FILLER                PIC  X(00050) VALUE                \n025618     \" TOTAL # ACCTS CHANGED =                          \".        \n025620     05  FILLER                PIC  X(00050) VALUE                \n025622     \"                                                  \".        \n025624     05  FILLER                PIC  X(00050) VALUE                \n025626     \"                                                  \".        \n025628     05  FILLER                PIC  X(00010) VALUE                \n025630     \"          \".                                                \n025632     02  Z-NX-RMDRPT-REC-7     REDEFINES Z-VA-RMDRPT-REC-7.       \n025634     05  FILLER                PIC X(0025).                       \n025636     05  RMDRPT-TOT-FM-7       PIC ZZZZZZZ9.                      \n025638     05  FILLER                PIC X(0127).                       \n025640* 008 LINE RECORD FOLLOWS                                         \n025642  01 WS-LE-FACTOR.                                                \n025644     05 WS-LE-FACTOR-X.                                           \n025646        10 WS-LE-FACT-1           PIC 99.                         \n025648        10 WS-LE-FACT-2           PIC 9.                          \n025650     05 WS-LE-FACTOR9 REDEFINES WS-LE-FACTOR-X    PIC 999.        \n025652                                                                  \n025654  01 WS-RMD-LEF-CUTOFF-YR         PIC 9(04) VALUE 2022.           \n025656*\n025658*\n025660 LINKAGE SECTION.\n025662*------- -------\n025664 01 WS-SUFFIX-IN                 PIC X.                           \n025666*\n025668*****************************************************************\n025670 PROCEDURE DIVISION\n025672     USING WS-SUFFIX-IN.\n025674*****************************************************************\n025676*\n025678 Z-INITIALIZATION SECTION.\n025680 Z-INITIALIZATION-PARAGRAPH.\n025682*\n025684     IF Z-RUNNING-FLAG = ZERO\n025686     CHANGE ATTRIBUTE LIBACCESS OF \"GENERALSUPPORT\"\n025688         TO BYFUNCTION\n025690     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n025692         USING Z-CALL-CURRENTDATE\n025694     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT\n025696     COMPUTE Z-DATE-DEFAULT-CC = Z-DATE0-CC\n025698     COMPUTE Z-DATE-DEFAULT-YY = Z-DATE0-YY\n025700     COMPUTE Z-DATE-DEFAULT-MM = Z-DATE0-MM\n025702     COMPUTE Z-DATE-DEFAULT-DD = Z-DATE0-DD\n025704     COMPUTE Z-DATE-CC-CUTOFF = 70.\n025706     PERFORM Z-PROCESS-INIT THRU Z-PROCESS-INIT-XIT.\n025708     MOVE LOW-VALUES TO Z-SAVE-AREA.\n025710     MOVE LOW-VALUES TO Z-TEMPORARY-AREA.\n025712     PERFORM Z-OPEN-DB-1.\n025714     PERFORM Z-OPEN-DB-2.\n025716 Z-DMS2-ABORT.\n025718     MOVE ZERO TO Z-DMS2-ABORT-FLAG.\n025720     PERFORM Z-DMS2-BEGIN-TRANS\n025722        THRU Z-DMS2-BEGIN-TRANS-XIT.\n025724     IF Z-DMS2-ABORT-FLAG = 1\n025726         GO TO Z-DMS2-ABORT.\n025728     MOVE 2 TO Z-DMS2-ET-TYPE.\n025730     PERFORM Z-DMS2-END-TRANS\n025732        THRU Z-DMS2-END-TRANS-XIT.\n025734     IF Z-DMS2-ABORT-FLAG = 1\n025736         GO TO Z-DMS2-ABORT.\n025738     IF Z-RESTART-FLAG = ZERO\n025740         GO TO Z-RESTART-SKIP.\n025742     IF Z-RESTART-PROCESS = 3\n025744         GO TO Z-RESTART-PROCESS-3.\n025746 Z-RESTART-SKIP.\n025748*\n025750**** OPEN FILES\n025752*\n025754     MOVE 1 TO Z-RUNNING-FLAG.\n025756*\n025758*****************************************************************\n025760 Z-MAIN-CONTROL SECTION.\n025762*****************************************************************\n025764 Z-MAIN-CONTROL-PARAGRAPH.\n025766*\n025768*\n025770*\n025772 Z-BEGIN-PROCESS-BLOCK.\n025774*\n025776**** MAIN PROCESS\n025778 Z-RESTART-PROCESS-3.\n025780     PERFORM Z-PROCESS-INIT THRU Z-PROCESS-INIT-XIT.\n025782     PERFORM Z-3-PROCESS THRU Z-3-XIT.\n025784     IF Z-DMS2-ABORT-FLAG = 1\n025786         GO TO Z-DMS2-ABORT.\n025788*\n025790 Z-PROCESS-DONE.\n025792*\n025794     IF Z-NO-PROCESS\n025796         DISPLAY \"NO PROCESS SELECTED\".\n025798*\n025800*****************************************************************\n025802 Z-WRAP-UP SECTION.\n025804*****************************************************************\n025806 Z-WRAP-UP-PARAGRAPH.\n025808*\n025810*\n025812**** CLOSE FILES\n025814*\n025816*\n025818***********  CLOSE OF REPORT FILE  LISTING WITH SAVE\n025820*\n025822     IF  Z-RPTINFO1-OPEN NOT = 0\n025824         CLOSE LISTING WITH SAVE\n025826         MOVE 0 TO Z-RPTINFO1-OPEN\n025828         MOVE 0 TO Z-RPTINFO1-RS-OPEN.\n025830*\n025832***********  CLOSE OF REPORT FILE  FICHE WITH SAVE\n025834*\n025836     IF  Z-RPTINFO2-OPEN NOT = 0\n025838         CLOSE FICHE WITH SAVE\n025840         MOVE 0 TO Z-RPTINFO2-OPEN\n025842         MOVE 0 TO Z-RPTINFO2-RS-OPEN.\n025844*\n025846***********  CLOSE OF FILE BK-SPEC-FILE WITH SAVE\n025848*\n025850     IF Z-FLINFO3-OPEN NOT = 0\n025852         CLOSE BK-SPEC-FILE WITH SAVE\n025854         MOVE 0 TO Z-FLINFO3-OPEN\n025856         MOVE 0 TO Z-FLINFO3-RS-OPEN.\n025858*\n025860***********  CLOSE OF FILE PROC-FILE WITH SAVE\n025862*\n025864     IF Z-FLINFO4-OPEN NOT = 0\n025866         CLOSE PROC-FILE WITH SAVE\n025868         MOVE 0 TO Z-FLINFO4-OPEN\n025870         MOVE 0 TO Z-FLINFO4-RS-OPEN.\n025872*\n025874***********  CLOSE OF FILE DST-FILE-MAINT WITH SAVE\n025876*\n025878     IF Z-FLINFO5-OPEN NOT = 0\n025880         CLOSE DST-FILE-MAINT WITH SAVE\n025882         MOVE 0 TO Z-FLINFO5-OPEN\n025884         MOVE 0 TO Z-FLINFO5-RS-OPEN.\n025886*\n025888***********  CLOSE OF FILE CST-FILE-MAINT WITH SAVE\n025890*\n025892     IF Z-FLINFO6-OPEN NOT = 0\n025894         CLOSE CST-FILE-MAINT WITH SAVE\n025896         MOVE 0 TO Z-FLINFO6-OPEN\n025898         MOVE 0 TO Z-FLINFO6-RS-OPEN.\n025900     MOVE ZERO TO Z-RESTART-PROCESS.\n025902     IF Z-DMS2-TRANS-STATE = ZERO\n025904         PERFORM Z-DMS2-BEGIN-TRANS\n025906            THRU Z-DMS2-BEGIN-TRANS-XIT.\n025908     IF Z-DMS2-ABORT-FLAG = 1\n025910         GO TO Z-DMS2-ABORT.\n025912     MOVE 2 TO Z-DMS2-ET-TYPE.\n025914     PERFORM Z-DMS2-END-TRANS\n025916        THRU Z-DMS2-END-TRANS-XIT.\n025918     IF Z-DMS2-ABORT-FLAG = 1\n025920         GO TO Z-DMS2-ABORT.\n025922     PERFORM Z-CLOSE-DB-1.\n025924     PERFORM Z-CLOSE-DB-2.\n025926*\n025928     MOVE ZERO TO Z-RUNNING-FLAG.\n025930*\n025932 Z-PROGRAM-XIT.\n025934*\n025936     STOP RUN.\n025938*\n025940*****************************************************************\n025942 Z-SUPPORT SECTION.\n025944*****************************************************************\n025946 Z-SUPPORT-PARAGRAPH.\n025948*\n025950 Z-PROCESS-INIT.\n025952*\n025954     MOVE  ZEROS TO Z-FLAGS-AREA.\n025956     MOVE   9999 TO Z-EXIT-LEVEL.\n025958     MOVE  ZEROS TO Z-FLINFO-UPDATES.\n025960*\n025962 Z-PROCESS-INIT-XIT.\n025964     EXIT.\n025966*\n025968 Z-OPEN-DB-1.\n025970     IF Z-DMS1-OPEN = ZERO\n025972     MOVE 1 TO Z-DMS1-OPEN\n025974     OPEN INQUIRY LDBSPCDB\n025976         ON EXCEPTION\n025978         MOVE \"LDBSPCDB\" TO Z-DMS-EXCEPT-STR\n025980         MOVE \"SPCDB\" TO Z-DMS-EXCEPT-DB\n025982         MOVE ZERO TO Z-DMS-EXCEPT-SEQ\n025984         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT\n025986         DISPLAY \">>>>>> ABORT PROGRAM: MINDISTCALC\"\n025988         DISPLAY \">>>>>> AT OPEN INQUIRY DATABASE LDBSPCDB\"\n025990         CHANGE ATTRIBUTE STATUS OF MYSELF TO -1.\n025992*\n025994 Z-OPEN-DB-2.\n025996     IF Z-DMS2-OPEN = ZERO\n025998     MOVE 3 TO Z-DMS2-OPEN\n026000     OPEN UPDATE LDBTDADB\n026002         ON EXCEPTION\n026004         MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-STR\n026006         MOVE \"TDADB\" TO Z-DMS-EXCEPT-DB\n026008         MOVE ZERO TO Z-DMS-EXCEPT-SEQ\n026010         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT\n026012         DISPLAY \">>>>>> ABORT PROGRAM: MINDISTCALC\"\n026014         DISPLAY \">>>>>> AT OPEN UPDATE DATABASE LDBTDADB\"\n026016         CHANGE ATTRIBUTE STATUS OF MYSELF TO -1.\n026018*\n026020 Z-CLOSE-DB-1.\n026022     IF Z-DMS1-OPEN > ZERO\n026024     CLOSE LDBSPCDB\n026026         ON EXCEPTION\n026028         IF  DMSTATUS (ABORT)\n026030             MOVE 1 TO Z-DMS2-ABORT-FLAG\n026032             GO TO Z-DMS2-ABORT\n026034         ELSE\n026036             MOVE \"LDBSPCDB\" TO Z-DMS-EXCEPT-STR\n026038             MOVE \"SPCDB\" TO Z-DMS-EXCEPT-DB\n026040             MOVE ZERO TO Z-DMS-EXCEPT-SEQ\n026042             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n026044     MOVE ZERO TO Z-DMS1-OPEN.\n026046*\n026048*\n026050 Z-CLOSE-DB-2.\n026052     IF Z-DMS2-OPEN > ZERO\n026054     CLOSE LDBTDADB\n026056         ON EXCEPTION\n026058         IF  DMSTATUS (ABORT)\n026060             MOVE ZERO TO Z-DMS2-OPEN\n026062             PERFORM Z-OPEN-DB-2\n026064             MOVE 1 TO Z-DMS2-ABORT-FLAG\n026066             GO TO Z-DMS2-ABORT\n026068         ELSE\n026070             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-STR\n026072             MOVE \"TDADB\" TO Z-DMS-EXCEPT-DB\n026074             MOVE ZERO TO Z-DMS-EXCEPT-SEQ\n026076             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n026078     MOVE ZERO TO Z-DMS2-OPEN.\n026080*\n026082*\n026084**** FILE EXCEPTION\n026086*\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    512 lines from 12528 to 13039.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 27, "total_chunks": 55, "start_line": 12528, "end_line": 13039, "line_count": 512}

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
- Source code length: 33945 characters

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
CHUNK 27 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 12528 to 13039 (512 lines)
Chunk Tokens (estimated): ~7,889
Actual Input Tokens: 9,295 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 12528-13039 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 27 of 55 chunks
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
      The source code below is only CHUNK 27 of 55.


=============================================================================
CHUNK 27 SOURCE CODE (Lines 12528-13039)
=============================================================================

```cobol
025064         OLD-SPECS-CNV-TOT-DNLOAD.                                
025066         15 OLD-SPECS-CNV-TOT-DNLOAD-X   PIC X(08).               
025068     10  FILLER                          PIC X(13).               
025070     10  OLD-SPECS-ADDR-ALERT-DAYS       PIC 999.                 
025072     10  OLD-SPECS-COMB-SEND-CERT        PIC X(1).                
025074     10  OLD-SPECS-APPLY-GRACE-AT-SR     PIC X(1).                
025076     10  OLD-SPECS-DB-SUFFIX             PIC X(1).                
025078     10  OLD-SPECS-EOY-YTD-ROLL          PIC X(1).                
025080     10  OLD-SPECS-COMB-DDA-OPT          PIC X(1).                
025082     10  OLD-SPECS-CONTINUE              PIC X(1).                
025084                                                                  
025086**  SPECS FOR 580 PCR                                             
025088   05  SPECS-580-AREA.                                            
025090     10  SPECS-580-PRT-FORMAT            PIC X(1).                
025092     10  SPECS-580-PRT-ACCT              PIC X(1).                
025094     10  SPECS-580-PROTECT               PIC X(1).                
025096     10  SPECS-580-RATE-1                PIC X(1).                
025098     10  SPECS-580-RATE-2                PIC X(1).                
025100     10  SPECS-580-MAT-DT                PIC X(1).                
025102     10  SPECS-580-GRACE-IN-PROC         PIC X(3).                
025104     10  SPECS-580-SUPPRESS-TIN          PIC X(1).                
025106     10  SPECS-580-PRT-MAT               PIC X(1).                
025108     10  SPECS-580-PRT-DESC              PIC X(1).                
025110     10  SPECS-580-SUPPRESS-TRAILER      PIC X(1).                
025112     10  SPECS-580-PRT-DAYS-IN-CYCLE     PIC X(1).                
025114     10  SPECS-580-PRT-CUST-NO           PIC X(1).                
025116     10  FILLER                          PIC X(50).               
025118   05  OLD-580-AREA.                                              
025120     10  OLD-580-PRT-FORMAT            PIC X(1).                  
025122     10  OLD-580-PRT-ACCT              PIC X(1).                  
025124     10  OLD-580-PROTECT               PIC X(1).                  
025126     10  OLD-580-RATE-1                PIC X(1).                  
025128     10  OLD-580-RATE-2                PIC X(1).                  
025130     10  OLD-580-MAT-DT                PIC X(1).                  
025132     10  OLD-580-GRACE-IN-PROC         PIC X(3).                  
025134     10  OLD-580-SUPPRESS-TIN          PIC X(1).                  
025136     10  OLD-580-PRT-MAT               PIC X(1).                  
025138     10  OLD-580-PRT-DESC              PIC X(1).                  
025140     10  OLD-580-SUPPRESS-TRAILER      PIC X(1).                  
025142     10  OLD-580-PRT-DAYS-IN-CYCLE     PIC X(1).                  
025144     10  OLD-580-PRT-CUST-NO           PIC X(1).                  
025146     10  FILLER                          PIC X(50).               
025148                                                                  
025150**  SPECS FOR 560 PCR                                             
025152   05  WS-SPEC-OPTION.                                            
025154     10  WS-DISPLAY-RATE                 PIC X(01) VALUE "X".     
025156     10  WS-DISP-PRT.                                             
025158         15  WS-PRT-DISP-1               PIC X(01).               
025160         15  WS-PRT-DISP-2               PIC X(01).               
025162         15  WS-PRT-DISP-3               PIC X(01).               
025164         15  WS-PRT-DISP-4               PIC X(01).               
025166         15  WS-PRT-DISP-5               PIC X(01).               
025168         15  WS-PRT-DISP-6               PIC X(01).               
025170     10  WS-NOTICE-TIN-PRT               PIC X(01).               
025172     10  FILLER                          PIC X(57).               
025174   05 OLD-560-AREA.                                               
025176     10  OLD-560-DISPLAY-RATE                 PIC X(01).          
025178     10  OLD-560-DISP-PRT.                                        
025180         15  OLD-560-PRT-DISP-1               PIC X(01).          
025182         15  OLD-560-PRT-DISP-2               PIC X(01).          
025184         15  OLD-560-PRT-DISP-3               PIC X(01).          
025186         15  OLD-560-PRT-DISP-4               PIC X(01).          
025188         15  OLD-560-PRT-DISP-5               PIC X(01).          
025190         15  OLD-560-PRT-DISP-6               PIC X(01).          
025192     10  OLD-560-NOTICE-TIN-PRT               PIC X(01).          
025194     10  FILLER                          PIC X(57).               
025196                                                                  
025198                                                                  
025200**  SPECS FOR 601 PCR                                             
025202   05  RPT601-SPECS.                                              
025204     10  RPT601-APR                      PIC X(01) VALUE " ".     
025206     10  RPT601-NO-TIN                   PIC X(01) VALUE " ".     
025208     10  RPT601-BEG-DT-1                 PIC 9(08) VALUE 0.       
025210     10  RPT601-END-DT-1                 PIC 9(08) VALUE 0.       
025212     10  RPT601-OPT-1                    PIC X(01) VALUE SPACES.  
025214     10  RPT601-BEG-DT-2                 PIC 9(08) VALUE 0.       
025216     10  RPT601-END-DT-2                 PIC 9(08) VALUE 0.       
025218     10  RPT601-OPT-2                    PIC X(01) VALUE SPACE.   
025220     10  RPT601-BEG-DT-3                 PIC 9(08) VALUE 0.       
025222     10  RPT601-END-DT-3                 PIC 9(08) VALUE 0.       
025224     10  RPT601-OPT-3                    PIC X(01) VALUE SPACE.   
025226     10  RPT601-SUPP-DOB                 PIC X(01) VALUE SPACE.   
025228     10  RPT601-SUPP-ACCT                PIC 9(01) VALUE 0.       
025230     10  RPT601-MASK-OPTION              PIC X(01) VALUE SPACE.   
025232     10  RPT601-MASK-CHAR                PIC X(01) VALUE SPACE.   
025234     10  RPT601-MASK-LENGTH              PIC X(01) VALUE SPACE.   
025236     10  FILLER                          PIC X(03) VALUE "   ".   
025238     10  RPT601-TRUNC-TIN                PIC X(01) VALUE " ".     
025240     10  RPT601-PRT-RATE                 PIC X(01) VALUE " ".     
025242     10  RPT601-PRT-APYE-EOY             PIC X(01) VALUE " ".     
025244     10  RPT601-STMT-DET-PRT             PIC X(01) VALUE " ".     
025246                                                                  
025248   05 OLD-601-AREA.                                               
025250     10  OLD-601-APR                     PIC X(01) VALUE SPACES.  
025252     10  OLD-601-NO-TIN                  PIC X(01) VALUE SPACES.  
025254     10  OLD-601-BEG-DT-1                PIC 9(08) VALUE ZEROES.  
025256     10  OLD-601-END-DT-1                PIC 9(08) VALUE ZEROES.  
025258     10  OLD-601-OPT-1                   PIC X(01) VALUE SPACES.  
025260     10  OLD-601-BEG-DT-2                PIC 9(08) VALUE ZEROES.  
025262     10  OLD-601-END-DT-2                PIC 9(08) VALUE ZEROES.  
025264     10  OLD-601-OPT-2                   PIC X(01) VALUE SPACES.  
025266     10  OLD-601-BEG-DT-3                PIC 9(08) VALUE ZEROES.  
025268     10  OLD-601-END-DT-3                PIC 9(08) VALUE ZEROES.  
025270     10  OLD-601-OPT-3                   PIC X(01) VALUE SPACES.  
025272     10  OLD-601-SUPP-DOB                PIC X(01) VALUE SPACES.  
025274     10  OLD-601-SUPP-ACCT               PIC 9(01) VALUE ZEROES.  
025276     10  OLD-601-MASK-OPTION             PIC X(01) VALUE SPACE.   
025278     10  OLD-601-MASK-CHAR               PIC X(01) VALUE SPACE.   
025280     10  OLD-601-MASK-LENGTH             PIC X(01) VALUE SPACE.   
025282     10  FILLER                          PIC X(03) VALUE SPACES.  
025284     10  OLD-601-TRUNC-TIN               PIC X(01) VALUE SPACES.  
025286     10  OLD-601-PRT-RATE                PIC X(01) VALUE SPACES.  
025288     10  OLD-601-PRT-APYE-EOY            PIC X(01) VALUE SPACES.  
025290     10  OLD-601-STMT-DET-PRT            PIC X(01) VALUE SPACES.  
025292                                                                  
025294                                                                  
025296**  SPECS FOR 601 PCR BANK 0000                                   
025298   05  RPT601-CSI-OPTIONS.                                        
025300     10  RPT601-CSI-APR                  PIC X(01) VALUE " ".     
025302     10  RPT601-CSI-TIN                  PIC X(01) VALUE " ".     
025304     10  RPT601-CSI-BEG-DT-1             PIC 9(08) VALUE 0.       
025306     10  RPT601-CSI-END-DT-1             PIC 9(08) VALUE 0.       
025308     10  RPT601-CSI-OPT-1                PIC X(01) VALUE " ".     
025310     10  RPT601-CSI-BEG-DT-2             PIC 9(08) VALUE 0.       
025312     10  RPT601-CSI-END-DT-2             PIC 9(08) VALUE 0.       
025314     10  RPT601-CSI-OPT-2                PIC X(01) VALUE " ".     
025316     10  RPT601-CSI-BEG-DT-3             PIC 9(08) VALUE 0.       
025318     10  RPT601-CSI-END-DT-3             PIC 9(08) VALUE 0.       
025320     10  RPT601-CSI-OPT-3                PIC X(01) VALUE " ".     
025322     10  FILLER                          PIC X(07) VALUE " ".     
025324     10  RPT601-CSI-TRUNC-TIN            PIC X(01) VALUE " ".     
025326     10  RPT601-CSI-PRT-RATE             PIC X(01) VALUE " ".     
025328     10  RPT601-CSI-PRT-APYE-EOY         PIC X(01) VALUE " ".     
025330     10  RPT601-CSI-STMT-DET-PRT         PIC X(01) VALUE " ".     
025332                                                                  
025334**  SPECS FOR 140, 640 PCR                                        
025336   05  WS-RPT640-SPECS-FIELDS.                                    
025338     10  WS-RPT640-SPECS                 PIC X(1).                
025340     10  FILLER                          PIC X(64).               
025342   05 OLD-640-AREA.                                               
025344     10  OLD-640-SPECS                   PIC X(1).                
025346     10  FILLER                          PIC X(64).               
025348                                                                  
025350**  SPECS FOR 090, 091, AND 092 PCRS                              
025352   05  WS-RPT-OPTIONS.                                            
025354     10  WS-SORT-OPT                     PIC X(01) VALUE SPACES.  
025356     10  FILLER                          PIC X(64).               
025358   05  OLD-RPT-OPTIONS.                                           
025360     10  OLD-SORT-OPT                    PIC X(01).               
025362     10  FILLER                          PIC X(64).               
025364                                                                  
025366   05  WS-090-OPTIONS.                                            
025368     10  WS-090-SORT                     PIC X(01) VALUE SPACES.  
025370     10  WS-REQUEST-TRIAL                PIC X(01) VALUE SPACES.  
025372     10  FILLER                          PIC X(63) VALUE SPACES.  
025374   05  OLD-090-AREA.                                              
025376     10  OLD-090-SORT                    PIC X(01).               
025378     10  OLD-090-REQUEST-TRIAL           PIC X(01).               
025380     10  FILLER                          PIC X(63).               
025382                                                                  
025384   05  RPT311-SPECS.                                              
025386     10  RPT311-MONTHLY                  PIC X(01) VALUE SPACES.  
025388     10  FILLER                          PIC X(64).               
025390   05  OLD-RPT311-SPECS.                                          
025392     10  OLD-RPT311-MONTHLY              PIC X(01) VALUE SPACES.  
025394     10  FILLER                          PIC X(64).               
025396                                                                  
025398   05  RPT408-SPECS.                                              
025400     10  RPT408-TOTCD-BYBRCH             PIC X(01) VALUE SPACES.  
025402     10  FILLER                          PIC X(64).               
025404   05  OLD-408-AREA.                                              
025406     10  OLD-408-TOTCD-BYBRCH            PIC X(01).               
025408     10  FILLER                          PIC X(64).               
025410                                                                  
025412   05 RPT410-CLASS-TABLE.                                         
025414    10 RPT410-TABLE OCCURS 65 TIMES.                              
025416       15 TBL410-CLASS-CODE       PIC X(01).                      
025418                                                                  
025420   05  RPT465-SPECS.                                              
025422     10 RPT465-LARGE-TRX-AMT             PIC 9(9)V99 VALUE ZEROS. 
025424     10 RPT465-LARGE-TRX-AMT-9S                                   
025426         REDEFINES RPT465-LARGE-TRX-AMT  PIC 9(11).               
025428     10 FILLER                           PIC X(54).               
025430   05  OLD-465-AREA.                                              
025432     10 OLD-465-LARGE-TRX-AMT            PIC 9(9)V99.             
025434     10 OLD-465-LARGE-TRX-AMT-9S                                  
025436         REDEFINES OLD-465-LARGE-TRX-AMT PIC 9(11).               
025438     10 FILLER                           PIC X(54).               
025440                                                                  
025442                                                                  
025444   05  RPT651-SPECS.                                              
025446     10  RPT651-MMDD-1                   PIC 9(04).               
025448     10  RPT651-MMDD-2                   PIC 9(04).               
025450     10  FILLER                          PIC X(57).               
025452   05  OLD-651-AREA.                                              
025454     10  OLD-651-MMDD-1                  PIC 9(04).               
025456     10  OLD-651-MMDD-2                  PIC 9(04).               
025458     10  FILLER                          PIC X(57).               
025460                                                                  
025462   05  RPT592-SPECS.                                              
025464       10  RPT592-OCT                    PIC X.                   
025466       10  RPT592-NOV                    PIC X.                   
025468       10  FILLER                        PIC X(63).               
025470   05  OLD-RPT592-SPECS.                                          
025472       10  OLD-RPT592-OCT                PIC X.                   
025474       10  OLD-RPT592-NOV                PIC X.                   
025476       10  FILLER                        PIC X(63).               
025478                                                                  
025480   05  RPT412-SPECS.                                              
025482       10  RPT412-ADDL-RPTS-TTLS         PIC X.                   
025484       10  FILLER                        PIC X(64).               
025486   05  OLD-412-AREA.                                              
025488       10  OLD-412-ADDL-RPTS-TTLS        PIC X.                   
025490       10  FILLER                        PIC X(64).               
025492                                                                  
025494   05  RPT550-SPECS.                                              
025496       10  RPT550-GEN-AFTER-GRACE        PIC X.                   
025498       10  FILLER                        PIC X(64).               
025500   05  OLD-RPT550-SPECS.                                          
025502       10  OLD-RPT550-GEN-AFTER-GRACE    PIC X.                   
025504       10  FILLER                        PIC X(64).               
025506                                                                  
025508   05  EOYR-SPECS-AREA.                                           
025510     10  FILLER                          PIC 9(7).                
025512     10  EOYR-CHK-RECON                  PIC 9(8).                
025514     10  FILLER                          PIC X(13).               
025516 01  RMDRPT-REC-9.                                                
025518     02  Z-VA-RMDRPT-REC-9.                                       
025520     05  FILLER                PIC  X(00050) VALUE                
025522     "*** TIN NUMBER:             TOTALS                ".        
025524     05  FILLER                PIC  X(00050) VALUE                
025526     "                                                  ".        
025528     05  FILLER                PIC  X(00050) VALUE                
025530     "                                                  ".        
025532     05  FILLER                PIC  X(00010) VALUE                
025534     "          ".                                                
025536     02  Z-NX-RMDRPT-REC-9     REDEFINES Z-VA-RMDRPT-REC-9.       
025538     05  FILLER                PIC X(0016).                       
025540     05  RMDRPT-TOT-TIN-9      PIC X(11).                         
025542     05  FILLER                PIC X(0031).                       
025544     05  RMDRPT-TIN-TOT-BAL-9  PIC ZZZ,ZZZ,ZZZ.99.                
025546     05  FILLER                PIC X(0011).                       
025548     05  RMDRPT-TIN-TOT-RMD-9  PIC ZZ,ZZZ,ZZZ.99.                 
025550     05  FILLER                PIC X(0064).                       
025552* 010 LINE RECORD FOLLOWS                                         
025554 01  RMDRPT-REC-10.                                               
025556     02  Z-VA-RMDRPT-REC-10.                                      
025558     05  FILLER                PIC  X(00050) VALUE                
025560     "*** TIN NUMBER:                                   ".        
025562     05  FILLER                PIC  X(00050) VALUE                
025564     "                                                  ".        
025566     05  FILLER                PIC  X(00050) VALUE                
025568     "                                                  ".        
025570     05  FILLER                PIC  X(00010) VALUE                
025572     "          ".                                                
025574     02  Z-NX-RMDRPT-REC-10    REDEFINES Z-VA-RMDRPT-REC-10.      
025576     05  FILLER                PIC X(0016).                       
025578     05  RMDRPT-TOT-TIN-10     PIC XXXXXXXXXXX.                   
025580     05  FILLER                PIC X(0133).                       
025582 01  RMDRPT-REC-5.                                                
025584     02  Z-VA-RMDRPT-REC-5.                                       
025586     05  FILLER                PIC  X(00050) VALUE                
025588     " TOTAL # OF ACCTS =                               ".        
025590     05  FILLER                PIC  X(00050) VALUE                
025592     "                                                  ".        
025594     05  FILLER                PIC  X(00050) VALUE                
025596     "                                                  ".        
025598     05  FILLER                PIC  X(00010) VALUE                
025600     "          ".                                                
025602     02  Z-NX-RMDRPT-REC-5     REDEFINES Z-VA-RMDRPT-REC-5.       
025604     05  FILLER                PIC X(0020).                       
025606     05  RMDRPT-CNT-5          PIC ZZZZZZZ9.                      
025608     05  FILLER                PIC X(0132).                       
025610* 006 LINE RECORD FOLLOWS                                         
025612 01  RMDRPT-REC-7.                                                
025614     02  Z-VA-RMDRPT-REC-7.                                       
025616     05  FILLER                PIC  X(00050) VALUE                
025618     " TOTAL # ACCTS CHANGED =                          ".        
025620     05  FILLER                PIC  X(00050) VALUE                
025622     "                                                  ".        
025624     05  FILLER                PIC  X(00050) VALUE                
025626     "                                                  ".        
025628     05  FILLER                PIC  X(00010) VALUE                
025630     "          ".                                                
025632     02  Z-NX-RMDRPT-REC-7     REDEFINES Z-VA-RMDRPT-REC-7.       
025634     05  FILLER                PIC X(0025).                       
025636     05  RMDRPT-TOT-FM-7       PIC ZZZZZZZ9.                      
025638     05  FILLER                PIC X(0127).                       
025640* 008 LINE RECORD FOLLOWS                                         
025642  01 WS-LE-FACTOR.                                                
025644     05 WS-LE-FACTOR-X.                                           
025646        10 WS-LE-FACT-1           PIC 99.                         
025648        10 WS-LE-FACT-2           PIC 9.                          
025650     05 WS-LE-FACTOR9 REDEFINES WS-LE-FACTOR-X    PIC 999.        
025652                                                                  
025654  01 WS-RMD-LEF-CUTOFF-YR         PIC 9(04) VALUE 2022.           
025656*
025658*
025660 LINKAGE SECTION.
025662*------- -------
025664 01 WS-SUFFIX-IN                 PIC X.                           
025666*
025668*****************************************************************
025670 PROCEDURE DIVISION
025672     USING WS-SUFFIX-IN.
025674*****************************************************************
025676*
025678 Z-INITIALIZATION SECTION.
025680 Z-INITIALIZATION-PARAGRAPH.
025682*
025684     IF Z-RUNNING-FLAG = ZERO
025686     CHANGE ATTRIBUTE LIBACCESS OF "GENERALSUPPORT"
025688         TO BYFUNCTION
025690     CALL "CURRENT_DATE OF GENERALSUPPORT"
025692         USING Z-CALL-CURRENTDATE
025694     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT
025696     COMPUTE Z-DATE-DEFAULT-CC = Z-DATE0-CC
025698     COMPUTE Z-DATE-DEFAULT-YY = Z-DATE0-YY
025700     COMPUTE Z-DATE-DEFAULT-MM = Z-DATE0-MM
025702     COMPUTE Z-DATE-DEFAULT-DD = Z-DATE0-DD
025704     COMPUTE Z-DATE-CC-CUTOFF = 70.
025706     PERFORM Z-PROCESS-INIT THRU Z-PROCESS-INIT-XIT.
025708     MOVE LOW-VALUES TO Z-SAVE-AREA.
025710     MOVE LOW-VALUES TO Z-TEMPORARY-AREA.
025712     PERFORM Z-OPEN-DB-1.
025714     PERFORM Z-OPEN-DB-2.
025716 Z-DMS2-ABORT.
025718     MOVE ZERO TO Z-DMS2-ABORT-FLAG.
025720     PERFORM Z-DMS2-BEGIN-TRANS
025722        THRU Z-DMS2-BEGIN-TRANS-XIT.
025724     IF Z-DMS2-ABORT-FLAG = 1
025726         GO TO Z-DMS2-ABORT.
025728     MOVE 2 TO Z-DMS2-ET-TYPE.
025730     PERFORM Z-DMS2-END-TRANS
025732        THRU Z-DMS2-END-TRANS-XIT.
025734     IF Z-DMS2-ABORT-FLAG = 1
025736         GO TO Z-DMS2-ABORT.
025738     IF Z-RESTART-FLAG = ZERO
025740         GO TO Z-RESTART-SKIP.
025742     IF Z-RESTART-PROCESS = 3
025744         GO TO Z-RESTART-PROCESS-3.
025746 Z-RESTART-SKIP.
025748*
025750**** OPEN FILES
025752*
025754     MOVE 1 TO Z-RUNNING-FLAG.
025756*
025758*****************************************************************
025760 Z-MAIN-CONTROL SECTION.
025762*****************************************************************
025764 Z-MAIN-CONTROL-PARAGRAPH.
025766*
025768*
025770*
025772 Z-BEGIN-PROCESS-BLOCK.
025774*
025776**** MAIN PROCESS
025778 Z-RESTART-PROCESS-3.
025780     PERFORM Z-PROCESS-INIT THRU Z-PROCESS-INIT-XIT.
025782     PERFORM Z-3-PROCESS THRU Z-3-XIT.
025784     IF Z-DMS2-ABORT-FLAG = 1
025786         GO TO Z-DMS2-ABORT.
025788*
025790 Z-PROCESS-DONE.
025792*
025794     IF Z-NO-PROCESS
025796         DISPLAY "NO PROCESS SELECTED".
025798*
025800*****************************************************************
025802 Z-WRAP-UP SECTION.
025804*****************************************************************
025806 Z-WRAP-UP-PARAGRAPH.
025808*
025810*
025812**** CLOSE FILES
025814*
025816*
025818***********  CLOSE OF REPORT FILE  LISTING WITH SAVE
025820*
025822     IF  Z-RPTINFO1-OPEN NOT = 0
025824         CLOSE LISTING WITH SAVE
025826         MOVE 0 TO Z-RPTINFO1-OPEN
025828         MOVE 0 TO Z-RPTINFO1-RS-OPEN.
025830*
025832***********  CLOSE OF REPORT FILE  FICHE WITH SAVE
025834*
025836     IF  Z-RPTINFO2-OPEN NOT = 0
025838         CLOSE FICHE WITH SAVE
025840         MOVE 0 TO Z-RPTINFO2-OPEN
025842         MOVE 0 TO Z-RPTINFO2-RS-OPEN.
025844*
025846***********  CLOSE OF FILE BK-SPEC-FILE WITH SAVE
025848*
025850     IF Z-FLINFO3-OPEN NOT = 0
025852         CLOSE BK-SPEC-FILE WITH SAVE
025854         MOVE 0 TO Z-FLINFO3-OPEN
025856         MOVE 0 TO Z-FLINFO3-RS-OPEN.
025858*
025860***********  CLOSE OF FILE PROC-FILE WITH SAVE
025862*
025864     IF Z-FLINFO4-OPEN NOT = 0
025866         CLOSE PROC-FILE WITH SAVE
025868         MOVE 0 TO Z-FLINFO4-OPEN
025870         MOVE 0 TO Z-FLINFO4-RS-OPEN.
025872*
025874***********  CLOSE OF FILE DST-FILE-MAINT WITH SAVE
025876*
025878     IF Z-FLINFO5-OPEN NOT = 0
025880         CLOSE DST-FILE-MAINT WITH SAVE
025882         MOVE 0 TO Z-FLINFO5-OPEN
025884         MOVE 0 TO Z-FLINFO5-RS-OPEN.
025886*
025888***********  CLOSE OF FILE CST-FILE-MAINT WITH SAVE
025890*
025892     IF Z-FLINFO6-OPEN NOT = 0
025894         CLOSE CST-FILE-MAINT WITH SAVE
025896         MOVE 0 TO Z-FLINFO6-OPEN
025898         MOVE 0 TO Z-FLINFO6-RS-OPEN.
025900     MOVE ZERO TO Z-RESTART-PROCESS.
025902     IF Z-DMS2-TRANS-STATE = ZERO
025904         PERFORM Z-DMS2-BEGIN-TRANS
025906            THRU Z-DMS2-BEGIN-TRANS-XIT.
025908     IF Z-DMS2-ABORT-FLAG = 1
025910         GO TO Z-DMS2-ABORT.
025912     MOVE 2 TO Z-DMS2-ET-TYPE.
025914     PERFORM Z-DMS2-END-TRANS
025916        THRU Z-DMS2-END-TRANS-XIT.
025918     IF Z-DMS2-ABORT-FLAG = 1
025920         GO TO Z-DMS2-ABORT.
025922     PERFORM Z-CLOSE-DB-1.
025924     PERFORM Z-CLOSE-DB-2.
025926*
025928     MOVE ZERO TO Z-RUNNING-FLAG.
025930*
025932 Z-PROGRAM-XIT.
025934*
025936     STOP RUN.
025938*
025940*****************************************************************
025942 Z-SUPPORT SECTION.
025944*****************************************************************
025946 Z-SUPPORT-PARAGRAPH.
025948*
025950 Z-PROCESS-INIT.
025952*
025954     MOVE  ZEROS TO Z-FLAGS-AREA.
025956     MOVE   9999 TO Z-EXIT-LEVEL.
025958     MOVE  ZEROS TO Z-FLINFO-UPDATES.
025960*
025962 Z-PROCESS-INIT-XIT.
025964     EXIT.
025966*
025968 Z-OPEN-DB-1.
025970     IF Z-DMS1-OPEN = ZERO
025972     MOVE 1 TO Z-DMS1-OPEN
025974     OPEN INQUIRY LDBSPCDB
025976         ON EXCEPTION
025978         MOVE "LDBSPCDB" TO Z-DMS-EXCEPT-STR
025980         MOVE "SPCDB" TO Z-DMS-EXCEPT-DB
025982         MOVE ZERO TO Z-DMS-EXCEPT-SEQ
025984         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT
025986         DISPLAY ">>>>>> ABORT PROGRAM: MINDISTCALC"
025988         DISPLAY ">>>>>> AT OPEN INQUIRY DATABASE LDBSPCDB"
025990         CHANGE ATTRIBUTE STATUS OF MYSELF TO -1.
025992*
025994 Z-OPEN-DB-2.
025996     IF Z-DMS2-OPEN = ZERO
025998     MOVE 3 TO Z-DMS2-OPEN
026000     OPEN UPDATE LDBTDADB
026002         ON EXCEPTION
026004         MOVE "LDBTDADB" TO Z-DMS-EXCEPT-STR
026006         MOVE "TDADB" TO Z-DMS-EXCEPT-DB
026008         MOVE ZERO TO Z-DMS-EXCEPT-SEQ
026010         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT
026012         DISPLAY ">>>>>> ABORT PROGRAM: MINDISTCALC"
026014         DISPLAY ">>>>>> AT OPEN UPDATE DATABASE LDBTDADB"
026016         CHANGE ATTRIBUTE STATUS OF MYSELF TO -1.
026018*
026020 Z-CLOSE-DB-1.
026022     IF Z-DMS1-OPEN > ZERO
026024     CLOSE LDBSPCDB
026026         ON EXCEPTION
026028         IF  DMSTATUS (ABORT)
026030             MOVE 1 TO Z-DMS2-ABORT-FLAG
026032             GO TO Z-DMS2-ABORT
026034         ELSE
026036             MOVE "LDBSPCDB" TO Z-DMS-EXCEPT-STR
026038             MOVE "SPCDB" TO Z-DMS-EXCEPT-DB
026040             MOVE ZERO TO Z-DMS-EXCEPT-SEQ
026042             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
026044     MOVE ZERO TO Z-DMS1-OPEN.
026046*
026048*
026050 Z-CLOSE-DB-2.
026052     IF Z-DMS2-OPEN > ZERO
026054     CLOSE LDBTDADB
026056         ON EXCEPTION
026058         IF  DMSTATUS (ABORT)
026060             MOVE ZERO TO Z-DMS2-OPEN
026062             PERFORM Z-OPEN-DB-2
026064             MOVE 1 TO Z-DMS2-ABORT-FLAG
026066             GO TO Z-DMS2-ABORT
026068         ELSE
026070             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-STR
026072             MOVE "TDADB" TO Z-DMS-EXCEPT-DB
026074             MOVE ZERO TO Z-DMS-EXCEPT-SEQ
026076             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
026078     MOVE ZERO TO Z-DMS2-OPEN.
026080*
026082*
026084**** FILE EXCEPTION
026086*
```

⚠️  This is the source code you must document.
    512 lines from 12528 to 13039.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

