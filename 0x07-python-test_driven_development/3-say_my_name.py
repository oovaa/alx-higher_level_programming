#!/usr/bin/python3
"""the say my name mod
task 2"""


def say_my_name(first_name, last_name=""):
    """the say my name  func"""
    if type(first_name) is not str:

        raise TypeError("first_name must be a string")

    if type(last_name) is not str:

        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
