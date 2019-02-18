import RLEsupport
import curses
from gameoflife import *
from time import sleep


# More patterns are available in ConwayLife.com. Use RLE file format from patterns
# Simulation only follows Conways original rules

# Simulation runs on finite grid, so choose your patterns carfully
# To expand the grid increase the value of m (for more col) and n (for more row)



# Patterns:

# 1. Block (still life)
# rle = "2o$2o!"
# x,y = 2,2

# 2. Beacon (Oscillator)
# rle ="2o2b$o3b$3bo$2b2o!"
# x,y = 4,4

# 3. Pulsar (Oscillator)
# rle ="2b3o3b3o2b2$o4bobo4bo$o4bobo4bo$o4bobo4bo$2b3o3b3o2b2$2b3o3b3o2b$o4bobo4bo$o4bobo4bo$o4bobo4bo2$2b3o3b3o!"
# x,y = 13,13

# 4. Gosper glider gun
# rle = "24bo$22bobo$12b2o6b2o12b2o$11bo3bo4b2o12b2o$2o8bo5bo3b2o$2o8bo3bob2o4bobo$10bo5bo7bo$11bo3bo$12b2o!"
# x, y = 36, 9

# 5. Garden of Eden 5 (Flower of Eden)
rle = "b3o2b2o3b$b2obobob3o$b3o2b5o$obobobobobo$4obobobob$4b3o4b$bobobob4o$obobobobobo$5o2b3ob$3obobob2ob$3b2o2b3o!"
x,y = 11, 11

# 6. Decapole (Oscillator)
# rle = "11b2o$10bobo2$8bobo2$6bobo2$4bobo2$2bobo2$obo$2o!"
# x,y = 13,13

# 7. Pentadecathlon (Oscillator)(Period=15)
# rle ="2bo4bo2b$2ob4ob2o$2bo4bo!"
# x = 10
# y = 3


def draw(value, window):
    for (row, col), char in value.items():
        window.addch(row, col, char)

def main(window):
    curses.curs_set(0)
    grid = RLEsupport.decode(rle,x,y,m=3, n=3) #input
    
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



if __name__ == "__main__":
    curses.wrapper(main)


