#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Return the print() and str() representation of the Rectangle.

        Returns:
            str: The string representation of the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Calculate the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """

        return self.__height * self.__width
