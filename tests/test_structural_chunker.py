"""
Tests for structural_chunker.py — tree-sitter query_code based semantic chunking.
"""

import pytest
from structural_chunker import (
    Declaration,
    Container,
    DeclarationMap,
    build_declaration_map,
    build_declaration_map_from_graph,
    chunk_at_declaration_boundaries,
    get_structural_context,
    update_seen_members,
)


# =============================================================================
# Test Data Helpers
# =============================================================================

def _make_query_results(matches):
    """Build a mock query_code response."""
    return {
        "success": True,
        "language": "c_sharp",
        "match_count": len(matches),
        "matches": matches,
    }


def _match(capture, node_type, text, start_row, end_row, start_byte=0, end_byte=0, start_col=0, end_col=0):
    """Build a single match entry."""
    return {
        "capture": capture,
        "type": node_type,
        "text": text,
        "start_point": {"row": start_row, "column": start_col},
        "end_point": {"row": end_row, "column": end_col},
        "start_byte": start_byte,
        "end_byte": end_byte,
    }


# =============================================================================
# Tests: build_declaration_map
# =============================================================================

class TestBuildDeclarationMap:

    def test_empty_results(self):
        result = build_declaration_map({"success": True, "matches": []})
        assert result is None

    def test_failed_results(self):
        result = build_declaration_map({"success": False, "matches": []})
        assert result is None

    def test_none_input(self):
        result = build_declaration_map(None)
        assert result is None

    def test_single_class_with_methods(self):
        matches = [
            # class Foo (lines 10-50, bytes 100-500)
            _match("container.def", "class_declaration", "public class Foo { ... }", 9, 49, 100, 500),
            _match("container.name", "identifier", "Foo", 9, 9, 115, 118),
            # method Bar (lines 15-25, bytes 200-350)
            _match("member.def", "method_declaration", "public void Bar() { ... }", 14, 24, 200, 350),
            _match("member.name", "identifier", "Bar", 14, 14, 220, 223),
            # method Baz (lines 30-45, bytes 360-480)
            _match("member.def", "method_declaration", "public int Baz() { ... }", 29, 44, 360, 480),
            _match("member.name", "identifier", "Baz", 29, 29, 375, 378),
        ]
        result = build_declaration_map(_make_query_results(matches))

        assert result is not None
        assert len(result.containers) == 1
        assert result.containers[0].name == "Foo"
        assert result.containers[0].start_line == 10  # 0-indexed row 9 → 1-indexed 10
        assert result.containers[0].end_line == 50
        assert len(result.containers[0].members) == 2
        assert result.containers[0].members[0].name == "Bar"
        assert result.containers[0].members[1].name == "Baz"
        assert len(result.standalone) == 0

    def test_nested_classes(self):
        """Inner class should be a member of the outer class."""
        matches = [
            # outer class (lines 1-100)
            _match("container.def", "class_declaration", "class Outer { ... }", 0, 99, 0, 1000),
            _match("container.name", "identifier", "Outer", 0, 0, 6, 11),
            # inner class (lines 30-60) — also a container
            _match("container.def", "class_declaration", "class Inner { ... }", 29, 59, 300, 600),
            _match("container.name", "identifier", "Inner", 29, 29, 306, 311),
            # method in inner class (lines 35-50)
            _match("member.def", "method_declaration", "void Foo() {}", 34, 49, 350, 500),
            _match("member.name", "identifier", "Foo", 34, 34, 355, 358),
        ]
        result = build_declaration_map(_make_query_results(matches))

        assert len(result.containers) == 2
        # Inner class members assigned to Inner (smallest containing container)
        inner = [c for c in result.containers if c.name == "Inner"][0]
        assert len(inner.members) == 1
        assert inner.members[0].name == "Foo"

    def test_standalone_members(self):
        """Members outside any container go to standalone list."""
        matches = [
            _match("member.def", "method_declaration", "void TopLevel() {}", 0, 10, 0, 100),
            _match("member.name", "identifier", "TopLevel", 0, 0, 5, 13),
        ]
        result = build_declaration_map(_make_query_results(matches))

        assert len(result.containers) == 0
        assert len(result.standalone) == 1
        assert result.standalone[0].name == "TopLevel"

    def test_field_without_name_capture(self):
        """field_declaration may lack a .name capture — fallback to text."""
        matches = [
            _match("container.def", "class_declaration", "class Foo { ... }", 0, 50, 0, 500),
            _match("container.name", "identifier", "Foo", 0, 0, 6, 9),
            _match("member.def", "field_declaration", "private int _count;", 10, 10, 100, 120),
        ]
        result = build_declaration_map(_make_query_results(matches))

        assert len(result.containers[0].members) == 1
        member = result.containers[0].members[0]
        assert "private int _count" in member.name


