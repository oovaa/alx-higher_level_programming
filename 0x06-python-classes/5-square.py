#!/usr/bin/python3

"""
This module contains the definition of the Square class.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
        size (property): Getter for the size attribute.
        size (setter): Setter for the size attribute.
        area(self): Calculates the area of the square.
        my_print(self): Prints the square with the '#' character.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        self.__size = size

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size for the square.
        Raises:
            ValueError: If value is less than 0.
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the '#' character.
        """
        if self.size == 0:
            print()
            return

        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
