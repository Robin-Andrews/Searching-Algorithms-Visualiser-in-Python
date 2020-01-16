"""
Generic Square Class
"""


class Square:
    """This class represents a simple Square object."""

    def __init__(self, size, pos, pen_size=5, pen_color="red", fill_color="blue"):
        """Constructor - create an instance of Square."""
        self._size = size
        self._pos = pos
        self._pen_size = pen_size
        self._pen_color = pen_color
        self._fill_color = fill_color

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