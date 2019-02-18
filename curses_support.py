import curses
from gameoflife import *
from time import sleep


def display_curses(grd, r=5):
    "Changes given matrix as a dict that contains position and character"
    # r is the shift from 0,0 of screen
    rows = len(grd)
    cols = len(grd[0])    
    output = { }
    for i in range(rows):
        for j in range(cols):
            if grd[i][j]:
                output[(i+r,j+r)] = "O"
            else:
                output[(i+r,j+r)] = "."
    return output


def draw(value, window):
    for (row, col), char in value.items():
        window.addch(row, col, char)


def main(window, grid):
    curses.curs_set(0)
    try:
        while True:
            window.clear()
            gd = display_curses(grid)
            draw(gd, window)
            grid = apply_rules(grid, neighbour_finder(grid))
            window.refresh()
            sleep(0.5)
    except KeyboardInterrupt:
        pass
