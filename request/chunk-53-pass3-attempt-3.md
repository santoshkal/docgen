# LLM Request Debug File
Generated: 2025-11-17T22:46:20.753308

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 53/55
- **Model**: gpt-4.1
- **Chunk Number**: 53
- **Pass Number**: 3
- **Attempt Number**: 3 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~7,010 tokens
- **Total Input**: ~8,968 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 53/55" (ID: detailed-code-explanation)

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


**CHUNK 53 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-17T19:50:50.832678", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 53 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 25460 to 25987 (528 lines)\nChunk Tokens (estimated): ~8,076\nActual Input Tokens: 9,482 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 25460-25987 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 53 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 53 of 55.\n\n\n=============================================================================\nCHUNK 53 SOURCE CODE (Lines 25460-25987)\n=============================================================================\n\n```cobol\n050928 Z-35-2-109-ELSE.\n050930     IF HOLD-TDA-ACTVC-CODE = 0290\n050932         NEXT SENTENCE ELSE\n050934         GO TO Z-35-2-110-ELSE.\n050936     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-ST-INT-CD.\n050938     GO TO Z-35-2-ENDIF.\n050940 Z-35-2-110-ELSE.\n050942     IF HOLD-TDA-ACTVC-CODE = 0291\n050944         NEXT SENTENCE ELSE\n050946         GO TO Z-35-2-111-ELSE.\n050948     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-ST-WHLD-CD.\n050950     GO TO Z-35-2-ENDIF.\n050952 Z-35-2-111-ELSE.\n050954     IF HOLD-TDA-ACTVC-CODE = 0292\n050956         NEXT SENTENCE ELSE\n050958         GO TO Z-35-2-112-ELSE.\n050960     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-ST-WHLD-AMT.\n050962     GO TO Z-35-2-ENDIF.\n050964 Z-35-2-112-ELSE.\n050966     IF HOLD-TDA-ACTVC-CODE = 0293\n050968         NEXT SENTENCE ELSE\n050970         GO TO Z-35-2-113-ELSE.\n050972     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-ST-CUR-W-AMT.\n050974     GO TO Z-35-2-ENDIF.\n050976 Z-35-2-113-ELSE.\n050978     IF HOLD-TDA-ACTVC-CODE = 0294\n050980         NEXT SENTENCE ELSE\n050982         GO TO Z-35-2-114-ELSE.\n050984     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-ST-LST-W-AMT.\n050986     GO TO Z-35-2-ENDIF.\n050988 Z-35-2-114-ELSE.\n050990     IF HOLD-TDA-ACTVC-CODE = 0295\n050992         NEXT SENTENCE ELSE\n050994         GO TO Z-35-2-115-ELSE.\n050996     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-ST-WHLD-STD.\n050998     GO TO Z-35-2-ENDIF.\n051000 Z-35-2-115-ELSE.\n051002     IF HOLD-TDA-ACTVC-CODE = 0296\n051004         NEXT SENTENCE ELSE\n051006         GO TO Z-35-2-116-ELSE.\n051008     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-ST-WHLD-YTD.\n051010     GO TO Z-35-2-ENDIF.\n051012 Z-35-2-116-ELSE.\n051014     IF HOLD-TDA-ACTVC-CODE = 0301\n051016         NEXT SENTENCE ELSE\n051018         GO TO Z-35-2-117-ELSE.\n051020     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-PENLTY-CD.\n051022     GO TO Z-35-2-ENDIF.\n051024 Z-35-2-117-ELSE.\n051026     IF HOLD-TDA-ACTVC-CODE = 0372\n051028         NEXT SENTENCE ELSE\n051030         GO TO Z-35-2-118-ELSE.\n051032     MOVE WS-CHG-WK-9-10 TO HOLD-TDAA-CS-ACCT.\n051034     GO TO Z-35-2-ENDIF.\n051036 Z-35-2-118-ELSE.\n051038     IF HOLD-TDA-ACTVC-CODE = 0375\n051040         NEXT SENTENCE ELSE\n051042         GO TO Z-35-2-119-ELSE.\n051044     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-NO-COMB-IRS.\n051046     GO TO Z-35-2-ENDIF.\n051048 Z-35-2-119-ELSE.\n051050     IF HOLD-TDA-ACTVC-CODE = 0401\n051052         NEXT SENTENCE ELSE\n051054         GO TO Z-35-2-120-ELSE.\n051056     MOVE WS-CHG-WK-X-1 TO HOLD-TDAI-UNINSURED.\n051058     GO TO Z-35-2-ENDIF.\n051060 Z-35-2-120-ELSE.\n051062     IF HOLD-TDA-ACTVC-CODE = 0402\n051064         NEXT SENTENCE ELSE\n051066         GO TO Z-35-2-121-ELSE.\n051068     MOVE WS-CHG-WK-9-5 TO HOLD-TDAI-DS-C-YTD-CNT.\n051070     GO TO Z-35-2-ENDIF.\n051072 Z-35-2-121-ELSE.\n051074     IF HOLD-TDA-ACTVC-CODE = 0403\n051076         NEXT SENTENCE ELSE\n051078         GO TO Z-35-2-122-ELSE.\n051080     MOVE WS-CHG-WK-9-5 TO HOLD-TDAI-DS-P-YTD-CNT.\n051082     GO TO Z-35-2-ENDIF.\n051084 Z-35-2-122-ELSE.\n051086     IF HOLD-TDA-ACTVC-CODE = 0404\n051088         NEXT SENTENCE ELSE\n051090         GO TO Z-35-2-123-ELSE.\n051092     MOVE WS-CHG-WK-9-5 TO HOLD-TDAI-CN-YTD-CNT.\n051094     GO TO Z-35-2-ENDIF.\n051096 Z-35-2-123-ELSE.\n051098     IF HOLD-TDA-ACTVC-CODE = 0405\n051100         NEXT SENTENCE ELSE\n051102         GO TO Z-35-2-124-ELSE.\n051104     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-CN-YTD-AMT.\n051106     GO TO Z-35-2-ENDIF.\n051108 Z-35-2-124-ELSE.\n051110     IF HOLD-TDA-ACTVC-CODE = 0406\n051112         NEXT SENTENCE ELSE\n051114         GO TO Z-35-2-125-ELSE.\n051116     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-CN-LYTD-AMT.\n051118     GO TO Z-35-2-ENDIF.\n051120 Z-35-2-125-ELSE.\n051122     IF HOLD-TDA-ACTVC-CODE = 0407\n051124         NEXT SENTENCE ELSE\n051126         GO TO Z-35-2-126-ELSE.\n051128     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-AMT-C-YTD.\n051130     GO TO Z-35-2-ENDIF.\n051132 Z-35-2-126-ELSE.\n051134     IF HOLD-TDA-ACTVC-CODE = 0408\n051136         NEXT SENTENCE ELSE\n051138         GO TO Z-35-2-127-ELSE.\n051140     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-AMT-P-YTD.\n051142     GO TO Z-35-2-ENDIF.\n051144 Z-35-2-127-ELSE.\n051146     IF HOLD-TDA-ACTVC-CODE = 0409\n051148         NEXT SENTENCE ELSE\n051150         GO TO Z-35-2-128-ELSE.\n051152     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-INT-AMT.\n051154     GO TO Z-35-2-ENDIF.\n051156 Z-35-2-128-ELSE.\n051158     IF HOLD-TDA-ACTVC-CODE = 0411\n051160         NEXT SENTENCE ELSE\n051162         GO TO Z-35-2-129-ELSE.\n051164     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (1).\n051166     GO TO Z-35-2-ENDIF.\n051168 Z-35-2-129-ELSE.\n051170     IF HOLD-TDA-ACTVC-CODE = 0412\n051172         NEXT SENTENCE ELSE\n051174         GO TO Z-35-2-130-ELSE.\n051176     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (2).\n051178     GO TO Z-35-2-ENDIF.\n051180 Z-35-2-130-ELSE.\n051182     IF HOLD-TDA-ACTVC-CODE = 0413\n051184         NEXT SENTENCE ELSE\n051186         GO TO Z-35-2-131-ELSE.\n051188     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (3).\n051190     GO TO Z-35-2-ENDIF.\n051192 Z-35-2-131-ELSE.\n051194     IF HOLD-TDA-ACTVC-CODE = 0414\n051196         NEXT SENTENCE ELSE\n051198         GO TO Z-35-2-132-ELSE.\n051200     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (4).\n051202     GO TO Z-35-2-ENDIF.\n051204 Z-35-2-132-ELSE.\n051206     IF HOLD-TDA-ACTVC-CODE = 0415\n051208         NEXT SENTENCE ELSE\n051210         GO TO Z-35-2-133-ELSE.\n051212     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (5).\n051214     GO TO Z-35-2-ENDIF.\n051216 Z-35-2-133-ELSE.\n051218     IF HOLD-TDA-ACTVC-CODE = 0416\n051220         NEXT SENTENCE ELSE\n051222         GO TO Z-35-2-134-ELSE.\n051224     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (6).\n051226     GO TO Z-35-2-ENDIF.\n051228 Z-35-2-134-ELSE.\n051230     IF HOLD-TDA-ACTVC-CODE = 0417\n051232         NEXT SENTENCE ELSE\n051234         GO TO Z-35-2-135-ELSE.\n051236     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (7).\n051238     GO TO Z-35-2-ENDIF.\n051240 Z-35-2-135-ELSE.\n051242     IF HOLD-TDA-ACTVC-CODE = 0418\n051244         NEXT SENTENCE ELSE\n051246         GO TO Z-35-2-136-ELSE.\n051248     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (8).\n051250     GO TO Z-35-2-ENDIF.\n051252 Z-35-2-136-ELSE.\n051254     IF HOLD-TDA-ACTVC-CODE = 0419\n051256         NEXT SENTENCE ELSE\n051258         GO TO Z-35-2-137-ELSE.\n051260     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (9).\n051262     GO TO Z-35-2-ENDIF.\n051264 Z-35-2-137-ELSE.\n051266     IF HOLD-TDA-ACTVC-CODE = 0420\n051268         NEXT SENTENCE ELSE\n051270         GO TO Z-35-2-138-ELSE.\n051272     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (10).\n051274     GO TO Z-35-2-ENDIF.\n051276 Z-35-2-138-ELSE.\n051278     IF HOLD-TDA-ACTVC-CODE = 0421\n051280         NEXT SENTENCE ELSE\n051282         GO TO Z-35-2-139-ELSE.\n051284     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (11).\n051286     GO TO Z-35-2-ENDIF.\n051288 Z-35-2-139-ELSE.\n051290     IF HOLD-TDA-ACTVC-CODE = 0422\n051292         NEXT SENTENCE ELSE\n051294         GO TO Z-35-2-140-ELSE.\n051296     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (12).\n051298     GO TO Z-35-2-ENDIF.\n051300 Z-35-2-140-ELSE.\n051302     IF HOLD-TDA-ACTVC-CODE = 0423\n051304         NEXT SENTENCE ELSE\n051306         GO TO Z-35-2-141-ELSE.\n051308     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (13).\n051310     GO TO Z-35-2-ENDIF.\n051312 Z-35-2-141-ELSE.\n051314     IF HOLD-TDA-ACTVC-CODE = 0424\n051316         NEXT SENTENCE ELSE\n051318         GO TO Z-35-2-142-ELSE.\n051320     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (14).\n051322     GO TO Z-35-2-ENDIF.\n051324 Z-35-2-142-ELSE.\n051326     IF HOLD-TDA-ACTVC-CODE = 0425\n051328         NEXT SENTENCE ELSE\n051330         GO TO Z-35-2-143-ELSE.\n051332     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (15).\n051334     GO TO Z-35-2-ENDIF.\n051336 Z-35-2-143-ELSE.\n051338     IF HOLD-TDA-ACTVC-CODE = 0426\n051340         NEXT SENTENCE ELSE\n051342         GO TO Z-35-2-144-ELSE.\n051344     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (16).\n051346     GO TO Z-35-2-ENDIF.\n051348 Z-35-2-144-ELSE.\n051350     IF HOLD-TDA-ACTVC-CODE = 0427\n051352         NEXT SENTENCE ELSE\n051354         GO TO Z-35-2-145-ELSE.\n051356     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (17).\n051358     GO TO Z-35-2-ENDIF.\n051360 Z-35-2-145-ELSE.\n051362     IF HOLD-TDA-ACTVC-CODE = 0428\n051364         NEXT SENTENCE ELSE\n051366         GO TO Z-35-2-146-ELSE.\n051368     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (18).\n051370     GO TO Z-35-2-ENDIF.\n051372 Z-35-2-146-ELSE.\n051374     IF HOLD-TDA-ACTVC-CODE = 0429\n051376         NEXT SENTENCE ELSE\n051378         GO TO Z-35-2-147-ELSE.\n051380     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (19).\n051382     GO TO Z-35-2-ENDIF.\n051384 Z-35-2-147-ELSE.\n051386     IF HOLD-TDA-ACTVC-CODE = 0430\n051388         NEXT SENTENCE ELSE\n051390         GO TO Z-35-2-148-ELSE.\n051392     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (20).\n051394     GO TO Z-35-2-ENDIF.\n051396 Z-35-2-148-ELSE.\n051398     IF HOLD-TDA-ACTVC-CODE = 0441\n051400         NEXT SENTENCE ELSE\n051402         GO TO Z-35-2-149-ELSE.\n051404     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (1).\n051406     GO TO Z-35-2-ENDIF.\n051408 Z-35-2-149-ELSE.\n051410     IF HOLD-TDA-ACTVC-CODE = 0442\n051412         NEXT SENTENCE ELSE\n051414         GO TO Z-35-2-150-ELSE.\n051416     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (2).\n051418     GO TO Z-35-2-ENDIF.\n051420 Z-35-2-150-ELSE.\n051422     IF HOLD-TDA-ACTVC-CODE = 0443\n051424         NEXT SENTENCE ELSE\n051426         GO TO Z-35-2-151-ELSE.\n051428     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (3).\n051430     GO TO Z-35-2-ENDIF.\n051432 Z-35-2-151-ELSE.\n051434     IF HOLD-TDA-ACTVC-CODE = 0444\n051436         NEXT SENTENCE ELSE\n051438         GO TO Z-35-2-152-ELSE.\n051440     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (4).\n051442     GO TO Z-35-2-ENDIF.\n051444 Z-35-2-152-ELSE.\n051446     IF HOLD-TDA-ACTVC-CODE = 0445\n051448         NEXT SENTENCE ELSE\n051450         GO TO Z-35-2-153-ELSE.\n051452     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (5).\n051454     GO TO Z-35-2-ENDIF.\n051456 Z-35-2-153-ELSE.\n051458     IF HOLD-TDA-ACTVC-CODE = 0446\n051460         NEXT SENTENCE ELSE\n051462         GO TO Z-35-2-154-ELSE.\n051464     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (6).\n051466     GO TO Z-35-2-ENDIF.\n051468 Z-35-2-154-ELSE.\n051470     IF HOLD-TDA-ACTVC-CODE = 0447\n051472         NEXT SENTENCE ELSE\n051474         GO TO Z-35-2-155-ELSE.\n051476     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (7).\n051478     GO TO Z-35-2-ENDIF.\n051480 Z-35-2-155-ELSE.\n051482     IF HOLD-TDA-ACTVC-CODE = 0448\n051484         NEXT SENTENCE ELSE\n051486         GO TO Z-35-2-156-ELSE.\n051488     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (8).\n051490     GO TO Z-35-2-ENDIF.\n051492 Z-35-2-156-ELSE.\n051494     IF HOLD-TDA-ACTVC-CODE = 0449\n051496         NEXT SENTENCE ELSE\n051498         GO TO Z-35-2-157-ELSE.\n051500     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (9).\n051502     GO TO Z-35-2-ENDIF.\n051504 Z-35-2-157-ELSE.\n051506     IF HOLD-TDA-ACTVC-CODE = 0450\n051508         NEXT SENTENCE ELSE\n051510         GO TO Z-35-2-158-ELSE.\n051512     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (10).\n051514     GO TO Z-35-2-ENDIF.\n051516 Z-35-2-158-ELSE.\n051518     IF HOLD-TDA-ACTVC-CODE = 0451\n051520         NEXT SENTENCE ELSE\n051522         GO TO Z-35-2-159-ELSE.\n051524     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (11).\n051526     GO TO Z-35-2-ENDIF.\n051528 Z-35-2-159-ELSE.\n051530     IF HOLD-TDA-ACTVC-CODE = 0452\n051532         NEXT SENTENCE ELSE\n051534         GO TO Z-35-2-160-ELSE.\n051536     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (12).\n051538     GO TO Z-35-2-ENDIF.\n051540 Z-35-2-160-ELSE.\n051542     IF HOLD-TDA-ACTVC-CODE = 0453\n051544         NEXT SENTENCE ELSE\n051546         GO TO Z-35-2-161-ELSE.\n051548     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (13).\n051550     GO TO Z-35-2-ENDIF.\n051552 Z-35-2-161-ELSE.\n051554     IF HOLD-TDA-ACTVC-CODE = 0454\n051556         NEXT SENTENCE ELSE\n051558         GO TO Z-35-2-162-ELSE.\n051560     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (14).\n051562     GO TO Z-35-2-ENDIF.\n051564 Z-35-2-162-ELSE.\n051566     IF HOLD-TDA-ACTVC-CODE = 0455\n051568         NEXT SENTENCE ELSE\n051570         GO TO Z-35-2-163-ELSE.\n051572     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (15).\n051574     GO TO Z-35-2-ENDIF.\n051576 Z-35-2-163-ELSE.\n051578     IF HOLD-TDA-ACTVC-CODE = 0456\n051580         NEXT SENTENCE ELSE\n051582         GO TO Z-35-2-164-ELSE.\n051584     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (16).\n051586     GO TO Z-35-2-ENDIF.\n051588 Z-35-2-164-ELSE.\n051590     IF HOLD-TDA-ACTVC-CODE = 0457\n051592         NEXT SENTENCE ELSE\n051594         GO TO Z-35-2-165-ELSE.\n051596     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (17).\n051598     GO TO Z-35-2-ENDIF.\n051600 Z-35-2-165-ELSE.\n051602     IF HOLD-TDA-ACTVC-CODE = 0458\n051604         NEXT SENTENCE ELSE\n051606         GO TO Z-35-2-166-ELSE.\n051608     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (18).\n051610     GO TO Z-35-2-ENDIF.\n051612 Z-35-2-166-ELSE.\n051614     IF HOLD-TDA-ACTVC-CODE = 0459\n051616         NEXT SENTENCE ELSE\n051618         GO TO Z-35-2-167-ELSE.\n051620     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (19).\n051622     GO TO Z-35-2-ENDIF.\n051624 Z-35-2-167-ELSE.\n051626     IF HOLD-TDA-ACTVC-CODE = 0460\n051628         NEXT SENTENCE ELSE\n051630         GO TO Z-35-2-168-ELSE.\n051632     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (20).\n051634     GO TO Z-35-2-ENDIF.\n051636 Z-35-2-168-ELSE.\n051638     IF HOLD-TDA-ACTVC-CODE = 0471\n051640         NEXT SENTENCE ELSE\n051642         GO TO Z-35-2-169-ELSE.\n051644     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (1).\n051646     GO TO Z-35-2-ENDIF.\n051648 Z-35-2-169-ELSE.\n051650     IF HOLD-TDA-ACTVC-CODE = 0472\n051652         NEXT SENTENCE ELSE\n051654         GO TO Z-35-2-170-ELSE.\n051656     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (2).\n051658     GO TO Z-35-2-ENDIF.\n051660 Z-35-2-170-ELSE.\n051662     IF HOLD-TDA-ACTVC-CODE = 0473\n051664         NEXT SENTENCE ELSE\n051666         GO TO Z-35-2-171-ELSE.\n051668     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (3).\n051670     GO TO Z-35-2-ENDIF.\n051672 Z-35-2-171-ELSE.\n051674     IF HOLD-TDA-ACTVC-CODE = 0474\n051676         NEXT SENTENCE ELSE\n051678         GO TO Z-35-2-172-ELSE.\n051680     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (4).\n051682     GO TO Z-35-2-ENDIF.\n051684 Z-35-2-172-ELSE.\n051686     IF HOLD-TDA-ACTVC-CODE = 0475\n051688         NEXT SENTENCE ELSE\n051690         GO TO Z-35-2-173-ELSE.\n051692     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (5).\n051694     GO TO Z-35-2-ENDIF.\n051696 Z-35-2-173-ELSE.\n051698     IF HOLD-TDA-ACTVC-CODE = 0476\n051700         NEXT SENTENCE ELSE\n051702         GO TO Z-35-2-174-ELSE.\n051704     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (6).\n051706     GO TO Z-35-2-ENDIF.\n051708 Z-35-2-174-ELSE.\n051710     IF HOLD-TDA-ACTVC-CODE = 0477\n051712         NEXT SENTENCE ELSE\n051714         GO TO Z-35-2-175-ELSE.\n051716     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (7).\n051718     GO TO Z-35-2-ENDIF.\n051720 Z-35-2-175-ELSE.\n051722     IF HOLD-TDA-ACTVC-CODE = 0478\n051724         NEXT SENTENCE ELSE\n051726         GO TO Z-35-2-176-ELSE.\n051728     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (8).\n051730     GO TO Z-35-2-ENDIF.\n051732 Z-35-2-176-ELSE.\n051734     IF HOLD-TDA-ACTVC-CODE = 0479\n051736         NEXT SENTENCE ELSE\n051738         GO TO Z-35-2-177-ELSE.\n051740     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (9).\n051742     GO TO Z-35-2-ENDIF.\n051744 Z-35-2-177-ELSE.\n051746     IF HOLD-TDA-ACTVC-CODE = 0480\n051748         NEXT SENTENCE ELSE\n051750         GO TO Z-35-2-178-ELSE.\n051752     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (10).\n051754     GO TO Z-35-2-ENDIF.\n051756 Z-35-2-178-ELSE.\n051758     IF HOLD-TDA-ACTVC-CODE = 0481\n051760         NEXT SENTENCE ELSE\n051762         GO TO Z-35-2-179-ELSE.\n051764     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (11).\n051766     GO TO Z-35-2-ENDIF.\n051768 Z-35-2-179-ELSE.\n051770     IF HOLD-TDA-ACTVC-CODE = 0482\n051772         NEXT SENTENCE ELSE\n051774         GO TO Z-35-2-180-ELSE.\n051776     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (12).\n051778     GO TO Z-35-2-ENDIF.\n051780 Z-35-2-180-ELSE.\n051782     IF HOLD-TDA-ACTVC-CODE = 0483\n051784         NEXT SENTENCE ELSE\n051786         GO TO Z-35-2-181-ELSE.\n051788     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (13).\n051790     GO TO Z-35-2-ENDIF.\n051792 Z-35-2-181-ELSE.\n051794     IF HOLD-TDA-ACTVC-CODE = 0484\n051796         NEXT SENTENCE ELSE\n051798         GO TO Z-35-2-182-ELSE.\n051800     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (14).\n051802     GO TO Z-35-2-ENDIF.\n051804 Z-35-2-182-ELSE.\n051806     IF HOLD-TDA-ACTVC-CODE = 0485\n051808         NEXT SENTENCE ELSE\n051810         GO TO Z-35-2-183-ELSE.\n051812     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (15).\n051814     GO TO Z-35-2-ENDIF.\n051816 Z-35-2-183-ELSE.\n051818     IF HOLD-TDA-ACTVC-CODE = 0486\n051820         NEXT SENTENCE ELSE\n051822         GO TO Z-35-2-184-ELSE.\n051824     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (16).\n051826     GO TO Z-35-2-ENDIF.\n051828 Z-35-2-184-ELSE.\n051830     IF HOLD-TDA-ACTVC-CODE = 0487\n051832         NEXT SENTENCE ELSE\n051834         GO TO Z-35-2-185-ELSE.\n051836     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (17).\n051838     GO TO Z-35-2-ENDIF.\n051840 Z-35-2-185-ELSE.\n051842     IF HOLD-TDA-ACTVC-CODE = 0488\n051844         NEXT SENTENCE ELSE\n051846         GO TO Z-35-2-186-ELSE.\n051848     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (18).\n051850     GO TO Z-35-2-ENDIF.\n051852 Z-35-2-186-ELSE.\n051854     IF HOLD-TDA-ACTVC-CODE = 0489\n051856         NEXT SENTENCE ELSE\n051858         GO TO Z-35-2-187-ELSE.\n051860     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (19).\n051862     GO TO Z-35-2-ENDIF.\n051864 Z-35-2-187-ELSE.\n051866     IF HOLD-TDA-ACTVC-CODE = 0490\n051868         NEXT SENTENCE ELSE\n051870         GO TO Z-35-2-188-ELSE.\n051872     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (20).\n051874     GO TO Z-35-2-ENDIF.\n051876 Z-35-2-188-ELSE.\n051878     IF HOLD-TDA-ACTVC-CODE = 0501\n051880         NEXT SENTENCE ELSE\n051882         GO TO Z-35-2-189-ELSE.\n051884     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-RR-CYC-NBR.\n051886     GO TO Z-35-2-ENDIF.\n051888 Z-35-2-189-ELSE.\n051890     IF HOLD-TDA-ACTVC-CODE = 0502\n051892         NEXT SENTENCE ELSE\n051894         GO TO Z-35-2-190-ELSE.\n051896     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-IGL-GRP.\n051898     GO TO Z-35-2-ENDIF.\n051900 Z-35-2-190-ELSE.\n051902     IF HOLD-TDA-ACTVC-CODE = 0503\n051904         NEXT SENTENCE ELSE\n051906         GO TO Z-35-2-191-ELSE.\n051908     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-ACCT-OPTION.\n051910     GO TO Z-35-2-ENDIF.\n051912 Z-35-2-191-ELSE.\n051914     IF HOLD-TDA-ACTVC-CODE = 0505\n051916         NEXT SENTENCE ELSE\n051918         GO TO Z-35-2-192-ELSE.\n051920     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-FEE-FREQ.\n051922     GO TO Z-35-2-ENDIF.\n051924 Z-35-2-192-ELSE.\n051926     IF HOLD-TDA-ACTVC-CODE = 0506\n051928         NEXT SENTENCE ELSE\n051930         GO TO Z-35-2-193-ELSE.\n051932     MOVE WS-CHG-WK-9-4 TO HOLD-TDAA-FEE-NTRVL.\n051934     GO TO Z-35-2-ENDIF.\n051936 Z-35-2-193-ELSE.\n051938     IF HOLD-TDA-ACTVC-CODE = 0507\n051940         NEXT SENTENCE ELSE\n051942         GO TO Z-35-2-194-ELSE.\n051944     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-BAL-BEG-MAT.\n051946     GO TO Z-35-2-ENDIF.\n051948 Z-35-2-194-ELSE.\n051950     IF HOLD-TDA-ACTVC-CODE = 0508\n051952         NEXT SENTENCE ELSE\n051954         GO TO Z-35-2-195-ELSE.\n051956     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-ANTIC-INT.\n051958     GO TO Z-35-2-ENDIF.\n051960 Z-35-2-195-ELSE.\n051962     IF HOLD-TDA-ACTVC-CODE = 0509\n051964         NEXT SENTENCE ELSE\n051966         GO TO Z-35-2-196-ELSE.\n051968     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-FAIR-MRKT.\n051970     GO TO Z-35-2-ENDIF.\n051972 Z-35-2-196-ELSE.\n051974     IF HOLD-TDA-ACTVC-CODE = 0510\n051976         NEXT SENTENCE ELSE\n051978         GO TO Z-35-2-197-ELSE.\n051980     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-LST-WHLD-AMT.\n051982     GO TO Z-35-2-ENDIF.\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    528 lines from 25460 to 25987.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 53, "total_chunks": 55, "start_line": 25460, "end_line": 25987, "line_count": 528}

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
- Source code length: 24827 characters

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
CHUNK 53 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 25460 to 25987 (528 lines)
Chunk Tokens (estimated): ~8,076
Actual Input Tokens: 9,482 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 25460-25987 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 53 of 55 chunks
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
      The source code below is only CHUNK 53 of 55.


