from math import floor

from src.common.utils import eq, lt, gt


def binary_search(items, item):
    low = 0
    high = len(items) - 1

    while high >= low:
        mid = int(floor((high + low) / 2))
        if eq(items[mid], item):
            return mid

        if gt(item, items[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return None
