#!/usr/bin/python3
""" a status module to fetch an url"""
import urllib.request


if __name__ == "__main__":
    req = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')

    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
    print(f"\t- utf8 content: {data}")
