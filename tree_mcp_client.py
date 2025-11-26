"""
Tree MCP Client for Project Directory Scanning

This module provides a client for the Tree MCP server which runs in Docker
and provides directory tree scanning functionality.

The client:
- Communicates with the Tree MCP server via Docker stdio
- Scans project directories for COBOL files
- Returns structured file lists for orchestrator consumption
- Supports JSON output for machine-readable results
"""

import asyncio
import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field

from mcp_use import MCPClient

logger = logging.getLogger(__name__)


@dataclass
class FileInfo:
    """Information about a discovered file."""
    name: str
    path: str  # Relative path from project root
    absolute_path: str
    extension: str
    size: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "name": self.name,
            "path": self.path,
            "absolute_path": self.absolute_path,
            "extension": self.extension,
            "size": self.size,
        }


@dataclass
class TreeScanResult:
    """Result of a directory tree scan."""
    success: bool
    project_path: str
    files: List[FileInfo] = field(default_factory=list)
    total_files: int = 0
    error: Optional[str] = None
    raw_json: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "success": self.success,
            "project_path": self.project_path,
            "files": [f.to_dict() for f in self.files],
            "total_files": self.total_files,
            "error": self.error,
        }

    def get_file_paths(self) -> List[str]:
        """Get list of absolute file paths."""
        return [f.absolute_path for f in self.files]

    def get_relative_paths(self) -> List[str]:
        """Get list of relative file paths."""
        return [f.path for f in self.files]


