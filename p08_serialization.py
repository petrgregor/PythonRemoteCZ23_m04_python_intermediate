import pickle
from abc import ABC, abstractmethod

data = {
    'a': [1, 2.0, 3, 4 + 6j],
    'b': ("Alice has a cat", "Python programming is great"),
    'c': [False, True, False]
}
print(data)

# serialization
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# deserialization
with open('data.pickle', 'rb') as f:
    data2 = pickle.load(f)

print(data2)


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


rectangle1 = Rectangle(3, 4)
print(rectangle1)

with open('rectangle1.pickle', 'wb') as f:
    pickle.dump(rectangle1, f)

with open('rectangle1.pickle', 'rb') as f:
    rectangle2 = pickle.load(f)

print(rectangle2)
