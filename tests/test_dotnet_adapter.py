"""
Tests for the .NET/C# Language Adapter
"""

import os
import tempfile
from pathlib import Path

import pytest

from languages.dotnet.adapter import DotNetAdapter

SAMPLE_CS_SOURCE = """\
using System;
using System.Collections.Generic;
using System.Linq;
using Newtonsoft.Json;
using ng.iMES.Core;

namespace ng.iMES.Services
{
    /// <summary>
    /// Manages order processing workflow.
    /// </summary>
    public class OrderService : IOrderService
    {
        private readonly ILogger _logger;
        private readonly IOrderRepository _repository;

        public OrderService(ILogger logger, IOrderRepository repository)
        {
            _logger = logger;
            _repository = repository;
        }

        public string Name { get; set; }

        public async Task<Order> ProcessOrderAsync(int orderId)
        {
            try
            {
                var order = await _repository.GetByIdAsync(orderId);
                if (order == null)
                    throw new ArgumentException($"Order {orderId} not found");

                order.Status = OrderStatus.Processing;
                await _repository.UpdateAsync(order);

                _logger.LogInformation("Processed order {OrderId}", orderId);
                return order;
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Failed to process order {OrderId}", orderId);
                throw;
            }
        }

        public void HandleError(Exception ex)
        {
            _logger.LogError(ex, "Unhandled error in OrderService");
        }

        public static void Main(string[] args)
        {
            Console.WriteLine("Starting OrderService...");
        }
    }

    public enum OrderStatus
    {
        Pending,
        Processing,
        Completed,
        Failed
    }
}
"""


@pytest.fixture
def adapter():
    return DotNetAdapter()


@pytest.fixture
def sample_cs_file(tmp_path):
    """Create a temporary C# source file."""
    cs_file = tmp_path / "OrderService.cs"
    cs_file.write_text(SAMPLE_CS_SOURCE)
    return cs_file


@pytest.fixture
def sample_workspace(tmp_path):
    """Create a temporary workspace with several C# files."""
    # Regular source files
    (tmp_path / "OrderService.cs").write_text("public class OrderService {}")
    (tmp_path / "CustomerService.cs").write_text("public class CustomerService {}")

    # Subdirectory with more files
    subdir = tmp_path / "Models"
    subdir.mkdir()
    (subdir / "Order.cs").write_text("public class Order {}")
    (subdir / "Customer.cs").write_text("public class Customer {}")

    # Generated files that should be excluded
    (tmp_path / "AssemblyInfo.cs").write_text("[assembly: AssemblyTitle]")
    (tmp_path / "Form1.Designer.cs").write_text("// auto-generated")
    (tmp_path / "Resource.g.cs").write_text("// auto-generated")

    return tmp_path


# =============================================================================
# Identity & Config
# =============================================================================

class TestIdentity:
    def test_language_id(self, adapter):
        assert adapter.language_id == 'dotnet'

    def test_display_name(self, adapter):
        assert adapter.display_name == '.NET/C#'

    def test_file_extensions(self, adapter):
        assert adapter.file_extensions == ['.cs']

    def test_code_block_language(self, adapter):
        assert adapter.code_block_language == 'csharp'

    def test_template_path_exists(self, adapter):
        assert adapter.template_path.name == 'template.yaml'
        assert adapter.template_path.exists()


# =============================================================================
# File Discovery
# =============================================================================

