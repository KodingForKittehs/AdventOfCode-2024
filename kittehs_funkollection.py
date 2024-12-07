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
    return [int(i) for i in re.findall(r"\d+", line)]


def nom_file(file, split_on=None):
    with open(file, encoding="utf-8") as f:
        res = []
        for line in (line.strip() for line in f.readlines()):
            if split_on is not None and line == split_on:
                yield res
                res = []
            else:
                res.append(line)
        yield res


def eat(file, split_on=None):
    if split_on is None:
        try:
            return next(nom_file(file))
        except FileNotFoundError:
            return next(nom_file("sample"))
    else:
        try:
            return list(nom_file(file, split_on))
        except FileNotFoundError:
            return list(nom_file("sample", split_on))

def to_grid(lines):
    return list(list(c for c in line) for line in lines)
