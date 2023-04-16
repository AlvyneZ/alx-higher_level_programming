#!/usr/bin/python3
"""
This "rectangle.py" module provides one class:
    Rectangle
"""
from .base import Base


class Rectangle(Base):
    """
    Class that defines a rectangle for storing dimensions and location

    Attrs:
        self.__height (integer): height of a rectangle instance
        self.__width (integer): width of a rectangle instance
        self.__x (integer): Grid horizontal location of a rectangle instance
        self.__y (integer): Grid vertical location of a rectangle instance
        height: getter and setter for self.__height
        width: getter and setter for self.__width
        x: getter and setter for self.__x
        y: getter and setter for self.__y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializer for setting rectangle dimensions and location

        Args:
            height (integer): height of a rectangle instance
            width (integer): width of a rectangle instance
            x (integer): Grid horizontal location of a rectangle instance
            y (integer): Grid vertical location of a rectangle instance
        """
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    def pos_int_validator(self, name, value):
        """
        Ensures a value for an argument "name" is a positive integer

        Args:
            name (string): name of the argument being validated
            value (integer): value provided
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def pos_nz_int_validator(self, name, value):
        """
        Ensures a value for an argument "name" is a positive non-zero integer

        Args:
            name (string): name of the argument being validated
            value (integer): value provided
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

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
        Sets the private instance attribute width with validation (>= 0)

        Args:
            width (integer): width of the rectangle instance
        """
        self.pos_nz_int_validator("width", width)
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
        Sets the private instance attribute height with validation (>= 0)

        Args:
            height (integer): height of the rectangle instance
        """
        self.pos_nz_int_validator("height", height)
        self.__height = height

    @property
    def x(self):
        """
        Retrieves the private instance attribute x of a rectangle instance

        Returns:
            The horizontal grid location of the current rectangle instance
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Sets the private instance attribute x with validation (> 0)

        Args:
            x (integer): Grid horizontal location of the rectangle instance
        """
        self.pos_int_validator("x", x)
        self.__x = x

    @property
    def y(self):
        """
        Retrieves the private instance attribute y of a rectangle instance

        Returns:
            The vertical grid location of the current rectangle instance
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Sets the private instance attribute y with validation (> 0)

        Args:
            x (integer): Grid vertical location of the rectangle instance
        """
        self.pos_int_validator("y", y)
        self.__y = y
