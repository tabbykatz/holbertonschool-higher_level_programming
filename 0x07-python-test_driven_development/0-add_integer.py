#!/usr/bin/python3
"""add integer module"""


def add_integer(a, b=98):
    """adds 2 integers.

    Args:
        a: the first int
        b: the second int

    Raises:
        TypeError: if a or b are not int or float

    Returns:
        the sum of a and b
    """

    if type(a) not in (float, int):
        raise TypeError('a must be an integer')
    if type(b) not in (float, int):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
