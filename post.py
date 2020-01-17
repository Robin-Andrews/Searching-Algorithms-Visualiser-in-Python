import time

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True

TITLE = "TEST"
FRAME_WIDTH = 400
FRAME_HEIGHT = 400
DELAY = 1


class Square:
    """This class represents a simple Square object."""

    def __init__(self, size, pos, pen_size=2, pen_color="red", fill_color="blue"):
        """Constructor - create an instance of Square."""
        self._size = size
        self._pos = pos
        self._pen_size = pen_size
        self._pen_color = pen_color
        self._fill_color = fill_color

    def set_color(self, color):
        self._fill_color = color

    def get_color(self):
        return self._fill_color

    def is_in(self, pos):
        """
        Determine whether coordinates are within the area of this Square.
        """
        return self._pos[0] < pos[0] < self._pos[0] + self._size and self._pos[1] < pos[1] < self._pos[1] + self._size

    def draw(self, canvas):
        """
        calls canvas.draw_image() to display self on canvas.
        """
        points = [(self._pos[0], self._pos[1]), (self._pos[0] + self._size, self._pos[1]),
                  (self._pos[0] + self._size, self._pos[1] + self._size), (self._pos[0], self._pos[1] + self._size)]
        canvas.draw_polygon(points, self._pen_size, self._pen_color, self._fill_color)

    def __str__(self):
        return "Square: {}".format(self._pos)


def tick():
    global cur_time, index
    cur_time += 1
    if cur_time == DELAY:
        print(cur_time)
        squares[index].set_color("green")
        cur_time = 0
        index += 1



def draw(canvas):
    for square in squares:
        square.draw(canvas)





timer = simplegui.create_timer(1000, tick)
frame = simplegui.create_frame(TITLE, FRAME_WIDTH, FRAME_HEIGHT)
frame.set_draw_handler(draw)

width = 20
squares = []
for i in range(10):
    squares.append(Square(width, (i * width, 0)))

index = 0
cur_time = 0
timer.start()
frame.start()

