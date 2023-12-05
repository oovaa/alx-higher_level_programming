#!/usr/bin/python3
"""dum docs"""


import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.

    This function takes a string in JSON format and deserializes it into
    object (like a dictionary or a list, depending on the JSON structure
    the `json.loads` method from the Python standard library's `json

    Args:
        my_str (str): A string in JSON format to be deserialized.

    Returns:
        object: The Python object resulting from the deserialization
    """
    return json.loads(my_str)
