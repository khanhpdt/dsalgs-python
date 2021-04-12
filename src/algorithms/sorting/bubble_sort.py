from src.common.utils import list_to_str, exchange


def bubble_sort(arr):
    print("Sorting %s..." % list_to_str(arr))

    items = arr.copy()

    for i in reversed(range(len(items))):
        for j in range(0, i):
            if items[j] > items[j + 1]:
                exchange(items, j, j + 1)

    return items
