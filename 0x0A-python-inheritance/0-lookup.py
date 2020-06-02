#!/usr/bin/python3
"""lookup method module - no test cases needed"""


def lookup(obj):
    """looks up the attr and methods of an object
    Args:
        obj: the object we are looking up
    Returns:
        a list object of attr"""
    return dir(obj)
