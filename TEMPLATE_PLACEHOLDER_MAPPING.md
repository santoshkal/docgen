# Template Placeholder to Metadata Mapping

**Purpose**: Map every `{{placeholder}}` in template to its metadata source
**Status**: Phase 2, Task 2.1 - Audit Complete

---

## Critical Missing Placeholders (Causing "Information not available")

### 1. `{{source_file_path}}` ❌ MISSING IN CONTEXT
**Template Location**: `document-header` → `metadata-info`
**Expected Source**: `gnucobol_analysis.file_path` OR `ctags_outline.outline.file`
**Current Status**: ❌ NOT passed in filtered context
**Fix Required**: Add to `filter_metadata_for_pass()` essential fields

**Available in metadata**: ✅ Yes
- GnuCOBOL: `gnucobol_analysis['file_path'] = "/workspace/TDAS-MINDISTCALC.c74"`
- CTags: `ctags_outline['outline']['file'] = "/workspace/TDAS-MINDISTCALC.c74"`

---

### 2. `{{program_name}}` ✅ AVAILABLE
**Template Location**: Multiple sections
**Expected Source**: `context.program_name` (from state)
**Current Status**: ✅ Passed through in all contexts
**Fix Required**: None

---

### 3. Called-by Relationships ❌ MISSING
**Placeholders Affected**:
- Paragraph sections show "Called by: Information not available in metadata"

**Expected Source**: Reverse call graph (not in current metadata)
**Current Status**: ❌ Does not exist
**Fix Required**: Phase 3 - Build reverse call graph from CFG edges

---

## All Template Placeholders (91 total)

### Document Metadata (Header)
- `{{generation_timestamp}}` - ✅ Available (runtime)
- `{{program_name}}` - ✅ Available (state)
- `{{source_file_path}}` - ❌ **MISSING** (needs gnucobol.file_path)

### Executive Summary
- `{{summary_paragraph}}` - ✅ LLM Generated
- `{{responsibilities_list}}` - ✅ LLM Generated
- `{{dependencies_list}}` - ✅ LLM Generated

### Program Structure
- `{{division}}` - ✅ Available (ctags.outline.other[kind=division])
- `{{section_name}}` - ✅ Available (ctags.outline.other[kind=section])
- `{{line_number}}` - ✅ Available (ctags.outline.other[].line)
- `{{inferred_purpose}}` - ✅ LLM Generated

### Copybooks
- `{{copybook_name}}` - ✅ Available (superbol_cfg.copybooks[].name)
- `{{copybook_line}}` - ✅ Available (superbol_cfg.copybooks[].line)
- `{{copybook_context}}` - ✅ Available (superbol_cfg.copybooks[].context)
- `{{copybook_purpose}}` - ✅ LLM Generated

### Program Calls
- `{{called_program_name}}` - ✅ Available (superbol_cfg.calls[].to)
- `{{calling_paragraphs}}` - ✅ Available (superbol_cfg.calls[].from)
- `{{call_count}}` - ✅ Available (gnucobol.call_summary.call_counts)
- `{{call_relationships_with_frequency}}` - ✅ LLM Generated from metadata

### Control Flow
- `{{cfg_node_count}}` - ✅ Available (superbol_cfg.nodes.length)
- `{{cfg_edge_count}}` - ✅ Available (superbol_cfg.edges.length)
- `{{complexity_level}}` - ✅ Derived from CFG metrics

### Data Structures
- `{{data_item_name}}` - ✅ Available (superbol_symbols.symbols[kind=13].name)
- `{{data_programs}}` - ✅ LLM Generated
- `{{business_programs}}` - ✅ LLM Generated

### CTags Metrics
- `{{ctags_symbol_count}}` - ✅ Available (ctags.symbol_count)
- `{{ctags_paragraph_count}}` - ✅ Available (ctags.outline.other[kind=paragraph].length)
- `{{ctags_division_count}}` - ✅ Available (ctags.outline.other[kind=division].length)
- `{{ctags_data_count}}` - ✅ Available (ctags.outline.other[kind=data].length)

### GnuCOBOL Metrics
- `{{gnucobol_call_count}}` - ✅ Available (gnucobol.analysis.lines_in_listing)
- `{{gnucobol_unique_programs}}` - ✅ Derived from program_calls
- `{{gnucobol_success}}` - ✅ Available (gnucobol.success)

### Code Explanation
- `{{comprehensive_code_explanations}}` - ✅ LLM Generated (chunked)
- `{{detailed_execution_sequence}}` - ✅ LLM Generated
- `{{code_reference_links}}` - ✅ Generated from line numbers

---

## Essential Fields to Add to Filtering

### In `filter_metadata_for_pass()` - Add These Fields:

```python
# GnuCOBOL essential scalars (currently MISSING):
filtered["gnucobol_analysis"] = {
    ...existing fields...
    "file_path": gnucobol.get("file_path"),  # ← ADD THIS
    "success": gnucobol.get("success"),       # ← ADD THIS
    "message": gnucobol.get("message"),       # ← ADD THIS
}

# CTags essential fields (currently MISSING):
filtered["ctags_outline"] = {
    ...existing fields...
    "file": ctags.get("outline", {}).get("file"),  # ← ADD THIS
    "symbol_count": ctags.get("symbol_count"),      # ← ADD THIS
}

# SuperBol essential fields (currently MISSING):
filtered["superbol_symbols"] = {
    ...existing fields...
    "success": superbol_symbols.get("success"),  # ← ADD THIS
    "error": superbol_symbols.get("error"),      # ← ADD THIS
}
```

---

## Summary

**Total Placeholders**: 91
**Available**: 88 (96.7%)
**Missing**: 3 (3.3%)

**Missing Placeholders**:
1. ❌ `source_file_path` - FIX: Add gnucobol.file_path to context
2. ❌ Called-by relationships - FIX: Phase 3 (build reverse call graph)
3. ❌ Minor scalar fields (success, error) - FIX: Add to filtering

**Next Steps**:
1. ✅ Task 2.1 Complete - Mapping done
2. ⏳ Task 2.2 - Enhance filter_metadata_for_pass()
3. ⏳ Task 2.3 - Update build_section_context()
