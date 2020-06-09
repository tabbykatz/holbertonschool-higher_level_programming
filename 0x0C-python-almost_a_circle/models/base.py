#!/usr/bin/python3
'''Base class module - tests located in test/test_base.py'''
from json import dumps
from json import loads
import csv


class Base:
    '''the Base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''init magic'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''__dict__ to json'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''retrieve __dict__ from json'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''put json object in a file'''
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") \
                as content:
            content.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        '''retrieve string from file and from jsonification'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as content:
            return [cls.create(**arg) for arg in
                    cls.from_json_string(content.read())]

    @classmethod
    def create(cls, **dictionary):
        '''loads an instance'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''makes object in csv file'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                             for obj in list_objs]
            else:
                list_objs = [[obj.id, obj.size, obj.x, obj.y]
                             for obj in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding="utf-8") as content:
            writer = csv.writer(content)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''retrieve an object from the csv file'''
        from models.rectangle import Rectangle
        from models.square import Square
        load = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as content:
            reader = csv.reader(content)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    string = {"id": row[0], "width": row[1], "height": row[2],
                              "x": row[3], "y": row[4]}
                else:
                    string = {"id": row[0], "size": row[1],
                              "x": row[2], "y": row[3]}
                load.append(cls.create(**string))
        return load
