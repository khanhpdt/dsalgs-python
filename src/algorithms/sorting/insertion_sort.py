from src.common.utils import move, list_to_str


def insertion_sort(arr):
    print("Sorting %s..." % list_to_str(arr))

    items = arr.copy()

    for i in range(len(items)):
        item = items[i]

        # shift items on the left of item i to the right to preserve the right place to insert the item i
        j = i - 1
        while j >= 0 and items[j] > item:
            items[j + 1] = items[j]
            j = j - 1

        items[j + 1] = item

    return items


def insertion_sort2(arr):
    print("Sorting %s..." % list_to_str(arr))

    items = arr.copy()

    for i in range(len(items)):
        # find the position to insert items[i] without breaking the order in the sorted area
        j = i - 1
        while j >= 0 and items[j] > items[i]:
            j = j - 1

        insertion_index = 0 if j < 0 else j + 1

        if insertion_index != i:
            items = move(items, i, insertion_index)

    return items
