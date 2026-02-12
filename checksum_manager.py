"""
Checksum Manager for COBOL Documentation Agent

Handles checksum calculation, storage, and comparison for:
- Source COBOL files
- Generated metadata files

Used to intelligently determine when to regenerate metadata.
"""

import hashlib
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime


class ChecksumManager:
    """
    Manages checksums for source files and metadata files
    """

    def __init__(self, algorithm: str = "sha256"):
        """
        Initialize checksum manager

        Args:
            algorithm: Hash algorithm to use (sha256, md5, sha1)
        """
        self.algorithm = algorithm
        self.hash_func = getattr(hashlib, algorithm)

    def calculate_file_checksum(self, file_path: Path) -> str:
        """
        Calculate checksum of a single file

        Args:
            file_path: Path to file

        Returns:
            Hexadecimal checksum string
        """
        hash_obj = self.hash_func()

        try:
            with open(file_path, 'rb') as f:
                # Read file in chunks for memory efficiency
                for chunk in iter(lambda: f.read(8192), b''):
                    hash_obj.update(chunk)

            return hash_obj.hexdigest()

        except Exception as e:
            print(f"⚠ Warning: Could not calculate checksum for {file_path}: {e}")
            return ""

    def calculate_source_checksums(self, source_files: List[Path], workspace_path: Path) -> Dict[str, Any]:
        """
        Calculate checksums for all source files with relative paths

        Args:
            source_files: List of paths to source files
            workspace_path: Root workspace path (for calculating relative paths)

        Returns:
            Dictionary with metadata and file checksums (keys are relative paths)
        """
        print(f"\n{'='*70}")
        print("Calculating Source File Checksums")
        print(f"{'='*70}")

        workspace_path = Path(workspace_path)
        checksums = {}
        file_details = {}

        for file_path in sorted(source_files):
            # Calculate relative path from workspace root
            try:
                relative_path = file_path.relative_to(workspace_path)
            except ValueError:
                # If file is outside workspace, use absolute path
                relative_path = file_path

            # Use forward slashes for cross-platform compatibility
            path_key = str(relative_path).replace('\\', '/')

            checksum = self.calculate_file_checksum(file_path)

            if checksum:
                checksums[path_key] = checksum
                file_details[path_key] = {
                    "size_bytes": file_path.stat().st_size,
                    "modified_at": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
                }
                print(f"  ✓ {path_key}: {checksum[:16]}...")

        result = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "workspace_path": str(workspace_path),
                "algorithm": self.algorithm,
                "file_count": len(checksums),
                "agent_version": "1.0.0"
            },
            "source_files": checksums,
            "file_details": file_details
        }

        print(f"\n✓ Calculated checksums for {len(checksums)} files")
        return result

    def calculate_metadata_checksums(self, metadata_dir: Path) -> Dict[str, Any]:
        """
        Calculate checksums for all generated metadata files

        Args:
            metadata_dir: Base directory containing metadata

        Returns:
            Dictionary with metadata checksums organized by tool
        """
        print(f"\n{'='*70}")
        print("Calculating Metadata File Checksums")
        print(f"{'='*70}")

        metadata_dir = Path(metadata_dir)

        # Define metadata structure
        tools = {
            "ctags": metadata_dir / "ctags",
            "gnucobol": metadata_dir / "gnucobol",
            "superbol": metadata_dir / "superbol"
        }

        result = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "algorithm": self.algorithm,
            },
            "ctags": {},
            "gnucobol": {},
            "superbol": {},
            "statistics": {
                "total_files": 0,
                "total_size_bytes": 0
            }
        }

        total_files = 0
        total_size = 0

        # Calculate checksums for each tool's metadata
        for tool_name, tool_dir in tools.items():
            if not tool_dir.exists():
                print(f"⚠ Warning: {tool_name} directory not found: {tool_dir}")
                continue

            print(f"\n{tool_name.upper()}:")

            # Find all JSON files (and .tags files for ctags)
            patterns = ["*.json", "*.tags"] if tool_name == "ctags" else ["*.json"]

            for pattern in patterns:
                for file_path in sorted(tool_dir.rglob(pattern)):
                    relative_path = file_path.relative_to(tool_dir)
                    checksum = self.calculate_file_checksum(file_path)

                    if checksum:
                        # Use forward slashes for consistency across platforms
                        key = str(relative_path).replace('\\', '/')
                        result[tool_name][key] = checksum

                        total_files += 1
                        total_size += file_path.stat().st_size

                        print(f"  ✓ {key}: {checksum[:16]}...")

        result["statistics"]["total_files"] = total_files
        result["statistics"]["total_size_bytes"] = total_size

        print(f"\n✓ Calculated checksums for {total_files} metadata files")
        return result

    def save_checksums(self, checksums: Dict[str, Any], output_path: Path) -> bool:
        """
        Save checksums to YAML file

        Args:
            checksums: Checksum dictionary
            output_path: Path to save YAML file

        Returns:
            True if successful, False otherwise
        """
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, 'w') as f:
                yaml.dump(checksums, f, default_flow_style=False, sort_keys=False)

            print(f"✓ Checksums saved to: {output_path}")
            return True

        except Exception as e:
            print(f"✗ Error saving checksums to {output_path}: {e}")
            return False

    def load_checksums(self, checksum_path: Path) -> Optional[Dict[str, Any]]:
        """
        Load checksums from YAML file

        Args:
            checksum_path: Path to checksum YAML file

        Returns:
            Checksum dictionary if file exists, None otherwise
        """
        if not checksum_path.exists():
            return None

        try:
            with open(checksum_path, 'r') as f:
                checksums = yaml.safe_load(f)

            return checksums

        except Exception as e:
            print(f"⚠ Warning: Could not load checksums from {checksum_path}: {e}")
            return None

    def compare_checksums(
        self,
        old_checksums: Optional[Dict[str, Any]],
        new_checksums: Dict[str, Any],
        checksum_type: str = "source"
    ) -> bool:
        """
        Compare two checksum dictionaries

        Args:
            old_checksums: Previous checksums (or None if first run)
            new_checksums: Current checksums
            checksum_type: Type of checksums ("source" or "metadata")

        Returns:
            True if checksums match, False if different
        """
        if old_checksums is None:
            print(f"ℹ No previous {checksum_type} checksums found (first run)")
            return False

        # Get the file checksums (skip metadata)
        old_files = old_checksums.get("source_files" if checksum_type == "source" else checksum_type, {})
        new_files = new_checksums.get("source_files" if checksum_type == "source" else checksum_type, {})

        # For metadata, we need to check all three tools
        if checksum_type == "metadata":
            old_files = {
                "ctags": old_checksums.get("ctags", {}),
                "gnucobol": old_checksums.get("gnucobol", {}),
                "superbol": old_checksums.get("superbol", {})
            }
            new_files = {
                "ctags": new_checksums.get("ctags", {}),
                "gnucobol": new_checksums.get("gnucobol", {}),
                "superbol": new_checksums.get("superbol", {})
            }

        # Compare
        if old_files == new_files:
            print(f"✓ {checksum_type.capitalize()} checksums match - no changes detected")
            return True
        else:
            print(f"⚠ {checksum_type.capitalize()} checksums differ - changes detected")

            # Show what changed (for source files)
            if checksum_type == "source":
                self._show_source_differences(old_files, new_files)

            return False

    def _show_source_differences(self, old_files: Dict, new_files: Dict):
        """Show which source files changed"""
        old_set = set(old_files.keys())
        new_set = set(new_files.keys())

        added = new_set - old_set
        removed = old_set - new_set
        common = old_set & new_set

        modified = [f for f in common if old_files[f] != new_files[f]]

        if added:
            print(f"  + Added files: {', '.join(sorted(added))}")
        if removed:
            print(f"  - Removed files: {', '.join(sorted(removed))}")
        if modified:
            print(f"  ~ Modified files: {', '.join(sorted(modified))}")


