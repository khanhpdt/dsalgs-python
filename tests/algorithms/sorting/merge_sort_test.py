from src.algorithms.sorting.merge_sort import merge, merge_sort_top_down, merge_sort_bottom_up
from tests.algorithms.sorting.sort_test_common import SortTestCommon


class TestMerge:

    def test_merge(self):
        arr = [3, 7, 19, 5, 8, 10, 12, 2, 1]
        merge(arr, 0, 2, 5)
        assert arr[0:6] == [3, 5, 7, 8, 10, 19]

    def test_merge_whole_array(self):
        arr = [3, 7, 19, 5, 8, 10]
        merge(arr, 0, 2, 5)
        assert arr == [3, 5, 7, 8, 10, 19]


class TestMergeSortTopDown(SortTestCommon):

    def sort_func(self, items):
        return merge_sort_top_down(items)


class TestMergeSortBottomUp(SortTestCommon):

    def sort_func(self, items):
        return merge_sort_bottom_up(items)
