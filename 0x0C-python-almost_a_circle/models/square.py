#!/usr/bin/python3

"""
class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        """
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value


    def update(self, *args, **kwargs):
        """
        @args - is the list of arguments
        @kwargs - 
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
        """
        """

        str = "[Square] ({}) {}/{} - {}"
        return (str.format(self.id, self.x, self.y, self.width))
