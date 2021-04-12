import random

from src.challenges.find_largest_items import find_largest_items
from src.common.has_same_items import has_same_items


class TestFindLargestItems:

    def test_find_largest_items(self):
        items = list(range(100))
        random.shuffle(items)

        largest_items = find_largest_items(items, 10)

        assert has_same_items(largest_items, list(range(90, 100)))
