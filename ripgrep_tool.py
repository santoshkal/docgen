"""
RipGrep Tool for COBOL Source Code Pattern Extraction (Phase 2)

Direct subprocess calls to ripgrep binary for pattern-based extraction.
No MCP overhead - simple, fast, and reliable.

Following IMPLEMENTATION_PLAN.md Phase 2 structure.
"""

import subprocess
import shutil
import re
from dataclasses import dataclass
from typing import List, Optional, Dict


@dataclass
class SearchResult:
    """Represents a ripgrep search result"""
    file_path: str
    line_number: int
    match_text: str
    context_before: List[str] = None
    context_after: List[str] = None

    def __post_init__(self):
        if self.context_before is None:
            self.context_before = []
        if self.context_after is None:
            self.context_after = []


def check_ripgrep_installed() -> bool:
    """
    Check if ripgrep is installed.

    Returns:
        True if ripgrep (rg) is available, False otherwise
    """
    return shutil.which("rg") is not None


class RipgrepTool:
    """
    Wrapper for ripgrep command-line tool.

    Provides methods for pattern-based source code extraction.
    """

    def __init__(self, binary_path: Optional[str] = None):
        """
        Initialize RipgrepTool.

        Args:
            binary_path: Optional path to rg binary. If None, searches PATH.
        """
        if binary_path:
            self.binary = binary_path
        else:
            self.binary = shutil.which("rg")
            if not self.binary:
                self.binary = "rg"  # Fallback, will fail gracefully

    def is_available(self) -> bool:
        """
        Check if ripgrep is available and working.

        Returns:
            True if ripgrep can be executed
        """
        try:
            result = subprocess.run(
                [self.binary, "--version"],
                capture_output=True,
                timeout=5
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False

    def get_version(self) -> Optional[str]:
        """
        Get ripgrep version string.

        Returns:
            Version string or None if unavailable
        """
        try:
            result = subprocess.run(
                [self.binary, "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                # First line contains version
                return result.stdout.split('\n')[0]
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
        return None

    def search(self, pattern: str, file_path: str) -> List[SearchResult]:
        """
        Search for pattern in file.

        Args:
            pattern: Regex pattern to search for
            file_path: Path to file to search

        Returns:
            List of SearchResult objects
        """
        try:
            result = subprocess.run(
                [self.binary, "--line-number", "--no-heading", pattern, file_path],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 1:  # No matches
                return []

            # Parse output: "line_number:matched_text"
            results = []
            for line in result.stdout.split('\n'):
                if not line.strip():
                    continue

                match = re.match(r'^(\d+):(.*)$', line)
                if match:
                    line_num = int(match.group(1))
                    text = match.group(2)
                    results.append(SearchResult(
                        file_path=file_path,
                        line_number=line_num,
                        match_text=text
                    ))

            return results

        except (FileNotFoundError, subprocess.TimeoutExpired):
            return []

    def search_with_context(
        self,
        pattern: str,
        file_path: str,
        before: int = 0,
        after: int = 0
    ) -> List[SearchResult]:
        """
        Search for pattern with surrounding context lines.

        Args:
            pattern: Regex pattern to search for
            file_path: Path to file to search
            before: Number of context lines before match
            after: Number of context lines after match

        Returns:
            List of SearchResult objects with context
        """
        try:
            cmd = [self.binary, "--line-number", "--no-heading"]

            if before > 0:
                cmd.append(f"--before-context={before}")
            if after > 0:
                cmd.append(f"--after-context={after}")

            cmd.extend([pattern, file_path])

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 1:  # No matches
                return []

            # Parse output with context
            # Format: "line_num:text" for matches, "line_num-text" for context
            return self._parse_context_output(result.stdout, file_path)

        except (FileNotFoundError, subprocess.TimeoutExpired):
            return []

    def search_multiline(self, pattern: str, file_path: str) -> List[SearchResult]:
        """
        Search for multiline pattern.

        Args:
            pattern: Regex pattern (can span multiple lines)
            file_path: Path to file to search

        Returns:
            List of SearchResult objects
        """
        try:
            result = subprocess.run(
                [self.binary, "--multiline", "--line-number", "--no-heading",
                 pattern, file_path],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 1:  # No matches
                return []

            # Parse multiline output
            results = []
            for line in result.stdout.split('\n'):
                if not line.strip():
                    continue

                match = re.match(r'^(\d+):(.*)$', line)
                if match:
                    line_num = int(match.group(1))
                    text = match.group(2)
                    results.append(SearchResult(
                        file_path=file_path,
                        line_number=line_num,
                        match_text=text
                    ))

            return results

        except (FileNotFoundError, subprocess.TimeoutExpired):
            return []

    def _parse_context_output(
        self,
        output: str,
        file_path: str
    ) -> List[SearchResult]:
        """
        Parse ripgrep output with context.

        Context format:
          line_num:match_text  (actual match)
          line_num-context_text  (context line)

        Args:
            output: Raw ripgrep output
            file_path: File being searched

        Returns:
            List of SearchResult objects with context populated
        """
        results = []
        lines = output.split('\n')

        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue

            # Check if this is a match line (contains ':')
            match = re.match(r'^(\d+):(.*)$', line)
            if match:
                line_num = int(match.group(1))
                text = match.group(2)

                # Collect context before
                context_before = []
                j = i - 1
                while j >= 0:
                    ctx_line = lines[j].strip()
                    if not ctx_line:
                        break
                    ctx_match = re.match(r'^(\d+)-(.*)$', ctx_line)
                    if ctx_match:
                        context_before.insert(0, ctx_match.group(2))
                        j -= 1
                    else:
                        break

                # Collect context after
                context_after = []
                j = i + 1
                while j < len(lines):
                    ctx_line = lines[j].strip()
                    if not ctx_line:
                        break
                    ctx_match = re.match(r'^(\d+)-(.*)$', ctx_line)
                    if ctx_match:
                        context_after.append(ctx_match.group(2))
                        j += 1
                    else:
                        break

                results.append(SearchResult(
                    file_path=file_path,
                    line_number=line_num,
                    match_text=text,
                    context_before=context_before,
                    context_after=context_after
                ))

            i += 1

        return results


# ==================================================
# DAY 6 MORNING: Pattern-Specific Extractors
# ==================================================

def extract_sql_statements(file_path: str, rg_tool: RipgrepTool) -> List[str]:
    """
    Extract EXEC SQL statements from COBOL file.

    Args:
        file_path: Path to COBOL file
        rg_tool: RipgrepTool instance

    Returns:
        List of SQL statement strings
    """
    # Search for EXEC SQL blocks
    results = rg_tool.search_multiline(r"EXEC SQL.*?END-EXEC", file_path)

    statements = []
    for result in results:
        statements.append(result.match_text)

    # Also try line-by-line if multiline didn't work
    if not statements:
        results = rg_tool.search_with_context("EXEC SQL", file_path, after=10)
        for result in results:
            # Combine match and context
            full_statement = result.match_text + '\n' + '\n'.join(result.context_after)
            statements.append(full_statement)

    return statements


def extract_comments(file_path: str, rg_tool: RipgrepTool) -> List[str]:
    """
    Extract comment lines from COBOL file.

    COBOL comments start with * in column 7.

    Args:
        file_path: Path to COBOL file
        rg_tool: RipgrepTool instance

    Returns:
        List of comment strings
    """
    # Pattern for COBOL comments (asterisk in column 7)
    results = rg_tool.search(r"^\s{6}\*", file_path)

    comments = []
    for result in results:
        comments.append(result.match_text)

    return comments


def extract_error_handling_blocks(file_path: str, rg_tool: RipgrepTool) -> List[str]:
    """
    Extract error handling code blocks.

    Args:
        file_path: Path to COBOL file
        rg_tool: RipgrepTool instance

    Returns:
        List of error handling code blocks
    """
    error_patterns = [
        "ON ERROR",
        "ON EXCEPTION",
        "ON SIZE ERROR",
        "INVALID KEY",
        "AT END",
        "FILE STATUS"
    ]

    error_blocks = []
    for pattern in error_patterns:
        results = rg_tool.search_with_context(pattern, file_path, before=1, after=3)
        for result in results:
            # Combine into a block
            block_lines = result.context_before + [result.match_text] + result.context_after
            error_blocks.append('\n'.join(block_lines))

    return error_blocks


def extract_call_statements(file_path: str, rg_tool: RipgrepTool) -> List[Dict]:
    """
    Extract CALL statements from COBOL file.

    Args:
        file_path: Path to COBOL file
        rg_tool: RipgrepTool instance

    Returns:
        List of dicts with program name and context
    """
    results = rg_tool.search_with_context(r"\bCALL\s+", file_path, after=1)

    calls = []
    for result in results:
        # Try to extract program name from CALL statement
        # Pattern: CALL 'PROGRAM-NAME' or CALL "PROGRAM-NAME"
        match = re.search(r"CALL\s+['\"]([^'\"]+)['\"]", result.match_text)
        if match:
            program_name = match.group(1)
            calls.append({
                "program": program_name,
                "line": result.line_number,
                "context": result.match_text
            })
        else:
            # Fallback: just store the line
            calls.append({
                "program": "UNKNOWN",
                "line": result.line_number,
                "context": result.match_text
            })

    return calls
