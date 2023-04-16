#!/usr/bin/python3
"""
This "base.py" module defines one class:
    Base
"""


class Base:
    """
    Class that defines a base class to manage object identifiers

    Attrs:
        __nb_objects (integer): count of instantiated objects
        self.id (integer): identifier of a base instance
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
