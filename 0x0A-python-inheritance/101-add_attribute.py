#!/usr/bin/python3
"""this is my module for add_attribute"""


def add_attribute(obj, name, value):
    """see if i can add attribute"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    elif hasattr(obj, "__slots__") and name in obj.__slots__:
        setattr(obj, name, value)
    else:
        raise TypeError('can\'t add new attribute')
