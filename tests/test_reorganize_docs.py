"""
Unit tests for the reorganize-docs refactoring.

Tests the new two-phase documentation generation approach:
- Phase 1: Code explanation generation + prose extraction
- Phase 2: Section generation with prose context
- Phase 3: Document assembly
"""

import pytest
import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cobol_doc_agent import (
    extract_prose_from_explanation,
    get_tmp_dir,
    save_to_tmp,
    load_from_tmp,
    cleanup_tmp,
    assemble_final_document
)


class TestExtractProseFromExplanation:
    """Tests for extract_prose_from_explanation() function."""

    def test_removes_cobol_code_blocks(self):
        """Should remove ```cobol ... ``` blocks."""
        input_md = """## Chunk 1/10

### Block 1: IDENTIFICATION DIVISION

```cobol
000014 IDENTIFICATION DIVISION.
000016 PROGRAM-ID.    TESTPROG.
```

**Purpose:**
- Declares the program's identity.

**Detailed Explanation:**
- This is the identification section.
"""
        result = extract_prose_from_explanation(input_md)

        assert "```cobol" not in result
        assert "000014 IDENTIFICATION DIVISION" not in result
        assert "## Chunk 1/10" in result
        assert "### Block 1: IDENTIFICATION DIVISION" in result
        assert "**Purpose:**" in result
        assert "Declares the program's identity" in result

    def test_removes_generic_code_blocks(self):
        """Should remove ``` ... ``` blocks without language specifier."""
        input_md = """## Section

```
some code here
```

Some prose here.
"""
        result = extract_prose_from_explanation(input_md)

        assert "```" not in result
        assert "some code here" not in result
        assert "Some prose here" in result

    def test_preserves_chunk_headers(self):
        """Should preserve ## Chunk N/M headers."""
        input_md = """## Chunk 5/47 (Lines 2174-2573)

### Block 1: DATA DIVISION

```cobol
000520 DATA DIVISION.
```

**Purpose:**
- Data definitions.
"""
        result = extract_prose_from_explanation(input_md)

        assert "## Chunk 5/47 (Lines 2174-2573)" in result
        assert "### Block 1: DATA DIVISION" in result

    def test_preserves_block_headers(self):
        """Should preserve ### Block N: headers."""
        input_md = """### Block 3: ENVIRONMENT DIVISION (Lines 408-440)

```cobol
000408 ENVIRONMENT DIVISION.
```

**Purpose:**
- Environment settings.

### Block 4: INPUT-OUTPUT SECTION

```cobol
000442 INPUT-OUTPUT SECTION.
```

**Purpose:**
- File definitions.
"""
        result = extract_prose_from_explanation(input_md)

        assert "### Block 3: ENVIRONMENT DIVISION" in result
        assert "### Block 4: INPUT-OUTPUT SECTION" in result

    def test_removes_verbatim_copy_header(self):
        """Should remove '## COBOL Code (Complete Verbatim Copy)' headers."""
        input_md = """## COBOL Code (Complete Verbatim Copy)

```cobol
000014 IDENTIFICATION DIVISION.
000016 PROGRAM-ID.    TESTPROG.
```

## Explanation by Block

Some explanation here.
"""
        result = extract_prose_from_explanation(input_md)

        assert "## COBOL Code (Complete Verbatim Copy)" not in result
        assert "## Explanation by Block" in result
        assert "Some explanation here" in result

    def test_cleans_excessive_whitespace(self):
        """Should reduce multiple newlines to double newlines."""
        input_md = """## Section 1



Some text.




More text.
"""
        result = extract_prose_from_explanation(input_md)

        # Should not have more than 2 consecutive newlines
        assert "\n\n\n" not in result
        assert "Some text" in result
        assert "More text" in result

    def test_handles_empty_input(self):
        """Should handle empty string gracefully."""
        result = extract_prose_from_explanation("")
        assert result == ""

    def test_handles_no_code_blocks(self):
        """Should return unchanged text if no code blocks present."""
        input_md = """## Section

This is just prose.

**Purpose:**
- Some purpose.
"""
        result = extract_prose_from_explanation(input_md)

        assert "## Section" in result
        assert "This is just prose" in result
        assert "**Purpose:**" in result

    def test_realistic_chunk_output(self):
        """Test with realistic chunk output format."""
        input_md = """## Chunk 1/47: Lines 1-484

## COBOL Code (Complete Verbatim Copy)

```cobol
000014 IDENTIFICATION DIVISION.
000016 PROGRAM-ID.    MINDISTCALC.
000018 AUTHOR.        "XGEN Generator".
```

## Explanation by Block

### Block 1: IDENTIFICATION DIVISION (Lines 14-24)

```cobol
000014 IDENTIFICATION DIVISION.
000016 PROGRAM-ID.    MINDISTCALC.
```

**Purpose:**
- Declares the program's identity, authorship, and metadata.

**Detailed Explanation:**
- `IDENTIFICATION DIVISION.`: Standard COBOL division.
- `PROGRAM-ID.    MINDISTCALC.`: Program name.

**Technical Details:**
- Variables used: None.
- Called by: Not applicable.

---

### Block 2: REMARKS (Lines 26-404)

```cobol
000026*REMARKS.
000028*  SYSTEM    : TDAR
```

**Purpose:**
- Documentation comments.

## Coverage Self-Assessment

**Code Blocks Generated:**
1. Block 1: IDENTIFICATION DIVISION - 5 lines
2. Block 2: REMARKS - 200 lines
"""
        result = extract_prose_from_explanation(input_md)

        # Code should be removed
        assert "000014 IDENTIFICATION DIVISION" not in result
        assert "000016 PROGRAM-ID" not in result
        assert "```cobol" not in result

        # Headers should be preserved
        assert "## Chunk 1/47: Lines 1-484" in result
        assert "## Explanation by Block" in result
        assert "### Block 1: IDENTIFICATION DIVISION" in result
        assert "### Block 2: REMARKS" in result

        # Prose should be preserved
        assert "**Purpose:**" in result
        assert "**Detailed Explanation:**" in result
        assert "**Technical Details:**" in result
        assert "Standard COBOL division" in result

        # Verbatim copy header should be removed
        assert "## COBOL Code (Complete Verbatim Copy)" not in result


