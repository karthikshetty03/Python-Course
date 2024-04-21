import random as r

import requests as req

# This is the output of the code

"""
this is a comment, it will not be executed
"""

# Naming convention for constants
PI = 3.1415

text = "Hello, World!"
print(text)
text = 'Hello, World!'
print(text)

# Numeric types
number = -100
print(number)
number = 100
print(number)

# Float
number = 3.14
print(number)

# Complex
number = 1 + 2j
print(number)

# Boolean
boolean = True
print(boolean)

# Sequence Types
# List, ordered collection of items
list0 = [1, 2, 3, 4, 5]
print(list0)

# Tuple, cannot be changed once they are created
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Set, unordered collection of unique items
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Empty dict
my_dict = {}
print(my_dict.keys())
my_dict['name'] = 'John'
my_dict['age'] = 30
print(my_dict)

# Dictionary, unordered collection of key-value pairs
my_dict = {'name1': 'John', 'name2': 'Luigi', 'name3': 'Mario'}
print(my_dict)

# from 1 to 999
numbers = range(1, 1000)
print(numbers)

# Empty set
nums = set()
nums.add(1)

# set of numbers, does not keep track of order
numbers = {1, 2, 2, 3, 3, 4, 5}
print(numbers)
print(nums)

# frozen set
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)

# Boolean
boolean = True
print(boolean)

# Bytes
byte = b"Hello"
print(byte)

# Byte array
byte_array = bytearray(5)
print(byte_array)

# Memory view
memory_view = memoryview(byte_array)
print(memory_view)

# None Type
is_empty = None
print(is_empty)


# type hinting
def greeting(names: str) -> str:
    return "Hello, " + names


name: str = "John"
age: int = 30
print(name + " is " + str(age) + " years old")

# F-strings
print(f"{name} is {age} years old")

list0 = [1, 2, 3, 4, 5, 6]
print(list0)
list0.append(7)
print(list0)
list0.remove(2)
print(list0)
list0.pop()
print(list0)
list0.pop(0)
print(list0)
list0.insert(0, 1)
print(list0)
list0.clear()
print(list0)

# List slicing
list0 = [1, 2, 3, 4, 5, 6]
print(list0[0:2])
print(list0[2:])
print(list0[:2])
print(list0[-1])
print(list0[-2])
print(list0[-3:-1])
print(list0[::2])
print(list0[::-1])

# List comprehension
list0 = [i for i in range(10)]
print(list0)
list1 = [i for i in range(10) if i % 2 == 0]
print(list1)
list1.extend(list0)
print(list1)
list1 += list1
list1.sort()
print(list1)

# tuple are defined by comma and not by parenthesis
# tuples are ordered and unchangeable
people: tuple = "John", "Luigi", "Mario"
print(people)
tuple2: tuple = "John",
print(tuple2)

# tuple unpacking
person1, person2, person3 = people
print(person1)

# various types of if-else
if age < 18:
    print("You are a minor")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")

# do this if True else do this
print("You are a senior") if age > 65 else print("You are an adult")

a, b = 10, 20
print('a is greater than b') if a > b else print('b is greater than a') if b > a else print('a is equal to b')

# while loop
i = 0
while i < 10:
    print(i)
    i += 1

# for loop
for i in range(10):
    print(i)

# for loop with step
for i in range(0, 10, 2):
    print(i)

# for loop with step
for i in range(10, 0, -1):
    print(i)

# for loop with pass
for i in range(10):
    pass

# print everything in same line
for i in range(10):
    print(i, end=" ")

# for else: else block will be executed if the loop is not terminated by a break statement
for i in range(10):
    print(i)
else:
    print("All done")


# parameters and arguments to a function
def greet(name2: str, age2: int) -> str:
    return f"Hello, {name2}. You are {age2} years old."


# function with default arguments
def greet1(name1: str = "John", age1: int = 30) -> str:
    return f"Hello, {name1}. You are {age1} years old."


# function with variable number of arguments
def greet2(*names: str) -> str:
    return f"Hello, {' --> '.join(names)}"


print(greet("John", 30))
print(greet1())
print(greet2("John", "Luigi", "Mario"))


# use default parameters at the end
def greet3(name3: str, age3: int = 30) -> str:
    return f"Hello, {name3}. You are {age3} years old."


print(greet3("John"))
print(greet3(age3=40, name3="Luigi"))


# *args - variable number of arguments
# **kwargs - variable number of keyword arguments
def greet4(*args, **kwargs):
    print(args)
    print('Printing keyword arguments')
    try:
        for index, (key, value) in enumerate(list(kwargs.items())):
            print(f"{index}) {key}: {value}")
    except Exception as ex:
        print(ex)
    return f"Hello, {kwargs['name']}. You are {kwargs['age']} years old."


print(greet4(1, 2, 3, name="John", age=30))

# user input
# name: str = input("Enter your name: ")
# print(f"Hello, {name}")

# a = input("A: ")
# b = input("B: ")
# print("Sum: ", int(a) + int(b))

# exception handling
try:
    a = 10 / 0
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("Done")

# raise an exception
x = 1
if x < 0:
    raise Exception("x should be positive")


# custom exception
class ValueTooSmallError(Exception):
    pass


# use the custom exception
try:
    x = 10
    if x < 5:
        raise ValueTooSmallError("Value is too small")
except ValueTooSmallError as e:
    print(e)

# file handling
file = open("file.txt", "w")
file.write("Hello, World!")
file.close()

file = open("file.txt", "r")
print(file.read())
file.close()

# using with statement - automatically closes the file
with open("file.txt", "w") as file:
    file.write("Hello, World!")

with open("file.txt", "r") as file:
    print(file.read())

print(r.randint(1, 10))
resp = req.get("https://www.google.com")
print("status Code: ", resp.status_code)
print("Response: ", resp.text)

# Package vs. library
# Package is a collection of modules
# Library is a collection of packages
# Module is a file containing Python code

# Example of a package
# import package.module
# from package import module
# from package.module import function

# example of a library
# import library
# from library import package
# from library.package import module
# from library.package.module import function
