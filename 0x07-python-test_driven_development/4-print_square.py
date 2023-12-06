#!/usr/bin/python3
"""dum docs """


def print_square(size):
    """
    Print a square of a given size using the '#' character.

    Parameters:
    size (int): The size of the sides of the square. Must be a non-negative integer.

    Raises:
    TypeError: If 'size' is not an integer.
    ValueError: If 'size' is less than or equal to 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size <= 0:
        raise ValueError("size must be > 0")

    for x in range(size):
        print("#" * size)
