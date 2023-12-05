#!/usr/bin/python3
"""
This module provides a function to write and print the contents of a text file.

The function writes the entire content of a file whose name is passed as an
argument and prints it to the standard output. It is assumed that the file
is encoded in UTF-8.
"""


def write_file(filename="", text=""):
    """
    Write text to a file.

    This function opens a file specified by `filename` and writes the provided
    `text` to it. If the file already exists, its content will be overwritten.
    The function assumes the file is encoded in UTF-8.

    Args:
        filename (str): The name of the file where the text will be writte
                If the filename is empty, a ValueError will be raised.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
