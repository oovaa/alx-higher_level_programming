#!/usr/bin/python3
"""Define a Square class representing a square.

This class includes methods for calculating the area, printing the square,
and providing a string representation.
"""


class Square:
    """Define a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Get/set the size of the square."""
        return self.__size

    @property
    def position(self):
        """Get/set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If the position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the '#' character."""
        if self.size == 0:
            print()
            return

        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)

    def __str__(self) -> str:
        """Return a string representation of the square."""
        result = ""

        if self.size == 0:
            return result

        for i in range(self.position[1]):
            result += "\n"

        for i in range(self.size):
            result += " " * self.position[0]
            result += "#" * self.size + "\n"

        return result.rstrip()
