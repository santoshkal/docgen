# Quick Start - MCP Integration

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies

```bash
cd /home/santosh/cobol-work/agent
source .venv/bin/activate
pip install -r requirements.txt
```

**New requirement**: `mcp-use` library for MCP integration

---

### Step 2: Generate Metadata + Documentation

```bash
python cobol_doc_agent.py MAINPROG \
  --generate-metadata \
  --workspace /home/santosh/cobol-work
```

**What happens:**
1. ✨ Starts 3 Docker MCP servers (ctags, gnucobol, superbol)
2. 📊 Generates metadata for all `*.COB` files concurrently
3. 💾 Writes metadata to `../output/`
4. 📝 Generates comprehensive documentation
5. 🧹 Cleans up Docker containers automatically

---

### Step 3: View Results

```bash
# Check metadata
ls -R ../output/

# View documentation
cat ../docs/MAINPROG-documentation.md
```

---

## 📖 Common Usage Patterns

### Pattern 1: First Time Setup

Generate everything from scratch:

```bash
python cobol_doc_agent.py MAINPROG \
  --generate-metadata \
  --workspace /home/santosh/cobol-work \
  --metadata-dir ../output \
  --output-dir ../docs
```

---

### Pattern 2: Regenerate Documentation Only

Use existing metadata:

```bash
python cobol_doc_agent.py MAINPROG
```

---

### Pattern 3: Force Regenerate All

Force metadata regeneration even if files exist:

```bash
python cobol_doc_agent.py MAINPROG \
  --generate-metadata \
  --no-skip-existing \
  --workspace /home/santosh/cobol-work
```

---

### Pattern 4: Batch Generation

Generate for multiple programs:

```bash
# Generate metadata once
python mcp_metadata_generator.py /home/santosh/cobol-work ../output

# Then generate docs for each program
for program in MAINPROG CUSTOMER ACCTOPER; do
  python cobol_doc_agent.py $program
done
```

---

## 🛠 Troubleshooting

### Issue: Docker permission denied
```bash
sudo usermod -aG docker $USER
newgrp docker
```

### Issue: mcp-use not found
```bash
pip install mcp-use
```

### Issue: No COBOL files found
Check workspace path contains `*.COB` files:
```bash
ls /home/santosh/cobol-work/*.COB
```

---

## 📚 Documentation

- **MCP_INTEGRATION_GUIDE.md** - Full documentation
- **MCP_INTEGRATION_SUMMARY.md** - Implementation summary
- **README.md** - Original agent documentation

---

## 🎯 Quick Reference

| Command | Purpose |
|---------|---------|
| `--generate-metadata` | Enable metadata generation via MCP |
| `--workspace PATH` | Path to COBOL source files |
| `--metadata-dir PATH` | Where to save/load metadata |
| `--output-dir PATH` | Where to save documentation |
| `--no-skip-existing` | Force regenerate even if exists |

---

## ✅ Success Indicators

After running, you should see:

1. **Docker containers started**:
   ```
   Starting MCP Server Containers
   ✓ Started ctags: a1b2c3d4
   ✓ Started gnucobol: e5f6g7h8
   ✓ Started superbol: i9j0k1l2
   ```

2. **Metadata generated**:
   ```
   Generating Ctags Metadata
   ✓ Tags file generated
   ✓ Project symbols written
   ✓ Generated outline for MAINPROG

   Generating GnuCOBOL Metadata
   ✓ Batch analysis complete

   Generating SuperBol LSP Metadata
   ✓ Generated symbols for MAINPROG
   ✓ CFG generation complete
   ```

3. **Documentation created**:
   ```
   COBOL Documentation Generator
   Mode: Generate metadata + documentation

   ✓ Metadata generation complete
   ✓ Successfully loaded all metadata for MAINPROG
   ✓ Template loaded successfully
   ✓ Document assembled: 25678 characters
   ✓ Documentation saved to: ../docs/MAINPROG-documentation.md
   ```

---

**Ready to test? Run Step 1-3 above! 🎉**
