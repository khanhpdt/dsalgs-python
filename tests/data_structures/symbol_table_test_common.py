from src.common.key_value import Key, KeyValue
from src.data_structures.symbol_table import SymbolTable


class SymbolTableTestCommon:

    def setup_method(self):
        self.table: SymbolTable = None
        self.items: [KeyValue] = []

    def test_get_from_empty_table(self):
        assert self.table.get(Key(1)) is None

    def test_get_not_exist(self):
        self.table.put(Key(1), 1)
        assert self.table.get(Key(2)) is None

    def test_put_replace_existing(self):
        self.put_default_items()

        key = self.key(1)
        new_value = 1000000
        assert self.table.get(key) != new_value
        size_before = self.table.size()

        self.table.put(key, new_value)

        assert self.table.get(key) == new_value
        assert self.table.size() == size_before

    def test_put_and_get_sequential(self):
        self.put_default_items()

        for i in range(len(self.items)):
            assert self.table.get(self.key(i)) == self.value(i)

    def put_default_items(self):
        self.items = self.default_items()
        for i in range(len(self.items)):
            self.table.put(self.key(i), self.value(i))

    @staticmethod
    def default_items():
        keys = [Key(1), Key(4), Key(2), Key(8), Key(12)]
        values = [100, 400, 200, 800, 1200]

        items = []
        for i in range(len(keys)):
            items.append(KeyValue(keys[i], values[i]))
        return items

    def key(self, i):
        return self.items[i].key

    def value(self, i):
        return self.items[i].value

    def test_delete_items_in_the_table(self):
        self.put_default_items()

        for i in range(len(self.items)):
            assert self.table.get(self.key(i)) == self.value(i)
            self.table.delete(self.key(i))
            assert self.table.get(self.key(i)) is None

    def test_delete_items_not_in_the_table(self):
        self.put_default_items()
        size_before = self.table.size()

        self.table.delete(Key(1111))
        assert self.table.size() == size_before

    def test_put_get_intermixed(self):
        for i in range(len(self.items)):
            self.table.put(self.key(i), self.value(i))
            assert self.table.get(self.key(i)) == self.value(i)

    def test_put_get_delete_intermixed(self):
        for i in range(len(self.items)):
            self.table.put(self.key(i), self.value(i))
            assert self.table.get(self.key(i)) == self.value(i)

            self.table.delete(self.key(i))
            assert self.table.get(self.key(i)) is None

    def test_contains(self):
        assert not self.table.contains(Key(1))

        self.put_default_items()

        for i in range(len(self.items)):
            assert self.table.contains(self.key(i))

    def test_check_empty(self):
        assert self.table.is_empty()

        self.put_default_items()
        assert not self.table.is_empty()

    def test_size_of_empty_table(self):
        assert self.table.size() == 0

    def test_size_with_put_delete_intermixed(self):
        self.put_default_items()

        assert self.table.size() == 5

        self.table.put(Key(13), 1300)
        assert self.table.size() == 6

        self.table.delete(Key(12))
        assert self.table.size() == 5
