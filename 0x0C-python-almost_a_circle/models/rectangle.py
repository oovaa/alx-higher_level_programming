#!/usr/bin/python3
"""Defines a rectangle class."""


from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)  # Calling the constructor of Base
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @x.setter
    def x(self, x):
        if not isinstance(x, int) or isinstance(x, bool):
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @width.setter
    def width(self, width):
        if not isinstance(width, int) or isinstance(width, bool):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        print(self.y * "\n", end="")
        for i in range(self.height):
            print(self.x * " " + "#" * self.width)

    def __str__(self) -> str:
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        attributes = ['id', 'width', 'height', 'x', 'y']

        if args:
            for attr, arg in zip(attributes, args):
                setattr(self, attr, arg)
        else:
            for attr in kwargs:
                if attr in attributes:
                    setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        atrs_list = ["x", "y", "id", "height", "width"]
        return {x: getattr(self, x) for x in atrs_list}
