from src.algorithms.graph_search import GraphSearch
from src.data_structures.graph import Vertex


class BreadthFirstSearch(GraphSearch):

    def __init__(self, source: Vertex) -> None:
        super().__init__(source)
        self._marked = {}

        self._search()

    def _search(self):
        to_be_visited_vertices = [self.source]
        self._marked[self.source.key] = True

        while len(to_be_visited_vertices) > 0:
            # visit the vertices close to the source first
            v = to_be_visited_vertices.pop(0)

            for adj in v.adjacent:
                if adj.key not in self._marked:
                    self._marked[adj.key] = True
                    to_be_visited_vertices.append(adj)

    def marked(self, v: Vertex):
        return v.key in self._marked

    def count(self):
        return len(self._marked)
