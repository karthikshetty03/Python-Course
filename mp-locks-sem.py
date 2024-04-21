from time import sleep
from multiprocessing import Process, Lock, Semaphore


def func(p_lock, identifier):
    with p_lock:
        sleep(1)
        print(f'Process {identifier} is running...')


def main():
    lock = Lock()
    sem = Semaphore(3)

    processes1 = [Process(target=func, args=(lock, _)) for _ in range(15)]
    processes2 = [Process(target=func, args=(sem, _)) for _ in range(15)]

    for _ in processes1:
        # _.start()
        pass

    for _ in processes1:
        # _.join()
        pass

    for _ in processes2:
        _.start()

    for _ in processes2:
        _.join()


if __name__ == '__main__':
    main()
