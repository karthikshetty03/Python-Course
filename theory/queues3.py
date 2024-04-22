from multiprocessing import Process, Queue
import time


def square_num(identifier: int, num: int, queue: Queue):
    time.sleep(2)
    queue.put((identifier, num ** 2))


def main():
    queue: Queue = Queue()
    data: list[int] = list(range(1, 9))
    processes = [Process(target=square_num, args=(i, num, queue))
                 for i, num in enumerate(data)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    # unsorted
    results = [queue.get() for _ in range(len(data))]
    print(results)

    # sorted
    results = [val for val in sorted(results)]
    print(results)


if __name__ == '__main__':
    main()
