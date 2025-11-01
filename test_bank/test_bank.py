from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello, friend") == 0
    assert value("HELLO there!") == 0

def test_h_start():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("hola") == 20

def test_other():
    assert value("good morning") == 100
    assert value("welcome") == 100
    assert value("bye") == 100

def test_whitespace_and_case():
    assert value("   Hello") == 0
    assert value("  hI") == 20
    assert value("  Good Day") == 100