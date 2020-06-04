#!/usr/bin/python3
"""
function that returns an object \
(Python data structure)
"""
import json


def from_json_string(my_str):
    """
    from_json_string - representation of an object
    my_str - object to evaluate
    Return: JSON
    """

    return(json.loads(my_str))
