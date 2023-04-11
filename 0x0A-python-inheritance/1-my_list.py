#!/usr/bin/python3
"""
This module provides one class:
    MyList(List)
"""


class MyList(list):
    """
    Class that adds sorted printing to lists

    Attrs:
        print_sorted(self): Prints elements of a list of integers
         in ascending order
    """

    def __init__(self):
        """
        Initializer for initializing base class
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints elements of a list of integers in ascending order
        """
        print(sorted(self))
