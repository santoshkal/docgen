"""
Multi-File Resolver for COBOL Projects (Phase 3)

Resolves copybooks and called programs across multi-file codebases.

Following IMPLEMENTATION_PLAN.md Phase 3 structure.
"""

import re
from pathlib import Path
from typing import List, Dict, Optional, Set
from dataclasses import dataclass

from ripgrep_tool import RipgrepTool


# ==================================================
# DAY 7: Copybook Resolver
# ==================================================

class CopybookResolver:
    """
    Resolves COPY statements to find and extract copybook files.

    Searches for copybooks in standard locations:
    - Same directory as source file
    - ./copybooks/
    - ./COPY/
    - ../copybooks/
    - Configured search paths
    """

    def __init__(self, codebase_root: str, search_paths: Optional[List[str]] = None):
        """
        Initialize CopybookResolver.

        Args:
            codebase_root: Root directory of COBOL codebase
            search_paths: Additional directories to search for copybooks
        """
        self.codebase_root = Path(codebase_root)
        self.search_paths = []

        # Add standard search paths
        if search_paths:
            self.search_paths.extend([Path(p) for p in search_paths])

        # Add default search paths
        self.search_paths.extend([
            self.codebase_root / "copybooks",
            self.codebase_root / "COPY",
            self.codebase_root / "copy",
            self.codebase_root.parent / "copybooks"
        ])

    def find_copybook(self, copybook_name: str) -> Optional[str]:
        """
        Find copybook file by name.

        Searches in configured search paths for files matching the copybook name.

        Args:
            copybook_name: Name of copybook (e.g., "CUSTOMER-REC")

        Returns:
            Full path to copybook file, or None if not found
        """
        # Try various extensions
        extensions = [".cpy", ".CPY", ".cbl", ".CBL", ".copy", ".COPY", ""]

        for search_path in self.search_paths:
            if not search_path.exists():
                continue

            for ext in extensions:
                # Try exact match
                candidate = search_path / f"{copybook_name}{ext}"
                if candidate.exists() and candidate.is_file():
                    return str(candidate)

                # Try case-insensitive search
                for file in search_path.glob("*"):
                    if file.stem.upper() == copybook_name.upper() and file.suffix.lower() in [e.lower() for e in extensions]:
                        return str(file)

        return None

    def extract_copybook_content(self, copybook_path: str) -> Optional[str]:
        """
        Extract content from copybook file.

        Args:
            copybook_path: Path to copybook file

        Returns:
            Copybook content as string, or None if error
        """
        try:
            with open(copybook_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except Exception:
            return None

    def parse_copy_statements(self, cobol_file_path: str) -> List[str]:
        """
        Parse COPY statements from COBOL file.

        Finds all COPY statements in the file.

        Args:
            cobol_file_path: Path to COBOL source file

        Returns:
            List of copybook names referenced
        """
        copybook_names = []

        try:
            with open(cobol_file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Pattern to match COPY statements
            # Examples:
            #   COPY CUSTMAST.
            #   COPY "CUSTOMER-REC".
            #   COPY CUSTMAST OF COPYLIB.
            patterns = [
                r'\bCOPY\s+([A-Z0-9-]+)\s*\.',
                r'\bCOPY\s+["\']([A-Z0-9-]+)["\']',
                r'\bCOPY\s+([A-Z0-9-]+)\s+OF\s+',
            ]

            for pattern in patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                copybook_names.extend(matches)

            # Remove duplicates while preserving order
            seen = set()
            unique_copybooks = []
            for name in copybook_names:
                if name not in seen:
                    seen.add(name)
                    unique_copybooks.append(name)

            return unique_copybooks

        except Exception:
            return []

    def resolve_all_copybooks(self, cobol_file_path: str) -> Dict[str, str]:
        """
        Resolve all copybooks referenced in a COBOL file.

        Args:
            cobol_file_path: Path to COBOL source file

        Returns:
            Dict mapping copybook_name -> copybook_content
        """
        copybook_names = self.parse_copy_statements(cobol_file_path)
        resolved = {}

        for name in copybook_names:
            path = self.find_copybook(name)
            if path:
                content = self.extract_copybook_content(path)
                if content:
                    resolved[name] = content

        return resolved

    def build_copybook_dependency_graph(self, cobol_file_path: str) -> Dict[str, List[str]]:
        """
        Build dependency graph of copybook relationships.

        Args:
            cobol_file_path: Path to COBOL source file

        Returns:
            Dict mapping file_path -> list of copybook names it references
        """
        graph = {}

        # Get copybooks for main file
        copybook_names = self.parse_copy_statements(cobol_file_path)
        graph[cobol_file_path] = copybook_names

        # Could recursively check copybooks for nested COPY statements
        # For now, just return the main file's dependencies

        return graph


# ==================================================
# DAY 8: Called Program Resolver
# ==================================================

@dataclass
class ProgramInfo:
    """Information about a COBOL program"""
    program_id: str
    file_path: str
    purpose: Optional[str] = None


class CalledProgramResolver:
    """
    Resolves CALL statements to find called programs.

    Searches for program files in standard locations.
    """

    def __init__(
        self,
        codebase_root: str,
        search_paths: Optional[List[str]] = None,
        rg_tool: Optional[RipgrepTool] = None
    ):
        """
        Initialize CalledProgramResolver.

        Args:
            codebase_root: Root directory of COBOL codebase
            search_paths: Additional directories to search for programs
            rg_tool: RipgrepTool instance for searching
        """
        self.codebase_root = Path(codebase_root)
        self.rg_tool = rg_tool or RipgrepTool()

        self.search_paths = []

        # Add configured search paths
        if search_paths:
            self.search_paths.extend([Path(p) for p in search_paths])

        # Add default search paths
        self.search_paths.extend([
            self.codebase_root / "programs",
            self.codebase_root / "src",
            self.codebase_root,
        ])

    def find_called_program(self, program_name: str) -> Optional[str]:
        """
        Find called program file by name.

        Args:
            program_name: Name of program (e.g., "SUBROUTINE-A")

        Returns:
            Full path to program file, or None if not found
        """
        # Try various extensions
        extensions = [".cbl", ".CBL", ".cob", ".COB", ".c74", ""]

        for search_path in self.search_paths:
            if not search_path.exists():
                continue

            for ext in extensions:
                # Try exact match
                candidate = search_path / f"{program_name}{ext}"
                if candidate.exists() and candidate.is_file():
                    return str(candidate)

                # Try case-insensitive search
                for file in search_path.glob("*"):
                    if file.stem.upper() == program_name.upper():
                        return str(file)

        return None

    def extract_program_header(self, program_path: str) -> Dict[str, str]:
        """
        Extract program header information.

        Extracts PROGRAM-ID and other identification division info.

        Args:
            program_path: Path to COBOL program file

        Returns:
            Dict with program information
        """
        header = {
            "program_id": None,
            "author": None,
            "purpose": None
        }

        try:
            with open(program_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Extract PROGRAM-ID
            prog_id_match = re.search(
                r'PROGRAM-ID\.\s+([A-Z0-9-]+)',
                content,
                re.IGNORECASE
            )
            if prog_id_match:
                header["program_id"] = prog_id_match.group(1)

            # Extract AUTHOR if present
            author_match = re.search(
                r'AUTHOR\.\s+([^\n]+)',
                content,
                re.IGNORECASE
            )
            if author_match:
                header["author"] = author_match.group(1).strip()

            # Try to extract purpose from comments
            purpose_patterns = [
                r'\*\s*PURPOSE:\s*([^\n]+)',
                r'\*\s*DESCRIPTION:\s*([^\n]+)',
            ]
            for pattern in purpose_patterns:
                purpose_match = re.search(pattern, content, re.IGNORECASE)
                if purpose_match:
                    header["purpose"] = purpose_match.group(1).strip()
                    break

        except Exception:
            pass

        return header

    def parse_call_statements(self, cobol_file_path: str) -> List[str]:
        """
        Parse CALL statements from COBOL file.

        Args:
            cobol_file_path: Path to COBOL source file

        Returns:
            List of program names called
        """
        program_names = []

        try:
            with open(cobol_file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Pattern to match CALL statements
            # Examples:
            #   CALL 'PROGRAM-NAME'
            #   CALL "PROGRAM-NAME"
            #   CALL WS-PROGRAM-NAME
            patterns = [
                r'\bCALL\s+["\']([A-Z0-9-]+)["\']',
            ]

            for pattern in patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                program_names.extend(matches)

            # Remove duplicates
            return list(set(program_names))

        except Exception:
            return []

    def resolve_all_calls(self, cobol_file_path: str) -> Dict[str, Dict]:
        """
        Resolve all CALL statements in a file.

        Args:
            cobol_file_path: Path to COBOL source file

        Returns:
            Dict mapping program_name -> {path, header_info}
        """
        program_names = self.parse_call_statements(cobol_file_path)
        resolved = {}

        for name in program_names:
            path = self.find_called_program(name)
            if path:
                header = self.extract_program_header(path)
                resolved[name] = {
                    "path": path,
                    "program_id": header.get("program_id"),
                    "author": header.get("author"),
                    "purpose": header.get("purpose")
                }
            else:
                resolved[name] = {
                    "path": None,
                    "program_id": name,
                    "error": "Program file not found"
                }

        return resolved

    def build_call_hierarchy(
        self,
        cobol_file_path: str,
        depth: int = 1,
        visited: Optional[Set[str]] = None
    ) -> Dict:
        """
        Build call hierarchy tree.

        Args:
            cobol_file_path: Path to COBOL source file
            depth: Maximum depth to traverse
            visited: Set of already visited files (to avoid cycles)

        Returns:
            Dict representing call hierarchy
        """
        if visited is None:
            visited = set()

        # Avoid cycles
        if cobol_file_path in visited:
            return {"program": cobol_file_path, "calls": [], "error": "Circular reference"}

        visited.add(cobol_file_path)

        # Extract program name
        header = self.extract_program_header(cobol_file_path)
        program_name = header.get("program_id", Path(cobol_file_path).stem)

        hierarchy = {
            "program": program_name,
            "path": cobol_file_path,
            "calls": []
        }

        if depth > 0:
            # Get called programs
            called_programs = self.resolve_all_calls(cobol_file_path)

            for prog_name, info in called_programs.items():
                if info.get("path"):
                    # Recursively build hierarchy for called program
                    sub_hierarchy = self.build_call_hierarchy(
                        info["path"],
                        depth - 1,
                        visited.copy()  # Pass copy to allow different paths
                    )
                    hierarchy["calls"].append(sub_hierarchy)
                else:
                    # Program not found
                    hierarchy["calls"].append({
                        "program": prog_name,
                        "path": None,
                        "error": "Not found"
                    })

        return hierarchy
