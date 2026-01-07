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
import time
from dataclasses import dataclass
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


@dataclass
class ClaudeResponse:
    """Response object mimicking LangChain's response structure."""
    content: str
    model: str
    usage: Optional[Dict[str, int]] = None

    def __str__(self) -> str:
        return self.content


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
        """Async query to Claude Agent SDK."""
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
