# Source Extraction Implementation Plan
## Complete 3-Phase Implementation for COBOL Documentation Agent

**Document Version:** 1.1
**Created:** 2025-10-27
**Last Updated:** 2025-10-27
**Status:** Phase 1 ✅ COMPLETE | Phase 2 ✅ COMPLETE | Phase 3 ✅ COMPLETE

---

## Overview

This document outlines the complete implementation plan for integrating source code extraction into the COBOL Documentation Agent. The goal is to enhance documentation quality by providing the LLM with actual COBOL source code in addition to metadata.

### Implementation Strategy: Option A (Selected)
**Selective Source Extraction** - Extract only relevant source code sections based on documentation section requirements, with intelligent search and multi-file support.

---

## Phase 1: Basic Source Extraction (Days 1-4) ✅ COMPLETE

### Goal
Create foundation for extracting COBOL source code and integrating it into the documentation generation workflow.

### What Was Implemented

#### 1. Core Extraction Module (`source_extractor.py`)
**Purpose:** Low-level COBOL source parsing and extraction

**Key Functions:**
- `extract_division(source_text, division_name)` - Extract specific division (IDENTIFICATION, DATA, PROCEDURE, etc.)
- `compress_source(source_text)` - Remove comments and blank lines to reduce tokens
- `format_for_documentation(source_text)` - Wrap in markdown code blocks

**Features:**
- Handles COBOL division boundaries correctly
- Preserves code structure and indentation
- Optional compression to save tokens
- Markdown formatting for LLM consumption

**Tests:** 29 passing tests covering all extraction scenarios

---

#### 2. Integration Layer (`source_integration.py`)
**Purpose:** High-level interface between agent and extraction logic

**Key Functions:**
- `extract_source_for_section(section_id, cobol_file_path, paragraph_metadata, compress)` - Main entry point for section-specific extraction
- Returns formatted source code ready for LLM prompts

**Section Mapping:**
- `2_data_structures` → DATA DIVISION
- `3_business_logic` → PROCEDURE DIVISION
- `4_file_operations` → ENVIRONMENT + DATA DIVISION (file-related)
- `5_error_handling` → PROCEDURE DIVISION (error-handling paragraphs)

**Tests:** 11 passing tests for integration scenarios

---

#### 3. Section Requirements (`section_requirements.py`)
**Purpose:** Configuration for which sections need source extraction

**Key Functions:**
- `should_extract_source(section_id)` - Determine if section needs source
- `get_divisions_for_section(section_id)` - Map section to COBOL divisions

**Configuration:**
```python
SECTION_SOURCE_REQUIREMENTS = {
    "2_data_structures": ["DATA"],
    "3_business_logic": ["PROCEDURE"],
    "4_file_operations": ["ENVIRONMENT", "DATA"],
    "5_error_handling": ["PROCEDURE"],
    # ... more sections
}
```

**Tests:** 10 passing tests

---

#### 4. Agent Integration (`cobol_doc_agent.py`)
**Purpose:** Integrate source extraction into main documentation workflow

**Changes Made:**

**A. Updated AgentState TypedDict:**
```python
enable_source_extraction: bool      # Toggle extraction on/off
compress_source: bool               # Toggle compression
cobol_file_path: Optional[str]      # Path to COBOL source file
```

**B. Modified `build_section_context()` (lines 1023-1051):**
```python
# Phase 1: Source Code Extraction Integration
if state.get("enable_source_extraction", False) and SOURCE_EXTRACTION_AVAILABLE:
    section_id = section.get("id", "")
    cobol_file_path = state.get("cobol_file_path")

    if cobol_file_path and should_extract_source(section_id):
        compress = state.get("compress_source", True)
        source_code = extract_source_for_section(
            section_id, cobol_file_path, compress=compress
        )

        if source_code:
            filtered_context["source_code"] = source_code
```

**C. Updated `generate_documentation()` signature:**
- Added parameters: `enable_source_extraction`, `compress_source`, `cobol_file_path`
- Auto-detection logic for COBOL file path

**D. Graceful Degradation:**
- Continues without source if extraction fails
- Imports wrapped in try-except for optional dependency

---

#### 5. Configuration Support (`config_loader.py` & `config-74.yaml`)

**Added to config_loader.py:**
```python
def get_source_extraction_config(self) -> Dict[str, Any]:
    """Get source code extraction configuration (Phase 1)"""
    return config.get('source_extraction', {})
```

