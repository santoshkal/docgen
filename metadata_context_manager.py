"""
Metadata Context Manager for Large COBOL Projects

Handles intelligent metadata management for LLM context windows when generating
Project Overview documents. Designed for GPT-4.1 with 1M token context.

STRATEGIES FOR LARGE PROJECTS:
==============================

1. SINGLE-REQUEST STRATEGY (< 500K tokens of metadata)
   - Load all metadata into a single request
   - Most accurate results - LLM sees complete picture
   - Best for: Small to medium projects (< 100 programs)

2. HIERARCHICAL SUMMARIZATION (500K - 2M tokens)
   - First pass: Summarize each metadata file independently
   - Second pass: Combine summaries for final overview
   - Maintains accuracy while fitting context
   - Best for: Large projects (100-500 programs)

3. CHUNKED ANALYSIS (> 2M tokens)
   - Chunk metadata by logical groups (directories, call clusters)
   - Generate partial overviews for each chunk
   - Final synthesis pass combines partial overviews
   - Best for: Very large projects (500+ programs)

4. HYBRID APPROACH
   - Critical metadata (call graph, entry points) always included
   - Supporting metadata (file list, cross-refs) summarized or sampled
   - Dynamically adjusts based on available context budget

TOKEN BUDGET ALLOCATION (for 1M context):
=========================================
- System prompt + template: ~2K tokens (reserved)
- Response buffer: ~50K tokens (reserved for output)
- Available for metadata: ~948K tokens

METADATA PRIORITY (when context is limited):
============================================
1. Call graph (inter-program dependencies) - CRITICAL
2. Project relationships summary - HIGH
3. File inventory (programs + copybooks) - HIGH
4. Per-program details - MEDIUM (can be summarized)
5. Cross-references - LOW (can be omitted)
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

# Import tiktoken for accurate token counting
try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False
    print("⚠ Warning: tiktoken not installed. Token counts will be estimated.")


class ContextStrategy(Enum):
    """Strategy for handling metadata in context."""
    SINGLE_REQUEST = "single_request"      # All metadata in one request
    HIERARCHICAL = "hierarchical"          # Summarize then combine
    CHUNKED = "chunked"                    # Process in logical chunks
    HYBRID = "hybrid"                      # Priority-based selection


@dataclass
class TokenBudget:
    """Token budget allocation for Project Overview generation."""
    total_context: int = 1_000_000         # GPT-4.1 context window
    system_prompt_reserve: int = 2_000     # Reserved for system prompt
    template_reserve: int = 3_000          # Reserved for template instructions
    response_reserve: int = 50_000         # Reserved for LLM response
    safety_margin: int = 5_000             # Safety buffer

    @property
    def available_for_metadata(self) -> int:
        """Calculate available tokens for metadata."""
        return (self.total_context -
                self.system_prompt_reserve -
                self.template_reserve -
                self.response_reserve -
                self.safety_margin)


@dataclass
class MetadataFile:
    """Represents a metadata file with its token count."""
    name: str
    path: str
    content: Dict[str, Any] = field(default_factory=dict)
    raw_content: str = ""
    token_count: int = 0
    priority: int = 1  # 1=highest, 5=lowest
    is_loaded: bool = False
    is_summarized: bool = False
    summary: str = ""
    summary_tokens: int = 0


class MetadataContextManager:
    """
    Manages metadata loading and context allocation for Project Overview generation.

    Usage:
        manager = MetadataContextManager(model="gpt-4")
        manager.add_metadata_file("call_graph", path, priority=1)
        manager.add_metadata_file("relationships", path, priority=2)

        strategy, context = manager.prepare_context()
        # Use context in LLM request
    """

    def __init__(
        self,
        model: str = "gpt-4",
        budget: Optional[TokenBudget] = None,
        verbose: bool = True
    ):
        """
        Initialize the context manager.

        Args:
            model: Model name for tiktoken encoding
            budget: Token budget allocation (defaults to GPT-4.1 1M context)
            verbose: Print detailed information
        """
        self.model = model
        self.budget = budget or TokenBudget()
        self.verbose = verbose
        self.metadata_files: Dict[str, MetadataFile] = {}
        self._encoder = self._get_encoder()

    def _get_encoder(self):
        """Get tiktoken encoder for the model."""
        if TIKTOKEN_AVAILABLE:
            try:
                return tiktoken.encoding_for_model(self.model)
            except Exception:
                # Fallback to cl100k_base for newer models
                return tiktoken.get_encoding("cl100k_base")
        return None

    def count_tokens(self, text: str) -> int:
        """
        Count exact tokens using tiktoken.

        Args:
            text: Text to count tokens for

        Returns:
            Exact token count (or estimate if tiktoken unavailable)
        """
        if self._encoder:
            return len(self._encoder.encode(text))
        else:
            # Fallback: ~4 chars per token for English/code
            return len(text) // 4

    def add_metadata_file(
        self,
        name: str,
        path: str,
        priority: int = 3
    ) -> bool:
        """
        Add a metadata file to be managed.

        Args:
            name: Identifier for the metadata file
            path: File path
            priority: Loading priority (1=highest, 5=lowest)

        Returns:
            True if file was added successfully
        """
        file_path = Path(path)
        if not file_path.exists():
            if self.verbose:
                print(f"⚠ Metadata file not found: {path}")
            return False

        self.metadata_files[name] = MetadataFile(
            name=name,
            path=path,
            priority=priority
        )
        return True

    def load_all_metadata(self) -> Dict[str, int]:
        """
        Load all metadata files and count their tokens.

        Returns:
            Dictionary of {name: token_count}
        """
        token_counts = {}

        for name, meta_file in self.metadata_files.items():
            try:
                with open(meta_file.path, 'r') as f:
                    meta_file.raw_content = f.read()
                    meta_file.content = json.loads(meta_file.raw_content)

                meta_file.token_count = self.count_tokens(meta_file.raw_content)
                meta_file.is_loaded = True
                token_counts[name] = meta_file.token_count

                if self.verbose:
                    print(f"✓ Loaded {name}: {meta_file.token_count:,} tokens")

            except Exception as e:
                if self.verbose:
                    print(f"✗ Failed to load {name}: {e}")
                token_counts[name] = 0

        return token_counts

    def get_total_tokens(self) -> int:
        """Get total tokens across all loaded metadata."""
        return sum(mf.token_count for mf in self.metadata_files.values() if mf.is_loaded)

    def determine_strategy(self) -> ContextStrategy:
        """
        Determine the best strategy based on metadata size.

        Returns:
            Recommended ContextStrategy
        """
        total_tokens = self.get_total_tokens()
        available = self.budget.available_for_metadata

        if self.verbose:
            print(f"\n📊 Context Analysis:")
            print(f"   Total metadata: {total_tokens:,} tokens")
            print(f"   Available budget: {available:,} tokens")
            print(f"   Usage: {total_tokens/available*100:.1f}%")

        if total_tokens <= available * 0.5:  # < 50% of budget
            strategy = ContextStrategy.SINGLE_REQUEST
        elif total_tokens <= available:  # 50-100% of budget
            strategy = ContextStrategy.HYBRID
        elif total_tokens <= available * 2:  # 100-200% of budget
            strategy = ContextStrategy.HIERARCHICAL
        else:  # > 200% of budget
            strategy = ContextStrategy.CHUNKED

        if self.verbose:
            print(f"   Recommended strategy: {strategy.value}")

        return strategy

    def prepare_context_single_request(self) -> str:
        """
        Prepare context for single-request strategy.
        All metadata included in full.

        Returns:
            Combined metadata context string
        """
        context_parts = []

        # Sort by priority
        sorted_files = sorted(
            self.metadata_files.values(),
            key=lambda x: x.priority
        )

        for meta_file in sorted_files:
            if meta_file.is_loaded:
                context_parts.append(f"\n{'='*60}")
                context_parts.append(f"METADATA: {meta_file.name.upper()}")
                context_parts.append(f"{'='*60}")
                context_parts.append(json.dumps(meta_file.content, indent=2))

        return "\n".join(context_parts)

    def prepare_context_hybrid(self) -> str:
        """
        Prepare context using hybrid strategy.
        High-priority metadata in full, low-priority summarized.

        Returns:
            Combined metadata context string
        """
        context_parts = []
        remaining_budget = self.budget.available_for_metadata

        # Sort by priority
        sorted_files = sorted(
            self.metadata_files.values(),
            key=lambda x: x.priority
        )

        for meta_file in sorted_files:
            if not meta_file.is_loaded:
                continue

            if meta_file.token_count <= remaining_budget:
                # Include in full
                context_parts.append(f"\n{'='*60}")
                context_parts.append(f"METADATA: {meta_file.name.upper()} (FULL)")
                context_parts.append(f"{'='*60}")
                context_parts.append(json.dumps(meta_file.content, indent=2))
                remaining_budget -= meta_file.token_count
            else:
                # Need to summarize or truncate
                context_parts.append(f"\n{'='*60}")
                context_parts.append(f"METADATA: {meta_file.name.upper()} (TRUNCATED)")
                context_parts.append(f"{'='*60}")

                # Intelligent truncation based on content type
                truncated = self._truncate_metadata(meta_file, remaining_budget)
                context_parts.append(truncated)
                remaining_budget = 0

        return "\n".join(context_parts)

    def _truncate_metadata(self, meta_file: MetadataFile, max_tokens: int) -> str:
        """
        Intelligently truncate metadata to fit token budget.

        Args:
            meta_file: Metadata file to truncate
            max_tokens: Maximum tokens allowed

        Returns:
            Truncated JSON string
        """
        content = meta_file.content

        # Strategy depends on metadata type
        if meta_file.name == "call_graph":
            # Keep structure but limit entries per program
            return self._truncate_call_graph(content, max_tokens)
        elif meta_file.name == "file_list":
            # Keep file list but remove details
            return self._truncate_file_list(content, max_tokens)
        else:
            # Generic truncation - keep first N characters
            json_str = json.dumps(content, indent=2)
            # Estimate chars for tokens (4 chars/token)
            max_chars = max_tokens * 4
            if len(json_str) > max_chars:
                return json_str[:max_chars] + "\n... [TRUNCATED]"
            return json_str

    def _truncate_call_graph(self, content: Dict, max_tokens: int) -> str:
        """Truncate call graph keeping most connected programs."""
        if not isinstance(content, dict):
            return json.dumps(content, indent=2)

        # Count calls per program
        call_counts = {prog: len(calls) for prog, calls in content.items()}

        # Sort by call count (most calls first)
        sorted_progs = sorted(call_counts.keys(), key=lambda x: -call_counts[x])

        # Include programs until budget exhausted
        truncated = {}
        current_tokens = 0

        for prog in sorted_progs:
            prog_json = json.dumps({prog: content[prog]}, indent=2)
            prog_tokens = self.count_tokens(prog_json)

            if current_tokens + prog_tokens <= max_tokens:
                truncated[prog] = content[prog]
                current_tokens += prog_tokens
            else:
                break

        result = json.dumps(truncated, indent=2)
        omitted = len(content) - len(truncated)
        if omitted > 0:
            result += f"\n\n[{omitted} programs omitted due to context limits]"

        return result

    def _truncate_file_list(self, content: Dict, max_tokens: int) -> str:
        """Truncate file list keeping essential info."""
        if not isinstance(content, dict) or 'files' not in content:
            return json.dumps(content, indent=2)

        # Simplify file entries
        simplified = {
            'total_files': content.get('total_files', len(content.get('files', []))),
            'files': []
        }

        for f in content.get('files', []):
            simplified['files'].append({
                'name': f.get('name', ''),
                'path': f.get('path', ''),
                'extension': f.get('extension', '')
            })

        result = json.dumps(simplified, indent=2)

        # Check if still too large
        if self.count_tokens(result) > max_tokens:
            # Just list file names
            files = [f.get('name', '') for f in content.get('files', [])]
            return json.dumps({
                'total_files': len(files),
                'file_names': files
            }, indent=2)

        return result

    def prepare_context(self) -> Tuple[ContextStrategy, str, Dict[str, Any]]:
        """
        Prepare the optimal context for LLM request.

        Returns:
            Tuple of (strategy, context_string, metadata_stats)
        """
        # Load all metadata
        self.load_all_metadata()

        # Determine strategy
        strategy = self.determine_strategy()

        # Prepare context based on strategy
        if strategy == ContextStrategy.SINGLE_REQUEST:
            context = self.prepare_context_single_request()
        elif strategy in (ContextStrategy.HYBRID, ContextStrategy.HIERARCHICAL):
            context = self.prepare_context_hybrid()
        else:
            # For CHUNKED strategy, return first chunk
            # (full chunked processing requires multiple LLM calls)
            context = self.prepare_context_hybrid()

        # Calculate final stats
        context_tokens = self.count_tokens(context)
        stats = {
            'strategy': strategy.value,
            'total_metadata_tokens': self.get_total_tokens(),
            'context_tokens': context_tokens,
            'budget_available': self.budget.available_for_metadata,
            'budget_used_percent': context_tokens / self.budget.available_for_metadata * 100,
            'files_included': len([mf for mf in self.metadata_files.values() if mf.is_loaded])
        }

        if self.verbose:
            print(f"\n📦 Context Prepared:")
            print(f"   Strategy: {strategy.value}")
            print(f"   Context tokens: {context_tokens:,}")
            print(f"   Budget usage: {stats['budget_used_percent']:.1f}%")

        return strategy, context, stats


def analyze_project_metadata(
    call_graph_path: str,
    relationships_path: str,
    file_list_path: str,
    model: str = "gpt-4"
) -> Dict[str, Any]:
    """
    Analyze project metadata and recommend context strategy.

    Args:
        call_graph_path: Path to call_graph.json
        relationships_path: Path to project-relationships.json
        file_list_path: Path to file_list.json
        model: Model name for token counting

    Returns:
        Analysis results with recommended strategy
    """
    manager = MetadataContextManager(model=model)

    # Add metadata files with priorities
    manager.add_metadata_file("call_graph", call_graph_path, priority=1)
    manager.add_metadata_file("relationships", relationships_path, priority=2)
    manager.add_metadata_file("file_list", file_list_path, priority=3)

    # Load and analyze
    token_counts = manager.load_all_metadata()
    strategy = manager.determine_strategy()

    return {
        'token_counts': token_counts,
        'total_tokens': manager.get_total_tokens(),
        'recommended_strategy': strategy.value,
        'budget': {
            'total_context': manager.budget.total_context,
            'available_for_metadata': manager.budget.available_for_metadata
        }
    }


# Example usage and testing
if __name__ == "__main__":
    print("="*70)
    print("METADATA CONTEXT MANAGER - TEST")
    print("="*70)

    # Test with sample paths
    result = analyze_project_metadata(
        call_graph_path="/home/santosh/cobol-work/metadata/superbol/cfg/call_graph.json",
        relationships_path="/home/santosh/cobol-work/metadata/gnucobol/project-relationships.json",
        file_list_path="/home/santosh/cobol-work/metadata/file_list.json"
    )

    print("\n📋 Analysis Results:")
    print(json.dumps(result, indent=2))
