"""
Unit tests for Project Metadata Generator and Cache

Tests cover:
- MetadataResult and ProjectMetadataResult dataclasses
- MetadataCache operations
- MetadataCacheManager checksum and change detection
- SharedMetadataReader caching behavior
- ProjectMetadataGenerator initialization and configuration
"""

import pytest
import json
import sys
import tempfile
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch, MagicMock
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from project_metadata_generator import (
    MetadataResult,
    ProjectMetadataResult,
    ProjectMetadataGenerator,
)
from metadata_cache import (
    FileCacheEntry,
    MetadataCache,
    MetadataCacheManager,
    SharedMetadataReader,
    get_files_to_process,
)
from tree_mcp_client import FileInfo


class TestMetadataResult:
    """Tests for MetadataResult dataclass."""

    def test_create_success_result(self):
        """Test creating successful result."""
        result = MetadataResult(
            success=True,
            file_path="/project/MAIN.cbl",
            program_name="MAIN",
            metadata_files=["/meta/ctags/MAIN.json", "/meta/gnucobol/MAIN.json"],
            duration_seconds=5.2,
        )
        assert result.success is True
        assert result.program_name == "MAIN"
        assert len(result.metadata_files) == 2
        assert result.error is None

    def test_create_error_result(self):
        """Test creating error result."""
        result = MetadataResult(
            success=False,
            file_path="/project/BAD.cbl",
            program_name="BAD",
            error="Parse error",
        )
        assert result.success is False
        assert result.error == "Parse error"

    def test_to_dict(self):
        """Test result serialization."""
        result = MetadataResult(
            success=True,
            file_path="/project/MAIN.cbl",
            program_name="MAIN",
            metadata_files=["/meta/ctags/MAIN.json"],
            duration_seconds=3.5,
        )
        d = result.to_dict()
        assert d["success"] is True
        assert d["program_name"] == "MAIN"
        assert len(d["metadata_files"]) == 1


class TestProjectMetadataResult:
    """Tests for ProjectMetadataResult dataclass."""

    def test_create_result(self):
        """Test creating project result."""
        file_results = [
            MetadataResult(success=True, program_name="A"),
            MetadataResult(success=True, program_name="B"),
            MetadataResult(success=False, program_name="C", error="Failed"),
        ]
        result = ProjectMetadataResult(
            success=False,  # One file failed
            project_path="/project",
            total_files=3,
            successful_files=2,
            failed_files=1,
            file_results=file_results,
            project_metadata_files=["/meta/project-cfg.json"],
            errors=["C: Failed"],
            duration_seconds=15.0,
        )
        assert result.total_files == 3
        assert result.successful_files == 2
        assert result.failed_files == 1
        assert len(result.errors) == 1

    def test_to_dict(self):
        """Test project result serialization."""
        result = ProjectMetadataResult(
            success=True,
            project_path="/project",
            total_files=2,
            successful_files=2,
            failed_files=0,
        )
        d = result.to_dict()
        assert d["success"] is True
        assert d["total_files"] == 2


class TestFileCacheEntry:
    """Tests for FileCacheEntry dataclass."""

    def test_create_entry(self):
        """Test creating cache entry."""
        entry = FileCacheEntry(
            source_path="/project/MAIN.cbl",
            source_checksum="abc123",
            last_generated="2025-11-26T10:00:00",
            metadata_files=["/meta/ctags/MAIN.json"],
            generation_success=True,
        )
        assert entry.source_checksum == "abc123"
        assert entry.generation_success is True

    def test_to_dict(self):
        """Test entry serialization."""
        entry = FileCacheEntry(
            source_path="/project/MAIN.cbl",
            source_checksum="abc123",
            last_generated="2025-11-26T10:00:00",
        )
        d = entry.to_dict()
        assert d["source_checksum"] == "abc123"

    def test_from_dict(self):
        """Test entry deserialization."""
        data = {
            "source_path": "/project/MAIN.cbl",
            "source_checksum": "abc123",
            "last_generated": "2025-11-26T10:00:00",
            "metadata_files": ["/meta/MAIN.json"],
            "generation_success": True,
        }
        entry = FileCacheEntry.from_dict(data)
        assert entry.source_path == "/project/MAIN.cbl"
        assert entry.source_checksum == "abc123"


