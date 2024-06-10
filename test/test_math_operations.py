from pynary import BinaryArray as b
import random
from constants import LARGE_NUM, SMALL_NUM, MED_NUM


class TestMathOperations:
    def setup_method(self, method):
        random.seed(42)

    # -----------------------------------------------------------------
    # Test constructor and subscript functions
    # -----------------------------------------------------------------

    def test_sub_self(self):
        test_arrays = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]
        binary_arrays = [b(t) for t in test_arrays]

        for bin_arr in binary_arrays:
            assert bin_arr - bin_arr == 0

    def test_sub_other(self):
        test_arrays = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]
        test_answers = [
            [sum([(c - d) for (c, d) in zip(x, y)]) for x in test_arrays]
            for y in test_arrays
        ]
        binary_arrays = [b(t) for t in test_arrays]
        binary_answers = [[x - y for x in binary_arrays] for y in binary_arrays]

        for b_ans, t_ans in zip(binary_answers, test_answers):
            assert b_ans == t_ans
