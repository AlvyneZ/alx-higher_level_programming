#!/usr/bin/python3
"""
This module "6-base_geometry.py" provides one class:
    BaseGeometry
"""


class BaseGeometry:
    """
    Class  that defines a BaseGeometry with an unimplemented
     method for area calculation

    Attrs:
        area: should be defined by derived classes
    """
    def area(self):
        """
        Raises an Exception (derived classes should override it)
        """
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
