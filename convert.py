# https://en.wikipedia.org/wiki/Roman_numerals

LOOKUP = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
REV_LOOKUP = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}

def roman_to_arabic(roman: str) -> int:
    total = 0
    last_char = 0
    for char in reversed(roman):
        this_char = LOOKUP[char]
        if this_char < last_char:
            total -= this_char
        else:
            total += this_char
        last_char = this_char

    return total


def arabic_to_roman(arabic: int) -> str:
    result = ""
    while arabic:
        reduce_by = max(k for k in REV_LOOKUP if k <= arabic)
        result += REV_LOOKUP[reduce_by]
        arabic -= reduce_by

    return result

