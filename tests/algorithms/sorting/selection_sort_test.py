from src.algorithms.sorting.selection_sort import selection_sort
from tests.algorithms.sorting.sort_test_common import SortTestCommon


class TestSelectionSort(SortTestCommon):

    def sort_func(self, items):
        return selection_sort(items)
