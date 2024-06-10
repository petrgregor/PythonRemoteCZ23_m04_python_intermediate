import pickle
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def circuit(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"Rectangle(a={self.a}, b={self.b})"

    def __str__(self):
        return (f"Rectangle with parameters a={self.a} and b={self.b}"
                f" has circuit={self.circuit()} and area={self.area()}.")

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


try:
    with open('rectangle1.pickle', 'rb') as f:
        rectangle = pickle.load(f)
        print(rectangle)
except FileNotFoundError:
    print("ERROR: FileNotFoundError")

print("END")
