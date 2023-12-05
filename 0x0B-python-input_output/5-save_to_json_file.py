#!/usr/bin/python3
"""docs

"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object as a JSON file.

    This function serializes a Python object (`my_obj`) into a
    and writes it to a file specified by `filename`. The file will
    it already exists. The function assumes the file is encoded in UTF

        my_obj (object): The Python object to be serialized and saved
                         should be serializable to JSON (e.g., dict, list
                         int, float, bool
        filename (str): The name of the file where the JSON data will

    Returns:
        None: This function does not return any value.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
