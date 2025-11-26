"""
Project-Level Metadata Generator for COBOL Documentation Orchestrator

This module extends the base MCP metadata generator to support:
- Project-level metadata generation (relationships, cross-references, CFG)
- Batch file processing for multiple COBOL files
- Structured metadata storage in ./metadata directory
- Integration with Tree MCP client for file discovery

The generator runs MCP tools in two phases:
1. Per-file phase: Generate metadata for each file individually
2. Project phase: Generate project-wide relationships and call graphs
"""

import asyncio
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from mcp_use import MCPClient

from tree_mcp_client import TreeMCPClient, TreeScanResult, FileInfo

logger = logging.getLogger(__name__)


@dataclass
class MetadataResult:
    """Result of metadata generation for a single file or project."""
    success: bool
    file_path: Optional[str] = None
    program_name: Optional[str] = None
    metadata_files: List[str] = field(default_factory=list)
    error: Optional[str] = None
    duration_seconds: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "file_path": self.file_path,
            "program_name": self.program_name,
            "metadata_files": self.metadata_files,
            "error": self.error,
            "duration_seconds": self.duration_seconds,
        }


@dataclass
class ProjectMetadataResult:
    """Result of project-level metadata generation."""
    success: bool
    project_path: str
    total_files: int = 0
    successful_files: int = 0
    failed_files: int = 0
    file_results: List[MetadataResult] = field(default_factory=list)
    project_metadata_files: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    duration_seconds: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "project_path": self.project_path,
            "total_files": self.total_files,
            "successful_files": self.successful_files,
            "failed_files": self.failed_files,
            "file_results": [r.to_dict() for r in self.file_results],
            "project_metadata_files": self.project_metadata_files,
            "errors": self.errors,
            "duration_seconds": self.duration_seconds,
        }


