#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    num = {'I': 1,
           'V': 5,
           'X': 10,
           'L': 50,
           'C': 100,
           'D': 500,
           'M': 1000}
    res = 0
    for i in range(0, len(roman_string)):
        if i == 0 or num[roman_string[i]] <= num[roman_string[i - 1]]:
                res += num[roman_string[i]]
        else:
                res += num[roman_string[i]] - 2 * num[roman_string[i - 1]]
    return (res)
