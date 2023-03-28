#!/usr/bin/python3
"""
Module of class for defining a square by its size
"""


class Square:
    """
    Class that defines a square

    Attrs:
        self.__size: side length of a square instance
    """
    def __init__(self, size):
        """
        Initializer for setting square size

        Args:
            size: the length of the sides of the square
        """
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
