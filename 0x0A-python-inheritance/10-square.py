#!/usr/bin/python3
"""
This module "10-square.py" provides one class:
    Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that defines a Square based on Rectangle

    Attrs:
        self.__size: square side length
    """
    def __init__(self, size: int) -> None:
        """
        Initializer for square instance
        Args:
            size (int): square's side length
        """
        super().integer_validator("size", size)

        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of a square instance

        Returns:
            The area of the current square instance
        """
        return self.__size ** 2


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
