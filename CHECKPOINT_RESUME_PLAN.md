# Implementation Plan: Checkpoint/Resume Mechanism for Batch Processing

## Overview

Add a robust checkpoint/resume mechanism to the COBOL Documentation Agent that allows:
1. **Automatic progress saving** after each file is processed
2. **Resume from interruption** without re-processing completed files
3. **Retry failed files** with configurable retry limits
4. **Progress visibility** with detailed status reporting

---

## Architecture

### Component Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         cobol_doc_agent.py                              │
│                                                                         │
│  ┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐   │
│  │  CLI Arguments  │    │  Batch Loop      │    │  Single File     │   │
│  │  --resume       │───▶│  (main driver)   │───▶│  Processing      │   │
│  │  --restart      │    │                  │    │                  │   │
│  │  --status       │    └────────┬─────────┘    └──────────────────┘   │
│  └─────────────────┘             │                                      │
│                                  │                                      │
│                    ┌─────────────▼─────────────┐                        │
│                    │   CheckpointManager       │                        │
│                    │   (checkpoint_manager.py) │                        │
│                    └─────────────┬─────────────┘                        │
│                                  │                                      │
└──────────────────────────────────┼──────────────────────────────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   .checkpoint.yaml          │
                    │   (persistent state file)   │
                    └─────────────────────────────┘
```

### Data Flow

```
┌──────────┐     ┌────────────────┐     ┌──────────────────┐
│  Start   │────▶│ Load/Create    │────▶│ Filter Pending   │
│  Batch   │     │ Checkpoint     │     │ Files            │
└──────────┘     └────────────────┘     └────────┬─────────┘
                                                 │
                                                 ▼
                 ┌───────────────────────────────────────────┐
                 │           For Each Pending File           │
                 │  ┌─────────────────────────────────────┐  │
                 │  │ 1. Mark as "in_progress"            │  │
                 │  │ 2. Save checkpoint                  │  │
                 │  │ 3. Process file (generate docs)     │  │
                 │  │ 4. Mark as "completed" or "failed"  │  │
                 │  │ 5. Save checkpoint                  │  │
                 │  └─────────────────────────────────────┘  │
                 └───────────────────────────────────────────┘
                                                 │
                                                 ▼
                              ┌──────────────────────────────┐
                              │  Generate Summary Report     │
                              └──────────────────────────────┘
```

---

## File: `checkpoint_manager.py` (NEW)

### Class: `FileStatus` (Enum)

```python
class FileStatus(str, Enum):
    PENDING = "pending"           # Not yet processed
    IN_PROGRESS = "in_progress"   # Currently being processed
    COMPLETED = "completed"       # Successfully completed
    FAILED = "failed"             # Failed after max retries
    SKIPPED = "skipped"           # Skipped by user request
```

### Class: `FileCheckpoint` (TypedDict)

```python
class FileCheckpoint(TypedDict):
    status: str                   # FileStatus value
    started_at: Optional[str]     # ISO timestamp
    completed_at: Optional[str]   # ISO timestamp
    output_file: Optional[str]    # Path to generated doc
    error: Optional[str]          # Last error message
    retry_count: int              # Number of retries attempted
    file_hash: Optional[str]      # SHA256 of source file (for change detection)
```

### Class: `CheckpointState` (TypedDict)

```python
class CheckpointState(TypedDict):
    version: int                  # Schema version for migration
    config_hash: str              # Hash of config for change detection
    source_dir: str               # Source directory path
    output_dir: str               # Output directory path
    started_at: str               # ISO timestamp of first run
    last_updated: str             # ISO timestamp of last update
    total_files: int              # Total files to process
    files: Dict[str, FileCheckpoint]  # Per-file status
