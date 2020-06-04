#!/usr/bin/python3
"""the matrix_mul module"""


def matrix_mul(m_a, m_b):
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
    if not a_list:
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        b_list = False
    if not b_list:
        raise TypeError('m_b must be a list')

    if len(m_a) == 0:
        a_contains = False
    if len(m_b) == 0:
        b_contains = False

    for inner in m_a:
        if not isinstance(inner, list):
            aInner_list = False
            raise TypeError('m_a must be a list of lists')
        if len(inner) == 0:
            a_inner_contains = False
            raise TypeError('m_a can\'t be empty')
        if len(inner) != len(m_a[0]):
            a_same = False
        for item in inner:
            if not isinstance(item, int) and not isinstance(item, float):
                a_number = False

    for inner in m_b:
        if not isinstance(inner, list):
            bInner_list = False
            raise TypeError('m_b must be a list of lists')
        if len(inner) == 0:
            b_inner_contains = False
            raise ValueError('m_b can\'t be empty')
        if len(inner) != len(m_b[0]):
            b_same = False
        for item in inner:
            if not isinstance(item, int) and not isinstance(item, float):
                b_number = False

    if not aInner_list:
        raise TypeError('m_a must be a list of lists')
    if not bInner_list:
        raise TypeError('m_b must be a list of lists')
    if not a_contains:
        raise ValueError('m_a can\'t be empty')
    if not b_contains:
        raise ValueError('m_b can\'t be empty')
    if not a_inner_contains:
        raise ValueError('m_a can\'t be empty')
    if not b_inner_contains:
        raise ValueError('m_b can\'t be empty')
    if not a_number:
        raise TypeError('m_a should contain only integers or floats')
    if not b_number:
        raise TypeError('m_b should contain only integers or floats')
    if not a_same:
        raise TypeError('each row of m_a must be of the same size')
    if not b_same:
        raise TypeError('each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        mul = False
    if not mul:
        raise ValueError('m_a and m_b can\'t be multiplied')

    product = [[] for item in range(len(m_a))]

    for item in range(len(m_a)):
        for item2 in range(len(m_b[0])):
            answer = 0
            for span in range(len(m_b)):
                answer += m_a[item][span] * m_b[span][item2]
            product[item].append(answer)

    return product

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
