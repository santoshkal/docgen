"""
COBOL Language Adapter Package

Registers the CobolAdapter with the adapter registry on import.
"""

from adapter_registry import register_adapter
from languages.cobol.adapter import CobolAdapter

register_adapter('cobol', CobolAdapter)