def get_source_files(
    workspace_path: Path,
    patterns: List[str] = None,
    filter_config: Optional[Dict[str, Any]] = None
) -> List[Path]:
    """
    Recursively get list of all COBOL source files in workspace with optional filtering.

    Args:
        workspace_path: Path to workspace directory (searches recursively)
        patterns: List of file patterns to match (e.g., ["*.COB", "*.cbl"])
                  Defaults to common COBOL extensions if not provided
        filter_config: Optional filtering configuration dict with:
            - extensions_include: List of extensions to include (e.g., ['.c74', '.XMOD'])
            - extensions_exclude: List of extensions to exclude (e.g., ['.xgn'])
            - exclude_files: List of file patterns to exclude (e.g., ['TEST*'])
            - include_files: List of file patterns to include (overrides all)

    Returns:
        List of COBOL file paths (sorted, no duplicates)
    """
    import fnmatch

    workspace = Path(workspace_path)
    filter_config = filter_config or {}

    # Extract filter settings
    extensions_include = filter_config.get('extensions_include', [])
    extensions_exclude = filter_config.get('extensions_exclude', [])
    exclude_files = filter_config.get('exclude_files', [])
    include_files = filter_config.get('include_files', [])

    # Normalize extensions (ensure they start with '.')
    extensions_include = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions_include]
    extensions_exclude = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions_exclude]

    # ─────────────────────────────────────────────────────────────────
    # PRIORITY 1: If include_files specified, ONLY match those patterns
    # ─────────────────────────────────────────────────────────────────
    if include_files:
        files = []
        for pattern in include_files:
            # Support both exact names and glob patterns
            matched = list(workspace.rglob(pattern))
            files.extend(matched)
        files = sorted(set(files))
        print(f"  → File filter: include_files matched {len(files)} files")
        return files

    # ─────────────────────────────────────────────────────────────────
    # PRIORITY 2: Determine which extensions to search for
    # ─────────────────────────────────────────────────────────────────
    # Default COBOL file patterns covering common naming conventions
    default_extensions = [
        '.COB', '.cob',           # Standard COBOL
        '.cbl', '.CBL',           # COBOL
        '.COBOL', '.cobol',       # Full name
        '.c74', '.C74',           # COBOL-74
        '.XMOD', '.xmod',         # XGEN modules (human-authored)
        '.XLIB', '.xlib',         # XGEN libraries (human-authored)
        '.xgn', '.XGN',           # XGEN specification files
    ]

    if extensions_include:
        # Use ONLY the specified extensions
        # Add both original and case variants
        search_extensions = []
        for ext in extensions_include:
            search_extensions.append(ext)
            search_extensions.append(ext.lower())
            search_extensions.append(ext.upper())
        search_extensions = list(set(search_extensions))
        print(f"  → File filter: including only extensions {extensions_include}")
    elif extensions_exclude:
        # Use all defaults EXCEPT excluded ones
        exclude_lower = [ext.lower() for ext in extensions_exclude]
        search_extensions = [ext for ext in default_extensions if ext.lower() not in exclude_lower]
        print(f"  → File filter: excluding extensions {extensions_exclude}")
    else:
        # Use patterns if provided, otherwise defaults
        if patterns:
            search_extensions = None  # Will use patterns directly
        else:
            search_extensions = default_extensions

    # Build patterns from extensions
    if search_extensions is not None:
        patterns = [f"*{ext}" for ext in search_extensions]

    # ─────────────────────────────────────────────────────────────────
    # Search for files matching patterns
    # ─────────────────────────────────────────────────────────────────
    files = []
    for pattern in patterns:
        files.extend(workspace.rglob(pattern))

    # Remove duplicates
    files = list(set(files))

    # ─────────────────────────────────────────────────────────────────
    # PRIORITY 3: Apply exclude_files patterns
    # ─────────────────────────────────────────────────────────────────
    if exclude_files:
        original_count = len(files)
        filtered_files = []
        for f in files:
            excluded = False
            for pattern in exclude_files:
                if fnmatch.fnmatch(f.name, pattern):
                    excluded = True
                    break
            if not excluded:
                filtered_files.append(f)
        files = filtered_files
        excluded_count = original_count - len(files)
        if excluded_count > 0:
            print(f"  → File filter: excluded {excluded_count} files matching {exclude_files}")

    # Sort and return
    return sorted(files)


