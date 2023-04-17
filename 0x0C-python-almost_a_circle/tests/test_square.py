#!/usr/bin/python3
"""
This "test_square.py" module defines one class:
    TestSquare: for testing the functionality of the Square class

Run as a module from project directory using:
$   python3 -m unittest ./tests/test_square.py
"""
import unittest

from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """
    Class for testing the functionality of the Square class

    Methods:
        tearDown: resets parameters at the end of tests
        test_init: tests square attributes setting
        test_setters: tests the validation of instance attribute setters
        test_str: tests the __str__ function of Square
        test_update: tests for update function of Square
        test_to_dictionary: tests for to_dictionary function of Square
    """

    def tearDown(self):
        """
        Runs at the end of each test to reset Base identifier count
        """
        Base._Base__nb_objects = 0
        return super().tearDown()

    def test_init(self):
        """
        Test for checking the setting of instance attributes
        """
        with self.assertRaises(
                TypeError,
                msg="Square should require 1 positional arguments"):
            Square()

        s1 = Square(4)
        self.assertEqual(
            s1.id, 1,
            "Square initializer should set id attribute to 1 for first object")
        self.assertEqual(
            s1.size, 4,
            "Square getter size should return height or width (4)")
        self.assertEqual(
            s1.width, 4,
            "Square initializer should set height attribute as passed (4)")
        self.assertEqual(
            s1.height, 4,
            "Square initializer should set height attribute as passed (4)")
        self.assertEqual(
            s1.x, 0,
            "Square initializer should have default x attribute as 0")
        self.assertEqual(
            s1.y, 0,
            "Square initializer should have default y attribute as 0")

        s2 = Square(5)
        self.assertEqual(
            s2.id, 2,
            "Square initializer should set id attribute to 2 for 2nd object")

        s3 = Square(2, 5, 6, 12)
        self.assertEqual(
            s3.id, 12,
            "Square initializer should set id attribute as passed (12)")
        self.assertEqual(
            s3.x, 5,
            "Square initializer should set x attribute as passed (5)")
        self.assertEqual(
            s3.y, 6,
            "Square initializer should set y attribute as passed (6)")

    def test_setters(self):
        """
        Test for checking the validation of instance attributes
        """
        s1 = Square(10, 5, 6, 12)

        with self.assertRaises(
                ValueError,
                msg="Square size should be greater than 0"):
            s1.size = 0
        with self.assertRaises(
                ValueError,
                msg="Square size cannot be negative"):
            s1.size = -12
        with self.assertRaises(
                TypeError,
                msg="Square size must be an integer"):
            s1.size = 9.3
        with self.assertRaises(
                TypeError,
                msg="Square size must be an integer"):
            s1.size = "str"

        s1.x = 0
        self.assertEqual(
            s1.x, 0,
            "Square x attribute setter should allow 0")
        with self.assertRaises(
                ValueError,
                msg="Square attribute x cannot be negative"):
            s1.x = -12
        with self.assertRaises(
                TypeError,
                msg="Square attribute x must be an integer"):
            s1.x = 9.3
        with self.assertRaises(
                TypeError,
                msg="Square attribute x must be an integer"):
            s1.x = "str"

        s1.y = 0
        self.assertEqual(
            s1.y, 0,
            "Square y attribute setter should allow 0")
        with self.assertRaises(
                ValueError,
                msg="Square attribute y cannot be negative"):
            s1.y = -12
        with self.assertRaises(
                TypeError,
                msg="Square attribute y must be an integer"):
            s1.y = 9.3
        with self.assertRaises(
                TypeError,
                msg="Square attribute y must be an integer"):
            s1.y = "str"

    def test_str(self):
        """
        Test for __str__ function of Square
        """
        s1 = Square(6, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 6")

        s2 = Square(5, 1)
        self.assertEqual(s2.__str__(), "[Square] (1) 1/0 - 5")

    def test_update(self):
        """
        Test for update function of Square
        """
        s1 = Square(2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

        s1.update(6, 8, 9, 0)
        self.assertEqual(s1.id, 6)
        self.assertEqual(s1.width, 8)
        self.assertEqual(s1.height, 8)
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.x, 9)
        self.assertEqual(s1.y, 0)

        s1.update(1, size=2, x=4, y=5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 8)
        self.assertEqual(s1.height, 8)
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.x, 9)
        self.assertEqual(s1.y, 0)

        s1.update(x=4, size=3, y=5, id=6)
        self.assertEqual(s1.id, 6)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.height, 3)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)

    def test_to_dictionary(self):
        """
        Test for to_dictionary function of Square
        """
        s1 = Square(2, 4, 5)
        d1 = {"id": 1, "size": 2, "x": 4, "y": 5}
        self.assertDictEqual(s1.to_dictionary(), d1)

        s2 = Square(3)
        d2 = {"id": 2, "size": 3, "x": 0, "y": 0}
        self.assertDictEqual(s2.to_dictionary(), d2)