class TestMetadataCache:
    """Tests for MetadataCache dataclass."""

    def test_create_cache(self):
        """Test creating cache."""
        cache = MetadataCache(
            project_path="/project",
            files={
                "/project/A.cbl": FileCacheEntry(
                    source_path="/project/A.cbl",
                    source_checksum="aaa",
                    last_generated="2025-11-26T10:00:00",
                )
            }
        )
        assert len(cache.files) == 1
        assert "/project/A.cbl" in cache.files

    def test_to_dict_and_from_dict(self):
        """Test cache serialization roundtrip."""
        original = MetadataCache(
            project_path="/project",
            last_full_generation="2025-11-26T10:00:00",
            files={
                "/project/A.cbl": FileCacheEntry(
                    source_path="/project/A.cbl",
                    source_checksum="aaa",
                    last_generated="2025-11-26T10:00:00",
                )
            },
            project_metadata=["/meta/project-cfg.json"],
        )

        d = original.to_dict()
        restored = MetadataCache.from_dict(d)

        assert restored.project_path == original.project_path
        assert len(restored.files) == len(original.files)
        assert restored.project_metadata == original.project_metadata


class TestMetadataCacheManager:
    """Tests for MetadataCacheManager."""

    def test_calculate_checksum(self, tmp_path):
        """Test checksum calculation."""
        # Create test file
        test_file = tmp_path / "test.cbl"
        test_file.write_text("IDENTIFICATION DIVISION.\nPROGRAM-ID. TEST.")

        checksum = MetadataCacheManager.calculate_checksum(str(test_file))

        assert len(checksum) == 64  # SHA256 hex digest length
        assert checksum.isalnum()

    def test_checksum_changes_with_content(self, tmp_path):
        """Test that checksum changes when content changes."""
        test_file = tmp_path / "test.cbl"

        test_file.write_text("Version 1")
        checksum1 = MetadataCacheManager.calculate_checksum(str(test_file))

        test_file.write_text("Version 2")
        checksum2 = MetadataCacheManager.calculate_checksum(str(test_file))

        assert checksum1 != checksum2

    def test_needs_regeneration_not_in_cache(self, tmp_path):
        """Test that files not in cache need regeneration."""
        manager = MetadataCacheManager(str(tmp_path))

        # Create a test file
        test_file = tmp_path / "test.cbl"
        test_file.write_text("TEST CONTENT")

        assert manager.needs_regeneration(str(test_file)) is True

    def test_needs_regeneration_checksum_changed(self, tmp_path):
        """Test that files with changed checksum need regeneration."""
        metadata_dir = tmp_path / "metadata"
        metadata_dir.mkdir()
        manager = MetadataCacheManager(str(metadata_dir))

        # Create test file and add to cache
        test_file = tmp_path / "test.cbl"
        test_file.write_text("Original content")

        manager.update_entry(str(test_file), ["/meta/test.json"], success=True)
        manager.save_cache()

        # Modify the file
        test_file.write_text("Modified content")

        # Should need regeneration
        assert manager.needs_regeneration(str(test_file)) is True

    def test_needs_regeneration_metadata_missing(self, tmp_path):
        """Test that files with missing metadata need regeneration."""
        metadata_dir = tmp_path / "metadata"
        metadata_dir.mkdir()
        manager = MetadataCacheManager(str(metadata_dir))

        # Create test file
        test_file = tmp_path / "test.cbl"
        test_file.write_text("TEST CONTENT")

        # Add to cache with non-existent metadata file
        manager.update_entry(
            str(test_file),
            [str(tmp_path / "nonexistent.json")],
            success=True
        )

        # Should need regeneration because metadata file doesn't exist
        assert manager.needs_regeneration(str(test_file)) is True

    def test_needs_regeneration_previous_failure(self, tmp_path):
        """Test that files with previous failures need regeneration."""
        metadata_dir = tmp_path / "metadata"
        metadata_dir.mkdir()
        manager = MetadataCacheManager(str(metadata_dir))

        # Create test file
        test_file = tmp_path / "test.cbl"
        test_file.write_text("TEST CONTENT")

        # Add to cache as failed
        manager.update_entry(str(test_file), [], success=False, error="Parse error")

        # Should need regeneration
        assert manager.needs_regeneration(str(test_file)) is True

    def test_no_regeneration_needed(self, tmp_path):
        """Test that unchanged files don't need regeneration."""
        metadata_dir = tmp_path / "metadata"
        metadata_dir.mkdir()
        manager = MetadataCacheManager(str(metadata_dir))

        # Create test file
        test_file = tmp_path / "test.cbl"
        test_file.write_text("TEST CONTENT")

        # Create metadata file
        meta_file = metadata_dir / "test.json"
        meta_file.write_text('{"test": true}')

        # Add to cache
        manager.update_entry(str(test_file), [str(meta_file)], success=True)

        # Should NOT need regeneration
        assert manager.needs_regeneration(str(test_file)) is False

    def test_get_files_needing_regeneration(self, tmp_path):
        """Test filtering files that need regeneration."""
        metadata_dir = tmp_path / "metadata"
        metadata_dir.mkdir()
        manager = MetadataCacheManager(str(metadata_dir))

        # Create test files
        file1 = tmp_path / "A.cbl"
        file1.write_text("FILE A")
        file2 = tmp_path / "B.cbl"
        file2.write_text("FILE B")
        file3 = tmp_path / "C.cbl"
        file3.write_text("FILE C")

        # Create metadata for A
        meta_a = metadata_dir / "A.json"
        meta_a.write_text('{}')
        manager.update_entry(str(file1), [str(meta_a)], success=True)

        # B and C not in cache
        source_files = [str(file1), str(file2), str(file3)]
        needs_regen = manager.get_files_needing_regeneration(source_files)

        assert str(file1) not in needs_regen  # Cached
        assert str(file2) in needs_regen  # Not cached
        assert str(file3) in needs_regen  # Not cached

    def test_save_and_load_cache(self, tmp_path):
        """Test cache persistence."""
        metadata_dir = tmp_path / "metadata"
        metadata_dir.mkdir()

        # Create and save cache
        manager1 = MetadataCacheManager(str(metadata_dir))
        test_file = tmp_path / "test.cbl"
        test_file.write_text("TEST")
        manager1.update_entry(str(test_file), ["/meta/test.json"], success=True)
        manager1.save_cache()

        # Load cache in new manager
        manager2 = MetadataCacheManager(str(metadata_dir))

        assert str(test_file) in manager2.cache.files

    def test_clear_cache(self, tmp_path):
        """Test cache clearing."""
        metadata_dir = tmp_path / "metadata"
        metadata_dir.mkdir()
        manager = MetadataCacheManager(str(metadata_dir))

        manager.update_entry("/test.cbl", ["/meta/test.json"], success=True)
        manager.save_cache()

        assert len(manager.cache.files) == 1

        manager.clear_cache()

        assert len(manager.cache.files) == 0
        assert not manager.cache_file.exists()

    def test_get_cache_stats(self, tmp_path):
        """Test cache statistics."""
        metadata_dir = tmp_path / "metadata"
        metadata_dir.mkdir()
        manager = MetadataCacheManager(str(metadata_dir))

        manager.update_entry("/a.cbl", ["/meta/a.json"], success=True)
        manager.update_entry("/b.cbl", [], success=False, error="Failed")
        manager.update_project_metadata(["/meta/project.json"])

        stats = manager.get_cache_stats()

        assert stats["total_entries"] == 2
        assert stats["successful"] == 1
        assert stats["failed"] == 1
        assert stats["project_metadata_files"] == 1


