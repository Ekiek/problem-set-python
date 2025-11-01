import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("0/1") == 0
    assert convert("1/1") == 100

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("3/0")  
    with pytest.raises(ValueError):
        convert("a/b") 
    with pytest.raises(ValueError):
        convert("5/4")  
    with pytest.raises(ValueError):
        convert("-1/2")  

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
