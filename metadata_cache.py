"""
Metadata Cache Manager for COBOL Documentation Orchestrator

This module provides intelligent caching and reuse of generated metadata:
- Checksums to detect file changes
- Skip regeneration for unchanged files
- Efficient metadata sharing across parallel agents
- Token budget optimization by avoiding duplicate metadata

The cache tracks:
- Source file checksums (SHA256)
- Metadata file timestamps
- Generation status per file
"""

import hashlib
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

logger = logging.getLogger(__name__)


@dataclass
class FileCacheEntry:
    """Cache entry for a single source file."""
    source_path: str
    source_checksum: str
    last_generated: str  # ISO format timestamp
    metadata_files: List[str] = field(default_factory=list)
    generation_success: bool = True
    error: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_path": self.source_path,
            "source_checksum": self.source_checksum,
            "last_generated": self.last_generated,
            "metadata_files": self.metadata_files,
            "generation_success": self.generation_success,
            "error": self.error,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FileCacheEntry":
        return cls(
            source_path=data["source_path"],
            source_checksum=data["source_checksum"],
            last_generated=data["last_generated"],
            metadata_files=data.get("metadata_files", []),
            generation_success=data.get("generation_success", True),
            error=data.get("error"),
        )


@dataclass
class MetadataCache:
    """
    Cache for tracking generated metadata and detecting changes.

    This cache enables:
    - Skipping unchanged files during regeneration
    - Efficient incremental updates
    - Tracking which metadata files exist for each source
    """
    version: str = "1.0"
    project_path: str = ""
    last_full_generation: Optional[str] = None
    files: Dict[str, FileCacheEntry] = field(default_factory=dict)
    project_metadata: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "version": self.version,
            "project_path": self.project_path,
            "last_full_generation": self.last_full_generation,
            "files": {k: v.to_dict() for k, v in self.files.items()},
            "project_metadata": self.project_metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MetadataCache":
        files = {}
        for k, v in data.get("files", {}).items():
            files[k] = FileCacheEntry.from_dict(v)

        return cls(
            version=data.get("version", "1.0"),
            project_path=data.get("project_path", ""),
            last_full_generation=data.get("last_full_generation"),
            files=files,
            project_metadata=data.get("project_metadata", []),
        )


