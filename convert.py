# https://en.wikipedia.org/wiki/Roman_numerals

LOOKUP = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def roman_to_arabic(roman: str) -> int:
    total = 0
    last_char = 0
    for char in roman:
        this_char = LOOKUP[char]
        if this_char > last_char:
            total = total + this_char-(last_char*2)
        else:
            total += this_char
        last_char = this_char

    return total
