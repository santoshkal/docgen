"""
Adapter Registry

Factory and registry for language adapters. Maps language IDs to adapter
classes and provides instantiation from config.

Usage:
    from adapter_registry import get_adapter, register_adapter

    # Get adapter for a language (auto-discovers built-in adapters)
    adapter = get_adapter('cobol')

    # Or from config dict
    adapter = get_adapter_from_config(config)
"""

from typing import Dict, Optional, Type

from language_adapter import LanguageAdapter


# Global registry mapping language_id -> adapter class
_ADAPTER_REGISTRY: Dict[str, Type[LanguageAdapter]] = {}


def register_adapter(language_id: str, adapter_class: Type[LanguageAdapter]) -> None:
    """
    Register a language adapter class.

    Args:
        language_id: Language identifier (e.g., 'cobol', 'dotnet')
        adapter_class: Concrete LanguageAdapter subclass

    Raises:
        TypeError: If adapter_class is not a LanguageAdapter subclass
    """
    if not (isinstance(adapter_class, type) and issubclass(adapter_class, LanguageAdapter)):
        raise TypeError(
            f"adapter_class must be a LanguageAdapter subclass, got {type(adapter_class)}"
        )
    _ADAPTER_REGISTRY[language_id] = adapter_class


def get_adapter(language_id: str = 'cobol') -> LanguageAdapter:
    """
    Get an adapter instance for the given language.

    Auto-discovers built-in adapters on first call if not yet registered.

    Args:
        language_id: Language identifier (default: 'cobol')

    Returns:
        Instantiated LanguageAdapter

    Raises:
        ValueError: If no adapter is registered for the language
    """
    # Auto-discover built-in adapters if registry is empty
    if not _ADAPTER_REGISTRY:
        _discover_builtin_adapters()

    adapter_class = _ADAPTER_REGISTRY.get(language_id)
    if adapter_class is None:
        available = ', '.join(sorted(_ADAPTER_REGISTRY.keys())) or '(none)'
        raise ValueError(
            f"No adapter registered for language '{language_id}'. "
            f"Available: {available}"
        )

    return adapter_class()


def get_adapter_from_config(config: Dict) -> LanguageAdapter:
    """
    Get an adapter instance from a configuration dictionary.

    Reads the language setting from config['source']['language'],
    defaulting to 'cobol' for backward compatibility.

    Args:
        config: Configuration dictionary (from config_loader)

    Returns:
        Instantiated LanguageAdapter
    """
    source_config = config.get('source', {})
    language_id = source_config.get('language', 'cobol')
    return get_adapter(language_id)


def list_adapters() -> Dict[str, str]:
    """
    List all registered adapters.

    Returns:
        Dictionary mapping language_id -> display_name
    """
    if not _ADAPTER_REGISTRY:
        _discover_builtin_adapters()

    result = {}
    for lang_id, adapter_class in sorted(_ADAPTER_REGISTRY.items()):
        # Instantiate briefly to get display name
        try:
            adapter = adapter_class()
            result[lang_id] = adapter.display_name
        except Exception:
            result[lang_id] = lang_id
    return result


def _discover_builtin_adapters() -> None:
    """
    Auto-discover and register built-in language adapters.

    Imports adapter modules from the languages/ package. Each module
    is expected to register itself via register_adapter() in its __init__.py.
    """
    # Import built-in language packages — each registers itself
    try:
        import languages.cobol  # noqa: F401
    except ImportError:
        pass

    try:
        import languages.dotnet  # noqa: F401
    except ImportError:
        pass
