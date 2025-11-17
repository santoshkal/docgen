# LLM Request Debug File
Generated: 2025-11-14T18:50:15.869319

## Request Metadata
- **Section ID**: detailed-code-explanation
- **Section Title**: Detailed Code-Block Explanation - Chunk 28/55
- **Model**: gpt-4.1
- **Chunk Number**: 28
- **Pass Number**: 3
- **Attempt Number**: 2 (RETRY)

## Token Estimates (4 chars/token)
- **System Prompt**: ~1,958 tokens
- **User Prompt**: ~7,802 tokens
- **Total Input**: ~9,760 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Detailed Code-Block Explanation - Chunk 28/55" (ID: detailed-code-explanation)

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


**CHUNK 28 of 55**: Continue numbering from previous chunks.

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

{"program_name": "TDAS-MINDISTCALC", "timestamp": "2025-11-14T17:36:35.036798", "source_file_path": "/workspace/TDAS-MINDISTCALC.c74", "source_code": "\n=============================================================================\nCHUNK 28 of 55 - TDAS-MINDISTCALC.c74\n=============================================================================\nLines: 13040 to 13672 (633 lines)\nChunk Tokens (estimated): ~7,906\nActual Input Tokens: 9,312 (measured with tiktoken)\n\n\u26a0\ufe0f  MANDATORY ACCOUNTABILITY REQUIREMENTS:\n1. Document EVERY paragraph within lines 13040-13672 sequentially\n2. Start each entry with: \"Block N: PARAGRAPH-NAME (Line X)\"\n3. Process blocks in strict sequential order by line number\n4. At the end, provide completion checklist with ALL paragraphs documented\n5. Missing line numbers will make skipped content immediately obvious\n6. NO SUMMARIZATION - Show complete code for each block\n\nCHUNK PROCESSING RULES:\n- This is chunk 28 of 55 chunks\n- Continue numbering sequentially from previous chunks\n- If this is chunk 1, start numbering from 1\n- If this is chunk 2+, continue from where the previous chunk ended\n- Parse EVERY line in this chunk - do not skip any content\n- Group paragraphs ONLY when they implement a single functionality\n- Provide completion checklist at end listing all documented paragraphs\n=============================================================================\n\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\nNOTE: The above program map shows the ENTIRE program structure for context.\n      The source code below is only CHUNK 28 of 55.\n\n\n=============================================================================\nCHUNK 28 SOURCE CODE (Lines 13040-13672)\n=============================================================================\n\n```cobol\n026088 Z-FL-EXCEPTION.\n026090     IF Z-FILE-EOF\n026092         MOVE \"END OF FILE\" TO Z-FL-EXCEPT-ERR\n026094     ELSE IF Z-FILE-DUPLICATES\n026096         MOVE \"DUPLICATES\" TO Z-FL-EXCEPT-ERR\n026098     ELSE IF Z-FILE-NOTFOUND\n026100         MOVE \"NOT FOUND\" TO Z-FL-EXCEPT-ERR\n026102     ELSE IF Z-FILE-BOUNDARY\n026104         MOVE \"BOUNDARY ERROR\" TO Z-FL-EXCEPT-ERR\n026106     ELSE\n026108         MOVE \"I-O ERROR\" TO Z-FL-EXCEPT-ERR.\n026110*\n026112     MOVE \"(\" TO Z-FL-EXCEPT-LIT-PARN.\n026114     MOVE \") ON FILE \" TO Z-FL-EXCEPT-LIT-ON.\n026116     MOVE \" AT \" TO Z-FL-EXCEPT-LIT-AT.\n026118*\n026120     MOVE 1 TO Z-EDIT-ERROR-FLAG.\n026122     MOVE Z-FL-EXCEPT-MSG TO Z-DISP-COMPACT-BUFFER\n026124     MOVE 80 TO Z-DISP-SIZE\n026126     PERFORM Z-DISP-COMPRESS THRU Z-DISP-COMPRESS-XIT\n026128     MOVE Z-DISP-COMPACT-BUFFER TO Z-FL-EXCEPT-MSG\n026130     DISPLAY Z-FL-EXCEPT-MSG.\n026132     IF  Z-FL-EXCEPT-TITLE NOT EQUAL SPACES\n026134         STRING \">>> TITLE :\" DELIMITED BY SIZE,\n026136                Z-FL-EXCEPT-TITLE DELIMITED BY SIZE\n026138          INTO Z-FL-EXCEPT-MSG\n026140         DISPLAY Z-FL-EXCEPT-MSG.\n026142     MOVE SPACES TO Z-FL-EXCEPT-TITLE.\n026144     MOVE ZEROS TO Z-FLINFO-UPDATES.\n026146*\n026148 Z-FL-EXCEPTION-XIT.\n026150     EXIT.\n026152*\n026154**** DATABASE EXCEPTION\n026156*\n026158 Z-DMS-EXCEPTION.\n026160     MOVE \"DMS \" TO Z-DMS-EXCEPT-LIT-DMS.\n026162     MOVE \"ERROR (CAT:  )\" TO Z-DMS-EXCEPT-CAT.\n026164     MOVE DMSTATUS (DMCATEGORY) TO Z-DMS-EXCEPT-CAT-NO.\n026166     IF DMSTATUS (NOTFOUND)\n026168            MOVE \"NOTFOUND\" TO Z-DMS-EXCEPT-CAT.\n026170     IF DMSTATUS (NORECORD)\n026172            MOVE \"NORECORD\" TO Z-DMS-EXCEPT-CAT.\n026174     IF DMSTATUS (DUPLICATES)\n026176            MOVE \"DUPLICATES\" TO Z-DMS-EXCEPT-CAT.\n026178     IF DMSTATUS (DEADLOCK)\n026180            MOVE \"DEADLOCK\" TO Z-DMS-EXCEPT-CAT.\n026182     IF DMSTATUS (DATAERROR)\n026184            MOVE \"DATAERROR\" TO Z-DMS-EXCEPT-CAT.\n026186     IF DMSTATUS (NOTLOCKED)\n026188            MOVE \"NOTLOCKED\" TO Z-DMS-EXCEPT-CAT.\n026190     IF DMSTATUS (KEYCHANGED)\n026192            MOVE \"KEYCHANGED\" TO Z-DMS-EXCEPT-CAT.\n026194     IF DMSTATUS (SYSTEMERROR)\n026196            MOVE \"SYSTEMERROR\" TO Z-DMS-EXCEPT-CAT.\n026198     IF DMSTATUS (READONLY)\n026200            MOVE \"READONLY\" TO Z-DMS-EXCEPT-CAT.\n026202     IF DMSTATUS (IOERROR)\n026204            MOVE \"IOERROR\" TO Z-DMS-EXCEPT-CAT.\n026206     IF DMSTATUS (LIMITERROR)\n026208            MOVE \"LIMITERROR\" TO Z-DMS-EXCEPT-CAT.\n026210     IF DMSTATUS (OPENERROR)\n026212            MOVE \"OPENERROR\" TO Z-DMS-EXCEPT-CAT.\n026214     IF DMSTATUS (CLOSEERROR)\n026216            MOVE \"CLOSEERROR\" TO Z-DMS-EXCEPT-CAT.\n026218     IF DMSTATUS (NORECORD)\n026220            MOVE \"NORECORD\" TO Z-DMS-EXCEPT-CAT.\n026222     IF DMSTATUS (INUSE)\n026224            MOVE \"INUSE\" TO Z-DMS-EXCEPT-CAT.\n026226     IF DMSTATUS (AUDITERROR)\n026228            MOVE \"AUDITERROR\" TO Z-DMS-EXCEPT-CAT.\n026230     IF DMSTATUS (ABORT)\n026232            MOVE \"ABORT\" TO Z-DMS-EXCEPT-CAT.\n026234     IF DMSTATUS (SECURITYERROR)\n026236            MOVE \"SECURITYERROR\" TO Z-DMS-EXCEPT-CAT.\n026238     IF DMSTATUS (VERSIONERROR)\n026240            MOVE \"VERSIONERROR\" TO Z-DMS-EXCEPT-CAT.\n026242     MOVE \" ON \" TO Z-DMS-EXCEPT-LIT-ON.\n026244     IF Z-DMS-EXCEPT-DB EQUAL SPACES\n026246            MOVE SPACES TO Z-DMS-EXCEPT-LIT-OF\n026248     ELSE\n026250            MOVE \" OF \" TO Z-DMS-EXCEPT-LIT-OF.\n026252     MOVE \" (SUBCAT:\" TO Z-DMS-EXCEPT-LIT-SUBCAT.\n026254     MOVE DMSTATUS (DMERRORTYPE) TO Z-DMS-EXCEPT-SUBCAT.\n026256     MOVE \") AT \" TO Z-DMS-EXCEPT-LIT-AT.\n026258*\n026260     MOVE 1 TO Z-EDIT-ERROR-FLAG.\n026262     MOVE Z-DMS-EXCEPT-MSG TO Z-DISP-COMPACT-BUFFER.\n026264     MOVE 80 TO Z-DISP-SIZE.\n026266     PERFORM Z-DISP-COMPRESS THRU Z-DISP-COMPRESS-XIT.\n026268     MOVE Z-DISP-COMPACT-BUFFER TO Z-DMS-EXCEPT-MSG.\n026270     DISPLAY Z-DMS-EXCEPT-MSG.\n026272     DISPLAY \"DMSTRUCTURE: \", DMSTATUS(DMSTRUCTURE).\n026274     MOVE ZEROS TO Z-FLINFO-UPDATES.\n026276     IF  DMSTATUS (DEADLOCK) AND\n026278         DMSTATUS (DMERRORTYPE) = 3\n026280\n026282             CHANGE ATTRIBUTE STATUS OF MYSELF TO -1.\n026284*\n026286 Z-DMS-EXCEPTION-XIT.\n026288     EXIT.\n026290*\n026292**** DMS RELOCK\n026294* LDBSPCDB\n026296 Z-DMS1-RELOCK.\n026298     WAIT 2.\n026300*\n026302 Z-DMS1-RELOCK-XIT.\n026304     EXIT.\n026306*\n026308**** DMS CLEAR MODIFY FLAGS\n026310* LDBSPCDB\n026312 Z-DMS1-CLEAR-MODIFY-FLAGS.\n026314*\n026316 Z-DMS1-CLEAR-MODIFY-FLAGS-XIT.\n026318     EXIT.\n026320*\n026322**** DMS FREE\n026324* LDBSPCDB\n026326 Z-DMS1-FREE.\n026328     MOVE ZERO TO Z-DMS1-FOUND-LOCK.\n026330*\n026332 Z-DMS1-FREE-XIT.\n026334     EXIT.\n026336*\n026338**** DMS RELOCK\n026340* LDBTDADB\n026342 Z-DMS2-RELOCK.\n026344*\n026346     IF Z-DMS2-TRANS-STATE > 0\n026348         DISPLAY \">>>>>> ABORT PROGRAM: MINDISTCALC\"\n026350         DISPLAY \">>>>>> AFTER DEADLOCK\"\n026352         CHANGE ATTRIBUTE STATUS OF MYSELF TO -1.\n026354     WAIT 2.\n026356*\n026358 Z-DMS2-RELOCK-XIT.\n026360     EXIT.\n026362*\n026364**** DMS CLEAR MODIFY FLAGS\n026366* LDBTDADB\n026368 Z-DMS2-CLEAR-MODIFY-FLAGS.\n026370*\n026372 Z-DMS2-CLEAR-MODIFY-FLAGS-XIT.\n026374     EXIT.\n026376*\n026378**** DMS FREE\n026380* LDBTDADB\n026382 Z-DMS2-FREE.\n026384     MOVE ZERO TO Z-DMS2-FOUND-LOCK.\n026386*\n026388 Z-DMS2-FREE-XIT.\n026390     EXIT.\n026392*\n026394**** BEGIN TRANSACTION\n026396* LDBTDADB\n026398 Z-DMS2-BEGIN-TRANS.\n026400     MOVE 1 TO Z-DMS2-TRANS-STATE.\n026402     MOVE 0 TO Z-DMS2-ABORT-FLAG.\n026404     MOVE ZERO TO Z-DMS2-UPDATES.\n026406*    IF Z-DMS2-BT-TYPE = 0\n026408     BEGIN-TRANSACTION NO-AUDIT TDARESTART OF LDBTDADB\n026410         ON EXCEPTION\n026412            NEXT SENTENCE.\n026414*\n026416 Z-DMS2-CHECK-BT-EXCEPTION.\n026418*\n026420     IF DMSTATUS(DMERROR)\n026422         MOVE ZERO TO Z-DMS2-TRANS-STATE\n026424         IF DMSTATUS (ABORT)\n026426             MOVE 1 TO Z-DMS2-ABORT-FLAG\n026428             PERFORM Z-DMS2-FREE\n026430                 THRU Z-DMS2-FREE-XIT\n026432             GO TO Z-DMS2-BEGIN-TRANS-XIT\n026434         ELSE IF DMSTATUS (DEADLOCK)\n026436             PERFORM Z-DMS2-RELOCK\n026438                 THRU Z-DMS2-RELOCK-XIT\n026440             GO TO Z-DMS2-BEGIN-TRANS\n026442         ELSE\n026444             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n026446             MOVE \"TDARESTART OF LDBTDADB\" TO Z-DMS-EXCEPT-STR\n026448             MOVE ZEROS TO Z-DMS-EXCEPT-SEQ\n026450             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n026452*\n026454 Z-DMS2-BEGIN-TRANS-XIT.\n026456     EXIT.\n026458*\n026460**** END TRANSACTION\n026462* LDBTDADB\n026464 Z-DMS2-END-TRANS.\n026466*\n026468     MOVE ZERO TO Z-DMS2-FOUND-LOCK.\n026470     MOVE ZERO TO Z-DMS2-TRANS-STATE.\n026472     IF Z-DMS2-ET-TYPE = 4\n026474         GO TO Z-DMS2-ABORT-TRANS.\n026476     IF Z-DMS2-ET-TYPE = 2\n026478         GO TO Z-DMS2-END-TRANS-NO-AUDIT.\n026480     IF Z-DMS2-ET-TYPE = 1\n026482         GO TO Z-DMS2-END-TRANS-SYNC.\n026484*    IF Z-DMS2-ET-TYPE = 0  ***\n026486     END-TRANSACTION AUDIT TDARESTART OF LDBTDADB\n026488         ON EXCEPTION\n026490            NEXT SENTENCE.\n026492     GO TO Z-DMS2-CHECK-ET-EXCEPTION.\n026494*\n026496 Z-DMS2-END-TRANS-SYNC.\n026498*\n026500     END-TRANSACTION AUDIT TDARESTART OF LDBTDADB SYNC\n026502         ON EXCEPTION\n026504            NEXT SENTENCE.\n026506     GO TO Z-DMS2-CHECK-ET-EXCEPTION.\n026508*\n026510 Z-DMS2-END-TRANS-NO-AUDIT.\n026512*\n026514     END-TRANSACTION NO-AUDIT TDARESTART OF LDBTDADB\n026516         ON EXCEPTION\n026518            NEXT SENTENCE.\n026520     GO TO Z-DMS2-CHECK-ET-EXCEPTION.\n026522*\n026524 Z-DMS2-ABORT-TRANS.\n026526*\n026528     ABORT-TRANSACTION TDARESTART OF LDBTDADB\n026530         ON EXCEPTION\n026532            NEXT SENTENCE.\n026534*\n026536 Z-DMS2-CHECK-ET-EXCEPTION.\n026538*\n026540     IF DMSTATUS (DMERROR)\n026542         IF DMSTATUS (ABORT)\n026544             MOVE 1 TO Z-DMS2-ABORT-FLAG\n026546             PERFORM Z-DMS2-FREE\n026548                 THRU Z-DMS2-FREE-XIT\n026550             GO TO Z-DMS2-END-TRANS-XIT\n026552         ELSE IF DMSTATUS (DEADLOCK)\n026554             PERFORM Z-DMS2-RELOCK\n026556                 THRU Z-DMS2-RELOCK-XIT\n026558             PERFORM Z-DMS2-BEGIN-TRANS\n026560                 THRU Z-DMS2-BEGIN-TRANS-XIT\n026562             GO TO Z-DMS2-END-TRANS\n026564         ELSE\n026566             MOVE 1 TO Z-DMS2-TRANS-STATE\n026568             MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n026570             MOVE \"TDARESTART OF LDBTDADB\" TO Z-DMS-EXCEPT-STR\n026572             MOVE ZEROS TO Z-DMS-EXCEPT-SEQ\n026574             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT\n026576             IF Z-DMS2-UPDATES > ZERO\n026578                 DISPLAY \">>>>>> ABORT PROGRAM: MINDISTCALC\"\n026580                 DISPLAY \">>>>>> AT END TRANSACTION\"\n026582                      CHANGE ATTRIBUTE STATUS OF MYSELF TO -1.\n026584*\n026586     PERFORM Z-DMS2-CLEAR-MODIFY-FLAGS\n026588        THRU Z-DMS2-CLEAR-MODIFY-FLAGS-XIT.\n026590     MOVE ZERO TO Z-DMS2-ET-TYPE.\n026592*\n026594 Z-DMS2-END-TRANS-XIT.\n026596     EXIT.\n026598*\n026600 Z-DMS2-RESTART-CREATE.\n026602* LDBTDADB\n026604     CREATE TDARESTART OF LDBTDADB\n026606         ON EXCEPTION\n026608         MOVE \"TDARESTART OF LDBTDADB\" TO Z-DMS-EXCEPT-STR\n026610         MOVE \"LDBTDADB\" TO Z-DMS-EXCEPT-DB\n026612         MOVE ZERO TO Z-DMS-EXCEPT-SEQ\n026614         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.\n026616 Z-DMS2-RESTART-CREATE-XIT.\n026618     EXIT.\n026620*\n026622****\n026624 Z-CHECK-RESTART.\n026626*\n026628**** REPOSITION FILES\n026630*\n026632     IF Z-RESTART-PROCESS = 0 AND Z-RUNNING-FLAG = 1\n026634         PERFORM Z-CLOSE-DB-1\n026636         PERFORM Z-OPEN-DB-1\n026638         PERFORM Z-CLOSE-DB-2\n026640         PERFORM Z-OPEN-DB-2 .\n026642     IF Z-RPTINFO1-RS-OPEN = 0\n026644         IF Z-RPTINFO1-OPEN = 0\n026646             GO TO Z-RESTART-REPORT1-DONE\n026648         ELSE\n026650             CLOSE LISTING\n026652             MOVE 0 TO Z-RPTINFO1-OPEN\n026654             GO TO Z-RESTART-REPORT1-DONE.\n026656     IF Z-RPTINFO1-OPEN = 0\n026658         OPEN OUTPUT LISTING\n026660         MOVE 3 TO Z-RPTINFO1-OPEN.\n026662     MOVE \"RESTARTED\" TO Z-RPT-1-BUFFER.\n026664     WRITE Z-RPT-1-BUFFER AFTER ADVANCING PAGE.\n026666     MOVE SPACES TO Z-RPT-1-BUFFER.\n026668     WRITE Z-RPT-1-BUFFER AFTER ADVANCING PAGE.\n026670     WRITE Z-RPT-1-BUFFER\n026672         AFTER ADVANCING Z-RPT-1-LINE LINES.\n026674 Z-RESTART-REPORT1-DONE.\n026676     IF Z-RPTINFO2-RS-OPEN = 0\n026678         IF Z-RPTINFO2-OPEN = 0\n026680             GO TO Z-RESTART-REPORT2-DONE\n026682         ELSE\n026684             CLOSE FICHE\n026686             MOVE 0 TO Z-RPTINFO2-OPEN\n026688             GO TO Z-RESTART-REPORT2-DONE.\n026690     IF Z-RPTINFO2-OPEN = 0\n026692         OPEN OUTPUT FICHE\n026694         MOVE 3 TO Z-RPTINFO2-OPEN.\n026696     MOVE \"RESTARTED\" TO Z-RPT-2-BUFFER.\n026698     WRITE Z-RPT-2-BUFFER AFTER ADVANCING PAGE.\n026700     MOVE SPACES TO Z-RPT-2-BUFFER.\n026702     WRITE Z-RPT-2-BUFFER AFTER ADVANCING PAGE.\n026704     WRITE Z-RPT-2-BUFFER\n026706         AFTER ADVANCING Z-RPT-2-LINE LINES.\n026708 Z-RESTART-REPORT2-DONE.\n026710 Z-CHECK-RESTART-XIT.\n026712     EXIT.\n026714*\n026716**** DISPLAY COMPRESS\n026718*\n026720 Z-DISP-COMPRESS.\n026722     MOVE Z-DISP-COMPACT-BUFFER TO Z-LALPHA-1.\n026724     MOVE SPACES TO Z-LALPHA-2.\n026726     CALL \"XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY\" USING            \n026728         Z-LALPHA-1, Z-LALPHA-2, Z-STR-INT-ONE, Z-DISP-SIZE,      \n026730         Z-STR-INT-ZERO, Z-STR-INT-ONE, Z-STR-INT-ONE,            \n026732         Z-STR-INT-ZERO.\n026734     MOVE Z-LALPHA-1 TO Z-DISP-COMPACT-BUFFER.\n026736 Z-DISP-COMPRESS-XIT.\n026738     EXIT.\n026740*\n026742 Z-DATE-CALC-T.\n026744     ADD Z-DATE-TT-1 TO Z-DATE-T.\n026746     IF Z-DATE-T > +99 OR Z-DATE-T < -99\n026748         DIVIDE Z-DATE-T BY +100 GIVING Z-DATE-S\n026750         REMAINDER Z-DATE-T.\n026752     MOVE Z-DATE-T TO Z-DATE-TT-1.\n026754     IF Z-DATE-TT-1 < ZERO\n026756         ADD +100 TO Z-DATE-TT-1\n026758         SUBTRACT +1 FROM Z-DATE-S.\n026760*\n026762 Z-DATE-CALC-T-EXIT.\n026764     EXIT.\n026766*\n026768 Z-DATE-CALC-S.\n026770     ADD Z-DATE-SS-1 TO Z-DATE-S.\n026772     IF Z-DATE-S > +59 OR Z-DATE-S < -59\n026774         DIVIDE Z-DATE-S BY +60 GIVING Z-DATE-U\n026776         REMAINDER Z-DATE-S.\n026778     MOVE Z-DATE-S TO Z-DATE-SS-1.\n026780     IF Z-DATE-SS-1 < ZERO\n026782         ADD +60 TO Z-DATE-SS-1\n026784         SUBTRACT +1 FROM Z-DATE-U.\n026786*\n026788 Z-DATE-CALC-S-EXIT.\n026790     EXIT.\n026792*\n026794 Z-DATE-CALC-U.\n026796     ADD Z-DATE-UU-1 TO Z-DATE-U.\n026798     IF Z-DATE-U > +59 OR  Z-DATE-U < -59\n026800         DIVIDE Z-DATE-U BY +60 GIVING Z-DATE-Z\n026802             REMAINDER Z-DATE-U.\n026804     MOVE Z-DATE-U TO Z-DATE-UU-1.\n026806     IF Z-DATE-UU-1 < ZERO\n026808         ADD +60 TO Z-DATE-UU-1\n026810         SUBTRACT +1 FROM Z-DATE-Z.\n026812*\n026814 Z-DATE-CALC-U-EXIT.\n026816     EXIT.\n026818*\n026820 Z-DATE-CALC-Z.\n026822     ADD Z-DATE-ZZ-1 TO Z-DATE-Z.\n026824     IF Z-DATE-Z > +23 OR Z-DATE-Z < -23\n026826         DIVIDE Z-DATE-Z BY +24 GIVING Z-DATE-D\n026828         REMAINDER Z-DATE-Z.\n026830     MOVE Z-DATE-Z TO Z-DATE-ZZ-1.\n026832     IF Z-DATE-ZZ-1 < ZERO\n026834         ADD +24 TO Z-DATE-ZZ-1\n026836         SUBTRACT +1 FROM Z-DATE-D.\n026838*\n026840 Z-DATE-CALC-Z-EXIT.\n026842     EXIT.\n026844*\n026846 Z-DATE-CNVRT-WEEKS-TO-DD.\n026848     MULTIPLY  Z-DATE-W BY +7 GIVING Z-DATE-D.\n026850*\n026852 Z-DATE-CNVRT-WEEKS-TO-DD-EXIT.\n026854     EXIT.\n026856*\n026858 Z-DATE-CALC-D.\n026860     IF Z-DATE-D > ZERO\n026862         PERFORM Z-DATE-CALC-LEAP-YEAR\n026864            THRU Z-DATE-CALC-LEAP-YEAR-EXIT\n026866         PERFORM Z-DATE-CALC-MONTH-DAYS\n026868            THRU Z-DATE-CALC-MONTH-DAYS-EXIT\n026870         PERFORM Z-DATE-ADD-1ST-YR\n026872            THRU Z-DATE-ADD-1ST-YR-EXIT\n026874         PERFORM Z-DATE-ADD-D\n026876            THRU Z-DATE-ADD-D-EXIT\n026878           UNTIL Z-DATE-D = ZEROS\n026880     ELSE\n026882         PERFORM Z-DATE-SUBTRACT-1ST-YR\n026884            THRU Z-DATE-SUBTRACT-1ST-YR-EXIT\n026886         PERFORM Z-DATE-SUBTRACT-D\n026888            THRU Z-DATE-SUBTRACT-D-EXIT\n026890           UNTIL Z-DATE-D = ZEROS.\n026892     MOVE ZEROS TO Z-DATE-C.\n026894     MOVE ZEROS TO Z-DATE-Y.\n026896     MOVE ZEROS TO Z-DATE-M.\n026898*\n026900 Z-DATE-CALC-D-EXIT.\n026902     EXIT.\n026904*\n026906 Z-DATE-ADD-1ST-YR.\n026908     ADD Z-DATE-JJJ-1, Z-DATE-D GIVING Z-DATE-UNITS-WORK.\n026910     IF Z-DATE-LEAP-YEAR\n026912         IF Z-DATE-UNITS-WORK NOT > +366\n026914             MOVE Z-DATE-UNITS-WORK TO Z-DATE-JJJ-1\n026916             MOVE ZEROS TO Z-DATE-D\n026918         ELSE\n026920             SUBTRACT Z-DATE-JJJ-1 FROM +366\n026922               GIVING Z-DATE-UNITS-WORK\n026924             SUBTRACT Z-DATE-UNITS-WORK FROM Z-DATE-D\n026926             PERFORM Z-DATE-INCREMENT-YY-CC\n026928                THRU Z-DATE-INCREMENT-YY-CC-EXIT\n026930             PERFORM Z-DATE-CALC-LEAP-YEAR\n026932                THRU Z-DATE-CALC-LEAP-YEAR-EXIT\n026934             PERFORM Z-DATE-CALC-MONTH-DAYS\n026936                THRU Z-DATE-CALC-MONTH-DAYS-EXIT\n026938     ELSE\n026940         IF Z-DATE-UNITS-WORK NOT > +365\n026942             MOVE Z-DATE-UNITS-WORK TO Z-DATE-JJJ-1\n026944             MOVE ZEROS TO Z-DATE-D\n026946         ELSE\n026948             SUBTRACT Z-DATE-JJJ-1 FROM +365\n026950               GIVING Z-DATE-UNITS-WORK\n026952             SUBTRACT Z-DATE-UNITS-WORK FROM Z-DATE-D\n026954             PERFORM Z-DATE-INCREMENT-YY-CC\n026956                THRU Z-DATE-INCREMENT-YY-CC-EXIT\n026958             PERFORM Z-DATE-CALC-LEAP-YEAR\n026960                THRU Z-DATE-CALC-LEAP-YEAR-EXIT\n026962             PERFORM Z-DATE-CALC-MONTH-DAYS\n026964                THRU Z-DATE-CALC-MONTH-DAYS-EXIT.\n026966*\n026968 Z-DATE-ADD-1ST-YR-EXIT.\n026970     EXIT.\n026972*\n026974 Z-DATE-SUBTRACT-1ST-YR.\n026976     ADD Z-DATE-JJJ-1, Z-DATE-D GIVING Z-DATE-UNITS-WORK.\n026978     IF Z-DATE-UNITS-WORK > ZEROS\n026980         ADD Z-DATE-D TO Z-DATE-JJJ-1\n026982         MOVE  ZEROS TO Z-DATE-D\n026984     ELSE\n026986         ADD Z-DATE-JJJ-1 TO Z-DATE-D\n026988         PERFORM Z-DATE-DECREMENT-YY-CC\n026990             THRU Z-DATE-DECREMENT-YY-CC-EXIT\n026992         PERFORM Z-DATE-CALC-LEAP-YEAR\n026994             THRU Z-DATE-CALC-LEAP-YEAR-EXIT\n026996         PERFORM Z-DATE-CALC-MONTH-DAYS\n026998             THRU Z-DATE-CALC-MONTH-DAYS-EXIT\n027000         IF Z-DATE-LEAP-YEAR\n027002             ADD Z-DATE-UNITS-WORK, 366 GIVING\n027004                 Z-DATE-JJJ-1\n027006         ELSE\n027008             ADD Z-DATE-UNITS-WORK, 365 GIVING\n027010                 Z-DATE-JJJ-1.\n027012 Z-DATE-SUBTRACT-1ST-YR-EXIT.\n027014     EXIT.\n027016*\n027018 Z-DATE-ADD-D.\n027020     IF Z-DATE-LEAP-YEAR\n027022         IF Z-DATE-D > +366\n027024             SUBTRACT +366 FROM Z-DATE-D\n027026             PERFORM Z-DATE-INCREMENT-YY-CC\n027028                THRU Z-DATE-INCREMENT-YY-CC-EXIT\n027030             PERFORM Z-DATE-CALC-LEAP-YEAR\n027032                THRU Z-DATE-CALC-LEAP-YEAR-EXIT\n027034             PERFORM Z-DATE-CALC-MONTH-DAYS\n027036                THRU Z-DATE-CALC-MONTH-DAYS-EXIT\n027038         ELSE\n027040             MOVE Z-DATE-D TO Z-DATE-JJJ-1\n027042             MOVE ZEROS TO Z-DATE-D\n027044     ELSE\n027046         IF Z-DATE-D > +365\n027048             SUBTRACT +365 FROM Z-DATE-D\n027050             PERFORM Z-DATE-INCREMENT-YY-CC\n027052                THRU Z-DATE-INCREMENT-YY-CC-EXIT\n027054             PERFORM Z-DATE-CALC-LEAP-YEAR\n027056                THRU Z-DATE-CALC-LEAP-YEAR-EXIT\n027058             PERFORM Z-DATE-CALC-MONTH-DAYS\n027060                THRU Z-DATE-CALC-MONTH-DAYS-EXIT\n027062         ELSE\n027064             MOVE Z-DATE-D TO Z-DATE-JJJ-1\n027066             MOVE ZEROS TO Z-DATE-D.\n027068 Z-DATE-ADD-D-EXIT.\n027070     EXIT.\n027072*\n027074 Z-DATE-INCREMENT-YY-CC.\n027076     IF Z-DATE-YY-1 < 99\n027078         ADD +1 TO Z-DATE-YY-1\n027080     ELSE\n027082         MOVE ZEROS TO Z-DATE-YY-1\n027084         ADD +1 TO Z-DATE-CC-1.\n027086 Z-DATE-INCREMENT-YY-CC-EXIT.\n027088     EXIT.\n027090*\n027092 Z-DATE-SUBTRACT-D.\n027094     IF Z-DATE-LEAP-YEAR\n027096         IF Z-DATE-D NOT > -366\n027098             ADD +366 TO Z-DATE-D\n027100             IF Z-DATE-D = ZEROS\n027102                 PERFORM Z-DATE-DECREMENT-YY-CC\n027104                    THRU Z-DATE-DECREMENT-YY-CC-EXIT\n027106                 MOVE +365 TO Z-DATE-JJJ-1\n027108             ELSE\n027110                 PERFORM Z-DATE-DECREMENT-YY-CC\n027112                    THRU Z-DATE-DECREMENT-YY-CC-EXIT\n027114                 PERFORM Z-DATE-CALC-LEAP-YEAR\n027116                    THRU Z-DATE-CALC-LEAP-YEAR-EXIT\n027118                 PERFORM Z-DATE-CALC-MONTH-DAYS\n027120                    THRU Z-DATE-CALC-MONTH-DAYS-EXIT\n027122         ELSE\n027124             COMPUTE Z-DATE-JJJ-1 = Z-DATE-D + 366\n027126             MOVE ZEROS TO Z-DATE-D\n027128     ELSE\n027130         IF Z-DATE-D NOT > -365\n027132             ADD +365 TO Z-DATE-D\n027134             IF Z-DATE-D = ZEROS\n027136                 PERFORM Z-DATE-DECREMENT-YY-CC\n027138                    THRU Z-DATE-DECREMENT-YY-CC-EXIT\n027140                 PERFORM Z-DATE-CALC-LEAP-YEAR\n027142                    THRU Z-DATE-CALC-LEAP-YEAR-EXIT\n027144                 PERFORM Z-DATE-CALC-MONTH-DAYS\n027146                    THRU Z-DATE-CALC-MONTH-DAYS-EXIT\n027148                 MOVE ZEROS TO Z-DATE-JJJ-1\n027150                 IF Z-DATE-LEAP-YEAR\n027152                     ADD +366 TO Z-DATE-JJJ-1\n027154                 ELSE\n027156                     ADD +365 TO Z-DATE-JJJ-1\n027158             ELSE\n027160                 PERFORM Z-DATE-DECREMENT-YY-CC\n027162                    THRU Z-DATE-DECREMENT-YY-CC-EXIT\n027164                 PERFORM Z-DATE-CALC-LEAP-YEAR\n027166                    THRU Z-DATE-CALC-LEAP-YEAR-EXIT\n027168                 PERFORM Z-DATE-CALC-MONTH-DAYS\n027170                    THRU Z-DATE-CALC-MONTH-DAYS-EXIT\n027172         ELSE\n027174             COMPUTE Z-DATE-JJJ-1 = Z-DATE-D + 365\n027176             MOVE ZEROS TO Z-DATE-D.\n027178 Z-DATE-SUBTRACT-D-EXIT.\n027180     EXIT.\n027182*\n027184 Z-DATE-DECREMENT-YY-CC.\n027186     IF Z-DATE-YY-1 > 0\n027188         SUBTRACT +1 FROM Z-DATE-YY-1\n027190     ELSE\n027192         MOVE +99 TO Z-DATE-YY-1\n027194         SUBTRACT +1 FROM Z-DATE-CC-1.\n027196 Z-DATE-DECREMENT-YY-CC-EXIT.\n027198     EXIT.\n027200*\n027202 Z-DATE-CALC-M.\n027204     IF Z-DATE-M > ZERO\n027206         PERFORM Z-DATE-ADD-M\n027208            THRU Z-DATE-ADD-M-EXIT\n027210     ELSE\n027212         PERFORM Z-DATE-SUBTRACT-M\n027214            THRU Z-DATE-SUBTRACT-M-EXIT.\n027216 Z-DATE-CALC-M-EXIT.\n027218     EXIT.\n027220*\n027222 Z-DATE-ADD-M.\n027224     IF Z-DATE-M > +11\n027226         DIVIDE Z-DATE-M BY +12 GIVING Z-DATE-Y\n027228             REMAINDER Z-DATE-M\n027230         ADD Z-DATE-MM-1 TO Z-DATE-M\n027232         IF Z-DATE-M > +12\n027234             DIVIDE Z-DATE-M BY +12 GIVING Z-DATE-UNITS-WORK\n027236                 REMAINDER Z-DATE-M\n027238             ADD Z-DATE-UNITS-WORK TO Z-DATE-Y\n027240             MOVE Z-DATE-M TO Z-DATE-MM-1\n027242         ELSE\n027244             MOVE Z-DATE-M TO Z-DATE-MM-1\n027246     ELSE\n027248         ADD Z-DATE-MM-1 TO Z-DATE-M\n027250         IF Z-DATE-M > +12\n027252             DIVIDE Z-DATE-M BY +12 GIVING Z-DATE-Y\n027254                 REMAINDER Z-DATE-M\n027256             MOVE Z-DATE-M TO Z-DATE-MM-1\n027258         ELSE\n027260             MOVE Z-DATE-M TO Z-DATE-MM-1.\n027262 Z-DATE-ADD-M-EXIT.\n027264     EXIT.\n027266*\n027268 Z-DATE-SUBTRACT-M.\n027270     IF Z-DATE-M < -12\n027272         DIVIDE Z-DATE-M BY +12 GIVING Z-DATE-Y\n027274             REMAINDER Z-DATE-M\n027276         ADD Z-DATE-MM-1 TO Z-DATE-M\n027278         IF Z-DATE-M < +1\n027280             ADD +12 TO Z-DATE-M\n027282             SUBTRACT +1 FROM Z-DATE-Y\n027284             MOVE Z-DATE-M TO Z-DATE-MM-1\n027286         ELSE\n027288             MOVE Z-DATE-M TO Z-DATE-MM-1\n027290     ELSE\n027292         ADD Z-DATE-MM-1 TO Z-DATE-M\n027294         IF Z-DATE-M < +1\n027296             ADD +12 TO Z-DATE-M\n027298             SUBTRACT +1 FROM Z-DATE-Y\n027300             MOVE Z-DATE-M TO Z-DATE-MM-1\n027302         ELSE\n027304             MOVE Z-DATE-M TO Z-DATE-MM-1.\n027306*\n027308 Z-DATE-SUBTRACT-M-EXIT.\n027310     EXIT.\n027312*\n027314 Z-DATE-CALC-Y.\n027316     ADD Z-DATE-YY-1 TO Z-DATE-Y.\n027318     IF Z-DATE-Y > +99 OR Z-DATE-Y < -99\n027320         DIVIDE Z-DATE-Y BY +100 GIVING Z-DATE-C\n027322             REMAINDER Z-DATE-Y.\n027324     MOVE Z-DATE-Y TO Z-DATE-YY-1.\n027326     IF Z-DATE-YY-1 < ZERO\n027328         ADD +100 TO Z-DATE-YY-1\n027330         SUBTRACT +1 FROM Z-DATE-C.\n027332*\n027334 Z-DATE-CALC-Y-EXIT.\n027336     EXIT.\n027338*\n027340 Z-DATE-CALC-C.\n027342     ADD Z-DATE-CC-1 TO Z-DATE-C.\n027344     MOVE Z-DATE-C TO Z-DATE-CC-1.\n027346*\n027348 Z-DATE-CALC-C-EXIT.\n027350     EXIT.\n027352*\n```\n\n\u26a0\ufe0f  This is the source code you must document.\n    633 lines from 13040 to 13672.\n    Refer to the template instructions for complete requirements.\n", "chunk_number": 28, "total_chunks": 55, "start_line": 13040, "end_line": 13672, "line_count": 633}

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
- Source code length: 27792 characters

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
CHUNK 28 of 55 - TDAS-MINDISTCALC.c74
=============================================================================
Lines: 13040 to 13672 (633 lines)
Chunk Tokens (estimated): ~7,906
Actual Input Tokens: 9,312 (measured with tiktoken)

