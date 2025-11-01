from twttr import shorten

def test_basic():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"

def test_with_vowels():
    assert shorten("hello") == "hll"
    assert shorten("AEIOU") == ""

def test_with_numbers_and_symbols():
    assert shorten("CS50!") == "CS50!"
    assert shorten("123abc!") == "123bc!"

def test_mixed_case():
    assert shorten("Python") == "Pythn"
    assert shorten("ApPlE") == "pPl" or shorten("ApPlE") == "pPl"