```

### Class: `CheckpointManager`

```python
class CheckpointManager:
    """
    Manages checkpoint state for batch documentation generation.

    Features:
    - Atomic saves (write to temp, then rename)
    - Config change detection
    - Source file change detection
    - Progress reporting
    """

    def __init__(
        self,
        output_dir: Path,
        config_hash: str,
        checkpoint_filename: str = ".checkpoint.yaml"
    ):
        """
        Initialize checkpoint manager.

        Args:
            output_dir: Directory where checkpoint file is stored
            config_hash: Hash of current config for change detection
            checkpoint_filename: Name of checkpoint file
        """

    def load_or_create(self, source_files: List[Path]) -> CheckpointState:
        """
        Load existing checkpoint or create new one.

        Args:
            source_files: List of source files to process

        Returns:
            Loaded or newly created checkpoint state
        """

    def save(self) -> None:
        """
        Save current checkpoint state atomically.

        Uses write-to-temp-then-rename pattern for crash safety.
        """

    def mark_file_started(self, filename: str) -> None:
        """
        Mark a file as in_progress before processing.

        Args:
            filename: Name of file being processed
        """

    def mark_file_completed(
        self,
        filename: str,
        output_file: str
    ) -> None:
        """
        Mark a file as successfully completed.

        Args:
            filename: Name of completed file
            output_file: Path to generated documentation
        """

    def mark_file_failed(
        self,
        filename: str,
        error: str
    ) -> None:
        """
        Mark a file as failed.

        Args:
            filename: Name of failed file
            error: Error message
        """

    def get_pending_files(self) -> List[str]:
        """
        Get list of files that need processing.

        Returns files with status: pending, in_progress (interrupted),
        or failed (if retry_count < max_retries).

        Returns:
            List of filenames to process
        """

    def get_completed_files(self) -> List[str]:
        """
        Get list of successfully completed files.

        Returns:
            List of completed filenames
        """

    def get_failed_files(self) -> List[str]:
        """
        Get list of files that failed after max retries.

        Returns:
            List of failed filenames
        """

    def should_reprocess(self, filename: str, file_path: Path) -> bool:
        """
        Check if a completed file should be reprocessed.

        Returns True if:
        - File hash changed (source modified)
        - Config hash changed (and config_change_reprocess=True)

        Args:
            filename: Name of file to check
            file_path: Path to source file

        Returns:
            True if file should be reprocessed
        """

    def config_changed(self) -> bool:
        """
        Check if config has changed since checkpoint was created.

        Returns:
            True if config hash differs
        """

    def get_progress(self) -> Dict[str, Any]:
        """
        Get current progress statistics.

        Returns:
            Dict with keys: total, completed, failed, pending,
            percent_complete, elapsed_time, estimated_remaining
        """

    def get_summary_report(self) -> str:
        """
        Generate human-readable summary report.

        Returns:
            Formatted string with progress details
        """

    def delete_checkpoint(self) -> None:
        """
        Delete checkpoint file (for --restart).
        """

    @staticmethod
    def compute_config_hash(config: Dict[str, Any]) -> str:
        """
        Compute hash of relevant config fields.

        Only includes fields that affect output:
        - llm config (provider, model, temperature)
        - template path
        - source extensions

        Args:
            config: Full configuration dict

        Returns:
            SHA256 hash string
        """

    @staticmethod
    def compute_file_hash(file_path: Path) -> str:
        """
        Compute SHA256 hash of file contents.

        Args:
            file_path: Path to file

        Returns:
            SHA256 hash string
        """
```

---

## File: `cobol_doc_agent.py` (MODIFY)

### New CLI Arguments

```python
# Add to argument parser (around line 3850)

parser.add_argument(
    '--resume',
    action='store_true',
    default=True,
    help='Resume from checkpoint if exists (default: True)'
)

parser.add_argument(
    '--restart',
    action='store_true',
    help='Ignore checkpoint and restart from beginning'
)

parser.add_argument(
    '--status',
    action='store_true',
    help='Show checkpoint status and exit without processing'
)

parser.add_argument(
    '--retry-failed',
    action='store_true',
    help='Only retry previously failed files'
)

parser.add_argument(
    '--files',
    type=str,
    help='Comma-separated list of specific files to process'
)

