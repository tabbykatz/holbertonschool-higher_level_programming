#!/usr/bin/python3
"""class Rectangle module - no test cases needed"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """is a sublass of Rectangle"""
    def __init__(self, size):
        """init method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """get the area of square"""
        return self.__size * self.__size

    def __str__(self):
        """to return the string rep of square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
