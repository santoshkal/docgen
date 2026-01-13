"""
Claude Agent SDK Client

A wrapper module that provides a LangChain-compatible interface for the Claude Agent SDK.
This allows easy migration from OpenAI/LangChain to Claude Agent SDK.

Usage:
    from claude_sdk_client import ClaudeSdkLLM

    llm = ClaudeSdkLLM(model="claude-sonnet-4-20250514")
    response = llm.invoke([
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello!"}
    ])
    print(response.content)
"""

import asyncio
import json
import subprocess
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# Claude Agent SDK imports
try:
    from claude_agent_sdk import (
        query,
        ClaudeAgentOptions,
        AssistantMessage,
        TextBlock,
        ToolUseBlock,
        ClaudeSDKError,
        CLINotFoundError,
        CLIConnectionError,
        ProcessError,
        CLIJSONDecodeError
    )
    CLAUDE_SDK_AVAILABLE = True
except ImportError:
    CLAUDE_SDK_AVAILABLE = False
    # Define placeholder types for when SDK is not available
    ClaudeAgentOptions = None  # type: ignore
    AssistantMessage = None  # type: ignore
    TextBlock = None  # type: ignore
    query = None  # type: ignore
    ClaudeSDKError = Exception  # type: ignore
    CLINotFoundError = Exception  # type: ignore
    CLIConnectionError = Exception  # type: ignore
    ProcessError = Exception  # type: ignore


# Threshold for switching to direct CLI call (bytes)
# Linux ARG_MAX is ~2MB but the SDK command includes other args
# 50KB is a safe threshold to avoid hitting limits
PROMPT_SIZE_THRESHOLD = 50 * 1024  # 50KB


@dataclass
class ClaudeResponse:
    """Response object mimicking LangChain's response structure."""
    content: str
    model: str
    usage: Optional[Dict[str, int]] = None

    def __str__(self) -> str:
        return self.content


def _find_claude_cli() -> str:
    """Find the Claude CLI binary path."""
    import shutil

    # Check for bundled CLI first (in SDK package)
    try:
        import claude_agent_sdk
        sdk_path = Path(claude_agent_sdk.__file__).parent
        bundled = sdk_path / "_bundled" / "claude"
        if bundled.exists():
            return str(bundled)
    except Exception:
        pass

    # Fall back to system-wide search
    if cli := shutil.which("claude"):
        return cli

    # Check common locations
    locations = [
        Path.home() / ".npm-global/bin/claude",
        Path("/usr/local/bin/claude"),
        Path.home() / ".local/bin/claude",
        Path.home() / "node_modules/.bin/claude",
    ]

    for path in locations:
        if path.exists():
            return str(path)

    raise FileNotFoundError("Claude CLI not found. Install with: npm install -g @anthropic-ai/claude-code")


def _call_claude_cli_direct(
    prompt: str,
    system_prompt: Optional[str] = None,
    model: Optional[str] = None
) -> str:
    """
    Call Claude CLI directly using a temp file for large prompts.

    This bypasses the SDK's command-line argument limitation by:
    1. Writing the prompt to a temp file
    2. Using shell to pipe the file content to claude CLI

    Args:
        prompt: The user prompt (can be very large)
        system_prompt: Optional system prompt
        model: Optional model name

    Returns:
        The response text from Claude
    """
    cli_path = _find_claude_cli()

    # Build command
    cmd = [cli_path, "--print"]

    if system_prompt:
        cmd.extend(["--system-prompt", system_prompt])

    if model:
        cmd.extend(["--model", model])

    # Disable tools for pure LLM calls
    cmd.extend(["--allowedTools", ""])

    # Write prompt to temp file and read via stdin
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
        f.write(prompt)
        temp_path = f.name

    try:
        # Use shell to pipe temp file to claude CLI
        # The prompt is passed via stdin, not command line
        with open(temp_path, 'r', encoding='utf-8') as prompt_file:
            result = subprocess.run(
                cmd,
                stdin=prompt_file,
                capture_output=True,
                text=True,
                timeout=600  # 10 minute timeout
            )

        if result.returncode != 0:
            # Capture both stderr and stdout for debugging
            error_msg = result.stderr.strip() if result.stderr else ""
            stdout_msg = result.stdout.strip() if result.stdout else ""

            # Check for specific API errors
            combined_output = f"{stdout_msg} {error_msg}".lower()

            # Detect context limit error
            if "prompt is too long" in combined_output or "context limit" in combined_output:
                # Calculate approximate token count
                prompt_tokens = len(prompt) // 4  # Rough estimate: 4 chars per token
                raise RuntimeError(
                    f"CONTEXT OVERFLOW: Prompt too large for Claude's context window.\n"
                    f"  Prompt size: {len(prompt):,} bytes (~{prompt_tokens:,} tokens)\n"
                    f"  Claude limit: ~200,000 tokens\n"
                    f"  Solution: Reduce prompt size by ~{max(0, prompt_tokens - 170000):,} tokens\n"
                    f"  Raw error: {stdout_msg[:200]}"
                )

            # Build detailed error message for other errors
            details = []
            if stdout_msg:
                details.append(f"stdout: {stdout_msg[:1000]}")
            if error_msg:
                details.append(f"stderr: {error_msg[:1000]}")
            if not details:
                details.append("No output captured")

            full_error = f"Claude CLI failed (exit {result.returncode}): {'; '.join(details)}"
            raise RuntimeError(full_error)

        return result.stdout.strip()

    finally:
        # Clean up temp file
        Path(temp_path).unlink(missing_ok=True)


