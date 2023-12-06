#!/usr/bin/python3
"""dum modual 
task 5
"""


def text_indentation(text):
    """a function that prints a text with 2 new lines after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    
