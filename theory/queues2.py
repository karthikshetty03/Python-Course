from multiprocessing import Queue, Process, current_process


def func(queue: Queue):
    name = current_process().name
    try:
        print(f"{name} received data: {queue.get(timeout=3)}")
    except Exception as e:
        print("Timeout!", e)


def main():
    queue: Queue = Queue()
    # Send in order, then receive in order
    queue.put(1)
    queue.put(2)
    queue.put(3)
    queue.put(4)
    processes = [Process(target=func, args=(queue,)) for _ in range(5)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()


if __name__ == "__main__":
    main()
