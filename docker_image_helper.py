"""
Docker image presence helper for MCP server containers.

Used by `mcp_metadata_generator.py` and `mermaid_validator.py` to guarantee
that a referenced image is available locally before issuing `docker run`.

Behaviour for `ensure_image(ref)`:

    1. `docker image inspect <ref>` — exit 0 ⇒ image present, return.
    2. Otherwise `docker pull <ref>`. On success, return. On failure, raise
       `RuntimeError` quoting the image reference and the underlying docker
       stderr so misconfiguration is loud.

Designed for fully-qualified references (e.g.
`ghcr.io/<org>/<image>:<tag>`) but works with any string `docker` accepts.

Each (ref) is processed at most once per Python process — the in-process
cache means batch runs over many files only pull a given image once.
"""

from __future__ import annotations

import subprocess
import threading
from typing import Set


_ENSURED: Set[str] = set()
_LOCK = threading.Lock()


def _docker_available() -> bool:
    """Return True if the `docker` CLI is on PATH and responsive."""
    try:
        subprocess.run(
            ["docker", "version", "--format", "{{.Server.Version}}"],
            check=True,
            capture_output=True,
            timeout=10,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return False


def _image_present_locally(ref: str) -> bool:
    """True iff `docker image inspect <ref>` exits 0."""
    result = subprocess.run(
        ["docker", "image", "inspect", ref],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def _pull_image(ref: str) -> None:
    """Pull `ref` from its registry. Raises RuntimeError on failure with the
    underlying docker stderr inlined."""
    print(f"  → docker pull {ref}")
    result = subprocess.run(
        ["docker", "pull", ref],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        stderr = (result.stderr or "").strip()
        stdout = (result.stdout or "").strip()
        detail = stderr or stdout or f"exit code {result.returncode}"
        raise RuntimeError(
            f"docker pull failed for image reference {ref!r}:\n{detail}"
        )
    # Print final status line from `docker pull` (e.g. "Status: Downloaded
    # newer image for ...") so the operator sees a clear success marker.
    last_status = ""
    for line in (result.stdout or "").splitlines():
        if line.startswith("Status:"):
            last_status = line.strip()
    if last_status:
        print(f"    {last_status}")


def ensure_image(ref: str) -> None:
    """Make sure `ref` is available locally; pull from its registry otherwise.

    Args:
        ref: Fully-qualified or bare docker image reference. Empty/None is a
            no-op.

    Raises:
        RuntimeError: if the docker CLI is not available, or if the image
            cannot be pulled from its registry.
    """
    if not ref:
        return

    with _LOCK:
        if ref in _ENSURED:
            return

        if not _docker_available():
            raise RuntimeError(
                "docker CLI not found or not responsive. "
                "Install Docker and ensure the daemon is running before "
                "invoking MCP-server-backed metadata generation or mermaid "
                "validation."
            )

        if _image_present_locally(ref):
            print(f"  ✓ Image present locally: {ref}")
            _ENSURED.add(ref)
            return

        print(f"  ⚠ Image not found locally: {ref}")
        _pull_image(ref)
        _ENSURED.add(ref)


def reset_cache() -> None:
    """Forget all previously-ensured images. Test-only."""
    with _LOCK:
        _ENSURED.clear()
