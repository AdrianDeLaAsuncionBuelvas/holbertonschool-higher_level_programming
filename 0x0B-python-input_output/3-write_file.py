#!/usr/bin/python3
"""
function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    write_file - writes a string to a text file
    text - text to a write
    """

    with open(filename, mode='w', encoding='utf-8') as file_open:
        count_char = file_open.write(text)
        return (count_char)
