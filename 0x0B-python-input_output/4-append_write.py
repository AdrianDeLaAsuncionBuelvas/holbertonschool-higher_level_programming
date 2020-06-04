#!/usr/bin/python3
"""
Function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    append_write - Appends a string at the end of a text file
    filename - Name of a a File
    text - Text to Appends
    """

    count = 0
    with open(filename, mode='a', encoding='utf-8') as file_open:
        file_open.write(text)
        for n_a in text:
            count += 1
        return(count)
