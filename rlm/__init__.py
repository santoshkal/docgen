"""
Phase 2 package — PageIndex + deterministic generators + λ-RLM planner.

Replaces the legacy exec()-based REPL pipeline with the trusted-combinator
planner approach (Φ = M_synth ∘ REDUCE_CONCAT ∘ MAP(M, leaf_prompt) ∘ FILTER).
The root LLM never authors control flow; the only neural calls happen at MAP
leaves and a single synthesis step.

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
