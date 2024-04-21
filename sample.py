def do_something():
    print("Doing something....")


# do_something()
# if we simply import this module, the above if uncommented function will run on import itself
# to avoid this, we use the below if statement
# main is whatever file we are currently running
print(__name__)
if __name__ == "__main__":
    do_something()

var = 10
x = 10


# defining a function inside a function
def outer():
    var1 = 13
    x = 20

    def inner():
        x = 30
        var2 = 20
        print("Inner function")
        print(f"var: {var}")
        print(f"var1: {var1}")
        print(f"var2: {var2}")
        print(f"Inner x: {x}")

    inner()
    print("Outer function")
    print(f"var: {var}")
    print(f"var1: {var1}")
    # print(f"var2: {var2}")
    print(f"Outer x: {x}")


print("Global scope")
print(f"var: {var}")
# print(f"var1: {var1}")
# print(f"var2: {var2}")
print(f"Global x: {x}")

outer()


# inner() - this will throw an error as inner is not defined in the global scope

# global keyword

def outer2():
    global x
    x = 301
    print(f"x: {x}")


outer2()
print(f"x: {x}")


# nonlocal keyword
# nonlocal is used to refer to a variable in the outer function
# when the variable is not in the global scope
# nonlocal is used to refer to a variable in the outer function

def outer3():
    x = 10

    def inner():
        nonlocal x
        x = 20
        print(f"Inner x: {x}")

    inner()
    print(f"Outer x: {x}")


outer3()


# list comprehension - examples
sample_list = [i for i in range(10)]
print(sample_list)


sample_list2 = [i for i in range(10) if i % 2 == 0]
print(sample_list2)


people: list[str] = ["John", "Luigi", "Mario"]
cap_people = [person.upper() for person in people]
print(cap_people)


# slice lists
numbers: list[int] = list(range(21))
print(numbers[::3])
print(numbers[10::3])
print(numbers[3:16:3])
print(numbers[::-1])
print(numbers[:-1])
print(numbers[0:])
