import pytest
import convert

# https://en.wikipedia.org/wiki/Roman_numerals
@pytest.mark.parametrize("roman,arabic", (
    ("I", 1),
    ("II", 2),
    ("III", 3),
    ("V", 5),
    ("VI", 6),
    ("IV", 4),
    ("X", 10),
    ("L", 50),
    ("C", 100),
    ("D", 500),
    ("M", 1000),
    ("CLX", 160),
    ("XXXIX", 39),
    ("MMCDXXI", 2421),
))
def test_roman_to_arabic(roman: str, arabic: int):
    assert convert.roman_to_arabic(roman) == arabic
