"""One-shot Claude sub-LLM helper for the Phase 2 planner.

Adapted from the old ~rlm/pipeline_repl.py — kept only the one-shot
`call_claude` path. The multi-turn `ClaudeSDKClient` path is no longer used
anywhere in the project.

Behaviour preserved from the original:
  - 5x retry with exponential backoff on transient (429/500/overloaded) errors.
  - Non-transient errors trigger `fallback_manager.trigger_fallback(err)` so
    subsequent calls in the session resolve to the configured fallback model.
  - `get_model` is consulted before every attempt so fallback state takes
    effect mid-flight (within the retry loop).

The Claude Agent SDK runs each call as `query()` with an empty `allowed_tools`
list and a deny-list to prevent the sub-LLM from invoking built-in tools.
"""

from __future__ import annotations

import asyncio
from typing import Any, Callable, Dict, Optional, Tuple

try:
    from claude_agent_sdk import (
        AssistantMessage,
        ClaudeAgentOptions,
        ResultMessage,
        TextBlock,
        query,
    )
except ImportError as e:  # pragma: no cover — surfaced at import time
    raise ImportError(
        "claude-agent-sdk is required for the Phase 2 planner. "
        "Install with: pip install claude-agent-sdk"
    ) from e


# Built-in SDK tools the sub-LLM must not be able to invoke. Matches the
# previous REPL-engine deny-list verbatim.
DISALLOWED_TOOLS = [
    "Bash", "Edit", "Read", "Write", "Glob", "Grep", "NotebookEdit",
    "WebFetch", "WebSearch", "TodoWrite", "BashOutput", "KillBash",
    "ExitPlanMode", "ListMcpResources", "ReadMcpResource", "Task",
    "AskUserQuestion",
]


async def call_claude(
    prompt: str,
    system_prompt: Optional[str] = None,
    model: Optional[str] = None,
    max_thinking_tokens: Optional[int] = None,
    max_output_tokens: Optional[int] = None,
    max_retries: int = 5,
    base_delay: float = 2.0,
    fallback_manager: Optional[Any] = None,
    get_model: Optional[Callable[[], str]] = None,
) -> Tuple[str, Optional[Dict[str, Any]]]:
    """
    One-shot Claude call via `claude_agent_sdk.query()` with retry + fallback.

    Args:
        prompt: The prompt to send.
        system_prompt: Optional system-prompt override.
        model: Initial model. Only used on the first attempt when `get_model`
            is None; otherwise `get_model` is consulted on every attempt.
        max_thinking_tokens, max_output_tokens: Forwarded to the SDK.
        max_retries, base_delay: Exponential-backoff retry policy for transient
            (429 / 500 / overloaded) errors.
        fallback_manager: Optional LLMFallbackManager. On non-transient errors
            (and only when a fallback is configured and not yet active),
            `trigger_fallback(err)` is called so subsequent calls in the session
            switch to the fallback model.
        get_model: Callable returning the current effective model name. Called
            before every attempt so fallback kicks in mid-flight.

    Returns:
        (response_text, result_info_dict).
    """
    last_error: Optional[Exception] = None

    for attempt in range(max_retries):
        effective_model = get_model() if get_model else model

        opts: Dict[str, Any] = {
            "allowed_tools": [],
            "disallowed_tools": DISALLOWED_TOOLS,
        }
        if effective_model:
            opts["model"] = effective_model
        if system_prompt:
            opts["system_prompt"] = system_prompt
        if max_thinking_tokens is not None:
            opts["max_thinking_tokens"] = max_thinking_tokens
        if max_output_tokens is not None:
            opts["env"] = {"CLAUDE_CODE_MAX_OUTPUT_TOKENS": str(max_output_tokens)}

        options = ClaudeAgentOptions(**opts)

        try:
            response_text = ""
            result_info: Optional[Dict[str, Any]] = None

            async for message in query(prompt=prompt, options=options):
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            response_text += block.text
                elif isinstance(message, ResultMessage):
                    result_info = {
                        "usage": message.usage,
                        "total_cost_usd": message.total_cost_usd,
                        "duration_ms": message.duration_ms,
                        "duration_api_ms": message.duration_api_ms,
                        "is_error": message.is_error,
                        "num_turns": message.num_turns,
                        "session_id": message.session_id,
                    }
                    if message.is_error:
                        raise RuntimeError(
                            f"Claude returned error: {message.result or response_text}"
                        )

            return response_text, result_info

        except Exception as e:
            error_str = str(e).lower()
            transient = (
                "429" in str(e)
                or "rate" in error_str
                or "too many" in error_str
                or "500" in str(e)
                or "internal server error" in error_str
                or "overloaded" in error_str
            )
            last_error = e

            if transient and attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt)
                print(
                    f"    Transient SDK error, waiting {delay}s "
                    f"({attempt + 1}/{max_retries}): {str(e)[:180]}"
                )
                await asyncio.sleep(delay)
                continue

            # Non-transient — trigger fallback if configured and not yet active,
            # then retry once on the fallback model.
            if (
                fallback_manager is not None
                and getattr(fallback_manager, "has_fallback", lambda: False)()
                and not getattr(fallback_manager, "is_fallback_active", lambda: False)()
            ):
                fallback_manager.trigger_fallback(e)
                if attempt < max_retries - 1:
                    continue

            raise

    if last_error:
        raise last_error
    return "", None
