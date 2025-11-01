import pytest
from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("1") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("") == False

def test_start_with():
    assert is_valid("1A") == False
    assert is_valid("9B12") == False
    assert is_valid("!A12") == False
    assert is_valid("AB") == True
    assert is_valid("AA123") == True

def test_alphanumeric():
    assert is_valid("PI3.14") == False
    assert is_valid("AB CD") == False
    assert is_valid("AB-CD") == False
    assert is_valid("AB_CD") == False
    assert is_valid("AB#12") == False

def test_zero_first_number():
    assert is_valid("AA012") == False
    assert is_valid("AB0123") == False

def test_numbers_in_middle():
    assert is_valid("AB12C") == False
    assert is_valid("A1B2") == False

def test_valid_plates():
    assert is_valid("AA") == True
    assert is_valid("AB12") == True
    assert is_valid("XY123") == True
    assert is_valid("HELLO1") == True
    assert is_valid("AB1") == True
