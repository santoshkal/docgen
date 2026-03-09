"""
Tests for the Adapter Registry
"""

import pytest

from adapter_registry import (
    _ADAPTER_REGISTRY,
    get_adapter,
    get_adapter_from_config,
    list_adapters,
    register_adapter,
)
from language_adapter import LanguageAdapter


@pytest.fixture(autouse=True)
def ensure_registry_populated():
    """
    Ensure adapters are registered before each test.

    We force-import the language packages so their register_adapter() calls
    run, even if the registry was cleared. Python module caching means
    `import` is a no-op on second call, so we explicitly re-register.
    """
    from languages.cobol.adapter import CobolAdapter
    from languages.dotnet.adapter import DotNetAdapter

    # Ensure both are registered
    _ADAPTER_REGISTRY['cobol'] = CobolAdapter
    _ADAPTER_REGISTRY['dotnet'] = DotNetAdapter
    yield


class TestRegistration:
    def test_register_and_get_cobol(self):
        adapter = get_adapter('cobol')
        assert adapter.language_id == 'cobol'
        assert adapter.display_name == 'COBOL'

    def test_register_and_get_dotnet(self):
        adapter = get_adapter('dotnet')
        assert adapter.language_id == 'dotnet'
        assert adapter.display_name == '.NET/C#'

    def test_get_unknown_adapter_raises(self):
        # Force discovery first
        get_adapter('cobol')
        with pytest.raises(ValueError, match="No adapter registered"):
            get_adapter('fortran')

    def test_register_non_adapter_raises(self):
        with pytest.raises(TypeError, match="LanguageAdapter subclass"):
            register_adapter('bad', str)


class TestAutoDiscovery:
    def test_both_adapters_auto_discover(self):
        adapters = list_adapters()
        assert 'cobol' in adapters
        assert 'dotnet' in adapters

    def test_cobol_display_name(self):
        adapters = list_adapters()
        assert adapters['cobol'] == 'COBOL'

    def test_dotnet_display_name(self):
        adapters = list_adapters()
        assert adapters['dotnet'] == '.NET/C#'


class TestConfigRouting:
    def test_default_is_cobol(self):
        adapter = get_adapter_from_config({})
        assert adapter.language_id == 'cobol'

    def test_explicit_cobol(self):
        config = {'source': {'language': 'cobol'}}
        adapter = get_adapter_from_config(config)
        assert adapter.language_id == 'cobol'

    def test_explicit_dotnet(self):
        config = {'source': {'language': 'dotnet'}}
        adapter = get_adapter_from_config(config)
        assert adapter.language_id == 'dotnet'

    def test_unknown_language_raises(self):
        # Force discovery first
        get_adapter('cobol')
        config = {'source': {'language': 'rust'}}
        with pytest.raises(ValueError, match="No adapter registered"):
            get_adapter_from_config(config)

    def test_missing_source_section_defaults_cobol(self):
        config = {'output': {'path': '/tmp'}}
        adapter = get_adapter_from_config(config)
        assert adapter.language_id == 'cobol'


class TestAdapterProperties:
    def test_cobol_adapter_has_required_properties(self):
        adapter = get_adapter('cobol')
        assert isinstance(adapter.file_extensions, list)
        assert len(adapter.file_extensions) > 0
        assert adapter.code_block_language == 'cobol'
        assert adapter.template_path is not None

    def test_dotnet_adapter_has_required_properties(self):
        adapter = get_adapter('dotnet')
        assert isinstance(adapter.file_extensions, list)
        assert '.cs' in adapter.file_extensions
        assert adapter.code_block_language == 'csharp'
        assert adapter.template_path is not None
