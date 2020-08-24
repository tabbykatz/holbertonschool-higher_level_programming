#!/usr/bin/python3
""" The Holberton School staff evaluates candidates applying for a back-end
position with multiple technical challenges, like this one: """
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
          .format(argv[2], argv[1])
    r = requests.get(url)
    n = 0
    for i in r.json():
        if n < 10:
            print("{}: {}".format(i.get("sha"),
                  i.get("commit").get("author").get("name")))
        n += 1
