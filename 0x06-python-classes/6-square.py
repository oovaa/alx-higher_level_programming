#!/usr/bin/python3

"""
This module contains the definition of the Square class.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): new instance of Square class.
        size (property): Getter for the size attribute.
        size (setter): Setter for the size attribute.
        position (property): Getter for the position attribute.
        position (setter): Setter for the position attribute.
        area(self): Calculates the area of the square.
        my_print(self): Prints the square with the '#' character.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): position of square. Defaults (0,0).
        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer, or if position is not tuple.
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The new position for the square.
        Raises:
            ValueError: If position is not a tuple of 2 positive integers.
            TypeError: If position is not a tuple.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
