#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    for key, i in new.items():
        i *= 2
        new[key] = i
    return (new)
