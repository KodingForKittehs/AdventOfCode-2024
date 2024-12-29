# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import collections
import kittehs_funkollection as kf
inp = "input.txt"
lines = [int(line) for line in kf.eat(inp)]

print(lines)

def mix(a, secret):
    return a ^ secret

def prune(secret):
    return secret % 16777216

def generate_secret(secret, n):
    r1 = secret
    for i in range(n):
        r1 = mix(r1 * 64, r1)
        r1 = prune(r1)

        r1 = mix(r1 // 32, r1)
        r1 = prune(r1)

        r1 = mix(r1 * 2048, r1)
        r1 = prune(r1)
    return r1


p1 = 0
for secret in lines:
    print(generate_secret(secret, 2000))
    p1 += generate_secret(secret, 2000)

print(f"Part 1: {p1}")
