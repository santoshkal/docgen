"""
Unified Tokenizer Module

Single source of truth for token estimation and model limits.
Supports both OpenAI and Claude models with accurate token counting.
"""

from typing import Any, Dict, List, Optional

# Check if tiktoken is available for accurate token counting (OpenAI)
try:
    import tiktoken as _tiktoken_check  # noqa: F401
    TIKTOKEN_AVAILABLE = True
    del _tiktoken_check
except ImportError:
    TIKTOKEN_AVAILABLE = False


# ============================================================================
# MODEL TOKEN LIMITS
# ============================================================================
# Max INPUT tokens for each model (leaving room for output)
MODEL_TOKEN_LIMITS: Dict[str, int] = {
    # OpenAI models
    "gpt-4.1": 900000,        # 1M context → 900K input max
    "gpt-4o": 100000,         # 128K context → 100K input max
    "gpt-4-turbo": 100000,    # 128K context → 100K input max
    "gpt-4": 6000,            # 8K context → 6K input max
    "gpt-3.5-turbo": 14000,   # 16K context → 14K input max

    # Claude models (standard context — 200K)
    "claude-opus-4-6": 180000,           # 200K context → 180K input max
    "claude-opus-4-5": 180000,           # 200K context → 180K input max
    "claude-sonnet-4-6": 180000,         # 200K context → 180K input max
    "claude-sonnet-4-20250514": 180000,  # 200K context → 180K input max
    "claude-haiku-4-5-20251001": 180000, # 200K context → 180K input max
    "sonnet": 180000,                    # Alias
    "opus": 180000,                      # Alias
    "haiku": 180000,                     # Alias
    "sonnet[1]": 180000,                 # Special alias for Claude Code
}

# Claude models with 1M context beta
CLAUDE_1M_BETA_LIMIT = 900000  # 1M context → 900K input max
CLAUDE_1M_BETA_FLAG = "context-1m-2025-08-07"


def detect_provider_from_model(model: str) -> str:
    """
    Detect the LLM provider from model name.

    Args:
        model: Model name (e.g., 'gpt-4o', 'sonnet', 'claude-sonnet-4-20250514')

    Returns:
        Provider name: 'openai', 'anthropic', or 'unknown'
    """
    model_lower = model.lower()

    # OpenAI models
    if model_lower.startswith('gpt-'):
        return 'openai'

    # Claude models (various naming conventions)
    if any(name in model_lower for name in ['claude', 'sonnet', 'opus', 'haiku']):
        return 'anthropic'

    return 'unknown'


def get_token_limit(model: str, betas: Optional[List[str]] = None) -> int:
    """
    Get max input tokens for a model.

    Handles special cases:
    - Claude with 1M beta: returns 900K
    - Unknown models: returns conservative 100K default

    Args:
        model: Model name
        betas: Optional list of beta features (e.g., ['context-1m-2025-08-07'])

    Returns:
        Maximum input token count
    """
    # Check for Claude 1M beta
    if betas and CLAUDE_1M_BETA_FLAG in betas:
        provider = detect_provider_from_model(model)
        if provider == 'anthropic':
            return CLAUDE_1M_BETA_LIMIT

    # Look up model in limits
    if model in MODEL_TOKEN_LIMITS:
        return MODEL_TOKEN_LIMITS[model]

    # Try lowercase match
    model_lower = model.lower()
    for key, limit in MODEL_TOKEN_LIMITS.items():
        if key.lower() == model_lower:
            return limit

    # Default for unknown models
    return 100000


def estimate_tokens(text: str, model: str = "gpt-4") -> int:
    """
    Estimate token count for text using provider-aware tokenization.

    - OpenAI models: Uses tiktoken with model-specific encoding
    - Claude/unknown models: Uses tiktoken cl100k_base for accurate BPE counting
    - Falls back to len(text)//4 estimation if tiktoken unavailable

    Args:
        text: Text to count tokens for
        model: Model name for tokenization

    Returns:
        Estimated token count
    """
    if not text:
        return 0

    provider = detect_provider_from_model(model)

    # For OpenAI models, use tiktoken if available
    if provider == 'openai' and TIKTOKEN_AVAILABLE:
        try:
            import tiktoken as tk
            encoder = tk.encoding_for_model(model)
            return len(encoder.encode(text))
        except Exception:
            # Fallback to estimation if tiktoken fails
            pass

    # For Claude or unknown: use tiktoken cl100k_base for accurate BPE tokenization
    if TIKTOKEN_AVAILABLE:
        try:
            import tiktoken as tk
            encoder = tk.get_encoding("cl100k_base")
            return len(encoder.encode(text))
        except Exception:
            pass

    # Last-resort fallback if tiktoken unavailable
    return len(text) // 4


def estimate_tokens_for_messages(
    messages: List[Any],
    model: str = "gpt-4"
) -> int:
    """
    Estimate total token count for a list of messages.

    Args:
        messages: List of message objects (LangChain or dict format)
        model: Model name for tokenization

    Returns:
        Estimated total token count
    """
    total = 0

    for msg in messages:
        # Handle LangChain message objects
        if hasattr(msg, 'content'):
            content = msg.content
        # Handle dict-style messages
        elif isinstance(msg, dict):
            content = msg.get('content', '')
        else:
            content = str(msg)

        total += estimate_tokens(content, model)

    return total


def get_model_info(model: str, betas: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Get comprehensive information about a model.

    Args:
        model: Model name
        betas: Optional list of beta features

    Returns:
        Dict with model info:
        - provider: 'openai' or 'anthropic'
        - max_input_tokens: Maximum input token limit
        - has_1m_beta: Whether 1M beta is enabled
        - tiktoken_available: Whether accurate counting is available
    """
    provider = detect_provider_from_model(model)
    max_tokens = get_token_limit(model, betas)
    has_1m = betas and CLAUDE_1M_BETA_FLAG in betas and provider == 'anthropic'

    return {
        'provider': provider,
        'max_input_tokens': max_tokens,
        'has_1m_beta': has_1m,
        'tiktoken_available': TIKTOKEN_AVAILABLE
    }
