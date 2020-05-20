#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Class Square
    Attributes:
    size -- size of square"""
    def __init__(self, size=0, position=(0, 0)):
        """Class Method Private instance attribute"""
        self.size = size
        self.position = position

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
            for row in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end='')
                """walk the area of the square"""
                for j in range(self.__size):
                    print("#", end='')
                print("")

    """Property position
    Return:
    The position of the Tuple"""
    @property
    def position(self):
        return (self.__position)

    """Setter position
    Attributes:
    value -- values that is entered"""
    @position.setter
    def position(self, value):
        """in this part the tuple data is validated """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        """validates if the tuple data is integer"""
        if any(not isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        """it is validated that they are positive numbers"""
        if any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
