from grid import Grid


def display_logical_grid(logical_grid, graphical_grid, color="blue"):
    num_rows, num_cols = graphical_grid.get_dimensions()
    for i in range(num_rows):
        for j in range(num_cols):
            if logical_grid[i][j] == "#":
                graphical_grid._grid[i][j].set_color("blue")



# maze = ["..........",
#         "..*#...##.",
#         "..##...#*.",
#         ".....###..",
#         "......*..."]
#
# maze = [list(maze[i]) for i in range(len(maze))]
# for row in maze:
#     print(row)

