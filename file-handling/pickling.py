import pickle

# Pickle a dictionary into a file
favorite_color = {"lion": "yellow", "kitty": "red"}
pickle.dump(favorite_color, open("save.p", "wb"))


# class Fruit with name and calories
class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def describe_fruit(self):
        print(f"{self.name} has {self.calories} calories")


if __name__ == "__main__":
    # Create an instance of Fruit
    # apple = Fruit("apple", 52)
    # Pickle the instance of Fruit
    # pickle.dump(apple, open("apple.p", "wb"))

    # Unpickle the instance of Fruit
    apple = pickle.load(open("apple.p", "rb"))
    apple.describe_fruit()

"""
Disclaimer: 
pickling is not secure and should not be used to store sensitive data.
unpickling data from an untrusted source can lead to security risks.
"""