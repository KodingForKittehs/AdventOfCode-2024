# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import heapq
import kittehs_funkollection as kf


def is_inside(loc, n):
    return 0 <= loc[0] < n and 0 <= loc[1] < n

def is_valid(loc, n, fallen_bytes):
    return is_inside(loc, n) and loc not in fallen_bytes

def solve():
    inp = "input"
    if inp == "sample1":
        fallen = 12
        size = 6
    else:
        fallen = 1024
        size = 70
    lines = next(kf.nom_file(inp))
    lines = [kf.find_ints(x) for x in lines]
    n = size + 1

    fallen_bytes = set()
    for line_no in range(0, fallen):
        line = lines[line_no]
        fallen_bytes.add((line[0], line[1]))

    def flood_fill():
        heap = []
        visited = set()
        heapq.heappush(heap, (0, (0, 0)))

        while heap:
            steps, loc = heapq.heappop(heap)
            if loc in visited:
                continue
            visited.add(loc)
            if loc == (n - 1, n - 1):
                return steps
            for d in kf.dirs_4:
                new_loc = (loc[0] + d[0], loc[1] + d[1])
                if is_valid(new_loc, n, fallen_bytes):
                    heapq.heappush(heap, (steps + 1, new_loc))
        return -1

    print(f"Part 1: {flood_fill()}")

    for line_no in range(fallen, len(lines)):
        line = lines[line_no]
        fallen_bytes.add((line[0], line[1]))
        if flood_fill() == -1:
            print(f"Part 2: {line[0]},{line[1]}")
            break

solve()
