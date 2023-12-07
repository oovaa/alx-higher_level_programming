#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        list_dictionaries = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        json_string = json.dumps(list_dictionaries)

        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(json_string)
