from multiprocessing import Pipe, Process, current_process
from random import randint
import os
import time


def sender(connection):
    print(f"Sender {current_process().name} ({os.getpid()})...")

    for _ in range(5):
        rand: int = randint(1, 10)
        connection.send(rand)
        print(f"Sent: {rand} was sent")
        time.sleep(0.5)

    print(f"Sending None...")  # None is a sentinel value, a value that signals the end of the sequence
    connection.send(None)
    print("Done with sending data!")


def receiver(connection):
    print(f"Receiver {current_process().name} ({os.getpid()})...")

    while True:
        data = connection.recv()
        print(f"Received: {data}")
        if data is None:
            print("Received None, exiting...")
            break
    print("Done receiving data!")


def main():
    c1, c2 = Pipe()
    s = Process(target=sender, args=(c1,))
    r = Process(target=receiver, args=(c2,))
    s.start()
    r.start()
    s.join()
    r.join()


if __name__ == '__main__':
    main()
