#!/usr/bin/env python3
"""
End-to-End Test Script for Metadata Generation Pipeline

This script tests the complete metadata generation workflow:
1. Tree MCP Server - Directory scanning
2. CTags MCP Server - Code structure extraction
3. GnuCOBOL MCP Server - COBOL analysis & relationships
4. SuperBOL MCP Server - Symbols & CFG generation
5. Metadata caching - Change detection

Prerequisites:
- Docker running
- All MCP server images built (as configured in your config.yaml)
- A valid config.yaml file with servers and tree_server sections

Usage:
    python test_metadata_e2e.py --config <config.yaml> <cobol_project_path> [--metadata-dir ./metadata] [--skip-tree] [--skip-mcp]

Examples:
    # Full test with config file
    python test_metadata_e2e.py --config config-74.yaml /home/user/cobol-project

    # Test only Tree MCP (file discovery)
    python test_metadata_e2e.py --config config.yaml /home/user/cobol-project --skip-mcp

    # Test only metadata generation (skip Tree MCP, provide files manually)
    python test_metadata_e2e.py --config config.yaml /home/user/cobol-project --skip-tree

    # Custom metadata directory
    python test_metadata_e2e.py --config config.yaml /home/user/cobol-project --metadata-dir /tmp/test-metadata
"""

import argparse
import asyncio
import json
import logging
import sys
from datetime import datetime
from pathlib import Path

from config_loader import load_config

# Global logger - will be configured after metadata_dir is known
logger = logging.getLogger(__name__)


def setup_logging(metadata_dir: Path, verbose: bool = False):
    """Setup logging to both console and file in metadata directory."""
    log_level = logging.DEBUG if verbose else logging.INFO
    log_format = '%(asctime)s - %(levelname)s - %(message)s'

    # Create formatter
    formatter = logging.Formatter(log_format)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)

    # File handler - write to metadata directory
    log_file = metadata_dir / "metadata_generation.log"
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(logging.DEBUG)  # Always capture debug to file
    file_handler.setFormatter(formatter)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    logger.info(f"Logging to: {log_file}")


def print_header(title: str):
    """Print a formatted section header."""
    print(f"\n{'='*70}")
    print(f" {title}")
    print(f"{'='*70}\n")


def print_result(label: str, value, indent: int = 0):
    """Print a labeled result."""
    prefix = "  " * indent
    print(f"{prefix}{label}: {value}")


async def test_tree_mcp(project_path: str, metadata_dir: str, tree_config: dict) -> dict:
    """
    Test Tree MCP Server for file discovery.

    Returns:
        Dict with test results and discovered files
    """
    print_header("Phase 1: Tree MCP Server Test")

    from tree_mcp_client import TreeMCPClient, scan_project_directory

    result = {
        "success": False,
        "files": [],
        "error": None,
        "duration": 0,
    }

    start = datetime.now()

    try:
        print(f"Project path: {project_path}")
        print(f"Docker image: {tree_config.get('docker_image')}")
        print(f"Extensions: {tree_config.get('extensions')}")
        print()

        # Run tree scan
        print("Starting Tree MCP scan...")
        scan_result = await scan_project_directory(
            project_path=project_path,
            docker_image=tree_config.get("docker_image"),
            extensions=tree_config.get("extensions"),
            exclude_dirs=tree_config.get("exclude_dirs"),
            max_depth=tree_config.get("max_depth"),
            output_file=str(Path(metadata_dir) / "file_list.json"),
        )

        result["duration"] = (datetime.now() - start).total_seconds()

        if scan_result.success:
            result["success"] = True
            result["files"] = [f.to_dict() for f in scan_result.files]

            print(f"✅ Tree MCP scan successful!")
            print(f"   Duration: {result['duration']:.2f}s")
            print(f"   Files found: {scan_result.total_files}")
            print()

            if scan_result.files:
                print("   Discovered COBOL files:")
                for f in scan_result.files[:10]:  # Show first 10
                    print(f"     - {f.path}")
                if len(scan_result.files) > 10:
                    print(f"     ... and {len(scan_result.files) - 10} more")
        else:
            result["error"] = scan_result.error
            print(f"❌ Tree MCP scan failed: {scan_result.error}")

    except Exception as e:
        result["error"] = str(e)
        result["duration"] = (datetime.now() - start).total_seconds()
        print(f"❌ Tree MCP test error: {e}")
        logger.exception("Tree MCP test failed")

    return result


