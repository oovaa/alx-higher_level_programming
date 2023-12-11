#!/usr/bin/python3
"""Defines a base model class."""

import json
import csv
import turtle as tr


class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """

        return json.dumps(list_dictionaries) if list_dictionaries \
            is not None else "[]"

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """

        return [] if json_string is None or len(json_string) == 0 \
            else json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = cls.__name__ + ".json"

        if list_objs is None:
            # If list_objs is None, write an empty list as JSON string.
            json_string = "[]"
        else:
            # Convert list_objs to a list of dictionaries
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            # Convert list of dictionaries to JSON string
            json_string = cls.to_json_string(list_dictionaries)

        with open(filename, "w") as f:
            f.write(json_string)

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """

        filename = cls.__name__ + ".json"
        instances_list = []

        try:
            with open(filename, "r") as fh:
                # This is a list of dictionaries
                dicts_list = json.load(fh)
                # Create instances from dictionaries
                instances_list = [cls.create(**d) for d in dicts_list]
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist, we can either pass,
            # return an empty list,
            # or perhaps even create the file. For now, we'll
            # just return an empty list.
            return []

        return instances_list

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of cls with attributes set from a dictionary.

        Args:
            **dictionary: A dictionary of attributes to set on the instance.

        Returns:
            An instance of cls with attributes set according to the dictionary.
        """
        # Creating a "dummy" instance with default values.
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            # Handle other potential subclasses or raise an error.
            raise TypeError("Unknown class")

        # Updating the dummy instance with actual values.
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """

        filename = cls.__name__ + ".csv"

        if not list_objs:  # If the list is empty
            with open(filename, 'w', newline='') as csvfile:
                csvfile.write("[]")
        else:
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
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        objects = []

        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)

                obj = None
                for row in reader:

                    if cls.__name__ == 'Rectangle':
                        if len(row) == 5:
                            obj = cls(int(row[1]), int(row[2]), int(
                                row[3]), int(row[4]), int(row[0]))

                    elif cls.__name__ == 'Square':
                        if len(row) == 4:
                            obj = cls(int(row[1]), int(row[2]),
                                      int(row[3]), int(row[0]))

                    objects.append(obj)
        except FileNotFoundError:
            return []
        return objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        screen = tr.Screen()
        turtle = tr.Turtle()

        # Draw squares
        for square in list_squares:
            turtle.penup()
            # Move to the starting position of the square
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)

        # Separate the drawing of rectangles and squares by a gap
        turtle.penup()
        turtle.goto(200, 0)  # This is an arbitrary gap; adjust as needed
        turtle.pendown()

        # Draw rectangles
        for rec in list_rectangles:
            turtle.penup()
            # Move to the starting position of the rectangle
            turtle.goto(rec.x, rec.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rec.width)
                turtle.right(90)
                turtle.forward(rec.height)
                turtle.right(90)

        tr.done()
