#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    big = 0
    best = ""
    for key, i in a_dictionary.items():
        if (i > big):
            big = i
            best = key
    return (best)
