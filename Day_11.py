# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
from functools import lru_cache
import re

def find_ints(line):
    return [int(i) for i in re.findall(r"\d+", line)]

def file_as_line(file):
    with open(file, encoding="utf-8") as f:
        return f.readline().strip()

@lru_cache(maxsize=None)
def get_count(stone, blinks):
    if blinks == 1:
        if stone == 0:
            return 1
        if len(str(stone)) % 2 == 0:
            return 2
        return 1

    if stone == 0:
        return get_count(1, blinks - 1)
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        return (
            get_count(int(stone_str[:len(stone_str) // 2]), blinks - 1) +
            get_count(int(stone_str[len(stone_str) // 2:]), blinks - 1)
        )
    return get_count(stone * 2024, blinks - 1)

print(
    sum(
        get_count(ln, 75)
        for ln in find_ints(file_as_line("input"))
    )
)

