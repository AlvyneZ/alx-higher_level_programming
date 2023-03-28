#!/usr/bin/python3
"""
Module of class for defining a square by its size (with value checking)
"""


class Square:
    """
    Class that defines a square of integer value sides

    Attrs:
        self.__size (integer): side length of a square instance
        area: calculates the area of the current square instance
    """
    def __init__(self, size=0):
        """
        Initializer for setting square size

        Args:
            size (integer): the length of the sides of the square
        """
        if type(size) != int:
            raise(TypeError("size must be an integer"))
        if size < 0:
            raise(ValueError("size must be >= 0"))
        self.__size = size

    def area(self):
        """
        Calculates the area of the current square instance

        Returns:
            The area of the square
        """
        return self.__size ** 2


if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
