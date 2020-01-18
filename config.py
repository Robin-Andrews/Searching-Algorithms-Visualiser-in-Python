try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True
    simplegui.Frame._keep_timers = False

TITLE = "Breadth First Search on a Grid"
FRAME_WIDTH = 400
FRAME_HEIGHT = 400
DELAY = 1
BG_COLOR = "black"

START_SYMBOL = "S"  # not currently used
END_SYMBOL = "E"
OBSTACLE = "#"

frame = simplegui.create_frame(TITLE, FRAME_WIDTH, FRAME_HEIGHT)
frame.set_canvas_background(BG_COLOR)
