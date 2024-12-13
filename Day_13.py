# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import functools
import re

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

def find_ints(line):
    return [int(i) for i in re.findall(r"\d+", line)]

@functools.lru_cache(maxsize=None)
def get_min_cost_memoized(curr, a, b, prize):
    if curr == prize:
        return 0
    if curr[0] > prize[0] or curr[1] > prize[1]:
        return float("inf")
    
    cost_a = 3 + get_min_cost_memoized((curr[0]+a[0], curr[1]+a[1]), a, b, prize)
    cost_b = 1 + get_min_cost_memoized((curr[0]+b[0], curr[1]+b[1]), a, b, prize)

    return min(cost_a, cost_b)

def get_min_cost_lin_alg(a, b, prize):
    # Cramer's rule
    D = a[0] * b[1] - a[1] * b[0]
    Dx = prize[0] * b[1] - prize[1] * b[0]
    Dy = a[0] * prize[1] - a[1] * prize[0]
    if Dx % D != 0 or Dy % D != 0:
        return float("inf")
    x = Dx / D
    y = Dy / D
    return 3 * x + y

def solve():
    p1 = p2 = 0
    sections = list(nom_file("input", ""))

    for section in sections:
        a = tuple(find_ints(section[0]))
        b = tuple(find_ints(section[1]))
        prize = tuple(find_ints(section[2]))
        p2z = 10000000000000
        prize2 = (prize[0] + p2z, prize[1] + p2z)

        cost = get_min_cost_memoized((0, 0), a, b, prize)
        cost2 = get_min_cost_lin_alg(a, b, prize2)
        if cost != float("inf"):
            p1 += cost
        if cost2 != float("inf"):
            p2 += cost2

    print(p1)
    print(int(p2))

solve()