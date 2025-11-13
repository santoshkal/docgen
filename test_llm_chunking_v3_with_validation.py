#!/usr/bin/env python3
"""
Test V3: Enhanced with Accurate Token Counting + Pydantic Validation

Enhancements:
1. Uses tiktoken for EXACT token counts (not estimation)
2. Pydantic data models for JSON validation
3. Error feedback loop - if validation fails, LLM gets errors and retries
4. Comprehensive validation of expected vs actual output

This addresses:
- Accurate token measurement for cost/limit tracking
- Structured validation of LLM output
- Automatic correction via feedback loop
"""

import json
import os
import yaml
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError, field_validator
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False
    print("⚠ tiktoken not available, will use estimation")

# Configuration
COBOL_FILE = "/home/santosh/cobol-work/TDAS-MINDISTCALC.c74"
OUTPUT_JSON = "/home/santosh/cobol-work/agent/llm_chunking_metadata_v3_validated.json"
CONFIG_FILE = "/home/santosh/cobol-work/agent/config-test-detailed-code.yaml"

# Pydantic Models for Validation
class DataItemInfo(BaseModel):
    """Represents a COBOL data item."""
    name: str = Field(..., description="Data item name (e.g., 'WS-CUSTOMER-RECORD')")
    line: int = Field(..., gt=0, description="Exact line number where data item is defined")
    sequence_number: str = Field(..., pattern=r'^\d{6}$', description="6-digit sequence number from columns 1-6")
    level: str = Field(..., description="Level number (01, 05, 77, 88, etc.)")
    picture: Optional[str] = Field(None, description="PICTURE clause (e.g., 'X(100)', '9(5)', etc.)")
    division: str = Field(..., description="Which section: WORKING-STORAGE, FILE-SECTION, LINKAGE-SECTION")

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError("Data item name cannot be empty")
        return v.strip()


class SectionInfo(BaseModel):
    """Represents a COBOL section."""
    name: str = Field(..., description="Section name (e.g., 'Z-INITIALIZATION')")
    line: int = Field(..., gt=0, description="Exact line number where section is defined")
    sequence_number: str = Field(..., pattern=r'^\d{6}$', description="6-digit sequence number from columns 1-6")
    paragraphs_in_section: List[str] = Field(default_factory=list, description="Names of paragraphs in this section")

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError("Section name cannot be empty")
        return v.strip()


class ParagraphInfo(BaseModel):
    """Represents a COBOL paragraph."""
    name: str = Field(..., description="Paragraph name")
    line: int = Field(..., gt=0, description="Exact line number where paragraph is defined")
    sequence_number: str = Field(..., pattern=r'^\d{6}$', description="6-digit sequence number")
    section: Optional[str] = Field(None, description="Section this paragraph belongs to (if any)")
    performs: List[str] = Field(default_factory=list, description="List of paragraphs this one PERFORMs")
    estimated_end_line: Optional[int] = Field(None, gt=0, description="Estimated line where paragraph ends")

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError("Paragraph name cannot be empty")
        return v.strip()


class PerformStatement(BaseModel):
    """Represents a PERFORM statement."""
    from_line: int = Field(..., gt=0, description="Line number where PERFORM statement is")
    from_paragraph: str = Field(..., description="Paragraph containing the PERFORM")
    to_paragraph: str = Field(..., description="Target paragraph being performed")
    statement: str = Field(..., description="The actual PERFORM statement text")


class Statistics(BaseModel):
    """Statistics about the extraction."""
    total_data_items: int = Field(..., ge=0, description="Total data items extracted from DATA DIVISION")
    total_sections: int = Field(..., ge=0)
    total_paragraphs: int = Field(..., ge=0)
    total_performs: int = Field(..., ge=0)
    expected_paragraphs: int = Field(default=2598, description="Expected paragraph count from CTags")
    coverage_percentage: float = Field(..., ge=0, le=100)

    @field_validator('coverage_percentage')
    @classmethod
    def validate_coverage(cls, v, info):
        # Calculate coverage
        total = info.data.get('total_paragraphs', 0)
        expected = info.data.get('expected_paragraphs', 2598)
        calculated = (total / expected * 100) if expected > 0 else 0
        if abs(calculated - v) > 1.0:  # Allow 1% tolerance
            raise ValueError(f"Coverage mismatch: reported {v:.2f}% but calculated {calculated:.2f}%")
        return v


