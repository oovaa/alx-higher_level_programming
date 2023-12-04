#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
    Function that returns the list of available attributes  of an obj
    """
    return dir(obj)
