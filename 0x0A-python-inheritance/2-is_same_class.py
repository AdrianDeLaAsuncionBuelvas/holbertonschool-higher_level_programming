#!/usr/bin/python3

"""
function that returns True if the object is exactly an instance of\
 the specified class; otherwise False
"""


def is_same_class(obj, a_class):
    """
    is_same_class - check a object and a class
    obj - object to check
    a_class - class instance
    """

    if type(obj) is a_class:
        return (True)
    else:
        return (False)
