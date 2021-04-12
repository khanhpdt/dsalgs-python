from src.algorithms.sorting.insertion_sort import insertion_sort, insertion_sort2
from tests.algorithms.sorting.sort_test_common import SortTestCommon


class TestInsertionSort(SortTestCommon):
    def sort_func(self, items):
        return insertion_sort(items)


class TestInsertionSort2(SortTestCommon):
    def sort_func(self, items):
        return insertion_sort2(items)
