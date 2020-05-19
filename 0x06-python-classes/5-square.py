#!/usr/bin/python3
"""My square module"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Create a Square

        Args: size: length of a side of Square
        """
        self.__size = size

    @property
    def size(self):
        """"The propery of size as the len of a side of Square

        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Get the area of a Square

        Returns: The size squared
        """
        return self.__size * self.__size

    def my_print(self):
        """print the square in #"""
        if self.size > 0:
            for l in range(self.size):
                for w in range(self.size):
                    print("#", end='')
                print()
        else:
            print()
