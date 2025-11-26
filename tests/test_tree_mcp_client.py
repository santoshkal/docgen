"""
Unit tests for Tree MCP Client

Tests cover:
- FileInfo and TreeScanResult data classes
- JSON parsing from tree output
- File extraction from tree structure
- Extension filtering
- Error handling
"""

import pytest
import json
import sys
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch, MagicMock

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from tree_mcp_client import (
    TreeMCPClient,
    FileInfo,
    TreeScanResult,
    scan_project_directory,
)


class TestFileInfo:
    """Tests for FileInfo dataclass."""

    def test_create_file_info(self):
        """Test creating FileInfo instance."""
        info = FileInfo(
            name="MAINPROG.cbl",
            path="src/MAINPROG.cbl",
            absolute_path="/project/src/MAINPROG.cbl",
            extension=".cbl",
            size=1024,
        )
        assert info.name == "MAINPROG.cbl"
        assert info.path == "src/MAINPROG.cbl"
        assert info.absolute_path == "/project/src/MAINPROG.cbl"
        assert info.extension == ".cbl"
        assert info.size == 1024

    def test_to_dict(self):
        """Test FileInfo to_dict conversion."""
        info = FileInfo(
            name="TEST.cob",
            path="TEST.cob",
            absolute_path="/project/TEST.cob",
            extension=".cob",
        )
        result = info.to_dict()
        assert result["name"] == "TEST.cob"
        assert result["path"] == "TEST.cob"
        assert result["extension"] == ".cob"
        assert result["size"] is None


class TestTreeScanResult:
    """Tests for TreeScanResult dataclass."""

    def test_empty_result(self):
        """Test empty scan result."""
        result = TreeScanResult(
            success=True,
            project_path="/project",
        )
        assert result.success is True
        assert result.files == []
        assert result.total_files == 0
        assert result.error is None

    def test_result_with_files(self):
        """Test scan result with files."""
        files = [
            FileInfo("A.cbl", "A.cbl", "/p/A.cbl", ".cbl"),
            FileInfo("B.cob", "src/B.cob", "/p/src/B.cob", ".cob"),
        ]
        result = TreeScanResult(
            success=True,
            project_path="/p",
            files=files,
            total_files=2,
        )
        assert len(result.files) == 2
        assert result.total_files == 2

    def test_get_file_paths(self):
        """Test getting absolute file paths."""
        files = [
            FileInfo("A.cbl", "A.cbl", "/p/A.cbl", ".cbl"),
            FileInfo("B.cob", "src/B.cob", "/p/src/B.cob", ".cob"),
        ]
        result = TreeScanResult(success=True, project_path="/p", files=files, total_files=2)
        paths = result.get_file_paths()
        assert paths == ["/p/A.cbl", "/p/src/B.cob"]

    def test_get_relative_paths(self):
        """Test getting relative file paths."""
        files = [
            FileInfo("A.cbl", "A.cbl", "/p/A.cbl", ".cbl"),
            FileInfo("B.cob", "src/B.cob", "/p/src/B.cob", ".cob"),
        ]
        result = TreeScanResult(success=True, project_path="/p", files=files, total_files=2)
        paths = result.get_relative_paths()
        assert paths == ["A.cbl", "src/B.cob"]

    def test_error_result(self):
        """Test error scan result."""
        result = TreeScanResult(
            success=False,
            project_path="/project",
            error="Connection failed",
        )
        assert result.success is False
        assert result.error == "Connection failed"

    def test_to_dict(self):
        """Test TreeScanResult to_dict conversion."""
        files = [FileInfo("A.cbl", "A.cbl", "/p/A.cbl", ".cbl")]
        result = TreeScanResult(
            success=True,
            project_path="/p",
            files=files,
            total_files=1,
        )
        d = result.to_dict()
        assert d["success"] is True
        assert d["project_path"] == "/p"
        assert len(d["files"]) == 1
        assert d["total_files"] == 1


