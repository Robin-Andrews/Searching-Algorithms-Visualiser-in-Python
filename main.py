import config
from grid import Grid

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
    grid.draw(canvas)

def click(pos):
    print(grid.get_indices_from_coords(pos))

### if name ....

state = "begin"
frame = simplegui.create_frame(config.TITLE, config.FRAME_WIDTH, config.FRAME_HEIGHT)
frame.set_canvas_background("black")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)


grid = Grid(8, 8)
frame.start()
