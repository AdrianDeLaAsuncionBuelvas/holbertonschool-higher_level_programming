#!/usr/bin/python3
"""Error code with requests Module"""
import requests
import sys

if __name__ == '__main__':
    """sends a request to the URL and displays the body of the response"""
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
