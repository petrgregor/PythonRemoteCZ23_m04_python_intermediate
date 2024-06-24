"""
An abstract class is used to map objects that do not exist by themselves, but are the basis for other objects.
For example, you are not able to create an animal because you don't know what type of animal it is.
You need to create an abstract class which maps this situation and child classes which implement a method that
returns the sound made by a specific animal.
"""
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):

    def make_sound(self):
        return "Roooaaarrrr"


class Bird(Animal):

    @abstractmethod
    def make_sound(self):
        pass


class Sparrow(Bird):

    def make_sound(self):
        return "Krrrraaaakraaaa"


if __name__ == "__main__":
    lion = Lion()
    print(lion.make_sound())

    sparrow = Sparrow()
    print(sparrow.make_sound())
