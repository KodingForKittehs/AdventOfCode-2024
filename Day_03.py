# pylint: disable=missing-module-docstring, missing-function-docstring, missing-final-newline
import re

def get_input(file):
    with open(file, encoding="utf-8") as f:
        return f.read()

def clean_input(line):
    while r := re.findall(r"don't\(\).*?do\(\)", line, re.DOTALL):
        line = line.replace(r[0], "xx")

    line = re.sub(r"don't\(\).*", "xx", line, re.DOTALL)
    return line

def solve():
    line = get_input("input")

    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
    res1 = sum(int(match[0]) * int(match[1]) for match in matches)

    line = clean_input(line)
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)

    res2 = sum(int(match[0]) * int(match[1]) for match in matches)
    print(f"P1: {res1} P2: {res2}")

solve()