# =============================================================================
# Tests: chunk_at_declaration_boundaries
# =============================================================================

class TestChunkAtDeclarationBoundaries:

    def _make_lines(self, n):
        """Create n lines of fake source code."""
        return [f"line {i+1}\n" for i in range(n)]

    def _make_decl_map(self, containers, standalone=None):
        return DeclarationMap(containers=containers, standalone=standalone or [])

    def test_small_file_single_chunk(self):
        """File smaller than max_tokens should produce one chunk."""
        lines = self._make_lines(10)
        decl_map = self._make_decl_map([
            Container(name="Foo", kind="class_declaration", start_line=1, end_line=10,
                      members=[Declaration(name="Bar", kind="method", start_line=3, end_line=8)])
        ])
        chunks, verif = chunk_at_declaration_boundaries(lines, decl_map, max_tokens_per_chunk=100000)

        assert verif.valid
        assert len(chunks) == 1
        assert chunks[0].start_line == 1
        assert chunks[0].end_line == 10

    def test_full_coverage(self):
        """All lines must be covered, no gaps."""
        lines = self._make_lines(100)
        decl_map = self._make_decl_map([
            Container(name="A", kind="class", start_line=1, end_line=100,
                      members=[
                          Declaration(name="m1", kind="method", start_line=10, end_line=30),
                          Declaration(name="m2", kind="method", start_line=31, end_line=60),
                          Declaration(name="m3", kind="method", start_line=61, end_line=90),
                      ])
        ])
        # Force small chunks
        chunks, verif = chunk_at_declaration_boundaries(lines, decl_map, max_tokens_per_chunk=200)

        assert verif.valid
        total_lines = sum(c.line_count for c in chunks)
        assert total_lines == 100

    def test_empty_file(self):
        chunks, verif = chunk_at_declaration_boundaries([], DeclarationMap([], []))
        assert verif.valid
        assert len(chunks) == 0


# =============================================================================
# Tests: get_structural_context
# =============================================================================