class MetadataCacheManager:
    """
    Manages metadata caching for efficient regeneration.

    Features:
    - SHA256 checksums for change detection
    - Skip unchanged files
    - Track metadata file locations
    - Support incremental updates
    """

    def __init__(self, metadata_dir: str, cache_file: str = "metadata_cache.json"):
        """
        Initialize cache manager.

        Args:
            metadata_dir: Directory containing metadata
            cache_file: Name of cache file (stored in metadata_dir)
        """
        self.metadata_dir = Path(metadata_dir)
        self.cache_file = self.metadata_dir / cache_file
        self.cache: MetadataCache = MetadataCache()
        self._load_cache()

    def _load_cache(self) -> None:
        """Load cache from file if it exists."""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r') as f:
                    data = json.load(f)
                self.cache = MetadataCache.from_dict(data)
                logger.info(f"Loaded cache with {len(self.cache.files)} entries")
            except Exception as e:
                logger.warning(f"Failed to load cache: {e}")
                self.cache = MetadataCache()
        else:
            logger.info("No existing cache found, starting fresh")

    def save_cache(self) -> None:
        """Save cache to file."""
        self.metadata_dir.mkdir(parents=True, exist_ok=True)
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(self.cache.to_dict(), f, indent=2)
            logger.debug(f"Cache saved with {len(self.cache.files)} entries")
        except Exception as e:
            logger.error(f"Failed to save cache: {e}")

    @staticmethod
    def calculate_checksum(file_path: str) -> str:
        """
        Calculate SHA256 checksum of a file.

        Args:
            file_path: Path to file

        Returns:
            Hex digest of SHA256 hash
        """
        sha256 = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(8192), b''):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except Exception as e:
            logger.error(f"Failed to calculate checksum for {file_path}: {e}")
            return ""

    def needs_regeneration(self, source_path: str) -> bool:
        """
        Check if a source file needs metadata regeneration.

        A file needs regeneration if:
        - It's not in the cache
        - Its checksum has changed
        - Any of its metadata files are missing
        - Previous generation failed

        Args:
            source_path: Path to source file

        Returns:
            True if metadata should be regenerated
        """
        source_path = str(Path(source_path).absolute())

        # Not in cache
        if source_path not in self.cache.files:
            logger.debug(f"  {Path(source_path).name}: Not in cache")
            return True

        entry = self.cache.files[source_path]

        # Previous generation failed
        if not entry.generation_success:
            logger.debug(f"  {Path(source_path).name}: Previous generation failed")
            return True

        # Checksum changed
        current_checksum = self.calculate_checksum(source_path)
        if current_checksum != entry.source_checksum:
            logger.debug(f"  {Path(source_path).name}: Checksum changed")
            return True

        # Metadata files missing
        for metadata_file in entry.metadata_files:
            if not Path(metadata_file).exists():
                logger.debug(f"  {Path(source_path).name}: Missing metadata file {metadata_file}")
                return True

        logger.debug(f"  {Path(source_path).name}: Up to date")
        return False

    def get_files_needing_regeneration(self, source_files: List[str]) -> List[str]:
        """
        Filter list of source files to those needing regeneration.

        Args:
            source_files: List of source file paths

        Returns:
            List of files that need metadata regeneration
        """
        needs_regen = []
        up_to_date = []

        for source_path in source_files:
            if self.needs_regeneration(source_path):
                needs_regen.append(source_path)
            else:
                up_to_date.append(source_path)

        logger.info(f"Cache check: {len(needs_regen)} need regeneration, {len(up_to_date)} up to date")
        return needs_regen

    def update_entry(
        self,
        source_path: str,
        metadata_files: List[str],
        success: bool = True,
        error: Optional[str] = None,
    ) -> None:
        """
        Update cache entry for a source file.

        Args:
            source_path: Path to source file
            metadata_files: List of generated metadata file paths
            success: Whether generation succeeded
            error: Error message if failed
        """
        source_path = str(Path(source_path).absolute())
        checksum = self.calculate_checksum(source_path)

        entry = FileCacheEntry(
            source_path=source_path,
            source_checksum=checksum,
            last_generated=datetime.now().isoformat(),
            metadata_files=metadata_files,
            generation_success=success,
            error=error,
        )

        self.cache.files[source_path] = entry
        logger.debug(f"Updated cache entry for {Path(source_path).name}")

    def update_project_metadata(self, metadata_files: List[str]) -> None:
        """
        Update project-level metadata file list.

        Args:
            metadata_files: List of project metadata file paths
        """
        self.cache.project_metadata = metadata_files
        self.cache.last_full_generation = datetime.now().isoformat()

    def get_cached_metadata_files(self, source_path: str) -> List[str]:
        """
        Get list of cached metadata files for a source file.

        Args:
            source_path: Path to source file

        Returns:
            List of metadata file paths (empty if not cached)
        """
        source_path = str(Path(source_path).absolute())
        if source_path in self.cache.files:
            return self.cache.files[source_path].metadata_files
        return []

    def get_all_cached_metadata(self) -> Dict[str, List[str]]:
        """
        Get all cached metadata file mappings.

        Returns:
            Dict mapping source paths to their metadata files
        """
        return {
            source: entry.metadata_files
            for source, entry in self.cache.files.items()
        }

    def clear_cache(self) -> None:
        """Clear all cache entries."""
        self.cache = MetadataCache()
        if self.cache_file.exists():
            self.cache_file.unlink()
        logger.info("Cache cleared")

    def get_cache_stats(self) -> Dict[str, Any]:
        """
        Get cache statistics.

        Returns:
            Dict with cache statistics
        """
        total_entries = len(self.cache.files)
        successful = sum(1 for e in self.cache.files.values() if e.generation_success)
        failed = total_entries - successful

        total_metadata_files = sum(
            len(e.metadata_files) for e in self.cache.files.values()
        )

        return {
            "total_entries": total_entries,
            "successful": successful,
            "failed": failed,
            "total_metadata_files": total_metadata_files,
            "project_metadata_files": len(self.cache.project_metadata),
            "last_full_generation": self.cache.last_full_generation,
        }


