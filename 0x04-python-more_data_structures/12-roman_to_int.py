#!/usr/bin/python3
def gv(rl):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    return roman_numerals[rl]


def roman_to_int(roman_string):
    ans = 0