class TestFileDiscovery:
    def test_discover_files_basic(self, adapter, sample_workspace):
        files = adapter.discover_source_files(str(sample_workspace))
        names = [f.name for f in files]

        # Should find regular .cs files (including subdirectory)
        assert 'OrderService.cs' in names
        assert 'CustomerService.cs' in names
        assert 'Order.cs' in names
        assert 'Customer.cs' in names

        # Should exclude auto-generated files
        assert 'AssemblyInfo.cs' not in names
        assert 'Form1.Designer.cs' not in names
        assert 'Resource.g.cs' not in names

    def test_discover_files_with_include_filter(self, adapter, sample_workspace):
        files = adapter.discover_source_files(
            str(sample_workspace),
            filter_config={'include_files': ['Order*.cs']}
        )
        names = [f.name for f in files]
        assert 'OrderService.cs' in names
        assert 'Order.cs' in names
        assert 'CustomerService.cs' not in names

    def test_discover_files_with_exclude_filter(self, adapter, sample_workspace):
        files = adapter.discover_source_files(
            str(sample_workspace),
            filter_config={'exclude_files': ['*Service.cs']}
        )
        names = [f.name for f in files]
        assert 'OrderService.cs' not in names
        assert 'CustomerService.cs' not in names
        assert 'Order.cs' in names
        assert 'Customer.cs' in names

    def test_discover_empty_dir(self, adapter, tmp_path):
        files = adapter.discover_source_files(str(tmp_path))
        assert files == []

    def test_discover_nonexistent_dir(self, adapter):
        files = adapter.discover_source_files('/nonexistent/path')
        assert files == []

    def test_get_program_name(self, adapter):
        assert adapter.get_program_name('/some/path/OrderService.cs') == 'OrderService'
        assert adapter.get_program_name('MyClass.cs') == 'MyClass'


# =============================================================================
# Structural Boundaries
# =============================================================================

class TestStructuralBoundaries:
    def test_regex_fallback_finds_boundaries(self, adapter):
        lines = SAMPLE_CS_SOURCE.splitlines(keepends=True)
        boundaries = adapter.find_structural_boundaries(lines)

        # Should find namespace, class, methods
        kinds = [b.kind for b in boundaries]
        assert 'namespace' in kinds
        assert 'class' in kinds
        assert 'method' in kinds

    def test_ctags_metadata_boundaries(self, adapter):
        lines = SAMPLE_CS_SOURCE.splitlines(keepends=True)
        metadata = {
            'symbols': [
                {'name': 'ng.iMES.Services', 'kind': 'namespace', 'line': 7},
                {'name': 'OrderService', 'kind': 'class', 'line': 13},
                {'name': 'ProcessOrderAsync', 'kind': 'method', 'line': 26},
                {'name': 'HandleError', 'kind': 'method', 'line': 48},
                {'name': 'Main', 'kind': 'method', 'line': 53},
            ]
        }
        boundaries = adapter.find_structural_boundaries(lines, metadata)

        names = [b.name for b in boundaries]
        assert 'ng.iMES.Services' in names
        assert 'OrderService' in names
        assert 'ProcessOrderAsync' in names
        assert 'HandleError' in names
        assert 'Main' in names


# =============================================================================
# Chunking
# =============================================================================

class TestChunking:
    def test_chunk_source_file(self, adapter, sample_cs_file):
        chunks, verification = adapter.chunk_source_file(str(sample_cs_file))

        assert verification.valid
        assert verification.total_lines > 0
        assert verification.chunks >= 1
        assert len(chunks) >= 1

        # All lines should be covered
        total_chunk_lines = sum(c.line_count for c in chunks)
        assert total_chunk_lines == verification.total_lines

    def test_chunk_nonexistent_file(self, adapter):
        chunks, verification = adapter.chunk_source_file('/nonexistent.cs')
        assert not verification.valid
        assert 'not found' in verification.error.lower()

    def test_format_chunk_for_llm(self, adapter):
        from language_adapter import SourceChunk
        chunk = SourceChunk(
            chunk_number=1,
            start_line=1,
            end_line=10,
            line_count=10,
            content="public class Foo { }",
            estimated_tokens=5,
        )
        formatted = adapter.format_chunk_for_llm(chunk, 3, "Foo.cs")
        assert "Chunk 1/3" in formatted
        assert "Foo.cs" in formatted
        assert "```csharp" in formatted
        assert "public class Foo" in formatted


# =============================================================================
# Source Extraction
# =============================================================================

class TestSourceExtraction:
    def test_compress_source(self, adapter):
        source = """
// This is a comment
using System;

/* Block
   comment */

public class Foo
{
    // Another comment
    public void Bar() { }
}
"""
        compressed = adapter.compress_source(source)
        assert '// This is a comment' not in compressed
        assert '/* Block' not in compressed
        assert 'public class Foo' in compressed
        assert 'public void Bar()' in compressed

    def test_extract_structural_scope(self, adapter, sample_cs_file):
        result = adapter.extract_structural_scope(str(sample_cs_file), 'namespace')
        assert result is not None
        assert 'namespace' in result
        assert 'OrderService' in result

    def test_section_source_requirements(self, adapter):
        reqs = adapter.get_section_source_requirements()
        assert 'detailed-code-explanation' in reqs
        assert reqs['detailed-code-explanation'].extract_source is True


