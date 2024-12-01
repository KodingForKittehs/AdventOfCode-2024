# pylint: disable=missing-module-docstring, missing-function-docstring, missing-final-newline

def split_file(file):
    with open(file, encoding="utf-8") as f:
        return f.read().splitlines()

def solve():
    lines = split_file("input")
    list_1, list_2 = [], []

    for line in lines:
        a, b = line.split("   ")
        list_1.append(int(a))
        list_2.append(int(b))
    list_1 = sorted(list_1)
    list_2 = sorted(list_2)

    result1 = 0
    result2 = 0
    for (i, j) in zip(list_1, list_2):
        result1 += abs(i - j)
        first_in_second = list_2.count(i)
        result2 += i * first_in_second

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")

solve()