parser.add_argument(
    '--max-retries',
    type=int,
    default=3,
    help='Maximum retries for failed files (default: 3)'
)
```

### Modified Batch Processing Loop

Location: Around line 3980-4050 in `main()` function

```python
def run_batch_with_checkpoint(
    cobol_files_to_process: List[Tuple[str, str]],
    config: Dict[str, Any],
    args: argparse.Namespace
) -> Dict[str, Any]:
    """
    Run batch processing with checkpoint/resume support.

    Args:
        cobol_files_to_process: List of (program_name, file_path) tuples
        config: Loaded configuration
        args: CLI arguments

    Returns:
        Summary dict with completion statistics
    """
    from checkpoint_manager import CheckpointManager

    output_dir = Path(config['output']['docs_path'])

    # Compute config hash for change detection
    config_hash = CheckpointManager.compute_config_hash(config)

    # Initialize checkpoint manager
    checkpoint = CheckpointManager(
        output_dir=output_dir,
        config_hash=config_hash
    )

    # Handle --restart flag
    if args.restart:
        checkpoint.delete_checkpoint()
        print("Checkpoint deleted. Starting fresh.")

    # Load or create checkpoint
    source_files = [Path(fp) for _, fp in cobol_files_to_process]
    state = checkpoint.load_or_create(source_files)

    # Handle --status flag
    if args.status:
        print(checkpoint.get_summary_report())
        return {'status_only': True}

    # Check for config changes
    if checkpoint.config_changed() and not args.restart:
        print("\n⚠ Configuration has changed since last run!")
        print("Options:")
        print("  1. Continue anyway (may produce inconsistent results)")
        print("  2. Restart with --restart flag")
        response = input("Continue? [y/N]: ")
        if response.lower() != 'y':
            return {'aborted': True, 'reason': 'config_changed'}

    # Get files to process
    if args.retry_failed:
        pending = checkpoint.get_failed_files()
        print(f"\nRetrying {len(pending)} failed files...")
    elif args.files:
        pending = [f.strip() for f in args.files.split(',')]
        print(f"\nProcessing {len(pending)} specified files...")
    else:
        pending = checkpoint.get_pending_files()

    # Print progress header
    progress = checkpoint.get_progress()
    print(f"\n{'='*70}")
    print(f"BATCH PROCESSING {'(RESUMING)' if progress['completed'] > 0 else ''}")
    print(f"{'='*70}")
    print(f"Total files: {progress['total']}")
    print(f"Completed: {progress['completed']}")
    print(f"Failed: {progress['failed']}")
    print(f"Remaining: {len(pending)}")
    print(f"{'='*70}\n")

    # Process each pending file
    for idx, filename in enumerate(pending, 1):
        # Find full path for this file
        file_path = next(
            (fp for pn, fp in cobol_files_to_process if Path(fp).name == filename),
            None
        )

        if not file_path:
            print(f"⚠ File not found: {filename}")
            continue

        program_name = Path(file_path).stem

        print(f"\n[{idx}/{len(pending)}] Processing: {filename}")
        print(f"    Program: {program_name}")

        # Mark as in_progress and save checkpoint
        checkpoint.mark_file_started(filename)
        checkpoint.save()

        try:
            # Generate documentation for this file
            output_path = generate_documentation(
                program_name=program_name,
                workspace_path=str(Path(file_path).parent),
                metadata_dir=config['output']['metadata_dir'],
                template_path=config['template']['path'],
                output_dir=str(output_dir),
                llm_config=config['llm'],
                cobol_file_path=file_path,
                generate_metadata=True,
            )

            if output_path:
                checkpoint.mark_file_completed(filename, output_path)
                print(f"    ✓ Completed: {output_path}")
            else:
                checkpoint.mark_file_failed(filename, "generate_documentation returned None")
                print(f"    ✗ Failed: No output generated")

        except Exception as e:
            checkpoint.mark_file_failed(filename, str(e))
            print(f"    ✗ Failed: {e}")

            # Check if we should continue or abort
            if not args.continue_on_error:
                print("\nUse --continue-on-error to skip failed files")
                checkpoint.save()
                raise

        # Save checkpoint after each file
        checkpoint.save()

        # Print running progress
        progress = checkpoint.get_progress()
        print(f"    Progress: {progress['percent_complete']:.1f}% "
              f"({progress['completed']}/{progress['total']})")

    # Final summary
    print(f"\n{'='*70}")
    print("BATCH PROCESSING COMPLETE")
    print(f"{'='*70}")
    print(checkpoint.get_summary_report())

    return checkpoint.get_progress()
