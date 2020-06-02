#!/usr/bin/python3
"""MyList class module- test cases in tests/1-my_list.txt"""


class MyList(list):
    """my own class: MyList, inherits from list"""
    def print_sorted(self):
        """print sorted list method"""
        print(sorted(self))
