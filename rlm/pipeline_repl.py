"""
Sandboxed REPL environment for the RLM iteration loop.

Adapted from ~/rlm/demo/pipeline.py. The notable differences here:

- `call_claude` accepts an optional `fallback_manager` and a `get_model`
  callable, so fallback state (session-wide) can override the model on every
  retry in a way that matches the existing LLMFallbackManager pattern.
- `PipelineREPL` records sub-LLM call state so trajectory logs can be written
  by the caller.

The REPL exposes `context`, `metadata`, `section_instruction`, `section_title`,
`program_name`, `llm_query()`, `llm_query_batched()`, `FINAL_VAR()`, and
`SHOW_VARS()` — the surface the root LLM is trained against.
"""

from __future__ import annotations

import asyncio
import io
import os
import sys
import threading
import time
from typing import Any, Callable, Dict, List, Optional, Tuple

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
        "claude-agent-sdk is required for the RLM Phase 2 pipeline. "
        "Install with: pip install claude-agent-sdk"
    ) from e


# All built-in tools to disallow for pure LLM calls.
DISALLOWED_TOOLS = [
    "Bash", "Edit", "Read", "Write", "Glob", "Grep", "NotebookEdit",
    "WebFetch", "WebSearch", "TodoWrite", "BashOutput", "KillBash",
    "ExitPlanMode", "ListMcpResources", "ReadMcpResource", "Task",
    "AskUserQuestion",
]


# ---------------------------------------------------------------------------
# Safe builtins for exec()'d REPL blocks
# ---------------------------------------------------------------------------

_SAFE_BUILTINS: Dict[str, Any] = {
    "print": print, "len": len, "str": str, "int": int, "float": float,
    "list": list, "dict": dict, "set": set, "tuple": tuple, "bool": bool,
    "type": type, "isinstance": isinstance, "issubclass": issubclass,
    "enumerate": enumerate, "zip": zip, "map": map, "filter": filter,
    "sorted": sorted, "reversed": reversed, "range": range,
    "min": min, "max": max, "sum": sum, "abs": abs, "round": round,
    "any": any, "all": all, "pow": pow, "divmod": divmod,
    "chr": chr, "ord": ord, "hex": hex, "bin": bin, "oct": oct,
    "repr": repr, "ascii": ascii, "format": format, "hash": hash, "id": id,
    "iter": iter, "next": next, "slice": slice, "callable": callable,
    "hasattr": hasattr, "getattr": getattr, "setattr": setattr, "delattr": delattr,
    "dir": dir, "vars": vars,
    "bytes": bytes, "bytearray": bytearray, "memoryview": memoryview,
    "complex": complex, "object": object, "super": super,
    "property": property, "staticmethod": staticmethod, "classmethod": classmethod,
    "__import__": __import__, "open": open,
    # Exceptions
    "Exception": Exception, "BaseException": BaseException,
    "ValueError": ValueError, "TypeError": TypeError, "KeyError": KeyError,
    "IndexError": IndexError, "AttributeError": AttributeError,
    "FileNotFoundError": FileNotFoundError, "OSError": OSError, "IOError": IOError,
    "RuntimeError": RuntimeError, "NameError": NameError, "ImportError": ImportError,
    "StopIteration": StopIteration, "AssertionError": AssertionError,
    "NotImplementedError": NotImplementedError,
    "ArithmeticError": ArithmeticError, "LookupError": LookupError, "Warning": Warning,
    # Blocked
    "input": None, "eval": None, "exec": None, "compile": None,
    "globals": None, "locals": None,
}


# ---------------------------------------------------------------------------
# Sub-LLM call with fallback-aware retry
# ---------------------------------------------------------------------------


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
        prompt, system_prompt, model, max_thinking_tokens, max_output_tokens:
            Forwarded to the SDK. `model` is only used on the first attempt;
            `get_model` (if provided) is consulted before every retry so fallback
            state can override the model session-wide.
        max_retries, base_delay: Exponential-backoff retry policy for transient
            (429 / 500 / overloaded) errors.
        fallback_manager: Optional LLMFallbackManager. On non-transient errors,
            `trigger_fallback(err)` is called before the next retry so that
            subsequent calls in the session switch to the fallback model.
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


# ---------------------------------------------------------------------------
# Sandboxed REPL
# ---------------------------------------------------------------------------


