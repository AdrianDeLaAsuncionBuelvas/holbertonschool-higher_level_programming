#!/usr/bin/python3

"""
Class BaseGeometry
"""


class BaseGeometry():
    """
    Class BaseGeometry
    """
    pass

    def area(self):
        """
        Area of a Geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator - validates if an integers was entered
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        instantiation with width and height
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Return: area of geometric figure
        """

        return (self.__width * self.__height)

    def __str__(self):
        """
        Method Print
        """

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


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
