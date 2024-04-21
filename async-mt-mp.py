import multiprocessing as mp
from asyncMtMpHelper import get_time, timestamp, kill_time
import os
import time


def func():
    print(f"Starting {mp.current_process().name} ({os.getpid()})...({timestamp()})")
    kill_time()
    print(f"{os.getpid()} finished! ({timestamp()})")


@get_time
def main():
    processes = []
    for i in range(23):
        p = mp.Process(name=f"Process-{i}", target=func)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


def convert_to_z(number: int) -> str:
    time.sleep(2)
    return number * "z"


@get_time
def main2():
    print(f"Cores available: {mp.cpu_count()}")
    values: tuple[int, ...] = tuple(range(0, 41))
    print(f"Values: {type(values)}")

    """
    Results: ['', 'z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz']
    Time taken: 2.1299614170s
    
    range from(0, value<numberOfCores) will take almost the same time ~2s
    If we run more than the number of cores, the time taken will be doubled now,
    because it will have to wait for a core to be free to process the next task.
    
    Results: ['', 'z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzzz', 'zzzzzzz', 'zzzzzzzz', 'zzzzzzzzz', 'zzzzzzzzzz']
    Time taken: 4.1140145420s
    
    Time taken will be increased by 2s if the number of processes cross any multiple of the number of cores.
    10 processes ~ 2s
    11 processes ~ 4s
    20 processes ~ 4s
    21 processes ~ 6s
    30 processes ~ 6s
    31 processes ~ 8s
    40 processes ~ 8s
    More processes spawned, more delays can happen - these are just rough logical numbers
    """

    """
    Benefit of using mp.Pool() is that it will automatically manage the number of processes spawned
    based on the number of cores available.
    ELse in normal mp.Process() we have to manage the number of processes spawned, else it will take more time.
    """

    with mp.Pool() as pool:
        results: list[str] = pool.map(convert_to_z, values)
        print("Results:", results)


if __name__ == "__main__":
    # main()
    main2()
