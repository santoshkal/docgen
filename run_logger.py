"""
Centralized Run Logging System

Creates a per-run directory that centralizes all artifacts for easy post-mortem:
- Console output (tee'd stdout/stderr)
- LLM trace files (per-program subdirectories)
- Debug request files (per-program subdirectories)
- Run manifest with per-program status

Directory structure:
    <docs_path>/runs/<run-id>/
    ├── console.log
    ├── console_stderr.log
    ├── run-manifest.yaml
    ├── traces/<program>/
    └── requests/<program>/
"""

import sys
import yaml
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


class TeeStream:
    """
    Wraps a stream (stdout/stderr) to write to both the original stream and a log file.

    Flushes after every write for crash safety so the log file is complete
    up to the point of any crash.
    """

    def __init__(self, original_stream, log_file_path: Path):
        self.original = original_stream
        self.log_file = open(log_file_path, 'a', encoding='utf-8')

    def write(self, data):
        self.original.write(data)
        self.original.flush()
        try:
            self.log_file.write(data)
            self.log_file.flush()
        except Exception:
            pass  # Never let logging break the program

    def flush(self):
        self.original.flush()
        try:
            self.log_file.flush()
        except Exception:
            pass

    def close_log(self):
        """Close the log file (but not the original stream)."""
        try:
            self.log_file.close()
        except Exception:
            pass

    def __getattr__(self, name):
        """Delegate everything else (isatty, fileno, etc.) to original stream."""
        return getattr(self.original, name)


