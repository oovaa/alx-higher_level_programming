#!/usr/bin/python3
"""dum docs
task 4
"""


def print_square(size):
    """the dum function"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    for x in range(size):
        print("#" * size)
