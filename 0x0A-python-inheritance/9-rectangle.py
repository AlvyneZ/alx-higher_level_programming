#!/usr/bin/python3
"""
This module "9-rectangle.py" provides one class:
    Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that defines a Rectangle based on Base Geometry

    Attrs:
        self.__width: rectangle width
        self.__height: rectangle height
    """
    def __init__(self, width, height):
        """
        Initializer for rectangle instance

        Args:
            width (int): rectangle's width
            height (int): rectangle's height
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of a rectangle instance

        Returns:
            The area of the current rectangle instance
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Converts the rectangle to a printable string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
