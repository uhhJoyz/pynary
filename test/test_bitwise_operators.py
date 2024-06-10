from pynary import BinaryArray as b
import random
from constants import LARGE_NUM, MED_NUM, SMALL_NUM


class TestBitwiseOperations:
    def setup_method(self, method):
        random.seed(42)

    # -----------------------------------------------------------------
    # Test bitwise and operator
    # -----------------------------------------------------------------

    def test_bitwise_and_small_0(self):
        test_arr = [0 for _ in range(SMALL_NUM)]
        bin_arr = b(test_arr)
        bin_arr_2 = b(test_arr)
        bin_arr_2.bit_and(bin_arr)

        assert bin_arr == bin_arr_2

    def test_bitwise_and_small_1(self):
        test_arr = [1 for _ in range(SMALL_NUM)]
        bin_arr = b(test_arr)
        bin_arr_2 = b(test_arr)
        bin_arr_2.bit_and(bin_arr)

        assert bin_arr == bin_arr_2

    def test_bitwise_and_small_self_random(self):
        test_arr = [random.randint(0, 1) for _ in range(SMALL_NUM)]
        bin_arr = b(test_arr)
        bin_arr_2 = b(test_arr)
        bin_arr_2.bit_and(bin_arr)

        assert bin_arr == bin_arr_2

    def test_bitwise_and_neq_0_1(self):
        zero_arr = [0 for _ in range(SMALL_NUM)]
        one_arr = [1 for _ in range(SMALL_NUM)]
        bin_arr = b(one_arr)
        bin_arr.bit_and(b(zero_arr))

        assert bin_arr == b(zero_arr)
        assert bin_arr != b(one_arr)

    def test_bitwise_and_zero_random(self):
        zero_arr = [0 for _ in range(SMALL_NUM)]
        one_arr = [random.randint(0, 1) for _ in range(SMALL_NUM)]
        bin_arr = b(one_arr)
        bin_arr.bit_and(b(zero_arr))

        assert bin_arr == b(zero_arr)
        assert bin_arr != b(one_arr)

    def test_bitwise_and_two_random(self):
        t1 = [random.randint(0, 1) for _ in range(SMALL_NUM)]
        t2 = [random.randint(0, 1) for _ in range(SMALL_NUM)]
        and_arr = [x & y for (x, y) in zip(t1, t2)]
        bin_arr = b(t1)
        bin_arr.bit_and(b(t2))

        assert bin_arr == b(and_arr)

    def test_bitwise_and_two_random_large(self):
        t1 = [random.randint(0, 1) for _ in range(LARGE_NUM)]
        t2 = [random.randint(0, 1) for _ in range(LARGE_NUM)]
        and_arr = [x & y for (x, y) in zip(t1, t2)]
        bin_arr = b(t1)
        bin_arr.bit_and(b(t2))

        assert bin_arr == b(and_arr)

    # -----------------------------------------------------------------
    # Test bitwise or operator
    # -----------------------------------------------------------------

    def test_bitwise_or_small_0(self):
        test_arr = [0 for _ in range(SMALL_NUM)]
        bin_arr = b(test_arr)
        bin_arr_2 = b(test_arr)
        bin_arr_2.bit_or(bin_arr)

        assert bin_arr == bin_arr_2

    def test_bitwise_or_small_1(self):
        test_arr = [1 for _ in range(SMALL_NUM)]
        bin_arr = b(test_arr)
        bin_arr.bit_or(b(test_arr))

        assert bin_arr == b(test_arr)

    def test_bitwise_or_small_0_1(self):
        t1 = [1 for _ in range(SMALL_NUM)]
        t2 = [0 for _ in range(SMALL_NUM)]

        bin_arr = b(t1)
        bin_arr.bit_or(b(t2))

        assert bin_arr == b(t1)
        assert bin_arr != b(t2)

    def test_bitwise_or_random_identity(self):
        t1 = [random.randint(0, 1) for _ in range(SMALL_NUM)]
        t2 = [0 for _ in range(SMALL_NUM)]

        bin_arr = b(t1)
        bin_arr.bit_or(b(t2))

        assert bin_arr == b(t1)

    def test_bitwise_or_random_fill(self):
        t1 = [random.randint(0, 1) for _ in range(SMALL_NUM)]
        t2 = [1 for _ in range(SMALL_NUM)]

        bin_arr = b(t1)
        bin_arr.bit_or(b(t2))

        assert bin_arr == b(t2)
        assert bin_arr != b(t1)

    def test_bitwise_or_random(self):
        t1 = [random.randint(0, 1) for _ in range(SMALL_NUM)]
        t2 = [1 for _ in range(SMALL_NUM)]
        or_arr = [x | y for (x, y) in zip(t1, t2)]

        bin_arr = b(t1)
        bin_arr.bit_or(b(t2))

        assert bin_arr == b(or_arr)

    def test_bitwise_or_random_large(self):
        t1 = [random.randint(0, 1) for _ in range(LARGE_NUM)]
        t2 = [1 for _ in range(LARGE_NUM)]
        or_arr = [x | y for (x, y) in zip(t1, t2)]

        bin_arr = b(t1)
        bin_arr.bit_or(b(t2))

        assert bin_arr == b(or_arr)

    # -----------------------------------------------------------------
    # Test bitwise xor operator
    # -----------------------------------------------------------------

    def test_bitwise_xor_small_0(self):
        test_arr = [0 for _ in range(SMALL_NUM)]
        bin_arr = b(test_arr)
        bin_arr_2 = b(test_arr)
        bin_arr_2.bit_xor(bin_arr)

        assert bin_arr == bin_arr_2

    def test_bitwise_xor_small_1(self):
        test_arr = [1 for _ in range(SMALL_NUM)]
        zero_arr = [0 for _ in range(SMALL_NUM)]
        bin_arr = b(test_arr)
        bin_arr.bit_xor(b(test_arr))

        assert bin_arr == b(zero_arr)

    def test_bitwise_xor_small_0_1(self):
        t1 = [1 for _ in range(SMALL_NUM)]
        t2 = [0 for _ in range(SMALL_NUM)]

        bin_arr = b(t1)
        bin_arr.bit_xor(b(t2))

        assert bin_arr == b(t1)
        assert bin_arr != b(t2)

    def test_bitwise_xor_random_identity(self):
        t1 = [random.randint(0, 1) for _ in range(SMALL_NUM)]
        t2 = [0 for _ in range(SMALL_NUM)]

        bin_arr = b(t1)
        bin_arr.bit_xor(b(t2))

        assert bin_arr == b(t1)

    def test_bitwise_xor_random_fill(self):
        t1 = [random.randint(0, 1) for _ in range(SMALL_NUM)]
        t2 = [1 for _ in range(SMALL_NUM)]
        t3 = [abs(x - 1) for x in t1]

        bin_arr = b(t1)
        bin_arr.bit_xor(b(t2))

        assert bin_arr == b(t3)
        assert bin_arr != b(t1)

    def test_bitwise_xor_random(self):
        t1 = [random.randint(0, 1) for _ in range(SMALL_NUM)]
        t2 = [1 for _ in range(SMALL_NUM)]
        t3 = [abs(x - 1) for x in t1]

        bin_arr = b(t1)
        bin_arr.bit_xor(b(t2))

        assert bin_arr == b(t3)

    def test_bitwise_xor_random_large(self):
        t1 = [random.randint(0, 1) for _ in range(LARGE_NUM)]
        t2 = [1 for _ in range(LARGE_NUM)]
        t3 = [abs(x - 1) for x in t1]

        bin_arr = b(t1)
        bin_arr.bit_xor(b(t2))

        assert bin_arr == b(t3)

    # -----------------------------------------------------------------
    # Test bitwise not operator
    # -----------------------------------------------------------------

    def test_bitwise_not_0(self):
        t1 = [0 for _ in range(SMALL_NUM)]
        t2 = [1 for _ in range(SMALL_NUM)]
        bin_arr = b(t1)
        bin_arr.bit_not()

        assert bin_arr == b(t2)

    def test_bitwise_not_1(self):
        t1 = [0 for _ in range(SMALL_NUM)]
        t2 = [1 for _ in range(SMALL_NUM)]
        bin_arr = b(t2)
        bin_arr.bit_not()

        assert bin_arr == b(t1)

    def test_bitwise_not_random(self):
        t1 = [random.randint(0, 1) for _ in range(SMALL_NUM)]
        t2 = [abs(x - 1) for x in t1]
        bin_arr = b(t1)
        bin_arr.bit_not()

        assert bin_arr == b(t2)

    def test_bitwise_not_random_large(self):
        t1 = [random.randint(0, 1) for _ in range(LARGE_NUM)]
        t2 = [abs(x - 1) for x in t1]
        bin_arr = b(t1)
        bin_arr.bit_not()

        assert bin_arr == b(t2)
