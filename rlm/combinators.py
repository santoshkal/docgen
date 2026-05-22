"""Pre-verified combinator library for the RLM planner.

Inspired by λ-RLM (arXiv 2603.20105). These four combinators give the planner
a small, trusted vocabulary for the patterns Phase 2 actually uses:

    MAP            — fan-out a function across a list  (every section)
    FILTER         — keep items matching a predicate    (retrieval, error-handling)
    REDUCE_CONCAT  — fold a list of strings into one    (final aggregation)
    CROSS          — Cartesian product                  (pairwise sections)

The only neural primitive (`M` in the paper) is the `llm_fn` callable threaded
into `run_planner`. These functions are deterministic, side-effect-free, and
total — they cannot raise unexpected runtime errors when given well-typed
inputs.
"""

from __future__ import annotations

from typing import Any, Callable, Iterable, Sequence, TypeVar

T = TypeVar("T")
U = TypeVar("U")


def MAP(fn: Callable[[T], U], items: Iterable[T]) -> list[U]:
    """Apply `fn` to each element of `items` and return the results as a list.

    Equivalent to `[fn(x) for x in items]`. Use this for the dominant pattern
    of "iterate over PageIndex blocks → llm_fn each":

        summaries = MAP(lambda b: llm_fn(f"Summarise: {b['text']}"), blocks)

    Note: the planner uses `asyncio.gather` with a semaphore for parallel
    leaf calls; `MAP(llm_fn, ...)` written by hand would be sequential.
    """
    return [fn(x) for x in items]


def FILTER(predicate: Callable[[T], bool], items: Iterable[T]) -> list[T]:
    """Keep only the elements of `items` for which `predicate(x)` is truthy.

    Equivalent to `[x for x in items if predicate(x)]`. Use this for retrieval
    and relevance filtering:

        relevant = FILTER(lambda b: "error" in b.get("tags", []), blocks)
    """
    return [x for x in items if predicate(x)]


def REDUCE_CONCAT(items: Sequence[Any], sep: str = "\n\n") -> str:
    """Join a sequence of strings into a single string with `sep` between them.

    Non-string items are coerced via `str()`. Empty input returns "". Use this
    as the aggregation step inside the planner chain:

        findings = REDUCE_CONCAT(parsed_leaf_outputs)
        # passed into the M_synth (synthesis) prompt
    """
    if not items:
        return ""
    return sep.join(x if isinstance(x, str) else str(x) for x in items)


def CROSS(a: Iterable[T], b: Iterable[U]) -> list[tuple[T, U]]:
    """Return the Cartesian product `[(a_i, b_j) for a_i in a for b_j in b]`.

    Use this for pairwise sections (e.g., inter-program-communication) where
    every caller must be considered against every callee:

        pairs = CROSS(callers, callees)
        edges = MAP(lambda p: llm_fn(f"Relate {p[0]} -> {p[1]}"), pairs)
    """
    a_list = list(a)
    b_list = list(b)
    return [(x, y) for x in a_list for y in b_list]
