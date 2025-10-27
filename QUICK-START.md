# Quick Start Guide - COBOL Documentation Agent

## 5-Minute Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set API Key

```bash
export OPENAI_API_KEY="your-key-here"
```

### 3. Run Agent

```bash
cd agent
python cobol_doc_agent.py MAINPROG
```

### 4. View Output

```bash
cat ../docs/MAINPROG-documentation.md
```

## That's It!

Your documentation is in `../docs/MAINPROG-documentation.md` (relative to agent directory)

---

## What Just Happened?

The agent:
1. Loaded metadata from `../output/superbol/`, `../output/gnucobol/`, `../output/ctags/`
2. Read template structure from `./cobol-doc-template.yaml` (in agent directory)
3. Used OpenAI GPT-4o to intelligently fill the template
4. Generated comprehensive Markdown documentation to `../docs/`

---

## Next Steps

### Generate for All Programs

```bash
# Create batch script (run from agent directory)
cd agent
cat > generate_all.sh << 'EOF'
#!/bin/bash
for prog in MAINPROG ACCTOPER CUSTMGMT TRANPROC VALIDATE; do
    echo "Generating docs for $prog..."
    python cobol_doc_agent.py "$prog"
done
EOF

chmod +x generate_all.sh
./generate_all.sh
```

### Customize Template

Edit `cobol-doc-template.yaml` to:
- Add/remove sections
- Change diagram types
- Modify formatting
- Adjust detail level

### View Generated Docs

```bash
# Preview in terminal (from agent directory)
mdcat ../docs/MAINPROG-documentation.md

# Or open in browser
grip ../docs/MAINPROG-documentation.md
```

---

## File Structure

```
cobol-work/
├── agent/                      # Agent directory (work from here)
│   ├── cobol-doc-template.yaml # Template (customize this)
│   ├── cobol_doc_agent.py      # Agent (main logic)
│   ├── example_usage.py        # Usage examples
│   └── requirements.txt        # Dependencies
├── output/                     # Metadata (input)
│   ├── superbol/
│   ├── gnucobol/
│   └── ctags/
└── docs/                       # Generated docs (output)
    └── *.md
```

---

## Common Commands

```bash
# All commands should be run from the agent directory
cd agent

# Single program
python cobol_doc_agent.py MAINPROG

# With examples
python example_usage.py

# Custom output directory (specify relative to agent dir)
python cobol_doc_agent.py MAINPROG --output-dir ../custom-docs

# Help
python cobol_doc_agent.py --help
```

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'langgraph'"

```bash
pip install -r requirements.txt
```

### "AuthenticationError: Invalid API key"

```bash
export OPENAI_API_KEY="your-actual-key"
echo $OPENAI_API_KEY  # Verify it's set
```

### "FileNotFoundError: superbol-MAINPROG-doc-symbols.json"

Metadata doesn't exist for this program. Check:
```bash
ls ../output/superbol/superbol-*-doc-symbols.json
```

### "Output looks different each time"

Check temperature setting in `cobol_doc_agent.py`:
```python
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.1  # Should be low for consistency
)
```

---

## Full Documentation

- **Complete Guide**: `README-COBOL-DOC-AGENT.md`
- **Workflow Details**: `WORKFLOW-GUIDE.md`
- **Examples**: `example_usage.py`

---

## Questions?

1. Read `README-COBOL-DOC-AGENT.md` for comprehensive documentation
2. Check `WORKFLOW-GUIDE.md` for detailed workflow explanation
3. Run `python example_usage.py` for usage examples
