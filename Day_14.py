# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import re

w, h, = 101, 103
pos = 0
vel = 1

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
        return next(nom_file(file))
    return list(nom_file(file, split_on))

def find_ints(line):
    return [int(i) for i in re.findall(r"-*\d+", line)]

def print_grid(grid):
    for row in grid:
        print("".join(row))

def find_sublist(lst, sublst):
    sub_len = len(sublst)
    for i in range(len(lst) - sub_len + 1):
        if lst[i : i + sub_len] == sublst:
            return i
    return -1

def has_a_tree(grid):
    for row in grid:
        if find_sublist(row, ["#"] * 8) >= 0:
            return True
    return False

def get_grid(positions):
    grid = [["." for _ in range(w)] for _ in range(h)]
    for r in positions:
        grid[r[1]][r[0]] = "#"
    return grid

def print_bots(positions):
    print_grid(get_grid(positions))

def move(robots, times=1):
    result = []
    for r in robots:
        position = [r[pos][0], r[pos][1]]
        velocity = r[vel]
        position[0] += velocity[0] * times
        position[1] += velocity[1] * times
        position[0] = position[0] % w
        position[1] = position[1] % h
        result.append(position)
    return result

def safety_factor(positions):
    quads = [0] * 4
    for position in positions:
        if 0 <= position[0] < w // 2 and 0 <= position[1] < h // 2:
            quads[0] += 1
        elif w // 2 < position[0] < w and 0 <= position[1] < h // 2:
            quads[1] += 1
        elif w // 2 < position[0] < w and h // 2 < position[1] < h:
            quads[2] += 1
        elif 0 <= position[0] < w // 2 and h // 2 < position[1] < h:
            quads[3] += 1
    return quads[0] * quads[1] * quads[2] * quads[3]

def solve():
    lines = eat("input")
    robots = []

    for line in lines:
        p0, p1, v0, v1 = find_ints(line)
        robots.append(((p0, p1), (v0, v1)))

    p1 = safety_factor(move(robots, 100))
    print(f"P1: {p1}")

    for i in range(100000):
        postions = move(robots, i)
        if has_a_tree(get_grid(postions)):
            print(f"P2: {i}")
            break

solve()