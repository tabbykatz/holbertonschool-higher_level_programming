#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    items = 0
    try:
        while items is not x:
            print(my_list[items], end='')
            items = items + 1
    except IndexError:
        None
    print()
    return items
