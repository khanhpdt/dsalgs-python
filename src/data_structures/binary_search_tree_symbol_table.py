from src.common.key_value import Key
from src.data_structures.binary_search_tree import BinarySearchTree
from src.data_structures.ordered_symbol_table import OrderedSymbolTable


class BinarySearchTreeSymbolTable(OrderedSymbolTable):

    def __init__(self) -> None:
        self.tree = BinarySearchTree()

    def put(self, key: Key, value):
        self.tree.put(key, value)

    def get(self, key: Key):
        node = self.tree.get(key)
        return node.value if node is not None else None

    def delete(self, key: Key):
        self.tree.delete(key)

    def contains(self, key: Key):
        return self.get(key) is not None

    def min(self):
        min_node = self.tree.min()
        return min_node.key if min_node is not None else None

    def max(self):
        max_node = self.tree.max()
        return max_node.key if max_node is not None else None

    def floor(self, key: Key):
        floor_node = self.tree.floor(key)
        return floor_node.key if floor_node is not None else None

    def ceiling(self, key: Key):
        ceiling_node = self.tree.ceiling(key)
        return ceiling_node.key if ceiling_node is not None else None

    def rank(self, key: Key):
        return self.tree.rank(key)

    def select(self, rank):
        node = self.tree.select(rank)
        return node.key if node is not None else None

    def size_of_range(self, low: Key = None, high: Key = None):
        return len(self.range(low, high))

    def range(self, low: Key = None, high: Key = None):
        nodes = self.tree.range(low, high)
        return list(map(lambda node: node.key, nodes))

    def size(self):
        return self.tree.size()
