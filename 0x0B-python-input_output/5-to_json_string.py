#!/usr/bin/python3
"""
function that returns the JSON representation o
 an object (string)
"""
import json


def to_json_string(my_obj):
    """
    to_json_string - representation of an object
    my_obj - object to evaluate
    Return: JSON
    """

    return(json.dumps(my_obj))
