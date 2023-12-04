#!/usr/bin/python3
"""Check if the provided object is exactly an instance of the"""


def is_kind_of_class(obj, a_class):
    """
    Check if the provided object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """

    return isinstance(obj, a_class)
