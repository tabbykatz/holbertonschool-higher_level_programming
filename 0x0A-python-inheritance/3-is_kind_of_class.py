#!/usr/bin/python3
"""is kind of class module - no test cases needed"""


def is_kind_of_class(obj, a_class):
    """checks if obj is of a sublass of a_class
    Args:
        obj: the object
        a_class: the class we are checking it for
    """
    return isinstance(obj, a_class)
