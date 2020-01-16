import config
from grid import Grid
import helper_functions as helpers

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    simplegui.Frame._hide_status = True


def draw(canvas):
    """
    Default draw handler for the simplegui frame
    """
    # use state to decide what gets shown
    graphical_grid.draw(canvas)

def click(pos):
    i, j =  graphical_grid.get_indices_from_coords(pos)
    graphical_grid._grid[i][j].set_color("green")

### if name ....

state = "begin"
frame = simplegui.create_frame(config.TITLE, config.FRAME_WIDTH, config.FRAME_HEIGHT)
frame.set_canvas_background("black")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)


graphical_grid = Grid(8, 8, 5, "black", "green")

maze = ["........",
        "..*#....",
        "..##....",
        "..##....",
        "..##....",
        "..##....",
        ".....###",
        "......*."]

maze = [list(maze[i]) for i in range(len(maze))]
helpers.display_logical_grid(maze, graphical_grid)
frame.start()
