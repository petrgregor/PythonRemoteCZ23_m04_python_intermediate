import re

task1 = """
Task 1
Extract all numbers from the given text using regular expressions.
i.e., for the "test43543lfdsfdsfl534543fdgl432fr" it will be:

    43543
    534543
    432
"""

print(task1)
text = "test43543lfdsfdsfl534543fdgl432fr"
pattern = r"\d+"
match = re.findall(pattern, text)
print(match)
for elem in match:
    print(elem)

print("-"*80)

task1a = """
Task 1a
Take the same text as in the exercise above 
and write a program using regular expressions that will remove all numbers 
from the text."""

print(task1a)

print(re.sub(pattern, "", text))  # FIXME

print('-'*80)
task2 = """
Task 2
Write a program that uses regular expressions 
to check whether the given telephone number is correct.

The correct numbers are:
    48123456789
    +48123456789
    0048123456789

At the beginning use either 48, +48 or 0048, and then 9 digits."""

print(task2)

#numbers = ['48123456789', '+48123456789', '0048123456789', '4564', '+42011122233']
numbers = '48123456789,+48123456789,0048123456789,4564,+42011122233'
pattern = r"(\+|00)?48\d{9}"

for number in numbers.split(","):
    print(f"{number}: {bool(re.fullmatch(pattern, number))}")

print('Pomocí lambda:')
list(map(lambda x: print(f"{x}: {bool(re.fullmatch(pattern, x))}"), numbers.split(",")))

print('-'*80)
task3a = """
Task 3a:
Pomocí regulárního výrazu rozhodněte, zda je zadané číslo dělitelné 10.
"""
print(task3a)


print('-'*80)
task3b = """
Task3b:
Pomocí regulárního výrazu rozhodněte, zda je zadané číslo sudé.
"""


task4 = """
Task 
Pomocí regulárního výrazu ověřte, zda je zadané číslo platným rodným číslem.
Dělitelnost číslem 11 nelze řešit regulárním výrazem, to musíme v Pythonu.
"""
