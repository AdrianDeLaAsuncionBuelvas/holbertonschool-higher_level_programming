#!/usr/bin/python3
"""
function that returns the list of available attributes \
and methods of an object
"""


def lookup(obj):
    """
    lookup - return a list of available attributes
    obj - object to check
    """
    return (dir(obj))
