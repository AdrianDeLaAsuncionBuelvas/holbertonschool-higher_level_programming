#!/usr/bin/python3

"""
Unittest for models/rectangle.py
"""
import sys
import os
import io
import contextlib
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
            self.assertEqual("width must be an integer", str(x.exception))

            with self.assertRaises(TypeError) as x:
                r = Rectangle(13, 2.0)
            self.assertEqual("height must be an integer", str(x.exception))

            with self.assertRaises(TypeError) as x:
                r = Rectangle(13, 20, 1.7777)
            self.assertEqual("x must be an integer", str(x.exception))

            with self.assertRaises(TypeError) as x:
                r = Rectangle(13, 20, 17, 8.0)
            self.assertEqual("y must be an integer", str(x.exception))

    def test_15_dict_test(self):
        """Test for dicts passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r = Rectangle(10, {})
        self.assertEqual(
            "height must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle({"a": 1, "b": 2, "c": 3}, 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(10, 2, {"a": 1})
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(10, 2, 0, {"hi": None})
        self.assertEqual(
            "y must be an integer",
            str(x.exception))

    def test_16_tuple_test(self):
        """Test for tuples passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r = Rectangle(10, ())
        self.assertEqual(
            "height must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle((1, 2, 3), 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(10, 2, (2, 4))
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(10, 2, 0, ("hi",))
        self.assertEqual(
            "y must be an integer",
            str(x.exception))

    def test_17_negative_ints(self):
        """Test for negative inputs."""
        with self.assertRaises(ValueError) as x:
            r = Rectangle(1, -2)
        self.assertEqual(
            "height must be > 0",
            str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(-1, -2)
        self.assertEqual(
            "width must be > 0",
            str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(1, 2, -1)
        self.assertEqual(
            "x must be >= 0",
            str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(1, 2, 5, -1)
        self.assertEqual(
            "y must be >= 0",
            str(x.exception))

    def test_18_area(self):
        """Test for area."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)
        r = Rectangle(1, 20, 1)
        self.assertEqual(r.area(), 20)
        r = Rectangle(4, 5, 6, 2)
        self.assertEqual(r.area(), 20)
        r = Rectangle(9, 7, 4, 6, 12)
        self.assertEqual(r.area(), 63)

    def test_19_display(self):
        """Test for display."""
        r = Rectangle(4, 6)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        four_by_six = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(s, four_by_six)
        r = Rectangle(2, 4)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        two_by_four = "##\n##\n##\n##\n"
        self.assertEqual(s, two_by_four)
        r = Rectangle(1, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        one_by_one = "#\n"
        self.assertEqual(s, one_by_one)

    def test_20_str(self):
        """Test for __str__"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r = Rectangle(5, 5, 1, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 1/1 - 5/5")
        r = Rectangle(1, 1, 0)
        self.assertEqual(r.__str__(), "[Rectangle] (2) 0/0 - 1/1")
        r = Rectangle(1, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (3) 0/0 - 1/1")

    def test_21_update_args(self):
        """Test for update method."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r.update(90, 2)
        self.assertEqual(r.__str__(), "[Rectangle] (90) 10/10 - 2/10")
        r.update(91, 3, 4)
        self.assertEqual(r.__str__(), "[Rectangle] (91) 10/10 - 3/4")
        r.update(92, 6, 7, 8)
        self.assertEqual(r.__str__(), "[Rectangle] (92) 8/10 - 6/7")
        r.update(93, 9, 10, 11, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (93) 11/12 - 9/10")
        r = Rectangle(1, 1)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 4/5 - 2/3")

    def test_22_update_kwargs(self):
        """Test for update with dict."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 3/1 - 2/1")

    def test_23_empty_update(self):
        """Test for empty update."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(r.__str__(), "[Rectangle] (5) 3/4 - 1/2")

    def test_24_to_json_string(self):
        """Test for json string of rectangle."""
        r = Rectangle(10, 7, 2, 8)
        d = r.to_dictionary()
        json_d = Base.to_json_string([d])
        self.assertEqual(type(json_d), str)
        self.assertEqual(
            d, {'height': 7, 'id': 1, 'width': 10, 'x': 2, 'y': 8})

    def test_25_save_to_file(self):
        """Test for save_to_file method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        res = '[{"x": 2, "y": 8, "id": 2, "height": 7, "width": 10},' + \
            ' {"x": 0, "y": 0, "id": 3, "height": 4, "width": 2}]'
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))

    def test_26_create(self):
        """Test for create method with rectangle."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual((r1 == r2), False)
        self.assertEqual((r1 is r2), False)

    def test_27_create_list(self):
        """Test for create method with list."""
        r = Rectangle(1, 1)
        r_dictionary = r.to_dictionary()
        with self.assertRaises(TypeError) as e:
            r = Rectangle.create([1, 2, 3])
        self.assertEqual(
            "create() takes 1 positional argument but 2 were given", str(
                e.exception))

    def test_28_load_from_files(self):
        """Test for load_from_files."""
        with self.assertRaises(TypeError) as e:
            rect_list = Rectangle.load_from_file("Rectangle.json")
        self.assertEqual("load_from_file() takes 1 positional \
argument but 2 were given", str(e.exception))

    def test_29_save_to_file_empty_list(self):
        """Test for empty list in save_to_file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')
        empty = []
        Rectangle.save_to_file(empty)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_30_save_to_file_two_args(self):
        """Test for two args in save_to_file"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 6)


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
