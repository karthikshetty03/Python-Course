import multiprocessing as mp
import time
from asyncMtMpHelper import *
import functools


def add_numbers(*args) -> int:
    print(f"Adding: {args}")
    time.sleep(2)
    return sum(args)


def func_a(param):
    time.sleep(2)
    return param


def func_b(param):
    time.sleep(2)
    return param


def func_c(param1, param2):
    time.sleep(2)
    return param1, param2


def map_func(func):
    return func()


@get_time
def main():
    print(f"Cores available: {mp.cpu_count()}")
    """
    partial functions - allows us to fix a certain number of arguments of a function and generate a new function.
    """
    a = functools.partial(func_a, 'A"')
    b = functools.partial(func_b, 'B')
    c = functools.partial(func_c, 'C1', 'C2')

    with mp.Pool() as pool:
        results = pool.map(map_func, [a, b, c])
        print(results)


if __name__ == '__main__':
    main()