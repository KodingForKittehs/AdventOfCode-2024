# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
from collections import defaultdict
from itertools import permutations
import numpy as np


def nom_file(file):
    with open(file, encoding="utf-8") as f:
        yield from (line.strip() for line in f.readlines())


def to_grid(lines):
    return list(list(c for c in line) for line in lines)


def get_an(grid, start, end, part):
    diff = end - start
    result = []
    while not is_outside(grid, end):
        result.append(end)
        end = end + diff
    if part == 1:
        return [result[1]] if len(result) > 1 else []
    return result


def get_antinodes(grid, a, b, part):
    return get_an(grid, a, b, part) + get_an(grid, b, a, part)


def is_outside(grid, point):
    return (
        point[0] < 0
        or point[1] < 0
        or point[0] >= len(grid)
        or point[1] >= len(grid[0])
    )


def get_ant_locs(grid):
    ant_locs = defaultdict(list)
    for i, _ in enumerate(grid):
        for j, _ in enumerate(grid[i]):
            if grid[i][j] != ".":
                ant_locs[grid[i][j]].append(np.array([i, j]))
    return ant_locs

def solve():
    grid = to_grid(nom_file("input"))

    anti_p1 = set()
    anti_p2 = set()

    ant_locs = get_ant_locs(grid)
    for key in ant_locs:
        locations = ant_locs[key]

        for a, b in permutations(locations, 2):
            for an in get_antinodes(grid, a, b, 1):
                anti_p1.add(tuple(an))
            for an in get_antinodes(grid, a, b, 2):
                anti_p2.add(tuple(an))

    print(len(anti_p1))
    print(len(anti_p2))


solve()
