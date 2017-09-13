import util

def test_date_to_float():
    assert(util.date_to_float('20170802040145.4370000') == 1501657305.437)

def test_float_to_date():
    assert(util.float_to_date(1501657305.437) == '20170802040145.4370000')
