#!/usr/bin/python3
"""
Module of class for defining a rectangle by its dimensions
    ie, width & height (with value checking)
"""


class Rectangle:
    """
    Class that defines a rectangle of integer value dimensions

    Attrs:
        self.__height (integer): height of a rectangle instance
        self.__width (integer): width of a rectangle instance
        height: getter and setter for self.__height
        width: getter and setter for self.__width
    """
    def __init__(self, width=0, height=0):
        """
        Initializer for setting rectangle dimensions

        Args:
            height (integer): height of a rectangle instance
            width (integer): width of a rectangle instance
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Retrieves the private instance attribute width of a rectangle instance

        Returns:
            The width of the current rectangle instance
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets the private instance attribute width checking its value

        Args:
            width (integer): width of the rectangle instance
        """
        if type(width) != int:
            raise(TypeError("width must be an integer"))
        if width < 0:
            raise(ValueError("width must be >= 0"))
        self.__width = width

    @property
    def height(self):
        """
        Retrieves the private instance attribute height of a rectangle instance

        Returns:
            The height of the current rectangle instance
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets the private instance attribute height checking its value

        Args:
            height (integer): height of the rectangle instance
        """
        if type(height) != int:
            raise(TypeError("height must be an integer"))
        if height < 0:
            raise(ValueError("height must be >= 0"))
        self.__height = height


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)