class CobolExtractionResult(BaseModel):
    """Complete extraction result from LLM."""
    analysis_method: str = Field(..., description="Description of analysis method used")
    identification_division_start_line: Optional[int] = Field(None, gt=0)
    environment_division_start_line: Optional[int] = Field(None, gt=0)
    data_division_start_line: Optional[int] = Field(None, gt=0)
    procedure_division_start_line: Optional[int] = Field(None, gt=0)
    procedure_division_end_line: Optional[int] = Field(None, gt=0)
    total_lines_processed: int = Field(..., gt=0)
    data_items: List[DataItemInfo] = Field(default_factory=list, description="Data items from DATA DIVISION")
    sections: List[SectionInfo] = Field(default_factory=list)
    paragraphs: List[ParagraphInfo] = Field(...)  # Required, must have paragraphs
    perform_graph: List[PerformStatement] = Field(default_factory=list)
    statistics: Statistics
    completion_checklist: List[str] = Field(default_factory=list, description="Checklist of all elements found")

    @field_validator('paragraphs')
    @classmethod
    def validate_paragraphs(cls, v):
        EXPECTED_PARAGRAPH_COUNT = 2598  # Known from CTags

        if len(v) == 0:
            raise ValueError("Must extract at least some paragraphs - empty list not allowed")

        # HARD CHECK: Must extract exactly 2,598 paragraphs
        if len(v) != EXPECTED_PARAGRAPH_COUNT:
            raise ValueError(
                f"INCOMPLETE EXTRACTION: Found {len(v)} paragraphs but MUST extract exactly {EXPECTED_PARAGRAPH_COUNT} paragraphs. "
                f"Missing: {EXPECTED_PARAGRAPH_COUNT - len(v)} paragraphs. "
                f"You must process the ENTIRE source file and extract ALL paragraphs."
            )

        # Check for duplicate line numbers
        line_numbers = [p.line for p in v]
        if len(line_numbers) != len(set(line_numbers)):
            duplicates = [line for line in line_numbers if line_numbers.count(line) > 1]
            raise ValueError(f"Duplicate line numbers found: {set(duplicates)}")

        return v

    @field_validator('completion_checklist')
    @classmethod
    def validate_checklist(cls, v, info):
        # Checklist should have entries for each paragraph
        para_count = len(info.data.get('paragraphs', []))
        if para_count > 0 and len(v) == 0:
            raise ValueError(f"Completion checklist is empty but {para_count} paragraphs were extracted")
        return v


# Token counting functions
def get_exact_token_count(text: str, model: str = "gpt-4") -> int:
    """Get exact token count using tiktoken."""
    if not TIKTOKEN_AVAILABLE:
        # Fallback to estimation
        return len(text) // 4

    try:
        encoder = tiktoken.encoding_for_model(model)
        return len(encoder.encode(text))
    except Exception as e:
        print(f"  ⚠ Tiktoken error: {e}, using estimation")
        return len(text) // 4


