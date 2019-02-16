# Blinker is period 2 oscillator pattern

from gameoflife import *
from time import sleep

# This is the initial configuration for blinker:
grid = [ [False, False, False, False, False],
         [False, False, True, False, False],
         [False, False, True, False, False],
         [False, False, True, False, False],
         [False, False, False, False, False] ]

try:
    while True:
        print(display(grid))
        sleep(0.5)
        apply_rules(grid, neighbour_finder(grid))

except KeyboardInterrupt:
    print('interrupted!')
