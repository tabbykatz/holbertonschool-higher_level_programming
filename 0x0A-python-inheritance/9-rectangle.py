#!/usr/bin/python3
"""module for Rectangle, class what inherits from BG - no test cases"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle is a subclass of BG"""
    def __init__(self, width, height):
        """init method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """str rep method for rectangle"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
