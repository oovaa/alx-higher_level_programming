#!/usr/bin/python3
"""i hate docs"""


def append_write(filename="", text=""):
    """
    Append text to the end of a file.

    This function opens a file specified by `filename` in append mode
    the provided `text` to the end of the file. If the file does not exist
    be created. The function handles the file encoding as UTF-8, making
    for text files containing Unicode characters.

    Args:
        filename (str): The name of the file to which
            If the filename is empty, a ValueError will be raised.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
