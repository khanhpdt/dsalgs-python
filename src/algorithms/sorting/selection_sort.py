from src.common.utils import exchange, list_to_str


def selection_sort(arr):
    print("Sorting %s..." % list_to_str(arr))

    items = arr.copy()

    for i in range(0, len(items) - 1):
        # select the minimum item from the unsorted items
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j

        if i != min_index:
            exchange(items, i, min_index)

    return items
