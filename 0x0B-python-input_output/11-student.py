#!/usr/bin/python3
"""student class module"""


class Student:
    """a class we shall json"""
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get dict"""
        return self.__dict__.copy()
