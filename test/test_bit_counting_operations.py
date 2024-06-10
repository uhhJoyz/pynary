from pynary import BinaryArray as b
import random
from constants import LARGE_NUM, MED_NUM, SMALL_NUM


class TestBitCountingOperations:
    def setup_method(self, method):
        random.seed(42)

    def test_bit_count_small(self):
        test_arrays = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]
        binary_arrays = [b(t) for t in test_arrays]

        for i, binarr in enumerate(binary_arrays):
            assert binarr.count_ones() == sum(test_arrays[i])

    def test_bit_count_medium(self):
        test_arrays = [
            [0 for _ in range(MED_NUM)],
            [1 for _ in range(MED_NUM)],
            [random.randint(0, 1) for _ in range(MED_NUM)],
        ]
        binary_arrays = [b(t) for t in test_arrays]

        for i, binarr in enumerate(binary_arrays):
            assert binarr.count_ones() == sum(test_arrays[i])

    def test_find_zero(self):
        test_arrays = [
            [0 for _ in range(MED_NUM)],
            [1 for _ in range(MED_NUM)],
            [random.randint(0, 1) for _ in range(MED_NUM)],
        ]
        binary_arrays = [b(t) for t in test_arrays]

        assert binary_arrays[0].find_first_zero() == 0
        assert binary_arrays[1].find_first_zero() == -1

        for i, x in enumerate(test_arrays[2]):
            if x == 0:
                assert binary_arrays[2].find_first_zero() == i
                break
