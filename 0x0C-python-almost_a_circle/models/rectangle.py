#!/usr/bin/python3

"""Class Rectangle inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Class defining a square """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Class Rectangle
        Args:
            width: integer that receives the width
            height: integer that receives the height
            x: integer that receives the x
            y: integer that receives the y
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Returns width as a private attribute
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Define the width
        Args:
            value: integer that represents the width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns height as a private attribute
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """Define the height
        Args:
        value: integer that represents the height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Returns x as a private attribute
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """Define the x
        Args:
            value: integer that represents the x
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Returns y as a private attribute
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """Define the y
        Args:
            value: integer that represents the y
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area value of the Rectangle
        """

        return (self.__width * self.__height)

    def display(self):
        """
        Print is Stdout with character '#'
        """

        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print('')

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        Args:
            args: is the list of arguments
            kwargs: can be thought of as a double pointer \
to a dictionary: key/value
        """

        attrs = ['id', 'width', 'height', 'x', 'y']
        for elem in range(len(args)):
            for attr in range(len(attrs)):
                if attr == elem:
                    setattr(self, attrs[attr], args[elem])
                    break

        if not args or len(args) == 0:
            for key, val in kwargs.items():
                for attr in range(len(attrs)):
                    if key == attrs[attr]:
                        setattr(self, attrs[attr], val)
                        break

    def to_dictionary(self):
        """
        Returns the dictionary
        """

        dt = {'x': self.x, 'width': self.width, 'id': self.id, \
              'height': self.height, 'y': self.y}

        return (dt)

    def __str__(self):
        """
        Args:
            str method return String with datas
        """

        str = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return (str.format(self.id, self.__x, self.__y, \
                           self.__width, self.__height))
