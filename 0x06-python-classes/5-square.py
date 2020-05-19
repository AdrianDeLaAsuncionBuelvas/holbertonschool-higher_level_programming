#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Class Square
    Attributes:
    size -- size of square"""
    def __init__(self, size=0):
        """Class Method Private instance attribute"""
        self.size = size

    """Property size
    Return:
    size of Class"""
    @property
    def size(self):
        return (self.__size)

    """Class Method  Setter size
    Attributes:
    value -- value to calculate"""
    @size.setter
    def size(self, value):

        if type(value) is int:
            if value < 0:
                """Raised when the Value is incorrect"""
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            """Raised when the Value is incorrect"""
            raise TypeError("size must be an integer")

    """ Public instance that returns the current square area"""
    def area(self):
        return (self.__size ** 2)

    """Public instance that prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size is 0:
            print("")
        else:
            for i in range(self.__size):
                """walk the area of the square"""
                for j in range(self.__size):
                    print("#", end='')
                print("")
