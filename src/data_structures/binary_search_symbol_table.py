from math import floor

from src.common.key_value import Key, KeyValue
from src.common.utils import lt, eq, shift_right, gt
from src.data_structures.ordered_symbol_table import OrderedSymbolTable


class BinarySearchSymbolTable(OrderedSymbolTable):

    def __init__(self) -> None:
        self._items: [KeyValue] = []

    def put(self, key: Key, value):
        r = self.rank(key)

        if r >= len(self._items):
            self._items.append(KeyValue(key, value))
        elif eq(self._items[r].key, key):
            self._items[r].value = value
        else:
            shift_right(self._items, r)
            self._items[r] = KeyValue(key, value)

    def get(self, key: Key):
        idx = self._index_of_key(key)
        return self._items[idx].value if idx is not None else None

    def delete(self, key: Key):
        idx = self._index_of_key(key)
        if idx is None:
            return
        self._items.pop(idx)

    def _index_of_key(self, key):
        r = self.rank(key)
        return r if r < len(self._items) and eq(self._items[r].key, key) else None

    def contains(self, key: Key):
        return self._index_of_key(key) is not None

    def min(self):
        return self._items[0].key if not self.is_empty() else None

    def max(self):
        return self._items[-1].key if not self.is_empty() else None

    def floor(self, key: Key):
        r = self.rank(key)
        if r >= len(self._items):
            return self.max()
        if r == 0 and not eq(self._items[r].key, key):
            return None
        return self._items[r].key if eq(self._items[r].key, key) else self._items[r - 1].key

    def ceiling(self, key: Key):
        r = self.rank(key)
        if r >= len(self._items):
            return None
        if r == 0 and not eq(self._items[r].key, key):
            return self.min()
        return self._items[r].key

    def rank(self, key: Key):
        low = 0
        high = len(self._items) - 1
        while high >= low:
            mid = int(floor(high + low) / 2)
            if eq(key, self._items[mid].key):
                return mid
            if mid + 1 < len(self._items) and gt(key, self._items[mid].key) and lt(key, self._items[mid + 1].key):
                return mid + 1
            if gt(key, self._items[mid].key):
                low = mid + 1
            else:
                high = mid - 1

        if low >= len(self._items):
            return len(self._items)
        if high < 0:
            return 0

    def select(self, rank):
        if rank < 0 or rank >= len(self._items):
            return None
        return self._items[rank].key

    def size_of_range(self, low: Key = None, high: Key = None):
        return len(self.range(low, high))

    def range(self, low: Key = None, high: Key = None):
        rank_of_low = self.rank(low) if low is not None else 0
        rank_of_high = self.rank(high) if high is not None else len(self._items) - 1

        if rank_of_low > rank_of_high:
            return []

        result = []
        for i in range(rank_of_low, rank_of_high):
            result.append(self._items[i].key)

        if high is None or (0 <= rank_of_high < len(self._items) and eq(self._items[rank_of_high].key, high)):
            result.append(self._items[rank_of_high].key)

        return result

    def size(self):
        return len(self._items)
