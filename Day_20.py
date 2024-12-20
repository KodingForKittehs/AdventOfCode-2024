# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import collections
import kittehs_funkollection as kf

inp = "input"
grid = kf.file_as_grid(inp)
distance = {}

def is_valid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != "#"

def get_manhatten_locations(center, size):
    for loc in kf.get_manhatten_locs(size):
        if is_valid(center[0] + loc[0], center[1] + loc[1]):
            yield (center[0] + loc[0], center[1] + loc[1])

def find_path(start, end):
    q = collections.deque([(start, 0)])
    visited = set()
    while q:
        (x, y), dist = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        distance[(x, y)] = dist
        if (x, y) == end:
            return dist
        for dx, dy in kf.dirs_4:
            if is_valid(x + dx, y + dy):
                q.append(((x + dx, y + dy), dist + 1))
    return -1

def get_cheats(size):
    cheats = collections.Counter()
    for (x, y), dist in distance.items():
        node = (x, y)
        for cheat_len in range(1, size):
            for node2 in get_manhatten_locations(node, cheat_len + 1):
                cheat_distance = dist + (len(distance) - distance[node2]) + cheat_len
                cheats[len(distance) - 1 - cheat_distance] += 1
    return sum(cheats[ch] for ch in cheats if 100 <= ch)


def solve():
    start = next(kf.find_in_grid(grid, "S"))
    end = next(kf.find_in_grid(grid, "E"))

    find_path(start, end)
    print(f"Part 1: {get_cheats(2)}")
    print(f"Part 2: {get_cheats(20)}")

solve()