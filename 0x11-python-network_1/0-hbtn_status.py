#!/usr/bin/python3
""" a status module to fetch an url"""
from urllib.request import Request, urlopen


if __name == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as response:
        data = response.read().decode('utf-8')

    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
    print(f"\t- utf8 content: {data}")
