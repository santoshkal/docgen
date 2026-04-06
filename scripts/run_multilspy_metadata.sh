#!/usr/bin/env bash
# ---------------------------------------------------------------
# run_multilspy_metadata.sh
#
# Build the multilspy Docker image with C# support and run the
# metadata generation script against the iMES project.
#
# Usage:
#   ./run_multilspy_metadata.sh                     # fresh run
#   ./run_multilspy_metadata.sh --resume            # resume from checkpoint
#   ./run_multilspy_metadata.sh --status            # show progress
#   ./run_multilspy_metadata.sh /path/to/project    # custom workspace
# ---------------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
MCP_SERVER_DIR="$HOME/mcp-servers/multilspy-mcp-server"
DOCKER_IMAGE="multilspy-csharp:latest"
OUTPUT_DIR="$SCRIPT_DIR/metadata"

# Parse arguments
RESUME=""
STATUS=""
WORKSPACE="$HOME/Downloads/iMES-master"

for arg in "$@"; do
    case "$arg" in
        --resume|-r) RESUME="--resume" ;;
        --status|-s) STATUS="--status" ;;
        *) WORKSPACE="$arg" ;;
    esac
done

# Status check — no Docker needed
if [[ -n "$STATUS" ]]; then
    python3 "$SCRIPT_DIR/generate_multilspy_metadata.py" \
        --output "$OUTPUT_DIR" --status
    exit 0
fi

# ---------------------------------------------------------------
# 1. Validate inputs
# ---------------------------------------------------------------
if [[ ! -d "$WORKSPACE" ]]; then
    echo "ERROR: Workspace directory not found: $WORKSPACE"
    exit 1
fi

if [[ ! -d "$MCP_SERVER_DIR/src" ]]; then
    echo "ERROR: multilspy-mcp-server not found at: $MCP_SERVER_DIR"
    exit 1
fi

echo "================================================"
echo "  multilspy Metadata Generator"
echo "================================================"
echo "  Workspace:  $WORKSPACE"
echo "  Output:     $OUTPUT_DIR"
echo "  Docker:     $DOCKER_IMAGE"
echo "  Resume:     ${RESUME:-no}"
echo "================================================"

# ---------------------------------------------------------------
# 2. Build Docker image (with C# / .NET support)
# ---------------------------------------------------------------
echo ""
echo "[Step 1/3] Building Docker image: $DOCKER_IMAGE ..."
echo "  (This includes .NET 8.0 SDK for OmniSharp C# support)"
echo ""

docker build \
    -t "$DOCKER_IMAGE" \
    -f "$SCRIPT_DIR/Dockerfile.multilspy-csharp" \
    "$MCP_SERVER_DIR"

echo ""
echo "[Step 1/3] Docker image built successfully."

# ---------------------------------------------------------------
# 3. Verify Docker image works
# ---------------------------------------------------------------
echo ""
echo "[Step 2/3] Verifying Docker image ..."

docker run --rm "$DOCKER_IMAGE" python -c "
from multilspy_mcp.server import mcp
print('multilspy-mcp-server loaded OK')
print(f'Tools: {len(mcp._tool_manager._tools) if hasattr(mcp, \"_tool_manager\") else \"?\"} registered')
"

echo "[Step 2/3] Docker image verified."

# ---------------------------------------------------------------
# 4. Install Python MCP client SDK (if needed) and run the script
# ---------------------------------------------------------------
echo ""
echo "[Step 3/3] Running metadata generation ..."
echo ""

# Ensure the mcp client SDK is available locally
if ! python3 -c "import mcp" 2>/dev/null; then
    echo "  Installing MCP Python SDK (mcp[cli]) ..."
    pip install --quiet "mcp[cli]>=1.1.3"
fi

# Only clean output on fresh run (not resume)
if [[ -z "$RESUME" ]]; then
    if [[ -d "$OUTPUT_DIR" ]]; then
        echo "  Clearing previous metadata in $OUTPUT_DIR ..."
        rm -rf "$OUTPUT_DIR"
    fi
fi
mkdir -p "$OUTPUT_DIR"

# Run the generator
python3 "$SCRIPT_DIR/generate_multilspy_metadata.py" \
    --workspace "$WORKSPACE" \
    --output "$OUTPUT_DIR" \
    $RESUME

echo ""
echo "================================================"
echo "  Done! Metadata written to: $OUTPUT_DIR"
echo "================================================"
echo ""
echo "Output structure:"
find "$OUTPUT_DIR" -type f -name "*.json" | head -30
TOTAL_FILES=$(find "$OUTPUT_DIR" -type f -name "*.json" | wc -l)
echo "  ... ($TOTAL_FILES total JSON files)"
