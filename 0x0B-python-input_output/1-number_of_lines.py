#!/usr/bin/python3
"""
function that returns the number of lines of a text file
"""


def number_of_lines(filename=""):
    """
    Return number of lines
    filename -- Contain the file name
    """
    count = 0
    with open(filename, mode='r', encoding='utf-8') as file_open:
        for n_l in file_open:
            count += 1
        return(count)
