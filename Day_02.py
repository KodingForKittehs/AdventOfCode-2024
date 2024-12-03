# pylint: disable=missing-module-docstring, missing-function-docstring, missing-final-newline
from itertools import pairwise

def split_file(file):
    with open(file, encoding="utf-8") as f:
        return f.read().splitlines()

def is_safe(levels):
    diffs = [j - i for i, j in pairwise(levels)]

    for diff in diffs:
        if abs(diff) < 1 or abs(diff) > 3:
            return False

    return all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)

def is_report_or_removed_level_safe(levels):
    if is_safe(levels):
        return True

    for i in range(len(levels)):
        report_with_level_i_removed = levels[:i] + levels[i + 1:]
        if is_safe(report_with_level_i_removed):
            return True
    return False

def solve():
    lines = split_file("input")
    p1_safe = p2_safe = 0

    for report in lines:
        levels = [int(item) for item in report.split()]
        if is_safe(levels):
            p1_safe += 1
        if is_report_or_removed_level_safe(levels):
            p2_safe += 1
    print(f"P1: {p1_safe} P2: {p2_safe}")

solve()
