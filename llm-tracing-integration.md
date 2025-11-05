# LLM Call Tracing Integration

## Overview

The COBOL Documentation Agent now includes comprehensive LLM call tracing to track performance, token usage, and runtime statistics for every LLM invocation during documentation generation.

---

## What's Tracked

For **EACH LLM CALL** made during agent runtime:

1. **Timing**: Duration in seconds (start to finish)
2. **Tokens**:
   - Input tokens (estimated from prompt text)
   - Output tokens (estimated from response)
   - Total tokens
3. **Metadata**:
   - Section ID and title
   - Pass number (for two-pass mode)
   - Chunk number (for large file processing)
   - Model name (gpt-4o, claude-3-5-sonnet, etc.)
4. **Timestamps**: Start and end timestamps

## Output Files

When you run the agent, two trace files are generated:

```
llm_trace_<program_name>.jsonl          # JSONL log (machine-readable)
llm_trace_<program_name>_report.txt     # Human-readable detailed report
```

### JSONL Log Format

Each line is a JSON object:

```json
{"type": "session_start", "timestamp": "2025-01-04T10:30:00", "agent": "cobol_doc_agent"}
{"type": "llm_call", "call_id": 1, "section_id": "executive-summary", "model": "gpt-4o", "duration_seconds": 3.245, "input_tokens": 15234, "output_tokens": 856, ...}
{"type": "llm_call", "call_id": 2, "section_id": "program-structure", "model": "gpt-4o", "duration_seconds": 2.891, "input_tokens": 12456, "output_tokens": 643, ...}
...
{"type": "session_end", "timestamp": "2025-01-04T10:35:00", "summary": {...}, "section_stats": {...}}
```

### Text Report Format

Comprehensive human-readable report with:
- Summary statistics (total calls, duration, tokens)
- Per-section breakdown
- Individual call details

---

## Runtime Output

At the end of agent execution, you'll see:

```
==============================================================================
LLM CALL TRACE SUMMARY
==============================================================================

Total LLM Calls: 18
Total Duration: 2.35 minutes (141.2 seconds)
Average Call Duration: 7.844 seconds

Token Usage:
  Input Tokens:  245,678
  Output Tokens: 12,345
  Total Tokens:  258,023
  Avg Input:     13,648.8 tokens/call
  Avg Output:    685.8 tokens/call

------------------------------------------------------------------------------
PER-SECTION BREAKDOWN
------------------------------------------------------------------------------
Section                                  Calls    Duration     Tokens
------------------------------------------------------------------------------
detailed-code-explanation                5        58.2s        125,456
control-flow-analysis                    2        18.5s        45,234
executive-summary                        1        8.3s         15,678
...
==============================================================================

✓ Trace log written to: llm_trace_MINDISTCALC.jsonl
✓ Detailed report written to: llm_trace_MINDISTCALC_report.txt
```

---

## Integration Details

### Files Modified

1. **`cobol_doc_agent.py`**:
   - `generate_documentation()`: Initialize and finalize tracer
   - `generate_section_content()`: Wrap LLM calls with tracer
   - `process_section_recursive()`: Pass pass_number to child calls
   - `process_large_file_in_chunks()`: Pass chunk_number to child calls

2. **`llm_tracer.py`** (new file):
   - `LLMCallTracer` class: Core tracking logic
   - Token estimation (1 token ≈ 4 chars)
   - JSONL logging
   - Summary report generation

### Key Functions

```python
# Initialize tracer at start of documentation generation
from llm_tracer import init_tracer, finalize_tracer
tracer = init_tracer(f"llm_trace_{program_name}.jsonl")

# Tracer is automatically used in generate_section_content()
from llm_tracer import get_tracer
tracer = get_tracer()
tracer.start_call(section_id, section_title, pass_number, chunk_number, model)
response = llm.invoke(messages)
tracer.end_call(response, input_messages, input_text)

# Finalize at end (in finally block to ensure execution)
finalize_tracer()
```

---

## Use Cases

### Performance Analysis
- Identify slow sections: Which sections take the longest?
- Optimize token usage: Which sections use the most tokens?
- Model comparison: Test different models and compare performance

### Cost Estimation
- Calculate API costs based on token usage
- Project costs for large batches of programs
- Optimize prompt engineering to reduce tokens

### Runtime Debugging
- Track exactly where agent is spending time
- Identify bottlenecks in documentation generation
- Verify two-pass mode and chunking behavior

### Quality Metrics
- Correlate section quality with token usage
- Identify sections that may need more/less context
- Measure impact of program map vs full source code

---

## Token Estimation

The tracer uses a **conservative** token estimation:

```python
estimated_tokens = len(text) // 4
```

This approximates **1 token ≈ 4 characters**, which aligns with:
- OpenAI's tokenizer (GPT-3.5/4): ~4 chars/token average
- Anthropic's tokenizer (Claude): ~4-5 chars/token average

**Note**: These are estimates. For exact token counts, use the provider's tokenizer API.

---

## Example: Large File Processing

For a 26,755-line COBOL file processed in 5 chunks:

```
LLM CALL TRACE SUMMARY
==============================================================================

Total LLM Calls: 13
Total Duration: 3.45 minutes (207 seconds)

PER-SECTION BREAKDOWN
------------------------------------------------------------------------------
Section                                  Calls    Duration     Tokens
------------------------------------------------------------------------------
detailed-code-explanation                5        145.2s       478,234
  └─ Chunk 1/5                          1        28.5s        95,678
  └─ Chunk 2/5                          1        2.1s         2,456
  └─ Chunk 3/5                          1        32.8s        98,234
  └─ Chunk 4/5                          1        41.2s        145,678
  └─ Chunk 5/5                          1        40.6s        136,188
executive-summary                        1        8.3s         15,678
control-flow-analysis                    2        18.5s        45,234
...
```

This shows:
- Section breakdown by call count and duration
- Individual chunk performance
- Token distribution across chunks

---

## Future Enhancements

Potential improvements:

1. **Real Token Counting**: Use provider's tokenizer API for exact counts
2. **Cost Calculation**: Automatic cost estimation based on model pricing
3. **Visualization**: Generate charts/graphs of token usage and timing
4. **Historical Tracking**: Compare runs over time
5. **Alerts**: Warn if token usage exceeds thresholds
6. **Streaming Support**: Track streaming LLM calls

---

## Implementation Status

✅ **Complete and Integrated**

All features implemented and tested:
- Per-call timing ✓
- Token estimation ✓
- Section/pass/chunk tracking ✓
- JSONL logging ✓
- Summary reports ✓
- Finalization in finally block ✓

Ready for production use.
