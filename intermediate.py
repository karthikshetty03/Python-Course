import sys

print('string', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sep='::', end='~~~\n')

# enumerate function - gives number starting from 0 to iterate over a sequence
for i, char in enumerate('hello'):
    print(i, char, end=' ')
print()

# zip function - to iterate over multiple sequences
for i, j in zip('hello', 'worldPython'):
    print(i, j, end=' ')
print()

number: float = 1.666666
print(round(number, 3))

# help function - to get help on a function
print(help(round))

# dir function - to get all the attributes and methods of an object
print(dir(number))

# id function - to get the memory address of an object
print(id(number))

# type function - to get the typeof an object
print(type(number))

# isinstance function - to check if an object is an instance of a class
print(isinstance(number, float))

numbers: range = range(10)
large_numbers: range = range(10 ** 20)
print(large_numbers)
print(numbers)
# print(list(large_numbers))
print(list(numbers))
print("size of range obj", sys.getsizeof(large_numbers))
print("size of range obj", sys.getsizeof(numbers))
print(sys.getsizeof(list(numbers)))

# eval function - to evaluate a string as a python expression
print(eval('10*5'))
print(sys.int_info)
print(sys.float_info)

# exec function - to execute a string as a python statement
exec('print("executing a string as a python statement")')

# globals function - to get the global variables
print(globals())

# locals function - to get the local variables
print(locals())

# all function - to check if all elements in an iterable are true
print(all([1, 2, 3, 4, 5]))

# any function - to check if any element in an iterable is true
print(any([0, 0, 0, 0, 1]))

# callable function - to check if an object is callable
print(callable(print))

# chr function - to get the character from an ascii value
print(chr(65))

# ord function - to get the ascii value of a character
print(ord('A'))

# compile function - to compile a string as a python code
code = 'print("compiled code")'
compiled_code = compile(code, 'compiled_code', 'exec')
exec(compiled_code)

# isinstance function - to check if an object is an instance of a class
print(isinstance(number, float))

# issubclass function - to check if a class is a subclass of another class
print(issubclass(float, object))

# iter function - to get an iterator from an iterable
iterable = [1, 2, 3, 4, 5]
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))


# filter function - to filter elements from an iterable
def is_even(num):
    return num % 2 == 0


even_nums = filter(is_even, iterable)


# map function - to apply a function to all elements of an iterable
def square(num):
    return num ** 2


mapped_nums = map(square, iterable)
print(list(mapped_nums))

# sorted function - to sort an iterable
print(sorted(iterable, reverse=True))
print(iterable.sort())
