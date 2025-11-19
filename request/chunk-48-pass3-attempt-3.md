# LLM Request Debug File
Generated: 2025-11-17T22:33:50.677979

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 48/55
- **Model**: gpt-4.1
- **Chunk Number**: 48
- **Pass Number**: 3
- **Attempt Number**: 3 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~7,924 tokens
- **Total Input**: ~9,882 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 48/55" (ID: detailed-code-explanation)

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


**CHUNK 48 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-17T19:50:50.832678", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 48 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 22984 to 23416 (433 lines)\nChunk Tokens (estimated): ~8,066\nActual Input Tokens: 9,472 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 22984-23416 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 48 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 48 of 55.\n\n\n=============================================================================\nCHUNK 48 SOURCE CODE (Lines 22984-23416)\n=============================================================================\n\n```cobol\n045976         TDB-TDACUST.\n045978     MOVE HOLD-TDAC-N3-MODIFIED OF HOLD-TDACUST TO                \n045980         TDB-TDAC-N3-MODIFIED OF TDB-TDACUST.\n045982     MOVE HOLD-TDAC-N3-PRINT-CD OF HOLD-TDACUST TO                \n045984         TDB-TDAC-N3-PRINT-CD OF TDB-TDACUST.\n045986     MOVE HOLD-TDAC-N3-KEY OF HOLD-TDACUST TO TDB-TDAC-N3-KEY OF  \n045988         TDB-TDACUST.\n045990     MOVE HOLD-TDAC-N3-FIRST OF HOLD-TDACUST TO TDB-TDAC-N3-FIRST \n045992         OF TDB-TDACUST.\n045994     MOVE HOLD-TDAC-N3-MID OF HOLD-TDACUST TO TDB-TDAC-N3-MID OF  \n045996         TDB-TDACUST.\n045998     MOVE HOLD-TDAC-N3-LAST OF HOLD-TDACUST TO TDB-TDAC-N3-LAST   \n046000         OF TDB-TDACUST.\n046002     MOVE HOLD-TDAC-N3-PREFIX OF HOLD-TDACUST TO                  \n046004         TDB-TDAC-N3-PREFIX OF TDB-TDACUST.\n046006     MOVE HOLD-TDAC-N3-SUFFIX OF HOLD-TDACUST TO                  \n046008         TDB-TDAC-N3-SUFFIX OF TDB-TDACUST.\n046010     MOVE HOLD-TDAC-N3-FAMILIAR OF HOLD-TDACUST TO                \n046012         TDB-TDAC-N3-FAMILIAR OF TDB-TDACUST.\n046014     MOVE HOLD-TDAC-N3-PRT-PFX OF HOLD-TDACUST TO                 \n046016         TDB-TDAC-N3-PRT-PFX OF TDB-TDACUST.\n046018     MOVE HOLD-TDAC-N3-PRT-SFX OF HOLD-TDACUST TO                 \n046020         TDB-TDAC-N3-PRT-SFX OF TDB-TDACUST.\n046022     MOVE HOLD-TDAC-N3-DESIGNAT OF HOLD-TDACUST TO                \n046024         TDB-TDAC-N3-DESIGNAT OF TDB-TDACUST.\n046026     MOVE HOLD-TDAC-ADDR-KEY OF HOLD-TDACUST TO TDB-TDAC-ADDR-KEY \n046028         OF TDB-TDACUST.\n046030     MOVE HOLD-TDAC-ADDR-1 OF HOLD-TDACUST TO TDB-TDAC-ADDR-1 OF  \n046032         TDB-TDACUST.\n046034     MOVE HOLD-TDAC-ADDR-2 OF HOLD-TDACUST TO TDB-TDAC-ADDR-2 OF  \n046036         TDB-TDACUST.\n046038     MOVE HOLD-TDAC-CITY OF HOLD-TDACUST TO TDB-TDAC-CITY OF      \n046040         TDB-TDACUST.\n046042     MOVE HOLD-TDAC-STATE OF HOLD-TDACUST TO TDB-TDAC-STATE OF    \n046044         TDB-TDACUST.\n046046     MOVE HOLD-TDAC-PROVINCE OF HOLD-TDACUST TO TDB-TDAC-PROVINCE \n046048         OF TDB-TDACUST.\n046050     MOVE HOLD-TDAC-COUNTRY OF HOLD-TDACUST TO TDB-TDAC-COUNTRY   \n046052         OF TDB-TDACUST.\n046054     MOVE HOLD-TDAC-ZIP OF HOLD-TDACUST TO TDB-TDAC-ZIP OF        \n046056         TDB-TDACUST.\n046058     MOVE HOLD-TDAC-ZIP-4 OF HOLD-TDACUST TO TDB-TDAC-ZIP-4 OF    \n046060         TDB-TDACUST.\n046062     MOVE HOLD-TDAC-LONGITUDE OF HOLD-TDACUST TO                  \n046064         TDB-TDAC-LONGITUDE OF TDB-TDACUST.\n046066     MOVE HOLD-TDAC-LATITUDE OF HOLD-TDACUST TO TDB-TDAC-LATITUDE \n046068         OF TDB-TDACUST.\n046070     MOVE HOLD-TDAC-MAIL-CD OF HOLD-TDACUST TO TDB-TDAC-MAIL-CD   \n046072         OF TDB-TDACUST.\n046074     MOVE HOLD-TDAC-TICKLER-FLAG OF HOLD-TDACUST TO               \n046076         TDB-TDAC-TICKLER-FLAG OF TDB-TDACUST.\n046078     MOVE HOLD-TDAC-RESIDENT-CD OF HOLD-TDACUST TO                \n046080         TDB-TDAC-RESIDENT-CD OF TDB-TDACUST.\n046082     MOVE HOLD-TDAC-ALIEN-CD OF HOLD-TDACUST TO TDB-TDAC-ALIEN-CD \n046084         OF TDB-TDACUST.\n046086     MOVE HOLD-TDAC-SHT-NAME OF HOLD-TDACUST TO TDB-TDAC-SHT-NAME \n046088         OF TDB-TDACUST.\n046090     MOVE HOLD-TDAC-BAR-CD OF HOLD-TDACUST TO TDB-TDAC-BAR-CD OF  \n046092         TDB-TDACUST.\n046094     MOVE HOLD-TDAC-PHONE-1 OF HOLD-TDACUST TO TDB-TDAC-PHONE-1   \n046096         OF TDB-TDACUST.\n046098     MOVE HOLD-TDAC-PHONE-2 OF HOLD-TDACUST TO TDB-TDAC-PHONE-2   \n046100         OF TDB-TDACUST.\n046102     MOVE HOLD-TDAC-TIN-CD OF HOLD-TDACUST TO TDB-TDAC-TIN-CD OF  \n046104         TDB-TDACUST.\n046106     MOVE HOLD-TDAC-TIN-CERT-CD OF HOLD-TDACUST TO                \n046108         TDB-TDAC-TIN-CERT-CD OF TDB-TDACUST.\n046110     MOVE HOLD-TDAC-TIN-CERT-DT OF HOLD-TDACUST TO                \n046112         TDB-TDAC-TIN-CERT-DT OF TDB-TDACUST.\n046114     MOVE HOLD-TDAC-TIN-NBR OF HOLD-TDACUST TO TDB-TDAC-TIN-NBR   \n046116         OF TDB-TDACUST.\n046118     MOVE HOLD-TDAC-OFFICER OF HOLD-TDACUST TO TDB-TDAC-OFFICER   \n046120         OF TDB-TDACUST.\n046122     MOVE HOLD-TDAC-EMP-CD OF HOLD-TDACUST TO TDB-TDAC-EMP-CD OF  \n046124         TDB-TDACUST.\n046126     MOVE HOLD-TDAC-FREE-MARK OF HOLD-TDACUST TO                  \n046128         TDB-TDAC-FREE-MARK OF TDB-TDACUST.\n046130     MOVE HOLD-TDAC-INQ-SECR-CD OF HOLD-TDACUST TO                \n046132         TDB-TDAC-INQ-SECR-CD OF TDB-TDACUST.\n046134     MOVE HOLD-TDAC-PRIVACY OF HOLD-TDACUST TO TDB-TDAC-PRIVACY   \n046136         OF TDB-TDACUST.\n046138     MOVE HOLD-TDAC-BK-DEF-CD1 OF HOLD-TDACUST TO                 \n046140         TDB-TDAC-BK-DEF-CD1 OF TDB-TDACUST.\n046142     MOVE HOLD-TDAC-BK-DEF-CD2 OF HOLD-TDACUST TO                 \n046144         TDB-TDAC-BK-DEF-CD2 OF TDB-TDACUST.\n046146     MOVE HOLD-TDAC-BK-DEF-CD3 OF HOLD-TDACUST TO                 \n046148         TDB-TDAC-BK-DEF-CD3 OF TDB-TDACUST.\n046150     MOVE HOLD-TDAC-BK-DEF-CD4 OF HOLD-TDACUST TO                 \n046152         TDB-TDAC-BK-DEF-CD4 OF TDB-TDACUST.\n046154     MOVE HOLD-TDAC-BK-DEF-CD5 OF HOLD-TDACUST TO                 \n046156         TDB-TDAC-BK-DEF-CD5 OF TDB-TDACUST.\n046158     MOVE HOLD-TDAC-EMPLOYEE-ID OF HOLD-TDACUST TO                \n046160         TDB-TDAC-EMPLOYEE-ID OF TDB-TDACUST.\n046162     MOVE HOLD-TDAC-EMAIL-ADDR OF HOLD-TDACUST TO                 \n046164         TDB-TDAC-EMAIL-ADDR OF TDB-TDACUST.\n046166     MOVE HOLD-TDAC-EMAIL-ADDR-1-30 OF HOLD-TDACUST TO            \n046168         TDB-TDAC-EMAIL-ADDR-1-30 OF TDB-TDACUST.\n046170     MOVE HOLD-TDAC-EMAIL-ADDR-31-60 OF HOLD-TDACUST TO           \n046172         TDB-TDAC-EMAIL-ADDR-31-60 OF TDB-TDACUST.\n046174     MOVE HOLD-TDAC-EMAIL-ADDR-61-90 OF HOLD-TDACUST TO           \n046176         TDB-TDAC-EMAIL-ADDR-61-90 OF TDB-TDACUST.\n046178     MOVE HOLD-TDAC-EMAIL-ADDR-91-100 OF HOLD-TDACUST TO          \n046180         TDB-TDAC-EMAIL-ADDR-91-100 OF TDB-TDACUST.\n046182     MOVE HOLD-TDAC-EMAIL-ADDR-1-50 OF HOLD-TDACUST TO            \n046184         TDB-TDAC-EMAIL-ADDR-1-50 OF TDB-TDACUST.\n046186     MOVE HOLD-TDAC-EMAIL-ADDR-51-100 OF HOLD-TDACUST TO          \n046188         TDB-TDAC-EMAIL-ADDR-51-100 OF TDB-TDACUST.\n046190     MOVE HOLD-TDAC-EMAIL-PSSWRD OF HOLD-TDACUST TO               \n046192         TDB-TDAC-EMAIL-PSSWRD OF TDB-TDACUST.\n046194     MOVE HOLD-TDAC-GENDER OF HOLD-TDACUST TO TDB-TDAC-GENDER OF  \n046196         TDB-TDACUST.\n046198     MOVE HOLD-TDAC-NEW-CUST OF HOLD-TDACUST TO TDB-TDAC-NEW-CUST \n046200         OF TDB-TDACUST.\n046202     MOVE HOLD-TDAC-OPEN-DT OF HOLD-TDACUST TO TDB-TDAC-OPEN-DT   \n046204         OF TDB-TDACUST.\n046206     MOVE HOLD-TDAC-LUPD-DATE OF HOLD-TDACUST TO                  \n046208         TDB-TDAC-LUPD-DATE OF TDB-TDACUST.\n046210     MOVE HOLD-TDAC-LUPD-TIME OF HOLD-TDACUST TO                  \n046212         TDB-TDAC-LUPD-TIME OF TDB-TDACUST.\n046214     MOVE HOLD-TDAC-LST-CONTACT OF HOLD-TDACUST TO                \n046216         TDB-TDAC-LST-CONTACT OF TDB-TDACUST.\n046218     MOVE HOLD-TDAC-BIRTH-DT OF HOLD-TDACUST TO TDB-TDAC-BIRTH-DT \n046220         OF TDB-TDACUST.\n046222     MOVE HOLD-TDAC-BIRTH-DT-2 OF HOLD-TDACUST TO                 \n046224         TDB-TDAC-BIRTH-DT-2 OF TDB-TDACUST.\n046226     MOVE HOLD-TDAC-BIRTH-DT-3 OF HOLD-TDACUST TO                 \n046228         TDB-TDAC-BIRTH-DT-3 OF TDB-TDACUST.\n046230     MOVE HOLD-TDAC-DEATH-DT OF HOLD-TDACUST TO TDB-TDAC-DEATH-DT \n046232         OF TDB-TDACUST.\n046234     MOVE HOLD-TDAC-ADD-DT OF HOLD-TDACUST TO TDB-TDAC-ADD-DT OF  \n046236         TDB-TDACUST.\n046238     MOVE HOLD-TDAC-ADD-TM OF HOLD-TDACUST TO TDB-TDAC-ADD-TM OF  \n046240         TDB-TDACUST.\n046242     MOVE HOLD-TDAC-ROTH-DATE OF HOLD-TDACUST TO                  \n046244         TDB-TDAC-ROTH-DATE OF TDB-TDACUST.\n046246     MOVE HOLD-TDAC-CD-BAL OF HOLD-TDACUST TO TDB-TDAC-CD-BAL OF  \n046248         TDB-TDACUST.\n046250     MOVE HOLD-TDAC-CD-BAL-BYR OF HOLD-TDACUST TO                 \n046252         TDB-TDAC-CD-BAL-BYR OF TDB-TDACUST.\n046254     MOVE HOLD-TDAC-CD-PENLTY OF HOLD-TDACUST TO                  \n046256         TDB-TDAC-CD-PENLTY OF TDB-TDACUST.\n046258     MOVE HOLD-TDAC-CD-WTHLD OF HOLD-TDACUST TO TDB-TDAC-CD-WTHLD \n046260         OF TDB-TDACUST.\n046262     MOVE HOLD-TDAC-CD-INT OF HOLD-TDACUST TO TDB-TDAC-CD-INT OF  \n046264         TDB-TDACUST.\n046266     MOVE HOLD-TDAC-CD-OID-INT OF HOLD-TDACUST TO                 \n046268         TDB-TDAC-CD-OID-INT OF TDB-TDACUST.\n046270     MOVE HOLD-TDAC-IRA-BAL OF HOLD-TDACUST TO TDB-TDAC-IRA-BAL   \n046272         OF TDB-TDACUST.\n046274     MOVE HOLD-TDAC-IRA-BAL-BYR OF HOLD-TDACUST TO                \n046276         TDB-TDAC-IRA-BAL-BYR OF TDB-TDACUST.\n046278     MOVE HOLD-TDAC-IRA-PENLTY OF HOLD-TDACUST TO                 \n046280         TDB-TDAC-IRA-PENLTY OF TDB-TDACUST.\n046282     MOVE HOLD-TDAC-IRA-WTHLD OF HOLD-TDACUST TO                  \n046284         TDB-TDAC-IRA-WTHLD OF TDB-TDACUST.\n046286     MOVE HOLD-TDAC-IRA-INT OF HOLD-TDACUST TO TDB-TDAC-IRA-INT   \n046288         OF TDB-TDACUST.\n046290     MOVE HOLD-TDAC-IRA-CONTR OF HOLD-TDACUST TO                  \n046292         TDB-TDAC-IRA-CONTR OF TDB-TDACUST.\n046294     MOVE HOLD-TDAC-IRA-CONTR-LY OF HOLD-TDACUST TO               \n046296         TDB-TDAC-IRA-CONTR-LY OF TDB-TDACUST.\n046298     MOVE HOLD-TDAC-IRA-DISTR OF HOLD-TDACUST TO                  \n046300         TDB-TDAC-IRA-DISTR OF TDB-TDACUST.\n046302     MOVE HOLD-TDAC-IRA-DISTR-LY OF HOLD-TDACUST TO               \n046304         TDB-TDAC-IRA-DISTR-LY OF TDB-TDACUST.\n046306     MOVE HOLD-TDAC-IRA-ROLLOVER OF HOLD-TDACUST TO               \n046308         TDB-TDAC-IRA-ROLLOVER OF TDB-TDACUST.\n046310     MOVE HOLD-TDAC-IRA-TRF-IN OF HOLD-TDACUST TO                 \n046312         TDB-TDAC-IRA-TRF-IN OF TDB-TDACUST.\n046314     MOVE HOLD-TDAC-IRA-TRF-OUT OF HOLD-TDACUST TO                \n046316         TDB-TDAC-IRA-TRF-OUT OF TDB-TDACUST.\n046318     MOVE HOLD-TDAC-IRA-FAIR-MKT OF HOLD-TDACUST TO               \n046320         TDB-TDAC-IRA-FAIR-MKT OF TDB-TDACUST.\n046322     MOVE HOLD-TDAC-CIF-REMARK OF HOLD-TDACUST TO                 \n046324         TDB-TDAC-CIF-REMARK OF TDB-TDACUST.\n046326     MOVE HOLD-TDAC-CD-ST-WHLD OF HOLD-TDACUST TO                 \n046328         TDB-TDAC-CD-ST-WHLD OF TDB-TDACUST.\n046330     MOVE HOLD-TDAC-IRA-ST-WHLD OF HOLD-TDACUST TO                \n046332         TDB-TDAC-IRA-ST-WHLD OF TDB-TDACUST.\n046334     MOVE 1 TO Z-II.\n046336 Z-14-7-1-LOOP.\n046338     IF Z-II > 12\n046340         GO TO Z-14-7-1-LOOP-XIT.\n046342     MOVE HOLD-TDAC-CURR-YR-AMT OF HOLD-TDACUST (Z-II) TO         \n046344         TDB-TDAC-CURR-YR-AMT OF TDB-TDACUST (Z-II).\n046346     MOVE HOLD-TDAC-LAST-YR-AMT OF HOLD-TDACUST (Z-II) TO         \n046348         TDB-TDAC-LAST-YR-AMT OF TDB-TDACUST (Z-II).\n046350     ADD 1 TO Z-II.\n046352     GO TO Z-14-7-1-LOOP.\n046354 Z-14-7-1-LOOP-XIT.\n046356     MOVE HOLD-TDAC-TIN-CD-2 OF HOLD-TDACUST TO TDB-TDAC-TIN-CD-2 \n046358         OF TDB-TDACUST.\n046360     MOVE HOLD-TDAC-TIN-CRT-CD-2 OF HOLD-TDACUST TO               \n046362         TDB-TDAC-TIN-CRT-CD-2 OF TDB-TDACUST.\n046364     MOVE HOLD-TDAC-TIN-CRT-DT-2 OF HOLD-TDACUST TO               \n046366         TDB-TDAC-TIN-CRT-DT-2 OF TDB-TDACUST.\n046368     MOVE HOLD-TDAC-TIN-NBR-2 OF HOLD-TDACUST TO                  \n046370         TDB-TDAC-TIN-NBR-2 OF TDB-TDACUST.\n046372     MOVE HOLD-TDAC-TIN-CD-3 OF HOLD-TDACUST TO TDB-TDAC-TIN-CD-3 \n046374         OF TDB-TDACUST.\n046376     MOVE HOLD-TDAC-TIN-CRT-CD-3 OF HOLD-TDACUST TO               \n046378         TDB-TDAC-TIN-CRT-CD-3 OF TDB-TDACUST.\n046380     MOVE HOLD-TDAC-TIN-CRT-DT-3 OF HOLD-TDACUST TO               \n046382         TDB-TDAC-TIN-CRT-DT-3 OF TDB-TDACUST.\n046384     MOVE HOLD-TDAC-TIN-NBR-3 OF HOLD-TDACUST TO                  \n046386         TDB-TDAC-TIN-NBR-3 OF TDB-TDACUST.\n046388     MOVE HOLD-TDAC-NAICS-CD OF HOLD-TDACUST TO TDB-TDAC-NAICS-CD \n046390         OF TDB-TDACUST.\n046392     MOVE HOLD-TDAC-CIF-PASS-THR OF HOLD-TDACUST TO               \n046394         TDB-TDAC-CIF-PASS-THR OF TDB-TDACUST.\n046396     MOVE HOLD-TDAC-EMAIL-NTC OF HOLD-TDACUST TO                  \n046398         TDB-TDAC-EMAIL-NTC OF TDB-TDACUST.\n046400     MOVE HOLD-TDAC-RMD-YR-AMT OF HOLD-TDACUST TO                 \n046402         TDB-TDAC-RMD-YR-AMT OF TDB-TDACUST.\n046404     MOVE HOLD-TDAC-ADDR-CHG-DT OF HOLD-TDACUST TO                \n046406         TDB-TDAC-ADDR-CHG-DT OF TDB-TDACUST.\n046408     MOVE HOLD-TDAC-WTHLD-CD OF HOLD-TDACUST TO TDB-TDAC-WTHLD-CD \n046410         OF TDB-TDACUST.\n046412     MOVE HOLD-TDAC-ST-WHLD-CD OF HOLD-TDACUST TO                 \n046414         TDB-TDAC-ST-WHLD-CD OF TDB-TDACUST.\n046416     MOVE HOLD-TDAC-WTHLD-AMT OF HOLD-TDACUST TO                  \n046418         TDB-TDAC-WTHLD-AMT OF TDB-TDACUST.\n046420     MOVE HOLD-TDAC-ST-WHLD-AMT OF HOLD-TDACUST TO                \n046422         TDB-TDAC-ST-WHLD-AMT OF TDB-TDACUST.\n046424     MOVE HOLD-TDAC-FOREIGN-LANG OF HOLD-TDACUST TO               \n046426         TDB-TDAC-FOREIGN-LANG OF TDB-TDACUST.\n046428     MOVE HOLD-TDAC-L-ROLLOVR-DT OF HOLD-TDACUST TO               \n046430         TDB-TDAC-L-ROLLOVR-DT OF TDB-TDACUST.\n046432     MOVE HOLD-TDAC-CUSTM-FIELDS OF HOLD-TDACUST TO               \n046434         TDB-TDAC-CUSTM-FIELDS OF TDB-TDACUST.\n046436     MOVE HOLD-TDAC-LLC-NAME OF HOLD-TDACUST TO TDB-TDAC-LLC-NAME \n046438         OF TDB-TDACUST.\n046440     MOVE HOLD-TDAC-LLC-TIN-CD OF HOLD-TDACUST TO                 \n046442         TDB-TDAC-LLC-TIN-CD OF TDB-TDACUST.\n046444     MOVE HOLD-TDAC-LLC-TIN OF HOLD-TDACUST TO TDB-TDAC-LLC-TIN   \n046446         OF TDB-TDACUST.\n046448     MOVE HOLD-TDAC-FOREIGN-PHN OF HOLD-TDACUST TO                \n046450         TDB-TDAC-FOREIGN-PHN OF TDB-TDACUST.\n046452     MOVE 0350 TO TDB-MESSAGE-NBR.\n046454     GO TO Z-14-4-ENDIF.\n046456 Z-14-4-2-ELSE.\n046458     MOVE TDAC-BANK OF TDACUST TO TDB-TDAC-BANK OF TDB-TDACUST.\n046460     MOVE TDAC-CUST OF TDACUST TO TDB-TDAC-CUST OF TDB-TDACUST.\n046462     MOVE TDAC-BRCH OF TDACUST TO TDB-TDAC-BRCH OF TDB-TDACUST.\n046464     MOVE TDAC-STATUS OF TDACUST TO TDB-TDAC-STATUS OF            \n046466         TDB-TDACUST.\n046468     MOVE TDAC-NAME-1 OF TDACUST TO TDB-TDAC-NAME-1 OF            \n046470         TDB-TDACUST.\n046472     MOVE TDAC-N1-KEY OF TDACUST TO TDB-TDAC-N1-KEY OF            \n046474         TDB-TDACUST.\n046476     MOVE TDAC-N1-FIRST OF TDACUST TO TDB-TDAC-N1-FIRST OF        \n046478         TDB-TDACUST.\n046480     MOVE TDAC-N1-MID OF TDACUST TO TDB-TDAC-N1-MID OF            \n046482         TDB-TDACUST.\n046484     MOVE TDAC-N1-LAST OF TDACUST TO TDB-TDAC-N1-LAST OF          \n046486         TDB-TDACUST.\n046488     MOVE TDAC-N1-PREFIX OF TDACUST TO TDB-TDAC-N1-PREFIX OF      \n046490         TDB-TDACUST.\n046492     MOVE TDAC-N1-SUFFIX OF TDACUST TO TDB-TDAC-N1-SUFFIX OF      \n046494         TDB-TDACUST.\n046496     MOVE TDAC-N1-FAMILIAR OF TDACUST TO TDB-TDAC-N1-FAMILIAR OF  \n046498         TDB-TDACUST.\n046500     MOVE TDAC-N1-PRT-PFX OF TDACUST TO TDB-TDAC-N1-PRT-PFX OF    \n046502         TDB-TDACUST.\n046504     MOVE TDAC-N1-PRT-SFX OF TDACUST TO TDB-TDAC-N1-PRT-SFX OF    \n046506         TDB-TDACUST.\n046508     MOVE TDAC-N1-DESIGNAT OF TDACUST TO TDB-TDAC-N1-DESIGNAT OF  \n046510         TDB-TDACUST.\n046512     MOVE TDAC-NAME-2 OF TDACUST TO TDB-TDAC-NAME-2 OF            \n046514         TDB-TDACUST.\n046516     MOVE TDAC-N2-MODIFIED OF TDACUST TO TDB-TDAC-N2-MODIFIED OF  \n046518         TDB-TDACUST.\n046520     MOVE TDAC-N2-PRINT-CD OF TDACUST TO TDB-TDAC-N2-PRINT-CD OF  \n046522         TDB-TDACUST.\n046524     MOVE TDAC-N2-KEY OF TDACUST TO TDB-TDAC-N2-KEY OF            \n046526         TDB-TDACUST.\n046528     MOVE TDAC-N2-FIRST OF TDACUST TO TDB-TDAC-N2-FIRST OF        \n046530         TDB-TDACUST.\n046532     MOVE TDAC-N2-MID OF TDACUST TO TDB-TDAC-N2-MID OF            \n046534         TDB-TDACUST.\n046536     MOVE TDAC-N2-LAST OF TDACUST TO TDB-TDAC-N2-LAST OF          \n046538         TDB-TDACUST.\n046540     MOVE TDAC-N2-PREFIX OF TDACUST TO TDB-TDAC-N2-PREFIX OF      \n046542         TDB-TDACUST.\n046544     MOVE TDAC-N2-SUFFIX OF TDACUST TO TDB-TDAC-N2-SUFFIX OF      \n046546         TDB-TDACUST.\n046548     MOVE TDAC-N2-FAMILIAR OF TDACUST TO TDB-TDAC-N2-FAMILIAR OF  \n046550         TDB-TDACUST.\n046552     MOVE TDAC-N2-PRT-PFX OF TDACUST TO TDB-TDAC-N2-PRT-PFX OF    \n046554         TDB-TDACUST.\n046556     MOVE TDAC-N2-PRT-SFX OF TDACUST TO TDB-TDAC-N2-PRT-SFX OF    \n046558         TDB-TDACUST.\n046560     MOVE TDAC-N2-DESIGNAT OF TDACUST TO TDB-TDAC-N2-DESIGNAT OF  \n046562         TDB-TDACUST.\n046564     MOVE TDAC-NAME-3 OF TDACUST TO TDB-TDAC-NAME-3 OF            \n046566         TDB-TDACUST.\n046568     MOVE TDAC-N3-MODIFIED OF TDACUST TO TDB-TDAC-N3-MODIFIED OF  \n046570         TDB-TDACUST.\n046572     MOVE TDAC-N3-PRINT-CD OF TDACUST TO TDB-TDAC-N3-PRINT-CD OF  \n046574         TDB-TDACUST.\n046576     MOVE TDAC-N3-KEY OF TDACUST TO TDB-TDAC-N3-KEY OF            \n046578         TDB-TDACUST.\n046580     MOVE TDAC-N3-FIRST OF TDACUST TO TDB-TDAC-N3-FIRST OF        \n046582         TDB-TDACUST.\n046584     MOVE TDAC-N3-MID OF TDACUST TO TDB-TDAC-N3-MID OF            \n046586         TDB-TDACUST.\n046588     MOVE TDAC-N3-LAST OF TDACUST TO TDB-TDAC-N3-LAST OF          \n046590         TDB-TDACUST.\n046592     MOVE TDAC-N3-PREFIX OF TDACUST TO TDB-TDAC-N3-PREFIX OF      \n046594         TDB-TDACUST.\n046596     MOVE TDAC-N3-SUFFIX OF TDACUST TO TDB-TDAC-N3-SUFFIX OF      \n046598         TDB-TDACUST.\n046600     MOVE TDAC-N3-FAMILIAR OF TDACUST TO TDB-TDAC-N3-FAMILIAR OF  \n046602         TDB-TDACUST.\n046604     MOVE TDAC-N3-PRT-PFX OF TDACUST TO TDB-TDAC-N3-PRT-PFX OF    \n046606         TDB-TDACUST.\n046608     MOVE TDAC-N3-PRT-SFX OF TDACUST TO TDB-TDAC-N3-PRT-SFX OF    \n046610         TDB-TDACUST.\n046612     MOVE TDAC-N3-DESIGNAT OF TDACUST TO TDB-TDAC-N3-DESIGNAT OF  \n046614         TDB-TDACUST.\n046616     MOVE TDAC-ADDR-KEY OF TDACUST TO TDB-TDAC-ADDR-KEY OF        \n046618         TDB-TDACUST.\n046620     MOVE TDAC-ADDR-1 OF TDACUST TO TDB-TDAC-ADDR-1 OF            \n046622         TDB-TDACUST.\n046624     MOVE TDAC-ADDR-2 OF TDACUST TO TDB-TDAC-ADDR-2 OF            \n046626         TDB-TDACUST.\n046628     MOVE TDAC-CITY OF TDACUST TO TDB-TDAC-CITY OF TDB-TDACUST.\n046630     MOVE TDAC-STATE OF TDACUST TO TDB-TDAC-STATE OF TDB-TDACUST.\n046632     MOVE TDAC-PROVINCE OF TDACUST TO TDB-TDAC-PROVINCE OF        \n046634         TDB-TDACUST.\n046636     MOVE TDAC-COUNTRY OF TDACUST TO TDB-TDAC-COUNTRY OF          \n046638         TDB-TDACUST.\n046640     MOVE TDAC-ZIP OF TDACUST TO TDB-TDAC-ZIP OF TDB-TDACUST.\n046642     MOVE TDAC-ZIP-4 OF TDACUST TO TDB-TDAC-ZIP-4 OF TDB-TDACUST.\n046644     MOVE TDAC-LONGITUDE OF TDACUST TO TDB-TDAC-LONGITUDE OF      \n046646         TDB-TDACUST.\n046648     MOVE TDAC-LATITUDE OF TDACUST TO TDB-TDAC-LATITUDE OF        \n046650         TDB-TDACUST.\n046652     MOVE TDAC-MAIL-CD OF TDACUST TO TDB-TDAC-MAIL-CD OF          \n046654         TDB-TDACUST.\n046656     MOVE TDAC-TICKLER-FLAG OF TDACUST TO TDB-TDAC-TICKLER-FLAG   \n046658         OF TDB-TDACUST.\n046660     MOVE TDAC-RESIDENT-CD OF TDACUST TO TDB-TDAC-RESIDENT-CD OF  \n046662         TDB-TDACUST.\n046664     MOVE TDAC-ALIEN-CD OF TDACUST TO TDB-TDAC-ALIEN-CD OF        \n046666         TDB-TDACUST.\n046668     MOVE TDAC-SHT-NAME OF TDACUST TO TDB-TDAC-SHT-NAME OF        \n046670         TDB-TDACUST.\n046672     MOVE TDAC-BAR-CD OF TDACUST TO TDB-TDAC-BAR-CD OF            \n046674         TDB-TDACUST.\n046676     MOVE TDAC-PHONE-1 OF TDACUST TO TDB-TDAC-PHONE-1 OF          \n046678         TDB-TDACUST.\n046680     MOVE TDAC-PHONE-2 OF TDACUST TO TDB-TDAC-PHONE-2 OF          \n046682         TDB-TDACUST.\n046684     MOVE TDAC-TIN-CD OF TDACUST TO TDB-TDAC-TIN-CD OF            \n046686         TDB-TDACUST.\n046688     MOVE TDAC-TIN-CERT-CD OF TDACUST TO TDB-TDAC-TIN-CERT-CD OF  \n046690         TDB-TDACUST.\n046692     MOVE TDAC-TIN-CERT-DT OF TDACUST TO TDB-TDAC-TIN-CERT-DT OF  \n046694         TDB-TDACUST.\n046696     MOVE TDAC-TIN-NBR OF TDACUST TO TDB-TDAC-TIN-NBR OF          \n046698         TDB-TDACUST.\n046700     MOVE TDAC-OFFICER OF TDACUST TO TDB-TDAC-OFFICER OF          \n046702         TDB-TDACUST.\n046704     MOVE TDAC-EMP-CD OF TDACUST TO TDB-TDAC-EMP-CD OF            \n046706         TDB-TDACUST.\n046708     MOVE TDAC-FREE-MARK OF TDACUST TO TDB-TDAC-FREE-MARK OF      \n046710         TDB-TDACUST.\n046712     MOVE TDAC-INQ-SECR-CD OF TDACUST TO TDB-TDAC-INQ-SECR-CD OF  \n046714         TDB-TDACUST.\n046716     MOVE TDAC-PRIVACY OF TDACUST TO TDB-TDAC-PRIVACY OF          \n046718         TDB-TDACUST.\n046720     MOVE TDAC-BK-DEF-CD1 OF TDACUST TO TDB-TDAC-BK-DEF-CD1 OF    \n046722         TDB-TDACUST.\n046724     MOVE TDAC-BK-DEF-CD2 OF TDACUST TO TDB-TDAC-BK-DEF-CD2 OF    \n046726         TDB-TDACUST.\n046728     MOVE TDAC-BK-DEF-CD3 OF TDACUST TO TDB-TDAC-BK-DEF-CD3 OF    \n046730         TDB-TDACUST.\n046732     MOVE TDAC-BK-DEF-CD4 OF TDACUST TO TDB-TDAC-BK-DEF-CD4 OF    \n046734         TDB-TDACUST.\n046736     MOVE TDAC-BK-DEF-CD5 OF TDACUST TO TDB-TDAC-BK-DEF-CD5 OF    \n046738         TDB-TDACUST.\n046740     MOVE TDAC-EMPLOYEE-ID OF TDACUST TO TDB-TDAC-EMPLOYEE-ID OF  \n046742         TDB-TDACUST.\n046744     MOVE TDAC-EMAIL-ADDR OF TDACUST TO TDB-TDAC-EMAIL-ADDR OF    \n046746         TDB-TDACUST.\n046748     MOVE TDAC-EMAIL-PSSWRD OF TDACUST TO TDB-TDAC-EMAIL-PSSWRD   \n046750         OF TDB-TDACUST.\n046752     MOVE TDAC-GENDER OF TDACUST TO TDB-TDAC-GENDER OF            \n046754         TDB-TDACUST.\n046756     MOVE TDAC-NEW-CUST OF TDACUST TO TDB-TDAC-NEW-CUST OF        \n046758         TDB-TDACUST.\n046760     MOVE TDAC-OPEN-DT OF TDACUST TO TDB-TDAC-OPEN-DT OF          \n046762         TDB-TDACUST.\n046764     MOVE TDAC-LUPD-DATE OF TDACUST TO TDB-TDAC-LUPD-DATE OF      \n046766         TDB-TDACUST.\n046768     MOVE TDAC-LUPD-TIME OF TDACUST TO TDB-TDAC-LUPD-TIME OF      \n046770         TDB-TDACUST.\n046772     MOVE TDAC-LST-CONTACT OF TDACUST TO TDB-TDAC-LST-CONTACT OF  \n046774         TDB-TDACUST.\n046776     MOVE TDAC-BIRTH-DT OF TDACUST TO TDB-TDAC-BIRTH-DT OF        \n046778         TDB-TDACUST.\n046780     MOVE TDAC-BIRTH-DT-2 OF TDACUST TO TDB-TDAC-BIRTH-DT-2 OF    \n046782         TDB-TDACUST.\n046784     MOVE TDAC-BIRTH-DT-3 OF TDACUST TO TDB-TDAC-BIRTH-DT-3 OF    \n046786         TDB-TDACUST.\n046788     MOVE TDAC-DEATH-DT OF TDACUST TO TDB-TDAC-DEATH-DT OF        \n046790         TDB-TDACUST.\n046792     MOVE TDAC-ADD-DT OF TDACUST TO TDB-TDAC-ADD-DT OF            \n046794         TDB-TDACUST.\n046796     MOVE TDAC-ADD-TM OF TDACUST TO TDB-TDAC-ADD-TM OF            \n046798         TDB-TDACUST.\n046800     MOVE TDAC-ROTH-DATE OF TDACUST TO TDB-TDAC-ROTH-DATE OF      \n046802         TDB-TDACUST.\n046804     MOVE TDAC-CD-BAL OF TDACUST TO TDB-TDAC-CD-BAL OF            \n046806         TDB-TDACUST.\n046808     MOVE TDAC-CD-BAL-BYR OF TDACUST TO TDB-TDAC-CD-BAL-BYR OF    \n046810         TDB-TDACUST.\n046812     MOVE TDAC-CD-PENLTY OF TDACUST TO TDB-TDAC-CD-PENLTY OF      \n046814         TDB-TDACUST.\n046816     MOVE TDAC-CD-WTHLD OF TDACUST TO TDB-TDAC-CD-WTHLD OF        \n046818         TDB-TDACUST.\n046820     MOVE TDAC-CD-INT OF TDACUST TO TDB-TDAC-CD-INT OF            \n046822         TDB-TDACUST.\n046824     MOVE TDAC-CD-OID-INT OF TDACUST TO TDB-TDAC-CD-OID-INT OF    \n046826         TDB-TDACUST.\n046828     MOVE TDAC-IRA-BAL OF TDACUST TO TDB-TDAC-IRA-BAL OF          \n046830         TDB-TDACUST.\n046832     MOVE TDAC-IRA-BAL-BYR OF TDACUST TO TDB-TDAC-IRA-BAL-BYR OF  \n046834         TDB-TDACUST.\n046836     MOVE TDAC-IRA-PENLTY OF TDACUST TO TDB-TDAC-IRA-PENLTY OF    \n046838         TDB-TDACUST.\n046840     MOVE TDAC-IRA-WTHLD OF TDACUST TO TDB-TDAC-IRA-WTHLD OF      \n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    433 lines from 22984 to 23416.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 48, "total_chunks": 55, "start_line": 22984, "end_line": 23416, "line_count": 433}

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
- Source code length: 28575 characters

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
CHUNK 48 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 22984 to 23416 (433 lines)
Chunk Tokens (estimated): ~8,066
Actual Input Tokens: 9,472 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 22984-23416 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 48 of 55 chunks
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
      The source code below is only CHUNK 48 of 55.


