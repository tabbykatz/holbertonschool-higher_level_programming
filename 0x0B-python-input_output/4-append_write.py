#!/usr/bin/python3
"""module for append_write"""


def append_write(filename="", text=""):
    """to append text to file"""
    with open(filename, "a", encoding="utf-8") as content:
        return content.write(text)
