from typing import Iterable
import timeit

text: str = "SAMPLEEd TEXT"
"""
:20 is the width of the text
"""
print(f"{text:20} text")
print(f"{text:<20} text")
print(f"{text:>20} text")
print(f"{text:^20} text")

print(f"{text:_<20} text")
print(f"{text:_>20} text")
print(f"{text:_^20} text")

number: float = 10_000.123456
print(f"{number:,.2f}")

num: float = .096
print(f"{num:.2%}")

num2: float = 0.123456789
print(f"{num2:.2e}")

num3: float = 123456789
print(f"{num3:,.2%}")

num4: float = 10 ** -10
print(f"{num4:.0e}")
print(f"{num4:e}")

numbers: tuple = (12, 'hello', False)
print(numbers)
numbers: tuple[int, str] = (12, 'hello')
print(numbers)
numbers: tuple[int,] = (12,)
print(numbers)
numbers: tuple[int, ...] = (12, 13, 14)
print(numbers)
numbers: tuple[int | str, ...] = (12, 'hello', 14)

people: list = [['John', 'Luigi', 'Mario'], ['Luigi', 'Mario', 'John']]
new_list: list[str] = []
for name in people:
    for n in name:
        new_list.append(n)
print(new_list)

new_list: list[str] = [name
                       for names in people
                       for name in names]
print(new_list)

complex_people: list = [['John', 'Luigi', 'Mario'], ['Luigi', 'Mario', 'John'], 'Luigi', 'Mario', 'John', [1, 2, 3]]


def flatten(iterable: Iterable) -> list:
    l: list = []
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, str):
            l.extend(flatten(item))
        else:
            l.append(item)
    return l


print(flatten(complex_people))

print(... == Ellipsis)


def do_something():
    ...


'''
kashett2@KASHETT2-M-7GCQ Python-Course % cd tips-and-tricks 
kashett2@KASHETT2-M-7GCQ tips-and-tricks % pylint main.py
************* Module tips-and-tricks.main
main.py:54:0: C0301: Line too long (116/100) (line-too-long)
main.py:96:0: C0305: Trailing newlines (trailing-newlines)
main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
main.py:57:0: C0116: Missing function or method docstring (missing-function-docstring)
main.py:71:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 9.00/10

kashett2@KASHETT2-M-7GCQ tips-and-tricks % 

'''

"""
 C0301:
Error messages from pylint
R -> Refactor for a “good practice” metric violation
C -> Convention for coding standard violation
W -> Warning for stylistic problems, or minor programming issues
E -> Error for important programming issues (i.e. most probably bug)
F -> Fatal for errors which prevented further processing
"""

import math, random  # NOQA: E401 E402

math.sqrt(16)
random.random()

hello = lambda text: print(text)  # NOQA

hello("HELLO")

text = 'Hello' 'World' 'all' 'are' 'concatenated' 'together'
print(text)


def strings_concat_raw():
    string: str = 'string'

    """
    strings are immutable, 
    so each time we concatenate a string, 
    a new string is created
    """
    for i in range(1000):
        string += 'string'

    # print(string)
    return string


def strings_concat_list():
    string: str = 'string'
    string_list: list[str] = [string]

    for i in range(1000):
        string_list.append(string)

    return ''.join(string_list)


if __name__ == '__main__':
    time_concat: float = timeit.timeit(stmt=strings_concat_raw, number=100_000)
    time_join: float = timeit.timeit(stmt=strings_concat_list, number=100_000)
    print(f"time_concat: {time_concat}")
    print(f"time_join: {time_join}")
    percent_faster: float = (time_concat - time_join) / time_concat * 100
    print(f"percent_faster: {percent_faster:.2f}%")
