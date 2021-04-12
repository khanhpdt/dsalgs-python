from src.algorithms.connected_components import ConnectedComponents
from src.data_structures.graph import Graph


class TestConnectedComponents:

    def setup_method(self):
        self.graph = Graph()

    def build_default_graph(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(0, 5)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(2, 4)
        self.graph.add_edge(3, 4)
        self.graph.add_edge(3, 5)

        self.graph.add_edge(6, 7)
        self.graph.add_edge(6, 8)
        self.graph.add_edge(7, 8)

    def test_find_connected_components(self):
        self.build_default_graph()
        cc = ConnectedComponents(self.graph)

        assert cc.count() == 2

        self.assert_connected(cc, [0, 1, 2, 3, 4, 5])
        self.assert_connected(cc, [6, 7, 8])

        self.assert_not_connected(cc, 0, [6, 7, 8])
        self.assert_not_connected(cc, 7, [0, 1, 2, 3, 4, 5])

    def assert_connected(self, cc, connected_vertices_keys):
        for i in range(len(connected_vertices_keys) - 1):
            for j in range(i + 1, len(connected_vertices_keys)):
                v1 = self.graph.vertex(connected_vertices_keys[i])
                v2 = self.graph.vertex(connected_vertices_keys[j])
                assert cc.connected(v1, v2)
                assert cc.component_id(v1) == cc.component_id(v2)

    def assert_not_connected(self, cc, key, unconnected_vertices_keys):
        v = self.graph.vertex(key)
        for key in unconnected_vertices_keys:
            other_v = self.graph.vertex(key)
            assert not cc.connected(v, other_v)
            assert cc.component_id(v) != cc.component_id(other_v)
