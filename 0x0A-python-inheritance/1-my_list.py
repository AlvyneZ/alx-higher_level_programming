#!/usr/bin/python3
"""
This "1-my_list.py" module provides one class:
    MyList(List)
"""


class MyList(list):
    """
    Class that adds sorted printing to lists

    Attrs:
        print_sorted(self): Prints elements of a list of integers
         in ascending order
    """

    def __init__(self, lis=[]):
        """
        Initializer for initializing base class
        """
        super().__init__(lis)

    def print_sorted(self):
        """
        Prints elements of a list of integers in ascending order
        """
        sList = self.copy()
        sList.sort()
        print(sList)