class ProjectMetadataGenerator:
    """
    Generates metadata for an entire COBOL project using MCP servers.

    This class orchestrates metadata generation for:
    - Per-file metadata: CTags outlines, GnuCOBOL analysis, SuperBOL symbols/CFG
    - Project-level metadata: Relationships, cross-references, project CFG

    Directory Structure:
    ./metadata/
    ├── file_list.json              # List of all COBOL files in project
    ├── project_metadata.json       # Project-level summary
    ├── ctags/
    │   ├── project-symbols.json    # Project-wide symbols
    │   ├── project-outline.json    # Project-wide outline
    │   └── {program}-outline.json  # Per-file outlines
    ├── gnucobol/
    │   ├── project-relationships.json  # Project-wide relationships
    │   ├── project-cross-refs.json     # Project-wide cross-references
    │   └── {program}-analysis.json     # Per-file analysis
    └── superbol/
        ├── project-cfg.json            # Project-wide CFG
        ├── {program}-symbols.json      # Per-file symbols
        └── cfg/
            └── {program}-cfg.json      # Per-file CFG
    """

    def __init__(
        self,
        project_path: str,
        metadata_dir: str,
        servers_config: Dict[str, Any],
        tree_server_config: Optional[Dict[str, Any]] = None,
        copybook_paths: Optional[List[str]] = None,
    ):
        """
        Initialize Project Metadata Generator.

        Args:
            project_path: Path to the COBOL project directory
            metadata_dir: Directory to store generated metadata
            servers_config: MCP servers configuration (ctags, gnuCobol, superbol-lsp)
            tree_server_config: Tree MCP server configuration
            copybook_paths: List of directories containing copybooks
        """
        self.project_path = Path(project_path).absolute()
        self.metadata_dir = Path(metadata_dir).absolute()
        self.servers_config = servers_config
        self.tree_server_config = tree_server_config or {}
        self.copybook_paths = copybook_paths or []

        self.mcp_client: Optional[MCPClient] = None
        self._session_active = False

        # Discovered files
        self.cobol_files: List[FileInfo] = []

    def _ensure_directories(self) -> None:
        """Create required metadata directory structure."""
        dirs = [
            self.metadata_dir,
            self.metadata_dir / "ctags",
            self.metadata_dir / "gnucobol",
            self.metadata_dir / "superbol",
            self.metadata_dir / "superbol" / "cfg",
        ]
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)
        logger.info(f"Metadata directories created at: {self.metadata_dir}")

    def _get_mcp_config(self) -> Dict[str, Any]:
        """Generate MCP configuration for Docker-based servers."""
        ctags_image = self.servers_config.get('ctags', {}).get('docker_image')
        gnucobol_image = self.servers_config.get('gnuCobol', {}).get('docker_image')
        superbol_image = self.servers_config.get('superbol-lsp', {}).get('docker_image')

        if not ctags_image:
            raise ValueError("Missing required config: servers.ctags.docker_image")
        if not gnucobol_image:
            raise ValueError("Missing required config: servers.gnuCobol.docker_image")
        if not superbol_image:
            raise ValueError("Missing required config: servers.superbol-lsp.docker_image")

        # Build volume mounts for copybook paths
        gnucobol_args = [
            "run", "-i", "--rm",
            "-v", f"{self.project_path}:/workspace:ro",
            "-v", f"{self.metadata_dir / 'gnucobol'}:/output",
        ]
        # Add copybook path mounts
        for i, cp_path in enumerate(self.copybook_paths):
            gnucobol_args.extend(["-v", f"{Path(cp_path).absolute()}:/copybooks{i}:ro"])
        gnucobol_args.append(gnucobol_image)

        return {
            "mcpServers": {
                "ctags": {
                    "command": "docker",
                    "args": [
                        "run", "-i", "--rm",
                        "-v", f"{self.project_path}:/workspace:ro",
                        "-v", f"{self.metadata_dir / 'ctags'}:/output",
                        ctags_image
                    ]
                },
                "gnucobol": {
                    "command": "docker",
                    "args": gnucobol_args
                },
                "superbol": {
                    "command": "docker",
                    "args": [
                        "run", "-i", "--rm",
                        "-v", f"{self.project_path}:/workspace:ro",
                        "-v", f"{self.metadata_dir / 'superbol'}:/output",
                        superbol_image
                    ]
                }
            }
        }

    async def initialize(self) -> None:
        """Initialize MCP client and create sessions."""
        if self._session_active:
            logger.warning("Sessions already active")
            return

        self._ensure_directories()

        logger.info("Initializing MCP Metadata Generator...")
        mcp_config = self._get_mcp_config()
        logger.debug(f"MCP Config: {json.dumps(mcp_config, indent=2)}")

        self.mcp_client = MCPClient.from_dict(mcp_config)
        await self.mcp_client.create_all_sessions()
        self._session_active = True
        logger.info("MCP sessions created and ready")

    async def cleanup(self) -> None:
        """Cleanup MCP sessions."""
        if self._session_active:
            logger.info("Cleaning up MCP sessions...")
            self._session_active = False
            logger.info("Sessions closed")

    async def discover_files(self) -> TreeScanResult:
        """
        Discover COBOL files in the project using Tree MCP server.

        Returns:
            TreeScanResult containing discovered files
        """
        logger.info(f"Discovering COBOL files in: {self.project_path}")

        docker_image = self.tree_server_config.get("docker_image")
        if not docker_image:
            raise ValueError("tree_server.docker_image is required in config")

        tree_client = TreeMCPClient(
            docker_image=docker_image,
            extensions=self.tree_server_config.get("extensions"),
            exclude_dirs=self.tree_server_config.get("exclude_dirs"),
            max_depth=self.tree_server_config.get("max_depth"),
        )

        result = await tree_client.scan_directory(str(self.project_path))

        if result.success:
            self.cobol_files = result.files
            # Save file list to metadata directory
            tree_client.write_file_list(result, str(self.metadata_dir / "file_list.json"))
            logger.info(f"Discovered {len(self.cobol_files)} COBOL files")
        else:
            logger.error(f"File discovery failed: {result.error}")

        return result

    async def generate_per_file_metadata(
        self,
        file_info: FileInfo,
        generate_ctags: bool = True,
        generate_gnucobol: bool = True,
        generate_superbol: bool = True,
    ) -> MetadataResult:
        """
        Generate metadata for a single COBOL file.

        Args:
            file_info: FileInfo object for the file
            generate_ctags: Whether to generate CTags metadata
            generate_gnucobol: Whether to generate GnuCOBOL metadata
            generate_superbol: Whether to generate SuperBOL metadata

        Returns:
            MetadataResult with generated file paths
        """
        start_time = datetime.now()
        program_name = Path(file_info.name).stem
        # file_info.path already contains /workspace/ prefix from Tree MCP
        # Use it directly without adding another prefix
        docker_file_path = file_info.path if file_info.path.startswith("/workspace") else f"/workspace/{file_info.path}"
        metadata_files = []
        errors = []

        logger.info(f"Generating metadata for: {program_name}")

        try:
            # CTags: Generate per-file outline
            if generate_ctags:
                try:
                    ctags_session = self.mcp_client.get_session("ctags")

                    # First generate tags for this file (JSON format)
                    await ctags_session.call_tool(
                        "generate_tags",
                        {
                            "path": docker_file_path,
                            "language": "cobol",
                            "output_format": "json",
                            "output_file": f"/output/{program_name}.tags"
                        }
                    )

                    # Then get file outline
                    outline_result = await ctags_session.call_tool(
                        "get_file_outline",
                        {
                            "file_path": docker_file_path,
                            "tags_file": f"/output/{program_name}.tags"
                        }
                    )

                    outline_path = self.metadata_dir / "ctags" / f"ctags-{program_name}-outline.json"
                    self._write_json(outline_result, outline_path)
                    metadata_files.append(str(outline_path))
                    logger.debug(f"  CTags outline: {outline_path.name}")

                except Exception as e:
                    errors.append(f"CTags error: {e}")
                    logger.warning(f"  CTags failed: {e}")

            # GnuCOBOL: Generate per-file relationships and cross-references
            if generate_gnucobol:
                try:
                    gnucobol_session = self.mcp_client.get_session("gnucobol")

                    # Per-file relationship extraction
                    rel_result = await gnucobol_session.call_tool(
                        "extract_relationships",
                        {
                            "file_path": docker_file_path,
                            "copybook_paths": [f"/copybooks{i}" for i in range(len(self.copybook_paths))]
                        }
                    )

                    rel_path = self.metadata_dir / "gnucobol" / f"gnucobol-{program_name}-relationships.json"
                    self._write_json(rel_result, rel_path)
                    metadata_files.append(str(rel_path))
                    logger.debug(f"  GnuCOBOL relationships: {rel_path.name}")

                    # Cross-references
                    xref_result = await gnucobol_session.call_tool(
                        "extract_cross_references_tool",
                        {
                            "file_path": docker_file_path,
                            "copybook_paths": [f"/copybooks{i}" for i in range(len(self.copybook_paths))],
                            "skip_compiler": True  # Use regex for speed
                        }
                    )

                    xref_path = self.metadata_dir / "gnucobol" / f"gnucobol-{program_name}-cross-refs.json"
                    self._write_json(xref_result, xref_path)
                    metadata_files.append(str(xref_path))
                    logger.debug(f"  GnuCOBOL cross-refs: {xref_path.name}")

                except Exception as e:
                    errors.append(f"GnuCOBOL error: {e}")
                    logger.warning(f"  GnuCOBOL failed: {e}")

            # SuperBOL: Generate per-file symbols and CFG
            if generate_superbol:
                try:
                    superbol_session = self.mcp_client.get_session("superbol")

                    # Document symbols
                    symbols_result = await superbol_session.call_tool(
                        "code_document_symbols",
                        {
                            "file_path": docker_file_path,
                            "language": "cobol"
                        }
                    )

                    symbols_path = self.metadata_dir / "superbol" / f"superbol-{program_name}-symbols.json"
                    self._write_json(symbols_result, symbols_path)
                    metadata_files.append(str(symbols_path))
                    logger.debug(f"  SuperBOL symbols: {symbols_path.name}")

                    # Per-file CFG
                    cfg_result = await superbol_session.call_tool(
                        "cobol_generate_cfg_file",
                        {
                            "file_path": docker_file_path,
                            "output_format": "json",
                            "output_file": f"/output/cfg/{program_name}-cfg.json"
                        }
                    )
                    cfg_path = self.metadata_dir / "superbol" / "cfg" / f"{program_name}-cfg.json"
                    metadata_files.append(str(cfg_path))
                    logger.debug(f"  SuperBOL CFG: {cfg_path.name}")

                except Exception as e:
                    errors.append(f"SuperBOL error: {e}")
                    logger.warning(f"  SuperBOL failed: {e}")

            duration = (datetime.now() - start_time).total_seconds()

            return MetadataResult(
                success=len(errors) == 0,
                file_path=file_info.absolute_path,
                program_name=program_name,
                metadata_files=metadata_files,
                error="; ".join(errors) if errors else None,
                duration_seconds=duration,
            )

        except Exception as e:
            duration = (datetime.now() - start_time).total_seconds()
            logger.error(f"Failed to generate metadata for {program_name}: {e}")
            return MetadataResult(
                success=False,
                file_path=file_info.absolute_path,
                program_name=program_name,
                error=str(e),
                duration_seconds=duration,
            )

    async def generate_project_metadata(self) -> List[str]:
        """
        Generate project-level metadata (relationships, CFG, cross-references).

        This should be called after all per-file metadata has been generated.

        Returns:
            List of generated project metadata file paths
        """
        logger.info("Generating project-level metadata...")
        metadata_files = []

        try:
            # SuperBOL: Project-wide CFG
            logger.info("  Generating project CFG (SuperBOL)...")
            superbol_session = self.mcp_client.get_session("superbol")

            # Build glob pattern from configured extensions
            # The tool expects patterns like "**/*.cbl" for recursive search
            extensions = self.tree_server_config.get("extensions", [".cbl", ".CBL", ".cob", ".COB", ".cpy", ".CPY"])
            # Use recursive glob pattern to find all COBOL files in subdirectories
            # Pattern should be "**/*.cbl" to match files in any subdirectory
            file_pattern = "**/*" + extensions[0] if extensions else "**/*.cbl"

            cfg_result = await superbol_session.call_tool(
                "cobol_generate_cfg_project",
                {
                    "file_pattern": file_pattern,
                    "output_format": "json",
                    "output_dir": "/output/cfg"
                }
            )

            project_cfg_path = self.metadata_dir / "superbol" / "project-cfg.json"
            self._write_json(cfg_result, project_cfg_path)
            metadata_files.append(str(project_cfg_path))
            logger.info(f"    Project CFG: {project_cfg_path.name}")

        except Exception as e:
            logger.warning(f"  SuperBOL project CFG failed: {e}")

        try:
            # GnuCOBOL: Project-wide relationship extraction (directory mode)
            logger.info("  Generating project relationships (GnuCOBOL)...")
            gnucobol_session = self.mcp_client.get_session("gnucobol")

            rel_result = await gnucobol_session.call_tool(
                "extract_relationships",
                {
                    "directory": "/workspace",
                    "recursive": True,
                    "copybook_paths": [f"/copybooks{i}" for i in range(len(self.copybook_paths))],
                    "max_files": 500  # Increase limit for large projects
                }
            )

            project_rel_path = self.metadata_dir / "gnucobol" / "project-relationships.json"
            self._write_json(rel_result, project_rel_path)
            metadata_files.append(str(project_rel_path))
            logger.info(f"    Project relationships: {project_rel_path.name}")

        except Exception as e:
            logger.warning(f"  GnuCOBOL project relationships failed: {e}")

        try:
            # CTags: Project-wide symbols and outline
            logger.info("  Generating project symbols (CTags)...")
            ctags_session = self.mcp_client.get_session("ctags")

            # Generate tags for all files
            # f.path already contains /workspace/ prefix from Tree MCP
            file_paths = [f.path if f.path.startswith("/workspace") else f"/workspace/{f.path}" for f in self.cobol_files]
            await ctags_session.call_tool(
                "generate_tags",
                {
                    "path": " ".join(file_paths),
                    "language": "cobol",
                    "output_format": "json",
                    "output_file": "/output/project.tags"
                }
            )

            # Project symbols
            symbols_result = await ctags_session.call_tool(
                "generate_project_symbols",
                {
                    "tags_file": "/output/project.tags",
                    "languages": ["cobol"]
                }
            )

            project_symbols_path = self.metadata_dir / "ctags" / "project-symbols.json"
            self._write_json(symbols_result, project_symbols_path)
            metadata_files.append(str(project_symbols_path))
            logger.info(f"    Project symbols: {project_symbols_path.name}")

            # Project outline
            outline_result = await ctags_session.call_tool(
                "generate_project_outline",
                {
                    "tags_file": "/output/project.tags",
                    "max_depth": 10
                }
            )

            project_outline_path = self.metadata_dir / "ctags" / "project-outline.json"
            self._write_json(outline_result, project_outline_path)
            metadata_files.append(str(project_outline_path))
            logger.info(f"    Project outline: {project_outline_path.name}")

        except Exception as e:
            logger.warning(f"  CTags project metadata failed: {e}")

        return metadata_files

    async def generate_all_metadata(
        self,
        files: Optional[List[FileInfo]] = None,
        skip_discovery: bool = False,
    ) -> ProjectMetadataResult:
        """
        Generate all metadata for the project.

        Args:
            files: Optional list of files to process (uses discovered files if None)
            skip_discovery: Skip file discovery (use provided files or previously discovered)

        Returns:
            ProjectMetadataResult with all generation results
        """
        start_time = datetime.now()
        errors = []

        try:
            # Initialize MCP sessions
            await self.initialize()

            # Discover files if needed
            if not skip_discovery and files is None:
                discovery_result = await self.discover_files()
                if not discovery_result.success:
                    return ProjectMetadataResult(
                        success=False,
                        project_path=str(self.project_path),
                        errors=[f"File discovery failed: {discovery_result.error}"],
                        duration_seconds=(datetime.now() - start_time).total_seconds(),
                    )

            # Use provided files or discovered files
            files_to_process = files or self.cobol_files

            if not files_to_process:
                return ProjectMetadataResult(
                    success=False,
                    project_path=str(self.project_path),
                    errors=["No COBOL files to process"],
                    duration_seconds=(datetime.now() - start_time).total_seconds(),
                )

            logger.info(f"Processing {len(files_to_process)} COBOL files...")

            # Phase 1: Generate per-file metadata
            file_results = []
            for file_info in files_to_process:
                result = await self.generate_per_file_metadata(file_info)
                file_results.append(result)
                if not result.success:
                    errors.append(f"{result.program_name}: {result.error}")

            # Phase 2: Generate project-level metadata
            project_metadata_files = []
            if len(files_to_process) > 1:  # Only for multi-file projects
                project_metadata_files = await self.generate_project_metadata()
            else:
                logger.info("Skipping project-level metadata (single file)")

            # Calculate statistics
            successful = sum(1 for r in file_results if r.success)
            failed = len(file_results) - successful

            # Write project metadata summary
            duration = (datetime.now() - start_time).total_seconds()
            result = ProjectMetadataResult(
                success=failed == 0,
                project_path=str(self.project_path),
                total_files=len(files_to_process),
                successful_files=successful,
                failed_files=failed,
                file_results=file_results,
                project_metadata_files=project_metadata_files,
                errors=errors,
                duration_seconds=duration,
            )

            # Save project metadata summary
            summary_path = self.metadata_dir / "project_metadata.json"
            with open(summary_path, 'w') as f:
                json.dump(result.to_dict(), f, indent=2)
            logger.info(f"Project metadata summary: {summary_path}")

            logger.info(f"Metadata generation complete: {successful}/{len(files_to_process)} files successful")
            return result

        except Exception as e:
            logger.error(f"Metadata generation failed: {e}")
            return ProjectMetadataResult(
                success=False,
                project_path=str(self.project_path),
                errors=[str(e)],
                duration_seconds=(datetime.now() - start_time).total_seconds(),
            )

        finally:
            await self.cleanup()

    def _write_json(self, data: Any, path: Path) -> None:
        """Write JSON data to file, handling MCP result objects."""
        path.parent.mkdir(parents=True, exist_ok=True)

        # Handle CallToolResult from mcp-use
        if hasattr(data, 'content'):
            content_items = data.content
            if content_items and len(content_items) > 0:
                first_item = content_items[0]
                if hasattr(first_item, 'text'):
                    try:
                        json_data = json.loads(first_item.text)
                        with open(path, 'w') as f:
                            json.dump(json_data, f, indent=2)
                        return
                    except json.JSONDecodeError:
                        with open(path, 'w') as f:
                            f.write(first_item.text)
                        return
                else:
                    with open(path, 'w') as f:
                        json.dump({"content": str(first_item)}, f, indent=2)
                    return
            else:
                with open(path, 'w') as f:
                    json.dump({"error": "Empty result"}, f, indent=2)
                return

        # Regular dict/list
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)


