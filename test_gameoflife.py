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
    n, m = 1,2
    assert gameoflife.existential_check(n,m,row,col) == True


def test_neighbour_finder():
    neighbour_hood = [ [False, True],
                       [True, False] ]
    result =  [ [2,1],
                [1,2] ]

    assert gameoflife.neighbour_finder(neighbour_hood) == result

