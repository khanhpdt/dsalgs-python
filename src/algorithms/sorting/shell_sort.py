from math import floor

from src.algorithms.sorting.insertion_sort import insertion_sort
from src.common.utils import list_to_str, exchange


def shell_sort(arr):
    print("Sorting %s..." % list_to_str(arr))

    items = arr.copy()

    h = start_of_gap_sequence(len(items))

    while h >= 1:
        for i in range(0, h):
            items[i::h] = insertion_sort(items[i::h])
        h = floor(h / 3)

    return items


def start_of_gap_sequence(n):
    # Use sequence (1/2) * (3^k - 1), k >= 1. Start from the largest element smaller than n/3.
    h = 1
    while h < floor(n / 3):
        h = 3 * h + 1
    return h


def shell_sort2(arr):
    print("Sorting %s..." % list_to_str(arr))

    items = arr.copy()

    h = start_of_gap_sequence(len(items))

    while h >= 1:
        for i in range(h, len(items)):
            # a compact version of insertion sort to sort the items h-position apart
            # i.e., sort items i, i-h, i-2*h, ...
            for j in range(i, h - 1, -h):
                if items[j] < items[j - h]:
                    exchange(items, j, j - h)
        h = floor(h / 3)

    return items
