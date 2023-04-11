#!/usr/bin/python3
"""
This "3-is_kind_of_class.py" module provides one function:
    is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """
    Function that checks if an object is an instance of the specified
     class or is an instance of a class derived from the specified class

    Attrs:
        obj: Object to be checked
        a_class: Specified Class of interest

    Returns:
        True if obj is an instance of a-class or of a class derived from it,
         False otherwise
    """
    return isinstance(obj, a_class)


if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
