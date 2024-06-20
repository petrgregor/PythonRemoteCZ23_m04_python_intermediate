import timeit


def linear_search(lst_, to_find_):
    for index, item in enumerate(lst_):
        if item == to_find_:
            return index
        elif item > to_find_:
            return None
    return None


print(linear_search([1, 10, 100, 150, 200], 1))


def binary_search(lst_, to_find_):
    lower = 0
    upper = len(lst_)-1
    middle = int((lower+upper)/2)
    while upper-lower > 1:
        if lst_[middle] == to_find_:
            return middle
        elif lst_[middle] > to_find_:
            middle, upper = int((lower+middle)/2), middle
        else:
            middle, lower = int((middle+upper)/2), middle
    return None


if __name__ == "__main__":
    setup = '''
from __main__ import linear_search, binary_search
import random
lst = sorted([random.randint(0, 1000000) for _ in range(100000)])
to_find = random.randint(0, 1000000)
    '''

    linear_search_code = '''
result = linear_search(lst, to_find)
    '''

    binary_search_code = '''
result = binary_search(lst, to_find)
    '''

    print(timeit.timeit(stmt=linear_search_code,
                        setup=setup,
                        number=1000))
    print(timeit.timeit(stmt=binary_search_code,
                        setup=setup,
                        number=1000))
