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
