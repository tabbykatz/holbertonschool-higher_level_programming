#!/usr/bin/python3
"""module for lazy_matrix_mul"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """mul m_a by m_b
    Args:
        m_a: the first matrix
        m_b: the other matrix
    Returns:
        matrix: product
    Raises:
        TypeError: if m_a or m_b are not lists or not lists of lists
        ValueError: if m_a or m_b are empty or can't be multiplied
        TypeError: if m_a or m_b have non int/float or are not rect
    """
    m_a_notempty = True
    m_b_notempty = True
    m_a_rect = True
    m_b_rect = True
    m_a_num = True
    m_b_num = True
    m_a_notscalar = True
    m_b_notscalar = True

    for row in m_a:
        if not isinstance(row, list):
            m_a_notscalar = False
        if len(row) != len(m_a[0]):
            m_a_rect = False
        for num in row:
            if not isinstance(num, (int, float)):
                m_a_num = False

    for row in m_b:
        if not isinstance(row, list):
            m_b_notscalar = False
        if len(row) != len(m_b[0]):
            m_b_rect = False
        for num in row:
            if not isinstance(num, (int, float)):
                m_b_num = False

    if not m_a_notscalar:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if not m_b_notscalar:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if not m_a_num:
        raise TypeError("invalid data type for einsum")

    if not m_b_num:
        raise TypeError("invalid data type for einsum")

    if not m_a_rect:
        raise ValueError("setting an array element with a sequence.")

    if not m_b_rect:
        raise ValueError("setting an array element with a sequence.")

    return numpy.matrix(m_a) * numpy.matrix(m_b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
