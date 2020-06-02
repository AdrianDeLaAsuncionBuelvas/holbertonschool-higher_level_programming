#!/usr/bin/python3

"""
Class List
"""


class MyList(list):
    """
    MyList inherits from list
    """

    def print_sorted(self):
        """
        print_sorted - prints the list, but sorted (ascending sort)
        """

        print(sorted(self))
