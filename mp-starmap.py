import multiprocessing as mp
import time
from asyncMtMpHelper import *


def add_numbers(*args) -> int:
    print(f"Adding: {args}")
    time.sleep(2)
    return sum(args)


@get_time
def main():
    print(f"Cores available: {mp.cpu_count()}")
    """
    starmap() is similar to map() but it takes an iterable of iterables as input.
    It will then unpack each of the inner iterables and pass them as arguments to the target function.
    """
    values: tuple[tuple[int, ...], ...] = (1, 2), (3, 4), (5, 6, 99), (7, 8, 9, 10),
    with mp.Pool() as pool:
        results: list[float] = pool.starmap(add_numbers, values)
    print(f"Results: {results}")


if __name__ == '__main__':
    main()
