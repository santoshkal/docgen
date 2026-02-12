"""
Checkpoint Manager for Batch Documentation Generation

Provides checkpoint/resume functionality for long-running batch processes:
- Saves progress after each file
- Resumes from interruption without re-processing completed files
- Retries failed files with configurable limits
- Detects config and source file changes

Usage:
    from checkpoint_manager import CheckpointManager

    checkpoint = CheckpointManager(output_dir, config_hash)
    state = checkpoint.load_or_create(source_files)

    for filename in checkpoint.get_pending_files():
        checkpoint.mark_file_started(filename)
        checkpoint.save()

        try:
            # Process file...
            checkpoint.mark_file_completed(filename, output_path)
        except Exception as e:
            checkpoint.mark_file_failed(filename, str(e))

        checkpoint.save()
"""

import hashlib
import json
import os
import tempfile
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml


class FileStatus(str, Enum):
    """Status of a file in the checkpoint."""
    PENDING = "pending"           # Not yet processed
    IN_PROGRESS = "in_progress"   # Currently being processed
    COMPLETED = "completed"       # Successfully completed
    FAILED = "failed"             # Failed after max retries
    SKIPPED = "skipped"           # Skipped by user request


class CheckpointManager:
    """
    Manages checkpoint state for batch documentation generation.

    Features:
    - Atomic saves (write to temp, then rename)
    - Config change detection
    - Source file change detection
    - Progress reporting
    """

    CHECKPOINT_VERSION = 1
    DEFAULT_FILENAME = ".checkpoint.yaml"

    def __init__(
        self,
        output_dir: Path,
        config_hash: str,
        checkpoint_filename: str = DEFAULT_FILENAME,
        max_retries: int = 3
    ):
        """
        Initialize checkpoint manager.

        Args:
            output_dir: Directory where checkpoint file is stored
            config_hash: Hash of current config for change detection
            checkpoint_filename: Name of checkpoint file
            max_retries: Maximum retries per file before marking as failed
        """
        self.output_dir = Path(output_dir)
        self.config_hash = config_hash
        self.checkpoint_filename = checkpoint_filename
        self.checkpoint_path = self.output_dir / checkpoint_filename
        self.max_retries = max_retries
        self.state: Optional[Dict[str, Any]] = None

    def load_or_create(self, source_files: List[Path]) -> Dict[str, Any]:
        """
        Load existing checkpoint or create new one.

        Args:
            source_files: List of source files to process

        Returns:
            Loaded or newly created checkpoint state
        """
        if self.checkpoint_path.exists():
            try:
                self.state = self._load_checkpoint()
                print(f"  ✓ Loaded checkpoint: {self.checkpoint_path}")
                print(f"    Started: {self.state.get('started_at', 'unknown')}")
                print(f"    Last updated: {self.state.get('last_updated', 'unknown')}")

                # Check for new files not in checkpoint
                self._sync_files_with_checkpoint(source_files)

                return self.state
            except Exception as e:
                print(f"  ⚠ Failed to load checkpoint: {e}")
                print(f"    Creating new checkpoint...")

        # Create new checkpoint
        self.state = self._create_checkpoint(source_files)
        self.save()
        print(f"  ✓ Created new checkpoint: {self.checkpoint_path}")

        return self.state

    def _load_checkpoint(self) -> Dict[str, Any]:
        """Load checkpoint from file."""
        with open(self.checkpoint_path, 'r') as f:
            return yaml.safe_load(f)

    def _create_checkpoint(self, source_files: List[Path]) -> Dict[str, Any]:
        """Create new checkpoint state."""
        now = datetime.now().isoformat()

        files = {}
        for file_path in source_files:
            filename = file_path.name
            files[filename] = {
                'status': FileStatus.PENDING.value,
                'started_at': None,
                'completed_at': None,
                'output_file': None,
                'file_hash': self.compute_file_hash(file_path),
                'retry_count': 0,
                'error': None,
                'file_path': str(file_path),
            }

        return {
            'version': self.CHECKPOINT_VERSION,
            'config_hash': self.config_hash,
            'source_dir': str(source_files[0].parent) if source_files else '',
            'output_dir': str(self.output_dir),
            'started_at': now,
            'last_updated': now,
            'total_files': len(source_files),
            'files': files,
        }

    def _sync_files_with_checkpoint(self, source_files: List[Path]) -> None:
        """
        Sync checkpoint with current source files.

        Adds new files and checks for source changes.
        """
        if not self.state:
            return

        existing_files = set(self.state.get('files', {}).keys())
        current_files = {f.name: f for f in source_files}

        # Add new files
        for filename, file_path in current_files.items():
            if filename not in existing_files:
                print(f"    + New file detected: {filename}")
                self.state['files'][filename] = {
                    'status': FileStatus.PENDING.value,
                    'started_at': None,
                    'completed_at': None,
                    'output_file': None,
                    'file_hash': self.compute_file_hash(file_path),
                    'retry_count': 0,
                    'error': None,
                    'file_path': str(file_path),
                }
                self.state['total_files'] = len(self.state['files'])

        # Check for source changes on completed files
        for filename, file_info in self.state['files'].items():
            if file_info['status'] == FileStatus.COMPLETED.value:
                if filename in current_files:
                    current_hash = self.compute_file_hash(current_files[filename])
                    if current_hash != file_info.get('file_hash'):
                        print(f"    ~ Source changed: {filename} (will reprocess)")
                        file_info['status'] = FileStatus.PENDING.value
                        file_info['file_hash'] = current_hash
                        file_info['retry_count'] = 0

    def save(self) -> None:
        """
        Save current checkpoint state atomically.

        Uses write-to-temp-then-rename pattern for crash safety.
        """
        if not self.state:
            return

        # Update timestamp
        self.state['last_updated'] = datetime.now().isoformat()

        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Write to temp file first, then rename (atomic on most filesystems)
        temp_fd, temp_path = tempfile.mkstemp(
            dir=self.output_dir,
            prefix='.checkpoint_',
            suffix='.tmp'
        )

        try:
            with os.fdopen(temp_fd, 'w') as f:
                yaml.dump(self.state, f, default_flow_style=False, sort_keys=False)

            # Atomic rename
            os.replace(temp_path, self.checkpoint_path)

        except Exception:
            # Clean up temp file on error
            if os.path.exists(temp_path):
                os.unlink(temp_path)
            raise

    def mark_file_started(self, filename: str) -> None:
        """
        Mark a file as in_progress before processing.

        Args:
            filename: Name of file being processed
        """
        if not self.state or filename not in self.state['files']:
            return

        self.state['files'][filename]['status'] = FileStatus.IN_PROGRESS.value
        self.state['files'][filename]['started_at'] = datetime.now().isoformat()

    def mark_file_completed(self, filename: str, output_file: str) -> None:
        """
        Mark a file as successfully completed.

        Args:
            filename: Name of completed file
            output_file: Path to generated documentation
        """
        if not self.state or filename not in self.state['files']:
            return

        self.state['files'][filename]['status'] = FileStatus.COMPLETED.value
        self.state['files'][filename]['completed_at'] = datetime.now().isoformat()
        self.state['files'][filename]['output_file'] = output_file
        self.state['files'][filename]['error'] = None

    def mark_file_failed(self, filename: str, error: str) -> None:
        """
        Mark a file as failed and increment retry count.

        Args:
            filename: Name of failed file
            error: Error message
        """
        if not self.state or filename not in self.state['files']:
            return

        file_info = self.state['files'][filename]
        file_info['retry_count'] = file_info.get('retry_count', 0) + 1
        file_info['error'] = error

        if file_info['retry_count'] >= self.max_retries:
            file_info['status'] = FileStatus.FAILED.value
        else:
            # Keep as pending for retry
            file_info['status'] = FileStatus.PENDING.value

    def mark_file_skipped(self, filename: str, reason: str = None) -> None:
        """
        Mark a file as skipped.

        Args:
            filename: Name of skipped file
            reason: Optional reason for skipping
        """
        if not self.state or filename not in self.state['files']:
            return

        self.state['files'][filename]['status'] = FileStatus.SKIPPED.value
        if reason:
            self.state['files'][filename]['error'] = f"Skipped: {reason}"

    def get_pending_files(self) -> List[str]:
        """
        Get list of files that need processing.

        Returns files with status: pending or in_progress (interrupted).

        Returns:
            List of filenames to process
        """
        if not self.state:
            return []

        pending = []
        for filename, file_info in self.state['files'].items():
            status = file_info.get('status')
            if status in [FileStatus.PENDING.value, FileStatus.IN_PROGRESS.value]:
                pending.append(filename)

        return sorted(pending)

    def get_files_to_retry(self) -> List[str]:
        """
        Get list of failed files that can be retried.

        Returns:
            List of filenames that failed but haven't exceeded max_retries
        """
        if not self.state:
            return []

        to_retry = []
        for filename, file_info in self.state['files'].items():
            if file_info.get('status') == FileStatus.FAILED.value:
                if file_info.get('retry_count', 0) < self.max_retries:
                    to_retry.append(filename)

        return sorted(to_retry)

    def get_completed_files(self) -> List[str]:
        """
        Get list of successfully completed files.

        Returns:
            List of completed filenames
        """
        if not self.state:
            return []

        return sorted([
            filename for filename, file_info in self.state['files'].items()
            if file_info.get('status') == FileStatus.COMPLETED.value
        ])

    def get_failed_files(self) -> List[str]:
        """
        Get list of files that failed after max retries.

        Returns:
            List of failed filenames
        """
        if not self.state:
            return []

        return sorted([
            filename for filename, file_info in self.state['files'].items()
            if file_info.get('status') == FileStatus.FAILED.value
        ])

    def get_file_path(self, filename: str) -> Optional[str]:
        """
        Get the full file path for a filename.

        Args:
            filename: Name of the file

        Returns:
            Full path to the file, or None if not found
        """
        if not self.state or filename not in self.state['files']:
            return None

        return self.state['files'][filename].get('file_path')

    def config_changed(self) -> bool:
        """
        Check if config has changed since checkpoint was created.

        Returns:
            True if config hash differs
        """
        if not self.state:
            return False

        return self.state.get('config_hash') != self.config_hash

    def get_progress(self) -> Dict[str, Any]:
        """
        Get current progress statistics.

        Returns:
            Dict with progress information
        """
        if not self.state:
            return {
                'total': 0,
                'completed': 0,
                'failed': 0,
                'pending': 0,
                'in_progress': 0,
                'skipped': 0,
                'percent_complete': 0.0,
            }

        total = self.state.get('total_files', 0)
        completed = len(self.get_completed_files())
        failed = len(self.get_failed_files())
        pending = len(self.get_pending_files())

        in_progress = sum(
            1 for f in self.state['files'].values()
            if f.get('status') == FileStatus.IN_PROGRESS.value
        )

        skipped = sum(
            1 for f in self.state['files'].values()
            if f.get('status') == FileStatus.SKIPPED.value
        )

        percent = (completed / total * 100) if total > 0 else 0.0

        # Calculate elapsed time
        started_at = self.state.get('started_at')
        elapsed = None
        if started_at:
            try:
                start_dt = datetime.fromisoformat(started_at)
                elapsed = datetime.now() - start_dt
            except ValueError:
                pass

        return {
            'total': total,
            'completed': completed,
            'failed': failed,
            'pending': pending,
            'in_progress': in_progress,
            'skipped': skipped,
            'percent_complete': percent,
            'elapsed': str(elapsed).split('.')[0] if elapsed else None,
            'started_at': started_at,
            'last_updated': self.state.get('last_updated'),
        }

    def get_summary_report(self) -> str:
        """
        Generate human-readable summary report.

        Returns:
            Formatted string with progress details
        """
        progress = self.get_progress()

        # Build progress bar
        bar_width = 30
        filled = int(bar_width * progress['percent_complete'] / 100)
        bar = '█' * filled + '░' * (bar_width - filled)

        lines = [
            "",
            "═" * 70,
            "CHECKPOINT STATUS",
            "═" * 70,
            f"Checkpoint file: {self.checkpoint_path}",
            f"Output directory: {self.output_dir}",
            "",
            f"Started: {progress['started_at'] or 'N/A'}",
            f"Last updated: {progress['last_updated'] or 'N/A'}",
            f"Elapsed time: {progress['elapsed'] or 'N/A'}",
            "",
            f"Progress: [{bar}] {progress['completed']}/{progress['total']} ({progress['percent_complete']:.1f}%)",
            "",
            f"  ✓ Completed:   {progress['completed']:4d} files",
            f"  ✗ Failed:      {progress['failed']:4d} files",
            f"  ○ Pending:     {progress['pending']:4d} files",
            f"  ⊘ Skipped:     {progress['skipped']:4d} files",
        ]

        # Add failed files list
        failed_files = self.get_failed_files()
        if failed_files:
            lines.append("")
            lines.append("Failed files:")
            for i, filename in enumerate(failed_files[:10], 1):
                error = self.state['files'][filename].get('error', 'Unknown error')
                # Truncate error message
                if len(error) > 50:
                    error = error[:47] + "..."
                lines.append(f"  {i}. {filename}")
                lines.append(f"     Error: {error}")

            if len(failed_files) > 10:
                lines.append(f"  ... and {len(failed_files) - 10} more")

        lines.append("═" * 70)

        return "\n".join(lines)

    def delete_checkpoint(self) -> None:
        """Delete checkpoint file (for --restart)."""
        if self.checkpoint_path.exists():
            self.checkpoint_path.unlink()
            print(f"  ✓ Deleted checkpoint: {self.checkpoint_path}")
        self.state = None

    def reset_failed_files(self) -> int:
        """
        Reset failed files to pending status for retry.

        Returns:
            Number of files reset
        """
        if not self.state:
            return 0

        count = 0
        for filename, file_info in self.state['files'].items():
            if file_info.get('status') == FileStatus.FAILED.value:
                file_info['status'] = FileStatus.PENDING.value
                file_info['retry_count'] = 0
                file_info['error'] = None
                count += 1

        return count

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
            SHA256 hash string (first 16 chars)
        """
        # Extract relevant config fields
        relevant = {
            'llm': config.get('llm', {}),
            'template': config.get('template', {}),
        }

        # Create deterministic JSON string
        config_str = json.dumps(relevant, sort_keys=True)

        # Compute hash
        return hashlib.sha256(config_str.encode()).hexdigest()[:16]

    @staticmethod
    def compute_file_hash(file_path: Path) -> str:
        """
        Compute SHA256 hash of file contents.

        Args:
            file_path: Path to file

        Returns:
            SHA256 hash string (first 16 chars)
        """
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256()
                for chunk in iter(lambda: f.read(8192), b''):
                    file_hash.update(chunk)
            return file_hash.hexdigest()[:16]
        except Exception:
            return "unknown"
