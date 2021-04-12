from typing import Optional

from src.data_structures.graph import Graph, Vertex


class DepthFirstPaths:
    """
    Finds all the paths incident to the source using depth-first search.

    This implementation finds all the paths from the source to all of its connected vertices
    and saves those paths in memory.
    """

    def __init__(self, graph: Graph, source: Vertex) -> None:
        self.graph = graph
        self.source = source
        self._paths = {}

        self._find_paths(self.source, [])

    def _find_paths(self, v: Vertex, base_path: [Vertex]):
        self._paths[v.key] = base_path + [v]

        for adj in v.adjacent:
            if adj.key not in self._paths:
                self._find_paths(adj, self._paths[v.key])

    def has_path_to(self, v: Vertex):
        """
        :return: True if there's a path from source to v. False otherwise.
        """
        return v.key in self._paths

    def path_to(self, v: Vertex) -> [Vertex]:
        """
        :return: list of vertices along the path from source to vertex. Empty list if there is no such path.
        """
        return self._paths[v.key] if v.key in self._paths else []


class DepthFirstPaths2:
    """
    This implementation does not store all the connected paths in memory.
    Instead, it only stores the second-to-last vertex of each path.
    e.g., for the path s->w->...->t->v, it stores only t, which will be used to
    construct the path from s to v.

    Compare to the above implementation, this one uses less memory
    but needs more time to find a path to a given vertex.
    """

    def __init__(self, graph: Graph, source: Vertex) -> None:
        self.graph = graph
        self.source = source
        self._edgesTo = {}

        self._find_edges(self.source, None)

    def _find_edges(self, v: Vertex, parent: Optional[Vertex]):
        self._edgesTo[v.key] = parent
        for adj in v.adjacent:
            if adj.key not in self._edgesTo:
                self._find_edges(adj, v)

    def has_path_to(self, v: Vertex):
        """
        :return: True if there's a path from source to v. False otherwise.
        """
        return v.key in self._edgesTo

    def path_to(self, v: Vertex) -> [Vertex]:
        """
        :return: list of vertices along the path from source to vertex. Empty list if there is no such path.
        """
        if not self.has_path_to(v):
            return []

        result = []
        current = v
        while not current.equals(self.source):
            result.append(current)
            current = self._edgesTo[current.key]

        result.append(self.source)

        result.reverse()
        return result
