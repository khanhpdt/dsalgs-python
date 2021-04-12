from src.algorithms.depth_first_search import DepthFirstSearch
from src.data_structures.graph import Graph, Vertex


class ConnectedComponents:

    def __init__(self, graph: Graph) -> None:
        self.graph = graph

        self._vertex_components = {}
        self._component_count = 0

        self._find_components()

    def _find_components(self):
        vertices_without_components = {}
        for v in self.graph.vertices():
            vertices_without_components[v.key] = v

        while len(vertices_without_components) > 0:
            _, v = vertices_without_components.popitem()
            self._vertex_components[v.key] = self._component_count

            dfs = DepthFirstSearch(v)

            v_keys = [k for k in vertices_without_components.keys()]
            for other_v_key in v_keys:
                if dfs.marked(self.graph.vertex(other_v_key)):
                    self._vertex_components[other_v_key] = self._component_count
                    vertices_without_components.pop(other_v_key)

            self._component_count = self._component_count + 1

    def connected(self, v1: Vertex, v2: Vertex) -> bool:
        """
        Check if v1 and v2 are connected.
        :return: True if they are. False otherwise.
        """
        if v1.key not in self._vertex_components or v2.key not in self._vertex_components:
            raise ValueError("One of the vertices is not in the graph")
        return self._vertex_components[v1.key] == self._vertex_components[v2.key]

    def count(self) -> int:
        """
        :return: the number of connected components in the graph.
        """
        return self._component_count

    def component_id(self, v: Vertex) -> int:
        """
        :return: the id of the component where the given vertex belongs
        """
        if v.key not in self._vertex_components:
            raise ValueError("Vertex is not the graph")
        return self._vertex_components[v.key]