**Added to config-74.yaml:**
```yaml
# Source Code Extraction (Phase 1)
source_extraction:
  enabled: true   # Enable source code extraction
  compress: true  # Remove comments and blank lines to reduce tokens
```

---

#### 6. Integration Tests
**File:** `test_integration_simple.py`

**Tests (All Passing 5/5):**
1. ✅ AgentState TypedDict has required fields
2. ✅ Source extraction modules can be imported
3. ✅ Config loader reads source extraction settings
4. ✅ build_section_context integrates extraction
5. ✅ End-to-end source extraction works

---

### Phase 1 Results

✅ **50 tests passing** (29 extractor + 11 integration + 10 requirements)
✅ **Fully integrated** into cobol_doc_agent.py
✅ **Config-driven** with feature flags
✅ **Graceful degradation** on failures
✅ **Auto-detection** of COBOL files

**Status:** PRODUCTION READY

---

## Phase 2: RipGrep Integration (Days 5-7) 🔄 PENDING

### Goal
Implement intelligent code search using ripgrep to find relevant snippets across large COBOL files, reducing token usage and improving relevance.

### Problem Phase 2 Solves

**Current Issue:** Phase 1 extracts entire divisions (e.g., entire PROCEDURE DIVISION might be 10,000+ lines)

**Solution:** Use ripgrep to search for specific patterns and extract only relevant code blocks with context

### What Will Be Implemented

#### 1. RipGrep Search Module (`source_search.py`)
**Purpose:** Intelligent pattern-based search in COBOL files

**Key Functions:**

```python
def search_paragraphs(cobol_file_path: str, paragraph_names: List[str]) -> Dict[str, str]:
    """
    Search for specific paragraph definitions and their implementations

    Args:
        cobol_file_path: Path to COBOL file
        paragraph_names: List of paragraph names to find

    Returns:
        Dict mapping paragraph_name -> code snippet with context
    """

def search_variable_usage(cobol_file_path: str, variable_name: str) -> List[str]:
    """
    Find all lines where a variable is used (MOVE, COMPUTE, IF, etc.)

    Returns:
        List of code snippets showing variable usage
    """

def search_file_operations(cobol_file_path: str) -> str:
    """
    Find all file-related code (FD, OPEN, CLOSE, READ, WRITE)

    Returns:
        Combined snippet of all file operations
    """

def search_with_context(cobol_file_path: str, pattern: str,
                       context_lines: int = 5) -> List[str]:
    """
    Low-level ripgrep search with surrounding context

    Args:
        pattern: Regex pattern to search
        context_lines: Number of lines before/after match

    Returns:
        List of matched snippets with context
    """
```

**Features:**
- Use Python `subprocess` to call `rg` command
- Support regex patterns for flexible matching
- Extract surrounding context (±N lines)
- Handle COBOL-specific patterns (paragraph names, division headers, etc.)
- Combine multiple search results intelligently

---

#### 2. Search Pattern Definitions (`search_patterns.py`)
**Purpose:** Pre-defined search patterns for different section types

**Pattern Categories:**

```python
# Paragraph definition patterns
PARAGRAPH_DEFINITION = r'^\s{7}[A-Z0-9-]+\.\s*$'

# Data structure patterns
DATA_ITEM_DEFINITION = r'^\s+\d{2}\s+[A-Z0-9-]+\s+'
FILE_DEFINITION = r'^\s+FD\s+[A-Z0-9-]+'

# File operation patterns
FILE_OPERATIONS = [
    r'\bOPEN\s+(INPUT|OUTPUT|I-O|EXTEND)\b',
    r'\bCLOSE\b',
    r'\bREAD\b',
    r'\bWRITE\b',
]

# Control flow patterns
PERFORM_STATEMENTS = r'\bPERFORM\s+[A-Z0-9-]+'
CALL_STATEMENTS = r'\bCALL\s+["\'][\w-]+["\']'

# Error handling patterns
ERROR_HANDLING = [
    r'\bON\s+SIZE\s+ERROR\b',
    r'\bINVALID\s+KEY\b',
    r'\bAT\s+END\b',
    r'\bFILE\s+STATUS\b',
]

# Section-specific search strategies
SECTION_SEARCH_PATTERNS = {
    "2_data_structures": {
        "patterns": [DATA_ITEM_DEFINITION, FILE_DEFINITION],
        "divisions": ["DATA"],
        "context_lines": 3,
    },
    "3_business_logic": {
        "patterns": [PARAGRAPH_DEFINITION, PERFORM_STATEMENTS],
        "divisions": ["PROCEDURE"],
        "context_lines": 10,  # More context for logic
    },
    "4_file_operations": {
        "patterns": FILE_OPERATIONS + [FILE_DEFINITION],
        "divisions": ["ENVIRONMENT", "DATA", "PROCEDURE"],
        "context_lines": 5,
    },
    # ... more sections
}
```

