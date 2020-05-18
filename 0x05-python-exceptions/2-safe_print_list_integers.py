#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    items = 0
    count = 0
    while items < x:
        try:
            print("{:d}".format(my_list[items]), end='')
            count = count + 1
        except TypeError:
            pass
        except ValueError:
            pass
        items = items + 1
    print()
    return count
