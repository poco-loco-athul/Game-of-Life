# Conway's Game of Life
"gameoflife contains functions to simulate Conway's Game of Life"

def within_bounds(m_row, n_col, rows, cols):
    """Checks whether the calling cell(a,b) exists or not. This helps
    count_of_alive_neighbours() stay inside the given matrix."""
    return all([m_row in range(rows),
                n_col in range(cols)])

def make_empty_matrix(m_row, n_col):
    "Makes empty matrix with 'm' rows and 'n' columns"
    return [[None for i in range(n_col)] for j in range(m_row)]

def all_neighbours(m_row, n_col):
    "Returns all 8 neighbours, even out bounds"
    list_a = [m_row + x for x in [-1, 0, 1]]
    list_b = [n_col + y for y in [-1, 0, 1]]
    neighbours = [(m, n) for m in list_a for n in list_b]
    neighbours.remove((m_row, n_col))
    return neighbours

def count_of_alive_neighbours(grid):
    "Returns number of neighbouring alive cells for each cell"
    rows, cols = len(grid), len(grid[0])
    count_matrix = make_empty_matrix(rows, cols)
    for row in range(rows):
        for col in range(cols):
            count = 0
            # A cell can have 8 possible neighbours
            # if cell exists, if cell is alive, count increments
            cells = all_neighbours(row, col)
            for cel in cells:
                if within_bounds(cel[0], cel[1], rows, cols):
                    if grid[cel[0]][cel[1]]:
                        count += 1
            count_matrix[row][col] = count
    return count_matrix

def apply_rules(grid, neighbour):
    "Applies Conway's rules and produces next generation"
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            # Rules 1,2 and 3
            if grid[row][col]:
                if neighbour[row][col] not in [2, 3]:
                    grid[row][col] = False
            # Rule 4
            if not grid[row][col]:
                if neighbour[row][col] == 3:
                    grid[row][col] = True
    return grid


def display(grd):
    "Displays given grid(matrix) as a string"
    rows, cols = len(grd), len(grd[0])
    dsply_string = ""
    for i in range(rows):
        dsply_string += "\t\n"
        for j in range(cols):
            if grd[i][j]:
                dsply_string += "O "
            else:
                dsply_string += ". "
    return dsply_string


def display_curses(grd, disp=5):
    "Changes given matrix as a dict that contains position and character"
    # disp is the shift from 0,0 of screen
    rows, cols = len(grd), len(grd[0])
    dsply_dict = {}
    for i in range(rows):
        for j in range(cols):
            if grd[i][j]:
                dsply_dict[(i+disp, j+disp)] = "O"
            else:
                dsply_dict[(i+disp, j+disp)] = "."
    return dsply_dict
