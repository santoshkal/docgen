#!/bin/bash
# Test script to verify agent setup is correct

echo "=========================================="
echo "COBOL Documentation Agent - Setup Test"
echo "=========================================="
echo

# Check we're in the right directory
if [ ! -f "cobol_doc_agent.py" ]; then
    echo "❌ ERROR: Must run from agent/ directory"
    echo "   Run: cd agent && ./test_setup.sh"
    exit 1
fi
echo "✓ Running from agent directory"

# Check API key
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ ERROR: OPENAI_API_KEY not set"
    echo "   Run: export OPENAI_API_KEY='your-key'"
    exit 1
fi
echo "✓ OPENAI_API_KEY is set"

# Check Python dependencies
echo
echo "Checking Python dependencies..."
python -c "import langgraph" 2>/dev/null && echo "✓ langgraph installed" || echo "❌ langgraph missing"
python -c "import langchain_openai" 2>/dev/null && echo "✓ langchain-openai installed" || echo "❌ langchain-openai missing"
python -c "import yaml" 2>/dev/null && echo "✓ pyyaml installed" || echo "❌ pyyaml missing"

# Check template file
echo
if [ -f "cobol-doc-template.yaml" ]; then
    echo "✓ Template file exists: cobol-doc-template.yaml"
else
    echo "❌ ERROR: cobol-doc-template.yaml not found"
    exit 1
fi

# Check metadata directories
echo
echo "Checking metadata directories..."
if [ -d "../output/superbol" ]; then
    COUNT=$(ls ../output/superbol/superbol-*-doc-symbols.json 2>/dev/null | wc -l)
    echo "✓ SuperBol metadata: $COUNT files"
else
    echo "❌ ERROR: ../output/superbol not found"
    exit 1
fi

if [ -f "../output/gnucobol/gnucobol-batch-analyze-all.json" ]; then
    echo "✓ GnuCOBOL metadata exists"
else
    echo "❌ ERROR: ../output/gnucobol/gnucobol-batch-analyze-all.json not found"
    exit 1
fi

if [ -d "../output/ctags" ]; then
    COUNT=$(ls ../output/ctags/ctags-*-outline.json 2>/dev/null | wc -l)
    echo "✓ Ctags metadata: $COUNT files"
else
    echo "❌ ERROR: ../output/ctags not found"
    exit 1
fi

# Check output directory
echo
if [ ! -d "../docs" ]; then
    echo "⚠ Output directory doesn't exist, creating: ../docs"
    mkdir -p ../docs
fi
echo "✓ Output directory ready: ../docs"

# List available programs
echo
echo "=========================================="
echo "Available Programs:"
echo "=========================================="
for file in ../output/superbol/superbol-*-doc-symbols.json; do
    PROG=$(basename "$file" | sed 's/superbol-//;s/-doc-symbols.json//')
    echo "  - $PROG"
done

echo
echo "=========================================="
echo "Setup Check Complete!"
echo "=========================================="
echo
echo "To generate documentation, run:"
echo "  python cobol_doc_agent.py <PROGRAM_NAME>"
echo
echo "Example:"
echo "  python cobol_doc_agent.py MAINPROG"
echo
