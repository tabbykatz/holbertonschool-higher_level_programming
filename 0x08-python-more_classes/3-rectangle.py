#!/usr/bin/python3
"""my rectangle module"""


class Rectangle:
    """defines the rectangle"""

    def __init__(self, width=0, height=0):
        """init rectangle
        Args:
            width: the width
            height: the height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """the property of width as one side of a rectangle
        Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width
        Args:
            value: to set the width to
        Raises:
            TypeError: if width is not int
            ValueError: if width < 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """the property of height as another side of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height
        Args:
            value: to set the height to
        Raises:
            TypeError: if value is not int
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """return the string rep of rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return (("#" * self.width + "\n") * self.height)[:-1]
