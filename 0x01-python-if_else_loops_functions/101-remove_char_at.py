#!/usr/bin/python3
def remove_char_at(str, n):
    res = ''
    for i, c in enumerate(str):
        if i is not n:
            res = res + c
    return res
