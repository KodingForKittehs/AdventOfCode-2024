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


def init(line):
    _id = 0
    files = []
    id_lookup = []
    for i in range(0, len(line), 2):
        file_length = int(line[i])
        lst = []
        for j in range(0, file_length):
            files.append(_id)
            lst.append(len(files) - 1)
        id_lookup.append(lst)
        _id += 1
        if i + 1 < len(line):
            for j in range(0, int(line[i + 1])):
                files.append(None)
    return files, id_lookup


def swap_empties_to_end(files):
    i = 0
    j = len(files) - 1
    while i < j:
        if files[i] is None:
            while files[j] is None:
                j -= 1
            if i < j:
                files[i], files[j] = files[j], files[i]
        i += 1


def checksum(files):
    return sum(i * c for i, c in enumerate(files) if c is not None)


def find_sublist(lst, sublst):
    sub_len = len(sublst)
    for i in range(len(lst) - sub_len + 1):
        if lst[i : i + sub_len] == sublst:
            return i
    return None


def attempt_move(_id, files, id_lookup):
    locs = id_lookup[_id]
    if empty := find_sublist(files, [None] * len(locs)):
        if empty > locs[0]:
            return
        for i in range(len(locs)):
            files[empty + i] = _id
        for i, c in enumerate(locs):
            files[c] = None


def part1(line):
    files, _ = init(line)
    swap_empties_to_end(files)
    return checksum(files)


def part2(line):
    files, id_lookup = init(line)

    for _id in range(len(id_lookup) - 1, -1, -1):
        attempt_move(_id, files, id_lookup)

    return checksum(files)


def solve():
    line = next(nom_file("input"))[0]
    print("Part 1:", part1(line))
    print("Part 2:", part2(line))


solve()
