"""
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
    #if number >= 3:
    #    numbers = numbers[:-1]
    #    print(numbers)
    numbers.append(number)
    print(numbers)
"""
from functools import reduce


def to_lower(sentence_):
    return sentence_.lower()


to_lower_lambda = lambda s: s.lower()

sentence = "HA HA HA"
print(to_lower(sentence))
print(to_lower_lambda(sentence))


def square(x):
    return x ** 2


square_lambda = lambda x: x ** 2

print(f"{square(4)} == {square_lambda(4)}")


def equals(x, y):
    return x == y


equals_lambda = lambda x, y: x == y

print(f"{equals(5, 5)} == {equals_lambda(5, 5)}")
print(f"{equals(5, 3)} == {equals_lambda(5, 3)}")


def multiply(n):
    return lambda x: x * n


multiply2 = multiply(2)
print(f"2 * 11 = {multiply2(11)}")

multiply3 = multiply(3)
print(f"3 * 11 = {multiply3(11)}")

# map
items = [1, 2, 3, 4, 5]


def squared_func(numbers):
    squared_ = []
    for number in numbers:
        squared_.append(number ** 2)
    return squared_


squared1 = squared_func(items)
squared2 = list(map(lambda x: x ** 2, items))
print(f"{squared1} == {squared2}")


# filter
def odds_filter_func(numbers):
    filtered = []
    for number in numbers:
        if number % 2:
            filtered.append(number)
    return filtered


odds1 = odds_filter_func(items)
odds2 = list(filter(lambda x: x % 2, items))
print(f"{odds1} == {odds2}")

even1 = list(filter(lambda x: x % 2 == 0, items))
even2 = list(filter(lambda x: not x % 2, items))
print(f"{even1} == {even2}")

# reduce
items = [1, 2, 3, 4, 5]


def sum_func(numbers):
    result = 0
    for number in numbers:
        result += number
    return result


sum1 = sum_func(items)
sum2 = reduce(lambda x, y: x + y, items)
print(f"{sum1} = {sum2}")

multiply1 = reduce(lambda x, y: x * y, items)
print(multiply1)

odds_squared = list(map(lambda x: x ** 2, list(filter(lambda x: x % 2, items))))
print(odds_squared)

sum_odds_squared = reduce(
    lambda x, y: x + y,
    list(
        map(
            lambda x: x ** 2,
            list(
                filter(
                    lambda x: x % 2,
                    items
                )
            )
        )
    )
)
print(sum_odds_squared)

even_squared = list(map(lambda x: x ** 2, list(filter(lambda x: x % 2 == 0, items))))
print(f"even_squared: {even_squared}")

# sorted
pairs = [(1, 20), (2, 15), (30, 8)]
print(sorted(pairs, key=lambda x: x[1]))

print("min:")
print(min(pairs))
print(min(pairs, key=lambda x: x[1]))
print(min(pairs, key=lambda x: x[0]+x[1]))
print(min(pairs, key=lambda x: x[0]*x[1]))

print("max:")
print(max(pairs))
print(max(pairs, key=lambda x: x[1]))
print(max(pairs, key=lambda x: x[0]+x[1]))
print(max(pairs, key=lambda x: x[0]*x[1]))

print("filter:")
ages = [5, 15, 25, 18, 17, 35, 45, 12]
adults = list(filter(lambda x: x >= 18, ages))
print(f"adults: {adults}")

"""
Lambdas
Task 1

Write a program that uses the filter function to print words which are palindromes in the word list passed. 
A palindrome is an expression that sounds the same when read from both the left and the right side. 
For example, such words are palindromes: radar, level, rotor
"""

words = ['radar', 'pivo', 'LEVEL', 'jelenovipivonelej', 'jelen', 'rotor', 'kobylamamalybok']
palindroms = list(filter(lambda x: x == x[::-1], words))
print(palindroms)

# chceme seznam slov upravit tak, aby každé slovo začínalo velkým písmenem
capitalized_words1 = list(map(lambda x: x.capitalize(), words))
capitalized_words2 = list(map(lambda x: x[0].upper() + x[1:].lower(), words))
print(f"{capitalized_words1} == {capitalized_words2}")

for word in capitalized_words1:
    print(word, end=' ')
print()

list(map(lambda x: print(x, end=' '), capitalized_words1))
print()

jelen = "jelen"
print(f"'{jelen}', '{jelen[::-1]}', '{str(reversed(jelen))}', '{"".join(reversed(jelen))}'")
