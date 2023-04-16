#!/usr/bin/python3
"""
This "test_base.py" module defines one class:
    TestBase: for testing the functionality of the Base class

Run from project directory using:
$   python3 -m unittest ./tests/test_base.py
"""
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """
    Class for testing the functionality of the Base class

    Methods:
        tearDown: resets parameters at the end of tests
        test_init: tests identifier incrementing and setting
    """

    def tearDown(self):
        """
        Runs at the end of each test to reset Base identifier count
        """
        Base._Base__nb_objects = 0
        return super().tearDown()

    def test_init(self):
        """
        Test for checking the setting of instance id and incrementing
         of __nb_objects
        """
        b1 = Base()
        b2 = Base()
        b3 = Base(None)
        b4 = Base(12)
        b5 = Base("str")
        b6 = Base()
        b7 = Base([1, 2, 3])

        self.assertEqual(
            b1.id, 1,
            "initializer should set id of first object to 1")
        self.assertEqual(
            b2.id, 2,
            "initializer should increment id for subsequent objects")
        self.assertEqual(
            b3.id, 3,
            "initializer should increment id for subsequent objects")
        self.assertEqual(
            b4.id, 12,
            "initializer should set id with the provided value")
        self.assertEqual(
            b5.id, "str",
            "initializer should set id with the provided value")
        self.assertEqual(
            b6.id, 4,
            "initializer should increment id for subsequent objects")
        self.assertEqual(
            b7.id, [1, 2, 3],
            "initializer should set id with the provided value")
        self.assertEqual(
            Base._Base__nb_objects, 4,
            "Recorded number of objects should equal objects "
            "initialized with id not set")
