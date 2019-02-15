import gameoflife

def test_existential_check():
    row, col = 2,2 
    # when m is out of index
    n, m = 1,3
    assert gameoflife.existential_check(n,m,row,col) == False
    # when n is out of indec
    n, m = -1,1
    assert gameoflife.existential_check(n,m,row,col) == False
    # when n and m are in index
    n, m = 1,1
    assert gameoflife.existential_check(n,m,row,col) == True


def test_neighbour_finder():
    neighbour_hood = [ [False, True],
                       [True, False] ]
    result =  [ [2,1],
                [1,2] ]
    assert gameoflife.neighbour_finder(neighbour_hood) == result

    neighbour_hood = [ [False, True, False],
                       [True, False, False],
                       [True, False, True] ]
    result =  [ [2,1,1],[2,4,2],[1,3,0] ]
    assert gameoflife.neighbour_finder(neighbour_hood) == result



#Test for rules:
def test_rule_one():
    grid =  [ [True, False],
              [False, False] ]
    neighbours = [ [0,1],
                   [1,1] ]
    result =  [ [False, False],
                [False, False] ]
    assert gameoflife.rule_one(grid, neighbours,2,2) == result
    
    grid =  [ [False, False, True],
              [True, False, False],
              [False, True, False]]
    neighbours = [ [1,2,0],
                   [1,3,2],
                   [2,1,1]]
    result =  [ [False, False, False],
                [False, False, False],
                [False, False, False]]
    assert gameoflife.rule_one(grid, neighbours,3,3) == result

def test_rule_three():
    grid =  [ [True, True],
              [True, True] ]
    neighbours = [ [3,3],
                   [3,3] ]
    result =  [ [False, False],
                [False, False] ]
    assert gameoflife.rule_three(grid, neighbours,2,2) == result
    
    grid =  [ [False, True, True],
              [True, True, False],
              [False, True, False]]
    neighbours = [ [3,3,2],
                   [3,4,4],
                   [3,2,2]]
    result =  [ [False, True, True],
                [True, False, False],
                [False, True, False]]
    assert gameoflife.rule_three(grid, neighbours,3,3) == result
    

