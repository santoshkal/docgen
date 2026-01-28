"""
LLM Fallback Manager

Provides fallback support for LLM calls:
- Tracks fallback state across session
- Provides phase-specific configurations
- Wraps LLM invocations with automatic fallback on error

Usage:
    from llm_fallback import LLMFallbackManager, invoke_llm_with_fallback

    # Initialize with config that may have 'fallback' block
    fallback_manager = LLMFallbackManager(llm_config)

    # Use wrapper for all LLM calls
    response = invoke_llm_with_fallback(
        llm_config=llm_config,
        messages=messages,
        fallback_manager=fallback_manager,
        phase=1
    )
"""

from typing import Any, Dict, List, Optional
import time


class LLMFallbackManager:
    """
    Manages LLM fallback state across a documentation generation session.

    Behavior:
    - If no 'fallback' block in config: has_fallback() returns False
    - On ANY error during LLM call: triggers fallback for ALL remaining calls
    - Provides phase-specific config (phase1 vs phase2 can have different models/betas)
    """

    def __init__(self, llm_config: Dict[str, Any]):
        """
        Initialize fallback manager.

        Args:
            llm_config: Full LLM configuration dict, may contain 'fallback' block
        """
        self.primary_config = {
            'provider': llm_config.get('provider', 'openai'),
            'model': llm_config.get('model', 'gpt-4o'),
            'temperature': llm_config.get('temperature', 0.1),
            'api_key': llm_config.get('api_key'),
            'betas': llm_config.get('betas'),
        }

        self.fallback_config = llm_config.get('fallback')
        self._fallback_active = False
        self._fallback_trigger_error: Optional[Exception] = None
        self._fallback_triggered_at: Optional[str] = None

    def has_fallback(self) -> bool:
        """
        Check if fallback is configured.

        Returns:
            True if 'fallback' block exists in config
        """
        return self.fallback_config is not None

    def is_fallback_active(self) -> bool:
        """
        Check if fallback is currently active.

        Returns:
            True if fallback has been triggered
        """
        return self._fallback_active

    def trigger_fallback(self, error: Exception) -> None:
        """
        Trigger fallback mode due to an error.

        Once triggered, ALL subsequent calls use fallback config.

        Args:
            error: The exception that caused the fallback
        """
        if not self.has_fallback():
            return

        if not self._fallback_active:
            self._fallback_active = True
            self._fallback_trigger_error = error
            self._fallback_triggered_at = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"  ⚠ FALLBACK TRIGGERED: {type(error).__name__}: {str(error)[:100]}")
            print(f"    All remaining LLM calls will use fallback provider")

    def get_llm_config(self, phase: int = 1) -> Dict[str, Any]:
        """
        Get effective LLM config for current state and phase.

        Args:
            phase: Phase number (1 or 2) for phase-specific fallback config

        Returns:
            LLM config dict ready for create_llm()
        """
        if not self._fallback_active or not self.fallback_config:
            return self.primary_config.copy()

        # Build fallback config
        fb = self.fallback_config
        phase_key = f'phase{phase}'

        # Get base fallback settings
        config = {
            'provider': fb.get('provider', self.primary_config['provider']),
            'temperature': fb.get('temperature', self.primary_config.get('temperature', 0.1)),
            'api_key': fb.get('api_key', self.primary_config.get('api_key')),
        }

        # Get phase-specific settings
        if phase_key in fb:
            phase_config = fb[phase_key]
            config['model'] = phase_config.get('model', fb.get('model', 'sonnet'))
            config['betas'] = phase_config.get('betas', fb.get('betas'))
        else:
            # Use top-level fallback model/betas
            config['model'] = fb.get('model', 'sonnet')
            config['betas'] = fb.get('betas')

        return config

    def get_status(self) -> Dict[str, Any]:
        """
        Get current fallback status for logging.

        Returns:
            Dict with status information
        """
        return {
            'has_fallback': self.has_fallback(),
            'fallback_active': self._fallback_active,
            'trigger_error': str(self._fallback_trigger_error) if self._fallback_trigger_error else None,
            'triggered_at': self._fallback_triggered_at,
            'primary_provider': self.primary_config.get('provider'),
            'primary_model': self.primary_config.get('model'),
            'fallback_provider': self.fallback_config.get('provider') if self.fallback_config else None,
        }


