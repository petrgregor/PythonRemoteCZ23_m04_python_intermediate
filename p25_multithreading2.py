import threading
import time


class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args=(), kwargs=None):
        """if args is None:
            args = ()"""
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args   # [1, 2, 3, 4, 5]
        self.kwargs = kwargs
        self.result = None
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)  # *self.args => 1 2 3 4 5

    def join(self, timeout=None):
        super().join(timeout)
        return self.result


def print_cube(num):
    time.sleep(5)
    print(f"Cube: {num * num * num}")
    return num ** 3


def print_square(num):
    time.sleep(5)
    return num * num


# tato část se spustí pouze v případě, že tento soubor spouštím přímo
# pokud ale tento soubor importuji do jiného souboru, pak se tato část kódu nespustí
if __name__ == "__main__":
    thread1 = ThreadWithReturnValue(target=print_square, args=(10,))
    thread2 = ThreadWithReturnValue(target=print_cube, args=(10,))

    thread1.start()
    thread2.start()

    print(f"print_square: {thread1.join()}")
    print(f"print_cube: {thread2.join()}")

    print("Done!")

