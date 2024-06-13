from math import sqrt

print("Naivní metoda iterování velkým seznamem")
# naivní metoda bez použití iterátoru
def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def get_n_primes(n):
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes


primes_lst = get_n_primes(100)
#print(primes_lst)
for prime in primes_lst:
    #print(prime)
    pass


print('-'*80)
print("Iterátor: PrimeIterator")
# lepší metoda s použitím iterátoru


class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > 2:
            self.number += 2
        else:
            self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        if is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()


prime_iterator = PrimeIterator(10)
print(prime_iterator.__next__())
print(prime_iterator.__next__())
print(prime_iterator.__next__())
print(prime_iterator.__next__())
print(prime_iterator.__next__())
print(prime_iterator.__next__())
for prime in prime_iterator:
    print(prime)
print("Done")


print('-'*80)
print("Iterátor: FibonacciIterator")
"""
Task: Fibonacci number iterator
Vytvořte iterátor, který bude procházet Fibonacciho posoupnost:
1, 1, 2, 3, 5, 8, 13, ....
"""


class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_numbers >= self.n:
            raise StopIteration
        result = self.b
        self.a, self.b = self.b, self.a + self.b
        self.generated_numbers += 1
        return result


fibonacci_iterator = FibonacciIterator(10)
for fib in fibonacci_iterator:
    print(fib)


print('-'*80)
print("Iterátor: PowTwoIterator")
# TODO: PowTwoIterator
"""
Task: PowTwoIterator.
Vytvořte iterátor, který bude iterovat přes druhé mocniny kladných čísel:
1, 4, 9, 16, 25, 36, 49,...
"""


print('-'*80)
print("Iterátor: TriangleNumbersIterator")
# TODO: TriangleNumbersIterator
"""
Task: TriangleNumbersIterator.
https://www.mathsisfun.com/algebra/triangular-numbers.html
1, 3, 6, 10, 15, 27, 28, 36, 45,...
"""

print('-'*80)
print("Iterátor: PerfectNumbersIterator")
# https://en.wikipedia.org/wiki/Perfect_number
# TODO: PerfectNumbersIterator


print('-'*80)
print("Iterátor: DividersIterator")
"""
Iterátor, který prochází všechny dělitele zadaného čísla, např. pro n=12: 1, 2, 3, 4, 6, 12
"""
# TODO: DividersIterator