async def test_metadata_generation(
    project_path: str,
    metadata_dir: str,
    servers_config: dict,
    tree_config: dict,
    skip_tree: bool = False,
) -> dict:
    """
    Test full metadata generation pipeline.

    Returns:
        Dict with test results
    """
    print_header("Phase 2: Metadata Generation Test")

    from project_metadata_generator import ProjectMetadataGenerator
    from tree_mcp_client import FileInfo

    result = {
        "success": False,
        "total_files": 0,
        "successful_files": 0,
        "failed_files": 0,
        "metadata_files": [],
        "errors": [],
        "duration": 0,
    }

    start = datetime.now()

    try:
        print(f"Project path: {project_path}")
        print(f"Metadata dir: {metadata_dir}")
        print(f"Skip Tree MCP: {skip_tree}")
        print()

        print("MCP Servers:")
        for name, config in servers_config.items():
            print(f"  - {name}: {config.get('docker_image', 'not configured')}")
        print()

        generator = ProjectMetadataGenerator(
            project_path=project_path,
            metadata_dir=metadata_dir,
            servers_config=servers_config,
            tree_server_config=tree_config,
        )

        if skip_tree:
            # Manually find COBOL files without Tree MCP
            print("Scanning for COBOL files locally (skipping Tree MCP)...")
            project = Path(project_path)
            patterns = ["**/*.cbl", "**/*.CBL", "**/*.cob", "**/*.COB",
                       "**/*.cpy", "**/*.CPY", "**/*.c74", "**/*.C74"]

            files = []
            for pattern in patterns:
                for f in project.glob(pattern):
                    rel_path = str(f.relative_to(project))
                    files.append(FileInfo(
                        name=f.name,
                        path=rel_path,
                        absolute_path=str(f),
                        extension=f.suffix,
                    ))

            generator.cobol_files = files
            print(f"Found {len(files)} COBOL files locally")

            gen_result = await generator.generate_all_metadata(
                files=files,
                skip_discovery=True,
            )
        else:
            print("Running full metadata generation (with Tree MCP discovery)...")
            gen_result = await generator.generate_all_metadata()

        result["duration"] = (datetime.now() - start).total_seconds()
        result["success"] = gen_result.success
        result["total_files"] = gen_result.total_files
        result["successful_files"] = gen_result.successful_files
        result["failed_files"] = gen_result.failed_files
        result["errors"] = gen_result.errors
        result["metadata_files"] = gen_result.project_metadata_files

        print()
        if gen_result.success:
            print(f"✅ Metadata generation successful!")
        else:
            print(f"⚠️  Metadata generation completed with errors")

        print(f"   Duration: {result['duration']:.2f}s")
        print(f"   Total files: {gen_result.total_files}")
        print(f"   Successful: {gen_result.successful_files}")
        print(f"   Failed: {gen_result.failed_files}")

        if gen_result.errors:
            print(f"\n   Errors:")
            for err in gen_result.errors[:5]:
                print(f"     - {err}")
            if len(gen_result.errors) > 5:
                print(f"     ... and {len(gen_result.errors) - 5} more")

        # Show generated files
        print(f"\n   Project metadata files:")
        for mf in gen_result.project_metadata_files:
            print(f"     - {Path(mf).name}")

    except Exception as e:
        result["error"] = str(e)
        result["duration"] = (datetime.now() - start).total_seconds()
        print(f"❌ Metadata generation error: {e}")
        logger.exception("Metadata generation failed")

    return result


