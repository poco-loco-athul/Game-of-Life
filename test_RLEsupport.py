import RLEsupport


def test_RLE_to_string():
    # Test for replacing of b, o and $
    val = "2o$2b!"
    result = "True True ;False False"
    assert RLEsupport.RLE_to_string(val) == result
    
    # Test for empty lines
    val ="2b3o3$o4b!"
    result = "False False True True True ;False ;False ;True False False False False"
    assert RLEsupport.RLE_to_string(val) == result


def test_string_to_matrix():
    value =  "True False ;True False"
    rslt  = [[True, False],[True, False]]
    assert RLEsupport.string_to_matrix(value) == rslt


def test_expand_matrix():
    val =  [[True, False],[True, False]]
    result = [[False],[False],[False],
              [False, False, False, True, False],
              [False, False, False, True, False],
              [False],[False],[False]]
    assert RLEsupport.expand_matrix(val) == result
    
    
def test_fill_matrix():
    value =   [[False],[False],[False],
               [False, False, False, True, False],
               [False, False, False, True, False],
               [False],[False],[False]]
    x, y = 2,2
    rslt = [[False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, True, False, False, False, False],
            [False, False, False, True, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False]]
    assert RLEsupport.fill_matrix(value,x,y) == rslt
    


def test_decode():
    RLE_value ="2b3o3b3o2b2$o4bobo4bo"
    x, y = 3, 13
    rst = [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, True, True, True, False, False, False, True, True, True, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
           [False, False, False, True, False, False, False, False, True, False, True, False, False, False, False, True, False, False, False],
           [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]]
    assert RLEsupport.decode(RLE_value, x, y) == rst

    
