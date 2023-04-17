#!/usr/bin/python3
"""
This "base.py" module defines one class:
    Base
"""
import json


class Base:
    """
    Class that defines a base class to manage object identifiers

    Attrs:
        __nb_objects (integer): count of instantiated objects
        self.id (integer): identifier of a base instance

    Methods:
        to_json_string: Coverts a list of dictionaries to a json string
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializer for setting base identifier

        Args:
            id (integer): identifier of a base instance
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Coverts a list of dictionaries to a json string

        Args:
            list_dictionaries: object to be converted

        Returns:
            json string representation of list of dicttionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Coverts a json string to a list of dictionaries

        Args:
            json_string: json string to be converted

        Returns:
            The original jsonified list of dictionaries
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Converts a dictionary to the corresponding class instance
        """
        from .rectangle import Rectangle
        from .square import Square

        if cls.__name__ == "Rectangle":
            obj = Rectangle(1, 1, id=100)
        elif cls.__name__ == "Square":
            obj = Square(1, id=100)
        else:
            obj = Base(id=100)
        obj.update(**dictionary)
        return obj
