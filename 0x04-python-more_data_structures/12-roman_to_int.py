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
    i = 0

    if not roman_string:
        return 0

    while i < len(roman_string) - 1:

        if gv(roman_string[i]) < gv(roman_string[i+1]):
            ans += gv(roman_string[i+1]) - gv(roman_string[i])
            i += 1
        else:
            ans += gv(roman_string[i])

        i += 1
    if i < len(roman_string):
        ans += gv(roman_string[i])

    return ans