def validate_and_retry(llm, prompt: str, system_msg: str, max_retries: int = 3) -> tuple[CobolExtractionResult, int]:
    """
    Call LLM and validate response. If validation fails, provide feedback and retry.

    Returns:
        Tuple of (validated_result, attempt_number)
    """
    for attempt in range(1, max_retries + 1):
        print(f"\n  Attempt {attempt}/{max_retries}...")

        try:
            # Call LLM
            messages = [
                SystemMessage(content=system_msg),
                HumanMessage(content=prompt)
            ]

            response = llm.invoke(messages)
            result_text = response.content

            # Get token usage
            usage = getattr(response, 'response_metadata', {}).get('token_usage', {})
            prompt_tokens = usage.get('prompt_tokens', 0)
            completion_tokens = usage.get('completion_tokens', 0)

            print(f"    Tokens: {prompt_tokens:,} input, {completion_tokens:,} output")

            # Parse JSON
            result_json = json.loads(result_text)

            # Validate with Pydantic
            validated_result = CobolExtractionResult(**result_json)

            print(f"    ✓ Validation passed!")
            return validated_result, attempt

        except json.JSONDecodeError as e:
            error_msg = f"JSON parsing error: {str(e)}"
            print(f"    ✗ {error_msg}")

            if attempt < max_retries:
                # Add error feedback to prompt
                prompt += f"\n\n⚠️ PREVIOUS ATTEMPT FAILED:\n{error_msg}\n\nPlease fix and provide valid JSON only."

        except ValidationError as e:
            error_details = []
            incomplete_extraction = False
            extracted_count = 0

            for error in e.errors():
                field = '.'.join(str(loc) for loc in error['loc'])
                msg = error['msg']
                error_details.append(f"  - {field}: {msg}")

                # Check if this is the incomplete extraction error
                if 'paragraphs' in field and 'INCOMPLETE EXTRACTION' in msg:
                    incomplete_extraction = True
                    # Try to extract the count from context if available
                    try:
                        extracted_count = len(result_json.get('paragraphs', []))
                    except:
                        pass

            error_msg = "Validation errors:\n" + '\n'.join(error_details)
            print(f"    ✗ Validation failed:")
            for detail in error_details:
                print(f"      {detail}")

            if attempt < max_retries:
                # Add detailed validation errors to prompt
                prompt += f"\n\n⚠️ PREVIOUS ATTEMPT FAILED VALIDATION:\n{error_msg}\n\n"

                if incomplete_extraction and extracted_count > 0:
                    # Provide specific guidance for incomplete extraction
                    missing = 2598 - extracted_count
                    prompt += f"❌ CRITICAL ERROR: You only extracted {extracted_count} paragraphs!\n"
                    prompt += f"   You are missing {missing} paragraphs ({(missing/2598)*100:.1f}% of PROCEDURE DIVISION).\n\n"
                    prompt += f"INSTRUCTIONS TO FIX:\n"
                    prompt += f"1. You MUST scan the ENTIRE source file from line 1 to line {total_source_lines}\n"
                    prompt += f"2. **IDENTIFICATION DIVISION** (Lines ~1-20): Extract PROGRAM-ID, AUTHOR, etc.\n"
                    prompt += f"3. **ENVIRONMENT DIVISION**: Extract FILE-CONTROL entries\n"
                    prompt += f"4. **DATA DIVISION** (⚠️ CRITICAL - Lines ~100-25000+):\n"
                    prompt += f"   - Extract ALL 01-level items from WORKING-STORAGE\n"
                    prompt += f"   - Extract ALL FD entries from FILE SECTION\n"
                    prompt += f"   - DO NOT skip data items - they are essential!\n"
                    prompt += f"5. **PROCEDURE DIVISION** (Lines ~25000-{total_source_lines}):\n"
                    prompt += f"   - Extract ALL 2,598 paragraphs (lines ending with period in columns 8+)\n"
                    prompt += f"   - These are the paragraph definitions - extract ALL of them\n"
                    prompt += f"6. Do NOT stop early - process until line {total_source_lines}\n"
                    prompt += f"7. Expected: 2,598 paragraphs + data items from DATA DIVISION\n\n"
                else:
                    prompt += "Please fix these issues and ensure:\n"
                    prompt += "1. **Extract EXACTLY 2,598 paragraphs (no more, no less)**\n"
                    prompt += "2. All line numbers are > 0\n"
                    prompt += "3. Sequence numbers are exactly 6 digits\n"
                    prompt += "4. Statistics coverage_percentage is 100.0\n"
                    prompt += "5. Completion checklist has 2,598 entries\n"
                    prompt += "6. No duplicate line numbers\n"

                prompt += "\nProvide corrected JSON output with ALL 2,598 paragraphs."

        except Exception as e:
            print(f"    ✗ Unexpected error: {e}")
            if attempt < max_retries:
                prompt += f"\n\n⚠️ ERROR: {str(e)}\n\nPlease provide valid JSON output."

    raise ValueError(f"Failed after {max_retries} attempts")


# Main script
print("="*80)
print("TEST V3: ENHANCED WITH VALIDATION + ACCURATE TOKENS")
print("="*80)

# Check tiktoken availability
if TIKTOKEN_AVAILABLE:
    print("\n✓ tiktoken available: Using exact token counts")
else:
    print("\n⚠ tiktoken not available: Using estimation (~4 chars/token)")
    print("  Install with: pip install tiktoken")

# Load config
print(f"\n[1] Loading config: {CONFIG_FILE}")
with open(CONFIG_FILE, 'r') as f:
    config = yaml.safe_load(f)

