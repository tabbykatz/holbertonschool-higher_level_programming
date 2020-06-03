#!/usr/bin/python3
"""modue for p_tri"""


def pascal_triangle(n):
    """returns p tri for n"""
    horiz = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            horiz[n][i + 1] = sum(horiz[n - 1][i:i + 2])
    return horiz
