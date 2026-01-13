"""
Chunk Topic Tagger for Section-Specific Context Selection

This module provides functionality to:
1. Tag Phase 1 chunks by topic based on content analysis
2. Filter chunks for specific Phase 2 sections
3. Build section-specific prose context

The goal is to reduce context size from ~435K tokens to ~100-150K tokens per section
by only including relevant chunks.
"""

import re
from typing import Dict, List, Any, Set, Tuple


# ============================================================================
# TOPIC DEFINITIONS
# ============================================================================

# Topics that can be assigned to chunks
TOPIC_CATEGORIES = {
    "initialization": {
        "description": "Program initialization, setup, entry points",
        "paragraph_patterns": [
            r"(?i)INIT",
            r"(?i)START",
            r"(?i)BEGIN",
            r"(?i)MAIN",
            r"(?i)0000-",
            r"(?i)000-",
            r"(?i)ENTRY",
            r"(?i)SETUP",
            r"(?i)OPEN",
        ],
        "content_keywords": [
            "initialization", "initializing", "initialize",
            "entry point", "main procedure", "program start",
            "open file", "opening", "setup",
        ],
    },
    "termination": {
        "description": "Program termination, cleanup, exit",
        "paragraph_patterns": [
            r"(?i)END",
            r"(?i)TERM",
            r"(?i)EXIT",
            r"(?i)CLOSE",
            r"(?i)FINISH",
            r"(?i)9999-",
            r"(?i)999-",
            r"(?i)STOP",
        ],
        "content_keywords": [
            "termination", "terminate", "closing",
            "exit", "cleanup", "end of program",
            "close file", "stop run",
        ],
    },
    "error_handling": {
        "description": "Error handling, exceptions, ABEND processing",
        "paragraph_patterns": [
            r"(?i)ERROR",
            r"(?i)ERR-",
            r"(?i)-ERR",
            r"(?i)ABEND",
            r"(?i)EXCEPTION",
            r"(?i)FAIL",
            r"(?i)INVALID",
        ],
        "content_keywords": [
            "error", "exception", "abend", "failure",
            "invalid", "incorrect", "problem", "issue",
            "error handling", "error message", "error code",
            "rollback", "recovery", "retry",
        ],
    },
    "validation": {
        "description": "Data validation, input checking",
        "paragraph_patterns": [
            r"(?i)VALID",
            r"(?i)CHECK",
            r"(?i)VERIFY",
            r"(?i)EDIT",
        ],
        "content_keywords": [
            "validation", "validate", "validating",
            "check", "checking", "verify", "verification",
            "edit check", "input validation", "data validation",
            "range check", "format check",
        ],
    },
    "calculation": {
        "description": "Business calculations, computations",
        "paragraph_patterns": [
            r"(?i)CALC",
            r"(?i)COMPUTE",
            r"(?i)PROCESS",
            r"(?i)TOTAL",
            r"(?i)SUM",
            r"(?i)AVERAGE",
        ],
        "content_keywords": [
            "calculation", "calculate", "computing", "compute",
            "formula", "algorithm", "arithmetic",
            "total", "sum", "average", "multiply", "divide",
            "percentage", "rate", "amount",
        ],
    },
    "data_movement": {
        "description": "Data movement, transformations, MOVE statements",
        "paragraph_patterns": [
            r"(?i)MOVE",
            r"(?i)COPY",
            r"(?i)TRANSFER",
            r"(?i)FORMAT",
            r"(?i)CONVERT",
        ],
        "content_keywords": [
            "move", "moving", "copy", "copying",
            "transfer", "transform", "convert", "conversion",
            "format", "formatting", "reformat",
            "assign", "assignment",
        ],
    },
    "file_io": {
        "description": "File operations, READ/WRITE",
        "paragraph_patterns": [
            r"(?i)READ",
            r"(?i)WRITE",
            r"(?i)FILE",
            r"(?i)RECORD",
            r"(?i)INPUT",
            r"(?i)OUTPUT",
        ],
        "content_keywords": [
            "file", "record", "read", "write",
            "input", "output", "sequential", "indexed",
            "file handling", "file processing",
            "end of file", "eof", "at end",
        ],
    },
    "database": {
        "description": "Database operations, SQL, EXEC SQL",
        "paragraph_patterns": [
            r"(?i)SQL",
            r"(?i)DB",
            r"(?i)DATABASE",
            r"(?i)CURSOR",
            r"(?i)FETCH",
            r"(?i)INSERT",
            r"(?i)UPDATE",
            r"(?i)DELETE",
            r"(?i)SELECT",
        ],
        "content_keywords": [
            "sql", "database", "cursor", "fetch",
            "select", "insert", "update", "delete",
            "exec sql", "sqlcode", "sqlstate",
            "commit", "rollback", "transaction",
            "table", "column", "row",
        ],
    },
    "reporting": {
        "description": "Report generation, printing, output formatting",
        "paragraph_patterns": [
            r"(?i)REPORT",
            r"(?i)PRINT",
            r"(?i)DISPLAY",
            r"(?i)HEADER",
            r"(?i)FOOTER",
            r"(?i)DETAIL",
            r"(?i)SUMMARY",
        ],
        "content_keywords": [
            "report", "print", "display", "output",
            "header", "footer", "detail line",
            "page", "line", "column", "format",
            "listing", "summary", "total line",
        ],
    },
    "control_flow": {
        "description": "Control flow, loops, conditions",
        "paragraph_patterns": [
            r"(?i)LOOP",
            r"(?i)ITERATE",
            r"(?i)PERFORM",
        ],
        "content_keywords": [
            "loop", "iterate", "iteration",
            "perform", "until", "varying",
            "condition", "if", "else", "evaluate",
            "when", "other", "branch",
        ],
    },
    "data_structure": {
        "description": "Data definitions, WORKING-STORAGE, copybooks",
        "paragraph_patterns": [],  # Data divisions don't have paragraphs
        "content_keywords": [
            "working-storage", "data division",
            "file section", "linkage section",
            "01 level", "05 level", "pic", "picture",
            "copybook", "copy", "filler",
            "redefines", "occurs", "table", "array",
        ],
    },
    "subprogram_call": {
        "description": "Subprogram calls, CALL statements",
        "paragraph_patterns": [
            r"(?i)CALL",
            r"(?i)INVOKE",
        ],
        "content_keywords": [
            "call", "calling", "subprogram",
            "module", "routine", "subroutine",
            "using", "returning", "parameter",
            "linkage", "interface",
        ],
    },
}


