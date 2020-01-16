"""
Grid class - uses Square class
"""

import config
from square import Square


class Grid:
    """This class creates a grid comprised of `Square` objects."""

    def __init__(self, num_rows, num_cols, pen_size=5, pen_color="red", fill_color="blue"):
        """Constructor - creates and instance of Grid."""
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._pen_size = pen_size
        self._pen_color = pen_color
        self._fill_color = fill_color
        self._cell_width = config.FRAME_WIDTH // self._num_cols
        self._cell_height = config.FRAME_HEIGHT // self._num_rows
        self._grid = []
        for i in range(self._num_rows):
            new_row = []
            for j in range(self._num_cols):
                new_row.append(Square(self._cell_width, (j * self._cell_width, i * self._cell_height), self._pen_size,
                                      self._pen_color, self._fill_color))
            self._grid.append(new_row)

    def get_indices_from_coords(self, pos):
        clicked_square_index = None
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                if self._grid[i][j].is_in(pos):
                    clicked_square_index = (i, j)
        return clicked_square_index

    def get_dimensions(self):
        return (self._num_rows, self._num_cols)

    def set_color(i, j, color):
        """"""
        self._grid[i][j].set_color(color)

    def get_color(i, j):
        """"""
        return self._grid[i][j]

    def draw(self, canvas):
        for row in self._grid:
            for square in row:
                square.draw(canvas)

    def __str__(self):
        res = ""
        for row in self._grid:
            for item in row:
                res += str(item) + " "
        return res
