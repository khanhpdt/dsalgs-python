from src.challenges.multiway_merge import multiway_merge_simple, multiway_merge


class TestMultiwayMerge:

    def test_multiway_merge_simple_small_streams(self):
        s = multiway_merge_simple(self.small_streams())
        assert s == self.expected_result_for_small_streams()

    def test_multiway_merge_small_streams(self):
        s = multiway_merge(self.small_streams())
        assert s == self.expected_result_for_small_streams()

    @staticmethod
    def small_streams():
        s1 = (i for i in [3, 20, 41])
        s2 = (i for i in [12, 14, 20, 29])
        s3 = (i for i in [21, 29, 51, 89, 199])
        return [s1, s2, s3]

    @staticmethod
    def expected_result_for_small_streams():
        return [3, 12, 14, 20, 20, 21, 29, 29, 41, 51, 89, 199]

    def test_multiway_merge_simple_big_streams(self):
        s = multiway_merge_simple(self.big_streams())
        assert s == self.expected_result_for_big_streams()

    def test_multiway_merge_big_streams(self):
        s = multiway_merge(self.big_streams())

        expected = self.expected_result_for_big_streams()
        assert s == expected

    @staticmethod
    def big_streams():
        s1 = (i * 2 for i in range(100))
        s2 = (i * 3 for i in range(100))
        s3 = (i * 4 for i in range(100))
        return [s1, s2, s3]

    @staticmethod
    def expected_result_for_big_streams():
        return sorted([i * 2 for i in range(100)] + [i * 3 for i in range(100)] + [i * 4 for i in range(100)])
