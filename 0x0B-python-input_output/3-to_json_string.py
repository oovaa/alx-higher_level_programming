#!/usr/bin/python3
"""the dum docs"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object as a string.

    Args:
    my_obj (Any): The Python object to be converted to JSON string.

    Returns:
    str:
    """
    return json.dumps(my_obj)
