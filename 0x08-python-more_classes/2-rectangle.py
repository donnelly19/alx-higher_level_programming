#!/usr/bin/python3


""""defining the rectangle class"""


class Rectangle:

    """initializing the objects"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """retrieving the width property"""
    def width(self):
        return self.__width

    """setting the width"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """retrieving height property"""
    def height(self):
        return self.__height

    """setting the height"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """defining a public instance"""
    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
