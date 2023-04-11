#!/usr/bin/python3
"""
This module provides one function:
    lookup(obj)
"""


def lookup(obj):
    """
    Function that retrieves the list of available attributes
     and methods of an object

    Attrs:
        obj: Object whose attributes and methods are required

    Returns:
        A list of attributes and methods of obj
    """
    return dir(obj)


if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3

        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
