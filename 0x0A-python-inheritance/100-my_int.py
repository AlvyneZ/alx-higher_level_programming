#!/usr/bin/python3
"""
This "100-my_int.py" module provides one class:
    MyInt(int)
"""


class MyInt(int):
    """
    Rebel derived class that inverts equality checks (== and !=)
    """

    def __init__(self, val):
        """
        Initializer for initializing MyInt class
        """
        super().__init__()
        super().__new__(int, val)

    def __new__(cls, value, *args, **kwargs):
        """
        For setting new value for integer
        """
        return super(cls, cls).__new__(cls, value)

    def __eq__(self, my_int):
        """
        Equality Checker
        """
        return super().__ne__(my_int)

    def __ne__(self, my_int):
        """
        Non Equality Checker
        """
        return super().__eq__(my_int)


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
