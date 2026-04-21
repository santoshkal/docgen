"""
RLM (Recursive Language Model) Phase 2 package.

Replaces the legacy per-section Phase 2 pipeline with the
RLM REPL + PageIndex + deterministic-generator approach
originally developed in ~/rlm/demo.

The SDK-dependent modules are imported lazily so that lightweight modules
(pageindex, deterministic) remain usable without the Claude Agent SDK
installed (useful for tests and offline tooling).

Public entry point:
    from rlm.orchestrator import run_phase2_rlm

    section_outputs = run_phase2_rlm(
        state=state,
        code_explanation=code_explanation_md,
        llm_config=llm_config,
        fallback_manager=fallback_manager,
        full_config=full_config,
    )
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from rlm.orchestrator import run_phase2_rlm  # noqa: F401

__all__ = ["run_phase2_rlm"]
