# LLM Request Debug File
Generated: 2025-11-14T19:07:48.625129

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 34/55
- **Model**: gpt-4.1
- **Chunk Number**: 34
- **Pass Number**: 3
- **Attempt Number**: 2 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~7,703 tokens
- **Total Input**: ~9,661 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 34/55" (ID: detailed-code-explanation)

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


**CHUNK 34 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-14T17:36:35.036798", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 34 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 16331 to 16896 (566 lines)\nChunk Tokens (estimated): ~7,990\nActual Input Tokens: 9,396 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 16331-16896 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 34 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 34 of 55.\n\n\n=============================================================================\nCHUNK 34 SOURCE CODE (Lines 16331-16896)\n=============================================================================\n\n```cobol\n032670 Z-20-29-2-ELSE.\n032672     IF H-REPORT-NO = \"TDA-053\"\n032674         NEXT SENTENCE ELSE\n032676         GO TO Z-20-29-3-ELSE.\n032678     MOVE \"053\" TO GWS-RMT-EXT.\n032680     GO TO Z-20-29-ENDIF.\n032682 Z-20-29-3-ELSE.\n032684     IF H-REPORT-NO = \"TDA-700\"\n032686         NEXT SENTENCE ELSE\n032688         GO TO Z-20-29-4-ELSE.\n032690     MOVE \"700\" TO GWS-RMT-EXT.\n032692 Z-20-29-4-ELSE.\n032694 Z-20-29-ENDIF.\n032696     IF TDB-TDAPC-COPIES > 1\n032698         NEXT SENTENCE ELSE\n032700         GO TO Z-20-34-1-ELSE.\n032702     MOVE TDB-TDAPC-COPIES TO GWS-NO-PARTS.\n032704     IF TDB-TDAPC-FICHE-PRT > 0\n032706         NEXT SENTENCE\n032708     ELSE\n032710         GO TO Z-20-36-END-MOVE.\n032712     MOVE \"1\" TO GWS-MICROFICHE-CODE.\n032714 Z-20-36-END-MOVE.\n032716 Z-20-34-1-ELSE.\n032718     IF TDB-TDAPC-FICHE-PRT > 0\n032720         NEXT SENTENCE ELSE\n032722         GO TO Z-20-37-1-ELSE.\n032724     COMPUTE Z-GSTRNUM-1-9 = 1 + TDB-TDAPC-FICHE-PRT.\n032726     MOVE Z-GSTRNUM-1 TO GWS-MICROFICHE-CODE.\n032728 Z-20-37-1-ELSE.\n032730        PERFORM 99-PRT-LABEL-CHECK.                               \n032732     IF ( WS-SYS-HOST = \"CSIA\" ) OR ( WS-SYS-HOST = \"CSID\" ) OR ( \n032734         WS-SYS-HOST = \"CSIB\" )\n032736         NEXT SENTENCE ELSE\n032738         GO TO Z-20-39-1-ELSE.\n032740     MOVE ID-PRT74-2 TO WS-LISTING-NAME.\n032742     DISPLAY \"WS-LISTING-NAME -> \", WS-LISTING-NAME.\n032744     MOVE WS-LISTING-NAME TO Z-LALPHA-1.\n032746     MOVE SPACES TO Z-LALPHA-2.\n032748     MOVE \" ON\" TO Z-LALPHA-3.\n032750     MOVE 40 TO Z-GINT-1.\n032752     MOVE 0 TO Z-LINT-1.\n032754     MOVE 3 TO Z-LINT-2.\n032756     MOVE SPACES TO Z-GALPHA-1.\n032758     CALL \"XSTRPAT OF XGEN/RUNTIME/LIBRARY\" USING Z-GALPHA-1,     \n032760         Z-LALPHA-1, Z-LALPHA-2, Z-LALPHA-3, Z-GINT-1,            \n032762         Z-STR-INT-ZERO, Z-LINT-1, Z-STR-INT-ONE, Z-LINT-2,       \n032764         Z-STR-INT-ONE.\n032766     IF Z-GINT-1 < 1\n032768         MOVE 1 TO Z-GINT-1.\n032770     MOVE Z-GALPHA-1 TO WS-LISTING-NAME.\n032772     MOVE \".\" TO Z-LALPHA-1.\n032774     MOVE 40 TO Z-GINT-1.\n032776     MOVE 1 TO Z-LINT-1.\n032778     MOVE WS-LISTING-NAME TO Z-GALPHA-1.\n032780     CALL \"XSTRCAT OF XGEN/RUNTIME/LIBRARY\" USING Z-GALPHA-1,     \n032782         Z-STR-INT-ZERO, Z-LALPHA-1, Z-GINT-1, Z-STR-INT-ZERO,    \n032784         Z-LINT-1.\n032786     IF Z-GINT-1 < 1\n032788         MOVE 1 TO Z-GINT-1.\n032790     MOVE Z-GALPHA-1 TO WS-LISTING-NAME.\n032792     GO TO Z-20-39-ENDIF.\n032794 Z-20-39-1-ELSE.\n032796     MOVE ID-PRT74-2 TO ID-PRINT-NAME-NT.\n032798            INSPECT ID-PRINT-NAME-NT REPLACING ALL \"/\" BY \"_\".    \n032800     MOVE ID-PRINT-FILES-NT TO WS-LISTING-NAME.\n032802     DISPLAY \"WS-LISTING-NAME -> \", WS-LISTING-NAME.\n032804 Z-20-39-ENDIF.\n032806        PERFORM 999999-CHANGE1.                                   \n032808        PERFORM 999999-CHANGE24.                                  \n032810     MOVE 1 TO PRT-LIST-FILE-STATUS.\n032812     MOVE BANK-CSI-BR-CODE TO H-CSI-BR-NO.\n032814     MOVE BANK-NO TO H-BANK-NO-9.\n032816     MOVE BANK-NAME TO H-BANK-NAME.\n032818     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.\n032820     MOVE Z-DATE2-MM TO Z-DATE3-MM.\n032822     MOVE Z-DATE2-DD TO Z-DATE3-DD.\n032824     MOVE Z-DATE2-YY TO Z-DATE3-YY.\n032826     MOVE Z-DATE3-FORMAT-9 TO H-DATE.\n032828*    RETRIEVE TODAY'S DATE\n032830     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n032832          USING Z-CALL-CURRENTDATE.\n032834     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n032836     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n032838     ACCEPT Z-DATE0-TIME   FROM TIME.\n032840     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.\n032842     MOVE Z-DATE0-UU TO Z-DATE4-UU.\n032844     MOVE Z-DATE4-FORMAT-9 TO H-CSI-HHMM.\n032846*    RETRIEVE TODAY'S DATE\n032848     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n032850          USING Z-CALL-CURRENTDATE.\n032852     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n032854     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n032856     ACCEPT Z-DATE0-TIME   FROM TIME.\n032858     MOVE Z-DATE0-DD TO Z-DATE5-DD.\n032860     MOVE Z-DATE5-FORMAT-9 TO H-CSI-DD.\n032862     IF H-REPORT-NO = \"TD-4920\"\n032864         NEXT SENTENCE ELSE\n032866         GO TO Z-20-54-1-ELSE.\n032868     MOVE \"TDA ZIP+4 FILE MAINTENANCE\" TO H-RPT-TITLE.\n032870     GO TO Z-20-54-ENDIF.\n032872 Z-20-54-1-ELSE.\n032874     IF H-REPORT-NO = \"TDA-054\"\n032876         NEXT SENTENCE ELSE\n032878         GO TO Z-20-54-2-ELSE.\n032880     MOVE \"CLOSED COD HISTORY REPORT\" TO H-RPT-TITLE.\n032882     GO TO Z-20-54-ENDIF.\n032884 Z-20-54-2-ELSE.\n032886     IF H-REPORT-NO = \"TDA-700\"\n032888         NEXT SENTENCE ELSE\n032890         GO TO Z-20-54-3-ELSE.\n032892     MOVE \"RMD CALCULATION REPORT\" TO H-RPT-TITLE.\n032894     GO TO Z-20-54-ENDIF.\n032896 Z-20-54-3-ELSE.\n032898     MOVE \"TIME DEPOSIT EXCEPTIONS\" TO H-REPORT-TITLE.\n032900     MOVE \"TD-000 \" TO H-REPORT-NO.\n032902 Z-20-54-ENDIF.\n032904     MOVE 1 TO HDR-CTL.\n032906********IF  H-REPORT-NO NOT = \"TD-4920\"                           \n032908     IF ( GWS-PRT-NEW = 1 )\n032910         NEXT SENTENCE ELSE\n032912         GO TO Z-20-61-1-ELSE.\n032914                PERFORM 999999-CHANGE54.                          \n032916                PERFORM 999999-CHANGE34.                          \n032918     GO TO Z-20-61-ENDIF.\n032920 Z-20-61-1-ELSE.\n032922                PERFORM 999999-CHANGE55.                          \n032924 Z-20-61-ENDIF.\n032926********ENDIF.                                                    \n032928*\n032930******* OPEN REPORT LISTING\n032932*\n032934     IF  Z-RPTINFO1-OPEN = 0\n032936         OPEN OUTPUT LISTING \n032938         MOVE ZEROS TO Z-RPT-1-PAGE\n032940         MOVE ZEROS TO Z-RPT-1-LINE\n032942         MOVE ZEROS TO Z-RPT-1-TRAP\n032944         MOVE 3 TO Z-RPTINFO1-OPEN\n032946         MOVE 3 TO Z-RPTINFO1-RS-OPEN.\n032948     MOVE \"BK\" TO TP-LN-BANK.\n032950     MOVE PROC-BANK TO TP-LN-BKNO.\n032952     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.\n032954     MOVE Z-DATE2-MM TO Z-DATE3-MM.\n032956     MOVE Z-DATE2-DD TO Z-DATE3-DD.\n032958     MOVE Z-DATE2-YY TO Z-DATE3-YY.\n032960     MOVE Z-DATE3-FORMAT-9 TO TP-LN-DATE.\n032962     MOVE WS-TP-DLY-WKLY TO TP-LN3.\n032964     MOVE \"P\" TO WS-TEAR-PAGE-TYPE.\n032966     IF H-REPORT-NO NOT = \"TDA-041\"\n032968         NEXT SENTENCE ELSE\n032970         GO TO Z-20-68-1-ELSE.\n032972************ PERFORM TPR-TEAR-PAGES\n032974     PERFORM Z-21-PROCEDURE THRU Z-21-XIT.\n032976     IF  Z-EXIT-EDITEXIT\n032978         GO TO Z-20-XIT.\n032980     IF  Z-DMS2-ABORT-FLAG = 1\n032982         GO TO Z-20-XIT.\n032984     IF  Z-EXIT-LEVEL < 0\n032986         GO TO Z-20-END.\n032988*\n032990 Z-20-68-1-ELSE.\n032992 Z-20-27-1-ELSE.\n032994     IF FICHE-REQUEST AND PRT-FICHE-CLOSE\n032996         NEXT SENTENCE ELSE\n032998         GO TO Z-20-70-1-ELSE.\n033000     MOVE \"SP\" TO GWS-PRT-DESCRIPTOR.\n033002     MOVE 0 TO GWS-NO-PARTS.\n033004     COMPUTE Z-GSTRNUM-2-9 = 1 + TDB-TDAPC-FICHE-PRT.\n033006     MOVE Z-GSTRNUM-2 TO GWS-MICROFICHE-CODE.\n033008     IF H-REPORT-NO = \"TD-4720\"\n033010         NEXT SENTENCE ELSE\n033012         GO TO Z-20-74-1-ELSE.\n033014     MOVE \"472\" TO GWS-RMT-EXT.\n033016     GO TO Z-20-74-ENDIF.\n033018 Z-20-74-1-ELSE.\n033020     IF H-REPORT-NO = \"TDA-701\"\n033022         NEXT SENTENCE ELSE\n033024         GO TO Z-20-74-2-ELSE.\n033026     MOVE \"701\" TO GWS-RMT-EXT.\n033028     GO TO Z-20-74-ENDIF.\n033030 Z-20-74-2-ELSE.\n033032     MOVE \"950\" TO GWS-RMT-EXT.\n033034 Z-20-74-ENDIF.\n033036        PERFORM 99-PRT-LABEL-CHECK.                               \n033038     MOVE 0 TO WS-FICHE-RMT-PASS.\n033040     MOVE \"000\" TO GWS-RMT-EXT.\n033042     MOVE ID-PRT74-2 TO WS-FICHE-NAME.\n033044     MOVE ID-PRT74-2 TO ID-PRINT-NAME-NT.\n033046        INSPECT ID-PRINT-NAME-NT REPLACING ALL \"/\" BY \"_\".        \n033048     IF ( WS-SYS-HOST = \"CSIA\" ) OR ( WS-SYS-HOST = \"CSID\" ) OR ( \n033050         WS-SYS-HOST = \"CSIB\" )\n033052         NEXT SENTENCE ELSE\n033054         GO TO Z-20-82-1-ELSE.\n033056     DISPLAY \"WS-FICHE-NAME -> \", WS-FICHE-NAME.\n033058     MOVE WS-FICHE-NAME TO Z-LALPHA-1.\n033060     MOVE SPACES TO Z-LALPHA-2.\n033062     MOVE \" ON\" TO Z-LALPHA-3.\n033064     MOVE 40 TO Z-GINT-1.\n033066     MOVE 0 TO Z-LINT-1.\n033068     MOVE 3 TO Z-LINT-2.\n033070     MOVE SPACES TO Z-GALPHA-1.\n033072     CALL \"XSTRPAT OF XGEN/RUNTIME/LIBRARY\" USING Z-GALPHA-1,     \n033074         Z-LALPHA-1, Z-LALPHA-2, Z-LALPHA-3, Z-GINT-1,            \n033076         Z-STR-INT-ZERO, Z-LINT-1, Z-STR-INT-ONE, Z-LINT-2,       \n033078         Z-STR-INT-ONE.\n033080     IF Z-GINT-1 < 1\n033082         MOVE 1 TO Z-GINT-1.\n033084     MOVE Z-GALPHA-1 TO WS-FICHE-NAME.\n033086     MOVE \".\" TO Z-LALPHA-1.\n033088     MOVE 40 TO Z-GINT-1.\n033090     MOVE 1 TO Z-LINT-1.\n033092     MOVE WS-FICHE-NAME TO Z-GALPHA-1.\n033094     CALL \"XSTRCAT OF XGEN/RUNTIME/LIBRARY\" USING Z-GALPHA-1,     \n033096         Z-STR-INT-ZERO, Z-LALPHA-1, Z-GINT-1, Z-STR-INT-ZERO,    \n033098         Z-LINT-1.\n033100     IF Z-GINT-1 < 1\n033102         MOVE 1 TO Z-GINT-1.\n033104     MOVE Z-GALPHA-1 TO WS-FICHE-NAME.\n033106     GO TO Z-20-82-ENDIF.\n033108 Z-20-82-1-ELSE.\n033110     MOVE ID-PRINT-FILES-NT TO WS-FICHE-NAME.\n033112     DISPLAY \"WS-FICHE-NAME -> \", WS-FICHE-NAME.\n033114 Z-20-82-ENDIF.\n033116        PERFORM 999999-CHANGE22.                                  \n033118        PERFORM 999999-CHANGE33.                                  \n033120     MOVE 1 TO PRT-FICHE-FILE-STATUS.\n033122     MOVE BANK-CSI-BR-CODE TO H-CSI-BR-NO.\n033124     MOVE BANK-NO TO H-BANK-NO-9.\n033126     MOVE BANK-NAME TO H-BANK-NAME.\n033128     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.\n033130     MOVE Z-DATE2-MM TO Z-DATE3-MM.\n033132     MOVE Z-DATE2-DD TO Z-DATE3-DD.\n033134     MOVE Z-DATE2-YY TO Z-DATE3-YY.\n033136     MOVE Z-DATE3-FORMAT-9 TO H-DATE.\n033138*    RETRIEVE TODAY'S DATE\n033140     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n033142          USING Z-CALL-CURRENTDATE.\n033144     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n033146     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n033148     ACCEPT Z-DATE0-TIME   FROM TIME.\n033150     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.\n033152     MOVE Z-DATE0-UU TO Z-DATE4-UU.\n033154     MOVE Z-DATE4-FORMAT-9 TO H-CSI-HHMM.\n033156*    RETRIEVE TODAY'S DATE\n033158     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n033160          USING Z-CALL-CURRENTDATE.\n033162     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n033164     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n033166     ACCEPT Z-DATE0-TIME   FROM TIME.\n033168     MOVE Z-DATE0-DD TO Z-DATE5-DD.\n033170     MOVE Z-DATE5-FORMAT-9 TO H-CSI-DD.\n033172     IF H-REPORT-NO = \"TD-4720\"\n033174         NEXT SENTENCE ELSE\n033176         GO TO Z-20-95-1-ELSE.\n033178     MOVE \"TDA POSTAL ZIP+4 UNCHANGED\" TO H-RPT-TITLE.\n033180     GO TO Z-20-95-ENDIF.\n033182 Z-20-95-1-ELSE.\n033184     IF H-REPORT-NO = \"TDA-701\"\n033186         NEXT SENTENCE ELSE\n033188         GO TO Z-20-95-2-ELSE.\n033190     MOVE \"RMD CALCULATION REPORT FOR INHERITED IRA'S\" TO         \n033192         H-RPT-TITLE.\n033194     GO TO Z-20-95-ENDIF.\n033196 Z-20-95-2-ELSE.\n033198     MOVE \"TIME DEPOSIT EXCEPTIONS\" TO H-REPORT-TITLE.\n033200     MOVE \"TD-000 \" TO H-REPORT-NO.\n033202 Z-20-95-ENDIF.\n033204************ PERFORM HEADING-SETUP\n033206     PERFORM Z-16-PROCEDURE THRU Z-16-XIT.\n033208     IF  Z-EXIT-EDITEXIT\n033210         GO TO Z-20-XIT.\n033212     IF  Z-DMS2-ABORT-FLAG = 1\n033214         GO TO Z-20-XIT.\n033216     IF  Z-EXIT-LEVEL < 0\n033218         GO TO Z-20-END.\n033220*\n033222     MOVE 1 TO HDR-CTL.\n033224********IF  H-REPORT-NO NOT = \"TD-4720\"                           \n033226     IF ( GWS-PRT-NEW = 1 )\n033228         NEXT SENTENCE ELSE\n033230         GO TO Z-20-102-1-ELSE.\n033232           PERFORM 999999-CHANGE72.                               \n033234     IF ( WS-SYS-HOST = \"CSIB\" )\n033236         NEXT SENTENCE ELSE\n033238         GO TO Z-20-103-1-ELSE.\n033240              PERFORM 999999-CHANGE52.                            \n033242     GO TO Z-20-103-ENDIF.\n033244 Z-20-103-1-ELSE.\n033246              PERFORM 999999-CHANGE53.                            \n033248 Z-20-103-ENDIF.\n033250     GO TO Z-20-102-ENDIF.\n033252 Z-20-102-1-ELSE.\n033254           PERFORM 999999-CHANGE73.                               \n033256********ENDIF.                                                    \n033258 Z-20-102-ENDIF.\n033260*\n033262******* OPEN REPORT FICHE\n033264*\n033266     IF  Z-RPTINFO2-OPEN = 0\n033268         OPEN OUTPUT FICHE \n033270         MOVE ZEROS TO Z-RPT-2-PAGE\n033272         MOVE ZEROS TO Z-RPT-2-LINE\n033274         MOVE ZEROS TO Z-RPT-2-TRAP\n033276         MOVE 3 TO Z-RPTINFO2-OPEN\n033278         MOVE 3 TO Z-RPTINFO2-RS-OPEN.\n033280     MOVE \"BK\" TO TP-LN-BANK.\n033282     MOVE PROC-BANK TO TP-LN-BKNO.\n033284     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.\n033286     MOVE Z-DATE2-MM TO Z-DATE3-MM.\n033288     MOVE Z-DATE2-DD TO Z-DATE3-DD.\n033290     MOVE Z-DATE2-YY TO Z-DATE3-YY.\n033292     MOVE Z-DATE3-FORMAT-9 TO TP-LN-DATE.\n033294     MOVE WS-TP-DLY-WKLY TO TP-LN3.\n033296     MOVE \"F\" TO WS-TEAR-PAGE-TYPE.\n033298************ PERFORM TPR-TEAR-PAGES\n033300     PERFORM Z-21-PROCEDURE THRU Z-21-XIT.\n033302     IF  Z-EXIT-EDITEXIT\n033304         GO TO Z-20-XIT.\n033306     IF  Z-DMS2-ABORT-FLAG = 1\n033308         GO TO Z-20-XIT.\n033310     IF  Z-EXIT-LEVEL < 0\n033312         GO TO Z-20-END.\n033314*\n033316 Z-20-70-1-ELSE.\n033318     IF LIST-REQUEST AND TDB-TDAPC-RPT-NBR NOT = 651\n033320         NEXT SENTENCE ELSE\n033322         GO TO Z-20-111-1-ELSE.\n033324     MOVE ZEROS TO Z-RPT-1-PAGE.\n033326     MOVE 58 TO Z-RPT-1-LINE.\n033328 Z-20-111-1-ELSE.\n033330     IF FICHE-REQUEST\n033332         NEXT SENTENCE ELSE\n033334         GO TO Z-20-114-1-ELSE.\n033336     MOVE ZEROS TO Z-RPT-2-PAGE.\n033338     MOVE 58 TO Z-RPT-2-LINE.\n033340 Z-20-114-1-ELSE.\n033342 Z-20-END.\n033344     IF Z-EDIT-ERROR\n033346         GO TO Z-20-XIT.\n033348 Z-20-SKIP.\n033350     IF Z-EXIT-LEVEL NOT < 0\n033352         MOVE 0 TO Z-EXIT-CODE\n033354         MOVE 9999 TO Z-EXIT-LEVEL.\n033356 Z-20-XIT.\n033358     EXIT.\n033360*\n033362*****************************************************************\n033364*    PROCEDURE CLOSE-PRT-FILE\n033366*****************************************************************\n033368 Z-22-PROCEDURE.\n033370*\n033372     MOVE 0 TO Z-EXIT-CODE.\n033374     MOVE 9999 TO Z-EXIT-LEVEL.\n033376     IF PRT-LIST-OPEN\n033378         NEXT SENTENCE ELSE\n033380         GO TO Z-22-1-1-ELSE.\n033382     MOVE PROC-BANK TO TP-LN-BKNO.\n033384     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.\n033386     MOVE Z-DATE2-MM TO Z-DATE3-MM.\n033388     MOVE Z-DATE2-DD TO Z-DATE3-DD.\n033390     MOVE Z-DATE2-YY TO Z-DATE3-YY.\n033392     MOVE Z-DATE3-FORMAT-9 TO TP-LN-DATE.\n033394     MOVE WS-TP-DLY-WKLY TO TP-LN3.\n033396     MOVE 1 TO TP-SKIP.\n033398     MOVE \"P\" TO WS-TEAR-PAGE-TYPE.\n033400     MOVE BANK-CSI-BR-CODE TO H-CSI-BR-NO.\n033402     MOVE BANK-NO TO H-BANK-NO-9.\n033404     MOVE BANK-NAME TO H-BANK-NAME.\n033406     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.\n033408     MOVE Z-DATE2-MM TO Z-DATE3-MM.\n033410     MOVE Z-DATE2-DD TO Z-DATE3-DD.\n033412     MOVE Z-DATE2-YY TO Z-DATE3-YY.\n033414     MOVE Z-DATE3-FORMAT-9 TO H-DATE.\n033416*    RETRIEVE TODAY'S DATE\n033418     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n033420          USING Z-CALL-CURRENTDATE.\n033422     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n033424     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n033426     ACCEPT Z-DATE0-TIME   FROM TIME.\n033428     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.\n033430     MOVE Z-DATE0-UU TO Z-DATE4-UU.\n033432     MOVE Z-DATE4-FORMAT-9 TO H-CSI-HHMM.\n033434*    RETRIEVE TODAY'S DATE\n033436     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n033438          USING Z-CALL-CURRENTDATE.\n033440     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n033442     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n033444     ACCEPT Z-DATE0-TIME   FROM TIME.\n033446     MOVE Z-DATE0-DD TO Z-DATE5-DD.\n033448     MOVE Z-DATE5-FORMAT-9 TO H-CSI-DD.\n033450     IF H-REPORT-NO = \"TDA-054\"\n033452         NEXT SENTENCE ELSE\n033454         GO TO Z-22-13-1-ELSE.\n033456     MOVE \"CLOSED COD HISTORY REPORT\" TO H-RPT-TITLE.\n033458     GO TO Z-22-13-ENDIF.\n033460 Z-22-13-1-ELSE.\n033462     IF H-REPORT-NO = \"TD-4920\"\n033464         NEXT SENTENCE ELSE\n033466         GO TO Z-22-13-2-ELSE.\n033468     MOVE \"TDA ZIP+4 FILE MAINTENANCE\" TO H-RPT-TITLE.\n033470     MOVE 0 TO GWS-MICROFICHE-CODE.\n033472     MOVE \"Y\" TO WS-LIST-REQUEST.\n033474     MOVE \" \" TO WS-FICHE-REQUEST.\n033476     GO TO Z-22-13-ENDIF.\n033478 Z-22-13-2-ELSE.\n033480     IF H-REPORT-NO = \"TDA-700\"\n033482         NEXT SENTENCE ELSE\n033484         GO TO Z-22-13-3-ELSE.\n033486     MOVE \"RMD CALCULATION REPORT\" TO H-RPT-TITLE.\n033488     GO TO Z-22-13-ENDIF.\n033490 Z-22-13-3-ELSE.\n033492     MOVE \"TIME DEPOSIT EXCEPTIONS\" TO H-REPORT-TITLE.\n033494     MOVE \"TD-000 \" TO H-REPORT-NO.\n033496 Z-22-13-ENDIF.\n033498************ PERFORM HEADING-SETUP\n033500     PERFORM Z-16-PROCEDURE THRU Z-16-XIT.\n033502     IF  Z-EXIT-EDITEXIT\n033504         GO TO Z-22-XIT.\n033506     IF  Z-DMS2-ABORT-FLAG = 1\n033508         GO TO Z-22-XIT.\n033510     IF  Z-EXIT-LEVEL < 0\n033512         GO TO Z-22-END.\n033514*\n033516     MOVE 1 TO HDR-CTL.\n033518************ PERFORM TPR-TEAR-PAGES\n033520     PERFORM Z-21-PROCEDURE THRU Z-21-XIT.\n033522     IF  Z-EXIT-EDITEXIT\n033524         GO TO Z-22-XIT.\n033526     IF  Z-DMS2-ABORT-FLAG = 1\n033528         GO TO Z-22-XIT.\n033530     IF  Z-EXIT-LEVEL < 0\n033532         GO TO Z-22-END.\n033534*\n033536     MOVE 0 TO PRT-LIST-FILE-STATUS.\n033538*\n033540***********  CLOSE OF REPORT FILE  LISTING WITH CRUNCH\n033542*\n033544     IF  Z-RPTINFO1-OPEN NOT = 0\n033546         CLOSE LISTING WITH CRUNCH\n033548         MOVE 0 TO Z-RPTINFO1-OPEN\n033550         MOVE 0 TO Z-RPTINFO1-RS-OPEN.\n033552     IF GWS-PRT-NEW = 1\n033554         NEXT SENTENCE ELSE\n033556         GO TO Z-22-27-1-ELSE.\n033558               PERFORM 999999-CHANGE54.                           \n033560               PERFORM 999999-CHANGE34.                           \n033562     GO TO Z-22-27-ENDIF.\n033564 Z-22-27-1-ELSE.\n033566               PERFORM 999999-CHANGE55.                           \n033568 Z-22-27-ENDIF.\n033570 Z-22-1-1-ELSE.\n033572     IF PRT-FICHE-OPEN\n033574         NEXT SENTENCE ELSE\n033576         GO TO Z-22-28-1-ELSE.\n033578     MOVE PROC-BANK TO TP-LN-BKNO.\n033580     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.\n033582     MOVE Z-DATE2-MM TO Z-DATE3-MM.\n033584     MOVE Z-DATE2-DD TO Z-DATE3-DD.\n033586     MOVE Z-DATE2-YY TO Z-DATE3-YY.\n033588     MOVE Z-DATE3-FORMAT-9 TO TP-LN-DATE.\n033590     MOVE WS-TP-DLY-WKLY TO TP-LN3.\n033592     MOVE 1 TO TP-SKIP.\n033594     MOVE \"F\" TO WS-TEAR-PAGE-TYPE.\n033596     MOVE BANK-CSI-BR-CODE TO H-CSI-BR-NO.\n033598     MOVE BANK-NO TO H-BANK-NO-9.\n033600     MOVE BANK-NAME TO H-BANK-NAME.\n033602     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.\n033604     MOVE Z-DATE2-MM TO Z-DATE3-MM.\n033606     MOVE Z-DATE2-DD TO Z-DATE3-DD.\n033608     MOVE Z-DATE2-YY TO Z-DATE3-YY.\n033610     MOVE Z-DATE3-FORMAT-9 TO H-DATE.\n033612*    RETRIEVE TODAY'S DATE\n033614     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n033616          USING Z-CALL-CURRENTDATE.\n033618     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n033620     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n033622     ACCEPT Z-DATE0-TIME   FROM TIME.\n033624     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.\n033626     MOVE Z-DATE0-UU TO Z-DATE4-UU.\n033628     MOVE Z-DATE4-FORMAT-9 TO H-CSI-HHMM.\n033630*    RETRIEVE TODAY'S DATE\n033632     CALL \"CURRENT_DATE OF GENERALSUPPORT\"\n033634          USING Z-CALL-CURRENTDATE.\n033636     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.\n033638     ACCEPT Z-DATE0-YYJJJ  FROM DAY.\n033640     ACCEPT Z-DATE0-TIME   FROM TIME.\n033642     MOVE Z-DATE0-DD TO Z-DATE5-DD.\n033644     MOVE Z-DATE5-FORMAT-9 TO H-CSI-DD.\n033646     IF H-REPORT-NO = \"TD-4720\"\n033648         NEXT SENTENCE ELSE\n033650         GO TO Z-22-40-1-ELSE.\n033652     MOVE \"TDA POSTAL ZIP+4 UNCHANGED\" TO H-RPT-TITLE.\n033654     MOVE 1 TO GWS-MICROFICHE-CODE.\n033656     MOVE \"Y\" TO WS-FICHE-REQUEST.\n033658     MOVE \" \" TO WS-LIST-REQUEST.\n033660     GO TO Z-22-40-ENDIF.\n033662 Z-22-40-1-ELSE.\n033664     IF H-REPORT-NO = \"TDA-701\"\n033666         NEXT SENTENCE ELSE\n033668         GO TO Z-22-40-2-ELSE.\n033670     MOVE \"RMD CALCULATION REPORT FOR INHERITED IRA'S\" TO         \n033672         H-RPT-TITLE.\n033674     GO TO Z-22-40-ENDIF.\n033676 Z-22-40-2-ELSE.\n033678     MOVE \"TIME DEPOSIT EXCEPTIONS\" TO H-REPORT-TITLE.\n033680     MOVE \"TD-000 \" TO H-REPORT-NO.\n033682 Z-22-40-ENDIF.\n033684************ PERFORM HEADING-SETUP\n033686     PERFORM Z-16-PROCEDURE THRU Z-16-XIT.\n033688     IF  Z-EXIT-EDITEXIT\n033690         GO TO Z-22-XIT.\n033692     IF  Z-DMS2-ABORT-FLAG = 1\n033694         GO TO Z-22-XIT.\n033696     IF  Z-EXIT-LEVEL < 0\n033698         GO TO Z-22-END.\n033700*\n033702     MOVE 1 TO HDR-CTL.\n033704************ PERFORM TPR-TEAR-PAGES\n033706     PERFORM Z-21-PROCEDURE THRU Z-21-XIT.\n033708     IF  Z-EXIT-EDITEXIT\n033710         GO TO Z-22-XIT.\n033712     IF  Z-DMS2-ABORT-FLAG = 1\n033714         GO TO Z-22-XIT.\n033716     IF  Z-EXIT-LEVEL < 0\n033718         GO TO Z-22-END.\n033720*\n033722     MOVE 0 TO PRT-FICHE-FILE-STATUS.\n033724*\n033726***********  CLOSE OF REPORT FILE  FICHE WITH CRUNCH\n033728*\n033730     IF  Z-RPTINFO2-OPEN NOT = 0\n033732         CLOSE FICHE WITH CRUNCH\n033734         MOVE 0 TO Z-RPTINFO2-OPEN\n033736         MOVE 0 TO Z-RPTINFO2-RS-OPEN.\n033738*********IF H-REPORT-NO NOT = \"TD-4720\"                           \n033740     IF ( GWS-PRT-NEW = 1 )\n033742         NEXT SENTENCE ELSE\n033744         GO TO Z-22-53-1-ELSE.\n033746           PERFORM 999999-CHANGE72.                               \n033748     IF ( WS-SYS-HOST = \"CSIB\" )\n033750         NEXT SENTENCE ELSE\n033752         GO TO Z-22-54-1-ELSE.\n033754             PERFORM 999999-CHANGE52.                             \n033756     GO TO Z-22-54-ENDIF.\n033758 Z-22-54-1-ELSE.\n033760             PERFORM 999999-CHANGE53.                             \n033762 Z-22-54-ENDIF.\n033764     GO TO Z-22-53-ENDIF.\n033766 Z-22-53-1-ELSE.\n033768            PERFORM 999999-CHANGE73.                              \n033770 Z-22-53-ENDIF.\n033772 Z-22-28-1-ELSE.\n033774*****ENDIF.                                                       \n033776 Z-22-END.\n033778     IF Z-EDIT-ERROR\n033780         GO TO Z-22-XIT.\n033782 Z-22-SKIP.\n033784     IF Z-EXIT-LEVEL NOT < 0\n033786         MOVE 0 TO Z-EXIT-CODE\n033788         MOVE 9999 TO Z-EXIT-LEVEL.\n033790 Z-22-XIT.\n033792     EXIT.\n033794*\n033796*****************************************************************\n033798*    PROCEDURE WRITE-REPORT\n033800*****************************************************************\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    566 lines from 16331 to 16896.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 34, "total_chunks": 55, "start_line": 16331, "end_line": 16896, "line_count": 566}

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
- Source code length: 27389 characters

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
CHUNK 34 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 16331 to 16896 (566 lines)
Chunk Tokens (estimated): ~7,990
Actual Input Tokens: 9,396 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 16331-16896 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 34 of 55 chunks
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
      The source code below is only CHUNK 34 of 55.


