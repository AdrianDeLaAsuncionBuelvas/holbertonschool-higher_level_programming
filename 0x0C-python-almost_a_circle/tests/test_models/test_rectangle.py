#!/usr/bin/python3

"""
Unittest for models/rectangle.py
"""
import sys
import os
import io
import unittest

from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):
    """Tests for Class Rectangle"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_00_isinstance(self):
        """Test for isinstance"""

        r = Rectangle(2, 3)
        self.assertEqual(isinstance(r, Base), True)

    def test_01_float(self):
        """Test for float number"""
        with self.assertRaises(TypeError) as x:
            r = Rectangle(float(1.2), float(2.2), 1)
        self.assertEqual("width must be an integer", str(x.exception))

    def test_02_float_nan(self):
        """Test float nan"""
        with self.assertRaises(TypeError) as x:
            r = Rectangle(float("nan"), 1)
        self.assertEqual("width must be an integer", str(x.exception))

    def test_03_float_inf(self):
        """Test float inf"""
        with self.assertRaises(TypeError) as x:
            r = Rectangle(float("inf"), 1)
        self.assertEqual("width must be an integer", str(x.exception))

    def test_04_one_args(self):
        """Test only one argument"""
        with self.assertRaises(TypeError) as x:
            r = Rectangle(7)
        self.assertEqual("__init__() missing 1 required positional argument:\
 'height'", str(x.exception))

    def test_05_zero_input(self):
        """Test 0 number"""
        with self.assertRaises(ValueError) as x:
            r = Rectangle(0, 7)
        self.assertEqual("width must be > 0", str(x.exception))

    def test_05_zero_input(self):
        """Test 0 number"""
        with self.assertRaises(ValueError) as x:
            r = Rectangle(7, 0)
        self.assertEqual("height must be > 0", str(x.exception))

    def test_06_two_args(self):
        """Test for two arguments passed"""
        r = Rectangle(7, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_07_three_args(self):
        """Test for three arguments passed"""
        r = Rectangle(7, 2, 10)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 0)

    def test_08_four_args(self):
        """Test for four arguments passed"""
        r = Rectangle(7, 2, 10, 20)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 20)

    def test_09_five_args(self):
        """Test for Five argument passed"""
        r = Rectangle(7, 2, 10, 20, 5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 20)

    def test_10_private_attr(self):
        """Test for attributes being private"""
        r = Rectangle(5, 2, 10, 20, 7)
        dt = {"_Rectangle__width": 5, "_Rectangle__height": 2,
              "_Rectangle__x": 10, "_Rectangle__y": 20, "id": 7}
        self.assertEqual(r.__dict__, dt)

    def test_11_None_input(self):
        """Test for None passed"""
        with self.assertRaises(TypeError) as x:
            r = Rectangle(None)
        self.assertEqual("__init__() missing 1 required positional argument:\
 'height'", str(x.exception))

    def test_12_No_args(self):
        """Test for None passed"""
        with self.assertRaises(TypeError) as x:
            r = Rectangle()
        self.assertEqual("__init__() missing 2 required positional\
 arguments: 'width' and 'height'", str(x.exception))

    def test_13_string_test(self):
        """"""
        with self.assertRaises(TypeError) as x:
            r = Rectangle("2", 7)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r = Rectangle(2, "7")
        self.assertEqual("height must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r = Rectangle(2, 7, "4")
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r = Rectangle(2, 7, 4, "Cool")
        self.assertEqual("y must be an integer", str(x.exception))

        def test_14_float_test(self):
            """Test for floats passed in as arguments"""
            with self.assertRaises(TypeError) as x:
                r = Rectangle(1.3, 20)
            self.assertEqual("width must be an integer")

            with self.assertRaises(TypeError) as x:
                r = Rectangle(13, 2.0)
            self.assertEqual("height must be an integer")

            with self.assertRaises(TypeError) as x:
                r = Rectangle(13, 20, 1.7777)
            self.assertEqual("x must be an integer")

            with self.assertRaises(TypeError) as x:
                r = Rectangle(13, 20, 17, 8.0)
            self.assertEqual("y must be an integer")

    def test_docstrings(self):
        """checks if Rectangle has a docstring"""
        self.assertEqual(len(Rectangle.__doc__) > 0, True)
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(hasattr(Rectangle, "width"))
        self.assertTrue(Rectangle.width.__doc__)
        self.assertTrue(hasattr(Rectangle, "height"))
        self.assertTrue(Rectangle.height.__doc__)
        self.assertTrue(hasattr(Rectangle, "x"))
        self.assertTrue(Rectangle.x.__doc__)
        self.assertTrue(hasattr(Rectangle, "y"))
        self.assertTrue(Rectangle.y.__doc__)
        self.assertTrue(hasattr(Rectangle, "area"))
        self.assertTrue(Rectangle.area.__doc__)
        self.assertTrue(hasattr(Rectangle, "display"))
        self.assertTrue(Rectangle.display.__doc__)
        self.assertTrue(hasattr(Rectangle, "__str__"))
        self.assertTrue(Rectangle.__str__.__doc__)
        self.assertTrue(hasattr(Rectangle, "update"))
        self.assertTrue(Rectangle.update.__doc__)
        self.assertTrue(hasattr(Rectangle, "to_dictionary"))
        self.assertTrue(Rectangle.to_dictionary.__doc__)


if __name__ == '__main__':
    unittest.main()
