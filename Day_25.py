# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import collections
import kittehs_funkollection as kf

inp = "input.txt"

locks_and_keys = kf.eat(inp, "")
locks = [item for item in locks_and_keys if item[0][0] == "#"]
keys = [item for item in locks_and_keys if item[0][0] == "."]

print(locks_and_keys)
print(locks)
print(keys)

def try_key(lock, key):
    for lock_row, key in zip(lock, key):
        for lock_char, key_char in zip(lock_row, key):
            if lock_char == "#" and key_char == "#":
                return False
    return True

p1 = 0
for lock in locks:
    for key in keys:
        if try_key(lock, key):
            p1 += 1

print(f"Part 1: {p1}")