from src.common.comparable import Comparable


def exchange(items, i1, i2):
    tmp = items[i1]
    items[i1] = items[i2]
    items[i2] = tmp


def list_to_str(items):
    return "[%s]" % ", ".join([str(item) for item in items])


def circular_shift_right(items, start, end):
    """
    Circular shift items from start until end to the right by one position.
    Circular here means the end item will not be removed but moved to the start position.

    For example, if items = [1, 2, 3, 4, 5], start = 1, end = 3, then result = [1, 4, 2, 3, 5].
    """
    if start > end:
        raise ValueError("Expected start <= end")

    items_copy = items.copy()
    end_item = items_copy[end]

    for i in reversed(range(start + 1, end + 1)):
        items_copy[i] = items_copy[i - 1]
    items_copy[start] = end_item

    return items_copy


def circular_shift_left(items, start, end):
    """
    Circular shift items from start until end to the left by one position.
    Circular here means the start item will not be removed but moved to the end position.

    For example, if items = [1, 2, 3, 4, 5], start = 1, end = 3, then result = [1, 3, 4, 2, 5].
    """

    if start > end:
        raise ValueError("Expected start <= end")

    items_copy = items.copy()
    start_item = items_copy[start]

    for i in range(start, end):
        items_copy[i] = items_copy[i + 1]
    items_copy[end] = start_item

    return items_copy


def move(items, from_pos, to_pos):
    """
    Move item from from_pos to to_pos and keep the relative order of the other items.
    """
    move_from_left_to_right = from_pos < to_pos
    if move_from_left_to_right:
        return circular_shift_left(items, from_pos, to_pos)
    return circular_shift_right(items, to_pos, from_pos)


def index_of_min(items):
    """
    Find index of the min item. None items are ignored in the search.

    Might return None if all items are None.
    """

    start_index = None
    for i in range(len(items)):
        if items[i] is not None:
            start_index = i
            break

    if start_index is None:
        return None

    current_min_index = start_index
    current_min = items[current_min_index]
    for i in range(len(items)):
        if items[i] is not None and items[i] < current_min:
            current_min_index = i
            current_min = items[i]

    return current_min_index


def index_of(items, item):
    """
    Find index of the given item in the given list.

    :return: None if not found
    """

    for i in range(len(items)):
        if eq(items[i], item):
            return i
    return None


def compare(o1, o2):
    if o1 is None and o2 is None:
        return True

    if type(o1) != type(o2):
        raise ValueError("Not comparable")

    if isinstance(o1, Comparable) and isinstance(o2, Comparable):
        return o1.compare_to(o2)

    if type(o1) not in (int, float, str):
        raise ValueError("Not comparable")

    if o1 > o2:
        return 1
    if o1 == o2:
        return 0
    return -1


def lt_or_eq(o1, o2):
    return compare(o1, o2) <= 0


def lt(o1, o2):
    return compare(o1, o2) < 0


def gt_or_eq(o1, o2):
    return compare(o1, o2) >= 0


def gt(o1, o2):
    return compare(o1, o2) > 0


def eq(o1, o2):
    if o1 is None and o2 is None:
        return True

    if type(o1) != type(o2):
        return False

    if isinstance(o1, Comparable) and isinstance(o2, Comparable):
        return o1.equals(o2)

    if type(o1) not in (int, float, str):
        raise ValueError("Not comparable")

    return o1 == o2


def shift_right(items, start):
    """
    Shift items from the given index start to the right by one position.
    The item at the index start will be assigned None.

    Example: if items = [1, 2, 3, 4] and start = 1, then items will be [1, None, 2, 3, 4].
    """

    if start < 0 or start >= len(items):
        return items

    items.append(items[-1])
    for i in range(len(items) - 2, start, -1):
        items[i] = items[i - 1]
    items[start] = None
