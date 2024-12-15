# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import itertools
import kittehs_funkollection as kf

def can_move(grid, pos, direction):
    item = grid[pos[0]][pos[1]]
    if item == ".":
        return True
    if item == "#":
        return False
    if item == "@":
        return can_move(grid, (pos[0] + direction[0], pos[1] + direction[1]), direction)

    if item == "[":
        if direction[1] == 0:
            return (
                can_move(grid, (pos[0] + direction[0], pos[1] + direction[1]), direction)
                and can_move(grid, (pos[0] + direction[0], pos[1] + 1 + direction[1]), direction)
            )
        return can_move(grid, (pos[0] + direction[0], pos[1] + 1 + direction[1]), direction)
                        
    if item == "]":
        if direction[1] == 0:
            return (
                can_move(grid, (pos[0] + direction[0], pos[1] + direction[1]), direction)
                and can_move(grid, (pos[0] + direction[0], pos[1] - 1 + direction[1]), direction)
            )
        return can_move(grid, (pos[0] + direction[0], pos[1] - 1 + direction[1]), direction)
    return False

def try_move(grid, pos, direction):
    item = grid[pos[0]][pos[1]]
    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if grid[new_pos[0]][new_pos[1]] == "#":
        return False
    if grid[new_pos[0]][new_pos[1]] != ".":
        if grid[new_pos[0]][new_pos[1]] == "]" and direction[1] == 0:
            try_move(grid, (new_pos[0], new_pos[1] - 1), direction)
        if grid[new_pos[0]][new_pos[1]] == "[" and direction[1] == 0:
            try_move(grid, (new_pos[0], new_pos[1] + 1), direction)
        attempt = try_move(grid, new_pos, direction)
        if not attempt:
            return False
    grid[pos[0]][pos[1]] = "."
    grid[new_pos[0]][new_pos[1]] = item
    return True

def count_boxes(grid):
    count = 0
    for box in kf.find_in_grid(grid, "O"):
        count += 100 * box[0] + box[1]
    for box in kf.find_in_grid(grid, "["):
        count += 100 * box[0] + box[1]
    return count

def widen_grid(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for item in row:
            match (item):
                case "#":
                    new_row.append("#")
                    new_row.append("#")
                case ".":
                    new_row.append(".")
                    new_row.append(".")
                case "@":
                    new_row.append("@")
                    new_row.append(".")
                case "O":
                    new_row.append("[")
                    new_row.append("]")
                case _:
                    new_row.append(item)
        new_grid.append(new_row)
    return new_grid

def solve():
    inp = "input"
    grid, moves = kf.eat(inp, "")
    grid = kf.to_grid(grid)
    grid2 = widen_grid(grid)
    moves = list(itertools.chain(*moves))
    robot = next(kf.find_in_grid(grid, "@"))
    robot2 = next(kf.find_in_grid(grid2, "@"))
    move_map = {
        "^": (-1, 0),
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1)
    }

    for move in moves:
        direction = move_map.get(move)
        if try_move(grid, robot, direction):
            robot = (robot[0] + direction[0], robot[1] + direction[1])
        if can_move(grid2, robot2, direction):
            try_move(grid2, robot2, direction)
            robot2 = (robot2[0] + direction[0], robot2[1] + direction[1])

    p1 = count_boxes(grid)
    p2 = count_boxes(grid2)
    print(f"P1: {p1}")
    print(f"P2: {p2}")

solve()