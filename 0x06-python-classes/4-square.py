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
        self.size = size

    @property
    def size(self):
        """
        Retrieves the private instance attribute size of a square instance

        Returns:
            The side length of the current square instance
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Sets the private instance attribute size checking its value

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
        Calculates the area of a square instance

        Returns:
            The area of the current square instance
        """
        return self.__size ** 2


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