def test_cache_manager(metadata_dir: str, source_files: list) -> dict:
    """
    Test metadata cache manager.

    Returns:
        Dict with cache test results
    """
    print_header("Phase 3: Cache Manager Test")

    from metadata_cache import MetadataCacheManager

    result = {
        "success": False,
        "cache_stats": {},
        "files_needing_regen": [],
        "error": None,
    }

    try:
        cache = MetadataCacheManager(metadata_dir)

        # Get cache stats
        stats = cache.get_cache_stats()
        result["cache_stats"] = stats

        print(f"Cache file: {cache.cache_file}")
        print(f"Cache entries: {stats['total_entries']}")
        print(f"Successful: {stats['successful']}")
        print(f"Failed: {stats['failed']}")
        print(f"Total metadata files: {stats['total_metadata_files']}")
        print(f"Last full generation: {stats['last_full_generation']}")

        # Check which files need regeneration
        if source_files:
            print(f"\nChecking {len(source_files)} files for regeneration...")
            needs_regen = cache.get_files_needing_regeneration(source_files)
            result["files_needing_regen"] = needs_regen

            print(f"Files needing regeneration: {len(needs_regen)}")
            print(f"Files up to date: {len(source_files) - len(needs_regen)}")

        result["success"] = True
        print(f"\n✅ Cache manager test successful!")

    except Exception as e:
        result["error"] = str(e)
        print(f"❌ Cache manager error: {e}")
        logger.exception("Cache test failed")

    return result


def verify_metadata_files(metadata_dir: str) -> dict:
    """
    Verify generated metadata files exist and are valid JSON.

    Returns:
        Dict with verification results
    """
    print_header("Phase 4: Metadata File Verification")

    metadata_path = Path(metadata_dir)
    result = {
        "success": False,
        "files_checked": 0,
        "valid_files": 0,
        "invalid_files": [],
        "missing_dirs": [],
    }

    # Check directories
    expected_dirs = ["ctags", "gnucobol", "superbol", "superbol/cfg"]
    for d in expected_dirs:
        dir_path = metadata_path / d
        if not dir_path.exists():
            result["missing_dirs"].append(d)

    if result["missing_dirs"]:
        print(f"⚠️  Missing directories: {result['missing_dirs']}")
    else:
        print(f"✅ All expected directories exist")

    # Check JSON files
    print(f"\nVerifying JSON files...")
    json_files = list(metadata_path.rglob("*.json"))
    result["files_checked"] = len(json_files)

    for jf in json_files:
        try:
            with open(jf, 'r') as f:
                json.load(f)
            result["valid_files"] += 1
        except json.JSONDecodeError as e:
            result["invalid_files"].append(f"{jf.name}: {e}")
        except Exception as e:
            result["invalid_files"].append(f"{jf.name}: {e}")

    print(f"JSON files found: {result['files_checked']}")
    print(f"Valid JSON: {result['valid_files']}")
    print(f"Invalid JSON: {len(result['invalid_files'])}")

    if result["invalid_files"]:
        print(f"\nInvalid files:")
        for inv in result["invalid_files"][:5]:
            print(f"  - {inv}")

    result["success"] = len(result["invalid_files"]) == 0 and len(result["missing_dirs"]) == 0

    if result["success"]:
        print(f"\n✅ All metadata files verified!")
    else:
        print(f"\n⚠️  Verification completed with issues")

    return result


