#!/usr/bin/python3
"""
Function that writes an Object to a text file,\
 using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - Write an object to a text file, \
Using a JSON representation
    my_obj - is a object
    filename - Name of a File
    """

    with open(filename, mode='w', encoding='utf-8') as file_json:
        file_json.write(json.dumps(my_obj))
