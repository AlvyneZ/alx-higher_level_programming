#!/usr/bin/python3
"""
0-add_integer module
Functions:
    add_integer: adds integers or integer-casted floats
"""


def add_integer(a, b=98):
    """
    Addition function for integers (or floats casted to integer)
    """
    if type(a) != int:
        if type(a) != float:
            raise TypeError("a must be an integer")
        a = int(a)
    if type(b) != int:
        if type(b) != float:
            raise TypeError("b must be an integer")
        b = int(b)
    return (a + b)


if __name__ == "__main__":
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
