a: int = 10
b: int = 3

c = a // b

print(c, type(c))

print(2 == 2.0)

text: str = 'This is text'

for l in text:
    print(l + '-', end='')


def foo():
    try:
        return 1
    finally:
        return 2


result: int = foo()
print(result)
print(type({}))

num: int = 5


def func(num: int):
    print(num)


func(10)


def add(a: int = 4, b: int = 0):
    return a + b


print(add(5))
print('Hello' == "Hello")