async def main():
    parser = argparse.ArgumentParser(
        description="End-to-End Test for Metadata Generation Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "--config",
        required=True,
        help="Path to YAML configuration file (required)"
    )
    parser.add_argument(
        "project_path",
        help="Path to COBOL project directory"
    )
    parser.add_argument(
        "--metadata-dir",
        help="Directory for metadata output (overrides config file)"
    )
    parser.add_argument(
        "--skip-tree",
        action="store_true",
        help="Skip Tree MCP test (find files locally)"
    )
    parser.add_argument(
        "--skip-mcp",
        action="store_true",
        help="Skip MCP metadata generation (test Tree only)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    # Load configuration from YAML file
    try:
        config = load_config(args.config)
        print(f"Loaded configuration from: {args.config}")
    except FileNotFoundError:
        print(f"❌ Configuration file not found: {args.config}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error loading configuration: {e}")
        sys.exit(1)

    # Validate project path
    project_path = Path(args.project_path).absolute()
    if not project_path.exists():
        print(f"❌ Project path does not exist: {project_path}")
        sys.exit(1)

    # Get metadata directory (CLI overrides config)
    if args.metadata_dir:
        metadata_dir = Path(args.metadata_dir).absolute()
    else:
        output_config = config.get_output_config()
        metadata_dir = Path(output_config.get("metadata_dir", "./metadata")).absolute()
    metadata_dir.mkdir(parents=True, exist_ok=True)

    # Setup logging to both console and file
    setup_logging(metadata_dir, args.verbose)

    # Get MCP server configuration from config file
    servers_config = config.get_servers_config()
    tree_server_config = config.get_tree_server_config()

    # Validate required Docker images are configured
    missing_configs = []
    if not servers_config.get("ctags", {}).get("docker_image"):
        missing_configs.append("servers.ctags.docker_image")
    if not servers_config.get("gnuCobol", {}).get("docker_image"):
        missing_configs.append("servers.gnuCobol.docker_image")
    if not servers_config.get("superbol-lsp", {}).get("docker_image"):
        missing_configs.append("servers.superbol-lsp.docker_image")
    if not tree_server_config.get("docker_image"):
        missing_configs.append("tree_server.docker_image")

    if missing_configs:
        print(f"❌ Missing required Docker image configurations in {args.config}:")
        for cfg in missing_configs:
            print(f"   - {cfg}")
        sys.exit(1)

    # Build tree_config with defaults for non-docker settings
    tree_config = {
        "docker_image": tree_server_config.get("docker_image"),
        "extensions": tree_server_config.get("extensions", [".cbl", ".CBL", ".cob", ".COB", ".cpy", ".CPY", ".c74", ".C74"]),
        "exclude_dirs": tree_server_config.get("exclude_dirs", [".git", "node_modules", "__pycache__", ".venv"]),
        "max_depth": tree_server_config.get("max_depth"),
    }

    print_header("COBOL Metadata Generation - End-to-End Test")
    print(f"Project: {project_path}")
    print(f"Metadata: {metadata_dir}")
    print(f"Skip Tree: {args.skip_tree}")
    print(f"Skip MCP: {args.skip_mcp}")

    results = {
        "project_path": str(project_path),
        "metadata_dir": str(metadata_dir),
        "timestamp": datetime.now().isoformat(),
        "tests": {}
    }

    discovered_files = []

    # Test 1: Tree MCP
    if not args.skip_tree:
        tree_result = await test_tree_mcp(str(project_path), str(metadata_dir), tree_config)
        results["tests"]["tree_mcp"] = tree_result
        if tree_result["success"]:
            discovered_files = [f["absolute_path"] for f in tree_result["files"]]

    # Test 2: Metadata Generation
    if not args.skip_mcp:
        mcp_result = await test_metadata_generation(
            str(project_path),
            str(metadata_dir),
            servers_config,
            tree_config,
            skip_tree=args.skip_tree,
        )
        results["tests"]["metadata_generation"] = mcp_result

    # Test 3: Cache Manager
    cache_result = test_cache_manager(str(metadata_dir), discovered_files)
    results["tests"]["cache_manager"] = cache_result

    # Test 4: File Verification
    verify_result = verify_metadata_files(str(metadata_dir))
    results["tests"]["verification"] = verify_result

    # Summary
    print_header("Test Summary")

    all_passed = True
    for test_name, test_result in results["tests"].items():
        status = "✅ PASS" if test_result.get("success") else "❌ FAIL"
        print(f"  {test_name}: {status}")
        if not test_result.get("success"):
            all_passed = False

    # Save results
    results_file = metadata_dir / "test_results.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to: {results_file}")

    if all_passed:
        print(f"\n✅ All tests passed!")
        sys.exit(0)
    else:
        print(f"\n⚠️  Some tests failed. Check results for details.")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
