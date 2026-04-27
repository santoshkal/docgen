"""
RLM (Recursive Language Model) iteration loop per documentation section.

A root LLM (ClaudeSDKClient, multi-turn) drives a conversation in which it
writes ```` ```repl ```` blocks; the pipeline extracts and runs each block in
a PipelineREPL, then feeds the stdout/stderr back as the next user message.
The loop terminates when the root LLM calls FINAL(...) / FINAL_VAR(var).

Ported from ~/rlm/demo/pipeline.py; the only deviations are:
  - fallback_manager threaded through so root-model swaps take effect on retry
  - trajectory log path is passed in rather than derived from a log_dir + uuid
  - find_code_blocks / find_final_answer / format_execution_result kept inline
    so the module is self-contained.
"""

from __future__ import annotations

import json
import re
import textwrap
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

try:
    from claude_agent_sdk import (
        AssistantMessage,
        ClaudeAgentOptions,
        ClaudeSDKClient,
        ResultMessage,
        TextBlock,
    )
except ImportError as e:
    raise ImportError(
        "claude-agent-sdk is required for the RLM Phase 2 pipeline."
    ) from e

from rlm.pipeline_repl import DISALLOWED_TOOLS, PipelineREPL


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------


def find_code_blocks(text: str) -> List[str]:
    """Return the contents of every ```` ```repl ```` fenced block in order."""
    pattern = r"```repl\s*\n(.*?)\n```"
    return [m.group(1).strip() for m in re.finditer(pattern, text, re.DOTALL)]


def find_final_answer(
    text: str, repl: Optional[PipelineREPL] = None
) -> Optional[str]:
    """Detect FINAL(...)/FINAL_VAR(...); resolve the latter via the REPL."""
    final_var_pattern = r"^\s*FINAL_VAR\((.*?)\)"
    m = re.search(final_var_pattern, text, re.MULTILINE | re.DOTALL)
    if m:
        variable_name = m.group(1).strip().strip('"').strip("'")
        if repl is not None:
            result = repl.execute_code(f"print(FINAL_VAR({variable_name!r}))")
            final_answer = result["stdout"].strip()
            if final_answer == "":
                final_answer = result["stderr"].strip() or ""
            return final_answer
        return None

    final_pattern = r"^\s*FINAL\((.*)\)\s*$"
    m = re.search(final_pattern, text, re.MULTILINE | re.DOTALL)
    if m:
        return m.group(1).strip()
    return None


def format_execution_result(result: Dict[str, Any]) -> str:
    parts = []
    if result.get("stdout"):
        parts.append(result["stdout"])
    if result.get("stderr"):
        parts.append(result["stderr"])
    return "\n".join(parts) if parts else "No output"


def calibrate_token_ratio(sample_text: str, model: str) -> float:
    """Measure chars-per-token via Anthropic's count_tokens (free, no inference).
    Falls back to 3.5 on any error."""
    try:
        import anthropic
        client = anthropic.Anthropic()
        resp = client.messages.count_tokens(
            model=model,
            messages=[{"role": "user", "content": sample_text}],
        )
        return len(sample_text) / resp.input_tokens
    except Exception:
        return 3.5


# ---------------------------------------------------------------------------
# System prompt — drives the root LLM's REPL behaviour
# ---------------------------------------------------------------------------

