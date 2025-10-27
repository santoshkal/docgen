# COBOL Documentation Agent - Source Extraction Implementation Plan

**Version**: 2.0
**Date**: 2025-10-26
**Approach**: Test-Driven Development (TDD)

---

## ⚠️ CRITICAL: Test-Driven Development Mandate

**ALL implementation MUST follow TDD approach:**

```
1. Write Test First (Red)
   ↓
2. Implement Minimum Code to Pass (Green)
   ↓
3. Refactor (Clean)
   ↓
4. Repeat for Next Feature
```

**No code is written without a failing test first!**

---

## Executive Summary

**Objective**: Enhance COBOL Documentation Agent with four-tier extraction strategy:
- **Tier 1**: Metadata-based structured extraction (file I/O)
- **Tier 2**: Pattern-based extraction (Ripgrep direct CLI)
- **Tier 3**: Multi-file resolution (copybooks, called programs)
- **Tier 4**: Fallback (current metadata-only approach)

**Timeline**: 10 days (phased implementation)
**Risk**: Medium-High (unlimited source extraction)

---

## Implementation Strategy

### Phased Incremental Implementation

**Phase 1: Core Option A** (Days 1-4)
- Source extraction using metadata line numbers + file I/O
- TDD: Write tests for each extractor function first
- All 11 sections enabled
- Deduplication and compression
- **Deliverable**: Working source extraction with 40% token reduction

**Phase 2: Ripgrep Integration** (Days 5-6)
- Pattern-based extraction via Ripgrep direct CLI (no MCP)
- TDD: Write pattern extraction tests first
- SQL, comments, error handlers, etc.
- **Deliverable**: Pattern-based extraction working

**Phase 3: Multi-File Support** (Days 7-9)
- Copybook resolution
- Called program resolution
- TDD: Write multi-file resolver tests first
- **Deliverable**: Multi-file dependencies resolved

**Phase 4: Integration & Polish** (Day 10)
- End-to-end testing
- Optimization
- Documentation

---

## Four-Tier Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ Tier 1: Metadata-Based Structured Extraction (Primary)      │
│   • Python file I/O using metadata line numbers             │
│   • All 11 sections enabled (10 with source, 1 metadata-only)│
│   • No size limits, with deduplication                       │
│   Implementation: Phase 1                                    │
├─────────────────────────────────────────────────────────────┤
│ Tier 2: Ripgrep Pattern-Based Extraction                    │
│   • Direct subprocess calls to ripgrep binary                │
│   • SQL, comments, error handling, custom patterns          │
│   • No MCP overhead (faster, simpler)                        │
│   Implementation: Phase 2                                    │
├─────────────────────────────────────────────────────────────┤
│ Tier 3: Multi-File Resolution                               │
│   • Resolve COPY statements → extract copybook content      │
│   • Resolve CALL statements → find called programs          │
│   • Build dependency graphs                                  │
│   Implementation: Phase 3                                    │
├─────────────────────────────────────────────────────────────┤
│ Tier 4: Fallback (Always Available)                         │
│   • Current two-pass metadata-only approach                  │
│   • Graceful degradation if extraction fails                │
└─────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Core Source Extraction (Option A) - TDD

### Timeline: Days 1-4 (4 days)

### Goal
Implement source code extraction using metadata line numbers + file I/O for all sections.

### TDD Workflow

```
For each feature:
1. Write test in test_source_extractor.py (RED)
2. Run test - should FAIL
3. Implement minimum code in source_extractor.py (GREEN)
4. Run test - should PASS
5. Refactor code (CLEAN)
6. Commit
7. Move to next feature
```

---

### Step 1.1: Setup Test Infrastructure (Day 1 Morning - 2 hours)

#### TDD Cycle 1: Basic Test Structure

**1. Write Test First**

Create: `agent/tests/test_source_extractor.py`

```python
import pytest
from source_extractor import extract_lines

def test_extract_lines_exists():
    """Test that extract_lines function exists"""
    assert callable(extract_lines)

def test_extract_lines_basic():
    """Test basic line extraction"""
    # Create test file
    test_file = "/tmp/test_cobol.cbl"
    with open(test_file, 'w') as f:
        f.write("Line 1\n")
        f.write("Line 2\n")
        f.write("Line 3\n")

    # Test
    result = extract_lines(test_file, 1, 2)

    # Should extract lines 1-2
    assert result == "Line 1\nLine 2\n"
```

