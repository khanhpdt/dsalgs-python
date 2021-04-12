from src.data_structures.priority_queue import PriorityQueue


def find_largest_items(items, m):
    """
    Given n items, find m largest items, where m <= n.

    Constraints:
        - n can be a huge number

    Computational complexity: O(n*log(m))
    """

    queue = PriorityQueue.min_priority_queue()

    for item in items:
        if queue.size() < m:
            queue.insert(item)
        elif queue.peek() < item:
            queue.remove()
            queue.insert(item)

    return queue.get_all()
