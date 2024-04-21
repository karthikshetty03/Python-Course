from enum import Enum
# import sample

# Truthy and Falsy values
# Falsy values: "", 0, [], {}, None, False
# Truthy values: "hello", 1, [1], {1}, True

empty_list = []
empty_set = set()
empty_tuple = ()
empty_dict = {}
empty_string = ""

"""
tuple[int] specifies a tuple with exactly one element of type int.
tuple[int, int, ...] specifies a tuple with at least two elements of type int, 
followed by any number of additional int elements.
list[int] specifies a list that can contain any number of elements, all of which must be of type int.
set[int] specifies a set that can contain any number of unique elements, all of which must be of type int.
dict[str, int] specifies a dictionary where the keys are of type str and the values are of type int.
"""

print(type(empty_set))
print(type(empty_list))
print(type(empty_tuple))
print(type(empty_dict))
print(type(empty_string))

var = None
if var:
    print("Truthy")
else:
    print("Falsy")


class State(Enum):
    ON = 1
    OFF = 0


state = 1
if state == State.ON.value:
    print(f"The lamp is turned {State.ON.name}")
elif state == State.OFF.value:
    print(f"The lamp is turned {State.OFF.name}")
else:
    print("Unknown state")

# Comparing floats
a = 0.3
b = 0.1 + 0.2
print(a == b)
print(a)


def compare_floats(af: float, bf: float, tol: float = 1e-9) -> bool:
    return abs(af - bf) < tol


print(compare_floats(0.3, 0.1 + 0.2))
