import RLEsupport


def test_RLE_to_string():
    x, y = 2, 2 
    val = "2o$2b!"
    result = "True True; False False"
    assert RLEsupport.RLE_to_string(val,x,y) == result
