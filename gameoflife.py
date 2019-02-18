# Conway's Game of Life

def existential_check(a,b,row,col): 
    "Checks whether the calling cell(a,b) exists or not. This helps neighbour_finder() stay inside the given matrix. "
    if a in range(row) and b in range(col):    
        return True
    else:
        return False
    

def neighbour_finder(grid):
    "neighbour_finder() finds number of neighbouring alive cells for each cell"
    rows = len(grid)
    cols = len(grid[0])
    result = [[None for i in range(cols)] for j in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            count = 0
            # A cell can have 8 possible neighbours
            # if cell exists, if cell is alive, count increments
            cells = [(i-1,j-1), (i-1, j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]
            for k in cells:
                if existential_check(k[0],k[1],rows,cols): 
                    if grid[ k[0] ][ k[1] ]:
                        count += 1
            result[i][j] = count
    return result


def apply_rules(grd,neighbour):
    "Applies Conway's rules and produces next generation"
    rows = len(grd)
    cols = len(grd[0])    
    for i in range(rows):
        for j in range(cols):
            # Rules 1,2 and 3
            if grd[i][j]:
                if neighbour[i][j] not in range(2,4):
                    grd[i][j] = False
            # Rule 4        
            if not grd[i][j]:
                if neighbour[i][j] == 3:
                    grd[i][j] = True
    return grd

                    
def display(grd):
    "Displays given grid(matrix) as a string"
    rows = len(grd)
    cols = len(grd[0])    
    formatter = ""
    for i in range(rows):
        formatter += "\t\n"
        for j in range(cols):
            if grd[i][j]:
                formatter += "O "
            else:
                formatter += ". "
    return formatter


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
