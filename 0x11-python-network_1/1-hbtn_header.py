#!/usr/bin/python3
"""  a Python script that takes in a URL, sends a
request to the URL and displays the value of the
X-Request-Id variable found in the header of the response"""
from urllib.request import Request, urlopen
import sys


if __name == "__main__":
    url = sys.argv[1]
    req = Request(url)
    with urlopen(req) as response:
        data = r.headers.get("X-Request-Id")
        print(data)
