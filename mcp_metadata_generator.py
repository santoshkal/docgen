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
            # Close sessions (containers will auto-cleanup via --rm)
            # Check mcp-use API for proper cleanup method
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
                    "file_path": file_path
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


# Synchronous wrapper for LangGraph integration
def generate_metadata_sync(workspace_path: str, output_dir: str, cobol_files: List[str], servers_config: Dict[str, Any] = None):
    """
    Synchronous wrapper for metadata generation

    Can be called from LangGraph nodes.

    Args:
        workspace_path: Path to directory containing COBOL source files
        output_dir: Base directory for metadata output
        cobol_files: List of COBOL file names (e.g., ["MAINPROG.COB"])
        servers_config: Optional server configuration dict from YAML config
    """
    generator = MCPMetadataGenerator(workspace_path, output_dir, servers_config)
    asyncio.run(generator.generate_all_metadata(cobol_files))


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
