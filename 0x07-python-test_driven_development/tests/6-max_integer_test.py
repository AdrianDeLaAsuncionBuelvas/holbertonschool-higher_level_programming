#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    class Max_Integer -- check the numbers of a function
    unittest.TestCase -- module provides a rich set of tools for\
 constructing and running tests
    """

    def test_empy_list(self):
        """
        check if the list is empty
        """
        self.assertEqual(max_integer(), None)

    def test_check_input(self):
        """
        check the number input
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([2007]), 2007)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-2222, 30, 75]), 75)
        self.assertEqual(max_integer([-1024, -2202, -7]), -7)

    if __name__ == '__main__':
        unittest.main()
