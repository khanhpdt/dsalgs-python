import random

from src.common.utils import exchange, list_to_str, lt_or_eq, gt_or_eq, gt, lt


def quick_sort(arr):
    print("Sorting %s..." % list_to_str(arr))

    items = arr.copy()
    random.shuffle(items)

    _quick_sort_recursive(items, 0, len(items) - 1)

    return items


def _quick_sort_recursive(items, start, end):
    partitioning_item_idx = partition(items, start, end)
    if partitioning_item_idx is not None:
        _quick_sort_recursive(items, start, partitioning_item_idx - 1)
        _quick_sort_recursive(items, partitioning_item_idx + 1, end)


def partition(items, start, end):
    if start >= end:
        return None

    partitioning_item = items[start]

    left = start
    right = end + 1
    while True:
        # scan from the left to find the item not in correct position, i.e., item > partitioning item
        left = left + 1
        while left <= end and lt_or_eq(items[left], partitioning_item):
            left = left + 1

        # scan from the right to find the item not in correct position, i.e., item < partitioning item
        right = right - 1
        while right > start and gt_or_eq(items[right], partitioning_item):
            right = right - 1

        # partitioning done. what's left is to move the partitioning item to the right position.
        if left >= right:
            break

        exchange(items, left, right)

    exchange(items, start, right)

    return right


def quick_sort_3way(arr):
    print("Sorting %s..." % list_to_str(arr))

    items = arr.copy()
    random.shuffle(items)

    _quick_sort_3way_recursive(items, 0, len(items) - 1)

    return items


def _quick_sort_3way_recursive(items, start, end):
    less_than_idx, greater_than_idx = partition_3way(items, start, end)
    if less_than_idx is not None and greater_than_idx is not None:
        _quick_sort_3way_recursive(items, start, less_than_idx - 1)
        _quick_sort_3way_recursive(items, greater_than_idx + 1, end)


def partition_3way(items, start, end):
    if start >= end:
        return None, None

    partitioning_item = items[start]
    less_than_idx = start
    greater_than_idx = end

    # Invariant:
    #   - a[start..less_than_idx - 1] < partitioning_item
    #   - a[greater_than_idx + 1..end] > partitioning_item
    #   - a[less_than_idx..i-1] = partitioning_item
    #   - a[i..greater_than_idx] are not yet examined

    i = start + 1
    while i <= greater_than_idx:
        if lt(items[i], partitioning_item):
            # move items < partitioning_item to the left
            exchange(items, i, less_than_idx)
            less_than_idx = less_than_idx + 1
            # move the pointer because we know that the new item at the position i is
            # either equal or less than the partitioning item
            i = i + 1
        elif gt(items[i], partitioning_item):
            # move items > partitioning_item to the right
            exchange(items, i, greater_than_idx)
            greater_than_idx = greater_than_idx - 1
            # here, we don't move the pointer because we don't know how the new item
            # at the position i compares to the partitioning item
        else:
            # leave the items = partitioning_item where they are
            i = i + 1

    return less_than_idx, greater_than_idx
