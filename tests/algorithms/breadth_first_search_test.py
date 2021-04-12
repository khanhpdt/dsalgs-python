from src.algorithms.breadth_first_search import BreadthFirstSearch
from src.data_structures.graph import Graph


class TestBreadthFirstSearch:

    def setup_method(self):
        self.graph = Graph()

    def test_search_all_connected_vertices(self):
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

        bfs = BreadthFirstSearch(self.graph.vertex(0))
        assert bfs.count() == 6
        self.assert_marked(bfs, [0, 1, 2, 3, 4, 5])

        bfs = BreadthFirstSearch(self.graph.vertex(6))
        assert bfs.count() == 3
        self.assert_marked(bfs, [6, 7, 8])

    def assert_marked(self, bfs, marked_keys):
        for key in marked_keys:
            assert bfs.marked(self.graph.vertex(key))
