import threading
from asyncMtMpHelper import get_time, timestamp, kill_time
import os


def func():
    print(f"Starting ({os.getpid()})...({timestamp()})")
    kill_time()
    print(f"{os.getpid()} finished! ({timestamp()})")


@get_time
def main():
    threads = []
    for i in range(15):
        t = threading.Thread(name=f"Thread-{i}", target=func)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
