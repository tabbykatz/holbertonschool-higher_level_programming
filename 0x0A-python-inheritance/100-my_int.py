#!/usr/bin/python3
"""module for MyInt, a class - non test cases needed"""


class MyInt(int):
    """my int"""
    def __eq__(self, other):
        """myint is a rebel, eq is !="""
        return int(self) != int(other)

    def __ne__(self, other):
        """myint is a rebel, ne is =="""
        return int(self) == int(other)