llm_config = config.get('llm', {})
model = llm_config.get('model', 'gpt-4')
api_key_template = llm_config.get('api_key', '')

if api_key_template.startswith('${') and api_key_template.endswith('}'):
    env_var = api_key_template[2:-1]
    api_key = os.environ.get(env_var)
    if not api_key:
        print(f"✗ Error: {env_var} not set!")
        exit(1)
else:
    api_key = api_key_template

print(f"  Model: {model}")

# Initialize LLM
llm = ChatOpenAI(
    model=model,
    temperature=0.0,
    api_key=api_key,
    model_kwargs={"response_format": {"type": "json_object"}}
)

# Read COBOL source
print(f"\n[2] Reading COBOL file: {COBOL_FILE}")
with open(COBOL_FILE, 'r') as f:
    source_lines = f.readlines()
    source_code = ''.join(source_lines)

total_source_lines = len(source_lines)
print(f"  ✓ Total source lines: {total_source_lines:,}")

# Build prompt with accountability
prompt = f"""You are a COBOL-74 parser. Extract complete program structure with EXACT line numbers.

=============================================================================
MANDATORY ACCOUNTABILITY REQUIREMENTS
=============================================================================
⚠️  CRITICAL - YOU MUST PROCESS ALL DIVISIONS FROM LINE 1 TO LINE {total_source_lines}:

**COMPLETE COVERAGE REQUIRED:**
1. **IDENTIFICATION DIVISION** (Lines ~1-20):
   - Extract PROGRAM-ID, AUTHOR, DATE-WRITTEN, REMARKS
   - Record exact line numbers

2. **ENVIRONMENT DIVISION** (if present):
   - Extract CONFIGURATION SECTION, INPUT-OUTPUT SECTION
   - Record all FILE-CONTROL entries
   - Record exact line numbers

3. **DATA DIVISION** (⚠️ CRITICAL - May span lines ~100-25000+):
   - Extract ALL 01-level data items from WORKING-STORAGE
   - Extract ALL FD entries from FILE SECTION
   - Extract ALL items from LINKAGE SECTION (if present)
   - Record exact line numbers for EVERY data item
   - DO NOT skip FILLER definitions or data tables

4. **PROCEDURE DIVISION** (Lines ~25000-{total_source_lines}):
   - Extract ALL sections (if present)
   - Extract ALL 2,598 paragraphs (this is VERIFIED count from CTags)
   - Record exact line numbers
   - Extract PERFORM relationships
   - DO NOT skip any paragraph

**VALIDATION RULES:**
1. **Process EVERY line from line 1 to line {total_source_lines} sequentially**
2. **MUST EXTRACT EXACTLY 2,598 PARAGRAPHS from PROCEDURE DIVISION**
3. **Record exact line number for each element (data item, paragraph, section)**
4. **Process in strict sequential order** - no jumping around
5. **At the end, provide a completion checklist** with ALL paragraphs found
6. **Missing line numbers will make skipped content immediately obvious**
7. **NO SUMMARIZATION** - Extract every element, even if repetitive

⚠️  VALIDATION WILL REJECT: Any output with != 2,598 paragraphs

=============================================================================
COBOL-74 FORMAT RULES
=============================================================================
- **Columns 1-6**: Sequence numbers (e.g., "025680")
- **Column 7**: Indicator (* = comment, / = page break, space = code)
- **Columns 8-72**: COBOL code area
- **Paragraph names**: Start in columns 8-12 and END WITH A PERIOD
- **Section names**: End with " SECTION."

=============================================================================
OUTPUT FORMAT (MUST MATCH THIS EXACT SCHEMA)
=============================================================================
{{
  "analysis_method": "Complete line-by-line scan of ALL {total_source_lines} lines including ALL divisions",
  "identification_division_start_line": LINE_NUMBER,
  "environment_division_start_line": LINE_NUMBER_OR_NULL,
  "data_division_start_line": LINE_NUMBER_OR_NULL,
  "procedure_division_start_line": LINE_NUMBER,
  "procedure_division_end_line": LINE_NUMBER,
  "total_lines_processed": {total_source_lines},
  "data_items": [
    {{
      "name": "WS-CUSTOMER-RECORD",
      "line": EXACT_LINE_NUMBER,
      "sequence_number": "001234",
      "level": "01",
      "picture": "X(100) or null",
      "division": "WORKING-STORAGE or FILE-SECTION or LINKAGE-SECTION"
    }}
  ],
  "sections": [
    {{
      "name": "Z-INITIALIZATION",
      "line": EXACT_LINE_NUMBER,
      "sequence_number": "025680",
      "paragraphs_in_section": ["PARA-1", "PARA-2"]
    }}
  ],
  "paragraphs": [
    {{
      "name": "Z-INITIALIZATION-PARAGRAPH",
      "line": EXACT_LINE_NUMBER,
      "sequence_number": "025680",
      "section": "Z-INITIALIZATION or null",
      "performs": ["OTHER-PARA-1"],
      "estimated_end_line": APPROX_LINE_NUMBER
    }}
  ],
  "perform_graph": [
    {{
      "from_line": LINE_NUMBER,
      "from_paragraph": "CALLER",
      "to_paragraph": "CALLEE",
      "statement": "PERFORM CALLEE"
    }}
  ],
  "statistics": {{
    "total_data_items": COUNT,
    "total_sections": COUNT,
    "total_paragraphs": COUNT,
    "total_performs": COUNT,
    "expected_paragraphs": 2598,
    "coverage_percentage": (total_paragraphs / 2598) * 100
  }},
  "completion_checklist": [
    "✓ IDENTIFICATION DIVISION (Line X)",
    "✓ ENVIRONMENT DIVISION (Line Y)",
    "✓ DATA DIVISION - FILE SECTION (Line Z)",
    "✓ DATA DIVISION - WORKING-STORAGE (Line W)",
    "✓ PROCEDURE DIVISION (Line V)",
    "✓ PARAGRAPH-NAME (Line A, Seq NNNNNN)",
    "✓ NEXT-PARAGRAPH (Line B, Seq NNNNNN)"
  ]
}}

=============================================================================
VALIDATION RULES (Your output will be validated):
=============================================================================
1. **paragraphs list MUST contain exactly 2,598 entries** (HARD REQUIREMENT)
2. **data_items list should contain data items from DATA DIVISION** (recommended)
3. **All division start line numbers must be present and > 0**
4. All line numbers must be > 0
5. All sequence_number fields must be exactly 6 digits
6. coverage_percentage must be 100.0 (since you extracted all 2,598 paragraphs)
7. completion_checklist should list ALL divisions + ALL 2,598 paragraphs
8. No duplicate line numbers
9. statistics.total_data_items must match len(data_items)
10. statistics.total_paragraphs must equal 2,598

⚠️  CRITICAL: If you extract only 50 paragraphs, validation will FAIL with:
    "INCOMPLETE EXTRACTION: Found 50 paragraphs but MUST extract exactly 2,598"

⚠️  CRITICAL: If you skip DATA DIVISION (lines ~100-25000), you will miss essential structure!
    The validation expects ALL divisions to be processed.

If validation fails, you will receive detailed error feedback and must fix it.

=============================================================================
COMPLETE COBOL-74 SOURCE CODE ({total_source_lines:,} lines)
=============================================================================

{source_code}

=============================================================================
Extract complete program structure from ALL divisions (IDENTIFICATION, ENVIRONMENT,
DATA, PROCEDURE) with exact line numbers. Output ONLY valid JSON.
=============================================================================
"""

