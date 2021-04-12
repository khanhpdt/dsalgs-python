from src.common.utils import eq
from src.algorithms.sorting.quick_sort import quick_sort


def has_same_items(l1, l2):
    """
    This implementation takes O(n*log(n)) time mainly for sorting the two lists before comparing their items.

    Another implementation would be to loop over the first list, build a hash table from that list, and then
    loop over the second list to check if any item not in the hash table. Note that we also need to keep track of
    the item count to handle duplicated items. This implementation takes O(n) time.
    """

    if len(l1) != len(l2):
        return False

    sorted_l1 = quick_sort(l1)
    sorted_l2 = quick_sort(l2)

    for i in range(len(sorted_l1)):
        if not eq(sorted_l1[i], sorted_l2[i]):
            return False
    return True
