#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter
as a parameter"""
import requests
import sys


if __name__ == "__main__":
    let = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {"q": let}
    req = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
