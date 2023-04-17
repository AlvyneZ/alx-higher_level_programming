#!/usr/bin/python3
"""
This "square.py" module provides one class:
    Square(Rectangle)
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    Class that defines a square for storing dimensions and location

    Attrs:
        size: getter and setter for self.__width and self.__height

    Methods:
        update: Updates attributes of a square instance
        to_dictionary: converts an instance to dictionary
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializer for setting square dimensions and location

        Args:
            size (integer): side length of a square instance
            x (integer): Grid horizontal location of a rectangle instance
            y (integer): Grid vertical location of a rectangle instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Retrieves the private instance attribute width of a square instance

        Returns:
            The width of the current square instance
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Sets the private instance attributes height and width

        Args:
            size (integer): side length of the square instance
        """
        self.width = size
        self.height = size

    def __str__(self):
        """
        Returns a string representation of the square
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """
        Updater for setting square dimensions and location

        Args:
            args (tuple): positional arguments
            kwargs (dict): keyword arguments
        """
        if len(args) == 0 and kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.size = args[i]
            if i == 2:
                self.x = args[i]
            if i == 3:
                self.y = args[i]

    def to_dictionary(self):
        """
        Converts instance to dictionary of attributes
        """
        dict_rep = {}
        dict_rep["id"] = self.id
        dict_rep["size"] = self.size
        dict_rep["x"] = self.x
        dict_rep["y"] = self.y
        return dict_rep