class ClaudeSdkLLM:
    """
    Claude Agent SDK wrapper with LangChain-compatible interface.

    This class provides a synchronous `invoke()` method that works similarly
    to ChatOpenAI from langchain_openai.

    Args:
        model: Claude model to use (claude-opus-4-5, claude-sonnet-4-20250514, claude-haiku-4-5-20251001)
        system_prompt: Optional default system prompt
        max_retries: Number of retries on rate limit errors (default: 5)
        base_delay: Base delay for exponential backoff in seconds (default: 2)
        allowed_tools: List of tools to allow (default: None = no tools)
        cwd: Working directory for Claude (default: None)

    Example:
        llm = ClaudeSdkLLM(model="claude-sonnet-4-20250514")

        # Using message list (LangChain style)
        from langchain_core.messages import SystemMessage, HumanMessage
        response = llm.invoke([
            SystemMessage(content="You are a helpful assistant"),
            HumanMessage(content="Hello!")
        ])

        # Or using simple strings
        response = llm.invoke_simple(
            system_prompt="You are a helpful assistant",
            user_prompt="Hello!"
        )
    """

    # Model name mapping for convenience
    MODEL_ALIASES = {
        "claude-opus": "claude-opus-4-5",
        "claude-sonnet": "claude-sonnet-4-20250514",
        "claude-haiku": "claude-haiku-4-5-20251001",
        "opus": "claude-opus-4-5",
        "sonnet": "claude-sonnet-4-20250514",
        "haiku": "claude-haiku-4-5-20251001",
    }

    def __init__(
        self,
        model: str = "claude-sonnet-4-20250514",
        system_prompt: Optional[str] = None,
        max_retries: int = 5,
        base_delay: float = 2.0,
        allowed_tools: Optional[List[str]] = None,
        cwd: Optional[str] = None,
        temperature: Optional[float] = None,  # Accepted but ignored (for compatibility)
        api_key: Optional[str] = None,  # Accepted but ignored (uses Claude Code auth)
    ):
        if not CLAUDE_SDK_AVAILABLE:
            raise ImportError(
                "Claude Agent SDK not installed. Run: pip install claude-agent-sdk\n"
                "Also ensure Claude Code CLI is installed: npm install -g @anthropic-ai/claude-code"
            )

        # Resolve model aliases
        self.model = self.MODEL_ALIASES.get(model, model)
        self.default_system_prompt = system_prompt
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.allowed_tools = allowed_tools
        self.cwd = cwd

        # Log if temperature was passed (it's ignored)
        if temperature is not None:
            print(f"  Note: temperature={temperature} ignored (Claude SDK uses default)")

    def _build_options(self, system_prompt: Optional[str] = None) -> Any:
        """Build ClaudeAgentOptions from configuration."""
        opts = {}

        # Use provided system prompt or default
        if system_prompt:
            opts["system_prompt"] = system_prompt
        elif self.default_system_prompt:
            opts["system_prompt"] = self.default_system_prompt

        # Set model
        if self.model:
            opts["model"] = self.model

        # Set allowed tools (empty list = no tools)
        if self.allowed_tools is not None:
            opts["allowed_tools"] = self.allowed_tools
        else:
            # Default: no tools for pure LLM calls
            opts["allowed_tools"] = []

        # Set working directory
        if self.cwd:
            opts["cwd"] = self.cwd

        return ClaudeAgentOptions(**opts)

    async def _query_async(
        self,
        prompt: str,
        system_prompt: Optional[str] = None
    ) -> str:
        """
        Async query to Claude Agent SDK.

        Automatically uses direct CLI call for large prompts to avoid
        "Argument list too long" errors (Linux ARG_MAX limit).

        Args:
            prompt: The user prompt
            system_prompt: Optional system prompt

        Returns:
            The response text from Claude
        """
        # Determine if we need direct CLI call based on prompt size
        prompt_size = len(prompt.encode('utf-8'))
        use_direct_cli = prompt_size > PROMPT_SIZE_THRESHOLD

        if use_direct_cli:
            print(f"    → Using direct CLI call for large prompt ({prompt_size:,} bytes)")
            # Use direct CLI call with temp file (bypasses ARG_MAX)
            # Run in thread pool to not block async event loop
            loop = asyncio.get_event_loop()
            return await loop.run_in_executor(
                None,
                _call_claude_cli_direct,
                prompt,
                system_prompt,
                self.model
            )

        # For small prompts, use the SDK (simpler error handling)
        options = self._build_options(system_prompt)

        full_response = ""
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        full_response += block.text

        return full_response

    def _query_with_retry(
        self,
        prompt: str,
        system_prompt: Optional[str] = None
    ) -> str:
        """Query with exponential backoff retry on rate limit errors."""
        last_error = None

        for attempt in range(self.max_retries):
            try:
                return asyncio.run(self._query_async(prompt, system_prompt))

            except (CLIConnectionError, ProcessError) as e:
                error_str = str(e).lower()
                # Check for rate limit indicators
                if '429' in str(e) or 'rate' in error_str or 'too many' in error_str:
                    if attempt < self.max_retries - 1:
                        delay = self.base_delay * (2 ** attempt)
                        print(f"    ⚠ Rate limit hit, waiting {delay}s before retry ({attempt + 1}/{self.max_retries})...")
                        time.sleep(delay)
                        last_error = e
                    else:
                        print(f"    ✗ Rate limit exceeded after {self.max_retries} retries")
                        raise
                else:
                    raise

            except CLINotFoundError:
                raise ImportError(
                    "Claude Code CLI not found. Install with: npm install -g @anthropic-ai/claude-code"
                )

            except ClaudeSDKError as e:
                # For other SDK errors, raise immediately
                raise

        # Should not reach here, but just in case
        if last_error:
            raise last_error
        return ""

    def invoke(
        self,
        messages: List[Any],
        **kwargs
    ) -> ClaudeResponse:
        """
        Invoke Claude with a list of messages (LangChain-compatible interface).

        Args:
            messages: List of message objects with 'content' attribute and type
                     (SystemMessage, HumanMessage) or dicts with 'role' and 'content'

        Returns:
            ClaudeResponse with 'content' attribute
        """
        system_prompt = None
        user_prompts = []

        for msg in messages:
            # Handle LangChain message objects
            if hasattr(msg, 'content'):
                msg_type = type(msg).__name__
                content = msg.content

                if msg_type == 'SystemMessage' or getattr(msg, 'type', None) == 'system':
                    system_prompt = content
                elif msg_type == 'HumanMessage' or getattr(msg, 'type', None) == 'human':
                    user_prompts.append(content)
                elif msg_type == 'AIMessage' or getattr(msg, 'type', None) == 'ai':
                    # AI messages are typically previous responses, skip for now
                    pass
                else:
                    # Treat unknown as user message
                    user_prompts.append(content)

            # Handle dict-style messages
            elif isinstance(msg, dict):
                role = msg.get('role', 'user')
                content = msg.get('content', '')

                if role == 'system':
                    system_prompt = content
                elif role in ('user', 'human'):
                    user_prompts.append(content)

        # Combine user prompts
        combined_prompt = "\n\n".join(user_prompts)

        # Query Claude
        response_text = self._query_with_retry(combined_prompt, system_prompt)

        return ClaudeResponse(
            content=response_text,
            model=self.model
        )

    def invoke_simple(
        self,
        user_prompt: str,
        system_prompt: Optional[str] = None
    ) -> ClaudeResponse:
        """
        Simple invoke with just strings (no message objects needed).

        Args:
            user_prompt: The user's prompt/question
            system_prompt: Optional system prompt (uses default if not provided)

        Returns:
            ClaudeResponse with 'content' attribute
        """
        response_text = self._query_with_retry(user_prompt, system_prompt)

        return ClaudeResponse(
            content=response_text,
            model=self.model
        )


def create_claude_sdk_llm(
    model: str = "claude-sonnet-4-20250514",
    temperature: Optional[float] = None,
    api_key: Optional[str] = None,
    **kwargs
) -> ClaudeSdkLLM:
    """
    Factory function to create a ClaudeSdkLLM instance.

    This function signature matches the pattern used in cobol_doc_agent.py
    for creating LLM instances.

    Args:
        model: Claude model name or alias
        temperature: Ignored (for compatibility)
        api_key: Ignored (uses Claude Code auth)
        **kwargs: Additional arguments passed to ClaudeSdkLLM

    Returns:
        ClaudeSdkLLM instance
    """
    return ClaudeSdkLLM(
        model=model,
        temperature=temperature,
        api_key=api_key,
        **kwargs
    )


# Convenience check function
def check_claude_sdk_available() -> bool:
    """Check if Claude Agent SDK is available and CLI is installed."""
    if not CLAUDE_SDK_AVAILABLE:
        return False

    # Try a simple import test
    try:
        from claude_agent_sdk import query
        return True
    except Exception:
        return False
