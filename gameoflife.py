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


def rule_one(grd,neighb,rows,cols):
    for i in range(rows):
        for j in range(cols):
            if grd[i][j]:
                if neighb[i][j] < 2:
                    grd[i][j] = False
    return grd
                    
