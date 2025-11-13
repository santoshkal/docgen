# LLM Request Debug File
Generated: 2025-11-12T19:57:14.359921

## Request Metadata
- **Section ID**: execution-flow-sequence
- **Section Title**: Execution Flow Sequence
- **Model**: gpt-4.1
- **Chunk Number**: N/A
- **Pass Number**: 2
- **Attempt Number**: 1 (INITIAL)

## Token Estimates (4 chars/token)
- **System Prompt**: ~681 tokens
- **User Prompt**: ~42,307 tokens
- **Total Input**: ~42,988 tokens

---

## System Prompt

```
You are a technical documentation agent specializing in COBOL code analysis.

Your task is to generate documentation for the section: "Execution Flow Sequence" (ID: execution-flow-sequence)

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
```mermaid
sequenceDiagram
  participant User
  participant {{program_name}}
  {{external_program_participants}}

  {{detailed_execution_sequence}}
```


INSTRUCTION:
Create detailed sequence diagram from metadata showing REALISTIC execution flow.

**CRITICAL - Mermaid Sequence Diagram Sanitization:**
Participant names in sequence diagrams must be sanitized:
1. Replace spaces with underscores or remove them
2. Remove or replace special characters: " ' / \ * -
3. Use only alphanumeric and underscores
4. Keep names short (under 20 chars if possible)

Sanitization Examples for Sequence Diagrams:
- Original: L"S"/"GENL" → Sanitized: LSGENL
- Original: INIT-SYSTEM → Sanitized: INITSYSTEM
- Original: 000026*REMARKS → Sanitized: REMARKS_000026

Use superbol_cfg to build sequence:
1. Start with MAIN-PROGRAM or entry paragraph (sanitized name)
2. Follow performs[] to show internal paragraph calls (sanitized names)
3. Integrate calls[] to show external program interactions (sanitized names)
4. Include line numbers as notes
5. Show loops, conditionals, and error paths

Example structure with sanitization:
```
User->>MAINPROG: Start
MAINPROG->>INITSYSTEM: PERFORM (line 21)
INITSYSTEM->>DBCONNECT: CALL (line 33)
Note over DBCONNECT: Establishes DB connection
DBCONNECT-->>INITSYSTEM: Return
INITSYSTEM->>LOGGER: CALL (line 38)
LOGGER-->>INITSYSTEM: Return
loop User Operations
    MAINPROG->>PROCESSSELECTION: PERFORM
    alt Customer Operations
        PROCESSSELECTION->>CUSTMGMT: CALL (line 71)
    alt Account Operations
        PROCESSSELECTION->>ACCTOPER: CALL (line 82)
    alt Transactions
        PROCESSSELECTION->>TRANPROC: CALL (line 96)
    end
