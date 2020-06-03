#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry():
    """
    Class that defines a Figure
    """

    pass

    def area(self):
        """
        Area of a Geometry
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Integer_validator - validates if an integers was entered
        name: string to validate
        value: Value to validate
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
        Instantiation with width and height
        width: Width of a Figure
        height: Height of a Figure
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
