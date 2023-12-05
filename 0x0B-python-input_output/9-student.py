#!/usr/bin/python3

"""The Sitty Module.

This module defines the Student class,
which models a basic student with
attributes for first name, last name,
and age. It provides functionality
to represent the student's information in JSON format.
"""


class Student:
    """A class representing a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Convert the student's attributes to a dictionary.

    This method creates and returns a dictionary representation of the student,
    with keys for 'first_name', 'last_name', and 'age'.
    Returns:
            dict: A dictionary containing the student's attributes.
        """
        result = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return result
