#!/usr/bin/python3
"""student class module"""


class Student:
    """a class we shall json"""
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get dict, names if only string"""
        if type(attrs) is list and all([type(a) == str for a in attrs]):
            return {name: value for name, value in self.__dict__.items()
                    if name in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        '''gets dict attr from json.'''
        for key, value in json.items():
            self.__dict__[key] = value