# Section to topic mapping - which topics are relevant for each Phase 2 section
SECTION_TOPIC_MAPPING: Dict[str, List[str]] = {
    "executive-summary": [
        "initialization",
        "termination",
        "calculation",
        "database",
        "file_io",
        "reporting",
    ],
    "key-responsibilities": [
        "initialization",
        "calculation",
        "validation",
        "database",
        "file_io",
        "reporting",
        "subprogram_call",
    ],
    "business-logic": [
        "calculation",
        "validation",
        "control_flow",
        "data_movement",
    ],
    "data-flow-analysis": [
        "data_movement",
        "file_io",
        "database",
        "data_structure",
        "subprogram_call",
    ],
    "error-handling": [
        "error_handling",
        "validation",
        "termination",
    ],
    "overview": [
        "initialization",
        "termination",
        "data_structure",
    ],
    "interface-analysis": [
        "file_io",
        "database",
        "subprogram_call",
        "data_structure",
    ],
}

# Default topics for sections not in the mapping
DEFAULT_TOPICS = [
    "initialization",
    "calculation",
    "validation",
    "error_handling",
]


# ============================================================================
# TAGGING FUNCTIONS
# ============================================================================

def tag_chunk(
    chunk_prose: str,
    chunk_info: Dict[str, Any],
    paragraph_names: List[str] = None
) -> Set[str]:
    """
    Tag a chunk with relevant topics based on content analysis.

    Uses both paragraph name patterns and content keyword matching.

    Args:
        chunk_prose: The prose text for this chunk (from Phase 1)
        chunk_info: Chunk metadata (start_line, end_line, etc.)
        paragraph_names: List of paragraph names in this chunk (optional)

    Returns:
        Set of topic names that apply to this chunk
    """
    topics: Set[str] = set()
    prose_lower = chunk_prose.lower()

    for topic_name, topic_def in TOPIC_CATEGORIES.items():
        # Check paragraph name patterns
        if paragraph_names:
            for para_name in paragraph_names:
                for pattern in topic_def["paragraph_patterns"]:
                    if re.search(pattern, para_name):
                        topics.add(topic_name)
                        break

        # Check content keywords
        keyword_matches = 0
        for keyword in topic_def["content_keywords"]:
            if keyword in prose_lower:
                keyword_matches += 1

        # Require at least 2 keyword matches for content-based tagging
        if keyword_matches >= 2:
            topics.add(topic_name)

    # If no topics found, assign a generic "general" topic
    if not topics:
        topics.add("general")

    return topics