class TestTreeMCPClient:
    """Tests for TreeMCPClient class."""

    def test_requires_docker_image(self):
        """Test that docker_image is required."""
        import pytest
        with pytest.raises(TypeError):
            # docker_image is required, no default
            TreeMCPClient()

    def test_empty_docker_image_raises_error(self):
        """Test that empty docker_image raises error."""
        import pytest
        with pytest.raises(ValueError, match="docker_image is required"):
            TreeMCPClient(docker_image="")

    def test_initialization_with_docker_image(self):
        """Test client initialization with docker_image."""
        client = TreeMCPClient(docker_image="tree-mcp:test")
        assert client.docker_image == "tree-mcp:test"
        assert ".cbl" in client.extensions
        assert ".git" in client.exclude_dirs
        assert client.max_depth is None

    def test_custom_initialization(self):
        """Test client initialization with custom parameters."""
        client = TreeMCPClient(
            docker_image="custom-tree:v1",
            extensions=[".cbl", ".cob"],
            exclude_dirs=[".git", "build"],
            max_depth=5,
        )
        assert client.docker_image == "custom-tree:v1"
        assert client.extensions == [".cbl", ".cob"]
        assert client.exclude_dirs == [".git", "build"]
        assert client.max_depth == 5

    def test_mcp_config_generation(self):
        """Test MCP configuration generation."""
        client = TreeMCPClient(docker_image="tree:test")
        config = client._get_mcp_config("/project/path")

        assert "mcpServers" in config
        assert "tree" in config["mcpServers"]
        tree_config = config["mcpServers"]["tree"]
        assert tree_config["command"] == "docker"
        assert "tree:test" in tree_config["args"]
        assert "-v" in tree_config["args"]
        assert "/project/path:/workspace:ro" in tree_config["args"]

    def test_filter_by_extensions_cobol(self):
        """Test filtering files by COBOL extensions."""
        client = TreeMCPClient(docker_image="tree-mcp:test", extensions=[".cbl", ".cob", ".cpy"])
        files = [
            FileInfo("PROG.cbl", "PROG.cbl", "/p/PROG.cbl", ".cbl"),
            FileInfo("DATA.cpy", "DATA.cpy", "/p/DATA.cpy", ".cpy"),
            FileInfo("README.md", "README.md", "/p/README.md", ".md"),
            FileInfo("Makefile", "Makefile", "/p/Makefile", ""),
        ]
        filtered = client._filter_by_extensions(files)
        assert len(filtered) == 2
        assert all(f.extension in [".cbl", ".cpy"] for f in filtered)

    def test_filter_by_extensions_case_insensitive(self):
        """Test extension filtering is case insensitive."""
        client = TreeMCPClient(docker_image="tree-mcp:test", extensions=[".cbl", ".CBL"])
        files = [
            FileInfo("PROG.cbl", "PROG.cbl", "/p/PROG.cbl", ".cbl"),
            FileInfo("PROG2.CBL", "PROG2.CBL", "/p/PROG2.CBL", ".CBL"),
            FileInfo("prog3.Cbl", "prog3.Cbl", "/p/prog3.Cbl", ".Cbl"),
        ]
        filtered = client._filter_by_extensions(files)
        assert len(filtered) == 3

    def test_filter_by_extensions_none_returns_all(self):
        """Test filtering with None extensions returns all files."""
        client = TreeMCPClient(docker_image="tree-mcp:test", extensions=None)
        # When extensions is None, client uses default extensions
        # But for filtering, we test the _filter_by_extensions method directly
        client.extensions = None  # Override to None
        files = [
            FileInfo("PROG.cbl", "PROG.cbl", "/p/PROG.cbl", ".cbl"),
            FileInfo("README.md", "README.md", "/p/README.md", ".md"),
        ]
        filtered = client._filter_by_extensions(files)
        # When extensions is None/empty, all files should pass through
        assert len(filtered) == 2


