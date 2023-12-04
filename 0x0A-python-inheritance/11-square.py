#!/usr/bin/python3
"""Defines a base geometry class Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the Square.

        Returns:
            int: The area of the Square.
        """

        return self.__size ** 2

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    def print(self):
        """
        Print the string representation of the Square.

        This method prints the square's details. It's an additional method for
        and utilizes the __str__ method for its output.
        """
        print(self.__str__())
