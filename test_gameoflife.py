import gameoflife

def test_within_bounds():
    row, col = 2,2 
    # when m is out of index
    n, m = 1,3
    assert gameoflife.within_bounds(n,m,row,col) == False
    # when n is out of indec
    n, m = -1,1
    assert gameoflife.within_bounds(n,m,row,col) == False
    # when n and m are in index
    n, m = 1,1
    assert gameoflife.within_bounds(n,m,row,col) == True


def test_count_of_alive_neighbours():
    neighbour_hood = [ [False, True],
                       [True, False] ]
    result =  [ [2,1],
                [1,2] ]
    assert gameoflife.count_of_alive_neighbours(neighbour_hood) == result

    neighbour_hood = [ [False, True, False],
                       [True, False, False],
                       [True, False, True] ]
    result =  [ [2,1,1],[2,4,2],[1,3,0] ]
    assert gameoflife.count_of_alive_neighbours(neighbour_hood) == result


def test_apply_rules():
    grid =  [ [False, False, True],
              [True, False, False],
              [False, True, False]]
    neighbours = [ [1,2,0],
                   [1,3,2],
                   [2,1,1]]
    result =  [ [False, False, False],
                [False, True, False],
                [False, False, False]]
    assert gameoflife.apply_rules(grid, neighbours) == result

    grid =  [ [False, True, True],
              [True, True, False],
              [False, True, False]]
    neighbours = [ [3,3,2],
                   [3,4,4],
                   [3,2,2]]
    result =  [ [True, True, True],
                [True, False, False],
                [True, True, False]]
    assert gameoflife.apply_rules(grid, neighbours) == result


def test_display():
    grid = [ [False, True],
             [True, False] ]
    dsply ="\t\n. O \t\nO . "
    assert gameoflife.display(grid) == dsply


def test_display_curses():
    grid = [ [False, True],
             [True, False] ]
    dsply = { (5,5) : "." , (5,6) : "O",(6,5) : "O", (6,6) : "." }
    assert gameoflife.display_curses(grid, r=5) == dsply
    
    

