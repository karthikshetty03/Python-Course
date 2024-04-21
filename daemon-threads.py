import threading
import time
import random

"""
daemon threads are considered to be low priority threads.
Only stays alive while the main thread is alive.
"""

"""
semaphore is basically multiple locks.
"""
sem = threading.Semaphore(10)
"""
if we replace the above with lock, then only one thread will be able to run at a time.
else, 5 threads will be able to run at a time.
"""


def process_something(process_id: int):
    sem.acquire()
    print(f"Running {process_id}")
    num = random.randint(1, 10)
    print(f"Sleeping for {num} seconds")
    time.sleep(num)
    print(f"Finished {process_id}")
    sem.release()


def process_something_with_sem(process_id: int):
    with sem:  # works for both semaphore and lock
        print(f"Running {process_id}")
        num = random.randint(1, 10)
        print(f"Sleeping for {num} seconds")
        time.sleep(num)
        print(f"Finished {process_id}")


def indefinite_loop():
    while True:
        print(time.time())
        time.sleep(1)


if __name__ == '__main__':
    # thread = threading.Thread(target=indefinite_loop, daemon=True)
    # thread.start()
    for i in range(10):
        time.sleep(0.5)
        # thread = threading.Thread(target=process_something, args={i + 1})
        thread = threading.Thread(target=process_something_with_sem, args={i + 1})
        thread.start()
