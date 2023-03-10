import pytest
import convert
import itertools

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

@pytest.mark.parametrize("arabic,roman", (
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (5, "V"),
    (6, "VI"),
    (4, "IV"),
    (10, "X"),
    (50, "L"),
    (100, "C"),
    (500, "D"),
    (1000, "M"),
    (160, "CLX"),
    (140, "CXL"),
    (39, "XXXIX"),
    (2421, "MMCDXXI"),
    (3999, "MMMCMXCIX"),
))
def test_arabic_to_roman(arabic, roman):
    assert convert.arabic_to_roman(arabic) == roman

def test_no_quartets():
    for n in range(1, 4000):
        roman = convert.arabic_to_roman(n)
        # print(roman)
        for _, block in itertools.groupby(roman):
            assert len(list(block)) < 4

def test_inverts():
    for n in range(1, 4000):
        assert convert.roman_to_arabic(convert.arabic_to_roman(n)) == n
