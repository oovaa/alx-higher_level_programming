#!/usr/bin/python3
"""class to json modual"""


def class_to_json(obj):
    """
    Convert the attributes of an object into a JSON string.

This function takes an object, accesses its `__dict__` attribute, and then
serializes that dictionary to a JSON-formatted string using `json.dumps`.
The `__dict__` attribute of the object contains all its instance attributes,
which this function will serialize. It's important to ensure that all the
attributes are serializable to JSON (e.g., they should be of types like
dict, list, str, int, float, bool, or None).

    Args:
obj (object): The object whose attributes are to be serialized.

    Returns:
str: A JSON string representing the serialized attributes of the object.
    """
    return obj.__dict__
