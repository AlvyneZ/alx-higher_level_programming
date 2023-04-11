#!/usr/bin/python3
"""
This module "7-base_geometry.py" provides one class:
    BaseGeometry
"""


class BaseGeometry:
    """
    Class that defines a BaseGeometry

    Attrs:
        area(): should be defined by derived classes
        integer_validator(name, value): Validates a value confirming
         it's an integer
    """
    def __init__(self):
        """
        Empty Initializer for base class
        """
        super().__init__()

    def area(self):
        """
        Raises an Exception (derived classes should override it)
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Ensures a value for an argument "name" is an integer

        Args:
            name (string): name of the argument being validated
            value (integer): value provided
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
