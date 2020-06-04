#!/usr/bin/python3
"""read_lines module"""


def read_lines(filename="", nb_lines=0):
    """to read n lines from file, print entire thing if n <= 0 or > file"""
    with open(filename, "r", encoding="utf-8") as content:
        if not nb_lines:
            print(content.read(), end="")
            return
        for eachline in content:
            print(eachline, end="")
            nb_lines -= 1
            if not nb_lines:
                break
