#!/usr/bin/python3
"""Defines a square class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Since a square is a rectangle with equal width and height, this class
    uses the same attributes as Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square's sides.
            x (int, optional): The x-coordinate of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the square. Defaults to 0.
            id (int, optional): The id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, size):
        """Get/set the size of the Square."""
        if not isinstance(size, int):
            raise TypeError("width must be an integer")

        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        ats = ["id", "size", "x", "y"]
        if args and args != []:
            for atr, value in zip(ats, args):
                setattr(self, atr, value)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        atrs_list = ["id", "x", "size", "y"]
        return {x: getattr(self, x) for x in atrs_list}
