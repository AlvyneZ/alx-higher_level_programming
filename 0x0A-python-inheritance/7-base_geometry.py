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


if __name__ == "__main__":
    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
