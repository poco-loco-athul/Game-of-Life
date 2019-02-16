from gameoflife import *
from time import sleep
import RLEsupport


# 1. Beacon: works
rle ="2o2b$o3b$3bo$2b2o!"
x,y = 4,4



grid = RLEsupport.decode(rle,x,y)
try:
    while True:
        print(display(grid))
        sleep(0.5)
        apply_rules(grid, neighbour_finder(grid))

except KeyboardInterrupt:
    print('\ninterrupted!')