```

---

## File: `config_loader.py` (MODIFY)

### New Config Section

```python
def get_checkpoint_config(self) -> Dict[str, Any]:
    """
    Get checkpoint/resume configuration.

    Returns configuration for checkpoint behavior including:
    - enabled: Whether checkpoint is enabled
    - auto_resume: Auto-resume if checkpoint exists
    - retry_failed: Retry failed files on resume
    - max_retries: Maximum retries per file
    - reprocess_on_config_change: Reprocess completed files if config changed
    - reprocess_on_source_change: Reprocess if source file modified

    Returns:
        Dictionary with checkpoint configuration
    """
    config = self._ensure_loaded()
    cp_config = config.get('checkpoint', {})

    return {
        'enabled': cp_config.get('enabled', True),
        'auto_resume': cp_config.get('auto_resume', True),
        'retry_failed': cp_config.get('retry_failed', True),
        'max_retries': cp_config.get('max_retries', 3),
        'reprocess_on_config_change': cp_config.get('reprocess_on_config_change', False),
        'reprocess_on_source_change': cp_config.get('reprocess_on_source_change', True),
    }
```

### Example Config Section

```yaml
# Checkpoint/Resume Configuration
checkpoint:
  enabled: true                      # Enable checkpoint/resume feature
  auto_resume: true                  # Auto-resume if checkpoint exists
  retry_failed: true                 # Retry failed files on resume
  max_retries: 3                     # Max retries per file before marking failed
  reprocess_on_config_change: false  # Reprocess all if config changes
  reprocess_on_source_change: true   # Reprocess if source file modified
```

---

## Checkpoint File Format

### File: `.checkpoint.yaml`

```yaml
# COBOL Documentation Agent - Checkpoint File
# DO NOT EDIT MANUALLY - This file is auto-generated

version: 1
config_hash: "sha256:a1b2c3d4e5f6..."
source_dir: "/home/santosh/Downloads/csi-cobol"
output_dir: "/home/santosh/Downloads/csi-cobol-output/docs"
started_at: "2024-01-28T10:00:00.000000"
last_updated: "2024-01-28T14:35:22.123456"

# Statistics
total_files: 232
completed_count: 45
failed_count: 2
skipped_count: 0

# Per-file status
files:
  ACCTA.XMOD:
    status: completed
    started_at: "2024-01-28T10:05:00.000000"
    completed_at: "2024-01-28T10:08:32.456789"
    output_file: "ACCTA-documentation-28-01-2024.md"
    file_hash: "sha256:1234abcd..."
    retry_count: 0
    error: null

  ACCTB.XMOD:
    status: failed
    started_at: "2024-01-28T10:08:35.000000"
    completed_at: null
    output_file: null
    file_hash: "sha256:5678efgh..."
    retry_count: 3
    error: "API Error: 429 Too Many Requests - Rate limit exceeded"

  ACCTC.XMOD:
    status: in_progress
    started_at: "2024-01-28T14:35:00.000000"
    completed_at: null
    output_file: null
    file_hash: "sha256:9012ijkl..."
    retry_count: 0
    error: null

  ACCTD.XMOD:
    status: pending
    started_at: null
    completed_at: null
    output_file: null
    file_hash: null
    retry_count: 0
    error: null
```

---

## CLI Usage Examples

### Basic Usage

```bash
# Normal run - auto-resumes if checkpoint exists
python cobol_doc_agent.py config.yaml

# Check status without processing
python cobol_doc_agent.py config.yaml --status

# Force restart (delete checkpoint)
python cobol_doc_agent.py config.yaml --restart

# Only retry failed files
python cobol_doc_agent.py config.yaml --retry-failed

# Process specific files only
python cobol_doc_agent.py config.yaml --files "ACCTA.XMOD,ACCTB.XMOD"

# Continue even if some files fail
python cobol_doc_agent.py config.yaml --continue-on-error

# Increase max retries
python cobol_doc_agent.py config.yaml --max-retries 5
```

### Status Output Example

```
═══════════════════════════════════════════════════════════════════════════
CHECKPOINT STATUS
═══════════════════════════════════════════════════════════════════════════
Checkpoint file: /home/santosh/Downloads/csi-cobol-output/docs/.checkpoint.yaml
Source directory: /home/santosh/Downloads/csi-cobol
Output directory: /home/santosh/Downloads/csi-cobol-output/docs

Started: 2024-01-28 10:00:00
Last updated: 2024-01-28 14:35:22
Elapsed time: 4h 35m 22s

Progress: [██████████████░░░░░░░░░░░░░░░░] 45/232 (19.4%)

  ✓ Completed:  45 files
  ✗ Failed:      2 files
  ○ Pending:   185 files

Failed files:
  1. ACCTB.XMOD - API Error: 429 Too Many Requests
  2. RPT045.XMOD - Timeout after 600s

