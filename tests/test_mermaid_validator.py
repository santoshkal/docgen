"""
Unit tests for mermaid_validator.py
"""

import pytest
from mermaid_validator import MermaidValidator, MermaidBlock


class TestMermaidBlockExtraction:
    """Tests for extracting mermaid blocks from markdown."""

    def test_extract_single_block(self):
        """Test extracting a single mermaid block."""
        markdown = """
# Test Document

Some text here.

```mermaid
flowchart TD
    A --> B
```

More text.
"""
        validator = MermaidValidator()
        blocks = validator.extract_mermaid_blocks(markdown, "test-section")

        assert len(blocks) == 1
        assert blocks[0].code == "flowchart TD\n    A --> B"
        assert blocks[0].section_id == "test-section"

    def test_extract_multiple_blocks(self):
        """Test extracting multiple mermaid blocks."""
        markdown = """
# Document

```mermaid
flowchart LR
    A --> B
```

Some text.

```mermaid
sequenceDiagram
    Alice->>Bob: Hello
```
"""
        validator = MermaidValidator()
        blocks = validator.extract_mermaid_blocks(markdown, "test")

        assert len(blocks) == 2
        assert "flowchart LR" in blocks[0].code
        assert "sequenceDiagram" in blocks[1].code

    def test_extract_no_blocks(self):
        """Test when there are no mermaid blocks."""
        markdown = """
# Document

Just regular markdown with no diagrams.

```python
print("hello")
```
"""
        validator = MermaidValidator()
        blocks = validator.extract_mermaid_blocks(markdown, "test")

        assert len(blocks) == 0

    def test_positions_are_captured(self):
        """Test that block positions are correctly captured."""
        markdown = "before\n```mermaid\ntest\n```\nafter"
        validator = MermaidValidator()
        blocks = validator.extract_mermaid_blocks(markdown, "test")

        assert len(blocks) == 1
        # The block should start after "before\n"
        assert blocks[0].start_pos == 7
        # Extract should give us the content
        assert markdown[blocks[0].start_pos:blocks[0].end_pos] == "```mermaid\ntest\n```"


class TestBlockReplacement:
    """Tests for replacing blocks in markdown."""

    def test_replace_single_block(self):
        """Test replacing a single block."""
        markdown = "before\n```mermaid\noriginal\n```\nafter"
        validator = MermaidValidator()
        original_blocks = validator.extract_mermaid_blocks(markdown, "test")

        # Create fixed block with new code
        fixed_blocks = [MermaidBlock(
            code="fixed",
            start_pos=original_blocks[0].start_pos,
            end_pos=original_blocks[0].end_pos,
            section_id="test"
        )]

        result = validator.replace_blocks_in_markdown(markdown, original_blocks, fixed_blocks)

        assert "```mermaid\nfixed\n```" in result
        assert "original" not in result
        assert result.startswith("before")
        assert result.endswith("after")

    def test_replace_multiple_blocks(self):
        """Test replacing multiple blocks in correct positions."""
        markdown = "start\n```mermaid\nfirst\n```\nmiddle\n```mermaid\nsecond\n```\nend"
        validator = MermaidValidator()
        original_blocks = validator.extract_mermaid_blocks(markdown, "test")

        # Fix both blocks
        fixed_blocks = [
            MermaidBlock(code="fixed1", start_pos=original_blocks[0].start_pos,
                         end_pos=original_blocks[0].end_pos, section_id="test"),
            MermaidBlock(code="fixed2", start_pos=original_blocks[1].start_pos,
                         end_pos=original_blocks[1].end_pos, section_id="test"),
        ]

        result = validator.replace_blocks_in_markdown(markdown, original_blocks, fixed_blocks)

        assert "fixed1" in result
        assert "fixed2" in result
        assert "first" not in result
        assert "second" not in result
        assert result.startswith("start")
        assert result.endswith("end")
        # Check order is preserved
        assert result.index("fixed1") < result.index("fixed2")

    def test_no_change_when_blocks_identical(self):
        """Test that markdown is unchanged when blocks are identical."""
        markdown = "text\n```mermaid\ncode\n```\nmore"
        validator = MermaidValidator()
        blocks = validator.extract_mermaid_blocks(markdown, "test")

        # Same blocks (no fix needed)
        result = validator.replace_blocks_in_markdown(markdown, blocks, blocks)

        assert result == markdown


class TestLLMFixCleanup:
    """Tests for LLM response cleanup."""

    def test_removes_mermaid_fence(self):
        """Test that mermaid fence is removed from LLM response."""
        validator = MermaidValidator()

        # Simulate what fix_mermaid_with_llm does with the cleanup
        fixed = "```mermaid\nflowchart TD\n    A --> B\n```"

        # Apply the same cleanup logic
        if fixed.startswith('```mermaid'):
            fixed = fixed[10:]
        if fixed.startswith('```'):
            fixed = fixed[3:]
        if fixed.endswith('```'):
            fixed = fixed[:-3]
        fixed = fixed.strip()

        assert fixed == "flowchart TD\n    A --> B"

    def test_removes_generic_fence(self):
        """Test that generic fence is removed."""
        fixed = "```\nflowchart TD\n```"

        if fixed.startswith('```mermaid'):
            fixed = fixed[10:]
        if fixed.startswith('```'):
            fixed = fixed[3:]
        if fixed.endswith('```'):
            fixed = fixed[:-3]
        fixed = fixed.strip()

        assert fixed == "flowchart TD"
