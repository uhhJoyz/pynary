import pprint
from binary_storage_lib import BinaryArray as b
import random
from test.constants import LARGE_NUM, MED_NUM, SMALL_NUM

if __name__ == "__main__":
    test_arrays = [
        [0 for _ in range(MED_NUM)],
        [1 for _ in range(MED_NUM)],
        [random.randint(0, 1) for _ in range(MED_NUM)],
    ]
    binary_arrays = [b(t) for t in test_arrays]
    print(len(binary_arrays[1]))
    print(len(test_arrays[1]))
    # pprint.pp(test_arrays[1])
    for i in range(12):
        print(f"index: {i}, {test_arrays[1][i]}")

    for i, x in enumerate(test_arrays[1]):
        if x != 0:
            print(i)
            break

    assert binary_arrays[0].find_first_zero() == 0
    print(binary_arrays[1].find_first_zero())

    for i, x in enumerate(test_arrays[2]):
        if x == 0:
            print(i)
            # assert binary_arrays[2].find_first_zero() == i
            break
