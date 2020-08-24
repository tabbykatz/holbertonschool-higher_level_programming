#!/usr/bin/python3
""" sends a request to the URL and displays the response with requests """
""" Uses requests module. Prddints error code"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    if response.status_code > 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
