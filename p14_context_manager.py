from contextlib import contextmanager

try:
    f = open('new_file.txt', 'w')
    f.write("Hello World")
    print(a)
except NameError:
    print("NameError")
finally:
    f.close()

"""while True:
    pass"""

with open("file.txt", 'w') as f2:
    f2.write("Hello world")
    # zde je pořád soubor otevřený

# zde už soubor je zavřený
"""while True:
    pass"""


# Your own context manager as a class
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # opening and sharing of resources
        print(f"Opening file {self.filename}")
        self.file = open(self.filename, self.mode)
        print(f"File {self.filename} successfully open")
        return self.file

    def __exit__(self, type, value, traceback):
        # cleaning, release of resources
        self.file.close()
        print(f"File {self.filename} successfully closed")
        print(f"type={type}, value={value}, traceback={traceback}")


with FileManager('test.txt', 'w') as f:
    f.write("Test")


# Your own context manager as a function
@contextmanager
def file_manager(filename, mode):
    print(f"Opening file {filename}")
    f = open(filename, mode)
    print(f"File {filename} successfully open")
    yield f
    f.close()
    print(f"File {filename} successfully closed")


print('-'*80)
with file_manager("text.txt", "w") as f:
    print("Writing to file...")
    f.write("Test from context_manager")
    print("... done")
