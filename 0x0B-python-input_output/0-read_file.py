#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    """
    read_file - Read a text file
    filename - Name of a File
    """

    with open(filename, mode="r", encoding="utf-8") as file_open:
        print(file_open.read(), end='')
