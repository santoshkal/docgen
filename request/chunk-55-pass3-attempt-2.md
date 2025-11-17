# LLM Request Debug File
Generated: 2025-11-14T19:56:40.111012

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 55/55
- **Model**: gpt-4.1
- **Chunk Number**: 55
- **Pass Number**: 3
- **Attempt Number**: 2 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~4,186 tokens
- **Total Input**: ~6,144 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 55/55" (ID: detailed-code-explanation)

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


**CHUNK 55 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-14T17:36:35.036798", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 55 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 26516 to 26755 (240 lines)\nChunk Tokens (estimated): ~3,563\nActual Input Tokens: 4,969 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 26516-26755 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 55 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 55 of 55.\n\n\n=============================================================================\nCHUNK 55 SOURCE CODE (Lines 26516-26755)\n=============================================================================\n\n```cobol\n053040 Z-35-2-285-ELSE.\n053042     IF HOLD-TDA-ACTVC-CODE = 0819\n053044         NEXT SENTENCE ELSE\n053046         GO TO Z-35-2-286-ELSE.\n053048     MOVE WS-CHG-WK-X-3 TO HOLD-TDAC-OFFICER.\n053050     GO TO Z-35-2-ENDIF.\n053052 Z-35-2-286-ELSE.\n053054     IF HOLD-TDA-ACTVC-CODE = 0820\n053056         NEXT SENTENCE ELSE\n053058         GO TO Z-35-2-287-ELSE.\n053060     MOVE WS-CHG-WK-X-1 TO HOLD-TDAC-TIN-CD.\n053062     GO TO Z-35-2-ENDIF.\n053064 Z-35-2-287-ELSE.\n053066     IF HOLD-TDA-ACTVC-CODE = 0821\n053068         NEXT SENTENCE ELSE\n053070         GO TO Z-35-2-288-ELSE.\n053072     MOVE WS-CHG-WK-9-1 TO HOLD-TDAC-MAIL-CD.\n053074     GO TO Z-35-2-ENDIF.\n053076 Z-35-2-288-ELSE.\n053078     IF HOLD-TDA-ACTVC-CODE = 0822\n053080         NEXT SENTENCE ELSE\n053082         GO TO Z-35-2-289-ELSE.\n053084     MOVE WS-CHG-WK-9-1 TO HOLD-TDAC-ALIEN-CD.\n053086     GO TO Z-35-2-ENDIF.\n053088 Z-35-2-289-ELSE.\n053090     IF HOLD-TDA-ACTVC-CODE = 0823\n053092         NEXT SENTENCE ELSE\n053094         GO TO Z-35-2-290-ELSE.\n053096     MOVE WS-CHG-WK-9-3 TO HOLD-TDAC-BAR-CD.\n053098     GO TO Z-35-2-ENDIF.\n053100 Z-35-2-290-ELSE.\n053102     IF HOLD-TDA-ACTVC-CODE = 0824\n053104         NEXT SENTENCE ELSE\n053106         GO TO Z-35-2-291-ELSE.\n053108     MOVE WS-CHG-WK-X-1 TO HOLD-TDAC-EMP-CD.\n053110     GO TO Z-35-2-ENDIF.\n053112 Z-35-2-291-ELSE.\n053114     IF HOLD-TDA-ACTVC-CODE = 0825\n053116         NEXT SENTENCE ELSE\n053118         GO TO Z-35-2-292-ELSE.\n053120     MOVE WS-CHG-WK-9-4 TO HOLD-TDAC-BRCH.\n053122     GO TO Z-35-2-ENDIF.\n053124 Z-35-2-292-ELSE.\n053126     IF HOLD-TDA-ACTVC-CODE = 0826\n053128         NEXT SENTENCE ELSE\n053130         GO TO Z-35-2-293-ELSE.\n053132     MOVE WS-CHG-WK-X-20 TO HOLD-TDAC-SHT-NAME.\n053134     GO TO Z-35-2-ENDIF.\n053136 Z-35-2-293-ELSE.\n053138     IF HOLD-TDA-ACTVC-CODE = 0827\n053140         NEXT SENTENCE ELSE\n053142         GO TO Z-35-2-294-ELSE.\n053144     MOVE WS-CHG-WK-9-1 TO HOLD-TDAC-TIN-CERT-CD.\n053146     GO TO Z-35-2-ENDIF.\n053148 Z-35-2-294-ELSE.\n053150     IF HOLD-TDA-ACTVC-CODE = 0830\n053152         NEXT SENTENCE ELSE\n053154         GO TO Z-35-2-295-ELSE.\n053156     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-BAL.\n053158     GO TO Z-35-2-ENDIF.\n053160 Z-35-2-295-ELSE.\n053162     IF HOLD-TDA-ACTVC-CODE = 0831\n053164         NEXT SENTENCE ELSE\n053166         GO TO Z-35-2-296-ELSE.\n053168     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-PENLTY.\n053170     GO TO Z-35-2-ENDIF.\n053172 Z-35-2-296-ELSE.\n053174     IF HOLD-TDA-ACTVC-CODE = 0832\n053176         NEXT SENTENCE ELSE\n053178         GO TO Z-35-2-297-ELSE.\n053180     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-WTHLD.\n053182     GO TO Z-35-2-ENDIF.\n053184 Z-35-2-297-ELSE.\n053186     IF HOLD-TDA-ACTVC-CODE = 0833\n053188         NEXT SENTENCE ELSE\n053190         GO TO Z-35-2-298-ELSE.\n053192     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-INT.\n053194     GO TO Z-35-2-ENDIF.\n053196 Z-35-2-298-ELSE.\n053198     IF HOLD-TDA-ACTVC-CODE = 0834\n053200         NEXT SENTENCE ELSE\n053202         GO TO Z-35-2-299-ELSE.\n053204     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-CONTR.\n053206     GO TO Z-35-2-ENDIF.\n053208 Z-35-2-299-ELSE.\n053210     IF HOLD-TDA-ACTVC-CODE = 0835\n053212         NEXT SENTENCE ELSE\n053214         GO TO Z-35-2-300-ELSE.\n053216     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-CONTR-LY.\n053218     GO TO Z-35-2-ENDIF.\n053220 Z-35-2-300-ELSE.\n053222     IF HOLD-TDA-ACTVC-CODE = 0836\n053224         NEXT SENTENCE ELSE\n053226         GO TO Z-35-2-301-ELSE.\n053228     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-DISTR.\n053230     GO TO Z-35-2-ENDIF.\n053232 Z-35-2-301-ELSE.\n053234     IF HOLD-TDA-ACTVC-CODE = 0837\n053236         NEXT SENTENCE ELSE\n053238         GO TO Z-35-2-302-ELSE.\n053240     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-DISTR-LY.\n053242     GO TO Z-35-2-ENDIF.\n053244 Z-35-2-302-ELSE.\n053246     IF HOLD-TDA-ACTVC-CODE = 0838\n053248         NEXT SENTENCE ELSE\n053250         GO TO Z-35-2-303-ELSE.\n053252     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-ROLLOVER.\n053254     GO TO Z-35-2-ENDIF.\n053256 Z-35-2-303-ELSE.\n053258     IF HOLD-TDA-ACTVC-CODE = 0839\n053260         NEXT SENTENCE ELSE\n053262         GO TO Z-35-2-304-ELSE.\n053264     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-TRF-IN.\n053266     GO TO Z-35-2-ENDIF.\n053268 Z-35-2-304-ELSE.\n053270     IF HOLD-TDA-ACTVC-CODE = 0840\n053272         NEXT SENTENCE ELSE\n053274         GO TO Z-35-2-305-ELSE.\n053276     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-TRF-OUT.\n053278     GO TO Z-35-2-ENDIF.\n053280 Z-35-2-305-ELSE.\n053282     IF HOLD-TDA-ACTVC-CODE = 0842\n053284         NEXT SENTENCE ELSE\n053286         GO TO Z-35-2-306-ELSE.\n053288     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-ST-WHLD.\n053290     GO TO Z-35-2-ENDIF.\n053292 Z-35-2-306-ELSE.\n053294     IF HOLD-TDA-ACTVC-CODE = 0843\n053296         NEXT SENTENCE ELSE\n053298         GO TO Z-35-2-307-ELSE.\n053300     MOVE WS-CHG-WK-9-1 TO HOLD-TDAC-INQ-SECR-CD.\n053302     GO TO Z-35-2-ENDIF.\n053304 Z-35-2-307-ELSE.\n053306     IF HOLD-TDA-ACTVC-CODE = 0845\n053308         NEXT SENTENCE ELSE\n053310         GO TO Z-35-2-308-ELSE.\n053312     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-CD-BAL.\n053314     GO TO Z-35-2-ENDIF.\n053316 Z-35-2-308-ELSE.\n053318     IF HOLD-TDA-ACTVC-CODE = 0846\n053320         NEXT SENTENCE ELSE\n053322         GO TO Z-35-2-309-ELSE.\n053324     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-CD-PENLTY.\n053326     GO TO Z-35-2-ENDIF.\n053328 Z-35-2-309-ELSE.\n053330     IF HOLD-TDA-ACTVC-CODE = 0847\n053332         NEXT SENTENCE ELSE\n053334         GO TO Z-35-2-310-ELSE.\n053336     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-CD-WTHLD.\n053338     GO TO Z-35-2-ENDIF.\n053340 Z-35-2-310-ELSE.\n053342     IF HOLD-TDA-ACTVC-CODE = 0848\n053344         NEXT SENTENCE ELSE\n053346         GO TO Z-35-2-311-ELSE.\n053348     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-CD-INT.\n053350     GO TO Z-35-2-ENDIF.\n053352 Z-35-2-311-ELSE.\n053354     IF HOLD-TDA-ACTVC-CODE = 0849\n053356         NEXT SENTENCE ELSE\n053358         GO TO Z-35-2-312-ELSE.\n053360     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-CD-OID-INT.\n053362     GO TO Z-35-2-ENDIF.\n053364 Z-35-2-312-ELSE.\n053366     IF HOLD-TDA-ACTVC-CODE = 0850\n053368         NEXT SENTENCE ELSE\n053370         GO TO Z-35-2-313-ELSE.\n053372     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-CD-ST-WHLD.\n053374     GO TO Z-35-2-ENDIF.\n053376 Z-35-2-313-ELSE.\n053378     IF HOLD-TDA-ACTVC-CODE = 0851\n053380         NEXT SENTENCE ELSE\n053382         GO TO Z-35-2-314-ELSE.\n053384     MOVE WS-CHG-WK-X-1 TO HOLD-TDAC-BK-DEF-CD1.\n053386     GO TO Z-35-2-ENDIF.\n053388 Z-35-2-314-ELSE.\n053390     IF HOLD-TDA-ACTVC-CODE = 0852\n053392         NEXT SENTENCE ELSE\n053394         GO TO Z-35-2-315-ELSE.\n053396     MOVE WS-CHG-WK-X-1 TO HOLD-TDAC-BK-DEF-CD2.\n053398     GO TO Z-35-2-ENDIF.\n053400 Z-35-2-315-ELSE.\n053402     IF HOLD-TDA-ACTVC-CODE = 0853\n053404         NEXT SENTENCE ELSE\n053406         GO TO Z-35-2-316-ELSE.\n053408     MOVE WS-CHG-WK-X-1 TO HOLD-TDAC-BK-DEF-CD3.\n053410     GO TO Z-35-2-ENDIF.\n053412 Z-35-2-316-ELSE.\n053414     IF HOLD-TDA-ACTVC-CODE = 0854\n053416         NEXT SENTENCE ELSE\n053418         GO TO Z-35-2-317-ELSE.\n053420     MOVE WS-CHG-WK-X-1 TO HOLD-TDAC-BK-DEF-CD4.\n053422     GO TO Z-35-2-ENDIF.\n053424 Z-35-2-317-ELSE.\n053426     IF HOLD-TDA-ACTVC-CODE = 0855\n053428         NEXT SENTENCE ELSE\n053430         GO TO Z-35-2-318-ELSE.\n053432     MOVE WS-CHG-WK-X-1 TO HOLD-TDAC-BK-DEF-CD5.\n053434     GO TO Z-35-2-ENDIF.\n053436 Z-35-2-318-ELSE.\n053438     IF HOLD-TDA-ACTVC-CODE = 0857\n053440         NEXT SENTENCE ELSE\n053442         GO TO Z-35-2-319-ELSE.\n053444     MOVE WS-CHG-WK-X-3 TO HOLD-TDAC-TICKLER-FLAG.\n053446     GO TO Z-35-2-ENDIF.\n053448 Z-35-2-319-ELSE.\n053450     IF HOLD-TDA-ACTVC-CODE = 0863\n053452         NEXT SENTENCE ELSE\n053454         GO TO Z-35-2-320-ELSE.\n053456     MOVE WS-CHG-WK-9-S15V2 TO HOLD-TDAC-RMD-YR-AMT.\n053458     GO TO Z-35-2-ENDIF.\n053460 Z-35-2-320-ELSE.\n053462     IF HOLD-TDA-ACTVC-CODE = 0913\n053464         NEXT SENTENCE ELSE\n053466         GO TO Z-35-2-321-ELSE.\n053468     MOVE WS-CHG-WK-9-8 TO HOLD-TDAC-OPEN-DT.\n053470     GO TO Z-35-2-ENDIF.\n053472 Z-35-2-321-ELSE.\n053474     IF HOLD-TDA-ACTVC-CODE = 0915\n053476         NEXT SENTENCE ELSE\n053478         GO TO Z-35-2-322-ELSE.\n053480     MOVE WS-CHG-WK-9-8 TO HOLD-TDAC-LST-CONTACT.\n053482     GO TO Z-35-2-ENDIF.\n053484 Z-35-2-322-ELSE.\n053486     IF HOLD-TDA-ACTVC-CODE = 0920\n053488         NEXT SENTENCE ELSE\n053490         GO TO Z-35-2-323-ELSE.\n053492     MOVE WS-CHG-WK-9-8 TO HOLD-TDAC-BIRTH-DT.\n053494     GO TO Z-35-2-ENDIF.\n053496 Z-35-2-323-ELSE.\n053498     IF HOLD-TDA-ACTVC-CODE = 0921\n053500         NEXT SENTENCE ELSE\n053502         GO TO Z-35-2-324-ELSE.\n053504     MOVE WS-CHG-WK-9-8 TO HOLD-TDAC-DEATH-DT.\n053506 Z-35-2-324-ELSE.\n053508 Z-35-2-ENDIF.\n053510     IF Z-EDIT-ERROR\n053512         GO TO Z-35-XIT.\n053514 Z-35-SKIP.\n053516 Z-35-XIT.\n053518     EXIT.\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    240 lines from 26516 to 26755.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 55, "total_chunks": 55, "start_line": 26516, "end_line": 26755, "line_count": 240}

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
- Source code length: 13816 characters

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
CHUNK 55 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 26516 to 26755 (240 lines)
Chunk Tokens (estimated): ~3,563
Actual Input Tokens: 4,969 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 26516-26755 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 55 of 55 chunks
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
      The source code below is only CHUNK 55 of 55.


