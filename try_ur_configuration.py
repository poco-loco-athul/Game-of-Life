from gameoflife import *
from time import sleep

# Try your intial configuration in the grid
# False is dead; True is alive

grid = [ [False, False, False, False, False],
         [False, False, True, False, False],
         [False, True, True, True, False],
         [False, False, True, False, False],
         [False, False, False, False, False] ]

try:
    while True:
        print(display(grid))
        sleep(0.5)
        apply_rules(grid, neighbour_finder(grid))

except KeyboardInterrupt:
    print('interrupted!')
