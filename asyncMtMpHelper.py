"""
asyncio - Achieves multithreading based on the code logic
multithreading - Achieves multiprocessing based on the operating system
multiprocessing - Achieves multiprocessing based on the number of cores in the CPU
first two are concurrent programming, last one is parallel programming

GIL - Global Interpreter Lock, a lock that allows only one thread to execute at a time,
even if the CPU has multiple cores

For I/O bound tasks, use asyncio and multithreading, because you will be waiting for the I/O
For CPU bound tasks, like image processing, use multiprocessing, because we can utilize all the cores

Starting a process is more expensive than starting a thread, because a process has its own memory space
and threads share the same memory space

Process Pools - A pool of processes that can be reused, similar to thread pools
"""

from time import perf_counter
from functools import wraps
from datetime import datetime


def get_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        end = perf_counter()
        print(f"Time taken: {end - start:.10f}s")

    return wrapper


def timestamp() -> str:
    return f"{datetime.now():%H:%M:%S}"


def kill_time():
    for _ in range(10 ** 7):
        pass