class TestTreeParsing:
    """Tests for parsing tree JSON output."""

    def test_extract_files_simple(self):
        """Test extracting files from simple tree structure."""
        client = TreeMCPClient(docker_image="tree-mcp:test")
        tree_data = [
            {"type": "file", "name": "MAINPROG.cbl"},
            {"type": "file", "name": "SUBPROG.cob"},
        ]
        files = client._extract_files_from_tree(tree_data, "/project")
        assert len(files) == 2
        assert files[0].name == "MAINPROG.cbl"
        assert files[0].path == "MAINPROG.cbl"
        assert files[0].absolute_path == "/project/MAINPROG.cbl"
        assert files[1].name == "SUBPROG.cob"

    def test_extract_files_nested_directories(self):
        """Test extracting files from nested directory structure."""
        client = TreeMCPClient(docker_image="tree-mcp:test")
        tree_data = [
            {
                "type": "directory",
                "name": "src",
                "contents": [
                    {"type": "file", "name": "MAIN.cbl"},
                    {
                        "type": "directory",
                        "name": "copy",
                        "contents": [
                            {"type": "file", "name": "COMMON.cpy"},
                        ]
                    }
                ]
            }
        ]
        files = client._extract_files_from_tree(tree_data, "/project")
        assert len(files) == 2
        assert files[0].path == "src/MAIN.cbl"
        assert files[0].absolute_path == "/project/src/MAIN.cbl"
        assert files[1].path == "src/copy/COMMON.cpy"

    def test_extract_files_excludes_directories(self):
        """Test that excluded directories are skipped."""
        client = TreeMCPClient(docker_image="tree-mcp:test", exclude_dirs=[".git", "node_modules"])
        tree_data = [
            {"type": "file", "name": "MAIN.cbl"},
            {
                "type": "directory",
                "name": ".git",
                "contents": [
                    {"type": "file", "name": "config"},
                ]
            },
            {
                "type": "directory",
                "name": "src",
                "contents": [
                    {"type": "file", "name": "SUB.cbl"},
                ]
            }
        ]
        files = client._extract_files_from_tree(tree_data, "/project")
        assert len(files) == 2
        assert all(".git" not in f.path for f in files)

    def test_extract_files_handles_report_entry(self):
        """Test that report entries from tree command are ignored."""
        client = TreeMCPClient(docker_image="tree-mcp:test")
        tree_data = [
            {"type": "file", "name": "MAIN.cbl"},
            {"type": "report", "directories": 2, "files": 5},
        ]
        files = client._extract_files_from_tree(tree_data, "/project")
        assert len(files) == 1
        assert files[0].name == "MAIN.cbl"

    def test_extract_files_with_size(self):
        """Test extracting files that include size information."""
        client = TreeMCPClient(docker_image="tree-mcp:test")
        tree_data = [
            {"type": "file", "name": "LARGE.cbl", "size": 50000},
            {"type": "file", "name": "SMALL.cbl", "size": 1024},
        ]
        files = client._extract_files_from_tree(tree_data, "/project")
        assert len(files) == 2
        assert files[0].size == 50000
        assert files[1].size == 1024

    def test_extract_files_empty_tree(self):
        """Test extracting from empty tree structure."""
        client = TreeMCPClient(docker_image="tree-mcp:test")
        files = client._extract_files_from_tree([], "/project")
        assert len(files) == 0

    def test_extract_files_single_dict(self):
        """Test extracting from single file entry (not list)."""
        client = TreeMCPClient(docker_image="tree-mcp:test")
        tree_data = {"type": "file", "name": "SINGLE.cbl"}
        files = client._extract_files_from_tree(tree_data, "/project")
        assert len(files) == 1
        assert files[0].name == "SINGLE.cbl"


class TestJSONExtraction:
    """Tests for extracting JSON from MCP results."""

    def test_extract_json_from_dict_with_json_data(self):
        """Test extracting JSON when result has json_data field."""
        client = TreeMCPClient(docker_image="tree-mcp:test")
        result = {
            "success": True,
            "json_data": [{"type": "file", "name": "TEST.cbl"}],
        }
        data = client._extract_json_from_result(result)
        assert data == [{"type": "file", "name": "TEST.cbl"}]

    def test_extract_json_from_plain_dict(self):
        """Test extracting JSON from plain dict result."""
        client = TreeMCPClient(docker_image="tree-mcp:test")
        result = {"type": "file", "name": "TEST.cbl"}
        data = client._extract_json_from_result(result)
        assert data == {"type": "file", "name": "TEST.cbl"}

    def test_extract_json_from_call_tool_result(self):
        """Test extracting JSON from CallToolResult-like object."""
        client = TreeMCPClient(docker_image="tree-mcp:test")

        # Mock CallToolResult structure
        mock_text_content = Mock()
        mock_text_content.text = json.dumps({
            "success": True,
            "json_data": [{"type": "file", "name": "MOCK.cbl"}]
        })

        mock_result = Mock()
        mock_result.content = [mock_text_content]

        data = client._extract_json_from_result(mock_result)
        assert data == [{"type": "file", "name": "MOCK.cbl"}]

    def test_extract_json_returns_none_on_failure(self):
        """Test that extraction returns None on parse failure."""
        client = TreeMCPClient(docker_image="tree-mcp:test")

        mock_text_content = Mock()
        mock_text_content.text = "not valid json {"

        mock_result = Mock()
        mock_result.content = [mock_text_content]

        data = client._extract_json_from_result(mock_result)
        assert data is None


