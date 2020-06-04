#!/usr/bin/python3

"""
Class that define a Student
"""


class Student():
    """
    Define a Student
    """
    def __init__(self, first_name, last_name, age):
        """Initialization Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student
        """

        if attrs is None:
            return (self.__dict__)
        my_dict = {}
        for attr in attrs:
            if attr in self.__dict__.keys():
                my_dict[attr] = self.__dict__[attr]
        return (my_dict)
