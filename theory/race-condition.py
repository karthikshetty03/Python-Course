import threading
import time

"""
A race condition occurs when two or more threads can access shared data and they try to change it at the same time.
"""

lock = threading.Lock()


def edit(operation: str, amount: int, repeat: int):
    global value
    """
    without this lock, the value will be different every time the program is run, because of race condition
    """
    with lock:
        for _ in range(repeat):
            temp: int = value
            time.sleep(0)

            if operation == 'add':
                temp += amount
            elif operation == 'subtract':
                temp -= amount

            time.sleep(0)
            value = temp


if __name__ == '__main__':
    value: int = 0
    adder = threading.Thread(target=edit, args=('add', 100, 1_000_000))
    subtractor = threading.Thread(target=edit, args=('subtract', 100, 1_000_000))
    adder.start()
    subtractor.start()
    print("Waiting for threads to finish...")
    adder.join()
    subtractor.join()
    print(f"Value: {value}")
