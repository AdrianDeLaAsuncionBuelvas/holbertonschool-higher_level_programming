#!/usr/bin/python3
class Square:
    """Class Square that defines a square"""
    def __init__(self, size=0):
        """Class Method Private instance attribute"""
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