=============================================================================
CHUNK 34 SOURCE CODE (Lines 16331-16896)
=============================================================================

```cobol
032670 Z-20-29-2-ELSE.
032672     IF H-REPORT-NO = "TDA-053"
032674         NEXT SENTENCE ELSE
032676         GO TO Z-20-29-3-ELSE.
032678     MOVE "053" TO GWS-RMT-EXT.
032680     GO TO Z-20-29-ENDIF.
032682 Z-20-29-3-ELSE.
032684     IF H-REPORT-NO = "TDA-700"
032686         NEXT SENTENCE ELSE
032688         GO TO Z-20-29-4-ELSE.
032690     MOVE "700" TO GWS-RMT-EXT.
032692 Z-20-29-4-ELSE.
032694 Z-20-29-ENDIF.
032696     IF TDB-TDAPC-COPIES > 1
032698         NEXT SENTENCE ELSE
032700         GO TO Z-20-34-1-ELSE.
032702     MOVE TDB-TDAPC-COPIES TO GWS-NO-PARTS.
032704     IF TDB-TDAPC-FICHE-PRT > 0
032706         NEXT SENTENCE
032708     ELSE
032710         GO TO Z-20-36-END-MOVE.
032712     MOVE "1" TO GWS-MICROFICHE-CODE.
032714 Z-20-36-END-MOVE.
032716 Z-20-34-1-ELSE.
032718     IF TDB-TDAPC-FICHE-PRT > 0
032720         NEXT SENTENCE ELSE
032722         GO TO Z-20-37-1-ELSE.
032724     COMPUTE Z-GSTRNUM-1-9 = 1 + TDB-TDAPC-FICHE-PRT.
032726     MOVE Z-GSTRNUM-1 TO GWS-MICROFICHE-CODE.
032728 Z-20-37-1-ELSE.
032730        PERFORM 99-PRT-LABEL-CHECK.                               
032732     IF ( WS-SYS-HOST = "CSIA" ) OR ( WS-SYS-HOST = "CSID" ) OR ( 
032734         WS-SYS-HOST = "CSIB" )
032736         NEXT SENTENCE ELSE
032738         GO TO Z-20-39-1-ELSE.
032740     MOVE ID-PRT74-2 TO WS-LISTING-NAME.
032742     DISPLAY "WS-LISTING-NAME -> ", WS-LISTING-NAME.
032744     MOVE WS-LISTING-NAME TO Z-LALPHA-1.
032746     MOVE SPACES TO Z-LALPHA-2.
032748     MOVE " ON" TO Z-LALPHA-3.
032750     MOVE 40 TO Z-GINT-1.
032752     MOVE 0 TO Z-LINT-1.
032754     MOVE 3 TO Z-LINT-2.
032756     MOVE SPACES TO Z-GALPHA-1.
032758     CALL "XSTRPAT OF XGEN/RUNTIME/LIBRARY" USING Z-GALPHA-1,     
032760         Z-LALPHA-1, Z-LALPHA-2, Z-LALPHA-3, Z-GINT-1,            
032762         Z-STR-INT-ZERO, Z-LINT-1, Z-STR-INT-ONE, Z-LINT-2,       
032764         Z-STR-INT-ONE.
032766     IF Z-GINT-1 < 1
032768         MOVE 1 TO Z-GINT-1.
032770     MOVE Z-GALPHA-1 TO WS-LISTING-NAME.
032772     MOVE "." TO Z-LALPHA-1.
032774     MOVE 40 TO Z-GINT-1.
032776     MOVE 1 TO Z-LINT-1.
032778     MOVE WS-LISTING-NAME TO Z-GALPHA-1.
032780     CALL "XSTRCAT OF XGEN/RUNTIME/LIBRARY" USING Z-GALPHA-1,     
032782         Z-STR-INT-ZERO, Z-LALPHA-1, Z-GINT-1, Z-STR-INT-ZERO,    
032784         Z-LINT-1.
032786     IF Z-GINT-1 < 1
032788         MOVE 1 TO Z-GINT-1.
032790     MOVE Z-GALPHA-1 TO WS-LISTING-NAME.
032792     GO TO Z-20-39-ENDIF.
032794 Z-20-39-1-ELSE.
032796     MOVE ID-PRT74-2 TO ID-PRINT-NAME-NT.
032798            INSPECT ID-PRINT-NAME-NT REPLACING ALL "/" BY "_".    
032800     MOVE ID-PRINT-FILES-NT TO WS-LISTING-NAME.
032802     DISPLAY "WS-LISTING-NAME -> ", WS-LISTING-NAME.
032804 Z-20-39-ENDIF.
032806        PERFORM 999999-CHANGE1.                                   
032808        PERFORM 999999-CHANGE24.                                  
032810     MOVE 1 TO PRT-LIST-FILE-STATUS.
032812     MOVE BANK-CSI-BR-CODE TO H-CSI-BR-NO.
032814     MOVE BANK-NO TO H-BANK-NO-9.
032816     MOVE BANK-NAME TO H-BANK-NAME.
032818     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.
032820     MOVE Z-DATE2-MM TO Z-DATE3-MM.
032822     MOVE Z-DATE2-DD TO Z-DATE3-DD.
032824     MOVE Z-DATE2-YY TO Z-DATE3-YY.
032826     MOVE Z-DATE3-FORMAT-9 TO H-DATE.
032828*    RETRIEVE TODAY'S DATE
032830     CALL "CURRENT_DATE OF GENERALSUPPORT"
032832          USING Z-CALL-CURRENTDATE.
032834     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
032836     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
032838     ACCEPT Z-DATE0-TIME   FROM TIME.
032840     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.
032842     MOVE Z-DATE0-UU TO Z-DATE4-UU.
032844     MOVE Z-DATE4-FORMAT-9 TO H-CSI-HHMM.
032846*    RETRIEVE TODAY'S DATE
032848     CALL "CURRENT_DATE OF GENERALSUPPORT"
032850          USING Z-CALL-CURRENTDATE.
032852     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
032854     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
032856     ACCEPT Z-DATE0-TIME   FROM TIME.
032858     MOVE Z-DATE0-DD TO Z-DATE5-DD.
032860     MOVE Z-DATE5-FORMAT-9 TO H-CSI-DD.
032862     IF H-REPORT-NO = "TD-4920"
032864         NEXT SENTENCE ELSE
032866         GO TO Z-20-54-1-ELSE.
032868     MOVE "TDA ZIP+4 FILE MAINTENANCE" TO H-RPT-TITLE.
032870     GO TO Z-20-54-ENDIF.
032872 Z-20-54-1-ELSE.
032874     IF H-REPORT-NO = "TDA-054"
032876         NEXT SENTENCE ELSE
032878         GO TO Z-20-54-2-ELSE.
032880     MOVE "CLOSED COD HISTORY REPORT" TO H-RPT-TITLE.
032882     GO TO Z-20-54-ENDIF.
032884 Z-20-54-2-ELSE.
032886     IF H-REPORT-NO = "TDA-700"
032888         NEXT SENTENCE ELSE
032890         GO TO Z-20-54-3-ELSE.
032892     MOVE "RMD CALCULATION REPORT" TO H-RPT-TITLE.
032894     GO TO Z-20-54-ENDIF.
032896 Z-20-54-3-ELSE.
032898     MOVE "TIME DEPOSIT EXCEPTIONS" TO H-REPORT-TITLE.
032900     MOVE "TD-000 " TO H-REPORT-NO.
032902 Z-20-54-ENDIF.
032904     MOVE 1 TO HDR-CTL.
032906********IF  H-REPORT-NO NOT = "TD-4920"                           
032908     IF ( GWS-PRT-NEW = 1 )
032910         NEXT SENTENCE ELSE
032912         GO TO Z-20-61-1-ELSE.
032914                PERFORM 999999-CHANGE54.                          
032916                PERFORM 999999-CHANGE34.                          
032918     GO TO Z-20-61-ENDIF.
032920 Z-20-61-1-ELSE.
032922                PERFORM 999999-CHANGE55.                          
032924 Z-20-61-ENDIF.
032926********ENDIF.                                                    
032928*
032930******* OPEN REPORT LISTING
032932*
032934     IF  Z-RPTINFO1-OPEN = 0
032936         OPEN OUTPUT LISTING 
032938         MOVE ZEROS TO Z-RPT-1-PAGE
032940         MOVE ZEROS TO Z-RPT-1-LINE
032942         MOVE ZEROS TO Z-RPT-1-TRAP
032944         MOVE 3 TO Z-RPTINFO1-OPEN
032946         MOVE 3 TO Z-RPTINFO1-RS-OPEN.
032948     MOVE "BK" TO TP-LN-BANK.
032950     MOVE PROC-BANK TO TP-LN-BKNO.
032952     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.
032954     MOVE Z-DATE2-MM TO Z-DATE3-MM.
032956     MOVE Z-DATE2-DD TO Z-DATE3-DD.
032958     MOVE Z-DATE2-YY TO Z-DATE3-YY.
032960     MOVE Z-DATE3-FORMAT-9 TO TP-LN-DATE.
032962     MOVE WS-TP-DLY-WKLY TO TP-LN3.
032964     MOVE "P" TO WS-TEAR-PAGE-TYPE.
032966     IF H-REPORT-NO NOT = "TDA-041"
032968         NEXT SENTENCE ELSE
032970         GO TO Z-20-68-1-ELSE.
032972************ PERFORM TPR-TEAR-PAGES
032974     PERFORM Z-21-PROCEDURE THRU Z-21-XIT.
032976     IF  Z-EXIT-EDITEXIT
032978         GO TO Z-20-XIT.
032980     IF  Z-DMS2-ABORT-FLAG = 1
032982         GO TO Z-20-XIT.
032984     IF  Z-EXIT-LEVEL < 0
032986         GO TO Z-20-END.
032988*
032990 Z-20-68-1-ELSE.
032992 Z-20-27-1-ELSE.
032994     IF FICHE-REQUEST AND PRT-FICHE-CLOSE
032996         NEXT SENTENCE ELSE
032998         GO TO Z-20-70-1-ELSE.
033000     MOVE "SP" TO GWS-PRT-DESCRIPTOR.
033002     MOVE 0 TO GWS-NO-PARTS.
033004     COMPUTE Z-GSTRNUM-2-9 = 1 + TDB-TDAPC-FICHE-PRT.
033006     MOVE Z-GSTRNUM-2 TO GWS-MICROFICHE-CODE.
033008     IF H-REPORT-NO = "TD-4720"
033010         NEXT SENTENCE ELSE
033012         GO TO Z-20-74-1-ELSE.
033014     MOVE "472" TO GWS-RMT-EXT.
033016     GO TO Z-20-74-ENDIF.
033018 Z-20-74-1-ELSE.
033020     IF H-REPORT-NO = "TDA-701"
033022         NEXT SENTENCE ELSE
033024         GO TO Z-20-74-2-ELSE.
033026     MOVE "701" TO GWS-RMT-EXT.
033028     GO TO Z-20-74-ENDIF.
033030 Z-20-74-2-ELSE.
033032     MOVE "950" TO GWS-RMT-EXT.
033034 Z-20-74-ENDIF.
033036        PERFORM 99-PRT-LABEL-CHECK.                               
033038     MOVE 0 TO WS-FICHE-RMT-PASS.
033040     MOVE "000" TO GWS-RMT-EXT.
033042     MOVE ID-PRT74-2 TO WS-FICHE-NAME.
033044     MOVE ID-PRT74-2 TO ID-PRINT-NAME-NT.
033046        INSPECT ID-PRINT-NAME-NT REPLACING ALL "/" BY "_".        
033048     IF ( WS-SYS-HOST = "CSIA" ) OR ( WS-SYS-HOST = "CSID" ) OR ( 
033050         WS-SYS-HOST = "CSIB" )
033052         NEXT SENTENCE ELSE
033054         GO TO Z-20-82-1-ELSE.
033056     DISPLAY "WS-FICHE-NAME -> ", WS-FICHE-NAME.
033058     MOVE WS-FICHE-NAME TO Z-LALPHA-1.
033060     MOVE SPACES TO Z-LALPHA-2.
033062     MOVE " ON" TO Z-LALPHA-3.
033064     MOVE 40 TO Z-GINT-1.
033066     MOVE 0 TO Z-LINT-1.
033068     MOVE 3 TO Z-LINT-2.
033070     MOVE SPACES TO Z-GALPHA-1.
033072     CALL "XSTRPAT OF XGEN/RUNTIME/LIBRARY" USING Z-GALPHA-1,     
033074         Z-LALPHA-1, Z-LALPHA-2, Z-LALPHA-3, Z-GINT-1,            
033076         Z-STR-INT-ZERO, Z-LINT-1, Z-STR-INT-ONE, Z-LINT-2,       
033078         Z-STR-INT-ONE.
033080     IF Z-GINT-1 < 1
033082         MOVE 1 TO Z-GINT-1.
033084     MOVE Z-GALPHA-1 TO WS-FICHE-NAME.
033086     MOVE "." TO Z-LALPHA-1.
033088     MOVE 40 TO Z-GINT-1.
033090     MOVE 1 TO Z-LINT-1.
033092     MOVE WS-FICHE-NAME TO Z-GALPHA-1.
033094     CALL "XSTRCAT OF XGEN/RUNTIME/LIBRARY" USING Z-GALPHA-1,     
033096         Z-STR-INT-ZERO, Z-LALPHA-1, Z-GINT-1, Z-STR-INT-ZERO,    
033098         Z-LINT-1.
033100     IF Z-GINT-1 < 1
033102         MOVE 1 TO Z-GINT-1.
033104     MOVE Z-GALPHA-1 TO WS-FICHE-NAME.
033106     GO TO Z-20-82-ENDIF.
033108 Z-20-82-1-ELSE.
033110     MOVE ID-PRINT-FILES-NT TO WS-FICHE-NAME.
033112     DISPLAY "WS-FICHE-NAME -> ", WS-FICHE-NAME.
033114 Z-20-82-ENDIF.
033116        PERFORM 999999-CHANGE22.                                  
033118        PERFORM 999999-CHANGE33.                                  
033120     MOVE 1 TO PRT-FICHE-FILE-STATUS.
033122     MOVE BANK-CSI-BR-CODE TO H-CSI-BR-NO.
033124     MOVE BANK-NO TO H-BANK-NO-9.
033126     MOVE BANK-NAME TO H-BANK-NAME.
033128     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.
033130     MOVE Z-DATE2-MM TO Z-DATE3-MM.
033132     MOVE Z-DATE2-DD TO Z-DATE3-DD.
033134     MOVE Z-DATE2-YY TO Z-DATE3-YY.
033136     MOVE Z-DATE3-FORMAT-9 TO H-DATE.
033138*    RETRIEVE TODAY'S DATE
033140     CALL "CURRENT_DATE OF GENERALSUPPORT"
033142          USING Z-CALL-CURRENTDATE.
033144     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
033146     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
033148     ACCEPT Z-DATE0-TIME   FROM TIME.
033150     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.
033152     MOVE Z-DATE0-UU TO Z-DATE4-UU.
033154     MOVE Z-DATE4-FORMAT-9 TO H-CSI-HHMM.
033156*    RETRIEVE TODAY'S DATE
033158     CALL "CURRENT_DATE OF GENERALSUPPORT"
033160          USING Z-CALL-CURRENTDATE.
033162     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
033164     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
033166     ACCEPT Z-DATE0-TIME   FROM TIME.
033168     MOVE Z-DATE0-DD TO Z-DATE5-DD.
033170     MOVE Z-DATE5-FORMAT-9 TO H-CSI-DD.
033172     IF H-REPORT-NO = "TD-4720"
033174         NEXT SENTENCE ELSE
033176         GO TO Z-20-95-1-ELSE.
033178     MOVE "TDA POSTAL ZIP+4 UNCHANGED" TO H-RPT-TITLE.
033180     GO TO Z-20-95-ENDIF.
033182 Z-20-95-1-ELSE.
033184     IF H-REPORT-NO = "TDA-701"
033186         NEXT SENTENCE ELSE
033188         GO TO Z-20-95-2-ELSE.
033190     MOVE "RMD CALCULATION REPORT FOR INHERITED IRA'S" TO         
033192         H-RPT-TITLE.
033194     GO TO Z-20-95-ENDIF.
033196 Z-20-95-2-ELSE.
033198     MOVE "TIME DEPOSIT EXCEPTIONS" TO H-REPORT-TITLE.
033200     MOVE "TD-000 " TO H-REPORT-NO.
033202 Z-20-95-ENDIF.
033204************ PERFORM HEADING-SETUP
033206     PERFORM Z-16-PROCEDURE THRU Z-16-XIT.
033208     IF  Z-EXIT-EDITEXIT
033210         GO TO Z-20-XIT.
033212     IF  Z-DMS2-ABORT-FLAG = 1
033214         GO TO Z-20-XIT.
033216     IF  Z-EXIT-LEVEL < 0
033218         GO TO Z-20-END.
033220*
033222     MOVE 1 TO HDR-CTL.
033224********IF  H-REPORT-NO NOT = "TD-4720"                           
033226     IF ( GWS-PRT-NEW = 1 )
033228         NEXT SENTENCE ELSE
033230         GO TO Z-20-102-1-ELSE.
033232           PERFORM 999999-CHANGE72.                               
033234     IF ( WS-SYS-HOST = "CSIB" )
033236         NEXT SENTENCE ELSE
033238         GO TO Z-20-103-1-ELSE.
033240              PERFORM 999999-CHANGE52.                            
033242     GO TO Z-20-103-ENDIF.
033244 Z-20-103-1-ELSE.
033246              PERFORM 999999-CHANGE53.                            
033248 Z-20-103-ENDIF.
033250     GO TO Z-20-102-ENDIF.
033252 Z-20-102-1-ELSE.
033254           PERFORM 999999-CHANGE73.                               
033256********ENDIF.                                                    
033258 Z-20-102-ENDIF.
033260*
033262******* OPEN REPORT FICHE
033264*
033266     IF  Z-RPTINFO2-OPEN = 0
033268         OPEN OUTPUT FICHE 
033270         MOVE ZEROS TO Z-RPT-2-PAGE
033272         MOVE ZEROS TO Z-RPT-2-LINE
033274         MOVE ZEROS TO Z-RPT-2-TRAP
033276         MOVE 3 TO Z-RPTINFO2-OPEN
033278         MOVE 3 TO Z-RPTINFO2-RS-OPEN.
033280     MOVE "BK" TO TP-LN-BANK.
033282     MOVE PROC-BANK TO TP-LN-BKNO.
033284     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.
033286     MOVE Z-DATE2-MM TO Z-DATE3-MM.
033288     MOVE Z-DATE2-DD TO Z-DATE3-DD.
033290     MOVE Z-DATE2-YY TO Z-DATE3-YY.
033292     MOVE Z-DATE3-FORMAT-9 TO TP-LN-DATE.
033294     MOVE WS-TP-DLY-WKLY TO TP-LN3.
033296     MOVE "F" TO WS-TEAR-PAGE-TYPE.
033298************ PERFORM TPR-TEAR-PAGES
033300     PERFORM Z-21-PROCEDURE THRU Z-21-XIT.
033302     IF  Z-EXIT-EDITEXIT
033304         GO TO Z-20-XIT.
033306     IF  Z-DMS2-ABORT-FLAG = 1
033308         GO TO Z-20-XIT.
033310     IF  Z-EXIT-LEVEL < 0
033312         GO TO Z-20-END.
033314*
033316 Z-20-70-1-ELSE.
033318     IF LIST-REQUEST AND TDB-TDAPC-RPT-NBR NOT = 651
033320         NEXT SENTENCE ELSE
033322         GO TO Z-20-111-1-ELSE.
033324     MOVE ZEROS TO Z-RPT-1-PAGE.
033326     MOVE 58 TO Z-RPT-1-LINE.
033328 Z-20-111-1-ELSE.
033330     IF FICHE-REQUEST
033332         NEXT SENTENCE ELSE
033334         GO TO Z-20-114-1-ELSE.
033336     MOVE ZEROS TO Z-RPT-2-PAGE.
033338     MOVE 58 TO Z-RPT-2-LINE.
033340 Z-20-114-1-ELSE.
033342 Z-20-END.
033344     IF Z-EDIT-ERROR
033346         GO TO Z-20-XIT.
033348 Z-20-SKIP.
033350     IF Z-EXIT-LEVEL NOT < 0
033352         MOVE 0 TO Z-EXIT-CODE
033354         MOVE 9999 TO Z-EXIT-LEVEL.
033356 Z-20-XIT.
033358     EXIT.
033360*
033362*****************************************************************
033364*    PROCEDURE CLOSE-PRT-FILE
033366*****************************************************************
033368 Z-22-PROCEDURE.
033370*
033372     MOVE 0 TO Z-EXIT-CODE.
033374     MOVE 9999 TO Z-EXIT-LEVEL.
033376     IF PRT-LIST-OPEN
033378         NEXT SENTENCE ELSE
033380         GO TO Z-22-1-1-ELSE.
033382     MOVE PROC-BANK TO TP-LN-BKNO.
033384     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.
033386     MOVE Z-DATE2-MM TO Z-DATE3-MM.
033388     MOVE Z-DATE2-DD TO Z-DATE3-DD.
033390     MOVE Z-DATE2-YY TO Z-DATE3-YY.
033392     MOVE Z-DATE3-FORMAT-9 TO TP-LN-DATE.
033394     MOVE WS-TP-DLY-WKLY TO TP-LN3.
033396     MOVE 1 TO TP-SKIP.
033398     MOVE "P" TO WS-TEAR-PAGE-TYPE.
033400     MOVE BANK-CSI-BR-CODE TO H-CSI-BR-NO.
033402     MOVE BANK-NO TO H-BANK-NO-9.
033404     MOVE BANK-NAME TO H-BANK-NAME.
033406     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.
033408     MOVE Z-DATE2-MM TO Z-DATE3-MM.
033410     MOVE Z-DATE2-DD TO Z-DATE3-DD.
033412     MOVE Z-DATE2-YY TO Z-DATE3-YY.
033414     MOVE Z-DATE3-FORMAT-9 TO H-DATE.
033416*    RETRIEVE TODAY'S DATE
033418     CALL "CURRENT_DATE OF GENERALSUPPORT"
033420          USING Z-CALL-CURRENTDATE.
033422     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
033424     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
033426     ACCEPT Z-DATE0-TIME   FROM TIME.
033428     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.
033430     MOVE Z-DATE0-UU TO Z-DATE4-UU.
033432     MOVE Z-DATE4-FORMAT-9 TO H-CSI-HHMM.
033434*    RETRIEVE TODAY'S DATE
033436     CALL "CURRENT_DATE OF GENERALSUPPORT"
033438          USING Z-CALL-CURRENTDATE.
033440     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
033442     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
033444     ACCEPT Z-DATE0-TIME   FROM TIME.
033446     MOVE Z-DATE0-DD TO Z-DATE5-DD.
033448     MOVE Z-DATE5-FORMAT-9 TO H-CSI-DD.
033450     IF H-REPORT-NO = "TDA-054"
033452         NEXT SENTENCE ELSE
033454         GO TO Z-22-13-1-ELSE.
033456     MOVE "CLOSED COD HISTORY REPORT" TO H-RPT-TITLE.
033458     GO TO Z-22-13-ENDIF.
033460 Z-22-13-1-ELSE.
033462     IF H-REPORT-NO = "TD-4920"
033464         NEXT SENTENCE ELSE
033466         GO TO Z-22-13-2-ELSE.
033468     MOVE "TDA ZIP+4 FILE MAINTENANCE" TO H-RPT-TITLE.
033470     MOVE 0 TO GWS-MICROFICHE-CODE.
033472     MOVE "Y" TO WS-LIST-REQUEST.
033474     MOVE " " TO WS-FICHE-REQUEST.
033476     GO TO Z-22-13-ENDIF.
033478 Z-22-13-2-ELSE.
033480     IF H-REPORT-NO = "TDA-700"
033482         NEXT SENTENCE ELSE
033484         GO TO Z-22-13-3-ELSE.
033486     MOVE "RMD CALCULATION REPORT" TO H-RPT-TITLE.
033488     GO TO Z-22-13-ENDIF.
033490 Z-22-13-3-ELSE.
033492     MOVE "TIME DEPOSIT EXCEPTIONS" TO H-REPORT-TITLE.
033494     MOVE "TD-000 " TO H-REPORT-NO.
033496 Z-22-13-ENDIF.
033498************ PERFORM HEADING-SETUP
033500     PERFORM Z-16-PROCEDURE THRU Z-16-XIT.
033502     IF  Z-EXIT-EDITEXIT
033504         GO TO Z-22-XIT.
033506     IF  Z-DMS2-ABORT-FLAG = 1
033508         GO TO Z-22-XIT.
033510     IF  Z-EXIT-LEVEL < 0
033512         GO TO Z-22-END.
033514*
033516     MOVE 1 TO HDR-CTL.
033518************ PERFORM TPR-TEAR-PAGES
033520     PERFORM Z-21-PROCEDURE THRU Z-21-XIT.
033522     IF  Z-EXIT-EDITEXIT
033524         GO TO Z-22-XIT.
033526     IF  Z-DMS2-ABORT-FLAG = 1
033528         GO TO Z-22-XIT.
033530     IF  Z-EXIT-LEVEL < 0
033532         GO TO Z-22-END.
033534*
033536     MOVE 0 TO PRT-LIST-FILE-STATUS.
033538*
033540***********  CLOSE OF REPORT FILE  LISTING WITH CRUNCH
033542*
033544     IF  Z-RPTINFO1-OPEN NOT = 0
033546         CLOSE LISTING WITH CRUNCH
033548         MOVE 0 TO Z-RPTINFO1-OPEN
033550         MOVE 0 TO Z-RPTINFO1-RS-OPEN.
033552     IF GWS-PRT-NEW = 1
033554         NEXT SENTENCE ELSE
033556         GO TO Z-22-27-1-ELSE.
033558               PERFORM 999999-CHANGE54.                           
033560               PERFORM 999999-CHANGE34.                           
033562     GO TO Z-22-27-ENDIF.
033564 Z-22-27-1-ELSE.
033566               PERFORM 999999-CHANGE55.                           
033568 Z-22-27-ENDIF.
033570 Z-22-1-1-ELSE.
033572     IF PRT-FICHE-OPEN
033574         NEXT SENTENCE ELSE
033576         GO TO Z-22-28-1-ELSE.
033578     MOVE PROC-BANK TO TP-LN-BKNO.
033580     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.
033582     MOVE Z-DATE2-MM TO Z-DATE3-MM.
033584     MOVE Z-DATE2-DD TO Z-DATE3-DD.
033586     MOVE Z-DATE2-YY TO Z-DATE3-YY.
033588     MOVE Z-DATE3-FORMAT-9 TO TP-LN-DATE.
033590     MOVE WS-TP-DLY-WKLY TO TP-LN3.
033592     MOVE 1 TO TP-SKIP.
033594     MOVE "F" TO WS-TEAR-PAGE-TYPE.
033596     MOVE BANK-CSI-BR-CODE TO H-CSI-BR-NO.
033598     MOVE BANK-NO TO H-BANK-NO-9.
033600     MOVE BANK-NAME TO H-BANK-NAME.
033602     MOVE PROCESS-DATE TO Z-DATE2-FORMAT-9.
033604     MOVE Z-DATE2-MM TO Z-DATE3-MM.
033606     MOVE Z-DATE2-DD TO Z-DATE3-DD.
033608     MOVE Z-DATE2-YY TO Z-DATE3-YY.
033610     MOVE Z-DATE3-FORMAT-9 TO H-DATE.
033612*    RETRIEVE TODAY'S DATE
033614     CALL "CURRENT_DATE OF GENERALSUPPORT"
033616          USING Z-CALL-CURRENTDATE.
033618     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
033620     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
033622     ACCEPT Z-DATE0-TIME   FROM TIME.
033624     MOVE Z-DATE0-ZZ TO Z-DATE4-ZZ.
033626     MOVE Z-DATE0-UU TO Z-DATE4-UU.
033628     MOVE Z-DATE4-FORMAT-9 TO H-CSI-HHMM.
033630*    RETRIEVE TODAY'S DATE
033632     CALL "CURRENT_DATE OF GENERALSUPPORT"
033634          USING Z-CALL-CURRENTDATE.
033636     MOVE Z-CALL-CURRENTDATE TO Z-DATE0-FORMAT.
033638     ACCEPT Z-DATE0-YYJJJ  FROM DAY.
033640     ACCEPT Z-DATE0-TIME   FROM TIME.
033642     MOVE Z-DATE0-DD TO Z-DATE5-DD.
033644     MOVE Z-DATE5-FORMAT-9 TO H-CSI-DD.
033646     IF H-REPORT-NO = "TD-4720"
033648         NEXT SENTENCE ELSE
033650         GO TO Z-22-40-1-ELSE.
033652     MOVE "TDA POSTAL ZIP+4 UNCHANGED" TO H-RPT-TITLE.
033654     MOVE 1 TO GWS-MICROFICHE-CODE.
033656     MOVE "Y" TO WS-FICHE-REQUEST.
033658     MOVE " " TO WS-LIST-REQUEST.
033660     GO TO Z-22-40-ENDIF.
033662 Z-22-40-1-ELSE.
033664     IF H-REPORT-NO = "TDA-701"
033666         NEXT SENTENCE ELSE
033668         GO TO Z-22-40-2-ELSE.
033670     MOVE "RMD CALCULATION REPORT FOR INHERITED IRA'S" TO         
033672         H-RPT-TITLE.
033674     GO TO Z-22-40-ENDIF.
033676 Z-22-40-2-ELSE.
033678     MOVE "TIME DEPOSIT EXCEPTIONS" TO H-REPORT-TITLE.
033680     MOVE "TD-000 " TO H-REPORT-NO.
033682 Z-22-40-ENDIF.
033684************ PERFORM HEADING-SETUP
033686     PERFORM Z-16-PROCEDURE THRU Z-16-XIT.
033688     IF  Z-EXIT-EDITEXIT
033690         GO TO Z-22-XIT.
033692     IF  Z-DMS2-ABORT-FLAG = 1
033694         GO TO Z-22-XIT.
033696     IF  Z-EXIT-LEVEL < 0
033698         GO TO Z-22-END.
033700*
033702     MOVE 1 TO HDR-CTL.
033704************ PERFORM TPR-TEAR-PAGES
033706     PERFORM Z-21-PROCEDURE THRU Z-21-XIT.
033708     IF  Z-EXIT-EDITEXIT
033710         GO TO Z-22-XIT.
033712     IF  Z-DMS2-ABORT-FLAG = 1
033714         GO TO Z-22-XIT.
033716     IF  Z-EXIT-LEVEL < 0
033718         GO TO Z-22-END.
033720*
033722     MOVE 0 TO PRT-FICHE-FILE-STATUS.
033724*
033726***********  CLOSE OF REPORT FILE  FICHE WITH CRUNCH
033728*
033730     IF  Z-RPTINFO2-OPEN NOT = 0
033732         CLOSE FICHE WITH CRUNCH
033734         MOVE 0 TO Z-RPTINFO2-OPEN
033736         MOVE 0 TO Z-RPTINFO2-RS-OPEN.
033738*********IF H-REPORT-NO NOT = "TD-4720"                           
033740     IF ( GWS-PRT-NEW = 1 )
033742         NEXT SENTENCE ELSE
033744         GO TO Z-22-53-1-ELSE.
033746           PERFORM 999999-CHANGE72.                               
033748     IF ( WS-SYS-HOST = "CSIB" )
033750         NEXT SENTENCE ELSE
033752         GO TO Z-22-54-1-ELSE.
033754             PERFORM 999999-CHANGE52.                             
033756     GO TO Z-22-54-ENDIF.
033758 Z-22-54-1-ELSE.
033760             PERFORM 999999-CHANGE53.                             
033762 Z-22-54-ENDIF.
033764     GO TO Z-22-53-ENDIF.
033766 Z-22-53-1-ELSE.
033768            PERFORM 999999-CHANGE73.                              
033770 Z-22-53-ENDIF.
033772 Z-22-28-1-ELSE.
033774*****ENDIF.                                                       
033776 Z-22-END.
033778     IF Z-EDIT-ERROR
033780         GO TO Z-22-XIT.
033782 Z-22-SKIP.
033784     IF Z-EXIT-LEVEL NOT < 0
033786         MOVE 0 TO Z-EXIT-CODE
033788         MOVE 9999 TO Z-EXIT-LEVEL.
033790 Z-22-XIT.
033792     EXIT.
033794*
033796*****************************************************************
033798*    PROCEDURE WRITE-REPORT
033800*****************************************************************
```

⚠️  This is the source code you must document.
    566 lines from 16331 to 16896.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