# Synchronous wrapper for integration
def generate_project_metadata_sync(
    project_path: str,
    metadata_dir: str,
    servers_config: Dict[str, Any],
    tree_server_config: Optional[Dict[str, Any]] = None,
    copybook_paths: Optional[List[str]] = None,
) -> ProjectMetadataResult:
    """
    Synchronous wrapper for project metadata generation.

    Args:
        project_path: Path to COBOL project directory
        metadata_dir: Directory for metadata output
        servers_config: MCP servers configuration
        tree_server_config: Tree MCP server configuration
        copybook_paths: Copybook directories

    Returns:
        ProjectMetadataResult
    """
    generator = ProjectMetadataGenerator(
        project_path=project_path,
        metadata_dir=metadata_dir,
        servers_config=servers_config,
        tree_server_config=tree_server_config,
        copybook_paths=copybook_paths,
    )
    return asyncio.run(generator.generate_all_metadata())


# CLI for testing
if __name__ == "__main__":
    import sys
    from config_loader import load_config

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    async def main():
        if len(sys.argv) < 3:
            print("Usage: python project_metadata_generator.py --config <config.yaml> <project_path> [metadata_dir]")
            print("Example: python project_metadata_generator.py --config config-74.yaml /home/user/cobol-project ./metadata")
            sys.exit(1)

        # Parse arguments
        if sys.argv[1] != "--config":
            print("Error: First argument must be --config <config.yaml>")
            sys.exit(1)

        config_path = sys.argv[2]
        project_path = sys.argv[3]
        metadata_dir = sys.argv[4] if len(sys.argv) > 4 else None

        # Load configuration
        try:
            config = load_config(config_path)
            print(f"Loaded configuration from: {config_path}")
        except FileNotFoundError:
            print(f"Error: Configuration file not found: {config_path}")
            sys.exit(1)
        except Exception as e:
            print(f"Error loading configuration: {e}")
            sys.exit(1)

        # Get server configs from config file
        servers_config = config.get_servers_config()
        tree_config = config.get_tree_server_config()

        # Validate required Docker images
        missing = []
        if not servers_config.get("ctags", {}).get("docker_image"):
            missing.append("servers.ctags.docker_image")
        if not servers_config.get("gnuCobol", {}).get("docker_image"):
            missing.append("servers.gnuCobol.docker_image")
        if not servers_config.get("superbol-lsp", {}).get("docker_image"):
            missing.append("servers.superbol-lsp.docker_image")
        if not tree_config.get("docker_image"):
            missing.append("tree_server.docker_image")

        if missing:
            print(f"Error: Missing required Docker image configurations in {config_path}:")
            for m in missing:
                print(f"  - {m}")
            sys.exit(1)

        # Get metadata_dir from config if not provided
        if not metadata_dir:
            output_config = config.get_output_config()
            metadata_dir = output_config.get("metadata_dir", "./metadata")

        print(f"\n{'='*70}")
        print(f"Project Metadata Generator")
        print(f"{'='*70}")
        print(f"Config:  {config_path}")
        print(f"Project: {project_path}")
        print(f"Output:  {metadata_dir}")
        print(f"{'='*70}\n")

        generator = ProjectMetadataGenerator(
            project_path=project_path,
            metadata_dir=metadata_dir,
            servers_config=servers_config,
            tree_server_config=tree_config,
        )

        result = await generator.generate_all_metadata()

        print(f"\n{'='*70}")
        print(f"Results")
        print(f"{'='*70}")
        print(f"Success: {result.success}")
        print(f"Files processed: {result.total_files}")
        print(f"Successful: {result.successful_files}")
        print(f"Failed: {result.failed_files}")
        print(f"Duration: {result.duration_seconds:.2f}s")

        if result.errors:
            print(f"\nErrors:")
            for error in result.errors:
                print(f"  - {error}")

    asyncio.run(main())
