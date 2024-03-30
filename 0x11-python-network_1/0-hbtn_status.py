#!/usr/bin/python3
""" a status module to fetch an url"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = Request(url)
    with urlopen(req) as response:
        data = response.read()

    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
    print(f"\t- utf8 content: {data.decode("utf-8")}")
