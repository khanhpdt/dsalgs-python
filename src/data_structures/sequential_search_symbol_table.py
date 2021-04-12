from src.algorithms.sorting.quick_sort import quick_sort
from src.common.key_value import Key, KeyValue
from src.common.utils import index_of, gt, lt, gt_or_eq, lt_or_eq
from src.data_structures.ordered_symbol_table import OrderedSymbolTable


class SequentialSearchSymbolTable(OrderedSymbolTable):
    """
    This implementation maintains an unordered list to store the items.
    The search operation searches a given key by simply going over each item
    in the list and compare it with the given key.
    """

    def __init__(self) -> None:
        self._items: [KeyValue] = []

    def put(self, key: Key, value):
        item_idx = self._index_of_key(key)
        if item_idx is None:
            self._items.append(KeyValue(key, value))
        else:
            self._items[item_idx].value = value

    def _index_of_key(self, key):
        return index_of(self._items, KeyValue(key))

    def get(self, key: Key):
        item_idx = self._index_of_key(key)
        if item_idx is not None:
            return self._items[item_idx].value
        return None

    def delete(self, key: Key):
        item_idx = self._index_of_key(key)
        if item_idx is not None:
            self._items.pop(item_idx)

    def contains(self, key: Key):
        return self.get(key) is not None

    def min(self):
        if self.is_empty():
            return None

        current_min = self._items[0].key
        for i in range(1, self.size_of_range()):
            if lt(self._items[i].key, current_min):
                current_min = self._items[i].key
        return current_min

    def max(self):
        if self.is_empty():
            return None

        current_max = self._items[0].key
        for i in range(1, self.size_of_range()):
            if gt(self._items[i].key, current_max):
                current_max = self._items[i].key
        return current_max

    def floor(self, key: Key):
        if self.is_empty():
            return None

        candidate = None
        for i in range(self.size_of_range()):
            current_item_key = self._items[i].key
            if current_item_key.equals(key):
                return current_item_key

            candidate = current_item_key \
                if lt(current_item_key, key) and (candidate is None or gt(current_item_key, candidate)) \
                else candidate

        return candidate

    def ceiling(self, key: Key):
        if self.is_empty():
            return None

        candidate = None
        for i in range(self.size_of_range()):
            current_item_key = self._items[i].key
            if current_item_key.equals(key):
                return current_item_key

            candidate = current_item_key \
                if gt(current_item_key, key) and (candidate is None or lt(current_item_key, candidate)) \
                else candidate

        return candidate

    def rank(self, key: Key):
        result = 0
        for item in self._items:
            if lt(item.key, key):
                result = result + 1
        return result

    def select(self, rank):
        if rank < 0 or rank >= self.size_of_range():
            return None

        sorted_items = quick_sort(self._items)
        return sorted_items[rank].key

    def size_of_range(self, low: Key = None, high: Key = None):
        return len(self.range(low, high))

    def range(self, low: Key = None, high: Key = None):
        result = []
        for item in self._items:
            key = item.key

            in_range = True
            if low is not None:
                in_range = gt_or_eq(key, low)
            if in_range and high is not None:
                in_range = lt_or_eq(key, high)

            if in_range:
                result.append(key)

        return result

    def size(self):
        return len(self._items)
