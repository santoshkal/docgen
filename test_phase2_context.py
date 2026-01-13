#!/usr/bin/env python3
"""
Test script to debug Phase 2 context size issues.

This script:
1. Extracts prose from existing documentation OR creates sample prose
2. Tests chunk filtering with actual topic matching
3. Shows exactly what context size is sent to Claude
4. Helps debug the "Prompt is too long" error
"""

import json
import re
import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from chunk_topic_tagger import (
    TaggedChunkStore,
    tag_chunk,
    extract_paragraph_names_from_prose,
    SECTION_TOPIC_MAPPING,
    estimate_section_context_size,
)
from source_chunker import estimate_tokens


def extract_code_explanation_from_doc(doc_path: str) -> str:
    """Extract the Detailed Code Explanation section from a doc file."""
    with open(doc_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the detailed code explanation section
    # Pattern: ## Detailed Code Explanation ... until next ## or end
    pattern = r'(## Detailed Code Explanation.*?)(?=\n## [A-Z]|\Z)'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        return match.group(1)

    # Alternative: look for chunk sections
    pattern = r'(## Chunk \d+.*?)(?=\n## [A-Z]|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)
    if matches:
        return '\n\n'.join(matches)

    return ""


def extract_prose_from_explanation(explanation: str) -> str:
    """Remove code blocks from explanation to get prose only."""
    # Remove COBOL code blocks
    prose = re.sub(r'```cobol\n.*?```', '', explanation, flags=re.DOTALL)
    prose = re.sub(r'```\n.*?```', '', prose, flags=re.DOTALL)

    # Clean up excessive whitespace
    prose = re.sub(r'\n{3,}', '\n\n', prose)

    return prose.strip()


def split_prose_into_chunks(prose: str, chunk_size: int = 50000) -> list:
    """Split prose into chunks for testing."""
    chunks = []
    lines = prose.split('\n')

    current_chunk = []
    current_size = 0
    chunk_num = 1

    for line in lines:
        line_size = len(line)
        if current_size + line_size > chunk_size and current_chunk:
            chunk_text = '\n'.join(current_chunk)
            chunks.append({
                'chunk_number': chunk_num,
                'prose': chunk_text,
                'start_line': (chunk_num - 1) * 1000,
                'end_line': chunk_num * 1000,
            })
            chunk_num += 1
            current_chunk = [line]
            current_size = line_size
        else:
            current_chunk.append(line)
            current_size += line_size

    # Add last chunk
    if current_chunk:
        chunk_text = '\n'.join(current_chunk)
        chunks.append({
            'chunk_number': chunk_num,
            'prose': chunk_text,
            'start_line': (chunk_num - 1) * 1000,
            'end_line': chunk_num * 1000,
        })

    return chunks


def create_tagged_store_from_prose(prose: str) -> TaggedChunkStore:
    """Create a tagged store from raw prose."""
    chunks = split_prose_into_chunks(prose)
    store = TaggedChunkStore()

    for chunk in chunks:
        # Extract paragraph names
        paragraph_names = extract_paragraph_names_from_prose(chunk['prose'])

        # Tag chunk
        topics = tag_chunk(
            chunk['prose'],
            {'start_line': chunk['start_line'], 'end_line': chunk['end_line']},
            paragraph_names
        )

        store.add_chunk(
            chunk_number=chunk['chunk_number'],
            prose=chunk['prose'],
            topics=topics,
            start_line=chunk['start_line'],
            end_line=chunk['end_line']
        )

    return store


def test_section_filtering(store: TaggedChunkStore):
    """Test filtering for each section."""
    print("\n" + "=" * 70)
    print("SECTION FILTERING TEST")
    print("=" * 70)

    # Get total prose size
    total_prose = "\n\n".join(c['prose'] for c in store.chunks)
    total_chars = len(total_prose)
    total_tokens = estimate_tokens(total_prose)

    print(f"\nTotal prose: {total_chars:,} chars (~{total_tokens:,} tokens)")
    print(f"Claude limit: ~170,000 tokens for input")

    # Test each section
    print("\n" + "-" * 70)
    print(f"{'Section':<30} {'Chars':>12} {'Tokens':>12} {'Reduction':>10}")
    print("-" * 70)

    for section_id, topics in SECTION_TOPIC_MAPPING.items():
        section_prose = store.get_prose_for_section(section_id)
        section_chars = len(section_prose)
        section_tokens = estimate_tokens(section_prose)
        reduction = ((total_chars - section_chars) / total_chars * 100) if total_chars > 0 else 0

        fits = "OK" if section_tokens < 150000 else "TOO BIG"
        print(f"{section_id:<30} {section_chars:>12,} {section_tokens:>12,} {reduction:>9.0f}% {fits}")

    print("-" * 70)


def simulate_phase2_context(store: TaggedChunkStore, section_id: str = "executive-summary"):
    """Simulate what Phase 2 sends to Claude."""
    print(f"\n{'=' * 70}")
    print(f"SIMULATING PHASE 2 CONTEXT FOR: {section_id}")
    print("=" * 70)

    # Get filtered prose
    section_prose = store.get_prose_for_section(section_id)

    # Build program_map (simplified for test)
    program_map = """
## Program Map

**Paragraphs**: 100+ paragraphs (summarized)
**Data Items**: 500+ data items (summarized)
**Entry Points**: 0000-MAIN-PROCEDURE
**Key Sections**: IDENTIFICATION, ENVIRONMENT, DATA, PROCEDURE
"""

    # Build context like build_prose_based_context() does
    context = {
        "program_name": "TDAS-MINDISTCALC",
        "timestamp": "2026-01-12T12:00:00",
        "explanation_prose": section_prose,
        "program_map": program_map,
    }

    context_json = json.dumps(context)
    context_tokens = estimate_tokens(context_json)

    # Build the full prompt like generate_section_content() does
    system_prompt = f"""You are a technical documentation agent...

TEMPLATE STRUCTURE...
INSTRUCTION...

(~500 chars of system prompt)
"""

    user_prompt = f"""Generate documentation for this section using the following metadata:

{context_json}

Remember:
- Program name: {context.get('program_name', 'UNKNOWN')}
- Follow template structure exactly
"""

    full_prompt = system_prompt + "\n" + user_prompt
    full_prompt_chars = len(full_prompt)
    full_prompt_tokens = estimate_tokens(full_prompt)

    print(f"\nContext breakdown:")
    print(f"  explanation_prose: {len(section_prose):,} chars")
    print(f"  program_map: {len(program_map):,} chars")
    print(f"  context JSON: {len(context_json):,} chars (~{context_tokens:,} tokens)")
    print(f"  full prompt: {full_prompt_chars:,} chars (~{full_prompt_tokens:,} tokens)")

    print(f"\nClaude limit: ~170,000 tokens")
    print(f"Status: {'OK' if full_prompt_tokens < 170000 else 'TOO BIG - will fail!'}")

    if full_prompt_tokens > 170000:
        overage = full_prompt_tokens - 170000
        print(f"\nNEED TO REDUCE BY: ~{overage:,} tokens ({overage * 4:,} chars)")


def main():
    # Try to find existing documentation
    docs_dir = Path("../docs")
    doc_files = sorted(docs_dir.glob("TDAS-MINDISTCALC-documentation-*.md"), reverse=True)

    prose = ""

    if doc_files:
        latest_doc = doc_files[0]
        print(f"Using existing doc: {latest_doc}")

        explanation = extract_code_explanation_from_doc(str(latest_doc))
        if explanation:
            prose = extract_prose_from_explanation(explanation)
            print(f"Extracted prose: {len(prose):,} chars")
        else:
            print("No code explanation found in doc")

    # If no prose found, create sample
    if not prose or len(prose) < 10000:
        print("\nCreating sample prose for testing...")
        # Create ~700K chars of sample prose (simulating 55 chunks)
        sample_chunk = """
## Chunk {n} (Lines {start}-{end})

### 0{n}00-PROCESS-SECTION
This paragraph performs the main processing logic for this section.
It includes validation of input data, calculation of intermediate values,
and preparation for the next processing step.

**Purpose**: Process records and validate data
**Variables Used**: WS-COUNTER, WS-TOTAL, WS-STATUS
**Called Paragraphs**: 0{n}10-VALIDATE, 0{n}20-CALCULATE

### 0{n}10-VALIDATE
Validates the input record against business rules.
Checks for required fields and valid date formats.

### 0{n}20-CALCULATE
Performs distance calculations using the Haversine formula.
Updates running totals and counters.

**Technical Details**:
- Uses COMPUTE statement for arithmetic
- Error handling via 88-level conditions
- SQL queries for database lookups
"""
        prose = ""
        for i in range(1, 56):  # 55 chunks
            chunk_prose = sample_chunk.format(n=i, start=i*1000, end=(i+1)*1000-1)
            prose += chunk_prose + "\n\n"

        print(f"Created sample prose: {len(prose):,} chars")

    # Create tagged store
    print("\nCreating tagged chunk store...")
    store = create_tagged_store_from_prose(prose)

    stats = store.get_stats()
    print(f"Chunks: {stats['total_chunks']}")
    print(f"Topics: {', '.join(stats['topics'].keys())}")
    print(f"Total prose: {stats['total_prose_chars']:,} chars")

    # Test filtering
    test_section_filtering(store)

    # Simulate Phase 2 context
    for section_id in ["executive-summary", "business-logic", "error-handling"]:
        simulate_phase2_context(store, section_id)


if __name__ == "__main__":
    main()
