#!/usr/bin/python3
"""module for save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON rep"""
    with open(filename, "w", encoding="utf=8") as content:
        json.dump(my_obj, content)
