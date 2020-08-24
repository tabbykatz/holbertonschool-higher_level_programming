#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter, and
displays the body of the response """
import urllib.parse as parse
import urllib.request as request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({"email": email}).encode("ascii")
    do = request.Request(url, data)
    with request.urlopen(do) as result:
        print(result.read().decode("utf-8"))
