#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_value1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a_value2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b_value1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b_value2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a_value1 + b_value1, a_value2 + b_value2)
