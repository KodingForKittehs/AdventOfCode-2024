# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import functools
import kittehs_funkollection as kf

inp = "input"
towels, designs = kf.eat(inp, "")
towels = set(towels[0].split(", "))

@functools.lru_cache(maxsize=None)
def can_create_design(design, d_index):
    if d_index == len(design):
        return 1
    
    return sum(
        can_create_design(design, d_index + len(towel))
        for towel in towels
        if design[d_index:d_index + len(towel)] == towel
    )

print(f"Part 1: {sum(can_create_design(design, 0) > 0 for design in designs)}")
print(f"Part 2: {sum(can_create_design(design, 0) for design in designs)}")
