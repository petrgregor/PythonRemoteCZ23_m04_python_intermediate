from abc import ABC, abstractmethod
from copy import deepcopy


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
                f" has circuit={self.circuit()} and area={self.area()}"
                f" diagonal length={Diagonal.length(self.a, self.b)}.")

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Diagonal(ABC):

    @staticmethod
    def length(a, b):
        return (a**2 + b**2)**(1/2)


rectangle1 = Rectangle(3, 4)
print(rectangle1)

rectangle2 = rectangle1  # nevytvoří kopii, ale odkaz na stejný objekt
print(rectangle2)

rectangle1.a = 5
print(rectangle1)
print(rectangle2)  # rectangle1 i rectangle2 je stejný objekt se dvěmi názvy
rectangle2.b = 6
print(rectangle1)
print(rectangle2)

lst = [1, rectangle1, 3]
copy_lst = lst  # toto vlastně ani není kopie, jen nový název pro stejný seznam
shallow_copy_lst = list(lst)
deep_copy_lst = deepcopy(lst)
print('-'*80)
print(f"lst = {lst}")
print(f"copy_lst = {copy_lst}")
print(f"shallow_copy_lst = {shallow_copy_lst}")
print(f"deep_copy_lst = {deep_copy_lst}")

lst[1].a = 11
print('-'*80)
print(f"lst = {lst}")
print(f"copy_lst = {copy_lst}")
print(f"shallow_copy_lst = {shallow_copy_lst}")
print(f"deep_copy_lst = {deep_copy_lst}")

lst[0] = 20
print('-'*80)
print(f"lst = {lst}")
print(f"copy_lst = {copy_lst}")
print(f"shallow_copy_lst = {shallow_copy_lst}")
print(f"deep_copy_lst = {deep_copy_lst}")