class PipelineREPL:
    """
    Sandboxed REPL environment for the RLM iteration loop.

    Exposes `llm_query()`, `llm_query_batched()`, `SHOW_VARS()`, and
    `FINAL_VAR()` inside the exec namespace. Sub-LLM calls go through
    `call_claude()`.
    """

    def __init__(
        self,
        llm_config: Dict[str, Any],
        fallback_manager: Optional[Any] = None,
        get_sub_model: Optional[Callable[[], str]] = None,
    ):
        """
        Args:
            llm_config: dict with sub_model, max_output_tokens, max_thinking_tokens.
            fallback_manager: optional LLMFallbackManager; triggered on sub-LLM failure.
            get_sub_model: optional callable returning the current effective sub-model.
                When provided, it is consulted before every sub-LLM call (so
                fallback-state model swaps take effect immediately).
        """
        self.llm_config = llm_config
        self._fallback_manager = fallback_manager
        self._get_sub_model = get_sub_model
        self._lock = threading.Lock()
        self._sub_llm_calls = 0
        self._total_cost = 0.0
        self._pending_sub_calls: List[Dict[str, Any]] = []

        # Concurrency limit for sub-LLM calls (CPU count).
        self._max_concurrent = os.cpu_count() or 4

        # Dedicated background event loop for sub-LLM calls (exec is sync, SDK is async).
        self._sub_loop = asyncio.new_event_loop()
        self._sub_thread = threading.Thread(
            target=self._sub_loop.run_forever, daemon=True
        )
        self._sub_thread.start()

        self.globals: Dict[str, Any] = {
            "__builtins__": _SAFE_BUILTINS.copy(),
            "__name__": "__main__",
        }
        self.locals: Dict[str, Any] = {}

        self.globals["llm_query"] = self._llm_query
        self.globals["llm_query_batched"] = self._llm_query_batched
        self.globals["FINAL_VAR"] = self._final_var
        self.globals["SHOW_VARS"] = self._show_vars

    # --- Public API ---

    def add_context(self, data: Any, var_name: str = "context") -> None:
        self.locals[var_name] = data

    def execute_code(self, code: str) -> Dict[str, Any]:
        self._pending_sub_calls = []
        with self._lock:
            old_stdout, old_stderr = sys.stdout, sys.stderr
            stdout_buf, stderr_buf = io.StringIO(), io.StringIO()
            exec_start = time.time()
            try:
                sys.stdout, sys.stderr = stdout_buf, stderr_buf
                combined = {**self.globals, **self.locals}
                exec(code, combined, combined)  # noqa: S102 — sandboxed REPL
                for key, value in combined.items():
                    if key not in self.globals and not key.startswith("_"):
                        self.locals[key] = value
                stdout = stdout_buf.getvalue()
                stderr = stderr_buf.getvalue()
            except Exception as e:
                stdout = stdout_buf.getvalue()
                stderr = stderr_buf.getvalue() + f"\n{type(e).__name__}: {e}"
            finally:
                sys.stdout, sys.stderr = old_stdout, old_stderr
                exec_elapsed = time.time() - exec_start
        return {
            "stdout": stdout,
            "stderr": stderr,
            "sub_calls": list(self._pending_sub_calls),
            "execution_time": exec_elapsed,
        }

    def get_stats(self) -> Dict[str, Any]:
        return {
            "sub_llm_calls": self._sub_llm_calls,
            "sub_llm_cost_usd": self._total_cost,
        }

    def cleanup(self) -> None:
        self._sub_loop.call_soon_threadsafe(self._sub_loop.stop)
        self._sub_thread.join(timeout=5)

    # --- REPL-exposed callables ---

    def _current_sub_model(self) -> str:
        if self._get_sub_model is not None:
            return self._get_sub_model()
        return self.llm_config.get("sub_model", "claude-sonnet-4-20250514")

    def _llm_query(self, prompt: str, model: Optional[str] = None) -> str:
        """Single sub-LLM call. `model` override is honored only for this call."""
        sub_model = model or self._current_sub_model()
        call_start = time.time()
        try:
            coro = call_claude(
                prompt=prompt,
                model=sub_model,
                max_thinking_tokens=self.llm_config.get("max_thinking_tokens"),
                max_output_tokens=self.llm_config.get("max_output_tokens"),
                fallback_manager=self._fallback_manager,
                get_model=None if model else self._current_sub_model,
            )
            future = asyncio.run_coroutine_threadsafe(coro, self._sub_loop)
            response_text, result_info = future.result()
            call_elapsed = time.time() - call_start
            self._sub_llm_calls += 1
            cost = (result_info or {}).get("total_cost_usd") or 0
            self._total_cost += cost
            self._pending_sub_calls.append({
                "model": sub_model, "prompt": prompt, "prompt_length": len(prompt),
                "response": response_text, "response_length": len(response_text),
                "cost_usd": cost, "duration_s": round(call_elapsed, 2),
                "usage": (result_info or {}).get("usage"), "is_error": False,
            })
            return response_text
        except Exception as e:
            call_elapsed = time.time() - call_start
            self._pending_sub_calls.append({
                "model": sub_model, "prompt": prompt, "prompt_length": len(prompt),
                "response": str(e), "response_length": 0,
                "cost_usd": 0, "duration_s": round(call_elapsed, 2),
                "usage": None, "is_error": True,
            })
            return f"Error: LLM query failed - {e}"

    def _llm_query_batched(
        self, prompts: List[str], model: Optional[str] = None
    ) -> List[str]:
        """Run several sub-LLM calls concurrently (CPU-count semaphore)."""
        sub_model = model or self._current_sub_model()
        sem = asyncio.Semaphore(self._max_concurrent)

        async def _throttled_call(prompt: str):
            async with sem:
                return await call_claude(
                    prompt=prompt,
                    model=sub_model,
                    max_thinking_tokens=self.llm_config.get("max_thinking_tokens"),
                    max_output_tokens=self.llm_config.get("max_output_tokens"),
                    fallback_manager=self._fallback_manager,
                    get_model=None if model else self._current_sub_model,
                )

        async def _run_batch():
            tasks = [_throttled_call(p) for p in prompts]
            return await asyncio.gather(*tasks, return_exceptions=True)

        batch_start = time.time()
        try:
            future = asyncio.run_coroutine_threadsafe(_run_batch(), self._sub_loop)
            results = future.result()
            batch_elapsed = time.time() - batch_start
            per_call_time = batch_elapsed / max(len(results), 1)
            responses: List[str] = []
            for i, r in enumerate(results):
                if isinstance(r, Exception):
                    self._pending_sub_calls.append({
                        "model": sub_model, "prompt": prompts[i],
                        "prompt_length": len(prompts[i]),
                        "response": str(r), "response_length": 0,
                        "cost_usd": 0, "duration_s": round(per_call_time, 2),
                        "usage": None, "is_error": True,
                    })
                    responses.append(f"Error: LLM query failed - {r}")
                else:
                    response_text, result_info = r
                    self._sub_llm_calls += 1
                    cost = (result_info or {}).get("total_cost_usd") or 0
                    self._total_cost += cost
                    duration_ms = (result_info or {}).get("duration_ms")
                    self._pending_sub_calls.append({
                        "model": sub_model, "prompt": prompts[i],
                        "prompt_length": len(prompts[i]),
                        "response": response_text,
                        "response_length": len(response_text),
                        "cost_usd": cost,
                        "duration_s": round(duration_ms / 1000, 2) if duration_ms else round(per_call_time, 2),
                        "usage": (result_info or {}).get("usage"), "is_error": False,
                    })
                    responses.append(response_text)
            return responses
        except Exception as e:
            batch_elapsed = time.time() - batch_start
            per_call_time = batch_elapsed / max(len(prompts), 1)
            for i, p in enumerate(prompts):
                self._pending_sub_calls.append({
                    "model": sub_model, "prompt": p, "prompt_length": len(p),
                    "response": str(e), "response_length": 0,
                    "cost_usd": 0, "duration_s": round(per_call_time, 2),
                    "usage": None, "is_error": True,
                })
            return [f"Error: LLM query failed - {e}"] * len(prompts)

    def _final_var(self, variable_name: str) -> str:
        variable_name = variable_name.strip().strip('"').strip("'")
        if variable_name in self.locals:
            return str(self.locals[variable_name])
        available = [k for k in self.locals.keys() if not k.startswith("_")]
        if available:
            return (
                f"Error: Variable '{variable_name}' not found. "
                f"Available variables: {available}. "
                "You must create and assign a variable BEFORE calling FINAL_VAR on it."
            )
        return (
            f"Error: Variable '{variable_name}' not found. "
            "No variables have been created yet. "
            "You must create and assign a variable in a REPL block BEFORE calling FINAL_VAR on it."
        )

    def _show_vars(self) -> str:
        available = {
            k: type(v).__name__
            for k, v in self.locals.items()
            if not k.startswith("_")
        }
        if not available:
            return "No variables created yet. Use ```repl``` blocks to create variables."
        return f"Available variables: {available}"
