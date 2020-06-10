#!/usr/bin/python3
"""
Unittest for models/base.py
"""
import unittest
import os
import json

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base Class"""

    def test_init(self):
        """tests for instantiation"""
        test1 = Base()
        self.assertEqual(test1.id, 1)
        test2 = Base(13)
        self.assertEqual(test2.id, 13)
        test3 = Base()
        self.assertEqual(test3.id, 2)
        test4 = Base(-1)
        self.assertEqual(test4.id, -1)
        test5 = Base(True)
        self.assertEqual(test5.id, True)
        test6 = Base("10")
        self.assertEqual(test6.id, "10")

    def test_json_directory(self):
        """testing the function that turns an object to a json
        string"""
        rect = Rectangle(2, 6, 1, 2, 20)
        dicRect = rect.to_dictionary()
        self.assertEqual(type(dicRect), dict)
        rectExp = {'id': 20, 'width': 2, 'height': 6, 'x': 1, 'y': 2}
        self.assertEqual(dicRect, rectExp)
        jsonOut = Base.to_json_string([dicRect])
        self.assertEqual(type(jsonOut), str)

        sqr = Square(2, 1, 2, 13)
        dicSqr = sqr.to_dictionary()
        self.assertEqual(type(dicSqr), dict)
        sqrExp = {'id': 13, 'size': 2, 'x': 1, 'y': 2}
        self.assertEqual(dicSqr, sqrExp)
        jsonSOut = Base.to_json_string([dicRect])
        self.assertEqual(type(jsonSOut), str)

        empty = Base.to_json_string([])
        self.assertEqual(empty, "[]")

    def test_from_json_file(self):
        """tests if a file is created with the json module """
        test1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([test1])
        with open("Rectangle.json", mode="r") as fd:
            self.assertEqual([test1.to_dictionary()], json.load(fd))

        empty = []
        Rectangle.save_to_file(empty)
        with open("Rectangle.json", mode="r") as fd:
            self.assertEqual(empty, json.load(fd))

        Rectangle.save_to_file(None)
        with open("Rectangle.json", mode="r") as fd:
            self.assertEqual(empty, json.load(fd))

        test2 = Square(1, 3, 4, 5)
        Square.save_to_file([test2])
        with open("Square.json", mode="r") as fd:
            self.assertEqual([test2.to_dictionary()], json.load(fd))

        Square.save_to_file(empty)
        with open("Square.json", mode="r") as fd:
            self.assertEqual(empty, json.load(fd))

        Square.save_to_file(None)
        with open("Square.json", mode="r") as fd:
            self.assertEqual(empty, json.load(fd))

    def test_from_json_string(self):
        """creates a dict from json string"""
        dicRec = [
            {'width': 3, 'height': 4, 'id': 1},
            {'width': 8, 'height': 7, 'id': 2}
        ]
        jsonStr = Rectangle.to_json_string(dicRec)
        Exp = Rectangle.from_json_string(jsonStr)
        self.assertEqual(type(jsonStr), str)
        self.assertEqual(type(Exp), list)
        self.assertEqual(Exp, dicRec)

        dicSqr = [
            {'size': 3, 'id': 1},
            {'size': 8, 'id': 2}
        ]
        jsonSStr = Square.to_json_string(dicSqr)
        sExp = Square.from_json_string(jsonSStr)
        self.assertEqual(type(jsonSStr), str)
        self.assertEqual(type(sExp), list)
        self.assertEqual(sExp, dicSqr)

    def test_different_objects_same_value(self):
        """creates an object with dictionary keys and values"""
        rec1 = Rectangle(10, 3, 2, 1, 4)
        dic = rec1.to_dictionary()
        rec2 = Rectangle(**dic)
        self.assertNotEqual(rec1, rec2)

        sqr1 = Square(10, 3, 1, 4)
        _dic = sqr1.to_dictionary()
        sqr2 = Square(**_dic)
        self.assertNotEqual(sqr1, sqr2)

    def test_load_and_compare(self):
        """dump two objects to json file, then load them and compare"""
        sqr1 = Square(5)
        sqr2 = Square(7)
        ls_i = [sqr1, sqr2]
        Square.save_to_file(ls_i)
        ls_out = Square.load_from_file()
        self.assertNotEqual(ls_i, ls_out)

        rec1 = Rectangle(10, 7)
        rec2 = Rectangle(2, 4)
        ls = [rec1, rec2]
        Rectangle.save_to_file(ls)
        ls_o = Rectangle.load_from_file()
        self.assertNotEqual(ls, ls_o)

if __name__ == '__main__':
    unittest.main()
