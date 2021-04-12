from math import floor

from src.common.utils import list_to_str


def merge_sort_top_down(arr):
    print("Sorting %s..." % list_to_str(arr))

    items = arr.copy()

    # top-down: start from the whole array
    _merge_sort_top_down_recursive(items, 0, len(items) - 1)

    return items


def _merge_sort_top_down_recursive(items, start_idx, end_idx):
    if start_idx > end_idx:
        return []

    if start_idx == end_idx:
        return [items[start_idx]]

    mid = int(floor((start_idx + end_idx) / 2))

    _merge_sort_top_down_recursive(items, start_idx, mid)
    _merge_sort_top_down_recursive(items, mid + 1, end_idx)
    merge(items, start_idx, mid, end_idx)


def merge_sort_bottom_up(arr):
    print("Sorting %s..." % list_to_str(arr))

    items = arr.copy()
    n = len(items)

    # bottom-up: start from the smallest subarrays up until the whole array
    sz = 1
    while sz < n:
        for start in range(0, n - sz, 2 * sz):
            merge(items, start, start + sz - 1, min(start + 2 * sz - 1, n - 1))
        sz = 2 * sz

    return items


def merge(items, start, mid, end):
    """
    Merge two sorted subarrays: one from start until mid, and the other from mid + 1 until end

    :return: a sorted array containing elements in the two sorted subarrays
    """

    aux = items[start:(end + 1)].copy()

    first_half_idx = 0
    first_half_idx_end = mid - start
    second_half_idx = mid - start + 1
    second_half_idx_end = len(aux) - 1

    for i in range(start, end + 1):
        if first_half_idx > first_half_idx_end:
            items[i] = aux[second_half_idx]
            second_half_idx = second_half_idx + 1
        elif second_half_idx > second_half_idx_end:
            items[i] = aux[first_half_idx]
            first_half_idx = first_half_idx + 1
        elif aux[first_half_idx] <= aux[second_half_idx]:
            items[i] = aux[first_half_idx]
            first_half_idx = first_half_idx + 1
        else:
            items[i] = aux[second_half_idx]
            second_half_idx = second_half_idx + 1
