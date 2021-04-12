from abc import ABC, abstractmethod
from math import floor

from src.common.utils import exchange, compare, lt_or_eq, gt_or_eq


class BinaryHeapProperty(ABC):

    @abstractmethod
    def hold_for_item(self, item, parent):
        raise NotImplementedError("Not supported")

    @abstractmethod
    def select_child(self, child1, child1_idx, child2, child2_idx):
        raise NotImplementedError("Not supported")

    def hold_for_array(self, arr):
        i = 0
        while (2 * i + 1) < len(arr):
            child_1 = 2 * i + 1
            if not self.hold_for_item(arr[child_1], arr[i]):
                print("Child %s > Node %s" % (child_1, i))
                return False

            child_2 = 2 * i + 2
            if child_2 < len(arr) and not self.hold_for_item(arr[child_2], arr[i]):
                print("Child %s > Node %s" % (child_2, i))
                return False

            i = i + 1

        return True


class MinHeapProperty(BinaryHeapProperty):

    def hold_for_item(self, item, parent):
        return lt_or_eq(parent, item)

    def select_child(self, child1, child1_idx, child2, child2_idx):
        return child1_idx if lt_or_eq(child1, child2) else child2_idx


class MaxHeapProperty(BinaryHeapProperty):

    def hold_for_item(self, item, parent):
        return gt_or_eq(parent, item)

    def select_child(self, child1, child1_idx, child2, child2_idx):
        return child1_idx if gt_or_eq(child1, child2) else child2_idx


class BinaryHeap:
    """
    Binary heap is a data structure where each node has at most two children
    and is greater than or equal to its children.

    Computational complexity:
        - Insert: O(log(n)), where n is the number of items
        - Remove: O(log(n)), where n is the number of items
    """

    def __init__(self, heap_property: BinaryHeapProperty) -> None:
        self._heap_property = heap_property
        self._items = []

    @staticmethod
    def min_heap():
        return BinaryHeap(MinHeapProperty())

    @staticmethod
    def max_heap():
        return BinaryHeap(MaxHeapProperty())

    def build(self, arr):
        self._items = []
        for item in arr:
            self.insert(item)

    def insert(self, item):
        self._items.append(item)
        self._ensure_heap_property_bottom_up(len(self._items) - 1)

    def _ensure_heap_property_bottom_up(self, item_idx):
        parent_idx = self._get_parent_of(item_idx)
        while parent_idx >= 0 and not self._heap_property.hold_for_item(self.get(item_idx), self.get(parent_idx)):
            exchange(self._items, item_idx, parent_idx)
            item_idx = parent_idx
            parent_idx = self._get_parent_of(item_idx)

    def get(self, item_idx):
        if item_idx < 0 or item_idx >= self.size():
            return None
        return self._items[item_idx]

    def size(self):
        return len(self._items)

    @staticmethod
    def _get_parent_of(i):
        return int(floor((i - 1) / 2))

    def get_all(self):
        return self._items.copy()

    def check_heap_property(self):
        return self._heap_property.hold_for_array(self.get_all())

    def remove(self):
        root_idx = 0
        return self._remove_item(root_idx)

    def _remove_item(self, item_idx):
        item = self.get(item_idx)

        if item is None:
            return item

        self._items[item_idx] = self._items[len(self._items) - 1]
        self._items.pop()

        self._ensure_heap_property_top_down(item_idx)

        return item

    def _ensure_heap_property_top_down(self, item_idx):
        child_idx = self._select_child_to_replace(item_idx)

        while child_idx is not None \
                and not self._heap_property.hold_for_item(self.get(child_idx), self.get(item_idx)):
            exchange(self._items, item_idx, child_idx)
            item_idx = child_idx
            child_idx = self._select_child_to_replace(item_idx)

    def _select_child_to_replace(self, item_idx):
        child1_idx = item_idx * 2 + 1
        child1 = self.get(child1_idx)
        child2_idx = item_idx * 2 + 2
        child2 = self.get(child2_idx)

        if child1 is None and child2 is None:
            return None
        elif child2 is None:
            return child1_idx
        return self._heap_property.select_child(child1, child1_idx, child2, child2_idx)
