#!/usr/bin/python3
""" a Python script that takes 2 arguments and lists
10 commits (from the most recent to oldest) of a repository"""
import requests
import sys


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    req = requests.get(url)
    commit = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commit[i].get("sha"),
                commit[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
