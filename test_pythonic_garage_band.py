from pythonic_garage_band import Musician, Guitarist, Drummer, Bassist, Band, read_file

def test_guitarist_role():
    expected = 'Guitarist'
    actual = Guitarist('Guitarist', 'guitar').role
    assert expected == actual

def test_guitarist_instrument():
    expected = 'guitar'
    actual = Guitarist('Guitarist', 'guitar').instrument
    assert expected == actual

def test_guitarist_str():
    expected = 'I am a Guitarist'
    actual = Guitarist('Guitarist', 'guitar').__str__()
    assert expected == actual

def test_guitarist_repr():
    assert 'This is Guitarist' == Guitarist('Guitarist', 'guitar').__repr__()

def test_guitarist_get_instrument():
    assert 'guitar' == Guitarist('Guitarist', 'guitar').get_instrument()

def test_guitarist_play_solo():
    assert 'Guitarist is playing solo on the guitar' == Guitarist('Guitarist', 'guitar').play_solo()

def test_drummer_play_solo():
     assert 'Drummer is playing solo on the drums' == Drummer('Drummer', 'drums').play_solo()

def test_guitarist_str():
    assert 'I am a Bassist' == Bassist('Bassist', 'bass').__str__()

def test_musicians_members():
    Musician.members = []
    guitarist = Guitarist('Guitarist', 'guitar')
    bassist = Bassist('Bassist','bass')
    drummer = Drummer('Drummer', 'drums')
    assert [guitarist, bassist, drummer] == Musician.members

def test_Band_instance():
    
