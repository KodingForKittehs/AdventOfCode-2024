# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import heapq
import kittehs_funkollection as kf
inp = "input"
grid = kf.file_as_grid(inp)

kf.print_grid(grid)
start = next(kf.find_in_grid(grid, "S"))
end = next(kf.find_in_grid(grid, "E"))
print(start)

queue = [(0, (start, 0))]
visited = {}

while queue:
    dist, (pos, dir) = heapq.heappop(queue)
    if (pos, dir) in visited:
        if visited[(pos, dir)] < dist:
            continue
    visited[(pos, dir)] = dist
    if pos == end:
        print(dist)
        break
    x, y = pos
    for i, (dx, dy) in enumerate(kf.dirs_4):
        new_pos = (x + dx, y + dy)
        if grid[new_pos[0]][new_pos[1]] == "#":
            continue
        if i == dir:
            heapq.heappush(queue, (dist + 1, (new_pos, i)))
        elif i == (dir + 1) % 4 or i == (dir - 1) % 4:
            heapq.heappush(queue, (dist + 1001, (new_pos, i)))