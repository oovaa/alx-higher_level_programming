#!/usr/bin/python3
"""
Module to extend Python's built-in list functionality with additional
"""


class MyList(list):
    """
    A subclass of the standard Python list with enhanced printing
    """

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """
        Prints the elements of the list in a sorted order without altering
        """
        print(sorted(self))
