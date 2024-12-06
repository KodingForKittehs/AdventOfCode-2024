# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring
import re
import time

class Timer:
    def __init__(self, label=""):
        self.start = 0
        self.end = 0
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f"Time taken {self.label}: {self.end - self.start}")

def find_ints(line):
    return [int(i) for i in re.findall(r'\d+', line)]
