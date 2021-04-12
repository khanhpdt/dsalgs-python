from src.common.utils import list_to_str
from src.data_structures.binary_heap import BinaryHeap, MaxHeapProperty


def heap_sort(arr):
    print("Sorting %s..." % list_to_str(arr))

    items = arr.copy()

    heap = BinaryHeap.max_heap()
    heap.build(items)

    for i in reversed(range(len(items))):
        items[i] = heap.remove()

    return items
