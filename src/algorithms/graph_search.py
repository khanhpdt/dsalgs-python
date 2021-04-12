from abc import ABC, abstractmethod

from src.data_structures.graph import Vertex


class GraphSearch(ABC):

    def __init__(self, source: Vertex) -> None:
        self.source = source

    @abstractmethod
    def marked(self, v: Vertex):
        """
        Check if v is connected with the source.
        :return: True if v is connected. False otherwise.
        """
        raise NotImplementedError("Implement this")

    @abstractmethod
    def count(self):
        """
        :return: the number of vertices connected with the source.
        """
        raise NotImplementedError("Implement this")
