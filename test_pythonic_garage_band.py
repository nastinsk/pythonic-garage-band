from pythonic_garage_band import Musician, Guitarist

def test_guitarist_role():
    expected = "Guitarist"
    actual = Musician('Guitarist', 'guitar').role
    assert expected == actual

def test_guitarist_instrument():
    expected = "guitar"
    actual = Musician('Guitarist', 'guitar').instrument
    assert expected == actual