class RunLogger:
    """
    Manages a per-run directory that centralizes all artifacts.

    Lifecycle:
        1. __init__()         → creates run dir, writes partial manifest
        2. start_console_tee()→ installs TeeStream on stdout/stderr
        3. get_trace_dir()    → returns per-program trace directory
        4. get_request_dir()  → returns per-program request directory
        5. record_program_result() → tracks per-program status
        6. finalize()         → writes final manifest, restores streams
    """

    def __init__(self, output_dir: str, run_id: Optional[str] = None):
        """
        Create the run directory and write an initial (in_progress) manifest.

        Args:
            output_dir: Base output directory (docs_path). Run dir will be
                        created under <output_dir>/runs/<run_id>/
            run_id: Optional explicit run ID. Defaults to ISO timestamp.
        """
        if run_id is None:
            run_id = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

        self.run_id = run_id
        self.output_dir = Path(output_dir)
        self.run_dir = self.output_dir / "runs" / run_id
        self.run_dir.mkdir(parents=True, exist_ok=True)

        # Sub-directories (created lazily per-program)
        self.traces_dir = self.run_dir / "traces"
        self.requests_dir = self.run_dir / "requests"

        # Program tracking
        self._current_program: Optional[str] = None
        self._program_results: List[Dict[str, Any]] = []
        self._start_time = datetime.now()

        # Stream backup for restore on finalize
        self._original_stdout = None
        self._original_stderr = None
        self._tee_stdout: Optional[TeeStream] = None
        self._tee_stderr: Optional[TeeStream] = None

        # Write partial manifest immediately (crash safety)
        self._write_manifest(status="in_progress")

        print(f"→ Run logger initialized: {self.run_dir}")

    def start_console_tee(self):
        """Install TeeStream on stdout and stderr."""
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr

        console_log = self.run_dir / "console.log"
        stderr_log = self.run_dir / "console_stderr.log"

        self._tee_stdout = TeeStream(self._original_stdout, console_log)
        self._tee_stderr = TeeStream(self._original_stderr, stderr_log)

        sys.stdout = self._tee_stdout
        sys.stderr = self._tee_stderr

    def get_trace_dir(self, program_name: str) -> Path:
        """Get (and create) the trace directory for a program."""
        d = self.traces_dir / program_name
        d.mkdir(parents=True, exist_ok=True)
        return d

    def get_trace_log_path(self, program_name: str) -> str:
        """Get full path to llm_trace.jsonl for a program."""
        return str(self.get_trace_dir(program_name) / "llm_trace.jsonl")

    def get_request_dir(self, program_name: str) -> Path:
        """Get (and create) the request directory for a program."""
        d = self.requests_dir / program_name
        d.mkdir(parents=True, exist_ok=True)
        return d

    def set_current_program(self, program_name: str):
        """Set the program currently being processed."""
        self._current_program = program_name

    def get_current_program(self) -> Optional[str]:
        """Get the program currently being processed."""
        return self._current_program

    def record_program_result(
        self,
        name: str,
        status: str,
        output_path: Optional[str] = None,
        error: Optional[str] = None,
    ):
        """
        Record the result of processing a single program.

        Args:
            name: Program name
            status: 'completed' or 'failed'
            output_path: Path to generated doc (on success)
            error: Error message (on failure)
        """
        entry: Dict[str, Any] = {
            "program": name,
            "status": status,
            "timestamp": datetime.now().isoformat(),
        }
        if output_path:
            entry["output_path"] = output_path
        if error:
            entry["error"] = error
        self._program_results.append(entry)

    def finalize(
        self,
        config_hash: Optional[str] = None,
        total_files: Optional[int] = None,
        mode: Optional[str] = None,
    ):
        """
        Write final run-manifest.yaml and restore stdout/stderr.

        Args:
            config_hash: Hash of the config used for this run
            total_files: Total number of files targeted
            mode: 'batch' or 'single'
        """
        self._write_manifest(
            status="completed",
            config_hash=config_hash,
            total_files=total_files,
            mode=mode,
        )

        # Restore original streams
        if self._tee_stdout is not None:
            self._tee_stdout.close_log()
            sys.stdout = self._original_stdout
            self._tee_stdout = None

        if self._tee_stderr is not None:
            self._tee_stderr.close_log()
            sys.stderr = self._original_stderr
            self._tee_stderr = None

        print(f"→ Run finalized: {self.run_dir / 'run-manifest.yaml'}")

    # ── internal ──────────────────────────────────────────────────────

    def _write_manifest(
        self,
        status: str,
        config_hash: Optional[str] = None,
        total_files: Optional[int] = None,
        mode: Optional[str] = None,
    ):
        """Write (or overwrite) run-manifest.yaml."""
        completed = sum(1 for r in self._program_results if r["status"] == "completed")
        failed = sum(1 for r in self._program_results if r["status"] == "failed")

        manifest: Dict[str, Any] = {
            "run_id": self.run_id,
            "status": status,
            "started_at": self._start_time.isoformat(),
            "updated_at": datetime.now().isoformat(),
            "programs_completed": completed,
            "programs_failed": failed,
        }
        if mode:
            manifest["mode"] = mode
        if config_hash:
            manifest["config_hash"] = config_hash
        if total_files is not None:
            manifest["total_files"] = total_files
        if self._program_results:
            manifest["programs"] = self._program_results

        manifest_path = self.run_dir / "run-manifest.yaml"
        with open(manifest_path, "w") as f:
            yaml.dump(manifest, f, default_flow_style=False, sort_keys=False)


# ═══════════════════════════════════════════════════════════════════════
# MODULE-LEVEL ACCESSORS (same pattern as llm_tracer.py)
# ═══════════════════════════════════════════════════════════════════════

_run_logger: Optional[RunLogger] = None


def init_run_logger(output_dir: str, run_id: Optional[str] = None) -> RunLogger:
    """
    Initialize the global RunLogger.

    Args:
        output_dir: Base output directory (docs_path)
        run_id: Optional explicit run ID

    Returns:
        RunLogger instance
    """
    global _run_logger
    _run_logger = RunLogger(output_dir, run_id)
    return _run_logger


def get_run_logger() -> Optional[RunLogger]:
    """Get global RunLogger instance, or None if not initialized."""
    return _run_logger
