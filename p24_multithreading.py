import threading


def iterate_print(iter):
    for item in iter:
        print(item)


if __name__ == "__main__":
    # bez vláken
    iterate_print([1, 2, 3, 4])
    iterate_print(["a", "b", "c", "d"])

    print("-"*80)

    # pomocí vláken
    # vytvoříme vlákna
    thread1 = threading.Thread(target=iterate_print, args=(range(5),))
    thread2 = threading.Thread(target=iterate_print, args=(["a", "b", "c", "d"],))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("Done!")

