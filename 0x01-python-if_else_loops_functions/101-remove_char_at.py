#!/usr/bin/python3
def remove_char_at(str, n):
    fixed_str = ""
    for i, letter in enumerate(str):
        if i != n:
            fixed_str += letter
    return fixed_str
