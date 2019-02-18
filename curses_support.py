

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
