#!/usr/bin/python3
"""
This "2-is_same_class.py" module provides one function:
    is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """
    Function that checks if an object is exactly an instance
     of the specified class

    Attrs:
        obj: Object to be checked
        a_class: Specified Class of interest

    Returns:
        True if obj is exactly an instance of a-class, False otherwise
    """
    return (type(obj) == a_class)


if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