def extract_paragraph_names_from_prose(prose: str) -> List[str]:
    """
    Extract paragraph names mentioned in prose.

    Looks for patterns like:
    - "paragraph XXXX-YYYY"
    - "### XXXX-YYYY"
    - block titles with paragraph names

    Args:
        prose: The prose text

    Returns:
        List of paragraph names found
    """
    paragraphs = []

    # Pattern 1: Markdown headers with paragraph names (e.g., "### 1000-INIT-PROCESS")
    header_pattern = r'###?\s+(\d{4}-[A-Z0-9-]+)'
    paragraphs.extend(re.findall(header_pattern, prose))

    # Pattern 2: "paragraph XXXX" mentions
    mention_pattern = r'paragraph\s+([A-Z0-9-]+)'
    paragraphs.extend(re.findall(mention_pattern, prose, re.IGNORECASE))

    # Pattern 3: PERFORM references
    perform_pattern = r'PERFORM\s+([A-Z0-9-]+)'
    paragraphs.extend(re.findall(perform_pattern, prose))

    return list(set(paragraphs))


# ============================================================================
# CHUNK STORAGE AND RETRIEVAL
# ============================================================================

class TaggedChunkStore:
    """
    Stores Phase 1 chunks with their topic tags for efficient retrieval in Phase 2.
    """

    def __init__(self):
        self.chunks: List[Dict[str, Any]] = []
        self._topic_index: Dict[str, List[int]] = {}  # topic -> chunk indices

    def add_chunk(
        self,
        chunk_number: int,
        prose: str,
        topics: Set[str],
        start_line: int,
        end_line: int,
        metadata: Dict[str, Any] = None
    ):
        """Add a tagged chunk to the store."""
        chunk_entry = {
            "chunk_number": chunk_number,
            "prose": prose,
            "topics": list(topics),
            "start_line": start_line,
            "end_line": end_line,
            "metadata": metadata or {},
        }

        chunk_idx = len(self.chunks)
        self.chunks.append(chunk_entry)

        # Update topic index
        for topic in topics:
            if topic not in self._topic_index:
                self._topic_index[topic] = []
            self._topic_index[topic].append(chunk_idx)

    def get_chunks_by_topics(self, topics: List[str]) -> List[Dict[str, Any]]:
        """
        Get all chunks that match any of the given topics.

        Args:
            topics: List of topic names to match

        Returns:
            List of matching chunks, sorted by chunk_number
        """
        matching_indices: Set[int] = set()

        for topic in topics:
            if topic in self._topic_index:
                matching_indices.update(self._topic_index[topic])

        # Also include "general" chunks if few matches
        if len(matching_indices) < 3 and "general" in self._topic_index:
            matching_indices.update(self._topic_index["general"])

        matching_chunks = [self.chunks[i] for i in sorted(matching_indices)]
        return matching_chunks

    def get_all_chunks(self) -> List[Dict[str, Any]]:
        """Get all chunks in order."""
        return self.chunks

    def get_prose_for_section(
        self,
        section_id: str,
        max_tokens: int = 80000  # Conservative: leaves room for system prompt (~5K) + program_map (~5K) + output (~30K)
    ) -> str:
        """
        Get filtered prose for a specific Phase 2 section.

        Uses a TOKEN BUDGET to ensure the returned prose fits within Claude's
        context window. Prioritizes chunks by topic relevance score.

        Args:
            section_id: The section ID (e.g., "executive-summary")
            max_tokens: Maximum tokens to return (default 120K, leaving ~50K for other context)

        Returns:
            Concatenated prose from relevant chunks only, within token budget
        """
        # Get topics for this section
        section_topics = set(SECTION_TOPIC_MAPPING.get(section_id, DEFAULT_TOPICS))

        # Score each chunk by topic relevance (higher = more relevant)
        scored_chunks = []
        for chunk in self.chunks:
            chunk_topics = set(chunk.get('topics', []))
            # Score = number of matching topics
            score = len(section_topics & chunk_topics)
            # Bonus for strongly relevant topics (exact section name match)
            if section_id.replace('-', '_') in chunk_topics:
                score += 5
            scored_chunks.append((score, chunk))

        # Sort by score (descending), then by chunk number (ascending for context)
        scored_chunks.sort(key=lambda x: (-x[0], x[1]['chunk_number']))

        # Build prose within token budget
        prose_parts = []
        total_chars = 0
        char_budget = max_tokens * 4  # Rough: 4 chars per token
        included_chunks = 0

        # Always include first and last chunk for context (program start/end)
        must_include = set()
        if self.chunks:
            must_include.add(self.chunks[0]['chunk_number'])
            must_include.add(self.chunks[-1]['chunk_number'])

        for score, chunk in scored_chunks:
            chunk_num = chunk['chunk_number']

            # Skip if score is 0 and not must-include
            if score == 0 and chunk_num not in must_include:
                continue

            chunk_header = f"\n## Chunk {chunk_num} (Lines {chunk['start_line']}-{chunk['end_line']})\n"
            chunk_text = chunk_header + chunk['prose']
            chunk_chars = len(chunk_text)

            # Check budget
            if total_chars + chunk_chars > char_budget:
                # If we haven't included anything yet, include truncated version
                if included_chunks == 0:
                    remaining = char_budget - total_chars
                    if remaining > 1000:
                        truncated = chunk_text[:remaining // 2] + \
                            f"\n\n... [TRUNCATED to fit {max_tokens:,} token budget] ...\n\n" + \
                            chunk_text[-remaining // 2:]
                        prose_parts.append(truncated)
                        included_chunks += 1
                break

            prose_parts.append(chunk_text)
            total_chars += chunk_chars
            included_chunks += 1

        # If no chunks matched at all, include summary from first chunks
        if not prose_parts and self.chunks:
            first_chunk = self.chunks[0]
            prose_parts.append(f"\n## Summary (Chunk 1)\n{first_chunk['prose'][:char_budget]}")

        result = "\n".join(prose_parts)

        # Final safety check - hard truncate if still over budget
        if len(result) > char_budget:
            half = char_budget // 2
            result = result[:half] + \
                f"\n\n... [HARD TRUNCATED: {len(result):,} chars → {char_budget:,} chars] ...\n\n" + \
                result[-half:]

        return result

    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about stored chunks and topics."""
        topic_counts = {topic: len(indices) for topic, indices in self._topic_index.items()}

        return {
            "total_chunks": len(self.chunks),
            "topics": topic_counts,
            "total_prose_chars": sum(len(c["prose"]) for c in self.chunks),
        }

    def to_dict(self) -> Dict[str, Any]:
        """Serialize store to dictionary for saving."""
        return {
            "chunks": self.chunks,
            "topic_index": self._topic_index,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TaggedChunkStore":
        """Deserialize store from dictionary."""
        store = cls()
        store.chunks = data.get("chunks", [])
        store._topic_index = data.get("topic_index", {})
        return store


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def estimate_section_context_size(
    store: TaggedChunkStore,
    section_id: str
) -> Tuple[int, int, float]:
    """
    Estimate the context size for a section.

    Args:
        store: Tagged chunk store
        section_id: Section ID

    Returns:
        Tuple of (filtered_chars, total_chars, reduction_percentage)
    """
    total_chars = sum(len(c["prose"]) for c in store.chunks)
    filtered_prose = store.get_prose_for_section(section_id)
    filtered_chars = len(filtered_prose)

    reduction = ((total_chars - filtered_chars) / total_chars * 100) if total_chars > 0 else 0

    return filtered_chars, total_chars, reduction


def print_section_estimates(store: TaggedChunkStore):
    """Print estimated context sizes for all sections."""
    print("\n  → Section Context Estimates:")
    print("    " + "-" * 60)

    for section_id in SECTION_TOPIC_MAPPING.keys():
        filtered, total, reduction = estimate_section_context_size(store, section_id)
        topics = SECTION_TOPIC_MAPPING.get(section_id, [])

        # Estimate tokens (rough: 4 chars per token)
        filtered_tokens = filtered // 4

        print(f"    {section_id}:")
        print(f"      Topics: {', '.join(topics[:3])}{'...' if len(topics) > 3 else ''}")
        print(f"      Size: {filtered:,} chars (~{filtered_tokens:,} tokens)")
        print(f"      Reduction: {reduction:.1f}%")

    print("    " + "-" * 60)


# ============================================================================
# MAIN TAGGING ENTRY POINT
# ============================================================================

def create_tagged_store_from_chunks(
    chunk_results: List[Tuple[int, str, Dict[str, Any]]]
) -> TaggedChunkStore:
    """
    Create a tagged chunk store from Phase 1 results.

    This is called after Phase 1 completes to build the store.

    Args:
        chunk_results: List of tuples (chunk_number, prose, chunk_info)

    Returns:
        Populated TaggedChunkStore
    """
    store = TaggedChunkStore()

    for chunk_number, prose, chunk_info in chunk_results:
        # Extract paragraph names from prose
        paragraph_names = extract_paragraph_names_from_prose(prose)

        # Tag this chunk
        topics = tag_chunk(prose, chunk_info, paragraph_names)

        # Add to store
        store.add_chunk(
            chunk_number=chunk_number,
            prose=prose,
            topics=topics,
            start_line=chunk_info.get("start_line", 0),
            end_line=chunk_info.get("end_line", 0),
            metadata=chunk_info
        )

    return store


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Test the tagging system
    sample_prose = """
    ## Chunk 1 (Lines 1-500)

    ### 0000-MAIN-PROCEDURE
    This is the main entry point of the program. It performs initialization
    by calling 1000-INIT-PROCESS.

    ### 1000-INIT-PROCESS
    This paragraph handles initialization of working storage variables
    and opens the input and output files.

    ### 2000-PROCESS-RECORDS
    The main processing loop reads records from the input file,
    performs calculations on the data, and writes to output.

    ### 8000-ERROR-HANDLER
    This error handling routine is invoked when SQLCODE is not zero.
    It displays an error message and performs ABEND processing.

    ### 9999-END-PROGRAM
    Closes all files and terminates the program with STOP RUN.
    """

    # Extract paragraphs
    paragraphs = extract_paragraph_names_from_prose(sample_prose)
    print(f"Found paragraphs: {paragraphs}")

    # Tag the chunk
    topics = tag_chunk(sample_prose, {"start_line": 1, "end_line": 500}, paragraphs)
    print(f"Topics: {topics}")

    # Create store and test retrieval
    store = TaggedChunkStore()
    store.add_chunk(1, sample_prose, topics, 1, 500)

    print(f"\nStore stats: {store.get_stats()}")

    # Test section filtering
    for section_id in ["executive-summary", "error-handling", "data-flow-analysis"]:
        prose = store.get_prose_for_section(section_id)
        print(f"\n{section_id}: {len(prose)} chars")
