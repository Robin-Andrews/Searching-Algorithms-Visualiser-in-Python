try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True

TITLE = "Breadth First Search on a Grid"
FRAME_WIDTH = 400
FRAME_HEIGHT = 400
DELAY = 2
BG_COLOR = "black"

START_SYMBOL = "S" # not currently used
END_SYMBOL = "E"
OBSTACLE = "#"

frame = simplegui.create_frame(TITLE, FRAME_WIDTH, FRAME_HEIGHT)
frame.set_canvas_background(BG_COLOR)