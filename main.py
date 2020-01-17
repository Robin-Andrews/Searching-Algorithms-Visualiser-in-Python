import config
from grid import Grid
import helper_functions as helpers
import search
import time


def draw(canvas):
    """
    Default draw handler for the simplegui frame
    """
    # use state to decide what gets shown
    graphical_grid.draw(canvas)


def click(pos):
    i, j = graphical_grid.get_indices_from_coords(pos)
    graphical_grid._grid[i][j].set_color("green")


### if name ....

state = "begin"
# frame = simplegui.create_frame(config.TITLE, config.FRAME_WIDTH, config.FRAME_HEIGHT)
config.frame.set_canvas_background("black")
config.frame.set_draw_handler(draw)
config.frame.set_mouseclick_handler(click)

rows = 10
cols = 12
graphical_grid = Grid(rows, cols, 1, "black", "green")


maze = [[0] * cols for i in range(rows)]
maze[0][0] = "S"
maze[rows - 1][cols - 1] = "E"

maze = [list(maze[i]) for i in range(len(maze))]
helpers.display_logical_grid(maze, graphical_grid)
path = search.bfs(maze, (0, 0), graphical_grid)
print(path)
config.frame.start()
