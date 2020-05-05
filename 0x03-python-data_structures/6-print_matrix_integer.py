#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for inside in matrix:
        if len(inside) == 0:
            print()
        for i in range(len(inside)):
            print("{:d}".format(inside[i]),
                  end="\n" if i is len(inside) - 1 else " ")
