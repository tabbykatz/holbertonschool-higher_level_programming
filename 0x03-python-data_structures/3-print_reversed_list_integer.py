#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list)
    for i in reversed(range(i)):
        print("{:d}".format(my_list[i]))
