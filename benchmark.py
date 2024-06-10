from pynary import BinaryArray as b
import random
from timeit import timeit
from constants import SMALL_NUM, LARGE_NUM, MED_NUM, NUM_TESTS


# helper functions to print performance metrics from the benchmark
def print_performance(perf, iters=MED_NUM):
    print(f"Over {iters} iterations")
    print(f"Library average execution time: {perf[0] / iters} seconds")
    print(f"Python average execution time: {perf[1] / iters} seconds")
    print(f"Library speed proportion {perf[2]}")


def benchmark_overhead():
    time_overhead_lib = timeit(
        "arr = [random.randint(0,1) for _ in range(MED_NUM)]\n" + "bin_arr = b(arr)",
        setup="from pynary import BinaryArray as b\n"
        + "import random\n"
        + "random.seed(42)\n"
        + "from constants import MED_NUM\n",
        number=NUM_TESTS,
    )
    time_overhead_python = timeit(
        "ans = [bool(random.randint(0,1)) for _ in range(MED_NUM)]",
        setup="from constants import MED_NUM\n"
        + "import random\n"
        + "random.seed(42)\n",
        number=NUM_TESTS,
    )

    return [
        time_overhead_lib,
        time_overhead_python,
        time_overhead_python / time_overhead_lib,
    ]


def benchmark_equals():
    time_equal_lib = timeit(
        "ans = b1 == b2",
        setup="from pynary import BinaryArray as b\n"
        + "import random\n"
        + "random.seed(42)\n"
        + "from constants import MED_NUM\n"
        + "arr = [random.randint(0,1) for _ in range(MED_NUM)]\n"
        + "b1 = b(arr)\n"
        + "b2 = b(arr)",
        number=NUM_TESTS,
    )
    time_equal_python = timeit(
        "ans = e1 == e2",
        setup="from constants import MED_NUM\n"
        + "import random\n"
        + "random.seed(42)\n"
        + "e1 = [bool(random.randint(0,1)) for _ in range(MED_NUM)]\n"
        + "e2 = e1.copy()",
        number=NUM_TESTS,
    )

    return [
        time_equal_python,
        time_equal_python,
        time_equal_python / time_equal_lib,
    ]


def benchmark_one_count():
    time_bitwise_one_count_lib = timeit(
        "b1.count_ones()",
        setup="from pynary import BinaryArray as b\n"
        + "import random\n"
        + "random.seed(42)\n"
        + "from constants import MED_NUM\n"
        + "b1 = b([random.randint(0,1) for _ in range(MED_NUM)])",
        number=NUM_TESTS,
    )
    time_bitwise_one_count_python = timeit(
        "sum([int(a) for a in e1])",
        setup="from constants import MED_NUM\n"
        + "import random\n"
        + "random.seed(42)\n"
        + "e1 = [bool(random.randint(0,1)) for _ in range(MED_NUM)]",
        number=NUM_TESTS,
    )

    return [
        time_bitwise_one_count_lib,
        time_bitwise_one_count_python,
        time_bitwise_one_count_python / time_bitwise_one_count_lib,
    ]


def benchmark_bitwise_or():
    time_bitwise_or_lib = timeit(
        "b1.bit_or(b2)",
        setup="from pynary import BinaryArray as b\n"
        + "import random\n"
        + "random.seed(42)\n"
        + "from constants import MED_NUM\n"
        + "b1 = b([random.randint(0,1) for _ in range(MED_NUM)])\n"
        + "b2=b([random.randint(0,1) for _ in range(MED_NUM)])",
        number=NUM_TESTS,
    )
    time_bitwise_or_python = timeit(
        "[a or b for a, b in zip(e1, e2)]",
        setup="from constants import MED_NUM\n"
        + "import random\n"
        + "random.seed(42)\n"
        + "e1 = [bool(random.randint(0,1)) for _ in range(MED_NUM)]\n"
        + "e2=[bool(random.randint(0,1)) for _ in range(MED_NUM)]",
        number=NUM_TESTS,
    )

    return [
        time_bitwise_or_lib,
        time_bitwise_or_python,
        time_bitwise_or_python / time_bitwise_or_lib,
    ]