Estimated time remaining: ~18h 20m (based on avg 4.5 min/file)
═══════════════════════════════════════════════════════════════════════════
```

---

## Error Handling

### Recoverable Errors (Auto-Retry)

| Error Type | Handling |
|------------|----------|
| Rate limit (429) | Exponential backoff, retry up to max_retries |
| Timeout | Retry with same timeout |
| Temporary network error | Retry after 30s |
| LLM API transient error | Retry up to max_retries |

### Non-Recoverable Errors (Mark Failed)

| Error Type | Handling |
|------------|----------|
| File not found | Mark failed, continue |
| Invalid COBOL syntax | Mark failed, continue |
| Output directory permission | Abort batch |
| Checkpoint write failure | Abort batch |

### Interrupted Processing

| Scenario | Handling |
|----------|----------|
| Ctrl+C during file | Mark in_progress, save checkpoint |
| System crash | in_progress treated as pending on resume |
| Kill -9 | in_progress treated as pending on resume |

---

## Implementation Order

### Phase 1: Core Checkpoint (MVP)
1. Create `checkpoint_manager.py` with basic functionality
2. Add checkpoint loading/saving
3. Add `--restart` and `--status` flags
4. Integrate basic checkpoint into batch loop
5. Test with small batch (5-10 files)

### Phase 2: Robustness
1. Add atomic save (temp file + rename)
2. Add config change detection
3. Add source file change detection
4. Add `--retry-failed` flag
5. Add progress estimation

### Phase 3: Polish
1. Add `--files` flag for selective processing
2. Add `--continue-on-error` flag
3. Add detailed error reporting
4. Add checkpoint config section
5. Update documentation

---

## Testing Plan

### Unit Tests

```python
# test_checkpoint_manager.py

def test_create_new_checkpoint():
    """Test creating checkpoint for new batch"""

def test_load_existing_checkpoint():
    """Test loading existing checkpoint"""

def test_mark_file_completed():
    """Test marking file as completed"""

def test_mark_file_failed():
    """Test marking file as failed with retry count"""

def test_get_pending_files():
    """Test filtering pending files"""

def test_config_change_detection():
    """Test config hash comparison"""

def test_source_file_change_detection():
    """Test file hash comparison"""

def test_atomic_save():
    """Test crash-safe saving"""

def test_corrupted_checkpoint_recovery():
    """Test handling of corrupted checkpoint file"""
```

### Integration Tests

```python
def test_batch_with_checkpoint():
    """Test full batch run with checkpoint"""

def test_resume_after_interrupt():
    """Test resuming interrupted batch"""

def test_retry_failed_files():
    """Test --retry-failed flag"""

def test_restart_flag():
    """Test --restart flag deletes checkpoint"""
```

### Manual Testing

1. Run batch on 10 files, interrupt at file 5, resume
2. Run batch, modify config, test warning
3. Run batch, modify source file, verify reprocess
4. Run batch with intentional failures, test retry
5. Test with disk full scenario

---

## Files to Create/Modify

| File | Action | Description |
|------|--------|-------------|
| `checkpoint_manager.py` | **CREATE** | Core checkpoint management class |
| `cobol_doc_agent.py` | **MODIFY** | Add CLI args, integrate checkpoint |
| `config_loader.py` | **MODIFY** | Add checkpoint config section |
| `test_checkpoint_manager.py` | **CREATE** | Unit tests |
| `config.example.yaml` | **MODIFY** | Add checkpoint config example |

---

## Estimated Effort

| Phase | Tasks | Estimate |
|-------|-------|----------|
| Phase 1 (MVP) | Core checkpoint functionality | 2-3 hours |
| Phase 2 (Robustness) | Error handling, change detection | 2-3 hours |
| Phase 3 (Polish) | CLI options, documentation | 1-2 hours |
| Testing | Unit + integration tests | 2-3 hours |
| **Total** | | **7-11 hours** |

---

## Approval Checklist

Before implementation, please confirm:

- [ ] Checkpoint file location (output_dir or separate?)
- [ ] Default behavior: auto-resume or require flag?
- [ ] Config change: warn and continue, or require --restart?
- [ ] Max retries default value (3?)
- [ ] Include file hash checking for source changes?
- [ ] Checkpoint save frequency (after each file, or configurable?)
