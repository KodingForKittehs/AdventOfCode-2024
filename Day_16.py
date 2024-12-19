# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import heapq
import kittehs_funkollection as kf

inp = "input"
grid = kf.file_as_grid(inp)
start = next(kf.find_in_grid(grid, "S"))
end = next(kf.find_in_grid(grid, "E"))

def plug_dead_ends():
    filled = True
    while filled:
        filled = False
        for i, (x, y) in enumerate(kf.find_in_grid(grid, ".")):
            if grid[x][y] != ".":
                continue
            hash_count = 0
            for dx, dy in kf.dirs_4:
                new_pos = (x + dx, y + dy)
                if grid[new_pos[0]][new_pos[1]] == "#":
                    hash_count += 1
            if hash_count >= 3:
                filled = True
                grid[x][y] = "#"

def get_min_dist(start, end, end_dir, max_dist=1000000):
    queue = [(0, start)]
    visited = {}

    while queue:
        dist, (pos, dirn) = heapq.heappop(queue)
        if dist > max_dist:
            continue
        if (pos, dirn) in visited:
            if visited[(pos, dirn)] < dist:
                continue
        visited[(pos, dirn)] = dist
        if (pos, dirn) == (end, end_dir):
            return dist
        x, y = pos
        for i, (dx, dy) in enumerate(kf.dirs_4):
            new_pos = (x + dx, y + dy)
            if grid[new_pos[0]][new_pos[1]] == "#":
                continue
            if i == dirn:
                heapq.heappush(queue, (dist + 1, (new_pos, i)))
            elif i == (dirn + 1) % 4 or i == (dirn - 1) % 4:
                heapq.heappush(queue, (dist + 1001, (new_pos, i)))
    return -1

def solve():
    plug_dead_ends()
    from_south = get_min_dist((start, 0), end, 3)
    from_west = get_min_dist((start, 0), end, 0)

    if from_south != -1 and from_south < from_west:
        p1 = from_south
        end_dir = 3
    else:
        p1 = from_west
        end_dir = 0

    print("Part 1:", p1)
 
    seats = set()
    for i, loc in enumerate(kf.find_in_grid(grid, ".")):
        for d in range(4):
            first = get_min_dist((start, 0), loc, d, p1)
            if first == -1 or first > p1:
                continue
            second = get_min_dist((loc, d), end, end_dir, p1 - first)
            if first != -1 and second != -1 and first + second == p1:
                seats.add(loc)
    print("Part 2:", len(seats) + 2)

solve()