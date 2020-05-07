#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda v: v if v != search else replace, my_list))