class TestSharedMetadataReader:
    """Tests for SharedMetadataReader."""

    def test_read_metadata(self, tmp_path):
        """Test reading metadata file."""
        metadata_dir = tmp_path / "metadata"
        metadata_dir.mkdir()

        # Create test metadata
        test_data = {"symbols": ["A", "B", "C"]}
        test_file = metadata_dir / "test.json"
        test_file.write_text(json.dumps(test_data))

        reader = SharedMetadataReader(str(metadata_dir))
        data = reader.read_metadata("test.json")

        assert data == test_data

    def test_read_metadata_caching(self, tmp_path):
        """Test that metadata is cached in memory."""
        metadata_dir = tmp_path / "metadata"
        metadata_dir.mkdir()

        test_file = metadata_dir / "test.json"
        test_file.write_text('{"value": 1}')

        reader = SharedMetadataReader(str(metadata_dir))

        # First read
        data1 = reader.read_metadata("test.json")
        assert reader.get_cache_size() == 1

        # Second read (from cache)
        data2 = reader.read_metadata("test.json")
        assert data1 == data2
        assert reader.get_cache_size() == 1  # Still 1, not 2

    def test_read_nonexistent_file(self, tmp_path):
        """Test reading nonexistent file returns None."""
        reader = SharedMetadataReader(str(tmp_path))
        data = reader.read_metadata("nonexistent.json")
        assert data is None

    def test_read_file_metadata(self, tmp_path):
        """Test reading all metadata for a program."""
        metadata_dir = tmp_path / "metadata"
        (metadata_dir / "ctags").mkdir(parents=True)
        (metadata_dir / "gnucobol").mkdir(parents=True)
        (metadata_dir / "superbol" / "cfg").mkdir(parents=True)

        # Create test metadata files
        (metadata_dir / "ctags" / "ctags-TEST-outline.json").write_text('{"ctags": true}')
        (metadata_dir / "gnucobol" / "gnucobol-TEST-analysis.json").write_text('{"gnucobol": true}')

        reader = SharedMetadataReader(str(metadata_dir))
        metadata = reader.read_file_metadata("TEST")

        assert metadata["ctags_outline"] == {"ctags": True}
        assert metadata["gnucobol_analysis"] == {"gnucobol": True}
        assert metadata["superbol_symbols"] is None  # Not created

    def test_clear_cache(self, tmp_path):
        """Test clearing in-memory cache."""
        metadata_dir = tmp_path / "metadata"
        metadata_dir.mkdir()
        (metadata_dir / "test.json").write_text('{}')

        reader = SharedMetadataReader(str(metadata_dir))
        reader.read_metadata("test.json")

        assert reader.get_cache_size() == 1

        reader.clear_cache()

        assert reader.get_cache_size() == 0


