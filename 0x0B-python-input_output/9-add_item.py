#!/usr/bin/python3
"""module for add_item"""
import json
import os.path
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

thing = "add_item.json"
json = []

if os.path.exists(thing):
    json = load_from_json_file(thing)

for arg in range(1, len(sys.argv)):
    json.append(sys.argv[arg])

save_to_json_file(json, thing)
