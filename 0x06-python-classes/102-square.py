#!/usr/bin/python3
"""
Square Module
Defines a Square class that represents a square with a size and various methods.

"""


class Square:
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Checks if two Square instances are equal based on their area.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Checks if two Square instances are not equal based on their area.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.

        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Checks if the area of the current Square instance is less than
        the area of another Square instance.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area is less, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Checks if the area of the current Square instance is less than or equal to
        the area of another Square instance.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area is less than or equal, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Checks if the area of the current Square instance is greater than
        the area of another Square instance.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area is greater, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Checks if the area of the current Square instance is greater than or equal to
        the area of another Square instance.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
