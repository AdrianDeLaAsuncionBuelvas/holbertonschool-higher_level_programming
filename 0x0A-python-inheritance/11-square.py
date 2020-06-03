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
        size: Size of Square
        """

        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def __str__(self):
        """
        Print area of a Square
        """

        return ("[Square] {}/{}".format(self.__size, self.__size))