class TestGetStructuralContext:

    def _make_containers(self):
        return [
            Container(
                name="SmallClass", kind="class_declaration",
                start_line=1, end_line=50,
                members=[
                    Declaration(name="m1", kind="method", start_line=5, end_line=20),
                    Declaration(name="m2", kind="method", start_line=25, end_line=45),
                ]
            ),
            Container(
                name="BigClass", kind="class_declaration",
                start_line=60, end_line=500,
                members=[
                    Declaration(name="a", kind="method", start_line=70, end_line=150),
                    Declaration(name="b", kind="method", start_line=160, end_line=300),
                    Declaration(name="c", kind="method", start_line=310, end_line=490),
                ]
            ),
        ]

    def test_complete_class(self):
        containers = self._make_containers()
        decl_map = DeclarationMap(containers=containers, standalone=[])

        ctx = get_structural_context(1, 55, decl_map, {})
        assert len(ctx) == 1
        assert "**Complete**" in ctx[0]
        assert "SmallClass" in ctx[0]
        assert "2 of 2 members" in ctx[0]

    def test_starts_class(self):
        containers = self._make_containers()
        decl_map = DeclarationMap(containers=containers, standalone=[])

        ctx = get_structural_context(55, 200, decl_map, {})
        assert any("**Starts**" in c for c in ctx)
        assert any("BigClass" in c for c in ctx)

    def test_continues_class(self):
        containers = self._make_containers()
        decl_map = DeclarationMap(containers=containers, standalone=[])

        ctx = get_structural_context(200, 350, decl_map, {})
        assert any("**Continues**" in c for c in ctx)

    def test_ends_class(self):
        containers = self._make_containers()
        decl_map = DeclarationMap(containers=containers, standalone=[])

        ctx = get_structural_context(400, 510, decl_map, {})
        assert any("**Ends**" in c for c in ctx)

    def test_no_overlap(self):
        containers = self._make_containers()
        decl_map = DeclarationMap(containers=containers, standalone=[])

        ctx = get_structural_context(51, 59, decl_map, {})
        assert len(ctx) == 0  # Between the two classes

    def test_previously_documented(self):
        containers = self._make_containers()
        decl_map = DeclarationMap(containers=containers, standalone=[])
        seen = {"BigClass": ["a"]}

        ctx = get_structural_context(200, 350, decl_map, seen)
        assert any("Previously documented: 1 members" in c for c in ctx)


# =============================================================================
# Tests: update_seen_members
# =============================================================================

class TestUpdateSeenMembers:

    def test_tracks_members(self):
        containers = [
            Container(
                name="Foo", kind="class", start_line=1, end_line=100,
                members=[
                    Declaration(name="a", kind="method", start_line=10, end_line=30),
                    Declaration(name="b", kind="method", start_line=40, end_line=60),
                    Declaration(name="c", kind="method", start_line=70, end_line=90),
                ]
            )
        ]
        decl_map = DeclarationMap(containers=containers, standalone=[])
        seen = {}

        update_seen_members(1, 50, decl_map, seen)
        assert "Foo" in seen
        assert seen["Foo"] == ["a"]  # Only method 'a' fits in lines 1-50 (b starts at 40 but ends at 60)

    def test_accumulates_across_chunks(self):
        containers = [
            Container(
                name="Foo", kind="class", start_line=1, end_line=100,
                members=[
                    Declaration(name="a", kind="method", start_line=10, end_line=30),
                    Declaration(name="b", kind="method", start_line=40, end_line=60),
                ]
            )
        ]
        decl_map = DeclarationMap(containers=containers, standalone=[])
        seen = {}

        update_seen_members(1, 35, decl_map, seen)
        assert seen["Foo"] == ["a"]

        update_seen_members(36, 100, decl_map, seen)
        assert seen["Foo"] == ["a", "b"]


# =============================================================================
# Tests for build_declaration_map_from_graph (tree-sitter-graph format)
# =============================================================================

def _make_graph_node(id, ntype, name, start_row, end_row, edges=None):
    """Build a mock tree-sitter-graph node with typed attrs."""
    node = {
        "id": id,
        "attrs": {
            "type": {"type": "string", "string": ntype},
            "name": {"type": "string", "string": name},
            "start_row": {"type": "int", "int": start_row},
            "end_row": {"type": "int", "int": end_row},
        },
        "edges": [{"sink": s} for s in (edges or [])],
    }
    return node


