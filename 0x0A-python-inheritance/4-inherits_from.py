#!/usr/bin/python3
"""
This "4-inherits_from.py" module provides one function:
    inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """
    Function that checks if an object is an instance of a
     class derived/inheriting from the specified class

    Attrs:
        obj: Object to be checked
        a_class: Specified Class of interest

    Returns:
        True if obj is an instance of a class derived from a_class,
         False otherwise
    """
    return isinstance(obj, a_class) and (type(obj) != a_class)


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
