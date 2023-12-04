#!/usr/bin/python3

def add_attribute(obj, name, value):
    """
    Add a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute should be added.
        name: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
