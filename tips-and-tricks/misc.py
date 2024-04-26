from array import array
from sys import getsizeof
from datetime import datetime

print('This is a quote: \'Hello, World\'')
print("This\vis\va\vmessage\v")  # Run it in console

string: str = 'Hello, World' \
              ' This is a string' \
              ' This is a string' \
              ' This is a string'

print(string)

values = (1, 2, 3, 4, 5)
a, b, *c = values
e, _, _, _, f = values
print(f)
print(c, type(c))

"""list vs arrays - Lists in python defined as list = [1, 2, 3, 4, 5] - 
Arrays in python defined as arr = array('i', [1, 2, 3, 4, 5]) 'i' is the typecode for signed integer, 
other type codes are 'I' for unsigned integer, 
'f' for float, 'd' for double, etc. an array can have a single type of elements, 
whereas a list can have different types of elements. 
memory size of an array for a single/less elements is more than that of a list. 
whereas memory size of a list is more than that of an array 
when the number of elements is significantly more than the initialization cost.
array is faster than list, numpy is used for ML, DL, AI, etc.
"""

arr = array('i', range(10_000))
lst = list(range(10_000))

print('Array', getsizeof(arr), 'bytes')
print('List', getsizeof(lst), 'bytes')

arr1 = array('i', range(1))
arr1.append(6)
print(arr1)
lst1 = list(range(1))

print('Array1', getsizeof(arr1), 'bytes')
print('List1', getsizeof(lst1), 'bytes')


@lambda _: _()
def script_start_time() -> str:
    current_time: str = f'{datetime.now():%H:%M:%S}'
    print(f'Start time: {current_time}')
    return current_time

print(script_start_time)
