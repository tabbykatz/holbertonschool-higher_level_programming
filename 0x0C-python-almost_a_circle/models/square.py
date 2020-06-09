#!/usr/bin/python3
'''Square class module - test located in tests/test_square/py'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''my Square class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''init magic'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''str info about a square'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''get size of a square'''
        return self.width

    @size.setter
    def size(self, value):
        '''set size of a square'''
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''updates instance attr via */**args'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''updates instance attr via */** args'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''dictionary rep of a class'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