class TestWriteFileList:
    """Tests for writing file list to JSON."""

    def test_write_file_list(self, tmp_path):
        """Test writing scan results to JSON file."""
        client = TreeMCPClient(docker_image="tree-mcp:test")

        files = [
            FileInfo("A.cbl", "A.cbl", "/p/A.cbl", ".cbl"),
            FileInfo("B.cob", "src/B.cob", "/p/src/B.cob", ".cob"),
        ]
        result = TreeScanResult(
            success=True,
            project_path="/p",
            files=files,
            total_files=2,
        )

        output_file = tmp_path / "metadata" / "file_list.json"
        client.write_file_list(result, str(output_file))

        assert output_file.exists()

        with open(output_file) as f:
            data = json.load(f)

        assert data["success"] is True
        assert data["project_path"] == "/p"
        assert len(data["files"]) == 2
        assert data["files"][0]["name"] == "A.cbl"

    def test_write_file_list_creates_directory(self, tmp_path):
        """Test that writing creates parent directories."""
        client = TreeMCPClient(docker_image="tree-mcp:test")
        result = TreeScanResult(success=True, project_path="/p")

        # Use deeply nested path
        output_file = tmp_path / "deep" / "nested" / "path" / "file_list.json"
        client.write_file_list(result, str(output_file))

        assert output_file.exists()


class TestIntegration:
    """Integration tests with mocked MCP client."""

    @pytest.mark.asyncio
    async def test_scan_directory_success(self):
        """Test successful directory scan with mocked MCP client."""
        # Create mock session
        mock_session = AsyncMock()
        mock_result = Mock()
        mock_text = Mock()
        mock_text.text = json.dumps({
            "success": True,
            "json_data": [
                {"type": "file", "name": "MAINPROG.cbl"},
                {
                    "type": "directory",
                    "name": "copy",
                    "contents": [
                        {"type": "file", "name": "COMMON.cpy"}
                    ]
                }
            ]
        })
        mock_result.content = [mock_text]
        mock_session.call_tool = AsyncMock(return_value=mock_result)

        # Create mock MCP client
        mock_mcp_client = Mock()
        mock_mcp_client.get_session.return_value = mock_session
        mock_mcp_client.create_all_sessions = AsyncMock()

        # Create client and inject mock
        client = TreeMCPClient(docker_image="tree-mcp:test")

        with patch('tree_mcp_client.MCPClient') as MockMCPClient:
            MockMCPClient.from_dict.return_value = mock_mcp_client

            result = await client.scan_directory("/test/project")

        assert result.success is True
        assert result.total_files == 2
        assert result.files[0].name == "MAINPROG.cbl"
        assert result.files[1].name == "COMMON.cpy"
        assert result.files[1].path == "copy/COMMON.cpy"

    @pytest.mark.asyncio
    async def test_scan_directory_with_filtering(self):
        """Test directory scan with extension filtering."""
        client = TreeMCPClient(docker_image="tree-mcp:test", extensions=[".cbl", ".cob"])

        # Create mock session
        mock_session = AsyncMock()
        mock_result = Mock()
        mock_text = Mock()
        mock_text.text = json.dumps({
            "success": True,
            "json_data": [
                {"type": "file", "name": "MAINPROG.cbl"},
                {"type": "file", "name": "README.md"},
                {"type": "file", "name": "SUBPROG.cob"},
            ]
        })
        mock_result.content = [mock_text]
        mock_session.call_tool = AsyncMock(return_value=mock_result)

        mock_mcp_client = Mock()
        mock_mcp_client.get_session.return_value = mock_session
        mock_mcp_client.create_all_sessions = AsyncMock()

        with patch('tree_mcp_client.MCPClient') as MockMCPClient:
            MockMCPClient.from_dict.return_value = mock_mcp_client

            result = await client.scan_directory("/test/project")

        assert result.success is True
        assert result.total_files == 2
        assert all(f.extension in [".cbl", ".cob"] for f in result.files)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
