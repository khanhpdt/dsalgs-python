from src.algorithms.binary_search import binary_search


class TestBinarySearch():

    def setup_method(self):
        self.items = list(range(251))

    def test_binary_search_simple(self):
        assert binary_search([], 1) is None
        assert binary_search(list(range(1)), 0) == 0
        assert binary_search(list(range(4)), 3) == 3
        assert binary_search(list(range(4)), 4) is None

    def test_binary_search(self):
        for n in [89, 100, 110, 251]:
            assert binary_search(list(range(n)), 88) == 88
            assert binary_search(list(range(n)), 8888) is None
