#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """
    Rectangle class representing a geometric rectangle.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): Width of the rectangle. Default is 0.
            height (int): Height of the rectangle. Default is 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): Width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): Height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Return perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def print(self):
        """Print the rectangle using '#' characters."""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        s = ""
        for i in range(self.__height):
            s += self.__width * "#"
            s += "\n"
        s = s[:-1]  # Remove the trailing newline character
        return s

    def __repr__(self):
        """
        Return a string representation of the rectangle for recreation.

        Returns:
            str: String representation of the rectangle for recreation.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(slef):
        print("Bye rectangle...")
