import threading
import time

"""
Global Interpreter Lock (GIL) is a mutex that protects access to Python objects,
preventing multiple threads from executing Python bytecodes at once.
This lock is necessary because CPython's memory management is not thread-safe.
"""

"""
Concurrency vs Parallelism
- Concurrency: multiple tasks make progress together, but not necessarily at the same time
- Parallelism: multiple tasks run at the same time, potentially on different cores
"""

"""
asyncio uses a single-threaded event loop to run tasks concurrently.
It is useful for I/O-bound tasks, but not for CPU-bound tasks.
Using asyncio, not running at the same time but happening at the same time
"""

lock = threading.Lock()


def counter(name: str, limit: int):
    for i in range(limit):
        time.sleep(0.5)
        print(name, i + 1, sep=": ")


def task1():
    lock.acquire()
    counter('T-1', 5)
    # If we don't release the lock, the other thread will not be able to run
    lock.release()


def task2():
    lock.acquire()
    counter('T-2', 5)
    lock.release()


def task3():
    counter('T-3', 5)


def process_data(name: str, count: int):
    print(f"Starting name: {name}")
    for i in range(count):
        print(name, i + 1, sep=": ")
        time.sleep(1)


def main():
    thread11 = threading.Thread(target=task1)
    thread22 = threading.Thread(target=task2)
    thread33 = threading.Thread(target=task3)
    thread11.start()
    thread22.start()
    thread33.start()
    thread11.join()
    thread22.join()
    thread33.join()


if __name__ == '__main__':
    # process_data("Thread 1", 5)
    # process_data("Thread 2", 5)
    # thread_one = threading.Thread(target=process_data, kwargs={"name": "Thread 1", "count": 5})
    # thread_two = threading.Thread(target=process_data, args=("Thread 2", 5))
    # thread_one.start()
    # thread_two.start()
    # thread_one.join()
    # thread_two.join()
    # thread1 = threading.Thread(target=task1)
    # thread2 = threading.Thread(target=task2)
    # thread1.start()
    # thread1.join()
    # thread2.start()
    # thread2.join()
    main()
