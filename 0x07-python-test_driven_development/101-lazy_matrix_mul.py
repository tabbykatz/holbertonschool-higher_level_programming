#!/usr/bin/python3
"""the lazy_matrix_mul module"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Raises:
        TypeError: if either matrix != list , list of lists, if elements are
               not int or float, or inner lists are not of the same len
        ValueError: if lists are empty, or items cannot be multiplied
    Returns: the product matrix
    """

    a_list = True
    b_list = True
    aInner_list = True
    bInner_list = True
    a_same = True
    b_same = True
    a_number = True
    b_number = True
    a_contains = True
    b_contains = True
    a_inner_contains = True
    b_inner_contains = True
    mul = True

    if not isinstance(m_a, list):
        a_list = False
    if not isinstance(m_b, list):
        b_list = False
    if len(m_a) == 0:
        a_contains = False
    if len(m_b) == 0:
        b_contains = False

    for inner in m_a:
        if len(inner) == 0:
            a_inner_contains = False
        if not isinstance(inner, list):
            aInner_list = False
        if len(inner) != len(m_a[0]):
            a_same = False
        for item in inner:
            if not isinstance(item, int) and not isinstance(item, float):
                a_number = False

    for inner in m_b:
        if len(inner) == 0:
            b_inner_contains = False
        if not isinstance(inner, list):
            bInner_list = False
        if len(inner) != len(m_b[0]):
            b_same = False
        for item in inner:
            if not isinstance(item, int) and not isinstance(item, float):
                b_number = False

    if not a_list:
        raise TypeError('not sure what Guillaume meant by new message')
    if not b_list:
        raise TypeError('not sure what Guillaume meant by new message')
    if not aInner_list:
        raise TypeError('not sure what Guillaume meant by new message')
    if not bInner_list:
        raise TypeError('not sure what Guillaume meant by new message')
    if not a_contains:
        raise ValueError('not sure what Guillaume meant by new message')
    if not b_contains:
        raise ValueError('not sure what Guillaume meant by new message')
    if not a_inner_contains:
        raise ValueError('not sure what Guillaume meant by new message')
    if not b_inner_contains:
        raise ValueError('not sure what Guillaume meant by new message')
    if not a_number:
        raise TypeError('not sure what Guillaume meant by new message')
    if not b_number:
        raise TypeError('not sure what Guillaume meant by new message')
    if not a_same:
        raise TypeError('not sure what Guillaume meant by new message')
    if not b_same:
        raise TypeError('not sure what Guillaume meant by new message')
    if len(m_a[0]) != len(m_b):
        mul = False
    if not mul:
        raise ValueError('m_a and m_b can\'t be multiplied')

    return numpy.matrix(m_a) * numpy.matrix(m_b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
