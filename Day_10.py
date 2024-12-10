# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import


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


def to_grid(lines):
    return list(list(int(c) for c in line) for line in lines)


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_inside(grid, point):
    return 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0])


def get_score(grid, point):
    to_visit = [point]
    end_set = set()
    rating = 0
    while to_visit:
        current = to_visit.pop()
        current_elevation = grid[current[0]][current[1]]

        new_branches = 0
        for d in dirs:
            new_point = (current[0] + d[0], current[1] + d[1])
            if (
                is_inside(grid, new_point) 
                and grid[new_point[0]][new_point[1]] == current_elevation + 1
            ):
                new_branches += 1
                if current_elevation == 8:
                    end_set.add(new_point)
                else:
                    to_visit.append(new_point)
        if new_branches > 1:
            rating += new_branches - 1
        if new_branches == 0:
            rating -= 1
            
    return len(end_set), rating + 1

def solve():
    line = next(nom_file("input"))
    grid = to_grid(line)

    total = 0
    totalr = 0
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == 0:
                s, r = get_score(grid, (i, j))
                total += s
                totalr += r
    print(total)
    print(totalr)

solve()

