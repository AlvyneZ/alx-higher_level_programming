#!/usr/bin/python3
"""
This "test_rectangle.py" module defines one class:
    TestRectangle: for testing the functionality of the Rectangle class

Run as a module from project directory using:
$   python3 -m unittest ./tests/test_rectangle.py
"""
from io import StringIO

import unittest
from unittest.mock import patch

from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    Class for testing the functionality of the Rectangle class

    Methods:
        tearDown: resets parameters at the end of tests
        test_init: tests rectangle attributes setting
        test_setters: tests the validation of instance attribute setters
        test_area: tests the area function of Rectangle
        test_display: tests the display function of Rectangle
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
                msg="Rectangle should require 2 positional arguments"):
            Rectangle()

        r1 = Rectangle(10, 2)
        self.assertEqual(
            r1.id, 1,
            "Base initializer should set id attribute to 1 for first object")
        self.assertEqual(
            r1.width, 10,
            "Base initializer should set height attribute as passed (2)")
        self.assertEqual(
            r1.height, 2,
            "Base initializer should set height attribute as passed (10)")
        self.assertEqual(
            r1.x, 0,
            "Base initializer should have default x attribute as 0")
        self.assertEqual(
            r1.y, 0,
            "Base initializer should have default y attribute as 0")

        r2 = Rectangle(2, 10)
        self.assertEqual(
            r2.id, 2,
            "Base initializer should set id attribute to 2 for second object")

        r3 = Rectangle(10, 2, 5, 6, 12)
        self.assertEqual(
            r3.id, 12,
            "Base initializer should set id attribute as passed (12)")
        self.assertEqual(
            r3.x, 5,
            "Base initializer should set x attribute as passed (5)")
        self.assertEqual(
            r3.y, 6,
            "Base initializer should set y attribute as passed (6)")

    def test_setters(self):
        """
        Test for checking the validation of instance attributes
        """
        r1 = Rectangle(10, 2, 5, 6, 12)

        with self.assertRaises(
                ValueError,
                msg="Rectangle width should be greater than 0"):
            r1.width = 0
        with self.assertRaises(
                ValueError,
                msg="Rectangle width cannot be negative"):
            r1.width = -12
        with self.assertRaises(
                TypeError,
                msg="Rectangle width must be an integer"):
            r1.width = 9.3
        with self.assertRaises(
                TypeError,
                msg="Rectangle width must be an integer"):
            r1.width = "str"

        with self.assertRaises(
                ValueError,
                msg="Rectangle height should be greater than 0"):
            r1.height = 0
        with self.assertRaises(
                ValueError,
                msg="Rectangle height cannot be negative"):
            r1.height = -12
        with self.assertRaises(
                TypeError,
                msg="Rectangle height must be an integer"):
            r1.height = 9.3
        with self.assertRaises(
                TypeError,
                msg="Rectangle height must be an integer"):
            r1.height = "str"

        r1.x = 0
        self.assertEqual(
            r1.x, 0,
            "Rectangle x attribute setter should allow 0")
        with self.assertRaises(
                ValueError,
                msg="Rectangle attribute x cannot be negative"):
            r1.x = -12
        with self.assertRaises(
                TypeError,
                msg="Rectangle attribute x must be an integer"):
            r1.x = 9.3
        with self.assertRaises(
                TypeError,
                msg="Rectangle attribute x must be an integer"):
            r1.x = "str"

        r1.y = 0
        self.assertEqual(
            r1.y, 0,
            "Rectangle y attribute setter should allow 0")
        with self.assertRaises(
                ValueError,
                msg="Rectangle attribute y cannot be negative"):
            r1.y = -12
        with self.assertRaises(
                TypeError,
                msg="Rectangle attribute y must be an integer"):
            r1.y = 9.3
        with self.assertRaises(
                TypeError,
                msg="Rectangle attribute y must be an integer"):
            r1.y = "str"

    def test_area(self):
        """
        Test for area function of Rectangle
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """
        Test for display function of Rectangle
        """
        with patch("sys.stdout", StringIO()) as Screen:
            r1 = Rectangle(2, 4)
            r1.display()
            self.assertEqual(
                Screen.getvalue(), "##\n##\n##\n##\n")

        with patch("sys.stdout", StringIO()) as Screen:
            r1 = Rectangle(2, 4, 1, 3, 12)
            r1.display()
            self.assertEqual(
                Screen.getvalue(), "\n\n\n ##\n ##\n ##\n ##\n")
