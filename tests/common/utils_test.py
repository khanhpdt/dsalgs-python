import random

from src.common import utils
from src.common.has_same_items import has_same_items
from src.common.key_value import KeyValue, Key
from src.common.utils import index_of_min, compare, eq, index_of, shift_right


class TestUtils(object):

    def test_circular_shift_right(self):
        assert utils.circular_shift_right([1, 2, 3, 4, 5], 1, 3) == [1, 4, 2, 3, 5]
        assert utils.circular_shift_right([1, 2, 3, 4, 5], 0, 4) == [5, 1, 2, 3, 4]

    def test_circular_shift_left(self):
        assert utils.circular_shift_left([1, 2, 3, 4, 5], 1, 3) == [1, 3, 4, 2, 5]
        assert utils.circular_shift_left([1, 2, 3, 4, 5], 0, 4) == [2, 3, 4, 5, 1]

    def test_move_from_left_to_right(self):
        assert utils.move([1, 2, 3, 4, 5], 0, 4) == [2, 3, 4, 5, 1]
        assert utils.move([1, 2, 3, 4, 5], 1, 3) == [1, 3, 4, 2, 5]

    def test_move_same(self):
        assert utils.move([1, 2, 3, 4, 5], 3, 3) == [1, 2, 3, 4, 5]

    def test_move_from_right_to_left(self):
        assert utils.move([1, 2, 3, 4, 5], 2, 0) == [3, 1, 2, 4, 5]
        assert utils.move([1, 2, 3, 4, 5], 3, 1) == [1, 4, 2, 3, 5]

    def test_list_to_str(self):
        assert utils.list_to_str([]) == "[]"
        assert utils.list_to_str([1, 2, 3]) == "[1, 2, 3]"

    def test_check_lists_contain_same_items(self):
        assert has_same_items([], [])
        assert has_same_items([1, 2, 3], [3, 1, 2])
        assert not has_same_items([], [1])
        assert not has_same_items([1, 2], [3, 1, 2])

        items = list(range(100))
        list1 = items.copy()
        random.shuffle(list1)
        list2 = items.copy()
        random.shuffle(list2)
        assert has_same_items(list1, list2)

    def test_find_index_of_min(self):
        assert index_of_min([3, 1, 2]) == 1
        assert index_of_min([3, None, 2]) == 2
        assert index_of_min([3, None, None]) == 0
        assert index_of_min([None, None, None]) is None

        items = list(range(100))
        random.shuffle(items)
        assert index_of_min(items) == items.index(0)

    def test_find_index_of_item(self):
        assert index_of([3, 1, 2], 3) == 0
        assert index_of([3, 1, 2], 1) == 1
        assert index_of([3, None, 2], None) == 1
        assert index_of([3, None, 2], 2) == 2

        items = list(range(100))
        random.shuffle(items)
        assert index_of(items, 44) == items.index(44)

        assert index_of([KeyValue(Key(1)), KeyValue(Key(4)), KeyValue(Key(2))], KeyValue(Key(4))) == 1

    def test_compare_primitives(self):
        assert compare(1, 2) == -1
        assert compare(2, 2) == 0
        assert compare(2, 1) == 1

        assert compare(1.1, 1.2) == -1
        assert compare(2.1, 1.9) == 1
        assert compare(2.1, 2.1) == 0

        assert compare(KeyValue(1), KeyValue(2)) == -1
        assert compare(KeyValue(2), KeyValue(2)) == 0
        assert compare(KeyValue(2), KeyValue(1)) == 1

    def test_check_equals(self):
        assert eq(None, None)

        assert not eq(1, 2)
        assert eq(2, 2)
        assert not eq(2, 1)

        assert not eq(1.1, 1.2)
        assert not eq(2.1, 1.9)
        assert eq(2.1, 2.1)

        assert not eq(KeyValue(1), KeyValue(2))
        assert eq(KeyValue(2), KeyValue(2))
        assert not eq(KeyValue(2), KeyValue(1))

        assert not eq(KeyValue(Key(1)), KeyValue(Key(2)))
        assert eq(KeyValue(Key(2)), KeyValue(Key(2)))
        assert not eq(KeyValue(Key(2)), KeyValue(Key(1)))

    def test_shift_right(self):
        self.assert_shift_right([1, 2, 3, 4], 0, [None, 1, 2, 3, 4])
        self.assert_shift_right([1, 2, 3, 4], 1, [1, None, 2, 3, 4])
        self.assert_shift_right([1, 2, 3, 4], 3, [1, 2, 3, None, 4])
        self.assert_shift_right([], 1, [])
        self.assert_shift_right([1, 2, 3, 4], 4, [1, 2, 3, 4])
        self.assert_shift_right([1, 2, 3, 4], -1, [1, 2, 3, 4])

    @staticmethod
    def assert_shift_right(items, start, expected_items):
        items_copy = items.copy()
        shift_right(items_copy, start)
        assert items_copy == expected_items
