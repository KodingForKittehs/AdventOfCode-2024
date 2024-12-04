# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name
def split_file(file):
    with open(file, encoding="utf-8") as f:
        return f.read().splitlines()

to_find = "XMAS"

dirs = [
    (1, 0), # down
    (1, 1), # down right
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1)
]

mas_dirs = [
    (1, 1), # down right
    (-1, 1),
    (-1, -1),
    (1, -1)
]

def check_direction(i, j, d, lines):
    word = ""
    di, dj = d
    while 0 <= j < len(lines[0]) and 0 <= i < len(lines) and len(word) < len(to_find):
        word += lines[i][j]
        i += di
        j += dj
    if word.startswith(to_find):
        return 1
    return 0

def check_location(i, j, lines):
    return sum(check_direction(i, j, d, lines) for d in dirs)

def check_location_mas(i, j, lines):
    ms = ""
    if lines[i][j] == "A":
        for d in mas_dirs:
            di, dj = d
            if 0 <= i + di < len(lines[0]) and 0 <= j + dj < len(lines):
                ms += lines[i + di][j + dj]
        if ms in ["MMSS", "SSMM", "MSSM", "SMMS"]:
            return 1
    return 0

def solve():
    total = 0
    total_mas = 0
    lines = split_file("input")
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            total += check_location(i, j, lines)
            total_mas += check_location_mas(i, j, lines)
    print(total)
    print(total_mas)

solve()
