from abc import ABC, abstractmethod


class Comparable(ABC):

    @abstractmethod
    def compare_to(self, other):
        raise NotImplementedError("Implement this")

    @abstractmethod
    def equals(self, other):
        raise NotImplementedError("Implement this")
