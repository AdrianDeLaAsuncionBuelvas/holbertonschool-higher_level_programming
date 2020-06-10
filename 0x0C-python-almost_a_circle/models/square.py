#!/usr/bin/python3

"""
Class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Defining a Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the Class Square
        Args:
            size: integer that receives the size
            x: integer that receives the x
            y: integer that receives the y
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns size as a private attribute"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Define the size
        Args:
            value: integer that represents the size
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes
        Args:
            args: is the list of arguments
            kwargs: double pointer to a dictionary: key/value
        """

        attrs = ['id', 'size', 'x', 'y']
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

        dt = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

        return (dt)

    def __str__(self):
        """Method return String with datas"""

        str = "[Square] ({}) {}/{} - {}"
        return (str.format(self.id, self.x, self.y, self.width))