class TreeMCPClient:
    """
    Client for Tree MCP server to scan project directories.

    This client uses the mcp-use library to communicate with a Docker-based
    Tree MCP server for scanning COBOL project directories.
    """

    def __init__(
        self,
        docker_image: str,
        extensions: Optional[List[str]] = None,
        exclude_dirs: Optional[List[str]] = None,
        max_depth: Optional[int] = None,
    ):
        """
        Initialize Tree MCP Client.

        Args:
            docker_image: Docker image name for Tree MCP server (required, from config)
            extensions: List of file extensions to include (e.g., [".cbl", ".cob"])
            exclude_dirs: List of directories to exclude (e.g., [".git", "node_modules"])
            max_depth: Maximum directory depth to scan (None = unlimited)
        """
        if not docker_image:
            raise ValueError("docker_image is required - configure it in your config.yaml under tree_server.docker_image")
        self.docker_image = docker_image
        self.extensions = extensions or [
            ".cbl", ".CBL", ".cob", ".COB", ".cpy", ".CPY", ".c74", ".C74"
        ]
        self.exclude_dirs = exclude_dirs or [
            ".git", "node_modules", "__pycache__", ".venv"
        ]
        self.max_depth = max_depth
        self.mcp_client: Optional[MCPClient] = None
        self._session_active = False

    def _get_mcp_config(self, project_path: str) -> Dict[str, Any]:
        """
        Generate MCP configuration for Docker-based Tree server.

        Args:
            project_path: Absolute path to project directory

        Returns:
            Configuration dict for MCPClient.from_dict()
        """
        return {
            "mcpServers": {
                "tree": {
                    "command": "docker",
                    "args": [
                        "run",
                        "-i",
                        "--rm",
                        "-v", f"{project_path}:/workspace:ro",
                        self.docker_image
                    ]
                }
            }
        }

    async def initialize(self, project_path: str) -> None:
        """
        Initialize MCP client and create session.

        Args:
            project_path: Absolute path to project directory
        """
        if self._session_active:
            logger.warning("Session already active, skipping initialization")
            return

        logger.info(f"Initializing Tree MCP client for: {project_path}")

        # Create MCP client from config
        mcp_config = self._get_mcp_config(project_path)
        logger.debug(f"MCP Configuration: {json.dumps(mcp_config, indent=2)}")

        self.mcp_client = MCPClient.from_dict(mcp_config)

        # Create session (starts Docker container)
        logger.info("Creating MCP session (starting Docker container)...")
        await self.mcp_client.create_all_sessions()
        self._session_active = True
        logger.info("Tree MCP session created and ready")

    async def cleanup(self) -> None:
        """Cleanup MCP session (Docker container cleaned up via --rm)."""
        if self.mcp_client and self._session_active:
            logger.info("Cleaning up Tree MCP session...")
            # Docker container will auto-cleanup via --rm flag
            self._session_active = False
            logger.info("Tree MCP session closed")

    async def scan_directory(self, project_path: str) -> TreeScanResult:
        """
        Scan a project directory for COBOL files.

        Args:
            project_path: Path to the project directory

        Returns:
            TreeScanResult containing list of discovered files
        """
        project_path = str(Path(project_path).absolute())
        logger.info(f"Scanning directory: {project_path}")

        try:
            # Initialize if not already done
            if not self._session_active:
                await self.initialize(project_path)

            session = self.mcp_client.get_session("tree")

            # Build tool arguments
            tool_args = {
                "path": "/workspace",  # Docker-mounted path
            }

            if self.max_depth is not None:
                tool_args["max_depth"] = self.max_depth

            # Call tree_json_output for structured data
            logger.info("Calling tree_json_output tool...")
            result = await session.call_tool("tree_json_output", tool_args)

            # Parse the result
            json_data = self._extract_json_from_result(result)

            if json_data is None:
                return TreeScanResult(
                    success=False,
                    project_path=project_path,
                    error="Failed to parse JSON output from Tree MCP server",
                )

            # Extract files from JSON tree structure
            files = self._extract_files_from_tree(json_data, project_path)

            # Filter by extensions
            filtered_files = self._filter_by_extensions(files)

            logger.info(f"Found {len(filtered_files)} COBOL files out of {len(files)} total files")

            return TreeScanResult(
                success=True,
                project_path=project_path,
                files=filtered_files,
                total_files=len(filtered_files),
                raw_json=json_data,
            )

        except Exception as e:
            logger.error(f"Error scanning directory: {e}")
            return TreeScanResult(
                success=False,
                project_path=project_path,
                error=str(e),
            )

        finally:
            await self.cleanup()

    def _extract_json_from_result(self, result: Any) -> Optional[Dict[str, Any]]:
        """
        Extract JSON data from MCP tool result.

        Args:
            result: Result from MCP tool call

        Returns:
            Parsed JSON data or None if parsing fails
        """
        try:
            # Handle CallToolResult from mcp-use
            if hasattr(result, 'content'):
                content_items = result.content
                if content_items and len(content_items) > 0:
                    first_item = content_items[0]
                    if hasattr(first_item, 'text'):
                        # Parse the text as JSON
                        data = json.loads(first_item.text)
                        # tree command returns result with json_data field
                        if isinstance(data, dict) and "json_data" in data:
                            return data["json_data"]
                        return data
            elif isinstance(result, dict):
                if "json_data" in result:
                    return result["json_data"]
                return result
            return None
        except (json.JSONDecodeError, AttributeError) as e:
            logger.error(f"Failed to parse JSON result: {e}")
            return None

    def _extract_files_from_tree(
        self,
        tree_data: Any,
        project_path: str,
        current_path: str = ""
    ) -> List[FileInfo]:
        """
        Recursively extract file information from tree JSON structure.

        The tree command JSON format is:
        [{"type": "directory", "name": "dir", "contents": [...]},
         {"type": "file", "name": "file.cbl"}, ...]

        Args:
            tree_data: JSON tree data (list or dict)
            project_path: Absolute path to project root
            current_path: Current relative path (for recursion)

        Returns:
            List of FileInfo objects
        """
        files = []

        # Handle list of entries
        if isinstance(tree_data, list):
            for item in tree_data:
                files.extend(self._extract_files_from_tree(item, project_path, current_path))
            return files

        # Handle single entry (dict)
        if not isinstance(tree_data, dict):
            return files

        item_type = tree_data.get("type", "")
        item_name = tree_data.get("name", "")

        if item_type == "file":
            # Build paths
            rel_path = f"{current_path}/{item_name}" if current_path else item_name
            abs_path = str(Path(project_path) / rel_path)

            # Get extension
            ext = Path(item_name).suffix

            files.append(FileInfo(
                name=item_name,
                path=rel_path,
                absolute_path=abs_path,
                extension=ext,
                size=tree_data.get("size"),
            ))

        elif item_type == "directory":
            # Skip excluded directories
            if item_name in self.exclude_dirs:
                logger.debug(f"Skipping excluded directory: {item_name}")
                return files

            # Recurse into directory contents
            contents = tree_data.get("contents", [])
            new_path = f"{current_path}/{item_name}" if current_path else item_name

            for content in contents:
                files.extend(self._extract_files_from_tree(content, project_path, new_path))

        # Handle report entry (tree command adds this at the end)
        elif item_type == "report":
            pass  # Skip report entries

        return files

    def _filter_by_extensions(self, files: List[FileInfo]) -> List[FileInfo]:
        """
        Filter files by configured extensions.

        Args:
            files: List of all files

        Returns:
            List of files matching configured extensions
        """
        if not self.extensions:
            return files

        # Normalize extensions (ensure they start with '.')
        normalized_exts = set()
        for ext in self.extensions:
            if not ext.startswith('.'):
                ext = '.' + ext
            normalized_exts.add(ext.lower())

        filtered = []
        for file in files:
            if file.extension.lower() in normalized_exts:
                filtered.append(file)
            else:
                logger.debug(f"Filtered out file: {file.name} (extension: {file.extension})")

        return filtered

    def write_file_list(self, scan_result: TreeScanResult, output_path: str) -> None:
        """
        Write scan results to a JSON file.

        Args:
            scan_result: Result from scan_directory
            output_path: Path to output JSON file
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w') as f:
            json.dump(scan_result.to_dict(), f, indent=2)

        logger.info(f"File list written to: {output_path}")


async def scan_project_directory(
    project_path: str,
    docker_image: str,
    extensions: Optional[List[str]] = None,
    exclude_dirs: Optional[List[str]] = None,
    max_depth: Optional[int] = None,
    output_file: Optional[str] = None,
) -> TreeScanResult:
    """
    Convenience function to scan a project directory.

    Args:
        project_path: Path to project directory
        docker_image: Docker image for Tree MCP server (required, from config)
        extensions: File extensions to include
        exclude_dirs: Directories to exclude
        max_depth: Maximum scan depth
        output_file: Optional path to write results JSON

    Returns:
        TreeScanResult containing discovered files
    """
    client = TreeMCPClient(
        docker_image=docker_image,
        extensions=extensions,
        exclude_dirs=exclude_dirs,
        max_depth=max_depth,
    )

    result = await client.scan_directory(project_path)

    if output_file:
        client.write_file_list(result, output_file)

    return result


def scan_project_directory_sync(
    project_path: str,
    docker_image: str,
    extensions: Optional[List[str]] = None,
    exclude_dirs: Optional[List[str]] = None,
    max_depth: Optional[int] = None,
    output_file: Optional[str] = None,
) -> TreeScanResult:
    """
    Synchronous wrapper for scan_project_directory.

    Args:
        project_path: Path to project directory
        docker_image: Docker image for Tree MCP server (required, from config)
        extensions: File extensions to include
        exclude_dirs: Directories to exclude
        max_depth: Maximum scan depth
        output_file: Optional path to write results JSON

    Returns:
        TreeScanResult containing discovered files
    """
    return asyncio.run(scan_project_directory(
        project_path=project_path,
        docker_image=docker_image,
        extensions=extensions,
        exclude_dirs=exclude_dirs,
        max_depth=max_depth,
        output_file=output_file,
    ))


# CLI for testing
if __name__ == "__main__":
    import sys

    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    async def main():
        if len(sys.argv) < 2:
            print("Usage: python tree_mcp_client.py <project_path> [output_file]")
            print("Example: python tree_mcp_client.py /home/user/cobol-project ./metadata/file_list.json")
            sys.exit(1)

        project_path = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None

        print(f"\n{'='*70}")
        print(f"Scanning COBOL Project: {project_path}")
        print(f"{'='*70}\n")

        result = await scan_project_directory(
            project_path=project_path,
            output_file=output_file,
        )

        if result.success:
            print(f"\n{'='*70}")
            print(f"Scan Complete: Found {result.total_files} COBOL files")
            print(f"{'='*70}\n")

            for file in result.files:
                print(f"  - {file.path}")

            if output_file:
                print(f"\nResults written to: {output_file}")
        else:
            print(f"\nScan Failed: {result.error}")
            sys.exit(1)

    asyncio.run(main())
