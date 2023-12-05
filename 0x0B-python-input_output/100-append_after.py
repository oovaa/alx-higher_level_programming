#!/usr/bin/python3

"""Advanced Task 13"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file, after each line containing
    a specific string (see example):
    """
    if not filename:
        return

    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
