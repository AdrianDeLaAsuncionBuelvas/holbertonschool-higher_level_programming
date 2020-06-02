#!/usr/bin/python3

"""
function that returns True if the object is an instance of, \
or if the object is an instance of a class that inherited from, \
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - check a type object if a instance of the class
    obj - object to check
    a_class - class to check
    """

    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
