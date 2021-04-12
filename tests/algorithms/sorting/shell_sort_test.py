from src.algorithms.sorting.shell_sort import shell_sort, shell_sort2
from tests.algorithms.sorting.sort_test_common import SortTestCommon


class TestShellSort(SortTestCommon):

    def sort_func(self, items):
        return shell_sort(items)


class TestShellSort2(SortTestCommon):

    def sort_func(self, items):
        return shell_sort2(items)