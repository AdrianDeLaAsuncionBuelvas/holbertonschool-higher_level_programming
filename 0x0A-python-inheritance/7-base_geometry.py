#!/usr/bin/python3

"""
Class BaseGeometry
"""


class BaseGeometry():
    """
    BaseGeometry - Empty Class
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
