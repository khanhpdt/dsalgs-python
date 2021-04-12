from src.algorithms.depth_first_paths import DepthFirstPaths, DepthFirstPaths2
from src.common.has_same_items import has_same_items
from src.data_structures.graph import Graph


class DepthFirstPathsTestCommon:

    def setup_method(self):
        self.graph = Graph()
        self.TestClass = None

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

    def assert_has_path_to(self, paths, keys):
        for key in keys:
            assert paths.has_path_to(self.graph.vertex(key))

    def assert_not_has_path_to(self, paths, keys):
        for key in keys:
            assert not paths.has_path_to(self.graph.vertex(key))

    def assert_path(self, paths, to_vertex_key, expected_keys):
        vertices = paths.path_to(self.graph.vertex(to_vertex_key))
        keys = [v.key for v in vertices]
        assert has_same_items(keys, expected_keys)

    def test_check_has_path(self):
        self.build_default_graph()

        paths = self.TestClass(self.graph, self.graph.vertex(0))
        self.assert_has_path_to(paths, [0, 1, 2, 3, 4, 5])
        self.assert_not_has_path_to(paths, [6, 7, 8])

        paths = self.TestClass(self.graph, self.graph.vertex(7))
        self.assert_has_path_to(paths, [6, 7, 8])
        self.assert_not_has_path_to(paths, [0, 1, 2, 3, 4, 5])

    def test_get_paths(self):
        self.build_default_graph()

        paths = self.TestClass(self.graph, self.graph.vertex(0))

        self.assert_path(paths, 0, [0])
        self.assert_path(paths, 1, [0, 1])
        self.assert_path(paths, 2, [0, 1, 2])
        self.assert_path(paths, 3, [0, 1, 2, 3])
        self.assert_path(paths, 4, [0, 1, 2, 3, 4])
        self.assert_path(paths, 5, [0, 1, 2, 3, 5])

        self.assert_path(paths, 6, [])
        self.assert_path(paths, 7, [])
        self.assert_path(paths, 8, [])


class TestDepthFirstPaths(DepthFirstPathsTestCommon):

    def setup_method(self):
        super().setup_method()
        self.TestClass = DepthFirstPaths


class TestDepthFirstPaths2(DepthFirstPathsTestCommon):

    def setup_method(self):
        super().setup_method()
        self.TestClass = DepthFirstPaths2
