#!/usr/bin/python3

"""
Class BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Instantiation with size
        size - size of Square
        """

        self.__size = size
        self.integer_validator("size", size)

        super().__init__(size, size)
