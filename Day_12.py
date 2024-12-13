# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import shapely


def file_as_grid(file, ctype=str):
    with open(file, encoding="utf-8") as f:
        return list(list(ctype(c) for c in line.strip()) for line in f.readlines())


grid = file_as_grid("input")


def get_locs(location):
    for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        loc = (location[0] + d[0], location[1] + d[1])
        if is_inside(loc):
            yield loc


def is_inside(point):
    return 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0])


def count_90degree_turns(ring):
    count = 0
    coords = []
    for i in range(len(ring.coords) - 1):
        coords.append(ring.coords[i])

    for i, _ in enumerate(coords):
        i2 = (i + 2) % len(coords)
        if coords[i][0] != coords[i2][0] and coords[i][1] != coords[i2][1]:
            count += 1

    return count


def get_sides(poly):
    return sum(
        count_90degree_turns(line) for line in poly.interiors
    ) + count_90degree_turns(poly.exterior)


def get_price(i, j, visit):
    to_check = [(i, j)]
    plant = grid[i][j]
    poly = shapely.geometry.Polygon()

    while to_check:
        nxt = to_check.pop()
        if nxt in visit:
            continue

        if is_inside(nxt) and grid[nxt[0]][nxt[1]] == plant:
            visit.add(nxt)
            poly = poly.union(
                shapely.geometry.Polygon(
                    [
                        (nxt[0], nxt[1]),
                        (nxt[0] + 1, nxt[1]),
                        (nxt[0] + 1, nxt[1] + 1),
                        (nxt[0], nxt[1] + 1),
                    ]
                )
            )
            to_check.extend(get_locs(nxt))
    return poly.area * poly.length, poly.area * get_sides(poly)


def solve():
    visit = set()
    p1sum = p2sum = 0
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if (i, j) in visit:
                continue
            p1, p2 = get_price(i, j, visit)
            p1sum += p1
            p2sum += p2
    print(f"P1: {int(p1sum)}")
    print(f"P2: {int(p2sum)}")


solve()
