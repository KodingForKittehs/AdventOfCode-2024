# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import re

def find_ints(line):
    return [int(i) for i in re.findall(r"\d+", line)]


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


def recurse(nums, use_extra_ops):
    if len(nums) == 1:
        return [nums[0]]
    end = nums[-1]
    front = recurse(nums[0:-1], use_extra_ops)
    res = [i + end for i in front] + [i * end for i in front]
    if use_extra_ops:
        res += [int(str(i) + str(end)) for i in front]
    return res


def check_test_value(expect, nums, use_extra_ops):
    return expect if expect in recurse(nums, use_extra_ops) else 0


def solve():
    lines = next(nom_file("input"))
    lines = [find_ints(line) for line in lines]
    p1 = sum(check_test_value(line[0], line[1:], False) for line in lines)
    p2 = sum(check_test_value(line[0], line[1:], True) for line in lines)
    print(f"P1: {p1} P2: {p2}")


solve()
