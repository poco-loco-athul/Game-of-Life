import gameoflife

def test_neighbour_finder():

    neighbour_hood = [ [False, True],
                       [True, False] ]

    result =  [ [2,1],
                [1,2] ]

    assert gameoflife.neighbour_finder(neighbour_hood) == result