=============================================================================
CHUNK 55 SOURCE CODE (Lines 26516-26755)
=============================================================================

```cobol
053040 Z-35-2-285-ELSE.
053042     IF HOLD-TDA-ACTVC-CODE = 0819
053044         NEXT SENTENCE ELSE
053046         GO TO Z-35-2-286-ELSE.
053048     MOVE WS-CHG-WK-X-3 TO HOLD-TDAC-OFFICER.
053050     GO TO Z-35-2-ENDIF.
053052 Z-35-2-286-ELSE.
053054     IF HOLD-TDA-ACTVC-CODE = 0820
053056         NEXT SENTENCE ELSE
053058         GO TO Z-35-2-287-ELSE.
053060     MOVE WS-CHG-WK-X-1 TO HOLD-TDAC-TIN-CD.
053062     GO TO Z-35-2-ENDIF.
053064 Z-35-2-287-ELSE.
053066     IF HOLD-TDA-ACTVC-CODE = 0821
053068         NEXT SENTENCE ELSE
053070         GO TO Z-35-2-288-ELSE.
053072     MOVE WS-CHG-WK-9-1 TO HOLD-TDAC-MAIL-CD.
053074     GO TO Z-35-2-ENDIF.
053076 Z-35-2-288-ELSE.
053078     IF HOLD-TDA-ACTVC-CODE = 0822
053080         NEXT SENTENCE ELSE
053082         GO TO Z-35-2-289-ELSE.
053084     MOVE WS-CHG-WK-9-1 TO HOLD-TDAC-ALIEN-CD.
053086     GO TO Z-35-2-ENDIF.
053088 Z-35-2-289-ELSE.
053090     IF HOLD-TDA-ACTVC-CODE = 0823
053092         NEXT SENTENCE ELSE
053094         GO TO Z-35-2-290-ELSE.
053096     MOVE WS-CHG-WK-9-3 TO HOLD-TDAC-BAR-CD.
053098     GO TO Z-35-2-ENDIF.
053100 Z-35-2-290-ELSE.
053102     IF HOLD-TDA-ACTVC-CODE = 0824
053104         NEXT SENTENCE ELSE
053106         GO TO Z-35-2-291-ELSE.
053108     MOVE WS-CHG-WK-X-1 TO HOLD-TDAC-EMP-CD.
053110     GO TO Z-35-2-ENDIF.
053112 Z-35-2-291-ELSE.
053114     IF HOLD-TDA-ACTVC-CODE = 0825
053116         NEXT SENTENCE ELSE
053118         GO TO Z-35-2-292-ELSE.
053120     MOVE WS-CHG-WK-9-4 TO HOLD-TDAC-BRCH.
053122     GO TO Z-35-2-ENDIF.
053124 Z-35-2-292-ELSE.
053126     IF HOLD-TDA-ACTVC-CODE = 0826
053128         NEXT SENTENCE ELSE
053130         GO TO Z-35-2-293-ELSE.
053132     MOVE WS-CHG-WK-X-20 TO HOLD-TDAC-SHT-NAME.
053134     GO TO Z-35-2-ENDIF.
053136 Z-35-2-293-ELSE.
053138     IF HOLD-TDA-ACTVC-CODE = 0827
053140         NEXT SENTENCE ELSE
053142         GO TO Z-35-2-294-ELSE.
053144     MOVE WS-CHG-WK-9-1 TO HOLD-TDAC-TIN-CERT-CD.
053146     GO TO Z-35-2-ENDIF.
053148 Z-35-2-294-ELSE.
053150     IF HOLD-TDA-ACTVC-CODE = 0830
053152         NEXT SENTENCE ELSE
053154         GO TO Z-35-2-295-ELSE.
053156     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-BAL.
053158     GO TO Z-35-2-ENDIF.
053160 Z-35-2-295-ELSE.
053162     IF HOLD-TDA-ACTVC-CODE = 0831
053164         NEXT SENTENCE ELSE
053166         GO TO Z-35-2-296-ELSE.
053168     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-PENLTY.
053170     GO TO Z-35-2-ENDIF.
053172 Z-35-2-296-ELSE.
053174     IF HOLD-TDA-ACTVC-CODE = 0832
053176         NEXT SENTENCE ELSE
053178         GO TO Z-35-2-297-ELSE.
053180     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-WTHLD.
053182     GO TO Z-35-2-ENDIF.
053184 Z-35-2-297-ELSE.
053186     IF HOLD-TDA-ACTVC-CODE = 0833
053188         NEXT SENTENCE ELSE
053190         GO TO Z-35-2-298-ELSE.
053192     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-INT.
053194     GO TO Z-35-2-ENDIF.
053196 Z-35-2-298-ELSE.
053198     IF HOLD-TDA-ACTVC-CODE = 0834
053200         NEXT SENTENCE ELSE
053202         GO TO Z-35-2-299-ELSE.
053204     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-CONTR.
053206     GO TO Z-35-2-ENDIF.
053208 Z-35-2-299-ELSE.
053210     IF HOLD-TDA-ACTVC-CODE = 0835
053212         NEXT SENTENCE ELSE
053214         GO TO Z-35-2-300-ELSE.
053216     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-CONTR-LY.
053218     GO TO Z-35-2-ENDIF.
053220 Z-35-2-300-ELSE.
053222     IF HOLD-TDA-ACTVC-CODE = 0836
053224         NEXT SENTENCE ELSE
053226         GO TO Z-35-2-301-ELSE.
053228     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-DISTR.
053230     GO TO Z-35-2-ENDIF.
053232 Z-35-2-301-ELSE.
053234     IF HOLD-TDA-ACTVC-CODE = 0837
053236         NEXT SENTENCE ELSE
053238         GO TO Z-35-2-302-ELSE.
053240     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-DISTR-LY.
053242     GO TO Z-35-2-ENDIF.
053244 Z-35-2-302-ELSE.
053246     IF HOLD-TDA-ACTVC-CODE = 0838
053248         NEXT SENTENCE ELSE
053250         GO TO Z-35-2-303-ELSE.
053252     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-ROLLOVER.
053254     GO TO Z-35-2-ENDIF.
053256 Z-35-2-303-ELSE.
053258     IF HOLD-TDA-ACTVC-CODE = 0839
053260         NEXT SENTENCE ELSE
053262         GO TO Z-35-2-304-ELSE.
053264     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-TRF-IN.
053266     GO TO Z-35-2-ENDIF.
053268 Z-35-2-304-ELSE.
053270     IF HOLD-TDA-ACTVC-CODE = 0840
053272         NEXT SENTENCE ELSE
053274         GO TO Z-35-2-305-ELSE.
053276     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-TRF-OUT.
053278     GO TO Z-35-2-ENDIF.
053280 Z-35-2-305-ELSE.
053282     IF HOLD-TDA-ACTVC-CODE = 0842
053284         NEXT SENTENCE ELSE
053286         GO TO Z-35-2-306-ELSE.
053288     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-IRA-ST-WHLD.
053290     GO TO Z-35-2-ENDIF.
053292 Z-35-2-306-ELSE.
053294     IF HOLD-TDA-ACTVC-CODE = 0843
053296         NEXT SENTENCE ELSE
053298         GO TO Z-35-2-307-ELSE.
053300     MOVE WS-CHG-WK-9-1 TO HOLD-TDAC-INQ-SECR-CD.
053302     GO TO Z-35-2-ENDIF.
053304 Z-35-2-307-ELSE.
053306     IF HOLD-TDA-ACTVC-CODE = 0845
053308         NEXT SENTENCE ELSE
053310         GO TO Z-35-2-308-ELSE.
053312     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-CD-BAL.
053314     GO TO Z-35-2-ENDIF.
053316 Z-35-2-308-ELSE.
053318     IF HOLD-TDA-ACTVC-CODE = 0846
053320         NEXT SENTENCE ELSE
053322         GO TO Z-35-2-309-ELSE.
053324     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-CD-PENLTY.
053326     GO TO Z-35-2-ENDIF.
053328 Z-35-2-309-ELSE.
053330     IF HOLD-TDA-ACTVC-CODE = 0847
053332         NEXT SENTENCE ELSE
053334         GO TO Z-35-2-310-ELSE.
053336     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-CD-WTHLD.
053338     GO TO Z-35-2-ENDIF.
053340 Z-35-2-310-ELSE.
053342     IF HOLD-TDA-ACTVC-CODE = 0848
053344         NEXT SENTENCE ELSE
053346         GO TO Z-35-2-311-ELSE.
053348     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-CD-INT.
053350     GO TO Z-35-2-ENDIF.
053352 Z-35-2-311-ELSE.
053354     IF HOLD-TDA-ACTVC-CODE = 0849
053356         NEXT SENTENCE ELSE
053358         GO TO Z-35-2-312-ELSE.
053360     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-CD-OID-INT.
053362     GO TO Z-35-2-ENDIF.
053364 Z-35-2-312-ELSE.
053366     IF HOLD-TDA-ACTVC-CODE = 0850
053368         NEXT SENTENCE ELSE
053370         GO TO Z-35-2-313-ELSE.
053372     MOVE WS-CHG-WK-9-S13V2 TO HOLD-TDAC-CD-ST-WHLD.
053374     GO TO Z-35-2-ENDIF.
053376 Z-35-2-313-ELSE.
053378     IF HOLD-TDA-ACTVC-CODE = 0851
053380         NEXT SENTENCE ELSE
053382         GO TO Z-35-2-314-ELSE.
053384     MOVE WS-CHG-WK-X-1 TO HOLD-TDAC-BK-DEF-CD1.
053386     GO TO Z-35-2-ENDIF.
053388 Z-35-2-314-ELSE.
053390     IF HOLD-TDA-ACTVC-CODE = 0852
053392         NEXT SENTENCE ELSE
053394         GO TO Z-35-2-315-ELSE.
053396     MOVE WS-CHG-WK-X-1 TO HOLD-TDAC-BK-DEF-CD2.
053398     GO TO Z-35-2-ENDIF.
053400 Z-35-2-315-ELSE.
053402     IF HOLD-TDA-ACTVC-CODE = 0853
053404         NEXT SENTENCE ELSE
053406         GO TO Z-35-2-316-ELSE.
053408     MOVE WS-CHG-WK-X-1 TO HOLD-TDAC-BK-DEF-CD3.
053410     GO TO Z-35-2-ENDIF.
053412 Z-35-2-316-ELSE.
053414     IF HOLD-TDA-ACTVC-CODE = 0854
053416         NEXT SENTENCE ELSE
053418         GO TO Z-35-2-317-ELSE.
053420     MOVE WS-CHG-WK-X-1 TO HOLD-TDAC-BK-DEF-CD4.
053422     GO TO Z-35-2-ENDIF.
053424 Z-35-2-317-ELSE.
053426     IF HOLD-TDA-ACTVC-CODE = 0855
053428         NEXT SENTENCE ELSE
053430         GO TO Z-35-2-318-ELSE.
053432     MOVE WS-CHG-WK-X-1 TO HOLD-TDAC-BK-DEF-CD5.
053434     GO TO Z-35-2-ENDIF.
053436 Z-35-2-318-ELSE.
053438     IF HOLD-TDA-ACTVC-CODE = 0857
053440         NEXT SENTENCE ELSE
053442         GO TO Z-35-2-319-ELSE.
053444     MOVE WS-CHG-WK-X-3 TO HOLD-TDAC-TICKLER-FLAG.
053446     GO TO Z-35-2-ENDIF.
053448 Z-35-2-319-ELSE.
053450     IF HOLD-TDA-ACTVC-CODE = 0863
053452         NEXT SENTENCE ELSE
053454         GO TO Z-35-2-320-ELSE.
053456     MOVE WS-CHG-WK-9-S15V2 TO HOLD-TDAC-RMD-YR-AMT.
053458     GO TO Z-35-2-ENDIF.
053460 Z-35-2-320-ELSE.
053462     IF HOLD-TDA-ACTVC-CODE = 0913
053464         NEXT SENTENCE ELSE
053466         GO TO Z-35-2-321-ELSE.
053468     MOVE WS-CHG-WK-9-8 TO HOLD-TDAC-OPEN-DT.
053470     GO TO Z-35-2-ENDIF.
053472 Z-35-2-321-ELSE.
053474     IF HOLD-TDA-ACTVC-CODE = 0915
053476         NEXT SENTENCE ELSE
053478         GO TO Z-35-2-322-ELSE.
053480     MOVE WS-CHG-WK-9-8 TO HOLD-TDAC-LST-CONTACT.
053482     GO TO Z-35-2-ENDIF.
053484 Z-35-2-322-ELSE.
053486     IF HOLD-TDA-ACTVC-CODE = 0920
053488         NEXT SENTENCE ELSE
053490         GO TO Z-35-2-323-ELSE.
053492     MOVE WS-CHG-WK-9-8 TO HOLD-TDAC-BIRTH-DT.
053494     GO TO Z-35-2-ENDIF.
053496 Z-35-2-323-ELSE.
053498     IF HOLD-TDA-ACTVC-CODE = 0921
053500         NEXT SENTENCE ELSE
053502         GO TO Z-35-2-324-ELSE.
053504     MOVE WS-CHG-WK-9-8 TO HOLD-TDAC-DEATH-DT.
053506 Z-35-2-324-ELSE.
053508 Z-35-2-ENDIF.
053510     IF Z-EDIT-ERROR
053512         GO TO Z-35-XIT.
053514 Z-35-SKIP.
053516 Z-35-XIT.
053518     EXIT.
```

⚠️  This is the source code you must document.
    240 lines from 26516 to 26755.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

