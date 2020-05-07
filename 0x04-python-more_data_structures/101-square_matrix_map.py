#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda inside: list(map(lambda item: item**2, inside)),
        matrix))