def benchmark_bitwise_and():
    time_bitwise_and_lib = timeit(
        "b1.bit_and(b2)",
        setup="from pynary import BinaryArray as b\n"
        + "import random\n"
        + "random.seed(42)\n"
        + "from constants import MED_NUM\n"
        + "b1 = b([random.randint(0,1) for _ in range(MED_NUM)])\n"
        + "b2=b([random.randint(0,1) for _ in range(MED_NUM)])",
        number=NUM_TESTS,
    )
    time_bitwise_and_python = timeit(
        "[a and b for a, b in zip(e1, e2)]",
        setup="from constants import MED_NUM\n"
        + "import random\n"
        + "random.seed(42)\n"
        + "e1 = [bool(random.randint(0,1)) for _ in range(MED_NUM)]\n"
        + "e2=[bool(random.randint(0,1)) for _ in range(MED_NUM)]",
        number=NUM_TESTS,
    )

    return [
        time_bitwise_and_lib,
        time_bitwise_and_python,
        time_bitwise_and_python / time_bitwise_and_lib,
    ]


def benchmark_bitwise_xor():
    time_bitwise_xor_lib = timeit(
        "b1.bit_xor(b2)",
        setup="from pynary import BinaryArray as b\n"
        + "import random\n"
        + "random.seed(42)\n"
        + "from constants import MED_NUM\n"
        + "b1 = b([random.randint(0,1) for _ in range(MED_NUM)])\n"
        + "b2=b([random.randint(0,1) for _ in range(MED_NUM)])",
        number=NUM_TESTS,
    )
    time_bitwise_xor_python = timeit(
        "[a ^ b for a, b in zip(e1, e2)]",
        setup="from constants import MED_NUM\n"
        + "import random\n"
        + "random.seed(42)\n"
        + "e1 = [bool(random.randint(0,1)) for _ in range(MED_NUM)]\n"
        + "e2=[bool(random.randint(0,1)) for _ in range(MED_NUM)]",
        number=NUM_TESTS,
    )

    return [
        time_bitwise_xor_lib,
        time_bitwise_xor_python,
        time_bitwise_xor_python / time_bitwise_xor_lib,
    ]


def benchmark_bitwise_not():
    time_bitwise_not_lib = timeit(
        "bin_arr.bit_not()",
        setup="from pynary import BinaryArray as b\n"
        + "from constants import MED_NUM\n"
        + "bin_arr = b([0 for _ in range(MED_NUM)])",
        number=NUM_TESTS,
    )
    time_bitwise_not_python = timeit(
        "[not a for a in example]",
        setup="from constants import MED_NUM\n"
        + "example = [False for _ in range(MED_NUM)]",
        number=NUM_TESTS,
    )

    return [
        time_bitwise_not_lib,
        time_bitwise_not_python,
        time_bitwise_not_python / time_bitwise_not_lib,
    ]


if __name__ == "__main__":
    # benchmark each function
    not_data = benchmark_bitwise_not()
    xor_data = benchmark_bitwise_xor()
    and_data = benchmark_bitwise_and()
    or_data = benchmark_bitwise_or()
    one_count_data = benchmark_one_count()
    equals_data = benchmark_equals()
    overhead_data = benchmark_overhead()

    # print benchmarks
    print("NOT Benchmark")
    print_performance(not_data)
    print()

    print("XOR Benchmark")
    print_performance(xor_data)
    print()

    print("AND Benchmark")
    print_performance(and_data)
    print()

    print("OR Benchmark")
    print_performance(or_data)
    print()

    print("One Count Benchmark")
    print_performance(one_count_data)
    print()

    print("== Benchmark")
    print_performance(equals_data)
    print()

    print("Overhead Benchmark")
    print_performance(overhead_data)
    print()