class TestGetFilesToProcess:
    """Tests for get_files_to_process utility."""

    def test_force_regenerate(self, tmp_path):
        """Test force regenerate returns all files."""
        files = ["/a.cbl", "/b.cbl", "/c.cbl"]
        result = get_files_to_process(files, str(tmp_path), force_regenerate=True)
        assert result == files

    def test_normal_processing(self, tmp_path):
        """Test normal processing uses cache."""
        metadata_dir = tmp_path / "metadata"
        metadata_dir.mkdir()

        # Create test file
        test_file = tmp_path / "test.cbl"
        test_file.write_text("TEST")

        files = [str(test_file)]
        result = get_files_to_process(files, str(metadata_dir), force_regenerate=False)

        # File not in cache, should be included
        assert str(test_file) in result


class TestProjectMetadataGenerator:
    """Tests for ProjectMetadataGenerator."""

    def test_initialization(self, tmp_path):
        """Test generator initialization."""
        project_path = tmp_path / "project"
        project_path.mkdir()
        metadata_dir = tmp_path / "metadata"

        servers_config = {
            "ctags": {"docker_image": "ctags:test"},
            "gnuCobol": {"docker_image": "gnucobol:test"},
            "superbol-lsp": {"docker_image": "superbol:test"},
        }

        generator = ProjectMetadataGenerator(
            project_path=str(project_path),
            metadata_dir=str(metadata_dir),
            servers_config=servers_config,
        )

        assert generator.project_path == project_path
        assert generator.metadata_dir == metadata_dir

    def test_ensure_directories(self, tmp_path):
        """Test directory creation."""
        project_path = tmp_path / "project"
        project_path.mkdir()
        metadata_dir = tmp_path / "metadata"

        servers_config = {
            "ctags": {"docker_image": "ctags:test"},
            "gnuCobol": {"docker_image": "gnucobol:test"},
            "superbol-lsp": {"docker_image": "superbol:test"},
        }

        generator = ProjectMetadataGenerator(
            project_path=str(project_path),
            metadata_dir=str(metadata_dir),
            servers_config=servers_config,
        )

        generator._ensure_directories()

        assert (metadata_dir / "ctags").exists()
        assert (metadata_dir / "gnucobol").exists()
        assert (metadata_dir / "superbol").exists()
        assert (metadata_dir / "superbol" / "cfg").exists()

    def test_missing_config_raises_error(self, tmp_path):
        """Test that missing config raises ValueError."""
        project_path = tmp_path / "project"
        project_path.mkdir()

        # Missing gnuCobol config
        servers_config = {
            "ctags": {"docker_image": "ctags:test"},
            "superbol-lsp": {"docker_image": "superbol:test"},
        }

        generator = ProjectMetadataGenerator(
            project_path=str(project_path),
            metadata_dir=str(tmp_path / "metadata"),
            servers_config=servers_config,
        )

        with pytest.raises(ValueError, match="gnuCobol"):
            generator._get_mcp_config()

    def test_mcp_config_generation(self, tmp_path):
        """Test MCP configuration generation."""
        project_path = tmp_path / "project"
        project_path.mkdir()
        metadata_dir = tmp_path / "metadata"

        servers_config = {
            "ctags": {"docker_image": "ctags:v1"},
            "gnuCobol": {"docker_image": "gnucobol:v1"},
            "superbol-lsp": {"docker_image": "superbol:v1"},
        }

        generator = ProjectMetadataGenerator(
            project_path=str(project_path),
            metadata_dir=str(metadata_dir),
            servers_config=servers_config,
        )

        config = generator._get_mcp_config()

        assert "mcpServers" in config
        assert "ctags" in config["mcpServers"]
        assert "gnucobol" in config["mcpServers"]
        assert "superbol" in config["mcpServers"]
        assert "ctags:v1" in config["mcpServers"]["ctags"]["args"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