**2. Run Test** → Should FAIL (function doesn't exist)

**3. Implement Minimum Code**

Create: `agent/source_extractor.py`

```python
def extract_lines(file_path: str, start: int, end: int) -> str:
    """Extract lines from file."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
        return ''.join(lines[start-1:end])
```

**4. Run Test** → Should PASS

**5. Refactor** → Add error handling, docstrings

**6. Commit** → "feat: add basic extract_lines function"

---

### Step 1.2: Core Extraction Functions (Day 1 Afternoon - 4 hours)

#### TDD Cycles

**Cycle 1: Line Extraction with Validation**

Tests to write first:
```python
def test_extract_lines_invalid_range():
    """Test extraction with invalid line range"""
    with pytest.raises(ValueError):
        extract_lines(file, -1, 10)

def test_extract_lines_file_not_found():
    """Test extraction with non-existent file"""
    with pytest.raises(FileNotFoundError):
        extract_lines("/nonexistent/file", 1, 10)

def test_extract_lines_end_before_start():
    """Test extraction with end < start"""
    with pytest.raises(ValueError):
        extract_lines(file, 10, 5)
```

Then implement validation in `extract_lines()`

**Cycle 2: Line Range Extraction**

Tests first:
```python
def test_extract_lines_by_ranges_single_range():
    """Test extraction with single range"""
    ranges = [(1, 3)]
    result = extract_lines_by_ranges(file, ranges)
    assert "Line 1" in result
    assert "Line 3" in result

def test_extract_lines_by_ranges_multiple_ranges():
    """Test extraction with multiple ranges"""
    ranges = [(1, 2), (5, 6)]
    result = extract_lines_by_ranges(file, ranges)
    assert "Line 1" in result
    assert "Line 5" in result
```

Then implement `extract_lines_by_ranges()`

**Cycle 3: Context Extraction**

Tests first:
```python
def test_extract_lines_with_context():
    """Test extraction with before/after context"""
    result = extract_lines_with_context(file, line=5, before=2, after=2)
    # Should get lines 3-7 (5 ±2)
    assert "Line 3" in result
    assert "Line 7" in result
```

Then implement `extract_lines_with_context()`

---

### Step 1.3: Deduplication System (Day 2 Morning - 3 hours)

#### TDD Cycle: Deduplication

**1. Write Tests First**

```python
def test_compute_source_hash():
    """Test source code hashing for deduplication"""
    source1 = "PROCEDURE DIVISION.\n    DISPLAY 'HELLO'."
    source2 = "PROCEDURE DIVISION.\n    DISPLAY 'HELLO'."
    source3 = "PROCEDURE DIVISION.\n    DISPLAY 'WORLD'."

    hash1 = compute_source_hash(source1)
    hash2 = compute_source_hash(source2)
    hash3 = compute_source_hash(source3)

    assert hash1 == hash2  # Same content, same hash
    assert hash1 != hash3  # Different content, different hash

def test_deduplicate_source_extracts():
    """Test deduplication of source extracts"""
    dedup_map = {}

    source1 = "PROCEDURE DIVISION.\n    PERFORM MAIN-LOGIC."

    # First time - should return source
    result1 = deduplicate_source_extract(source1, "section-1", dedup_map)
    assert result1 == source1
    assert "section-1" in str(dedup_map)

    # Second time with same source - should return reference
    result2 = deduplicate_source_extract(source1, "section-2", dedup_map)
    assert "section-1" in result2  # References first section
    assert "same as" in result2.lower()
```

**2. Run Tests** → Should FAIL

**3. Implement**

```python
import hashlib

def compute_source_hash(source: str) -> str:
    """Compute hash of source code for deduplication."""
    return hashlib.sha256(source.encode()).hexdigest()[:16]

def deduplicate_source_extract(
    source: str,
    section_id: str,
    dedup_map: dict
) -> str:
    """Avoid sending duplicate source to LLM."""
    source_hash = compute_source_hash(source)

    if source_hash in dedup_map:
        previous_section = dedup_map[source_hash]
        return f"[Source code identical to {previous_section} - see above]"

    dedup_map[source_hash] = section_id
    return source
```

**4. Run Tests** → Should PASS

**5. Refactor & Commit**

---

### Step 1.4: Division Extractors (Day 2 Afternoon - 4 hours)

#### TDD Cycle: Division Extraction

**1. Write Tests First**

Create fixture with test metadata:
```python
@pytest.fixture
def test_metadata():
    """Mock metadata from ctags/superbol"""
    return {
        "divisions": [
            {"name": "IDENTIFICATION DIVISION", "line": 1, "end_line": 10},
            {"name": "DATA DIVISION", "line": 257, "end_line": 3129},
            {"name": "PROCEDURE DIVISION", "line": 12835, "end_line": 16882}
        ]
    }

def test_find_division_boundaries(test_metadata):
    """Test finding division start/end lines"""
    boundaries = find_division_boundaries(test_metadata)

    assert "DATA DIVISION" in boundaries
    assert boundaries["DATA DIVISION"] == (257, 3129)
    assert boundaries["PROCEDURE DIVISION"] == (12835, 16882)

def test_extract_data_division(test_cobol_file, test_metadata):
    """Test extracting DATA DIVISION"""
    result = extract_data_division(test_cobol_file, test_metadata)

    assert "DATA DIVISION" in result
    assert "WORKING-STORAGE" in result
    assert len(result) > 0

def test_extract_procedure_division(test_cobol_file, test_metadata):
    """Test extracting PROCEDURE DIVISION"""
    result = extract_procedure_division(test_cobol_file, test_metadata)

    assert "PROCEDURE DIVISION" in result
    assert len(result) > 0

def test_extract_division_not_found(test_cobol_file):
    """Test extraction when division doesn't exist"""
    metadata = {"divisions": []}
    result = extract_data_division(test_cobol_file, metadata)

    assert result is None
```

**2. Run Tests** → Should FAIL

**3. Implement**

```python
def find_division_boundaries(metadata: dict) -> dict:
    """Find line boundaries for each division."""
    boundaries = {}
    divisions = metadata.get("divisions", [])

    for div in divisions:
        name = div["name"]
        start = div.get("line")
        end = div.get("end_line")
        if start and end:
            boundaries[name] = (start, end)

    return boundaries

def extract_data_division(file_path: str, metadata: dict) -> Optional[str]:
    """Extract DATA DIVISION using metadata."""
    boundaries = find_division_boundaries(metadata)

    if "DATA DIVISION" not in boundaries:
        return None

    start, end = boundaries["DATA DIVISION"]
    return extract_lines(file_path, start, end)

def extract_procedure_division(file_path: str, metadata: dict) -> Optional[str]:
    """Extract PROCEDURE DIVISION using metadata."""
    boundaries = find_division_boundaries(metadata)

    if "PROCEDURE DIVISION" not in boundaries:
        return None

    start, end = boundaries["PROCEDURE DIVISION"]
    return extract_lines(file_path, start, end)
```

**4. Run Tests** → Should PASS

**5. Refactor & Commit**

---

### Step 1.5: Paragraph Extractors (Day 3 Morning - 3 hours)

#### TDD Cycle: Paragraph Extraction

**Tests First**:
```python
def test_extract_paragraph_by_name():
    """Test extracting specific paragraph"""
    metadata = {
        "paragraphs": [
            {"name": "MAIN-LOGIC", "line": 100, "end_line": 150},
            {"name": "VALIDATE-INPUT", "line": 200, "end_line": 250}
        ]
    }

    result = extract_paragraph(file, metadata, "MAIN-LOGIC")
    assert "MAIN-LOGIC" in result

def test_extract_multiple_paragraphs():
    """Test extracting multiple paragraphs"""
    result = extract_paragraphs_by_names(
        file, metadata, ["MAIN-LOGIC", "VALIDATE-INPUT"]
    )
    assert "MAIN-LOGIC" in result
    assert "VALIDATE-INPUT" in result
```

Then implement `extract_paragraph()` and `extract_paragraphs_by_names()`

---

### Step 1.6: Optimization Functions (Day 3 Afternoon - 3 hours)

#### TDD Cycle: Compression

**Tests First**:
```python
def test_compress_source_code():
    """Test source code compression"""
    source = """
    PROCEDURE DIVISION.

        DISPLAY 'HELLO'.


        DISPLAY 'WORLD'.

    """

    compressed = compress_source_code(source)

    # Should remove blank lines
    assert compressed.count('\n\n\n') == 0
    # Should preserve code
    assert "DISPLAY 'HELLO'" in compressed

def test_estimate_token_count():
    """Test token estimation"""
    source = "A" * 400  # 400 characters
    tokens = estimate_token_count(source)

    # Rough estimate: chars / 4
    assert 80 <= tokens <= 120

def test_add_section_markers():
    """Test adding section markers"""
    source = "PROCEDURE DIVISION.\n    DISPLAY 'TEST'."
    marked = add_section_markers(source, "PROCEDURE DIVISION")

    assert "BEGIN PROCEDURE DIVISION" in marked
    assert "END PROCEDURE DIVISION" in marked
```

Then implement compression and helper functions

---

### Step 1.7: Integration with Agent (Day 4 - 6 hours)

#### TDD Cycle: Agent Integration

**1. Write Integration Tests First**

Create: `agent/tests/test_integration_source_extraction.py`

```python
def test_extract_source_code_for_section_data_structures():
    """Test source extraction for data-structures section"""
    section = {"id": "data-structures", "title": "Data Structures"}
    state = {...}  # Mock state

    result = extract_source_code_for_section(section, file, metadata, state)

    assert result is not None
    assert "DATA DIVISION" in result
    assert "WORKING-STORAGE" in result

def test_build_section_context_with_source():
    """Test context building includes source code"""
    section = {"id": "data-structures"}
    state = {
        "source_extraction_enabled": True,
        "cobol_files": [test_file],
        "full_metadata": test_metadata,
        ...
    }

    context = build_section_context(state, section)

    assert "source_code" in context
    assert context["source_code"] is not None

def test_source_extraction_disabled():
    """Test that source extraction can be disabled"""
    state = {"source_extraction_enabled": False, ...}
    context = build_section_context(state, section)

    assert context.get("source_code") is None
```

**2. Run Tests** → Should FAIL

**3. Implement Integration**

Modify `cobol_doc_agent.py`:
- Add imports
- Extend AgentState
- Create `extract_source_code_for_section()`
- Modify `build_section_context()`

**4. Run Tests** → Should PASS

**5. End-to-End Test**

```bash
python cobol_doc_agent.py --config ./config-74.yaml
```

Verify:
- Documentation generates
- Source code included in sections
- Token usage measured

---

### Phase 1 Deliverables

**Code:**
- [ ] `agent/source_extractor.py` (~650 lines)
- [ ] `agent/section_requirements.py` (~450 lines)
- [ ] `agent/tests/test_source_extractor.py` (~400 lines)
- [ ] `agent/tests/test_section_requirements.py` (~150 lines)
- [ ] `agent/tests/test_integration_source_extraction.py` (~200 lines)
- [ ] Modified `agent/cobol_doc_agent.py` (+300 lines)
- [ ] Modified `agent/config-74.yaml` (+50 lines)
- [ ] Modified `agent/cobol-doc-template.yaml` (+250 lines)

**Tests:**
- [ ] All unit tests pass (90%+ coverage)
- [ ] Integration test passes
- [ ] End-to-end test generates complete documentation

**Metrics:**
- [ ] Token usage measured
- [ ] Documentation quality assessed
- [ ] Performance benchmarked

**Acceptance Criteria:**
- [ ] Source extraction works for all 10 relevant sections
- [ ] Deduplication reduces redundancy
- [ ] Compression optimizes size
- [ ] Token usage: target 1.0-1.5M (vs baseline 1.8M)
- [ ] All tests GREEN

---

## Phase 2: Ripgrep Integration - TDD

### Timeline: Days 5-6 (2 days)

### Goal
Add pattern-based extraction using Ripgrep direct CLI (no MCP).

### TDD Workflow

Same as Phase 1: **Tests First → Implement → Refactor**

---

### Step 2.1: Ripgrep Tool Infrastructure (Day 5 Morning - 3 hours)

#### TDD Cycle 1: Ripgrep Availability Check

**1. Write Tests First**

Create: `agent/tests/test_ripgrep_tool.py`

```python
import pytest
from ripgrep_tool import RipgrepTool, check_ripgrep_installed

def test_check_ripgrep_installed():
    """Test checking if ripgrep is installed"""
    installed = check_ripgrep_installed()
    assert isinstance(installed, bool)

def test_ripgrep_tool_initialization():
    """Test RipgrepTool initialization"""
    rg = RipgrepTool()
    assert rg is not None

def test_ripgrep_tool_is_available():
    """Test availability check"""
    rg = RipgrepTool()
    available = rg.is_available()
    assert isinstance(available, bool)

@pytest.mark.skipif(not check_ripgrep_installed(), reason="ripgrep not installed")
def test_ripgrep_get_version():
    """Test getting ripgrep version"""
    rg = RipgrepTool()
    version = rg.get_version()
    assert version is not None
    assert len(version) > 0
```

**2. Run Tests** → Should FAIL

**3. Implement**

Create: `agent/ripgrep_tool.py`

```python
import subprocess
import shutil

def check_ripgrep_installed() -> bool:
    """Check if ripgrep is installed."""
    return shutil.which("rg") is not None

class RipgrepTool:
    def __init__(self, binary_path="/usr/bin/rg"):
        self.binary = binary_path
        if not binary_path:
            self.binary = shutil.which("rg")

    def is_available(self) -> bool:
        """Check if ripgrep is available."""
        try:
            result = subprocess.run(
                [self.binary, "--version"],
                capture_output=True,
                timeout=5
            )
            return result.returncode == 0
        except:
            return False

    def get_version(self) -> str:
        """Get ripgrep version."""
        result = subprocess.run(
            [self.binary, "--version"],
            capture_output=True,
            text=True
        )
        return result.stdout.split('\n')[0]
```

**4. Run Tests** → Should PASS

**5. Refactor & Commit**

---

### Step 2.2: Basic Pattern Search (Day 5 Afternoon - 3 hours)

#### TDD Cycle: Search Function

**Tests First**:
```python
@pytest.fixture
def test_cobol_file():
    """Create test COBOL file with patterns"""
    content = """
    IDENTIFICATION DIVISION.
    PROGRAM-ID. TEST-PROG.

    PROCEDURE DIVISION.
        EXEC SQL
            SELECT * FROM CUSTOMERS
        END-EXEC.

        ON ERROR
            DISPLAY 'ERROR OCCURRED'.

        * This is a comment
        CALL 'SUBROUTINE-A' USING PARAM1.
    """
    with open("/tmp/test.cbl", "w") as f:
        f.write(content)
    return "/tmp/test.cbl"

@pytest.mark.skipif(not check_ripgrep_installed(), reason="ripgrep not installed")
def test_search_basic_pattern(test_cobol_file):
    """Test basic pattern search"""
    rg = RipgrepTool()
    results = rg.search("EXEC SQL", test_cobol_file)

    assert len(results) > 0
    assert any("EXEC SQL" in r.match_text for r in results)

@pytest.mark.skipif(not check_ripgrep_installed(), reason="ripgrep not installed")
def test_search_with_context(test_cobol_file):
    """Test search with before/after context"""
    rg = RipgrepTool()
    results = rg.search_with_context("ON ERROR", test_cobol_file, before=1, after=1)

    assert len(results) > 0
    result = results[0]
    assert result.context_before or result.context_after

@pytest.mark.skipif(not check_ripgrep_installed(), reason="ripgrep not installed")
def test_search_multiline(test_cobol_file):
    """Test multiline pattern search"""
    rg = RipgrepTool()
    results = rg.search_multiline(r"EXEC SQL.*?END-EXEC", test_cobol_file)

    assert len(results) > 0
```

Then implement `search()`, `search_with_context()`, `search_multiline()`

---

### Step 2.3: Pattern Extractors (Day 6 Morning - 3 hours)

#### TDD Cycle: High-Level Extractors

**Tests First**:
```python
def test_extract_sql_statements(test_cobol_file):
    """Test SQL statement extraction"""
    rg = RipgrepTool()
    sql_statements = extract_sql_statements(test_cobol_file, rg)

    assert len(sql_statements) > 0
    assert any("SELECT" in stmt for stmt in sql_statements)

def test_extract_comments(test_cobol_file):
    """Test comment extraction"""
    rg = RipgrepTool()
    comments = extract_comments(test_cobol_file, rg)

    assert len(comments) > 0
    assert any("This is a comment" in c for c in comments)

def test_extract_error_handling_blocks(test_cobol_file):
    """Test error handling extraction"""
    rg = RipgrepTool()
    errors = extract_error_handling_blocks(test_cobol_file, rg)

    assert len(errors) > 0
    assert any("ON ERROR" in e for e in errors)

def test_extract_call_statements(test_cobol_file):
    """Test CALL statement extraction"""
    rg = RipgrepTool()
    calls = extract_call_statements(test_cobol_file, rg)

    assert len(calls) > 0
    assert any("SUBROUTINE-A" in c["program"] for c in calls)
```

Then implement pattern-specific extractors

---

### Step 2.4: Agent Integration (Day 6 Afternoon - 2 hours)

#### TDD Cycle: Integration

**Tests First**:
```python
def test_initialize_ripgrep_node():
    """Test ripgrep initialization in agent"""
    state = {"ripgrep_enabled": True}
    new_state = initialize_ripgrep_node(state)

    assert "ripgrep_tool" in new_state
    assert "ripgrep_available" in new_state

def test_extract_with_patterns_enabled():
    """Test extraction with ripgrep patterns"""
    section = {
        "id": "error-handling",
        "requirements": {
            "ripgrep_patterns": ["ON ERROR", "ON EXCEPTION"]
        }
    }
    state = {"ripgrep_available": True, "ripgrep_tool": RipgrepTool()}

    result = extract_source_code_for_section(section, file, metadata, state)

    assert "ON ERROR" in result

def test_extract_with_ripgrep_unavailable():
    """Test graceful fallback when ripgrep unavailable"""
    section = {"id": "error-handling", ...}
    state = {"ripgrep_available": False}

    # Should not crash, should fall back
    result = extract_source_code_for_section(section, file, metadata, state)
    # Result may be None or fallback content
```

Then implement integration into `cobol_doc_agent.py`

---

### Phase 2 Deliverables

**Code:**
- [ ] `agent/ripgrep_tool.py` (~450 lines)
- [ ] `agent/tests/test_ripgrep_tool.py` (~300 lines)
- [ ] Modified `agent/source_extractor.py` (+100 lines - pattern extractors)
- [ ] Modified `agent/cobol_doc_agent.py` (+150 lines)
- [ ] Modified `agent/section_requirements.py` (+50 lines - pattern configs)
- [ ] Modified `agent/config-74.yaml` (+30 lines)

**Tests:**
- [ ] All ripgrep tests pass
- [ ] Integration tests pass
- [ ] Pattern extraction works for SQL, comments, errors

**Acceptance Criteria:**
- [ ] Ripgrep available and working
- [ ] Pattern extraction functional
- [ ] Fallback works when ripgrep unavailable
- [ ] All tests GREEN

---

## Phase 3: Multi-File Support - TDD

### Timeline: Days 7-9 (3 days)

### Goal
Resolve copybooks and called programs across multi-file codebase.

### TDD Workflow

Same: **Tests First → Implement → Refactor**

---

### Step 3.1: Copybook Resolver (Day 7 - 6 hours)

#### TDD Cycle 1: Finding Copybooks

**Tests First**:
```python
@pytest.fixture
def test_codebase():
    """Create test codebase structure"""
    # Create directory structure
    # /tmp/test-codebase/
    #   programs/TEST.cbl
    #   copybooks/CUSTOMER-REC.cpy
    #   copybooks/ERROR-CODES.cpy
    pass

def test_find_copybook_in_same_directory():
    """Test finding copybook in same directory"""
    resolver = CopybookResolver(codebase_root, ripgrep)
    path = resolver.find_copybook("CUSTOMER-REC")

    assert path is not None
    assert "CUSTOMER-REC.cpy" in path

def test_find_copybook_in_standard_location():
    """Test finding copybook in standard location"""
    resolver = CopybookResolver(codebase_root, ripgrep)
    path = resolver.find_copybook("ERROR-CODES")

    assert path is not None

def test_find_copybook_not_found():
    """Test handling of missing copybook"""
    resolver = CopybookResolver(codebase_root, ripgrep)
    path = resolver.find_copybook("NONEXISTENT")

    assert path is None

def test_extract_copybook_content():
    """Test extracting copybook content"""
    resolver = CopybookResolver(codebase_root, ripgrep)
    content = resolver.extract_copybook_content(copybook_path)

    assert content is not None
    assert len(content) > 0
```

Then implement `CopybookResolver` class

---

#### TDD Cycle 2: Resolving All Copybooks

**Tests First**:
```python
def test_resolve_all_copybooks():
    """Test resolving all copybooks in program"""
    metadata = {
        "copy_statements": [
            {"name": "CUSTOMER-REC", "line": 45},
            {"name": "ERROR-CODES", "line": 46}
        ]
    }

    resolver = CopybookResolver(codebase_root, ripgrep)
    resolved = resolver.resolve_all_copybooks(program_file, metadata)

    assert "CUSTOMER-REC" in resolved
    assert "ERROR-CODES" in resolved
    assert len(resolved["CUSTOMER-REC"]) > 0

def test_copybook_dependency_graph():
    """Test building copybook dependency graph"""
    resolver = CopybookResolver(codebase_root, ripgrep)
    graph = resolver.build_copybook_dependency_graph()

    assert isinstance(graph, dict)
```

Then implement resolution functions

---

### Step 3.2: Called Program Resolver (Day 8 - 6 hours)

#### TDD Cycle: Program Resolution

**Tests First**:
```python
def test_find_called_program():
    """Test finding called program"""
    resolver = CalledProgramResolver(codebase_root, ripgrep)
    path = resolver.find_called_program("SUBROUTINE-A")

    assert path is not None
    assert ".cbl" in path

def test_extract_program_header():
    """Test extracting program header"""
    resolver = CalledProgramResolver(codebase_root, ripgrep)
    header = resolver.extract_program_header(program_path)

    assert "program_id" in header
    assert "purpose" in header

def test_resolve_all_calls():
    """Test resolving all CALL statements"""
    metadata = {
        "call_statements": [
            {"name": "SUBROUTINE-A", "line": 100},
            {"name": "SUBROUTINE-B", "line": 200}
        ]
    }

    resolver = CalledProgramResolver(codebase_root, ripgrep)
    resolved = resolver.resolve_all_calls(program_file, metadata)

    assert "SUBROUTINE-A" in resolved
    assert resolved["SUBROUTINE-A"]["path"] is not None

def test_build_call_hierarchy():
    """Test building call hierarchy"""
    resolver = CalledProgramResolver(codebase_root, ripgrep)
    hierarchy = resolver.build_call_hierarchy("MAIN-PROGRAM", depth=2)

    assert hierarchy["program"] == "MAIN-PROGRAM"
    assert "calls" in hierarchy
```

Then implement `CalledProgramResolver`

---

### Step 3.3: Agent Integration (Day 9 - 6 hours)

#### TDD Cycle: Multi-File Integration

**Tests First**:
```python
def test_initialize_multi_file_resolvers():
    """Test initialization of multi-file resolvers"""
    state = {
        "multi_file_enabled": True,
        "codebase_root": "/tmp/test-codebase",
        "ripgrep_tool": RipgrepTool()
    }

    new_state = initialize_multi_file_resolvers_node(state)

    assert "copybook_resolver" in new_state
    assert "called_program_resolver" in new_state

def test_extract_with_copybooks():
    """Test extraction includes copybook content"""
    section = {
        "id": "data-structures",
        "requirements": {
            "include_copybooks": True
        }
    }
    state = {
        "copybook_resolver": CopybookResolver(...),
        ...
    }

    result = extract_source_code_for_section(section, file, metadata, state)

    assert "COPY CUSTOMER-REC" in result
    assert "01 CUSTOMER-REC" in result  # Copybook content

def test_extract_with_called_programs():
    """Test extraction includes called program info"""
    section = {
        "id": "inter-program-communication",
        "requirements": {
            "resolve_called_programs": True
        }
    }

    result = extract_source_code_for_section(section, file, metadata, state)

    assert "SUBROUTINE-A" in result
    assert "Location:" in result
```

Then implement integration

---

### Phase 3 Deliverables

**Code:**
- [ ] `agent/multi_file_resolver.py` (~550 lines)
- [ ] `agent/tests/test_multi_file_resolver.py` (~350 lines)
- [ ] Modified `agent/cobol_doc_agent.py` (+200 lines)
- [ ] Modified `agent/section_requirements.py` (+50 lines)
- [ ] Modified `agent/config-74.yaml` (+50 lines)

**Tests:**
- [ ] All multi-file tests pass
- [ ] Copybook resolution works
- [ ] Called program resolution works
- [ ] Integration tests pass

**Acceptance Criteria:**
- [ ] Copybooks found and extracted
- [ ] Called programs found and documented
- [ ] Dependency graphs correct
- [ ] All tests GREEN

---

## Phase 4: Integration & Polish

### Timeline: Day 10 (1 day)

### Goals
- End-to-end testing
- Optimization
- Documentation
- Release preparation

---

### Step 4.1: End-to-End Testing (Morning - 3 hours)

**Test Scenarios**:
1. Single-file COBOL (TDAS-MINDISTCALC.c74)
2. Multi-file COBOL with copybooks
3. Multi-file with called programs
4. Large files (stress test)

**Metrics to Collect**:
- Token usage per section
- Total token usage
- Generation time
- Memory usage
- Cache hit rates

**Success Criteria**:
- All sections generate
- Documentation quality ≥ baseline
- Token usage within acceptable range

---

### Step 4.2: Optimization (Afternoon - 2 hours)

**Performance Tuning**:
- Review token usage data
- Adjust deduplication thresholds
- Tune compression settings
- Optimize caching

**Quality Tuning**:
- Review generated documentation
- Adjust section requirements if needed
- Fine-tune prompts

---

### Step 4.3: Documentation (Evening - 2 hours)

**Documents to Create/Update**:
- [ ] `docs/SOURCE-EXTRACTION.md`
- [ ] `docs/RIPGREP-INTEGRATION.md`
- [ ] `docs/MULTI-FILE-SUPPORT.md`
- [ ] `docs/TOKEN-OPTIMIZATION.md`
- [ ] `README.md` (update)
- [ ] `CHANGELOG.md` (create/update)

---

### Step 4.4: Release Checklist

- [ ] All unit tests pass (90%+ coverage)
- [ ] All integration tests pass
- [ ] End-to-end test generates complete docs
- [ ] Token usage measured and acceptable
- [ ] Documentation complete
- [ ] CHANGELOG updated
- [ ] Code reviewed
- [ ] Commit and push to repository

---

## Success Metrics

### Must Have (Go/No-Go)
- [ ] All 11 sections generate successfully
- [ ] No crashes or exceptions
- [ ] Documentation quality ≥ baseline
- [ ] Total token usage ≤ 3M
- [ ] Generation time ≤ 10 minutes
- [ ] All tests pass

### Should Have
- [ ] Token usage 1.5-2.5M (vs baseline 1.8M)
- [ ] Copybooks resolved
- [ ] Called programs identified
- [ ] Generation time ≤ 7 minutes

### Nice to Have
- [ ] Token usage ≤ 1.5M
- [ ] Generation time ≤ 5 minutes
- [ ] Complete dependency graphs

---

## Risk Management

### Risk 1: Token Usage Explosion
**Mitigation**: Aggressive deduplication, monitoring, emergency limits

### Risk 2: Test Coverage Gaps
**Mitigation**: TDD enforces tests first, aim for 90%+ coverage

### Risk 3: Multi-File Complexity
**Mitigation**: Phased approach, thorough testing, timeouts

### Risk 4: Ripgrep Not Available
**Mitigation**: Graceful fallback, installation instructions

---

## Development Environment Setup

### Prerequisites
```bash
# Install ripgrep
sudo apt install ripgrep  # Debian/Ubuntu
brew install ripgrep      # macOS

# Verify installation
rg --version

# Install Python dependencies
pip install pytest pytest-cov

# Setup test fixtures
mkdir -p /tmp/test-cobol-codebase/{programs,copybooks}
```

### Running Tests
```bash
# Run all tests
pytest agent/tests/ -v

# Run with coverage
pytest agent/tests/ --cov=agent --cov-report=html

# Run specific phase tests
pytest agent/tests/test_source_extractor.py -v
pytest agent/tests/test_ripgrep_tool.py -v
pytest agent/tests/test_multi_file_resolver.py -v
```

---

## Commit Message Convention

Follow conventional commits:

```
feat: add basic line extraction function
test: add tests for division extraction
fix: handle missing division boundaries
refactor: optimize deduplication algorithm
docs: update source extraction guide
```

---

## Summary

This implementation plan follows strict TDD principles:

1. **Write tests first** (RED)
2. **Implement minimum code** (GREEN)
3. **Refactor** (CLEAN)
4. **Repeat**

Each phase is self-contained and independently testable. No code is written without a failing test first.

**Timeline**: 10 days
**Approach**: Phased, incremental, test-driven
**Phases**: 4 (Option A → Ripgrep → Multi-file → Polish)

---

**Ready to begin implementation when approved.**
