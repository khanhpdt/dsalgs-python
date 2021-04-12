from src.common.has_same_items import has_same_items
from src.common.key_value import Key, KeyValue
from src.data_structures.ordered_symbol_table import OrderedSymbolTable
from tests.data_structures.symbol_table_test_common import SymbolTableTestCommon


class OrderedSymbolTableTestCommon(SymbolTableTestCommon):

    def setup_method(self):
        print("Before OrderedSymbolTableTestCommon")
        self.table: OrderedSymbolTable = None
        self.items: [KeyValue] = []

    def test_get_min_key(self):
        assert self.table.min() is None

        self.put_default_items()
        assert self.table.min().equals(Key(1))

        self.table.put(Key(0), 0)
        assert self.table.min().equals(Key(0))

    def test_get_max_key(self):
        assert self.table.max() is None

        self.put_default_items()
        assert self.table.max().equals(Key(12))

        self.table.put(Key(13), 1300)
        assert self.table.max().equals(Key(13))

    def test_floor_empty_table(self):
        assert self.table.floor(Key(3)) is None

    def test_floor_of_items_in_the_table(self):
        self.put_default_items()

        assert self.table.floor(Key(1)).equals(Key(1))
        assert self.table.floor(Key(2)).equals(Key(2))
        assert self.table.floor(Key(4)).equals(Key(4))
        assert self.table.floor(Key(8)).equals(Key(8))
        assert self.table.floor(Key(12)).equals(Key(12))

    def test_floor_of_item_smaller_than_all_the_items_in_the_table(self):
        self.put_default_items()
        assert self.table.floor(Key(0)) is None

    def test_floor_of_item_greater_than_all_the_items_in_the_table(self):
        self.put_default_items()
        assert self.table.floor(Key(14)).equals(Key(12))

    def test_floor_of_items_not_in_the_table_but_fall_in_the_middle_of_the_tables(self):
        self.put_default_items()

        assert self.table.floor(Key(3)).equals(Key(2))
        assert self.table.floor(Key(5)).equals(Key(4))
        assert self.table.floor(Key(6)).equals(Key(4))
        assert self.table.floor(Key(7)).equals(Key(4))
        assert self.table.floor(Key(9)).equals(Key(8))
        assert self.table.floor(Key(10)).equals(Key(8))
        assert self.table.floor(Key(11)).equals(Key(8))

    def test_ceiling_empty_table(self):
        assert self.table.ceiling(Key(3)) is None

    def test_ceiling_of_items_in_the_table(self):
        self.put_default_items()

        assert self.table.ceiling(Key(1)).equals(Key(1))
        assert self.table.ceiling(Key(2)).equals(Key(2))
        assert self.table.ceiling(Key(4)).equals(Key(4))
        assert self.table.ceiling(Key(8)).equals(Key(8))
        assert self.table.ceiling(Key(12)).equals(Key(12))

    def test_ceiling_of_item_smaller_than_all_the_items_in_the_table(self):
        self.put_default_items()
        assert self.table.ceiling(Key(0)).equals(Key(1))

    def test_ceiling_of_item_greater_than_all_the_items_in_the_table(self):
        self.put_default_items()
        assert self.table.ceiling(Key(14)) is None

    def test_ceiling_of_items_not_in_the_table_but_fall_in_the_middle_of_the_tables(self):
        self.put_default_items()

        assert self.table.ceiling(Key(3)).equals(Key(4))
        assert self.table.ceiling(Key(5)).equals(Key(8))
        assert self.table.ceiling(Key(6)).equals(Key(8))
        assert self.table.ceiling(Key(7)).equals(Key(8))
        assert self.table.ceiling(Key(9)).equals(Key(12))
        assert self.table.ceiling(Key(10)).equals(Key(12))
        assert self.table.ceiling(Key(11)).equals(Key(12))

    def test_rank_empty_table(self):
        assert self.table.rank(Key(2)) == 0

    def test_rank_of_items_in_the_table(self):
        self.put_default_items()

        assert self.table.rank(Key(1)) == 0
        assert self.table.rank(Key(2)) == 1
        assert self.table.rank(Key(4)) == 2
        assert self.table.rank(Key(8)) == 3
        assert self.table.rank(Key(12)) == 4

    def test_rank_of_item_smaller_than_all_items_in_the_table(self):
        self.put_default_items()
        assert self.table.rank(Key(0)) == 0

    def test_rank_of_item_greater_than_all_items_in_the_table(self):
        self.put_default_items()
        assert self.table.rank(Key(13)) == 5

    def test_rank_of_items_not_in_the_table_but_fall_in_the_middle_of_the_tables(self):
        self.put_default_items()

        assert self.table.rank(Key(3)) == 2
        assert self.table.rank(Key(5)) == 3
        assert self.table.rank(Key(6)) == 3
        assert self.table.rank(Key(7)) == 3
        assert self.table.rank(Key(9)) == 4
        assert self.table.rank(Key(10)) == 4
        assert self.table.rank(Key(11)) == 4

    def test_rank_with_put_delete_intermixed(self):
        self.put_default_items()

        assert self.table.rank(Key(14)) == 5

        self.table.put(Key(13), 1600)
        assert self.table.rank(Key(14)) == 6

        self.table.put(Key(9), 2200)
        assert self.table.rank(Key(14)) == 7

        self.table.delete(Key(8))
        assert self.table.rank(Key(14)) == 6

    def test_select_from_empty_table(self):
        assert self.table.select(0) is None

    def test_select_rank_not_in_table(self):
        self.put_default_items()
        assert self.table.select(-1) is None
        assert self.table.select(len(self.items)) is None
        assert self.table.select(len(self.items) + 1) is None

    def test_select_rank_in_table(self):
        self.put_default_items()

        assert self.table.select(0).equals(Key(1))
        assert self.table.select(1).equals(Key(2))
        assert self.table.select(2).equals(Key(4))
        assert self.table.select(3).equals(Key(8))
        assert self.table.select(4).equals(Key(12))

    def test_select_with_put_delete_intermixed(self):
        self.put_default_items()

        assert self.table.select(5) is None

        self.table.put(Key(13), 1600)
        assert self.table.select(5).equals(Key(13))

        self.table.put(Key(9), 2200)
        assert self.table.select(4).equals(Key(9))
        assert self.table.select(5).equals(Key(12))
        assert self.table.select(6).equals(Key(13))

    def test_size_of_range_without_lower_bound(self):
        assert self.table.size_of_range(high=Key(12)) == 0

        self.put_default_items()

        assert self.table.size_of_range(high=Key(12)) == 5
        assert self.table.size_of_range(high=Key(1)) == 1
        assert self.table.size_of_range(high=Key(8)) == 4

    def test_size_of_range_without_higher_bound(self):
        assert self.table.size_of_range(high=Key(12)) == 0

        self.put_default_items()

        assert self.table.size_of_range(low=Key(12)) == 1
        assert self.table.size_of_range(low=Key(2)) == 4
        assert self.table.size_of_range(low=Key(1)) == 5

    def test_size_of_range_with_same_bounds(self):
        self.put_default_items()
        assert self.table.size_of_range(low=Key(7), high=Key(7)) == 0
        assert self.table.size_of_range(low=Key(8), high=Key(8)) == 1

    def test_size_of_range_with_invalid_bounds(self):
        self.put_default_items()
        assert self.table.size_of_range(low=Key(8), high=Key(7)) == 0

    def test_size_of_range_with_bounds(self):
        assert self.table.size_of_range(low=Key(0), high=Key(10)) == 0

        self.put_default_items()

        assert self.table.size_of_range(low=Key(0), high=Key(10)) == 4
        assert self.table.size_of_range(low=Key(1), high=Key(8)) == 4
        assert self.table.size_of_range(low=Key(1), high=Key(13)) == 5
        assert self.table.size_of_range(low=Key(5), high=Key(13)) == 2
        assert self.table.size_of_range(low=Key(7), high=Key(8)) == 1

        self.table.put(Key(13), 1300)
        assert self.table.size_of_range(low=Key(5), high=Key(13)) == 3

        self.table.delete(Key(12))
        assert self.table.size_of_range(low=Key(5), high=Key(13)) == 2

    def test_range_from_empty_table(self):
        assert self.table.range() == []

    def test_range_without_bounds(self):
        self.put_default_items()

        assert has_same_items(self.table.range(), [Key(1), Key(2), Key(4), Key(8), Key(12)])

        self.table.put(Key(13), 1300)
        assert has_same_items(self.table.range(), [Key(1), Key(2), Key(4), Key(8), Key(12), Key(13)])

        self.table.delete(Key(12))
        assert has_same_items(self.table.range(), [Key(1), Key(2), Key(4), Key(8), Key(13)])

    def test_range_without_lower_bound(self):
        self.put_default_items()

        assert self.table.range(high=Key(0)) == []
        assert has_same_items(self.table.range(high=Key(12)), [Key(1), Key(2), Key(4), Key(8), Key(12)])
        assert has_same_items(self.table.range(high=Key(1)), [Key(1)])
        assert has_same_items(self.table.range(high=Key(8)), [Key(1), Key(2), Key(4), Key(8)])

    def test_range_without_higher_bound(self):
        self.put_default_items()

        assert self.table.range(low=Key(13)) == []
        assert has_same_items(self.table.range(low=Key(12)), [Key(12)])
        assert has_same_items(self.table.range(low=Key(2)), [Key(2), Key(4), Key(8), Key(12)])
        assert has_same_items(self.table.range(low=Key(1)), [Key(1), Key(2), Key(4), Key(8), Key(12)])

    def test_range_with_same_bounds(self):
        self.put_default_items()

        assert self.table.range(low=Key(7), high=Key(7)) == []
        assert has_same_items(self.table.range(low=Key(8), high=Key(8)), [Key(8)])

    def test_range_with_invalid_bounds(self):
        self.put_default_items()
        assert self.table.range(low=Key(8), high=Key(7)) == []

    def test_range_with_bounds(self):
        self.put_default_items()

        assert has_same_items(self.table.range(low=Key(0), high=Key(10)), [Key(1), Key(2), Key(4), Key(8)])
        assert has_same_items(self.table.range(low=Key(1), high=Key(8)), [Key(1), Key(2), Key(4), Key(8)])
        assert has_same_items(self.table.range(low=Key(1), high=Key(13)), [Key(1), Key(2), Key(4), Key(8), Key(12)])
        assert has_same_items(self.table.range(low=Key(5), high=Key(13)), [Key(8), Key(12)])

        self.table.put(Key(13), 1300)
        assert has_same_items(self.table.range(low=Key(5), high=Key(13)), [Key(8), Key(12), Key(13)])

        self.table.delete(Key(12))
        assert has_same_items(self.table.range(low=Key(5), high=Key(13)), [Key(8), Key(13)])
