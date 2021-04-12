from abc import ABC, abstractmethod

from src.common.key_value import Key


class SymbolTable(ABC):

    @abstractmethod
    def put(self, key: Key, value):
        raise NotImplementedError("Implement this")

    @abstractmethod
    def get(self, key: Key):
        """
        :return: Get the value associated with the given key. None if no key found.
        """
        raise NotImplementedError("Implement this")

    @abstractmethod
    def delete(self, key: Key):
        """
        Remove from the table the record associated with the given key.
        """
        raise NotImplementedError("Implement this")

    @abstractmethod
    def contains(self, key: Key):
        """
        :return: True if the table contains a record associated with the given key. False otherwise.
        """
        raise NotImplementedError("Implement this")

    @abstractmethod
    def size(self):
        """
        :return: The number of items in the table.
        """
        raise NotImplementedError("Implement this")

    def is_empty(self):
        """
        :return: True if the table is empty. False otherwise.
        """
        return self.size() == 0