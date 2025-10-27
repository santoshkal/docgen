#!/bin/bash
# Generate documentation for all COBOL programs in the project

echo "=========================================="
echo "COBOL Documentation Generator - Batch Mode"
echo "=========================================="
echo

# Check API key
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ ERROR: OPENAI_API_KEY not set"
    echo "   Run: export OPENAI_API_KEY='your-key'"
    exit 1
fi

# Get list of programs from metadata
PROGRAMS=()
for file in ../output/superbol/superbol-*-doc-symbols.json; do
    PROG=$(basename "$file" | sed 's/superbol-//;s/-doc-symbols.json//')
    PROGRAMS+=("$PROG")
done

TOTAL=${#PROGRAMS[@]}
echo "Found $TOTAL programs to document:"
for prog in "${PROGRAMS[@]}"; do
    echo "  - $prog"
done
echo

# Confirm
read -p "Generate documentation for all $TOTAL programs? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 0
fi

echo
echo "=========================================="
echo "Starting batch generation..."
echo "=========================================="
echo

# Track results
SUCCESS=0
FAILED=0
FAILED_PROGS=()

# Generate documentation for each program
for ((i=0; i<${#PROGRAMS[@]}; i++)); do
    PROG="${PROGRAMS[$i]}"
    NUM=$((i+1))

    echo "[$NUM/$TOTAL] Generating documentation for $PROG..."

    if python cobol_doc_agent.py "$PROG" > /dev/null 2>&1; then
        echo "  ✓ Success"
        SUCCESS=$((SUCCESS+1))
    else
        echo "  ✗ Failed"
        FAILED=$((FAILED+1))
        FAILED_PROGS+=("$PROG")
    fi
    echo
done

# Summary
echo "=========================================="
echo "Batch Generation Complete!"
echo "=========================================="
echo "Success: $SUCCESS programs"
echo "Failed:  $FAILED programs"

if [ $FAILED -gt 0 ]; then
    echo
    echo "Failed programs:"
    for prog in "${FAILED_PROGS[@]}"; do
        echo "  - $prog"
    done
    echo
    echo "Retry failed programs with:"
    for prog in "${FAILED_PROGS[@]}"; do
        echo "  python cobol_doc_agent.py $prog"
    done
fi

echo
echo "Documentation saved to: ../docs/"
ls -lh ../docs/*.md 2>/dev/null | wc -l | xargs echo "Total files:"

exit 0
