from src.common.comparable import Comparable
from src.common.utils import compare, eq


class Vertex(Comparable):

    def __init__(self, key, value=None) -> None:
        self.key = key
        self.value = value
        self.adjacent: [Vertex] = []

    def compare_to(self, other):
        return compare(self.key, other.key)

    def equals(self, other):
        return eq(self.key, other.key)


class Graph:

    def __init__(self) -> None:
        self._vertices: [Vertex] = []
        self._vertex_indices = {}

    def add_vertex(self, key, value=None):
        if type(key) not in (int, str):
            raise ValueError("Type not supported")

        if self.vertex(key) is not None:
            self.vertex(key).value = value
        else:
            self._add_vertex(Vertex(key, value))

    def _add_vertex(self, v: Vertex):
        self._vertices.append(v)
        self._vertex_indices[v.key] = len(self._vertices) - 1

    def vertex(self, key) -> Vertex:
        return self._vertices[self._vertex_indices[key]] if key in self._vertex_indices else None

    def add_edge(self, vertex1_key, vertex2_key):
        vertex1 = self.vertex(vertex1_key)
        if vertex1 is None:
            vertex1 = Vertex(vertex1_key)
            self._add_vertex(vertex1)

        vertex2 = self.vertex(vertex2_key)
        if vertex2 is None:
            vertex2 = Vertex(vertex2_key)
            self._add_vertex(vertex2)

        vertex1.adjacent.append(vertex2)
        vertex2.adjacent.append(vertex1)

    def adj(self, vertex_key):
        vertex = self.vertex(vertex_key)
        if vertex is None:
            raise ValueError(f"Found no vertex with key: {vertex_key}.")
        return vertex.adjacent

    def vertices(self):
        return self._vertices.copy()
