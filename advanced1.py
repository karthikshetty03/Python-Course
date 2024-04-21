from dataclasses import dataclass


@dataclass
class Fruit2:
    name: str = 'grapes'
    calories: int = 52


class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


# lambda function example
def square(ele: float) -> float:
    return ele ** 2


sq = lambda number_val: number_val ** 2
print(f"square : {sq(5)}")

even: list[int] = list(filter(lambda x: x % 2 == 0, range(0, 20)))
print(f"even: {even}")


# walrus operator useful for assignment and comparison in one line of code (:=)
# example
def walrus_operator():
    exp = 10
    while exp > 0:
        print(exp)
        exp -= 1


# using walrus operator
def walrus_operator_ex():
    val = 10
    while (val := val - 1) > 0:
        print(val)


def get_info(text: str) -> dict:
    return {'text': text,
            'letters': (length := len(text.replace(" ", ""))),
            'words': (words := text.split()),
            "total_words": (word_length := len(words)),
            "avg_per_word": length / word_length if word_length > 0 else "No words found"
            }


# while user_input := input("Enter something: "):
#     print(">>", user_input)
# else:
#     print("You entered nothing!")


# generator function - return 1 value at a time
def generate_list(n: int):
    for i in range(n):
        yield i


if __name__ == '__main__':
    fruit_a: Fruit = Fruit('apple', 52)
    fruit_b: Fruit = Fruit('apple', 52)
    print(f"a: {id(fruit_a)} b: {id(fruit_b)}")  # is operator checks the memory address
    print(f"fruit_a == fruit_b: {fruit_a == fruit_b}")
    print(f"fruit_a is fruit_b: {fruit_a is fruit_b}")

    _ = 50
    a = 100
    b = _ + a
    print(f"b: {b}")

    a = 10
    b = 10
    print(f"a: {id(a)} b: {id(b)}")  # same id because of memory optimization

    for key, value in get_info("This is some text!").items():
        print(key, value, sep=': ')

    pineapple1: Fruit2 = Fruit2('pineapple', 452)
    pineapple2: Fruit2 = Fruit2('pineapple', 452)
    pineapple3: Fruit = Fruit('pineapple', 452)
    print(f"pineapple1 == pineapple2: {pineapple1 == pineapple2}")
    print(f"pineapple2 == pineapple3: {pineapple2 == pineapple3}")
    print(pineapple2)
    print(pineapple3)
    grapes: Fruit2 = Fruit2()
    print(grapes)
    generated_list = generate_list(10 ** 100)
    print(generated_list)
    print(next(generated_list))
    print(next(generated_list))
    print(next(generated_list))
    print(next(generated_list))
    print(next(generated_list))

    list_a: list[int] = []
    for num in generated_list:
        if num == 10:
            break
        list_a.append(num)
    print(list_a)  # last 5 numbers because we break at 10 and 5 elements are already consumed

    print(next(generated_list))
    print(next(generated_list))
    print(next(generated_list))
    print(next(generated_list))
    print(next(generated_list))

    # delete keyword
    del fruit_a
    # try:
    #     print(fruit_a)  # NameError: name 'fruit_a' is not defined
    # except NameError as e:
    #     print(e)

    try:
        # assert keyword
        assert isinstance(pineapple1, Fruit), "pineapple1 is not instance of Fruit"
    except AssertionError as e:
        print(e)

    # doc string
    """
    This is a doc string
    """

    status: int = 400
    if status == 200:
        print("Success...")
    elif status == 400:
        print("Bad Request...")
    elif status == 500:
        print("Internal Server Error...")
    elif status == 300:
        print("Redirect...")
    else:
        print("Unknown status code...")

    match status:
        case 200:
            print("Success...")
        case 400:
            print("Bad Request...")
        case 500:
            print("Internal Server Error...")
        case 300:
            print("Redirect...")
        case _:
            print("Unknown status code...")

    user_input: str = input("Enter command: ")
    p_command: list[str] = user_input.split()

    print(f"p_command: {p_command}")
    match p_command:
        case ['find', *images]:
            print(f"Finding: {images}")
        case ['download', *images]:
            print(f"Downloading: {images}")
        case ['cancel' | 'delete', *images] if len(images) > 1:
            print(f"Deleting: {images}")
        case _:
            print("Unknown command...")
