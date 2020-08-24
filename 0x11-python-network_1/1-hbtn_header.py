#!/usr/bin/python3
""" displays the value of the X-Request-Id variable found in the header """
import urllib.request as request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as result:
        info = result.info()
        print(info.get("X-Request-Id"))