=============================================================================
CHUNK 48 SOURCE CODE (Lines 22984-23416)
=============================================================================

```cobol
045976         TDB-TDACUST.
045978     MOVE HOLD-TDAC-N3-MODIFIED OF HOLD-TDACUST TO                
045980         TDB-TDAC-N3-MODIFIED OF TDB-TDACUST.
045982     MOVE HOLD-TDAC-N3-PRINT-CD OF HOLD-TDACUST TO                
045984         TDB-TDAC-N3-PRINT-CD OF TDB-TDACUST.
045986     MOVE HOLD-TDAC-N3-KEY OF HOLD-TDACUST TO TDB-TDAC-N3-KEY OF  
045988         TDB-TDACUST.
045990     MOVE HOLD-TDAC-N3-FIRST OF HOLD-TDACUST TO TDB-TDAC-N3-FIRST 
045992         OF TDB-TDACUST.
045994     MOVE HOLD-TDAC-N3-MID OF HOLD-TDACUST TO TDB-TDAC-N3-MID OF  
045996         TDB-TDACUST.
045998     MOVE HOLD-TDAC-N3-LAST OF HOLD-TDACUST TO TDB-TDAC-N3-LAST   
046000         OF TDB-TDACUST.
046002     MOVE HOLD-TDAC-N3-PREFIX OF HOLD-TDACUST TO                  
046004         TDB-TDAC-N3-PREFIX OF TDB-TDACUST.
046006     MOVE HOLD-TDAC-N3-SUFFIX OF HOLD-TDACUST TO                  
046008         TDB-TDAC-N3-SUFFIX OF TDB-TDACUST.
046010     MOVE HOLD-TDAC-N3-FAMILIAR OF HOLD-TDACUST TO                
046012         TDB-TDAC-N3-FAMILIAR OF TDB-TDACUST.
046014     MOVE HOLD-TDAC-N3-PRT-PFX OF HOLD-TDACUST TO                 
046016         TDB-TDAC-N3-PRT-PFX OF TDB-TDACUST.
046018     MOVE HOLD-TDAC-N3-PRT-SFX OF HOLD-TDACUST TO                 
046020         TDB-TDAC-N3-PRT-SFX OF TDB-TDACUST.
046022     MOVE HOLD-TDAC-N3-DESIGNAT OF HOLD-TDACUST TO                
046024         TDB-TDAC-N3-DESIGNAT OF TDB-TDACUST.
046026     MOVE HOLD-TDAC-ADDR-KEY OF HOLD-TDACUST TO TDB-TDAC-ADDR-KEY 
046028         OF TDB-TDACUST.
046030     MOVE HOLD-TDAC-ADDR-1 OF HOLD-TDACUST TO TDB-TDAC-ADDR-1 OF  
046032         TDB-TDACUST.
046034     MOVE HOLD-TDAC-ADDR-2 OF HOLD-TDACUST TO TDB-TDAC-ADDR-2 OF  
046036         TDB-TDACUST.
046038     MOVE HOLD-TDAC-CITY OF HOLD-TDACUST TO TDB-TDAC-CITY OF      
046040         TDB-TDACUST.
046042     MOVE HOLD-TDAC-STATE OF HOLD-TDACUST TO TDB-TDAC-STATE OF    
046044         TDB-TDACUST.
046046     MOVE HOLD-TDAC-PROVINCE OF HOLD-TDACUST TO TDB-TDAC-PROVINCE 
046048         OF TDB-TDACUST.
046050     MOVE HOLD-TDAC-COUNTRY OF HOLD-TDACUST TO TDB-TDAC-COUNTRY   
046052         OF TDB-TDACUST.
046054     MOVE HOLD-TDAC-ZIP OF HOLD-TDACUST TO TDB-TDAC-ZIP OF        
046056         TDB-TDACUST.
046058     MOVE HOLD-TDAC-ZIP-4 OF HOLD-TDACUST TO TDB-TDAC-ZIP-4 OF    
046060         TDB-TDACUST.
046062     MOVE HOLD-TDAC-LONGITUDE OF HOLD-TDACUST TO                  
046064         TDB-TDAC-LONGITUDE OF TDB-TDACUST.
046066     MOVE HOLD-TDAC-LATITUDE OF HOLD-TDACUST TO TDB-TDAC-LATITUDE 
046068         OF TDB-TDACUST.
046070     MOVE HOLD-TDAC-MAIL-CD OF HOLD-TDACUST TO TDB-TDAC-MAIL-CD   
046072         OF TDB-TDACUST.
046074     MOVE HOLD-TDAC-TICKLER-FLAG OF HOLD-TDACUST TO               
046076         TDB-TDAC-TICKLER-FLAG OF TDB-TDACUST.
046078     MOVE HOLD-TDAC-RESIDENT-CD OF HOLD-TDACUST TO                
046080         TDB-TDAC-RESIDENT-CD OF TDB-TDACUST.
046082     MOVE HOLD-TDAC-ALIEN-CD OF HOLD-TDACUST TO TDB-TDAC-ALIEN-CD 
046084         OF TDB-TDACUST.
046086     MOVE HOLD-TDAC-SHT-NAME OF HOLD-TDACUST TO TDB-TDAC-SHT-NAME 
046088         OF TDB-TDACUST.
046090     MOVE HOLD-TDAC-BAR-CD OF HOLD-TDACUST TO TDB-TDAC-BAR-CD OF  
046092         TDB-TDACUST.
046094     MOVE HOLD-TDAC-PHONE-1 OF HOLD-TDACUST TO TDB-TDAC-PHONE-1   
046096         OF TDB-TDACUST.
046098     MOVE HOLD-TDAC-PHONE-2 OF HOLD-TDACUST TO TDB-TDAC-PHONE-2   
046100         OF TDB-TDACUST.
046102     MOVE HOLD-TDAC-TIN-CD OF HOLD-TDACUST TO TDB-TDAC-TIN-CD OF  
046104         TDB-TDACUST.
046106     MOVE HOLD-TDAC-TIN-CERT-CD OF HOLD-TDACUST TO                
046108         TDB-TDAC-TIN-CERT-CD OF TDB-TDACUST.
046110     MOVE HOLD-TDAC-TIN-CERT-DT OF HOLD-TDACUST TO                
046112         TDB-TDAC-TIN-CERT-DT OF TDB-TDACUST.
046114     MOVE HOLD-TDAC-TIN-NBR OF HOLD-TDACUST TO TDB-TDAC-TIN-NBR   
046116         OF TDB-TDACUST.
046118     MOVE HOLD-TDAC-OFFICER OF HOLD-TDACUST TO TDB-TDAC-OFFICER   
046120         OF TDB-TDACUST.
046122     MOVE HOLD-TDAC-EMP-CD OF HOLD-TDACUST TO TDB-TDAC-EMP-CD OF  
046124         TDB-TDACUST.
046126     MOVE HOLD-TDAC-FREE-MARK OF HOLD-TDACUST TO                  
046128         TDB-TDAC-FREE-MARK OF TDB-TDACUST.
046130     MOVE HOLD-TDAC-INQ-SECR-CD OF HOLD-TDACUST TO                
046132         TDB-TDAC-INQ-SECR-CD OF TDB-TDACUST.
046134     MOVE HOLD-TDAC-PRIVACY OF HOLD-TDACUST TO TDB-TDAC-PRIVACY   
046136         OF TDB-TDACUST.
046138     MOVE HOLD-TDAC-BK-DEF-CD1 OF HOLD-TDACUST TO                 
046140         TDB-TDAC-BK-DEF-CD1 OF TDB-TDACUST.
046142     MOVE HOLD-TDAC-BK-DEF-CD2 OF HOLD-TDACUST TO                 
046144         TDB-TDAC-BK-DEF-CD2 OF TDB-TDACUST.
046146     MOVE HOLD-TDAC-BK-DEF-CD3 OF HOLD-TDACUST TO                 
046148         TDB-TDAC-BK-DEF-CD3 OF TDB-TDACUST.
046150     MOVE HOLD-TDAC-BK-DEF-CD4 OF HOLD-TDACUST TO                 
046152         TDB-TDAC-BK-DEF-CD4 OF TDB-TDACUST.
046154     MOVE HOLD-TDAC-BK-DEF-CD5 OF HOLD-TDACUST TO                 
046156         TDB-TDAC-BK-DEF-CD5 OF TDB-TDACUST.
046158     MOVE HOLD-TDAC-EMPLOYEE-ID OF HOLD-TDACUST TO                
046160         TDB-TDAC-EMPLOYEE-ID OF TDB-TDACUST.
046162     MOVE HOLD-TDAC-EMAIL-ADDR OF HOLD-TDACUST TO                 
046164         TDB-TDAC-EMAIL-ADDR OF TDB-TDACUST.
046166     MOVE HOLD-TDAC-EMAIL-ADDR-1-30 OF HOLD-TDACUST TO            
046168         TDB-TDAC-EMAIL-ADDR-1-30 OF TDB-TDACUST.
046170     MOVE HOLD-TDAC-EMAIL-ADDR-31-60 OF HOLD-TDACUST TO           
046172         TDB-TDAC-EMAIL-ADDR-31-60 OF TDB-TDACUST.
046174     MOVE HOLD-TDAC-EMAIL-ADDR-61-90 OF HOLD-TDACUST TO           
046176         TDB-TDAC-EMAIL-ADDR-61-90 OF TDB-TDACUST.
046178     MOVE HOLD-TDAC-EMAIL-ADDR-91-100 OF HOLD-TDACUST TO          
046180         TDB-TDAC-EMAIL-ADDR-91-100 OF TDB-TDACUST.
046182     MOVE HOLD-TDAC-EMAIL-ADDR-1-50 OF HOLD-TDACUST TO            
046184         TDB-TDAC-EMAIL-ADDR-1-50 OF TDB-TDACUST.
046186     MOVE HOLD-TDAC-EMAIL-ADDR-51-100 OF HOLD-TDACUST TO          
046188         TDB-TDAC-EMAIL-ADDR-51-100 OF TDB-TDACUST.
046190     MOVE HOLD-TDAC-EMAIL-PSSWRD OF HOLD-TDACUST TO               
046192         TDB-TDAC-EMAIL-PSSWRD OF TDB-TDACUST.
046194     MOVE HOLD-TDAC-GENDER OF HOLD-TDACUST TO TDB-TDAC-GENDER OF  
046196         TDB-TDACUST.
046198     MOVE HOLD-TDAC-NEW-CUST OF HOLD-TDACUST TO TDB-TDAC-NEW-CUST 
046200         OF TDB-TDACUST.
046202     MOVE HOLD-TDAC-OPEN-DT OF HOLD-TDACUST TO TDB-TDAC-OPEN-DT   
046204         OF TDB-TDACUST.
046206     MOVE HOLD-TDAC-LUPD-DATE OF HOLD-TDACUST TO                  
046208         TDB-TDAC-LUPD-DATE OF TDB-TDACUST.
046210     MOVE HOLD-TDAC-LUPD-TIME OF HOLD-TDACUST TO                  
046212         TDB-TDAC-LUPD-TIME OF TDB-TDACUST.
046214     MOVE HOLD-TDAC-LST-CONTACT OF HOLD-TDACUST TO                
046216         TDB-TDAC-LST-CONTACT OF TDB-TDACUST.
046218     MOVE HOLD-TDAC-BIRTH-DT OF HOLD-TDACUST TO TDB-TDAC-BIRTH-DT 
046220         OF TDB-TDACUST.
046222     MOVE HOLD-TDAC-BIRTH-DT-2 OF HOLD-TDACUST TO                 
046224         TDB-TDAC-BIRTH-DT-2 OF TDB-TDACUST.
046226     MOVE HOLD-TDAC-BIRTH-DT-3 OF HOLD-TDACUST TO                 
046228         TDB-TDAC-BIRTH-DT-3 OF TDB-TDACUST.
046230     MOVE HOLD-TDAC-DEATH-DT OF HOLD-TDACUST TO TDB-TDAC-DEATH-DT 
046232         OF TDB-TDACUST.
046234     MOVE HOLD-TDAC-ADD-DT OF HOLD-TDACUST TO TDB-TDAC-ADD-DT OF  
046236         TDB-TDACUST.
046238     MOVE HOLD-TDAC-ADD-TM OF HOLD-TDACUST TO TDB-TDAC-ADD-TM OF  
046240         TDB-TDACUST.
046242     MOVE HOLD-TDAC-ROTH-DATE OF HOLD-TDACUST TO                  
046244         TDB-TDAC-ROTH-DATE OF TDB-TDACUST.
046246     MOVE HOLD-TDAC-CD-BAL OF HOLD-TDACUST TO TDB-TDAC-CD-BAL OF  
046248         TDB-TDACUST.
046250     MOVE HOLD-TDAC-CD-BAL-BYR OF HOLD-TDACUST TO                 
046252         TDB-TDAC-CD-BAL-BYR OF TDB-TDACUST.
046254     MOVE HOLD-TDAC-CD-PENLTY OF HOLD-TDACUST TO                  
046256         TDB-TDAC-CD-PENLTY OF TDB-TDACUST.
046258     MOVE HOLD-TDAC-CD-WTHLD OF HOLD-TDACUST TO TDB-TDAC-CD-WTHLD 
046260         OF TDB-TDACUST.
046262     MOVE HOLD-TDAC-CD-INT OF HOLD-TDACUST TO TDB-TDAC-CD-INT OF  
046264         TDB-TDACUST.
046266     MOVE HOLD-TDAC-CD-OID-INT OF HOLD-TDACUST TO                 
046268         TDB-TDAC-CD-OID-INT OF TDB-TDACUST.
046270     MOVE HOLD-TDAC-IRA-BAL OF HOLD-TDACUST TO TDB-TDAC-IRA-BAL   
046272         OF TDB-TDACUST.
046274     MOVE HOLD-TDAC-IRA-BAL-BYR OF HOLD-TDACUST TO                
046276         TDB-TDAC-IRA-BAL-BYR OF TDB-TDACUST.
046278     MOVE HOLD-TDAC-IRA-PENLTY OF HOLD-TDACUST TO                 
046280         TDB-TDAC-IRA-PENLTY OF TDB-TDACUST.
046282     MOVE HOLD-TDAC-IRA-WTHLD OF HOLD-TDACUST TO                  
046284         TDB-TDAC-IRA-WTHLD OF TDB-TDACUST.
046286     MOVE HOLD-TDAC-IRA-INT OF HOLD-TDACUST TO TDB-TDAC-IRA-INT   
046288         OF TDB-TDACUST.
046290     MOVE HOLD-TDAC-IRA-CONTR OF HOLD-TDACUST TO                  
046292         TDB-TDAC-IRA-CONTR OF TDB-TDACUST.
046294     MOVE HOLD-TDAC-IRA-CONTR-LY OF HOLD-TDACUST TO               
046296         TDB-TDAC-IRA-CONTR-LY OF TDB-TDACUST.
046298     MOVE HOLD-TDAC-IRA-DISTR OF HOLD-TDACUST TO                  
046300         TDB-TDAC-IRA-DISTR OF TDB-TDACUST.
046302     MOVE HOLD-TDAC-IRA-DISTR-LY OF HOLD-TDACUST TO               
046304         TDB-TDAC-IRA-DISTR-LY OF TDB-TDACUST.
046306     MOVE HOLD-TDAC-IRA-ROLLOVER OF HOLD-TDACUST TO               
046308         TDB-TDAC-IRA-ROLLOVER OF TDB-TDACUST.
046310     MOVE HOLD-TDAC-IRA-TRF-IN OF HOLD-TDACUST TO                 
046312         TDB-TDAC-IRA-TRF-IN OF TDB-TDACUST.
046314     MOVE HOLD-TDAC-IRA-TRF-OUT OF HOLD-TDACUST TO                
046316         TDB-TDAC-IRA-TRF-OUT OF TDB-TDACUST.
046318     MOVE HOLD-TDAC-IRA-FAIR-MKT OF HOLD-TDACUST TO               
046320         TDB-TDAC-IRA-FAIR-MKT OF TDB-TDACUST.
046322     MOVE HOLD-TDAC-CIF-REMARK OF HOLD-TDACUST TO                 
046324         TDB-TDAC-CIF-REMARK OF TDB-TDACUST.
046326     MOVE HOLD-TDAC-CD-ST-WHLD OF HOLD-TDACUST TO                 
046328         TDB-TDAC-CD-ST-WHLD OF TDB-TDACUST.
046330     MOVE HOLD-TDAC-IRA-ST-WHLD OF HOLD-TDACUST TO                
046332         TDB-TDAC-IRA-ST-WHLD OF TDB-TDACUST.
046334     MOVE 1 TO Z-II.
046336 Z-14-7-1-LOOP.
046338     IF Z-II > 12
046340         GO TO Z-14-7-1-LOOP-XIT.
046342     MOVE HOLD-TDAC-CURR-YR-AMT OF HOLD-TDACUST (Z-II) TO         
046344         TDB-TDAC-CURR-YR-AMT OF TDB-TDACUST (Z-II).
046346     MOVE HOLD-TDAC-LAST-YR-AMT OF HOLD-TDACUST (Z-II) TO         
046348         TDB-TDAC-LAST-YR-AMT OF TDB-TDACUST (Z-II).
046350     ADD 1 TO Z-II.
046352     GO TO Z-14-7-1-LOOP.
046354 Z-14-7-1-LOOP-XIT.
046356     MOVE HOLD-TDAC-TIN-CD-2 OF HOLD-TDACUST TO TDB-TDAC-TIN-CD-2 
046358         OF TDB-TDACUST.
046360     MOVE HOLD-TDAC-TIN-CRT-CD-2 OF HOLD-TDACUST TO               
046362         TDB-TDAC-TIN-CRT-CD-2 OF TDB-TDACUST.
046364     MOVE HOLD-TDAC-TIN-CRT-DT-2 OF HOLD-TDACUST TO               
046366         TDB-TDAC-TIN-CRT-DT-2 OF TDB-TDACUST.
046368     MOVE HOLD-TDAC-TIN-NBR-2 OF HOLD-TDACUST TO                  
046370         TDB-TDAC-TIN-NBR-2 OF TDB-TDACUST.
046372     MOVE HOLD-TDAC-TIN-CD-3 OF HOLD-TDACUST TO TDB-TDAC-TIN-CD-3 
046374         OF TDB-TDACUST.
046376     MOVE HOLD-TDAC-TIN-CRT-CD-3 OF HOLD-TDACUST TO               
046378         TDB-TDAC-TIN-CRT-CD-3 OF TDB-TDACUST.
046380     MOVE HOLD-TDAC-TIN-CRT-DT-3 OF HOLD-TDACUST TO               
046382         TDB-TDAC-TIN-CRT-DT-3 OF TDB-TDACUST.
046384     MOVE HOLD-TDAC-TIN-NBR-3 OF HOLD-TDACUST TO                  
046386         TDB-TDAC-TIN-NBR-3 OF TDB-TDACUST.
046388     MOVE HOLD-TDAC-NAICS-CD OF HOLD-TDACUST TO TDB-TDAC-NAICS-CD 
046390         OF TDB-TDACUST.
046392     MOVE HOLD-TDAC-CIF-PASS-THR OF HOLD-TDACUST TO               
046394         TDB-TDAC-CIF-PASS-THR OF TDB-TDACUST.
046396     MOVE HOLD-TDAC-EMAIL-NTC OF HOLD-TDACUST TO                  
046398         TDB-TDAC-EMAIL-NTC OF TDB-TDACUST.
046400     MOVE HOLD-TDAC-RMD-YR-AMT OF HOLD-TDACUST TO                 
046402         TDB-TDAC-RMD-YR-AMT OF TDB-TDACUST.
046404     MOVE HOLD-TDAC-ADDR-CHG-DT OF HOLD-TDACUST TO                
046406         TDB-TDAC-ADDR-CHG-DT OF TDB-TDACUST.
046408     MOVE HOLD-TDAC-WTHLD-CD OF HOLD-TDACUST TO TDB-TDAC-WTHLD-CD 
046410         OF TDB-TDACUST.
046412     MOVE HOLD-TDAC-ST-WHLD-CD OF HOLD-TDACUST TO                 
046414         TDB-TDAC-ST-WHLD-CD OF TDB-TDACUST.
046416     MOVE HOLD-TDAC-WTHLD-AMT OF HOLD-TDACUST TO                  
046418         TDB-TDAC-WTHLD-AMT OF TDB-TDACUST.
046420     MOVE HOLD-TDAC-ST-WHLD-AMT OF HOLD-TDACUST TO                
046422         TDB-TDAC-ST-WHLD-AMT OF TDB-TDACUST.
046424     MOVE HOLD-TDAC-FOREIGN-LANG OF HOLD-TDACUST TO               
046426         TDB-TDAC-FOREIGN-LANG OF TDB-TDACUST.
046428     MOVE HOLD-TDAC-L-ROLLOVR-DT OF HOLD-TDACUST TO               
046430         TDB-TDAC-L-ROLLOVR-DT OF TDB-TDACUST.
046432     MOVE HOLD-TDAC-CUSTM-FIELDS OF HOLD-TDACUST TO               
046434         TDB-TDAC-CUSTM-FIELDS OF TDB-TDACUST.
046436     MOVE HOLD-TDAC-LLC-NAME OF HOLD-TDACUST TO TDB-TDAC-LLC-NAME 
046438         OF TDB-TDACUST.
046440     MOVE HOLD-TDAC-LLC-TIN-CD OF HOLD-TDACUST TO                 
046442         TDB-TDAC-LLC-TIN-CD OF TDB-TDACUST.
046444     MOVE HOLD-TDAC-LLC-TIN OF HOLD-TDACUST TO TDB-TDAC-LLC-TIN   
046446         OF TDB-TDACUST.
046448     MOVE HOLD-TDAC-FOREIGN-PHN OF HOLD-TDACUST TO                
046450         TDB-TDAC-FOREIGN-PHN OF TDB-TDACUST.
046452     MOVE 0350 TO TDB-MESSAGE-NBR.
046454     GO TO Z-14-4-ENDIF.
046456 Z-14-4-2-ELSE.
046458     MOVE TDAC-BANK OF TDACUST TO TDB-TDAC-BANK OF TDB-TDACUST.
046460     MOVE TDAC-CUST OF TDACUST TO TDB-TDAC-CUST OF TDB-TDACUST.
046462     MOVE TDAC-BRCH OF TDACUST TO TDB-TDAC-BRCH OF TDB-TDACUST.
046464     MOVE TDAC-STATUS OF TDACUST TO TDB-TDAC-STATUS OF            
046466         TDB-TDACUST.
046468     MOVE TDAC-NAME-1 OF TDACUST TO TDB-TDAC-NAME-1 OF            
046470         TDB-TDACUST.
046472     MOVE TDAC-N1-KEY OF TDACUST TO TDB-TDAC-N1-KEY OF            
046474         TDB-TDACUST.
046476     MOVE TDAC-N1-FIRST OF TDACUST TO TDB-TDAC-N1-FIRST OF        
046478         TDB-TDACUST.
046480     MOVE TDAC-N1-MID OF TDACUST TO TDB-TDAC-N1-MID OF            
046482         TDB-TDACUST.
046484     MOVE TDAC-N1-LAST OF TDACUST TO TDB-TDAC-N1-LAST OF          
046486         TDB-TDACUST.
046488     MOVE TDAC-N1-PREFIX OF TDACUST TO TDB-TDAC-N1-PREFIX OF      
046490         TDB-TDACUST.
046492     MOVE TDAC-N1-SUFFIX OF TDACUST TO TDB-TDAC-N1-SUFFIX OF      
046494         TDB-TDACUST.
046496     MOVE TDAC-N1-FAMILIAR OF TDACUST TO TDB-TDAC-N1-FAMILIAR OF  
046498         TDB-TDACUST.
046500     MOVE TDAC-N1-PRT-PFX OF TDACUST TO TDB-TDAC-N1-PRT-PFX OF    
046502         TDB-TDACUST.
046504     MOVE TDAC-N1-PRT-SFX OF TDACUST TO TDB-TDAC-N1-PRT-SFX OF    
046506         TDB-TDACUST.
046508     MOVE TDAC-N1-DESIGNAT OF TDACUST TO TDB-TDAC-N1-DESIGNAT OF  
046510         TDB-TDACUST.
046512     MOVE TDAC-NAME-2 OF TDACUST TO TDB-TDAC-NAME-2 OF            
046514         TDB-TDACUST.
046516     MOVE TDAC-N2-MODIFIED OF TDACUST TO TDB-TDAC-N2-MODIFIED OF  
046518         TDB-TDACUST.
046520     MOVE TDAC-N2-PRINT-CD OF TDACUST TO TDB-TDAC-N2-PRINT-CD OF  
046522         TDB-TDACUST.
046524     MOVE TDAC-N2-KEY OF TDACUST TO TDB-TDAC-N2-KEY OF            
046526         TDB-TDACUST.
046528     MOVE TDAC-N2-FIRST OF TDACUST TO TDB-TDAC-N2-FIRST OF        
046530         TDB-TDACUST.
046532     MOVE TDAC-N2-MID OF TDACUST TO TDB-TDAC-N2-MID OF            
046534         TDB-TDACUST.
046536     MOVE TDAC-N2-LAST OF TDACUST TO TDB-TDAC-N2-LAST OF          
046538         TDB-TDACUST.
046540     MOVE TDAC-N2-PREFIX OF TDACUST TO TDB-TDAC-N2-PREFIX OF      
046542         TDB-TDACUST.
046544     MOVE TDAC-N2-SUFFIX OF TDACUST TO TDB-TDAC-N2-SUFFIX OF      
046546         TDB-TDACUST.
046548     MOVE TDAC-N2-FAMILIAR OF TDACUST TO TDB-TDAC-N2-FAMILIAR OF  
046550         TDB-TDACUST.
046552     MOVE TDAC-N2-PRT-PFX OF TDACUST TO TDB-TDAC-N2-PRT-PFX OF    
046554         TDB-TDACUST.
046556     MOVE TDAC-N2-PRT-SFX OF TDACUST TO TDB-TDAC-N2-PRT-SFX OF    
046558         TDB-TDACUST.
046560     MOVE TDAC-N2-DESIGNAT OF TDACUST TO TDB-TDAC-N2-DESIGNAT OF  
046562         TDB-TDACUST.
046564     MOVE TDAC-NAME-3 OF TDACUST TO TDB-TDAC-NAME-3 OF            
046566         TDB-TDACUST.
046568     MOVE TDAC-N3-MODIFIED OF TDACUST TO TDB-TDAC-N3-MODIFIED OF  
046570         TDB-TDACUST.
046572     MOVE TDAC-N3-PRINT-CD OF TDACUST TO TDB-TDAC-N3-PRINT-CD OF  
046574         TDB-TDACUST.
046576     MOVE TDAC-N3-KEY OF TDACUST TO TDB-TDAC-N3-KEY OF            
046578         TDB-TDACUST.
046580     MOVE TDAC-N3-FIRST OF TDACUST TO TDB-TDAC-N3-FIRST OF        
046582         TDB-TDACUST.
046584     MOVE TDAC-N3-MID OF TDACUST TO TDB-TDAC-N3-MID OF            
046586         TDB-TDACUST.
046588     MOVE TDAC-N3-LAST OF TDACUST TO TDB-TDAC-N3-LAST OF          
046590         TDB-TDACUST.
046592     MOVE TDAC-N3-PREFIX OF TDACUST TO TDB-TDAC-N3-PREFIX OF      
046594         TDB-TDACUST.
046596     MOVE TDAC-N3-SUFFIX OF TDACUST TO TDB-TDAC-N3-SUFFIX OF      
046598         TDB-TDACUST.
046600     MOVE TDAC-N3-FAMILIAR OF TDACUST TO TDB-TDAC-N3-FAMILIAR OF  
046602         TDB-TDACUST.
046604     MOVE TDAC-N3-PRT-PFX OF TDACUST TO TDB-TDAC-N3-PRT-PFX OF    
046606         TDB-TDACUST.
046608     MOVE TDAC-N3-PRT-SFX OF TDACUST TO TDB-TDAC-N3-PRT-SFX OF    
046610         TDB-TDACUST.
046612     MOVE TDAC-N3-DESIGNAT OF TDACUST TO TDB-TDAC-N3-DESIGNAT OF  
046614         TDB-TDACUST.
046616     MOVE TDAC-ADDR-KEY OF TDACUST TO TDB-TDAC-ADDR-KEY OF        
046618         TDB-TDACUST.
046620     MOVE TDAC-ADDR-1 OF TDACUST TO TDB-TDAC-ADDR-1 OF            
046622         TDB-TDACUST.
046624     MOVE TDAC-ADDR-2 OF TDACUST TO TDB-TDAC-ADDR-2 OF            
046626         TDB-TDACUST.
046628     MOVE TDAC-CITY OF TDACUST TO TDB-TDAC-CITY OF TDB-TDACUST.
046630     MOVE TDAC-STATE OF TDACUST TO TDB-TDAC-STATE OF TDB-TDACUST.
046632     MOVE TDAC-PROVINCE OF TDACUST TO TDB-TDAC-PROVINCE OF        
046634         TDB-TDACUST.
046636     MOVE TDAC-COUNTRY OF TDACUST TO TDB-TDAC-COUNTRY OF          
046638         TDB-TDACUST.
046640     MOVE TDAC-ZIP OF TDACUST TO TDB-TDAC-ZIP OF TDB-TDACUST.
046642     MOVE TDAC-ZIP-4 OF TDACUST TO TDB-TDAC-ZIP-4 OF TDB-TDACUST.
046644     MOVE TDAC-LONGITUDE OF TDACUST TO TDB-TDAC-LONGITUDE OF      
046646         TDB-TDACUST.
046648     MOVE TDAC-LATITUDE OF TDACUST TO TDB-TDAC-LATITUDE OF        
046650         TDB-TDACUST.
046652     MOVE TDAC-MAIL-CD OF TDACUST TO TDB-TDAC-MAIL-CD OF          
046654         TDB-TDACUST.
046656     MOVE TDAC-TICKLER-FLAG OF TDACUST TO TDB-TDAC-TICKLER-FLAG   
046658         OF TDB-TDACUST.
046660     MOVE TDAC-RESIDENT-CD OF TDACUST TO TDB-TDAC-RESIDENT-CD OF  
046662         TDB-TDACUST.
046664     MOVE TDAC-ALIEN-CD OF TDACUST TO TDB-TDAC-ALIEN-CD OF        
046666         TDB-TDACUST.
046668     MOVE TDAC-SHT-NAME OF TDACUST TO TDB-TDAC-SHT-NAME OF        
046670         TDB-TDACUST.
046672     MOVE TDAC-BAR-CD OF TDACUST TO TDB-TDAC-BAR-CD OF            
046674         TDB-TDACUST.
046676     MOVE TDAC-PHONE-1 OF TDACUST TO TDB-TDAC-PHONE-1 OF          
046678         TDB-TDACUST.
046680     MOVE TDAC-PHONE-2 OF TDACUST TO TDB-TDAC-PHONE-2 OF          
046682         TDB-TDACUST.
046684     MOVE TDAC-TIN-CD OF TDACUST TO TDB-TDAC-TIN-CD OF            
046686         TDB-TDACUST.
046688     MOVE TDAC-TIN-CERT-CD OF TDACUST TO TDB-TDAC-TIN-CERT-CD OF  
046690         TDB-TDACUST.
046692     MOVE TDAC-TIN-CERT-DT OF TDACUST TO TDB-TDAC-TIN-CERT-DT OF  
046694         TDB-TDACUST.
046696     MOVE TDAC-TIN-NBR OF TDACUST TO TDB-TDAC-TIN-NBR OF          
046698         TDB-TDACUST.
046700     MOVE TDAC-OFFICER OF TDACUST TO TDB-TDAC-OFFICER OF          
046702         TDB-TDACUST.
046704     MOVE TDAC-EMP-CD OF TDACUST TO TDB-TDAC-EMP-CD OF            
046706         TDB-TDACUST.
046708     MOVE TDAC-FREE-MARK OF TDACUST TO TDB-TDAC-FREE-MARK OF      
046710         TDB-TDACUST.
046712     MOVE TDAC-INQ-SECR-CD OF TDACUST TO TDB-TDAC-INQ-SECR-CD OF  
046714         TDB-TDACUST.
046716     MOVE TDAC-PRIVACY OF TDACUST TO TDB-TDAC-PRIVACY OF          
046718         TDB-TDACUST.
046720     MOVE TDAC-BK-DEF-CD1 OF TDACUST TO TDB-TDAC-BK-DEF-CD1 OF    
046722         TDB-TDACUST.
046724     MOVE TDAC-BK-DEF-CD2 OF TDACUST TO TDB-TDAC-BK-DEF-CD2 OF    
046726         TDB-TDACUST.
046728     MOVE TDAC-BK-DEF-CD3 OF TDACUST TO TDB-TDAC-BK-DEF-CD3 OF    
046730         TDB-TDACUST.
046732     MOVE TDAC-BK-DEF-CD4 OF TDACUST TO TDB-TDAC-BK-DEF-CD4 OF    
046734         TDB-TDACUST.
046736     MOVE TDAC-BK-DEF-CD5 OF TDACUST TO TDB-TDAC-BK-DEF-CD5 OF    
046738         TDB-TDACUST.
046740     MOVE TDAC-EMPLOYEE-ID OF TDACUST TO TDB-TDAC-EMPLOYEE-ID OF  
046742         TDB-TDACUST.
046744     MOVE TDAC-EMAIL-ADDR OF TDACUST TO TDB-TDAC-EMAIL-ADDR OF    
046746         TDB-TDACUST.
046748     MOVE TDAC-EMAIL-PSSWRD OF TDACUST TO TDB-TDAC-EMAIL-PSSWRD   
046750         OF TDB-TDACUST.
046752     MOVE TDAC-GENDER OF TDACUST TO TDB-TDAC-GENDER OF            
046754         TDB-TDACUST.
046756     MOVE TDAC-NEW-CUST OF TDACUST TO TDB-TDAC-NEW-CUST OF        
046758         TDB-TDACUST.
046760     MOVE TDAC-OPEN-DT OF TDACUST TO TDB-TDAC-OPEN-DT OF          
046762         TDB-TDACUST.
046764     MOVE TDAC-LUPD-DATE OF TDACUST TO TDB-TDAC-LUPD-DATE OF      
046766         TDB-TDACUST.
046768     MOVE TDAC-LUPD-TIME OF TDACUST TO TDB-TDAC-LUPD-TIME OF      
046770         TDB-TDACUST.
046772     MOVE TDAC-LST-CONTACT OF TDACUST TO TDB-TDAC-LST-CONTACT OF  
046774         TDB-TDACUST.
046776     MOVE TDAC-BIRTH-DT OF TDACUST TO TDB-TDAC-BIRTH-DT OF        
046778         TDB-TDACUST.
046780     MOVE TDAC-BIRTH-DT-2 OF TDACUST TO TDB-TDAC-BIRTH-DT-2 OF    
046782         TDB-TDACUST.
046784     MOVE TDAC-BIRTH-DT-3 OF TDACUST TO TDB-TDAC-BIRTH-DT-3 OF    
046786         TDB-TDACUST.
046788     MOVE TDAC-DEATH-DT OF TDACUST TO TDB-TDAC-DEATH-DT OF        
046790         TDB-TDACUST.
046792     MOVE TDAC-ADD-DT OF TDACUST TO TDB-TDAC-ADD-DT OF            
046794         TDB-TDACUST.
046796     MOVE TDAC-ADD-TM OF TDACUST TO TDB-TDAC-ADD-TM OF            
046798         TDB-TDACUST.
046800     MOVE TDAC-ROTH-DATE OF TDACUST TO TDB-TDAC-ROTH-DATE OF      
046802         TDB-TDACUST.
046804     MOVE TDAC-CD-BAL OF TDACUST TO TDB-TDAC-CD-BAL OF            
046806         TDB-TDACUST.
046808     MOVE TDAC-CD-BAL-BYR OF TDACUST TO TDB-TDAC-CD-BAL-BYR OF    
046810         TDB-TDACUST.
046812     MOVE TDAC-CD-PENLTY OF TDACUST TO TDB-TDAC-CD-PENLTY OF      
046814         TDB-TDACUST.
046816     MOVE TDAC-CD-WTHLD OF TDACUST TO TDB-TDAC-CD-WTHLD OF        
046818         TDB-TDACUST.
046820     MOVE TDAC-CD-INT OF TDACUST TO TDB-TDAC-CD-INT OF            
046822         TDB-TDACUST.
046824     MOVE TDAC-CD-OID-INT OF TDACUST TO TDB-TDAC-CD-OID-INT OF    
046826         TDB-TDACUST.
046828     MOVE TDAC-IRA-BAL OF TDACUST TO TDB-TDAC-IRA-BAL OF          
046830         TDB-TDACUST.
046832     MOVE TDAC-IRA-BAL-BYR OF TDACUST TO TDB-TDAC-IRA-BAL-BYR OF  
046834         TDB-TDACUST.
046836     MOVE TDAC-IRA-PENLTY OF TDACUST TO TDB-TDAC-IRA-PENLTY OF    
046838         TDB-TDACUST.
046840     MOVE TDAC-IRA-WTHLD OF TDACUST TO TDB-TDAC-IRA-WTHLD OF      
```

⚠️  This is the source code you must document.
    433 lines from 22984 to 23416.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

