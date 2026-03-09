"""
.NET/C# Language Adapter Package

Registers the DotNetAdapter with the adapter registry on import.
"""

from adapter_registry import register_adapter
from languages.dotnet.adapter import DotNetAdapter

register_adapter('dotnet', DotNetAdapter)