end
```

Be comprehensive but realistic - show actual execution path.


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

{
  "program_name": "TDAS-MINDISTCALC",
  "timestamp": "2025-11-12T19:57:14.318655",
  "superbol_symbols": {
    "program_id": null,
    "children": [],
    "procedure_division": null,
    "paragraphs": null,
    "sections": null
  },
  "superbol_cfg": {
    "nodes": [
      {
        "type": "paragraph",
        "name": "000026*REMARKS",
        "line": 8
      },
      {
        "type": "section",
        "name": "000412",
        "line": 201
      },
      {
        "type": "section",
        "name": "000442",
        "line": 216
      },
      {
        "type": "section",
        "name": "000528",
        "line": 259
      },
      {
        "type": "section",
        "name": "001624",
        "line": 807
      },
      {
        "type": "section",
        "name": "001678",
        "line": 834
      },
      {
        "type": "section",
        "name": "025660",
        "line": 12825
      },
      {
        "type": "section",
        "name": "025678",
        "line": 12834
      },
      {
        "type": "section",
        "name": "025760",
        "line": 12875
      },
      {
        "type": "section",
        "name": "025802",
        "line": 12896
      },
      {
        "type": "section",
        "name": "025942",
        "line": 12966
      },
      {
        "type": "section",
        "name": "027776*Z-USERS-DECLARATIONS",
        "line": 13883
      },
      {
        "type": "paragraph",
        "name": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "line": 13886
      },
      {
        "type": "section",
        "name": "028168",
        "line": 14079
      },
      {
        "type": "paragraph",
        "name": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "line": 14738
      },
      {
        "type": "section",
        "name": "029688",
        "line": 14839
      },
      {
        "type": "section",
        "name": "029696",
        "line": 14843
      },
      {
        "type": "section",
        "name": "030004",
        "line": 14997
      },
      {
        "type": "section",
        "name": "030012",
        "line": 15001
      },
      {
        "type": "paragraph",
        "name": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "line": 15015
      },
      {
        "type": "section",
        "name": "030042",
        "line": 15016
      },
      {
        "type": "section",
        "name": "030436",
        "line": 15213
      },
      {
        "type": "paragraph",
        "name": "032926********ENDIF",
        "line": 16458
      },
      {
        "type": "paragraph",
        "name": "033256********ENDIF",
        "line": 16623
      },
      {
        "type": "paragraph",
        "name": "033774*****ENDIF",
        "line": 16882
      }
    ],
    "edges": [
      {
        "from": "000026*REMARKS",
        "to": "Z-PROCESS-INIT",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-OPEN-DB-1",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-OPEN-DB-2",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-BEGIN-TRANS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-ABORT",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-END-TRANS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-ABORT",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-RESTART-SKIP",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-RESTART-PROCESS-3",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-PROCESS-INIT",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-3-PROCESS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-ABORT",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-BEGIN-TRANS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-ABORT",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-END-TRANS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-ABORT",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-CLOSE-DB-1",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-CLOSE-DB-2",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-ABORT",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-OPEN-DB-2",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-ABORT",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DISP-COMPRESS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DISP-COMPRESS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-FREE",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-BEGIN-TRANS-XIT",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-RELOCK",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-BEGIN-TRANS",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-ABORT-TRANS",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-END-TRANS-NO-AUDIT",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-END-TRANS-SYNC",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-CHECK-ET-EXCEPTION",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-CHECK-ET-EXCEPTION",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-CHECK-ET-EXCEPTION",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-FREE",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-END-TRANS-XIT",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-RELOCK",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-BEGIN-TRANS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-END-TRANS",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-CLEAR-MODIFY-FLAGS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-CLOSE-DB-1",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-OPEN-DB-1",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-CLOSE-DB-2",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-OPEN-DB-2",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-RESTART-REPORT1-DONE",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-RESTART-REPORT1-DONE",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-RESTART-REPORT2-DONE",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-RESTART-REPORT2-DONE",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-ADD-1ST-YR",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-ADD-D",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-SUBTRACT-1ST-YR",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-SUBTRACT-D",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INCREMENT-YY-CC",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INCREMENT-YY-CC",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-DECREMENT-YY-CC",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INCREMENT-YY-CC",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INCREMENT-YY-CC",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-DECREMENT-YY-CC",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-DECREMENT-YY-CC",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-DECREMENT-YY-CC",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-DECREMENT-YY-CC",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-ADD-M",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-SUBTRACT-M",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR-EXIT",
        "type": "goto"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CONVERT-MDY-TO-JUL",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-DATE-1",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-DATE-2",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-DATE-3",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-UNITS",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-MATH-WA",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-JUL-MDY",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-LEAP-YR",
        "type": "perform"
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-CVRT-STATUS",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-1-4-END-MOVE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-1-6-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-1-11-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-1-13-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-1-15-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-1-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-RPT-1-ADV-PAGE-CNT",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-1-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-2-4-END-MOVE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-2-6-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-2-11-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-2-13-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-2-15-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-2-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-RPT-2-ADV-PAGE-CNT",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-2-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-RESTART",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-2-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-2-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-2-CONT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-3-CONT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-12-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-5-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-15-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-15-ENDIF",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-15-2-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-15-ENDIF",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-15-3-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-21-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-5-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-5-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-5-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-5-LOOP",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-23-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-23-ENDIF",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-23-2-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-32-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "GET-BANK-INFO",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-4-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "GET-ACCT-INFO",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-5-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "CLOSE-FM-FILE-RPT",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-6-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-37-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-39-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-41-EXIT-SKIP",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-39-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "GET-BANK-INFO",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-4-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-39-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-39-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "GET-ACCT-INFO",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-5-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-39-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-39-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "CLOSE-FM-FILE-RPT",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-6-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-39-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-39-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-39-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-39-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-39-LOOP",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-51-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-55-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-57-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-62-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "GET-BANK-INFO",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-4-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-57-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-57-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "GET-ACCT-INFO",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-5-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-57-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-57-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "CLOSE-FM-FILE-RPT",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-6-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-57-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-57-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-57-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-57-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS2-BEGIN-TRANS",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS2-FREE",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS2-END-TRANS",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-57-LOOP",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS2-FREE",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS2-END-TRANS",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-72-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-76-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-79-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-85-DISPLAY",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-86-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-88-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-90-EXIT-SKIP",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-88-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-91-1-ELSE",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-88-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-END",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-88-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-88-LOOP",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-93-DISPLAY",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS2-FREE",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS2-END-TRANS",
        "type": "perform"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-XIT",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-PROCESS",
        "type": "goto"
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-3-RESTART-1",
        "type": "goto"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-REMOTE-LBL-CHK",
        "type": "perform"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-RMT-LBL-CHK",
        "type": "perform"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "ONCE",
        "type": "perform"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT1",
        "type": "perform"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-REMOTE-LBL-CHK",
        "type": "perform"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-RMT-LBL-CHK",
        "type": "perform"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "Z-7-1-1-ELSE",
        "type": "goto"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-NEW-NAME-CHK",
        "type": "perform"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "Z-7-1-ENDIF",
        "type": "goto"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "Z-7-1-2-ELSE",
        "type": "goto"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-REMOTE-LBL-CHK",
        "type": "perform"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "TPR-REMOTE-BANK",
        "type": "perform"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "Z-8-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "Z-7-XIT",
        "type": "goto"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "Z-7-XIT",
        "type": "goto"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "Z-7-END",
        "type": "goto"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-LABEL-END",
        "type": "goto"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-LABEL-END",
        "type": "goto"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-LABEL-END",
        "type": "goto"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-LONG-LABEL-CHK",
        "type": "goto"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-LABEL-END",
        "type": "goto"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-LABEL-END",
        "type": "goto"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-LABEL-END",
        "type": "goto"
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-LABEL-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-7-3-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-7-3-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-NEW-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-FIND2",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-NEW-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-FOUND",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-FIND3",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-NEW-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-FOUND",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-FIND4",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-NEW-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-FOUND",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-FIND5",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-NEW-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-FOUND",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-FIND6",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-NEW-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-FOUND",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-NEW-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-NEW-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-NAME-EXIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-FIND2",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-EXIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-FOUND",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-FIND3",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-EXIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-FOUND",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-FIND4",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-EXIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-FOUND",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-FIND5",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-EXIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-FOUND",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-FIND6",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-EXIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-FOUND",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-EXIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-NEW-CHG-EXIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-7-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-8-4-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-8-5-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-8-5-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-8-4-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-8-9-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-8-9-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-8-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-1-1-LOOP-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-1-1-LOOP",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-2-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-3-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-2-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-2-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-2-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-2-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-3-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-4-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-5-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-21-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-22-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-21-LOOP",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-6-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-7-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-8-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-9-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-8-10-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-2-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-2-LOOP",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-9-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-10-1-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-10-1-CONT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "SETUP-ACCT-NO-READ",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-10-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-10-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-10-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-10-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "TDD-TDAA-MOVE-TO-TDB",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-12-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "TDD-TDAA-MOVE-TO-HOLD",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-13-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "TDB-CUST-INQ",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-14-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-22-END-MOVE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-22-1-LOOP-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-22-1-LOOP",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-23-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "TDB-IRAUPD-INQ",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-15-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-END",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-41-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-42-1-LOOP-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-42-1-LOOP",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-16-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-17-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-18-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-19-XIT",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-1-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-1-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-22-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-22-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-27-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-29-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-29-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-29-2-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-29-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-29-3-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-29-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-29-4-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-34-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-36-END-MOVE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-37-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-LABEL-CHECK",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-39-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-39-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "999999-CHANGE1",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "999999-CHANGE24",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-54-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-54-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-54-2-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-54-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-54-3-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-54-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-61-1-ELSE",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "999999-CHANGE54",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "999999-CHANGE34",
        "type": "perform"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-20-61-ENDIF",
        "type": "goto"
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "999999-CHANGE55",
        "type": "perform"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-68-1-ELSE",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "TPR-TEAR-PAGES",
        "type": "perform"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-21-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-XIT",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-XIT",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-END",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-70-1-ELSE",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-74-1-ELSE",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-74-ENDIF",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-74-2-ELSE",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-74-ENDIF",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "99-PRT-LABEL-CHECK",
        "type": "perform"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-82-1-ELSE",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-82-ENDIF",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "999999-CHANGE22",
        "type": "perform"
      },
      {
        "from": "032926********ENDIF",
        "to": "999999-CHANGE33",
        "type": "perform"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-95-1-ELSE",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-95-ENDIF",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-95-2-ELSE",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-95-ENDIF",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "HEADING-SETUP",
        "type": "perform"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-16-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-XIT",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-XIT",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-END",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-102-1-ELSE",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "999999-CHANGE72",
        "type": "perform"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-103-1-ELSE",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "999999-CHANGE52",
        "type": "perform"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-103-ENDIF",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "999999-CHANGE53",
        "type": "perform"
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-20-102-ENDIF",
        "type": "goto"
      },
      {
        "from": "032926********ENDIF",
        "to": "999999-CHANGE73",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "TPR-TEAR-PAGES",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-21-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-20-XIT",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-20-XIT",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-20-END",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-20-111-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-20-114-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-20-XIT",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-1-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-13-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-13-ENDIF",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-13-2-ELSE",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-13-ENDIF",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-13-3-ELSE",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-13-ENDIF",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "HEADING-SETUP",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-16-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-XIT",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-XIT",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-END",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "TPR-TEAR-PAGES",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-21-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-XIT",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-XIT",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-END",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-27-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "999999-CHANGE54",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "999999-CHANGE34",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-27-ENDIF",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "999999-CHANGE55",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-28-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-40-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-40-ENDIF",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-40-2-ELSE",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-40-ENDIF",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "HEADING-SETUP",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-16-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-XIT",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-XIT",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-END",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "TPR-TEAR-PAGES",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-21-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-XIT",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-XIT",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-END",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-53-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "999999-CHANGE72",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-54-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "999999-CHANGE52",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-54-ENDIF",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "999999-CHANGE53",
        "type": "perform"
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-22-53-ENDIF",
        "type": "goto"
      },
      {
        "from": "033256********ENDIF",
        "to": "999999-CHANGE73",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-22-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-1-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-2-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "RMDRPT-SETUP",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-24-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-7-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-8-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "RMDRPT2-SETUP",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-25-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-13-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-21-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-22-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-M",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-22-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-22-2-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-22-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-31-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-31-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-35-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-37-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-37-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-37-2-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-37-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-47-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-48-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-48-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-47-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-47-2-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-51-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-51-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-47-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-47-3-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-54-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-54-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-47-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-57-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-57-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-35-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-63-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-63-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-69-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-69-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-75-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-75-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-78-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-79-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-81-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-82-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-82-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-87-END-MOVE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-88-END-MOVE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-89-END-MOVE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-90-END-MOVE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-91-END-MOVE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-92-END-MOVE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-95-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-95-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-95-2-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-95-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-95-3-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-102-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-102-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-81-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-109-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-112-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-112-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-118-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-121-ADD-SKIP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-109-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-123-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-124-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-126-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-124-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-132-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-123-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-139-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-140-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-142-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-140-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-148-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-150-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-151-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-152-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-151-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-155-ADD-SKIP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-6-1-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-6-4-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "CLOSE-PRT-FILE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-22-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-6-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-6-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-6-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-6-8-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "CLOSE-PRT-FILE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-22-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-6-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-6-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-6-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-6-13-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-6-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-1-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-1-CONT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-2-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-5-1-LOOP-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-5-1-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-9-1-LOOP-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-9-1-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-11-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-13-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-13-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-14-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-14-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-14-2-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-14-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-14-3-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-13-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-13-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-13-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-11-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-4-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-3-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-3-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-4-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-3-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-7-NEXT-SKIP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-3-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-8-1-LOOP-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-8-1-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-9-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "WRITE-CUST-FM-REC",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-26-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-3-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-15-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-17-1-LOOP-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-17-1-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-18-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-18-CONT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-19-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-21-1-LOOP-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-21-1-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-21-2-LOOP-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-21-2-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-23-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-23-2-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-26-NEXT-SKIP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-YY-DIFF",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-28-NEXT-SKIP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-31-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-34-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-35-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-36-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-37-EXIT-SKIP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-36-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-40-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-41-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-41-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-41-2-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-41-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-45-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-49-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-52-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-36-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-36-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "COMB-AUTO-RMD-ADJ",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-57-SKIPPROC",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "COMB-AUTO-RMD-ADJ",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-27-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-59-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-65-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-68-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-72-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-76-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-80-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-80-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-80-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-82-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-82-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-86-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "TDD-MINDIST-SETUP-AND-CALC",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-28-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-82-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-88-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-89-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-91-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-94-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-96-SKIP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-FL-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-111-SKIP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-FL-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-124-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "WRITE-REPORT",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-82-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-127-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-128-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-130-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-130-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-130-2-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-130-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-130-3-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-140-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-142-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-140-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-150-SKIP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-FL-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-163-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-163-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-166-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-168-SKIP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-FL-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-82-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-82-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-183-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "TDD-MINDIST-SETUP-AND-CALC",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-28-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-185-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-186-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-188-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-191-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-193-SKIP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-FL-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-208-SKIP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-FL-EXCEPTION",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-221-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "WRITE-REPORT",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-3-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-14-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-224-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-226-END-MOVE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-3-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-3-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "WRITE-CUST-FM-REC",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-26-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-229-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-230-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-231-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-232-EXIT-SKIP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-231-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-235-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-236-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-236-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-236-2-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-236-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-240-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-244-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-247-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-231-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-231-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "COMB-AUTO-RMD-ADJ",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-252-SKIPPROC",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "COMB-AUTO-RMD-ADJ",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-27-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-254-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-260-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-263-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-267-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-274-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-276-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-279-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-5-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-3-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-3-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-6-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-6-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-18-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-20-1-ELSE",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-PRINT-TEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-18-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-20-ENDIF",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-25-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-25-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-18-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-18-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-21-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-1-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-2-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-2-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-1-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-1-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-1-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-1-LOOP",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-END",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "type": "perform"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-XIT",
        "type": "goto"
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-END",
        "type": "goto"
      }
    ],
    "calls": [
      {
        "from": "000026*REMARKS",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 12840
      },
      {
        "from": "000026*REMARKS",
        "to": "XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY",
        "line": 13358
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 14104
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 16214
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 16223
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 16287
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 16296
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "XSTRPAT OF XGEN/RUNTIME/LIBRARY",
        "line": 16374
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "XSTRCAT OF XGEN/RUNTIME/LIBRARY",
        "line": 16385
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 16410
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 16419
      },
      {
        "from": "032926********ENDIF",
        "to": "XSTRPAT OF XGEN/RUNTIME/LIBRARY",
        "line": 16531
      },
      {
        "from": "032926********ENDIF",
        "to": "XSTRCAT OF XGEN/RUNTIME/LIBRARY",
        "line": 16542
      },
      {
        "from": "032926********ENDIF",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 16565
      },
      {
        "from": "032926********ENDIF",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 16574
      },
      {
        "from": "033256********ENDIF",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 16704
      },
      {
        "from": "033256********ENDIF",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 16713
      },
      {
        "from": "033256********ENDIF",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 16802
      },
      {
        "from": "033256********ENDIF",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 16811
      },
      {
        "from": "033774*****ENDIF",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 20164
      },
      {
        "from": "033774*****ENDIF",
        "to": "CURRENT_DATE OF GENERALSUPPORT",
        "line": 21326
      }
    ],
    "copybooks": [
      {
        "name": "FILES",
        "library": null,
        "line": 18,
        "context": "DATA-DIVISION"
      },
      {
        "name": "FILES",
        "library": "COPY",
        "line": 84,
        "context": "DATA-DIVISION"
      },
      {
        "name": "IN",
        "library": "THE",
        "line": 14769,
        "context": "028168"
      },
      {
        "name": "STATEMENT",
        "library": "THE",
        "line": 14774,
        "context": "028168"
      },
      {
        "name": "PRINTER",
        "library": null,
        "line": 14829,
        "context": "028168"
      },
      {
        "name": "REPLACING",
        "library": null,
        "line": 14864,
        "context": "029696"
      }
    ],
    "performs": [
      {
        "from": "000026*REMARKS",
        "to": "Z-PROCESS-INIT",
        "line": 12848
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-OPEN-DB-1",
        "line": 12851
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-OPEN-DB-2",
        "line": 12852
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-BEGIN-TRANS",
        "line": 12855
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-END-TRANS",
        "line": 12860
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-PROCESS-INIT",
        "line": 12885
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-3-PROCESS",
        "line": 12886
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-BEGIN-TRANS",
        "line": 12947
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-END-TRANS",
        "line": 12952
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-CLOSE-DB-1",
        "line": 12956
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-CLOSE-DB-2",
        "line": 12957
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS-EXCEPTION",
        "line": 12987
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS-EXCEPTION",
        "line": 13000
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS-EXCEPTION",
        "line": 13016
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-OPEN-DB-2",
        "line": 13026
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS-EXCEPTION",
        "line": 13033
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DISP-COMPRESS",
        "line": 13058
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DISP-COMPRESS",
        "line": 13128
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-FREE",
        "line": 13209
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-RELOCK",
        "line": 13213
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS-EXCEPTION",
        "line": 13220
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-FREE",
        "line": 13268
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-RELOCK",
        "line": 13272
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-BEGIN-TRANS",
        "line": 13274
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS-EXCEPTION",
        "line": 13282
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS2-CLEAR-MODIFY-FLAGS",
        "line": 13288
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DMS-EXCEPTION",
        "line": 13302
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-CLOSE-DB-1",
        "line": 13312
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-OPEN-DB-1",
        "line": 13313
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-CLOSE-DB-2",
        "line": 13314
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-OPEN-DB-2",
        "line": 13315
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 13426
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 13428
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-ADD-1ST-YR",
        "line": 13430
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-ADD-D",
        "line": 13432
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-SUBTRACT-1ST-YR",
        "line": 13436
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-SUBTRACT-D",
        "line": 13438
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INCREMENT-YY-CC",
        "line": 13458
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 13460
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 13462
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INCREMENT-YY-CC",
        "line": 13472
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 13474
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 13476
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-DECREMENT-YY-CC",
        "line": 13489
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 13491
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 13493
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INCREMENT-YY-CC",
        "line": 13508
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 13510
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 13512
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INCREMENT-YY-CC",
        "line": 13520
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 13522
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 13524
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-DECREMENT-YY-CC",
        "line": 13546
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-DECREMENT-YY-CC",
        "line": 13550
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 13552
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 13554
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-DECREMENT-YY-CC",
        "line": 13563
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 13565
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 13567
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-DECREMENT-YY-CC",
        "line": 13575
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 13577
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 13579
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-ADD-M",
        "line": 13598
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-SUBTRACT-M",
        "line": 13601
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "line": 13702
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-CONVERT-MDY-TO-JUL",
        "line": 13717
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-DATE-1",
        "line": 13746
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-DATE-2",
        "line": 13748
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-DATE-3",
        "line": 13750
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-UNITS",
        "line": 13756
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-MATH-WA",
        "line": 13758
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-JUL-MDY",
        "line": 13760
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-LEAP-YR",
        "line": 13762
      },
      {
        "from": "000026*REMARKS",
        "to": "Z-DATE-INIT-CVRT-STATUS",
        "line": 13764
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-RPT-1-ADV-PAGE-CNT",
        "line": 13967
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-1-PROCEDURE",
        "line": 13970
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-RPT-2-ADV-PAGE-CNT",
        "line": 14062
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-2-PROCEDURE",
        "line": 14065
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS-EXCEPTION",
        "line": 14123
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS-EXCEPTION",
        "line": 14136
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS-EXCEPTION",
        "line": 14154
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS-EXCEPTION",
        "line": 14167
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "GET-BANK-INFO",
        "line": 14280
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-4-PROCEDURE",
        "line": 14281
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "GET-ACCT-INFO",
        "line": 14293
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-5-PROCEDURE",
        "line": 14294
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "CLOSE-FM-FILE-RPT",
        "line": 14306
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-6-PROCEDURE",
        "line": 14307
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "GET-BANK-INFO",
        "line": 14351
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-4-PROCEDURE",
        "line": 14352
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "GET-ACCT-INFO",
        "line": 14364
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-5-PROCEDURE",
        "line": 14365
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "CLOSE-FM-FILE-RPT",
        "line": 14378
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-6-PROCEDURE",
        "line": 14379
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "GET-BANK-INFO",
        "line": 14513
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-4-PROCEDURE",
        "line": 14514
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "GET-ACCT-INFO",
        "line": 14526
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-5-PROCEDURE",
        "line": 14527
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "CLOSE-FM-FILE-RPT",
        "line": 14539
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-6-PROCEDURE",
        "line": 14540
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS2-BEGIN-TRANS",
        "line": 14571
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS2-FREE",
        "line": 14577
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS2-END-TRANS",
        "line": 14584
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS2-FREE",
        "line": 14596
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS2-END-TRANS",
        "line": 14600
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS2-FREE",
        "line": 14712
      },
      {
        "from": "027782*Z-USERS-DECLARATIONS-PARAGRAPH",
        "to": "Z-DMS2-END-TRANS",
        "line": 14716
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-REMOTE-LBL-CHK",
        "line": 14775
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-RMT-LBL-CHK",
        "line": 14776
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "ONCE",
        "line": 14797
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT1",
        "line": 14836
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-REMOTE-LBL-CHK",
        "line": 14863
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-RMT-LBL-CHK",
        "line": 14864
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-NEW-NAME-CHK",
        "line": 14872
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "99-PRT-REMOTE-LBL-CHK",
        "line": 14878
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "TPR-REMOTE-BANK",
        "line": 14879
      },
      {
        "from": "029486*L\"S\"/\"GENL\"/\"PRINTER-PR\"",
        "to": "Z-8-PROCEDURE",
        "line": 14880
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-DMS-EXCEPTION",
        "line": 15669
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "SETUP-ACCT-NO-READ",
        "line": 15678
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-11-PROCEDURE",
        "line": 15679
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "TDD-TDAA-MOVE-TO-TDB",
        "line": 15708
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-12-PROCEDURE",
        "line": 15709
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "TDD-TDAA-MOVE-TO-HOLD",
        "line": 15717
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-13-PROCEDURE",
        "line": 15718
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "TDB-CUST-INQ",
        "line": 15740
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-14-PROCEDURE",
        "line": 15741
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "TDB-IRAUPD-INQ",
        "line": 16068
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "Z-15-PROCEDURE",
        "line": 16069
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "99-PRT-LABEL-CHECK",
        "line": 16360
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "999999-CHANGE1",
        "line": 16398
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "999999-CHANGE24",
        "line": 16399
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "999999-CHANGE54",
        "line": 16452
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "999999-CHANGE34",
        "line": 16453
      },
      {
        "from": "030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"",
        "to": "999999-CHANGE55",
        "line": 16456
      },
      {
        "from": "032926********ENDIF",
        "to": "TPR-TEAR-PAGES",
        "line": 16481
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-21-PROCEDURE",
        "line": 16482
      },
      {
        "from": "032926********ENDIF",
        "to": "99-PRT-LABEL-CHECK",
        "line": 16513
      },
      {
        "from": "032926********ENDIF",
        "to": "999999-CHANGE22",
        "line": 16553
      },
      {
        "from": "032926********ENDIF",
        "to": "999999-CHANGE33",
        "line": 16554
      },
      {
        "from": "032926********ENDIF",
        "to": "HEADING-SETUP",
        "line": 16597
      },
      {
        "from": "032926********ENDIF",
        "to": "Z-16-PROCEDURE",
        "line": 16598
      },
      {
        "from": "032926********ENDIF",
        "to": "999999-CHANGE72",
        "line": 16611
      },
      {
        "from": "032926********ENDIF",
        "to": "999999-CHANGE52",
        "line": 16615
      },
      {
        "from": "032926********ENDIF",
        "to": "999999-CHANGE53",
        "line": 16618
      },
      {
        "from": "032926********ENDIF",
        "to": "999999-CHANGE73",
        "line": 16622
      },
      {
        "from": "033256********ENDIF",
        "to": "TPR-TEAR-PAGES",
        "line": 16644
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-21-PROCEDURE",
        "line": 16645
      },
      {
        "from": "033256********ENDIF",
        "to": "HEADING-SETUP",
        "line": 16744
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-16-PROCEDURE",
        "line": 16745
      },
      {
        "from": "033256********ENDIF",
        "to": "TPR-TEAR-PAGES",
        "line": 16754
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-21-PROCEDURE",
        "line": 16755
      },
      {
        "from": "033256********ENDIF",
        "to": "999999-CHANGE54",
        "line": 16774
      },
      {
        "from": "033256********ENDIF",
        "to": "999999-CHANGE34",
        "line": 16775
      },
      {
        "from": "033256********ENDIF",
        "to": "999999-CHANGE55",
        "line": 16778
      },
      {
        "from": "033256********ENDIF",
        "to": "HEADING-SETUP",
        "line": 16837
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-16-PROCEDURE",
        "line": 16838
      },
      {
        "from": "033256********ENDIF",
        "to": "TPR-TEAR-PAGES",
        "line": 16847
      },
      {
        "from": "033256********ENDIF",
        "to": "Z-21-PROCEDURE",
        "line": 16848
      },
      {
        "from": "033256********ENDIF",
        "to": "999999-CHANGE72",
        "line": 16868
      },
      {
        "from": "033256********ENDIF",
        "to": "999999-CHANGE52",
        "line": 16872
      },
      {
        "from": "033256********ENDIF",
        "to": "999999-CHANGE53",
        "line": 16875
      },
      {
        "from": "033256********ENDIF",
        "to": "999999-CHANGE73",
        "line": 16879
      },
      {
        "from": "033774*****ENDIF",
        "to": "RMDRPT-SETUP",
        "line": 16908
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-24-PROCEDURE",
        "line": 16909
      },
      {
        "from": "033774*****ENDIF",
        "to": "RMDRPT2-SETUP",
        "line": 16928
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-25-PROCEDURE",
        "line": 16929
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 16952
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 16968
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "line": 16970
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 16981
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "line": 16983
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "line": 16986
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "line": 16988
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "line": 16991
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 16994
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 16996
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 17005
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "line": 17007
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 17018
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "line": 17020
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "line": 17023
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-M",
        "line": 17025
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "line": 17028
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "line": 17031
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 17034
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 17036
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 17046
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 17061
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "line": 17063
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 17074
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "line": 17076
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "line": 17079
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "line": 17081
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "line": 17084
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 17087
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 17089
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 17099
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 17111
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "line": 17113
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 17124
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "line": 17126
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "line": 17129
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "line": 17131
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "line": 17134
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 17137
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 17139
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 17149
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 17168
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "line": 17170
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 17181
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "line": 17183
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "line": 17186
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "line": 17188
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "line": 17191
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 17194
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 17196
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 17217
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 17233
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "line": 17235
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 17246
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "line": 17248
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "line": 17251
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "line": 17253
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "line": 17256
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 17259
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 17261
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 17272
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 17287
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 17349
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 17558
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "line": 17578
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "line": 17601
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "line": 17619
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 17660
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 17673
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 17689
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 17725
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 17763
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 17809
      },
      {
        "from": "033774*****ENDIF",
        "to": "CLOSE-PRT-FILE",
        "line": 17811
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-22-PROCEDURE",
        "line": 17812
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "line": 17825
      },
      {
        "from": "033774*****ENDIF",
        "to": "CLOSE-PRT-FILE",
        "line": 17827
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-22-PROCEDURE",
        "line": 17828
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 17885
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 18325
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 18341
      },
      {
        "from": "033774*****ENDIF",
        "to": "WRITE-CUST-FM-REC",
        "line": 18645
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-26-PROCEDURE",
        "line": 18646
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 18668
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 18685
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 18781
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "line": 19527
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-YY-DIFF",
        "line": 19542
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 19554
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "line": 19556
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 19567
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "line": 19569
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "line": 19572
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "line": 19574
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "line": 19577
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 19580
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 19582
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 19658
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 19677
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 19696
      },
      {
        "from": "033774*****ENDIF",
        "to": "COMB-AUTO-RMD-ADJ",
        "line": 19719
      },
      {
        "from": "033774*****ENDIF",
        "to": "COMB-AUTO-RMD-ADJ",
        "line": 19723
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-27-PROCEDURE",
        "line": 19724
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 19754
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 19767
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "line": 19792
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "line": 19805
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 19826
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 19847
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 19865
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 19887
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 19905
      },
      {
        "from": "033774*****ENDIF",
        "to": "TDD-MINDIST-SETUP-AND-CALC",
        "line": 20022
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-28-PROCEDURE",
        "line": 20023
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-FL-EXCEPTION",
        "line": 20080
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-FL-EXCEPTION",
        "line": 20116
      },
      {
        "from": "033774*****ENDIF",
        "to": "WRITE-REPORT",
        "line": 20134
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-PROCEDURE",
        "line": 20135
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-FL-EXCEPTION",
        "line": 20245
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-FL-EXCEPTION",
        "line": 20292
      },
      {
        "from": "033774*****ENDIF",
        "to": "TDD-MINDIST-SETUP-AND-CALC",
        "line": 20322
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-28-PROCEDURE",
        "line": 20323
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-FL-EXCEPTION",
        "line": 20381
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-FL-EXCEPTION",
        "line": 20417
      },
      {
        "from": "033774*****ENDIF",
        "to": "WRITE-REPORT",
        "line": 20434
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-23-PROCEDURE",
        "line": 20435
      },
      {
        "from": "033774*****ENDIF",
        "to": "WRITE-CUST-FM-REC",
        "line": 20482
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-26-PROCEDURE",
        "line": 20483
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 20550
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 20569
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 20588
      },
      {
        "from": "033774*****ENDIF",
        "to": "COMB-AUTO-RMD-ADJ",
        "line": 20611
      },
      {
        "from": "033774*****ENDIF",
        "to": "COMB-AUTO-RMD-ADJ",
        "line": 20615
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-27-PROCEDURE",
        "line": 20616
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 20646
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 20659
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "line": 20684
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "line": 20697
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 20716
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 20733
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "line": 20751
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "line": 20768
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "line": 20808
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "line": 20809
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "line": 20823
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "line": 20824
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "line": 20832
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "line": 20833
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "line": 20842
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "line": 20843
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-PRINT-TEAR",
        "line": 20864
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-30-PROCEDURE",
        "line": 20865
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "line": 20938
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "line": 20939
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "line": 20947
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "line": 20948
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "line": 20972
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "line": 20973
      },
      {
        "from": "033774*****ENDIF",
        "to": "TPR-WRITE-TEAR",
        "line": 20981
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-29-PROCEDURE",
        "line": 20982
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-1-NEWPAGE",
        "line": 21041
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-RPT-2-NEWPAGE",
        "line": 21059
      },
      {
        "from": "033774*****ENDIF",
        "to": "CHECK-PRT-FILE",
        "line": 21089
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-20-PROCEDURE",
        "line": 21090
      },
      {
        "from": "033774*****ENDIF",
        "to": "SETUP-NEW-REPORT",
        "line": 21106
      },
      {
        "from": "033774*****ENDIF",
        "to": "SETUP-NEW-REPORT",
        "line": 21110
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-18-PROCEDURE",
        "line": 21111
      },
      {
        "from": "033774*****ENDIF",
        "to": "CHECK-PRT-FILE",
        "line": 21146
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-20-PROCEDURE",
        "line": 21147
      },
      {
        "from": "033774*****ENDIF",
        "to": "SETUP-NEW-REPORT",
        "line": 21163
      },
      {
        "from": "033774*****ENDIF",
        "to": "SETUP-NEW-REPORT",
        "line": 21167
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-18-PROCEDURE",
        "line": 21168
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-FL-EXCEPTION",
        "line": 21270
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-FL-EXCEPTION",
        "line": 21429
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 22899
      },
      {
        "from": "033774*****ENDIF",
        "to": "TDB-CUST-01BAT2-ACTV-ADJ",
        "line": 22917
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-32-PROCEDURE",
        "line": 22918
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 23542
      },
      {
        "from": "033774*****ENDIF",
        "to": "TDB-IRA-01BAT4-ACTV-ADJ",
        "line": 23560
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-33-PROCEDURE",
        "line": 23561
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-REGS",
        "line": 23747
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "line": 23749
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 23760
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-MDY-TO-JUL-CTRL",
        "line": 23762
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALCULATIONS",
        "line": 23765
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-Y",
        "line": 23767
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-C",
        "line": 23770
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-LEAP-YEAR",
        "line": 23773
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-CALC-MONTH-DAYS",
        "line": 23775
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "line": 23783
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-YY-DIFF",
        "line": 23798
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "line": 23800
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-YY-DIFF",
        "line": 23815
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-INITIALIZE-CTRL",
        "line": 23822
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DATE-YY-DIFF",
        "line": 23837
      },
      {
        "from": "033774*****ENDIF",
        "to": "CALC-MINDIST-AMT",
        "line": 23854
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-34-PROCEDURE",
        "line": 23855
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 24173
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 24189
      },
      {
        "from": "033774*****ENDIF",
        "to": "TDB-ACTV-ADJUSTMENT",
        "line": 24262
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-35-PROCEDURE",
        "line": 24263
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 24289
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 24412
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 24428
      },
      {
        "from": "033774*****ENDIF",
        "to": "TDB-ACTV-ADJUSTMENT",
        "line": 24495
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-35-PROCEDURE",
        "line": 24496
      },
      {
        "from": "033774*****ENDIF",
        "to": "Z-DMS-EXCEPTION",
        "line": 24522
      }
    ],
    "total_nodes": 25,
    "total_edges": 1890
  },
  "gnucobol_analysis": {
    "summary": {},
    "program_calls": [],
    "call_summary": {},
    "paragraphs": [],
    "sections": [],
    "performs": []
  },
  "ctags_outline": {
    "program_name": null,
    "divisions": [],
    "paragraphs": [],
    "total_paragraphs": 0,
    "sections": [],
    "performs": [],
    "data_items": []
  },
  "program_map": "\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nPROGRAM MAP: TDAS-MINDISTCALC\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n\u2502\n\u2502 Total Paragraphs: 0\n\u2502 Total Data Items: 0\n\u2502 External Calls: 21\n\u2502\n\u251c\u2500\u2500 IDENTIFICATION DIVISION\n\u2502   \u2514\u2500\u2500 PROGRAM-ID: TDAS-MINDISTCALC\n\u2502\n\u2514\u2500\u2500 PROCEDURE DIVISION\n    \u2502\n    \u251c\u2500\u2500 Top 50 Most Important Paragraphs:\n    \u2502   # 1  Z-35-2-ENDIF  [Importance: 646]\n    \u2502   # 2  Z-DMS-EXCEPTION  [Importance: 210]\n    \u2502   # 3  Z-DATE-CALC-LEAP-YEAR  [Importance: 175]\n    \u2502   # 4  Z-RPT-1-NEWPAGE  [Importance: 140]\n    \u2502   # 5  Z-DATE-CALC-MONTH-DAYS  [Importance: 119]\n    \u2502   # 6  Z-DATE-INITIALIZE-REGS  [Importance: 119]\n    \u2502   # 7  Z-DATE-INITIALIZE-CTRL  [Importance: 84]\n    \u2502   # 8  030040*L\"S\"/\"GENL\"/\"RMTPRTLBL\"  [Importance: 80]\n    \u2502   # 9  Z-RPT-2-NEWPAGE  [Importance: 77]\n    \u2502   #10  Z-DATE-MDY-TO-JUL-CTRL  [Importance: 63]\n    \u2502   #11  Z-5-XIT  [Importance: 58]\n    \u2502   #12  CALCULATIONS  [Importance: 56]\n    \u2502   #13  Z-DATE-CALC-Y  [Importance: 56]\n    \u2502   #14  Z-DATE-CALC-C  [Importance: 56]\n    \u2502   #15  Z-FL-EXCEPTION  [Importance: 56]\n    \u2502   #16  TPR-WRITE-TEAR  [Importance: 56]\n    \u2502   #17  Z-29-PROCEDURE  [Importance: 56]\n    \u2502   #18  Z-3-XIT  [Importance: 56]\n    \u2502   #19  032926********ENDIF  [Importance: 40]\n    \u2502   #20  033256********ENDIF  [Importance: 40]\n    \u2502   #21  Z-DMS2-END-TRANS  [Importance: 37]\n    \u2502   #22  Z-DMS2-FREE  [Importance: 35]\n    \u2502   #23  Z-DATE-DECREMENT-YY-CC  [Importance: 35]\n    \u2502   #24  Z-DMS2-BEGIN-TRANS  [Importance: 30]\n    \u2502   #25  Z-DATE-INCREMENT-YY-CC  [Importance: 28]\n    \u2502   #26  TPR-TEAR-PAGES  [Importance: 28]\n    \u2502   #27  Z-21-PROCEDURE  [Importance: 28]\n    \u2502   #28  Z-DATE-YY-DIFF  [Importance: 28]\n    \u2502   #29  COMB-AUTO-RMD-ADJ  [Importance: 28]\n    \u2502   #30  SETUP-NEW-REPORT  [Importance: 28]\n    \u2502   #31  Z-21-XIT  [Importance: 26]\n    \u2502   #32  Z-5-14-END  [Importance: 24]\n    \u2502   #33  Z-30-XIT  [Importance: 22]\n    \u2502   #34  Z-OPEN-DB-2  [Importance: 21]\n    \u2502   #35  GET-BANK-INFO  [Importance: 21]\n    \u2502   #36  Z-4-PROCEDURE  [Importance: 21]\n    \u2502   #37  GET-ACCT-INFO  [Importance: 21]\n    \u2502   #38  Z-5-PROCEDURE  [Importance: 21]\n    \u2502   #39  CLOSE-FM-FILE-RPT  [Importance: 21]\n    \u2502   #40  Z-6-PROCEDURE  [Importance: 21]\n    \u2502   #41  99-PRT-REMOTE-LBL-CHK  [Importance: 21]\n    \u2502   #42  HEADING-SETUP  [Importance: 21]\n    \u2502   #43  Z-16-PROCEDURE  [Importance: 21]\n    \u2502   #44  000026*REMARKS  [Importance: 20]\n    \u2502   #45  033774*****ENDIF  [Importance: 20]\n    \u2502   #46  Z-11-XIT  [Importance: 18]\n    \u2502   #47  Z-22-XIT  [Importance: 18]\n    \u2502   #48  99-NEW-END  [Importance: 16]\n    \u2502   #49  Z-PROCESS-INIT  [Importance: 14]\n    \u2502   #50  Z-OPEN-DB-1  [Importance: 14]\n    \u2502\n    \u2514\u2500\u2500 External Calls (21 total):\n        \u251c\u2500> CURRENT_DATE OF GENERALSUPPORT (called 16 times)\n        \u251c\u2500> XSTRPAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCAT OF XGEN/RUNTIME/LIBRARY (called 2 times)\n        \u251c\u2500> XSTRCOMPRESS OF XGEN/RUNTIME/LIBRARY (called 1 times)\n\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\nMap Token Count: ~779\n\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550"
}

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
- Has source_code: No
- Source code length: 0 characters

### Program Map Present
- Has program_map: Yes
- Program map length: 3219 characters

### Other Context Keys
- program_name: str
- timestamp: str
- superbol_symbols: dict
- superbol_cfg: dict
- gnucobol_analysis: dict
- ctags_outline: dict

---

## Full Source Code (if present)

*(No source code in context)*

---

## Program Map (if present)


```
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
```

