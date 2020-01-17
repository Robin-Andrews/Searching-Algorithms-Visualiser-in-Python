"""
Based on solution from https://stackoverflow.com/a/47902476/3042018
"""

import config
import collections
import time


def bfs(grid, start, graphical_grid):
    height, width = len(grid), len(grid[0])
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == "E":
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != "#" and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                if grid[y2][x2] != "E":
                    graphical_grid._grid[y2][x2].set_color("orange")
                seen.add((x2, y2))

# wall, clear, goal = "#", ".", "*"
# width, height = 10, 5
# grid = ["..........",
#         "..*#...##.",
#         "..##...#*.",
#         ".....###..",
#         "......*..."]
# path = bfs(grid, (5, 2))
# print(path)
# [(5, 2), (4, 2), (4, 3), (4, 4), (5, 4), (6, 4)]
