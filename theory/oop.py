from abc import ABC, abstractmethod
from typing import Protocol


class Lamp:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color

    def turn_on(self):
        print(f"{self.model} is turned on")

    def turn_off(self):
        print(f"{self.model} is turned off")

    def describe(self):
        print(f"Lamp: {self.model} is of {self.color} color")


# private - only class
# protected - class and subclasses
# public - everywhere

# private variables in python
# __variable_name
# protected variables in python
# _variable_name
# public variables in python
# variable_name
class Fruit:
    def __init__(self, name: str, calories: int = 0):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        print(f"Getting name: {self._name}")
        return self._name

    # getter is by default, but setter is not
    @name.setter
    def name(self, value: str):
        print(f"{self._name} is now: {value}!")
        self._name = value

    @property
    def kcal(self):
        return self._calories

    @kcal.setter
    def kcal(self, value: int):
        self._calories = value

    def __str__(self):
        return f"{self._name} has {self._calories} kcal"

    def __repr__(self):
        return f"Fruit(name={self._name}, calories={self._calories})"

    # def __eq__(self, other):
    #     return self.__dict__ == other.__dict__


# Methods vs Functions
# Methods are functions that are part of a class
# Functions are standalone entities
class Car:
    def __init__(self, name: str, model: str, version: str = "1.0"):
        self.name = name
        self.__model = model
        self._version = version

    def description(self):
        print(f"{self.name} {self.__model}")

    def _self_maintenance(self):
        print(f"{self.name} is doing self maintenance")

    def __self_maintenance_pvt(self):
        print(f"{self.name} is doing self maintenance")


class SelfDrivingCar(Car):
    def __init__(self, name: str, model: str, version: str):
        super().__init__(name, model, version)

    def self_driving(self):
        print(f"{self.name} {self._version} is self driving")
        # print(f"model is {self._Car__model}") --> Bad practice


# Inheritance
class Animal:
    def __init__(self, name: str):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Cat(Animal):
    def __init__(self, name: str, breed: str, weight: float):
        super().__init__(name)
        self.breed = breed
        self.weight = weight

    def meow(self):
        print(f"{self.name} of breed {self.breed} weighing {self.weight} is meowing")


class Dog(Animal):
    def __init__(self, name: str, breed: str, weight: float):
        super().__init__(name)
        self.breed = breed
        self.weight = weight

    def bark(self):
        print(f"{self.name} of breed {self.breed} weighing {self.weight} is barking")

    def sleep(self):
        super().sleep()
        print(f"{self.name} is sleeping like a dog")


class Calculator:
    def __init__(self, name: str):
        self.name = name

    def description(self):
        print(f"{self.name} is a calculator")

    @staticmethod
    def add(a: int, b: int):
        print(a + b)
        return a + b

    @classmethod
    def create_with_version(cls, name: str, version: str):
        return cls(f'{name} {version}')


class Phone(ABC):
    def __init__(self, model: str):
        self.model = model

    @property
    @abstractmethod
    def power(self):
        ...

    @abstractmethod
    def call(self):
        ...

    @abstractmethod
    def message(self):
        ...


# Class must implement all abstract methods
class IBanana(Phone):
    def __init__(self, model: str):
        super().__init__(model)

    @property
    def power(self):
        return "Battery Powered"

    def call(self):
        print("Calling from iBanana")

    def message(self):
        print("Messaging from iBanana")


class Printable(Protocol):
    pages: int

    def print(self):
        pass

    def recycle(self):
        pass


class Book(Printable):
    pages: int

    def __init__(self, title: str):
        self.title = title

    def print(self):
        print(f"Printing book {self.title}")

    def recycle(self):
        print(f"Recycling book {self.title}")


class Magazine:
    pages: int

    def __init__(self, title: str):
        self.title = title

    def print(self):
        print(f"Printing magazine {self.title}")

    def recycle(self):
        print(f"Recycling magazine {self.title}")


def print_item(printable: Printable):
    printable.print()


class Connection:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print("Connecting....")
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            print("There's already a connection")
            return cls.__instance

    def __init__(self):
        print("Connected to the internet")


class Vehicle:
    def __new__(cls, wheels: int):
        if wheels == 2:
            return Bike()
        elif wheels == 4:
            return Cars()
        else:
            return super().__new__(cls)

    def __init__(self, wheels: int):
        self.wheels = wheels
        print("Vehicle is created with wheels: ", wheels)


class Bike:
    def __init__(self):
        print("Bike is created")


class Cars:
    def __init__(self):
        print("Cars is created")


if __name__ == "__main__":
    red_lamp: Lamp = Lamp("RRX55", "Red")
    red_lamp.turn_on()
    red_lamp.turn_off()
    red_lamp.describe()
    print(red_lamp.__dict__)
    apple1: Fruit = Fruit("Apple", 100)
    apple2: Fruit = Fruit("Apple", 100)
    print(apple1.__dict__)
    print(apple2.__dict__)
    print(apple1 == apple2)
    print(apple1.__eq__(apple2))
    print(apple1.name)
    apple1.name = "Banana"
    print(apple1.name)
    print(apple1.kcal)
    apple1.kcal = 205
    print(apple1.kcal)
    print(apple1)
    print(apple1.__repr__())
    print(repr(apple1))
    car: Car = Car("BMW", "X5")
    car.description()
    print(car.__dict__)
    # car._self_maintenance()
    # car._Car__self_maintenance_pvt()
    sdc: SelfDrivingCar = SelfDrivingCar("Tesla", "Model S", "2.0")
    sdc.self_driving()
    cat: Cat = Cat("Tom", "Persian", 5.5)
    cat.eat()
    cat.sleep()
    cat.meow()
    dog: Dog = Dog("Spike", "Bulldog", 10.5)
    dog.eat()
    dog.sleep()
    dog.bark()
    calc: Calculator = Calculator("Casio")
    calc.description()
    calc.add(5, 10)
    Calculator.add(5, 10)
    calc_version: Calculator = Calculator.create_with_version("Casio", "2.0")
    calc_version.description()
    book: Printable = Book("Python")
    print_item(book)
    magazine: Printable = Magazine("Python")
    print_item(magazine)
    connection1: Connection = Connection()
    connection2: Connection = Connection()
    print(connection1 == connection2)
    bike: Vehicle = Vehicle(2)
    cars: Vehicle = Vehicle(4)
    vehicle: Vehicle = Vehicle(6)
