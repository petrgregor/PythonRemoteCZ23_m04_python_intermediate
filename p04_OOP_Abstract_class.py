from abc import ABC, abstractmethod
from math import pi

"""
# Bez použití abstraktní třídy:
class Circle:
    def __init__(self, r):
        self.r = r

    def circuit(self):
        return 2 * pi * self.r

    def area(self):
        return pi * (self.r ** 2)


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


rectangle1 = Rectangle(5, 6)
print(f"Rectangle1: circuit={rectangle1.circuit()}, area={rectangle1.area()}.")

circle1 = Circle(10)
print(f"Circle1: circuit={circle1.circuit()}, area={circle1.area()}")
"""


class Figure(ABC):
    @abstractmethod
    def circuit(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def circuit(self):
        return 2 * pi * self.r

    def area(self):
        return pi * (self.r ** 2)


class Square(Figure):
    def __init__(self, a):
        self.a = a

    def circuit(self):
        return 4 * self.a

    def area(self):
        return self.a ** 2


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


# TODO: class Triangle


rectangle1 = Rectangle(5, 6)
print(f"Rectangle1: circuit={rectangle1.circuit()}, area={rectangle1.area()}.")

circle1 = Circle(10)
print(f"Circle1: circuit={circle1.circuit()}, area={circle1.area()}")

square1 = Square(5)
print(f"Square1: circuit={square1.circuit()}, area={square1.area()}")
