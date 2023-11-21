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
        __init__(self, size=None): Initializes a new instance of the Square class.
    """

    def __init__(self, size=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to None.
        """
        if size is not None:
            self.__size = size
