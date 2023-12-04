#!/usr/bin/python3
"""a dum task"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class inherited (directly or indirectly).

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a class that inherited from a cls.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
