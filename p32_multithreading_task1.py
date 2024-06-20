"""
Task 1

Write a program that sorts the numbers using the SleepSort algorithm.

NOTE: This algorithm is a curiosity, it is neither a reliable nor a efficient solution!

It consists of using the sleep () function.

For each of these numbers, we create a separate thread and put it to sleep using the sleep function.
We do this for a time proportional to the value of the number.
It is known that the thread that has been dormant for the shortest amount of time, i.e.
the thread with the smallest number, will finish executing the fastest.
After the sleep function, these numbers can be added to the collection thus obtaining a sorting effect.
"""
import threading
from time import sleep


def sleep_sort(number_):
    sleep(number_ * 0.01)
    sorted_numbers.append(number_)


"""Task 1a

The above program sorts the numbers in ascending order. Modify the code to sort numbers in descending order.
"""
def sleep_sort_desc(number_, max_number_):
    sleep((max_number_ - number_ + 1) * 0.01)
    sorted_numbers_desc.append(number_)


if __name__ == "__main__":
    numbers_to_sort = [4, 2, 6, 9, 3, 1, 5, 12, 25, 1]

    sorted_numbers = []
    sorted_numbers_desc = []
    threads = []

    for number in numbers_to_sort:
        thread = threading.Thread(target=sleep_sort, args=(number,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"sorted numbers: {sorted_numbers}")

    threads = []
    max_number = max(numbers_to_sort)
    for number in numbers_to_sort:
        thread = threading.Thread(target=sleep_sort_desc, args=(number, max_number,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"descending numbers: {sorted_numbers_desc}")
