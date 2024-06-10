from pynary import BinaryArray as b
import random
from constants import LARGE_NUM, SMALL_NUM, MED_NUM


class TestBasicOperations:
    def setup_method(self, method):
        random.seed(42)

    # -----------------------------------------------------------------
    # Test constructor and subscript functions
    # -----------------------------------------------------------------

    def test_array_init_all_false(self):
        test_arr = [0 for _ in range(SMALL_NUM)]
        bin_arr = b(test_arr)

        for i, x in enumerate(test_arr):
            assert bin_arr[i] == x

    def test_array_init_all_true(self):
        test_arr = [1 for _ in range(SMALL_NUM)]
        bin_arr = b(test_arr)

        for i, x in enumerate(test_arr):
            assert bin_arr[i] == x

    def test_array_init_random_values(self):
        test_arr = [random.randint(0, 1) for _ in range(LARGE_NUM)]
        bin_arr = b(test_arr)

        for i, x in enumerate(test_arr):
            assert bin_arr[i] == x

    # -----------------------------------------------------------------
    # Test assignment operations
    # -----------------------------------------------------------------

    def test_array_assign_0_to_0(self):
        test_arr = [0]
        bin_arr = b(test_arr)

        bin_arr[0] = 0
        assert bin_arr[0] == 0

    def test_array_assign_0_to_1(self):
        test_arr = [0]
        bin_arr = b(test_arr)

        bin_arr[0] = 1
        assert bin_arr[0] == 1

    def test_array_assign_1_to_0(self):
        test_arr = [1]
        bin_arr = b(test_arr)

        bin_arr[0] = 0
        assert bin_arr[0] == 0

    def test_array_assign_1_to_1(self):
        test_arr = [1]
        bin_arr = b(test_arr)

        bin_arr[0] = 1
        assert bin_arr[0] == 1

    # -----------------------------------------------------------------
    # Test to string function
    # -----------------------------------------------------------------

    def test_to_string_all_0(self):
        test_arr = [0 for _ in range(SMALL_NUM)]
        bin_arr = b(test_arr)

        assert str(bin_arr) == str(test_arr)

    def test_to_string_all_1(self):
        test_arr = [1 for _ in range(SMALL_NUM)]
        bin_arr = b(test_arr)

        assert str(bin_arr) == str(test_arr)

    def test_to_string_random(self):
        test_arr = [random.randint(0, 1) for _ in range(LARGE_NUM)]
        bin_arr = b(test_arr)

        assert str(bin_arr) == str(test_arr)

    # -----------------------------------------------------------------
    # Test equality validity
    # -----------------------------------------------------------------

    def test_equal_differing_len(self):
        test_arr = [0 for _ in range(SMALL_NUM)]
        bin_arr = b(test_arr)
        test_arr.append(0)
        bin_arr_2 = b(test_arr)

        assert bin_arr == bin_arr
        assert bin_arr_2 == bin_arr_2
        assert bin_arr != bin_arr_2

    def test_equal_differing_single_value(self):
        test_arr = [0 for _ in range(SMALL_NUM)]
        bin_arr = b(test_arr)
        test_arr[1] = 1
        bin_arr_2 = b(test_arr)

        assert bin_arr == bin_arr
        assert bin_arr_2 == bin_arr_2
        assert bin_arr != bin_arr_2

    def test_equal_random_values(self):
        test_arr = [random.randint(0, 1) for _ in range(LARGE_NUM)]
        bin_arr = b(test_arr)
        test_arr = [random.randint(0, 1) for _ in range(LARGE_NUM)]
        bin_arr_2 = b(test_arr)

        assert bin_arr == bin_arr
        assert bin_arr_2 == bin_arr_2
        assert bin_arr != bin_arr_2

    # -----------------------------------------------------------------
    # Test length
    # -----------------------------------------------------------------

    def test_len_function(self):
        test_arrays = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(MED_NUM)],
            [random.randint(0, 1) for _ in range(LARGE_NUM)],
        ]
        bin_arrays = [b(t) for t in test_arrays]

        for bin_arr, test_arr in zip(bin_arrays, test_arrays):
            assert len(bin_arr) == len(test_arr)

    # -----------------------------------------------------------------
    # Test less than
    # -----------------------------------------------------------------

    def test_lt_self(self):
        t_arr = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]

        b_arr = [b(t) for t in t_arr]

        for bin_arr in b_arr:
            assert not (b_arr < b_arr)

    def test_lt_true(self):
        t_arr = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]

        b_arr = [b(t) for t in t_arr]

        assert b_arr[0] < b_arr[1]
        assert b_arr[0] < b_arr[2]
        assert b_arr[2] < b_arr[1]

    def test_lt_false(self):
        t_arr = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]

        b_arr = [b(t) for t in t_arr]

        assert not (b_arr[1] < b_arr[0])
        assert not (b_arr[2] < b_arr[0])
        assert not (b_arr[1] < b_arr[2])

    # -----------------------------------------------------------------
    # Test greater than
    # -----------------------------------------------------------------

    def test_gt_self(self):
        t_arr = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]

        b_arr = [b(t) for t in t_arr]

        for bin_arr in b_arr:
            assert not (b_arr > b_arr)

    def test_gt_true(self):
        t_arr = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]

        b_arr = [b(t) for t in t_arr]

        assert b_arr[1] > b_arr[0]
        assert b_arr[2] > b_arr[0]
        assert b_arr[1] > b_arr[2]

    def test_gt_false(self):
        t_arr = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]

        b_arr = [b(t) for t in t_arr]

        assert not (b_arr[0] > b_arr[1])
        assert not (b_arr[0] > b_arr[2])
        assert not (b_arr[2] > b_arr[1])

    # -----------------------------------------------------------------
    # Test less than
    # -----------------------------------------------------------------

    def test_le_self(self):
        t_arr = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]

        b_arr = [b(t) for t in t_arr]

        for bin_arr in b_arr:
            assert b_arr <= b_arr

    def test_le_true(self):
        t_arr = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]

        b_arr = [b(t) for t in t_arr]

        assert b_arr[0] <= b_arr[1]
        assert b_arr[0] <= b_arr[2]
        assert b_arr[2] <= b_arr[1]

    def test_le_false(self):
        t_arr = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]

        b_arr = [b(t) for t in t_arr]

        assert not (b_arr[1] <= b_arr[0])
        assert not (b_arr[2] <= b_arr[0])
        assert not (b_arr[1] <= b_arr[2])

    # -----------------------------------------------------------------
    # Test greater than or equal to
    # -----------------------------------------------------------------

    def test_ge_self(self):
        t_arr = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]

        b_arr = [b(t) for t in t_arr]

        for bin_arr in b_arr:
            assert b_arr >= b_arr

    def test_ge_true(self):
        t_arr = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]

        b_arr = [b(t) for t in t_arr]

        assert b_arr[1] >= b_arr[0]
        assert b_arr[2] >= b_arr[0]
        assert b_arr[1] >= b_arr[2]

    def test_ge_false(self):
        t_arr = [
            [0 for _ in range(SMALL_NUM)],
            [1 for _ in range(SMALL_NUM)],
            [random.randint(0, 1) for _ in range(SMALL_NUM)],
        ]

        b_arr = [b(t) for t in t_arr]

        assert not (b_arr[0] >= b_arr[1])
        assert not (b_arr[0] >= b_arr[2])
        assert not (b_arr[2] >= b_arr[1])
