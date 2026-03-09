# Enhancement: Structured Plaintext Prompt Format

## Problem

Currently, `generate_section_content()` in `cobol_doc_agent.py` (line 2050-2098) serializes the entire `chunk_context` dict as **raw compact JSON** and embeds it directly in the user prompt:

```python
context_json = json.dumps(context)       # line 2050
metadata_str = context_json              # line 2098
user_prompt = f"""Generate documentation for this section using the following metadata:

{metadata_str}                           # line 2128 — raw JSON blob
"""
```

This means the LLM receives source code, program map, and instructions with:
- All newlines escaped as `\n`
- All quotes escaped as `\"`
- Markdown headers flattened into JSON string values
- Code indentation lost in the escaped representation

**Impact**: LLMs comprehend properly formatted text significantly better than escaped JSON strings — especially for source code where indentation and line breaks carry structural meaning.

---

## Current Chunk Context Keys (Phase 1)

Built in `process_large_file_in_chunks()` (~line 2415-2435):

| Key | Type | Content | Best Format |
|-----|------|---------|-------------|
| `program_name` | str | "BroadcastService" | Plaintext header |
| `timestamp` | str | ISO timestamp | Plaintext header |
| `source_file_path` | str/None | File path | Plaintext header |
| `source_code` | str | Program map + source chunk (already formatted markdown) | **Plaintext** (as-is) |
| `chunk_number` | int | 3 | Plaintext header |
| `total_chunks` | int | 3 | Plaintext header |
| `start_line` | int | 3225 | Plaintext header |
| `end_line` | int | 3810 | Plaintext header |
| `line_count` | int | 586 | Plaintext header |
| `syntax_tree` | dict | Filtered AST for chunk | JSON (structured data) |

---

## Proposed Format

Replace the single JSON blob with **structured plaintext sections**, keeping JSON only for structured metadata that is genuinely key-value/nested data:

```
Generate documentation for this section.

## File: BroadcastService
Chunk: 3/3 (lines 3225–3810, 586 lines)

### Program Structure Map
# Program Map: BroadcastService

## Namespaces
- broadcasts (line 3)
- ng.utils.data.readers (line 3801)

## Types
- interface IDataReceiverControls (line 3803)
...

## Summary
- Namespaces: 2, Types: 2, Methods: 0, Properties: 152

### Source Code (lines 3225–3810)

```csharp
public bool AutoLogging
{
    get { return this.autoLogging; }
    set { this.autoLogging = value; }
}
...
```

### Syntax Tree (filtered for lines 3225–3810)

```json
{"type": "compilation_unit", "children": [...]}
```

Remember:
- Program name: BroadcastService
- Follow template structure exactly
- Reference line numbers from metadata
- Generate valid Markdown and Mermaid syntax
```

---

## Implementation Plan

### Change Location

`cobol_doc_agent.py` — `generate_section_content()` function (lines 2040-2136)

### Step 1: Add `format_context_as_plaintext()` helper (~line 2040)

```python
def format_context_as_plaintext(context: Dict[str, Any]) -> str:
    """
    Format chunk context as structured plaintext instead of raw JSON.

    Human-readable content (source code, program map) is rendered as-is.
    Structured data (syntax_tree) remains as compact JSON.
    """
    parts = []

    # Header metadata
    program = context.get('program_name', 'UNKNOWN')
    chunk_num = context.get('chunk_number', '')
    total = context.get('total_chunks', '')
    start = context.get('start_line', '')
    end = context.get('end_line', '')
    lines = context.get('line_count', '')

    parts.append(f"## File: {program}")
    if chunk_num:
        parts.append(f"Chunk: {chunk_num}/{total} (lines {start}–{end}, {lines} lines)")
    parts.append("")

    # Source code (already contains program map + code as formatted markdown)
    source = context.get('source_code', '')
    if source:
        parts.append(source)
        parts.append("")

    # Structured metadata — keep as JSON
    syntax_tree = context.get('syntax_tree')
    if syntax_tree:
        parts.append("### Syntax Tree (filtered for this chunk)")
        parts.append("```json")
        parts.append(json.dumps(syntax_tree, separators=(',', ':')))
        parts.append("```")
        parts.append("")

    # Any other context keys (Phase 2 may have additional keys)
    skip_keys = {'program_name', 'timestamp', 'source_file_path', 'source_code',
                 'chunk_number', 'total_chunks', 'start_line', 'end_line',
                 'line_count', 'syntax_tree'}
    extras = {k: v for k, v in context.items() if k not in skip_keys and v}
    if extras:
        parts.append("### Additional Context")
        parts.append("```json")
        parts.append(json.dumps(extras, separators=(',', ':')))
        parts.append("```")
        parts.append("")

    return "\n".join(parts)
```

### Step 2: Replace `metadata_str = context_json` (line 2098)

```python
# Before (current):
metadata_str = context_json

# After:
metadata_str = format_context_as_plaintext(context)
```

**Keep `context_json`** for the token counting and truncation logic above (lines 2050-2096) — that still needs JSON for size estimation. Only the final prompt assembly changes.

### Step 3: Update user prompt template (line 2126)

```python
# Before:
user_prompt = f"""Generate documentation for this section using the following metadata:

{metadata_str}
...

# After:
user_prompt = f"""Generate documentation for this section.

{metadata_str}
...
```

Minor wording change — "metadata" → remove since it's no longer a JSON blob.

---

## Token Impact

The plaintext format should be **slightly smaller** than JSON because:
- No `{"key": "value"}` wrapper overhead
- No escaped `\n` (real newlines are 1 token vs `\n` being extra)
- No escaped `\"` around strings
- No comma/brace structural tokens

Estimated savings: **~5-8%** fewer tokens for the same content.

---

## Phase 2 Consideration

Phase 2 (`run_phase2_sections()`) also uses `generate_section_content()` with a different context shape (prose, section-specific metadata). The `format_context_as_plaintext()` function should handle both shapes via the `skip_keys` + `extras` pattern — unknown keys fall through to the JSON `Additional Context` block.

---

## Scope

- **Change**: Only the prompt formatting in `generate_section_content()`
- **No change**: Token estimation, truncation logic, system prompt, template, LLM call mechanics
- **Risk**: Low — the LLM receives the same information, just better formatted
- **Rollback**: Revert `metadata_str` back to `context_json`

---

## Verification

1. Run the agent on one file with the change
2. Compare the request debug file (`chunk-01-pass1.md`) — should show properly formatted sections
3. Compare output quality — code explanation should be at least as good (likely better)
4. Compare token counts — should be equal or slightly lower
