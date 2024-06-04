import math

a = 3
b = [1, 0, 2]
for elem in b:
    if elem != 0:
        result = a / elem
        print(f"Result is: {result}")
    else:
        print("Error: Division by zero")

# print(b[3])  # IndexError: list index out of range

for elem in b:
    try:
        result = a / elem
        print(f"Result is {result}")
    except ZeroDivisionError:
        print("Error: Division by zero")

print('-' * 80)
i = 0
while i < 4:
    try:
        result = a / b[i]
        print(f"Result is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero")
    except IndexError:
        print("Error: list index out of range")
    except:
        print("Error.")
    finally:
        i += 1


print('-'*80)


def divide_old(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero")


def divide(a, b):
    return a / b


def divide_all(a, b_list):
    for elem in b_list:
        try:
            result = divide(a, elem)
            print(f"{a} / {elem} = {result}")
        except TypeError:
            print("Error: TypeError")
        #except ZeroDivisionError:
        #    print("Error: Division by zero")


def main():
    a = 5
    b = [1, 2, 0, -1, "Ahoj"]
    try:
        divide_all(a, b)
    except TypeError:
        print("Error: Division by zero")


try:
    main()
except ZeroDivisionError:
    print("Error: Division by zero")


print((-16)**(1/2))
# print(math.log(-5))  # ValueError

print('-'*80)


def divide(a, b):
    try:
        return a / b
    except TypeError:
        print('Error: Type error')
    except ZeroDivisionError:
        print('Error: Division by zero')


def divide_all(a, b_list):
    i = 0
    while i <= len(b_list):
        try:
            result = divide(a, b_list[i])
            print(f"{a} / {b_list[i]} = {result}")
        except IndexError:
            print('Error: Index error')
        finally:
            i += 1


def main2():
    a = 10
    b = ['a', 1, 0, -5, 'Ahoj']
    divide_all(a, b)


try:
    main2()
except:
    print('Error.')

print('-'*80)


def sqrt(num):
    if num < 0:
        raise ValueError("Square root is not possible to count for negative number.")
    return num**(1/2)


num = -16
try:
    print(f"sqrt({num}) = {sqrt(num)}")
except ValueError:
    print("ERROR: Square root is not possible to count for negative number.")

print("done")