class SharedMetadataReader:
    """
    Efficient reader for sharing metadata across parallel agents.

    This class provides:
    - Lazy loading of metadata files
    - In-memory caching to avoid redundant reads
    - Thread-safe access for parallel agents
    """

    def __init__(self, metadata_dir: str):
        """
        Initialize shared metadata reader.

        Args:
            metadata_dir: Directory containing metadata files
        """
        self.metadata_dir = Path(metadata_dir)
        self._cache: Dict[str, Any] = {}

    def read_metadata(self, relative_path: str) -> Optional[Dict[str, Any]]:
        """
        Read metadata file with caching.

        Args:
            relative_path: Path relative to metadata_dir

        Returns:
            Parsed JSON data or None if not found
        """
        full_path = str(self.metadata_dir / relative_path)

        # Check in-memory cache
        if full_path in self._cache:
            return self._cache[full_path]

        # Read from file
        try:
            file_path = Path(full_path)
            if not file_path.exists():
                return None

            with open(file_path, 'r') as f:
                data = json.load(f)

            # Cache for reuse
            self._cache[full_path] = data
            return data

        except Exception as e:
            logger.error(f"Failed to read metadata {relative_path}: {e}")
            return None

    def read_project_relationships(self) -> Optional[Dict[str, Any]]:
        """Read project-level relationships (GnuCOBOL)."""
        return self.read_metadata("gnucobol/project-relationships.json")

    def read_project_cfg(self) -> Optional[Dict[str, Any]]:
        """Read project-level CFG (SuperBOL)."""
        return self.read_metadata("superbol/project-cfg.json")

    def read_project_symbols(self) -> Optional[Dict[str, Any]]:
        """Read project-level symbols (CTags)."""
        return self.read_metadata("ctags/project-symbols.json")

    def read_file_metadata(self, program_name: str) -> Dict[str, Any]:
        """
        Read all metadata for a specific program.

        Args:
            program_name: Program name (without extension)

        Returns:
            Dict with all available metadata for the program

        Note: analyze_cobol (gnucobol_analysis) is deprecated.
              Using gnucobol_relationships and gnucobol_cross_refs instead.
        """
        return {
            "ctags_outline": self.read_metadata(f"ctags/ctags-{program_name}-outline.json"),
            "gnucobol_relationships": self.read_metadata(f"gnucobol/gnucobol-{program_name}-relationships.json"),
            "gnucobol_cross_refs": self.read_metadata(f"gnucobol/gnucobol-{program_name}-cross-refs.json"),
            "superbol_symbols": self.read_metadata(f"superbol/superbol-{program_name}-symbols.json"),
            "superbol_cfg": self.read_metadata(f"superbol/cfg/{program_name}-cfg.json"),
        }

    def clear_cache(self) -> None:
        """Clear in-memory cache."""
        self._cache.clear()

    def get_cache_size(self) -> int:
        """Get number of cached entries."""
        return len(self._cache)


# Utility functions
def get_files_to_process(
    source_files: List[str],
    metadata_dir: str,
    force_regenerate: bool = False,
) -> List[str]:
    """
    Determine which files need metadata generation.

    Args:
        source_files: List of all source file paths
        metadata_dir: Metadata directory path
        force_regenerate: If True, regenerate all files

    Returns:
        List of files needing metadata generation
    """
    if force_regenerate:
        logger.info("Force regeneration enabled - processing all files")
        return source_files

    cache_manager = MetadataCacheManager(metadata_dir)
    return cache_manager.get_files_needing_regeneration(source_files)
