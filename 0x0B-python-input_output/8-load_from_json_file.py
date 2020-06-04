#!/usr/bin/python3
"""
Function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a JSON file
    filename - Name of a File
    """

    with open(filename, encoding='utf-8') as file_json:
        for line in file_json:
            new_obj = json.loads(line)
    return(new_obj)
