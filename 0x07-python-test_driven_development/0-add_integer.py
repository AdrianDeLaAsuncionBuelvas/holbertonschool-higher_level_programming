#!/usr/bin/python3
"""
Function that adds 2 Integers
"""


def add_integer(a, b=98):
    """
    Adds 2 Integers
    a -- Number to adds
    b -- Number to adds

    Return:
    The result of Adds
    """

    if type(a) is float:
        """if it is a floating type we will cast it to int"""
        a = int(a)
    if type(b) is float:
        """if it is a floating type we will cast it to int"""
        b = int(b)
    if type(a) is not int:
        """if it is not an int or Float... it shows an error message"""
        raise TypeError("a must be an integer")
    if type(b) is not int:
        """if it is not an int or Float... it shows an error message"""
        raise TypeError("b must be an integer")
    return (a + b)