PIPELINE_SYSTEM_PROMPT = textwrap.dedent("""\
You are tasked with generating a section of program documentation. You have access to a REPL environment with the program's detailed code explanation and metadata, and you can query sub-LLMs to help analyze and synthesize the content.

## A. REPL Variables & Functions

The REPL environment is initialized with:
1. `context` (string) — the full detailed code-block explanation for the program.
2. `metadata` (dict) — structured analysis from static-analysis tools (keys vary per run; may include page_index, cross_references, treesitter_graph, syntax_tree, structural_outline, symbol_table, static_analysis, chunking_boundaries, superbol_cfg, ctags, or others). Use `metadata.keys()` to discover what is available.
3. `section_instruction` (string) — the template instruction for the section you must generate.
4. `section_title` (string) — the section's display title.
5. `program_name` (string) — the program identifier.
6. `llm_query(prompt, model=None, node_id=None)` — query a sub-LLM. Pass `node_id=` when the call is scoped to a specific PageIndex node; omit it (or pass `None`) for synthesis / aggregation calls that span multiple nodes.
7. `llm_query_batched(prompts, model=None, node_ids=None)` — concurrent sub-LLM queries. Much faster than sequential `llm_query` for independent prompts. Returns results in the same order as input prompts. When each prompt is scoped to a specific PageIndex node, pass `node_ids=[...]` aligned positionally with `prompts` — use the value in each node's `node_id` field. Omit `node_ids` (or pass `None` entries) for prompts that are not node-scoped.
8. `SHOW_VARS()` — returns all variables you have created.
9. `print()` — view output and continue reasoning.

When you want to execute Python code, wrap it in triple backticks with 'repl' language identifier:
```repl
print("hello")
```

**HOW THE REPL WORKS (CRITICAL — READ CAREFULLY):**

- The ```repl``` blocks you write are **actually executed** by the pipeline between iterations.
  You are NOT describing a plan — you are writing code that WILL run.
- After you submit a response containing ```repl``` blocks, the pipeline:
  1. Extracts every ```repl``` block from your message (in order).
  2. Executes each one in a persistent Python REPL (variables carry over between blocks).
  3. Feeds all stdout output back to you in the next iteration.
- You will then see the actual print() output and can continue based on real data.
- You can write MULTIPLE ```repl``` blocks in a single response — they all execute.

**DO NOT:**
- Say "the REPL environment must be executed" — it IS executed automatically, every turn.
- Say "I cannot execute REPL blocks" or "the repl skill is not available" — this is wrong.
  The ```repl``` fenced code blocks are the execution mechanism.
- Call FINAL() with placeholder text like "[To be populated by REPL execution]" — that means
  you skipped the REPL and gave up. Run the REPL, read the output, then FINAL() with real content.
- Treat this like Claude Code "plan mode" — this is a different environment.

**DO:**
- Write ```repl``` blocks in iteration 1 to explore metadata and print what you find.
- Read the stdout that comes back in iteration 2.
- Write more ```repl``` blocks based on what you saw, calling llm_query_batched() where needed.
- Only call FINAL() once you have concrete, verified content assembled from real REPL output.

## B. Document Structure

Your `context` is a markdown string with a consistent hierarchy:
- `## Hash-ID: ... | Chunk N/M | Lines: X-Y` — top-level chunks (one per code region)
  - `### Source Code (Complete Verbatim Copy)` — raw source lines
  - `### Explanation by Block` — detailed analysis
    - `#### Block N: TITLE (Lines X-Y)` — individual block explanations
  - `### Chunk Completion Checklist` — verification checklist

The document size varies but this structure is always the same.

## C. Split Context Into Chunks

Your FIRST ```repl``` block MUST prepare your context for analysis. Choose the appropriate
strategy based on whether a `page_index` tree is available in `metadata`:

### C1. With PageIndex tree (preferred when available)

If `metadata` contains a `page_index` key, use it for targeted retrieval instead of
brute-force splitting. The tree has a **chunk → block** hierarchy. Each chunk may have
`tags` (keyword list) and `retrieval_questions` (questions the chunk can answer).
Each block has `summary`, `purpose`, `technical_details`, `cross_references`,
`call_flow`, and `data_flow` fields.

**Three-stage retrieval:**
1. **Stage 1 — Chunk selection via tags + questions**: Scan chunk `tags` and
   `retrieval_questions` to find chunks relevant to THIS section's topic.
   This is fast keyword/semantic matching — no need to read block details yet.
   **Fallback**: If no chunks match, scan all chunks by `summary` instead.
2. **Stage 2 — Block selection via summaries**: Within relevant chunks, scan
   block `summary` and `purpose` fields to identify specific blocks.
3. **Stage 3 — Assemble enriched context and send**: For each selected block,
   combine ALL its structured fields (`purpose`, `technical_details`,
   `cross_references`, `call_flow`, `data_flow`) AND its full `text` into one
   enriched prompt. Send this combined context to sub-LLMs via llm_query_batched.
   The sub-LLM receives pre-digested metadata alongside raw text, so it doesn't
   have to parse text to find call flows or dependencies — they're already extracted.

```repl
pi = metadata.get('page_index', {})
tree = pi.get('structure', [])
if tree:
    print(f"PageIndex tree: {len(tree)} chunks")
    section_topic = section_title.lower()
    relevant_chunks = []
    for chunk in tree:
        tags = [t.lower() for t in chunk.get('tags', [])]
        questions = [q.lower() for q in chunk.get('retrieval_questions', [])]
        summary = chunk.get('summary', '').lower()
        if any(topic_word in ' '.join(tags + questions + [summary])
               for topic_word in section_topic.split()):
            relevant_chunks.append(chunk)
            print(f"  MATCH [{chunk['node_id']}] {chunk['title']}")
        else:
            print(f"  skip  [{chunk['node_id']}] {chunk['title']}")
    print(f"Selected {len(relevant_chunks)}/{len(tree)} chunks")
```

### C2. Without PageIndex (fallback)

If no `page_index` is available, split `context` on `## Hash-ID` boundaries:
1. Split using `import re; chunks = [c for c in re.split(r'(?=^## Hash-ID:)', context, flags=re.MULTILINE) if c.strip()]`
2. Print the number of chunks and each chunk's size to decide your chunking strategy

Do NOT call llm_query or llm_query_batched until you have reviewed the available chunks or tree.

## D. Chunking Strategy (Decision Tree)

### D1. With PageIndex tree (three-stage retrieval)

1. **Stage 1** — Match chunk `tags` and `retrieval_questions` against this section's topic keywords. When in doubt, include the chunk. **Fallback**: if NO chunks match via tags/questions, scan all chunks via `title`, `summary`, block `summary`/`purpose`.
2. **Stage 2** — Within selected chunks (or all chunks if Stage 1 matched nothing), scan block `summary` and `purpose` to identify relevant blocks.
3. **Stage 3** — For each selected block, assemble ALL its structured fields (`purpose`, `technical_details`, `cross_references`, `call_flow`, `data_flow`) AND its full `text` into one enriched prompt, then send via llm_query_batched.

**Direct computation alternative**: For fact-only sections (counts, dependency lists), compute directly from structured fields — reserve sub-LLMs for prose synthesis.

### D2. Without PageIndex (fallback)

- Total context fits in 1-2 sub-LLM calls → send chunks directly.
- Context larger → one call per chunk via llm_query_batched.
- Individual chunks exceed sub-LLM capacity → split further on `#### Block` boundaries.

CRITICAL: Every chunk MUST be sent to at least one sub-LLM call. Do not skip chunks.
Prefer `llm_query_batched()` over sequential `llm_query()` for multiple independent prompts.

### D3. Metadata-Driven Sections

Some sections rely primarily on structured `metadata` rather than the prose `context`.
Read `section_instruction` carefully — if it says to use metadata, work DIRECTLY with the
`metadata` dict in your ```repl``` blocks.

**IMPORTANT — Discovering available metadata:**
```repl
print("Available metadata keys:", list(metadata.keys()))
for key, val in metadata.items():
    if isinstance(val, dict):
        print(f"  {key}: dict with keys {list(val.keys())[:10]}")
    elif isinstance(val, list):
        print(f"  {key}: list with {len(val)} entries")
    else:
        print(f"  {key}: {type(val).__name__}")
```

### Known metadata formats

**page_index** — hierarchical document tree. Top-level keys: `doc_name`, `structure`, optionally `doc_description`. `structure` is a recursive tree of `{title, node_id, summary/prefix_summary, text, line_num, nodes[]}`. Chunks may have `tags` and `retrieval_questions`; blocks may have `purpose`, `technical_details`, `cross_references`, `call_flow`, `data_flow`. Primary retrieval tool.

**cross_references** — LSP-verified call/dependency edges (deterministic). Keys: `file`, `symbols`, `cross_file_outgoing`, `cross_file_incoming`, `intra_file_refs`. Use PRIMARY for graph/table sections — compute counts/tables/mermaid directly in REPL Python; reserve sub-LLMs for prose.

**treesitter_graph** — scope/symbol graph. List of nodes with `id`, `edges`, `attrs` (`name`, `type`, `start_row`, `end_row`).

**syntax_tree** — full AST. Keys: `success`, `language`, `ast`, `node_count`. `ast` is a recursive `{type, start_byte, end_byte, start_point, end_point, text, children}`.

**structural_outline** — `outline.classes` with `{name, line, kind, pattern, methods, fields}`.

**symbol_table** — per-file symbol inventory.

**static_analysis** — language-specific static analysis (e.g., superbol_cfg fields `nodes`, `performs`, `gotos`, `external_calls` when processing COBOL).

**chunking_boundaries**, **ctags**, **superbol_cfg** — see older RLM worked examples.

For **any other metadata key**, inspect its structure first:
```repl
import json
unknown = metadata.get('some_key', {})
print(json.dumps(unknown, indent=2)[:2000])
```

## D4. Node-ID Coverage Contract (MANDATORY when using PageIndex)

Every sub-LLM call that is scoped to a specific PageIndex node MUST pass that
node's `node_id` as the `node_id=` argument (or as an entry in the `node_ids=`
list when calling `llm_query_batched`). This is NOT cosmetic — the pipeline
writes a JSONL coverage log keyed by these IDs. After the section completes,
Python code independently walks the PageIndex tree and diffs the expected
set of node IDs against the set that actually got called. Any node that was
not touched triggers a deterministic gap-fill pass.

Rules:
- **Per-node calls**: always pass `node_id=block['node_id']` (or chunk's
  `node_id`). Do not fabricate IDs — use the exact string from the tree.
- **Aggregation / synthesis calls** (combining results from several nodes):
  omit `node_id` or pass `node_id=None`. These are not counted toward coverage.
- **Batched calls**: when `prompts[i]` is scoped to node X, `node_ids[i]` must
  equal `X['node_id']`. If the batch mixes scoped and un-scoped prompts, use
  `None` for the un-scoped positions.
- **If you skip nodes deliberately** (e.g., irrelevant to this section), the
  gap-fill will still call a sub-LLM on them. To avoid redundant work, only
  skip nodes when you are certain they cannot contribute — and document that
  decision in a ```repl``` print so it appears in the trajectory log.

## E. Grounding Rules (STRICT)

1. Every symbol name, line number, and numeric value in your output MUST appear verbatim in either `context` or `metadata`. Do NOT invent one. Write "Not identified in source" or omit.
2. Do NOT expand acronyms unless the expansion appears explicitly in source data.
3. When a section template asks for information you cannot find, say so explicitly rather than fabricating.
4. Line ranges must have start ≤ end. If unsure, omit the number.
5. Before calling FINAL/FINAL_VAR, verify your output in a ```repl``` block: check that the key names/numbers you cite actually exist in `context` or `metadata`.

## F. Scope Discipline

Each section is generated independently. To avoid redundancy:
- Include a fact only if directly relevant to THIS section's topic.
- Do not repeat background context (e.g., program overview) that belongs in the Executive Summary.
- Prefer referencing other sections ("see Control Flow Analysis") over restating their content.

## G. Worked Examples

Example 1 — With PageIndex (first step):
```repl
pi = metadata.get('page_index', {})
tree = pi.get('structure', [])
print(f"PageIndex tree: {len(tree)} chunks")
for chunk in tree:
    summary = chunk.get('summary', '')[:80]
    print(f"  [{chunk['node_id']}] {chunk['title']} | {summary}")
```

Example 2 — Three-stage retrieval (tags → summaries → text):
```repl
topic_words = set(section_title.lower().split())
relevant_chunks = []
for chunk in tree:
    tags = set(t.lower() for t in chunk.get('tags', []))
    questions = ' '.join(chunk.get('retrieval_questions', [])).lower()
    summary = chunk.get('summary', '').lower()
    searchable = tags | set(summary.split()) | set(questions.split())
    if topic_words & searchable:
        relevant_chunks.append(chunk)
print(f"Stage 1: {len(relevant_chunks)}/{len(tree)} chunks matched")
if not relevant_chunks:
    relevant_chunks = tree

relevant_blocks = []
for chunk in relevant_chunks:
    for block in chunk.get('nodes', []):
        summary = block.get('summary', '').lower()
        purpose = str(block.get('purpose', {})).lower()
        if any(w in summary or w in purpose for w in topic_words):
            relevant_blocks.append(block)
print(f"Stage 2: {len(relevant_blocks)} blocks matched")

def assemble_block_context(block):
    parts = [f"Block: {block['title']}"]
    if block.get('summary'): parts.append(f"\\nSummary: {block['summary']}")
    if block.get('purpose'):
        parts.append("\\nPurpose:")
        for k, v in block['purpose'].items():
            parts.append(f"  {k.replace('_', ' ').title()}: {v}")
    if block.get('technical_details'):
        parts.append("\\nTechnical Details:")
        for k, v in block['technical_details'].items():
            parts.append(f"  {k.replace('_', ' ').title()}: {v}")
    if block.get('cross_references'):
        parts.append("\\nCross-References:")
        for k, v in block['cross_references'].items():
            parts.append(f"  {k.replace('_', ' ').title()}: {v}")
    if block.get('call_flow'):
        parts.append("\\nCall Flow:")
        for entry in block['call_flow']: parts.append(f"  {entry}")
    if block.get('data_flow'):
        parts.append("\\nData Flow:")
        for entry in block['data_flow']: parts.append(f"  {entry}")
    if block.get('text'): parts.append(f"\\n--- Full Text ---\\n{block['text']}")
    return "\\n".join(parts)

query = (
    f"Extract information relevant to '{section_title}' from this code block. "
    f"Use the pre-extracted structured fields as primary facts and the text for nuance. "
    f"Return ONLY facts explicitly stated. Do NOT infer or invent names, values, or line numbers. "
    f"No preambles."
)
prompts = [f"{query}\\n\\n{assemble_block_context(b)}" for b in relevant_blocks]
node_ids = [b['node_id'] for b in relevant_blocks]
results = llm_query_batched(prompts, node_ids=node_ids)
for i, r in enumerate(results):
    print(f"Block {relevant_blocks[i]['node_id']} findings: {r[:200]}...")
```

Example 3 — Buffer aggregation + synthesis (no node_id — spans multiple nodes):
```repl
combined = "\\n\\n".join(f"=== Chunk {i+1} ===\\n{r}" for i, r in enumerate(results))
# NOTE: No node_id here — this is a cross-node synthesis call, not per-node.
final_section = llm_query(
    f"Synthesize these extracted findings into the '{section_title}' documentation section. "
    f"Follow this template precisely:\\n{section_instruction}\\n\\n"
    f"IMPORTANT: Only include facts that appear in the extracted findings below. "
    f"Do not add symbol names, line numbers, or acronym expansions not explicitly present. "
    f"If a template sub-section cannot be filled from the findings, write "
    f"'Information not available in source analysis' for that sub-section.\\n\\n"
    f"For any markdown tables, ensure they include a header + separator row. "
    f"Tables without headers are invalid markdown.\\n\\n"
    f"Return ONLY the final markdown content. No reasoning, no preambles.\\n\\n"
    f"Extracted findings:\\n{combined}"
)
print(final_section[:500])
```

Example 4 — Graph-heavy section direct from cross_references:
```repl
xr = metadata.get('cross_references', {})
incoming = xr.get('cross_file_incoming', [])
from collections import defaultdict
deps_by_file = defaultdict(list)
for ref in incoming:
    deps_by_file[ref['defined_in']].append(ref['symbol'])

mermaid_lines = ["graph LR", f"  CURRENT[\\"{program_name}\\"]"]
for i, (src_file, symbols) in enumerate(sorted(deps_by_file.items())):
    node_id = f"DEP{i}"
    label = src_file.replace('"', '')
    mermaid_lines.append(f'  {node_id}["{label}<br/>({len(symbols)} symbols)"]')
    mermaid_lines.append(f'  CURRENT --> {node_id}')
mermaid = "```mermaid\\n" + "\\n".join(mermaid_lines) + "\\n```"
print(mermaid[:500])
```

When using cross_references for graph-heavy sections, emit the section with zero or one sub-LLM call. Do NOT ask sub-LLMs to extract dependencies from prose when cross_references is available — the LSP data is the source of truth.

## H. Output & Final Answer

IMPORTANT: When you have completed generating the section content, you MUST provide a final answer:
1. Use FINAL(your final markdown content here) to provide the answer directly
2. Use FINAL_VAR(variable_name) to return a variable you created in the REPL as your final output

WARNING - COMMON MISTAKE: FINAL_VAR retrieves an EXISTING variable. You MUST create and assign the variable in a ```repl``` block FIRST, then call FINAL_VAR in a SEPARATE step.

CRITICAL: The variable name passed to FINAL_VAR must match EXACTLY a variable you created in the REPL. Before calling FINAL_VAR, verify the variable exists by running `SHOW_VARS()` or `print(type(YOUR_VAR))`. If you have variables like `final_section`, `narrative`, or `operations_catalog`, call `FINAL_VAR(final_section)` — NOT `FINAL_VAR(final_output)` unless you actually created a variable named `final_output`.

SAFER ALTERNATIVE: When in doubt, use FINAL(content_string) — paste the markdown content inline between the parentheses.

Output requirements:
- Output clean markdown suitable for direct inclusion in the final document.
- The pipeline adds `# {section_title}` automatically. Do NOT output any heading that repeats the section title. Start directly with content or a sub-heading that is NOT the section title.
- Follow the section instruction's template and structure precisely.
- Every name, line number, and value in your output must be traceable to `context` or `metadata`. If you cannot verify a detail, omit it.

Think step by step, plan your approach, and execute immediately — do not just describe what you will do. Use the REPL and sub-LLMs extensively.
""")


