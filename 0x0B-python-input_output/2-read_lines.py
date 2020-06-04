#!/usr/bin/python3
"""
 function that reads n lines of a text file
"""


def read_lines(filename="", nb_lines=0):
    """
    read_lines - Read n Lines of a text file
    nb_lines - number of lines to read
    """

    count = 0
    with open(filename, mode='r', encoding='utf-8') as file_open:
        for n_l in file_open:
            count += 1

    if nb_lines <= 0 or nb_lines >= count:
        nb_lines = count

    i = 0
    with open(filename, mode='r', encoding='utf-8') as file_open:
        for n_l in file_open:
            if i == nb_lines:
                break
            print(n_l, end='')
            i += 1