def invoke_llm_with_fallback(
    llm_config: Dict[str, Any],
    messages: List[Any],
    fallback_manager: Optional[LLMFallbackManager] = None,
    phase: int = 1,
    max_retries: int = 3,
    base_delay: float = 2.0
) -> Any:
    """
    Invoke LLM with automatic fallback support.

    Behavior:
    1. Get effective config from fallback_manager (respects fallback state)
    2. Create LLM via create_llm()
    3. Try llm.invoke(messages) with retry on rate limits
    4. On error: trigger fallback (if available), retry with fallback LLM
    5. If no fallback or already in fallback: re-raise error

    Args:
        llm_config: Original LLM configuration
        messages: List of messages to send to LLM
        fallback_manager: Optional fallback manager instance
        phase: Phase number (1 or 2) for phase-specific fallback
        max_retries: Maximum retries for rate limit errors
        base_delay: Base delay for exponential backoff

    Returns:
        LLM response object

    Raises:
        Exception: If LLM call fails and no fallback available
    """
    # Import here to avoid circular imports
    from cobol_doc_agent import create_llm

    # Get effective config
    if fallback_manager:
        effective_config = fallback_manager.get_llm_config(phase)
    else:
        effective_config = llm_config

    # Track if we're using fallback for this specific call
    using_fallback = fallback_manager and fallback_manager.is_fallback_active()

    # Create LLM
    llm = create_llm(effective_config)

    # Attempt with retry
    last_error = None
    for attempt in range(max_retries):
        try:
            response = llm.invoke(messages)
            return response

        except Exception as e:
            error_str = str(e).lower()
            last_error = e

            # Check for rate limit (retry with backoff)
            if '429' in str(e) or 'rate' in error_str or 'too many' in error_str:
                if attempt < max_retries - 1:
                    delay = base_delay * (2 ** attempt)
                    print(f"    ⚠ Rate limit hit, waiting {delay}s before retry ({attempt + 1}/{max_retries})...")
                    time.sleep(delay)
                    continue
                else:
                    print(f"    ✗ Rate limit exceeded after {max_retries} retries")

            # Not a rate limit error, or retries exhausted
            # Try fallback if available and not already using it
            if fallback_manager and fallback_manager.has_fallback() and not using_fallback:
                fallback_manager.trigger_fallback(e)

                # Retry with fallback config
                fallback_config = fallback_manager.get_llm_config(phase)
                fallback_llm = create_llm(fallback_config)
                fallback_model = fallback_config.get('model', 'unknown')

                print(f"    → Retrying with fallback LLM: {fallback_model}")

                try:
                    response = fallback_llm.invoke(messages)
                    return response
                except Exception as fallback_error:
                    # Fallback also failed
                    print(f"    ✗ Fallback LLM also failed: {type(fallback_error).__name__}")
                    raise fallback_error

            # No fallback available or already in fallback mode
            raise e

    # Should not reach here, but just in case
    if last_error:
        raise last_error
    raise RuntimeError("LLM invocation failed with no error captured")


def create_fallback_manager_if_configured(llm_config: Dict[str, Any]) -> Optional[LLMFallbackManager]:
    """
    Create a fallback manager only if fallback is configured.

    Convenience function for optional fallback support.

    Args:
        llm_config: LLM configuration that may contain 'fallback' block

    Returns:
        LLMFallbackManager if fallback configured, None otherwise
    """
    manager = LLMFallbackManager(llm_config)
    if manager.has_fallback():
        return manager
    return None