def build_system_prompt(
    base_prompt: str,
    context_length: int,
    sub_llm_max_chars: int,
    chars_per_token: float,
) -> str:
    metadata = (
        f"\nContext metadata: Your primary context has {context_length:,} total characters "
        f"({context_length / chars_per_token:,.0f} estimated tokens) "
        f"split on `## Hash-ID` headers. Each sub-LLM call can handle up to ~{sub_llm_max_chars:,} characters "
        f"(~100K tokens). Character-to-token ratio for this document: ~{chars_per_token:.1f} chars/token."
    )
    return base_prompt + metadata


def build_user_prompt(root_prompt: str, iteration: int) -> str:
    if iteration == 0:
        return (
            "You have not interacted with the REPL environment or seen your context yet. "
            "Your next action should be to explore the context and plan your approach to "
            "generate this documentation section. Do not provide a final answer yet.\n\n"
            "REMINDER: The ```repl``` code blocks you write ARE executed automatically by the "
            "pipeline. Output from print() will appear in the NEXT iteration's context. Do not "
            "say 'the REPL must be executed' or 'I cannot execute code' — write the ```repl``` "
            "blocks and they WILL run. Do not call FINAL() with placeholder text; only call "
            "FINAL() after you have real REPL output to base the answer on.\n\n"
            f'Think step-by-step on what to do using the REPL environment to answer the '
            f'original prompt: "{root_prompt}".\n\n'
            "Continue using the REPL environment, which has the `context` variable, and "
            "querying sub-LLMs by writing to ```repl``` tags, and determine your answer. "
            "Your next action:"
        )
    return (
        "The history before is your previous interactions with the REPL environment. "
        f'Think step-by-step on what to do using the REPL environment to answer the '
        f'original prompt: "{root_prompt}".\n\n'
        "Continue using the REPL environment, which has the `context` variable, and "
        "querying sub-LLMs by writing to ```repl``` tags, and determine your answer. "
        "Your next action:"
    )