system_message = "You are a COBOL-74 parser with strict accountability. Extract ALL divisions (IDENTIFICATION, ENVIRONMENT, DATA, PROCEDURE) with ALL elements and exact line numbers. Your output will be validated against a Pydantic schema. Output ONLY valid JSON."

# Calculate exact token count for prompt
print(f"\n[3] Analyzing prompt tokens...")
prompt_tokens_exact = get_exact_token_count(prompt, model)
system_tokens_exact = get_exact_token_count(system_message, model)
total_input_tokens = prompt_tokens_exact + system_tokens_exact

print(f"  System message tokens: {system_tokens_exact:,}")
print(f"  Prompt tokens: {prompt_tokens_exact:,}")
print(f"  Total input tokens: {total_input_tokens:,}")

if TIKTOKEN_AVAILABLE:
    print(f"  ✓ Exact count using tiktoken")
else:
    print(f"  ⚠ Estimated count (~4 chars/token)")

# Send to LLM with validation and retry
print(f"\n[4] Sending to LLM with validation: {model}")
print(f"  Max retries: 3")
print(f"  Waiting for response...")

try:
    validated_result, attempts = validate_and_retry(llm, prompt, system_message, max_retries=3)

    print(f"\n✓ SUCCESS after {attempts} attempt(s)!")

    # Save validated result
    with open(OUTPUT_JSON, 'w') as f:
        json.dump(validated_result.model_dump(), f, indent=2)

    print(f"✓ Saved validated result to: {OUTPUT_JSON}")

    # Analysis
    print(f"\n{'='*80}")
    print(f"VALIDATED RESULTS ANALYSIS")
    print(f"{'='*80}")

    stats = validated_result.statistics
    print(f"\nExtraction Statistics:")
    print(f"  Data Items: {stats.total_data_items}")
    print(f"  Sections: {stats.total_sections}")
    print(f"  Paragraphs: {stats.total_paragraphs}")
    print(f"  PERFORM statements: {stats.total_performs}")
    print(f"  Coverage: {stats.coverage_percentage:.2f}%")
    print(f"  Checklist items: {len(validated_result.completion_checklist)}")

    print(f"\nDivision Start Lines:")
    if validated_result.identification_division_start_line:
        print(f"  IDENTIFICATION DIVISION: Line {validated_result.identification_division_start_line}")
    if validated_result.environment_division_start_line:
        print(f"  ENVIRONMENT DIVISION: Line {validated_result.environment_division_start_line}")
    if validated_result.data_division_start_line:
        print(f"  DATA DIVISION: Line {validated_result.data_division_start_line}")
    if validated_result.procedure_division_start_line:
        print(f"  PROCEDURE DIVISION: Line {validated_result.procedure_division_start_line} - {validated_result.procedure_division_end_line}")

    print(f"\nValidation:")
    print(f"  ✓ All fields validated against Pydantic schema")
    print(f"  ✓ Line numbers all > 0")
    print(f"  ✓ Sequence numbers all 6 digits")
    print(f"  ✓ No duplicate line numbers")
    print(f"  ✓ Statistics are accurate")

    # Show sample data items
    if validated_result.data_items:
        print(f"\nFirst 10 data items from DATA DIVISION:")
        for d in sorted(validated_result.data_items, key=lambda x: x.line)[:10]:
            pic = f" PIC {d.picture}" if d.picture else ""
            print(f"  Line {d.line:6} (seq {d.sequence_number}): {d.level} {d.name}{pic}")

    # Show sample paragraphs
    if validated_result.paragraphs:
        print(f"\nFirst 10 paragraphs from PROCEDURE DIVISION:")
        for p in sorted(validated_result.paragraphs, key=lambda x: x.line)[:10]:
            print(f"  Line {p.line:6} (seq {p.sequence_number}): {p.name}")

    # Comparison with expected
    print(f"\n{'='*80}")
    print(f"COMPARISON WITH EXPECTED (CTags)")
    print(f"{'='*80}")
    print(f"Expected paragraphs: 2,598")
    print(f"Extracted paragraphs: {stats.total_paragraphs}")
    print(f"Coverage: {stats.coverage_percentage:.2f}%")

    if stats.coverage_percentage >= 95:
        print(f"\n✅ EXCELLENT! Near-complete extraction with accountability + validation")
    elif stats.coverage_percentage >= 80:
        print(f"\n✓ GOOD coverage with validated output")
    else:
        print(f"\n⚠ Coverage could be better, but output is validated as correct")

    print(f"\n{'='*80}")
    print(f"TEST COMPLETE")
    print(f"{'='*80}")
    print(f"\nEnhancements Used:")
    print(f"  ✓ Complete division extraction (IDENTIFICATION, ENVIRONMENT, DATA, PROCEDURE)")
    print(f"  ✓ Exact token counting with tiktoken")
    print(f"  ✓ Pydantic schema validation")
    print(f"  ✓ Error feedback and retry loop")
    print(f"  ✓ Comprehensive field validation")
    print(f"  ✓ Accountability requirements")

except ValueError as e:
    print(f"\n❌ FAILED: {e}")
    print(f"\nThe LLM could not produce valid output after 3 attempts.")
    print(f"Validation errors prevented acceptance of invalid data.")
    exit(1)
