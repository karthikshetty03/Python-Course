import functools
from functools import wraps
from time import perf_counter, sleep
from typing import Callable


# custom decorator
def get_time(funct):
    """Times any function"""

    @wraps(funct)
    def wrapper(*args, **kwargs):
        start_time: float = perf_counter()
        funct(*args, **kwargs)
        print(f"Function name: {funct.__name__}")
        print(f"Function docstring: {funct.__doc__}")
        print(f"Function arguments: {args} {kwargs}")
        end_time: float = perf_counter()
        total_time = round(end_time - start_time, 3)
        print(f"Total time: {total_time} seconds")

    return wrapper


def repeat(times: int, message: str):
    """Repeats function call x amount of times"""

    def decorator(fun: Callable):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                fun(*args, **kwargs)
            print(message)

        return wrapper

    return decorator


@repeat(3, "This is func")
def func():
    print("Hello")


@repeat(3, "This is func2")
def func2(a: int, b: int):
    print(a, b, sep=" ")


@get_time
def do_something(param: str):
    """Do something important"""
    sleep(1)
    print(param)


def memoize(fib):
    cache: dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key: str = args[0]
        if key not in cache:
            cache[key] = fib(*args, **kwargs)
        print(f"Cache: {cache}")
        return cache[key]

    return wrapper


def memoizer(print_cache=False):
    def decorator(fib):
        cache: dict = {}

        @wraps(fib)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key not in cache:
                cache[key] = fib(*args, **kwargs)
                if print_cache:
                    print(f"Cache: {cache}")
            return cache[key]

        return wrapper

    return decorator


@functools.cache
@memoizer(print_cache=False)
@memoize
def fibonacci(n: int) -> int:
    """Returns the nth fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# context manager
with open("test.txt", "w") as file:
    file.write("Hello world")


# custom context manager
class File:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("Opening file...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")


# custom exception clas
class NegativeException(Exception):
    """Raised when a negative number is passed"""

    def __init__(self, num: float, error_code: int):
        self.num = num
        self.error_code = error_code
        super().__init__(f"{self.num} is less than 0, error_code: {self.error_code}", self.num, self.error_code)

    def __str__(self):
        return f"{self.num} is less than 0, error_code: {self.error_code}"

    def custom_method(self):
        print("Custom method", f"{self.num} is less than 0, error_code: {self.error_code}")

    # for pickling
    def __reduce__(self):
        return self.__class__, (self.num, self.error_code)


if __name__ == "__main__":
    # do_something("Hello")
    func()
    func2(1, 2)
    start: float = perf_counter()
    print(fibonacci(10))
    end: float = perf_counter()
    print(f"Total time for fib : {end - start}")

    with File('test.py') as file:
        print(file.name)
    print("Done")

    try:
        raise NegativeException(-5, 999)
    except NegativeException as e:
        print(e)  # __str__ method in Exception class is implemented to return the message only
        print(e.args)
        e.custom_method()

"""
Python was created by Guido van Rossum, and released in 1991. Python was nemed after the comedy television show 
Monty Python's Flying Circus. Python is an interpreted language, means that it is executed line by line. Python is 
dynamically typed, means that you don't have to declare the type of a variable. Python is a high-level language, 
means that it is easy to read and write. What is PEP? - PEP stands for Python Enhancement Proposal. It is a design 
document that provides information to the Python community, or describes a new feature for Python or its processes or 
environment.

"""