---

#### 3. Enhanced Source Integration (`source_integration.py` updates)
**Purpose:** Use ripgrep search instead of full division extraction

**New Strategy:**

```python
def extract_source_for_section_smart(section_id: str,
                                     cobol_file_path: str,
                                     paragraph_metadata: Optional[Dict] = None,
                                     compress: bool = True,
                                     max_tokens: int = 4000) -> Optional[str]:
    """
    Smart extraction using ripgrep search

    Strategy:
    1. Get search patterns for this section
    2. Use ripgrep to find relevant code blocks
    3. Combine and deduplicate results
    4. If under token limit, return
    5. If over limit, prioritize and truncate
    """

    # Get patterns for this section
    patterns = get_search_patterns_for_section(section_id)

    # Search using ripgrep
    results = []
    for pattern in patterns:
        snippets = search_with_context(cobol_file_path, pattern,
                                      context_lines=patterns.context_lines)
        results.extend(snippets)

    # Deduplicate overlapping snippets
    combined = merge_overlapping_snippets(results)

    # Check token count
    if count_tokens(combined) <= max_tokens:
        return format_for_documentation(combined, compress)
    else:
        # Truncate intelligently
        return truncate_to_budget(combined, max_tokens, compress)
```

**Benefits:**
- Extract only relevant code (not entire divisions)
- Reduce token usage by 60-80%
- More targeted context for LLM
- Faster extraction (ripgrep is very fast)

---

#### 4. Testing (`test_source_search.py`)

**Test Coverage:**
- Test paragraph search finds correct definitions
- Test variable usage search finds all references
- Test file operation search finds OPEN/CLOSE/READ/WRITE
- Test context lines are included correctly
- Test pattern matching with real COBOL code
- Test deduplication of overlapping results
- Test token budget enforcement

**Target:** 15-20 passing tests

---

### Phase 2 Integration Points

**In `build_section_context()`:**
```python
# Phase 2: Smart source extraction with ripgrep
if state.get("enable_source_extraction", False):
    section_id = section.get("id", "")
    cobol_file_path = state.get("cobol_file_path")

    if cobol_file_path and should_extract_source(section_id):
        # Use smart extraction with ripgrep
        source_code = extract_source_for_section_smart(
            section_id,
            cobol_file_path,
            paragraph_metadata=metadata.get("paragraphs"),
            compress=state.get("compress_source", True),
            max_tokens=4000  # Budget per section
        )
```

**In `section_requirements.py`:**
- Add `get_search_patterns_for_section(section_id)`
- Add token budget limits per section
- Add relevance scoring for search results

---

### Phase 2 Deliverables

**New Files:**
- `source_search.py` (200-300 lines)
- `search_patterns.py` (150-200 lines)
- `test_source_search.py` (15-20 tests)

**Modified Files:**
- `source_integration.py` - Add `extract_source_for_section_smart()`
- `section_requirements.py` - Add search pattern definitions

**Expected Outcome:**
- 70-80% reduction in extracted source size
- More relevant code snippets
- Faster extraction times
- All tests passing (15-20 new tests)

---

## Phase 3: Multi-File Support (Days 8-10) 🔄 PENDING

### Goal
Handle COBOL projects with COPY statements and multiple source files (copybooks), enabling documentation of real-world modular COBOL programs.

### Problem Phase 3 Solves

**Current Issue:**
- Single file extraction only
- COPY statements ignored (e.g., `COPY CUSTMAST.`)
- Missing definitions from copybooks
- Incomplete documentation for modular programs

**Solution:**
- Parse COPY statements
- Locate and extract from copybooks
- Merge multi-file context intelligently

---

### What Will Be Implemented

#### 1. COPY Statement Parser (`copy_resolver.py`)
**Purpose:** Parse COPY statements and resolve copybook file paths

**Key Functions:**

