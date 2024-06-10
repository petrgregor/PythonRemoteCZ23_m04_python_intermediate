from abc import ABC, abstractmethod
from dataclasses import dataclass


class Figure(ABC):
    @abstractmethod
    def circuit(self):
        pass

    @abstractmethod
    def area(self):
        pass


@dataclass
class Rectangle(Figure):
    a: int
    b: int

    def __init__(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError
        if a <= 0 or b <= 0:
            raise ValueError
        self.a = a
        self.b = b

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


rectangle1 = Rectangle(3, 4)
print(f"rectangle1: circuit={rectangle1.circuit()}, area={rectangle1.area()}")
rectangle2 = Rectangle(3, 4)
print(f"rectangle2: circuit={rectangle2.circuit()}, area={rectangle2.area()}")

print(f"Are rectangle1 and rectangle2 same: {rectangle1 == rectangle2}")
print(rectangle1)
rectangle3 = Rectangle(4, 3)
print(f"rectangle3: circuit={rectangle3.circuit()}, area={rectangle3.area()}")
print(f"Are rectangle1 and rectangle3 same: {rectangle1 == rectangle3}")

"""
try:
    rectangle4 = Rectangle("Hi", "Rectangle")
    print(rectangle4)
    print(f"rectangle4: circuit={rectangle4.circuit()}, area={rectangle4.area()}")
except ValueError as e:
    print(f"ERROR: {e}")"""

try:
    rectangle5 = Rectangle(3, -4)
    print(rectangle5)
    print(f"rectangle5: circuit={rectangle5.circuit()}, area={rectangle5.area()}")
except ValueError:
    print("ERROR")

print(f"{rectangle3.a}")
