#!/usr/bin/python3
"""rec model"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
        id (int): The id of the rectangle (inherited from Base).
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): The id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        """
        Set the x-coordinate of the rectangle.

        Args:
            x (int): The new x-coordinate.

        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is negative.
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    # Similar docstrings can be added for the other properties and their setters.

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Print the rectangle using the '#' character.

        The rectangle is offset by its x and y coordinates.
        """
        print(self.y * "\n", end="")
        for i in range(self.height):
            print(self.x * " " + "#" * self.width)

    def __str__(self) -> str:
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args can be used to update attributes in the following order:
        id, width, height, x, y.

        Kwargs can be used to update attributes by name.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        for attr, arg in zip(attributes, args):
            setattr(self, attr, arg)

        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
