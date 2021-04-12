import random


class SortTestCommon:

    def sort_func(self, items):
        raise RuntimeError("Not supported")

    def test_simple(self):
        assert self.sort_func([]) == []
        assert self.sort_func([1]) == [1]
        assert self.sort_func([1, 2, 3, 4]) == [1, 2, 3, 4]
        assert self.sort_func([4, 3, 2, 1]) == [1, 2, 3, 4]
        assert self.sort_func([4, 4, 4, 4]) == [4, 4, 4, 4]

    def test_many(self):
        for i in range(1, 100):
            arr = list(range(1, i + 1))
            random.shuffle(arr)
            assert self.sort_func(arr) == sorted(arr)
