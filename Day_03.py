# pylint: disable=missing-module-docstring, missing-function-docstring, missing-final-newline, invalid-name
import re

def get_input(file):
    with open(file, encoding="utf-8") as f:
        return f.read()

def clean_input(line):
    line = re.sub(r"don't\(\).*?do\(\)", "x", line, flags=re.DOTALL)
    return re.sub(r"don't\(\).*", "xx", line, flags=re.DOTALL)

def get_mult(line):
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
    return sum(int(match[0]) * int(match[1]) for match in matches)

def solve():
    line = get_input("input")
    res1 = get_mult(line)
    line = clean_input(line)
    res2 = get_mult(line)
    print(f"P1: {res1} P2: {res2}")

solve()
