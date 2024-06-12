"""
Context Managers
Task 1

Write a context manager class that will print the run duration of the code that is executed.
"""
import time
from datetime import datetime


class ElapsedTimeManager:
    def __init__(self):
        pass

    def __enter__(self):
        self.start_time = datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Elapsed time: {(datetime.now() - self.start_time).total_seconds()} s")


with ElapsedTimeManager():
    time.sleep(3)
