import random

from src.data_structures.binary_heap import BinaryHeap, MinHeapProperty, MaxHeapProperty


class TestBinaryMinHeapProperty:

    heap_property = None

    def setup_class(self):
        self.heap_property = MinHeapProperty()

    def test_check_node(self):
        assert self.heap_property.hold_for_item(2, 1)
        assert not self.heap_property.hold_for_item(1, 2)

    def test_check_heap(self):
        assert self.heap_property.hold_for_array([1, 2, 3])
        assert self.heap_property.hold_for_array([1, 3, 2])
        assert not self.heap_property.hold_for_array([2, 1, 3])
        assert not self.heap_property.hold_for_array([1, 2, 7, 4, 5, 6])
        assert self.heap_property.hold_for_array([1, 2, 7, 4, 5, 8])


class TestBinaryMaxHeapProperty:

    heap_property = None

    def setup_class(self):
        self.heap_property = MaxHeapProperty()

    def test_check_node(self):
        assert self.heap_property.hold_for_item(1, 2)
        assert not self.heap_property.hold_for_item(2, 1)

    def test_check_heap(self):
        assert self.heap_property.hold_for_array([3, 2, 1])
        assert self.heap_property.hold_for_array([3, 1, 2])
        assert not self.heap_property.hold_for_array([2, 1, 3])
        assert not self.heap_property.hold_for_array([7, 6, 4, 3, 2, 5])
        assert self.heap_property.hold_for_array([7, 6, 4, 3, 2, 1])


class BinaryHeapTestCommon:

    heap: BinaryHeap = None

    def test_build_heap_empty(self):
        self.heap.build([])
        assert self.heap.check_heap_property()

    def test_build_heap_one_element(self):
        self.heap.build([1])
        assert self.heap.check_heap_property()

    def test_build_heap_three_elements(self):
        self.heap.build([2, 1, 3])
        assert self.heap.check_heap_property()

    def test_build_heap_many(self):
        for i in range(100):
            arr = list(range(i))
            random.shuffle(arr)
            self.heap.build(arr)
            assert self.heap.check_heap_property()

    def test_remove_makes_heap_empty(self):
        self.heap.build([2])

        root = self.heap.remove()

        assert root == 2
        assert self.heap.size() == 0

    def test_remove_from_empty_heap(self):
        self.heap.build([])

        root = self.heap.remove()

        assert root is None

    def test_get_invalid_item_index(self):
        self.heap.build([])
        assert self.heap.get(1) is None

        self.heap.build([1, 3, 2])
        assert self.heap.get(3) is None

        self.heap.build([1, 3, 2])
        assert self.heap.get(-1) is None


class TestBinaryMaxHeap(BinaryHeapTestCommon):

    def setup_class(self):
        self.heap = BinaryHeap.max_heap()

    def test_remove_root_keeps_heap_property(self):
        self.heap.build([2, 1, 3, 5, 4, 6])

        root = self.heap.remove()

        assert root == 6
        assert self.heap.size() == 5
        assert self.heap.check_heap_property()


class TestBinaryMinHeap(BinaryHeapTestCommon):

    def setup_class(self):
        self.heap = BinaryHeap.min_heap()

    def test_remove_root_keeps_heap_property(self):
        self.heap.build([2, 1, 3, 5, 4, 6])

        root = self.heap.remove()

        assert root == 1
        assert self.heap.size() == 5
        assert self.heap.check_heap_property()
