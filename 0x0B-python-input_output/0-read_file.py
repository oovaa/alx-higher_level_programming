#!/usr/bin/python3
"""
This module provides a function to read and print the contents of a text file.

The function reads the entire content of a file whose name is passed as an
argument and prints it to the standard output. It is assumed that the file
is encoded in UTF-8.
"""


def read_file(filename=""):
    """
    Read and print the content of a file.

    This function opens a file in read-only mode and prints its content to the
    standard output. It handles the file encoding as UTF-8, making it suitable
    for text files containing unicode characters.

    Args:
        filename (str): The name of the file to read. If not provided, defaults
                        to an empty string, which will cause an error.

    Returns:
        None: This function does not return any value. It prints the file content
              to the standard output.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
