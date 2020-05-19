#!/usr/bin/python3
"""My square module"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Create a Square

        Args:
            size: length of side

        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
