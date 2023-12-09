#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)  # Calling the constructor of Base
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
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
        return self.width * self.height

    def display(self):
        print(self.y * "\n", end="")

        for i in range(self.height):
            print(self.x * " " + "#" * self.width)

    def __str__(self) -> str:
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        attributes = ['id', 'width', 'height', 'x', 'y']

        if args:
            for attr, arg in zip(attributes, args):
                setattr(self, attr, arg)
        else:
            for attr in kwargs:
                if attr in attributes:
                    setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        atrs_list = ["x", "y", "id", "height", "width"]
        return {x: getattr(self, x) for x in atrs_list}
