#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the body of the response checks for errors
"""
import sys
import urllib.error
import urllib.request

if __name__ == '__main__':

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('ascii'))
    except urllib.error.HTTPError as e:
        print("Error code : {}".format(e.code))
