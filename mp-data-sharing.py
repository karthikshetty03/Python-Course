from multiprocessing import Process

numbers: list[int] = [0]


def func():
    # numbers = [1]  # SyntaxError: name 'numbers' is assigned to before global declaration
    global numbers
    numbers.extend([6, 7, 8, 9, 10])
    print(f"Process data: {numbers}")


def main():
    process = Process(target=func)
    process.start()
    process.join()
    print(f"Main data: {numbers}")


if __name__ == "__main__":
    """In multiprocessing, each process has its own memory space. So, the changes made to the data in the child 
    process to the global variable in the parent process will not be reflected.
    """
    main()
