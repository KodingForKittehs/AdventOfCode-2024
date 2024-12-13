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


def file_as_grid(file, ctype=str):
    with open(file, encoding="utf-8") as f:
        return list(list(ctype(c) for c in line.strip()) for line in f.readlines())


def file_as_line(file):
    with open(file, encoding="utf-8") as f:
        return f.readline().strip()


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


def find_sublist(lst, sublst):
    sub_len = len(sublst)
    for i in range(len(lst) - sub_len + 1):
        if lst[i : i + sub_len] == sublst:
            return i
    return -1


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


def to_grid(lines, ctype=str):
    return list(list(ctype(c) for c in line) for line in lines)


def is_inside(grid, point):
    return 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0])


dirs_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # E S W N
dirs_8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def get_locs(grid, location, dirs):
    for d in dirs:
        loc = (location[0] + d[0], location[1] + d[1])
        if is_inside(grid, loc):
            yield loc


def find_in_grid(grid, value):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == value:
                yield (i, j)
