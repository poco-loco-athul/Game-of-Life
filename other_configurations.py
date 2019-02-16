from gameoflife import *
from time import sleep
import RLEsupport


# 1. Beacon
# rle ="2o2b$o3b$3bo$2b2o!"
# x,y = 4,4

# 2. Pulsar
# rle ="2b3o3b3o2b2$o4bobo4bo$o4bobo4bo$o4bobo4bo$2b3o3b3o2b2$2b3o3b3o2b$o4bobo4bo$o4bobo4bo$o4bobo4bo2$2b3o3b3o!"
# x,y = 13,13

# 3. Gosper glider gun
rle = "24bo$22bobo$12b2o6b2o12b2o$11bo3bo4b2o12b2o$2o8bo5bo3b2o$2o8bo3bob2o4bobo$10bo5bo7bo$11bo3bo$12b2o!"
x, y = 36, 9



grid = RLEsupport.decode(rle,x,y)
try:
    while True:
        print(display(grid))
        sleep(0.5)
        apply_rules(grid, neighbour_finder(grid))

except KeyboardInterrupt:
    print('\ninterrupted!')