class TestTmpFileHelpers:
    """Tests for tmp file helper functions."""

    def test_get_tmp_dir(self):
        """Should return correct tmp directory path."""
        result = get_tmp_dir("TESTPROG")
        assert result == Path("./tmp/TESTPROG")

    def test_save_and_load_tmp(self, tmp_path, monkeypatch):
        """Should save and load content correctly."""
        # Monkeypatch get_tmp_dir to use pytest's tmp_path
        monkeypatch.setattr(
            "cobol_doc_agent.get_tmp_dir",
            lambda name: tmp_path / name
        )

        content = "Test content for COBOL doc"
        program_name = "TESTPROG"
        filename = "test_file.txt"

        # Save
        save_path = save_to_tmp(content, program_name, filename)
        assert save_path.exists()

        # Load
        loaded = load_from_tmp(program_name, filename)
        assert loaded == content

    def test_load_nonexistent_file(self, tmp_path, monkeypatch):
        """Should return None for nonexistent file."""
        monkeypatch.setattr(
            "cobol_doc_agent.get_tmp_dir",
            lambda name: tmp_path / name
        )

        result = load_from_tmp("NONEXISTENT", "file.txt")
        assert result is None

    def test_cleanup_tmp(self, tmp_path, monkeypatch):
        """Should remove tmp directory."""
        monkeypatch.setattr(
            "cobol_doc_agent.get_tmp_dir",
            lambda name: tmp_path / name
        )

        # Create tmp directory with files
        program_name = "TESTPROG"
        save_to_tmp("content1", program_name, "file1.txt")
        save_to_tmp("content2", program_name, "file2.txt")

        tmp_dir = tmp_path / program_name
        assert tmp_dir.exists()

        # Cleanup
        cleanup_tmp(program_name)
        assert not tmp_dir.exists()


class TestAssembleFinalDocument:
    """Tests for assemble_final_document() function."""

    def test_assembles_sections_in_order(self):
        """Should assemble sections in template order."""
        template = {
            "sections": [
                {"id": "section-a", "title": "Section A"},
                {"id": "detailed-code-explanation", "title": "Code Explanation"},
                {"id": "section-b", "title": "Section B"},
            ]
        }

        code_explanation = "## Code Explanation\n\nDetailed code here."
        section_outputs = {
            "section-a": "## Section A\n\nContent A.",
            "section-b": "## Section B\n\nContent B.",
        }

        result = assemble_final_document(
            program_name="TESTPROG",
            code_explanation=code_explanation,
            section_outputs=section_outputs,
            template=template
        )

        # Check order
        pos_a = result.find("Section A")
        pos_code = result.find("Code Explanation")
        pos_b = result.find("Section B")

        assert pos_a < pos_code < pos_b

    def test_includes_document_header(self):
        """Should include program name in header."""
        template = {"sections": []}

        result = assemble_final_document(
            program_name="TESTPROG",
            code_explanation="",
            section_outputs={},
            template=template
        )

        assert "# TESTPROG - Code Documentation" in result
        assert "**Program**: TESTPROG" in result

    def test_handles_missing_sections(self):
        """Should handle sections not in section_outputs."""
        template = {
            "sections": [
                {"id": "missing-section", "title": "Missing Section"},
            ]
        }

        result = assemble_final_document(
            program_name="TESTPROG",
            code_explanation="",
            section_outputs={},
            template=template
        )

        assert "Missing Section" in result
        assert "*Section not generated*" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
