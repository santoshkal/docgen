#!/usr/bin/env python3
"""
CLI wrapper around questionnaire_aggregator.

Kept for ad-hoc runs against an already-assembled documentation markdown file.
The aggregation logic itself lives in `questionnaire_aggregator` at the agent
root and is the same code path the Phase 2 → Phase 3 handoff calls internally.

Usage:
    python3 scripts/aggregate_questionnaires.py path/to/doc.md --in-place
    python3 scripts/aggregate_questionnaires.py path/to/doc.md -o out.md
    python3 scripts/aggregate_questionnaires.py path/to/docs-dir/ --in-place
    python3 scripts/aggregate_questionnaires.py path/to/doc.md --program-name MyProg
"""

from __future__ import annotations

import sys
from pathlib import Path

# Make the agent root importable when this script is run directly.
_AGENT_ROOT = Path(__file__).resolve().parent.parent
if str(_AGENT_ROOT) not in sys.path:
    sys.path.insert(0, str(_AGENT_ROOT))

from questionnaire_aggregator import cli  # noqa: E402

if __name__ == "__main__":
    sys.exit(cli())
