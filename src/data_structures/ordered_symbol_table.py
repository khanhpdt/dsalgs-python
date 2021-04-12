from abc import abstractmethod

from src.common.key_value import Key
from src.data_structures.symbol_table import SymbolTable


class OrderedSymbolTable(SymbolTable):

    @abstractmethod
    def min(self):
        """
        :return: the minimum key in the table.
        """
        raise NotImplementedError("Implement this")

    @abstractmethod
    def max(self):
        """
        :return: the maximum key in the table.
        """
        raise NotImplementedError("Implement this")

    @abstractmethod
    def floor(self, key: Key):
        """
        :return: the largest key in the table that is less than or equal to the given key.
        """
        raise NotImplementedError("Implement this")

    @abstractmethod
    def ceiling(self, key: Key):
        """
        :return: the smallest key in the table that is greater than or equal to the given key.
        """
        raise NotImplementedError("Implement this")

    @abstractmethod
    def rank(self, key: Key):
        """
        :return: the number of keys in the table less than the given key
        """
        raise NotImplementedError("Implement this")

    @abstractmethod
    def select(self, rank):
        """
        :return: the key of the given rank
        """
        raise NotImplementedError("Implement this")

    @abstractmethod
    def size_of_range(self, low: Key = None, high: Key = None):
        """
        :return: the number of keys in range [low, high] inclusive.
        If low or high is not given, the corresponding side is unbounded.
        """
        raise NotImplementedError("Implement this")

    @abstractmethod
    def range(self, low: Key = None, high: Key = None):
        """
        :return: the list of keys in range [low, high].
        If low or high is not given, the corresponding side is unbounded.
        """
        raise NotImplementedError("Implement this")
