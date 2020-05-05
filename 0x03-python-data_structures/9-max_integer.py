#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return None
    else:
        new_list = my_list.copy()
        new_list.sort()
        return new_list[-1]
