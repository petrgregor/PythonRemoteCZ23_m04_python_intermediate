import time
from datetime import datetime


def disable_at_night(func):
    # a decorator that only calls a decorated function during the day
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()

    return wrapper


@disable_at_night
def say_something():
    print("Hello world")


say_something()


def elapsed_time(func):
    def wrapper():
        time_start = datetime.now()
        print(f"Starting 'my_function' at {time_start.strftime("%H:%M:%S")}")
        func()
        time_end = datetime.now()
        print(f"Ending 'my_function' at {time_end.strftime("%H:%M:%S")}")
        print(f"Elapsed time: {time_end - time_start}")

    return wrapper


@elapsed_time
def my_function():
    print("Inside my_function")
    time.sleep(2)  # simulujeme náročnou výpočetní činnost


my_function()


"""
class MyDateTime:
    def __init__(self, day, month, year, hour, minute, second):
        self.day = day
        self.mon
"""


def run_only_between(from_=7, to_=22):
    # a decorator that only calls a decorated function at certain times
    def dec(func):
        def wrapper():
            if from_ <= datetime.now().hour < to_:
                func()

        return wrapper

    return dec


@run_only_between(9, 15)
def say_something2():
    print("Hello world from say_something2")


say_something2()


def elapsed_time2(debug=False):
    def dec(func):
        def wrapper():
            if debug:
                time_start = datetime.now()
                print(f"Starting 'my_function2' at {time_start}")
            func()
            if debug:
                time_end = datetime.now()
                print(f"Ending 'my_function2' at {time_end}")
                print(f"Elapsed time: {time_end - time_start}")

        return wrapper

    return dec


DEBUG = False


@elapsed_time2(DEBUG)
def my_function2():
    print("Inside my_function2")
    time.sleep(2)  # simulujeme náročnou výpočetní činnost


print('-'*80)
my_function2()