```python
def find_copy_statements(cobol_file_path: str) -> List[CopyStatement]:
    """
    Parse COBOL file and find all COPY statements

    Returns:
        List of CopyStatement objects with:
        - copybook_name: Name from COPY statement
        - replacing_clause: REPLACING clause if present
        - line_number: Where COPY appears
    """

def resolve_copybook_path(copybook_name: str,
                         search_paths: List[str]) -> Optional[str]:
    """
    Find copybook file in search paths

    Search order:
    1. Same directory as main file
    2. ./copybooks/
    3. ./COPY/
    4. ../copybooks/
    5. Configured COPY paths from environment

    Returns:
        Full path to copybook file, or None if not found
    """

def build_dependency_graph(main_file: str,
                          search_paths: List[str]) -> Dict[str, List[str]]:
    """
    Build dependency graph of COPY relationships

    Returns:
        Dict mapping file_path -> list of copybook paths it COPYs
    """

class CopyStatement:
    """Represents a COBOL COPY statement"""
    copybook_name: str
    replacing_clause: Optional[str]
    line_number: int
    resolved_path: Optional[str]
```

**Features:**
- Parse COPY with and without REPLACING
- Handle various COPY formats:
  - `COPY CUSTMAST.`
  - `COPY CUSTMAST OF COPYLIB.`
  - `COPY "copybooks/customer.cpy".`
- Resolve relative and absolute paths
- Handle missing copybooks gracefully

---

#### 2. Multi-File Extractor (`multi_file_extractor.py`)
**Purpose:** Extract and combine source from multiple files

**Key Functions:**

```python
def extract_from_multiple_files(main_file: str,
                               section_id: str,
                               copybook_paths: List[str],
                               compress: bool = True,
                               max_tokens: int = 6000) -> str:
    """
    Extract source from main file and copybooks

    Strategy:
    1. Extract from main file (priority)
    2. Extract from each copybook
    3. Label each snippet by file
    4. Merge within token budget

    Returns:
        Combined source with file labels
    """

def prioritize_files(main_file: str,
                    copybooks: List[str],
                    section_id: str) -> List[Tuple[str, float]]:
    """
    Prioritize which files to extract from based on relevance

    Scoring:
    - Main file: 1.0 (always highest)
    - Copybooks with DATA items: 0.8 (for data sections)
    - Copybooks with PROCEDURE code: 0.6 (rare but possible)
    - Generic copybooks: 0.4

    Returns:
        List of (file_path, priority_score) sorted by priority
    """

def merge_multi_file_context(extracts: List[FileExtract],
                             max_tokens: int) -> str:
    """
    Merge extracts from multiple files within token budget

    Strategy:
    1. Always include main file extracts (highest priority)
    2. Add copybook extracts in priority order
    3. Stop when token budget reached
    4. Add summary of excluded files

    Returns:
        Formatted markdown with file labels:

        ## Source Code

        ### From MAINPROG.cbl:
        ```cobol
        ...
        ```

        ### From CUSTMAST.cpy:
        ```cobol
        ...
        ```
    """

class FileExtract:
    """Represents source extracted from one file"""
    file_path: str
    file_name: str
    source_code: str
    token_count: int
    priority: float
```

**Features:**
- Label source by file for clarity
- Prioritize main program over copybooks
- Token budget management across files
- Summary of included/excluded files

---

#### 3. Enhanced Integration Layer (`source_integration.py` updates)
**Purpose:** Coordinate multi-file extraction

**New Main Function:**

```python
def extract_source_for_section_multi_file(
    section_id: str,
    cobol_file_path: str,
    paragraph_metadata: Optional[Dict] = None,
    compress: bool = True,
    max_tokens: int = 6000,
    copybook_search_paths: Optional[List[str]] = None
) -> Optional[str]:
    """
    Full multi-file extraction with ripgrep and COPY resolution

    Workflow:
    1. Find COPY statements in main file
    2. Resolve copybook paths
    3. Build file priority list
    4. Extract from each file using ripgrep (Phase 2)
    5. Merge within token budget
    6. Return formatted multi-file source
    """

    # Find copybooks
    copy_statements = find_copy_statements(cobol_file_path)
    copybooks = [resolve_copybook_path(stmt.copybook_name, search_paths)
                 for stmt in copy_statements]
    copybooks = [cb for cb in copybooks if cb]  # Filter None

    # Prioritize files
    files_to_process = prioritize_files(cobol_file_path, copybooks, section_id)

    # Extract from each file
    extracts = []
    for file_path, priority in files_to_process:
        # Use Phase 2 ripgrep search
        source = extract_source_for_section_smart(
            section_id, file_path, paragraph_metadata, compress, max_tokens=2000
        )
        if source:
            extracts.append(FileExtract(file_path, source, priority))

    # Merge within budget
    return merge_multi_file_context(extracts, max_tokens)
```

---

#### 4. Configuration Updates

