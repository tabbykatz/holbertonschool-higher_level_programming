#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """insert text after search string."""
    lines = []
    with open(filename, "r", encoding="utf-8") as content:
        getline = content.readlines()
        i = 0
        while i < len(getline):
            if search_string in getline[i]:
                getline[i:i + 1] = [getline[i], new_string]
                i += 1
            i += 1
    with open(filename, "w", encoding="utf-8") as content:
        content.writelines(getline)
