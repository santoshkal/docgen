#!/usr/bin/env python3
"""
Run Phase 2 only - bypasses Phase 1 by using existing documentation.

This script:
1. Extracts prose from existing documentation
2. Creates a tagged chunk store
3. Runs Phase 2 section generation
4. Useful for debugging Phase 2 without waiting 3+ hours for Phase 1

Usage:
    python run_phase2_only.py [config.yaml] [doc_path]
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))


def extract_chunks_from_doc(doc_path: str) -> list:
    """Extract individual chunks from existing documentation."""
    with open(doc_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all chunk sections
    # Pattern: ## Chunk N/M: Lines X-Y ... until next ## Chunk
    # Note: Chunks can have internal ## sections (## Explanation, ## Coverage)
    # So we only stop at the next chunk header pattern
    chunk_pattern = r'(## Chunk (\d+)/(\d+): Lines (\d+)-(\d+).*?)(?=\n## Chunk \d+/\d+:|\Z)'
    matches = re.findall(chunk_pattern, content, re.DOTALL)

    print(f"   Debug: Found {len(matches)} chunk matches")

    chunks = []
    for full_content, chunk_num, total_chunks, start_line, end_line in matches:
        # Remove code blocks to get prose
        prose = re.sub(r'```[\w]*\n.*?```', '', full_content, flags=re.DOTALL)
        prose = re.sub(r'\n{3,}', '\n\n', prose)
        prose = prose.strip()

        if len(prose) < 500:
            print(f"   Warning: Chunk {chunk_num} has little prose ({len(prose)} chars)")

        chunks.append({
            'chunk_number': int(chunk_num),
            'prose': prose,
            'start_line': int(start_line),
            'end_line': int(end_line),
        })

    # If no chunks found with main pattern, try simpler extraction
    if not chunks:
        print("   Trying alternative extraction method...")
        # Split by chunk headers
        parts = re.split(r'\n(## Chunk \d+/\d+: Lines \d+-\d+)', content)

        chunk_num = 0
        for i in range(1, len(parts), 2):
            if i + 1 < len(parts):
                header = parts[i]
                body = parts[i + 1]

                # Parse header
                header_match = re.match(r'## Chunk (\d+)/\d+: Lines (\d+)-(\d+)', header)
                if header_match:
                    chunk_num = int(header_match.group(1))
                    start_line = int(header_match.group(2))
                    end_line = int(header_match.group(3))

                    # Find where this chunk ends (next chunk or section header)
                    end_marker = re.search(r'\n## [A-Z]', body)
                    if end_marker:
                        body = body[:end_marker.start()]

                    # Remove code blocks
                    prose = re.sub(r'```[\w]*\n.*?```', '', body, flags=re.DOTALL)
                    prose = re.sub(r'\n{3,}', '\n\n', prose).strip()

                    chunks.append({
                        'chunk_number': chunk_num,
                        'prose': prose,
                        'start_line': start_line,
                        'end_line': end_line,
                    })

    return chunks


def create_tagged_store(chunks: list):
    """Create tagged store from extracted chunks."""
    from chunk_topic_tagger import (
        TaggedChunkStore,
        tag_chunk,
        extract_paragraph_names_from_prose,
    )

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


def run_phase2(config_path: str, doc_path: str):
    """Run Phase 2 with prose extracted from existing documentation."""
    from config_loader import load_config
    from cobol_doc_agent import (
        run_phase2_sections,
        build_prose_based_context,
        assemble_final_document,
        save_to_tmp,
    )
    from chunk_topic_tagger import print_section_estimates
    import yaml

    print("=" * 70)
    print("PHASE 2 ONLY MODE")
    print("=" * 70)

    # Load config
    print(f"\n1. Loading config: {config_path}")
    config_loader = load_config(config_path)
    llm_config = config_loader.get_llm_config()
    print(f"   LLM: {llm_config.get('provider')} / {llm_config.get('model')}")

    # Extract chunks from existing doc
    print(f"\n2. Extracting chunks from: {doc_path}")
    chunks = extract_chunks_from_doc(doc_path)
    print(f"   Found {len(chunks)} chunks")

    if not chunks:
        print("   ERROR: No chunks found in document!")
        print("   Make sure the document has '## Chunk N/M:' sections")
        return

    # Create tagged store
    print(f"\n3. Creating tagged chunk store...")
    tagged_store = create_tagged_store(chunks)
    stats = tagged_store.get_stats()
    print(f"   Chunks: {stats['total_chunks']}")
    print(f"   Topics: {', '.join(sorted(stats['topics'].keys()))}")
    print(f"   Total prose: {stats['total_prose_chars']:,} chars")

    # Show section estimates
    print_section_estimates(tagged_store)

    # Combine all prose for fallback
    full_prose = "\n\n".join(c['prose'] for c in chunks)
    print(f"\n4. Full prose size: {len(full_prose):,} chars")

    # Load template
    template_path = config_loader.get_template_config().get('path', './cobol-doc-template.yaml')
    print(f"\n5. Loading template: {template_path}")
    with open(template_path, 'r') as f:
        template = yaml.safe_load(f)

    # Build minimal state
    program_name = config_loader.get_source_config().get('program_name', 'UNKNOWN')
    state = {
        'program_name': program_name,
        'template': template,
        'ctags_outline': {},
        'superbol_cfg': {},
    }

    # Run Phase 2
    print(f"\n6. Running Phase 2 sections...")
    print("=" * 70)

    section_outputs = run_phase2_sections(
        state=state,
        explanation_prose=full_prose,
        llm_config=llm_config,
        tagged_store=tagged_store
    )

    # Summary
    print("\n" + "=" * 70)
    print("PHASE 2 COMPLETE")
    print("=" * 70)
    print(f"Sections generated: {len(section_outputs)}")
    for section_id, content in section_outputs.items():
        status = "OK" if "Generation Failed" not in content else "FAILED"
        print(f"  - {section_id}: {len(content):,} chars [{status}]")

    # Save outputs
    output_dir = Path(config_loader.get_output_config().get('docs_path', '../docs'))
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%d-%m-%Y")
    output_file = output_dir / f"{program_name}-phase2-test-{timestamp}.md"

    # Build simple output
    output_parts = [f"# {program_name} - Phase 2 Test Output\n"]
    output_parts.append(f"**Generated**: {datetime.now().isoformat()}\n")
    output_parts.append("---\n")

    for section_id, content in section_outputs.items():
        output_parts.append(f"\n{content}\n")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_parts))

    print(f"\nOutput saved to: {output_file}")


def main():
    # Default paths
    config_path = "config.tdas-claude-sdk.yaml"
    doc_path = None

    # Parse arguments
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
    if len(sys.argv) > 2:
        doc_path = sys.argv[2]

    # Find latest doc if not specified
    if not doc_path:
        docs_dir = Path("../docs")
        doc_files = sorted(docs_dir.glob("TDAS-MINDISTCALC-documentation-*.md"), reverse=True)

        # Find a doc with actual content (not all failed sections)
        for df in doc_files:
            if df.stat().st_size > 100000:  # At least 100KB
                doc_path = str(df)
                break

        if not doc_path and doc_files:
            doc_path = str(doc_files[0])

    if not doc_path:
        print("ERROR: No documentation file found!")
        print("Usage: python run_phase2_only.py [config.yaml] [doc_path]")
        sys.exit(1)

    print(f"Config: {config_path}")
    print(f"Doc: {doc_path}")
    print(f"Doc size: {Path(doc_path).stat().st_size:,} bytes")

    run_phase2(config_path, doc_path)


if __name__ == "__main__":
    main()