class TestBuildDeclarationMapFromGraph:
    """Tests for parsing tree-sitter-graph JSON into DeclarationMap."""

    def test_none_input(self):
        assert build_declaration_map_from_graph(None) is None

    def test_empty_list(self):
        assert build_declaration_map_from_graph([]) is None

    def test_empty_dict(self):
        assert build_declaration_map_from_graph({}) is None

    def test_single_class_with_method(self):
        """Class with one method — parent→child edge."""
        nodes = [
            _make_graph_node(0, "class", "Foo", 10, 50, edges=[1]),
            _make_graph_node(1, "method", "bar", 12, 20),
        ]
        dm = build_declaration_map_from_graph(nodes)
        assert dm is not None
        assert len(dm.containers) == 1
        assert dm.containers[0].name == "Foo"
        # 0-indexed rows → 1-indexed lines
        assert dm.containers[0].start_line == 11
        assert dm.containers[0].end_line == 51
        assert len(dm.containers[0].members) == 1
        assert dm.containers[0].members[0].name == "bar"
        assert dm.containers[0].members[0].start_line == 13

    def test_wrapped_format(self):
        """Graph data wrapped in {success: true, graph: [...]}."""
        nodes = [
            _make_graph_node(0, "class", "Foo", 10, 50, edges=[1]),
            _make_graph_node(1, "method", "bar", 12, 20),
        ]
        wrapped = {"success": True, "graph": nodes, "graph_nodes": 2}
        dm = build_declaration_map_from_graph(wrapped)
        assert dm is not None
        assert len(dm.containers) == 1
        assert dm.containers[0].name == "Foo"

    def test_duplicate_class_nodes_deduplicated(self):
        """Class appears once per member edge — should be deduplicated."""
        nodes = [
            _make_graph_node(0, "class", "Foo", 10, 100, edges=[2]),
            _make_graph_node(1, "class", "Foo", 10, 100, edges=[3]),
            _make_graph_node(2, "method", "a", 12, 30),
            _make_graph_node(3, "method", "b", 35, 60),
        ]
        dm = build_declaration_map_from_graph(nodes)
        assert dm is not None
        assert len(dm.containers) == 1
        assert dm.containers[0].name == "Foo"
        assert len(dm.containers[0].members) == 2
        member_names = [m.name for m in dm.containers[0].members]
        assert "a" in member_names
        assert "b" in member_names

    def test_standalone_enum(self):
        """Enum without edges becomes a standalone container."""
        nodes = [
            _make_graph_node(0, "enum", "Color", 5, 8),
        ]
        dm = build_declaration_map_from_graph(nodes)
        assert dm is not None
        assert len(dm.containers) == 1
        assert dm.containers[0].name == "Color"
        assert dm.containers[0].kind == "enum_declaration"
        assert len(dm.containers[0].members) == 0

    def test_multiple_member_types(self):
        """Class with method, constructor, property, field."""
        nodes = [
            _make_graph_node(0, "class", "Bar", 0, 100, edges=[4]),
            _make_graph_node(1, "class", "Bar", 0, 100, edges=[5]),
            _make_graph_node(2, "class", "Bar", 0, 100, edges=[6]),
            _make_graph_node(3, "class", "Bar", 0, 100, edges=[7]),
            _make_graph_node(4, "method", "doWork", 10, 20),
            _make_graph_node(5, "constructor", "Bar", 2, 8),
            _make_graph_node(6, "property", "Name", 25, 30),
            _make_graph_node(7, "field", "count", 35, 35),
        ]
        dm = build_declaration_map_from_graph(nodes)
        assert dm is not None
        assert len(dm.containers) == 1
        members = dm.containers[0].members
        assert len(members) == 4
        types = {m.kind for m in members}
        assert "method_declaration" in types
        assert "constructor_declaration" in types
        assert "property_declaration" in types
        assert "field_declaration" in types
        # Members sorted by start_line
        assert members[0].name == "Bar"  # constructor at row 2 → line 3
        assert members[1].name == "doWork"  # method at row 10 → line 11

    def test_row_to_line_conversion(self):
        """0-indexed rows converted to 1-indexed lines."""
        nodes = [
            _make_graph_node(0, "class", "X", 0, 9, edges=[1]),
            _make_graph_node(1, "method", "y", 2, 5),
        ]
        dm = build_declaration_map_from_graph(nodes)
        assert dm.containers[0].start_line == 1  # row 0 → line 1
        assert dm.containers[0].end_line == 10  # row 9 → line 10
        assert dm.containers[0].members[0].start_line == 3  # row 2 → line 3
        assert dm.containers[0].members[0].end_line == 6  # row 5 → line 6
