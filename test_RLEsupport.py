import RLEsupport


def test_RLE_to_string():
    val = "2o$2b!"
    result = "True True ;False False"
    assert RLEsupport.RLE_to_string(val) == result
