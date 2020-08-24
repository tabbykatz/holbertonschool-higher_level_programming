#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status with requests """
import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(response.text), response.text))
