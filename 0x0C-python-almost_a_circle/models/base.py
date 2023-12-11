#!/usr/bin/python3
import json
import csv
import turtle as tr


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries) if list_dictionaries \
            is not None else "[]"

    @staticmethod
    def from_json_string(json_string):
        return [] if json_string is None or len(json_string) == 0 \
            else json.loads(json_string)

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

    @classmethod
    def load_from_file(cls):
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
        # Assuming the first two arguments of the constructor are
        # mandatory like width and height.
        # These will be overwritten by the dictionary values.
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):

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

    @staticmethod
    def draw(list_rectangles, list_squares):
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