# Convenience functions for use in agent
def should_regenerate_metadata(
    workspace_path: Path,
    source_checksum_path: Path,
    metadata_dir: Path,
    metadata_checksum_path: Path,
    cobol_files: Optional[List[str]] = None
) -> tuple[bool, str]:
    """
    Determine if metadata should be regenerated based on checksums

    Args:
        workspace_path: Path to COBOL source files
        source_checksum_path: Path to source checksum YAML
        metadata_dir: Path to metadata directory
        metadata_checksum_path: Path to metadata checksum YAML
        cobol_files: Optional list of specific COBOL file names to process (e.g., ["PROG.COB", "MAIN.c74"])
                    If None, auto-discovers all COBOL files in workspace

    Returns:
        Tuple of (should_regenerate: bool, reason: str)
    """
    manager = ChecksumManager()

    # Get source files - use provided list or auto-discover
    if cobol_files:
        # Convert file names to full paths
        source_files = [workspace_path / fname for fname in cobol_files]
        print(f"\nℹ Processing {len(source_files)} specified files: {', '.join(cobol_files)}")
    else:
        # Auto-discover all COBOL files (recursively searches all subdirectories)
        source_files = get_source_files(workspace_path)
        print(f"\nℹ Auto-discovered {len(source_files)} COBOL files in workspace")

    if not source_files:
        return False, "No COBOL source files found"

    # Calculate current source checksums with relative paths
    current_source_checksums = manager.calculate_source_checksums(source_files, workspace_path)

    # Load previous source checksums
    previous_source_checksums = manager.load_checksums(source_checksum_path)

    # CASE 1: First run (no source checksums)
    if previous_source_checksums is None:
        print("\n" + "="*70)
        print("DECISION: Generate metadata (first run)")
        print("="*70)
        # Save source checksums for next run
        manager.save_checksums(current_source_checksums, source_checksum_path)
        return True, "First run - no previous source checksums"

    # CASE 2: Source files changed
    if not manager.compare_checksums(previous_source_checksums, current_source_checksums, "source"):
        print("\n" + "="*70)
        print("DECISION: Generate metadata (source files changed)")
        print("="*70)
        # Update source checksums
        manager.save_checksums(current_source_checksums, source_checksum_path)
        return True, "Source files changed"

    # Source unchanged - check metadata checksums
    print("\n" + "="*70)
    print("Source Files Unchanged - Checking Metadata")
    print("="*70)

    # Load previous metadata checksums
    previous_metadata_checksums = manager.load_checksums(metadata_checksum_path)

    # CASE 3: Metadata checksums missing
    if previous_metadata_checksums is None:
        print("\n" + "="*70)
        print("DECISION: Generate metadata (no metadata checksums)")
        print("="*70)
        return True, "Metadata checksums missing"

    # Calculate current metadata checksums
    current_metadata_checksums = manager.calculate_metadata_checksums(metadata_dir)

    # CASE 4: Metadata files corrupted/incomplete
    if not manager.compare_checksums(previous_metadata_checksums, current_metadata_checksums, "metadata"):
        print("\n" + "="*70)
        print("DECISION: Generate metadata (metadata corrupted/incomplete)")
        print("="*70)
        return True, "Metadata files corrupted or incomplete"

    # CASE 5: Everything valid
    print("\n" + "="*70)
    print("DECISION: Skip metadata generation (all checksums valid)")
    print("="*70)
    return False, "All checksums valid"


def save_metadata_checksums(metadata_dir: Path, metadata_checksum_path: Path):
    """
    Calculate and save metadata checksums after generation

    Args:
        metadata_dir: Path to metadata directory
        metadata_checksum_path: Path to save checksums
    """
    manager = ChecksumManager()

    # Calculate metadata checksums
    metadata_checksums = manager.calculate_metadata_checksums(metadata_dir)

    # Save to file
    manager.save_checksums(metadata_checksums, metadata_checksum_path)
