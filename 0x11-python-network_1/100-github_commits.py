#!/usr/bin/python3
"""
Listing the 10 most recent commits on a GitHub repository
"""

import sys
import requests

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])
    req = requests.get(url)
    commits = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
