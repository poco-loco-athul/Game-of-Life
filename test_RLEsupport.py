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