=============================================================================
CHUNK 53 SOURCE CODE (Lines 25460-25987)
=============================================================================

```cobol
050928 Z-35-2-109-ELSE.
050930     IF HOLD-TDA-ACTVC-CODE = 0290
050932         NEXT SENTENCE ELSE
050934         GO TO Z-35-2-110-ELSE.
050936     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-ST-INT-CD.
050938     GO TO Z-35-2-ENDIF.
050940 Z-35-2-110-ELSE.
050942     IF HOLD-TDA-ACTVC-CODE = 0291
050944         NEXT SENTENCE ELSE
050946         GO TO Z-35-2-111-ELSE.
050948     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-ST-WHLD-CD.
050950     GO TO Z-35-2-ENDIF.
050952 Z-35-2-111-ELSE.
050954     IF HOLD-TDA-ACTVC-CODE = 0292
050956         NEXT SENTENCE ELSE
050958         GO TO Z-35-2-112-ELSE.
050960     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-ST-WHLD-AMT.
050962     GO TO Z-35-2-ENDIF.
050964 Z-35-2-112-ELSE.
050966     IF HOLD-TDA-ACTVC-CODE = 0293
050968         NEXT SENTENCE ELSE
050970         GO TO Z-35-2-113-ELSE.
050972     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-ST-CUR-W-AMT.
050974     GO TO Z-35-2-ENDIF.
050976 Z-35-2-113-ELSE.
050978     IF HOLD-TDA-ACTVC-CODE = 0294
050980         NEXT SENTENCE ELSE
050982         GO TO Z-35-2-114-ELSE.
050984     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-ST-LST-W-AMT.
050986     GO TO Z-35-2-ENDIF.
050988 Z-35-2-114-ELSE.
050990     IF HOLD-TDA-ACTVC-CODE = 0295
050992         NEXT SENTENCE ELSE
050994         GO TO Z-35-2-115-ELSE.
050996     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-ST-WHLD-STD.
050998     GO TO Z-35-2-ENDIF.
051000 Z-35-2-115-ELSE.
051002     IF HOLD-TDA-ACTVC-CODE = 0296
051004         NEXT SENTENCE ELSE
051006         GO TO Z-35-2-116-ELSE.
051008     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-ST-WHLD-YTD.
051010     GO TO Z-35-2-ENDIF.
051012 Z-35-2-116-ELSE.
051014     IF HOLD-TDA-ACTVC-CODE = 0301
051016         NEXT SENTENCE ELSE
051018         GO TO Z-35-2-117-ELSE.
051020     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-PENLTY-CD.
051022     GO TO Z-35-2-ENDIF.
051024 Z-35-2-117-ELSE.
051026     IF HOLD-TDA-ACTVC-CODE = 0372
051028         NEXT SENTENCE ELSE
051030         GO TO Z-35-2-118-ELSE.
051032     MOVE WS-CHG-WK-9-10 TO HOLD-TDAA-CS-ACCT.
051034     GO TO Z-35-2-ENDIF.
051036 Z-35-2-118-ELSE.
051038     IF HOLD-TDA-ACTVC-CODE = 0375
051040         NEXT SENTENCE ELSE
051042         GO TO Z-35-2-119-ELSE.
051044     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-NO-COMB-IRS.
051046     GO TO Z-35-2-ENDIF.
051048 Z-35-2-119-ELSE.
051050     IF HOLD-TDA-ACTVC-CODE = 0401
051052         NEXT SENTENCE ELSE
051054         GO TO Z-35-2-120-ELSE.
051056     MOVE WS-CHG-WK-X-1 TO HOLD-TDAI-UNINSURED.
051058     GO TO Z-35-2-ENDIF.
051060 Z-35-2-120-ELSE.
051062     IF HOLD-TDA-ACTVC-CODE = 0402
051064         NEXT SENTENCE ELSE
051066         GO TO Z-35-2-121-ELSE.
051068     MOVE WS-CHG-WK-9-5 TO HOLD-TDAI-DS-C-YTD-CNT.
051070     GO TO Z-35-2-ENDIF.
051072 Z-35-2-121-ELSE.
051074     IF HOLD-TDA-ACTVC-CODE = 0403
051076         NEXT SENTENCE ELSE
051078         GO TO Z-35-2-122-ELSE.
051080     MOVE WS-CHG-WK-9-5 TO HOLD-TDAI-DS-P-YTD-CNT.
051082     GO TO Z-35-2-ENDIF.
051084 Z-35-2-122-ELSE.
051086     IF HOLD-TDA-ACTVC-CODE = 0404
051088         NEXT SENTENCE ELSE
051090         GO TO Z-35-2-123-ELSE.
051092     MOVE WS-CHG-WK-9-5 TO HOLD-TDAI-CN-YTD-CNT.
051094     GO TO Z-35-2-ENDIF.
051096 Z-35-2-123-ELSE.
051098     IF HOLD-TDA-ACTVC-CODE = 0405
051100         NEXT SENTENCE ELSE
051102         GO TO Z-35-2-124-ELSE.
051104     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-CN-YTD-AMT.
051106     GO TO Z-35-2-ENDIF.
051108 Z-35-2-124-ELSE.
051110     IF HOLD-TDA-ACTVC-CODE = 0406
051112         NEXT SENTENCE ELSE
051114         GO TO Z-35-2-125-ELSE.
051116     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-CN-LYTD-AMT.
051118     GO TO Z-35-2-ENDIF.
051120 Z-35-2-125-ELSE.
051122     IF HOLD-TDA-ACTVC-CODE = 0407
051124         NEXT SENTENCE ELSE
051126         GO TO Z-35-2-126-ELSE.
051128     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-AMT-C-YTD.
051130     GO TO Z-35-2-ENDIF.
051132 Z-35-2-126-ELSE.
051134     IF HOLD-TDA-ACTVC-CODE = 0408
051136         NEXT SENTENCE ELSE
051138         GO TO Z-35-2-127-ELSE.
051140     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-AMT-P-YTD.
051142     GO TO Z-35-2-ENDIF.
051144 Z-35-2-127-ELSE.
051146     IF HOLD-TDA-ACTVC-CODE = 0409
051148         NEXT SENTENCE ELSE
051150         GO TO Z-35-2-128-ELSE.
051152     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-INT-AMT.
051154     GO TO Z-35-2-ENDIF.
051156 Z-35-2-128-ELSE.
051158     IF HOLD-TDA-ACTVC-CODE = 0411
051160         NEXT SENTENCE ELSE
051162         GO TO Z-35-2-129-ELSE.
051164     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (1).
051166     GO TO Z-35-2-ENDIF.
051168 Z-35-2-129-ELSE.
051170     IF HOLD-TDA-ACTVC-CODE = 0412
051172         NEXT SENTENCE ELSE
051174         GO TO Z-35-2-130-ELSE.
051176     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (2).
051178     GO TO Z-35-2-ENDIF.
051180 Z-35-2-130-ELSE.
051182     IF HOLD-TDA-ACTVC-CODE = 0413
051184         NEXT SENTENCE ELSE
051186         GO TO Z-35-2-131-ELSE.
051188     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (3).
051190     GO TO Z-35-2-ENDIF.
051192 Z-35-2-131-ELSE.
051194     IF HOLD-TDA-ACTVC-CODE = 0414
051196         NEXT SENTENCE ELSE
051198         GO TO Z-35-2-132-ELSE.
051200     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (4).
051202     GO TO Z-35-2-ENDIF.
051204 Z-35-2-132-ELSE.
051206     IF HOLD-TDA-ACTVC-CODE = 0415
051208         NEXT SENTENCE ELSE
051210         GO TO Z-35-2-133-ELSE.
051212     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (5).
051214     GO TO Z-35-2-ENDIF.
051216 Z-35-2-133-ELSE.
051218     IF HOLD-TDA-ACTVC-CODE = 0416
051220         NEXT SENTENCE ELSE
051222         GO TO Z-35-2-134-ELSE.
051224     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (6).
051226     GO TO Z-35-2-ENDIF.
051228 Z-35-2-134-ELSE.
051230     IF HOLD-TDA-ACTVC-CODE = 0417
051232         NEXT SENTENCE ELSE
051234         GO TO Z-35-2-135-ELSE.
051236     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (7).
051238     GO TO Z-35-2-ENDIF.
051240 Z-35-2-135-ELSE.
051242     IF HOLD-TDA-ACTVC-CODE = 0418
051244         NEXT SENTENCE ELSE
051246         GO TO Z-35-2-136-ELSE.
051248     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (8).
051250     GO TO Z-35-2-ENDIF.
051252 Z-35-2-136-ELSE.
051254     IF HOLD-TDA-ACTVC-CODE = 0419
051256         NEXT SENTENCE ELSE
051258         GO TO Z-35-2-137-ELSE.
051260     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (9).
051262     GO TO Z-35-2-ENDIF.
051264 Z-35-2-137-ELSE.
051266     IF HOLD-TDA-ACTVC-CODE = 0420
051268         NEXT SENTENCE ELSE
051270         GO TO Z-35-2-138-ELSE.
051272     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (10).
051274     GO TO Z-35-2-ENDIF.
051276 Z-35-2-138-ELSE.
051278     IF HOLD-TDA-ACTVC-CODE = 0421
051280         NEXT SENTENCE ELSE
051282         GO TO Z-35-2-139-ELSE.
051284     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (11).
051286     GO TO Z-35-2-ENDIF.
051288 Z-35-2-139-ELSE.
051290     IF HOLD-TDA-ACTVC-CODE = 0422
051292         NEXT SENTENCE ELSE
051294         GO TO Z-35-2-140-ELSE.
051296     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (12).
051298     GO TO Z-35-2-ENDIF.
051300 Z-35-2-140-ELSE.
051302     IF HOLD-TDA-ACTVC-CODE = 0423
051304         NEXT SENTENCE ELSE
051306         GO TO Z-35-2-141-ELSE.
051308     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (13).
051310     GO TO Z-35-2-ENDIF.
051312 Z-35-2-141-ELSE.
051314     IF HOLD-TDA-ACTVC-CODE = 0424
051316         NEXT SENTENCE ELSE
051318         GO TO Z-35-2-142-ELSE.
051320     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (14).
051322     GO TO Z-35-2-ENDIF.
051324 Z-35-2-142-ELSE.
051326     IF HOLD-TDA-ACTVC-CODE = 0425
051328         NEXT SENTENCE ELSE
051330         GO TO Z-35-2-143-ELSE.
051332     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (15).
051334     GO TO Z-35-2-ENDIF.
051336 Z-35-2-143-ELSE.
051338     IF HOLD-TDA-ACTVC-CODE = 0426
051340         NEXT SENTENCE ELSE
051342         GO TO Z-35-2-144-ELSE.
051344     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (16).
051346     GO TO Z-35-2-ENDIF.
051348 Z-35-2-144-ELSE.
051350     IF HOLD-TDA-ACTVC-CODE = 0427
051352         NEXT SENTENCE ELSE
051354         GO TO Z-35-2-145-ELSE.
051356     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (17).
051358     GO TO Z-35-2-ENDIF.
051360 Z-35-2-145-ELSE.
051362     IF HOLD-TDA-ACTVC-CODE = 0428
051364         NEXT SENTENCE ELSE
051366         GO TO Z-35-2-146-ELSE.
051368     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (18).
051370     GO TO Z-35-2-ENDIF.
051372 Z-35-2-146-ELSE.
051374     IF HOLD-TDA-ACTVC-CODE = 0429
051376         NEXT SENTENCE ELSE
051378         GO TO Z-35-2-147-ELSE.
051380     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (19).
051382     GO TO Z-35-2-ENDIF.
051384 Z-35-2-147-ELSE.
051386     IF HOLD-TDA-ACTVC-CODE = 0430
051388         NEXT SENTENCE ELSE
051390         GO TO Z-35-2-148-ELSE.
051392     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAI-DS-CN-AMT (20).
051394     GO TO Z-35-2-ENDIF.
051396 Z-35-2-148-ELSE.
051398     IF HOLD-TDA-ACTVC-CODE = 0441
051400         NEXT SENTENCE ELSE
051402         GO TO Z-35-2-149-ELSE.
051404     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (1).
051406     GO TO Z-35-2-ENDIF.
051408 Z-35-2-149-ELSE.
051410     IF HOLD-TDA-ACTVC-CODE = 0442
051412         NEXT SENTENCE ELSE
051414         GO TO Z-35-2-150-ELSE.
051416     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (2).
051418     GO TO Z-35-2-ENDIF.
051420 Z-35-2-150-ELSE.
051422     IF HOLD-TDA-ACTVC-CODE = 0443
051424         NEXT SENTENCE ELSE
051426         GO TO Z-35-2-151-ELSE.
051428     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (3).
051430     GO TO Z-35-2-ENDIF.
051432 Z-35-2-151-ELSE.
051434     IF HOLD-TDA-ACTVC-CODE = 0444
051436         NEXT SENTENCE ELSE
051438         GO TO Z-35-2-152-ELSE.
051440     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (4).
051442     GO TO Z-35-2-ENDIF.
051444 Z-35-2-152-ELSE.
051446     IF HOLD-TDA-ACTVC-CODE = 0445
051448         NEXT SENTENCE ELSE
051450         GO TO Z-35-2-153-ELSE.
051452     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (5).
051454     GO TO Z-35-2-ENDIF.
051456 Z-35-2-153-ELSE.
051458     IF HOLD-TDA-ACTVC-CODE = 0446
051460         NEXT SENTENCE ELSE
051462         GO TO Z-35-2-154-ELSE.
051464     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (6).
051466     GO TO Z-35-2-ENDIF.
051468 Z-35-2-154-ELSE.
051470     IF HOLD-TDA-ACTVC-CODE = 0447
051472         NEXT SENTENCE ELSE
051474         GO TO Z-35-2-155-ELSE.
051476     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (7).
051478     GO TO Z-35-2-ENDIF.
051480 Z-35-2-155-ELSE.
051482     IF HOLD-TDA-ACTVC-CODE = 0448
051484         NEXT SENTENCE ELSE
051486         GO TO Z-35-2-156-ELSE.
051488     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (8).
051490     GO TO Z-35-2-ENDIF.
051492 Z-35-2-156-ELSE.
051494     IF HOLD-TDA-ACTVC-CODE = 0449
051496         NEXT SENTENCE ELSE
051498         GO TO Z-35-2-157-ELSE.
051500     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (9).
051502     GO TO Z-35-2-ENDIF.
051504 Z-35-2-157-ELSE.
051506     IF HOLD-TDA-ACTVC-CODE = 0450
051508         NEXT SENTENCE ELSE
051510         GO TO Z-35-2-158-ELSE.
051512     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (10).
051514     GO TO Z-35-2-ENDIF.
051516 Z-35-2-158-ELSE.
051518     IF HOLD-TDA-ACTVC-CODE = 0451
051520         NEXT SENTENCE ELSE
051522         GO TO Z-35-2-159-ELSE.
051524     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (11).
051526     GO TO Z-35-2-ENDIF.
051528 Z-35-2-159-ELSE.
051530     IF HOLD-TDA-ACTVC-CODE = 0452
051532         NEXT SENTENCE ELSE
051534         GO TO Z-35-2-160-ELSE.
051536     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (12).
051538     GO TO Z-35-2-ENDIF.
051540 Z-35-2-160-ELSE.
051542     IF HOLD-TDA-ACTVC-CODE = 0453
051544         NEXT SENTENCE ELSE
051546         GO TO Z-35-2-161-ELSE.
051548     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (13).
051550     GO TO Z-35-2-ENDIF.
051552 Z-35-2-161-ELSE.
051554     IF HOLD-TDA-ACTVC-CODE = 0454
051556         NEXT SENTENCE ELSE
051558         GO TO Z-35-2-162-ELSE.
051560     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (14).
051562     GO TO Z-35-2-ENDIF.
051564 Z-35-2-162-ELSE.
051566     IF HOLD-TDA-ACTVC-CODE = 0455
051568         NEXT SENTENCE ELSE
051570         GO TO Z-35-2-163-ELSE.
051572     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (15).
051574     GO TO Z-35-2-ENDIF.
051576 Z-35-2-163-ELSE.
051578     IF HOLD-TDA-ACTVC-CODE = 0456
051580         NEXT SENTENCE ELSE
051582         GO TO Z-35-2-164-ELSE.
051584     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (16).
051586     GO TO Z-35-2-ENDIF.
051588 Z-35-2-164-ELSE.
051590     IF HOLD-TDA-ACTVC-CODE = 0457
051592         NEXT SENTENCE ELSE
051594         GO TO Z-35-2-165-ELSE.
051596     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (17).
051598     GO TO Z-35-2-ENDIF.
051600 Z-35-2-165-ELSE.
051602     IF HOLD-TDA-ACTVC-CODE = 0458
051604         NEXT SENTENCE ELSE
051606         GO TO Z-35-2-166-ELSE.
051608     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (18).
051610     GO TO Z-35-2-ENDIF.
051612 Z-35-2-166-ELSE.
051614     IF HOLD-TDA-ACTVC-CODE = 0459
051616         NEXT SENTENCE ELSE
051618         GO TO Z-35-2-167-ELSE.
051620     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (19).
051622     GO TO Z-35-2-ENDIF.
051624 Z-35-2-167-ELSE.
051626     IF HOLD-TDA-ACTVC-CODE = 0460
051628         NEXT SENTENCE ELSE
051630         GO TO Z-35-2-168-ELSE.
051632     MOVE WS-CHG-WK-X-2 TO HOLD-TDAI-DS-TYPE (20).
051634     GO TO Z-35-2-ENDIF.
051636 Z-35-2-168-ELSE.
051638     IF HOLD-TDA-ACTVC-CODE = 0471
051640         NEXT SENTENCE ELSE
051642         GO TO Z-35-2-169-ELSE.
051644     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (1).
051646     GO TO Z-35-2-ENDIF.
051648 Z-35-2-169-ELSE.
051650     IF HOLD-TDA-ACTVC-CODE = 0472
051652         NEXT SENTENCE ELSE
051654         GO TO Z-35-2-170-ELSE.
051656     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (2).
051658     GO TO Z-35-2-ENDIF.
051660 Z-35-2-170-ELSE.
051662     IF HOLD-TDA-ACTVC-CODE = 0473
051664         NEXT SENTENCE ELSE
051666         GO TO Z-35-2-171-ELSE.
051668     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (3).
051670     GO TO Z-35-2-ENDIF.
051672 Z-35-2-171-ELSE.
051674     IF HOLD-TDA-ACTVC-CODE = 0474
051676         NEXT SENTENCE ELSE
051678         GO TO Z-35-2-172-ELSE.
051680     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (4).
051682     GO TO Z-35-2-ENDIF.
051684 Z-35-2-172-ELSE.
051686     IF HOLD-TDA-ACTVC-CODE = 0475
051688         NEXT SENTENCE ELSE
051690         GO TO Z-35-2-173-ELSE.
051692     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (5).
051694     GO TO Z-35-2-ENDIF.
051696 Z-35-2-173-ELSE.
051698     IF HOLD-TDA-ACTVC-CODE = 0476
051700         NEXT SENTENCE ELSE
051702         GO TO Z-35-2-174-ELSE.
051704     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (6).
051706     GO TO Z-35-2-ENDIF.
051708 Z-35-2-174-ELSE.
051710     IF HOLD-TDA-ACTVC-CODE = 0477
051712         NEXT SENTENCE ELSE
051714         GO TO Z-35-2-175-ELSE.
051716     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (7).
051718     GO TO Z-35-2-ENDIF.
051720 Z-35-2-175-ELSE.
051722     IF HOLD-TDA-ACTVC-CODE = 0478
051724         NEXT SENTENCE ELSE
051726         GO TO Z-35-2-176-ELSE.
051728     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (8).
051730     GO TO Z-35-2-ENDIF.
051732 Z-35-2-176-ELSE.
051734     IF HOLD-TDA-ACTVC-CODE = 0479
051736         NEXT SENTENCE ELSE
051738         GO TO Z-35-2-177-ELSE.
051740     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (9).
051742     GO TO Z-35-2-ENDIF.
051744 Z-35-2-177-ELSE.
051746     IF HOLD-TDA-ACTVC-CODE = 0480
051748         NEXT SENTENCE ELSE
051750         GO TO Z-35-2-178-ELSE.
051752     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (10).
051754     GO TO Z-35-2-ENDIF.
051756 Z-35-2-178-ELSE.
051758     IF HOLD-TDA-ACTVC-CODE = 0481
051760         NEXT SENTENCE ELSE
051762         GO TO Z-35-2-179-ELSE.
051764     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (11).
051766     GO TO Z-35-2-ENDIF.
051768 Z-35-2-179-ELSE.
051770     IF HOLD-TDA-ACTVC-CODE = 0482
051772         NEXT SENTENCE ELSE
051774         GO TO Z-35-2-180-ELSE.
051776     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (12).
051778     GO TO Z-35-2-ENDIF.
051780 Z-35-2-180-ELSE.
051782     IF HOLD-TDA-ACTVC-CODE = 0483
051784         NEXT SENTENCE ELSE
051786         GO TO Z-35-2-181-ELSE.
051788     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (13).
051790     GO TO Z-35-2-ENDIF.
051792 Z-35-2-181-ELSE.
051794     IF HOLD-TDA-ACTVC-CODE = 0484
051796         NEXT SENTENCE ELSE
051798         GO TO Z-35-2-182-ELSE.
051800     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (14).
051802     GO TO Z-35-2-ENDIF.
051804 Z-35-2-182-ELSE.
051806     IF HOLD-TDA-ACTVC-CODE = 0485
051808         NEXT SENTENCE ELSE
051810         GO TO Z-35-2-183-ELSE.
051812     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (15).
051814     GO TO Z-35-2-ENDIF.
051816 Z-35-2-183-ELSE.
051818     IF HOLD-TDA-ACTVC-CODE = 0486
051820         NEXT SENTENCE ELSE
051822         GO TO Z-35-2-184-ELSE.
051824     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (16).
051826     GO TO Z-35-2-ENDIF.
051828 Z-35-2-184-ELSE.
051830     IF HOLD-TDA-ACTVC-CODE = 0487
051832         NEXT SENTENCE ELSE
051834         GO TO Z-35-2-185-ELSE.
051836     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (17).
051838     GO TO Z-35-2-ENDIF.
051840 Z-35-2-185-ELSE.
051842     IF HOLD-TDA-ACTVC-CODE = 0488
051844         NEXT SENTENCE ELSE
051846         GO TO Z-35-2-186-ELSE.
051848     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (18).
051850     GO TO Z-35-2-ENDIF.
051852 Z-35-2-186-ELSE.
051854     IF HOLD-TDA-ACTVC-CODE = 0489
051856         NEXT SENTENCE ELSE
051858         GO TO Z-35-2-187-ELSE.
051860     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (19).
051862     GO TO Z-35-2-ENDIF.
051864 Z-35-2-187-ELSE.
051866     IF HOLD-TDA-ACTVC-CODE = 0490
051868         NEXT SENTENCE ELSE
051870         GO TO Z-35-2-188-ELSE.
051872     MOVE WS-CHG-WK-9-2 TO HOLD-TDAI-CN-TYPE (20).
051874     GO TO Z-35-2-ENDIF.
051876 Z-35-2-188-ELSE.
051878     IF HOLD-TDA-ACTVC-CODE = 0501
051880         NEXT SENTENCE ELSE
051882         GO TO Z-35-2-189-ELSE.
051884     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-RR-CYC-NBR.
051886     GO TO Z-35-2-ENDIF.
051888 Z-35-2-189-ELSE.
051890     IF HOLD-TDA-ACTVC-CODE = 0502
051892         NEXT SENTENCE ELSE
051894         GO TO Z-35-2-190-ELSE.
051896     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-IGL-GRP.
051898     GO TO Z-35-2-ENDIF.
051900 Z-35-2-190-ELSE.
051902     IF HOLD-TDA-ACTVC-CODE = 0503
051904         NEXT SENTENCE ELSE
051906         GO TO Z-35-2-191-ELSE.
051908     MOVE WS-CHG-WK-9-2 TO HOLD-TDAA-ACCT-OPTION.
051910     GO TO Z-35-2-ENDIF.
051912 Z-35-2-191-ELSE.
051914     IF HOLD-TDA-ACTVC-CODE = 0505
051916         NEXT SENTENCE ELSE
051918         GO TO Z-35-2-192-ELSE.
051920     MOVE WS-CHG-WK-9-1 TO HOLD-TDAA-FEE-FREQ.
051922     GO TO Z-35-2-ENDIF.
051924 Z-35-2-192-ELSE.
051926     IF HOLD-TDA-ACTVC-CODE = 0506
051928         NEXT SENTENCE ELSE
051930         GO TO Z-35-2-193-ELSE.
051932     MOVE WS-CHG-WK-9-4 TO HOLD-TDAA-FEE-NTRVL.
051934     GO TO Z-35-2-ENDIF.
051936 Z-35-2-193-ELSE.
051938     IF HOLD-TDA-ACTVC-CODE = 0507
051940         NEXT SENTENCE ELSE
051942         GO TO Z-35-2-194-ELSE.
051944     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-BAL-BEG-MAT.
051946     GO TO Z-35-2-ENDIF.
051948 Z-35-2-194-ELSE.
051950     IF HOLD-TDA-ACTVC-CODE = 0508
051952         NEXT SENTENCE ELSE
051954         GO TO Z-35-2-195-ELSE.
051956     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-ANTIC-INT.
051958     GO TO Z-35-2-ENDIF.
051960 Z-35-2-195-ELSE.
051962     IF HOLD-TDA-ACTVC-CODE = 0509
051964         NEXT SENTENCE ELSE
051966         GO TO Z-35-2-196-ELSE.
051968     MOVE WS-CHG-WK-9-S9V2 TO HOLD-TDAA-FAIR-MRKT.
051970     GO TO Z-35-2-ENDIF.
051972 Z-35-2-196-ELSE.
051974     IF HOLD-TDA-ACTVC-CODE = 0510
051976         NEXT SENTENCE ELSE
051978         GO TO Z-35-2-197-ELSE.
051980     MOVE WS-CHG-WK-9-S8V2 TO HOLD-TDAA-LST-WHLD-AMT.
051982     GO TO Z-35-2-ENDIF.
```

⚠️  This is the source code you must document.
    528 lines from 25460 to 25987.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