**Add to `config-74.yaml`:**
```yaml
# Source Code Extraction (Phase 1-3)
source_extraction:
  enabled: true
  compress: true

  # Phase 2: RipGrep search
  use_smart_search: true  # Use ripgrep instead of full division extraction
  max_tokens_per_section: 6000

  # Phase 3: Multi-file support
  resolve_copybooks: true  # Follow COPY statements
  copybook_search_paths:
    - ./copybooks
    - ./COPY
    - ../copybooks
  max_copybook_depth: 3  # Prevent infinite recursion
```

**Add to `config_loader.py`:**
```python
def get_source_extraction_config(self) -> Dict[str, Any]:
    config = self._ensure_loaded()
    extraction_config = config.get('source_extraction', {})

    # Defaults for Phase 2 & 3
    extraction_config.setdefault('use_smart_search', True)
    extraction_config.setdefault('max_tokens_per_section', 6000)
    extraction_config.setdefault('resolve_copybooks', True)
    extraction_config.setdefault('copybook_search_paths',
                                 ['./copybooks', './COPY', '../copybooks'])
    extraction_config.setdefault('max_copybook_depth', 3)

    return extraction_config
```

---

#### 5. Agent Integration Updates (`cobol_doc_agent.py`)

**Update `build_section_context()`:**
```python
# Phase 3: Multi-file extraction with COPY support
if state.get("enable_source_extraction", False):
    extraction_config = state.get("source_extraction_config", {})

    if extraction_config.get("resolve_copybooks", True):
        # Multi-file extraction
        source_code = extract_source_for_section_multi_file(
            section_id,
            cobol_file_path,
            paragraph_metadata=metadata.get("paragraphs"),
            compress=state.get("compress_source", True),
            max_tokens=extraction_config.get("max_tokens_per_section", 6000),
            copybook_search_paths=extraction_config.get("copybook_search_paths")
        )
    else:
        # Single-file extraction (Phase 2 only)
        source_code = extract_source_for_section_smart(...)
```

---

#### 6. Testing (`test_multi_file.py`)

**Test Scenarios:**

1. **COPY Statement Parsing:**
   - Parse simple COPY statements
   - Parse COPY with REPLACING
   - Parse COPY OF library
   - Handle malformed COPY statements

2. **Copybook Resolution:**
   - Find copybook in same directory
   - Find copybook in ./copybooks/
   - Find copybook with different extensions (.cpy, .CPY, .cbl)
   - Handle missing copybooks gracefully

3. **Multi-File Extraction:**
   - Extract from main file + 1 copybook
   - Extract from main file + 3 copybooks
   - Respect token budget (drop low-priority files)
   - Label files correctly in output

4. **File Prioritization:**
   - Main file always highest priority
   - Data copybooks prioritized for data sections
   - Token budget enforced across files

5. **Dependency Graph:**
   - Build simple dependency graph (A copies B)
   - Handle nested copies (A copies B, B copies C)
   - Detect circular dependencies (A copies B, B copies A)
   - Respect max depth limit

**Target:** 20-25 passing tests

---

### Phase 3 Deliverables

**New Files:**
- `copy_resolver.py` (250-300 lines)
- `multi_file_extractor.py` (300-350 lines)
- `test_multi_file.py` (20-25 tests)

**Modified Files:**
- `source_integration.py` - Add multi-file extraction function
- `cobol_doc_agent.py` - Update build_section_context for multi-file
- `config_loader.py` - Add copybook configuration support
- `config-74.yaml` - Add copybook settings

**Expected Outcome:**
- Support for modular COBOL programs
- Complete documentation even with COPY statements
- Intelligent prioritization of copybooks
- All tests passing (70+ total tests)

---

## Implementation Timeline

| Phase | Days | Focus | Status |
|-------|------|-------|--------|
| **Phase 1** | 1-4 | Basic source extraction & integration | ✅ COMPLETE |
| **Phase 2** | 5-7 | RipGrep search for targeted extraction | 🔄 PENDING |
| **Phase 3** | 8-10 | Multi-file support with COPY resolution | 🔄 PENDING |

**Total Estimated Time:** 10 days

---

## Testing Strategy

### Unit Tests
- Each module has dedicated test file
- Test individual functions in isolation
- Mock file I/O where appropriate

### Integration Tests
- Test Phase 2 + Phase 3 together
- Test with real COBOL files
- Verify token budgets respected
- Verify multi-file extraction works end-to-end

