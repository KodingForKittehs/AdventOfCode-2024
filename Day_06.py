# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import

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

def find_guard(cat):
    for i, line in enumerate(cat):
        for j, char in enumerate(line):
            if char == "^":
                return (i, j)
    return None

def solve():
    cat = next(nom_file("input"))

    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    guard_dir = 0
    start_pos = find_guard(cat)
    guard_pos = start_pos
    visited = set()
    visited.add(tuple(guard_pos))

    while True:
        guard_step = guard_pos[0] + dirs[guard_dir][0], guard_pos[1] + dirs[guard_dir][1]

        if (
            guard_step[0] < 0
            or guard_step[0] >= len(cat)
            or guard_step[1] < 0
            or guard_step[1] >= len(cat[0])
        ):
            break

        if cat[guard_step[0]][guard_step[1]] == "#":
            guard_dir = (guard_dir + 1) % 4
        else:
            guard_pos = guard_step
            visited.add(tuple(guard_pos))
    print(f"P1: {len(visited)}")

    cnt = 0
    visited.remove(start_pos)
    for v in visited:
        guard_pos = start_pos
        guard_dir = 0

        escape = False
        for _ in range(10000):
            guard_step = guard_pos[0] + dirs[guard_dir][0], guard_pos[1] + dirs[guard_dir][1]

            if (
                guard_step[0] < 0
                or guard_step[0] >= len(cat)
                or guard_step[1] < 0
                or guard_step[1] >= len(cat[0])
            ):
                escape = True
                break

            if cat[guard_step[0]][guard_step[1]] == "#" or tuple(guard_step) == v:
                guard_dir = (guard_dir + 1) % 4
            else:
                guard_pos = guard_step
        if not escape:
            cnt += 1
    print(f"P2: {cnt}")

solve()
