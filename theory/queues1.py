from multiprocessing import Process, Queue


def insert_value(queue: Queue, value: int):
    queue.put(value)
    print(f'Value {value} has been inserted into the queue')


def main():
    queue: Queue = Queue()
    processes = [Process(target=insert_value, args=(queue, i)) for i in range(5)]  # range 6 will block similar to pipe
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    results = [queue.get() for _ in processes]
    print(f'All values inserted into the queue: {results}')


if __name__ == '__main__':
    main()
