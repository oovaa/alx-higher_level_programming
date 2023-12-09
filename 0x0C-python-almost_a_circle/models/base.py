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
        list_dictionaries = [obj.to_dictionary()
                             for obj in list_objs] if list_objs else []
        json_string = json.dumps(list_dictionaries)

        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        return [] if json_string is None or len(json_string) == 0 \
            else json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of cls with attributes set from a dictionary.

        Args:
            **dictionary: A dictionary of attributes to set on the instance.

        Returns:
            An instance of cls with attributes set according to the dictionary.
        """
        # Assuming the first two arguments of the constructor are
        # mandatory like width and height.
        # These will be overwritten by the dictionary values.
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"

        with open(filename, "r") as fh:
            dicslist = json.load(fh)

        instaces_list = [cls.create(**x) for x in dicslist]

        return instaces_list