# ---------------------------------------------------------------------------
# Root LLM session helpers
# ---------------------------------------------------------------------------


async def _collect_client_response(
    client: ClaudeSDKClient,
) -> Tuple[str, Optional[Dict[str, Any]]]:
    response_text = ""
    result_info: Optional[Dict[str, Any]] = None
    async for message in client.receive_response():
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    response_text += block.text
        elif isinstance(message, ResultMessage):
            result_info = {
                "usage": message.usage,
                "total_cost_usd": message.total_cost_usd,
                "duration_ms": message.duration_ms,
                "duration_api_ms": message.duration_api_ms,
                "is_error": message.is_error,
                "num_turns": message.num_turns,
                "session_id": message.session_id,
            }
            if message.is_error:
                raise RuntimeError(
                    f"Claude returned error: {message.result or response_text}"
                )
    return response_text, result_info


# ---------------------------------------------------------------------------
# Main iteration loop
# ---------------------------------------------------------------------------


async def run_rlm_section(
    repl: PipelineREPL,
    root_prompt: str,
    llm_config: Dict[str, Any],
    max_iterations: int,
    context_length: int,
    log_dir: Path,
    section_id: str,
    sub_llm_max_chars: int = 630_000,
    chars_per_token: float = 3.5,
    fallback_manager: Optional[Any] = None,
    get_root_model: Optional[Callable[[], str]] = None,
) -> Tuple[str, Dict[str, Any]]:
    """
    Drive the root LLM through up to `max_iterations` turns for a single section.

    Returns:
        (final_text, stats_dict). `final_text` is the section markdown;
        `stats_dict` contains iteration count, cost, trajectory log path, etc.
    """
    max_result_chars = 20_000

    log_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_id = str(uuid.uuid4())[:8]
    trajectory_path = log_dir / f"{section_id}_trajectory_{ts}_{run_id}.jsonl"

    def _log_entry(entry: Dict[str, Any]) -> None:
        with open(trajectory_path, "a", encoding="utf-8") as f:
            json.dump(entry, f, default=str)
            f.write("\n")

    _log_entry({
        "type": "metadata",
        "timestamp": datetime.now().isoformat(),
        "section_id": section_id,
        "root_model": llm_config.get("root_model"),
        "sub_model": llm_config.get("sub_model"),
        "max_iterations": max_iterations,
        "context_length": context_length,
        "max_output_tokens": llm_config.get("max_output_tokens"),
        "max_thinking_tokens": llm_config.get("max_thinking_tokens"),
        "root_prompt": root_prompt,
        "chars_per_token": chars_per_token,
        "sub_llm_max_chars": sub_llm_max_chars,
    })

    system_prompt = build_system_prompt(
        PIPELINE_SYSTEM_PROMPT, context_length, sub_llm_max_chars, chars_per_token
    )

    opts: Dict[str, Any] = {
        "system_prompt": system_prompt,
        "allowed_tools": [],
        "disallowed_tools": DISALLOWED_TOOLS,
    }
    effective_root_model = (
        get_root_model() if get_root_model else llm_config.get("root_model")
    )
    if effective_root_model:
        opts["model"] = effective_root_model
    if llm_config.get("max_thinking_tokens"):
        opts["max_thinking_tokens"] = llm_config["max_thinking_tokens"]
    if llm_config.get("max_output_tokens"):
        opts["env"] = {"CLAUDE_CODE_MAX_OUTPUT_TOKENS": str(llm_config["max_output_tokens"])}

    options = ClaudeAgentOptions(**opts)

    pending_results: Optional[List[Dict[str, Any]]] = None

    async with ClaudeSDKClient(options=options) as client:
        for iteration in range(max_iterations):
            iter_start = time.time()
            print(f"\n  --- Iteration {iteration + 1}/{max_iterations} ---")

            user_prompt = build_user_prompt(root_prompt, iteration)
            if pending_results:
                result_parts = []
                for er in pending_results:
                    result_parts.append(
                        f"Code executed:\n```python\n{er['code']}\n```\n\n"
                        f"REPL output:\n{er['display_result']}"
                    )
                message = "\n\n".join(result_parts) + "\n\n" + user_prompt
            else:
                message = user_prompt

            root_start = time.time()
            try:
                await client.query(message)
                response_text, result_info = await _collect_client_response(client)
                root_elapsed = time.time() - root_start
                root_cost = (result_info or {}).get("total_cost_usd") or 0
                print(
                    f"    Root LLM responded ({root_elapsed:.1f}s, "
                    f"{len(response_text):,} chars, ${root_cost:.4f})"
                )
            except Exception as e:
                root_elapsed = time.time() - root_start
                print(f"    Root LLM ERROR ({root_elapsed:.1f}s): {str(e)[:200]}")
                if (
                    fallback_manager is not None
                    and getattr(fallback_manager, "has_fallback", lambda: False)()
                    and not getattr(fallback_manager, "is_fallback_active", lambda: False)()
                ):
                    fallback_manager.trigger_fallback(e)
                _log_entry({
                    "type": "iteration",
                    "iteration": iteration + 1,
                    "timestamp": datetime.now().isoformat(),
                    "user_message_length": len(message),
                    "root_error": str(e)[:500],
                    "root_duration_s": round(root_elapsed, 2),
                    "code_blocks": [],
                    "final_answer_found": False,
                    "iteration_time_s": round(time.time() - iter_start, 2),
                })
                pending_results = None
                # Re-raise so the orchestrator can retry the whole section with
                # the (now-active) fallback root model.
                raise

            code_blocks = find_code_blocks(response_text)
            print(f"    Found {len(code_blocks)} code block(s)")

            execution_results: List[Dict[str, Any]] = []
            logged_code_blocks: List[Dict[str, Any]] = []
            for i, code in enumerate(code_blocks):
                result = repl.execute_code(code)
                exec_elapsed = result["execution_time"]
                result_str = format_execution_result(result)
                display_result = result_str
                if len(display_result) > max_result_chars:
                    display_result = (
                        display_result[:max_result_chars]
                        + f"... + [{len(display_result) - max_result_chars} chars...]"
                    )
                execution_results.append({"code": code, "display_result": display_result})
                logged_code_blocks.append({
                    "code": code,
                    "stdout": result["stdout"],
                    "stderr": result["stderr"],
                    "execution_time_s": round(exec_elapsed, 2),
                    "sub_calls": result["sub_calls"],
                    "sub_call_count": len(result["sub_calls"]),
                })
                sub_count = len(result["sub_calls"])
                sub_info = f" | {sub_count} sub-call(s)" if sub_count else ""
                preview = result_str[:200].replace("\n", " ")
                print(f"    Code block {i+1}: {exec_elapsed:.1f}s{sub_info} | {preview}...")

            final_answer = find_final_answer(response_text, repl=repl)
            final_found = final_answer is not None

            iter_elapsed = time.time() - iter_start
            _log_entry({
                "type": "iteration",
                "iteration": iteration + 1,
                "timestamp": datetime.now().isoformat(),
                "user_message": message,
                "user_message_length": len(message),
                "root_response": response_text,
                "root_response_length": len(response_text),
                "root_cost_usd": root_cost,
                "root_duration_s": round(root_elapsed, 2),
                "root_usage": (result_info or {}).get("usage"),
                "code_blocks": logged_code_blocks,
                "final_answer_found": final_found,
                "iteration_time_s": round(iter_elapsed, 2),
            })

            if final_found:
                if final_answer and final_answer.startswith("Error: Variable"):
                    print(f"    FINAL_VAR error at iteration {iteration + 1}, continuing...")
                    continue
                print(f"    FINAL answer found at iteration {iteration + 1}")
                repl_stats = repl.get_stats()
                return final_answer, {
                    "iterations": iteration + 1,
                    "root_llm_calls": iteration + 1,
                    **repl_stats,
                    "trajectory_log": str(trajectory_path),
                }

            pending_results = execution_results if execution_results else None

        # Max iterations reached — force a final answer
        print(f"\n  Max iterations ({max_iterations}) reached, forcing final answer...")
        forced_prompt = (
            "You have reached the maximum number of iterations. Provide your final answer NOW "
            "using FINAL_VAR(variable_name) or FINAL(content). Include ONLY information you have "
            "already extracted and verified from the source data. For any template sub-section you "
            "could not fill from the source data, write 'Not available in source analysis.' "
            "Do NOT invent content to fill gaps."
        )

        try:
            await client.query(forced_prompt)
            response_text, result_info = await _collect_client_response(client)
            final_answer = find_final_answer(response_text, repl=repl)

            _log_entry({
                "type": "iteration",
                "iteration": max_iterations + 1,
                "timestamp": datetime.now().isoformat(),
                "note": "forced_final",
                "user_message": forced_prompt,
                "root_response": response_text,
                "root_response_length": len(response_text),
                "root_cost_usd": (result_info or {}).get("total_cost_usd") or 0,
                "root_usage": (result_info or {}).get("usage"),
                "code_blocks": [],
                "final_answer_found": final_answer is not None,
            })

            if final_answer is not None and not (
                isinstance(final_answer, str)
                and final_answer.startswith("Error: Variable")
            ):
                repl_stats = repl.get_stats()
                return final_answer, {
                    "iterations": max_iterations + 1,
                    "root_llm_calls": max_iterations + 1,
                    **repl_stats,
                    "trajectory_log": str(trajectory_path),
                }

            cleaned_response = re.sub(
                r"^\s*FINAL(?:_VAR)?\s*\([^)]*\)\s*$", "", response_text,
                flags=re.MULTILINE,
            ).strip()
            if isinstance(final_answer, str) and final_answer.startswith("Error: Variable"):
                print("    Forced FINAL_VAR failed (variable not found); using raw response as fallback")
            repl_stats = repl.get_stats()
            return cleaned_response, {
                "iterations": max_iterations + 1,
                "root_llm_calls": max_iterations + 1,
                **repl_stats,
                "trajectory_log": str(trajectory_path),
            }

        except Exception as e:
            print(f"    Forced final answer ERROR: {str(e)[:200]}")
            _log_entry({
                "type": "iteration",
                "iteration": max_iterations + 1,
                "timestamp": datetime.now().isoformat(),
                "note": "forced_final_error",
                "root_error": str(e)[:500],
                "code_blocks": [],
                "final_answer_found": False,
            })
            repl_stats = repl.get_stats()
            return (
                f"*Section generation failed after {max_iterations} iterations.*\n\n**Error**: {e}",
                {
                    "iterations": max_iterations + 1,
                    "root_llm_calls": max_iterations + 1,
                    **repl_stats,
                    "trajectory_log": str(trajectory_path),
                },
            )
