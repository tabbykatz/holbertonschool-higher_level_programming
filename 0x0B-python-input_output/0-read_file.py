#!/usr/bin/python3
"""my read_file module"""


def read_file(filename=""):
    """read from a file"""
    with open(filename, "r", encoding="utf-8") as content:
        text = content.read()
        print(text, end="")
