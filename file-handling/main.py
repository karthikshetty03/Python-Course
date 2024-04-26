import os
import json

"""
modes of file handling: either read or write, rt, wt, at, rb, wb, ab
r - read
w - write
a - append
t - text (default)
b - binary (images, videos, etc.)
"""
# file = open('sample.txt', 'r') $ will have to close the file

with open('sample.txt', 'r') as file:
    # print(file.read(10))
    # print(file.readline())
    # print(file.readlines()) # returns a list of lines
    for line in file:
        print(line, end='')
    print("\nFile closed")

with open('sample.txt', 'a') as file:
    file.write('\nThis is the fourth line')

with open('sample1.txt', 'a+') as file:  # a+ allows reading and writing
    file.write('\nThis is the fourth line')
    file.seek(0)  # moves the cursor to the beginning of the file
    print(file.readlines())

with open('sample2.txt', 'w+') as file:  # a+ allows reading and writing
    file.write('This is always the first line')
    file.seek(0)  # moves the cursor to the beginning of the file
    print(file.readlines())

# x mode will create a file if it doesn't exist
try:
    with open('sample5.txt', 'x') as file:
        file.write('This is the first line')
except FileExistsError:
    print('File already exists')

try:
    with open('sample55.txt', 'x+') as file:
        file.write('This is the first line')
        file.seek(0)
        print(file.read())
except FileExistsError:
    print('File already exists')

# Deleting files

if os.path.exists('sample5.txt'):
    os.remove('sample5.txt')
    print('File deleted')
else:
    print('File does not exist')

if os.path.exists('sample55.txt'):
    os.remove('sample55.txt')
    print('File deleted')
else:
    print('File does not exist')

for item in os.listdir('.'):
    print(item, end=' ')
else:
    print()

with open('sample.json') as file:  # default mode is 'r'
    content: dict = json.load(file)
    print(content)

with open('sample.json') as file:
    content: str = file.read()
    print(content)
    contents: dict = json.loads(content)
    print(contents)

sample_dict = {'name': 'John Doe', 'age': 30, 'is_student': False, 'courses': None}
sample_json = json.dumps(sample_dict)
print(sample_json)

with open('sample1.json', 'w') as file:
    json.dump(sample_dict, file, indent=2)


