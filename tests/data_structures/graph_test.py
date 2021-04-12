from src.common.has_same_items import has_same_items
from src.data_structures.graph import Graph


class TestGraph:

    def setup_method(self):
        self.graph = Graph()

    def test_add_vertex(self):
        self.graph.add_vertex(1)
        assert self.graph.vertex(1).key == 1

    def test_add_vertex_update_existing(self):
        self.graph.add_vertex(1, 100)
        assert self.graph.vertex(1).value == 100

        self.graph.add_vertex(1, 200)
        assert self.graph.vertex(1).value == 200

    def test_add_edge_should_add_vertex_if_not_exist(self):
        assert self.graph.vertex(1) is None
        assert self.graph.vertex(2) is None

        self.graph.add_edge(1, 2)

        assert self.graph.vertex(1) is not None
        assert self.graph.vertex(2) is not None

    def test_get_adjacents(self):
        self.graph.add_vertex(1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)

        self.assert_adjacents(1, [2, 3])
        self.assert_adjacents(2, [1])
        self.assert_adjacents(3, [1])

    def assert_adjacents(self, key, expected_adj_keys):
        adjacents = self.graph.adj(key)
        adj_keys = [adj.key for adj in adjacents]
        assert has_same_items(adj_keys, expected_adj_keys)