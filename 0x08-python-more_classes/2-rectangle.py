#!/usr/bin/python3

"""
Empty class Rectangle
"""


class Rectangle():
    """
    Class Rectangle that defines a Rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get width of rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set width of rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get height of rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Set height of rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Instance returns the rectangle area
        """
        return(self.__width * self.__height)

    def perimeter(self):
        """
        Instance returns the rectangle area
        """
        return(self.__width + self.__height) * 2
