#!/usr/bin/python3

"""
Class Rectangle
"""


class Rectangle():
    """
    Class Rectangle that defines a Rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Instance returns the rectangle area
        """
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """
        Print the rectangle with the character #
        """
        string = ''
        """it is stored in a variable to iterate"""
        if self.__width == 0 or self.__height == 0:
            return (string)
        """
        Runs width and height
        """
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            string += '\n'
        return (string[:-1])

    def __repr__(self):
        """
        Return the class name and its arguments
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes an Instance
        """
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        """

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return (rect_1)
        else:
            return (rect_2)
