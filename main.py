#!/usr/bin/env python3

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import collections

import config
from grid import Grid
import helper_functions as helpers


def tick():
    global maze, graphical_maze, cur_time, bfs_queue, visited_positions, num_rows, num_cols, program_state
    print("Begin tick()")
    cur_time += 1
    if cur_time == config.DELAY:
        if program_state == "do_bfs":
            if bfs_queue:
                path = bfs_queue.popleft()
                i, j = path[-1]
                if maze[i][j] == "E":
                    program_state = "finished"
                for i2, j2 in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):  # Down, up, right, left
                    if (0 <= i2 < num_rows and 0 <= j2 < num_cols and maze[i2][j2] != "#" and
                            (i2, j2) not in visited_positions):
                        bfs_queue.append(path + [(i2, j2)])
                        if maze[i2][j2] != "E":
                            graphical_maze._grid[i2][j2].set_color("orange")
                        print("Visiting", (i2, j2))
                        visited_positions.add((i2, j2))
                        cur_time = 0

                        break  # FIXME! Added to avoid more than one movement in one tick.
                               #        But maybe/probably not the good correction.


def draw(canvas):
    """
    Default draw handler for the simplegui frame
    """
    global graphical_maze
    # use state to decide what gets shown
    if graphical_maze:
        graphical_maze.draw(canvas)


def click(pos):
    i, j = graphical_maze.get_indices_from_coords(pos)
    graphical_maze._grid[i][j].set_color("green")


def start():
    global program_state, timer
    timer.start()
    program_state = "do_bfs"


def reset():
    global maze, graphical_maze, program_state, cur_time, bfs_queue, visited_positions, num_rows, num_cols, timer
    timer.stop()
    program_state = "start"
    cur_time = 0

    # Create logical maze
    num_rows = 10
    num_cols = 5
    maze = [[0] * num_cols for i in range(num_rows)]
    maze[0][0] = "S"
    maze[num_rows - 1][num_cols - 1] = "E"

    # Create graphical maze
    graphical_maze = Grid(num_rows, num_cols, 1, "black", "green")

    # Display graphical maze
    helpers.display_logical_grid(maze, graphical_maze)

    # BFS setup
    bfs_queue = collections.deque([[(0, 0)]])
    visited_positions = set([(0, 0)])


def main():
    """
    Set GUI handlers and initialise GUI and timer
    """
    global graphical_maze, timer, cur_time
    cur_time = 0
    graphical_maze = None

    config.frame.set_draw_handler(draw)
    # config.frame.set_mouseclick_handler(click)
    start_button = config.frame.add_button("Start", start, 60)  # FIXME! unused variable
    reset_button = config.frame.add_button("Reset", reset, 60)  # FIXME! unused variable
    timer = simplegui.create_timer(1000, tick)

    reset()
    config.frame.start()


if __name__ == "__main__":
    main()
