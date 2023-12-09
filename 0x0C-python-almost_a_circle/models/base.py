#!/usr/bin/python3
import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):

        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for obj in list_objs:

                if cls.__name__ == 'Rectangle':
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])

                elif cls.__name__ == 'Square':
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        objects = []

        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)

                for row in reader:

                    if cls.__name__ == 'Rectangle':
                        obj = cls(int(row[1]), int(row[2]), int(
                            row[3]), int(row[4]), int(row[0]))

                    elif cls.__name__ == 'Square':
                        obj = cls(int(row[1]), int(row[2]),
                                  int(row[3]), int(row[0]))

                    objects.append(obj)
        except FileNotFoundError:
            pass
        return objects
