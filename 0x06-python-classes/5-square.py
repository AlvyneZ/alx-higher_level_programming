#!/usr/bin/python3
"""
Module of class for defining a square by its size (with value checking)
"""


class Square:
    """
    Class that defines a square of integer value sides

    Attrs:
        self.__size (integer): side length of a square instance
        size: getter and setter for self.__size
        area: calculates the area of the current square instance
        my_print: prints out the current squarte instance
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

    def my_print(self):
        """
        Prints out the square in stdout with '#'
        """
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print("")


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
