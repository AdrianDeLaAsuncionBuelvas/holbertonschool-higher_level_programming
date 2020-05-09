#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return (None)

    numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    value_previous = 0
    for i in range(len(roman_string)):
        for key, value in numbers.items():
            if key == roman_string[i]:
                result += value
                if (value_previous < value):
                    result -= (value_previous * 2)
                    value_previous = value
    return (result)
