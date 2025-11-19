# Test Mode: Prompt Quality Hypothesis Testing

**Date**: 2025-11-14
**Purpose**: Test if improved YAML prompts alone can achieve 100% code coverage without retries or fallback mechanisms

---

## Hypothesis

With sufficiently detailed and structured prompts in the YAML template, the LLM can be instructed to return the COMPLETE COBOL code block verbatim on the FIRST attempt, eliminating the need for:
- Retry logic
- Source code fallback/insertion
- Gap-filling passes

---

## Changes Made (All in cobol_doc_agent.py)

### 1. ✅ Disabled Retry Logic (Lines 1937-2037)

**Before**: Up to 2 attempts (1 initial + 1 retry)
```python
max_retries = 1  # 2 attempts total
for attempt in range(1, max_retries + 2):
    # Generate content
    # If coverage < 95%, retry with aggressive feedback
```

**After**: Single attempt only, no retries
```python
# TEST MODE: RETRIES DISABLED
attempt = 1  # SINGLE ATTEMPT ONLY
try:
    # Generate content once
    # Log coverage (no retry decisions)
```

**Impact**: Tests whether prompt quality alone can achieve completeness

---

### 2. ✅ Disabled Source Code Fallback (Lines 2051-2107)

**Before**: Always insert original source code to guarantee 100% coverage
```python
# Extract explanations from LLM
llm_explanations = extract_explanations_from_llm_response(chunk_result)

# Add original source code
final_chunk_doc = f"""
### Complete Source Code
```cobol
{chunk_info['content']}  ← ORIGINAL SOURCE (100% guaranteed)
```

### Detailed Explanations
{llm_explanations}  ← LLM's explanation
"""
```

**After**: Use ONLY LLM's raw response (no source insertion)
```python
# TEST MODE: Use raw LLM response as-is
final_chunk_doc = f"""
{chunk_result}  ← ONLY what LLM returned

**[TEST MODE] Validation Summary:**
- LLM returned lines: {validation_result.found_lines}
- LLM coverage: {explanation_coverage:.1f}%
- **Using ONLY LLM response (no source fallback)**
"""
```

**Impact**: Reveals actual LLM coverage without any safety net

---

### 3. ✅ Kept Validation & Logging (Lines 1997-2013)

**Validation still active** to measure and report:
- ✅ Total lines in chunk
- ✅ Expected executable lines
- ✅ LLM returned lines
- ✅ Coverage percentage
- ✅ Missing line count

**Example output**:
```
  ✓ Complete: 98.5% coverage (197/200 executable lines)
     [TEST MODE] LLM returned complete code

  ⚠ Incomplete: 75.3% coverage (150/199 executable lines)
     Missing: 49 executable lines
     [TEST MODE] Recording LLM coverage as-is (no retry, no fallback)
```

---

### 4. ✅ Gap-Filling Already Disabled (Line 2143)

No changes needed - already disabled by default:
```python
ENABLE_GAP_FILLING = False  # Feature flag
```

---

## What Gets Tested

### Prompt Quality Factors:

1. **Explicitness**: Does YAML instruction clearly state "return COMPLETE code verbatim"?
2. **Structure**: Are requirements formatted clearly (numbered lists, bold emphasis)?
3. **Examples**: Does template show expected format?
4. **Positioning**: Is instruction placed optimally (after code block)?
5. **Redundancy**: Are critical requirements repeated in multiple places?

### Measured Outcomes:

| Metric | What It Shows |
|--------|---------------|
| **Coverage %** | How much code LLM returned vs expected |
| **Complete chunks** | # chunks with ≥95% coverage |
| **Incomplete chunks** | # chunks with <95% coverage |
| **Missing lines** | Specific line count LLM omitted |

---

## Test Execution

### Command:
```bash
cd /home/santosh/cobol-work/agent
python3 cobol_doc_agent.py <PROGRAM-NAME> \
    --workspace ../workspace \
    --output-dir ../metadata \
    --docs-path ../docs \
    --template ./cobol-doc-template.yaml
```

### What to Observe:

1. **Console Output**:
   ```
   Processing chunk 1/25...
     Lines: 500 total, 480 executable, 20 non-executable
     (Comments: 15, Page breaks: 5)

     ✓ Complete: 98.5% coverage (473/480 executable lines)
        [TEST MODE] LLM returned complete code
   ```

2. **Generated Documentation**:
   - Check `../docs/<PROGRAM>-documentation.md`
   - Look for `[TEST MODE]` markers in validation summaries
   - Compare line counts: expected vs LLM returned

3. **LLM Trace**:
   - Check `llm_trace_<PROGRAM>.jsonl`
   - Count LLM calls (should be fewer without retries)
   - Check input/output token usage

---

## Success Criteria

### 🎯 Hypothesis CONFIRMED if:
- ✅ Average coverage across all chunks ≥ 95%
- ✅ Most chunks (>80%) achieve 100% coverage on first attempt
- ✅ No missing critical code sections (only minor omissions like comments)

### ❌ Hypothesis REJECTED if:
- ❌ Average coverage < 90%
- ❌ Many chunks have significant gaps (>10% missing)
- ❌ LLM consistently skips data definitions, FILLERs, or table entries

---

## Reverting Changes

To restore normal operation (with retries and source fallback):

### Option 1: Uncomment Code Blocks
Search for `# TEST MODE:` and `# COMMENTED OUT:` blocks and uncomment the original logic

### Option 2: Git Restore (if committed before test)
```bash
git restore cobol_doc_agent.py
```

### Option 3: Manual Restoration
1. Line 1941: Change `attempt = 1` to `for attempt in range(1, max_retries + 2):`
2. Lines 1952-1982: Uncomment retry feedback logic
3. Lines 2056-2086: Uncomment original source insertion
4. Lines 2088-2104: Delete TEST MODE section

---

## Expected Learning Outcomes

### If Prompts Work Well (≥95% coverage):
- ✅ Can simplify code generation logic
- ✅ Reduce API calls (no retries needed)
- ✅ Faster documentation generation
- ✅ Lower costs (fewer output tokens)
- ✅ Confirms: Good prompting > Complex retry logic

### If Prompts Fall Short (<90% coverage):
- ❌ Retries and fallbacks are necessary
- ❌ LLM inherently abbreviates/summarizes long code
- ❌ Need more sophisticated post-processing
- ❌ Should investigate chunking strategy alternatives
- ✅ Confirms: Safety nets (source insertion) are valuable

### If Results are Mixed (90-95% coverage):
- 🤔 Prompts help but aren't sufficient alone
- 🤔 Selective retries (only for <90% coverage) might be optimal
- 🤔 Consider hybrid: good prompts + minimal fallback
- 🤔 Some code patterns (FILLER tables, DATA divisions) harder for LLM

---

## Next Steps After Test

Based on results, decide:

1. **If ≥95% coverage**: Keep test mode, remove commented code permanently
2. **If 90-95% coverage**: Implement selective retry (only when coverage <90%)
3. **If <90% coverage**: Restore full retry + fallback mechanisms, improve prompts further

Document findings and update prompt engineering best practices for COBOL code documentation.

---

**Test Mode Active**: ✅ Ready for testing
**Retry Logic**: ❌ Disabled
**Source Fallback**: ❌ Disabled
**Validation/Logging**: ✅ Active
**Gap-Filling**: ❌ Already disabled

**Status**: System configured for pure prompt quality testing
