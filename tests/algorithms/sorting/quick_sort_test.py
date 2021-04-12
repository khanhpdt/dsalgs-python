import random

from src.algorithms.sorting.quick_sort import quick_sort, partition, partition_3way, quick_sort_3way
from tests.algorithms.sorting.sort_test_common import SortTestCommon


class TestPartition:

    def test_partition_return_mid(self):
        arr = [3, 9, 2, 12, 5, 6, 4, 20, 28]
        mid = partition(arr, 1, 7)
        assert mid == 5

    def test_partition(self):
        arr = [3, 9, 2, 12, 5, 6, 4, 20, 28]
        partition(arr, 1, 7)
        assert arr == [3, 6, 2, 4, 5, 9, 12, 20, 28]

    def test_partition_many(self):
        for i in range(100):
            arr = list(range(i + 1))
            random.shuffle(arr)

            low = 0
            high = len(arr) - 1
            partitioning_item = arr[low]

            partition(arr, low, high)

            self.assert_partition(arr, low, high, partitioning_item)

    @staticmethod
    def assert_partition(arr, low, high, partitioning_item):
        mid_index = arr.index(partitioning_item)

        for j in range(low, mid_index):
            assert arr[j] <= partitioning_item

        for j in range(mid_index + 1, high):
            assert arr[j] >= partitioning_item


class TestQuickSort(SortTestCommon):

    def sort_func(self, items):
        return quick_sort(items)


class TestPartition3Way:

    def test_partition(self):
        arr = [3, 9, 2, 12, 9, 6, 9, 20, 28]
        partition_3way(arr, 1, 7)
        assert arr == [3, 2, 6, 9, 9, 9, 20, 12, 28]

    def test_partition_return_less_than_and_greater_than_indexes(self):
        arr = [3, 9, 2, 12, 9, 6, 9, 20, 28]
        lt_idx, gt_idx = partition_3way(arr, 1, 7)
        assert lt_idx == 3 and gt_idx == 5

    def test_partition_many(self):
        for i in range(100):
            arr = list(range(i + 1))
            random.shuffle(arr)

            # duplicate partitioning_item for 5 times
            partitioning_item = arr[0]
            for j in range(3):
                arr.append(j)
            random.shuffle(arr)
            arr = [partitioning_item] + arr

            low = 0
            high = len(arr) - 1

            lt_idx, gt_idx = partition_3way(arr, low, high)

            self.assert_partition(arr, low, high, lt_idx, gt_idx, partitioning_item)

    @staticmethod
    def assert_partition(arr, low, high, lt_idx, gt_idx, partitioning_item):
        for i in range(low, lt_idx):
            assert arr[i] < partitioning_item

        for i in range(lt_idx, gt_idx + 1):
            assert arr[i] == partitioning_item

        for i in range(gt_idx + 1, high + 1):
            assert arr[i] > partitioning_item


class TestQuickSort3Way(SortTestCommon):

    def sort_func(self, items):
        return quick_sort_3way(items)
