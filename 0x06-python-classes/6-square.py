#!/usr/bin/python3
"""
Module of class for defining a square by its size (with value checking)
"""


class Square:
    """
    Class that defines a square of integer value sides

    Attributes:
        self.__size (integer): side length of a square instance
        self.__position (tuple of 2 integer): grid location of
            a square instance
        area: calculates the area of the current square instance
        my_print: prints out the current squarte instance
    
    Properties:
        size: getter and setter for self.__size
        position: getter and setter for self.__position
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializer for setting square size

        Args:
            size (integer): the length of the sides of the square
            position (tuple of 2 integer): grid location of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the private instance attribute position of a square instance

        Returns:
            The grid location of the current square instance
        """
        return self.__position

    @position.setter
    def position(self, position):
        """
        Sets the private instance attribute position checking its value

        Args:
            position (tuple of 2 integer): grid location of the square
        """
        if (type(position) != tuple) or (len(position) != 2) or\
                (type(position[0]) != int) or (position[0] < 0) or\
                (type(position[1]) != int) or (position[1] < 0):
            raise(TypeError("position must be a tuple of 2 positive integers"))
        self.__position = position

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
            return
        for y in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
