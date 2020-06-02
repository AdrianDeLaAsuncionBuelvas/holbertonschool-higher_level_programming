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
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
