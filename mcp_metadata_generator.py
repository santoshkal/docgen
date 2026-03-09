"""
MCP Metadata Generator for COBOL Documentation Agent

Uses mcp-use library to interact with Docker-based MCP servers:
- ctags-mcp-server
- gnucobol-mcp-server
- superbol-lsp-mcp-server

The mcp-use library handles:
- Starting Docker containers via docker run
- stdio communication
- Container cleanup (via --rm flag)
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

from mcp_use import MCPClient


class MCPMetadataGenerator:
    """
    Generates metadata for COBOL programs using MCP servers
    """

    def __init__(self, workspace_path: str, output_base_dir: str, servers_config: Dict[str, Any] = None):
        self.workspace_path = Path(workspace_path).absolute()
        self.output_base_dir = Path(output_base_dir).absolute()
        self.mcp_client: MCPClient = None
        self.servers_config = servers_config or {}

    def get_mcp_config(self) -> Dict[str, Any]:
        """
        Generate mcp-use configuration for Docker-based MCP servers

        Returns configuration dict for MCPClient.from_dict()
        """
        # Ensure output directories exist
        (self.output_base_dir / "ctags").mkdir(parents=True, exist_ok=True)
        (self.output_base_dir / "gnucobol").mkdir(parents=True, exist_ok=True)
        (self.output_base_dir / "superbol").mkdir(parents=True, exist_ok=True)
        (self.output_base_dir / "superbol" / "superbol-cfg").mkdir(parents=True, exist_ok=True)

        # Get Docker image names from config (required - no defaults)
        ctags_image = self.servers_config.get('ctags', {}).get('docker_image')
        gnucobol_image = self.servers_config.get('gnuCobol', {}).get('docker_image')
        superbol_image = self.servers_config.get('superbol-lsp', {}).get('docker_image')

        # Validate that all required docker images are configured
        if not ctags_image:
            raise ValueError("Missing required config: servers.ctags.docker_image")
        if not gnucobol_image:
            raise ValueError("Missing required config: servers.gnuCobol.docker_image")
        if not superbol_image:
            raise ValueError("Missing required config: servers.superbol-lsp.docker_image")

        config = {
            "mcpServers": {
                "ctags": {
                    "command": "docker",
                    "args": [
                        "run",
                        "-i",
                        "--rm",
                        "-v", f"{self.workspace_path}:/workspace:ro",
                        "-v", f"{self.output_base_dir / 'ctags'}:/output",
                        ctags_image
                    ]
                },
                "gnucobol": {
                    "command": "docker",
                    "args": [
                        "run",
                        "-i",
                        "--rm",
                        "-v", f"{self.workspace_path}:/workspace:ro",
                        "-v", f"{self.output_base_dir / 'gnucobol'}:/output",
                        gnucobol_image
                    ]
                },
                "superbol": {
                    "command": "docker",
                    "args": [
                        "run",
                        "-i",
                        "--rm",
                        "-v", f"{self.workspace_path}:/workspace:ro",
                        "-v", f"{self.output_base_dir / 'superbol'}:/output",
                        superbol_image
                    ]
                }
            }
        }

        return config

    async def initialize(self):
        """Initialize MCP client and create sessions"""
        print("\n" + "="*70)
        print("Initializing MCP Metadata Generator")
        print("="*70)

        # Create MCP client from config
        mcp_config = self.get_mcp_config()
        print(f"\nMCP Configuration:")
        print(json.dumps(mcp_config, indent=2))

        self.mcp_client = MCPClient.from_dict(mcp_config)

        # Create sessions for all servers (mcp-use starts Docker containers)
        print("\nCreating MCP sessions (starting Docker containers)...")
        await self.mcp_client.create_all_sessions()
        print("✓ All MCP sessions created and ready")

    async def cleanup(self):
        """Cleanup MCP sessions (Docker containers cleaned up via --rm)"""
        print("\n" + "="*70)
        print("Cleaning Up MCP Sessions")
        print("="*70)

        if self.mcp_client:
            try:
                await self.mcp_client.close_all_sessions()
            except BaseException as e:
                # CancelledError (BaseException in Python 3.9+) and cancel scope
                # errors are common with anyio/mcp_use during cleanup.
                # Docker containers will still be cleaned up via --rm flag.
                print(f"  ⚠ Session cleanup encountered non-critical error: {e}")
            print("✓ Sessions closed, Docker containers cleaned up automatically")

    async def generate_ctags_metadata(self, cobol_files: List[str]):
        """
        Generate ctags metadata for COBOL files

        Steps:
        1. Generate tags file for entire project
        2. Generate project symbols
        3. Generate project outline (all files at once)

        Args:
            cobol_files: List of COBOL file names (e.g., ["MAINPROG.COB"])
        """
        print("\n" + "="*70)
        print("Generating Ctags Metadata")
        print("="*70)

        session = self.mcp_client.get_session("ctags")
        is_single_file = len(cobol_files) == 1

        if is_single_file:
            print(f"  ℹ Single-file mode detected - skipping project-level tools")

        # Step 1: Generate tags file for specific files (works for both single and project)
        print("\n1. Generating tags file...")
        # Build list of specific file paths instead of entire workspace
        file_paths = [f"/workspace/{Path(f).name}" for f in cobol_files]
        print(f"   Processing {len(file_paths)} specific files: {', '.join([Path(f).name for f in cobol_files])}")

        tags_result = await session.call_tool(
            "generate_tags",
            {
                "path": " ".join(file_paths),  # Pass specific files, not entire workspace
                "language": "cobol",
                "output_format": "json",
                "output_file": "/output/cobol-project.tags"
            }
        )
        print("  ✓ Tags file generated at output/ctags/cobol-project.tags")

        # Step 2: Generate project symbols (SKIP in single-file mode)
        if not is_single_file:
            print("\n2. Generating project symbols...")
            symbols_result = await session.call_tool(
                "generate_project_symbols",
                {
                    "tags_file": "/output/cobol-project.tags",
                    "languages": "cobol"
                }
            )

            # Write symbols to file
            symbols_path = self.output_base_dir / "ctags" / "project-symbols.json"
            self._write_json(symbols_result, symbols_path)
            print(f"  ✓ Project symbols written to {symbols_path.name}")
        else:
            print("\n2. Skipping project symbols (single-file mode)")

        # Step 3: Generate project outline (SKIP in single-file mode)
        if not is_single_file:
            print("\n3. Generating project outline...")
            outline_result = await session.call_tool(
                "generate_project_outline",
                {
                    "tags_file": "/output/cobol-project.tags",
                    "max_depth": 10
                }
            )

            # Write outline
            outline_path = self.output_base_dir / "ctags" / "project-outline.json"
            self._write_json(outline_result, outline_path)
            print(f"  ✓ Project outline generated")
        else:
            print("\n3. Skipping project outline (single-file mode)")

        # Step 4: Generate per-file outlines using get_file_outline
        print("\n4. Generating per-file outlines...")
        for cobol_file in cobol_files:
            program_name = Path(cobol_file).stem
            file_path = f"/workspace/{Path(cobol_file).name}"

            file_outline_result = await session.call_tool(
                "get_file_outline",
                {
                    "file_path": file_path,
                    "tags_file": "/output/cobol-project.tags"
                }
            )

            # Write per-file outline
            file_outline_path = self.output_base_dir / "ctags" / f"ctags-{program_name}-outline.json"
            self._write_json(file_outline_result, file_outline_path)
            print(f"  ✓ Generated outline for {program_name}")

    async def generate_gnucobol_metadata(self, cobol_files: List[str]):
        """
        Generate GnuCOBOL analysis metadata

        Steps:
        1. Batch analyze all COBOL files using directory parameter

        Args:
            cobol_files: List of COBOL file names (e.g., ["MAINPROG.COB"])
        """
        print("\n" + "="*70)
        print("Generating GnuCOBOL Metadata")
        print("="*70)

        session = self.mcp_client.get_session("gnucobol")
        is_single_file = len(cobol_files) == 1

        if is_single_file:
            print(f"  ℹ Single-file mode detected - skipping project-level tools")

        # Batch analyze all files using directory (SKIP in single-file mode)
        if not is_single_file:
            print(f"\nBatch analyzing {len(cobol_files)} COBOL files...")
            batch_result = await session.call_tool(
                "batch_analyze",
                {
                    "directory": "/workspace"
                }
            )

            # Write batch analysis
            batch_path = self.output_base_dir / "gnucobol" / "gnucobol-batch-analyze-all.json"
            self._write_json(batch_result, batch_path)
            print(f"  ✓ Batch analysis written to {batch_path.name}")
        else:
            print(f"\nSkipping batch analysis (single-file mode)")

        # Generate individual file analysis for each COBOL file
        print(f"\nGenerating individual file analysis...")
        for cobol_file in cobol_files:
            program_name = Path(cobol_file).stem
            file_path = f"/workspace/{Path(cobol_file).name}"

            file_result = await session.call_tool(
                "analyze_cobol",
                {
                    "file_path": file_path,
                    "include_source": False,
                }
            )

            # Write individual analysis
            file_path_out = self.output_base_dir / "gnucobol" / f"gnucobol-{program_name}-analysis.json"
            self._write_json(file_result, file_path_out)
            print(f"  ✓ Analysis for {program_name}")

    async def generate_superbol_metadata(self, cobol_files: List[str]):
        """
        Generate SuperBol LSP metadata

        Steps:
        1. Generate document symbols for each file
        2. Generate CFG for entire project

        Args:
            cobol_files: List of COBOL file names (e.g., ["MAINPROG.COB"])
        """
        print("\n" + "="*70)
        print("Generating SuperBol LSP Metadata")
        print("="*70)

        session = self.mcp_client.get_session("superbol")
        is_single_file = len(cobol_files) == 1

        if is_single_file:
            print(f"  ℹ Single-file mode detected - skipping project-level tools")

        # Step 1: Generate document symbols for each file
        print("\n1. Generating document symbols...")
        for cobol_file in cobol_files:
            program_name = Path(cobol_file).stem
            file_path = f"/workspace/{Path(cobol_file).name}"

            symbols_result = await session.call_tool(
                "code_document_symbols",
                {
                    "file_path": file_path,
                    "language": "cobol"
                }
            )

            # Write symbols
            symbols_path = self.output_base_dir / "superbol" / f"superbol-{program_name}-doc-symbols.json"
            self._write_json(symbols_result, symbols_path)
            print(f"  ✓ Generated symbols for {program_name}")

        # Step 2: Generate CFG for entire project (SKIP in single-file mode)
        if not is_single_file:
            print("\n2. Generating CFG for all files...")
            # Note: Using wildcard to match all COBOL file extensions (.COB, .cob, .cbl, .c74, etc.)
            cfg_result = await session.call_tool(
                "cobol_generate_cfg_project",
                {
                    "file_pattern": "/workspace/*",  # Match all files, SuperBOL will filter COBOL files
                    "output_format": "json",
                    "output_dir": "/output/superbol-cfg"
                }
            )
            print("  ✓ CFG generation complete (check output/superbol/superbol-cfg/)")
        else:
            print("\n2. Skipping project CFG generation (single-file mode)")

        # Step 3: Generate individual CFG files
        print("\n3. Generating individual CFG files...")
        for cobol_file in cobol_files:
            program_name = Path(cobol_file).stem
            file_path = f"/workspace/{Path(cobol_file).name}"
            output_file = f"/output/superbol-cfg/{program_name}.json"

            cfg_file_result = await session.call_tool(
                "cobol_generate_cfg_file",
                {
                    "file_path": file_path,
                    "output_format": "json",
                    "output_file": output_file
                }
            )
            print(f"  ✓ CFG for {program_name}")

    async def generate_all_metadata(self, cobol_files: List[str]):
        """
        Generate all metadata from all MCP servers

        Runs metadata generation concurrently for better performance.

        Args:
            cobol_files: List of COBOL file names (e.g., ["MAINPROG.COB", "CUSTOMER.COB"])
        """
        try:
            # Initialize MCP client and sessions
            await self.initialize()

            # Generate metadata concurrently from all servers
            print("\n" + "="*70)
            print("Generating Metadata from All Servers (Concurrent)")
            print("="*70)

            results = await asyncio.gather(
                self.generate_ctags_metadata(cobol_files),
                self.generate_gnucobol_metadata(cobol_files),
                self.generate_superbol_metadata(cobol_files),
                return_exceptions=True  # Don't fail entire process if one server fails
            )

            # Check for errors
            errors = [r for r in results if isinstance(r, Exception)]
            if errors:
                print(f"\n⚠ {len(errors)} server(s) encountered errors:")
                for error in errors:
                    print(f"  - {error}")

            print("\n" + "="*70)
            print("✓ Metadata Generation Complete!")
            print("="*70)
            print(f"\nMetadata saved to: {self.output_base_dir}")
            print(f"  - {self.output_base_dir / 'ctags'}")
            print(f"  - {self.output_base_dir / 'gnucobol'}")
            print(f"  - {self.output_base_dir / 'superbol'}")

        except Exception as e:
            print(f"\n✗ Error during metadata generation: {e}")
            raise

        finally:
            # Always cleanup sessions
            await self.cleanup()

    def _write_json(self, data: Any, path: Path):
        """
        Write JSON data to file

        Handles CallToolResult objects from mcp-use by extracting content
        """
        path.parent.mkdir(parents=True, exist_ok=True)

        # Extract content from CallToolResult if needed
        if hasattr(data, 'content'):
            # CallToolResult has a content field which is a list of text/image content
            content_items = data.content
            if content_items and len(content_items) > 0:
                # Get the first text content item
                first_item = content_items[0]
                if hasattr(first_item, 'text'):
                    # Parse the text as JSON if possible
                    try:
                        json_data = json.loads(first_item.text)
                        with open(path, 'w') as f:
                            json.dump(json_data, f, indent=2)
                    except json.JSONDecodeError:
                        # If not JSON, write as text
                        with open(path, 'w') as f:
                            f.write(first_item.text)
                else:
                    # Write the content as-is
                    with open(path, 'w') as f:
                        json.dump({"content": str(first_item)}, f, indent=2)
            else:
                # Empty content
                with open(path, 'w') as f:
                    json.dump({"error": "Empty result"}, f, indent=2)
        else:
            # Regular dict/list, write directly
            with open(path, 'w') as f:
                json.dump(data, f, indent=2)


class ConfigDrivenMCPMetadataGenerator:
    """
    Generic MCP metadata generator — reads servers/tools from YAML config.

    Unlike MCPMetadataGenerator which hardcodes ctags/gnucobol/superbol,
    this class dynamically builds MCP sessions from the config's
    metadata.servers section and runs the declared tools.
    """

    def __init__(self, workspace_path: str, output_base_dir: str, servers_config: Dict[str, Any]):
        self.workspace_path = Path(workspace_path).absolute()
        self.output_base_dir = Path(output_base_dir).absolute()
        self.servers_config = servers_config
        self.mcp_client: MCPClient = None

    def get_mcp_config(self) -> Dict[str, Any]:
        """Build mcp-use config dynamically from servers_config."""
        mcp_servers = {}

        for server_name, server_cfg in self.servers_config.items():
            if not isinstance(server_cfg, dict):
                continue
            if not server_cfg.get('enabled', True):
                continue

            docker_image = server_cfg.get('docker_image')
            if not docker_image:
                raise ValueError(f"Missing docker_image for server: {server_name}")

            # Create output directory for this server
            server_output_dir = self.output_base_dir / server_name
            server_output_dir.mkdir(parents=True, exist_ok=True)

            mcp_servers[server_name] = {
                "command": "docker",
                "args": [
                    "run", "-i", "--rm",
                    "-v", f"{self.workspace_path}:/workspace:ro",
                    "-v", f"{server_output_dir}:/output",
                    docker_image
                ]
            }

        return {"mcpServers": mcp_servers}

    def _substitute_placeholders(self, args: Dict[str, Any], source_file: str = "", program_name: str = "") -> Dict[str, Any]:
        """Replace {{placeholders}} in tool arguments."""
        # Compute workspace-relative path for source file
        # e.g., "AutolivSweden/Atoms.cs" for nested files, "MAINPROG.cbl" for flat
        if source_file:
            try:
                relative_source = str(Path(source_file).relative_to(self.workspace_path))
            except ValueError:
                relative_source = Path(source_file).name
        else:
            relative_source = ""

        result = {}
        for key, value in args.items():
            if isinstance(value, str):
                if '{{source_content}}' in value:
                    # Read file content for tools that need source code as a string
                    file_path = Path(source_file) if source_file else None
                    if file_path and file_path.exists():
                        content = file_path.read_text(encoding='utf-8', errors='replace')
                        value = value.replace('{{source_content}}', content)
                    else:
                        value = value.replace('{{source_content}}', '')
                        print(f"  ⚠ Cannot read source content: {file_path}")
                value = value.replace('{{workspace}}', '/workspace')
                value = value.replace('{{source_file}}', f'/workspace/{relative_source}' if relative_source else '/workspace')
                value = value.replace('{{program_name}}', program_name)
            result[key] = value
        return result

    async def initialize(self):
        """Initialize MCP client and create sessions."""
        print("\n" + "=" * 70)
        print("Initializing Config-Driven MCP Metadata Generator")
        print("=" * 70)

        mcp_config = self.get_mcp_config()
        print(f"\nMCP Configuration:")
        print(json.dumps(mcp_config, indent=2))

        self.mcp_client = MCPClient.from_dict(mcp_config)
        print("\nCreating MCP sessions (starting Docker containers)...")
        await self.mcp_client.create_all_sessions()
        print("✓ All MCP sessions created and ready")

    async def cleanup(self):
        """Cleanup MCP sessions."""
        print("\n" + "=" * 70)
        print("Cleaning Up MCP Sessions")
        print("=" * 70)

        if self.mcp_client:
            try:
                await self.mcp_client.close_all_sessions()
            except BaseException as e:
                print(f"  ⚠ Session cleanup encountered non-critical error: {e}")
            print("✓ Sessions closed, Docker containers cleaned up automatically")

    async def generate_all_metadata(self, source_files: List[str]):
        """
        Generate metadata for all source files using configured MCP servers.

        Args:
            source_files: List of source file names (e.g., ["MyClass.cs"])
        """
        try:
            await self.initialize()

            print("\n" + "=" * 70)
            print(f"Generating Metadata for {len(source_files)} files")
            print("=" * 70)

            for server_name, server_cfg in self.servers_config.items():
                if not isinstance(server_cfg, dict):
                    continue
                if not server_cfg.get('enabled', True):
                    continue
                if 'tools' not in server_cfg:
                    continue

                print(f"\n--- Server: {server_name} ---")
                session = self.mcp_client.get_session(server_name)

                for tool_cfg in server_cfg['tools']:
                    tool_name = tool_cfg['name']
                    output_key = tool_cfg.get('output_key', tool_name)
                    scope = tool_cfg.get('scope', 'file')
                    base_args = tool_cfg.get('args', {})

                    if scope == 'project':
                        # Run once for the whole project
                        args = self._substitute_placeholders(base_args)
                        print(f"\n  Running {tool_name} (project scope)...")
                        result = await session.call_tool(tool_name, args)

                        output_path = self.output_base_dir / output_key
                        if not output_path.suffix:
                            output_path = output_path.with_suffix('.json')
                        output_path.parent.mkdir(parents=True, exist_ok=True)
                        self._write_json(result, output_path)
                        print(f"  ✓ {tool_name} → {output_path.name}")

                    elif scope == 'file':
                        # Run per source file
                        output_dir = self.output_base_dir / output_key
                        output_dir.mkdir(parents=True, exist_ok=True)

                        for source_file in source_files:
                            program_name = Path(source_file).stem
                            args = self._substitute_placeholders(
                                base_args,
                                source_file=source_file,
                                program_name=program_name
                            )

                            print(f"  Running {tool_name} for {program_name}...")
                            result = await session.call_tool(tool_name, args)

                            file_output = output_dir / f"{program_name}.json"
                            self._write_json(result, file_output)
                            print(f"  ✓ {tool_name}({program_name}) → {file_output.name}")

            print("\n" + "=" * 70)
            print("✓ Config-Driven Metadata Generation Complete!")
            print("=" * 70)
            print(f"\nMetadata saved to: {self.output_base_dir}")

        except Exception as e:
            print(f"\n✗ Error during metadata generation: {e}")
            raise
        finally:
            await self.cleanup()

    def _write_json(self, data: Any, path: Path):
        """Write JSON data to file (handles CallToolResult objects)."""
        path.parent.mkdir(parents=True, exist_ok=True)

        if hasattr(data, 'content'):
            content_items = data.content
            if content_items and len(content_items) > 0:
                first_item = content_items[0]
                if hasattr(first_item, 'text'):
                    try:
                        json_data = json.loads(first_item.text)
                        with open(path, 'w') as f:
                            json.dump(json_data, f, indent=2)
                    except json.JSONDecodeError:
                        with open(path, 'w') as f:
                            f.write(first_item.text)
                else:
                    with open(path, 'w') as f:
                        json.dump({"content": str(first_item)}, f, indent=2)
            else:
                with open(path, 'w') as f:
                    json.dump({"error": "Empty result"}, f, indent=2)
        else:
            with open(path, 'w') as f:
                json.dump(data, f, indent=2)


def create_metadata_generator(config: Dict[str, Any], workspace_path: str, output_base_dir: str):
    """
    Factory: auto-detect config format and return the right generator.

    If any server has 'tools' declarations → ConfigDrivenMCPMetadataGenerator.
    Otherwise → legacy MCPMetadataGenerator (COBOL-specific).
    """
    servers_config = config.get('metadata', {}).get('servers', {})
    has_tools = any(
        'tools' in s
        for s in servers_config.values()
        if isinstance(s, dict)
    )
    if has_tools:
        return ConfigDrivenMCPMetadataGenerator(workspace_path, output_base_dir, servers_config)
    return MCPMetadataGenerator(workspace_path, output_base_dir, servers_config)


# Synchronous wrapper for LangGraph integration
def generate_metadata_sync(
    workspace_path: str,
    output_dir: str,
    cobol_files: List[str],
    servers_config: Dict[str, Any] = None,
    config: Dict[str, Any] = None
):
    """
    Synchronous wrapper for metadata generation

    Can be called from LangGraph nodes.

    Args:
        workspace_path: Path to directory containing source files
        output_dir: Base directory for metadata output
        cobol_files: List of source file names (e.g., ["MAINPROG.COB", "MyClass.cs"])
        servers_config: Optional server configuration dict from YAML config
        config: Optional full config dict — if provided, uses factory to pick generator
    """
    if config:
        generator = create_metadata_generator(config, workspace_path, output_dir)
    else:
        generator = MCPMetadataGenerator(workspace_path, output_dir, servers_config)

    asyncio.run(generator.generate_all_metadata(cobol_files))

    # After asyncio.run() closes the event loop, lingering Docker subprocess
    # transports hit __del__ and print noisy RuntimeError ("Event loop is
    # closed") to stderr.  Force GC now with stderr suppressed so those
    # harmless messages don't appear.  Docker containers are already removed
    # via --rm flag.
    import gc, io
    real_stderr = sys.stderr
    sys.stderr = io.StringIO()
    try:
        gc.collect()
    finally:
        sys.stderr = real_stderr


# CLI for testing
if __name__ == "__main__":
    import sys

    async def main():
        if len(sys.argv) < 2:
            print("Usage: python mcp_metadata_generator.py <workspace_path> [output_dir]")
            print("Example: python mcp_metadata_generator.py /home/santosh/cobol-work ./output")
            sys.exit(1)

        workspace = sys.argv[1]
        output = sys.argv[2] if len(sys.argv) > 2 else "./output"

        # Find all COBOL files in workspace (.COB, .cob, .cbl, .CBL, .COBOL, .cobol, .c74, .C74)
        workspace_path = Path(workspace)
        patterns = [
            "*.COB", "*.cob",           # Standard COBOL
            "*.cbl", "*.CBL",           # COBOL
            "*.COBOL", "*.cobol",       # Full name
            "*.c74", "*.C74"            # COBOL-74
        ]

        cobol_files = []
        for pattern in patterns:
            cobol_files.extend(workspace_path.glob(pattern))
        cobol_files = sorted(set([f.name for f in cobol_files]))

        if not cobol_files:
            print(f"✗ No COBOL files found in {workspace}")
            print(f"   Searched for: {', '.join(patterns)}")
            sys.exit(1)

        print(f"\nFound {len(cobol_files)} COBOL files:")
        for f in cobol_files:
            print(f"  - {f}")

        # Generate metadata
        generator = MCPMetadataGenerator(workspace, output)
        await generator.generate_all_metadata(cobol_files)

    asyncio.run(main())
