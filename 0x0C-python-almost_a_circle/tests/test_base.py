#!/usr/bin/python3
"""
This "test_base.py" module defines one class:
    TestBase: for testing the functionality of the Base class

Run from project directory using:
$   python3 -m unittest ./tests/test_base.py
"""
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Class for testing the functionality of the Base class

    Methods:
        tearDown: resets parameters at the end of tests
        test_init: tests identifier incrementing and setting
        test_to_json_string: tests to_json_string method
        test_from_json_string: tests from_json_string method
        test_create: tests the create method
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

    def test_to_json_string(self):
        """
        Test for to_json_string method of Base class
        """
        self.assertEqual(
            Base.to_json_string(None),
            "[]",
            "converter should return a JSON of an empty list for None arg"
        )
        self.assertEqual(
            Base.to_json_string([]),
            "[]",
            "converter should return a JSON of an empty list for [] arg"
        )
        self.assertEqual(
            Base.to_json_string([{"a": 1, "b": 2}]),
            """[{"a": 1, "b": 2}]"""
        )
        self.assertEqual(
            Base.to_json_string([{"a": 1, "b": 2}, {"c": 3}]),
            """[{"a": 1, "b": 2}, {"c": 3}]"""
        )

    def test_from_json_string(self):
        """
        Test for from_json_string method of Base class
        """
        self.assertListEqual(
            Base.from_json_string(None),
            [],
            "converter should return an empty list for None arg"
        )
        self.assertListEqual(
            Base.from_json_string("[]"),
            [],
            "converter should return an empty list for [] arg"
        )
        self.assertListEqual(
            Base.from_json_string("""[{"a": 1, "b": 2}]"""),
            [{"a": 1, "b": 2}]
        )
        self.assertListEqual(
            Base.from_json_string("""[{"a": 1, "b": 2}, {"c": 3}]"""),
            [{"a": 1, "b": 2}, {"c": 3}]
        )

    def test_create(self):
        """
        Test for create method of Base class
        """
        r1 = Rectangle(1, 2, 3, 4)
        dr1 = r1.to_dictionary()
        r2 = Rectangle.create(**dr1)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertEqual(r1 == r2, False)
        self.assertEqual(r1 is r2, False)

        s1 = Square(1, 2, 3)
        ds1 = s1.to_dictionary()
        s2 = Square.create(**ds1)
        self.assertEqual(s1.__str__(), s2.__str__())
        self.assertEqual(s1 == s2, False)
        self.assertEqual(s1 is s2, False)
