#!/usr/bin/python3
"""
This "test_rectangle.py" module defines one class:
    TestRectangle: for testing the functionality of the Rectangle class

Run as a module from project directory using:
$   python3 -m unittest ./tests/test_rectangle.py
"""
import unittest

from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    Class for testing the functionality of the Rectangle class

    Methods:
        tearDown: resets parameters at the end of tests
        test_init: tests rectangle attributes setting
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
