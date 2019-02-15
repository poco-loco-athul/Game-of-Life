# Conway's Game of Life

def existential_check(a,b,row,col): 
    "Checks whether the calling neighbour(a,b) exists or not"
    if a in range(row) and b in range(col):    
        return True
    else:
        return False

def neighbour_finder(grid):
    "neighbour_finder() finds number of alive cells for each cells (dead or alive)"
    rows = len(grid)
    cols = len(grid[0])

    result = [[None for i in range(rows)] for j in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            count = 0
            #Counting:
            if existential_check(i-1,j-1,rows,cols):
                if grid[i-1][j-1]:
                    count += 1
            if existential_check(i-1,j,rows,cols):
                if grid[i-1][j]:
                    count += 1
            if existential_check(i-1,j+1,rows,cols):
                if grid[i-1][j+1]:
                    count += 1

            if existential_check(i,j-1,rows,cols):
                if grid[i][j-1]:    
                    count += 1
            if existential_check(i,j+1,rows,cols):
                if grid[i][j+1]:    
                    count += 1

            if existential_check(i+1,j-1,rows,cols):
                if grid[i+1][j-1]:    
                    count += 1
            if existential_check(i+1,j,rows,cols):
                if grid[i+1][j]:    
                    count += 1
            if existential_check(i+1,j+1,rows,cols):
                if grid[i+1][j+1]:    
                    count += 1

            result[i][j] = count

    return result


def apply_rules(grd,neighbour):
    rows = len(grd)
    cols = len(grd[0])    
    "Applies Coway's rules and produces next generation"
    for i in range(rows):
        for j in range(cols):
            if grd[i][j]:
                if neighbour[i][j] not in range(2,4):
                    grd[i][j] = False
            if not grd[i][j]:
                if neighbour[i][j] == 3:
                    grd[i][j] = True
    return grd

                    
def display(grd):
    rows = len(grd)
    cols = len(grd[0])    
    "Displays given grid(matrix) as string"
    formatter = ""
    for i in range(rows):
        formatter += "\t\n"
        for j in range(cols):
            if grd[i][j]:
                formatter += "O "
            else:
                formatter += ". "
    return formatter
