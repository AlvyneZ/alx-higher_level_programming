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

    def __eq__(self, other):
        """
        Checks for equality between squares based on area when '==' is used
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks for inequality between squares based on area when '!=' is used
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparison between squares based on area when '<' is used
        """
        return self.area() < other.area()

    def __gt__(self, other):
        """
        Greater than comparison between squares based on area when '>' is used
        """
        return self.area() > other.area()

    def __le__(self, other):
        """
        Less/equal comparison between squares based on area when '<=' is used
        """
        return self.area() <= other.area()

    def __ge__(self, other):
        """
        Greatr/equal comparison between squares based on area when '>=' is used
        """
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