# =============================================================================
# Using Directive Parsing
# =============================================================================

class TestDependencyParsing:
    def test_parse_using_directives(self, adapter, sample_cs_file):
        refs = adapter.parse_dependency_references(str(sample_cs_file))
        names = [r.name for r in refs]

        assert 'System' in names
        assert 'System.Collections.Generic' in names
        assert 'System.Linq' in names
        assert 'Newtonsoft.Json' in names
        assert 'ng.iMES.Core' in names

        # All should be 'using' type
        for ref in refs:
            assert ref.reference_type == 'using'

    def test_parse_external_calls(self, adapter, sample_cs_file):
        calls = adapter.parse_external_calls(str(sample_cs_file))
        targets = [c.target for c in calls]

        # Should detect instantiations and static calls
        assert any('Console' in t for t in targets)
        assert all(c.caller == 'OrderService' for c in calls)


# =============================================================================
# Metadata
# =============================================================================

class TestMetadata:
    def test_metadata_file_patterns(self, adapter):
        patterns = adapter.get_metadata_file_patterns('OrderService')

        assert 'structural_outline' in patterns
        assert 'symbol_table' in patterns
        assert 'syntax_tree' in patterns

        # Should include program name in patterns
        assert any('OrderService' in p for p in patterns['structural_outline'])

    def test_normalize_metadata(self, adapter):
        raw = {
            'structural_outline': {'symbols': []},
            'symbol_table': {'data': 'test'},
            'syntax_tree': {'ast': {'type': 'program'}},
        }
        normalized = adapter.normalize_metadata(raw)

        assert normalized.structural_outline == {'symbols': []}
        assert normalized.symbol_table == {'data': 'test'}
        assert normalized.syntax_tree == {'ast': {'type': 'program'}}
        assert normalized.control_flow_graph == {}


# =============================================================================
# Mandatory Elements
# =============================================================================

class TestMandatoryElements:
    def test_entry_point_patterns(self, adapter):
        patterns = adapter.get_entry_point_patterns()
        assert 'Main' in patterns
        assert 'Startup' in patterns

    def test_error_handler_patterns(self, adapter):
        patterns = adapter.get_error_handler_patterns()
        assert 'Catch' in patterns
        assert 'HandleError' in patterns

    def test_identify_mandatory_elements(self, adapter):
        metadata = {
            'structural_outline': {
                'symbols': [
                    {'name': 'Main', 'kind': 'method', 'line': 10},
                    {'name': 'ProcessOrder', 'kind': 'method', 'line': 20},
                    {'name': 'HandleError', 'kind': 'method', 'line': 30},
                ]
            }
        }
        elements = adapter.identify_mandatory_elements(metadata)

        entry_names = [e.name for e in elements['entry_points']]
        error_names = [e.name for e in elements['error_handlers']]

        assert 'Main' in entry_names
        assert 'HandleError' in error_names


# =============================================================================
# Program Map
# =============================================================================

class TestProgramMap:
    def test_generate_program_map_with_metadata(self, adapter):
        metadata = {
            'structural_outline': {
                'symbols': [
                    {'name': 'ng.iMES.Services', 'kind': 'namespace', 'line': 7},
                    {'name': 'OrderService', 'kind': 'class', 'line': 13},
                    {'name': 'ProcessOrderAsync', 'kind': 'method', 'line': 26},
                    {'name': 'HandleError', 'kind': 'method', 'line': 48},
                    {'name': 'Name', 'kind': 'property', 'line': 24},
                ]
            }
        }
        program_map = adapter.generate_program_map('OrderService', metadata)

        assert 'OrderService' in program_map
        assert 'Namespaces' in program_map
        assert 'Types' in program_map
        assert 'Methods' in program_map
        assert 'Properties' in program_map

    def test_generate_program_map_no_metadata(self, adapter):
        program_map = adapter.generate_program_map('Empty', {})
        assert 'No structural metadata available' in program_map

    def test_language_context(self, adapter):
        context = adapter.get_language_context_for_prompt()
        assert 'C#' in context
        assert 'namespace' in context
        assert 'async/await' in context
