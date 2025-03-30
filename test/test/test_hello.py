from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argumant():
    assert hello("David") == "hello, David"