### End-to-End Tests
- Run full agent with source extraction enabled
- Generate documentation for multi-file COBOL program
- Verify source code appears in correct sections
- Verify copybook content is included

**Target:** 70-80 total tests passing across all phases

---

## Success Criteria

### Phase 1 ✅ (ACHIEVED)
- [x] Extract COBOL divisions correctly
- [x] Compress source code (remove comments/blanks)
- [x] Integrate into agent workflow
- [x] Config-driven feature flags
- [x] 50 tests passing

### Phase 2 (TO VERIFY)
- [ ] RipGrep searches find relevant code
- [ ] Token usage reduced by 60-80%
- [ ] Search patterns cover all section types
- [ ] Extraction faster than Phase 1
- [ ] 65-70 tests passing

### Phase 3 (TO VERIFY)
- [ ] COPY statements parsed correctly
- [ ] Copybooks resolved in search paths
- [ ] Multi-file extraction within token budget
- [ ] File labels clear in documentation
- [ ] 80-90 tests passing

---

## Configuration Reference

### Final Configuration (All Phases)

```yaml
# Source Code Extraction (Phase 1-3)
source_extraction:
  # Phase 1: Basic extraction
  enabled: true
  compress: true

  # Phase 2: RipGrep search
  use_smart_search: true
  max_tokens_per_section: 6000
  search_context_lines: 5  # Lines before/after match

  # Phase 3: Multi-file support
  resolve_copybooks: true
  copybook_search_paths:
    - ./copybooks
    - ./COPY
    - ../copybooks
    - /opt/cobol/copybooks  # System copybooks
  max_copybook_depth: 3
  prioritize_main_file: true
```

---

## Files Summary

### Created Files (Phase 1) ✅
- `source_extractor.py` (386 lines, 29 tests)
- `source_integration.py` (197 lines, 11 tests)
- `section_requirements.py` (118 lines, 10 tests)
- `test_integration_simple.py` (5 integration tests)

### To Be Created (Phase 2) 🔄
- `source_search.py` (200-300 lines)
- `search_patterns.py` (150-200 lines)
- `test_source_search.py` (15-20 tests)

### To Be Created (Phase 3) 🔄
- `copy_resolver.py` (250-300 lines)
- `multi_file_extractor.py` (300-350 lines)
- `test_multi_file.py` (20-25 tests)

### Modified Files (All Phases)
- `cobol_doc_agent.py` - Main agent integration
- `config_loader.py` - Configuration support
- `config-74.yaml` - Settings
- `source_integration.py` - Enhanced extraction strategies

---

## Dependencies

### Python Standard Library
- `re` - Regular expressions
- `pathlib` - Path handling
- `subprocess` - For calling ripgrep

### External Tools
- **ripgrep** (`rg`) - Required for Phase 2
  - Install: `apt install ripgrep` (Ubuntu/Debian)
  - Install: `brew install ripgrep` (macOS)

### Python Packages (Already Installed)
- `pytest` - Testing framework
- `pyyaml` - Configuration files

---

## Risk Mitigation

### Risk: RipGrep not installed
**Mitigation:** Fallback to Phase 1 full extraction if `rg` not found

### Risk: Copybooks not found
**Mitigation:** Continue with main file only, log warning about missing copybooks

### Risk: Token budget exceeded
**Mitigation:** Progressive truncation strategy, always include something (never empty context)

### Risk: Circular COPY dependencies
**Mitigation:** Track visited files, enforce max depth limit

---

## Future Enhancements (Post Phase 3)

### Phase 4 (Optional): Advanced Features
- **Semantic chunking** - Split large procedures into logical chunks
- **Call graph integration** - Extract call chains for complex logic
- **AI-powered relevance** - Use LLM to score snippet relevance
- **Caching** - Cache extracted source to speed up regeneration
- **Incremental extraction** - Only re-extract changed files

### Phase 5 (Optional): Performance Optimization
- **Parallel extraction** - Extract from multiple files concurrently
- **Lazy loading** - Extract on-demand per section
- **Smart caching** - Cache ripgrep results
- **Token estimation** - Pre-calculate tokens before extraction

---

## Conclusion

This 3-phase implementation provides:
1. ✅ **Phase 1** - Foundation for source extraction
2. 🔄 **Phase 2** - Intelligent search to reduce token usage
3. 🔄 **Phase 3** - Real-world multi-file COBOL support

**End Result:** Documentation agent that can generate accurate, detailed documentation by analyzing actual COBOL source code, not just metadata, while staying within token budgets and handling complex multi-file projects.

---

**Document End**
