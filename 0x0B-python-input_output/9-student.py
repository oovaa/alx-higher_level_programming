#!/usr/bin/python3

"""the sitty modual"""


class Student:
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        result = dict()
        result["first_name"] = self.first_name
        result["last_name"] = self.last_name
        result["age"] = self.age
        return result