⚠️  MANDATORY ACCOUNTABILITY REQUIREMENTS:
1. Document EVERY paragraph within lines 13040-13672 sequentially
2. Start each entry with: "Block N: PARAGRAPH-NAME (Line X)"
3. Process blocks in strict sequential order by line number
4. At the end, provide completion checklist with ALL paragraphs documented
5. Missing line numbers will make skipped content immediately obvious
6. NO SUMMARIZATION - Show complete code for each block

CHUNK PROCESSING RULES:
- This is chunk 28 of 55 chunks
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
      The source code below is only CHUNK 28 of 55.


=============================================================================
CHUNK 28 SOURCE CODE (Lines 13040-13672)
=============================================================================

```cobol
026088 Z-FL-EXCEPTION.
026090     IF Z-FILE-EOF
026092         MOVE "END OF FILE" TO Z-FL-EXCEPT-ERR
026094     ELSE IF Z-FILE-DUPLICATES
026096         MOVE "DUPLICATES" TO Z-FL-EXCEPT-ERR
026098     ELSE IF Z-FILE-NOTFOUND
026100         MOVE "NOT FOUND" TO Z-FL-EXCEPT-ERR
026102     ELSE IF Z-FILE-BOUNDARY
026104         MOVE "BOUNDARY ERROR" TO Z-FL-EXCEPT-ERR
026106     ELSE
026108         MOVE "I-O ERROR" TO Z-FL-EXCEPT-ERR.
026110*
026112     MOVE "(" TO Z-FL-EXCEPT-LIT-PARN.
026114     MOVE ") ON FILE " TO Z-FL-EXCEPT-LIT-ON.
026116     MOVE " AT " TO Z-FL-EXCEPT-LIT-AT.
026118*
026120     MOVE 1 TO Z-EDIT-ERROR-FLAG.
026122     MOVE Z-FL-EXCEPT-MSG TO Z-DISP-COMPACT-BUFFER
026124     MOVE 80 TO Z-DISP-SIZE
026126     PERFORM Z-DISP-COMPRESS THRU Z-DISP-COMPRESS-XIT
026128     MOVE Z-DISP-COMPACT-BUFFER TO Z-FL-EXCEPT-MSG
026130     DISPLAY Z-FL-EXCEPT-MSG.
026132     IF  Z-FL-EXCEPT-TITLE NOT EQUAL SPACES
026134         STRING ">>> TITLE :" DELIMITED BY SIZE,
026136                Z-FL-EXCEPT-TITLE DELIMITED BY SIZE
026138          INTO Z-FL-EXCEPT-MSG
026140         DISPLAY Z-FL-EXCEPT-MSG.
026142     MOVE SPACES TO Z-FL-EXCEPT-TITLE.
026144     MOVE ZEROS TO Z-FLINFO-UPDATES.
026146*
026148 Z-FL-EXCEPTION-XIT.
026150     EXIT.
026152*
026154**** DATABASE EXCEPTION
026156*
026158 Z-DMS-EXCEPTION.
026160     MOVE "DMS " TO Z-DMS-EXCEPT-LIT-DMS.
026162     MOVE "ERROR (CAT:  )" TO Z-DMS-EXCEPT-CAT.
026164     MOVE DMSTATUS (DMCATEGORY) TO Z-DMS-EXCEPT-CAT-NO.
026166     IF DMSTATUS (NOTFOUND)
026168            MOVE "NOTFOUND" TO Z-DMS-EXCEPT-CAT.
026170     IF DMSTATUS (NORECORD)
026172            MOVE "NORECORD" TO Z-DMS-EXCEPT-CAT.
026174     IF DMSTATUS (DUPLICATES)
026176            MOVE "DUPLICATES" TO Z-DMS-EXCEPT-CAT.
026178     IF DMSTATUS (DEADLOCK)
026180            MOVE "DEADLOCK" TO Z-DMS-EXCEPT-CAT.
026182     IF DMSTATUS (DATAERROR)
026184            MOVE "DATAERROR" TO Z-DMS-EXCEPT-CAT.
026186     IF DMSTATUS (NOTLOCKED)
026188            MOVE "NOTLOCKED" TO Z-DMS-EXCEPT-CAT.
026190     IF DMSTATUS (KEYCHANGED)
026192            MOVE "KEYCHANGED" TO Z-DMS-EXCEPT-CAT.
026194     IF DMSTATUS (SYSTEMERROR)
026196            MOVE "SYSTEMERROR" TO Z-DMS-EXCEPT-CAT.
026198     IF DMSTATUS (READONLY)
026200            MOVE "READONLY" TO Z-DMS-EXCEPT-CAT.
026202     IF DMSTATUS (IOERROR)
026204            MOVE "IOERROR" TO Z-DMS-EXCEPT-CAT.
026206     IF DMSTATUS (LIMITERROR)
026208            MOVE "LIMITERROR" TO Z-DMS-EXCEPT-CAT.
026210     IF DMSTATUS (OPENERROR)
026212            MOVE "OPENERROR" TO Z-DMS-EXCEPT-CAT.
026214     IF DMSTATUS (CLOSEERROR)
026216            MOVE "CLOSEERROR" TO Z-DMS-EXCEPT-CAT.
026218     IF DMSTATUS (NORECORD)
026220            MOVE "NORECORD" TO Z-DMS-EXCEPT-CAT.
026222     IF DMSTATUS (INUSE)
026224            MOVE "INUSE" TO Z-DMS-EXCEPT-CAT.
026226     IF DMSTATUS (AUDITERROR)
026228            MOVE "AUDITERROR" TO Z-DMS-EXCEPT-CAT.
026230     IF DMSTATUS (ABORT)
026232            MOVE "ABORT" TO Z-DMS-EXCEPT-CAT.
026234     IF DMSTATUS (SECURITYERROR)
026236            MOVE "SECURITYERROR" TO Z-DMS-EXCEPT-CAT.
026238     IF DMSTATUS (VERSIONERROR)
026240            MOVE "VERSIONERROR" TO Z-DMS-EXCEPT-CAT.
026242     MOVE " ON " TO Z-DMS-EXCEPT-LIT-ON.
026244     IF Z-DMS-EXCEPT-DB EQUAL SPACES
026246            MOVE SPACES TO Z-DMS-EXCEPT-LIT-OF
026248     ELSE
026250            MOVE " OF " TO Z-DMS-EXCEPT-LIT-OF.
026252     MOVE " (SUBCAT:" TO Z-DMS-EXCEPT-LIT-SUBCAT.
026254     MOVE DMSTATUS (DMERRORTYPE) TO Z-DMS-EXCEPT-SUBCAT.
026256     MOVE ") AT " TO Z-DMS-EXCEPT-LIT-AT.
026258*
026260     MOVE 1 TO Z-EDIT-ERROR-FLAG.
026262     MOVE Z-DMS-EXCEPT-MSG TO Z-DISP-COMPACT-BUFFER.
026264     MOVE 80 TO Z-DISP-SIZE.
026266     PERFORM Z-DISP-COMPRESS THRU Z-DISP-COMPRESS-XIT.
026268     MOVE Z-DISP-COMPACT-BUFFER TO Z-DMS-EXCEPT-MSG.
026270     DISPLAY Z-DMS-EXCEPT-MSG.
026272     DISPLAY "DMSTRUCTURE: ", DMSTATUS(DMSTRUCTURE).
026274     MOVE ZEROS TO Z-FLINFO-UPDATES.
026276     IF  DMSTATUS (DEADLOCK) AND
026278         DMSTATUS (DMERRORTYPE) = 3
026280
026282             CHANGE ATTRIBUTE STATUS OF MYSELF TO -1.
026284*
026286 Z-DMS-EXCEPTION-XIT.
026288     EXIT.
026290*
026292**** DMS RELOCK
026294* LDBSPCDB
026296 Z-DMS1-RELOCK.
026298     WAIT 2.
026300*
026302 Z-DMS1-RELOCK-XIT.
026304     EXIT.
026306*
026308**** DMS CLEAR MODIFY FLAGS
026310* LDBSPCDB
026312 Z-DMS1-CLEAR-MODIFY-FLAGS.
026314*
026316 Z-DMS1-CLEAR-MODIFY-FLAGS-XIT.
026318     EXIT.
026320*
026322**** DMS FREE
026324* LDBSPCDB
026326 Z-DMS1-FREE.
026328     MOVE ZERO TO Z-DMS1-FOUND-LOCK.
026330*
026332 Z-DMS1-FREE-XIT.
026334     EXIT.
026336*
026338**** DMS RELOCK
026340* LDBTDADB
026342 Z-DMS2-RELOCK.
026344*
026346     IF Z-DMS2-TRANS-STATE > 0
026348         DISPLAY ">>>>>> ABORT PROGRAM: MINDISTCALC"
026350         DISPLAY ">>>>>> AFTER DEADLOCK"
026352         CHANGE ATTRIBUTE STATUS OF MYSELF TO -1.
026354     WAIT 2.
026356*
026358 Z-DMS2-RELOCK-XIT.
026360     EXIT.
026362*
026364**** DMS CLEAR MODIFY FLAGS
026366* LDBTDADB
026368 Z-DMS2-CLEAR-MODIFY-FLAGS.
026370*
026372 Z-DMS2-CLEAR-MODIFY-FLAGS-XIT.
026374     EXIT.
026376*
026378**** DMS FREE
026380* LDBTDADB
026382 Z-DMS2-FREE.
026384     MOVE ZERO TO Z-DMS2-FOUND-LOCK.
026386*
026388 Z-DMS2-FREE-XIT.
026390     EXIT.
026392*
026394**** BEGIN TRANSACTION
026396* LDBTDADB
026398 Z-DMS2-BEGIN-TRANS.
026400     MOVE 1 TO Z-DMS2-TRANS-STATE.
026402     MOVE 0 TO Z-DMS2-ABORT-FLAG.
026404     MOVE ZERO TO Z-DMS2-UPDATES.
026406*    IF Z-DMS2-BT-TYPE = 0
026408     BEGIN-TRANSACTION NO-AUDIT TDARESTART OF LDBTDADB
026410         ON EXCEPTION
026412            NEXT SENTENCE.
026414*
026416 Z-DMS2-CHECK-BT-EXCEPTION.
026418*
026420     IF DMSTATUS(DMERROR)
026422         MOVE ZERO TO Z-DMS2-TRANS-STATE
026424         IF DMSTATUS (ABORT)
026426             MOVE 1 TO Z-DMS2-ABORT-FLAG
026428             PERFORM Z-DMS2-FREE
026430                 THRU Z-DMS2-FREE-XIT
026432             GO TO Z-DMS2-BEGIN-TRANS-XIT
026434         ELSE IF DMSTATUS (DEADLOCK)
026436             PERFORM Z-DMS2-RELOCK
026438                 THRU Z-DMS2-RELOCK-XIT
026440             GO TO Z-DMS2-BEGIN-TRANS
026442         ELSE
026444             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
026446             MOVE "TDARESTART OF LDBTDADB" TO Z-DMS-EXCEPT-STR
026448             MOVE ZEROS TO Z-DMS-EXCEPT-SEQ
026450             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
026452*
026454 Z-DMS2-BEGIN-TRANS-XIT.
026456     EXIT.
026458*
026460**** END TRANSACTION
026462* LDBTDADB
026464 Z-DMS2-END-TRANS.
026466*
026468     MOVE ZERO TO Z-DMS2-FOUND-LOCK.
026470     MOVE ZERO TO Z-DMS2-TRANS-STATE.
026472     IF Z-DMS2-ET-TYPE = 4
026474         GO TO Z-DMS2-ABORT-TRANS.
026476     IF Z-DMS2-ET-TYPE = 2
026478         GO TO Z-DMS2-END-TRANS-NO-AUDIT.
026480     IF Z-DMS2-ET-TYPE = 1
026482         GO TO Z-DMS2-END-TRANS-SYNC.
026484*    IF Z-DMS2-ET-TYPE = 0  ***
026486     END-TRANSACTION AUDIT TDARESTART OF LDBTDADB
026488         ON EXCEPTION
026490            NEXT SENTENCE.
026492     GO TO Z-DMS2-CHECK-ET-EXCEPTION.
026494*
026496 Z-DMS2-END-TRANS-SYNC.
026498*
026500     END-TRANSACTION AUDIT TDARESTART OF LDBTDADB SYNC
026502         ON EXCEPTION
026504            NEXT SENTENCE.
026506     GO TO Z-DMS2-CHECK-ET-EXCEPTION.
026508*
026510 Z-DMS2-END-TRANS-NO-AUDIT.
026512*
026514     END-TRANSACTION NO-AUDIT TDARESTART OF LDBTDADB
026516         ON EXCEPTION
026518            NEXT SENTENCE.
026520     GO TO Z-DMS2-CHECK-ET-EXCEPTION.
026522*
026524 Z-DMS2-ABORT-TRANS.
026526*
026528     ABORT-TRANSACTION TDARESTART OF LDBTDADB
026530         ON EXCEPTION
026532            NEXT SENTENCE.
026534*
026536 Z-DMS2-CHECK-ET-EXCEPTION.
026538*
026540     IF DMSTATUS (DMERROR)
026542         IF DMSTATUS (ABORT)
026544             MOVE 1 TO Z-DMS2-ABORT-FLAG
026546             PERFORM Z-DMS2-FREE
026548                 THRU Z-DMS2-FREE-XIT
026550             GO TO Z-DMS2-END-TRANS-XIT
026552         ELSE IF DMSTATUS (DEADLOCK)
026554             PERFORM Z-DMS2-RELOCK
026556                 THRU Z-DMS2-RELOCK-XIT
026558             PERFORM Z-DMS2-BEGIN-TRANS
026560                 THRU Z-DMS2-BEGIN-TRANS-XIT
026562             GO TO Z-DMS2-END-TRANS
026564         ELSE
026566             MOVE 1 TO Z-DMS2-TRANS-STATE
026568             MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
026570             MOVE "TDARESTART OF LDBTDADB" TO Z-DMS-EXCEPT-STR
026572             MOVE ZEROS TO Z-DMS-EXCEPT-SEQ
026574             PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT
026576             IF Z-DMS2-UPDATES > ZERO
026578                 DISPLAY ">>>>>> ABORT PROGRAM: MINDISTCALC"
026580                 DISPLAY ">>>>>> AT END TRANSACTION"
026582                      CHANGE ATTRIBUTE STATUS OF MYSELF TO -1.
026584*
026586     PERFORM Z-DMS2-CLEAR-MODIFY-FLAGS
026588        THRU Z-DMS2-CLEAR-MODIFY-FLAGS-XIT.
026590     MOVE ZERO TO Z-DMS2-ET-TYPE.
026592*
026594 Z-DMS2-END-TRANS-XIT.
026596     EXIT.
026598*
026600 Z-DMS2-RESTART-CREATE.
026602* LDBTDADB
026604     CREATE TDARESTART OF LDBTDADB
026606         ON EXCEPTION
026608         MOVE "TDARESTART OF LDBTDADB" TO Z-DMS-EXCEPT-STR
026610         MOVE "LDBTDADB" TO Z-DMS-EXCEPT-DB
026612         MOVE ZERO TO Z-DMS-EXCEPT-SEQ
026614         PERFORM Z-DMS-EXCEPTION THRU Z-DMS-EXCEPTION-XIT.
026616 Z-DMS2-RESTART-CREATE-XIT.
026618     EXIT.
026620*
026622****
026624 Z-CHECK-RESTART.
026626*
026628**** REPOSITION FILES
026630*
026632     IF Z-RESTART-PROCESS = 0 AND Z-RUNNING-FLAG = 1
026634         PERFORM Z-CLOSE-DB-1
026636         PERFORM Z-OPEN-DB-1
026638         PERFORM Z-CLOSE-DB-2
026640         PERFORM Z-OPEN-DB-2 .
026642     IF Z-RPTINFO1-RS-OPEN = 0
026644         IF Z-RPTINFO1-OPEN = 0
026646             GO TO Z-RESTART-REPORT1-DONE
026648         ELSE
026650             CLOSE LISTING
026652             MOVE 0 TO Z-RPTINFO1-OPEN
026654             GO TO Z-RESTART-REPORT1-DONE.
026656     IF Z-RPTINFO1-OPEN = 0
026658         OPEN OUTPUT LISTING
026660         MOVE 3 TO Z-RPTINFO1-OPEN.
026662     MOVE "RESTARTED" TO Z-RPT-1-BUFFER.
026664     WRITE Z-RPT-1-BUFFER AFTER ADVANCING PAGE.
026666     MOVE SPACES TO Z-RPT-1-BUFFER.
026668     WRITE Z-RPT-1-BUFFER AFTER ADVANCING PAGE.
026670     WRITE Z-RPT-1-BUFFER
026672         AFTER ADVANCING Z-RPT-1-LINE LINES.
026674 Z-RESTART-REPORT1-DONE.
026676     IF Z-RPTINFO2-RS-OPEN = 0
026678         IF Z-RPTINFO2-OPEN = 0
026680             GO TO Z-RESTART-REPORT2-DONE
026682         ELSE
026684             CLOSE FICHE
026686             MOVE 0 TO Z-RPTINFO2-OPEN
026688             GO TO Z-RESTART-REPORT2-DONE.
026690     IF Z-RPTINFO2-OPEN = 0
026692         OPEN OUTPUT FICHE
026694         MOVE 3 TO Z-RPTINFO2-OPEN.
026696     MOVE "RESTARTED" TO Z-RPT-2-BUFFER.
026698     WRITE Z-RPT-2-BUFFER AFTER ADVANCING PAGE.
026700     MOVE SPACES TO Z-RPT-2-BUFFER.
026702     WRITE Z-RPT-2-BUFFER AFTER ADVANCING PAGE.
026704     WRITE Z-RPT-2-BUFFER
026706         AFTER ADVANCING Z-RPT-2-LINE LINES.
026708 Z-RESTART-REPORT2-DONE.
026710 Z-CHECK-RESTART-XIT.
026712     EXIT.
026714*
026716**** DISPLAY COMPRESS
026718*
026720 Z-DISP-COMPRESS.
026722     MOVE Z-DISP-COMPACT-BUFFER TO Z-LALPHA-1.
026724     MOVE SPACES TO Z-LALPHA-2.
026726     CALL "XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY" USING            
026728         Z-LALPHA-1, Z-LALPHA-2, Z-STR-INT-ONE, Z-DISP-SIZE,      
026730         Z-STR-INT-ZERO, Z-STR-INT-ONE, Z-STR-INT-ONE,            
026732         Z-STR-INT-ZERO.
026734     MOVE Z-LALPHA-1 TO Z-DISP-COMPACT-BUFFER.
026736 Z-DISP-COMPRESS-XIT.
026738     EXIT.
026740*
026742 Z-DATE-CALC-T.
026744     ADD Z-DATE-TT-1 TO Z-DATE-T.
026746     IF Z-DATE-T > +99 OR Z-DATE-T < -99
026748         DIVIDE Z-DATE-T BY +100 GIVING Z-DATE-S
026750         REMAINDER Z-DATE-T.
026752     MOVE Z-DATE-T TO Z-DATE-TT-1.
026754     IF Z-DATE-TT-1 < ZERO
026756         ADD +100 TO Z-DATE-TT-1
026758         SUBTRACT +1 FROM Z-DATE-S.
026760*
026762 Z-DATE-CALC-T-EXIT.
026764     EXIT.
026766*
026768 Z-DATE-CALC-S.
026770     ADD Z-DATE-SS-1 TO Z-DATE-S.
026772     IF Z-DATE-S > +59 OR Z-DATE-S < -59
026774         DIVIDE Z-DATE-S BY +60 GIVING Z-DATE-U
026776         REMAINDER Z-DATE-S.
026778     MOVE Z-DATE-S TO Z-DATE-SS-1.
026780     IF Z-DATE-SS-1 < ZERO
026782         ADD +60 TO Z-DATE-SS-1
026784         SUBTRACT +1 FROM Z-DATE-U.
026786*
026788 Z-DATE-CALC-S-EXIT.
026790     EXIT.
026792*
026794 Z-DATE-CALC-U.
026796     ADD Z-DATE-UU-1 TO Z-DATE-U.
026798     IF Z-DATE-U > +59 OR  Z-DATE-U < -59
026800         DIVIDE Z-DATE-U BY +60 GIVING Z-DATE-Z
026802             REMAINDER Z-DATE-U.
026804     MOVE Z-DATE-U TO Z-DATE-UU-1.
026806     IF Z-DATE-UU-1 < ZERO
026808         ADD +60 TO Z-DATE-UU-1
026810         SUBTRACT +1 FROM Z-DATE-Z.
026812*
026814 Z-DATE-CALC-U-EXIT.
026816     EXIT.
026818*
026820 Z-DATE-CALC-Z.
026822     ADD Z-DATE-ZZ-1 TO Z-DATE-Z.
026824     IF Z-DATE-Z > +23 OR Z-DATE-Z < -23
026826         DIVIDE Z-DATE-Z BY +24 GIVING Z-DATE-D
026828         REMAINDER Z-DATE-Z.
026830     MOVE Z-DATE-Z TO Z-DATE-ZZ-1.
026832     IF Z-DATE-ZZ-1 < ZERO
026834         ADD +24 TO Z-DATE-ZZ-1
026836         SUBTRACT +1 FROM Z-DATE-D.
026838*
026840 Z-DATE-CALC-Z-EXIT.
026842     EXIT.
026844*
026846 Z-DATE-CNVRT-WEEKS-TO-DD.
026848     MULTIPLY  Z-DATE-W BY +7 GIVING Z-DATE-D.
026850*
026852 Z-DATE-CNVRT-WEEKS-TO-DD-EXIT.
026854     EXIT.
026856*
026858 Z-DATE-CALC-D.
026860     IF Z-DATE-D > ZERO
026862         PERFORM Z-DATE-CALC-LEAP-YEAR
026864            THRU Z-DATE-CALC-LEAP-YEAR-EXIT
026866         PERFORM Z-DATE-CALC-MONTH-DAYS
026868            THRU Z-DATE-CALC-MONTH-DAYS-EXIT
026870         PERFORM Z-DATE-ADD-1ST-YR
026872            THRU Z-DATE-ADD-1ST-YR-EXIT
026874         PERFORM Z-DATE-ADD-D
026876            THRU Z-DATE-ADD-D-EXIT
026878           UNTIL Z-DATE-D = ZEROS
026880     ELSE
026882         PERFORM Z-DATE-SUBTRACT-1ST-YR
026884            THRU Z-DATE-SUBTRACT-1ST-YR-EXIT
026886         PERFORM Z-DATE-SUBTRACT-D
026888            THRU Z-DATE-SUBTRACT-D-EXIT
026890           UNTIL Z-DATE-D = ZEROS.
026892     MOVE ZEROS TO Z-DATE-C.
026894     MOVE ZEROS TO Z-DATE-Y.
026896     MOVE ZEROS TO Z-DATE-M.
026898*
026900 Z-DATE-CALC-D-EXIT.
026902     EXIT.
026904*
026906 Z-DATE-ADD-1ST-YR.
026908     ADD Z-DATE-JJJ-1, Z-DATE-D GIVING Z-DATE-UNITS-WORK.
026910     IF Z-DATE-LEAP-YEAR
026912         IF Z-DATE-UNITS-WORK NOT > +366
026914             MOVE Z-DATE-UNITS-WORK TO Z-DATE-JJJ-1
026916             MOVE ZEROS TO Z-DATE-D
026918         ELSE
026920             SUBTRACT Z-DATE-JJJ-1 FROM +366
026922               GIVING Z-DATE-UNITS-WORK
026924             SUBTRACT Z-DATE-UNITS-WORK FROM Z-DATE-D
026926             PERFORM Z-DATE-INCREMENT-YY-CC
026928                THRU Z-DATE-INCREMENT-YY-CC-EXIT
026930             PERFORM Z-DATE-CALC-LEAP-YEAR
026932                THRU Z-DATE-CALC-LEAP-YEAR-EXIT
026934             PERFORM Z-DATE-CALC-MONTH-DAYS
026936                THRU Z-DATE-CALC-MONTH-DAYS-EXIT
026938     ELSE
026940         IF Z-DATE-UNITS-WORK NOT > +365
026942             MOVE Z-DATE-UNITS-WORK TO Z-DATE-JJJ-1
026944             MOVE ZEROS TO Z-DATE-D
026946         ELSE
026948             SUBTRACT Z-DATE-JJJ-1 FROM +365
026950               GIVING Z-DATE-UNITS-WORK
026952             SUBTRACT Z-DATE-UNITS-WORK FROM Z-DATE-D
026954             PERFORM Z-DATE-INCREMENT-YY-CC
026956                THRU Z-DATE-INCREMENT-YY-CC-EXIT
026958             PERFORM Z-DATE-CALC-LEAP-YEAR
026960                THRU Z-DATE-CALC-LEAP-YEAR-EXIT
026962             PERFORM Z-DATE-CALC-MONTH-DAYS
026964                THRU Z-DATE-CALC-MONTH-DAYS-EXIT.
026966*
026968 Z-DATE-ADD-1ST-YR-EXIT.
026970     EXIT.
026972*
026974 Z-DATE-SUBTRACT-1ST-YR.
026976     ADD Z-DATE-JJJ-1, Z-DATE-D GIVING Z-DATE-UNITS-WORK.
026978     IF Z-DATE-UNITS-WORK > ZEROS
026980         ADD Z-DATE-D TO Z-DATE-JJJ-1
026982         MOVE  ZEROS TO Z-DATE-D
026984     ELSE
026986         ADD Z-DATE-JJJ-1 TO Z-DATE-D
026988         PERFORM Z-DATE-DECREMENT-YY-CC
026990             THRU Z-DATE-DECREMENT-YY-CC-EXIT
026992         PERFORM Z-DATE-CALC-LEAP-YEAR
026994             THRU Z-DATE-CALC-LEAP-YEAR-EXIT
026996         PERFORM Z-DATE-CALC-MONTH-DAYS
026998             THRU Z-DATE-CALC-MONTH-DAYS-EXIT
027000         IF Z-DATE-LEAP-YEAR
027002             ADD Z-DATE-UNITS-WORK, 366 GIVING
027004                 Z-DATE-JJJ-1
027006         ELSE
027008             ADD Z-DATE-UNITS-WORK, 365 GIVING
027010                 Z-DATE-JJJ-1.
027012 Z-DATE-SUBTRACT-1ST-YR-EXIT.
027014     EXIT.
027016*
027018 Z-DATE-ADD-D.
027020     IF Z-DATE-LEAP-YEAR
027022         IF Z-DATE-D > +366
027024             SUBTRACT +366 FROM Z-DATE-D
027026             PERFORM Z-DATE-INCREMENT-YY-CC
027028                THRU Z-DATE-INCREMENT-YY-CC-EXIT
027030             PERFORM Z-DATE-CALC-LEAP-YEAR
027032                THRU Z-DATE-CALC-LEAP-YEAR-EXIT
027034             PERFORM Z-DATE-CALC-MONTH-DAYS
027036                THRU Z-DATE-CALC-MONTH-DAYS-EXIT
027038         ELSE
027040             MOVE Z-DATE-D TO Z-DATE-JJJ-1
027042             MOVE ZEROS TO Z-DATE-D
027044     ELSE
027046         IF Z-DATE-D > +365
027048             SUBTRACT +365 FROM Z-DATE-D
027050             PERFORM Z-DATE-INCREMENT-YY-CC
027052                THRU Z-DATE-INCREMENT-YY-CC-EXIT
027054             PERFORM Z-DATE-CALC-LEAP-YEAR
027056                THRU Z-DATE-CALC-LEAP-YEAR-EXIT
027058             PERFORM Z-DATE-CALC-MONTH-DAYS
027060                THRU Z-DATE-CALC-MONTH-DAYS-EXIT
027062         ELSE
027064             MOVE Z-DATE-D TO Z-DATE-JJJ-1
027066             MOVE ZEROS TO Z-DATE-D.
027068 Z-DATE-ADD-D-EXIT.
027070     EXIT.
027072*
027074 Z-DATE-INCREMENT-YY-CC.
027076     IF Z-DATE-YY-1 < 99
027078         ADD +1 TO Z-DATE-YY-1
027080     ELSE
027082         MOVE ZEROS TO Z-DATE-YY-1
027084         ADD +1 TO Z-DATE-CC-1.
027086 Z-DATE-INCREMENT-YY-CC-EXIT.
027088     EXIT.
027090*
027092 Z-DATE-SUBTRACT-D.
027094     IF Z-DATE-LEAP-YEAR
027096         IF Z-DATE-D NOT > -366
027098             ADD +366 TO Z-DATE-D
027100             IF Z-DATE-D = ZEROS
027102                 PERFORM Z-DATE-DECREMENT-YY-CC
027104                    THRU Z-DATE-DECREMENT-YY-CC-EXIT
027106                 MOVE +365 TO Z-DATE-JJJ-1
027108             ELSE
027110                 PERFORM Z-DATE-DECREMENT-YY-CC
027112                    THRU Z-DATE-DECREMENT-YY-CC-EXIT
027114                 PERFORM Z-DATE-CALC-LEAP-YEAR
027116                    THRU Z-DATE-CALC-LEAP-YEAR-EXIT
027118                 PERFORM Z-DATE-CALC-MONTH-DAYS
027120                    THRU Z-DATE-CALC-MONTH-DAYS-EXIT
027122         ELSE
027124             COMPUTE Z-DATE-JJJ-1 = Z-DATE-D + 366
027126             MOVE ZEROS TO Z-DATE-D
027128     ELSE
027130         IF Z-DATE-D NOT > -365
027132             ADD +365 TO Z-DATE-D
027134             IF Z-DATE-D = ZEROS
027136                 PERFORM Z-DATE-DECREMENT-YY-CC
027138                    THRU Z-DATE-DECREMENT-YY-CC-EXIT
027140                 PERFORM Z-DATE-CALC-LEAP-YEAR
027142                    THRU Z-DATE-CALC-LEAP-YEAR-EXIT
027144                 PERFORM Z-DATE-CALC-MONTH-DAYS
027146                    THRU Z-DATE-CALC-MONTH-DAYS-EXIT
027148                 MOVE ZEROS TO Z-DATE-JJJ-1
027150                 IF Z-DATE-LEAP-YEAR
027152                     ADD +366 TO Z-DATE-JJJ-1
027154                 ELSE
027156                     ADD +365 TO Z-DATE-JJJ-1
027158             ELSE
027160                 PERFORM Z-DATE-DECREMENT-YY-CC
027162                    THRU Z-DATE-DECREMENT-YY-CC-EXIT
027164                 PERFORM Z-DATE-CALC-LEAP-YEAR
027166                    THRU Z-DATE-CALC-LEAP-YEAR-EXIT
027168                 PERFORM Z-DATE-CALC-MONTH-DAYS
027170                    THRU Z-DATE-CALC-MONTH-DAYS-EXIT
027172         ELSE
027174             COMPUTE Z-DATE-JJJ-1 = Z-DATE-D + 365
027176             MOVE ZEROS TO Z-DATE-D.
027178 Z-DATE-SUBTRACT-D-EXIT.
027180     EXIT.
027182*
027184 Z-DATE-DECREMENT-YY-CC.
027186     IF Z-DATE-YY-1 > 0
027188         SUBTRACT +1 FROM Z-DATE-YY-1
027190     ELSE
027192         MOVE +99 TO Z-DATE-YY-1
027194         SUBTRACT +1 FROM Z-DATE-CC-1.
027196 Z-DATE-DECREMENT-YY-CC-EXIT.
027198     EXIT.
027200*
027202 Z-DATE-CALC-M.
027204     IF Z-DATE-M > ZERO
027206         PERFORM Z-DATE-ADD-M
027208            THRU Z-DATE-ADD-M-EXIT
027210     ELSE
027212         PERFORM Z-DATE-SUBTRACT-M
027214            THRU Z-DATE-SUBTRACT-M-EXIT.
027216 Z-DATE-CALC-M-EXIT.
027218     EXIT.
027220*
027222 Z-DATE-ADD-M.
027224     IF Z-DATE-M > +11
027226         DIVIDE Z-DATE-M BY +12 GIVING Z-DATE-Y
027228             REMAINDER Z-DATE-M
027230         ADD Z-DATE-MM-1 TO Z-DATE-M
027232         IF Z-DATE-M > +12
027234             DIVIDE Z-DATE-M BY +12 GIVING Z-DATE-UNITS-WORK
027236                 REMAINDER Z-DATE-M
027238             ADD Z-DATE-UNITS-WORK TO Z-DATE-Y
027240             MOVE Z-DATE-M TO Z-DATE-MM-1
027242         ELSE
027244             MOVE Z-DATE-M TO Z-DATE-MM-1
027246     ELSE
027248         ADD Z-DATE-MM-1 TO Z-DATE-M
027250         IF Z-DATE-M > +12
027252             DIVIDE Z-DATE-M BY +12 GIVING Z-DATE-Y
027254                 REMAINDER Z-DATE-M
027256             MOVE Z-DATE-M TO Z-DATE-MM-1
027258         ELSE
027260             MOVE Z-DATE-M TO Z-DATE-MM-1.
027262 Z-DATE-ADD-M-EXIT.
027264     EXIT.
027266*
027268 Z-DATE-SUBTRACT-M.
027270     IF Z-DATE-M < -12
027272         DIVIDE Z-DATE-M BY +12 GIVING Z-DATE-Y
027274             REMAINDER Z-DATE-M
027276         ADD Z-DATE-MM-1 TO Z-DATE-M
027278         IF Z-DATE-M < +1
027280             ADD +12 TO Z-DATE-M
027282             SUBTRACT +1 FROM Z-DATE-Y
027284             MOVE Z-DATE-M TO Z-DATE-MM-1
027286         ELSE
027288             MOVE Z-DATE-M TO Z-DATE-MM-1
027290     ELSE
027292         ADD Z-DATE-MM-1 TO Z-DATE-M
027294         IF Z-DATE-M < +1
027296             ADD +12 TO Z-DATE-M
027298             SUBTRACT +1 FROM Z-DATE-Y
027300             MOVE Z-DATE-M TO Z-DATE-MM-1
027302         ELSE
027304             MOVE Z-DATE-M TO Z-DATE-MM-1.
027306*
027308 Z-DATE-SUBTRACT-M-EXIT.
027310     EXIT.
027312*
027314 Z-DATE-CALC-Y.
027316     ADD Z-DATE-YY-1 TO Z-DATE-Y.
027318     IF Z-DATE-Y > +99 OR Z-DATE-Y < -99
027320         DIVIDE Z-DATE-Y BY +100 GIVING Z-DATE-C
027322             REMAINDER Z-DATE-Y.
027324     MOVE Z-DATE-Y TO Z-DATE-YY-1.
027326     IF Z-DATE-YY-1 < ZERO
027328         ADD +100 TO Z-DATE-YY-1
027330         SUBTRACT +1 FROM Z-DATE-C.
027332*
027334 Z-DATE-CALC-Y-EXIT.
027336     EXIT.
027338*
027340 Z-DATE-CALC-C.
027342     ADD Z-DATE-CC-1 TO Z-DATE-C.
027344     MOVE Z-DATE-C TO Z-DATE-CC-1.
027346*
027348 Z-DATE-CALC-C-EXIT.
027350     EXIT.
027352*
```

⚠️  This is the source code you must document.
    633 lines from 13040 to 13672.
    Refer to the template instructions for complete requirements.

```

---

## Program Map (if present)

*(No program map in context)*

