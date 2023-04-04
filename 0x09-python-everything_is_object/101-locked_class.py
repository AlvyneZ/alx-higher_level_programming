#!/usr/bin/python3
"""
101-locked_class module
Class:
    LockedClass: allows instantiating of only one instance attribute
"""


class LockedClass:
    """
    Class that allows instantiating of only one instance attribute,
        first_name
    """

    __slots__ = ["first_name"]


if __name__ == "__main__":
    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
